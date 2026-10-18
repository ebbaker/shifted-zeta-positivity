#!/usr/bin/env python3
"""Rebuild the bounded analytic records and compare fresh 192/256-bit replay.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Recorded execution configuration: gpt-6.1-sol, reasoning effort ultra.
This replays scalar/exact claims; it does not certify the open global bridge.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time
import flint
from flint import arb,ctx

BASE='papers/investigations-3/11_arithmetic_collision_rigidity'

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def require(ok,why):
    if not ok: raise ArithmeticError(why)
def run(argv):
    start=time.perf_counter()
    done=subprocess.run(argv,check=True,capture_output=True,text=True)
    return time.perf_counter()-start,done.stdout

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output-dir',type=Path,required=True)
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    p.add_argument('--verify-reference',type=Path)
    args=p.parse_args()
    repo=args.repo.resolve(); dest=args.output_dir.resolve();dest.mkdir(parents=True,exist_ok=True)
    src=repo/BASE/'numerics/analytic_continuation'
    if args.verify_reference:
        reference=json.loads(args.verify_reference.read_text())
        for rel,expected in reference['source_sha256'].items():
            require(digest(repo/rel)==expected,'changed reference source: '+rel)
    runs=[];ctx.prec=256
    with tempfile.TemporaryDirectory(prefix='acr-analytic-replay-') as temporary:
        tmp=Path(temporary)
        records={}
        for bits in (192,256):
            target=dest if bits==192 else tmp
            outer=target/'OUTER20_EXCLUSION_20261018.json'
            constant=target/'CONSTANT_DISTANCE_TAIL_20261018.json'
            seconds,_=run([sys.executable,str(src/'certify_outer20_exclusion.py'),'--repo',str(repo),'--output',str(outer),'--precision',str(bits),'--execution-model',args.execution_model,'--execution-effort',args.execution_effort])
            runs.append({'case':'outer20','precision_bits':bits,'total_seconds_including_process_start':seconds})
            seconds,_=run([sys.executable,str(src/'certify_constant_distance_tail.py'),'--output',str(constant),'--bits',str(bits),'--execution-model',args.execution_model,'--execution-effort',args.execution_effort])
            runs.append({'case':'constant_distance','precision_bits':bits,'total_seconds_including_process_start':seconds})
            records[bits]=(json.loads(outer.read_text()),json.loads(constant.read_text()))
        remote=dest/'REMOTE_COLLISION_CONTROL_20261018.json'
        seconds,_=run([sys.executable,str(src/'check_remote_polynomial_control.py'),'--output',str(remote),'--execution-model',args.execution_model,'--execution-effort',args.execution_effort])
        runs.append({'case':'remote_polynomial','arithmetic':'exact rational','total_seconds_including_process_start':seconds})
        n_overlap=0
        for name,value in records[192][0]['scalar_enclosures'].items():
            require(arb(value).overlaps(arb(records[256][0]['scalar_enclosures'][name])),'outer precision disagreement: '+name)
            n_overlap+=1
        for lo,hi in zip(records[192][1]['records'],records[256][1]['records'],strict=True):
            for name in ('q_star','B_star','eta','C_X','uniform_bound_at_X'):
                require(arb(lo[name]).overlaps(arb(hi[name])),'constant-distance precision disagreement: '+name)
                n_overlap+=1
        primary=records[192][0]
        require(all(primary['strict_checks'].values()),'failed outer scalar comparison')
        require(len(primary['invalid_parameter_rejections'])==5,'missing outer negative guards')
        for rel,expected in primary['source_sha256'].items():
            require(digest(repo/rel)==expected,'changed inherited input: '+rel)
        require(primary['script_sha256']==digest(src/'certify_outer20_exclusion.py'),'outer script identity')
        require(records[192][1]['source_sha256']==digest(src/'certify_constant_distance_tail.py'),'constant script identity')
        remote_data=json.loads(remote.read_text())
        require(remote_data['status']=='PASS','remote exact control failed')
        require(remote_data['script_sha256']==digest(src/'check_remote_polynomial_control.py'),'remote script identity')
    rels=[
        BASE+'/notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md',
        BASE+'/notes/02_updated_research_plan/12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md',
        BASE+'/notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md',
        BASE+'/notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md',
        'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex',
        BASE+'/numerics/high_height_consumer/HIGH_HEIGHT_CONSUMER_LEDGER_20261018.json',
    ]+[BASE+'/numerics/analytic_continuation/'+name for name in (
        'certify_outer20_exclusion.py','certify_constant_distance_tail.py','check_remote_polynomial_control.py','replay_analytic_continuation.py')]
    report={
        'date':'2026-10-18','prepared_for':'Edward Baker','actual_model':args.execution_model,
        'actual_effort':args.execution_effort,'llm_assistance':'substantial; internal same-model derivation and replay',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'status':'PASS: auxiliary analytic/exact replay; global route remains open',
        'source_sha256':{r:digest(repo/r) for r in rels},
        'records_sha256':{f.name:digest(f) for f in (dest/'OUTER20_EXCLUSION_20261018.json',dest/'CONSTANT_DISTANCE_TAIL_20261018.json',remote)},
        'all_192_256_scalar_intersections':n_overlap,'outer_strict_scalar_checks':len(primary['strict_checks']),
        'outer_negative_parameter_rejections':len(primary['invalid_parameter_rejections']),
        'runs':runs,'total_measured_seconds':sum(r['total_seconds_including_process_start'] for r in runs),
        'finite_consumer_status':'inherited unchanged; prior 256-bit and real-source cell replay not rerun',
        'remaining_slab':{'time':['1/100','1/5'],'absolute_height_open':['1001','exp(2000)']},
        'new_newman_bound':False,
    }
    (dest/'ANALYTIC_CONTINUATION_REPLAY_20261018.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'intersections':n_overlap,'seconds':report['total_measured_seconds']}))
if __name__=='__main__': main()
