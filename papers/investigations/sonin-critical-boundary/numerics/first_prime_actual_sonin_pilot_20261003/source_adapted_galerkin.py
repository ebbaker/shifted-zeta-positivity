#!/usr/bin/env python3
"""Floating actual-Sonin metric trial. No quadrature or rounding enclosure.
Exact mathematical trial q=Pi_infinity b, b normalized physical indicators.
The inverse keeps its identity complement. Every Gram integral is compact.
Prepared for Edward Baker, 2026-10-03, GPT-6 (Codex), effort not exposed.
"""
import argparse, json, time
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

def run(cells=80,logmax=2.8,rank=24,quad=240,seedquad=20,nper=1024,tout=4.,drop=1e-8,prolate_json=None):
 started=time.time();r=2**-.5;a=np.log(2.)
 e=np.exp(np.linspace(0,logmax,cells+1));lo=e[:-1];hi=e[1:];width=hi-lo;sq=np.sqrt(width)
 x,w=gauss(120,0,1);E=basis(x,rank); CE=fbasis(x,rank)
 C=E.T@(w[:,None]*CE);C=(C+C.T)/2;R=np.linalg.inv(np.eye(rank)-C@C);Rm=R-np.eye(rank)
 if prolate_json:
  pr=json.loads(Path(prolate_json).read_text())
  if pr['rank']!=rank:raise ValueError('rank must match prolate midpoint input')
  R=np.array(pr['R']);Rm=R-np.eye(rank)
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
 # Output-compressed smoothing norm. Midpoint grid; dyadic shift exact.
 dt=a/nper; nin=int(np.ceil((tout+.46)/dt));u=(np.arange(nin)+.5)*dt
 J=int(np.ceil(.45/dt));v=np.arange(-J,J+1)*dt
 snx=np.linspace(-.45,.45,16385);snf=source(snx);norm=np.sqrt(np.trapezoid(snf*snf,snx))
 fv=source(v)/norm
 hlog=np.sqrt(np.exp(u))[:,None]*hh(np.exp(u))
 cv=fftconvolve(hlog,fv[:,None],mode='full',axes=0)*dt
 ts=(np.arange(len(cv))+.5-J)*dt
 select=(ts>=-.45)&(ts<tout)
 inds=np.where(select)[0];toutgrid=ts[select]
 cvD=cv[inds].copy();valid=inds>=nper;cvD[valid]-=r*cv[inds[valid]-nper]
 anti=cumulative_simpson(snf*np.exp(-snx/2)/norm,x=snx,initial=0)
 ac=CubicSpline(snx,anti)
 def primitive(x):return ac(np.clip(x,-.45,.45))
 def bsmooth(ts):
  tt=ts[:,None]
  return np.exp(tt/2)/sq*(primitive(tt-np.log(lo))-primitive(tt-np.log(hi)))
 resp=bsmooth(toutgrid)-r*bsmooth(toutgrid-a)-cvD
 H=resp.T@resp*dt;H=(H+H.T)/2
 ev,V=np.linalg.eigh(G);keep=ev>drop*ev[-1];W=V[:,keep]/np.sqrt(ev[keep])
 whiten= W.T@H@W; vals,vec=np.linalg.eigh((whiten+whiten.T)/2)
 ans={'status':'EXPLORATORY_NO_QUADRATURE_ENCLOSURE','prolate_input':str(prolate_json) if prolate_json else 'floating_gauss_inverse','cells':cells,'log_seed_max':logmax,'physical_seed_max':float(e[-1]),'rank':rank,'quadrature':quad,'seed_quadrature':seedquad,'grid_per_log2':nper,'output_log_max':tout,'gram_drop_relative':drop,'retained_dimension':int(np.sum(keep)),'G_min':float(ev[0]),'G_max':float(ev[-1]),'N_min':float(np.linalg.eigvalsh(N)[0]),'B_finite_output':float(np.trace(whiten)),'trace_minus_Q_upper':float(np.trace(whiten)-1.047808594),'largest_response_eigenvalues':vals[-10:][::-1].tolist(),'dimension_capture':{str(k):float(np.sum(vals[-k:])) for k in [5,10,20,40,80] if k<=len(vals)},'whitening_defect_frobenius':float(np.linalg.norm(W.T@G@W-np.eye(W.shape[1]))),'elapsed_seconds':time.time()-started,'uncontrolled_errors':['finite output quadrature','compact Gram quadratures','floating sine-integral evaluation and cancellation','source normalization/interpolation','finite-rank prolate inverse error not propagated']}
 return ans

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--cells',type=int,default=80);p.add_argument('--logmax',type=float,default=2.8);p.add_argument('--rank',type=int,default=24);p.add_argument('--quad',type=int,default=240);p.add_argument('--seedquad',type=int,default=20);p.add_argument('--nper',type=int,default=1024);p.add_argument('--tout',type=float,default=4.);p.add_argument('--drop',type=float,default=1e-8);p.add_argument('--prolate-json',type=Path);p.add_argument('--output',type=Path);args=p.parse_args();kw=vars(args).copy();out=kw.pop('output');r=run(**kw);print(json.dumps(r),flush=True)
 if out:out.write_text(json.dumps(r,indent=2)+'\n')
