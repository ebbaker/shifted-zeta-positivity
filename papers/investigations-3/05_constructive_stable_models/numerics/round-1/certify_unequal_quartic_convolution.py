#!/usr/bin/env python3
"""Exact rational local certificate for an unequal pure-quartic convolution.

2026-10-17. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model gpt-6.1-sol (Codex), reasoning effort ultra.
Same-model research preparation, not a formal review.

Retained contract: stdlib Fraction arithmetic only, delta=1/4, degree 6,
exactly three coefficients, no parameter grid or refinement. The formulas
and a floating scout preceded this retained verification. No quadrature,
special-function evaluation, or theta fitting is part of this certificate.

If X,Y are independent with density proportional to exp(-x^4), put
S=X+Y/4 and V(s)=-log density(S). For A=1+(1/4)^4 and
n=Gamma(3/4)/(sqrt(A)*Gamma(1/4)), Cauchy and integration by parts give
1/4<n<1/2. Taylor coefficients are polynomials in n over the rationals.
"""
from fractions import Fraction as F
from math import factorial
import hashlib
import json
from pathlib import Path
import platform
import argparse


def add(p, q):
    r = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += x
    return r


def scale(p, x):
    return [v*x for v in p]


def mul(p, q):
    r = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return r


def polynomial_range(p, lower, upper):
    lo = hi = F(0)
    for i, x in enumerate(p):
        pair = sorted([x*lower**i, x*upper**i])
        lo += pair[0]
        hi += pair[1]
    return lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    delta = F(1, 4)
    A = 1+delta**4

    # Under density proportional exp(-A*y^4):
    # E y^(4l)=(1/4)_l/A^l; E y^(4l+2)=n*(3/4)_l/A^l.
    def moment(j):
        assert j % 2 == 0
        k = j//4
        r = F(1)
        if j % 4 == 0:
            for z in range(k):
                r *= F(1, 4)+z
            return [r/A**k]
        for z in range(k):
            r *= F(3, 4)+z
        return [F(0), r/A**k]

    coeff = {}
    for degree in [2, 4, 6]:
        total = [F(0)]
        for k1 in range(degree+1):
            for k2 in range(degree//2+1):
                for k3 in range(degree//3+1):
                    for k4 in range(degree//4+1):
                        if k1+2*k2+3*k3+4*k4 != degree:
                            continue
                        weight = (4*delta**3)**k1*(-6*delta**2)**k2
                        weight *= (4*delta)**k3*(-1)**k4
                        weight /= factorial(k1)*factorial(k2)*factorial(k3)*factorial(k4)
                        total = add(total, scale(moment(3*k1+2*k2+k3), weight))
        coeff[degree] = total
    v2 = scale(coeff[2], -1)
    v4 = add(scale(coeff[4], -1), scale(mul(coeff[2], coeff[2]), F(1, 2)))
    v6 = add(add(scale(coeff[6], -1), mul(coeff[2], coeff[4])),
             scale(mul(mul(coeff[2], coeff[2]), coeff[2]), -F(1, 3)))
    assert v2 == [F(0), F(96, 257)]
    assert v4 == [F(16417024, 16974593), F(0), F(4608, 66049)]
    assert v6 == [F(0), -F(2130739200, 4362470401), F(0), F(294912, 16974593)]
    # Strict Cauchy gives 1/12<m^2<1/4. The inequalities below imply
    # 1/16<n^2<1/4 and therefore 1/4<n<1/2.
    assert F(1, 12)/A > F(1, 16)
    assert F(1, 4)/A < F(1, 4)
    outer = {'s2': (F(9, 100), F(19, 100)),
             's4': (F(97, 100), F(99, 100)),
             's6': (-F(1, 4), -F(11, 100))}
    rows = []
    for label, polynomial in [('s2', v2), ('s4', v4), ('s6', v6)]:
        lo, hi = polynomial_range(polynomial, F(1, 4), F(1, 2))
        assert lo > outer[label][0]
        assert hi < outer[label][1]
        rows.append({'coefficient': label,
                     'polynomial_in_n': [str(x) for x in polynomial],
                     'exact_interval': [str(lo), str(hi)],
                     'strict_rational_outer_interval': [str(x) for x in outer[label]],
                     'verified': True})
    record = {
        'date': '2026-10-17', 'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial LLM assistance; same-model preparation, not formal review.',
        'recorded_parent_model': 'gpt-6.1-sol (Codex)',
        'recorded_reasoning_effort': 'ultra',
        'status': 'exact rational certificate',
        'contract': {'delta_exact': '1/4', 'max_taylor_degree': 6,
                     'coefficient_count': 3, 'arithmetic': 'stdlib fractions.Fraction',
                     'quadrature': False, 'parameter_grid': False,
                     'termination': 'fixed three coefficient calculations, no refinement'},
        'scout_and_retained_run': 'Analytic derivation and a floating scout preceded this retained exact verification.',
        'python_version': platform.python_version(),
        'source_filename': Path(__file__).name,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'parameter_A_exact': str(A),
        'auxiliary_n': 'Gamma(3/4)/(sqrt(A)*Gamma(1/4))',
        'proved_auxiliary_n_interval': ['1/4', '1/2'],
        'rows': rows,
        'scope': 'An independent two-pure-quartic convolution has positive quartic and negative sixth potential coefficients. No theta matching or approximation claim.'}
    formatted = json.dumps(record, indent=2)+'\n'
    if args.output:
        args.output.write_text(formatted)
    else:
        print(formatted, end='')


if __name__ == '__main__':
    main()
