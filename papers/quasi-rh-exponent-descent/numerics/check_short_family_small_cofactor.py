#!/usr/bin/env python3
"""Exact finite checks for the short-family small-cofactor reduction.

The local residue fields use rational split primes 7, 13, 19, all of
cardinality 1 modulo 6. The checks concern local character coefficients
and exponent algebra, not an asymptotic moment or analytic Poisson bound.
"""

from fractions import Fraction as Q
from itertools import combinations
from math import gcd, prod
from pathlib import Path
import json


PRIMES = (7, 13, 19)
# Coordinates in Z[zeta_6], where zeta_6**2 = zeta_6 - 1.
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def prime_factors(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def logs_for_prime(p):
    primitive = next(
        g for g in range(2, p)
        if all(pow(g, (p - 1) // q, p) != 1 for q in prime_factors(p - 1))
    )
    result = {}
    x = 1
    for exponent in range(p - 1):
        result[x] = exponent % 6
        x = x * primitive % p
    assert len(result) == p - 1 and x == 1
    return primitive, result


LOGS = {p: logs_for_prime(p)[1] for p in PRIMES}


def char_phase(support, k):
    """None is a genuine character zero, not a phase exponent."""
    if any(k % p == 0 for p in support):
        return None
    return sum(LOGS[p][k % p] for p in support) % 6


def ratio_phase(left, right, k):
    a, b = char_phase(left, k), char_phase(right, k)
    return None if a is None or b is None else (a - b) % 6


def primitive_ratio(left, right, k):
    return ratio_phase(left - right, right - left, k)


def exact_sum(phases):
    a = b = 0
    for phase in phases:
        if phase is not None:
            x, y = ROOTS[phase]
            a += x
            b += y
    return [a, b]


def coefficient_checks():
    supports = [
        frozenset(choice)
        for size in range(len(PRIMES) + 1)
        for choice in combinations(PRIMES, size)
    ]
    comparisons = 0
    complete_sums = []
    for left in supports:
        for right in supports:
            common = left & right
            conductor = prod(left ^ right)
            common_norm = prod(common)
            assert conductor * common_norm**2 == prod(left) * prod(right)
            assert gcd(conductor, common_norm) == 1
            period = prod(left | right)
            for k in range(period):
                actual = ratio_phase(left, right, k)
                psi = primitive_ratio(left, right, k)
                masked = None if gcd(k, common_norm) != 1 else psi
                assert actual == masked
                comparisons += 1
            complete = exact_sum(ratio_phase(left, right, k) for k in range(period))
            if left != right:
                assert conductor > 1
                assert complete == [0, 0]
                complete_sums.append({
                    "left": prod(left), "right": prod(right),
                    "conductor": conductor, "shared_mask": common_norm,
                    "period": period, "sum_Z_zeta6": complete,
                })
            else:
                assert complete == [prod(p - 1 for p in left), 0]
    left, right, k = frozenset((7, 13)), frozenset((7, 19)), 7
    assert ratio_phase(left, right, k) is None
    assert primitive_ratio(left, right, k) is not None
    return comparisons, complete_sums


def vector(**kwargs):
    return {key: Q(value) for key, value in kwargs.items() if value}


def combine(*terms):
    result = {}
    for term in terms:
        for key, value in term.items():
            result[key] = result.get(key, Q(0)) + value
    return {key: value for key, value in result.items() if value}


def scaled(multiplier, term):
    return {key: multiplier * value for key, value in term.items()}


def exponent_checks():
    # Physical scales: H=D^h, B=D^b, F=D^f, X=D^(1-b-f).
    x = vector(one=1, b=-1, f=-1)
    r = vector(one=2, h=-1, b=-2)
    outside_and_counts = vector(h=1, one=-2, b=2, f=1)
    pair_cost = combine(outside_and_counts, scaled(2, x), r)
    diagonal_cost = combine(outside_and_counts, x, r)
    assert pair_cost == vector(one=2, b=-2, f=-1)
    assert diagonal_cost == vector(one=1, b=-1)
    # t_d exponent minus Z exponent = g-d >= 0, since d divides gcd.
    t_d = vector(f=2, g=2, h=-1, d=-1)
    z = vector(f=2, g=1, h=-1)
    assert combine(t_d, scaled(-1, z)) == vector(g=1, d=-1)
    # A generic fixed positive buffer remains admissible at every h>0.
    examples = []
    for h in (Q(8, 9), Q(4, 5), Q(2, 3), Q(1, 4)):
        beta = Q(1, 2) + 5 * h / 12
        examples.append({
            "h": str(h), "b_cutoff_exponent": str(1 - h),
            "f_cutoff_exponent": str(h / 2), "beta_if_new_moment": str(beta),
        })
        eta = h / 20
        b_max, f_max = 1 - h + eta, h / 2 + eta
        assert 1 - b_max - f_max == h / 2 - 2 * eta > 0
        assert 1 - h - b_max == -eta
        assert 2 * f_max - h == 2 * eta
    assert examples[0]["beta_if_new_moment"] == "47/54"
    assert Q(7, 8) - Q(47, 54) == Q(1, 216)
    return examples


def main():
    comparisons, complete_sums = coefficient_checks()
    record = {
        "status": "all exact coefficient and exponent checks passed",
        "model": "GPT-6 (Codex), inherited; exact serving variant and effort unexposed",
        "scope": "Finite residue-field identities and rational exponents only; no asymptotic moment.",
        "local_residue_cardinalities": list(PRIMES),
        "pointwise_zero_mask_comparisons": comparisons,
        "nonprincipal_complete_period_checks": len(complete_sums),
        "nonprincipal_complete_periods": complete_sums,
        "shared_mask_countercheck": {
            "m1": 91, "m2": 133, "k": 7,
            "actual_product_is_zero": True,
            "primitive_ratio_without_shared_mask_is_nonzero": True,
        },
        "continuous_exponent_certificates": {
            "total_pair_count_cost": "2-2*b-f <= 2 for b,f>=0",
            "transformed_diagonal_cost": "1-b",
            "poisson_t_over_Z_exponent": "g-d >= 0 since d|gcd",
            "residual_column_length_lower_exponent": "h/2-2*eta > 0 for eta<h/10",
            "positive_dual_counterexample_growth_ratio": "D^(1-h)",
        },
        "conditional_examples": exponent_checks(),
    }
    path = Path(__file__).with_name("short_family_small_cofactor_check.json")
    path.write_text(json.dumps(record, indent=2) + "\n")
    print(f"PASS: {comparisons} masks, {len(complete_sums)} complete periods, exponent identities")
    print(path)


if __name__ == "__main__":
    main()
