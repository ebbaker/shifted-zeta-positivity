#!/usr/bin/env python3
"""Bounded exact algebra and frozen-input check for FCG-E02 R2.

Prepared for Edward Baker with substantial LLM assistance, 30 October 2026.
Actual recorded model gpt-6.1-sol, effort ultra, Investigation05 chat0047.
No theta evaluation, control-certificate replay, or flow simulation.
Run from anywhere after installation; uses the Python standard library.
"""

from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "papers/investigations-5/05_radial_theta_collision_geometry"
PACKET = BASE / (
    "research-progress/handoffs/fixed_coefficient_parameter_geometry/"
    "FCG-E02_R2_REGIONAL_COEFFICIENT_ASSESSMENT_20261030.md"
)
PACKET_HASH = "b561c7ce0bea695284aabc68e1923bf853e02a9639bca57b5944f4f9d02eeb89"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    assert digest(PACKET) == PACKET_HASH, "Issued packet changed"
    inputs = []
    for relative, expected in re.findall(
        r"\| \x60(papers/[^\x60]+)\x60 \| \x60([0-9a-f]{64})\x60 \|",
        PACKET.read_text(),
    ):
        actual = digest(ROOT / relative)
        assert actual == expected, f"Frozen input changed: {relative}"
        inputs.append({"path": relative, "sha256": actual, "matches": True})
    assert len(inputs) == 9

    checks = []

    def positive(name, value):
        assert value > 0, name
        checks.append({"check": name, "positive_exact_gap": str(value), "passed": True})

    def equal(name, actual, expected):
        assert actual == expected, name
        checks.append({"check": name, "exact_value": str(actual), "passed": True})

    exp3_lower = sum((F(3**k, factorial(k)) for k in range(9)), F(0))
    equal("sum k=0..8 of 3^k/k!", exp3_lower, F(89641, 4480))
    positive("exp3 partial sum exceeds 20", exp3_lower - 20)
    equal("20 times 11/10", F(20) * F(11, 10), F(22))
    arithmetic_upper = F(1, 22) / (1 - F(1, 22**3))**2
    positive("complete arithmetic majorant below 1/21", F(1, 21) - arithmetic_upper)
    positive("4pi-1 exceeds 11 using pi>31/10", 4 * F(31, 10) - 1 - 11)
    positive("primitive M0 lower bound exceeds 3/50", F(1, 16) - F(1, 1848) - F(3, 50))
    positive("8pi-5/16 exceeds 24 using pi>31/10", 8 * F(31, 10) - F(5, 16) - 24)
    positive("pi squared below 10 using pi<22/7", F(10) - F(22, 7)**2)
    positive("sqrt(pi)<9/5 using pi<22/7", F(9, 5)**2 - F(22, 7))
    positive("sqrt(24)>24/5", F(24) - F(24, 5)**2)
    equal("Gaussian prefactor rational upper comparison", F(18) / (2 * 24 * F(24, 5)), F(5, 64))
    equal("5/64 times 1/21", F(5, 64) * F(1, 21), F(5, 1344))
    positive("second-moment upper bound below 3/800", F(3, 800) - F(5, 1344))
    positive("a_plus<5 after squaring sqrt6<79/32", F(79, 32)**2 - 6)
    equal("coefficient lower comparison", 1 - F(25) * F(3, 800) / (2 * F(3, 50)), F(7, 32))
    equal("mass lower comparison", F(3, 50) * F(7, 32), F(21, 1600))

    # I_(2k)/sqrt(pi), for the half-line weight exp(-4u^2).
    gaussian = {0: F(1, 4)}
    for k in range(1, 4):
        gaussian[2*k] = F(2*k - 1, 8) * gaussian[2*k - 2]
    control_m0 = 64 * gaussian[4] + 6 * gaussian[0]
    control_m2 = 64 * gaussian[6] + 6 * gaussian[2]
    equal("Gaussian control M0/sqrt(pi)", control_m0, F(9, 4))
    equal("Gaussian control M2/sqrt(pi)", control_m2, F(21, 32))
    equal("Gaussian control M2/M0", control_m2/control_m0, F(7, 24))
    equal("Gaussian control center coefficient", 1 - 12 * control_m2/control_m0, F(-5, 2))
    positive("weighted-square event bracket fits own radius", F(1, 16) - F(1, 20000))
    equal("carrier radial Jacobian 4pi/(8pi) times dr/r=2du", F(4, 8) * 2, F(1))
    equal("K1 second moment in dimension three", F(3) * 2, F(6))
    equal("energy floor coefficient after removing pi*R^3", F(1, 4) / F(4, 3), F(3, 16))
    equal("C01 M2/m lower comparison", F(3, 800) / F(21, 1600), F(2, 7))
    equal("C01 H squared lower coefficient", F(9, 7) - F(2, 7), F(1))
    equal("C01 H_A squared coefficient", 1 + F(9, 7), F(16, 7))
    equal("zero-mass squared-L2 decay exponent 4kappa/7", 4 * F(7, 8) / 7, F(1, 2))

    # Algebraic cancellation in the imported Fourier split, no numerics.
    equal("low-frequency exponent -2+10/7", -2 + F(10, 7), F(-4, 7))
    record = {
        "task": "FCG-E02 R2",
        "date": "2026-10-30",
        "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial; internal proof assessment",
        "model": "gpt-6.1-sol",
        "effort": "ultra",
        "chat": "0047",
        "thread_id": "01a18d3a-0de3-7781-b7e1-79a42cf0a6fd",
        "packet": {"path": str(PACKET.relative_to(ROOT)), "sha256": PACKET_HASH},
        "inputs": inputs,
        "script_sha256": digest(Path(__file__)),
        "checks": checks,
        "all_passed": True,
        "scope": "Exact fractions and frozen byte identity only. Classical pi bounds, cosine strictness, theta tail domination, semigroup estimates and proof scope are assessed in the written review; not certified by this script.",
    }
    output = Path(__file__).with_name("fcg_e02_r2_exact_check_20261030.json")
    output.write_text(json.dumps(record, indent=2) + "\n")
    print(f"{len(checks)} exact algebra checks and {len(inputs)} frozen input hashes passed.")
    print(f"Record: {output}")


if __name__ == "__main__":
    run()
