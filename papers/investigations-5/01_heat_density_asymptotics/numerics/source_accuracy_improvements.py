"""AN02 complete-source interpolation improvements; floating diagnostics.

Prepared for Edward Baker with substantial LLM assistance, GPT-6.1 Sol,
reasoning effort inherited from the parent session. Mathematical cell-cap
and convex-chord inequalities are continuous; their binary64 evaluations
are not outward-rounded enclosures. No model/source/cutoff change is made.
"""
import math
import time
import numpy as np
from numpy.polynomial.legendre import leggauss

PI=math.pi
US=1.5
P2=np.array([1.25,2.25,3.25,4.25])
C2=np.array([-75.,330.,-224.,32.])
P3=np.array([1.25,2.25,3.25,4.25,5.25])
C3=np.array([-375.,3270.,-4232.,1440.,-128.])


def _lse(a,axis=None):
    a=np.asarray(a)
    if axis is None: return float(np.logaddexp.reduce(a.ravel()))
    return np.logaddexp.reduce(a,axis=axis)


def phi(u,n=4):
    u=np.asarray(u)
    k=np.arange(1,n+1,dtype=float).reshape((-1,)+(1,)*u.ndim)
    A=PI*k*k*np.exp(4*u)
    return (2*PI**(-.25)*k**(-.5)*np.exp(2.25*np.log(A)-A)*(1-1.5/A)).sum(0)


def log_positive_derivative_tail(a,derivative=2,nb=8):
    """All modes n>nb via the first omitted term / (1-r).

    A_(nb+1)(a) is beyond the largest monomial maximum. The n-power
    2p-1/2 is <=8 for derivative2 and <=10 for derivative3.
    """
    powers,coeff=(P2,C2) if derivative==2 else (P3,C3)
    n=nb+1
    A=PI*n*n*np.exp(4*np.asarray(a))
    assert np.all(A>powers.max())
    ratio=(1+1/n)**(2*powers.max()-.5)*np.exp(-PI*(2*nb+3)*np.exp(4*np.asarray(a)))
    assert np.all(ratio<1)
    logs=(-.25*math.log(PI)-.5*math.log(n)+np.log(np.abs(coeff))[:,None]
          +powers[:,None]*np.log(A).reshape(1,-1)-A.reshape(1,-1))
    return _lse(logs,axis=0)-np.log1p(-np.asarray(ratio).reshape(-1))


def log_monomial_cap(a,b,derivative=2,nb=8):
    """LC5 for order2, or the analogous positive order3 bound."""
    a,b=np.asarray(a),np.asarray(b)
    powers,coeff=(P2,C2) if derivative==2 else (P3,C3)
    logs=[]
    for n in range(1,nb+1):
        lo=PI*n*n*np.exp(4*a);hi=PI*n*n*np.exp(4*b)
        v=np.clip(powers[:,None],lo[None,:],hi[None,:])
        logs.extend(-.25*math.log(PI)-.5*math.log(n)+
                    np.log(np.abs(coeff))[:,None]+powers[:,None]*np.log(v)-v)
    logs.append(log_positive_derivative_tail(a,derivative,nb))
    return _lse(np.asarray(logs),axis=0)


def log_abs_phi2_midpoint(c,nb=8):
    """|finite signed Phi''(c)| plus a positive all-mode remainder."""
    c=np.asarray(c)
    logs,signs=[],[]
    for n in range(1,nb+1):
        A=PI*n*n*np.exp(4*c)
        poly=-75+A*(330+A*(-224+32*A))
        with np.errstate(divide='ignore'):
            logs.append(-.25*math.log(PI)-.5*math.log(n)+1.25*np.log(A)-A+np.log(abs(poly)))
        signs.append(np.sign(poly))
    logs=np.asarray(logs);signs=np.asarray(signs)
    top=np.max(logs,axis=0)
    scaled=np.sum(signs*np.exp(logs-top),axis=0)
    with np.errstate(divide='ignore'):
        finite=top+np.log(abs(scaled))
    return np.logaddexp(finite,log_positive_derivative_tail(c,2,nb))


