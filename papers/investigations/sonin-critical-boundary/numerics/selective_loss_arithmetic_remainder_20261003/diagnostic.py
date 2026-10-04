#!/usr/bin/env python3
"""Small actual arithmetic remainder versus singular-series model, floating."""
from collections import defaultdict
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
# Reuse the previous definitions without writing a cache into its directory.
sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location('dyadic_base', BASE_SOURCE)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
A0, B0, A = BASE.A0, BASE.B0, BASE.A
WIDTH = B0 - A0
QMAX = 2 * WIDTH
REGIONS = ('lower', 'bulk', 'upper')
REGION_BOUNDS = (A0, B0, 2 * A0, 2 * B0)
XS = (19.375, 53.625, 101.3, 201.75, 501.125)
C2 = 0.660161815846869
C2_SOURCE = 'https://www.itc.u-tokyo.ac.jp/Annual_Report/no12/AnnualReportNo12.pdf'
GAMMA = 0.5772156649015329
A_SS = 2 - GAMMA - math.log(2 * math.pi)
F0 = 1.5
C_D = 2 * math.log(2) - 0.75


def cw_array(z, order=40):
    z = np.asarray(z, dtype=float)
    result = np.zeros_like(z)
    active = (z >= 0) & (z < WIDTH)
    zz = z[active]
    nodes, weights = BASE.gauss(order)
    radius = (WIDTH - zz) / 2
    t = (A0 + B0 - zz[:, None]) / 2 + radius[:, None] * nodes
    result[active] = radius * np.sum(BASE.w(t) * BASE.w(t + zz[:, None])
                                    * weights[None, :], axis=1)
    return result


def f_array(q, order=40):
    q = np.asarray(q, dtype=float)
    result = np.zeros_like(q)
    active = (q >= 0) & (q < QMAX)
    qq = q[active]
    nodes, weights = BASE.gauss(order)
    lo = np.maximum(1, qq / WIDTH)
    radius = (2 - lo) / 2
    u = (2 + lo[:, None]) / 2 + radius[:, None] * nodes
    cvals = cw_array((qq[:, None] / u).ravel(), order).reshape(u.shape)
    result[active] = radius * np.sum(u * cvals * weights[None, :], axis=1)
    return result


def pair_array(n, m, X, order=24):
    n, m = np.asarray(n), np.asarray(m)
    center = (np.log(n) + np.log(m)) / 2
    delta = (np.log(m) - np.log(n)) / 2
    lo = np.maximum(-A + np.abs(delta), math.log(X) - center)
    hi = np.minimum(A - np.abs(delta), math.log(2 * X) - center)
    radius = np.maximum(0, hi - lo) / 2
    nodes, weights = BASE.gauss(order)
    v = (lo + hi)[:, None] / 2 + radius[:, None] * nodes
    return np.sqrt(n * m) * radius * np.sum(
        np.exp(2 * v) * BASE.g(v + delta[:, None])
        * BASE.g(v - delta[:, None]) * weights[None, :], axis=1)


def h_blocks(qs, order=40):
    """Dimensionless H_1(q) partitioned by both packet-region caps."""
    qs = np.asarray(qs, dtype=float)
    nodes, weights = BASE.gauss(order)
    result = {}
    for i, name_n in enumerate(REGIONS):
        for j in range(i, len(REGIONS)):
            name_m = REGIONS[j]
            lo = np.maximum.reduce((np.full_like(qs, REGION_BOUNDS[i]),
                                    REGION_BOUNDS[j] - qs,
                                    qs / math.expm1(2 * A)))
            hi = np.minimum(REGION_BOUNDS[i + 1], REGION_BOUNDS[j + 1] - qs)
            radius = np.maximum(0, hi - lo) / 2
            t = (lo + hi)[:, None] / 2 + radius[:, None] * nodes
            # Zero-radius rows can have t<=0 outside the support; replace them.
            t[radius == 0, :] = 1
            wts = pair_array(t.ravel(), (t + qs[:, None]).ravel(), 1)
            wts = wts.reshape(t.shape)
            result[f'{name_n}/{name_m}'] = radius * np.sum(
                wts * weights[None, :], axis=1)
    return result


def singular_series(h):
    if h % 2:
        return 0.0
    out = 2 * C2
    remaining = h
    while remaining % 2 == 0:
        remaining //= 2
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            out *= (p - 1) / (p - 2)
            while remaining % p == 0:
                remaining //= p
        p += 2
    if remaining > 2:
        out *= (remaining - 1) / (remaining - 2)
    return out


