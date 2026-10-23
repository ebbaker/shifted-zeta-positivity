"""Small floating diagnostics for HDC-08; not an interval certificate."""
import json, math
from fractions import Fraction as Q
import numpy as np

checks={}
# Exact controls using rational formulas.
checks['quadratic_resolvent_pole']={
 'tau_pole':str(Q(-1,4)), 'discriminant_at_pole':str(4*(1+2*Q(-1,4))),
 'tau_collision':str(Q(-1,2)), 'double_q':str(Q(1,2)),
 'triple_q':str(Q(1,2)+Q(2,3))}
for x in [Q(1),Q(3,2),Q(2)]:
 t=(x*x-9)/2; v=1/x
 assert x*x-9-2*t==0 and x*v==1 and 2*x!=0
checks['graph_fold']={'sample_x':['1','3/2','2'],'frozen_derivatives_nonzero':True,'slope_times_velocity':'1'}
checks['graph_negative_orientation']={'x':1,'slope_times_velocity':2,'jacobian':-4}
# A relative wall-error example and coefficients: normalized y=z/2.
eps=0.03; radius=2.; eta=eps/(radius*radius-1); K=-math.log1p(-eta)
Ek=[0.,K,2*K]; d=[0.,Ek[1],Ek[2]/2+Ek[1]**2/2]
cref=np.array([1.,0.,-0.25]); c=np.array([1.,0.,-(1+eps)/4])
C=np.array([0.,d[1],d[2]+abs(cref[1])*d[1]])
assert np.all(np.abs(c-cref)<=C+1e-15)
# Sylvester resultant S(P,P') for degree two.
def sylv2(c):
 return np.array([[1,c[1],c[2]],[2,c[1],0],[0,2,c[1]]],complex)
S=sylv2(c); Ss=sylv2(cref)
eS=math.sqrt(5*C[1]**2+C[2]**2)
ED=3*eS*(np.linalg.norm(Ss,2)+eS)**2
D=c[1]**2-4*c[2]; Ds=cref[1]**2-4*cref[2]
assert abs(D-Ds)<=ED
# Independent contour trapezoidal check of log moment identity.
angles=2*np.pi*(np.arange(4096)+.5)/4096
z=radius*np.exp(1j*angles); y=z/radius
ell=np.log((z*z-1-eps)/(z*z-1))
contour_p2=-2*np.mean(y*ell*z/radius)
assert abs(contour_p2-eps/2)<1e-12
checks['relative_wall_coefficient_discriminant']={
 'eta':eta,'K':K,'normalized_p2_change':eps/2,
 'log_integral_p2_change':[contour_p2.real,contour_p2.imag],
 'coefficient_error':np.abs(c-cref).tolist(),'coefficient_bound':C.tolist(),
 'discriminant_error':abs(D-Ds),'discriminant_bound':ED}
# Complex root perturbation and singular-value / resolvent estimate.
w=np.array([-1-.2j,.1+.3j,1.4-.1j]); dr=np.array([.01+.02j,-.015+.005j,.01-.01j]); z=w+dr
rho=np.abs(dr); a=.3+.1j; n=len(w)
def lap(r):
 L=np.zeros((n,n),complex)
 for i in range(n):
  for j in range(i):
   W=(r[i]-r[j])**-2
   L[i,i]+=W;L[j,j]+=W;L[i,j]-=W;L[j,i]-=W
 return L
E=np.zeros((n,n))
for i in range(n):
 for j in range(i):
  dij=abs(w[i]-w[j]); rij=rho[i]+rho[j]
  E[i,j]=E[j,i]=rij*(2*dij+rij)/(dij*dij*(dij-rij)**2)
EL=2*np.max(np.sum(E,axis=1)); L=lap(z); Ls=lap(w)
delta=np.linalg.svd(np.eye(n)+a*L,compute_uv=False)[-1]
deltas=np.linalg.svd(np.eye(n)+a*Ls,compute_uv=False)[-1]
assert deltas>abs(a)*EL
q=np.trace(np.eye(n)-np.linalg.inv(np.eye(n)+a*L)); qs=np.trace(np.eye(n)-np.linalg.inv(np.eye(n)+a*Ls))
Eq=n*abs(a)*EL/(deltas*(deltas-abs(a)*EL))
assert np.linalg.norm(L-Ls,2)<=EL
assert delta>=deltas-abs(a)*EL
assert abs(q-qs)<=Eq
checks['complex_resolvent_stability']={
 'L_error':float(np.linalg.norm(L-Ls,2)),'L_bound':float(EL),
 'actual_smin':float(delta),'proved_smin_fallback':float(deltas-abs(a)*EL),
 'q_error':float(abs(q-qs)),'q_bound':float(Eq)}
# Check nonholomorphic weighted-moment sign on F=z+alpha*bar(z)-b.
# Choose b so the one graph zero lies outside the unit disk: no singular area integrand.
alpha=.2; b=2.; nt=2048; nr=256
th=2*np.pi*(np.arange(nt)+.5)/nt
zc=np.exp(1j*th); dz=1j*zc
F=zc+alpha*np.conj(zc)-b; dF=dz+alpha*np.conj(dz)
boundary=np.mean(zc*dF/F)/1j
rr=(np.arange(nr)+.5)/nr
area=0j
for r in rr:
 zz=r*np.exp(1j*th); ff=zz+alpha*np.conj(zz)-b
 area+=np.mean(alpha/ff)*r*(2*np.pi/nr)
weighted=boundary+area/np.pi
assert abs(weighted)<1e-7
checks['graph_moment_area_sign']={'boundary':[boundary.real,boundary.imag],
 'area_over_pi':[area.real/np.pi,area.imag/np.pi],
 'corrected_zero_moment_abs':abs(weighted)}
record={'date':'2026-10-23','prepared_for':'Edward Baker','model':'gpt-6-astra','effort':'ultra',
 'acknowledgement':'Developed with substantial LLM assistance.',
 'status':'exact rational controls and floating diagnostics; no theta certificate', 'checks':checks}
print(json.dumps(record,indent=2))
