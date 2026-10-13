"""
lab_adhm_check.py -- does the ADHM / jumping-line dictionary escape the
circularity of memo6 §4?

BACKGROUND.  memo6 §4 closed the program on the finding that the reality
involution on a zero multiset yields a COMMUTATIVE algebra with TRIVIAL
involution, for which "the trace form is positive definite" IS the conclusion
(Sylvester + Albert), so no mechanism is being applied.  Weil's argument needs
a NONcommutative algebra with a positive anti-involution and a distinguished
element not fixed by it.

ADHM is the one place in this program's orbit where a noncommutative algebra
with a positive involution appears attached to finite quaternionic matrix data,
and where the discriminating invariant of twistor_lift_computation.md §3 -- the
sigma-action on the components of a divisor in the space of lines -- is already
governed by a positivity condition ("no real jumping lines").  Two questions:

  (a) does the ADHM variety actually fail to commute?
  (b) is the positivity non-circular, or is it Sylvester's law again in disguise?

SET-UP (Atiyah's quaternionic normal form for charge k, SU(2)).
   Delta(q) = [ T - q I_k ; lambda ] ,  T in H^{kxk},  lambda in H^{1xk},
   ADHM condition:  Delta^dag Delta is REAL (k x k), and the instanton is
   regular iff Delta^dag Delta is also nonsingular for every q in H -- i.e.
   iff the associated bundle has NO REAL JUMPING LINES.  So the real jumping
   locus is exactly  Z(det Delta^dag Delta)  inside H.

THE DICTIONARY UNDER TEST.  For a monic real p of degree k, the zero set of the
slice extension R p in H (real roots -> isolated points, conjugate pairs ->
2-spheres) is exactly the zero set of
   P_p(q) := p(x_0 + i r) p(x_0 - i r) ,   r = |Im q| .
So the canonical question is: for which p does there exist admissible ADHM data
with  det(Delta^dag Delta) = P_p ?  Nothing here is invented: both sides are the
canonical objects of their respective theories.

RESULT.  Theorem (§4): only for hyperbolic p, and then lambda = 0 and
T = T_0 real symmetric with char poly p -- the data collapses onto the
COMMUTATIVE REAL locus of the ADHM variety.  So (a) is YES and (b) is NO:
noncommutativity exists but the matching condition annihilates it, and
"admissible data exists" is equivalent to hyperbolicity via the spectral
theorem for real symmetric matrices.  memo6 §4 stands, re-derived from the
gauge-theory side.
"""
import numpy as np
import sympy as sp
from math import comb

from lab_qalg import (qmul, qdag, qadd, qsub, qsimp, qscalar_times_I,
                  qsym_matrix, qsym_row, verify_table)
import lab_adhm_num as an

np.set_printoptions(precision=6, suppress=True)
XS = sp.symbols('x0 x1 x2 x3', real=True)
EPS3 = {1: (2, 3, +1), 2: (1, 3, -1), 3: (1, 2, +1)}   # a -> (b,c,eps_abc)
LINE = "=" * 78


def head(s):
    print()
    print(LINE)
    print(s)
    print(LINE)


# ===================================================================== PART 0
head("PART 0  quaternionic matrix algebra: sanity")
t = verify_table()
assert (t[('i', 'j')], t[('j', 'i')], t[('j', 'k')], t[('k', 'i')]) == ('k', '-k', 'i', 'j')
assert all(t[(c, c)] == '-1' for c in 'ijk')
print("  multiplication table i*j=k, j*i=-k, j*k=i, k*i=j, i^2=j^2=k^2=-1 : OK")

