"""
Ihara laboratory, core machinery.  Round 1.

Conventions (documented in the LAB note):

* Graphs are finite, connected, simple, (q+1)-regular. Ihara zeta via Bass:
      zeta_X(u)^{-1} = (1-u^2)^{|E|-|V|} det(I - A u + q u^2).
* Nontrivial eigenvalues: all lambda except q+1, and except -(q+1) when bipartite.
* Each nontrivial eigenvalue lambda (mult m) is encoded by theta with
  lambda = 2 sqrt(q) cos(theta)   (natural units: ordinates measured in units of log q):
    - tempered   |lambda| <= 2 sqrt(q):  theta = tau in [0, pi]           (on-line zeros)
    - exc+       lambda  >  2 sqrt(q):  theta = i*delta, delta>0          (real zeros, "Siegel type")
    - exc-       lambda  < -2 sqrt(q):  theta = pi - i*delta              (offset pair at height pi)
* Principal-tower truncation: only the principal zeros are kept (the 2 pi Z towers
  of the periodic s-plane picture -- the graph "gamma factor" -- are dropped; variant
  for round 2). Each eigenvalue deposits total weight 2m on atoms t = gamma^2:
    tempered: 2m at t = tau^2  (>0)
    exc+    : 2m at t = -delta^2  (<0, real)             -> Nevanlinna, not Stieltjes
    exc-    : m at each of t = (pi -/+ i delta)^2 (conj pair) -> not Nevanlinna (neg. squares)
* Herglotz response q_X(z) = sum_j w_j / (t_j - z).   Graph RH (Ramanujan) <=> Stieltjes.
* Krein string convention (fixed by the 1-mass computation and round-trip tested):
  string = [m_1, l_1, m_2, l_2, ..., m_N, l_N], first mass AT the measuring end x=0,
  Dirichlet wall at the far end;  q(z) = 1/(-z m_1 + 1/(l_1 + 1/(-z m_2 + ...)));
  q(0) = total length = sum l_k.
* Shifted family: h_omega(w) = sum_j m_j * [pair terms 1/(omega+w-i gamma)+1/(omega+w+i gamma)],
  q_omega(z) = h_omega(sqrt(-z))/sqrt(-z), principal branch.
* Screw function (zero side), pair rho = 1/2 +/- i gamma:
      T(t; gamma, omega) = sum_{s=+,-} (e^{b t} - 1 - b t)/b^2 ,  b = s*i*gamma - omega.
  Checks: omega=0, gamma real: T = 2(1-cos gamma t)/gamma^2; real pair gamma = i delta:
  leading growth e^{(delta-omega)t}/(delta-omega)^2 (Siegel shielding, positive).
"""
import numpy as np
from mpmath import mp, mpf, mpc, sqrt as msqrt, cos as mcos, acos as macos, cosh as mcosh, \
    acosh as macosh, exp as mexp, pi as mpi, polyroots, fabs, re as mre, im as mim, conj, eig, matrix

