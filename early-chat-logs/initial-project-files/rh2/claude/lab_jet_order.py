"""
lab_jet_order.py -- how thick a neighbourhood of a slice do you actually need?

Follows memo8.  memo8 established that the discriminant between det M and P_p is
r^2 - t^2, which vanishes identically on the slice Pi_e (a slice is the equality
locus of the Cauchy-Schwarz inequality t^2 <= r^2), so a one-slice condition is
blind by construction; and that "one slice plus ONE off-slice point" already
forces S = 0, i.e. hyperbolicity.  That left the natural refinement open:

    the extra point can be taken infinitesimally close to the slice.  At what
    ORDER in the transverse jet does the discriminant first appear?

This is the quantitative form of "you need more than a slice", stated in the
currency the ambitwistor literature uses (order of formal neighbourhood).

STRUCTURE (proved here, verified in Parts 1-4).  Inside the R1 family of
memo8 §2 we have T_a = e_a S for a = 1,2,3, hence

    sum_{a=1}^{3} x_a T_a = <Im q, e> S = t S ,
    M(q) = C + s I - 2 x_0 T_0 - 2 t S ,    s = |q|^2 = x_0^2 + t^2 + nu^2 ,

where nu := |Im q - t e| is the distance from q to Pi_e.  So det M depends on q
only through (x_0, t, nu^2) and P_p only through (x_0, t^2 + nu^2).  Two
immediate consequences: the deficit is EVEN in nu, and its transverse
dependence is ISOTROPIC in the 2-plane normal to the slice.

With A_j = (x_0 - tau_j)^2, B_j = A_j + t^2 + nu^2 + sigma_j^2, and conjugate
roots paired (sigma -> -sigma, which memo8 §2 shows is forced):

    det M = R * prod_pairs ( B^2 - 4 t^2 sigma^2 ) ,
    P_p   = R * prod_pairs ( B^2 - 4 (t^2 + nu^2) sigma^2 ) ,
    R     = prod_{real roots} ( A + t^2 + nu^2 ) ,

so corresponding factors differ by EXACTLY 4 nu^2 sigma^2 and telescoping gives

    det M - P_p = 4 nu^2 R_0 sum_p sigma_p^2 prod_{q != p}(B_{q,0}^2 - 4 t^2 sigma_q^2)
                  + O(nu^4) ,        ( )_0 = evaluated at nu = 0 .

Since B_0^2 - 4 t^2 sigma^2 >= B_0^2 - 4 r^2 sigma^2 = (A+(t-sigma)^2)(A+(t+sigma)^2)
> 0 and R_0 > 0, the nu^2 coefficient is > 0 unless every sigma_p = 0.

CONCLUSION.  The deficit vanishes to FIRST order transverse to the slice and
first appears at SECOND order.  Its transverse Hessian is the isotropic rank-2
form 2*c2*I_2 -- rank 2 being the two sphere directions, the same 2 as the
-(2/r)B Vekua trace term -- positive definite iff S != 0.  So the ladder is

    slice                      Pi_e        : blind (memo8)
    1st infinitesimal nbhd     Pi_e^(1)    : STILL blind -- adds nothing
    2nd infinitesimal nbhd     Pi_e^(2)    : total collapse, S = 0

i.e. the minimal thickening that sees anything is exactly second order, and it
is already in the collapse regime.  There is no intermediate order.
"""
import numpy as np
import sympy as sp
from math import comb
from scipy.optimize import least_squares
import lab_adhm_num as an

LINE = "=" * 78


def head(s):
    print(); print(LINE); print(s); print(LINE, flush=True)


def build_R1(roots, e):
    """memo8 §2 realisation: T_0 = diag(Re), S = diag(Im), T_a = e_a S, lam = 0."""
    r = np.array(roots, dtype=complex)
    return [np.diag(r.real)] + [e[a] * np.diag(r.imag) for a in range(3)], np.zeros((len(r), 4))


def frame(e):
    """orthonormal n1, n2 spanning the 2-plane transverse to e inside Im H."""
    a = np.eye(3)[np.argmin(np.abs(e))]
    n1 = a - (a @ e) * e; n1 /= np.linalg.norm(n1)
    n2 = np.cross(e, n1); n2 /= np.linalg.norm(n2)
    return n1, n2


E = np.array([0.3, -0.6, 0.74]); E = E / np.linalg.norm(E)
N1, N2 = frame(E)

