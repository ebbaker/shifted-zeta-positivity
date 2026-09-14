"""
Check 6: mechanism of the tiny eigenvalues.  For the eigenvectors of the cosine compression
W_K belonging to the smallest eigenvalues, evaluate the zero sum  sum_gamma 2|Fhat(gamma)|^2
directly (300 zeros) and the Fourier mass inside the zero-free window |tau| < 14.13.
If Q_L[f] = sum_rho |Fhat|^2 (explicit formula), the eigenvalue must equal the zero sum.
"""
import numpy as np, json, mpmath as mp, importlib.util, sys
spec = importlib.util.spec_from_file_location('chk3', 'chk3_operator_and_schur.py')
# re-use assemble() without running the whole chk3 script: copy the function source
src = open('chk3_operator_and_schur.py').read()
start = src.index('def assemble'); end = src.index('def active_powers')
ns = {}
exec("import numpy as np, mpmath as mp\nfrom scipy.special import digamma\nmp.mp.dps=30\npsi14=float(mp.digamma(0.25)); w0=psi14-np.log(np.pi)\ndef a_k(k): return 2*k+0.5\n" + src[start:end], ns)
assemble = ns['assemble']
from sympy import primerange
def active_powers(L):
    pp = []
    for p in primerange(2, int(np.exp(L))+2):
        m = 1
        while m*np.log(p) < L:
            pp.append((int(p), m)); m += 1
    return pp
zeros = np.array([float(z) for z in json.load(open('zeros_300.json'))])
gamma1 = zeros[0]
res = {}
for L, K, nvec in [(1.0, 400, 3), (2.0, 400, 4)]:
    M = assemble(L, K, active_powers(L)); W = M['W']; nu = M['nu']; om = M['om']
    ev, V = np.linalg.eigh(W)
    print(f"\nL={L}, K={K}: smallest eigenvalues {ev[:nvec]}")
    def Fhat(c, t):   # F = sum c_j e_j on (0,L), zero extension
        t = np.atleast_1d(t)[:, None]
        # int_0^L cos(om x) e^{-itx} dx = (1/2)[E(om - t) + E(-om - t)],  E(al) = L e^{i al L/2} sinc(al L/2)
        def E(al): return L*np.exp(1j*al*L/2)*np.sinc(al*L/(2*np.pi))
        return ((c*nu)[None, :]*(E(om[None, :]-t) + E(-om[None, :]-t))/2).sum(1)
    for k in range(nvec):
        c = V[:, k]
        zs = 2*np.sum(np.abs(Fhat(c, zeros))**2)
        # tail beyond last zero: density (1/2pi) log(t/2pi)
        from scipy import integrate
        # tail: |Fhat|^2 ~ (f(0)^2 + f(L)^2)/t^2 on average (endpoint jumps), zero density log(t/2pi)/(2pi)
        f0 = np.sum(c*nu); fL = np.sum(c*nu*M['sgn']); T = zeros[-1]
        tail = 2*(f0**2 + fL**2)/(2*np.pi)*(np.log(T/(2*np.pi)) + 1)/T
        inside = integrate.quad(lambda t: abs(Fhat(c, t)[0])**2, -gamma1, gamma1, limit=400)[0]/(2*np.pi)
        total = np.sum(c**2)
        print(f"  k={k}: eigenvalue={ev[k]:.6e}   zero sum (300 zeros)={zs:.6e} (+tail~{tail:.1e})   ratio={zs/ev[k]:.6f}   Fourier mass in |tau|<gamma_1: {inside/total:.12f}   endpoint values f(0)={np.sum(c*nu):.2e}, f(L)={np.sum(c*nu*M['sgn']):.2e}")
        res[f'L{L}_k{k}'] = dict(eig=float(ev[k]), zero_sum=float(zs), tail=float(tail), mass_inside=float(inside/total))
json.dump(res, open('chk6.json', 'w'), indent=1)
