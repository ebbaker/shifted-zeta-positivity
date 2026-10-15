#!/usr/bin/env python3
"""Certified square-support collision retaining the first source endpoint.

15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra; reasoning effort ultra. Requires python-flint.
The constructed weights and final positive normalization are independent of
heat time. Only their construction uses the fixed target time T=1/4.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import time
import flint
from flint import arb, acb, ctx


def ball_record(a):
    return a.str(35, more=True)


def source_polynomial(order):
    """P_k with d_u^k[e^u(2a^2-3a)e^-a]=e^u e^-a P_k(a), a'=4a."""
    p={2: 2, 1: -3}
    for _ in range(order):
        q={}
        for degree, coeff in p.items():
            q[degree]=q.get(degree,0)+(1+4*degree)*coeff
            q[degree+1]=q.get(degree+1,0)-4*coeff
        p={k:v for k,v in q.items() if v}
    return p


def evaluate_polynomial(p,a):
    return sum((v*a**k for k,v in p.items()),arb(0))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--bits',type=int,default=160)
    args=parser.parse_args()
    started=time.monotonic()
    ctx.prec=args.bits
    pi=arb.pi(); T=arb(1)/4
    xl,xr=arb('44.1303'),arb('44.1304')
    xc=(xl+xr)/2; rho=(xr-xl)/2
    checks=[]; evaluations=[]

    def check(label,statement):
        if not statement:
            raise AssertionError(label)
        checks.append(label)

    check('first_source_derivative_polynomial_exact',source_polynomial(1)=={3:-8,2:30,1:-15})
    check('third_source_derivative_polynomial_exact',source_polynomial(3)=={5:-128,4:1440,3:-4232,2:3270,1:-375})
    p1=source_polynomial(1); p3=source_polynomial(3)
    d=[evaluate_polynomial(p1,pi*n*n) for n in (1,2,3)]
    check('first_mode_endpoint_derivative_positive',d[0]>0)
    check('second_mode_endpoint_derivative_negative',d[1]<0)
    check('third_mode_endpoint_derivative_negative',d[2]<0)
    b2=-d[0]/d[1]; b3=-d[0]/d[2]

    # For u>=1 and k<=3, k log u+u^2/4+9u <= e^(2u)/4+12e^u.
    # Divide by e^(4u), use monotonicity, and verify the endpoint constant.
    check('tail_envelope_scalar_inequality',
          (-arb(2)).exp()/4+12*(-arb(3)).exp()<pi/2)

    def tail(n):
        a=pi*n*n
        return a*(a-4-(a/2)*arb(4).exp()).exp()

    def integral(n,k,x=None):
        a=pi*n*n
        def f(u,analytic):
            # Entire in complex u, including the nested exponential.
            q=(4*u).exp()
            z=(T*u*u+u-a*(q-1)).exp()*(2*a*a*q*q-3*a*q)*u**k
            if x is not None:
                phase=x*u
                z *= (phase.cos(),-phase.sin(),-phase.cos(),phase.sin())[k%4]
            return z
        z=acb.integral(f,0,1,rel_tol=arb('1e-32'),abs_tol=arb('1e-36'),
                       eval_limit=200000,depth_limit=30)
        check(f'finite_real_integral_{len(evaluations)}',z.is_finite() and z.imag.contains(0))
        result=z.real+arb(0,tail(n))
        evaluations.append({'n':n,'jet_order':k,
                            'x':None if x is None else ball_record(x),
                            'value_with_complete_tail':ball_record(result),
                            'tail_allowance':ball_record(tail(n))})
        return result

    def combine(jets):
        # G_theta=A+theta B; all raw mode weights become positive when 0<theta<1.
        aa=[jets[0][k]+b3*jets[2][k] for k in range(len(jets[0]))]
        bb=[b2*jets[1][k]-b3*jets[2][k] for k in range(len(jets[0]))]
        return aa,bb

    wronskians={}
    for label,x in [('left',xl),('right',xr)]:
        jets=[[integral(n,k,x) for k in (0,1)] for n in (1,2,3)]
        aa,bb=combine(jets)
        wronskians[label]=aa[1]*bb[0]-aa[0]*bb[1]
    check('wronskian_positive_at_left',wronskians['left']>0)
    check('wronskian_negative_at_right',wronskians['right']<0)

    center=[[integral(n,k,xc) for k in (0,1,2)] for n in (1,2,3)]
    moments=[[integral(n,k,None) for k in (1,2,3)] for n in (1,2,3)]
    # Two nested mean-value bounds retain the small local oscillatory derivative
    # for G and G', while the global positive moments pay derivative variation.
    boxes=[]
    for n in (0,1,2):
        derivative_bounds=[center[n][1].abs_upper()+rho*moments[n][1].abs_upper(),
                           center[n][2].abs_upper()+rho*moments[n][2].abs_upper(),
                           moments[n][2].abs_upper()]
        boxes.append([center[n][k]+arb(0,rho*derivative_bounds[k]) for k in (0,1,2)])
    aa,bb=combine(boxes)
    check('A_negative_throughout_bracket',aa[0]<0)
    check('B_positive_throughout_bracket',bb[0]>0)
    theta=-aa[0]/bb[0]
    check('theta_positive',theta>0)
    check('theta_below_one',theta<1)
    curvature=aa[2]+theta*bb[2]
    check('combined_second_derivative_negative_throughout_bracket',curvature<0)
    dp=aa[2]*bb[0]-aa[0]*bb[2]
    check('wronskian_derivative_negative_throughout_bracket',dp<0)

    normalized_weights=[arb(1),theta*b2,(1-theta)*b3]
    raw_weights=[normalized_weights[n-1]*((n*n-1)*pi).exp() for n in (1,2,3)]
    check('all_three_raw_weights_positive',all(a>0 for a in raw_weights))
    source_first=(-pi).exp()*sum((normalized_weights[n-1]*d[n-1] for n in (1,2,3)),arb(0))
    # Exact vanishing is established by the affine identity, not this ball test.
    check('first_endpoint_ball_consistent_with_exact_zero',source_first.contains(0))
    source_third=(-pi).exp()*sum((normalized_weights[n-1]*evaluate_polynomial(p3,pi*n*n)
                                  for n in (1,2,3)),arb(0))
    check('third_source_endpoint_derivative_negative',source_third<0)
    primitive_first=(-pi).exp()*sum((normalized_weights[n-1]*(1-4*pi*n*n)
                                     for n in (1,2,3)),arb(0))
    check('primitive_first_endpoint_negative',primitive_first<0)
    scale=-1/(2*primitive_first)
    check('primitive_normalization_positive',scale>0)
    scaled_third=scale*source_third
    check('normalization_retains_failed_third_source_endpoint',scaled_third<0)

    record={
        'date':'2026-10-15','prepared_for':'Edward Baker',
        'llm_assistance':'Substantial LLM assistance; exact endpoint algebra and validated finite integration.',
        'model':'gpt-6-astra','reasoning_effort':'ultra',
        'checker':Path(__file__).name,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_version':platform.python_version(),'python_flint_version':flint.__version__,
        'precision_bits':args.bits,'elapsed_seconds':time.monotonic()-started,
        'time':'1/4','x_bracket_exact_decimal':['44.1303','44.1304'],
        'definition':'G_n=exp(pi*n^2)H_n; b_n=-P1(pi)/P1(pi*n^2). G=G_1+theta*b_2*G_2+(1-theta)*b_3*G_3. theta is fixed at the unique bracketed Wronskian root, then held fixed for all heat times.',
        'P1':source_polynomial(1),'P3':source_polynomial(3),
        'b2':ball_record(b2),'b3':ball_record(b3),
        'wronskian_left':ball_record(wronskians['left']),
        'wronskian_right':ball_record(wronskians['right']),
        'wronskian_derivative_on_bracket':ball_record(dp),
        'theta_enclosure':ball_record(theta),
        'raw_square_weights_enclosures':[ball_record(a) for a in raw_weights],
        'combined_second_x_derivative_enclosure':ball_record(curvature),
        'source_first_u_derivative_at_zero':'exactly zero by the displayed affine endpoint identity',
        'source_third_u_derivative_at_zero':ball_record(source_third),
        'primitive_first_u_derivative_at_zero':ball_record(primitive_first),
        'positive_fixed_normalization_for_primitive_endpoint_minus_half':ball_record(scale),
        'scaled_source_third_u_derivative_at_zero':ball_record(scaled_third),
        'assertions_passed':len(checks),'checks':checks,'integrals':evaluations,
        'establishes':[
            'There are fixed positive weights on the first three square nodes producing a nondegenerate double zero at T=1/4 in the declared x bracket.',
            'All support-only nonnegative-polynomial and square-gap localizing inequalities hold, by their exact sum representation.',
            'The first source odd derivative vanishes exactly. Positive fixed scaling gives psi_prime(0)=-1/2 and hence psi_triple_prime(0)=-1/2.',
            'The third source odd derivative does not vanish: full source reflection is not retained.'
        ],
        'does_not_establish':[
            'A theta collision or any RH conclusion.',
            'Failure of a certificate using the full elliptic multiplier, modular reflection, actual equal weights, or the complete odd endpoint hierarchy.',
            'A numerical epsilon threshold for the analytic extension to positive weights at every square node.'
        ]
    }
    text=json.dumps(record,indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
        print(f'PASS: {len(checks)} assertions; theta={theta}; normalized Hxx={curvature}; Phi_triple_prime={source_third}')
    else:
        print(text,end='')

if __name__=='__main__':
    main()
