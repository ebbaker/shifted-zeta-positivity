#!/usr/bin/env python3
"""Regenerate a fixed new 104--108 or 108--112 complete-source rectangle.

Prepared for Edward Baker, 2026-10-14, with substantial LLM assistance.
Recorded parent model: gpt-6.1-sol, reasoning effort ultra.
The imported historical driver is unchanged. Its original 1/9 cone test
retains its own PASS/INCOMPLETE result; successful stationary signs and
nonvanishing are reported separately and verified by the exact auditor.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace

import certify_phase_centered_residual as core


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--x-left', type=int, choices=(104,108), required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    with tempfile.TemporaryDirectory(prefix='inv21-fixed-cusp-') as tmp:
        raw = Path(tmp)/'historical-driver-output.json'
        parameters = SimpleNamespace(
            x_left=str(args.x_left), x_right=str(args.x_left+4), width='1',
            time_slabs=8, bits=192, space_order=12, time_order=8,
            B_squared='1/9', output=raw)
        cone_return = core.run(parameters)
        record = json.loads(raw.read_text())
        historical_metadata = {key:record[key] for key in
                               ('recorded_model','recorded_effort')}
        record.update({
            'recorded_model':'gpt-6.1-sol', 'recorded_effort':'ultra',
            'historical_driver_hardcoded_attribution':historical_metadata,
            'execution_wrapper_name':Path(__file__).name,
            'execution_wrapper_sha256':digest(__file__),
            'execution_wrapper_protocol':{
                'each_band_declared_before_its_first_evaluation':True,
                'joint_blind_predeclaration':False,
                'declaration_sequence':[
                    'Declare104--108 with unit spatial cells,8time slabs,192bits,orders12/8,and unchanged1/9cone before evaluating that band.',
                    'After104--108 successfully resolved all stationary signs and norms,declare the adjacent108--112 extension with identical parameters before its first evaluation.',
                    'Fix half-time filter a=pi/16,b=1/4,lambda=1/2,K0=K1=0 before evaluating new branch products; identify all branch cells from paid current-jet enclosures.'],
                'first_band':['104','108'], 'second_band':['108','112'],
                'same_parameters_for_both_bands':True,
                'a':'pi/16', 'N':8, 'U':'3/2', 'width':'1',
                't':['0','1/2'], 'time_slabs':8,
                'bits':192, 'space_order':12, 'time_order':8,
                'B_squared':'1/9', 'filter_adjusted_after_observation':False},
            'historical_driver_return_code':cone_return,
            'stationary_sign_status':
                'PASS' if record['all_stationary_observations_resolved'] else 'INCOMPLETE',
            'norm_status':
                'PASS' if all(c['norm_positive'] for c in record['cells']) else 'INCOMPLETE',
            'status_explanation':
                'The unchanged status and failed_cells fields concern the original uniform 1/9 residual-cone test. Stationary-sign and norm conclusions have separate fields; none converts an unsuccessful cone enclosure into a negative mathematical sign.',
        })
        args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({key:record[key] for key in
                     ('domain','status','stationary_sign_status','norm_status',
                      'cell_count','all_stationary_observations_resolved')},indent=2))
    return 0 if record['stationary_sign_status']==record['norm_status']=='PASS' else 1


if __name__=='__main__':
    raise SystemExit(main())
