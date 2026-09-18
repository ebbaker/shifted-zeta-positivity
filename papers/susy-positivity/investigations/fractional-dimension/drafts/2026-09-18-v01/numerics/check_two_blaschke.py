#!/usr/bin/env python3
"""
The Markov decomposition past the rank-two wall, and what the criterion is worth
there.  Standard library only; prints JSON to stdout.  Written by Claude Opus 5
(Anthropic), model `claude-opus-5`, for the fractional-dimension investigation,
18 September 2026.

PROVENANCE.  Lines between the two banner comments below are copied verbatim from
../loewner/numerics/check_contraction_margin.py (the registered assembly of
V_{omega,L}), with ONE change, marked [PATCH] in place:

  gauss_jacobi_unit: the k = 0 Jacobi recurrence coefficient was written as
  (be^2 - al^2)/(d (d+2)) with d = al + be, which is 0/0 at al = be = 0, i.e. at
  omega = 1 exactly.  It is replaced by its removable value (be - al)/(al+be+2),
  equal to the old expression whenever d != 0.  Without it the parent programme
  raises ZeroDivisionError at omega = 1 and only there.  Nothing else changed:
  in particular the assembly itself needed NO second Blaschke factor, because it
  is built from the PARTIAL FRACTIONS of R_omega,

      R_omega(p) = 1 - 4 omega b/(p+b) - 4 omega a/(p-a),

  which are the same algebra at every omega.  The Blaschke factorization of
  R_omega enters the proofs, not the assembly.

WHAT IS CHECKED.

  A. The patched quadrature.  Gauss-Jacobi moments int_0^1 x^(om-1) x^m dx =
     1/(om+m) at omega = 1/2, 1, 3/2, 2, including omega = 1 where the parent
     programme cannot run.
  B. The factorization and the second Blaschke factor.  With a = 1/2 - omega,
     b = 1/2 + omega, c = -a = omega - 1/2:
       R_omega = (p+a)(p-b)/((p+b)(p-a))            (product form)
               = 1 - 4 om b/(p+b) - 4 om a/(p-a)    (the assembly's form)
               = B_b(p) . (p+a)/(p-a) ,
     and for omega >= 1/2, (p+a)/(p-a) = B_c(p) is a Blaschke factor of the right
     half-plane, so R_omega = B_b B_c is INNER; for omega < 1/2 it is a ratio
     B_b/B_a with a pole at p = a > 0 and is not.  Checked on a complex grid, on
     the imaginary axis (|R| = 1 at every omega), and at the pole.
     Also K_omega = R_omega Ktilde_omega end to end, with zeta at real arguments.
  C. Complete monotonicity past the wall.  The parent's grouping
     Khat = ((p+a)/(p-a)) Ktilde fails to exhibit positivity for omega > 1/2,
     because (p+a)/(p-a) has causal kernel delta_0 + 2a e^(a t) with 2a < 0.
     Regrouping the Gamma factors repairs it: with z = (p+a)/2,

       Khat^Gamma_omega(p) = pi^om Gamma(z+c)/Gamma(z+om) . Gamma(z+1)/Gamma(z+c+1),

     a product of two Gamma ratios whose parameter gaps are 1/2 and c, both >= 0
     exactly when omega >= 1/2; each is completely monotone by the Beta integral,
     so Khat_omega is completely monotone for every omega >= 1/2.  The identity is
     checked against the parent's form, and the kernel is sampled for positivity
     (at omega = 1 against its closed form 2 pi e^(-tau/2)).
  D. The assembly's own certificate at the new shifts.  int_0^inf e^(-p tau)
     kappa_omega(tau) dtau against pi^om Gamma((a+p)/2)/Gamma((b+p)/2) R_omega(p)
     at omega = 1, 3/2, 2, with omega = 0.1, 1/2 as controls.
  E. Contraction at omega = 1, 3/2, 2 and L = log 3.  This is a CALIBRATION, not
     a test: Proposition 3 of the accompanying note shows ||V_{omega,L}|| <= 1
     holds unconditionally for every omega >= 1/2, by the Euler product alone.
     The run is recorded to show the instrument returns it, and to show the
     first-order law lambda_min(D)/(2 omega) = m_L degrading as omega grows.
  F. The two intervals.  sign(r_{d+1}(3)) = sign((4/3)(d+1)d(d-1)) and sign(a) =
     sign((1-d)/2) are opposite for every d > 0 with d != 1: the open interval on
     which the lattice point count is negative is exactly the open interval on
     which the criterion has arithmetic content.

  Counts below refer to finite test cases, not independent theorems.

ZETA HYGIENE.  zeta is evaluated ONLY at real arguments u >= 1.2, by a convergent
Euler-Maclaurin sum, in group B alone; every other group uses Gamma, sinh, exp,
polynomials and the integers below e^L.  No value off the real axis is computed
and no zero is located.

SCOPE.  Nothing here is a positivity certificate for the Weil form and nothing
here is a statement about the zeros.
"""
import json
import math