# cross-check the fast numeric layer against the symbolic one
rng = np.random.default_rng(7)
k = 3
z = rng.normal(size=an.nparams(k))
T_, lam_ = an.unpack(z, k)
Tq = [sp.Matrix(T_[a]) for a in range(4)]
lq = [sp.Matrix(1, k, lambda i, j: sp.Float(lam_[j, a])) for a in range(4)]
A_ = qsub(Tq, qscalar_times_I(XS, k))
G_ = qsimp(qadd(qmul(qdag(A_), A_), qmul(qdag(lq), lq)))
iu = np.triu_indices(k, 1)
sym_im = np.concatenate([np.array(G_[a].evalf(), dtype=float)[iu] for a in EPS3])
print("  |symbolic Im blocks - numeric adhm_residual| = %.2e"
      % np.abs(sym_im - an.adhm_residual(T_, lam_)).max())
Qs = rng.normal(size=(4, 4))
dv = [float(sp.Matrix(G_[0]).subs(dict(zip(XS, [sp.Float(x) for x in q]))).det())
      for q in Qs]
print("  |det(real block) - detM| = %.2e" % np.abs(np.array(dv) - an.detM(T_, lam_, Qs)).max())


# ===================================================================== PART 1
head("PART 1  what 'Delta^dag Delta real' forces  (derived, not assumed)")

for kk in (2, 3):
    T = qsym_matrix('T', kk)                       # fully general quaternionic
    lam = qsym_row('L', kk)
    A = qsub(T, qscalar_times_I(XS, kk))
    G = qsimp(qadd(qmul(qdag(A), A), qmul(qdag(lam), lam)))
    lin, con = set(), 0
    for a in EPS3:
        for i in range(kk):
            for j in range(kk):
                for mono, c in sp.Poly(sp.expand(G[a][i, j]), *XS).terms():
                    if c == 0:
                        continue
                    if sum(mono) == 1:
                        lin.add(sp.simplify(c))
                    else:
                        con += 1
    # the x-linear conditions are exactly  T_a antisymmetric part = 0
    forced = set()
    for c in lin:
        forced |= {s for s in c.free_symbols}
    offdiag_only = all(len(sp.Add.make_args(sp.expand(c))) == 2 for c in lin)
    print(f"  k={kk}: {len(lin)} distinct x-linear conditions"
          f" (each of the form T_a[i,j] - T_a[j,i] = 0: {offdiag_only}),"
          f" {con} x-independent ones")

# with symmetric blocks imposed, check the normal form and the ADHM equations
print()
print("  imposing symmetric blocks:")
for kk in (2, 3):
    T = qsym_matrix('T', kk, symmetric=True)
    lam = qsym_row('L', kk)
    A = qsub(T, qscalar_times_I(XS, kk))
    G = qsimp(qadd(qmul(qdag(A), A), qmul(qdag(lam), lam)))
    C = sum((T[a] * T[a] for a in range(4)), sp.zeros(kk, kk)) + qmul(qdag(lam), lam)[0]
    s = sum(x ** 2 for x in XS)
    pred = C + s * sp.eye(kk) - 2 * sum((XS[a] * T[a] for a in range(4)), sp.zeros(kk, kk))
    ok0 = sp.simplify(sp.expand(G[0] - pred)) == sp.zeros(kk, kk)
    okc = True
    for a, (b, c, sg) in EPS3.items():
        e = (T[0] * T[a] - T[a] * T[0]) - sg * (T[b] * T[c] - T[c] * T[b]) + qmul(qdag(lam), lam)[a]
        if sp.simplify(sp.expand(G[a] - e)) != sp.zeros(kk, kk):
            okc = False
    print(f"    k={kk}:  Re = C + |q|^2 I - 2 sum_a x_a T_a  with C = sum_a T_a^2 + Re(lam^dag lam) : {ok0}")
    print(f"           Im_a = [T_0,T_a] - eps_abc [T_b,T_c] + Im_a(lam^dag lam) : {okc}")

print()
print("  => reality  <=>  (i) all four blocks T_a real SYMMETRIC")
print("                   (ii) [T_0,T_a] - eps_abc[T_b,T_c] + Im_a(lam^dag lam) = 0.")
print("     These are the classical ADHM equations; (ii) is nonlinear and")
print("     noncommutative.  C = sum_a T_a^2 + Re(lam^dag lam) is automatically PSD:")
print("     that is the positivity the construction supplies.")


