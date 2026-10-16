#!/usr/bin/env python3
"""Checks supporting response_claude_20260914.md (Python 3 and NumPy).

Exact checks are identified separately from floating-point diagnostics.
The cosine normalization and shift integral helper are reused from the prior
Codex check; the image and special-function implementations below are new.
No interval arithmetic, full residual Gram, or positivity certificate is
computed. JSON is printed to stdout; manuscript files are never edited.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import numpy as np
from check_review_20260913 import cosine_data, shift_matrix


def exact_checks():
    image_cases = 0
    for r in (F(1, 10), F(1, 2), F(9, 10)):
        assert 1 - r > 0 and 1 + r > 0
        for count in (1, 2, 5, 10):
            assert 1 / (1 - r*r) - sum(r**(2*m) for m in range(count)) == r**(2*count) / (1 - r*r)
            image_cases += 1
    x = F(1, 4)
    coefficient = 4 * (x*x/2 - x/2 + F(1, 12))
    assert coefficient == -F(1, 24)
    # W=[[2,1],[1,2]]: its eigenvalues are 1 and 3, whereas S=3/2.
    schur = F(2) - F(1, 2)
    assert schur not in (F(1), F(3))
    # A=0, H=I_2, B=(0,1), Y=0. Retaining only residual row 0 gives
    # the false proposed lower matrix 0, while the exact Schur matrix is -1.
    partial_lower, exact_schur = F(0), -F(1)
    assert partial_lower > exact_schur
    # Ordered positive matrices can have a gap much larger than lambda_min(S).
    epsilon = F(1, 10**6)
    assert min(epsilon, F(1)) > 0 and F(1) > min(epsilon, F(2))
    return {
        "method": "exact Fraction arithmetic",
        "geometric_image_cases": image_cases,
        "digamma_tau_minus_two_coefficient": str(coefficient),
        "schur_congruence_does_not_preserve_eigenvalues": True,
        "partial_residual_gram_need_not_give_lower_bound": True,
        "gap_below_smallest_eigenvalue_is_not_necessary": True,
    }


def density(t):
    return np.exp(-t / 2) / (-np.expm1(-2 * t))


def image_group(length, m, x, y):
    return (density(x+y+2*m*length) + density((2*m+2)*length-x-y)
            + density((2*m+2)*length+x-y) + density((2*m+2)*length-x+y))


def image_diagnostics():
    largest_error, largest_ratio, min_psd = 0.0, 0.0, 0.0
    cases = 0
    for length in (0.2, 1.0, 3.0):
        grid = length * np.linspace(0.03, 0.97, 16)
        x, y = grid[:, None], grid[None, :]
        images = sum(image_group(length, m, x, y) for m in range(400))
        masses = np.zeros_like(images)
        for k in range(2000):
            a = 2*k + 0.5
            u, v, r = np.exp(-a*grid), np.exp(-a*(length-grid)), np.exp(-a*length)
            masses += (np.outer(u, u) + np.outer(v, v)
                       + r*(np.outer(u, v) + np.outer(v, u))) / (1-r*r)
        largest_error = max(largest_error, float(np.max(np.abs(images-masses))))
        for count in (1, 2, 5, 12):
            # Directly sum the positive tail; avoid cancellation against K_L.
            tail = sum(image_group(length, m, x, y) for m in range(count, count+400))
            bound = (2*(1+np.exp(-length/2))*np.exp(-count*length)
                     / ((-np.expm1(-length))*(-np.expm1(-4*count*length))))
            ratio = float(np.max(tail) / bound)
            assert 0 < ratio < 1
            largest_ratio = max(largest_ratio, ratio)
            normalized = tail / np.max(tail)
            smallest = float(np.linalg.eigvalsh(normalized)[0])
            min_psd = min(min_psd, smallest)
            assert smallest > -2e-12
            cases += 1
    assert largest_error < 2e-11
    return {
        "method": "floating-point kernel samples; proofs are in derivations Section 5",
        "cases": cases,
        "maximum_mass_vs_image_error": largest_error,
        "maximum_sampled_tail_to_uniform_bound_ratio": largest_ratio,
        "minimum_normalized_sampled_tail_eigenvalue": min_psd,
    }


BERNOULLI = (F(1, 6), -F(1, 30), F(1, 42), -F(1, 30),
             F(5, 66), -F(691, 2730), F(7, 6), -F(3617, 510))


def psi_and_derivative(z):
    """Recurrence plus asymptotics, used only for floating-point diagnostics."""
    z = np.asarray(z, dtype=complex)
    shifted = z + 32
    psi = np.log(shifted) - 1/(2*shifted)
    derivative = 1/shifted + 1/(2*shifted**2)
    for k, bernoulli in enumerate(BERNOULLI, 1):
        psi -= float(bernoulli)/(2*k*shifted**(2*k))
        derivative += float(bernoulli)/shifted**(2*k+1)
    for j in range(32):
        psi -= 1/(z+j)
        derivative += 1/(z+j)**2
    return psi, derivative


def arithmetic_compression(count):
    """L=1, all gamma masses via digamma; 80 exponential correction terms."""
    length = 1.0
    omega, nu = cosine_data(length, count)
    psi, derivative = psi_and_derivative(0.25 + 0.5j*omega)
    psi_quarter = -np.euler_gamma - np.pi/2 - 3*np.log(2)
    assert abs(psi[0].real-psi_quarter) < 1e-13
    b = psi.real - psi_quarter
    csum = np.empty(count)
    csum[0] = derivative[0].real/4
    csum[1:] = psi[1:].imag/(2*omega[1:])
    diagonal = np.empty(count)
    diagonal[0] = csum[0]
    diagonal[1:] = psi[1:].imag/(4*omega[1:]) + derivative[1:].real/8
    s = omega**2
    denominator = s[:, None]-s[None, :]
    rational = np.zeros((count, count))
    np.divide((s*csum)[:, None]-(s*csum)[None, :], denominator,
              out=rational, where=denominator != 0)
    np.fill_diagonal(rational, diagonal)
    a = 2*np.arange(80, dtype=float)+0.5
    columns = a[:, None]/(a[:, None]**2+s)
    exp_correction = columns.T @ (np.exp(-a)[:, None]*columns)
    parity = (-1.0)**np.arange(count)
    boundary = 2*nu[:, None]*nu[None, :]*(rational-exp_correction*parity[None, :])
    boundary[parity[:, None] != parity[None, :]] = 0
    jpos = 0.5*(parity*np.exp(0.5)-1)/(0.25+s)
    jneg = -0.5*(parity*np.exp(-0.5)-1)/(0.25+s)
    c = nu/2*(np.exp(-0.25)*jpos+np.exp(0.25)*jneg)
    odd = nu/2*(np.exp(-0.25)*jpos-np.exp(0.25)*jneg)
    shift = shift_matrix(length, count, np.log(2))
    matrix = (np.diag(b+psi_quarter-np.log(np.pi)) + boundary
              + 2*np.outer(c, c)-2*np.outer(odd, odd)
              - np.log(2)/np.sqrt(2)*(shift+shift.T))
    assert np.max(np.abs(matrix-matrix.T)) < 2e-13
    return (matrix+matrix.T)/2


def finite_response_diagnostics():
    results = {}
    for count in (40, 80, 200):
        w = arithmetic_compression(count)
        a, b, h = w[:4, :4], w[4:, :4], w[4:, 4:]
        assert np.linalg.eigvalsh(h)[0] > 1/16
        upper = a-b.T @ np.linalg.solve(h, b)
        results[str(count)] = {
            "upper_response_eigenvalues": np.linalg.eigvalsh(upper).tolist(),
            "compression_smallest_eigenvalue": float(np.linalg.eigvalsh(w)[0]),
        }
    reference = json.loads((Path(__file__).parent / "check_claude_20260914/chk4.json").read_text())
    errors = [float(np.max(np.abs(np.array(results[str(count)]["upper_response_eigenvalues"])
                                 - np.array(reference[f"L1_K{count}_U_eigs"], dtype=float))))
              for count in (40, 80)]
    assert max(errors) < 5e-12
    return {
        "method": "double precision, independent digamma implementation; reused cosine/shift helper",
        "length": 1, "low_dimension": 4,
        "galerkin": results,
        "maximum_difference_from_recorded_50_digit_values": max(errors),
        "full_residual_gram_evaluated": False,
        "rigorous_interval_or_positivity_certificate": False,
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    result = {
        "source_sha256": {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                          for name in ("manuscript.tex", "derivations.tex")},
        "exact_checks": exact_checks(),
        "image_diagnostics": image_diagnostics(),
        "finite_response_diagnostics": finite_response_diagnostics(),
        "status": "all checks passed",
        "scope": "Supporting checks only; no formal proof, RH verification, or arithmetic positivity certificate.",
    }
    print(json.dumps(result, indent=2))
