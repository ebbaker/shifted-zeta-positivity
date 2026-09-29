#!/usr/bin/env python3
"""Small candidate/actual-ground comparison. Floating diagnostics, not a proof.

GPT-6 (Codex); exact serving variant and reasoning effort not exposed. 2026-09-28.
The candidate is the restriction of the analytic even Xi kernel, NOT the
prolate finite-sum candidate. No zeta zeros or positivity premise are used.
Repository imports are read-only and Python bytecode generation is disabled.
"""
import argparse
import hashlib
import json
import platform
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
bootstrap = argparse.ArgumentParser(add_help=False)
bootstrap.add_argument('--repo-numerics', type=Path, default=Path(__file__).resolve().parent)
NUM = bootstrap.parse_known_args()[0].repo_numerics.resolve()
sys.path.insert(0, str(NUM))
import mpmath as mp
from check_mass_stiffness import prime_powers, weil_matrix, strings, scaled_error
from check_odd_blocks import blocks, coefficients as inherited_coefficients


def coefficients(limit, nmax):
    """Same closed formula as inherited builder, with X replacing 13.

    The gamma exponential tail is exp(-(2k+1/2)L), L=log X; prime_powers
    supplies the same exact finite prime list. Only these parameters vary.
    A tiny defining-distribution check guards this parameter extension.
    """
    length = mp.log(limit)
    count = int(mp.ceil((mp.mp.dps+20)*mp.log(10)/(2*length)))
    exp_terms = [mp.power(limit, -2*k-mp.mpf('.5')) for k in range(count)]
    powers = prime_powers(limit)
    b, odd = {}, {}
    sinh2 = mp.sinh(length/4)**2
    for n in range(1,nmax+1):
        d = 2*mp.pi*n/length
        z = mp.mpf('.25')+1j*d/2
        psi, trigamma = mp.digamma(z), mp.polygamma(1,z)
        pole_sin = -2*d*(mp.cosh(length/2)-1)/(d*d+mp.mpf('.25'))
        sine_arch = mp.im(psi)/2-mp.fsum(
            d*e/((2*k+mp.mpf('.5'))**2+d*d) for k,e in enumerate(exp_terms))
        sine_prime = mp.fsum(mp.log(p)/mp.sqrt(q)*mp.sin(d*mp.log(q)) for q,p in powers)
        b[n] = (sine_arch+sine_prime-pole_sin)/mp.pi
        arch = mp.re(psi)-mp.log(mp.pi)-mp.im(psi)/(length*d)+mp.re(trigamma)/(2*length)
        arch += 4*d*d/length*mp.fsum(
            e/((2*k+mp.mpf('.5'))**2+d*d)**2 for k,e in enumerate(exp_terms))
        pole = -16*sinh2*d*d/(length*(d*d+mp.mpf('.25'))**2)
        prime = mp.fsum(mp.log(p)/mp.sqrt(q)*(2*(1-mp.log(q)/length)*mp.cos(d*mp.log(q))
                      +2*mp.sin(d*mp.log(q))/(length*d)) for q,p in powers)
        odd[n] = arch+pole-prime
    c = mp.digamma(mp.mpf('.25'))-mp.log(mp.pi)+mp.polygamma(1,mp.mpf('.25'))/(2*length)
    c -= 2/length*mp.fsum(e/(2*k+mp.mpf('.5'))**2 for k,e in enumerate(exp_terms))
    c += 32*sinh2/length-mp.fsum(2*mp.log(p)/mp.sqrt(q)*(1-mp.log(q)/length) for q,p in powers)
    return b, odd, c


def xi_kernel(x):
    """E(h)(exp |x|); evenness avoids cancellation in the negative-x series."""
    u = mp.exp(abs(x))
    nmax = int(mp.ceil(mp.sqrt((mp.mp.dps+25)*mp.log(10)/mp.pi)/u))+2
    return mp.sqrt(u)*mp.fsum(mp.pi/2*(n*u)**2*(2*mp.pi*(n*u)**2-3)*
                              mp.exp(-mp.pi*(n*u)**2) for n in range(1,nmax+1))


def candidate(length, nmax, segments=8):
    points = [length*j/(2*segments) for j in range(segments+1)]
    integral = lambda fun: 2*mp.quad(fun,points,method='gauss-legendre')
    mean = integral(xi_kernel)
    norm2 = integral(lambda x:xi_kernel(x)**2)
    moment = integral(lambda x:x*x*xi_kernel(x))/(2*mean)
    coeff = [mean/mp.sqrt(length)]
    for n in range(1,nmax+1):
        d = 2*mp.pi*n/length
        coeff.append((-1)**n*mp.sqrt(2/length)*integral(lambda x:xi_kernel(x)*mp.cos(d*x)))
    return mp.matrix(coeff)/mp.sqrt(norm2), moment, mean/mp.sqrt(norm2)


def check_definition(limit, data):
    n = 3
    full, direct = weil_matrix(limit,n)
    even, odd = mp.zeros(2*n+1,n+1), mp.zeros(2*n+1,n)
    even[n,0] = 1
    for j in range(1,n+1):
        even[n+j,j] = even[n-j,j] = 1/mp.sqrt(2)
        odd[n+j,j-1] = 1/mp.sqrt(2)
        odd[n-j,j-1] = -1/mp.sqrt(2)
    plus, minus = blocks(n,*data)
    return dict(even_closed_vs_definition=scaled_error(plus,even.T*full*even),
                odd_closed_vs_definition=scaled_error(minus,odd.T*full*odd),
                direct_entry=direct)


