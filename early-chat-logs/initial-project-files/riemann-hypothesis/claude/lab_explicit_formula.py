"""Explicit-formula bridge.

Guinand-Weil explicit formula in rotated coordinates (zeros of Xi at z = gamma,
rho = 1/2 + i*gamma, multiset closed under gamma -> -gamma and gamma -> conj):

    sum_gamma h(gamma) = h(i/2) + h(-i/2)
                       + (1/2pi) int h(t) [Re psi(1/4 + it/2) - log pi] dt
                       - 2 sum_{n>=2} Lambda(n)/sqrt(n) * g(log n),

for h even, holomorphic in |Im| <= 1/2+eps, decaying; g(u) = (1/2pi) int h(r) e^{-iur} dr.

Test family (analytic, Gaussian-localized at center c, frequency lambda):
    h(r) = e^{i lam (r-c)} G(r-c) + e^{-i lam (r+c)} G(r+c),   G(v)=exp(-v^2/(2 sigma^2))
    g(u) = (sigma/sqrt(2pi)) [ e^{-iuc} e^{-sigma^2 (u-lam)^2/2} + e^{+iuc} e^{-sigma^2 (u+lam)^2/2} ]
Then Z(c,lam) := sum_gamma h(gamma) is the linear building block; the bridge
quadratic form is  Q(c) = int |Z(c,lam)|^2 w(lam) dlam.
"""
import numpy as np, mpmath as mp, pickle, os

mp.mp.dps = 30

# ---------------- zeros (cached) ----------------
def zeta_zeros(K, cache='zeros.pkl'):
    if os.path.exists(cache):
        zs = pickle.load(open(cache, 'rb'))
        if len(zs) >= K:
            return zs[:K]
    zs = [float(mp.im(mp.zetazero(k))) for k in range(1, K + 1)]
    pickle.dump(zs, open(cache, 'wb'))
    return zs

# ---------------- von Mangoldt ----------------
def mangoldt_upto(N):
    lam = np.zeros(N + 1)
    sieve = np.ones(N + 1, bool); sieve[:2] = False
    for p in range(2, N + 1):
        if sieve[p]:
            sieve[2*p::p] = False
            pk = p
            while pk <= N:
                lam[pk] = np.log(p)
                pk *= p
    return lam

# ---------------- test family ----------------
def h_val(r, c, lam, sig):
    r = np.asarray(r, dtype=complex)
    return (np.exp(1j*lam*(r - c) - (r - c)**2/(2*sig**2))
          + np.exp(-1j*lam*(r + c) - (r + c)**2/(2*sig**2)))

def g_val(u, c, lam, sig):
    u = np.asarray(u, dtype=float)
    pref = sig/np.sqrt(2*np.pi)
    return pref*(np.exp(-1j*u*c - sig**2*(u - lam)**2/2)
               + np.exp(+1j*u*c - sig**2*(u + lam)**2/2))

# ---------------- three sides of the EF ----------------
def zero_side(zeros_ay, c, lam, sig):
    """zeros_ay: list of (a,y): a>0 real part, y>=0. Each (a,0) means the pair
    {a,-a}; each (a,y>0) means the quadruple {±a±iy}. Sum h over the multiset."""
    tot = 0 + 0j
    for (a, y) in zeros_ay:
        if y == 0.0:
            tot += h_val(a, c, lam, sig) + h_val(-a, c, lam, sig)
        else:
            for g_ in (a + 1j*y, a - 1j*y, -a + 1j*y, -a - 1j*y):
                tot += h_val(g_, c, lam, sig)
    return complex(tot)

def prime_side(c, lam, sig, N=None):
    if N is None:
        N = int(np.exp(lam + 6.0/sig)) + 10
    L = mangoldt_upto(N)
    n = np.arange(2, N + 1)
    gs = g_val(np.log(n), c, lam, sig)
    return complex(-2.0*np.sum(L[2:]/np.sqrt(n)*gs))

def arch_side(c, lam, sig):
    def integrand(t):
        hv = (mp.e**(1j*lam*(t - c) - (t - c)**2/(2*sig**2))
            + mp.e**(-1j*lam*(t + c) - (t + c)**2/(2*sig**2)))
        return hv*(mp.re(mp.digamma(mp.mpf('0.25') + 0.5j*t)) - mp.log(mp.pi))
    val = mp.quad(integrand, [-mp.inf, -c, 0, c, mp.inf])
    return complex(val/(2*mp.pi))

def pole_side(c, lam, sig):
    return complex(h_val(0.5j, c, lam, sig) + h_val(-0.5j, c, lam, sig))

def rhs(c, lam, sig):
    return pole_side(c, lam, sig) + arch_side(c, lam, sig) + prime_side(c, lam, sig)
