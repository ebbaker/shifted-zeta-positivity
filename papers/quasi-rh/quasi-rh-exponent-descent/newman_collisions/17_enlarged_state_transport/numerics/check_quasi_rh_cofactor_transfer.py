#!/usr/bin/env python3
"""Exact finite checks for the conditional quasi-RH cofactor transfer.

These checks verify rational exponent bookkeeping and finite coefficient
identities. They do not verify the imported quasi-RH theorem or prime
counting consequence, partial summation, lattice asymptotics, or any
unbounded moment estimate.

The analytic source uses a squarefree good ideal P: every prime-ideal
factor avoids the original fixed exclusion set S. All original physical
zero extensions and good-monoid masks remain in place. Norm entries below
are formal labels for distinct prime ideals; repeated norm entries are
intentional and are never merged. The finite examples do not instantiate
all analytic support restrictions.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def check() -> dict:
    q = Fraction
    h = q(30, 41)
    row_root_exponent = h / 6
    theta = q(11, 12)
    exponent_checks = (
        row_root_exponent == q(5, 41),
        2 + row_root_exponent == q(87, 41),
        1 + h == q(71, 41),
        (2 + row_root_exponent) - (1 + h) == q(16, 41),
        ((2 + row_root_exponent) - (1 + h)) / 2 == q(8, 41),
        (q(1, 2) - q(1, 20)) * (1 - theta) == q(3, 80),
        (1 + theta) / 2 + q(1, 20) * (1 - theta) == q(77, 80),
        (q(1, 2) - q(1, 4)) * (1 - theta) == q(1, 48),
        q(1, 2) - q(1, 4) > row_root_exponent,
    )
    for index, passed in enumerate(exponent_checks, start=1):
        if not passed:
            raise AssertionError(f"Exponent check {index} failed")

    coefficient_checks = 0
    cost_checks = 0
    cases = []
    for norms in ((7,), (7, 7), (7, 13, 19), (7, 7, 13, 13)):
        size = len(norms)
        subsets = [
            tuple(i for i in range(size) if mask >> i & 1)
            for mask in range(1 << size)
        ]
        divisor_norm = {subset: 1 for subset in subsets}
        for subset in subsets:
            for index in subset:
                divisor_norm[subset] *= norms[index]
        coefficients = dict(divisor_norm)
        for subset in subsets:
            for index, norm in enumerate(norms):
                if index not in subset:
                    coefficients[subset] *= 1 - norm

        for divisor in subsets:
            total = sum(
                coefficients[multiple]
                for multiple in subsets
                if set(divisor) <= set(multiple)
            )
            if total != divisor_norm[divisor]:
                raise AssertionError((norms, divisor, total))
            coefficient_checks += 1

        product_cost = 1
        for norm in norms:
            product_cost *= 2 * norm - 1
        if sum(abs(value) for value in coefficients.values()) != product_cost:
            raise AssertionError((norms, "coefficient cost"))
        cost_checks += 1
        cases.append({
            "distinct_prime_ideal_norm_labels": list(norms),
            "divisor_count": len(subsets),
            "exact_l1_coefficient_cost": product_cost,
        })

    total_checks = len(exponent_checks) + coefficient_checks + cost_checks
    return {
        "date": "2026-10-10",
        "model": "GPT-6 (Codex)",
        "reasoning_effort": "Not exposed; not inferred",
        "status": "passed",
        "exact_checks": total_checks,
        "exponent_checks": len(exponent_checks),
        "divisor_coefficient_checks": coefficient_checks,
        "coefficient_cost_checks": cost_checks,
        "exponents": {
            "row_length": str(h),
            "sixth_power_root_length": str(row_root_exponent),
            "assumed_prime_counting_exponent": str(theta),
            "raw_filter_energy": str(2 + row_root_exponent),
            "full_moment_target": str(1 + h),
            "raw_exponent_gap": str(q(16, 41)),
            "cost_normalized_beta_threshold": str(q(8, 41)),
            "old_beta_endpoint": str(q(1, 20)),
            "old_range_minimum_pnt_gain": str(q(3, 80)),
            "direct_beta_endpoint": str(q(1, 4)),
            "direct_range_minimum_pnt_gain": str(q(1, 48)),
        },
        "cases": cases,
        "source_notes": [
            "The analytic P is squarefree and consists of good prime ideals avoiding the fixed exclusion set S.",
            "Every physical zero extension and original good-monoid mask is retained.",
            "Equal norms label distinct prime ideals and are deliberately retained as distinct indices.",
            "Prime-counting error is imported conditionally from the assumed October 5 paper, Corollary 1.2, using only modulus 3.",
        ],
        "limitations": [
            "Exact finite checks only; not independent mathematical validation.",
            "No verification of the imported theorem, prime-counting asymptotic, partial summation, or lattice count.",
            "No bound or lower bound for the complete actual short-family response is established.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--record", type=Path,
        help="Write the deterministic JSON verification record to this path.",
    )
    args = parser.parse_args()
    result = check()
    serialized = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.record is not None:
        args.record.parent.mkdir(parents=True, exist_ok=True)
        args.record.write_text(serialized, encoding="utf-8")
    print(serialized, end="")


if __name__ == "__main__":
    main()
