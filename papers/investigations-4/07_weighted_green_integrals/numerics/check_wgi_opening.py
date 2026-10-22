#!/usr/bin/env python3
"""Exact algebra for the WGI opening note; no theta acquisition.

Prepared for Edward Baker, 2026-10-22, with substantial LLM assistance.
Recorded authoring configuration: gpt-6.1-sol (Codex), effort ultra.
The written proofs carry the analytic claims. This replay checks finite
normalizations, coefficient identities and rational control inequalities.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integral(coeff, end=F(1)):
    return sum((c * end ** (j + 1) / (j + 1)
                for j, c in enumerate(coeff)), F(0))


def derivative(coeff):
    return [j * coeff[j] for j in range(1, len(coeff))]


def evaluate(coeff, x):
    return sum((c * x ** j for j, c in enumerate(coeff)), F(0))


def run(note):
    psi = [F(1), F(-3), F(3), F(-1)]
    signed_radial = [F(-3), F(12), F(-9)]
    assert all(evaluate(p, F(1)) == 0
               for p in (psi, derivative(psi), derivative(derivative(psi))))
    assert integral(psi) == F(1, 4)
    assert integral(signed_radial) == 0
    negative = -integral(signed_radial, F(1, 3))
    assert negative == F(4, 9)
    for m in range(13):
        shifted = [F(0)] * m + signed_radial
        assert integral(shifted) == F(6*m, (m+1)*(m+2)*(m+3))
    for n in range(1, 13):
        for k in range(1, n+1):
            coefficient = sum((F((-1)**(j+1) * comb(j, k) * (-1)**(j-k), j)
                               for j in range(k, n+1)), F(0))
            assert coefficient == F((-1)**(k+1) * comb(n, k), k)

    h = D2 = F(2)
    D3 = D4 = F(0)
    P = r_ambient = d_ambient = F(1)
    C0 = D3 + P*D2
    C1 = D4 + P*D3
    J0 = D3 + D4 + F(4)*C0/(3*h)*(D2+D3)
    alpha = min(F(1), h/(4*C0))
    R = F(1, 2)*min(r_ambient, d_ambient/alpha,
                    h/(4*(C0+C1)), h/(2*J0))
    d = min(alpha*R, h*R*R/(32*D2))
    t0 = d/4
    eps2 = D3*R + D4*d
    k = h-eps2
    v = t0*k
    b = k*k/D2
    e = v*v if v <= b else 2*b*v-b*b
    M = D2*(t0+R*R/2)
    eps = D2*R+D3*t0
    U = M*M+eps*eps
    green = R*eps*(M+D2)/(5*h*R/8)**2
    assert (R, d, t0, M, eps, e) == (
        F(1, 8), F(1, 2048), F(1, 8192), F(65, 4096),
        F(1, 4), F(1, 16777216))
    Q = U/e
    assert Q == 1052801 == 2**20 + 65**2
    assert green == F(8257, 3200) < 3
    # log 2 = 2 atanh(1/3) > 2/3: the omitted series is positive.
    range_lower = F(4, 9)*20*F(2, 3)
    assert range_lower == F(160, 27) > 5 > green
    rho = (U-e)/(U+e)
    assert rho == F(526400, 526401)
    m = F(526401)
    N = 10001
    taylor_allowance_lower = F(8, 9)*(m-N)/N
    assert taylor_allowance_lower == F(4131200, 90009) > 45
    assert 1027**2 > Q
    # r_C < 513/514; r^(n+1)/(1-r) increases with r in [0,1).
    cheb_degree = 4096
    Nc = cheb_degree+1
    cheb_upper = F(16, 9)*F(514, Nc)*F(513, 514)**Nc
    assert cheb_upper < F(1, 10000)
    scale = 10**12
    upper_ceil = (cheb_upper.numerator*scale+cheb_upper.denominator-1)//cheb_upper.denominator
    assert F(upper_ceil, scale) >= cheb_upper
    return {
        'schema': 1,
        'date': '2026-10-22',
        'prepared_for': 'Edward Baker',
        'assistance': 'Substantial LLM assistance',
        'model': 'gpt-6.1-sol (Codex)',
        'reasoning_effort': 'ultra',
        'status': 'exact rational algebra checks passed; no theta acquisition',
        'scope': 'Finite checks support the written proofs; no canonical gain or acquisition cost certified.',
        'files_sha256': {Path(__file__).name: digest(Path(__file__)), note.name: digest(note)},
        'checks': {
            'weight_C2_join': True,
            'signed_mass_zero': True,
            'positive_and_negative_mass': '4/9',
            'radial_moments_checked_m': [0, 12],
            'polynomial_coefficients_checked_n': [1, 12],
            'quadratic_contract': {key: str(value) for key, value in
                                   [('R', R), ('d', d), ('t0', t0), ('M', M),
                                    ('epsilon', eps), ('e', e), ('U', U), ('U_over_e', Q)]},
            'direct_coarse_green_cap': str(green),
            'range_cap_strict_lower': str(range_lower),
            'range_cap_exceeds_direct_cap': True,
            'midpoint_rho': str(rho),
            'midpoint_degrees_screened': [1, 10000],
            'midpoint_allowance_lower': str(taylor_allowance_lower),
            'midpoint_allowance_exceeds_45': True,
            'chebyshev_degree': cheb_degree,
            'chebyshev_r_strict_upper': '513/514',
            'chebyshev_allowance_upper_rounded_up': f'{upper_ceil // scale}.{upper_ceil % scale:012d}',
            'chebyshev_allowance_less_than_1_over_10000': True,
            'actual_weighted_mass_computed': False,
            'canonical_source_moments_acquired': False,
            'complete_estimator_advantage_proved': False,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    parser.add_argument('--note', type=Path,
                        default=here.parent/'notes/01_REGULAR_SLICE_AND_COUPLED_LOG_ENCLOSURES_20261022.md')
    parser.add_argument('--output', type=Path, default=here/'WGI_OPENING_CHECKS_20261022.json')
    args = parser.parse_args()
    record = run(args.note.resolve())
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status': record['status'], 'output': str(args.output),
                      'chebyshev_allowance_upper': record['checks']['chebyshev_allowance_upper_rounded_up']}))


if __name__ == '__main__':
    main()
