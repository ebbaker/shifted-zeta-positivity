#!/usr/bin/env python3
"""Algebra and asymptotic controls for SU(2) character source channels.

Prepared for Edward Baker with GPT-6 (Codex) assistance, 2026-09-25.
Reasoning effort not exposed or inferred. Prescribed marginal densities only;
this does not sample the interacting YM measure or certify an infinite limit.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np


def bump(x, center, radius, phase):
    x = np.asarray(x)
    v = (x - center) / radius
    out = np.zeros_like(x, dtype=complex)
    inside = np.abs(v) < 1
    out[inside] = np.exp(-1 / (1 - v[inside]**2)) * np.exp(1j * phase * x[inside])
    return out


def f(x):
    return bump(x, 0.0, 1.3, 0.37)


def minus_i_fprime(x):
    x = np.asarray(x)
    v = x / 1.3
    out = np.zeros_like(x, dtype=complex)
    inside = np.abs(v) < 1
    derivative_factor = -2 * x[inside] / 1.3**2 / (1 - v[inside]**2)**2 + 0.37j
    out[inside] = -1j * f(x[inside]) * derivative_factor
    return out


def g(x):
    return (1 + 0.1j * np.asarray(x)) * bump(x, 0.2, 1.3, -0.23)


def rho(theta, haar=False):
    if haar:
        return np.ones_like(np.asarray(theta), dtype=float)
    return (1 + 0.35 * np.cos(theta) + 0.2 * np.cos(2 * theta)) / 0.9


def t(k, haar=False):
    if haar:
        return float(k == 0)
    return {0: 1 / 0.9, 1: 0.35 / 1.8, 2: 0.2 / 1.8}.get(abs(k), 0.0)


def gram(a, b, haar=False):
    # Index zero is unused. Toeplitz and Hankel parts are evaluated separately.
    size = max(len(a), len(b))
    a = np.pad(a, (0, size - len(a)))
    b = np.pad(b, (0, size - len(b)))
    result = t(0, haar) * np.vdot(a, b)
    for k in (1, 2):
        result += t(k, haar) * (np.vdot(a[k:], b[:-k]) + np.vdot(a[:-k], b[k:]))
        for n in range(1, k):
            if n < size and k - n < size:
                result -= t(k, haar) * np.conj(a[n]) * b[k - n]
    return result


def packet(scale, function, alpha=0.0, shift=0.0, haar=False):
    size = math.ceil(scale * math.exp(1.5 + shift)) + 2
    n = np.arange(1, size)
    result = np.zeros(size, dtype=complex)
    result[1:] = (function(np.log(n / scale) - shift) * np.exp(1j * alpha * n)
                  / np.sqrt(n * rho(alpha, haar)))
    return result


def winding(a, coeff):
    result = np.zeros(a * (len(coeff) - 1) + 1, dtype=complex)
    result[::a] = coeff
    return result


def haar_current(coeff):
    result = np.zeros(len(coeff) + 1, dtype=complex)
    n = np.arange(1, len(coeff))
    result[n + 1] += 0.5j * (n + 0.5) * coeff[n]
    n = n[n >= 2]
    result[n - 1] -= 0.5j * (n - 0.5) * coeff[n]
    return result


def l2sum(vectors):
    result = np.zeros(max(len(v) for v in vectors), dtype=complex)
    for v in vectors:
        result[:len(v)] += v
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    seed = 20260925
    rng = np.random.default_rng(seed)
    checks = []
    convergence = []

    def check(label, actual, expected, tolerance=2e-11):
        error = float(abs(actual - expected))
        scale = max(1.0, float(abs(expected)))
        checks.append({'label': label, 'absolute_error': error,
                       'scaled_error': error / scale, 'tolerance': tolerance,
                       'passed': error <= tolerance * scale})

    nodes, weights = np.polynomial.legendre.leggauss(360)
    x = 3 * nodes
    weights = 3 * weights

    def pairing(shift=0.0, left=f, right=g, multiplier=None):
        values = np.conj(left(x)) * right(x - shift)
        if multiplier is not None:
            values *= multiplier(x)
        return np.sum(weights * values)

    theta = 2 * np.pi * (np.arange(4096) + 0.5) / 4096
    modes = np.arange(1, 9)
    for haar in (True, False):
        label = 'Haar' if haar else 'positive_central_control'
        av = np.zeros(9, complex)
        bv = np.zeros(9, complex)
        av[1:] = rng.normal(size=8) + 1j * rng.normal(size=8)
        bv[1:] = rng.normal(size=8) + 1j * rng.normal(size=8)

        def sine(c, angle):
            return np.sum(c[1:, None] * np.sin(modes[:, None] * angle), axis=0)

        for a in (2, 3, 5):
            # Independent root-transfer expression for the weighted adjoint.
            adjoint = sum(rho((theta + 2 * np.pi * j) / a, haar)
                          * sine(av, (theta + 2 * np.pi * j) / a)
                          for j in range(a)) / (a * rho(theta, haar))
            adjoint_pair = 2 * np.mean(rho(theta, haar) * np.conj(adjoint) * sine(bv, theta))
            check(f'{label}: weighted adjoint a={a}', gram(av, winding(a, bv), haar), adjoint_pair)
            density_average = sum(rho((theta + 2 * np.pi * j) / a, haar)
                                  for j in range(a)) / a
            norm_rhs = 2 * np.mean(density_average * abs(sine(bv, theta))**2)
            check(f'{label}: norm defect a={a}', gram(winding(a, bv), winding(a, bv), haar), norm_rhs)

        for a in (2, 3, 5):
            for alpha in (0.0, 2 * np.pi / 5):
                left = winding(a, packet(40, f, alpha, haar=haar))
                pieces = []
                for j in range(a):
                    beta = (alpha + 2 * np.pi * j) / a
                    pieces.append(math.sqrt(rho(beta, haar) / (a * rho(alpha, haar)))
                                  * packet(40, f, beta, math.log(a), haar))
                right = l2sum(pieces)
                padded = l2sum([left, -right])
                check(f'{label}: exact channel branching a={a}, alpha={alpha}',
                      np.linalg.norm(padded), 0)

        for a, b in ((1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (4, 6)):
            divisor = math.gcd(a, b)
            rho_d = sum(rho(2 * np.pi * j / divisor, haar) for j in range(divisor)) / divisor
            predicted = (divisor * rho_d / (math.sqrt(a * b) * rho(0, haar))
                         * pairing(math.log(b / a)))
            errors = []
            for scale in (32, 128, 512):
                measured = gram(winding(a, packet(scale, f, haar=haar)),
                                winding(b, packet(scale, g, haar=haar)), haar)
                errors.append(float(abs(measured - predicted)))
            convergence.append({'density': label, 'a': a, 'b': b,
                                'scales': [32, 128, 512], 'absolute_errors': errors})
            check(f'{label}: mixed limit a={a}, b={b}', measured, predicted, 2e-5)

        for alpha, beta in ((0, np.pi), (np.pi / 3, np.pi / 3), (np.pi / 3, 2 * np.pi / 3)):
            expected = pairing() if alpha == beta else 0
            phase_errors = []
            for scale in (128, 512, 2048, 8192):
                measured = gram(packet(scale, f, alpha, haar=haar),
                                packet(scale, g, beta, haar=haar), haar)
                phase_errors.append(float(abs(measured - expected)))
            convergence.append({'density': label, 'alpha': alpha, 'beta': beta,
                                'scales': [128, 512, 2048, 8192], 'absolute_errors': phase_errors})
            check(f'{label}: channel orthogonality {alpha}, {beta}',
                  measured, expected, 2e-5)

        for a in (2, 3, 4, 9):
            sr = packet(512, f, haar=haar)
            difference = l2sum([sr, -winding(a, sr)])
            avg = sum(rho(2 * np.pi * j / a, haar) for j in range(a)) / a
            expected = ((1 + avg / rho(0, haar)) * pairing(left=f, right=f)
                        - 2 / math.sqrt(a) * np.real(pairing(math.log(a), f, f)))
            check(f'{label}: positive block a={a}', gram(difference, difference, haar), expected, 2e-5)

    # Haar two-dimensional gluing comparison: no interacting-state substitution.
    scale = 512
    sf, sg = packet(scale, f, haar=True), packet(scale, g, haar=True)
    n = np.arange(len(sg), dtype=float)
    handle = np.zeros_like(n)
    handle[1:] = (scale / n[1:])**2
    check('2D: rescaled handle multiplier', gram(sf, sg * handle, True),
          pairing(multiplier=lambda z: np.exp(-2 * z)), 2e-5)
    area = np.exp(-0.4 * (n**2 - 1) / scale**2)
    check('2D: scaled cylinder multiplier', gram(sf, sg * area, True),
          pairing(multiplier=lambda z: np.exp(-0.4 * np.exp(2 * z))), 2e-5)
    electric = (n**2 - 1) / scale**2
    check('Haar: electric energy escape coefficient', gram(sf, sf * electric, True),
          pairing(left=f, right=f, multiplier=lambda z: np.exp(2 * z)), 2e-5)

    errors = []
    for scale in (32, 128, 512, 2048):
        error = l2sum([haar_current(packet(scale, f, haar=True)),
                       -packet(scale, minus_i_fprime, haar=True)])
        errors.append(float(np.linalg.norm(error)))
    convergence.append({'observable': 'Haar electric-Wilson current', 'scales': [32, 128, 512, 2048],
                        'absolute_errors': errors})
    check('Haar: current graph limit', errors[-1], 0, 2e-5)
    sr = packet(512, f, haar=True)
    for a in (3, 4, 5):
        current_winding = haar_current(winding(a, sr))
        predicted = a * a / 2 * pairing(left=f, right=f, multiplier=lambda z: np.exp(2 * z))
        check(f'Haar: other-channel current growth a={a}',
              np.vdot(current_winding, current_winding) / 512**2, predicted, 2e-5)

    record = {'date': '2026-09-25', 'prepared_for': 'Edward Baker',
              'model': 'GPT-6 (Codex)', 'reasoning_effort': 'not exposed; not inferred',
              'purpose': 'Finite algebra and asymptotic controls, not YM sampling or interval certification.',
              'python_version': platform.python_version(), 'numpy_version': np.__version__,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'parameters': {'seed': seed, 'angular_points': 4096, 'gauss_legendre_points': 360,
                             'density': '(1+0.35*cos(theta)+0.2*cos(2*theta))/0.9',
                             'asymptotic_scales': [32, 128, 512],
                             'phase_refinement_scales': [128, 512, 2048, 8192],
                             'current_refinement_scales': [32, 128, 512, 2048]},
              'check_count': len(checks), 'all_passed': all(c['passed'] for c in checks),
              'checks': checks, 'convergence': convergence}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'check_count': len(checks), 'all_passed': record['all_passed'],
                      'failed': [c for c in checks if not c['passed']],
                      'max_asymptotic_error': max(c['absolute_errors'][-1] for c in convergence)}, indent=2))
    if not record['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
