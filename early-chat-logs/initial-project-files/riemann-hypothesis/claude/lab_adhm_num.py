"""Numeric machinery for the ADHM matching test.

Data:  T_a  (a=0..3) real symmetric k x k,  lam in H^k  (k quaternions).
Reality of Delta^dag Delta forces (verified symbolically in lab_adhm_check.py):
    (i)  every T_a real symmetric;
    (ii) [T_0,T_a] - eps_abc [T_b,T_c] + Im_a(lam^dag lam) = 0   (a=1,2,3).
Then
    Delta^dag Delta = M(q) = C + |q|^2 I - 2 sum_a x_a T_a ,
    C = sum_a T_a^2 + Re(lam^dag lam)  >= 0  (automatically PSD).
The dictionary under test:  det M(q) = P_p(q) := p(x_0 + i r) p(x_0 - i r),
r = |Im q|.  Z(P_p) is exactly the zero set of the slice extension of p
(real roots -> points, conjugate pairs -> 2-spheres), and Z(det M) is the
real jumping locus of the associated twistor bundle.
"""
import numpy as np

EPS = np.zeros((3, 3, 3))
for (a, b, c), s in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
                     (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items():
    EPS[a, b, c] = s


def qmul_scalar(p, q):
    """Product of two quaternions given as length-4 arrays (1,i,j,k)."""
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
                     a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
                     a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


def qconj(p):
    return np.array([p[0], -p[1], -p[2], -p[3]])


def lam_gram(lam):
    """(lam^dag lam)_{ij} = conj(lam_i) lam_j ; returns array (4,k,k)."""
    k = lam.shape[0]
    G = np.zeros((4, k, k))
    for i in range(k):
        for j in range(k):
            G[:, i, j] = qmul_scalar(qconj(lam[i]), lam[j])
    return G


def unpack(z, k):
    """z -> (T list of 4 symmetric kxk, lam (k,4))."""
    n = k * (k + 1) // 2
    iu = np.triu_indices(k)
    T = []
    for a in range(4):
        S = np.zeros((k, k))
        S[iu] = z[a * n:(a + 1) * n]
        S = S + S.T - np.diag(np.diag(S))
        T.append(S)
    lam = z[4 * n:4 * n + 4 * k].reshape(k, 4)
    return T, lam


def nparams(k):
    return 4 * (k * (k + 1) // 2) + 4 * k


def com(X, Y):
    return X @ Y - Y @ X


# a -> (b, c, sign) with {b,c} = {1,2,3}\{a}, b<c, sign = eps_{abc}
_ADHM_TRIPLES = {1: (2, 3, +1), 2: (1, 3, -1), 3: (1, 2, +1)}


def adhm_residual(T, lam):
    """The three ADHM equations
         [T_0,T_a] - eps_abc [T_b,T_c] + Im_a(lam^dag lam) = 0,
    each an antisymmetric k x k matrix; returns strictly-upper entries."""
    G = lam_gram(lam)
    k = T[0].shape[0]
    iu = np.triu_indices(k, 1)
    out = []
    for a, (b, c, sgn) in _ADHM_TRIPLES.items():
        E = com(T[0], T[a]) - sgn * com(T[b], T[c]) + G[a]
        out.append(E[iu])
    return np.concatenate(out) if len(out) else np.array([])


def Cmat(T, lam):
    return sum(Ta @ Ta for Ta in T) + lam_gram(lam)[0]


def detM(T, lam, Q):
    """det M(q) at each row q of Q (shape (N,4))."""
    C = Cmat(T, lam)
    k = C.shape[0]
    s = (Q ** 2).sum(axis=1)
    M = (C[None, :, :] + s[:, None, None] * np.eye(k)[None, :, :]
         - 2.0 * sum(Q[:, a][:, None, None] * T[a][None, :, :] for a in range(4)))
    return np.linalg.det(M)


def P_target(roots, Q):
    """P_p(q) = prod_m (|q|^2 - 2 rho_m x_0 + rho_m^2), real for real p."""
    x0 = Q[:, 0]
    s = (Q ** 2).sum(axis=1)
    val = np.ones(len(Q), dtype=complex)
    for rho in roots:
        val = val * (s - 2.0 * rho * x0 + rho ** 2)
    return val.real


def sample_points(k, seed=0, mult=1):
    """Enough random points to pin a degree-2k polynomial in 4 variables."""
    from math import comb
    dim = comb(2 * k + 4, 4)
    rng = np.random.default_rng(seed)
    return rng.normal(size=(mult * dim, 4))


def make_residual(k, roots, Q, w_adhm=1.0):
    tgt = P_target(roots, Q)
    scale = max(np.abs(tgt).mean(), 1e-12)

    def F(z):
        T, lam = unpack(z, k)
        r1 = w_adhm * adhm_residual(T, lam)
        r2 = (detM(T, lam, Q) - tgt) / scale
        return np.concatenate([r1, r2])
    return F


def search(k, roots, ntrials=60, seed=0, scale=1.0, verbose=False):
    """Global-ish search: least_squares from many random starts."""
    from scipy.optimize import least_squares
    Q = sample_points(k, seed=seed)
    F = make_residual(k, roots, Q)
    rng = np.random.default_rng(seed + 1)
    best, bestz = np.inf, None
    for t in range(ntrials):
        z0 = rng.normal(scale=scale, size=nparams(k))
        try:
            sol = least_squares(F, z0, xtol=1e-14, ftol=1e-14, gtol=1e-14,
                                max_nfev=900)
        except Exception:
            continue
        c = float(np.sqrt(2 * sol.cost))
        if c < best:
            best, bestz = c, sol.x
        if verbose and t % 20 == 0:
            print(f"      trial {t:3d}  best residual so far {best:.3e}")
    return best, bestz
