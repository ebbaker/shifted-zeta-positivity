"""Count and whole-collar bounds for the frozen AGC-JH-E07 r1 chart.

19 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
The packet requests gpt-6.2-sol / ultra. Serving metadata is unreported.
"""

from hashlib import sha256
from itertools import zip_longest
import json
from math import comb
from pathlib import Path
from time import perf_counter

from flint import acb, arb, ctx


CENTER = 36
RADIUS = 9
COLLAR_OFFSET = arb(1) / 64
BRACKETS = ((28, 29), (42, 43))
EXPANSION_ORDER = 4
HDC_RECORD = Path(
    "papers/investigations-4/12_height_dependent_heat_contours/numerics/"
    "07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json"
)
HDC_HASH = "966540b5221b7b5f6cd4d73672728bee1fc26045efdb69c38bde4e9a813239dc"


class ChartFailure(ValueError):
    """A chart gate failed, with a record of all completed checks."""

    def __init__(self, message, metadata):
        super().__init__(message)
        self.metadata = metadata


def _point(value):
    return {"exact": str(value.fmpq()), "display": str(value)}


def _ball(value):
    return {
        "lower": str(value.lower().fmpq()),
        "upper": str(value.upper().fmpq()),
        "display": str(value),
    }


def _inherited_count():
    record_path = Path(__file__).resolve().parents[5] / HDC_RECORD
    record_bytes = record_path.read_bytes()
    digest = sha256(record_bytes).hexdigest()
    if digest != HDC_HASH:
        raise ValueError(f"HDC count record SHA-256 mismatch: {digest}")
    record = json.loads(record_bytes)
    box = {
        "x": ["26", "46"], "y": ["-2", "2"],
        "Re_tau": ["-1/10000", "1/10000"], "Im_tau": ["-1/10000", "1/10000"],
    }
    if (record["status"] != "PASS" or record["complete_zero_count_uniform_D"] != 2
            or record["anchor_tau"] != "0" or record["physical_box"] != box):
        raise ValueError("HDC count or geometry does not match the frozen chart")
    return {"path": str(HDC_RECORD), "sha256": digest, "count": 2, "physical_box": box}


def _horner(coefficients, w):
    value = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        value = value * w + coefficient
    return value


def _bracket_signs(coefficients, error):
    samples = []
    for lo, hi in BRACKETS:
        left = _horner(coefficients, arb(lo - CENTER)) + arb(0, error)
        right = _horner(coefficients, arb(hi - CENTER)) + arb(0, error)
        opposite = (left > 0 and right < 0) or (left < 0 and right > 0)
        samples.append({"x": [lo, hi], "values": [_ball(left), _ball(right)], "opposite": opposite})
    return samples


def _derivative_coefficients(coefficients, order):
    return [coefficients[k] * comb(k, order) for k in range(order, len(coefficients))] or [arb(0)]


def _range_terms(coefficients, radius):
    # Each derivative polynomial here represents p^(k)/k!.
    derivatives = [_derivative_coefficients(coefficients, k) for k in range(EXPANSION_ORDER)]
    majorant = _horner([abs(c) for c in _derivative_coefficients(coefficients, EXPANSION_ORDER)], radius)
    return derivatives, majorant.upper()


def _arc_modulus(terms, midpoint, displacement, error):
    derivatives, majorant = terms
    value = abs(_horner(derivatives[0], midpoint))
    variation = majorant * displacement ** EXPANSION_ORDER + error
    for k, coefficients in enumerate(derivatives[1:], start=1):
        variation += abs(_horner(coefficients, midpoint)) * displacement ** k
    return (value - variation).lower(), (value + variation).upper()


