#!/usr/bin/env python3
"""Outward certificate for one Euler-factor control's raw Laguerre witness.

Prepared for Edward Baker, 14 October 2026, with LLM assistance by
gpt-6-astra (Codex), reasoning effort ultra.

Dependency: python-flint (tested with 0.9.0). No mpmath or binary64
arithmetic enters the certificate. See the linked Note 2 for the analytic
tail bounds and the exact positive-source-variable integral identity.

Run from this directory:
    python3 -B certify_euler_factor_witness.py --output /tmp/witness.json
"""

import argparse
import hashlib
import json
import platform
from pathlib import Path

try:
    import flint
    from flint import acb, arb, ctx
except ImportError as exc:
    raise SystemExit("Install python-flint (tested version: 0.9.0) to replay.") from exc


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def exact_dyadic(value):
    """An exact integer times a power of two, with no decimal conversion."""
    mantissa, exponent = value.man_exp()
    return {"mantissa": str(mantissa), "exponent": int(exponent)}


def enclosure(value):
    require(value.is_finite(), "Non-finite real enclosure")
    return {
        "display": value.str(35, more=True),
        "lower_dyadic": exact_dyadic(value.lower()),
        "upper_dyadic": exact_dyadic(value.upper()),
    }


def certify(precision, theta_terms):
    require(precision >= 96, "At least 96 bits are required")
    require(theta_terms >= 2, "Retain at least two theta terms")
    ctx.prec = precision
    pi = arb.pi()
    a = arb(41).log() / 2
    c = arb(1) / 2
    t = arb(1) / 5
    x = arb(168413) / 100000
    upper_limit = arb(1)
    tolerance_bits = precision - 38
    tolerance = arb(2) ** (-tolerance_bits)
    m = theta_terms + 1

    # The omitted theta series is positive. Its n-index majorant is
    # geometric after n=m, and each omitted term decreases with v>=0.
    q = (arb(m + 1) / m) ** 4 * (-pi * (2 * m + 1)).exp()
    source_geometric_ratio = 16 * (-3 * pi).exp()
    require(a > 0 and c > 0 and c < 1 and t > 0, "Parameter domain")
    require(2 * pi > 3, "Positivity of every theta source summand")
    require(4 * pi * m * m > 9, "Omitted summands decrease in v")
    require(q > 0 and q < 1, "Theta-index geometric majorant")
    require(source_geometric_ratio < arb(1) / 2, "Full source majorant")
    require(16 * pi * (4 * upper_limit).exp() > 2 * t,
            "Tail logarithmic derivative decreases on [U,infinity)")
    density_error = 2 * pi * pi * m ** 4 * (-pi * m * m).exp() / (1 - q)

    def truncated_source(v):
        e4, e5, e9 = (4 * v).exp(), (5 * v).exp(), (9 * v).exp()
        return sum(
            (2 * pi * pi * n ** 4 * e9 - 3 * pi * n * n * e5)
            * (-pi * n * n * e4).exp()
            for n in range(1, theta_terms + 1)
        )

    def wave(r, derivative):
        phase = x * r
        if derivative == 0:
            trig = phase.cos()
        elif derivative == 1:
            trig = -phase.sin()
        else:
            trig = -phase.cos()
        return r ** derivative * (t * r * r).exp() * trig

    jet_records = []
    jets = []
    for derivative in range(3):
        def integrand(v, analytic):
            # Entire in the complex variable v: only polynomial, exp,
            # sin and cos operations occur here. The constant log(41)
            # was already enclosed as a real parameter. Therefore the
            # analytic flag needs no branch-cut check for this callback.
            return truncated_source(v) * (
                wave(v, derivative)
                + c / 2 * (wave(v + a, derivative) + wave(v - a, derivative))
            )

        finite = acb.integral(
            integrand, 0, upper_limit,
            rel_tol=tolerance, abs_tol=tolerance,
            eval_limit=100000, depth_limit=30,
        )
        require(finite.is_finite(), "Quadrature returned a non-finite ball")
        require(finite.imag.contains(0), "Real integral lacks zero imaginary part")

        theta_payment = (
            upper_limit * density_error * (1 + c)
            * (upper_limit + a) ** derivative
            * (t * (upper_limit + a) ** 2).exp()
        )
        decay_slope = (
            4 * pi * (4 * upper_limit).exp() - 9
            - 2 * t * (upper_limit + a)
            - arb(derivative) / (upper_limit + a)
        )
        require(decay_slope > 0, "Tail is not decreasing at U")
        infinite_tail_payment = (
            (1 + c) * 4 * pi * pi * (upper_limit + a) ** derivative
            * (9 * upper_limit + t * (upper_limit + a) ** 2
               - pi * (4 * upper_limit).exp()).exp()
            / decay_slope
        )
        payment = theta_payment + infinite_tail_payment
        require(theta_payment > 0 and infinite_tail_payment > 0,
                "Tail payments must be positive")
        # Arb's radius constructor rounds outwards. Passing the upper
        # endpoint pays for every point of the two analytic bound balls.
        full_jet = finite.real + arb(0, payment.upper())
        jets.append(full_jet)
        jet_records.append({
            "derivative": derivative,
            "finite_integral_real": enclosure(finite.real),
            "finite_integral_imaginary": enclosure(finite.imag),
            "theta_index_payment_bound": enclosure(theta_payment),
            "infinite_source_and_shift_tail_bound": enclosure(infinite_tail_payment),
            "tail_decay_slope": enclosure(decay_slope),
            "full_jet": enclosure(full_jet),
        })

    raw_l0 = jets[1] ** 2 - jets[0] * jets[2]
    require(raw_l0 < 0, "The full raw Laguerre interval is not strictly negative")
    lower_display = -arb(5299994533574706) / (arb(10) ** 21)
    upper_display = -arb(5299994533574704) / (arb(10) ** 21)
    require(raw_l0 > lower_display and raw_l0 < upper_display,
            "The full interval does not fit the stated rational display bracket")
    return {
        "schema": "euler-factor-raw-laguerre-witness-v1",
        "date": "2026-10-14",
        "provenance": {
            "prepared_for": "Edward Baker",
            "llm_assistance": "gpt-6-astra (Codex)",
            "reasoning_effort": "ultra",
        },
        "checker": {
            "file": Path(__file__).name,
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "runtime": {
            "python": platform.python_version(),
            "python_flint": flint.__version__,
        },
        "parameters": {
            "p": 41, "c": "1/2", "t": "1/5", "x": "168413/100000",
            "a": "log(41)/2", "U": "1", "retained_theta_terms": theta_terms,
            "precision_bits": precision, "quadrature_tolerance_bits": tolerance_bits,
            "quadrature_eval_limit": 100000, "quadrature_depth_limit": 30,
            "normalization": "H=integral_0^infinity Phi_control(u)*exp(t*u^2)*cos(x*u) du",
        },
        "majorants": {
            "theta_index_ratio": enclosure(q),
            "uniform_omitted_density_bound": enclosure(density_error),
            "full_source_geometric_ratio": enclosure(source_geometric_ratio),
        },
        "jets": jet_records,
        "raw_laguerre_L0": enclosure(raw_l0),
        "strict_rational_display_bracket": {
            "lower": "-5299994533574706/1000000000000000000000",
            "upper": "-5299994533574704/1000000000000000000000",
        },
        "checks": {
            "all_majorant_hypotheses": True,
            "all_integrals_finite_and_real": True,
            "theta_index_and_complete_source_shift_tails_paid": True,
            "raw_L0_upper_endpoint_negative": True,
            "rational_display_bracket_verified": True,
        },
        "conclusion": "Lambda_(c=1/2,p=41) > 1/5",
        "scope": "One raw witness; no collision identification, global equality, or RH claim.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the small execution record here")
    parser.add_argument("--precision", type=int, default=128)
    parser.add_argument("--theta-terms", type=int, default=4)
    args = parser.parse_args()
    record = certify(args.precision, args.theta_terms)
    serialized = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
