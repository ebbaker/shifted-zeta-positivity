#!/usr/bin/env python3
"""Exact check of the cleared-denominator ambient logarithmic-energy formula.

Prepared for Edward Baker, 2026-10-15. Substantial LLM assistance:
gpt-6-astra, effort ultra (verified and supplied by parent turn metadata).
Standalone Python standard-library implementation; no sampling or division by energy.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

NV = 5  # t, x0, x1, x2, x3
Z = (0,) * NV


def const(n):
    return {Z: n} if n else {}


def var(i):
    k = list(Z)
    k[i] = 1
    return {tuple(k): 1}


def add(*ps):
    out = {}
    for p in ps:
        for k, c in p.items():
            out[k] = out.get(k, 0) + c
    return {k: c for k, c in out.items() if c}


def scale(p, c):
    return {k: c * v for k, v in p.items() if c * v}


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = {}
    for k, c in a.items():
        for l, d in b.items():
            m = tuple(x + y for x, y in zip(k, l))
            out[m] = out.get(m, 0) + c * d
    return {k: c for k, c in out.items() if c}


def diff(p, i):
    out = {}
    for k, c in p.items():
        if k[i]:
            m = list(k)
            m[i] -= 1
            out[tuple(m)] = c * k[i]
    return out


def reflect(p):
    return {k: c * (-1) ** sum(k[i] for i in (2, 3, 4))
            for k, c in p.items()}


def physical(p):
    return {k: c for k, c in p.items() if not any(k[2:])}


def set_zero(p, index):
    return {k: c for k, c in p.items() if k[index] == 0}


def cadd(a, b):
    return add(a[0], b[0]), add(a[1], b[1])


def cmul(a, b):
    return sub(mul(a[0], b[0]), mul(a[1], b[1])), add(mul(a[0], b[1]), mul(a[1], b[0]))


def cpowers(a, n):
    out = [(const(1), {})]
    for _ in range(n):
        out.append(cmul(out[-1], a))
    return out


TP = cpowers((add(var(0), var(3)), var(4)), 12)
ZP = cpowers((var(1), var(2)), 12)


def heat_jet(n, m):
    ans = ({}, {})
    for k in range((n - m) // 2 + 1):
        c = (-1) ** k * math.factorial(n) // (math.factorial(k) * math.factorial(n - m - 2 * k))
        p = cmul(TP[k], ZP[n - m - 2 * k])
        ans = cadd(ans, (scale(p[0], c), scale(p[1], c)))
    return ans


def G(n, m):
    h, hp = heat_jet(n, m), heat_jet(n, m + 1)
    return (h[0], h[1], hp[0], scale(hp[1], -1))


hj = heat_jet
labels = []
for n in range(13):
    g = G(n, 0)
    pg = [physical(p) for p in g]
    energy = add(*(mul(p, p) for p in pg))
    first, second = [], []
    for k in range(1, 5):
        gd = [physical(diff(p, k)) for p in g]
        gdd = [physical(diff(diff(p, k), k)) for p in g]
        first.append(scale(add(*(mul(p, d) for p, d in zip(pg, gd))), 2))
        second.append(scale(add(*(add(mul(d, d), mul(p, dd))
                                 for p, d, dd in zip(pg, gd, gdd))), 2))
    lhs = sub(mul(energy, add(*second)), add(*(mul(p, p) for p in first)))
    h = [physical(hj(n, j)[0]) for j in range(4)]
    l0 = sub(mul(h[1], h[1]), mul(h[0], h[2]))
    determinant = sub(mul(h[0], h[3]), mul(h[1], h[2]))
    rhs = scale(add(mul(l0, l0), mul(determinant, determinant)), 4)
    assert lhs == rhs, n
    labels.append(f"degree {n}: Ehat*Delta_q(Ehat)-|grad_q(Ehat)|^2=4*(L0^2+D^2) on physical slice")

parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True, type=Path)
args = parser.parse_args()
record = {
    "date": "2026-10-15",
    "prepared_for": "Edward Baker",
    "model": "gpt-6-astra",
    "reasoning_effort": "ultra",
    "model_effort_provenance": "Verified and supplied by parent turn metadata",
    "checks_passed": len(labels),
    "arithmetic": "Exact sparse integer polynomials; no sampling or division by energy or jets",
    "labels": labels,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "limitations": "Finite heat-polynomial verification; the general proof uses holomorphy. Logarithmic formula applies only at E>0. No theta sign estimate.",
}
args.output.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"checks_passed": len(labels), "output": str(args.output)}))
