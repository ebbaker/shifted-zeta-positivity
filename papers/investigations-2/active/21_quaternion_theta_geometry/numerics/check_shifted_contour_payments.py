#!/usr/bin/env python3
"""Ball-arithmetic replay of Note 12's complete-source tail payments.

2026-10-14. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6.1-sol (Codex); reasoning effort: ultra.
Uses python-flint. Selected-point agreement checks are implementation tests,
not stationary-sign certificates or an arbitrary-height nonvanishing claim.
"""
import argparse
from hashlib import sha256
import json
from math import ceil, comb, factorial, sqrt
from pathlib import Path
import platform

import flint
from flint import arb, acb, ctx


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def enc(a):
    require(a.is_finite(), "Nonfinite real enclosure")
    def dy(v):
        m, e = v.man_exp()
        return {"mantissa": str(m), "exponent": int(e)}
    return {"display": a.str(20, more=True),
            "lower_dyadic": dy(a.lower()), "upper_dyadic": dy(a.upper())}


def symmetric(a):
    require(a >= 0, "Negative error payment")
    return arb(0, a.upper())


def s_poly(k, lam, b):
    return sum(arb(comb(k, r)*factorial(r))*b**(k-r)/lam**(r+1)
               for r in range(k+1))


def index_payment(k, a, n, tau):
    c = (4*a).cos()
    m = n+1
    alpha = arb.pi()*m*m
    beta = c*alpha
    rho = (arb(m+1)/m)**4*(-arb.pi()*c*(2*m+1)).exp()
    lam = 4*beta-9
    require(c > 0 and rho < 1 and lam > 0 and 8*beta >= tau,
            "Index-tail hypotheses")
    payment = (2*alpha**2+3*alpha)*(-beta).exp()/(1-rho)*s_poly(k, lam, a)
    return payment, rho, beta


def integration_payment(k, a, u, tau):
    c = (4*a).cos()
    b = arb.pi()*c*(4*u).exp()
    rho = 16*(-3*b).exp()
    lam = 4*b-9-2*tau*u
    exponent = tau*u*u+9*u-b
    require(c > 0 and rho < 1 and lam > 0 and 8*b >= tau,
            "Integration-tail hypotheses")
    payment = (2*arb.pi()**2+3*arb.pi())*exponent.exp()/(1-rho)*s_poly(k, lam, u+a)
    return payment, rho, exponent


def finite_integral(k, a, n, u, t, x, tol):
    ii = acb(0, 1)
    p = arb.pi()
    def f(v, analytic):
        z = v+ii*a
        source = acb(0)
        for j in range(1, n+1):
            alpha = p*j*j
            source += (2*alpha*alpha*(9*z).exp()-3*alpha*(5*z).exp())*(-alpha*(4*z).exp()).exp()
        return (ii*z)**k*(t*z*z+ii*x*v).exp()*source
    value = acb.integral(f, 0, u, rel_tol=tol, abs_tol=tol,
                         eval_limit=100000, depth_limit=35)
    require(value.is_finite(), "Finite shifted quadrature")
    return value.real


def scalable_samples():
    rows = []
    tau = arb(1)/2
    p = 12
    for x in (41, 100, 1000, 1000000, 1000000000000):
        xx = arb(x)
        ell = xx.log()
        target = xx/(2*arb.pi())*(p*ell+32)
        m = ceil(sqrt(float(target)))
        require(arb(m*m) >= target and arb((m-1)**2) < target,
                "Certified ceiling choice")
        a = arb.pi()/8-1/xx
        u = (ell+2*(ell+8).log())/4
        require(a > 0 and a < arb.pi()/8 and (4*a).cos() >= 2/xx,
                "Adaptive contour in strip")
        require(u <= ell/2+2, "Cutoff logarithm bound")
        en, eu = [], []
        for k in range(4):
            ni, rho, beta = index_payment(k, a, m-1, tau)
            ui, rho_u, exponent = integration_payment(k, a, u, tau)
            require(beta >= p*ell+32, "Scalable beta bound")
            require(1/(1-rho) <= 1+xx/(2*arb.pi()*m),
                    "Growing geometric denominator paid")
            require(exponent <= -arb(47)/8*ell**2-arb(181)/2*ell-364,
                    "Complete integration-tail exponent")
            # exp((pi/8-a)x)=e for this choice of contour.
            en.append(enc(arb(1).exp()*ni))
            eu.append(enc(arb(1).exp()*ui))
        rows.append({"x": x, "p": p, "N": m-1, "a": enc(a), "U": enc(u),
                     "index_normalized_errors": en,
                     "integration_normalized_errors": eu})
    return rows


def agreement_samples(bits):
    rows = []
    tol = arb(2)**(-(bits-64))
    n = 8
    u = arb(3)/2
    a = arb.pi()/16
    x = arb(41)
    for t in (arb(0), arb(1)/2):
        jets = []
        for k in range(4):
            shifted = finite_integral(k, a, n, u, t, x, tol)
            direct = finite_integral(k, arb(0), n, u, t, x, tol)
            ni, _, _ = index_payment(k, a, n, t)
            ui, _, _ = integration_payment(k, a, u, t)
            ndi, _, _ = index_payment(k, arb(0), n, t)
            udi, _, _ = integration_payment(k, arb(0), u, t)
            # Each route encloses the same normalized complete physical jet.
            shifted_scale = ((arb.pi()/8-a)*x).exp()
            direct_scale = (arb.pi()/8*x).exp()
            require(shifted_scale*shifted.rad() < arb(10)**(-40) and
                    direct_scale*direct.rad() < arb(10)**(-40),
                    "Useful selected-point quadrature accuracy")
            shifted_full = shifted_scale*(shifted+symmetric(ni+ui))
            direct_full = direct_scale*(direct+symmetric(ndi+udi))
            require(shifted_full.overlaps(direct_full),
                    "Paid shifted/direct complete-jet agreement")
            # Record quadrature radii separately from analytic omitted-domain errors.
            jets.append({"k": k, "shifted_normalized": enc(shifted_full),
                         "direct_normalized": enc(direct_full),
                         "shifted_quadrature_radius": enc(shifted_scale*shifted.rad()),
                         "shifted_analytic_payment": enc(shifted_scale*(ni+ui)),
                         "direct_quadrature_radius": enc(direct_scale*direct.rad()),
                         "direct_analytic_payment": enc(direct_scale*(ndi+udi))})
        rows.append({"t": enc(t), "x": 41, "N": n, "a": enc(a), "U": enc(u),
                     "jets": jets})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bits", type=int, default=256)
    args = parser.parse_args()
    require(args.bits >= 192, "At least 192-bit arithmetic required")
    ctx.prec = args.bits
    samples = scalable_samples()
    agreements = agreement_samples(args.bits)
    record = {"date": "2026-10-14", "intended_author": "Edward Baker",
              "llm_assistance": "Substantial", "recorded_model": "gpt-6.1-sol (Codex)",
              "recorded_reasoning_effort": "ultra", "python": platform.python_version(),
              "python_flint": flint.__version__, "bits": args.bits,
              "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "status": "All payment hypotheses and eight selected complete-jet comparisons passed",
              "scope": "Absolute tail-payment replay and implementation comparison; no stationary sign or global nonvanishing certificate",
              "scalable_samples": samples, "selected_point_agreement": agreements}
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(record["status"])
    for row in samples:
        print("x=%s N=%s k=0 normalized index error=%s" %
              (row["x"], row["N"], row["index_normalized_errors"][0]["display"]))


if __name__ == "__main__":
    main()
