#!/usr/bin/env python3
"""Small dyadic signed-pair identity checks; floating, never a certificate."""
from collections import defaultdict
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parent
A = 0.25
A0 = math.exp(-A)
B0 = math.exp(A)
ELL = 2 * A
NU = 146640624550936576 / 37921101075
SQRT_NU = math.sqrt(NU)
XS = (8.125, 19.375, 53.625, 101.3)


@lru_cache(None)
def gauss(order):
    return np.polynomial.legendre.leggauss(order)


def quad(fn, lo, hi, order):
    if hi <= lo:
        return 0.0
    z, q = gauss(order)
    r = (hi - lo) / 2
    return float(r * np.dot(q, fn((lo + hi) / 2 + r * z)))


def g(v):
    v = np.asarray(v)
    out = np.zeros_like(v, dtype=float)
    inside = np.abs(v) < A
    x = v[inside]
    xx = x * x
    out[inside] = (-64 * x * (1 - 16 * xx) ** 5
                   * (2689 - 215072 * xx + 256 * xx * xx) / SQRT_NU)
    return out


def w(t):
    t = np.asarray(t)
    out = np.zeros_like(t, dtype=float)
    inside = (t > A0) & (t < B0)
    out[inside] = g(-np.log(t[inside])) / np.sqrt(t[inside])
    return out


def pair_y(n, m, X, order=24):
    """Centered log-coordinate weight, symmetric in n and m."""
    center = (math.log(n) + math.log(m)) / 2
    delta = (math.log(m) - math.log(n)) / 2
    lo = max(-A + abs(delta), math.log(X) - center)
    hi = min(A - abs(delta), math.log(2 * X) - center)
    return math.sqrt(n * m) * quad(
        lambda v: np.exp(2 * v) * g(v + delta) * g(v - delta),
        lo, hi, order)


def pair_t(n, m, X, order=40):
    """Independent ratio-coordinate weight, from t=n/x and dx=-n dt/t^2."""
    ratio = m / n
    lo = max(n / (2 * X), A0, A0 / ratio)
    hi = min(n / X, B0, B0 / ratio)
    return n * quad(lambda t: w(t) * w(ratio * t) / (t * t),
                    lo, hi, order)


def prime_powers(X):
    limit = math.ceil(2 * B0 * X)
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            for n in range(p * p, limit + 1, p):
                sieve[n] = False
    rows = []
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        n, exponent = p, 1
        while n < 2 * B0 * X:
            if n > A0 * X:
                cap = ('lower' if n < B0 * X else
                       'upper' if n > 2 * A0 * X else 'bulk')
                rows.append({'n': n, 'prime': p, 'exponent': exponent,
                             'Lambda': math.log(p), 'packet_region': cap})
            n *= p
            exponent += 1
    return sorted(rows, key=lambda row: row['n'])


def direct_square(X, rows, order=32, log_coordinate=False):
    """Integrate the actual signal before squaring; split all packet endpoints."""
    if not rows:
        return 0.0, 1
    points = {X, 2 * X}
    for row in rows:
        for endpoint in (row['n'] / B0, row['n'] / A0):
            if X < endpoint < 2 * X:
                points.add(endpoint)
    points = sorted(points)
    terms = []
    for lo, hi in zip(points[:-1], points[1:]):
        if log_coordinate:
            def integrand(y):
                p = sum((row['Lambda'] / math.sqrt(row['n'])
                         * g(y - math.log(row['n']))) for row in rows)
                return np.exp(2 * y) * p * p
            terms.append(quad(integrand, math.log(lo), math.log(hi), order))
        else:
            def integrand(x):
                V = sum((row['Lambda'] * w(row['n'] / x)) for row in rows)
                return V * V
            terms.append(quad(integrand, lo, hi, order))
    return math.fsum(terms), len(points) - 1


