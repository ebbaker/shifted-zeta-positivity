#!/usr/bin/env python3
"""Exact finite algebra and rational budgets for mixed note 11.

Prepared for Edward Baker, 9 October 2026, with GPT-6 (Codex), inherited
configuration; exact serving variant and reasoning effort are not exposed.
This checker does not estimate any unbounded character correlation.
Uses the standard library, prints deterministic JSON, and writes no files.
"""

from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path


# A sixth root is its exponent modulo 6; None is the zero extension.
def multiply(*values):
    return None if any(v is None for v in values) else sum(values) % 6


def power(value, exponent):
    if exponent == 0:
        return 0
    return None if value is None else value * exponent % 6


def conjugate(value):
    return None if value is None else -value % 6


def main():
    assertions = 0

    def check(condition, label):
        nonlocal assertions
        if not condition:
            raise AssertionError(label)
        assertions += 1

    symbols = [None, *range(6)]
    for k, p, q in product(range(30), symbols, symbols):
        alpha, r = k % 2, k // 2
        row = multiply(p, power(q, 2))
        lhs = power(row, k)
        rhs = multiply(power(row, alpha), power(p, 2 * r),
                       conjugate(power(q, 2 * r)))
        check(lhs == rhs, "one-core joint cubic factor, including zero")

        residue = r % 3
        d, e, z = int(residue == 1), int(residue == 2), r // 3
        check(r == d + 2 * e + 3 * z, "unique cubic power extraction")
        # The extracted cubic power is one on units, zero at its support.
        mask = None if z > 0 and row is None else 0
        extracted = multiply(power(row, 2 * d), power(row, 4 * e), mask)
        check(power(row, 2 * r) == extracted,
              "cubic extraction retains every cube zero mask")

    for k, l, row in product(range(18), range(18), symbols):
        alpha, r = k % 2, k // 2
        beta, t = l % 2, l // 2
        check((k - l) % 2 == (alpha - beta) % 2,
              "quadratic projected conductor depends only on parity cores")
        check((k - l) % 3 == (alpha + 2 * r - beta - 2 * t) % 3,
              "cubic projected conductor retains square-factor data")
        actual = multiply(conjugate(power(row, k)), power(row, l))
        phase = power(row, (l - k) % 6)
        masked = None if row is None and (k > 0 or l > 0) else phase
        check(actual == masked, "ratio phase requires canceled-phase zero")

    h0 = F(71, 125)
    for h, same_core_survives in [(h0 - F(1, 10000), False),
                                  (h0, False),
                                  (h0 + F(1, 10000), True)]:
        check((2 * h > F(142, 125)) == same_core_survives,
              "strict radical boundary for f2=1")

    d = F(9, 25)
    m = F(54905017, 135320000)
    g = F(51935541903, 169150000000)
    s = F(3, 15625)
    mu = F(12288947, 169150000000)
    T = F(8884236001, 3383000000)
    C = T - (2 * (1 - mu) + g + d * m)
    check(C == 1 - g - (2 - 2 * d) * m - 3 * s + 2 * mu,
          "affordable middle exponent identity")
    p, q = F(13, 50), F(4, 25)
    c1 = F(2, 3) * min(p, q) + F(1, 3) * max(p, q)
    c2 = F(1, 3) * min(p, q) + F(2, 3) * max(p, q)
    check(c1 == F(29, 150), "first joint cubic term")
    check(c2 == F(17, 75), "second joint cubic term")
    check(p + q == F(21, 50), "exterior radical exponent")
    check(F(142, 125) - 2 * (p + q) == F(37, 125),
          "actual raw projected threshold")
    check(2 * m > F(37, 125), "distinct prime columns survive both cuts")

    phi = F(37, 150) - m / 6
    check(phi - C == F(1487314601, 253725000000),
          "existing grouped raw deficit")
    check(p + q - C == F(41749421609, 169150000000),
          "full core recombination deficit")
    for a in [F(0), m / 4, m / 2, 3 * m / 4, m]:
        ell = (m - a) / 2
        block = max(p + q + ell, c1 + 2 * ell, c2 + 5 * ell / 3)
        diag, recombined = a - 2 * m + block, 2 * a - 2 * m + block
        check(diag <= p + q - m, "diagonal core budget")
        check(recombined <= p + q, "positive core recombination budget")
        if a == m:
            check(diag == p + q - m, "large-core diagonal endpoint")
            check(recombined == p + q, "large-core recombination endpoint")

    # Infinite-series conclusions are proved in the note; these check the
    # stated exponents at one permissible loss, not convergence by sampling.
    delta = F(1, 1000)
    check(1 + 2 * delta > 1 and F(3, 2) + 3 * delta > 1,
          "first Cauchy weight series exponents")
    check(F(3, 2) - 3 * delta > 1,
          "cube series in leading bounded-coefficient term")
    check(3 - 2 * delta > 1 and F(9, 2) - 3 * delta > 1,
          "first cubic off-diagonal term series exponents")
    check(F(7, 3) - 2 * delta > 1 and F(7, 2) - 3 * delta > 1,
          "second cubic off-diagonal term series exponents")

    def number(v):
        return {"exact": str(v), "decimal": float(v)}

    source = Path(__file__)
    record = {
        "status": "passed",
        "assertions": assertions,
        "date": "2026-10-09",
        "provenance": "GPT-6 (Codex), inherited; exact variant/effort unavailable",
        "checker_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "scope": ["zero-preserving local root-of-unity algebra",
                  "exact projected parity/cubic predicates",
                  "strict cutoff boundary", "rational method budgets"],
        "not_verified": ["native reciprocity transfer", "large sieve proof",
                         "selected family population", "unbounded cross-core moment"],
        "parameters": {"m": number(m), "p": number(p), "q": number(q)},
        "budgets": {"affordable_C": number(C), "existing_grouped_phi": number(phi),
                    "existing_grouped_deficit": number(phi - C),
                    "positive_core_recombination": number(p + q),
                    "positive_core_recombination_deficit": number(p + q - C),
                    "same_core_diagonal": number(p + q - m)},
    }
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
