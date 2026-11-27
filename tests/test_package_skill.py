import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_skill", ROOT / "scripts/package_skill.py")
packaging = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packaging)


REFERENCES = ("personalization.md", "profile-schema.md", "updates.md")

SKILLS = ("linkedin-hook-generator", "linkedin-post-writer", "linkedin-post-analyzer", "linkedin-profile-optimizer", "linkedin-topic-finder")


class SkillDistributionTest(unittest.TestCase):
    def test_archive_installs_the_exact_source_without_other_repository_files(self):
        for name in SKILLS:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as directory:
                archive = packaging.package_skill(name, Path(directory) / "skill.zip")
                with zipfile.ZipFile(archive) as bundle:
                    self.assertEqual(bundle.namelist(), [f"{name}/SKILL.md", *[f"{name}/references/{ref}" for ref in REFERENCES], f"{name}/scripts/skill_updates.py"])
                    bundle.extractall(Path(directory) / "skills")
                installed = Path(directory) / "skills" / name / "SKILL.md"
                self.assertEqual(installed.read_bytes(), (ROOT / "skills" / name / "SKILL.md").read_bytes())
                for ref in REFERENCES:
                    reference = installed.parent / "references" / ref
                    self.assertEqual(reference.read_bytes(), (ROOT / "skills" / name / "references" / ref).read_bytes())
                self.assertIn("references/personalization.md", installed.read_text())
                self.assertIn("references/updates.md", installed.read_text())
                self.assertEqual((installed.parent / "scripts/skill_updates.py").read_bytes(), (ROOT / "scripts/skill_updates.py").read_bytes())

    def test_archives_are_reproducible(self):
        for name in SKILLS:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as directory:
                first = packaging.package_skill(name, Path(directory) / "first.zip")
                second = packaging.package_skill(name, Path(directory) / "second.zip")
                self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_all_skills_share_the_same_personalization_contract(self):
        for ref in REFERENCES:
            with self.subTest(reference=ref):
                references = [(ROOT / "skills" / name / "references" / ref).read_bytes() for name in SKILLS]
                self.assertTrue(references[0])
                self.assertTrue(all(content == references[0] for content in references))

    def test_cannot_package_a_path_outside_the_skills_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                packaging.package_skill("../private", Path(directory) / "skill.zip")


if __name__ == "__main__":
    unittest.main()
