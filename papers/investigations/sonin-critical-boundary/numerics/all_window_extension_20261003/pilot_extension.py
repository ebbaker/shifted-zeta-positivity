#!/usr/bin/env python3
"""Bounded floating preflight at L=6/5; this script does not certify a sign.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and reasoning effort are not exposed.
Only two prescribed lambda/cutoff configurations are examined. Both project out
full analytic moments before Legendre compression, retaining both parities.
No large matrices are saved; this source regenerates every diagnostic.
"""
import argparse
import hashlib
import json
import math
import platform
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.special import digamma, gammaln, spherical_in, spherical_jn
from numpy.polynomial.legendre import legder, leggauss, legval

L = 6 / 5
CONFIGS = ((1.0, 164.0, 160), (0.5, 100.0, 100))


def active_prime_powers(length):
    """Complete positive amplitudes for n=p^m with log(n)<length."""
    limit = math.ceil(math.exp(length))
    rows = []
    for p in range(2, limit):
        if any(p % j == 0 for j in range(2, math.isqrt(p) + 1)):
            continue
        power = p
        m = 1
        while math.log(power) < length:
            rows.append((p, m, power, math.log(power), 2 * math.log(p) / math.sqrt(power)))
            power *= p
            m += 1
    return rows


ARITHMETIC = active_prime_powers(L)
C = sum(row[4] for row in ARITHMETIC)


def gamma(t):
    return digamma(0.25 + 0.5j * np.asarray(t)).real - np.log(np.pi)


def multiplier(t):
    ans = gamma(t)
    for _, _, _, delay, amplitude in ARITHMETIC:
        ans -= amplitude * np.cos(delay * t)
    return ans


