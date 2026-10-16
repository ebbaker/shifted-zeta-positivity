"""
Weil form Q_{0,L} on L^2(-L/2,L/2), orthonormal sine basis, CLOSED FORM.

All three families of archimedean integrals are summed in closed form by
expanding n(r) = e^{-r/2}/(1-e^{-2r}) = sum_{q>=0} e^{-(2q+1/2) r} and splitting
each term into a q-sum that telescopes into digamma/trigamma and a remainder
that is geometric in q.  Nothing is quadrature; precision is set by mp.mp.dps.

Convention: f supported in (-L/2, L/2); prime sum over n < e^L.
(Zhu arXiv:2608.24827 supports f in (-L,L): Zhu's L is half of this L.)
"""
import mpmath as mp

def sieve(n):
    s = [True]*(n+1); s[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if s[i]: s[i*i::i] = [False]*len(s[i*i::i])
    return [i for i, v in enumerate(s) if v]

def prime_comb(L):
    out = []
    for p in sieve(int(mp.e**L)+2):
        m = 1
        while m*mp.log(p) < L:
            out.append((m*mp.log(p), mp.log(p)*mp.mpf(p)**(-mp.mpf(m)/2))); m += 1
    return out

def geo_sum(term, L):
    """sum_{q>=0} term(beta=2q+1/2); each term carries e^{-beta L}, so geometric."""
    tot = mp.mpf(0); eps = mp.mpf(10)**(-mp.mp.dps-10)
    q = 0
    while True:
        t = term(2*q + mp.mpf(1)/2)
        tot += t
        if q > 2 and abs(t) < eps*max(abs(tot), mp.mpf(1)):
            return tot
        q += 1
        if q > 20000: return tot

class WeilForm:
    def __init__(self, L, N):
        self.L = mp.mpf(L); self.N = N; self.alpha = mp.pi/self.L
        L, al = self.L, self.alpha
        self.psi14 = mp.digamma(mp.mpf(1)/4)

        # A_m = int_0^L sin(m alpha r) n(r) dr
        self.A = [mp.mpf(0)]
        for m in range(1, 2*N+1):
            c = m*al
            head = mp.im(mp.digamma(mp.mpf(1)/4 + 1j*c/2))/2
            tail = -(-1)**m * c * geo_sum(lambda b: mp.e**(-b*L)/(b**2+c**2), L)
            self.A.append(head + tail)

        # B_k = int_0^L [(L-r) cos(k alpha r) - L] n(r) dr
        self.B = [mp.mpf(0)]
        for k in range(1, N+1):
            c = k*al
            head = (-L/2*(mp.re(mp.digamma(mp.mpf(1)/4+1j*c/2)) - self.psi14)
                    - mp.re(mp.psi(1, mp.mpf(1)/4+1j*c/2))/4)
            sub = geo_sum(lambda b: mp.e**(-b*L)*(-(-1)**k*(b**2-c**2)/(b**2+c**2)**2 - L/b), L)
            self.B.append(head - sub)

        # C = int_0^L (e^{-r/2} - 1) n(r) dr
        head = (self.psi14 - mp.digamma(mp.mpf(1)/2))/2
        sub = geo_sum(lambda b: mp.e**(-(b+mp.mpf(1)/2)*L)/(b+mp.mpf(1)/2) - mp.e**(-b*L)/b, L)
        self.C = head - sub

        self.tail = mp.atanh(mp.e**(-L))
        self.const = -(mp.log(4*mp.pi) + mp.euler)

        self.Ep, self.Em = [mp.mpf(0)], [mp.mpf(0)]
        for j in range(1, N+1):
            for beta, st in ((mp.mpf(1)/2, self.Ep), (-mp.mpf(1)/2, self.Em)):
                I = j*al*(1-(-1)**j*mp.e**(beta*L))/(beta**2+(j*al)**2)
                st.append(mp.sqrt(2/L)*mp.e**(-beta*L/2)*I)

    def S(self, j, k, u):
        L, al = self.L, self.alpha
        if (j-k) % 2: return mp.mpf(0)
        if j == k:
            return 2/L*((L-u)*mp.cos(k*al*u) + mp.sin(k*al*u)/(k*al))
        sj, sk = mp.sin(j*al*u), mp.sin(k*al*u)
        return 2/mp.pi*((sk-sj)/(j-k) + (sj+sk)/(j+k))

    def Sint(self, j, k):
        if (j-k) % 2: return mp.mpf(0)
        if j == k:  return 2/self.L*(self.B[k] + self.A[k]/(k*self.alpha))
        return 2/mp.pi*((self.A[k]-self.A[j])/(j-k) + (self.A[j]+self.A[k])/(j+k))

    def matrix(self, comb, parity, scale=1, arch_only=False):
        idx = [j for j in range(1, self.N+1) if (j-1) % 2 == parity]
        n = len(idx); M = mp.zeros(n, n)
        for a, j in enumerate(idx):
            for b in range(a, n):
                k = idx[b]; d = 1 if j == k else 0
                val = (self.Ep[j]*self.Em[k] + self.Em[j]*self.Ep[k]
                       + d*self.const
                       - (self.Sint(j, k) - 2*d*self.C) + 2*d*self.tail)
                if comb and not arch_only:
                    val -= scale*mp.fsum(w*self.S(j, k, dd) for dd, w in comb)
                M[a, b] = val; M[b, a] = val
        return M, idx

def lam_min(M, iters=60):
    """Smallest eigenvalue by inverse iteration on a Cholesky factor (M must be PD)."""
    n = M.rows
    if n == 0: return mp.inf
    Lc = mp.cholesky(M)                       # raises if not positive definite
    v = mp.matrix([mp.mpf(1)/(i+1) for i in range(n)])
    lam_old = None
    for it in range(iters):
        y = mp.lu_solve(M, v) if False else _chol_solve(Lc, v)
        nrm = mp.sqrt(mp.fsum(yi**2 for yi in y))
        v = y/nrm
        Mv = M*v
        lam = mp.fsum(v[i]*Mv[i] for i in range(n))
        if lam_old is not None and abs(lam-lam_old) < abs(lam)*mp.mpf(10)**(-mp.mp.dps+5):
            return lam
        lam_old = lam
    return lam

def _chol_solve(Lc, b):
    n = Lc.rows
    y = mp.matrix(n, 1)
    for i in range(n):
        y[i] = (b[i] - mp.fsum(Lc[i, j]*y[j] for j in range(i)))/Lc[i, i]
    x = mp.matrix(n, 1)
    for i in reversed(range(n)):
        x[i] = (y[i] - mp.fsum(Lc[j, i]*x[j] for j in range(i+1, n)))/Lc[i, i]
    return x
