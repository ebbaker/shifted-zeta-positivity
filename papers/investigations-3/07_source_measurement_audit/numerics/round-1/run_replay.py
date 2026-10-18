#!/usr/bin/env python3
"""Rebuild the fixed round-1 replay and its small portable records.

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol, reasoning effort ultra. Requires mpmath and
python-flint. Full floating outputs are regenerable working data; only the
certificates, compact witnesses and small summary need to be retained.
"""
import argparse
import hashlib
import itertools
import json
import platform
import resource
import subprocess
import sys
import time
from pathlib import Path
import mpmath as mp
from replay_record_hygiene import CONTENT_HASH_POLICY, mathematical_content_digest, peak_rss_bytes

def read(p):return json.loads(p.read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main(out, original):
    started=time.monotonic();here=Path(__file__).resolve().parent;out.mkdir(parents=True,exist_ok=True)
    def run(name,*args):
        subprocess.run([sys.executable,str(here/name),*map(str,args)],check=True)
    for dps in (80,120):
        extra=['--compare-record',original] if original else []
        run('replay_measurements.py','--dps',dps,'--output-dir',out,*extra)
        run('replay_feasibility.py',out/f'EVALUATION_DPS{dps}.json',out/f'FEASIBILITY_DPS{dps}.json')
    full=read(out/'FEASIBILITY_DPS120.json');compact=[]
    for c in full['cases']:
        v={k:c[k] for k in ('point_id','t','x','N','tail','anchor_a1')}
        v['equality']={'augmented_minor':c['equality'].get('augmented_minor')}
        sep=c['positive'].get('strict_farkas_separator')
        v['positive']={'strict_farkas_separator':{'normalized_point_multiplier':sep['normalized_point_multiplier']}} if sep else {}
        compact.append(v)
    witness=out/'FEASIBILITY_WITNESSES.json'
    witness.write_text(json.dumps({'schema':'source_measurement_compact_witnesses_v1',
        'date':'2026-10-17','prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra',
        'status':'rational decimal candidates; signs are verified separately',
        'generator_sha256':digest(here/'replay_feasibility.py'),'cases':compact},indent=2)+'\n')
    run('certify_evaluation.py','--output',out/'CERTIFIED_EVALUATION.json')
    run('certify_measurements.py','--evaluation',out/'CERTIFIED_EVALUATION.json','--output',out/'CERTIFIED_MEASUREMENTS.json')
    run('certify_feasibility.py','--evaluation',out/'CERTIFIED_EVALUATION.json','--candidates',witness,'--output',out/'CERTIFIED_FEASIBILITY.json')
    run('check_analytic_bounds.py','--evaluation',out/'CERTIFIED_EVALUATION.json','--output',out/'ANALYTIC_BOUND_CHECKS.json')
    mp.mp.dps=140
    cmp=read(out/'PRECISION_AND_ORIGINAL_COMPARISON.json')
    lo=read(out/'FEASIBILITY_DPS80.json');hi=read(out/'FEASIBILITY_DPS120.json')
    assert len(lo['cases'])==len(hi['cases'])==32
    difference=mp.mpf(0)
    for a,b in zip(lo['cases'],hi['cases']):
        assert a['positive']['status']==b['positive']['status'] and a['equality']['status']==b['equality']['status']
        for av,bv in zip(a['equality']['a_first_N'],b['equality']['a_first_N']):
            difference=max(difference,abs(mp.mpf(av)-mp.mpf(bv))/max(1,abs(mp.mpf(bv))))
    fields=['C_relative_80_vs_120','eta_sufficient_exclusion_radius_relative_80_vs_120',
            'actual_equality_measurement_distance_relative_80_vs_120']
    summary={'schema':'source_measurement_round1_summary_v1','date':'2026-10-17',
        'prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra',
        'python_version':platform.python_version(),'precision_comparison_status':'diagnostic; independent interval records establish enclosures',
        'fixed_case_counts':{'observations':6,'conditioning_combinations':24,'feasibility_combinations':32},
        'max_precision_relative_differences':{k:mp.nstr(max(mp.mpf(v[k]) for v in cmp['conditioning']),25) for k in fields},
        'max_feasibility_coefficient_scaled_precision_difference':mp.nstr(difference,25),
        'all_feasibility_precision_classifications_agree':True,
        'max_baseline_h_relative_precision_difference':mp.nstr(max(mp.mpf(v['h_relative_l2_80_vs_120']) for v in cmp['cases']),25),
        'certificate_totals':read(out/'CERTIFIED_FEASIBILITY.json')['totals'],
        'elapsed_seconds':time.monotonic()-started,
        'platform_system':platform.system(),
        'largest_child_peak_rss_bytes':peak_rss_bytes(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,platform.system()),
        'replay_budget_seconds':1800,'memory_budget_bytes':1073741824,
        'no_threshold_or_support_sweep':True}
    if original:
        summary['original_record_sha256']=digest(original)
        summary['max_original_C_relative_difference']=mp.nstr(max(mp.mpf(v['C_relative_original_vs_120']) for v in cmp['conditioning']),25)
        summary['original_x85_h_relative_difference']=next(v['h_relative_l2_original_vs_120'] for v in cmp['cases'] if v['case']=='t0_x85')
    names=['CERTIFIED_EVALUATION.json','CERTIFIED_MEASUREMENTS.json','CERTIFIED_FEASIBILITY.json','ANALYTIC_BOUND_CHECKS.json','FEASIBILITY_WITNESSES.json']
    summary['record_sha256']={n:digest(out/n) for n in names}
    summary['content_hash_policy']=CONTENT_HASH_POLICY
    summary['record_content_sha256']={n:mathematical_content_digest(read(out/n)) for n in names}
    summary['code_sha256']={p.name:digest(p) for p in sorted(here.glob('*.py'))}
    summary['mathematical_content_sha256']=mathematical_content_digest(summary)
    (out/'REPLAY_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    assert summary['elapsed_seconds']<1800 and summary['largest_child_peak_rss_bytes']<1073741824
    print('ROUND_REPLAY_COMPLETE',json.dumps(summary),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',type=Path,required=True)
    p.add_argument('--original-record',type=Path);a=p.parse_args();main(a.output_dir,a.original_record)
