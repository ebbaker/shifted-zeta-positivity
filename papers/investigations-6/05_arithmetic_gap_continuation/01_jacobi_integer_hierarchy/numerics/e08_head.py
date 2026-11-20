"""Complete moving-head Taylor enclosure for AGC-JH-E08 r1.

19 November 2026, prepared for Edward Baker with OpenAI Codex LLM
assistance. The packet specifies gpt-6.2-sol / ultra for execution.
Serving-model and effort metadata are unavailable.
"""

from math import comb, factorial
from time import perf_counter

from flint import arb, ctx

from e07_fields import _ball, _parity_pivots, _xi, _xi_jet


SITES = 24
CENTER = 36
SPATIAL_RADIUS = 10
LEVELS = ((10, 768, 192), (14, 1280, 240))


def _time_zero_data(last_link, mass):
    jet = _xi_jet(0, 2 * last_link + 1, mass)
    if not jet[0].contains(1) or not all(value.contains(0) for value in jet[1::2]):
        raise ArithmeticError("normalized xi origin parity check failed")
    moments = [arb(1)] + [
        (-1) ** j * factorial(2 * j) * jet[2 * j]
        for j in range(1, last_link + 1)
    ]
    if not all(moment.is_finite() and moment > 0 for moment in moments):
        raise ArithmeticError("a normalized even source moment was not certified positive")
    pivots = _parity_pivots(moments)
    betas = [arb(0)] + [pivots[j] / pivots[j - 1] for j in range(1, last_link + 1)]
    if not all(beta.is_finite() and beta > 0 for beta in betas[1:]):
        raise ArithmeticError("a time-zero beta link was not certified positive")
    return pivots, betas


def _edge_jets(betas, order, time_scale):
    """Beta and square-root Taylor coefficients in s = t / time_scale."""
    beta_rows = [[beta] for beta in betas]
    beta_rows[0].extend([arb(0)] * order)
    for k in range(1, order + 1):
        for j in range(1, len(betas) - k):
            previous, current, following = beta_rows[j - 1:j + 2]
            value = sum(
                current[i] * (following[k - 1 - i] - previous[k - 1 - i])
                for i in range(k)
            )
            current.append(time_scale * value / k)

    edges = []
    for beta in beta_rows[1:SITES]:
        edge = [beta[0].sqrt()]
        for k in range(1, order + 1):
            known = sum(edge[i] * edge[k - i] for i in range(1, k))
            edge.append((beta[k] - known) / (2 * edge[0]))
        if not all(value.is_finite() for value in edge):
            raise ArithmeticError("a moving-edge coefficient was nonfinite")
        edges.append(edge)
    return edges


def _complex_head_bounds(pivots, edges, h0, time_radius):
    """Tilted orthonormal Gram and Duhamel bounds on |t| <= time_radius."""
    padded = [arb(0), *(edge[0] for edge in edges), arb(0)]
    norm_zero = max((left + right).upper() for left, right in zip(padded, padded[1:]))
    min_pivot = min(value.lower() for value in pivots[:SITES])
    if not (min_pivot > 0 and norm_zero.is_finite()):
        raise ArithmeticError("the time-zero Jacobi norm or pivot bound failed")

    # For u >= 1 the squared orthonormal polynomial sum is bounded by
    # SITES*(1+norm_zero)^degree*u^degree/min_pivot. Each monic polynomial
    # is a characteristic polynomial of a leading compression of J(0).
    degree = 2 * (SITES - 1)
    pi = arb.pi()
    pi_e4 = pi * arb(4).exp()
    theta_denominator = 1 - 16 * (-3 * pi).exp()
    slope = 4 * pi_e4 - 2 * time_radius - (9 + degree)
    if not (theta_denominator > 0 and slope > 0 and 16 * pi_e4 > 2 * time_radius):
        raise ArithmeticError("the tilted theta tail majorant is undecided")
    theta_constant = 2 * pi ** 2 / theta_denominator
    # Use u^degree <= exp(degree*(u-1)), then negative curvature of the
    # exponent and its tangent at 1. h0 is the canonical half-line mass.
    tail = (
        SITES * (1 + norm_zero) ** degree * theta_constant
        * (time_radius + 9 - pi_e4).exp() / (h0 * min_pivot * slope)
    ).upper()
    bulk = (time_radius.exp() - 1).upper()
    gram_change = (bulk + tail).upper()
    if not gram_change < arb(1) / 2:
        raise ArithmeticError("the common complex Gram perturbation reaches one half")
    # The Schur complements in the time-zero orthonormal basis equal the
    # moving monic norms divided by their time-zero norms. Their log
    # branches give the analytic square roots of the adjacent norm ratios.
    schur_change = (gram_change / (1 - gram_change)).upper()
    if not schur_change < 1:
        raise ArithmeticError("the Schur complement displacement reaches one")
    edge_relative_change = (schur_change / (1 - schur_change)).upper()
    norm_change = (norm_zero * edge_relative_change).upper()
    norm_complex = (norm_zero + norm_change).upper()
    # Duhamel uses exp(i*z*J(0)) as the reference, so its exponent starts
    # with |Im z|, while the perturbation pays the full |z|.
    abs_z = CENTER + SPATIAL_RADIUS
    field_majorant = (SPATIAL_RADIUS * norm_zero + abs_z * norm_change).exp().upper()
    return norm_complex, field_majorant, {
        "physical_H0_at_zero": _ball(h0),
        "minimum_pivot_through_degree_23": _ball(min_pivot),
        "time_zero_spectral_norm_upper": _ball(norm_zero),
        "tail_square_polynomial_degree": degree,
        "theta_envelope_constant": _ball(theta_constant),
        "tail_exponent_decrease_per_unit_lower": _ball(slope.lower()),
        "gram_change_bulk_upper": _ball(bulk),
        "gram_change_tail_upper": _ball(tail),
        "gram_change_upper": _ball(gram_change),
        "schur_complement_change_upper": _ball(schur_change),
        "relative_edge_change_upper": _ball(edge_relative_change),
        "jacobi_norm_change_upper": _ball(norm_change),
        "complex_jacobi_norm_upper": _ball(norm_complex),
        "duhamel_field_majorant_upper": _ball(field_majorant),
    }


