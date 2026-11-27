"""BarakaSocial update helper. Standard library; local files only change after approval."""
import argparse
from contextlib import contextmanager
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile
import time
import urllib.request
import uuid
import zipfile

REPOSITORY = "https://github.com/kconde2/barakasocial-linkedin-claude-skills"
CATALOG_URL = "https://raw.githubusercontent.com/kconde2/barakasocial-linkedin-claude-skills/main/image-updates.json"
SKILLS = ("linkedin-image-finder", "linkedin-meme-finder")
INTERVAL = 48 * 60 * 60
MAX_BYTES = 4 * 1024 * 1024


def digest(data):
    return hashlib.sha256(data).hexdigest()


def version_key(value):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)(?:-preview\.(\d+))?", value)
    if not match:
        raise ValueError("Unsupported version")
    major, minor, patch, preview = match.groups()
    return (int(major), int(minor), int(patch), int(preview) if preview else float("inf"))


def read_identity(directory):
    text = (directory / "SKILL.md").read_text()
    name = re.search(r"^name: ([a-z0-9-]+)$", text, re.M)
    version = re.search(r'^  version: "([^"]+)"$', text, re.M)
    if not name or name[1] not in SKILLS or not version:
        raise ValueError("Unknown installed skill")
    version_key(version[1])
    return name[1], version[1]


def safe_path(name):
    p = PurePosixPath(name)
    if not name or "\\" in name or p.is_absolute() or ".." in p.parts or str(p) != name:
        raise ValueError("Unsafe archive path")
    return p


def validate_catalog(data):
    if data.get("schema_version") != 1 or not isinstance(data.get("skills"), dict):
        raise ValueError("Invalid catalog")
    for name, item in data["skills"].items():
        if name not in SKILLS:
            raise ValueError("Unknown skill in catalog")
        version_key(item["latest"])
        if item["latest"] not in item["releases"]:
            raise ValueError("Latest release missing")
        for version, release in item["releases"].items():
            version_key(version)
            expected = f"{REPOSITORY}/releases/download/v{version}/{name}.zip"
            if release["url"] != expected or not re.fullmatch("[a-f0-9]{64}", release["sha256"]):
                raise ValueError("Invalid release source")
            if "SKILL.md" not in release["files"] or not release["files"]:
                raise ValueError("Incomplete release")
            for path, checksum in release["files"].items():
                safe_path(path)
                if not re.fullmatch("[a-f0-9]{64}", checksum):
                    raise ValueError("Invalid file checksum")
            if not isinstance(release["notes"], str) or len(release["notes"]) > 2000:
                raise ValueError("Invalid release notes")
    return data


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "BarakaSocial-skill-updates/1"})
    with urllib.request.urlopen(request, timeout=5) as response:
        if not response.url.startswith("https://"):
            raise ValueError("Insecure redirect")
        data = response.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("Download too large")
    return data


def atomic_json(path, data):
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix=".state-")
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


@contextmanager
def locked(directory):
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    handle = (directory / "lock").open("a+b")
    unlock = None
    try:
        try:
            import fcntl
        except ImportError:
            import msvcrt
            if handle.seek(0, 2) == 0:
                handle.write(b"0")
                handle.flush()
            handle.seek(0)
            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError:
                raise RuntimeError("Update helper busy; continue the task without checking")
            def unlock():
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                raise RuntimeError("Update helper busy; continue the task without checking")
            def unlock():
                fcntl.flock(handle, fcntl.LOCK_UN)
        yield
    finally:
        if unlock:
            unlock()
        handle.close()


def load_state(path):
    if not path.exists():
        return {}
    try:
        state = json.loads(path.read_text())
        if not isinstance(state, dict):
            raise ValueError()
        if "catalog" in state:
            validate_catalog(state["catalog"])
        return state
    except (ValueError, KeyError, TypeError):
        # Preserve corrupted state for inspection; do not overwrite it.
        raise ValueError("Update state is unreadable; continue the task without checking")


def file_hashes(directory):
    hashes = {}
    for path in directory.rglob("*"):
        if path.is_symlink():
            raise ValueError("Symlink in installation; manual update required")
        if path.is_file():
            hashes[path.relative_to(directory).as_posix()] = digest(path.read_bytes())
    return hashes


def unpack(data, name, version, release, destination):
    if digest(data) != release["sha256"]:
        raise ValueError("Archive checksum mismatch")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        files = {}
        total = 0
        for entry in archive.infolist():
            path = safe_path(entry.filename)
            if entry.is_dir() or len(path.parts) < 2 or path.parts[0] != name:
                raise ValueError("Unexpected archive entry")
            if stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError("Archive symlink")
            relative = PurePosixPath(*path.parts[1:]).as_posix()
            if relative in files:
                raise ValueError("Duplicate archive entry")
            total += entry.file_size
            if total > MAX_BYTES:
                raise ValueError("Expanded archive too large")
            content = archive.read(entry)
            if release["files"].get(relative) != digest(content):
                raise ValueError("File checksum mismatch")
            files[relative] = content
        if set(files) != set(release["files"]):
            raise ValueError("Incomplete archive")
        for relative, content in files.items():
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    if read_identity(destination) != (name, version):
        raise ValueError("Archive identity mismatch")


