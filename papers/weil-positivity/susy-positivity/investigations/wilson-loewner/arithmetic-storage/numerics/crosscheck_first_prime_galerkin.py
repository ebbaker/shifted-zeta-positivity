#!/usr/bin/env python3
"""Independent floating cross-check of the first-prime session (FLOATING DIAGNOSTICS ONLY).

A separately written Galerkin model of the central Weil form on L^2(0,R):
    Q[F] = (w0 + int_R^inf nu0)|F|^2 + int_0^R nu0(u)(|F|^2 - Re<F,S_u F>) du
           + 2 F^(i/2) F^(-i/2) - sum_{log n<R} (2 Lambda(n)/sqrt n) Re<F, S_{log n} F>,
    nu0(u) = 2 e^{-u/2}/(1 - e^{-2u}),  w0 = psi(1/4) - log pi,
in orthonormal Legendre bases on one window or on the split (0,L) + (L,R).  The
gamma form is integrated in the translation variable u against exact polynomial
correlations, independently of the session's cosine/exponential-series formulas
and of weil-depth's moment representation.  Galerkin values are upper bounds for
spectral bottoms and lower bounds for the relative coupling sup; nothing here is a
certificate.

Prepared for Edward Baker, 24 September 2026, by Claude (Anthropic); session
configured as claude-fable-5-1, runtime-reported serving model Claude Opus 5.5
(claude-opus-5-5); the serving model may differ.  Reasoning effort not exposed.
"""
import argparse, hashlib, json, platform, sys, time
from math import log, sqrt, pi
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
import scipy
from scipy.special import digamma
from scipy.optimize import brentq
import scipy.linalg as sl

W0 = float(digamma(0.25) - log(pi))


def mangoldt(n):
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return log(p) if m == 1 else 0.0
    return 0.0


def leg(x, a, b, N):
    t = 2.0*(x - a)/(b - a) - 1.0
    P = np.zeros((N, x.size)); P[0] = 1.0
    if N > 1:
        P[1] = t
    for k in range(1, N - 1):
        P[k + 1] = ((2*k + 1)*t*P[k] - k*P[k - 1])/(k + 1)
    out = P*np.sqrt((2*np.arange(N) + 1)/(b - a))[:, None]
    out[:, (x < a - 1e-15) | (x > b + 1e-15)] = 0.0
    return out


class Basis:
    def __init__(self, windows, Ns):
        self.windows, self.Ns = windows, Ns
        self.off = np.cumsum([0] + list(Ns)); self.dim = int(self.off[-1])

    def blocks(self):
        for a, (w, N) in enumerate(zip(self.windows, self.Ns)):
            yield w, N, slice(int(self.off[a]), int(self.off[a + 1]))


def corr(u, B, nx):
    C = np.zeros((B.dim, B.dim)); xg, wg = leggauss(nx)
    for wa, Na, sa in B.blocks():
        for wb, Nb, sb in B.blocks():
            lo, hi = max(wa[0], wb[0] + u), min(wa[1], wb[1] + u)
            if hi > lo:
                x = lo + (hi - lo)*(xg + 1)/2; w = wg*(hi - lo)/2
                C[sa, sb] = (leg(x, *wa, Na)*w) @ leg(x - u, *wb, Nb).T
    return C


def nu_complete(u):
    return 2*np.exp(-u/2)/(-np.expm1(-2*u))


def nu_tower(M):
    a = 2*np.arange(M) + 0.5
    return lambda u: float(np.sum(2*np.exp(-a*u)))


def assemble(B, R, M=None):
    """(archimedean+pole matrix, prime matrix) on basis B; M = tower truncation or None."""
    nx = max(B.Ns) + 10; nq = 2*max(B.Ns) + 60
    nuf = nu_complete if M is None else nu_tower(M)
    a = 2*np.arange(M if M else 4000) + 0.5
    tail = float(np.sum(2*np.exp(-a*R)/a))
    ends = sorted({w[0] for w in B.windows} | {w[1] for w in B.windows})
    bps = sorted({abs(p - q) for p in ends for q in ends} | {0.0, R})
    ug, uw = leggauss(nq); G = np.zeros((B.dim, B.dim)); I = np.eye(B.dim)
    for lo, hi in zip(bps[:-1], bps[1:]):
        if hi - lo < 1e-14:
            continue
        for u, w in zip(lo + (hi - lo)*(ug + 1)/2, uw*(hi - lo)/2):
            C = corr(u, B, nx); G += w*nuf(u)*(I - (C + C.T)/2)
    xg, wg = leggauss(300); ep = np.zeros(B.dim); em = np.zeros(B.dim)
    for wa, Na, sa in B.blocks():
        x = wa[0] + (wa[1] - wa[0])*(xg + 1)/2; w = wg*(wa[1] - wa[0])/2
        Phi = leg(x, *wa, Na); ep[sa] = (Phi*w) @ np.exp(x/2); em[sa] = (Phi*w) @ np.exp(-x/2)
    Qa = (W0 + tail)*I + G + np.outer(ep, em) + np.outer(em, ep)
    P = np.zeros((B.dim, B.dim)); n = 2
    while log(n) < R:
        lam = mangoldt(n)
        if lam > 0:
            C = corr(log(n), B, nx); P -= (2*lam/sqrt(n))*(C + C.T)/2
        n += 1
    return Qa, P


