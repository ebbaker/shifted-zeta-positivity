#!/usr/bin/env python3
"""Rational transfer of existing outward linear-probe certificates.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-03.
Model: GPT-6 (Codex); exact serving variant and effort not exposed.
No new zero enumeration or verification of published analytic inputs.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

INPUT_HASHES = {
    'bound_192.json': '21a71598fb9dcf8fe51743e75f65aedd5c5deee69619d2bda806da3e9ac6f2c0',
    'bound_256.json': '3c39ccfbc704122de57c04395e120f11a5a563d9d3838c5b6388a9e7c50a60b8',
    'certify.py': '6f3947f99d4b45307b8a84fb25a6ec56d395d98fb5467106d77dac0a95c63a1b',
}
COMPONENTS = [
    'low_linear_mass_through_500',
    'critical_linear_tail_majorant_above_500',
    'trivial_zero_majorant_at_1',
]


def interval(obj):
    lo, hi = F(obj['lower']), F(obj['upper'])
    if not 0 < lo <= hi:
        raise ArithmeticError('Invalid positive enclosure')
    return lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path,
                        default=Path(__file__).resolve().parent.parent /
                        'selective_loss_quadratic_target_20261003')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    for name, expected in INPUT_HASHES.items():
        if sha256((args.input_dir / name).read_bytes()).hexdigest() != expected:
            raise ArithmeticError('Source hash mismatch: ' + name)

    b_upper = F(124, 25)
    r_upper = F(39, 25) / 10**51
    imported = []
    for bits in [192, 256]:
        r = json.loads((args.input_dir / f'bound_{bits}.json').read_text())
        if (r['status'] != 'CERTIFIED_FINITE_CONTINUUM_CONSTANTS'
                or r['bits'] != bits
                or r['script_sha256'] != INPUT_HASHES['certify.py']
                or r['computed_zero_count_at_500'] != 269
                or not r['both_zero_signs_included']
                or r['published_verified_height'] != '3000000000000'):
            raise ArithmeticError('Unexpected imported certificate scope')
        en = {k: interval(v) for k, v in r['enclosures'].items()}
        b_en = (sum(en[k][0] for k in COMPONENTS),
                sum(en[k][1] for k in COMPONENTS))
        r_en = en['unknown_linear_tail_constant']
        if not b_en[1] < b_upper or not r_en[1] < r_upper:
            raise ArithmeticError('Rational coefficient rounding failed')
        imported.append({'bits': bits, 'b': [str(v) for v in b_en],
                         'R_H': [str(v) for v in r_en]})
    for key in ['b', 'R_H']:
        left, right = [tuple(F(v) for v in r[key]) for r in imported]
        if max(left[0], right[0]) > min(left[1], right[1]):
            raise ArithmeticError('Imported enclosures do not overlap')

    # (283/50)^2 > 32, so 2^(5/2)<283/50.
    sqrt32_upper = F(283, 50)
    if not sqrt32_upper**2 > 32:
        raise ArithmeticError('Cross coefficient enclosure failed')
    cross_upper = F(4, 5)*(sqrt32_upper-1)
    rows = []
    for power, ceiling in [(99, 38), (100, 40), (102, 72)]:
        xmax = 10**power
        sqrt_x_upper = (F(16, 5)*10**((power-1)//2)
                        if power % 2 else F(10**(power//2)))
        if sqrt_x_upper**2 < xmax:
            raise ArithmeticError('Square-root range enclosure failed')
        budget = (F(3, 2)*b_upper**2
                  + cross_upper*b_upper*r_upper*sqrt_x_upper
                  + F(7, 3)*r_upper**2*xmax)
        if not budget < ceiling:
            raise ArithmeticError('Finite-range threshold failed')
        rows.append({'X_min': 'e', 'X_max': str(xmax),
                     'X_max_power_of_ten': power,
                     'sqrt_X_max_upper': str(sqrt_x_upper),
                     'normalized_budget_upper': str(budget),
                     'strict_variance_coefficient': ceiling})
    record = {
        'date': '2026-10-03', 'prepared_for': 'Edward Baker',
        'model': 'GPT-6 (Codex)', 'serving_variant': 'not exposed; not inferred',
        'reasoning_effort': 'not exposed; not inferred',
        'llm_acknowledgement': 'Prepared with substantial LLM assistance.',
        'status': 'PASS_RATIONAL_FINITE_DYADIC_VARIANCE_TRANSFER',
        'input_sha256': INPUT_HASHES,
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'imported_enclosures': imported,
        'rational_upper_bounds': {'b': str(b_upper), 'R_H': str(r_upper),
                                  'cross_coefficient': str(cross_upper)},
        'complete_shell_formula':
            '(3/2)b^2 X^2 + (4/5)(2^(5/2)-1)b R_H X^(5/2) + (7/3)R_H^2 X^3',
        'finite_continuum_conclusions': rows,
        'external_inputs': [
            'Complete linear explicit formula for the exact prepared probe.',
            'Published Platt-Trudgian RH verification through height 3e12.',
            'Published zero-count majorant N(t)<=t log(t), t>=100.',
            'Previously generated 192/256-bit outward low-zero and tail records.',
        ],
        'limitations': [
            'All-real-X statements only in the displayed finite ranges.',
            'No smaller fixed global delta and no global RH claim.',
            'A rational transfer check, not a new verification of the zeros or analytic inputs.',
            'Linear coefficient tail H^-5 log(H); cubic variance tail H^-10 log(H)^2.',
        ],
    }
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status': record['status'],
                     'thresholds': [
                         {'X_max': '10^'+str(r['X_max_power_of_ten']),
                          'coefficient': r['strict_variance_coefficient'],
                          'budget': str(float(F(r['normalized_budget_upper'])))}
                         for r in rows]}))


if __name__ == '__main__':
    main()
