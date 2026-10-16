#!/usr/bin/env python3
"""Exact scalar reserves for the effective collective-attraction checkpoint.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This checker evaluates no heat function, zero, phase, or parameter mesh.
Polymath's approximation theorem and the analytic arguments in the associated
note remain proof inputs. Fractions prove the elementary scalar inequalities;
Decimal only serializes rational interval endpoints with directed rounding.
The program writes nothing and emits deterministic JSON to standard output.
"""

from dataclasses import dataclass
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


CHECKS = []


def require(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError("Reversed interval")

    def __add__(self, other):
        if not isinstance(other, Interval):
            other = Interval(F(other), F(other))
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        if not isinstance(other, Interval):
            other = Interval(F(other), F(other))
        return self + (-other)

    def scale(self, value):
        value = F(value)
        ends = (self.lo * value, self.hi * value)
        return Interval(min(ends), max(ends))


def exp_positive(value, terms=120):
    """Positive rational Taylor sum plus a proved geometric upper tail."""
    value = F(value)
    if value < 0 or value >= terms + 2:
        raise ValueError("Unsupported exponential Taylor argument")
    term = F(1)
    total = term
    for k in range(1, terms + 1):
        term *= value / k
        total += term
    next_term = term * value / (terms + 1)
    tail = next_term / (1 - value / (terms + 2))
    return Interval(total, total + tail)


def arctan_positive(value, terms=80):
    """Alternating rational series with its signed first omitted term."""
    value = F(value)
    if not 0 < value < 1:
        raise ValueError("Unsupported arctangent argument")
    total = F(0)
    for k in range(terms):
        total += (-1) ** k * value ** (2 * k + 1) / (2 * k + 1)
    remainder = (-1) ** terms * value ** (2 * terms + 1) / (2 * terms + 1)
    return Interval(min(total, total + remainder), max(total, total + remainder))


def log_near_one(value, terms=160):
    """Log on [1,2], using the positive atanh series and a rational tail."""
    value = F(value)
    if not 1 <= value <= 2:
        raise ValueError("Logarithm argument outside [1,2]")
    z = (value - 1) / (value + 1)
    total = F(0)
    for k in range(terms):
        total += 2 * z ** (2 * k + 1) / (2 * k + 1)
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return Interval(total, total + tail)


LOG_TWO = log_near_one(F(2))


def log_positive(value):
    value = F(value)
    if value <= 0:
        raise ValueError("Nonpositive logarithm argument")
    power = 0
    while value > 2:
        value /= 2
        power += 1
    while value < 1:
        value *= 2
        power -= 1
    return log_near_one(value) + LOG_TWO.scale(power)


def decimal_end(value, rounding, precision=90):
    ctx = Context(prec=precision, rounding=rounding)
    return str(ctx.divide(Decimal(value.numerator), Decimal(value.denominator)))


def outward(interval):
    return {
        "lower": decimal_end(interval.lo, ROUND_FLOOR),
        "upper": decimal_end(interval.hi, ROUND_CEILING),
        "serialization_precision": 90,
    }


def polynomial_add(left, right):
    result = dict(left)
    for monomial, value in right.items():
        result[monomial] = result.get(monomial, F(0)) + value
    return {m: c for m, c in result.items() if c}


def polynomial_scale(poly, value):
    return {m: c * F(value) for m, c in poly.items() if c * F(value)}


def polynomial_multiply(left, right):
    result = {}
    for (a1, w1), c1 in left.items():
        for (a2, w2), c2 in right.items():
            m = (a1 + a2, w1 + w2)
            result[m] = result.get(m, F(0)) + c1 * c2
    return {m: c for m, c in result.items() if c}


def main():
    # Exact universal scalar inputs; no enormous cutoff is constructed.
    x_threshold = 10**16
    h_floor = 9 * 10**15
    radius = F(1, 20)
    t_min, t_max = F(1, 5), F(3, 10)
    y_min, y_max = F(17, 20), F(19, 20)
    ell_floor = F(67, 2)
    pi = arctan_positive(F(1, 5)).scale(16) - arctan_positive(F(1, 239)).scale(4)
    require("Machin_pi_lower_gt_3", pi.lo > 3)
    require("Machin_pi_upper_lt_22_over_7", pi.hi < F(22, 7))
    require("four_pi_upper_lt_13", 4 * pi.hi < 13)
    require("h_floor_below_x_minus_radius", x_threshold - radius > h_floor)
    q_floor = F(h_floor, 13)
    require("q_floor_gt_4e14", q_floor > 4 * 10**14)
    require("exp_ell_floor_lt_4e14", exp_positive(ell_floor).hi < 4 * 10**14)
    require("exp_37_gt_h_floor", exp_positive(37).lo > h_floor)
    require("source_x_domain", h_floor > 200)
    require("source_t_domain", 0 < t_min <= t_max <= F(1, 2))
    require("source_y_domain", 0 < y_min < y_max < 1)
    require("disk_y_bounds", F(9, 10) - radius == y_min and F(9, 10) + radius == y_max)
    require("source_Re_s_positive_part_zero",
            1 - 3 * y_min + 4 * y_max * (1 + y_max) / h_floor**2 < 0)
    require("natural_cutoff_gt_1e7_plus_1", q_floor > (10**7 + 2)**2)
    cutoff_parameter_span = 1 / (40 * pi.lo) + (t_max - t_min) / 16
    require("natural_cutoff_span_lt_1", cutoff_parameter_span < 1)
    rho_upper = (1 / (40 * pi.lo) + t_max / 16) / (2 * q_floor)
    require("log_cutoff_offset_lt_1e_minus_16", rho_upper < F(1, 10**16))
    require("loose_log_cutoff_offset_lt_1_over_100", F(1, 2) / q_floor < F(1, 100))
    require("log_two_lt_7_over_10", LOG_TWO.hi < F(7, 10))
    require("weighted_main_head_function_decreasing", LOG_TWO.lo > F(5, 12))
    require("weighted_main_tail_function_decreasing", 4 * LOG_TWO.lo > F(4, 7))
    require("log_16_lt_3", LOG_TWO.hi * 4 < 3)
    log_ten = log_positive(10)
    require("log_ten_gt_23_over_10", log_ten.lo > F(23, 10))
    require("log_ten_lt_231_over_100", log_ten.hi < F(231, 100))
    require("log_four_pi_lt_3", exp_positive(3).lo > 4 * pi.hi)

    # Main coefficient exponents, polynomial tails, and weighted tails.
    main_head_exponent = F(37, 40) + (ell_floor - 3) / 20
    main_tail_exponent = F(37, 40) + (ell_floor / 2 - F(1, 100)) / 20
    require("main_head_exponent_ge_12_over_5", main_head_exponent > F(12, 5))
    require("main_tail_exponent_ge_7_over_4", main_tail_exponent > F(7, 4))
    require("two_to_minus_12_over_5_lt_19_over_100", F(1, 2**12) < F(19, 100)**5)
    require("two_to_minus_7_over_5_lt_19_over_50", F(1, 2**7) < F(19, 50)**5)
    main_tail = F(19, 100) + F(19, 50) * F(5, 7) + F(1, 6)
    require("main_tail_equals_1319_over_2100", main_tail == F(1319, 2100))
    require("main_integral_above_16_equals_one_sixth", F(4, 3) * F(1, 8) == F(1, 6))
    require("full_source_main_sum_equals_seven_thirds", 1 + 1 / (F(7, 4) - 1) == F(7, 3))
    require("main_tail_lt_two_thirds", main_tail < F(2, 3))
    log_head = F(19, 100) * F(7, 10) + F(19, 50) * (F(1, 2) + F(25, 49))
    require("main_log_head_equals_25327_over_49000", log_head == F(25327, 49000))
    require("main_log_head_lt_13_over_25", log_head < F(13, 25))
    log_tail = F(1, 8) * (F(4, 3) * (4 * LOG_TWO.hi) + F(16, 9))
    require("main_log_tail_lt_13_over_18", log_tail < F(13, 18))
    require("log_weight_envelope_equals_559_over_450", F(13, 25) + F(13, 18) == F(559, 450))
    require("log_weight_lt_5_over_4", F(559, 450) < F(5, 4))
    require("alpha_derivative_bound_2_over_h", F(6, h_floor**2) + F(1, h_floor) < F(2, h_floor))
    require("heat_derivative_factor_lt_1001_over_1000", 1 + t_max / h_floor < F(1001, 1000))
    main_derivative = F(1, 2) * F(1001, 1000) * F(5, 4)
    require("main_derivative_equals_1001_over_1600", main_derivative == F(1001, 1600))
    require("main_derivative_lt_63_over_100", main_derivative < F(63, 100))

    # Reflected leg, its own complete-disk Cauchy estimate, and gamma factors.
    alpha_real_loss = 2 * t_max / h_floor**2
    require("reflected_head_exponent_ge_3_over_2",
            F(1, 40) + (ell_floor - 3) / 20 - alpha_real_loss > F(3, 2))
    require("reflected_tail_exponent_ge_17_over_20",
            F(1, 40) + (ell_floor / 2 - F(1, 100)) / 20 - alpha_real_loss > F(17, 20))
    require("reflected_integral_coefficient_lt_7",
            F(20, 3) * exp_positive(F(3, 2000)).hi < 7)
    require("reflected_integral_coefficient_equals_20_over_3", 1 / (1 - F(17, 20)) == F(20, 3))
    require("gamma_exp_point02_lt_103_over_100", exp_positive(F(1, 50)).hi < F(103, 100))
    require("gamma_geometric_envelope_lt_103_over_100", F(50, 49) < F(103, 100))
    kappa_log_upper = F(16, 100) * 37 / h_floor
    require("kappa_coefficient_reserve",
            t_max * y_max * h_floor / (2 * (h_floor - 6)) < F(16, 100))
    require("log_largest_cutoff_below_log_h",
            (h_floor + 2 * radius) / 12 + t_max / 16 < h_floor**2)
    require("kappa_log_upper_lt_1e_minus_14", kappa_log_upper < F(1, 10**14))
    require("complete_reflection_multiplier_exp_lt_point02",
            F(19, 1000) + rho_upper + kappa_log_upper < F(1, 50))
    require("reflected_head_exponential_lt_1e_minus_6", exp_positive(F(1139, 80)).lo > 10**6)
    require("reflected_tail_exponential_lt_1e_minus_5", exp_positive(F(469, 40)).lo > 10**5)
    reflected_value = F(103, 100) * (F(3, 10**6) + F(7, 10**5))
    require("reflected_value_equals_7519_over_1e8", reflected_value == F(7519, 10**8))
    require("reflected_value_lt_1e_minus_4", reflected_value < F(1, 10**4))
    require("reflected_Cauchy_derivative_lt_1_over_500", reflected_value / radius < F(1, 500))
    require("reflected_direct_derivative_lt_1_over_100", 67 * reflected_value < F(1, 100))
    require("reflected_x_exp_monotonicity_head", ell_floor * F(17, 40) > 1)
    require("reflected_x_exp_monotonicity_tail", ell_floor * F(7, 20) > 1)
    alpha_extra = F(1, 2) * (F(1, 100) + F(11, 7)) + F(3, h_floor)
    require("alpha_modulus_lt_three_fifths_ell",
            alpha_extra < ell_floor / 10)
    require("mprime_modulus_lt_ell", F(3, 5) * (1 + t_max / h_floor) < 1)

    # True-function value error, including the complete cutoff jump.
    require("source_denominator_gt_99_percent_x", F(666, 100) < h_floor / 100)
    require("source_C_denominator_gt_99_percent_x", 12 < h_floor / 100)
    require("negative_cutoff_log_below_positive_log_q", t_max / (16 * q_floor) < ell_floor)
    eab_exponent = (F(6, 1000) * 37**2 + 1) / (F(99, 100) * h_floor)
    require("eAB_exponent_lt_1point1e_minus_15", eab_exponent < F(11, 10**16))
    require("eAB_expm1_lt_1point12e_minus_15",
            eab_exponent / (1 - eab_exponent) < F(112, 10**17))
    require("eAB_weighted_sum_lt_5", F(203, 100) * F(7, 3) < 5)
    require("eAB_total_lt_1e_minus_14", 5 * F(112, 10**17) < F(1, 10**14))
    require("eAB_majorant_derivative_negative",
            F(12, 1000)**2 - 4 * F(6, 1000) < 0)
    ec_correction = F(124, 100) * 4 / 10**7 + F(3 * 37 + 16, 1) / (F(99, 100) * h_floor)
    require("source_C_numerator_pi_reserve", F(3, 2) * pi.hi + F(1044, 100) < 16)
    require("eC_correction_lt_1e_minus_6", ec_correction < F(1, 10**6))
    negative_exponent = F(37, 80) * ell_floor + ell_floor**2 / 80
    require("eC_negative_exponent_equals_9447_over_320", negative_exponent == F(9447, 320))
    require("eC_exponent_reserve_gt_29point5", negative_exponent - ec_correction > F(59, 2))
    require("crossing_exponent_reserve_gt_29point5",
            negative_exponent - rho_upper**2 / 20 > F(59, 2))
    require("eC_and_jump_scalar_exponential_lt_2e_minus_13",
            exp_positive(F(59, 2)).lo > 5 * 10**12)
    require("complete_jump_lt_5e_minus_13", F(203, 100) * F(2, 10**13) < F(5, 10**13))
    full_remainder = F(1, 10**14) + F(2, 10**13) + F(5, 10**13)
    require("full_remainder_lt_1e_minus_12", full_remainder < F(1, 10**12))
    require("remainder_Cauchy_derivative_lt_2e_minus_11", full_remainder / radius < F(2, 10**11))
    require("remainder_errors_below_coarse_1e_minus_4",
            F(2, 10**11) < F(1, 10**4))

    # Normalizer and U'/U reserves.
    require("sqrt_h_floor_gt_1e7", h_floor > 10**14)
    require("log_h_below_sqrt_h_at_endpoint", F(37) < 10**7)
    require("log_sqrt_derivative_order_for_h_ge_floor", h_floor > 4)
    normalizer_loss = F(4, h_floor**2) + F(3, 10 * 10**7)
    require("normalizer_loss_lt_1_over_1000", normalizer_loss < F(1, 1000))
    u_lower = F(1, 3) - F(2, 10**4)
    u_prime_upper = F(63, 100) + F(1, 100) + F(1, 10**4)
    require("U_value_gt_33_over_100", u_lower > F(33, 100))
    require("U_derivative_lt_13_over_20", u_prime_upper < F(13, 20))
    require("U_log_derivative_lt_2", F(13, 20) / F(33, 100) < 2)
    probe_lower = ell_floor / 4 - F(1, 2000) - 2
    require("probe_lower_equals_12749_over_2000", probe_lower == F(12749, 2000))
    require("probe_log_derivative_gt_6", probe_lower > 6)
    require("probe_above_maximal_zero", F(9, 10) > F(1, 5))
    require("probe_comparison_factor_one", (F(9, 10) / F(1, 5))**2 > 5)
    field_lower = F(6) / F(9, 10) - F(2) / (F(81, 100) - F(1, 25))
    require("field_equals_940_over_231", field_lower == F(940, 231))
    require("field_lower_gt_4", field_lower > 4)

    # Universal polynomial identities for the mirror-floor landing formula.
    # A monomial (i,j) is a**i * w**j; all coefficients are exact.
    a_poly, w_poly = {(1, 0): F(1)}, {(0, 1): F(1)}
    a_plus_w = polynomial_add(a_poly, w_poly)
    a_plus_2w = polynomial_add(a_poly, polynomial_scale(w_poly, 2))
    derived_m_numerator = polynomial_add(polynomial_scale(a_plus_2w, F(1, 4)),
                                         polynomial_scale(a_poly, F(1, 4)))
    require("mirror_M_derivative_polynomial_identity",
            derived_m_numerator == polynomial_scale(a_plus_w, F(1, 2)))
    speed_numerator = polynomial_add(polynomial_scale(a_plus_w, 2), polynomial_scale(w_poly, 2))
    require("mirror_speed_numerator_identity", speed_numerator == polynomial_scale(a_plus_2w, 2))
    require("mirror_derivative_reciprocal_speed_identity",
            polynomial_multiply(a_plus_w, speed_numerator)
            == polynomial_multiply(polynomial_scale(a_plus_2w, 2), a_plus_w))
    gain_numerator = polynomial_add(a_plus_2w, polynomial_scale(a_plus_w, -1))
    require("mirror_gain_derivative_polynomial_identity", gain_numerator == w_poly)

    mirror_a, w0, t0 = F(10**32), F(1, 25), F(1, 5)
    mirror_gain = w0**2 / (4 * (mirror_a + 2 * w0))
    require("mirror_gain_exact_closed_form", mirror_gain == F(1, 2500 * 10**32 + 200))
    require("mirror_gain_positive", mirror_gain > 0)
    require("mirror_gain_below_classical_duration", mirror_gain < w0 / 2)
    require("mirror_classical_endpoint_equals_11_over_50", t0 + w0 / 2 == F(11, 50))
    high_speed_poly = {(0, 0): F(2), (0, 1): F(16)}
    high_log_argument_poly = {(0, 0): F(1), (0, 1): F(8)}
    require("high_sector_speed_landing_reciprocal_polynomial_identity",
            polynomial_scale(high_speed_poly, F(8, 16)) == high_log_argument_poly)
    require("high_sector_log_argument_equals_33_over_25", 1 + 8 * w0 == F(33, 25))
    high_duration = log_positive(F(33, 25)).scale(F(1, 16))
    high_landing = high_duration + t0
    require("high_sector_landing_gt_start", high_landing.lo > t0)
    require("high_sector_duration_below_classical", high_duration.hi < w0 / 2)
    require("high_sector_landing_below_end_of_time_window", high_landing.hi < F(3, 10))
    require("high_sector_landing_lt_point218", high_landing.hi < F(109, 500))

    result = {
        "date": "2026-10-09",
        "provenance": "GPT-6 (Codex), inherited configuration; exact serving variant and configured reasoning effort are not exposed and are not inferred.",
        "scope": "Exact scalar reserves, universal landing identities, and one scalar logarithm interval. No heat evaluation, zero search, phase sampling, parameter mesh, or huge-cutoff loop. Imported analytic theorems and the note's analytic inequalities remain proof inputs.",
        "backend": "Python standard-library Fraction rational series; Decimal directed endpoint serialization only. No external arithmetic backend.",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "all_checks_passed": True,
        "assertions": len(CHECKS),
        "checks": CHECKS,
        "parameters": {
            "x_threshold": str(x_threshold),
            "t_interval": ["1/5", "3/10"],
            "probe_height": "9/10",
            "disk_radius": "1/20",
            "disk_imaginary_interval": ["17/20", "19/20"],
            "log_q_lower": "67/2",
            "initial_squared_height": "1/25",
        },
        "scalar_enclosures": {
            "pi": outward(pi),
            "log_two": outward(LOG_TWO),
            "log_33_over_25": outward(log_positive(F(33, 25))),
            "conditional_high_sector_landing": outward(high_landing),
            "conditional_high_sector_gain_over_point22": outward(Interval(F(11, 50), F(11, 50)) - high_landing),
            "mirror_gain_lower": {
                "exact": str(mirror_gain),
                "outward": outward(Interval(mirror_gain, mirror_gain)),
            },
            "conditional_mirror_global_endpoint_upper": {
                "exact": str(F(11, 50) - mirror_gain),
                "outward": outward(Interval(F(11, 50) - mirror_gain, F(11, 50) - mirror_gain)),
            },
        },
        "proved_scalar_bounds": {
            "normalized_value_remainder": "<1e-12",
            "normalized_derivative_remainder": "<2e-11",
            "probe_logarithmic_derivative": ">12749/2000>6",
            "high_sector_exact_attraction": ">=940/231>4",
            "conditional_landing_formula": "1/5 + log(33/25)/16",
            "mirror_gain_formula": "1/(2500*10^32+200)",
        },
        "limits": "The high-sector landing requires that a maximizing nonreal zero remain in the stated sector. The mirror endpoint requires an initial strip of squared width 1/25 at time 1/5. The script proves neither zero-location hypothesis nor any imported heat-flow theorem.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
