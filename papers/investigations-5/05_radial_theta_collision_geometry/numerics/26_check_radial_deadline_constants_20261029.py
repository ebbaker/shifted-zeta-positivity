#!/usr/bin/env python3
"""R9 constants only: exact rational checks; floating illustrations are not certificates.
Prepared for Edward Baker, 29 October 2026; substantial LLM assistance,
gpt-6-astra / recorded effort max, Investigation05 chat0030.
No theta acquisition, quadrature or PDE simulation.
"""
from fractions import Fraction as Q
import json
import math

k = Q(21, 20)
checks = {
    'exponential_upper_below_5_over_4': Q(925, 756) < Q(5, 4),
    'carrier_ratio_below_9': Q(26, 3) < 9,
    'Z_fifth_power_majorant_below_243': Q(400 * 4 * 9**3, 49 * 512) < 3**5,
    'k_power_7_below_3_over_2': k**7 < Q(3, 2),
    'k_power_3_below_6_over_5': k**3 < Q(6, 5),
    'first_term_square_below_81_over_100': Q(45, 56) < Q(81, 100),
    'curvature_term_budget_equals_1_over_10': Q(80, 7) * 3 * Q(6, 5) * Q(7, 2880) == Q(1, 10),
    'gain_prefactor_equals_41_over_441': 1 - k**-2 == Q(41, 441),
    'beta_over_kappa_equals_4_over_5': Q(7, 10) / Q(7, 8) == Q(4, 5),
    'gaussian_control_moment_ratio': (Q(21, 32) + Q(123, 256)) / (Q(9, 4) + Q(21, 32)) == Q(97, 248),
    'gaussian_carrier_lower_bound': 7 + 8 * Q(97, 248) == Q(314, 31),
    'gaussian_control_fails_concentration': Q(314, 31) > 9,
}
assert all(checks.values())
gain = (41 / 441) * (1 - (2873 / 2880)**(4 / 5))
record = {
    'date': '2026-10-29', 'prepared_for': 'Edward Baker',
    'llm_assistance': 'substantial', 'model': 'gpt-6-astra', 'effort': 'max',
    'chat': 'Investigation05 chat0030', 'request': 'CTF-B02 R9',
    'scope': 'Exact rational constant checks only; no source or PDE certificate.',
    'exact_checks': checks,
    'exact_gain_formula': '(41/441)*(1-(2873/2880)^(4/5))',
    'floating_illustrations_not_certificates': {
        'compression_window_b0': (8 / 7) * math.log(2880 / 2873),
        'deadline_fraction_saved': gain,
        'deadline_percent_saved': 100 * gain,
        'optimized_first_moment_to_old_half_split_ratio': (7 / 10) * (7 / 4)**(2 / 5),
    },
}
print(json.dumps(record, indent=2, sort_keys=True))
