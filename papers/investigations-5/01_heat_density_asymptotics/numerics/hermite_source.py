"""AN03 positive cubic-Hermite finite source and explicit source remainders.

Prepared for Edward Baker with substantial LLM assistance, GPT-6.1 Sol.
Stored finite, nonnegative binary64 Bernstein coefficients define the exact
finite source. Positivity follows algebraically; transcendental nodal value
and derivative error candidates remain unproved. All floating budget values
are diagnostics, not outward-rounded continuous numerical certificates.
"""
import math
import time
from fractions import Fraction
from functools import lru_cache
import numpy as np
from numpy.polynomial.legendre import leggauss

PI=math.pi
US=1.5
# d/du = 4A d/dA, A=pi*n^2*exp(4u). Every derivative below has
# pi^(-1/4)n^(-1/2) exp(-A) A^(5/4) times the indicated polynomial.
CP={0:np.array([-3.,2.]),1:np.array([-15.,30.,-8.]),
    2:np.array([-75.,330.,-224.,32.]),
    3:np.array([-375.,3270.,-4232.,1440.,-128.]),
    4:np.array([-1875.,30930.,-68096.,41408.,-8448.,512.])}
BASIS={'hermite_remainder':[0,0,1,-2,1],
       'linear_remainder':[0,1,-1],
       'value_left':[1,0,-3,2], 'value_right':[0,0,3,-2],
       'slope_left_abs':[0,1,-2,1], 'slope_right_abs':[0,0,1,-1],
       'linear_left':[1,-1], 'linear_right':[0,1],
       'bernstein0':[1,-3,3,-1], 'bernstein1':[0,3,-6,3],
       'bernstein2':[0,0,3,-3], 'bernstein3':[0,0,0,1]}


def lse(x,axis=None):
    x=np.asarray(x)
    return float(np.logaddexp.reduce(x.ravel())) if axis is None else np.logaddexp.reduce(x,axis=axis)


def nodes_array(mesh):
    if np.ndim(mesh)==0:
        if int(mesh)!=mesh or mesh<1:raise ValueError('Positive mesh count required')
        u=np.linspace(0,US,int(mesh)+1)
    else:u=np.asarray(mesh,dtype=float)
    if u.ndim!=1 or len(u)<2 or u[0]!=0 or u[-1]!=US or np.any(np.diff(u)<=0):
        raise ValueError('Nodes must increase strictly from0 to1.5')
    return u


def theta_values_slopes(u,n=4):
    """Canonical Phi_N and Phi_N', evaluated directly with internal A scaling."""
    u=np.asarray(u);k=np.arange(1,n+1).reshape((-1,)+(1,)*u.ndim)
    A=PI*k*k*np.exp(4*u)
    scale=PI**(-.25)*k**(-.5)*np.exp(1.25*np.log(A)-A)
    f=np.sum(scale*(2*A-3),axis=0)
    d=np.sum(scale*(-15+A*(30-8*A)),axis=0)
    return f,d


def log_positive_tail(u,derivative=2,nb=8):
    """All modes beyond nb, positive monomials and geometric mode ratio."""
    u=np.asarray(u).reshape(-1);c=CP[derivative];p=1.25+np.arange(len(c))
    n=nb+1;A=PI*n*n*np.exp(4*u)
    assert np.all(A>p.max())
    ratio=(1+1/n)**(2*p.max()-.5)*np.exp(-PI*(2*nb+3)*np.exp(4*u))
    assert np.all(ratio<1)
    terms=(-.25*math.log(PI)-.5*math.log(n)+np.log(abs(c))[:,None]
           +p[:,None]*np.log(A)[None,:]-A[None,:])
    return lse(terms,axis=0)-np.log1p(-ratio)


def log_monomial_cap(a,b,derivative,nb=8):
    a,b=np.asarray(a),np.asarray(b);c=CP[derivative];p=1.25+np.arange(len(c));terms=[]
    for n in range(1,nb+1):
        lo=PI*n*n*np.exp(4*a);hi=PI*n*n*np.exp(4*b)
        v=np.clip(p[:,None],lo[None,:],hi[None,:])
        terms.extend(-.25*math.log(PI)-.5*math.log(n)+np.log(abs(c))[:,None]+p[:,None]*np.log(v)-v)
    terms.append(log_positive_tail(a,derivative,nb))
    return lse(terms,axis=0)


