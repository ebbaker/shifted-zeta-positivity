#!/usr/bin/env python3
"""Finite exact checks for the integer quadratic response lift.

Prepared for Edward Baker, 2026-10-08, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited; exact variant and effort are not exposed.
These are coefficient/mask checks, not estimates of prime cancellation.
"""

from fractions import Fraction as Q
from math import gcd, isqrt
from pathlib import Path
import json


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def jacobi(n, u):
    assert u > 0 and u % 2 == 1
    n %= u
    sign = 1
    while n:
        while n % 2 == 0:
            n //= 2
            if u % 8 in (3, 5):
                sign = -sign
        n, u = u, n
        if n % 4 == u % 4 == 3:
            sign = -sign
        n %= u
    return sign if u == 1 else 0


def jacobi_by_factors(n, u):
    out = 1
    for p, exponent in factors(u).items():
        legendre = pow(n % p, (p - 1) // 2, p)
        if legendre == p - 1:
            legendre = -1
        out *= legendre ** exponent
    return out


def split_square(u):
    a = b = 1
    for p, exponent in factors(u).items():
        a *= p ** (exponent % 2)
        b *= p ** (exponent // 2)
    assert a * b * b == u
    return a, b


def root_count(H):
    return (isqrt(H) + 1) // 2


def main():
    mask_count = 0
    for u in range(1, 402, 2):
        a, b = split_square(u)
        for n in range(1, 258):
            symbol = jacobi(n, u)
            assert symbol == jacobi_by_factors(n, u)
            assert symbol == jacobi(n, a) * (gcd(n, b) == 1)
            mask_count += 1
    assert split_square(27) == (3, 3)
    assert jacobi(3, 9) == 0  # cancelled phase is still zero on a nonunit
    assert jacobi(3 * 3, 3) == 0
    for H in range(1, 1001):
        assert root_count(H) == sum(b % 2 == 1 for b in range(1, isqrt(H) + 1))

    # Rational formal prime-power coefficients substitute for Lambda(n)L(n/X).
    # The exact identity is coefficientwise, so no floating log or probe
    # quadrature is needed. All higher powers remain present.
    support = [n for n in range(2, 129) if len(factors(n)) == 1]
    coeff = {n: Q((-1) ** n * ((n % 11) - 5), n + 1) for n in support}
    prime_base = {n: next(iter(factors(n))) for n in support}

    def response(u):
        return sum((c * jacobi(n, u) for n, c in coeff.items()), Q(0))

    for u in range(1, 402, 2):
        a, b = split_square(u)
        deletion = sum((c * jacobi(n, a) for n, c in coeff.items()
                        if b % prime_base[n] == 0), Q(0))
        assert response(u) == response(a) - deletion

    H = 81
    rows = list(range(1, H + 1, 2))
    energy = sum((response(u) ** 2 for u in rows), Q(0))
    gram = Q(0)
    for n, cn in coeff.items():
        for m, cm in coeff.items():
            kernel = sum(jacobi(n * m, u) for u in rows)
            assert kernel == sum(jacobi(n, u) * jacobi(m, u) for u in rows)
            gram += cn * cm * kernel
    assert gram == energy
    for p in (3, 5, 7, 11):
        assert sum(jacobi(p * p, u) for u in rows) == sum(u % p != 0 for u in rows)
    grouped = sum((sum(response(a * b * b) ** 2
                       for b in range(1, isqrt(H // a) + 1, 2))
                   for a in rows if all(e == 1 for e in factors(a).values())), Q(0))
    assert grouped == energy

    conditional = []
    for h, loss in [(Q(1), Q(0)), (Q(1, 2), Q(0)), (Q(1, 4), Q(1, 20))]:
        beta = Q(1, 2) + loss / 2 + h / 4
        variance_power = 2 + loss + h / 2
        assert variance_power == 1 + 2 * beta
        # Large-sieve coherent term X^2 sqrt(H) / sqrt(H) is X^2.
        assert (2 + h / 2 - h / 2) / 2 == 1
        conditional.append({"h": str(h), "loss": str(loss), "beta": str(beta),
                            "variance_power": str(variance_power)})
    record = {
        "date": "2026-10-08",
        "arithmetic": "integer and exact rational",
        "mask_checks": mask_count,
        "odd_rows_checked_through": 401,
        "column_integers_checked_through": 257,
        "shared_factor_case": {"u": 27, "a": 3, "b": 3},
        "root_counts_checked_through": 1000,
        "formal_prime_power_columns": len(support),
        "gram_rows_upper_bound": H,
        "deletion_identity": True,
        "full_gram_identity": True,
        "primitive_grouping_identity": True,
        "diagonal_zero_mask": True,
        "conditional_exponents": conditional,
        "large_sieve_extraction_retains_exponent_one": True,
        "localized_example": {
            "h": "7/5", "conductor_cutoff": "3/5",
            "weighted_energy_power": "17/10", "conditional_beta": "17/20"
        },
        "scope": "Finite coefficient identities only; no asymptotic prime moment or zero-free theorem.",
    }
    h = Q(7, 5)
    assert 2 - h == Q(3, 5)
    assert 2 + (h - (2 - h)) / 2 == 1 + h
    assert 1 + h / 2 == Q(17, 10)
    assert Q(1, 2) + h / 4 == Q(17, 20)
    out = Path(__file__).with_name("integer_quadratic_lift_record_20261008.json")
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(f"All exact checks passed; wrote {out.name}")


if __name__ == "__main__":
    main()
