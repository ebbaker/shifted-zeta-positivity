#!/usr/bin/env python3
"""Fresh source-specific failure controls for Note 11.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Authoring: gpt-6.1-sol, actual effort ultra. Same-model internal replay.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

import flint
from flint import ctx


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--receipts',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--execution-model',required=True)
    parser.add_argument('--execution-effort',required=True)
    args=parser.parse_args()
    source=args.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/run_plan02_pilot.py'
    sys.path.insert(0,str(source.parent))
    from run_plan02_pilot import replay_controls,control_screen
    ctx.prec=192
    started=time.monotonic()
    expected=replay_controls(args.repo,args.receipts)
    screen=control_screen(args.repo,args.receipts,expected)
    if len(screen['event_rejections']) != 5 or not all(
            row['strict_first_jet_rejected'] and row['strict_signed_margin_rejected']
            for row in screen['event_rejections']):
        raise ArithmeticError('event screen failed')
    if not screen['euler_witness']['strict_signed_margin_rejected']:
        raise ArithmeticError('Euler witness screen failed')
    record={'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
            'actual_model':args.execution_model,'actual_effort':args.execution_effort,
            'llm_assistance':'substantial; same-model internal control replay',
            'python':platform.python_version(),'python_flint':flint.__version__,
            'interface_precision_bits':ctx.prec,
            'rounding':'outward Arb/Acb; imported source certificates retain their recorded precision',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'status':'fresh source-specific controls replayed; no theta tail constants substituted',
            'screen':screen,'seconds':time.monotonic()-started}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'event_rejections':5,'euler_witness_rejected':True}))

if __name__=='__main__':
    main()
