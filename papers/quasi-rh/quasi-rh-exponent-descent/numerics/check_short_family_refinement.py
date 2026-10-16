#!/usr/bin/env python3
"""Exact algebra checks for the fixed-short-family extraction refinement.

No asymptotic moment, prime-counting theorem, or zero-free claim is tested.
Only standard-library rational arithmetic is used. Output is reproducible.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def chain(h, a):
    b = (1 + a) / 2 + 5 * h / 12
    c = 1 - h / 6
    assert 0 < h <= 1 and a >= 0 and 0 < c < 1
    if b >= 1:
        return {"h": str(h), "a": str(a), "b": str(b), "trivial": True}
    theta = F(1)
    stages = [str(theta)]
    n = 0
    while theta > b:
        n += 1
        theta = max(b, c * theta)
        assert theta == max(b, c**n)
        stages.append(str(theta))
        assert n < 10000
    assert c**n <= b < c ** (n - 1)
    assert theta == b
    # Squared full-family exponent minus the prime repetition count.
    assert 2 * b == 1 + a + h - h / 6
    # Unrestricted positive coefficients force precisely b >= 1.
    assert 2 - (1 + a + 5 * h / 6) == 2 * (1 - b)
    return {
        "h": str(h), "a": str(a), "b": str(b), "c": str(c),
        "stages": n, "chain": stages,
    }


def moebius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign


def nu(n):
    # Completely multiplicative, including nu(2)=-1 and nu(3)=1.
    v2 = 0
    while n % 2 == 0:
        n //= 2
        v2 += 1
    return (-1) ** v2


def weight(x):
    # Compact annular rational test; smoothness is not needed for identity QA.
    return (x - 1) * (2 - x) if 1 <= x <= 2 else F(0)


def masked_sum(scale, p=None):
    upper = int(2 * scale)
    return sum(
        (moebius(n) * nu(n) * weight(F(n) / scale)
         for n in range(1, upper + 1) if p is None or n % p), F(0)
    )


def mask_checks():
    records = []
    for p in (2, 3, 5, 7):
        for scale in (F(32), F(63, 2), F(121)):
            a = masked_sum(scale)
            b = masked_sum(scale, p)
            lower = masked_sum(scale / p, p)
            assert a == b - nu(p) * lower
            geometric = F(0)
            j = 0
            reduced = scale
            while 2 * reduced >= 1:
                geometric += nu(p) ** j * masked_sum(reduced)
                reduced /= p
                j += 1
            assert b == geometric
            # Dropping the mask must actually be detectable in this fixture.
            records.append({"prime": p, "scale": str(scale), "a": str(a),
                            "masked": str(b), "terms": j})
    assert any(r["a"] != r["masked"] for r in records)
    return records


def main():
    cases = [chain(F(2, 3), F(0)), chain(F(1, 2), F(0)),
             chain(F(1, 4), F(0)), chain(F(1, 10), F(0)),
             chain(F(2, 3), F(1, 20))]
    assert cases[0]["chain"] == ["1", "8/9", "64/81", "7/9"]
    result = {
        "status": "all exact algebra and finite mask checks passed",
        "scope": "No arithmetic moment or zero-free region is certified.",
        "model": "GPT-6 (Codex), inherited; serving variant and effort unexposed",
        "chains": cases,
        "mask_checks": mask_checks(),
        "source_range_example": {
            "h": "2/3", "B": "1",
            "dual_ratio_exponent_upper": "1/3",
            "required_new_regime": "dual row length can exceed column product",
        },
    }
    output = Path(__file__).with_name("short_family_refinement_check.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(cases)} rational chains; 12 finite masked identities")
    print(output)


if __name__ == "__main__":
    main()
