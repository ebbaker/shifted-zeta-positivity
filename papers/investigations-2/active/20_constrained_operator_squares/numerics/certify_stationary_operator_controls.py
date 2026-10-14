#!/usr/bin/env python3
"""Stationary Laguerre controls with full theta tails and parameter payments.
Prepared for Edward Baker with substantial LLM assistance, 2026-10-14.
Recorded model gpt-6.1-sol (Codex), reasoning effort ultra.
Requires python-flint; no binary64 arithmetic enters the certificate.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path
from fractions import Fraction
import flint
from flint import arb, acb, ctx

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def rat(s):
    f=Fraction(s)
    return arb(f.numerator)/f.denominator

def ball(a,b):
    return (a+b)/2+arb(0, ((b-a)/2).upper())

def enc(a):
    require(a.is_finite(),'Nonfinite enclosure')
    def dy(v):
        m,e=v.man_exp()
        return {'mantissa':str(m),'exponent':int(e)}
    return {'display':a.str(30,more=True),'lower_dyadic':dy(a.lower()),'upper_dyadic':dy(a.upper())}

class Source:
    def __init__(self, control, bits, terms):
        self.control=control; self.pi=arb.pi(); self.a=arb(41).log()/2 if control else arb(0)
        self.c=rat('1/2') if control else arb(0); self.n=terms; self.tol=arb(2)**(-(bits-40))
        p=self.pi; m=terms+1
        q=(arb(m+1)/m)**4*(-p*(2*m+1)).exp()
        require(2*p>3 and 4*p*m*m>9 and q<1,'Theta-index positivity and majorant domain')
        require(16*(-3*p).exp()<rat('1/2'),'Full-source majorant domain')
        require(not control or self.a>1,'Odd absolute-moment finite callback domain')
        self.B=2*p*p*m**4*(-p*m*m).exp()/(1-q)
        self.payments=[]
    def phi(self,v):
        p=self.pi
        return sum((2*p*p*n**4*(9*v).exp()-3*p*n*n*(5*v).exp())*(-p*n*n*(4*v).exp()).exp() for n in range(1,self.n+1))
    def integrate(self,t,x,j,moment=False):
        a=self.a;p=self.pi;c=self.c
        def wave(r,ab,rj):
            if moment:
                return ab**j*(t*r*r).exp()
            phase=x*r
            trig=(phase.cos(),-phase.sin(),-phase.cos(),phase.sin())[j%4]
            return rj**j*(t*r*r).exp()*trig
        def f(v,analytic):
            # Entire callbacks; abs(v-a)=a-v is valid on 0<=v<=1<a.
            z=wave(v,v,v)
            if self.control:
                z+=c/2*(wave(v+a,v+a,v+a)+wave(v-a,a-v,v-a))
            return self.phi(v)*z
        finite=acb.integral(f,0,1,rel_tol=self.tol,abs_tol=self.tol,eval_limit=100000,depth_limit=30)
        require(finite.is_finite() and finite.imag.contains(0),'Finite real validated integral')
        D=self.B*(1+c)*(1+a)**j*(t*(1+a)**2).exp()
        slope=4*p*arb(4).exp()-9-2*t*(1+a)-arb(j)/(1+a)
        require(slope>0 and 16*p*arb(4).exp()>2*t,'Infinite-tail monotonicity')
        tail=(1+c)*4*p*p*(1+a)**j*(9+t*(1+a)**2-p*arb(4).exp()).exp()/slope
        full=finite.real+arb(0,(D+tail).upper())
        self.payments.append({'kind':'moment' if moment else 'jet','order':j,'finite':enc(finite.real),'theta_index_payment':enc(D),'infinite_source_and_shift_tail':enc(tail),'slope':enc(slope),'full':enc(full)})
        return full

def case(name,control,stationary_order,x0s,dxs,dts,bits,terms):
    t0=rat('1/5');x0=rat(x0s);dx=rat(dxs);dt=rat(dts)
    source=Source(control,bits,terms)
    # Enough central jets for first-order parameter transport of j<=3.
    jets=[source.integrate(t0,x0,j) for j in range(6)]
    moments=[source.integrate(t0+dt,arb(0),j,moment=True) for j in range(8)]
    require(all(m>0 for m in moments),'All absolute moments positive')
    def transported(j,xoffset):
        # Multivariate Taylor with integral remainder along the straight
        # (t,x) segment: d/dt H_j=-H_{j+2}. Moments bound all x derivatives.
        do_t=arb(0,dt.upper())
        v=jets[j]+xoffset*jets[j+1]-do_t*jets[j+2]
        ax=abs(xoffset)
        remainder=(ax*ax*moments[j+2]/2+ax*dt*moments[j+3]+dt*dt*moments[j+4]/2)
        return v+arb(0,remainder.upper())
    whole=[transported(j,arb(0,dx.upper())) for j in range(4)]
    left=transported(stationary_order,-dx);right=transported(stationary_order,dx)
    deriv=whole[stationary_order+1]
    require((left<0 and right>0 and deriv>0) or (left>0 and right<0 and deriv<0),'Unique uniform stationary branch')
    j=stationary_order-1
    stationary_laguerre=-whole[j]*whole[j+2]
    if control:
        require(stationary_laguerre < -rat('4/1000000'),'Control stationary negative margin')
    else:
        require(stationary_laguerre>0,'Genuine stationary positive margin')
    return {'name':name,'control':control,'stationary_derivative_order':stationary_order,'parameters':{'t0':'1/5','t_radius':dts,'x0':x0s,'x_radius':dxs,'p':41 if control else None,'c':'1/2' if control else '0','U':'1','theta_terms':terms},'center_jets':[enc(v) for v in jets],'absolute_moments_at_tmax':[enc(v) for v in moments],'uniform_jets':[enc(v) for v in whole],'stationarity_endpoint_left':enc(left),'stationarity_endpoint_right':enc(right),'stationarity_derivative':enc(deriv),'stationary_L'+str(j):enc(stationary_laguerre),'integrals_and_payments':source.payments,'checks':{'unique_stationary_curve_at_every_time':True,'implicit_function_hypothesis':True,'theta_index_and_full_shift_tails_paid':True,'t_x_Taylor_remainder_paid':True,'signed_stationary_margin':True}}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);ap.add_argument('--precision',type=int,default=160);ap.add_argument('--theta-terms',type=int,default=4);args=ap.parse_args()
    require(args.precision>=128 and args.theta_terms>=4,'Certificate settings');ctx.prec=args.precision
    cases=[case('theta stationary H near 31.05754',False,1,'31.05753718634','1/100000','1/1000000',args.precision,args.theta_terms),case('theta stationary H_x near 9.48225',False,2,'9.4822468462','1/10000','1/1000000',args.precision,args.theta_terms),case('Euler p=41 c=1/2 stationary H',True,1,'1.68413603215','1/1000000','1/1000000',args.precision,args.theta_terms)]
    r={'schema':'inv20-stationary-operator-controls-v1','date':'2026-10-14','provenance':{'prepared_for':'Edward Baker','llm_assistance':'gpt-6.1-sol (Codex)','reasoning_effort':'ultra'},'runtime':{'python':platform.python_version(),'python_flint':flint.__version__},'checker':{'file':Path(__file__).name,'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},'precision_bits':args.precision,'quadrature':{'tolerance_bits':args.precision-40,'eval_limit':100000,'depth_limit':30},'normalization':'H=int_0^infinity Phi(u) exp(t u^2) cos(xu) du; full even-source shifts for control','cases':cases,'status':'PASS','scope':'Three thin compact stationary boxes. Local signs and operator-ansatz screen, not a global theta factorization or RH theorem.'}
    s=json.dumps(r,indent=2,sort_keys=True)+'\n'
    if args.output: args.output.write_text(s)
    print(json.dumps({'status':r['status'],'cases':[{k:v for k,v in c.items() if k in ('name','stationarity_endpoint_left','stationarity_endpoint_right','stationary_L0','stationary_L1')} for c in cases]},indent=2))
if __name__=='__main__':main()
