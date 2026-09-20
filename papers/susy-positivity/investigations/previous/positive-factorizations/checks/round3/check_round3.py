"""Round 3: odd-sector factor and first-prime stabilization.

Exact Fraction interval bounds certify the signs; NumPy quadratures are
separate identity diagnostics. No zero data or fitted matrix is a proof input.
Run from any directory. Python 3 + NumPy. See INVESTIGATION_round3.md.
"""
from __future__ import annotations

from fractions import Fraction as F
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np
from numpy.polynomial.legendre import leggauss

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('round2', ROOT/'checks/round2/check_round2.py')
r2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r2)
I, exp_point = r2.Interval, r2.exp_point


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def power(x, n):
    ans = I(1)
    for _ in range(n):
        ans *= x
    return ans


def log_point(x):
    """Range reduction keeps the atanh series argument at most 1/3."""
    x = F(x)
    require(x > 0, 'Positive logarithm argument required')
    k = 0
    while x < 1:
        x *= 2
        k -= 1
    while x > 2:
        x /= 2
        k += 1
    return r2.log_point(x) + k*r2.log_point(2)


def log_interval(x):
    x = I.cast(x)
    return I(log_point(x.lo).lo, log_point(x.hi).hi)


def constants():
    ln2 = log_point(2)
    pi = 16*r2.atan_point(F(1, 5))-4*r2.atan_point(F(1, 239))
    harmonic = sum((F(1, k) for k in range(1, 129)), F(0))
    gamma = I(harmonic-7*ln2.hi-F(1, 128), harmonic-7*ln2.lo)
    w0 = -gamma-pi/2-3*ln2-log_interval(pi)
    return ln2, pi, gamma, w0


def odd_certificate():
    _, pi, gamma, _ = constants()
    L, ell = F(7, 10), F(7, 20)
    D = F(31, 480)  # Proved Lipschitz bound for r(t)=j(t)-1/(2t).
    cosh = (exp_point(ell/2)+exp_point(-ell/2))/2
    require(power(cosh, 2).hi < F(33, 32), 'Cosh bound')
    constant = -gamma-log_interval(pi*L)
    pole = F(13, 75)*ell**3*F(33, 32)

    def rational_part(u):
        numerator = (F(7, 5)-F(22, 15)*u
                     -2*D*ell**2*(F(3, 10)-u/6+power(u, 2)/25)-pole)
        return numerator/(1-F(4, 5)*u)

    # Covers [0, 99/100] with rational intervals, not point sampling.
    mesh = 2000
    best = None
    best_cell = None
    for k in range(1980):
        u = I(F(k, mesh), F(k+1, mesh))
        value = constant-log_interval(1-u)/2+rational_part(u)
        require(value.lo > F(1, 100), f'Odd potential cell {k}')
        if best is None or value.lo < best:
            best, best_cell = value.lo, k
    # On [99/100,1), use -log(1-u) >= log(100); no endpoint evaluation.
    tail = constant+log_point(100)/2+rational_part(I(F(99, 100), 1))
    require(tail.lo > F(1, 100), 'Odd potential endpoint tail')
    return dict(status='exact rational interval certificate',
                total_length_upper='7/10', proven_floor='1/100',
                mesh_denominator=mesh, covered_cells=1980,
                smallest_cell_lower=float(best), smallest_cell=best_cell,
                endpoint_tail_lower=float(tail.lo),
                regular_kernel_lipschitz_bound='31/480',
                cosh_squared_upper='33/32',
                scope='Odd gamma sector only; all 0<L<=7/10, central shift.')


