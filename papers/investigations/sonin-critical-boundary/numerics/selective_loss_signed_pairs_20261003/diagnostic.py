#!/usr/bin/env python3
"""Signed causal Gram/discrepancy diagnostic; no inverse or certificate."""
import hashlib
import json
import math
from pathlib import Path
import platform
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
RS=tuple(range(2,11))
NORM_SQ=146640624550936576/37921101075
NORM=math.sqrt(NORM_SQ)
CAP_NORM_SQ=917180/580421327

def g(x):
    xx=x*x
    return -64*x*(1-16*xx)**5*(2689-215072*xx+256*xx*xx)/NORM

def vcap(y):
    out=np.zeros_like(y)
    inside=np.abs(y)<.25
    t=y[inside]; a=1-16*t*t
    hp=-256*t*a**7
    hpp=-256*a**6*(1-240*t*t)
    out[inside]=(-hpp-hp/2)/NORM
    return out

def powers(L):
    cutoff=math.exp(L); N=int(cutoff)
    sieve=[True]*(N+1); sieve[:2]=[False,False]
    for p in range(2,math.isqrt(N)+1):
        if sieve[p]:
            for n in range(p*p,N+1,p): sieve[n]=False
    rows=[]
    for p in range(2,N+1):
        if not sieve[p]: continue
        n=p; m=1
        while n<cutoff:
            rows.append({'n':n,'p':p,'m':m,'u':math.log(n),
                         'coefficient':math.log(p)/math.sqrt(n)})
            n*=p; m+=1
    return sorted(rows,key=lambda row:row['n'])

def breakpoints(r,rows):
    L=r+.5; half=L/2
    pts={-half,half,-r/2+.25,r/2-.25}
    for row in rows:
        a=row['u']-r/2
        for center in (a,-a):
            for endpoint in (center-.25,center+.25):
                pts.add(max(-half,min(half,endpoint)))
    return np.array(sorted(pts))

def moments(r,rows,order):
    nodes,weights=np.polynomial.legendre.leggauss(order)
    individual=[]
    for row in rows:
        u=row['u']
        if u<=r:
            individual.append(0.0)
            continue
        lo=-.25; hi=r+.25-u
        radius=(hi-lo)/2; mid=(hi+lo)/2
        z=mid+radius*nodes
        mk=float(radius*np.dot(weights,np.sinh((z+u-r/2)/2)*g(z)))
        individual.append(math.sqrt(2)*row['coefficient']*mk)
    y=nodes/4
    cap_moment=float(math.sqrt(2)*np.dot(weights,
        np.sinh((y-r/2)/2)*vcap(y))/4)
    return {'order':order,'arithmetic_moment':math.fsum(individual),
            'individual_moment_square_sum':math.fsum(m*m for m in individual),
            'continuum_moment':cap_moment}

def integrate(r,rows,pts,order):
    nodes,weights=np.polynomial.legendre.leggauss(order)
    mid=(pts[:-1]+pts[1:])/2; radius=(pts[1:]-pts[:-1])/2
    x=(mid[:,None]+radius[:,None]*nodes[None,:]).ravel()
    qw=(radius[:,None]*weights[None,:]).ravel()
    y=x+r/2
    p=np.zeros_like(x); diag=np.zeros_like(x)
    reflected_self=0.0; evaluations=0
    for row in rows:
        u=row['u']; c=row['coefficient']
        left=int(np.searchsorted(y,u-.25,side='right'))
        right=int(np.searchsorted(y,u+.25,side='left'))
        if right<=left: continue
        local=g(y[left:right]-u)
        p[left:right]+=c*local
        diag[left:right]+=c*c*local*local
        evaluations+=right-left
        if abs(u-r/2)<.25:
            mirror_arg=r-y[left:right]-u
            mask=np.abs(mirror_arg)<.25
            reflected_self+=float(c*c*np.dot(qw[left:right][mask],
                local[mask]*g(mirror_arg[mask])))
    pref=p[::-1]
    w=(p-pref)/math.sqrt(2)
    p0=vcap(y); p0ref=p0[::-1]; w0=(p0-p0ref)/math.sqrt(2)
    e=w-w0
    J=float(np.dot(qw,p*p)); D=float(np.dot(qw,diag))
    C=float(np.dot(qw,p*pref)); raw=J-C
    direct_raw=float(np.dot(qw,w*w))
    continuum=float(np.dot(qw,w0*w0))
    mixed=float(np.dot(qw,w*w0))
    discrepancy=float(np.dot(qw,e*e))
    return {'order':order,'polynomial_evaluations':evaluations,
            'J_causal_energy':J,'D_direct_diagonal':D,
            'Theta_signed_offdiagonal':J-D,'C_reflected_convolution':C,
            'minus_C_response_contribution':-C,
            'C_same_prime_power':reflected_self,
            'full_packet_diagonal':D-reflected_self,
            'raw_norm_sq':raw,'direct_raw_norm_sq':direct_raw,
            'continuum_cap_norm_sq':continuum,
            'arithmetic_continuum_inner_product':mixed,
            'discrepancy_raw_norm_sq':discrepancy,
            'moment_whole_quadrature':float(np.dot(qw,np.sinh(x/2)*w)),
            'mean_moment_diagnostic':float(np.dot(qw,w)),
            'cosh_moment_diagnostic':float(np.dot(qw,np.cosh(x/2)*w)),
            'reflection_grid_error':float(np.max(np.abs(x+x[::-1]))),
            'raw_identity_residual':direct_raw-raw,
            'centering_identity_residual':discrepancy-(raw-2*mixed+continuum)}

