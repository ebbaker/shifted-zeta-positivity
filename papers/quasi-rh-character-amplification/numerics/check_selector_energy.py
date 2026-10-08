#!/usr/bin/env python3
"""Exact checks for selector energy and the conditional application wedge.

Prepared with GPT-6 (Codex) assistance, 2026-10-08. No arithmetic
cancellation or zero-free theorem is certified by this script.
"""
from fractions import Fraction as F
from itertools import product
import json

eta, alpha = F(1, 5000), F(5, 6)
ds, xs = (F(9, 25), F(21, 50)), (F(49, 100), F(1, 2))
rows = []
for delta, x in product(ds, xs):
    a = alpha-delta
    D, B = 3-F(17, 9)*x, 2-F(8, 9)*x
    P, J = B*(1-x), a*D+delta*B*(1-x)
    R = 1-delta+a*delta*P/(2*J)
    t0 = 1+delta*P/(2*J)
    factor = a*B/J
    tnew = t0-B*eta/J
    rnew = (B*tnew-F(5, 9)*x)/D-eta/(delta*D)
    mnew = tnew-rnew
    Rnew = R-factor*eta
    width = eta/(delta*(1-x))
    assert rnew == 1-factor/2-(1-factor)*width
    assert mnew == F(1, 2)-a/J*((1-x)/2-eta/delta)
    assert 1-delta*(x+(1-x)*rnew) == Rnew+eta
    assert 1-delta*(F(4, 9)*x+B*mnew) == Rnew
    assert 1-delta*(x+(1-x)*(rnew+width)) == Rnew
    rows.append((delta, x, rnew, mnew, width, (1-R)/delta))

# These extrema are continuous conclusions only in conjunction with the
# derivative signs proved in the note. Certify their stated coarse sign
# bounds here using exact fractions.
positive_delta_term = alpha*F(7, 9)*ds[0]**2/F(4)
negative_delta_term = eta*(alpha*ds[1]+(alpha-ds[0])*F(3, 2))
assert positive_delta_term == F(21, 1000)
assert negative_delta_term == F(53, 250000)
assert positive_delta_term > negative_delta_term
assert 5*(alpha-ds[1])-4*ds[1]*(1-xs[0])**2 > 0
assert (alpha-ds[0])*F(25, 12)+ds[1] < F(3, 2)

assert (min(r[2] for r in rows), max(r[2] for r in rows)) == (
    F(47749, 67660), F(10261670, 14086891))
assert (min(r[3] for r in rows), max(r[3] for r in rows)) == (
    F(3470383, 8566666), F(28646, 69475))
assert (min(r[4] for r in rows), max(r[4] for r in rows)) == (
    F(1, 1071), F(1, 900))
hmin = min(r[5] for r in rows)
assert hmin == F(3646037, 4283333)
strip_saving = ds[0]*(hmin-(1+F(701, 1000))/2)
assert strip_saving == F(55121103, 214166650000)
assert strip_saving-eta == F(12287773, 214166650000) > 0

def rec(v):
    return {"exact": str(v), "decimal": float(v)}

result = {
    "scope": "exponent identities; continuous bounds use the note's derivative proofs",
    "status": "mixed saving in the wedge remains unproved",
    "r_new": {"min": rec(min(r[2] for r in rows)), "max": rec(max(r[2] for r in rows))},
    "m_new": {"min": rec(min(r[3] for r in rows)), "max": rec(max(r[3] for r in rows))},
    "wedge_width": {"min": rec(min(r[4] for r in rows)), "max": rec(max(r[4] for r in rows))},
    "count_strip_saving": rec(strip_saving),
    "count_strip_margin_below_target": rec(strip_saving-eta),
    "outer_wedge_m_lower": rec(min(r[3] for r in rows)-F(1, 900)),
    "outer_wedge_r_upper": rec(max(r[2] for r in rows)+F(1, 900)),
    "m_delta_sign_lower_gap": rec(positive_delta_term-negative_delta_term),
}
print(json.dumps(result, indent=2, sort_keys=True))
