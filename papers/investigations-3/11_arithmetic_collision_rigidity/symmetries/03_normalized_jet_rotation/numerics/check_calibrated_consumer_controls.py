#!/usr/bin/env python3
"""S03-T3 actual-helper controls and fresh source-specific event replay.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual authoring model gpt-6.1-sol, effort ultra; same-model internal work.
No theta estimates are transferred to the altered-source controls.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import time
from types import SimpleNamespace, ModuleType

import flint
from flint import arb, acb, acb_series, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/03_normalized_jet_rotation'
S02=INV/'symmetries/02_cutoff_reflection/numerics'

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module

def check(ok,msg):
    if not ok: raise ArithmeticError(msg)

def A(x): return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def out(v):
    check(v.is_finite(),'nonfinite reported control value')
    return v.str(38,more=True)
def zero(v,msg): check(v.contains(0),msg)
def excludes_zero(v,msg): check(not v.contains(0),msg)
def rational_dyadic(row):
    n,e=int(row['mantissa']),int(row['exponent'])
    return F(n*2**e) if e>=0 else F(n,2**(-e))
def rational_poly(cs,x):
    q=F(0)
    for c in reversed(cs): q=q*x+c
    return q


def event_and_oscillator(m):
    """Use each fixture's exact residual/anchor errors in the actual consumers."""
    ii=acb(0,1);x=A(0);a=A(-1);w=A(1);wp=A(0)
    # H=x^2-2(t-1/4), H_t=-H_xx, at t=1/4, x=0.
    H=[A(0),A(0),A(2)];f=[A(1),A(0),A(0)]
    check(A(-2)==-H[2],'polynomial backward heat equation')
    # r=H-f has Wa=2i at a=-1 and Wx=-1 at the event.
    Wr_a=acb(0,2);Wr_x=acb(-1,0);Wf=m.jet_vector(f,w)
    Wg=(ii*(x-a)).exp()*Wr_a
    B=abs((-ii*x).exp()*Wr_x-(-ii*a).exp()*Wr_a).upper()
    direct=m.paid_radius(abs(Wf).lower(),abs(Wr_x).upper())
    calibrated=m.paid_radius(abs(Wf+Wg).lower(),B)
    scalar=m.scalar_radius(abs(Wf+Wr_a).lower(),
        abs((-ii*x).exp()*Wf-(-ii*a).exp()*Wf).upper(),A(0),B)
    source=m.propagate_radius(m.jet_vector(H,w),m.jet_vector(H,w),m.Wprime(H,w,wp),A(0))
    for name,value in [('direct',direct),('calibrated',calibrated),('scalar',scalar),('source_direct',source)]:
        check(not value>0,'exact polynomial event passed '+name)
    # A collision at a nonzero midpoint must be rejected by propagation too.
    # W(x)=1-x on [0,1], midpoint 1/2, derivative -1, event at 1.
    propagated=m.propagate_radius(acb(arb(A(F(1,2)),A(F(1,2))),0),
                                 acb(A(F(1,2))),acb(-1),A(F(1,2)))
    check(not propagated>0,'propagation paid incorrectly on endpoint event')
    check(abs(acb(A(F(1,2)))).lower()>0,'omitted derivative payment mutant escaped')
    check(abs(Wf).lower()>0 and abs(Wf+Wg).lower()>0,
          'omitted residual payment mutants are not challenged')
    # The retained anchor is uncertain: nominal Wg=d, actual residual zero.
    d=A(F(1,8));eps=d
    uncertain_direct=m.paid_radius(d,eps)
    uncertain_scalar=m.scalar_radius(d,A(0),eps,A(0))
    check(not uncertain_direct>0 and not uncertain_scalar>0,
          'uncertain anchor generated a false strict exclusion')
    check(m.paid_radius(d,A(0))>0 and m.scalar_radius(d,A(0),A(0),A(0))>0,
          'anchor-uncertainty omission mutation is not detected')
    # Nonconstant phase, no heat premise: g=A0 cos(theta)+B0 sin(theta).
    x=A(F(2,5));theta=x+x*x/5;w=1+2*x/5;wp=A(F(2,5))
    aa=A(F(3,5));bb=A(F(-2,7))
    g=aa*theta.cos()+bb*theta.sin()
    gx=w*(-aa*theta.sin()+bb*theta.cos())
    gxx=-w*w*g+wp*gx/w
    Wg=m.jet_vector([g,gx,gxx],w)
    Rg=g+gxx/(w*w)-wp*gx/(w**3)
    zero(Rg,'oscillator Rg is not zero')
    zero(m.Wprime([g,gx,gxx],w,wp)-ii*w*Wg,'calibration derivative sign')
    excludes_zero(m.Wprime([g,gx,gxx],w,wp)+ii*w*Wg,
                  'wrong-sign Wg derivative mutant not distinguished')
    # Independent automatic spatial derivative for a nonoscillator jet.
    z=acb_series([acb(x),acb(1)],4);q=1+z+z*z;ws=2+z
    qj=[q[0].real,q[1].real,2*q[2].real]
    expected=(q-ii*q.derivative()/ws).derivative()[0]
    actual=m.Wprime(qj,2+x,A(1))
    zero(actual-expected,'actual Wprime vs independent series')
    mutant=acb(qj[1],-qj[2]/(2+x)-qj[1]/((2+x)**2))
    excludes_zero(mutant-expected,'wrong omega_x sign mutant not distinguished')
    invalid=[]
    for label,call in [('negative_paid_error',lambda:m.paid_radius(A(1),A(-1))),
          ('negative_scalar_increment',lambda:m.scalar_radius(A(1),A(-1),A(0),A(0))),
          ('negative_anchor_error',lambda:m.scalar_radius(A(1),A(0),A(-1),A(0))),
          ('negative_residual_increment',lambda:m.scalar_radius(A(1),A(0),A(0),A(-1))),
          ('negative_halfwidth',lambda:m.propagate_radius(acb(1),acb(1),acb(0),A(-1)))]:
        try:call()
        except ArithmeticError:invalid.append(label)
        else:raise ArithmeticError('invalid helper input accepted: '+label)
    return {'polynomial':'H=x^2-2(t-1/4); exact event (1/4,0); own errors',
       'polynomial_paid_margins':{k:out(v) for k,v in
           [('direct',direct),('calibrated',calibrated),('scalar',scalar),('source_direct',source)]},
       'polynomial_complete_residual_increment_upper':out(B),
       'endpoint_propagation_margin':out(propagated),
       'anchor_uncertainty':{'own_error':out(eps),'direct':out(uncertain_direct),
            'scalar':out(uncertain_scalar),'omitting_error_would_strictly_pass':True},
       'oscillator_Rg_zero':True,'Wg_prime_equals_positive_i_omega_Wg':True,
       'Wprime_independent_series':True,'mutations_detected':[
           'omit direct residual error','omit calibrated residual error','omit derivative propagation cost',
           'omit nonzero anchor uncertainty','reverse Wg derivative sign','reverse omega_x derivative sign'],
       'invalid_inputs_rejected':invalid}


