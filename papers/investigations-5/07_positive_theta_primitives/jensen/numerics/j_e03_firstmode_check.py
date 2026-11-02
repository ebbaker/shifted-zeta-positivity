#!/usr/bin/env python3
"""Fresh contributing J-E03 first-mode identity audit. Standard-library integers.
Prepared for Edward Baker with substantial LLM assistance; gpt-6.1-sol, ultra.
Fixed P0 through P7 only.
No numerical evaluations and no repository writes.
"""
import json
from hashlib import sha256
from pathlib import Path

def trim(p):
    p=list(p)
    while p and p[-1]==0:
        p.pop()
    return p

def add(*ps):
    q=[0]*max(map(len,ps),default=0)
    for p in ps:
        for i,a in enumerate(p): q[i]+=a
    return trim(q)

def scale(p,a): return trim([a*b for b in p])
def mul(p,q):
    r=[0]*max(0,len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return trim(r)
def power(p,n):
    r=[1]
    for _ in range(n): r=mul(r,p)
    return r

def derivative(p): return trim([i*p[i] for i in range(1,len(p))])
def determinant3(a,b,c,d,e,f,g,h,i):
    return add(mul(a,add(mul(e,i),scale(mul(f,h),-1))),
               scale(mul(b,add(mul(d,i),scale(mul(f,g),-1))),-1),
               mul(c,add(mul(d,h),scale(mul(e,g),-1))))

t=[0,1];d=[-3,2]
P=[[0,-3,2]]
for _ in range(7):
    P.append(add(scale(mul(t,derivative(P[-1])),4),mul([1,-4],P[-1])))
A=add(mul(P[0],P[3]),scale(mul(P[1],P[2]),-1))
B=add(mul(P[0],P[4]),scale(mul(P[2],P[2]),-1))
W=determinant3(P[0],P[1],P[2],P[2],P[3],P[4],P[4],P[5],P[6])
W1=determinant3(P[0],P[1],P[3],P[2],P[3],P[5],P[4],P[5],P[7])
N=add(mul(mul(P[0],A),W1),scale(mul(add(mul(P[0],B),scale(mul(P[1],A),-1)),W),-3))
p=[-654885,3056130,-6180300,7280280,-5589360,2917728,-1034304,239232,-32768,2048]
Rprime_numerator=add(mul([0,-352,128],power(d,2)),[0,-192])
assert mul(A,power(d,2))==mul(power(P[0],2),Rprime_numerator)
assert mul(N,power(d,7))==scale(mul(mul(power(t,5),p),power(P[0],6)),3*2**26)
# Also check the source recurrence against both reduced rational R/T formulas.
Rbase=[33,-88,16]
Tbase=[-1983,-11632,14944,-3840,256]
assert mul(P[2],d)==mul(P[0],add(mul(Rbase,d),[24]))
assert mul(P[4],d)==mul(P[0],add(mul(Tbase,d),[-7824]))
# The simpler cross-multiplication closes every denominator using P0=t*d.
assert mul(N,d)==scale(mul(power(t,11),p),3*2**26)
print(json.dumps({'date':'2026-11-01','prepared_for':'Edward Baker',
 'llm_assistance':'substantial','model':'gpt-6.1-sol','effort':'ultra','task':'J-E03',
 'scope':'exact first-mode P0..P7; no numeric evaluations',
 'checks':{'R1_formula':True,'T1_formula':True,'R1prime_formula':True,'K1_formula_from_joint_N':True},
 'P_degrees':[len(v)-1 for v in P], 'N_degree':len(N)-1,
 'first_mode_K_leading_power':7,'first_mode_K_leading_coefficient':3*2**30,
 'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
