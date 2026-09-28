import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('sync',Path(__file__).resolve().parents[1]/'scripts/sync_from_ilya_drive.py')
sync=importlib.util.module_from_spec(spec);spec.loader.exec_module(sync)
class SelectionTests(unittest.TestCase):
 def test_service_containers_excluded(self):
  self.assertEqual(sync.publication_names(['.system','_backups','_derivative-subskills','real']),{'real'})
 def test_broken_skill_still_blocks(self):
  with tempfile.TemporaryDirectory() as d:
   self.assertIn('missing SKILL.md',sync.validate_skill(Path(d)))
 def test_identical_duplicate_and_divergence(self):
  with tempfile.TemporaryDirectory() as d, patch.object(sync,'SKILLS_DIR',Path(d)):
   for n in ['skill','skill 2']:
    (Path(d)/n).mkdir();(Path(d)/n/'SKILL.md').write_text('same')
   self.assertEqual(sync.publication_names(['skill','skill 2']),{'skill'})
   (Path(d)/'skill 2'/'extra.md').write_text('different')
   with self.assertRaises(ValueError): sync.publication_names(['skill','skill 2'])
if __name__=='__main__': unittest.main()
