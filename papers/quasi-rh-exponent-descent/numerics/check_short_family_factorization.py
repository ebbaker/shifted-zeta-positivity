#!/usr/bin/env python3
"""Exact finite algebra and rational-budget checks for short-family notes 8--10.

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; configured effort is not exposed.

Standard library only. Prints deterministic JSON; creates or modifies no files.
The arithmetic model is a finite truncation of a free commutative ideal-style
monoid, with prime-norm labels 7, 13, 19 and 25. It is not an enumeration of all
Eisenstein ideals, and its twists are not computed sextic residue symbols.
Finite algebra and exact rational exponents do not prove Poisson summation,
uniform conductor bounds, transform decay, an asymptotic moment, or RH.
"""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, prod
import json


COUNTS = Counter()


def check(group, condition, detail=""):
    if not condition:
        raise AssertionError(f"{group}: {detail}")
    COUNTS[group] += 1


@dataclass(frozen=True)
class Q6:
    """a + b*zeta_6, exactly; zeta_6**2 = zeta_6 - 1."""

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

    def __rsub__(self, other):
        return self.cast(other) - self

    def __mul__(self, other):
        other = self.cast(other)
        return Q6(self.a * other.a - self.b * other.b,
                  self.a * other.b + self.b * other.a + self.b * other.b)

    __rmul__ = __mul__

    def conjugate(self):
        return Q6(self.a + self.b, -self.b)

    def abs2(self):
        return self.a * self.a + self.a * self.b + self.b * self.b

    def real(self):
        return self.a + self.b / 2

    def __truediv__(self, other):
        other = self.cast(other)
        denominator = other.abs2()
        if denominator == 0:
            raise ZeroDivisionError
        numerator = self * other.conjugate()
        return Q6(numerator.a / denominator, numerator.b / denominator)

    def __pow__(self, exponent):
        if exponent < 0:
            return (Q6(1) / self) ** (-exponent)
        answer, base = Q6(1), self
        while exponent:
            if exponent & 1:
                answer = answer * base
            base = base * base
            exponent //= 2
        return answer


ZERO, ONE, ZETA = Q6(), Q6(1), Q6(0, 1)
NORMS = (7, 13, 19, 25)
UNIT = (0, 0, 0, 0)
CAP = 25 ** 4


@lru_cache(None)
def norm(n):
    return prod(q ** e for q, e in zip(NORMS, n))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


def gcd_vec(a, b):
    return tuple(min(x, y) for x, y in zip(a, b))


@lru_cache(None)
def mu(n):
    return 0 if any(e > 1 for e in n) else (-1) ** sum(n)


@lru_cache(None)
def radical(n):
    return tuple(int(e > 0) for e in n)


@lru_cache(None)
def divisors(n):
    return tuple(product(*(range(e + 1) for e in n)))


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
DELTA = {n: int(n == UNIT) for n in DOMAIN}
ONES = {n: 1 for n in DOMAIN}
MOBIUS = {n: mu(n) for n in DOMAIN}


def convolve(f, g):
    return {n: sum((f[d] * g[subtract(n, d)] for d in divisors(n)), 0)
            for n in DOMAIN}


def linear_combination(terms):
    return {n: sum(coefficient * values[n] for coefficient, values in terms)
            for n in DOMAIN}


def twist_values(prime_values):
    return {n: prod_q6(value ** exponent
                      for value, exponent in zip(prime_values, n))
            for n in DOMAIN}


def prod_q6(values):
    answer = ONE
    for value in values:
        answer *= value
    return answer


def run_field_checks():
    check("exact_field", ZETA ** 2 == ZETA - ONE)
    check("exact_field", ZETA ** 6 == ONE)
    check("exact_field", ZETA.conjugate() == ONE - ZETA)
    for i in range(6):
        root = ZETA ** i
        check("exact_field", root.abs2() == 1)
        check("exact_field", root.conjugate() == ZETA ** ((-i) % 6))
    for a, b in product(range(-2, 3), repeat=2):
        value = Q6(F(a, 3), F(b, 5))
        check("exact_field", value * value.conjugate() == Q6(value.abs2()))
        if value != ZERO:
            check("exact_field", value / value == ONE)


