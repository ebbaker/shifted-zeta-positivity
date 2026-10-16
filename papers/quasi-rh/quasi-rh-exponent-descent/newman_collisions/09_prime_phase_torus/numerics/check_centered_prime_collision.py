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

# Independent affine-centered Bell rows through order four.
A,A1,A2,A3,B,B1,B2,B3,r=variables(9)
def ds(p):
    return A1*p.d(0)+A2*p.d(1)+A3*p.d(2)+B1*p.d(4)+B2*p.d(5)+B3*p.d(6)
v=A+B*r
rows={
 2:[A*A+A1,2*A*B+B1,B*B],
 3:[A**3+3*A*A1+A2,3*A*A*B+3*(A*B1+B*A1)+B2,3*A*B*B+3*B*B1,B**3],
 4:[A**4+6*A*A*A1+3*A1*A1+4*A*A2+A3,
    4*A**3*B+6*(A*A*B1+2*A*B*A1)+6*A1*B1+4*(A*B2+B*A2)+B3,
    6*A*A*B*B+6*(2*A*B*B1+B*B*A1)+3*B1*B1+4*B*B2,
    4*A*B**3+6*B*B*B1,B**4]}
current=P(1)
for j in range(1,5):
    current=ds(current)+v*current
    if j>=2: check(current==sum((p*r**k for k,p in enumerate(rows[j])),P(0)))
# Candidate elimination, verified after multiplication by c.
u0,v0,u1,v1,A,c,d,X0,Y0,X1,Y1,e1,H=variables(13)
lhs=c*(u0*X0-v0*Y0+u1*X1-v1*Y1+H)
rhs=-c*v0*Y0+(c*u1+d*v1)*X1+c*H+(c*u0-A*v1)*X0+v1*e1
check(lhs-rhs==-v1*(c*Y1+d*X1-A*X0+e1))
# All residual terms against the centered frozen frequency.
b,eps,V1,V2,V3=variables(5)
v=b+eps
raw={2:v*v+V1,3:v**3+3*v*V1+V2,
     4:v**4+6*v*v*V1+3*V1*V1+4*v*V2+V3}
res={2:2*b*eps+eps*eps+V1,
     3:3*b*b*eps+3*b*eps*eps+eps**3+3*(b+eps)*V1+V2,
     4:4*b**3*eps+6*b*b*eps*eps+4*b*eps**3+eps**4
       +6*(b+eps)**2*V1+3*V1*V1+4*(b+eps)*V2+V3}
for j in (2,3,4): check(raw[j]-b**j==res[j])
# Genuine pair-coordinate algebra and completion coefficient.
h,delta,Gamma=variables(3)
rn=(h+delta)/2; rm=(h-delta)/2
D=rn**3*rm**3+F(3,4)*rn**2*rm**2*(rn**2+rm**2)-Gamma*rn**2*rm**2/2
Q=-rn**3*rm**3+F(3,4)*rn**2*rm**2*(rn**2+rm**2)-Gamma*rn**2*rm**2/2
check(D==(h*h-delta*delta)**2*(5*h*h+delta*delta)/128-Gamma*(h*h-delta*delta)**2/32)
check(Q==(h*h-delta*delta)**2*(h*h+5*delta*delta)/128-Gamma*(h*h-delta*delta)**2/32)
ln,lm,t=variables(3)
check(t*(ln*ln+lm*lm)/4==t*((ln+lm)**2+(ln-lm)**2)/8)
c,X2,Y3,X4,gamma=variables(5)
g2=-2*c*c*X2; g3=2*c**3*Y3; g4=2*c**4*X4
check(2*g3*g3-3*g2*g4-gamma*g2*g2==4*c**6*(2*Y3*Y3+3*X2*X4)-4*gamma*c**4*X2*X2)
# Complete measured quadratic payment on exact rational perturbations.
def lagrange(g,gamma): return 2*g[1]**2-3*g[0]*g[2]-gamma*g[0]**2
def payment(g,z,gamma):
    return (4*abs(g[1])*z[1]+2*z[1]**2
          +3*(abs(g[0])*z[2]+abs(g[2])*z[0]+z[0]*z[2])
          +abs(gamma)*(2*abs(g[0])*z[0]+z[0]**2))
for k in range(1,26):
    g=[F(k-13,7),F(2*k-17,11),F(9-k,5)]
    z=[F(k,53),F(2*k+1,79),F(k+3,67)]
    for gam in (F(-3),F(-1,2),F(0),F(1,3),F(2)):
        for signs in ((1,1,1),(1,-1,1),(-1,1,-1),(-1,-1,-1)):
            e=[sign*bound/F(2) for sign,bound in zip(signs,z)]
            check(abs(lagrange([a+b for a,b in zip(g,e)],gam)-lagrange(g,gam))<=payment(g,z,gam))
