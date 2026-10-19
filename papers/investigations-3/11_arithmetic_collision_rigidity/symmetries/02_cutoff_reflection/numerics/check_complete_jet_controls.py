#!/usr/bin/env python3
"""Fresh source-specific controls through the S02-T2 complete-jet helpers.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Authoring gpt-6.1-sol, effort ultra. Same-model internal replay only.
Requires python-flint 0.9.0. No theta errors are imported into source controls.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

import flint
from flint import arb, acb, acb_series, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
S01=INV/'symmetries/01_modular_self_duality/numerics/check_paired_consumer_controls.py'

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def check(condition,message):
    if not condition:raise ArithmeticError(message)
def load(path):
    spec=importlib.util.spec_from_file_location('s02_complete_jet_control_evaluator',path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module;spec.loader.exec_module(module);return module
def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def display(v):return v.str(38,more=True)

def source_challenge(ev,row,event):
    jets=[arb(s) for s in row['source_specific_jet_balls']]
    check(all(v.is_finite() for v in jets),'nonfinite source ball')
    if event:check(jets[0].contains(0) and jets[1].contains(0),'source event missing')
    signs=ev.sign_tests(jets,arb(0),arb(0),arb(0))
    W,error,direct,schur=ev.first_jet_test(jets,arb(1),arb(0))
    check(error==0,'source event received a nonzero residual allowance')
    for key in ['box_laguerre','box_excess','schur_laguerre_lower','schur_excess_lower']:
        check(not(signs[key]>0),'source control accepted '+key)
    if event:
        check(not(direct>0) and not(schur>0),'collision accepted by first-jet helper')
    else:
        check(all(signs[k]<0 for k in ['box_laguerre','box_excess',
              'schur_laguerre_lower','schur_excess_lower']),'Euler witness not strictly negative')
    return {'control':row['control'],'source_domain':row['source_domain'],
            'source_specific_complete_jet_balls':[display(v) for v in jets],
            'normalization':{'A':'1','b':'0','b_prime':'0','omega':'1','eta':'0'},
            'theta_errors_or_constants_used':False,
            'strict_first_jet_rejected':bool(not(direct>0)) if event else None,
            'strict_joint_Schur_first_rejected':bool(not(schur>0)) if event else None,
            'first_jet_lower':display(direct),'joint_Schur_first_margin':display(schur),
            'strict_sign_acceptances':{key:bool(value>0) for key,value in signs.items() if key!='box_energy'},
            'sign_outputs':{key:display(value) for key,value in signs.items()},
            'Euler_signs_strictly_negative':bool(signs['box_laguerre']<0 and signs['box_excess']<0) if not event else None}

def quotient2(p,q):
    out=[]
    for n in range(3):
        out.append((p[n]-sum(q[j]*out[n-j] for j in range(1,n+1)))/q[0])
    return out

def exact_schur_fixtures(ev):
    # f1(z)=(b+gamma*z)/(1+b*gamma*z); f=(a+z*f1)/(1+a*z*f1).
    # The rational Taylor calculation below is independent of the cover code.
    eta=F(3,7);radius=F(1,2);rows=ev.schur_residual_cover(A(eta))
    fixtures=[]
    params=[(-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1),
            (0,0,-1),(0,0,1),(F(1,2),F(1,3),-1),
            (F(1,2),F(1,3),1),(F(-1,2),F(2,3),-1),
            (F(-1,2),F(2,3),1),(0,1,-1),(0,-1,1)]
    for av,bv,gv in params:
        a,b,g=map(F,(av,bv,gv))
        # Combining the two rational linear-fractional maps gives:
        coeff=quotient2([a,a*b*g+b,g],[F(1),b*g+a*b,a*g])
        expected=[eta*coeff[0],eta*coeff[1]/radius,2*eta*coeff[2]/radius**2]
        formula=[eta*a,2*eta*(1-a*a)*b,
                 8*eta*(1-a*a)*((1-b*b)*g-a*b*b)]
        check(expected==formula,'rational Schur coefficient identity')
        ia=min(7,max(0,int(4*(a+1))));ib=min(7,max(0,int(4*(b+1))))
        cover=rows[8*ia+ib]
        check(all(ball.contains(A(value)) for ball,value in zip(cover,expected)),
              'Schur cell omits exact rational jet')
        fixtures.append({'alpha':str(a),'beta':str(b),'gamma':str(g),
                         'eta':str(eta),'radius':str(radius),
                         'exact_local_jets':[str(v) for v in expected],
                         'cover_cell':[ia,ib],'covered':True})
    # Concrete second-jet mutations fail against exact realizable rational maps.
    a,b,g=F(0),F(0),F(1)
    actual=8*eta*(1-a*a)*((1-b*b)*g-a*b*b)
    half=4*eta*(1-a*a)*((1-b*b)*g-a*b*b)
    check(actual!=half,'factor-eight mutation fixture ineffective')
    a,b,g=F(1,2),F(1,3),F(1)
    actual=8*eta*(1-a*a)*((1-b*b)*g-a*b*b)
    omitted=8*eta*(1-a*a)*((1-b*b)*g)
    check(actual!=omitted,'alpha beta-square mutation fixture ineffective')
    # Gamma=+/-1 must both remain admitted by the exact real Schur body.
    lo=8*eta*(1-a*a)*(-(1-b*b)-a*b*b)
    hi=8*eta*(1-a*a)*((1-b*b)-a*b*b)
    check(lo<hi,'gamma extreme interval collapsed')
    return {'parameter_domain':'alpha,beta,gamma all real in [-1,1]',
            'eta':str(eta),'disk_radius':str(radius),
            'exact_fixtures':fixtures,
            'mutations_detected':[
                {'mutation':'second-derivative factor 8 replaced by 4',
                 'exact':str(8*eta),'mutated':str(4*eta)},
                {'mutation':'omit -alpha*beta^2 in second Schur coefficient',
                 'exact':str(actual),'mutated':str(omitted)},
                {'mutation':'collapse gamma interval to a single endpoint',
                 'gamma_minus_one':str(lo),'gamma_plus_one':str(hi)}],
            'scope':'Exact rational fixture checks of coefficient normalization and cover inclusion; not a completeness proof.'}

def diagonal_point_fixture(ev,repo):
    evaluator=ev.ClosedJetEvaluator(repo,192)
    x=arb(1000);t=arb(1)/10;data=evaluator.jets(x,t)
    z=acb_series([acb(x),acb(1)],3)
    C=-evaluator.old.W_real(z,t)*evaluator.old.J(z,t,8)[0]
    c=C[0].real;cp=C[1].real;cpp=2*C[2].real
    u=data['u'];h=data['h'];bp=data['b_x']
    check((cp+h*c-u).contains(0),'independent correction derivative identity')
    f0prime=data['full'][1]
    f1prime=data['full'][2]+cpp+bp*c+h*cp
    r0=f0prime-data['frozen'][1]+u
    r1=f1prime-data['frozen'][2]-h*u
    check(r0.contains(0) and r1.contains(0),'frozen diagonal propagation defect identity')
    check(u.abs_lower()>0,'diagonal correction defect fixture is vacuous')
    return {'x':'1000','t':'1/10','bits':192,
            'correction_derivatives_obtained_by':'Acb power series of -W_real(z,t)*J(z,t,8)',
            'profile_derivative_u':display(u),
            'd_f0_minus_f1_plus_u':display(r0),
            'd_f1_minus_f2_minus_h_u':display(r1),
            'residuals_contain_zero':True,'nonzero_u_certified':True,
            'identities':['d_x frozen0 = frozen1-u','d_x frozen1 = frozen2+h*u'],
            'scope':'Point fixture only; supports the explicitly paid diagonal correction in closed-cell propagation.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--evaluator-script',type=Path,required=True)
    parser.add_argument('--work-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--execution-model',required=True)
    parser.add_argument('--execution-effort',required=True)
    args=parser.parse_args();started=time.monotonic()
    repo=args.repo.resolve();work=args.work_dir.resolve();work.mkdir(parents=True,exist_ok=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    source_record=work/'S01_SOURCE_SPECIFIC_CONTROLS.json'
    completed=subprocess.run([sys.executable,str(repo/S01),'--repo',str(repo),
        '--work-dir',str(work),'--output',str(source_record),
        '--execution-model',args.execution_model,'--execution-effort',args.execution_effort],
        check=True,capture_output=True,text=True,timeout=180)
    source=json.loads(source_record.read_text())
    check(source['status']=='pass' and source['precision_bits']==192,'fresh source replay status')
    check(source['review_script_sha256']==digest(repo/S01),'fresh S01 producer pin')
    for row in source['source_pins']:check(digest(repo/row['path'])==row['sha256'],'source pin '+row['path'])
    for row in source['fresh_receipt_identities'].values():
        check(digest(work/'receipts'/row['file'])==row['sha256'],'fresh receipt pin')
    ctx.prec=192;ev=load(args.evaluator_script)
    outcomes=[source_challenge(ev,row,i<5) for i,row in enumerate(source['downstream_outcomes'])]
    check(len(outcomes)==6,'five events plus one Euler witness required')
    schur=exact_schur_fixtures(ev)
    diagonal=diagonal_point_fixture(ev,repo)
    record={'schema':'s02-complete-jet-controls-v1','date':'2026-10-19',
        'timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':args.execution_model,'actual_effort':args.execution_effort,
        'llm_assistance':'substantial; same-model internal replay',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'precision_bits':192,'status':'pass',
        'scope':'New S02 helpers reject all five fresh source-specific collisions; Euler Laguerre and excess remain strictly negative. Exact Schur normalization fixtures and pointwise diagonal correction check. No source theorem, theta bound, collision-free coverage or global conclusion added.',
        'ball_transport':'Fresh source-specific complete event balls re-enclosed from Arb display strings; no assertion of exact dyadic identity. eta=0 because complete source jets already include source errors.',
        'evaluator_sha256':digest(args.evaluator_script),'script_sha256':digest(__file__),
        'S01_control_producer':{'path':str(S01),'sha256':digest(repo/S01)},
        'fresh_source_record':{'filename':source_record.name,'sha256':digest(source_record),
                               'external_work_dir':str(work)},
        'source_pins':source['source_pins'],
        'fresh_receipt_identities':source['fresh_receipt_identities'],
        'analytic_premise_screen':source['analytic_premise_screen'],
        'downstream_outcomes':outcomes,'exact_real_Schur_fixtures':schur,
        'frozen_diagonal_point_fixture':diagonal,'seconds':time.monotonic()-started}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'sha256':digest(args.output),
        'evaluator_sha256':record['evaluator_sha256'],'events_rejected':5,
        'Euler_strict_negative':True,'exact_Schur_fixtures':len(schur['exact_fixtures']),
        'diagonal_identity_pass':True,'bytes':args.output.stat().st_size,
        'seconds':record['seconds']}))

if __name__=='__main__':main()
