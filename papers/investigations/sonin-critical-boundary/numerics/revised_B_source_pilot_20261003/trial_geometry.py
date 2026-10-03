#!/usr/bin/env python3
"""Floating actual-Sonin metric trial. No quadrature or rounding enclosure.
Exact mathematical trial q=Pi_infinity b, b normalized physical indicators.
The inverse keeps its identity complement. Every Gram integral is compact.
Prepared for Edward Baker, 2026-10-03, GPT-6 (Codex), effort not exposed.
"""
import argparse, json, time, sys, hashlib
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre, eval_legendre, spherical_jn, sici
from scipy.signal import fftconvolve
from scipy.integrate import cumulative_simpson
from scipy.interpolate import CubicSpline

def gauss(n,a,b):
 x,w=roots_legendre(n);return a+(b-a)*(x+1)/2,w*(b-a)/2

def basis(x,r):
 return np.array([np.sqrt(4*j+1)*eval_legendre(2*j,x) for j in range(r)]).T

def fbasis(x,r):
 return np.array([2*(-1)**j*np.sqrt(4*j+1)*spherical_jn(2*j,2*np.pi*x) for j in range(r)]).T

def source(x):
 x=np.asarray(x);f=np.zeros_like(x);ii=np.abs(x)<.45;z=x[ii];q=1-(z/.45)**2;p=np.exp(-1/q)
 dp=-2*z/(.45**2*q*q)*p
 ddp=(4*z*z/(.45**4*q**4)-2/(.45**2*q*q)-8*z*z/(.45**4*q**3))*p
 f[ii]=-2*dp-z*ddp+.25*z*p
 return f

def geometry(cells=80,logmax=2.8,rank=24,quad=240,seedquad=20,nper=1024,tout=4.,drop=1e-8,ancestor_numerics=None):
 started=time.time();r=2**-.5;a=np.log(2.)
 e=np.exp(np.linspace(0,logmax,cells+1));lo=e[:-1];hi=e[1:];width=hi-lo;sq=np.sqrt(width)
 # Regenerate inherited certified model; no derived prolate matrix is persisted.
 if ancestor_numerics is None:
  candidates=[base/'susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics' for base in Path(__file__).resolve().parents]
  ancestor_numerics=next((p for p in candidates if (p/'prolate_certificate.py').is_file()),None)
 if ancestor_numerics is None:raise ValueError('Provide --ancestor-numerics pointing to inherited arithmetic-storage/numerics')
 inherited=Path(ancestor_numerics).resolve();sys.path.insert(0,str(inherited))
 import prolate_certificate
 record,_,inverse=prolate_certificate.certify(rank=rank,precision_bits=256)
 R=np.array([[float(inverse[i,j]) for j in range(rank)] for i in range(rank)])
 Rm=R-np.eye(rank)
 prolate_meta={'generator_sha256':hashlib.sha256((inherited/'prolate_certificate.py').read_bytes()).hexdigest(),'exact_dyadic_inverse_sha256':record['dyadic_inverse_sha256'],'precision_bits':256,'float_conversion_error_enclosed':False}
 # Tensor seed quadrature (each normalized indicator integrates dy/sqrt(width)).
 g,gw=roots_legendre(seedquad)
 sx=(lo[:,None]+hi[:,None])/2+width[:,None]*g/2
 sw=np.sqrt(width)[:,None]*gw/2
 t=np.einsum('jn,jnk->kj',sw,fbasis(sx.ravel(),rank).reshape(cells,seedquad,rank))
 coeff=Rm@t
 def tb(x):
  xx=np.asarray(x)[:,None];return 2*(hi*np.sinc(2*xx*hi)-lo*np.sinc(2*xx*lo))/sq
 def zz(x):return tb(x)+basis(x,rank)@coeff
 def hh(x):
  xx=np.asarray(x)[:,None]
  v=(sici(2*np.pi*(xx-lo))[0]-sici(2*np.pi*(xx-hi))[0]+sici(2*np.pi*(xx+hi))[0]-sici(2*np.pi*(xx+lo))[0])/(np.pi*sq)
  return v+fbasis(np.asarray(x),rank)@coeff
 bh=np.einsum('jn,jnk->jk',sw,hh(sx.ravel()).reshape(cells,seedquad,cells))
 N=np.eye(cells)-(bh+bh.T)/2
 # S=<q_i,U_log2 q_j>, all four terms compact.
 Sbb=r*np.maximum(0,np.minimum(hi[:,None],2*hi)-np.maximum(lo[:,None],2*lo))/(sq[:,None]*sq)
 # seed_i vs translated h_j on intersection seed_i with x>2.
 xl=np.maximum(lo,2);ww=np.maximum(hi-xl,0)
 sx2=(xl[:,None]+hi[:,None])/2+ww[:,None]*g/2
 sw2=ww[:,None]/sq[:,None]*gw/2
 Sbh=r*np.einsum('in,inj->ij',sw2,hh((sx2/2).ravel()).reshape(cells,seedquad,cells))
 # h_i vs translated seed_j: change x=2u.
 Shb=np.sqrt(2)*np.einsum('jn,jni->ij',sw,hh((2*sx).ravel()).reshape(cells,seedquad,cells))
 y,wy=gauss(quad,0,.5);globalhh=zz(y).T@(wy[:,None]*np.sqrt(2)*zz(2*y))
 y,wy=gauss(quad,0,2);localhh=hh(y).T@(wy[:,None]*r*hh(y/2))
 S=Sbb-Sbh-Shb+globalhh-localhh
 G=1.5*N-r*(S+S.T);G=(G+G.T)/2
 ev,V=np.linalg.eigh(G);keep=ev>drop*ev[-1];W=V[:,keep]/np.sqrt(ev[keep])
 return {'lo':lo,'hi':hi,'sq':sq,'hh':hh,'G':G,'W':W,'G_min':float(ev[0]),'G_max':float(ev[-1]),'retained':int(np.sum(keep)),'inherited_prolate':prolate_meta}
