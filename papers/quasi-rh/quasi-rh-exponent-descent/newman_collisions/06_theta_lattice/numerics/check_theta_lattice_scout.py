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

t,x,*J=variables(11)
def dx(p):
    return p.d(1)+sum((J[k+1]*p.d(k+2) for k in range(8)),P(0))
def dt(p):
    return p.d(0)-sum((J[k+2]*p.d(k+2) for k in range(7)),P(0))
a=2*t-1-x*x
value=1+a*J[0]+4*t*x*J[1]-4*t*t*J[2]
current=value
for j in range(5):
    expected=(1 if j==0 else 0)+(a+4*t*j)*J[j]+4*t*x*J[j+1]-4*t*t*J[j+2]
    if j: expected=expected-2*j*x*J[j-1]
    if j>=2: expected=expected-j*(j-1)*J[j-2]
    check(current==expected)
    current=dx(current)
check(dt(value)+dx(dx(value))==0)
# e^u v^k theta^(k): d_u has diagonal 1+4k and next entry 4.
coeff={0:F(1)}
for _ in range(2):
    nxt={}
    for k,v in coeff.items():
        nxt[k]=nxt.get(k,F(0))+(1+4*k)*v
        nxt[k+1]=nxt.get(k+1,F(0))+4*v
    coeff=nxt
check(coeff=={0:F(1),1:F(24),2:F(16)})
check(coeff[1]/16==F(3,2))
check(coeff[2]/16==1)
# The modular derivative at v=1 gives the spectator odd endpoint factor.
phi0=F(7,3); theta1=F(6,5); theta_prime=-theta1/4
check(4*phi0*theta_prime==-phi0*theta1)
check(phi0*theta1!=phi0)
families.extend(["rotor differential insertion", "zero-mode affine readout through fourth jet", "backward-heat compatibility", "spectator coefficient and odd-endpoint mismatch"])
finish('theta_lattice_scout_record_20261010.json')
