#!/usr/bin/env python3
"""Rigorous scalar evaluation of a family p=3 heat-floor envelope.

Prepared for Edward Baker with LLM assistance, 17 October 2026.
Model: gpt-6-astra (Codex); reasoning effort: ultra.
Analytic source: ../../notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md.
Requires python-flint. No input data, floating arithmetic, numerical quadrature,
parameter sampling, or network input is used to decide an inequality.

The analytic input is the separate Euler/critical/far-reflection envelope:
  ell >= 129/5, h=t/2 in (0,1/8], sigma=2+h*ell/2, parity-even majorants.
This script certifies the scalar bounds of that envelope. The analytic
majorization and parameter monotonicity are not proved by running the script.

Each rational h-cell uses h_hi and sigma_min=2+(129/10)*h_lo.
The completely monotone positive derivative majorants are evaluated at sigma_min
or (sigma_min+1)/2. M2 is increasing in h,c,b. The boundary Gaussian bound
is decreasing in V and increasing in h after the checked inequalities.
The ordinary tail and tilted Gaussian mass are evaluated at the same adverse
endpoints. The first cell covers every 0<h<=1/8000; t=0 uses the time-zero floor.
"""
from fractions import Fraction as Q
from functools import lru_cache
import json
import flint
from flint import arb, arb_series, ctx

BITS=128
NCELLS=1000
ctx.prec=BITS

def require(ok,message):
    if not ok:
        raise ArithmeticError(message)

def A(q):
    q=Q(q)
    return arb(q.numerator)/q.denominator

@lru_cache(None)
def jets(q):
    s=A(q)
    z=arb_series([s,1],4).zeta().log()
    g=arb_series([s/2,1],4).lgamma()
    return -z[1],2*z[2],-6*z[3],g[2]/2,-3*g[3]/4

def M2(h,c,b):
    d=1-h*b
    require(d>0,'nonpositive Gaussian-moment denominator')
    z=c*(h/d).sqrt()
    return h/d**A(Q(3,2))*((1+z*z)*(z*z/2).exp()*(1+A(Q(4,5))*z)+A(Q(4,5))*z)

def elementary_and_tail_constants():
    L=A(Q(129,5));S=A(Q(289,80));kap=A(Q(57,100))
    require(A(2).zeta()<A(Q(33,20)),'zeta(2)<1.65')
    require(A(Q(5,4)).zeta()<5,'zeta(5/4)<5')
    require(jets(Q(5,4))[3]<A(Q(26,25)),'Gamma curvature at 5/4')
    require((2/arb.pi()).sqrt()<A(Q(4,5)),'sqrt(2/pi)<4/5')
    require(jets(Q(2))[0]<kap,'kappa(2)<.57')
    require(arb.pi()*A(Q(7,12)).exp()+(-L).exp()<A(2).exp(),
            'log ceil(Qproxy/2) <= ell+2')
    require(Q(129,5)/4-Q(57,100)/2-Q(1,5)/2>6, 'final rational floor exceeds six')
    ell0=(A(10**12)/arb.pi()).log()+arb(1).digamma()
    require(ell0>L,'uniform time-zero ell lower bound')

    # Two ordinary/reflected critical strips, both split at 1 and 5/4.
    R=(L*(L-2)).sqrt()
    C=A(Q(33,20))*2*S*(L+5)/(2*arb.pi()).sqrt()
    Z0=2-L/4-3*arb(3).sqrt()*R/8
    Z1=1-3*L/8-3*arb(3).sqrt()*R/16
    Dc=Nc=arb(0)
    for length,Z,c in [(Q(1,2),Z0,Q(1,8)),(Q(1,4),Z1,Q(9,128))]:
        def H(r):
            return (A(r)/(arb(1).exp()*A(c)))**A(r)
        Dc+=C*A(length)*Z.exp()*H(Q(1,2))
        Nc+=C*A(length)*Z.exp()*((S+A(Q(1,4)))*H(Q(3,2))+kap*H(Q(1,2)))
    Dc*=2;Nc*=2
    require(Dc<A(Q(1,10**5)),'critical D bound')
    require(Nc<A(Q(1,2000)),'critical N bound')

    # Far reflected half-line: whole tilted Gaussian, with three N cases.
    b=A(Q(26,25));d=A(Q(87,100));C=A(Q(33,4))
    Zmax=(9*b/(2*d)).exp()/d.sqrt()
    Df=C*Zmax*(-3*L/2).exp()
    N1=Df*(L+kap+3*b/d+10/d.sqrt())
    N2=Df*(L+kap+3*b/d+(L/d).sqrt())
    h0=A(Q(1,100));v=A(Q(7,4));d0=1-b*h0
    N3=C*(9*b/2-3*L/2).exp()*(1+(1+kap/100)/v)/(d0*(2*arb.pi()*h0).sqrt())*(-d0*v*v/(2*h0)).exp()
    require(Df<A(Q(1,10**10)),'far reflected D bound')
    for j,N in enumerate((N1,N2,N3),1):
        require(N<A(Q(1,10**8)),f'far reflected N case {j}')
    return {'ell0_at_q_1e12':ell0,'D_critical':Dc,'N_critical':Nc,
            'D_far_reflected':Df,'N_far_case1':N1,'N_far_case2':N2,'N_far_case3':N3}

