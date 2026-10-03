#!/usr/bin/env python3
"""Finite smooth source-space B_d,Q,K_d pilot; no enclosure or operator claim.
Prepared for Edward Baker, GPT-6 (Codex), effort/variant not exposed.
"""
import argparse, json, hashlib, platform, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.signal import fftconvolve
from scipy.special import digamma
from scipy.interpolate import CubicSpline
from scipy.integrate import cumulative_simpson
from numpy.polynomial import Legendre
from trial_geometry import geometry

def raw_sources(x,dim,mean_zero,b=.45):
 x=np.asarray(x);out=np.zeros((len(x),dim));sel=np.abs(x)<b;z=x[sel];q=1-(z/b)**2
 phi=np.exp(-1/q);l1=-2*z/(b*b*q*q);l2=-2/(b*b*q*q)-8*z*z/(b**4*q**3);l3=-24*z/(b**4*q**3)-48*z**3/(b**6*q**4)
 p1=phi*l1;p2=phi*(l1*l1+l2);p3=phi*(l1**3+3*l1*l2+l3)
 for n in range(dim):
  pol=Legendre.basis(n);vv=[pol.deriv(k)(z/b)/b**k if k<=n else np.zeros_like(z) for k in range(4)]
  if mean_zero:out[sel,n]=-p3*vv[0]-3*p2*vv[1]-3*p1*vv[2]-phi*vv[3]+.25*(p1*vv[0]+phi*vv[1])
  else:out[sel,n]=-p2*vv[0]-2*p1*vv[1]-phi*vv[2]+.25*phi*vv[0]
 return out

def whiten_sources(dim,mean_zero,source_grid):
 x=np.linspace(-.45,.45,source_grid+1);raw=raw_sources(x,dim,mean_zero)
 gram=np.trapezoid(raw[:,:,None]*raw[:,None,:],x,axis=0)
 # Cholesky whitening preserves the parity separation up to roundoff.
 L=np.linalg.cholesky(gram);U=np.linalg.solve(L.T,np.eye(dim));f=raw@U
 return x,f,U,float(np.linalg.cond(gram))

def arithmetic(x,f,pad):
 dx=x[1]-x[0];m=(len(x)-1)*pad;t=2*np.pi*np.fft.fftfreq(m,dx);ft=np.fft.fft(f,m,axis=0)*dx
 gam=np.real(digamma(.25+.5j*t))-np.log(np.pi)
 Gamma=np.real(ft.conj().T@(gam[:,None]*ft))/(m*dx)
 fs=CubicSpline(x,f,axis=0,extrapolate=False);a=np.log(2.);shift=np.nan_to_num(fs(x+a))
 cor=np.trapezoid(f[:,:,None]*shift[:,None,:],x,axis=0)
 prime=a/np.sqrt(2)*(cor+cor.T)
 return (Gamma-prime+Gamma.T-prime.T)/2,Gamma,prime

def diagforms(B,Q):
 K=(B-Q+B.T-Q.T)/2;k,V=np.linalg.eigh(K);Kp=(V*np.maximum(k,0))@V.T
 ev,U=np.linalg.eigh(B);keep=ev>max(ev[-1]*1e-12,0);W=U[:,keep]/np.sqrt(ev[keep]);gen=np.linalg.eigvalsh(W.T@K@W)
 bpk=B-Kp
 return {'B_matrix':B.tolist(),'Q_matrix':Q.tolist(),'K_d_matrix':K.tolist(),'K_d_positive_part':Kp.tolist(),'B_minus_K_d_positive_part':bpk.tolist(),'B_eigenvalues':ev.tolist(),'Q_eigenvalues':np.linalg.eigvalsh(Q).tolist(),'K_d_eigenvalues':k.tolist(),'B_minus_K_d_positive_part_eigenvalues':np.linalg.eigvalsh(bpk).tolist(),'generalized_K_d_over_B_eigenvalues':gen.tolist(),'commutator_B_Q_frobenius':float(np.linalg.norm(B@Q-Q@B))}

