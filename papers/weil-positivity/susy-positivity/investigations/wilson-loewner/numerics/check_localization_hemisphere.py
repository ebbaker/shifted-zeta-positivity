#!/usr/bin/env python3
"""Independent quadrature checks for the free-hyper localization comparison.

Python standard library only. These are floating-point diagnostics, not interval
certificates and not a calculation of the 4d normal-fluctuation determinant.
See notes/PREDICTIVE_LOCALIZATION_HEMISPHERE_TEST_20260920.md.
"""

import argparse
import cmath
import hashlib
import json
import math
from pathlib import Path
import platform


def gauss_legendre(order):
    nodes, weights = [], []
    for j in range(1, order + 1):
        z = math.cos(math.pi * (j - 0.25) / (order + 0.5))
        for _ in range(40):
            p0, p1 = 1.0, z
            for k in range(2, order + 1):
                p0, p1 = p1, ((2 * k - 1) * z * p1 - (k - 1) * p0) / k
            dp = order * (z * p1 - p0) / (z * z - 1)
            dz = p1 / dp
            z -= dz
            if abs(dz) < 2e-16:
                break
        # Recompute derivative at the final node.
        p0, p1 = 1.0, z
        for k in range(2, order + 1):
            p0, p1 = p1, ((2 * k - 1) * z * p1 - (k - 1) * p0) / k
        dp = order * (z * p1 - p0) / (z * z - 1)
        nodes.append(z)
        weights.append(2 / ((1 - z * z) * dp * dp))
    return nodes, weights


def integrator(order):
    nodes, weights = gauss_legendre(order)

    def integrate(f, lo, hi, pieces=1):
        terms = []
        width = (hi - lo) / pieces
        for j in range(pieces):
            center = lo + (j + 0.5) * width
            for z, weight in zip(nodes, weights):
                terms.append(0.5 * width * weight * f(center + 0.5 * width * z))
        return complex(math.fsum(complex(t).real for t in terms),
                       math.fsum(complex(t).imag for t in terms))
    return integrate


def polynomial(x):
    return 2 * x * x - 3 * x


def eigen_polynomial(s):
    return s * (2 * s - 1)


def logcosh(x):
    return abs(x) + math.log1p(math.exp(-2 * abs(x))) - math.log(2)


def log_arithmetic(p, omega):
    return (omega * math.log(math.pi)
            + math.lgamma((p + 2.5 - omega) / 2)
            - math.lgamma((p + 2.5 + omega) / 2)
            + math.log(p - 0.5 - omega) - math.log(p - 0.5 + omega))


def green(mu, t):
    if t > 0:
        return math.exp(-mu * t) / (1 + math.exp(-2 * math.pi * mu))
    return -math.exp(-mu * t) / (1 + math.exp(2 * math.pi * mu))


