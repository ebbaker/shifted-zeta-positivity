#!/usr/bin/env python3
"""Exact rational checks for the explicit Gaussian-localization note.

Prepared for Edward Baker, 2026-10-04, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact variant and reasoning
effort are not exposed and are not inferred. Standard library only.

This checks arithmetic behind analytic majorants. It does not compute zeta
zeros, certify an arithmetic cancellation estimate, or formally verify the
analytic proofs. Rational Taylor remainders give outward elementary-function
enclosures; decimal strings below are rounded outwards, never used as inputs.
"""

from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import math

TERMS = 80


def point(x):
    return (F(x), F(x))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[1], -a[0])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = [x * y for x in a for y in b]
    return (min(values), max(values))


def div(a, b):
    assert b[0] > 0
    return mul(a, (1 / b[1], 1 / b[0]))


def scale(a, x):
    return mul(a, point(x))


def atanh_log_series(x):
    """Enclose 2*atanh(x), 0 <= x <= 1/3, by a positive series."""
    assert 0 <= x <= F(1, 3)
    total = F(0)
    power = x
    for j in range(TERMS):
        total += 2 * power / (2 * j + 1)
        power *= x * x
    remainder = 2 * power / ((2 * TERMS + 1) * (1 - x * x))
    return (total, total + remainder)


LOG2 = atanh_log_series(F(1, 3))


def log_point(q):
    q = F(q)
    assert q > 0
    exponent = 0
    while q >= 2:
        q /= 2
        exponent += 1
    while q < 1:
        q *= 2
        exponent -= 1
    return add(atanh_log_series((q - 1) / (q + 1)), scale(LOG2, exponent))


def log_interval(a):
    assert a[0] > 0
    # Round the rational inputs outward before the next series. Otherwise
    # nested logarithms generate needlessly huge exact denominators.
    unit = 10**50
    lo = F((a[0]*unit).__floor__(), unit)
    hi = F(ceil(a[1]*unit), unit)
    assert lo > 0
    return (log_point(lo)[0], log_point(hi)[1])


