#!/usr/bin/env python3
"""Exact checks for the selector-preserving conductor and upper-band notes.

Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.
These checks do not validate imported analytic theorems or prove the
remaining mixed estimate. The application wedge has a separate checker,
check_selector_energy.py.
"""
from fractions import Fraction as F
from itertools import product
import json


def rec(value):
    return {"exact": str(value), "decimal": float(value)}


# Sparse polynomials in (delta, r, m): equality means coefficient equality,
# rather than agreement on a finite parameter grid.
def constant(value):
    return {(0, 0, 0): F(value)} if value else {}


def add(*polys):
    result = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            result[powers] = result.get(powers, F(0)) + coefficient
    return {powers: coefficient for powers, coefficient in result.items()
            if coefficient}


def scale(value, poly):
    return {powers: F(value)*coefficient for powers, coefficient in poly.items()
            if value*coefficient}


def multiply(*polys):
    result = constant(1)
    for poly in polys:
        next_result = {}
        for powers, coefficient in result.items():
            for other, other_coefficient in poly.items():
                new_powers = tuple(a+b for a, b in zip(powers, other))
                next_result[new_powers] = (
                    next_result.get(new_powers, F(0))
                    + coefficient*other_coefficient)
        result = {powers: coefficient
                  for powers, coefficient in next_result.items() if coefficient}
    return result


delta_poly, r_poly, m_poly = (
    {(1, 0, 0): F(1)}, {(0, 1, 0): F(1)}, {(0, 0, 1): F(1)})
eta, gamma = F(1, 5000), F(1, 6250)
threshold_loss = F(9, 12500)
assert threshold_loss == 2*(eta+gamma)
K = add(constant(1-eta), multiply(delta_poly, m_poly))
R0 = add(constant(F(9, 8)), scale(-F(23, 20), delta_poly))
v_plain = add(scale(2, multiply(delta_poly, m_poly)),
              constant(-threshold_loss))
v_total = add(scale(2, multiply(delta_poly,
                              add(m_poly, constant(F(23, 20))))),
              constant(-F(1, 4)-threshold_loss))
assert add(constant(1), scale(F(1, 2), v_plain)) == add(K, constant(-gamma))
assert add(R0, scale(F(1, 2), v_total)) == add(K, constant(-gamma))

delta_range = (F(9, 25), F(21, 50))
r_range = (F(7, 10), F(37, 50))
m_range = (F(9, 25), F(1, 2))
plain_corners, total_corners = [], []
for delta, m in product(delta_range, m_range):
    plain_corners.append(2*delta*m-threshold_loss)
    total_corners.append(2*delta*(m+F(23, 20))-F(1, 4)-threshold_loss)
# Both partial derivatives of each cutoff are positive on the rectangle:
# plain: 2m and 2delta; total: 2(m+23/20) and 2delta.
assert min(delta_range) > 0 and min(m_range) > 0
assert (min(plain_corners), max(plain_corners)) == (
    F(3231, 12500), F(5241, 12500))
assert (min(total_corners), max(total_corners)) == (
    F(2614, 3125), F(14191, 12500))
assert min(total_corners)-F(4, 5) == F(114, 3125)

# The fixed-subset fourth-moment capacity and its upper-band cost.
c_m = scale(F(2, 9), add(constant(1), scale(-2, m_poly)))
inverse_capacity = scale(F(1, 2), add(constant(1), scale(-1, r_poly)))
assert add(scale(2, m_poly), scale(F(9, 2), c_m)) == constant(1)
bracket = add(m_poly, scale(-F(1, 2), r_poly),
              scale(-F(1, 2), add(inverse_capacity, scale(-1, c_m))))
simple_bracket = add(scale(F(7, 9), m_poly), scale(-F(1, 4), r_poly),
                     constant(-F(5, 36)))
assert bracket == simple_bracket
capacity_gap_min = (1-r_range[1])/2-F(2, 9)*(1-2*m_range[0])
assert capacity_gap_min == F(61, 900) > 0
upper_m_min = F(21, 50)
bracket_min = F(7, 9)*upper_m_min-r_range[1]/4-F(5, 36)
assert bracket_min == F(1, 360) > 0
# The positive bracket increases in m and decreases in r. Multiplication
# by positive delta therefore has its continuous minimum at these corners.
ideal_saving_min = delta_range[0]*bracket_min
assert ideal_saving_min == F(1, 1000)
selection_loss_max = delta_range[1]*F(1, 1000)/2
assert selection_loss_max == F(21, 100000)
upper_band_margin = ideal_saving_min-selection_loss_max-eta
assert upper_band_margin == F(59, 100000)
assert min(upper_band_margin, gamma) == gamma
counterexample_saving = F(2, 5)*(F(7, 9)*F(2, 5)-F(18, 25)/4-F(5, 36))
assert counterexample_saving == -F(7, 2250)


# A phase exponent denotes a sixth root of unity; None denotes zero.
# This avoids approximate complex arithmetic entirely.
def local_character(valuation, row_phase, orientation):
    if valuation == 0:
        return 0
    if row_phase is None:
        return None
    return (orientation*valuation*row_phase) % 6


def ratio_left(left, right, row_phase, orientation):
    first = local_character(left, row_phase, orientation)
    second = local_character(right, row_phase, orientation)
    return None if first is None or second is None else (first-second) % 6


def ratio_data(left, right):
    residue = (left-right) % 6
    conductor = residue != 0
    zero_mask = (left > 0 or right > 0) and residue == 0
    return residue, conductor, zero_mask


