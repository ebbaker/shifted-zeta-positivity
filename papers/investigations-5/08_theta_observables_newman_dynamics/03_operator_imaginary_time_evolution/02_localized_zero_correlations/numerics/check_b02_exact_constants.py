#!/usr/bin/env python3
"""Exact rational bookkeeping for Note04; not a theta numerical experiment.

Prepared for Edward Baker with substantial OpenAI Codex assistance,
7 November 2026. Actual exact backend model/effort unavailable.
Python standard library only. Prints a small JSON record to stdout.
The analytic weak-test proof and the logarithmic integral remain in Note04.
"""

from fractions import Fraction as Q
import json


def integrate_polynomial(coefficients, left, right):
    return sum(
        coefficient * (right ** (power + 1) - left ** (power + 1)) / (power + 1)
        for power, coefficient in enumerate(coefficients)
    )


def main():
    # For psi=(1-r^2)^2, q=r^2, dA=pi dq and Delta psi=16q-8.
    positive = [Q(-8), Q(16)]
    negative = [Q(8), Q(-16)]
    mass_plus = integrate_polynomial(positive, Q(1, 2), Q(1))
    mass_minus = integrate_polynomial(negative, Q(0), Q(1, 2))
    plus_r4 = integrate_polynomial([Q(0), Q(0)] + positive, Q(1, 2), Q(1)) / mass_plus
    minus_r4 = integrate_polynomial([Q(0), Q(0)] + negative, Q(0), Q(1, 2)) / mass_minus
    a_plus = plus_r4 + Q(1, 16)
    a_minus = minus_r4 + Q(1, 16)
    true_statistic = 2 * (1 - Q(1, 4)) ** 2
    t = 2 * true_statistic
    exp_cubic_lower = 1 + t + t**2 / 2 + t**3 / 6
    assert mass_plus == mass_minus == 2
    assert (plus_r4, minus_r4) == (Q(17, 24), Q(1, 24))
    assert (a_plus, a_minus, true_statistic) == (Q(37, 48), Q(5, 48), Q(9, 8))
    assert exp_cubic_lower > a_plus / a_minus

    clearance = Q(25, 6) - 4
    local_log_coefficient = Q(1, 2) * clearance**2  # multiplies pi*m*log(2)
    allowance_coefficient = 2 * local_log_coefficient  # multiplies m*log(2)
    defect_squared_coefficient = allowance_coefficient / 2
    assert clearance == Q(1, 6)
    assert local_log_coefficient == Q(1, 72)
    assert allowance_coefficient == Q(1, 36)
    assert defect_squared_coefficient == Q(1, 72)
    print(json.dumps({
        "task": "TND-OC-B02",
        "prepared_for": "Edward Baker",
        "local_date": "2026-11-07",
        "llm_assistance": "substantial OpenAI Codex",
        "actual_exact_backend_model": None,
        "actual_effort": None,
        "arithmetic": "Python fractions.Fraction, exact rational",
        "scope": "Two predeclared algebraic constant checks; no canonical field or zeros evaluated",
        "radial_jensen_control": {
            "laplacian_mass_in_units_of_pi": str(mass_plus),
            "a_plus": str(a_plus), "a_minus": str(a_minus),
            "true_statistic": str(true_statistic),
            "exp_cubic_lower": str(exp_cubic_lower),
            "ratio": str(a_plus / a_minus),
            "strict_log_comparison_verified": True,
        },
        "harmonic_allowance": {
            "disk_clearance": str(clearance),
            "l1_coefficient_in_units_of_pi_m_log2": str(local_log_coefficient),
            "q_allowance_coefficient_in_units_of_m_log2": str(allowance_coefficient),
            "d_squared_stop_coefficient_in_units_of_m_log2": str(defect_squared_coefficient),
        },
        "status": "exact_bookkeeping_passed_not_an_analytic_or_theta_certificate",
    }, indent=2) + "\n")


if __name__ == "__main__":
    main()
