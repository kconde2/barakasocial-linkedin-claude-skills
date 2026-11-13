import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_skill", ROOT / "scripts/package_skill.py")
packaging = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packaging)


class SkillDistributionTest(unittest.TestCase):
    def test_archive_installs_the_exact_source_without_other_repository_files(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = packaging.package_skill("linkedin-hook-generator", Path(directory) / "skill.zip")
            with zipfile.ZipFile(archive) as bundle:
                self.assertEqual(bundle.namelist(), ["linkedin-hook-generator/SKILL.md"])
                bundle.extractall(Path(directory) / "skills")
            installed = Path(directory) / "skills/linkedin-hook-generator/SKILL.md"
            self.assertEqual(installed.read_bytes(), (ROOT / "skills/linkedin-hook-generator/SKILL.md").read_bytes())

    def test_archives_are_reproducible(self):
        with tempfile.TemporaryDirectory() as directory:
            first = packaging.package_skill("linkedin-hook-generator", Path(directory) / "first.zip")
            second = packaging.package_skill("linkedin-hook-generator", Path(directory) / "second.zip")
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_cannot_package_a_path_outside_the_skills_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                packaging.package_skill("../private", Path(directory) / "skill.zip")


if __name__ == "__main__":
    unittest.main()
