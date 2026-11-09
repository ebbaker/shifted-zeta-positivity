"""Certified contour acquisition for the frozen TND-OC-E13 r1 rectangle.

Prepared for Edward Baker with OpenAI Codex assistance, 9 November 2026.
Per-agent backend model and reasoning effort are not independently exposed.
"""
from bisect import bisect_left, bisect_right
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

from flint import acb, acb_series, arb, ctx


PRECISIONS = (128, 256, 512)
RECTANGLE = tuple(map(Fraction, (988, 2012, "-3/2", "3/2")))
SIGMA_MAX = Fraction(1, 2**24)
CUT_FRACTIONS = (Fraction(1, 2), Fraction(3, 8), Fraction(5, 8))
# A proposed cut can pass through a root. Abandon that candidate locally
# before exhausting a run-wide cap. The outer contour has no fallback.
CUT_REFINEMENT_DEPTH = 20
HARD_DEPTH = 96


class GateError(Exception):
    def __init__(self, gate, detail):
        super().__init__(f"{gate}: {detail}")
        self.gate = gate
        self.detail = detail


class CutUnavailable(Exception):
    pass


def dyadic(value):
    """Convert an exact dyadic rational into an Arb point."""
    denominator = value.denominator
    if denominator & (denominator - 1):
        raise ValueError(f"not dyadic: {value}")
    return arb((value.numerator, 1 - denominator.bit_length()))


def midpoint_fraction(ball):
    mantissa, exponent = ball.mid().man_exp()
    return Fraction(int(mantissa)) * Fraction(2) ** int(exponent)


def zeta_source(z, order):
    """Return Z, or the four complex-ball coefficients of Z(z+t)."""
    slope = acb(0, -arb(1) / 2)
    s = acb(arb(1) / 2) + slope * z
    if order == 0:
        return s.zeta()
    if order != 3:
        raise ValueError(f"unsupported canonical series order: {order}")
    values = acb_series([s, slope], prec=4).zeta()
    return tuple(values[k] for k in range(4))


def series_log_derivative(coefficients):
    b0, b1, b2, b3 = coefficients
    if not all(value.is_finite() for value in coefficients) or b0.contains(0):
        return None
    r0 = b1 / b0
    r1 = (2 * b2 - b1 * r0) / b0
    r2 = (3 * b3 - b1 * r1 - b2 * r0) / b0
    return r0, r1, r2


def point(axis, fixed, moving):
    return acb(dyadic(moving), dyadic(fixed)) if axis == 0 else acb(
        dyadic(fixed), dyadic(moving)
    )


def segment_box(axis, fixed, lo, hi):
    moving = arb(dyadic((lo + hi) / 2), dyadic((hi - lo) / 2))
    return acb(moving, dyadic(fixed)) if axis == 0 else acb(dyadic(fixed), moving)


@dataclass(frozen=True, slots=True)
class Fragment:
    lo: Fraction
    hi: Fraction
    image: acb
    angle: arb
    record: int
    subdivision_depth: int


@dataclass(frozen=True, slots=True)
class Edge:
    axis: int
    fixed: Fraction
    parts: tuple
    ends: tuple
    starts: tuple

    @classmethod
    def build(cls, axis, fixed, parts):
        parts = tuple(parts)
        return cls(
            axis, fixed, parts, tuple(p.hi for p in parts), tuple(p.lo for p in parts)
        )