def sample(X):
    rows = prime_powers(X)
    diagonal = []
    offdiagonal = []
    shifted = defaultdict(list)
    blocks = defaultdict(list)
    pair_residuals = []
    symmetry_residuals = []
    for i, row in enumerate(rows):
        n, ln = row['n'], row['Lambda']
        d = ln * ln * pair_y(n, n, X)
        diagonal.append(d)
        blocks[f"{row['packet_region']}/{row['packet_region']}"].append(d)
        for other in rows[i + 1:]:
            m, lm = other['n'], other['Lambda']
            wy = pair_y(n, m, X)
            wt = pair_t(n, m, X)
            pair_residuals.append(abs(wy - wt))
            symmetry_residuals.append(abs(wy - pair_y(m, n, X)))
            term = 2 * ln * lm * wy
            if term:
                offdiagonal.append(term)
                shifted[m - n].append(ln * lm * wy)
                regions = sorted((row['packet_region'], other['packet_region']))
                blocks['/'.join(regions)].append(term)
    D = math.fsum(diagonal)
    C = math.fsum(offdiagonal)
    shifted_values = {str(h): math.fsum(values)
                      for h, values in sorted(shifted.items())}
    direct, pieces = direct_square(X, rows)
    log_direct, _ = direct_square(X, rows, log_coordinate=True)
    # Deliberately wrong windows expose both missing caps separately.
    alternatives = {}
    predicates = {
        'omit_n_below_X': lambda n: n >= X,
        'omit_n_above_2X': lambda n: n <= 2 * X,
        'keep_only_X_to_2X': lambda n: X <= n <= 2 * X,
        'keep_only_full_packets': lambda n: B0 * X <= n <= 2 * A0 * X,
    }
    for name, predicate in predicates.items():
        kept = [row for row in rows if predicate(row['n'])]
        value, _ = direct_square(X, kept)
        alternatives[name] = {
            'kept_prime_power_count': len(kept),
            'omitted_n': [row['n'] for row in rows if not predicate(row['n'])],
            'square_integral': value,
            'difference_from_complete': value - direct,
        }
    scale = max(1.0, direct, D)
    residuals = {
        'direct_x_vs_pair_sum_absolute': abs(direct - D - C),
        'direct_x_vs_log_square_absolute': abs(direct - log_direct),
        'offdiagonal_vs_twice_shifted_sum_absolute': abs(
            C - 2 * math.fsum(shifted_values.values())),
        'largest_pair_y_vs_t_absolute': max(pair_residuals, default=0.0),
        'largest_pair_symmetry_absolute': max(symmetry_residuals, default=0.0),
    }
    assert residuals['direct_x_vs_pair_sum_absolute'] < 2e-10 * scale
    assert residuals['direct_x_vs_log_square_absolute'] < 2e-10 * scale
    assert residuals['largest_pair_y_vs_t_absolute'] < 2e-10 * X
    return {
        'X': X, 'complete_integer_support_open': [A0 * X, 2 * B0 * X],
        'full_packet_integer_support_closed': [B0 * X, 2 * A0 * X],
        'prime_power_count': len(rows), 'packet_endpoint_piece_count': pieces,
        'prime_powers': rows,
        'cap_counts': {region: sum(row['packet_region'] == region for row in rows)
                       for region in ('lower', 'bulk', 'upper')},
        'diagonal_D': D, 'signed_offdiagonal_C': C,
        'positive_offdiagonal_mass': math.fsum(v for v in offdiagonal if v > 0),
        'negative_offdiagonal_mass': math.fsum(v for v in offdiagonal if v < 0),
        'direct_V_square_integral': direct,
        'direct_log_weighted_p_square_integral': log_direct,
        'V_square_over_X2_log_2X': direct / (X * X * math.log(2 * X)),
        'shifted_C_h_without_factor_two': shifted_values,
        'signed_cap_block_contributions_including_diagonal': {
            name: math.fsum(values) for name, values in sorted(blocks.items())},
        'deliberately_truncated_windows': alternatives,
        'consistency': residuals,
    }


