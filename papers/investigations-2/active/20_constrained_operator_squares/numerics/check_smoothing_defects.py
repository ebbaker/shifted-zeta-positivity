#!/usr/bin/env python3
"""Exact four-site CAR checks for investigation 20; standard library only.

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6.1-sol; reasoning effort: ultra.
This validates finite algebra, not a continuum theorem or theta certificate.
"""

import argparse
import hashlib
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path

M = 4
DIM = 1 << M


def add(*matrices):
    out = {}
    for matrix in matrices:
        for key, value in matrix.items():
            out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(value, matrix):
    return {key: value * entry for key, entry in matrix.items() if value * entry}


def adj(matrix):
    return {(j, i): value for (i, j), value in matrix.items()}


def mul(a, b):
    out = {}
    rows = {}
    for (k, j), value in b.items():
        rows.setdefault(k, []).append((j, value))
    for (i, k), value in a.items():
        for j, other in rows.get(k, []):
            key = (i, j)
            out[key] = out.get(key, F(0)) + value * other
    return {key: value for key, value in out.items() if value}


def sub(a, b):
    return add(a, scale(-1, b))


def ann(site):
    return {(state ^ (1 << site), state): F((-1) ** ((state & ((1 << site) - 1)).bit_count()))
            for state in range(DIM) if state & (1 << site)}


def translation_image(state, step):
    occupied = [j for j in range(M) if state & (1 << j)]
    moved = [(j + step) % M for j in occupied]
    inversions = sum(moved[i] > moved[j] for i in range(len(moved))
                     for j in range(i + 1, len(moved)))
    return sum(1 << j for j in moved), F((-1) ** inversions)


def alpha(matrix, step):
    images = [translation_image(state, step) for state in range(DIM)]
    return {(images[i][0], images[j][0]): images[i][1] * images[j][1] * value
            for (i, j), value in matrix.items()}


def channel(matrix, weights):
    return add(*(scale(weights[j], alpha(matrix, j)) for j in range(M)))


def convolution(a, b):
    return [sum((a[j] * b[(i - j) % M] for j in range(M)), F(0)) for i in range(M)]


def diag(matrix, state):
    assert all(i == j for i, j in matrix)
    return matrix.get((state, state), F(0))


def frac(value):
    return str(value)


