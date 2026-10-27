#!/usr/bin/env python3
"""Exact finite-algebra and conservative source-budget checks for Notes12-13.

Prepared for Edward Baker with substantial LLM assistance, 27 October 2026.
Recorded model gpt-6.1-sol, actual effort ultra. Standard library only.
No zero search, actual theta interval evaluation, or new excluded slab.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
from math import factorial


def pair_energy(x):
    return sum((1/(x[i]-x[j])**2 for i in range(len(x))
                for j in range(i+1, len(x))), F(0))


def geometry_checks():
    records = []
    for m in range(2, 13):
        x = [F(i*i+3*i-5, 7) for i in range(m)]
        center = sum(x)/m
        y = [v-center for v in x]
        variance = sum(v*v for v in y)
        p = F(m*(m-1), 2)
        f = [sum((1/(x[i]-x[j]) for j in range(m) if i != j), F(0))
             for i in range(m)]
        energy = pair_energy(x)
        assert sum(f) == 0
        assert sum(y[i]*f[i] for i in range(m)) == p
        assert sum(z*z for z in f) == 2*energy
        defect = sum((f[i]-p*y[i]/variance)**2 for i in range(m))/2
        assert energy == p*p/(2*variance)+defect and defect >= 0
        if m == 2:
            assert defect == 0

        # Real exterior poles on both sides; full velocity B=2 U'/U.
        exterior = [min(x)-F(5, 2), min(x)-F(1, 3), max(x)+F(4, 7)]
        force = [2*sum(1/(v-z) for z in exterior) for v in x]
        spread = max(abs(v-z) for v in (min(x), max(x)) for z in exterior)
        lam = 2*len(exterior)/(spread*spread)
        s_direct = -sum(y[i]*force[i] for i in range(m))
        s_pairs = -sum((x[i]-x[j])*(force[i]-force[j])
                       for i in range(m) for j in range(i+1, m))/m
        assert s_direct == s_pairs and s_direct >= lam*variance
        velocity = [2*f[i]+force[i] for i in range(m)]
        vprime = 2*sum(y[i]*velocity[i] for i in range(m))
        assert vprime == 4*p-2*s_direct
        assert vprime <= 4*p-2*lam*variance
        # A positive exterior slope reverses the required comparison.
        expanding = [2*f[i]+y[i] for i in range(m)]
        assert 2*sum(y[i]*expanding[i] for i in range(m)) > 4*p
        records.append({
            'm': m, 'E': str(energy), 'V': str(variance),
            'shape_defect': str(defect), 'exterior_lambda': str(lam),
            'exterior_compression': str(s_direct),
            'variance_derivative': str(vprime),
        })
    return records


def ceil_log2(n):
    assert isinstance(n, int) and n > 0
    return (n-1).bit_length()


def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)


def analytic_quadrature_checks():
    # Exactness on monomials through degree 2q-1, not a theta evaluation.
    cases = []
    for q in range(1, 6):
        cells, length = 7, F(3, 2)
        h = length/cells
        for degree in range(2*q+1):
            approximation = F(0)
            for j in range(cells):
                center = (F(j)+F(1, 2))*h
                for k in range(q):
                    if degree >= 2*k:
                        derivative = (F(factorial(degree), factorial(degree-2*k))
                                      *center**(degree-2*k))
                        approximation += (2*(h/2)**(2*k+1)
                                          *derivative/factorial(2*k+1))
            exact = length**(degree+1)/(degree+1)
            if degree < 2*q:
                assert approximation == exact
            else:
                assert approximation != exact
        cases.append({'q': q, 'cells': cells, 'exact_through_degree': 2*q-1,
                      'first_omitted_even_degree_detected': True})
    return cases


def source_budget_checks():
    # Conservative exact substitutes: pi>3, pi<4, pi**2<10, 2<e<3, Cbar<8.
    # Sample envelope: T=Theta=1, A=12, |a|=20,
    # rbar=1/4, S=4, R=11. W=2 satisfies the frequency gate.
    # B_* <= 2 exp(28)+1 < 2*3**28+1.
    b_upper = 2*3**28+1
    mode_offset = ceil_log2(160*b_upper)
    records = []
    for m, order in ((2, 2), (3, 2), (10, 5)):
        degree = m+order+1
        for j in (2, 10, 100, 1000, 10000, 1000000):
            # r=2^-j, |c|=2^-4; raw epsilon=2^(-target_exp).
            target_exp = 4+degree*j
            v = 1
            while True:
                l_lower = 3*16**v//4
                if v*v+12*v <= l_lower and l_lower >= target_exp+2:
                    break
                v += 1
            assert l_lower >= 2
            # Q <= 8/(4L) 2^-L <= 2^-L <= epsilon/4.
            assert 2 <= l_lower and l_lower >= target_exp+2
            ell = 2
            while 3*ell*ell//4 < target_exp+mode_offset:
                ell += 2
            exponent = 3*ell*ell//4
            assert exponent >= target_exp+mode_offset
            # C_K B <=40B*2^(-3ell²/4) <= epsilon/4.
            assert 160*b_upper <= 2**mode_offset
            k = ell-1
            s2 = sum(n**2 for n in range(1, k+1))
            s4 = sum(n**4 for n in range(1, k+1))
            s6 = sum(n**6 for n in range(1, k+1))
            dv_upper = 3**(v*v+3*v)*(
                ((2*v+23)*32+480)*s4*3**(9*v)
                +60*s2*3**(5*v)+512*s6*3**(13*v))
            # M=ceil(Dv_upper V²/epsilon) pays midpoint epsilon/4.
            # Store its power-of-two upper bound, never build that field.
            node_count_log2_upper = ceil_log2(dv_upper*v*v)+target_exp
            assert dv_upper*v*v <= 2**(node_count_log2_upper-target_exp)
            d = F(1, 16)
            kernel_exponent = (F(v)+2*d)**2+20*d+3*(F(v)+2*d)
            bv_upper = 3**ceil_fraction(kernel_exponent)*(
                32*s4*3**ceil_fraction(9*(F(v)+d))
                +12*s2*3**ceil_fraction(5*(F(v)+d)))
            q = max(1, (ceil_log2(8*v*bv_upper)+target_exp+1)//2)
            assert 8*v*bv_upper <= 2**(2*q-target_exp)
            records.append({
                'm': m, 'N': order, 'radius_negative_log2': j,
                'normalizing_c': '1/16 (parameter illustration, not acquired theta data)',
                'raw_error_negative_log2': target_exp,
                'frequency_cutoff_integer': v,
                'frequency_tail_exponent_lower': l_lower,
                'theta_mode_count': k,
                'theta_tail_exponent_lower': exponent,
                'midpoint_node_count_log2_upper': node_count_log2_upper,
                'analytic_quadrature_order_q': q,
                'analytic_quadrature_derivative_terms': 16*v*q,
                'coefficient_rounding': 'separate epsilon/4 allowance, not evaluated',
            })
    return records


def run():
    return {
        'status': 'passed', 'date': '2026-10-27',
        'prepared_for': 'Edward Baker', 'llm_assistance': 'substantial',
        'model': 'gpt-6.1-sol', 'effort': 'ultra',
        'scope': ('exact rational root identities and integer-verified conservative '
                  'source-budget schedules; no actual theta interval evaluation, '
                  'zero search, efficient runtime claim, or excluded slab'),
        'geometry_cases': geometry_checks(),
        'source_budget_cases': source_budget_checks(),
        'analytic_quadrature_exactness': analytic_quadrature_checks(),
        'negative_control': 'positive exterior slope violates the compression premise',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'scope', 'script_sha256')}))