def source_payment_fixture(m,work):
    """Exercise the actual full run source branch with exact own source balls.

    Every fixture source value encloses 2+[-1/4,1/4], and its complete
    source error is already in the returned ball. The radius is 7/4 up to
    outward radius rounding (<2^-20). A second .25 charge fails this bound.
    """
    source_value=arb(2,A(F(1,4)));source_error=source_value.rad().upper()
    class Source:
        def enclose(self,*_):
            return [source_value,A(0),A(0)],[{'total':source_error},{'total':A(0)},{'total':A(0)}]
    class Evaluator:
        def __init__(self,*_):
            self.eta={'full':source_error}
            self.old=SimpleNamespace(alpha=lambda _:acb(0),alphap=lambda _:acb(0),
               W_real=lambda z,t:acb_series([0],3),J=lambda z,t,n:(acb_series([0],3),acb(0)))
        def jets(self,x,t,recenter=None):
            return {'theta':x,'omega':A(1),'omega_x':A(0),'b':A(0),'b_x':A(0),
               'chi':A(1),'full':[A(2),A(0),A(0)]}
    hh=SimpleNamespace(validate_setup=lambda *_:None,load_setup=lambda _:Source())
    setup_path=work/'EXACT_CONSTANT_SOURCE_FIXTURE.json'
    setup_path.write_text(json.dumps({'bits':192})+'\n')
    zero_coeff=[{'mantissa':'0','exponent':0}]
    contract={'domain':{'t':['1/100','1/5'],'x':[999,1001],'anchor':999,'cover':[32,128]},
       'inherited_physical_error_ledger':{'scope':'exact fixture'},
       'source_sha256':{},'source_setup':{'mathematical_setup_sha256':'fixture'},
       'nominal_physical_anchor_time_coefficients':{'physical_delta_over_Gstar':zero_coeff,
         'physical_delta_x_over_Gstar':zero_coeff},'analytic_only_complete_increment_upper':'0',
       'slabs':[{'nominal_anchor_uncertainty_upper':'0','complete_correlated_increment_upper':'0',
         'uncalibrated_residual_anchor_radius_upper':'1/4','uncalibrated_residual_slab_radius_upper':'1/4'} for _ in range(32)]}
    fixture_root=work/'fixture-root';fixture_lane=fixture_root/LANE/'numerics'
    fixture_lane.mkdir(parents=True,exist_ok=True)
    old={'physical_error_ledger':contract['inherited_physical_error_ledger'],
       'calibrated_oscillator':{'nominal_physical_anchor_time_coefficients':contract['nominal_physical_anchor_time_coefficients']},
       'slabs':[{'t':['1/100','1/5'],'nominal_oscillator_anchor_uncertainty_upper':'0',
          'correlated_signed_prefix_integral_upper':'0','anchor_residual_jet_radius_upper':'1/4',
          'full_box_residual_jet_radius_upper':'1/4'} for _ in range(32)]}
    for row in contract['slabs']: row['t']=['1/100','1/5']
    (fixture_lane/'S03_CORRELATED_RESIDUAL_192_20261018.json').write_text(json.dumps(old)+'\n')
    (fixture_lane/'S03_PHASE_ANALYTIC_ALLOWANCE_20261019.json').write_text(json.dumps(
       {'runs':[{'allowance':{'combined':'0'}}]})+'\n')
    original_load,original_canonical=m.load,m.canonical_setup
    try:
        m.load=lambda p,name:hh if p.name=='high_height_consumer.py' else SimpleNamespace(ClosedJetEvaluator=Evaluator)
        m.canonical_setup=lambda _:'fixture'
        row=m.run(fixture_root,contract,setup_path,192)
    finally:m.load,m.canonical_setup=original_load,original_canonical
    expected=source_value.lower()
    for key in ['source_direct_raw','source_direct_propagated','source_direct_best']:
        check(abs(A(row['direct_complete_phase_radius_lower'][key])-expected).upper()<A(F(1,2**20)),
              'source error charged again or interval rounding excessive: '+key)
    diagnostic=A(row['maximum_source_phase_error_diagnostic_upper'])
    zero(diagnostic-source_error,'own source error diagnostic')
    check(m.paid_radius(expected,source_error)<expected,'double payment mutation lacks gap')
    return {'scope':'Actual run() source branch on an exact constant first-jet fixture; fixture source errors already inside balls',
       'source_ball':out(source_value),'source_error_diagnostic_upper':out(diagnostic),
       'expected_once_paid_radius':out(expected),'radius_rounding':'Arb radius enclosure retained; each actual radius differs from complete source ball lower endpoint by less than 2^-20','actual_source_direct_radii':{
           k:row['direct_complete_phase_radius_lower'][k] for k in ['source_direct_raw','source_direct_propagated','source_direct_best']},
       'double_source_payment_mutation_would_fail_once_paid_bound':True,
       'actual_cell_evaluations':row['work']['cells']}


