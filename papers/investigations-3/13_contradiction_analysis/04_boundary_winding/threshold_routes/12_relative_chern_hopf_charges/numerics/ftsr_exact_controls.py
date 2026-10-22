#!/usr/bin/env python3
"""Exact rational controls for BW12 finite-time reconstruction.

Prepared for Edward Baker, 21 October 2026, with substantial LLM assistance.
Recorded model: gpt-6-astra (Codex); reasoning effort: ultra.
These are finite algebra checks, not theta-source certificates.
"""
from fractions import Fraction as Q
from math import comb, factorial
import argparse
import hashlib
import json
from pathlib import Path


def trim(p):
    p = list(map(Q, p))
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p or [Q(0)]


def add(p, q):
    r = [Q(0)] * max(len(p), len(q))
    for i, v in enumerate(p):
        r[i] += v
    for i, v in enumerate(q):
        r[i] += v
    return trim(r)


def scale(p, c):
    return trim([c * v for v in p])


def mul(p, q):
    r = [Q(0)] * (len(p) + len(q) - 1)
    for i, v in enumerate(p):
        for j, w in enumerate(q):
            r[i + j] += v * w
    return trim(r)


def deriv(p, n=1):
    for _ in range(n):
        p = trim([i * v for i, v in enumerate(p)][1:])
    return p


def value(p, x):
    return sum(v * x**i for i, v in enumerate(p))


def shift(p, a):
    return trim([sum(p[k] * comb(k, j) * a**(k-j)
                     for k in range(j, len(p))) for j in range(len(p))])


def remainder(p, q):
    p = trim(p)
    q = trim(q)
    while len(p) >= len(q) and p != [0]:
        n = len(p) - len(q)
        p = add(p, [Q(0)] * n + scale(q, -p[-1] / q[-1]))
    return p


