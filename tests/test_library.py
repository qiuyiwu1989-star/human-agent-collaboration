import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'skills/collaboration-library'
spec=importlib.util.spec_from_file_location('search',BASE/'scripts/search.py')
search=importlib.util.module_from_spec(spec);spec.loader.exec_module(search)
records=json.loads(search.CATALOG.read_text())['records']

class LibraryTests(unittest.TestCase):
    def test_integrity_and_provenance(self):
        ids={r['id'] for r in records}
        self.assertEqual(len(ids),len(records))
        for r in records:
            for field in ('id','title','kind','scenarios','keywords','summary','when_to_use','avoid_when','steps','output','verification','sources'):
                self.assertTrue(r[field],(r['id'],field))
            self.assertTrue(set(r['related']) <= ids)
            self.assertIn(r['kind'],['method','example','scenario','evaluation','experience'])
            self.assertIn(r['evidence_status'],['documented','illustrative','unevaluated','observed-success','observed-failure'])
            for source in r['sources']:
                path=(ROOT/source['path']).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertIn(source['section'],path.read_text())
            if r['evidence_status'].startswith('observed-'):
                self.assertEqual(r['kind'],'experience')
                for key in ('context','action','result','limitations','evidence'):self.assertTrue(r['outcome'][key])
                for evidence in r['outcome']['evidence']:
                    path=(ROOT/evidence).resolve()
                    self.assertTrue(path.is_relative_to(ROOT));self.assertTrue(path.is_file())
            else:self.assertIsNone(r['outcome'])
    def test_retrieval_tasks(self):
        for query,wanted in [('页面说不清需要原型','M02'),('handoff','M09'),('原始数据 因果','M04'),('缩短 润色','M12')]:
            self.assertIn(wanted,[r['id'] for _,r in search.search(records,query)[:3]],query)
        results=search.search(records,kind='method',scenario='写作')
        self.assertTrue(results)
        self.assertTrue(all(r['kind']=='method' and '写作' in r['scenarios'] for _,r in results))
        self.assertEqual(search.search(records,status='observed-success'),[])
        self.assertEqual(search.search(records,'zzzzunmatchedterm'),[])
    def test_standalone_copy_and_cli(self):
        import shutil
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'skill';shutil.copytree(BASE,dest)
            script=dest/'scripts/search.py'
            def run(*args):return subprocess.run([sys.executable,str(script),*args],cwd=tmp,capture_output=True,text=True)
            r=run('--id','M02');self.assertEqual(r.returncode,0)
            self.assertIn('steps',json.loads(r.stdout)['items'][0])
            self.assertGreater(json.loads(run('--related','M02').stdout)['total'],0)
            self.assertNotEqual(run('--id','missing').returncode,0)
            self.assertNotEqual(run('--limit','0').returncode,0)
    def test_generated_index_is_current(self):
        old=(BASE/'references/index.md').read_bytes()
        subprocess.run([sys.executable,str(BASE/'scripts/build_index.py')],check=True)
        self.assertEqual(old,(BASE/'references/index.md').read_bytes())
if __name__=='__main__':unittest.main()