def dyadic_and_normalizer(m,repo,anchors):
    contract=json.loads(anchors.read_text());anchor=contract['nominal_physical_anchor_time_coefficients']
    coeffs={key:anchor[key] for key in ['physical_delta_over_Gstar','physical_delta_x_over_Gstar']}
    n=0;mutations=0;maxbits=0
    for rows in coeffs.values():
        for row in rows:
            decoded=m.dyadic(row);exact=rational_dyadic(row)
            check(decoded.is_exact(),'dyadic import gained rounding radius')
            check(F(str(decoded.fmpq()))==exact,'dyadic import differs from exact rational')
            maxbits=max(maxbits,abs(int(row['mantissa'])).bit_length());n+=1
            if not (decoded-A(float(exact))).contains(0):mutations+=1
    check(n==26 and mutations>0,'dyadic export or float mutation not challenged')
    evaluator_mod=load('s03_t3_control_full',repo/S02/'evaluate_complete_frozen_jets.py')
    e=evaluator_mod.ClosedJetEvaluator(repo,192);o=e.old;ii=acb(0,1);rows=[]
    for X,T in [(F(999)+F(11,32),F(37,500)),(F(1000)+F(7,16),F(31,200))]:
        x,t=A(X),A(T);data=e.jets(x,t)
        check('b' in data and 'b_x' in data,'normalizer return interface omits b/b_x')
        zs=acb_series([acb(x),acb(1)],4);ts=acb_series([acb(t),acb(1)],3)
        N=o.normalizer(zs,t);Nt=o.normalizer(acb(x),ts);G=acb(e.logGc.exp())
        b=(N.derivative()/N)[0];bp=(N.derivative()/N).derivative()[0]
        zero(data['b']-b.real,'offcenter normalizer b spatial derivative')
        zero(data['b_x']-bp.real,'offcenter normalizer bx spatial derivative')
        check(not data['b'].contains(0) and not data['b_x'].contains(0),'offcenter derivative control trivial')
        v=[1+t,A(3),A(5)];physical=(1+t)+3*(zs-x)+A(F(5,2))*(zs-x)**2
        qseries=G*physical/N;q=m.Q_from_physical(v,data)
        for j in range(3):zero(q[j]-math.factorial(j)*qseries[j].real,'physical conversion offcenter derivative '+str(j))
        # Both normalizer derivative terms must be present in Qxx.
        no_b= data['chi']*v[2]
        no_bp=data['chi']*(v[2]-2*data['b']*v[1]+data['b']**2*v[0])
        excludes_zero(no_b-qseries[2].real*2,'omit b normalizer mutation escaped')
        excludes_zero(no_bp-qseries[2].real*2,'omit bx normalizer mutation escaped')
        full=o.series_approximation(acb(x),t,True)
        for j in range(3):zero(data['full'][j]-math.factorial(j)*full[j].real,'offcenter coherent full spatial jet '+str(j))
        # Time derivative of physical-to-normalized Q, independently as a series.
        s=(1-ii*acb(x))/2
        logA_t=((o.alpha(s)**2+o.alpha(1-s)**2)/8).real
        zero((Nt.derivative()/Nt)[0].real-logA_t,'normalizer offcenter time derivative')
        Qt=G*(1+ts)/Nt
        qt_formula=data['chi']*(1-v[0]*logA_t)
        zero(Qt[1].real-qt_formula,'physical Q offcenter time derivative')
        excludes_zero(Qt[1].real-data['chi'],'omit normalizer time derivative mutation escaped')
        # Retained polynomial evaluation at noncentral times vs exact rationals.
        for key,cs in coeffs.items():
            expected=rational_poly([rational_dyadic(c) for c in cs],T-F(21,200))
            actual=m.poly([m.dyadic(c) for c in cs],t-A(F(21,200)))
            zero(actual-A(expected),'offcenter exact dyadic anchor polynomial '+key)
        rows.append({'x':str(X),'t':str(T),'b':out(data['b']),'b_x':out(data['b_x']),
            'normalizer_log_time_derivative':out(logA_t),
            'spatial_full_jets_verified':3,'spatial_physical_conversion_jets_verified':3,
            'normalizer_and_Q_time_derivatives_verified':True,'exact_anchor_polynomials_verified':2})
    return {'exact_dyadics_checked':n,'largest_mantissa_bits':maxbits,
      'dyadics_distinguished_from_binary64_conversion':mutations,
      'offcenter_derivative_checks':rows,'mutations_detected':[
          'decode retained coefficients through binary64','omit normalizer b','omit normalizer bx','omit normalizer time derivative']}