def continuum_pair_square(bounds, outer_order, pair_order=24, whole_packets=False):
    """Integrate W_1(n,m) over a density rectangle, independently of V0^2.

    The complete rectangle has fixed cap partitions; no arithmetic diagonal
    is added to this Lebesgue double integral (its diagonal has measure zero).
    """
    nodes, weights = gauss(outer_order)
    ns, qs = [], []
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        ns.extend((lo + hi) / 2 + (hi - lo) / 2 * nodes)
        qs.extend((hi - lo) / 2 * weights)
    ns, qs = np.array(ns), np.array(qs)
    n = np.repeat(ns, len(ns))
    m = np.tile(ns, len(ns))
    qq = np.repeat(qs, len(qs)) * np.tile(qs, len(qs))
    z, q = gauss(pair_order)
    signed, absolute = [], []
    for start in range(0, len(n), 2048):
        nn, mm = n[start:start + 2048], m[start:start + 2048]
        cc = (np.log(nn) + np.log(mm)) / 2
        dd = (np.log(mm) - np.log(nn)) / 2
        if whole_packets:
            lo = -A + np.abs(dd)
            hi = A - np.abs(dd)
        else:
            lo = np.maximum(-A + np.abs(dd), -cc)
            hi = np.minimum(A - np.abs(dd), math.log(2) - cc)
        radius = np.maximum(0, hi - lo) / 2
        vv = (lo + hi)[:, None] / 2 + radius[:, None] * z
        kernels = np.sqrt(nn * mm) * radius * np.sum(
            np.exp(2 * vv) * g(vv + dd[:, None])
            * g(vv - dd[:, None]) * q[None, :], axis=1)
        contributions = qq[start:start + 2048] * kernels
        signed.append(float(np.sum(contributions)))
        absolute.append(float(np.sum(np.abs(contributions))))
    return {'outer_order_per_partition': outer_order, 'pair_order': pair_order,
            'whole_packets': whole_packets,
            'signed_double_integral_at_X_1': math.fsum(signed),
            'absolute_kernel_double_integral_at_X_1': math.fsum(absolute)}


def truncated_continuum_square(order):
    """Independently square int_1^2 w(n/x) dn with both caps retained."""
    def integrand(x):
        density = []
        for xx in x:
            lo = max(A0, 1 / xx)
            hi = min(B0, 2 / xx)
            density.append(xx * quad(w, lo, hi, 40))
        return np.square(density)
    bounds = (1, B0, 2 * A0, 2)
    return math.fsum(quad(integrand, lo, hi, order)
                     for lo, hi in zip(bounds[:-1], bounds[1:]))


def whole_packet_continuum_square(order):
    """Square the complete dyadic-band density over both exterior x caps."""
    def integrand(x):
        density = []
        for xx in x:
            lo = max(A0, A0 / xx)
            hi = min(B0, 2 * B0 / xx)
            density.append(xx * quad(w, lo, hi, 40))
        return np.square(density)
    lower = quad(integrand, A0 / B0, 1, order)
    upper = quad(integrand, 2, 2 * B0 / A0, order)
    return {'lower_exterior_cap': lower, 'upper_exterior_cap': upper,
            'total_c_g': lower + upper}


def continuum_checks():
    moment = quad(w, A0, B0, 48)
    full_direct = (7 / 3) * moment * moment
    full_pairs = [continuum_pair_square((A0, B0, 2 * A0, 2 * B0), order)
                  for order in (48, 80)]
    truncated_pairs = [continuum_pair_square((1, B0, 2 * A0, 2), order)
                       for order in (48, 80)]
    truncated_squares = {str(order): truncated_continuum_square(order)
                         for order in (24, 40)}
    whole_pairs = [continuum_pair_square((A0, B0, 2 * A0, 2 * B0), order,
                                        whole_packets=True)
                   for order in (48, 80)]
    whole_squares = {str(order): whole_packet_continuum_square(order)
                    for order in (24, 40)}
    assert abs(full_pairs[-1]['signed_double_integral_at_X_1']) < 2e-8
    assert abs(truncated_pairs[-1]['signed_double_integral_at_X_1']
               - truncated_squares['40']) < 2e-8
    assert abs(whole_pairs[-1]['signed_double_integral_at_X_1']
               - whole_squares['40']['total_c_g']) < 2e-8
    return {
        'int_w_dt_order_48': moment,
        'complete_continuum_V_square_at_X_1_from_moment': full_direct,
        'complete_continuum_pair_quadratures': full_pairs,
        'truncated_continuum_pair_quadratures': truncated_pairs,
        'truncated_continuum_V_square_at_X_1_independent_orders': truncated_squares,
        'whole_packet_continuum_pair_quadratures': whole_pairs,
        'whole_packet_continuum_exterior_squares_at_X_1_independent_orders': whole_squares,
        'scale_law': 'Every displayed continuum square at real X equals X^3 times its X=1 value.',
        'interpretation': 'Complete density cancels exactly since int w=0. Two different changes leave positive X^3 errors: truncating the density atoms to [X,2X], or retaining the complete active band but replacing W_X by whole-packet W_infinity.',
    }


