#!/usr/bin/env python3
"""Exploratory actual first-prime boundary trace with finite resolvent matrices.

No sign certification: the omitted Galerkin complement and source/interpolation
errors have not been enclosed. Evaluates the actual dyadic cosine operator,
not arithmetic subtraction or a constant/global zeta endpoint symbol.
Prepared for Edward Baker, 2026-10-03, with GPT-6 (Codex) assistance.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import CubicSpline
from scipy.signal import fftconvolve
from scipy.special import sici


def sources(grid=32768, b=0.45):
    """h=phi, x phi, and (x^2-c)phi; F=(-d^2+1/4)h, normalized."""
    x=np.linspace(-b,b,grid+1)
    dx=x[1]-x[0]
    phi=np.zeros_like(x); dp=phi.copy(); ddp=phi.copy()
    active=np.abs(x)<b
    z=x[active]; q=1-(z/b)**2
    phi[active]=np.exp(-1/q)
    dp[active]=-2*z/(b*b*q*q)*phi[active]
    ddp[active]=(4*z*z/(b**4*q**4)-2/(b*b*q*q)-8*z*z/(b**4*q**3))*phi[active]
    c=np.trapezoid(x*x*phi,x)/np.trapezoid(phi,x)
    fs=[]; means=[]
    for p,p1,p2 in [(np.ones_like(x),0*x,0*x),(x,np.ones_like(x),0*x),(x*x-c,2*x,2+0*x)]:
        f=-p2*phi-2*p1*dp-p*ddp+p*phi/4
        norm=np.sqrt(np.trapezoid(f*f,x)); f/=norm
        fs.append(f); means.append(float(np.trapezoid(p*phi,x)/norm))
    # Cross correlation of F_i and F_j, symmetrized under u -> -u.
    lags=np.arange(-grid,grid+1)*dx
    correlations={}
    for i in range(3):
        for j in range(i,3):
            cor=fftconvolve(fs[i][::-1],fs[j],mode='full')*dx
            cor=(cor+cor[::-1])/2
            correlations[i,j]=CubicSpline(lags,cor,extrapolate=False)
    return correlations, {'half_support':b,'source_grid':grid,
        'even_zero_mean_coefficient':float(c),'normalized_h_means':means,
        'sources':['A phi / norm','A(x phi) / norm','A((x^2-c)phi) / norm']}


def cosine_block(n, terms=32, prime=True, power=1):
    """Galerkin of C in normalized indicator functions on a power mesh."""
    edges=(np.arange(n+1)/n)**power
    scale=1/np.sqrt(np.diff(edges)[:,None]*np.diff(edges)[None,:])
    xy=edges[:,None]*edges[None,:]
    def block(k):
        a=sici(k*xy)[0]
        return scale/k*(a[1:,1:]-a[1:,:-1]-a[:-1,1:]+a[:-1,:-1])
    if not prime:return 2*block(2*np.pi)
    ans=-block(np.pi)
    for m in range(terms):ans+=block(2*np.pi*2**m)
    return (ans+ans.T)/2


def sine_linear_weights(omega,u):
    """Exact sine integral weights for linear interpolants on uniform u grid."""
    omega=np.asarray(omega)
    h=u[1]-u[0]; theta=omega*h
    f=np.sinc(theta/(2*np.pi))**2
    ans=h*f[:,None]*np.sin(omega[:,None]*u[None,:])
    a=f/2
    z=np.abs(theta)<0.01
    bb=np.zeros_like(theta)
    bb[z]=theta[z]/6-theta[z]**3/120+theta[z]**5/5040-theta[z]**7/362880
    bb[~z]=(theta[~z]-np.sin(theta[~z]))/theta[~z]**2
    ans[:,0]=h*(a*np.sin(omega*u[0])+bb*np.cos(omega*u[0]))
    ans[:,-1]=h*(a*np.sin(omega*u[-1])-bb*np.cos(omega*u[-1]))
    return ans


def tx_block(n,corr, half_support, ugrid=1024,zquad=6,terms=32,prime=True,power=1):
    """Projected TX from integrated dyadic kernels and compact log crossing."""
    length=2*half_support
    u=np.linspace(1,np.exp(length),ugrid+1)
    zedges=(np.arange(n+1)/n)**power
    widths=np.diff(zedges)
    nodes,weights=leggauss(zquad)
    z=(zedges[:-1,None]+zedges[1:,None])/2+nodes*widths[:,None]/2
    zz=z.reshape(-1)
    lag=np.log(u[:,None]/zz[None,:])
    val=np.nan_to_num(corr(lag),nan=0.0)/np.sqrt(u[:,None]*zz[None,:])
    # g_j(u)=int X(u,z)e_j(z) dz. Divide by u for integrated cosine cell.
    g=np.sqrt(widths)[None,:]/2*np.sum(val.reshape(ugrid+1,n,zquad)*weights,axis=2)/u[:,None]
    y=zedges
    def integrated(k):
        w=sine_linear_weights(k*y,u)
        return 1/(np.sqrt(widths)[:,None]*k)*(w[1:]-w[:-1])
    if prime:
        yy=-integrated(np.pi)
        for m in range(terms):yy+=integrated(2*np.pi*2**m)
    else:yy=2*integrated(2*np.pi)
    return yy@g


def square_block(n,terms=32,prime=True,power=1):
    """Exact integral formula for E*C^2*E (finite dyadic sum)."""
    e=(np.arange(n+1)/n)**power
    scale=1/np.sqrt(np.diff(e)[:,None]*np.diff(e)[None,:])
    ks=[np.pi]+[2*np.pi*2**m for m in range(terms)] if prime else [2*np.pi]
    co=[-1]+[1]*terms if prime else [2]
    ans=np.zeros((n,n))
    def J(x): return x*sici(x)[0]-2*np.sin(x/2)**2
    for i,(ki,ci) in enumerate(zip(ks,co)):
        ai=ki*e[:,None]
        for j in range(i+1):
            kj,cj=ks[j],co[j]
            bj=kj*e[None,:]
            v=0.5*(J(ai+bj)-J(ai-bj))
            v=scale*ci*cj/(ki*kj)*(v[1:,1:]-v[1:,:-1]-v[:-1,1:]+v[:-1,:-1])
            ans+=v if i==j else v+v.T
    return (ans+ans.T)/2


def run(n,ugrid,source_grid,terms,zquad,prime,full_square=False,power=1):
    started=time.time()
    cs,meta=sources(source_grid)
    C=cosine_block(n,terms,prime,power)
    eigen,Q=np.linalg.eigh(C)
    if np.max(np.abs(eigen))>=1:raise ArithmeticError('Compressed inverse is not positive')
    R=(Q*(eigen/(1-eigen**2)))@Q.T
    actual_gap=None
    leakage=None
    if full_square:
        H=square_block(n,terms,prime,power)
        A=np.eye(n)-H
        actual_gap=float(np.linalg.eigvalsh(A)[0])
        leakage=float(np.linalg.eigvalsh(H-C@C)[-1])
        if actual_gap<=0: raise ArithmeticError("True Galerkin denominator is not positive")
        R=np.linalg.solve(A,C).T
    K=np.zeros((3,3)); K_reversed=np.zeros((3,3))
    for (i,j),corr in cs.items():
        A=tx_block(n,corr,meta['half_support'],ugrid,zquad,terms,prime,power)
        K[i,j]=K[j,i]=2*np.sum(R*A.T)
        K_reversed[i,j]=K_reversed[j,i]=2*np.sum(R.T*A.T)
    return {'status':'EXPLORATORY_UNENCLOSED_GALERKIN_TRACE','prime_set':[2] if prime else [],
        'sigma':0.5,'cutoff_cells':n,'mesh_power':power,'crossing_interpolation_intervals':ugrid,
        'z_gauss_order':zquad,'dyadic_terms':terms,'meta':meta,
        'C_min_eigenvalue':float(eigen[0]),'C_max_eigenvalue':float(eigen[-1]),
        'compressed_gap':float(np.min(1-eigen**2)),
        'resolvent_denominator':'I-E*C^2*E' if full_square else 'I-(E*C*E)^2',
        'true_Galerkin_gap':actual_gap,'offgrid_leakage_norm_squared':leakage,
        'K_matrix':K.tolist(),'K_reversed_finite_order':K_reversed.tolist(),
        'scalar_order':'2 Tr[D (I-H)^(-1) B]' if full_square else '2 Tr[D (I-D^2)^(-1) B]',
        'mean_zero_restriction_eigenvalues':np.linalg.eigvalsh(K[1:,1:]).tolist(),
        'elapsed_seconds':time.time()-started,
        'uncontrolled_errors':['Galerkin complement in C(I-C^2)^-1 TX',
                               'floating arithmetic and sine-integral corner cancellation',
                               'source sampling/correlation interpolation',
                               'crossing interpolation and z quadrature'],
        'dyadic_operator_tail_bound':float((0.5/(1-2**-0.5))*2**(-terms/2)) if prime else 0.0}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cells',type=int,nargs='+',default=[64,128,256])
    parser.add_argument('--ugrid',type=int,default=1024)
    parser.add_argument('--source-grid',type=int,default=16384)
    parser.add_argument('--terms',type=int,default=32)
    parser.add_argument('--zquad',type=int,default=6)
    parser.add_argument('--archimedean',action='store_true')
    parser.add_argument('--full-square',action='store_true')
    parser.add_argument('--mesh-power',type=float,default=1)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    results=[]
    for n in args.cells:
        result=run(n,args.ugrid,args.source_grid,args.terms,args.zquad,not args.archimedean,args.full_square,args.mesh_power)
        results.append(result); print(json.dumps(result),flush=True)
    if args.output:
        args.output.write_text(json.dumps({'date':'2026-10-03',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'results':results},indent=2)+'\n')
