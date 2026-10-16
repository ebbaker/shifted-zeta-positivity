#!/usr/bin/env python3
"""Exploratory central-energy multiplication norms. No continuum sign certificate.

Reuses the v0.3 paper's exact polynomial/moment routines to assemble only the
retained form (including two extra output modes for coordinate multiplication).
Arb builds the entries; mpmath computes diagnostic generalized eigenvalues.
The finite-input values are NOT upper bounds for the full energy norm.
"""
import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
import mpmath as mp
from flint import arb as A, arb_mat as AM, ctx

DEFAULT_SOURCE = str(Path(__file__).with_name('reference_certify_arb.py'))

def load_source(path):
    spec = importlib.util.spec_from_file_location('paper_certificate', path)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    return c

def midpoint(x):
    m, e = x.mid().man_exp()
    return mp.mpf(int(m))*mp.mpf(2)**int(e)

def head(c, log_horizon, n, degree, omega='0', return_balls=False):
    L, w = A(log_horizon).log(), A(omega)
    kmax = n+degree
    base = c.profile(degree)
    # G_omega(t)=cosh(omega*t) G_0(t), exactly at the kernel level.
    g = [sum((c.rat(base[j-2*k])*w**(2*k)/math.factorial(2*k)
              for k in range(j//2+1)), A(0)) for j in range(degree+1)]
    p = AM([[(-1)**(i+k)*math.comb(i,k)*math.comb(i+k,k) if k <= i else 0
             for k in range(n)] for i in range(n)])
    b = AM(n,kmax)
    ell = A.const_euler()+(2*A.pi()*L).log()
    h = Fraction(0)
    for k in range(n):
        if k:
            h += Fraction(1,k)
        b[k,k] = ell-c.rat(h)
        beta = Fraction(1,k+1)
        for j in range(1,degree+1):
            if j > 1:
                beta *= Fraction(j-1,j+k)
            b[k,k+j] = g[j]*c.rat(beta)*L**j
    q = p*b
    d = p*c.moment(n,kmax,'plain')*q.transpose()+p*c.moment(n,n,'log')*p.transpose()
    for integer,prime,_ in c.prime_powers(L,log_horizon):
        delay = A(integer).log()
        delta = delay/L
        tr = AM([[math.comb(k,r)*(-delta)**(k-r) if r <= k else 0
                  for r in range(n)] for k in range(n)])
        v = (p*tr)*(2*A(prime).log()/A(integer).sqrt()*(w*delay).cosh())
        d += p*c.moment(n,n,'tail',delta)*v.transpose()
    scales = [A(2*i+1).sqrt() for i in range(n)]
    Q = AM(n,n)
    for i in range(n):
        for j in range(n):
            z = -(d[i,j]+d[j,i])*scales[i]*scales[j]/2
            if (i+j)%2:
                assert z.contains(0)
                z = A(0)
            Q[i,j] = z
    if return_balls:
        return Q
    return mp.matrix([[midpoint(Q[i,j]) for j in range(n)] for i in range(n)])

def take(q, rows, cols=None):
    if cols is None:
        cols = rows
    return mp.matrix([[q[i,j] for j in cols] for i in rows])

def run(c, integer, n, degree, shifts):
    total = n+2
    L = mp.log(integer)
    Q = head(c,integer,total,degree)
    X = mp.matrix(total)
    for j in range(total-1):
        x = L*(j+1)/(2*mp.sqrt((2*j+1)*(2*j+3)))
        X[j,j+1] = X[j+1,j] = x
    # Extra two modes make Q[Xf] and <X^2 f,Qf> exact within the profile model.
    X2 = X*X
    B = (X2*Q+Q*X2)/2-X*Q*X
    modes = list(range(n))
    XX = (X*Q*X)
    out = {'log_horizon':integer,'input_modes':n,'profile_degree':degree,
           'precision_bits':ctx.prec,'eigensolver_digits':mp.mp.dps,'sectors':{}}
    for parity,name in [(0,'even'),(1,'odd')]:
        ids = list(range(parity,n,2))
        q = take(Q,ids)
        eig,vec = mp.eigsy(q)
        assert eig[0] > 0
        v = vec[:,0]
        t = take(XX,ids)
        r = mp.diag([1/mp.sqrt(x) for x in eig])
        energy_X = r*vec.T*t*vec*r
        energy_X = (energy_X+energy_X.T)/2
        ek = mp.eigsy(energy_X,eigvals_only=True)
        kappa = mp.sqrt(ek[-1,0])
        curvature = (v.T*take(B,ids)*v)[0]
        curvature_scale = mp.sqrt(eig[0]/(-curvature)) if curvature < 0 else None
        out['sectors'][name] = {
            'head_minimum':mp.nstr(eig[0],24),
            'coordinate_energy_norm_finite_input':mp.nstr(kappa,24),
            'pi_over_4kappa_diagnostic_not_safe_bound':mp.nstr(mp.pi/(4*kappa),18),
            'ground_vector_shift_quadratic_coefficient':mp.nstr(curvature,24),
            'quadratic_root_diagnostic':mp.nstr(curvature_scale,18) if curvature_scale else None}
    # Entrywise check of the exact double-commutator identity for the w^2 term,
    # using a small finite difference with O(w^2) error after division.
    eps = mp.mpf('1e-12')
    shifted = head(c,integer,total,degree,str(eps))
    fd = (shifted-Q)/(eps**2)
    bb = take(B,modes)
    residual = take(fd,modes)-bb
    out['commutator_finite_difference_max_error'] = mp.nstr(max(abs(x) for x in residual),12)
    out['shifted_head_minima_diagnostic'] = {}
    for shift in shifts:
        qs = head(c,integer,n,degree,shift)
        out['shifted_head_minima_diagnostic'][shift] = {
            name:mp.nstr(mp.eigsy(take(qs,list(range(parity,n,2))),eigvals_only=True)[0],18)
            for parity,name in [(0,'even'),(1,'odd')]}
    print(json.dumps(out),flush=True)
    return out

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source',default=DEFAULT_SOURCE)
    p.add_argument('--horizons',type=int,nargs='+',default=[2,3,5,7])
    p.add_argument('--n',type=int,default=64)
    p.add_argument('--degree',type=int,default=220)
    p.add_argument('--bits',type=int,default=1536)
    p.add_argument('--digits',type=int,default=85)
    p.add_argument('--shifts',nargs='*',default=[])
    p.add_argument('--output',required=True)
    args = p.parse_args()
    ctx.prec = args.bits
    mp.mp.dps = args.digits
    c = load_source(args.source)
    results = []
    for horizon in args.horizons:
        results.append(run(c,horizon,args.n,args.degree,args.shifts))
        Path(args.output).write_text(json.dumps({
            'status':'Exploratory finite-input diagnostics; no new positivity or energy-norm upper certificate.',
            'source_commit':'a566944dc1be2899e37fce3d0e857516ced33d8f',
            'results':results},indent=2)+'\n')

if __name__ == '__main__':
    main()
