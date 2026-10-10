#!/usr/bin/env python3
"""A surviving annular opposite-valuation block and gated-count bookkeeping.

This checks finite residue algebra, literal annular ownership, and rational
implications. It does not prove a native selected moment, lattice Poisson,
prime-ideal asymptotics, or a power estimate for the remaining aggregate.
Only numpy and the Python standard library are required.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

import numpy as np


ASSERTIONS = 0


def require(condition, message=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def prime64(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # This Miller--Rabin base set is deterministic below 2**64.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        y = pow(a, d, n)
        if y in (1, n - 1):
            continue
        for _ in range(s - 1):
            y = y * y % n
            if y == n - 1:
                break
        else:
            return False
    return True


def next_split_prime(n):
    n += (1 - n) % 6
    while not prime64(n):
        n += 6
    require(n < 2**64)
    require(n % 6 == 1 and prime64(n))
    return n


def factors_divisors(factors):
    for es in itertools.product(*(range(e + 1) for _, e in factors)):
        yield math.prod(p**e for (p, _), e in zip(factors, es)), es


def plateau_value(x):
    # Certificate for any fixed C-infinity profile equal to one on [1/2,2]
    # and zero outside [1/3,3]. No live factor enters its transition zone.
    if x <= F(1, 3) or x >= 3:
        return 0
    if F(1, 2) <= x <= 2:
        return 1
    return None


def coefficient(factors, D, N):
    total = math.prod(p**e for p, e in factors)
    ans, live = 0, []
    for dinv, de in factors_divisors(factors):
        if max(de) > 1:
            continue
        remain = [(p, e - di) for (p, e), di in zip(factors, de)]
        for v1, _ in factors_divisors(remain):
            v2 = total // (dinv * v1)
            values = [plateau_value(F(dinv, D)),
                      plateau_value(F(v1, N)), plateau_value(F(v2, N))]
            if 0 in values:
                continue
            require(None not in values, "Unexpected profile transition")
            mu = (-1)**sum(de)
            ans += mu
            live.append([dinv, v1, v2, mu])
    return ans, live


def annular_block():
    p, q = 7, 13
    U, D, N = 10**25, 10**18, 2 * 10**10
    d1 = next_split_prime(D)
    d2 = next_split_prime(d1 + 1)
    t1 = next_split_prime(N // q)
    t2 = next_split_prime(N // (p * q))
    t3 = next_split_prime(N // p)
    t4 = next_split_prime(t2 + 1)
    require(len({p, q, d1, d2, t1, t2, t3, t4}) == 8)
    k1f = [(p, 1), (q, 2), (d1, 1), (t1, 1), (t2, 1)]
    k2f = [(p, 2), (q, 1), (d2, 1), (t3, 1), (t4, 1)]
    c1, live1 = coefficient(k1f, D, N)
    c2, live2 = coefficient(k2f, D, N)
    require(c1 == c2 == -4)
    require(len(live1) == len(live2) == 4)
    require(all(t[0] == d1 for t in live1))
    require(all(t[0] == d2 for t in live2))
    # No column divisor enters the short comparison annulus [Y1/3,3Y1],
    # Y1=U**(1/4); compare fourth powers exactly, avoiding floating roots.
    for fs in (k1f, k2f):
        for a, _ in factors_divisors(fs):
            require(a**4 * 81 < U or a**4 > 81 * U)
    k1 = math.prod(p**e for p, e in k1f)
    k2 = math.prod(p**e for p, e in k2f)
    require(math.gcd(k1, k2) == p * q)
    a, b = d1 * t1 * t2, d2 * t3 * t4
    f = p * q * a * b
    require(k1 == p * q**2 * a and k2 == p**2 * q * b)
    require(math.gcd(a, b) == math.gcd(a * b, p * q) == 1)
    # r=.72, d=.4: B=U**(.286). These integer comparisons are stronger
    # than the requested pair gates, since a,b>U and f>U**2.
    require(a > U and b > U and f > U**2)
    require(max(e for _, e in k1f + k2f) < 6)
    require(D**10 > U**7 and D**100 < U**73)
    require(N**5 > U**2 and N**500 < U**207)
    return {
        "U": str(U), "D": str(D), "N": str(N),
        "prime_norms": dict(zip(["p", "q", "d1", "d2", "t1", "t2", "t3", "t4"],
                               map(str, [p, q, d1, d2, t1, t2, t3, t4]))),
        "centered_coefficients": [c1, c2],
        "live_ownerships": [live1, live2],
        "gcd_norm": p * q, "exclusive_norms": [str(a), str(b)],
        "primitive_good_quotient_norm": str(f),
        "sixth_power_factors": [1, 1],
    }


def primitive_root(p):
    primes, n = [], p - 1
    f = 2
    while f * f <= n:
        if n % f == 0:
            primes.append(f)
            while n % f == 0:
                n //= f
        f += 1
    if n > 1:
        primes.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // a, p) != 1 for a in primes):
            return g
    raise AssertionError("No root")


def sextic(p, power):
    g = primitive_root(p)
    values = np.zeros(p, dtype=complex)
    x = 1
    for j in range(p - 1):
        values[x] = np.exp(2j * np.pi * ((power * j) % 6) / 6)
        x = x * g % p
    return values


def finite_fourier():
    errors, records = [], []
    for primes, powers in [([7, 13], [-1, 1]),
                           ([7, 13, 19], [-1, 1, 1]),
                           ([7, 13, 31], [1, -1, -1])]:
        Q = math.prod(primes)
        local = [sextic(p, e) for p, e in zip(primes, powers)]
        values = np.array([math.prod(ch[x % p] for p, ch in zip(primes, local))
                           for x in range(Q)], dtype=complex)
        gauss = np.fft.ifft(values) * math.sqrt(Q)
        tau_crt = math.prod(ch[(Q // p) % p] *
                            (np.fft.ifft(ch) * math.sqrt(p))[1]
                            for p, ch in zip(primes, local))
        for j in range(Q):
            err = abs(gauss[j] - np.conjugate(values[j]) * gauss[1])
            errors.append(err)
            require(err < 2e-11)
            require((abs(values[j]) < 1e-12) == any(j % p == 0 for p in primes))
        require(abs(gauss[1] - tau_crt) < 2e-11)
        require(abs(abs(gauss[1]) - 1) < 2e-11)
        require(abs(gauss[0]) < 2e-11)
        coherent = np.array([float(abs(v - 1) < 1e-11) for v in values])
        phi = math.prod(p - 1 for p in primes)
        require(int(sum(coherent)) == phi // 6)
        masks = [np.array([float(x % 5 in (1, 3)) for x in range(Q)]),
                 coherent,
                 np.ones(Q)]
        for W in masks:
            lhs = np.dot(W, values)
            rhs = gauss[1] / math.sqrt(Q) * np.dot(np.conjugate(values), np.fft.fft(W))
            err = abs(lhs - rhs)
            errors.append(err)
            require(err < 2e-9)
        H = np.dot(coherent, values)
        require(abs(H - phi / 6) < 2e-9)
        require(abs(sum(values)) < 2e-9)
        records.append({"prime_norms": primes, "local_powers": powers,
                        "quotient_norm": Q, "unit_count": phi,
                        "coherent_mask_count": phi // 6,
                        "coherent_kernel_real": round(float(H.real), 10),
                        "normalized_gauss_modulus": round(abs(gauss[1]), 12)})
    return {"blocks": records, "max_absolute_error": max(errors),
            "tolerance": 2e-9,
            "scope": "Finite residue-ring algebra; local additive conventions are chosen explicitly. This is not native lattice Poisson or a selected-row experiment."}


def rational_targets():
    eta, ell = F(1, 5000), F(1, 10**6)
    samples, Fs = [], []
    for d, x in itertools.product([F(9, 25), F(39, 100), F(21, 50)],
                                   [F(49, 100), F(99, 200), F(1, 2)]):
        a, B, Dc = F(5, 6) - d, 2 - 8*x/9, 3 - 17*x/9
        P, J = B*(1-x), a*Dc+d*B*(1-x)
        Fx = a*B/J
        Rstar = 1-d+a*d*P/(2*J)
        Rnew = Rstar-Fx*eta
        rnew = 1-Fx/2-(1-Fx)*eta/(d*(1-x))
        require(1-d*(x+(1-x)*rnew) == Rnew+eta)
        Fs.append(Fx)
        for ar in [0, eta/(2*d*(1-x)), eta/(d*(1-x)),
                   (eta+ell)/(d*(1-x))]:
            r = rnew+ar
            direct = 1-d*(x+(1-x)*r)-Rnew
            tapered = eta-d*(1-x)*ar
            require(direct == tapered)
            require(1-d*(x+(1-x)*r)-max(0, tapered) <= Rnew)
            samples.append({"d": str(d), "x": str(x),
                            "r_minus_rnew": str(ar),
                            "gated_inverse_mass_gain_needed_before_losses": str(max(0, tapered))})
    require(min(Fs) == F(1091200, 2012413))
    require(min(Fs)*eta-F(1, 10000) == F(169987, 20124130000))
    # Two positive classes: the new high-plain gate can have power-small
    # inverse mass while the full mixed energy remains a fixed fraction.
    for t in [F(1, 1000), F(1, 100), F(1, 10)]:
        high_mass, outside_mass = t, 1-t
        gate, outside_plain = F(3, 4), F(1, 2)
        require(outside_plain < gate)
        require(high_mass == t)
        mixed = high_mass+outside_mass*outside_plain
        require(mixed >= F(1, 2))
    return {"minimum_payoff_factor": str(min(Fs)),
            "count_reserve_at_uniform_eta": str(min(Fs)*eta-F(1, 10000)),
            "tapered_samples": samples,
            "scope": "Exact detector/count and positive-measure implications, conditional on the stated witness and pointwise inputs; no arithmetic tail mass estimate is proved."}


def main():
    block = annular_block()
    fourier = finite_fourier()
    targets = rational_targets()
    record = {"date": "2026-10-09", "annular_native_ideal_block": block,
              "finite_fourier": fourier, "weaker_gated_count_target": targets,
              "assertions": ASSERTIONS,
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "status": "New exact block transform and weaker sufficient detector obligation; full mixed moment and power estimate remain unproved."}
    path = Path(__file__).with_name("mixed_program_checkpoint_record_20261009.json")
    path.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(f"{ASSERTIONS} assertions passed; wrote {path.name}")
    print(f"Centered annular coefficients: {block['centered_coefficients']}; gcd norm {block['gcd_norm']}")
    print(f"Maximum finite Fourier error: {fourier['max_absolute_error']:.3g}")


if __name__ == "__main__":
    main()