def contract_guards(m,repo,anchors,setup_path,work):
    contract=json.loads(anchors.read_text());setup=json.loads(setup_path.read_text())
    check(m.canonical_setup(setup)==contract['source_setup']['mathematical_setup_sha256'],
          'control baseline mathematical cache identity')
    observed=copy.deepcopy(setup);observed['setup']['seconds']+=1
    observed['setup']['callbacks']+=1
    check(m.canonical_setup(observed)==m.canonical_setup(setup),
          'canonical identity improperly includes acquisition observations')
    cases=[]
    changed=copy.deepcopy(contract);changed['domain']['x'][1]=1002
    cases.append(('changed fixed domain',changed,setup_path,'fixed B/anchor/cover contract'))
    changed=copy.deepcopy(contract)
    row=changed['nominal_physical_anchor_time_coefficients']['physical_delta_over_Gstar'][0]
    row['mantissa']=str(int(row['mantissa'])+1)
    cases.append(('changed retained dyadic anchor',changed,setup_path,'exported nominal anchors altered'))
    changed=copy.deepcopy(contract);changed['slabs'][0]['nominal_anchor_uncertainty_upper']='0'
    cases.append(('erased retained anchor uncertainty',changed,setup_path,'retained slab allowance altered'))
    changed=copy.deepcopy(contract);changed['analytic_only_complete_increment_upper']='0'
    cases.append(('changed complete analytic allowance',changed,setup_path,'retained analytic-only increment altered'))
    changed=copy.deepcopy(contract);changed['inherited_physical_error_ledger']['control_mutation']='changed'
    cases.append(('changed inherited complete error ledger',changed,setup_path,'inherited complete error ledger altered'))
    changed=copy.deepcopy(contract);key=next(iter(changed['source_sha256']))
    changed['source_sha256'][key]='0'*64
    cases.append(('changed source identity pin',changed,setup_path,'anchor dependency pin'))
    corrupt=copy.deepcopy(setup)
    row=corrupt['setup']['midpoint_jets'][0]['midpoint_dyadic'];row['mantissa']=str(int(row['mantissa'])+1)
    check(m.canonical_setup(corrupt)!=m.canonical_setup(setup),'corrupt mathematical cache canonical identity unchanged')
    corrupt_path=work/'CORRUPT_SOURCE_CACHE_CONTROL.json';corrupt_path.write_text(json.dumps(corrupt)+'\n')
    cases.append(('changed source mathematical cache',copy.deepcopy(contract),corrupt_path,'source mathematical setup mismatch'))
    outcomes=[]
    real_load=m.load
    try:
        def guarded_load(path,name):
            check(path.name=='high_height_consumer.py','contract mutation reached analytic evaluator/consumer loop')
            return real_load(path,name)
        m.load=guarded_load
        for label,c,path,expected_message in cases:
            try:m.run(repo,c,path,192)
            except ArithmeticError as error:
                check(expected_message in str(error),'wrong input-guard rejection for '+label+': '+str(error))
                outcomes.append({'mutation':label,'rejection':str(error),'rejected_before_consumer_loop':True})
            else:raise ArithmeticError('mutated consumer input accepted: '+label)
    finally:m.load=real_load
    return {'observation_only_cache_changes_preserve_mathematical_identity':True,
       'mathematical_cache_change_alters_identity':True,'mutations':outcomes}


