"""Two independent checks of the central form Q_{0,L}, evaluated purely from
its Fourier/kernel definition (eq. weil) -- no use of the paper's U^gamma
monomial formula, G_0 profile, or moment tables.

 (A) Explicit-formula normalization: for a smooth even test f_c = cos^6(pi x/L),
     compare Q_{0,L}[f] with 2*sum_{gamma>0} |fhat_c(gamma)|^2 over zeta zeros.
 (Head-matrix entries are checked in check_head_exact.py, which uses an exact
     closed form for the log-multiplier part; a quadosc-based tail was not accurate
     enough for the tau^-2 decay of Legendre modes.)
"""
import os as _os
ARCHIVE_1P8 = _os.environ.get('ARCHIVE_1P8', 'output/length_1p8_N128/central_matrices.json.gz')
ARCHIVE_LOG7 = _os.environ.get('ARCHIVE_LOG7', 'output/log7_N128/central_matrices.json.gz')
import mpmath as mp
mp.mp.dps = 25
L = mp.mpf(9)/5
LOGPI = mp.log(mp.pi)
Lam = [(2, mp.log(2)), (3, mp.log(3)), (4, mp.log(2)), (5, mp.log(5))]

def multiplier(tau):
    return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*tau/2)) - LOGPI

def arch_term(fhat2):
    """(1/2pi) \int_R m(tau) |fhat(tau)|^2 dtau, integrand even in tau.
    Split multiplier: log(|tau|/2pi) + remainder O(tau^-2).  Both pieces are
    integrated on [0,T] with subdivision; beyond T use quadosc on the
    oscillatory tail (period pi/L in tau for |fhat|^2 ~ cos(tau L))."""
    T = mp.mpf(400)
    pts = [mp.mpf(0)] + [mp.mpf(2)**k/8 for k in range(0, 12)] + [T]
    pts = sorted(set(pts))
    head = mp.quad(lambda t: multiplier(t)*fhat2(t), pts)
    tail = mp.quadosc(lambda t: multiplier(t)*fhat2(t), [T, mp.inf], period=mp.pi/L)
    return 2*(head+tail)/(2*mp.pi)

def weil_form(f, fhat2, support):
    """Q_{0,L}[f] for real f on (0,L); f given in centered coordinate."""
    a, b = support
    C = mp.quad(lambda x: f(x)*mp.cosh(x/2), [a, 0, b])
    S = mp.quad(lambda x: f(x)*mp.sinh(x/2), [a, 0, b])
    def corr(d):  # \int f(x) f(x-d) dx
        return mp.quad(lambda x: f(x)*f(x-d), [a+d, b]) if d < b-a else mp.mpf(0)
    arith = -sum(lam/mp.sqrt(n)*2*corr(mp.log(n)) for n, lam in Lam if mp.log(n) < L)
    arch = arch_term(fhat2)
    return dict(arch=arch, pole=2*C**2-2*S**2, arith=arith, total=arch+2*C**2-2*S**2+arith)

# ---------- (A) explicit formula ----------
def fc(x):
    return mp.cos(mp.pi*x/L)**6 if abs(x) < L/2 else mp.mpf(0)
# cos^6 = (10 + 15 cos 2a + 6 cos 4a + cos 6a)/32 with a = pi x / L
coef = [(mp.mpf(10)/32, 0), (mp.mpf(15)/32, 2*mp.pi/L), (mp.mpf(6)/32, 4*mp.pi/L), (mp.mpf(1)/32, 6*mp.pi/L)]
def sinc_int(w):  # \int_{-L/2}^{L/2} cos(w x) dx
    return L if w == 0 else 2*mp.sin(w*L/2)/w
def fhat(tau):
    return sum(c*(sinc_int(w-tau)+sinc_int(w+tau))/2 for c, w in coef)
fhat2 = lambda t: fhat(t)**2
norm2 = mp.quad(lambda x: fc(x)**2, [-L/2, 0, L/2])
res = weil_form(fc, fhat2, (-L/2, L/2))
print("(A) test f_c = cos^6(pi x/L), L=9/5;  ||f||^2 =", mp.nstr(norm2, 12))
for k in ('arch', 'pole', 'arith', 'total'):
    print(f"    {k:6s} = {mp.nstr(res[k], 18)}")
zs = mp.mpf(0)
for n in range(1, 101):
    zs += 2*fhat(mp.im(mp.zetazero(n)))**2
    if n in (10, 30, 60, 100):
        print(f"    zero sum through n={n:3d}: {mp.nstr(zs, 18)}")
print("    relative discrepancy Q vs zero-sum:", mp.nstr((res['total']-zs)/zs, 5))
print("    Rayleigh quotient of this smooth test:", mp.nstr(res['total']/norm2, 8))

