#!/usr/bin/env python3
"""Independent direct checks of marked ranks 3 through 6.

Prepared for Edward Baker, 23 October 2026, with substantial LLM assistance.
Recorded model gpt-6-astra (Codex), effort ultra.
Requires SymPy and the sibling 14_discrete_feng_kernel_check.py.
Uses exact numerator division, independently of the generating-residue script.
These finite checks do not establish all ranks or the arithmetic error bounds;
those proofs are in Note 15. No floating-point or zeta-zero data is used.
"""
import argparse,json
from datetime import datetime,timezone
import importlib.util
from pathlib import Path
import sympy as S
p=Path(__file__).with_name('14_discrete_feng_kernel_check.py')
spec=importlib.util.spec_from_file_location('oldcheck',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
s,t,a,b,c,th=m.s,m.t,m.a,m.b,m.c,m.theta
r=s+t;N=-s*t*t+t*t*(a+c)+a*c*(s+2*t)
def extractI(reg,C):
 h=m.homogeneous_parts(reg,5);num=(a-c)*h[5]
 for j in range(5):
  num+=(b+c)*(-a-b)**j/S.factorial(j)*h[5-j].subs({a:-b,b:-a,c:c},simultaneous=True)
  num-=(a+b)*(-b-c)**j/S.factorial(j)*h[5-j].subs({a:a,b:-c,c:-b},simultaneous=True)
 q,rem=S.div(S.Poly(S.expand(num),a,b,c,s,t),S.Poly((a+b)*(b+c)*(a-c),a,b,c,s,t));assert rem.is_zero
 return S.factor(S.Poly(q.as_expr(),a,b,c).coeff_monomial(a*b*c)/C)
def extractJ(reg,C):
 h=m.homogeneous_parts(reg,3);num=h[3]-sum((-a-b)**j/S.factorial(j)*h[3-j].subs({a:-b,b:-a},simultaneous=True) for j in range(4))
 q,rem=S.div(S.Poly(S.expand(num),a,b,s,t),S.Poly(a+b,a,b,s,t));assert rem.is_zero
 return S.factor(S.Poly(q.as_expr(),a,b).coeff_monomial(a*b)/C)
M0=lambda z:(1+th)/(th*z**2)-2/(th*z**3)
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output",type=Path,required=True)
args=parser.parse_args()
records=[]
for k in [3,4,5,6]:
 inv=S.Add(*[S.binomial(k+i-2,i)*S.binomial(k+j-2,j)*(-a)**i*(-c)**j*t**(4-i-j) for i in range(5) for j in range(5-i)])
 Ir=extractI(b*(s+b)*N**k*inv,S.factorial(k)*r**(k+1)*t**(3*k+3))
 inv=S.Add(*[S.binomial(k+i-2,i)*(-b)**i*s**(4-i) for i in range(5)])
 Il=extractI(b*(t+a)*(t+c)*(b-t)**k*inv,S.factorial(k)*r**(k+1)*t*s**(k+3))
 inv=S.Add(*[S.binomial(k+i-2,i)*(-a)**i*t**(3-i) for i in range(4)])
 J=extractJ((s+b)*(a-s)**k*inv,S.factorial(k)*r**(k+1)*t**(k+2))
 K=S.factor(Ir+Il.subs({s:t,t:s},simultaneous=True)+J)
 R0=m.residue_from_principal_part(M0(s)*K,S.S.Zero)
 assert S.cancel(R0)==0
 print('PASS direct rank',k,'baseline s0 residue identically zero',flush=True)
 records.append({'rank':k,'complete_kernel':str(K),'baseline_s0_residue':str(R0),'passed':True})

args.output.write_text(json.dumps({"status":"passed","scope":"exact algebra only; finite rank check independent of all-rank generating proof","model":"gpt-6-astra (Codex)","reasoning_effort":"ultra","sympy_version":S.__version__,"run_utc":datetime.now(timezone.utc).isoformat(),"checks":records},indent=2)+"\n")
