#!/usr/bin/env python3
"""Bounded Arb algebra controls for the analytic corrected RS reference.

Prepared for Edward Baker, 2026-10-23. Substantial LLM assistance:
gpt-6-astra (Codex), effort ultra. These are algebra/normalization controls,
not a high-height theta wall, source-error, or simplicity certificate.
"""
import argparse,hashlib,json,platform,time
from pathlib import Path
import flint
from flint import arb,acb,acb_series,ctx

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path)
    args=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.cap=4
    pi=arb.pi();I=acb(0,1);checks=[];records=[]
    def check(name,ok):
        if not ok:raise AssertionError(name)
        checks.append(name)
    def checkzero(name,v):
        check(name+'_contains_zero',v.contains(0))
        check(name+'_radius_below_1e-40',v.abs_upper()<arb('1e-40'))
    def M0(s):
        return s*(s-1)/16*(2*pi).sqrt()*(-s*pi.log()/2+(s/2-arb(1)/2)*(s/2).log()-s/2).exp()
    def alpha(s):return 1/(2*s)+1/(s-1)+(s/(2*pi)).log()/2
    def ap1(s):return -1/(2*s*s)-1/(s-1)**2+1/(2*s)
    def ap2(s):return 1/s**3+2/(s-1)**3-1/(2*s*s)
    def C0(p):return ((I*pi*(p*p/2+arb(3)/8)).exp()-I*arb(2).sqrt()*(pi*p/2).cos())/(2*(pi*p).cos())
    def Csharp(p):return ((-I*pi*(p*p/2+arb(3)/8)).exp()+I*arb(2).sqrt()*(pi*p/2).cos())/(2*(pi*p).cos())
    def V(v,N):
        p=1+2*N-(2*v/pi).sqrt();c=C0(p);cs=Csharp(p)
        cr=(c+cs)/2;ci=(c-cs)/(2*I)
        return v.sqrt()*(v*cr-ci)
    def prefactor(t,z,N):return -(-1)**N*pi.sqrt()/4*(-pi*z/8-pi*pi*t/64).exp()
    def corr(t,z,N):return prefactor(t,z,N)*V(z/2+pi*t/8,N)
    def term(t,z,n,sign):
        s=(1+sign*I*z)/2;b=alpha(s)-arb(n).log()
        return M0(s)*(-s*arb(n).log()+t*b*b/4).exp()
    for v in [100,125,1000]:
        v=arb(v);u=(-I*(v*(v/(2*pi)).log()/2-v/2-pi/8)).exp()
        lhs=M0(I*v)*u*(I*pi/8).exp()
        rhs=-pi.sqrt()/8*v.sqrt()*(v+I)*(-pi*v/4).exp()
        checkzero('canonical_phase_'+str(v.mid().fmpq()),(lhs-rhs)/rhs)
    # The two local removable values are checked through the independently
    # differentiated numerator/denominator, never division by a zero ball.
    for p in [-arb(1)/2,arb(1)/2]:
        numerator=(I*pi*(p*p/2+arb(3)/8)).exp()-I*arb(2).sqrt()*(pi*p/2).cos()
        denominator=2*(pi*p).cos()
        dn=I*pi*p*(I*pi*(p*p/2+arb(3)/8)).exp()+I*arb(2).sqrt()*pi/2*(pi*p/2).sin()
        dd=-2*pi*(pi*p).sin()
        check('removable_numerator_zero_'+str(p),numerator.contains(0))
        check('removable_denominator_zero_'+str(p),denominator.contains(0))
        checkzero('removable_value_'+str(p),dn/dd-(1-I)/4)
    cases=[(acb(arb(1)/10000),acb(200),3),
           (acb(arb(1)/10),acb(400,arb(3)/5),5),
           (acb(arb(1)/1000,arb(1)/5000),acb(1000,-arb(2)/5),8)]
    for number,(t,z,N) in enumerate(cases):
        # Independently differentiate in time and in space, then compare with
        # differentiation of V in its own variable. No RHS differentiation.
        ts=acb_series([t,1]);zs=acb_series([z,1]);v=z/2+pi*t/8
        ct=corr(ts,z,N)[1];czz=2*corr(t,zs,N)[2]
        vpp=2*V(acb_series([v,1]),N)[2]
        factor=prefactor(t,z,N)
        checkzero('corrected_heat_defect_'+str(number),(ct+czz)/factor-vpp/4)
        # Explicit V derivatives separately versus automatic series algebra.
        p=1+2*N-(2*v/pi).sqrt();ps=acb_series([p,1]);c=C0(ps);cs=Csharp(ps)
        cr=[(c[j]+cs[j])/2 for j in range(3)]
        ci=[(c[j]-cs[j])/(2*I) for j in range(3)]
        q=-1/(2*pi*v).sqrt();sv=v.sqrt()
        vp=arb(3)/2*sv*cr[0]+v*sv*q*cr[1]-ci[0]/(2*sv)-sv*q*ci[1]
        explicit=3*cr[0]/(4*sv)+arb(5)/2*sv*q*cr[1]+v*sv*q*q*(2*cr[2])+ci[0]/(4*v*sv)-q*ci[1]/(2*sv)-sv*q*q*(2*ci[2])
        vseries=V(acb_series([v,1]),N)
        checkzero('V_first_derivative_'+str(number),vp-vseries[1])
        checkzero('V_second_derivative_'+str(number),explicit-2*vseries[2])
        for sign in [-1,1]:
            for n in [1,3,7]:
                g=term(t,z,n,sign)
                gt=term(ts,z,n,sign)[1];gzz=2*term(t,zs,n,sign)[2]
                s=(1+sign*I*z)/2;b=alpha(s)-arb(n).log();d1=ap1(s);d2=ap2(s)
                rhs=-(d1+t*b*b*d1+t*(d1*d1+b*d2)/2+t*t*b*b*d1*d1/4)/4
                checkzero('single_term_heat_defect_'+str(number)+'_'+str(sign)+'_'+str(n),(gt+gzz)/g-rhs)
        records.append({'tau':str(t),'z':str(z),'fixed_N':N,'correction_defect_divided_by_prefactor':str(vpp/4)})
    for x,t,N in [(200,arb(1)/10000,3),(400,arb(1)/10,5),(1000,arb(1)/100,8)]:
        v=arb(x)/2+pi*t/8;p=1+2*N-(2*v/pi).sqrt()
        u=(-I*(v*(v/(2*pi)).log()/2-v/2-pi/8)).exp()
        displayed=2*(-1)**N*(t*pi*pi/64).exp()*(M0(I*v)*C0(p)*u*(I*pi/8).exp()).real
        analytic=corr(acb(t),acb(x),N)
        checkzero('real_axis_corrected_display_'+str(x),(analytic-displayed)/prefactor(acb(t),acb(x),N))
    output={'status':'PASS','date':'2026-10-23','prepared_for':'Edward Baker','model':'gpt-6-astra (Codex)',
        'reasoning_effort':'ultra','llm_assistance':True,'checker':Path(__file__).name,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_version':platform.python_version(),'python_flint_version':flint.__version__,'precision_bits':256,
        'primary_definitions':'https://arxiv.org/html/1904.12438v2, M0 equation(6), Corollary6.4 correction',
        'derivations_tested':['canonical phase and normalization','local removable C0 values',
            'analytic correction agrees with real-axis published display','explicit V first and second derivatives',
            'corrected heat-defect cancellation by independent series derivatives','single-term full-sum heat defect for both carriers'],
        'analytic_cases':records,'assertions':len(checks),'checks':checks,'elapsed_seconds':time.monotonic()-start,
        'scope':'Algebra and normalization controls only. No high-height H-wall lower bound, complex-time imported source estimate, RH, or global simplicity result is asserted.'}
    text=json.dumps(output,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')
if __name__=='__main__':main()