class Contours:
    def __init__(self, source, meter, emit):
        self.source = source
        self.meter = meter
        self.emit = emit
        self.node_id = 0
        self.fragment_id = 0
        self.endpoint = lru_cache(maxsize=131072)(self.endpoint)
        self.precisions = set()

    def set_precision(self, bits):
        ctx.prec = bits
        if bits not in self.precisions:
            self.meter(f"precision_{bits}")
            self.precisions.add(bits)

    def zeta(self, z, order=0):
        self.meter("scalar_calls" if order == 0 else "cubic_calls")
        return self.source(z, order)

    def endpoint(self, x, y, bits):
        # Precision is part of the cache key.
        if bits != ctx.prec:
            raise ValueError("endpoint precision mismatch")
        return self.zeta(acb(dyadic(x), dyadic(y)))

    def angle(self, axis, fixed, lo, hi):
        if axis == 0:
            start = self.endpoint(lo, fixed, ctx.prec)
            end = self.endpoint(hi, fixed, ctx.prec)
        else:
            start = self.endpoint(fixed, lo, ctx.prec)
            end = self.endpoint(fixed, hi, ctx.prec)
        if start.contains(0) or end.contains(0):
            return None
        angle = (end / start).arg()
        pi = arb.pi()
        if angle.is_finite() and -pi < angle < pi:
            return angle
        return None

    def accept_fragment(self, axis, fixed, lo, hi, image, angle, depth, parent=None):
        self.meter("accepted_segments")
        self.fragment_id += 1
        record = self.fragment_id
        self.emit({
            "event": "boundary_segment",
            "id": record,
            "axis": axis,
            "fixed": str(fixed),
            "lo": str(lo),
            "hi": str(hi),
            "zeta_real": str(image.real),
            "zeta_imag": str(image.imag),
            "angle": str(angle),
            "precision": ctx.prec,
            "segment_depth": depth,
            "inherited_image_from": parent,
        })
        return Fragment(lo, hi, image, angle, record, depth)

    def winding_segments(self, axis, fixed, lo, hi, depth_limit, inherited=None):
        """Certify a dyadic segment or refine it, preserving orientation."""
        base_depth = inherited.subdivision_depth if inherited is not None else 0
        depth_limit = min(depth_limit, HARD_DEPTH - base_depth)
        pending = [(lo, hi, 0)]
        while pending:
            lo, hi, depth = pending.pop()
            self.meter("boundary_segment_attempts")
            levels = PRECISIONS if depth >= max(0, depth_limit - 2) else PRECISIONS[:1]
            for bits in levels:
                self.set_precision(bits)
                image = (
                    self.zeta(segment_box(axis, fixed, lo, hi))
                    if inherited is None else inherited.image
                )
                if not image.is_finite() or image.contains(0):
                    continue
                angle = self.angle(axis, fixed, lo, hi)
                if angle is not None:
                    source_record = inherited.record if inherited else None
                    yield self.accept_fragment(
                        axis, fixed, lo, hi, image, angle, base_depth + depth, source_record
                    )
                    break
            else:
                if depth >= depth_limit:
                    raise CutUnavailable({
                        "axis": axis, "fixed": str(fixed), "lo": str(lo), "hi": str(hi),
                        "segment_depth": base_depth + depth,
                        "reason": "no outward zero-free image and branch-safe endpoint ratio",
                    })
                self.meter("boundary_subdivisions")
                mid = (lo + hi) / 2
                pending.extend(((mid, hi, depth + 1), (lo, mid, depth + 1)))

    def new_edge(self, axis, fixed, lo, hi, depth_limit):
        return Edge.build(
            axis, fixed, self.winding_segments(axis, fixed, lo, hi, depth_limit)
        )

    def clip_edge(self, edge, lo, hi):
        start = bisect_right(edge.ends, lo)
        stop = bisect_left(edge.starts, hi)
        parts = []
        for part in edge.parts[start:stop]:
            a, b = max(lo, part.lo), min(hi, part.hi)
            if (a, b) == (part.lo, part.hi):
                parts.append(part)
            else:
                parts.extend(
                    self.winding_segments(edge.axis, edge.fixed, a, b, 8, inherited=part)
                )
        if not parts or parts[0].lo != lo or parts[-1].hi != hi:
            raise GateError("completeness", "inherited fragments do not cover the child edge")
        return Edge.build(edge.axis, edge.fixed, parts)

    def new_node(self, box, depth, parent, fraction):
        if depth > HARD_DEPTH:
            raise GateError("cell_depth_cap", {"depth": depth, "parent": parent})
        self.meter("attempted_nodes")
        self.node_id += 1
        self.emit({
            "event": "cell_attempt", "id": self.node_id, "parent": parent,
            "depth": depth, "cut_fraction": fraction, "box": list(map(str, box)),
        })
        return self.node_id

    def count(self, cell_id, edges):
        # Edges are in bottom, right, top, left order; all fragments increase
        # their moving coordinate. Reverse top and left by negating their sums.
        self.set_precision(PRECISIONS[0])
        angle_sum = arb(0)
        for sign, edge in zip((1, 1, -1, -1), edges):
            for part in edge.parts:
                angle_sum += sign * part.angle
        winding = angle_sum / (2 * arb.pi())
        count = winding.unique_fmpz() if winding.is_finite() else None
        self.emit({
            "event": "cell_winding", "id": cell_id, "winding": str(winding),
            "count": None if count is None else int(count),
            "edges": [[part.record for part in edge.parts] for edge in edges],
        })
        if count is None or int(count) < 0:
            raise CutUnavailable({
                "cell": cell_id, "winding": str(winding),
                "reason": "winding does not enclose one nonnegative integer",
            })
        return int(count)

    def split(self, cell_id, box, edges, count, depth):
        x0, x1, y0, y1 = box
        bottom, right, top, left = edges
        split_x = x1 - x0 >= y1 - y0
        for fraction in CUT_FRACTIONS:
            if split_x:
                cut = x0 + fraction * (x1 - x0)
                low = (x0, cut, y0, y1)
                high = (cut, x1, y0, y1)
            else:
                cut = y0 + fraction * (y1 - y0)
                low = (x0, x1, y0, cut)
                high = (x0, x1, cut, y1)
            low_id = self.new_node(low, depth + 1, cell_id, str(fraction))
            high_id = self.new_node(high, depth + 1, cell_id, str(fraction))
            try:
                if split_x:
                    shared = self.new_edge(1, cut, y0, y1, CUT_REFINEMENT_DEPTH)
                    lo_edges = (self.clip_edge(bottom, x0, cut), shared,
                                self.clip_edge(top, x0, cut), left)
                    hi_edges = (self.clip_edge(bottom, cut, x1), right,
                                self.clip_edge(top, cut, x1), shared)
                else:
                    shared = self.new_edge(0, cut, x0, x1, CUT_REFINEMENT_DEPTH)
                    lo_edges = (bottom, self.clip_edge(right, y0, cut), shared,
                                self.clip_edge(left, y0, cut))
                    hi_edges = (shared, self.clip_edge(right, cut, y1), top,
                                self.clip_edge(left, cut, y1))
                low_count = self.count(low_id, lo_edges)
                high_count = self.count(high_id, hi_edges)
            except CutUnavailable as error:
                self.emit({
                    "event": "candidate_cut_failed", "cell": cell_id,
                    "children": [low_id, high_id], "fraction": str(fraction),
                    "detail": error.args[0],
                })
                continue
            if low_count + high_count != count:
                raise GateError("completeness", {
                    "cell": cell_id, "parent_count": count,
                    "child_counts": [low_count, high_count],
                })
            self.emit({
                "event": "candidate_cut_accepted", "cell": cell_id,
                "children": [low_id, high_id], "fraction": str(fraction),
            })
            return (low_id, low, lo_edges, low_count, depth + 1), (
                high_id, high, hi_edges, high_count, depth + 1
            )
        raise GateError("cut_contour", {
            "cell": cell_id, "box": list(map(str, box)), "depth": depth,
            "reason": "all three declared cut fractions failed within local refinement schedule",
        })

    def moment_piece(self, axis, fixed, lo, hi, sign, center, allowance):
        z = segment_box(axis, fixed, lo, hi)
        log_derivative = series_log_derivative(self.zeta(z, 3))
        if log_derivative is None:
            return None
        _, r1, r2 = log_derivative
        g_second = 2 * ((z - center) * r2 + r1)
        length = dyadic(hi - lo)
        remainder = (length**3 * g_second.abs_upper() / 24).upper()
        if not remainder.is_finite() or not remainder <= allowance:
            return None
        midpoint = point(axis, fixed, (lo + hi) / 2)
        b0, b1, _, _ = self.zeta(midpoint, 3)
        if not b0.is_finite() or b0.contains(0):
            return None
        delta = acb(length) if axis == 0 else acb(0, length)
        midpoint_term = sign * delta * (midpoint - center) * b1 / b0
        pad = arb(0, remainder)
        enclosed = midpoint_term + acb(pad, pad)
        if not enclosed.is_finite():
            return None
        if not (enclosed.real.rad() <= allowance and enclosed.imag.rad() <= allowance):
            return None
        return enclosed, remainder

    def centroid(self, cell_id, box, edges, count):
        x0, x1, y0, y1 = box
        center = acb(dyadic((x0 + x1) / 2), dyadic((y0 + y1) / 2))
        perimeter = 2 * (x1 - x0 + y1 - y0)
        self.set_precision(PRECISIONS[0])
        # Local budget per unit length. For an integral coordinate budget
        # of 3*n*sigma_max, the Euclidean multiplier after division is
        # 3*sqrt(2)/(2*pi) < 1. The full rounded enclosure is tested below.
        rate = 3 * dyadic(SIGMA_MAX) * count / dyadic(perimeter)
        integral = acb(0)
        for sign, edge in zip((1, 1, -1, -1), edges):
            for part in edge.parts:
                pending = [(part.lo, part.hi, 0)]
                while pending:
                    lo, hi, depth = pending.pop()
                    self.meter("moment_segment_attempts")
                    allowance = rate * dyadic(hi - lo)
                    levels = PRECISIONS if depth >= 16 else PRECISIONS[:1]
                    for bits in levels:
                        self.set_precision(bits)
                        result = self.moment_piece(
                            edge.axis, edge.fixed, lo, hi, sign, center, allowance
                        )
                        if result is not None:
                            break
                    else:
                        if part.subdivision_depth + depth >= HARD_DEPTH:
                            raise GateError("moment_segment_depth_cap", {
                                "cell": cell_id, "lo": str(lo), "hi": str(hi),
                                "axis": edge.axis, "fixed": str(edge.fixed),
                                "moment_depth": depth,
                                "segment_depth": part.subdivision_depth + depth,
                            })
                        self.meter("moment_subdivisions")
                        mid = (lo + hi) / 2
                        pending.extend(((mid, hi, depth + 1), (lo, mid, depth + 1)))
                        continue
                    self.meter("accepted_segments")
                    enclosed, remainder = result
                    integral += enclosed
                    self.emit({
                        "event": "moment_segment", "cell": cell_id,
                        "boundary_fragment": part.record, "axis": edge.axis,
                        "fixed": str(edge.fixed), "lo": str(lo), "hi": str(hi),
                        "orientation": sign, "remainder": str(remainder),
                        "real": str(enclosed.real), "imag": str(enclosed.imag),
                        "precision": ctx.prec, "moment_depth": depth,
                        "segment_depth": part.subdivision_depth + depth,
                    })
        average = integral / acb(0, 2 * arb.pi() * count)
        enclosure = center + average
        if not enclosure.is_finite():
            raise GateError("centroid_enclosure", {"cell": cell_id, "reason": "nonfinite enclosure"})
        x = midpoint_fraction(enclosure.real)
        y = midpoint_fraction(enclosure.imag)
        sigma = (enclosure - acb(dyadic(x), dyadic(y))).abs_upper()
        self.emit({
            "event": "centroid", "cell": cell_id, "multiplicity": count,
            "centered_moment_real": str((average * count).real),
            "centered_moment_imag": str((average * count).imag),
            "enclosure_real": str(enclosure.real), "enclosure_imag": str(enclosure.imag),
            "dyadic_x": str(x), "dyadic_y": str(y), "euclidean_error": str(sigma),
        })
        if not sigma.is_finite() or not sigma <= dyadic(SIGMA_MAX):
            raise GateError("centroid_Euclidean_error", {"cell": cell_id, "sigma": str(sigma)})
        return count, x, y, sigma

    def acquire(self):
        box = RECTANGLE
        x0, x1, y0, y1 = box
        root = self.new_node(box, 0, None, None)
        try:
            edges = (
                self.new_edge(0, y0, x0, x1, HARD_DEPTH),
                self.new_edge(1, x1, y0, y1, HARD_DEPTH),
                self.new_edge(0, y1, x0, x1, HARD_DEPTH),
                self.new_edge(1, x0, y0, y1, HARD_DEPTH),
            )
            outer_count = self.count(root, edges)
        except CutUnavailable as error:
            raise GateError("outer_contour", error.args[0]) from error
        self.emit({"event": "outer_count", "count": outer_count})
        if outer_count > 1024:
            raise GateError("outer_count_cap", {"count": outer_count})
        pending = [(root, box, edges, outer_count, 0)]
        occupied = []
        while pending:
            cell_id, cell, edges, count, depth = pending.pop()
            if not count:
                continue
            x0, x1, y0, y1 = cell
            diameter_squared = (x1 - x0)**2 + (y1 - y0)**2
            if diameter_squared <= SIGMA_MAX:
                self.emit({
                    "event": "occupied_leaf", "cell": cell_id, "count": count,
                    "diameter_squared": str(diameter_squared), "depth": depth,
                })
                occupied.append((cell_id, cell, edges, count))
                continue
            children = self.split(cell_id, cell, edges, count, depth)
            pending.extend(reversed(children))
        occupied_count = sum(leaf[3] for leaf in occupied)
        if len(occupied) > 1024 or occupied_count != outer_count:
            raise GateError("leaf_completeness", {
                "count": occupied_count, "outer_count": outer_count, "leaves": len(occupied)
            })
        self.emit({"event": "leaf_completeness", "count": occupied_count, "leaves": len(occupied)})
        leaves = [self.centroid(*leaf) for leaf in occupied]
        self.emit({"event": "centroid_acquisition_complete", "leaves": len(leaves)})
        return outer_count, leaves