def log_bernstein_cap(a,b,derivative=4,nb=8):
    """Continuous signed-polynomial hull cap plus an all-mode tail.

    Polynomial degree is3 for Phi'' and5 for Phi^(4). The exact Bernstein
    coefficients on [Alo,Ahi] give a convex hull containing its full range.
    The factor A^(5/4)exp(-A) is maximized separately. No root search enters.
    """
    a,b=np.asarray(a),np.asarray(b);poly=CP[derivative];degree=len(poly)-1;terms=[]
    for n in range(1,nb+1):
        lo=PI*n*n*np.exp(4*a);hi=PI*n*n*np.exp(4*b);width=hi-lo
        power=[]
        for j in range(degree+1):
            dp=np.polynomial.polynomial.polyder(poly,j)
            power.append(np.polynomial.polynomial.polyval(lo,dp)*width**j/math.factorial(j))
        bern=[sum(power[j]*math.comb(k,j)/math.comb(degree,j) for j in range(k+1))
              for k in range(degree+1)]
        hull=np.max(abs(np.asarray(bern)),axis=0)
        v=np.clip(1.25,lo,hi)
        terms.append(-.25*math.log(PI)-.5*math.log(n)+1.25*np.log(v)-v+np.log(hull))
    terms.append(log_positive_tail(a,derivative,nb))
    return lse(terms,axis=0)


def log_abs_phi2(c,nb=8):
    c=np.asarray(c);terms=[];signs=[]
    for n in range(1,nb+1):
        A=PI*n*n*np.exp(4*c);p=np.polynomial.polynomial.polyval(A,CP[2])
        with np.errstate(divide='ignore'):
            terms.append(-.25*math.log(PI)-.5*math.log(n)+1.25*np.log(A)-A+np.log(abs(p)))
        signs.append(np.sign(p))
    terms=np.asarray(terms);top=np.max(terms,axis=0)
    with np.errstate(divide='ignore'):
        answer=top+np.log(abs(np.sum(np.asarray(signs)*np.exp(terms-top),axis=0)))
    return np.logaddexp(answer,log_positive_tail(c,2,nb))


def complete_caps(nodes):
    u=nodes_array(nodes);a,b=u[:-1],u[1:];h=b-a
    b2=np.minimum(log_monomial_cap(a,b,2),log_bernstein_cap(a,b,2))
    b2=np.minimum(b2,np.logaddexp(log_abs_phi2((a+b)/2),np.log(h/2)+log_monomial_cap(a,b,3)))
    b4=np.minimum(log_monomial_cap(a,b,4),log_bernstein_cap(a,b,4))
    return b2,b4


def _fraction_upper(value):
    """Convert a nonnegative rational to an upper binary64 number exactly."""
    z=float(value)
    if Fraction.from_float(z)<value:z=np.nextafter(z,np.inf)
    return z


