#!/usr/bin/env python3
"""Check source bindings and rational endpoints of the saved scalar certificates.

Prepared for Edward Baker with GPT-6 (Codex), 2026-10-03.
Exact serving variant and configured reasoning effort were not exposed.
This is a record audit, not an independent implementation of the analytic proof.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--package', type=Path, default=Path(__file__).resolve().parent)
parser.add_argument('--diagonal', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
script_hash = sha256((args.package/'certify_zero_tail.py').read_bytes()).hexdigest()
diagonal_raw = args.diagonal.read_bytes()
diagonal_hash = sha256(diagonal_raw).hexdigest()
diagonal = json.loads(diagonal_raw)
records = [json.loads((args.package/f'zero_tail_{bits}.json').read_text())
           for bits in (192, 256)]
limits = {'delta_T': '1.058e-116', 'horizon_tail_cost': '3.961e-8',
          'archimedean_remainder_bound_at_2': '0.01237498726501953',
          'continuum_absolute_bound': '1.47931505787654'}
for rec, bits in zip(records, (192, 256)):
    if rec['bits'] != bits or rec['script_sha256'] != script_hash:
        raise ArithmeticError('Script or precision binding failed')
    if rec['diagonal_certificate_sha256'] != diagonal_hash:
        raise ArithmeticError('Diagonal source binding failed')
    if F(rec['imported_Q_upper']) != F(diagonal['Q_diagonal']['upper']):
        raise ArithmeticError('Imported diagonal endpoint mismatch')
    if rec['status'] != 'CERTIFIED_CONTINUUM_ABSOLUTE_BOUND_LT_1_48_ON_2_TO_500':
        raise ArithmeticError('Unexpected status')
    for key, cap in limits.items():
        lo, hi = (F(rec[key][side]) for side in ('lower', 'upper'))
        if not 0 < lo <= hi < F(cap):
            raise ArithmeticError(f'Outward comparison failed: {key}')
for key in limits:
    low = max(F(rec[key]['lower']) for rec in records)
    high = min(F(rec[key]['upper']) for rec in records)
    if low > high:
        raise ArithmeticError(f'Precision intervals do not overlap: {key}')
for key in ('source_norm_squared', 'interior_sixth_derivative_norm_squared',
            'boundary_atom_total_variation', 'interior_L1_upper_integer',
            'sixth_distributional_derivative_TV_upper_integer', 'K_squared',
            'published_RH_verified_height', 'zero_count_majorant', 'interval_r'):
    if records[0][key] != records[1][key]:
        raise ArithmeticError(f'Invariant data mismatch: {key}')
record = {'status': 'PASS', 'date': '2026-10-03',
          'model': 'GPT-6 (Codex)', 'reasoning_effort': 'not exposed',
          'serving_variant': 'not exposed', 'checked_precisions': [192, 256],
          'checked_upper_limits': limits, 'script_sha256': script_hash,
          'diagonal_certificate_sha256': diagonal_hash,
          'replay_script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
          'certificate_sha256': {str(bits): sha256((args.package/f'zero_tail_{bits}.json').read_bytes()).hexdigest()
                                 for bits in (192, 256)},
          'scope': 'Rational endpoint and source-binding audit; analytic proof and published verification are inputs.'}
args.output.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'comparisons': len(limits), 'precisions': [192, 256]}))
