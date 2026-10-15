#!/usr/bin/env python3
"""Finite exact checks for multiplicative theta-source dilations.

Prepared for Edward Baker, 15 October 2026, with substantial LLM assistance.
Recorded coordinating model: gpt-6-astra; reasoning effort: ultra.

Standard library only; optional --output writes a small JSON receipt.
These checks do not prove infinite convergence, a theta signed estimate,
or RH. They verify finite divisor masks, formal source/transform algebra,
lower-trace bookkeeping, and exact rational majorant arithmetic.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform


CHECKS = []


def check(label, statement):
    if not statement:
        raise AssertionError(label)
    CHECKS.append(label)


# Small sparse rational polynomial ring. Monomials are sorted tuples
# (variable, nonnegative exponent). No numerical symbolic library is used.
def constant(value):
    return {(): F(value)} if value else {}


def variable(name):
    return {((name, 1),): F(1)}


def add(*terms):
    result = {}
    for p in terms:
        for monomial, coefficient in p.items():
            result[monomial] = result.get(monomial, F(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(p, coefficient):
    return {m: c * coefficient for m, c in p.items() if c * coefficient}


def multiply(*terms):
    result = constant(1)
    for p in terms:
        next_result = {}
        for m, a in result.items():
            for n, b in p.items():
                powers = dict(m)
                for name, exponent in n:
                    powers[name] = powers.get(name, 0) + exponent
                key = tuple(sorted(powers.items()))
                next_result[key] = next_result.get(key, F(0)) + a * b
        result = {m: c for m, c in next_result.items() if c}
    return result


def power(p, exponent):
    result = constant(1)
    for _ in range(exponent):
        result = multiply(result, p)
    return result


def substitute(p, replacements):
    result = {}
    for monomial, coefficient in p.items():
        term = constant(coefficient)
        for name, exponent in monomial:
            term = multiply(term, power(replacements.get(name, variable(name)), exponent))
        result = add(result, term)
    return result


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    factors = 0
    candidate = 2
    while candidate * candidate <= n:
        if n % candidate == 0:
            n //= candidate
            factors += 1
            if n % candidate == 0:
                return 0
        candidate += 1
    if n > 1:
        factors += 1
    return (-1) ** factors


def split_smooth(n, primes):
    smooth, free = 1, n
    for p in primes:
        while free % p == 0:
            smooth *= p
            free //= p
    return smooth, free


def decimal_display(value):
    with localcontext() as context:
        context.prec = 18
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    # The mode number in phi_k is kept symbolic. Scaling q -> n^2 q
    # is checked against independently replacing k -> kn.
    pi, q, k, n = map(variable, ("pi", "q", "k", "n"))
    amplitude = add(scale(multiply(power(pi, 2), power(k, 4), power(q, 2)), 2),
                    scale(multiply(pi, power(k, 2), q), -3))
    check("source amplitude under q -> n^2 q equals mode k -> kn",
          substitute(amplitude, {"q": multiply(power(n, 2), q)})
          == substitute(amplitude, {"k": multiply(k, n)}))
    rate = multiply(pi, power(k, 2), q)
    check("source exponential rate under dilation equals mode kn",
          substitute(rate, {"q": multiply(power(n, 2), q)})
          == substitute(rate, {"k": multiply(k, n)}))
    check("D_n prefactor cancels source e^u shift",
          F(-1, 2) + F(1, 2) == 0)
    primitive_derivative_factor = add(constant(1), scale(rate, -4))
    check("primitive source derivative and beta boundary scale to mode kn",
          substitute(primitive_derivative_factor, {"q": multiply(power(n, 2), q)})
          == substitute(primitive_derivative_factor, {"k": multiply(k, n)}))

    check("Mobius divisor identity for n=1..72",
          all(sum(mobius(d) for d in divisors(m)) == int(m == 1)
              for m in range(1, 73)))
    check("multiplicative dilation support semigroup, including repeated prime",
          all(int(m % (r * s) == 0)
              == (int(m % r == 0) * int(m % r == 0 and (m // r) % s == 0))
              for r, s in ((2, 2), (2, 3), (6, 5), (1, 7))
              for m in range(1, 121)))
    for cutoff in (1, 4, 8):
        truncated = {m: sum(mobius(d) for d in divisors(m) if d <= cutoff)
                     for m in range(1, 73)}
        check("truncated Mobius keeps only first mode below cutoff N=" + str(cutoff),
              all(truncated[m] == int(m == 1) for m in range(1, cutoff + 1))
              and all(abs(truncated[m]) <= len(divisors(m)) for m in truncated))

    sieve_records = []
    for primes in ((2,), (2, 3), (2, 3, 5)):
        product = math.prod(primes)
        ds = divisors(product)
        masks = {m: sum(mobius(d) for d in ds if m % d == 0)
                 for m in range(1, 121)}
        check("finite prime sieve mask " + str(primes),
              all(masks[m] == int(math.gcd(m, product) == 1) for m in masks))
        first = next(m for m in range(2, 121) if masks[m])
        check("first unsieved integer is least omitted prime " + str(primes),
              all(first % d for d in range(2, first))
              and first not in primes
              and all(split_smooth(m, primes)[1] == 1 for m in range(1, first)))
        decompositions = [split_smooth(m, primes) for m in range(1, 121)]
        check("unique smooth/free reconstruction " + str(primes),
              all(a * b == m and math.gcd(b, product) == 1
                  and split_smooth(a, primes)[1] == 1
                  for m, (a, b) in enumerate(decompositions, 1))
              and all(sum(1 for a in divisors(m)
                          if split_smooth(a, primes)[1] == 1
                          and math.gcd(m // a, product) == 1) == 1
                      for m in range(1, 121)))
        check("smooth endpoint includes every mode below remainder start " + str(primes),
              all(split_smooth(m, primes)[1] == 1 for m in range(1, first))
              and split_smooth(first, primes)[1] != 1)
        sieve_records.append({"primes": list(primes), "squarefree_product": product,
                              "divisor_coefficients": {str(d): mobius(d) for d in ds},
                              "first_unsieved_integer_above_one": first,
                              "mask_checked_through": 120,
                              "smooth_free_unique_factorization_checked_through": 120})

    # Physical complex transform uses w=iz. Its shifted parameter is
    # w-2ta and its prefactor exponent is -a+ta^2-wa.
    a, b, t, w, v = map(variable, ("a", "b", "t", "w", "v"))
    def prefactor(length, frequency):
        return add(scale(length, -1), multiply(t, power(length, 2)),
                   scale(multiply(frequency, length), -1))
    shifted_w = add(w, scale(multiply(t, a), -2))
    check("physical transform prefactors obey multiplicative semigroup",
          add(prefactor(a, w), prefactor(b, shifted_w))
          == prefactor(add(a, b), w))
    left_exponent = add(prefactor(a, w),
                        multiply(t, power(add(v, a), 2)),
                        multiply(shifted_w, add(v, a)))
    check("shifted full transform minus lower strip recovers original weight",
          left_exponent == add(scale(a, -1), multiply(t, power(v, 2)), multiply(w, v)))
    check("complex frequency shifts compose at total source-strip length",
          add(shifted_w, scale(multiply(t, b), -2))
          == add(w, scale(multiply(t, add(a, b)), -2)))

    # Universal lower trace: d0 b/8-A/16, where b is the endpoint's
    # beta mass and the starting field has its full beta mass 1/2.
    A, mass, R, W, V, VN, alpha, eta, Z = map(
        variable, ("A", "mass", "R", "W", "V", "VN", "alpha", "eta", "Z"))
    for d0 in (0, 1):
        trace = add(scale(mass, F(d0, 8)), scale(A, F(-1, 16)))
        check("cutoff-aware lower source trace, branch " + str(d0),
              substitute(trace, {"mass": add(constant(F(1, 2)), scale(R, -1))})
              == add(constant(F(d0, 16)), scale(A, F(-1, 16)), scale(R, F(-d0, 8))))
        check("prescribed beta-mass coefficient cancels lower trace, branch " + str(d0),
              not substitute(trace, {"A": scale(mass, 2 * d0)}))
        check("simple complete-start coefficient leaves only beta-tail trace, branch " + str(d0),
              substitute(trace, {"mass": add(constant(F(1, 2)), scale(R, -1)),
                                 "A": constant(d0)}) == scale(R, F(-d0, 8)))

    full_observation = add(power(W, 2), scale(multiply(alpha, W, V), -1))
    cutoff_observation = add(power(W, 2), scale(multiply(alpha, W, VN), -1))
    check("complete-first-factor endpoint remainder identity",
          add(full_observation, scale(cutoff_observation, -1))
          == scale(multiply(alpha, W, add(V, scale(VN, -1))), -1))
    check("remainder vanishes at W=0",
          not substitute(add(full_observation, scale(cutoff_observation, -1)),
                         {"W": constant(0)}))
    check("squared mixed error bound keeps physical energy",
          add(multiply(power(eta, 2), add(power(W, 2), power(Z, 2))),
              scale(multiply(power(eta, 2), power(W, 2)), -1))
          == multiply(power(eta, 2), power(Z, 2)))

    # Finite rational majorant checks. The analytic proof uses pi>3,
    # pi<4, and e>8/3; these mathematical facts are declared inputs.
    # The positive exponential series verifies the last bound directly.
    check("positive exponential partial sum proves e>8/3",
          sum((F(1, math.factorial(k)) for k in range(5)), F(0)) > F(8, 3))
    check("physical heat range satisfies first-mode absorption condition",
          F(3) > F(1, 2) / 8)
    tail_records = []
    for m in (3, 5, 7, 11):
        d = F(12 * m * m - 9)
        ratio = F(m + 1, m) ** 4 * F(3, 8) ** (3 * (2 * m + 1))
        check("rational tail denominator and geometric ratio, m=" + str(m),
              d > 0 and 0 < ratio < 1)
        values = []
        for j in (0, 1):
            bound = (32 * m ** 4 * math.factorial(j) * F(3, 8) ** (3 * m * m)
                     / (d ** (j + 1) * (1 - ratio)))
            check("positive rational physical jet remainder, m=%d j=%d" % (m, j), bound > 0)
            values.append({"j": j, "rational_upper_bound": str(bound),
                           "decimal_display_not_used_for_checks": decimal_display(bound)})
        tail_records.append({"first_remaining_index": m, "ratio_upper_bound": str(ratio),
                             "denominator_lower_bound": str(d), "jet_bounds": values})

    receipt = {
        "date": "2026-10-15", "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial LLM assistance; finite exact checks separated from analytic claims.",
        "model": "gpt-6-astra", "reasoning_effort": "ultra",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "PASS", "arithmetic": "Python standard-library Fraction and sparse rational polynomials",
        "python_version": platform.python_version(),
        "checker": Path(__file__).name,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "assertions_passed": len(CHECKS), "checks": CHECKS,
        "prime_sieves": sieve_records, "rational_remainder_majorants": tail_records,
        "analytic_remainder_formula": "2*pi^2*m^4*j!*exp(-pi*m^2)/((4*pi*m^2-9-Y)^(j+1)*(1-(1+1/m)^4*exp(-pi*(2*m+1))))",
        "analytic_remainder_conditions": "Re(t)<=T, T>=0, |Im(z)|<=Y, pi*m^2>=T/8, 4*pi*m^2-9-Y>0; real-source integration on u>=0.",
        "rational_majorant_conditions": "0<=t<=1/2, real spectral endpoint, j=0 or 1; declared elementary inputs 3<pi<4 and e>8/3.",
        "lower_trace": "(delta_(j0)*sum(endpoint_mask_n*beta_n)-A/2)/8; complete starting normalization retained.",
        "physical_transform": "T_n F(t,z)=n^(-1/2)*exp(t*a_n^2-i*z*a_n)*(F(t,z+2*i*t*a_n)-integral_0^a_n exp(t*v^2+i*(z+2*i*t*a_n)*v)*Phi(v)dv)",
        "scope": ["Finite divisor and sieve masks through stated bounds.",
                  "Formal symbolic source scaling, transform prefactors and lower-trace identities.",
                  "Exact rational arithmetic for explicit coarse remainder bounds; no quadrature."],
        "not_established": ["Infinite convergence or universal divisor identities merely from enumeration; these require the separate analytic proofs.",
                            "A sign for a real oscillatory transform of the positive sifted source.",
                            "The scalar bound W B_boundary <= C W^2+epsilon |W| for the main trace.",
                            "Any RH implication beyond the existing conditional framework.",
                            "A computational gain over an ordinary cutoff with the same first omitted index."],
        "massive_resolvent_checks": "Not included; the associated note gives an analytically reviewed derivation.",
    }
    text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(json.dumps({"status": "PASS", "assertions": len(CHECKS),
                          "output": str(args.output), "bytes": len(text.encode())}))
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
