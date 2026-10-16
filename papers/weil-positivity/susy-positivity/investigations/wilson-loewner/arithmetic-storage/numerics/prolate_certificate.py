#!/usr/bin/env python3
"""Certified cutoff-cosine gap and finite-rank polynomial resolvent.

Prepared for Edward Baker, 2026-09-29, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.

Only python-flint/Arb interval operations decide certificate inequalities.
The approximation is the cosine Taylor kernel in normalized even Legendre
polynomials on (0,1). No sampled eigenvalues or empirical tail estimates.
See projection_findings.md for the infinite-dimensional error proof.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform

import flint
from flint import arb, arb_mat, ctx, fmpq


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def rational(value):
    q = Fraction(value)
    return arb(fmpq(q.numerator, q.denominator))


def identity(n):
    return arb_mat([[int(i == j) for j in range(n)] for i in range(n)])


def show(value):
    return value.str(40)


def pack(value):
    """Exact dyadic midpoint and outward radius, suitable for replay."""
    result = [[str(m), int(e)]
              for m, e in (value.mid().man_exp(), value.rad().man_exp())]
    copy = arb((int(result[0][0]), result[0][1]),
               (int(result[1][0]), result[1][1]))
    require(copy.contains(value), "Dyadic export failed containment")
    return result


def frobenius(matrix):
    return sum((matrix[i, j].abs_upper() * matrix[i, j].abs_upper()
                for i in range(matrix.nrows())
                for j in range(matrix.ncols())), arb(0)).sqrt()


def ldl_positive(matrix):
    """Unpivoted interval LDL: success certifies positive definiteness."""
    n = matrix.nrows()
    lower = [[arb(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        pivot = matrix[i, i] - sum(
            (lower[i][k] * lower[i][k] * pivots[k] for k in range(i)), arb(0))
        require(pivot > 0, f"Positive-definiteness certificate failed at {i}: {pivot}")
        pivots.append(pivot)
        for j in range(i + 1, n):
            numerator = matrix[j, i] - sum(
                (lower[j][k] * lower[i][k] * pivots[k]
                 for k in range(i)), arb(0))
            lower[j][i] = numerator / pivot
    return pivots


def legendre_monomial_moment(k, j):
    """Integral_0^1 P_(2k)(x) x^(2j) dx, exactly rational."""
    if k > j:
        return Fraction(0)
    return Fraction(math.factorial(2*j) * 2**(2*k) * math.factorial(j+k),
                    math.factorial(j-k) * math.factorial(2*j+2*k+1))


def build_model(rank=24):
    require(rank >= 4, "Taylor geometric tail requires rank >= 4")
    two_pi = 2 * arb.pi()
    coefficients = [2 * (-1)**j * two_pi**(2*j) / math.factorial(2*j)
                    for j in range(rank)]
    overlaps = [[arb(4*k+1).sqrt() * rational(legendre_monomial_moment(k, j))
                 for j in range(rank)] for k in range(rank)]
    values = [[arb(0) for _ in range(rank)] for _ in range(rank)]
    for k in range(rank):
        for ell in range(k, rank):
            value = sum((coefficients[j] * overlaps[k][j] * overlaps[ell][j]
                         for j in range(max(k, ell), rank)), arb(0))
            values[k][ell] = value
            values[ell][k] = value
    matrix = arb_mat(values)
    # Independent monomial-kernel trace checks verify the basis conversion.
    direct_trace = sum((coefficients[j]/(4*j+1) for j in range(rank)), arb(0))
    direct_square_trace = sum((coefficients[j]*coefficients[k]/(2*j+2*k+1)**2
                               for j in range(rank) for k in range(rank)), arb(0))
    require((matrix.trace()-direct_trace).contains(0), "Trace normalization check failed")
    require(((matrix*matrix).trace()-direct_square_trace).contains(0),
            "Squared trace normalization check failed")
    ratio = two_pi**2 / ((2*rank+1)*(2*rank+2))
    require(ratio < 1, "Taylor tail ratio not certified below 1")
    first = 2 * two_pi**(2*rank) / (math.factorial(2*rank)*(4*rank+1))
    tail = first / (1-ratio)
    perturbation = tail * (2+tail)
    return matrix, tail, perturbation, ratio


def certify(rank=24, precision_bits=256, gap="57/1000000"):
    ctx.prec = precision_bits
    gap_q = Fraction(gap)
    gap_ball = rational(gap_q)
    require(gap_ball > 0 and gap_ball < 1, "Gap must be strictly between 0 and 1")
    matrix, tail, perturbation, ratio = build_model(rank)
    ident = identity(rank)
    finite_a = ident - matrix*matrix
    # The finite block has gap gamma+delta, and the complement is identity.
    pivots = ldl_positive(finite_a - ident*(gap_ball+perturbation))
    require(gap_ball+perturbation < 1, "Complement gap condition failed")
    inverse_ball = finite_a.inv()
    # A fixed exactly dyadic self-adjoint approximation defines a genuine
    # operator, unlike an interval family. Symmetrize before taking midpoint.
    inverse_mid = ((inverse_ball + inverse_ball.transpose())/2).mid()
    require(inverse_mid == inverse_mid.transpose(), "Midpoint inverse is not symmetric")
    finite_residual = ident - finite_a*inverse_mid
    finite_residual_bound = frobenius(finite_residual)
    # ||I + E(R-I)E*|| <= max(1, ||R||_F).
    inverse_norm_bound = frobenius(inverse_mid)
    require(inverse_norm_bound > 1, "Use max(1, Frobenius) in this parameter regime")
    residual_bound = finite_residual_bound + perturbation*inverse_norm_bound
    require(residual_bound < 1, "Full operator residual is not below 1")
    inverse_error_bound = residual_bound/gap_ball
    # Nuclear column decomposition M=sum_j (M e_j)e_j*, sharper here than
    # sqrt(rank)*||M||_F and requiring no spectral approximation.
    cosine_trace_bound = sum((sum((matrix[i,j].abs_upper()*matrix[i,j].abs_upper()
                                   for i in range(rank)), arb(0)).sqrt()
                              for j in range(rank)), arb(0))+tail
    smoothed_resolvent_trace_error = (cosine_trace_bound*inverse_error_bound
                                      + tail*inverse_norm_bound)
    # No trial eigenvector or approximate top eigenvalue enters the proof.
    # The lower bound for the gap is all that is claimed.
    packed_mid = [[pack(inverse_mid[i,j]) for j in range(rank)] for i in range(rank)]
    digest = hashlib.sha256(json.dumps(packed_mid, separators=(",", ":")).encode()).hexdigest()
    scalars = {
        "cosine_operator_error_bound": tail,
        "squared_operator_error_bound": perturbation,
        "tail_geometric_ratio": ratio,
        "inverse_norm_upper_bound": 1/gap_ball,
        "finite_inverse_residual_bound": finite_residual_bound,
        "polynomial_resolvent_norm_bound": inverse_norm_bound,
        "full_inverse_residual_bound": residual_bound,
        "inverse_approximation_error_bound": inverse_error_bound,
        "cosine_trace_norm_bound": cosine_trace_bound,
        "smoothed_resolvent_trace_norm_error": smoothed_resolvent_trace_error,
    }
    simple_caps = {}
    if rank == 32 and gap_q == Fraction(57, 1000000):
        simple_caps = {
            "cosine_operator_error_bound": "1.5e-40",
            "inverse_norm_upper_bound": "17544",
            "inverse_approximation_error_bound": "9.2e-32",
            "cosine_trace_norm_bound": "2.858",
            "smoothed_resolvent_trace_norm_error": "2.7e-31",
        }
        for key, cap in simple_caps.items():
            require(scalars[key] < rational(cap), f"Simple cap failed: {key}")
    record = {
        "status": "CERTIFIED",
        "claim": "I-C^2 >= gamma I on L2(0,1); finite-rank polynomial resolvent error enclosed",
        "operator": "C(x,y)=2*cos(2*pi*x*y), 0<x,y<1",
        "rank": rank,
        "max_polynomial_degree": 2*rank-2,
        "precision_bits": precision_bits,
        "gamma_exact": str(gap_q),
        "runtime": {"python": platform.python_version(), "python_flint": flint.__version__,
                    "flint": flint.__FLINT_VERSION__},
        "bounds": {name: {"display": show(value), "ball": pack(value)}
                   for name, value in scalars.items()},
        "strict_rational_caps": simple_caps,
        "positive_ldl_pivots": [{"display": show(p), "ball": pack(p)} for p in pivots],
        "dyadic_inverse_sha256": digest,
        "scope": ["No evaluated Sonin projection or trace is claimed.",
                  "All positivity and inequality checks use outward Arb balls.",
                  "Kernel Taylor tail covers the full infinite-dimensional complement.",
                  "Rebuild using this script; certificate is not based on sampled eigenvalues."],
    }
    return record, matrix, inverse_mid


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rank", type=int, default=32)
    parser.add_argument("--precision-bits", type=int, default=256)
    parser.add_argument("--gap", default="57/1000000")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "records" / "prolate_certificate_rank32.json")
    args = parser.parse_args()
    record, _, _ = certify(args.rank, args.precision_bits, args.gap)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": record["status"], "gamma_exact": record["gamma_exact"],
                      "rank": record["rank"],
                      "bounds": {k: v["display"] for k,v in record["bounds"].items()},
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
