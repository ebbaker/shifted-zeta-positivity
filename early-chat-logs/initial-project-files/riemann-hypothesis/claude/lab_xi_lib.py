"""Numerics lab for the rotational-symmetry RH program.

Objects:
  * Xi(x) via the Riemann cosine transform  Xi(x) = C * int_0^inf Phi(u) cos(xu) du
    (Phi > 0, super-exponentially decaying), with derivatives; validated against
    the mpmath xi.
  * The Davenport-Heilbronn function Xi_DH(z) = Lambda_DH(1/2 + iz): even, real
    on R, entire, functional equation -- but with off-line zeros (zero spheres
    in the quaternionic extension).  The canonical control case.
  * The Laguerre detector  L1[F](x) = F'(x)^2 - F(x) F''(x)  (axis shadow of the
    sphere/no-sphere dichotomy: L1 >= 0 everywhere is necessary for zeros real).
  * The l-graded sector energies E_l built from Bessel tags j_l(lambda*y0):
    quadratic in the zeros; real zeros vanish from every l>=1 sector.
"""
import numpy as np
import mpmath as mp
from scipy.special import spherical_jn

# ----------------------------------------------------------------------
# Xi via the Phi cosine transform (numpy, vectorized)
# ----------------------------------------------------------------------
def Phi(u, nterms=6):
    """Polya's Phi(u) = sum_n (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}."""
    u = np.asarray(u, dtype=float)
    out = np.zeros_like(u)
    e2u = np.exp(2.0 * u)
    for n in range(1, nterms + 1):
        out += (2 * np.pi**2 * n**4 * np.exp(4.5 * u)
                - 3 * np.pi * n**2 * np.exp(2.5 * u)) * np.exp(-np.pi * n**2 * e2u)
    return out

# quadrature grid for the u-integral (Phi is numerically 0 beyond u ~ 2.5)
_U = np.linspace(0.0, 3.2, 64001)
_PHI = Phi(_U)
_DU = _U[1] - _U[0]

def xi_int(x, deriv=0):
    """Xi and derivatives from the cosine transform:
       Xi(x) = 4 * int_0^inf Phi(u) cos(xu) du   (constant 4 certified against mpmath xi),
       Xi'(x) = -4 * int Phi(u) u sin(xu) du,  Xi''(x) = -4 * int Phi(u) u^2 cos(xu) du."""
    x = np.atleast_1d(np.asarray(x, dtype=float))
    ph = x[:, None] * _U[None, :]
    if deriv == 0:
        ker = np.cos(ph)
        w = _PHI
    elif deriv == 1:
        ker = -np.sin(ph)
        w = _PHI * _U
    elif deriv == 2:
        ker = -np.cos(ph)
        w = _PHI * _U**2
    else:
        raise ValueError
    vals = 4.0 * np.trapezoid(ker * w[None, :], dx=_DU, axis=1)  # 4: matches xi(1/2+ix), verified
    return vals if vals.size > 1 else vals[0]

def xi_mp(x):
    """Reference value: xi(1/2+ix) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)."""
    s = mp.mpf('0.5') + mp.mpc(0, 1) * mp.mpf(str(x))
    v = mp.mpf('0.5') * s * (s - 1) * mp.pi**(-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    return complex(v)

# ----------------------------------------------------------------------
# Davenport-Heilbronn
# ----------------------------------------------------------------------
_chi = {1: 1, 2: 1j, 3: -1j, 4: -1}          # odd character mod 5, chi(2)=i
_kappa = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)

def L_chi(s, conj=False):
    tot = mp.mpc(0)
    for a in range(1, 5):
        c = _chi[a].conjugate() if conj else _chi[a]
        tot += c * mp.zeta(s, mp.mpf(a) / 5)
    return 5**(-s) * tot

def f_DH(s):
    s = mp.mpc(s)
    return ((1 - 1j * _kappa) * L_chi(s) + (1 + 1j * _kappa) * L_chi(s, conj=True)) / 2

def Lambda_DH(s):
    s = mp.mpc(s)
    return (mp.mpf(5) / mp.pi)**(s / 2) * mp.gamma((s + 1) / 2) * f_DH(s)

def Xi_DH(z):
    """Rotated DH: real and even for real z."""
    return Lambda_DH(mp.mpf('0.5') + 1j * mp.mpc(z))

def Xi_DH_real(x):
    return float(Xi_DH(mp.mpf(str(x))).real)

# ----------------------------------------------------------------------
# Laguerre detector (function data only -- no zero locations used)
# ----------------------------------------------------------------------
def laguerre_xi(x):
    """L1[Xi](x) from the analytic derivatives of the cosine transform."""
    F, F1, F2 = xi_int(x, 0), xi_int(x, 1), xi_int(x, 2)
    return F1**2 - F * F2

def laguerre_num(F, x, h=1e-3):
    """L1 by central differences for any real function F (e.g. Xi_DH_real)."""
    f0 = F(x)
    fp = (F(x + h) - F(x - h)) / (2 * h)
    fpp = (F(x + h) - 2 * f0 + F(x - h)) / h**2
    return fp**2 - f0 * fpp

# ----------------------------------------------------------------------
# l-graded sector energies (quadratic in the zeros)
# ----------------------------------------------------------------------
def sector_energy(zeros, ell, lam_max=2.0, nlam=2000, lam_scale=1.0):
    """E_l = int_0^lam_max | sum_rho j_l(lam*y_rho) e^{i lam a_rho} |^2 w(lam) dlam,
       zeros = list of (a, y) with y>=0: y=0 real zero, y>0 zero sphere (pair).
       w = Gaussian window exp(-(lam/lam_scale)^2)."""
    lam = np.linspace(1e-6, lam_max, nlam)
    S = np.zeros_like(lam, dtype=complex)
    for (a, y) in zeros:
        S += spherical_jn(ell, lam * y) * np.exp(1j * lam * a)
    w = np.exp(-(lam / lam_scale)**2)
    return np.trapezoid(np.abs(S)**2 * w, lam)

def zeta_ordinates(n):
    return [float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)]
