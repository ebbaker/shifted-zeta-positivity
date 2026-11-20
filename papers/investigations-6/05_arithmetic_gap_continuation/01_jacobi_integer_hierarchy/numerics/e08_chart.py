"""Common bivariate collar and real-root enclosures for AGC-JH-E08.

19 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Requested execution configuration gpt-6.2-sol / ultra. Serving metadata unavailable.
"""

from itertools import zip_longest
from math import factorial

from flint import acb, arb

from e07_chart import (
    BRACKETS, CENTER, COLLAR_OFFSET, EXPANSION_ORDER, RADIUS,
    _derivative_coefficients, _horner, _inherited_count, _point,
)


INNER = 8
BRACKET_STEPS = 32
NEWTON_STEPS = 6


class ChartFailure(ValueError):
    """A failed numerical gate with the enclosures obtained at that stage."""


class Field:
    """Taylor coefficients in powers of s=10000t and w=z-36 and one value tail."""

    def __init__(self, rows, tail):
        self.rows = rows
        self.tail = arb(tail).upper()
        if not (self.tail.is_finite() and self.tail >= 0 and rows
                and all(row and all(c.is_finite() for c in row) for row in rows)):
            raise ChartFailure("nonfinite or empty field model")
        self.jets = [
            [_derivative_coefficients(row, k) for row in rows]
            for k in range(EXPANSION_ORDER + 2)
        ]
        self.value_calls = 0
        self.derivative_calls = 0
        self.arc_calls = 0

    def difference(self, other):
        if len(self.rows) != len(other.rows):
            raise ChartFailure("time degrees differ in the common field models")
        rows = [
            [c - d for c, d in zip_longest(f, y, fillvalue=arb(0))]
            for f, y in zip(self.rows, other.rows)
        ]
        return Field(rows, self.tail + other.tail)

    def _time_jet(self, order, center, time):
        rows = self.jets[order]
        if time.is_zero():
            return _horner(rows[0], center)
        return _horner([_horner(row, center) for row in rows], time)

    def _jet_majorant(self, order, radius, time):
        time_abs = time.abs_upper()
        bounds = [_horner([abs(c) for c in row], radius) for row in self.jets[order]]
        return _horner(bounds, time_abs).abs_upper()

    def arc_range(self, midpoint, chord, majorant, time):
        self.arc_calls += 1
        value = abs(self._time_jet(0, midpoint, time))
        error = majorant * chord ** EXPANSION_ORDER + self.tail
        for k in range(1, EXPANSION_ORDER):
            error += abs(self._time_jet(k, midpoint, time)) * chord ** k
        return (value - error).lower(), (value + error).upper()

    def real_range(self, x, time, derivative=False):
        w = x - CENTER
        if not w.abs_upper() <= RADIUS:
            raise ChartFailure("real value or first derivative requested outside radius nine")
        order = int(derivative)
        if derivative:
            self.derivative_calls += 1
        else:
            self.value_calls += 1
        if w.is_exact():
            return self._time_jet(order, w, time) + arb(0, self.tail)
        # Recenter at a fixed spatial point before interval evaluation.  The
        # derivative polynomial's kth Taylor coefficient is (k+1) times
        # the original polynomial's (k+1)st normalized derivative.
        m, d = w.mid(), w.rad()
        last = order + EXPANSION_ORDER
        error = factorial(last) // factorial(EXPANSION_ORDER)
        error *= self._jet_majorant(last, w.abs_upper(), time) * d ** EXPANSION_ORDER
        terms = [
            self._time_jet(order + k, m, time) * (factorial(order + k) // factorial(k))
            for k in range(EXPANSION_ORDER)
        ]
        return _horner(terms, w - m) + arb(0, (error + self.tail).upper())


def circle_bounds(fields, radius, sectors, time):
    majorants = [f._jet_majorant(EXPANSION_ORDER, radius, time) for f in fields]
    h = arb.pi() / sectors
    chord = (radius * h).upper()
    f_floors, y_floors, numerators, ratios = [], [], [], []
    for j in range(sectors // 2):  # the remaining sectors are conjugates
        theta = (2 * j + 1) * h
        mid = radius * acb(theta.cos(), theta.sin())
        f, y, b = [
            field.arc_range(mid, chord, majorant, time)
            for field, majorant in zip(fields, majorants)
        ]
        f_floors.append(f[0])
        y_floors.append(y[0])
        numerators.append(b[1])
        if y[0] > 0:
            ratios.append((b[1] / y[0]).upper())
    eta = max(ratios) if len(ratios) == sectors // 2 else None
    return min(f_floors), min(y_floors), eta, {
        "radius": _point(radius),
        "sectors_covered": sectors,
        "sectors_evaluated": sectors // 2,
        "F_floor": _point(min(f_floors)),
        "Y_floor": _point(min(y_floors)),
        "B_upper": _point(max(numerators)),
        "local_ratio_upper": _point(eta) if eta is not None else None,
        "F_floor_sector": f_floors.index(min(f_floors)),
        "Y_floor_sector": y_floors.index(min(y_floors)),
        "B_upper_sector": numerators.index(max(numerators)),
        "local_ratio_sector": ratios.index(eta) if eta is not None else None,
    }


def certify_collar(fields, sectors, time, output):
    output["prior_HDC_count"] = _inherited_count()
    bounds = [
        circle_bounds(fields, radius, sectors, time)
        for radius in (RADIUS - COLLAR_OFFSET, RADIUS + COLLAR_OFFSET)
    ]
    output["boundary_checks"] = [boundary[3] for boundary in bounds]
    f_floor = min(boundary[0] for boundary in bounds)
    y_floor = min(boundary[1] for boundary in bounds)
    if not (f_floor > 0 and y_floor > 0):
        raise ChartFailure(
            f"collar floor gate: F >= {f_floor.str(12)}, Y >= {y_floor.str(12)}"
        )
    eta = max(boundary[2] for boundary in bounds)
    if not eta < 1:
        raise ChartFailure(f"strict Rouche ratio gate: eta <= {eta.str(12)}")
    output.update({
        "annulus_F_floor": _point(f_floor), "annulus_Y_floor": _point(y_floor),
        "annulus_eta_upper": _point(eta),
        "root_buffer": 1, "strict_inner_radius": INNER,
        "anchor_and_continuation": (
            "At zero the canonical strip and HDC rectangle bound both disk counts by two. "
            "The two certified real F signs place two distinct zeros inside radius 8. "
            "Whole-boundary F clearance transports this count to each real time, and "
            "strict Rouche transfers each boundary count to Y. Each of F and Y also "
            "has two real bracket sign changes uniformly, strictly inside radius 8. "
            "Reciprocals and B/Y extend the two-circle bounds to the annulus."
        ),
    })
    return eta


def _sign(value):
    return (value > 0) - (value < 0)


def _search_endpoint(field, time, lo, hi, target_sign, seek_lower):
    # For each search retain the last certified outer sign. A rejected
    # trial need not have a determined sign or satisfy any monotonicity.
    for _ in range(BRACKET_STEPS):
        mid = (lo + hi) / 2
        matching = _sign(field.real_range(mid, time)) == target_sign
        if matching == seek_lower:
            lo = mid
        else:
            hi = mid
    return lo if seek_lower else hi


def root_tubes(field, time, observations):
    roots = []
    for initial in BRACKETS:
        lo, hi = map(arb, initial)
        left, right = field.real_range(lo, time), field.real_range(hi, time)
        left_sign, right_sign = _sign(left), _sign(right)
        item = {
            "initial": initial, "initial_signs": [left_sign, right_sign],
            "maximum_refinement_trials": 2 * BRACKET_STEPS + NEWTON_STEPS,
        }
        observations.append(item)
        if not (left_sign and right_sign == -left_sign):
            raise ChartFailure(f"real signs in {initial} unresolved: {left.str(12)}, {right.str(12)}")
        lower = _search_endpoint(field, time, lo, hi, left_sign, seek_lower=True)
        upper = _search_endpoint(field, time, lo, hi, right_sign, seek_lower=False)
        if not lower < upper:
            raise ChartFailure(f"uniform real signs gave inconsistent tube in {initial}")
        item["refined_sign_endpoints"] = [_point(lower), _point(upper)]
        root = lower.union(upper)
        if not (root - CENTER).abs_upper() < INNER:
            raise ChartFailure(f"root buffer lost in {initial}")
        slope = field.real_range(root, time, derivative=True)
        if not _sign(slope):
            raise ChartFailure(f"zero-containing real slope in {initial}: {slope.str(12)}")
        # The existing root in the bracket satisfies the real MVT.
        # Intersecting retains that root for every time in the slab.
        for _ in range(NEWTON_STEPS):
            center = root.mid()
            narrowed = root.intersection(center - field.real_range(center, time) / slope)
            if narrowed.rad() >= root.rad():
                break
            root = narrowed
            slope = field.real_range(root, time, derivative=True)
            if not _sign(slope):
                raise ChartFailure(f"zero-containing refined slope in {initial}: {slope.str(12)}")
        roots.append((root, slope))
    return roots
