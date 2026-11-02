#!/usr/bin/env python3
"""Exact record/replay checks for J-E03, 1 November 2026.

Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol (Codex), effort ultra.
This checks the fixed certificate's data and replay, not the analytic proof.
Standard library only. The supplied replay must use the unchanged E02 program.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


def value(pair):
    return F(int(pair[0]))*F(2)**pair[1]


def check_balls(obj):
    count=0
    if isinstance(obj,dict):
        if all(k in obj for k in ['mid','radius','lower','upper']):
            m,r,l,h=(value(obj[k]) for k in ['mid','radius','lower','upper'])
            assert r>=0 and l<=m-r and h>=m+r
            count+=1
        for v in obj.values():count+=check_balls(v)
    elif isinstance(obj,list):
        for v in obj:count+=check_balls(v)
    return count


def stable(record):
    return {k:v for k,v in record.items() if k not in
            ['arithmetic_elapsed_seconds','prior_arithmetic_seconds','total_arithmetic_seconds']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--replay',type=Path,required=True)
    args=parser.parse_args();repo=args.repo.resolve()
    route=repo/'papers/investigations-5/07_positive_theta_primitives/jensen'
    fixed=route/'numerics/J_E02_R1_INTERVAL_RECORD_20261101.json'
    assert sha256(fixed.read_bytes()).hexdigest()=='cc5266c631e6cdbd9ef7d966a82969e5703da133e6adc5f2c1ab2badcee76b6b'
    r=json.loads(fixed.read_text());replayed=json.loads(args.replay.read_text())
    assert r['status']==replayed['status']=='certified'
    assert stable(r)==stable(replayed)
    assert sha256((route/'numerics/j_e02_certificate.py').read_bytes()).hexdigest()==r['code_sha256']
    for name,h in r['input_sha256'].items():
        assert sha256((route/name).read_bytes()).hexdigest()==h,name
    serialized_balls=check_balls(r)
    O,M=r['origin'],r['middle']
    assert O['status']==M['status']=='certified'
    assert len(O['cells'])==1 and len(M['cells'])==126
    assert len(O['attempts'])==1 and len(M['attempts'])==126
    acquisition=O['attempts'][0]['acquisition']
    assert acquisition['precision']==128
    assert len(acquisition['source_coefficients'])==71
    assert len(acquisition['U_coefficients'])==32 and len(acquisition['V_coefficients'])==30
    for j,b in enumerate(acquisition['source_coefficients']):
        if j%2:assert value(b['mid'])==value(b['radius'])==0
    oc=O['cells'][0]
    assert F(oc['left'])==0 and F(oc['right'])==F(1,4096)
    assert value(oc['U_lower']['lower'])>1762
    assert value(oc['V_lower']['lower'])>F(2)**54
    cells=sorted(M['cells'],key=lambda c:F(c['left']))
    for j,c in enumerate(cells):
        assert F(c['left'])==F(j+2,128) and F(c['right'])==F(j+3,128)
        assert c['precision']==128 and c['depth']==0 and c['status']=='certified'
        assert value(c['A_lower']['lower'])>F(2)**-17
        assert value(c['N_lower']['lower'])>F(2)**-86
    assert F(cells[0]['left'])**2==F(oc['right']) and F(cells[-1]['right'])==1
    assert oc['precision']==128 and oc['depth']==0 and oc['status']=='certified'

    # Inspect the actual exact numerator data as well as its status flags.
    arpath=route/'numerics/J_E02_R1_ALGEBRA_RECORD_20261101.json'
    ar=json.loads(arpath.read_text())
    assert sha256((route/'numerics/j_e02_algebra_audit.py').read_bytes()).hexdigest()==ar['code_sha256']
    N={tuple(e):F(c) for e,c in ar['joint_N']}
    assert len(N)==29 and sum(abs(c) for c in N.values())==76
    assert all(sum(e)==6 and sum(j*k for j,k in enumerate(e))==13 for e in N)
    v=json.loads((route/'numerics/J_E02_R1_REPLAY_VALIDATION_20261101.json').read_text())
    for name,h in v['artifact_sha256'].items():
        assert sha256((route/'numerics'/name).read_bytes()).hexdigest()==h

    paths=['AGENTS.md','GPT_RESEARCH_MODEL_WORKFLOW.md','LARGE_FILES.md','tools/CHAT_HISTORY.md']
    relative=route.relative_to(repo)
    paths += [str(relative/x) for x in ['notes/03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md',
             'notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md',
             'notes/07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md',
             'notes/09_J_B02_GLOBAL_TAIL_AND_COMPACT_CERTIFICATE_20261101.md',
             'notes/11_J_E02_R1_GLOBAL_SIGN_CERTIFICATE_RETURN_20261101.md',
             'notes/12_CONTINUATION_FOR_SOL_J_E03_GLOBAL_SIGN_ASSESSMENT_20261101.md',
             'numerics/j_e02_certificate.py','numerics/j_e02_algebra_audit.py',
             'numerics/J_E02_R1_INTERVAL_RECORD_20261101.json',
             'numerics/J_E02_R1_ALGEBRA_RECORD_20261101.json',
             'numerics/J_E02_R1_REPLAY_VALIDATION_20261101.json']]
    result=dict(date='2026-11-01',prepared_for='Edward Baker',llm_assistance='substantial',
        model='gpt-6.1-sol',effort='ultra',task='J-E03',scope='fixed E02 r1 certificate; analytical assessment is in Review01',
        code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        input_sha256={p:sha256((repo/p).read_bytes()).hexdigest() for p in paths},
        replay_arithmetic_seconds=replayed['arithmetic_elapsed_seconds'],
        replay_versions=replayed['arithmetic'],replay_non_timing_fields_identical=True,
        interval_non_timing_content_sha256=sha256(json.dumps(stable(r),sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        exact_dyadic_enclosures_checked=serialized_balls,
        record_checks=dict(input_and_code_hashes=True,ball_endpoint_consistency=True,
            full_exact_cover=True,origin_parity=True,positive_after_error_margins=True,
            all_128_bits_depth_zero=True,no_extra_cells_or_orders=True,actual_N_degree_and_coefficients=True),
        leaf_count=dict(origin=1,middle=126),conservative_lower_bounds=dict(origin_U='1762',origin_V='2^54',middle_A='2^-17',middle_N='2^-86'),
        review_relationship='same authoring assistant and model; fresh contributing same-model read-only checks; no independent specialist review')
    print(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