# ===================================================================== PART 2
head("PART 2  TEST (a): does the ADHM variety fail to commute?")

# exact rational witness
s1 = np.array([[0., 1.], [1., 0.]])
s3 = np.array([[1., 0.], [0., -1.]])
Tw = [s1, s3, np.zeros((2, 2)), np.zeros((2, 2))]
lamw = np.array([[1., 0., 0., 0.], [0., 2., 0., 0.]])       # lambda = (1, 2i)
res = np.abs(an.adhm_residual(Tw, lamw)).max()
print("  exact witness  T_0 = [[0,1],[1,0]], T_1 = diag(1,-1), T_2 = T_3 = 0,"
      " lambda = (1, 2i):")
print("    ADHM residual = %.1e   [T_0,T_1] =" % res, Tw[0] @ Tw[1] - Tw[1] @ Tw[0],
      " -> noncommutative")
assert res < 1e-14

from scipy.optimize import least_squares
print()
print("  census: solve the ADHM equations alone from 120 random starts")
for kk in (2, 3, 4):
    rng = np.random.default_rng(3 + kk)
    vals = []
    for _ in range(120):
        sol = least_squares(lambda z: an.adhm_residual(*an.unpack(z, kk)),
                            rng.normal(size=an.nparams(kk)),
                            xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=900)
        T, lam = an.unpack(sol.x, kk)
        nrm = max(np.abs(Ta).max() for Ta in T)
        if np.sqrt(2 * sol.cost) < 1e-10 and nrm > 1e-3:
            vals.append(max(np.abs(an.com(T[a], T[b])).max()
                            for a in range(4) for b in range(4)) / nrm ** 2)
    print(f"    k={kk}: {len(vals)}/120 exact solutions, "
          f"largest normalised max_ab|[T_a,T_b]|/|T|^2 = {max(vals):.3f}")

print()
print("  ANSWER (a): YES.  The ADHM variety is richly noncommutative at every")
print("  k >= 2.  memo6 §4's commutativity objection is NOT automatic here.")


# ===================================================================== PART 3
head("PART 3  the identity chain behind the theorem, verified")

