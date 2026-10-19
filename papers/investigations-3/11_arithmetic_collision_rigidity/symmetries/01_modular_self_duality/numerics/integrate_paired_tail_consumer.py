#!/usr/bin/env python3
"""S01-T1: paired omitted-mode payment in the unchanged physical consumer.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol; actual effort ultra. Internal verification.
Requires python-flint 0.9.0. No coverage or timing superiority claim.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time

import flint
from flint import arb, ctx

INV = Path('papers/investigations-3/11_arithmetic_collision_rigidity')
S01 = INV/'symmetries/01_modular_self_duality'


def check(c, message):
    if not c:
        raise ArithmeticError(message)


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def s(v):
    return v.str(45, more=True)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def invariant_fingerprint(ev, base):
    """Everything consumed here except the allowed mode-tail replacement."""
    data = {'values':[base.dyadic(v) for v in ev.values],
            'radii':[base.dyadic(v) for v in ev.radii],
            'source':[base.dyadic(v) for v in ev.uniform_tails[1]],
            'majorant':base.dyadic(ev.majorant),
            'full_H_moment':base.dyadic(ev.full_H_moment),
            'high_order_tails':[[base.dyadic(v) for v in vv] for vv in ev.high_order_tails],
            'frozen':[str(v) for v in (ev.tlo,ev.thi,ev.tc,ev.xlo,ev.xhi,ev.xc,
                                       ev.L,ev.K,ev.maxmid,ev.maxrem)]}
    return hashlib.sha256(json.dumps(data,sort_keys=True).encode()).hexdigest()


def install_paired_tail(ev, paired):
    """Reusable, B-only real consumer interface; changes uniform mode tails only.

    Returns (receipt, previous_mode_vector). Caller may restore the original
    vector as ``ev.uniform_tails = (previous, ev.uniform_tails[1])``.
    High-order moment tails are deliberately not changed.
    """
    check((ev.tlo,ev.thi,ev.tc,ev.xlo,ev.xhi,ev.xc) ==
          (F(1,100),F(1,5),F(21,200),F(999),F(1001),F(1000)),
          'paired consumer requires the fixed B rectangle and midpoint')
    check(ev.m==12 and ev.U==2 and ev.L==24 and ev.K==12 and
          ev.maxmid==50 and ev.maxrem==52, 'paired consumer frozen parameters mismatch')
    check(ev.d.overlaps(arb.pi()/8-4*arb(1000).log()/1000),
          'paired consumer contour mismatch')
    # The stronger equality check catches an altered contour within a broad ball.
    expected=arb.pi()/8-4*arb(1000).log()/1000
    check(ev.d.str(0,more=True)==expected.str(0,more=True),
          'paired consumer requires the original contour enclosure')
    check(ctx.prec==ev.bits and ev.bits>=128, 'paired consumer precision mismatch')
    for value,reference,name in [(ev.pi,arb.pi(),'pi'),
            (ev.c,(4*expected).cos(),'cos4d'),
            (ev.sin4d,(4*expected).sin(),'sin4d'),
            (ev.norm,arb(1000)**(arb(9)/4),'fixed normalization')]:
        check(value.str(0,more=True)==reference.str(0,more=True),
              'paired consumer '+name+' mismatch')
    check(len(ev.lams)==11 and all(value.str(0,more=True)==(arb.pi()*n*n).str(0,more=True)
          for n,value in enumerate(ev.lams,1)), 'paired consumer retained modes mismatch')
    receipt, improved = paired.tail_bounds(0,ev.bits)
    previous = ev.uniform_tails[0]
    reference,_ = ev.tails(ev.xlo,ev.xhi)
    check(len(previous)==3 and all(a==b for a,b in zip(previous,reference)),
          'baseline mode vector changed before installation')
    check(all(0<new<old for new,old in zip(improved,previous)),
          'paired mode vector must strictly improve all three physical derivatives')
    ev.uniform_tails=(improved,ev.uniform_tails[1])
    return receipt,previous


def geometry(report):
    return [(row['t'],row['x'],row['depth'],row['status'])
            for row in report['initial_attempt_cells']+report['repair_choices']+report['repair_cells']]


def run(repo,bits,base,paired):
    ctx.prec=bits
    started=time.monotonic()
    ev=base.bounded(lambda:base.WholeCellEvaluator(bits),60)
    fingerprint=invariant_fingerprint(ev,base)
    baseline=base.run_signed_consumer(ev)
    check(baseline['status']=='pass','baseline signed consumer failed')
    _,old_budgets=ev.enclose(ev.tlo,ev.thi,ev.xlo,ev.xhi)
    old_tail=list(ev.uniform_tails[0])
    receipt,previous=install_paired_tail(ev,paired)
    improved=base.run_signed_consumer(ev)
    check(improved['status']=='pass','paired signed consumer failed')
    _,new_budgets=ev.enclose(ev.tlo,ev.thi,ev.xlo,ev.xhi)
    check(invariant_fingerprint(ev,base)==fingerprint,'unallowed evaluator data changed')
    check(geometry(baseline)==geometry(improved),'adaptive comparison geometry changed; review required')
    rows=[]
    for j,(old,new) in enumerate(zip(old_budgets,new_budgets)):
        check(all(old[k]==new[k] for k in ['quadrature','taylor','source']),
              'a common error component changed')
        oldtotal=sum((old[k] for k in ['quadrature','taylor','source','mode']),arb(0))
        newtotal=sum((new[k] for k in ['quadrature','taylor','source','mode']),arb(0))
        check(newtotal<oldtotal,'complete added-error decrease lost')
        rows.append({'j':j,'old_mode':s(old_tail[j]),'paired_mode':s(ev.uniform_tails[0][j]),
                     'quadrature_with_internal_rounding':s(old['quadrature']),
                     'whole_box_Taylor':s(old['taylor']),'retained_source_tail':s(old['source']),
                     'old_complete_added_error':s(oldtotal),'paired_complete_added_error':s(newtotal),
                     'paired_over_old_complete':s(newtotal/oldtotal)})
    cells=[]
    same=0
    for a,b in zip(baseline['repair_cells'],improved['repair_cells']):
        check(a['t']==b['t'] and a['x']==b['x'],'matched cell mismatch')
        identical=a['excess_norm2']==b['excess_norm2']
        same+=int(identical)
        cells.append({'t':a['t'],'x':a['x'],'depth':a['depth'],
                      'old_signed_excess':a['excess_norm2'],
                      'paired_signed_excess':b['excess_norm2'],
                      'same_signed_excess_interval':identical,
                      'same_jet_images':a['jet']==b['jet']})
    # Export compact, exact comparison results; do not round a hypothetical gain up.
    old_min=arb(baseline['summary']['minimum_signed_excess_norm2'])
    new_min=arb(improved['summary']['minimum_signed_excess_norm2'])
    result={'bits':bits,'shared_setup_seconds':ev.setup_seconds,
            'shared_setup_callbacks':ev.callbacks,'unchanged_evaluator_data_sha256':fingerprint,
            'baseline_summary':baseline['summary'],'paired_summary':improved['summary'],
            'baseline_initial_attempt':baseline['initial_attempt'],
            'paired_initial_attempt':improved['initial_attempt'],
            'same_adaptive_geometry':True,'same_signed_interval_count':same,
            'accepted_cells':cells,'complete_error_ledger':rows,'tail_receipt':receipt,
            'signed_margin_strict_improvement_resolved':bool(new_min>old_min),
            'same_reported_minimum':baseline['summary']['minimum_signed_excess_norm2']==
                                    improved['summary']['minimum_signed_excess_norm2'],
            'baseline_consumer_seconds':baseline['consumer_seconds'],
            'paired_consumer_seconds':improved['consumer_seconds'],
            'paired_tail_setup_included_in_run_seconds':True,
            'run_seconds_including_shared_setup':time.monotonic()-started}
    ev.uniform_tails=(previous,ev.uniform_tails[1])
    check(all(a==b for a,b in zip(ev.uniform_tails[0],old_tail)), 'baseline restoration failed')
    # A changed box or contour cannot silently consume the B-only bound.
    ev.xhi=F(1002)
    try:
        install_paired_tail(ev,paired)
    except ArithmeticError:
        result['changed_domain_rejected']=True
    else:
        raise ArithmeticError('changed domain accepted')
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bits',type=int,nargs='+',default=[192,256])
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    args=p.parse_args()
    repo=args.repo.resolve()
    base_path=repo/INV/'numerics/high_height_consumer/high_height_consumer.py'
    paired_path=repo/S01/'numerics/check_paired_modular_tail.py'
    base=load(base_path,'s01_complete_consumer_base')
    paired=load(paired_path,'s01_complete_consumer_tail')
    replays=[]
    for bits in args.bits:
        row=run(repo,bits,base,paired)
        replays.append(row)
        print(json.dumps({'bits':bits,'accepted_cells':len(row['accepted_cells']),
              'same_signed_intervals':row['same_signed_interval_count'],
              'same_minimum':row['same_reported_minimum'],
              'old_minimum':row['baseline_summary']['minimum_signed_excess_norm2'],
              'paired_minimum':row['paired_summary']['minimum_signed_excess_norm2']}),flush=True)
    ctx.prec=max(args.bits)
    # The precision replays bound the same declared formulas. Compare the
    # interval ratios; different quadrature enclosures may legitimately differ.
    if len(replays)>1:
        for row in replays[1:]:
            for j in range(3):
                for key in ['old_mode','paired_mode','whole_box_Taylor','retained_source_tail']:
                    check(arb(row['complete_error_ledger'][j][key]).overlaps(
                          arb(replays[0]['complete_error_ledger'][j][key])),
                          'precision replay of common analytic term disjoint')
    fixtures={'non_even_vertical_boundary':paired.vertical_fixture(),
              'inadmissible_tail_parameter_rejections':paired.negative_cases()}
    pins=[base_path,paired_path,repo/S01/'notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md',
          repo/INV/'symmetries/notes/01_S01_COMPLETE_CONSUMER_COMPARISON_CONTRACT_20261019.md',
          repo/INV/'numerics/high_height_consumer/REAL_COMPARISON.json',
          repo/INV/'numerics/high_height_consumer/SIGNED_CONSUMER.json']
    pins+=list((repo/INV/'manuscript/positive_arithmetic_packets/sections').glob('0[178]*.tex'))
    report={'schema':'s01-complete-consumer-integration-v1','date':'2026-10-19',
            'timezone':'America/New_York','prepared_for':'Edward Baker',
            'actual_model':args.execution_model,'actual_effort':args.execution_effort,
            'llm_assistance':'substantial; internal same-model research and delegated review',
            'python':platform.python_version(),'python_flint':flint.__version__,
            'source_sha256':{str(v.relative_to(repo)):digest(v) for v in pins},
            'script_sha256':digest(__file__),
            'primary_metric':'minimum (L0-E/100)/Gc^2 in unchanged signed consumer',
            'domain':{'t':['1/100','1/5'],'x':[999,1001]},
            'replays':replays,'mechanism_controls':fixtures,'status':'pass',
            'new_coverage':False,'new_Newman_bound':False,'performance_claim':False,
            'strongest_real_source_complete_error_reference':'<2.165e-12 Gc at 768 bits; different polynomial; not beaten',
            'decision':'Retain reusable paired-tail integration. Stop tuning this omitted tail on B if the paid physical margin is unchanged.'}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'pass','output':str(args.output),'bytes':args.output.stat().st_size}))

if __name__=='__main__':
    main()
