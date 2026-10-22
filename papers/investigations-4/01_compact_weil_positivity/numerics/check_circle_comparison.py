#!/usr/bin/env python3
"""Bounded controls for I4-W01. Analytic proofs are in Note 01.
Prepared for Edward Baker with LLM assistance, gpt-6-astra, effort ultra.
Exact integer controls and double-precision diagnostics; no interval certificate.
Requires Python 3.10+ and NumPy. Writes a small receipt to --output.
"""
from __future__ import annotations
import argparse, cmath, hashlib, json, math, platform, sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np

def polyadd(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return c

def polymul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def shift(a,u):
 c=[F(0)]*len(a)
 for j,x in enumerate(a):
  for i in range(j+1):c[i]+=x*math.comb(j,i)*(-u)**(j-i)
 return c

def corr(u,odd):
 seg=[(F(-1),F(0),[F(1),F(1)]),(F(0),F(1),[F(1),F(-1)])]
 if odd:seg=[(a,b,[F(0)]+p) for a,b,p in seg]
 ans=F(0)
 for a,b,p in seg:
  for c,d,q in seg:
   lo=max(a,c+u);hi=min(b,d+u)
   if hi<=lo:continue
   v=polymul(p,shift(q,u))
   ans+=sum(x*(hi**(j+1)-lo**(j+1))/F(j+1) for j,x in enumerate(v))
 return ans

def interpolate(xs,ys):
 out=[F(0)]
 for i,x in enumerate(xs):
  p=[ys[i]]
  for j,y in enumerate(xs):
   if i!=j:p=[z/(x-y) for z in polymul(p,[-y,F(1)])]
  out=polyadd(out,p)
 return out

def digamma(z):
 # Recurrence to Re z>=20, then Bernoulli expansion; floating diagnostic only.
 z=np.asarray(z,dtype=complex);ans=np.zeros_like(z)
 for _ in range(20):ans-=1/z;z=z+1
 ans+=np.log(z)-1/(2*z)
 for j,b in enumerate([1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6],1):
  ans-=b/(2*j*z**(2*j))
 return ans

def prime_data(X):
 out=[]
 for p in range(2,X+1):
  if any(p%d==0 for d in range(2,math.isqrt(p)+1)):continue
  n=p
  while n<=X:out.append((n,math.log(p)/math.sqrt(n)));n*=p
 return sorted(out)

def quad(fun,a,b,order=128):
 x,w=np.polynomial.legendre.leggauss(order);u=(b-a)*x/2+(a+b)/2
 return float(np.dot(w,fun(u))*(b-a)/2)

def kernel(s):return np.exp(-s/2)/(-np.expm1(-2*s))

def main():
 if not __debug__:
  raise SystemExit("Checks require assertions: rerun without -O or PYTHONOPTIMIZE.")
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 exact=0
 # Integer complex cyclic translations: ||g-Ug||²=2||g||²-2Re<g,Ug>.
 for n in [3,5,8]:
  vals=[(i*i-3*i+1,2*i-5) for i in range(n)]
  for d in range(n):
   norm=sum(x*x+y*y for x,y in vals)
   inner=sum(x*vals[(i-d)%n][0]+y*vals[(i-d)%n][1] for i,(x,y) in enumerate(vals))
   jump=sum((x-vals[(i-d)%n][0])**2+(y-vals[(i-d)%n][1])**2 for i,(x,y) in enumerate(vals))
   assert jump==2*norm-2*inner;exact+=1
 # Elementary arithmetic lower bound: each central binomial divides the lcm.
 for n in range(1,101):
  lcm=1
  for k in range(1,2*n+1):lcm=math.lcm(lcm,k)
  assert lcm%math.comb(2*n,n)==0;exact+=1
 # Exact piecewise autocorrelations; extra points test the interpolation independently.
 polys={}
 for odd in [False,True]:
  pair=[]
  for left in [0,1]:
   xs=[F(left)+F(j,5) for j in range(6)]
   p=interpolate(xs,[corr(x,odd) for x in xs]);pair.append(p)
   for j in range(1,8):
    x=F(left)+F(j,8)
    assert sum(c*x**i for i,c in enumerate(p))==corr(x,odd);exact+=1
  polys[odd]=pair
 # Kernel image sum: different indices on each side, with signed-offset controls.
 kernel_errors=[]
 for P in [4.,8.,12.]:
  for t in [-1.,-.25,0.,.75,1.]:
   lhs=sum(float(kernel(abs(t+j*P))) for j in range(-80,81) if j)
   rhs=sum(2*math.cosh((2*r+.5)*t)/math.expm1((2*r+.5)*P) for r in range(20))
   err=abs(lhs-rhs);kernel_errors.append(err);assert err<2e-14
 a0=-0.5772156649015328606-math.pi/2-3*math.log(2)-math.log(math.pi)
 assert abs(float(digamma(.25).real)-math.log(math.pi)-a0)<2e-14
 L=2.;P=8.;primes=prime_data(8);W=sum(c for _,c in primes);D=2*W-a0
 cases=[]
 for odd in [False,True]:
  norm=float(corr(F(0),odd));coef=[np.array([float(x) for x in p]) for p in polys[odd]]
  def R(u):
   u=np.asarray(u);return np.where(u<=1,np.polynomial.polynomial.polyval(u,coef[0]),np.polynomial.polynomial.polyval(u,coef[1]))
  # Real-line gamma form: autocorrelation integral, no Fourier summation.
  def integrand(u):return 2*kernel(u)*(norm-R(u))
  tail=sum(math.exp(-(2*r+.5)*2)/(2*r+.5) for r in range(40))
  AR=a0*norm+quad(integrand,0,1)+quad(integrand,1,2)+2*norm*tail
  def f(x):return (x if odd else np.ones_like(x))*(1-np.abs(x))
  moments=[]
  for r in range(12):
   lam=2*r+.5
   C=quad(lambda x:f(x)*np.cosh(lam*x),-1,0)+quad(lambda x:f(x)*np.cosh(lam*x),0,1)
   S=quad(lambda x:f(x)*np.sinh(lam*x),-1,0)+quad(lambda x:f(x)*np.sinh(lam*x),0,1)
   moments.append((C,S))
  image=sum(2*(C*C-S*S)/math.expm1((2*r+.5)*P) for r,(C,S) in enumerate(moments))
  C,S=moments[0];prime=-2*sum(c*float(corr(F(str(math.log(n))),odd)) if math.log(n)<2 else 0 for n,c in primes)
  Q=AR+2*C*C-2*S*S+prime
  estimates=[]
  for N in [1024,4096]:
   k=np.arange(1,N+1);tau=2*np.pi*k/P
   ft=(1j*(2*np.sin(tau)/tau**2-4*(1-np.cos(tau))/tau**3)) if odd else 2*(1-np.cos(tau))/tau**2
   a=digamma(.25+.5j*tau).real-np.log(np.pi)
   AP=(a0*(0 if odd else 1)+2*np.dot(a,np.abs(ft)**2))/P
   delta=AR-AP-image
   assert abs(delta)<2e-7
   estimates.append({'N':N,'A_circle_truncated':float(AP),'gamma_identity_residual':float(delta)})
  assert (image<0)==odd
  AP=estimates[-1]['A_circle_truncated'];Qcircle=AP+2*C*C-2*S*S+prime
  E=AP-a0*norm+sum(2*c*(norm-(float(corr(F(str(math.log(n))),odd)) if math.log(n)<2 else 0)) for n,c in primes)+2*C*C
  assert E>0
  assert abs((E-Qcircle)-(D*norm+2*S*S))<2e-13
  epsilon_bound=2*math.exp(-(P-L)/2)/((1-math.exp(-P/2))*(1-math.exp(-2*(P-L))))
  l1=quad(lambda x:np.abs(f(x)),-1,0)+quad(lambda x:np.abs(f(x)),0,1)
  assert abs(image)<=epsilon_bound*l1*l1
  cases.append({'test':'x*(1-|x|)_+' if odd else '(1-|x|)_+','norm_squared':norm,'Q_real_diagnostic':Q,'image':image,'image_bound':epsilon_bound*l1*l1,'positive_completion':E,'completion_excess_diagnostic':E-Q,'limiting_excess':D*norm+2*S*S,'fourier_checks':estimates})
 # Explicit delocalized odd circle witness, with complete poles.
 P=16.;beta=2*math.pi/P;h=float(digamma(.25+.5j*beta).real)-math.log(math.pi)-2*sum(c*math.cos(beta*math.log(n)) for n,c in primes)
 pole=-16*beta*beta/P*math.sinh(P/4)**2/(.25+beta*beta)**2
 assert h<0 and h+pole<0
 receipt={'classification':'exact integer/rational controls plus double-precision diagnostics; not an interval certificate or theta zero computation','prepared_for':'Edward Baker','date_local':'2026-10-21','model':'gpt-6-astra','effort':'ultra','python':platform.python_version(),'python_optimize':sys.flags.optimize,'numpy':np.__version__,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_checks':exact,'max_kernel_identity_error':max(kernel_errors),'tests':cases,'odd_circle_witness':{'P':P,'prime_cutoff':8,'diagonal_part':h,'negative_pole_part':pole,'form_value':h+pole},'status':'PASS'}
 args.output.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'PASS','exact_checks':exact,'max_kernel_identity_error':max(kernel_errors),'max_gamma_residual':max(abs(v['gamma_identity_residual']) for c in cases for v in c['fourier_checks']),'output':str(args.output)}))
if __name__=='__main__':main()