def run_truncated_inverse_checks():
    for z in (1, 7, 13, 25, 49):
        m = {n: mu(n) * (norm(n) <= z) for n in DOMAIN}
        one_m = convolve(ONES, m)
        r = {n: DELTA[n] - one_m[n] for n in DOMAIN}
        for n in DOMAIN:
            if norm(n) <= z:
                check("inverse_support", r[n] == 0, (z, n))
        m_power, one_power, r_power = DELTA, DELTA, DELTA
        summands = []
        for j in range(1, 5):
            m_power = convolve(m_power, m)
            if j > 1:
                one_power = convolve(one_power, ONES)
            r_power = convolve(r_power, r)
            summands.append(convolve(m_power, one_power))
            polynomial = linear_combination([
                ((-1) ** (k - 1) * comb(j, k), summands[k - 1])
                for k in range(1, j + 1)])
            remainder = convolve(MOBIUS, r_power)
            for n in DOMAIN:
                check("truncated_inverse", polynomial[n] + remainder[n] == mu(n),
                      (z, j, n))
                if norm(n) <= z ** j:
                    check("endpoint_support", remainder[n] == 0, (z, j, n))
                    check("endpoint_coefficients", polynomial[n] == mu(n), (z, j, n))
                if norm(n) == z ** j:
                    check("exact_endpoints", polynomial[n] == mu(n), (z, j, n))

    p, p2 = (1, 0, 0, 0), (2, 0, 0, 0)
    m = {n: mu(n) * (norm(n) <= 7) for n in DOMAIN}
    c = convolve(m, m)
    witness = [c[UNIT], c[p], c[p2]]
    check("overlap_witness", witness == [1, -2, 1])
    check("overlap_witness", -sum(witness) == mu(p2) == 0)
    check("overlap_witness", -(witness[0] + witness[1]) != mu(p2))
    check("overlap_witness", mu(p2) == 0 and c[p2] == 1)
    return witness


PRIME_TWISTS = (
    (ONE, ONE, ONE, ONE),
    (ZETA, ZETA ** 2, ZETA ** 4, ZETA ** 5),
    (ZETA, ZERO, ZETA ** 3, ONE),
    (ONE, ZERO, ONE, ONE),
    (ZERO, ZERO, ZERO, ZERO),
)
TWISTS = tuple(twist_values(values) for values in PRIME_TWISTS)


def run_twisted_checks():
    for prime_values, lam in zip(PRIME_TWISTS, TWISTS):
        for n in DOMAIN:
            for d in divisors(n):
                check("complete_multiplicativity",
                      lam[n] == lam[d] * lam[subtract(n, d)], (prime_values, n, d))
            if any(e and value == ZERO for e, value in zip(n, prime_values)):
                check("zero_masks", lam[n] == ZERO)
        for z, j in ((13, 2), (25, 3)):
            m = {n: lam[n] * (mu(n) * (norm(n) <= z)) for n in DOMAIN}
            twisted_one = lam
            m_power = {n: Q6(DELTA[n]) for n in DOMAIN}
            one_power = m_power.copy()
            terms = []
            for k in range(1, j + 1):
                m_power = convolve(m_power, m)
                if k > 1:
                    one_power = convolve(one_power, twisted_one)
                terms.append(((-1) ** (k - 1) * comb(j, k),
                              convolve(m_power, one_power)))
            polynomial = linear_combination(terms)
            for n in DOMAIN:
                if norm(n) <= z ** j:
                    check("twisted_inverse", polynomial[n] == lam[n] * mu(n),
                          (prime_values, z, j, n))


D = 100
PROFILE_CAP = 625
PROFILE_COLUMNS = tuple(n for n in DOMAIN if D <= norm(n) <= PROFILE_CAP)
PROFILE_DIVISORS = tuple(n for n in DOMAIN if norm(n) <= PROFILE_CAP)
ROW_WEIGHTS = (F(2, 3), F(3, 5), F(5, 7), F(7, 11), F(11, 13))