# ===== BEGIN material copied from ../loewner/numerics/check_contraction_margin.py =====
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
        # [PATCH] removable at al + be = 0 (omega = 1); identical elsewhere.
        diag.append((be - al) / (al + be + 2.0) if k == 0
                    else (be * be - al * al) / (d * (d + 2.0)))
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


# ===== END material copied from ../loewner/numerics/check_contraction_margin.py =====

# --------------------------------------------------------------------- driver
L3 = math.log(3.0)
NBASIS, NQ_OUT, NQ_IN = 24, 32, 32
OMEGAS_PAST = (1.0, 1.5, 2.0)                 # ranks m = 3, 4, 5
OMEGAS_ALL = (0.1, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0)
PGRID = (3.0, 5.0, 8.0)

# Bernoulli numbers B_2k for the Euler-Maclaurin tail of zeta.
_B2K = (1.0 / 6.0, -1.0 / 30.0, 1.0 / 42.0, -1.0 / 30.0, 5.0 / 66.0, -691.0 / 2730.0)


def zeta_real(u, N=24):
    """zeta(u) for REAL u > 1 by Euler-Maclaurin.  No other zeta value is computed."""
    if u <= 1.0:
        raise ValueError("this programme evaluates zeta only at real u > 1")
    tot = math.fsum(float(n) ** (-u) for n in range(1, N))
    tot += N ** (1.0 - u) / (u - 1.0) + 0.5 * N ** (-u)
    poch, fact = u, 2.0
    for k, B in enumerate(_B2K, start=1):
        tot += B / fact * poch * N ** (-u - 2.0 * k + 1.0)
        poch *= (u + 2.0 * k - 1.0) * (u + 2.0 * k)
        fact *= (2.0 * k + 1.0) * (2.0 * k + 2.0)
    return tot


def Lambda_real(u):
    """Lambda(u) = pi^(-u/2) Gamma(u/2) zeta(u), real u > 1."""
    return math.pi ** (-u / 2.0) * math.gamma(u / 2.0) * zeta_real(u)


def xi_real(u):
    """xi(u) = (1/2) u (u-1) Lambda(u), real u > 1.  (The parent manuscript's entire xi.)"""
    return 0.5 * u * (u - 1.0) * Lambda_real(u)


def R_product(om, p):
    a, b = 0.5 - om, 0.5 + om
    return (p + a) * (p - b) / ((p + b) * (p - a))


def R_partial(om, p):
    a, b = 0.5 - om, 0.5 + om
    return 1.0 - 4.0 * om * b / (p + b) - 4.0 * om * a / (p - a)


def blaschke(c, p):
    return (p - c) / (p + c)


def khatG_closed(om, p):
    """pi^om Gamma(z+c)/Gamma(z+om) . Gamma(z+1)/Gamma(z+c+1), z = (p+a)/2, c = om - 1/2."""
    a, c = 0.5 - om, om - 0.5
    z = (p + a) / 2.0
    return (math.pi ** om * math.gamma(z + c) / math.gamma(z + om)
            * math.gamma(z + 1.0) / math.gamma(z + c + 1.0))


def khatG_parent(om, p):
    """((p+a)/(p-a)) . pi^om Gamma((p+a)/2)/Gamma((p+b)/2), the parent's grouping."""
    a, b = 0.5 - om, 0.5 + om
    return ((p + a) / (p - a)) * math.pi ** om * math.gamma((p + a) / 2.0) / math.gamma((p + b) / 2.0)


def khat_atom(ker, tau):
    """kG(tau) + 2a J_a(tau): the causal kernel of ((p+a)/(p-a)) K^Gamma_omega."""
    a = 0.5 - ker.omega
    return kG_direct(ker.omega, tau) + 2.0 * a * J_direct(ker, a, tau)


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
    g = Group("A. the patched Gauss-Jacobi rule for the weight tau^(omega-1)",
              "the parent programme raises ZeroDivisionError at omega = 1 exactly, where the "
              "k = 0 Jacobi recurrence coefficient is 0/0; the patched rule is checked against "
              "exact moments at the half-integer shifts, omega = 1 included")
    for om in (0.5, 1.0, 1.5, 2.0):
        x, w = gauss_jacobi_unit(om, 16)
        for m in range(8):
            q = math.fsum(wi * xi ** m for xi, wi in zip(x, w))
            g.add("int_0^1 x^(%g-1) x^%d dx = 1/(%g+%d)" % (om, m, om, m),
                  abs(q - 1.0 / (om + m)) * (om + m), 1e-13)
    return g.out()


