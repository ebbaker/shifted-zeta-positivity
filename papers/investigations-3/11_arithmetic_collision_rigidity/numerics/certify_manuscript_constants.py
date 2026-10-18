#!/usr/bin/env python3
"""Exact-rational enclosures for the manuscript's displayed constants.

Prepared for Edward Baker, 18 October 2026.
LLM assistance: OpenAI gpt-6-astra, reasoning effort max.
Uses only the Python standard library. No floating-point input is used.
This verifies constants, not the manuscript's analytic proofs.
"""
from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import platform

BITS = 256
GRID = 1 << BITS


def floor_grid(x):
    return F((x.numerator * GRID) // x.denominator, GRID)


def ceil_grid(x):
    return -floor_grid(-x)


@dataclass(frozen=True)
class I:
    lo: F
    hi: F = None

    def __post_init__(self):
        lo, hi = F(self.lo), F(self.lo if self.hi is None else self.hi)
        assert lo <= hi
        object.__setattr__(self, "lo", floor_grid(lo))
        object.__setattr__(self, "hi", ceil_grid(hi))

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        b = I.cast(other)
        return I(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-I.cast(other))

    def __rsub__(self, other):
        return I.cast(other) - self

    def __mul__(self, other):
        b = I.cast(other)
        vals = [x * y for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def reciprocal(self):
        assert self.lo > 0 or self.hi < 0, "division interval contains zero"
        return I(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        return self * I.cast(other).reciprocal()

    def __rtruediv__(self, other):
        return I.cast(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        value, base = I(1), self
        while n:
            if n & 1:
                value = value * base
            base = base * base
            n //= 2
        return value


def atan_reciprocal(q):
    # The final included term (j=40) is positive.
    upper = sum((F((-1) ** j, (2*j + 1) * q ** (2*j + 1))
                 for j in range(41)), F(0))
    return I(upper - F(1, 83 * q ** 83), upper)


def exp_positive(x):
    x = I.cast(x)
    assert x.lo >= 0
    k = 0
    while x.hi / (2 ** k) > F(1, 8):
        k += 1
    lo, hi = x.lo / (2 ** k), x.hi / (2 ** k)
    def partial(z):
        return sum((z ** j / factorial(j) for j in range(33)), F(0))
    upper_tail = hi ** 33 / factorial(33) / (1 - hi / 34)
    result = I(partial(lo), partial(hi) + upper_tail)
    for _ in range(k):
        result = result * result
    return result


def exp_negative(x):
    return exp_positive(x).reciprocal()


def max_interval(a, b):
    return I(max(a.lo, b.lo), max(a.hi, b.hi))


def decimal_bound(x, direction):
    with localcontext() as ctx:
        ctx.prec = 36
        ctx.rounding = direction
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def serialize(x):
    return {
        "lower_rational": str(x.lo),
        "upper_rational": str(x.hi),
        "lower_decimal": decimal_bound(x.lo, ROUND_FLOOR),
        "upper_decimal": decimal_bound(x.hi, ROUND_CEILING),
    }


def compute():
    pi = 16 * atan_reciprocal(5) - 4 * atan_reciprocal(239)
    assert pi.lo > 3 and pi.hi < F(22, 7)
    kappa = F(7, 8) * (32 * pi ** 2 - 12 * pi) * exp_negative(4 * pi)
    assert kappa.lo > 0
    values = {"pi": pi, "kappa": kappa}
    per_m = {}
    for m in (2, 3, 5):
        def ratio(k):
            return I(F(m + 1, m)) ** k * exp_negative(pi * (2*m + 1))
        r4, r6 = ratio(4), ratio(6)
        assert r4.hi < 1 and r6.hi < 1
        S = 2 * pi ** 2 * m ** 4 * exp_negative(pi * m*m) / (1 - r4)
        Q = 8 * pi ** 3 * m ** 6 * exp_negative(pi * m*m) / (1 - r6)
        eps = [S * factorial(j) / (4 * pi * m*m - 9) ** (j+1)
               for j in range(3)]
        rho = (4096 * eps[0] + 2 * Q) / kappa
        eta1 = max_interval(8192 * eps[1], Q / 8 + 2 * S) / kappa
        eta2 = max_interval(8192 * eps[2],
                            3 * Q / 512 + S / 8 + 4 * eps[0]) / kappa
        per_m[m] = dict(S=S, Q=Q, rho=rho, eta1=eta1, eta2=eta2,
                        eps0=eps[0], eps1=eps[1], eps2=eps[2])
    B1, B2 = per_m[2]["eta1"], per_m[2]["eta2"]
    values.update(B1=B1, B2=B2, curvature=B2 + B1 ** 2)
    for m, d in per_m.items():
        d["remainder_first"] = d["eta1"] + B1 * d["rho"]
        d["remainder_second"] = (d["eta2"] + 2 * B1 * d["eta1"] +
                                  (2 * B1 ** 2 + B2) * d["rho"])
        values.update({f"m{m}_{name}": value for name, value in d.items()})
    bounds = {
        "B1": "10.75", "curvature": "117", "m3_rho": "0.000263",
        "m5_rho": "7.3e-25", "m5_remainder_first": "7.9e-24",
        "m5_remainder_second": "1.7e-22",
    }
    for name, bound in bounds.items():
        assert values[name].lo > 0
        assert values[name].hi < F(bound), (name, serialize(values[name]))
    table = {
        "kappa": ("0.00084868730924288", "0.00084868730924289"),
        "B1": ("10.74965739776", "10.74965739777"),
        "B2": ("0.67024234490", "0.67024234492"),
        "curvature": ("116.22537651419", "116.22537651420"),
        "m3_rho": ("0.00026291407856", "0.00026291407858"),
        "m5_rho": ("7.25125221685e-25", "7.25125221687e-25"),
        "m5_remainder_first": ("7.84147998969e-24", "7.84147998971e-24"),
        "m5_remainder_second": ("1.69074692399e-22", "1.69074692402e-22"),
    }
    for name, (lower, upper) in table.items():
        assert F(lower) < values[name].lo <= values[name].hi < F(upper)
    return values, bounds, table


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    values, bounds, table = compute()
    record = {
        "date": "2026-10-18",
        "prepared_for": "Edward Baker",
        "model": "gpt-6-astra",
        "reasoning_effort": "max",
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Exact-rational enclosures of explicit manuscript constants; "
                 "not proof validation or independent review.",
        "arithmetic": {"type": "fractions.Fraction", "outward_dyadic_bits": BITS,
                       "atan_last_index": 40, "exp_degree": 32,
                       "exp_reduced_argument_upper_bound": "1/8"},
        "enclosures": {key: serialize(value) for key, value in values.items()},
        "strict_upper_bound_checks": bounds,
        "printed_table_enclosures_checked": table,
        "all_checks_passed": True,
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    for name in ("kappa", "B1", "B2", "curvature", "m3_rho", "m5_rho",
                 "m5_remainder_first", "m5_remainder_second"):
        print(name, serialize(values[name])["lower_decimal"],
              serialize(values[name])["upper_decimal"])
    print("All strict upper bounds passed.")


if __name__ == "__main__":
    main()