# ---------------------------------------------------------------- graphs
def K(n):
    A = np.zeros((n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            if i != j:
                A[i][j] = 1
    return A

def cycle_adj(n):
    A = np.zeros((n, n), dtype=object)
    for i in range(n):
        A[i][(i+1) % n] = 1; A[(i+1) % n][i] = 1
    return A

def prism(n):
    """C_n x K_2, 3-regular on 2n vertices."""
    A = np.zeros((2*n, 2*n), dtype=object)
    for i in range(n):
        for (a, b) in [(i, (i+1) % n), (n+i, n+(i+1) % n)]:
            A[a][b] = 1; A[b][a] = 1
        A[i][n+i] = 1; A[n+i][i] = 1
    return A

def moebius(n):
    """Moebius ladder: C_{2n} plus antipodal chords, 3-regular on 2n vertices."""
    N = 2*n
    A = cycle_adj(N)
    for i in range(n):
        A[i][i+n] = 1; A[i+n][i] = 1
    return A

def lcf(n, pattern, reps):
    """LCF notation on Hamiltonian cycle of length n."""
    A = cycle_adj(n)
    seq = pattern * reps
    assert len(seq) == n
    for i, k in enumerate(seq):
        j = (i + k) % n
        A[i][j] = 1; A[j][i] = 1
    return A

def petersen():
    A = np.zeros((10, 10), dtype=object)
    for i in range(5):
        A[i][(i+1) % 5] = A[(i+1) % 5][i] = 1          # outer C5
        A[5+i][5+(i+2) % 5] = A[5+(i+2) % 5][5+i] = 1  # inner pentagram
        A[i][5+i] = A[5+i][i] = 1                      # spokes
    return A

def heawood():   return lcf(14, [5, -5], 7)
def desargues(): return lcf(20, [5, -5, 9, -9], 5)
def cube():      return lcf(8, [3, -3], 4)

def Kbip(a, b):
    A = np.zeros((a+b, a+b), dtype=object)
    for i in range(a):
        for j in range(b):
            A[i][a+j] = A[a+j][i] = 1
    return A

def crown(n):
    """K_{n,n} minus a perfect matching, (n-1)-regular."""
    A = Kbip(n, n)
    for i in range(n):
        A[i][n+i] = A[n+i][i] = 0
    return A

def bipartite_double(A):
    n = A.shape[0]
    B = np.zeros((2*n, 2*n), dtype=object)
    B[:n, n:] = A; B[n:, :n] = A
    return B

def random_cubic(n, seed):
    """Pairing model with rejection; returns simple 3-regular adjacency."""
    rng = np.random.default_rng(seed)
    assert n % 2 == 0
    while True:
        stubs = np.repeat(np.arange(n), 3)
        rng.shuffle(stubs)
        A = np.zeros((n, n), dtype=object)
        ok = True
        for k in range(0, len(stubs), 2):
            i, j = int(stubs[k]), int(stubs[k+1])
            if i == j or A[i][j]:
                ok = False; break
            A[i][j] = A[j][i] = 1
        if ok and connected(A):
            return A

def connected(A):
    n = A.shape[0]
    seen = {0}; stack = [0]
    while stack:
        v = stack.pop()
        for w in range(n):
            if A[v][w] and w not in seen:
                seen.add(w); stack.append(w)
    return len(seen) == n

def is_bipartite(A):
    n = A.shape[0]; color = [None]*n; color[0] = 0; stack = [0]
    while stack:
        v = stack.pop()
        for w in range(n):
            if A[v][w]:
                if color[w] is None:
                    color[w] = 1 - color[v]; stack.append(w)
                elif color[w] == color[v]:
                    return False
    return True

def girth(A):
    """Shortest cycle via BFS from each vertex."""
    n = A.shape[0]; best = None
    for s in range(n):
        dist = [-1]*n; par = [-1]*n; dist[s] = 0; queue = [s]
        while queue:
            v = queue.pop(0)
            for w in range(n):
                if not A[v][w]:
                    continue
                if dist[w] == -1:
                    dist[w] = dist[v] + 1; par[w] = v; queue.append(w)
                elif w != par[v]:
                    c = dist[v] + dist[w] + 1
                    if best is None or c < best:
                        best = c
    return best

# ---------------------------------------------------------------- exact charpoly
def charpoly_exact(A):
    """Faddeev-LeVerrier over Python ints. Returns coeffs c[0..n], p(x)=sum c[k] x^k, c[n]=1."""
    n = A.shape[0]
    Ai = [[int(A[i][j]) for j in range(n)] for i in range(n)]
    M = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # M_0 = I
    c = [0]*(n+1); c[n] = 1
    for k in range(1, n+1):
        AM = [[sum(Ai[i][t]*M[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        tr = sum(AM[i][i] for i in range(n))
        assert tr % k == 0
        ck = -tr // k
        c[n-k] = ck
        M = [[AM[i][j] + (ck if i == j else 0) for j in range(n)] for i in range(n)]
    return c

from fractions import Fraction

def _pdiv(a, b):
    """Exact polynomial division a = q*b + r over Fraction; coeffs low->high."""
    a = [Fraction(x) for x in a]; b = [Fraction(x) for x in b]
    while a and a[-1] == 0: a.pop()
    while b and b[-1] == 0: b.pop()
    q = [Fraction(0)]*(max(len(a)-len(b)+1, 1))
    r = a[:]
    while len(r) >= len(b) and any(x != 0 for x in r):
        d = len(r) - len(b)
        cq = r[-1]/b[-1]
        q[d] = cq
        for i in range(len(b)):
            r[d+i] -= cq*b[i]
        while r and r[-1] == 0: r.pop()
    return q, r

def _pgcd(a, b):
    a = [Fraction(x) for x in a]; b = [Fraction(x) for x in b]
    while b and any(x != 0 for x in b):
        _, r = _pdiv(a, b)
        a, b = b, r
    # normalize monic
    while a and a[-1] == 0: a.pop()
    lead = a[-1]
    return [x/lead for x in a]

def _pderiv(a):
    return [Fraction(k)*a[k] for k in range(1, len(a))]

def squarefree_mult(c):
    """c: integer coeffs low->high. Returns list of (squarefree poly (Fraction), multiplicity)."""
    p = [Fraction(x) for x in c]
    out = []
    m = 1
    while len(p) > 1:
        g = _pgcd(p, _pderiv(p))
        sf, _ = _pdiv(p, g)          # squarefree part of p
        # factor of multiplicity exactly m: sf / squarefree-part-of-g
        if len(g) > 1:
            g_sf, _ = _pdiv(g, _pgcd(g, _pderiv(g)))
            f_m, _ = _pdiv(sf, _pgcd(sf, g_sf))
        else:
            f_m = sf
        if len(f_m) > 1:
            out.append((f_m, m))
        p = g
        m += 1
    return out

def eigen_data(A, dps=60):
    """Exact charpoly -> Yun square-free -> mp roots per factor -> [(lambda, mult)] descending."""
    mp.dps = dps
    c = charpoly_exact(A)
    out = []
    for f, m in squarefree_mult(c):
        # f coeffs low->high, squarefree: polyroots converges
        den = 1
        for x in f: den = den*x.denominator//__import__('math').gcd(den, x.denominator)
        fi = [int(x*den) for x in f]
        roots = polyroots([mpf(x) for x in reversed(fi)], maxsteps=400, extraprec=200)
        for r in roots:
            out.append((mre(r), m))
    return sorted(out, key=lambda p: -p[0])

# ---------------------------------------------------------------- spectral -> zero data
class GraphData:
    pass

def analyze(A, dps=60, name="?"):
    mp.dps = dps
    G = GraphData()
    G.name = name
    G.n = A.shape[0]
    G.m = sum(int(A[i][j]) for i in range(G.n) for j in range(i+1, G.n))
    degs = {sum(int(x) for x in A[i]) for i in range(G.n)}
    assert len(degs) == 1, "graph must be regular"
    G.deg = degs.pop(); G.q = G.deg - 1
    G.chi = G.n - G.m; G.b1 = 1 - G.chi
    G.bipartite = is_bipartite(A)
    G.girth = girth(A)
    G.eigs = eigen_data(A, dps)
    twosq = 2*msqrt(G.q)
    G.tempered, G.excP, G.excN = [], [], []   # (theta-data, mult)
    tol = mpf(10)**(-dps//2)
    for lam, mult in G.eigs:
        if fabs(lam - (G.q+1)) < tol:
            continue
        if G.bipartite and fabs(lam + (G.q+1)) < tol:
            continue
        x = lam/twosq
        if fabs(x) <= 1:
            G.tempered.append((macos(x), mult))            # tau in [0, pi]
        elif x > 1:
            G.excP.append((macosh(x), mult))               # delta > 0
        else:
            G.excN.append((macosh(-x), mult))              # delta > 0, theta = pi - i delta
    G.ramanujan = (not G.excP) and (not G.excN)
    return G

def atoms(G):
    """Atoms (t_j, w_j) of q_X; t may be negative (exc+) or complex-conjugate pairs (exc-)."""
    out = []
    for tau, m in G.tempered:
        out.append((tau**2, mpf(2*m)))
    for de, m in G.excP:
        out.append((-de**2, mpf(2*m)))
    for de, m in G.excN:
        th = mpi - mpc(0, 1)*de
        out.append((th**2, mpf(m)))
        out.append((conj(th**2), mpf(m)))
    return out

def gammas(G):
    """Zero-ordinate pair list [(gamma, mult, kind)]; pair means {gamma, -gamma}."""
    out = []
    for tau, m in G.tempered:
        out.append((tau, m, 'T'))
    for de, m in G.excP:
        out.append((mpc(0, 1)*de, m, 'P'))
    for de, m in G.excN:
        out.append((mpi - mpc(0, 1)*de, m, 'N'))   # + conjugate handled by Re in Psi / split in atoms
    return out

# ---------------------------------------------------------------- q, h, Psi
def q_of_z(G, z):
    return sum(w/(t - z) for (t, w) in atoms(G))

def h_omega(G, w, omega):
    """Paired log-derivative analogue at shift omega (real for real w)."""
    def pairterm(g):
        return 1/(omega + w - mpc(0, 1)*g) + 1/(omega + w + mpc(0, 1)*g)
    s = mpc(0)
    for (g, m, kind) in gammas(G):
        if kind == 'N':
            # atoms m at g^2 and m at conj(g)^2  <=>  (m/2)[pairterm(g) + pairterm(conj g)];
            # analytic in w (no Re!), real on the real axis, consistent with atoms() at omega=0.
            s += mpf(m)/2 * (pairterm(g) + pairterm(conj(g)))
        else:
            s += m * pairterm(g)
    return s

def q_omega(G, z, omega):
    w = msqrt(-z)
    return h_omega(G, w, omega)/w

def psi_pair(t, g, omega):
    """(e^{bt}-1-bt)/b^2 summed over b = +/- i g - omega."""
    tot = mpc(0)
    for sgn in (1, -1):
        b = sgn*mpc(0, 1)*g - omega
        tot += (mexp(b*t) - 1 - b*t)/b**2
    return tot

def Psi(G, t, omega=mpf(0)):
    s = mpf(0)
    for (g, m, kind) in gammas(G):
        v = psi_pair(t, g, omega)
        s += m * (mre(v) if kind == 'N' else mre(v))
    return s

# ---------------------------------------------------------------- string synthesis
def poly_from_atoms(ats):
    """q = P/Q with Q = prod (t_j - z), P = sum w_j prod_{i != j} (t_i - z). Coeffs low->high in z."""
    def pmul(a, b):
        out = [mpc(0)]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x*y
        return out
    Q = [mpc(1)]
    for (t, w) in ats:
        Q = pmul(Q, [t, mpc(-1)])
    P = [mpc(0)]*max(1, len(Q)-1)
    for j, (t, w) in enumerate(ats):
        prod = [mpc(w)]
        for i, (t2, w2) in enumerate(ats):
            if i != j:
                prod = pmul(prod, [t2, mpc(-1)])
        for i, x in enumerate(prod):
            P[i] += x
    return P, Q

def _deg(p, tol):
    d = len(p) - 1
    nrm = max(abs(x) for x in p)
    if nrm == 0:
        return 0
    while d > 0 and abs(p[d]) < tol*nrm:
        d -= 1
    return d

def string_from_q(P, Q, tol=None):
    """Stieltjes CF: q = 1/(-z m1 + 1/(l1 + 1/(-z m2 + ...))). Returns [m1, l1, m2, l2, ...].
    Coefficients may come out negative/complex-small for non-Stieltjes input; we return them raw."""
    if tol is None:
        tol = mpf(10)**(-mp.dps + 15)
    P = [mpc(x) for x in P]; Q = [mpc(x) for x in Q]
    out = []
    for _ in range(2*len(Q)):
        # step 1: mass:  1/q = Q/P = -z m + u,  m = -lead(Q)/lead(P) with dQ = dP+1
        dP, dQ = _deg(P, tol), _deg(Q, tol)
        if dQ != dP + 1:
            break
        mcoef = -Q[dQ]/P[dP]
        # R = Q + m z P  (so that 1/q + m z = R/P)
        R = [mpc(0)]*max(len(Q), len(P)+1)
        for i, x in enumerate(Q):
            R[i] += x
        for i, x in enumerate(P):
            R[i+1] += mcoef*x
        out.append(mcoef)
        dR = _deg(R, tol)
        if all(abs(x) < tol*max(abs(y) for y in Q) for x in R):
            break
        # step 2: length: u = R/P = 1/(l + v),  l = lead(P)/lead(R) with dP = dR
        dP2 = _deg(P, tol)
        if dP2 != dR:
            break
        lcoef = P[dP2]/R[dR]
        # S = P - l R ; v = S/R and next level q' = v  (v = 1/(-z m' + ...))
        S = [mpc(0)]*max(len(P), len(R))
        for i, x in enumerate(P):
            S[i] += x
        for i, x in enumerate(R):
            S[i] -= lcoef*x
        out.append(lcoef)
        dS = _deg(S, tol)
        if all(abs(x) < tol*max(abs(y) for y in P) for x in S):
            break
        P, Q = S, R
    return out

def q_from_string(coeffs, z):
    """Evaluate the CF q = 1/(-z m1 + 1/(l1 + 1/(-z m2 + ...))) from the far end inward."""
    val = None
    for k, c in enumerate(reversed(coeffs)):
        pos = len(coeffs) - 1 - k     # 0-based index in coeffs
        role_mass = (pos % 2 == 0)
        term = (-z*c) if role_mass else c
        val = term if val is None else term + 1/val
    return 1/val

def string_positions(coeffs):
    """[(x_k, m_k)] cumulative positions; total length; from [m1,l1,m2,l2,...]."""
    xs, x = [], mpf(0)
    for i in range(0, len(coeffs), 2):
        m = coeffs[i]
        xs.append((x, m))
        if i+1 < len(coeffs):
            x += mre(coeffs[i+1])
    return xs, x + (mre(coeffs[-1]) if len(coeffs) % 2 == 0 else 0)

# ---------------------------------------------------------------- Pick / negative squares
def pick_kappa(f, pts):
    """Number of negative eigenvalues of the Pick matrix of f at points pts in C+."""
    N = len(pts)
    Kmat = matrix(N, N)
    for i in range(N):
        for j in range(N):
            zi, zj = pts[i], pts[j]
            Kmat[i, j] = (f(zi) - conj(f(zj)))/(zi - conj(zj))
    E, _ = eig(Kmat)
    neg = sum(1 for e in E if mre(e) < -mpf(10)**(-mp.dps//3))
    return neg, sorted([mre(e) for e in E])

# ---------------------------------------------------------------- Bass validation
def bass_check(G, A, ntest=4, seed=1):
    """Check det(I - Au + q u^2) = u^n p_A((1+q u^2)/u) at random u; and K4 closed form."""
    mp.dps = 40
    n = G.n
    c = charpoly_exact(A)
    rng = np.random.default_rng(seed)
    worst = mpf(0)
    for _ in range(ntest):
        u = mpc(*(rng.uniform(-0.5, 0.5, 2)))
        M = matrix(n, n)
        for i in range(n):
            for j in range(n):
                M[i, j] = (1 if i == j else 0) - int(A[i][j])*u + (G.q*u**2 if i == j else 0)
        from mpmath import det
        lhs = det(M)
        x = (1 + G.q*u**2)/u
        rhs = u**n * sum(mpf(c[k])*x**k for k in range(n+1))
        worst = max(worst, abs(lhs - rhs)/max(mpf(1), abs(lhs)))
    return worst
