#!/usr/bin/env python3
"""Exact finite algebra checks for a joint index/source-current experiment.

15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded coordinating model: gpt-6-astra; reasoning effort: ultra.

Only Python's standard library is required. All arithmetic is rational.
These checks do not establish convergence, a theta sign, or an RH implication.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path
import random


COUNTS = Counter()


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    COUNTS[name] += 1


class Poly:
    """Sparse Q[u,q,z]; z is formal and may later be specialized to i*omega."""

    def __init__(self, terms=0):
        if isinstance(terms, Poly):
            terms = terms.terms
        if not isinstance(terms, dict):
            terms = {(0, 0, 0): Q(terms)}
        self.terms = {p: Q(c) for p, c in terms.items() if c}

    def __add__(self, other):
        other = Poly(other)
        terms = dict(self.terms)
        for p, c in other.terms.items():
            terms[p] = terms.get(p, 0) + c
        return Poly(terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly({p: -c for p, c in self.terms.items()})

    def __sub__(self, other):
        return self + -Poly(other)

    def __rsub__(self, other):
        return Poly(other) + -self

    def __mul__(self, other):
        other = Poly(other)
        terms = {}
        for a, ac in self.terms.items():
            for b, bc in other.terms.items():
                p = tuple(x + y for x, y in zip(a, b))
                terms[p] = terms.get(p, 0) + ac * bc
        return Poly(terms)

    __rmul__ = __mul__

    def __pow__(self, degree):
        if not isinstance(degree, int) or degree < 0:
            raise ValueError("polynomial powers must be nonnegative integers")
        result = Poly(1)
        for _ in range(degree):
            result = result * self
        return result

    def __eq__(self, other):
        return self.terms == Poly(other).terms

    def __bool__(self):
        return bool(self.terms)

    def diff(self, variable=0):
        terms = {}
        for powers, coefficient in self.terms.items():
            exponent = powers[variable]
            if exponent:
                p = list(powers)
                p[variable] -= 1
                terms[tuple(p)] = exponent * coefficient
        return Poly(terms)

    def at_u(self, value):
        terms = {}
        for (a, b, c), coefficient in self.terms.items():
            powers = (0, b, c)
            terms[powers] = terms.get(powers, 0) + coefficient * value**a
        return Poly(terms)

    def integrate_u(self, upper):
        terms = {}
        for (a, b, c), coefficient in self.terms.items():
            powers = (0, b, c)
            terms[powers] = (terms.get(powers, 0)
                            + coefficient * upper**(a + 1) / (a + 1))
        return Poly(terms)


U = Poly({(1, 0, 0): 1})
QQ = Poly({(0, 1, 0): 1})
Z = Poly({(0, 0, 1): 1})
ZERO = Poly()


def clean(values):
    return {n: Poly(value) for n, value in values.items() if n >= 1 and value}


def array_add(first, second, scale=Q(1)):
    return clean({n: first.get(n, ZERO) + scale * second.get(n, ZERO)
                  for n in first.keys() | second.keys()})


def step(values):
    """Killed averaging, retaining every positive destination index."""
    result = {}
    for source, value in values.items():
        for destination in (source - 1, source + 1):
            if destination >= 1:
                result[destination] = result.get(destination, ZERO) + Q(1, 2) * value
    return clean(result)


def laplacian(values):
    """Independent coordinate formula; zero is reset, no upper cutoff."""
    return clean({n: values.get(n - 1, ZERO) - 2 * values.get(n, ZERO)
                  + values.get(n + 1, ZERO)
                  for n in range(1, max(values, default=0) + 2)})


def derivative(values):
    return clean({n: value.diff() for n, value in values.items()})


def current(values, depth):
    moving = values
    result = {}
    for _ in range(depth):
        result = array_add(result, moving, -Q(1, 2))
        moving = step(moving)
    return result, moving


def random_u_poly(rng, degree):
    return Poly({(a, 0, 0): Q(rng.randint(-9, 9), rng.randint(1, 7))
                 for a in range(degree + 1)})


def rectangle_checks(rng):
    for size in range(1, 9):
        for degree in range(6):
            upper = Q(size + degree + 1, degree + 2)
            j = [random_u_poly(rng, degree) for _ in range(size + 2)]
            k = [random_u_poly(rng, degree + 1) for _ in range(size + 1)]
            rho = [random_u_poly(rng, degree) for _ in range(size + 1)]
            source = {n: j[n - 1] - 2*j[n] + j[n + 1] + k[n].diff() + rho[n]
                      for n in range(1, size + 1)}
            lhs = sum((source[n].integrate_u(upper) for n in source), ZERO)
            lower_index = (j[0] - j[1]).integrate_u(upper)
            upper_index = (j[size + 1] - j[size]).integrate_u(upper)
            lower_source = -sum((k[n].at_u(0) for n in source), ZERO)
            upper_source = sum((k[n].at_u(upper) for n in source), ZERO)
            residual = sum((rho[n].integrate_u(upper) for n in source), ZERO)
            check("finite_rectangle_all_four_boundaries",
                  lhs == lower_index + upper_index + lower_source + upper_source + residual)
            weighted_lhs = sum((n*source[n].integrate_u(upper) for n in source), ZERO)
            weighted_index = (j[0] - (size+1)*j[size] + size*j[size+1]).integrate_u(upper)
            weighted_source = sum((n*(k[n].at_u(upper) - k[n].at_u(0)) for n in source), ZERO)
            weighted_residual = sum((n*rho[n].integrate_u(upper) for n in source), ZERO)
            check("finite_rectangle_first_moment_boundaries",
                  weighted_lhs == weighted_index + weighted_source + weighted_residual)
    # A sentinel has four nonzero boundary contributions: omission of any one fails.
    upper = Q(3, 2)
    j = [Poly(1), Poly(3), Poly(5), Poly(9)]
    k = [ZERO, U+2, 2*U+3]
    pieces = [(j[0]-j[1]).integrate_u(upper),
              (j[3]-j[2]).integrate_u(upper),
              -sum((k[n].at_u(0) for n in (1, 2)), ZERO),
              sum((k[n].at_u(upper) for n in (1, 2)), ZERO)]
    for piece in pieces:
        check("rectangle_boundary_sentinel_nonzero", bool(piece))
    lhs = sum(((j[n-1]-2*j[n]+j[n+1]+k[n].diff()).integrate_u(upper)
               for n in (1, 2)), ZERO)
    check("rectangle_boundary_sentinel_identity", lhs == sum(pieces, ZERO))
    for piece in pieces:
        check("rectangle_missing_boundary_detected", lhs != sum(pieces, ZERO)-piece)


def killed_current_checks(rng):
    for support in range(1, 9):
        for degree in range(5):
            f = clean({n: random_u_poly(rng, degree) for n in range(1, support+1)})
            k = clean({n: random_u_poly(rng, degree+1) for n in range(1, support+1)})
            g = array_add(f, derivative(k), -1)
            for depth in range(1, 10):
                j, rho = current(g, depth)
                check("killed_current_exact_laplacian", laplacian(j) == array_add(g, rho, -1))
                check("killed_current_zero_coordinate", 0 not in j and 0 not in rho)
                check("killed_current_no_unrecorded_upper_cutoff",
                      max(rho, default=0) <= support+depth and max(j, default=0) <= support+depth-1)
                dj, drho = current(derivative(g), depth)
                check("current_commutes_with_source_derivative", derivative(j) == dj)
                check("iterate_commutes_with_source_derivative", derivative(rho) == drho)
                check("joint_current_exact_interior",
                      array_add(array_add(laplacian(j), derivative(k)), rho) == f)
                # An arbitrary finite rectangle may cut through nonzero upper flux.
                m = 1 + (support+depth) // 2
                upper = Q(5, 3)
                lhs = sum((f.get(n, ZERO).integrate_u(upper) for n in range(1, m+1)), ZERO)
                flux = (-j.get(1, ZERO)+j.get(m+1, ZERO)-j.get(m, ZERO)).integrate_u(upper)
                flux += sum((k.get(n, ZERO).at_u(upper)-k.get(n, ZERO).at_u(0)
                             +rho.get(n, ZERO).integrate_u(upper) for n in range(1, m+1)), ZERO)
                check("joint_current_finite_rectangle", lhs == flux)
    # A point source verifies that the rightmost site is retained at each step.
    moving = {3: Poly(1)}
    for depth in range(1, 13):
        moving = step(moving)
        check("rightmost_surviving_path_retained", moving[3+depth] == Q(1, 2**depth))
        check("absorbed_zero_is_never_averaged_back", 0 not in moving)


def source_reduction_checks():
    for t in (Q(-3, 2), Q(-1, 7), Q(0), Q(2, 5), Q(3)):
        d = 2*t*U + Z
        for lam in (Q(1, 3), Q(1), Q(7, 2), Q(11)):
            def operator(p):
                return p.diff() + 4*QQ*p.diff(1) + (1+d-4*lam*QQ)*p
            for degree in range(7):
                g = U**degree
                primitive = -Q(1, 2)*lam*g*QQ + Q(1, 8)*((1-d)*g-g.diff())
                target = (2*lam**2*QQ**2 - 3*lam*QQ)*g
                residual = Q(1, 8)*(g.diff().diff()+2*d*g.diff()+(d**2+2*t-1)*g)
                difference = target-operator(primitive)
                check("source_reduction_formal_frequency_identity", difference == residual)
                check("source_reduction_no_q_in_residual",
                      all(powers[1] == 0 for powers in difference.terms))
                endpoint = -Q(1, 2)*lam*g.at_u(0) + Q(1, 8)*((1-Z)*g.at_u(0)-g.diff().at_u(0))
                # Physical u=0 also imposes q=1; z remains formal.
                substituted = Poly({(a, 0, c): sum(
                    value for (aa, _b, cc), value in primitive.at_u(0).terms.items()
                    if aa == a and cc == c)
                    for a, _b, c in primitive.at_u(0).terms})
                check("source_primitive_lower_endpoint", substituted == endpoint)
    # Linearity tests a mixed g with all degrees present, beyond single monomials.
    t, lam = Q(2, 7), Q(5, 3)
    d = 2*t*U+Z
    g = sum((Q((-1)**j, j+1)*U**j for j in range(7)), ZERO)
    p = -Q(1, 2)*lam*g*QQ + Q(1, 8)*((1-d)*g-g.diff())
    lp = p.diff()+4*QQ*p.diff(1)+(1+d-4*lam*QQ)*p
    check("source_reduction_mixed_polynomial",
          (2*lam**2*QQ**2-3*lam*QQ)*g-lp
          == Q(1, 8)*(g.diff().diff()+2*d*g.diff()+(d**2+2*t-1)*g))


def physical_lower_edge_checks():
    # Taylor polynomials suffice only for these exact zeroth/first jet tests.
    # The rational p(0) values below are NOT true exponential theta values.
    weights = (Q(1, 4), Q(1, 8), Q(1, 8))
    cutoff = (Q(1, 2), Q(3, 4), Q(0))
    lambdas = (Q(1), Q(4), Q(9))
    weighted_beta = sum((b*d for b, d in zip(weights, cutoff)), Q(0))
    check("surrogate_primitive_normalization", sum(weights) == Q(1, 2))
    for t in (Q(-1, 2), Q(0), Q(3, 2)):
        heat = 1+t*U**2+Q(1, 2)*t**2*U**4
        for x, delta in ((Q(0), Q(1, 2)), (Q(2, 3), Q(1, 7))):
            def c0(frequency):
                return sum((Q((-1)**k, factorial(2*k))*frequency**(2*k)*U**(2*k)
                            for k in range(5)), ZERO)
            def c1(frequency):
                return sum((Q((-1)**(k+1), factorial(2*k+1))*frequency**(2*k+1)*U**(2*k+2)
                            for k in range(4)), ZERO)
            starting = (c0(x), c1(x), -U**2*c0(x))
            endpoint = (c0(x+delta), c1(x+delta))
            for jet in (0, 1):
                delta_j0 = Q(int(jet == 0))
                cancelling_a = 2*delta_j0*weighted_beta
                for a in (Q(-2, 3), Q(0), Q(1), cancelling_a):
                    lower = ZERO
                    for beta, d, lam in zip(weights, cutoff, lambdas):
                        f = heat*(d*endpoint[jet]-a*starting[0]
                                  -Q(2, 5)*starting[1]-Q(3, 7)*starting[jet+1])
                        check("physical_kernel_lower_value", f.at_u(0) == delta_j0*d-a)
                        check("physical_kernel_lower_derivative_evenness", f.diff().at_u(0) == 0)
                        p0 = beta/(4*lam-1)
                        pprime0 = (1-4*lam)*p0
                        k0 = Q(1, 8)*(pprime0*f.at_u(0)-p0*f.diff().at_u(0))
                        check("primitive_complete_lower_edge_formula",
                              -k0 == Q(1, 8)*(beta*f.at_u(0)+p0*f.diff().at_u(0)))
                        lower -= k0
                    check("physical_lower_edge_same_cutoff_weights",
                          lower == Q(1, 8)*(delta_j0*weighted_beta-a/2))
                    if a == cancelling_a:
                        check("physical_lower_edge_correction_cancels", lower == 0)
    deficit = Q(1, 2)-weighted_beta
    check("physical_lower_edge_cutoff_deficit_positive", deficit > 0)
    check("physical_lower_edge_full_anchor_leaves_deficit",
          Q(1, 8)*(weighted_beta-Q(1, 2)) == -deficit/8)


def is_psd_2x2(a, b, d):
    return a >= 0 and d >= 0 and a*d-b*b >= 0


def signed_quotient_checks():
    # W=z_1. The symmetric observation matrix is [[B,A/2],[A/2,0]].
    # Known rational square roots make the exact optimal threshold rational.
    for b, a, norm in ((3, 4, 5), (-3, 4, 5), (5, 12, 13), (-5, 12, 13),
                       (0, 2, 2), (2, 0, 2), (-2, 0, 2), (0, 0, 0)):
        b, a, norm = Q(b), Q(a), Q(norm)
        check("signed_threshold_known_norm", norm*norm == a*a+b*b)
        optimum = (b+norm)/2
        check("signed_threshold_optimum_psd", is_psd_2x2(optimum-b, -a/2, optimum))
        for offset in (Q(-1), Q(-1, 100), Q(0), Q(1, 100), Q(2)):
            c = optimum+offset
            psd = is_psd_2x2(c-b, -a/2, c)
            criterion = c >= 0 and b <= c and a*a <= 4*c*(c-b)
            check("signed_threshold_sylvester_equivalence", psd == criterion)
            check("signed_threshold_exact_optimality", psd == (c >= optimum))
    # J(tau)=diag(tau^2,tau^4), ell=(tau,-tau^2), W=(Jc)_2.
    # u and q now serve as formal coefficients c_0 and c_1.
    c0, c1 = U, QQ
    for tau in [Q(0), Q(3, 2), Q(-3, 2)] + [sign*Q(1, 2**k) for k in range(10) for sign in (-1, 1)]:
        h, w = tau**2*c0, tau**4*c1
        ell = tau*c0-tau**2*c1
        certificate = (Q(1, 2)*tau**2*c0-tau**3*c1)**2 + Q(1, 4)*tau**8*c1**2
        check("degenerating_analytic_example_square_completion",
              Q(1, 4)*(h*h+w*w)-w*ell == certificate)
        if tau:
            a, b, c = 1/tau, -1/tau**2, Q(1, 4)
            check("degenerating_example_exact_descent", tau**2*a == tau and tau**4*b == -tau**2)
            check("degenerating_example_uniform_signed_psd", is_psd_2x2(c, -a/2, c-b))
            check("degenerating_example_determinant", c*(c-b)-a*a/4 == Q(1, 16))
            check("degenerating_example_absolute_norm_formula", a*a+b*b == 1/tau**2+1/tau**4)
        else:
            check("degenerating_example_zero_fiber_descent", h == 0 and w == 0 and ell == 0)
    previous = Q(0)
    for k in range(12):
        tau = Q(1, 2**k)
        norm_squared = 1/tau**2+1/tau**4
        check("degenerating_example_absolute_norm_lower_bound", norm_squared >= 16**k)
        check("degenerating_example_absolute_norm_increases", norm_squared > previous)
        previous = norm_squared


def run():
    COUNTS.clear()
    rng = random.Random(20261015)
    rectangle_checks(rng)
    killed_current_checks(rng)
    source_reduction_checks()
    physical_lower_edge_checks()
    signed_quotient_checks()
    return {
        "status": "passed",
        "research_date": "2026-10-15",
        "author": "Prepared for Edward Baker with substantial LLM assistance",
        "model": "gpt-6-astra",
        "reasoning_effort": "ultra",
        "arithmetic": "fractions.Fraction; sparse rational polynomial identities; no floating point",
        "total_assertions": sum(COUNTS.values()),
        "assertion_groups": dict(sorted(COUNTS.items())),
        "scope": [
            "Finite rectangular sum/integration identities, retaining both index and source boundaries.",
            "Finite-depth killed-current identities and differentiation commutation on polynomial arrays.",
            "Symbolic source reduction in Q[u,q,z], with z formal and hence permitting z=i*omega.",
            "Rational lambda values are algebraic stand-ins, not actual pi*n^2 theta parameters.",
            "Physical kernel lower jets and primitive boundary bookkeeping with rational surrogate normalization.",
            "Exact signed-quadratic thresholds and a degenerating analytic matrix example.",
            "Finite algebra only: no certification of infinite limits, theta positivity, collision exclusion, or RH."
        ],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional JSON receipt path")
    arguments = parser.parse_args()
    result = run()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
