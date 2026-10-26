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
            self.assertIn(r['evidence_status'],['documented','illustrative','unevaluated','observed-success','observed-failure','reported-outcome'])
            for source in r['sources']:
                path=(ROOT/source['path']).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertIn(source['section'],path.read_text())
            if r['evidence_status'].startswith('observed-') or r['evidence_status']=='reported-outcome':
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
    def test_mined_methods_and_reported_outcomes(self):
        for query,title in [('负向测试 历史缺陷','事故驱动门禁与负向测试'),('accepted 回读 reportedAt','指令接受不等于设备完成'),('request_id 回执 重试','幂等写回与不确定结果恢复'),('引文 说话人 有效期','引用的四维核验'),('音频 分片 缓存','长音频分片缓存与双重验收')]:
            self.assertIn(title,[r['title'] for _,r in search.search(records,query,kind='method')[:3]])
        cases=search.search(records,status='reported-outcome')
        self.assertEqual(len(cases),6)
        self.assertTrue(all(r['kind']=='experience' and r['outcome']['limitations'] for _,r in cases))

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
