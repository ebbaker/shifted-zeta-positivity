#!/usr/bin/env python3
"""Floating four-basis Chebyshev fit and exact signed smoothing identities."""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parent
BASE_SOURCE = ROOT.parent / 'selective_loss_dyadic_pairs_20261003' / 'diagnostic.py'
sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location('dyadic_base', BASE_SOURCE)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
A0, B0 = BASE.A0, BASE.B0
XS = (19.375, 53.625, 101.3, 201.75, 501.125)
SS = (1.0, 1.3, 1.7, 2.0)


def basis(u):
    return np.column_stack((np.ones_like(u), u, np.sqrt(u), np.log(u)))


def gprime(v):
    """Derivative of the factored polynomial g inside its compact support."""
    v = np.asarray(v)
    result = np.zeros_like(v, dtype=float)
    inside = np.abs(v) < BASE.A
    z = v[inside] ** 2
    P = 2689 - 215072 * z + 256 * z * z
    result[inside] = (-64 / BASE.SQRT_NU * (1 - 16 * z) ** 4
                     * ((1 - 176 * z) * P
                        + (1 - 16 * z) * (-430144 * z + 1024 * z * z)))
    return result


def wprime(t):
    t = np.asarray(t)
    result = np.zeros_like(t, dtype=float)
    inside = (t > A0) & (t < B0)
    z = -np.log(t[inside])
    result[inside] = -(gprime(z) + BASE.g(z) / 2) / t[inside] ** 1.5
    return result


def lambda_table(X):
    limit = math.ceil(2 * B0 * X)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    lambdas = np.zeros(limit + 1)
    for p in np.flatnonzero(sieve):
        n = int(p)
        while n <= limit:
            lambdas[n] = math.log(p)
            n *= int(p)
    return lambdas, np.cumsum(lambdas)


def quadrature(X, lo, hi, order):
    first = math.floor(X * lo) + 1
    last = math.ceil(X * hi) - 1
    breaks = np.r_[lo, np.arange(first, last + 1) / X, hi]
    breaks = np.unique(breaks)
    breaks = breaks[(breaks >= lo) & (breaks <= hi)]
    mids = (breaks[:-1] + breaks[1:]) / 2
    radii = (breaks[1:] - breaks[:-1]) / 2
    nodes, weights = BASE.gauss(order)
    u = (mids[:, None] + radii[:, None] * nodes).ravel()
    qw = (radii[:, None] * weights).ravel()
    return u, qw, breaks


def epsilon(X, u, psi):
    return psi[np.floor(X * u).astype(int)] - X * u


def fit(X, psi, order):
    u, weights, breaks = quadrature(X, A0, 2 * B0, order)
    phi = basis(u)
    eps = epsilon(X, u, psi)
    weighted_phi = np.sqrt(weights)[:, None] * phi
    weighted_eps = np.sqrt(weights) * eps
    coeff, _, rank, singular = np.linalg.lstsq(weighted_phi, weighted_eps,
                                              rcond=None)
    fitted = phi @ coeff
    residual = eps - fitted
    raw_norm = float(np.dot(weights, eps * eps))
    projected_norm = float(np.dot(weights, residual * residual))
    fit_norm = float(np.dot(weights, fitted * fitted))
    mids = (breaks[:-1] + breaks[1:]) / 2
    lengths = breaks[1:] - breaks[:-1]
    at_mid = epsilon(X, mids, psi)
    raw_exact_pieces = math.fsum(lengths * at_mid * at_mid
                                + X * X * lengths ** 3 / 12)
    condition = float(singular[0] / singular[-1])
    return {
        'quadrature_order': order, 'piece_count': len(breaks) - 1,
        'basis_order': ['1', 'u', 'sqrt(u)', 'log(u)'],
        'coefficients': coeff.tolist(), 'rank': int(rank),
        'weighted_design_singular_values': singular.tolist(),
        'weighted_design_condition': condition,
        'Gram_condition_from_singular_values': condition * condition,
        'raw_epsilon_norm_squared': raw_norm,
        'raw_epsilon_norm_squared_direct_piece_formula': raw_exact_pieces,
        'fit_norm_squared': fit_norm,
        'projected_epsilon_norm_squared': projected_norm,
        'projected_norm_over_X_log2X': projected_norm / (X * math.log(2 * X)),
        'orthogonality_moments': (phi.T @ (weights * residual)).tolist(),
        'Pythagorean_absolute_residual': abs(raw_norm - fit_norm - projected_norm),
        'raw_norm_vs_piece_formula_absolute': abs(raw_norm - raw_exact_pieces),
    }


