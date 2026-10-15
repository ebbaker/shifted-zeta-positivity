#!/usr/bin/env python3
"""Exact finite audit of reflected octonion lift and physical bilinear identities.

Prepared for Edward Baker, 2026-10-15 (America/New_York).
Substantial LLM assistance: recorded model gpt-6-astra, effort ultra,
as verified and supplied by the parent turn metadata.
Python standard library only. Sparse integer polynomials, no sampling.
This verifies finitely many heat-polynomial inputs and polynomial identities;
the general lift proof is the chain rule, not these finite checks.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

NV = 9  # t, x0, x1, x2, x3, y0, y1, y2, y3
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


def qadd(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))


def qneg(a):
    return tuple(scale(x, -1) for x in a)


def qbar(a):
    return (a[0],) + tuple(scale(x, -1) for x in a[1:])


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (
        add(mul(a0, b0), scale(add(mul(a1, b1), mul(a2, b2), mul(a3, b3)), -1)),
        add(mul(a0, b1), mul(a1, b0), mul(a2, b3), scale(mul(a3, b2), -1)),
        add(mul(a0, b2), scale(mul(a1, b3), -1), mul(a2, b0), mul(a3, b1)),
        add(mul(a0, b3), mul(a1, b2), scale(mul(a2, b1), -1), mul(a3, b0)),
    )


def omul(a, b):
    aa, ab, ba, bb = a[:4], a[4:], b[:4], b[4:]
    return qadd(qmul(aa, ba), qneg(qmul(bb, qbar(ab)))) + qadd(qmul(qbar(aa), bb), qmul(ba, ab))


def vsub(a, b):
    return tuple(sub(x, y) for x, y in zip(a, b))


def assoc(a, b, c):
    return vsub(omul(omul(a, b), c), omul(a, omul(b, c)))


def basis(i):
    return tuple(const(int(i == j)) for j in range(8))


def lift(n, m):
    return G(n, m) + tuple(reflect(p) for p in G(n, m + 2))


def d8(a):
    out = tuple({} for _ in range(8))
    for i in range(8):
        term = omul(basis(i), tuple(diff(p, i + 1) for p in a))
        out = tuple(add(x, y) for x, y in zip(out, term))
    return out


checks = []


def check(label, lhs, rhs):
    if lhs != rhs:
        raise AssertionError(label)
    checks.append(label)


for n in range(13):
    for m in range(4):
        o = lift(n, m)
        check(f"degree {n} jet {m}: full D8", d8(o), tuple({} for _ in range(8)))
        check(f"degree {n} jet {m}: x0 derivative", tuple(diff(p, 1) for p in o), lift(n, m + 1))
        check(f"degree {n} jet {m}: external heat", tuple(diff(p, 0) for p in o), tuple(scale(p, -1) for p in lift(n, m + 2)))
        check(f"degree {n} jet {m}: physical trace", tuple(physical(p) for p in o), tuple(physical(p) for p in G(n, m) + G(n, m + 2)))
        original = G(n, m) + G(n, m + 2)
        check(f"degree {n} jet {m}: same-q defect", d8(original), tuple({} for _ in range(4)) + tuple(scale(p, 2) for p in G(n, m + 3)))
        hh = [physical(heat_jet(n, j)[0]) for j in range(m, m + 4)]
        lj = sub(mul(hh[1], hh[1]), mul(hh[0], hh[2]))
        lj1 = sub(mul(hh[2], hh[2]), mul(hh[1], hh[3]))
        check(f"degree {n} level {m}: Laguerre heat hierarchy", add(diff(lj, 0), diff(diff(lj, 1), 1)), scale(lj1, 2))

# Independent indeterminates a,b,c,d for two physical vectors (a,b),(c,d).
a, b, c, d = (var(i) for i in range(4))
av = (a, {}, b, {}, {}, {}, {}, {})
bv = (c, {}, d, {}, {}, {}, {}, {})
dot = add(mul(a, c), mul(b, d))
det = sub(mul(a, d), mul(b, c))
norma = add(mul(a, a), mul(b, b))
normb = add(mul(c, c), mul(d, d))
expected_dot = tuple(scale(dot, 2) if i == 6 else {} for i in range(8))
expected_det = tuple(scale(det, -2) if i == 6 else {} for i in range(8))
check("dot associator", assoc(omul(av, basis(1)), omul(bv, basis(3)), basis(4)), expected_dot)
check("wedge associator", assoc(omul(av, basis(1)), omul(bv, basis(1)), basis(4)), expected_det)
check("Lagrange radial-transverse identity", mul(norma, normb), add(mul(dot, dot), mul(det, det)))

# Four jet variables plus retained second pair (c2,c3).
h0, h1, h2, h3, c2, c3 = (var(i) for i in range(6))
full = scale(add(mul(h0, h2), mul(h1, h3)), -1)
retained = scale(add(mul(h0, c2), mul(h1, c3)), -1)
tail2, tail3 = sub(h2, c2), sub(h3, c3)
check("full-amplitude cutoff payment identity", sub(full, retained), scale(add(mul(h0, tail2), mul(h1, tail3)), -1))
F = (h0, {}, h1, {}, {}, {}, {}, {})
FN_t = (scale(c2, -1), {}, scale(c3, -1), {}, {}, {}, {}, {})
check("polarized retained heat associator", assoc(omul(F, basis(1)), omul(FN_t, basis(3)), basis(4)), tuple(scale(retained, 2) if i == 6 else {} for i in range(8)))
L0 = sub(mul(h1, h1), mul(h0, h2))
L1 = sub(mul(h2, h2), mul(h1, h3))
check("first stationary observation", set_zero(full, 1), set_zero(L0, 1))
check("second stationary observation", set_zero(full, 2), set_zero(L1, 2))
check("first stationary optimal cutoff", set_zero(retained, 1), scale(mul(h0, c2), -1))
check("second stationary cutoff extra tail", set_zero(sub(retained, scale(mul(h1, c3), -1)), 2), set_zero(mul(h0, tail2), 2))
dotx = add(mul(h0, h1), mul(h1, h2))
E = add(mul(h0, h0), mul(h1, h1))
normx = add(mul(h1, h1), mul(h2, h2))
D = sub(mul(h0, h3), mul(h1, h2))
check("first jet Gram identity", mul(E, normx), add(mul(dotx, dotx), mul(L0, L0)))
check("jet Pluecker identity real", mul(L0, scale(h2, -1)), add(mul(L1, h0), mul(D, h1)))
check("jet Pluecker identity imaginary", mul(L0, scale(h3, -1)), add(mul(L1, h1), mul(D, h2)))
check("Laguerre inertia decomposition", scale(L0, 4), add(scale(mul(h1, h1), 4), mul(sub(h0, h2), sub(h0, h2)), scale(mul(add(h0, h2), add(h0, h2)), -1)))

parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
record = {
    "date": "2026-10-15",
    "prepared_for": "Edward Baker",
    "model": "gpt-6-astra",
    "reasoning_effort": "ultra",
    "model_effort_provenance": "Verified and supplied by parent turn metadata",
    "arithmetic": "Exact sparse integer polynomials in nine real variables; no sampling",
    "heat_inputs": "H(s,z)=exp(-s*d_z^2) z^n for every 0<=n<=12; lift levels 0<=m<=3",
    "checks_passed": len(checks),
    "labels": checks,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "limitations": ["Finite algebra verification, not a proof of the general entire-source statement", "No theta inequality or new finite-height certificate", "Reflected lift is constant in the four r coordinates and changes the off-physical-slice quaternionic trace"],
}
args.output.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"checks_passed": len(checks), "output": str(args.output)}))
