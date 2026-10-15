#!/usr/bin/env python3
"""Exact finite algebra for the elliptic-shift source-core experiment.

No numerical theta sign test or infinite-series theorem is claimed.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import platform


counts = {}


def check(got, want, group):
    assert got == want, (group, got, want)
    counts[group] = counts.get(group, 0) + 1


def clean(p):
    return {k: F(v) for k, v in p.items() if v}


def add(*ps):
    result = {}
    for p in ps:
        for k, v in p.items():
            result[k] = result.get(k, F(0)) + v
    return clean(result)


def scale(p, a):
    return clean({k: a * v for k, v in p.items()})


def mul(p, q):
    result = {}
    for k, v in p.items():
        for ell, w in q.items():
            key = tuple(a + b for a, b in zip(k, ell))
            result[key] = result.get(key, F(0)) + v * w
    return clean(result)


def diff(p, which):
    result = {}
    for k, v in p.items():
        if k[which]:
            ell = list(k)
            ell[which] -= 1
            result[tuple(ell)] = v * k[which]
    return clean(result)


def at_first(p, value):
    result = {}
    for (a, b), coefficient in p.items():
        result[b] = result.get(b, F(0)) + coefficient * value ** a
    return clean(result)


# R_k(X,c) is D^k exp(lambda z) / exp(lambda z), with X=lambda+a,
# D=partial_z+a, partial_z a=c and partial_z c=0.
X = {(1, 0): F(1)}
c = {(0, 1): F(1)}
R = {(0, 0): F(1)}
for _ in range(4):
    R = add(mul(X, R), mul(c, diff(R, 0)))
check(R, {(4, 0): F(1), (2, 1): F(6), (0, 2): F(3)},
      'covariant_fourth_jet')

# After dividing by the source normalization, use s=pi*q. The ordinary
# fourth/second-derivative operator on the shifted mode has this polynomial.
shifted = add(
    {(k, 2): F(comb(4, k)) for k in range(5)},
    {(k, 1): -F(3, 2) * comb(2, k) for k in range(3)},
)
expected = {(4, 2): F(1), (3, 2): F(4), (2, 2): F(6),
            (1, 2): F(4), (0, 2): F(1), (2, 1): -F(3, 2),
            (1, 1): F(-3), (0, 1): -F(3, 2)}
check(shifted, expected, 'translated_source_operator')
check(at_first(shifted, -1), {}, 'translated_zero_mode_cancellation')
check(sum(F(comb(4, k)) * (-1) ** k for k in range(5)), F(0),
      'translated_zero_mode_cancellation')
check(sum(-F(3, 2) * comb(2, k) * (-1) ** k for k in range(3)), F(0),
      'translated_zero_mode_cancellation')


def physical_projection(a):
    """Coefficient of phi_m after the complete source operator at z=0."""
    positive = {abs(n) for n in a if n}
    return clean({m: (a.get(m, F(0)) + a.get(-m, F(0))) / 2
                  for m in positive})


def shifted_coefficients(a, k):
    return {n + k: value for n, value in a.items()}


def one_dim_difference(a, b):
    return clean({n: a.get(n, F(0)) - b.get(n, F(0))
                  for n in set(a) | set(b)})


for N in range(1, 10):
    a = {n: F(1) for n in range(-N, N + 1)}
    raw_difference = one_dim_difference(shifted_coefficients(a, 1), a)
    check(raw_difference, {N + 1: F(1), -N: F(-1)}, 'raw_shift_boundary')
    original = physical_projection(a)
    for k in range(-min(N, 4), min(N, 4) + 1):
        observed = one_dim_difference(
            physical_projection(shifted_coefficients(a, k)), original)
        expected_boundary = {}
        for r in range(1, abs(k) + 1):
            expected_boundary[N + r] = expected_boundary.get(N + r, 0) + F(1, 2)
        for r in range(abs(k)):
            expected_boundary[N - r] = expected_boundary.get(N - r, 0) - F(1, 2)
        check(observed, clean(expected_boundary), 'finite_shift_boundary_band')
    check(physical_projection(shifted_coefficients(a, 1)),
          physical_projection(shifted_coefficients(a, -1)),
          'symmetric_shift_has_same_source')

for M in (1, 2, 3, 4, 7):
    a = {0: F(1)}
    for n in range(1, M + 1):
        a[n] = a[-n] = F(n + 1, n)
    observed = one_dim_difference(
        physical_projection(shifted_coefficients(a, 1)), physical_projection(a))
    laplacian = clean({m: (a.get(m - 1, 0) + a.get(m + 1, 0)
                           - 2 * a.get(m, 0)) / 2
                       for m in range(1, M + 2)})
    check(observed, laplacian, 'projected_coefficient_laplacian')
    check(observed[M + 1], a[M] / 2, 'finite_support_control_rejected')

# A ramp on the whole integer lattice, not a finite truncation of one.
for A in (F(1), F(3, 2)):
    for b in (F(-1, 3), F(0), F(2, 3)):
        a = lambda n: A + b * abs(n)
        for k in range(1, 6):
            for m in range(1, 13):
                defect = (a(m - k) + a(m + k) - 2 * a(m)) / 2
                check(defect, b * max(k - m, 0), 'ramp_shift_projection')

# Differentiate p_n=e^u exp(-a), a=pi*n^2*e^(4u):
# derivative of p_n P(a) is p_n[(1-4a)P+4aP'].
def primitive_derivative(p):
    result = {}
    for exponent, coefficient in p.items():
        result[exponent] = result.get(exponent, F(0)) + (1 + 4 * exponent) * coefficient
        result[exponent + 1] = result.get(exponent + 1, F(0)) - 4 * coefficient
    return clean(result)

first = primitive_derivative({0: F(1)})
second = primitive_derivative(first)
second[0] -= 1
check(first, {0: F(1), 1: F(-4)}, 'primitive_endpoint_polynomial')
check(clean({k: v / 8 for k, v in second.items()}),
      {2: F(2), 1: F(-3)}, 'primitive_source_polynomial')

# Exact collision controls test the unresolved scalar quadratic form in both
# parity branches. They are not claimed to obey theta arithmetic relations.
delta = F(1, 4)
control_receipts = []
for K in (F(0), F(1), F(16), F(1024)):
    s = F(7, 64) / (K + 1)
    for j, multiple in ((0, F(1)), (1, F(3))):
        W = multiple * 2 * s
        endpoint = multiple * (delta ** 2 + 2 * s - 2 * delta)
        energy = W ** 2
        signed_core = W * endpoint + K * energy
        check(signed_core < 0, True, 'stationary_heat_control_indefiniteness')
        # Exact stationarity at x=0 and nonvanishing W on [0,delta] follow
        # directly from W(x)=multiple*(x^2+2s).
        check(multiple > 0 and s > 0, True, 'stationary_heat_control_domain')
        control_receipts.append({'j': j, 'K': str(K), 's': str(s),
                                 'C_plus_K_E': str(signed_core)})

check(-F(1, 2) ** 2, -F(1, 4), 'unresolved_quadratic_determinant')

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path)
args = parser.parse_args()
record = {
    'status': 'pass',
    'date': '2026-10-15',
    'prepared_for': 'Edward Baker',
    'assistance': 'Substantial LLM assistance',
    'model': 'gpt-6-astra',
    'reasoning_effort': 'ultra',
    'arithmetic': 'Python standard library fractions.Fraction; exact finite polynomials and coefficient arrays',
    'python_version': platform.python_version(),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'assertions_by_group': counts,
    'exact_assertions': sum(counts.values()),
    'polynomial_control_receipts': control_receipts,
    'analytic_proofs_not_inferred_from_finite_checks': [
        'Convergence and vanishing upper primitive endpoints',
        'Gaussian boundary tail with physical heat weights',
        'Polynomial-growth projected-shift rigidity and primitive normalization',
        'Classification of every fixed finite shift combination',
    ],
    'not_established': [
        'A theta-specific signed-core inequality',
        'Theta collision exclusion or an RH conclusion',
        'Impossibility of more general coupled arithmetic or bilocal methods',
        'Any new numerical collision for an arithmetic source',
    ],
}
serialized = json.dumps(record, indent=2, sort_keys=True) + '\n'
if args.output:
    args.output.write_text(serialized)
print(serialized)
