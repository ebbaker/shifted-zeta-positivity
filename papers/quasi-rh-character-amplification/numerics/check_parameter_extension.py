"""Exact exponent checks; not verification of the external analytic lemmas.

Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Serving variant and configured reasoning effort were not exposed.
Uses only Python's standard library. Output is a small JSON record.
"""
from fractions import Fraction as F
import json


# Sparse polynomials in (delta, y), with exact rational coefficients.
def const(c):
    return {(0, 0): F(c)} if c else {}


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def mul(*ps):
    out = const(1)
    for p in ps:
        new = {}
        for (i, j), v in out.items():
            for (k, l), w in p.items():
                key = (i + k, j + l)
                new[key] = new.get(key, F(0)) + v * w
        out = {k: v for k, v in new.items() if v}
    return out


def scale(c, p):
    return mul(const(c), p)


def power(p, n):
    return mul(*([p] * n))


d, y = {(1, 0): F(1)}, {(0, 1): F(1)}
v = add(const(51), scale(41, y))
py = add(const(7), scale(18, y), scale(8, power(y, 2)))
jy = add(const(185), scale(170, y),
         mul(add(const(-138), scale(12, y), scale(96, power(y, 2))), d))
# Source equation (20.9), before division by its positive denominator.
lhs = mul(v, add(scale(2, mul(jy, add(const(1), mul(add(const(3), scale(8, y)), d)))),
                 scale(-468, mul(add(const(F(5, 6)), scale(-1, d)), d, py))))
rhs = add(mul(add(const(3), scale(5, y)),
              add(power(add(scale(4, mul(v, d)), const(-79)), 2), const(49))),
          scale(4, mul(y, add(scale(4, mul(v, d,
              add(mul(add(const(1), scale(3, y)), add(const(15), scale(32, y)), d),
                  const(9), scale(-13, y)))), const(265), scale(3485, y)))))
assert lhs == rhs
# P/D <= 2/3 follows from this nonnegative factorization on 0<=y<=1/2.
pd_gap = add(const(16), scale(-20, y), scale(-24, power(y, 2)))
assert pd_gap == mul(add(const(F(1, 2)), scale(-1, y)), add(scale(24, y), const(32)))

r = F(1, 100000)
b, ell, h0 = F(1, 8), F(1, 6), F(13, 16)
lx, ly, h = F(17, 48) - r, F(23, 48) - r, h0 + r
M = lx + ly
sigma0 = F(7, 8) - r / 6
c = lx / 2 - 1 + h / 6
low = lx / 2 + b / 12
assert h == 1 - lx + ell
assert ly - lx == b
assert M + ell == 1 - 2 * r
assert sigma0 + c == low
assert c == -F(11, 16) - r / 3
assert low == F(3, 16) - r / 2
assert 0 < r < F(1, 24)
# The low summand is piecewise affine. Checking its endpoints and kink
# proves f(d)<=0 on the complete interval [0,ell].
kink = ell - 4 * r
f = lambda t: -t + max(F(0), t - ell + 4 * r) / 8
assert max(f(t) for t in [F(0), kink, ell]) == 0
assert lx - ell > 0 and M - 2 * ell > 0
assert ly - ell - F(11, 6) * b > 0

m0 = F(49, 440640)
adaptive = m0 - F(7, 4) * r
floor = F(7, 1200) - F(38, 25) * r
middle = F(49, 14400) - (F(7, 8) + F(17, 50)) * r
small = F(63, 800) - F(101, 150) * r
assert min(adaptive, floor, middle, small) > 0
# Reserve a fixed frequency extension and leave room for arbitrarily
# small analytic losses. This is a feasibility check, not explicit bounds
# on the constants in those analytic losses.
zeta = adaptive / 16
assert ell / (h + zeta) > F(1, 5) > F(7, 37)
assert 2 * zeta < adaptive / 4

x0, w0, z0 = F(87, 100), F(19, 20), F(33, 200)
good = max(1 - x0 - w0 - 6 * z0, -x0 - w0,
           -x0 - 6 * z0, -w0 - 6 * z0, 4 - 6 * x0 - 6 * z0)
assert good == -F(181, 100)
assert good < -1 - F(4, 5)
ramified = max(1 - x0 - w0, F(3, 2) - 3 * x0,
              2 - 3 * x0 - w0, 2 - 4 * x0,
              F(5, 2) - 4 * x0 - w0, 3 - 6 * x0,
              4 - 6 * x0 - 6 * z0)
assert ramified == -F(41, 50)
principal_error = max(-x0, -6 * z0, 4 - 5 * x0 - 6 * z0, 1 - w0 - 6 * z0)
assert principal_error == -F(87, 100)
assert sigma0 > x0
assert x0 + F(1, 2) - 1 > F(1, 3)
small_ramified = max(F(1, 2), -F(1, 2), F(3, 2) - 2*x0,
                    2 - 3*x0, 3 - 5*x0, 4 - 5*x0 - 6*F(17, 50))
assert small_ramified == F(1, 2)

def entry(q):
    return {"exact": str(q), "decimal": float(q)}


result = {
    "scope": "Exact algebra and exponent feasibility only; external analytic lemmas are assumed.",
    "source_identity_20_9": "verified by exact polynomial expansion",
    "ratio_bound_P_over_D": "verified nonnegative factorization",
    "r": entry(r), "sigma0": entry(sigma0),
    "variance_delta": entry(2*sigma0-1),
    "variance_exponent": entry(1+2*sigma0),
    "low_exponent": entry(low), "signal_constant": entry(c),
    "margins": {k: entry(q) for k,q in {
        "adaptive": adaptive, "floor": floor, "middle": middle, "small": small,
        "principal_w": ly/20, "principal_z": h/600,
        "frequency_extension": zeta,
        "slot_supply_above_one_fifth": ell/(h+zeta)-F(1,5),
    }.items()},
    "extended_euler_region": {
        "minimum_real_s": entry(x0), "good_prime_defect": entry(good),
        "ramified_defect": entry(ramified), "principal_error": entry(principal_error),
    },
    "conditional_short_family_examples": {
        "crude_prime_error_h_6_over_7": entry(max(F(1,2)+F(5,12)*F(6,7),1-F(6,7)/6)),
        "mobius_baseline_7_over_8_h_2_over_3": entry(max(F(1,2)+F(5,12)*F(2,3),F(7,8)*(1-F(2,3)/6))),
    },
}
print(json.dumps(result, indent=2, sort_keys=True))
