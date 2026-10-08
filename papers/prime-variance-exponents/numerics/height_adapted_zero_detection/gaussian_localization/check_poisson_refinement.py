#!/usr/bin/env python3
"""Exact rational checks for the Gaussian Poisson-cutoff refinement.

Prepared for Edward Baker, 2026-10-04, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Standard library only. Every sign decision uses integers or Fraction.
The checks cover finite formal-logarithm identities, constant certificates,
and algebra supporting the analytic all-sample budget proofs. They do not
formally certify contour rotation, Poisson summation, or any actual giant
Gaussian Mobius sum, and they do not prove a signed cancellation estimate.
The old checker hashes identify reference provenance only; no old source
is imported or needed to replay this standalone checker.
"""

from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import math


REFERENCE_SOURCE_SHA256 = {
    "check_explicit_gaussian_constants.py":
        "4b5277a670cc75b49aae6f3ddd18d8d0d3a0749cc73112bb77516db021dfedf9",
    "check_gaussian_arithmetic_reduction.py":
        "d2a3f31ac3d081890317c86db68d6762094a06413acacd97286820b70fd716ce",
}


def factorization(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def mobius(n):
    exponents = factorization(n).values()
    return 0 if any(e > 1 for e in exponents) else (-1)**len(exponents)


def divisors(n):
    out = []
    for d in range(1, math.isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)


def add_formal_log(target, n, coefficient):
    """Expand log(n) in independent formal prime logarithms."""
    for p, exponent in factorization(n).items():
        target[p] = target.get(p, F(0))+coefficient*exponent
        if target[p] == 0:
            del target[p]


def lambda_formal(n):
    factors = factorization(n)
    return {next(iter(factors)): F(1)} if len(factors) == 1 else {}


def synthetic_weight(n):
    return (F(n % 7-3, n+1), F((-1)**n, n+2))


def clean(target):
    for p in list(target):
        if target[p] == 0:
            del target[p]


def finite_identity_checks():
    coefficient_checks = 0
    for n in range(1, 4097):
        lhs = {}
        for d in divisors(n):
            add_formal_log(lhs, d, -mobius(d))
        assert lhs == lambda_formal(n), (n, lhs)
        coefficient_checks += 1
    cap_cases = 0
    pair_checks = 0
    for D in (F(1), F(3, 2), F(2), F(15), F(77, 5), F(31, 2), F(18), F(100)):
        for B in (F(20), F(127, 2), F(127), F(255, 2), F(511, 2)):
            if B <= D:
                continue
            for component in (0, 1):
                prime, low, high, grouped_high = {}, {}, {}, {}
                for n in range(1, B.__floor__()+1):
                    weight = synthetic_weight(n)[component]
                    for p, coefficient in lambda_formal(n).items():
                        prime[p] = prime.get(p, F(0))+coefficient*weight
                    for d in divisors(n):
                        if d <= D:
                            add_formal_log(low, d, -mobius(d)*weight)
                        else:
                            add_formal_log(grouped_high, d, -mobius(d)*weight)
                for r in range(1, (B/D).__floor__()+1):
                    for d in range(D.__floor__()+1, (B/r).__floor__()+1):
                        assert d > D and d*r <= B
                        assert r < B/D
                        add_formal_log(high, d, -mobius(d)*synthetic_weight(d*r)[component])
                        pair_checks += 1
                for target in (prime, low, high, grouped_high):
                    clean(target)
                assert high == grouped_high, (D, B, component)
                combined = dict(low)
                for p, coefficient in high.items():
                    combined[p] = combined.get(p, F(0))+coefficient
                clean(combined)
                assert combined == prime, (D, B, component)
                cap_cases += 1
    return {
        "formal_log_coefficient_checks": coefficient_checks,
        "complex_component_cutoff_checks": cap_cases,
        "retained_pair_cutoff_checks": pair_checks,
        "weights": "synthetic complex rational weights, not actual Gaussians",
        "cutoffs": "real D, strict d>D, weak dr<=B, strict active r<B/D, full terminal caps",
    }


def atan_lower(x, terms=4):
    """Even truncation of the alternating series is a rational lower bound."""
    assert F(0) < x < 1 and terms % 2 == 0
    return sum(((-1)**j*x**(2*j+1)/(2*j+1)
                for j in range(terms)), F(0))


def log2_enclosure(terms=24):
    """Use log(2)=2*atanh(1/3), with an exact positive tail bound."""
    x = F(1, 3)
    lower = sum((2*x**(2*j+1)/(2*j+1)
                 for j in range(terms)), F(0))
    remainder = 2*x**(2*terms+1)/((2*terms+1)*(1-x*x))
    return lower, lower+remainder


def elementary_certificates():
    # atan(1/2)+atan(1/3)=pi/4: both angles are in (0,pi/2),
    # and the tangent addition formula yields one.
    assert (F(1, 2)+F(1, 3))/(1-F(1, 2)*F(1, 3)) == 1
    pi_lower = 4*(atan_lower(F(1, 2))+atan_lower(F(1, 3)))
    assert pi_lower > F(25, 8)
    sin_factor_lower = 1-F(1, 6*100**2)
    assert 2*F(25, 8)*sin_factor_lower > 6
    # theta<=1/100; sin(theta)>=theta*(1-theta^2/6).
    # Hence a=2*pi*sin(theta)>6/T for theta=1/T, T>=100.

    e_lower = sum((F(1, math.factorial(j)) for j in range(4)), F(0))
    partial = sum((F(1, math.factorial(j)) for j in range(6)), F(0))
    e_upper = partial+F(1, math.factorial(6))/(1-F(1, 7))
    assert e_lower > F(5, 2) and e_upper < F(11, 4)
    epsilon_max = F(1, 4*44*100**2)
    assert epsilon_max == F(1, 1760000)
    rotation_E_upper = F(11, 4)/(1-epsilon_max)
    assert rotation_E_upper < 3
    # exp(epsilon)<=1/(1-epsilon) for 0<=epsilon<1.

    lower_log2, upper_log2 = log2_enclosure()
    assert 3*upper_log2+1 < F(31, 10)
    # p=5/2: e^u-1 >= u^2/2+u^3/6 >= u^(5/2)/2.
    # With v=sqrt(u), the last inequality has this exact certificate.
    assert F(1, 6)*F(3, 2)**2+F(1, 8) == F(1, 2)
    assert -2*F(1, 6)*F(3, 2) == -F(1, 2)
    assert F(1, 8) > 0
    # v^2/6-v/2+1/2 = (v-3/2)^2/6+1/8.

    geometric_checks = 0
    for q in (F(1, 5), F(1, 2), F(3, 4), F(99, 100)):
        for modes in (1, 2, 7, 40):
            finite_sum = sum((q**h for h in range(1, modes+1)), F(0))
            assert finite_sum+q**(modes+1)/(1-q) == q/(1-q)
            geometric_checks += 1
    # q=exp(-u): sum_{h>=1}q^h=q/(1-q)=1/(exp(u)-1).
    # Both signs are included in 2E; no separate zeta(p) factor occurs.

    sum_rounding_factor = F(101, 100)**3
    assert sum_rounding_factor < F(11, 10)
    # For increasing x^(p-1), sum_{d<=D}d^(p-1)
    # <= integral_1^(floor(D)+1)x^(p-1)dx <= (D+1)^p/p.
    # Bound each log(d) by log(D), then use D>=100 and p<3.

    assert F(12, 5)**2 < 6
    p, alpha = F(5, 2), F(77, 5)
    prefactor = 4*3*F(11, 10)/p*alpha/(6**2*F(12, 5))
    assert prefactor == F(847, 900) and prefactor < 1
    gaussian_linear = F(1, 4)-p
    exponent = p*alpha+gaussian_linear**2+20*gaussian_linear
    assert exponent == -F(23, 16)
    assert 26-alpha == F(53, 5)
    assert p*15+gaussian_linear**2+20*gaussian_linear == -F(39, 16)
    assert alpha > 15
    assert alpha*44 > 7 and 2**7 > 100  # D=exp(alpha*k)>100.
    return {
        "pi_lower_alternating_rational": str(pi_lower),
        "sin_theta_over_theta_lower_at_T100": str(sin_factor_lower),
        "e_lower_taylor": str(e_lower),
        "e_upper_taylor_with_tail": str(e_upper),
        "rotation_epsilon_max": str(epsilon_max),
        "rotation_E_upper_using_11_over_4": str(rotation_E_upper),
        "log2_rational_enclosure": [str(lower_log2), str(upper_log2)],
        "geometric_mode_moment_certificate": "v^2/6-v/2+1/2=(v-3/2)^2/6+1/8, v=sqrt(u)",
        "rational_geometric_mode_identity_checks": geometric_checks,
        "geometric_mode_sum": "sum_(h>=1)exp(-h*u)=1/(exp(u)-1); both signs already included in 2E; no zeta factor",
        "divisor_sum_rounding_upper": str(sum_rounding_factor),
        "poisson_error_prefactor_after_alpha": str(prefactor),
        "poisson_error_exponent_per_k": str(exponent),
        "new_cofactor_exponent_per_k": str(26-alpha),
    }


def multiply(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def upper_tail_polynomial(k):
    alpha = F(11, 4)
    poly = multiply(multiply([26*k, F(1)], [1+26*k, F(1)]),
                    [F(15, 4), F(1, 2)/k])
    return sum((coefficient*math.factorial(j)/alpha**(j+1)
                for j, coefficient in enumerate(poly)), F(0))


def all_sample_budget_checks():
    N, k, p, alpha = F(10), F(44), F(5, 2), F(77, 5)
    # k*T^p*exp(-23k/16) decreases with k>=44.
    assert 1/k-F(23, 16) < 0
    # Substitute k=4(N+1), T<exp(N), log(8e)<31/10.
    N_exponent = p+F(31, 10)-F(23, 4)
    assert N_exponent == -F(3, 20)
    assert 1/(N+1)-F(3, 20) < 0
    base_exponent = F(3, 20)*N+F(23, 4)
    assert base_exponent == F(29, 4)
    exp_quarter_lower = 1+F(1, 4)+F(1, 4)**2/2
    assert exp_quarter_lower > F(5, 4)
    base_exp_lower = F(5, 2)**7*F(5, 4)
    assert base_exp_lower == F(390625, 512)
    assert base_exp_lower > 16*4*(N+1)
    deletion_ratio_upper = 4*(N+1)/base_exp_lower
    assert deletion_ratio_upper == F(22528, 390625)
    assert deletion_ratio_upper < F(1, 16)

    # Recheck old high-product bound: independent of divisor cutoff D.
    coefficients = [F(10140, 11), F(12818, 121),
                    F(6756, 1331), F(1472, 14641)]
    polynomial_checks = 0
    for sample in (F(8), F(44), F(168), F(328)):
        expected = (coefficients[0]*sample**2+coefficients[1]*sample
                    +coefficients[2]+coefficients[3]/sample)
        assert upper_tail_polynomial(sample) == expected
        polynomial_checks += 1
    tail_base = upper_tail_polynomial(F(8))/64
    assert tail_base == F(219062021, 234256) and tail_base < 1000
    # Relative-frequency tail remains <=80*k*exp(-5*k/2).
    assert F(26, 9)*(26+F(1, 8)) < 80

    # k^q<=exp(k) (q=1,3/2,2), for k>=44:
    # 44<2^6 and log(2)<1 show q*log(44)<12<44;
    # the log ratio decreases since q/k-1<0.
    assert 44 < 2**6 and 12 < 44
    for q in (F(1), F(3, 2), F(2)):
        assert q/k-1 < 0
    old_N_exponent = F(31, 10)-6
    assert old_N_exponent == -F(29, 10)
    old_base_exponent = F(29, 10)*N+6
    assert old_base_exponent == 35
    high_ratio_upper = F(250, 2**35)
    frequency_ratio_upper = F(80, 2**35)
    assert high_ratio_upper < F(1, 16)
    assert frequency_ratio_upper < F(1, 16)

    # Continuum: |L_D|<=alpha*k*(1+alpha*k), and
    # 1+alpha*k+alpha^2*k^2 <=254*k^2 for k>=1.
    assert 1+alpha+alpha*alpha < 254
    assert 1/k**2+alpha/k+alpha*alpha < 238
    assert 100**2-F(97, 16) > 10
    continuum_N_exponent = F(31, 10)-40
    assert continuum_N_exponent == -F(369, 10)
    continuum_base_exponent = F(369, 10)*N+40
    assert continuum_base_exponent == 409
    continuum_ratio_upper = F(254, 2**409)
    assert continuum_ratio_upper < F(1, 16)

    # The refined target's same detector allowance:
    # direct: 1/4 + low/16 + high/16 + fixed_line/16 <1/2;
    # optional band: add freq/16, with all four errors strict.
    assert F(1, 4)+3*F(1, 16) == F(7, 16) < F(1, 2)
    assert F(1, 4)+4*F(1, 16) == F(1, 2)
    return {
        "deletion_error_upper": "k*T^(5/2)*exp(-23*k/16)",
        "deletion_error_over_eta_all_N_upper": "4*(N+1)*exp(-3*N/20-23/4)",
        "deletion_base_N10_rational_ratio_upper": str(deletion_ratio_upper),
        "deletion_base_exp_29_over_4_lower": str(base_exp_lower),
        "deletion_log_derivative_upper_at_N10": str(1/(N+1)-F(3, 20)),
        "product_tail_polynomial_checks": polynomial_checks,
        "product_tail_polynomial_coefficients": list(map(str, coefficients)),
        "product_tail_polynomial_over_k_squared_at_8": str(tail_base),
        "product_error_over_eta_base_N10_upper": str(high_ratio_upper),
        "relative_frequency_error_over_eta_base_N10_upper": str(frequency_ratio_upper),
        "continuum_coefficient_upper": "254*k^2 (238*k^2 is also valid for k>=44)",
        "continuum_error_over_eta_base_N10_upper": str(continuum_ratio_upper),
        "budget_proof": "analytic monotonicity plus exact rational base certificates; no finite floating sweep",
    }


def polynomial_value(coefficients, x):
    value = F(0)
    for coefficient in reversed(coefficients):
        value = value*x+coefficient
    return value


def partial_summation_checks():
    """Check the lower-open, upper-closed endpoint identity exactly."""
    cases = 0
    for D in (F(1), F(3, 2), F(2), F(15), F(77, 5), F(31, 2), F(18)):
        for L in (F(17), F(35, 2), F(31), F(101, 3), F(42)):
            if L <= D:
                continue
            points = [D]+[F(n) for n in range(D.__floor__()+1, L.__ceil__())]+[L]
            for component in (0, 1):
                coefficients = {
                    n: mobius(n)*synthetic_weight(n)[component]
                    for n in range(D.__floor__()+1, L.__floor__()+1)
                }
                terminal_prefix = sum(coefficients.values(), F(0))
                for polynomial in ([F(3, 2)], [F(-1), F(2, 3)],
                                   [F(1, 5), F(-2, 7), F(3, 11)],
                                   [F(0), F(5, 13), F(-1, 3), F(2, 9)]):
                    lhs = sum((coefficient*polynomial_value(polynomial, F(n))
                               for n, coefficient in coefficients.items()), F(0))
                    integral = F(0)
                    for left, right in zip(points, points[1:]):
                        prefix = sum((coefficient for n, coefficient in coefficients.items()
                                      if n <= left), F(0))
                        integral += prefix*(polynomial_value(polynomial, right)
                                            -polynomial_value(polynomial, left))
                    rhs = terminal_prefix*polynomial_value(polynomial, L)-integral
                    assert lhs == rhs, (D, L, component, polynomial)
                    cases += 1
    return {
        "polynomial_partial_summation_cases": cases,
        "coefficients": "Mobius times synthetic complex rational components",
        "amplitudes": "exact rational polynomials of degrees zero through three",
        "endpoint_convention": "D<d<=L, terminal prefix retained, all real-cap intervals paid",
    }


def conditional_signed_constant_checks():
    """Check constants in two implications conditional on unproved inputs."""
    N, k = F(10), F(44)
    # Baseline dyadic blocks of size Y^(3/5) give prefix constant A=3.
    delta, alpha, A = F(2, 5), F(77, 5), F(3)
    assert F(3, 2)**5 < 2**3
    assert A/delta == F(15, 2)
    # Full-amplitude Gaussian moment and upper-cap certificates used in
    # the signed partial-summation bound, valid for k>=8.
    y2_over_k2_upper = F(41, 2)**2+F(2, 8)
    y4_over_k4_upper = (F(41, 2)**4+12*F(41, 2)**2/8+F(12, 8**2))
    q0_square_upper = 1+F(1, 2*8)
    assert y2_over_k2_upper < 421 and y4_over_k4_upper < 421**2
    assert q0_square_upper == F(17, 16)
    assert 421*q0_square_upper < 22**2
    assert F(421, 4)*q0_square_upper < 11**2
    assert F(421**2, 4)*q0_square_upper < 217**2
    assert F(11, 8)+217 < 240
    assert F(121, 16)*8 > 60 and 2**60 > 13*8
    assert F(121, 16)-F(1, 8) > 0
    baseline_exponent = F(81, 16)-alpha*delta
    assert baseline_exponent == -F(439, 400)
    assert 24/(2+24*k)-F(439, 400) < 0
    baseline_N_exponent = F(31, 10)-F(439, 100)
    assert baseline_N_exponent == -F(129, 100)
    assert F(720)/(720*N+735)-F(129, 100) < 0
    baseline_prefactor = A/delta*(2+24*4*(N+1))
    assert baseline_prefactor == 7935
    assert F(129, 100)*N+F(439, 100) == F(1729, 100) > 17
    e_strict_lower = sum((F(1, math.factorial(j)) for j in range(5)), F(0))
    assert e_strict_lower > F(8, 3)
    baseline_exp_lower = F(8, 3)**17
    assert baseline_exp_lower > 7935000
    baseline_ratio_upper = F(7935)/baseline_exp_lower
    assert baseline_ratio_upper < F(1, 1000)
    assert F(1, 1000)+F(1, 16) < F(1, 4)

    # Cofactor-aware C(d) estimates: individual modes instead of a
    # geometric envelope, differentiated only after removing d^(-it).
    p, beta, delta = F(5, 2), F(71, 4), F(7, 20)
    assert e_strict_lower > p
    assert 1+1/(p-1) == F(5, 3)  # Integral-test bound for zeta(5/2).
    assert 2*3*F(5, 3) == 10
    assert 6**5 > 80**2  # 10/6^(5/2)<1/8.
    theta_max, lemma_k_min = F(1, 100), F(8)
    q0_second_moment = (F(3, 2)**2+1/(2*lemma_k_min)
                        +theta_max**2/(4*lemma_k_min**2))
    assert q0_second_moment < 4
    assert F(11, 4)/(1-F(1, 4*8*100**2)) < 3
    assert F(1, 4)-p == -F(9, 4)
    assert (F(1, 4)-p)**2+20*(F(1, 4)-p) == -F(639, 16)
    assert F(3, 2)**20 < 2**13  # Prefix A=3 for Y^(13/20).
    assert 1-delta == F(13, 20)
    assert beta > alpha and 26-beta == F(33, 4)
    assert p-delta == F(43, 20)
    secondary_coefficient_per_k = (F(3, 8)*beta
                                   +3/(p-delta)*(F(1, 8)/8+beta/4))
    assert secondary_coefficient_per_k < 15
    secondary_exponent = (p-delta)*beta-F(639, 16)
    assert secondary_exponent == -F(71, 40)
    assert 1/k-F(71, 40) < 0
    assert p+F(31, 10)-F(71, 10) == -F(3, 2)
    assert 1/(N+1)-F(3, 2) < 0
    secondary_base_prefactor = 60*(N+1)
    secondary_base_exponent = F(3, 2)*N+F(71, 10)
    assert secondary_base_prefactor == 660
    assert secondary_base_exponent == F(221, 10) > 22
    secondary_exp_lower = F(5, 2)**22
    assert secondary_exp_lower > 660000
    secondary_ratio_upper = secondary_base_prefactor/secondary_exp_lower
    assert secondary_ratio_upper < F(1, 1000)

    # Complete high-pair estimate at E=exp(beta*k).
    assert 2*A/delta == F(120, 7)
    stronger_exponent = F(81, 16)-beta*delta
    assert stronger_exponent == -F(23, 20)
    assert 24/(2+24*k)-F(23, 20) < 0
    assert F(31, 10)-F(23, 5) == -F(3, 2)
    assert 96/(96*N+98)-F(3, 2) < 0
    stronger_base_prefactor = F(120, 7)*(96*N+98)
    stronger_base_exponent = F(3, 2)*N+F(23, 5)
    assert stronger_base_prefactor == F(126960, 7)
    assert stronger_base_exponent == F(98, 5) > 19
    stronger_exp_lower = F(5, 2)**19
    assert stronger_exp_lower > F(126960000, 7)
    stronger_ratio_upper = stronger_base_prefactor/stronger_exp_lower
    assert stronger_ratio_upper < F(1, 1000)

    # Continuum at E uses its complete finite coefficient.
    assert 1+beta+beta**2 < 334
    stronger_continuum_ratio_upper = F(334, 2**409)
    assert stronger_continuum_ratio_upper < F(1, 16)
    # The refined G_D differs from G_E by secondary signed deletion plus
    # the affordable full product tail; continuum at E is retained.
    assert F(1, 8)+2*F(1, 1000) < F(1, 4)
    return {
        "input_scope": "conditional constants only; neither dyadic twisted Mobius input is proved or numerically certified",
        "baseline": {
            "dyadic_input": "every partial block prefix <=Y^(3/5)",
            "prefix_A": 3, "delta": "2/5",
            "full_signed_prefactor": "(15/2)*(2+24k)",
            "full_signed_exponent_per_k": str(baseline_exponent),
            "ratio_over_eta_all_N_upper": "(720N+735)*exp(-129N/100-439/100)",
            "base_N10_exp_lower": str(baseline_exp_lower),
            "base_N10_ratio_upper": str(baseline_ratio_upper),
            "Gaussian_y_second_moment_over_k_squared_upper_at_k8": str(y2_over_k2_upper),
            "Gaussian_y_fourth_moment_over_k_fourth_upper_at_k8": str(y4_over_k4_upper),
            "Gaussian_q0_second_moment_upper_at_k8": str(q0_square_upper),
            "signed_integral_amplitude_coefficient_upper": "1+22k; complete endpoint-inclusive bound retained as 2+24k",
            "absolute_envelope_coefficient_upper": "11k+217k^2<240k^2 for k>=8",
        },
        "cofactor_aware_lemma": {
            "C_definition": "d^(it)*(sum_(r>=1)W(dr)-Phi(1)/d)",
            "C_majorant_constant": "1/8",
            "d_times_C_prime_majorant_constant": "1/4",
            "common_majorant": "T^(5/2)*d^(3/2)*exp(-639k/16)",
            "constant_square_certificate": "6^5>80^2",
            "rotated_q0_second_moment_upper_at_T100_k8": str(q0_second_moment),
            "analytic_scope": "constants checked; differentiated Poisson/contour argument requires companion proof",
        },
        "cofactor_aware_criterion": {
            "dyadic_input": "every partial block prefix <=Y^(13/20)",
            "prefix_A": 3, "delta": "7/20", "secondary_E": "exp(71k/4)",
            "secondary_coefficient_per_k_upper_at_k8": str(secondary_coefficient_per_k),
            "secondary_error_upper": "15*k*T^(5/2)*exp(-71k/40)",
            "secondary_error_over_eta_all_N_upper": "60*(N+1)*exp(-3N/2-71/10)",
            "secondary_base_N10_ratio_upper": str(secondary_ratio_upper),
            "high_pair_error_upper": "(120/7)*(2+24k)*exp(-23k/20)",
            "high_pair_error_over_eta_all_N_upper": "(120/7)*(96N+98)*exp(-3N/2-23/5)",
            "high_pair_base_N10_ratio_upper": str(stronger_ratio_upper),
            "continuum_coefficient_upper": "334k^2",
            "continuum_base_N10_ratio_upper": str(stronger_continuum_ratio_upper),
            "G_D_total_over_eta_upper": "1/8+2/1000<1/4",
        },
    }


def main():
    identities = finite_identity_checks()
    constants = elementary_certificates()
    budgets = all_sample_budget_checks()
    partial_summation = partial_summation_checks()
    conditional_signed = conditional_signed_constant_checks()
    source = Path(__file__).resolve()
    record = {
        "date": "2026-10-04",
        "prepared_for": "Edward Baker",
        "model": "GPT-6 (Codex), inherited configuration; exact serving variant and configured reasoning effort not exposed and not inferred",
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "reference_source_sha256": REFERENCE_SOURCE_SHA256,
        "reference_source_scope": "provenance only; reference files are neither imported nor consumed during replay",
        "method": "standard library, exact integers and fractions.Fraction; no floating sign decisions",
        "claim_scope": "exact finite algebra and constant/budget arithmetic; analytic contour rotation and Poisson arguments require the companion proof; no giant arithmetic-sum or Fourier certificate and no signed cancellation bound",
        "parameters": {
            "b": "3/4", "Gaussian_center": "20k", "p": "5/2",
            "theta": "1/T", "T_min": 100, "k_min": 44, "N_min": 10,
            "k_samples": "4(N+1),4(N+2),...,8N", "eta_N": "(8e)^(-N)",
            "D": "exp(77k/5)", "B": "exp(26k)",
            "strict_cofactor_upper": "exp(53k/5)",
            "optional_relative_frequency_band": [-3, 3],
        },
        "constants": constants,
        "identities": identities,
        "budgets": budgets,
        "partial_summation": partial_summation,
        "conditional_signed_constants": conditional_signed,
        "example_T_3e12": {
            "N": 41, "k_min": 168, "k_max": 328,
            "log_D_range": [str(F(77, 5)*168), str(F(77, 5)*328)],
            "log_B_range": [4368, 8528],
            "log_cofactor_upper_range": [str(F(53, 5)*168), str(F(53, 5)*328)],
            "scope": "scale illustration only; no actual large sum is evaluated",
        },
        "status": "checks passed; the signed arithmetic detector bound remains unproved",
    }
    target = source.with_name("poisson_refinement_record_20261004.json")
    target.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"record": str(target), "source_sha256": record["source_sha256"],
                      "identities": identities,
                      "deletion_ratio_upper_at_N10": budgets["deletion_base_N10_rational_ratio_upper"],
                      "prefactor": constants["poisson_error_prefactor_after_alpha"],
                      "exponent_per_k": constants["poisson_error_exponent_per_k"],
                      "partial_summation": partial_summation,
                      "conditional_signed_baseline_ratio_upper": conditional_signed["baseline"]["base_N10_ratio_upper"],
                      "conditional_cofactor_aware_high_pair_ratio_upper": conditional_signed["cofactor_aware_criterion"]["high_pair_base_N10_ratio_upper"]}, indent=2))


if __name__ == "__main__":
    main()
