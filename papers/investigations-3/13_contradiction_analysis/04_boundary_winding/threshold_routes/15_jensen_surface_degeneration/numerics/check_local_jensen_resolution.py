#!/usr/bin/env python3
"""Bounded BW-15 comparison; rigorous balls, machine-dependent timings.

For Edward Baker, 2026-10-21. Substantial LLM assistance:
gpt-6-astra (Codex), recorded effort max. No global RH/simplicity claim.
Requires python-flint==0.9.0 (FLINT 3.6.0 in the recorded environment).
"""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import time

import flint
from flint import acb, acb_series, arb, ctx


K = 64
GUARD_BITS = 832


def xi(w):
    return w * (w - 1) / 2 * (-w / 2 * arb.pi().log()).exp() * (w / 2).gamma() * w.zeta()


def f_series(c, length, radius=None):
    """Taylor coefficients at every point of a square containing the disk.

    The negative-real branch is evaluated as i sqrt(-s), so the square
    never crosses the square-root branch cut. xi's symmetry supplies f.
    """
    ctx.cap = length
    z = acb(c) if radius is None else acb(arb(c, radius), arb(0, radius))
    s = acb_series([z, 1])
    w = acb(0, 1) * (-s).sqrt() if c < 0 else s.sqrt()
    return xi(w + arb(1) / 2)


def star_series(c, length, radius=None):
    ctx.cap = length
    z = acb(c) if radius is None else acb(arb(c, radius), arb(0, radius))
    s = acb_series([z, 1])
    if c < 0:
        q = (-s).sqrt() * arb.pi()
        return (1 + s) * q.sin() / q
    q = s.sqrt() * arb.pi()
    return (1 + s) * (q.exp() - (-q).exp()) / (2 * q)


def show(x):
    return x.str(30)


def positive(x, label):
    if not (x.is_finite() and x > 0):
        raise ArithmeticError(f"Unresolved positive comparison: {label}: {x}")


def real_part(x):
    # Used only where the mathematical function is known to be real.
    if not x.imag.contains(0):
        raise ArithmeticError("Reality check failed")
    return x.real


def central_coefficients(bits):
    ctx.prec = bits
    ctx.cap = 2 * K + 1
    v = xi(acb_series([arb(1) / 2, 1]))
    for k in range(1, 2 * K + 1, 2):
        if not v[k].contains(0):
            raise ArithmeticError("Evenness check failed")
    return [real_part(v[2 * k]) for k in range(K + 1)]


def jensen_coefficients(coeff, degree):
    b = arb(1)
    out = []
    for k, ck in enumerate(coeff):
        if k:
            b = b * (degree - k + 1) / degree
        out.append(ck * b)
    return out


def polynomial_value(coeff, x):
    v = arb(0)
    for ck in reversed(coeff):
        v = v * x + ck
    return v


def linear_margin(coeff, c, r):
    p0 = polynomial_value(coeff, c)
    p1 = polynomial_value([k * coeff[k] for k in range(1, len(coeff))], c)
    R = abs(c) + r
    m2 = sum((k * (k - 1) * abs(coeff[k]) * R ** (k - 2)
              for k in range(2, len(coeff))), arb(0))
    margin = abs(p1) * r - abs(p0) - m2 * r * r / 2
    return p0, p1, m2, margin


def direct_method(bits):
    ctx.prec = bits
    c, r = -arb(19979) / 100, arb(1) / 1000
    start = time.perf_counter()
    fc = f_series(c, 2)
    f0, f1 = real_part(fc[0]), real_part(fc[1])
    m2 = 2 * abs(f_series(c, 3, r)[2])
    margin = abs(f1) * r - abs(f0) - m2 * r * r / 2
    positive(margin, "direct Rouche margin")
    elapsed = time.perf_counter() - start
    return {
        "target_bits": bits,
        "f_center": show(f0), "f_prime_center": show(f1),
        "local_second_derivative_upper": show(m2.upper()),
        "rouche_margin": show(margin),
        "root_count_with_multiplicity": 1,
        "seconds_total": elapsed,
        "complete_xi_series_calls": 2,
        "series_lengths": [2, 3],
        "working_bits": bits,
    }


