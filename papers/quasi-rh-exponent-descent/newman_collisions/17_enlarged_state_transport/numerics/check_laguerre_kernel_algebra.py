#!/usr/bin/env python3
"""Exact finite algebra checks; not analytic or theta-sign verification."""
from fractions import Fraction
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import platform

COUNT = 0


def const(c):
    return {(0, 0): Fraction(c)} if c else {}


def mono(a, b, c=1):
    return {(a, b): Fraction(c)} if c else {}


def add(*terms):
    out = {}
    for term in terms:
        for key, val in term.items():
            out[key] = out.get(key, Fraction(0)) + val
    return {key: val for key, val in out.items() if val}


def mul(a, b):
    out = {}
    for (ai, aj), av in a.items():
        for (bi, bj), bv in b.items():
            key = (ai + bi, aj + bj)
            out[key] = out.get(key, Fraction(0)) + av * bv
    return {key: val for key, val in out.items() if val}


def scale(c, p):
    return {key: Fraction(c) * val for key, val in p.items() if c * val}


def power(p, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, p)
    return out


def derivative(p, var, n=1):
    for _ in range(n):
        out = {}
        for key, val in p.items():
            k = key[var]
            if k:
                newkey = list(key)
                newkey[var] -= 1
                out[tuple(newkey)] = val * k
        p = out
    return p


def check(a, b, label):
    global COUNT
    assert a == b, (label, a, b)
    COUNT += 1


def heat_poly(m):
    return {
        (k, m - 2 * k): Fraction((-1) ** k * factorial(m),
                                factorial(k) * factorial(m - 2 * k))
        for k in range(m // 2 + 1)
    }


def laguerre(h, j):
    h0 = derivative(h, 1, j)
    h1 = derivative(h, 1, j + 1)
    h2 = derivative(h, 1, j + 2)
    return add(power(h1, 2), scale(-1, mul(h0, h2)))


# Every heat polynomial is an exact solution. Verify the hierarchy on
# individual degrees and mixed heat-polynomial solutions, so nonlinear
# cross contributions are also exercised.
families = [heat_poly(m) for m in range(1, 13)]
families += [add(heat_poly(3), scale(7, heat_poly(6)),
                 scale(-3, heat_poly(9))),
             add(scale(11, heat_poly(2)), heat_poly(5), heat_poly(10))]
for i, h in enumerate(families):
    check(add(derivative(h, 0), derivative(h, 1, 2)), {},
          f"heat family {i}")
    for j in range(7):
        lhs = add(derivative(laguerre(h, j), 0),
                  derivative(laguerre(h, j), 1, 2))
        check(lhs, scale(2, laguerre(h, j + 1)),
              f"Laguerre hierarchy family {i}, j={j}")

cubic = heat_poly(3)
check(laguerre(cubic, 0), add(mono(0, 4, 3), mono(2, 0, 36)),
      "cubic global first Laguerre expression")
check(laguerre(cubic, 1), add(mono(0, 2, 18), mono(1, 0, 36)),
      "cubic second Laguerre expression")

# Difference-frequency autocorrelation algebra, variables u,v.
u, v = mono(1, 0), mono(0, 1)
uv = mul(u, v)
for j in range(11):
    sym = add(power(uv, j + 1),
              scale(Fraction(1, 2), mul(power(u, j), power(v, j + 2))),
              scale(Fraction(1, 2), mul(power(u, j + 2), power(v, j))))
    target = scale(Fraction(1, 2),
                   mul(power(uv, j), power(add(u, v), 2)))
    check(sym, target, f"autocorrelation integrand j={j}")
    multiplier = add(power(u, 2), power(v, 2),
                     scale(-1, power(add(u, scale(-1, v)), 2)))
    check(mul(multiplier, target),
          scale(2, mul(uv, target)), f"kernel heat hierarchy j={j}")

# Map the difference-frequency kernel to the retained theta kernel J_j:
# u=s+r, v=r-s, p=u-v=2s, du=dr. Thus K_j(2s)=4 J_j(s),
# and (1/8)*integral e^(ixp)K_j(p)dp=integral e^(2ixs)J_j(s)ds.
s, r = mono(1, 0), mono(0, 1)
u, v = add(s, r), add(r, scale(-1, s))
uv = mul(u, v)
for j in range(11):
    mapped = mul(power(uv, j), power(add(u, v), 2))
    j_integrand = mul(power(r, 2), power(add(power(r, 2),
                                              scale(-1, power(s, 2))), j))
    check(mapped, scale(4, j_integrand), f"K_j(2s)=4J_j(s), j={j}")
    multiplier = add(power(u, 2), power(v, 2), scale(-4, power(s, 2)))
    check(mul(multiplier, j_integrand), scale(2, mul(uv, j_integrand)),
          f"J_j heat hierarchy j={j}")

# Score-Q convention: A=2H, so L_j(A)=4L_j(H) and the raw score
# quadratics Q_j=beta^2 L_j(A)=4beta^2 L_j(H). This checks the
# amplitude factor directly; the analytic score dictionary is separate.
for j in range(7):
    check(laguerre(scale(2, cubic), j), scale(4, laguerre(cubic, j)),
          f"A=2H Laguerre normalization, j={j}")

# Note 4's positive even triple source. For g=e^-z^2, the action of
# (-D_z^2-a) on p*g is -p''+4z*p'-(4z^2-2+a)*p.
z = mono(0, 1)


def gaussian_op(p, a):
    return add(scale(-1, derivative(p, 1, 2)),
               scale(4, mul(z, derivative(p, 1))),
               scale(-1, mul(add(scale(4, power(z, 2)),
                                  const(a - 2)), p)))


r3 = gaussian_op(const(1), 40)
for _ in range(3):
    r3 = gaussian_op(r3, 30)
expected = add(mono(0, 8, 256), mono(0, 6, 4736),
               mono(0, 4, 51840), mono(0, 2, 317760),
               const(871680))
check(r3, expected, "positive even triple source coefficients")
assert all(val > 0 for val in r3.values())
COUNT += 1

record = {
    "date": "2026-10-10",
    "prepared_for": "Edward Baker",
    "model": "GPT-6 (Codex)",
    "reasoning_effort": "Not exposed in this session; not inferred",
    "acknowledgment": "Substantial LLM assistance; internal exact algebra replay, not independent mathematical validation.",
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python_version": platform.python_version(),
    "exact_assertions": COUNT,
    "arithmetic": "Python standard library Fraction",
    "passed": True,
    "scope": ["finite heat/Laguerre hierarchy algebra including mixed terms",
              "cubic global L0 and L1 countercontrol",
              "autocorrelation integrands and kernel hierarchy",
              "u=s+r, v=r-s kernel mapping K_j(2s)=4J_j(s)",
              "A=2H amplitude and score-Q normalization convention",
              "positive even triple Gaussian-source coefficients"],
    "not_verified": ["analytic weighted remainder theorem",
                     "genuine theta stationary signs",
                     "parameter coverage or approximation error bounds",
                     "RH or all-time control for Gaussian source"],
}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--record", type=Path,
                    help="Write a record only when this explicit path is supplied.")
args = parser.parse_args()
if args.record:
    args.record.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"exact_assertions": COUNT, "passed": True,
                  "source_sha256": record["source_sha256"],
                  "record": str(args.record) if args.record else None}))