def tau(ground,length):
    return length**2/24+mp.sqrt(2)/ground[0]*mp.fsum(
        ground[n]/(2*mp.pi*n/length)**2 for n in range(1,ground.rows))


def run(digits,cases,output):
    mp.mp.dps=digits
    report=dict(date='2026-09-28',model='GPT-6 (Codex)',exact_serving_variant='not exposed',reasoning_effort='not exposed',
        generator_version='portable-v2; mathematical formulas unchanged from archived run-sources/v1',
        status='multiprecision floating diagnostics; no interval or infinite-tail certification',
        candidate='L2-normalized restriction of the analytic even Xi kernel, then Fourier projected; not the finite prolate candidate',
        basis='e0=L^(-1/2), en=sqrt(2/L) cos(2 pi n (x+L/2)/L), centered x',
        digits=digits,python=platform.python_version(),mpmath=mp.__version__,
        zero_data_used=False,source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest()
             for p in (Path(__file__),NUM/'check_mass_stiffness.py',NUM/'check_odd_blocks.py')},
        definition_checks={},cases=[])
    for limit in sorted(set(x for x,n in cases)):
        start=time.monotonic()
        nmax=max(n for x,n in cases if x==limit)
        data=coefficients(limit,2*nmax)
        report['definition_checks'][str(limit)]=check_definition(limit,data)
        if max(report['definition_checks'][str(limit)].values())>mp.power(10,-digits//2):
            raise ArithmeticError('Closed formula disagrees with definition.')
        if limit==13:
            legacy=inherited_coefficients(2*nmax)
            report['definition_checks'][str(limit)]['legacy_coefficients']=max(
                [abs(data[j][n]-legacy[j][n]) for j in (0,1) for n in range(1,2*nmax+1)]
                +[abs(data[2]-legacy[2])])
        length=mp.log(limit)
        cand,moment,mean=candidate(length,2*nmax)
        big,_=blocks(2*nmax,*data)
        for n in sorted(nn for x,nn in cases if x==limit):
            plus,minus=blocks(n,*data)
            eig,vec=mp.eigsy(plus)
            odd=mp.eigsy(minus,eigvals_only=True)
            v=cand[:n+1,:]
            pnorm=mp.norm(v)
            vhat=v/pnorm
            u=vec[:,0]
            overlap=(u.T*vhat)[0]
            if overlap<0:u=-u;overlap=-overlap
            rho=(vhat.T*plus*vhat)[0]
            residual=mp.norm(plus*vhat-rho*vhat)
            sigma=eig[1]-rho
            cross=big[n+1:2*n+1,:n+1]
            tailsq=1-pnorm**2
            if tailsq < -mp.power(10,-digits//2):raise ArithmeticError('Projection norm >1')
            row=dict(X=limit,L=length,N=n,even_eigenvalues=list(eig[:min(4,n+1)]),
                finite_even_ground_gap=eig[1]-eig[0],least_odd=odd[0],
                simple_even_observed=bool(eig[1]>eig[0] and odd[0]>eig[0]),
                candidate_rayleigh=rho,finite_candidate_residual=residual,
                second_even_minus_rayleigh=sigma,residual_gate_positive=bool(sigma>0),
                residual_over_separation=residual/sigma if sigma>0 else None,
                overlap=overlap,projected_candidate_ground_distance=mp.norm(u-vhat),
                full_candidate_ground_distance=mp.sqrt(max(mp.mpf(0),2-2*(u.T*v)[0])),
                candidate_projection_tail_norm=mp.sqrt(max(mp.mpf(0),tailsq)),
                ground_signed_half_second_moment=tau(u,length),
                projected_candidate_signed_half_second_moment=tau(vhat,length),
                true_truncated_candidate_half_second_moment=moment,
                ground_mean=mp.sqrt(length)*u[0],candidate_mean=mean,
                retained_candidate_even_spectral_weights=[(vec[:,j].T*vhat)[0]**2 for j in range(min(4,n+1))],
                candidate_coupling_to_next_N_rows=mp.norm(cross*vhat),
                actual_ground_coupling_to_next_N_rows=mp.norm(cross*u),
                checks=dict(eigenpair_residual=mp.norm(plus*u-eig[0]*u),
                    projection_overlap_distance_identity=abs(mp.norm(u-vhat)**2-(2-2*overlap)),
                    candidate_projection_energy_identity=abs(rho-mp.fsum(eig[j]*(vec[:,j].T*vhat)[0]**2 for j in range(n+1)))))
            report['cases'].append(row)
            output.write_text(json.dumps(strings(report),indent=2)+'\n')
            print(json.dumps(strings(dict(X=limit,N=n,rho=rho,sigma=sigma,residual=residual,
                ratio=row['residual_over_separation'],distance=row['full_candidate_ground_distance'],
                overlap=overlap,tau=row['ground_signed_half_second_moment'],elapsed_seconds=time.monotonic()-start))),flush=True)
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--digits',type=int,default=90)
    p.add_argument('--repo-numerics',type=Path,default=Path(__file__).resolve().parent,
                   help='Directory containing the existing CCM builders; defaults to this script directory.')
    p.add_argument('--case',action='append',default=[])
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    cases=[tuple(map(int,c.split(','))) for c in args.case] or [(5,8),(5,16),(13,8),(13,16),(13,32),(29,16),(29,32)]
    args.output.parent.mkdir(parents=True,exist_ok=True)
    report=run(args.digits,cases,args.output)
    args.output.write_text(json.dumps(strings(report),indent=2)+'\n')
