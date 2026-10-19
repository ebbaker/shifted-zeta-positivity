#!/usr/bin/env python3
"""S03 bounded complete fixed-cutoff direct/transport comparison.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Authoring model/effort: gpt-6.1-sol / ultra (same-model internal work).
No theorem beyond imported S02 analytic contract is asserted by this checker.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import time
import flint
from flint import arb, acb, acb_series, ctx


def check(ok,message):
    if not ok: raise ArithmeticError(message)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def out(x):return x.str(38,more=True)
def A(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def interval(lo,hi):
    lo,hi=A(lo),A(hi)
    return arb((lo+hi)/2,((hi-lo)/2).upper())


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--s02-record',type=Path)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    args=p.parse_args();ctx.prec=args.bits;started=time.monotonic()
    base=args.repo/'papers/investigations-3/11_arithmetic_collision_rigidity'
    s02=base/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py'
    rec=args.s02_record or s02.with_name('S02_CUTOFF_REFLECTION_192_20261018.json')
    d=json.loads(rec.read_text());check(d['script_sha256']==sha(s02),'S02 script pin mismatch')
    for path,pin in d['source_sha256'].items():
        check(sha(args.repo/path)==pin,'S02 source pin mismatch: '+path)
    spec=importlib.util.spec_from_file_location('s02_fixed_cutoff',s02)
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    eta=A(d['reference_box']['eta_candidate']).upper();radius=A(F(1,2))
    nt=32;nx=128
    def phase_jet(x,t):
        s=(1-acb(0,1)*acb(x))/2
        mp=lambda v:old.alpha(v)*(1+t*old.alphap(v)/2)
        mpp=lambda v:old.alphap(v)*(1+t*old.alphap(v)/2)+t*old.alpha(v)*old.alphapp(v)/2
        theta=((old.mt(s,t)-old.mt(1-s,t))/(2*acb(0,1))).real
        w=(-(mp(s)+mp(1-s))/4).real
        wp=(acb(0,1)*(mpp(s)-mpp(1-s))/8).real
        logAp=(-acb(0,1)*(mp(s)-mp(1-s))/4).real
        return theta,w,wp,logAp
    def jet(x,t):
        theta,w,wp,b=phase_jet(x,t)
        ss=(1-acb(0,1)*acb(x))/2
        P=acb(1);Px=acb(0);Pxx=acb(0)
        for n in range(2,9):
            ell=A(n).log()
            wn=(t*ell*ell/4-(ss+t*old.alpha(ss)/2)*ell).exp()
            coeff=acb(0,1)*ell/2*(1+t*old.alphap(ss)/2)
            P+=wn;Px+=coeff*wn
            Pxx+=(coeff*coeff+t*ell*old.alphapp(ss)/8)*wn
        zs=acb_series([acb(x),acb(1)],3)
        # Simplified real normalized prefactor avoids a tiny/tiny quotient.
        ks=-old.W_real(zs,t)*old.J(zs,t,8)[0]
        ee=(acb(0,1)*theta).exp()
        f0=2*(ee*P).real-ks[0].real
        f1=2*(ee*(acb(0,1)*w*P+Px)).real-ks[1].real
        f2=2*(ee*((acb(0,1)*wp-w*w)*P+2*acb(0,1)*w*Px+Pxx)).real-2*ks[2].real
        ww=acb(f0,-f1/w)
        # n=1 contributes the constant 2 to Z and cancels exactly first.
        zz=2*(P-1)-acb(0,1)/w*(Px+ee.conjugate()**2*Px.conjugate())-ee.conjugate()*(ks[0]-acb(0,1)*ks[1]/w)
        rr=f0+f2/w**2-wp*f1/w**3
        return theta,w,wp,b,ww,zz,rr,f0,f1,f2
    # Declared closed rational cover. Each cell includes every x,t it covers.
    omega_lo=A(100);omega_hi=A(0);wp_hi=A(0);b_hi=A(0)
    phase_lo=A(0);phase_hi=-A(10000)
    min_fjet=A(100);min_anchor=A(100);max_signed=A(0);min_transport=A(100)
    max_defect=A(0);slabs=[]
    naive_min_fjet=A(100);naive_max_signed=A(0);naive_min_transport=A(100)
    for it in range(nt):
        t=interval(F(1,100)+F(19,100)*it/nt,F(1,100)+F(19,100)*(it+1)/nt)
        th0,w0,wp0,b0,W0,Z0,R0,*_=jet(A(999),t)
        anchor=abs(W0).lower();min_anchor=min(min_anchor,anchor)
        slab_signed=A(0);slab_direct=A(100);slab_margin=A(100)
        for ix in range(nx):
            x=interval(F(999)+F(2)*ix/nx,F(999)+F(2)*(ix+1)/nx)
            th,w,wp,b,W,Z,R,*_=jet(x,t)
            check(w<0,'phase orientation lost on closed cell')
            omega_lo=min(omega_lo,abs(w).lower());omega_hi=max(omega_hi,abs(w).upper())
            wp_hi=max(wp_hi,abs(wp).upper());b_hi=max(b_hi,abs(b).upper())
            phase_lo=min(phase_lo,th.lower());phase_hi=max(phase_hi,th.upper())
            direct=abs(W).lower();signed=abs(Z-Z0).upper()
            naive_min_fjet=min(naive_min_fjet,direct)
            naive_max_signed=max(naive_max_signed,signed)
            naive_min_transport=min(naive_min_transport,(anchor-signed).lower())
            # Exact approximant propagation inside each same closed cell:
            # Z_x=-i exp(-i theta) omega R, W_x=i omega(W-R).
            # This keeps the signed center value rather than summing modes.
            xc=A(F(999)+F(2*ix+1,nx))
            tc,wc,wpc,bc,Wc,Zc,Rc,*_=jet(xc,t)
            half_width=A(F(1,nx))
            z_variation=half_width*abs(w).upper()*abs(R).upper()
            w_variation=half_width*abs(w).upper()*(abs(W).upper()+abs(R).upper())
            direct=max(direct,(abs(Wc).lower()-w_variation).lower())
            signed=min(signed,(abs(Zc-Z0).upper()+z_variation).upper())
            slab_signed=max(slab_signed,signed);slab_direct=min(slab_direct,direct)
            slab_margin=min(slab_margin,(anchor-signed).lower())
            max_defect=max(max_defect,abs(R).upper())
        max_signed=max(max_signed,slab_signed);min_fjet=min(min_fjet,slab_direct)
        min_transport=min(min_transport,slab_margin)
        slabs.append({'t_index':it,'approximant_anchor_radius_lower':out(anchor),
                      'complete_signed_integral_modulus_upper':out(slab_signed),
                      'direct_approximant_radius_lower':out(slab_direct),
                      'anchor_minus_signed_integral_lower':out(slab_margin)})
    eJ=eta*(1+1/(radius*omega_lo)**2).sqrt()
    eJjoint=eta*max(A(1),1/(radius*omega_lo))
    defect_err=eta*(1+2/(radius**2*omega_lo**2)+wp_hi/(radius*omega_lo**3))
    integrated_residual=(2*eta*(omega_hi+2/(radius**2*omega_lo)+wp_hi/(radius*omega_lo**2))).upper()
    endpoint_residual=2*eJ
    direct_lower=min_fjet-eJ
    transport_lower=min_transport-eJ-endpoint_residual
    joint_transport_lower=min_transport-3*eJjoint
    standard_lower=min_transport-eJ-integrated_residual
    sigma=omega_lo/(1+b_hi*b_hi+omega_hi*omega_hi).sqrt()
    # A point witness tests the *specified uniform error-payment rule* itself.
    # It does not assert the actual physical residual attains that budget.
    t=A(F(1,100));j0=jet(A(999),t);j1=jet(A(1001),t)
    witness_anchor=abs(j0[4]);witness_signed=abs(j1[5]-j0[5])
    witness_endpoint_slack=witness_anchor-witness_signed-3*eJ
    witness_standard_slack=witness_anchor-witness_signed-eJ-integrated_residual
    witness_joint_slack=witness_anchor-witness_signed-3*eJjoint
    check(direct_lower>0,'fixed-cover direct exclusion failed')
    check(witness_endpoint_slack<0,'predeclared endpoint-budget failure witness not certified')
    check(witness_standard_slack<0,'predeclared integrated-budget failure witness not certified')
    # Rotation identity differential check, using an explicit second jet.
    # The analytic proof is separate; this is an adversarial normalization check.
    sample=jet(A(1000),A(F(21,200)))
    f=old.series_approximation(acb(1000),A(F(21,200)),True)
    theta,w,wp,b,W,Z,R,*stable_derivatives=sample
    stable_crosschecks=[]
    for order,value in enumerate(stable_derivatives):
        diff=value-math.factorial(order)*f[order].real
        check(diff.contains(0),f'stable complete jet vs original S02 order {order}')
        stable_crosschecks.append({'order':order,'difference':out(diff),'contains_zero':True})
    Wp=f[1].real-acb(0,1)*(2*f[2].real/w-wp*f[1].real/w**2)
    Zp=(-acb(0,1)*theta).exp()*(Wp-acb(0,1)*w*W)
    identity=Zp+acb(0,1)*(-acb(0,1)*theta).exp()*w*R
    check(identity.contains(0),'transport differential identity normalization')
    check((sample[5]+2-(-acb(0,1)*theta).exp()*W).contains(0),'stable signed primitive normalization')
    # Elementary controls are exact identities in the companion derivation;
    # interval checks detect sign, orientation and normalization mistakes.
    pi=arb.pi()
    constant_at_pi3=abs((acb(0,-1)*pi/3).exp()-1)
    constant_at_pi=abs((acb(0,-1)*pi).exp()-1)
    check((constant_at_pi3-1).contains(0),'constant-control equality at pi/3')
    check(constant_at_pi>1,'constant-control strict overrun at pi')
    qanchor=acb(1,-2);zanchor=acb(0,-1).exp()*qanchor
    collision_integral=-acb(0,1)*zanchor
    check((abs(collision_integral)-A(5).sqrt()).contains(0),'collision-control exact cancellation')
    osc=old.A(F(7,5));theta_control=A(F(3,7))
    qo=osc*theta_control.cos();qop=-osc*theta_control.sin();qopp=-qo
    check((qopp+qo).contains(0),'oscillator residual zero')
    result={
       'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
       'actual_model':args.execution_model,'actual_effort':args.execution_effort,
       'llm_assistance':'substantial; same-model parallel derivation and numerical internal check',
       'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':args.bits,
       'domain':{'t':['1/100','1/5'],'x':['999','1001'],'anchor_x':'999'},
       'fixed_cutoff':8,'retained_terms':'all n=1,...,8 and the entire signed S02 correction',
       'closed_cover':{'t_cells':nt,'x_cells':nx,'total_cells':nt*nx,
                       'method':'whole-cell interval derivatives plus midpoint propagation on identical cells; Z_x=-i exp(-i theta) omega R_f; W_x=i omega(W-R_f)'},
       'phase':{'orientation':'decreasing in x on every certified closed cell',
                'range_enclosure':[out(phase_lo),out(phase_hi)],
                'absolute_omega_lower':out(omega_lo),'absolute_omega_upper':out(omega_hi),
                'absolute_omega_x_upper':out(wp_hi),'absolute_logA_x_upper':out(b_hi)},
       'inherited_S02_contract':{'record':str(rec.relative_to(args.repo)),'record_sha256':sha(rec),
                              'disk_radius':'1/2','eta_upper':out(eta),
                              'script_sha256':sha(s02),'source_pins_validated':True,
                              'status':'imported complete holomorphic fixed-cutoff error, not re-proved'},
       'naive_whole_cell_enclosure':{'direct_approximant_radius_lower':out(naive_min_fjet),
                                    'signed_integral_modulus_upper':out(naive_max_signed),
                                    'endpoint_budget_lower':out(naive_min_transport-3*eJ),
                                    'joint_disk_endpoint_budget_lower':out(naive_min_transport-3*eJjoint)},
       'direct':{'approximant_first_jet_radius_lower':out(min_fjet),
                 'uniform_residual_first_jet_norm_upper':out(eJ),
                 'joint_disk_residual_first_jet_norm_upper':out(eJjoint),
                 'joint_disk_normalized_first_jet_radius_lower':out(min_fjet-eJjoint),
                 'normalized_first_jet_radius_lower':out(direct_lower),
                 'coordinate_matrix_smallest_singular_value_lower':out(sigma),
                 'physical_sqrt_energy_divided_by_A_lower':out(sigma*direct_lower),
                 'passes':True},
       'transport':{'integral_definition':'I_f(x)=integral from theta(999) to theta(x) of exp(-is) (D_theta^2+1)f ds',
                    'exact_integral_evaluation':'I_f=i(Z_f(x)-Z_f(999)); evaluate Z_f-2 before subtraction so the n=1 constant cancels exactly',
                    'quadrature_error':'0; exact endpoint antiderivative identity',
                    'signed_complete_integral_modulus_upper':out(max_signed),
                    'approximant_anchor_radius_lower':out(min_anchor),
                    'physical_anchor_radius_lower':out(min_anchor-eJ),
                    'anchor_minus_signed_integral_lower':out(min_transport),
                    'complete_approximant_defect_abs_upper_diagnostic':out(max_defect),
                    'cauchy_residual_defect_abs_upper':out(defect_err),
                    'cauchy_integrated_residual_upper':out(integrated_residual),
                    'endpoint_primitive_residual_integral_upper':out(endpoint_residual),
                    'joint_disk_endpoint_primitive_residual_integral_upper':out(2*eJjoint),
                    'standard_budget_lower_bound':out(standard_lower),
                    'endpoint_budget_lower_bound':out(transport_lower),
                    'joint_disk_endpoint_budget_lower_bound':out(joint_transport_lower),
                    'passes_standard_budget':False,'passes_endpoint_budget':False,
                    'passes_joint_disk_endpoint_budget':bool(joint_transport_lower>0),
                    'joint_disk_status':'fixed-cover interval lower bound remains negative; point witness is positive; no scoped impossibility for this sharper rule',
                    'joint_disk_provenance':'analytic Schwarz-Pick refinement discovered in the opening internal review, after the separate Cauchy comparison',
                    'witness':{'t':'1/100','x':'1001','anchor_radius':out(witness_anchor),
                               'complete_signed_integral_modulus':out(witness_signed),
                               'endpoint_budget_slack':out(witness_endpoint_slack),
                               'joint_disk_endpoint_budget_slack':out(witness_joint_slack),
                               'standard_budget_slack':out(witness_standard_slack)}},
       'elementary_controls':{'constant_Q':{'theta':'x','anchor_theta':'0','anchor_radius':'1','integral_modulus_at_pi_over_3':out(constant_at_pi3),'integral_modulus_at_pi':out(constant_at_pi),'failed_premise':'strict signed-integral smaller-than-anchor bound; even a nonzero constant does not satisfy it on long intervals'},
                              'heat_polynomial_event':{'H':'x^2-2(t-t_c)','time':'t_c','anchor_x':'1','event_x':'0','anchor_radius':out(abs(qanchor)),'integral_modulus_at_event':out(abs(collision_integral)),'failed_premise':'strict propagation bound fails by equality at the event'},
                              'oscillatory_residual':{'r':'c cos(theta)','defect':'0 exactly','failed_premise':'independent endpoint envelope does not use exact residual correlation'}},
       'slabs':slabs,'algebra_check':{'differential_identity_contains_zero':True,'residual':str(identity),'stable_complete_jet_vs_S02':stable_crosschecks},
       'comparison_gate':'PASS scoped no-advantage comparison: standard Cauchy rule fails a certified point witness; direct exclusion passes on the full box; sharper joint-disk propagation remains inconclusive on the fixed cover',
       'limitations':['Finite real box only; no improved global arithmetic estimate or exterior.',
                      'Error-budget failure does not imply the actual complete defect integral is large.',
                      'The direct exclusion reuses established S02 complete error and claims no newly covered region.',
                      'The endpoint primitive payment is valid but reduces to direct first-jet information.',
                      'No quadrature or operation-cost advantage is claimed.'],
       'script_sha256':sha(__file__),'seconds':time.monotonic()-started}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'comparison_gate':result['comparison_gate'],'direct_lower':out(direct_lower),
                      'signed_integral_upper':out(max_signed),'endpoint_transport_lower':out(transport_lower),
                      'witness_endpoint_slack':out(witness_endpoint_slack),'joint_disk_transport_lower':out(joint_transport_lower),'seconds':result['seconds']}))

if __name__=='__main__':main()
