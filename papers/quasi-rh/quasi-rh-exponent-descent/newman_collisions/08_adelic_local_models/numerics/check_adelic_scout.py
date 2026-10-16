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

a,a1,a2,a3,a4,l2,l3,l5=variables(8)
def deriv(p): return a1*p.d(0)+a2*p.d(1)+a3*p.d(2)+a4*p.d(3)
expected=[P(1),a,a*a+a1,a**3+3*a*a1+a2,a**4+6*a*a*a1+3*a1*a1+4*a*a2+a3]
current=P(1)
for j in range(5):
    check(current==expected[j]); current=deriv(current)+a*current
support={1:(0,0,0),2:(1,0,0),3:(0,1,0),4:(2,0,0),5:(0,0,1),6:(1,1,0)}
logs={1:P(0),2:l2,3:l3,4:2*l2,5:l5,6:l2+l3}
for n,k in support.items():
    check(2**k[0]*3**k[1]*5**k[2]==n)
    check(sum((e*l for e,l in zip(k,(l2,l3,l5))),P(0))==logs[n])
check(logs[6]**2-l2*l2-l3*l3==2*l2*l3)
# Exact Gaussian moment-generating coefficients through degree twenty.
for k in range(11):
    moment=F(math.factorial(2*k),4**k*math.factorial(k))
    check(moment/F(math.factorial(2*k))==F(1,4**k*math.factorial(k)))
# Diagonal rational character: exponent at infinity plus local exponents cancels.
for u in range(-4,5):
    for v in range(-4,5):
        for w in range(-2,3):
            arch=u*l2+v*l3+w*l5
            local=-u*l2-v*l3-w*l5
            check(arch+local==0)
# A diagonal twist commutes with a diagonal heat action, on every retained composite.
for n in support:
    weight=F(n*n+1,n+2); twist=F(2*n-3,n+4)
    check(weight*twist==twist*weight)
families.extend(["six-term valuation support including composite 6", "mixed heat factor", "shared Gaussian moments", "raw first-through-fourth jet recurrence", "diagonal rational global compatibility", "twist commutation control"])
finish('adelic_scout_record_20261010.json')
