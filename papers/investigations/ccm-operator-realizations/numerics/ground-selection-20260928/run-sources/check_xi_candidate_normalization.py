#!/usr/bin/env python3
"""Independent normalizations for the diagnostic Xi candidate, no zero data.

GPT-6 Astra; effort not exposed; 2026-09-28. Floating checks only.
"""
import hashlib
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
from check_xi_ground_comparison import mp,xi_kernel,strings

mp.mp.dps=70
def direct(x):
    u=mp.exp(x)
    nmax=int(mp.ceil(mp.sqrt((mp.mp.dps+25)*mp.log(10)/mp.pi)/u))+2
    return mp.sqrt(u)*mp.fsum(mp.pi/2*(n*u)**2*(2*mp.pi*(n*u)**2-3)*
           mp.exp(-mp.pi*(n*u)**2) for n in range(1,nmax+1))
def xi(z):
    s=mp.mpf('.5')+1j*z
    return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)/2
points=[mp.mpf(0),mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),1,mp.mpf('1.5'),2,3]
integral=lambda fun:2*mp.quad(fun,points,method='gauss-legendre')
mean=integral(xi_kernel)
moment=integral(lambda x:x*x*xi_kernel(x))/(2*mean)
target=-mp.re(mp.diff(xi,0,2)/xi(0))/2
out=dict(date='2026-09-28',model='GPT-6 Astra',reasoning_effort='not exposed',
    status='multiprecision normalization checks; not interval-certified',digits=mp.mp.dps,
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    generator_sha256=hashlib.sha256(Path(__file__).with_name('check_xi_ground_comparison.py').read_bytes()).hexdigest(),
    zero_data_used=False,evenness_errors={str(x):abs(direct(x)-direct(-x)) for x in (mp.mpf('.25'),mp.mpf('.75'))},
    full_kernel_half_second_moment=moment,xi_derivative_target=target,moment_absolute_error=abs(moment-target),
    normalized_real_transform_errors={str(t):abs(integral(lambda x:xi_kernel(x)*mp.cos(t*x))/mean-xi(t)/xi(0)) for t in (1,5,10)},
    tail_policy='Integrals truncated at |x|=3; superexponential tails are below working precision but not interval-enclosed.')
destination=Path(sys.argv[1])
destination.write_text(json.dumps(strings(out),indent=2)+'\n')
print(json.dumps(strings(out),indent=2))