def weight(n):
    """Finite complex profile samples; no smoothness or analytic claim."""
    value = norm(n)
    if not D <= value <= PROFILE_CAP:
        return ZERO
    return Q6(F(value + 3, 101), F(value % 11 - 5, 13))


def run_amplitude_checks():
    m = {n: mu(n) * (norm(n) <= 25) for n in DOMAIN}
    c = convolve(m, m)
    integral = Q6(F(2, 7), F(3, 11))
    check("principal_centering", integral != integral.conjugate())
    amplitudes = []
    principal_witness = None
    for row, lam in enumerate(TWISTS):
        amplitude = sum((mu(n) * lam[n] * weight(n) for n in PROFILE_COLUMNS), ZERO)
        free_sums = {
            d: sum((lam[n] * weight(add(d, n)) for n in DOMAIN
                    if norm(d) * norm(n) <= PROFILE_CAP), ZERO)
            for d in PROFILE_DIVISORS}
        terms = {d: -c[d] * lam[d] * free_sums[d] for d in PROFILE_DIVISORS}
        check("weighted_amplitudes", sum(terms.values(), ZERO) == amplitude, row)
        # Synthetic principal coefficients: this checks centering algebra,
        # including zero masks, not the analytic residue formula for kappa_u.
        kappa = F(2, 3) if row == 0 else (F(3, 5) if row in (3, 4) else F(0))
        for cutoff in (1, 7, 25, 49, 100, 625):
            small = sum((value for d, value in terms.items() if norm(d) <= cutoff), ZERO)
            large = sum((value for d, value in terms.items() if norm(d) > cutoff), ZERO)
            main = -kappa * D * integral * sum(
                (c[d] * lam[d] / norm(d) for d in PROFILE_DIVISORS if norm(d) <= cutoff), ZERO)
            centered, residual = small - main, large + main
            check("weighted_amplitudes", amplitude == small + large)
            check("principal_centering", amplitude == centered + residual)
            cross = 2 * (centered * residual.conjugate()).real()
            check("principal_centering",
                  amplitude.abs2() == centered.abs2() + residual.abs2() + cross)
            check("principal_centering",
                  amplitude.abs2() <= 2 * centered.abs2() + 2 * residual.abs2())
            check("principal_centering",
                  residual.abs2() <= 2 * amplitude.abs2() + 2 * centered.abs2())
            if row == 0 and cutoff == 1:
                check("principal_centering", main != main.conjugate())
                principal_witness = {"main_a": str(main.a), "main_b": str(main.b)}
        amplitudes.append(amplitude)
    energy = sum(rho * value.abs2() for rho, value in zip(ROW_WEIGHTS, amplitudes)) / D
    check("weighted_amplitudes", energy >= 0)
    return principal_witness


def run_gcd_checks():
    x = tuple({n: mu(n) * lam[n] * weight(n) for n in PROFILE_COLUMNS} for lam in TWISTS)
    b = {}
    for d in PROFILE_DIVISORS:
        b[d] = sum(rho * sum((row[n] for n in PROFILE_COLUMNS
                              if all(v <= e for v, e in zip(d, n))), ZERO).abs2()
                   for rho, row in zip(ROW_WEIGHTS, x)) / D
        check("positive_divisor_moments", b[d] >= 0)
    coprime = sum((rho * sum((row[n] * row[m].conjugate()
                             for n in PROFILE_COLUMNS for m in PROFILE_COLUMNS
                             if n != m and gcd_vec(n, m) == UNIT), ZERO)
                   for rho, row in zip(ROW_WEIGHTS, x)), ZERO) / D
    signed = sum(mu(d) * value for d, value in b.items())
    check("signed_gcd_identity", coprime == Q6(signed))
    diagonal_witness = None
    for cutoff in (1, 7, 13, 25, 49, 100, 625):
        sigma = {n: sum(mu(d) for d in divisors(n) if norm(d) <= cutoff)
                 for n in DOMAIN}
        for n in DOMAIN:
            if norm(n) <= cutoff:
                check("truncated_gcd_coefficients", sigma[n] == int(n == UNIT))
            check("truncated_gcd_coefficients", abs(sigma[n]) <= len(divisors(n)))
        truncated = sum(mu(d) * value for d, value in b.items() if norm(d) <= cutoff)
        diagonal = sum(rho * sum(row[n].abs2() * sigma[n] for n in PROFILE_COLUMNS)
                       for rho, row in zip(ROW_WEIGHTS, x)) / D
        tail = sum((rho * sum((row[n] * row[m].conjugate() * sigma[gcd_vec(n, m)]
                              for n in PROFILE_COLUMNS for m in PROFILE_COLUMNS
                              if n != m and norm(gcd_vec(n, m)) > cutoff), ZERO)
                    for rho, row in zip(ROW_WEIGHTS, x)), ZERO) / D
        check("signed_gcd_truncation", Q6(truncated) - coprime == Q6(diagonal) + tail)
        if cutoff == 1:
            check("truncated_diagonal_witness", diagonal > 0)
            diagonal_witness = str(diagonal)
        if cutoff == PROFILE_CAP:
            check("signed_gcd_truncation", diagonal == 0 and tail == ZERO)
    return diagonal_witness


