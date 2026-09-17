#!/usr/bin/env python3
"""Exploratory verification for the inner-function note, 17 September 2026.

**NOT a registered check programme.** It requires `mpmath`, which the
repository's conventions exclude, so it is kept here rather than in
`numerics/` proper and is not listed in the CHECKS dictionary of
`validation/drafts.py`. Its purpose is to make the numbers quoted in
`notes/INNER_FUNCTION_AND_RESONANCE_20260917.md` reproducible.

Four groups, matching the note:

  (a) |K_w(i tau)| = 1, Proposition 1 (unconditional).
  (b) |K_w(i tau) - 1|^2 is a Lorentzian of height 4 and half-width w at each
      zero, Proposition 3.
  (c) its mass over a window is 2w times the number of zeros in the window.
  (d) the phase derivative Re[xi'/xi(1/2+w+i tau)] integrates to pi times the
      zero count, Section 4 -- the group-delay identity. The quadrature must be
      split at the zeros; a naive rule under-resolves peaks of width w.
  (e) the Cayley transform (1 - K_w)/(1 + K_w) is purely imaginary on the
      critical line and equals i tan(Psi), Psi = arg xi(1/2 + w + i tau).
      This is Section 5 of the critical-path note: the cumulative-storage
      coordinate of the shifted-zeta programme is a reactance, so the
      contraction criterion is positive-realness.

Author: Claude Opus 5 (Anthropic). Run: python3 exploratory/verify_inner_function.py
"""
from mpmath import (mp, mpf, mpc, zeta, gamma, pi, fabs, quad, zetazero,
                    siegeltheta, re, diff, arg, tan)
import json

mp.dps = 25


def xi(s):
    s = mpc(s)
    return mpf(1) / 2 * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def K(w, tau):
    """K_w(i tau) = xi(1/2 - w + i tau) / xi(1/2 + w + i tau)."""
    return xi(mpf(1) / 2 - w + 1j * tau) / xi(mpf(1) / 2 + w + 1j * tau)


def dlogxi(s):
    return diff(xi, s) / xi(s)


def main():
    out = {"date": "2026-09-17", "model": "claude-opus-5",
           "requires": "mpmath (not standard library); not a registered check"}

    # (a) unimodularity
    worst = mpf(0)
    for w in (mpf('0.5'), mpf('0.3'), mpf('0.05'), mpf('0.001')):
        for tau in (mpf('0.3'), mpf('5'), mpf('14.1'), mpf('30'), mpf('123.456')):
            worst = max(worst, fabs(fabs(K(w, tau)) - 1))
    out["unimodularity_worst_deviation"] = mp.nstr(worst, 5)

    zs = [zetazero(k).imag for k in range(1, 25)]
    g1 = zs[0]

    # (b) line shape at the first zero
    shape = []
    for w in (mpf('0.05'), mpf('0.01')):
        for du in (mpf('0'), w, 2 * w, 5 * w):
            shape.append({"w": float(w), "tau_minus_gamma1": float(du),
                          "computed": float(fabs(K(w, g1 + du) - 1) ** 2),
                          "lorentzian": float(4 * w ** 2 / (w ** 2 + du ** 2))})
    out["line_shape"] = shape

    # (c) absorption mass, one zero and a window
    mass = []
    for w in (mpf('0.05'), mpf('0.02'), mpf('0.01')):
        I = quad(lambda t: fabs(K(w, t) - 1) ** 2,
                 [g1 - 1, g1 - w, g1, g1 + w, g1 + 1]) / (2 * pi)
        mass.append({"window": "gamma_1 +- 1", "w": float(w),
                     "integral": float(I), "2w_times_count": float(2 * w),
                     "ratio": float(I / (2 * w))})
    T1, T2 = mpf(10), mpf(60)
    inwin = [z for z in zs if T1 < z < T2]
    for w in (mpf('0.02'), mpf('0.01')):
        pts = [T1] + sorted(z + d for z in inwin for d in (-w, 0, w)) + [T2]
        I = quad(lambda t: fabs(K(w, t) - 1) ** 2, pts) / (2 * pi)
        mass.append({"window": "[10,60]", "zeros": len(inwin), "w": float(w),
                     "integral": float(I),
                     "2w_times_count": float(2 * w * len(inwin)),
                     "ratio": float(I / (2 * w * len(inwin)))})
    out["absorption_mass"] = mass

    # (d) group delay
    delay = []
    T1, T2 = mpf(20), mpf(70)
    inwin = [z for z in zs if T1 < z < T2]
    for w in (mpf('0.2'), mpf('0.05')):
        pts = [T1]
        for z in inwin:
            pts += [z - 10 * w, z - w, z, z + w, z + 10 * w]
        pts = [T1] + [p for p in sorted(pts) if T1 < p < T2] + [T2]
        I = quad(lambda t: re(dlogxi(mpf(1) / 2 + w + 1j * t)), pts, maxdegree=3)
        delay.append({"window": "[20,70]", "zeros": len(inwin), "w": float(w),
                      "integral_Re_dlogxi": float(I),
                      "pi_times_count": float(pi * len(inwin)),
                      "theta_difference": float(siegeltheta(T2) - siegeltheta(T1))})
    out["group_delay"] = delay

    # (e) Cayley transform / positive-real reading
    cayley = []
    for w in (mpf('0.4'), mpf('0.1'), mpf('0.01')):
        for t in (mpf('3'), mpf('14.5'), mpf('40'), mpf('101.7')):
            Z = (1 - K(w, t)) / (1 + K(w, t))
            Psi = arg(xi(mpf(1) / 2 + w + 1j * t))
            cayley.append({"w": float(w), "tau": float(t),
                           "abs_Re_Z": float(fabs(re(Z))),
                           "abs_Z_minus_i_tan_Psi": float(fabs(Z - 1j * tan(Psi)))})
    out["cayley_reactance"] = cayley

    out["reading"] = (
        "The transfer symbol is unimodular on the critical line, so the transfer "
        "is an all-pass filter; the Riemann zeros are its resonances, each "
        "contributing a Lorentzian of height 4 and half-width w to |K_w - 1|^2 "
        "with mass 4 pi w, so the Weil form is the total resonant response; and "
        "the phase derivative is pi times the zero density, whose smooth part is "
        "theta'(tau), so the archimedean symbol is the filter's group delay. "
        "The Cayley transform of a unimodular symbol is a reactance, so the "
        "cumulative-storage criterion of the shifted-zeta programme is that the "
        "transfer's impedance be positive-real.")
    out["scope"] = (
        "Numerical support for Propositions 1 and 3 and Section 4 of the note. "
        "Unimodularity is unconditional; the resonance and delay readings are "
        "checked at finitely many points and on two windows. Nothing here is a "
        "positivity certificate and nothing assumes or tests the Riemann "
        "hypothesis.")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
