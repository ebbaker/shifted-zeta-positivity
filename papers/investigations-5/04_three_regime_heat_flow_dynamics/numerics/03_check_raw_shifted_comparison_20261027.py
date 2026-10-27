#!/usr/bin/env python3
"""Bounded scalar replay for CE Notes15-16, standard library only.

27 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model gpt-6.1-sol, effort ultra. Reuses the repository Fraction
interval engine; this is not independent arithmetic or a theta jet cover.
"""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from functools import cache
from math import factorial, isqrt
from pathlib import Path
import sys


def ceil_f(x):
    return -((-x.numerator)//x.denominator)


def sqrt_ceil(x):
    s = isqrt(x.numerator//x.denominator)
    return s+(s*s*x.denominator < x.numerator)


def run(repo):
    base_path = repo/'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/certify_manuscript_constants.py'
    spec = importlib.util.spec_from_file_location('raw_shifted_interval_engine', base_path)
    base = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = base
    spec.loader.exec_module(base)
    base.BITS = 2048
    base.GRID = 1 << base.BITS
    I = base.I

    def atan_inv(q, n=220):
        s = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(n+1)), F(0))
        tail = F(1, (2*n+3)*q**(2*n+3))
        return I(s-tail, s+tail)

    pi = 16*atan_inv(5)-4*atan_inv(239)
    assert 3 < pi.lo < pi.hi < F(22, 7)

    def sin_i(x):
        term, total = x, x
        for k in range(1, 141):
            term = -term*x*x/F((2*k)*(2*k+1))
            total = total+term
        tail = x.hi**283/factorial(283)
        return total+I(-tail, tail)

    def ln_unit(y):
        z = (y-1)/(y+1)
        term, total = z, I(0)
        for k in range(301):
            total = total+term/F(2*k+1)
            term = term*z*z
        tail = 2*term.hi/F(603)/(1-z.hi*z.hi)
        return 2*total+I(0, tail)

    ln2 = ln_unit(I(2))

    @cache
    def ln_exact(y):
        assert y > 0
        k = y.numerator.bit_length()-y.denominator.bit_length()
        v = y/(F(2)**k)
        while v < 1:
            k -= 1
            v *= 2
        while v > 2:
            k += 1
            v /= 2
        return k*ln2+ln_unit(I(v))

    @cache
    def ln_i(y):
        y = I.cast(y)
        assert y.lo > 0
        return I(ln_exact(y.lo).lo, ln_exact(y.hi).hi)

    def exp_neg(y):
        assert y.lo >= 0
        # Avoid ever constructing exp(exp(height)); e>2 is enough here.
        if y.lo >= 256:
            return I(0, F(1, 2**256))
        return base.exp_negative(y)

    def upper_text(x):
        return base.decimal_bound(x.hi, base.ROUND_CEILING)

    ln4, ln3 = 2*ln2, ln_i(3)
    ln_eps = -6*ln_i(10)
    ln_quarter = ln_eps-ln4
    b, B, zeta = F(1, 8), F(1, 4), F(1, 256)
    rho, theta = F(1, 2), F(1, 3)
    alpha = pi/8
    cases = []
    for height_bits in (16, 64, 256, 512):
        X, A = 2**height_bits, 2**height_bits-1
        lx, la = height_bits*ln2, ln_i(A)
        log_a4pi = ln_i(I(A)/(4*pi))
        for method in ('raw', 'fixed_shift', 'moving_positive_slab'):
            if method == 'raw':
                sigma, g, c = I(0), alpha, I(1)
            elif method == 'fixed_shift':
                sigma = pi/16
                g, c = alpha-sigma, sin_i(pi/4)
            else:
                g = zeta*lx*lx/X
                sigma, c = alpha-g, sin_i(4*g)
            assert 0 < g.lo <= g.hi <= alpha.hi
            eta = pi*c
            if method == 'moving_positive_slab':
                M = sqrt_ceil((1/c).hi)  # Q=1
            else:
                M = sqrt_ceil(((g*X-ln_eps+100*lx+100)/eta).hi)
            M = max(2, M)
            K = M-1
            rate = 4*eta*M*M-9
            ratio = I(F(M+1, M))**4*exp_neg(eta*(2*M+1))
            assert rate.lo > 0 and (8*eta*M*M).lo >= B and ratio.hi < 1
            log_s = ln_i(2*pi*pi*M**4+3*pi*M*M)-eta*M*M-ln_i(1-ratio)
            log_r = -F(7, 4)*la+g*X-F(b, 16)*log_a4pi*log_a4pi-b*sigma*sigma
            log_mode0 = log_r+log_s-ln_i(rate)
            log_mode1 = log_r+log_s+ln_i(sigma/rate+1/(rate*rate))
            mode_pass = max(log_mode0.hi, log_mode1.hi) <= ln_quarter.lo
            if method != 'moving_positive_slab':
                assert mode_pass
            log_csource = ln_i(30000)+3*I(max(F(0), -ln_i(eta).hi),
                                         max(F(0), -ln_i(eta).lo))
            V = max(1, ceil_f((lx/4).hi))
            while True:
                lv = eta/2*base.exp_positive(I(4*V))
                log_frequency = log_r+log_csource+ln_i(1+sigma)-lv-ln_i(4*lv)
                if B*V*V+10*V <= lv.lo and log_frequency.hi <= ln_quarter.lo:
                    break
                V += 1
                assert V < 2000
            delta = rho*g
            J = ceil_f((V/(2*theta*delta)).hi)
            h = F(V, J)
            assert h/2 <= theta*delta.lo
            s2 = F(K*(K+1)*(2*K+1), 6)
            s4 = F(K*(K+1)*(2*K+1)*(3*K*K+3*K-1), 30)
            log_pa = ln_i(2*pi*pi*s4)+9*(V+delta)
            log_pb = ln_i(3*pi*s2)+5*(V+delta)
            assert (log_pa-log_pb).lo > 0
            log_pk = log_pa+ln_i(1+exp_neg(log_pa-log_pb))
            positive = I(max(F(0), (sigma-delta).lo), max(F(0), (sigma-delta).hi))
            da = (V+delta)**2-positive**2-log_a4pi**2/16
            t_star = base.max_interval(b*da, B*da)
            log_m1 = (-F(7, 4)*la+ln_i(V+sigma+delta)+log_pk
                      +(g+delta)*X+t_star)
            log_quad_prefactor = ln_i(V)+log_m1-ln_i(1-theta)
            q = max(1, ceil_f(((log_quad_prefactor-ln_quarter)/(2*ln3)).hi))
            log_quad = log_quad_prefactor-2*q*ln3
            assert log_quad.hi <= ln_quarter.lo
            log_z1 = log_m1-log_pk
            log_scaled_coefficient_allowance = (ln_eps+ln_i(1-theta*theta)
                -ln_i(16)-ln_i(V)-log_z1-ln_i(2*q-1))
            cases.append({
                'method': method, 'height_box': f'[2^{height_bits}-1,2^{height_bits}]',
                'time_box': '[1/8,1/4]', 'carrier': 'W_t(x), exactly Note15 (8)',
                'normalized_component_tolerance': '1e-6', 'ell': '1',
                'shift': '0' if method == 'raw' else ('pi/16' if method == 'fixed_shift'
                         else 'pi/8-(log X)^2/(256 X)'),
                'first_omitted_mode_M': str(M), 'frequency_cutoff_V': V,
                'cells_J': str(J), 'quadrature_order_q': str(q),
                'paired_derivative_entries_Jq': str(J*q),
                'unaggregated_mode_entries_KJq': str(K*J*q),
                'mode_quarter_budget_passed': mode_pass,
                'frequency_quarter_budget_passed': True,
                'quadrature_quarter_budget_passed': True,
                'log_normalized_mode0_upper': upper_text(log_mode0),
                'log_normalized_mode1_upper': upper_text(log_mode1),
                'log_normalized_frequency_upper': upper_text(log_frequency),
                'log_normalized_quadrature_upper': upper_text(log_quad),
                'log_scaled_source_coefficient_allowance_lower': base.decimal_bound(
                    log_scaled_coefficient_allowance.lo, base.ROUND_FLOOR),
                'log_scaled_source_coefficient_allowance_upper': upper_text(log_scaled_coefficient_allowance),
                'coefficient_allowance_scope': 'use lower endpoint as sufficient log tolerance; required only, not evaluated; final point error separately reserved',
            })
    moving = [c for c in cases if c['method'] == 'moving_positive_slab']
    assert not moving[0]['mode_quarter_budget_passed']
    assert moving[-1]['mode_quarter_budget_passed']
    raw_last = next(c for c in cases if c['method'] == 'raw' and '2^512]' in c['height_box'])
    assert int(moving[-1]['unaggregated_mode_entries_KJq']) < int(raw_last['unaggregated_mode_entries_KJq'])
    return {
        'status': 'passed', 'date': '2026-10-27', 'prepared_for': 'Edward Baker',
        'llm_assistance': 'substantial', 'model': 'gpt-6.1-sol', 'effort': 'ultra',
        'scope': ('Exact rational scalar upper-bound checks for complete source-budget '
                  'schedules. No source coefficients or theta field values evaluated, '
                  'no runtime benchmark, first-jet margin, or new covered slab.'),
        'arithmetic': 'reused Fraction intervals, 2048-bit outward dyadic rounding; logs and sine enclosed by Taylor tails',
        'pi_enclosure': base.serialize(pi),
        'cases': cases,
        'source_budget_failures_are_recorded': 'moving fixed-Q schedule fails at small examples and passes at the largest; no extrapolated onset claim',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'interval_engine': str(base_path.relative_to(repo)),
        'interval_engine_sha256': hashlib.sha256(base_path.read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo
    if repo is None:
        repo = next(p for p in Path(__file__).resolve().parents
                    if (p/'papers/investigations-3').is_dir())
    result = run(repo)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'scope', 'script_sha256')}))
