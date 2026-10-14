#!/usr/bin/env python3
"""Exact finite-sum and paid selected-point diagnostics for investigation 21.

2026-10-14, prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra, effort ultra. All decisions use Arb/Acb balls.
The finite sum is exactly Note16's arithmetic integrand at its saddle.
It is not an approximation to the complete theta function without further
integration and error estimates. No rectangle or arbitrary-height claim.
Place beside check_shifted_contour_payments.py, or expose it on PYTHONPATH.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform
import time

import flint
from flint import arb,acb,acb_series,ctx
import check_shifted_contour_payments as source


def require(condition,message):
    if not condition: raise RuntimeError(message)


def real(q):
    q=Fraction(q);return arb(q.numerator)/q.denominator


def enc(z): return source.enc(z)


def cenc(z): return {'real':enc(z.real),'imag':enc(z.imag)}


def phi_one(z):
    p=arb.pi()
    return (2*p*p*(9*z).exp()-3*p*(5*z).exp())*(-p*(4*z).exp()).exp()


def shared(x,theta):
    a=arb.pi()/16;t=real(theta)/x.log()
    b=((x+2*t*a)/(4*arb.pi()*(4*a).sin())).log()/4
    cutoff=(2*b).exp();N=int(float(cutoff))
    require(arb(N)<=cutoff and cutoff<arb(N+1),'certified staircase cutoff')
    require(0<=t<=arb(1)/2,'selected point in threshold time range')
    D=[acb(0) for _ in range(4)];diagonals=[arb(0),arb(0)];weights=[]
    for n in range(1,N+1):
        ln=arb(n).log();d=ln/2;nu=b-d
        weight=(-ln/2+t*d*d-2*t*d*acb(b,a)-acb(0,x*d)).exp()
        q=acb(-a,nu)
        for j in range(4):D[j]+=weight*q**j
        diagonals[0]+=abs(weight)**2*nu**2
        diagonals[1]+=abs(weight)**2*nu**2*(a*a+nu*nu)
        weights.append(weight)
    z=acb(b,a);carrier=(t*z*z+acb(0,x*b)).exp()*phi_one(z)
    require(abs(carrier)>0,'nonzero carrier at diagnostic point')
    unit=carrier/abs(carrier);p=[(unit*d).real for d in D]
    forms=[]
    for j in range(2):
        Hermitian=abs(D[j+1])**2-(D[j]*D[j+2].conjugate()).real
        Wronskian=D[j+1]**2-D[j]*D[j+2]
        margin=Hermitian-abs(Wronskian)
        L=p[j+1]**2-p[j]*p[j+2]
        identity=2*L-Hermitian-(unit*unit*Wronskian).real
        require(identity.contains(0),'exact Hermitian projection identity')
        forms.append({'j':j,'Hermitian':enc(Hermitian),'Wronskian':cenc(Wronskian),'phase_free_margin_H_minus_abs_W':enc(margin),'strictly_negative_margin':bool(margin<0),'actual_carrier_phase_form':enc(L),'strictly_negative_actual_carrier_form':bool(L<0),'diagonal_sum':enc(diagonals[j]),'complete_cross_sum':enc(L-diagonals[j])})
    return {'x':enc(x),'theta':str(theta),'t':enc(t),'a':enc(a),'b':enc(b),'N':N,'D':[cenc(d) for d in D],'carrier_unit':cenc(unit),'forms':forms,'absolute_weight_sum':enc(sum(abs(w) for w in weights))}


def full_diagnostics(x,t,jets,method):
    E=jets[0]**2+jets[1]**2
    require(E>0,'selected point norm enclosure separated from zero')
    a=arb.pi()/8-1/x
    b=((x+2*t*a)/(4*arb.pi()*(4*a).sin())).log()/4
    mu=a*a+b*b;C=[-jets[j+2]-2*a*jets[j+1]-mu*jets[j] for j in range(2)]
    omega=(x/(4*arb.pi())).log()/4
    return {'x':enc(x),'t':enc(t),'method':method,'normalized_jets':[enc(z) for z in jets],'norm_squared':enc(E),'a':enc(a),'b':enc(b),'mu':enc(mu),'normalized_L_over_omega2_E':[enc((jets[j+1]**2-jets[j]*jets[j+2])/(omega*omega*E)) for j in range(2)],'C_squared_over_mu_squared_E':enc((C[0]**2+C[1]**2)/(mu*mu*E)),'stationarity_checked':False}


def exact_zero_time(x):
    ctx.prec=256;ctx.cap=4
    s=acb_series([acb(arb(1)/2,x/2),acb(0,arb(1)/2)],4)
    xi_over_8=s*(s-1)*(-(s/2)*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()/16
    scale=(arb.pi()*x/8).exp();values=[xi_over_8[k]*factorial(k)*scale for k in range(4)]
    require(all(v.imag.contains(0) for v in values),'reality of completed zeta jets')
    return full_diagnostics(x,arb(0),[v.real for v in values],'Acb power series of xi(1/2+ix/2)/8')


def paid_heated(x,theta,bits,N):
    ctx.prec=bits;t=real(theta)/x.log();a=arb.pi()/16;U=arb(3)/2;tau=arb(1)/2
    scale=((arb.pi()/8-a)*x).exp();tol=arb(2)**(-(bits-64));jets=[];payments=[]
    for j in range(4):
        retained=source.finite_integral(j,a,N,U,t,x,tol)
        index=source.index_payment(j,a,N,tau)[0]
        integration=source.integration_payment(j,a,U,tau)[0]
        jets.append(scale*(retained+source.symmetric(index+integration)))
        payments.append({'j':j,'normalized_quadrature_radius':enc(scale*retained.rad()),'normalized_index_payment':enc(scale*index),'normalized_integration_payment':enc(scale*integration)})
    row=full_diagnostics(x,t,jets,'validated complete-source shifted quadrature plus both omitted-domain payments')
    row.update({'theta':str(theta),'bits':bits,'source_contour_a':enc(a),'N':N,'U':'3/2','payments':payments})
    return row


def staircase_rows():
    rows=[];a=arb.pi()/16
    for n in (4,10,100):
        theta=arb(1);base=4*arb.pi()*(4*a).sin()*n*n;x=base
        for _ in range(12):x=base-2*a*theta/x.log()
        displacement=x/100000000
        left=shared(x-displacement,1);right=shared(x+displacement,1)
        require(left['N']==n-1 and right['N']==n,'verified neighboring staircase indices')
        # Exactly at v=d_n, the following identity needs no approximation to
        # the implicit transition height. It is true for every x,t.
        t=theta/x.log();d=arb(n).log()/2;z=acb(d,a)
        weight=(-arb(n).log()/2+t*d*d-2*t*d*z-acb(0,x*d)).exp()
        carrier=(t*z*z+acb(0,x*d)).exp()*phi_one(z)
        alpha=arb.pi()*n*n
        phi_n=(2*alpha*alpha*acb(0,9*a).exp()-3*alpha*acb(0,5*a).exp())*(-alpha*acb(0,4*a).exp()).exp()
        expected=(-t*a*a).exp()*phi_n
        for j in range(4):
            difference=carrier*weight*(-a)**j-expected*(-a)**j
            require(difference.real.contains(0) and difference.imag.contains(0),'staircase carrier/phase jump cancellation')
        rows.append({'n':n,'transition_height_approximation':enc(x),'left':left,'right':right,'jump_identity':'carrier(d_n) A_n(d_n) (-a)^j = exp(-t*a²) phi_n(i*a) (-a)^j; external exp(-a*x) omitted on both sides','jump_checks_passed':4})
    return rows


def perturbation_bounds():
    # Coefficient dictionaries expand the relevant polynomials exactly.
    def add(a,b):
        out=a.copy()
        for m,c in b.items():out[m]=out.get(m,0)+c
        return {m:c for m,c in out.items() if c}
    def scale(a,c):return {m:v*c for m,v in a.items() if v*c}
    def mul(a,b):
        out={}
        for m,c in a.items():
            for n,d in b.items():
                key=tuple(sorted(m+n));out[key]=out.get(key,0)+c*d
        return {m:c for m,c in out.items() if c}
    def variable(s):return {(s,):Fraction(1)}
    c,s,e0,e1,e2,e3=map(variable,['c','s','e0','e1','e2','e3'])
    p=[add(c,e0),add(scale(s,-1),e1),add(scale(c,-1),e2),add(s,e3)]
    circle=add(mul(c,c),mul(s,s))
    first=add(add(add(add(add(circle,scale(mul(s,e1),-2)),mul(e1,e1)),scale(mul(c,e2),-1)),mul(c,e0)),scale(mul(e0,e2),-1))
    second=add(add(add(add(add(circle,scale(mul(c,e2),-2)),mul(e2,e2)),mul(s,e3)),scale(mul(s,e1),-1)),scale(mul(e1,e3),-1))
    norm=add(add(add(add(circle,scale(mul(c,e0),2)),scale(mul(s,e1),-2)),mul(e0,e0)),mul(e1,e1))
    require(add(mul(p[1],p[1]),scale(mul(p[0],p[2]),-1))==first,'first perturbation polynomial')
    require(add(mul(p[2],p[2]),scale(mul(p[1],p[3]),-1))==second,'second perturbation polynomial')
    require(add(mul(p[0],p[0]),mul(p[1],p[1]))==norm,'norm perturbation polynomial')
    delta=Fraction(1,8);signed=1-4*delta-delta*delta;norm_bound=1-4*delta
    require(signed==Fraction(31,64) and norm_bound==Fraction(1,2),'exact delta=1/8 constants')
    return {'exact_polynomial_checks':3,'hypotheses':'c²+s²=1, |e_j|<=delta','argument':'Each linear error has absolute bound <=4delta because |c|,|s|<=1; keep the positive error square and pay the single negative error product by delta². The norm has positive error squares and linear loss <=4delta.','signed_lower_bound':'1-4delta-delta²','norm_lower_bound':'1-4delta','delta':'1/8','signed_lower_at_delta':str(signed),'norm_lower_at_delta':str(norm_bound)}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',required=True,type=Path);args=ap.parse_args()
    started=time.monotonic();ctx.prec=192
    selected=[('200',1),('211',1),('1000',1),('48987/10',2),('1000000',1)]
    shared_rows=[shared(real(x),theta) for x,theta in selected]
    require(shared_rows[1]['forms'][0]['strictly_negative_margin'],'x211 phase-free cone counterexample')
    require(shared_rows[3]['forms'][0]['strictly_negative_margin'],'x4898.7 phase-free cone counterexample')
    require(shared_rows[3]['forms'][0]['strictly_negative_actual_carrier_form'],'x4898.7 actual-carrier pointwise integrand obstruction')
    jumps=staircase_rows();perturbation=perturbation_bounds()
    zero_rows=[exact_zero_time(real(x)) for x in ('200','211','1000','1000000')]
    heated=[]
    for x,theta,bits,N in [('211',1,256,8),('1000',1,512,12)]:
        heated.append(paid_heated(real(x),theta,bits,N));print('paid point',x,'elapsed',round(time.monotonic()-started,3),flush=True)
    record={'schema':'inv21_shared_arithmetic_diagnostics_v1','date':'2026-10-14','prepared_for':'Edward Baker','llm_assistance':'Substantial','recorded_model':'gpt-6-astra','recorded_effort':'ultra','runtime':{'python':platform.python_version(),'python_flint':flint.__version__},'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'imported_source_name':Path(source.__file__).name,'imported_source_sha256':sha256(Path(source.__file__).read_bytes()).hexdigest(),'status':'PASS','scope':'Exact finite arithmetic-sum counterexamples, staircase algebra checks, and selected complete-source point enclosures. No height-cover or all-height assertion.','theta_convention':'theta=t*log(x), as in Note16; convert explicitly when comparing a theorem using t*log(x/(4pi))','common_sum_definition':'D_j=sum_(n<=exp(2b)) n^(-1/2) exp(t*d_n²-2t*d_n*(b+ia)-i*x*d_n) (-a+i*(b-d_n))^j; a=pi/16, b=log((x+2ta)/(4pi sin4a))/4','hermitian_identity':'2 L_j(Re(exp(i*phase)D))=H_j+Re(exp(2i*phase)W_j)','shared_arithmetic':shared_rows,'staircase_transitions':jumps,'zero_time_complete_jets':zero_rows,'paid_heated_complete_jets':heated,'four_jet_perturbation_bounds':perturbation,'endpoint_cancellation_observation':'The full carrier cancels every exp(-i*x*d_n) staircase jump phase. After summing every index, g_j(z)=(iz)^j exp(tz²)Phi(z) satisfies conjugate(g_j^(r)(ia))=(-1)^r g_j^(r)(ia), so every inverse-x boundary coefficient i^(-r-1)g_j^(r)(ia) has zero real part. This is an analytic consequence of complete-source evenness, not a numerical proof of an all-height sign.','limitations':['The shared arithmetic sum is an exact integrand object; its forms are not the complete integrated theta Laguerre forms.','Failure of the all-phase integrand cone does not contradict positivity using the actual carrier and integration.','All counterexamples use theta=1 or2 and do not contradict an outer-region theorem with theta>=4+epsilon.','Paid complete-source points do not establish stationarity, rectangle coverage, or uniform relative errors.'],'elapsed_seconds':time.monotonic()-started}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print('PASS',args.output,'seconds',record['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
