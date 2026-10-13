"""
Numerical library for the Second Involution note.

Conventions (matching second_involution_intro.tex):
  rho = 1/2 + i*gamma ; zero multiset {gamma} closed under gamma -> -gamma
  and gamma -> conj(gamma).
  Test function (sigma > 0 fixed):
      h_{c,lam}(r) = exp(i lam (r-c)) exp(-(r-c)^2/(2 sigma^2))
                   + exp(-i lam (r+c)) exp(-(r+c)^2/(2 sigma^2))
  Z(c,lam) = sum over full multiset {gamma} of h_{c,lam}(gamma).

Guinand-Weil (paper eq. (1.2)):
  Z = h(i/2) + h(-i/2)
      + (1/2pi) Int h(t) [ Re psi(1/4 + it/2) - log pi ] dt
      - 2 sum_{n>=2} Lambda(n) n^{-1/2} g(log n),
  g(u) = (1/2pi) Int h(r) e^{-iur} dr
       = (sigma/sqrt(2pi)) [ e^{-iuc} e^{-sigma^2 (u-lam)^2/2}
                           + e^{+iuc} e^{-sigma^2 (u+lam)^2/2} ].
"""
import numpy as np
import mpmath as mp

SIGMA = 1.0
LAMSTAR = float(np.log(2.0))

# ---------------------------------------------------------------- primes
def mangoldt_table(nmax):
    """Return arrays n, Lambda(n) for 2 <= n <= nmax with Lambda(n) != 0."""
    ns, vals = [], []
    sieve = np.ones(nmax + 1, dtype=bool); sieve[:2] = False
    for p in range(2, nmax + 1):
        if sieve[p]:
            sieve[2*p::p] = False
    primes = np.nonzero(sieve)[0]
    for p in primes:
        logp = np.log(float(p))
        q = p
        while q <= nmax:
            ns.append(q); vals.append(logp)
            q *= p
    ns = np.array(ns, dtype=float); vals = np.array(vals, dtype=float)
    order = np.argsort(ns)
    return ns[order], vals[order]

NMAX = 20000
_NS, _LAM = mangoldt_table(NMAX)
_LOGNS = np.log(_NS)
_INVSQ = 1.0 / np.sqrt(_NS)

# ---------------------------------------------------------------- prime side
def Z_prime(c, lam, sigma=SIGMA, arch=True):
    """Z(c,lam) from the prime side (complex).  c may be an array."""
    c = np.atleast_1d(np.asarray(c, dtype=float))
    u = _LOGNS
    w_minus = np.exp(-sigma**2 * (u - lam)**2 / 2.0)
    w_plus  = np.exp(-sigma**2 * (u + lam)**2 / 2.0)
    # g(log n) for each c: (sigma/sqrt(2pi)) [e^{-i u c} w_minus + e^{i u c} w_plus]
    phase = np.exp(-1j * np.outer(c, u))
    g = (sigma / np.sqrt(2*np.pi)) * (phase * w_minus + np.conj(phase) * w_plus)
    prime_sum = -2.0 * (g * (_LAM * _INVSQ)).sum(axis=1)
    if arch:
        prime_sum = prime_sum + np.array([_arch_plus_poles(ci, lam, sigma) for ci in c])
    return prime_sum if prime_sum.size > 1 else prime_sum[0]

def _h(r, c, lam, sigma):
    return (mp.e**(1j*lam*(r-c)) * mp.e**(-(r-c)**2/(2*sigma**2)) +
            mp.e**(-1j*lam*(r+c)) * mp.e**(-(r+c)**2/(2*sigma**2)))

def _arch_plus_poles(c, lam, sigma):
    """Pole terms + archimedean integral, complex, via mpmath quadrature."""
    mp.mp.dps = 20
    pole = _h(mp.mpc(0, 0.5), c, lam, sigma) + _h(mp.mpc(0, -0.5), c, lam, sigma)
    def integrand(t):
        psi_re = mp.re(mp.digamma(mp.mpc(0.25, t/2.0)))
        return _h(t, c, lam, sigma) * (psi_re - mp.log(mp.pi))
    W = 14.0
    if abs(c) > 2*W:   # h concentrates near t = +-c
        I = (mp.quad(integrand, [c - W, c, c + W]) +
             mp.quad(integrand, [-c - W, -c, -c + W]))
    else:
        lo, hi = -abs(c) - W, abs(c) + W
        I = mp.quad(integrand, [lo, -abs(c), 0, abs(c), hi])
    return complex(pole + I / (2*mp.pi))

# ---------------------------------------------------------------- zero side
def load_zeros(path='zeros.txt'):
    return np.loadtxt(path)

def Z_zero(c, lam, gammas_pos, sigma=SIGMA):
    """Z(c,lam) summed over multiset {+-gamma_n} (all on real axis)."""
    c = np.atleast_1d(np.asarray(c, dtype=float))
    out = np.zeros(c.shape, dtype=complex)
    for sgn in (1.0, -1.0):
        g = sgn * gammas_pos
        d1 = g[None, :] - c[:, None]
        d2 = g[None, :] + c[:, None]
        out += (np.exp(1j*lam*d1 - d1**2/(2*sigma**2)) +
                np.exp(-1j*lam*d2 - d2**2/(2*sigma**2))).sum(axis=1)
    return out if out.size > 1 else out[0]

def Z_zero_multiset(c, lam, gammas_full, sigma=SIGMA):
    """Z(c,lam) over an explicit full multiset of (possibly complex) gammas."""
    c = np.atleast_1d(np.asarray(c, dtype=float))
    g = np.asarray(gammas_full, dtype=complex)
    d1 = g[None, :] - c[:, None]
    d2 = g[None, :] + c[:, None]
    out = (np.exp(1j*lam*d1 - d1**2/(2*sigma**2)) +
           np.exp(-1j*lam*d2 - d2**2/(2*sigma**2))).sum(axis=1)
    return out if out.size > 1 else out[0]

def D_defect(c, gammas_full, sigma=SIGMA):
    """Windowed reality defect D(c) = sum (Im gamma)^2 exp(-(Re gamma - c)^2/2sigma^2)."""
    c = np.atleast_1d(np.asarray(c, dtype=float))
    g = np.asarray(gammas_full, dtype=complex)
    y2 = np.imag(g)**2
    x = np.real(g)
    out = (y2[None, :] * np.exp(-(x[None, :] - c[:, None])**2/(2*sigma**2))).sum(axis=1)
    return out if out.size > 1 else out[0]

# ---------------------------------------------------------------- oscillation
def B_coeff(n, lam=LAMSTAR, sigma=SIGMA):
    """Coefficient of cos(c log n) in the prime part of F(c) = Re Z(c,lam)."""
    ln = np.log(n)
    Lam = 0.0
    m = n
    # Lambda(n)
    for p in range(2, n+1):
        if n % p == 0:
            k = n
            while k % p == 0:
                k //= p
            Lam = np.log(p) if k == 1 else 0.0
            break
    return 2*Lam*n**-0.5*(sigma/np.sqrt(2*np.pi))*(np.exp(-sigma**2*(ln-lam)**2/2)
                                                   + np.exp(-sigma**2*(ln+lam)**2/2))

def window_osc(F_vals):
    return F_vals.max() - F_vals.min()
