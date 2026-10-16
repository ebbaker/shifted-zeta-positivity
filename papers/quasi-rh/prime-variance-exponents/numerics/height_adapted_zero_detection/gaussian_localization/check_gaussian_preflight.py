#!/usr/bin/env python3
"""Formal Gaussian diagnostics for Edward Baker, 4 October 2026.

Prepared with substantial LLM assistance: GPT-6 (Codex), inherited
configuration; exact serving variant and reasoning effort not exposed.
No zeta zero calculations or outward certificates.
"""
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

b = Fraction(3, 4)
a = Fraction(20)
delta = Fraction(1, 16)
radius = Fraction(3)
H = delta * (a - delta)
G = radius * radius - (1 - b) ** 2 - a * (1 - b)
assert H == Fraction(319, 256)
assert G == Fraction(63, 16)
assert a >= 2 * b and G > H > 0

def logadd(x, y):
    hi = max(x, y)
    return hi + math.log1p(math.exp(min(x, y) - hi))

rows = []
for N in range(1, 4097):
    kmin = 4 * (N + 1)
    log_eta = -N * (math.log(8) + 1)
    log_left = math.log(N) - kmin * float(H)
    log_remote = math.log(N) - kmin * float(G)
    log_ratio = logadd(log_left, log_remote) - log_eta
    assert log_ratio < -math.log(2)
    rows.append((N, log_ratio))

worst_N, worst_log_ratio = max(rows, key=lambda row: row[1])

# Formal equal-real-part pair. Its normalized sum is exactly
# 2*cos(k*nu*(a+2*xi)); this vanishes at the chosen nu.
k = 40.0
xi = 0.05
nu = math.pi / (2 * k * (float(a) + 2 * xi))
phase = k * nu * (float(a) + 2 * xi)
normalized_pair = cmath.exp(1j * phase) + cmath.exp(-1j * phase)
assert abs(normalized_pair) < 1e-14

# The ray mu=a*k turns residues into ordinary integer powers exactly.
h = 4.0
power = 7
formal_coordinate = complex(0.00001, 0.02)
exponent = formal_coordinate ** 2 + float(a) * formal_coordinate
direct = cmath.exp(h * power * exponent)
power_sum_base = cmath.exp(h * exponent) ** power
ray_residual = abs(direct - power_sum_base) / max(1, abs(direct))
assert ray_residual < 1e-13

record = {
    "status": "formal identities and floating parameter diagnostics only",
    "zeta_zero_claim": False,
    "outward_certificate": False,
    "model": "GPT-6 (Codex), inherited configuration",
    "reasoning_effort": "not exposed; not inferred",
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "parameters": {"b": str(b), "a": str(a), "delta": str(delta),
                   "R": str(radius), "H": str(H), "G": str(G),
                   "h": 4, "m": "N"},
    "loss_checks": {"N_min": 1, "N_max": 4096,
                    "worst_N": worst_N,
                    "largest_loss_over_eta": math.exp(worst_log_ratio),
                    "required_upper_ratio": 0.5,
                    "selected_log_ratios": [{"N": N, "log_loss_over_eta": lr}
                        for N, lr in rows if N in (1, 2, 4, 8, 16, 32, 64,
                                                  128, 256, 512, 1024, 4096)]},
    "formal_cancellation": {"k": k, "xi": xi, "nu": nu,
                            "phase": phase,
                            "normalized_pair_absolute_residual": abs(normalized_pair)},
    "ray_power_identity_relative_residual": ray_residual,
}
output = Path(__file__).with_name('gaussian_preflight_record_20261004.json')
output.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({"record": str(output),
                  "worst_N": worst_N,
                  "largest_loss_over_eta": math.exp(worst_log_ratio),
                  "formal_pair_residual": abs(normalized_pair),
                  "ray_residual": ray_residual}))
