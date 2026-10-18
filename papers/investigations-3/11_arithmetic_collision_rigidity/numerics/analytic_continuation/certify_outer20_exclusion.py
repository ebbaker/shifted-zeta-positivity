#!/usr/bin/env python3
"""Scalar Arb replay of uniform relaxations for the exp(20/epsilon) exterior.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Actual inherited parent configuration: gpt-6.1-sol, effort ultra.
The analytic monotonicity argument is in Note 14, SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS. This script does
not enumerate a Riemann--Siegel cutoff or certify the remaining finite bridge.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import flint
from flint import arb, ctx


def A(v):
    return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)


def out(v):
    return v.str(45,more=True)


def guard_parameters(epsilon,t,X):
    if not (epsilon>0 and epsilon<=A(F(1,2))
            and t>=epsilon and t<=A(F(1,2))):
        raise ValueError('outside the positive-time slab domain')
    if not X.log()>=20/epsilon:
        raise ValueError('height is below exp(20/epsilon)')
    L=(X/(4*arb.pi())).log()
    R=A(F(5,2))/L
    if not (0<R<=1 and X-R>=200):
        raise ValueError('outside the imported complex disk domain')
    return R


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--execution-model','--model',dest='execution_model',required=True)
    parser.add_argument('--execution-effort','--effort',dest='execution_effort',required=True)
    parser.add_argument('--precision','--bits',dest='precision',type=int,default=192)
    args=parser.parse_args()
    ctx.prec=args.precision
    pi=arb.pi(); z0=A(40); X0=z0.exp()
    ell0=A(37); r=A(F(5,2)); rmax=A(F(68,1000)); delta=A('1e-15')
    V0=(X0-rmax)/2
    q0=(X0-rmax)/(4*pi)
    checks={}
    values={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise ArithmeticError(name)
    def put(name,value):
        values[name]=out(value)
        return value

    check('log_4pi_below_2_54',(4*pi).log()<A('2.54'))
    check('L_above_37',40-(4*pi).log()>ell0)
    check('R_below_0_068',r/ell0<rmax)
    check('R_at_most_one',rmax<1)
    check('lower_disk_height_above_200',X0-rmax>200)
    logq_delta=put('log_q_perturbation_upper',2*rmax/X0)
    check('log_q_delta_below_1e_15',logq_delta<delta)
    logs_delta=put('log_S_perturbation_upper',rmax/X0+(1+rmax)**2/(2*X0**2))
    check('log_S_delta_below_1e_15',logs_delta<delta)
    eps_logq=put('epsilon_log_q_lower',20-((4*pi).log()+delta)/2)
    check('epsilon_log_q_above_18_7',eps_logq>A('18.7'))
    check('log_q_above_37',40-(4*pi).log()-delta>37)

    Acap=put('Astar_over_L_upper',3/(2*V0*ell0)
               +((1+delta/ell0)**2+pi*pi/(4*ell0**2)).sqrt()/2)
    Dcap=put('Dstar_upper',3/(2*V0**2)+1/(2*V0))
    check('Astar_below_0_51_L',Acap<A('.51'))
    check('Dstar_below_0_001',Dcap<A('.001'))
    check('alpha_error_below_0_001',1/V0**2<A('.001'))
    cutoff_delta=put('cutoff_log_ratio_upper',
                     (2*rmax+pi/8)/(X0-rmax))
    check('cutoff_log_extra_below_0_01',cutoff_delta/2<A('.01'))
    check('m_minus_at_least_1e8',q0>(A(10**8)+1)**2)
    check('cutoff_span_under_one',rmax/(2*pi)+A(F(1,32))<1)

    # These use deliberately relaxed constants, shared by the analytic proof.
    klogm=put('kstar_log_m_upper',A('.0085')*z0/(X0-A('6.068')))
    check('m_power_k_below_two',klogm.exp()<2)
    pmin=put('power_p_lower',(1-rmax)/2+A('18.7')/8-A('.0015'))
    check('power_p_above_14_over_5',pmin>A(F(14,5)))
    check('AB_power_sums_dominate_n_minus_two',A(F(14,5))-rmax/2>2)
    Kcap=put('Kstar_upper',(r*A('.51')*(1+A('.00025'))/2).exp())
    check('Kstar_below_1_9',Kcap<A('1.9'))
    romega=put('R_omega_lower',r/2*(A(F(1,2))*(1-delta/ell0)
                         -A('.001')/ell0-A('.0001275')))
    check('R_omega_above_0_62',romega>A('.62'))

    Ucap=put('U_n_upper',((z0*z0/64+A('.626'))/(X0-A('6.728'))).exp()-1)
    check('U_n_below_1e_14',Ucap<A('1e-14'))
    cpositive=put('C_positive_exponent_upper',
                  A('1.24')*(A(3)**rmax+A(3)**(-rmax))/(A(10**8)-A('.125'))
                  +4*z0/(X0-A('12.068')))
    check('C_positive_exponent_below_one',cpositive<1)
    E_C=put('E_C_upper',(-A('18.7')*37/16+cpositive).exp())
    check('E_C_below_1e_17',E_C<A('1e-17'))
    check('C_second_numerator_relaxation',3*pi/2+A('10.44')<40)

    pp=A(F(14,5))
    tail=put('arithmetic_sum_upper',A(2)**(-pp)+A(3)**(-pp)+A(3)**(1-pp)/(pp-1))
    eta=put('eta_1_upper',A('1.9')*(2*tail+A('6e-14')+A('1e-17')))
    pair=put('strict_pair_criterion_upper',(eta/2)**2+(eta/A('1.24'))**2)
    check('strict_pair_criterion_below_one',pair<1)

    # The positive case is taken strictly above the threshold, so guard
    # success does not depend on an ambiguous ball equality at exp(40).
    guard_parameters(A(F(1,2)),A(F(1,2)),A(41).exp())
    rejections=[]
    for label,eps,tt,zz in [
        ('zero_epsilon',A(0),A('.2'),A(41).exp()),
        ('epsilon_above_half',A('.6'),A('.6'),A(41).exp()),
        ('time_below_epsilon',A('.2'),A('.1'),A(101).exp()),
        ('time_above_half',A('.1'),A('.6'),A(201).exp()),
        ('height_below_threshold',A(F(1,2)),A(F(1,2)),A(39).exp()),
    ]:
        try:
            guard_parameters(eps,tt,zz)
        except ValueError as exc:
            rejections.append({'case':label,'rejected':True,'reason':str(exc)})
        else:
            raise ArithmeticError('invalid theorem parameters accepted: '+label)

    rel=[
        'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex',
        'papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md',
        'papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md',
        'papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md',
    ]
    report={
        'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
        'llm_assistance':'substantial; same-model analytic derivation and scalar replay',
        'actual_model':args.execution_model,'actual_effort':args.execution_effort,
        'configuration_provenance':'trusted inherited parent execution context',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'precision_bits':ctx.prec,
        'status':'PASS: scalar outward replay; all-X coverage comes from the analytic proof',
        'theorem_domain':'0<epsilon<=1/2, epsilon<=t<=1/2, |x|>=exp(20/epsilon)',
        'frozen_parameters':'at arbitrary real height X, L=log(X/(4pi)), R=(5/2)/L, a=0, N=1',
        'primary_source':'https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3',
        'source_sha256':{p:hashlib.sha256((args.repo/p).read_bytes()).hexdigest() for p in rel},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scalar_enclosures':values,'strict_checks':checks,
        'invalid_parameter_rejections':rejections,
        'limitations':['does not close 1001<|x|<exp(2000) at epsilon=1/100',
                       'does not establish a new Newman bound',
                       'uses the imported explicit fixed-cutoff Riemann--Siegel error theorem'],
    }
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks':len(checks),
                      'pair_criterion':out(pair),'output':str(args.output)}))


if __name__=='__main__':
    main()
