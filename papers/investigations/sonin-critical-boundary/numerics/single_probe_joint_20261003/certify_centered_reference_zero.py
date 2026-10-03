#!/usr/bin/env python3
"""Outward bracket for the unique centered-reference sign change.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and effort are not exposed.
This is a scalar certificate, not arithmetic/Weil positivity.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import platform

import flint
from flint import arb, acb, ctx


def ab(x):
    x = Fraction(x)
    return arb(x.numerator) / x.denominator


def pack(x):
    if not x.is_finite():
        raise ArithmeticError("Nonfinite scalar enclosure")
    return {"lower": str(x.lower().fmpq()), "upper": str(x.upper().fmpq())}


def centered(t):
    return acb(ab(Fraction(5, 4)), ab(t) / 2).digamma().real - arb.pi().log()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, default=192)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.bits < 128:
        raise ValueError("At least 128-bit precision is required")
    ctx.prec = args.bits
    lo, hi = Fraction(6), Fraction(7)
    if not (centered(lo) < 0 and centered(hi) > 0):
        raise ArithmeticError("Initial sign bracket not certified")
    for _ in range(64):
        mid = (lo + hi) / 2
        value = centered(mid)
        if value < 0:
            lo = mid
        elif value > 0:
            hi = mid
        else:
            raise ArithmeticError("Unresolved bisection sign")
    vlo, vhi = centered(lo), centered(hi)
    if not (vlo < 0 and vhi > 0):
        raise ArithmeticError("Final sign bracket not certified")
    record = {
        "description": "Unique zero of Re psi(5/4+i t/2)-log(pi), for t>0",
        "scope": "Scalar sign bracket only; uniqueness is proved in the companion note",
        "date": "2026-10-03",
        "model": "GPT-6 (Codex); exact serving variant and reasoning effort not exposed",
        "bits": args.bits,
        "bisections": 64,
        "python": platform.python_version(),
        "python_flint": flint.__version__,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "t_star_lower": str(lo),
        "t_star_upper": str(hi),
        "m_at_lower": pack(vlo),
        "m_at_upper": pack(vhi),
        "m_at_zero": pack(centered(0)),
        "t_star_over_pi_lower": str((ab(lo) / arb.pi()).lower().fmpq()),
        "t_star_over_pi_upper": str((ab(hi) / arb.pi()).upper().fmpq()),
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({
        "output": str(args.output),
        "t_star_lower_decimal": str(ab(lo)),
        "t_star_upper_decimal": str(ab(hi)),
        "density_lower_decimal": str(ab(lo) / arb.pi()),
        "density_upper_decimal": str(ab(hi) / arb.pi()),
    }, indent=2))


if __name__ == "__main__":
    main()