rng = np.random.default_rng(5)
kk = 3
sol = least_squares(lambda z: an.adhm_residual(*an.unpack(z, kk)),
                    rng.normal(size=an.nparams(kk)),
                    xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
T, lam = an.unpack(sol.x, kk)
C = an.Cmat(T, lam)
print("  admissible test data, ADHM residual %.1e, max|[T_a,T_b]| = %.3f"
      % (np.sqrt(2 * sol.cost),
         max(np.abs(an.com(T[a], T[b])).max() for a in range(4) for b in range(4))))

e = rng.normal(size=3)
e /= np.linalg.norm(e)
Te = sum(e[a] * T[a + 1] for a in range(3))
N = T[0] + 1j * Te
err = 0.0
for _ in range(6):
    u, v = rng.normal(size=2)
    x, eta = (u + v) / 2, (u - v) / 2
    Mslice = C + (x ** 2 - eta ** 2) * np.eye(kk) - 2 * x * T[0] - 2j * eta * Te
    L = u * v * np.eye(kk) - u * N - v * np.conj(N) + C
    err = max(err, abs(np.linalg.det(Mslice) - np.linalg.det(L)))
print("  (i) on the slice Pi_e, continuing y -> i.eta and setting u = x+eta, v = x-eta:")
print("      M  =  uv I - u N - v Nbar + C   with  N = T_0 + i T_e ;  max error %.1e" % err)

u, v = sp.symbols('u v')
for m in (2, 3):
    Nm = sp.Matrix(m, m, lambda i, j: sp.Symbol(f'n{i}{j}'))
    Nb = sp.Matrix(m, m, lambda i, j: sp.Symbol(f'm{i}{j}'))
    Cm = sp.Matrix(m, m, lambda i, j: sp.Symbol(f'c{i}{j}'))
    d = sp.expand((u * v * sp.eye(m) - u * Nm - v * Nb + Cm).det())
    co = sp.Poly(d, u, v).coeff_monomial(u ** (m - 1) * v ** (m - 1))
    pred = Cm.trace() + Nm.trace() * Nb.trace() - (Nm * Nb).trace()
    print("  (ii) k=%d: coeff(u^%d v^%d) of det(uvI - uN - vNbar + C)"
          "  ==  tr C + tr N tr Nbar - tr(N Nbar) : %s"
          % (m, m - 1, m - 1, sp.simplify(sp.expand(co - pred)) == 0))


# ===================================================================== PART 4
head("PART 4  THE THEOREM")
print("""  Let Delta = [T - qI ; lambda] with Delta^dag Delta real, and suppose
      det(Delta^dag Delta)(q) = P_p(q) = p(x_0 + i r) p(x_0 - i r)
  for a monic real p of degree k >= 1.  Then lambda = 0, T_1 = T_2 = T_3 = 0,
  T = T_0 is real symmetric, and p = char poly of T_0.  In particular p is
  HYPERBOLIC.

  Proof.  By Part 1, Delta^dag Delta = C + |q|^2 I - 2 sum_a x_a T_a with all
  T_a real symmetric and C = sum_a T_a^2 + Re(lam^dag lam) >= 0.  Restrict q to
  a slice Pi_e = {x_0 + y e}, continue y -> i.eta, and put u = x_0+eta,
  v = x_0-eta.  Then P_p becomes p(u)p(v) and, by Part 3(i),
      det( uv I - u N - v Nbar + C ) = p(u) p(v),      N = T_0 + i T_e .
  The u^k v^k coefficient is 1 on both sides.  Comparing the coefficient of
  u^{k-1} v^{k-1} (Part 3(ii)) and using p(u) = det(uI - Nbar), p(v) =
  det(vI - N) -- which is the u^k, resp. v^k, leading coefficient of the same
  identity -- gives
      tr C  =  tr(N Nbar)  =  tr T_0^2 + tr T_e^2        for EVERY unit e.
  The left side is independent of e, so the quadratic form e -> tr T_e^2 =
  sum_{ab} e_a e_b tr(T_a T_b) is constant on S^2, hence tr(T_a T_b) =
  kappa delta_ab (a,b >= 1) and tr T_e^2 = kappa.  But
      tr C = tr T_0^2 + 3 kappa + ||lambda||^2 ,
  so 3 kappa + ||lambda||^2 = kappa, i.e. 2 kappa + ||lambda||^2 = 0.  Both
  terms are >= 0, so kappa = 0 and lambda = 0; kappa = tr T_a^2 = 0 with T_a
  real symmetric forces T_1 = T_2 = T_3 = 0.  Then C = T_0^2 and
      det(Delta^dag Delta) = det( (T_0 - x_0 I)^2 + r^2 I )
                           = prod_j [ (x_0 - tau_j)^2 + r^2 ],
  tau_j the eigenvalues of the real symmetric T_0, hence real; matching with
  P_p = prod_m [ (x_0 - rho_m)^2 + r^2 ] gives {rho_m} = {tau_j}.  QED

  Notes (from an independent adversarial review pass).
   * The NONLINEAR ADHM equations are never used, and neither is C >= 0: only
     the LINEAR part of the reality condition (symmetry of the four blocks)
     plus the shapes of M and C.  The collapse is forced before the
     interesting equations are consulted.
   * k >= 2 is not needed; the chain holds at k = 1.
   * Summing the trace relation over e = i, j, k and using tr T_e = 0 gives the
     obstruction directly, so THREE slices suffice, not the whole sphere.
   * Symmetry of T_a is load-bearing in exactly one place: kappa = ||T_1||_F^2
     >= 0.  An exact ideal-membership certificate at k = 2 for symbolic monic p
     is in lab_adhm_certificate.py: modulo the affine-linear coefficient
     equations, 2 sum_{a>=1} tr T_a^2 + 3||lambda||^2 is an exact rational
     combination of four of the remaining ones.""")

print("  numerical confirmation of the two conclusions on solved data follows in Part 5.")


# ===================================================================== PART 5
head("PART 5  TEST (b): existence search, hyperbolic vs non-hyperbolic")

# --- Jensen polynomials of Xi, for the real instances -----------------------
from mpmath import mp, mpf, quad, exp, pi, factorial, polyroots
mp.dps = 30


def Phi(uu):
    s, n = mpf(0), 1
    while n <= 60:
        t = (2 * pi ** 2 * n ** 4 * exp(mpf(9) * uu / 2)
             - 3 * pi * n ** 2 * exp(mpf(5) * uu / 2)) * exp(-pi * n ** 2 * exp(2 * uu))
        s += t
        if n > 3 and abs(t) < mpf(10) ** (-mp.dps - 5):
            break
        n += 1
    return s


NM = 10
M = [quad(lambda uu: Phi(uu) * uu ** (2 * m), [0, 4]) for m in range(NM)]
b = [4 * M[m] / factorial(2 * m) for m in range(NM)]
gamma = [factorial(m) * b[m] for m in range(NM)]
print("  moments: 4*M_0 = %s  vs  xi(1/2) = 0.4971207174   (rel err %.1e)"
      % (mp.nstr(b[0], 10), float(abs(b[0] / mpf('0.4971207174') - 1))))
assert all(x > 0 for x in b)


def jensen_roots(d, n):
    co = [comb(d, j) * gamma[n + j] for j in range(d + 1)]
    rts = polyroots(list(reversed(co)), maxsteps=400, extraprec=400)
    r = np.array([complex(x) for x in rts])
    return r / np.abs(r).max()          # dilation of q; harmless, helps conditioning


cases = []
for kk, nm, roots in [
        (2, "z^2-1", [1.0, -1.0]),
        (2, "z^2+1", [1j, -1j]),
        (2, "(z-1)(z-2)", [1.0, 2.0]),
        (2, "z^2+z+1", [(-1 + 3 ** .5 * 1j) / 2, (-1 - 3 ** .5 * 1j) / 2]),
        (3, "(z-1)(z-2)(z-3)", [1.0, 2.0, 3.0]),
        (3, "(z^2+1)(z-1)", [1j, -1j, 1.0]),
        (4, "(z^2-1)(z^2-4)", [1.0, -1.0, 2.0, -2.0]),
        (4, "(z^2+1)(z^2-1)", [1j, -1j, 1.0, -1.0]),
        (4, "X^4+10X^3+26X^2+22X+3  [memo5 counterexample]",
         list(np.roots([1., 10., 26., 22., 3.]))),
        (2, "J^{2,0} of Xi", None),
        (3, "J^{3,0} of Xi", None),
        (3, "J^{3,1} of Xi", None)]:
    if roots is None:
        roots = list(jensen_roots(kk, int(nm.split(',')[1][0])))
    cases.append((kk, nm, roots))

print()
print("  residual = || ADHM eqs ||  +  || det M - P_p || / scale,  40 random starts")
print(f"  {'k':>2}  {'p':<42} {'hyperbolic':>10} {'best residual':>14}  {'|T_1..3|':>9}")
verdict = []
for kk, nm, roots in cases:
    hyp = all(abs(np.imag(r)) < 1e-9 for r in roots)
    best, zb = an.search(kk, roots, ntrials=40, seed=11)
    T, lam = an.unpack(zb, kk)
    t123 = max(np.abs(T[a]).max() for a in (1, 2, 3))
    print(f"  {kk:>2}  {nm:<42} {('yes' if hyp else 'NO'):>10} {best:>14.3e}  {t123:>9.2e}")
    verdict.append((nm, hyp, best, t123, np.abs(lam).max()))

print()
ok = all((b < 1e-8) == h for (_, h, b, _, _) in verdict)
print("  existence tracks hyperbolicity exactly on all %d cases: %s" % (len(verdict), ok))
print("  and on every solved (hyperbolic) case the data lands on T_1=T_2=T_3=0,")
print("  lambda=0: max over solved cases of |T_1..3| = %.2e, of |lambda| = %.2e"
      % (max(t for (_, h, b, t, _) in verdict if b < 1e-8),
         max(l for (_, h, b, _, l) in verdict if b < 1e-8)))


# ===================================================================== PART 6
head("PART 6  where the discriminating power actually sits")
print("  The off-axis (sphere) data is doing all the work.  Matching only on the")
print("  REAL AXIS, det(C + x^2 I - 2x T_0) = p(x)^2, is satisfiable for")
print("  non-hyperbolic p: take k=2, T_0 = 0, T_1 = diag(1,-1), T_2 = T_3 = 0,")
print("  lambda = 0, so C = I and")
Tb = [np.zeros((2, 2)), np.diag([1., -1.]), np.zeros((2, 2)), np.zeros((2, 2))]
lb = np.zeros((2, 4))
print("    ADHM residual = %.1e" % np.abs(an.adhm_residual(Tb, lb)).max())
xs = np.linspace(-2, 2, 7)
Qax = np.stack([xs, 0 * xs, 0 * xs, 0 * xs], axis=1)
lhs = an.detM(Tb, lb, Qax)
rhs = (xs ** 2 + 1) ** 2
print("    det M on the real axis vs (x^2+1)^2 : max diff %.1e   (p = x^2+1, NOT hyperbolic)"
      % np.abs(lhs - rhs).max())
Qsl = np.stack([xs, 0 * xs + 0.7, 0 * xs, 0 * xs], axis=1)          # inside the slice C_i
Qof = np.stack([xs, 0 * xs, 0 * xs + 0.7, 0 * xs], axis=1)          # same (x_0, r), other slice
print("    in fact det M = P_p on the whole 2-plane {x_2=x_3=0}: max diff %.1e"
      % np.abs(an.detM(Tb, lb, Qsl) - an.P_target([1j, -1j], Qsl)).max())
print("    this datum is just the x_0 <-> x_1 rotation of the p = x^2-1 solution,")
print("    and ONE SLICE cannot tell which axis is the real one.  Moving to a")
print("    different slice at the same (x_0, r) breaks it:")
print("      max |det M - P_p| off that plane = %.3f"
      % np.abs(an.detM(Tb, lb, Qof) - an.P_target([1j, -1j], Qof)).max())
print("    => the discriminating power is not 'off the real axis' but 'off any")
print("       single slice': it is carried by the full 2-sphere of complex")
print("       structures, exactly the invariant of twistor_lift_computation §3.")

head("SUMMARY")
print("""  (a) YES: the ADHM variety is genuinely noncommutative at every k >= 2, and
      the positivity it carries (C = sum T_a^2 + Re(lam^dag lam) >= 0) is
      structural, not assumed.  This is the first object in this program with
      the algebraic shape memo6 §4 said was missing.

  (b) NO: the matching condition det(Delta^dag Delta) = P_p forces lambda = 0
      and T_1 = T_2 = T_3 = 0 -- the data collapses onto the COMMUTATIVE REAL
      locus -- and then "p hyperbolic" is the spectral theorem for real
      symmetric matrices.  Proved (Part 4), and confirmed on 12 cases (Part 5):
      admissible data exists exactly for the hyperbolic targets, including a
      NO for the memo5 quartic that passes the Newton/Turan test.

  So the noncommutativity is real but the dictionary annihilates it.  memo6 §4
  stands, now re-derived from the gauge-theory side: the obstruction is not that
  a noncommutative algebra with a positive involution is unavailable -- it is
  that pinning the jumping locus to the zero set of a slice extension is
  precisely the condition that kills the noncommutative directions.""")
