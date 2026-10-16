#!/usr/bin/env python3
"""Exact-rational algebra and endpoint checks for prime-density centering.

Synthetic kernel: f(v)=(v-1)^8(2-v)^8 on [1,2], H(v)=v*f(v),
ell=-H'. The point measure has weight p at each prime p, not log(p).
These deliberately rational inputs test identities valid for any atomic
measure; they are not numerical evidence about the fixed arithmetic probe.
Substantial LLM assistance, GPT-6 (Codex), inherited configuration.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import platform


def multiply(a, b):
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def power(a, n):
    result = [F(1)]
    for _ in range(n):
        result = multiply(result, a)
    return result


def poly_value(coefficients, x):
    result = F(0)
    for c in reversed(coefficients):
        result = result * x + c
    return result


FPOLY = multiply(power([F(-1), F(1)], 8), power([F(2), F(-1)], 8))
HPOLY = [F(0)] + FPOLY
LPOLY = [-i * HPOLY[i] for i in range(1, len(HPOLY))]
FPRIMITIVE = [F(0)] + [c / (i + 1) for i, c in enumerate(FPOLY)]
FMOMENT = poly_value(FPRIMITIVE, F(2)) - poly_value(FPRIMITIVE, F(1))
Q = F(7, 3)


def kernel(poly, x):
    return poly_value(poly, x) if 1 < x < 2 else F(0)


def f(x):
    return kernel(FPOLY, x)


def h(x):
    return kernel(HPOLY, x)


def ell(x):
    return kernel(LPOLY, x)


def floor(x):
    return x.numerator // x.denominator


def arithmetic(limit):
    prime = [True] * (limit + 1)
    prime[:2] = [False, False]
    for p in range(2, limit + 1):
        if prime[p]:
            for n in range(p * p, limit + 1, p):
                prime[n] = False
    primes = [p for p in range(2, limit + 1) if prime[p]]
    mu = [1] * (limit + 1)
    mu[0] = 0
    for p in primes:
        for n in range(p, limit + 1, p):
            mu[n] *= -1
        for n in range(p * p, limit + 1, p * p):
            mu[n] = 0
    return primes, mu


def run_case(X, U):
    assert U >= 1 and U * U <= X
    cap = floor(2 * X / U)
    primes, mu = arithmetic(cap)
    ms = range(floor(U) + 1, cap + 1)
    aa = {}
    comparisons = 0
    for m in ms:
        direct = sum(mu[d] for d in range(floor(U) + 1, m + 1) if m % d == 0)
        expanded = -sum(mu[d] for d in range(1, floor(U) + 1) if m % d == 0)
        assert direct == expanded
        aa[m] = direct
        comparisons += 1
    N = X / U
    m1 = sum((F(mu[d], d) for d in range(1, floor(U) + 1)), F(0))
    continuum = FMOMENT * m1 / Q
    density = sum((F(aa[m], m) * h(m / N) for m in ms), F(0)) / Q
    divisor_density = F(0)
    lattice_remainder = F(0)
    for d in range(1, floor(U) + 1):
        lattice_sum = sum((f(d * F(k) / N) for k in range(1, floor(2 * N / d) + 1)), F(0))
        divisor_density -= mu[d] * lattice_sum / (Q * N)
        lattice_remainder -= mu[d] * (lattice_sum - N * FMOMENT / d) / (Q * N)
    assert density == divisor_density
    assert density + continuum == lattice_remainder

    # Right-continuous theta with rational atom weight p.
    theta_U = F(sum(p for p in primes if p <= U))
    error_U = theta_U - U
    prime_scalar = F(0)
    boundary = F(0)
    bulk = F(0)
    for m in ms:
        scale = X / m
        atom_sum = sum((p * ell(F(p) / scale) for p in primes if p > U), F(0))
        prime_scalar += aa[m] * atom_sum / (Q * X)
        boundary -= aa[m] * error_U * ell(U / scale) / (Q * X)
        endpoint = 2 * scale
        theta_segment = theta_U
        left = U
        integral_error_gprime = F(0)
        points = [F(p) for p in primes if U < p < endpoint] + [endpoint]
        for right in points:
            gl, gr = ell(left / scale), ell(right / scale)
            # Integral (theta_segment - t)*g'(t) on this interval.
            integral_error_gprime += (
                theta_segment * (gr - gl) - right * gr + left * gl
                + scale * (h(left / scale) - h(right / scale))
            )
            if right.denominator == 1 and int(right) in primes:
                theta_segment += right
            left = right
        bulk -= aa[m] * integral_error_gprime / (Q * X)
    discrepancy = prime_scalar - density
    assert discrepancy == boundary + bulk
    assert continuum + prime_scalar == lattice_remainder + discrepancy
    comparisons += 4
    return comparisons, boundary != 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    comparisons = cases = negative_controls = 0
    for U in [F(2), F(5, 2), F(3), F(4), F(5), F(11, 2), F(7), F(13, 2)]:
        for factor in [F(1), F(9, 8), F(3, 2), F(2)]:
            n, boundary_needed = run_case(U * U * factor, U)
            comparisons += n
            cases += 1
            negative_controls += int(boundary_needed)
    assert negative_controls > 0, "The control must detect omitted cutoff boundaries."
    result = {
        "date": "2026-10-04",
        "status": "EXACT_RATIONAL_ALGEBRA_CHECK",
        "cases": cases,
        "exact_comparisons": comparisons,
        "omitted_boundary_control_failures": negative_controls,
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Synthetic compact polynomial kernel, exact Mobius coefficients, prime atoms weighted by p.",
        "limitations": "Not the fixed probe; no derivative-TV or global asymptotic estimate is certified.",
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
