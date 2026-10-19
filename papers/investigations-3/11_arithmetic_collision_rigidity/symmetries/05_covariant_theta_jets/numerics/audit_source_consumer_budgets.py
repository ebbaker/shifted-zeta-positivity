#!/usr/bin/env python3
"""S05-T1: quantify existing S01/S06 budgets before choosing a handoff.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual authoring model gpt-6.1-sol, reasoning effort ultra.
No physical consumer, new exclusion, or full coefficient setup is run.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import flint
from flint import arb, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
S01=INV/'symmetries/01_modular_self_duality'
S06=INV/'symmetries/06_hodge_and_transverse_geometry'
PINS={
    str(S06/'numerics/check_signed_transverse.py'):'2eb377fa03c916c50a55e3c3fa4c55f360ffc25184ce180151beff234dcd0a0f',
    str(S01/'numerics/S01_COMPLETE_CONSUMER_20261019.json'):'4e5b8336843da26294d721c2338e8b2bac5f8af67260aea7843205d1fb97806a',
    str(S01/'numerics/integrate_paired_tail_consumer.py'):'f6b89d07cbf1f6fb7fbdbe0a491545a86c5ecabf9320bccf6285db53c7c1158f',
}

def check(c,m):
    if not c: raise ArithmeticError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def out(x):return x.str(40,more=True)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bits',type=int,choices=[192,256],default=192)
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    a=p.parse_args();repo=a.repo.resolve();ctx.prec=a.bits
    check(a.execution_model.strip() and a.execution_effort.strip(),'actual metadata required')
    for rel,h in PINS.items():check(sha(repo/rel)==h,'stale budget source: '+rel)
    path=repo/S01/'numerics/S01_COMPLETE_CONSUMER_20261019.json'
    old=json.loads(path.read_text())
    check(old['status']=='pass','S01 record did not pass')
    check(old['script_sha256']==PINS[str(S01/'numerics/integrate_paired_tail_consumer.py')],
          'S01 budget producer mismatch')
    for rel,h in old['source_sha256'].items():check(sha(repo/rel)==h,'stale S01 budget input: '+rel)
    oldrow=next(r for r in old['replays'] if r['bits']==a.bits)
    s01=[]
    for r in oldrow['complete_error_ledger']:
        total=arb(r['paired_complete_added_error'])
        source=arb(r['retained_source_tail'])
        fraction=source/total
        check(fraction<arb('4e-424'),'source-cutoff fraction ceiling')
        s01.append({'j':r['j'],'complete_error':out(total),
             'quadrature_fraction':out(arb(r['quadrature_with_internal_rounding'])/total),
             'Taylor_fraction':out(arb(r['whole_box_Taylor'])/total),
             'unchanged_nonquadrature_floor':out(arb(r['whole_box_Taylor'])+arb(r['paired_mode'])+source),
             'retained_source_tail':out(source),'source_tail_fraction':out(fraction),
             'existing_real_fixed_point_range_budget':'0; source-domain mismatch'})
    src=repo/S06/'numerics/check_signed_transverse.py'
    spec=importlib.util.spec_from_file_location('s05_t1_s06_endpoint',src)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    fresh=mod.endpoint_and_moments(a.bits)
    pieces={'third_endpoint':fresh['f3'].abs_upper()/999**2,
            'fifth_endpoint':fresh['f5'].abs_upper()/999**4,
            'sixth_derivative_L1':fresh['norms'][6]/999**4}
    check(abs(sum(pieces.values(),arb(0))-fresh['error6'])<arb('1e-50'),
          'S06 budget recombination')
    tails=fresh['tail_norms'][6]/fresh['norms'][6]
    check(tails<arb('7.2e-98'),'S06 negligible mode-tail fraction')
    radii=[v.rad().upper() for v in fresh['ends']]
    T=arb(1)/5
    endpoint_rounding=(radii[1]+(radii[3]+6*T*radii[1])/999**2
                       +(radii[5]+20*T*radii[3]+60*T*T*radii[1])/999**4)
    check(endpoint_rounding/fresh['error6']<arb('1e-50'),
          'S06 endpoint-rounding fraction negligible')
    check(fresh['ends'][1]<0,'raw g has a nonzero odd endpoint')
    result={'schema':'s05-t1-source-consumer-budget-audit-v1',
       'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
       'actual_model':a.execution_model,'actual_effort':a.execution_effort,
       'llm_assistance':'substantial; internal same-model consumer-fit audit',
       'precision_bits':a.bits,'python_flint':flint.__version__,'script_sha256':sha(__file__),
       'source_sha256':PINS,'S01_historical_producer_and_all_source_pins_verified':True,
       'S01':{'historical_budget_rows':s01,
              'setup_callbacks_historical':oldrow['shared_setup_callbacks'],
              'fresh_51_coefficient_setup':False,
              'real_parity_Taylor_fit':False,
              'possible_shifted_polynomial_factor_fit':'separate bounded j=0 probe'},
       'S06':{'fresh_endpoint_and_moment_call':True,
              'raw_source':'g=pi sum n^2 phi_n, not even',
              'raw_g_prime_at_zero':out(fresh['ends'][1]),
              'endpoint_radii':[out(v) for v in radii],
              'scaled_error6':out(fresh['error6']),
              'scaled_contributions':{k:out(v) for k,v in pieces.items()},
              'contribution_fractions':{k:out(v/fresh['error6']) for k,v in pieces.items()},
              'endpoint_rounding_budget_upper':out(endpoint_rounding),
              'endpoint_rounding_over_error6':out(endpoint_rounding/fresh['error6']),
              'sixth_L1_mode_tail_fraction':out(tails),
              'real_fixed_point_range_budget':'0; point endpoints and analytic all-u moments',
              'current_completed_C_consumer':'physical H/Hx/Hxx interface, no real local-source ranges',
              'real_parity_Taylor_fit':False},
       'interpretation':'Scoped consumer selection, not a new physical error or impossibility theorem.',
       'controls':{'raw_g_odd_endpoint_nonzero':True,
              'source_and_physical_derivative_coordinates_distinct':True},
       'status':'pass'}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(a.output),'bits':a.bits,'status':'pass',
                      'S06_sixth_L1_fraction':out(pieces['sixth_derivative_L1']/fresh['error6'])}))

if __name__=='__main__':main()
