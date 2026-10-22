#!/usr/bin/env python3
"""BW14 two-endpoint constants and complete-tail checks, 21 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Authoring model gpt-6-astra (Codex), recorded effort max.
Requires python-flint 0.9.0. No oscillatory integral or zero search.
Analytic statements and scope: ../notes/01_TWO_ENDPOINT_TAIL_CONSTRAINT_20261021.md.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import flint
from flint import arb, ctx, fmpq_poly


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def show(x):
    return x.str(48, more=True)


def run(bits):
    ctx.prec = bits
    pi = arb.pi()
    half = arb(1) / 2

    # Exact differentiation of e^(u-a) P(a), with a'=4a.
    a = fmpq_poly([0, 1])
    P = 2*a*a - 3*a
    derivative = (1-4*a)*P + 4*a*P.derivative()
    require(derivative == -8*a**3+30*a*a-15*a, 'source derivative')
    require((4*a-1)*(2*a*a-7*a+2)+2 == -derivative,
            'rational endpoint quotient')

    def beta(n):
        lam = pi*n*n
        return (4*lam-1)*(-lam).exp()

    def ratio(n):
        lam = pi*n*n
        return 2*lam*lam-7*lam+2+2/(4*lam-1)

    def gamma(n):
        return beta(n)*ratio(n)

    R = half-beta(1)
    R2 = R-beta(2)
    G = -gamma(1)
    delta = ratio(3)-ratio(2)
    S = G-ratio(2)*R
    M = S/delta
    require(R > 0 and R2 > 0 and G > 0 and delta > 0 and S > 0,
            'positive moments and gap')
    require(0 < M and M < R, 'nonnegative extremizer')
    require(R/M > 2916280 and R/M < 2916281, 'mass reduction')
    require(M/R2 > 1 and M/R2 < arb('1.000000001414'),
            'same-coefficient direct comparison')
    require(M-R2 > 0, 'strict loss to the direct mass')

    # Independent complete positive sums through 5, all omitted n>=6 paid.
    m = 6
    lam = pi*m*m
    qb = (arb(m+1)/m)**2 * (-pi*(2*m+1)).exp()
    qg = (arb(m+1)/m)**6 * (-pi*(2*m+1)).exp()
    require(qb < 1 and qg < 1, 'infinite mode ratios')
    tb = (4*lam*(-lam).exp()/(1-qb)).upper()
    tg = (8*lam**3*(-lam).exp()/(1-qg)).upper()
    bs = sum((beta(n) for n in range(1,m)), arb(0))
    gs = sum((gamma(n) for n in range(1,m)), arb(0))
    require(arb(bs,tb).contains(half), 'complete primitive normalization')
    require(arb(gs,tg).contains(0), 'complete reflection derivative')
    spos = sum((beta(n)*(ratio(n)-ratio(2)) for n in range(3,m)), arb(0))
    require(arb(spos,tg).overlaps(S), 'positive surplus evaluation')
    r2sum = sum((beta(n) for n in range(3,m)), arb(0))
    require(arb(r2sum,tb).overlaps(R2), 'direct mass evaluation')

    # These are the predeclared complex-domain envelopes, no point sampling.
    T, Z, Y = half, arb(31), arb(1)
    def widths(n):
        lam = pi*n*n
        d = 4*lam-1
        D = d-Y
        require(lam > T/8 and D > 0, 'complex moment domain')
        aa = ((1+2*T+Z*Z)/(d*D)
              +8*(T*T+T*Z*Z)/(d*D**3))/8
        bb = (2*Z/(d*D)
              +2*Z*(1+10*T+Z*Z)/(d*D**3)
              +96*T*T*Z/(d*D**5))/8
        return aa, bb

    a2,b2 = widths(2)
    a3,b3 = widths(3)
    C0,C1 = a2+a3,b2+b3
    C = (C0*C0+C1*C1).sqrt()
    one = R*C
    two = M*C
    direct = R2*C
    require(one > two and two > direct, 'uniform allowance ordering')
    require(M < arb('5.891258863e-11') and R > arb('1.718056625e-4'),
            'published mass bounds')
    require(one < arb('1.041323e-5') and two < arb('3.570720e-12'),
            'published vector allowance bounds')
    require(M*C0 < arb('3.557128e-12') and M*C1 < arb('3.112519e-13'),
            'published component allowance bounds')

    # Exact coefficient constraints for the mass-maximizing two-atom tail.
    w2,w3 = R-M,M
    require(w2 > 0 and w3 > 0, 'positive relaxed weights')
    require((w2+w3-R).contains(0), 'extremizer total mass')
    require((ratio(2)*w2+ratio(3)*w3-G).contains(0),
            'extremizer reflection moment')
    # A second admissible noncanonical tail, supported on 2 and 4.
    w4 = S/(ratio(4)-ratio(2))
    require(0 < w4 and w4 < M, 'distinct feasible source')
    require((ratio(2)*(R-w4)+ratio(4)*w4-G).contains(0),
            'second extremizer moment')

    return {
        'status':'passed', 'date':'2026-10-21',
        'prepared_for':'Edward Baker',
        'model':'gpt-6-astra', 'reasoning_effort':'max',
        'review':'same-assistant only; no independent specialist review',
        'python':platform.python_version(), 'python_flint':flint.__version__,
        'precision_bits':bits,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'domain':{'abs_t':'1/2','abs_Re_z':'30','abs_Im_z':'1','Z_majorant':'31'},
        'constants':{k:show(v) for k,v in {
            'R':R,'G':G,'r2':ratio(2),'r3':ratio(3),'Delta':delta,
            'S':S,'M_two_endpoint':M,'R2_direct':R2,
            'one_to_two_mass_ratio':R/M,'two_to_direct_ratio':M/R2,
            'strict_mass_excess':M-R2,'C0':C0,'C1':C1,'C_euclidean':C,
            'one_endpoint_allowance':one,'two_endpoint_allowance':two,
            'direct_allowance':direct,
            'two_endpoint_value_allowance':M*C0,
            'two_endpoint_derivative_allowance':M*C1,
            'extremizer_a2':w2/beta(2),'extremizer_a3':w3/beta(3),
            'alternate_tail_w4':w4}.items()},
        'complete_tail_check':{
            'finite_modes':'1..5','first_omitted_mode':m,
            'beta_tail_upper':show(tb),'gamma_tail_upper':show(tg),
            'beta_ratio_upper':show(qb.upper()),'gamma_ratio_upper':show(qg.upper()),
            'positive_surplus_core':show(spos)},
        'scope':[
            'Analytic coefficient-constraint and complete complex-domain error bounds.',
            'No theta head quadrature, collision exclusion, or global simplicity claim.',
            'Finite-prime collision controls can satisfy both endpoint constraints.',
            'Direct equal-coefficient arithmetic is strictly sharper for this shared envelope.'
        ]}


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,default=192)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run(args.bits)
    payload=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.write_text(payload)
    print(payload)
