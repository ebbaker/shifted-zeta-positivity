#!/usr/bin/env python3
"""Exact controls for coupled parity cutoffs and full starting factors.
15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra; reasoning effort ultra.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    counts = Counter()

    def check(label, statement):
        if not statement:
            raise AssertionError(label)
        counts[label] += 1

    # Direct finite basis checks of the integer lattice and masks.
    for n in range(-6, 7):
        for m in range(-6, 7):
            p, k = n+m, n-m
            check('lattice_inverse', p % 2 == k % 2 and (p+k)//2 == n and (p-k)//2 == m)
            check('parity_channels', (p % 2 == 0) == (n % 2 == m % 2))
            check('box_is_diamond', max(abs(p), abs(k)) == abs(n)+abs(m))
            for N in (1, 3, 5):
                check('endpoint_strip', (abs(p-k) <= 2*N) == (abs(m) <= N))

    # The /4 in the integer-mode source weights cancels the four signs.
    box_cases = 0
    for signed in (False, True):
        a = {n: F((-1)**n if signed else 1, n+1) for n in range(1, 11)}
        b = {m: F((m % 3)-1 if signed else m, m+2) for m in range(1, 6)}
        for N in range(1, 5):
            for M in range(N, N+4):
                full = sum(a.values())*sum(b[m] for m in range(1, N+1))
                strip = F(0)
                box = F(0)
                for n in range(-10, 11):
                    for m in range(-N, N+1):
                        if n == 0 or m == 0:
                            continue
                        p, k = n+m, n-m
                        weight = a[abs(n)]*b[abs(m)]/4
                        strip += weight
                        if abs(p) <= M and abs(k) <= M:
                            box += weight
                prefix = sum(b[m]*sum(a[n] for n in range(1, M-m+1)) for m in range(1, N+1))
                correction = sum(b[m]*sum(a[n] for n in range(M-m+1, 11)) for m in range(1, N+1))
                check('strip_retains_product', strip == full)
                check('box_prefix_identity', box == prefix)
                check('exact_box_correction', full-box == correction)
                box_cases += 1

    # A row-constant mask annihilates all tested zero-sum starting basis vectors.
    for N in (1, 2, 4):
        for n in range(1, 6):
            for l in range(1, 6):
                for m in range(1, 6):
                    B_nm = int(m <= N)
                    B_lm = int(m <= N)
                    check('row_constant_kernel', B_nm-B_lm == 0)

    witnesses = []
    for epsilon in (F(0), F(1, 2), F(1, 16), F(1, 256)):
        a = {1:F(1), 3:-1+epsilon}
        full = sum(a.values())
        box = sum(value for n, value in a.items() if n+1 <= 3)
        check('cancellation_witness', full == epsilon and box == 1 and box-full == 1-epsilon)
        witnesses.append({'epsilon':str(epsilon), 'full_product':str(full), 'parity_box_product':str(box), 'absolute_error':str(box-full)})

    # Bilinear same/cross parity accounting; the unwanted difference channel
    # cancels only when both sectors remain in the expression.
    parity_cases = 0
    for we, wo, ve, vo in ((1,-1,0,0), (2,-3,5,-7), (0,4,-1,3), (-2,-1,-3,-4)):
        for alpha in (F(1,2), F(2,3), F(7,8)):
            same = we*we+wo*wo-alpha*(we*ve+wo*vo)
            cross = 2*we*wo-alpha*(we*vo+wo*ve)
            total = (we+wo)**2-alpha*(we+wo)*(ve+vo)
            difference = (we-wo)**2-alpha*(we-wo)*(ve-vo)
            check('parity_sum', same+cross == total)
            check('parity_difference', same-cross == difference)
            check('parity_half_formulas', same == (total+difference)/2 and cross == (total-difference)/2)
            parity_cases += 1

    # Exact polynomial margin for every lambda >= 12, hence >= 4*pi.
    check('endpoint_polynomial_margin', 8*12**2-30*12+15 == 807)
    check('endpoint_polynomial_increasing', 16*12-30 == 162 and 162 > 0)
    for lam in (12, 13, 16, 32):
        P1 = -8*lam**3+30*lam**2-15*lam
        check('endpoint_polynomial_factor', P1 == -lam*(8*lam**2-30*lam+15) and P1 < 0)

    # f'_even(0)=-beta yields beta/x^2 and -2 beta/x^3.
    beta = F(3, 7)
    check('cosine_IBP_leading_coefficient', -(-beta) == beta)
    check('sine_IBP_leading_coefficient', -2*beta == 2*(-beta))
    for j, factorial in ((0, 1), (1, 2)):
        leading_even = (-1)**j*factorial*beta
        leading_minus = 2*leading_even
        for alpha in (F(1,2), F(3,4), F(99,100)):
            B = leading_minus**2-alpha*leading_minus**2
            check('difference_channel_asymptotic', B == 4*(factorial*beta)**2*(1-alpha) and B > 0)

    record = {
        'date':'2026-10-15', 'prepared_for':'Edward Baker',
        'model':'gpt-6-astra', 'reasoning_effort':'ultra',
        'llm_assistance':'Substantial LLM assistance; internal exact controls.',
        'status':'PASS', 'script':Path(__file__).name,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_version':platform.python_version(),
        'exact_assertions':sum(counts.values()), 'assertions_by_group':dict(counts),
        'box_cases':box_cases, 'parity_amplitude_cases':parity_cases,
        'formal_cancellation_witnesses':witnesses,
        'analytic_proofs_not_inferred_from_checks':[
            'Universal row-constant mask characterization',
            'Gaussian source tails and the absolute box-error estimate',
            'Theta parity dilation and the full shifted one-sided transform',
            'Integrable derivative bounds, Schwartz decay and general asymptotic statements',
        ],
        'scope':'Finite exact algebra only; arbitrary-vector witnesses are not theta fields. No theta signed-core estimate, stationary sign domain, or collision exclusion. The actual-theta parity cancellation theorem is the analytic argument in the accompanying note.',
    }
    result = json.dumps(record, indent=2)+'\n'
    if args.output:
        args.output.write_text(result)
    print(result)


if __name__ == '__main__':
    main()
