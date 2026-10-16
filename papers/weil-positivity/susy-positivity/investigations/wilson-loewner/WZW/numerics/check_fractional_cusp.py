#!/usr/bin/env python3
"""Continuous-exponent test of a fractional-memory modular radiation channel.

Independent Bessel-extension, positive relaxation, stable-delay, asymptotic,
and arithmetic-tangent controls. Requires mpmath; no external data, zero table,
or interval certification. Prepared for Edward Baker with GPT-6 (Codex),
23 September 2026; effort not exposed and not inferred.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import mpmath as mp


def xi(s):
    s=mp.mpc(s)
    if s in (0,1):
        return mp.mpf('.5')
    if s.real<mp.mpf('.5'):
        return xi(1-s)
    return s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)


def K(p):
    return xi(p)/xi(p+1)


def target(p,w):
    return xi(mp.mpf('.5')+p-w)/xi(mp.mpf('.5')+p+w)


def a_half(p):
    return mp.diff(xi,p)/xi(p)+mp.diff(xi,p+1)/xi(p+1)


def psi(p,beta):
    return 2*mp.pi*(p/(2*mp.pi))**beta


def response(p,beta):
    return K(psi(p,beta))


def extension(y,p,beta):
    if not y:
        return mp.mpf(1)
    z=mp.sqrt(p)*y
    return 2**(1-beta)/mp.gamma(beta)*z**beta*mp.besselk(beta,z)


def extension_prime(y,p,beta):
    z=mp.sqrt(p)*y
    return -2**(1-beta)/mp.gamma(beta)*mp.sqrt(p)*z**beta*mp.besselk(beta-1,z)


def flux_constant(beta):
    return 2**(1-2*beta)*mp.gamma(1-beta)/mp.gamma(beta)


def relaxation_integral(p,beta):
    pref=(2*mp.pi)**(1-beta)*mp.sin(mp.pi*beta)/mp.pi
    return pref*mp.quad(lambda t:mp.exp(beta*t)*p/(p+mp.exp(t)),[-mp.inf,-1,0,1,mp.inf])


def half_clock_density(v,u):
    return v/(mp.sqrt(2)*u**mp.mpf('1.5'))*mp.exp(-mp.pi*v*v/(2*u))


def regularized_k0(t):
    # 2*t*k0(t*t), analytically extended to t=0.
    r=t*t
    ratio=-mp.expm1(-2*r)/(2*r) if r else mp.mpf(1)
    return 2*mp.sqrt(2)*(2*mp.exp(-2*r)-1)/mp.sqrt(ratio)


def first_prime_native(u):
    ell=mp.log(2)
    return mp.quad(lambda t:regularized_k0(t)*half_clock_density(t*t+ell,u)/2,
                   [0,mp.mpf('.5'),1,2,mp.inf])


def prime_free(u,w):
    z=-mp.expm1(-2*u)
    return 2*mp.pi**w/mp.gamma(w)*(mp.exp(-(mp.mpf('2.5')-w)*u)*z**(w-1)
        -w*mp.exp((mp.mpf('.5')-w)*u)*mp.betainc(w,mp.mpf('1.5')-w,0,z))


def native_tangent(p):
    return p*mp.log(p/(2*mp.pi))*mp.diff(K,p)/K(p)


def repr_number(z):
    z=mp.mpc(z)
    if not z.imag:
        return mp.nstr(z.real,24)
    return dict(real=mp.nstr(z.real,24),imag=mp.nstr(z.imag,24))


def run(dps):
    mp.mp.dps=dps
    cases=[];observations={}
    def check(name,value,threshold,comparison='<='):
        value,threshold=float(value),float(threshold)
        cases.append(dict(name=name,value=value,threshold=threshold,comparison=comparison,
            passed=math.isfinite(value) and (value<=threshold if comparison=='<=' else value>=threshold)))
    def relative(x,y):
        return abs(x-y)/max(1,abs(y))

    # Genuine scale and integer field controls do not change the front exponent.
    p=mp.mpf('1e7')
    for scale in map(mp.mpf,['.5','1','2']):
        f=lambda z:K(z/scale)
        exponent=-p*mp.diff(f,p)/f(p)
        check(f'uniform scale fixed exponent scale={scale}',abs(exponent-mp.mpf('.5')),1e-5)
    for order in [1,2,3]:
        def raised(z):
            return K(z)*mp.fprod((z-(2*j+1))/(z+(2*j+1)) for j in range(1,order))
        check(f'integer raising fixed exponent order={order}',abs(-p*mp.diff(raised,p)/raised(p)-mp.mpf('.5')),1e-5)
        z=mp.mpc(3,2);s=(z+1)/2
        phi=mp.sqrt(mp.pi)*mp.gamma(z/2)/mp.gamma((z+1)/2)*mp.zeta(z)/mp.zeta(z+1)
        coefficient=(-1)**order*mp.rf(1-s,order)/mp.rf(s,order)*phi
        check(f'raising product versus constant term order={order}',relative(coefficient,raised(z)),1e-35)

    # Local weighted diffusion, independently solved by Bessel functions.
    extension_values=[]
    for beta in map(mp.mpf,['.25','.5','.75']):
        z=mp.mpc(2,1);y=mp.mpf('.7')
        W=lambda x:extension(x,z,beta)
        check(f'Bessel extension ODE beta={beta}',abs(mp.diff(W,y,2)+(1-2*beta)/y*mp.diff(W,y)-z*W(y)),1e-35)
        check(f'Bessel derivative identity beta={beta}',relative(mp.diff(W,y),extension_prime(y,z,beta)),1e-35)
        small=mp.mpf('1e-16')
        computed=-small**(1-2*beta)*extension_prime(small,z,beta)/flux_constant(beta)
        check(f'boundary flux gives fractional power beta={beta}',relative(computed,z**beta),1e-7)
        check(f'positive relaxation representation beta={beta}',relative(relaxation_integral(z,beta),psi(z,beta)),1e-35)
        extension_values.append(dict(beta=str(beta),boundary_flux=repr_number(computed),power=repr_number(z**beta)))
    observations['extension_flux']=extension_values

    # One independent bulk-energy quadrature, away from the singular boundary.
    beta=mp.mpf('.5');z=mp.mpc(2,1);eps=mp.mpf('.01')
    c=(2*mp.pi)**(1-beta)/flux_constant(beta)
    boundary=-c*eps**(1-2*beta)*mp.conj(extension(eps,z,beta))*extension_prime(eps,z,beta)
    bulk=c*mp.quad(lambda y:y**(1-2*beta)*(abs(extension_prime(y,z,beta))**2
                        +mp.re(z)*abs(extension(y,z,beta))**2),[eps,1,3,mp.inf])
    check('weighted diffusion bulk energy versus boundary supply',relative(bulk,mp.re(boundary)),1e-35)
    observations['extension_energy_control']=dict(boundary_real_supply=repr_number(mp.re(boundary)),bulk=repr_number(bulk))

    fronts=[]
    for beta in map(mp.mpf,['.5','.8','1']):
        p=mp.mpf('1e10');w=beta/2
        leading=(2*mp.pi/p)**w
        native=response(p,beta);desired=target(p,w)
        check(f'fractional response leading amplitude beta={beta}',relative(native/leading,1),1e-4)
        check(f'arithmetic response leading amplitude omega={w}',relative(desired/leading,1),1e-7)
        exponent=-p*mp.diff(lambda q:response(q,beta),p)/native
        check(f'continuous front exponent beta={beta}',abs(exponent-w),1e-4)
        fronts.append(dict(beta=str(beta),native_exponent=repr_number(exponent),required_exponent=str(w),native_scaled=repr_number(native/leading)))
    observations['fronts']=fronts
    subleading=[]
    for beta in map(mp.mpf,['.5','.8']):
        p=mp.mpf('1e10');leading=(2*mp.pi/p)**(beta/2)
        native=(response(p,beta)/leading-1)*p**beta
        desired=(target(p,beta/2)/leading-1)*p
        native_limit=-mp.mpf('1.75')*(2*mp.pi)**(beta-1)
        desired_limit=-mp.mpf('1.75')*beta
        check(f'native subleading fractional power beta={beta}',relative(native,native_limit),1e-4)
        check(f'arithmetic subleading integer power beta={beta}',relative(desired,desired_limit),1e-7)
        subleading.append(dict(beta=str(beta),native_scaled=repr_number(native),native_limit=repr_number(native_limit),arithmetic_scaled=repr_number(desired),arithmetic_limit=repr_number(desired_limit)))
    observations['incompatible_subleading_powers']=subleading
    for p in [mp.mpf(2),mp.mpc(1,3)]:
        check(f'original channel recovered beta1 p={p}',relative(response(p,1),K(p)),1e-35)

    boundary_values=[]
    for beta in map(mp.mpf,['.5','.8']):
        for nu in [1,5,20]:
            p=mp.j*nu;value=response(p,beta);expected=target(p,beta/2)
            check(f'strict boundary attenuation beta={beta},nu={nu}',1-abs(value),.001,'>=')
            check(f'arithmetic boundary modulus beta={beta},nu={nu}',abs(abs(expected)-1),1e-35)
            boundary_values.append(dict(beta=str(beta),nu=nu,native_modulus=repr_number(abs(value)),arithmetic_modulus=repr_number(abs(expected))))
    observations['boundary_moduli']=boundary_values

    tangents=[]
    for p in map(mp.mpf,[2,4,8]):
        analytic=native_tangent(p);numeric=mp.diff(lambda b:mp.log(response(p,b)),1)
        required=-a_half(p)/2
        check(f'fractional parameter derivative p={p}',relative(analytic,numeric),1e-35)
        check(f'arithmetic parameter tangent mismatch p={p}',abs(analytic-required),.02,'>=')
        tangents.append(dict(p=str(p),native=repr_number(analytic),required=repr_number(required)))
    observations['tangents']=tangents
    p=mp.mpf('1e8');leading=-mp.log(p/(2*mp.pi))/2
    check('native tangent passes leading logarithm',relative(native_tangent(p),leading),1e-6)
    check('arithmetic tangent passes leading logarithm',relative(-a_half(p)/2,leading),1e-6)

    # Stable clock at beta=1/2 has an explicit Gaussian first-passage density.
    ell=mp.log(2)
    for p in [mp.mpf(2),mp.mpc(2,1)]:
        value=mp.sqrt(2)*ell*mp.quad(lambda t:mp.exp(-mp.pi*ell*ell*t*t/2-p/(t*t)),[0,1,3,mp.inf])
        check(f'stable density Laplace p={p}',relative(value,mp.exp(-ell*psi(p,mp.mpf('.5')))),1e-35)
    mass=mp.sqrt(2)*ell*mp.quad(lambda t:mp.exp(-mp.pi*ell*ell*t*t/2),[0,1,3,mp.inf])
    check('stable delay density normalized',abs(mass-1),1e-35)
    u=mp.mpf('.5')
    early=mp.sqrt(2)*ell*mp.quad(lambda t:mp.exp(-mp.pi*ell*ell*t*t/2),[1/mp.sqrt(u),3,mp.inf])
    exact=mp.erfc(ell*mp.sqrt(mp.pi/(2*u)))
    check('early delay probability versus erfc',relative(early,exact),1e-35)
    check('positive probability before original first delay',early,.08,'>=')
    observations['early_delay_probability']=repr_number(early)
    for u in map(mp.mpf,['.25','.5']):
        val=first_prime_native(u)
        check(f'first prime sector nonzero before log2 u={u}',val,.06,'>=')

    delays=[];w=mp.mpf('.25');c2=(2**w-2**(-w))/mp.sqrt(2)
    expected=c2*(2*mp.pi)**w/mp.gamma(w)
    for eps in map(mp.mpf,['.0001','.000001']):
        native=first_prime_native(ell+eps);arithmetic=c2*prime_free(eps,w)
        check(f'arithmetic delayed singular coefficient eps={eps}',abs(eps**(1-w)*arithmetic-expected),.00005)
        check(f'fractional native first delay stays bounded eps={eps}',abs(native),.2)
        check(f'native scaled first delay vanishes eps={eps}',abs(eps**(1-w)*native),.0002)
        delays.append(dict(epsilon=str(eps),native=repr_number(native),arithmetic=repr_number(arithmetic),native_scaled=repr_number(eps**(1-w)*native),arithmetic_scaled=repr_number(eps**(1-w)*arithmetic)))
    observations['first_prime_comparison']=delays
    with mp.workdps(dps+15):
        refined=first_prime_native(mp.log(2)+mp.mpf('.0001'))
    check('first prime integral precision refinement',relative(mp.mpf(delays[0]['native']),refined),1e-22)

    # Euler-coefficient tangent after removing the common archimedean part.
    p=mp.mpf(4)
    native_coefficient=-ell*p*mp.log(p/(2*mp.pi))/2
    native_diff=mp.diff(lambda b:mp.exp(-ell*psi(p,b))/2,1)/mp.exp(-ell*p)
    arithmetic_diff=mp.diff(lambda b:(2**(b/2)-2**(-b/2))/mp.sqrt(2),1)
    check('first Euler tangent native derivative',relative(native_coefficient,native_diff),1e-35)
    check('first Euler tangent arithmetic derivative',relative(arithmetic_diff,mp.mpf('.75')*ell),1e-35)
    check('first Euler tangent coefficients disagree',abs(native_coefficient-arithmetic_diff),.05,'>=')
    observations['first_euler_tangent']=dict(p=str(p),native=repr_number(native_coefficient),arithmetic=repr_number(arithmetic_diff))

    # xi'(1)/xi(1) is available in closed form, with no differentiation at a pole.
    kp0=mp.log(4*mp.pi)-2-mp.euler
    low=[]
    for small in map(mp.mpf,['1e-8','1e-12']):
        coefficient=(response(small,mp.mpf('.5'))-1)/mp.sqrt(small)
        expected=kp0*mp.sqrt(2*mp.pi)
        check(f'low frequency fractional branch coefficient p={small}',abs(coefficient-expected),1e-5)
        low.append(dict(p=str(small),fractional_coefficient=repr_number(coefficient)))
    observations['low_frequency_branch']=low
    endpoint=K(2*mp.pi)
    check('zero order limit is not identity',1-mp.re(endpoint),.2,'>=')
    check('small beta approaches nonidentity limit',abs(response(2,mp.mpf('1e-7'))-endpoint),1e-7)
    observations['zero_order_limit']=repr_number(endpoint)

    # General complete Bernstein clock boundary real part, beyond powers.
    frequency=mp.mpf(3);a=mp.mpf('.2');b=mp.mpf('.7')
    atoms=[(mp.mpf('.4'),mp.mpf('.5')),(mp.mpf('1.2'),mp.mpf(2))]
    clock=lambda p:a+b*p+sum(weight*p/(p+rate) for weight,rate in atoms)
    positive=a+sum(weight*frequency**2/(rate**2+frequency**2) for weight,rate in atoms)
    check('complete Bernstein boundary dissipation identity',abs(mp.re(clock(mp.j*frequency))-positive),1e-35)
    check('general nontrivial memory clock loses boundary modulus',1-abs(K(clock(mp.j*frequency))),.01,'>=')

    observations['finite_transfer_comparison']=[dict(beta=str(b),p=p,native=repr_number(response(p,b)),arithmetic=repr_number(target(p,b/2))) for b in map(mp.mpf,['.5','.8']) for p in [2,4,8]]
    return dict(schema_version=1,date='2026-09-23',prepared_for='Edward Baker',
        model='GPT-6 (Codex; developer-provided identity)',effort='not exposed; not inferred',
        scope='Specified fractional-memory modular channel passes continuous front exponent but fails arithmetic transfer; limited geometry/raising controls and complete-Bernstein clock exclusion; no general deformation no-go or RH result',
        python=platform.python_version(),dependencies={'mpmath':mp.__version__},parameters={'decimal_precision':dps,'refinement_digits':15,'clock_scale':'2*pi','beta_values':['.5','.8','1'],'arithmetic_clock':'omega=beta/2'},
        case_count=len(cases),exact_rational_cases=0,all_pass=all(c['passed'] for c in cases),cases=cases,observations=observations,
        program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--dps',type=int,default=50)
    args=parser.parse_args()
    if args.dps<45:parser.error('Use at least 45 decimal digits.')
    result=run(args.dps)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        print(json.dumps({'case_count':result['case_count'],'all_pass':result['all_pass'],'failed':[c for c in result['cases'] if not c['passed']],'output':str(args.output)}))
    else:print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(not result['all_pass'])


if __name__=='__main__':main()
