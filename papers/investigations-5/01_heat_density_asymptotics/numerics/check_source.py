#!/usr/bin/env python3
"""HDA-17-AN02: six exact-rational adaptive source controls.

Prepared for Edward Baker with substantial LLM assistance, gpt-6.1-sol,
reasoning effort ultra (parent session metadata). No source/interval claim.
No external packages. All Taylor coefficients are fractions; order 4.
"""
from fractions import Fraction as Q
import hashlib
import json
import platform
from pathlib import Path
import sys
import time

ORDER=4
ZERO=(0,0,0)
class J:
    def __init__(self, data=0):
        if isinstance(data,J): self.c=dict(data.c)
        elif isinstance(data,dict): self.c={k:Q(v) for k,v in data.items() if v}
        else: self.c={ZERO:Q(data)} if data else {}
    def __add__(self,other):
        other=J(other); d=dict(self.c)
        for k,v in other.c.items(): d[k]=d.get(k,Q(0))+v
        return J(d)
    __radd__=__add__
    def __neg__(self): return J({k:-v for k,v in self.c.items()})
    def __sub__(self,other): return self+-J(other)
    def __rsub__(self,other): return J(other)+-self
    def __mul__(self,other):
        other=J(other); d={}
        for a,u in self.c.items():
            for b,v in other.c.items():
                k=tuple(a[i]+b[i] for i in range(3))
                if sum(k)<=ORDER: d[k]=d.get(k,Q(0))+u*v
        return J(d)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0: return self.inv()**(-n)
        out=J(1)
        while n:
            if n&1: out=out*self
            self=self*self; n//=2
        return out
    def inv(self):
        a=self.value(); assert a
        u=(self-a)*(1/a); out=J(1); power=J(1)
        for k in range(1,ORDER+1):
            power=power*(-u); out=out+power
        return out*(1/a)
    def __truediv__(self,other): return self*J(other).inv()
    def __rtruediv__(self,other): return J(other)*self.inv()
    def d(self,i,n=1):
        out=self
        for _ in range(n):
            d={}
            for k,v in out.c.items():
                if k[i]:
                    q=list(k); q[i]-=1; d[tuple(q)]=v*k[i]
            out=J(d)
        return out
    def value(self): return self.c.get(ZERO,Q(0))
    def log_derivatives(self):
        # Constant is log(D0); set it to 0 because all identities differentiate S,r.
        a=self.value(); assert a>0
        u=(self-a)*(1/a); out=J(0); power=J(1)
        for k in range(1,ORDER+1):
            power=power*u; out=out+power*Q((-1)**(k+1),k)
        return out

def lap(f): return f.d(1,2)+f.d(2,2)
def box(f): return f.d(1,2)-f.d(2,2)
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def cscale(a,b): return (a[0]*b,a[1]*b)
def cd(a,i,n=1): return (a[0].d(i,n),a[1].d(i,n))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def bar_d(a): return ((a[0].d(1)-a[1].d(2))/2,(a[1].d(1)+a[0].d(2))/2)
def creal(a): return a[0]
def cabs2(a): return a[0]**2+a[1]**2

