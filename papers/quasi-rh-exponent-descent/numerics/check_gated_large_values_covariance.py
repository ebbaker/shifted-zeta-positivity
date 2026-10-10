#!/usr/bin/env python3
"""Finite sextic-mask and gated large-values checks; no asymptotic proof.

The exact finite character model is over integer residue fields at split
prime norms. It is not an Eisenstein detector bin or a source slot manifest.
Only the phase-normalized identity uses floating square roots; the companion
amplitude identity and every valuation, mask and exponent check are exact.
"""
from __future__ import annotations

import cmath
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

COUNT = 0
MAX_ERROR = 0.0
ROOTS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
PRIMES = (7, 13, 19)
ETA, ELL = F(1, 5000), F(1, 10**6)


def check(value, why=""):
    global COUNT
    COUNT += 1
    if not value:
        raise AssertionError(why)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(c, x):
    return c*x[0], c*x[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c+b*d


def conj(x):
    return x[0]+x[1], -x[1]


def norm(x):
    a, b = x
    return a*a+a*b+b*b


def as_complex(x):
    return complex(float(x[0]))+float(x[1])*cmath.exp(1j*math.pi/3)


def primitive_log(p):
    for g in range(2, p):
        values = [pow(g, j, p) for j in range(p-1)]
        if len(set(values)) == p-1:
            return {v: j % 6 for j, v in enumerate(values)}
    raise AssertionError("no primitive root")


LOGS = {p: primitive_log(p) for p in PRIMES}


def character(row, n, keep_zero=True):
    exponent = 0
    for e, p in zip(row, PRIMES):
        if e:
            if n % p == 0:
                return (0, 0) if keep_zero else (1, 0)
            exponent += e*LOGS[p][n % p]
    return ROOTS[exponent % 6]


def mobius(n):
    answer, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            answer = -answer
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -answer if n > 1 else answer


def finite_model():
    rows = list(itertools.product(range(6), repeat=3))
    columns = [n for n in range(15, 61) if math.gcd(n, 6) == 1]
    inverse = [d for d in range(28, 111) if math.gcd(d, 6) == 1]
    D, N, slots = 55, 30, (7, 37)
    slot_product = math.prod(slots)
    deleted_checks = 0
    neighbor_max = 0
    for u in rows:
        by_conductor = {}
        for v in rows:
            q = math.prod(p for p, a, b in zip(PRIMES, u, v) if a != b)
            delete = math.prod(p for p, a, b in zip(PRIMES, u, v) if a == b and a > 0)
            ratio = tuple((a-b) % 6 for a, b in zip(u, v))
            by_conductor[q] = by_conductor.get(q, 0)+1
            for n in columns:
                actual = mul(character(u, n), conj(character(v, n)))
                expected = character(ratio, n) if math.gcd(n, delete) == 1 else (0, 0)
                check(actual == expected, "a canceled local phase lost its zero")
                if delete > 1 and math.gcd(n, delete) > 1:
                    deleted_checks += 1
        for q, multiplicity in by_conductor.items():
            omega = sum(q % p == 0 for p in PRIMES)
            check(multiplicity <= 5**omega)
            neighbor_max = max(neighbor_max, multiplicity)

    data = []
    coefficient = {}
    for d in inverse:
        for n in columns:
            product = d*n*slot_product
            coefficient[product] = coefficient.get(product, 0)+mobius(d)
    for row in rows:
        if not any(row):
            continue  # The detector family is nonprincipal.
        plain = (0, 0)
        inv = (0, 0)
        for n in columns:
            plain = add(plain, character(row, n))
        for d in inverse:
            inv = add(inv, scale(mobius(d), character(row, d)))
        prime = (1, 0)
        for p in slots:
            prime = mul(prime, character(row, p))
        expanded = (0, 0)
        for n, c in coefficient.items():
            expanded = add(expanded, scale(c, character(row, n)))
        check(expanded == mul(mul(inv, plain), prime), "marked convolution mismatch")
        weight = F(norm(mul(inv, prime)), D*slot_product)
        data.append({"row": row, "s": plain, "w": weight,
                     "plain_square": F(norm(plain), N)})
    live = [x for x in data if x["w"] > 0 and x["plain_square"] > 0]
    threshold = sorted(x["plain_square"] for x in live)[len(live)//2]
    gate = [x for x in data if x["w"] > 0 and x["plain_square"] >= threshold]
    mass = sum((x["w"] for x in gate), F(0))
    energy = sum((x["w"]*x["plain_square"] for x in gate), F(0))
    covariance = (F(0), F(0))
    diagonal = F(0)
    phase_covariance = 0j
    column_norm_phase = 0.0
    for u in gate:
        su = as_complex(u["s"])/math.sqrt(N)
        eu = su/abs(su)
        for v in gate:
            sv = as_complex(v["s"])/math.sqrt(N)
            ev = sv/abs(sv)
            knum = (0, 0)
            for n in columns:
                knum = add(knum, mul(character(u["row"], n), conj(character(v["row"], n))))
            endpoint = mul(conj(u["s"]), v["s"])
            term = scale(u["w"]*v["w"]/N**2, mul(endpoint, knum))
            covariance = add(covariance, term)
            phase_covariance += float(u["w"]*v["w"])*eu.conjugate()*ev*as_complex(knum)/N
            if u["row"] == v["row"]:
                diagonal += term[0]
                check(term[1] == 0)
    check(covariance[1] == 0 and covariance[0] >= 0)
    # Exact amplitude endpoint version: E_gate^2 <= L_N * B_gate.
    check(energy**2 <= len(columns)*covariance[0])
    check(energy >= threshold*mass)
    exact_column_norm = F(0)
    for n in columns:
        column = (F(0), F(0))
        floating_column = 0j
        for u in gate:
            column = add(column, scale(u["w"], mul(conj(u["s"]), character(u["row"], n))))
            su = as_complex(u["s"])/math.sqrt(N)
            floating_column += float(u["w"])*(su/abs(su)).conjugate()*as_complex(character(u["row"], n))/math.sqrt(N)
        exact_column_norm += norm(column)/N**2
        column_norm_phase += abs(floating_column)**2
    check(exact_column_norm == covariance[0])
    global MAX_ERROR
    MAX_ERROR = max(MAX_ERROR, abs(phase_covariance-column_norm_phase))
    check(abs(phase_covariance.imag) < 2e-10)
    check(abs(phase_covariance.real-column_norm_phase) < 2e-10)
    check(phase_covariance.real+2e-10 >= float(threshold*mass**2/len(columns)))
    return {"sixth_power_free_valuation_rows": len(rows), "nonprincipal_rows": len(data),
            "live_gated_rows": len(gate), "plain_columns": len(columns),
            "inverse_columns": len(inverse), "whole_slot_prime_labels": list(slots),
            "convolution_columns": len(coefficient), "retained_canceled_mask_cases": deleted_checks,
            "maximum_fixed_conductor_neighbor_multiplicity": neighbor_max,
            "gate_threshold": str(threshold), "gated_inverse_mass": str(mass),
            "gated_mixed_energy": str(energy), "exact_amplitude_covariance": str(covariance[0]),
            "exact_diagonal_covariance": str(diagonal),
            "exact_off_diagonal_covariance": str(covariance[0]-diagonal),
            "phase_covariance_real": phase_covariance.real,
            "phase_identity_max_absolute_error": MAX_ERROR}


def params(d, x):
    a, B, DD = F(5, 6)-d, 2-8*x/9, 3-17*x/9
    P, J = B*(1-x), a*DD+d*B*(1-x)
    Fx = a*B/J
    Rnew = 1-d+a*d*P/(2*J)-Fx*ETA
    return Rnew


def rational_ledger():
    dlo, dhi, xlo, xhi = F(9, 25), F(21, 50), F(49, 100), F(1, 2)
    alo, Bmax, Dmin = F(5, 6)-dhi, F(352, 225), F(37, 18)
    hmax = Bmax*(1-xlo)/Dmin
    abs_Fd_max = F(5, 6)*Bmax**2*(1-xlo)/(alo*Dmin)**2
    check(-1+hmax/2+ETA*abs_Fd_max+F(2, 5) < 0)
    # h_x = ((10/9)(1-x)-B D)/D^2 <0, and F_x>0.
    check(F(10, 9)*(1-xlo)-F(14, 9)*Dmin < 0)
    Rmin = params(dhi, xhi)
    sum_min = Rmin+dhi*F(2, 5)
    amplitude_gap = dhi*F(1, 50)*F(3, 20)
    low_pair_reserve = sum_min-F(3, 2)*F(8, 15)-amplitude_gap
    diagonal_reserve = Rmin-(1-dlo)*F(207, 500)-amplitude_gap
    check(Rmin == F(158126, 248125))
    check(sum_min == F(199811, 248125))
    check(amplitude_gap == F(63, 50000))
    check(low_pair_reserve == F(79869, 19850000))
    check(diagonal_reserve == F(7365613, 19850000))
    check(low_pair_reserve-ELL > F(1, 250))
    check(diagonal_reserve-ELL > F(37, 100))
    check((F(7, 8)-dhi)*F(2, 5) == F(91, 500))
    check((F(1, 2)-dhi)*F(2, 5) == F(4, 125))
    # Solving the large-values quadratic supplies an actual positive
    # mass reserve, rather than only excluding the unbuffered threshold.
    for a, b, mass in itertools.product(
            [F(0), F(1, 10), F(1), F(3)],
            [F(0), F(1, 7), F(1), F(5)],
            [F(i, 10) for i in range(61)]):
        if mass**2 <= b+a*mass:
            check(max(F(0), mass-a)**2 <= b)
    for delta in [F(1, 1000000), F(1, 10000), F(1, 100)]:
        reserve = low_pair_reserve-ELL
        zeta = min(delta/4, reserve/4)
        check(0 < zeta < delta/2)
        check(zeta < reserve)
        check(delta-2*zeta > 0 and reserve-zeta > 0)
    # Finite sample checks supplement, and do not replace, monotonicity.
    for i in range(31):
        d = dlo+(dhi-dlo)*F(i, 30)
        for j in range(21):
            x = xlo+(xhi-xlo)*F(j, 20)
            R = params(d, x)
            check(R >= Rmin)
            check(R+d*F(2, 5) >= sum_min)
    return {"low_row_ratio_conductor_cap_exponent": "8/15",
            "target_count_uniform_lower": str(Rmin),
            "target_count_plus_plain_gate_uniform_lower": str(sum_min),
            "universal_slot_upper_lower_gap_upper": str(amplitude_gap),
            "low_pair_absorption_reserve_before_losses": str(low_pair_reserve),
            "principal_pair_absorption_reserve_before_losses": str(diagonal_reserve),
            "total_literal_large_values_loss_assumed_upper": str(ELL),
            "low_pair_reserve_after_assumed_losses": str(low_pair_reserve-ELL),
            "source_entrywise_covariance_exponent_deficit_lower": "91/500",
            "hypothetical_square_root_covariance_exponent_deficit_lower": "4/125"}


def main():
    finite = finite_model()
    ledger = rational_ledger()
    record = {"date": "2026-10-09", "assertions": COUNT,
              "model": "GPT-6 (Codex), inherited configuration; exact serving variant and reasoning effort not exposed",
              "scope": "Finite exact sextic character, physical-zero, marked-convolution, gated amplitude-covariance and rational exponent identities. The phase-normalized identity uses floating roots. No native Eisenstein zero bin, source slot manifest, unbounded covariance, or improved count is certified.",
              "finite_model": finite, "continuous_ledger": ledger,
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out = Path(__file__).with_name("gated_large_values_covariance_record_20261009.json")
    out.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(f"{COUNT} assertions passed; wrote {out.name}")
    print(f"Low-pair conditional absorption reserve: {ledger['low_pair_reserve_after_assumed_losses']}")
    print(f"Phase identity maximum absolute error: {MAX_ERROR:.3g}")


if __name__ == "__main__":
    main()
