#!/usr/bin/env python3
"""18 November 2026: fixed, source-free rational replay for Edward Baker.

Prepared with OpenAI Codex LLM assistance; actual model/effort unavailable
in chat0004. This checks the finite arithmetic in Note32, not a canonical
source estimate. No source sampling, parameter search or external library.
Run from any directory; JSON is printed to stdout for a small run record.
"""
import json
from fractions import Fraction as Q
from math import factorial


def ratio(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def main():
    d, dp = Q(".1787368"), Q(".1787369")
    b, bp = Q(".6037742"), Q(".6037744")
    duration, stop, f = Q(".1003"), Q(".0001"), Q(3, 10)
    v, vm = 1 - 2 * d * b, 1 - 2 * dp * bp
    kcap = Q(1057, 375000)
    force_diff = Q(1000, 423) - Q(423, 500) * Q(151, 250)
    exp8_lower = sum((Q(8) ** k / factorial(k) for k in range(11)), Q(0))
    log_argument = Q(82637, 37)
    constant_k_endpoint = dp - 2 * vm * duration + (vm**2 + kcap - 1) * duration**2 / dp
    required_k = 1 - vm**2 + dp * (stop - dp + 2 * vm * duration) / duration**2
    lam2 = 2 * f
    w = 4 * lam2 * duration**2
    jcoef = d / 2 + (2 * d * b**2 - 2 * b) / lam2
    cosh_head = sum((w**j / factorial(2 * j) for j in range(5)), Q(0))
    sinh_head = 2 * duration * sum((w**j / factorial(2 * j + 1) for j in range(5)), Q(0))
    cosh_tail = (w**5 / factorial(10)) / (1 - w / (12 * 11))
    sinh_tail = 2 * duration * (w**5 / factorial(11)) / (1 - w / (13 * 12))
    lower = d + jcoef * (cosh_head + cosh_tail - 1) - v * (sinh_head + sinh_tail)
    tail_payment = -jcoef * cosh_tail + v * sinh_tail
    r, c, dmax, q = Q(9, 10), Q(1, 10), Q(1, 5), Q(11, 25)
    source_b = r * (12 / q**2 + 16 * dmax / q**3)
    source_log = r * 2 * (r + c) * (24 / q**3 + 48 * dmax / q**4)
    checks = {
        "anchor_gap_squared_below_0846_squared": 4 * dp < Q(423, 500)**2,
        "force_difference_above_185": force_diff > Q(37, 20),
        "exp8_rational_lower_exceeds_log_argument": exp8_lower > log_argument,
        "constant_k_endpoint_below_minus_00008239": constant_k_endpoint < -Q(8239, 10**8),
        "required_constant_k_above_00605917": required_k > Q(605917, 10**8),
        "constant_k_cap_below_required_floor": kcap < required_k,
        "negative_cosh_coefficient": jcoef < 0,
        "positive_v": v > 0,
        "taylor_ratios_below_one": 0 < w < 12 * 11,
        "retained_f_endpoint_above_00016246": lower > Q(16246, 10**8),
        "retained_f_margin_above_00006246": lower - stop > Q(6246, 10**8),
        "taylor_payment_below_390e_minus_15": tail_payment < Q(390, 10**17),
        "comparison_m_bounded_by_initial_b": 2 * b**2 > f,
        "comparison_d_strictly_decreases_when_positive": 4 * b * d < 2,
        "trial_q_exact": (r - c)**2 - dmax == q,
        "source_b_coefficient": source_b == Q(119250, 1331),
        "source_log_coefficient": source_log == Q(14175000, 14641),
    }
    result = {
        "date": "2026-11-18",
        "prepared_for": "Edward Baker",
        "assistance": "OpenAI Codex LLM assistance",
        "recorded_model": None,
        "recorded_effort": None,
        "scope": "Exact rational scalar comparisons only; no canonical source evaluation or certificate of the forcing floor",
        "parameters": {"d": str(d), "d_plus": str(dp), "b": str(b), "b_plus": str(bp),
                       "duration": str(duration), "stop": str(stop), "physical_forcing_floor": str(f)},
        "checks": checks,
        "all_passed": all(checks.values()),
        "constant_k_endpoint": ratio(constant_k_endpoint),
        "required_constant_k": ratio(required_k),
        "retained_f_endpoint_lower": ratio(lower),
        "retained_f_margin_lower": ratio(lower - stop),
        "taylor_tail_payment": ratio(tail_payment),
        "source_error_coefficients": {"B": str(source_b), "log": str(source_log)},
    }
    print(json.dumps(result, indent=2))
    if not result["all_passed"]:
        raise SystemExit("A fixed arithmetic claim failed; do not broaden the check.")


if __name__ == "__main__":
    main()
