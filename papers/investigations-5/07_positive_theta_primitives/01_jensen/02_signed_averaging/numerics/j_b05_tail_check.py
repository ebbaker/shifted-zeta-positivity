#!/usr/bin/env python3
"""J-B05 finite exact check, 1 November 2026; Edward Baker, LLM assistance.
Actual contributor: gpt-6-astra / ultra. Only P0--P7 are generated.
Checks polynomial coefficients supporting the analytical mixed-node
obstruction. It does not certify a compact source sign or sample nodes.
"""
from fractions import Fraction
from pathlib import Path
import json

def build_record():
    p = [0, -3, 2]
    polys = []
    rows = []
    expected = {2: (16, -88), 4: (256, -3840), 6: (4096, -116736)}
    for j in range(8):
        polys.append(p[:])
        if j in expected:
            a = Fraction(p[-1], 2)
            b = Fraction(p[-2], 2) + Fraction(3, 2) * a
            assert (a, b) == expected[j]
            rows.append({'source_derivative': j, 'leading_power': j,
                         'leading_coefficient': str(a),
                         'next_coefficient': str(b)})
        if j < 7:
            q = [0] * (len(p) + 1)
            for k, c in enumerate(p):
                q[k] += (4*k + 1) * c
                q[k+1] -= 4*c
            p = q
    assert Fraction(-3840 - 2*16*(-88), 64) == -16
    assert Fraction(-116736 - 3*16**2*(-88), 1024) == -48
    return {'task': 'J-B05', 'date_local': '2026-11-01',
            'model': 'gpt-6-astra', 'effort': 'ultra',
            'method': 'exact integer recurrence and Fraction arithmetic',
            'scope': 'P0 through P7, no source samples or coefficient scan',
            'polynomials_ascending': polys, 'quotient_top_two': rows,
            'f_puiseux_correction': -16, 'g_puiseux_correction': -48,
            'g_divided_difference_derivative_leading': 24,
            'status': 'finite algebra checked; full-source sign is analytical in note'}

if __name__ == '__main__':
    record = build_record()
    target = Path(__file__).with_name('J_B05_TAIL_CHECK_20261101.json')
    target.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'status': 'pass', 'record': str(target),
                      'checked_orders': [2,4,6], 'recurrence_cap': 7}))
