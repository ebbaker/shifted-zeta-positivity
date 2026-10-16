#!/usr/bin/env python3
"""Modular Hodge channel, lossless cusp load, and shift-tangent diagnostics.

Requires mpmath and NumPy. Finite controls, not rigorous enclosures or an RH
test. Includes regression checks for two corrected continuation programs.
Prepared for Edward Baker, GPT-6 (Codex), 23 September 2026.
Effort not exposed; not inferred.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform

import mpmath as mp
import numpy as np

CASES=[]


def check(name, value, threshold, comparison='<=', kind='floating'):
    value,threshold=float(value),float(threshold)
    passed=math.isfinite(value) and (value<=threshold if comparison=='<=' else value>=threshold)
    CASES.append(dict(name=name,value=value,threshold=threshold,
                      comparison=comparison,passed=passed,kind=kind))


def relative(x,y):
    return abs(x-y)/max(mp.mpf(1),abs(y))


def xi(s):
    s=mp.mpc(s)
    if s in (0,1):
        return mp.mpf('.5')
    if s.real<mp.mpf('.5'):
        return xi(1-s)
    return s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)


def half(p):
    return xi(p)/xi(p+1)


def phi(p):
    # Scalar Eisenstein coefficient with p=2*sigma-1.
    return mp.sqrt(mp.pi)*mp.gamma(p/2)/mp.gamma((p+1)/2)*mp.zeta(p)/mp.zeta(p+1)


def a_half(p):
    return mp.diff(xi,p)/xi(p)+mp.diff(xi,p+1)/xi(p+1)


def coupled(p,alpha,b):
    r=mp.exp(-b*p)*half(p)  # normalized (minus raw) reflection at the port
    return (p*r+alpha*(1-r))/(p+alpha*(1-r))


def tangent(p,b):
    r=mp.exp(-b*p)*half(p)
    return (1-r)**2/(p*r)


def qratio(u):
    return -mp.expm1(-2*u)/(2*u) if u else mp.mpf(1)


def k0(u):
    return 2*(2*mp.exp(-2*u)-1)/mp.sqrt(-mp.expm1(-2*u))


def G0(u):
    if u<=0:
        return mp.mpf(0)
    z=mp.sqrt(-mp.expm1(-2*u))
    # atanh(z)=u+log(1+z), avoiding catastrophic loss for large u.
    return 4*z-2*u-2*mp.log1p(z)


def Q0(u):
    # Integral of k0*k0 up to u. The substitution v=u*sin(theta)^2
    # removes both square-root endpoint behaviors.
    def integrand(theta):
        v=u*mp.sin(theta)**2
        return (2*mp.sqrt(2*u)*mp.cos(theta)*(2*mp.exp(-2*v)-1)
                /mp.sqrt(qratio(v))*G0(u-v))
    return mp.quad(integrand,[0,mp.pi/4,mp.pi/2])


def kernel_beta(u,omega):
    z=-mp.expm1(-2*u)
    prefactor=2*mp.pi**omega/mp.gamma(omega)
    return prefactor*(mp.exp(-(mp.mpf('2.5')-omega)*u)*z**(omega-1)
        -omega*mp.exp((mp.mpf('.5')-omega)*u)
        *mp.betainc(omega,mp.mpf('1.5')-omega,0,z))


def prime_free_symbol(p,omega):
    return (mp.pi**omega*mp.gamma((p+mp.mpf('2.5')-omega)/2)
            /mp.gamma((p+mp.mpf('2.5')+omega)/2)
            *(p-mp.mpf('.5')-omega)/(p-mp.mpf('.5')+omega))


def complex_json(z):
    return dict(real=mp.nstr(mp.re(z),24),imag=mp.nstr(mp.im(z),24))


def load_sibling(filename,name):
    path=Path(__file__).with_name(filename)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(dps):
    mp.mp.dps=dps
    observations={}
    for p in [mp.mpf(2),mp.mpf(4),mp.mpc(3,2),mp.mpc('.5',3)]:
        sigma=(p+1)/2
        raw=(1-sigma)/sigma*phi(p)
        check(f'gradient constant term gives minus K p={p}',relative(-raw,half(p)),1e-35)

    for k in map(mp.mpf,['.3','1','5','10']):
        sigma=mp.mpf('.5')-mp.j*k
        energy=mp.mpf('.25')+k*k
        check(f'normalized gradient channel isometry k={k}',
              max(abs(abs(sigma/mp.sqrt(energy))-1),abs(abs((1-sigma)/mp.sqrt(energy))-1)),1e-35)
    for eps in map(mp.mpf,['.0001','.000001']):
        check(f'scalar pole residue eps={eps}',abs(eps*phi(1+eps)-6/mp.pi),10*eps)
        check(f'gradient removes pole eps={eps}',abs(half(1+eps)-3/mp.pi),eps)
    observations['completed_value_at_p1']=mp.nstr(mp.re(half(1)),24)

    for n in [2,3,4,6,12]:
        coprime=sum(math.gcd(j,n)==1 for j in range(1,n+1))
        prime_factors=[p for p in range(2,n+1) if n%p==0
                       and all(p%d for d in range(2,math.isqrt(p)+1))]
        product=Fraction(1)
        for p in prime_factors:
            product*=Fraction(p-1,p)
        check(f'primitive residue coefficient n={n}',
              0 if Fraction(coprime,n)==product else 1,0,kind='exact rational')

    for p in [mp.mpf(2),mp.mpf(5),mp.mpc(3,2)]:
        # Laplace transform of the geometric gamma/rational kernel.
        val=mp.quad(lambda t: 2*mp.sqrt(2)*mp.exp(-p*t*t)
                    *(2*mp.exp(-2*t*t)-1)/mp.sqrt(qratio(t*t)),
                    [0,mp.mpf('.5'),1,2,mp.inf])
        check(f'half shift kernel Laplace p={p}',relative(val,prime_free_symbol(p,mp.mpf('.5'))),1e-35)
    for u in map(mp.mpf,['.1','.7']):
        check(f'half shift cumulative derivative u={u}',relative(mp.diff(G0,u),k0(u)),1e-35)
        check(f'incomplete beta agrees with half shift closed form u={u}',
              relative(kernel_beta(u,mp.mpf('.5')),k0(u)),1e-35)

    ell=mp.log(2)
    def window_output(u):
        return G0(u)+(G0(u-ell)/2 if u>ell else 0)
    energy=mp.quad(lambda u:window_output(u)**2,[0,ell,1])
    check('physical half shift unit window contraction',energy,1)
    check('physical half shift positive future output',1-energy,mp.mpf('.001'),'>=')
    with mp.workdps(dps+15):
        refined=mp.quad(lambda u:window_output(u)**2,[0,mp.log(2),1])
        check('unit window quadrature refinement',relative(energy,refined),1e-35)
    observations['unit_window_constant_input']=dict(output_energy=mp.nstr(energy,24),
        future_energy_from_proved_conservation=mp.nstr(1-energy,24))

    for k,alpha,b in [(mp.mpf('.7'),mp.mpf('.3'),1),(mp.mpf(2),mp.mpf(1),1),(mp.mpf(5),mp.mpf('.4'),0)]:
        p=-2*mp.j*k
        raw=-mp.exp(-p*b)*half(p)
        matrix=mp.matrix([[1,-(1+raw)],[mp.j*k-alpha,-mp.j*k*(raw-1)]])
        rhs=mp.matrix([-1,mp.j*k+alpha])
        raw_out,interior=mp.lu_solve(matrix,rhs)
        value=coupled(p,alpha,b)
        check(f'interface solve versus response k={k},b={b}',relative(-raw_out,value),1e-35)
        check(f'lossless loaded reflection k={k},b={b}',abs(abs(value)-1),1e-35)

    for p,alpha,b in [(mp.mpc(1,2),mp.mpf('.2'),0),(mp.mpc(1,2),mp.mpf('.2'),1),
                      (mp.mpc(3,'.5'),mp.mpf(1),0),(mp.mpc(3,'.5'),mp.mpf(1),1)]:
        r=mp.exp(-p*b)*half(p)
        den=p+alpha*(1-r); num=p*r+alpha*(1-r)
        rhs=abs(p)**2*(1-abs(r)**2)+2*alpha*mp.re(p)*abs(1-r)**2
        check(f'loaded passivity identity p={p},b={b}',relative(abs(den)**2-abs(num)**2,rhs),1e-35)
    for p in [mp.mpf(2),mp.mpf(4)]:
        for b in [0,1]:
            derivative=mp.diff(lambda alpha:mp.log(coupled(p,alpha,b)),0)
            check(f'logarithmic load tangent p={p},b={b}',relative(derivative,tangent(p,b)),1e-35)

    fits=[]
    for p in [2,4,8,32,128,512]:
        fits.append(dict(p=p,half_shift=mp.nstr(mp.re(half(p)),20),
            arithmetic_source=mp.nstr(mp.re(a_half(p)),20),
            clock_fit_b0=mp.nstr(mp.re(-tangent(p,0)/a_half(p)),20),
            clock_fit_b1=mp.nstr(mp.re(-tangent(p,1)/a_half(p)),20)))
    observations['incompatible_clock_fits']=fits
    check('b0 shift-clock fit changes with frequency',
          abs(mp.mpf(fits[0]['clock_fit_b0'])-mp.mpf(fits[3]['clock_fit_b0'])),.005,'>=')
    check('b1 shift-clock fit changes with frequency',
          abs(mp.mpf(fits[0]['clock_fit_b1'])-mp.mpf(fits[2]['clock_fit_b1'])),700,'>=')
    for b in [0,1]:
        p=mp.mpf(1000000)
        scaled=tangent(p,b)*mp.sqrt(2*mp.pi*p)*mp.exp(-b*p)
        check(f'large-p load tangent asymptotic b={b}',abs(scaled-1),.006)

    first_delay=[]
    omega=mp.mpf('.5'); c2=mp.mpf('.5'); c2prime=mp.mpf('1.5')*mp.log(2)
    A=mp.sqrt(2); C=mp.log(2*mp.pi)-mp.digamma(omega)
    for eps in map(mp.mpf,['.0001','.000001']):
        native_increment=-G0(eps)+Q0(eps)
        physical_increment=-G0(eps)  # b+log(2)<2*b for the chosen b=1
        target_increment=c2prime*k0(eps)+c2*mp.diff(lambda w:kernel_beta(eps,w),omega)
        prediction=A/mp.sqrt(eps)*(c2*mp.log(eps)+c2prime+c2*C)
        check(f'arithmetic first-delay tangent eps={eps}',relative(target_increment,prediction),.001)
        check(f'b0 load first-delay tangent eps={eps}',abs(native_increment/mp.sqrt(eps)+2*mp.sqrt(2)),.07)
        check(f'b1 physical load first-delay tangent eps={eps}',abs(physical_increment/mp.sqrt(eps)+2*mp.sqrt(2)),.001)
        first_delay.append(dict(epsilon=mp.nstr(eps),load_increment_b0=mp.nstr(native_increment,24),
                                load_increment_b1=mp.nstr(physical_increment,24),
                                arithmetic_increment=mp.nstr(target_increment,24)))
    observations['first_prime_tangent']=first_delay

    roots=[]
    for guess in [14,21]:
        ordinate=mp.findroot(lambda t:mp.re(xi(mp.mpf('.5')+mp.j*t)),(guess-mp.mpf('.3'),guess+mp.mpf('.3')))
        rho=mp.mpf('.5')+mp.j*ordinate
        derivative=mp.diff(xi,rho)/xi(rho+1)
        required_clock=-mp.exp(rho)/(rho*derivative)
        eps=mp.mpf('1e-9')
        residue=mp.exp(rho)/(rho*derivative)
        check(f'sampled zero residual near {guess}',abs(xi(rho)),1e-35)
        check(f'load logarithmic pole residue near {guess}',relative(eps*tangent(rho+eps,1),residue),1e-7)
        check(f'pole clock cannot be real near {guess}',abs(mp.im(required_clock)),.01,'>=')
        roots.append(dict(root=complex_json(rho),required_real_clock_candidate=complex_json(required_clock),
                          xi_derivative_magnitude=mp.nstr(abs(mp.diff(xi,rho)),24)))
    observations['illustrative_pole_samples']=roots

    boundary=load_sibling('check_boundary_readout.py','boundary_readout_for_modular_check')
    brownian=load_sibling('check_brownian_readout.py','brownian_readout_for_modular_check')
    regressions=[]
    for w,u in [(mp.mpf('.25'),mp.mpf(1)),(mp.mpf('.4'),mp.mpf('.7')),(mp.mpf('.5'),mp.mpf('1.2'))]:
        expected=kernel_beta(u,w)
        numeric=boundary.target_kernel(float(u),float(w),n=100)
        high_precision=brownian.prime_free(u,w)
        check(f'corrected NumPy kernel versus beta omega={w},u={u}',relative(float(numeric),expected),1e-10)
        check(f'corrected mpmath kernel versus beta omega={w},u={u}',relative(high_precision,expected),1e-35)
        regressions.append(dict(omega=mp.nstr(w),u=mp.nstr(u),corrected=mp.nstr(expected,24)))
    observations['kernel_regressions']=regressions
    for w in map(mp.mpf,['.25','.4']):
        p=mp.mpf(2)
        def integrand(t):
            if not t:
                return (2*mp.pi)**w/(w*mp.gamma(w))
            u=t**(1/w)
            return mp.exp(-p*u)*kernel_beta(u,w)*t**(1/w-1)/w
        integral=mp.quad(integrand,[0,mp.mpf('.5'),1,2,mp.inf])
        check(f'general kernel independent Laplace check omega={w}',relative(integral,prime_free_symbol(p,w)),1e-30)

    siblings={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
              for name in ['check_boundary_readout.py','check_brownian_readout.py']}
    return dict(schema_version=1,date='2026-09-23',prepared_for='Edward Baker',
        model='GPT-6 (Codex; developer-provided identity)',effort='not exposed; not inferred',
        python=platform.python_version(),dependencies=dict(mpmath=mp.__version__,numpy=np.__version__),
        parameters=dict(decimal_precision=dps,refinement_digits=15,physical_cusp_position=1,
                        first_delay_omega='.5',norm_window=1),
        scope='Fixed-shift modular Hodge scattering and a specified real cusp-channel delta coupling; arithmetic shift-tangent exclusion, finite controls, and corrected-kernel regressions; no variable-shift physical realization or RH result',
        case_count=len(CASES),exact_rational_cases=sum(c['kind']=='exact rational' for c in CASES),
        all_pass=all(c['passed'] for c in CASES),cases=CASES,observations=observations,
        program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        corrected_sibling_sha256=siblings)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--dps',type=int,default=50)
    args=parser.parse_args()
    if args.dps<45:
        parser.error('Use at least 45 decimal digits for these thresholds.')
    result=run(args.dps)
    output=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(output)
        print(json.dumps(dict(case_count=result['case_count'],exact_rational_cases=result['exact_rational_cases'],
                              all_pass=result['all_pass'],output=str(args.output),failed=[c for c in CASES if not c['passed']])))
    else:
        print(output,end='')
    raise SystemExit(not result['all_pass'])


if __name__=='__main__':
    main()
