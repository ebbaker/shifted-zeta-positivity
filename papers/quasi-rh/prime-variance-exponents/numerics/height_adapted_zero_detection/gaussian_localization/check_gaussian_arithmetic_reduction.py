#!/usr/bin/env python3
"""Exact arithmetic checks behind the finite Gaussian Mobius reduction.

Prepared for Edward Baker, 2026-10-04, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact variant and reasoning
effort are not exposed and are not inferred. Standard library only.

Formal prime logarithms and synthetic complex rational weights check finite
identities and cutoff conventions. Rational elementary-function enclosures
check budget arithmetic. No actual Gaussian prime/Mobius sum is evaluated
at the enormous proposed scales, and no cancellation inequality is proved.
"""

from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import math

ROOT = Path(__file__).resolve().parent
DEPENDENCY_NAME = "check_explicit_gaussian_constants.py"
DEPENDENCY_SHA256 = "4b5277a670cc75b49aae6f3ddd18d8d0d3a0749cc73112bb77516db021dfedf9"
dependency_path = ROOT/DEPENDENCY_NAME
if not dependency_path.exists():
    raise SystemExit(f"Missing {DEPENDENCY_NAME}; use the same investigation numerics folder.")
if sha256(dependency_path.read_bytes()).hexdigest() != DEPENDENCY_SHA256:
    raise SystemExit("Elementary-enclosure dependency changed; audit before updating its expected hash.")
spec = importlib.util.spec_from_file_location("gaussian_elementary_enclosures", dependency_path)
elem = importlib.util.module_from_spec(spec)
spec.loader.exec_module(elem)


def factorization(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p,0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n,0)+1
    return out


def mobius(n):
    exponents = factorization(n).values()
    return 0 if any(e > 1 for e in exponents) else (-1)**len(exponents)


def divisors(n):
    out = []
    for d in range(1,math.isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)


def add_formal_log(target, n, coefficient):
    """log(n)=sum_p v_p(n)log(p), with exact formal coefficients."""
    for p, exponent in factorization(n).items():
        target[p] = target.get(p,F(0))+coefficient*exponent
        if target[p] == 0:
            del target[p]


def lambda_formal(n):
    factors = factorization(n)
    return {next(iter(factors)):F(1)} if len(factors)==1 else {}


def synthetic_weight(n):
    return (F(n % 7 - 3,n+1), F((-1)**n,n+2))


def finite_identity_checks():
    # The identity includes nonsquarefree numbers and every prime power.
    coefficient_checks = 0
    for n in range(1,4097):
        lhs = {}
        for d in divisors(n):
            add_formal_log(lhs,d,-mobius(d))
        assert lhs == lambda_formal(n),(n,lhs)
        coefficient_checks += 1
    cap_cases = 0
    for D in (F(1),F(3,2),F(2),F(15),F(31,2),F(18)):
        for B in (F(20),F(127,2),F(127),F(255,2)):
            if B <= D:
                continue
            for component in (0,1):
                prime, low, high, grouped_high = {},{},{},{}
                for n in range(1,B.__floor__()+1):
                    weight = synthetic_weight(n)[component]
                    for p, coefficient in lambda_formal(n).items():
                        prime[p] = prime.get(p,F(0))+coefficient*weight
                    for d in divisors(n):
                        if d <= D:
                            add_formal_log(low,d,-mobius(d)*weight)
                        else:
                            add_formal_log(grouped_high,d,-mobius(d)*weight)
                for r in range(1,(B/D).__floor__()+1):
                    for d in range(D.__floor__()+1,(B/r).__floor__()+1):
                        assert d > D and d*r <= B
                        assert r < B/D  # the strict lower divisor cap survives
                        add_formal_log(high,d,-mobius(d)*synthetic_weight(d*r)[component])
                for dictionary in (prime,low,high,grouped_high):
                    for p in list(dictionary):
                        if dictionary[p] == 0:
                            del dictionary[p]
                assert high == grouped_high,(D,B,component)
                combined = dict(low)
                for p, coefficient in high.items():
                    combined[p] = combined.get(p,F(0))+coefficient
                    if combined[p] == 0:
                        del combined[p]
                assert combined == prime,(D,B,component)
                cap_cases += 1
    return {"formal_log_coefficient_checks":coefficient_checks,
            "complex_component_cutoff_checks":cap_cases,
            "weights":"synthetic complex rational weights, not actual Gaussians",
            "cutoffs":"real D, strict d>D, weak dr<=B, full terminal cofactor caps"}