def build_source(nodes,n=4,gamma=1e-12):
    """Build one exact positive finite source from stored Bernstein values.

    If any proposed cubic Bernstein coefficient is negative, use the linear
    interpolant for that whole cell. There is no clipping of cubic values.
    Fraction comparisons pay the discrepancy between stored coefficients and
    the ideal Hermite/linear coefficients of the exact stored nodal floats,
    including the source-cell width subtraction and division by3.
    """
    started=time.perf_counter();u=nodes_array(nodes);h=np.diff(u);f,d=theta_values_slopes(u,n)
    coef=np.array([f[:-1],f[:-1]+h*d[:-1]/3,f[1:]-h*d[1:]/3,f[1:]]).T
    if not np.all(np.isfinite(coef)):raise ArithmeticError('Nonfinite source coefficient')
    fallback=np.any(coef<0,axis=1)
    for i in np.flatnonzero(fallback):
        coef[i]=[f[i],(2*f[i]+f[i+1])/3,(f[i]+2*f[i+1])/3,f[i+1]]
    if np.any(coef<0) or not np.all(np.isfinite(coef)):
        raise ArithmeticError('Nonnegative source construction failed')
    rounding=np.zeros_like(coef)
    fq=[Fraction.from_float(float(x)) for x in f]
    dq=[Fraction.from_float(float(x)) for x in d]
    uq=[Fraction.from_float(float(x)) for x in u]
    for i in range(len(h)):
        if fallback[i]:ideal=[fq[i],(2*fq[i]+fq[i+1])/3,(fq[i]+2*fq[i+1])/3,fq[i+1]]
        else:
            width=uq[i+1]-uq[i]
            ideal=[fq[i],fq[i]+width*dq[i]/3,fq[i+1]-width*dq[i+1]/3,fq[i+1]]
        rounding[i]=[_fraction_upper(abs(Fraction.from_float(float(c))-v)) for c,v in zip(coef[i],ideal)]
    # Separate unproved nodal arithmetic candidates; derivative error uses
    # positive monomials, which survive the cancellation Phi_N'(0)~0.
    with np.errstate(divide='ignore'):
        log_value_candidate=np.logaddexp(math.log(gamma)+np.log(f),math.log(1e-300))
    logs=[]
    for k in range(1,n+1):
        A=PI*k*k*np.exp(4*u)
        logs.extend(-.25*math.log(PI)-.5*math.log(k)+np.log(abs(CP[1]))[:,None]
                    +(1.25+np.arange(3))[:,None]*np.log(A)[None,:]-A[None,:])
    log_slope_candidate=np.logaddexp(math.log(gamma)+lse(logs,axis=0),math.log(1e-300))
    b2,b4=complete_caps(u)
    meta=dict(cells=len(h),modes=n,cutoff=US,stored_bernstein_coefficients=4*len(h),
        distinct_nodal_values=len(u),distinct_nodal_slopes=len(u),
        fallback_cells=int(fallback.sum()),hermite_cells=int((~fallback).sum()),
        fallback_indices=np.flatnonzero(fallback).tolist(),
        zero_stored_coefficients=int(np.count_nonzero(coef==0)),
        min_coefficient=float(coef.min()),nonnegative_stored_coefficients=True,
        positivity='exact algebraic consequence for stored nonnegative binary64 Bernstein coefficients',
        coefficient_construction_rounding='exact rational discrepancy; upper binary64 conversions',
        nodal_value_derivative_arithmetic='separate unproved candidates gamma=1e-12 plus1e-300 floor',
        min_width=float(h.min()),max_width=float(h.max()),build_seconds=time.perf_counter()-started)
    return dict(nodes=u,h=h,values=f,slopes=d,coefficients=coef,fallback=fallback,
        coefficient_rounding=rounding,log_value_candidate=log_value_candidate,
        log_slope_candidate=log_slope_candidate,log_B2=b2,log_B4=b4,metadata=meta)


@lru_cache(None)
def _chord_moments(name,order):
    """Exact rational integrals p(v)*left/right affine chord bases."""
    poly=BASIS[name];left=[];right=[]
    def moment(power,a,b):return (b**(power+1)-a**(power+1))/(power+1)
    for k in range(order):
        a=Fraction(k,order);b=Fraction(k+1,order);d=b-a
        z0=sum(Fraction(c)*moment(j,a,b) for j,c in enumerate(poly))
        z1=sum(Fraction(c)*moment(j+1,a,b) for j,c in enumerate(poly))
        ll=(b*z0-z1)/d;rr=(z1-a*z0)/d
        assert ll>0 and rr>0
        left.append(_fraction_upper(ll));right.append(_fraction_upper(rr))
    return np.asarray(left),np.asarray(right)


