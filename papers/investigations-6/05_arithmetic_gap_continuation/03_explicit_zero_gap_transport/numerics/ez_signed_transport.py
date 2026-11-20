"""Outward interval core for the E03 signed velocity difference.

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance,
gpt-6.2-sol/ultra. The caller supplies the validation and reporting driver.
"""

from hashlib import sha256
import importlib.util
from math import comb, factorial
from pathlib import Path

from flint import arb, ctx


OPENING_SHA256 = "3022c6f9257cd3796aaf5b856e77e43f9472b0462aa4c112dd777bcf8997d89f"
PRECISION_BITS = 224
SPATIAL_CAP = 4
ANCHOR_TIME = 1000
MOMENT_DEGREE = 28
TILTED_DEGREE = 11


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def center():
    return arb(671) / 500


def load_anchor():
    """Acquire exactly the 28 positive-degree moments and two pinned brackets."""
    ctx.prec = PRECISION_BITS
    path = Path(__file__).with_name("certify_backward_gap.py")
    require(sha256(path.read_bytes()).hexdigest() == OPENING_SHA256,
            "changed opening driver")
    spec = importlib.util.spec_from_file_location("ez_opening_pinned", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # The opening loader checks both the founding integrator and its receipt.
    source, anchors = module.anchor_inputs()
    b = center()
    moments = [arb(1)] + [
        source.expect(lambda u: (u - b)**degree)
        for degree in range(1, MOMENT_DEGREE + 1)
    ]
    require(moments[MOMENT_DEGREE] > 0, "positive anchor absolute moment")
    return moments, anchors


def tilted_moments(moments, s):
    """Normalized moments on the supplied interval of nonnegative physical s.

    The moment of P**p uses the exponential Taylor series through 27-p.
    The Cauchy allowance at radius r is exp(s*(b**2+r**2)) E[P**28]/r**(28-p).
    The minimum of the radius-one and radius-three bounds is valid.
    """
    if s == 0:
        return moments[:TILTED_DEGREE + 1]
    b = center()
    linear = -2 * b * s
    quadratic_derivative = -2 * s
    coefficients = [arb(1), linear]
    for degree in range(2, MOMENT_DEGREE):
        coefficients.append(
            (linear * coefficients[-1] + quadratic_derivative * coefficients[-2])
            / degree
        )
    scale_one = ((b * b + 1) * s.upper()).exp() * moments[MOMENT_DEGREE]
    scale_three = ((b * b + 9) * s.upper()).exp() * moments[MOMENT_DEGREE]
    unnormalized = []
    for p in range(TILTED_DEGREE + 1):
        remainder_order = MOMENT_DEGREE - p
        polynomial = sum(coefficients[n] * moments[p + n] for n in range(remainder_order))
        remainder = min(scale_one.upper(), (scale_three / 3**remainder_order).upper())
        unnormalized.append(polynomial + arb(0, remainder))
    mass = unnormalized[0]
    require(mass > 0, "positive tilted mass")
    return [arb(1)] + [value / mass for value in unnormalized[1:]]


def counted_roots(d, b, q1, q2, cap, w):
    """Enclose both labelled roots and the margins of their common chart."""
    mean = b + d[1]
    variance = d[2] - d[1]**2
    require(mean > 0 and variance > 0, "positive mean and variance")
    current_floor = (1 - cap**2 * w / 2).lower()
    require(current_floor > 0, "positive current throughout the spatial chart")
    disk_radius = (cap**2 * variance / 2).upper()
    require(disk_radius < 1, "centered characteristic disk avoids zero")
    phase_error = disk_radius.asin().upper()
    reach = (cap * mean - phase_error - q2).lower()
    require(reach > 0, "phase counts the first two positive levels")
    x1 = (q1 + arb(0, phase_error)) / mean
    x2 = (q2 + arb(0, phase_error)) / mean
    gap = x2 - x1
    require(x1 > 0 and x2 < cap and gap > 0, "separated counted root tubes")
    return x1, x2, gap, current_floor, phase_error, reach


def difference_moments(d, b):
    """Even moments of the size-weighted difference on the tilted source."""
    mean = b + d[1]
    require(mean > 0, "positive size-weight normalization")
    values = [arb(1)]
    for p in range(2, 11, 2):
        moment = sum(
            (-1)**i * comb(p, i) * d[i] * (b * d[p - i] + d[p - i + 1])
            for i in range(p + 1)
        ) / mean
        require(moment > 0, f"positive weighted-difference moment of order {p}")
        values.append(moment)
    return values


def bound_cell(d, b, q1, q2, cap):
    _, w, m4, m6, m8, m10 = difference_moments(d, b)
    x1, x2, gap, floor, phase_error, reach = counted_roots(d, b, q1, q2, cap, w)
    j1 = (1 - x1**2 * w / 2).lower().union(arb(1))
    j2 = (1 - x2**2 * w / 2).lower().union(arb(1))
    require(j1 > 0 and j2 > 0, "positive node current denominators")
    kappa4 = m4 - 3 * w**2
    coefficients = [
        kappa4 / 6,
        w * m4 / 24 - m6 / 120,
        m8 / 5040 - w * m6 / 720,
    ]
    terms = [
        coefficient * ((x2**degree / j2 - x1**degree / j1) / gap)
        for degree, coefficient in zip((3, 5, 7), coefficients)
    ]
    remainder_coefficient = m10 / factorial(9) + w * m8 / factorial(8)
    remainder = (
        remainder_coefficient * (x1**9 / j1 + x2**9 / j2) / gap
    ).upper()
    normalized_drift = sum(terms) + arb(0, remainder)
    backward_drift = w - normalized_drift
    require(backward_drift > 0, "strict physical backward gap widening")
    return {
        "roots": (x1, x2),
        "gap": gap,
        "current_floor": floor,
        "centered_phase_error": phase_error,
        "phase_reach_margin": reach,
        "w": w,
        "fourth_cumulant": kappa4,
        "coefficients": coefficients,
        "terms": terms,
        "remainder": remainder,
        "normalized_drift": normalized_drift,
        "backward_drift": backward_drift,
    }


def bounds(values):
    """Outward decimal endpoints of the hull of a collection of balls."""
    return {
        "lower": min(value.lower() for value in values).str(24),
        "upper": max(value.upper() for value in values).str(24),
    }


def endpoint_discriminant(moments, anchors, s, integral_G):
    """Combine an already paid integral from s=0 with the endpoint mean ratio."""
    a_start = center() + moments[1]
    a_end = center() + tilted_moments(moments, s)[1]
    require(a_start > 0 and a_end > 0, "positive endpoint means")
    a_ratio = a_start / a_end
    anchor_D = ((anchors[1] - anchors[0]) / 2)**2
    require(anchor_D > 0, "positive pinned anchor discriminant")
    D = anchor_D * a_ratio**2 * (-2 * integral_G).exp()
    require(D > 0, "positive transported end discriminant")
    return D, a_ratio, a_end, anchor_D


def run_transport(moments, anchors, first_cell, end_cell, cells_per_unit):
    """Return (summary, D_at_end, records, integral_G) for the specified cells.

    Cell indices are half-open. Each numerical enclosure covers its closed cell.
    Each record is (s, x1, x2, d), with d the normalized tilted moments.
    D_at_end is returned only for first_cell=0. To join runs, sum integral_G
    over adjoining cell ranges and call endpoint_discriminant.
    """
    require(ctx.prec >= PRECISION_BITS, "anchor/transport working precision")
    require(len(moments) == MOMENT_DEGREE + 1 and len(anchors) == 2, "anchor input shape")
    require(moments[0] == 1 and moments[MOMENT_DEGREE] > 0, "anchor input normalization")
    require(0 <= first_cell < end_cell and cells_per_unit > 0, "nonempty cell range")
    require(0 < anchors[0] < anchors[1] < SPATIAL_CAP, "ordered pinned anchor brackets")
    step = arb(1) / cells_per_unit
    b = center()
    q1 = arb.pi() / 2
    q2 = 3 * q1
    checked, records = [], []
    for cell in range(first_cell, end_cell):
        s = (cell * step).union((cell + 1) * step)
        d = tilted_moments(moments, s)
        try:
            result = bound_cell(d, b, q1, q2, SPATIAL_CAP)
        except ArithmeticError as error:
            raise ArithmeticError(f"time cell {cell}/{cells_per_unit}: {error}") from error
        checked.append(result)
        records.append((s, *result["roots"], d))
    if first_cell == 0:
        require(all(tube.contains(anchor) for tube, anchor in zip(checked[0]["roots"], anchors)),
                "counted root tubes agree with the anchor indices")

    integral_G = step * sum(row["normalized_drift"] for row in checked)
    normalized_sign = "unresolved"
    if all(row["normalized_drift"] > 0 for row in checked):
        normalized_sign = "positive"
    if all(row["normalized_drift"] < 0 for row in checked):
        normalized_sign = "negative"
    summary = {
        "cell_indices": [first_cell, end_cell],
        "cells_per_unit": cells_per_unit,
        "physical_time": [
            (ANCHOR_TIME - end_cell * step).str(24),
            (ANCHOR_TIME - first_cell * step).str(24),
        ],
        "spatial_cap": SPATIAL_CAP,
        "precision_bits": ctx.prec,
        "current_floor_min": min(row["current_floor"] for row in checked).str(24),
        "phase_reach_margin_min": min(row["phase_reach_margin"] for row in checked).str(24),
        "centered_phase_error_max": max(row["centered_phase_error"] for row in checked).str(24),
        "root_tubes": [bounds([row["roots"][k] for row in checked]) for k in range(2)],
        "spatial_gap_lower_min": min(row["gap"].lower() for row in checked).str(24),
        "w": bounds([row["w"] for row in checked]),
        "fourth_cumulant": bounds([row["fourth_cumulant"] for row in checked]),
        "normalized_log_gap_drift": bounds([row["normalized_drift"] for row in checked]),
        "normalized_log_gap_drift_sign": normalized_sign,
        "physical_backward_log_gap_drift": bounds([row["backward_drift"] for row in checked]),
        "integrated_normalized_drift": bounds([integral_G]),
        "integrated_spatial_remainder_upper": (
            step * sum(row["remainder"] for row in checked)
        ).upper().str(24),
        "velocity_terms": {
            f"x^{degree}": {
                "coefficient": bounds([row["coefficients"][i] for row in checked]),
                "integrated_divided_difference_term": bounds([
                    step * sum(row["terms"][i] for row in checked)
                ]),
            }
            for i, degree in enumerate((3, 5, 7))
        },
    }
    D = None
    if first_cell == 0:
        D, a_ratio, a_end, anchor_D = endpoint_discriminant(
            moments, anchors, end_cell * step, integral_G
        )
        summary.update({
            "anchor_D": bounds([anchor_D]),
            "anchor_D_width_upper": (2 * anchor_D.rad()).upper().str(24),
            "endpoint_mean": bounds([a_end]),
            "endpoint_mean_ratio": bounds([a_ratio]),
            "endpoint_mean_ratio_width_upper": (2 * a_ratio.rad()).upper().str(24),
            "endpoint_D": bounds([D]),
            "endpoint_D_width_upper": (2 * D.rad()).upper().str(24),
            "whole_path_D_lower": anchor_D.lower().str(24),
        })
    return summary, D, records, integral_G
