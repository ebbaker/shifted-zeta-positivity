#!/usr/bin/env python3
"""Exact rational checks for theta elliptic-defect stability constants.

14 October 2026. Prepared for Edward Baker with LLM assistance (gpt-6.1-sol, ultra).
All decisions use fractions; no sampled theta values enter this checker.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def theta_derivative(p):
    # (5 + 4q d/dq)[p(q) exp(-q)] = p_next(q) exp(-q).
    out = [0] * (len(p) + 1)
    for k, coefficient in enumerate(p):
        out[k] += (5 + 4 * k) * coefficient
        out[k + 1] -= 4 * coefficient
    return out


def atan_interval(inv, terms):
    x = F(1, inv)
    total = sum(((-1)**k * x**(2*k + 1) / (2*k + 1)
                 for k in range(terms)), F(0))
    nxt = (-1)**terms * x**(2*terms + 1) / (2*terms + 1)
    return min(total, total + nxt), max(total, total + nxt)


def polynomial_interval(coefficients, left, right):
    lo = hi = F(0)
    for coefficient in coefficients[::-1]:
        products = [lo * left, lo * right, hi * left, hi * right]
        lo, hi = min(products) + coefficient, max(products) + coefficient
    return lo, hi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, proposition, evidence=None):
        assert proposition, name
        entry = {'name': name, 'passed': True}
        if evidence is not None:
            entry['evidence'] = evidence
        checks.append(entry)

    # The partial exponential series proves exp(3)>20.
    exp3_partial = sum((F(3)**k / factorial(k) for k in range(9)), F(0))
    check('exp(3)>20 from positive Taylor terms', exp3_partial > 20,
          str(exp3_partial))
    pi_upper = F(22, 7)
    r = F(1, 160000)
    rho0, rho = F(1, 2000), F(1, 8000)
    bounds = [F(1, 2), F(1, 8), F(1, 12), F(1, 12)]
    c_squared = []
    for j in range(4):
        a_upper = 2 * pi_upper**2 * factorial(j) / 3**(j + 1)
        if j == 0:
            s4 = (1 + 11*r + 11*r*r + r**3) / (1-r)**5
            majorant = (a_upper / 20 / (1-rho0))**2 * s4
        else:
            majorant = (a_upper / 20 / (1-rho))**2 / (1-r)
        c_squared.append(str(majorant))
        check(f'C{j} squared rational majorant', majorant < bounds[j]**2,
              {'majorant': str(majorant), 'target': str(bounds[j]**2)})

    b0, b1, b2, b3 = bounds
    l0_quadratic = b1*b1 + b0*b2
    l1_quadratic = b2*b2 + b1*b3
    check('L0 quadratic coefficient', l0_quadratic == F(11, 192))
    check('L1 quadratic coefficient', l1_quadratic == F(5, 288))
    check('L0 linear coefficient',
          2*b1*b1 + b0*b2 + b2*b0 == 2*l0_quadratic)
    check('L1 linear coefficient',
          2*b2*b2 + b1*b3 + b3*b1 == 2*l1_quadratic)

    defect, delta = F(1, 30000), F(1, 120000)
    check('local slope gap', delta-defect*b1 == F(1, 240000))
    check('local second-derivative gap', delta-defect*b2 == F(1, 180000))
    origin_anchor = F(3, 125)
    inner_anchor = F(7733, 350000)
    check('original inner anchor exceeds 1/50', inner_anchor > F(1, 50))
    check('perturbed origin remains above 1/50',
          origin_anchor-defect*b0 > F(1, 50))
    check('perturbed inner region remains above 1/100',
          F(1, 50)-defect*b0 > F(1, 100))
    check('central norm gap from inner value and outer slope alternatives',
          min(F(1, 100), delta-defect*b1) == F(1, 240000))
    check('origin stationary L0 positive margin',
          F(1, 50)*(delta-defect*b2) == F(1, 9000000))

    p0 = [-3, 2]
    p1 = theta_derivative(p0)
    p2 = theta_derivative(p1)
    p3 = theta_derivative(p2)
    check('P1 recurrence', p1 == [-15, 30, -8])
    check('P2 recurrence', p2 == [-75, 330, -224, 32])
    check('P3 recurrence', p3 == [-375, 3270, -4232, 1440, -128])
    first = mul(p1, [coefficient*4**k for k, coefficient in enumerate(p3)])
    second = mul([coefficient*4**k for k, coefficient in enumerate(p1)], p3)
    determinant_poly = [a-b for a, b in zip(first, second)]
    check('determinant polynomial identity', determinant_poly ==
          [0, -113400, 907200, -2570400, 3081600, -1520640, 245760])
    a_lo, a_hi = atan_interval(5, 12)
    b_lo, b_hi = atan_interval(239, 4)
    pi_lo, pi_hi = 16*a_lo-4*b_hi, 16*a_hi-4*b_lo
    simple_lo = F(314159265358979, 10**14)
    simple_hi = F(314159265358980, 10**14)
    check('Machin alternating bounds enclose pi in simple rational interval',
          simple_lo < pi_lo < pi_hi < simple_hi)
    det_lo, det_hi = polynomial_interval(determinant_poly, simple_lo, simple_hi)
    check('remote-collision determinant positive',
          F(4598266, 10**6) < det_lo < det_hi < F(4598268, 10**6),
          {'lower': str(det_lo), 'upper': str(det_hi)})

    record = {
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic': 'Python standard-library Fraction; all decisions exact',
        'date': '2026-10-14', 'prepared_for': 'Edward Baker',
        'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra',
        'scope': 'Algebraic constants and determinant control; no theta sign certificate',
        'checks': checks,
    }
    if args.output:
        args.output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'passed': len(checks), 'output': str(args.output) if args.output else None}))


if __name__ == '__main__':
    main()
