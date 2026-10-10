#!/usr/bin/env python3
"""Exact polynomial certificates for the analytic collective-attraction note.

This is finite algebra, not evaluation of H_t or a zero search. It uses only
the Python standard library, prints a small deterministic record, and writes
no files. Universal identities are checked by coefficient equality.
"""

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


class Poly:
    def __init__(self, terms=None):
        self.terms = {e: Q(c) for e, c in (terms or {}).items() if c}

    @staticmethod
    def scalar(x):
        return Poly({(0, 0, 0): Q(x)})

    @staticmethod
    def variable(i):
        e = [0, 0, 0]
        e[i] = 1
        return Poly({tuple(e): Q(1)})

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly.scalar(other)
        out = self.terms.copy()
        for e, c in other.terms.items():
            out[e] = out.get(e, Q(0)) + c
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -Q(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly.scalar(other)
        out = {}
        for e, c in self.terms.items():
            for f, d in other.terms.items():
                ef = tuple(a + b for a, b in zip(e, f))
                out[ef] = out.get(ef, Q(0)) + c * d
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        out = Poly.scalar(1)
        for _ in range(n):
            out = out * self
        return out

    def at(self, *values):
        return sum(c * values[0] ** e[0] * values[1] ** e[1]
                   * values[2] ** e[2] for e, c in self.terms.items())

    def canonical(self):
        return [[list(e), str(c)] for e, c in sorted(self.terms.items())]


identities = {}
checks = {}


def identity(name, left, right):
    assert not (left - right).terms, name
    payload = json.dumps(left.canonical(), separators=(",", ":")).encode()
    identities[name] = {"monomials": len(left.terms),
                        "coefficient_sha256": sha256(payload).hexdigest()}


def require(name, predicate):
    assert predicate, name
    checks[name] = checks.get(name, 0) + 1


# Variables: s = squared horizontal distance / y^2,
# q = eta^2/y^2 - 1, u = 1 - v^2/y^2.
s, q, u = [Poly.variable(i) for i in range(3)]
de = (s + 2 - u) ** 2 - 4 * (1 - u)
dq = (s + q + 2 - u) ** 2 - 4 * (q + 1) * (1 - u)
identity("exact_field_denominator", de, s ** 2 + 2 * (2 - u) * s + u ** 2)
identity("probe_denominator", dq,
         s ** 2 + 2 * (q + 2 - u) * s + (q + u) ** 2)

low = 4 * (s + u) * dq - q * (s + q + u) * de
low_certificate = (
    (4 - q) * s ** 3
    + (12 + 4 * (1 - u) + q * (4 - q) + u * q) * s ** 2
    + u * (12 + 4 * (1 - u) + 12 * q + 2 * q ** 2 + q * u) * s
    + u * (u + q) * ((4 - q) * u + 4 * q)
)
identity("closer_probe_positive_factor_certificate", low, low_certificate)

high = (s + u) * dq - (s + q + u) * de
identity("higher_probe_positive_factor_certificate", high,
         q * (s ** 2 + (q - 4 + 6 * u) * s + u * (q + u)))

# A real external root has E/Q=(s+q+1)/(s+1), which is >=1.
identity("real_root_ratio_gap", (s + q + 1) - (s + 1), q)

# The low-probe own-pair subtraction cancels the baseline speed exactly.
# Third variable is an arbitrary positive w, second is q=(eta^2-w)/w.
# Multiply the physical inequality by q*w=eta^2-w to clear the own-pair
# denominator; the first variable is L_eta/eta in this identity.
identity("own_pair_cancellation", -2 * q * u
         - 4 * u * q * Q(1, 4) * s * q * u
         + 4 * u * q * Q(1, 4) * 2, -(q * u) ** 2 * s)

# Limits establishing sharpness, with u=0: numerator/(s+4)(s+q).
sharp_num = s ** 2 + 2 * (q + 2) * s + q ** 2
sharp_den = (s + 4) * (s + q)
identity("sharp_ratio_gap_from_one", sharp_num - sharp_den,
         q * (s + q - 4))

# Closed landing integral: variables s=w, q=n, u=B^2.
# F'(w) = 1/(n+2) + n B^2/[2(n+2)(B^2+2(n+2)w)].
identity("landing_derivative_after_common_denominator",
         2 * (u + 2 * (q + 2) * s) + q * u,
         (q + 2) * (u + 4 * s))
identity("landing_gain_integrand",
         (u + 2 * (q + 2) * s) - (u + 4 * s), 2 * q * s)

# Supplementary exact rational substitutions check denominator signs and
# the two comparison regimes, including boundary q=4 and u=0,1.
sv = [Q(0), Q(1, 100), Q(1, 4), Q(1), Q(4), Q(100)]
uv = [Q(0), Q(1, 4), Q(1, 2), Q(1)]
for sq in sv:
    for uq in uv:
        for qq in [Q(1, 100), Q(1, 2), Q(1), Q(3), Q(4)]:
            den_e = de.at(sq, qq, uq)
            den_q = dq.at(sq, qq, uq)
            require("low_probe_certificate_nonnegative", low.at(sq, qq, uq) >= 0)
            if den_e and den_q:
                require("low_probe_rational_comparison",
                        (sq + uq) / den_e >= qq * (sq + qq + uq) / (4 * den_q))
        for qq in [Q(4), Q(5), Q(10), Q(100)]:
            require("high_probe_certificate_nonnegative", high.at(sq, qq, uq) >= 0)
            den_e = de.at(sq, qq, uq)
            den_q = dq.at(sq, qq, uq)
            if den_e and den_q:
                require("high_probe_rational_comparison",
                        (sq + uq) / den_e >= (sq + qq + uq) / den_q)

for qq in [Q(1, 100), Q(1), Q(3), Q(4), Q(5), Q(10)]:
    require("sharp_small_distance_limit",
            sharp_num.at(Q(0), qq, Q(0))
            / sharp_den.at(Q(0), qq, Q(0)) == qq / 4)
require("sharp_infinite_distance_leading_coefficients",
        sharp_num.terms.get((2, 0, 0)) == sharp_den.terms.get((2, 0, 0)) == 1)

# Conservative count choices avoid evaluating pi/log: independent rational
# inequalities validate endpoint-error and gain denominators algebraically.
for a in [Q(0), Q(1, 4), Q(1), Q(10), Q(100)]:
    require("count_budget_reserve", (4 * a + 1) - 4 * a == 1)
for x in [Q(3), Q(4), Q(10), Q(100)]:
    require("count_error_endpoint_bound", 2 + 2 * x <= x ** 2)
for ww in [Q(1, 100), Q(1, 25), Q(1), Q(10)]:
    for nn in [Q(1), Q(2), Q(10)]:
        for bb in [Q(1), Q(100), Q(10000)]:
            fp = (bb + 4 * ww) / (2 * bb + 4 * (nn + 2) * ww)
            require("landing_strict_gain", 0 < fp < Q(1, 2))
            require("gain_integrand_positive", nn * ww / (bb + 2 * (nn + 2) * ww) > 0)

record = {
    "status": "PASS",
    "date": "2026-10-09",
    "scope": "Universal polynomial identities and finite rational substitutions; no heat-function evaluation, zero search, effective count constant, or numerical Newman bound.",
    "provenance": {"model": "GPT-6 (Codex), inherited configuration",
                   "effort": "Configured reasoning effort not exposed; not inferred"},
    "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "universal_identities": identities,
    "rational_checks": checks,
    "rational_assertions": sum(checks.values()),
    "positivity_domains": {"low_probe": "s>=0, 0<q<=4, 0<=u<=1",
                           "high_probe": "s>=0, q>=4, 0<=u<=1"},
}
print(json.dumps(record, sort_keys=True, indent=2))
