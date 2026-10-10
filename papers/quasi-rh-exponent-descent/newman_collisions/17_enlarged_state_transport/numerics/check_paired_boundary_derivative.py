#!/usr/bin/env python3
"""Outward check of the first raw divisor channel's unmatched endpoint.

This certifies J_{0,P=1}'(0)>0 at t=0. It checks a boundary source,
not a complete-theta Fourier sign or a collision exclusion.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path


HASHES = {
    "check_block_current.py": "0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2",
    "check_complete_current_rectangle.py": "ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path)
    parser.add_argument("--cells", type=int, default=4096)
    parser.add_argument("--interval-source-dir", type=Path,
                        default=Path(__file__).resolve().parents[2]
                        / "13_microlocal_phase_space" / "numerics")
    args = parser.parse_args()
    if args.cells <= 0:
        raise ValueError("--cells must be positive")
    for name, digest in HASHES.items():
        if hashlib.sha256((args.interval_source_dir / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError("Retained interval source mismatch: " + name)
    sys.path.insert(0, str(args.interval_source_dir))
    from check_complete_current_rectangle import I, pi_interval, PRECISION

    pi = pi_interval()
    z = 2 * pi
    width = I(1) / args.cells
    integral = I(0)
    for k in range(args.cells):
        left, right = width * k, width * (k + 1)
        r = I(left.lo, right.hi)
        w = ((4 * r).exp() + (-4 * r).exp()) / 2
        # d/ds [e^(10s)(z(s)^2-6z(s)w+9)e^(-z(s)w)], z'=4z.
        polynomial = 18 * z**2 + 24 * z**2 * w**2 - 4 * z**3 * w - 120 * z * w + 90
        integral += 2 * width * pi**2 * r**2 * polynomial * (-z * w).exp()

    # For r=1+y, cosh(4r)<=e^(4r), cosh(4r)>=e^(4r)/2,
    # and e^(4r)>=e^4(1+4y). Every polynomial term is bounded by C*w^2.
    C = 42 * z**2 + 4 * z**3 + 120 * z + 90
    b = 4 * pi * I(4).exp() - 8
    if b.lo <= 0:
        raise ArithmeticError("Invalid tail denominator")
    tail = 2 * pi**2 * C * (8 - pi * I(4).exp()).exp() * (1 / b + 2 / b**2 + 2 / b**3)
    complete = integral + I(tail.hi.copy_negate(), tail.hi)
    if complete.lo <= 0:
        raise ArithmeticError("Endpoint derivative did not separate from zero")
    record = {
        "status": "PASS",
        "date": "2026-10-10",
        "prepared_for": "Edward Baker",
        "model": "GPT-6 (Codex)",
        "reasoning_effort": "Not exposed in this session; not inferred",
        "acknowledgment": "Substantial LLM assistance; internal outward replay, not independent validation.",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "imported_sources": HASHES,
        "arithmetic": str(PRECISION) + "-digit outward Decimal; complete cell ranges and analytic tail",
        "time": "0",
        "product_channel": 1,
        "source_derivative": "J_{0,P=1}'(0)",
        "cells_on_0_to_1": args.cells,
        "finite_integral": integral.strings(),
        "absolute_tail_upper": str(tail.hi),
        "complete_derivative": complete.strings(),
        "leading_2Re_boundary_coefficient": (-complete / 2).strings(),
        "boundary_asymptotic": "2Re i integral_0^a exp(-2xy) J_{0,1}(iy)dy = -J_{0,1}'(0)/(2x^2)+O_a(x^-4)",
        "scope": "The raw P=1 channel has a nonzero unmatched endpoint. Complete Jacobi gluing cancels all endpoint terms only after summing the channels. No complete Fourier sign or RH conclusion.",
    }
    if args.record:
        args.record.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: record[key] for key in
                     ("status", "complete_derivative", "absolute_tail_upper", "cells_on_0_to_1")}, indent=2))


if __name__ == "__main__":
    main()