def implementation_mutations(m,repo,anchors,consumer,work):
    """Break actual helper implementations in memory; each control must fail."""
    outcomes=[]
    def reject(label,call):
        try:call()
        except ArithmeticError as error:
            outcomes.append({'implementation_mutation':label,'detected_by_control':str(error)})
        else:raise ArithmeticError('implementation mutation escaped actual controls: '+label)
    for label,name,replacement,control in [
       ('paid_radius omits complete residual error','paid_radius',lambda nominal,error:nominal.lower(),lambda:event_and_oscillator(m)),
       ('scalar_radius omits anchor uncertainty','scalar_radius',
           lambda anchor,increment,error,residual:m.paid_radius((anchor-increment).lower(),residual),lambda:event_and_oscillator(m)),
       ('propagate_radius omits derivative payment','propagate_radius',
           lambda cell,mid,prime,half:max(cell.abs_lower(),mid.abs_lower()),lambda:event_and_oscillator(m)),
       ('Wprime reverses omega_x sign','Wprime',
           lambda jet,w,wp:acb(jet[1],-jet[2]/w-jet[1]*wp/(w*w)),lambda:event_and_oscillator(m)),
       ('dyadic decoder uses binary64','dyadic',lambda row:arb(float(rational_dyadic(row))),lambda:dyadic_and_normalizer(m,repo,anchors)),
       ('Q_from_physical omits normalizer derivatives','Q_from_physical',
           lambda values,data:[data['chi']*v for v in values],lambda:dyadic_and_normalizer(m,repo,anchors))]:
        original=getattr(m,name)
        try:
            setattr(m,name,replacement);reject(label,control)
        finally:setattr(m,name,original)
    # Load an in-memory copy with one real source-consumer payment altered.
    source=consumer.read_text();needle="'source_direct_best':rs,"
    check(source.count(needle)==1,'source double-payment mutation site changed; revise explicit control')
    source=source.replace(needle,"'source_direct_best':paid_radius(rs,source_error),")
    mutant=ModuleType('s03_t3_source_double_payment_mutant');mutant.__file__=str(consumer)
    exec(compile(source,str(consumer)+' [in-memory source-payment mutant]','exec'),mutant.__dict__)
    reject('run source branch subtracts complete source error twice',lambda:source_payment_fixture(mutant,work))
    return {'mutation_method':'Temporary in-memory replacement of actual helpers and one compiled source-branch payment; retained consumer file unchanged',
       'all_mutants_detected':True,'outcomes':outcomes}


