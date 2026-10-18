#!/usr/bin/env python3
"""Matched pilot, source-specific controls and bounded signed estimate.

Prepared for Edward Baker with substantial LLM assistance, 18 October 2026.
Authoring: gpt-6.1-sol, actual effort max. Same-model internal computation.
Requires python-flint 0.9.0 and the explicitly supplied replay receipts.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

import flint
from flint import arb, acb, ctx
from certify_shifted_theta_jet import Evaluator,A,rec,check,coordinate_separator,laguerre_excess,square


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_receipt(folder, filename, source, expected_sha256):
    path=folder/filename
    check(digest(path)==expected_sha256,'control receipt bytes do not match fresh replay')
    data=json.loads(path.read_text())
    recorded=data.get('checker_sha256',data.get('checker',{}).get('sha256') if isinstance(data.get('checker'),dict) else None)
    check(recorded==digest(source),'control source hash differs from replay receipt')
    return data,{'file':filename,'sha256':digest(path),'source_sha256':digest(source)}


def rejection(name,jets,domain):
    check(jets[0].contains(0) and jets[1].contains(0),name+' event not enclosed')
    check(coordinate_separator(jets) is None,name+' passed a strict coordinate margin')
    excess=laguerre_excess(jets,F(1,100))
    check(not excess>0,name+' passed the strict signed margin')
    return {'control':name,'event_domain':domain,'event_jet_enclosures':[rec(v) for v in jets],
            'strict_first_jet_rejected':True,'strict_signed_margin_rejected':True,
            'signed_excess':rec(excess),'theta_error_constants_used':False}


def finite_square_moment(weights,T):
    # Uniform positive absolute source moments through order 4 at times <=T.
    # On [0,1], u^j<=1 and int phi_n=(4lambda-1)e^-lambda/8.
    pi=arb.pi();e4=arb(4).exp()
    mass=arb(0)
    for n,weight in weights.items():
        lam=pi*n*n
        denominator=4*lam*e4-13-2*T
        check(denominator>0,'square-control source tail failed')
        mass += weight*((4*lam-1)*T.exp()/8+2*lam*lam*(T+9+lam-lam*e4).exp()/denominator)
    return mass.upper()


def replay_controls(repo,folder):
    folder.mkdir(parents=True,exist_ok=True)
    root=repo/'papers/investigations-2/active'
    sources={
        'THREE_SQUARE_REPLAY.json':root/'22_theta_manifold_geometry/numerics/certify_square_support_endpoint_collision.py',
        'FOUR_SQUARE_REPLAY.json':root/'22_theta_manifold_geometry/numerics/check_theta_two_endpoint_control.py',
        'REFLECTED_CONTROL_REPLAY.json':root/'22_theta_manifold_geometry/numerics/check_theta_center_separation.py',
        'EULER_FACTOR_REPLAY.json':root/'19_euler_factor_controls/numerics/certify_euler_factor_witness.py'}
    expected={}
    for filename,source in sources.items():
        subprocess.run([sys.executable,str(source),'--output',str(folder/filename)],
                       check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
        expected[filename]=digest(folder/filename)
    return expected


def control_screen(repo,folder,expected):
    root=repo/'papers/investigations-2/active'
    three,three_id=load_receipt(folder,'THREE_SQUARE_REPLAY.json',root/'22_theta_manifold_geometry/numerics/certify_square_support_endpoint_collision.py',expected['THREE_SQUARE_REPLAY.json'])
    four,four_id=load_receipt(folder,'FOUR_SQUARE_REPLAY.json',root/'22_theta_manifold_geometry/numerics/check_theta_two_endpoint_control.py',expected['FOUR_SQUARE_REPLAY.json'])
    reflected,reflected_id=load_receipt(folder,'REFLECTED_CONTROL_REPLAY.json',root/'22_theta_manifold_geometry/numerics/check_theta_center_separation.py',expected['REFLECTED_CONTROL_REPLAY.json'])
    euler,euler_id=load_receipt(folder,'EULER_FACTOR_REPLAY.json',root/'19_euler_factor_controls/numerics/certify_euler_factor_witness.py',expected['EULER_FACTOR_REPLAY.json'])
    events=[];eps=arb('1e-8')
    center=three['integrals'][12:21]
    moments=three['integrals'][21:30]
    radius=(A(F(three['x_bracket_exact_decimal'][1]))-A(F(three['x_bracket_exact_decimal'][0])))/2
    boxes=[]
    for n in range(3):
        jets=[arb(center[3*n+k]['value_with_complete_tail']) for k in range(3)]
        mm=[arb(moments[3*n+k]['value_with_complete_tail']).abs_upper() for k in range(3)]
        derivatives=[jets[1].abs_upper()+radius*mm[1],jets[2].abs_upper()+radius*mm[2],mm[2]]
        boxes.append([jets[k]+arb(0,(radius*derivatives[k]).upper()) for k in range(3)])
    b2,b3,theta=map(arb,(three['b2'],three['b3'],three['theta_enclosure']))
    vv={1:arb(1),2:theta*b2,3:(1-theta)*b3}
    aa=[boxes[0][k]+b3*boxes[2][k] for k in range(3)]
    bb=[b2*boxes[1][k]-b3*boxes[2][k] for k in range(3)]
    allowance=(eps*finite_square_moment(vv,arb(1)/4+eps)).upper()
    jets=[aa[k]+theta*bb[k]+arb(0,allowance) for k in range(3)]
    events.append(rejection('three-square fixed-coefficient event',jets,
                  {'t':['0.24999999','0.25000001'],'x':three['x_bracket_exact_decimal']}))
    cert=four['collision_certificate'];q=arb(cert['q_enclosure'])
    jets=[q*arb(cert['vertex_boxes']['3'][str(k)])+(1-q)*arb(cert['vertex_boxes']['4'][str(k)]) for k in range(3)]
    vv={int(n):arb(value) for n,value in cert['scaled_mode_weights_v'].items()}
    allowance=(eps*finite_square_moment(vv,arb(1)/100+eps)).upper()
    jets=[v+arb(0,allowance) for v in jets]
    events.append(rejection('four-square fixed-coefficient event',jets,
                  {'t':['0.00999999','0.01000001'],'x':cert['x_bracket_exact_decimal']}))
    # A surrounding box, not just the exact event: spatial errors use source
    # moments; the time halo uses H_t=-H_xx and positive source moments.
    pi=arb.pi();X=pi/4+arb(0,eps);c=arb(reflected['source_scale_c'])
    M=[(arb(k+1)/4).gamma()/4 for k in range(5)]
    f0=arb(reflected['F_at_collision'])+arb(0,(eps*M[1]).upper())
    f1,f2=arb(0,M[1].upper()),arb(0,M[2].upper())
    factor=1+(4*X).cos();first=-4*(4*X).sin();second=-16*(4*X).cos()
    jets=[c*f0*factor,c*(f1*factor+f0*first),c*(f2*factor+2*f1*first+f0*second)]
    for j in range(3):
        k=j+2
        positive_moment=M[k]+sum((__import__('math').comb(k,l)*4**(k-l)*M[l] for l in range(k+1)),arb(0))
        tail=2*8**k*(64*eps-256).exp()/(128-16*eps-arb(k)/8)
        paid=eps*c*((64*eps).exp()*positive_moment+tail)
        jets[j]+=arb(0,paid.upper())
    events.append(rejection('reflected super-Gaussian event',jets,
                  {'t':['0.24999999','0.25000001'],'x':'pi/4 +/- 1e-8'}))
    # The q_{T,a} contract gives J_T=B cos^2(az), B=2int e^-cosh(u)cos(xu)du.
    # Select a=pi/2 and x*=1; B(1)>0 is checked by complete quadrature.
    bjet=[];mom=[]
    for k in range(4):
        def integrand(u,analytic):
            phase=(u.cos(),-u.sin(),-u.cos(),u.sin())[k%4]
            return (-u.cosh()).exp()*u**k*phase
        finite=acb.integral(integrand,0,6,abs_tol=arb('1e-35'),rel_tol=arb('1e-28'))
        tail=6**k*(-arb(6).cosh()).exp()/(arb(6).sinh()-arb(k)/6)
        bjet.append(2*(finite.real+arb(0,tail.upper())))
        positive=acb.integral(lambda u,analytic:(-u.cosh()).exp()*u**k,0,6,
                              abs_tol=arb('1e-35'),rel_tol=arb('1e-28'))
        mom.append((2*(positive.real+tail)).upper())
    check(bjet[0]>0,'qTa selected Bessel carrier could vanish')
    bx=[bjet[j]+arb(0,(eps*mom[j+1]).upper()) for j in range(3)]
    x=arb(1,eps);a=pi/2
    factor=square((a*x).cos());first=-a*(2*a*x).sin();second=-2*a*a*(2*a*x).cos()
    jets=[bx[0]*factor,bx[1]*factor+bx[0]*first,bx[2]*factor+2*bx[1]*first+bx[0]*second]
    for j in range(3):
        k=j+2
        def positive(u,analytic):
            p=(-u.cosh()).exp()/2+(-(u-2*a).cosh()).exp()/4+(-(u+2*a).cosh()).exp()/4
            return (eps*u*u).exp()*u**k*p
        integral=sum((acb.integral(positive,left,left+2,abs_tol=arb('1e-30'),rel_tol=arb('1e-25'),
                                  eval_limit=200000,depth_limit=30) for left in range(0,10,2)),acb(0))
        check(integral.is_finite() and integral.imag.contains(0),'qTa source-moment quadrature failed')
        denominator=(10-2*a).sinh()-20*eps-arb(k)/10
        check(denominator>0,'qTa moment tail failed')
        tail=10**k*(100*eps-(10-2*a).cosh()).exp()/denominator
        jets[j]+=arb(0,(2*eps*(integral.real+tail)).upper())
    events.append(rejection('qTa exact-threshold family event',jets,
                  {'t':['0.24999999','0.25000001'],'x':['0.99999999','1.00000001'],'a':'pi/2'}))
    events.append(rejection('polynomial backward-heat event',
                  [arb(0,arb('3e-8')),arb(0,arb('2e-8')),arb(2)],
                  {'t':['0.24999999','0.25000001'],'x':['-1e-8','1e-8'],'field':'x^2-2(t-1/4)'}))
    ej=[arb(row['full_jet']['display']) for row in euler['jets']]
    check(laguerre_excess(ej,F(1,100))<0,'genuine Euler negative-Laguerre witness not rejected')
    analytic=[
        {'control':'finite-prime orbit','outcome':'theta premise fails','missing_premise':'complete normalized analytic reflection','numerical_event_test':'not attempted: theorem gives no effective event height'},
        {'control':'three/four square','outcome':'theta premise fails and enclosed event rejected','missing_premise':'complete reflection and unchanged complete coefficients'},
        {'control':'reflected super-Gaussian','outcome':'theta premise fails and enclosed event rejected','missing_premise':'exact normalized theta integer-square source expansion'},
        {'control':'smooth shape and positive primitive','outcome':'theta premise fails; analytic witness retained','missing_premise':'theta square-mode data','numerical_event_test':'not attempted: no certified damping/event box supplied'},
        {'control':'Euler factors','outcome':'genuine negative-Laguerre witness rejected','missing_premise':'unchanged normalized theta coefficients and level','numerical_event_test':'witness is not a double-event enclosure'},
        {'control':'q and qTa','outcome':'theta premise fails; applicable qTa event enclosed and rejected','missing_premise':'exact theta square-source expansion','q_only_status':'proved positive threshold; no event location inferred'},
        {'control':'smooth-density and two-channel','outcome':'no extension of the theta signed certificate to these classes','missing_premise':'the evaluated complete theta source; generic auxiliary positivity does not supply the signed estimate'}]
    return {'event_rejections':events,'euler_witness':{'parameters':euler['parameters'],'L0':euler['raw_laguerre_L0'],
            'strict_signed_margin_rejected':True,'label':'negative-Laguerre witness, not an enclosed event'},
            'analytic_premise_screen':analytic,'receipt_identities':{'three_square':three_id,'four_square':four_id,'reflected':reflected_id,'euler':euler_id}}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True);p.add_argument('--receipts',type=Path,required=True)
    p.add_argument('--validation',type=Path,required=True);p.add_argument('--declaration',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--signed-output',type=Path,required=True)
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    args=p.parse_args();ctx.prec=160;start=time.monotonic()
    declaration=json.loads(args.declaration.read_text());validation=json.loads(args.validation.read_text())
    evaluator_source=Path(__file__).with_name('certify_shifted_theta_jet.py')
    check(validation['script_sha256']==digest(evaluator_source),'evaluator source differs from validation')
    pilot_costs={name:validation['methods'][name]['construction_seconds']+validation['pilot'][name]['timing_seconds'] for name in ('real','shifted')}
    adjoining={};adjoining_manifests={}
    for name in ('real','shifted'):
        evaluator=Evaluator(name,xlo=F(45),xhi=F(65))
        result=evaluator.pilot(seconds_limit=10)
        check(evaluator.construction_seconds+result['timing_seconds']<10,'adjoining resource budget exceeded')
        adjoining[name]=result;adjoining_manifests[name]=evaluator.manifest()
    margin_gain=arb(adjoining['shifted']['minimum_margin_lower'])/arb(adjoining['real']['minimum_margin_lower'])
    speed_gain=pilot_costs['real']/pilot_costs['shifted']
    performance_pass=speed_gain>=2 or bool(margin_gain>=arb('1.1'))
    expected=replay_controls(args.repo,args.receipts)
    controls=control_screen(args.repo,args.receipts,expected)
    meta={'date':'2026-10-18','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance; same-model internal interval computation.',
          'execution_model':args.execution_model,'execution_effort':args.execution_effort,
          'python':platform.python_version(),'python_flint':flint.__version__,
          'script_sha256':digest(Path(__file__)),'evaluator_sha256':digest(evaluator_source)}
    output={**meta,'predeclaration':declaration,'predeclaration_sha256':digest(args.declaration),'validation_sha256':digest(args.validation),
            'pilot_total_cost_seconds':pilot_costs,'pilot_speed_gain_real_over_shifted':speed_gain,
            'adjoining_results':adjoining,'adjoining_manifests':adjoining_manifests,'adjoining_minimum_margin_ratio':rec(margin_gain),
            'performance_gate_passed':performance_pass,'validation_gate_passed':True,'control_screen':controls,
            'decision':'No scan expansion: validation and error reduction are retained; neither predeclared performance/coverage gate passed.' if not performance_pass else 'Performance gate passed only for the stated bounded comparison.',
            'comparison_scope':'One measured run; same exact rectangle, output conclusion, tolerances, precision and 77 midpoint derivatives. Shifted moment majorants, rejects and precomputation are charged. No optimality claim.',
            'control_implementation_repair':{'failed_attempt':'The qTa control cosine interval is centred on zero. Native arb ** 2 in python-flint 0.9.0 returned NaN there; the finite-jet guard stopped the run. Direct diagnostics found the Bessel and source-moment integrals finite.',
                                             'bounded_repair':'Use the explicit outward real square range in both the shared signed interface and qTa factor. Source-moment integration also has explicit finite checks and five length-two subintervals. No failed control was accepted.'}}
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    evaluator=Evaluator('shifted')
    signed=evaluator.pilot(signed_constant=F(1,100),max_depth=16)
    signed_record={**meta,'evaluator_manifest':evaluator.manifest(),'predeclaration_sha256':digest(args.declaration),
                   'candidate':'H_x^2-H H_xx > (H^2+H_x^2)/100 on the exact D0 rectangle',
                   'classification':'quantitative finite-domain signed certificate on previously covered territory, not a global arithmetic sign mechanism',
                   'certificate':signed,'scope':'No new collision-free coverage or global Newman conclusion; the complete-source analytic mechanism remains open.'}
    args.signed_output.write_text(json.dumps(signed_record,indent=2)+'\n')
    print(json.dumps({'performance_gate_passed':performance_pass,'speed_gain':speed_gain,'adjoining_margin_ratio':rec(margin_gain),
                      'enclosed_event_boxes_rejected':len(controls['event_rejections']),'signed_strips':signed['accepted_strips'],
                      'signed_minimum_excess_lower':signed['minimum_margin_lower'],'seconds':time.monotonic()-start},indent=2))


if __name__=='__main__':main()
