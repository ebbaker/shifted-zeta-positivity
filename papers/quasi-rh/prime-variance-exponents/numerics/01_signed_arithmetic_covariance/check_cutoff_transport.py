#!/usr/bin/env python3
"""Exact finite coefficient checks for the Vaughan cutoff-transport note.

Every logarithm is represented by its integer prime-factor vector. No
floating point, probe quadrature, or asymptotic exponent fit is used.
Standard library only. Prints a small reproducible result; saves no arrays.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json


LIMIT = 256
CUTOFFS = (Fraction(1), Fraction(7, 2), Fraction(8), Fraction(61, 4), Fraction(32))


@lru_cache(None)
def factor(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def mobius(n):
    fs = factor(n)
    return 0 if any(e > 1 for e in fs.values()) else (-1) ** len(fs)


MU = [0] + [mobius(n) for n in range(1, LIMIT + 1)]
PP = [(n, next(iter(factor(n)))) for n in range(2, LIMIT + 1)
      if len(factor(n)) == 1]


def empty():
    return [{} for _ in range(LIMIT + 1)]


def add(dst, src, scale=1):
    for p, coefficient in src.items():
        updated = dst.get(p, 0) + scale * coefficient
        if updated:
            dst[p] = updated
        else:
            dst.pop(p, None)


def combine(*terms):
    result = empty()
    for scale, table in terms:
        for n in range(1, LIMIT + 1):
            add(result[n], table[n], scale)
    return result


@lru_cache(None)
def b_table(u, v):
    """Coefficient of w(n/x) in B_(u,v), using A_u(m)."""
    a = [0] * (LIMIT + 1)
    for d in range(1, LIMIT + 1):
        if d > u:
            for m in range(d, LIMIT + 1, d):
                a[m] += MU[d]
    result = empty()
    for m in range(1, LIMIT + 1):
        if a[m]:
            for r, p in PP:
                if m * r > LIMIT:
                    break
                if r > v:
                    add(result[m * r], {p: a[m]})
    return result


def log_convolution(lo, hi):
    """Sum_(lo<d<=hi) mu(d) log(k) w(dk/x)."""
    result = empty()
    for d in range(1, LIMIT + 1):
        if lo < d <= hi and MU[d]:
            for k in range(1, LIMIT // d + 1):
                add(result[d * k], factor(k), MU[d])
    return result


def lattice_rectangle(dlo, dhi, rlo, rhi):
    """Sum mu(d) Lambda(r) L(x/(dr)), retaining every cofactor."""
    result = empty()
    for d in range(1, LIMIT + 1):
        if dlo < d <= dhi and MU[d]:
            for r, p in PP:
                if d * r > LIMIT:
                    break
                if rlo < r <= rhi:
                    for n in range(d * r, LIMIT + 1, d * r):
                        add(result[n], {p: MU[d]})
    return result


def prime_annulus(lo, hi):
    result = empty()
    for r, p in PP:
        if lo < r <= hi:
            result[r] = {p: 1}
    return result


def m1(u):
    return sum((Fraction(MU[d], d) for d in range(1, LIMIT + 1)
                if d <= u), Fraction(0))


counts = {name: 0 for name in ("vaughan", "u_transport", "v_transport", "mixed_rectangle")}
scalar_checks = 0


def check(name, left, right, params):
    for n in range(1, LIMIT + 1):
        if left[n] != right[n]:
            raise AssertionError((name, params, n, left[n], right[n]))
        counts[name] += 1


full_lambda = prime_annulus(0, LIMIT)
for u in CUTOFFS:
    for v in CUTOFFS:
        check("vaughan", full_lambda,
              combine((1, log_convolution(0, u)),
                      (-1, lattice_rectangle(0, u, 0, v)),
                      (1, prime_annulus(0, v)), (1, b_table(u, v))),
              (str(u), str(v)))

for u1, u2 in combinations(CUTOFFS, 2):
    for v in CUTOFFS:
        check("u_transport", combine((1, b_table(u2, v)), (-1, b_table(u1, v))),
              combine((-1, log_convolution(u1, u2)),
                      (1, lattice_rectangle(u1, u2, 0, v))),
              (str(u1), str(u2), str(v)))
        # Formal c_w*x coefficient on the centered identity's two sides.
        assert m1(u2) - m1(u1) == sum(
            (Fraction(MU[d], d) for d in range(1, LIMIT + 1) if u1 < d <= u2),
            Fraction(0))
        scalar_checks += 1

for v1, v2 in combinations(CUTOFFS, 2):
    for u in CUTOFFS:
        check("v_transport", combine((1, b_table(u, v2)), (-1, b_table(u, v1))),
              combine((1, lattice_rectangle(0, u, v1, v2)),
                      (-1, prime_annulus(v1, v2))),
              (str(u), str(v1), str(v2)))

for u1, u2 in combinations(CUTOFFS, 2):
    for v1, v2 in combinations(CUTOFFS, 2):
        check("mixed_rectangle",
              combine((1, b_table(u2, v2)), (-1, b_table(u2, v1)),
                      (-1, b_table(u1, v2)), (1, b_table(u1, v1))),
              lattice_rectangle(u1, u2, v1, v2),
              tuple(map(str, (u1, u2, v1, v2))))

print(json.dumps({
    "status": "passed",
    "limit": LIMIT,
    "cutoffs": list(map(str, CUTOFFS)),
    "coefficient_vector_comparisons": counts,
    "total_coefficient_vector_comparisons": sum(counts.values()),
    "exact_rational_centering_checks": scalar_checks,
    "arithmetic": "integer prime-log vectors and rational continuum coefficients",
    "scope": "finite identity verification only; no global power bound",
}, indent=2))
