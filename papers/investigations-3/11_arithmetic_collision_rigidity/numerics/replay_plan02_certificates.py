#!/usr/bin/env python3
"""Adversarial replay of the finite overview 02 outcome, not a global bound.

18 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort max. Same-model internal review;
the replay uses the real-source contour at 256 bits for saved signed cells.
"""
from fractions import Fraction as F
import argparse
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import time

from flint import arb,acb,ctx
import flint
from certify_shifted_theta_jet import Evaluator,A,rec,check,coordinate_separator,laguerre_excess,square
from run_plan02_pilot import load_receipt,digest


def cover(cells,left,right):
    check(bool(cells),'empty cover')
    cursor=left
    for cell in cells:
        a,b=map(F,cell['x'])
        check(a==cursor and a<b and b<=right,'cover gap, overlap, reversed interval or excess')
        cursor=b
    check(cursor==right,'cover misses equality endpoint')


def bound_input(path,sha):
    check(digest(path)==sha,'input hash mismatch')
    return json.loads(path.read_text())


def expected_failure(label,func):
    try:
        func()
    except (ArithmeticError,ValueError,FileNotFoundError,KeyError,TypeError):
        return label
    raise ArithmeticError('failure injection was accepted: '+label)


def root_diagnostic(evaluator,component):
    t=F(1,10)
    previous=None;left=right=None
    for k in range(41):
        x=F(25)+F(k,2)
        value=evaluator.enclose(t,t,x,x)[0][component]
        if previous and ((previous[1]>0 and value<0) or (previous[1]<0 and value>0)):
            left,right=previous[0],x
            break
        previous=(x,value)
    check(left is not None,'no diagnostic sign-change bracket located')
    for _ in range(27):
        middle=(left+right)/2
        vl=evaluator.enclose(t,t,left,left)[0][component]
        vm=evaluator.enclose(t,t,middle,middle)[0][component]
        check((vl>0 or vl<0) and (vm>0 or vm<0),'diagnostic root interval too fine')
        if (vl>0 and vm>0) or (vl<0 and vm<0):left=middle
        else:right=middle
    values,budgets=evaluator.enclose(t,t,left,right)
    opposite=1 if component==0 else 0
    check(values[opposite]>0 or values[opposite]<0,'diagnostic first jet lower bound absent')
    return {'component_root':['H','Hx'][component],'t':'1/10','x_bracket':[str(left),str(right)],
            'physical_jet':[rec(v) for v in values],
            'other_component_lower':rec(values[opposite].abs_lower()),
            'interpretation':'ordinary root certified by derivative sign' if component==0 else 'stationary point with directly certified nonzero value; not assumed'}


