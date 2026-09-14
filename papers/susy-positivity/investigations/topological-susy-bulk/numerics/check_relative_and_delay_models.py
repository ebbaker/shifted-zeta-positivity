#!/usr/bin/env python3
"""Relative-complex, primitive-return, and comparison-model diagnostics.

Python 3 + NumPy only. These floating-point checks are not sign certificates.
The analytic identities and their scopes are proved in ../manuscript.tex.
No target eigensystem, spectral square root, or zeta-zero data is used.
"""
from pathlib import Path
import argparse
import cmath
import json
import math
import platform
import numpy as np
from numpy.polynomial.legendre import leggauss


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def encode(z):
    return [float(np.real(z)), float(np.imag(z))]


def quad(fun, lo, hi, n):
    if hi <= lo:
        return 0j
    x, w = leggauss(n)
    xx = (hi-lo)*x/2 + (hi+lo)/2
    return (hi-lo)/2 * np.dot(w, fun(xx))


def bump(x, phase=0.0):
    # Smooth, complex, supported in [-0.8, 0.8], inside I_2.
    x = np.asarray(x)
    result = np.zeros_like(x, dtype=complex)
    inside = np.abs(x) < .8
    z = x[inside]/.8
    result[inside] = np.exp(-1/(1-z*z)) * (1+.3j*x[inside]) * np.exp(1j*phase*x[inside])
    return result


def channel_pairing(a, n):
    lo, hi = -.8, .8
    f = lambda x: bump(x, 1.7)
    g = lambda x: bump(x, -2.3)*(1-.4*x)
    def response(fun, x):
        left = quad(lambda y: np.exp(-a*(x-y))*fun(y), lo, x, n)
        right = quad(lambda y: np.exp(-a*(y-x))*fun(y), x, hi, n)
        return a*(left+right)/2, a*a*(-left+right)/2
    x, w = leggauss(n)
    x, w = (hi-lo)*x/2+(hi+lo)/2, (hi-lo)*w/2
    uf, df = np.array([response(f,t) for t in x]).T
    ug, dg = np.array([response(g,t) for t in x]).T
    c = 2/a
    spatial_inside = c*np.dot(w, np.conj(g(x)-ug)*(f(x)-uf)+np.conj(dg)*df/a**2)
    endpoints_f = [response(f,t)[0] for t in (lo,hi)]
    endpoints_g = [response(g,t)[0] for t in (lo,hi)]
    tails = c/a * np.vdot(endpoints_g,endpoints_f)
    # Since u=(a/2) exp(-a|.|)*f, the kernel is c delta-exp(-a|.|).
    kernel = c*np.dot(w, np.conj(g(x))*(f(x)-uf))
    error = abs(spatial_inside+tails-kernel)
    require(error < 2e-8, 'Full-line projected amplitude/kernel mismatch')
    require(abs(tails) > 1e-5, 'Omitted exterior-output control did not detect a loss')
    return dict(a=a, order=n, kernel_pairing=encode(kernel),
                amplitude_pairing=encode(spatial_inside+tails),
                exterior_pairing=encode(tails), absolute_error=float(error))


