#!/usr/bin/env python3
"""Rational audit of retained scalar records and cumulative kernel signs.

Prepared for Edward Baker with LLM assistance, 2026-10-03.
GPT-6 (Codex); exact serving variant and effort not exposed or inferred.
This does not regenerate Arb zeros or verify published analytic inputs.
"""
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path


def interval(pack):
    lo, hi = F(pack['lower']), F(pack['upper'])
    assert lo <= hi
    return lo, hi


def derivative(p, n=1):
    for _ in range(n):
        p = [i*p[i] for i in range(1, len(p))]
    return p


def multiply(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out


def integrate(p, lo, hi):
    return sum(x*(hi**(i+1)-lo**(i+1))/(i+1)
               for i, x in enumerate(p))


def shift(p, s):
    out = [F(0)]*len(p)
    for j, x in enumerate(p):
        for i in range(j+1):
            out[i] += x*comb(j, i)*s**(j-i)
    return out


def exact_kernel_check():
    h = [F(0)]*17
    for j in range(9):
        h[2*j] = F(comb(8, j)*(-16)**j)
    hp, hpp, hppp = derivative(h), derivative(h, 2), derivative(h, 3)
    g0 = [F(0)]*16
    q0 = [x/4 for x in h]
    for i, x in enumerate(hpp):
        q0[i] -= x
    for i, x in enumerate(hp):
        g0[i] += x/4
    for i, x in enumerate(hppp):
        g0[i] -= x
    a = F(1, 4)
    nu = integrate(multiply(g0, g0), -a, a)
    nu6 = integrate(multiply(derivative(g0, 6), derivative(g0, 6)), -a, a)
    assert nu == F(146640624550936576, 37921101075)
    assert nu6 == F(2504085215525628254072340480, 19)
    for order in range(5):
        d = derivative(g0, order)
        assert sum(c*a**i for i, c in enumerate(d)) == 0
        assert sum(c*(-a)**i for i, c in enumerate(d)) == 0
    atom = 2*factorial(8)*8**8
    assert 8117695446119**2 > nu6/2
    b = atom+8117695446119
    signs = {}
    for s in [F(1, 16), F(1, 8), F(1, 4)]:
        value = integrate(multiply(g0, shift(q0, s)), -a, a-s)/nu
        signs[str(s)] = str(value)
    assert F(signs['1/8']) == F(
        -1140808292835309014305621023,
        342620277570940280369078861824)
    assert F(signs['1/16']) > 0 and F(signs['1/4']) > 0
    return nu, nu6, b, signs


def main():
    here = Path(__file__).resolve().parent
    source_hash = hashlib.sha256((here/'certify.py').read_bytes()).hexdigest()
    nu, nu6, b, signs = exact_kernel_check()
    records = []
    for bits in [192, 256]:
        r = json.loads((here/f'bound_{bits}.json').read_text())
        assert r['status'] == 'CERTIFIED_FINITE_CONTINUUM_CONSTANTS'
        assert r['bits'] == bits and r['script_sha256'] == source_hash
        assert F(r['source_norm_squared']) == nu
        assert F(r['interior_sixth_derivative_norm_squared']) == nu6
        assert r['total_variation_upper_integer'] == b
        assert r['computed_zero_count_at_500'] == 269
        assert r['both_zero_signs_included'] is True
        assert r['published_verified_height'] == '3000000000000'
        assert interval(r['last_included_ordinate'])[1] < 500
        assert interval(r['first_excluded_ordinate'])[0] > 500
        en = {key: interval(value) for key, value in r['enclosures'].items()}
        assert all(lo > 0 for lo, hi in en.values())
        assert en['K'][0]**2 <= F(b*b)/nu <= en['K'][1]**2
        components = ['low_linear_mass_through_500',
                      'critical_linear_tail_majorant_above_500',
                      'unknown_tail_cost_at_225', 'trivial_zero_majorant_at_1']
        p_lo, p_hi = en['uniform_p_upper_on_1_to_225']
        assert p_lo <= sum(en[k][0] for k in components)
        assert p_hi >= sum(en[k][1] for k in components)
        assert p_hi < F(497, 100)
        assert en['initial_energy_upper_at_1'][1] < F(127, 100)
        assert en['theta_lower_ratio_at_exp10'][0] > F(1, 2)
        assert en['diagonal_lower_constant'][1] < 48
        margin = F(100**2, 4)-48-F(127, 100)-F(497, 100)**2*99
        slope = F(100, 2)-F(497, 100)**2
        assert margin == F(53409, 10000) and margin > 5
        assert slope == F(252991, 10000) and slope > 0
        thresholds = r['certified_rational_thresholds']
        assert F(thresholds['sign_margin_at_Y100']) == margin
        assert F(thresholds['increasing_D_minus_J_slope_after_Y100']) == slope
        assert r['conclusions']['signed_pair_interval'] == ['100', '225']
        assert r['conclusions']['signed_pair_upper'] == '-5'
        records.append(en)
    assert records[0].keys() == records[1].keys()
    for key in records[0]:
        left, right = records[0][key], records[1][key]
        assert max(left[0], right[0]) <= min(left[1], right[1]), key
    print(json.dumps({
        'status': 'PASS_RATIONAL_RECORD_AND_KERNEL_AUDIT',
        'precisions': [192, 256],
        'script_sha256': source_hash,
        'sign_margin_at_Y100': str(margin),
        'minimum_slope_after_Y100': str(slope),
        'cumulative_autocorrelation_values': signs,
        'scope': 'Records and exact polynomial algebra; not regeneration '
                 'of rigorous zeros or proof of external analytic inputs.'
    }, indent=2))


if __name__ == '__main__':
    main()