def log_bernstein_cap(a,b,nb=8):
    """Continuous signed-cubic Bernstein cap for every retained mode.

    Phi_n'' = pi^-1/4 n^-1/2 e^-A A^5/4 P(A),
    P(A)=-75+330A-224A^2+32A^3. A polynomial's range on a closed
    interval is contained in the convex hull of its Bernstein coefficients.
    The positive factor is maximized independently on the interval.
    """
    logs=[]
    for n in range(1,nb+1):
        lo=PI*n*n*np.exp(4*a);hi=PI*n*n*np.exp(4*b);d=hi-lo
        p0=-75+lo*(330+lo*(-224+32*lo))
        p1=330+lo*(-448+96*lo)
        p2=-448+192*lo
        bern=np.array([p0,p0+d*p1/3,p0+2*d*p1/3+d*d*p2/6,
                       -75+hi*(330+hi*(-224+32*hi))])
        hull=np.max(abs(bern),axis=0)
        v=np.clip(1.25,lo,hi)
        logs.append(-.25*math.log(PI)-.5*math.log(n)+1.25*np.log(v)-v+np.log(hull))
    logs.append(log_positive_derivative_tail(a,2,nb))
    return _lse(np.asarray(logs),axis=0)


def _source_nodes(mesh):
    if np.ndim(mesh)==0:
        m=int(mesh)
        if m<1 or m!=mesh:raise ValueError('Positive integer mesh size required')
        u=np.linspace(0,US,m+1)
    else:
        u=np.asarray(mesh,dtype=float)
        if u.ndim!=1 or len(u)<2 or u[0]!=0 or u[-1]!=US or np.any(np.diff(u)<=0):
            raise ValueError('Nodes must increase strictly from0 to1.5')
    return u


def cell_caps(m,nb=8):
    """Continuous mathematical caps on a uniform count or explicit nodes."""
    u=_source_nodes(m);a,b=u[:-1],u[1:];h=b-a
    lc5=log_monomial_cap(a,b,2,nb)
    third=log_monomial_cap(a,b,3,nb)
    middle=np.logaddexp(log_abs_phi2_midpoint((a+b)/2,nb),np.log(h/2)+third)
    bern=log_bernstein_cap(a,b,nb)
    return dict(u=u,a=a,b=b,h=h,lc5=lc5,midpoint=middle,bernstein=bern,
                best=np.minimum(lc5,np.minimum(middle,bern)),
                third=third,complete_mode_tail_log=log_positive_derivative_tail(a,2,nb))


def weight_integrals(a,b,j,t,Y=1.,method='gauss',order=8):
    """Return interpolation and left/right hat weight integrals.

    interpolation = (1/2) integral (u-a)(b-u) W_j du.
    hats = integral (1-v) W_j du, integral v W_j du.
    For t,Y>=0, W_j''>=0. The chord option is a continuous upper bound,
    using order equal subintervals and positive exact polynomial weights.
    The Gauss option is a diagnostic integration, with unpaid remainder.
    """
    if order not in (8,12): raise ValueError('Only levels8 and12 are in scope')
    a,b=np.asarray(a),np.asarray(b);h=b-a
    if method=='lc4':
        W=b**j*np.exp(t*b*b+Y*b)
        return h**3*W/12,h*W/2,h*W/2
    if method=='gauss':
        s,w=leggauss(order);v=(s+1)/2;w=w/2
        u=a[:,None]+h[:,None]*v
        W=u**j*np.exp(t*u*u+Y*u)
        return (h**3/2*(W@(w*v*(1-v))),
                h*(W@(w*(1-v))),h*(W@(w*v)))
    if method=='chord':
        if t<0 or Y<0 or j<0 or int(j)!=j:
            raise ValueError('Convexity proof here needs t,Y>=0, integer j>=0')
        v=np.linspace(0,1,order+1);d=1/order;c=(v[:-1]+v[1:])/2
        u=a[:,None]+h[:,None]*v
        W=u**j*np.exp(t*u*u+Y*u)
        left,right=W[:,:-1],W[:,1:]
        # Exact integrals of the quadratic/linear factors times each
        # nonnegative affine chord basis on each source-cell subinterval.
        il=d*c*(1-c)/2-(1-2*c)*d*d/12-d**3/24
        ir=d*c*(1-c)/2+(1-2*c)*d*d/12-d**3/24
        ll=d*(1-c)/2+d*d/12;lr=d*(1-c)/2-d*d/12
        rl=d*c/2-d*d/12;rr=d*c/2+d*d/12
        assert min(il.min(),ir.min(),ll.min(),lr.min(),rl.min(),rr.min())>0
        return (h**3/2*(left@il+right@ir),
                h*(left@ll+right@lr),h*(left@rl+right@rr))
    raise ValueError('Unknown weight method')