def integrated_basis(source,j,t=64.,Y=1.,order=8,weights='chord'):
    """Positive integrals int_0^1 p(v) W_j(a+hv)dv for every needed p.

    Convex W_j gives a continuous upper bound by affine secants; exact
    rational polynomial moments define positive coefficients. Endpoint
    exponentials and subsequent binary64 arithmetic remain unpaid.
    """
    if order not in (8,12):raise ValueError('Only8/12 refinement levels are in scope')
    a=source['nodes'][:-1];h=source['h']
    if weights=='gauss':
        x,w=leggauss(order);v=(x+1)/2;w=w/2
        u=a[:,None]+h[:,None]*v;W=u**j*np.exp(t*u*u+Y*u)
        return {name:W@(w*np.polynomial.polynomial.polyval(v,p)) for name,p in BASIS.items()}
    if weights=='chord':
        if t<0 or Y<0 or j<0 or int(j)!=j:raise ValueError('Convexity needs t,Y>=0, integerj>=0')
        v=np.linspace(0,1,order+1);u=a[:,None]+h[:,None]*v
        W=u**j*np.exp(t*u*u+Y*u);left,right=W[:,:-1],W[:,1:]
        return {name:left@_chord_moments(name,order)[0]+right@_chord_moments(name,order)[1]
                for name in BASIS}
    raise ValueError('weights must be chord or gauss')


def complete_tail_log(t,j,Y=1.):
    s=max(t,0);U=US;lam=4*PI*math.exp(4*U)-2*s*U-9-Y-j/U
    assert lam>0 and 16*PI*math.exp(4*U)>=2*s
    return math.log(2*PI*PI/(1-16*math.exp(-3*PI)))+j*math.log(U)+s*U*U+(9+Y)*U-PI*math.exp(4*U)-math.log(lam)


def source_budget(source,t=64.,Y=1.,order=8,weights='chord',jmax=3,return_arrays=False):
    """Complete source orders0..3, with every requested category separate."""
    u=source['nodes'];h=source['h'];fallback=source['fallback'];n=source['metadata']['modes']
    A=PI*(n+1)**2*np.exp(4*u);ratio=(1+1/(n+1))**4*np.exp(-PI*(2*n+3)*np.exp(4*u))
    logtau=math.log(2*PI*PI*(n+1)**4)+9*u-A-np.log1p(-ratio)
    logtau1=log_positive_tail(u,1,n)
    rows=[];arrays=[]
    for j in range(jmax+1):
        z=integrated_basis(source,j,t,Y,order,weights)
        with np.errstate(divide='ignore'):
            logi4=source['log_B4']+5*np.log(h)+np.log(z['hermite_remainder'])-math.log(24)
            logi2=source['log_B2']+3*np.log(h)+np.log(z['linear_remainder'])-math.log(2)
        logi4=np.where(fallback,-np.inf,logi4);logi2=np.where(fallback,logi2,-np.inf)
        log_interp=np.logaddexp(logi4,logi2)
        vl=h*np.where(fallback,z['linear_left'],z['value_left'])
        vr=h*np.where(fallback,z['linear_right'],z['value_right'])
        dl=np.where(fallback,0,h*h*z['slope_left_abs'])
        dr=np.where(fallback,0,h*h*z['slope_right_abs'])
        with np.errstate(divide='ignore'):
            lvl,lvr,ldl,ldr=map(np.log,(vl,vr,dl,dr))
            logm0=np.logaddexp(logtau[:-1]+lvl,logtau[1:]+lvr)
            logm1=np.logaddexp(logtau1[:-1]+ldl,logtau1[1:]+ldr)
            loga0=np.logaddexp(source['log_value_candidate'][:-1]+lvl,source['log_value_candidate'][1:]+lvr)
            loga1=np.logaddexp(source['log_slope_candidate'][:-1]+ldl,source['log_slope_candidate'][1:]+ldr)
            logc=lse(np.stack([np.log(source['coefficient_rounding'][:,k])+np.log(h*z['bernstein'+str(k)]) for k in range(4)]),axis=0)
        categories=dict(interpolation=lse(log_interp),omitted_value_modes=lse(logm0),
            omitted_derivative_modes=lse(logm1),nodal_value_arithmetic_candidate=lse(loga0),
            nodal_derivative_arithmetic_candidate=lse(loga1),
            coefficient_construction_rounding=lse(logc),complete_tail=complete_tail_log(t,j,Y))
        row={key:(math.exp(value) if key!='complete_tail' else None) for key,value in categories.items()}
        row.pop('complete_tail');row.update(j=j,complete_tail_log10=categories['complete_tail']/math.log(10),
            total=math.exp(lse(list(categories.values()))),
            interpolation_hermite=math.exp(lse(logi4)),interpolation_fallback_linear=math.exp(lse(logi2)),
            omitted_modes=math.exp(np.logaddexp(categories['omitted_value_modes'],categories['omitted_derivative_modes'])),
            nodal_arithmetic_candidate=math.exp(np.logaddexp(categories['nodal_value_arithmetic_candidate'],categories['nodal_derivative_arithmetic_candidate'])),
            log10_categories={key:val/math.log(10) for key,val in categories.items()})
        k=int(np.argmax(log_interp));row['dominant_cell']=[float(u[k]),float(u[k+1])]
        rows.append(row);arrays.append(dict(j=j,log_interpolation=log_interp,log_hermite=logi4,log_fallback=logi2,log_modes_value=logm0,log_modes_derivative=logm1,log_nodal_value=loga0,log_nodal_derivative=loga1,log_coefficient_rounding=logc))
    out=dict(source=source['metadata'],t=t,Y=Y,weight_method=weights,weight_order=order,
        weight_integration=('continuous convex-secant upper bound' if weights=='chord' else 'Gauss diagnostic; remainder unpaid'),
        rounding='nodal transcendental and budget arithmetic unpaid; source coefficient construction discrepancy paid separately',rows=rows)
    if return_arrays:out['arrays']=arrays
    return out


