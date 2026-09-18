#!/usr/bin/env python3
"""
The compressed shifted-Weil transfer V_{omega,L} assembled from the elementary
kernel of the Markov decomposition, and its contraction data, at L = log 3.
Standard library only; prints JSON to stdout.  Nothing here is a positivity
certificate; every number is computed at one horizon where the margin of the
localized Weil form is already known to be positive.

WHAT IS ASSEMBLED.  With s = 1/2 + p, a = 1/2 - omega, b = 1/2 + omega, the
shifted transfer K_omega(p) = xi(s-omega)/xi(s+omega) has causal kernel

    k_omega(t) = sum_{n < e^L} ct_n kappa_omega(t - log n),
    ct_n       = n^{omega-1/2} prod_{p | n} (1 - p^{-2 omega}),
    kappa_omega(tau) = kG(tau) - 4 omega b J_{-b}(tau) - 4 omega a J_a(tau),
    J_c(tau)   = int_0^tau e^{c (tau-u)} kG(u) du,
    kG(x)      = (2 pi^omega / Gamma(omega)) (2 sinh x)^{omega-1} e^{x/2},

i.e. a Beta-distributed continuous delay convolved with a multiplicative comb at
the integers, corrected by two exponential smoothings.  No zeta, no xi, no zeros
enter: only Gamma, sinh, exp and the integers below e^L.

THE SINGULARITY, HANDLED EXACTLY.  kG(tau) = tau^{omega-1} G(tau) with

    G(tau) = (2 pi^omega / Gamma(omega)) ((2 sinh tau)/tau)^{omega-1} e^{tau/2}

analytic on |tau| < pi, and J_c(tau) = tau^omega Psi_c(tau) with

    Psi_c(tau) = int_0^1 v^{omega-1} e^{c tau (1-v)} G(tau v) dv ,

so the whole single-atom kernel is kappa_omega(tau) = tau^{omega-1} Gh(tau) with

    Gh(tau) = G(tau) - 4 omega tau (b Psi_{-b}(tau) + a Psi_a(tau))

analytic on |tau| < pi.  Every integral against tau^{omega-1} is then done by
GAUSS-JACOBI quadrature for that exact weight (Golub-Welsch on the closed-form
Jacobi recurrence, alpha = 0, beta = omega - 1), which converges geometrically
and never forms tau explicitly by subtraction.  This replaces the substitution
tau = u^{1/omega} plus tanh-sinh rule of the exploratory mpmath programme, whose
intermediate quantities (tau ~ 1e-100 at omega = 0.01) are not representable in
double precision; here nothing underflows, because the weight carries the
singularity and the integrand is O(1).

WHAT IS CHECKED.

  A. The quadrature.  Gauss-Jacobi moments against 1/(omega+m) exactly, the
     Gauss-Legendre rule against exact polynomial moments, and the closed-form
     one-sided sine autocorrelations S_jk against direct quadrature.
  B. Self-consistency of the assembly: V, the mass, lambda_min(D) recomputed at
     a larger node count agree to the stated tolerance (geometric convergence).
  C. The mass.  int_0^L k_omega at five shifts, and its first-order limit
     (1 - int)/omega extrapolated to omega = 0 against the closed form of
     Proposition 2.3 of the contraction-margin note (poles, digamma, primes; no
     zeros).
  D. Contraction.  ||V_{omega,L}|| < 1 at every omega tested.
  E. The first-order law.  lambda_min(I - V^T V)/(2 omega) against m_L^(N), the
     smallest eigenvalue of the localized Weil form Q_{0,L} computed IN THE SAME
     BASIS by an independent closed-form assembler (the prime comb and three
     families of archimedean integrals summed by digamma/trigamma; no
     quadrature, no zeros), and the same law on the fixed vector e_1.
  F. The cumulative Cayley coordinate.  Z = (I-V)(I+V)^{-1}, P = (2/omega) Re Z:
     the exact congruence D = (omega/2)(I+V*)P(I+V), the accretivity P >= 0
     (the positive-real criterion), and lambda_min(P) = m_L^(N) + O(omega^2) --
     one order better in omega than the defect, because Z = tanh(omega G/2) is
     odd in omega.

  Counts below refer to finite test cases, not independent theorems.
"""
import json
import math

# ----------------------------------------------------------------- constants
EULER = 0.57721566490153286061
LOG_4PI = math.log(4.0 * math.pi)

# ------------------------------------------------- digamma / trigamma, complex
# psi(z) = log z - 1/(2z) - sum_{k>=1} B_2k / (2k z^2k), shifted up by recurrence.
_PSI_C = (1.0 / 12.0, -1.0 / 120.0, 1.0 / 252.0, -1.0 / 240.0, 1.0 / 132.0,
          -691.0 / 32760.0, 1.0 / 12.0, -3617.0 / 8160.0)
_PSI1_C = (1.0 / 6.0, -1.0 / 30.0, 1.0 / 42.0, -1.0 / 30.0, 5.0 / 66.0,
           -691.0 / 2730.0, 7.0 / 6.0, -3617.0 / 510.0)


