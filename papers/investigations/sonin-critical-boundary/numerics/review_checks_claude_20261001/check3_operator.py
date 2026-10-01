"""
End-to-end operator check of Lemma phase-trace (eq. L-trace) and the critical limit
(eq. local-Llimit) for the ACTUAL zeta phase v_sigma, by discretization.

Setup: periodic box [-X, X), N points, spacing dx.  V = v_sigma(D) as a circulant via FFT,
P = 1_{x>=0}, chi = 1 - P, J = reflection x -> -x, b(D) = Gaussian frequency multiplier
centred at gamma_1 with |b(gamma_1)| = 1.

On a circle the indicator P has TWO interfaces (x=0 and the seam x=+-X); the second is the
mirror image of the first (symbol v <-> conj v, L <-> C^2), and in finite dimensions
Tr(a(D)(V^*PV-P)) = 0 identically.  So the line identity

   Tr(b L b^*) = int |b|^2 phi' dt/2pi + Tr(b C^2 b^*) + 2 Re Tr(C T P a chi)        (eq. L-trace)

is tested by LOCALIZING every trace to the interface at x=0: sum over basis vectors with
|x_k| < X/2 and cut outputs with Theta = 1_{|x|<X/2}.  Kernels decay like exp(-eps|x|),
eps = sigma-1/2, so X/2 >> 1/eps makes the seam contribution negligible.

Reported for sigma in {0.8, 0.7, 0.6, 0.55}:
   LHS = Tr_0(b L b^*),  bulk, Tr_0(b C^2 b^*), crossing,  RHS = bulk + C^2 + crossing,
   and the top squared singular values of the localized Hankel block Theta chi V P b^* Theta.
Expected: LHS ~ RHS (identity), LHS -> |b(gamma_1)|^2 = 1, C^2 and crossing -> 0.
"""
import numpy as np, mpmath as mp, time, sys
mp.mp.dps = 15
pi = mp.pi

X  = float(sys.argv[1]) if len(sys.argv) > 1 else 150.0
dx = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1
N  = int(round(2*X/dx))
x  = -X + dx*np.arange(N)
t  = 2*np.pi*np.fft.fftfreq(N, d=dx)          # FFT frequency grid (radians per unit x)
g1 = float(mp.im(mp.zetazero(1)))

def v_sigma_grid(sigma):
    vals = np.empty(N, dtype=complex)
    cache = {}
    for i, ti in enumerate(t):
        key = abs(ti)
        if key not in cache:
            tt = mp.mpf(key)
            z = mp.zeta(sigma + 1j*tt)
            gam = mp.gamma(mp.mpf('0.25') + 1j*tt/2) / mp.gamma(mp.mpf('0.25') - 1j*tt/2)
            cache[key] = complex(gam * mp.power(pi, -1j*tt) * z / mp.conj(z))
        vals[i] = cache[key] if ti >= 0 else np.conj(cache[key])
    # Nyquist point (m=-N/2, no partner): force a real value so that v(-t)=conj v(t) exactly
    if N % 2 == 0:
        vals[N//2] = 1.0
    return vals

def multiplier_matrix(m):
    """dense matrix of the Fourier multiplier m(D) on the periodic grid"""
    return np.fft.ifft(m[:, None]*np.fft.fft(np.eye(N), axis=0), axis=0)

def gamma_inf(tt):
    return mp.re(mp.digamma(mp.mpf('0.25') + 1j*mp.mpf(tt)/2)) - mp.log(pi)
def phi_prime(sigma, tt):
    s = sigma + 1j*mp.mpf(tt)
    return gamma_inf(tt) + 2*mp.re(mp.zeta(s, derivative=1)/mp.zeta(s))

# frequency multipliers for the source
b_sym  = np.exp(-(t-g1)**2/2)       # b(t), real, b(gamma_1)=1
a_sym  = b_sym**2                   # a = |b|^2
Bbar   = multiplier_matrix(b_sym)   # b(D)^* = conj(b)(D) = b(D) since b real
A      = multiplier_matrix(a_sym)
P      = np.diag((x >= 0).astype(float))
chi    = np.eye(N) - P
J      = np.zeros((N, N)); J[(-np.arange(N)) % N, np.arange(N)] = 1.0   # x_k -> -x_k  (index k -> -k mod N)
Theta  = np.diag((np.abs(x) < X/2).astype(float))
idx0   = np.abs(x) < X/2

print(f"grid: X={X}, dx={dx}, N={N}, dt={t[1]:.4f}, tmax={t.max():.2f}; gamma_1={g1:.5f}")
print(f"{'sigma':>6} {'LHS Tr0(bLb*)':>14} {'bulk':>10} {'Tr0(bC^2b*)':>12} {'2Re cross':>10} {'RHS':>10} {'LHS-RHS':>9}   top s_i^2 of localized Hankel block")
for sigma in ([float(s) for s in sys.argv[3].split(",")] if len(sys.argv) > 3 else [0.8, 0.7, 0.6, 0.55]):
    t0 = time.time()
    sg = mp.mpf(sigma)
    v  = v_sigma_grid(sg)
    V  = multiplier_matrix(v)
    F  = J @ V                       # F = J v(D)
    # sanity: F selfadjoint unitary involution
    err_inv = np.linalg.norm(F @ F - np.eye(N)) / np.sqrt(N)
    err_sa  = np.linalg.norm(F - F.conj().T) / np.sqrt(N)
    T  = chi @ F @ P
    C  = chi @ F @ chi
    # localized traces at the interface x=0
    M_L  = Theta @ chi @ V @ P @ Bbar          # chi V P b^*   (L = (chi V P)^*(chi V P))
    M_C  = Theta @ P @ V @ chi @ Bbar          # P V chi b^*   (C^2 = (P V chi)^*(P V chi))
    lhs  = np.sum(np.abs(M_L[:, idx0])**2)
    trC2 = np.sum(np.abs(M_C[:, idx0])**2)
    Xa   = P @ A @ chi
    cross_mat = C @ T @ Xa
    cross = 2*np.real(np.trace(cross_mat[np.ix_(idx0, idx0)]))
    # bulk term by quadrature (Poisson-type peak at gamma_1 resolved by splitting)
    eps = sigma - 0.5
    pts = [g1-8, g1-2, g1-1, g1-10*eps, g1-eps, g1, g1+eps, g1+10*eps, g1+1, g1+2, g1+8]
    bulk = float(mp.quad(lambda tt: mp.exp(-(tt-g1)**2)*phi_prime(sg, tt)/(2*pi), pts))
    rhs = bulk + trC2 + cross
    sv = np.linalg.svd(M_L[np.ix_(idx0, idx0)], compute_uv=False)
    print(f"{sigma:6.2f} {lhs:14.6f} {bulk:10.6f} {trC2:12.6f} {cross:10.6f} {rhs:10.6f} {lhs-rhs:9.2e}   {np.round(sv[:5]**2, 4)}   [F^2-I: {err_inv:.1e}, F-F*: {err_sa:.1e}, {time.time()-t0:.0f}s]")
