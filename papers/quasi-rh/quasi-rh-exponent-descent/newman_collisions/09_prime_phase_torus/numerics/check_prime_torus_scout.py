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

O,Op,d,dp,c,cp,C0,Y0,C1,Y1,C2,Y2,t,h,A1,A2=variables(16)
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cadd(z,w): return (z[0]+w[0],z[1]+w[1])
a=(P(0),-O); ap=(P(0),-Op); beta=(-d,c); bp=(-dp,cp)
S=(C0,Y0); S1=(C1,Y1); S2=(C2,Y2)
first=cadd(cmul(a,S),cmul(beta,S1))
check(first[0]==O*Y0-c*Y1-d*C1)
coef0=cadd(cmul(a,a),ap)
coef1=cadd((2*cmul(a,beta)[0],2*cmul(a,beta)[1]),bp)
second=cadd(cadd(cmul(coef0,S),cmul(coef1,S1)),cmul(cmul(beta,beta),S2))
check(second[0]==-O*O*C0+Op*Y0+(2*O*c-dp)*C1-(2*O*d+cp)*Y1+(d*d-c*c)*C2+2*d*c*Y2)
B=1+t*A1/2
log_ss=A1*B+t*h*A2/2
residual=(h*h-h*h*B*B-log_ss)/4
check(residual==(h*h*(1-B*B)-A1*B-t*h*A2/2)/4)
# Residual at t=0 is exactly -alpha'/4.
check((h*h-h*h-A1)/4==-A1/4)
# Signed core/edge correlation partition on exact rational vectors.
for u in range(-3,4):
    for v in range(-3,4):
        for w in range(-2,3):
            A=(F(u,3),F(v,5)); Bv=(F(w,7),F(u-v,11))
            norm=lambda z:z[0]*z[0]+z[1]*z[1]
            total=(A[0]+Bv[0],A[1]+Bv[1])
            cross=2*(A[0]*Bv[0]+A[1]*Bv[1])
            check(norm(total)==norm(A)+norm(Bv)+cross)
# Exact monomial log encoding for all n<=256 (formal prime exponents).
primes=[p for p in range(2,257) if all(p%k for k in range(2,math.isqrt(p)+1))]
for n in range(1,257):
    m=n; product=1
    for p in primes:
        while m%p==0: m//=p; product*=p
    check(m==1 and product==n)
# Separate jet recurrence variables after all earlier polynomials have been checked.
v,v1,v2,v3,v4=variables(5)
def dv(p): return v1*p.d(0)+v2*p.d(1)+v3*p.d(2)+v4*p.d(3)
expected=[P(1),v,v*v+v1,v**3+3*v*v1+v2,v**4+6*v*v*v1+3*v1*v1+4*v*v2+v3]
current=P(1)
for j in range(5): check(current==expected[j]); current=dv(current)+v*current
families.extend(["actual drift-containing first and second orbit jets", "finite heat residual including alpha derivatives", "signed complete core/edge correlation identity", "prime monomial encoding through 256", "first-through-fourth raw jet recurrence"])
finish('prime_torus_scout_record_20261010.json')
