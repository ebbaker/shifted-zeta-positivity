"""Complete normalized theta source on the frozen AGC-JH-E08 slab.

19 November 2026. Prepared for Edward Baker with OpenAI Codex LLM
assistance. The E08 packet specifies gpt-6.2-sol / ultra. Serving
metadata are unavailable.
"""

from math import factorial
from time import perf_counter

from flint import arb, ctx

from e07_fields import CAUCHY_RADIUS, CENTER, RADIUS, _ball, _xi, _xi_jet


def _theta_tail(time_radius, imaginary_radius, physical_mass):
    """Bound the absolute normalized tilted source integral on u >= 1.

    Use Phi(u) <= C exp(9u - pi exp(4u)) from HDC Note13. For u >= 1,
    u^2 <= exp(4(u-1)) and exp(4(u-1)) >= 1 + 4(u-1). Also
    cosh(Bu) <= exp(Bu). The resulting exponential integrates exactly.
    """
    pi = arb.pi()
    constant = 2 * pi**2 / (1 - 16 * (-3 * pi).exp())
    decay = pi * arb(4).exp() - time_radius
    slope = 4 * decay - 9 - imaginary_radius
    if not slope > 0:
        raise ArithmeticError("theta tail exponential is not certified integrable")
    return (constant * (9 + imaginary_radius - decay).exp() / (slope * physical_mass)).upper()


def build_source(K, bits, terms):
    """Return real coefficient rows, a uniform complex-modulus tail, and metadata.

    The exact coefficient in each ball multiplies (t/T)^k (z-36)^m.
    The absolute tail holds on |t| <= T and |z-36| <= 10, for the
    exact coefficients. Coefficient rounding is paid by interval evaluation.
    """
    if (K, bits, terms) not in ((10, 768, 144), (14, 1280, 160)):
        raise ValueError("source level outside the frozen E08 r1 packet")
    start = perf_counter()
    ctx.prec = bits
    time_step = arb(1) / 10000
    time_radius = arb(1) / 20
    xi_mass = _xi(arb(1) / 2)
    if not xi_mass.is_finite() or not xi_mass > 0:
        raise ArithmeticError("xi normalization is not certified positive")

    saved_cap = ctx.cap
    try:
        spatial_jet = _xi_jet(CENTER, terms + 2 * K, xi_mass)
        origin_jet = _xi_jet(0, 2 * K + 1, xi_mass)
    finally:
        ctx.cap = saved_cap
    if not origin_jet[0].contains(1) or not all(c.contains(0) for c in origin_jet[1::2]):
        raise ArithmeticError("time-zero source origin parity check failed")

    # The heat law is H_t = -H_zz. Work in the scaled variable s=t/T
    # before dividing by H_t(0)/H_0(0). Its exact constant term is one.
    factorials = [factorial(j) for j in range(terms + 2 * K)]
    time_factors = [(-time_step)**k for k in range(K + 1)]
    mass_jet = [arb(1)] + [
        time_factors[k] * (factorials[2 * k] // factorials[k]) * origin_jet[2 * k]
        for k in range(1, K + 1)
    ]
    if not all(coefficient > 0 for coefficient in mass_jet):
        raise ArithmeticError("an even theta moment is not certified positive")

    rows = []
    for k in range(K + 1):
        row = []
        for m in range(terms):
            shifted = m + 2 * k
            multiplier = factorials[shifted] // (factorials[k] * factorials[m])
            heat_coefficient = time_factors[k] * multiplier * spatial_jet[shifted]
            row.append(heat_coefficient - sum(mass_jet[j] * rows[k - j][m] for j in range(1, k + 1)))
        if not all(coefficient.is_finite() for coefficient in row):
            raise ArithmeticError("normalized theta coefficient is nonfinite")
        rows.append(row)

    # Positivity pays the bulk up to u=1, and the complete theta bound
    # pays the remainder on the larger complex-time Cauchy disk.
    physical_mass = xi_mass / 8
    mass_tail = _theta_tail(time_radius, 0, physical_mass)
    spatial_integral_tail = _theta_tail(time_radius, CAUCHY_RADIUS, physical_mass)
    bulk_factor = time_radius.exp()
    mass_change = (bulk_factor - 1 + mass_tail).upper()
    mass_lower = (1 - mass_change).lower()
    if not mass_lower > 0:
        raise ArithmeticError("tilted source mass lacks a nonzero complex-time floor")

    # Reflection identifies F_0(24i) with xi(25/2)/xi(1/2).
    untilted_majorant = _xi(arb(CAUCHY_RADIUS + 1) / 2) / xi_mass
    if not untilted_majorant.is_finite() or not untilted_majorant > 0:
        raise ArithmeticError("time-zero Cauchy majorant is not certified positive")
    normalized_majorant = ((bulk_factor * untilted_majorant + spatial_integral_tail) / mass_lower).upper()
    time_ratio = time_step / time_radius
    space_ratio = arb(RADIUS) / CAUCHY_RADIUS
    time_tail = (normalized_majorant * time_ratio**(K + 1) / (1 - time_ratio)).upper()
    spatial_tail = (
        normalized_majorant * space_ratio**terms / ((1 - space_ratio) * (1 - time_ratio))
    ).upper()
    complete_tail = (time_tail + spatial_tail).upper()
    rounding_radius = sum(
        coefficient.rad() * RADIUS**m for row in rows for m, coefficient in enumerate(row)
    ).upper()
    return rows, complete_tail, {
        "time_degree": K,
        "precision_bits": bits,
        "centered_spatial_terms": terms,
        "centered_xi_series_terms": terms + 2 * K,
        "origin_xi_series_terms": 2 * K + 1,
        "uniform_time_radius": "1/10000",
        "uniform_spatial_radius": RADIUS,
        "cauchy_time_radius": "1/20",
        "cauchy_spatial_radius": CAUCHY_RADIUS,
        "physical_H0_at_zero": _ball(physical_mass),
        "mass_integral_tail_upper": _ball(mass_tail),
        "spatial_integral_tail_upper": _ball(spatial_integral_tail),
        "mass_change_upper": _ball(mass_change),
        "complex_time_mass_floor": _ball(mass_lower),
        "time_zero_spatial_majorant": _ball(untilted_majorant),
        "normalized_polydisk_majorant": _ball(normalized_majorant),
        "normalized_time_tail_upper": _ball(time_tail),
        "normalized_spatial_tail_upper": _ball(spatial_tail),
        "normalized_complete_tail_upper": _ball(complete_tail),
        "radius_weighted_coefficient_radii": _ball(rounding_radius),
        "seconds": perf_counter() - start,
    }