def prime_certificate():
    ln2, _, _, w0 = constants()
    L, N = F(1), 64
    a = lambda k: F(4*k+1, 2)
    kinetic = I(0)
    for k in range(N):
        m = a(k)
        kinetic += (6/(L*m*m)-24/(L**3*m**4)
                    +exp_point(-m*L)*(6/(L*m*m)+24/(L*L*m**3)+24/(L**3*m**4)))
    m = a(N)
    s2 = I(1/(2*m), 1/(2*m)+1/(m*m))
    s4 = I(1/(6*m**3), 1/(6*m**3)+1/m**4)
    etail = (exp_point(-m*L)/(1-exp_point(-2*L))
             *(6/(L*m*m)+24/(L*L*m**3)+24/(L**3*m**4)))
    kinetic += 6/L*s2-24/(L**3)*s4+I(0, etail.hi)
    cosh = (exp_point(L/4)+exp_point(-L/4))/2
    sinh = (exp_point(L/4)-exp_point(-L/4))/2
    qgamma = w0+kinetic-24/(L**3)*power(2*L*cosh-8*sinh, 2)
    exp_mhalf_a = I(exp_point(-ln2.hi/2).lo, exp_point(-ln2.lo/2).hi)
    c = ln2*exp_mhalf_a
    corr = 1-3*ln2/L+2*power(ln2/L, 3)
    prime = -2*c*corr
    debit = c*(1-power(2*ln2/L-1, 3))
    total, remainder = qgamma+prime, qgamma-debit
    require(qgamma.hi < F(-12, 100), 'Gamma linear input must be negative')
    require(total.lo > F(26, 100), 'Prime must stabilize this input')
    require(remainder.hi < F(-58, 100), 'Independent-edge remainder must fail')
    return dict(status='exact rational interval certificate', total_length='1',
                input='sqrt(12)*x on (-1/2,1/2), unit L2 norm',
                mass_terms=N, gamma=qgamma.display(), first_prime=prime.display(),
                full_form=total.display(), forced_diagonal=debit.display(),
                edge_remainder=remainder.display(),
                assertions=['gamma < -0.12', 'full form on this input > 0.26',
                            'edge remainder < -0.58'],
                scope='Signs on this explicit input; not an all-input positivity certificate.')


W0 = -.5772156649015328606-math.pi/2-3*math.log(2)-math.log(math.pi)


def tail(t):
    r = np.exp(-t/2)
    return np.arctanh(r)+np.arctan(r)


def jump(t):
    return np.exp(-t/2)/(-np.expm1(-2*t))


def kernel(t):
    return 2*np.cosh(t/2)-jump(t)


def odd_identity(L, n):
    ell = L/2
    z, w = leggauss(n)
    x = ell*(z+1)/2
    wx = ell*w/2
    b = 4/(5*ell**2)
    phi = lambda x: x*(1-b*x*x)
    # A complex odd polynomial; f=phi*h with an even polynomial h.
    h = lambda x: 1+.3j*(x/ell)**2+.2*(x/ell)**4
    f = lambda x: phi(x)*h(x)
    norm = 2*np.dot(wx, abs(f(x))**2)
    S = 2*np.dot(wx, f(x)*np.sinh(x/2))
    v, wv = leggauss(16)
    t = L*(z+1)/2
    wt = L*w/2
    xx = -t[:, None]/2+(L-t[:, None])*v/2
    corr = (L-t)/2*((np.conj(f(xx+t[:, None]))*f(xx))@wv)
    target = W0*norm+np.dot(wt, 2*jump(t)*(norm-corr.real))
    target += 2*tail(L)*norm-2*abs(S)**2

    # Independent pointwise action on the fixed cubic, by split jump integrals.
    derivative_term = np.zeros_like(x)
    for sign, length in [(1, ell+x), (-1, ell-x)]:
        t = length[:, None]*(z+1)/2
        tj = t*jump(t)
        poly = 1-b*(3*x[:, None]**2-3*sign*x[:, None]*t+t*t)
        derivative_term += sign*length/2*((tj*poly)@w)
    Sphi = 2*np.dot(wx, phi(x)*np.sinh(x/2))
    potential = (W0+tail(ell+x)+tail(ell-x)
                 +derivative_term/phi(x)-2*Sphi*np.sinh(x/2)/phi(x))
    # Remove the sole endpoint logarithm before Gaussian quadrature. Its
    # polynomial moment is evaluated explicitly, not by a denser grid.
    from numpy.polynomial.polynomial import polymul
    coeff = polymul([0, 0, 1], polymul(polymul([1, 0, -.8], [1, 0, -.8]),
                                      [1, 0, 0, 0, .49, 0, 0, 0, .04]))
    log_moment = ell**3*sum(ck*(math.log(ell)-sum(1/j for j in range(1, k+2)))/(k+1)
                               for k, ck in enumerate(coeff))
    pot_energy = np.dot(wx, (2*potential+np.log(ell-x))*abs(f(x))**2)-log_moment
    # Triangle in (x,y) on (0,ell); g=sqrt(2) f. Duffy quadrature resolves
    # the logarithmic corner at x=y=ell in the potential separately above.
    d = ell*(z+1)/2
    wd = ell*w/2
    y = (ell-d[:, None])*(z+1)/2
    wy = (ell-d[:, None])*w/2
    xx = y+d[:, None]
    conductance = kernel(xx+y)-kernel(d[:, None])
    edge_integrand = conductance*phi(xx)*phi(y)*2*abs(h(xx)-h(y))**2
    edge = np.dot(wd, np.sum(wy*edge_integrand, axis=1))
    return dict(L=L, nodes=n, target=float(target), factor=float(edge+pot_energy),
                absolute_difference=float(abs(target-edge-pot_energy)),
                input_norm_squared=float(norm),
                sampled_potential_min=float(potential.min()),
                all_sampled_folded_conductances_positive=bool(np.all(conductance>0)))


