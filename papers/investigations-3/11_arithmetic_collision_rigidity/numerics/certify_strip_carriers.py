#!/usr/bin/env python3
"""Rational checks for investigation 11's 18 October strip-carrier continuation.

Prepared for Edward Baker with substantial LLM assistance: gpt-6-astra,
reasoning effort ultra. Reuses the manuscript's exact interval arithmetic;
this is not an independent arithmetic implementation or proof verification.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', type=Path, default=Path(__file__).with_name('certify_manuscript_constants.py'))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('packet_constant_intervals', args.base)
    base = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = base
    spec.loader.exec_module(base)
    values, _, _ = base.compute()  # also replays all original printed checks
    F = base.F
    pi = values['pi']
    kappa_strip = F(6, 7) * values['kappa']
    mass = values['m5_S'] / (100*pi - 10)
    rho_strip = (4097*mass + 2*values['m5_Q'] + values['m5_S']) / kappa_strip
    dm = F(29, 200)
    first = dm * values['m5_rho']
    second = dm**2 * values['m5_rho']
    checks = {
        'rho_strip_m5': (rho_strip, F('8.5e-25')),
        'real_remainder_first_m5': (first, F('1.06e-25')),
        'real_remainder_second_m5': (second, F('1.54e-26')),
        'old_one_sided_carrier_bound': (values['B2'], F('0.671')),
    }
    for name, (value, bound) in checks.items():
        assert 0 < value.lo <= value.hi < bound, name
    # Example constants for the shifted finite-mode tail lemma.  The exact
    # shift is d=pi/16; cos(4d)=1/sqrt(2)>7/10, so the rational lower bound
    # c0=7/10 gives a conservative certificate without a square-root routine.
    c0, m, Y, Tmax = F(7,10), 5, 1, F(1,2)
    lam = pi*m*m
    b = 4*c0*lam - 9 - Y
    ratio = base.I(F(m+1,m))**4 * base.exp_negative(c0*pi*(2*m+1))
    assert b.lo > 0 and (8*c0*lam).lo >= Tmax and ratio.hi < 1
    source = (2*lam**2 + 3*lam) * base.exp_negative(c0*lam) / (1-ratio)
    shift = pi/16
    shifted = {}
    for j in range(3):
        coeff = sum((math.comb(j,k) * shift**(j-k) * math.factorial(k) / b**(k+1)
                     for k in range(j+1)), base.I(0))
        shifted[f'K{j}'] = source*coeff
    for name, bound in {'K0':'8e-23','K1':'1.61e-23','K2':'3.23e-24'}.items():
        assert shifted[name].hi < F(bound), name
    record = {
        'date': '2026-10-18', 'prepared_for': 'Edward Baker',
        'model': 'gpt-6-astra', 'reasoning_effort': 'ultra',
        'python': platform.python_version(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'base_script_sha256': hashlib.sha256(args.base.read_bytes()).hexdigest(),
        'scope': 'Scalar rational certificates and original table replay; analytic proofs and collision exclusion are not numerically certified.',
        'arithmetic': 'Original Fraction intervals, outward 256-bit dyadic rounding; same implementation reused.',
        'checks': {name: {'enclosure': base.serialize(value), 'strict_upper_bound': str(bound)}
                   for name, (value,bound) in checks.items()},
        'strip_lower_constant': base.serialize(kappa_strip),
        'exact_schwarz_constants': {'carrier_log_slope': '1/8',
                                    'carrier_slope_squared_plus_absolute_curvature': '1/64',
                                    'real_remainder_log_slope_bound_m5': str(dm)},
        'shifted_tail_example': {
            'm': m, 'retained_modes': [1,2,3,4], 'Tmax': str(Tmax),
            'spectral_strip_half_width': Y, 'source_shift': 'pi/16',
            'cosine_lower_bound': str(c0),
            'bound': '|d_z^j(H-Htilde)| <= Kj exp(-pi Re(z)/16), j=0,1,2',
            'enclosures': {key:base.serialize(value) for key,value in shifted.items()},
            'scope': 'Tail constants only; no quadrature, positive field margin, or physical-relative error certified.'},
        'all_checks_passed': True,
    }
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    for name,(value,_) in checks.items():
        print(name, base.serialize(value)['upper_decimal'])
    for name,value in shifted.items():
        print('shifted_tail_'+name, base.serialize(value)['upper_decimal'])
    print('All original and new scalar checks passed.')


if __name__ == '__main__':
    main()
