import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_update_catalog as builder
from package_skill import package_skill
from skill_updates import SKILLS, validate_catalog


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.archives = Path(self.temp.name)
        for name in SKILLS:
            package_skill(name, self.archives / (name + ".zip"))
        self.previous = json.loads((ROOT / "updates.json").read_text())

    def test_candidate_keeps_published_history_and_matches_all_packages(self):
        candidate = builder.build(self.previous, self.archives)
        validate_catalog(candidate)
        for name in SKILLS:
            self.assertEqual(candidate["skills"][name]["latest"], "0.1.0-preview.14")
            for version, release in self.previous["skills"][name]["releases"].items():
                self.assertEqual(candidate["skills"][name]["releases"][version], release)
        self.assertNotEqual(self.previous, candidate)

    def test_existing_release_cannot_be_overwritten(self):
        candidate = builder.build(self.previous, self.archives)
        candidate["skills"][SKILLS[0]]["releases"]["0.1.0-preview.14"]["sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            builder.build(candidate, self.archives)

    def test_publication_verification_refuses_different_remote_asset(self):
        with patch.object(builder, "fetch", return_value=b"wrong remote archive"):
            with self.assertRaises(ValueError):
                builder.build(self.previous, self.archives, verify_published=True)
