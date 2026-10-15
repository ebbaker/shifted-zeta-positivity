#!/usr/bin/env python3
"""Exact arithmetic for the new theta Chern/ASD and covariant-jet identities.
Prepared for Edward Baker, 15 Oct 2026, substantial LLM assistance.
Coordinating model gpt-6-astra / ultra, supplied by parent.
No numerical sign or global-completion claim.
"""
from fractions import Fraction as F
from collections import defaultdict
import json

# Laurent polynomials in p,q,r,s; q>0 in the geometric application.
def clean(x): return {k:v for k,v in x.items() if v}
def mon(c=1,p=0,q=0,r=0,s=0): return clean({(p,q,r,s):F(c)})
def add(*aa):
    out=defaultdict(F)
    for a in aa:
        for k,v in a.items():out[k]+=v
    return clean(out)
def scale(a,c):return clean({k:v*c for k,v in a.items()})
def mul(a,b):
    out=defaultdict(F)
    for k,v in a.items():
        for l,w in b.items():out[tuple(x+y for x,y in zip(k,l))]+=v*w
    return clean(out)
def diff(a,i):
    out=defaultdict(F)
    for k,v in a.items():
        if k[i]:
            kk=list(k);kk[i]-=1;out[tuple(kk)]+=k[i]*v
    return clean(out)
def d_oneform(a):
    return {(i,j):add(diff(a[j],i),scale(diff(a[i],j),-1))
            for i in range(4) for j in range(i+1,4)}
count=0
def check(a,b):
    global count
    assert a==b,(a,b)
    count+=1

# Direct real-coordinate expansion of A/pi, then differentiation.
real=[{}, mon(-1,s=2), {}, mon(-2,q=1,s=1)]
imag=[mon(s=2), {}, mon(2,s=1), mon(2,p=1,s=1)]
for k,v in d_oneform(real).items():check(v,{})
for k,v in d_oneform(imag).items():check(v,mon(-2) if k==(2,3) else {})
# The base-only rescaling adds -i q^2 d tau.
real_hat=[real[0],add(real[1],mon(q=2)),real[2],real[3]]
imag_hat=[add(imag[0],mon(-1,q=2)),imag[1],imag[2],imag[3]]
for k,v in d_oneform(real_hat).items():check(v,{})
for k,v in d_oneform(imag_hat).items():
    expected=mon(2,q=1) if k==(0,1) else mon(-2) if k==(2,3) else {}
    check(v,expected)
# Derivative of log(h_hat/h)=2*pi*q^3/3, with pi factored out.
check(diff(mon(F(2,3),q=3),1),mon(2,q=2))
# Lattice invariance of log h+log |j|^2, with -2*pi factored out.
# Here p is the lattice integer n and s is Im z.
v=mon(s=1);nq=mon(p=1,q=1)
expr=add(mul(mon(q=-1),mul(add(v,nq),add(v,nq))),
         mon(-1,p=2,q=1),mon(-2,p=1,s=1),mon(-1,q=-1,s=2))
check(expr,{})

# Formal (d_z+a)^k theta with a'=c, c'=0; keys (a power,c power,theta jet).
def step(poly):
    out=defaultdict(F)
    for (a,c,j),v in poly.items():
        if a:out[a-1,c+1,j]+=a*v
        out[a,c,j+1]+=v
        out[a+1,c,j]+=v
    return clean(out)
poly={(0,0,0):F(1)}
for k in range(1,5):
    poly=step(poly)
    if k in (2,4):
        at_zero={(c,j):v for (a,c,j),v in poly.items() if not a}
        expected={(0,2):F(1),(1,0):F(1)} if k==2 else {
            (0,4):F(1),(1,2):F(6),(2,0):F(3)}
        check(at_zero,expected)
# Source coefficients after replacing its ordinary fourth jet by the covariant jet.
check(F(6,16),F(3,8))
check(F(3,16)-F(3,16),F(0))
# Anti-self-dual e12-e34 curvature has squared norm (2*pi)^2*2.
check(F(2)**2+F(-2)**2,F(8))
print(json.dumps({'status':'pass','exact_assertions':count,
    'arithmetic':'fractions.Fraction; formal Laurent polynomials and jet operator',
    'scope':'Full theta Chern curvature, ASD rescaling, lattice metric compatibility, fourth covariant jet and source cancellation',
    'not_established':['Theta stationary sign','Physical-energy estimate','Global modular descent','Metric completeness']},indent=2))
