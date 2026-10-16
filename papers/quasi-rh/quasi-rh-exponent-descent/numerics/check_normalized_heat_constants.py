#!/usr/bin/env python3
"""Exact final-constant checks for NORMALIZED_HEAT_COLLISION_CRITERION.

The disk estimates and imported approximation theorem are analytical inputs;
this script checks only the rational implications at the end of the proof.
It does not verify an RH statement or a finite-height rectangle numerically.
"""
from fractions import Fraction as F
import json


def main():
    p_lower = F(496, 1000) + F(62, 8) - F(15, 10000)
    omega_ratio_lower = (F(499, 1000) - F(128, 1000000)) / 2
    power_sum_constant = F(7, 6) + 2 * F(7, 6)
    tail = F(1, 256) + F(1, 896)
    eta_bound = F(13, 10) * (F(4, 10**40) + F(1, 10**100) + 2 * tail)
    eta_round = F(14, 1000)
    criterion_bound = (eta_round / 2)**2 + (eta_round / F(48, 100))**2
    assert p_lower > 8
    assert omega_ratio_lower > F(24, 100)
    assert power_sum_constant < 4
    assert eta_bound < eta_round
    assert criterion_bound < F(1, 1000) < 1
    print(json.dumps({
        "status": "exact rational implications passed",
        "scope": "Analytic disk/source estimates are inputs; no sampled heat values or compact rectangle certificate.",
        "p_lower": str(p_lower),
        "omega_over_log_lower": str(omega_ratio_lower),
        "power_sum_multiplier": str(power_sum_constant),
        "leading_pair_tail_bound": str(tail),
        "eta_is_less_than": str(eta_round),
        "cosine_sine_contradiction_bound": str(criterion_bound),
    }, indent=2))


if __name__ == '__main__':
    main()
