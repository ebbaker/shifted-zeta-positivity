"""
lab_product_object.py -- Working memo #25.

What object does Xi become in the Yang-Mills context, if the PRODUCT formula
(not the sum/moment formula) is the natural one?  Answer, certified here:

    Xi  <->  det(Delta^dag Delta)          (a determinant IS a product)
    log <->  a BIHARMONIC potential on R^4 (log|x| is the box^2 Green's fn)
    box^2 log det  =  the YM action density (Osborn's identity, DHKM App. C)
    zeros of the product  <->  instanton POSITIONS
    Im(zero)              <->  instanton SIZE

PART 1  box^2 log|x| in R^4, and the exact charge-1 density.
PART 2  't Hooft data: det f^{-1} = phi * prod|x-X_i|^2, and the exact
        cancellation of the point masses that a nonzero size buys.
PART 3  When does the product object HAVE k real roots?  Exactly when the four
        ADHM position matrices commute -- the roots are their simultaneous
        eigenvalues.  Certified by direct search.
PART 4  Gauge-group (in)dependence: the degree of det f^{-1} is 2k for every N.
"""
import numpy as np, sympy as sp, mpmath as mp
from scipy.optimize import minimize
def hline(s): print("\n"+s+"\n"+"-"*len(s))
rng = np.random.default_rng(7)

# ============================================================ PART 1
hline("PART 1 -- log|x| is the biharmonic Green's function of R^4")
r, c = sp.symbols('r c', positive=True)
def box(f):                                  # radial Laplacian in R^4
    return sp.simplify(sp.diff(f, r, 2) + 3*sp.diff(f, r)/r)
print("  box(log r)          =", sp.simplify(box(sp.log(r))), "   (= 2/r^2)")
print("  box(2/r^2)          =", sp.simplify(box(2/r**2)), "   => box^2 log r = 0 for r>0")
print("  (1/(4 pi^2 r^2) is the Laplace Green's fn in R^4, so box^2 log r = -8 pi^2 delta)")
F = -sp.log(r**2 + c)
d = sp.simplify(box(box(F)))
print("\n  charge-1 datum: tr_k log f = -log(|x|^2 + c),  c = 2 rho^2")
print("  box^2 (-log(r^2+c)) =", sp.factor(d))
fn1 = sp.lambdify(r, d.subs(c, 1))
Inum = mp.quad(lambda t: fn1(t)*2*mp.pi**2*t**3, [0, 1, 10, mp.inf])
print(f"  integral over R^4   = {mp.nstr(Inum,12)}  vs 16 pi^2 = {mp.nstr(16*mp.pi**2,12)}")
print(f"  (closed form: 96 c^2/(r^2+c)^4 integrates to exactly 16 pi^2 for every c)")
print("\n  concentration as the size -> 0 (fraction of the 16 pi^2 inside r < 0.1):")
for cc in [1.0, 1e-1, 1e-2, 1e-3, 1e-4]:
    fn = sp.lambdify(r, d.subs(c, cc))
    m = mp.quad(lambda t: fn(t)*2*mp.pi**2*t**3, [0, 0.1])/(16*mp.pi**2)
    print(f"    c = {cc:8.1e}   mass(r<0.1)/16pi^2 = {float(m):.6f}")
print("  => the smooth density converges to 16 pi^2 * delta.  A zero-size")
print("     instanton IS a point mass of the biharmonic potential.")

# ============================================================ PART 2
hline("PART 2 -- 't Hooft data: det f^{-1} = phi * prod |x-X_i|^2")
print("  f^{-1} = 2 wbar w + sum_n (a'_n + x_n)^2 ;  't Hooft: a' diagonal (centres),")
print("  all w_i aligned => 2 wbar w = 2 rho rho^T, rank one.  Matrix-determinant")
print("  lemma then gives det f^{-1} = (prod_i d_i) * (1 + sum_i 2 rho_i^2 / d_i),")
print("  d_i = |x - X_i|^2.  The second factor is the 't Hooft phi.\n")
print(f"  {'k':>2s} {'max rel. error over 400 random points':>40s}")
for k in [1,2,3,4,5]:
    worst = 0.0
    for _ in range(400):
        X = rng.normal(size=(k,4)); rho = np.abs(rng.normal(size=k))+0.2
        x = rng.normal(size=4)*1.5
        dd = np.array([np.sum((x-X[i])**2) for i in range(k)])
        A = np.diag(dd) + 2*np.outer(rho, rho)
        lhs = np.linalg.det(A)
        rhs = np.prod(dd)*(1 + np.sum(2*rho**2/dd))
        worst = max(worst, abs(lhs-rhs)/abs(rhs))
    print(f"  {k:2d} {worst:40.3e}")

print("\n  the point masses cancel exactly.  log det f^{-1} = log phi + sum log d_i,")
print("  and near a centre  phi ~ 2 rho_i^2/d_i,  so the two log singularities")
print("  cancel and log det f^{-1} -> log(2 rho_i^2) + regular.  Checked:")
k = 3
X = np.array([[0.,0,0,0],[1.,0.5,0,0],[-0.7,0.2,0.4,0]]); rho = np.array([0.6,0.4,0.9])
def logdet(x):
    dd = np.array([np.sum((x-X[i])**2) for i in range(k)])
    return np.log(np.linalg.det(np.diag(dd)+2*np.outer(rho,rho)))