def complete_tail_log(t,j,Y=1.):
    """FB7 logarithm; preserves a positive tail below IEEE underflow."""
    U=US;s=max(t,0)
    lam=4*PI*math.exp(4*U)-2*s*U-9-Y-j/U
    assert lam>0 and 16*PI*math.exp(4*U)>=2*s
    cb=1/(1-16*math.exp(-3*PI))
    return math.log(2*PI*PI*cb)+j*math.log(U)+s*U*U+(9+Y)*U-PI*math.exp(4*U)-math.log(lam)


def source_budget(m,t=64.,n=4,jmax=3,order=8,cap='best',weights='chord',Y=1.,return_arrays=False):
    """LC2/4 categories and per-cell logarithms for selected improved caps.

    Old source cutoff/modes stay fixed. Nodal arithmetic retains exactly
    the historical unproved candidate 1e-12 Phi_N(u_i)+1e-300. No rounding
    category is promoted to a certificate. Integrated hats also tighten
    omitted modes and candidate arithmetic without merging their ledgers.
    """
    data=cell_caps(m);u,a,b=data['u'],data['a'],data['b']
    if cap not in ('lc5','midpoint','bernstein','best'):raise ValueError('Unknown cap')
    logB=data[cap]
    A=PI*(n+1)**2*np.exp(4*u)
    ratio=(1+1/(n+1))**4*np.exp(-PI*(2*n+3)*np.exp(4*u))
    logmode=math.log(2*PI*PI*(n+1)**4)+9*u-A-np.log1p(-ratio)
    f=phi(u,n)
    with np.errstate(divide='ignore'):
        logsigma=np.logaddexp(math.log(1e-12)+np.log(f),math.log(1e-300))
    rows=[];arrays=[]
    for j in range(jmax+1):
        wi,wl,wr=weight_integrals(a,b,j,t,Y,weights,order)
        li=logB+np.log(wi)
        lm=np.logaddexp(logmode[:-1]+np.log(wl),logmode[1:]+np.log(wr))
        la=np.logaddexp(logsigma[:-1]+np.log(wl),logsigma[1:]+np.log(wr))
        totals=[_lse(li),_lse(lm),complete_tail_log(t,j,Y),_lse(la)]
        total_log=_lse(totals)
        k=int(np.argmax(li));positive=np.exp(li-_lse(li));centers=(a+b)/2
        rows.append(dict(j=j,interpolation=math.exp(totals[0]),
            omitted_modes=math.exp(totals[1]),complete_tail_log10=totals[2]/math.log(10),
            nodal_arithmetic_candidate=math.exp(totals[3]),total=math.exp(total_log),
            log10_categories=[x/math.log(10) for x in totals],
            dominant_cell_index=k,dominant_cell=[float(a[k]),float(b[k])],
            dominant_cell_fraction=float(positive[k]),
            interpolation_weighted_mean_u=float(positive@centers),
            central_90pct_u=[float(centers[np.searchsorted(np.cumsum(positive),q)]) for q in (.05,.95)]))
        arrays.append(dict(j=j,log_interpolation=li,log_modes=lm,log_nodal_candidate=la))
    out=dict(cells=len(u)-1,mesh_kind=('uniform' if np.ndim(m)==0 else 'explicit_nodes'),
             t=t,modes=n,cutoff=US,cap=cap,weight_method=weights,
             weight_level=order,rounding='unpaid; binary64 diagnostic',
             quadrature_remainder=('unpaid' if weights=='gauss' else
                 'continuous convex-chord upper bound' if weights=='chord' else 'LC4 maximum bound'),
             rows=rows)
    if return_arrays:out['arrays']=arrays;out['cell_caps']=data
    return out