def run_coherent_divisor_checks():
    witness = []
    for k in range(5):
        columns = tuple(tuple(bits) + (0,) * (4 - k)
                        for bits in product((0, 1), repeat=k))
        total = sum(mu(n) * mu(m) for n in columns for m in columns
                    if gcd_vec(n, m) == UNIT)
        prime_columns = tuple(n for n in columns if sum(n) == 1)
        prime_only = sum(mu(n) * mu(m) for n in prime_columns for m in prime_columns
                         if n != m)
        check("coherent_divisor_cancellation", total == (-1) ** k)
        check("coherent_divisor_cancellation", prime_only == k * (k - 1))
        witness.append({"k": k, "full_coprime_total": total,
                        "distinct_prime_total": prime_only})
    return witness


def run_double_convolution_checks():
    """Optional independent exact coprimality-convolution coefficient check."""
    columns = tuple(product(range(3), repeat=4))
    for n in columns:
        for m in columns:
            rhs = sum(mu(radical(d)) * mu(subtract(n, d)) * mu(subtract(m, e))
                      for d in divisors(n) for e in divisors(m)
                      if radical(d) == radical(e))
            lhs = mu(n) * mu(m) * int(gcd_vec(n, m) == UNIT)
            check("double_convolution_coefficients", rhs == lhs, (n, m))


def run_euler_deletion_checks():
    """Complete an actual coefficient deletion, with all prime exponents."""
    masks = tuple(product((0, 1), repeat=4)) + ((2, 1, 0, 0), (0, 3, 1, 0))
    for lam in TWISTS:
        for r in masks:
            allowed = lambda d: all(e == 0 or re > 0 for e, re in zip(d, r))
            for n in DOMAIN:
                rhs = sum((lam[d] * mu(subtract(n, d)) * lam[subtract(n, d)]
                           for d in divisors(n) if allowed(d)), ZERO)
                lhs = mu(n) * lam[n] * int(gcd_vec(n, r) == UNIT)
                check("euler_deletion_coefficients", rhs == lhs, (r, n))
            masked = sum((mu(n) * lam[n] * weight(n) for n in PROFILE_COLUMNS
                          if gcd_vec(n, r) == UNIT), ZERO)
            completed = sum((lam[d] * sum(
                (mu(n) * lam[n] * weight(add(d, n)) for n in DOMAIN
                 if norm(d) * norm(n) <= PROFILE_CAP), ZERO)
                for d in PROFILE_DIVISORS if allowed(d)), ZERO)
            check("euler_deletion_amplitudes", completed == masked, r)

    # This prime square lies in the sampled profile. The d=p^2 term is needed.
    p, p2 = (0, 1, 0, 0), (0, 2, 0, 0)
    lam = TWISTS[1]
    full = sum((lam[d] * mu(subtract(p2, d)) * lam[subtract(p2, d)]
                for d in divisors(p2)), ZERO)
    squarefree_only = sum((lam[d] * mu(subtract(p2, d)) * lam[subtract(p2, d)]
                           for d in divisors(p2) if mu(d) != 0), ZERO)
    check("euler_deletion_overlap_witness", norm(p2) >= D and norm(p2) <= PROFILE_CAP)
    check("euler_deletion_overlap_witness", full == ZERO)
    check("euler_deletion_overlap_witness", squarefree_only != full)
    check("euler_deletion_overlap_witness", lam[p2] == lam[p] ** 2 != ZERO)


