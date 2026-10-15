#!/usr/bin/env python3
"""One bounded positive tail-cone certificate, near the first theta real zero.

15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra, effort ultra. Requires python-flint 0.9.0.
No remote data. Run with --output receipt.json. All decimals below are exact.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb, acb, ctx


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--bits',type=int,default=160)
    args=parser.parse_args(); ctx.prec=args.bits
    started=time.monotonic(); checks=[]; records=[]
    def check(label,condition):
        if not condition: raise AssertionError(label)
        checks.append(label)
    def rec(x): return x.str(35,more=True)
    pi=arb.pi(); T=arb('0.011'); tc=arb('0.01'); xc=arb('28.3')
    dt=arb('0.001'); dx=arb('0.1'); X=arb('28.4'); U=arb(1)
    # n=1 is the fixed head; n=2,3,4 are optional cone diagnostics.
    N=1; M=4
    def beta(n):
        a=pi*n*n
        return (4*a-1)*(-a).exp()
    def primitive_radius(n):
        d=4*pi*n*n-1
        return ((1+2*T+X*X)/(d*d)+8*(T*T+T*X*X)/d**4)/8
    def derivative_radius(n):
        d=4*pi*n*n-1
        return (2*X/d**2+2*X*(1+10*T+X*X)/d**4+96*T*T*X/d**6)/8
    def tail(n):
        # Valid for j<=5, |sin|,|cos|<=1, t<=1/4 on u>=1.
        a=pi*n*n
        return a/(4*a-1)*(a-4-a*arb(4).exp()/2).exp()
    check('positive_time_box',tc-dt>0)
    check('source_upper_time_at_most_quarter',T<=arb(1)/4)
    check('source_tail_envelope_for_moments_through_five',
          (-arb(2)).exp()/4+14*(-arb(3)).exp()<pi/2)
    check('uniform_primitive_moment_condition',pi>=T/8)
    f47=Fraction(47*(47-2),(47+1)**2)-Fraction(1806,47**2)-Fraction(12,47**4)
    check('broad_rectangle_exact_rational_threshold',f47==Fraction(125421739,1249198336))
    check('broad_rectangle_exact_rational_margin',f47-Fraction(1,10)==Fraction(2509527,6245991680))
    check('broad_rectangle_margin_positive',f47>Fraction(1,10))
    # d^4 L(d)=d(d-2)*(d/(d+1))^2 is increasing for d>2.
    # The competing 1+10T+2X^2+48T^2/d^2 is decreasing.
    d2=4*pi*4-1
    signed_bracket=d2**3*(d2-2)/(d2+1)**2-(1+10*T+2*X*X+48*T*T/d2**2)
    check('all_n_ge_two_tail_derivatives_strictly_negative',signed_bracket>0)
    check('tail_threshold_d_exceeds_two',d2>2)
    integral_count=0
    def integral(n,j,x,t,label):
        nonlocal integral_count
        a=pi*n*n; d=4*a-1
        def integrand(u,analytic):
            q=(4*u).exp()
            z=(t*u*u+u-a*(q-1)).exp()*(2*a*a*q*q-3*a*q)*u**j/d
            if x is not None:
                phase=x*u
                z *= (phase.cos(),-phase.sin(),-phase.cos(),phase.sin())[j%4]
            return z
        z=acb.integral(integrand,0,U,abs_tol=arb('1e-38'),rel_tol=arb('1e-30'),
                       eval_limit=200000,depth_limit=30)
        check('finite_real_integral_'+str(integral_count),z.is_finite() and z.imag.contains(0))
        out=z.real+arb(0,tail(n)); integral_count+=1
        records.append({'label':label,'n':n,'moment_or_jet_order':j,
                        'spectral_parameter':None if x is None else rec(x),
                        'time':rec(t),'complete_source_integral':rec(out),
                        'absolute_source_tail':rec(tail(n))})
        return out
    def evaluate_mode(n):
        c=[integral(n,j,xc,tc,'center_jet') for j in range(4)]
        moments={j:integral(n,j,None,T,'absolute_moment').abs_upper() for j in range(2,6)}
        def second_remainder(j):
            return dx*dx*moments[j+2]/2+dx*dt*moments[j+3]+dt*dt*moments[j+4]/2
        boxes=[c[j]+arb(0,dx*c[j+1].abs_upper()+dt*c[j+2].abs_upper()+second_remainder(j)) for j in range(2)]
        ends={side:c[0]+sgn*dx*c[1]+arb(0,dt*c[2].abs_upper()+second_remainder(0))
              for side,sgn in [('left',-1),('right',1)]}
        return c,moments,boxes,ends
    core_started=time.monotonic()
    head=evaluate_mode(1); head_elapsed=time.monotonic()-core_started
    head_hx=beta(1)*head[2][1]
    check('head_derivative_negative_on_entire_parameter_box',head_hx<0)
    head_margin=-head_hx
    # The cone infimum for lambda=(0,-1) is exactly zero: all finite
    # vectors pair strictly positively, and the included limit is (1/8,0).
    positive_cone_margin=head_margin
    check('positive_tail_cone_separator_strict',positive_cone_margin>0)
    R1=arb(1)/2-beta(1)
    check('complete_tail_mass_positive',R1>0)
    baseline_started=time.monotonic()
    directional_error=R1*derivative_radius(2)
    directional_margin=head_margin-directional_error
    radial_radius=((arb(1)/8+primitive_radius(2))**2+derivative_radius(2)**2).sqrt()
    radial_error=R1*radial_radius
    radial_margin=head_margin-radial_error
    baseline_elapsed=time.monotonic()-baseline_started
    check('ordinary_directional_complete_start_cutoff_also_passes',directional_margin>0)
    check('ordinary_radial_complete_start_cutoff_also_passes',radial_margin>0)
    # Optional finite cone rectangles and root bracket are diagnostic work;
    # neither is required for the preceding separator proof.
    modes={1:head}
    for n in range(2,M+1):
        modes[n]=evaluate_mode(n)
        check('finite_tail_mode_negative_derivative_'+str(n),modes[n][2][1]<0)
    RM=arb(1)/2-sum((beta(n) for n in range(1,M+1)),arb(0))
    check('infinite_remaining_mode_mass_positive',RM>0)
    inf_h=arb(1)/8+arb(0,primitive_radius(M+1))
    inf_hx=arb(0,derivative_radius(M+1))
    root_ends={side:sum((beta(n)*modes[n][3][side] for n in range(1,M+1)),arb(0))+RM*inf_h
               for side in ['left','right']}
    check('complete_theta_positive_at_left_for_all_times_in_box',root_ends['left']>0)
    check('complete_theta_negative_at_right_for_all_times_in_box',root_ends['right']<0)
    # Actual equal theta coefficients are a member of the positive relaxation.
    # The already proved derivative sign makes this bracketed root unique
    # within the box, for every heat time in the interval.
    finite_rectangles={str(n):{'Hn_over_beta':rec(modes[n][2][0]),
                             'Hnx_over_beta':rec(modes[n][2][1])} for n in range(2,M+1)}
    record={
      'date':'2026-10-15','prepared_for':'Edward Baker',
      'llm_assistance':'Substantial LLM assistance; analytic tail estimates plus Arb/Acb validation.',
      'model':'gpt-6-astra','reasoning_effort':'ultra',
      'checker':Path(__file__).name,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'python_version':platform.python_version(),'python_flint_version':flint.__version__,
      'precision_bits':args.bits,'elapsed_seconds':time.monotonic()-started,
      'exact_box':{'t':['0.009','0.011'],'x':['28.2','28.4']},
      'fixed_head_modes':N,'optional_finite_tail_modes':[2,3,4],
      'separator_exact':['0','-1'],'selection':'Frozen after center-mode exploration; no optimization is executed by this checker.',
      'source_cutoff_exact':'1','source_tail_bound':'pi*n^2/(4*pi*n^2-1)*exp(pi*n^2-4-pi*n^2*exp(4)/2), valid for moments 0 through 5.',
      'uniform_parameter_enclosure':'Second-order two-variable Taylor bound from midpoint jets; heat derivative is minus second spatial derivative, absolute moments bound the full Hessian.',
      'analytic_infinite_tail_orientation':{
          'range':'all integers n>=2','d':'4*pi*n^2-1',
          'broader_rectangle_exact':{'t':['0','1/2'],'x':['0 exclusive','30']},
          'broader_rectangle_bound':'-Hnx/beta > x/(40*d^2) for every n>=2',
          'rational_threshold_f47':str(f47),'rational_margin_above_one_tenth':str(f47-Fraction(1,10)),
          'inequality':'-Hnx/beta >= x/4 * ((d-2)/(d*(d+1)^2) - (1+10*T+2*X^2)/d^4 - 48*T^2/d^6)',
          'scaled_bracket_lower_test_at_n2':rec(signed_bracket),
          'monotonic_extension':'d^4 L(d)=d(d-2)*(d/(d+1))^2 increases for d>2; opposing bound decreases.'},
      'finite_tail_rectangles':finite_rectangles,
      'infinite_tail_rectangle_n_ge_5':{'Hn_over_beta':rec(inf_h),'Hnx_over_beta':rec(inf_hx),
          'additional_sign':'Hnx_over_beta<0 for every finite n; zero included only in closure.'},
      'required_limit_point_exact':['1/8','0'],
      'limit_proof':'Displayed primitive envelopes shrink as n^-4 uniformly on the entire parameter box.',
      'tail_mass_R1':rec(R1),'tail_mass_after_4':rec(RM),
      'head_Hx_on_box':rec(head_hx),'positive_cone_infimum_exact':'0',
      'positive_tail_cone_margin':rec(positive_cone_margin),
      'ordinary_directional_tail_error':rec(directional_error),
      'ordinary_directional_margin':rec(directional_margin),
      'ordinary_radial_tail_error':rec(radial_error),'ordinary_radial_margin':rec(radial_margin),
      'complete_theta_root_endpoints':{k:rec(v) for k,v in root_ends.items()},
      'cost':{'core_head_integrals':8,'optional_diagnostic_integrals':integral_count-8,
              'head_enclosure_seconds':head_elapsed,'ordinary_tail_envelopes_seconds':baseline_elapsed,
              'cone_extra_tail_integrals':0,'ordinary_extra_tail_integrals':0,
              'assessment':'Both ordinary cutoff comparisons already pass with the same head enclosure; no computational advantage demonstrated.'},
      'assertions_passed':len(checks),'checks':checks,'integrals':records,
      'failed_candidates':[],
      'establishes':[
          'Every normalized positive-tail relaxation with a1=1 has Hx<0 throughout the exact box; hence no collision there.',
          'In fact normalization is unnecessary for the sign conclusion: any nonnegative tail weights with a1=1 and convergent derivative transform have Hx bounded above by the strictly negative head.',
          'The actual theta field has exactly one real zero in the declared x interval for every t in the declared time interval; this is a local bracket, without a proof that it is globally the first zero.',
          'The entire normalized tail cone is enclosed, including all infinite mode/source tails and the limit (1/8,0).'],
      'does_not_establish':[
          'Any all-event signed arithmetic boundary estimate, global noncollision result, or RH conclusion.',
          'Theta-specific arithmetic discrimination: recurrence and endpoint normalization are not needed for the successful separator sign.',
          'A practical advantage over ordinary complete-start cutoff enclosures; both tested baselines pass.']}
    text=json.dumps(record,indent=2)+'\n'
    if args.output: args.output.write_text(text)
    else: print(text,end='')
    print('PASS:',len(checks),'assertions;',integral_count,'integrals; cone margin',positive_cone_margin,
          '; directional baseline',directional_margin,'; radial baseline',radial_margin)
if __name__=='__main__': main()
