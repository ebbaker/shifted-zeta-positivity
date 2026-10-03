#!/usr/bin/env python3
"""Outward 7x7 joint Gram check for one prepared probe; no all-window claim.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and effort not exposed.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import platform
import time

import flint
from flint import arb, acb, ctx

BASE_SHA256 = '580357e377c032fbb3dc1012d2274771cfe01ab83fb7262bc1f656c4cdd0c907'
TRANSLATIONS = tuple(range(0, 13, 2))
SEPARATIONS = tuple(range(2, 13, 2))
SHIFT = Fraction(1, 20)


def load_base(path):
    digest = sha256(path.read_bytes()).hexdigest()
    if digest != BASE_SHA256:
        raise ArithmeticError('Base-script hash mismatch')
    spec = importlib.util.spec_from_file_location('prepared_probe_base', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def interval_ldl(first_row, shift):
    """Certify strict PD for the actual symmetric Toeplitz matrix minus shift I.

    Positive enclosing pivots inductively guarantee all exact denominators
    are positive. Treating repeated entries independently is conservative.
    No floating eigenvalue or numerical central matrix is used.
    """
    n = len(first_row)
    lower = [[arb(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        lower[i][i] = arb(1)
        pivot = first_row[0] - shift - sum(
            (lower[i][k] ** 2 * pivots[k] for k in range(i)), arb(0))
        if not pivot.is_finite() or not pivot > 0:
            raise ArithmeticError(f'Joint Gram pivot {i + 1} not positive: {pivot}')
        pivots.append(pivot)
        for j in range(i + 1, n):
            lower[j][i] = (first_row[j - i] - sum(
                (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)), arb(0))) / pivot
    return pivots


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bits', type=int, choices=(192, 256), required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--base-script', type=Path, default=(
        Path(__file__).resolve().parent.parent / 'all_window_mechanism_20261003' / 'certify_translated_probe.py'))
    args = parser.parse_args()
    base = load_base(args.base_script)
    ctx.prec = args.bits
    start = time.monotonic()
    ell = arb(1) / 2
    g, exact_phi, exact_norm = base.correlation_coefficients()
    phi = [base.ab(c) for c in exact_phi]
    divided = [-c for c in phi[1:]]

    def integrand(u, analytic):
        return base.polynomial(divided, u) * (u / 2).exp() / (
            2 * (u * u / 4).hypgeom_0f1(acb(3) / 2))

    integral = acb.integral(integrand, 0, acb(ell), abs_tol=arb(2) ** -100,
                            rel_tol=arb(2) ** -100, eval_limit=20000, depth_limit=40)
    if not integral.is_finite() or not integral.imag.contains(0):
        raise ArithmeticError('Validated diagonal integration failed')
    z = (-ell / 2).exp()
    gamma0 = acb(arb(1) / 4).digamma().real - arb.pi().log()
    diagonal = gamma0 + 2 * integral.real + 2 * (z.atanh() + z.atan())
    limit = int((arb(max(SEPARATIONS)) + ell).exp().upper().ceil().fmpq())
    if limit > 300000:
        raise ArithmeticError('Preflight sieve budget exceeded')
    rows = base.prime_power_rows(limit)
    sums = {r: [arb(0), 0] for r in SEPARATIONS}
    for n, p, exponent in rows:
        logn = arb(n).log()
        for r in SEPARATIONS:
            u = logn - r
            if abs(u) < ell:
                if not (u > 0 or u < 0):
                    raise ArithmeticError('Unresolved autocorrelation branch')
                weight = arb(p).log() / arb(n).sqrt()
                sums[r][0] += weight * base.polynomial(phi, abs(u))
                sums[r][1] += 1
            elif not abs(u) > ell:
                raise ArithmeticError('Unresolved support threshold')
    first_row = [diagonal]
    results = []
    for r in SEPARATIONS:
        signed, count = sums[r]
        bound = ell * (-arb(5) / 2 * (r - ell)).exp() / (1 - (-2 * (r - ell)).exp())
        # Radius construction encloses [-bound,+bound] using its upper endpoint.
        cross = -signed + arb(0, bound.upper())
        first_row.append(cross)
        results.append({'separation': r, 'prime_power_terms': count,
                        'signed_prime_sum': base.pack(signed),
                        'archimedean_remainder_bound': base.pack(bound),
                        'cross_form_enclosure': base.pack(cross)})
    pivots = interval_ldl(first_row, base.ab(SHIFT))
    seconds = time.monotonic() - start
    if seconds > 60:
        raise ArithmeticError('Preflight time budget exceeded')
    record = {
        'status': 'CERTIFIED_SEVEN_SOURCE_GRAM_GREATER_THAN_ONE_TWENTIETH_IDENTITY',
        'date': '2026-10-03', 'model': 'GPT-6 (Codex)',
        'serving_variant': 'not exposed', 'reasoning_effort': 'not exposed',
        'bits': args.bits, 'translations': list(TRANSLATIONS),
        'matrix': 'real symmetric Toeplitz; entry (i,j) = first_row[abs(i-j)]',
        'source_width': '1/2', 'total_support_width': '25/2',
        'certified_strict_lower_bound': str(SHIFT),
        'source': '(-d^2/dx^2+1/4)d/dx [(1-16x^2)^8 on |x|<1/4], L2-normalized',
        'source_polynomial_coefficients_unnormalized': [str(c) for c in g],
        'source_exact_norm_squared_unnormalized': str(exact_norm),
        'autocorrelation_coefficients_for_nonnegative_shift': [str(c) for c in exact_phi],
        'Q_diagonal': base.pack(diagonal),
        'sieve_limit': limit, 'all_prime_power_rows': len(rows), 'results': results,
        'first_row': [base.pack(c) for c in first_row],
        'shifted_LDL_pivots': [base.pack(p) for p in pivots],
        'base_script_sha256': BASE_SHA256,
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'seconds': seconds,
        'runtime': {'python': platform.python_version(), 'python_flint': flint.__version__, 'flint': flint.__FLINT_VERSION__},
        'limitations': [
            'One seven-dimensional subspace only; no full-source width 25/2 certificate.',
            'No all-translates, complete-probe-family, or all-window conclusion.',
            'The exactly prepared polynomial source is C4 and belongs to logarithmic form closure.',
            'Off-diagonal gamma remainder bounds are retained as outward symmetric balls.']}
    args.output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'status': record['status'], 'seconds': seconds,
                      'shift': str(SHIFT), 'pivot_lower_bounds_display': [float(p.lower()) for p in pivots]}))


if __name__ == '__main__':
    main()