CASES = [("z^2+1",                       [1j, -1j]),
         ("z^2+z+1",                     [(-1+3**.5*1j)/2, (-1-3**.5*1j)/2]),
         ("(z-1)((z+2)^2+9)",            [1.0, -2+3j, -2-3j]),
         ("(z^2+1)(z^2+4)",              [1j, -1j, 2j, -2j]),
         ("memo5 quartic",               list(np.roots([1., 10., 26., 22., 3.]))),
         ("(z-1)(z-2)  [hyp]",           [1.0, 2.0]),
         ("(z^2-1)(z^2-4) [hyp]",        [1.0, -1.0, 2.0, -2.0])]


# ===================================================================== PART 1
head("PART 1  exact symbolic identity: deficit = 4 nu^2 (...) + O(nu^4)")
x0, t, nu = sp.symbols('x0 t nu', real=True, positive=True)
r2 = t**2 + nu**2


def sym_check(npairs, nreal):
    tau = sp.symbols(f'tau1:{npairs+1}', real=True)
    sig = sp.symbols(f'sigma1:{npairs+1}', positive=True)
    rho = sp.symbols(f'rho1:{nreal+1}', real=True) if nreal else ()
    A = [(x0 - tau[p])**2 for p in range(npairs)]
    B = [A[p] + r2 + sig[p]**2 for p in range(npairs)]
    R = sp.prod([(x0 - rho[m])**2 + r2 for m in range(nreal)]) if nreal else sp.Integer(1)
    detM = R * sp.prod([B[p]**2 - 4*t**2*sig[p]**2 for p in range(npairs)])
    Pp = R * sp.prod([B[p]**2 - 4*r2*sig[p]**2 for p in range(npairs)])
    D = sp.expand(detM - Pp)
    orders = sorted({m for (m,) in sp.Poly(D, nu).monoms()})
    B0 = [A[p] + t**2 + sig[p]**2 for p in range(npairs)]
    pred = 4*R.subs(nu, 0)*sum(sig[p]**2 * sp.prod(
        [B0[q]**2 - 4*t**2*sig[q]**2 for q in range(npairs) if q != p]) for p in range(npairs))
    print(f"  {npairs} conj pair(s) + {nreal} real root(s):  nu-powers present {orders};"
          f"  c1 == 0: {sp.simplify(D.coeff(nu,1))==0};"
          f"  c2 == predicted: {sp.simplify(sp.expand(D.coeff(nu,2)-sp.expand(pred)))==0}", flush=True)


for npairs, nreal in [(1, 0), (1, 1), (2, 0), (2, 1), (1, 2)]:
    sym_check(npairs, nreal)
print("  => the deficit is an EVEN polynomial in nu with no constant term; its")
print("     lowest nonvanishing order is nu^2, with the stated coefficient.")


# ===================================================================== PART 2
head("PART 2  numeric transverse Taylor coefficients, via the real detM / P_p code")
x0v, tv = 0.37, 0.83
print(f"  slice point x_0 = {x0v}, t = {tv};  coefficients of det M - P_p in nu")
print(f"  {'p':<24}{'c0':>11}{'c1':>11}{'c2':>14}{'c3':>11}{'predicted c2':>15}")
for nm, roots in CASES:
    T, lam = build_R1(roots, E); k = len(roots); deg = 2*k
    nuv = np.linspace(-1, 1, deg + 3)
    Q = np.zeros((len(nuv), 4)); Q[:, 0] = x0v
    Q[:, 1:] = tv*E[None, :] + nuv[:, None]*N1[None, :]
    D = an.detM(T, lam, Q) - an.P_target(roots, Q)
    c = np.linalg.lstsq(np.vander(nuv, deg+1, increasing=True), D, rcond=None)[0]
    rr = np.array(roots, dtype=complex); tau_, sig_ = rr.real, rr.imag
    A = (x0v - tau_)**2; B0 = A + tv**2 + sig_**2
    pidx = [j for j in range(k) if sig_[j] > 1e-12]
    ridx = [j for j in range(k) if abs(sig_[j]) <= 1e-12]
    R = np.prod(A[ridx] + tv**2) if ridx else 1.0
    pred = 4*R*sum(sig_[p]**2*np.prod([B0[q]**2 - 4*tv**2*sig_[q]**2
                   for q in pidx if q != p]) for p in pidx)
    print(f"  {nm:<24}{c[0]:>11.2e}{c[1]:>11.2e}{c[2]:>14.6f}{c[3]:>11.2e}{pred:>15.6f}")
