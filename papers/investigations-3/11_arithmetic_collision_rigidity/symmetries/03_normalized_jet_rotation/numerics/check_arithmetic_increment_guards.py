#!/usr/bin/env python3
"""Fail-closed input guard checks for the independent G3 increment consumer.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Execution model and effort are supplied explicitly. No valid model rerun,
source H values, source quadrature, or event-acceptance claim is involved.
"""
from __future__ import annotations
import argparse, copy, hashlib, json, os, platform, subprocess, sys, tempfile, time
from pathlib import Path
import flint

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/03_normalized_jet_rotation'
CONSUMER=LANE/'numerics/estimate_arithmetic_residual_increment.py'
PRODUCER=LANE/'numerics/bound_complete_rs_edge.py'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def require(condition,message):
    if not condition:raise ArithmeticError(message)
def wrong_digest(digest):return ('0' if digest[0]!='0' else '1')+digest[1:]

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',required=True,type=Path)
    p.add_argument('--edge-record',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    args=p.parse_args();repo=args.repo.resolve();edge=args.edge_record.resolve()
    baseline=json.loads(edge.read_text())
    # Static provenance validation only. The unaltered numerical consumer is
    # replayed separately by the author/reviewer, never by this guard program.
    require(baseline['script_sha256']==sha(repo/PRODUCER),'baseline producer pin')
    require(baseline['retained_model']['sha256']==sha(repo/CONSUMER),'baseline model pin')
    for path,digest in baseline['source_sha256'].items():
        require(sha(repo/path)==digest,'baseline dependency pin: '+path)
    require(baseline['runs'] and {192,256}<=set(v['requested_bits'] for v in baseline['runs']),
            'baseline complete precision coverage')
    require(all(v['normalized_value_cap']=='6e-8' and v['physical_disk_radius']=='1'
               and v['normalized_first_x_cap']=='6e-8'
               and v['normalized_second_x_cap']=='1.2e-7' for v in baseline['runs']),
            'baseline edge caps and disk radius')
    require(256 in [v['requested_bits'] for v in baseline['runs']],
            'missing-precision case has a precision to remove')
    source_path=sorted(baseline['source_sha256'])[0]
    cases=[]
    for name in ['altered_edge_producer_hash','altered_model_hash','altered_source_hash',
                 'missing_precision','empty_runs','changed_value_cap','changed_radius']:
        altered=copy.deepcopy(baseline)
        if name=='altered_edge_producer_hash':
            altered['script_sha256']=wrong_digest(altered['script_sha256'])
            expected='complete edge producer pin';field='script_sha256'
        elif name=='altered_model_hash':
            altered['retained_model']['sha256']=wrong_digest(altered['retained_model']['sha256'])
            expected='edge polynomial model pin';field='retained_model.sha256'
        elif name=='altered_source_hash':
            altered['source_sha256'][source_path]=wrong_digest(altered['source_sha256'][source_path])
            expected='complete edge source pin: '+source_path;field='source_sha256.'+source_path
        elif name=='missing_precision':
            altered['runs']=[v for v in altered['runs'] if v['requested_bits']!=256]
            expected='edge precision coverage';field='runs: remove requested_bits=256'
        elif name=='empty_runs':
            altered['runs']=[];expected='complete edge cap';field='runs'
        elif name=='changed_value_cap':
            altered['runs'][0]['normalized_value_cap']='7e-8'
            expected='complete edge cap';field='runs[0].normalized_value_cap'
        elif name=='changed_radius':
            altered['runs'][0]['physical_disk_radius']='1/2'
            expected='complete edge cap';field='runs[0].physical_disk_radius'
        # Each isolated case has a new temporary input and nonexistent output.
        with tempfile.TemporaryDirectory(prefix='g3-increment-guard-') as tempname:
            temp=Path(tempname);record=temp/'altered-edge.json';result=temp/'must-not-exist.json'
            record.write_text(json.dumps(altered,sort_keys=True,indent=2)+'\n')
            argv=[sys.executable,str(repo/CONSUMER),'--repo',str(repo),'--edge-record',str(record),
                  '--output',str(result),'--bits','192','256',
                  '--execution-model',args.execution_model,'--execution-effort',args.execution_effort]
            started=time.monotonic()
            child=subprocess.run(argv,cwd=repo,env=os.environ.copy(),text=True,capture_output=True,timeout=15)
            elapsed=time.monotonic()-started
            stderr=child.stderr.strip();stdout=child.stdout.strip()
            error=stderr.splitlines()[-1] if stderr else ''
            passed=child.returncode!=0 and not result.exists() and expected in error and not stdout
            cases.append({'case':name,'altered_field':field,'input_sha256':sha(record),
                          'expected_guard':expected,'returncode':child.returncode,
                          'output_created':result.exists(),'stdout_empty':not stdout,
                          'captured_error':error[:500],'observed_seconds':elapsed,'passed':passed})
            require(passed,'consumer guard did not fail at expected boundary: '+name+' '+error)
    result={'date':'2026-10-19','prepared_for':'Edward Baker',
       'actual_model':args.execution_model,'actual_effort':args.execution_effort,
       'llm_assistance':'substantial; internal same-model bounded input validation',
       'python':platform.python_version(),'python_flint':flint.__version__,
       'child_python_matches_parent':True,'script_sha256':sha(__file__),
       'source_sha256':{str(v):sha(repo/v) for v in [CONSUMER,PRODUCER]},
       'complete_edge_record_sha256':sha(edge),
       'complete_edge_dependency_pins':baseline['source_sha256'],
       'source_H_values_used':False,'source_quadrature_used':False,
       'valid_numerical_consumer_rerun':False,'requested_consumer_bits':[192,256],
       'case_isolation':'A fresh TemporaryDirectory, altered input, and nonexistent output per case; removed after validation.',
       'all_passed':all(v['passed'] for v in cases),'case_count':len(cases),'cases':cases,
       'scope':'Fail-closed input guard validation only; no new estimate, acceptance consumer, collision exclusion, or independent mathematical review.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'cases':len(cases),'all_passed':result['all_passed']}))
if __name__=='__main__':main()
