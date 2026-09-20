"""Round 2: exact rational sign bound plus floating-point structural checks.

The sign bound uses Fraction arithmetic and elementary series with explicit tails.
The other checks use NumPy and are diagnostics, not interval certificates.
No zeta zeros or external data are inputs.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import cmath
import json
import math
import platform
import numpy as np
from numpy.polynomial.legendre import leggauss


class Interval:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def cast(x):
        return x if isinstance(x, Interval) else Interval(x)

    def __add__(self, x):
        x = self.cast(x)
        return Interval(self.lo+x.lo, self.hi+x.hi)
    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, x):
        return self + (-self.cast(x))

    def __rsub__(self, x):
        return self.cast(x) + (-self)

    def __mul__(self, x):
        x = self.cast(x)
        vals = [a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return Interval(min(vals), max(vals))
    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.cast(x)
        assert not x.lo <= 0 <= x.hi
        return self * Interval(1/x.hi, 1/x.lo)

    def __rtruediv__(self, x):
        return self.cast(x) / self

    def display(self):
        return [float(self.lo), float(self.hi)]


def exp_point(x, n=160):
    x = F(x)
    if x < 0:
        return 1 / exp_point(-x, n)
    assert x < n+2
    term = F(1)
    total = term
    for k in range(1,n+1):
        term *= x/k
        total += term
    first_missing = term*x/(n+1)
    remainder = first_missing/(1-x/(n+2))
    return Interval(total, total+remainder)


def log_point(x, n=48):
    x = F(x)
    assert x > 0
    if x < 1:
        return -log_point(1/x, n)
    z = (x-1)/(x+1)
    total = sum((2*z**(2*k+1)/F(2*k+1) for k in range(n)), F(0))
    remainder = 2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return Interval(total,total+remainder)


def atan_point(x, n=24):
    x = F(x)
    assert 0 <= x < 1
    s = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)), F(0))
    next_term = (-1)**n*x**(2*n+1)/F(2*n+1)
    return Interval(min(s,s+next_term),max(s,s+next_term))


def rational_pair_obstruction():
    # Euler's constant obeys H_m-log(m)-1/m < gamma < H_m-log(m).
    # Machin's formula and alternating arctangent series enclose pi.
    ln2 = log_point(2)
    pi = 16*atan_point(F(1,5))-4*atan_point(F(1,239))
    lnpi = Interval(log_point(pi.lo).lo,log_point(pi.hi).hi)
    m = 128
    harmonic = sum((F(1,k) for k in range(1,m+1)),F(0))
    gamma = Interval(harmonic-7*ln2.hi-F(1,m),harmonic-7*ln2.lo)
    w0 = -gamma-pi/2-3*ln2-lnpi
    L,b,N = F(2,3),F(1,3),32
    a = lambda k: F(4*k+1,2)
    series = sum(((1-exp_point(-a(k)*L))/(a(k)**2) for k in range(N)),Interval(0))
    # Integral bounds for the decreasing inverse-square tail; geometric bound
    # for its exponentially damped part.
    inverse_tail_integral = 1/(2*a(N))
    exponential_tail = exp_point(-a(N)*L)/(a(N)**2*(1-exp_point(-2*L)))
    series += Interval(inverse_tail_integral-exponential_tail.hi,
                       inverse_tail_integral+1/a(N)**2)
    sh = (exp_point(L/4)-exp_point(-L/4))/2
    qgamma = w0+2/L*series+32/L*sh*sh

    def J(lam):
        return (exp_point(-lam*b)*(lam*(L-b)-1)+exp_point(-lam*L))/(lam*lam)

    r_integral = J(F(-1,2))-sum((J(a(k)) for k in range(1,N)),Interval(0))
    omitted = (L-b)*exp_point(-a(N)*b)/(a(N)*(1-exp_point(-2*b)))
    r_integral += Interval(-omitted.hi,0)
    partial_comparison = qgamma-4/L*r_integral
    assert partial_comparison.hi < F(-1,25), 'Exact rational assertion failed'
    return dict(status='proved by rational arithmetic and explicit series tails',
                L=str(L), cutoff_b=str(b), number_of_mass_terms=N,
                exp_polynomial_degree=160, log_terms=48, atan_terms=24,
                gamma_constant_interval=qgamma.display(),
                partial_comparison_interval=partial_comparison.display(),
                exact_assertion='upper endpoint < -1/25',
                full_comparison_leq_partial=True,
                approximation_note='Displayed decimal endpoints are for reading; the assertion uses exact fractions.')


def digamma(z):
    correction = 0j
    while z.real < 32:
        correction -= 1/z
        z += 1
    ans = cmath.log(z)-1/(2*z)
    for k,b in enumerate([1/6,-1/30,1/42,-1/30,5/66,-691/2730],1):
        ans -= b/(2*k*z**(2*k))
    return ans+correction


def tower_checks():
    rows = []
    N = 20000
    masses = 2*np.arange(N,dtype=float)+.5
    for tau in [0.,.5,1.,3.,10.,100.]:
        terms = 2*tau*tau/(masses*(masses*masses+tau*tau))
        approx = float(terms.sum())
        direct = digamma(.25+.5j*tau).real-digamma(.25).real
        # Each term <= 2*tau^2/a_k^3; decreasing-series integral bound.
        first_missing_mass = 2*N+.5
        upper_tail = 2*tau*tau*(first_missing_mass**-3+
                                 1/(4*first_missing_mass**2))
        assert -1e-11 <= direct-approx <= upper_tail+1e-11
        rows.append(dict(tau=tau, kinetic_multiplier=direct, tower_partial_sum=approx,
                         deficit=direct-approx, analytic_tail_upper_bound=upper_tail))
    rng = np.random.default_rng(20260911)
    max_schur_error = 0.
    max_stationary_error = 0.
    min_bulk_eigenvalue = math.inf
    for a in [.5,2.5,6.5]:
        for tau in [0.,.3,2.,10.]:
            A = math.sqrt(2/a)*np.array([[1,-1],[0,1j*tau/a]],dtype=complex)
            H = A.conj().T@A
            schur = H[0,0]-H[0,1]*H[1,0]/H[1,1]
            expected = 2*tau*tau/(a*(a*a+tau*tau))
            max_schur_error=max(max_schur_error,float(abs(schur-expected)))
            f = rng.normal()+1j*rng.normal()
            u = a*a/(a*a+tau*tau)*f
            gap = float(np.vdot(A@np.array([f,u]),A@np.array([f,u])).real-expected*abs(f)**2)
            max_stationary_error=max(max_stationary_error,abs(gap))
            min_bulk_eigenvalue=min(min_bulk_eigenvalue,float(np.linalg.eigvalsh(H).min()))
    assert max_schur_error<2e-14 and max_stationary_error<2e-13
    return dict(modes=N, multiplier_checks=rows,
                max_single_channel_schur_error=max_schur_error,
                max_minimum_energy_error=max_stationary_error,
                minimum_sampled_bulk_eigenvalue=min_bulk_eigenvalue)


def comparison(M):
    out=-np.abs(M)
    np.fill_diagonal(out,np.diag(M).real)
    return out


def bulk_checks():
    # A coherent row involves f1,f2,u. It is not a two-endpoint spring.
    A=np.array([[1.,1.,0.,-1.],[0.,0.,1.,1.]])
    H=A.T@A
    boundary=H[:3,:3]-np.outer(H[:3,3],H[3,:3])/H[3,3]
    assert np.max(abs(boundary-.5*np.ones((3,3))))<1e-14
    q=np.zeros((6,6));q[4:,:4]=A
    susy_H=q.T@q+q@q.T
    assert np.max(abs(q@q))==0
    assert np.linalg.eigvalsh(susy_H).min()>-1e-13

    # Diagnostic for the proved finite-network comparison closure under Schur.
    rng=np.random.default_rng(74291)
    network_rows=[]
    for i in range(7):
        for j in range(i+1,7):
            row=np.zeros(7,dtype=complex)
            row[i]=.5+rng.random()
            row[j]=(.5+rng.random())*np.exp(1j*rng.uniform(-math.pi,math.pi))
            network_rows.append(row)
    B=np.vstack(network_rows)
    G=B.conj().T@B+.3*np.eye(7)
    schur=G[:3,:3]-G[:3,3:]@np.linalg.solve(G[3:,3:],G[3:,:3])
    assert np.linalg.eigvalsh(comparison(G)).min()>0
    assert np.linalg.eigvalsh(comparison(schur)).min()>0

    # First-prime correction has both signs, whereas any fixed-boundary-block
    # auxiliary elimination subtracts a positive semidefinite matrix.
    c=math.log(2)/math.sqrt(2)
    prime=np.array([[0.,-c],[-c,0.]])
    return dict(coherent_bulk_rows=A.tolist(), boundary_schur=boundary.tolist(),
                boundary_eigenvalues=np.linalg.eigvalsh(boundary).tolist(),
                boundary_comparison_eigenvalues=np.linalg.eigvalsh(comparison(boundary)).tolist(),
                nilpotence_error=float(np.max(abs(q@q))),
                superhamiltonian_min_eigenvalue=float(np.linalg.eigvalsh(susy_H).min()),
                magnetic_network_comparison_min_eigenvalue=float(np.linalg.eigvalsh(comparison(G)).min()),
                reduced_network_comparison_min_eigenvalue=float(np.linalg.eigvalsh(comparison(schur)).min()),
                first_prime_eigenvalues=np.linalg.eigvalsh(prime).tolist())


def gamma_comparison_diagnostic(L,n):
    x,w=leggauss(n)
    t=(x+1)*L/2;wt=w*L/2
    j=lambda t: np.exp(-t/2)/(-np.expm1(-2*t))
    r=lambda t:2*np.cosh(t/2)-j(t)
    e=math.exp(-L/2)
    tail=math.atanh(e)+math.atan(e)
    w0=-.5772156649015328606-math.pi/2-3*math.log(2)-math.log(math.pi)
    q=w0+2/L*np.dot(wt,t*j(t))+2*tail+32/L*math.sinh(L/4)**2
    t0=.28119957432296183
    t=(t0+L)/2+(L-t0)*x/2;wt=(L-t0)*w/2
    cmp=q-4/L*np.dot(wt,(L-t)*r(t))
    b=1/3
    t=(b+L)/2+(L-b)*x/2;wt=(L-b)*w/2
    partial=q-4/L*np.dot(wt,(L-t)*r(t))
    return dict(L=L,nodes=n,gamma_constant=float(q),comparison_constant=float(cmp),
                partial_comparison_constant=float(partial))


def main():
    certificate=rational_pair_obstruction()
    diagnostics=[gamma_comparison_diagnostic(L,n) for L in [2/3,math.log(2)] for n in [64,128]]
    for row in diagnostics:
        if row['L']==2/3:
            lo,hi=certificate['partial_comparison_interval']
            assert lo<row['partial_comparison_constant']<hi
    out=dict(python=platform.python_version(),numpy=np.__version__,
             rational_pair_obstruction=certificate,tower=tower_checks(),
             coherent_and_pairwise_bulk=bulk_checks(),gamma_diagnostics=diagnostics,
             robin_identity='For u(x)=exp(a*x), E_R[u]=-2*a; exact for every a,L>0.')
    Path(__file__).with_name('diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
