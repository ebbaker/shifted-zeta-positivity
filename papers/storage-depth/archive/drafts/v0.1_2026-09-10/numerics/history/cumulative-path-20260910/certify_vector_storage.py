#!/usr/bin/env python3
"""Full-output storage for an exact polynomial input, with Arb enclosures.

This certifies ONE Rayleigh quotient of I-V*V, never its positivity on all
inputs. The kernel and arithmetic normalization is the Weil-depth v0.3 one.
The analytic profile remainder is proved in cumulative_storage_path.md.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import time
import flint
from flint import arb as A, arb_poly as P, arb_series as S, ctx

HERE = Path(__file__).resolve().parent
DEFAULT_VECTOR = HERE.parent/'critical-path-20260910/generator_witness_log7.json'

def rat(s):
    f = Fraction(s)
    return A(f.numerator)/f.denominator

def profile(w, degree):
    # sinh(t)/t needs one extra term before division by t.
    ctx.cap = degree+2
    t = S([0,1],prec=degree+2)
    sinhc = ((t.exp()-(-t).exp())/2)/t
    g = (t/2+(w-1)*sinhc.log()).exp()
    a, b = A(1)/2-w, A(1)/2+w
    ya, yb = A(1), A(1)
    out = [A(1)]
    for j in range(1,degree+1):
        out.append(g[j]-4*(a*ya+b*yb))
        ya = (w*g[j]+a*ya)/(w+j)
        yb = (w*g[j]-b*yb)/(w+j)
    return out

def gamma_output(poly, L, w, degree):
    g = profile(w,degree)
    lp = [L**j for j in range(degree+1)]
    result = [A(0) for _ in range(len(poly)+degree)]
    factor = (2*A.pi()*L)**w/(1+w).gamma()
    for k,ak in enumerate(poly):
        if k:
            factor *= A(k)/(w+k)
        ratio = A(1)
        for j in range(degree+1):
            if j:
                ratio *= (w+j-1)/(w+k+j)
            result[k+j] += ak*factor*g[j]*lp[j]*ratio
    return P(result)

def distinct_primes(n):
    out = []
    for p in range(2,n+1):
        if n%p == 0:
            out.append(p)
            while n%p == 0:
                n //= p
        if n == 1:
            break
    return out

def delays(integer,L,w):
    out = [(A(0),A(1),1)]
    for n in range(2,integer):
        b = A(n)**(w-A(1)/2)
        for p in distinct_primes(n):
            b *= -(-2*w*A(p).log()).expm1()
        out.append((A(n).log()/L,b,n))
    return out

def mixed_moments(d,ell,w,degree):
    # An exact integration-by-parts recurrence. High precision is needed
    # when d/ell>1; enclosures, not midpoints, control all cancellation.
    r = ell/(ell+d)
    initial = ell**(w+1)*(ell+d)**w/(w+1)*r.hypgeom_2f1(-w,1,w+2)
    out = [initial]
    endpoint = ell**(w+1)*(ell+d)**(w+1)
    for k in range(degree):
        out.append((endpoint-d*(k+w+1)*out[-1])/(k+2*w+2))
        endpoint *= ell
    assert all(x > 0 for x in out), 'Moment recurrence requires more precision'
    return out

def full_norm_sq(p,ds,w):
    total = A(0)
    square = p*p
    for i,(di,bi,ni) in enumerate(ds):
        ell = 1-di
        v = ell**(2*w+1)
        diagonal = A(0)
        for k,c in enumerate(square.coeffs()):
            diagonal += c*v/(k+2*w+1)
            v *= ell
        assert diagonal > 0
        total += bi*bi*diagonal
        for dj,bj,nj in ds[i+1:]:
            d,ell = dj-di,1-dj
            product = p*p(P([d,1]))
            moments = mixed_moments(d,ell,w,product.degree())
            cross = sum((c*m for c,m in zip(product.coeffs(),moments)),A(0))
            total += 2*bi*bj*cross
    assert total > 0
    return total

def main(args):
    if not __debug__:
        raise RuntimeError('Assertions must be enabled')
    start = time.monotonic()
    ctx.prec = args.bits
    record = json.loads(Path(args.vector_record).read_text())
    integer = record['log_horizon']
    L,w = A(integer).log(),rat(args.shift)
    assert 0 < L < 3 and 0 < w <= A(1)/2
    ids = record['basis_degrees']
    values = [rat(s) for s in record['rational_vector_decimal_coefficients']]
    norm = sum((x*x for x in values),A(0))
    a = [A(0) for _ in range(max(ids)+1)]
    for n,v in zip(ids,values):
        for k in range(n+1):
            a[k] += v*A(2*n+1).sqrt()*(-1)**(n+k)*math.comb(n,k)*math.comb(n+k,k)
    print('Building full-output polynomial profile',flush=True)
    p = gamma_output(a,L,w,args.degree)
    ds = delays(integer,L,w)
    print('Integrating every pair of delayed outputs',flush=True)
    model = full_norm_sq(p,ds,w)/norm
    # |G_w(z)|<32768 on |z|=3: see the accompanying proof.
    assert A(3).sin() > A(1)/8
    assert (A(3)/2).exp() < 5
    assert 120+1440*A(3).exp() < 32768
    delta_gamma = ((2*A.pi()*L)**w/w.gamma()*32768*(L/3)**(args.degree+1)
                   /((args.degree+1+w)*(1-L/3)))
    delta = sum((b for _,b,_ in ds),A(0))*delta_gamma
    error = 2*delta*model.sqrt()+delta*delta
    storage = 1-model
    low,high = (storage-error.upper()).lower(),(storage+error.upper()).upper()
    data = {
        'result': 'POSITIVE scalar storage' if low > 0 else 'NEGATIVE scalar storage' if high < 0 else 'INCONCLUSIVE',
        'scope':'One exact input, with all output retained. Positive scalar storage is not an operator contraction certificate.',
        'normalization':'finite-horizon Weil v0.3, a566944dc1be2899e37fce3d0e857516ced33d8f',
        'log_horizon':integer,'shift_rational':args.shift,'profile_degree':args.degree,'precision_bits':args.bits,
        'vector_record':str(Path(args.vector_record).resolve()),
        'vector_sha256':hashlib.sha256(Path(args.vector_record).read_bytes()).hexdigest(),
        'model_norm_squared_ratio':model.str(55),
        'model_storage_ratio':storage.str(55),
        'full_transfer_operator_error_upper':delta.upper().str(40),
        'storage_error_upper':error.upper().str(40),
        'exact_storage_ratio_lower':low.str(55),'exact_storage_ratio_upper':high.str(55),
        'storage_over_2omega_lower':(low/(2*w)).lower().str(50),
        'storage_over_2omega_upper':(high/(2*w)).upper().str(50),
        'positive_lower_bound_pass':bool(low > 0),'negative_upper_bound_pass':bool(high < 0),
        'seconds':time.monotonic()-start,
        'versions':{'python':platform.python_version(),'python_flint':flint.__version__,'flint':flint.__FLINT_VERSION__},
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2),flush=True)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--vector-record',default=str(DEFAULT_VECTOR))
    p.add_argument('--shift',default='1e-11')
    p.add_argument('--degree',type=int,default=220)
    p.add_argument('--bits',type=int,default=6144)
    p.add_argument('--output',required=True)
    main(p.parse_args())
