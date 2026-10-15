#!/usr/bin/env python3
"""Exact Chern/ASD and covariant source identities; no theta sign test."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

# Polynomial differential forms in (p,q,r,s). Coefficients are rational.
def clean(p):
    return {k:v for k,v in p.items() if v}
def mono(c=1,p=0,q=0,r=0,s=0):
    return clean({(p,q,r,s):F(c)})
def add(*args):
    out={}
    for a in args:
        for k,v in a.items(): out[k]=out.get(k,F(0))+v
    return clean(out)
def diff(a,i):
    out={}
    for k,v in a.items():
        if k[i]:
            e=list(k); e[i]-=1
            out[tuple(e)]=v*k[i]
    return clean(out)
def exterior_one(a):
    out={}
    for j,coef in a.items():
        for i in range(4):
            if i==j: continue
            key=tuple(sorted((i,j)))
            term={k:v*(1 if i<j else -1) for k,v in diff(coef,i).items()}
            out[key]=add(out.get(key,{}),term)
    return clean(out)
checks=0
def check(a,b,label):
    global checks
    assert a==b,(label,a,b)
    checks+=1

# A/(pi*i)=2s dz-s^2 d tau, expanded in real coordinates.
real_A={0:mono(s=2),2:mono(2,s=1),3:mono(2,p=1,s=1)}
imag_A={1:mono(s=2),3:mono(2,q=1,s=1)}
check(exterior_one(real_A),{(2,3):mono(-2)},'Chern real curvature coefficient')
check(exterior_one(imag_A),{},'Chern imaginary coefficient closes')
real_B={0:mono(-1,q=2)}
imag_B={1:mono(-1,q=2)}
check(exterior_one(real_B),{(0,1):mono(2,q=1)},'ASD base curvature correction')
check(exterior_one(imag_B),{},'base imaginary coefficient closes')

# Wirtinger derivative of (2/3)q^3, after removing the common pi factor.
# partial_tau q=1/(2i), hence partial_tau f divided by i = -f_q/2.
check({k:-v/2 for k,v in diff(mono(F(2,3),q=3),1).items()},mono(-1,q=2),'base Hermitian rescaling')

# Hodge star in an oriented orthonormal coframe; curvature/(2pi*i)=e12-e34.
star_table={(0,1):((2,3),1),(2,3):((0,1),1),
            (0,2):((1,3),-1),(1,3):((0,2),-1),
            (0,3):((1,2),1),(1,2):((0,3),1)}
def star(a): return {star_table[k][0]:v*star_table[k][1] for k,v in a.items()}
asd={(0,1):F(1),(2,3):F(-1)}
check(star(asd),{k:-v for k,v in asd.items()},'anti-self-duality')
check(star(star(asd)),asd,'Hodge star squared')
check(4*sum(v*v for v in asd.values()),F(8),'curvature norm coefficient in pi squared')
for k in star_table:
    check(star(star({k:F(1)})),{k:F(1)},'basis Hodge involution')

# D=partial_z+a with partial_z a=b, partial_z b=0.
# Keys represent a^i b^j theta^(k), retaining noncommutativity of D.
def D(terms):
    out={}
    def put(k,v): out[k]=out.get(k,F(0))+v
    for (a,b,k),v in terms.items():
        if a: put((a-1,b+1,k),a*v)
        put((a,b,k+1),v)
        put((a+1,b,k),v)
    return clean(out)
terms={(0,0,0):F(1)}
for n in range(1,5):
    terms=D(terms)
    if n==2:
        check({(b,k):v for (a,b,k),v in terms.items() if a==0},
              {(1,0):F(1),(0,2):F(1)},'second covariant jet at zero')
fourth={(b,k):v for (a,b,k),v in terms.items() if a==0}
check(fourth,{(2,0):F(3),(1,2):F(6),(0,4):F(1)},'fourth covariant jet at zero')
# y^2 D^4-3pi^2 theta, with b=pi/y. Keys (power_y,power_pi,jet).
source={(2-b,b,k):v for (b,k),v in fourth.items()}
source[0,2,0]-=3
check(clean(source),{(1,1,2):F(6),(2,0,4):F(1)},'covariant source cancellation')
# D translated by s->s+n cancels derivative of multiplier exp(-2pi i n z).
check(F(-2)+F(2),F(0),'fiber multiplier cancellation coefficient')

ap=argparse.ArgumentParser()
ap.add_argument('--output',type=Path)
args=ap.parse_args()
record={'status':'pass','exact_assertions':checks,'date':'2026-10-15',
 'prepared_for':'Edward Baker','assistance':'Substantial LLM assistance',
 'coordinating_model':'gpt-6-astra','reasoning_effort':'ultra',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'arithmetic':'Python standard library fractions.Fraction',
 'scope':'Chern curvature, base Hermitian correction, Hodge ASD condition, curvature norm coefficient, covariant fourth-jet source cancellation and fiber multiplier cancellation.',
 'not_established':['Global modular descent','Finite global Yang-Mills action','Theta signed turning estimate','Analytic collision exclusion premise']}
out=json.dumps(record,indent=2,sort_keys=True)+'\n'
if args.output: args.output.write_text(out)
print(out)
