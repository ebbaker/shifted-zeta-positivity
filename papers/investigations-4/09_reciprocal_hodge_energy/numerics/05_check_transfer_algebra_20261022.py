#!/usr/bin/env python3
"""Exact small checks for RHE transfer Notes 09--11, not theta certificates."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


def add(a, b):
    return [(a[k] if k < len(a) else 0) + (b[k] if k < len(b) else 0)
            for k in range(max(len(a), len(b)))]


def scale(a, c):
    return [c*x for x in a]


def mul(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def diff(a):
    return [k*a[k] for k in range(1, len(a))] or [0]


def integral(a, left=Q(-1), right=Q(1)):
    return sum(Q(v,k+1)*(right**(k+1)-left**(k+1)) for k,v in enumerate(a))


def exp_integral_coefficients(a):
    # Integral_0^1 exp(y)*p(y) = A*exp(1)+B, with exact rational A,B.
    primitive = [Q(0)]*len(a)
    derivative = list(a)
    sign = 1
    while any(derivative):
        primitive = add(primitive,scale(derivative,sign))
        derivative = diff(derivative)
        sign = -sign
    return sum(primitive), -primitive[0]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    bump=[Q(1),0,Q(-3),0,Q(3),0,Q(-1)]
    mass=integral(bump)
    assert mass==Q(32,35)
    # For the actual heat solution H(t,z)=exp(t)cos(z), J at t=0 is exp(-iz).
    # u=exp(y), mu=u, T=mass. Green gives integral exp(y)(chi''-chi)=1.
    exp_pair=exp_integral_coefficients(add(diff(diff(bump)),scale(bump,-1)))
    assert exp_pair==(0,1)
    # For u=|z^2|=x^2+y^2, mu=4 and the bottom normal trace vanishes.
    chi_mass=integral(bump,Q(0),Q(1))
    x2_second=integral(mul([0,0,1],diff(diff(bump))))
    y2_second=integral(mul([0,0,1],diff(diff(bump))),Q(0),Q(1))
    green_potential=x2_second*chi_mass+mass*y2_second
    green_mass=4*mass*chi_mass
    assert green_potential==green_mass==Q(2048,1225)
    fixture=[]
    for a in [Q(0),Q(1,2),Q(2)]:
        field=[-a,0,1]
        field_p=diff(field)
        laguerre=add(mul(field_p,field_p),scale(mul(field,diff(field_p)),-1))
        direct=integral(mul(bump,laguerre))
        integrated=2*integral(mul(bump,mul(field_p,field_p)))-Q(1,2)*integral(mul(diff(diff(bump)),mul(field,field)))
        assert direct==integrated
        fixture.append({'a':str(a),'signed_Laguerre_integral':str(direct)})
    # The half-rectangle cutoff norm bound has coefficient 6144/(875 sqrt(5)).
    assert Q(384,25)*Q(16,35)==Q(32,35)*Q(192,25)==Q(6144,875)
    # Complete Taylor derivative-tail / field-tail ratio for N=65,rho=1/2,R=16.
    ratio=Q(1,16)*(Q(65)/(1-Q(1,2))+Q(1,2)/(1-Q(1,2))**2)/Q(1,2)/(1/(1-Q(1,2)))
    assert ratio==Q(33,4)
    result={'date':'2026-10-22','prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra',
            'status':'exact integer and rational checks passed',
            'scope':'Finite algebra and normal-sign checks only; not proof certification, theta acquisition, a trace integral enclosure or an endpoint exclusion.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'cosine_heat_jet_Green_exp_coefficients':[str(v) for v in exp_pair],
            'quadratic_modulus_Green_potential_and_mass':str(green_mass),
            'signed_functional_fixtures':fixture,
            'half_cutoff_norm_coefficient_without_sqrt5':str(Q(6144,875)),
            'Taylor_derivative_to_field_tail_ratio':str(ratio)}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'output':str(args.output)}))


if __name__=='__main__':
    main()