def source_rule(source,order=8):
    """Finite-source Gauss nodes and physical weights times stored cubic.

    Return signature matches the AN01/02 field evaluator. The ideal source
    is the exact polynomial with stored Bernstein coefficients; quadrature,
    node geometry and this binary64 evaluation have their later ledger.
    """
    if order not in (8,12):raise ValueError('Only8/12 refinements are in scope')
    v,w=leggauss(order);v=(v+1)/2;w=w/2;a=source['nodes'][:-1];h=source['h']
    u=a[:,None]+h[:,None]*v
    B=np.array([(1-v)**3,3*v*(1-v)**2,3*v*v*(1-v),v**3])
    values=source['coefficients']@B
    return u.ravel(),(h[:,None]*w*values).ravel()


def adaptive_nodes(m=768,t=64.,Y=1.,pilot=4096,floor_fraction=.05,return_metadata=False):
    """AN02 source-only quantile rule, now at the declared384/768 counts."""
    if m not in (384,768) or pilot!=4096 or floor_fraction!=.05:
        raise ValueError('Only adaptive384/768, pilot4096, floor.05 are in scope')
    u=np.linspace(0,US,pilot+1);b=u[1:];b2,_=complete_caps(u)
    logrho=(b2+t*b*b+Y*b+np.log1p(b**3))/3;shift=float(logrho.max())
    density=np.maximum(np.exp(logrho-shift),floor_fraction)
    cum=np.r_[0.,np.cumsum(density*np.diff(u))];targets=np.linspace(0,cum[-1],m+1)
    k=np.clip(np.searchsorted(cum,targets,side='right')-1,0,pilot-1)
    nodes=u[k]+(targets-cum[k])/density[k];nodes[0],nodes[-1]=0.,US
    recovered=np.interp(nodes,u,cum);mass=float(cum[-1]/m)
    metadata=dict(cells=m,pilot_cells=pilot,floor_fraction_of_peak=floor_fraction,
        density='[complete curvature cap*exp(tu^2+Yu)*(1+u^3)]^(1/3)',
        source_only=True,min_width=float(np.diff(nodes).min()),max_width=float(np.diff(nodes).max()),
        cumulative_mass_residual_in_cells=float(np.max(abs(recovered-targets))/mass))
    return (nodes,metadata) if return_metadata else nodes
