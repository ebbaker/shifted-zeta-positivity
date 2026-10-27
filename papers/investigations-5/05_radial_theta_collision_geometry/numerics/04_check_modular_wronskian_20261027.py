"""Exact algebra and rational source bounds for RTC-03 Note05.
Prepared for Edward Baker with substantial LLM assistance.
gpt-6-astra, recorded effort max; 27 October 2026.
The analytical large-frequency remainder and sign-change proof live in Note05.
No physical theta transform values, zeros or windings are sampled.
"""
import json
from pathlib import Path

from fractions import Fraction as F

N=10
class P:
    def __init__(self,v=0):
        self.d={k:F(x) for k,x in v.items() if x} if isinstance(v,dict) else ({(0,)*N:F(v)} if v else {})
    def __add__(self,o):
        o=o if isinstance(o,P) else P(o); d=dict(self.d)
        for k,v in o.d.items(): d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+-toP(o)
    def __rsub__(self,o): return toP(o)+-self
    def __mul__(self,o):
        o=toP(o);d={}
        for k,v in self.d.items():
            for l,w in o.d.items():
                m=tuple(a+b for a,b in zip(k,l)); d[m]=d.get(m,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,o): return self*F(1,o)
    def __pow__(self,n):
        out=P(1)
        for _ in range(n):out=out*self
        return out
    def diff(self,j):
        d={}
        for k,v in self.d.items():
            if k[j]:
                l=list(k);l[j]-=1;d[tuple(l)]=v*k[j]
        return P(d)
    def eval(self,vals):
        return sum((v*product(vals[j]**k[j] for j in range(N)) for k,v in self.d.items()),P())
    def __eq__(self,o): return self.d==toP(o).d
    def show(self): return [(k,str(v)) for k,v in sorted(self.d.items())]
def toP(v):return v if isinstance(v,P) else P(v)
def product(xs):
    v=1
    for x in xs:v=v*x
    return v
def var(j):
    k=[0]*N;k[j]=1;return P({tuple(k):1})
a,c,e,t=[var(j) for j in range(4)]
da=2*a-F(2,3)*a*(e+a+2*c)
dc=2*c-F(2,3)*c*(e-2*a-c)
de=2*e-F(1,3)*(e**2-a**2-a*c-c**2)
def D(p):return p.diff(0)*da+p.diff(1)*dc+p.diff(2)*de
ell=-(e+a-c)/6
R=D(ell)+ell**2+ell
polys=[R]
for _ in range(4):polys.append(D(polys[-1])+(F(1,2)+ell)*polys[-1])
at0=[p.eval([a,a,3,t]+[0]*6) for p in polys]
h0,h2,h4=at0[0],at0[2],at0[4]
g2=h2+t*h0/2
g4=h4+3*t*h2+F(3,4)*t**2*h0
disc=g2**2-h0*g4

# Scaled theta system and the exact modular weight.
assert D(a+c)==(2+4*ell)*(a+c)
wn=4*a*c
wd=(a+c)**2
assert D(wn)*wd-wn*D(wd)==2*(a-c)*wn*wd
assert h0==(2*a**2-3)/4
assert h2==(15-45*a**2-2*a**4)/8
assert h4==(-285+1800*a**2+191*a**4+102*a**6)/16
assert at0[1]==0 and at0[3]==0

# Full physical current, including the derivative of the multiplier.
y,v,z,u,g,lam,w,wp,delta,deltap=[var(j) for j in range(N)]
def physical_D(p):
    return p.diff(0)*v+p.diff(1)*(g-lam*y)+p.diff(2)*u+p.diff(3)*(-y-lam*z)+p.diff(6)*wp
W=y*u-v*z
assert physical_D(W)==-y**2-g*z
Qw=w*(y**2+g*z)-wp*W
assert physical_D(w*W)==-Qw

# Conjugation by h=sqrt(w). The forcing survives exactly.
h=w
U=h*y
Ux=h*(v+delta*y)
Uxx=h*(g-lam*y+2*delta*v+(deltap+delta**2)*y)
assert Uxx-2*delta*Ux+(lam+delta**2-deltap)*U==h*g
UZ=h*z
UZx=h*(u+delta*z)
assert U*UZx-Ux*UZ==h**2*W

# The positive Gaussian-polynomial collision remains an exact cancellation.
x=var(0)
gstar=16*x**4+24
ystar=4*x**2+4
zstar=P(-1)
def gaussian_D(p): return p.diff(0)-2*x*p
assert gaussian_D(gaussian_D(ystar))+6*ystar==gstar
assert gaussian_D(gaussian_D(zstar))+6*zstar==-ystar
Wstar=ystar*gaussian_D(zstar)-gaussian_D(ystar)*zstar
assert Wstar==8*x
assert ystar**2+gstar*zstar==32*x**2-8
assert w*(ystar**2+gstar*zstar)-wp*Wstar==-(wp*Wstar+w*(Wstar.diff(0)-4*x*Wstar))

# The leading large-lambda integrand coefficient, before any inequality.
j0,j1,j2,j3,j4,j5,eps,ww,wwp,_=[var(j) for j in range(N)]
YY=j0*eps-j2*eps**2+j4*eps**3
ZZ=-j0*eps**2+2*j2*eps**3-3*j4*eps**4
YYx=j1*eps-j3*eps**2+j5*eps**3
ZZx=-j1*eps**2+2*j3*eps**3-3*j5*eps**4
qq=ww*(YY**2+j0*ZZ)-wwp*(YY*ZZx-YYx*ZZ)
def coefficient(p,j,n):
    d={}
    for k,vv in p.d.items():
        if k[j]==n:
            kk=list(k);kk[j]=0;d[tuple(kk)]=vv
    return P(d)
