#!/usr/bin/env python3
"""Exact finite controls for the bounded infinite-L audit.

These controls check the rank-one trace/determinant identities and the
integer inequalities used in a prime-bound obstruction. They are not a
certificate of the Weil spectrum, a support sweep, or an infinite-L limit.
Only Python's standard library is needed; no zeta-zero data are used.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, lcm
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def determinant(matrix):
    a = [[F(x) for x in row] for row in matrix]
    n = len(a)
    result = F(1)
    for i in range(n):
        pivot = next((k for k in range(i, n) if a[k][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        p = a[i][i]
        result *= p
        for k in range(i + 1, n):
            factor = a[k][i] / p
            for j in range(i + 1, n):
                a[k][j] -= factor * a[i][j]
            a[k][i] = F(0)
    return result


def inverse(matrix):
    n = len(matrix)
    a = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for i in range(n):
        pivot = next((k for k in range(i, n) if a[k][i]), None)
        require(pivot is not None, 'Singular control matrix')
        a[i], a[pivot] = a[pivot], a[i]
        p = a[i][i]
        a[i] = [v / p for v in a[i]]
        for k in range(n):
            if k != i:
                factor = a[k][i]
                a[k] = [x - factor * y for x, y in zip(a[k], a[i])]
    return [row[n:] for row in a]


def product(values):
    result = F(1)
    for value in values:
        result *= value
    return result


def rank_one_control(label, a0, coefficients):
    # Unit frequency spacing: d_n=n. The ground Fourier coefficients are
    # a_0 and a_{-n}=a_n, with boundary sum s=a_0+2 sum(a_n).
    # Signed coefficients test the identity, not positive Weil hypotheses.
    a0 = F(a0)
    coeff = [F(a) for a in coefficients]
    n = len(coeff)
    s = a0 + 2 * sum(coeff)
    require(a0 != 0 and s != 0, 'Degenerate ground normalization')
    q = [[F((i + 1)**2 if i == j else 0)
          - 2 * (i + 1) * (j + 1) * coeff[i] / s
          for j in range(n)] for i in range(n)]
    inv = inverse(q)
    for i in range(n):
        for j in range(n):
            require(sum(q[i][k] * inv[k][j] for k in range(n)) == F(i == j),
                    'Inverse multiplication failed')
    trace = sum(inv[i][i] for i in range(n))
    correction = 2 / a0 * sum(a / (i + 1)**2 for i, a in enumerate(coeff))
    expected = sum(F(1, (i + 1)**2) for i in range(n)) + correction
    require(trace == expected, 'Rank-one trace identity failed')
    det = determinant(q)
    expected_det = product(F((i + 1)**2) for i in range(n)) * a0 / s
    require(det == expected_det, 'Ground-mean determinant identity failed')
    parameters = (F(-2), F(-1, 7), F(1, 3), F(3, 2), F(25, 3))
    for t in parameters:
        require(all((i + 1)**2 != t for i in range(n)), 'Control at a pole')
        shifted = [[q[i][j] - (t if i == j else 0) for j in range(n)]
                   for i in range(n)]
        direct = determinant(shifted) / det
        factored = product(1 - t / (i + 1)**2 for i in range(n))
        factored *= 1 - 2 * t / a0 * sum(
            a / ((i + 1)**2 - t) for i, a in enumerate(coeff))
        require(direct == factored, 'Normalized determinant identity failed')
    return dict(label=label,dimension=n,a0=str(a0),coefficients=list(map(str,coeff)),
                boundary_sum=str(s),trace_inverse=str(trace),
                ground_moment_correction=str(correction),
                determinant=str(det),spectral_parameter_checks=len(parameters))


def run():
    cases = [rank_one_control('constant ground', 1, [0, 0, 0, 0]),
             rank_one_control('one nonconstant coefficient', 3, [F(1, 2)]),
             rank_one_control('positive coefficients', 2,
                              [F(1, 2), F(1, 3), F(1, 5)]),
             rank_one_control('signed coefficients', 2,
                              [F(-1, 8), F(1, 16), F(-1, 32), F(1, 64)])]
    # The proof for all n uses Legendre's valuation formula and the largest
    # coefficient in (1+1)^(2n); these are independent finite controls.
    for n in range(1, 129):
        central = comb(2 * n, n)
        multiple = lcm(*range(1, 2 * n + 1))
        require(multiple % central == 0, 'Binomial does not divide lcm')
        require(central * (2 * n + 1) >= 4**n, 'Central-binomial bound failed')
    # Simple rational controls for constants in the analytic logarithm bounds.
    require(sum(F(3)**k / product(range(1, k + 1)) for k in range(6)) > 17,
            'exp(3)>17 Taylor lower bound failed')
    require(F(1, 4) + F(4, 75) < F(1, 2), 'Digamma upper-bound constants failed')
    require(2 * F(4) + 8 <= 4 * F(4), 'Scalar trace-bound constants failed')
    return dict(date='2026-09-26',
                model='GPT-6 (Codex); exact variant and reasoning effort not exposed',
                status='exact finite algebra controls; not a Weil-spectrum or infinite-L certificate',
                arithmetic='standard-library Fraction and integers',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                zero_data_used=False,arithmetic_support_sweep_performed=False,
                rank_one_cases=cases,total_spectral_parameter_checks=20,
                binomial_divisibility_checks=128,binomial_size_checks=128,
                constant_checks_passed=True,all_checks_passed=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).parent / 'records' /
                        'infinite_l_audit_controls_20260926.json')
    args = parser.parse_args()
    record = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print('Passed exact rank-one controls and 256 integer checks. No Weil limit is certified.')


if __name__ == '__main__':
    main()
