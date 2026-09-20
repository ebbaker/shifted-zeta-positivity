#!/usr/bin/env python3
"""Complete-output finite-input diagnostics of an arithmetic window append.

NumPy only. No output projection precedes either diagonal defect norm.
Singular quadratures use the inherited arithmetic kernel and Jacobi rule.
Finite quotients approximate LOWER bounds on the true coupling norm.
These floating calculations do not certify signs or input complements.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import numpy as np

L, H, W = .5, .05, .001
GAMMA = .5772156649015328606065120900824024


def basis(x, length, n):
    rho = np.full(n, math.sqrt(2/length)); rho[0] = 1/math.sqrt(length)
    return np.cos(np.asarray(x)[..., None]*np.arange(n)*math.pi/length)*rho


def gram(a, weights, b=None):
    return a.T@(weights[:, None]*(a if b is None else b))


def inverse_sqrt(a):
    d, u = np.linalg.eigh((a+a.T)/2)
    if d[0] <= 0:
        raise ValueError('Nonpositive diagnostic metric')
    return (u/np.sqrt(d))@u.T


def norm(a):
    return float(np.linalg.svd(a, compute_uv=False)[0])


def central(length, n, order):
    """Full central form from translation correlations, not an EMA truncation."""
    z, weight = np.polynomial.legendre.leggauss(order)
    u, weight = (z+1)*length/2, weight*length/2
    k = np.arange(n)*math.pi/length
    rho = np.full(n, math.sqrt(2/length)); rho[0] = 1/math.sqrt(length)
    minus, plus = k[:, None]-k[None, :], k[:, None]+k[None, :]
    q = np.zeros((n, n))
    for t, wt in zip(u, weight):
        d = length-t
        def cint(v):
            return d*np.sinc(v*d/math.pi)
        def sint(v):
            return v*d*d/2*np.sinc(v*d/(2*math.pi))**2
        corr = .5*(np.cos(k*t)[:, None]*(cint(minus)+cint(plus))
                    -np.sin(k*t)[:, None]*(sint(minus)+sint(plus)))
        corr *= rho[:, None]*rho[None, :]
        q += wt*2*math.exp(-t/2)/(-math.expm1(-2*t))*(np.eye(n)-(corr+corr.T)/2)
    rates = 2*np.arange(int(math.ceil(24/length)))+.5
    beyond = np.sum(2*np.exp(-rates*length)/rates)
    q += (-GAMMA-math.pi/2-3*math.log(2)-math.log(math.pi)+beyond)*np.eye(n)
    b = .5
    c = 2*b*math.sinh(b*length/2)*rho/(b*b+k*k)
    s = -2*b*math.cosh(b*length/2)*rho/(b*b+k*k)
    c[1::2] = 0; s[::2] = 0
    return q+2*np.outer(c,c)-2*np.outer(s,s)


def complete_defect(pilot, ker, length, n, order, delay):
    # V phi(x) = x^w times a smooth integral in the Jacobi delay variable.
    x0, wx = pilot.gj(1+2*W, order)
    x = length*x0
    v, wv = pilot.gj(W, delay)
    tau = x[:, None]*v
    scaled = np.einsum('ij,ijk->ik', wv*pilot.gh_array(ker,tau),
                       basis(x[:, None]*(1-v),length,n))
    output_gram = length**(1+2*W)*gram(scaled,wx)
    # Independent quadrature check of the projected response, used ONLY to
    # measure the error caused by prematurely projecting the output.
    xp0,wp=pilot.gj(1+W,order)
    xp=length*xp0
    sp=np.einsum('ij,ijk->ik',wv*pilot.gh_array(ker,xp[:,None]*v),
                 basis(xp[:,None]*(1-v),length,n))
    projected = length**(1+W)*gram(basis(xp,length,n),wp,sp)
    return np.eye(n)-output_gram, output_gram-projected.T@projected


def mixed(pilot, ker, n, order, inner):
    """Integrate by u=r+t, including the entire near-join triangle."""
    q, wq = np.polynomial.legendre.leggauss(inner)
    q, wq = (q+1)/2,wq/2
    # The cross-section length u cancels the beta singularity on (0,h).
    v, weights = pilot.gj(1+W,order)
    nodes = [(H*v, H**(1+W)*weights, True)]
    z, wz = np.polynomial.legendre.leggauss(order)
    for a,b in ((H,L),(L,L+H)):
        nodes.append(((a+b)/2+(b-a)*z/2,(b-a)*wz/2,False))
    y, b0 = np.zeros((n,n)),np.zeros((n,n))
    for us, weights, first in nodes:
        gh = pilot.gh_array(ker,us)
        for u, wt, smooth_kernel in zip(us,weights,gh):
            lo, hi = max(0.,u-L), min(H,u)
            ts = lo+(hi-lo)*q
            cross = gram(basis(ts,H,n),wq,basis(L-(u-ts),L,n))
            if first:
                y += wt*smooth_kernel*cross
            else:
                y += wt*u**(W-1)*smooth_kernel*(hi-lo)*cross
                g = -2*math.exp(-2.5*u)/(-math.expm1(-2*u))+2*math.exp(u/2)
                b0 += wt*g*(hi-lo)*cross/2
    # Independent regular quadrature for central near-corner integral.
    # Its cross-section length cancels 1/u exactly, with no fractional power.
    for u,wt in zip(H*(z+1)/2,H*wz/2):
        ts=u*q
        cross=gram(basis(ts,H,n),wq,basis(L-(u-ts),L,n))
        g_times_u=-2*u*math.exp(-2.5*u)/(-math.expm1(-2*u))+2*u*math.exp(u/2)
        b0+=wt*g_times_u*cross/2
    return y,b0


def run(pilot,n,order,delay,inner):
    ker = pilot.parent.Kernel(W,24)
    e, ep = complete_defect(pilot,ker,L,n,order,delay)
    dh, hp = complete_defect(pilot,ker,H,n,order,delay)
    signs = (-1.)**np.arange(n)
    f = signs[:,None]*dh*signs[None,:]
    y,b = mixed(pilot,ker,n,order,inner)
    a,c = central(L,n,order),central(H,n,order)
    coupling = inverse_sqrt(f)@y@inverse_sqrt(e)
    instant = inverse_sqrt(c)@b@inverse_sqrt(a)
    u, sv, vt = np.linalg.svd(coupling)
    old = inverse_sqrt(e)@vt[0]
    new = inverse_sqrt(f)@u[:,0]
    old /= np.linalg.norm(old); new /= np.linalg.norm(new)
    ts=np.array([.00001,.001,.01,.05,.2,.55])
    v,wv=pilot.gj(W,24)
    def hh(t):
        return (2*math.pi)**W/math.gamma(W)*(np.sinh(t)/t)**(W-1)*np.exp(-1.5*t)
    reduced=hh(ts)-2*W*ts*np.sum(wv*np.exp((.5-W)*ts[:,None]*(1-v))*hh(ts[:,None]*v),axis=1)
    result={
        'n_each_window':n,'output_order':order,'delay_order':delay,'cross_section_order':inner,
        'cumulative_coupling_quotient':float(sv[0]),
        'instantaneous_central_coupling_quotient':norm(instant),
        'mixed_norm_compression':norm(y),
        'mixed_norm_compression_div_scalar_anchor':norm(y)/.000049998,
        'min_old_defect_over_2omega':float(np.linalg.eigvalsh(e)[0]/(2*W)),
        'min_new_output_defect_over_2omega':float(np.linalg.eigvalsh(f)[0]/(2*W)),
        'min_old_central_form':float(np.linalg.eigvalsh(a)[0]),
        'min_new_central_form':float(np.linalg.eigvalsh(c)[0]),
        'old_output_projection_loss_norm':norm(ep),
        'new_output_projection_loss_norm':norm(hp),
        'cumulative_weak_pair':{
            'old_defect_per_unit_norm':float(old@e@old),
            'new_output_defect_per_unit_norm':float(new@f@new),
            'mixed_bilinear_per_unit_norm':float(new@y@old),
            'old_cosine_coefficients':old.tolist(),
            'new_cosine_coefficients':new.tolist()},
        'controls':{
            'signed_parent_vs_absorbed_kernel_max_error':float(np.max(abs(reduced-pilot.gh_array(ker,ts)))),
            'central_cross_vs_negative_cumulative_over_2omega_norm':norm(b+y/(2*W)),
            'central_parity_error':float(np.max(abs(a-signs[:,None]*a*signs[None,:])))}
    }
    assert result['controls']['signed_parent_vs_absorbed_kernel_max_error'] < 1e-10
    assert result['controls']['central_parity_error'] < 1e-9
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repository',type=Path)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.repository is None:
        args.repository=Path(__file__).resolve().parent.parents[4]
    src=args.repository/'papers/susy-positivity/investigations/critical-path/numerics/adaptive_ema_pilot.py'
    spec=importlib.util.spec_from_file_location('pilot',src)
    pilot=importlib.util.module_from_spec(spec);spec.loader.exec_module(pilot)
    configs=[(8,96,96,48),(16,144,144,64),(16,208,208,96),
             (32,240,240,128),(32,320,320,160)]
    rows=[]
    for cfg in configs:
        row=run(pilot,*cfg); rows.append(row)
        print(json.dumps({k:row[k] for k in ('n_each_window','output_order',
              'cumulative_coupling_quotient','instantaneous_central_coupling_quotient')}),flush=True)
    out={'date':'2026-09-20','model':'OpenAI GPT-6 (Codex; developer-provided identity)',
         'reasoning_effort':'Not exposed in this session; not inferred',
         'status':'Floating finite-input diagnostics, not certificates; no output projection in defect norms',
         'python':platform.python_version(),'numpy':np.__version__,
         'parameters':{'L':'1/2','h':'1/20','omega':'1/1000'},'runs':rows,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'inherited_source_sha256':{str(p.relative_to(args.repository)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (src,pilot.PARENT)}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')


if __name__=='__main__':
    main()
