#!/usr/bin/env python3
"""HDA-15 bounded diagnostic; no uniform/interval acceptance certificate.

Prepared for Edward Baker, 24 October 2026, gpt-6-astra, actual effort max.
Requires NumPy and mpmath. All mathematical inequalities are in Note 23.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from numpy.polynomial import polynomial as pol
from numpy.polynomial.legendre import leggauss
import mpmath as mp

mp.mp.dps = 80
PI = math.pi
US = 1.5
N = 4
Y = 1.0
LX, LY = 2.0, .5
ETA = .5
MESHS = [48, 96, 192]
TIMES = [-16., 0., 32., 64.]
POINTS = [(0., 0.), (4., .5), (8., 0.)]
PPOW = np.array([1.25, 2.25, 3.25, 4.25])
COEF = np.array([75., 330., 224., 32.])
KPOLY = np.array([1., 0., -4., 0., 6., 0., -4., 0., 1.])*315/256


def phi(u, modes=N):
    u = np.asarray(u)
    a = PI*np.arange(1, modes+1).reshape((-1,)+(1,)*u.ndim)**2*np.exp(4*u)
    # Each original positive summand = leading*(1-3/(2a)).
    terms = 2*PI**(-.25)*np.arange(1,modes+1).reshape((-1,)+(1,)*u.ndim)**(-.5)*np.exp(2.25*np.log(a)-a)*(1-1.5/a)
    return terms.sum(axis=0)


def phi_mp(u, modes=N):
    u=mp.mpf(float(u))
    return mp.fsum((2*mp.pi**2*n**4*mp.exp(9*u)-3*mp.pi*n**2*mp.exp(5*u))*mp.exp(-mp.pi*n*n*mp.exp(4*u)) for n in range(1,modes+1))


C = float(phi(0.,8))*math.sqrt(PI)/2
C_MP = phi_mp(0.,16)*mp.sqrt(mp.pi)/2


def bcell(a, b, nb=8):
    ans=np.zeros_like(a)
    for n in range(1,nb+1):
        lo=PI*n*n*np.exp(4*a);hi=PI*n*n*np.exp(4*b)
        v=np.minimum(np.maximum(PPOW[:,None],lo),hi)
        ans += PI**(-.25)*n**(-.5)*(COEF[:,None]*np.exp(PPOW[:,None]*np.log(v)-v)).sum(axis=0)
    n=nb+1;lo=PI*n*n*np.exp(4*a)
    remainder=PI**(-.25)*n**(-.5)*(COEF[:,None]*np.exp(PPOW[:,None]*np.log(lo)-lo)).sum(axis=0)
    ratio=(1+1/n)**8*np.exp(-PI*(2*nb+3)*np.exp(4*a))
    return ans+remainder/(1-ratio)


def nodal_tail(u):
    a=PI*(N+1)**2*np.exp(4*u)
    r=(1+1/(N+1))**4*np.exp(-PI*(2*N+3)*np.exp(4*u))
    return np.exp(math.log(2*PI**2*(N+1)**4)+9*u-a)/(1-r)


def weight_max(t,j,a,b):
    def w(u): return u**j*np.exp(t*u*u+Y*u)
    ans=np.maximum(w(a),w(b))
    if t<0:
        root=(-Y-math.sqrt(Y*Y-8*t*j))/(4*t)
        inside=(a<=root)&(root<=b)
        ans=np.maximum(ans, np.where(inside,w(root),0))
    return ans


def tail(j,t):
    s=max(t,0);u=mp.mpf(US)
    lam=4*mp.pi*mp.exp(4*u)-2*s*u-9-Y-j/u
    assert lam>0 and 16*mp.pi*mp.exp(4*u)>=2*s
    cb=1/(1-16*mp.exp(-3*mp.pi))
    val=2*mp.pi**2*cb*u**j*mp.exp(s*u*u+(9+Y)*u-mp.pi*mp.exp(4*u))/lam
    return val


def budget(m,t):
    u=np.linspace(0,US,m+1);a=u[:-1];b=u[1:];h=US/m
    bc=bcell(a,b);tau=nodal_tail(u);f=phi(u)
    # Candidate arithmetic majorant, tested at nodes but NOT certified.
    sigma=1e-12*f+1e-300
    rows=[]
    b2=float(bcell(np.array([0.]),np.array([US]))[0])
    for j in range(4):
        vmax=weight_max(t,j,a,b)
        interp=float(sum(bc*h**3*vmax/12))
        mode=float(sum((tau[:-1]+tau[1:])*h*vmax/2))
        arithmetic=float(sum((sigma[:-1]+sigma[1:])*h*vmax/2))
        tj=tail(j,t)
        # Conservative representable floor for diagnostic arithmetic only.
        total=interp+mode+arithmetic+max(float(tj),1e-300)
        # Use the original FB8 F_j integral, not its coarser elementary upper bound.
        sj=max(t,0.)
        fj=mp.quad(lambda v:v**j*mp.exp(sj*v*v+Y*v),[0,US/2,US])
        old=(mp.mpf(b2)*h*h/8+mp.mpf(nodal_tail(np.array([0.]))[0]))*fj+tj
        rows.append(dict(j=j,interpolation=interp,theta_modes=mode,
            nodal_arithmetic_candidate=arithmetic,tail=str(tj),tail_log10=float(mp.log10(tj)),
            total=total,FB8=float(old),FB8_over_cell=float(old/total)))
    return rows


def rule(m,order,kind='finite'):
    x,w=leggauss(order)
    if kind=='finite':
        nodes=np.linspace(0,US,m+1);h=US/m
        u=(nodes[:-1,None]+(x+1)*h/2).ravel()
        weights=np.tile(w*h/2,m)
        fn=phi(nodes)
        f=(fn[:-1,None]*(1-x)/2+fn[1:,None]*(1+x)/2).ravel()
    else:
        u=(x+1)*US/2;weights=w*US/2;f=phi(u,8)
    return u,weights*f


def jets(t,z,source):
    u,w=source
    e=np.exp(t*u*u)*w
    z=np.asarray(z).reshape(-1)
    ans=np.zeros((len(z),4),complex)
    for start in range(0,len(z),128):
        zz=z[start:start+128,None]*u
        co=np.cos(zz);si=np.sin(zz)
        ans[start:start+128]=np.stack([co@e,-si@(e*u),-co@(e*u*u),si@(e*u**3)],axis=1)
    return ans


def observables(t,h):
    q=(ETA*C)**2/math.sqrt(1+t*t);rt=-t/(1+t*t)
    g,p,v,a=h.T;D=abs(g)**2+q;w=q/D;AA=q/(PI*D**2)
    rho=AA*abs(p)**2;j=AA*v*np.conjugate(p)
    r_t=-2*AA*np.real(a*np.conjugate(p))+rt*(1-2*w)*rho+4*rho*np.real(v*np.conjugate(g)/D)
    S=np.log(D);sx=2*np.real(p*np.conjugate(g)/D);sy=-2*np.imag(p*np.conjugate(g)/D)
    st=-2*np.real(v*np.conjugate(g)/D)+rt*w
    return dict(R=rho,J=j,Rt=r_t,U=S,Ut=st,Ux=sx,Uy=sy,W=w,source=rt*(1-2*w)*rho)


def local_errors(t,g,ds,denominator=True):
    e=ETA*C/(1+t*t)**.25;q=e*e;rt=abs(t/(1+t*t))
    p=np.abs(g)+np.array(ds);m=np.maximum(abs(g[:,0])-ds[0],0);M=abs(g[:,0])+ds[0]
    def clamp(x):return np.minimum(np.maximum(x,m),M)
    if denominator:
        av=clamp(e/math.sqrt(5));bv=clamp(e);wv=clamp(e/math.sqrt(3))
        AA=q/(PI*(q+m*m)**2);A1=4*q*av/(PI*(q+av*av)**3)
        ast=bv/(q+bv*bv);bst=1/(q+m*m);w1=2*q*wv/(q+wv*wv)**2
    else:
        AA=np.full(len(g),1/(PI*q));A1=np.full(len(g),125/(54*math.sqrt(5)*PI*e**3))
        ast=np.full(len(g),1/(2*e));bst=np.full(len(g),1/q);w1=np.full(len(g),1/e)
    E=2*AA*p[:,1]*ds[1]+A1*p[:,1]**2*ds[0]
    Ej=AA*(p[:,1]*ds[2]+p[:,2]*ds[1])+A1*p[:,1]*p[:,2]*ds[0]
    E13=AA*(p[:,1]*ds[3]+p[:,3]*ds[1])+A1*p[:,1]*p[:,3]*ds[0]
    Ew=w1*ds[0];rh=AA*p[:,1]**2
    Es=rt*(E+2*rh*Ew)
    Et=2*E13+Es+4*(p[:,2]*ast*E+rh*(ast*ds[2]+p[:,2]*bst*ds[0]))
    G=2*p[:,1]*ast;d=2*ast*ds[1]+2*p[:,1]*bst*ds[0]
    return dict(R=E,J=Ej,Rt=Et,U=2*ast*ds[0],Ut=2*(ast*ds[2]+p[:,2]*bst*ds[0])+rt*Ew,
        Ux=d,Uy=d,W=Ew,source=Es,G=G,d=d)


def filter_rule(order):
    v,w=leggauss(order);xx,yy=np.meshgrid(v,v,indexing='ij');ww=np.outer(w,w).ravel()
    kv=pol.polyval(v,KPOLY);kd=pol.polyval(v,pol.polyder(KPOLY));kdd=pol.polyval(v,pol.polyder(KPOLY,2))
    weights=dict(K=ww*np.outer(kv,kv).ravel(),Kx=ww*np.outer(kd/LX,kv).ravel(),
        Ky=ww*np.outer(kv,kd/LY).ravel(),DK=ww*(np.outer(kdd/LX**2,kv)+np.outer(kv,kdd/LY**2)).ravel())
    return (LX*xx+1j*LY*yy).ravel(),weights


def filtered(obs,w):
    out={k:sum(w['K']*v) for k,v in obs.items()}
    q=0.;dq=0.
    for name,sign in [('Ux',1),('Uy',-1)]:
        v=obs[name];vbar=sum(w['K']*v)
        q+=sign*(sum(w['K']*v*v)-vbar*vbar)
        dq+=sign*(sum(w['DK']*v*v)-2*vbar*sum(w['DK']*v)-2*sum(w['Kx']*v)**2-2*sum(w['Ky']*v)**2)
    out.update(Q=q,DeltaQ=dq)
    return out


def filtered_errors(err,w):
    out={k:float(sum(w['K']*v)) for k,v in err.items() if k not in ['G','d']}
    G,d=err['G'],err['d'];conv=lambda name,v:sum(abs(w[name])*v)
    # Identical envelopes for x,y; factor 2 is the component sum.
    out['Q']=4*(conv('K',G*d)+conv('K',G)*conv('K',d))
    out['DeltaQ']=2*(2*conv('DK',G*d)+2*conv('K',d)*conv('DK',G)+2*conv('K',G)*conv('DK',d)
        +4*sum(conv(name,G)*conv(name,d) for name in ['Kx','Ky']))
    return out


def local_series_jets(t,z,m=192,degree=18):
    nodes=np.linspace(0,US,m+1);fn=phi(nodes);out=np.zeros(4,complex);bounds=np.zeros(4)
    for i in range(m):
        a,b=nodes[i:i+2];c=(a+b)/2;d=(b-a)/2
        f=np.array([(fn[i]+fn[i+1])/2,(fn[i+1]-fn[i])/(b-a)])
        theta=(2*abs(t)*c+abs(z))*d+abs(t)*d*d
        factor=(b-a)*max(fn[i],fn[i+1])*math.exp(t*c*c+abs(z.imag)*c+theta)*theta**(degree+1)/math.factorial(degree+1)
        bounds+=factor*b**np.arange(4)
        for sign in [-1,1]:
            P=np.array([0,2*t*c+sign*1j*z,t],complex)
            term=np.array([1+0j]);series=np.zeros(2*degree+1,complex);series[0]=1
            for n in range(1,degree+1):
                term=pol.polymul(term,P)/n;series[:len(term)]+=term
            base=pol.polymul(series,f)*np.exp(t*c*c+sign*1j*z*c)/2
            for j in range(4):
                co=pol.polymul(base,pol.polypow(np.array([c,1.]),j))*(sign*1j)**j
                out[j]+=sum(co[k]*2*d**(k+1)/(k+1) for k in range(0,len(co),2))
    return out,bounds


def primitive_mp(t,z,u):
    t=mp.mpf(t);z=mp.mpc(z);u=mp.mpf(u)
    if t==0:
        if z==0:return (u,u*u/2)
        az=1j*z
        return mp.expm1(az*u)/az,(mp.exp(az*u)*(az*u-1)+1)/(az*az)
    a=mp.sqrt(-t);v=-1j*z/(2*a)
    i0=mp.sqrt(mp.pi)/(2*a)*mp.exp(z*z/(4*t))*(mp.erf(a*u+v)-mp.erf(v))
    return i0,(mp.expm1(t*u*u+1j*z*u)-1j*z*i0)/(2*t)


def run():
    source_rows=[dict(cells=m,t=t,jets=budget(m,t)) for m in MESHS for t in TIMES]
    src=rule(192,8);srcrefine=rule(192,12);true=rule(0,256,'theta');truerefine=rule(0,384,'theta')
    pilots=[]
    for t in TIMES:
        ds=[r['total'] for r in budget(192,t)]
        for x,y in POINTS:
            values={};errs={}
            for order in [12,20]:
                offsets,w=filter_rule(order);z=x+1j*y-offsets
                gf=jets(t,z,src);gt=jets(t,z,true)
                fv=filtered(observables(t,gf),w);tv=filtered(observables(t,gt),w)
                values[order]=(fv,tv)
                if order==20:
                    errs['local']=filtered_errors(local_errors(t,gf,ds),w)
                    errs['FB10_same_local_P']=filtered_errors(local_errors(t,gf,ds,False),w)
                    refined_f=filtered(observables(t,jets(t,z,srcrefine)),w)
                    refined_t=filtered(observables(t,jets(t,z,truerefine)),w)
            fv,tv=values[20]
            errors={k:float(abs(fv[k]-tv[k])) for k in fv}
            assert all(errors[k]<=errs['local'][k]+2e-11 for k in fv),(t,x,y,errors,errs)
            pilots.append(dict(t=t,x=x,y=y,theta_values={k:([float(v.real),float(v.imag)] if k=='J' else float(v.real)) for k,v in tv.items()},
                observed_error=errors,local_allowance_quadrature=errs['local'],FB10_same_local_P=errs['FB10_same_local_P'],
                filter_12_to_20={k:float(max(abs(fv[k]-values[12][0][k]),abs(tv[k]-values[12][1][k]))) for k in fv},
                source_rule_refinement={k:float(max(abs(fv[k]-refined_f[k]),abs(tv[k]-refined_t[k]))) for k in fv}))
    node_rows=[]; initial_node_rows=[]
    u=np.linspace(0,US,193);fn=phi(u)
    for v,approx in zip(u,fn):
        exact=phi_mp(v);sigma=mp.mpf('1e-12')*exact+mp.mpf('1e-300')
        er=abs(mp.mpf(float(approx))-exact)
        node_rows.append(float(er/sigma))
        initial_node_rows.append(float(er/(mp.mpf('1e-14')*exact+mp.mpf('1e-300'))))
    worst_filter=[]
    for order in [20,40,64]:
        off,w=filter_rule(order);z=4+.5j-off
        worst_filter.append(dict(order=order,approx=filtered(observables(64.,jets(64.,z,src)),w),
            theta=filtered(observables(64.,jets(64.,z,true)),w)))
    worst_rows=[]
    for i,row in enumerate(worst_filter):
        worst_rows.append(dict(order=row['order'],observed_error={k:float(abs(row['approx'][k]-row['theta'][k])) for k in row['approx']},
            refinement_from_previous=None if i==0 else {k:float(max(abs(row['approx'][k]-worst_filter[i-1]['approx'][k]),
                abs(row['theta'][k]-worst_filter[i-1]['theta'][k]))) for k in row['approx']}))
    series=[]
    for t,z in [(-16.,10+1j),(0.,0j),(1e-8,10+1j),(-1e-8,10+1j),(32.,4+.5j),(64.,10+1j)]:
        actual,bounds=local_series_jets(t,z)
        ref=jets(t,[z],srcrefine)[0]
        series.append(dict(t=t,z=[z.real,z.imag],observed_jet_errors=[float(v) for v in abs(actual-ref)],truncation_bounds=[float(v) for v in bounds]))
    prim=[]
    for t,z,u in [(-16.,10+1j,1.5),(0.,0j,1.5),(0.,10+1j,1.5),(1e-8,10+1j,.25),(-1e-8,10+1j,.25),(64.,10+1j,1.5)]:
        q0=primitive_mp(t,z,u)
        refs=[mp.quad(lambda v:v**j*mp.exp(mp.mpf(t)*v*v+1j*mp.mpc(z)*v),[0,mp.mpf(u)/2,mp.mpf(u)]) for j in [0,1]]
        errs=[abs(q0[j]-refs[j])/max(mp.mpf(1),abs(refs[j])) for j in [0,1]]
        prim.append(dict(t=t,z=[z.real,z.imag],u=u,precision_digits=mp.mp.dps,
            normalized_error=[str(e) for e in errs],status='failed cancellation check' if max(errs)>mp.mpf('1e-30') else 'passed sampled check'))
    rng=np.random.default_rng(20261024);algebra_ratios=[]
    for i in range(128):
        t=TIMES[i%4]
        g=(rng.normal(size=4)+1j*rng.normal(size=4))*10**rng.uniform(-3,1)
        h=g+(rng.normal(size=4)+1j*rng.normal(size=4))*10**rng.uniform(-6,-1)
        if i==0:h=np.array([0.,0.,2.,0.],complex) # H=z^2-2t at its double event
        if i==1:g=np.array([0.,0.,2.,0.],complex)
        ds=abs(h-g)
        ee=local_errors(t,g[None,:],ds)
        oh=observables(t,h[None,:]);og=observables(t,g[None,:])
        for name in oh:
            actual=float(abs(oh[name][0]-og[name][0]));allowance=float(ee[name][0])
            assert actual<=allowance+1e-12,(i,name,actual,allowance)
            algebra_ratios.append(actual/allowance if allowance else 0.)
    return dict(date='2026-10-24',prepared_for='Edward Baker',model='gpt-6-astra',reasoning_effort='max',
        status='Floating diagnostic; symbolic bounds proved in Note 23; no interval or uniform HDA-17 certificate.',
        pointwise_algebra_checks=dict(cases=128,seed=20261024,max_error_over_allowance=max(algebra_ratios),includes_zero_and_double_event_jets=True),
        versions=dict(numpy=np.__version__,mpmath=mp.__version__),
        parameters=dict(time_slab=[-16,64],observation=[[-8,8],[-.5,.5]],buffer=[[-10,10],[-1,1]],
            eta=ETA,widths=[LX,LY],cutoff=US,theta_modes=N,derivative_modes=8,meshes=MESHS,
            times=TIMES,points=POINTS,filter_orders=[12,20],finite_source_orders=[8,12],theta_orders=[256,384],
            arithmetic_candidate='sigma_i=1e-12 Phi_N(u_i)+1e-300; initial 1e-14 multiplier failed; high-precision samples are not certification'),
        source_budgets=source_rows,pilots=pilots,nodal_max_error_over_candidate=max(node_rows),initial_nodal_1e_minus14_max_ratio=max(initial_node_rows),
        worst_case_filter_refinement=dict(t=64,x=4,y=.5,rows=worst_rows),
        regulator_C_float_error=str(abs(mp.mpf(C)-C_MP)),local_series_checks=series,raw_primitive_checks=prim,
        limitations=['Every reported decimal is floating unless explicitly an analytic formula.',
            'Filter refinement is empirical, not an integration error bound.',
            'The entire slab and gaps between points have not been enclosed.',
            'Nodal candidate, regulator rounding and polynomial/primitive arithmetic remain uncertified.',
            'The trial does not span the regulator switch or supply endpoint overlap.',
            'No claim that failed allowance is a lower bound on actual error.'])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True,type=Path);args=ap.parse_args()
    record=run();record['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    rows=record['pilots'];keys=rows[0]['observed_error'].keys()
    print(json.dumps(dict(cases=len(rows),max_observed={k:max(r['observed_error'][k] for r in rows) for k in keys},
        max_local_allowance={k:max(r['local_allowance_quadrature'][k] for r in rows) for k in keys},
        max_filter_refinement={k:max(r['filter_12_to_20'][k] for r in rows) for k in keys},
        primitive_failures=[r for r in record['raw_primitive_checks'] if r['status'].startswith('failed')]),indent=2))

if __name__=='__main__':main()
