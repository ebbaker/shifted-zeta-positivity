#!/usr/bin/env python3
"""Bounded packet and prime-orbit checks for Investigation 11.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Model gpt-6-astra (Codex), reasoning effort max.
Requires python-flint. Analytic identities and the existence theorem are
proved in the companion notes. This checks finite numerical evaluations and
certifies endpoint signs for one exactly defined infinite-orbit direction;
it does not locate or certify a collision of theta or of that direction.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, resource, signal, time
from pathlib import Path
import flint
from flint import arb, acb, ctx

BITS = 384
MAX_SECONDS = 240
N = 8
U = '1.5'
T = '0.25'
Z_RE = '30'
SEEDS = (5, 7, 11)

def bs(x):
    return x.str(65, more=True)

def cb(z):
    return {'real': bs(z.real), 'imag': bs(z.imag)}

def radius(x):
    return arb(0, x.abs_upper())

def advance(p):
    # P -> (1-4a)P + 4aP', exactly over the integers.
    out = [0] * (len(p) + 1)
    for k, v in enumerate(p):
        out[k] += (1+4*k)*v
        out[k+1] -= 4*v
    return out

def value(p, x):
    out = arb(0)
    for c in reversed(p): out = out*x+c
    return out

def polynomial_tail(p, start):
    """Sum |P(pi*n^2)|exp(-pi*n^2), n >= start, by monomials."""
    pi = arb.pi(); lam = pi*start*start; total = arb(0)
    for k, c in enumerate(p):
        if c:
            ratio = (arb(start+1)/start)**(2*k)*(-pi*(2*start+1)).exp()
            assert ratio < 1
            total += abs(c)*lam**k*(-lam).exp()/(1-ratio)
    return total

def moment_tail(start, j, y=arb(1)/3):
    """All source indices n>=start; t<=1/4; |Im z|<=y."""
    pi = arb.pi(); lam = pi*start*start
    assert lam >= arb(T)/8
    rate = 4*lam-9-y
    assert rate > 0
    ratio = (arb(start+1)/start)**4*(-pi*(2*start+1)).exp()
    assert ratio < 1
    return 2*lam**2*math.factorial(j)*(-lam).exp()/rate**(j+1)/(1-ratio)

def integral_tail(n, j, y=arb(1)/3):
    upper = arb(U); t = arb(T); lam = arb.pi()*n*n
    q = lam*(4*upper).exp()
    rate = 4*q-9-y-2*t*upper
    assert rate > 0 and 8*q > t
    height = 2*lam**2*(t*upper**2+(9+y)*upper-q).exp()
    return height*sum(arb(math.comb(j,k)*math.factorial(k))*upper**(j-k)/rate**(k+1)
                      for k in range(j+1))

def source(u, multiple=1):
    e4 = (4*u).exp(); total = acb(0)
    for n in range(1, N+1):
        lam = arb.pi()*(multiple*n)**2
        q = lam*e4
        total += (u-q).exp()*(2*q*q-3*q)
    return total

def integrate(f, lo, hi):
    result = acb.integral(f, lo, hi, rel_tol=arb('1e-96'),
                          abs_tol=arb('1e-105'), eval_limit=150000, depth_limit=35)
    assert result.is_finite()
    return result

def with_error(z, err):
    return z + acb(radius(err), radius(err))

def direct_packet(d, z, j):
    t = arb(T); ii = acb(0,1)
    raw = integrate(lambda u, analytic: (t*u*u+ii*z*u).exp()*(ii*u)**j*source(u,d), 0, arb(U))
    err = sum((integral_tail(d*n,j) for n in range(1,N+1)),arb(0)) + moment_tail(d*(N+1),j)
    return with_error(raw,err)

def shifted_packet(d, z, j):
    t = arb(T); a = arb(d).log()/2; ii = acb(0,1)
    assert a < arb(U)
    pref = (t*a*a-ii*z*a).exp()/arb(d).sqrt()
    w = z+ii*2*t*a
    def fun(v,analytic):
        return (t*v*v+ii*w*v).exp()*(ii*(v-a))**j*source(v)
    complete = integrate(fun,0,arb(U))
    lower = integrate(fun,0,a)
    # The paired integrand, after multiplying pref, has argument v-a>=0
    # above U>a. Bound it by v^j exp(t*v^2+y*v)Phi(v)/sqrt(d).
    err = sum((integral_tail(n,j) for n in range(1,N+1)),arb(0))/arb(d).sqrt()
    # For omitted original indices n>N, the paired expression is precisely
    # the omitted divisible source, whose first possible index is d*(N+1).
    err += moment_tail(d*(N+1),j)
    return with_error(pref*(complete-lower),err), complete, lower

def cosine_packet(d,z,j):
    t=arb(T)
    def fun(u,analytic):
        trig=((z*u).cos(),-(z*u).sin(),-(z*u).cos())[j]
        return (t*u*u).exp()*u**j*trig*source(u,d)
    raw=integrate(fun,0,arb(U))
    err=sum((integral_tail(d*n,j) for n in range(1,N+1)),arb(0))+moment_tail(d*(N+1),j)
    return with_error(raw,err)

def orbit_certificate():
    polys=[[0,-3,2]]
    for _ in range(3):polys.append(advance(polys[-1]))
    assert polys[1]==[0,-15,30,-8]
    assert polys[3]==[0,-375,3270,-4232,1440,-128]
    beta=[-1,4]; entries={}
    for r in SEEDS:
        lam=arb.pi()*r*r; row={}
        for name,poly in [('B',beta),('D1',polys[1]),('D3',polys[3])]:
            # The next possible {2,3}-smooth multiplier after 1 is 2.
            # Bounding by every integer n>=2r encloses the infinite orbit.
            tail=polynomial_tail(poly,2*r)*lam.exp()
            row[name]=value(poly,lam)+radius(tail)
            row[name+'_tail']=tail
        entries[r]=row
    b5,b7,b11=(entries[r]['B'] for r in SEEDS)
    d5,d7,d11=(entries[r]['D1'] for r in SEEDS)
    det=b5*d7-b7*d5
    assert not det.contains(0)
    w5=(-b11*d7+b7*d11)/det
    w7=(-b5*d11+b11*d5)/det
    weights=[w5,w7,arb(1)]
    residual_b=w5*b5+w7*b7+b11
    residual_d=w5*d5+w7*d7+d11
    assert residual_b.contains(0) and residual_d.contains(0)
    e3=sum((w*entries[r]['D3'] for w,r in zip(weights,SEEDS)),arb(0))
    assert e3<0
    v=[w*(arb.pi()*(r*r-121)).exp() for w,r in zip(weights,SEEDS)]
    assert abs(v[0])<1 and abs(v[1])<1 and v[2]==1
    # Every coefficient is indexed by its 2,3-free part. This verifies a
    # bounded discrete instance of the structural proof, including powers.
    def rough(n):
        for p in (2,3):
            while n%p==0:n//=p
        return n
    for n in range(1,201):
        assert rough(2*n)==rough(n)==rough(3*n)
    return {'seeds':list(SEEDS),'primes':[2,3],
            'scaled_orbit_endpoints':{str(r):{k:bs(vv) for k,vv in row.items()} for r,row in entries.items()},
            'two_constraint_determinant':bs(det),'scaled_weights':[bs(w) for w in weights],
            'coefficient_direction':[bs(vv) for vv in v],
            'scaled_primitive_residual':bs(residual_b),
            'scaled_first_source_derivative_residual':bs(residual_d),
            'scaled_third_source_derivative':bs(e3),
            'exact_definition':'Weights solve the infinite-orbit primitive and first-source-derivative equations; interval balls enclose those exact weights.',
            'certified':'The defining matrix is invertible, max coefficient magnitude is 1, and the next source odd derivative is negative.',
            'not_certified':'No collision location or coefficient multiplier at a collision is evaluated.'}

def main(output):
    started=time.monotonic();ctx.prec=BITS
    def timeout(signum,frame):raise TimeoutError('240-second bounded check exceeded')
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,MAX_SECONDS)
    record={'schema':'inv11_packets_prime_orbits_v1','date':'2026-10-18',
            'prepared_for':'Edward Baker','model':'gpt-6-astra','effort':'max',
            'llm_assistance':'Substantial LLM assistance; same-assistant checks.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'python':platform.python_version(),'python_flint':flint.__version__,
            'precision_bits':BITS,'scope':'Bounded numerical identity checks and an infinite-orbit endpoint certificate; no theta positivity or collision certificate.',
            'parameters':{'t':T,'z_real':Z_RE,'z_imag':'1/3','d':[2,3,6],
                          'derivatives':[0,1,2],'source_terms':N,'upper_integral':U,
                          'max_seconds':MAX_SECONDS},
            'orbit':orbit_certificate(),'packets':[]}
    z=acb(arb(Z_RE),arb(1)/3)
    for d in (2,3,6):
        for j in range(3):
            plus=direct_packet(d,z,j);minus=direct_packet(d,-z,j)
            transformed,complete,lower=shifted_packet(d,z,j)
            error=plus-transformed
            assert error.real.contains(0) and error.imag.contains(0)
            assert abs(error)<arb('1e-83')
            paired=(plus+(-1)**j*minus)/2
            direct_cos=cosine_packet(d,z,j)
            reflected_error=paired-direct_cos
            assert reflected_error.real.contains(0) and reflected_error.imag.contains(0)
            assert abs(reflected_error)<arb('1e-83')
            wrong_sign_rejected=None
            if j==1:
                wrong=(plus+minus)/2-direct_cos
                wrong_sign_rejected=not(wrong.real.contains(0) and wrong.imag.contains(0))
                assert wrong_sign_rejected
            record['packets'].append({'d':d,'j':j,'direct':cb(plus),
                'transformed':cb(transformed),'identity_difference':cb(error),
                'reflected_difference':cb(reflected_error),
                'wrong_reflection_derivative_sign_rejected':wrong_sign_rejected,
                'complete_piece_abs':bs(abs(complete)),
                'lower_piece_abs':bs(abs(lower)),
                'paired_difference_abs':bs(abs(complete-lower))})
            print('checked packet',d,'derivative',j,flush=True)
    record['elapsed_seconds']=time.monotonic()-started
    raw=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    record['peak_rss_bytes']=int(raw if platform.system()=='Darwin' else 1024*raw)
    record['status']='passed'
    output.write_text(json.dumps(record,indent=2)+'\n')
    print('saved',output,'seconds',record['elapsed_seconds'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    main(p.parse_args().output)