def jensen_method(bits, local_refinement=False):
    total_start = time.perf_counter()
    coeff_start = time.perf_counter()
    coeff = central_coefficients(bits + GUARD_BITS)
    for ck in coeff:
        positive(ck, "positive complete theta coefficient")
    ctx.prec = bits
    coeff = [ck + arb(0) for ck in coeff]  # pay down-rounding
    coefficient_seconds = time.perf_counter() - coeff_start
    c, r = -arb(19979) / 100, arb(1) / 1000
    R, eps = -c + r, arb(1) / 10**9
    moment_start = time.perf_counter()
    radial = f_series(R, 5 if local_refinement else 3)
    A = R * R * real_part(radial[2])  # R^2 f''(R)/2
    full_at_rho = real_part(f_series(2 * R, 1)[0])
    positive(A, "A_R")
    tail = full_at_rho / arb(2) ** (K + 1)
    extra = {}
    if local_refinement:
        # The complete omitted second-derivative tail is bounded because
        # k(k-1) 2^(-k) decreases for all k >= K+1 (K >= 2).
        second_coeff = [k*(k-1)*coeff[k] for k in range(2,len(coeff))]
        third_at_R = sum((k*(k-1)*(k-2)*coeff[k]*R**(k-3)
                          for k in range(3,len(coeff))),arb(0))
        second_tail = K*(K+1)*tail/(R*R)
        L2 = abs(polynomial_value(second_coeff,c)) + r*third_at_R + second_tail
        B = R*R*L2/2
        C = (3*R**4*real_part(radial[4]) + 3*R**3*real_part(radial[3])
             + R*R*real_part(radial[2])/2)
        threshold = (B+(B*B+4*eps*C).sqrt())/(2*eps)
        extra = {"local_f_second_derivative_upper":show(L2.upper()),
                 "omitted_second_derivative_tail_upper":show(second_tail.upper()),
                 "B_local":show(B),"C_R":show(C)}
    else:
        threshold = A/eps
    # The integer pays the selected envelope <= 1e-9, not actual error.
    degree = int(threshold.upper().ceil().unique_fmpz())
    if degree % 2 == 0:
        degree += 1
    approximation_error = B/degree+C/(degree*degree) if local_refinement else A/degree
    if not approximation_error <= eps:
        raise ArithmeticError("Degree does not pay approximation error")
    moment_seconds = time.perf_counter() - moment_start
    consumer_start = time.perf_counter()
    pc = jensen_coefficients(coeff, degree)
    p0, p1, m2, margin = linear_margin(pc, c, r)
    margin_F = margin - tail
    margin_f = margin_F - approximation_error
    positive(margin_F, "full Jensen polynomial Rouche margin")
    positive(margin_f, "limiting theta function Rouche margin")
    coefficient_radius_budget = sum((ck.rad() * R**k for k, ck in enumerate(coeff)), arb(0))
    if not coefficient_radius_budget < arb("1e-12"):
        raise ArithmeticError("Coefficient ball radii exceed budget")
    consumer_seconds = time.perf_counter() - consumer_start
    total_seconds = time.perf_counter() - total_start
    return {
        "target_bits": bits, "coefficient_working_bits": bits + GUARD_BITS,
        "bound":"local E5" if local_refinement else "radial E4",
        "retained_coefficients": K + 1,
        "highest_xi_derivative_order": 2 * K,
        "degree": degree, "genus_if_squarefree": (degree - 1) // 2,
        "A_R": show(A), "f_at_2R": show(full_at_rho),
        "approximation_error":show(approximation_error),
        "E4_envelope_at_this_degree": show(A / degree),
        "omitted_Jensen_tail_upper": show(tail.upper()),
        "weighted_coefficient_radius_budget": show(coefficient_radius_budget.upper()),
        "P_center": show(p0), "P_prime_center": show(p1),
        "polynomial_second_derivative_upper": show(m2.upper()),
        "raw_linear_margin": show(margin),
        "full_Jensen_margin": show(margin_F), "theta_transfer_margin": show(margin_f),
        "root_count_P_F_and_f_with_multiplicity": [1, 1, 1],
        "seconds_coefficients": coefficient_seconds,
        "seconds_full_moments_and_degree": moment_seconds,
        "seconds_consumer": consumer_seconds,
        "seconds_total": total_seconds,
        "complete_xi_series_calls": 3, "series_lengths": [129, 5 if local_refinement else 3, 1],
        "height_interval": [show((-c-r).sqrt()), show((-c+r).sqrt())],
        "physical_z_interval": [show(2*(-c-r).sqrt()), show(2*(-c+r).sqrt())],
        **extra,
    }