def run(action, skill_dir, state_dir, accept=None, replace_modified=False, downloader=fetch, now=None):
    now = time.time() if now is None else now
    skill_dir = Path(skill_dir).absolute()
    if skill_dir.is_symlink():
        raise ValueError("Managed/symlink installation; use its installer")
    name, installed = read_identity(skill_dir)
    state_dir = Path(state_dir).expanduser().absolute()
    if state_dir == skill_dir or skill_dir in state_dir.parents:
        raise ValueError("State must be outside the skill")
    with locked(state_dir):
        state_path = state_dir / "state.json"
        state = load_state(state_path)
        if action == "check":
            last = state.get("last_attempt")
            if not isinstance(last, (int, float)) or now < last or now - last >= INTERVAL:
                state["last_attempt"] = now
                # Persist attempt before the network call; failed checks also respect the interval.
                atomic_json(state_path, state)
                try:
                    catalog = validate_catalog(json.loads(downloader(CATALOG_URL)))
                    state["catalog"] = catalog
                    state["last_success"] = now
                    atomic_json(state_path, state)
                except Exception:
                    return {"status": "unavailable", "continue_task": True}
            catalog = state.get("catalog", {})
            item = catalog.get("skills", {}).get(name)
            if not item:
                return {"status": "unavailable", "continue_task": True}
            latest = item["latest"]
            if version_key(latest) <= version_key(installed):
                return {"status": "current", "version": installed}
            release = item["releases"][latest]
            # Different installations may have different versions. Notification is shared per skill/version.
            already = latest in state.get("notified", {}).get(name, [])
            return {"status": "available", "notify": not already, "skill": name,
                    "installed": installed, "version": latest, "notes": release["notes"],
                    "url": release["url"], "sha256": release["sha256"]}
        item = state.get("catalog", {}).get("skills", {}).get(name)
        if not item or not accept or accept not in item["releases"]:
            raise ValueError("Check first and name the exact offered version")
        if action == "notice":
            notified = state.setdefault("notified", {}).setdefault(name, [])
            if accept not in notified:
                notified.append(accept)
            atomic_json(state_path, state)
            return {"status": "notice_recorded"}
        if action != "install":
            raise ValueError("Unknown action")
        if version_key(accept) <= version_key(installed):
            return {"status": "current", "version": installed}
        release = item["releases"][accept]
        baseline = item["releases"].get(installed)
        before = file_hashes(skill_dir)
        changed = sorted(set(before) | set(baseline["files"])) if baseline else sorted(before)
        if baseline:
            changed = [p for p in changed if before.get(p) != baseline["files"].get(p)]
        if (not baseline or changed) and not replace_modified:
            return {"status": "review_required", "reason": "unknown_baseline" if not baseline else "local_changes",
                    "files": changed, "continue_task": True}
        # All downloads and staging finish before the installed directory is touched.
        staging = Path(tempfile.mkdtemp(prefix=f".{name}-stage-", dir=skill_dir.parent))
        backup = state_dir / "backups" / f"{name}-{uuid.uuid4().hex}"
        backup.parent.mkdir(parents=True, exist_ok=True)
        try:
            unpack(downloader(release["url"]), name, accept, release, staging)
            if file_hashes(skill_dir) != before:
                raise ValueError("Installation changed during download; retry after review")
            os.replace(skill_dir, backup)
            try:
                os.replace(staging, skill_dir)
                if file_hashes(skill_dir) != release["files"]:
                    raise ValueError("Installed file verification failed")
            except Exception:
                if skill_dir.exists():
                    shutil.rmtree(skill_dir)
                os.replace(backup, skill_dir)
                raise
        finally:
            if staging.exists():
                shutil.rmtree(staging)
        return {"status": "installed", "version": accept, "backup": str(backup),
                "reload": "Reload the skill or start a new session before claiming the new behavior."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["check", "notice", "install"])
    parser.add_argument("--skill-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--state-dir", type=Path, default=Path.home() / ".cache/barakasocial/image-skill-updates")
    parser.add_argument("--accept", help="Exact version approved for install, or displayed for notice")
    parser.add_argument("--replace-modified", action="store_true",
                        help="Only after separate approval to replace reviewed local modifications")
    args = parser.parse_args()
    try:
        result = run(args.action, args.skill_dir, args.state_dir, args.accept, args.replace_modified)
    except Exception as error:
        result = {"status": "error", "message": str(error), "continue_task": True}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
