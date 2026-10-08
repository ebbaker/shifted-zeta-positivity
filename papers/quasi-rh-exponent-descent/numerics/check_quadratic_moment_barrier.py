#!/usr/bin/env python3
"""Exact finite checks of quadratic moment structure and method limitations.

GPT-6 (Codex), inherited configuration, 2026-10-08. Exact variant and
reasoning effort are not exposed. No prime asymptotic is numerically tested.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
import json

from check_integer_quadratic_lift import factors, jacobi


def mu(n):
    fac = factors(n)
    return 0 if any(e > 1 for e in fac.values()) else (-1) ** len(fac)


def transform_checks():
    count = 0
    for a in range(1, 402, 2):
        square_divisors = [d for d in range(1, isqrt(a) + 1, 2) if a % (d*d) == 0]
        for k in range(1, 130, 2):
            lhs = mu(a) ** 2 * jacobi(k, a)
            rhs = sum(mu(d) * jacobi(k, a // (d*d))
                      for d in square_divisors if gcd(d, k) == 1)
            assert lhs == rhs
            count += 1
    # Without the canceled-phase mask this coefficient is false.
    unmasked = sum(mu(d) * jacobi(3, 9 // (d*d)) for d in (1, 3))
    assert unmasked == -1 and mu(9) ** 2 * jacobi(3, 9) == 0
    return count


def gram_checks():
    records = []
    for ceiling in (9, 21, 35):
        rows = [a for a in range(1, ceiling + 1, 2) if mu(a)]
        primes = [p for p in range(ceiling + 1, ceiling + 120)
                  if factors(p) == {p: 1}]
        # Arbitrary positive rational weights; the inequality is not specific
        # to square-root weights, and no float radicals are needed.
        weights = {a: F(1, a) for a in rows}
        coeff = {p: F(p % 11 - 5, p % 7 + 1) for p in primes}
        kernel = {(p, q): sum((weights[a] * jacobi(p*q, a) for a in rows), F(0))
                  for p in primes for q in primes}
        absolute_offdiag = sum((abs(coeff[p] * coeff[q] * kernel[p, q])
                                for p in primes for q in primes if p != q), F(0))
        diagonal = sum((coeff[p] ** 2 * kernel[p, p] for p in primes), F(0))
        positive_gram = sum((abs(coeff[p]) * abs(coeff[q]) * kernel[p, q]
                             for p in primes for q in primes), F(0))
        positive_rows = sum((weights[a] * sum((abs(coeff[p]) * jacobi(p, a)
                                              for p in primes), F(0)) ** 2
                             for a in rows), F(0))
        principal_lower = sum((abs(coeff[p]) for p in primes), F(0)) ** 2
        assert positive_gram == positive_rows
        assert positive_gram >= principal_lower
        assert absolute_offdiag >= principal_lower - diagonal
        assert principal_lower > diagonal
        records.append({"conductor_ceiling": ceiling, "rows": len(rows),
                        "prime_columns": len(primes),
                        "gram_identity": True, "positive_offdiagonal_lower_bound": True})
    return records


def envelope_checks():
    records = []
    for B in (F(3, 4), F(7, 8), F(9, 10), F(19, 20)):
        for h in (F(6, 5), F(7, 5), F(3, 2), F(7, 4), F(19, 10)):
            cap, crossing = 2-h, 2-2*B
            candidates = [F(0), cap]
            if 0 <= crossing <= cap:
                candidates.append(crossing)
            exact = max(min(2*B + a/2, 2-a/2) for a in candidates)
            formula = 1+B if h <= 2*B else 1+2*B-h/2
            assert exact == formula
            target = 1+h/2
            assert (exact <= target) == (h >= 2*B)
            if h < 4*B-2:
                assert h < 2*B
                assert exact-target == B-h/2 > 1-B
            records.append({"B": str(B), "h": str(h), "bound_power": str(exact),
                            "target_power": str(target), "fits": exact <= target})
    B, h = F(7, 8), F(7, 5)
    assert 2-2*B == F(1, 4)
    assert 1+B == F(15, 8)
    assert B-h/2 == F(7, 40)
    assert (1+h/2)/2 == F(17, 20)
    # The sharp abstract block uses total response mass exponent exactly two.
    assert (2-2*B) + 2*B == 2
    assert (2-2*B)/2 + 2*B == 1+B
    return records


def main():
    result = {
        "date": "2026-10-08",
        "arithmetic": "integer and exact rational; no floating square roots",
        "masked_squarefree_coefficient_checks": transform_checks(),
        "mask_omission_countercheck": True,
        "positive_gram_checks": gram_checks(),
        "rational_envelope_checks": envelope_checks(),
        "example": {"B": "7/8", "h": "7/5", "bottleneck_conductor_power": "1/4",
                    "target_power": "17/10", "available_power": "15/8",
                    "missing_energy_saving": "7/40"},
        "scope": "Finite identities and method bookkeeping only; no arithmetic moment or zero-free region.",
    }
    output = Path(__file__).with_name("quadratic_moment_barrier_record_20261008.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: masked transform, positive Gram obstruction, and exact envelope checks")


if __name__ == "__main__":
    main()
