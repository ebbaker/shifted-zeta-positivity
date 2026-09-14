"""
Check 3: assemble the full arithmetic operator W_L in the cosine basis (first Kp modes),
using closed forms independent of the paper's scripts, and test

  (i)   central-row formula r_h(q) against the exact chain-matrix norm and max row sum;
  (ii)  compression of the prime term  >= -(log p) r_h(q)   and of R_L >= -beta_L;
  (iii) the certified cutoff at L=1 (N=4) and at L=2, and  H_K - Lambda_K >= 0;
  (iv)  parity decoupling of W, hence of S;
  (v)   floating-point Galerkin enclosures U_K = A - B^T H_K^{-1} B and truncated L_K,
        their convergence in K, eigenvalues of S_1 (and S_2) -- DIAGNOSTIC ONLY;
  (vi)  minimum eigenvalue of the full compression W_K (Weil positivity sanity check).
"""
import numpy as np, mpmath as mp, json
from scipy.special import digamma
from sympy import primerange
mp.mp.dps = 30
out = {}

gammaE = float(mp.euler); psi14 = float(mp.digamma(0.25)); w0 = psi14 - np.log(np.pi)

def a_k(k): return 2*k + 0.5

# ---------- (i) central-row formula ---------------------------------------------
def r_h(h, q):
    return q/(1-q)*(2 - q**((h-1)//2) - q**(-(-(h-1)//2)))   # floor and ceil of (h-1)/2
worst = 0.0
for h in range(1, 40):
    for q in [0.9, 0.7, 2**-0.5, 3**-0.5, 0.3, 0.05]:
        M = np.array([[q**abs(i-j) if i != j else 0.0 for j in range(h)] for i in range(h)])
        rows = M.sum(1).max()
        nrm = np.linalg.norm(M, 2) if h > 0 else 0
        assert abs(rows - r_h(h, q)) < 1e-12, (h, q, rows, r_h(h, q))
        assert nrm <= r_h(h, q) + 1e-12
        worst = max(worst, nrm/r_h(h, q) if h > 1 else 0)
out['central_row_formula'] = 'exact match of max row sum for h<40; operator norm <= r_h; max norm/r_h = %.4f' % worst
print("(i) central row formula OK; max ||chain||/r_h =", round(worst, 4))

# ---------- assembly of W_L in cosine basis ---------------------------------------
def assemble(L, Kp, primes_powers):
    j = np.arange(Kp); om = j*np.pi/L
    nu = np.full(Kp, np.sqrt(2/L)); nu[0] = 1/np.sqrt(L)
    # b_j = Re psi(1/4 + i om/2) - psi(1/4)
    bj = digamma(0.25 + 0.5j*om).real - psi14
    # boundary entries: rational part via digamma sums
    z = 0.25 + 0.5j*om
    N_im = digamma(z).imag                                   # Im psi
    N_p = np.array([float(mp.re(mp.polygamma(1, mp.mpc(0.25, 0.5*w)))) for w in om])  # Re psi'
    with np.errstate(divide='ignore', invalid='ignore'):
        S1 = np.where(om > 0, N_im/(2*om), float(mp.polygamma(1, 0.25))/4)   # sum_k 1/(a_k^2+om^2)
    Rdiag = np.where(om > 0, N_im/(4*om) + N_p/8, float(mp.polygamma(1, 0.25))/4)  # sum a^2/(a^2+om^2)^2
    om2 = om**2
    num = om2[:, None]*S1[:, None] - om2[None, :]*S1[None, :]
    den = om2[:, None] - om2[None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        Rrat = num/den
    np.fill_diagonal(Rrat, Rdiag)
    # exponential part sum_k e^{-a_k L} a_k^2 g_k g_k^T
    ks = np.arange(0, 80); ak = a_k(ks)
    G = 1.0/(ak[None, :]**2 + om2[:, None])                   # Kp x 80
    wk = np.exp(-ak*L)*ak**2
    X = (G*wk[None, :]) @ G.T
    sgn = np.where(j % 2 == 0, 1.0, -1.0)
    kij = 2*np.outer(nu, nu)*(Rrat - sgn[None, :]*X)
    parity = (sgn[:, None] == sgn[None, :]).astype(float)
    kij *= parity
    # pole coefficients
    def Jj(sig):
        return sig*(sgn*np.exp(sig*L) - 1)/(sig**2 + om2)
    cj = nu/2*(np.exp(-L/4)*Jj(0.5) + np.exp(L/4)*Jj(-0.5))
    sj = nu/2*(np.exp(-L/4)*Jj(0.5) - np.exp(L/4)*Jj(-0.5))
    pole = 2*np.outer(cj, cj) - 2*np.outer(sj, sj)
    # shift entries
    def I_(lam, phi, aa, bb):
        with np.errstate(divide='ignore', invalid='ignore'):
            v = (np.sin(lam*bb + phi) - np.sin(lam*aa + phi))/lam
        return np.where(np.abs(lam) < 1e-14, (bb-aa)*np.cos(phi), v)
    def t_mat(d):
        wi = om[:, None]; wj = om[None, :]
        return np.outer(nu, nu)/2*(I_(wi-wj, wj*d, d, L) + I_(wi+wj, -wj*d, d, L))
    prime = np.zeros((Kp, Kp))
    for p, m in primes_powers:
        d = m*np.log(p); T = t_mat(d)
        prime -= np.log(p)*p**(-m/2)*(T + T.T)
    W = np.diag(bj + w0) + kij + pole + prime
    return dict(W=W, bj=bj, kij=kij, pole=pole, prime=prime, cj=cj, sj=sj, nu=nu, om=om, sgn=sgn)

def active_powers(L):
    pp = []
    for p in primerange(2, int(np.exp(L))+2):
        m = 1
        while m*np.log(p) < L:
            pp.append((int(p), m)); m += 1
    return pp

def beta_L(L):
    val = -w0 + 2*np.sinh(L/2) - L
    for p in primerange(2, int(np.exp(L))+2):
        if np.log(p) < L:
            h = int(np.ceil(L/np.log(p)))
            val += np.log(p)*r_h(h, p**-0.5)
    return val

for L, Kp in [(1.0, 6000), (2.0, 6000)]:
    print(f"\n================ L = {L} ================")
    pp = active_powers(L); print("active prime powers:", pp)
    M = assemble(L, Kp, pp); W = M['W']
    print("symmetry defect:", np.abs(W - W.T).max())
    # (ii) prime lower bound per prime, on the compression (min eigen of compression >= operator bound)
    for p in sorted(set(q for q, _ in pp)):
        mm = [(q, m) for q, m in pp if q == p]
        Mp = assemble(L, 1500, mm)['prime']
        lam = np.linalg.eigvalsh(Mp).min()
        h = int(np.ceil(L/np.log(p))); bound = -np.log(p)*r_h(h, p**-0.5)
        print(f"  prime {p}: min eig of 1500-mode compression = {lam:.6f}   bound -(log p) r_h = {bound:.6f}   ok={lam >= bound - 1e-10}")
    RL = w0*np.eye(1500) + M['pole'][:1500, :1500] + M['prime'][:1500, :1500]
    lamR = np.linalg.eigvalsh(RL).min(); bL = beta_L(L)
    print(f"  R_L compression min eig = {lamR:.6f}   -beta_L = {-bL:.6f}   ok={lamR >= -bL - 1e-10}")
    out[f'L{L}_RL_min_vs_minus_beta'] = (lamR, -bL)
    # (iii) cutoff
    bj = M['bj']; N = int(np.argmax(bj > bL + 1/16))
    print(f"  beta_L = {bL:.6f}; smallest j with b_j > beta_L+1/16: N = {N}  (b_{N-1}={bj[N-1]:.5f}, b_N={bj[N]:.5f}, threshold={bL+1/16:.5f})")
    Lam = np.diag(bj[N:] - bL)
    H = W[N:, N:]
    lamHL = np.linalg.eigvalsh(H[:1500-N, :1500-N] - Lam[:1500-N, :1500-N]).min()
    print(f"  min eig of (H - Lambda) on 1500-mode compression = {lamHL:.6f}  (>=0 required)")
    out[f'L{L}_cutoff'] = dict(beta=bL, N=N, H_minus_Lambda_min=lamHL)
    # (iv) parity decoupling
    sgn = M['sgn']; mixed = np.abs(W[np.ix_(sgn > 0, sgn < 0)]).max()
    print(f"  max |even-odd entry| of W = {mixed:.2e}")
    # (vi) Weil positivity sanity: min eig of full compression
    for K in [50, 200, 1000, 3000]:
        ev = np.linalg.eigvalsh(W[:K, :K])
        print(f"  min eig of W compressed to {K} modes: {ev[0]:.8f}  (next: {ev[1]:.6f}, {ev[2]:.6f})")
    # (v) Schur enclosures
    A = W[:N, :N]
    rec = []
    for K in [N+16, N+60, 200, 500, 1000, 2000, 4000, Kp-1]:
        if K <= N: continue
        HK = W[N:K, N:K]; BK = W[N:K, :N]
        Y = np.linalg.solve(HK, BK)
        U = A - BK.T @ Y
        # truncated residual Gram: rows K..Kp
        R = W[K:, :N] - W[K:, N:K] @ Y
        gram = R.T @ R
        dK = bj[K] - bL
        Lmat = U - gram/dK
        eU = np.linalg.eigvalsh((U+U.T)/2); eL = np.linalg.eigvalsh((Lmat+Lmat.T)/2)
        rec.append(dict(K=K, eigU=eU.tolist(), eigL=eL.tolist(), gap=float(np.linalg.norm(gram, 2)/dK),
                        resid_norm2=float(np.linalg.norm(R, 2)**2), dK=float(dK)))
        print(f"  K={K:5d}: eig(U_K) = {np.array2string(eU, precision=6)}   eig(L_K^trunc) = {np.array2string(eL, precision=6)}   gap={np.linalg.norm(gram,2)/dK:.2e}  |R_K|^2={np.linalg.norm(R,2)**2:.3e}")
    out[f'L{L}_schur'] = rec
    # even/odd blocks at the largest K
    K = Kp-1; HK = W[N:K, N:K]; BK = W[N:K, :N]; U = A - BK.T @ np.linalg.solve(HK, BK)
    ev_idx = [i for i in range(N) if i % 2 == 0]; od_idx = [i for i in range(N) if i % 2 == 1]
    print("  S^even eigs:", np.linalg.eigvalsh(U[np.ix_(ev_idx, ev_idx)]), "  S^odd eigs:", np.linalg.eigvalsh(U[np.ix_(od_idx, od_idx)]) if od_idx else None)
    print("  A eigs:", np.linalg.eigvalsh(A))
    out[f'L{L}_A_eigs'] = np.linalg.eigvalsh(A).tolist()

json.dump(out, open('chk3.json', 'w'), indent=1, default=float)
