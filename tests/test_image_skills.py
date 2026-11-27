import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import image_skill_updates as updates
from package_skill import package_skill
import skill_updates as legacy

class ImageSkillsTest(unittest.TestCase):
    def test_archives_and_update_identity(self):
        for name in updates.SKILLS:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                source=ROOT/'skills'/name
                self.assertEqual(updates.read_identity(source),(name,'0.1.0-preview.16'))
                self.assertEqual((source/'scripts/skill_updates.py').read_bytes(),(ROOT/'scripts/image_skill_updates.py').read_bytes())
                a=package_skill(name,Path(tmp)/'a.zip')
                b=package_skill(name,Path(tmp)/'b.zip')
                self.assertEqual(a.read_bytes(),b.read_bytes())
                with zipfile.ZipFile(a) as z:
                    self.assertEqual(set(z.namelist()),{f'{name}/SKILL.md',f'{name}/references/updates.md',f'{name}/scripts/skill_updates.py'})
    def test_cache_and_catalog_are_isolated_from_legacy(self):
        source=(ROOT/'scripts/image_skill_updates.py').read_text()
        self.assertIn('.cache/barakasocial/image-skill-updates', source)
        self.assertNotEqual(updates.CATALOG_URL,legacy.CATALOG_URL)

    def test_legacy_catalog_still_loads(self):
        legacy.validate_catalog(json.loads((ROOT/'updates.json').read_text()))
    def test_visual_catalog_has_two_skills_and_verified_archive_contents(self):
        for name in updates.SKILLS:
            with tempfile.TemporaryDirectory() as tmp:
                archive=package_skill(name,Path(tmp)/'a.zip').read_bytes()
                with zipfile.ZipFile(__import__('io').BytesIO(archive)) as z:
                    files={str(Path(p).relative_to(name)):updates.digest(z.read(p)) for p in z.namelist()}
                release={'url':f'{updates.REPOSITORY}/releases/download/v0.1.0-preview.16/{name}.zip','sha256':updates.digest(archive),'files':files,'notes':'New visual skill'}
                updates.validate_catalog({'schema_version':1,'skills':{name:{'latest':'0.1.0-preview.16','releases':{'0.1.0-preview.16':release}}}})
                updates.unpack(archive,name,'0.1.0-preview.16',release,Path(tmp)/'stage')