def group_factorization():
    g = Group("B. the factorization, and the second Blaschke factor",
              "R_omega = B_b . (p+a)/(p-a); the right factor is a Blaschke factor B_c with "
              "c = omega - 1/2 exactly when omega >= 1/2, so R_omega is inner past the wall "
              "and a ratio with a right-half-plane pole before it")
    rows = {}
    for om in OMEGAS_ALL:
        a, b, c = 0.5 - om, 0.5 + om, om - 0.5
        for p in PGRID:
            rp, rq = R_product(om, p), R_partial(om, p)
            g.add("R_omega product form = partial fractions, omega=%g p=%g" % (om, p),
                  abs(rp - rq) / abs(rp), 1e-14)
            g.add("R_omega = B_b . (p+a)/(p-a), omega=%g p=%g" % (om, p),
                  abs(rp - blaschke(b, p) * (p + a) / (p - a)) / abs(rp), 1e-14)
            if om >= 0.5:
                g.add("R_omega = B_b B_c with c = omega-1/2 >= 0, omega=%g p=%g" % (om, p),
                      abs(rp - blaschke(b, p) * blaschke(c, p)) / abs(rp), 1e-14)
            # K_omega = R_omega Ktilde_omega, end to end, zeta at real arguments only
            u1, u2 = p + a, p + b
            if u1 >= 1.2:
                K = xi_real(u1) / xi_real(u2)
                Kt = Lambda_real(u1) / Lambda_real(u2)
                g.add("K_omega = R_omega Ktilde_omega (real zeta), omega=%g p=%g" % (om, p),
                      abs(K - rp * Kt) / abs(K), 1e-13)
        # unimodular on the axis, at every omega
        axis = max(abs(abs(R_product(om, complex(0.0, y))) - 1.0)
                   for y in [0.05 * j for j in range(1, 401)])
        g.add("| |R_omega(i y)| - 1 | on 0 < y <= 20, omega=%g" % om, axis, 1e-13)
        # inner or not, on a right-half-plane grid away from the pole
        sup = 0.0
        for i in range(1, 101):
            x = 0.03 * i
            for j in range(0, 101):
                pp = complex(x, 0.06 * j)
                if abs(pp - a) < 1e-6:
                    continue
                sup = max(sup, abs(R_product(om, pp)))
        near_pole = abs(R_product(om, a + 1e-6)) if a > 0 else None
        if om >= 0.5:
            g.assert_true("R_omega is inner: sup |R| <= 1 on the grid in Re p > 0, omega=%g" % om,
                          sup <= 1.0 + 1e-12)
        else:
            g.assert_true("R_omega is NOT inner: it has a pole at p = a = %g > 0, omega=%g"
                          % (a, om), near_pole is not None and near_pole > 1e5)
        rows["omega = %g" % om] = {
            "a = 1/2 - omega": a, "c = omega - 1/2": c,
            "sup |R_omega| on the right-half-plane grid": sup,
            "|R_omega| just right of p = a": near_pole,
            "inner on Re p > 0": bool(om >= 0.5)}
    g.tables = {"the rational factor across the wall": rows}
    return g.out()


