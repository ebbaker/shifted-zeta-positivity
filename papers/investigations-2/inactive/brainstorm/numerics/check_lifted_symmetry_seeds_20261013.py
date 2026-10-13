#!/usr/bin/env python3
"""Exact finite controls for the lifted theta symmetry brainstorm.

Prepared for Edward Baker with substantial LLM assistance, 13 October 2026.
Model: gpt-6.1-sol (Codex), reasoning effort ultra.

These rational matrix checks diagnose coordinate, moving-symmetry, and
cutoff bookkeeping. They are not tests of genuine theta nonvanishing.
Only the Python standard library is used; no downloaded inputs are needed.
"""
import argparse
import hashlib
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, c):
    return [[c * x for x in r] for r in a]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(r) for r in zip(*a)]


def det(a):
    b = [r[:] for r in a]
    v = F(1)
    for j in range(len(b)):
        k = next((k for k in range(j, len(b)) if b[k][j]), None)
        if k is None:
            return F(0)
        if k != j:
            b[j], b[k] = b[k], b[j]
            v = -v
        p = b[j][j]
        v *= p
        for k in range(j + 1, len(b)):
            c = b[k][j] / p
            for l in range(j + 1, len(b)):
                b[k][l] -= c * b[j][l]
            b[k][j] = F(0)
    return v


def derivative(d):
    a = zero(d + 1)
    for j in range(1, d + 1):
        a[j - 1][j] = F(j)
    return a


def translation(dmat, c):
    n = len(dmat)
    a, power = eye(n), eye(n)
    for j in range(1, n):
        power = mul(power, dmat)
        a = add(a, scale(power, c ** j / math.factorial(j)))
    return a


def evaluation_pair(d, x):
    return [[x ** j for j in range(d + 1)],
            [F(0) if j == 0 else j * x ** (j - 1)
             for j in range(d + 1)]]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output')
    args = ap.parse_args()
    count = 0

    def check(actual, expected):
        nonlocal count
        assert actual == expected, (actual, expected)
        count += 1

    degrees = []
    for d in range(2, 11):
        n = d + 1
        dm = derivative(d)
        xm = zero(n)
        parity = eye(n)
        for j in range(n):
            parity[j][j] = F((-1) ** j)
            if j < d:
                xm[j + 1][j] = F(1)
        gen = scale(mul(dm, dm), -1)
        check(mul(parity, parity), eye(n))
        check(mul(mul(parity, dm), parity), scale(dm, -1))
        check(mul(mul(parity, xm), parity), scale(xm, -1))
        check(mul(parity, gen), mul(gen, parity))
        comm = add(mul(dm, xm), scale(mul(xm, dm), -1))
        boundary = eye(n)
        boundary[d][d] -= n
        check(comm, boundary)
        check(sum(comm[j][j] for j in range(n)), F(0))

        for a in [F(-2, 3), F(0), F(5, 4)]:
            # S_a f(x)=f(2a-x)=R exp(2a D) f(x).
            sm = mul(parity, translation(dm, 2 * a))
            check(mul(sm, sm), eye(n))
            check(mul(sm, gen), mul(gen, sm))
            # Derivative in the center a, computed term by term.
            power, ds = eye(n), zero(n)
            for j in range(1, n):
                power = mul(power, dm)
                ds = add(ds, scale(power, 2 ** j * a ** (j - 1)
                                   / math.factorial(j - 1)))
            ds = mul(parity, ds)
            check(ds, scale(mul(sm, dm), 2))
            check(ds, scale(mul(dm, sm), -2))

        tm = translation(dm, F(2, 3))
        ti = translation(dm, F(-2, 3))
        check(mul(tm, ti), eye(n))
        observation = evaluation_pair(d, F(7, 5))
        state = [[F((-1) ** j, j + 1)] for j in range(n)]
        check(mul(mul(observation, ti), mul(tm, state)),
              mul(observation, state))
        degrees.append(d)

    # A smooth even heat polynomial retains an exact double zero.
    # H(t,x)=x^2+2T-2t solves H_t=-H_xx and is parity invariant.
    threshold = F(1, 7)
    dm = derivative(2)
    gen = scale(mul(dm, dm), -1)
    parity = [[F(1), F(0), F(0)], [F(0), F(-1), F(0)],
              [F(0), F(0), F(1)]]
    for t in [F(0), threshold, F(2)]:
        coeff = [[2 * threshold - 2 * t], [F(0)], [F(1)]]
        check(mul(gen, coeff), [[F(-2)], [F(0)], [F(0)]])
        check(mul(parity, coeff), coeff)
    collision = [[F(0)], [F(0)], [F(1)]]
    check(mul(evaluation_pair(2, F(0)), collision), [[F(0)], [F(0)]])
    check(mul(mul(dm, dm), collision), [[F(2)], [F(0)], [F(0)]])

    # Connected anchored source with regular bulk matrix, but blind output.
    # This is a generic finite control, not the prescribed theta graph.
    bm = [[F(2), F(1), F(0)], [F(0), F(1, 2), F(1)]]
    q = [[F(1)], [F(-2)], [F(1)]]
    c = [[F(1), F(1), F(1)], [F(0), F(1), F(2)]]
    anchor = zero(3)
    anchor[0][0] = F(1)
    bulk = add(mul(transpose(bm), bm), anchor)
    check(mul(bm, q), [[F(0)], [F(0)]])
    check(mul(bulk, q), [[F(1)], [F(0)], [F(0)]])
    check(det(bulk), F(1))
    check(mul(c, q), [[F(0)], [F(0)]])

    record = {
        'title': 'Exact finite controls for lifted theta symmetry seeds',
        'date': '2026-10-13', 'prepared_for': 'Edward Baker',
        'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra',
        'llm_assistance': 'Substantial LLM assistance; internal check only',
        'arithmetic': 'Exact fractions; no floating comparisons',
        'assertions': count, 'all_pass': True, 'polynomial_degrees': degrees,
        'checks': {
            'parity_intertwines_fixed_heat_generator': True,
            'moving_reflection_center_derivative': 'dS_a/da=2 S_a D=-2 D S_a',
            'finite_cutoff_commutator': '[D,M]=I-(d+1)P_top',
            'passive_chart_preserves_physical_observation': True,
            'parity_symmetric_heat_polynomial_has_double_zero': True,
            'anchored_positive_bulk_can_have_blind_two_channel_output': True,
        },
        'limits': [
            'These are generic finite operator and heat controls',
            'No genuine theta sign, new reflection theorem, or RH implication',
            'Polynomial multiplication is truncated, with boundary term retained',
        ],
        'software': {'python': platform.python_version(),
                     'implementation': platform.python_implementation()},
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    result = json.dumps(record, indent=2) + '\n'
    if args.output:
        Path(args.output).write_text(result)
    print(result)


if __name__ == '__main__':
    main()
