#!/usr/bin/env python3
"""Floating diagnostics for the radial electric parity/log-angle response.

Prepared for Edward Baker with substantial GPT-6 (Codex) assistance, 2026-09-25.
Exact deployed variant and reasoning effort unavailable. NumPy only. These
controls do not sample the interacting Wilson state or certify any limit.
Only a small JSON record is written; all arrays remain in memory.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np


def bump(x, phase=0.37):
    x = np.asarray(x)
    v = x / 1.3
    out = np.zeros_like(x, dtype=complex)
    inside = abs(v) < 1
    out[inside] = np.exp(-1 / (1 - v[inside] ** 2) + 1j * phase * x[inside])
    return out


def f(x):
    return bump(x)


def g(x):
    return (1 + (0.2 + 0.1j) * np.asarray(x)) * bump(x, -0.23)


def minus_i_fprime(x):
    x = np.asarray(x)
    out = np.zeros_like(x, dtype=complex)
    inside = abs(x) < 1.3
    z = x[inside]
    out[inside] = -1j * f(z) * (-2 * z / 1.3 ** 2 / (1 - (z / 1.3) ** 2) ** 2 + 0.37j)
    return out


def packet(nscale, fun=f, beta=0.0):
    n = np.arange(math.ceil(nscale * math.exp(1.3)) + 3)
    c = np.zeros(len(n), complex)
    c[1:] = fun(np.log(n[1:] / nscale)) * np.exp(1j * beta * n[1:]) / np.sqrt(n[1:])
    return c


def current(c):
    n = np.arange(1, len(c))
    out = np.zeros(len(c) + 1, complex)
    out[n + 1] += 0.5j * (n + 0.5) * c[n]
    out[n[:-1]] -= 0.5j * (n[1:] - 0.5) * c[n[1:]]
    return out


def fftconv(a, b):
    size = len(a) + len(b) - 1
    fftsize = 1 << (size - 1).bit_length()
    return np.fft.ifft(np.fft.fft(a, fftsize) * np.fft.fft(b, fftsize))[:size]


def log_angle_integrals(size):
    """J_k=int_0^pi log(theta/(2pi))*cos(k theta) dtheta.

    J_0=pi*(log(1/2)-1), J_k=-Si(k*pi)/k. For k<=16 use
    independent Gauss quadrature of sinc; otherwise asymptotics at integer pi.
    """
    out = np.zeros(size)
    out[0] = np.pi * (math.log(0.5) - 1)
    nodes, weights = np.polynomial.legendre.leggauss(192)
    for k in range(1, min(size, 17)):
        x = k * np.pi * (nodes + 1) / 2
        si = k * np.pi / 2 * np.dot(weights, np.sinc(x / np.pi))
        out[k] = -si / k
    k = np.arange(17, size)
    x = k * np.pi
    series = np.ones_like(x)
    term = np.ones_like(x)
    for j in range(1, 9):
        term *= -(2 * j) * (2 * j - 1) / x ** 2
        series += term
    si = np.pi / 2 - (-1.0) ** k * series / x
    out[k] = -si / k
    return out


def response(a, b, parity=1, integrals=None):
    """parity=+1 cosine response; parity=-1 unmodified sine control."""
    size = max(len(a), len(b))
    a = np.pad(a, (0, size - len(a)))
    b = np.pad(b, (0, size - len(b)))
    j = log_angle_integrals(2 * size) if integrals is None else integrals
    electric = np.vdot(a[1:], np.log(np.arange(1, size)) * b[1:])
    toeplitz = fftconv(b, np.r_[j[size - 1:0:-1], j[:size]])[size - 1:2 * size - 1]
    hankel = fftconv(j[:2 * size - 1], b[::-1])[size - 1:2 * size - 1]
    return electric + np.vdot(a, toeplitz + parity * hankel) / np.pi


def digamma(z):
    """Recurrence to Re(z)>=18 and eight Bernoulli asymptotic terms."""
    z = np.asarray(z, dtype=complex)
    out = np.zeros_like(z)
    for _ in range(18):
        out -= 1 / z
        z = z + 1
    out += np.log(z) - 0.5 / z
    bernoulli = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730, 7 / 6, -3617 / 510]
    for k, bk in enumerate(bernoulli, 1):
        out -= bk / (2 * k * z ** (2 * k))
    return out


def spectral_pair(left=f, right=g, alpha=0.25, step=0.05, cutoff=256):
    nodes, weights = np.polynomial.legendre.leggauss(600)
    x, w = 1.3 * nodes, 1.3 * weights
    tau = np.arange(-cutoff, cutoff + step / 2, step)
    lf, rf = np.empty(len(tau), complex), np.empty(len(tau), complex)
    for start in range(0, len(tau), 256):
        sel = slice(start, start + 256)
        kernel = np.exp(-1j * tau[sel, None] * x[None, :])
        lf[sel] = kernel @ (w * left(x))
        rf[sel] = kernel @ (w * right(x))
    values = (digamma(alpha + 0.5j * tau).real - math.log(math.pi)) * np.conj(lf) * rf
    return np.sum(values[1:-1]) * step / (2 * np.pi) + (values[0] + values[-1]) * step / (4 * np.pi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    checks, sequences = [], []

    def check(label, actual, expected, tolerance):
        error = float(abs(actual - expected))
        checks.append(dict(label=label, absolute_error=error, tolerance=tolerance,
                           passed=error <= tolerance * max(1, float(abs(expected)))))

    nodes, weights = np.polynomial.legendre.leggauss(600)
    x, w = 1.3 * nodes, 1.3 * weights
    norm = float(np.dot(w, abs(f(x)) ** 2))
    xnorm = float(np.dot(w, x * abs(f(x)) ** 2))
    derivative_norm = float(np.dot(w, abs(minus_i_fprime(x)) ** 2))
    local_constant = -0.5772156649015328606 - np.pi / 2 - 3 * np.log(2) - np.log(np.pi)
    check('contact constant', digamma(0.25).real - np.log(np.pi), local_constant, 2e-13)

    spectral = {}
    for parity, alpha in ((1, 0.25), (-1, 0.75)):
        target = spectral_pair(alpha=alpha)
        refined = spectral_pair(alpha=alpha, step=0.025, cutoff=320)
        spectral[str(parity)] = [float(refined.real), float(refined.imag)]
        check(f'Fourier quadrature refinement parity={parity}', target, refined, 2e-9)
        errors = []
        for scale in (16, 64, 256, 1024):
            measured = response(packet(scale, f), packet(scale, g), parity)
            errors.append(float(abs(measured - refined)))
        sequences.append(dict(label=f'archimedean mixed limit parity={parity}',
                              scales=[16, 64, 256, 1024], absolute_errors=errors))
        check(f'archimedean mixed limit parity={parity}', measured, refined, 2e-8)

    # Independent quadrature of the exact finite physical log-angle pairing.
    # rho is prescribed, not sampled from the Wilson measure.
    u = 24 * (nodes + 1)
    theta = np.pi * np.exp(-u)
    tw = 24 * weights * theta
    rho = (1 + 0.35 * np.cos(theta) + 0.2 * np.cos(2 * theta)) / 0.9
    av = np.array([0, 0.4 + 0.2j, -0.3j, 0.1, 0.22 - 0.13j])
    bv = np.array([0, -0.1j, 0.3, -0.12 + 0.17j, 0.08])
    ns = np.arange(1, len(av))
    chi = np.sin(ns[:, None] * theta) / np.sin(theta)
    co = np.cos(ns[:, None] * theta) / np.sin(theta)
    left = av[1:] @ chi / np.sqrt(rho)
    elog = (np.log(ns) * bv[1:]) @ chi / np.sqrt(rho)
    bl = av[1:] @ co / np.sqrt(rho)
    br = bv[1:] @ co / np.sqrt(rho)
    phys_weight = tw * 2 / np.pi * rho * np.sin(theta) ** 2
    physical = np.dot(phys_weight, np.conj(left) * elog + np.log(theta / (2 * np.pi)) * np.conj(bl) * br)
    check('actual-weight finite pairing, prescribed rho', physical, response(av, bv), 3e-11)

    # Kernel integral is independent of the finite log-angle matrix.
    gn, gw = np.polynomial.legendre.leggauss(16)
    starts = np.arange(0, 80, 0.1)
    r = (starts[:, None] + 0.05 * (gn + 1)).ravel()
    rw = np.tile(0.05 * gw, len(starts))
    kernel = np.exp(-r / 2) / (-np.expm1(-2 * r))
    for tau in (0.4, 3.0, 12.0):
        integral = 2 * np.dot(rw, kernel * (1 - np.cos(tau * r)))
        exact = (digamma(0.25 + 0.5j * tau) - digamma(0.25)).real
        check(f'archimedean difference kernel tau={tau}', integral, exact, 3e-11)
    for tau in (1000, 10000):
        measured = digamma(0.25 + 0.5j * tau).real - math.log(math.pi)
        check(f'logarithmic high-frequency asymptotic tau={tau}', measured,
              math.log(tau / (2 * math.pi)), 2e-7)

    for beta in (np.pi / 3, np.pi):
        errors = []
        target = xnorm + math.log(beta / (2 * math.pi)) * norm
        for scale in (32, 128, 512, 2048):
            c = packet(scale, beta=beta)
            measured = response(c, c).real - math.log(scale) * np.vdot(c, c).real
            errors.append(abs(measured - target))
        sequences.append(dict(label=f'nonidentity phase finite part beta={beta}',
                              scales=[32, 128, 512, 2048], absolute_errors=errors))
        check(f'phase logarithmic divergence beta={beta}', measured, target, 3e-4)

    # Haar controls for the pi-current sign and winding-two defect.
    scale = 2048
    for beta, sign in ((0.0, 1), (np.pi, -1)):
        actual = current(packet(scale, beta=beta))
        expected = sign * packet(scale, minus_i_fprime, beta)
        expected = np.pad(expected, (0, len(actual) - len(expected)))
        check(f'current orientation beta={beta}', np.linalg.norm(actual - expected), 0, 5e-5)
    original = packet(scale)
    wound = np.zeros(2 * len(original) - 1, complex)
    wound[::2] = original
    actual = current(wound)
    df = packet(scale, minus_i_fprime)
    expected = np.zeros_like(actual)
    expected[:2 * len(df):2] = df
    defect = np.linalg.norm(actual - expected) ** 2
    check('winding-two derivative defect', defect, 2 * derivative_norm, 5e-5)

    negative_controls = []
    for p in (11, 101, 1009):
        c = np.zeros(p + 1, complex)
        c[1] = c[p] = 1
        val = response(c, c).real - 2 * np.log(p)
        negative_controls.append(dict(prime=p, signed_full_core_response=float(val)))
        check(f'signed completion is negative on full core p={p}', max(val, 0), 0, 1e-13)

    record = dict(date='2026-09-25', model='GPT-6 (Codex)',
                  deployed_variant='unavailable', reasoning_effort='unavailable',
                  llm_assistance=True, status='floating diagnostics, not proofs or Wilson samples',
                  python=platform.python_version(), numpy=np.__version__,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  check_count=len(checks), all_passed=all(c['passed'] for c in checks),
                  checks=checks, convergence=sequences, spectral_targets=spectral,
                  local_constant=float(local_constant), negative_controls=negative_controls)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({k: record[k] for k in ('check_count', 'all_passed', 'local_constant')}, indent=2))
    print(json.dumps({'failed': [c for c in checks if not c['passed']]}, indent=2))
    return 0 if record['all_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
