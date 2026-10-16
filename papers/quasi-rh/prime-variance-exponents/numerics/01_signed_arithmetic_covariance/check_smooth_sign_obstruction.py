#!/usr/bin/env python3
"""Exact finite checks for the smooth-cofactor sign obstruction.

Standard library only. Cutoffs include rational endpoints and the actual
algebraic U=X**(11/24), compared by integer/rational powers. Formal prime
logarithms are kept as integer dictionaries. No numerical kernel signs,
prime asymptotics, or global exponent are inferred from this check.
"""

import argparse
from bisect import bisect_left
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path


LIMIT = 4096


@lru_cache(None)
def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = 1
    return out


@lru_cache(None)
def divisors(n):
    out = [1]
    for p, e in factor(n).items():
        old = out[:]
        out += [d * p**j for j in range(1, e + 1) for d in old]
    return tuple(sorted(out))


def mu(n):
    fs = factor(n)
    return 0 if any(e > 1 for e in fs.values()) else (-1) ** len(fs)


class Cutoff:
    def __init__(self, value, algebraic=False):
        self.value = Fraction(value)
        self.algebraic = algebraic
        self.power = self.value**11 if algebraic else self.value

    def above(self, n):
        return n**24 > self.power if self.algebraic else n > self.value

    def short(self, k, m):
        # k < m/U, with strict equality handled exactly.
        return k**24 * self.power < m**24 if self.algebraic else k * self.value < m

    def rough(self, m):
        # P^-(m) >= m/U is sufficient, including equality.
        p = min(factor(m))
        return m**24 <= p**24 * self.power if self.algebraic else m <= p * self.value

    def label(self):
        return f"({self.value})^(11/24)" if self.algebraic else str(self.value)


def coefficient(m, cutoff):
    return sum(mu(d) for d in divisors(m) if cutoff.above(d))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    counts = Counter()
    xs = (Fraction(20001, 2), Fraction(4000001, 4))
    cutoffs = [Cutoff(u) for u in (1, Fraction(7, 2), 7, 31,
                                  Fraction(201, 2), 127, 512)]
    cutoffs += [Cutoff(x, True) for x in xs]
    for cutoff in cutoffs:
        for m in range(2, LIMIT + 1):
            a = coefficient(m, cutoff)
            short = sum(mu(m // k) for k in divisors(m) if cutoff.short(k, m))
            assert a == short, (cutoff.label(), m, a, short)
            counts["short_cofactor_identity"] += 1
            if cutoff.above(m):
                complement = -sum(mu(d) for d in divisors(m)
                                  if not cutoff.above(d))
                assert a == complement, (cutoff.label(), m)
                counts["complement_identity"] += 1
                if cutoff.rough(m):
                    assert a == mu(m), (cutoff.label(), m)
                    counts["rough_parity_identity"] += 1

    # This boundary has P^-(m)=m/U: the strict short-cofactor cap
    # excludes k=5, so only k=1 survives.
    assert coefficient(35, Cutoff(7)) == 1
    assert [k for k in divisors(35) if Cutoff(7).short(k, 35)] == [1]
    counts["strict_endpoint_example"] += 1

    primes = [p for p in range(2, 10001) if len(factor(p)) == 1
              and factor(p).get(p) == 1]
    examples = []
    for x in xs:
        cutoff = Cutoff(x, True)
        seen = Counter()
        for m in range(2, LIMIT + 1):
            fs = factor(m)
            r = len(fs)
            if (r not in (2, 3) or not cutoff.above(m)
                    or any(e != 1 for e in fs.values())
                    or cutoff.above(max(fs)) or not cutoff.rough(m)):
                continue
            # [4X/5,5X/2] lies strictly inside [A X,2B X].
            # Check the formal product coefficient at an actual retained
            # prime p, avoiding all floating cutoff and support tests.
            j = bisect_left(primes, 4 * x / (5 * m))
            while j < len(primes) and not cutoff.above(primes[j]):
                j += 1
            if j == len(primes):
                continue
            p = primes[j]
            if not Fraction(4, 5) * x <= p * m <= Fraction(5, 2) * x:
                continue
            n = p * m
            grouped = {}
            for inner in factor(n):
                if cutoff.above(inner) and cutoff.above(n // inner):
                    a = coefficient(n // inner, cutoff)
                    if a:
                        grouped[inner] = a
            assert grouped == {p: (-1) ** r}, (x, m, p, grouped)
            counts["unique_large_prime_grouped_coefficient"] += 1
            seen[r] += 1
            if seen[r] <= 2:
                examples.append({"X": str(x), "U": cutoff.label(),
                                 "m": m, "outer_prime_factors": list(fs),
                                 "inner_prime": p, "product": n,
                                 "A_U(m)": (-1) ** r,
                                 "formal_grouped_coefficient": grouped})
        assert seen[2] and seen[3], (x, seen)

    result = {
        "date": "2026-10-04",
        "status": "EXACT_FINITE_ARITHMETIC_CHECKS_PASSED",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limit": LIMIT,
        "cutoffs": [c.label() for c in cutoffs],
        "checks": dict(counts),
        "total_asserted_comparisons": sum(counts.values()),
        "examples": examples,
        "limitations": [
            "The all-real-X counting lower bounds are analytic PNT arguments, not numerical results.",
            "Kernel signs follow from exact moment identities in the note; no floating kernel signs are certified here.",
            "No fixed global exponent or finite-range asymptotic onset is inferred."
        ],
    }
    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