def parity_prime_control():
    # Compare the original full translation to the folded cap reflection.
    # Both parities, complex inputs, and both reflection eigenspaces.
    rng = np.random.default_rng(941)
    cap_dim = 7
    half_dim, delay = 10, 13
    T = np.zeros((2*half_dim, 2*half_dim))
    for k in range(2*half_dim-delay):
        T[k+delay, k] = 1
    J = np.eye(cap_dim)[::-1]
    Eplus = (np.eye(cap_dim)+J)/2
    Eminus = (np.eye(cap_dim)-J)/2
    c = math.log(2)/math.sqrt(2)
    errors = []
    for eps in [-1, 1]:
        half = rng.normal(size=half_dim)+1j*rng.normal(size=half_dim)
        full = np.concatenate([eps*half[::-1], half])/math.sqrt(2)
        g = half[-cap_dim:]
        lhs = -c*np.vdot(full, (T+T.T)@full)
        errors.append(float(abs(lhs+eps*c*np.vdot(g, J@g))))
        rhs = -eps*c*(np.linalg.norm(Eplus@g)**2-np.linalg.norm(Eminus@g)**2)
        errors.append(float(abs(lhs-rhs)))
    require(max(errors)<1e-13, 'Parity-prime identity')
    # An odd-sector prime correction is not positive on all inputs.
    minus = np.array([1., 0, 0, 0, 0, 0, -1.])/math.sqrt(2)
    plus = np.ones(cap_dim)/math.sqrt(cap_dim)
    require(np.vdot(minus, c*J@minus)<0, 'Negative prime control')
    require(np.vdot(plus, c*J@plus)>0, 'Positive prime control')
    return dict(max_error=max(errors), odd_cap_symmetric_energy=float(c),
                odd_cap_antisymmetric_energy=float(-c))


def main():
    if not __debug__:
        raise RuntimeError('Do not run certificate dependencies with Python -O.')
    out = dict(python=platform.python_version(), numpy=np.__version__,
               odd_factor=odd_certificate(), first_prime=prime_certificate())
    if '--certificate-only' not in sys.argv:
        out['odd_identity_diagnostics'] = [odd_identity(L, n)
            for L in [.25, math.log(2), .7] for n in [128, 256]]
        # Identity checks do not prove the sign; rational bounds above do.
        for low, high in zip(out['odd_identity_diagnostics'][::2], out['odd_identity_diagnostics'][1::2]):
            require(high['absolute_difference'] < 2e-10, 'Folded identity quadrature')
            require(low['absolute_difference'] < 2e-10, 'Second quadrature order')
        out['parity_prime_control'] = parity_prime_control()
    dest = Path(__file__).with_name('diagnostics.json')
    if '--certificate-only' not in sys.argv:
        dest.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