def fresh_source_controls(m,repo,work,model,effort):
    replay=repo/INV/'numerics/replay_nonstationary_controls.py';record_path=work/'SOURCE_SPECIFIC_REPLAY.json'
    receipts=work/'receipts';receipts.mkdir(parents=True,exist_ok=True)
    subprocess.run([sys.executable,str(replay),'--repo',str(repo),'--receipts',str(receipts),
        '--output',str(record_path),'--execution-model',model,'--execution-effort',effort],
        check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=150)
    source=json.loads(record_path.read_text());ctx.prec=192
    check(source['interface_precision_bits']==192,'fresh source interface precision')
    check(source['script_sha256']==sha(replay),'fresh source replay script identity')
    check(source['checker_sha256']==sha(repo/INV/'numerics/run_plan02_pilot.py'),'fresh checker identity')
    outcomes=[]
    def challenge(name,jets,domain,event):
        # A=Gstar=1, b=bx=0, omega=1: source-neutral first-jet control.
        check(len(jets)==3 and all(v.is_finite() for v in jets),
              'nonfinite source-control jet balls')
        data={'b':A(0),'b_x':A(0),'chi':A(1)}
        q=m.Q_from_physical(jets,data);W=m.jet_vector(q,A(1));P=m.Wprime(q,A(1),A(0))
        margin=m.paid_radius(m.propagate_radius(W,W,P,A(0)),A(0))
        # Existing signed witness retained to distinguish first-jet from L0.
        old_sign=jets[1]*jets[1]-jets[0]*jets[2]-(jets[0]*jets[0]+jets[1]*jets[1])/100
        check(margin.is_finite() and old_sign.is_finite(),
              'nonfinite source-control firstjet margin or signed diagnostic')
        if event:
            check(jets[0].contains(0) and jets[1].contains(0),'fresh event jets miss zero')
            check(not margin>0,'actual first-jet helper accepted fresh source event')
        else:check(old_sign<0,'Euler source witness no longer violates old sign')
        return {'control':name,'domain':domain,'source_jet_balls':[out(v) for v in jets],
          'actual_paid_direct_firstjet_margin':out(margin),'strict_firstjet_acceptance':bool(margin>0),
          'old_signed_excess':out(old_sign),'strict_signed_acceptance':bool(old_sign>0),
          'enclosed_event':event,'theta_error_constants_used':False,
          'expectation':'firstjet must reject' if event else 'old sign must reject; firstjet is allowed to pass'}
    for event in source['screen']['event_rejections']:
        outcomes.append(challenge(event['control'],[arb(v) for v in event['event_jet_enclosures']],event['event_domain'],True))
    check(len(outcomes)==5,'fresh source-specific event count')
    euler=json.loads((receipts/'EULER_FACTOR_REPLAY.json').read_text())
    outcomes.append(challenge('Euler-factor p=41 negative-Laguerre witness',
        [arb(v['full_jet']['display']) for v in euler['jets']],euler['parameters'],False))
    identities=source['screen']['receipt_identities']
    for value in identities.values():check(sha(receipts/value['file'])==value['sha256'],'fresh receipt identity')
    return {'fresh_replay_stored_sha256':sha(record_path),'external_receipts':str(receipts),
      'fresh_receipt_identities':identities,'outcomes':outcomes,
      'analytic_premise_screen':source['screen']['analytic_premise_screen'],
      'transport':'Fresh source receipt display balls conservatively re-enclosed at192 bits; no exact dyadic identity asserted',
      'scope':'Five source-specific event boxes through actual new direct helpers; Euler witnesses the signed estimate only. No theta constants, damping/event threshold, or new source theorem.'}


