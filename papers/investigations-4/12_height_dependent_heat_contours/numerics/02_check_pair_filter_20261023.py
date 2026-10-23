#!/usr/bin/env python3
"""Exact algebra diagnostics for HDC Notes 07--10; not a theta certificate.
Prepared for Edward Baker, 2026-10-23; LLM: gpt-6-astra, effort ultra.
Run with Python 3; stdout is a small JSON execution record.
"""
from fractions import Fraction as Q
import json
import sys

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def zero(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]

def eye(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = Q(1)
    return a

def add(a,b,scale=Q(1)):
    return [[x+scale*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def mul(a,b):
    return [[sum(x*y for x,y in zip(ar,bc)) for bc in zip(*b)] for ar in a]

def tr(a):
    return sum(a[i][i] for i in range(len(a)))

def inv(a):
    n=len(a); c=[list(ar)+er for ar,er in zip(a,eye(n))]
    for i in range(n):
        p=next(k for k in range(i,n) if c[k][i])
        c[i],c[p]=c[p],c[i]
        v=c[i][i]; c[i]=[x/v for x in c[i]]
        for j in range(n):
            if j!=i:
                v=c[j][i]; c[j]=[x-v*y for x,y in zip(c[j],c[i])]
    return [row[n:] for row in c]

def lap(x,weights=None):
    n=len(x); a=zero(n)
    for i in range(n):
        for j in range(i):
            w=(x[i]-x[j])**-2 if weights is None else weights[i,j]
            a[i][i]+=w; a[j][j]+=w; a[i][j]-=w; a[j][i]-=w
    return a

def state(x,t,b):
    n=len(x); l=lap(x); r=inv(add(eye(n),l,4*t))
    f=add(eye(n),r,-1); jstat=tr(mul(f,r))
    velocity=[2*sum(1/(x[i]-x[j]) for j in range(n) if j!=i)+2*b[i] for i in range(n)]
    wd={}; coeff={}; bracket_sum=Q(0)
    for i in range(n):
        for j in range(i):
            g=x[i]-x[j]; w=g**-2
            db=(b[i]-b[j])/g
            interior=sum(1/((x[i]-x[k])*(x[j]-x[k])) for k in range(n) if k not in (i,j))
            wd[i,j]=-2*w*(velocity[i]-velocity[j])/g
            check(wd[i,j]==-2*w*(4*w-2*interior+2*db))
            rv=[r[k][i]-r[k][j] for k in range(n)]
            coeff[i,j]=w*sum(v*v for v in rv)
            bracket_sum+=4*coeff[i,j]*(1-8*t*w+4*t*interior-4*t*db)
    ld=lap(x,wd)
    derivative=4*tr(mul(mul(r,r),add(l,ld,t)))
    check(derivative==bracket_sum)
    check(sum(coeff.values())==jstat/(4*t))
    check(0<=jstat<=tr(f))
    check(jstat<=Q(n-1,4))
    return {"L":l,"Ldot":ld,"q":tr(f),"J":jstat,"qp":derivative,"coeff":coeff}

cases=[]
for n in range(2,8):
    for scale in [Q(1),Q(1,1000)]:
        x=[scale*Q(i*i+2*i-n) for i in range(n)]
        a=max(abs(v) for v in x)
        rc=3*a+1
        exterior=[-2*rc,-3*rc,2*rc,4*rc]
        b=[sum(1/(v-y) for y in exterior) for v in x]
        t=Q(2,7)
        z=state(x,t,b); unforced=state(x,t,[Q(0)]*n)
        beta=sum(1/(y*y) for y in exterior)/(1-a/rc)**2
        difference=z["qp"]-unforced["qp"]
        check(0<=difference<=4*beta*z["J"])
        check(difference<=beta*(n-1))
        direct=16*t*sum(z["coeff"][i,j]*sum(1/((x[i]-y)*(x[j]-y)) for y in exterior)
                        for i in range(n) for j in range(i))
        check(difference==direct)
        # Sine-field local control: b cancels every selected internal velocity.
        sine_b=[-sum(1/(x[i]-x[j]) for j in range(n) if j!=i) for i in range(n)]
        sine=state(x,t,sine_b)
        check(sine["Ldot"]==zero(n))
        check(sine["qp"]>0)
        cases.append({"n":n,"scale":str(scale),"tail_error":str(difference),
                      "tail_bound":str(4*beta*z["J"])})

double=state([Q(-1),Q(1)],Q(1,2),[Q(0),Q(0)])
check(double["q"]==Q(1,2)); check(double["qp"]==0)
triple=state([Q(-1),Q(0),Q(1)],Q(1,6),[Q(0)]*3)
check(triple["q"]==Q(7,6)); check(triple["qp"]==0)
check(add(triple["L"],triple["Ldot"],Q(1,6))==zero(3))
simple=state([Q(-2),Q(2)],Q(1),[Q(0)]*2)
check(simple["q"]==Q(1,3)); check(simple["qp"]==Q(1,9))

# Sharp path blocks used in the uniform multiplicity consumer.
for m in range(2,31):
    if m%2==0:
        lower=Q(m,2)*Q(1,2)
    else:
        lower=Q(m-3,2)*Q(1,2)+Q(14,15)
    check(lower>=Q(m,4))
path=zero(3)
for i,j in [(0,1),(1,2)]:
    path[i][i]+=Q(1,2);path[j][j]+=Q(1,2)
    path[i][j]-=Q(1,2);path[j][i]-=Q(1,2)
check(tr(add(eye(3),inv(add(eye(3),path)),-1))==Q(14,15))

print(json.dumps({
    "date":"2026-10-23","prepared_for":"Edward Baker",
    "model":"gpt-6-astra","reasoning_effort":"ultra",
    "arithmetic":"Python standard-library Fraction, exact rational",
    "python":sys.version.split()[0],"assertions_passed":checks,
    "configurations":len(cases),"ranks":[2,3,4,5,6,7],
    "controls":{"double_q":str(double["q"]),"triple_q":str(triple["q"]),
                "simple_quadratic_q":str(simple["q"]),"triple_path_q":"14/15"},
    "claims_checked":["complete weight derivative","coupled filter derivative",
       "filter trace error bound","signed complete finite exterior-tail bound",
       "stationary sine cancellation","quadratic and Hermite collision controls",
       "pair-plus-triple multiplicity constant"],
    "scope":"Algebra diagnostics only; no canonical theta wall, spectral upper bound, or simplicity certificate."
},indent=2))