def ratio_right(left, right, row_phase, orientation):
    residue, _, zero_mask = ratio_data(left, right)
    if zero_mask and row_phase is None:
        return None
    return local_character(residue, row_phase, orientation)


row_states = (None, 0, 1, 2, 3, 4, 5)
valuation_cases = character_identity_checks = 0
for d, dprime, k, kprime, p, pprime in product(
        (0, 1), (0, 1), range(8), range(8), (0, 1), (0, 1)):
    # d is squarefree; a physical prime occurs at most once per side.
    # k retains prime powers, including differences divisible by six.
    valuation_cases += 1
    for left, right in ((k, kprime), (d+k+p, dprime+kprime+pprime)):
        _, conductor, zero_mask = ratio_data(left, right)
        assert not (conductor and zero_mask)
        assert (conductor or zero_mask) == (left > 0 or right > 0)
        for orientation, row_phase in product((-1, 1), row_states):
            assert ratio_left(left, right, row_phase, orientation) == ratio_right(
                left, right, row_phase, orientation)
            character_identity_checks += 1


def product_phase(phases):
    return None if any(phase is None for phase in phases) else sum(phases) % 6


formal_prime_norms = (7, 13, 19)


def describe_ratio(left, right):
    residues = [ratio_data(a, b)[0] for a, b in zip(left, right)]
    conductor_norm = mask_norm = 1
    for norm, a, b in zip(formal_prime_norms, left, right):
        _, conductor, zero_mask = ratio_data(a, b)
        if conductor:
            conductor_norm *= norm
        if zero_mask:
            mask_norm *= norm
    return {"residues_mod_six": residues,
            "primitive_conductor_norm": conductor_norm,
            "remaining_zero_mask_norm": mask_norm}


examples = [
    ("plain ramification cancels in total columns",
     (0, 1, 0), (1, 0, 0), (1, 0, 0), (0, 1, 0)),
    ("plain sixth-power phase cancels but its zeros survive",
     (0, 0, 1), (6, 1, 0), (0, 0, 0), (0, 1, 0)),
    ("inverse factor adds ramification beyond the plain ratio",
     (0, 0, 1), (1, 0, 0), (0, 0, 0), (0, 1, 0)),
]
example_records = []
crt_identity_checks = 0
for label, d, k, dprime, kprime in examples:
    n = tuple(a+b for a, b in zip(d, k))
    nprime = tuple(a+b for a, b in zip(dprime, kprime))
    for left, right in ((k, kprime), (n, nprime)):
        for rows, orientation in product(product(row_states, repeat=3), (-1, 1)):
            lhs = product_phase([ratio_left(a, b, row, orientation)
                                 for a, b, row in zip(left, right, rows)])
            rhs = product_phase([ratio_right(a, b, row, orientation)
                                 for a, b, row in zip(left, right, rows)])
            assert lhs == rhs
            crt_identity_checks += 1
    example_records.append({"case": label,
                            "plain": describe_ratio(k, kprime),
                            "total": describe_ratio(n, nprime)})
assert example_records[0]["plain"]["primitive_conductor_norm"] == 91
assert example_records[0]["total"]["primitive_conductor_norm"] == 1
assert example_records[1]["plain"]["primitive_conductor_norm"] == 1
assert example_records[1]["plain"]["remaining_zero_mask_norm"] == 91
assert example_records[1]["total"]["primitive_conductor_norm"] == 19

result = {
    "status": "exact algebra and finite mask checks; remaining mixed estimate unproved",
    "conductor_cutoffs": {
        "target_saving": rec(eta), "retained_error_margin": rec(gamma),
        "plain": {"formula": "2 delta m - 9/12500",
                  "min": rec(min(plain_corners)), "max": rec(max(plain_corners))},
        "total": {"formula": "2 delta (m+23/20) - 1/4 - 9/12500",
                  "min": rec(min(total_corners)), "max": rec(max(total_corners)),
                  "minimum_increase_over_previous_4_over_5": rec(F(114, 3125))},
        "identities": ["1 + v_plain/2 = K - gamma",
                       "(9/8 - 23 delta/20) + v_total/2 = K - gamma"],
        "continuous_extrema": "all cutoff partial derivatives are positive on the box",
    },
    "upper_plain_band": {
        "m_min": rec(upper_m_min), "selection_loss_allowance_max": rec(F(1, 1000)),
        "capacity_gap_min_on_full_box": rec(capacity_gap_min),
        "ideal_saving_min": rec(ideal_saving_min),
        "selection_exponent_cost_max": rec(selection_loss_max),
        "margin_below_target_on_C_plus": rec(upper_band_margin),
        "margin_after_low_row_conductors_restored": rec(gamma),
        "outside_band_example_ideal_saving": rec(counterexample_saving),
        "qualification": "requires the source physical-coefficient, pointwise-profile and mesh hypotheses",
    },
    "finite_character_checks": {
        "formal_prime_norms": list(formal_prime_norms),
        "local_tuple_valuation_cases": valuation_cases,
        "exact_local_character_identities": character_identity_checks,
        "exact_three_prime_product_identities": crt_identity_checks,
        "conductor_distinction_examples": example_records,
        "scope": "formal good-prime valuations and zero masks, not counts or profile main terms",
    },
    "proof_scope": (
        "Sparse polynomial coefficient identities and monotonicity certify the stated "
        "continuous exponent bounds. Finite phase tests check local formulas only. "
        "Imported analytic estimates are not validated by this computation; "
        "the application wedge is checked separately in check_selector_energy.py."),
}
print(json.dumps(result, indent=2, sort_keys=True))