print()
print("  isotropy in the transverse 2-plane (spread over 7 directions at nu = 0.3):")
for nm, roots in [("z^2+1", [1j, -1j]), ("memo5 quartic", list(np.roots([1., 10., 26., 22., 3.])))]:
    T, lam = build_R1(roots, E); vals = []
    for th in np.linspace(0, np.pi, 7):
        n = np.cos(th)*N1 + np.sin(th)*N2
        Q = np.zeros((1, 4)); Q[0, 0] = x0v; Q[0, 1:] = tv*E + 0.3*n
        vals.append(float(an.detM(T, lam, Q)[0] - an.P_target(roots, Q)[0]))
    vals = np.array(vals)
    print(f"    {nm:<24} spread {vals.max()-vals.min():.2e}   (mean value {vals.mean():.6f})")


# ===================================================================== PART 3
head("PART 3  the ladder: J0 (slice) / J1 (1st nbhd) / J2 (2nd nbhd) / P1 (slice+point)")
print("""  Each condition is solved by least squares from random starts over the FULL
  admissible ADHM data -- the R1 family is an output, not an input.

    J0 : det M = P_p on the slice Pi_e                      (memo8 R1)
    J1 : J0 plus all FIRST transverse derivatives match     (1st neighbourhood)
    J2 : J1 plus all SECOND transverse derivatives match    (2nd neighbourhood)
    P1 : J0 plus one finite off-slice point                 (memo8 §3(i))

  Caveat: J1/J2 use central differences with h = 1e-3, so residual |S| is
  amplified by h^-1 / h^-2.  The hyperbolic J2 entries are therefore convergence
  artifacts of the optimiser, not signal; the separation to look at is the
  non-hyperbolic plateau (order 1) against the hyperbolic decay.
""")


def slice_points(e, k, seed=0, mult=2):
    dim = comb(2*k+2, 2); rng = np.random.default_rng(seed)
    xy = rng.normal(size=(mult*dim, 2))
    Q = np.zeros((len(xy), 4)); Q[:, 0] = xy[:, 0]
    for a in range(3):
        Q[:, a+1] = xy[:, 1]*e[a]
    return Q


def jet_res(T, lam, roots, base, order, h=1e-3):
    def val(Q):
        return an.detM(T, lam, Q) - an.P_target(roots, Q)
    out = []
    if order >= 1:
        for n in (N1, N2):
            Qp = base.copy(); Qp[:, 1:] += h*n
            Qm = base.copy(); Qm[:, 1:] -= h*n
            out.append((val(Qp) - val(Qm))/(2*h))
    if order >= 2:
        v0 = val(base)
        for n in (N1, N2):
            Qp = base.copy(); Qp[:, 1:] += h*n
            Qm = base.copy(); Qm[:, 1:] -= h*n
            out.append((val(Qp) - 2*v0 + val(Qm))/h**2)
        Qpp = base.copy(); Qpp[:, 1:] += h*(N1+N2)
        Qmm = base.copy(); Qmm[:, 1:] -= h*(N1+N2)
        Qpm = base.copy(); Qpm[:, 1:] += h*(N1-N2)
        Qmp = base.copy(); Qmp[:, 1:] += h*(N2-N1)
        out.append((val(Qpp) + val(Qmm) - val(Qpm) - val(Qmp))/(4*h**2))
    return np.concatenate(out) if out else np.array([])


def solve(k, roots, order, extra=None, ntrials=15, seed=5):
    Q = slice_points(E, k, seed=seed)
    tgt = an.P_target(roots, Q); sc = max(np.abs(tgt).mean(), 1e-12)
    base = slice_points(E, k, seed=seed+101, mult=1)

    def F(z):
        T, lam = an.unpack(z, k)
        r = [an.adhm_residual(T, lam), (an.detM(T, lam, Q) - tgt)/sc]
        if order >= 1:
            r.append(jet_res(T, lam, roots, base, order)/sc)
        if extra is not None:
            t0 = an.P_target(roots, extra)
            r.append((an.detM(T, lam, extra) - t0)/max(abs(t0).mean(), 1e-12))
        return np.concatenate(r)
    rng = np.random.default_rng(seed+1); best, bz = np.inf, None
    for _ in range(ntrials):
        try:
            s = least_squares(F, rng.normal(size=an.nparams(k)), xtol=1e-14,
                              ftol=1e-14, gtol=1e-14, max_nfev=800)
        except Exception:
            continue
        c = float(np.sqrt(2*s.cost))
        if c < best:
            best, bz = c, s.x
    return best, bz


