#!/usr/bin/env python3
"""Small exact algebra replay for FCG-E02 R1; no theta evaluation or scan.

30 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded coordinating model gpt-6.1-sol, reasoning effort ultra, chat0044.
Run from any directory; stdout is the small JSON execution record.
"""

from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import re


def add(a, b):
    out = dict(a)
    for degree, coefficient in b.items():
        out[degree] = out.get(degree, F(0)) + coefficient
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: v * c for k, v in a.items() if v * c}


def derivative(a):
    return {k - 1: k * v for k, v in a.items() if k}


def shift(a, n):
    return {k + n: v for k, v in a.items()}


def weighted_derivative(a):
    # d/dw [f(w) p(t)] / f(w), t=tanh(4w), f'/f=-2t.
    da = derivative(a)
    return add(add(scale(da, 4), scale(shift(da, 2), -4)),
               scale(shift(a, 1), -2))


def mul2(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, ell), y in b.items():
            key = (i + k, j + ell)
            out[key] = out.get(key, F(0)) + x * y
    return {k: v for k, v in out.items() if v}


def render(a):
    return {str(k): str(v) for k, v in sorted(a.items())}


def main(repo_root=None):
    one = {0: F(1)}
    second = weighted_derivative(weighted_derivative(one))
    fourth = weighted_derivative(weighted_derivative(second))
    df = add(add(fourth, scale(second, -8)), scale(one, 16))
    expected_df = {0: F(528), 2: F(-2208), 4: F(1680)}
    assert df == expected_df
    assert second == {0: F(-8), 2: F(12)}

    # Commuting symbols x=d_z,y=d_w, derived from d_u=(x+y)/2,
    # d_v=(x-y)/2. This checks the operator factor independently of f.
    u2_minus_one = {(2, 0): F(1, 4), (1, 1): F(1, 2),
                    (0, 2): F(1, 4), (0, 0): F(-1)}
    v2_minus_one = {(2, 0): F(1, 4), (1, 1): F(-1, 2),
                    (0, 2): F(1, 4), (0, 0): F(-1)}
    source_operator = mul2(u2_minus_one, v2_minus_one)
    assert source_operator == {
        (4, 0): F(1, 16), (2, 2): F(-1, 8), (0, 4): F(1, 16),
        (2, 0): F(-1, 2), (0, 2): F(-1, 2), (0, 0): F(1)}
    assert 16 * 16 * 16 == 4096

    moments = {}
    for j in (2, 3):
        terms = {}
        for ell in range(j + 1):
            key = tuple(sorted((2 * ell, 2 * j - 2 * ell)))
            terms[key] = terms.get(key, F(0)) + F(comb(j, ell), 2**j)
        moments[str(j)] = render(terms)
    assert moments == {
        '2': {'(0, 4)': '1/2', '(2, 2)': '1/2'},
        '3': {'(0, 6)': '1/4', '(2, 4)': '3/4'}}

    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[5]
    packet_path = root / ('papers/investigations-5/05_radial_theta_collision_geometry/'
                         'research-progress/handoffs/fixed_coefficient_parameter_geometry/'
                         'FCG-E02_R1_POISSON_LOCALIZATION_ASSESSMENT_20261030.md')
    packet = packet_path.read_text()
    inputs = []
    for name, expected in re.findall(
            r'\| `(papers/[^`]+)` \| `([0-9a-f]{64})` \|', packet):
        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
        assert actual == expected, name
        inputs.append({'path': name, 'expected_sha256': expected,
                       'actual_sha256': actual, 'matches': True})
    assert len(inputs) == 8
    result = {
        'date': '2026-10-30', 'timezone': 'America/New_York',
        'prepared_for': 'Edward Baker', 'llm_assistance': 'substantial',
        'model': 'gpt-6.1-sol', 'effort': 'ultra', 'chat': '0044',
        'task': 'FCG-E02 R1', 'arithmetic': 'Python standard-library Fraction',
        'scope': 'exact algebra and input identity only; no theta numerics, '
                 'interval certificate, tail proof, or parameter scan',
        'checks_passed': True, 'df_over_f_in_t': render(df),
        'df_at_zero_over_f_at_zero': '528', 'df_at_zero': '528/sqrt(2)',
        'source_operator_coefficients': render(source_operator),
        'source_product_factor': 4096, 'mu_coefficients': moments,
        'packet_sha256': hashlib.sha256(packet_path.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'inputs': inputs}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