def run_case(name,point):
    t0,x0,y0=map(Q,point)
    t=J({ZERO:t0,(1,0,0):1})
    x=J({ZERO:x0,(0,1,0):1})
    y=J({ZERO:y0,(0,0,1):1})
    if name=='scaled_linear':
        H=(10*x,10*y); F=((10+t)*x,(10+t)*y)
    elif name=='quadratic_linear_residual':
        H=(10*(x*x-y*y-2*t),20*x*y); F=(H[0]+t*x,H[1]+t*y)
    elif name=='quadratic_quadratic_residual':
        H=(10*(x*x-y*y-2*t),20*x*y); F=(H[0]+t*(x*x-y*y),H[1]+2*t*x*y)
    else: raise ValueError(name)
    root_q=2+t+t*t+x*x; q=root_q**2
    r=q.log_derivatives(); rt=r.d(0); rx=r.d(1); rxx=r.d(1,2)
    fz=cd(F,1); fzz=cd(F,1,2); E=add(cd(F,0),fzz); Ez=cd(E,1)
    D=cabs2(F)+q; S=D.log_derivatives(); w=q/D; c=w*(1-w)
    rho=q*cabs2(fz)/D**2                  # pi rho
    j=cscale(cmul(fzz,conj(fz)),q/D**2)   # pi j
    V0=cscale(cmul(fzz,conj(F)),1/D); V1=cscale(V0,w); V2=cscale(V1,w)
    Z0=cscale(cmul(E,conj(F)),1/D); Z1=cscale(Z0,w); Z2=cscale(Z1,w)
    C=lap(S)/4-rho                      # pi C
    b=rt+(rxx+rx*rx)/2; B=b*w
    source=(1-2*w)*(rt*rho+rx*j[0])       # pi signed source
    DE=2*q*creal(cmul(Ez,conj(fz)))/D**2-4*rho*creal(Z0)
    G=S.d(1)**2-S.d(2)**2
    checks={}
    def check(label,difference):
        v=difference.value()
        checks[label]=str(v)
        assert v==0,(name,point,label,str(v))
    check('CJ15_density',4*rho-(lap(S)-2*(w*rx).d(1)+w*rxx+c*rx*rx))
    jc=add(bar_d(V0),cscale(V1,rx/2))
    check('CJ16_current_real',j[0]-jc[0]); check('CJ16_current_imag',j[1]-jc[1])
    check('CJ16_covariance_integrand',G-(4*V0[0]-box(S)+(rxx+rx*rx)*w))
    check('CJ17_S_t',S.d(0)-(-2*V0[0]+rt*w+2*Z0[0]))
    check('CJ17_w_t',w.d(0)-(rt*c+2*V1[0]-2*Z1[0]))
    check('CJ17_c_t',c.d(0)-(rt*c*(1-2*w)+2*(V1[0]-2*V2[0])-2*(Z1[0]-2*Z2[0])))
    check('CJ18_residual',4*DE-(2*lap(Z0[0])+4*(Z1[0]*rx).d(1)-2*(Z1[0]*rxx+(Z1[0]-2*Z2[0])*rx*rx)))
    # Differentiate the weak density/curvature formula with every coefficient retained.
    density_t_weak=lap(S.d(0))-2*(w.d(0)*rx+w*rx.d(0)).d(1)+w.d(0)*rxx+w*rxx.d(0)+c.d(0)*rx*rx+2*c*rx*rx.d(0)
    check('density_t_all_regulator_terms',4*rho.d(0)-density_t_weak)
    curvature_direct=(2*w.d(1)*rx+w*rxx-c*rx*rx)/4
    check('curvature_spatial',C-curvature_direct)
    check('curvature_t',C.d(0)-curvature_direct.d(0))
    check('curvature_square',box(C)-box(curvature_direct))
    check('adaptive_potential',S.d(0)-(-box(S)/2-G/2+B+2*Z0[0]))
    density_rhs=-box(rho)/2-lap(G)/8+lap(B)/4-C.d(0)-box(C)/2+lap(Z0[0])/2
    check('adaptive_density',rho.d(0)-density_rhs)
    check('adaptive_current_source',rho.d(0)+j[0].d(1)+j[1].d(2)-source-DE)
    # Direct signed radial source, and the simplified local curvature identity.
    T=rt*cabs2(fz)+rx*creal(cmul(fzz,conj(fz)))
    signed_radial=q*(cabs2(F)-q)/D**3
    check('signed_radial_source',source-signed_radial*T)
    L1=cscale(cmul(fz,conj(F)),w/D)
    check('pointwise_curvature_simplified',4*C-(w*rxx+c*rx*rx-4*rx*L1[0]))
    check('pointwise_curvature_t_simplified',4*C.d(0)-(w.d(0)*rxx+w*rxx.d(0)+c.d(0)*rx*rx+2*c*rx*rx.d(0)-4*rx.d(0)*L1[0]-4*rx*L1[0].d(0)))
    # Exact residual-aware L1 time identity. It contains E_z explicitly.
    V13=cscale(cmul(cd(F,1,3),conj(F)),w/D)
    residual_L1=add(cscale(cmul(Ez,conj(F)),w/D),cscale(cmul(fz,conj(E)),q/D**2))
    residual_L1=add(residual_L1,cscale(L1,-4*Z0[0]))
    L1t_rhs=add(add(add(cscale(L1,rt*(1-2*w)),cscale(V13,-1)),cscale(conj(j),-1)),cscale(L1,4*V0[0]))
    L1t_rhs=add(L1t_rhs,residual_L1)
    check('L1_t_real_with_E_z',L1[0].d(0)-L1t_rhs[0])
    check('L1_t_imag_with_E_z',L1[1].d(0)-L1t_rhs[1])
    # Source transfer inequalities are checked at real points, using exact maxima
    # on the local amplitude interval. Five cases lie above 2sqrt(q); sixth is 0.
    assert y0==0
    h0=H[0].value(); f0=F[0].value(); q0=q.value(); e0=root_q.value()
    ds=[abs(cd(F,1,k)[0].value()-cd(H,1,k)[0].value()) for k in range(3)]
    ps=[abs(cd(F,1,k)[0].value())+ds[k] for k in range(3)]
    m=max(abs(f0)-ds[0],Q(0)); M=abs(f0)+ds[0]
    if m==M==0:
        av=kv=a1v=Q(0); asv=1/q0; as1v=Q(0)
    else:
        assert m>=2*e0,('chosen local maximum region',m,e0)
        av=m/(q0+m*m); kv=2*q0*m/(q0+m*m)**2
        a1v=4*q0*m/(q0+m*m)**3
        asv=q0*(m*m-q0)/(q0+m*m)**3
        as1v=4*q0*m*(m*m-2*q0)/(q0+m*m)**4
    astar=q0/(q0+m*m)**2 # pi*A_*
    erho=2*astar*ps[1]*ds[1]+a1v*ps[1]**2*ds[0]
    ej=astar*(ps[1]*ds[2]+ps[2]*ds[1])+a1v*ps[1]*ps[2]*ds[0]
    ew=kv*ds[0]; rhos=astar*ps[1]**2; js=astar*ps[1]*ps[2]
    pstar=max(abs(1-2*q0/(q0+m*m)),abs(1-2*q0/(q0+M*M)))
    rt0=abs(rt.value()); rx0=abs(rx.value())
    product=pstar*(rt0*erho+rx0*ej)+2*ew*(rt0*rhos+rx0*js)
    radial=asv*(2*rt0*ps[1]*ds[1]+rx0*(ps[1]*ds[2]+ps[2]*ds[1]))+as1v*(rt0*ps[1]**2+rx0*ps[1]*ps[2])*ds[0]
    def source_hat(G):
        DG=cabs2(G)+q; wg=q/DG; pg=cd(G,1); vg=cd(G,1,2)
        return (1-2*wg)*(rt*q*cabs2(pg)/DG**2+rx*q*creal(cmul(vg,conj(pg)))/DG**2)
    actual=abs((source_hat(H)-source).value())
    assert actual<=product,(name,point,'product envelope',actual,product)
    assert actual<=radial,(name,point,'radial envelope',actual,radial)
    return {'field_pair':name,'regulator':'q=(2+t+t²+x²)², globally >=49/16','point':list(map(str,point)),'q':str(q.value()),'H':list(map(str,(H[0].value(),H[1].value()))),'F':list(map(str,(F[0].value(),F[1].value()))),'E':list(map(str,(E[0].value(),E[1].value()))),'E_z':list(map(str,(Ez[0].value(),Ez[1].value()))),'source_transfer':{'pi_times_actual_difference':str(actual),'pi_times_safe_product_envelope':str(product),'pi_times_signed_radial_envelope':str(radial),'safe_product_holds':True,'signed_radial_holds':True,'d0_d1_d2':list(map(str,ds))},'checks':checks}

def main():
    started=time.perf_counter()
    cases=[]
    for field,point in [
        ('scaled_linear',(1,1,0)),
        ('scaled_linear',(Q(1,2),1,0)),
        ('quadratic_linear_residual',(1,2,0)),
        ('quadratic_linear_residual',(Q(1,2),2,0)),
        ('quadratic_quadratic_residual',(1,2,0)),
        ('quadratic_linear_residual',(0,0,0)),
    ]:
        cases.append(run_case(field,point))
    runtime=time.perf_counter()-started
    result={'status':'six handpicked exact-rational differential identity and two source-envelope controls passed; no continuous transfer or theta validation','prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra','case_count':len(cases),'checks_per_case':len(cases[0]['checks']),'total_execution_seconds':runtime,'environment':{'python':sys.version,'platform':platform.platform(),'arithmetic':'Python fractions.Fraction truncated multivariate Taylor jets, total order 4; exact rational comparisons'},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':cases}
    output=Path(__file__).with_name('SOURCE_CONTROLS.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','case_count','checks_per_case','total_execution_seconds','script_sha256']},indent=2))
if __name__=='__main__': main()
