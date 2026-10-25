"""HDA-17-AN01: auditable positive CJ5--CJ14 coefficient substitutions.

Prepared for Edward Baker with substantial LLM assistance. This module uses
binary64 floating arithmetic. Kernel L1 values are analytic polynomial-root
integrals evaluated in floating arithmetic, not interval enclosures. Local
positive-convolution values and any unsupplied scalar extrema are diagnostic.
No coefficient depends on the requested actual d0, d2 or eta_E: only the
fixed amplitude caps bar0 and bar2 enter before the three source columns.
"""
import math
import numpy as np
from numpy.polynomial import polynomial as _poly
from numpy.polynomial.legendre import leggauss

KPOLY = (315.0/256.0)*np.array([1.,0.,-4.,0.,6.,0.,-4.,0.,1.])
FOUR_PI = 4*math.pi


def multi_indices(max_order):
    """All Cartesian multi-indices through a specified total order."""
    return [(i,n-i) for n in range(max_order+1) for i in range(n,-1,-1)]


def _add(a,b):
    return a[0]+b[0], a[1]+b[1]


def kernel_roots(derivative):
    """Interior real zeros of d^j[(1-u^2)^4], j=0,...,4."""
    if derivative == 0:
        return []
    if derivative == 1:
        return [0.]
    if derivative == 2:
        a = 1/math.sqrt(7)
        return [-a,a]
    if derivative == 3:
        a = math.sqrt(3/7)
        return [-a,0.,a]
    if derivative == 4:
        a = math.sqrt((15-2*math.sqrt(30))/35)
        b = math.sqrt((15+2*math.sqrt(30))/35)
        return [-b,-a,a,b]
    raise ValueError('Only kernel derivatives 0 through 4 are defined')


def kernel_l1_1d(derivative,scale=1.):
    """Exact algebraic-root decomposition, evaluated in binary64.

    K_scale(u)=scale^-1 (315/256)(1-(u/scale)^2)^4 on |u|<scale.
    The normalization is one, and no boundary delta enters through order 4.
    """
    p = _poly.polyder(KPOLY,derivative)
    ip = _poly.polyint(p)
    edges = [-1.]+kernel_roots(derivative)+[1.]
    value = sum(abs(_poly.polyval(b,ip)-_poly.polyval(a,ip))
                for a,b in zip(edges[:-1],edges[1:]))
    return float(value/scale**derivative)


def kernel_data(order,ell=2.,h=.5):
    """Tensor Gauss rule and signed/absolute kernel derivative weights.

    x,y are flattened physical offsets. Weights are already quadrature
    weights times the indicated K derivative; parent code must not multiply
    by the geometric weights a second time. Absolute M,D,B maps use sums of
    component absolute weights, which are valid triangle majorants.
    """
    if order not in (16,32,64):
        raise ValueError('HDA-17 filter orders are restricted to 16,32,64')
    if ell <= 0 or h <= 0:
        raise ValueError('Kernel scales must be positive')
    v,w = leggauss(order)
    vx,vy = np.meshgrid(v,v,indexing='ij')
    base = np.outer(w,w)*ell*h
    pd = [_poly.polyval(v,_poly.polyder(KPOLY,j)) for j in range(5)]
    signed,absolute,L = {},{},{}
    for i,j in multi_indices(4):
        kw = base*np.outer(pd[i]/ell**(i+1),pd[j]/h**(j+1))
        signed[(i,j)] = kw.ravel()
        absolute[(i,j)] = np.abs(kw).ravel()
        L[(i,j)] = kernel_l1_1d(i,ell)*kernel_l1_1d(j,h)
    return dict(order=order,ell=ell,h=h,x=(ell*vx).ravel(),
                y=(h*vy).ravel(),geometric_weights=base.ravel(),
                signed_weights=signed,abs_weights=absolute,L=L,
                l1_1d_x=[kernel_l1_1d(j,ell) for j in range(5)],
                l1_1d_y=[kernel_l1_1d(j,h) for j in range(5)])


def _interval_amplitudes(amplitude,q,bar0):
    """CJ4 maximum values on the entire closed modulus interval."""
    lower = np.maximum(amplitude-bar0,0.)
    upper = amplitude+bar0
    sq = np.sqrt(q)
    # v/(q+v^2) grows to sqrt(q), then decreases.
    va = np.minimum(np.maximum(sq,lower),upper)
    a = va/(q+va*va)
    # 2qv/(q+v^2)^2 grows to sqrt(q/3), then decreases.
    vk = np.minimum(np.maximum(sq/math.sqrt(3),lower),upper)
    k = 2*q*vk/(q+vk*vk)**2
    bstar = 1/(q+lower*lower)
    return a,bstar,k,upper


