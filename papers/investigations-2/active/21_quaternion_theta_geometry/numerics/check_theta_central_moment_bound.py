#!/usr/bin/env python3
"""Exact rational constants for a complete-theta central moment inequality.

14 October 2026. Prepared for Edward Baker with LLM assistance.
Recorded model: gpt-6.1-sol; reasoning effort: ultra.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path


def exp_lower(x, degree):
    return sum((x ** k / factorial(k) for k in range(degree + 1)), Q(0))


def exp_upper(x, degree):
    assert x < degree + 2
    return exp_lower(x, degree) + x ** (degree + 1) / factorial(degree + 1) / (1 - x / (degree + 2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    b = Q(7, 25)
    sphere_free_tail_integral = (2 * b ** 3 / 28 ** 2 + 10 * b ** 2 / 28 ** 3
                                + 24 * b / 28 ** 4 + Q(24, 28 ** 5))
    signed_moment_margin = Q(37, 500000) - Q(5, 8) * sphere_free_tail_integral
    central_scalar_margin = Q(597, 25000) - Q(1, 560)
    checks = {
        "exp_1_upper_lt_11_over_4": exp_upper(Q(1), 6) < Q(11, 4),
        "exp_1_lower_gt_8_over_3": exp_lower(Q(1), 4) > Q(8, 3),
        "exp_2_over_5_upper_lt_3_over_2": exp_upper(Q(2, 5), 2) < Q(3, 2),
        "exp_28_over_25_lower_gt_153_over_50": exp_lower(Q(28, 25), 7) > Q(153, 50),
        "complete_series_ratio_lt_half": 16 * Q(3, 8) ** 9 < Q(1, 2),
        "theta_core_lower_gt_6_over_25": Q(1485, 49) * Q(9, 7) * Q(4, 11) ** 5 > Q(6, 25),
        "tail_exponent_lt_minus_69_over_10": Q(1624, 625) - Q(153, 16) < -Q(69, 10),
        "tail_slope_lt_minus_28": 9 + Q(14, 25) - Q(153, 4) < -28,
        "exp_69_over_10_lower_gt_800": Q(8, 3) ** 6 * (1 + Q(9, 10) + Q(9, 10) ** 2 / 2) > 800,
        "positive_integrand_through_b": 1 - Q(25, 2) * b ** 2 == Q(1, 50),
        "signed_tail_integral_exact_value": sphere_free_tail_integral == Q(3497259, 33614000000),
        "signed_moment_margin_exact_value": signed_moment_margin == Q(2413193, 268912000000),
        "signed_moment_margin_gt_1_over_120000": signed_moment_margin > Q(1, 120000),
        "central_scalar_margin_gt_1_over_50": central_scalar_margin > Q(1, 50),
        "slope_domain_contains_8": Q(8) ** 2 / 6 <= Q(25, 2),
        "curvature_domain_contains_5": Q(5) ** 2 / 2 <= Q(25, 2),
        "stationary_L0_margin": Q(3, 125) * Q(1, 120000) == Q(1, 5000000),
    }
    result = {
        "checker_source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "fractions.Fraction (exact)",
        "date": "2026-10-14",
        "prepared_for": "Edward Baker",
        "model": "gpt-6.1-sol", "reasoning_effort": "ultra",
        "scope": "Exact constant checks supporting the analytic proof; no global theta sign certificate",
        "classical_pi_bounds_used": "25/8 < pi < 22/7; pi^2 < 10",
        "time_domain": "0 <= t <= 1",
        "source_bounds": {
            "core": "Phi(r) > 6/25 for 0 <= r <= 1/10",
            "complete_tail": "exp(t*r^2)*Phi(r) < exp(-28*(r-7/25))/20 for r >= 7/25",
        },
        "signed_moment_margin": str(signed_moment_margin),
        "central_scalar_margin": str(central_scalar_margin),
        "consequences": {
            "moment": "M2-(25/2)*M4 > 1/120000",
            "slope": "-Hx(t,x) > x/120000 for 0 < x <= 8",
            "curvature": "Hxx(t,x) < -1/120000 for |x| <= 5",
            "central_scalar": "H(t,x) > 1/50 for |x| <= 1",
            "physical_fueter_norm": "|F(t,x)| > 1/120000 for |x| <= 8",
            "stationary_L0": "L0(t,0) > 1/5000000",
        },
        "checks": checks,
        "all_pass": all(checks.values()),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"all_pass": result["all_pass"], "check_count": len(checks),
                      "checker_source_sha256": result["checker_source_sha256"]}))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
