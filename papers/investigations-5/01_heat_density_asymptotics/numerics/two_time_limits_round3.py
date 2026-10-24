#!/usr/bin/env python3
"""Floating diagnostics for Notes 11--12, not interval certificates.

2026-10-24. Prepared for Edward Baker with substantial LLM assistance.
gpt-6-astra (Codex), actual effort max. No theta roots are fitted.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

PI = math.pi
C = 315/256
CB = 1/(1-16*math.exp(-3*PI))
EPS = 1e-4


def gauss_panels(a, b, step, order):
    n = max(1, math.ceil((b-a)/step))
    edges = np.linspace(a,b,n+1)
    q,w = leggauss(order)
    nodes = ((edges[:-1,None]+edges[1:,None])/2
             +np.diff(edges)[:,None]*q/2).ravel()
    weights = (np.diff(edges)[:,None]*w/2).ravel()
    return nodes,weights


def phi(u, ntheta=8):
    u = np.asarray(u)
    return sum((2*PI**2*n**4*np.exp(9*u)-3*PI*n*n*np.exp(5*u))
               *np.exp(-PI*n*n*np.exp(4*u)) for n in range(1,ntheta+1))


def b2_majorant(N=4):
    def term(n):
        a=PI*n*n
        return PI**(-.25)/math.sqrt(n)*sum(
            coef*max(a,p)**p*math.exp(-max(a,p))
            for coef,p in [(75,1.25),(330,2.25),(224,3.25),(32,4.25)])
    ratio=(1+1/(N+1))**8*math.exp(-PI*(2*N+3))
    return dict(N=N,partial=sum(term(n) for n in range(1,N+1)),
                tail_allowance=term(N+1)/(1-ratio),ratio=ratio)


def J(A, maxp=3):
    vals=[math.sqrt(PI)/2*math.exp(A*A/4)*math.erfc(-A/2)]
    vals.append((1+A*vals[0])/2)
    for m in range(1,maxp):
        vals.append((m*vals[m-1]+A*vals[m])/2)
    return vals


def rho(h,p,eps=EPS):
    return eps**2*abs(p)**2/(PI*(abs(h)**2+eps**2)**2)


def negative_observations(T, order, phi0):
    v,w=gauss_panels(0,12,.25,order)
    u=v/math.sqrt(T)
    weights=w/math.sqrt(T)*np.exp(-v*v)*phi(u)
    grid=[(xi,eta) for eta in [0.,.5,1.] for xi in np.linspace(0,12,49)]
    z=math.sqrt(T)*np.array([x+1j*y for x,y in grid])
    phase=z[:,None]*u
    H=np.cos(phase)@weights
    Hp=-np.sin(phase)@(weights*u)
    G=phi0*math.sqrt(PI)/(2*math.sqrt(T))*np.exp(-z*z/(4*T))
    Gp=-z/(2*T)*G
    actual=rho(H,Hp)
    model=rho(G,Gp)
    profile=phi0**2/(16*EPS**2)*np.array([
        (x*x+y*y)*math.exp(-(x*x-y*y)/2) for x,y in grid])
    return dict(max_density_gaussian_error=float(max(abs(actual-model))),
                max_scaled_profile_error=float(max(abs(T*T*actual-profile))),
                data=np.column_stack((actual,model)).tolist())


def negative_rows(phi0,B2):
    A=1.
    jj=J(A)
    rows=[]
    for T in [1e6,1e8,1e10]:
        d0=B2*jj[2]/(2*T**1.5)
        d1=B2*jj[3]/(2*T**2)
        Q=phi0*jj[0]/math.sqrt(T)+d0
        P=phi0*jj[1]/T+d1
        bound=2*P*d1/(PI*EPS**2)+4*Q*P*P*d0/(PI*EPS**4)
        B=PI*phi0**2/(4*EPS**2)
        MA=phi0**2*math.exp(A*A/2)/(16*EPS**2)*2*math.exp(-1+A*A/2)
        profile_bound=T*T*bound+2*B*math.exp(A*A/2)*MA/T
        coarse=negative_observations(T,24,phi0)
        fine=negative_observations(T,40,phi0)
        change=float(np.max(abs(np.array(coarse.pop('data'))-
                                np.array(fine.pop('data')))))
        rows.append(dict(T=T,scaled_y_max=A,grid_xi=[0,12,49],
            grid_upsilon=[0,.5,1],density_error_allowance=bound,
            scaled_profile_allowance=profile_bound,quadrature_change=change,
            observed=fine,passed_observed_bound=fine['max_density_gaussian_error']<=bound))
    return rows


def saddle(t):
    f=lambda u:4*PI*math.exp(4*u)-2*t*u-9
    hi=max(2.,math.log(t+10))
    while f(hi)<=0:
        hi*=1.5
    # q' has its maximum at this u; choose its larger zero.
    lo=math.log(t/(8*PI))/4
    if f(lo)>=0:
        raise ValueError('No large saddle in this diagnostic range')
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    L=(lo+hi)/2
    return L,8*t*L-2*t+36


def gauss_tail(p,c,lam,h):
    vals=[math.sqrt(PI)/(2*math.sqrt(c))*math.exp(lam*lam/(4*c))
          *math.erfc(math.sqrt(c)*h-lam/(2*math.sqrt(c)))]
    boundary=math.exp(-c*h*h+lam*h)
    if p:
        vals.append((boundary+lam*vals[0])/(2*c))
    for m in range(1,p):
        vals.append((h**m*boundary+m*vals[m-1]+lam*vals[m])/(2*c))
    return vals[p]


def allowances(t,Y):
    L,kap=saddle(t)
    c=1/(4*math.e); d=.25; h=kap**(1/12)
    q=lambda u:t*u*u+9*u-PI*math.exp(4*u)
    gates=(L>=d and kap>=32 and t/kap<=c and q(L-d)>=q(0))
    QL=16*math.exp(-3*PI*math.exp(4*(L-d)))
    dL=3/(2*PI)*math.exp(-4*(L-d))+QL/(1-QL)
    eta=4*math.e/3*kap**(-.25)
    ec=math.expm1(eta)+math.exp(eta)*dL
    def G(p,y):return 2*gauss_tail(p,.5,y/math.sqrt(kap),0)
    def D(p,y):
        tail=2*(CB*gauss_tail(p,c,y/math.sqrt(kap),h)
                +gauss_tail(p,.5,y/math.sqrt(kap),h))
        logleft=math.log(CB)+(p+1)*math.log(L*math.sqrt(kap))+y*L-c*kap*d*d
        return ec*G(p,y)+tail+math.exp(logleft)
    zm=math.sqrt(2*PI)-D(0,0)
    out=dict(t=t,L=L,kappa=kap,source_gates=bool(gates),Z_lower=zm,D0=D(0,0))
    if not gates or zm<=0:return out
    emu=kap**(-.5)*D(1,0)/zm
    def A(p,y):return kap**(-p/2)*(G(p,y)+D(p,y))/zm
    B3=4*math.exp(Y*emu)*(A(3,Y)+emu**3*A(0,Y))
    # Use X<=kappa^(1/3); this conservative box bounds the actual snapped box.
    X=kap**(1/3)
    z2=X*X+Y*Y
    amin=1-A(2,0)*z2/2
    delta=z2**1.5*B3/(6*amin) if amin>0 else None
    mup=L+emu; mum=L-emu
    out.update(mean_error=emu,var_upper=A(2,0),B3_upper=B3,
               X_upper=X,a_min=amin,delta_upper=delta,
               mu_lower=mum,mu_upper=mup)
    if delta is None or not 0<delta<=.125 or mum<=0:return out
    rad=4*delta/mum
    passed=rad<min(Y,PI/(2*mup))
    e=4*delta/PI
    m=2*math.floor(mup*X/PI)
    harmonic=sum(1/d for d in range(1,m)) if m<100000 else 1+math.log(m-1)
    # For large populations use the elementary harmonic upper bound.
    vand=m*(m-1)*emu/mum+4*e/(1-2*e)*(m*harmonic-(m-1))
    ell=10.; hy=.75
    npop=2*mup*(ell+rad)/PI+2
    der=8*C/math.sqrt(7)*(6/7)**3/ell**2
    mass=emu/PI+npop*rad*der+(PI/mum)**3*fourth_norm()/(720*ell**4)
    out.update(carrier_gates=bool(passed),radius_upper=rad,
               population_upper=m,log_vandermonde_error_allowance=vand,
               density_bound_without_regulator_at_y0=mass*C/hy)
    return out


def fourth_norm():
    points=[0,math.sqrt((15-2*math.sqrt(30))/35),
            math.sqrt((15+2*math.sqrt(30))/35),1]
    primitive=lambda x:C*(144*x-480*x**3+336*x**5)
    return 2*sum(abs(primitive(b)-primitive(a)) for a,b in zip(points[:-1],points[1:]))


def expm1_remainder(x):
    # exp(x)-1-x, evaluated without central cancellation.
    x=np.asarray(x)
    out=np.expm1(x)-x
    small=abs(x)<.01
    q=x[small]
    out[small]=sum(q**k/math.factorial(k) for k in range(2,13))
    return out


def positive_source(t,order,cut):
    L,kap=saddle(t)
    w,weights=gauss_panels(-cut,cut,.5,order)
    v=w/math.sqrt(kap); u=L+v
    aa=PI*math.exp(4*L)
    qdiff=t*v*v-aa*expm1_remainder(4*v)
    b=1-3*np.exp(-4*u)/(2*PI)
    for n in range(2,9):
        b+=(n**4-3*n*n*np.exp(-4*u)/(2*PI))*np.exp(-PI*(n*n-1)*np.exp(4*u))
    raw=weights*np.exp(qdiff)*b
    p=raw/raw.sum()
    logM=math.log(2*PI**2)+t*L*L+9*L-aa-.5*math.log(kap)+math.log(raw.sum())
    return L,kap,u,v,p,logM


def positive_moments(t,order,cut):
    L,kap,u,v,p,logM=positive_source(t,order,cut)
    mean_v=float(p@v)
    mu=L+mean_v
    center=v-mean_v
    var=float(p@(center*center))
    B3=float(p@(abs(center)**3*np.exp(1.25*abs(center))))
    N=math.floor(mu*kap**(1/3)/PI); X=N*PI/mu
    z2=X*X+1.25**2
    amin=1-var*z2/2
    delta=z2**1.5*B3/(6*amin)
    rad=4*delta/mu
    return dict(L=L,kappa=kap,mu=mu,mu_minus_L=mean_v,var=var,B3=B3,
        N=N,X=X,a_min=amin,delta=delta,radius=rad,
        carrier_gates=bool(0<delta<=.125 and rad<min(1.25,PI/(2*mu))),
        logM=logM)


def contour_comparisons():
    rows=[]
    ell=10.; hy=.75
    for t in [1e4,1e6]:
        L,kap,u,v,p,logM=positive_source(t,40,14)
        mu=L+float(p@v)
        X=math.floor(mu*kap**(1/3)/PI)*PI/mu
        for center in [0.,.8*(X-ell)]:
            values=[]
            for order in [160,224]:
                q,w=leggauss(order)
                corners=[center-ell-1j*hy,center+ell-1j*hy,
                         center+ell+1j*hy,center-ell+1j*hy]
                integral=0j
                for a,b in zip(corners,corners[1:]+corners[:1]):
                    z=(a+b)/2+(b-a)*q/2; dz=(b-a)*w/2
                    phase=z[:,None]*u
                    H=np.cos(phase)@p
                    Hp=-np.sin(phase)@(p*u)
                    poly=C/ell*(1-((z-center)/ell)**2)**4
                    integral+=np.sum(poly*Hp/H*dz)/(2j*PI)
                values.append(integral)
            rows.append(dict(t=t,x=center,X=X,ell=ell,h=hy,
                measured_zero_intensity=float(values[-1].real),model_intensity=L/PI,
                absolute_intensity_error=abs(float(values[-1].real)-L/PI),
                contour_change=abs(values[-1]-values[-2]),
                imaginary_residue=abs(values[-1].imag),
                target='weak zero measure; finite-epsilon comparison is analytic, not measured'))
    return rows


def determinant_controls():
    rows=[]
    for m in [8,32,128]:
        e=.03
        displacement=e*np.sin(np.arange(m)*1.713)
        y=np.arange(m)+displacement
        diff=y[:,None]-y[None,:]
        i,j=np.triu_indices(m,1)
        logratio=2*float(np.log(abs(diff[i,j])/(j-i)).sum())
        bound=4*e/(1-2*e)*(m*sum(1/k for k in range(1,m))-(m-1))
        def lap(pts):
            dd=pts[:,None]-pts[None,:]
            np.fill_diagonal(dd,np.inf)
            ww=1/dd**2
            return np.diag(ww.sum(axis=1))-ww
        clock=lap(np.arange(m,dtype=float)); pert=lap(y)
        low=float(np.linalg.eigvalsh(pert-clock/(1+2*e)**2)[0])
        high=float(np.linalg.eigvalsh(clock/(1-2*e)**2-pert)[0])
        rows.append(dict(m=m,e=e,log_ratio=logratio,log_bound=bound,
            lower_matrix_min_eigenvalue=low,upper_matrix_min_eigenvalue=high,
            passed=bool(abs(logratio)<=bound and min(low,high)>-1e-12)))
    return rows


def degree_budget(t,Y=1.25,p=1):
    def logB(s,j):
        u=1+math.log(s+Y+10)
        main=(j+1)*math.log(u)-math.log(j+1)+s*u*u+(9+Y)*u
        tail=math.log(math.gamma((j+1)/2)/2)
        return math.log(2*PI**2*CB)+float(np.logaddexp(main,tail))
    c0=125/(54*math.sqrt(5))
    a=math.log(2/PI)+logB(t,1)+logB(2*t,1)-2*math.log(EPS)
    b=math.log(c0/PI)+2*logB(t,1)+logB(2*t,0)-3*math.log(EPS)
    logA=float(np.logaddexp(a,b))
    N=max(0,math.ceil((logA+p*math.log1p(t))/math.log(2))-1)
    return dict(t=t,Y=Y,p=p,N=N,log_absolute_allowance=logA-(N+1)*math.log(2),
                target=(1+t)**(-p),xi_derivatives_evaluated=False)


def cosine_series_control():
    t=.7; omega=1.3; Y=.5; N=4; eps=.5
    a=t*omega**2
    pn=sum(a**k/math.factorial(k) for k in range(N+1))
    c0=125/(54*math.sqrt(5))
    m1=omega*math.exp(a+Y*omega)
    e0=2**(-N-1)*math.exp(2*a+Y*omega)
    e1=omega*e0
    bound=2*m1*e1/(PI*eps**2)+c0*m1*m1*e0/(PI*eps**3)
    z=np.linspace(0,20,1001)+.2j
    cos=np.cos(omega*z); sin=np.sin(omega*z)
    err=float(max(abs(rho(math.exp(a)*cos,-omega*math.exp(a)*sin,eps)
                      -rho(pn*cos,-omega*pn*sin,eps))))
    return dict(t=t,omega=omega,N=N,epsilon=eps,density_error=err,allowance=bound,
                passed=err<=bound,scope='atomic model; canonical B_j not used')


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',required=True)
    args=parser.parse_args()
    phi0=float(phi(np.array(0.)))
    b2=b2_majorant(); B2=b2['partial']+b2['tail_allowance']
    positive=[]
    for t in [1024.,1e4,1e6,1e9,1e12]:
        a=positive_moments(t,24,12)
        b=positive_moments(t,40,14)
        change={k:abs(a[k]-b[k]) for k in ['mu_minus_L','var','B3','delta']}
        positive.append(dict(t=t,observed=b,refinement_change=change,
                             explicit_allowances=allowances(t,1.25)))
    record=dict(date='2026-10-24',prepared_for='Edward Baker',
        assistance='Substantial LLM assistance',model='gpt-6-astra',effort='max',
        status='FLOATING DIAGNOSTICS; NOT INTERVAL CERTIFICATES',
        python=platform.python_version(),numpy=np.__version__,epsilon=EPS,
        phi0=phi0,B2=b2,negative=negative_rows(phi0,B2),positive=positive,
        contour_comparisons=contour_comparisons(),
        determinant_controls=determinant_controls(),
        global_degree_budgets=[degree_budget(t) for t in [1,100,1024]],
        cosine_series_control=cosine_series_control(),
        limitations=['No outward rounding or quadrature/source-tail certificate.',
          'Negative grid checks do not prove all-height uniformity; the written proof does.',
          'Positive saddle quadrature omits tails beyond the recorded w cutoff.',
          'No theta roots fitted; determinant numerics are algebraic perturbed-lattice controls.',
          'Very-large-population harmonic numbers use the upper bound 1+log(m-1), evaluated in floating arithmetic.',
          'Global xi-derivative hierarchy not numerically evaluated.',
          'No current/covariance derivative or evolved-solution accuracy measured.'])
    record['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(args.output).write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:record[k] for k in ['phi0','B2','global_degree_budgets']},indent=2))
    print('Negative observed/bound:',[(r['T'],r['observed']['max_density_gaussian_error'],r['density_error_allowance']) for r in record['negative']])
    print('Positive delta / explicit gate:',[(r['t'],r['observed']['delta'],r['explicit_allowances'].get('carrier_gates',False)) for r in positive])


if __name__=='__main__':main()