# Rational unit-complex monomial controls check grouping, not actual height signs.
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cconj(z): return (z[0],-z[1])
def cpow(z,k):
    result=(F(1),F(0))
    for _ in range(k): result=cmul(result,z)
    return result

def factor(n):
    data={}; p=2
    while p*p<=n:
        while n%p==0: data[p]=data.get(p,0)+1; n//=p
        p+=1
    if n>1: data[n]=data.get(n,0)+1
    return data

def formal_log(n): return sum((F(p,p+1)*k for p,k in factor(n).items()),F(0))
def chi(n):
    z=(F(1),F(0))
    for p,k in factor(n).items():
        z=cmul(z,cpow((F(p*p-1,p*p+1),F(2*p,p*p+1)),k))
    return z

def numeric_coeff(h,delta,Gamma):
    outer=(h*h-delta*delta)**2
    return (outer*(5*h*h+delta*delta)/128-Gamma*outer/32,
            outer*(h*h+5*delta*delta)/128-Gamma*outer/32)

theta=(F(3,5),F(4,5)); theta2=cmul(theta,theta); mu=F(5,2)
Gamma=F(1,7)
for N in range(1,25):
    w={n:F(1,n+1) for n in range(1,N+1)}
    logs={n:formal_log(n) for n in w}; chars={n:chi(n) for n in w}
    q={n:cmul(theta,chars[n]) for n in w}
    def moments(indices):
        return [(sum((w[n]*(logs[n]-mu)**j*q[n][0] for n in indices),F(0)),
                 sum((w[n]*(logs[n]-mu)**j*q[n][1] for n in indices),F(0))) for j in range(5)]
    def K(m): return 2*m[3][1]**2+3*m[2][0]*m[4][0]-Gamma*m[2][0]**2
    total=K(moments(list(w)))
    ratio={}; product={}; partitions={(False,False):F(0),(False,True):F(0),(True,False):F(0),(True,True):F(0)}
    direct=F(0)
    for n in w:
        for m in w:
            h=logs[n]+logs[m]-2*mu; delta=logs[n]-logs[m]
            Dc,Pc=numeric_coeff(h,delta,Gamma)
            diffphase=cmul(chars[n],cconj(chars[m]))[0]
            sumphase=cmul(theta2,cmul(chars[n],chars[m]))[0]
            val=w[n]*w[m]*(Dc*diffphase+Pc*sumphase)
            direct+=val; partitions[(2*n>N,2*m>N)]+=val
            g=math.gcd(n,m); a,b=n//g,m//g
            ratio[(a,b)]=ratio.get((a,b),F(0))+w[n]*w[m]*Dc
            product[n*m]=product.get(n*m,F(0))+w[n]*w[m]*Pc
            check(g<=N//max(a,b) and math.gcd(a,b)==1 and g*a==n and g*b==m)
            check(formal_log(n*m)==logs[n]+logs[m])
    grouped_ratio=sum((value*cmul(chi(a),cconj(chi(b)))[0] for (a,b),value in ratio.items()),F(0))
    grouped_product=sum((value*cmul(theta2,chi(k))[0] for k,value in product.items()),F(0))
    check(direct==total)
    check(grouped_ratio+grouped_product==total)
    block=[n for n in w if 2*n>N]; core=[n for n in w if 2*n<=N]
    MB=moments(block); MC=moments(core)
    mixed=4*MC[3][1]*MB[3][1]+3*(MC[2][0]*MB[4][0]+MB[2][0]*MC[4][0])-2*Gamma*MC[2][0]*MB[2][0]
    check(partitions[(True,True)]==K(MB))
    check(partitions[(False,False)]==K(MC))
    check(partitions[(True,False)]+partitions[(False,True)]==mixed)
    check(total==K(MC)+K(MB)+mixed)
# Exact exponent and interval reserves.
for k in range(101):
    kap=F(1)+F(k,200)
    a=kap*(4-kap)/16; b=kap*(kap+4)/16; s=F(1,2)+kap/8
    check(2*a-kap==-2*b)
    check(a-b==-kap*kap/8)
    check(F(5,6)-s>=F(7,48))
    check((1-s)+(F(5,6)-s)==F(5,6)-kap/4)
    check(F(11,24)<=F(5,6)-kap/4<=F(7,12))
    check(F(7,24)<=F(5,3)-2*s<=F(5,12))
families.extend(["independent centered second-through-fourth raw Bell rows", "candidate elimination with both tolerances", "frozen-frequency residual polynomials", "threshold centered moment coefficient", "full measured quadratic perturbation payment", "ratio and divisor-product pair kernels and mixed heat factor", "complete ordered-pair grouping and block/core partition through N=24", "uniform centering and macroscopic-block exponent reserves"])
finish('centered_prime_collision_record_20261010.json')