class Projection:
    """Coefficients of exact P_E exp(i L t y), y in (-1/2,1/2)."""
    def __init__(self, rank):
        self.rank = rank
        self.n = np.arange(rank)
        self.a = L / 4
        self.alpha = L / 2
        self.sh, self.ch = np.sinh(self.a), np.cosh(self.a)
        self.mean = self.sh / self.a
        self.ns = np.sinh(2 * self.a) / (4 * self.a) - 0.5
        self.nc = np.sinh(2 * self.a) / (4 * self.a) + 0.5 - self.mean**2
        raw = np.sqrt(2 * self.n + 1) * spherical_in(self.n, self.a)
        self.us = np.where(self.n % 2, raw / np.sqrt(self.ns), 0)
        self.uc = np.where((self.n > 0) & (self.n % 2 == 0), raw / np.sqrt(self.nc), 0)

    def planes(self, t):
        t = np.asarray(t)
        omega = L * t
        v = omega / 2
        denom = self.alpha**2 + omega**2
        bs = 2 * (self.alpha * self.ch * np.sin(v) - omega * self.sh * np.cos(v)) / denom
        bc = 2 * (self.alpha * self.sh * np.cos(v) + omega * self.ch * np.sin(v)) / denom
        p = (np.sqrt(2 * self.n[:, None] + 1)
             * spherical_jn(self.n[:, None], v[None, :])
             * (-1.0) ** (self.n[:, None] // 2))
        p -= self.us[:, None] * bs[None, :] / np.sqrt(self.ns)
        p -= self.uc[:, None] * (bc - self.mean * np.sinc(v / np.pi))[None, :] / np.sqrt(self.nc)
        p[0] = 0
        return p

    def projected_norm2(self, source):
        return float(source @ source - source[0]**2 - (source @ self.us)**2 - (source @ self.uc)**2)

    def endpoint_tail_constants(self, source):
        """Analytic upper bounds after two integrations by parts, floated here.

        For the normalized reference source f=P_E source, b0 is the endpoint
        absolute sum and b1 is endpoint-derivative absolute sum + ||f''||_1.
        Triangle/Cauchy estimates replace the latter by an explicit L2 bound.
        """
        source = source / np.sqrt(self.projected_norm2(source))
        mus, muc = source @ self.us, source @ self.uc
        co = source * np.sqrt(2 * self.n + 1)
        dco, ddco = 2 * legder(co), 4 * legder(co, 2)
        b0, b1 = 0.0, 0.0
        for z in [-1.0, 1.0]:
            val = (legval(z, co) - source[0]
                   - mus * np.sinh(self.a * z) / np.sqrt(self.ns)
                   - muc * (np.cosh(self.a * z) - self.mean) / np.sqrt(self.nc))
            der = (legval(z, dco)
                   - mus * self.alpha * np.cosh(self.a * z) / np.sqrt(self.ns)
                   - muc * self.alpha * np.sinh(self.a * z) / np.sqrt(self.nc))
            b0 += abs(val)
            b1 += abs(der)
        ddnorm = np.sqrt(np.sum(ddco**2 / (2 * np.arange(len(ddco)) + 1)))
        ddnorm += abs(mus) * self.alpha**2
        ddnorm += abs(muc) * self.alpha**2 * np.sqrt(1 + self.mean**2 / self.nc)
        return float(b0), float(b1 + ddnorm)


def plane_tail(rank, z):
    ratio = z*z / ((2*rank+1)*(2*rank+3))
    if ratio >= 1:
        return math.inf
    logdf = gammaln(2*rank+2) - rank*np.log(2) - gammaln(rank+1)
    return float(np.exp(0.5 * (np.log(2*rank+1)+2*rank*np.log(z)-2*logdf-np.log1p(-ratio))))


def error_preflight(proj, T, nodes, signed_wabs):
    """Floating evaluation of analytic full-space errors; no outward rounding."""
    h = T / nodes
    v1 = float(gamma(T) - gamma(0) + T * sum(row[4]*row[3] for row in ARITHMETIC))
    v2 = 15*np.sqrt(3)/2 + T*sum(row[4]*row[3]**2 for row in ARITHMETIC)
    wbound = signed_wabs + h*v1/2
    delta = (plane_tail(proj.rank, L*T/2)
             + np.exp(proj.a)*plane_tail(proj.rank, proj.a)
             * (1/np.sqrt(proj.ns)+1/np.sqrt(proj.nc)))
    quad = L*h*h/(8*np.pi)*(v2+2*L/np.sqrt(3)*v1
                           +L*L*(1/np.sqrt(20)+1/6)*wbound)
    trunc = 2*L*delta*wbound/np.pi
    return dict(nodes=nodes, rank=proj.rank, cutoff=T, signed_variation=v1,
                integrated_second_derivative_majorant=float(v2),
                signed_absolute_weight_upper_estimate=float(wbound),
                projected_plane_tail_estimate=float(delta),
                smooth_midpoint_error_estimate=float(quad),
                truncation_error_estimate=float(trunc),
                total_error_estimate=float(quad+trunc))


def actual_q_diagnostics(proj, sources, cutoffs=(1024, 2048), order=16):
    """Finite GL quadrature plus a stated analytic positive tail majorant.

    q>=lambda>0 after the corresponding certified cutoff is a separate
    arithmetic check. For U>=1, the digamma series and the integral test give
    gamma(t)<=gamma(0)+4+0.5 log(1+4t^2)<=log(t)+b-C for t>=U.
    Each returned tail upper estimate evaluates the exact formula in floats;
    finite quadrature is diagnostic, not validated.
    """
    gnodes, gweights = leggauss(order)
    accum = np.zeros(len(sources))
    result = []
    norms = np.array([proj.projected_norm2(s) for s in sources])
    sc = np.array(sources)
    const = [proj.endpoint_tail_constants(s) for s in sources]
    previous = 0
    for U in cutoffs:
        for start in range(previous, U, 64):
            ends = np.arange(start, min(start+64, U))
            t = (ends[:, None]+(gnodes[None, :]+1)/2).ravel()
            w = np.tile(gweights/2, len(ends))
            transform = sc @ proj.planes(t)
            vals = (transform**2 @ (w*multiplier(t))) * L/np.pi / norms
            accum += vals
        b = float(gamma(0)+4+0.5*np.log(4+U**-2)+C)
        def integral(k):
            return U**(1-k)*((np.log(U)+b)/(k-1)+1/(k-1)**2)
        tails=[]
        for b0,b1 in const:
            tails.append((b0*b0/L*integral(2)+2*b0*b1/L**2*integral(3)
                          +b1*b1/L**3*integral(4))/np.pi)
        result.append(dict(cutoff=U, gauss_order_per_unit=order,
                           finite_q_values=accum.tolist(),
                           positive_tail_upper_estimates=tails))
        previous=U
    return dict(source_order=['raw_even', 'raw_odd', 'signed_worst'],
                endpoint_constants=[dict(b0=x,b1=y) for x,y in const],
                quadrature=result,
                limitations=['Source is the exact three-moment projection of a finite Legendre polynomial, normalized in L2; it lies in the form closure and is not itself compactly smooth.',
                             'Finite quadrature and tail-bound evaluation use ordinary floating arithmetic; this is not an outward source-value certificate.'])


def run_case(lam, T, rank, nodes, diagnostic):
    proj=Projection(rank)
    matrices={mode:[np.zeros((rank//2,rank//2)) for _ in range(2)] for mode in ['raw','signed']}
    wm={mode:0.0 for mode in ['raw','signed_abs']}
    h=T/nodes
    for k in range(0,nodes,2048):
        t=(np.arange(k,min(k+2048,nodes))+.5)*h
        p=proj.planes(t)
        signed=lam-multiplier(t)
        wm['raw']+=h*np.maximum(signed,0).sum()
        wm['signed_abs']+=h*np.abs(signed).sum()
        for mode,w in [('raw',np.maximum(signed,0)),('signed',signed)]:
            for parity in [0,1]:
                x=p[parity::2]
                matrices[mode][parity]+=(x*w)@x.T*(L*h/np.pi)
    spec={}; eigenvectors={}
    for mode in matrices:
        spec[mode]=[]; eigenvectors[mode]=[]
        for mat in matrices[mode]:
            ev,vec=eigh(mat,subset_by_index=[rank//2-1,rank//2-1])
            spec[mode].append(float(ev[0]))
            eigenvectors[mode].append(vec[:,0])
    directions=[];sources=[]
    for parity in [0,1]:
        vec=eigenvectors['raw'][parity]
        source=np.zeros(rank);source[parity::2]=vec
        norm2=proj.projected_norm2(source)
        signed_ev=float(vec@matrices['signed'][parity]@vec/norm2)
        raw_ev=float(vec@matrices['raw'][parity]@vec/norm2)
        sources.append(source)
        directions.append(dict(parity=['even','odd'][parity],full_projected_norm2=norm2,
            raw_lower=lam-raw_ev, signed_full_band_lower=lam-signed_ev,
            recaptured_positive_energy=raw_ev-signed_ev,
            finite_polynomial_legendre_coefficients=source.tolist()))
    worst_parity=int(np.argmax(spec['signed']))
    worst=np.zeros(rank);worst[worst_parity::2]=eigenvectors['signed'][worst_parity]
    sources.append(worst)
    result=dict(L='6/5',lambda_=lam,cutoff=T,rank=rank,nodes=nodes,
        cutoff_margin=float(gamma(T)-lam-C),top_eigenvalues=spec,
        raw_apparent_gap=lam-max(spec['raw']),signed_apparent_gap=lam-max(spec['signed']),
        weights={k:float(v) for k,v in wm.items()},
        error_preflights=[error_preflight(proj,T,n,wm['signed_abs']) for n in [20000,30000,40000]],
        raw_worst_directions=directions,
        signed_worst_direction=dict(parity=['even','odd'][worst_parity],
                                    finite_polynomial_legendre_coefficients=worst.tolist()))
    if diagnostic:
        result['actual_q_diagnostics']=actual_q_diagnostics(proj,sources)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--nodes',type=int,default=10000)
    parser.add_argument('--actual-q',action='store_true')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.nodes < 1000: parser.error('At least 1000 nodes required for this bounded preflight')
    start=time.time()
    cases=[]
    for config in CONFIGS:
        case=run_case(*config,args.nodes,args.actual_q)
        cases.append(case)
        print(json.dumps({k:case[k] for k in ['lambda_','cutoff','rank','nodes','top_eigenvalues','raw_apparent_gap','signed_apparent_gap']}),flush=True)
    record=dict(status='FLOATING_DIAGNOSTIC_NOT_A_CERTIFICATE', date='2026-10-03',
        model='GPT-6 (Codex)',serving_variant='not exposed',reasoning_effort='not exposed',
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        runtime=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        seconds=time.time()-start,active_prime_powers=[dict(p=p,m=m,n=n,delay=a,amplitude=c) for p,m,n,a,c in ARITHMETIC],
        absolute_prime_amplitude=C,constraints=['mean','exp(x/2)','exp(-x/2)'],
        reference_interval=['-1/2','1/2'],cases=cases,
        limitations=['Only L=6/5 and the two predetermined lambda/cutoff configurations were examined.',
                     'All matrices and source diagnostics use floating point; outward LDL and independent full-space bounds are required for certification.',
                     'The signed operator recaptures positive energy but retains the same absolute-amplitude tail cutoff; it does not remove the all-window cost obstruction.'])
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.output),seconds=record['seconds'])),flush=True)


if __name__=='__main__': main()
