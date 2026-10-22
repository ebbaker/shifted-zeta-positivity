#!/usr/bin/env python3
"""Exact finite checks for the paired theta-residual research note.

Prepared for Edward Baker, 2026-10-22, with substantial LLM assistance.
Recorded model gpt-6.1-sol (Codex), reasoning effort ultra.
No theta field, event, source optimizer or mass is acquired here.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


class Jet:
    """Rational Taylor algebra in dx,dy,eps, spatial order 2, eps order 2."""
    def __init__(self, value=0):
        self.d = {p: F(v) for p, v in value.items() if v} if isinstance(value, dict) else ({(0, 0, 0): F(value)} if value else {})

    def get(self, i, j, k):
        return self.d.get((i, j, k), F(0))

    def __add__(self, other):
        other = other if isinstance(other, Jet) else Jet(other)
        result = self.d.copy()
        for p, v in other.d.items():
            result[p] = result.get(p, 0)+v
        return Jet(result)

    __radd__ = __add__

    def __neg__(self):
        return Jet({p: -v for p, v in self.d.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Jet) else -F(other))

    def __rsub__(self, other):
        return -self+other

    def __mul__(self, other):
        other = other if isinstance(other, Jet) else Jet(other)
        result = {}
        for p, v in self.d.items():
            for q, w in other.d.items():
                r = tuple(a+b for a, b in zip(p, q))
                if r[0]+r[1] <= 2 and r[2] <= 2:
                    result[r] = result.get(r, 0)+v*w
        return Jet(result)

    __rmul__ = __mul__

    def __pow__(self, n):
        result = Jet(1)
        for _ in range(n):
            result = result*self
        return result

    def inverse(self):
        c = self.get(0, 0, 0)
        assert c != 0
        u = self*(1/c)-1
        return sum(((-u)**n for n in range(5)), Jet())*(1/c)

    def __truediv__(self, other):
        return self*(other.inverse() if isinstance(other, Jet) else 1/F(other))

    def log_nonconstant(self):
        c = self.get(0, 0, 0)
        assert c > 0
        u = self/c-1
        return sum((u**n*F((-1)**(n+1), n) for n in range(1, 5)), Jet())


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def cnorm(a):
    return a[0]*a[0]+a[1]*a[1]


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def poly(coefficients, z):
    result = (Jet(), Jet())
    for c in reversed(coefficients):
        result = cadd(cmul(result, z), (Jet(c), Jet()))
    return result


def derivative(coefficients):
    return [j*coefficients[j] for j in range(1, len(coefficients))]


def local_checks(fc, rc, x0, y0):
    z = (Jet(x0)+Jet({(1, 0, 0): 1}), Jet(y0)+Jet({(0, 1, 0): 1}))
    eps = Jet({(0, 0, 1): 1})
    f, r = poly(fc, z), poly(rc, z)
    fz, rz = poly(derivative(fc), z), poly(derivative(rc), z)
    fzz, rzz = poly(derivative(derivative(fc)), z), poly(derivative(derivative(rc)), z)
    h = cadd(f, (eps*r[0], eps*r[1]))
    hz = cadd(fz, (eps*rz[0], eps*rz[1]))
    hzz = cadd(fzz, (eps*rzz[0], eps*rzz[1]))
    energy = cnorm(h)+cnorm(hz)
    ef = cnorm(f)+cnorm(fz)
    a = (dot(f, r)+dot(fz, rz))/ef
    b = (cnorm(r)+cnorm(rz))/ef
    loge = energy.log_nonconstant()
    det1, det2 = cmul(h, hzz), cmul(hz, hz)
    density_without_pi = cnorm((det1[0]-det2[0], det1[1]-det2[1]))/(energy**2)
    for k in range(3):
        laplacian = 2*loge.get(2, 0, k)+2*loge.get(0, 2, k)
        assert laplacian == 4*density_without_pi.get(0, 0, k)
    for i in range(3):
        for j in range(3-i):
            assert loge.get(i, j, 1) == (2*a).get(i, j, 0)
            assert loge.get(i, j, 2) == (b-2*a*a).get(i, j, 0)


def run(note):
    rho = F(1, 16)
    cubic = F(8, 9)*2*rho**3/(3*(1-rho))
    assert cubic == F(1, 6480) < F(1, 100)
    assert F(1, 17)/(1-F(1, 17)) == rho
    theta = F(1, 16)
    assert (4*theta)**2/2 == F(1, 32) < F(1, 4)
    r_bar = F(81, 2048)
    source_upper_ratio = 2+3*r_bar/(1-r_bar)
    source_gap_ratio = 3-source_upper_ratio
    assert source_upper_ratio == F(4177, 1967) < 3
    assert source_gap_ratio == F(1724, 1967) > 0
    assert F(81, 16)*F(1, 128) == r_bar
    # Algebraic parameters, not approximations or samples of theta data.
    for alpha, beta in [(F(4), F(16)), (F(7), F(9)), (F(20), F(21))]:
        D = 2*alpha-3
        bk_over_a = 3*(beta-alpha)/(D*beta)
        assert 6/D-2*bk_over_a == 6*alpha/(D*beta) > 0
    gamma = F(3, 4)
    assert gamma/(gamma-gamma/2) == 2
    examples = [
        ([-F(1, 4096), 0, 1], [0, -F(3, 4096), 0, 1], F(1, 32), F(1, 64)),
        ([0, 1], [1, 0, 1], F(0), F(0)),
        ([1, 0, 1], [0, -1, 0, 1], F(1, 3), F(1, 5)),
    ]
    for args in examples:
        local_checks(*args)
    return {
        'schema': 1, 'date': '2026-10-22', 'prepared_for': 'Edward Baker',
        'assistance': 'Substantial LLM assistance',
        'model': 'gpt-6.1-sol (Codex)', 'reasoning_effort': 'ultra',
        'status': 'exact finite rational checks passed; no theta acquisition',
        'files_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (Path(__file__), note)},
        'checks': {
            'relative_floor_threshold': 'eta/sqrt(e) <= 1/17 implies rho <= 1/16',
            'cubic_allowance': str(cubic),
            'source_shift': str(theta),
            'ray_exponent_growth_upper': '1/32',
            'canonical_moment_ratio_strict_upper': str(source_upper_ratio),
            'coarse_minus_new_moment_gap_strict_lower_over_A': str(source_gap_ratio),
            'inherited_strip_minus_new_cap_exact_gap': '6*A*alpha/(D*beta) > 0',
            'strip_gap_algebraic_parameter_cases': 3,
            'local_polynomial_cases': len(examples),
            'density_laplacian_coefficients_checked_per_case': [0, 1, 2],
            'log_variation_coefficients_checked': 36,
            'signed_dual_or_optimizer_acquired': False,
            'canonical_source_values_acquired': False,
            'actual_weighted_mass_computed': False,
            'complete_direct_advantage_proved': False,
            'scope': 'Written proofs establish the all-mode inequalities and integrated comparison; finite cases check local normalization and coefficients only.'
        }
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    parser.add_argument('--note', type=Path, default=here.parent/'notes/02_PAIRED_THETA_RESIDUAL_AND_MATCHED_DIRECT_COMPARISON_20261022.md')
    parser.add_argument('--output', type=Path, default=here/'WGI_PAIRED_RESIDUAL_CHECKS_20261022.json')
    args = parser.parse_args()
    record = run(args.note.resolve())
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status': record['status'], 'local_polynomial_cases': 3,
                      'source_moment_gap_ratio': record['checks']['coarse_minus_new_moment_gap_strict_lower_over_A']}))


if __name__ == '__main__':
    main()
