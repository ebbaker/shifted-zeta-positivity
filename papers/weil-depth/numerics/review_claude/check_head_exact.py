"""Accurate, independent evaluation of the head matrix diagonal Q_{0,L}[phi_n].

Archimedean multiplier split:  m(tau) = log(|tau|/2pi) + r(tau),
   r(tau) = Re psi(1/4+i tau/2) - log(|tau|/2) = O(tau^-2).
The log part on a Legendre mode is exact via Weber-Schafheitlin
(DLMF 10.22.57) differentiated in lambda:
   (1/2pi) \int log(|tau|/2pi) |hat phi_n|^2 dtau
      = log 2 + (psi(n+1/2)+psi(n+3/2))/2 - log(pi L).
The remainder r(tau)|hat phi_n|^2 decays like tau^-4 and is integrated
numerically.  No use of the paper's U^gamma / G_0 / moment formulas."""
import os as _os
ARCHIVE_1P8 = _os.environ.get('ARCHIVE_1P8', 'output/length_1p8_N128/central_matrices.json.gz')
ARCHIVE_LOG7 = _os.environ.get('ARCHIVE_LOG7', 'output/log7_N128/central_matrices.json.gz')
import mpmath as mp, gzip, json
mp.mp.dps = 25
L = mp.mpf(9)/5
Lam = [(2, mp.log(2)), (3, mp.log(3)), (4, mp.log(2)), (5, mp.log(5))]

def jn2(n, x):
    if x == 0:
        return mp.mpf(1 if n == 0 else 0)
    return (mp.sqrt(mp.pi/(2*x))*mp.besselj(n+mp.mpf(1)/2, x))**2

def phihat2(n, tau):
    return (2*n+1)*L*jn2(n, tau*L/2)

def r(tau):
    return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*tau/2)) - mp.log(tau/2)

def log_part_exact(n):
    return mp.log(2) + (mp.digamma(n+mp.mpf(1)/2)+mp.digamma(n+mp.mpf(3)/2))/2 - mp.log(mp.pi*L)

def remainder_part(n):
    pts = [mp.mpf(0)] + [mp.mpf(2)**k/16 for k in range(0, 14)] + [mp.inf]
    return 2*mp.quad(lambda t: r(t)*phihat2(n, t), pts)/(2*mp.pi)

def phi(n):
    return lambda x: mp.sqrt((2*n+1)/L)*mp.legendre(n, 2*x/L)

def pole_and_arith(n):
    f = phi(n)
    C = mp.quad(lambda x: f(x)*mp.cosh(x/2), [-L/2, 0, L/2])
    S = mp.quad(lambda x: f(x)*mp.sinh(x/2), [-L/2, 0, L/2])
    def corr(d):
        return mp.quad(lambda x: f(x)*f(x-d), [-L/2+d, L/2])
    arith = -sum(lam/mp.sqrt(k)*2*corr(mp.log(k)) for k, lam in Lam if mp.log(k) < L)
    return 2*C**2-2*S**2, arith

# sanity check of the closed form at n=0 against direct quadrature of the sinc^2
direct0 = 2*mp.quad(lambda t: mp.log(t/(2*mp.pi))*4*mp.sin(t*L/2)**2/(L*t**2), [0, 1, 10, 100, 1000, 10**4, 10**5, 10**6, mp.inf])/(2*mp.pi)
print("closed form n=0:", mp.nstr(log_part_exact(0), 12), "  direct quad (approx):", mp.nstr(direct0, 12))

with gzip.open(ARCHIVE_1P8, 'rt') as fh:
    data = json.load(fh)
def entry(name, i, j):
    m, e = data['matrices'][name][i][j][0]
    return mp.mpf(int(m))*mp.mpf(2)**int(e)

print("\nDiagonal head entries at L=9/5 (Arb head from rebuilt certify_arb.py archive):")
print(" n |    log part |  remainder |       pole |      arith |  Fourier-side Q[n,n] |      Arb Q[n,n] |  difference")
for n in (0, 1, 2, 3, 6, 10, 20):
    lp = log_part_exact(n); rp = remainder_part(n); pole, ar = pole_and_arith(n)
    tot = lp+rp+pole+ar
    q = entry('Q', n, n)
    print(f"{n:2d} | {mp.nstr(lp,10):>11s} | {mp.nstr(rp,8):>10s} | {mp.nstr(pole,8):>10s} | {mp.nstr(ar,8):>10s} | {mp.nstr(tot,14):>20s} | {mp.nstr(q,14):>15s} | {mp.nstr(tot-q,3)}")