def atan_point(x):
    """Alternating-series enclosure, 0 < x < 1."""
    assert 0 < x < 1
    total = F(0)
    for j in range(TERMS):
        total += (-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
    following = total + (-1) ** TERMS * x ** (2 * TERMS + 1) / (2 * TERMS + 1)
    return (min(total, following), max(total, following))


PI = sub(scale(atan_point(F(1, 5)), 16), scale(atan_point(F(1, 239)), 4))
LOG8E = add(scale(LOG2, 3), point(1))


def exp_small(q):
    """Rational enclosure for exp(q), 0 <= q <= 2."""
    q = F(q)
    assert 0 <= q <= 2
    total, term = F(1), F(1)
    for j in range(1, TERMS + 1):
        term *= q / j
        total += term
    following = term * q / (TERMS + 1)
    remainder = following / (1 - q / (TERMS + 2))
    return (total, total + remainder)


def ceil(q):
    return -((-q.numerator) // q.denominator)


def decimal_out(q, upper, places=18):
    unit = 10 ** places
    integer = ceil(q * unit) if upper else (q * unit).__floor__()
    sign = "-" if integer < 0 else ""
    absolute = abs(integer)
    return f"{sign}{absolute // unit}.{absolute % unit:0{places}d}"


def display(a):
    return [decimal_out(a[0], False), decimal_out(a[1], True)]


def E(T):
    logT = log_point(T)
    loglogT = log_interval(logT)
    e1 = add(add(scale(logT, F("0.10076")),
                 scale(loglogT, F("0.24460"))), point(F("8.08344")))
    e2 = add(add(scale(logT, F("0.11200")),
                 scale(loglogT, F("0.12567"))), point(F("3.77417")))
    return (min(e1[0], e2[0]), min(e1[1], e2[1]))


def guard_count_bound(T):
    """BWv2 bound for closed |gamma-t|<=3, including endpoint limits."""
    T = F(T)
    assert T >= 100
    lower, upper = T - 3, T + 3
    # Algebraically the exact M(upper)-M(lower), with less cancellation.
    numerator = sub(add(scale(log_interval(div(point(lower), scale(PI, 2))), 6),
                        scale(log_point(upper / lower), upper)), point(6))
    main_difference = div(numerator, scale(PI, 2))
    return add(main_difference, add(E(lower), E(upper)))


def polynomial_integral(poly):
    """Integral on [-1/4,1/4] for polynomial coefficients in v."""
    return sum((2 * coefficient * F(1, 4) ** (degree + 1) / (degree + 1)
                for degree, coefficient in enumerate(poly) if degree % 2 == 0), F(0))


def multiply_poly(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def derivative(poly):
    return [j * poly[j] for j in range(1, len(poly))]


def shift_poly(poly, center):
    out = [F(0)] * len(poly)
    for n, coefficient in enumerate(poly):
        for j in range(n+1):
            out[j] += coefficient * math.comb(n,j) * center**(n-j)
    return out


Q_COEFFICIENTS = [F(math.factorial(8+j)*math.comb(8,j)*2**j,
                    math.factorial(8)) for j in range(9)]


def Q_norm_square(sigma):
    """Coefficients in nu^2 of |Q(sigma+i*nu)|^2."""
    real, imaginary = [F(0)]*9, [F(0)]*9
    for j, bj in enumerate(Q_COEFFICIENTS):
        degree = 8-j
        for k in range(degree+1):
            coefficient = bj*math.comb(degree,k)*sigma**(degree-k)
            if k % 2:
                imaginary[k] += coefficient*(-1)**((k-1)//2)
            else:
                real[k] += coefficient*(-1)**(k//2)
    total = [a+b for a,b in zip(multiply_poly(real,real),
                              multiply_poly(imaginary,imaginary))]
    assert not any(total[1::2])
    return total[::2]


def gaussian_tail_upper(p, a, lam):
    """Upper bound integral_a^infty x^p exp(-lam*x^2) dx.

    (a+w)^p <= a^p exp(p*w/a). For the values used here lam*a^2
    is an integer. exp(-n) < 2^-n follows from e>2.
    """
    a, lam = F(a), F(lam)
    exponent = lam * a * a
    n = exponent.__floor__()
    assert n >= 1 and 2 * lam * a - p / a > 0
    return a ** p * F(1, 2 ** n) / (2 * lam * a - p / a)


def checks_and_examples():
    h = [F(0)] * 17
    for j in range(9):
        h[2 * j] = F(math.comb(8, j) * (-16) ** j)
    I0 = polynomial_integral(h)
    a0 = polynomial_integral(multiply_poly(h, h))
    assert polynomial_integral([F(0), F(0)] + h) / I0 == F(1, 304)
    assert a0 > F(13, 40) ** 2
    assert I0 ** 2 > F(91, 200) ** 2 * a0
    a = [a0]
    hj = h
    for j in range(1, 4):
        hj = derivative(hj)
        a.append(polynomial_integral(multiply_poly(hj, hj)))
    assert a[1] / a0 == F(704, 5)
    assert a[2] / a0 == F(3666432, 65)
    assert a[3] / a0 == F(463970304, 13)
    T = F(100)
    norm_ratio_squared = (1 + (15*a[1]/a0 + F(1,2))/T**2
                          + (15*a[2]/a0 + 3*a[1]/a0 + F(1,16))/T**4
                          + (a[3]/a0 + a[2]/(2*a0) + a[1]/(16*a0))/T**6)
    assert norm_ratio_squared < F(111, 100) ** 2
    # Pointwise derivative maxima and the full demodulated physical bound.
    assert F(4096,15)*F(14,15)**14 < 121
    assert 2*F(4,5)**6 < 1
    assert F(1,11)*F(10,11)**10 < F(4,21)**2
    assert 25*F(3,13)**3*F(10,13)**10 < F(4,21)**2
    amplitude = F(40,13)*(F(40001,40000)
                           +11*(F(3,100)+F(1,4_000_000))
                           +256*F(3,10000)+F(8192,1_000_000))
    assert exp_small(F(1,8))[1] < F(8,7)
    assert exp_small(F(1,4))[1] < F(9,7)
    Mh = amplitude*F(12,7)
    baseline = Mh*F(54,49)
    assert baseline < F(33,4)
    # An exact polynomial positivity certificate for the pole reciprocal.
    minus, plus = Q_norm_square(F(-1,2)), Q_norm_square(F(1,2))
    assert minus[-1] == 1 and all(coefficient > 0 for coefficient in minus)
    pole_polynomial = shift_poly([F(51,50)**2*x-y
                                  for x,y in zip(minus,plus)],F(10000))
    assert all(coefficient > 0 for coefficient in pole_polynomial)
    assert F(40001,40000)**9 < F(1001,1000)
    assert F(7,8)*(F(5,4)-F(51,50))*F(1000,1001) > F(1,5)
    assert F(1001,1000)**2 > 1+F(9,10000)
    c0 = 8**8*math.factorial(8)
    pole_reciprocal_constant = F(37037,30000*c0)
    assert pole_reciprocal_constant < F(1,500_000_000_000)
    assert exp_small(F(3, 16))[1] < F(5, 4)
    assert add(exp_small(F(3,16)),
               div(point(1),exp_small(F(3,16))))[1]/2 < F(19,16)
    assert add(exp_small(F(11, 16)),
               div(point(1), exp_small(F(11, 16))))[1] / 2 < F(5, 4)
    assert exp_small(2)[1] < 8  # implies cosh(2)<4 with a separate check
    assert add(exp_small(2), div(point(1), exp_small(2)))[1] / 2 < 4
    assert LOG8E[1] < 4 and PI[0] > 3
    assert LOG8E[1] < F(31,10)
    assert F(17)*F(1,8)*F(99,100)/(608*F(5,4)) > F(1,400)
    assert (1+F(9,4096))**10 < F(33,32)
    assert F(17)*F(1,16)*F(49,50)/(608*2) > F(1,1250)
    assert (1+F(121,4096))**10 < F(3,2)
    assert PI[1] < F(22, 7)
    assert PI[0] > F(25,8)
    assert 6**8 < 2**21 and 5**16 < 2**41
    assert F(221,56)+F(1,100) < 4
    assert 1+F(4,105)+F(1,100) < F(11,10)
    # Core contour inequalities, using deliberately rounded rational bounds.
    base = F(7,3) * F(111,100) * F(200,91) * F(25,21)**3
    assert base * 2 / 5 < 4             # b and original d,c core
    assert base * 2 / 4 < 5             # d=9/16
    assert base * F(19,9) / 31 < F(2,3) # c=13/4
    # Polynomial inverse bounds used outside the Gaussian core.
    normalization = F(7,3)*F(111,100)*F(200,91)
    assert normalization*F(512,15)*F(420,5)*F(17,16)**3*F(77,64) < 25000
    assert normalization*F(4096,63)*F(2000,4)*F(17,16)**3*F(85,64) < 400000
    assert (F(128,127))**23 < F(5,4)
    assert 13+4*16 < F(25000,8**19)*F(63,4)**23
    # Gaussian tails in P: include both signs and 1/(2*pi), use pi>3.
    tail_P = F(400000, 8**19) * gaussian_tail_upper(23, 16, 8) / 3
    assert tail_P * 3 < F(1,100)  # sqrt(8)<3, k^1/2 tail decreases
    # Tails for the L2 bounds of psi and nu*psi, with both signs.
    tail_L2 = 2 * F(25000, 8**19)**2 * gaussian_tail_upper(46, 16, 16)
    tail_nu_L2 = 2 * F(25000, 8**19)**2 * gaussian_tail_upper(48, 16, 16)
    tail_derivative = 2 * F(10**6, 8**19)**2 * gaussian_tail_upper(46, F(127,8), 16)
    assert tail_L2 * 3 < F(1,10**6)
    assert tail_nu_L2 * 4 * 8**2 < F(1,10**6)
    assert tail_derivative * 3 < F(1,10**6)
    # Closed Gaussian-moment squared bounds, retaining the mixed terms.
    sqrtpi_upper, sqrt2_lower, sqrt8_lower = F(71,40), F(141,100), F(14,5)
    assert F(22,7) < sqrtpi_upper**2 and sqrt2_lower**2 < 2
    A2 = (169*sqrtpi_upper/sqrt2_lower + 52/sqrt8_lower
          + 8*sqrtpi_upper/(2*sqrt2_lower*8))
    B2 = 4*(169*sqrtpi_upper/(4*sqrt2_lower) + 26/sqrt8_lower
            + 12*sqrtpi_upper/(4*sqrt2_lower*8))
    C2 = (11664*sqrtpi_upper/sqrt2_lower + 3456/sqrt8_lower
          + 512*sqrtpi_upper/(2*sqrt2_lower*8))
    assert A2 + F(1,10**6) < 16**2
    assert B2 + F(1,10**6) < 16**2
    assert C2 + F(1,10**6) < 128**2
    assert F(14,5)**2 < 8
    assert F(16) * (16 + F(128) / F(14,5)) < 32**2
    # At N=10 the worst early error is at k=4(N+1). Its logarithmic
    # derivative in N is negative afterwards, as explained in the note.
    N, k = 10, 44
    early_log_ratio = add(log_point(F(528,7) * (1+6*k)),
                          sub(scale(LOG8E, N),
                              add(scale(log_point(k), F(1,2)), point(F(279,256)*k))))
    assert early_log_ratio[1] < -4 * LOG2[1]
    # Late uses C_c=2, denominator c-1=9/4, j1=26k.
    late_factor = F(33,2) * (F(4,9)*(1+26*k) + F(16,81))
    late_log_ratio = add(log_point(late_factor),
                         sub(scale(LOG8E,N),
                             add(scale(log_point(k),F(1,2)),point(F(9,4)*k))))
    assert late_log_ratio[1] < -4 * LOG2[1]
    # The note's all-N proofs use these deliberately loose base checks.
    assert 16*F(528,7)*(1+20*44)/6 < 2*19**4
    assert exp_small(1)[0] > 2
    # exp(3)>19 via exp(3/2)^2; exp(12)>19^4 then follows.
    assert exp_small(F(3,2))[0]**2 > 19
    assert 6400*7 < 19**4
    assert F(1,22)+F(31,10)-F(279,64) < 0
    assert F(1,22)+F(31,10)-9 < 0
    assert F(13)+31-F(279,256)*44 < 0
    assert F(12)+31-9*11 < 0
    # Global count proof's low-height seed N(5)<=3.
    M5 = div(scale(sub(log_interval(div(point(5),scale(PI,2))),point(1)),5),scale(PI,2))
    assert add(M5,E(5))[1] < 4
    examples = []
    for height in (100,10**6,3*10**12,10**20):
        Q = guard_count_bound(height)
        N = ceil(Q[1])
        assert ceil(Q[0]) == N
        assert N >= 10 and log_point(height+6)[1] < N
        eps_log = sub(neg(scale(LOG8E,N)),scale(LOG2,8))
        examples.append({"carrier_abs": str(height), "guard_count_upper_expression": display(Q),
                         "N": N, "k_min": 4*(N+1), "k_max": 8*N,
                         "physical_log_interval": [24*(N+1),208*N],
                         "log_arithmetic_threshold_eta_over_256": display(eps_log)})
    return {"I0": str(I0), "a0": str(a0),
            "norm_ratio_squared_at_100": str(norm_ratio_squared),
            "amplitude_upper": str(amplitude), "shell_upper": str(Mh),
            "baseline_before_roundup": str(baseline),
            "endpoint_c0": c0,
            "Q_coefficients_descending": list(map(str,Q_COEFFICIENTS)),
            "minus_half_Q_norm_squared_coefficients": list(map(str,minus)),
            "pole_ratio_positivity_coefficients_in_t_squared_minus_10000": list(map(str,pole_polynomial)),
            "pole_reciprocal_constant_before_roundup": str(pole_reciprocal_constant),
            "pi_enclosure": display(PI), "log_8e_enclosure": display(LOG8E),
            "early_log_error_over_eta_at_N10_k44": display(early_log_ratio),
            "late_log_error_over_eta_at_N10_k44": display(late_log_ratio),
            "examples": examples}


def main():
    checked = checks_and_examples()
    source = Path(__file__)
    record = {"date": "2026-10-04", "prepared_for": "Edward Baker",
              "model": "GPT-6 (Codex), inherited configuration; exact serving variant and reasoning effort not exposed",
              "source_sha256": sha256(source.read_bytes()).hexdigest(),
              "method": "fractions.Fraction, rational Taylor/alternating-series remainders; outward decimal display",
              "claim_scope": "arithmetic checks behind analytic majorants and published count input; no zeta-zero or arithmetic-cancellation certificate",
              "parameters": {"b": "3/4", "d": "9/16", "c": "13/4", "a": 20,
                             "delta": "1/16", "R": 3, "h": 4},
              "proved_analytic_constants": {"B_h": "33/4", "C_inv": 32,
                                            "P_d_prefactor": 4, "P_c_prefactor": 2,
                                            "global_unit_count_C0": 12},
              "checked": checked}
    target = source.with_name("explicit_gaussian_constants_record_20261004.json")
    target.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"record":str(target),"source_sha256":record["source_sha256"],
                      "examples":checked["examples"]},indent=2))


if __name__ == "__main__":
    main()