def run(dim=6,mean_zero=False,cells=160,nper=1024,logmax=3.5,tout=4.5,source_grid=16384,pad=16,ancestor_numerics=None):
 start=time.time();x,f,U,source_cond=whiten_sources(dim,mean_zero,source_grid)
 Q,Gamma,prime=arithmetic(x,f,pad)
 geom=geometry(cells=cells,logmax=logmax,rank=32,quad=400,seedquad=24,ancestor_numerics=ancestor_numerics)
 lo,hi,sq,hh,W=[geom[k] for k in ['lo','hi','sq','hh','W']]
 a=np.log(2.);r=2**-.5;dt=a/nper;nin=int(np.ceil((tout+.46)/dt));u=(np.arange(nin)+.5)*dt
 J=int(np.ceil(.45/dt));v=np.arange(-J,J+1)*dt;fv=raw_sources(v,dim,mean_zero)@U
 hlog=np.sqrt(np.exp(u))[:,None]*hh(np.exp(u));responses=[]
 for k in range(dim):
  cv=fftconvolve(hlog,fv[:,k,None],mode='full',axes=0)*dt
  ts=(np.arange(len(cv))+.5-J)*dt;inds=np.where((ts>=-.45)&(ts<tout))[0];out=ts[inds]
  cvD=cv[inds].copy();valid=inds>=nper;cvD[valid]-=r*cv[inds[valid]-nper]
  anti=cumulative_simpson(f[:,k]*np.exp(-x/2),x=x,initial=0);ac=CubicSpline(x,anti)
  def bsmooth(tt):
   tt=tt[:,None];return np.exp(tt/2)/sq*(ac(np.clip(tt-np.log(lo),-.45,.45))-ac(np.clip(tt-np.log(hi),-.45,.45)))
  resp=bsmooth(out)-r*bsmooth(out-a)-cvD
  responses.append(((resp@W)*np.sqrt(dt)).ravel())
 responses=np.stack(responses);B=responses@responses.T
 result={'status':'FLOATING_SOURCE_SPACE_PILOT_NOT_CERTIFIED','date':'2026-10-03','model':'GPT-6 (Codex)','reasoning_effort':'not exposed','source_preparation':'A d/dx(phi P_n)' if mean_zero else 'A(phi P_n)','source_dim':dim,'mean_zero_exact_by_preparation':mean_zero,'pole_neutral_exact_by_preparation':True,'source_grid':source_grid,'frequency_padding':pad,'source_orthonormalizer':U.tolist(),'source_gram_condition':source_cond,'source_orthonormality_error':float(np.linalg.norm(np.trapezoid(f[:,:,None]*f[:,None,:],x,axis=0)-np.eye(dim))),'source_means':np.trapezoid(f,x,axis=0).tolist(),'approximate_pole_moment_residuals':{str(sign):np.trapezoid(f*np.exp(sign*x[:,None]/2),x,axis=0).tolist() for sign in [-1,1]},'trial_cells':cells,'seed_log_max':logmax,'output_log_max':tout,'nper_log2':nper,'trial_G_min':geom['G_min'],'trial_retained':geom['retained'],'inherited_prolate':geom['inherited_prolate'],'quadrature_failures':{'nonfinite_detected':False,'rigorous_error_test':'not implemented; fixed quadrature has no certified failure/success criterion'},'Gamma_matrix':Gamma.tolist(),'prime_matrix':prime.tolist(),**diagforms(B,Q),'runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'platform':platform.platform()},'elapsed_seconds':time.time()-start,'limitations':['B_d is a theoretical lower quadratic form only before floating errors; no certified interval is claimed.','K_d=B_d-Q underestimates K only in the exact Galerkin construction; omitted B may alter the positive-part comparison.','The positive part of a source compression is not in general the compression of the full positive part.','No omitted source-space control; finite-family tests do not prove the revised all-source inequality.','All compact Gram, Fourier, convolution and source quadratures are unenclosed.']}
 # LARGE_FILES policy: persist summaries and hashes, not derived matrix arrays.
 matrix_keys=['B_matrix','Q_matrix','K_d_matrix','K_d_positive_part','B_minus_K_d_positive_part','Gamma_matrix','prime_matrix','source_orthonormalizer']
 result['derived_array_sha256']={key:hashlib.sha256(json.dumps(result[key],separators=(',',':'),allow_nan=False).encode()).hexdigest() for key in matrix_keys}
 result['derived_array_hash_format']='UTF-8 json.dumps(array,separators=(comma,colon),allow_nan=False), standard Python float formatting; no newline.'
 Be,V=np.linalg.eigh(B);BW=V/np.sqrt(Be)
 result['relative_positive_part_max']=float(np.linalg.eigvalsh(BW.T@np.array(result['K_d_positive_part'])@BW)[-1])
 result['opposite_parity_B_max']=max(abs(B[i,j]) for i in range(dim) for j in range(dim) if(i-j)%2)
 if not all(np.all(np.isfinite(result[key])) for key in matrix_keys):raise ArithmeticError('Nonfinite derived array; refusing output')
 for key in matrix_keys:del result[key]
 return result

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--dim',type=int,default=6);p.add_argument('--mean-zero',action='store_true');p.add_argument('--cells',type=int,default=160);p.add_argument('--nper',type=int,default=1024);p.add_argument('--logmax',type=float,default=3.5);p.add_argument('--tout',type=float,default=4.5);p.add_argument('--source-grid',type=int,default=16384);p.add_argument('--pad',type=int,default=16);p.add_argument('--ancestor-numerics',type=Path);p.add_argument('--output',type=Path,required=True);a=vars(p.parse_args());o=a.pop('output');res=run(**a);res['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();res['geometry_script_sha256']=hashlib.sha256(Path(__file__).with_name('trial_geometry.py').read_bytes()).hexdigest();o.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:res[k] for k in ['status','source_dim','mean_zero_exact_by_preparation','trial_cells','B_eigenvalues','Q_eigenvalues','K_d_eigenvalues','B_minus_K_d_positive_part_eigenvalues','generalized_K_d_over_B_eigenvalues','commutator_B_Q_frobenius','elapsed_seconds']}),flush=True)