q0 = np.array([[0.4, 0.0, 0.0, 0.9]])
print(f"  {'p':<26}{'J0':>11}{'J1':>11}{'J2':>11}{'P1':>11}   {'|S| at J2 opt':>14}")
for nm, roots in [("z^2+1  (NOT hyp)", [1j, -1j]),
                  ("z^2+z+1  (NOT hyp)", [(-1+3**.5*1j)/2, (-1-3**.5*1j)/2]),
                  ("z^2-1  (hyperbolic)", [1.0, -1.0]),
                  ("(z-1)(z-2) (hyp)", [1.0, 2.0])]:
    k = len(roots)
    r0, _ = solve(k, roots, 0); r1, _ = solve(k, roots, 1)
    r2v, z2 = solve(k, roots, 2); rp, _ = solve(k, roots, 0, extra=q0)
    T, lam = an.unpack(z2, k); S = sum(E[a]*T[a+1] for a in range(3))
    print(f"  {nm:<26}{r0:>11.2e}{r1:>11.2e}{r2v:>11.2e}{rp:>11.2e}   {np.abs(S).max():>14.2e}",
          flush=True)


# ===================================================================== PART 4
head("PART 4  the second-order jet condition IS 'S = 0', at every slice point")
print("  c2 = 4 R sum_p sigma_p^2 prod_{q!=p}(B_q^2 - 4 t^2 sigma_q^2), sampled over")
print("  400 random slice points (x_0, t).  Every factor is strictly positive, so")
print("  c2 > 0 unless every sigma_p = 0.")
print()
print(f"  {'p':<24}{'min c2 over 400 slice pts':>28}{'max c2':>14}{'S = 0':>8}")
rng = np.random.default_rng(3)
for nm, roots in CASES:
    k = len(roots); pts = rng.normal(size=(400, 2)); c2s = []
    rr = np.array(roots, dtype=complex); tau_, sig_ = rr.real, rr.imag
    pidx = [j for j in range(k) if sig_[j] > 1e-12]
    ridx = [j for j in range(k) if abs(sig_[j]) <= 1e-12]
    for a_, b_ in pts:
        A = (a_ - tau_)**2; B0 = A + b_**2 + sig_**2
        R = np.prod(A[ridx] + b_**2) if ridx else 1.0
        c2s.append(4*R*sum(sig_[p]**2*np.prod([B0[q]**2 - 4*b_**2*sig_[q]**2
                   for q in pidx if q != p]) for p in pidx))
    c2s = np.array(c2s)
    print(f"  {nm:<24}{c2s.min():>28.6e}{c2s.max():>14.4e}"
          f"{str(all(abs(np.imag(r))<1e-12 for r in roots)):>8}")

head("SUMMARY")
print("""  The transverse jet order at which a slice condition stops being blind is
  exactly TWO, and at order two the condition is already maximally strong.

    order 0  (the slice itself)        : every real monic p, no information
    order 1  (1st formal neighbourhood): STILL every real monic p -- the deficit
                                         has no linear transverse term at all
    order 2  (2nd formal neighbourhood): forces S = 0, i.e. p hyperbolic; the
                                         transverse Hessian IS the discriminant

  The Hessian is isotropic of rank 2 -- exactly the two sphere directions the
  equivariance quotients out, and the same 2 as the -(2/r)B Vekua trace term.
  Its size is 4 R sum_p sigma_p^2 prod(...), quadratic in the sphere radius, so
  it degrades continuously to 0 as a conjugate pair collides on the axis: the
  Lambda >= 0 consistency requirement of the brief §6.4 is met, now in a sharp
  form (the discriminant is exactly the second transverse jet, and it is exactly
  quadratic in the imaginary parts of the roots).

  What this does NOT do: it does not rescue matching.  The order-2 condition
  collapses the data exactly as a single finite off-slice point does, so the
  rigidity/existence trade-off (brief §3, screen 7) holds at the level of jets
  too, and there is no intermediate order.  What it DOES do is fix the currency:
  any future proposal can now be asked "at what order does your discriminant
  live?", and the answer must be >= 2.""")
