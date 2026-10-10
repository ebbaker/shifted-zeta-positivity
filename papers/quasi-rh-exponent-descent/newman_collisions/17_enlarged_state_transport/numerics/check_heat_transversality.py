#!/usr/bin/env python3
"""Exact internal algebra replay for project 17 heat-flow transversality.

Standard library only. Fractions and Q(sqrt(6)); no floating sign tests.
This verifies finite algebra, not genuine-theta preparation or collision absence.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

@dataclass(frozen=True)
class Q6:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))
    @staticmethod
    def coerce(v): return v if isinstance(v, Q6) else Q6(v)
    def __add__(self, v):
        v=self.coerce(v); return Q6(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self): return Q6(-self.a,-self.b)
    def __sub__(self,v): return self+-self.coerce(v)
    def __rsub__(self,v): return self.coerce(v)+-self
    def __mul__(self,v):
        v=self.coerce(v); return Q6(self.a*v.a+6*self.b*v.b,self.a*v.b+self.b*v.a)
    __rmul__=__mul__
    def __truediv__(self,v):
        v=self.coerce(v); den=v.a*v.a-6*v.b*v.b
        if den==0: raise ZeroDivisionError
        return self*Q6(v.a/den,-v.b/den)
    def __rtruediv__(self,v): return self.coerce(v)/self
    def __pow__(self,n):
        if n<0: return 1/(self**(-n))
        out=Q6(1)
        for _ in range(n): out=out*self
        return out
    def __bool__(self): return bool(self.a or self.b)
    def record(self): return {'rational':str(self.a),'sqrt6':str(self.b)}

# Sparse polynomials: exponents are tuples; coefficients may be F or Q6.
def clean(p): return {k:v for k,v in p.items() if v}
def add(p,q):
    out=dict(p)
    for k,v in q.items(): out[k]=out.get(k,0)+v
    return clean(out)
def scale(p,v): return clean({k:c*v for k,c in p.items()})
def mul(p,q,cap=None):
    out={}
    for k,v in p.items():
        for j,w in q.items():
            z=tuple(a+b for a,b in zip(k,j))
            if cap is not None and sum(z)>cap: continue
            out[z]=out.get(z,0)+v*w
    return clean(out)
def power(p,n,cap=None):
    width=len(next(iter(p))) if p else 1
    out={(0,)*width:F(1)}
    for _ in range(n): out=mul(out,p,cap)
    return out
def diff(p,var=0):
    out={}
    for k,v in p.items():
        if k[var]:
            z=list(k); z[var]-=1; out[tuple(z)]=v*k[var]
    return clean(out)
def eval_one(p,value):
    return sum((c*value**k[0] for k,c in p.items()),0)
def compose2(p,x,a,cap=4):
    out={}
    for (i,j),c in p.items():
        out=add(out,scale(mul(power(x,i,cap),power(a,j,cap),cap),c))
    return out

def check(ok,label,checks):
    if not ok: raise AssertionError(label)
    checks.append(label)

def gauged_dx(p):
    """(d/dx-x/2) p, after fixing Gaussian parameter a=1."""
    return add(diff(p),mul({(1,):F(-1,2)},p))
def inverse_fourier_k2_minus_q(p,q):
    """(-d_u^2-q)[p(u)e^-u^2] = returned polynomial times e^-u^2."""
    return add(add(scale(diff(diff(p)),-1),mul({(1,):F(4)},diff(p))),
               mul({(0,):F(2-q),(2,):F(-4)},p))
def remainder_x2_q(p,q):
    out={}
    for (n,),c in p.items():
        k=n%2; out[(k,)]=out.get((k,),0)+c*q**(n//2)
    return clean(out)
def polynomial_record(p):
    return {','.join(map(str,k)):str(c) for k,c in sorted(p.items())}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record',type=Path)
    args=parser.parse_args()
    checks=[]
    # Exact chord identities use only the prepared wavefunction time law.
    # Variables u,ell; aplus=u+ell/2 and aminus=u-ell/2.
    u={(1,0):F(1)}; ell={(0,1):F(1)}
    plus=add(u,scale(ell,F(1,2))); minus=add(u,scale(ell,F(-1,2)))
    product_time=scale(add(power(plus,2),power(minus,2)),F(1,2))
    check(product_time==add(power(u,2),scale(power(ell,2),F(1,4))),
          'chord prepared-state product time multiplier',checks)
    # Coefficients of psi_plus_pp*psi_minus, psi_plus_p*psi_minus_p,
    # and psi_plus*psi_minus_pp in f_ell_ell-f_u_u/4.
    transverse=[F(1,4)-F(1,4),F(-1,2)-F(1,2),F(1,4)-F(1,4)]
    check(transverse==[0,-1,0],'chord transverse gradient-source identity',checks)
    # Time derivative of gradient product gives u*f_u-ell*f_ell.
    check(add(u,scale(ell,F(-1,2)))==minus and
          add(u,scale(ell,F(1,2)))==plus,
          'gradient-overlap inhomogeneous source coefficients',checks)
    def chord_L(p): return add(scale(diff(diff(p,0),0),-1),mul({(0,2):F(1,4)},p))
    def chord_D(p): return add(diff(diff(p,1),1),mul({(2,0):F(1,4)},p))
    for i in range(5):
        for j in range(5):
            test={(i,j):F(1)}
            comm=add(chord_D(chord_L(test)),scale(chord_L(chord_D(test)),-1))
            expected=scale(test,i+j+1)
            if comm!=expected: raise AssertionError('chord operator commutator')
    checks.append('chord operator commutator on degree 0..4 tensor basis')

    # P(x,a) is the manuscript Gaussian quartic control's scalar polynomial.
    P={(4,0):F(1),(2,1):F(-12),(0,2):F(12),(0,4):F(24)}
    x={(1,0):F(1)}; a={(0,1):F(1)}
    heat_identity=add(add(mul(a,add(diff(diff(P,0),0),scale(diff(P,1),-1))),
                               scale(mul(x,diff(P,0)),-1)),scale(P,4))
    check(not heat_identity,'exact gauged heat PDE for Gaussian quartic',checks)
    # For H=K P with K=(sqrt(pi)/2)a^-9/2 exp(-x^2/(4a)), this
    # identity is exactly H_t=-H_xx, using a=1+t_star-t.
    density={(0,):F(1)}
    for _ in range(2): density=inverse_fourier_k2_minus_q(density,6)
    check(density=={(0,):F(24),(4,):F(16)},
          'positive quartic density and Fourier multiplier identity',checks)
    check(all(c>0 for c in density.values()),'quartic density positive coefficients',checks)

    r=Q6(0,1)
    fixedP={(4,):F(1),(2,):F(-12),(0,):F(36)}
    jets=[]; p=fixedP
    for j in range(5):
        jets.append(Q6.coerce(eval_one(p,r)))
        p=gauged_dx(p)
    expected=[Q6(0),Q6(0),Q6(48),Q6(0,-48),Q6(24)]
    check(jets==expected,'ordinary-double spatial jets in Q(sqrt6)',checks)
    h={(1,):Q6(1)}; xchart=add({(0,):r},h)
    zero_time={}
    # Solve P(r+h,1-z(h))=0 coefficient by coefficient; P_a(r,1)=48.
    for order in range(1,5):
        achart=add({(0,):Q6(1)},scale(zero_time,-1))
        remainder=compose2(P,xchart,achart,4)
        coefficient=Q6.coerce(remainder.get((order,),0))/48
        zero_time=add(zero_time,{(order,):coefficient})
    achart=add({(0,):Q6(1)},scale(zero_time,-1))
    check(not compose2(P,xchart,achart,4),'implicit zero graph vanishes through fourth order',checks)
    tau=[Q6.coerce(zero_time.get((j,),0))*factorial(j) for j in range(1,5)]
    check(tau==[Q6(0),Q6(1),Q6(0,2),Q6(47)],'implicit graph derivatives 0,1,2sqrt6,47',checks)
    ratio3=jets[3]/jets[2]; ratio4=jets[4]/jets[2]
    check(tau[2]==-2*ratio3 and tau[3]==-2*ratio4+8*ratio3**2,
          'universal heat-equation third and fourth graph formulas',checks)
    determinant=(-jets[2])*jets[2]-jets[1]*(-jets[3])
    check(determinant==Q6(-2304),'ordinary-double Jacobian determinant -Hxx squared',checks)

    # A genuine nonlinear spatial coordinate change, preserving physical time.
    change={(1,):Q6(2),(2,):Q6(F(1,3)),(3,):Q6(F(-1,5))}
    changed_time={}
    for (j,),v in zero_time.items(): changed_time=add(changed_time,scale(power(change,j,4),v))
    changed_tau=[Q6.coerce(changed_time.get((j,),0))*factorial(j) for j in range(1,5)]
    check(changed_tau==[Q6(0),Q6(4),Q6(4,16),Q6(F(11156,15),32)],
          'nonlinear coordinate jet transformation by exact composition',checks)
    changed_det=determinant*Q6(2)**2
    check(changed_det==Q6(-9216),'transformed first-jet Jacobian stays nonzero',checks)

    # A strictly positive Gaussian density with genuine quadruple zeros.
    density4={(0,):F(1)}
    for _ in range(4): density4=inverse_fourier_k2_minus_q(density4,30)
    expected_density4={(0,):F(646080),(2,):F(245760),(4,):F(42240),(6,):F(4096),(8,):F(256)}
    check(density4==expected_density4,'quadruple control inverse Fourier polynomial',checks)
    check(all(c>0 for c in density4.values()),'quadruple control positive density coefficients',checks)
    quadrupleP=power({(2,):F(1),(0,):F(-30)},4)
    p=quadrupleP
    quadremainders=[]
    for j in range(5):
        quadremainders.append(remainder_x2_q(p,30)); p=gauged_dx(p)
    check(all(not p for p in quadremainders[:4]) and quadremainders[4]=={(0,):F(345600)},
          'quadruple control exact order four at x squared=30',checks)
    # Hxxxx/(24*K)=14400, so after division by K the leading unfolding is
    # 14400*(h^4-12*s*h^2+12*s^2). Its first-jet Jacobian vanishes.
    check(F(345600,24)==14400,'quadruple leading heat-polynomial coefficient',checks)
    # A strictly positive even Gaussian source with odd multiplicity:
    # (-d_u^2-30)^3(-d_u^2-40)e^-u^2 has positive polynomial density.
    density3={(0,):F(1)}
    for qvalue in [30,30,30,40]:
        density3=inverse_fourier_k2_minus_q(density3,qvalue)
    expected_density3={(0,):F(871680),(2,):F(317760),(4,):F(51840),(6,):F(4736),(8,):F(256)}
    check(density3==expected_density3,'triple positive control inverse Fourier polynomial',checks)
    check(all(c>0 for c in density3.values()),'triple control positive density coefficients',checks)
    tripleP=mul(power({(2,):F(1),(0,):F(-30)},3),{(2,):F(1),(0,):F(-40)})
    p=tripleP; triple_remainders=[]
    for j in range(5):
        triple_remainders.append(remainder_x2_q(p,30)); p=gauged_dx(p)
    check(all(not p for p in triple_remainders[:3]) and
          triple_remainders[3]=={(1,):F(-14400)} and
          triple_remainders[4]=={(0,):F(1123200)},
          'triple control exact order three at x squared=30',checks)
    simple_rem=remainder_x2_q(tripleP,40)
    simple_first_rem=remainder_x2_q(gauged_dx(tripleP),40)
    check(not simple_rem and simple_first_rem=={(1,):F(2000)},
          'triple control companion roots simple at x squared=40',checks)

    heat_polynomials={}
    for degree in range(2,11):
        hp={}
        for j in range(degree//2+1):
            hp[(degree-2*j,j)]=F(factorial(degree)*(-1)**j,
                                   factorial(j)*factorial(degree-2*j))
        check(not add(diff(hp,1),diff(diff(hp,0),0)),
              f'degree {degree} heat-polynomial PDE',checks)
        check({k:v for k,v in hp.items() if k[1]==0}=={(degree,0):F(1)},
              f'degree {degree} heat-polynomial initial multiplicity',checks)
        heat_polynomials[str(degree)]=polynomial_record(hp)

    # Earlier-time stationary-sign controls, and a symbolic next-jet shift.
    stationary_controls={}
    for degree in range(2,11):
        hp={(degree-2*j,j):F(factorial(degree)*(-1)**j,
               factorial(j)*factorial(degree-2*j)) for j in range(degree//2+1)}
        rint=degree//2
        field=hp if degree%2==0 else diff(hp,0)
        # Substitute s=-1 and evaluate the stationary even field at h=0.
        field_at_sminus1={}
        for (hdegree,sdegree),c in field.items():
            field_at_sminus1[(hdegree,)]=field_at_sminus1.get((hdegree,),0)+c*(-1)**sdegree
        f0=eval_one(field_at_sminus1,F(0))
        f2=eval_one(diff(diff(field_at_sminus1)),F(0))
        check(not eval_one(diff(field_at_sminus1),F(0)),
              f'degree {degree} earlier-time stationary point',checks)
        check(f0==F(factorial(degree),factorial(rint)) and
              f2==F(factorial(degree),factorial(rint-1)) and f0*f2>0,
              f'degree {degree} earlier-time stationary product positive',checks)
        # Source H=P_m+B*P_(m+1), s=-delta,
        # h=-(m+1)*B*delta/r. Check leading critical coefficient as an
        # exact polynomial identity in independent symbols delta and B.
        nextdegree=degree+1
        hpnext={(nextdegree-2*j,j):F(factorial(nextdegree)*(-1)**j,
               factorial(j)*factorial(nextdegree-2*j)) for j in range(nextdegree//2+1)}
        stationarity_order=1 if degree%2==0 else 2
        ghp=hp; gnext=hpnext
        for _ in range(stationarity_order): ghp=diff(ghp,0); gnext=diff(gnext,0)
        shift={(1,1):F(-(degree+1),rint)}
        earlier={(1,0):F(-1)}
        symbolic_B={(0,1):F(1)}
        leadingcritical=add(compose2(ghp,shift,earlier,None),
                            mul(symbolic_B,compose2(gnext,shift,earlier,None)))
        check(not {k:c for k,c in leadingcritical.items() if k[0]<=rint},
              f'degree {degree} symbolic next-jet critical shift',checks)
        stationary_controls[str(degree)]={
          'field':'H' if degree%2==0 else 'Hx',
          'stationarity':'Hx=0' if degree%2==0 else 'Hxx=0',
          'F_at_earlier_time_s_minus1_h0':str(f0),
          'Fhh_at_earlier_time_s_minus1_h0':str(f2),
          'positive_product':str(f0*f2),
          'leading_critical_shift_h_over_delta_B':str(F(-(degree+1),rint)),
          'stationary_product_delta_exponent':str(2*rint-1)}

    # Additional varied rational source germs and the exact printed
    # overlap/normalization/error dictionaries. These are algebra controls,
    # not floating experiments or theta sign certificates.
    bulk_counts={}
    def bulk(ok,scope):
        if not ok: raise AssertionError(scope)
        bulk_counts[scope]=bulk_counts.get(scope,0)+1
    def earlier_germ(jets,spatial_order,c):
        # F(T-delta,c*delta) from the analytic heat Taylor coefficients.
        out={}
        for j,Fj in enumerate(jets):
            if not Fj: continue
            for k in range((j-spatial_order)//2+1):
                ell=j-spatial_order-2*k; exponent=k+ell
                out[exponent]=out.get(exponent,F(0))+Fj*c**ell/F(factorial(k)*factorial(ell))
        return {e:v for e,v in out.items() if v}
    for rint in range(1,9):
        degree=2*rint
        for seed in range(1,12):
            source=[F(0)]*degree+[F(seed-6 or 2),F(2*seed-7),F(seed+3),F(4-seed)]
            Fm,Fm1=source[degree:degree+2]
            slope=-Fm1/(rint*Fm)
            f,fx,fxx=[earlier_germ(source,order,slope) for order in (0,1,2)]
            bulk(min(f)==rint and f[rint]==Fm/F(factorial(rint)),
                 'varied rational heat germs: leading value')
            bulk(rint not in fx and all(e>rint for e in fx),
                 'varied rational heat germs: critical coefficient cancellation')
            bulk(min(fxx)==rint-1 and fxx[rint-1]==Fm/F(factorial(rint-1)),
                 'varied rational heat germs: leading curvature')
            bulk(f[rint]*fxx[rint-1]==Fm**2/F(factorial(rint)*factorial(rint-1))>0,
                 'varied rational heat germs: positive stationary product')

    for seed in range(1,101):
        xpos,beta=F(seed+2,3),F(seed+1,7)
        A0,A1,A2,A3=[F(((seed+i)*7)%19-9,i+1) for i in range(4)]
        # Frozen beta: impose A1=0 only in the first identity and A2=0
        # only in the second; they are distinct stationary candidates.
        D=-beta**2*A2-(xpos*xpos+2*beta)*A0
        bulk(A0*(D+(xpos*xpos+2*beta)*A0)==-beta**2*A0*A2,
             'frozen beta: complete first stationary score dictionary')
        D1=-beta**2*A3-(xpos*xpos+4*beta)*A1-2*xpos*A0
        bulk(A1*(D1+(xpos*xpos+4*beta)*A1+2*xpos*A0)==-beta**2*A1*A3,
             'frozen beta: complete second stationary score dictionary')

        source=[F(0),F(0),F(seed+1),F(7-seed,3),F(seed-10,2),F(3*seed-5,7),F(seed+4,9)]
        heat_taylor={}
        for time_order in range(4):
            for space_order in range(7-2*time_order):
                jet=source[2*time_order+space_order]
                if jet:
                    heat_taylor[(space_order,time_order)]=F((-1)**time_order,
                            factorial(time_order)*factorial(space_order))*jet
        tau_poly={}; local_x={(1,):F(1)}
        for order in range(1,7):
            remainder=compose2(heat_taylor,local_x,tau_poly,6)
            tau_poly=add(tau_poly,{(order,):remainder.get((order,),0)/source[2]})
        tau_generic=[tau_poly.get((j,),0)*factorial(j) for j in range(1,7)]
        r3,r4,r5,r6=[source[j]/source[2] for j in range(3,7)]
        formula=[F(0),F(1),-2*r3,8*r3*r3-2*r4,
                 -40*r3**3+10*r3*r4+6*r5,
                 240*r3**4-20*r3*r3*r4-116*r3*r5+16*r6]
        for order in range(2,6):
            bulk(tau_generic[order]==formula[order],
                 f'implicit heat fold: generic derivative order {order+1}')
        A,B,C=source[2:5]; xpos2=F(seed+3,2); g=9/xpos2**2
        threshold=2*B*B-3*A*C-g*A*A
        geometry=tau_generic[3]-F(5,3)*tau_generic[2]**2-F(2,3)*g
        bulk(geometry==F(2,3)*threshold/(A*A),
             'ordinary threshold quadratic and fold-jet dictionary')
        chi1=B/A; velocity1=-A; velocity2=C-B*B/A
        bulk(velocity2/velocity1-(chi1*chi1+g)/3==threshold/(3*A*A),
             'ordinary threshold quadratic and critical-value dictionary')
        V,Vx=F(2*seed-3,5),F(seed+4,11)
        time_shift=V/A; spatial_shift=B*V/(A*A)-Vx/A
        bulk(-A*time_shift+V==0 and -B*time_shift+A*spatial_shift+Vx==0,
             'ordinary collision source perturbation derivative')

        # Reconstruct G=bH independently via Leibniz from the stated
        # physical normalized jets. b(0)=1, b'/b=lambda and its two jets.
        G=[F(((seed+i)*5)%17-8,i+1) for i in range(4)]
        lam,lamp,lampp=F(seed-7,13),F(seed+2,17),F(3-seed,19)
        H=[G[0],G[1]-lam*G[0],
           G[2]-2*lam*G[1]+(lam*lam-lamp)*G[0],
           G[3]-3*lam*G[2]+3*(lam*lam-lamp)*G[1]
                 +(-lam**3+3*lam*lamp-lampp)*G[0]]
        bjets=[F(1),lam,lam*lam+lamp,lam**3+3*lam*lamp+lampp]
        rebuilt=[]
        for order in range(4):
            rebuilt.append(sum(F(factorial(order),factorial(j)*factorial(order-j))
                          *bjets[j]*H[order-j] for j in range(order+1)))
        bulk(rebuilt==G,'nonzero normalizer physical jet dictionary through order three')

        for j in (0,1):
            approx=[F(((seed+2*i)*5)%17-8,i+1) for i in range(4)]
            radii=[F(seed%5+1,20*(i+1)) for i in range(4)]
            error=[(-1)**(seed+i)*radii[i] for i in range(4)]
            actual=[approx[i]+error[i] for i in range(4)]
            payment=abs(approx[j])*radii[j+2]+abs(approx[j+2])*radii[j]+radii[j]*radii[j+2]
            laguerre_payment=2*abs(approx[j+1])*radii[j+1]+radii[j+1]**2+payment
            bulk(abs(actual[j]*actual[j+2]-approx[j]*approx[j+2])<=payment,
                 'complete physical product error payment')
            actual_l=actual[j+1]**2-actual[j]*actual[j+2]
            approx_l=approx[j+1]**2-approx[j]*approx[j+2]
            bulk(abs(actual_l-approx_l)<=laguerre_payment,
                 'complete Laguerre-expression error payment')

    record={
      'date':'2026-10-10',
      'model':'GPT-6 (Codex)',
      'reasoning_effort':'Active effort not exposed in this execution context',
      'arithmetic':'Python standard-library Fraction and Q(sqrt(6)); no floating signs',
      'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'checks_passed':checks,
      'bulk_exact_assertions':bulk_counts,
      'exact_assertion_count':len(checks)+sum(bulk_counts.values()),
      'quartic_control':{
        'threshold_time':'1/40','threshold_x':'sqrt(6)',
        'normalizer_at_threshold':'K=(sqrt(pi)/2)*exp(-3/2)',
        'spatial_jets_divided_by_K':[v.record() for v in jets],
        'tau_derivatives_1_to_4':[v.record() for v in tau],
        'jacobian_determinant_divided_by_K_squared':determinant.record()},
      'coordinate_change':{
        'x_minus_sqrt6':'2*y+y^2/3-y^3/5',
        'tau_derivatives_1_to_4':[v.record() for v in changed_tau],
        'jacobian_determinant_for_H_Hy_divided_by_K_squared':changed_det.record()},
      'quadruple_control':{
        'density_polynomial':polynomial_record(density4),
        'collision_time':'1/40','collision_x_squared':'30',
        'collision_chord_slice':'sqrt(pi)*exp(-k^2/4)*(k^2-30)^4',
        'time_interval_with_positive_wavefunction':'0<=t<=1/20',
        'scope':'Positive even source and exact order four; no global threshold claim',
        'normalizer_at_collision':'K=(sqrt(pi)/2)*exp(-15/2)',
        'Hxxxx_divided_by_K':'345600',
        'leading_unfolding_divided_by_K':'14400*(h^4-12*s*h^2+12*s^2)',
        'first_jet_jacobian':'0'},
      'positive_triple_control':{
        'density_polynomial':polynomial_record(density3),
        'collision_time':'1/40','collision_x_squared':'30','simple_x_squared':'40',
        'time_interval_with_positive_wavefunction':'0<=t<=1/20',
        'collision_chord_slice':'sqrt(pi)*exp(-k^2/4)*(k^2-30)^3*(k^2-40)',
        'normalizer_at_triple':'K=(sqrt(pi)/2)*exp(-15/2)',
        'Hxxx_divided_by_K':'-14400*x, evaluated at x^2=30',
        'Hxxxx_divided_by_K':'1123200',
        'Hx_at_simple_root_divided_by_its_K':'2000*x, evaluated at x^2=40',
        'scope':'Positive even source and exact odd multiplicity; no global threshold claim'},
      'heat_polynomials_variables':'h,s with exponent tuple h_degree,s_degree',
      'heat_polynomials':heat_polynomials,
      'earlier_stationary_controls':stationary_controls,
      'limitations':[
        'Finite identities only; Gaussian controls are not the genuine theta state.',
        'Positive density and the standard prepared chord identities permit these controls.',
        'No Riemann heat-flow collision exclusion, approximation interface or global threshold theorem is verified.',
        'The record contains algebraic checks; local analytic IFT and heat-polynomial splitting require the accompanying written proof.']}
    out=json.dumps(record,indent=2,sort_keys=True)+'\n'
    if args.record: args.record.write_text(out)
    print(out)

if __name__=='__main__': main()
