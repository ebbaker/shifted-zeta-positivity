#!/usr/bin/env python3
"""Interference bound and the two-channel exclusion for the localized Weil form.

Standard library only. Prints a JSON record to standard output.

The programme checks the inequality of the interference lemma,

    t * K[F] + B[F]/t + (w0 - sum kappa_p) ||f||^2 + P_L[f] >= 0   (t > 0),

which every coherent realization with archimedean channel norm K and prime
channel norm B = sum_p B_{r_p,d_p} must satisfy.  A single strictly negative
value at an explicit (L, f, t) excludes that channel architecture.  The
programme does not certify Weil positivity and constructs no field theory.

Quantities for a step function f on I_L are exact closed forms; the infinite
gamma series is summed with an explicit exponential tail bound (reported).
"""
import json
import math

EULER_GAMMA = 0.57721566490153286060651209008240243104215933593992
CATALAN = 0.91596559417721901505460351493238411077414937428167

# psi(1/4) = -gamma - pi/2 - 3 log 2 (Gauss digamma theorem);  w0 = psi(1/4) - log pi.
PSI_QUARTER = -EULER_GAMMA - math.pi / 2 - 3 * math.log(2)
W0 = PSI_QUARTER - math.log(math.pi)
# psi'(1/4) = pi^2 + 8 G;  sum_{n>=0} a_n^{-2} = psi'(1/4)/4 with a_n = 2n + 1/2.
PSI1_QUARTER = math.pi ** 2 + 8 * CATALAN
SUM_INV_A2 = PSI1_QUARTER / 4
NTERMS = 400


def a(n):
    return 2 * n + 0.5


def primes_below(x):
    out = []
    k = 2
    while k < x:
        if all(k % d for d in range(2, int(k ** 0.5) + 1)):
            out.append(k)
        k += 1
    return out


def kappa(p):
    r = p ** -0.5
    return 2 * math.log(p) * r / (1 - r)


def active_shifts(L):
    """(d, coefficient) for every prime power translation active on I_L."""
    out = []
    for p in primes_below(math.exp(L)):
        d, r, n = math.log(p), p ** -0.5, 1
        while n * d < L:
            out.append((n * d, 2 * d * r ** n))
            n += 1
    return out


class Step:
    """Real step function on I_L with m equal cells and values fv."""

    def __init__(self, L, fv):
        self.L, self.fv, self.m = L, list(fv), len(fv)
        self.h = L / self.m

    def corr(self, r):
        """<F, U_r F> = sum_{j,k} f_j f_k max(0, h - |r - (j-k)h|)."""
        h, fv, tot = self.h, self.fv, 0.0
        for j in range(self.m):
            for k in range(self.m):
                w = h - abs(r - (j - k) * h)
                if w > 0:
                    tot += fv[j] * fv[k] * w
        return tot

    def norm2(self):
        return self.corr(0.0)

    def _slope0(self):
        """Slope of c(0) - c(r) at r = 0+ (the function is linear on [0,h])."""
        return (self.corr(0.0) - self.corr(self.h)) / self.h

    def gamma_energy(self):
        """K[F] = 2 int_0^inf [c(0)-c(r)] n_gamma(r) dr, with n_gamma = sum_n e^{-a_n r}.

        Per mode: I_n = int_0^L (c(0)-c(r)) e^{-a_n r} dr + c(0) e^{-a_n L}/a_n.
        I_n - s0/a_n^2 decays like e^{-a_n h}, so the series is summed after
        subtracting the exactly known sum of s0/a_n^2.
        """
        L, h, m = self.L, self.h, self.m
        c0, s0 = self.corr(0.0), self._slope0()
        edges = [i * h for i in range(m + 1)]
        pieces = []
        for i in range(m):
            r0, r1 = edges[i], edges[i + 1]
            d0, d1 = c0 - self.corr(r0), c0 - self.corr(r1)
            slope = (d1 - d0) / (r1 - r0)
            pieces.append((r0, r1, d0 - slope * r0, slope))
        total, tail = 0.0, 0.0
        for n in range(NTERMS):
            an = a(n)
            acc = 0.0
            for r0, r1, const, slope in pieces:
                e0, e1 = math.exp(-an * r0), math.exp(-an * r1)
                acc += const * (e0 - e1) / an
                acc += slope * ((e0 * (r0 / an + 1 / an ** 2)) - (e1 * (r1 / an + 1 / an ** 2)))
            acc += c0 * math.exp(-an * L) / an
            total += acc - s0 / an ** 2
        aN = a(NTERMS)
        tail = abs(s0) * (h + 2 / aN) * math.exp(-aN * h) / (1 - math.exp(-2 * h)) \
            + c0 * math.exp(-aN * L) / (aN * (1 - math.exp(-2 * L)))
        return 2 * (total + s0 * SUM_INV_A2), 2 * tail

    def prime_channel(self, L):
        """B[F] = sum_p [ kappa_p ||f||^2 - 2 d_p sum_n r_p^n <F,U_{n d_p}F> ]."""
        val = sum(kappa(p) for p in primes_below(math.exp(L))) * self.norm2()
        for d, coef in active_shifts(L):
            val -= coef * self.corr(d)
        return val

    def prime_term(self, L):
        """The Weil prime contribution, -2 sum (log p) p^{-m/2} Re <F,U_{m log p}F>."""
        return -sum(coef * self.corr(d) for d, coef in active_shifts(L))

    def poles(self):
        L, h, fv = self.L, self.h, self.fv
        pc = ps = 0.0
        for j in range(self.m):
            lo = -L / 2 + j * h
            hi = lo + h
            pc += fv[j] * 2 * (math.sinh(hi / 2) - math.sinh(lo / 2))
            ps += fv[j] * 2 * (math.cosh(hi / 2) - math.cosh(lo / 2))
        return 2 * pc ** 2 - 2 * ps ** 2


