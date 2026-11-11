"""Directed coefficient acquisition for the literal-source E08 r1 pilot.

10 November 2026. Prepared for Edward Baker with OpenAI Codex LLM
assistance. See the execution return for recorded model provenance.
"""

from dataclasses import dataclass
from math import factorial
from time import monotonic

from flint import arb, arb_series, ctx

DEGREE = 64
N_SOURCE = 8
V_SOURCE = 2
START_PANELS = 32
JET_ORDER = 16


class SourceCap(RuntimeError):
    """A frozen runtime or source-panel budget has been exhausted."""


def _bump(stats, field, amount=1):
    stats[field] = stats.get(field, 0) + amount


def _c2_majorant(pi, n):
    first = (n + 1)**4 * (-pi * ((n + 1)**2 - 1)).exp()
    ratio = (arb(n + 2) / (n + 1))**4 * (-pi * (2*n + 3)).exp()
    return first / (1 - ratio)


def _q_majorant(pi, v):
    t = pi * arb(4*v).exp()
    polynomial = (((t + 4)*t + 12)*t + 24)*t + 24
    return (-t).exp() * polynomial / (2 * pi**2 * pi.root(4))


def _source_bounds():
    pi = arb.pi()
    q = _q_majorant(pi, 0)
    b0 = 5 * _c2_majorant(pi, 0)
    source_error = (5 * _c2_majorant(pi, N_SOURCE)*q
                    + b0 * _q_majorant(pi, V_SOURCE)) / 2
    return source_error.upper(), (2**64 * b0 * q).upper()


def require_coefficient_enclosures(coefficients, radii, enclosures):
    """Check exact dyadic centers/radii and containment of each acquired ball."""
    if not len(coefficients) == len(radii) == len(enclosures) == DEGREE + 1:
        raise ValueError("incomplete coefficient record")
    for j, (coefficient, radius, enclosure) in enumerate(
        zip(coefficients, radii, enclosures)
    ):
        if not (coefficient.is_finite() and coefficient.is_exact()
                and radius.is_finite() and radius.is_exact() and radius >= 0
                and enclosure.is_finite()):
            raise ValueError(f"invalid dyadic coefficient/radius at {j}")
        # Checking the exact midpoint and the Arb radius separately avoids
        # silently accepting an understated radius via constructor inflation.
        required = (enclosure.mid() - coefficient).abs_upper() + enclosure.rad()
        if not required <= radius:
            raise ValueError(f"coefficient error does not enclose the acquisition at {j}")


