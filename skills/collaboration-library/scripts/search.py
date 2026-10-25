#!/usr/bin/env python3
"""Offline catalog retrieval; Python standard library only. Scores are lexical relevance."""
import argparse
import json
from pathlib import Path
import re

CATALOG = Path(__file__).resolve().parents[1] / 'references/catalog.json'

def tokens(text):
    text = text.casefold()
    words = re.findall(r'[a-z0-9_-]+', text)
    for phrase in re.findall(r'[\u4e00-\u9fff]+', text):
        words.extend([phrase] if len(phrase) == 1 else [phrase[i:i+2] for i in range(len(phrase)-1)])
    return set(words)

def search(records, query='', kind=None, scenario=None, status=None):
    terms = tokens(query)
    results = []
    for record in records:
        if kind and record['kind'] != kind: continue
        if scenario and scenario not in record['scenarios']: continue
        if status and record['evidence_status'] != status: continue
        head = ' '.join([record['id'], record['title'], *record['keywords']]).casefold()
        body = json.dumps({k:record[k] for k in ('summary','steps','scenarios')}, ensure_ascii=False).casefold()
        score = sum(3 * (t in head) + (t in body) for t in terms)
        if query and query.casefold() in head: score += 10
        if terms and score == 0: continue
        results.append((score, record))
    return sorted(results, key=lambda item:(-item[0], item[1]['id']))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('query', nargs='?', default='')
    p.add_argument('--id'); p.add_argument('--related')
    p.add_argument('--kind', choices=['method','example','scenario','evaluation','experience'])
    p.add_argument('--scenario')
    p.add_argument('--status', choices=['documented','illustrative','unevaluated','observed-success','observed-failure','reported-outcome'])
    p.add_argument('--limit',type=int,default=5);p.add_argument('--full',action='store_true')
    a=p.parse_args()
    if a.limit < 1: p.error('--limit must be positive')
    records=json.loads(CATALOG.read_text())['records']; by_id={r['id']:r for r in records}
    if a.id and a.related: p.error('choose --id or --related')
    if a.id or a.related:
        key=a.id or a.related
        if key not in by_id: p.error('unknown ID: '+key)
        selected=[by_id[key]] if a.id else [by_id[x] for x in by_id[key]['related']]
        matches=search(selected,a.query,a.kind,a.scenario,a.status)
    else: matches=search(records,a.query,a.kind,a.scenario,a.status)
    items=[]
    for score,r in matches[:a.limit]:
        item=dict(r) if a.full or a.id else {k:r[k] for k in ('id','title','kind','summary','evidence_status','sources','related')}
        item['relevance_score']=score;items.append(item)
    print(json.dumps({'total':len(matches),'returned':len(items),'score_note':'Lexical relevance only; not confidence or proof of success.','items':items},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
