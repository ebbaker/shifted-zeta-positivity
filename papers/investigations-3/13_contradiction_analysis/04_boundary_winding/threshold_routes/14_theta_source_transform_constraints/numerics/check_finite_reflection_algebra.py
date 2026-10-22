#!/usr/bin/env python3
"""Exact transcription checks for BW-14 Note 05; not a theta sign pilot.

Prepared for Edward Baker, 21 October 2026, with substantial LLM assistance.
Recorded model gpt-6-astra (Codex), reasoning effort max.
Uses only Python's standard library. The analytic proofs are in Note 05.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform


def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, F(0)) + v
    return {k: v for k, v in c.items() if v}


def scale(a, c):
    return {k: v * c for k, v in a.items() if v * c}


def mul(a, b):
    c = {}
    for k, v in a.items():
        for l, w in b.items():
            c[k + l] = c.get(k + l, F(0)) + v * w
    return {k: v for k, v in c.items() if v}


def series_mul(a, b, order):
    out = [{} for _ in range(order + 1)]
    for j in range(order + 1):
        for k in range(j + 1):
            out[j] = add(out[j], mul(a[k], b[j-k]))
    return out


def run():
    order = 9
    # Coefficients in u, each an exact polynomial in lambda. Factor e^-lambda.
    exp4 = [{0: F(4**j, factorial(j))} for j in range(order+1)]
    exp5 = [{0: F(5**j, factorial(j))} for j in range(order+1)]
    exponent = [{}] + [{1: F(-4**j, factorial(j))} for j in range(1, order+1)]
    exp_exponent = [{0: F(1)}] + [{} for _ in range(order)]
    for n in range(1, order+1):
        for k in range(1, n+1):
            exp_exponent[n] = add(exp_exponent[n],
                scale(mul(exponent[k], exp_exponent[n-k]), F(k, n)))
    polynomial = [mul({2: F(2)}, q) for q in exp4]
    polynomial[0] = add(polynomial[0], {1: F(-3)})
    direct = series_mul(series_mul(exp5, exp_exponent, order), polynomial, order)

    # Independent repeated-derivative recurrence for lambda e^(5u-z) P_j(z).
    polys = [{0: F(-3), 1: F(2)}]
    for j in range(order):
        p = polys[-1]
        derivative = {k-1: k*v for k, v in p.items() if k}
        polys.append(add(mul({0: F(5), 1: F(-4)}, p),
                         mul({1: F(4)}, derivative)))
    for j in range(order+1):
        expected = {k+1: v/F(factorial(j)) for k, v in polys[j].items()}
        if direct[j] != expected:
            raise ArithmeticError(f"source derivative mismatch at order {j}")
    if polys[1] != {0: F(-15), 1: F(30), 2: F(-8)}:
        raise ArithmeticError("first source-derivative sign mismatch")

    # Compare heat-weighted cosine endpoint expansion with the finite connector.
    checked = 0
    for h in range(1, 9):
        for r in range(h):
            ell = h-r-1
            for j in range(3):
                connector = F((-1)**(r+1+ell+j)*factorial(2*h-1+j),
                              factorial(2*r+1)*factorial(ell))
                cosine = F((-1)**h*factorial(2*h-1),
                           factorial(2*r+1)*factorial(ell))
                differentiated = cosine*F((-1)**j*factorial(2*h+j-1),
                                           factorial(2*h-1))
                if connector != differentiated:
                    raise ArithmeticError("connector/physical derivative mismatch")
                checked += 1

    # The two example near-boundary exponents have exact conservative negatives.
    first_upper = F(7, 4)+4*(1-F(8, 3))
    second_upper = F(3, 4)+8*(1-24)
    if first_upper != F(-59, 12) or second_upper != F(-733, 4):
        raise ArithmeticError("asymptotic exponent arithmetic mismatch")

    return {
        "status": "passed",
        "date_local": "2026-10-21",
        "model": "gpt-6-astra",
        "reasoning_effort": "max",
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact rational polynomial coefficients; Python standard library",
        "source_derivative_orders": [0, order],
        "endpoint_orders": [2, 16],
        "physical_derivative_orders": [0, 2],
        "endpoint_coefficient_comparisons": checked,
        "first_source_polynomial": {str(k): str(v) for k, v in sorted(polys[1].items())},
        "example_rate_exponent_upper_bounds": [str(first_upper), str(second_upper)],
        "scope": "Transcription, normalization and sign checks only. No theta acquisition, interval certificate, collision test, or independent proof verification."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = run()
    rendered = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")
