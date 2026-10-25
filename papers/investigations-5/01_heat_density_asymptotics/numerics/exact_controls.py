#!/usr/bin/env python3
"""HDA-17-AN01 r1: 12 exact-rational local identity controls.

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

def run_case(name,kind,point):
    t0,x0,y0=map(Q,point)
    t=J({ZERO:t0,(1,0,0):1})
    x=J({ZERO:x0,(0,1,0):1})
    y=J({ZERO:y0,(0,0,1):1})
    if name=='z': F=(x,y)
    elif name=='z-a(t)': F=(x-t-t*t/3,y)
    elif name=='z^2-2t': F=(x*x-y*y-2*t,2*x*y)
    else: raise ValueError(name)
    q=J(2) if kind=='constant' else 2+t+t*t+x*x
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
        assert v==0,(name,kind,point,label,str(v))
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
    return {'field':name,'regulator':kind,'point':list(map(str,point)),'q':str(q.value()),'F':list(map(str,(F[0].value(),F[1].value()))),'E':list(map(str,(E[0].value(),E[1].value()))),'checks':checks}

def main():
    started=time.perf_counter()
    cases=[]
    for field in ['z','z-a(t)','z^2-2t']:
        for regulator in ['constant','spatial_time_positive']:
            for point in [(0,0,0),(1,Q(1,3),Q(1,2))]:
                cases.append(run_case(field,regulator,point))
    runtime=time.perf_counter()-started
    result={'status':'12 handpicked exact-rational differential identity controls passed; no continuous transfer or theta validation','prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra','case_count':len(cases),'checks_per_case':len(cases[0]['checks']),'total_execution_seconds':runtime,'environment':{'python':sys.version,'platform':platform.platform(),'arithmetic':'Python fractions.Fraction truncated multivariate Taylor jets, total order 4; exact rational comparisons'},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':cases}
    output=Path(__file__).with_name('EXACT_CONTROLS_20261024.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','case_count','checks_per_case','total_execution_seconds','script_sha256']},indent=2))
if __name__=='__main__': main()