def heat_diagnostic(evaluator):
    pi=evaluator.pi;d=evaluator.d
    def derivative(u,analytic):
        v=u+acb(0,d) if evaluator.method=='shifted' else u
        q=(4*v).exp()
        source=sum(((2*(pi*n*n)**2*q*q-3*pi*n*n*q)*(-pi*n*n*q).exp()
                    for n in range(1,5)),acb(0))
        base=(A(evaluator.tc)*v*v+v).exp()*source
        return base*v*v*((acb(0,A(evaluator.xc))*v).exp() if evaluator.method=='shifted' else (A(evaluator.xc)*u).cos())
    value=acb.integral(derivative,0,1,abs_tol=arb('1e-35'),rel_tol=arb('1e-28'),eval_limit=200000,depth_limit=30)
    check(value.is_finite(),'independent time-derivative integral failed')
    hxx=evaluator.midpoints[2]+arb(0,evaluator.quad_radii[2])
    residual=value.real+hxx
    check(residual.contains(0),'finite integral heat-equation diagnostic failed')
    return {'method':evaluator.method,'independently_integrated_time_derivative':rec(value.real),'H_t_plus_Hxx':rec(residual)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True);p.add_argument('--records',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--budget-output',type=Path,required=True)
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    args=p.parse_args();start=time.monotonic();ctx.prec=256
    records=args.records
    validation_path=records/'SHIFTED_EVALUATOR_VALIDATION_20261018.json'
    pilot_path=records/'SHIFTED_PILOT_COMPARISON_20261018.json'
    signed_path=records/'COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.json'
    validation=json.loads(validation_path.read_text());pilot=json.loads(pilot_path.read_text());signed=json.loads(signed_path.read_text())
    source=Path(__file__).with_name('certify_shifted_theta_jet.py')
    driver=Path(__file__).with_name('run_plan02_pilot.py')
    check(validation['script_sha256']==digest(source),'validation evaluator code hash mismatch')
    check(pilot['evaluator_sha256']==digest(source) and signed['evaluator_sha256']==digest(source),'consumer evaluator hash mismatch')
    check(pilot['script_sha256']==digest(driver) and signed['script_sha256']==digest(driver),'consumer driver hash mismatch')
    check(pilot['validation_sha256']==digest(validation_path),'pilot validation input hash mismatch')
    check(signed['evaluator_manifest']['exact_domain']['t']==['1/100','1/5']
          and signed['evaluator_manifest']['exact_domain']['x']==['25','45'],'signed certificate domain mismatch')
    check(signed['certificate']['signed_constant']=='1/100','signed coefficient mismatch')
    cover(signed['certificate']['cells'],F(25),F(45))
    for name in ('real','shifted'):cover(validation['pilot'][name]['cells'],F(25),F(45))
    real=Evaluator('real',bits=256)
    minimum=arb('1e100');weakest=None
    for cell in signed['certificate']['cells']:
        left,right=map(F,cell['x'])
        jets,_=real.enclose(F(1,100),F(1,5),left,right)
        excess=laguerre_excess(jets,F(1,100))
        check(excess>arb('4e-16'),'direct-source signed replay margin failed')
        if excess.lower()<minimum:
            minimum=excess.lower();weakest=cell['x']
    for cell in validation['pilot']['shifted']['cells']:
        left,right=map(F,cell['x'])
        check(coordinate_separator(real.enclose(F(1,100),F(1,5),left,right)[0]) is not None,'first-jet cell replay failed')
    shifted=Evaluator('shifted',bits=256)
    intersections=0
    for test in validation['matched_tests']:
        domain=tuple(map(F,test['exact_cell']))
        a=real.enclose(*domain)[0];b=shifted.enclose(*domain)[0]
        check(all(u.overlaps(v) for u,v in zip(a,b)),'256-bit contour crosscheck failed')
        intersections+=1
    roots=[root_diagnostic(real,component) for component in (0,1)]
    heat=[heat_diagnostic(e) for e in (real,shifted)]
    injections=[]
    check(square(arb(0,1)).contains(0) and square(arb(0,1)).contains(1),'outward zero-centred square regression')
    check(coordinate_separator([arb(0),arb(0),arb(2)]) is None,'equality passed a strict coordinate gate')
    check(not laguerre_excess([arb(0),arb(0),arb(2)],F(1,100))>0,'equality passed a strict signed gate')
    injections.extend(['zero-centred square explicitly encloses 0 and 1','strict equality rejected by both margin gates'])
    injections.append(expected_failure('nonfinite jet',lambda:coordinate_separator([arb('nan'),arb(1)])))
    injections.append(expected_failure('malformed jet dimension',lambda:laguerre_excess([arb(1)],F(1,100))))
    injections.append(expected_failure('cell outside frozen rectangle',lambda:real.enclose(F(1,100),F(1,5),F(24),F(25))))
    injections.append(expected_failure('unproved imaginary band',lambda:real.enclose(F(1,100),F(1,5),F(25),F(26),F(2),F(2))))
    injections.append(expected_failure('negative time domain',lambda:Evaluator('real',tlo=F(-1,100))))
    injections.append(expected_failure('unsupported mode count',lambda:Evaluator('shifted',modes=3)))
    changed=copy.deepcopy(signed['certificate']['cells']);changed[0]['x'][0]='25001/1000'
    injections.append(expected_failure('coverage gap',lambda:cover(changed,F(25),F(45))))
    changed=copy.deepcopy(signed['certificate']['cells']);changed[-1]['x'][1]='44999/1000'
    injections.append(expected_failure('missing closed endpoint',lambda:cover(changed,F(25),F(45))))
    saved_d=shifted.d
    shifted.d=shifted.pi/4
    injections.append(expected_failure('invalid source contour',shifted.admissibility))
    shifted.d=saved_d
    with tempfile.TemporaryDirectory(prefix='plan02-negative-tests-') as temp:
        temp=Path(temp)
        injections.append(expected_failure('missing bound input',lambda:bound_input(temp/'absent.json','0'*64)))
        bad=temp/'malformed.json';bad.write_text('{')
        injections.append(expected_failure('malformed JSON input',lambda:bound_input(bad,digest(bad))))
        bad=temp/'changed.json';bad.write_text(json.dumps({'all_checks_passed':True,'forged_margin':'1e9'}))
        injections.append(expected_failure('forged PASS with changed bytes',lambda:bound_input(bad,digest(signed_path))))
        # Freshly generated control outputs are byte-bound before use, and
        # their recorded code identity is checked against the executed source.
        source_control=args.repo/'papers/investigations-2/active/19_euler_factor_controls/numerics/certify_euler_factor_witness.py'
        payload=json.loads((records/'EULER_FACTOR_REPLAY.json').read_text())
        payload['raw_laguerre_L0']['display']='[1 +/- 0.01]'
        altered=temp/'EULER_FACTOR_REPLAY.json';altered.write_text(json.dumps(payload))
        expected=pilot['control_screen']['receipt_identities']['euler']['sha256']
        injections.append(expected_failure('changed control witness bytes',lambda:load_receipt(temp,altered.name,source_control,expected)))
    moment_error_summary={}
    for name in ('real','shifted'):
        margin=arb(validation['pilot'][name]['minimum_margin_lower'])
        error=arb(validation['pilot'][name]['worst_added_coordinate_error'])
        envelope=((arb(7)/4)*arb(45).log()-arb.pi()*45/8).exp()
        moment_error_summary[name]={'worst_coordinate_error':rec(error),'positive_G0_at_right_endpoint':rec(envelope),
                                     'error_over_G0_upper':rec((error/envelope).upper()),
                                     'jet_error_over_certified_jet_lower_upper':rec((arb(2).sqrt()*error/margin).upper()),
                                     'dominant_error':'finite-rectangle Taylor propagation; not omitted arithmetic modes'}
    outer=args.repo/'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex'
    budget={'date':'2026-10-18','prepared_for':'Edward Baker','model':args.execution_model,'reasoning_effort':args.execution_effort,
            'status':'Global route unclosed; expansion stopped at the stated gate','selected_feasible_route':None,
            'normalization':'H_0(z)=xi((1+iz)/2)/8','comparison_baseline':'published Lambda<=0.2; no current-best assertion',
            'slab_starting_contract':{'tau':'1/100 (inherited pilot endpoint, not an optimized target)','finite_target':{'t':['1/100','1/5'],'x':['0','exp(6400)']},
                'certified_this_round':[{'t':['1/100','1/5'],'x':['25','45'],'certificate':'SHIFTED_EVALUATOR_VALIDATION_20261018.json'},
                                       {'t':['1/100','1/5'],'x':['45','65'],'certificate':'SHIFTED_PILOT_COMPARISON_20261018.json'}],
                'outer':{'threshold':'exp(6400)','time':['1/100','1/2'],'status':'inherited proved corollary cor:eventual; source and domain inspected, not rederived or numerically recertified here','source_relative':str(outer.relative_to(args.repo)),'source_sha256':digest(outer)},
                'unclosed':['[0,25) and (65,exp(6400)) finite bridge in this round','no feasible measured cost for the complete bridge','all finite/outer seam and endpoint obligations of an improved global claim remain unclosed'],
                'conclusion':'Lambda<=1/100 is NOT established'},
            'canopy_route':{'parameters':None,'required':['exact initial zeta verification','final exterior nonvanishing','moving intermediate-time barrier with all theorem restrictions'],
                            'status':'no completed parameter/budget package selected','primary_theorem':'https://arxiv.org/html/1904.12438v2#S1.Thmtheorem2'},
            'near_boundary_asymptotic':{'effective_onset':None,'evaluated_constants':None,'retained_quadrature_cost':None,'status':'not consumed globally'},
            'decision':'retain the finite evaluator, measured error gain and local signed estimate; no larger scan or new Newman-bound announcement'}
    args.budget_output.write_text(json.dumps(budget,indent=2)+'\n')
    final={'date':'2026-10-18','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance; same-model internal adversarial replay, not specialist review.',
           'model':args.execution_model,'reasoning_effort':args.execution_effort,'python_flint':flint.__version__,'replay_bits':256,
           'verifier_sha256':digest(Path(__file__)),'evaluator_sha256':digest(source),'pilot_driver_sha256':digest(driver),
           'input_sha256':{path.name:digest(path) for path in (validation_path,pilot_path,signed_path)},
           'signed_cells_recalculated':len(signed['certificate']['cells']),'direct_source_signed_excess_minimum_lower':rec(minimum),
           'weakest_replayed_cell':weakest,'first_jet_cells_recalculated':len(validation['pilot']['shifted']['cells']),
           'matched_256_bit_point_and_cell_tests':intersections,'root_diagnostics':roots,'heat_diagnostics':heat,
           'failure_injection_results':injections,'error_scale_summary':moment_error_summary,
           'claims':[{'claim':'complete first jet is nonzero on D0','evidence':'128 strict coordinate strips; real-source 256-bit replay'},
                     {'claim':'L0>E/100 on D0','evidence':'all signed cells re-evaluated on real source at 256 bits; raw excess >4e-16'},
                     {'claim':'shifted propagation error is smaller in this fixed pilot','evidence':'complete component budgets; no speed superiority inferred'},
                     {'claim':'applicable control event boxes fail the strict interface','evidence':'five source-specific surrounding event boxes; Euler witness separately classified'}],
           'global_bound_established':False,'performance_gate_passed':pilot['performance_gate_passed'],
           'closure':'auxiliary finite outcome only; global consumer unclosed','all_replay_checks_passed':True,
           'limitations':['same model, shared source polynomial and Arb/Acb library','bounded tests cover previously known territory','no independently derived global arithmetic sign mechanism','no effective near-boundary asymptotic onset or global finite bridge'],
           'total_seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(final,indent=2)+'\n')
    print(json.dumps({'passed':True,'signed_cells':len(signed['certificate']['cells']),'direct_signed_excess_minimum':rec(minimum),
                      'failure_tests':len(injections),'roots':roots,'global_bound':False,'seconds':time.monotonic()-start},indent=2))


if __name__=='__main__':main()
