"""Arb source and canonical Jacobi head for AGC-JH-E07 r1.

19 November 2026, prepared for Edward Baker with OpenAI Codex assistance.
The packet requests gpt-6.2-sol / ultra. Serving metadata is unreported.
"""

from math import factorial
from time import perf_counter

import flint
from flint import acb, acb_mat, acb_series, arb, ctx


CENTER = 36
RADIUS = 10
CAUCHY_RADIUS = 24
TERMS = 144


def _xi(s):
    half_s = s / 2
    return s * (s - 1) * (-arb.pi().log() * half_s).exp() * half_s.gamma() * s.zeta() / 2


def _xi_jet(center, count, mass):
    ctx.cap = count
    s = acb_series([acb(arb(1) / 2, arb(center) / 2), acb(0, arb(1) / 2)])
    jet = _xi(s) / mass
    if not all(jet[k].is_finite() and jet[k].imag.contains(0) for k in range(count)):
        raise ArithmeticError("normalized xi Taylor jet has a nonfinite or nonreal enclosure")
    return [jet[k].real for k in range(count)]


def _parity_pivots(moments):
    """Return the normalised squared monic norms h_0 through h_(N-1)."""
    norms = [None] * len(moments)
    for parity in (0, 1):
        degrees = list(range(parity, len(moments), 2))
        lower = [[arb(0) for _ in degrees] for _ in degrees]
        pivots = []
        for i, degree in enumerate(degrees):
            pivot = moments[degree] - sum(lower[i][k] ** 2 * pivots[k] for k in range(i))
            if not pivot.is_finite() or not pivot > 0:
                raise ArithmeticError(f"nonpositive or undecided parity pivot at degree {degree}: {pivot}")
            norms[degree] = pivot
            pivots.append(pivot)
            for j in range(i + 1, len(degrees)):
                moment_index = (degree + degrees[j]) // 2
                correction = sum(lower[j][k] * lower[i][k] * pivots[k] for k in range(i))
                lower[j][i] = (moments[moment_index] - correction) / pivot
    return norms


def _head_jet(edges):
    """Enclose exp(i*CENTER*J)e_0 once, then apply i*J successively."""
    size = len(edges) + 1
    padded = [arb(0), *edges, arb(0)]
    spectral_upper = max((padded[j] + padded[j + 1]).upper() for j in range(size))
    matrix = acb_mat(size, size)
    for j, edge in enumerate(edges):
        matrix[j, j + 1] = matrix[j + 1, j] = acb(0, CENTER * edge)
    value = matrix.exp()
    vector = [value[j, 0] for j in range(size)]
    imaginary_edges = [acb(0, edge) for edge in edges]
    coefficients = []
    for order in range(TERMS):
        readout = vector[0]
        if not readout.is_finite() or not readout.imag.contains(0):
            raise ArithmeticError(f"Jacobi head jet has a nonfinite or nonreal enclosure at order {order}")
        coefficients.append(readout.real)
        if order < TERMS - 1:
            # The vector stores the derivative already divided by order!.
            outgoing = [acb(0) for _ in range(size)]
            for j, edge in enumerate(imaginary_edges):
                outgoing[j] += edge * vector[j + 1]
                outgoing[j + 1] += edge * vector[j]
            vector = [entry / (order + 1) for entry in outgoing]
    scaled_radius = RADIUS * spectral_upper
    tail = ((scaled_radius ** TERMS / factorial(TERMS)) * scaled_radius.exp()).upper()
    return coefficients, tail, spectral_upper


def _rounding_sum(coefficients):
    """Value perturbation on radius 10 if coefficients were replaced by midpoints."""
    return sum(coefficient.rad() * RADIUS ** k for k, coefficient in enumerate(coefficients)).upper()


def _ball(value):
    return {
        "lower": str(value.lower().fmpq()),
        "upper": str(value.upper().fmpq()),
        "display": str(value),
    }


