import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("skill_updates", ROOT / "scripts/skill_updates.py")
updates = importlib.util.module_from_spec(spec)
spec.loader.exec_module(updates)
NAME = "linkedin-post-analyzer"
OTHER = "linkedin-topic-finder"


def contents(name, version):
    return {"SKILL.md": f'---\nname: {name}\ndescription: Test\nmetadata:\n  version: "{version}"\n---\n'.encode(),
            "references/rules.md": b"rules"}


def bundle(name, files):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as z:
        for path, value in files.items():
            z.writestr(name + "/" + path, value)
    return buffer.getvalue()


def release(name, version, files):
    archive = bundle(name, files)
    return {"url": f"{updates.REPOSITORY}/releases/download/v{version}/{name}.zip",
            "sha256": updates.digest(archive),
            "files": {p: updates.digest(v) for p, v in files.items()},
            "notes": "Native choices"}, archive


class UpdateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.state = self.root / "state"
        self.install = self.root / "skills" / NAME
        self.install.mkdir(parents=True)
        self.catalog = {"schema_version": 1, "skills": {}}
        self.downloads = {}
        self.calls = []
        for name in (NAME, OTHER):
            releases = {}
            for version in ("0.1.0-preview.13", "0.1.0-preview.14"):
                files = contents(name, version)
                record, archive = release(name, version, files)
                releases[version] = record
                self.downloads[record["url"]] = archive
            self.catalog["skills"][name] = {"latest": "0.1.0-preview.14", "releases": releases}
        for path, data in contents(NAME, "0.1.0-preview.13").items():
            target = self.install / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        self.profile = self.root / "editorial-profile.json"
        self.profile.write_text('{"voice":"personal"}')

    def download(self, url):
        self.calls.append(url)
        if url == updates.CATALOG_URL:
            return json.dumps(self.catalog).encode()
        return self.downloads[url]

    def run_action(self, action="check", now=1000000, **kwargs):
        return updates.run(action, self.install, self.state, downloader=self.download, now=now, **kwargs)

    def test_first_use_checks_once_and_another_skill_uses_shared_cache(self):
        self.assertTrue(self.run_action()["notify"])
        other = self.root / OTHER
        other.mkdir()
        (other / "SKILL.md").write_bytes(contents(OTHER, "0.1.0-preview.13")["SKILL.md"])
        result = updates.run("check", other, self.state, downloader=self.download, now=1000001)
        self.assertTrue(result["notify"])
        self.assertEqual(self.calls, [updates.CATALOG_URL])
        self.run_action(now=1000000 + updates.INTERVAL - 1)
        self.assertEqual(len(self.calls), 1)
        self.run_action(now=1000000 + updates.INTERVAL)
        self.assertEqual(len(self.calls), 2)

    def test_check_never_installs_and_notice_is_once_per_release(self):
        original = updates.file_hashes(self.install)
        self.run_action()
        self.assertEqual(original, updates.file_hashes(self.install))
        self.run_action("notice", accept="0.1.0-preview.14")
        self.assertFalse(self.run_action()["notify"])
        self.assertEqual(original, updates.file_hashes(self.install))

    def test_new_release_can_notify_after_previous_notice(self):
        self.run_action()
        self.run_action("notice", accept="0.1.0-preview.14")
        record, archive = release(NAME, "0.1.0-preview.15", contents(NAME, "0.1.0-preview.15"))
        self.catalog["skills"][NAME]["releases"]["0.1.0-preview.15"] = record
        self.catalog["skills"][NAME]["latest"] = "0.1.0-preview.15"
        self.assertTrue(self.run_action(now=1000000 + updates.INTERVAL)["notify"])

    def test_install_requires_exact_version_and_preserves_profile_and_backup(self):
        self.run_action()
        with self.assertRaises(ValueError):
            self.run_action("install")
        result = self.run_action("install", accept="0.1.0-preview.14")
        self.assertEqual(result["status"], "installed")
        self.assertEqual(updates.read_identity(self.install)[1], "0.1.0-preview.14")
        self.assertEqual(updates.read_identity(Path(result["backup"]))[1], "0.1.0-preview.13")
        self.assertEqual(self.profile.read_text(), '{"voice":"personal"}')
        self.assertEqual(self.run_action()["status"], "current")

    def test_modified_files_require_separate_approval(self):
        self.run_action()
        (self.install / "private.md").write_text("local preference")
        before = updates.file_hashes(self.install)
        result = self.run_action("install", accept="0.1.0-preview.14")
        self.assertEqual(result["status"], "review_required")
        self.assertIn("private.md", result["files"])
        self.assertEqual(before, updates.file_hashes(self.install))
        result = self.run_action("install", accept="0.1.0-preview.14", replace_modified=True)
        self.assertEqual((Path(result["backup"]) / "private.md").read_text(), "local preference")

    def test_unknown_baseline_does_not_silently_replace(self):
        del self.catalog["skills"][NAME]["releases"]["0.1.0-preview.13"]
        self.run_action()
        self.assertEqual(self.run_action("install", accept="0.1.0-preview.14")["reason"], "unknown_baseline")

    def test_bad_checksum_preserves_installed_files(self):
        self.run_action()
        record = self.catalog["skills"][NAME]["releases"]["0.1.0-preview.14"]
        self.downloads[record["url"]] = b"bad archive"
        before = updates.file_hashes(self.install)
        with self.assertRaises(ValueError):
            self.run_action("install", accept="0.1.0-preview.14")
        self.assertEqual(before, updates.file_hashes(self.install))

    def test_path_traversal_rejected_even_if_archive_hash_matches(self):
        files = contents(NAME, "0.1.0-preview.14")
        files["../../escape"] = b"bad"
        record, archive = release(NAME, "0.1.0-preview.14", files)
        self.catalog["skills"][NAME]["releases"]["0.1.0-preview.14"] = record
        self.assertEqual(self.run_action()["status"], "unavailable")
        with self.assertRaises(ValueError):
            updates.unpack(archive, NAME, "0.1.0-preview.14", record, self.root / "staged")
        self.assertFalse((self.root / "escape").exists())

    def test_wrong_host_or_identity_rejected(self):
        self.catalog["skills"][NAME]["releases"]["0.1.0-preview.14"]["url"] = "https://example.org/skill.zip"
        self.assertEqual(self.run_action()["status"], "unavailable")
        record, archive = release(NAME, "0.1.0-preview.14", contents(OTHER, "0.1.0-preview.14"))
        with self.assertRaises(ValueError):
            updates.unpack(archive, NAME, "0.1.0-preview.14", record, self.root / "staged")

    def test_network_failure_is_nonblocking_and_rate_limited(self):
        calls = []
        def broken(url):
            calls.append(url)
            raise OSError("offline")
        first = updates.run("check", self.install, self.state, downloader=broken, now=1000000)
        second = updates.run("check", self.install, self.state, downloader=broken, now=1000001)
        self.assertTrue(first["continue_task"])
        self.assertEqual(second["status"], "unavailable")
        self.assertEqual(len(calls), 1)

    def test_concurrent_call_cannot_start_second_download(self):
        def nested(url):
            with self.assertRaises(RuntimeError):
                self.run_action()
            return self.download(url)
        result = updates.run("check", self.install, self.state, downloader=nested, now=1000000)
        self.assertEqual(result["status"], "available")
        self.assertEqual(self.calls, [updates.CATALOG_URL])

    def test_failed_replacement_restores_old_directory(self):
        self.run_action()
        original = updates.os.replace
        def failing(source, target):
            if "-stage-" in str(source):
                raise OSError("simulated rename failure")
            return original(source, target)
        with patch.object(updates.os, "replace", side_effect=failing):
            with self.assertRaises(OSError):
                self.run_action("install", accept="0.1.0-preview.14")
        self.assertEqual(updates.read_identity(self.install)[1], "0.1.0-preview.13")

    def test_change_during_download_is_preserved_and_stops_install(self):
        self.run_action()
        def changing(url):
            (self.install / "private.md").write_text("concurrent edit")
            return self.download(url)
        with self.assertRaises(ValueError):
            updates.run("install", self.install, self.state, accept="0.1.0-preview.14", downloader=changing)
        self.assertEqual((self.install / "private.md").read_text(), "concurrent edit")
        self.assertEqual(updates.read_identity(self.install)[1], "0.1.0-preview.13")

    def test_numeric_versions_and_no_downgrade(self):
        self.assertGreater(updates.version_key("0.1.0-preview.14"), updates.version_key("0.1.0-preview.9"))
        (self.install / "SKILL.md").write_bytes(contents(NAME, "0.1.0-preview.15")["SKILL.md"])
        self.assertEqual(self.run_action()["status"], "current")

    def test_cli_uses_cached_catalog_and_reports_json_without_network(self):
        self.run_action()
        state = json.loads((self.state / "state.json").read_text())
        state["last_attempt"] = updates.time.time()
        (self.state / "state.json").write_text(json.dumps(state))
        process = subprocess.run(
            [sys.executable, str(ROOT / "scripts/skill_updates.py"), "check",
             "--skill-dir", str(self.install), "--state-dir", str(self.state)],
            capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(process.stdout)["status"], "available")

    def test_corrupt_state_is_not_overwritten(self):
        self.state.mkdir()
        state = self.state / "state.json"
        state.write_text("{broken")
        with self.assertRaises(ValueError):
            self.run_action()
        self.assertEqual(state.read_text(), "{broken")
        self.assertEqual(self.calls, [])

    def test_symlink_installation_is_not_replaced(self):
        link = self.root / "managed"
        link.symlink_to(self.install, target_is_directory=True)
        with self.assertRaises(ValueError):
            updates.run("check", link, self.state, downloader=self.download)
        self.assertEqual(self.calls, [])

    def test_incomplete_package_preserves_installation(self):
        missing = contents(NAME, "0.1.0-preview.14")
        del missing["references/rules.md"]
        record = self.catalog["skills"][NAME]["releases"]["0.1.0-preview.14"]
        incomplete = bundle(NAME, missing)
        record["sha256"] = updates.digest(incomplete)
        self.downloads[record["url"]] = incomplete
        self.run_action()
        with self.assertRaises(ValueError):
            self.run_action("install", accept="0.1.0-preview.14")
        self.assertEqual(updates.read_identity(self.install)[1], "0.1.0-preview.13")
