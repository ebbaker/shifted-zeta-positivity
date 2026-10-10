#!/usr/bin/env python3
"""Exact finite formal identities; no actual heat-function sign certification."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import sys

class P:
    size = 0
    def __init__(self, data=0):
        if isinstance(data, P): self.a = dict(data.a)
        elif isinstance(data, dict): self.a = {k:F(v) for k,v in data.items() if v}
        else: self.a = {} if not data else {(0,)*self.size:F(data)}
    @classmethod
    def var(cls, i):
        key=[0]*cls.size; key[i]=1
        return cls({tuple(key):1})
    def __add__(self, other):
        b=dict(self.a)
        for k,v in P(other).a.items(): b[k]=b.get(k,F(0))+v
        return P(b)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.a.items()})
    def __sub__(self, other): return self+-P(other)
    def __rsub__(self, other): return P(other)+-self
    def __mul__(self, other):
        b={}
        for k,v in self.a.items():
            for l,w in P(other).a.items():
                key=tuple(a+c for a,c in zip(k,l)); b[key]=b.get(key,F(0))+v*w
        return P(b)
    __rmul__=__mul__
    def __truediv__(self, other): return self*F(1,other)
    def __pow__(self, power):
        out=P(1)
        for _ in range(power): out=out*self
        return out
    def d(self, i):
        out={}
        for key,v in self.a.items():
            if key[i]:
                k=list(key); k[i]-=1; out[tuple(k)]=v*key[i]
        return P(out)
    def __eq__(self, other): return self.a==P(other).a

checks=0
families=[]
def check(condition):
    global checks
    if not condition: raise AssertionError(f"exact check {checks+1} failed")
    checks+=1

def variables(n):
    P.size=n
    return [P.var(i) for i in range(n)]

def finish(name):
    source=Path(__file__)
    record={"date":"2026-10-10", "checker":source.name,
            "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
            "assertions_passed":checks, "families":families,
            "arithmetic":"Python standard-library Fraction sparse polynomials",
            "scope":"Finite formal identities only; no certified actual heat sign or independent validation."}
    target=source.with_name(name)
    target.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"record":str(target),"assertions_passed":checks},sort_keys=True))

s,q,A0,A1,A2,E0,E1,E2,x=variables(9)
c=s*(s-1)/2
def ds(p): return p.d(0)+A1*p.d(2)+A2*p.d(3)+E1*p.d(5)+E2*p.d(6)
check(s*(s/2-1+s/2)/2==c)
check((1-s/2)-1+s/2==0)
commutator=(ds(ds(c*A0))-c*A2)/4
check(commutator==((2*s-1)*A1+A0)/4)
lam=s/2-s*s/4
check(lam.d(0)==(1-s)/2)
check(lam.d(0).d(0)==-P(1)/2)
check((2*lam.d(0)*E1+lam.d(0).d(0)*E0)/4==(1-s)*E1/4-E0/8)
# Product-rule expansion after removing e^(qs/2).
first=A1+q*A0/2
second=ds(first)+q*first/2
check(second/4==A2/4+q*A1/4+q*q*A0/16)
# Complex spectral slice s=1/2+i x/2, encoded by real/imaginary pairs.
sr=P(F(1,2)); si=x/2
lambda_r=sr/2-(sr*sr-si*si)/4
lambda_i=si/2-2*sr*si/4
check(lambda_r==(3+x*x)/16)
check(lambda_i==x/8)
# Completion jets j=0..4: exact degree-two product coefficients.
for j in range(5):
    check((0 if j<1 else j*(2*s-1)/2)==(0 if j<1 else j*c.d(0)))
    check((0 if j<2 else F(j*(j-1),2))==(0 if j<2 else F(j*(j-1),2)*c.d(0).d(0)))
families.extend(["completed incoming coefficient extraction", "completion heat commutator", "cusp gauge drift and multiplication", "eigenwave residual", "nonunitary physical spectral slice", "completion spatial jet coefficients"])
finish('automorphic_scout_record_20261010.json')