def run(order):
    quad = integrator(order)

    def mellin(s, poly=lambda x: 1):
        # x = exp(v); truncation tails are tiny for this finite parameter list.
        # No interval enclosure is claimed for the quadrature or tail values.
        return quad(lambda v: cmath.exp(s * v - math.exp(v)) * poly(math.exp(v)),
                    -60, 6, 66)

    product_checks = []
    for mu in (0.2, 1.0, 3.0):
        n = 512
        partial_log = -math.fsum(math.log1p(mu * mu / (k + 0.5) ** 2)
                                for k in range(n))
        gap = partial_log + logcosh(math.pi * mu)
        a = n + 0.5
        lower = mu * mu / a - mu ** 4 / 2 * (a ** -4 + 1 / (3 * a ** 3))
        upper = mu * mu * (a ** -2 + a ** -1)
        assert lower <= gap <= upper
        product_checks.append(dict(mu=mu, pairs=n, log_tail=gap,
                                   analytic_lower_evaluated=lower,
                                   analytic_upper_evaluated=upper))

    green_errors = []
    for mu in (0.0, 0.2, 1.0):
        for n in (-3, -1, 0, 2):
            k = n + 0.5
            actual = quad(lambda t: green(mu, t) * cmath.exp(-1j * k * t),
                          0, 2 * math.pi, 4)
            green_errors.append(abs(actual - 1 / (mu + 1j * k)))
        for t in (0.1, 1.0, 3.0):
            assert abs(green(mu, t - 2 * math.pi) + green(mu, t)) < 1e-14
            assert abs(green(mu, t) * green(mu, -t)
                       + 0.25 / math.cosh(math.pi * mu) ** 2) < 1e-14

    moments = []
    for s in (0.5, 0.75, 1.0, 1.25, 2.25, 5.0):
        vacuum = mellin(s).real
        descendant = mellin(s, polynomial).real
        expected = math.gamma(s)
        expected_desc = eigen_polynomial(s) * expected
        moments.append(dict(s=s, vacuum=vacuum,
                            vacuum_relative_error=abs(vacuum / expected - 1),
                            descendant=descendant,
                            descendant_scaled_error=abs(descendant - expected_desc)
                            / max(1, abs(expected_desc))))

    reflection_errors, complex_descendant_errors = [], []
    for sigma in (0.0, 0.3, 1.2, 2.0):
        s = 0.5 - 1j * sigma
        amplitude = mellin(s)
        reflection_errors.append(abs(abs(amplitude) ** 2
                                     - math.pi / math.cosh(math.pi * sigma)))
        complex_descendant_errors.append(abs(mellin(s, polynomial)
                                            - eigen_polynomial(s) * amplitude))

    norms = []
    for name, poly, eig, exact, naive in (
        ("vacuum", lambda x: 1, lambda s: 1, 0.5, 0.5),
        ("one_bilinear_N", lambda x: x, lambda s: s, 0.25, 0.0),
        ("target_comparison_T", polynomial, eigen_polynomial, 0.75, 0.5),
    ):
        position = quad(lambda v: math.exp(v - 2 * math.exp(v))
                        * poly(math.exp(v)) ** 2, -60, 6, 66).real
        spectral = quad(lambda sigma: abs(eig(0.5 - 1j * sigma)) ** 2
                        / (2 * math.cosh(math.pi * sigma)), -18, 18, 36).real
        naive_square = quad(lambda sigma: eig(0.5 - 1j * sigma) ** 2
                            / (2 * math.cosh(math.pi * sigma)), -18, 18, 36)
        assert abs(position - exact) < 1e-12
        assert abs(spectral - exact) < 1e-12
        assert abs(naive_square - naive) < 1e-12
        norms.append(dict(state=name, position_norm_squared=position,
                          mellin_norm_squared=spectral, exact_norm_squared=exact,
                          naive_same_amplitude_square=naive_square.real,
                          naive_imaginary_part=naive_square.imag))

    transfer = []
    for p in (1.5, 2.0, 4.0, 8.0, 16.0, 64.0):
        for omega in (0.001, 0.1):
            s_minus, s_plus = (p + 0.5 - omega) / 2, (p + 0.5 + omega) / 2
            comparison_ratio = (math.pi ** omega
                                * mellin(s_minus, polynomial).real
                                / mellin(s_plus, polynomial).real)
            target = math.exp(log_arithmetic(p, omega))
            circle = math.exp(logcosh(math.pi * (p + omega))
                              - logcosh(math.pi * (p - omega)))
            single_pair = (math.pi ** omega * math.gamma(s_minus + 1)
                           / math.gamma(s_plus + 1))
            transfer.append(dict(p=p, omega=omega, arithmetic=target,
                                 hemisphere_comparison_ratio=comparison_ratio,
                                 hemisphere_relative_error=abs(comparison_ratio / target - 1),
                                 single_pair_ratio=single_pair,
                                 missing_pole_ratio=(p - 0.5 - omega) / (p - 0.5 + omega),
                                 circle_real_mass_ratio=circle))

    maxima = dict(green_fourier_absolute=max(green_errors),
                  gamma_reflection_absolute=max(reflection_errors),
                  complex_descendant_absolute=max(complex_descendant_errors),
                  real_gamma_relative=max(row["vacuum_relative_error"] for row in moments),
                  descendant_scaled=max(row["descendant_scaled_error"] for row in moments),
                  transfer_relative=max(row["hemisphere_relative_error"] for row in transfer))
    assert max(maxima.values()) < 2e-11, maxima
    return dict(quadrature_order_per_piece=order, errors=maxima,
                paired_mode_product=product_checks, real_mellin_checks=moments,
                gluing_and_adjoint_checks=norms, transfer_comparison=transfer)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = dict(schema=1, status="floating-point diagnostics; analytic arguments are in the note",
                  model="OpenAI GPT-6 (Codex; developer-provided identity)",
                  effort="not exposed in this session; not inferred",
                  python=platform.python_version(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  parameter_map_status="s=(p+1/2)/2 is a comparison convention, not a physical derivation",
                  polynomial_status="T=N(2N-1) is selected by target comparison, not predicted by an open line",
                  runs=[run(24), run(40)])
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(json.dumps({"status": "PASS", "errors_by_order":
                      {r["quadrature_order_per_piece"]: r["errors"] for r in result["runs"]}}, indent=2))


if __name__ == "__main__":
    main()