def finite_complex():
    # A periodic finite-difference control, not an interval approximation.
    rng = np.random.default_rng(9122026)
    n, a = 19, 1.3
    derivative = (np.roll(np.eye(n),1,axis=0)-np.roll(np.eye(n),-1,axis=0))/2
    D = np.vstack([np.eye(n), derivative/a])
    P = np.eye(2*n)-D@np.linalg.solve(D.T@D,D.T)
    f = rng.normal(size=n)+1j*rng.normal(size=n)
    source = np.r_[f,np.zeros(n)]
    harmonic = P@source
    q = np.zeros((3*n,3*n))
    q[n:,:n] = D
    H = q@q.T+q.T@q
    h = np.r_[np.zeros(n),harmonic]
    gauge = rng.normal(size=n)
    # Reparametrizing the auxiliary domain leaves the actual range fixed.
    R = np.diag(np.linspace(.5,1.7,n))
    DR = D@R
    PR = np.eye(2*n)-DR@np.linalg.solve(DR.T@DR,DR.T)
    errors = dict(nilpotence=np.linalg.norm(q@q), harmonic=np.linalg.norm(H@h),
                  gauge=np.linalg.norm(P@(source+D@gauge)-harmonic),
                  reparametrization=np.linalg.norm(PR-P))
    require(max(errors.values()) < 1e-12, 'Hilbert complex identities')
    require(np.linalg.norm(harmonic)>0.1, 'Boundary class incorrectly killed')
    exact = np.r_[np.zeros(n), D@f]
    require(np.linalg.norm(np.r_[np.zeros(n),P@(D@f)])<1e-12, 'Exact-state control')
    # Pairing of unprojected source with heat evolution is NOT protected.
    vals, vecs = np.linalg.eigh(H)
    raw = np.r_[np.zeros(n),source]
    heat = lambda t: float(np.sum(np.exp(-t*vals)*np.abs(vecs.T@raw)**2).real)
    return dict(errors={k:float(v) for k,v in errors.items()},
                harmonic_norm_squared=float(np.vdot(h,h).real),
                raw_heat_pairings=[heat(t) for t in [0,1,4]],
                exact_state_norm_squared=float(np.vdot(exact,exact).real))


def shift(n,d):
    T = np.zeros((n,n))
    if d<n:
        T[d:,:n-d] = np.eye(n-d)
    return T


def delay_identities():
    # Integer delays test exact compression algebra, not log(2)/log(3) fitting.
    n,d,e,r = 29,7,11,1/math.sqrt(2)
    T, U = shift(n,d), shift(n,e)
    I = np.eye(n)
    W = np.linalg.solve(I-r*T,I)
    Pi = I-T.T@T
    Y = np.vstack([math.sqrt(1-r*r)*W, r*Pi@W])
    poisson = W+W.T-I
    series = I.copy()
    power = I.copy()
    for k in range(1, math.ceil(n/d)):
        power = power@T
        series += r**k*(power+power.T)
    S = (r*I-T)@W
    defect = (1-r*r)*W.T@Pi@W
    wrong = (1-r*r)*W.T@W
    errors = dict(poisson=np.linalg.norm(Y.T@Y-poisson), series=np.linalg.norm(series-poisson),
                  defect=np.linalg.norm(I-S.T@S-defect),
                  semigroup=np.linalg.norm(T@U-shift(n,d+e)),
                  mixed_cap=np.linalg.norm(T.T@U-(T.T@T)@shift(n,e-d)))
    require(max(errors.values())<2e-13,'Delay algebra')
    missing = np.linalg.norm(wrong-poisson)
    require(missing>.1,'Endpoint omission control')
    alpha,beta = .4,.3
    A = I-alpha*T-beta*U
    corrected = I+alpha**2*T.T@T+beta**2*U.T@U-alpha*(T+T.T)-beta*(U+U.T)
    mixed = alpha*beta*(T.T@U+U.T@T)
    require(np.linalg.norm(A.T@A-corrected-mixed)<1e-13,'Two-label expansion')
    prime = -(T+T.T)
    eigen = np.linalg.eigvalsh(prime)
    require(eigen[0]<-.1 and eigen[-1]>.1,'Both signs of isolated prime')
    return dict(errors={k:float(v) for k,v in errors.items()},
                omitted_endpoint_error=float(missing), mixed_delay_norm=float(np.linalg.norm(mixed)),
                prime_extreme_eigenvalues=[float(eigen[0]),float(eigen[-1])],
                nilpotent_determinant=float(np.linalg.det(I-r*T)))


