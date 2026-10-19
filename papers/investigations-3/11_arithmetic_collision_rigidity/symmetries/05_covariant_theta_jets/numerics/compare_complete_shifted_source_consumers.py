#!/usr/bin/env python3
"""S05-T2 matched complete shifted-source acquisition comparison on fixed B.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual execution model and effort are required CLI metadata. Internal work.
No repository sources are changed. Requires python-flint 0.9.0.
"""
from __future__ import annotations
import argparse
from collections import Counter
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys
import time
import flint
from flint import arb, acb, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
S05=INV/'symmetries/05_covariant_theta_jets'
S01=INV/'symmetries/01_modular_self_duality'
METHODS=('expanded','polynomial_factored','exponential_grouped')
HYBRID='minimum_radius_hybrid'
OLD_HYBRID='old_alternatives_hybrid'


def check(condition,message):
    if not condition:
        raise ArithmeticError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_hash(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def s(value):
    return value.str(45,more=True)


def dyadic(value):
    check(value.is_finite() and value.is_exact(),'exact finite dyadic required')
    mantissa,exponent=value.man_exp()
    return {'mantissa':str(mantissa),'exponent':int(exponent)}


def undyadic(data):
    value=arb((int(data['mantissa']),int(data['exponent'])))
    check(value.is_finite() and value.is_exact(),'invalid exact dyadic')
    return value


def ball_record(value):
    return {'enclosure':s(value),'midpoint_dyadic':dyadic(value.mid()),
            'radius_upper_dyadic':dyadic(value.rad().upper())}


def restore_ball(row):
    return undyadic(row['midpoint_dyadic'])+arb(0,undyadic(row['radius_upper_dyadic']))


def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def validate_metadata(bits,model,effort):
    check(bits in (192,256),'only frozen 192/256-bit executions are allowed')
    check(isinstance(model,str) and bool(model.strip()),'actual model metadata required')
    check(isinstance(effort,str) and bool(effort.strip()),'actual effort metadata required')


def verify_pins(repo,pins):
    check(isinstance(pins,dict) and bool(pins),'nonempty source pin mapping required')
    receipts={}
    for relative,expected in pins.items():
        path=(repo/relative).resolve()
        check(path.is_relative_to(repo),'source pin must stay inside repository')
        check(path.is_file(),'source pin input missing: '+relative)
        receipts[relative]=digest(path)==expected
    check(all(receipts.values()),'stale source pin rejected')
    return receipts


def validate_coefficients(ev,rows):
    check(len(rows)==len(ev.values)==len(ev.radii)==51,'all 51 ordered coefficients required')
    for j,row in enumerate(rows):
        check(row['j']==j,'coefficient order changed')
        check(ev.values[j].is_finite() and ev.values[j].is_exact(),'coefficient midpoint must be exact and finite')
        check(ev.radii[j].is_finite() and ev.radii[j].is_exact() and ev.radii[j]>=0,
              'quadrature radius must be exact finite nonnegative')
        check(row['midpoint_dyadic']==dyadic(ev.values[j])
              and row['quadrature_radius_upper_dyadic']==dyadic(ev.radii[j]),
              'coefficient tuple differs from its receipt')


def validate_frozen(ev):
    check((ev.tlo,ev.thi,ev.tc,ev.xlo,ev.xhi,ev.xc)==
          (F(1,100),F(1,5),F(21,200),F(999),F(1001),F(1000)),'fixed B/midpoint changed')
    check(ev.bits==ctx.prec and ev.bits in (192,256),'fixed precision changed')
    check(ev.U==2 and ev.m==12 and ev.L==24 and ev.K==12 and ev.J==2
          and ev.maxmid==50 and ev.maxrem==52,'fixed source cutoff or degrees changed')
    d=arb.pi()/8-4*arb(1000).log()/1000
    for value,expected,label in ((ev.d,d,'contour'),(ev.pi,arb.pi(),'pi'),
           (ev.c,(4*d).cos(),'cos4d'),(ev.sin4d,(4*d).sin(),'sin4d'),
           (ev.norm,arb(1000)**(arb(9)/4),'normalization')):
        check(value.str(0,more=True)==expected.str(0,more=True),'fixed '+label+' changed')
    check(len(ev.lams)==11 and all(value.str(0,more=True)==(arb.pi()*n*n).str(0,more=True)
          for n,value in enumerate(ev.lams,1)),'fixed source modes changed')


def common_data(ev):
    validate_frozen(ev)
    return {'majorant':dyadic(ev.majorant),'full_H_moment':dyadic(ev.full_H_moment),
         'whole_box_taylor':dyadic(ev.whole_box_taylor),
         'uniform_tails':[[dyadic(v) for v in values] for values in ev.uniform_tails],
         'high_order_tails':[[dyadic(v) for v in values] for values in ev.high_order_tails]}


def make_candidate_class(base):
    class CandidateEvaluator(base.WholeCellEvaluator):
        def __init__(self,bits,method):
            check(method in METHODS[1:],'unknown candidate acquisition formula')
            # This setup copies the actual baseline constants. Only its finite
            # coefficient acquisition integrand differs. Inherited moment_bound,
            # tails, tick, enclose and acceptance functions remain unchanged.
            A=base.A
            ctx.prec=bits
            self.bits=bits;self.tlo=F(1,100);self.thi=F(1,5);self.tc=F(21,200)
            self.xlo=F(999);self.xhi=F(1001);self.xc=F(1000);self.U=arb(2);self.m=12
            self.L=24;self.K=12;self.J=2;self.maxmid=50;self.maxrem=52
            self.pi=arb.pi();self.d=self.pi/8-4*A(self.xc).log()/A(self.xc)
            self.c=(4*self.d).cos();self.sin4d=(4*self.d).sin()
            self.norm=A(self.xc)**(arb(9)/4);self.lams=[self.pi*n*n for n in range(1,self.m)]
            self.callbacks=0;self.jet_callbacks=[];self.jet_seconds=[];self.values=[];self.radii=[]
            self.fact=[math.factorial(j) for j in range(self.maxrem+1)]
            self.coeff_cache={};self.calls=0;self.start=time.monotonic();self.diagnostic={}
            self._raw_jets=[]
            self.uniform_tails=self.tails(self.xlo,self.xhi)
            self.high_order_tails=self.tails(self.xlo,self.xhi,self.maxrem)
            self.full_H_moment=None
            self.majorant=self.moment_bound()
            R=arb(1);dt=A((self.thi-self.tlo)/2)
            self.full_H_moment=(self.majorant+max(self.high_order_tails[0])+max(self.high_order_tails[1])).upper()
            self.whole_box_taylor=(self.majorant*(R**(self.L+1)/self.fact[self.L+1]
                +R.exp()*dt**(self.K+1)/self.fact[self.K+1])).upper()
            check(self.whole_box_taylor<arb('1e-9'),'unchanged Taylor subbudget failed')
            for j in range(self.maxmid+1):
                begin=time.monotonic();before=self.callbacks
                def integrand(u,analytic):
                    self.tick();v=u+acb(0,self.d);q=(4*v).exp();total=acb(0)
                    for lam in self.lams:
                        w=lam*q
                        if method=='polynomial_factored':
                            total+=w*(2*w-3)*(-w).exp()
                        else:
                            total+=(v-w).exp()*w*(2*w-3)
                    if method=='polynomial_factored':
                        return self.norm*(A(self.tc)*v*v+v+acb(0,A(self.xc))*u).exp()*total*(acb(0,1)*v)**j
                    return self.norm*(A(self.tc)*v*v+acb(0,A(self.xc))*u).exp()*total*(acb(0,1)*v)**j
                val=acb.integral(integrand,0,self.U,abs_tol=arb('1e-13'),rel_tol=arb('1e-30'),
                                 eval_limit=200000,depth_limit=30)
                check(val.is_finite(),'nonfinite midpoint coefficient '+str(j))
                self._raw_jets.append(val)
                self.values.append(val.real.mid());self.radii.append(val.real.rad().upper())
                self.jet_callbacks.append(self.callbacks-before)
                self.jet_seconds.append(time.monotonic()-begin)
            self.setup_seconds=time.monotonic()-self.start
    return CandidateEvaluator


def frozen_cover(ledger,bits):
    row=next(item for item in ledger['replays'] if item['bits']==bits)
    cells=[{'t':item['t'],'x':item['x'],'depth':item['depth']} for item in row['accepted_cells']]
    check(len(cells)==40,'historical fixed cover must have 40 accepted cells')
    validate_cover(cells)
    return cells


def validate_cover(cells):
    times=[F(1,100)+k*F(19,400) for k in range(5)]
    check(len(cells)==40,'fixed physical cover changed')
    matched=0
    for ta,tb in zip(times,times[1:]):
        slab=sorted([row for row in cells if list(map(F,row['t']))==[ta,tb]],
                    key=lambda row:F(row['x'][0]))
        check(slab and F(slab[0]['x'][0])==999 and F(slab[-1]['x'][1])==1001,
              'fixed cover misses a closed slab endpoint')
        check(all(F(a['x'][1])==F(b['x'][0]) for a,b in zip(slab,slab[1:])),
              'fixed cover has a spatial gap/overlap')
        check(all(F(row['x'][0])<F(row['x'][1]) and row['depth']>=0 for row in slab),
              'invalid fixed physical cell')
        matched+=len(slab)
    check(matched==len(cells),'fixed cover has unmatched time coordinates')


def acquire(base,candidate,bits,method):
    begin=time.monotonic()
    if method=='expanded':
        # Observe the unchanged baseline's returned integration balls without
        # changing any integrand, argument, tolerance or returned value.
        original_acb=base.acb
        class ReturnTrace:
            def __init__(self):
                self.returned=[]
            def __call__(self,*args,**kwargs):
                return original_acb(*args,**kwargs)
            def integral(self,*args,**kwargs):
                value=original_acb.integral(*args,**kwargs)
                self.returned.append(value)
                return value
        trace=ReturnTrace()
        base.acb=trace
        try:
            ev=base.bounded(lambda:base.WholeCellEvaluator(bits),60)
        finally:
            base.acb=original_acb
        check(len(trace.returned)==52,'baseline integration trace must contain moment plus51coefficients')
        ev._raw_jets=trace.returned[1:]
    else:
        ev=base.bounded(lambda:candidate(bits,method),60)
    validate_frozen(ev)
    coefficients=[]
    for j,(midpoint,radius) in enumerate(zip(ev.values,ev.radii)):
        raw=ev._raw_jets[j]
        check(raw.real.mid()==midpoint and raw.real.rad().upper()==radius,
              'baseline/candidate returned-ball trace does not match coefficient')
        coefficients.append({'j':j,'midpoint':s(midpoint),'midpoint_dyadic':dyadic(midpoint),
             'quadrature_radius_upper':s(radius),'quadrature_radius_upper_dyadic':dyadic(radius),
             'imaginary_integral_ball':ball_record(raw.imag),
             'callbacks':ev.jet_callbacks[j],'seconds_diagnostic':ev.jet_seconds[j],
             'finite':True})
    validate_coefficients(ev,coefficients)
    return ev,{'method':method,'seconds_including_original_common_setup':ev.setup_seconds,
         'actual_producer':'original base.WholeCellEvaluator constructor' if method=='expanded' else
                 'this script CandidateEvaluator with inherited original moment/tails/propagation',
         'outer_seconds_diagnostic':time.monotonic()-begin,'setup_callbacks':ev.callbacks,
         'coefficient_callbacks':sum(ev.jet_callbacks),
         'original_common_setup_callbacks':ev.callbacks-sum(ev.jet_callbacks),
         'original_common_setup_seconds_diagnostic':ev.setup_seconds-sum(ev.jet_seconds),
         'coefficient_count':51,'coefficients':coefficients,
         'acquisition_deadline_seconds':60,'acquisition_callback_limit':2000000,
         'per_integral_abs_tol':'1e-13','per_integral_rel_tol':'1e-30',
         'per_integral_eval_limit':200000,'per_integral_depth_limit':30,
         'rounding':'Each exact dyadic midpoint and outward quadrature radius encloses the real coefficient. Radius includes Acb arithmetic and integration error; no separate radius is silently discarded.'}


def install_common_pair(ev,integration,paired):
    begin=time.monotonic()
    receipt,_=integration.install_paired_tail(ev,paired)
    return {'seconds':time.monotonic()-begin,'receipt':receipt}


def whole_box_ledger(ev,base):
    values,budgets=ev.enclose(ev.tlo,ev.thi,ev.xlo,ev.xhi)
    dx=base.box(ev.xlo,ev.xhi)-base.A(ev.xc)
    output=[]
    for j,(value,budget) in enumerate(zip(values,budgets)):
        image=base.poly(ev.coeff_cache[(ev.tlo,ev.thi,j)],dx)
        output.append({'j':j,'components':{key:s(v) for key,v in budget.items()},
               'components_dyadic':{key:dyadic(v) for key,v in budget.items()},
               'polynomial_image_with_outward_rounding':ball_record(image),
               'complete_physical_jet_enclosure':ball_record(value)})
    return output


def fixed_consumer(ev,base,cover):
    validate_cover(cover)
    begin=time.monotonic();ev.calls=0;ev.coeff_cache={}
    cells=[];excesses=[];maxerrors=[arb(0),arb(0),arb(0)]
    for geometry in cover:
        ta,tb=map(F,geometry['t']);xa,xb=map(F,geometry['x'])
        excess,row=base.signed_cell(ev,ta,tb,xa,xb,geometry['depth'])
        check(excess>0,'fixed physical signed consumer failed')
        excesses.append(excess)
        errors=[];quadrature=[];taylor=[]
        for j,budget in enumerate(row['budgets']):
            error=arb(budget['total']).upper();maxerrors[j]=max(maxerrors[j],error)
            errors.append(budget['total']);quadrature.append(budget['quadrature']);taylor.append(budget['taylor'])
        cells.append({'t':geometry['t'],'x':geometry['x'],'depth':geometry['depth'],
            'jet':row['jet'],'excess_norm2':row['excess_norm2'],
            'quadrature_with_internal_rounding':quadrature,'taylor':taylor,
            'complete_added_errors':errors})
    check(ev.calls==40,'fixed physical call count changed')
    return {'status':'pass','closed_coverage_verified':True,'calls':ev.calls,
         'minimum_signed_excess_norm2':s(min(value.lower() for value in excesses)),
         'maximum_complete_added_errors':[s(value) for value in maxerrors],
         'cells':cells,'seconds_diagnostic':time.monotonic()-begin}


def geometry_signature(report):
    return [(row['t'],row['x'],row['depth'],row['status']) for row in
        report['initial_attempt_cells']+report['repair_choices']+report['repair_cells']]


def evaluate(ev,base,cover):
    before=canonical_hash(common_data(ev))
    ledger=whole_box_ledger(ev,base)
    fixed=fixed_consumer(ev,base,cover)
    adaptive=base.run_signed_consumer(ev)
    check(adaptive['status']=='pass','unchanged adaptive physical consumer failed')
    check(canonical_hash(common_data(ev))==before,'physical consumer changed common data')
    return {'whole_box_complete_error_ledger':ledger,'fixed_40_cell_consumer':fixed,
         'adaptive_consumer':{'status':adaptive['status'],'summary':adaptive['summary'],
               'initial_attempt':adaptive['initial_attempt'],
               'geometry_sha256':canonical_hash(geometry_signature(adaptive)),
               'seconds_diagnostic':adaptive['consumer_seconds']},
         '_adaptive_geometry':geometry_signature(adaptive)}


def compare_coefficients(evaluators):
    output={}
    baseline=evaluators['expanded']
    for method in METHODS[1:]:
        ev=evaluators[method]
        lower,equal,higher=[],[],[]
        for j in range(51):
            a=baseline.values[j]+arb(0,baseline.radii[j])
            b=ev.values[j]+arb(0,ev.radii[j])
            check(a.overlaps(b),'equivalent coefficient balls disjoint at order '+str(j))
            check(baseline._raw_jets[j].imag.overlaps(ev._raw_jets[j].imag),
                  'equivalent imaginary integral balls disjoint at order '+str(j))
            (lower if ev.radii[j]<baseline.radii[j] else
             higher if ev.radii[j]>baseline.radii[j] else equal).append(j)
        output[method]={'all_51_real_coefficient_balls_overlap':True,
             'all_51_imaginary_integral_balls_overlap':True,
             'smaller_radius_orders':lower,'equal_radius_orders':equal,'larger_radius_orders':higher}
    return output


def hybrid_evaluator(evaluators,acquisitions,base,choices):
    begin=time.monotonic()
    check(len(choices)>=2 and all(method in METHODS for method in choices),'invalid hybrid alternatives')
    for method in choices:
        validate_coefficients(evaluators[method],acquisitions[method]['coefficients'])
    ev=copy.copy(evaluators['expanded'])
    ev.values=[];ev.radii=[];ev.coeff_cache={};ev.calls=0
    selection=[]
    for j in range(51):
        method=min(choices,key=lambda key:evaluators[key].radii[j])
        source=evaluators[method]
        # The entire coefficient tuple is selected; no midpoint-radius mixing.
        ev.values.append(source.values[j]);ev.radii.append(source.radii[j])
        selection.append({'j':j,'method':method,'midpoint_dyadic':dyadic(source.values[j]),
                          'quadrature_radius_upper_dyadic':dyadic(source.radii[j])})
    selection_seconds=time.monotonic()-begin
    ev.setup_seconds=sum(acquisitions[method]['seconds_including_original_common_setup'] for method in choices)+selection_seconds
    ev.callbacks=sum(acquisitions[method]['setup_callbacks'] for method in choices)
    return ev,{'policy':'minimum exact real quadrature radius, choose whole(midpoint,radius) tuple; tie priority follows alternatives',
        'alternatives':list(choices),
        'predeclared':True,'selection':selection,'selection_counts':dict(Counter(row['method'] for row in selection)),
        'selection_seconds_diagnostic':selection_seconds,
        'charged_all_selected_complete_setups_seconds':ev.setup_seconds,
        'charged_all_selected_complete_setups_callbacks':ev.callbacks,
        'cost_claim':False}


def compare_results(results):
    baseline=results['expanded']
    output={}
    for method,result in results.items():
        if method=='expanded':
            continue
        errors=[]
        for j in range(3):
            old=undyadic(baseline['whole_box_complete_error_ledger'][j]['components_dyadic']['total'])
            new=undyadic(result['whole_box_complete_error_ledger'][j]['components_dyadic']['total'])
            errors.append({'j':j,'old_complete_added_error':s(old),'candidate_complete_added_error':s(new),
                'candidate_over_expanded':s(new/old),'expanded_minus_candidate':s(old-new),
                'strict_decrease':bool(new<old)})
        oldcells=baseline['fixed_40_cell_consumer']['cells']
        newcells=result['fixed_40_cell_consumer']['cells']
        output[method]={'whole_box_errors':errors,
            'all_40_same_reported_jets':all(a['jet']==b['jet'] for a,b in zip(oldcells,newcells)),
            'same_reported_signed_interval_count':sum(a['excess_norm2']==b['excess_norm2'] for a,b in zip(oldcells,newcells)),
            'fixed_minimum_reported_identical':baseline['fixed_40_cell_consumer']['minimum_signed_excess_norm2']==result['fixed_40_cell_consumer']['minimum_signed_excess_norm2'],
            'adaptive_geometry_identical':baseline['_adaptive_geometry']==result['_adaptive_geometry'],
            'adaptive_calls_identical':baseline['adaptive_consumer']['summary']['total_consumer_calls']==result['adaptive_consumer']['summary']['total_consumer_calls']}
    return output


def strongest_comparisons(results):
    output=[]
    for j in range(3):
        pure={method:undyadic(results[method]['whole_box_complete_error_ledger'][j]['components_dyadic']['total'])
              for method in METHODS}
        strongest=min(METHODS,key=lambda method:pure[method])
        old=undyadic(results[OLD_HYBRID]['whole_box_complete_error_ledger'][j]['components_dyadic']['total'])
        new=undyadic(results[HYBRID]['whole_box_complete_error_ledger'][j]['components_dyadic']['total'])
        output.append({'j':j,'strongest_pure_method':strongest,'strongest_pure_complete_added_error':s(pure[strongest]),
             'old_two_alternative_hybrid_error':s(old),'all_three_alternative_hybrid_error':s(new),
             'all_three_over_strongest_pure':s(new/pure[strongest]),
             'all_three_over_old_two_hybrid':s(new/old),
             'factoring_marginal_complete_error_decrease':s(old-new),
             'factoring_marginal_relative_decrease':s((old-new)/old),
             'strict_factoring_marginal_decrease':bool(new<old)})
    return output


def prepare_inputs(repo,expected_file):
    basepath=repo/INV/'numerics/high_height_consumer/high_height_consumer.py'
    integrationpath=repo/S01/'numerics/integrate_paired_tail_consumer.py'
    pairedpath=repo/S01/'numerics/check_paired_modular_tail.py'
    ledgerpath=repo/S01/'numerics/S01_COMPLETE_CONSUMER_20261019.json'
    ledger=json.loads(ledgerpath.read_text())
    check(ledger['status']=='pass','historical S01 ledger status is not pass')
    check(ledger['script_sha256']==digest(integrationpath),'historical S01 producer is stale')
    historical_receipt=verify_pins(repo,ledger['source_sha256'])
    paths=[basepath,integrationpath,pairedpath,ledgerpath,
       repo/S05/'notes/02_SOURCE_CONSUMER_FIT_AND_SHIFTED_ACQUISITION_SELECTION_20261019.md',
       repo/S05/'numerics/probe_shifted_source_consumer_fit.py',
       repo/S05/'numerics/check_covariant_source_enclosures.py']
    source_pins={str(path.relative_to(repo)):digest(path) for path in paths}
    if expected_file:
        expected=json.loads(expected_file.read_text())
        if 'source_sha256' in expected:
            expected=expected['source_sha256']
        check(set(expected)==set(source_pins),'full expected source-pin keyset required')
        verify_pins(repo,expected)
        check(all(source_pins.get(path)==sha for path,sha in expected.items()),'expected input pin not in this run')
    base=load_module(basepath,'s05_t2_original_complete_consumer')
    integration=load_module(integrationpath,'s05_t2_original_paired_integration')
    paired=load_module(pairedpath,'s05_t2_original_paired_bound')
    return base,integration,paired,ledger,source_pins,historical_receipt


def run(repo,bits,model,effort,output_dir,comparison_contract,expected_file=None):
    validate_metadata(bits,model,effort)
    check(comparison_contract.is_file(),'frozen comparison contract required')
    contract_sha=digest(comparison_contract)
    if expected_file:
        expected_report=json.loads(expected_file.read_text())
        if 'comparison_contract_input' in expected_report:
            check(expected_report['comparison_contract_input']['sha256']==contract_sha,
                  'frozen contract hash changed')
    base,integration,paired,historical,pins,historical_receipt=prepare_inputs(repo,expected_file)
    ctx.prec=bits
    cover=frozen_cover(historical,bits)
    candidate=make_candidate_class(base)
    started=time.monotonic();evaluators={};acquisitions={};pair_receipts={};common=None
    for method in METHODS:
        ev,acquisition=acquire(base,candidate,bits,method)
        pair_receipt=install_common_pair(ev,integration,paired)
        ev.setup_seconds+=pair_receipt['seconds']
        data=common_data(ev)
        if common is None:
            common=data
        else:
            check(data==common,'candidate changed moment/source/mode/order52/Taylor payment')
        evaluators[method]=ev;acquisitions[method]=acquisition;pair_receipts[method]=pair_receipt
        print(json.dumps({'bits':bits,'method':method,'coefficient_count':51,
              'setup_callbacks':ev.callbacks,'setup_seconds':ev.setup_seconds,
              'j0_radius':s(ev.radii[0]),'acquisition_status':'pass'}),flush=True)
    coefficient_comparison=compare_coefficients(evaluators)
    hybrid_receipts={}
    for name,choices in ((OLD_HYBRID,('expanded','exponential_grouped')),(HYBRID,METHODS)):
        hybrid,receipt=hybrid_evaluator(evaluators,acquisitions,base,choices)
        tail_seconds=sum(pair_receipts[method]['seconds'] for method in choices)
        hybrid.setup_seconds+=tail_seconds
        receipt['charged_all_selected_paired_tail_setup_seconds']=tail_seconds
        receipt['charged_total_setup_seconds']=hybrid.setup_seconds
        evaluators[name]=hybrid;hybrid_receipts[name]=receipt
    results={}
    for method,ev in evaluators.items():
        ctx.prec=bits
        check(common_data(ev)==common,'common budget altered before complete comparison')
        results[method]=evaluate(ev,base,cover)
        print(json.dumps({'bits':bits,'method':method,'consumer_status':'pass',
             'whole_box_complete_errors':[row['components']['total'] for row in results[method]['whole_box_complete_error_ledger']],
             'fixed_minimum':results[method]['fixed_40_cell_consumer']['minimum_signed_excess_norm2'],
             'adaptive_calls':results[method]['adaptive_consumer']['summary']['total_consumer_calls']}),flush=True)
    comparison=compare_results(results)
    strongest=strongest_comparisons(results)
    # All physical images must overlap for the equal finite-integral target.
    for method,result in results.items():
        for old,new in zip(results['expanded']['fixed_40_cell_consumer']['cells'],result['fixed_40_cell_consumer']['cells']):
            check(old['t']==new['t'] and old['x']==new['x'],'fixed physical geometry changed')
            check(all(arb(a).overlaps(arb(b)) for a,b in zip(old['jet'],new['jet'])),
                  'equal physical jet images disjoint')
        result.pop('_adaptive_geometry')
    verify_pins(repo,pins)
    check(digest(comparison_contract)==contract_sha,'comparison contract changed during execution')
    report={'schema':'s05-t2-complete-shifted-source-comparison-v1',
        'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':model,'actual_effort':effort,'llm_assistance':'substantial; internal same-model research and separate review',
        'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':bits,
        'script_sha256':digest(__file__),'source_sha256':pins,
        'comparison_contract_input':{'path_at_execution':str(comparison_contract),'sha256':contract_sha},
        'historical_S01_input_verification':{'status_pass':True,'producer_matches':True,'source_pin_matches':historical_receipt},
        'primary_metric':'Complete added physical errors at orders 0..2 in unchanged shifted acquisition on B, including all common tails, Taylor and outward arithmetic payments.',
        'frozen':{'B_t':['1/100','1/5'],'B_x':['999','1001'],'midpoint':['21/200','1000'],
             'source_contour':'v=u+i*d, d=pi/8-4*log(1000)/1000','u_integral':['0','2'],
             'physical_units':'(H,Hx,Hxx)/Gc, Gc=1000^(7/4)*exp(-125*pi)',
             'source_modes':[1,11],'coefficients':[0,50],'physical_outputs':[0,1,2],
             'degrees':[24,12],'moment_majorant_order':52,'fixed_geometry_cells':40,
             'fixed_geometry_sha256':canonical_hash(cover)},
        'formulas':{'expanded':'exp(tc*v^2+v+i*1000*u)*sum((2*lam^2*q^2-3*lam*q)*exp(-lam*q))',
             'polynomial_factored':'exp(tc*v^2+v+i*1000*u)*sum(w*(2*w-3)*exp(-w))',
             'exponential_grouped':'exp(tc*v^2+i*1000*u)*sum(exp(v-w)*w*(2*w-3))',
             'definitions':'q=exp(4v), w=lam*q, lam=pi*n^2; every integrand includes1000^(9/4)*(i*v)^j'},
        'common_data':common,'common_data_sha256':canonical_hash(common),
        'acquisitions':acquisitions,'paired_tail_acquisitions':pair_receipts,
        'coefficient_radius_comparison':coefficient_comparison,'hybrid_receipts':hybrid_receipts,
        'results':results,'comparison_to_expanded':comparison,
        'strongest_same_caller_comparisons':strongest,
        'strongest_existing_physical_accuracy_reference':'Different real-source 768-bit representation has complete error<2.165e-12Gc; not reacquired here and not claimed beaten.',
        'limitations':['Source factoring is finite mode algebra; no real parity-Taylor transfer or new signed-core estimate.',
             'Coefficient quadrature radii include arithmetic+integration error. Polynomial image arithmetic is outward rounded and retained separately from its complete added-error ledger.',
             'All three alternative acquisitions are charged to the hybrid. Timing is diagnostic; no matched cost or factor-two speedup claim.',
             'Same 40 closed physical cells and original adaptive acceptance; no new coverage, exterior theorem, or Newman bound.',
             'Uniform high-order tails and original moment/Taylor bounds remain common; only paired order0..2 omitted tails are installed equally.'],
        'new_coverage':False,'cost_claim':False,'status':'pass',
        'seconds_total_diagnostic':time.monotonic()-started}
    output=output_dir/f'S05_T2_COMPLETE_SHIFTED_SOURCE_{bits}_20261019.json'
    output.write_text(json.dumps(report,indent=2)+'\n')
    check(output.stat().st_size<1000000,'small record policy exceeded')
    print(json.dumps({'bits':bits,'output':str(output),'bytes':output.stat().st_size,'status':'pass'}),flush=True)
    return report


def validate_precision_replays(reports):
    if len(reports)<2:
        return
    for previous,current in zip(reports,reports[1:]):
        for method in METHODS:
            old=previous['acquisitions'][method]['coefficients']
            new=current['acquisitions'][method]['coefficients']
            for a,b in zip(old,new):
                av=undyadic(a['midpoint_dyadic'])+arb(0,undyadic(a['quadrature_radius_upper_dyadic']))
                bv=undyadic(b['midpoint_dyadic'])+arb(0,undyadic(b['quadrature_radius_upper_dyadic']))
                check(av.overlaps(bv),'precision replay coefficient balls disjoint')
                check(restore_ball(a['imaginary_integral_ball']).overlaps(restore_ball(b['imaginary_integral_ball'])),
                      'precision replay imaginary integral balls disjoint')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    parser.add_argument('--bits',type=int,nargs='+',default=[192,256])
    parser.add_argument('--execution-model',required=True)
    parser.add_argument('--execution-effort',required=True)
    parser.add_argument('--expected-source-pins',type=Path)
    parser.add_argument('--comparison-contract',type=Path,required=True)
    args=parser.parse_args()
    check(bool(args.bits) and len(set(args.bits))==len(args.bits),'nonempty unique precision list required')
    for bits in args.bits:
        validate_metadata(bits,args.execution_model,args.execution_effort)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    reports=[run(args.repo.resolve(),bits,args.execution_model,args.execution_effort,
                 args.output_dir,args.comparison_contract.resolve(),args.expected_source_pins) for bits in args.bits]
    ctx.prec=max(args.bits)
    validate_precision_replays(reports)
    if len(reports)>1:
        print(json.dumps({'precision_replays':'pass','all_3x51_equivalent_real_coefficient_balls_overlap':True}),flush=True)


if __name__=='__main__':
    main()
