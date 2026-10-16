#!/usr/bin/env python3
"""Exact finite divisor algebra for the cofactor-inverse compensation scout.

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Uses an integer norm model and exact Gaussian-integer character values.
This checks finite convolution identities, not Eisenstein reciprocity,
Poisson completion, Schwartz estimates, or an asymptotic signed moment.
Prints a small deterministic JSON record and writes no files.
"""

import json
from fractions import Fraction
from math import isqrt


def divisors(n):
    small = []
    large = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]


def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def multiply(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def scale(k, x):
    return (k * x[0], k * x[1])


ROOTS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def character(n):
    # Quartic character modulo five, including its original zero extension.
    return {0: (0, 0), 1: (1, 0), 2: (0, 1),
            3: (0, -1), 4: (-1, 0)}[n % 5]


def selector(a, row):
    # Arbitrary row-dependent bounded coefficients supported in [10,20].
    if not 10 <= a <= 20:
        return (0, 0)
    return ROOTS[(a + row) % 4]


checks = 0


def check(condition):
    global checks
    checks += 1
    assert condition


# Verify the model character, including nonunit zeros.
for n in range(1, 41):
    for m in range(1, 41):
        check(character(n * m) == multiply(character(n), character(m)))

# z=20, upper profile constant C0=2, D=100, hence A_D=10.
# Every product in [100,200] and selected a in [10,20] has
# 1 < n/a <= 20, so the complete b-divisor channel vanishes.
for row in range(4):
    for n in range(100, 201):
        for a in divisors(n):
            if 10 <= a <= 20:
                k = n // a
                check(1 < k <= 20)
                check(sum(mobius(b) for b in divisors(k) if b <= 20) == 0)

        for cutoff in [Fraction(0), Fraction(1), Fraction(13),
                       Fraction(20), Fraction(30), Fraction(143),
                       Fraction(143, 2), Fraction(201)]:
            full = (0, 0)
            small = (0, 0)
            tail = (0, 0)
            for a in divisors(n):
                if not 10 <= a <= 20:
                    continue
                for b in divisors(n // a):
                    if b > 20:
                        continue
                    m = n // (a * b)
                    value = scale(-mobius(a) * mobius(b), selector(a, row))
                    product_phase = multiply(character(a), character(b * m))
                    check(product_phase == character(n))
                    value = multiply(value, product_phase)
                    full = add(full, value)
                    if a * b <= cutoff:
                        small = add(small, value)
                    else:
                        tail = add(tail, value)
            check(full == (0, 0))
            check(add(small, tail) == full)

# At the balanced product 13*11=143 and cutoff 30, the a=13,
# b=11,m=1 prime tuple survives; b=1,m=11 is in the small sector.
check(13 * 11 > 30)
check(13 <= 30)
check(mobius(13) * mobius(11) == 1)


def r(cutoff, n):
    return int(n == 1) - sum(mobius(d) for d in divisors(n) if d <= cutoff)


def truncated(cutoff, n):
    return mobius(n) if n <= cutoff else 0


# Asymmetric inverse identity, including its supported remainder.
for n in range(1, 401):
    mixed = sum(mobius(a) * mobius(b)
                for a in divisors(n) if a <= 10
                for b in divisors(n // a) if b <= 20)
    remainder = sum(mobius(d) * r(10, e) * r(20, n // (d * e))
                    for d in divisors(n)
                    for e in divisors(n // d))
    check(mobius(n) == truncated(10, n) + truncated(20, n)
          - mixed + remainder)
    if n <= 200:
        check(remainder == 0)
    if 20 < n <= 200:
        check(mobius(n) == -mixed)

theta = Fraction(1, 40)
h = Fraction(2, 5)
a = Fraction(2, 5)
check(1 - theta - h / 6 == Fraction(109, 120))
check(1 + h / 6 == Fraction(16, 15))
check(1 + h / 6 - h - a == Fraction(4, 15))

print(json.dumps({
    "status": "passed",
    "assertions": checks,
    "model": "free multiplicative divisor algebra with integer norms",
    "character_values": "exact Gaussian integers; quartic modulo five with zeros",
    "covered": [
        "bounded row-dependent selectors",
        "cofactor inverse including support endpoints",
        "adaptive small/tail coefficient decomposition",
        "complex multiplicative phases and deletion zeros",
        "strict tail cutoff at integer and noninteger boundaries",
        "surviving primepair tuple",
        "asymmetric inverse with supported remainder",
        "rational coherent support and power-gap exponents"
    ],
    "not_verified": [
        "physical Eisenstein reciprocity",
        "native conductor comparison",
        "Poisson completion",
        "weighted row mass",
        "prime ideal theorem",
        "an asymptotic signed moment"
    ]
}, indent=2, sort_keys=True))