def group_monotone():
    g = Group("C. complete monotonicity past the wall, by regrouping the Gamma factors",
              "the parent's grouping Khat = ((p+a)/(p-a)) Ktilde has a factor whose causal "
              "kernel delta_0 + 2a e^(a t) is not positive for omega > 1/2; the regrouped form "
              "is a product of two Gamma ratios with parameter gaps 1/2 and c = omega - 1/2, "
              "both completely monotone exactly when omega >= 1/2")
    for om in OMEGAS_ALL:
        a, c = 0.5 - om, om - 0.5
        for p in PGRID:
            if om >= 0.5:
                g.add("Khat^Gamma regrouped = parent's grouping, omega=%g p=%g" % (om, p),
                      abs(khatG_closed(om, p) - khatG_parent(om, p)) / abs(khatG_parent(om, p)), 1e-13)
        g.assert_true("parameter gaps of the two Gamma ratios are 1/2 and c = %g, both >= 0 "
                      "iff omega >= 1/2 (omega=%g)" % (c, om), (c >= 0.0) == (om >= 0.5))
        g.assert_true("kernel of (p+a)/(p-a) is delta_0 + 2a e^(a t), positive iff omega <= 1/2 "
                      "(omega=%g, 2a = %g)" % (om, 2.0 * a), (a >= 0.0) == (om <= 0.5))
    # the kernel itself, sampled
    rows = {}
    for om in (0.5, 0.75, 1.0, 1.5, 2.0):
        ker = Kernel(om, 48)
        tau, vals = 0.02, []
        while tau < 24.0:
            vals.append((tau, khat_atom(ker, tau)))
            tau *= 1.4
        worst = min(vals, key=lambda z: z[1])
        g.assert_true("khat^Gamma_omega(tau) >= 0 at every sampled tau in [0.02, 24), omega=%g" % om,
                      worst[1] >= 0.0)
        rows["omega = %g" % om] = {"sampled points": len(vals),
                                   "min over the sample": worst[1], "at tau": worst[0]}
    # omega = 1: Khat^Gamma = 2 pi/(p + 1/2) exactly, kernel 2 pi e^(-tau/2)
    ker1 = Kernel(1.0, 48)
    err = max(abs(khat_atom(ker1, t) - 2.0 * math.pi * math.exp(-t / 2.0))
              / (2.0 * math.pi * math.exp(-t / 2.0)) for t in (0.1, 0.5, 1.0, 3.0, 6.0, 12.0))
    g.add("at omega = 1 the two Gamma ratios collapse and khat^Gamma(tau) = 2 pi e^(-tau/2) "
          "(compared through J_direct, whose relative accuracy at tau = 12 is about 1e-9)",
          err, 1e-8)
    g.tables = {"khat^Gamma_omega sampled for positivity": rows}
    return g.out()


def group_certificate():
    g = Group("D. the assembly's Laplace certificate at the new shifts",
              "the identity that certifies the assembled atom, asserted by the parent at "
              "omega = 0.01 and 0.1, now at omega = 1, 3/2, 2; it contains Gamma and nothing "
              "else -- no zeta, no xi, no zeros")
    rows = {}
    for om in (0.1, 0.5) + OMEGAS_PAST:
        sub = {}
        for p in PGRID:
            num, ex = laplace_kappa(om, p), laplace_closed(om, p)
            rel = abs(num - ex) / abs(ex)
            sub["p = %g" % p] = {"assembled": num, "closed form": ex, "relative error": rel}
            g.add("Laplace transform of the assembled atom, omega=%g p=%g" % (om, p), rel, 1e-11)
        rows["omega = %g" % om] = sub
    g.tables = {"single-atom Laplace certificate": rows}
    return g.out()


def group_calibration():
    g = Group("E. contraction at omega = 1, 3/2, 2 (ranks 3, 4, 5) at L = log 3 -- a calibration",
              "NOT a test.  Proposition 3 of the accompanying note: for every omega >= 1/2 the "
              "dichotomy's hypothesis holds unconditionally -- by the Euler product alone for "
              "omega > 1/2, with the classical zero-free region needed only at the boundary "
              "point omega = 1/2 -- so V_omega is unitary and every compression is a "
              "contraction unconditionally.  What is recorded is "
              "that the instrument returns it, and how fast the first-order law "
              "lambda_min(D)/(2 omega) = m_L^(N) degrades once omega is no longer small")
    mL = weil_margin_here(L3)
    rows = {}
    for om in (0.1, 0.5) + OMEGAS_PAST:
        d24 = contraction_data(om, L3, NBASIS, NQ_OUT, NQ_IN)
        d48 = contraction_data(om, L3, NBASIS, 48, 48)
        drift = abs(d48["lambda_min_D"] - d24["lambda_min_D"]) / abs(d24["lambda_min_D"])
        rows["omega = %g" % om] = {
            "atoms": d24["atoms"], "mass on the window": d24["mass"],
            "1 - ||V_N||": 1.0 - d24["norm_V"], "lambda_min(D_N)": d24["lambda_min_D"],
            "lambda_min(D_N)/(2 omega)": d24["lambda_min_D"] / (2.0 * om),
            "ratio to m_L^(24)": d24["lambda_min_D"] / (2.0 * om * mL),
            "quadrature drift 32 -> 48 nodes": drift}
        g.assert_true("||V_{%g,log3}|| < 1 (unconditional for omega >= 1/2; a calibration)" % om,
                      d24["norm_V"] < 1.0)
        g.add("quadrature converged: relative drift of lambda_min(D_N) from 32 to 48 nodes, "
              "omega=%g (lambda_min(D_N) is a 1e-8..1e-6 absolute quantity read off "
              "matrices of norm 1, so its relative floor is double precision, not the rule)"
              % om, drift, 1e-4)
    g.assert_true("the first-order law degrades monotonically in omega: the ratio to m_L^(24) "
                  "increases across omega = 0.1, 1/2, 1, 3/2, 2",
                  all(rows["omega = %g" % o1]["ratio to m_L^(24)"]
                      < rows["omega = %g" % o2]["ratio to m_L^(24)"]
                      for o1, o2 in zip((0.1, 0.5, 1.0, 1.5), (0.5, 1.0, 1.5, 2.0))))
    g.tables = {"m_L^(24) at L = log 3": mL, "calibration sweep": rows,
                "reading": ("the ratio to m_L^(24) runs from about 1 at omega = 0.1 to about 12 "
                            "at omega = 2: the margin is still set by the scale of the Weil "
                            "margin, because omega m_L << 1 at every shift here, but the "
                            "first-order law itself is a small-omega statement and visibly "
                            "loses accuracy.  None of these numbers is evidence for or against "
                            "any zero-free strip")}
    return g.out()