def main(output):
    identity = {(i, i): F(1) for i in range(DIM)}
    c = [ann(j) for j in range(M)]
    n = [mul(adj(op), op) for op in c]
    checks = {}
    car = all(add(mul(c[i], adj(c[j])), mul(adj(c[j]), c[i])) ==
              (identity if i == j else {}) and
              add(mul(c[i], c[j]), mul(c[j], c[i])) == {}
              for i in range(M) for j in range(M))
    checks['canonical_anticommutation'] = car
    checks['translation_on_annihilation'] = all(alpha(c[j], 1) == c[(j + 1) % M]
                                                for j in range(M))
    # This is an exact time slice of exp(t(alpha_1+alpha_-1-2I)), t=log(2)/2.
    p = [F(9, 16), F(3, 16), F(1, 16), F(3, 16)]
    p2 = convolution(p, p)
    fourier_modes = [([F(1)] * M, F(1), F(0)),
                     ([F(1), F(0), F(-1), F(0)], F(1, 2), F(-2)),
                     ([F(0), F(1), F(0), F(-1)], F(1, 2), F(-2)),
                     ([F(1), F(-1), F(1), F(-1)], F(1, 4), F(-4))]
    checks['heat_kernel_fourier_eigenvalues'] = all(convolution(p, mode) == [eigen * value for value in mode]
                                                   for mode, eigen, generator_eigen in fourier_modes)
    checks['heat_generator_fourier_eigenvalues'] = all(
        [mode[(j + 1) % M] + mode[(j - 1) % M] - 2 * mode[j] for j in range(M)] ==
        [generator_eigen * value for value in mode]
        for mode, eigen, generator_eigen in fourier_modes)
    a = add(c[0], adj(c[1]))
    b = add(c[2], scale(F(2), adj(c[3])))
    pa, pb = channel(a, p), channel(b, p)
    covariance = sub(channel(mul(adj(a), b), p), mul(adj(pa), pb))
    double = {}
    for j in range(M):
        for k in range(M):
            da = sub(alpha(a, j), alpha(a, k))
            db = sub(alpha(b, j), alpha(b, k))
            double = add(double, scale(p[j] * p[k] / 2, mul(adj(da), db)))
    checks['noncommuting_cross_covariance_double_average'] = covariance == double
    ordinary = sub(channel(mul(adj(a), a), p), mul(adj(pa), pa))
    centered = add(*(scale(p[j], mul(adj(sub(alpha(a, j), pa)),
                                    sub(alpha(a, j), pa))) for j in range(M)))
    checks['noncommuting_covariance_centered_squares'] = ordinary == centered
    checks['heat_channel_composition'] = channel(channel(a, p), p) == channel(a, p2)
    pc = channel(c[0], p)
    kappa = sum((value * value for value in p), F(0))
    checks['smoothed_fields_anticommutator'] = add(mul(pc, adj(pc)), mul(adj(pc), pc)) == scale(kappa, identity)

    q = {}
    normal_local = []
    for x in range(M):
        weights = [p[(j - x) % M] for j in range(M)]
        rho = add(*(scale(weights[j], n[j]) for j in range(M)))
        normal = sub(mul(rho, rho), add(*(scale(weights[j] ** 2, n[j]) for j in range(M))))
        normal_local.append(normal)
        q = add(q, normal)
        explicit = add(*(scale(weights[j] * weights[k], mul(n[j], n[k]))
                         for j in range(M) for k in range(M) if j != k))
        checks[f'normal_order_local_{x}'] = normal == explicit
    q_pair = add(*(scale(p2[(j - k) % M], mul(n[j], n[k]))
                   for j in range(M) for k in range(M) if j != k))
    checks['independent_smoothing_pair_semigroup'] = q == q_pair
    raw_contact = add(*(sub(mul(n[j], n[j]), n[j]) for j in range(M)))
    checks['common_smoothing_contact_is_zero'] = raw_contact == {} and channel(raw_contact, p) == {}
    values = [diag(q, state) for state in range(DIM)]
    n2_values = [values[state] for state in range(DIM) if state.bit_count() == 2]
    checks['independent_normal_order_nonnegative_all_sectors'] = min(values) == 0
    checks['independent_normal_order_positive_two_particle_sector'] = min(n2_values) > 0
    normal_covariance_full = -diag(normal_local[0], DIM - 1)
    checks['normal_ordered_covariance_has_negative_example'] = normal_covariance_full < 0

    # D^2=L and tr_spin(D)=0 imply tr_spin exp(sD)=sum (s^2 L)^m/(2m)!.
    trace_coeff = [F(1, factorial(2 * m)) for m in range(4)]
    heat_coeff = [F(1, factorial(m)) for m in range(4)]
    matched_second_trace_coeff = [F(2 ** m, factorial(2 * m)) for m in range(4)]
    gaussian_even_moments = [F(factorial(2 * m), factorial(m)) for m in range(4)]
    gaussian_coeff = [trace_coeff[m] * gaussian_even_moments[m] for m in range(4)]
    spin_j = {(0, 1): F(1), (1, 0): F(-1)}
    spin_power = {(0, 0): F(1), (1, 1): F(1)}
    spin_traces = []
    for power in range(7):
        spin_traces.append(sum((spin_power.get((j, j), F(0)) for j in range(2)), F(0)) / 2)
        spin_power = mul(spin_power, spin_j)
    checks['two_by_two_spin_trace_even_powers'] = spin_traces == [F(1), F(0), F(-1), F(0), F(1), F(0), F(-1)]
    checks['finite_spin_trace_differs_at_quadratic_order'] = trace_coeff[1] != heat_coeff[1]
    checks['matching_quadratic_scale_still_fails_quartic'] = matched_second_trace_coeff[1] == heat_coeff[1] and matched_second_trace_coeff[2] != heat_coeff[2]
    checks['gaussian_wave_average_matches_heat_through_degree_six'] = gaussian_coeff == heat_coeff
    assert all(checks.values()), checks
    record = {
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'recorded_on': '2026-10-14',
        'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial derivation and exact-checker assistance',
        'model': 'gpt-6.1-sol',
        'reasoning_effort': 'ultra',
        'arithmetic': 'Python standard-library fractions.Fraction; no floating point',
        'scope': 'Finite four-site CAR algebra and low-order Clifford moments; no continuum or theta certificate',
        'sites': M, 'fock_dimension': DIM,
        'heat_generator': 'alpha_1+alpha_-1-2I', 'heat_time': 'log(2)/2',
        'heat_weights': list(map(frac, p)), 'doubled_time_weights': list(map(frac, p2)),
        'self_contraction_kappa': frac(kappa),
        'checks': checks,
        'integrated_independent_pair_two_particle_range': [frac(min(n2_values)), frac(max(n2_values))],
        'integrated_independent_pair_full_occupancy': frac(values[-1]),
        'normal_ordered_local_covariance_full_occupancy': frac(normal_covariance_full),
        'normalized_spin_trace_coefficients_in_s_squared_L': list(map(frac, trace_coeff)),
        'heat_coefficients_in_s_squared_L': list(map(frac, heat_coeff)),
        'second_order_matched_spin_trace_coefficients': list(map(frac, matched_second_trace_coeff)),
        'gaussian_wave_average_coefficients': list(map(frac, gaussian_coeff)),
    }
    encoded = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if output:
        Path(output).write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    main(parser.parse_args().output)