def weak_coefficients(g,q,rt,rx,rxx,rtx,rtxx,bar0,bar2,kernel,
                      scalar=False,reg_caps=None,field_caps=None):
    """Return all CJ14 rows as fixed nonnegative [A,B,C] coefficients.

    g has shape (nodes, >=3); columns 0,2 are F,F_zz. Scalar q and regulator
    derivatives broadcast. reg_caps, when supplied for a scalar continuous
    buffer bound, has q_min,q_max,a0,R1,R2,T1,T2,Th,b0,c0. field_caps has
    P0 >= sup|F|+bar0 and P2 >= sup|F_zz|+bar2. Unprovided extrema are sampled
    and remain diagnostic. bar0/bar2 must be fixed before source refinement.
    The q supplied to local mode is the actual physical q, not a shifted q.
    """
    g = np.asarray(g)
    if g.ndim != 2 or g.shape[1] < 3:
        raise ValueError('g must have shape (nodes,>=3)')
    n = g.shape[0]
    def nodes(value):
        return np.broadcast_to(np.asarray(value,dtype=float),(n,)).copy()
    q,rt,rx,rxx,rtx,rtxx = map(nodes,(q,rt,rx,rxx,rtx,rtxx))
    if np.any(q <= 0) or np.any(~np.isfinite(q)):
        raise ValueError('q must be finite and strictly positive')
    if bar0 < 0 or bar2 < 0:
        raise ValueError('Fixed source caps must be nonnegative')
    qmin,qmax = float(q.min()),float(q.max())
    amp,amp2 = np.abs(g[:,0]),np.abs(g[:,2])
    sampled = dict(q_min=qmin,q_max=qmax,a0=float(np.max(np.abs(rt))),
                   R1=float(np.max(np.abs(rx))),R2=float(np.max(np.abs(rxx))),
                   T1=float(np.max(np.abs(rtx))),T2=float(np.max(np.abs(rtxx))),
                   Th=float(np.max(np.abs(2*rx*rtx))),
                   b0=float(np.max(np.abs(rt+(rxx+rx*rx)/2))),
                   c0=float(np.max(np.abs(rxx+rx*rx))))
    full_reg_keys = set(sampled)
    supplied_reg = reg_caps is not None and full_reg_keys.issubset(reg_caps)
    supplied_field = field_caps is not None and {'P0','P2'}.issubset(field_caps)
    if scalar:
        caps = dict(sampled)
        caps.update(reg_caps or {})
        qmin,qmax = caps['q_min'],caps['q_max']
        if qmin <= 0 or qmax < qmin:
            raise ValueError('Invalid scalar q interval')
        fc = dict(P0=float(amp.max()+bar0),P2=float(amp2.max()+bar2))
        fc.update(field_caps or {})
        P2 = np.array([fc['P2']])
        a = np.array([1/(2*math.sqrt(qmin))])
        bstar = np.array([1/qmin])
        k = np.array([1/math.sqrt(qmin)])
        zfactor = np.array([1/(2*math.sqrt(qmin))])
        a0,R1,R2,T1,T2,Th,b0,c0 = [np.array([caps[key]]) for key in
            ('a0','R1','R2','T1','T2','Th','b0','c0')]
        log_upper = float(np.logaddexp(2*math.log(fc['P0']) if fc['P0'] else
                                      -np.inf,math.log(qmax)))
        Sstar = np.array([max(abs(math.log(qmin)),abs(log_upper))])
        active_n = 1
    else:
        if n != kernel['x'].size:
            raise ValueError('Local field and kernel node counts differ')
        a,bstar,k,P0 = _interval_amplitudes(amp,q,bar0)
        P2 = amp2+bar2
        zfactor = 1/(2*np.sqrt(q))
        a0,R1,R2 = np.abs(rt),np.abs(rx),np.abs(rxx)
        T1,T2,Th = np.abs(rtx),np.abs(rtxx),np.abs(2*rx*rtx)
        b0,c0 = np.abs(rt+(rxx+rx*rx)/2),np.abs(rxx+rx*rx)
        log_upper = np.logaddexp(2*np.log(np.maximum(P0,np.finfo(float).tiny)),
                                 np.log(q))
        Sstar = np.maximum(np.abs(np.log(q)),np.abs(log_upper))
        caps = sampled
        active_n = n
    # Every source error is represented by its three independent columns.
    def vector(c0=0.,c2=0.,ce=0.):
        return np.column_stack([np.broadcast_to(c,(active_n,))
                                for c in (c0,c2,ce)])
    s,w,z = vector(2*a),vector(k),vector(ce=zfactor)
    v = [vector(P2*bstar+m*P2*a*k,a) for m in range(3)]
    st = 2*v[0]+a0[:,None]*w+2*z
    wt = a0[:,None]*w+2*v[1]+2*z
    ct = a0[:,None]*w+2*v[1]+4*v[2]+6*z
    L = kernel['L']
    def cv(alpha,value):
        if scalar:
            return L[alpha]*value[0]
        return kernel['abs_weights'][alpha]@value
    def mg(alpha,value):
        return cv(_add(alpha,(1,0)),value)+cv(_add(alpha,(0,1)),value)
    def db(alpha,value):
        return cv(_add(alpha,(2,0)),value)+cv(_add(alpha,(0,2)),value)
    def c_map(alpha):
        return (2*mg(alpha,R1[:,None]*w)+
                cv(alpha,(R2+R1*R1)[:,None]*w))/FOUR_PI
    def ct_map(alpha):
        return (2*mg(alpha,R1[:,None]*wt+T1[:,None]*w)+
                cv(alpha,R2[:,None]*wt+T2[:,None]*w+
                   (R1*R1)[:,None]*ct+Th[:,None]*w))/FOUR_PI
    def j_map(alpha):
        return (mg(alpha,v[0])+cv(alpha,R1[:,None]*v[1]))/(2*math.pi)
    def de_map(alpha):
        return (2*db(alpha,z)+4*mg(alpha,R1[:,None]*z)+
                2*cv(alpha,(R2+3*R1*R1)[:,None]*z))/FOUR_PI
    # Frozen physical-potential caps. Pointwise log bounds give a tighter
    # positive-convolution cap; no actual error d0 is used here.
    Ustar = {gamma:float(cv(gamma,Sstar)) for gamma in multi_indices(3)
             if gamma != (0,0)}
    e = {gamma:cv(gamma,s) for gamma in multi_indices(3)
         if gamma != (0,0)}
    rows = {}
    def put(name,alpha,value):
        value = np.asarray(value,dtype=float)
        if np.any(value < 0):
            raise ArithmeticError('Positive coefficient map became negative')
        rows[f'{name}:{alpha[0]},{alpha[1]}'] = value
    for alpha in multi_indices(4):
        put('U',alpha,cv(alpha,s))
        put('W',alpha,cv(alpha,w))
    for alpha in multi_indices(3):
        put('J',alpha,j_map(alpha))
    for alpha in multi_indices(2):
        C = c_map(alpha)
        Ct = ct_map(alpha)
        T = db(alpha,st)/FOUR_PI+Ct
        N = np.zeros(3)
        for direction in ((1,0),(0,1)):
            for bx in range(alpha[0]+1):
                for by in range(alpha[1]+1):
                    beta = (bx,by)
                    other = (alpha[0]-bx,alpha[1]-by)
                    gamma,delta = _add(beta,direction),_add(other,direction)
                    binomial = math.comb(alpha[0],bx)*math.comb(alpha[1],by)
                    N += binomial*(e[gamma]*Ustar[delta]+Ustar[gamma]*e[delta])
        Q = 4*cv(alpha,v[0])+db(alpha,s)+cv(alpha,c0[:,None]*w)+N
        put('R',alpha,db(alpha,s)/FOUR_PI+C)
        put('C',alpha,C)
        put('Q',alpha,Q)
        put('Ut',alpha,cv(alpha,st))
        put('Wt',alpha,cv(alpha,wt))
        put('Ct',alpha,Ct)
        put('Rt',alpha,T)
        put('B',alpha,cv(alpha,b0[:,None]*w))
        put('source',alpha,T+j_map(_add(alpha,(1,0)))+
            j_map(_add(alpha,(0,1)))+de_map(alpha))
    rows['DeltaQ'] = rows['Q:2,0']+rows['Q:0,2']
    return dict(rows=rows,L=L,metadata=dict(scalar=bool(scalar),
        cap_bar0=float(bar0),cap_bar2=float(bar2),regulator_caps=caps,
        continuous_suprema_supplied=bool(scalar and supplied_reg and supplied_field),
        sampled_extrema=bool(scalar and not(supplied_reg and supplied_field)),
        positive_convolution_diagnostic=bool(not scalar),
        physical_potential_cap_max=float(np.max(Sstar)),
        Ustar={f'{i},{j}':val for (i,j),val in Ustar.items()},
        quadrature_order=int(kernel['order'])))


if __name__ == '__main__':
    # Implementation sanity only: fixed, constant local coefficients give
    # convergent positive kernel sums; scalar cap rows are nonnegative.
    kr = kernel_data(64)
    nn = kr['x'].size
    gg = np.ones((nn,4),dtype=complex)
    result = weak_coefficients(gg,2.,.1,.2,.3,.4,.5,.01,.01,kr)
    assert len(result['rows']) == 95
    assert abs(kernel_l1_1d(0)-1) < 1e-14
    assert all(np.all(np.isfinite(v)) and np.all(v >= 0)
               for v in result['rows'].values())
    print({'row_count':len(result['rows']), 'L1_1d':kr['l1_1d_x'],
           'sample_Q00':result['rows']['Q:0,0'].tolist()})
