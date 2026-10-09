#!/usr/bin/env python3
"""Exact finite checks for the mean-zero short-family continuation.

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; effort is not exposed.

Standard library only. Prints deterministic JSON and writes no files.
The polynomial profile on [1,2] is a finite calculus diagnostic, not a
C-infinity test profile. Formal monoid twists are not residue symbols.
No analytic conductor, Poisson, Euler convergence, prime ideal theorem,
asymptotic moment, zero-free region, or RH conclusion is certified here.
"""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import prod
import json


COUNTS = Counter()


def check(group, condition, detail=""):
    if not condition:
        raise AssertionError(f"{group}: {detail}")
    COUNTS[group] += 1


@dataclass(frozen=True)
class Q6:
    """Exact a+b*zeta_6, where zeta_6**2=zeta_6-1."""
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))

    @staticmethod
    def cast(value):
        return value if isinstance(value, Q6) else Q6(value)

    def __add__(self, other):
        other = self.cast(other)
        return Q6(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q6(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __mul__(self, other):
        other = self.cast(other)
        return Q6(self.a * other.a - self.b * other.b,
                  self.a * other.b + self.b * other.a + self.b * other.b)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return Q6(self.a / F(other), self.b / F(other))

    def __pow__(self, exponent):
        answer = Q6(1)
        for _ in range(exponent):
            answer *= self
        return answer

    def conjugate(self):
        return Q6(self.a + self.b, -self.b)

    def abs2(self):
        return self.a * self.a + self.a * self.b + self.b * self.b


ZERO, ONE, ZETA = Q6(), Q6(1), Q6(0, 1)


def poly_multiply(a, b):
    answer = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            answer[i + j] += x * y
    return tuple(answer)


def poly_power(a, exponent):
    answer = (F(1),)
    for _ in range(exponent):
        answer = poly_multiply(answer, a)
    return answer


def derivative(a):
    return tuple(i * a[i] for i in range(1, len(a)))


def evaluate(a, t):
    answer = F(0)
    for coefficient in reversed(a):
        answer = answer * t + coefficient
    return answer


def integrate(a, mellin_integer=1):
    return sum(coefficient * F(2 ** (i + mellin_integer) - 1, i + mellin_integer)
               for i, coefficient in enumerate(a))


def integrate_log(a):
    """Exact constant and log(2) coefficients of integral_1^2 a(t)log(t)dt."""
    constant, logarithm = F(0), F(0)
    for i, coefficient in enumerate(a):
        degree = i + 1
        constant -= coefficient * F(2 ** degree - 1, degree ** 2)
        logarithm += coefficient * F(2 ** degree, degree)
    return constant, logarithm


V = poly_multiply(poly_power((F(-1), F(1)), 3),
                  poly_power((F(2), F(-1)), 3))
VP = derivative(V)
W = tuple((i + 1) * value for i, value in enumerate(V))
COMPLEX_SCALE = Q6(2, 1)


def profile(a, t):
    return evaluate(a, t) if 1 <= t <= 2 else F(0)


def run_profile_checks():
    check("exact_field", ZETA ** 2 == ZETA - ONE)
    check("exact_field", ZETA ** 6 == ONE)
    check("exact_field", ZETA * ZETA.conjugate() == ONE)
    for endpoint in (F(1), F(2)):
        for order in range(3):
            values = V
            for _ in range(order):
                values = derivative(values)
            check("profile_endpoints", evaluate(values, endpoint) == 0)
        check("profile_endpoints", evaluate(W, endpoint) == 0)
    for numerator in range(8, 17):
        t = F(numerator, 8)
        check("profile_derivative", evaluate(W, t) == evaluate(V, t) + t * evaluate(VP, t))
        check("profile_positivity", evaluate(V, t) >= 0)
    integral_v = integrate(V)
    check("mean_zero_integral", integral_v > 0)
    check("mean_zero_integral", integrate(W) == 0)
    for s in range(1, 13):
        check("mellin_factor", integrate(W, s) == (1 - s) * integrate(V, s), s)
    log_w = integrate_log(W)
    check("logarithmic_moment", log_w == (-integral_v, F(0)))
    check("logarithmic_moment", log_w[0] != 0)
    # log(C/t)=log(2)-log(t), and the log(2) integral term vanishes.
    jacobian = (-log_w[0], integrate(W) - log_w[1])
    check("prime_pair_jacobian", jacobian == (integral_v, F(0)))
    for kappa in (Q6(F(2, 3)), ZETA, ZERO):
        check("zero_principal_coefficient", kappa * COMPLEX_SCALE * integrate(W) == ZERO)
    return integral_v


NORMS = (7, 13, 19, 25)
UNIT = (0, 0, 0, 0)
D, Z, CAP = 4096, 91, 91 ** 2


@lru_cache(None)
def norm(n):
    return prod(q ** exponent for q, exponent in zip(NORMS, n))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


@lru_cache(None)
def mu(n):
    return 0 if any(exponent > 1 for exponent in n) else (-1) ** sum(n)


@lru_cache(None)
def divisors(n):
    return tuple(product(*(range(exponent + 1) for exponent in n)))


def enumerate_monoid():
    answer = []

    def visit(prefix, index, value):
        if index == len(NORMS):
            answer.append(tuple(prefix))
            return
        exponent = 0
        while value <= CAP:
            visit(prefix + [exponent], index + 1, value)
            exponent += 1
            value *= NORMS[index]

    visit([], 0, 1)
    return tuple(sorted(answer, key=lambda n: (norm(n), n)))


DOMAIN = enumerate_monoid()
PRIME_TWISTS = ((ONE, ONE, ONE, ONE),
                (ZETA, ZETA ** 2, ZETA ** 4, ZETA ** 5),
                (ONE, ZERO, ONE, ONE),
                (ZETA, ZERO, ZETA ** 3, ONE),
                (ONE, ONE, ONE, ZERO),
                (ZETA ** 3, ZETA ** 4, ZETA, ONE))


def lambda_values(prime_values):
    answer = {}
    for n in DOMAIN:
        value = ONE
        for root, exponent in zip(prime_values, n):
            value *= root ** exponent
        answer[n] = value
    return answer


TWISTS = tuple(lambda_values(values) for values in PRIME_TWISTS)


def complex_weight(n, scale=D):
    return COMPLEX_SCALE * profile(W, F(norm(n), scale))


def run_scalar_derivative_checks():
    for lam in TWISTS:
        for scale in (70, 100, 200, 1000, D):
            value_v, euler_d_v, value_w = ZERO, ZERO, ZERO
            for n in DOMAIN:
                t = F(norm(n), scale)
                v = profile(V, t)
                d_v = -t * profile(VP, t)
                w = profile(W, t)
                check("finite_scalar_derivative", w == v - d_v)
                value_v += mu(n) * lam[n] * COMPLEX_SCALE * v
                euler_d_v += mu(n) * lam[n] * COMPLEX_SCALE * d_v
                value_w += mu(n) * lam[n] * COMPLEX_SCALE * w
            check("finite_amplitude_derivative", value_w == value_v - euler_d_v)


def run_adaptive_amplitude_checks():
    m = {n: mu(n) * int(norm(n) <= Z) for n in DOMAIN}
    c = {n: sum(m[d] * m[subtract(n, d)] for d in divisors(n)) for n in DOMAIN}
    cutoffs = []
    nonzero = 0
    for row, (lam, modulus) in enumerate(zip(TWISTS, (1, 7, 13, 19, 25, 1729))):
        cutoff = F(512, modulus)  # D^(1-eta)/L at D=4096 and eta=1/4.
        cutoffs.append(str(cutoff))
        amplitude = sum((mu(n) * lam[n] * complex_weight(n) for n in DOMAIN), ZERO)
        nonzero += int(amplitude != ZERO)
        terms = {}
        for d in DOMAIN:
            free_sum = sum((lam[n] * complex_weight(add(d, n)) for n in DOMAIN
                            if norm(d) * norm(n) <= 2 * D), ZERO)
            terms[d] = -c[d] * lam[d] * free_sum
        small_keys = tuple(d for d in DOMAIN if norm(d) <= cutoff)
        small = sum((terms[d] for d in small_keys), ZERO)
        tail = sum((term for d, term in terms.items() if norm(d) > cutoff), ZERO)
        principal_sum = sum((c[d] * lam[d] / norm(d) for d in small_keys), ZERO)
        principal = -Q6(F(row + 1, 3)) * D * COMPLEX_SCALE * integrate(W) * principal_sum
        centered = small - principal
        residual = tail + principal
        check("adaptive_amplitude_identity", amplitude == sum(terms.values(), ZERO))
        check("adaptive_amplitude_identity", amplitude == small + tail)
        check("adaptive_amplitude_identity", amplitude == centered + residual)
        check("adaptive_principal_zero", principal == ZERO and centered == small)
        if cutoff < 1:
            check("adaptive_empty_cutoff", small_keys == ())
            check("adaptive_empty_cutoff", small == ZERO)
            check("adaptive_empty_cutoff", principal_sum == ZERO)
            check("adaptive_empty_cutoff", principal == ZERO)
        for n in DOMAIN:
            for d in divisors(n):
                check("adaptive_complex_multiplicativity", lam[n] == lam[d] * lam[subtract(n, d)])
    check("adaptive_nontrivial_witness", nonzero >= 2)
    check("adaptive_distinct_cutoffs", len(set(cutoffs)) == len(cutoffs))
    return cutoffs


def conductor_partition(exponents):
    conductor = tuple(int(e > 0 and e % 6 != 0) for e in exponents)
    extra_mask = tuple(int(e > 0 and e % 6 == 0) for e in exponents)
    radical = tuple(int(e > 0) for e in exponents)
    return conductor, extra_mask, radical


def run_conductor_and_radical_checks():
    for q in NORMS:
        for exponent in range(13):
            conductor = int(exponent > 0 and exponent % 6 != 0)
            extra_mask = int(exponent > 0 and exponent % 6 == 0)
            check("local_conductor_mask", conductor * extra_mask == 0)
            check("local_conductor_mask", conductor + extra_mask == int(exponent > 0))
            check("local_conductor_mask", q ** conductor * q ** extra_mask == q ** int(exponent > 0))
    for exponents in product((0, 1, 6, 7, 12), repeat=4):
        conductor, mask, radical = conductor_partition(exponents)
        q, e, ell = norm(conductor), norm(mask), norm(radical)
        check("combined_modulus", q * e == ell)
        check("combined_modulus", all(not (a and b) for a, b in zip(conductor, mask)))
        check("radical_weight", F(q, ell ** 2) <= F(1, ell))
    finite_euler = F(1)
    for q in NORMS:
        for sigma in (1, 2):
            r = F(1, q ** sigma)
            block = sum(r ** exponent / q for exponent in range(1, 6)) + r ** 6 / q ** 2
            weighted_local = 1 + block / (1 - r ** 6)
            radical_local = 1 + r / (q * (1 - r))
            check("radical_euler_local", weighted_local <= radical_local)
            check("radical_euler_local", (radical_local - 1) * (1 - r) == r / q)
            for blocks in (1, 2, 3):
                truncated = F(1)
                for exponent in range(1, 6 * blocks + 1):
                    coefficient = F(1, q ** (2 if exponent % 6 == 0 else 1))
                    truncated += coefficient * r ** exponent
                check("radical_euler_local",
                      truncated == 1 + block * (1 - r ** (6 * blocks)) / (1 - r ** 6))
                check("radical_euler_local", truncated <= weighted_local)
            if sigma == 1:
                finite_euler *= weighted_local
            # A prime in the extra deletion modulus contributes tau(E)^2=4.
            divisor_weighted_block = (sum(r ** exponent / q for exponent in range(1, 6))
                                      + 4 * r ** 6 / q ** 2)
            divisor_weighted_local = 1 + divisor_weighted_block / (1 - r ** 6)
            divisor_radical_majorant = 1 + 4 * r / (q * (1 - r))
            check("radical_euler_divisor_weight", divisor_weighted_local <= divisor_radical_majorant)
            check("radical_euler_divisor_weight", weighted_local <= divisor_weighted_local)
            for blocks in (1, 2, 3):
                truncated = F(1)
                for exponent in range(1, 6 * blocks + 1):
                    coefficient = F(4, q ** 2) if exponent % 6 == 0 else F(1, q)
                    truncated += coefficient * r ** exponent
                check("radical_euler_divisor_weight",
                      truncated == 1 + divisor_weighted_block * (1 - r ** (6 * blocks)) / (1 - r ** 6))
                check("radical_euler_divisor_weight", truncated <= divisor_weighted_local)
    return str(finite_euler)


def ceiling(value):
    return -((-value.numerator) // value.denominator)


def run_rational_checks():
    coherent = []
    for h in (F(4, 5), F(8, 9), F(2, 3)):
        eta = (1 - h) / 4
        for ell in (F(0), h / 6, h / 2, h):
            y = 1 - eta - ell
            check("adaptive_cutoff_exponents", y > 0)
            check("adaptive_cutoff_exponents", ell + y - 1 == -eta)
            check("adaptive_cutoff_exponents", 1 - y == ell + eta)
            for q_exponent in (F(0), ell / 2, ell):
                check("adaptive_weight_exponents", q_exponent - 2 * ell <= -ell)
                for requested in (0, 1, 10, 100):
                    epsilon = eta / 2
                    order = max(0, ceiling((requested + 1 - 2 * eta + epsilon) / (2 * eta)))
                    exponent = 2 * (y + q_exponent / 2 + order * (ell + y - 1)) - 1
                    prefactor = 1 - 2 * eta - 2 * order * eta
                    check("adaptive_energy_exponents", exponent == prefactor + q_exponent - 2 * ell)
                    check("adaptive_energy_exponents", prefactor + epsilon <= -requested)
        coherent.append({"h": str(h), "eta": str(eta),
                         "prime_sixth_row_radical_exponent": str(h / 6),
                         "product_cutoff_exponent": str(1 - h / 6 - eta),
                         "free_factor_upper_exponent": str(h / 6 + eta),
                         "each_mobius_factor_lower_exponent": str(F(1, 2) - h / 6 - eta)})
        floor = 1 + h / 6
        boundary = F(3, 4) + h / 6
        check("generic_bilinear_gap", floor - boundary == F(1, 4))
        for x in (F(1, 3), F(1, 2), F(2, 3), h, F(1)):
            terms = (1 + h - x, 1 + h / 6,
                     1 + 5 * h / 6 - 2 * x / 3,
                     1 + h / 3 - x / 6)
            check("generic_bilinear_gap", max(terms) >= floor)
            if x >= h:
                check("generic_bilinear_gap", max(terms) == floor)
        if h == F(4, 5):
            x = F(2, 3)
            check("balanced_bilinear_witness",
                  max(1 + h - x, floor, 1 + 5 * h / 6 - 2 * x / 3,
                      1 + h / 3 - x / 6) == F(11, 9))
            check("balanced_bilinear_witness", floor == F(17, 15))
            check("balanced_bilinear_witness", boundary == F(53, 60))
    expected = {F(4, 5): (F(13, 15), F(2, 15), F(11, 30)),
                F(8, 9): (F(23, 27), F(4, 27), F(19, 54))}
    for h, values in expected.items():
        check("coherent_length_exponents", values == (1 - h / 6, h / 6, F(1, 2) - h / 6))
    return coherent


def main():
    integral_v = run_profile_checks()
    run_scalar_derivative_checks()
    cutoffs = run_adaptive_amplitude_checks()
    radical_euler = run_conductor_and_radical_checks()
    coherent = run_rational_checks()
    record = {
        "status": "ok", "checks": sum(COUNTS.values()),
        "groups": dict(sorted(COUNTS.items())),
        "model": "GPT-6 (Codex); inherited effort not exposed",
        "finite_scope": {
            "profile": "V=(t-1)^3(2-t)^3 on [1,2]; W=V+t*V'",
            "profile_caveat": "Finite polynomial calculus diagnostic, not a C-infinity analytic profile.",
            "arithmetic": "Free ideal-style monoid, formal Q(zeta_6) twists including zeros.",
            "prime_norm_labels": list(NORMS), "monoid_norm_cap": CAP,
            "monoid_size": len(DOMAIN),
        },
        "exact_witnesses": {
            "integral_V": str(integral_v), "integral_W": "0",
            "integral_W_log_t": str(-integral_v),
            "integral_W_log_2_over_t": str(integral_v),
            "row_adaptive_cutoffs": cutoffs,
            "finite_radical_weight_euler_product_sigma1": radical_euler,
        },
        "rational_budgets": {
            "adaptive_cutoff": "Y_u=D^(1-eta)/L_u",
            "adaptive_energy": "D^(1-2*eta-2*A*eta) times sum Phi*Q_u/L_u^2",
            "generic_bilinear_exponents": ["1+h-x", "1+h/6", "1+5*h/6-2*x/3", "1+h/3-x/6"],
            "gap_above_improvement_boundary": "1/4",
            "coherent_lengths": coherent,
        },
        "limitations": [
            "No infinite Euler convergence or analytic conductor formula is verified.",
            "No PNT asymptotic, Poisson formula, moment theorem, or zero-free conclusion is verified.",
        ],
    }
    print(json.dumps(record, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