def _centered_path_series(edges, order, terms):
    """Build the spatial exponential by sparse paths and shift it to 36."""
    vector = [[arb(0)] * (order + 1) for _ in range(SITES)]
    vector[0][0] = arb(1)
    rows = [[arb(0)] * (terms - 1) for _ in range(order + 1)]
    for m in range(terms):
        # vector is J(s)^m e_0 / m!, computed modulo s^(order+1).
        # The bipartite paths vanish at site 0 for every odd m.
        if m % 2 == 0:
            sign = (-1) ** (m // 2)
            weights = [sign * comb(m, j) * CENTER ** (m - j) for j in range(m + 1)]
            for k, row in enumerate(rows):
                coefficient = vector[0][k]
                for j, weight in enumerate(weights):
                    row[j] += coefficient * weight
        if m + 1 == terms:
            break
        outgoing = [[arb(0)] * (order + 1) for _ in range(SITES)]
        for j in range((m + 1) % 2, SITES, 2):
            neighbors = []
            if j > 0:
                neighbors.append((edges[j - 1], vector[j - 1]))
            if j + 1 < SITES:
                neighbors.append((edges[j], vector[j + 1]))
            outgoing[j] = [
                sum(edge[i] * neighbor[k - i]
                    for edge, neighbor in neighbors for i in range(k + 1)) / (m + 1)
                for k in range(order + 1)
            ]
        vector = outgoing
    return rows


def build_head(K, bits, terms):
    """Return outward coefficient rows, a joint value tail, and its ledger.

    Rows are in ascending powers of s=t/T and z-36. The tail is a
    complex modulus bound on spatial radius 10 for every 0 <= t <= T.
    It also bounds the spatial derivative tail on radius 9 by Cauchy.
    """
    if (K, bits, terms) not in LEVELS:
        raise ValueError("moving-head parameters outside the frozen E08 r1 levels")
    ctx.prec = bits
    saved_cap = ctx.cap
    start = perf_counter()
    time_scale = arb(1) / 10000
    time_radius = arb(1) / 20
    last_link = SITES - 1 + K
    try:
        mass = _xi(arb(1) / 2)
        if not mass.is_finite() or not mass > 0:
            raise ArithmeticError("xi normalization was not certified positive")
        pivots, betas = _time_zero_data(last_link, mass)
    finally:
        ctx.cap = saved_cap
    acquired = perf_counter()
    edges = _edge_jets(betas, K, time_scale)
    norm_complex, majorant, constants = _complex_head_bounds(pivots, edges, mass / 8, time_radius)
    bounded = perf_counter()
    rows = _centered_path_series(edges, K, terms)
    if not all(value.is_finite() for row in rows for value in row):
        raise ArithmeticError("the centered moving-head series has a nonfinite coefficient")
    paths_done = perf_counter()

    ratio = time_scale / time_radius
    spatial_argument = (CENTER + SPATIAL_RADIUS) * norm_complex
    spatial = (spatial_argument.exp() * spatial_argument ** terms / factorial(terms)).upper()
    projected_spatial = (spatial / (1 - ratio)).upper()
    time = (majorant * ratio ** (K + 1) / (1 - ratio)).upper()
    tail = (projected_spatial + time).upper()
    rounding = sum(
        coefficient.rad() * SPATIAL_RADIUS ** j
        for row in rows for j, coefficient in enumerate(row)
    ).upper()
    if not (tail.is_finite() and tail > 0 and rounding.is_finite()):
        raise ArithmeticError("the joint moving-head remainder was not certified finite")
    return rows, tail, {
        "sites": SITES,
        "order": K,
        "precision_bits": bits,
        "time_scale": "1/10000",
        "complex_time_disk_radius": "1/20",
        "value_tail_spatial_radius": SPATIAL_RADIUS,
        "first_derivative_tail_spatial_radius": SPATIAL_RADIUS - 1,
        "last_time_zero_beta": last_link,
        "last_time_zero_moment_order": 2 * last_link,
        "origin_xi_terms": 2 * last_link + 1,
        "positive_pivot_count": len(pivots),
        "beta_24": _ball(betas[SITES]),
        "last_beta": _ball(betas[last_link]),
        "origin_exponential_terms": terms,
        "nonzero_even_origin_powers": terms // 2,
        "formal_tridiagonal_steps": terms - 1,
        "centered_terms_per_row": len(rows[0]),
        **constants,
        "space_truncation_complex_time_upper": _ball(spatial),
        "space_truncation_time_projected_upper": _ball(projected_spatial),
        "time_truncation_upper": _ball(time),
        "value_and_first_derivative_tail_upper": _ball(tail),
        "radius_weighted_coefficient_radii_upper": _ball(rounding),
        "seconds": {
            "xi_positive_pivots_and_links": acquired - start,
            "formal_time_edges_and_complex_disk": bounded - acquired,
            "paths_and_center_shift": paths_done - bounded,
            "total": perf_counter() - start,
        },
    }
