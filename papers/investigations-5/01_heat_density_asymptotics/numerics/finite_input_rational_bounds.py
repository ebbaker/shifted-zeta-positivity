#!/usr/bin/env python3
"""Elementary rational bounds for the analytical HDA-18-AN02 return.
Prepared for Edward Baker with LLM assistance, gpt-6.1-sol, effort ultra.
No canonical source samples, field evaluation, numerical mesh or search.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import comb, factorial
import hashlib,json,time
start=time.perf_counter()
c=[1875,30930,68096,41408,8448,512]
first=Q(8,5)*sum(Q(c[j])*(j+1)**(j+1)*Q(3,8)**(j+1) for j in range(6))
ratio=Q(3,2)**12*Q(3,8)**15
tail=2*Q(3,8)**12*sum(Q(c[j])*12**(j+1) for j in range(6))/(1-ratio)
kernel=[Q(315,256)]
for m in range(1,5):
 kernel.append(Q(315,256)*sum(comb(4,j)*Q(factorial(2*j),factorial(2*j-m)) for j in range(5) if 2*j>=m))
cases=[
 {'name':'complete_fourth_derivative_majorant','first_mode':str(first),'tail':str(tail),'sum':str(first+tail),'bound':2**20,'passed':first+tail<2**20},
 {'name':'fourth_derivative_mode_ratio','ratio':str(ratio),'passed':ratio<1},
 {'name':'kernel_derivative_coefficient_sums','bounds':list(map(str,kernel)),'passed':kernel==[Q(315,256),Q(315,4),Q(315),Q(4725,4),Q(16065,4)]},
 {'name':'finite_regulator_beta_time','bound':str(Q(1,16*226)+Q(13,226**2)),'ceiling':'1/512','passed':Q(1,16*226)+Q(13,226**2)<Q(1,512)},
 {'name':'real_saddle_bracket','q_half_lower':str(Q(95,4)+Q(9,2)-Q(22,7)*8),'qprime_half_lower':str(95+9-4*Q(22,7)*8),'qprime_one_upper':str(2*97+9-12*Q(8,3)**4),'passed':Q(95,4)+Q(9,2)-Q(22,7)*8>0 and 95+9-4*Q(22,7)*8>0 and 2*97+9-12*Q(8,3)**4<0}
]
r={'status':'passed' if all(x['passed'] for x in cases) else 'failed','prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra','scope':'Five exact-rational scalar majorant checks only. No theta/source or field samples, no gamma evaluation, no numerical certificate of a gap or full transfer.','case_count':len(cases),'total_execution_seconds':time.perf_counter()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':cases}
Path(__file__).with_name('FINITE_INPUT_RATIONAL_BOUNDS_20261024.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','case_count','total_execution_seconds','script_sha256']}))
raise SystemExit(0 if r['status']=='passed' else 1)
