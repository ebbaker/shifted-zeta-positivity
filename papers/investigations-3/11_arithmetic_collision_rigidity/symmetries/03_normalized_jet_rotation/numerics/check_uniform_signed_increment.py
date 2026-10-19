#!/usr/bin/env python3
"""Outward constants and exact guards for the written UAR-04 theorem.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual execution provenance is required. No H acquisition or quadrature.
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
NOTE=LANE/'notes/10_UNIFORM_SIGNED_RESIDUAL_INCREMENT_20261019.md'
SCRIPT=LANE/'numerics/check_uniform_signed_increment.py'
OLD=Path('papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes')
SOURCES=[NOTE,SCRIPT,
    INV/'symmetries/notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md',
    LANE/'notes/08_UNIFORM_FINITE_GAMMA_HEAT_REMAINDER_20261019.md',
    LANE/'notes/09_UNIFORM_COHERENT_EDGE_AND_CUTOFF_MATCHING_20261019.md',
    LANE/'numerics/UAR02_UNIFORM_FINITE_GAMMA_HEAT_20261019.json',
    LANE/'numerics/UAR03_UNIFORM_COHERENT_EDGE_20261019.json',
    OLD/'20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md',
    OLD/'22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md',
    LANE/'numerics/UAR04_SOURCE_CONTROLS_20261019.json',
    INV/'numerics/replay_nonstationary_controls.py',
    Path('result-summaries/12_collision_controls_and_screening.md')]

def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def out(v):return v.str(38,more=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(ok,msg):
    if not ok:raise ArithmeticError(msg)
def sector(t,k):
    check(isinstance(t,F) and isinstance(k,F),'exact parameters required')
    check(0<t<=F(1,20) and 1<=k<=2,'outside proved sector')
    return k/t
def reject(call):
    try:call()
    except ArithmeticError:return
    raise ArithmeticError('invalid fixture accepted')
def pins_valid(repo,pins):
    check(set(pins)=={str(p)for p in SOURCES},'missing/extra source pins')
    for name,digest in pins.items():
        p=repo/name
        check(p.is_file() and not p.is_symlink(),'missing/linked source: '+name)
        check(sha(p)==digest,'stale source: '+name)

def exact_guards():
    for t,k in [(F(1,20),F(1)),(F(1,20),F(2)),(F(1,100),F(3,2))]:
        check(sector(t,k)>=20,'sector minimum')
    for t,k in [(F(0),F(1)),(F(1,19),F(1)),(F(1,20),F(3)),(.05,F(1))]:
        reject(lambda t=t,k=k:sector(t,k))
    for nu in [F(-1),F(-1,2),F(0),F(3,4),F(1)]:
        check(1+nu>=0 and 1-nu>=0,'frequency coefficients nonnegative')
        check((1+nu)+(1-nu)==2,'frequency weights retain sum two')
    # A switch subtracts h from r; ordinary integral returns +Z_h.
    ra,rb,h=F(5),F(2),F(3,7)
    left=rb+h
    piecewise=(left-ra)+(rb-(left-h))
    check(piecewise==rb-ra+h,'ordinary-prefix transition sign')
    check(piecewise!=rb-ra-h,'negative-sign mutation fails')
    # Exact shifted Gaussian moments E[v]=0, E[v^2]=1/2.
    sigma,t=F(5,8),F(1,20)
    check(sigma+0==sigma,'signed Gaussian first moment')
    check(sigma*sigma+t/2==F(133,320),'Gaussian second moment')
    check(F(12,7)>F(153,100),'prefix coefficient is endpoint-max direction')
    check(F(153,100)+F(12,7)+F(137,10**6)<F(3245,1000),'complete prefix coefficient')
    return {'invalid_sector_inputs_rejected':4,'frequency_weights_sum_to_two':True,
        'positive_transition_sign':True,'signed_heat_first_moment':True,
        'prefix_optimization_direction':True,'same_N_overlap_by_identical_definition':True}

def scalar_checks(bits):
    ctx.prec=bits;pi=arb.pi();L=A(20);t=A(F(1,20));c=4*pi*L.exp()
    rho=A('.25');a=((c-rho)/(4*pi)+t/16).sqrt();ascale=(L/2).exp();V=(8/t).sqrt();D=A('.50001')
    vals={};flags={}
    def lt(name,v,cap):
        vals[name]={'value':out(v),'upper_cap':str(cap)};flags[name]=bool(v<A(cap))
    def gt(name,v,cap):
        vals[name]={'value':out(v),'lower_floor':str(cap)};flags[name]=bool(v>A(cap))
    m0=A(2).sqrt()/4*(pi*D*D).exp()
    m2=1/(4*pi)+D*D/2
    m4=3/(16*pi*pi)+D*D/(4*pi)+D**4/4
    m6=15/(64*pi**3)+9*D*D/(32*pi*pi)+3*D**4/(16*pi)+D**6/8
    lt('Mordell_mass',m0,'.777')
    lt('Mordell_profile_derivative',2*pi*m0*m2.sqrt(),'2.22')
    lt('signed_heat_first_coefficient',m0*(A('.625')*m2.sqrt()+2*pi/3*(m2*m4).sqrt()),'.391')
    zmax=D+A(2).sqrt()*V
    lt('central_log_ratio',zmax/a,'.001')
    hmax=(4*zmax+2*pi/3*zmax**3)/(A('.999')*a)
    lt('central_exponent',hmax,'.65')
    h2=16*m2+16*pi/3*m4+4*pi*pi/9*m6
    hrem=m0*((2*m2+pi*m4/2)/A('.999')+A('.5')*A('.65').exp()*h2/A('.999')**2)
    lt('central_exponential_remainder',hrem,'3.57')
    T=2*pi*a*a
    lt('central_gamma_log_coefficient',a*a*(A('.5')/T+6/T+4/(T-3)),'1.7')
    expmass=m0*(1+(4*m2.sqrt()+2*pi/3*(m2*m4).sqrt())/(A('.999')*a)+A('.5')*A('.65').exp()*h2/(A('.999')*a)**2)
    lt('exponential_kernel_mass',expmass,'.777')
    lt('central_gamma_remainder',expmass*A('1.7')*(A('1.7')/a**2).exp(),'1.322')
    lt('central_total_remainder',hrem+expmass*A('1.7')*(A('1.7')/a**2).exp(),5)
    lt('signed_model_complement_scaled',2*(-4*L).exp()*a*a,1)
    lt('complex_d_geometry_slack',rho/(2*pi*(a-1)),'1e-5')
    lt('slow_normalizer_beta_difference',A('7.01')+A('1.051'),12)
    lt('symmetric_normalizer_log_derivative',pi/8+3/c,'.4')
    lt('real_prefactor_ratio',((3*L+10)/(A('.99')*c)).exp(),'1.001')
    lt('actual_complex_prefactor',A('1.001')*A('.1').exp(),'1.107')
    amin=((c-rho)/(4*pi)+t/16).sqrt();taumin=(c-rho)/2+pi*t/8
    J=3*A('.777')/(4*taumin)+A('.777')/taumin**2+(A('2.22')+A('2.22')/taumin)/(4*pi*amin)
    W=(((c+rho)/2+pi*t/8)/taumin)**A(F(3,2))
    conversion=2*A('1.000001')*rho*W*J*ascale
    lt('analytic_profile_conversion_scaled',conversion,'.0885')
    edge=A('1.107')*(2*A('.391')*ascale/a+12*ascale/a**2+conversion)
    lt('complete_edge_coefficient',edge,'.97')
    gt('enlarged_edge_rotating_radius',rho*L/A('4.001'),1)
    B=t/4+A('1.05')**2/8
    lt('finite_chi_coefficient',1/(6*A('.499'))+A('1.01')*B,'.5')
    chix=1/(12*A('.499')**2)+A('1.05')*B+A('1.01')**2*A('.0525')/8
    lt('finite_chi_first_x_coefficient',chix,'.5')
    lt('finite_slow_frequency_coefficient',A('1.01')*A('1.000001')/4,'.253')
    gt('finite_frequency_weights_nonnegative',L/A('1.00025')-(L/2+A('.001')),0)
    finite=7+14*A('4.001')/L*(A('.253')/2+A('.5'))/c
    lt('finite_rotating_coefficient',finite,'7.001')
    lt('finite_scaled_coefficient',A('7.001')/(4*pi),'.558')
    lt('retained_endpoint_coefficient',edge+A('.558'),'1.528')
    lt('prefix_discrete_first_term',3/((L.exp()+t/16).sqrt()),'.000137')
    lt('complete_prefix_coefficient',A('1.53')+A(F(12,7))+A('.000137'),'3.245')
    S=(-A(F(13,16))/t).exp()
    finite_error=160*(A(F(3,16))/t).exp()/c**2
    eps=1000*(-A('86.05')).exp()
    lt('finite_error_over_scale',finite_error/S,'2.1e-9')
    lt('edge_error_over_scale',eps/S,'5e-28')
    lt('complete_folded_coefficient',A('3.245')+2*finite_error/S+36*eps/S,'3.246')
    lt('complete_opening_ceiling',A('3.246')*S,'2.846e-7')
    gt('source_error_box_floor',2*A('2.382')*A('.999')*A('.999999'), '4.75')
    lt('source_error_box_ledger_ratio',A('3.246')/A('4.75'),'.684')
    check(all(flags.values()),'outward reserve failed: '+str([k for k,v in flags.items() if not v]))
    return {'bits':bits,'all_checks_passed':True,'values':vals,'checks':flags,
        'opening_allowances':{'complete_prefix':out(A('3.246')*S),'scale':out(S),
            'two_endpoint_finite_error':out(2*finite_error),'double_edge_model_error':out(36*eps)},
        'scope':'Constants in written uniform proof, not a height grid or H/contour quadrature.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',required=True,type=Path)
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--output',type=Path);g.add_argument('--verify',type=Path)
    p.add_argument('--bits',type=int,nargs='+',default=[192,256]);p.add_argument('--execution-model');p.add_argument('--execution-effort')
    a=p.parse_args();repo=a.repo.resolve();guards=exact_guards()
    if a.verify:
        saved=json.loads(a.verify.read_text());pins_valid(repo,saved['source_sha256'])
        check(saved['scope']=='uniform_complete_ordinary_piecewise_residual_increment','wrong scope')
        check(saved['exact_guards']==guards,'guard replay differs')
        fresh=[scalar_checks(r['bits'])for r in saved['runs']]
        check(fresh==saved['runs'],'scalar replay differs')
        print(json.dumps({'status':'verified','bits':[r['bits']for r in fresh]}));return
    check(bool(a.execution_model)and bool(a.execution_effort),'actual provenance required')
    check(all(b>=128 for b in a.bits),'precision too low')
    pins={str(v):sha(repo/v)for v in SOURCES};pins_valid(repo,pins)
    reject(lambda:pins_valid(repo,{}));stale=dict(pins);stale[str(NOTE)]='0'*64
    reject(lambda:pins_valid(repo,stale));reject(lambda:pins_valid(repo/'absent_uar04_fixture',pins))
    record={'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':a.execution_model,'actual_effort':a.execution_effort,
        'llm_assistance':'substantial; separate same-model derivation and review',
        'scope':'uniform_complete_ordinary_piecewise_residual_increment',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'rounding':'outward Arb scalar reserves and exact rational fixtures',
        'source_sha256':pins,'exact_guards':guards,
        'source_guards':{'missing_pins_rejected':True,'stale_pin_rejected':True,'missing_files_rejected':True},
        'primary_sources':['https://arxiv.org/html/1904.12438v2#S6.SS2','https://arxiv.org/html/1904.12438v2#S6.SS3'],
        'runs':[scalar_checks(b)for b in a.bits],
        'limitations':['Analytic enclosure of the signed retained expression, not numerical quadrature.',
            'No source-H calibration, physical anchor or collision exclusion.',
            'No total acquisition-cost advantage or optimality claim.',
            'The source-ledger comparison has its declared separate-envelope class.',
            'Same-model/checker replay is not independent specialist validation.']}
    a.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'written','output':str(a.output),'bits':a.bits}))
if __name__=='__main__':main()