def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True,type=Path)
    p.add_argument('--consumer',required=True,type=Path);p.add_argument('--anchors',required=True,type=Path)
    p.add_argument('--setup',required=True,type=Path)
    p.add_argument('--work-dir',required=True,type=Path);p.add_argument('--output',required=True,type=Path)
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    args=p.parse_args();begin=time.monotonic();ctx.prec=192
    repo=args.repo.resolve();work=args.work_dir.resolve();work.mkdir(parents=True,exist_ok=True)
    m=load('s03_t3_controls_actual_consumer',args.consumer.resolve())
    mechanisms=event_and_oscillator(m)
    ledger=source_payment_fixture(m,work)
    normalizer=dyadic_and_normalizer(m,repo,args.anchors)
    mutants=implementation_mutations(m,repo,args.anchors,args.consumer,work)
    guards=contract_guards(m,repo,args.anchors,args.setup,work)
    sources=fresh_source_controls(m,repo,work,args.execution_model,args.execution_effort)
    paths=[repo/INV/'numerics/replay_nonstationary_controls.py',repo/INV/'numerics/run_plan02_pilot.py',
      repo/INV/'numerics/high_height_consumer/high_height_consumer.py',
      repo/S02/'evaluate_complete_frozen_jets.py',repo/S02/'check_cutoff_reflection.py',
      repo/INV/'numerics/certify_shifted_theta_jet.py',
      repo/'papers/investigations-2/active/22_theta_manifold_geometry/numerics/certify_square_support_endpoint_collision.py',
      repo/'papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_two_endpoint_control.py',
      repo/'papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_center_separation.py',
      repo/'papers/investigations-2/active/19_euler_factor_controls/numerics/certify_euler_factor_witness.py']
    result={'schema':'s03-t3-calibrated-controls-v1','date':'2026-10-19','timezone':'America/New_York',
       'prepared_for':'Edward Baker','actual_model':args.execution_model,'actual_effort':args.execution_effort,
       'llm_assistance':'substantial; separate delegated same-model internal controls',
       'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':192,'status':'pass',
       'scope':'Actual-helper and source-ledger controls; no primary-box performance claim, no new coverage, no independent human review',
       'script_sha256':sha(__file__),'consumer_script_sha256':sha(args.consumer),
       'anchor_export_sha256':sha(args.anchors),'source_setup_stored_sha256':sha(args.setup),
       'source_sha256':{str(path.relative_to(repo)):sha(path) for path in paths},
       'mechanism_controls':mechanisms,'source_payment_control':ledger,
       'dyadic_normalizer_controls':normalizer,'implementation_mutation_controls':mutants,
       'input_contract_guards':guards,'fresh_source_controls':sources,
       'seconds':time.monotonic()-begin}
    serialized=json.dumps(result,indent=2)+'\n';check(len(serialized.encode())<1048576,'small record size policy')
    args.output.write_text(serialized)
    print(json.dumps({'output':str(args.output),'status':'pass','bytes':len(serialized.encode()),
       'fresh_events_rejected':5,'Euler_old_sign_rejected':True,'exact_dyadic_coefficients_checked':26,
       'seconds':result['seconds']}))

if __name__=='__main__':main()
