"""
Check 1: the arithmetic normalization of Q_L against the zeta zeros.

Weil's explicit formula, in the normalisation used by the manuscript (Suzuki 1.1):
  sum_rho Phi_g(rho) = W(g),  Phi_g(s) = int g(x) e^{(s-1/2)x} dx,  g = F * F~.
For zeros rho = 1/2 + i gamma,  Phi_g(rho) = ghat(-gamma) = |Fhat(-gamma)|^2.

Test A: Gaussian-modulated F (Schwartz class) -- checks Suzuki's formula itself.
Test B: compactly supported f on (0,L) -- checks the manuscript's operator form Q_L
        (t_L via b(tau^2), w_0, 2cc*-2ss*, prime translations) against the zero sum.
"""
import mpmath as mp, os, json
from sympy import primerange

mp.mp.dps = 25
gammaE = mp.euler

def n_gamma(r):
    return mp.e**(-r/2)/(1-mp.e**(-2*r))

def fine_quad(fun, a, b, step):
    pts = mp.linspace(a, b, int((b-a)/step)+2)
    return mp.quad(fun, pts)

def weil_functional(g, g0, xmax, nmax, step):
    pole = fine_quad(lambda x: 2*mp.cosh(x/2)*g(x), -xmax, xmax, step)
    primes = 0
    for p in primerange(2, nmax+1):
        m = 1
        while p**m <= nmax:
            d = mp.log(p)*m
            primes += mp.log(p)*mp.mpf(p)**(-mp.mpf(m)/2)*(g(d)+g(-d))
            m += 1
    const = -(mp.log(4*mp.pi)+gammaE)*g0
    arch = -(fine_quad(lambda r: (g(r)+g(-r)-2*mp.e**(-r/2)*g0)*n_gamma(r), 0, xmax, step)
             + mp.quad(lambda r: (g(r)+g(-r)-2*mp.e**(-r/2)*g0)*n_gamma(r), [xmax, mp.inf]))
    return pole - primes + const + arch, dict(pole=pole, primes=primes, const=const, arch=arch)

# zeros cache
ZF = 'zeros_300.json'
if os.path.exists(ZF):
    zeros = [mp.mpf(z) for z in json.load(open(ZF))]
else:
    with mp.workdps(20):
        zeros = [mp.im(mp.zetazero(n)) for n in range(1, 301)]
    json.dump([mp.nstr(z, 22) for z in zeros], open(ZF, 'w'))
print("zeros loaded:", len(zeros), "highest:", mp.nstr(zeros[-1], 8))

# ---------------- Test A ----------------
omega = mp.mpf(30)
def gA(x):
    return mp.sqrt(mp.pi)/2*mp.e**(-x*x/4)*(mp.cos(omega*x)+mp.e**(-omega**2))
def Fhat2A(t):
    return mp.pi/2*(mp.e**(-(t-omega)**2/2)+mp.e**(-(t+omega)**2/2))**2
lhsA = sum(2*Fhat2A(gm) for gm in zeros)
rhsA, partsA = weil_functional(gA, gA(0), xmax=14, nmax=2_000_000, step=mp.mpf('0.1'))
print("\nTest A (F = e^{-x^2/2} cos(30x))")
print("  zero sum     =", mp.nstr(lhsA, 20))
print("  Weil formula =", mp.nstr(rhsA, 20))
print("  difference   =", mp.nstr(lhsA-rhsA, 5))
print("  parts:", {k: mp.nstr(v, 12) for k, v in partsA.items()})

# ---------------- Test B ----------------
L = mp.mpf(3)
# f(x) = sin^4(pi x/L) = 3/8 - (1/2) cos(2 pi x/L) + (1/8) cos(4 pi x/L)
coef = [(mp.mpf(3)/8, 0), (-mp.mpf(1)/2, 2*mp.pi/L), (mp.mpf(1)/8, 4*mp.pi/L)]
def f(x):
    return mp.sin(mp.pi*x/L)**4 if 0 < x < L else mp.mpf(0)
def E(alpha):   # int_0^L e^{i alpha x} dx
    return L*mp.e**(1j*alpha*L/2)*mp.sinc(alpha*L/2)
def Fhat(t):    # int_0^L f(x) e^{-itx} dx
    return sum(cc*(E(w-t)+E(-w-t))/2 for cc, w in coef)
def hf(r):      # Re <F, U_r F> for real f
    if r >= L: return mp.mpf(0)
    return mp.quad(lambda x: f(x)*f(x-r), [r, (r+L)/2, L])
normf2 = mp.quad(lambda x: f(x)**2, [0, L/2, L])
assert abs(normf2 - 35*L/128) < mp.mpf(10)**-18   # int_0^L sin^8(pi x/L) dx = 35L/128
print("\n|f|^2 =", mp.nstr(normf2, 12), " (35L/128 =", mp.nstr(35*L/128, 12), ")")

psi14 = mp.digamma(mp.mpf(1)/4)
def b(s):
    return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.sqrt(s)/2)) - psi14
w0 = psi14 - mp.log(mp.pi)
print("w0 =", mp.nstr(w0, 15), " check -gamma-pi/2-3log2-logpi =",
      mp.nstr(-gammaE-mp.pi/2-3*mp.log(2)-mp.log(mp.pi), 15))

pts = mp.linspace(0, 100, 401) + [150, 200, 300, 500, 1000, mp.inf]
tL = 2*mp.quad(lambda t: b(t*t)*abs(Fhat(t))**2, pts)/(2*mp.pi)
c = lambda x: mp.cosh((x-L/2)/2)
s = lambda x: mp.sinh((x-L/2)/2)
cf = mp.quad(lambda x: c(x)*f(x), [0, L/2, L]); sf = mp.quad(lambda x: s(x)*f(x), [0, L/2, L])
prime_term = 0; active = []
for p in primerange(2, int(mp.e**L)+2):
    m = 1
    while m*mp.log(p) < L:
        d = m*mp.log(p); active.append(p**m)
        prime_term += mp.log(p)*mp.mpf(p)**(-mp.mpf(m)/2)*2*hf(d)
        m += 1
QL = tL + w0*normf2 + 2*cf**2 - 2*sf**2 - prime_term
print("active prime powers below e^L:", sorted(active))

lhsB = sum(2*abs(Fhat(gm))**2 for gm in zeros)
tail = 2*mp.quad(lambda t: abs(Fhat(t))**2*mp.log(t/(2*mp.pi))/(2*mp.pi), [zeros[-1], 2*zeros[-1], mp.inf])
print("\nTest B (f = sin^4(pi x/L) on (0,3))")
print("  zero sum (300 zeros) =", mp.nstr(lhsB, 15), "  est. tail beyond last zero ~", mp.nstr(tail, 3))
print("  Q_L manuscript form  =", mp.nstr(QL, 15))
print("  difference           =", mp.nstr(lhsB-QL, 5))
print("  pieces: t_L=%s  w0|f|^2=%s  2c^2=%s  -2s^2=%s  -primes=%s" %
      tuple(mp.nstr(v, 10) for v in (tL, w0*normf2, 2*cf**2, -2*sf**2, -prime_term)))

def gB(x):
    return hf(abs(x))
rhsB, partsB = weil_functional(gB, normf2, xmax=L, nmax=int(mp.e**L)+1, step=mp.mpf('0.25'))
print("  Suzuki functional on g=F*F~ =", mp.nstr(rhsB, 15), "  diff vs Q_L:", mp.nstr(rhsB-QL, 5))
print("  parts:", {k: mp.nstr(v, 12) for k, v in partsB.items()})
