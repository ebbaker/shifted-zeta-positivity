#!/usr/bin/env python3
"""Complete a fixed suffix after the bounded sharp transfer gate run.
Prepared for Edward Baker, substantial LLM assistance, gpt-6.1-sol (Codex),
reasoning effort ultra, 17 October 2026. Same-model internal certificate.
"""
import argparse, hashlib, importlib.util, json, resource, sys
from pathlib import Path
CORE_SHA='aa6c73e0aa6672b5e6706f704b0a8dda42f1a572d9cd2a3766c91a61bebf6792'
START=172

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--directory',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();core_path=a.directory/'check_sharp_y_transfer_gate.py'
    first_path=a.directory/'SHARP_Y_TRANSFER_GATE_RECORD_20261017.json'
    plan_path=a.directory/'GATE_COMPLETION_PLAN_20261017.md'
    assert sha(core_path)==CORE_SHA,'gate engine hash mismatch'
    first=json.loads(first_path.read_text())
    assert first['code_sha256']==CORE_SHA
    assert first['plan_sha256']==sha(a.directory/'GATE_RUN_PLAN_20261017.md')
    assert first['t']=='157/1000' and first['y_squared']==['87677/2500000','343/500']
    assert first['memory_budget_pass'] and first['selftest']['passed']
    legs={r['leg']:r for r in first['legs']}
    assert set(legs)=={0,1,2,3} and all(legs[i]['passed'] for i in (1,2,3))
    prefix=legs[0]
    assert prefix['completed_patterns']==list(range(START))
    assert prefix['unresolved_leaf_count']==0
    assert prefix['stop_reason']=='box_budget'
    assert prefix['pending'][0]['pattern_index']==START
    spec=importlib.util.spec_from_file_location('bounded_sharp_gate_core',core_path)
    core=importlib.util.module_from_spec(spec);sys.modules[spec.name]=core;spec.loader.exec_module(core)
    OriginalLeg=core.Leg
    original=OriginalLeg(0)
    assert len(original.patterns)==243
    class SuffixLeg(OriginalLeg):
        def __init__(self,idx):
            assert idx==0
            super().__init__(idx)
            self.patterns=self.patterns[START:]
    core.Leg=SuffixLeg
    result=core.certify_leg(0,45,30000,36)
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak=rss if sys.platform=='darwin' else rss*1024
    memory=peak<512*1024**2
    # Completion indices are local to the fixed suffix. Check their exact union.
    global_completed=[START+i for i in result['completed_patterns']]
    union=sorted(prefix['completed_patterns']+global_completed)
    complete=result['passed'] and memory and result['seconds']<=45 and union==list(range(243))
    rec=dict(date='2026-10-17',prepared_for='Edward Baker',model='gpt-6.1-sol',reasoning_effort='ultra',
        status='outward transfer-gate completion only; not a Newman bound',
        code_sha256=sha(Path(__file__)),core_code_sha256=CORE_SHA,
        first_record_sha256=sha(first_path),plan_sha256=sha(plan_path),
        original_leg_N=list(original.__dict__[k] for k in ('nlo','nhi')),
        original_leg_primes=list(original.P),prefix_pattern_indices=prefix['completed_patterns'],
        suffix_start=START,suffix_pattern_labels=[p.label() for p in original.patterns[START:]],
        suffix_result=result,global_suffix_completed_indices=global_completed,
        other_complete_leg_indices=[1,2,3],peak_resident_bytes=peak,memory_budget_pass=memory,
        full_four_leg_transfer_certified=complete)
    a.output.write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(dict(full_four_leg_transfer_certified=complete,seconds=result['seconds'],
        evaluated=result['evaluated'],accepted=result['accepted'],stop_reason=result['stop_reason'],
        global_suffix_completed=len(global_completed),peak_resident_bytes=peak)))

if __name__=='__main__':main()
