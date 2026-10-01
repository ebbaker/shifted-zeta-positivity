"""
Independent numerical checks of convention-sensitive statements in
papers/investigations/sonin-critical-boundary/manuscript.tex (commit 7034f88).

Checks:
 1. v_{1/2}(t) == 1 with the manuscript's exact Gamma / pi^{-it} factors (Sec. 6, line ~840).
 2. phi'_sigma(t) = Re psi(1/4+it/2) - log pi + 2 Re zeta'/zeta(sigma+it)   (eq. phase-deriv)
    against a finite-difference derivative of arg v_sigma.
 3. Blaschke energy  E(B_{d,gamma}) = 4 pi^2  independent of d          (Lemma energy)
 4. Critical explicit formula (eq. critical-explicit) for a Gaussian source:
       Gamma[F] - W_{1/2}[F] = Z_crit[F] + Z_off[F] - 2 Re a(i/2)   (Z_off = 0 for the zeros used)
 (Checks 5-7 -- crossing formula at sigma = 0.75, 1, 1.5; the archimedean gap constant c_0;
  local phase concentration -- are in check2_crossings.py.)
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 20
pi = mp.pi

def v_sigma(sigma, t):
    t = mp.mpf(t)
    g = mp.gamma(mp.mpf('0.25') + 1j*t/2) / mp.gamma(mp.mpf('0.25') - 1j*t/2)
    return g * mp.power(pi, -1j*t) * mp.zeta(sigma + 1j*t) / mp.zeta(sigma - 1j*t)

def gamma_inf(t):
    t = mp.mpf(t)
    return mp.re(mp.digamma(mp.mpf('0.25') + 1j*t/2)) - mp.log(pi)

def zlog(s):
    return mp.zeta(s, derivative=1) / mp.zeta(s)

def phi_prime(sigma, t):
    return gamma_inf(t) + 2*mp.re(zlog(sigma + 1j*mp.mpf(t)))

print("=== Check 1: v_{1/2}(t) = 1 ===")
for t in [0.5, 3.0, 10.0, 14.0, 30.5, 100.25]:
    val = v_sigma(mp.mpf('0.5'), t)
    print(f"  t={t:8.3f}  v_{{1/2}}(t) = {mp.nstr(val, 12)}   |v-1| = {mp.nstr(abs(val-1), 3)}")

print("\n=== Check 2: phase derivative formula vs finite difference of arg v_sigma ===")
for sigma in [mp.mpf('0.6'), mp.mpf('0.9'), mp.mpf('1.5')]:
    for t in [2.0, 14.0, 25.3]:
        h = mp.mpf('1e-6')
        # continuous argument via log of ratio (small step, no branch issue)
        fd = mp.im(mp.log(v_sigma(sigma, t+h) / v_sigma(sigma, t-h))) / (2*h)
        an = phi_prime(sigma, t)
        print(f"  sigma={float(sigma):4.2f} t={t:6.2f}  FD={mp.nstr(fd,10)}  formula={mp.nstr(an,10)}  diff={mp.nstr(fd-an,3)}")

print("\n=== Check 3: Blaschke energy E(B_d) = 4 pi^2 ===")
for d in [mp.mpf('0.001'), mp.mpf('0.1'), mp.mpf('3'), mp.mpf('-0.05')]:
    # E = int int 4 d^2 / ((t^2+d^2)(s^2+d^2)) dt ds = (2 pi)^2 * ... compute directly
    inner = mp.quad(lambda t: 2*abs(d)/(t**2 + d**2), [-mp.inf, 0, mp.inf])
    E = inner**2  # separable integrand: (int 2|d|/(t^2+d^2))^2
    print(f"  d={float(d):8.4f}  E = {mp.nstr(E, 12)}   4pi^2 = {mp.nstr(4*pi**2, 12)}")
# also check the pointwise identity |B(t)-B(s)|^2/(t-s)^2 = 4d^2/((t^2+d^2)(s^2+d^2)) at a random point
d = mp.mpf('0.37'); t = mp.mpf('1.3'); s = mp.mpf('-0.8')
B = lambda x: (x - 1j*d)/(x + 1j*d)
lhs = abs(B(t)-B(s))**2/(t-s)**2; rhs = 4*d**2/((t**2+d**2)*(s**2+d**2))
print(f"  pointwise identity: lhs={mp.nstr(lhs,12)} rhs={mp.nstr(rhs,12)}")

# ---------- Gaussian source for explicit-formula checks ----------
# F(x) = exp(-x^2/(2 s^2)),  Fhat(t) = s sqrt(2pi) exp(-s^2 t^2/2),
# a(z) = Fhat(z) conj(Fhat(conj z)) = 2 pi s^2 exp(-s^2 z^2),  kappa_F(x) = s sqrt(pi) exp(-x^2/(4 s^2))
s0 = mp.mpf('0.3')
def a_of(z):
    return 2*pi*s0**2 * mp.exp(-s0**2 * z**2)
def kappa(x):
    return s0*mp.sqrt(pi)*mp.exp(-mp.mpf(x)**2/(4*s0**2))

def Gamma_F():
    return mp.quad(lambda t: gamma_inf(t)*a_of(t)/(2*pi), [-mp.inf, -20, -5, 0, 5, 20, mp.inf])

def W_sigma(sigma, nmax=50000):
    # sum over prime powers p^m <= nmax of log p * p^{-m sigma} * (kappa(m log p) + kappa(-m log p))
    tot = mp.mpf(0)
    import sympy
    for p in sympy.primerange(2, nmax):
        lp = mp.log(p)
        m = 1
        while p**m <= nmax:
            x = m*lp
            term = lp * mp.power(p, -m*sigma) * (kappa(x) + kappa(-x))
            tot += term
            m += 1
    return tot

print("\n=== Check 4: critical explicit formula for Gaussian source (s=0.3) ===")
# zeros
NZ = 40
zeros = [mp.im(mp.zetazero(n)) for n in range(1, NZ+1)]
print(f"  using {NZ} zeros, last gamma = {mp.nstr(zeros[-1],8)}; tail weight a(gamma_last) = {mp.nstr(a_of(zeros[-1]),3)}")
Zcrit = sum(2*a_of(g) for g in zeros)   # both signs of gamma, multiplicity 1
GF = Gamma_F()
W12 = W_sigma(mp.mpf('0.5'))
pole = 2*mp.re(a_of(1j/2))
lhs = GF - W12
rhs = Zcrit - pole
print(f"  Gamma[F]      = {mp.nstr(GF,12)}")
print(f"  W_{{1/2}}[F]   = {mp.nstr(W12,12)}")
print(f"  Z_crit[F]     = {mp.nstr(Zcrit,12)}")
print(f"  2 Re a(i/2)   = {mp.nstr(pole,12)}")
print(f"  LHS Gamma-W   = {mp.nstr(lhs,12)}")
print(f"  RHS Zcrit-pole= {mp.nstr(rhs,12)}")
print(f"  difference    = {mp.nstr(lhs-rhs,3)}")

