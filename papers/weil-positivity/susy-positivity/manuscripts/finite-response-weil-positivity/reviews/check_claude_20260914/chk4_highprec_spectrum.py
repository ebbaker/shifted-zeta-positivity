"""
Check 4: high-precision (mpmath, 50 digits) assembly of the cosine compression W_K of the
arithmetic operator W_L at L=1 and L=2, to confirm that the cascade of tiny eigenvalues seen
in double precision is real, and to confirm the sign of the smallest eigenvalues of S_1.
Entries use the same closed forms as chk3 but in arbitrary precision.
"""
import mpmath as mp, sys, json, time
from sympy import primerange
mp.mp.dps = 50
psi14 = mp.digamma(mp.mpf(1)/4); w0 = psi14 - mp.log(mp.pi)
psip14 = mp.polygamma(1, mp.mpf(1)/4)

def r_h(h, q):
    return q/(1-q)*(2 - q**((h-1)//2) - q**(-(-(h-1)//2)))
def beta_L(L):
    val = -w0 + 2*mp.sinh(L/2) - L
    for p in primerange(2, int(mp.e**L)+2):
        if mp.log(p) < L:
            h = int(mp.ceil(L/mp.log(p))); val += mp.log(p)*r_h(h, mp.mpf(p)**-mp.mpf('0.5'))
    return val
def active_powers(L):
    pp = []
    for p in primerange(2, int(mp.e**L)+2):
        m = 1
        while m*mp.log(p) < L:
            pp.append((int(p), m)); m += 1
    return pp

def assemble(L, K):
    om = [j*mp.pi/L for j in range(K)]
    nu = [1/mp.sqrt(L)] + [mp.sqrt(2/L)]*(K-1)
    sgn = [1 if j % 2 == 0 else -1 for j in range(K)]
    z = [mp.mpc(mp.mpf(1)/4, w/2) for w in om]
    bj = [mp.re(mp.digamma(zz)) - psi14 for zz in z]
    Nim = [mp.im(mp.digamma(zz)) for zz in z]
    Np = [mp.re(mp.polygamma(1, zz)) for zz in z]
    S1 = [Nim[j]/(2*om[j]) if j > 0 else psip14/4 for j in range(K)]
    Rdiag = [Nim[j]/(4*om[j]) + Np[j]/8 if j > 0 else psip14/4 for j in range(K)]
    ak = [2*k + mp.mpf(1)/2 for k in range(120)]
    wk = [mp.e**(-a*L)*a*a for a in ak]
    G = [[1/(a*a + w*w) for a in ak] for w in om]
    W = mp.zeros(K, K)
    # pole coefficients
    def Jj(j, sig): return sig*(sgn[j]*mp.e**(sig*L) - 1)/(sig*sig + om[j]**2)
    cj = [nu[j]/2*(mp.e**(-L/4)*Jj(j, mp.mpf(1)/2) + mp.e**(L/4)*Jj(j, -mp.mpf(1)/2)) for j in range(K)]
    sj = [nu[j]/2*(mp.e**(-L/4)*Jj(j, mp.mpf(1)/2) - mp.e**(L/4)*Jj(j, -mp.mpf(1)/2)) for j in range(K)]
    def I_(lam, phi, aa, bb):
        return (bb-aa)*mp.cos(phi) if lam == 0 else (mp.sin(lam*bb+phi) - mp.sin(lam*aa+phi))/lam
    pp = active_powers(L)
    pdata = [(mp.log(p)*mp.mpf(p)**(-mp.mpf(m)/2), m*mp.log(p)) for p, m in pp]
    for i in range(K):
        for j in range(i, K):
            v = mp.mpf(0)
            if sgn[i] == sgn[j]:
                if i == j: Rr = Rdiag[i]
                else: Rr = (om[i]**2*S1[i] - om[j]**2*S1[j])/(om[i]**2 - om[j]**2)
                X = mp.fsum(wk[k]*G[i][k]*G[j][k] for k in range(len(ak)))
                v += 2*nu[i]*nu[j]*(Rr - sgn[j]*X)
            v += 2*cj[i]*cj[j] - 2*sj[i]*sj[j]
            for coef, d in pdata:
                tij = nu[i]*nu[j]/2*(I_(om[i]-om[j], om[j]*d, d, L) + I_(om[i]+om[j], -om[j]*d, d, L))
                tji = nu[i]*nu[j]/2*(I_(om[j]-om[i], om[i]*d, d, L) + I_(om[i]+om[j], -om[i]*d, d, L))
                v -= coef*(tij + tji)
            if i == j: v += bj[j] + w0
            W[i, j] = v; W[j, i] = v
    return W, bj

out = {}
for L, Ks in [(mp.mpf(1), [40, 80]), (mp.mpf(2), [140, 200])]:
    bL = beta_L(L)
    for K in Ks:
        t0 = time.time()
        W, bj = assemble(L, K)
        E = mp.eigsy(W, eigvals_only=True)
        E = sorted(E)
        print(f"L={L} K={K} ({time.time()-t0:.0f}s): 12 smallest eigenvalues of W_K:")
        print("   ", [mp.nstr(e, 6) for e in E[:12]])
        out[f'L{int(L)}_K{K}_smallest'] = [mp.nstr(e, 12) for e in E[:14]]
        # S-matrix (Schur) with N from the certified rule
        N = next(j for j in range(K) if bj[j] > bL + mp.mpf(1)/16)
        if K > N + 4:
            A = W[0:N, 0:N]; B = W[N:K, 0:N]; H = W[N:K, N:K]
            Y = mp.inverse(H)*B
            U = A - B.T*Y
            EU = sorted(mp.eigsy((U+U.T)/2, eigvals_only=True))
            print(f"    N={N}; eig(U_K) smallest 8:", [mp.nstr(e, 6) for e in EU[:8]])
            out[f'L{int(L)}_K{K}_U_eigs'] = [mp.nstr(e, 12) for e in EU[:14]]
    sys.stdout.flush()
json.dump(out, open('chk4.json', 'w'), indent=1)
