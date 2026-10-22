#!/usr/bin/env python3
"""Chern/Hopf signs and quadratic controls; no theta certificate.
Prepared for Edward Baker with LLM assistance, gpt-6-astra, effort ultra,
22 October 2026. Standard-library exact fractions plus labelled floating
quadrature diagnostics; written analytic proofs remain in shared Notes 01–02.
"""
from fractions import Fraction as F
from pathlib import Path
import cmath
import hashlib
import json
import math


def wedge(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            if set(i) & set(j):
                continue
            sign = (-1)**sum(v > w for v in i for w in j)
            k = tuple(sorted(i+j))
            out[k] = out.get(k, F(0)) + sign*x*y
    return {k: v for k, v in out.items() if v}


def scale(c, a):
    return {k: c*v for k, v in a.items() if c*v}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0))+v
    return {k: v for k, v in out.items() if v}


def simpson(f, a, b, n):
    assert n % 2 == 0
    step = (b-a)/n
    return step/3*(f(a)+f(b)+sum((4 if j % 2 else 2)*f(a+j*step) for j in range(1,n)))


def run():
    # Coordinate order: (r, phi1, u, phi2); exact exterior-algebra controls.
    da = {(2,3): F(1), (1,2): F(1)}
    orientation_cases = 0
    for u in [F(1,4), F(1,2), F(9,25)]:
        a = {(1,): 1-u, (3,): u}
        assert wedge(a, da) == {(1,2,3): F(1)}
        assert wedge(da, da) == {}  # pulled-back CP1 curvature square
        for n in [-2, 0, 3]:
            assert wedge(add(a, {(1,): F(n)}), da) == {(1,2,3): F(n+1)}
        for r, delta in [(F(1), F(1,3)), (F(2), F(1,5))]:
            k = r*r/(r*r+delta*delta)
            kp = 2*r*delta*delta/(r*r+delta*delta)**2
            dad = add(wedge({(0,): kp}, a), scale(k, da))
            assert wedge(scale(k,a), dad) == {(1,2,3): k*k}
            assert wedge(dad,dad) == {(0,1,2,3): 2*k*kp}
            assert 0 <= 1-k*k <= 2*delta*delta/(r*r)
        orientation_cases += 1
    # Exact quadratic inverse: z=Z2/2, tau=Z2^2/8-Z1/2, H=z^2-2tau.
    inverse_cases = 0
    for z1, z2 in [(F(2), F(3)), (F(-1,4), F(2,5)), (F(3,7), F(0))]:
        z = z2/2
        tau = z2*z2/8-z1/2
        assert z*z-2*tau == z1 and 2*z == z2
        inverse_cases += 1
    # Direct quadratic face density on p-disk, before harmonic averaging.
    # Floating Simpson/trapezoid comparison is diagnostic, not an enclosure.
    P = 1.0
    T = Y = 0.05
    kappa = P*P/(1+P*P)
    radial_n, angular_n, heat_n = 32, 32, 64
    def density(tau, tangent):
        def radial(s):
            def at_angle(j):
                p = math.sqrt(s)*cmath.exp(2j*math.pi*j/angular_n)
                root = cmath.sqrt(1+2*p*p*tau)
                z = -2*p*tau/(1+root)
                h = z*z-2*tau
                ztau = -p/(1-p*z)
                return ((-2+2*z*ztau)*tangent/h).imag
            return sum(at_angle(j) for j in range(angular_n))*(2*math.pi/angular_n)/(1+s)**2
        return simpson(radial, 0.0, P*P, radial_n)/(4*math.pi**2)
    edges = [('late', lambda v: T+1j*v, 1j, -Y, Y),
             ('top', lambda v: v+1j*Y, 1, T, -T),
             ('early', lambda v: -T+1j*v, 1j, Y, -Y),
             ('bottom', lambda v: v-1j*Y, 1, -T, T)]
    rows = []
    for name, curve, tangent, lo, hi in edges:
        val = simpson(lambda v: density(curve(v),tangent), lo, hi, heat_n)
        expected = kappa/4
        err = abs(val-expected)
        assert err < 5e-8, (name,val,err)
        rows.append({'face':name, 'direct_quadrature_display':val,
                     'analytic_value': '1/8', 'absolute_difference_display':err})
    return {'date':'2026-10-22', 'author':'Prepared for Edward Baker',
            'llm_assistance':True, 'model':'gpt-6-astra', 'effort':'ultra',
            'scope':'Exact algebraic control cases and noncertified quadratic quadrature diagnostics only; not theta data, a general proof, or independent review.',
            'exterior_algebra_control_cases':orientation_cases,
            'quadratic_inverse_control_cases':inverse_cases,
            'quadrature':{'P':P,'T':T,'Y':Y,'radial_simpson_n':radial_n,
                          'angular_trapezoid_n':angular_n,'heat_simpson_n':heat_n,
                          'acceptance_absolute_difference':5e-8,'faces':rows},
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status':'passed'}


if __name__ == '__main__':
    out=Path(__file__).with_name('CHB_ANALYTIC_CHECKS_20261022.json')
    result=run()
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'receipt':str(out),
                      'maximum_quadrature_difference':max(x['absolute_difference_display'] for x in result['quadrature']['faces'])}))