def run_local_divisor_mean_checks():
    """F_beta^2=1*g_beta at beta=1, with exact rational local factors."""
    local_g = tuple(F(q, q - 1) ** 2 - 1 for q in NORMS)
    g = {n: F(0) if any(e > 1 for e in n)
         else F(prod(value for value, e in zip(local_g, n) if e))
         for n in DOMAIN}
    for value in local_g:
        check("local_divisor_mean", value > 0)
    for n in DOMAIN:
        f_squared = prod(F(q, q - 1) ** 2 for q, e in zip(NORMS, n) if e)
        divisor_mean = sum(g[d] for d in divisors(n))
        check("local_divisor_mean", f_squared == divisor_mean, n)
        check("local_divisor_mean", g[n] >= 0)
        if any(e > 1 for e in n):
            check("local_divisor_mean_support", g[n] == 0)
    finite_euler_sum = sum(g[n] / norm(n) for n in DOMAIN)
    finite_euler_product = prod(1 + value / q for q, value in zip(NORMS, local_g))
    check("local_divisor_mean", finite_euler_sum == finite_euler_product)
    return str(finite_euler_sum)


def ceiling(value):
    return -((-value.numerator) // value.denominator)


def run_rational_budgets():
    hs = (F(8, 9), F(4, 5), F(2, 3), F(1, 4))
    original_table = []
    centered_table = []
    for h in hs:
        original, transformed = 1 - h / 2, F(1, 2)
        check("original_transformed_cutoffs", 2 - 2 * original == h)
        check("original_transformed_cutoffs", h + 1 - 2 * transformed == h)
        if h > F(1, 2):
            check("original_transformed_cutoffs",
                  min(h + 1 - transformed, 2 - 2 * transformed) == 1)
            check("original_transformed_cutoffs", original > transformed)
        original_table.append({"h": str(h), "original": str(original),
                               "transformed": str(transformed)})
        for loss in (F(0), F(1, 216), F(1, 24), F(1, 2)):
            cutoff_one, cutoff_two = 1 - loss, 1 - (h + loss) / 2
            for theta in (cutoff_one, cutoff_two):
                check("truncation_power_budgets",
                      min(h + 1 - theta, 2 - 2 * theta) <= h + loss)
            check("truncation_power_budgets", (cutoff_two < cutoff_one) == (loss < h))
            beta = (1 + loss) / 2 + 5 * h / 12
            check("extraction_budgets", (beta < F(7, 8)) == (loss + 5 * h / 6 < F(3, 4)))
            y_boundary = (1 + loss - h) / 2
            check("centered_A0_budgets", 2 * h + 2 * y_boundary - 1 == h + loss)
        centered_table.append({"h": str(h), "A0_lossless_y": str((1 - h) / 2)})
        for divisor in (2, 3, 5):
            eta = (1 - h) / divisor
            y = 1 - h - eta
            check("all_A_centered_energy", 0 < eta < 1 - h and y > 0)
            check("all_A_centered_energy", h + y - 1 == -eta)
            check("all_A_centered_energy", 2 * h + 2 * y - 1 == 1 - 2 * eta)
            for requested in (0, 1, 3, 10, 100):
                preliminary_epsilon = eta / 2
                order = max(0, ceiling((requested + 1 - 2 * eta + preliminary_epsilon) / (2 * eta)))
                exponent = 2 * h + 2 * y - 1 + 2 * order * (h + y - 1)
                check("all_A_centered_energy", exponent == 1 - 2 * eta - 2 * order * eta)
                check("arbitrary_power_decay", exponent + preliminary_epsilon <= -requested)
    return original_table, centered_table


def run_core_conductor_budgets():
    hs = (F(8, 9), F(4, 5), F(2, 3), F(1, 4))
    fixed_core_table = []
    for h in hs:
        generic_tail = F(5, 6) + h / 3
        improvement_boundary = F(3, 4) + h / 6
        gap = F(1, 12) + h / 6
        check("generic_core_tail_gap", generic_tail - improvement_boundary == gap)
        check("generic_core_tail_gap", gap > 0)
        for loss in (F(0), F(1, 216), F(1, 24), F(1, 2)):
            if loss + 5 * h / 6 < F(3, 4):
                check("generic_core_tail_gap", generic_tail - (h + loss) > gap)
        for beta in (F(1, 2), F(2, 3), F(7, 8)):
            for kappa in (F(0), F(1, 8), F(1)):
                for delta in (F(0), h / 2, h):
                    exponent = 2 * beta - 1 + h / 6 + delta * (2 * kappa + F(5, 6))
                    substitution = (2 * beta - 1) + h * F(1, 6) + delta * (2 * kappa + F(5, 6))
                    check("uniform_core_conductor_budget", exponent == substitution)
                    check("uniform_core_conductor_budget", 0 <= delta <= h)
                    for loss in (F(0), F(1, 24)):
                        check("uniform_core_conductor_budget",
                              (exponent <= h + loss) ==
                              (delta * (2 * kappa + F(5, 6)) <= 1 - 2 * beta + 5 * h / 6 + loss))
        fixed = 2 * F(7, 8) - 1 + h / 6
        check("fixed_core_threshold", fixed == F(3, 4) + h / 6)
        inherited_loss = fixed - h
        check("fixed_core_threshold", inherited_loss + 5 * h / 6 == F(3, 4))
        check("fixed_core_threshold", (1 + inherited_loss) / 2 + 5 * h / 12 == F(7, 8))
        fixed_core_table.append({"h": str(h), "fixed_core_exponent": str(fixed),
                                 "inherited_loss": str(inherited_loss),
                                 "generic_tail_gap": str(gap)})
    return fixed_core_table


def main():
    run_field_checks()
    overlap = run_truncated_inverse_checks()
    run_twisted_checks()
    principal = run_amplitude_checks()
    diagonal = run_gcd_checks()
    coherent = run_coherent_divisor_checks()
    run_double_convolution_checks()
    run_euler_deletion_checks()
    divisor_mean = run_local_divisor_mean_checks()
    original, centered = run_rational_budgets()
    fixed_core = run_core_conductor_budgets()
    record = {
        "status": "ok",
        "checks": sum(COUNTS.values()),
        "groups": dict(sorted(COUNTS.items())),
        "model": "GPT-6 (Codex); inherited effort not exposed",
        "finite_model": {
            "kind": "free ideal-style monoid; formal twists, not residue symbols",
            "prime_norm_labels": list(NORMS),
            "norm_cap": CAP,
            "coefficient_domain_size": len(DOMAIN),
            "complex_field": "Q(zeta_6), zeta_6^2=zeta_6-1",
        },
        "witnesses": {
            "nonsquarefree_overlap_coefficients": overlap,
            "synthetic_complex_principal_main_term": principal,
            "nonzero_truncated_diagonal": diagonal,
            "coherent_divisor_cancellation": coherent,
            "finite_F1_squared_euler_sum": divisor_mean,
        },
        "rational_budgets": {
            "lossless_gcd_cutoffs": original,
            "centered_A0_boundaries": centered,
            "buffered_energy_exponent": "1-2*eta-2*A*eta",
            "requested_decay_powers": [0, 1, 3, 10, 100],
            "core_uniform_exponent": "2*beta-1+h/6+delta*(2*kappa+5/6)",
            "fixed_core_thresholds": fixed_core,
        },
        "limitations": [
            "Finite convolution, masks, centering, and rational powers only.",
            "No analytic Poisson, conductor, transform-decay, or moment theorem is verified.",
            "No zero-free region or RH conclusion is certified.",
        ],
    }
    print(json.dumps(record, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