def structural_checks():
    test_pairs = ((1.1, 1.3, 1.0), (1.6, 1.7, 1.0), (0.9, 1.2, 1.0),
                  (1.9, 2.3, 1.0))
    c = 3.14159
    homogeneity = [abs(pair_y(c * n, c * m, c * X) - c * pair_y(n, m, X))
                   for n, m, X in test_pairs]
    # Each zero is forced respectively by the lower cap, upper cap, or ratio.
    zeros = [(A0 * 0.9, 1.0, 1.0), (1.5, 2 * B0 * 1.1, 1.0),
             (1.0, math.exp(ELL) * 1.001, 1.0), (1.0, math.exp(ELL), 1.0)]
    zero_values = [pair_y(n, m, X) for n, m, X in zeros]
    norm = quad(lambda v: g(v) ** 2, -A, A, 24)
    assert abs(norm - 1) < 2e-12
    assert max(abs(value) for value in zero_values) < 1e-14
    assert max(homogeneity) < 1e-12
    return {'g_norm_squared_order_24': norm,
            'prepared_g_moments': {
                str(s): quad(lambda v: np.exp(s * v) * g(v), -A, A, 32)
                for s in (0, -0.5, 0.5)},
            'pair_zero_support_examples': [
                {'n': n, 'm': m, 'X': X, 'weight': value}
                for (n, m, X), value in zip(zeros, zero_values)],
            'homogeneity_scale': c,
            'largest_homogeneity_absolute_residual': max(homogeneity)}


def shift_density_checks():
    """Check continuum fixed-shift density H_X(h)=X^2 F(h/X)."""
    width = B0 - A0

    def cw(z):
        if z >= width:
            return 0.0
        return quad(lambda t: w(t) * w(t + z), A0, B0 - z, 48)

    def F(q):
        if q >= 2 * width:
            return 0.0
        return quad(lambda u: np.array([uu * cw(q / uu) for uu in u]),
                    max(1.0, q / width), 2, 48)

    def H_unit(q):
        lo = max(A0, q / (math.exp(ELL) - 1))
        hi = 2 * B0 - q
        if hi <= lo:
            return 0.0
        points = {lo, hi}
        for boundary in (A0, B0, 2 * A0, 2 * B0):
            for t in (boundary, boundary - q):
                if lo < t < hi:
                    points.add(t)
        points = sorted(points)
        return math.fsum(quad(
            lambda t: np.array([pair_y(tt, tt + q, 1.0) for tt in t]),
            ll, hh, 48) for ll, hh in zip(points[:-1], points[1:]))

    rows = []
    for q in (0.0, 0.05, 0.2, 0.45, 0.7, 0.95, 1.02):
        f, h = F(q), H_unit(q)
        assert abs(f - h) < 2e-10
        rows.append({'q': q, 'F_from_autocorrelation': f,
                     'H_1_q_from_pair_weight': h,
                     'absolute_identity_residual': abs(f - h)})
    return {
        'definition_C_w': 'integral w(t)w(t+z)dt',
        'definition_F': 'integral_1^2 u C_w(q/u)du',
        'definition_H': 'integral W_X(t,t+h)dt=X^2 F(h/X)',
        'F_zero_exact': '3/2, since integral w(t)^2dt=integral g(v)^2dv=1',
        'positive_shift_integral_exact': 'integral_0^infinity F(q)dq=(7/6)(integral w)^2=0',
        'support_upper_q': 2 * width,
        'samples': rows,
        'scope': 'Fixed small q identity checks; no singular-series asymptotic or prime-correlation bound is tested.',
    }


