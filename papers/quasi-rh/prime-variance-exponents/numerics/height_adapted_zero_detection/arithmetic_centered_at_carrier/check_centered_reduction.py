"""Finite diagnostics for the carrier-centered full-Lambda reduction.

Prepared for Edward Baker with substantial LLM assistance, 4 October 2026.
Model: GPT-6 (Codex), inherited configuration; exact variant/effort unexposed.
Exact synthetic identities and floating phase controls, not a zero certificate.
"""

import argparse
import cmath
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial, floor, log
from pathlib import Path


@dataclass(frozen=True)
class G:
    """A complex rational number."""
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other):
        other = gaussian(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-gaussian(other))

    def __mul__(self, other):
        other = gaussian(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, G):
            denom = other.re**2 + other.im**2
            return self * G(other.re/denom, -other.im/denom)
        return G(self.re/F(other), self.im/F(other))


def gaussian(value):
    return value if isinstance(value, G) else G(F(value))


ZERO = G()
ONE = G(F(1))
q = F(7, 3)


def vadd(left, right, scale=ONE):
    """Vectors in formal log-prime symbols; key 0 is a constant."""
    result = dict(left)
    for symbol, coefficient in right.items():
        value = result.get(symbol, ZERO) + coefficient * scale
        if value == ZERO:
            result.pop(symbol, None)
        else:
            result[symbol] = value
    return result


def constant(value):
    return {} if value == ZERO else {0: value}


def factors(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def mu(n):
    fs = factors(n)
    return 0 if any(a > 1 for a in fs.values()) else (-1) ** len(fs)


def lambda_vector(n):
    fs = factors(n)
    return {next(iter(fs)): ONE} if len(fs) == 1 else {}


def log_vector(n):
    return {p: gaussian(a) for p, a in factors(n).items()}


def prime_vector(n):
    fs = factors(n)
    return {n: ONE} if len(fs) == 1 and fs.get(n) == 1 else {}


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def multiply_polynomials(left, right):
    result = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] = result[i+j] + a*b
    return result


def polynomial_power(base, power):
    result = [ONE]
    for _ in range(power):
        result = multiply_polynomials(result, base)
    return result


def evaluate(poly, x):
    result = ZERO
    for a in reversed(poly):
        result = result*x + a
    return result


def derivative(poly):
    return [poly[j] * j for j in range(1, len(poly))]


def make_kernel(power, rotation):
    # P=(u-1)^power*(2-u)^power; ell=rotation*P', primitive=-rotation*P.
    poly = multiply_polynomials(
        polynomial_power([gaussian(-1), ONE], power),
        polynomial_power([gaussian(2), gaussian(-1)], power))
    primitive = [-a*rotation for a in poly]
    shell = derivative([a*rotation for a in poly])

    def ell(x):
        return evaluate(shell, x) if 1 < x < 2 else ZERO

    def prim(x):
        return evaluate(primitive, x) if 1 < x < 2 else ZERO

    def fprobe(x):
        return prim(x)/x if 1 < x < 2 else ZERO

    # Integral P_t/u: rational terms plus the constant coefficient*log(2).
    moment = {}
    moment = vadd(moment, {2: primitive[0]})
    rational = sum((primitive[j]*F(2**j-1, j)
                    for j in range(1, len(primitive))), ZERO)
    moment = vadd(moment, constant(rational))
    return ell, prim, fprobe, moment


def cofactor_kernel(ell, v):
    return sum((ell(k*v) for k in range(1, floor(F(2)/v)+1)), ZERO)