def _circle_bounds(f, y, difference, ef, ey, radius, sectors):
    source_terms = _range_terms(f, radius)
    head_terms = _range_terms(y, radius)
    difference_terms = _range_terms(difference, radius)
    h = ((2 * arb.pi()) / sectors) / 2
    # Chord distance on a sector is at most its midpoint arc length rho*h.
    # The chord also stays in the disk used for the fourth derivative bound.
    displacement = (radius * h).upper()
    error_sum = (ef + ey).upper()
    f_floors, y_floors, numerator_uppers, ratios = [], [], [], []
    for j in range(sectors // 2):
        theta = (2 * j + 1) * h
        midpoint = radius * acb(theta.cos(), theta.sin())
        flo, _ = _arc_modulus(source_terms, midpoint, displacement, ef)
        ylo, _ = _arc_modulus(head_terms, midpoint, displacement, ey)
        _, numerator = _arc_modulus(difference_terms, midpoint, displacement, error_sum)
        f_floors.append(flo)
        y_floors.append(ylo)
        numerator_uppers.append(numerator)
        if ylo > 0:
            ratios.append((numerator / ylo).upper())

    f_floor = min(f_floors)
    y_floor = min(y_floors)
    numerator = max(numerator_uppers)
    ratio = max(ratios) if len(ratios) == sectors // 2 else None
    return f_floor, y_floor, ratio, {
        "radius": _point(radius),
        "sectors_evaluated": sectors // 2,
        "sectors_covered": sectors,
        "source_modulus_lower": _point(f_floor),
        "source_floor_sector": f_floors.index(f_floor),
        "head_modulus_lower": _point(y_floor),
        "head_floor_sector": y_floors.index(y_floor),
        "numerator_modulus_upper": _point(numerator),
        "numerator_upper_sector": numerator_uppers.index(numerator),
        "local_ratio_upper": _point(ratio) if ratio is not None else None,
        "local_ratio_sector": ratios.index(ratio) if ratio is not None else None,
    }


def certify_chart(f, y, ef, ey, sectors):
    """Return the collar ratio upper bound and a JSON-serializable chart ledger.

    The polynomials are ascending real coefficient balls centered at 36.
    Errors are complex-modulus bounds on the disk of radius 10. Inputs
    may also supply (value, derivative) pairs, with only values used here.
    """
    if ctx.prec not in (768, 1280) or sectors < 2 or sectors % 2:
        raise ValueError("chart precision or sector parity outside the frozen packet")
    if sectors > (512 if ctx.prec == 768 else 4096):
        raise ValueError("sector count outside the frozen precision level")
    ef = arb(ef[0] if isinstance(ef, (tuple, list)) else ef).upper()
    ey = arb(ey[0] if isinstance(ey, (tuple, list)) else ey).upper()
    if not (ef.is_finite() and ey.is_finite() and ef >= 0 and ey >= 0):
        raise ValueError("expected finite nonnegative value tails")
    if not (f and y and all(c.is_finite() for c in (*f, *y))):
        raise ValueError("expected nonempty finite coefficient enclosures")

    start = perf_counter()
    count = _inherited_count()
    f_signs = _bracket_signs(f, ef)
    y_signs = _bracket_signs(y, ey)
    source_brackets = all(item["opposite"] for item in f_signs)
    head_brackets = all(item["opposite"] for item in y_signs)
    difference = [a - b for a, b in zip_longest(f, y, fillvalue=arb(0))]
    boundaries = [
        _circle_bounds(f, y, difference, ef, ey, radius, sectors)
        for radius in (RADIUS - COLLAR_OFFSET, RADIUS + COLLAR_OFFSET)
    ]
    f_floor = min(boundary[0] for boundary in boundaries)
    y_floor = min(boundary[1] for boundary in boundaries)
    ratio = max(boundary[2] for boundary in boundaries) if y_floor > 0 else None
    # HDC Note13's count-two rectangle contains the real projection of
    # both disks. The strip excludes its complement above and below.
    # Opposite signs locate the two source roots strictly inside radius 8.
    # Rouché transfers both disk counts using the separate arc ratios.
    transferred = source_brackets and ratio is not None and ratio < 1
    annulus = transferred and f_floor > 0 and y_floor > 0
    metadata = {
        "count_source": count,
        "source_strip_half_width_at_time_zero": 1,
        "center": CENTER,
        "integration_radius": RADIUS,
        "root_buffer": 1,
        "source_count_two": source_brackets,
        "head_count_two": transferred,
        "common_root_buffer_certified": transferred and head_brackets,
        "source_brackets": f_signs,
        "head_brackets": y_signs,
        "source_value_tail_upper": _point(ef),
        "head_value_tail_upper": _point(ey),
        "annulus_boundary_checks": [boundary[3] for boundary in boundaries],
        "annulus_source_floor_lower": _point(f_floor) if annulus else None,
        "annulus_head_floor_lower": _point(y_floor) if annulus else None,
        "annulus_relative_error_upper": _point(ratio) if annulus else None,
        "annulus_certified": annulus,
        "arc_expansion_order": EXPANSION_ORDER,
        "centered_polynomial_horner_evaluations": sectors * 3 * EXPANSION_ORDER,
        "real_endpoint_horner_evaluations": 2 * 2 * len(BRACKETS),
        "seconds": perf_counter() - start,
    }
    # If both circles have the same counts, there are no zeros between
    # them. Maximum modulus for q and each reciprocal extends the
    # boundary estimates to the closed annulus.
    if not (source_brackets and head_brackets):
        raise ChartFailure("source or head real sign brackets were not certified", metadata)
    if not (f_floor > 0 and y_floor > 0):
        raise ChartFailure("a whole-boundary floor was not certified", metadata)
    if not transferred:
        raise ChartFailure("the whole-boundary relative error failed strict Rouché transfer", metadata)
    return ratio, metadata
