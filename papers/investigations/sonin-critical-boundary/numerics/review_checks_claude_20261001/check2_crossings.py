"""
Remaining convention checks (finite ranges, dps=15):
 4b. critical explicit formula with s=0.15 so that the critical-zero sum is a visible contribution
 5.  eq. crossing-formula at sigma = 0.75, 1.0 (exceptional pole line), 1.5
 6.  c_0 = ||C_infty||
 7.  local phase concentration at gamma_1
"""
import mpmath as mp
import numpy as np
import sympy
mp.mp.dps = 15
pi = mp.pi

def gamma_inf(t):
    t = mp.mpf(t)
    return mp.re(mp.digamma(mp.mpf('0.25') + 1j*t/2)) - mp.log(pi)
def zlog(s):
    return mp.zeta(s, derivative=1) / mp.zeta(s)
def phi_prime(sigma, t):
    return gamma_inf(t) + 2*mp.re(zlog(sigma + 1j*mp.mpf(t)))

zeros = [mp.im(mp.zetazero(n)) for n in range(1, 31)]

def make_source(s0):
    a_of = lambda z: 2*pi*s0**2 * mp.exp(-s0**2 * z**2)
    kappa = lambda x: s0*mp.sqrt(pi)*mp.exp(-mp.mpf(x)**2/(4*s0**2))
    return a_of, kappa

def W_sigma(sigma, kappa, nmax=50000):
    tot = mp.mpf(0)
    for p in sympy.primerange(2, nmax):
        lp = mp.log(p); m = 1
        while p**m <= nmax:
            x = m*lp
            tot += lp * mp.power(p, -m*sigma) * (kappa(x) + kappa(-x))
            m += 1
    return tot

print("=== Check 4b: critical explicit formula, Gaussian source s=0.15 ===")
s0 = mp.mpf('0.15'); a_of, kappa = make_source(s0)
Tmax = 60  # a(60) = 2pi s^2 e^{-0.0225*3600} ~ e^{-81}
GF = mp.quad(lambda t: gamma_inf(t)*a_of(t)/(2*pi), mp.linspace(-Tmax, Tmax, 25))
W12 = W_sigma(mp.mpf('0.5'), kappa)
Zcrit = sum(2*a_of(g) for g in zeros)
pole = 2*mp.re(a_of(1j/2))
print(f"  Gamma[F]={mp.nstr(GF,12)}  W_1/2[F]={mp.nstr(W12,12)}  Z_crit[F]={mp.nstr(Zcrit,12)}  2Re a(i/2)={mp.nstr(pole,12)}")
print(f"  LHS Gamma-W = {mp.nstr(GF-W12,12)}   RHS Zcrit - pole = {mp.nstr(Zcrit-pole,12)}   diff = {mp.nstr(GF-W12-(Zcrit-pole),3)}")
print(f"  (first zero weight a(gamma_1) = {mp.nstr(a_of(zeros[0]),4)}, last used a(gamma_30) = {mp.nstr(a_of(zeros[-1]),3)})")

print("\n=== Check 5: eq. crossing-formula, bulk zeta part vs -W_sigma + P_sigma (Gaussian s=0.3) ===")
s0 = mp.mpf('0.3'); a_of, kappa = make_source(s0)
Tmax = 40
for sigma in [mp.mpf('0.75'), mp.mpf('1.0'), mp.mpf('1.5')]:
    pts = sorted(set([-Tmax] + [float(-g) for g in zeros[:6]] + [0.0] + [float(g) for g in zeros[:6]] + [Tmax]))
    pts = [mp.mpf(p) for p in pts]
    if sigma == 1:
        # removable value at t=0: integrand is smooth; avoid evaluating exactly at the pole by tiny offset in the quadrature nodes
        f = lambda t: a_of(t)*2*mp.re(zlog(sigma+1j*(t if t != 0 else mp.mpf('1e-9'))))/(2*pi)
    else:
        f = lambda t: a_of(t)*2*mp.re(zlog(sigma+1j*t))/(2*pi)
    bulk = mp.quad(f, pts)
    Wsig = W_sigma(sigma, kappa)
    if sigma < 1:   P = 2*mp.re(a_of(1j*(1-sigma)))
    elif sigma == 1: P = a_of(0)
    else:            P = mp.mpf(0)
    print(f"  sigma={float(sigma):4.2f}: bulk={mp.nstr(bulk,10)}  -W+P={mp.nstr(-Wsig+P,10)}  diff={mp.nstr(bulk-(-Wsig+P),3)}   [W={mp.nstr(Wsig,8)}, P={mp.nstr(P,8)}]")

print("\n=== Check 6: c_0 = ||C_infty|| via finite cosine transform on (0,1) ===")
from numpy.polynomial.legendre import leggauss
for n in [200, 400]:
    x, w = leggauss(n); u = 0.5*(x+1); wu = 0.5*w
    K = 2*np.cos(2*np.pi*np.outer(u, u)); sw = np.sqrt(wu)
    sv = np.linalg.svd(sw[:, None]*K*sw[None, :], compute_uv=False)
    print(f"  n={n}: c_0={sv[0]:.12f}  1-c_0^2={1-sv[0]**2:.6e}  next sv: {sv[1]:.6f} {sv[2]:.6f} {sv[3]:.6f} {sv[4]:.6f} {sv[5]:.2e}")
c = 2*np.pi
print(f"  Slepian asymptotic 1-lambda_0(c=2pi) ~ 4 sqrt(pi c) e^(-2c) = {4*np.sqrt(np.pi*c)*np.exp(-2*c):.3e}")
# transport constants at a few sigma>1 for the gap g_sigma = (zeta(2s)/zeta(s)^2)^2 (1-c0^2)
c0sq = sv[0]**2
for sg in [1.1, 1.5, 2.0, 3.0]:
    ratio = float(mp.zeta(2*sg)/mp.zeta(sg)**2)
    print(f"  sigma={sg}: (l/u)^2 = {ratio**2:.3e}   g_sigma = {ratio**2*(1-c0sq):.3e}")

print("\n=== Check 7: local phase concentration at gamma_1 (|b|^2 = exp(-(t-gamma_1)^2)) ===")
g1 = zeros[0]
b2 = lambda t: mp.exp(-(t-g1)**2)
for sigma in [mp.mpf('0.7'), mp.mpf('0.6'), mp.mpf('0.55'), mp.mpf('0.52'), mp.mpf('0.505')]:
    eps = sigma - mp.mpf('0.5')
    pts = [g1-7, g1-2, g1-1, g1-10*eps, g1-eps, g1, g1+eps, g1+10*eps, g1+1, g1+2, g1+7]
    val = mp.quad(lambda t: b2(t)*phi_prime(sigma, t)/(2*pi), pts)
    # Poisson prediction from the single Blaschke factor at gamma_1 plus smooth remainder ~ 0
    pois = mp.quad(lambda t: b2(t)*(2*eps/(eps**2+(t-g1)**2))/(2*pi), pts)
    print(f"  sigma={float(sigma):6.3f}: int|b|^2 phi' dt/2pi = {mp.nstr(val,8)}    pure Poisson term = {mp.nstr(pois,8)}")
