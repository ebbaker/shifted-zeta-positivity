#!/usr/bin/env python3
"""Finite algebra for the fixed-profile prime-pair barrier, 8 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact variant/effort not exposed.
Standard library only. Prints deterministic JSON and writes no files.
This checks finite divisor algebra, formal power-series coefficients, rational
partial fractions, polynomial integration by parts, and exponent bookkeeping.
It does not verify prime ideal counting, polynomial approximation, an infinite
asymptotic, an actual family moment, or RH. The polynomial bump is a finite
calculus diagnostic, not a C-infinity analytic test profile.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, prod
import json


counts = Counter()


def check(group, condition):
    if not condition:
        raise AssertionError(group)
    counts[group] += 1


norms = (5011, 61, 97, 109, 73)


def norm(n):
    return prod(p ** e for p, e in zip(norms, n))


def divisors(n):
    return product(*(range(e + 1) for e in n))


def mu(n):
    return 0 if any(e > 1 for e in n) else (-1) ** sum(n)


def coefficient(d, z):
    return sum(mu(a) * mu(b)
               for a in divisors(d)
               for b in [tuple(x - y for x, y in zip(d, a))]
               if norm(a) <= z and norm(b) <= z)


def tail(n, z, y):
    return -sum(coefficient(d, z) for d in divisors(n) if norm(d) > y)


cases = [((1, 0, 0, 0, 0), 0), ((0, 1, 1, 0, 0), -2),
         ((0, 1, 0, 1, 0), 0), ((0, 0, 0, 0, 2), -1)]
for n, expected in cases:
    check("product_coefficients", tail(n, 100, 200) == expected)

alpha = [F(0)] + [sum((F(1, 2 ** (k - j) * j) for j in range(1, k + 1)), F(0))
                     for k in range(1, 25)]
check("series_first_six", alpha[1:7] == [F(1), F(1), F(5, 6), F(2, 3), F(8, 15), F(13, 30)])
for k in range(1, 25):
    check("series_recurrence", alpha[k] == alpha[k - 1] / 2 + F(1, k))
    check("series_positivity", alpha[k] > 0)
    # Coefficient of v**k in (2B-v) F_B(v) = 2 log(B/(B-v)).
    check("series_kernel_identity", 2 * alpha[k] - alpha[k - 1] == F(2, k))

for b in range(5, 10):
    for v in (F(1, 3), F(2), F(7, 2)):
        for t in (F(1, 4), F(1, 2), F(3, 4)):
            s = b - v + t * v
            check("partial_fractions", F(1, s * (2 * b - v - s)) ==
                  (1 / s + 1 / (2 * b - v - s)) / (2 * b - v))


def poly_add(p, q):
    return [((p[i] if i < len(p) else F(0)) +
             (q[i] if i < len(q) else F(0))) for i in range(max(len(p), len(q)))]


def poly_scale(p, scale):
    return [scale * a for a in p]


def poly_mul(p, q):
    result = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result


# V(t)=(t-1)^6(2-t)^6 on [1,2], with zero extension. It has enough
# vanishing endpoint derivatives for the integration-by-parts checks J<=5.
vpoly = poly_mul([F(comb(6, i) * (-1) ** (6 - i)) for i in range(7)],
                 [F(comb(6, i) * 2 ** (6 - i) * (-1) ** i) for i in range(7)])


def log_integral(a, k):
    """Integral t**a log(2/t)**k dt on [1,2], as a polynomial in log(2)."""
    answer = [F(2 ** (a + 1) - 1, a + 1)]
    for j in range(1, k + 1):
        answer = poly_scale(answer, F(j, a + 1)) + [F(0)]
        answer[j] -= F(1, a + 1)
    return answer


def moment(profile, k):
    answer = [F(0)] * (k + 1)
    for a, coefficient_a in enumerate(profile):
        answer = poly_add(answer, poly_scale(log_integral(a, k), coefficient_a))
    return answer


check("polynomial_bump_mass", moment(vpoly, 0)[0] > 0)
for j in range(1, 6):
    wpoly = [a * (i + 1) ** j for i, a in enumerate(vpoly)]
    for k in range(9):
        actual = moment(wpoly, k)
        expected = ([F(0)] if k < j else
                    poly_scale(moment(vpoly, k - j), factorial(k) // factorial(k - j)))
        check("derivative_profile_log_moments", all(a == 0 for a in poly_add(actual, poly_scale(expected, -1))))
    check("derivative_profile_first_nonzero", moment(wpoly, j)[0] == factorial(j) * moment(vpoly, 0)[0] > 0)

h, a, theta = F(2, 5), F(2, 5), F(1, 40)


def extraction(h, a):
    return (1 + a) / 2 + 5 * h / 12


for height, loss, target in [(F(4, 5), F(0), F(5, 6)),
                              (F(1, 5), F(1, 10), F(19, 30))]:
    check("rational_exponents", extraction(height, loss) == target)

budgets = {
    "inner_Y": 1 - theta - h,
    "coherent_Y": 1 - theta - h / 6,
    "coherent_free_factor": theta + h / 6,
    "coherent_factor_lower": F(1, 2) - theta - h / 6,
    "conditional_extraction": extraction(h, a),
    "coherent_sector_power": 1 + h / 6,
    "power_gap": 1 + h / 6 - h - a,
}
expected = [F(23, 40), F(109, 120), F(11, 120), F(49, 120),
            F(13, 15), F(16, 15), F(4, 15)]
for actual, target in zip(budgets.values(), expected):
    check("rational_exponents", actual == target)

record = {
    "date": "2026-10-08",
    "author": "Prepared for Edward Baker with substantial LLM assistance",
    "model": "GPT-6 (Codex), inherited configuration; exact variant/effort not exposed",
    "status": "all exact finite assertions passed",
    "assertions": sum(counts.values()),
    "groups": dict(sorted(counts.items())),
    "alpha_first_six": [str(x) for x in alpha[1:7]],
    "exponents": {k: str(v) for k, v in budgets.items()},
    "scope": "Finite algebra only; polynomial bump is a calculus diagnostic, not a smooth test profile. No prime ideal theorem, density argument, asymptotic moment, or RH verification.",
}
print(json.dumps(record, indent=2, sort_keys=True))
