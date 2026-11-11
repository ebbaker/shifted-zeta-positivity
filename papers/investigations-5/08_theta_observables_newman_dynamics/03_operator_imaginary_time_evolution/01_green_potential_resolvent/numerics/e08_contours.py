"""Bounded Arb contour certificates and candidate generation for E08 r1.

10 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance. Runtime model provenance is recorded by the pilot owner.

Coordinates are local to the polynomial center. Only validated contours,
never candidate-solver output, certify a root count.
"""

from dataclasses import dataclass
from time import monotonic

from flint import acb, acb_poly, arb


@dataclass
class ContourBudget:
    max_tests: int = 65_536
    max_depth: int = 24
    deadline: float | None = None
    tests: int = 0
    polynomial_evaluations: int = 0
    polynomial_translations: int = 0
    rejections: int = 0
    max_depth_seen: int = 0
    candidate_calls: int = 0
    candidate_iterations: int = 0
    candidate_polynomial_evaluations: int = 0

    def check_time(self):
        if self.deadline is not None and monotonic() >= self.deadline:
            raise TimeoutError("case deadline")


def _exact_polynomial(coeffs):
    coefficients = [acb(c) for c in coeffs]
    if not coefficients or not all(c.is_exact() and c.is_finite() for c in coefficients):
        raise ValueError("contour needs nonempty finite exact dyadic coefficients")
    return acb_poly(coefficients)


def _strictly_nonzero(value):
    return value.is_finite() and value.abs_lower() > 0


def _contour(polynomial, paths, epsilon, budget):
    """Use convex image boxes and endpoint angle increments.

    For an accepted parameter interval, the interval evaluation contains
    its full polynomial image and lies in a convex box disjoint from zero.
    The image arc is homotopic there to its chord. Its lifted argument
    change is the principal argument of the endpoint ratio, since all
    points of a compact convex box avoiding zero lie in an open half-plane
    through zero. Arb encloses the principal argument away from its cut.
    """
    epsilon = arb(epsilon)
    if not epsilon.is_finite() or not epsilon >= 0:
        raise ValueError("contour needs a finite nonnegative error allowance")
    pi = arb.pi()
    total_angle = arb(0)
    lower, upper = None, None
    accepted = 0
    initial_tests = budget.tests
    witness = None

    def result(status, reason=None, count=None, winding=None):
        return {
            "status": status,
            "reason": reason,
            "count": count,
            "lower": lower,
            "upper": upper,
            "winding": winding,
            "epsilon": epsilon,
            "tested": budget.tests - initial_tests,
            "accepted": accepted,
            "witness": witness,
        }

    def evaluate(argument):
        budget.polynomial_evaluations += 1
        return polynomial(argument)

    try:
        for side, path in enumerate(paths):
            stack = [(arb(0), arb(1), 0)]
            endpoints = {}

            def endpoint(parameter):
                key = parameter.man_exp()
                if key not in endpoints:
                    endpoints[key] = evaluate(path(parameter))
                return endpoints[key]

            while stack:
                budget.check_time()
                if budget.tests >= budget.max_tests:
                    return result("inconclusive at cap", "contour test cap")
                left, right, depth = stack.pop()
                budget.tests += 1
                budget.max_depth_seen = max(budget.max_depth_seen, depth)

                whole = evaluate(path(left.union(right)))
                abs_lo, abs_hi = whole.abs_lower(), whole.abs_upper()
                witness = {
                    "side": side,
                    "left": left,
                    "right": right,
                    "depth": depth,
                    "image_modulus_lower": abs_lo,
                    "image_modulus_upper": abs_hi,
                }
                from_value, to_value = endpoint(left), endpoint(right)
                if abs_lo > epsilon and _strictly_nonzero(from_value) and _strictly_nonzero(to_value):
                    ratio = to_value / from_value
                    delta = ratio.arg()
                    if delta.is_finite() and delta > -pi and delta < pi:
                        accepted += 1
                        total_angle += delta
                        lower = abs_lo if lower is None else min(lower, abs_lo)
                        upper = abs_hi if upper is None else max(upper, abs_hi)
                        continue
                    witness["argument_interval"] = delta

                budget.rejections += 1
                # A certified point upper bound can prove failure of the
                # chosen margin inequality. An arc lower bound alone cannot.
                middle = (left + right) / 2
                for parameter, value in (
                    (left, from_value), (right, to_value), (middle, endpoint(middle))
                ):
                    if value.abs_upper() <= epsilon:
                        witness["point"] = parameter
                        witness["point_modulus_upper"] = value.abs_upper()
                        return result("specified gate failure", "point modulus <= error allowance")
                if depth >= budget.max_depth:
                    return result("inconclusive at cap", "contour subdivision depth")
                stack.append((middle, right, depth + 1))
                stack.append((left, middle, depth + 1))
    except TimeoutError:
        return result("inconclusive at cap", "case deadline")

    winding = total_angle / (2 * pi)
    count = winding.unique_fmpz()
    if count is None or count < 0:
        return result("inconclusive at cap", "winding integer not certified", winding=winding)
    if lower is None or not lower > epsilon:
        raise ArithmeticError("internal strict margin check failed")
    witness = None
    return result("certified", count=int(count), winding=winding)


