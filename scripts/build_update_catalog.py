"""Prepare a catalog from packaged skills. Publish only after checking uploaded release assets."""
import argparse
import json
from pathlib import Path
import zipfile
import tempfile

from skill_updates import SKILLS, REPOSITORY, digest, read_identity, validate_catalog, fetch, unpack
from package_skill import ROOT


def build(previous, archives, verify_published=False):
    result = json.loads(json.dumps(previous))
    for name in SKILLS:
        version = read_identity(ROOT / "skills" / name)[1]
        archive_path = archives / f"{name}.zip"
        data = archive_path.read_bytes()
        with zipfile.ZipFile(archive_path) as archive:
            files = {str(Path(path).relative_to(name)): digest(archive.read(path))
                     for path in archive.namelist()}
        release = {"url": f"{REPOSITORY}/releases/download/v{version}/{name}.zip",
                   "sha256": digest(data), "files": files,
                   "notes": "Contrôle partagé des mises à jour toutes les 48 heures. Installation après accord avec vérification et sauvegarde."}
        item = result["skills"].setdefault(name, {"releases": {}})
        existing = item["releases"].get(version)
        if existing and (existing["sha256"] != release["sha256"] or existing["files"] != files):
            raise ValueError("Never overwrite an existing release: " + name + " " + version)
        if existing:
            release = existing
        with tempfile.TemporaryDirectory() as folder:
            unpack(data, name, version, release, Path(folder))
        if verify_published and digest(fetch(release["url"])) != release["sha256"]:
            raise ValueError("Published ZIP differs from local ZIP: " + name)
        item["releases"][version] = release
        item["latest"] = version
    return validate_catalog(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=ROOT / "updates.json")
    parser.add_argument("--archives", type=Path, default=ROOT / "dist")
    parser.add_argument("--output", type=Path, default=ROOT / "dist/updates.json")
    parser.add_argument("--verify-published", action="store_true")
    args = parser.parse_args()
    previous = json.loads(args.previous.read_text())
    if args.output.resolve() == (ROOT / "updates.json").resolve() and not args.verify_published:
        parser.error("Updating the public catalog requires --verify-published")
    result = build(previous, args.archives, args.verify_published)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(args.output)