def genuine_log_delay_pairing(L, p, n):
    # Continuum calculation with log(p), splitting all changes in support.
    a,r = math.log(p),p**-.5
    # A polynomial in D_log,L; endpoint jumps allowed for this diagnostic.
    def f(x):
        x=np.asarray(x)
        return np.where((x>0)&(x<L),(1+.2j*x)*(1+.3*x),0j)
    kmax = math.ceil(L/a)-1
    def w(x):
        return sum(r**k*f(x-k*a) for k in range(kmax+1))
    breaks = sorted(set([0.,L,max(0.,L-a)] + [k*a for k in range(1,kmax+1)]))
    norm = quad(lambda x: np.abs(f(x))**2,0,L,n).real
    ynorm = 0.
    for l,h in zip(breaks[:-1],breaks[1:]):
        # Pi is the right endpoint reservoir (L-a,L), or all I if a>=L.
        fac = 1. if (l+h)/2 > max(0,L-a) else 1-r*r
        ynorm += fac*quad(lambda x: np.abs(w(x))**2,l,h,n).real
    qprime = sum(-2*a*r**k*quad(lambda x: np.conj(f(x))*f(x-k*a),k*a,L,n).real
                 for k in range(1,kmax+1))
    error=abs(a*(norm-ynorm)-qprime)
    require(error<1e-12,'True logarithmic-delay pairing')
    return dict(L=L,prime=p,active_powers=kmax,positive_loop_norm=float(ynorm),
                input_norm=float(norm),prime_form=float(qprime),error=float(error))


def connected_loops():
    p,q,z = 2,3,.4+.7j
    a,b = math.log(p),math.log(q)
    x,y = cmath.exp(-a*(.5+z)),cmath.exp(-b*(.5+z))
    exact = -a*x/(1-x)-b*y/(1-y)
    truncated = -sum(a*x**k+b*y**k for k in range(1,80))
    # Mixed xy coefficient in log(1-x-y) is -1; in log((1-x)(1-y)) is zero.
    require(abs(exact-truncated)<1e-14,'Euler logarithmic derivative')
    return dict(generator=encode(exact),series_error=abs(exact-truncated),
                product_log_xy_coefficient=0,shared_loop_log_xy_coefficient=-1,
                unwanted_sum_label=math.log(6),unwanted_difference_label=math.log(3/2))


def dirac_and_rotation():
    a=1.3
    rows=[]
    X=np.array([[0.,1.],[-1.,0.]])
    for t in [2.,10.,50.,250.]:
        # Hermitian tangential Dirac symbol; eigenvalues +/-sqrt(a^2+t^2).
        M=np.array([[a,t],[t,-a]])
        rho=math.hypot(a,t)
        minus=(np.eye(2)-M/rho)/2
        prescribed=np.array([1.,0.])
        rejected=float(np.linalg.norm(minus@prescribed)**2)
        d=np.array([1.,1j*t/a])
        P=np.eye(2)-np.outer(d,d.conj())/np.vdot(d,d)
        raw=np.array([1.,0.])
        # A skew-Hermitian phase rotation with nontrivial derivative.
        XX=1j*np.array([[0.,1.],[1.,0.]])
        derivative=(2/a)*np.vdot(raw,(XX@P-P@XX)@raw).real
        bound=(4/a)*np.linalg.norm(P@raw)*np.linalg.norm((np.eye(2)-P)@raw)
        require(abs(derivative)<=bound+1e-13,'Projection variation bound')
        rows.append(dict(frequency=t,negative_trace_fraction=rejected,
                         rotation_derivative=float(derivative),rotation_bound=float(bound)))
    # Endpoint Robin witness and its positive transparent-boundary control.
    L=1.
    integral=a*(math.exp(2*a*L)-1)
    endpoint=a*(1+math.exp(2*a*L))
    require(abs((integral-endpoint)+2*a)<1e-12,'Growing Green Robin witness')
    return dict(symbol_tests=rows,wrong_robin_energy=integral-endpoint,
                transparent_robin_energy=integral+endpoint)