def circle(coeffs, center, radius, epsilon, budget):
    """Certify a positive radius, counterclockwise circle in local coordinates."""
    center, radius = acb(center), arb(radius)
    if not center.is_exact() or not center.is_finite() or not radius.is_exact() or not radius > 0:
        raise ValueError("circle needs an exact center and positive exact radius")
    polynomial = _exact_polynomial(coeffs)
    if not center.is_zero():
        budget.polynomial_translations += 1
        polynomial = polynomial(acb_poly([center, 1]))

    def path(parameter):
        sin, cos = (2 * parameter).sin_cos_pi()
        return acb(radius * cos, radius * sin)

    return _contour(polynomial, [path], epsilon, budget)


def rectangle(coeffs, xlo, xhi, ylo, yhi, epsilon, budget):
    """Certify all four sides in counterclockwise order."""
    xlo, xhi, ylo, yhi = map(arb, (xlo, xhi, ylo, yhi))
    if not all(x.is_finite() and x.is_exact() for x in (xlo, xhi, ylo, yhi)):
        raise ValueError("rectangle corners must be finite and exact")
    if not xlo < xhi or not ylo < yhi:
        raise ValueError("rectangle must have positive width and height")
    vertices = [acb(xlo, ylo), acb(xhi, ylo), acb(xhi, yhi), acb(xlo, yhi)]
    paths = [
        lambda t, start=start, end=end: start + (end - start) * t
        for start, end in zip(vertices, vertices[1:] + vertices[:1])
    ]
    return _contour(_exact_polynomial(coeffs), paths, epsilon, budget)


def _midpoint(value):
    return acb(value.real.mid(), value.imag.mid())


def candidates(coeffs, A=1, *, budget=None):
    """One deterministic local Newton candidate invocation, at most 100 updates.

    Start at the local center and eight points on a fixed half-radius
    coordinate grid. Each path uses the exact dyadic midpoint of a ball
    step. Positions and residuals are heuristics here, not certificates.
    """
    polynomial = _exact_polynomial(coeffs)
    derivative = polynomial.derivative()
    A = arb(A)
    half = A / 2
    target = arb(2) ** -64
    duplicate_radius = arb(2) ** -42
    found = []
    if budget is not None:
        budget.candidate_calls += 1
    seeds = [(0, 0)] + [
        (i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)
    ]
    for i, j in seeds:
        position = _midpoint(acb(i * half, j * half))
        best, best_step = position, None
        for _ in range(20 if (i, j) == (0, 0) else 10):
            if budget is not None:
                budget.check_time()
                budget.candidate_iterations += 1
                budget.candidate_polynomial_evaluations += 2
            value, slope = polynomial(position), derivative(position)
            if not _strictly_nonzero(slope):
                if value.is_zero():
                    best, best_step = position, arb(0)
                break
            step = _midpoint(value / slope)
            if not step.is_finite():
                break
            next_position = _midpoint(position - step)
            if not next_position.is_finite() or not next_position.abs_upper() <= 2 * A:
                break
            size = step.abs_upper()
            if next_position.abs_upper() < A and (best_step is None or size < best_step):
                best, best_step = next_position, size
            position = next_position
            if size <= target:
                break
        if best_step is not None and best_step < arb(2) ** -20:
            if all((best - other).abs_lower() > duplicate_radius for other in found):
                found.append(best)
    return found


def clusters(points, n, s):
    """Yield tentative disjoint disk sets, ordered by the prescribed radii.

    Merge nearby candidate points when their trial disks overlap. The
    caller must check that the small counts sum to n after certification.
    An isolated candidate may represent several unresolved roots.
    """
    if n == 0:
        yield []
        return
    s = arb(s)
    for power in (24, 32, 40):
        radius = arb(2) ** -power
        groups = [[w] for w in points if w.abs_upper() + radius < s]
        while groups:
            centers = [_midpoint(sum(group, acb(0)) / len(group)) for group in groups]
            overlap = next(
                (
                    (i, j)
                    for i, w in enumerate(centers)
                    for j in range(i)
                    if not (w - centers[j]).abs_lower() > 2 * radius
                ),
                None,
            )
            if overlap is None:
                break
            i, j = overlap
            groups[j].extend(groups.pop(i))
        if groups and len(groups) <= n and all(w.abs_upper() + radius < s for w in centers):
            yield [(w, radius) for w in centers]