def controls():
    ctx.prec = 256
    quadratic = []
    for d in (65, 1000001):
        b2 = Fraction(d - 1, d)
        discriminant = Fraction(4) - 4 * b2
        gap_squared = discriminant / b2**2
        assert gap_squared == Fraction(4*d, (d-1)**2)
        quadratic.append({"degree": d, "squared_gap": str(gap_squared),
                          "sqrt_d_times_gap": str(Fraction(2*d, d-1))})
    factorial = 1
    sine_coeff = []
    for k in range(K + 1):
        if k:
            factorial *= (2*k)*(2*k+1)
        sine_coeff.append(arb.pi()**(2*k)/factorial)
    coeff = [sine_coeff[0]] + [sine_coeff[k]+sine_coeff[k-1] for k in range(1,K+1)]
    d = 1000001
    pc = jensen_coefficients(coeff, d)
    a, outer_r = arb(-1), arb(1)/100
    R = abs(a)+outer_r
    # f_*(a)=f_*'(a)=0 and f_*''(a)/2=1/2 exactly.
    m3 = 6*abs(star_series(a,4,outer_r)[3])
    limiting_margin = outer_r**2/2 - m3*outer_r**3/6
    A = R**2*real_part(star_series(R,3)[2])
    full_F_margin = limiting_margin - A/d
    positive(full_F_margin,"double-control outer two-zero count")
    split = []
    for sign in (-1,1):
        c, r = a+arb(sign)/1000, arb(1)/100000
        p0,p1,m2,margin=linear_margin(pc,c,r)
        Rsmall=abs(c)+r
        tail=real_part(star_series(2*Rsmall,1)[0])/arb(2)**(K+1)
        positive(margin-tail,"simple finite Jensen branch")
        assert abs(c-a)>r
        split.append({"center":show(c),"radius":show(r),
                      "full_Jensen_simple_root_margin":show(margin-tail),
                      "limiting_function_root_count":0})
    return {"quadratic_exact":quadratic,
            "infinite_product_double":{
                "degree":d,"retained_coefficients":K+1,
                "limiting_function_exact_double_at":-1,
                "outer_disk_radius":show(outer_r),
                "third_derivative_upper":show(m3.upper()),
                "limiting_two_root_margin":show(limiting_margin),
                "full_Jensen_two_root_margin":show(full_F_margin),
                "split_disks":split,
                "interpretation":"Finite simple branch points coexist with a limiting double zero."}}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    # Record, rather than conceal, the conditioning failure of a naive
    # 192-bit central-series acquisition. It is outside method timings.
    naive=central_coefficients(192)
    R=arb(199791)/1000
    naive_radius=sum((v.rad()*R**k for k,v in enumerate(naive)),arb(0))
    assert naive_radius > arb('1e-12')
    runs=[]
    for bits in (192,256):
        direct=direct_method(bits)
        jensen=jensen_method(bits)
        refined=jensen_method(bits,local_refinement=True)
        ratio=jensen['seconds_total']/direct['seconds_total']
        runs.append({"direct":direct,"jensen":jensen,
                     "jensen_over_direct_seconds":ratio,
                     "factor_two_speed_gate_passed":ratio<=0.5,
                     "local_refinement":refined,
                     "refined_over_direct_seconds":refined['seconds_total']/direct['seconds_total'],
                     "refined_factor_two_speed_gate_passed":refined['seconds_total']<=direct['seconds_total']/2,
                     "degree_reduction_factor":jensen['degree']/refined['degree']})
    if runs[0]['jensen']['degree']!=runs[1]['jensen']['degree']:
        raise ArithmeticError('Degree changed across precision replay')
    if runs[0]['local_refinement']['degree']!=runs[1]['local_refinement']['degree']:
        raise ArithmeticError('Refined degree changed across precision replay')
    result={
        "date":"2026-10-21","timezone":"America/New_York",
        "prepared_for":"Edward Baker","model":"gpt-6-astra","effort":"max",
        "llm_assistance":"Substantial; same-assistant implementation and checks.",
        "python_version":platform.python_version(),"python_flint":flint.__version__,
        "flint":flint.__FLINT_VERSION__,"platform":platform.platform(),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameters":{"s_center":"-19979/100","s_radius":"1/1000", "heat_time":0,
                      "K":K,"guard_bits":GUARD_BITS,"E4_error_target":"1e-9"},
        "naive_192bit_weighted_coefficient_radius":show(naive_radius),
        "precision_amendment":"After the recorded initial cancellation failure, use 832 guard bits for central coefficient acquisition only; check all returned balls. No increase in the coefficient budget.",
        "runs":runs,"controls":controls(),
        "timing_scope":"All mathematical data acquisition, rounding and certificate arithmetic; common imports/process startup excluded. One execution at each precision; timings are observations, not complexity bounds.",
        "status":"Interval-certified local root counts and error budgets; timings observational; no RH assumption, global simplicity claim, period certificate, or independent review.",
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"output":str(args.output),"degree":runs[0]['jensen']['degree'],
                      "time_ratios":[v['jensen_over_direct_seconds'] for v in runs],
                      "theta_margins":[v['jensen']['theta_transfer_margin'] for v in runs],
                      "refined_degree":runs[0]['local_refinement']['degree'],
                      "degree_reduction_factor":runs[0]['degree_reduction_factor'],
                      "refined_time_ratios":[v['refined_over_direct_seconds'] for v in runs],
                      "control":"double limit and split finite branches both certified"},indent=2))


if __name__=='__main__':
    main()
