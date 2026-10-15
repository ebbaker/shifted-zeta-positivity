#!/usr/bin/env python3
"""Exact finite-jet checks for the O(T-t) turning core; no theta certification.
Prepared for Edward Baker, 2026-10-15. Substantial LLM assistance.
Recorded coordinating model gpt-6-astra, reasoning effort ultra.
Uses only Python's standard library. The universal theorem is analytic.
"""
from fractions import Fraction as Q
from math import factorial, comb
import argparse
import hashlib
import json
from pathlib import Path

CHECKS = 0

def check(truth, message):
    global CHECKS
    CHECKS += 1
    if not truth:
        raise AssertionError(message)

def clean(poly):
    return {key: value for key, value in poly.items() if value}

def dx(poly, order=1):
    out = {}
    for (p, q), c in poly.items():
        if q >= order:
            out[p, q-order] = c * Q(factorial(q), factorial(q-order))
    return clean(out)

def ds(poly):
    return clean({(p-1, q): p*c for (p, q), c in poly.items() if p})

def heat_polynomial(germ):
    out = {}
    for degree, c in germ.items():
        for p in range(degree//2 + 1):
            out[p, degree-2*p] = c * Q(factorial(degree), factorial(p)*factorial(degree-2*p))
    return clean(out)

def inner(poly, c1, c2, cutoff):
    """Substitute x=s*(xi+c1)+c2*s^2, retaining powers s<=cutoff."""
    out = {}
    for (p, q), c in poly.items():
        if p+q > cutoff:
            continue
        for b in range(min(q, cutoff-p-q)+1):
            for a in range(q-b+1):
                coeff = c * comb(q, b)*comb(q-b, a)*c2**b*c1**(q-b-a)
                key = p+q+b, a
                out[key] = out.get(key, Q(0)) + coeff
    return clean(out)

def at_s(poly, power):
    return clean({(0, q): c for (p, q), c in poly.items() if p == power})

def mul(a, b, cutoff):
    out = {}
    for (p, q), c in a.items():
        for (i, j), d in b.items():
            if p+i <= cutoff:
                key = p+i, q+j
                out[key] = out.get(key, Q(0)) + c*d
    return clean(out)

def add(a, b, factor=1):
    out = dict(a)
    for key, c in b.items():
        out[key] = out.get(key, Q(0)) + factor*c
    return clean(out)

cases = []
for j in (0, 1):
    for r in range(1, 13):
        m = 2*r+j
        for label, sign, perturbed in (("pure", 1, False), ("asymmetric", 1, True), ("negative_asymmetric", -1, True)):
            germ = {m: sign*Q(r+1, r+2)}
            if perturbed:
                germ.update({m+1: Q(2*r+1, 3*r+2), m+2: -Q(r+2, 5), m+3: Q(7, r+3), m+4: -Q(11, 13)})
            H = heat_polynomial(germ)
            check(ds(H) == dx(H, 2), (j, r, label, "heat equation in s=T-t"))
            W, Wx, Wxx = (dx(H, j+k) for k in (0, 1, 2))
            A = factorial(m)*germ[m]
            B = factorial(m+1)*germ.get(m+1, Q(0))
            k = A / factorial(r)
            c1 = -B/(r*A)
            first_Wx = inner(Wx, c1, Q(0), r+2)
            c2 = -first_Wx.get((r+1, 0), Q(0))/(k*r)
            w, v, z = (inner(poly, c1, c2, r+2) for poly in (W, Wx, Wxx))
            check(all(p >= r for p, _ in w), (j, r, label, "W valuation"))
            check(all(p >= r for p, _ in v), (j, r, label, "Wx valuation"))
            check(all(p >= r-1 for p, _ in z), (j, r, label, "Wxx valuation"))
            check(at_s(w, r) == {(0, 0): k}, (j, r, label, "W core"))
            check(at_s(v, r) == {(0, 1): k*r}, (j, r, label, "Wx core"))
            check(at_s(z, r-1) == {(0, 0): k*r}, (j, r, label, "Wxx core"))
            check(v.get((r+1, 0), Q(0)) == 0, (j, r, label, "stationary center through second order"))
            numerator = add(mul(w, z, 2*r), mul(v, v, 2*r), -1)
            denominator = add(mul(w, w, 2*r), mul(v, v, 2*r))
            check(at_s(numerator, 2*r-1) == {(0, 0): k*k*r}, (j, r, label, "angular numerator"))
            check(at_s(denominator, 2*r) == {(0, 0): k*k, (0, 2): k*k*r*r}, (j, r, label, "angular denominator"))
            if j == 1:
                h = inner(H, c1, c2, r+2)
                check(all(p >= r+1 for p, _ in h), (j, r, label, "physical odd branch H valuation"))
                physical = add(mul(h, h, 2*r), mul(w, w, 2*r))
                check(at_s(physical, 2*r) == {(0, 0): k*k}, (j, r, label, "physical energy differs from jet denominator"))
            cases.append({"j": j, "r": r, "profile": label})
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, help="Optional JSON verification receipt")
args = parser.parse_args()
script = Path(__file__)
result = {
    "status": "pass",
    "date": "2026-10-15",
    "timezone": "America/New_York",
    "prepared_for": "Edward Baker",
    "assistance": "Substantial LLM assistance; exact finite algebra checks do not replace the analytic proof.",
    "model": "gpt-6-astra",
    "effort": "ultra",
    "script_name": script.name,
    "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
    "exact_assertions": CHECKS,
    "cases": len(cases),
    "multiplicities": "m=2r+j; j=0,1; r=1,...,12",
    "germs": ["pure", "asymmetric", "negative_asymmetric"],
    "scope": "Exact finite heat-polynomial identities, stationary-center coefficients, inner jet and angular rational profile. No interval arithmetic or theta sign certificate.",
}
encoded = json.dumps(result, indent=2) + "\n"
if args.output:
    args.output.write_text(encoded, encoding="utf-8")
print(encoded, end="")