@dataclass(frozen=True)
class SourcePolynomial:
    coefficients: tuple
    radii: tuple
    enclosures: tuple
    source_error: arb
    moment_65: arb

    def fixed_errors(self, radius):
        """Source plus Taylor allowances, excluding coefficient uncertainty."""
        radius = arb(radius)
        if not 0 <= radius <= arb(3) / 2:
            raise ValueError("disk radius lies outside the checked source bound")
        return tuple(
            (self.source_error
             + self.moment_65 * radius**(65-k) / factorial(65-k)).upper()
            for k in range(8)
        )

    def coefficient_errors(self, radius):
        require_coefficient_enclosures(self.coefficients, self.radii, self.enclosures)
        radius = arb(radius)
        errors = []
        for k in range(8):
            # Horner bounds the derivative of the nonnegative error polynomial.
            total = arb(0)
            for j in range(DEGREE, k-1, -1):
                total = total*radius + self.radii[j] * (factorial(j)//factorial(j-k))
            errors.append(total.upper())
        return tuple(errors)

    def errors(self, radius):
        """Directed upper allowances from Note14 (14)–(15)."""
        return tuple((fixed + coeff).upper() for fixed, coeff in zip(
            self.fixed_errors(radius), self.coefficient_errors(radius)
        ))


def _phase_and_variable(center, u0, stats):
    """Normalized u jets [coefficient of t^k = f^(k)(u0)/k!]."""
    u = arb_series([u0, 1], JET_ORDER + 1)
    rho = arb.pi() * (4*u).exp()
    phi = arb_series([0], JET_ORDER + 1)
    for n in range(1, N_SOURCE + 1):
        mode = n*n * rho
        phi += mode * (2*mode - 3) * (-mode).exp()
    phi *= u.exp()
    sine, cosine = (center*u).sin_cos()
    _bump(stats, "source_jet_calls")
    # Counts formal series calls, not their internal FLINT scalar operations.
    _bump(stats, "source_jet_exp_calls", N_SOURCE + 2)
    _bump(stats, "source_jet_sin_cos_calls")
    cs, sn = phi*cosine, phi*sine
    return u, (cs, -sn, -cs, sn)


def _panel(center, left, right, stats):
    midpoint = (left + right) / 2
    half = (right - left) / 2
    u_mid, midpoint_phases = _phase_and_variable(center, midpoint, stats)
    u_all, interval_phases = _phase_and_variable(center, arb(midpoint, half), stats)
    midpoint_weight = arb_series([1], JET_ORDER + 1)
    interval_weight = arb_series([1], JET_ORDER + 1)
    powers = tuple(2*half**(2*k+1)/(2*k+1) for k in range(8))
    # The interval series gives f^(16)/16!, so (16) has factor 2 h^17/17.
    remainder_multiplier = 2*half**17 / 17
    enclosures = []
    for j in range(DEGREE + 1):
        point_jet = midpoint_phases[j % 4] * midpoint_weight
        panel_jet = interval_phases[j % 4] * interval_weight
        midpoint_rule = sum(point_jet[2*k]*powers[k] for k in range(8))
        remainder = (panel_jet[16].abs_upper()*remainder_multiplier).upper()
        enclosures.append(midpoint_rule + arb(0, remainder))
        if j < DEGREE:
            midpoint_weight = midpoint_weight*u_mid/(j + 1)
            interval_weight = interval_weight*u_all/(j + 1)
    _bump(stats, "source_scalar_terms", (DEGREE + 1)*9)
    _bump(stats, "source_coefficient_integrands", DEGREE + 1)
    return tuple(enclosures)


def acquire(center, bits, limits, stats, refinement=0, cache=None):
    """Acquire all 65 coefficients on a dyadic refinement of 32 source panels.

    The optional cache belongs to one case and only holds its current grid.
    At a higher refinement, recomputed child panels count toward the case
    budget. A precision change starts the prescribed initial grid again.
    """
    if bits not in (128, 256, 512):
        raise ValueError("precision is outside the frozen tiers")
    if not isinstance(refinement, int) or not 0 <= refinement <= limits.get("source_depth", 12):
        raise SourceCap("source subdivision depth cap")
    if START_PANELS * 2**refinement > limits.get("source_live", 4096):
        raise SourceCap("live source-panel cap")
    if cache is None:
        cache = {}

    def check_time():
        if monotonic() >= limits.get("deadline", float("inf")):
            raise SourceCap("source deadline")

    def evaluate_grid(depth):
        count = START_PANELS * 2**depth
        stats["source_max_depth"] = max(stats.get("source_max_depth", 0), depth)
        totals = [arb(0) for _ in range(DEGREE + 1)]
        # Stream panels in order. Only their directed sum needs retention.
        stats["source_peak_live"] = max(stats.get("source_peak_live", 0), count)
        for panel in range(count):
            check_time()
            if stats.get("source_panels", 0) >= limits.get("source_panels", 32768):
                raise SourceCap("total source-panel evaluation cap")
            _bump(stats, "source_panels")
            left = arb(V_SOURCE*panel) / count
            right = arb(V_SOURCE*(panel+1)) / count
            totals = [a+b for a, b in zip(totals, _panel(center, left, right, stats))]
        return tuple(totals)

    with ctx.workprec(bits):
        center = arb(center)
        if not center.is_finite() or not center.is_exact():
            raise ValueError("source center is not an exact dyadic")
        key = (bits, center.man_exp())
        if cache.get("key") != key:
            cache.clear()
            cache.update(key=key, depth=-1)
        if refinement < cache["depth"]:
            raise ValueError("the source cache cannot rewind to a coarser grid")
        old_cap = ctx.cap
        ctx.cap = JET_ORDER + 1
        try:
            for depth in range(cache["depth"] + 1, refinement + 1):
                cache["enclosures"] = evaluate_grid(depth)
                cache["depth"] = depth
            check_time()
            enclosures = cache["enclosures"]
            coefficients = tuple(v.mid() for v in enclosures)
            radii = tuple(v.rad() for v in enclosures)
            require_coefficient_enclosures(coefficients, radii, enclosures)
            if "bounds" not in cache:
                cache["bounds"] = _source_bounds()
            return SourcePolynomial(coefficients, radii, enclosures, *cache["bounds"])
        finally:
            ctx.cap = old_cap