def build_fields(n, bits):
    """Return (F coefficients, Y coefficients, F tail, Y tail, receipt data).

    Coefficient balls include rounding. The positive tail bounds are
    complex-modulus bounds on |z-36| <= 10, valid relative to the exact
    coefficients contained in the returned balls. Cauchy's estimate on
    a unit radius gives the same absolute derivative tail on |z-36| <= 9.
    """
    if n not in (24, 28) or bits not in (768, 1280):
        raise ValueError("degree or precision outside the frozen E07 r1 packet")
    ctx.prec = bits
    start = perf_counter()
    saved_cap = ctx.cap
    try:
        mass = _xi(arb(1) / 2)
        if not mass.is_finite() or not mass > 0:
            raise ArithmeticError("xi normalization is not certified positive")
        at_zero = _xi_jet(0, 2 * n - 1, mass)
        if not at_zero[0].contains(1) or not all(coefficient.contains(0) for coefficient in at_zero[1::2]):
            raise ArithmeticError("normalized xi origin parity check failed")
        moments = [arb(1)] + [(-1) ** k * factorial(2 * k) * at_zero[2 * k] for k in range(1, n)]
        if not all(moment > 0 for moment in moments):
            raise ArithmeticError("an even source moment is not certified positive")
        moments_done = perf_counter()
        norms = _parity_pivots(moments)
        betas = [norms[j] / norms[j - 1] for j in range(1, n)]
        if not all(beta.is_finite() and beta > 0 for beta in betas):
            raise ArithmeticError("a canonical beta enclosure is not certified positive")
        edges = [beta.sqrt() for beta in betas]
        coefficients_done = perf_counter()

        f = _xi_jet(CENTER, TERMS, mass)
        # F(24i) is xi(-23/2)/xi(1/2) = xi(25/2)/xi(1/2) by reflection.
        cauchy_majorant = _xi(arb(25) / 2) / mass
        if not cauchy_majorant.is_finite() or not cauchy_majorant > 0:
            raise ArithmeticError("source Cauchy majorant is not certified positive")
        ratio = arb(RADIUS) / CAUCHY_RADIUS
        ef = (cauchy_majorant * ratio ** TERMS / (1 - ratio)).upper()
        source_done = perf_counter()
        y, ey, spectral_upper = _head_jet(edges)
        head_done = perf_counter()
    finally:
        ctx.cap = saved_cap

    return f, y, ef, ey, {
        "time": "0",
        "center": CENTER,
        "sites": n,
        "precision_bits": bits,
        "flint_version": flint.__FLINT_VERSION__,
        "python_flint_version": flint.__version__,
        "normalized_xi_mass": _ball(mass),
        "physical_H0_at_zero": _ball(mass / 8),
        "full_line_source_mass": _ball(mass / 4),
        "origin_xi_series_terms": 2 * n - 1,
        "normalized_even_moments": [_ball(moment) for moment in moments],
        "positive_parity_pivots": [_ball(norm) for norm in norms],
        "beta_links_through_n_minus_one": [_ball(beta) for beta in betas],
        "jacobi_edge_balls": [_ball(edge) for edge in edges],
        "centered_terms_per_field": TERMS,
        "complex_value_tail_radius": RADIUS,
        "first_derivative_tail_radius": RADIUS - 1,
        "source_cauchy_radius": CAUCHY_RADIUS,
        "source_cauchy_majorant": _ball(cauchy_majorant),
        "source_value_tail_upper": _ball(ef),
        "head_spectral_radius_upper": _ball(spectral_upper),
        "head_value_tail_upper": _ball(ey),
        "source_coefficient_radius_sum_on_radius_10": _ball(_rounding_sum(f)),
        "head_coefficient_radius_sum_on_radius_10": _ball(_rounding_sum(y)),
        "head_matrix_exponentials": 1,
        "head_tridiagonal_matrix_vector_products": TERMS - 1,
        "seconds": {
            "xi_moments": moments_done - start,
            "parity_ldl_and_links": coefficients_done - moments_done,
            "centered_xi_source": source_done - coefficients_done,
            "centered_jacobi_head": head_done - source_done,
        },
    }