def vaughan_at(n, cutoff):
    result = {}
    for d in divisors(n):
        if d <= cutoff:
            result = vadd(result, log_vector(n//d), gaussian(mu(d)))
            for b in divisors(n//d):
                if b <= cutoff:
                    result = vadd(result, lambda_vector(b), gaussian(-mu(d)))
        else:
            for b in divisors(n//d):
                if b > cutoff:
                    result = vadd(result, lambda_vector(b), gaussian(mu(d)))
    if n <= cutoff:
        result = vadd(result, lambda_vector(n))
    return result


def arithmetic_checks():
    counts = {"full_lambda_vaughan_coefficients": 0,
              "complex_weighted_high_divisor_grouping": 0,
              "complex_exact_density_cancellation": 0}
    negative = {"prime_power_deletion_changes_sum": False,
                "weak_lower_cutoff_changes_sum": False,
                "omitting_density_remainder_changes_identity": False}
    cutoffs = [F(2), F(5, 2), F(3), F(13, 4), F(4), F(9, 2), F(6)]
    for cutoff in cutoffs:
        for n in range(1, 257):
            assert vaughan_at(n, cutoff) == lambda_vector(n), (n, cutoff)
            counts["full_lambda_vaughan_coefficients"] += 1

    for power, rotation in [(3, G(F(1), F(2))), (4, G(F(2), F(-1)))]:
        ell, prim, fprobe, moment = make_kernel(power, rotation)
        assert prim(F(1)) == prim(F(2)) == ZERO
        for X in map(F, [8, 12, 17, 31, 48, 81, 121]):
            for U in cutoffs:
                if U*U > X:
                    continue
                Z = 2*X/U
                outer = grouped = prime_only = weak = {}
                density = ZERO
                for m in range(1, floor(Z)+1):
                    if m <= U:
                        continue
                    a = sum(mu(d) for d in divisors(m) if d > U)
                    density += prim(m*U/X) * F(a, m) / q
                    for n in range(1, floor(Z)+1):
                        if n > U:
                            weight = ell(F(m*n)/X) * a / (q*X)
                            outer = vadd(outer, lambda_vector(n), weight)
                            prime_only = vadd(prime_only, prime_vector(n), weight)
                for d in range(1, floor(Z)+1):
                    for n in range(1, floor(Z)+1):
                        if d > U and n > U:
                            weight = cofactor_kernel(ell, F(d*n)/X) * mu(d)/(q*X)
                            grouped = vadd(grouped, lambda_vector(n), weight)
                        if d >= U and n > U:
                            weight = cofactor_kernel(ell, F(d*n)/X) * mu(d)/(q*X)
                            weak = vadd(weak, lambda_vector(n), weight)
                assert outer == grouped, (power, X, U)
                counts["complex_weighted_high_divisor_grouping"] += 1
                negative["prime_power_deletion_changes_sum"] |= prime_only != grouped
                negative["weak_lower_cutoff_changes_sum"] |= weak != grouped

                Y = X/U
                M1 = sum((F(mu(d), d) for d in range(1, floor(U)+1)), F(0))
                density_plus_continuum = vadd(constant(density), moment, gaussian(M1/q))
                remainder = {}
                for d in range(1, floor(U)+1):
                    y = Y/d
                    lattice = sum((fprobe(F(k)/y)
                                   for k in range(1, floor(2*y)+1)), ZERO)
                    rf = vadd(constant(lattice), moment, gaussian(-y))
                    remainder = vadd(remainder, rf, gaussian(-F(mu(d))/(q*Y)))
                assert density_plus_continuum == remainder, (power, X, U)
                counts["complex_exact_density_cancellation"] += 1
                negative["omitting_density_remainder_changes_identity"] |= remainder != {}
    assert all(negative.values()), negative
    return counts, negative


def rational_budget_checks():
    checks = {}
    T = F(100)
    # A>3/4; replace inverse powers by (4/3)^j.
    first = factorial(8)*F(4,3)**9*9*2**67
    checks["primitive_product_term_below_2pow90"] = first < 2**90
    checks["primitive_term_below_2pow67_T7"] = first < 2**67*T**7
    middle = sum((F(factorial(8), factorial(j+1))*F(4,3)**(8-j)*T**j
                  for j in range(7)), F(0))
    checks["middle_coefficient_sum_below_16_T6"] = middle < 16*T**6
    checks["middle_variation_below_2pow67_T7"] = 48*2**67*T**6 < 2**67*T**7
    checks["full_eighth_variation_below_2pow75_T7"] = (
        first+3*2**67*middle+F(4,3)*2**74*T**7 < 2**75*T**7)
    checks["poisson_eighth_constant_below_2pow_minus20"] = 1209600 > 2**20
    checks["density_prefactor_below_2pow54"] = F(2**75, 1209600)/q < 2**54
    checks["balanced_density_below_2pow_minus32_r"] = F(1,2**26)/T < F(1,2**32)
    checks["saved_vaughan_prefactor"] = F(2**60, 2**70) == F(1,2**10)
    assert all(checks.values()), checks
    return checks


def density_frequency(xi, length):
    return length if xi == 0 else (1-cmath.exp(-1j*xi*length))/(1j*xi)


def floating_phase_checks():
    max_error = 0.0
    samples = 0
    omitted_phase_changes = False
    conjugated_factor_changes = False
    # Small finite arithmetic polynomials; synthetic multiplier cancels in comparison.
    U, Z, H = 2.5, 23.75, 6.4
    length = log(Z/U)
    for t in [-100.0, 100.0, 317.25]:
        for nu in [-t, -t+0.01, -17.0, -0.25, 0.0, 0.75, 9.0]:
            xi = t+nu
            dm = sum(mu(n)/n*cmath.exp(-1j*xi*log(n/U))
                     for n in range(1, floor(Z)+1) if n > U)
            dl = sum(log(next(iter(factors(n))))/n*cmath.exp(-1j*xi*log(n/U))
                     for n in range(1, floor(Z)+1) if n > U and len(factors(n)) == 1)
            de = dl-density_frequency(xi, length)
            mt = sum(mu(n)/n*cmath.exp(-1j*t*log(n/U))*cmath.exp(-1j*nu*log(n/U))
                     for n in range(1, floor(Z)+1) if n > U)
            lt = sum(log(next(iter(factors(n))))/n*cmath.exp(-1j*t*log(n/U))*
                     cmath.exp(-1j*nu*log(n/U))
                     for n in range(1, floor(Z)+1) if n > U and len(factors(n)) == 1)
            et = lt-density_frequency(t+nu, length)
            uncentered = cmath.exp(1j*xi*log(H))*dm*de
            centered = cmath.exp(1j*t*log(H))*cmath.exp(1j*nu*log(H))*mt*et
            max_error = max(max_error, abs(uncentered-centered))
            assert abs(uncentered-centered) < 1e-10
            omitted = cmath.exp(1j*nu*log(H))*mt*et
            conjugated = cmath.exp(1j*xi*log(H))*mt*et.conjugate()
            omitted_phase_changes |= abs(omitted-centered) > 1e-6
            conjugated_factor_changes |= abs(conjugated-centered) > 1e-6
            if nu == -t:
                assert density_frequency(xi, length) == length
            samples += 1
    assert omitted_phase_changes and conjugated_factor_changes
    return {"samples": samples, "maximum_absolute_phase_error": max_error,
            "tolerance": 1e-10,
            "density_value_at_displaced_origin_checked": True}, {
        "omitted_carrier_prefactor_changes_result": omitted_phase_changes,
        "conjugated_second_factor_changes_result": conjugated_factor_changes}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path,
                        default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    counts, negative = arithmetic_checks()
    budgets = rational_budget_checks()
    floating, float_negative = floating_phase_checks()
    source_paths = [
        "notes/height_adapted_zero_detection/PRIORITIZED_ASSESSMENT_20261004.md",
        "notes/height_adapted_zero_detection/gaussian_localization/HEIGHT_UNIFORM_VAUGHAN_REDUCTION_20261004.md",
        "notes/programs/01_signed_arithmetic_covariance/FINITE_CROSS_SPECTRUM_20261004.md",
        "notes/programs/01_signed_arithmetic_covariance/PRIME_DISCREPANCY_CENTERING_20261004.md",
    ]
    source_hashes = {}
    for name in source_paths:
        path = args.source_root/name
        if not path.is_file():
            raise FileNotFoundError(f"Missing reference source {path}; use --source-root")
        source_hashes[name] = sha256(path.read_bytes()).hexdigest()
    record = {
        "date": "2026-10-04", "model": "GPT-6 (Codex), inherited configuration",
        "reasoning_effort": "not exposed; not inferred",
        "status": "passed finite exact diagnostics and floating phase controls",
        "exact_identity_counts": counts,
        "exact_rational_budget_checks": budgets,
        "exact_negative_controls": negative,
        "floating_phase_diagnostics": floating,
        "floating_negative_controls": float_negative,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "reference_source_sha256": source_hashes,
        "limits": [
            "Synthetic complex polynomial kernels and formal prime-log symbols.",
            "No numerical validation of true prepared kernel derivative norms.",
            "No Mellin quadrature, analytic spectral-tail certification, or central saving.",
            "Floating phase controls are not outward arithmetic certificates.",
            "No claim about any actual zeta zero or continuous-parameter exclusion.",
        ],
    }
    output = Path(__file__).with_name("centered_reduction_record_20261004.json")
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "passed", "exact_identity_counts": counts,
                      "rational_budget_checks": len(budgets),
                      "floating_samples": floating["samples"],
                      "record": str(output)}, indent=2))


if __name__ == "__main__":
    main()
