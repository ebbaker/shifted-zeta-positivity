#!/usr/bin/env python3
"""Exact finite checks for conditional backward-heat collision expansions.

Prepared for Edward Baker, 14 October 2026.
Model: gpt-6-astra; reasoning effort: ultra.
Python standard library only. These tests concern finite rational heat
polynomials; they do not prove the analytic general theorem or exclude a
collision for the theta source.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json

CHECKS = []
CASES = []


def check(name, actual, expected):
    assert actual == expected, f"{name}: actual={actual!r}, expected={expected!r}"
    CHECKS.append(name)


def clean(a):
    return {k: v for k, v in a.items() if v}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(a, c):
    return clean({k: c*v for k, v in a.items()})


def mul(a, b, cap):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            if ka + kb <= cap:
                out[ka+kb] = out.get(ka+kb, F(0)) + va*vb
    return clean(out)


def pow_series(a, n, cap):
    out = {0: F(1)}
    for _ in range(n):
        out = mul(out, a, cap)
    return out


def coeff(a, k):
    return a.get(k, F(0))


def heat_jet(jets, k, branch, cap):
    """Compose a differentiated finite heat polynomial with y=branch(s).

    Directly sum J[k+2p+q] s^p y^q/(p! q!). No collision-asymptotic
    coefficients, branch formulas, or quotient formulas enter this routine.
    """
    degree = len(jets)-1
    powers = [pow_series(branch, q, cap) for q in range(max(0, degree-k)+1)]
    out = {}
    for p in range((degree-k)//2+1):
        for q in range(degree-k-2*p+1):
            jet = jets[k+2*p+q]
            if not jet:
                continue
            for exponent, value in powers[q].items():
                if p+exponent <= cap:
                    n = p+exponent
                    out[n] = out.get(n, F(0)) + jet*value/F(factorial(p)*factorial(q))
    return clean(out)


def solve_branch(jets, j, r, label, cap):
    """Eliminate two coefficients by exact two-point linear interpolation."""
    stationary = lambda d1, d2: heat_jet(jets, j+1, {1: d1, 2: d2}, cap)
    zero = coeff(stationary(F(0), F(0)), r)
    slope = coeff(stationary(F(1), F(0)), r)-zero
    assert slope, f"{label}: first elimination is singular"
    d1 = -zero/slope
    check(label+'.d1_coefficient_linearity', coeff(stationary(F(2), F(0)), r), zero+2*slope)
    zero2 = coeff(stationary(d1, F(0)), r+1)
    slope2 = coeff(stationary(d1, F(1)), r+1)-zero2
    assert slope2, f"{label}: second elimination is singular"
    d2 = -zero2/slope2
    check(label+'.d2_coefficient_linearity', coeff(stationary(d1, F(2)), r+1), zero2+2*slope2)
    residual = stationary(d1, d2)
    check(label+'.stationarity_through_order_r_plus_1',
          [coeff(residual, n) for n in range(r+2)], [F(0)]*(r+2))
    return {1: d1, 2: d2}


def first_two_laurent(numerator, denominator):
    """Divide leading terms of independently assembled numerator/denominator."""
    n, d = min(numerator), min(denominator)
    n0, n1 = coeff(numerator, n), coeff(numerator, n+1)
    d0, d1 = coeff(denominator, d), coeff(denominator, d+1)
    return n-d, n0/d0, (n1*d0-n0*d1)/(d0*d0)


def rational_text(x):
    return str(x)


def generic_cases():
    # Both signs of A; B=0 and B!=0; positive, zero, negative C; independent
    # nonzero higher jets that affect the actual stationary branch at d2.
    tails = [
        [F(2), F(3), F(5), F(7), F(11), F(13), F(17), F(19)],
        [F(-3,2), F(4,5), F(-7,3), F(9,2), F(1,7), F(-5), F(2), F(0)],
        [F(5,7), F(0), F(-11,4), F(2,3), F(-8,9), F(3), F(0), F(1)],
        [F(-2,3), F(-13,7), F(0), F(-1,2), F(6,5), F(0), F(-7), F(2)],
        [F(1,11), F(2,13), F(3,17), F(-4,19), F(5,23), F(-6,29), F(7,31), F(-8,37)],
    ]
    for m in range(2, 14):
        j, r = m % 2, m//2
        cap = 2*r+5
        for k, tail in enumerate(tails):
            label = f'm{m:02d}.jetset{k+1}'
            jets = [F(0)]*m + tail
            A, B, C = jets[m:m+3]
            branch = solve_branch(jets, j, r, label, cap)
            h = [heat_jet(jets, d, branch, cap) for d in range(4)]
            energy = add(mul(h[0], h[0], cap), mul(h[1], h[1], cap))
            laguerre = add(mul(h[j+1], h[j+1], cap), scale(mul(h[j], h[j+2], cap), F(-1)))
            expected_alpha = C/((r+1)*A) - B*B/(2*r*A*A)
            check(label+'.d1_formula', branch[1], -B/(r*A))
            check(label+'.h_j_vanishing_order', min(h[j]), r)
            check(label+'.h_j_leading', coeff(h[j], r), A/F(factorial(r)))
            check(label+'.alpha', coeff(h[j], r+1)/coeff(h[j], r), expected_alpha)
            check(label+'.energy_vanishing_order', min(energy), 2*r)
            check(label+'.energy_leading', coeff(energy, 2*r), (A/F(factorial(r)))**2)
            check(label+'.laguerre_vanishing_order', min(laguerre), 2*r-1)
            check(label+'.laguerre_leading', coeff(laguerre, 2*r-1), -r*(A/F(factorial(r)))**2)
            exponent, leading, constant = first_two_laurent(scale(laguerre, -1), energy)
            check(label+'.minus_L_over_E_pole_order', exponent, -1)
            check(label+'.minus_L_over_E_residue', leading, F(r))
            check(label+'.minus_L_over_E_constant', constant, expected_alpha)
            if j == 1:
                check(label+'.H_lower_terms_zero', [coeff(h[0], n) for n in range(r+1)], [F(0)]*(r+1))
                check(label+'.H_over_Hx_linear', coeff(h[0], r+1)/coeff(h[1], r), -B/(r*(r+1)*A))
            CASES.append({'multiplicity': m, 'stationary_index': j, 'r': r,
                          'jet_set': k+1, 'A': str(A), 'B': str(B), 'C': str(C),
                          'd1': str(branch[1]), 'd2': str(branch[2]), 'alpha': str(expected_alpha)})


def exact_controls():
    cap = 12
    # These complete polynomial outputs are specified independently.
    double = [F(0), F(0), F(2)]
    cubic = [F(0), F(0), F(0), F(6)]
    # Evaluate at nonstationary y=1+2s to check the full heat polynomial.
    branch = {0: F(1), 1: F(2)}
    check('double.full_H', heat_jet(double, 0, branch, cap), {0:F(1), 1:F(6), 2:F(4)})
    check('double.full_Hx', heat_jet(double, 1, branch, cap), {0:F(2), 1:F(4)})
    check('double.stationary_H', heat_jet(double, 0, {}, cap), {1:F(2)})
    check('double.stationary_Hx', heat_jet(double, 1, {}, cap), {})
    check('double.stationary_Hxx', heat_jet(double, 2, {}, cap), {0:F(2)})
    check('cubic.full_H', heat_jet(cubic, 0, branch, cap), {0:F(1), 1:F(12), 2:F(24), 3:F(8)})
    check('cubic.full_Hx', heat_jet(cubic, 1, branch, cap), {0:F(3), 1:F(18), 2:F(12)})
    check('cubic.stationary_H', heat_jet(cubic, 0, {}, cap), {})
    check('cubic.stationary_Hx', heat_jet(cubic, 1, {}, cap), {1:F(6)})
    check('cubic.stationary_Hxx', heat_jet(cubic, 2, {}, cap), {})
    h = [heat_jet(cubic, k, {}, cap) for k in range(4)]
    check('cubic.L0_positive_at_derivative_stationarity', add(mul(h[1], h[1], cap),scale(mul(h[0],h[2],cap),-1)), {2:F(36)})
    check('cubic.L1_negative_at_derivative_stationarity', add(mul(h[2], h[2], cap),scale(mul(h[1],h[3],cap),-1)), {1:F(-36)})


def substitute_time(series, replacement, cap):
    out = {}
    for power, value in series.items():
        out = add(out, scale(pow_series(replacement, power, cap), value))
    return out


def delay_checks():
    cap, drift, mu = 20, F(3,11), F(5,7)
    delay_examples = []
    for j in [0,1]:
        for r in [1,2,3]:
            # A=r! makes the selected component exactly s^r at y=0.
            jets = [F(0)]*(j+2*r) + [F(factorial(r))]
            h = [heat_jet(jets, k, {}, cap) for k in range(4)]
            energy = add(mul(h[0],h[0],cap),mul(h[1],h[1],cap))
            laguerre = add(mul(h[j+1],h[j+1],cap),scale(mul(h[j],h[j+2],cap),-1))
            current = add(add(scale(h[j+2],-1),scale(h[j+1],-2*drift)),scale(h[j],-mu))
            # Constant and moving delays, including a shrinking delay.
            delays = [({},'zero'),({0:F(1,7)},'fixed_1_7'),({0:F(2,3)},'fixed_2_3'),({1:F(2,5)},'proportional_s'),({2:F(3,4)},'quadratic_s')]
            for delay, delay_label in delays:
                label = f'delay.j{j}.r{r}.{delay_label}'
                earlier_s = add({1:F(1)},delay)
                earlier = substitute_time(current, earlier_s, cap)
                retained = mul(h[j], earlier, cap)
                absorption = mul(h[j], add(current,scale(earlier,F(-1,2))),cap)
                combined = add(scale(retained,F(1,2)),absorption)
                check(label+'.stationarity',h[j+1],{})
                check(label+'.split_identity',combined,mul(h[j],current,cap))
                check(label+'.Laguerre_identity',add(scale(mul(h[j],h[j],cap),mu),combined),laguerre)
                check(label+'.combined_over_E', {n-2*r:v for n,v in combined.items()}, {-1:F(-r),0:-mu})
                if r in [2,3] and delay_label=='fixed_2_3':
                    retained_ratio={n-2*r:v for n,v in retained.items()}
                    absorption_ratio={n-2*r:v for n,v in absorption.items()}
                    d=F(2,3)
                    strongest=-(r*d**(r-1)+mu*d**r)
                    check(label+'.retained_strongest_pole_order',min(retained_ratio),-r)
                    check(label+'.retained_strongest_pole_coefficient',coeff(retained_ratio,-r),strongest)
                    check(label+'.absorption_strongest_pole_coefficient',coeff(absorption_ratio,-r),-strongest/2)
                    check(label+'.higher_poles_cancel',{n:v for n,v in add(scale(retained_ratio,F(1,2)),absorption_ratio).items() if n < -1},{})
                    delay_examples.append({'j':j,'r':r,'delay':str(d),'mu':str(mu),
                        'P_over_E':{str(n):str(v) for n,v in sorted(retained_ratio.items())},
                        'Q_over_E':{str(n):str(v) for n,v in sorted(absorption_ratio.items())},
                        'P_over_2E_plus_Q_over_E':{'-1':str(-r),'0':str(-mu)}})
    return delay_examples


def exponent_checks():
    # E~s^(2r), -L~s^(2r-1), so (-L)/E^p has this exponent.
    for r in range(1,7):
        critical=F(2*r-1,2*r)
        check(f'exponent.r{r}.critical',F(2*r-1)-2*r*critical,F(0))
        check(f'exponent.r{r}.energy_loss',F(2*r-1)-2*r*F(1),F(-1))
        check(f'exponent.r{r}.subcritical',F(2*r-1)-2*r*(critical-F(1,10))>0,True)
        check(f'exponent.r{r}.supercritical',F(2*r-1)-2*r*(critical+F(1,10))<0,True)


def main():
    generic_cases()
    exact_controls()
    examples=delay_checks()
    exponent_checks()
    path=Path(__file__).resolve()
    receipt={
        'title':'Exact rational checks of conditional backward-heat collision behavior',
        'date':'2026-10-14', 'prepared_for':'Edward Baker',
        'model':'gpt-6-astra','reasoning_effort':'ultra',
        'status':'PASS', 'arithmetic':'fractions.Fraction; Python standard library only',
        'script':path.name,'script_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'named_assertions':len(CHECKS),'generic_jet_cases':len(CASES),
        'multiplicities':list(range(2,14)),'jet_sets_per_multiplicity':5,
        'scope':[
            'Independent coefficient elimination for the two-jet y=d1*s+d2*s^2 of the stationary branch.',
            'Stationarity through s^(r+1); selected-component, energy, Laguerre, and Laurent-quotient coefficients.',
            'Odd multiplicity H/Hx leading linear coefficient.',
            'Exact double and cubic heat-polynomial controls.',
            'Thirty exact retained/absorption split checks for constant and moving delays at exact stationarity.',
            'Fixed positive-delay examples at r=2 and r=3 with stronger canceling poles.',
            'Energy-power loss exponent arithmetic for r=1..6.'
        ],
        'limitations':[
            'Finite polynomial checks do not prove analytic stationary-branch existence or the general analytic theorem.',
            'The branch used in generic cases is its two-jet; its residual is verified only through the orders needed here.',
            'No assertion is made that the theta source has a collision, nor do these checks exclude one.',
            'Rational drift and mass constants check the algebraic delay identity; no numerical approximation to pi is used.'
        ],
        'cases':CASES,'fixed_delay_examples':examples,'checks':CHECKS
    }
    receipt_path=path.with_name('COLLISION_BEHAVIOR_CHECKS_20261014.json')
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','named_assertions','generic_jet_cases','script_sha256']},indent=2))
    print('Receipt:',receipt_path)


if __name__=='__main__':
    main()