def kernel_constants(order):
    # Cw(z)=1+O(z^2); subtracting 1 makes this integral regular at zero.
    KC = BASE.quad(lambda z: (cw_array(z, order) - 1) / z,
                   0, WIDTH, order) + math.log(WIDTH)
    JC = 1 + KC
    IF = F0 * JC + C_D
    cF = A_SS * F0 / 2 - IF / 2
    beta = C_D + 2 * cF - F0
    # Independently use the same regularized identity directly for F.
    IF_direct = F0 * (1 + math.log(QMAX)) + BASE.quad(
        lambda q: (f_array(q, order) - F0) / q, 0, QMAX, order)
    return {'order': order, 'K_C': KC, 'J_C': JC,
            'I_F_via_Cw': IF, 'I_F_direct_regularized_F': IF_direct,
            'I_F_identity_absolute_residual': abs(IF - IF_direct),
            'c_F': cF, 'beta_model': beta}


def actual_sample(X):
    rows = BASE.prime_powers(X)
    ns = np.array([row['n'] for row in rows])
    lambdas = np.array([row['Lambda'] for row in rows])
    max_h = math.ceil(QMAX * X) - 1
    hs = np.arange(1, max_h + 1)
    actual_h = defaultdict(list)
    actual_blocks = defaultdict(list)
    diag_blocks = defaultdict(list)
    diagonals = lambdas ** 2 * pair_array(ns, ns, X)
    for row, d in zip(rows, diagonals):
        diag_blocks[row['packet_region']].append(float(d))
    i, j = np.triu_indices(len(ns), 1)
    ww = pair_array(ns[i], ns[j], X)
    actual_terms = lambdas[i] * lambdas[j] * ww
    for ii, jj, term in zip(i, j, actual_terms):
        if term:
            h = int(ns[jj] - ns[ii])
            assert 1 <= h <= max_h
            actual_h[h].append(float(term))
            block = f"{rows[ii]['packet_region']}/{rows[jj]['packet_region']}"
            actual_blocks[block].append(float(2 * term))
    ah = np.array([math.fsum(actual_h[int(h)]) for h in hs])
    ss = np.array([singular_series(int(h)) for h in hs])
    F = f_array(hs / X, 40)
    F32 = f_array(hs / X, 32)
    H = X * X * F
    baseline = ss * H
    residual_h = 2 * (ah - baseline)
    hcaps = h_blocks(hs / X, 40)
    hcaps32 = h_blocks(hs / X, 32)
    hsum = sum(hcaps.values(), np.zeros(len(hs)))
    model_blocks = {name: float(2 * X * X * np.dot(ss, values))
                    for name, values in hcaps.items()}
    residual_blocks = {name: math.fsum(actual_blocks[name]) - model
                       for name, model in model_blocks.items()}
    D = math.fsum(diagonals)
    C = 2 * math.fsum(ah)
    C_SS = 2 * math.fsum(baseline)
    R = math.fsum(residual_h)
    V2, pieces = BASE.direct_square(X, rows)
    scale = X * X
    checks = {
        'actual_variance_decomposition_absolute': abs(V2 - D - C_SS - R),
        'actual_R_direct_vs_shifted_absolute': abs((V2 - D - C_SS) - R),
        'R_shifted_vs_caps_absolute': abs(R - math.fsum(residual_blocks.values())),
        'largest_H_over_X2_caps_vs_F_absolute': float(np.max(np.abs(hsum - F))),
        'largest_F32_vs_F40_absolute': float(np.max(np.abs(F32 - F))),
        'largest_cap32_vs_cap40_absolute': max(float(np.max(np.abs(
            hcaps[name] - hcaps32[name]))) for name in hcaps),
    }
    assert checks['actual_variance_decomposition_absolute'] < 2e-9 * scale
    assert checks['R_shifted_vs_caps_absolute'] < 2e-9 * scale
    assert checks['largest_H_over_X2_caps_vs_F_absolute'] < 2e-9
    return {
        'X': X, 'max_integer': int(max(ns)), 'prime_power_count': len(rows),
        'max_shift': max_h, 'packet_endpoint_piece_count': pieces,
        'cap_counts': {name: sum(row['packet_region'] == name for row in rows)
                       for name in REGIONS},
        'D_actual_diagonal': D, 'C_actual_offdiagonal': C,
        'C_SS_model_offdiagonal': C_SS,
        'D_actual_plus_C_SS_model': D + C_SS,
        'R_actual_signed_remainder': R,
        'R_positive_part': max(0, R),
        'V_actual_variance_direct': V2,
        'actual_variance_over_X2': V2 / scale,
        'model_D_plus_C_SS_over_X2': (D + C_SS) / scale,
        'R_over_X2': R / scale,
        'R_positive_over_X2_log2X': max(0, R) / (scale * math.log(2 * X)),
        'positive_per_shift_residual_mass': math.fsum(v for v in residual_h if v > 0),
        'negative_per_shift_residual_mass': math.fsum(v for v in residual_h if v < 0),
        'odd_shift_actual_mass': 2 * math.fsum(ah[hs % 2 == 1]),
        'even_shift_actual_mass': 2 * math.fsum(ah[hs % 2 == 0]),
        'D_log_density_model': scale * (F0 * math.log(X) + C_D),
        'D_log_density_model_plus_C_SS_over_X2': (
            scale * (F0 * math.log(X) + C_D) + C_SS) / scale,
        'signed_cap_blocks': {
            name: {'actual_offdiagonal': math.fsum(actual_blocks[name]),
                   'SS_model_offdiagonal': model_blocks[name],
                   'actual_signed_remainder': residual_blocks[name]}
            for name in model_blocks},
        'diagonal_by_cap': {name: math.fsum(diag_blocks[name]) for name in REGIONS},
        'per_shift': [
            {'h': int(h), 'SS_h': float(ss_h), 'actual_C_h_without_two': float(a_h),
             'H_X_h': float(h_h), 'SS_h_H_X_h': float(b_h),
             'signed_residual_with_two': float(r_h)}
            for h, ss_h, a_h, h_h, b_h, r_h in zip(hs, ss, ah, H, baseline, residual_h)],
        'checks': checks,
    }


