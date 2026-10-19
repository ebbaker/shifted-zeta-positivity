#!/usr/bin/env python3
"""S02-T1: strongest frozen exponential versus full analytic correction.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual reasoning effort ultra. Internal research.
Requires python-flint 0.9.0. Exact analytic error envelopes, not paid fields.
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
from flint import arb,acb,acb_series,ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
S02=INV/'symmetries/02_cutoff_reflection'
OLD=Path('papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport')


def check(c,message):
    if not c:raise ArithmeticError(message)


def out(x):return x.str(45,more=True)


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    spec.loader.exec_module(mod);return mod


def vmax(values):
    return max(v.abs_upper() for v in values)


def edge_payment(s,xlo,xhi,K,W,pref,R=F(1,2)):
    """Note22 printed-jump comparison; not a direct analytic-jump estimate."""
    check(R==F(1,2),'matched contract requires radius one half')
    check((xlo,xhi)==(1017,1019),'edge formula restricted to declared crossing C')
    pi=arb.pi();r=s.A(R);eps=arb(1)/100;T=arb(1)/5
    xm=arb(xlo)-r;xp=arb(xhi)+r;Tlo=xm/2
    vlo=Tlo+pi*eps/8;vhi=xp/2+pi*T/8
    alo=(vlo/(2*pi)).sqrt();ahi=(vhi/(2*pi)).sqrt();m=arb(9)
    check(alo<9 and ahi>9 and alo>8 and ahi<10,'global single crossing failed')
    d=vmax([alo-m,ahi-m]);E=vmax([(alo/m).log(),(ahi/m).log()])
    sigma=(1+r)/2;Delta=(sigma*sigma+(pi*T/8)**2).sqrt()
    D0=3/(2*vlo);D1=1/(2*Tlo)+3/(2*Tlo*Tlo);Ds=D0+Delta*D1
    parts={'sigma_log':sigma*E,'heat_log':T*E*E/4,
           'cubic_phase':2*pi*d**3/(3*alo),
           'Stirling_linear':Delta*D0,'Stirling_quadratic':Delta*Delta*D1/2,
           'heat_Stirling':T*(2*(E+pi/4)*Ds+Ds*Ds)/4}
    Lambda=sum(parts.values(),arb(0));rel=2*(Lambda.exp()-1)
    check(Lambda>0 and Lambda<arb('0.02'),'edge exponent admissibility')
    exactpref=(pref*rel).upper()
    # Literal historical prefactor bound, useful as a separate source audit.
    qlo=xm/(4*pi);qhi=xp/(4*pi)
    Z=qlo**(-arb(1)/4)*(-eps*qlo.log()**2/16+
        (3*(qhi.log()**2+pi*pi/4).sqrt()+arb('3.58'))/(xm-arb('8.52'))).exp()
    historical=(K*Z*rel).upper()
    check(exactpref<historical,'exact prefactor should improve historical edge bound here')
    return {'bound':out(exactpref),'literal_KZ_bound':out(historical),
            'Lambda':out(Lambda),'relative_2expm1':out(rel),
            'terms':{k:out(v) for k,v in parts.items()},
            'a_lower':out(alo),'a_upper':out(ahi),'d_upper':out(d),'log_ratio_upper':out(E),
            'delta_upper':out(Delta),'D0':out(D0),'D1':out(D1),'Ds':out(Ds),
            'scope':'Printed correction jump g9-exp(-iky)(C9(x)-C8(x)); shared by exact fixed-N decomposition.'},exactpref,Z


def logA_jets(s,x,t):
    z=acb(x);ss=(1-acb(0,1)*z)/2
    def mp(v):return s.alpha(v)*(1+t*s.alphap(v)/2)
    def mpp(v):return s.alphap(v)*(1+t*s.alphap(v)/2)+t*s.alpha(v)*s.alphapp(v)/2
    b=(-acb(0,1)*(mp(ss)-mp(1-ss))/4).real
    bp=(-(mpp(ss)+mpp(1-ss))/8).real
    check(b.is_finite() and bp.is_finite(),'nonfinite normalizer jets')
    return b,bp


def compare(s,xlo,xhi,nt,nx,ny,cross):
    check((xlo,xhi,nt,nx,ny,cross) in [(999,1001,4,24,8,False),(1017,1019,8,64,16,True)],
          'comparison outside declared domains or fixed covers')
    begin=time.monotonic();R=arb(1)/2;eps=arb(1)/100;T=arb(1)/5;pi=arb.pi()
    # Freshly repeat opening reference with its exact original grid and costs.
    original=s.disk_budget(xlo,xhi,8,nt,nx,ny,cross)
    constants=original['constants'];parts=original['error_parts']
    K=arb(constants['Kstar']).upper();W=arb(constants['W_real_upper']).upper()
    pref=arb(constants['correction_amplitude_over_A_upper']).upper()
    shared=arb(parts['AB_shared']).upper();published=arb(parts['signed_C_remainder']).upper()
    if cross:
        edge,edgebound,Z=edge_payment(s,xlo,xhi,K,W,pref)
    else:
        xm=arb(xlo)-R;xp=arb(xhi)+R;qlo=xm/(4*pi);qhi=xp/(4*pi)
        Z=qlo**(-arb(1)/4)*(-eps*qlo.log()**2/16+
            (3*(qhi.log()**2+pi*pi/4).sqrt()+arb('3.58'))/(xm-arb('8.52'))).exp()
        edge={'bound':'0','literal_KZ_bound':'0','scope':'No natural-cutoff change on B.'};edgebound=arb(0)
    xm=arb(xlo)-R;xp=arb(xhi)+R
    BC=arb('1.24')*(3**R+3**(-R))/(8-arb('.125'))+arb('6.92')/(xm-12)
    historical_residual=(K*Z*BC).upper()
    check(published<historical_residual,'stronger direct published residual gate')
    Mc=arb(0);Mr=arb(0);B=arb(0);B1=arb(0);Bplus=arb(0);Cplus=arb(0)
    complex_count=0;real_count=0;normalizer_count=0;minimum_den=None
    for it in range(nt):
        t=s.interval(F(1,100)+F(19,100)*it/nt,F(1,100)+F(19,100)*(it+1)/nt)
        for ix in range(nx):
            x=s.interval(F(xlo)-F(1,2)+F(3)*ix/nx,F(xlo)-F(1,2)+F(3)*(ix+1)/nx)
            _,fp=s.J(x,t,8);check(fp.is_finite(),'real profile failed')
            Mr=max(Mr,abs(fp).upper());real_count+=1
            # Normalizer return constants only need the real center family.
            X=s.interval(F(xlo)+F(2)*ix/nx,F(xlo)+F(2)*(ix+1)/nx)
            b,bp=logA_jets(s,X,t);B=max(B,b.abs_upper());B1=max(B1,bp.abs_upper())
            Bplus=max(Bplus,(b+pi/8).abs_upper())
            Cplus=max(Cplus,((b+pi/8)**2+bp).abs_upper());normalizer_count+=1
            for iy in range(ny):
                y=s.interval(F(iy,2*ny),F(iy+1,2*ny));z=acb(x,y)
                p=17-2*((z/2+pi*t/8)/(2*pi)).sqrt()
                den=(pi*p).cos().abs_lower()
                check(den>0,'profile cell encounters a removable denominator; local continuation needed')
                minimum_den=den if minimum_den is None else min(minimum_den,den)
                _,fp=s.J(z,t,8);check(fp.is_finite(),'complex profile failed')
                Mc=max(Mc,abs(fp).upper());complex_count+=1
    check(Mr<Mc,'recorded real-slope bound not strictly below complex bound')
    contfr=(K*W*R*Mr).upper();contan=(K*W*R*Mc).upper()
    eta_fr=(shared+published+edgebound+contfr).upper()
    eta_an=(shared+published+edgebound+contan).upper()
    check(eta_fr<eta_an,'full analytic envelope unexpectedly beats strongest frozen comparator')
    if cross:check(eta_an<arb(original['eta_candidate']),'shared analytic edge failed to sharpen crossing')
    # Literal Note22 full-profile recipe, apart from same Q normalization.
    vlo=xm/2+pi*eps/8;vhi=xp/2+pi*T/8;alo=(vlo/(2*pi)).sqrt()
    ahi=(vhi/(2*pi)).sqrt()
    pformal=s.interval(17-2*ahi,17-2*alo)
    check(pformal.abs_upper()<arb(21)/20,'historical global-profile phase range failed')
    Jglobal=3/vlo+1/(vlo*vlo)+(20+20/vlo)/(4*pi*alo)
    Wtau=(vhi/vlo)**(arb(3)/2)
    old_holo=(2*K*Z*R*Wtau*Jglobal).upper()
    # The historical theorem is center-normalized; divide by analytic A(z)
    # only after an additional segment bound. It is reported separately.
    historical_center=(shared+historical_residual+arb(edge['literal_KZ_bound']).upper()+old_holo).upper()
    historical_Q=(K*historical_center).upper()
    physical_factors=[arb(1),2+B,8+4*B+B*B+B1]
    correlated_factors=[2+Bplus,8+4*Bplus+Cplus]
    return {'label':'C' if cross else 'B','bits':ctx.prec,
            'real_domain':original['real_domain'],'radius':'1/2','fixed_cutoff':8,
            'enclosing_x':[str(F(xlo)-F(1,2)),str(F(xhi)+F(1,2))],
            'possible_natural_cutoffs':original['possible_natural_cutoffs'],
            'grid':[nt,nx,ny],'complex_cells':complex_count,'real_slope_cells':real_count,
            'real_normalizer_cells':normalizer_count,
            'profile_denominator_abs_lower':out(minimum_den),
            'common_source':{'AB':out(shared),'corrected_published_direct':out(published),
                             'older_KZ_BC':out(historical_residual)},
            'common_edge':edge,
            'slope':{'fixed_N_real':out(Mr),'fixed_N_complex':out(Mc)},
            'continuation':{'frozen_real':out(contfr),'full_complex':out(contan)},
            'eta':{'frozen':out(eta_fr),'full_same_edge':out(eta_an),
                   'full_opening':original['eta_candidate'],
                   'literal_prior_center_normalization':out(historical_center),
                   'literal_prior_after_safe_Q_conversion':out(historical_Q)},
            'ordering':{'frozen_strictly_smaller':True,
                        'full_over_frozen':out(eta_an/eta_fr),
                        'full_minus_frozen':out(eta_an-eta_fr),
                        'crossing_full_over_opening':out(eta_an/arb(original['eta_candidate'])) if cross else None},
            'Q_residual_jet_errors':{'frozen':[out(f*eta_fr) for f in [1,2,8]],
                                     'full_same_edge':[out(f*eta_an) for f in [1,2,8]]},
            'real_normalizer_bounds':{'abs_b':out(B),'abs_bprime':out(B1),
                                      'abs_b_plus_pi_over_8':out(Bplus),
                                      'abs_b_plus_k_squared_plus_bprime':out(Cplus)},
            'physical_jet_errors_over_A':{'frozen':[out(f*eta_fr) for f in physical_factors],
                                          'full_same_edge':[out(f*eta_an) for f in physical_factors]},
            'correlated_physical_demodulated_bounds':{
                'first_D_plus_k_error':out(correlated_factors[0]*eta_fr),
                'second_D_plus_k_error':out(correlated_factors[1]*eta_fr),
                'scope':'Bounds for (D+k)^j(H-G8)/A; retained frozen exponential annihilated before absolute estimation.'},
            'literal_prior_global_holomorphic_comparison':out(old_holo),
            'literal_prior_formal_phase_range':out(pformal),
            'literal_prior_phase_abs_below_21_over_20':True,
            'newly_shared_edge_vs_opening_direct':{
                'opening_direct_transition':parts['signed_cutoff_transition'],
                'analytic_printed_jump_transition':out(edgebound)},
            'opening_reference':original,
            'selected':'frozen per-disk correction for local jets; retain full for a named global analytic residual use',
            'seconds':time.monotonic()-begin}


def algebra_checks(s):
    old=s.algebra_checks();pi=arb.pi();k=pi/8;t=arb(21)/200;checks=[]
    for X in [arb(1000),arb(1018)]:
        z=acb_series([acb(X),acb(1)],3)
        C=s.correction(acb(X),t,8)
        frozen=C*(-k*(z-X)).exp()/s.normalizer(z,t)
        b,bp=logA_jets(s,X,t);c=(C/s.normalizer(acb(X),t)).real
        expected=[c,-(k+b)*c,((k+b)**2-bp)*c]
        for j in range(3):check((frozen[j]*(2 if j==2 else 1)-expected[j]).contains(0),'frozen normalized jet chain rule')
        full=s.correction(z,t,8)/s.normalizer(z,t)
        check((full[0]-frozen[0]).contains(0),'real-center correction values mismatch')
        check(not(full[1]-frozen[1]).contains(0),'derivative-freezing challenge inconclusive')
        zc=acb(X,arb(1)/5);x=zc.real;y=zc.imag
        pub=lambda n:(-acb(0,1)*k*y).exp()*s.correction(acb(x),t,n)
        analytic_jump=s.correction(zc,t,9)-s.correction(zc,t,8)
        printed_jump=pub(9)-pub(8)
        direct=s.mode(zc,t,9)-analytic_jump
        alternate=s.mode(zc,t,9)-printed_jump+(printed_jump-analytic_jump)
        check((direct-alternate).contains(0),'printed versus analytic jump decomposition')
        check(not(printed_jump-analytic_jump).contains(0),'wrong analytic-jump identification accepted')
        checks.append({'center':out(X),'same_center_value':True,'different_center_derivative':True,
                       'normalized_frozen_vector_verified':True,
                       'printed_analytic_jump_difference':str(printed_jump-analytic_jump),
                       'dropping_jump_continuation_difference_rejected':True})
    return {'opening_algebra':old,'frozen_and_jump_checks':checks}


def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--bits',type=int,nargs='+',default=[192,256])
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    args=p.parse_args();repo=args.repo.resolve();begin=time.monotonic()
    src=repo/S02/'numerics/check_cutoff_reflection.py';s=load(src,'s02_opening_comparison')
    runs=[]
    for bits in args.bits:
        check(bits>=128,'insufficient declared precision');ctx.prec=bits
        row={'bits':bits,'boxes':[compare(s,999,1001,4,24,8,False),compare(s,1017,1019,8,64,16,True)],
             'algebra':algebra_checks(s)}
        runs.append(row)
        print(json.dumps({'bits':bits,'eta':[{x['label']:x['eta']} for x in row['boxes']]}),flush=True)
    ctx.prec=max(args.bits)
    if len(runs)>1:
        for run in runs[1:]:
            for i in range(2):
                for key in ['frozen','full_same_edge']:
                    check(arb(runs[0]['boxes'][i]['eta'][key]).overlaps(arb(run['boxes'][i]['eta'][key])),
                          'precision replay disjoint for declared uniform allowance')
    rejected=[]
    try:compare(s,999,1002,4,24,8,False)
    except ArithmeticError as e:rejected.append({'case':'changed domain','reason':str(e)})
    else:raise ArithmeticError('changed comparison domain accepted')
    try:edge_payment(s,1017,1019,arb(2),arb(1),arb(1),F(1))
    except ArithmeticError as e:rejected.append({'case':'changed radius','reason':str(e)})
    else:raise ArithmeticError('changed comparison radius accepted')
    paths=[src,repo/S02/'notes/01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md',
           repo/INV/'symmetries/notes/02_S02_MATCHED_CORRECTION_COMPARISON_CONTRACT_20261019.md',
           repo/INV/'manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex',
           repo/OLD/'notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md',
           repo/OLD/'notes/21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md',
           repo/OLD/'notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md',
           repo/OLD/'numerics/check_theta_cutoff_matching.py']
    report={'schema':'s02-matched-correction-v1','date':'2026-10-19','timezone':'America/New_York',
            'prepared_for':'Edward Baker','actual_model':args.execution_model,'actual_effort':args.execution_effort,
            'llm_assistance':'substantial; internal derivation and separate same-model review',
            'python':platform.python_version(),'python_flint':flint.__version__,
            'script_sha256':digest(__file__),'source_sha256':{str(f.relative_to(repo)):digest(f) for f in paths},
            'primary_source':'https://arxiv.org/html/1904.12438v2#S6.SS3',
            'primary_metric':'complete normalized Q-disk residual eta and common Cauchy jet factors (1,2,8)',
            'runs':runs,'guard_rejections':rejected,'status':'pass',
            'classification':'matched estimate comparison; full analytic first-derivative continuation ledger does not beat strongest frozen comparator',
            'new_noncollision_coverage':False,'new_Newman_bound':False,'matched_cost_claim':False,
            'evaluated_whole_cell_jets':False,'selected_for_T2':'frozen center parameter during all spatial derivatives',
            'seconds':time.monotonic()-begin}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'pass','output':str(args.output),'bytes':args.output.stat().st_size,'seconds':report['seconds']}))

if __name__=='__main__':main()
