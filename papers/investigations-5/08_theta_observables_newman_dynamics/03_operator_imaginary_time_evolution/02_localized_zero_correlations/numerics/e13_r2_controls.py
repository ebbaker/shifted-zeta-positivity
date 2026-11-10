"""One source-free synthetic control batch for the E13 r2 endpoint evaluator.

9 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance. The assisting model and effort are unavailable.
"""

from collections import Counter
from fractions import Fraction as F

from flint import arb, ctx, fmpq


def _real(value):
    return arb(fmpq(value.numerator, value.denominator))


def _exact(value):
    mantissa, exponent = value.man_exp()
    return F(int(mantissa)) * F(2) ** int(exponent)


def _edges(lower, upper):
    return _exact(lower.lower()), _exact(upper.upper())


def _contains(interval, reference):
    return interval[0] <= reference[0] <= reference[1] <= interval[1]


def _point_cell(point, count=1):
    x, y = point
    return x, x, y, y, count


def _point_scale(meter):
    meter("pi")
    pi = arb.pi()
    meter("sqrt")
    return (2 * pi).sqrt() * 32 / (51 * 2000)


def _point_kernel(left, right, scale, meter):
    """Direct ordered point formula, with a single combined rational exponent."""
    x, y = left
    xp, yp = right
    center = (x + xp) / 2
    exponent = -F(25, 36) * (x - xp) ** 2
    exponent -= F(8, 17) * ((y - F(1, 2)) ** 2 + (yp + F(1, 2)) ** 2)
    meter("erf")
    right_edge = _real(2000 - center).erf()
    meter("erf")
    left_edge = _real(1000 - center).erf()
    meter("exp")
    return scale * (right_edge - left_edge) * _real(exponent).exp()


def _ordered_sum(points, scale, meter):
    total = arb(0)
    for i, left in enumerate(points):
        for j, right in enumerate(points):
            if i != j:
                total += _point_kernel(left, right, scale, meter)
    return total


def run_controls(evaluator, meter):
    """Run Request29's software controls before the canonical pair pass."""
    results, calls = {}, Counter()

    def require(condition, message):
        if not condition:
            raise evaluator.GateError("control_failed", message)

    def metered(name):
        if name in {"exp", "erf"} and calls["exp"] + calls["erf"] >= 10000:
            raise evaluator.GateError("control_call_cap", "10,000 exp/erf calls")
        meter(name)
        calls[name] += 1

    def record(name, result):
        require(name not in results and len(results) < 24, "synthetic fixture budget")
        results[name] = result

    def interval(cells, **mutations):
        with ctx.workprec(128):
            lo, hi = evaluator.range_sum(cells, metered, **mutations)
            require(lo.is_finite() and hi.is_finite(), "nonfinite control range")
            return _edges(lo, hi)

    with ctx.workprec(256):
        scale256 = _point_scale(metered)

    def reference(points):
        with ctx.workprec(256):
            point_sum = _ordered_sum(points, scale256, metered)
            require(point_sum.is_finite(), "nonfinite direct point reference")
            return _edges(point_sum, point_sum)

    def compare(name, bounds, points):
        expected = reference(points)
        require(_contains(bounds, expected), name + ": direct point ball not contained")
        record(name, "contained the 256-bit ordered point ball")
        return expected

    p = (F(1500), F(0))
    q = (F(1500), F(1, 8))
    require(interval([]) == (0, 0), "empty factorial sum")
    record("empty", "exact zero")
    require(interval([_point_cell(q)]) == (0, 0), "singleton factorial sum")
    record("singleton", "exact zero")
    real_double = [_point_cell(p, 2)]
    double_ref = compare("double_real_point", interval(real_double), (p, p))
    compare("double_nonreal_point", interval([_point_cell(q, 2)]), (q, q))

    real_cell = (F(1499), F(1501), F(1, 8), F(1, 8), 2)
    compare("same_cell_real_split", interval([real_cell]),
            ((F(2999, 2), q[1]), (F(3001, 2), q[1])))
    imag_cell = (F(1500), F(1500), F(-1, 4), F(3, 8), 2)
    compare("same_cell_imaginary_split", interval([imag_cell]),
            ((q[0], F(-1, 8)), (q[0], F(1, 4))))

    with ctx.workprec(128):
        scale128 = _point_scale(metered)
    edge_pairs = {}
    for edge, label in ((1000, "left_edge"), (2000, "right_edge")):
        left = (F(edge) - F(1, 8), F(1, 4))
        right = (F(edge) + F(1, 8), F(-1, 8))
        cells = [_point_cell(left), _point_cell(right)]
        edge_pairs[label] = cells, compare(label, interval(cells), (left, right))
        with ctx.workprec(128):
            forward = _point_kernel(left, right, scale128, metered)
            reverse = _point_kernel(right, left, scale128, metered)
            require(reverse > 0, label + ": positive denominator for mark-order ratio")
            measured = forward / reverse
            measured_edges = _edges(measured, measured)
        with ctx.workprec(256):
            metered("exp")
            ratio = _real(F(16, 17) * (left[1] - right[1])).exp()
            expected = _edges(ratio, ratio)
        require(_contains(measured_edges, expected), label + ": order ratio")
        record(label + "_order_ratio", "contained exp((16/17)(y-y'))")

    wide_cells = [
        (F(1000), F(1000) + F(1, 8), F(-1, 4), F(1, 8), 1),
        (F(1000) + F(1, 2), F(1000) + F(3, 4), F(0), F(1, 4), 1),
    ]
    wide_bounds = interval(wide_cells)
    corners = [[(x, y) for x in (a, b) for y in (c, d)] for a, b, c, d, _ in wide_cells]
    for index, points in enumerate(zip(corners[0], reversed(corners[1]))):
        compare(f"width_corner_{index}", wide_bounds, points)
    compare("width_interior", wide_bounds,
            tuple(((a + b) / 2, (c + d) / 2) for a, b, c, d, _ in wide_cells))

    cells, edge_ref = edge_pairs["left_edge"]
    require(interval(cells, drop_order=True)[1] < edge_ref[0], "missing order injection")
    record("missing_order", "mutated range disjoint from direct point ball")
    require(interval(real_double, drop_self=True)[1] < double_ref[0], "missing self injection")
    record("missing_self", "mutated range disjoint from direct point ball")

    def reject(name, gate, action):
        try:
            action()
        except evaluator.GateError as error:
            require(error.gate == gate, name + ": incorrect failed gate")
        else:
            raise evaluator.GateError("control_failed", name + ": injected input accepted")
        record(name, "rejected at " + gate)

    reject("excess_endpoint_radius", "endpoint_arithmetic_radius",
           lambda: evaluator.finalize(arb(1, arb((1, -9))), arb(1)))
    reject("final_radius_equality", "final_radius",
           lambda: evaluator.check_final_radius(F(0), F(1, 100)))
    reject("nonfinite_endpoint", "nonfinite_endpoint",
           lambda: evaluator.finalize(arb("nan"), arb(1)))
    return {"fixtures": len(results), "results": results, "calls": dict(calls),
            "range_precision_bits": 128, "reference_precision_bits": 256}