def multiply(a,b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def integrate_upper_tail_polynomial(k):
    alpha = F(11,4)
    poly = multiply(multiply([26*k,F(1)],[1+26*k,F(1)]),
                    [F(15,4),F(1,2)/k])
    return sum(coefficient*math.factorial(j)/alpha**(j+1)
               for j,coefficient in enumerate(poly))


def budget_checks():
    # The exact tilted Gaussian fourth moment of q^2-q-1/(2k).
    # For k>=2 its square is <=(T^2+1)^2 coefficient by coefficient.
    worst_r = F(1,4)  # r=1/(2k)
    assert 1+4*worst_r <= 2
    assert worst_r+2*worst_r**2 < 1
    gaussian_moments = []
    for k in (F(2),F(8),F(44),F(168)):
        r = 1/(2*k)
        for T in (F(0),F(100),F(1001)):
            real_poly = [-T*T-r,F(1),F(1)]
            imaginary_poly = [-T,-2*T]
            squared = multiply(real_poly,real_poly)
            imaginary_squared = multiply(imaginary_poly,imaginary_poly)
            for j,coefficient in enumerate(imaginary_squared):
                squared[j] += coefficient
            exact_moment = squared[0]+squared[2]*r+squared[4]*3*r*r
            expected = T**4+(1+2/k)*T*T+1/(2*k)+1/(2*k*k)
            assert exact_moment == expected
            assert expected <= (T*T+1)**2
            gaussian_moments.append({"k":str(k),"T":str(T),"fourth_moment":str(exact_moment)})
    coefficients = [F(10140,11),F(12818,121),F(6756,1331),F(1472,14641)]
    for k in (F(8),F(44),F(168),F(328)):
        expression = coefficients[0]*k*k+coefficients[1]*k+coefficients[2]+coefficients[3]/k
        assert integrate_upper_tail_polynomial(k) == expression
    tail_at_8 = integrate_upper_tail_polynomial(F(8))/64
    assert tail_at_8 == F(219062021,234256) and tail_at_8 < 1000
    # Frequency tail prefactor is <=80k using pi>3, k>=8.
    assert F(26,9)*(26+F(1,8)) < 80
    # Analytic monotonicity: the least sample is worst, then N=10 is worst.
    assert F(1,44)-F(31,16) < 0
    assert F(1,11)+F(31,10)-F(23,4) < 0
    assert F(3,88)-F(5,2) < 0
    assert F(3,22)+F(31,10)-10 < 0
    # Budget ratios to eta at the all-N proof's base, with outward logs.
    N,k = 10,44
    log_eta_recip = elem.scale(elem.LOG8E,N)
    low_ratio = elem.add(elem.log_point(F(5*k,4)),
                         elem.sub(elem.add(elem.point(2*N),log_eta_recip),
                                  elem.point(F(31,16)*k)))
    high_ratio = elem.sub(elem.add(elem.add(elem.log_point(250),
                                          elem.scale(elem.log_point(k),F(3,2))),
                                 log_eta_recip), elem.point(F(5,2)*k))
    freq_ratio = elem.sub(elem.add(elem.log_point(80*k),log_eta_recip),
                         elem.point(F(5,2)*k))
    cutoff = -4*elem.LOG2[1]
    assert low_ratio[1] < cutoff
    assert high_ratio[1] < cutoff
    assert freq_ratio[1] < cutoff
    assert elem.scale(elem.log_point(44),F(3,2))[1] < 44
    # Known continuum term is independently affordable, while retained.
    assert 1+15*k+225*k*k <= 241*k*k
    continuum_ratio = elem.sub(elem.add(elem.log_point(241*k*k),log_eta_recip),
                               elem.point(k*(100**2-F(81,16))))
    assert continuum_ratio[1] < cutoff
    # Error exponents from the chosen logarithmic scales.
    assert -F(7,4)*20+F(7,4)**2 == -F(511,16)
    assert 30-F(511,16) == -F(31,16)
    assert F(1,4)*26-F(6)**2/4 == -F(5,2)
    return {"tilted_gaussian_fourth_moment_examples":gaussian_moments,
            "upper_product_tail_polynomial_coefficients":list(map(str,coefficients)),
            "tail_polynomial_divided_by_k_squared_at_8":str(tail_at_8),
            "log_error_over_eta_base_N10_k44":{
                "low_divisors":elem.display(low_ratio),
                "upper_products":elem.display(high_ratio),
                "optional_relative_frequency_tail":elem.display(freq_ratio),
                "retained_continuum_at_T100":elem.display(continuum_ratio)}}


def main():
    identities = finite_identity_checks()
    budgets = budget_checks()
    record = {"date":"2026-10-04", "prepared_for":"Edward Baker",
              "model":"GPT-6 (Codex), inherited configuration; exact variant and reasoning effort not exposed",
              "source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
              "dependency_sha256":{DEPENDENCY_NAME:DEPENDENCY_SHA256},
              "claim_scope":"exact finite algebra and analytic-budget arithmetic; no actual large prime/Mobius sum or cancellation certificate",
              "parameters":{"b":"3/4","mu":"20k","D":"exp(15k)","B":"exp(26k)",
                            "cofactor_upper":"exp(11k)","optional_relative_frequency_band":[-3,3],
                            "N_min":10,"k_samples":"4(N+1),4(N+2),...,8N"},
              "identities":identities,"budgets":budgets,
              "example_T_3e12":{"N":41,"k_min":168,"k_max":328,
                                 "log_D_range":[2520,4920],"log_B_range":[4368,8528],
                                 "log_cofactor_upper_range":[1848,3608]},
              "status":"checks passed; remaining finite signed cancellation bound is unproved"}
    target = ROOT/'gaussian_arithmetic_reduction_record_20261004.json'
    target.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({"record":str(target),"source_sha256":record['source_sha256'],
                      "identities":identities,"budgets":budgets['log_error_over_eta_base_N10_k44']},indent=2))


if __name__ == '__main__':
    main()
