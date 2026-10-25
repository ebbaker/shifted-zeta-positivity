#!/usr/bin/env python3
"""Six exact scalar constant checks for HDA-18-AN03 r1.
Prepared for Edward Baker with substantial LLM assistance, gpt-6.1-sol,
actual effort ultra from parent turn metadata. No special-function samples.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,time
began=time.perf_counter()
l=Q(1000)
values=[
 ('alpha_derivative_margin',1-(Q(1,2)+Q(6*4**4,4096))),
 ('left_quadratic_margin',Q(9,20)*l*l-Q(194,3)*l-6),
 ('middle_quadratic_margin',l*l/2-4*l-203),
 ('arithmetic_decay_margin',Q(13,2)*l-53),
 ('field_constant_margin',Q(12000)-(12*97*10+7)),
 ('FI23_initial_gap_margin',Q(2**4100)-16*32*36864000)]
rows=[]
for name,value in values:
 row={'name':name,'passed':value>0}
 if name=='FI23_initial_gap_margin':
  row.update(expression='2^4100 - 16*32*36864000',subtracted_integer=16*32*36864000,power=4100)
 else:row['exact_margin']=str(value)
 rows.append(row)
result={'status':'passed' if all(r['passed'] for r in rows) else 'failed','prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra','date':'2026-10-25','case_count':len(rows),'scope':'Exactly six scalar rational/integer majorant checks, not theta, source, gamma, field or gap sampling; no interval or theorem certification.','total_execution_seconds':time.perf_counter()-began,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':rows}
Path(__file__).with_name('EFFECTIVE_OUTER_SCALAR_BOUNDS_20261025.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','case_count','total_execution_seconds','script_sha256']}))
raise SystemExit(0 if result['status']=='passed' else 1)
