#!/usr/bin/env python3
"""Exact finite checks for short-family divisor packets and product sectors.

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact variant/effort not exposed.

Standard library only; prints deterministic JSON and writes no files.
Most checks use a finite free ideal monoid, with distinct equal-norm primes.
The final local checks also compute actual split-prime sextic residue symbols
in Eisenstein residue fields. These do not validate reciprocity, primitive
conductors, Poisson, the prime ideal theorem, an asymptotic moment, or RH.
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
    """a+b*zeta_6, with zeta_6**2=zeta_6-1."""
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

    def __pow__(self, exponent):
        answer, base = Q6(1), self
        while exponent:
            if exponent & 1:
                answer = answer * base
            base = base * base
            exponent //= 2
        return answer

    def abs2(self):
        return self.a * self.a + self.a * self.b + self.b * self.b


ZERO, ONE, ZETA = Q6(), Q6(1), Q6(0, 1)


class Monoid:
    def __init__(self, norms):
        self.norms = tuple(norms)
        self.unit = (0,) * len(norms)

    @lru_cache(None)
    def norm(self, n):
        return prod(q ** e for q, e in zip(self.norms, n))

    @staticmethod
    def mu(n):
        return 0 if any(e > 1 for e in n) else (-1) ** sum(n)

    @staticmethod
    def add(a, b):
        return tuple(x + y for x, y in zip(a, b))

    @staticmethod
    def subtract(a, b):
        return tuple(x - y for x, y in zip(a, b))

    @staticmethod
    @lru_cache(None)
    def divisors(n):
        return tuple(product(*(range(e + 1) for e in n)))

    @lru_cache(None)
    def coefficient(self, n, z):
        return sum(self.mu(a) * self.mu(self.subtract(n, a))
                   for a in self.divisors(n)
                   if self.norm(a) <= z and self.norm(self.subtract(n, a)) <= z)

    def tail(self, n, z, above):
        return -sum(self.coefficient(d, z) for d in self.divisors(n)
                    if above(self.norm(d)))

    def twist(self, n, values):
        answer = ONE
        for value, exponent in zip(values, n):
            answer *= value ** exponent
        return answer

    def direct_tuples(self, n, z, above, values):
        answer = ZERO
        count = 0
        for a in self.divisors(n):
            if self.norm(a) > z or not self.mu(a):
                continue
            rest = self.subtract(n, a)
            for b in self.divisors(rest):
                if self.norm(b) > z or not self.mu(b):
                    continue
                if not above(self.norm(self.add(a, b))):
                    continue
                m = self.subtract(rest, b)
                answer -= (self.mu(a) * self.mu(b) * self.twist(a, values)
                           * self.twist(b, values) * self.twist(m, values))
                count += 1
        return answer, count

    def domain(self, cap):
        result = []

        def visit(prefix, index, value):
            if index == len(self.norms):
                result.append(tuple(prefix))
                return
            exponent = 0
            while value <= cap:
                visit(prefix + [exponent], index + 1, value)
                value *= self.norms[index]
                exponent += 1

        visit([], 0, 1)
        return tuple(sorted(result, key=lambda n: (self.norm(n), n)))


def run_product_checks():
    mon = Monoid((7, 7, 13, 25))
    domain = mon.domain(65536)
    twists = ((ONE,) * 4, (ZETA, ZETA ** 2, ZETA ** 4, ZETA ** 5),
              (ONE, ZERO, ZETA, ONE), (ZERO, ZERO, ZERO, ZERO))
    for z in (32, 64, 128, 256):
        for n in domain:
            size = mon.norm(n)
            if not z < size <= z * z:
                continue
            check("full_product_closure",
                  -sum(mon.coefficient(d, z) for d in mon.divisors(n)) == mon.mu(n))
            for y in (1, z, 2 * z, size, size + 1):
                above = lambda value: value > y
                tail = mon.tail(n, z, above)
                small = sum(mon.coefficient(d, z) for d in mon.divisors(n)
                            if mon.norm(d) <= y)
                check("tail_product_identity", tail == mon.mu(n) + small)
            if size <= 4096:
                for values in twists:
                    above = lambda value: value > z
                    direct, count = mon.direct_tuples(n, z, above, values)
                    grouped = mon.twist(n, values) * mon.tail(n, z, above)
                    check("twisted_tuple_recombination", direct == grouped)
    # Same norm does not identify distinct prime ideals.
    check("distinct_equal_norm_primes", mon.norm((1, 0, 0, 0)) == mon.norm((0, 1, 0, 0)))
    check("distinct_equal_norm_primes", (1, 0, 0, 0) != (0, 1, 0, 0))
    return len(domain)


def is_prime(n):
    if n < 2:
        return False
    return all(n % k for k in range(2, int(n ** 0.5) + 1))


def next_split_prime(n):
    while not (n % 3 == 1 and is_prime(n)):
        n += 1
    return n


def run_packet_checks():
    witnesses = []
    # Includes squareful b and two distinct equal-norm prime factors of b.
    for base in ((1, 0, 0), (0, 0, 1), (2, 0, 0), (1, 1, 0),
                 (1, 0, 1), (0, 0, 2), (3, 0, 0)):
        base_norms = (7, 7, 13)
        B = prod(q ** e for q, e in zip(base_norms, base))
        q = next_split_prime(B + 1)
        z = B * q
        r = next_split_prime(max(q + 1, z // 2))
        check("packet_geometry", r <= z)
        mon = Monoid(base_norms + (q, r))
        b = base + (0, 0)
        n = base + (1, 1)
        least = min(value for value, exponent in zip(base_norms, base) if exponent)
        y = (B * r + q * r) // 2
        check("packet_geometry", B * q <= z and r * least > z)
        check("packet_geometry", max(B * q, B * r) <= y < q * r)
        check("packet_geometry", z < mon.norm(n) <= z * z)
        for e in mon.divisors(b):
            d = mon.add(e, (0, 0, 0, 1, 1))
            check("packet_local_coefficient", mon.coefficient(d, z) == 2 * mon.mu(e))
        check("packet_divisor_sum", sum(mon.mu(e) for e in mon.divisors(b)) == 0)
        check("packet_zero", mon.tail(n, z, lambda value: value > y) == 0)
        for roots in ((ONE,) * 5, (ZETA, ZETA ** 2, ONE, ZETA ** 4, ZETA ** 5),
                      (ZERO, ONE, ONE, ZETA, ONE), (ONE, ONE, ZERO, ZETA, ZETA ** 3)):
            direct, count = mon.direct_tuples(n, z, lambda value: value > y, roots)
            check("packet_complex_and_masks", direct == ZERO)
            check("packet_nonempty_tuples", count >= 4)
        witnesses.append({"b_norm": B, "b_exponents": base, "q_norm": q,
                          "r_norm": r, "z": z, "y": y, "product_norm": mon.norm(n)})

    # Exact witnesses showing why the boundaries and both branches matter.
    mon = Monoid((7, 13, 61))
    n = (1, 1, 1)
    check("required_boundary", mon.tail(n, 91, lambda value: value > 610) == 0)
    check("required_boundary", mon.tail(n, 90, lambda value: value > 610) == -2)
    check("required_boundary", mon.tail(n, 91, lambda value: value > 426) == -2)
    check("required_boundary", mon.tail(n, 91, lambda value: value > 793) == 2)
    check("required_boundary", mon.tail(n, 427, lambda value: value > 610) == 2)
    check("retained_m1_branch", -mon.coefficient(n, 91) == 2)
    return witnesses


def ring_multiply(u, v):
    a, b = u
    c, d = v
    return a * c - b * d, a * d + b * c - b * d


def ring_power(u, exponent):
    answer = (1, 0)
    for _ in range(exponent):
        answer = ring_multiply(answer, u)
    return answer


def split_roots(p):
    return tuple(r for r in range(p) if (r * r + r + 1) % p == 0)


def sextic_symbol(p, root, u):
    value = (u[0] + u[1] * root) % p
    if not value:
        return ZERO
    residue = pow(value, (p - 1) // 6, p)
    for exponent in range(6):
        if pow(1 + root, exponent, p) == residue:
            return ZETA ** exponent
    raise AssertionError("sixth-root lookup failed")


def run_actual_local_checks():
    primes = (7, 13, 19, 181, 241)
    rows = tuple(product(range(-3, 4), repeat=2))
    for p in primes:
        check("actual_split_prime", is_prime(p) and p % 3 == 1)
        roots = split_roots(p)
        check("actual_split_prime", len(roots) == 2)
        for root in roots:
            check("actual_root_order", len({pow(1 + root, j, p) for j in range(6)}) == 6)
            for u in rows:
                symbol = sextic_symbol(p, root, u)
                sixth = sextic_symbol(p, root, ring_power(u, 6))
                check("actual_sixth_power_mask", sixth == (ZERO if symbol == ZERO else ONE))
                for v in ((1, 0), (0, 1), (2, -1), (p, 0)):
                    check("actual_symbol_multiplicativity",
                          sextic_symbol(p, root, ring_multiply(u, v))
                          == symbol * sextic_symbol(p, root, v))

    # Actual ideal norms, two local branches, and an exact fractional-power cutoff.
    D, L, z = 32768, 7, 256
    mon = Monoid((13, 19, 241))
    n = (1, 1, 1)
    above = lambda value: (value * L) ** 40 > D ** 39
    check("actual_packet_example", D <= mon.norm(n) <= 2 * D)
    check("actual_packet_example", not above(13 * 241) and above(19 * 241))
    check("actual_packet_example", mon.tail(n, z, above) == 0)
    for roots in product(*(split_roots(p) for p in mon.norms)):
        for u in ((1, 0), (2, -1), (-roots[0], 1)):
            values = tuple(sextic_symbol(p, root, u) for p, root in zip(mon.norms, roots))
            direct, count = mon.direct_tuples(n, z, above, values)
            check("actual_packet_complex", direct == ZERO and count == 4)
    semiprime = Monoid((181, 241))
    check("actual_semiprime_survives", D <= 181 * 241 <= 2 * D)
    check("actual_semiprime_survives", semiprime.tail((1, 1), z, above) == -2)
    check("actual_prime_square_survives", D <= 241 ** 2 <= 2 * D)
    check("actual_prime_square_survives", semiprime.tail((0, 2), z, above) == -1)
    return {"D": D, "good_radical_proxy": L, "z": z,
            "packet_prime_norms": [13, 19, 241], "packet_norm": mon.norm(n),
            "cutoff_test": "(Nd*7)^40 > 32768^39",
            "scope": "Actual local symbols; proxy cutoff is not a primitive-conductor computation."}


def run_budget_checks():
    h, theta, eta = F(2, 5), F(1, 40), F(1, 40)
    check("rational_budget", (1 + h) / 2 + 5 * h / 12 == F(13, 15))
    check("rational_budget", F(7, 8) - F(13, 15) == F(1, 120))
    check("rational_budget", 1 - theta - h == F(23, 40))
    check("rational_budget", F(1, 2) + theta == F(21, 40))
    check("rational_budget", F(1, 2) - h - 2 * theta - eta == F(1, 40))
    check("rational_budget", 1 + h / 6 - 2 * h == F(4, 15))
    check("rational_budget", 1 + h - 2 * F(3, 10) == 2 * h)
    for requested in range(1, 11):
        decay_order = 1 + 40 * (requested + 2)
        check("schwartz_tail_budget", 1 + h - eta * (decay_order - 1) < -requested)


def main():
    domain_size = run_product_checks()
    packets = run_packet_checks()
    actual = run_actual_local_checks()
    run_budget_checks()
    print(json.dumps({"status": "passed", "assertions": dict(sorted(COUNTS.items())),
                      "total_assertions": sum(COUNTS.values()),
                      "finite_monoid_domain": domain_size,
                      "packet_witnesses": packets, "actual_local_example": actual,
                      "scope": "Finite algebra, local residue symbols and rational budgets only; no asymptotic moment."},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