print(f"    {'dist to centre 0':>18s} {'log det f^{-1}':>18s}")
for e in [1e-1,1e-2,1e-3,1e-4,1e-6,1e-8]:
    x = X[0]+np.array([e,0,0,0]); print(f"    {e:18.1e} {logdet(x):18.10f}")
print(f"    limit predicted: log(2 rho_0^2 * prod_{{i>0}} d_i(X_0)) = "
      f"{np.log(2*rho[0]**2*np.prod([np.sum((X[0]-X[i])**2) for i in [1,2]])):.10f}")
print("  => with a NONZERO size the potential is smooth at the centre and the")
print("     action density is smooth and positive.  Set every size to zero and")
print("     phi == 1: the cancellation switches off and box^2 log det is pure")
print("     point masses -- k charges, no field.")

# ============================================================ PART 3
hline("PART 3 -- when does the product object have k real roots?")
print("  det[sum_n (a'_n + x_n)^2] = 0 at a real x  <=>  the four Hermitian k x k")
print("  matrices a'_n have a COMMON null vector for (a'_n + x_n), i.e. -x is a")
print("  SIMULTANEOUS eigenvalue.  So the roots of the product object are the")
print("  simultaneous eigenvalues of the position matrices, and they exist only")
print("  on the commuting locus.  Direct search over x in R^4:\n")
def detQ(x, A):
    k = A[0].shape[0]
    S = np.zeros((k,k), dtype=complex)
    for n in range(4): S += (A[n]+x[n]*np.eye(k)) @ (A[n]+x[n]*np.eye(k))
    return np.real(np.linalg.det(S))
def herm(k):
    M = rng.normal(size=(k,k))+1j*rng.normal(size=(k,k)); return (M+M.conj().T)/2
print(f"  {'case':38s} {'k':>2s} {'min_x det (best of 25 starts)':>32s}")
for k in [2,3,4]:
    # commuting: simultaneously diagonalisable with real eigenvalues
    U = np.linalg.qr(rng.normal(size=(k,k))+1j*rng.normal(size=(k,k)))[0]
    Ac = [U @ np.diag(rng.normal(size=k)) @ U.conj().T for _ in range(4)]
    An = [herm(k) for _ in range(4)]
    for label, A in [("commuting a'_n  (simultaneous eigs)", Ac),
                     ("generic non-commuting a'_n        ", An)]:
        best = np.inf
        for _ in range(25):
            res = minimize(detQ, rng.normal(size=4)*2, args=(A,), method="Nelder-Mead",
                           options={"maxiter":1500,"xatol":1e-12,"fatol":1e-16})
            best = min(best, res.fun)
        comm = max(np.linalg.norm(A[i]@A[j]-A[j]@A[i]) for i in range(4) for j in range(4))
        print(f"  {label:38s} {k:2d} {best:32.4e}   ||[a,a]||={comm:.2e}")
print("\n  => commuting: the determinant reaches 0 (the k real roots exist).")
print("     non-commuting: bounded away from 0 -- NO real roots at all, so the")
print("     product object cannot be a product of real quadratic factors.")

# ============================================================ PART 4
hline("PART 4 -- gauge group: the degree of det f^{-1} is 2k, independent of N")
print("  f^{-1} = 2 wbar^adot w_adot + sum_n (a'_n + x_n)^2 :  w is N x k, and it")
print("  enters WITHOUT x.  So N changes only the constant term.\n")
print(f"  {'N':>3s} {'k':>2s} {'deg_x det f^{-1}':>18s} {'#moduli 4kN':>12s}")
for N in [2,3,4,6]:
    for k in [1,2,3]:
        A = [herm(k) for _ in range(4)]
        W = rng.normal(size=(N,k))+1j*rng.normal(size=(N,k))
        WW = 2*np.real(W.conj().T @ W); WW = (WW+WW.T)/2
        # degree in a single direction t: det f^{-1}(t*e_1) is a polynomial in t
        ts = np.linspace(-1,1,4*k+6)
        vals = []
        for t in ts:
            S = WW.astype(complex)
            for n in range(4):
                B = A[n] + (t if n==0 else 0.0)*np.eye(k); S += B@B
            vals.append(np.real(np.linalg.det(S)))
        co = np.polyfit(ts, vals, 2*k+2)
        deg = max(i for i,cc in enumerate(co[::-1]) if abs(cc) > 1e-8*max(abs(co)))
        print(f"  {N:3d} {k:2d} {deg:18d} {4*k*N:12d}")
print("\n  => the shape of the product object is set by the charge k alone.")
print("     Changing the gauge group buys moduli, not factors.  And the whole")
print("     of Part 3 is a statement about k x k Hermitian matrices, so it is")
print("     identical for every classical group (and ADHM has no exceptional case).")
