#!/usr/bin/env python3
"""Independent shifted-channel Lipschitz-payment obstruction, no source quadrature.
Prepared for Edward Baker with substantial LLM assistance; same-model internal work.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, acb, acb_series, ctx

def A(v):
    return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def interval(lo,hi):
    lo,hi=A(lo),A(hi)
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def out(x): return x.str(45,more=True)
def check(b,msg):
    if not b: raise ArithmeticError(msg)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(bits):
    ctx.prec=bits;ctx.cap=8
    pi=arb.pi();ii=acb(0,1);t=A(F(21,200));x=A(1000)
    z=acb_series([acb(x),acb(1)],4);s=(1-ii*z)/2
    def m0(s):
        return s.log()+(s-1).log()-s*pi.log()/2+(2*pi).log()/2-A(16).log()+(s/2-A(F(1,2)))*(s/2).log()-s/2
    def alpha(s):
        return 1/(2*s)+1/(s-1)+(s/(2*pi)).log()/2
    def mt(s): return m0(s)+t*alpha(s)**2/4
    logA=(mt(s)+mt(1-s))/2;theta=(mt(s)-mt(1-s))/(2*ii)
    def real_cs(q,n):
        c=q[n];check(c.imag.contains(0),'real symmetry coefficient')
        return c.real
    logA0=real_cs(logA,0);b=real_cs(logA,1);bx=2*real_cs(logA,2);bxx=6*real_cs(logA,3)
    w=real_cs(theta,1);wx=2*real_cs(theta,2);wxx=6*real_cs(theta,3)
    check(w<0,'signed omega')
    mu=wx/w;mux=wxx/w-mu*mu
    d=pi/8-4*x.log()/x;c=(4*d).cos()
    check(d>0 and d<pi/8 and c>0,'contour admissibility')
    u=interval(F(59,100),F(3,5));zeta=acb(u,d);v=ii*zeta-b
    Gamma=v*v-bx-mu*v+w*w
    Gamma_x=-2*bx*v-bxx-mux*v+mu*bx+2*w*wx
    derivative_multiplier=(v-ii*w-mu)*Gamma+Gamma_x
    multiplier_lower=abs(derivative_multiplier).lower()
    check(multiplier_lower>0,'positive filtered-kernel derivative multiplier')
    # Avoid all oscillatory phase images. Reverse triangle for theta square 1,
    # followed by ordinary triangle for the retained squares 2,...,11.
    phi1_lower=((2*pi*pi*(9*u).exp()-3*pi*(5*u).exp())*(-pi*c*(4*u).exp()).exp()).lower()
    check(phi1_lower>0,'first theta square dominates its polynomial prefactor')
    rest_upper=arb(0)
    rest=[]
    for j in range(2,12):
        lam=pi*j*j
        term=((2*lam*lam*(9*u).exp()+3*lam*(5*u).exp())*(-lam*c*(4*u).exp()).exp()).upper()
        rest.append({'j':j,'bound_upper':out(term)})
        rest_upper+=term
    rest_upper=rest_upper.upper();phi_lower=(phi1_lower-rest_upper).lower()
    check(phi_lower>0,'retained theta square sum lower bound')
    # |P exp(t zeta^2+i x zeta)| = exp(t(u^2-d^2)-xd-log A)/|omega|.
    # Explicit positive u interval makes u*u an exact valid real range.
    positive_scale=((t*(u*u-d*d)-x*d-logA0).exp()/abs(w)).lower()
    kernel_derivative_lower=(positive_scale*phi_lower*multiplier_lower).lower()
    check(kernel_derivative_lower>0,'positive plus-channel derivative lower bound')
    # Full real-slice finite source is (Kplus+Kminus)/2. A rule that pays
    # channels separately owes at least one half of the plus-channel norm.
    source_Mx_lower=(A(F(1,2))*A(F(1,100))*kernel_derivative_lower).lower()
    # Separately differentiate the normalized filtered plus-channel series
    # at exact source nodes; the proof is the displayed product rule.
    series_checks=[]
    ws=theta.derivative();bs=logA.derivative();mus=ws.derivative()/ws
    for uu in (F(59,100),F(119,200),F(3,5)):
        zz=acb(A(uu),d);vv=ii*zz-bs
        GS=vv*vv-bs.derivative()-mus*vv+ws*ws
        PS=(-ii*theta-logA).exp()/ws
        phi=acb(0)
        for jj in range(1,12):
            lam=pi*jj*jj
            phi+=(2*lam*lam*(9*zz).exp()-3*lam*(5*zz).exp())*(-lam*(4*zz).exp()).exp()
        KS=(t*zz*zz+ii*z*zz).exp()*phi
        GS0=(ii*zz-b)**2-bx-mu*(ii*zz-b)+w*w
        GSx=-2*bx*(ii*zz-b)-bxx-mux*(ii*zz-b)+mu*bx+2*w*wx
        expected=(PS*KS)[0]*((ii*zz-b-ii*w-mu)*GS0+GSx)
        diff=(PS*KS*GS)[1]-expected
        check(diff.contains(0),'direct normalized filtered series derivative')
        series_checks.append({'u':str(uu),'difference':out(diff),'contains_zero':True})
    h=A(F(1,64));midpoint_lipschitz_payment_lower=(h*h*source_Mx_lower/4).lower()
    range_lipschitz_payment_lower=(h*h*source_Mx_lower/2).lower()
    check(midpoint_lipschitz_payment_lower>A('0.827470'),'one-cell payment fails analytic-only comparator')
    return {'bits':bits,'point':{'t':'21/200','x':'1000'},'closed_u_interval':['59/100','3/5'],
      'contour':{'d':out(d),'cos_4d':out(c),'source_m':12,'source_U':2},
      'phase':{'b':out(b),'b_x':out(bx),'b_xx':out(bxx),'omega':out(w),'omega_x':out(wx),'omega_xx':out(wxx),'mu':out(mu),'mu_x':out(mux)},
      'positive_branch_source_bound':{'phi_1_prefactor_and_decay_lower':out(phi1_lower),'remaining_squares_2_through_11_upper':out(rest_upper),'retained_source_modulus_lower':out(phi_lower),'other_square_bounds':rest},
      'filtered_derivative_bound':{'multiplier':out(derivative_multiplier),'multiplier_abs_lower':out(multiplier_lower),'positive_exponential_scale_lower':out(positive_scale),'plus_channel_integrand_modulus_lower':out(kernel_derivative_lower),'real_source_channel_triangle_Mx_lower':out(source_Mx_lower)},
      'independent_series_derivative_checks':series_checks,
      'payments':{'spatial_cell_width':'1/64','cell_with_witness_as_boundary':['63999/64','1000'],'midpoint_h_squared_Mx_over_4_lower':out(midpoint_lipschitz_payment_lower),'range_h_squared_Mx_over_2_lower':out(range_lipschitz_payment_lower),'analytic_only_endpoint_allowance_upper':'0.827470','source_informed_endpoint_allowance_upper':'0.002011747','source_informed_correlated_allowance_upper':'0.000266448','fails_all_three_retained_comparators':True},
      'tail_scope':'This is a lower bound on an assigned nonnegative retained-kernel variation payment. Omitted squares j>=12, retained u>2, arithmetic evaluation, parameter-time variation and rounding can only increase the prescribed complete sum; none is asserted to vanish or included in the positive retained-source lower bound.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--model',required=True);p.add_argument('--effort',required=True);p.add_argument('--bits',type=int,nargs='+',default=[192,256]);a=p.parse_args()
    data={'date':'2026-10-19','prepared_for':'Edward Baker','actual_model':a.model,'actual_effort':a.effort,'llm_assistance':'substantial; independent delegated derivation and interval check, same-model internal evidence','python':platform.python_version(),'python_flint':flint.__version__,'status':'Scoped failure of shifted-channel absolute parameter-variation payments, even when zero-order discrepancy is kept signed. Not a residual lower bound.','source_quadrature_performed':False,'source_jets_or_old_residual_polynomial_used':False,'runs':[run(b)for b in a.bits]}
    inv=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
    paths=[inv/'symmetries/03_normalized_jet_rotation/notes/03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md',inv/'numerics/high_height_consumer/high_height_consumer.py']
    data['script_sha256']=sha(__file__)
    data['source_sha256']={str(v):sha(a.repo/v) for v in paths}
    a.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'output':str(a.output),'payment_lower':[r['payments']['midpoint_h_squared_Mx_over_4_lower']for r in data['runs']]}))
if __name__=='__main__':main()