def adaptive_nodes(m=768,t=64.,Y=1.,pilot=4096,floor_fraction=.05,return_metadata=False):
    """One a priori source-only mesh; no field, root or filter-node data.

    A fixed pilot4096-cell continuous curvature envelope and upper-endpoint
    weight define piecewise-constant rho_i=(B_i exp(t*b_i^2+Y*b_i)
    (1+b_i^3))^(1/3). The factor1+u^3 covers source orders0...3 up to
    the harmless inequality u^j<=1+u^3. A fixed5%-of-peak positive floor
    prevents huge tail cells and preserves full cutoff coverage.
    Invert the exact cumulative integral of this piecewise-constant density.
    Pilot sampling does not certify the resulting optimized mesh: all
    final cell caps are recomputed continuously on the actual returned mesh.
    """
    if m!=768 or pilot!=4096 or floor_fraction!=.05:
        raise ValueError('The bounded AN02 adaptive test is fixed at768/4096/floor.05')
    d=cell_caps(pilot);u=d['u'];b=d['b']
    logrho=(d['best']+t*b*b+Y*b+np.log1p(b**3))/3
    shift=float(logrho.max());raw=np.exp(logrho-shift)
    density=np.maximum(raw,floor_fraction)
    mass=density*np.diff(u);cum=np.r_[0.,np.cumsum(mass)]
    targets=np.linspace(0,cum[-1],m+1)
    k=np.searchsorted(cum,targets,side='right')-1;k=np.clip(k,0,pilot-1)
    nodes=u[k]+(targets-cum[k])/density[k]
    nodes[0],nodes[-1]=0.,US
    assert np.all(np.diff(nodes)>0)
    recovered=np.interp(nodes,u,cum)
    target_mass=float(cum[-1]/m)
    metadata=dict(cells=m,pilot_cells=pilot,density='[B_i exp(t*b_i^2+Y*b_i)(1+b_i^3)]^(1/3)',
        floor_fraction_of_peak=floor_fraction,normalized_density_integral=float(cum[-1]),
        density_log_scale=shift,target_normalized_cell_mass=target_mass,
        cumulative_mass_residual_in_cells=float(np.max(abs(recovered-targets))/target_mass),
        actual_cell_mass_over_target=[float(np.diff(recovered).min()/target_mass),float(np.diff(recovered).max()/target_mass)],
        min_width=float(np.diff(nodes).min()),
        max_width=float(np.diff(nodes).max()),
        cells_midpoint_below_06=int(np.count_nonzero((nodes[:-1]+nodes[1:])/2<.6)),
        source_only=True,continuous_final_caps_recomputed=True)
    return (nodes,metadata) if return_metadata else nodes


if __name__=='__main__':
    started=time.perf_counter()
    for m in (192,384,768):
        old=source_budget(m,cap='lc5',weights='lc4')['rows']
        ig=source_budget(m,cap='lc5',weights='gauss',order=12)['rows']
        mid=source_budget(m,cap='midpoint',weights='chord',order=12)['rows']
        bern=source_budget(m,cap='bernstein',weights='chord',order=12)['rows']
        best=source_budget(m,cap='best',weights='chord',order=12)['rows']
        print(dict(cells=m,j0=[z[0]['interpolation'] for z in (old,ig,mid,bern,best)],
                   j2=[z[2]['interpolation'] for z in (old,ig,mid,bern,best)],
                   best_gain_j0=old[0]['interpolation']/best[0]['interpolation'],
                   peak=best[0]['dominant_cell'],central90=best[0]['central_90pct_u']))
    print('runtime_seconds',time.perf_counter()-started)