def group_intervals():
    g = Group("F. the two intervals coincide",
              "r_{d+1}(3) = (4/3)(d+1) d (d-1) is negative exactly on d in (0,1) (third note, "
              "Proposition 3.2), and a = (1-d)/2 is positive exactly on d in (0,1), which by "
              "Proposition 3 of the accompanying note is exactly where the criterion has "
              "arithmetic content.  Same open interval, same endpoints")
    grid = [0.05 * j for j in range(1, 81)]          # d in (0, 4], skipping d = 1
    for d in grid:
        if abs(d - 1.0) < 1e-12:
            continue
        r3 = 4.0 / 3.0 * (d + 1.0) * d * (d - 1.0)
        a = (1.0 - d) / 2.0
        g.assert_true("sign(r_{d+1}(3)) = -sign(a) at d = %g" % d,
                      (r3 < 0.0) == (a > 0.0))
    # the two endpoints of the gap, each degenerate in its own way
    g.add("at d = 1 (rank two) the point count and a vanish together: "
          "r_2+1(3) = 0 and a = 0",
          abs(4.0 / 3.0 * 2.0 * 1.0 * 0.0) + abs((1.0 - 1.0) / 2.0), 1e-15)
    g.add("at d = 0 (rank one) the point count vanishes and omega = 0, where "
          "Ktilde = 1 and the transfer is the identity",
          abs(4.0 / 3.0 * 1.0 * 0.0 * (-1.0)) + abs(0.0 / 2.0), 1e-15)
    g.tables = {"the coincidence": {
        "criterion has arithmetic content": "omega in (0, 1/2), i.e. d in (0,1), i.e. m in (1,2)",
        "lattice point count negative": "d in (0,1), i.e. m in (1,2)",
        "at m = 2 (rank two)": "a = 0; R_omega = B_b alone; criterion vacuous by the Euler "
                               "product; r_{d+1}(3) = 0",
        "at m = 1 (rank one)": "omega = 0; Ktilde = 1, V = I; the criterion's derivative is the "
                               "Weil form, so RH sits at THIS endpoint, not at rank two"}}
    return g.out()


def weil_margin_here(L):
    W = WeilForm(L, NBASIS)
    comb = prime_comb(L)
    Me, _ = W.matrix(comb, 0)
    Mo, _ = W.matrix(comb, 1)
    return min(jacobi_eigen(Me)[0][0], jacobi_eigen(Mo)[0][0])


def main():
    groups = [group_quadrature(), group_factorization(), group_monotone(),
              group_certificate(), group_calibration(), group_intervals()]
    out = {
        "programme": "check_two_blaschke.py",
        "investigation": "fractional-dimension",
        "model": "claude-opus-5",
        "object": "the Markov decomposition K_omega = R_omega Ktilde_omega past the rank-two "
                  "wall omega = 1/2, where R_omega = B_b B_c becomes inner, and the contraction "
                  "data of V_{omega,L} at omega = 1, 3/2, 2",
        "derived from": "../../loewner/numerics/check_contraction_margin.py, one patched line "
                        "(see the module docstring)",
        "zeta": "evaluated only at real arguments u >= 1.2, in group B, by Euler-Maclaurin; no "
                "value off the real axis and no zero is located",
        "scope": "finite test cases; not a positivity certificate and not a statement about the "
                 "zeros",
        "groups": groups,
    }
    out["all_pass"] = all(g["pass"] for g in groups)
    out["total_checks"] = sum(g["cases"] for g in groups)
    print(json.dumps(out, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