def response(X, s, psi, lambdas, coefficients, order):
    lo, hi = max(A0, A0 * s), min(2 * B0, B0 * s)
    u, weights, breaks = quadrature(X, lo, hi, order)
    kernel = -wprime(u / s) / s
    eps = epsilon(X, u, psi)
    phi = basis(u)
    raw = float(np.dot(weights, eps * kernel))
    fitted = float(np.dot(weights, (eps - phi @ coefficients) * kernel))
    null = phi.T @ (weights * kernel)
    n = np.flatnonzero(lambdas)
    direct = float(np.dot(lambdas[n], BASE.w(n / (X * s))))
    return {
        's': s, 'quadrature_order': order, 'piece_count': len(breaks) - 1,
        'V_Xs_direct_prime_power_sum': direct,
        'T_raw_epsilon': raw, 'T_projected_epsilon': fitted,
        'T_each_null_basis': null.tolist(),
        'direct_vs_T_raw_absolute': abs(direct - raw),
        'direct_vs_T_projected_absolute': abs(direct - fitted),
        'T_raw_vs_T_projected_absolute': abs(raw - fitted),
    }


def sample(X):
    lambdas, psi = lambda_table(X)
    fits = [fit(X, psi, order) for order in (16, 24)]
    assert fits[-1]['rank'] == 4
    coeff = np.array(fits[-1]['coefficients'])
    responses = [response(X, s, psi, lambdas, coeff, order)
                 for s in SS for order in (24, 32)]
    assert max(r['direct_vs_T_projected_absolute'] for r in responses) < 2e-8
    assert max(abs(v) for r in responses for v in r['T_each_null_basis']) < 2e-11
    return {'X': X, 'fit_orders': fits, 'responses': responses,
            'fit_order_projected_norm_difference_absolute': abs(
                fits[0]['projected_epsilon_norm_squared']
                - fits[1]['projected_epsilon_norm_squared']),
            'max_integer_sieved': len(lambdas) - 1}


def run():
    start = time.perf_counter()
    samples = []
    for X in XS:
        row = sample(X)
        samples.append(row)
        fit_row = row['fit_orders'][-1]
        print(f'X={X:g} raw={fit_row["raw_epsilon_norm_squared"]:.9g} '
              f'projected={fit_row["projected_epsilon_norm_squared"]:.9g} '
              f'Gram_cond={fit_row["Gram_condition_from_singular_values"]:.6g}',
              flush=True)
    record = {
        'date': '2026-10-03', 'prepared_for': 'Edward Baker',
        'model': 'GPT-6 (Codex); inherited configuration',
        'llm_acknowledgement': 'Prepared with substantial LLM assistance.',
        'serving_variant': 'not exposed; not inferred',
        'reasoning_effort': 'not exposed; not inferred',
        'status': 'FLOATING DIAGNOSTIC ONLY; no outward, interval, asymptotic, global arithmetic, or RH certificate.',
        'domain_u': [A0, 2 * B0],
        'formulas': {
            'epsilon': 'psi(Xu)−Xu',
            'T': '−s^(-1) integral epsilon(u) w_prime(u/s)du=V(Xs)',
            'fit': 'L2 orthogonal projection on span{1,u,sqrt(u),log(u)}',
            'w_prime': '−t^(-3/2)[g_prime(−log t)+g(−log t)/2]',
            'nullspace': 'T annihilates each of 1,u,sqrt(u),log(u), by the three prepared moments and compact endpoints.',
        },
        'method': 'All integer breakpoints n/X and kernel caps; weighted SVD least squares via numpy.linalg.lstsq, never inverse Gram.',
        'samples': samples,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'base_source_sha256': hashlib.sha256(BASE_SOURCE.read_bytes()).hexdigest(),
        'python_executable': sys.executable, 'python_version': platform.python_version(),
        'numpy_version': np.__version__, 'runtime_seconds': time.perf_counter() - start,
    }
    (ROOT / 'fitted_psi_record.json').write_text(json.dumps(record, indent=2) + '\n')
    print(f'Runtime {record["runtime_seconds"]:.3f}s', flush=True)


if __name__ == '__main__':
    run()