def cell(hl,hh):
    h=A(hh);sigma=Q(2)+Q(129,10)*hl;a=(sigma+1)/2;V=A((sigma-1)/2)
    kap,K2,K3,A1,A2=jets(sigma)
    c,K2a,K3a,b,A2a=jets(a)
    ka=K2a+b;ja=K3a+A2a;k=K2+A1
    require(h*k<1,'h*k<1')
    Mrho=ja*M2(h,c,b)/2
    P1=ka*M2(h,kap,ka)/2
    require((1/h-b)*V>c,'boundary expression decreases with V')
    require(V*V>h,'Gaussian density/tail first moment increases with h')
    BV=(c*V+b*V*V/2-V*V/(2*h)).exp()/(2*arb.pi()*h).sqrt()

    d=1-A(Q(26,25))*h
    T=(V*(d/(2*h)).sqrt()).erfc()/2
    DE=A(Q(33,4))*T/d.sqrt()
    NE=A(Q(33,4))*((-(d*V*V/(2*h))).exp()/((2*arb.pi()*h).sqrt()*d)+kap*T/d.sqrt())
    J=(h*kap*kap/2).exp()*((V-h*kap)/(2*h).sqrt()).erfc()/2
    DL=DE+A(Q(1,10**5)+Q(1,10**10))
    NL=NE+A(Q(1,2000)+Q(1,10**8))
    P2=DL+J
    d0=(-h*kap*kap/2).exp()-P1-P2
    require(d0>A(Q(93,100)),'d0>.93 on every cell')
    E=h*k*kap/(1-h*k)+(Mrho+BV+h*k*kap*DL+(1+h*k)*NL)/((1-h*k)*d0)
    require(E<A(Q(1,5)),'E<1/5 on every cell')
    return dict(Mrho=Mrho,P1=P1,BV=BV,DL=DL,NL=NL,P2=P2,d0=d0,E=E,hk=h*k)

def main():
    constants=elementary_and_tail_constants()
    maxima={};indices={};d0lower=None;d0index=None
    for i in range(NCELLS):
        vals=cell(Q(i,8*NCELLS),Q(i+1,8*NCELLS))
        for key in ['Mrho','P1','BV','DL','NL','P2','E','hk']:
            val=vals[key].upper()
            if key not in maxima or val>maxima[key]:
                maxima[key]=val;indices[key]=i
        low=vals['d0'].lower()
        if d0lower is None or low<d0lower:
            d0lower=low;d0index=i
    record={
      'programme':'family_floor_gate_arb_20261017.py',
      'prepared_for':'Edward Baker',
      'date_local':'2026-10-17',
      'llm_assistance':'Substantial LLM assistance; internal same-model research team',
      'model':'gpt-6-astra (Codex)', 'reasoning_effort':'ultra',
      'arithmetic':{'package':'python-flint','version':flint.__version__,'precision_bits':BITS},
      'domain':{'p':'3','ell_min':'129/5','h':'0<h<=1/8','t':'0<t<=1/4','family':'primitive nonprincipal characters; even Gamma majorants dominate both parities'},
      'cover':{'cells':NCELLS,'endpoints':'h_i=i/8000, i=0,...,1000','first_cell':'(0,1/8000]','unbounded_ell':'monotone endpoint envelope for ell>=129/5, plus analytic critical/reflected bounds'},
      'certified_rational_bounds':{'E_upper':'1/5','d0_lower':'93/100','D_critical_upper':'1/100000','N_critical_upper':'1/2000','D_far_upper':'1/10000000000','N_far_upper':'1/100000000','S_lower_at_q_ge_1e12':'6'},
      'all_checks_pass':True,
      'max_upper_enclosures':{k:v.str(30) for k,v in maxima.items()},
      'maximizing_cell_indices':indices,
      'd0_lower_enclosure':d0lower.str(30),'d0_minimizing_cell_index':d0index,
      'auxiliary_constant_enclosures':{k:v.str(30) for k,v in constants.items()},
      'scope':'Certifies evaluation of the analytic envelope. Requires its proved domination, completely monotone derivative bounds, parameter monotonicity and the Gaussian heat representation. Not a certificate of any imported strip-comparison theorem.'}
    print(json.dumps(record,indent=2))

if __name__=='__main__':
    main()
