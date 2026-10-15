#!/usr/bin/env python3
"""Exact algebra checks for Note 57. Standard library only; no theta certificate."""
from fractions import Fraction as F
from math import factorial
import argparse
import hashlib
import json
from pathlib import Path

checks = 0

def check(a, b, description):
    global checks
    assert a == b, (description, a, b)
    checks += 1

def clean(p):
    return {k: v for k, v in p.items() if v}

def add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)

def derivative(p, variable):
    out = {}
    for (s, x), v in p.items():
        e = (s, x)[variable]
        if e:
            key = (s - (variable == 0), x - (variable == 1))
            out[key] = out.get(key, F(0)) + e * v
    return clean(out)

def dx(p, n):
    for _ in range(n):
        p = derivative(p, 1)
    return p

def heat_monomial(m, amplitude=F(1)):
    # Independent finite exponential e^(s d_x^2)(amplitude*x^m/m!).
    return {(p, m-2*p): amplitude / (factorial(p)*factorial(m-2*p))
            for p in range(m//2+1)}

def center(p):
    return {s: v for (s, x), v in p.items() if x == 0}

def shift_linear(p, slope):
    out = {}
    for (s, x), v in p.items():
        out[s+x] = out.get(s+x, F(0)) + v*slope**x
    return {s: v for s, v in out.items() if v}

def product_laurent(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            out[a+b] = out.get(a+b, F(0)) + x*y
    return clean(out)

for r in range(1, 13):
    for j in (0, 1):
        m = 2*r+j
        H = heat_monomial(m)
        check(derivative(H, 0), dx(H, 2), 'finite backward heat equation')
        W = dx(H, j)
        check(center(dx(W, 1)), {}, 'canonical stationary predecessor')
        check(center(W), {r: F(1, factorial(r))}, 'central amplitude')
        check(center(dx(W, 2)), {r-1: F(1, factorial(r-1))}, 'stationary curvature')
        # Scale s=1, x=z, normalize by the center. This is independent
        # of the closed formula through derivative of the heat polynomial.
        profile = {x: v*factorial(r) for (s, x), v in W.items()}
        formula = {2*l: F(factorial(r), factorial(r-l)*factorial(2*l))
                   for l in range(r+1)}
        check(profile, formula, 'normalized heat profile')

        # Perturb the event germ. Substitution of the leading stationary
        # displacement verifies the odd-branch physical-energy comparison.
        A, B, D = F(2), F(3), F(5)
        Hp = add(add(heat_monomial(m, A), heat_monomial(m+1, B)),
                 heat_monomial(m+2, D))
        slope = -B/(r*A)
        Wp = shift_linear(dx(Hp, j), slope)
        check(Wp.get(r, 0), A/factorial(r), 'perturbed leading W')
        Wxp = shift_linear(dx(Hp, j+1), slope)
        check(Wxp.get(r, 0), 0, 'leading stationary displacement')
        if j:
            shifted_H = shift_linear(Hp, slope)
            check(shifted_H.get(r, 0), 0, 'odd lower physical component order')
            check(shifted_H.get(r+1, 0)/Wp[r], -B/(r*(r+1)*A),
                  'odd H/W coefficient; E/W^2 = 1+O(s^2)')

    for rho2 in (F(1, 3), F(2), F(7, 2), F(11)):
        # Re F on a circle is a Laurent polynomial in exp(i theta).
        # Its integral is the coefficient of exponent zero, checked by
        # multiplication, not by sampling angles.
        real_boundary = {0: F(1)}
        for l in range(1, r+1):
            coefficient = formula[2*l]*rho2**l/2
            real_boundary[2*l] = coefficient
            real_boundary[-2*l] = coefficient
        q = {0: F(1), 2: F(-1, 2), -2: F(-1, 2)}
        check(product_laurent(q, real_boundary).get(0, F(0)),
              1-F(r, 4)*rho2, 'weighted signed-current Fourier projection')

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path)
args = parser.parse_args()
record = {
    'status': 'pass',
    'exact_assertions': checks,
    'date': '2026-10-15',
    'prepared_for': 'Edward Baker',
    'assistance': 'Substantial LLM assistance',
    'coordinating_model': 'gpt-6-astra',
    'coordinating_reasoning_effort': 'ultra',
    'model_provenance': 'Verified and supplied by the parent conversation; internal work inherited that configuration.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'multiplicity_r_range': [1, 12],
    'physical_branches': [0, 1],
    'arithmetic': 'stdlib fractions.Fraction',
    'scope': 'Finite exact heat-polynomial, perturbed predecessor leading-term, and circle Fourier-projection checks. No theta numerical calculation or interval certificate.',
    'analytic_claims_not_tested_by_this_checker': [
        'Uniform holomorphic-circle convergence',
        'Strict positivity of the limiting positive and negative masses',
        'Optimization and limiting arguments for varying radii',
    ],
}
serialized = json.dumps(record, indent=2, sort_keys=True) + '\n'
if args.output:
    args.output.write_text(serialized)
print(serialized)