def digamma(z):
    """psi(z) for complex or real z with Re z > 0."""
    z = complex(z)
    shift = 0.0 + 0.0j
    while abs(z) < 18.0:
        shift -= 1.0 / z
        z += 1.0
    w = 1.0 / (z * z)
    tail = 0.0 + 0.0j
    for c in reversed(_PSI_C):
        tail = (tail + c) * w
    return shift + complex_log(z) - 0.5 / z - tail


def trigamma(z):
    """psi'(z) for complex or real z with Re z > 0."""
    z = complex(z)
    shift = 0.0 + 0.0j
    while abs(z) < 18.0:
        shift += 1.0 / (z * z)
        z += 1.0
    w = 1.0 / (z * z)
    tail = 0.0 + 0.0j
    for c in reversed(_PSI1_C):
        tail = (tail + c) * w
    return shift + 1.0 / z + 0.5 * w + tail / z


def complex_log(z):
    return complex(math.log(abs(z)), math.atan2(z.imag, z.real))


# ------------------------------------------------------------ linear algebra
def jacobi_eigen(A, sweeps=60):
    """Eigenvalues and eigenvectors of a real symmetric matrix by cyclic Jacobi.

    Returns (eigenvalues ascending, eigenvectors as a list of columns).
    """
    n = len(A)
    M = [row[:] for row in A]
    Vv = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = 0.0
        for p in range(n - 1):
            for q in range(p + 1, n):
                off += M[p][q] * M[p][q]
        if off <= 1e-300:
            break
        converged = True
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = M[p][q]
                if abs(apq) <= 1e-18 * math.sqrt(abs(M[p][p] * M[q][q]) + 1e-300):
                    continue
                converged = False
                theta = (M[q][q] - M[p][p]) / (2.0 * apq)
                t = (1.0 if theta >= 0.0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    mkp, mkq = M[k][p], M[k][q]
                    M[k][p] = c * mkp - s * mkq
                    M[k][q] = s * mkp + c * mkq
                for k in range(n):
                    mpk, mqk = M[p][k], M[q][k]
                    M[p][k] = c * mpk - s * mqk
                    M[q][k] = s * mpk + c * mqk
                for k in range(n):
                    vkp, vkq = Vv[k][p], Vv[k][q]
                    Vv[k][p] = c * vkp - s * vkq
                    Vv[k][q] = s * vkp + c * vkq
        if converged:
            break
    pairs = sorted((M[i][i], i) for i in range(n))
    vals = [p[0] for p in pairs]
    vecs = [[Vv[k][p[1]] for k in range(n)] for p in pairs]
    return vals, vecs


def solve(A, B):
    """Solve A X = B for square A by Gaussian elimination with partial pivoting."""
    n = len(A)
    m = len(B[0])
    M = [A[i][:] + B[i][:] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[piv][col]) < 1e-300:
            raise ZeroDivisionError("singular matrix")
        M[col], M[piv] = M[piv], M[col]
        d = M[col][col]
        for r in range(n):
            if r == col:
                continue
            f = M[r][col] / d
            if f == 0.0:
                continue
            for k in range(col, n + m):
                M[r][k] -= f * M[col][k]
    return [[M[i][n + k] / M[i][i] for k in range(m)] for i in range(n)]


def matmul(A, B):
    n, p, q = len(A), len(B), len(B[0])
    Bt = [[B[k][j] for k in range(p)] for j in range(q)]
    return [[math.fsum(A[i][k] * Bt[j][k] for k in range(p)) for j in range(q)] for i in range(n)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

# ------------------------------------------------------------ quadrature
_GJ_CACHE, _GL_CACHE = {}, {}


def gauss_jacobi_unit(omega, n):
    """Nodes/weights for int_0^1 x^(omega-1) f(x) dx (total mass 1/omega).

    Golub-Welsch on the closed-form monic Jacobi recurrence with alpha = 0,
    beta = omega - 1, mapped from [-1,1] to [0,1].
    """
    key = (omega, n)
    if key in _GJ_CACHE:
        return _GJ_CACHE[key]
    al, be = 0.0, omega - 1.0
    diag, sub = [], []
    for k in range(n):
        d = 2.0 * k + al + be
        diag.append((be * be - al * al) / (d * (d + 2.0)))
        if k >= 1:
            num = 4.0 * k * (k + al) * (k + be) * (k + al + be)
            den = d * d * (d + 1.0) * (d - 1.0)
            sub.append(math.sqrt(num / den))
    T = [[0.0] * n for _ in range(n)]
    for i in range(n):
        T[i][i] = diag[i]
        if i:
            T[i][i - 1] = T[i - 1][i] = sub[i - 1]
    vals, vecs = jacobi_eigen(T)
    mu0 = 2.0 ** omega / omega
    nodes = [(1.0 + t) / 2.0 for t in vals]
    weights = [mu0 * vecs[i][0] * vecs[i][0] * 2.0 ** (-omega) for i in range(n)]
    order = sorted(range(n), key=lambda i: nodes[i])
    _GJ_CACHE[key] = ([nodes[i] for i in order], [weights[i] for i in order])
    return _GJ_CACHE[key]


def gauss_legendre_unit(n):
    """Nodes/weights for int_0^1 f(x) dx by Newton iteration on P_n."""
    if n in _GL_CACHE:
        return _GL_CACHE[n]
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, 0.0
            for j in range(1, n + 1):
                p0, p1 = ((2.0 * j - 1.0) * x * p0 - (j - 1.0) * p1) / j, p0
            dp = n * (x * p0 - p1) / (x * x - 1.0)
            dx = -p0 / dp
            x += dx
            if abs(dx) < 1e-16:
                break
        nodes.append((1.0 + x) / 2.0)
        weights.append(1.0 / ((1.0 - x * x) * dp * dp))
    order = sorted(range(n), key=lambda i: nodes[i])
    _GL_CACHE[n] = ([nodes[i] for i in order], [weights[i] for i in order])
    return _GL_CACHE[n]


# --------------------------------------------- localized Weil form Q_{0,L}
def sieve(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = [False] * len(s[i * i::i])
    return [i for i, v in enumerate(s) if v]


def prime_comb(L):
    """(m log p, log p * p^(-m/2)) for every prime power below e^L."""
    out = []
    for p in sieve(int(math.exp(L)) + 2):
        m = 1
        while m * math.log(p) < L:
            out.append((m * math.log(p), math.log(p) * p ** (-m / 2.0)))
            m += 1
    return out


def geo_sum(term, tol=1e-19, cap=4000):
    """sum_{q>=0} term(beta = 2q + 1/2); every term carries e^(-beta L)."""
    tot = 0.0
    for q in range(cap):
        t = term(2.0 * q + 0.5)
        tot += t
        if q > 2 and abs(t) < tol * max(abs(tot), 1.0):
            break
    return tot


class WeilForm(object):
    """Q_{0,L} on L^2(-L/2, L/2) in the orthonormal sine basis, closed form.

    Port of the Wilson-lines exploratory assembler weil_sine_basis.py to the
    standard library: n(r) = e^(-r/2)/(1 - e^(-2r)) is expanded as
    sum_{q>=0} e^(-(2q+1/2) r), each term splitting into a q-sum that telescopes
    into digamma/trigamma and a geometric remainder.  Nothing is quadrature.
    """

    def __init__(self, L, N):
        self.L, self.N = L, N
        self.alpha = math.pi / L
        al = self.alpha
        self.psi14 = digamma(0.25).real

        self.A = [0.0]
        for m in range(1, 2 * N + 1):
            c = m * al
            head = digamma(complex(0.25, c / 2.0)).imag / 2.0
            tail = -((-1.0) ** m) * c * geo_sum(lambda b: math.exp(-b * L) / (b * b + c * c))
            self.A.append(head + tail)

        self.B = [0.0]
        for k in range(1, N + 1):
            c = k * al
            z = complex(0.25, c / 2.0)
            head = -L / 2.0 * (digamma(z).real - self.psi14) - trigamma(z).real / 4.0
            sgn = (-1.0) ** k
            sub = geo_sum(lambda b: math.exp(-b * L) * (
                -sgn * (b * b - c * c) / (b * b + c * c) ** 2 - L / b))
            self.B.append(head - sub)

        head = (self.psi14 - digamma(0.5).real) / 2.0
        sub = geo_sum(lambda b: math.exp(-(b + 0.5) * L) / (b + 0.5) - math.exp(-b * L) / b)
        self.C = head - sub

        self.tail = math.atanh(math.exp(-L))
        self.const = -(LOG_4PI + EULER)

        self.Ep, self.Em = [0.0], [0.0]
        for j in range(1, N + 1):
            for beta, st in ((0.5, self.Ep), (-0.5, self.Em)):
                I = j * al * (1.0 - ((-1.0) ** j) * math.exp(beta * L)) / (beta * beta + (j * al) ** 2)
                st.append(math.sqrt(2.0 / L) * math.exp(-beta * L / 2.0) * I)

    def S(self, j, k, u):
        L, al = self.L, self.alpha
        if (j - k) % 2:
            return 0.0
        if j == k:
            return 2.0 / L * ((L - u) * math.cos(k * al * u) + math.sin(k * al * u) / (k * al))
        sj, sk = math.sin(j * al * u), math.sin(k * al * u)
        return 2.0 / math.pi * ((sk - sj) / (j - k) + (sj + sk) / (j + k))

    def Sint(self, j, k):
        if (j - k) % 2:
            return 0.0
        if j == k:
            return 2.0 / self.L * (self.B[k] + self.A[k] / (k * self.alpha))
        return 2.0 / math.pi * ((self.A[k] - self.A[j]) / (j - k) + (self.A[j] + self.A[k]) / (j + k))

    def matrix(self, comb, parity):
        idx = [j for j in range(1, self.N + 1) if (j - 1) % 2 == parity]
        n = len(idx)
        M = [[0.0] * n for _ in range(n)]
        for ai, j in enumerate(idx):
            for bi in range(ai, n):
                k = idx[bi]
                d = 1.0 if j == k else 0.0
                val = (self.Ep[j] * self.Em[k] + self.Em[j] * self.Ep[k]
                       + d * self.const
                       - (self.Sint(j, k) - 2.0 * d * self.C) + 2.0 * d * self.tail)
                if comb:
                    val -= math.fsum(w * self.S(j, k, dd) for dd, w in comb)
                M[ai][bi] = M[bi][ai] = val
        return M, idx

# --------------------------------------------------- the elementary kernel
def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def comb_weight(n, omega):
    """ct_n = n^(omega-1/2) prod_{p|n} (1 - p^(-2 omega))."""
    v = n ** (omega - 0.5)
    for p in prime_factors(n):
        v *= 1.0 - p ** (-2.0 * omega)
    return v


class Kernel(object):
    """kappa_omega(tau) = tau^(omega-1) Gh(tau), with Gh analytic on |tau| < pi."""

    def __init__(self, omega, n_inner):
        self.omega = omega
        self.a, self.b = 0.5 - omega, 0.5 + omega
        self.pref = 2.0 * math.pi ** omega / math.gamma(omega)
        self.xv, self.wv = gauss_jacobi_unit(omega, n_inner)

    def G(self, tau):
        """kG(tau) = tau^(omega-1) G(tau); G(0) = pi^omega 2^omega / Gamma(omega)."""
        if tau < 1e-6:
            r = 2.0 * (1.0 + tau * tau / 6.0 * (1.0 + tau * tau / 20.0))
        else:
            r = 2.0 * math.sinh(tau) / tau
        return self.pref * r ** (self.omega - 1.0) * math.exp(tau / 2.0)

    def Ghat(self, tau):
        g = self.G(tau)
        if tau <= 0.0:
            return g
        a, b = self.a, self.b
        s1 = math.fsum(w * math.exp(-b * tau * (1.0 - v)) * self.G(tau * v)
                       for v, w in zip(self.xv, self.wv))
        s2 = math.fsum(w * math.exp(a * tau * (1.0 - v)) * self.G(tau * v)
                       for v, w in zip(self.xv, self.wv))
        return g - 4.0 * self.omega * tau * (b * s1 + a * s2)


def kernel_nodes(omega, L, n_outer, n_inner):
    """(t, weight, Gh(tau)) for every quadrature node of int_0^L k_omega(t) . dt.

    One Gauss-Jacobi rule per atom, over that atom's whole support [log n, L),
    in its local coordinate tau = t - log n.
    """
    ker = Kernel(omega, n_inner)
    x, w = gauss_jacobi_unit(omega, n_outer)
    atoms = []
    n = 1
    while math.log(n) < L:
        atoms.append(n)
        n += 1
    nodes = []
    for m in atoms:
        ln = math.log(m)
        T = L - ln
        pref = comb_weight(m, omega) * T ** omega
        for xi, wi in zip(x, w):
            tau = T * xi
            nodes.append((ln + tau, pref * wi, ker.Ghat(tau)))
    return atoms, nodes


def transfer_matrix(L, N, nodes):
    """V_jk = int_0^L k_omega(t) S_jk(t) dt, S_jk the one-sided sine autocorrelation."""
    al = math.pi / L
    V = [[0.0] * N for _ in range(N)]
    rows = []
    for (t, wgt, gh) in nodes:
        c = wgt * gh
        sn = [0.0] + [math.sin(j * al * t) for j in range(1, N + 1)]
        cs = [0.0] + [math.cos(j * al * t) for j in range(1, N + 1)]
        rows.append((t, c, sn, cs))
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            sg = 1.0 if (j + k) % 2 == 0 else -1.0
            acc = []
            for (t, c, sn, cs) in rows:
                if j == k:
                    s = ((L - t) * cs[k] + sn[k] / (k * al)) / L
                else:
                    A = (sg * sn[k] - sn[j]) / ((j - k) * al)
                    B = (-sg * sn[k] - sn[j]) / ((j + k) * al)
                    s = (A - B) / L
                acc.append(c * s)
            V[j - 1][k - 1] = math.fsum(acc)
    return V


def first_order_tail(L):
    """Proposition 2.3: lim_{omega->0} omega^(-1) int_L^inf k_omega."""
    xs, ws = gauss_legendre_unit(64)
    def integrand(u):
        uu = u * L
        if uu < 1e-4:
            val = 0.5 - uu / 24.0 + uu ** 3 / 2880.0
        else:
            val = 2.0 * math.exp(-uu / 2.0) / (1.0 - math.exp(-2.0 * uu)) - 1.0 / uu
        return val
    arch = L * math.fsum(w * integrand(x) for x, w in zip(xs, ws))
    von = 0.0
    for p in sieve(int(math.exp(L)) + 2):
        m = 1
        while m * math.log(p) < L:
            von += math.log(p) * p ** (-m / 2.0)
            m += 1
    return (8.0 * math.sinh(L / 2.0) - 2.0 * von - math.log(2.0 * math.pi)
            - EULER - arch - math.log(L))


def kG_direct(omega, tau):
    """kG(tau) written directly; safe for tau bounded away from 0."""
    return (2.0 * math.pi ** omega / math.gamma(omega)) * (2.0 * math.sinh(tau)) ** (omega - 1.0) * math.exp(tau / 2.0)


def J_direct(ker, c, tau, nj=48, ng=48):
    """int_0^tau e^(c (tau-u)) kG(u) du by splitting at 1: Gauss-Jacobi then Gauss-Legendre.

    An independent route to the exponential smoothings, used to validate the Psi route
    and to reach tau beyond the analyticity radius pi of Gh.
    """
    om = ker.omega
    lo = min(tau, 1.0)
    x, w = gauss_jacobi_unit(om, nj)
    tot = lo ** om * math.fsum(wi * math.exp(c * (tau - lo * xi)) * ker.G(lo * xi)
                               for xi, wi in zip(x, w))
    if tau > 1.0:
        xs, ws = gauss_legendre_unit(ng)
        tot += (tau - 1.0) * math.fsum(wi * math.exp(c * (tau - u)) * kG_direct(om, u)
                                       for u, wi in zip([1.0 + (tau - 1.0) * xi for xi in xs], ws))
    return tot


def laplace_kappa(omega, p, panels=12, nj=48, ng=48):
    """int_0^inf e^(-p tau) kappa_omega(tau) dtau, by panels out to where the tail dies."""
    a, b = 0.5 - omega, 0.5 + omega
    ker = Kernel(omega, 48)
    lam = p - omega + 0.5
    x, w = gauss_jacobi_unit(omega, nj)
    tot = math.fsum(wi * math.exp(-p * xi) * (ker.G(xi) - 4.0 * omega * xi ** (1.0 - omega) * (
        b * J_direct(ker, -b, xi) + a * J_direct(ker, a, xi))) for xi, wi in zip(x, w))
    xs, ws = gauss_legendre_unit(ng)
    hi = 1.0 + 44.0 / lam
    edges = [1.0 + (hi - 1.0) * (i / panels) ** 2 for i in range(panels + 1)]
    for lo_, hi_ in zip(edges[:-1], edges[1:]):
        tot += (hi_ - lo_) * math.fsum(
            wi * math.exp(-p * u) * (kG_direct(omega, u) - 4.0 * omega * (
                b * J_direct(ker, -b, u) + a * J_direct(ker, a, u)))
            for u, wi in zip([lo_ + (hi_ - lo_) * xi for xi in xs], ws))
    return tot


def laplace_closed(omega, p):
    """pi^om Gamma((a+p)/2)/Gamma((b+p)/2) . (p+a)(p-b)/((p+b)(p-a)), the exact transform."""
    a, b = 0.5 - omega, 0.5 + omega
    arch = math.pi ** omega * math.gamma((a + p) / 2.0) / math.gamma((b + p) / 2.0)
    return arch * (p + a) * (p - b) / ((p + b) * (p - a))


def contraction_data(omega, L, N, n_out, n_in):
    atoms, nodes = kernel_nodes(omega, L, n_out, n_in)
    V = transfer_matrix(L, N, nodes)
    mass = math.fsum(w * g for (_, w, g) in nodes)
    Vt = transpose(V)
    VtV = matmul(Vt, V)
    ev, _ = jacobi_eigen(VtV)
    lam_min_D = 1.0 - ev[-1]
    norm_V = math.sqrt(ev[-1])
    ident = [[1.0 if i == j else 0.0 for j in range(N)] for i in range(N)]
    ImV = [[ident[i][j] - V[i][j] for j in range(N)] for i in range(N)]
    IpV = [[ident[i][j] + V[i][j] for j in range(N)] for i in range(N)]
    Z = transpose(solve(transpose(IpV), transpose(ImV)))      # Z = (I-V)(I+V)^{-1}
    P = [[(Z[i][j] + Z[j][i]) / omega for j in range(N)] for i in range(N)]
    evP, _ = jacobi_eigen(P)
    cong = matmul(matmul([[ident[i][j] + Vt[i][j] for j in range(N)] for i in range(N)], P),
                  IpV)
    resid = max(abs((ident[i][j] - VtV[i][j]) - 0.5 * omega * cong[i][j])
                for i in range(N) for j in range(N))
    nVe1 = math.fsum(V[j][0] ** 2 for j in range(N))
    return {"atoms": atoms, "mass": mass, "norm_V": norm_V, "lambda_min_D": lam_min_D,
            "lambda_min_P": evP[0], "congruence_residual": resid,
            "first_order_e1": (1.0 - nVe1) / (2.0 * omega)}


# --------------------------------------------------------------------- driver
L3, L5, L7 = math.log(3.0), math.log(5.0), math.log(7.0)
HORIZONS = (("log3", L3), ("log5", L5), ("log7", L7))
NQ_OUT, NQ_IN, NBASIS = 32, 32, 24

# 40-digit values from the exploratory Gauss-Jacobi programme
# numerics/exploratory/contraction_margin_gj.py, records cmgj_*.json.  Pinning the
# double-precision run to them is a check of this programme, not of those records.
REFERENCE = {
    ("log3", 0.002): (0.99874046830809098, 6.2542610028206e-08, 0.998834296359),
    ("log3", 0.01): (0.99373231868666348, 6.2813855951291e-08, 0.994676219006),
    ("log3", 0.02): (0.98753944334018039, 6.3156282872086e-08, 0.990606967310),
    ("log3", 0.05): (0.96940739694379632, 6.4210662473792e-08, 0.985816212307),
    ("log3", 0.1): (0.94066265817721137, 6.6085742918379e-08, 1.002027293860),
    ("log5", 0.002): (0.99871215738503, None, 0.997521024451),
    ("log5", 0.01): (0.99359401159384, None, 0.988141423216),
    ("log7", 0.002): (0.99833179840551, None, 0.997490589391),
    ("log7", 0.01): (0.99171746960386, None, 0.988227552176),
}
M_L_24 = 6.2475139834328e-08          # lambda_min(Q_{0,log3}) in the same 24-mode basis, 40 digits
CAYLEY_C = 0.038271496                # (lambda_min(P) - lambda_min(D)/2om)/(m_L om^2) at om = 0.1, 40 digits


class Group(object):
    """A named group of checks, each with its own tolerance; the group passes when all do."""

    def __init__(self, name, note=None):
        self.name, self.note = name, note
        self.checks, self.tables = [], {}

    def add(self, what, error, tol):
        self.checks.append({"what": what, "error": error, "tolerance": tol, "pass": error < tol})
        return self

    def assert_true(self, what, ok):
        self.checks.append({"what": what, "error": 0.0 if ok else 1.0, "tolerance": 0.5, "pass": bool(ok)})
        return self

    def out(self):
        d = {"name": self.name, "cases": len(self.checks),
             "worst_margin_against_own_tolerance": max(c["error"] / c["tolerance"] for c in self.checks),
             "pass": all(c["pass"] for c in self.checks), "checks": self.checks}
        if self.note:
            d["note"] = self.note
        d.update(self.tables)
        return d


def group_quadrature():
    g = Group("A. the quadrature rules and the closed-form sine autocorrelations")
    gj = {}
    for om in (0.002, 0.01, 0.05, 0.1):
        x, w = gauss_jacobi_unit(om, NQ_OUT)
        e = max(abs(math.fsum(wi * xi ** m for xi, wi in zip(x, w)) - 1.0 / (om + m)) * (om + m)
                for m in range(2 * NQ_OUT))
        gj["omega = %g" % om] = e
        g.add("Gauss-Jacobi moments against 1/(omega+m), m < %d, omega = %g" % (2 * NQ_OUT, om), e, 1e-10)
    xs, ws = gauss_legendre_unit(64)
    gl = max(abs(math.fsum(wi * xi ** m for xi, wi in zip(xs, ws)) - 1.0 / (m + 1.0)) * (m + 1.0)
             for m in range(128))
    g.add("Gauss-Legendre moments against 1/(m+1), m < 128", gl, 1e-12)
    al = math.pi / L3
    ee = lambda j, x: math.sqrt(2.0 / L3) * math.sin(j * al * (x + L3 / 2.0))
    sworst = 0.0
    for (j, k) in ((1, 1), (1, 2), (3, 5), (4, 4), (7, 12), (24, 23)):
        for t in (0.03, 0.3, 0.7, 1.05):
            lo, hi = -L3 / 2.0 + t, L3 / 2.0
            direct = (hi - lo) * math.fsum(wi * ee(j, lo + (hi - lo) * xi) * ee(k, lo + (hi - lo) * xi - t)
                                           for xi, wi in zip(xs, ws))
            sg = 1.0 if (j + k) % 2 == 0 else -1.0
            if j == k:
                s = ((L3 - t) * math.cos(k * al * t) + math.sin(k * al * t) / (k * al)) / L3
            else:
                s = ((sg * math.sin(k * al * t) - math.sin(j * al * t)) / ((j - k) * al)
                     + (sg * math.sin(k * al * t) + math.sin(j * al * t)) / ((j + k) * al)) / L3
            sworst = max(sworst, abs(direct - s))
    g.add("S_jk closed form against direct quadrature, 24 pairs (j,k,t)", sworst, 1e-13)
    g.tables = {"Gauss-Jacobi worst relative moment error": gj,
                "Gauss-Legendre worst relative moment error": gl,
                "S_jk worst absolute error": sworst}
    return g.out()


def group_kernel():
    g = Group("B. the elementary kernel: two routes to the smoothings, and the exact Laplace transform",
              "the Laplace transform is the archimedean Gamma-ratio times the rational pole "
              "repair; it uses Gamma alone, no zeta and no zeros, and is the identity that "
              "says the Beta kernel and the R_omega correction are the right ones")
    consistency, laplace = {}, {}
    for om in (0.01, 0.1):
        ker = Kernel(om, NQ_IN)
        a, b = 0.5 - om, 0.5 + om
        e = 0.0
        for tau in (0.02, 0.2, 0.6, 1.0, L3):
            viaPsi = ker.Ghat(tau)
            viaJ = ker.G(tau) - 4.0 * om * tau ** (1.0 - om) * (
                b * J_direct(ker, -b, tau) + a * J_direct(ker, a, tau))
            e = max(e, abs(viaPsi - viaJ) / abs(viaPsi))
        consistency["omega = %g" % om] = e
        g.add("Gh via Psi against Gh via the split rule, 5 points, omega = %g" % om, e, 1e-11)
        rows, we = {}, 0.0
        for p in (2.0, 3.0, 5.0, 8.0):
            got, want = laplace_kappa(om, p), laplace_closed(om, p)
            rel = abs(got - want) / abs(want)
            rows["p = %g" % p] = {"assembled": got, "closed form": want, "relative error": rel}
            we = max(we, rel)
        laplace["omega = %g" % om] = rows
        g.add("Laplace transform of kappa_omega against the closed form, p in {2,3,5,8}, omega = %g" % om,
              we, 1e-10)
    g.tables = {"Gh, worst relative difference between the two routes": consistency,
                "int_0^inf e^(-p tau) kappa_omega dtau  vs  pi^om Gamma((a+p)/2)/Gamma((b+p)/2) (p+a)(p-b)/((p+b)(p-a))": laplace}
    return g.out()


def group_mass():
    g = Group("C. the mass on [0,L) at three horizons, and its first-order limit against Proposition 2.3",
              "the closed form integrates the poles, the digamma and the primes of xi'/xi "
              "directly; the assembled kernel carries them through the Beta convolution and "
              "the pole repair, so the agreement is between two arrangements of the same data")
    rows, tails = {}, {}
    for (name, L) in HORIZONS:
        closed = first_order_tail(L)
        tails[name] = closed
        sub, we = {}, 0.0
        for om in (0.002, 0.01):
            _, nodes = kernel_nodes(om, L, NQ_OUT, NQ_IN)
            mass = math.fsum(w * g_ for (_, w, g_) in nodes)
            ref = REFERENCE[(name, om)][0]
            rel = abs(mass - ref) / ref
            sub["omega = %g" % om] = {"mass on [0,L)": mass, "(1 - mass)/omega": (1.0 - mass) / om,
                                      "40-digit reference": ref, "relative error": rel}
            we = max(we, rel)
        g.add("mass against the 40-digit assembly, omega in {0.002, 0.01}, L = %s" % name, we, 1e-12)
        m2, m1 = sub["omega = 0.002"]["(1 - mass)/omega"], sub["omega = 0.01"]["(1 - mass)/omega"]
        extrap = m2 + (m2 - m1) * 0.25
        rel = abs(extrap - closed) / closed
        sub["two-point extrapolation to omega = 0"] = extrap
        sub["Proposition 2.3 closed form"] = closed
        sub["relative difference"] = rel
        g.add("two-point extrapolation of (1-mass)/omega against Proposition 2.3, L = %s" % name,
              rel, 1e-5)
        rows[name] = sub
    g.tables = {"horizons": rows, "Proposition 2.3 first-order tail": tails}
    return g.out()


def weil_margin(L):
    """m_L^(N) = lambda_min(Q_{0,L}) in the same N-mode sine basis, both parity blocks."""
    W = WeilForm(L, NBASIS)
    comb = prime_comb(L)
    Me, _ = W.matrix(comb, 0)
    Mo, _ = W.matrix(comb, 1)
    eve, _ = jacobi_eigen(Me)
    evo, _ = jacobi_eigen(Mo)
    return min(eve[0], evo[0]), eve[0], evo[0], Me[0][0]


def group_margin(mL, eve0, evo0, Qe1):
    g = Group("D. contraction and the first-order margin at L = log 3",
              "lambda_min(D) is a 1e-9 quantity read off matrices of norm 1, so double "
              "precision carries about four of its digits; the sharp assertions are "
              "contraction and |delta| < 1 percent, and the 40-digit comparison is made at "
              "the 1e-3 relative level the arithmetic supports")
    g.add("m_L^(24) from the closed-form Weil assembler against 40 digits",
          abs(mL - M_L_24) / M_L_24, 1e-7)
    rows = {}
    for om in (0.002, 0.01, 0.02, 0.05, 0.1):
        d = contraction_data(om, L3, NBASIS, NQ_OUT, NQ_IN)
        val = d["lambda_min_D"] / (2.0 * om)
        ratio = val / mL
        ref = REFERENCE[("log3", om)][1]
        rel = abs(val - ref) / ref
        rows["omega = %g" % om] = {
            "1 - ||V||": 1.0 - d["norm_V"], "lambda_min(D)": d["lambda_min_D"],
            "lambda_min(D)/(2 omega)": val, "ratio to m_L^(24)": ratio,
            "40-digit reference": ref, "relative error against it": rel,
            "first-order law on e_1, ratio to Q[e_1]": d["first_order_e1"] / Qe1,
            "e_1 ratio, 40-digit reference": REFERENCE[("log3", om)][2]}
        g.assert_true("||V_{%g,log3}|| < 1" % om, d["norm_V"] < 1.0)
        g.add("lambda_min(D)/(2 omega) against 40 digits, omega = %g" % om, rel, 1e-3)
        g.add("first-order law on e_1 against 40 digits, omega = %g" % om,
              abs(d["first_order_e1"] / Qe1 - REFERENCE[("log3", om)][2]), 1e-7)
    ratio01 = rows["omega = 0.01"]["ratio to m_L^(24)"]
    g.add("|lambda_min(D)/(2 omega) / m_L^(24) - 1| at omega = 0.01", abs(ratio01 - 1.0), 0.01)
    excess = {k: (v["ratio to m_L^(24)"] - 1.0) / float(k.split("= ")[1]) for k, v in rows.items()}
    g.tables = {"m_L^(24), even block": eve0, "m_L^(24), odd block": evo0,
                "omega sweep": rows,
                "relative excess over m_L^(24), divided by omega (Proposition 2.2 is linear)": excess}
    return g.out()


def group_horizons():
    g = Group("E. the first-order law on e_1 at L = log 5 and log 7",
              "m_L^(N) is 2.5e-17 and 2.1e-22 in this basis, below what double precision can "
              "read off a matrix of norm 1, so the margin at these horizons stays exploratory "
              "(see ../exploratory/cmgj_*.json); the first-order law on a fixed vector is "
              "O(1e-4) and is carried here")
    rows = {}
    for (name, L) in HORIZONS[1:]:
        W = WeilForm(L, NBASIS)
        Me, _ = W.matrix(prime_comb(L), 0)
        sub = {}
        for om in (0.002, 0.01):
            d = contraction_data(om, L, NBASIS, NQ_OUT, NQ_IN)
            r = d["first_order_e1"] / Me[0][0]
            ref = REFERENCE[(name, om)][2]
            sub["omega = %g" % om] = {"(1 - ||V e_1||^2)/(2 omega)": d["first_order_e1"],
                                      "Q_{0,L}[e_1]": Me[0][0], "ratio": r,
                                      "40-digit reference": ref, "difference": abs(r - ref)}
            g.add("first-order law on e_1 against 40 digits, L = %s, omega = %g" % (name, om),
                  abs(r - ref), 1e-6)
            g.add("| ||V|| - 1 | at L = %s, omega = %g (the true defect, 2.6e-19 and 2.1e-24, "
                  "is below double precision; only its absence at the 1e-12 level is asserted)"
                  % (name, om), abs(d["norm_V"] - 1.0), 1e-12)
        rows[name] = sub
    g.tables = {"horizons": rows}
    return g.out()


def group_cayley(mL):
    g = Group("F. the cumulative Cayley coordinate Z = (I-V)(I+V)^(-1), P = (2/omega) Re Z",
              "P >= 0 is the positive-real criterion, equivalent to ||V|| <= 1 by the exact "
              "congruence; and P = Q_{0,L} + O(omega^2), because Z = tanh(omega G/2) is odd "
              "in omega, where the defect carries a first-order correction -omega m_L^2")
    rows = {}
    for om in (0.002, 0.01, 0.02, 0.05, 0.1):
        d = contraction_data(om, L3, NBASIS, NQ_OUT, NQ_IN)
        dd = d["lambda_min_D"] / (2.0 * om)
        rows["omega = %g" % om] = {
            "lambda_min(P)": d["lambda_min_P"], "lambda_min(D)/(2 omega)": dd,
            "difference, relative to m_L^(24)": (d["lambda_min_P"] - dd) / mL,
            "difference / (m_L^(24) omega^2)": (d["lambda_min_P"] - dd) / mL / om ** 2,
            "congruence residual max |D - (omega/2)(I+V*)P(I+V)|": d["congruence_residual"]}
        g.add("congruence D = (omega/2)(I+V*) P (I+V), omega = %g" % om, d["congruence_residual"], 1e-15)
        g.assert_true("P_{%g,log3} >= 0 (accretive Z, positive-real symbol)" % om, d["lambda_min_P"] > 0.0)
    ratios = [rows["omega = %g" % om]["difference / (m_L^(24) omega^2)"] for om in (0.02, 0.05, 0.1)]
    spread = (max(ratios) - min(ratios)) / max(abs(r) for r in ratios)
    g.add("the difference is quadratic: spread of (lambda_min(P) - lambda_min(D)/2omega)/(m_L omega^2) "
          "over omega in {0.02, 0.05, 0.1}", spread, 0.15)
    g.add("that coefficient at omega = 0.1 against its 40-digit value %g" % CAYLEY_C,
          abs(ratios[-1] - CAYLEY_C) / CAYLEY_C, 0.02)
    g.tables = {"omega sweep at L = log 3": rows,
                "note on the two smallest shifts": (
                    "the difference is 1e-5 of a 1e-9 eigenvalue at omega = 0.01 and 1e-7 of it "
                    "at omega = 0.002, i.e. 1e-14 and 1e-16 in absolute terms, so those two rows "
                    "are at the double-precision floor and only omega >= 0.02 carries the law")}
    return g.out()


def main():
    mL, eve0, evo0, Qe1 = weil_margin(L3)
    groups = [group_quadrature(), group_kernel(), group_mass(),
              group_margin(mL, eve0, evo0, Qe1), group_horizons(), group_cayley(mL)]
    out = {
        "programme": "check_contraction_margin.py",
        "investigation": "loewner",
        "object": "V_{omega,L} = P_L (causal convolution with k_omega) P_L, k_omega the causal "
                  "kernel of xi(s-omega)/xi(s+omega), assembled from Gamma, sinh, exp and the "
                  "integers below e^L",
        "basis": "orthonormal sine basis on (-L/2, L/2), N = %d" % NBASIS,
        "quadrature": "Gauss-Jacobi for the weight tau^(omega-1), %d nodes outer, %d inner" % (NQ_OUT, NQ_IN),
        "scope": "finite test cases at three horizons; not a positivity certificate and not a "
                 "statement about the zeros",
        "groups": groups,
    }
    out["all_pass"] = all(g["pass"] for g in groups)
    out["total_checks"] = sum(g["cases"] for g in groups)
    print(json.dumps(out, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
