#!/usr/bin/env python3
"""Floating-point replay of one finite-lane Triangle row L_N (Gomila package).

Implements, in float64/numpy, the quantity

    L_N = (1 - g - Ssum)/M - corr,
    Ssum = sum_{n=2}^{DN} (|b(n)| + g |a0(n)|) n^{-sigma},
    corr = g * sum_{n=2}^{N} bt(n) (n^{kappa} - 1) n^{y - sigma},

with b, a0 the Euler-mollified convolutions of bt(m) = exp((t/4) log^2 m),
exactly as in src/lemma_sweep_p235711.c (TRIANGLE_WEIGHT) of the audited
package.  Non-rigorous: no interval arithmetic.  Used only for replay
agreement and for sensitivity (dL/dy, dL/dt) estimates.
"""
import argparse, json, math, sys, time
import numpy as np

PRIMES = {2: [2], 3: [2, 3], 4: [2, 3, 5], 5: [2, 3, 5, 7], 6: [2, 3, 5, 7, 11]}

def bt(lnm, t):
    return np.exp(0.25 * t * lnm * lnm)

def mollifier(primes, t):
    """Return list of (d, lambda_d) with lambda_d = mu(d) prod_{p|d} bt(p)."""
    out = []
    k = len(primes)
    for mask in range(1 << k):
        d = 1; lam = 1.0
        for i, p in enumerate(primes):
            if mask >> i & 1:
                d *= p; lam *= -bt(math.log(p), t)
        out.append((d, lam))
    return out

def row(N, y, t, primes, chunk=20_000_000, verbose=False, weight='triangle'):
    moll = mollifier(primes, t)
    D = max(d for d, _ in moll)
    xN = 4 * math.pi * N * N - math.pi * t / 4
    lnx4pi = math.log(xN / (4 * math.pi))
    inner = 1 - 3 * y + 4 * y * (1 + y) / xN ** 2
    inner = max(inner, 0.0)
    p = t * lnx4pi / 4 - t * inner / (2 * xN * xN)
    sigma = (1 + y) / 2 + p
    kappa = t * y / (2 * (xN - 6))
    g = math.exp(0.02 * y - y * lnx4pi / 2)
    M = sum(abs(lam) * d ** (-sigma) for d, lam in moll)
    # precompute bt(m), m^y for m = 1..N
    m = np.arange(1, N + 1, dtype=np.float64)
    lnm = np.log(m)
    btm = bt(lnm, t)
    my = np.exp(y * lnm)
    DN = D * N
    Ssum = 0.0
    t0 = time.time()
    n0 = 2
    while n0 <= DN:
        n1 = min(n0 + chunk, DN + 1)          # chunk covers n in [n0, n1)
        size = n1 - n0
        b = np.zeros(size); a0 = np.zeros(size)
        for d, lam in moll:
            mlo = -(-n0 // d)                 # ceil(n0/d)
            mhi = min(N, (n1 - 1) // d)
            if mlo > mhi:
                continue
            start = d * mlo - n0
            sl = slice(start, start + d * (mhi - mlo) + 1, d)
            seg = btm[mlo - 1:mhi]
            b[sl] += lam * seg
            a0[sl] += lam * seg * my[mlo - 1:mhi]
        n = np.arange(n0, n1, dtype=np.float64)
        if weight == 'triangle':
            w = (np.abs(b) + g * np.abs(a0)) * np.exp(-sigma * np.log(n))
        else:  # sharp L-type weight: max(|b - g a0|, c(g) |b + g a0|)
            c = (1 - g) / (1 + g)
            w = np.maximum(np.abs(b - g * a0), c * np.abs(b + g * a0)) * np.exp(-sigma * np.log(n))
        Ssum += float(np.sum(w))
        if verbose:
            print(f"  chunk [{n0},{n1}) Ssum={Ssum:.12f} elapsed={time.time()-t0:.1f}s", file=sys.stderr)
        n0 = n1
    corr = g * float(np.sum(btm[1:] * np.expm1(kappa * lnm[1:]) * np.exp((y - sigma) * lnm[1:])))
    L = (1 - g - Ssum) / M - corr
    return dict(N=N, y=y, t=t, weight=weight, primes=primes, D=D, DN=DN, xN=xN, sigma=sigma, g=g,
                kappa=kappa, M=M, Ssum=Ssum, corr=corr, L=L, seconds=time.time() - t0)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--y2", type=str, default="87677/2500000")
    ap.add_argument("--t", type=str, default="129/800")
    ap.add_argument("--mtype", type=int, default=6)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--weight", default="triangle", choices=["triangle","sharp"])
    a = ap.parse_args()
    def frac(s):
        if "/" in s:
            u, v = s.split("/"); return float(u) / float(v)
        return float(s)
    r = row(a.N, math.sqrt(frac(a.y2)), frac(a.t), PRIMES[a.mtype], verbose=a.verbose, weight=a.weight)
    print(json.dumps(r))
