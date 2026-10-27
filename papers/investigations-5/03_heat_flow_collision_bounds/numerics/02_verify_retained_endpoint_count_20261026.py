#!/usr/bin/env python3
"""Post-stop witness using retained completed pilot data; no source calls.

The original contour-integration protocol remains stopped. This verifies
a different analytical consequence of its earlier endpoint/corner balls.
Requires python-flint==0.9.0. See the associated research note for proofs.
"""
import argparse
import hashlib
import json
from pathlib import Path
import flint
from flint import arb, ctx


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--record', type=Path, required=True)
    parser.add_argument('--expected-sha256', required=True)
    parser.add_argument('--source-script', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    raw = args.record.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != args.expected_sha256:
        raise SystemExit('Retained record hash mismatch; refusing altered data')
    source = json.loads(raw)
    if hashlib.sha256(args.source_script.read_bytes()).hexdigest() != source['source_code_sha256']:
        raise SystemExit('Source script hash mismatch')
    if flint.__version__ != '0.9.0' or source['fixed_case']['m'] != 16:
        raise SystemExit('Unexpected version/case')
    if source['status'] != 'stopped' or source['failed_stage'] != 'continuous contour count':
        raise SystemExit('Unexpected raw-run provenance')

    tau = arb(source['fixed_case']['tau_X'])
    bounds = {}
    for c, floor in [('-4', arb('0.8144')), ('4', arb('0.2789'))]:
        point = source['endpoints'][c]
        F = arb(point['F']['real'])
        A = arb(point['A']['real']).abs_upper()
        Q = arb(point['Q']['real']).abs_upper()
        if not (2*tau*Q < 1):
            raise ArithmeticError('Gaussian moment fails '+c)
        error = 1-(-tau*A*A).exp()+(1-2*tau*Q).rsqrt()-1
        lower = (F.abs_lower()*(1-error.abs_upper())).lower()
        if not (error < arb(1)/2 and lower > floor):
            raise ArithmeticError('Recorded endpoint floor unsupported '+c)
        bounds[c] = {'transport_error_upper': error.abs_upper().str(50),
                     'recomputed_floor_lower': lower.str(50),
                     'certified_floor': floor.str(50)}

    left = arb(source['endpoints']['-4']['F']['real'])
    right = arb(source['endpoints']['4']['F']['real'])
    if not (left > 0 and right < 0):
        raise ArithmeticError('Required opposite endpoint signs unavailable')
    Pleft = arb(source['corners']['-4']['P'])
    Pright = arb(source['corners']['4']['P'])
    Psum = Pleft+Pright
    if not (Pleft > 0 and Pright > 0 and Psum < arb(2)/5):
        raise ArithmeticError('Two-corner population upper bound fails')
    # Every interior root contributes >=1/5 to Psum, exterior roots
    # contribute positively. Under RH, n <=5 Psum <2. Opposite real
    # signs imply n >=1, so n=1 counted with multiplicity.
    endpoint_common = arb('0.2789')
    full_wall = endpoint_common/4
    if not (full_wall > arb('0.0697')):
        raise ArithmeticError('Whole-wall rounding failed')
    record = {
        'date': '2026-10-26', 'timezone': 'America/New_York',
        'prepared_for': 'Edward Baker', 'llm_assistance': 'substantial',
        'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra',
        'thread_id': source['thread_id'], 'turn_id': source['turn_id'],
        'status': 'verified_post_stop_finite_witness_under_RH',
        'case_m': 16, 'precision_bits': ctx.prec, 'python_flint': flint.__version__,
        'raw_record_sha256': digest,
        'source_script_sha256': source['source_code_sha256'],
        'witness_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'original_protocol_status': source['status'],
        'original_protocol_failed_stage': source['failed_stage'],
        'new_source_evaluations': 0,
        'assumptions': ['RH', 'all-real order-one canonical product and exact-source Gaussian evolution'],
        'endpoint_bounds': bounds,
        'P_left': Pleft.str(50), 'P_right': Pright.str(50), 'P_sum': Psum.str(50),
        'count_upper_witness': (5*Psum).str(50),
        'count': 1, 'count_includes_multiplicity': True,
        'uniform_time_count': 1,
        'uniform_canonical_wall_lower': '0.0697',
        'full_wall_derivation': 'Count n=1 and endpoint common E=0.2789 give E/4^n=0.069725 >0.0697; all exterior zeros retained via concavity.',
        'not_established': ['Uniform-in-m endpoint/count data', 'Finite F_N mismatch/coefficient errors',
                            'Favorable Poisson model moment', 'Success of the stopped contour-count integration']
    }
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