def project(fun, B, nx=200):
    xg, wg = leggauss(nx); c = np.zeros(B.dim)
    for wa, Na, sa in B.blocks():
        x = wa[0] + (wa[1] - wa[0])*(xg + 1)/2; w = wg*(wa[1] - wa[0])/2
        c[sa] = (leg(x, *wa, Na)*w) @ fun(x)
    return c


def lam_min(Q):
    return float(np.linalg.eigvalsh(Q)[0])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--quick', action='store_true', help='smaller bases (for a fast replay)')
    args = ap.parse_args()
    t0 = time.time(); out = {}
    Ns = [40, 64] if args.quick else [48, 64, 80]
    # 1. single-window spectral bottoms (normalization check against weil-depth)
    rows = []
    for R in [0.2, 0.55, log(2), 0.75, log(3)]:
        for N in Ns:
            Qa, P = assemble(Basis([(0.0, R)], [N]), R)
            rows.append({'R': R, 'N': N, 'lambda_min': lam_min(Qa + P)})
        print('bottom', R, rows[-1]['lambda_min'], flush=True)
    out['single_window_bottoms'] = rows
    # 2. witnesses of the first session
    L, h = 0.55, 0.2; R = L + h
    psi = lambda x: np.cos(pi*x/R) - 0.27*np.cos(3*pi*x/R) - 0.1*np.cos(5*pi*x/R) - 0.056*np.cos(7*pi*x/R)
    B = Basis([(0.0, R)], [40]); Qa, P = assemble(B, R); c = project(psi, B)
    out['psi_witness'] = {'norm2': float(c @ c), 'Q_arch': float(c @ Qa @ c), 'prime': float(c @ P @ c),
                          'Q_complete': float(c @ (Qa + P) @ c)}
    f = lambda y: 1.061 - 0.842*np.cos(pi*y/L) - 0.271*np.cos(2*pi*y/L)      # reflected r = L - y
    v = lambda x: 0.809 + 0.592*np.cos(pi*(x - L)/h) + 0.014*np.cos(2*pi*(x - L)/h)
    N = 24; B = Basis([(0.0, L), (L, R)], [N, N]); Qa, P = assemble(B, R); Ta, _ = assemble(B, R, M=128)
    c = np.concatenate([project(f, Basis([(0.0, L)], [N])), project(v, Basis([(L, R)], [N]))])
    s1, s2 = slice(0, N), slice(N, 2*N); Qf = Qa + P
    out['fv_witness'] = {'norm2': float(c @ c), 'complete': float(c @ Qf @ c),
                         'proxy_M128': float(c[s1] @ Ta[s1, s1] @ c[s1] + c[s2] @ Ta[s2, s2] @ c[s2] + 2*c[s1] @ Qf[s1, s2] @ c[s2])}
    print('witnesses', out['psi_witness'], out['fv_witness'], flush=True)
    # 3. relative couplings at the split (11/20, 1/5)
    rel = []
    for N in ([16, 32] if args.quick else [16, 32, 48]):
        B = Basis([(0.0, L), (L, R)], [N, N]); Qa, P = assemble(B, R)
        s1, s2 = slice(0, N), slice(N, 2*N); Qf = Qa + P
        iA = sl.fractional_matrix_power(Qf[s1, s1], -0.5).real; iC = sl.fractional_matrix_power(Qf[s2, s2], -0.5).real
        k = lambda Hm: float(np.linalg.norm(iC @ Hm @ iA, 2))
        rel.append({'N_per_window': N, 'arch': k(-Qa[s2, s1]), 'prime': k(-P[s2, s1]), 'complete': k(-Qf[s2, s1]),
                    'lambda_min_joined': lam_min(Qf)})
        print('kappa', rel[-1], flush=True)
    out['relative_couplings'] = rel
    # 4. prime-free threshold and first-prime admissible weight interval
    def arch_bottom(Rv, N=64):
        Qa, _ = assemble(Basis([(0.0, Rv)], [N]), Rv); return lam_min(Qa)
    out['R_A_galerkin_N64'] = brentq(arch_bottom, 0.72, 0.75, xtol=1e-10)
    win = []
    for Rv in [0.75, 0.8, 0.9, 1.0, log(3) - 1e-12]:
        Qa, P = assemble(Basis([(0.0, Rv)], [64]), Rv)
        g = lambda s: lam_min(Qa + s*P)
        def edge(direction):
            step = 1e-9
            while g(1 + direction*step) > 0:
                step *= 2
            return brentq(g, 1 + direction*step/2, 1 + direction*step, xtol=1e-15)
        win.append({'R': Rv, 's_interval': [edge(-1), edge(+1)], 'lambda_min_s1': g(1.0), 'lambda_min_s0': g(0.0)})
        print('window', win[-1], flush=True)
    out['admissible_prime2_weight'] = win
    result = {'date': '2026-09-24',
              'model': 'Claude (Anthropic); session configured claude-fable-5-1; runtime-reported serving model Claude Opus 5.5 (claude-opus-5-5); serving model may differ',
              'reasoning_effort': 'not exposed', 'status': 'FLOATING DIAGNOSTICS; not certificates',
              'results': out, 'runtime': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'elapsed_seconds': time.time() - t0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