assert all(coefficient(qq,6,n)==0 for n in range(4))
leading=ww*(j2**2-j0*j4)-wwp*(j0*j3-j1*j2)
assert coefficient(qq,6,4)==leading
flux=ww*(j0*j3-j1*j2)
dflux=sum((flux.diff(j)*var(j+1) for j in range(5)),P())+flux.diff(7)*wwp
assert leading==-dflux

# Rational enclosures: pi, exp(-pi), theta_3(i), then v=pi^2 theta_3(i)^8/4.
tan_two=2*F(1,5)/(1-F(1,5)**2)
tan_four=2*tan_two/(1-tan_two**2)
assert (tan_four-F(1,239))/(1+tan_four*F(1,239))==1
def atan_bounds(q,n=8):
    s=sum(((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    next_term=q**(2*n+1)/F(2*n+1)
    return (s,s+next_term) if n%2==0 else (s-next_term,s)
lo5,hi5=atan_bounds(F(1,5))
lo239,hi239=atan_bounds(F(1,239))
pi_lo=16*lo5-4*hi239
pi_hi=16*hi5-4*lo239
assert F(157,50)<pi_lo<pi_hi<F(22,7)
def exp_bounds(r,n=24):
    term=F(1);s=term
    for k in range(1,n+1):
        term*=r/k;s+=term
    following=term*r/(n+1)
    assert r/(n+2)<1
    return s,s+following/(1-r/(n+2))
assert exp_bounds(F(157,50))[0]>F(250,11)
assert exp_bounds(F(22,7))[1]<F(1000,43)
qlo,qhi=F(43,1000),F(11,250)
klo,khi=F(543,500),F(1089,1000)
assert 1+2*qlo==klo
assert 1+2*(qhi+qhi**4/(1-qhi**5))<khi
vlo,vhi=F(47,10),F(49,10)
assert F(157,50)**2*klo**8/4>vlo
assert F(22,7)**2*khi**8/4<vhi

def H0(vv):return (2*vv-3)/4
def H2(vv):return (15-45*vv-2*vv**2)/8
def H4(vv):return (-285+1800*vv+191*vv**2+102*vv**3)/16
assert H0(vlo)==F(8,5) and H0(vhi)==F(17,10)
# H2 decreases and H4 increases throughout the positive interval.
assert -32<H2(vhi)<H2(vlo)<-30
assert H4(vhi)>H4(vlo)>1430
# 0<=t<=1/2: g2/K lies in [-32,-1183/40], g4/K>=1382.
g2_upper=-30+F(1,4)*F(17,10)
g4_lower=F(1430)-F(3,2)*32
disc_upper=32**2-F(8,5)*g4_lower
assert g2_upper==F(-1183,40)<0
assert g4_lower==1382 and disc_upper==F(-5936,5)<0

record={
    'date':'2026-10-27', 'prepared_for':'Edward Baker',
    'llm_assistance':'substantial', 'model':'gpt-6-astra', 'effort':'max',
    'status':'passed', 'arithmetic':'Python standard-library Fraction',
    'checked':[
        'Scaled nonlinear theta differential algebra and source derivatives through order four',
        'Modular weight logarithmic derivative, with no omitted multiplier term',
        'Complete weighted Wronskian and forced conjugated equation',
        'Exact Gaussian-polynomial collision cancellation for arbitrary scalar multiplier',
        'Leading large-frequency integrand is a complete derivative',
        'Rational complete-source constant enclosure and uniform endpoint sign'
    ],
    'source_bounds':{
        'pi':['157/50','22/7'], 'exp_minus_pi':['43/1000','11/250'],
        'theta3_i':['543/500','1089/1000'],
        'v_pi_squared_theta3_i_power8_over4':['47/10','49/10'],
        'physical_time_interval':['0','1/2'],
        'g2_over_theta3_interval':['-32','-1183/40'],
        'g4_over_theta3_lower':'1382',
        'endpoint_discriminant_over_theta3_squared_upper':'-5936/5'
    },
    'source_jet_polynomials_in_v':{
        'g0_at_t0_over_theta3':'(2*v-3)/4',
        'g2_at_t0_over_theta3':'(15-45*v-2*v^2)/8',
        'g4_at_t0_over_theta3':'(-285+1800*v+191*v^2+102*v^3)/16'
    },
    'physical_theta_sampling':False, 'canonical_source_constant_enclosure':True,
    'numerical_frequency_onset':None,
    'analytical_obligations_in_note':[
        'Imported theta identities and canonical modular normalization',
        'Full-source convergence and physical response asymptotic remainders',
        'Uniform eventual sign change of the actual integrand',
        'Boundary and source selection, scope of the obstruction'
    ],
    'canonical_collision_exclusion':False, 'independent_review':False
}
out=Path(__file__).with_name('04_MODULAR_WRONSKIAN_CHECKS_20261027.json')
if __name__=='__main__':
    out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':record['status'],'record':str(out),'endpoint_upper':str(disc_upper),'physical_theta_sampling':False}))