def run():
    start = time.perf_counter()
    structure = structural_checks()
    results = []
    for X in XS:
        result = sample(X)
        results.append(result)
        print(f'X={X:g} pp={result["prime_power_count"]} '
              f'D={result["diagonal_D"]:.9g} '
              f'C={result["signed_offdiagonal_C"]:.9g} '
              f'V2={result["direct_V_square_integral"]:.9g}', flush=True)
    continuum = continuum_checks()
    # At X=7/a0 the packet at n=7 exits the complete lower active support.
    transition_X = 7 / A0
    transition = [sample(transition_X * (1 + delta))
                  for delta in (-1e-6, 0.0, 1e-6)]
    upper_transition_X = 23 / (2 * B0)
    upper_transition = [sample(upper_transition_X * (1 + delta))
                        for delta in (-1e-6, 0.0, 1e-6)]
    shifts = shift_density_checks()
    record = {
        'date': '2026-10-03', 'prepared_for': 'Edward Baker',
        'model': 'GPT-6 (Codex); inherited configuration',
        'serving_variant': 'not exposed; not inferred',
        'reasoning_effort': 'not exposed; not inferred',
        'llm_acknowledgement': 'Prepared with substantial LLM assistance.',
        'status': 'FLOATING DIAGNOSTIC ONLY; no outward certificate, uniform numerical enclosure, or global prime-correlation estimate.',
        'scope': 'Exact dyadic pair weights, complete caps, shifted signed correlations, and continuum cancellation at small real X.',
        'normalization': {'a': A, 'ell': ELL, 'a0': A0, 'b0': B0,
                          'nu_exact': '146640624550936576/37921101075'},
        'formulas': {
            'w': 't^(-1/2) g(-log t), zero outside (a0,b0)',
            'V': 'sum Lambda(n) w(n/x)',
            'pair': 'sqrt(nm) integral_lo^hi exp(2v) g(v+delta) g(v-delta) dv',
            'pair_bounds': 'delta=log(m/n)/2, c=log(nm)/2; lo=max(-a+abs(delta),log X-c), hi=min(a-abs(delta),log(2X)-c)',
            'offdiagonal': '2 sum_(h>=1) sum_n Lambda(n)Lambda(n+h) W_X(n,n+h)',
            'complete_range': 'a0 X<n,m<2 b0 X, abs(log(n/m))<ell',
            'continuum': 'integral integral W_X(n,m) dn dm = integral_X^(2X) [x integral w]^2 dx = 0',
        },
        'structural_checks': structure, 'results': results,
        'continuum_checks': continuum, 'shift_density_checks': shifts,
        'lower_support_transition_near_X_7_over_a0': {
            'boundary_X': transition_X, 'relative_offsets': [-1e-6, 0, 1e-6],
            'results': transition,
            'interpretation': 'Noninteger real-X samples straddle a genuine support change; these samples do not establish a uniform numerical error bound.'},
        'upper_support_transition_near_X_23_over_2b0': {
            'boundary_X': upper_transition_X,
            'relative_offsets': [-1e-6, 0, 1e-6],
            'results': upper_transition,
            'interpretation': 'The packet at n=23 enters the complete upper active support.'},
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_executable': sys.executable,
        'python_version': platform.python_version(), 'numpy_version': np.__version__,
        'runtime_seconds': time.perf_counter() - start,
    }
    (ROOT / 'record.json').write_text(json.dumps(record, indent=2) + '\n')
    print(f'Complete continuum pair coefficient '
          f'{continuum["complete_continuum_pair_quadratures"][-1]["signed_double_integral_at_X_1"]:.3g}; '
          f'truncated coefficient '
          f'{continuum["truncated_continuum_V_square_at_X_1_independent_orders"]["40"]:.9g}', flush=True)
    print(f'Runtime {record["runtime_seconds"]:.3f} seconds', flush=True)


if __name__ == '__main__':
    run()
