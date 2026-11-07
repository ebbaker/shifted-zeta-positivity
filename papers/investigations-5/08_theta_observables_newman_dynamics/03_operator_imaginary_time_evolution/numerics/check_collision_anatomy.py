"""Exact local algebra checks; no theta evaluation or collision search.

6 November 2026. Prepared for Edward Baker with substantial LLM assistance,
gpt-6-astra / max. See operator Note07 for the analytical arguments.
"""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import hashlib
import json

def add(p, q):
    out = dict(p)
    for k, v in q.items(): out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}

def scale(p, a):
    return {k: a*v for k, v in p.items() if a*v}

def mul(p, q, cap=8):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            if i+j <= cap: out[i+j] = out.get(i+j, F(0)) + a*b
    return {k: v for k, v in out.items() if v}

def power(p, n):
    out = {0:F(1)}
    for _ in range(n): out=mul(out,p)
    return out

def heat(m):
    return {(j,m-2*j): F(factorial(m),factorial(j)*factorial(m-2*j))
            for j in range(m//2+1)}

def ds(p):
    return {(s-1,y):v*s for (s,y),v in p.items() if s}

def dyy(p):
    return {(s,y-2):v*y*(y-1) for (s,y),v in p.items() if y>=2}

def compose(p,s,y):
    out={}
    for (i,j),v in p.items(): out=add(out,scale(mul(power(s,i),power(y,j)),v))
    return out

def field(a,b,c):
    out={}
    for m,v in [(2,a/F(2)),(3,b/F(6)),(4,c/F(24))]:
        out=add(out,scale(heat(m),v))
    return out

def dx(p):
    return {(s,y-1):v*y for (s,y),v in p.items() if y}

for m in range(2,9): assert ds(heat(m))==dyy(heat(m))
cases=[(F(1),F(2),F(3)),(F(-2),F(1),F(-4)),(F(3),F(-2),F(5))]
for a,b,c in cases:
    h=field(a,b,c)
    B=c/(6*a)-b*b/(9*a*a)
    for sign in [-1,1]:
        # s=-e^2/2: root=e*sign + b/(3a)e^2 + sign*B/2 e^3.
        y={1:F(sign),2:b/(3*a),3:sign*B/2}
        r=compose(h,{2:F(-1,2)},y)
        assert all(r.get(i,F(0))==0 for i in range(5))
    critical={1:-b/a}
    val=compose(h,{1:F(1)},critical)
    assert val.get(1)==a
    assert val.get(2)==(c-b*b/a)/2
    slope=compose(dx(h),{1:F(1)},critical)
    assert slope.get(0,F(0))==0 and slope.get(1,F(0))==0
    r,rx=F(2),F(-3)
    dt=-r/a; xx=b*r/a**2-rx/a
    assert a*dt+r==0 and b*dt+a*xx+rx==0

def integral_even(p):
    return sum((F(2)*v/F(k+1) for k,v in p.items() if k%2==0),F(0))
shape={0:F(1),2:F(-1)}
assert integral_even(shape)==F(4,3)
assert integral_even(mul(shape,shape))==F(16,15)
assert integral_even({2:F(1)})==F(2,3)
# (4/3)/(16/15)=5/4; the common sqrt(2) and epsilon powers are explicit in Note07.
assert F(4,3)/F(16,15)==F(5,4)
q={0:F(2),1:F(3),2:F(-5),3:F(7),4:F(-11)}
f={0:F(0),1:F(0),2:F(16),3:F(0),4:F(-256)}
prod={n:sum(F(comb(n,k))*q[k]*f[n-k] for k in range(n+1)) for n in range(5)}
assert prod[0]==prod[1]==0
assert prod[2]==16*q[0] and prod[3]==48*q[1]
assert prod[4]==96*q[2]-256*q[0]

record={
    'date':'2026-11-06','author':'Edward Baker','llm_assistance':'Substantial',
    'actual_model':'gpt-6-astra','actual_effort':'max',
    'status':'passed','arithmetic':'Python fractions.Fraction exact rational arithmetic',
    'scope':['forward heat polynomials m=2..8','three asymmetric cubic/quartic heat jets',
             'root drift and squared-gap second coefficient','critical value and event-response algebra',
             'exact normalized lobe integrals and quotient coefficient','control product-rule coefficients'],
    'limits':'Finite algebra checks only; no theta values, numerical event search, uniform remainder certificate or independent review.',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
out=Path(__file__).with_name('COLLISION_ANATOMY_CHECK_20261106.json')
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'passed','record':str(out)}))
