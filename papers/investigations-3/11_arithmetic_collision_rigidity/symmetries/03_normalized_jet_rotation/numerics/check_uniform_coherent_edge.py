#!/usr/bin/env python3
"""Outward constants for UAR-03's uniform edge and matching proof.

Prepared for Edward Baker with substantial LLM assistance, 19 October 2026.
Checks analytic majorants and exact fixtures; no retained-model quadrature,
complete signed increment, physical acceptance or cost claim is performed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys
sys.dont_write_bytecode=True
import flint
from flint import arb,ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/03_normalized_jet_rotation'
NOTE=LANE/'notes/09_UNIFORM_COHERENT_EDGE_AND_CUTOFF_MATCHING_20261019.md'
SCRIPT=LANE/'numerics/check_uniform_coherent_edge.py'
OLD=Path('papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md')
SOURCES=[NOTE,SCRIPT,OLD,
    INV/'symmetries/notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md',
    LANE/'notes/08_UNIFORM_FINITE_GAMMA_HEAT_REMAINDER_20261019.md',
    LANE/'numerics/UAR02_UNIFORM_FINITE_GAMMA_HEAT_20261019.json',
    LANE/'notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md',
    INV/'symmetries/04_time_height_scaling/notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md',
    LANE/'numerics/UAR03_SOURCE_CONTROLS_20261019.json',
    INV/'numerics/replay_nonstationary_controls.py',
    Path('result-summaries/12_collision_controls_and_screening.md')]

def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def out(v):return v.str(38,more=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(ok,msg):
    if not ok:raise ArithmeticError(msg)

def sector(t,kappa):
    check(isinstance(t,F) and isinstance(kappa,F),'exact sector parameters required')
    check(0<t<=F(1,20) and 1<=kappa<=2,'sector outside proof')
    return kappa/t

def pins_valid(repo,pins):
    check(set(pins)=={str(p)for p in SOURCES},'missing/extra source pin')
    for name,digest in pins.items():
        p=repo/name
        check(p.is_file() and not p.is_symlink(),'missing/linked source: '+name)
        check(sha(p)==digest,'stale source: '+name)

def reject(call):
    try:call()
    except ArithmeticError:return
    raise ArithmeticError('invalid fixture accepted')

def exact_guards():
    for t,k in [(F(1,20),F(1)),(F(1,20),F(2)),(F(1,100),F(3,2))]:
        check(sector(t,k)>=20,'minimum L')
        # Global limits V²=S²=8/t exceed 4L, independent of chart center.
        check(8/t>=4*sector(t,k),'global truncation covers local budget')
    bad=[(F(0),F(1)),(F(-1),F(1)),(F(1,19),F(1)),
         (F(1,20),F(1,2)),(F(1,20),F(3)),(.05,F(1))]
    for t,k in bad:reject(lambda t=t,k=k:sector(t,k))
    # Right descending contour minus left descending contour closes clockwise.
    polygon=[(F(2),F(1)),(F(0),F(-1)),(F(-1),F(-1)),(F(1),F(1))]
    area2=sum(x*polygon[(j+1)%4][1]-y*polygon[(j+1)%4][0]
              for j,(x,y) in enumerate(polygon))
    check(area2<0,'descending contour residue sign')
    check((-area2)>0,'reversed contour mutation')
    for n in [1,2,8,9,22026,22027]:
        check((-1)**(n*n-n)==1,'kernel residue parity')
    for v_inside in [False,True]:
        for r_inside in [False,True]:
            gaussian=not v_inside;contour=v_inside and not r_inside
            check((gaussian or contour)==(not(v_inside and r_inside)),'rectangle complement coverage')
            check(not(gaussian and contour),'rectangle complement disjointness')
    old,m,eold,enew=F(5),F(3),F(1,10),F(1,5)
    new=old-m;bold=old-eold;bnew=new-enew
    check(m+bnew-bold==-(enew-eold),'exact heat edge compensation')
    check(-m+bnew-bold!=-(enew-eold),'residue sign mutation')
    return {'invalid_sector_inputs_rejected':len(bad),'global_t_only_limits_cover_all_charts':True,
        'descending_residue_clockwise_area2':str(area2),'kernel_integer_residue_parity':'exact',
        'rectangle_complement_disjoint_and_complete':True,'exact_heat_mode_compensation':True,
        'opposite_residue_sign_mutation_rejected':True}

def scalar_checks(bits):
    ctx.prec=bits;pi=arb.pi();L=A(20);t=A(F(1,20));R=1/L
    c=4*pi*L.exp();C=A(10)**9;T=A(3)*10**9;q=A(22025);dist=A('.500001')
    vals={};flags={}
    def lt(name,v,cap):
        v=A(v)
        vals[name]={'value':out(v),'upper_cap':str(cap)};flags[name]=bool(v<A(cap))
    def gt(name,v,cap):
        v=A(v)
        vals[name]={'value':out(v),'lower_floor':str(cap)};flags[name]=bool(v>A(cap))
    gt('opening_height',c,6*10**9)
    gt('contour_q_from_sector',A(10).exp()-1,22025)
    lt('natural_a_variation',R/(4*pi*(A(10).exp()-1)),'2e-7')
    delta=-(1-dist/q).log()
    lt('log_contour_radius_ratio',delta,'.000024')
    phaseD=2*pi*dist*(2+dist/q)
    lt('contour_phase_constant',phaseD**2/(4*pi),4)
    lt('negative_contour_branch_ratio',(1+dist/(q-dist))**2/pi,1)
    lt('gamma_reflection_log_remainder',1/(2*T),'2e-10')
    gt('gamma_reflection_log_reserve',pi*T-(12*T).log(),0)
    lt('global_linear_u',delta+3/(2*T),'.000025')
    lt('global_quadratic_u',1/(pi*q*q)+1/(4*(T-3)),'1e-9')
    lt('gaussian_u_constant',A('.000025')*A('.525')+2*A('1e-9')*A('.525')**2,'.000014')
    lt('gaussian_linear_v',A('.000025')*t.sqrt(),'.000006')
    lt('gaussian_majorant_coefficient',A(2).sqrt()*(4+A('2e-10')+A('.000014')).exp(),78)
    lt('weakened_gaussian_exponent_loss',A('4e-10')+A('12e-6')/L.sqrt(),'.01')
    amin=1-A('1e-10');vmin=2*L.sqrt();b=A('.000006')
    lt('gaussian_Mills_prefactor',156/(pi.sqrt()*(2*amin*vmin-b)),100)
    lt('retained_central_abs_u',A('.525')+2*A(2).sqrt(),4)
    lt('contour_tail_linear_coefficient',8/q,'.001')
    gt('contour_tail_quadratic_reserve',(pi-3)*vmin-A('.001'),0)
    ctail=(A(2).sqrt()*(4+4*A('.000024')+1/(2*T)+6/T+4/(T-3)).exp()/(6*vmin))
    lt('contour_tail_prefactor',ctail,50)
    lt('real_prefactor_Z_ratio',((3*L+10)/(A('.99')*c)).exp(),'1.001')
    lt('normalizer_vertical_cost',(A('.25')+A('.501')/20).exp(),'1.4')
    lt('per_channel_normalized_prefactor',A('1.001')*A('1.4'),2)
    lt('complete_edge_coefficient',4*(100+50),1000)
    lt('edge_rotating_Cauchy_coefficient',(1+A('8.002')**2).sqrt(),9)
    # Scaled quantities for inherited matching exponent: E=ec/c etc.
    ec=A('.025001');d0=A('3.000001');d1=A('1.000001');de=A('.526');ds=A('3.526002')
    n=(C/(4*pi)+t/16).sqrt();am=(n*n-R/(4*pi)).sqrt()
    d=R/(4*pi*(n+am));taumin=(C-R)/2+pi*t/8;Tmin=(C-R)/2
    lt('matching_E_geometry_scaled',C*d/am,'.025001')
    lt('matching_D0_geometry_scaled',C*3/(2*taumin),'3.000001')
    lt('matching_D1_geometry_scaled',C*(1/(2*Tmin)+A('1.5')/Tmin**2),'1.000001')
    lt('matching_Delta_geometry',(A('.525')**2+(pi*t/8)**2).sqrt(),'.526')
    lt('analytic_jump_a_ratio_scaled',C*d/am,'.0251')
    lt('analytic_jump_phase_loss',2*pi*d*d,'1e-11')
    gt('analytic_jump_tau_modulus_ratio',A('.5')-R/(2*C),'.499999')
    lt('matching_Ds_scaled',d0+de*d1,'3.526002')
    phase=2*pi/3*(ec/C)**3*(C/(4*pi)+t/16)*C
    lam=(A('.525')*ec+t*ec*ec/(4*C)+phase+de*d0+de*de*d1/2
         +t/4*(2*(ec/C+pi/4)*ds+ds*ds/C))
    lt('matching_Lambda_scaled',lam,'1.81')
    lt('printed_jump_mismatch_scaled',2*A('1.81')*(A('1.81')/C).exp(),'3.621')
    lt('jump_psi_derivative_scaled',A('.0251')/2,'.0126')
    trig=A('1e-11').cosh();tau=A('.499999')
    bracket=3/(4*tau)*(trig+trig/(tau*C))+(trig+trig/(tau*C))*A('.0126')+trig/(2*tau*tau*C)
    lt('analytic_jump_slow_derivative_scaled',bracket,'1.52')
    lt('jump_vertical_amplitude_ratio',(1+(R/(2*A('.499999')*C))**2)**A(F(3,4)),'1.000001')
    lt('printed_to_analytic_jump_payment',2*R*A('1.52')*A('1.000001'),'.16')
    lt('combined_jump_physical_mismatch',A('3.621')+A('.16'),'3.8')
    lt('normalized_coherent_jump_coefficient',2*A('3.8'),8)
    gt('crossing_c_over_n_squared',4*pi*(1-t/(16*q*q)),12)
    lt('crossing_rotating_n_squared_coefficient',A('32.008')/12,3)
    lt('transition_sum_prefactor',3/(1-(-A(10)).exp()),'3.01')
    edge=1000*(-A('86.05')).exp();rot=9*edge
    transition=A('3.01')*(-A('16.25')).exp()
    lt('opening_edge_error_ceiling',edge,'4.3e-35')
    lt('opening_edge_rotating_ceiling',rot,'3.9e-34')
    lt('opening_transition_prefix_ceiling',transition,'2.639e-7')
    check(all(flags.values()),'outward proof constant failed: '+str([k for k,v in flags.items() if not v]))
    return {'bits':bits,'all_checks_passed':True,'values':vals,'checks':flags,
        'opening_allowances':{'edge_model_error':out(edge),'edge_first_x_error':out(2*L*edge),
            'edge_rotating_error':out(rot),'corrected_transition_prefix':out(transition)},
        'scope':'Elementary reserves for written uniform proof, not sampled coverage or retained-model quadrature.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',required=True,type=Path)
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--output',type=Path);g.add_argument('--verify',type=Path)
    p.add_argument('--bits',type=int,nargs='+',default=[192,256]);p.add_argument('--execution-model');p.add_argument('--execution-effort')
    a=p.parse_args();repo=a.repo.resolve();guards=exact_guards()
    if a.verify:
        saved=json.loads(a.verify.read_text());pins_valid(repo,saved['source_sha256'])
        check(saved['scope']=='uniform_edge_model_error_and_corrected_transition_only','wrong source scope')
        check(saved['exact_guards']==guards,'guard replay differs')
        fresh=[scalar_checks(r['bits'])for r in saved['runs']]
        check(fresh==saved['runs'],'scalar replay differs; assess environment before replacing receipt')
        print(json.dumps({'status':'verified','bits':[r['bits']for r in fresh],'scope':saved['scope']}));return
    check(bool(a.execution_model)and bool(a.execution_effort),'actual execution provenance required')
    check(all(b>=128 for b in a.bits),'check precision too low')
    pins={str(v):sha(repo/v)for v in SOURCES};pins_valid(repo,pins)
    reject(lambda:pins_valid(repo,{}));stale=dict(pins);stale[str(NOTE)]='0'*64
    reject(lambda:pins_valid(repo,stale));reject(lambda:pins_valid(repo/'absent_uar03_fixture',pins))
    record={'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':a.execution_model,'actual_effort':a.execution_effort,
        'llm_assistance':'substantial; separate same-model mathematical/source review',
        'scope':'uniform_edge_model_error_and_corrected_transition_only',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'rounding':'outward Arb scalar bounds and exact rational/combinatorial fixtures',
        'source_sha256':pins,'exact_guards':guards,
        'source_guards':{'missing_pins_rejected':True,'stale_pin_rejected':True,'missing_files_rejected':True},
        'primary_sources':['https://arxiv.org/html/1904.12438v2#S4','https://dlmf.nist.gov/5.11#ii','https://dlmf.nist.gov/5.5#E3'],
        'runs':[scalar_checks(b)for b in a.bits],
        'limitations':['No retained bounded-contour quadrature or model endpoint evaluation.',
            'No complete signed residual increment, physical anchor or collision exclusion.',
            'Exact fixtures and outward constants support the written proof; they do not independently prove it.',
            'Same-model/checker replay is not implementation independent or specialist human review.']}
    a.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'written','output':str(a.output),'bits':a.bits,'scope':record['scope']}))

if __name__=='__main__':main()
