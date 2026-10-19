#!/usr/bin/env python3
"""Outward constants for UAR-02's written uniform finite-component proof.

Prepared for Edward Baker with substantial LLM assistance, 19 October 2026.
This is not theta quadrature, an RS edge estimate or a physical certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
sys.dont_write_bytecode=True
import flint
from flint import arb, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/03_normalized_jet_rotation'
NOTE=LANE/'notes/08_UNIFORM_FINITE_GAMMA_HEAT_REMAINDER_20261019.md'
SCRIPT=LANE/'numerics/check_uniform_finite_gamma_heat.py'
SOURCES=[NOTE,SCRIPT,
    INV/'symmetries/notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md',
    LANE/'notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md',
    INV/'symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md',
    LANE/'numerics/UAR02_SOURCE_CONTROLS_20261019.json',
    INV/'numerics/replay_nonstationary_controls.py',
    Path('result-summaries/12_collision_controls_and_screening.md')]

def A(v):
    return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)

def check(ok,message):
    if not ok: raise ArithmeticError(message)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def out(v): return v.str(38,more=True)

def validate_sector(t,kappa):
    check(isinstance(t,F) and isinstance(kappa,F),'exact rational sector parameters required')
    check(0<t<=F(1,20) and 1<=kappa<=2,'sector not covered')
    return kappa/t

def validate_pins(repo,pins):
    check(set(pins)=={str(p) for p in SOURCES},'missing/extra source pin')
    for name,digest in pins.items():
        p=repo/name
        check(p.is_file() and not p.is_symlink(),'missing/linked source: '+name)
        check(sha(p)==digest,'stale source: '+name)

def reject(call):
    try: call()
    except ArithmeticError: return
    raise ArithmeticError('invalid fixture accepted')

def exact_guards():
    for t,k in [(F(1,20),F(1)),(F(1,20),F(2)),(F(1,1000),F(3,2))]:
        check(validate_sector(t,k)>=20,'lower L')
    invalid=[(F(0),F(1)),(F(-1),F(1)),(F(1,19),F(1)),
             (F(1,20),F(1,2)),(F(1,20),F(3)),(.05,F(1))]
    for t,k in invalid: reject(lambda t=t,k=k:validate_sector(t,k))
    # For delta=sqrt(t)*v+t*a/2 and E v=0, E v²=1/2:
    # (alpha'/2) E delta² = alpha'*(t/4+t²*a²/8).
    expected={(1,0):F(1,4),(2,2):F(1,8)}
    derived={(1,0):F(1,2)*F(1,2),(2,2):F(1,2)*F(1,4)}
    check(derived==expected,'prescribed heat curvature moment')
    check({(1,0):F(1,4)}!=expected,'deleted heat drift mutation')
    return {'invalid_sector_inputs_rejected':len(invalid),
        'heat_correction_moment_identity':'exact rational coefficients',
        'deleted_t_squared_drift_mutation_rejected':True}

def scalar_checks(bits):
    ctx.prec=bits; pi=arb.pi(); C=A(10)**9; u=2*C.sqrt(); L=A(20)
    vals={}; flags={}
    def less(name,value,cap):
        vals[name]={'value':out(value),'upper_cap':str(cap)}
        flags[name]=bool(value<A(cap))
    def greater(name,value,floor):
        vals[name]={'value':out(value),'lower_floor':str(floor)}
        flags[name]=bool(value>A(floor))
    greater('opening_height',4*pi*A(20).exp(),10**9)
    greater('s_modulus_lower_reserve',C/2-1-A('.499')*C,0)
    less('s_modulus_upper_ratio',((C/2+1)**2+A('1.5')**2).sqrt()/C,'.501')
    less('log_alpha_real_loss',max(abs((A('.998')).log()/2),abs(A('1.002').log()/2)).upper()+A('1.5')/(A('.499')*C),'.002')
    less('log_alpha_imag',pi/4+A('.001')+A('1.5')/(A('.499')*C),'.8')
    less('alpha_minus_ell_modulus_at_L20',((L/2+A('.002'))**2+A('.8')**2).sqrt(),11)
    less('shift_abs',A(F(21,40)),'.6')
    less('sqrt_t',A('.05').sqrt(),'.224')
    less('central_d_over_sqrt_c',A('.448')+A('.6')/C.sqrt(),'.449')
    greater('central_segment_distance_ratio',A('.499')-A('.449')/C.sqrt(),'.49')
    less('alpha_prime_scaled',1/(2*A('.499'))+A('1.5')/(A('.499')**2*C),'1.01')
    less('alpha_second_scaled',A('.5')/A('.49')**2+3/(A('.49')**3*C),'2.1')
    less('central_argument_loss',(A('1.5')+A('.449')*C.sqrt())/(A('.49')*C),'.001')
    less('central_stirling_sec_factor',((pi/2+A('.001'))/2).cos()**-4,5)
    less('central_stirling_scaled',5/(45*A('.49')**3),1)
    less('reciprocal_difference_coefficient',1/(6*A('.499')*A('.49')),'.7')
    less('h_envelope_constant',1/(6*A('.499'))+A('.7')*A('.449')/C.sqrt()+1/C**2,'.35')
    less('h_envelope_quadratic',A('.505')+A('.35')*A('.449')/C.sqrt(),'.511')
    less('central_h_max',A('.35')/C+A('.511')*A('.449')**2,'.11')
    moments={}
    caps={1:'.727',2:'.538',3:'.407',4:'.315'}
    for j in range(1,5):
        v=sum((A(math.comb(j,k))*A('.224')**k*A('.6')**(j-k)
               *A(F(k+1,2)).gamma()/pi.sqrt() for k in range(j+1)),A(0))
        moments[str(j)]=out(v); less('moment_'+str(j),v,caps[j])
    h2=A('.35')**2+2*A('.35')*A('.511')*A('.538')+A('.511')**2*A('.315')
    less('h_squared_moment_scaled',h2,'.397196')
    central=A('.7')*A('.727')+A('.35')*A('.407')+1/C+A('.11').exp()*h2/2
    less('central_remainder_scaled',central,'.874')
    less('tail_sigma_over_u',A('1.05')/u+A('.112'),'.113')
    less('tail_gamma_quadratic',A('.113')**2,'.013')
    less('tail_polynomial_log_ratio',4*u.log()/u**2,'.001')
    less('tail_alpha_growth_ratio',(C.log()/2+1)/C.sqrt(),'.001')
    less('tail_other_factors_ratio',A('1.203')/u**2+A('.1293')/u+A('.000112'),'.001')
    less('m0_negative_lower_ratio',pi/8+(A('.75')*C.log()+5)/C,1)
    less('tail_exact_exponent_ratio',A('.25')-A('.985'),'-.7')
    less('tail_model_quadratic_coefficient',A('1.01')*A('.225')**2/2,'.026')
    greater('tail_model_exponential_reserve',u**2/4-(2+u**2).log(),0)
    # Positive log reserve proves the combined tail < c^-10 without underflow.
    greater('tail_c_minus10_log_reserve',A('2.8')*C+(A('.7')*(pi*C).sqrt()).log()-10*C.log(),0)
    less('total_relative_error_scaled',A('.874')+C**-8,2)
    less('chi_scaled',1/(6*A('.499'))+A('1.01')*(A('.05')/4+A('1.05')**2/8),'.5')
    less('extra_mode_log_loss',(1+(-A(10)).exp()).log(),'.001')
    less('exact_alpha_mass_factor',(1/C**2).exp(),'1.000001')
    less('real_mass_factor',6*A('1.000001'),7)
    less('complex_disk_transport',A('.6').exp(),2)
    less('complex_mode_log_rate_ratio',(A('.5')+A('.5005')/20)*(1+A('.05')*A('1.01')/(2*C)),'.6')
    less('rotating_coefficient',56*(1+(A('4.001')*(A('.6')+1/L))**2).sqrt(),160)
    greater('E1_monotonicity_reserve',A(F(29,16))*(A('.6')*L+1)-A('.6'),0)
    check(all(flags.values()),'failed outward proof constant: '+str([k for k,v in flags.items() if not v]))
    base=(-A(F(145,4))).exp()/(16*pi*pi)
    opening={'E0':56*base,'E1':56*13*base,'Delta_AB':160*base,
        'two_endpoint_Delta_AB':320*base,'common_finite_allowance_ratio_upper':4/(4*pi*A(20).exp())}
    check(opening['E0']<A('6.5e-17') and opening['E1']<A('8.4e-16')
          and opening['Delta_AB']<A('1.9e-16'),'opening rounded ceilings')
    return {'bits':bits,'all_checks_passed':True,'values':vals,'checks':flags,
        'gaussian_absolute_moments_of_d':moments,
        'opening_upper_allowances':{k:out(v) for k,v in opening.items()},
        'monotonic_scope':'Endpoint checks support the explicit analytic monotonic arguments in Note08; no sampled height coverage.'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--output',type=Path);g.add_argument('--verify',type=Path)
    p.add_argument('--bits',type=int,nargs='+',default=[192,256])
    p.add_argument('--execution-model');p.add_argument('--execution-effort')
    a=p.parse_args();repo=a.repo.resolve();guards=exact_guards()
    if a.verify:
        saved=json.loads(a.verify.read_text());validate_pins(repo,saved['source_sha256'])
        check(saved['scope']=='uniform_finite_component_only','wrong theorem scope')
        check(saved['exact_guards']==guards,'guard replay mismatch')
        fresh=[scalar_checks(r['bits']) for r in saved['runs']]
        check(fresh==saved['runs'],'scalar replay differs; assess environment/source before replacing receipt')
        print(json.dumps({'status':'verified','bits':[r['bits'] for r in fresh],'scope':saved['scope']}));return
    check(bool(a.execution_model) and bool(a.execution_effort),'actual execution provenance required')
    check(all(b>=128 for b in a.bits),'precision below declared check minimum')
    pins={str(v):sha(repo/v) for v in SOURCES};validate_pins(repo,pins)
    reject(lambda:validate_pins(repo,{}))
    stale=dict(pins);stale[str(NOTE)]='0'*64
    reject(lambda:validate_pins(repo,stale))
    reject(lambda:validate_pins(repo/'nonexistent_uar02_fixture',pins))
    record={'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':a.execution_model,'actual_effort':a.execution_effort,
        'llm_assistance':'substantial; separate same-model internal proof/replay review',
        'scope':'uniform_finite_component_only','python':platform.python_version(),'python_flint':flint.__version__,
        'rounding':'outward Arb scalar arithmetic; exact rational guard/correction fixtures',
        'source_sha256':pins,'exact_guards':guards,
        'source_guards':{'missing_pins_rejected':True,'stale_pin_rejected':True,'missing_files_rejected':True},
        'runs':[scalar_checks(b) for b in a.bits],
        'limitations':['Written analytic proof supplies unbounded-domain theorem; scalar replay does not prove it.',
            'No H source calibration, quadrature, inferred edge or physical acceptance data.',
            'Retained finite correction, complete RS edge and cutoff transition sum remain separate.',
            'No new physical margin, collision coverage, cost advantage or Newman bound.']}
    a.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'written','output':str(a.output),'bits':a.bits,
                      'scope':record['scope']}))

if __name__=='__main__':main()
