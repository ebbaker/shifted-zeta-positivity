#!/usr/bin/env python3
"""Finite certified contour replay; analytic theorems remain in companion note.
Prepared for Edward Baker, 2026-10-15. Substantial LLM assistance.
Recorded model gpt-6-astra; reasoning effort ultra.
Requires python-flint 0.9.0; no remote data or repository mutation.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse, hashlib, json, platform
import flint
from flint import arb, acb, ctx

ctx.prec=192
Q=32
N=6
T=arb(1)/4
pi=arb.pi()
sigma=arb(2).atan()/4
checks=[]
def check(truth,label):
    if not truth: raise AssertionError(label)
    checks.append(label)

def source(y,analytic=False):
    l=y.log(analytic=analytic)
    d1=acb(0);d2=acb(0)
    for n in range(1,N+1):
        a=pi*n*n
        v=(-a*y).exp()
        d1-=2*a*v;d2+=2*a*a*v
    A=(l/4).exp()*(y*y*d2+arb(3)/2*y*d1)
    return l,A

def integrand(x,j):
    def f(y,analytic):
        l,A=source(y,analytic)
        u=l/4
        # cos(xu+j*pi/2) expressed without pi/2 argument drift.
        trig=(x*u).cos() if j%2==0 else (x*u).sin()
        if j%4 in (1,2): trig=-trig
        return (T*l*l/16).exp()*A*u**j*trig/(4*y)
    return f

def integ(x,j,a,b):
    return acb.integral(integrand(arb(x),j),acb(a),acb(b),
        abs_tol=arb(2)**-160,rel_tol=arb(2)**-160,
        deg_limit=120,eval_limit=500000,depth_limit=30)

def tail_bound(x,j):
    # On q>=Q, 0<=|Im y|<=2: |G_j(y)|<=41 exp(x/(2Q)) q^(j+2)e^(-3q).
    m=j+2
    poly=sum(arb(factorial(m))/factorial(m-k)*arb(Q)**(m-k)/arb(3)**(k+1) for k in range(m+1))
    return 41*(arb(abs(x))/(2*Q)).exp()*(-arb(3)*Q).exp()*poly

def series_bound(x,j,length):
    # q in [1,Q], |Im y|<=2; tail n>N, ratio<1/3, Log branch Re y>0.
    r=N+1
    return length*(2448*r**4+27*r*r)*(arb(3)/2)**j*(sigma*abs(x)-pi*r*r).exp()

def inflate(z,err):
    return z+acb(arb(0,err),arb(0,err))

def lag(h,j): return h[j+1]**2-h[j]*h[j+2]
def lagmix(a,b,j): return a[j+1]*b[j+1]-(a[j]*b[j+2]+b[j]*a[j+2])/2

def chord(a,b,j): return a[j]*(b[j]-b[j+1])

# Exact formal checks of all ordered sectors, stationarity kept only after summing.
# Polynomials in abstract jet symbols use rational coefficients.
def mono(name): return {(name,):F(1)}
def padd(*ps):
    d={}
    for p in ps:
        for k,v in p.items(): d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def pscale(p,c): return {k:c*v for k,v in p.items() if c*v}
def pmul(a,b):
    d={}
    for k,v in a.items():
        for l,w in b.items():
            m=tuple(sorted(k+l));d[m]=d.get(m,F(0))+v*w
    return {k:v for k,v in d.items() if v}
def plag(h,j):return padd(pmul(h[j+1],h[j+1]),pscale(pmul(h[j],h[j+2]),-1))
for j in (0,1):
    va=[mono(f'v{k}') for k in range(4)];ba=[mono(f'b{k}') for k in range(4)]
    h=[padd(a,b) for a,b in zip(va,ba)]
    cross=padd(pscale(pmul(va[j+1],ba[j+1]),2),pscale(pmul(va[j],ba[j+2]),-1),pscale(pmul(ba[j],va[j+2]),-1))
    check(plag(h,j)==padd(plag(va,j),cross,plag(ba,j)),f'exact Laguerre four-sector expansion j={j}')
    vx=[mono(f'vx{k}') for k in range(3)];bx=[mono(f'bx{k}') for k in range(3)]
    vy=[mono(f'vy{k}') for k in range(3)];by=[mono(f'by{k}') for k in range(3)]
    hx=padd(vx[j],bx[j]);hy=padd(vy[j],by[j],pscale(vy[j+1],-1),pscale(by[j+1],-1))
    parts=[]
    for a in (vx,bx):
        for b in (vy,by):parts.append(pmul(a[j],padd(b[j],pscale(b[j+1],-1))))
    check(pmul(hx,hy)==padd(*parts),f'exact ordered chord four-sector expansion j={j}')

# Endpoint asymptotic algebra: d/dx[e^(kap*x) S(1/x)] corresponds
# to kap*S-z^2*dS/dz. Unknown coefficients must cancel at the stated order.
def dendpoint(p):
    out=pmul(mono('kap'),p)
    for key,value in p.items():
        n=key.count('z')
        if n:
            k=list(key);k.remove('z');k.extend(('z','z'))
            out=padd(out,{tuple(sorted(k)):-n*value})
    return out
def zcoef(p,n):
    return {tuple(k for k in key if k!='z'):v for key,v in p.items() if key.count('z')==n}
S={('z',):F(1)}
for n,name in ((2,'aa'),(3,'bb'),(4,'cc'),(5,'dd')):
    S=padd(S,{tuple(sorted((name,)+('z',)*n)):F(1)})
hh=[S]
for j in range(3):hh.append(dendpoint(hh[-1]))
for j in (0,1):
    L=plag(hh,j)
    check(zcoef(L,2)=={},f'endpoint Laguerre rank-one cancellation order2 j={j}')
    check(zcoef(L,3)=={},f'endpoint Laguerre rank-one cancellation order3 j={j}')
    check(zcoef(L,4)=={('kap',)*(2*j):F(-1)},f'endpoint Laguerre surviving order4 j={j}')
    C=pmul(hh[j],padd(hh[j],pscale(hh[j+1],-1)))
    check(zcoef(C,2)=={('kap',)*(2*j):F(1),('kap',)*(2*j+1):F(-1)},f'actual pi-four chord leading coefficient j={j}')

# Missing elliptic multiplier coefficient: a_(n+1)-a_n.
for n in range(-5,6):
    check((n+1)**2-1==n*n+2*n,f'elliptic multiplier exponent shift n={n}')

# Tail-bound elementary gates used analytically.
check(16*(-3*pi).exp()<arb(1)/3,'theta derivative tail ratio below one third')
check((arb(3)*Q).log()<5,'log(3Q)<5')
check(25<Q,'log-square initial bound at Q')
check(2*(arb(3)*Q).log()/Q<1,'log-square derivative bound at Q')
check(pi-arb(1)/32>3,'cusp exponential bound')
check(arb(Q+2).log()<4,'finite contour logarithm bound')
check(arb(Q+2)<81,'finite contour fourth-root bound')
check((arb(1)/2).exp()<2,'finite contour heat bound')

rows=[]
for x in (20,40,80,120):
    real=[];vertical=[];bottom=[];right=[]
    for j in range(4):
        o=integ(x,j,1,Q)
        v=integ(x,j,acb(1,-2),acb(Q,-2))
        b=integ(x,j,1,acb(1,-2))
        r=integ(x,j,acb(Q,-2),Q)
        check((o-v-b-r).contains(0),f'finite rectangle x={x},j={j}')
        real.append(inflate(o,tail_bound(x,j)+series_bound(x,j,Q-1)))
        vertical.append(inflate(v,tail_bound(x,j)+series_bound(x,j,Q-1)))
        bottom.append(inflate(b,series_bound(x,j,2)))
        right.append(r)
        check((real[-1]-vertical[-1]-bottom[-1]).contains(0),f'infinite full-theta contour enclosure x={x},j={j}')
    for j in (0,1):
        parts=lag(vertical,j)+2*lagmix(vertical,bottom,j)+lag(bottom,j)
        check((lag(real,j)-parts).contains(0),f'full Laguerre packet enclosure x={x},j={j}')
    ystar=acb(1,-2);lstar,Astar=source(ystar);u=lstar/4;kappa=acb(0,1)*u
    # Include the omitted full-theta endpoint modes before forming asymptotic ratios.
    rr=N+1;az=abs(ystar)
    endpoint_tail=(az.log()/4).exp()*(az*az*3*pi*pi*rr**4+arb(3)/2*az*3*pi*rr**2)*(-pi*rr*rr).exp()
    Astar=inflate(Astar,endpoint_tail)
    C=-(T*lstar*lstar/16).exp()*Astar/(2*acb(0,1))
    lead=C*(kappa*x).exp()/x
    laglead=-C*C*(2*kappa*x).exp()/x**4
    rows.append({'x':x,'H0_enclosure':str(real[0]),'H1_enclosure':str(real[1]),
        'shifted_H0_abs':str(abs(vertical[0])),'bottom_H0_abs':str(abs(bottom[0])),
        'shifted_amplitude_to_endpoint_leading':str(vertical[0]/lead),
        'shifted_L0_abs':str(abs(lag(vertical,0))),
        'shifted_L0_to_endpoint_leading':str(lag(vertical,0)/laglead),
        'physical_L0_enclosure':str(lag(real,0)),
        'real_ray_tail_bound_j0':str(tail_bound(x,0)),
        'series_tail_bound_ray_j0':str(series_bound(x,0,Q-1))})
    print('completed x='+str(x),flush=True)

# One actual two-point pi/4 chord replay, all four directed pieces retained.
x=32;ell=arb(1)/10;y=arb(x)+ell
jets={}
for label,xx in (('x',arb(x)),('y',y)):
    jets[label]={}
    for part,aa,bb,length in (('O',1,Q,Q-1),('V',acb(1,-2),acb(Q,-2),Q-1),('B',1,acb(1,-2),2)):
        vals=[]
        for j in range(3):
            val=integ(xx,j,aa,bb)
            err=series_bound(xx,j,length)+(tail_bound(xx,j) if part!='B' else 0)
            vals.append(inflate(val,err))
        jets[label][part]=vals
for j in (0,1):
    full=chord(jets['x']['O'],jets['y']['O'],j)
    packet=sum(chord(jets['x'][a],jets['y'][b],j) for a in ('V','B') for b in ('V','B'))
    check((full-packet).contains(0),f'full pi/4 chord ordered packet j={j}')

ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
rec={'schema_version':1,'record_type':'theta22_period_two_contour','status':'PASS','date':'2026-10-15','prepared_for':'Edward Baker','assistance':'Substantial LLM assistance',
'model':'gpt-6-astra','reasoning_effort':'ultra','arithmetic':'python-flint Arb/Acb at 192 bits; exact fractions for formal products',
'python_version':platform.python_version(),'python_flint_version':flint.__version__,
'precision_bits':ctx.prec,'theta_modes':N,'ray_cutoff':Q,'t':'1/4','phase_growth_sigma':str(sigma),
'exact_or_enclosure_assertions':len(checks),'checks':checks,'rows':rows,
'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
'scope':'Finite contour and bilocal identity enclosures with explicit full-theta lattice and ray tails; endpoint-asymptotic illustration.',
'not_established':['Theta chord positivity','Uniform source-prescribed gap','Collision exclusion','Asymptotic theorem from finite samples']}
s=json.dumps(rec,indent=2)+'\n'
if args.output:args.output.write_text(s)
print(s)
