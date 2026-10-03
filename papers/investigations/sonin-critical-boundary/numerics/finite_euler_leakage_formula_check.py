"""Floating-point checks of the full-output Gram formulas; NOT a certificate.

Run with Python, NumPy and SciPy. No artifacts are written. The mathematical
tail bounds are in ../notes/FINITE_EULER_RANK_ONE_ANALYSIS_20261003.md.
"""

import numpy as np
from scipy.special import sici
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss
p=2.; N=4
terms=[(-1,-1/p)]+[(n,1-1/p) for n in range(N)]
def J(x): return x*sici(x)[0]+np.cos(x)-1
def I(a,b): return .5*(J(a+b)-J(a-b))
def gram(m,n,ai,bi,aj,bj):
 s=0.
 for x,sx in [(bi,1),(ai,-1)]:
  for y,sy in [(bj,1),(aj,-1)]:s+=sx*sy*I(2*np.pi*p**m*x,2*np.pi*p**n*y)
 return s/(np.pi**2*p**(m+n)*np.sqrt((bi-ai)*(bj-aj)))
def B(n,a,b,x):
 z=2*np.pi*p**n*x
 return 2*((b*np.sinc(z*b/np.pi))-(a*np.sinc(z*a/np.pi)))/np.sqrt(b-a)
errs=[]
for m,n,aa,bb,cc,dd in [(-1,2,0,.2,.2,.55),(3,3,.1,.7,1.,1.8),(0,1,.4,1.,.2,.3)]:
 val=quad(lambda x:B(m,aa,bb,x)*B(n,cc,dd,x),0,1,epsabs=1e-12,epsrel=1e-12)[0]
 errs.append(abs(gram(m,n,aa,bb,cc,dd)-val))
bd=np.linspace(0,1,7); k=len(bd)-1
H=np.zeros((k,k));D=np.zeros((k,k))
for i in range(k):
 for j in range(k):
  a,b,c,d=bd[i],bd[i+1],bd[j],bd[j+1]
  D[i,j]=sum(co*2/(2*np.pi*p**n)*sum(sx*sy*sici(2*np.pi*p**n*x*y)[0] for x,sx in [(b,1),(a,-1)] for y,sy in [(d,1),(c,-1)])/np.sqrt((b-a)*(d-c)) for n,co in terms)
  H[i,j]=sum(co*do*gram(m,n,a,b,c,d) for m,co in terms for n,do in terms)
x,w=leggauss(500);x=(x+1)/2;w=w/2
CE=np.array([sum(co*B(n,bd[i],bd[i+1],x) for n,co in terms) for i in range(k)]).T
Hq=CE.T@(w[:,None]*CE)
print({'single_gram_errors':errs,'H_quadrature_max_error':float(np.max(np.abs(H-Hq))),'leakage_Gram_min_eigenvalue':float(np.linalg.eigvalsh(H-D@D)[0]),'leakage_trace':float(np.trace(H-D@D))})
