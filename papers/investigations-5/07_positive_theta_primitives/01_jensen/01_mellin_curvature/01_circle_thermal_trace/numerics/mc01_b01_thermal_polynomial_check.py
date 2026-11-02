#!/usr/bin/env python3
"""MC01-B01 exact algebra support: P0..P4 and one fixed confluent witness.
Prepared for Edward Baker with LLM assistance, gpt-6-astra / ultra,
1 November 2026 America/New_York. No theta truncation or numerical campaign.
"""
from fractions import Fraction as Q
import json

def derivative(p):
    return [i*p[i] for i in range(1,len(p))]

def value(p,x):
    return sum(c*x**i for i,c in enumerate(p))

def quotient_jet(p,d,x):
    f=value(p,x)/value(d,x)
    first=(value(derivative(p),x)-f*value(derivative(d),x))/value(d,x)
    second=(value(derivative(derivative(p)),x)-2*first*value(derivative(d),x)-f*value(derivative(derivative(d)),x))/value(d,x)
    return f,first,second

p0=[Q(0),Q(-3),Q(2)]
polys=[p0]
for _ in range(4):
    p=polys[-1]; nxt=[Q(0)]*(len(p)+1)
    for i,c in enumerate(p):
        nxt[i]+=(1+4*i)*c
        nxt[i+1]-=4*c
    polys.append(nxt)
assert polys[2]==[0,-75,330,-224,32]
assert polys[4]==[0,-1875,30930,-68096,41408,-8448,512]
x=Q(4)
r,r1,r2=quotient_jet(polys[2],p0,x)
z,z1,z2=quotient_jet(polys[4],p0,x)
h=(z2*r1-z1*r2)/(2*r1**3)
assert r1==Q(952,25)
assert h==Q(-157375,99127)
print(json.dumps({'arithmetic':'Python fractions.Fraction, exact rational',
 'scope':'P0 through P4; only x=4 is the fixed witness; no canonical-source truncation',
 'polynomials_constant_first':[[int(c) for c in p] for p in polys],
 'x':str(x),'r':str(r),'r_x':str(r1),'r_xx':str(r2),
 'z':str(z),'z_x':str(z1),'z_xx':str(z2),'confluent_h3':str(h),
 'assertions_passed':True},indent=2))
