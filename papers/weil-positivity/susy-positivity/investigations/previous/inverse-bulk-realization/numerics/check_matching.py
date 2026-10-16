#!/usr/bin/env python3
"""Exact finite algebra checks; not an analytical proof checker."""

from fractions import Fraction as F
import json


def mass(alpha, n):
    return 2 * (n + alpha)


def kinetic(alpha, s, count):
    return sum(
        (2 / mass(alpha, n)) * s / (mass(alpha, n) ** 2 + s)
        for n in range(count)
    )


def main():
    alpha = F(1, 4)
    counts = {}

    count = 0
    for p in (2, 3, 5, 6):
        for s in (F(0), F(1, 9), F(1), F(17, 3)):
            original = kinetic(alpha, s, p * 7)
            refined = sum(
                kinetic((alpha + j) / p, s / p**2, 7)
                for j in range(p)
            ) / p
            assert original == refined
            count += 1
    counts["finite_gamma_tower_refinement"] = count

    count = 0
    residual_norm = F(3, 7)
    derivative_norm = F(5, 11)
    for p in (2, 3, 5, 6):
        for j in range(p):
            for n in range(8):
                a = mass(alpha, p * n + j)
                b = mass((alpha + j) / p, n)
                assert a == p * b
                original = (2 / a) * (
                    residual_norm**2 + derivative_norm**2 / a**2
                )
                refined = (F(1, p) * 2 / b) * (
                    residual_norm**2 + (derivative_norm / p) ** 2 / b**2
                )
                assert original == refined
                count += 1
    counts["positive_action_refinement"] = count

    direct = sorted((alpha + j) / 6 for j in range(6))
    two_then_three = sorted(
        ((alpha + j) / 2 + k) / 3
        for j in range(2) for k in range(3)
    )
    three_then_two = sorted(
        ((alpha + j) / 3 + k) / 2
        for j in range(3) for k in range(2)
    )
    assert direct == two_then_three == three_then_two
    assert F(1, 2) * F(1, 3) == F(1, 6)
    counts["composite_refinement"] = 2

    count = 0
    kappa = F(7, 4)
    for lam in (F(1, 3), F(2), F(19, 2)):
        for mu in (F(0), F(3, 5)):
            lhs = lam * (1 - kappa / (lam + mu)) ** 2
            excess = (
                2 * kappa * mu / (lam + mu)
                + kappa**2 * lam / (lam + mu)**2
            )
            assert lhs == lam - 2 * kappa + excess
            assert excess > 0
            count += 1
    counts["rational_feedback_identity"] = count

    f = w = F(1)
    assert w**2 - 2 * f * w == -1
    counts["driven_energy_is_not_jointly_nonnegative"] = 1

    result = {
        "status": "passed",
        "date": "2026-09-14",
        "arithmetic": "exact rational",
        "checks": counts,
        "total_checks": sum(counts.values()),
        "six_branch_shifts": [str(value) for value in direct],
        "scope": (
            "Finite algebra checks for the written identities. "
            "No verification of an infinite-dimensional proof, "
            "no constructed prime junction, and no Weil positivity certificate."
        ),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
