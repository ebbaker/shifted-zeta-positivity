#!/usr/bin/env python3
"""Finite exact algebra for weighted theta reflection; no theta sign test.

Prepared for Edward Baker, 15 October 2026, with substantial LLM assistance.
Recorded coordinating model gpt-6-astra, effort ultra.
Standard library only. Analytic uniqueness is proved in the companion note.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, platform

def add(p,q):
    r=dict(p)
    for k,v in q.items(): r[k]=r.get(k,F(0))+v
    return {k:v for k,v in r.items() if v}
def scale(p,c): return {k:v*c for k,v in p.items() if v*c}
def step(p):
    # d/du [e^u exp(-a) p(a)], a'=4a.
    return add({k:(1+4*k)*v for k,v in p.items()}, {k+1:-4*v for k,v in p.items()})
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    checks=[]
    def check(name,a,b):
        assert a==b,(name,a,b)
        checks.append(name)
    ps=[{0:F(1)}]
    for k in range(35): ps.append(step(ps[-1]))
    phi=scale(add(ps[2],scale(ps[0],-1)),F(1,8))
    check('source_polynomial',phi,{2:F(2),1:F(-3)})
    check('first_odd_source_derivative',step(phi),{3:F(-8),2:F(30),1:F(-15)})
    q=phi
    for k in range(32):
        check(f'source_primitive_derivative_identity_{k}',q,scale(add(ps[k+2],scale(ps[k],-1)),F(1,8)))
        q=step(q)
    # Sum the formal odd-jet equations 8 Phi^(2k+1)=psi^(2k+3)-psi^(2k+1).
    # Each key labels an independent odd primitive jet, not its numerical value.
    total={}
    for k in range(16):
        total=add(total,{2*k+3:F(1,8),2*k+1:F(-1,8)})
        check(f'odd_endpoint_telescoping_through_{2*k+1}',total,
              {2*k+3:F(1,8),1:F(-1,8)})
    check('P_prime_normalization',F(1)+2*F(-1,2),F(0))
    record={'schema':'inv22_weighted_reflection_algebra_v1','date':'2026-10-15','prepared_for':'Edward Baker','llm_assistance':'Substantial','recorded_model':'gpt-6-astra','recorded_effort':'ultra','python':platform.python_version(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'PASS','exact_assertions':len(checks),'checks':checks,'scope':'Finite rational source-polynomial and endpoint-recurrence checks; no analytic uniqueness, infinite theta sign, or collision exclusion is computer-certified.'}
    if args.output: args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['status','exact_assertions','scope']}))
if __name__=='__main__': main()
