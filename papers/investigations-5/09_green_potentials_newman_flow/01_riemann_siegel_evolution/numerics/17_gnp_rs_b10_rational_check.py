#!/usr/bin/env python3
"""Exact exponent bookkeeping for GNP-RS-B10; not an analytic certificate.

12 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Actual model/effort unavailable in chat0007's recorded configurations.
Run with Python's standard library; no zeta samples or height campaign.
"""

from fractions import Fraction as F
import json


def main():
    beta, alpha, head = F(17, 81), F(1, 3), F(1, 10)
    theta, published, eps_src = F(19, 60), F(1515, 4816), F(151, 144480)
    low = lambda x: F(2, 7) - F(3, 14) * x + x * x / 2
    amp_square = alpha * (1 - alpha) / 2
    checks = {}

    def eq(name, actual, expected):
        assert actual == expected, (name, actual, expected)
        checks[name] = {"value": str(actual), "expected": str(expected), "passed": True}

    eq("window_exponent_gain", F(17, 72) - beta, F(17, 648))
    eq("source_slack", theta - published, F(151, 72240))
    eq("source_epsilon_half_slack", theta - published - eps_src, eps_src)
    eq("high_amplitude_square_exponent", amp_square, F(1, 9))
    eq("high_window_power", theta - amp_square, F(37, 180))
    eq("high_norm_square_margin", beta - theta + amp_square, F(7, 1620))
    eq("high_residual_margin", (beta - theta + amp_square) / 2, F(7, 3240))
    eq("final_fixed_cap", (beta - theta + amp_square) / 4, F(7, 6480))
    eq("low_top_power", low(alpha), F(17, 63))
    eq("low_bottom_power", low(head), F(377, 1400))
    eq("convex_endpoint_gap", low(alpha) - low(head), F(1, 1800))
    eq("low_threshold_balance", low(alpha) - F(9, 7) * beta, F(0))
    eq("final_rho_coefficient", F(9, 7) / 4, F(9, 28))
    eq("head_norm_square_margin", head / 4, F(1, 40))
    eq("head_multiplier_margin", head / 8, F(1, 80))
    eq("finite_head_margin", beta - 2 * head, F(4, 405))
    eq("reflected_margin", beta - F(3, 4) * head, F(437, 3240))
    eq("large_shift_power", F(3, 8) - 4 * beta, -F(301, 648))
    eq("head_norm_offdiag_power", F(11, 4) * head - 2 * beta, -F(469, 3240))
    eq("reflected_frequency_exponent", 5 * head, F(1, 2))
    eq("rho_range", F(1, 2) - beta, F(47, 162))
    eq("old_BW_internal_gate_failure", F(1, 2) - 2 * F(17, 72), F(1, 36))
    delta = F(1, 144)
    example_beta = F(17, 72) - delta
    eq("acceptance_window_exponent", example_beta, F(11, 48))
    eq("acceptance_rho", example_beta - beta, F(25, 1296))
    eq("acceptance_old_growth", F(9, 7) * delta, F(1, 112))
    eq("acceptance_new_low_power", low(alpha) - F(9, 7) * example_beta, -F(25, 1008))
    eq("acceptance_new_high_power", theta - amp_square - example_beta, -F(17, 720))
    assert 0 < delta < F(1, 72)
    assert 0 < theta < 1 and 0 < eps_src < theta - published
    assert F(1, 10) < F(1, 3) < F(1, 2) and 5 * head < F(7, 8)
    fixed_margin = F(7, 3240)
    assert all(x > fixed_margin for x in [head / 8, beta - 2 * head,
        beta - F(3, 4) * head, F(1, 32), F(1, 18), F(301, 1296)])
    print(json.dumps({
        "status": "passed_exact_fraction_bookkeeping",
        "parameters": {"beta": str(beta), "Z_exponent": str(alpha),
            "M_Y_exponent": str(head), "theta": str(theta),
            "source_epsilon": str(eps_src)},
        "checks": checks,
        "scope": "Exact rational exponents only; no analytic proof, numerical onset, or collision certificate."
    }, indent=2))


if __name__ == "__main__":
    main()
