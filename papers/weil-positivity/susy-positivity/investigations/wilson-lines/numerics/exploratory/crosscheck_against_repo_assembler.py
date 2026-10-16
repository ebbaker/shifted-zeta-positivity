"""End-to-end cross-check: Q[f] from the closed-form matrix vs the repository's
pre-existing quadrature assembler (weil_functional of chk1_explicit_formula.py),
fed the autocorrelation S(u) = g(u)+g(-u) in closed form."""
import mpmath as mp, wf2, random
from sympy import primerange
mp.mp.dps = 25
L = mp.mpf('1.6'); N = 9
random.seed(7)
c = [mp.mpf(random.uniform(-1, 1)) for _ in range(N)]
nrm = mp.sqrt(mp.fsum(x*x for x in c)); c = [x/nrm for x in c]
W = wf2.WeilForm(L, N); comb = wf2.prime_comb(L)
def S(u):                       # g(u) + g(-u) for f = sum c_k psi_k
    u = abs(u)
    if u >= L: return mp.mpf(0)
    return mp.fsum(c[j-1]*c[k-1]*W.S(j, k, u) for j in range(1, N+1) for k in range(1, N+1))
g0 = S(mp.mpf(0))/2
def n_gamma(r): return mp.e**(-r/2)/(1-mp.e**(-2*r))
def fq(fun, a, b, step): return mp.quad(fun, mp.linspace(a, b, int((b-a)/step)+2))
pole = fq(lambda x: 2*mp.cosh(x/2)*S(x)/2, -L, L, mp.mpf('0.05'))*2/2   # int 2cosh(x/2) g(x) dx
pole = fq(lambda u: 2*mp.cosh(u/2)*S(u), 0, L, mp.mpf('0.05'))
primes = 0
for p in primerange(2, int(mp.e**L)+2):
    m = 1
    while p**m <= int(mp.e**L)+1:
        primes += mp.log(p)*mp.mpf(p)**(-mp.mpf(m)/2)*S(mp.log(p)*m); m += 1
const = -(mp.log(4*mp.pi)+mp.euler)*g0
arch = -(fq(lambda r: (S(r)-2*mp.e**(-r/2)*g0)*n_gamma(r), 0, L, mp.mpf('0.02'))
         + mp.quad(lambda r: -2*mp.e**(-r/2)*g0*n_gamma(r), [L, mp.inf]))
rep = pole - primes + const + arch
closed = mp.mpf(0)
for par in (0, 1):
    Mx, ix = W.matrix(comb, par)
    closed += mp.fsum(c[ix[a]-1]*Mx[a, b]*c[ix[b]-1]
                      for a in range(len(ix)) for b in range(len(ix)))
print("||f||^2 (should be 1):", mp.nstr(g0, 18))
print("repository quadrature assembler:", mp.nstr(rep, 16))
print("closed-form matrix contraction :", mp.nstr(closed, 16))
print("relative difference            :", mp.nstr(abs(rep-closed)/abs(rep), 4))
print("  parts: pole=%s primes=%s const=%s arch=%s"
      % tuple(mp.nstr(v, 10) for v in (pole, primes, const, arch)))
Om = lambda t: mp.re(mp.digamma(mp.mpf(1)/4+1j*t/2)) - mp.log(mp.pi)
print()
print("Omega(0) =", mp.nstr(Om(0), 10), "; increasing in |tau|:",
      all(Om(mp.mpf(t)) < Om(mp.mpf(t)+mp.mpf('0.25')) for t in [0,0.5,1,2,5,10,50,200,1000]))
print("pi/gamma_1 =", mp.nstr(mp.pi/mp.mpf('14.1347251417'), 10))