def heat(p, t):
    """Exact backward heat polynomial exp(-t d_z^2) p."""
    out = [Q(0)]
    for j in range((len(p)-1)//2 + 1):
        out = add(out, scale(deriv(p, 2*j), (-t)**j / factorial(j)))
    return out


def gaussian_average(p, a, variance):
    s = shift(p, a)
    return sum(s[2*k] * Q(factorial(2*k), 2**k * factorial(k)) * variance**k
               for k in range((len(s)-1)//2 + 1))


def hermite(n):
    h0, h1 = [Q(1)], [Q(0), Q(1)]
    if n == 0:
        return h0
    for k in range(1, n):
        h0, h1 = h1, add(mul([0, 1], h1), scale(h0, -k))
    return h1


def hermite_at(n, a, sigma):
    return scale(shift([v / sigma**i for i, v in enumerate(hermite(n))], -a), 1)


def residue(num, den, b):
    """Coefficient of (z-b)^-1 by exact local formal division."""
    n, d = shift(num, b), shift(den, b)
    order = next(i for i, c in enumerate(d) if c)
    if order == 0:
        return Q(0)
    unit = d[order:]
    quotient = []
    for k in range(order):
        nk = n[k] if k < len(n) else Q(0)
        cross = sum(unit[j] * quotient[k-j]
                    for j in range(1, min(k+1, len(unit))))
        quotient.append((nk-cross) / unit[0])
    return quotient[-1]


def response(f, roots, v):
    c = sum(roots) / 2
    rs = sorted(set(roots))
    integral = lambda num, den: sum(residue(num, den, b) for b in rs)
    linear = -4 * integral(mul([-c, 1], v), f)
    quadratic = 2 * integral(mul([-c, 1], mul(v, v)), mul(f, f))
    quadratic -= integral(v, f)**2
    return linear, quadratic


def run():
    counts = {"gaussian_transfer": 0, "hermite_coefficients": 0,
              "parseval_and_projected_energy": 0, "quotient_response": 0,
              "double_three_jet_response": 0, "affine_collision": 0}
    for degree in range(1, 11):
        p = [Q((-1)**k * (k+1), degree+k+3) for k in range(degree+1)]
        for a in (Q(0), Q(2, 3)):
            for sigma in (Q(1, 2), Q(1), Q(2)):
                t = sigma**2 / 2
                evolved = heat(p, t)
                assert gaussian_average(evolved, a, 2*t) == value(p, a)
                counts["gaussian_transfer"] += 1
                coefficients = []
                for n in range(degree+2):
                    hn = hermite_at(n, a, sigma)
                    hn_average = gaussian_average(mul(evolved, hn), a, 2*t)
                    assert hn_average == sigma**n * value(deriv(p, n), a)
                    assert gaussian_average(mul(hn, hn), a, 2*t) == factorial(n)
                    coefficients.append(hn_average / factorial(n))
                    counts["hermite_coefficients"] += 1
                energy = gaussian_average(mul(evolved, evolved), a, 2*t)
                assert energy == sum(v*v*factorial(n) for n, v in enumerate(coefficients))
                for cutoff in (0, 1, 2, degree):
                    projected = [Q(0)]
                    for n in range(min(cutoff, degree)+1):
                        projected = add(projected, scale(hermite_at(n, a, sigma), coefficients[n]))
                    residual = add(evolved, scale(projected, -1))
                    expected = sum((2*t)**n * value(deriv(p, n), a)**2 / factorial(n)
                                   for n in range(cutoff+1, degree+1))
                    assert gaussian_average(mul(residual, residual), a, 2*t) == expected
                    # Reconstruct the polynomial at several exact points.
                    for z in (Q(-1, 3), Q(0), Q(7, 5)):
                        assert gaussian_average(projected, z, 2*t) == sum(
                            value(deriv(p, n), a)*(z-a)**n/factorial(n)
                            for n in range(min(cutoff, degree)+1))
                    counts["parseval_and_projected_energy"] += 1
    for roots in ((Q(-1, 2), Q(1, 2)), (Q(0), Q(0)),
                  (Q(1), Q(1)), (Q(1, 2), Q(3, 4))):
        cluster = mul([-roots[0], 1], [-roots[1], 1])
        for unit in ([1], [1, Q(1, 10)], [1, 0, Q(1, 10)]):
            f = mul(unit, cluster)
            for degree in range(4, 10):
                v = [Q((-1)**k*(k+2), 100*(degree+k+1)) for k in range(degree+1)]
                reduced = remainder(v, mul(cluster, cluster))
                assert response(f, roots, v) == response(f, roots, reduced)
                counts["quotient_response"] += 1
                if roots[0] == roots[1]:
                    b = roots[0]
                    vjet = shift(v, b)[:3]
                    pjet = shift(vjet, -b)
                    assert response(f, roots, v) == response(f, roots, pjet)
                    # h=E/U via independent truncated series division.
                    uj = shift(unit, b)
                    h = []
                    for k in range(3):
                        h.append((vjet[k] - sum(uj[j]*h[k-j]
                            for j in range(1, min(k+1, len(uj))))) / uj[0])
                    assert response(f, roots, v) == (-4*h[0], h[1]**2+4*h[0]*h[2])
                    counts["double_three_jet_response"] += 1
    for b in (Q(-1, 16), Q(1, 16)):
        for c in (Q(-1, 32), Q(1, 32)):
            event = c/2 - b*b/8
            position = -b/2
            f = [c-2*event, b, Q(1)]
            assert value(f, position) == value(deriv(f), position) == 0
            assert response([0, 0, 1], (Q(0), Q(0)), [c, b]) == (-4*c, b*b)
            counts["affine_collision"] += 1
    return {
        "status": "all exact rational controls passed",
        "date": "2026-10-21", "author": "Prepared for Edward Baker",
        "llm_assistance": "Substantial; gpt-6-astra (Codex), effort ultra",
        "checks": counts, "arithmetic": "Python standard-library fractions.Fraction",
        "scope": "Finite polynomial and rational-unit controls; not theta acquisition, a source certificate, or endpoint exclusion.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    record = run()
    output = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(output)
    print(output, end='')
