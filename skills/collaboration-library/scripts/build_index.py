#!/usr/bin/env python3
"""Render the human-readable index from the catalog; no network access."""
import json
from collections import Counter
from pathlib import Path
base=Path(__file__).resolve().parents[1]
records=json.loads((base/'references/catalog.json').read_text())['records']
counts=Counter(r['kind'] for r in records)
lines=['# 人机协作分类目录','','此页由 catalog.json 生成；完整字段可按 ID 用 scripts/search.py --id 读取。', '', '当前：'+ '、'.join(f'{k} {v} 条' for k,v in counts.items())+'。真实成功经验 '+str(sum(r['evidence_status']=='observed-success' for r in records))+' 条。','']
for kind,title in [('method','合作方法'),('example','典型示例（非真实成功案例）'),('scenario','场景映射'),('evaluation','评估用例（尚未运行）'),('experience','真实经验')]:
 lines += ['## '+title,'']
 subset=[r for r in records if r['kind']==kind]
 if not subset:lines+=['目前没有符合证据要求的条目。',''];continue
 for r in subset:
  lines += [f"### {r['id']} · {r['title']}",'',f"- 场景：{'、'.join(r['scenarios'])}；状态：{r['evidence_status']}",f"- 用途：{r['summary']}",f"- 检索词：{'、'.join(r['keywords'])}",f"- 关联：{', '.join(r['related']) or '无'}",'']
(base/'references/index.md').write_text('\n'.join(lines)+'\n')