def rel(a,b):
    return abs(a-b)/max(abs(b),np.finfo(float).tiny)

def run():
    start=time.perf_counter()
    n,w=np.polynomial.legendre.leggauss(24)
    mu2=float(np.dot(w,(n/4)**2*g(n/4)**2)/4)
    results=[]
    for r in RS:
        rows=powers(r+.5); pts=breakpoints(r,rows)
        q16=integrate(r,rows,pts,16)
        # All pieces remain; the larger order is a floating stability check.
        q24=integrate(r,rows,pts,24)
        m24=moments(r,rows,24); m32=moments(r,rows,32)
        ds=math.sinh((r+.5)/2)-(r+.5)/2
        M=m32['arithmetic_moment']**2/ds
        M0=m32['continuum_moment']**2/ds
        Me=(m32['arithmetic_moment']-m32['continuum_moment'])**2/ds
        R=q16['raw_norm_sq']-M
        E=q16['discrepancy_raw_norm_sq']-Me
        projected_diag=q16['full_packet_diagonal']-m32['individual_moment_square_sum']/ds
        Y=r+.25; D0=Y*Y/2+mu2/2
        result={'r':r,'L':r+.5,'Y':Y,'prime_power_count':len(rows),
                'piece_count':len(pts)-1,'largest_active_n':rows[-1]['n'],
                'primary_order':16,'raw_orders':[q16,q24],
                'moment_orders':[m24,m32],
                'D_continuum_diagonal_model':D0,
                'D_over_continuum_diagonal_model':q16['D_direct_diagonal']/D0,
                'projection_subtraction_M':M,
                'projected_arithmetic_norm_sq':R,
                'projected_full_packet_diagonal':projected_diag,
                'projected_full_packet_offdiagonal':R-projected_diag,
                'continuum_projection_subtraction':M0,
                'projected_continuum_norm_sq':q16['continuum_cap_norm_sq']-M0,
                'discrepancy_projection_subtraction':Me,
                'projected_discrepancy_norm_sq':E,
                'Theta_over_D':q16['Theta_signed_offdiagonal']/q16['D_direct_diagonal'],
                'J_over_D':q16['J_causal_energy']/q16['D_direct_diagonal'],
                'R_over_D':R/q16['D_direct_diagonal'],
                'consistency':{
                    'raw16_vs24_relative':rel(q16['raw_norm_sq'],q24['raw_norm_sq']),
                    'J16_vs24_relative':rel(q16['J_causal_energy'],q24['J_causal_energy']),
                    'D16_vs24_relative':rel(q16['D_direct_diagonal'],q24['D_direct_diagonal']),
                    'C16_vs24_absolute':abs(q16['C_reflected_convolution']-q24['C_reflected_convolution']),
                    'moment24_vs32_relative':rel(m24['arithmetic_moment'],m32['arithmetic_moment']),
                    'moment_whole16_vs_cap32_absolute':abs(q16['moment_whole_quadrature']-m32['arithmetic_moment']),
                    'continuum16_vs_exact_absolute':abs(q16['continuum_cap_norm_sq']-CAP_NORM_SQ),
                    'causal_identity_absolute':abs(q16['raw_identity_residual']),
                    'centering_identity_absolute':abs(q16['centering_identity_residual']),
                    'projected_gram_identity_absolute':abs(R-(q16['D_direct_diagonal']+
                        q16['Theta_signed_offdiagonal']-q16['C_reflected_convolution']-M))}}
        results.append(result)
        print(f'r={r} pp={len(rows)} pieces={len(pts)-1} '
              f'D={q16["D_direct_diagonal"]:.9g} Theta={q16["Theta_signed_offdiagonal"]:.9g} '
              f'C={q16["C_reflected_convolution"]:.9g} M={M:.6g} R={R:.9g}',flush=True)
    record={'date':'2026-10-03','prepared_for':'Edward Baker',
            'model':'GPT-6 (Codex)','serving_variant':'not exposed; not inferred',
            'reasoning_effort':'not exposed; not inferred',
            'llm_acknowledgement':'Prepared with substantial LLM assistance.',
            'status':'FLOATING DIAGNOSTIC ONLY; no outward certificate or global rate',
            'scope':'Complete arithmetic/discrepancy Gram cancellation; no A inverse, B inverse, Sonin correction, or safe complement computed.',
            'formulas':{'p':'sum Lambda(n)/sqrt(n) g(y-log n)',
                        'J':'integral_0^Y p(y)^2 dy, Y=r+1/4',
                        'D':'sum Lambda(n)^2/n integral_0^Y g(y-log n)^2 dy',
                        'Theta':'J-D (signed aggregate, not absolute pairs)',
                        'C':'integral p(y)p(r-y)dy=(p*p)(r)',
                        'raw':'J-C=D+Theta-C',
                        'projected':'D+Theta-C-M',
                        'complete_discrepancy':'w-w0, before projection and norm'},
            'mu2_probe_sq_diagnostic':mu2,
            'continuum_cap_norm_sq_exact':'917180/580421327',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'python_version':platform.python_version(),'numpy_version':np.__version__,
            'runtime_seconds':time.perf_counter()-start,'results':results}
    (ROOT/'record.json').write_text(json.dumps(record,indent=2)+'\n')
    print(f'Runtime {record["runtime_seconds"]:.3f} seconds')

if __name__=='__main__': run()