def acquire(source, meter, emit):
    """Return the certified full count and (multiplicity, x, y, sigma) leaves."""
    return Contours(source, meter, emit).acquire()


def synthetic_replay():
    """Exercise a rejected cut, nonreal roots and double-root multiplicity."""
    from collections import Counter

    mark = dyadic(Fraction(1, 8))
    roots = ((acb(1123), 1), (acb(1543, mark), 2), (acb(1543, -mark), 2))

    def polynomial(z, order):
        value = acb(1)
        if order:
            z = acb_series([z, 1], prec=4)
        for root, multiplicity in roots:
            value *= (z - root)**multiplicity
        return tuple(value[k] for k in range(4)) if order else value

    counts, events = Counter(), Counter()

    def meter(name):
        counts[name] += 1

    def emit(record):
        events[record["event"]] += 1

    count, leaves = acquire(polynomial, meter, emit)
    assert count == 5 and sorted(n for n, _, _, _ in leaves) == [1, 2, 2]
    matched = set()
    for n, x, y, sigma in leaves:
        center = acb(dyadic(x), dyadic(y))
        candidates = [
            index for index, (root, multiplicity) in enumerate(roots)
            if n == multiplicity and (root - center).abs_upper() <= sigma
        ]
        assert len(candidates) == 1
        matched.update(candidates)
    assert matched == {0, 1, 2} and events["candidate_cut_failed"] > 0
    return {"count": count, "leaf_multiplicities": [n for n, _, _, _ in leaves],
            "work": dict(counts), "events": dict(events)}


if __name__ == "__main__":
    import json
    import sys

    if sys.argv[1:] != ["--self-test"]:
        raise SystemExit("use --self-test for the synthetic contour replay")
    print(json.dumps(synthetic_replay(), sort_keys=True))

