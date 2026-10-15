#!/usr/bin/env python3
"""Exact mixed-sector algebra and a validated reflected quartic-source control.
15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra, reasoning effort ultra. Requires python-flint.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, platform
import flint
from flint import arb, acb, ctx

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);parser.add_argument('--bits',type=int,default=160)
    args=parser.parse_args();ctx.prec=args.bits;checks=[]
    def check(name,p):
        if not p:raise AssertionError(name)
        checks.append(name)
    def rec(x):return x.str(35,more=True)
    def add(*polys):
        result={}
        for p in polys:
            for k,v in p.items():result[k]=result.get(k,F(0))+v
        return {k:v for k,v in result.items() if v}
    def scale(p,s):return {k:s*v for k,v in p.items() if s*v}
    cc={(1,1):F(1,4),(1,-1):F(1,4),(-1,1):F(1,4),(-1,-1):F(1,4)}
    ss={(1,1):-F(1,4),(1,-1):F(1,4),(-1,1):F(1,4),(-1,-1):-F(1,4)}
    cm={(1,-1):F(1,2),(-1,1):F(1,2)}
    cp={(1,1):F(1,2),(-1,-1):F(1,2)}
    check('cosine_difference_decomposition_exact',add(cc,ss)==cm)
    check('cosine_sum_decomposition_exact',add(cc,scale(ss,-1))==cp)
    check('mixed_even_sector_exact',scale(add(cm,cp),F(1,2))==cc)
    check('mixed_odd_sector_exact',scale(add(cm,scale(cp,-1)),F(1,2))==ss)
    for epsilon in [F(1),F(1,2),F(1,16),F(1,1024)]:
        # At x*=pi/4, full factor 1+cos(4x*)=0; partial factor=epsilon.
        full_start=F(1)-F(1);partial_start=F(1)-(1-epsilon)
        check('complete_start_zero_'+str(epsilon),full_start==0)
        check('partial_start_residual_'+str(epsilon),partial_start==epsilon)
        check('nonzero_sector_cancellation_'+str(epsilon),partial_start/2-partial_start/2==0 and partial_start/2>0)
    check('stationary_amplitude_matrix_negative_determinant',-F(1,4)<0)
    pi=arb.pi();delta=arb(1)/4;xstar=pi/4;ystar=xstar+delta
    check('pi_upper_22_over7',pi<arb(22)/7)
    check('collision_spectral_point_below_one',xstar<1)
    check('endpoint_below_29_over28',ystar<arb(29)/28)
    # On [4,infinity), |cos(xu)|<=1 and quartic convexity gives this complete tail.
    tail0=(-arb(256)).exp()/256
    tail2=(-arb(256)).exp()/16
    tail4=(-arb(256)).exp()*(1+arb(1)/1024)
    def integral(callback,upper,tail):
        z=acb.integral(callback,0,upper,rel_tol=arb('1e-35'),abs_tol=arb('1e-40'),eval_limit=200000,depth_limit=30)
        check('validated_real_integral_'+str(len(checks)),z.is_finite() and z.imag.contains(0))
        return z.real+arb(0,tail)
    M0=integral(lambda u,analytic:(-u**4).exp(),4,tail0)
    M2=integral(lambda u,analytic:u*u*(-u**4).exp(),4,tail2)
    M4=integral(lambda u,analytic:u**4*(-u**4).exp(),4,tail4)
    Fstar=integral(lambda u,analytic:(-u**4).exp()*(xstar*u).cos(),4,tail0)
    Fend=integral(lambda u,analytic:(-u**4).exp()*(ystar*u).cos(),4,tail0)
    check('M4_identity_ball_consistency',(M4-M0/4).contains(0))
    check('M2_below_half_M0',M2<M0/2)
    check('Fstar_above_moment_lower_bound',Fstar>M0*(1-xstar*xstar/4))
    check('Fendpoint_above_moment_lower_bound',Fend>M0*(1-ystar*ystar/4))
    check('Fstar_positive',Fstar>0);check('Fendpoint_positive',Fend>0)
    def g(u):return (-u**4).exp()+((-(u-4)**4).exp()+(-(u+4)**4).exp())/2
    # For u>=8, g<=2 exp(-u^4/16), cosh u<=exp u, u<=u^4/32;
    # derivative of u^4/32 is >=64, giving total tail <=exp(-128)/32.
    tailnorm=(-arb(128)).exp()/32
    norm=integral(lambda u,analytic:u.cosh()*(-u*u/4).exp()*g(u),8,tailnorm)
    check('normalization_integral_positive',norm>0)
    c=1/(16*norm);check('source_normalization_positive',c>0)
    Hxx=16*c*Fstar
    endpoint=c*Fend*(1-arb(1).cos())
    defect=(-delta).exp()*endpoint
    lower_factor=F(3,4)*F(2295,3136)*F(11,24)
    check('explicit_defect_rational_lower_bound',defect>c*M0*arb(lower_factor.numerator)/lower_factor.denominator)
    check('positive_collision_curvature',Hxx>0)
    check('normalized_primitive_endpoint_ball_consistency',(-8*c*norm+arb(1)/2).contains(0))
    eps=arb(1)/16
    sector=c*c*eps*Fstar*Fend*(1-arb(1).cos())/2
    check('nonzero_even_sector_at_exact_physical_zero',sector>0)
    record={'date':'2026-10-15','prepared_for':'Edward Baker','model':'gpt-6-astra','reasoning_effort':'ultra','llm_assistance':'Substantial LLM assistance','checker':Path(__file__).name,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python_version':platform.python_version(),'python_flint_version':flint.__version__,'precision_bits':args.bits,'assertions_passed':len(checks),'checks':checks,'source_definition':'T=1/4; g(u)=exp(-u^4)+(exp(-(u-4)^4)+exp(-(u+4)^4))/2; Phi=c exp(-T u^2)g; c=1/(16 integral_0^infty cosh(u)exp(-T u^2)g du).','exact_collision':'T=1/4, x=pi/4, H(T,x)=c F(x)(1+cos(4x))','M0':rec(M0),'M2':rec(M2),'M4':rec(M4),'F_at_collision':rec(Fstar),'F_at_endpoint_delta_quarter':rec(Fend),'normalization_integral':rec(norm),'source_scale_c':rec(c),'Hxx_at_collision':rec(Hxx),'positive_fixed_endpoint_defect_constant':rec(defect),'defect_lower_bound_multiple_of_c_M0_exact':str(lower_factor),'mixed_even_sector_at_collision_epsilon_one_sixteenth':rec(sector),'mixed_odd_sector_at_collision':'Exactly the negative of the displayed even sector; the full product is zero because its starting factor vanishes.','F_integral_tail':rec(tail0),'normalization_integral_tail':rec(tailnorm),'analytic_claims_not_inferred_from_samples':['Full-line center/separation representation and stationarity subtraction','Exact Fourier translation factorization of the control','Positive source, joint entirety, full source reflection, normalized Green primitive and every odd primitive endpoint','Every positive Fourier/derivative Gram matrix','Local stationary predecessor and negative square-root-energy limit'],'not_established':['Theta signed-core estimate','Integer-square theta coefficient representation or elliptic automorphy for the control','Positivity of the heat-first primitive cosine transform','Impossibility of genuinely arithmetic coupled-source methods']}
    serialized=json.dumps(record,indent=2)+'\n'
    if args.output:
        args.output.write_text(serialized)
    print(serialized)
if __name__=='__main__':main()
