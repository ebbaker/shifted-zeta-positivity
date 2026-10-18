#!/usr/bin/env python3
"""Exact rational certificate for the revised manuscript table.

18 October 2026. Prepared for Edward Baker with substantial LLM assistance:
gpt-6-astra, ultra, editorial coordination of gpt-6.1-sol integration.
Reuses the original interval implementation; not an independent proof check.
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
    parser.add_argument('--base', type=Path,
                        default=Path(__file__).with_name('certify_manuscript_constants.py'))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('original_packet_intervals', args.base)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    old, _, _ = mod.compute()
    F = mod.F
    pi = old['pi']
    dm = F(29,200)
    strip_mass = old['m5_S']/(100*pi-10)
    kappa_s = F(6,7)*old['kappa']
    values = {
        'kappa': old['kappa'], 'rho3': old['m3_rho'], 'rho5': old['m5_rho'],
        'd5_rho5': dm*old['m5_rho'], 'd5_squared_rho5': dm**2*old['m5_rho'],
        'rho_strip5': (4097*strip_mass+2*old['m5_Q']+old['m5_S'])/kappa_s,
    }
    c, m, Y, T = F(7,10), 5, 1, F(1,2)
    lam = pi*m*m
    b = 4*c*lam-9-Y
    ratio = mod.I(F(m+1,m))**4*mod.exp_negative(c*pi*(2*m+1))
    assert b.lo > 0 and (8*c*lam).lo >= T and ratio.hi < 1
    S = (2*lam**2+3*lam)*mod.exp_negative(c*lam)/(1-ratio)
    d = pi/16
    for j in range(3):
        values[f'Kbar{j}'] = S*sum(
            (math.comb(j,k)*d**(j-k)*math.factorial(k)/b**(k+1)
             for k in range(j+1)), mod.I(0))
    table = {
        'kappa': ('0.00084868730924288','0.00084868730924289'),
        'rho3': ('0.00026291407856','0.00026291407858'),
        'rho5': ('7.25125221685e-25','7.25125221687e-25'),
        'd5_rho5': ('1.05143157144e-25','1.05143157145e-25'),
        'd5_squared_rho5': ('1.52457577859e-26','1.52457577860e-26'),
        'rho_strip5': ('8.47360190576e-25','8.47360190578e-25'),
        'Kbar0': ('7.95799323606e-23','7.95799323608e-23'),
        'Kbar1': ('1.60045950329e-23','1.60045950331e-23'),
        'Kbar2': ('3.22054543607e-24','3.22054543609e-24'),
    }
    bounds = {'rho3':'0.000263','rho5':'7.3e-25','d5_rho5':'1.06e-25',
              'd5_squared_rho5':'1.54e-26','rho_strip5':'8.5e-25',
              'Kbar0':'8e-23','Kbar1':'1.61e-23','Kbar2':'3.23e-24'}
    for name,(lo,hi) in table.items():
        v=values[name]
        assert F(lo)<v.lo<=v.hi<F(hi),name
    for name,bound in bounds.items():
        assert values[name].hi<F(bound),name
    record = {
        'date':'2026-10-18','prepared_for':'Edward Baker',
        'model':'gpt-6-astra','reasoning_effort':'ultra',
        'python':platform.python_version(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'base_script_sha256':hashlib.sha256(args.base.read_bytes()).hexdigest(),
        'scope':'Exact rational scalar table and headline checks; no quadrature or collision exclusion.',
        'arithmetic':{'type':'fractions.Fraction','outward_dyadic_bits':mod.BITS,
                      'reuse':'Original interval implementation, not independent implementation.'},
        'enclosures':{k:mod.serialize(v) for k,v in values.items()},
        'printed_table_enclosures_checked':table,
        'strict_upper_bound_checks':bounds,
        'shifted_constants_scope':'Kbar encloses conservative expression with cos(pi/4) replaced by 7/10.',
        'original_table_checks_passed':True,'all_checks_passed':True,
    }
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print('All nine revised table rows, eight headline bounds, and original checks passed.')


if __name__=='__main__':
    main()
