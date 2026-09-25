#!/usr/bin/env python3
"""Small floating controls for electric-current recentering and a gapped bound.

Prepared for Edward Baker with substantial GPT-6 (Codex) assistance, 2026-09-25.
Exact deployed variant and reasoning effort unavailable. These are Haar and
prescribed radial-density diagnostics, not a full interacting Wilson sample.
Analytical proofs, not this script, establish the limiting statements.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np


def profile(x, right=False):
    x = np.asarray(x)
    out = np.zeros_like(x, dtype=complex)
    inside = abs(x) < 1.3
    z = x[inside]
    phase = -0.23 if right else 0.37
    out[inside] = np.exp(-1 / (1 - (z / 1.3) ** 2) + 1j * phase * z)
    if right:
        out *= 1 + (0.2 + 0.1j) * x
    return out


def sine_limit(y, right=False, order=700):
    order = max(order, math.ceil(4 * float(np.max(y))))
    z, weights = np.polynomial.legendre.leggauss(order)
    x, weights = 1.3 * z, 1.3 * weights
    amplitude = weights * np.exp(x / 2) * profile(x, right)
    out = np.empty(len(y), complex)
    for start in range(0, len(y), 128):
        part = slice(start, start + 128)
        out[part] = math.sqrt(2 / np.pi) * (np.sin(y[part, None] * np.exp(x)[None, :]) @ amplitude)
    return out


def packet_coefficients(scale, right=False):
    labels = np.arange(1, math.ceil(scale * math.exp(1.3)) + 1)
    coefficients = profile(np.log(labels / scale), right) / np.sqrt(labels)
    return labels, coefficients


def recentered(y, scale, winding=1, right=False, weighted=False):
    labels, coefficients = packet_coefficients(scale, right)
    angle = 2 * np.arctan(y / (2 * scale))
    out = np.empty(len(y), complex)
    for start in range(0, len(y), 128):
        part = slice(start, start + 128)
        out[part] = np.sin(angle[part, None] * (winding * labels)[None, :]) @ coefficients
    out *= math.sqrt(2 / (np.pi * scale)) / np.sqrt(1 + (y / (2 * scale)) ** 2)
    if weighted:
        rho = (1 + 0.35 * np.cos(angle) + 0.2 * np.cos(2 * angle)) / 0.9
        out *= np.sqrt(rho / (1.55 / 0.9))
    return out


def total_weighted_norm(scale, winding):
    labels, coefficients = packet_coefficients(scale)
    c = np.zeros(winding * labels[-1] + 1, complex)
    c[winding * labels] = coefficients / math.sqrt(1.55 / 0.9)
    # All active labels exceed 2 at the scales used, so the Hankel term is zero.
    return float((np.vdot(c, c) / 0.9
                  + 2 * (0.175 / 0.9) * np.vdot(c[1:], c[:-1]).real
                  + 2 * (0.1 / 0.9) * np.vdot(c[2:], c[:-2]).real).real)


def primes_to(bound):
    sieve = np.ones(bound + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(bound) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return np.flatnonzero(sieve)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    nodes, weights = np.polynomial.legendre.leggauss(12)
    starts = np.arange(0, 160, 0.5)
    y = (starts[:, None] + 0.25 * (nodes + 1)).ravel()
    yw = np.tile(0.25 * weights, len(starts))
    xn, xw = np.polynomial.legendre.leggauss(700)
    x, xw = 1.3 * xn, 1.3 * xw
    norm = float(np.dot(xw, abs(profile(x)) ** 2))
    limit = sine_limit(y)
    refined = sine_limit(y, order=900)
    checks = []

    def check(label, discrepancy, tolerance):
        checks.append(dict(label=label, absolute_error=float(abs(discrepancy)),
                           tolerance=tolerance, passed=bool(abs(discrepancy) <= tolerance)))

    check('sine quadrature refinement', np.sqrt(np.dot(yw, abs(limit - refined) ** 2)), 1e-9)
    check('truncated sine Plancherel norm', np.dot(yw, abs(limit) ** 2) - norm, 2e-8)
    scales = [16, 64, 256, 1024]
    convergence = []
    for weighted in (False, True):
        errors = []
        for scale in scales:
            values = recentered(y, scale, weighted=weighted)
            errors.append(float(np.sqrt(np.dot(yw, abs(values - limit) ** 2))))
        convergence.append(dict(label='identity recentering', weighted=weighted,
                                scales=scales, local_L2_errors=errors))
        check(f'identity strong-limit local control weighted={weighted}', errors[-1], 2e-5)

    branch_controls = []
    for a in (2, 3, 5):
        target = sine_limit(a * y)
        target_right = sine_limit(a * y, right=True)
        # The independent arithmetic mixed integral uses translated log inputs.
        arithmetic = np.dot(xw, np.conj(profile(x)) * profile(x - np.log(a), True)) / np.sqrt(a)
        check(f'mixed arithmetic coefficient a={a}', np.dot(yw, np.conj(limit) * target_right) - arithmetic, 2e-8)
        for weighted in (False, True):
            values = recentered(y, 1024, winding=a, weighted=weighted)
            local_error = float(np.sqrt(np.dot(yw, abs(values - target) ** 2)))
            check(f'wound weak-limit local control a={a} weighted={weighted}', local_error, 2e-5)
            retained = float(np.dot(yw, abs(values) ** 2))
            if weighted:
                total = total_weighted_norm(1024, a)
                rho_a_ratio = (1.2 if a == 2 else 1.0) / 1.55
            else:
                _, c = packet_coefficients(1024)
                total = float(np.vdot(c, c).real)
                rho_a_ratio = 1.0
            predicted_loss = (rho_a_ratio - 1 / a) * norm
            check(f'escaped winding norm a={a} weighted={weighted}', (total - retained) - predicted_loss, 2e-6)
            branch_controls.append(dict(winding=a, weighted=weighted, total_norm_squared=total,
                                        norm_squared_in_0_160=retained,
                                        predicted_escaped_norm_squared=predicted_loss))

    delta = 0.6
    gapped_bounds = []
    for cutoff in (10, 100, 1000, 10000):
        p = primes_to(cutoff)
        lam = np.log(p)
        # Unit fixed coefficient. Dropping all other positive terms gives this
        # analytically proved lower bound; no finite matrix proves divergence.
        lower = delta + np.sum(delta * lam / (delta + lam))
        gapped_bounds.append(dict(cutoff=cutoff, prime_count=len(p), delta=delta,
                                  normalized_lower_bound=float(lower)))

    record = dict(date='2026-09-25', prepared_for='Edward Baker', model='GPT-6 (Codex)',
                  deployed_variant='unavailable', reasoning_effort='unavailable',
                  llm_assistance=True, status='floating diagnostics, not limiting proofs or Wilson samples',
                  python=platform.python_version(), numpy=np.__version__,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  parameters=dict(profile_support=[-1.3, 1.3], scales=scales, y_cutoff=160,
                                  y_panel_width=0.5, y_panel_order=12, log_input_order=700,
                                  refinement_order=900, prescribed_density='(1+0.35*cos(theta)+0.2*cos(2*theta))/0.9'),
                  norm_squared=norm, check_count=len(checks), all_passed=all(c['passed'] for c in checks),
                  checks=checks, convergence=convergence, branch_controls=branch_controls,
                  gapped_lower_bounds=gapped_bounds)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(dict(check_count=record['check_count'], all_passed=record['all_passed'],
                          failed=[c for c in checks if not c['passed']]), indent=2))
    return 0 if record['all_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