def coherent_deformation():
    count=20000
    masses=2*np.arange(count)+.5
    first_missing=2*count+.5
    a,b=math.log(2),math.log(3)
    bp,bq=2*a/math.sqrt(2),2*b/math.sqrt(3)
    def B(s):
        return np.sum((2/masses)*s/(masses*masses+s))
    def rh(t):
        j=np.exp(-t/2)/(-np.expm1(-2*t))
        logder=-.5-2/np.expm1(2*t)
        return j*(1+t*logder)
    def mixed_kernel(t):
        q=np.exp(-2*t)
        den=-np.expm1(-2*t)
        j=np.exp(-t/2)/den
        ld=-.5-2*q/den
        ldd=4*q/(den*den)
        return -.25*j*(1+3*t*ld+t*t*(ld*ld+ldd))
    rows=[]
    for tau in [0.,2.,10.,20.,50.,250.]:
        s=tau*tau
        prime=np.sum(2*masses/(masses*masses+s)**2)
        second=np.sum(-4*masses/(masses*masses+s)**3)
        h=2*s*prime
        eps=1e-5
        m=lambda eta:1-eta*bp*cmath.exp(-1j*a*tau)
        fd=(B(s*abs(m(eps))**2)-B(s*abs(m(-eps))**2))/(2*eps)
        exact=-bp*h*math.cos(a*tau)
        require(abs(fd-exact)<2e-8,'Deformation first variation')
        row=dict(frequency=tau,h_partial=float(h),
                 h_tail_upper_bound=4*s*(first_missing**-3+1/(4*first_missing**2)),
                 first_variation_error=abs(fd-exact),
                 product_mixed_partial=float(4*bp*bq*math.cos(a*tau)*math.cos(b*tau)*(s*prime+s*s*second)))
        ep=1e-4
        product=lambda u,v:(1-u*bp*cmath.exp(-1j*a*tau))*(1-v*bq*cmath.exp(-1j*b*tau))
        cross=sum(i*j*B(s*abs(product(i*ep,j*ep))**2) for i in [-1,1] for j in [-1,1])/(4*ep*ep)
        row['product_mixed_difference_error']=abs(cross-row['product_mixed_partial'])
        require(row['product_mixed_difference_error']<2e-6,'Product mixed derivative')
        if tau<=20:
            # Tail beyond 80 has size O(80 exp(-40)); split oscillatory integral.
            khat=sum(quad(lambda t:-2*rh(t)*np.cos(tau*t),l,u,256).real
                     for l,u in zip([0.,1.,3.,10.,30.],[1.,3.,10.,30.,80.]))
            err=abs(khat-(1-h))
            require(err<row['h_tail_upper_bound']+2e-9,'Residual Fourier/contact identity')
            row.update(residual_fourier=float(khat),residual_error=float(err))
            vhat=sum(quad(lambda t:2*mixed_kernel(t)*np.cos(tau*t),l,u,256).real
                     for l,u in zip([0.,1.,3.,10.,30.],[1.,3.,10.,30.,80.]))
            verr=abs(vhat-(s*prime+s*s*second))
            require(verr<row['h_tail_upper_bound']/2+2e-9,'Mixed residual Fourier identity')
            row.update(mixed_residual_fourier=float(vhat),mixed_residual_error=float(verr))
        rows.append(row)
    return dict(mass_terms=count,tests=rows,
                note='Finite differences use the same truncated tower; residual Fourier checks include an analytic mass-tail bound.')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    result=dict(status='floating-point identity diagnostics, not positivity proof',
                python=platform.python_version(),numpy=np.__version__,
                channel=[channel_pairing(a,n) for a in [.5,2.5] for n in [64,128]],
                complex=finite_complex(),delays=delay_identities(),
                logarithmic_delays=[genuine_log_delay_pairing(L,p,40)
                    for L,p in [(1.,2),(1.25,2),(1.25,3),(2.3,2),(2.3,3),(.5,2)]],
                connected=connected_loops(),dirac=dirac_and_rotation(),
                deformation=coherent_deformation())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