def report(L, fv, t):
    s = Step(L, fv)
    K, Ktail = s.gamma_energy()
    B = s.prime_channel(L)
    P = s.poles()
    n2 = s.norm2()
    ksum = sum(kappa(p) for p in primes_below(math.exp(L)))
    residual = (W0 - ksum) * n2
    weil = K + W0 * n2 + P + s.prime_term(L)
    value = t * K + B / t + residual + P
    return {
        "L": L, "cells": len(fv), "f": fv, "t": t,
        "norm2": n2, "gamma_energy_K": K, "gamma_series_tail_bound": Ktail,
        "prime_channel_B": B, "poles_P": P, "kappa_sum": ksum,
        "residual_constant": residual, "weil_form_Q_L": weil,
        "interference_bound_value": value,
        "excluded": value < -1e-9,
    }


def closed_form_constant_K(L):
    """K[1_{I_L}] = psi'(1/4)/2 - 2 sum_n e^{-a_n L}/a_n^2."""
    s = sum(math.exp(-a(n) * L) / a(n) ** 2 for n in range(NTERMS))
    return PSI1_QUARTER / 2 - 2 * s


def main():
    checks = {}
    # 1. the closed form for the indicator agrees with the general step routine
    agree = []
    for L in (0.5, 1.0, 1.25, 1.5, 2.0, 3.0):
        general, _ = Step(L, [1.0]).gamma_energy()
        agree.append(abs(general - closed_form_constant_K(L)))
    checks["indicator_gamma_energy_closed_form"] = len(agree)
    assert max(agree) < 1e-12, max(agree)

    # 2. the two explicit certificates
    cert_main = report(1.25, [1.0], 1.3)
    cert_unit = report(1.0, [1, 1, 0, -1, -1, 0, 1, 1], 0.75)
    assert cert_main["excluded"] and cert_unit["excluded"]
    checks["explicit_certificates"] = 2

    # 3. the Weil form itself stays nonnegative on these inputs (t = 1 is Q_L)
    pos = 0
    for L in (0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0, 4.0):
        r = report(L, [1.0], 1.0)
        assert abs(r["interference_bound_value"] - r["weil_form_Q_L"]) < 1e-9
        assert r["weil_form_Q_L"] > 0
        pos += 1
    checks["t_equals_one_is_the_weil_form"] = pos

    # 4. scan: where the indicator alone already violates the bound
    scan = []
    for i in range(0, 61):
        L = 0.5 + i * 0.1
        s = Step(L, [1.0])
        K, _ = s.gamma_energy()
        B = s.prime_channel(L)
        if B <= 0:
            continue
        t = math.sqrt(B / K)
        s_ = report(L, [1.0], t)
        scan.append({"L": round(L, 3), "t_star": t,
                     "value": s_["interference_bound_value"],
                     "excluded": s_["excluded"]})
    first = next(r["L"] for r in scan if r["excluded"])
    checks["indicator_scan_points"] = len(scan)

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-15",
        "arithmetic": "floating point with an explicit gamma-series tail bound",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "certificate_L_5_4_indicator": cert_main,
        "certificate_L_1_step": cert_unit,
        "first_excluded_L_for_the_indicator": first,
        "indicator_scan": scan,
        "scope": "Checks the interference inequality for the archimedean/prime "
                 "two-channel architecture. A negative value excludes that "
                 "architecture at that interval. No Weil positivity certificate, "
                 "no field-theoretic construction, and no statement about "
                 "realizations with different channel norms.",
    }, indent=2))


if __name__ == "__main__":
    main()
