#!/usr/bin/env python3
"""Exact complex heat-germ discriminants. Requires python-flint.
Prepared for Edward Baker, 2026-10-15, with substantial LLM assistance.
Recorded coordinating model gpt-6-astra, effort ultra.
"""
import argparse, hashlib, json, math, platform, time
from pathlib import Path
import flint
from flint import fmpq_mpoly_ctx

def main():
 p=argparse.ArgumentParser(description=__doc__); p.add_argument('--output',type=Path,required=True); args=p.parse_args()
 start=time.monotonic(); C=fmpq_mpoly_ctx.get(['t','z']); t,z=C.gens(); checks=0; rows=[]
 def check(v):
  nonlocal checks
  if not v: raise AssertionError('check '+str(checks+1))
  checks+=1
 def heat(m):
  return sum((math.factorial(m)//(math.factorial(k)*math.factorial(m-2*k))*(-t)**k*z**(m-2*k) for k in range(m//2+1)),C.constant(0))
 def t_order(poly):
  terms=poly.to_dict(); check(bool(terms)); check(all(e[1]==0 for e in terms))
  return min(e[0] for e in terms)
 for m in range(2,17):
  h=heat(m); L=m*(m-1)//2; r=m//2
  check(h.derivative('t')+h.derivative('z').derivative('z')==0)
  d=h.discriminant('z'); expected=2**L*math.prod(k**k for k in range(1,m+1))*t**L
  check(d==expected); check(t_order(d)==L); check((L-r)%2==0)
  row={'m':m,'real_spacetime_index':-r,'complex_degree':L,'declared_quaternion_degree':-L,'primitive_curve_milnor_number':2*L,'discriminant_coefficient':str(2**L*math.prod(k**k for k in range(1,m+1))),'asymmetric_cases':[]}
  if m<=10:
   for a,b in [(1,0),(-2,0),(1,1)]:
    q=h+a*heat(m+1)+b*heat(m+2)
    check(q.derivative('t')+q.derivative('z').derivative('z')==0)
    dq=q.discriminant('z'); check(t_order(dq)==L)
    row['asymmetric_cases'].append({'a':a,'b':b,'discriminant_order':L,'discriminant_terms':len(dq.to_dict())})
  rows.append(row)
 record={'date':'2026-10-15','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance','model':'gpt-6-astra','reasoning_effort':'ultra','checker':Path(__file__).name,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python_version':platform.python_version(),'python_flint_version':flint.__version__,'checks':checks,'model_cases':len(rows),'asymmetric_cases':sum(len(r['asymmetric_cases']) for r in rows),'scope':'Exact polynomial discriminants and heat identities. The analytic arbitrary-germ theorem is proved in the accompanying note; these checks do not certify theta zeros.','cases':rows,'elapsed_seconds':time.monotonic()-start}
 args.output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:record[k] for k in ['checks','model_cases','asymmetric_cases','elapsed_seconds']}))
if __name__=='__main__':main()