def run():
    start = time.perf_counter()
    constants = [kernel_constants(order) for order in (32, 48, 64)]
    assert constants[-1]['I_F_identity_absolute_residual'] < 2e-9
    samples = []
    for X in XS:
        row = actual_sample(X)
        samples.append(row)
        print(f'X={X:g} pp={row["prime_power_count"]} '
              f'V/X2={row["actual_variance_over_X2"]:.9g} '
              f'(D+SS)/X2={row["model_D_plus_C_SS_over_X2"]:.9g} '
              f'R/X2={row["R_over_X2"]:.9g}', flush=True)
    record = {
        'date': '2026-10-03', 'prepared_for': 'Edward Baker',
        'model': 'GPT-6 (Codex); inherited configuration',
        'serving_variant': 'not exposed; not inferred',
        'reasoning_effort': 'not exposed; not inferred',
        'llm_acknowledgement': 'Prepared with substantial LLM assistance.',
        'status': 'FLOATING DIAGNOSTIC ONLY; no outward enclosure, continuous-window certificate, global signed bound, or growth inference.',
        'singular_series_constant': {'C2_decimal': C2,
                                     'decimal_provenance': C2_SOURCE,
                                     'note': 'Published decimal used as floating input; no infinite product enclosure is claimed.'},
        'normalization': {'a0': A0, 'b0': B0, 'F0': F0, 'A_SS': A_SS, 'C_D': C_D},
        'formulas': {
            'R': '2 sum_h [sum_n Lambda(n)Lambda(n+h)W_X(n,n+h)−SS(h)H_X(h)]',
            'H': 'X^2 F(h/X)',
            'variance': 'V_square=D+C_SS+R',
            'J_C': '1+log(width)+integral_0^width [C_w(q)−1]dq/q',
            'I_F': '(3/2)J_C+(2log2−3/4)',
            'c_F': 'A_SS F0/2−I_F/2',
            'beta_model': 'C_D+2c_F−F0=F0(−gamma−log(2pi)−K_C)',
            'D_density_log_model': 'X^2[(3/2)log X+2log2−3/4]',
        },
        'kernel_constant_orders': constants,
        'samples': samples,
        'scope': 'Actual complete prime-power remainder at five small real shells; singular-series model constants are model calculations, not actual remainder estimates.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'base_source_path': str(BASE_SOURCE),
        'base_source_sha256': hashlib.sha256(BASE_SOURCE.read_bytes()).hexdigest(),
        'python_executable': sys.executable, 'python_version': platform.python_version(),
        'numpy_version': np.__version__, 'runtime_seconds': time.perf_counter() - start,
    }
    (ROOT / 'record.json').write_text(json.dumps(record, indent=2) + '\n')
    print(f'beta_model={constants[-1]["beta_model"]:.12g}; '
          f'runtime={record["runtime_seconds"]:.3f}s', flush=True)


if __name__ == '__main__':
    run()
