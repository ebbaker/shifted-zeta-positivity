"""
lab_positivity_refuted.py   --  RH2, memo 18

Settles brief 3.7 / memo12 0(2):

    M(q) = C + |q|^2 I - 2 sum_a x_a T_a,   T_a real k x k arbitrary,
    C real symmetric,  det M(q) = P_p(q) = p(x0+ir) p(x0-ir)  on all of H.

    Conjecture (memo 12):  C >= 0  ==>  p hyperbolic.
    Verdict: TRUE at k=2 (Theorem A, an exact equivalence); FALSE at k=4.

Part 1  symbolic: all eight k=2 coefficient conditions, and the sl(2,R) Gram.
Part 2  exact (rational): the two k=4 counterexamples B1 and B2.
Part 3  the quaternionic contrast family (Omega < 0), numerically.
Part 4  the PSD-constrained search table (see memo 18 section 4 for the record).
Part 5  Theorem C: the general Clifford member, with SIMPLE conjugate roots OFF the
        imaginary axis and C positive definite.  Exact integer instance.

Run:  python3 lab_positivity_refuted.py [1|2|3|4|5|all]
"""
import sys
import numpy as np

# ----------------------------------------------------------------- helpers
def Pp(p, x):
    """p(x0+ir) p(x0-ir) at a real quaternion x = (x0,x1,x2,x3)."""
    z = x[0] + 1j*np.linalg.norm(x[1:])
    w = np.polyval(p, z)
    return (w*np.conj(w)).real

def detM(C, T, x):
    k = C.shape[0]
    return np.linalg.det(C + float(x@x)*np.eye(k) - 2*sum(x[a]*T[a] for a in range(4)))

def check_full_H(C, T, p, n=6000, seed=0, label=""):
    rng = np.random.default_rng(seed)
    X = rng.normal(scale=1.6, size=(n, 4))
    err = np.array([abs(detM(C, T, x) - Pp(p, x)) for x in X])
    sc  = np.array([abs(Pp(p, x)) for x in X]).mean()
    print(f"   {label} full-H match over {n} random q: max rel err = {err.max()/sc:.3e}")
    return err.max()/sc

# ---------------------------------------------- PART 1: k=2, symbolically
def part1():
    import sympy as sp
    u, v, s, d = sp.symbols('u v s d')
    mk = lambda n: sp.Matrix(2, 2, lambda i, j: sp.Symbol(f'{n}{i}{j}'))
    T0, Te = mk('a'), mk('t')
    c00, c01, c11 = sp.symbols('c00 c01 c11')
    C = sp.Matrix([[c00, c01], [c01, c11]])
    I2, I = sp.eye(2), sp.I
    N, Nb = T0 + I*Te, T0 - I*Te

    P = sp.Poly(sp.expand((u*v*I2 - u*N - v*Nb + C).det()
                          - (u**2 - s*u + d)*(v**2 - s*v + d)), u, v)
    claims = {
        (2,1): -(sp.trace(N) - s),
        (1,2): -(sp.trace(Nb) - s),
        (2,0):  (N.det() - d),
        (0,2):  (Nb.det() - d),
        (1,1):  (sp.trace(C) + sp.trace(N)*sp.trace(Nb) - sp.trace(N*Nb) - s**2),
        (1,0): -(sp.trace(N)*sp.trace(C) - sp.trace(N*C)) + s*d,
        (0,1): -(sp.trace(Nb)*sp.trace(C) - sp.trace(Nb*C)) + s*d,
        (0,0):  (C.det() - d**2),
    }
    print("PART 1  --  k=2 coefficient conditions of det(uvI - uN - vNbar + C) = p(u)p(v)")
    ok = True
    for mon in sorted(claims):
        co = sp.expand(P.coeff_monomial(u**mon[0]*v**mon[1]))
        good = sp.expand(co - sp.expand(claims[mon])) == 0
        ok &= good
        print(f"   u^{mon[0]} v^{mon[1]} : {good}")
    print("   ALL EIGHT MATCH:", ok)

    h  = sp.Matrix([[1,0],[0,-1]]); m = sp.Matrix([[0,1],[1,0]]); J = sp.Matrix([[0,-1],[1,0]])
    B  = sp.Matrix(3,3, lambda a,b: sp.trace([h,m,J][a]*[h,m,J][b]))
    print("   Gram of tr(XY) on sl(2,R) in basis (h,m,J):", B.tolist(),
          "-> signature (2,1); hence kappa = 0.")
    print("   Endgame: kappa=0 => d = det T0, tr C = tr T0^2 = s^2 - 2d;")
    print("            C>=0 => tr C >= 2 sqrt(det C) = 2|d| => disc(p) = s^2-4d >= 0.")
    print("   Converse: p hyperbolic => tr C = r1^2+r2^2 >= 0, det C = (r1 r2)^2 >= 0 => C>=0.")
    print("   THEOREM A:  at k=2,  C >= 0  <=>  p hyperbolic.   spec(C) = {rho_1^2, rho_2^2}.\n")

# ------------------------------------- PART 2: the k=4 counterexamples
def clifford_blocks():
    """real 4x4, traceless, anticommuting, T_a^2 = +I  (a Cl_{3,0}(R) module)."""
    kron = np.kron
    s3  = np.array([[1.,0],[0,-1]]); s1 = np.array([[0.,1],[1,0]])
    is2 = np.array([[0.,1],[-1,0]]); I2 = np.eye(2)
    return [kron(s3,I2), kron(s1,I2), kron(is2,is2)], kron(I2, is2)   # blocks, J

def part2():
    import sympy as sp
    x0,x1,x2,x3,r,u = sp.symbols('x0 x1 x2 x3 r u')
    I, R = sp.I, sp.Rational
    kron = lambda A,B: sp.Matrix(sp.BlockMatrix(
        [[A[i,j]*B for j in range(A.cols)] for i in range(A.rows)]))
    s3  = sp.Matrix([[1,0],[0,-1]]); s1 = sp.Matrix([[0,1],[1,0]])
    is2 = sp.Matrix([[0,1],[-1,0]]); I2, I4 = sp.eye(2), sp.eye(4)
    CL = [kron(s3,I2), kron(s1,I2), kron(is2,is2)]
    J  = kron(I2, is2)
    assert all(M*M == I4 for M in CL)
    assert all(CL[i]*CL[j] + CL[j]*CL[i] == sp.zeros(4) for i in range(3) for j in range(3) if i != j)
    assert all(sp.trace(M) == 0 for M in CL)
    assert J*J == -I4 and all(J*M == M*J for M in CL)
    print("PART 2  --  exact (rational) verification of the k=4 counterexamples")
    print("   Clifford blocks: real, traceless, anticommuting, T_a^2 = +I.  OK")

    q2 = x0**2 + x1**2 + x2**2 + x3**2
    def verify(T0, Ts, C, pfun, name):
        M = C + q2*I4 - 2*(x0*T0 + x1*Ts[0] + x2*Ts[1] + x3*Ts[2])
        lhs = sp.expand(M.det())
        rhs = sp.expand(sp.expand(pfun(x0+I*r)*pfun(x0-I*r)).subs(r**2, x1**2+x2**2+x3**2))
        z = sp.expand(lhs - rhs)
        ev = sp.Matrix(C).eigenvals()
        print(f"   {name}:  det M - P_p = {z}   (zero: {z==0});  spec(C) = {list(ev)}")
        print(f"      p(u) = {sp.factor(sp.expand(pfun(u)))},  roots {sp.roots(sp.Poly(sp.expand(pfun(u)),u))}")
        return z == 0

    a, s = R(3,5), 1
    ok1 = verify(a*I4, CL, (a**2+s**2)*I4, lambda w: ((w-a)**2 + s**2)**2,
                 "B1  T0=aI,  C=(a^2+s^2)I  [DOUBLED pair]")
    b, s = R(1,2), R(3,2)
    ok2 = verify(b*J, [s*M for M in CL], (s**2-b**2)*I4,
                 lambda w: (w**2 + (s+b)**2)*(w**2 + (s-b)**2),
                 "B2  T0=bJ,  C=(s^2-b^2)I  [2 SIMPLE pairs]")
    print("   BOTH EXACT:", ok1 and ok2, " -- C is positive definite in both. 3.7 IS FALSE.\n")

    CLn, Jn = clifford_blocks()
    for (T0, Ts, C, p, nm) in [
        (0.6*np.eye(4), CLn, 1.36*np.eye(4), np.polymul([1,-1.2,1.36],[1,-1.2,1.36]), "B1"),
        (0.5*Jn, [1.5*M for M in CLn], 2.0*np.eye(4), np.polymul([1,0,1],[1,0,4]),   "B2")]:
        check_full_H(C, [T0]+list(Ts), np.array(p, float), label=nm)
    print()

# ------------------------------- PART 3: quaternionic contrast (Omega < 0)
def part3():
    print("PART 3  --  the quaternionic branch, Omega = T_e^2 = -I  (contrast case)")
    def qmul(a,b):
        a0,a1,a2,a3=a; b0,b1,b2,b3=b
        return np.array([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                         a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0])
    E = np.eye(4)
    L = lambda mu: np.column_stack([qmul(mu, E[c]) for c in range(4)])
    Rm= lambda mu: np.column_stack([qmul(E[c], mu) for c in range(4)])
    Ls = [L(E[1]), L(E[2]), L(E[3])]
    print("   L_a^2 = -I:", [bool(np.allclose(M@M, -np.eye(4))) for M in Ls],
          "  kappa = tr(L_a^2) =", float(np.trace(Ls[0]@Ls[0])))
    for mu, tag in [(np.array([0,.3,-.5,.387298]), "mu purely imaginary"),
                    (np.array([1.4,0,0,0]),        "mu real, |mu| > 1")]:
        T0 = Rm(mu); C = T0@T0 - np.eye(4)
        p  = np.poly(T0 + 1j*Ls[0]).real
        rt = np.roots(p)
        print(f"   {tag}: C = {np.round(np.linalg.eigvalsh(C),4)} (PSD: "
              f"{bool(np.linalg.eigvalsh(C).min() >= -1e-12)}),  max|Im root| = "
              f"{abs(rt.imag).max():.2e}  -> "
              f"{'NON-hyperbolic' if abs(rt.imag).max()>1e-6 else 'hyperbolic'}")
        check_full_H(C, [T0]+Ls, p, n=4000, label="   ")
    print("   => sign(Omega) decides hyperbolicity; C>=0 is achievable on either branch.\n")

# --------------------------------------------------- PART 4: search record
SEARCH_TABLE = """PART 4  --  PSD-constrained search record (C = LL^T, T_a free, 76 sample points)
   k  p                          roots                best RMS   reading
   2  z^2+1                      simple pair          4.4e-02    plateau (Theorem A)
   4  (z^2+1)^2                  doubled pair         2.9e-15    solved (B1)
   4  ((z-.6)^2+1)^2             doubled pair         4.7e-15    solved (B1)
   4  (z^2+1)(z^2+4)             2 simple pairs       8.9e-06    solved exactly (B2)
   4  near-miss quartic          simple pair off-axis 1.3e-07    INCONCLUSIVE
   Calibration: (z^2+1)(z^2+4) is exactly solvable (B2) yet the optimiser only
   reached 8.9e-06 on the same budget, so 1.3e-07 is NOT evidence of a plateau.
"""

# ------------------------------------------- PART 5: Theorem C (off-axis roots)
def part5():
    import sympy as sp
    x0,x1,x2,x3,r,u=sp.symbols('x0 x1 x2 x3 r u'); I=sp.I
    kron=lambda A,B: sp.Matrix(sp.BlockMatrix([[A[i,j]*B for j in range(A.cols)] for i in range(A.rows)]))
    s3=sp.Matrix([[1,0],[0,-1]]);s1=sp.Matrix([[0,1],[1,0]]);is2=sp.Matrix([[0,1],[-1,0]])
    I2,I4=sp.eye(2),sp.eye(4)
    Mc=[kron(s3,I2),kron(s1,I2),kron(is2,is2)]; Jc=kron(I2,is2)
    assert all(A*A==I4 for A in Mc) and Jc*Jc==-I4 and all(Jc*A==A*Jc for A in Mc)
    print("PART 5  --  Theorem C: T_0 = z, T_a = M_a w, C = (z^2+w^2) I,  z^2+w^2 real > 0")
    a,b,sg,ta = 3,1,3,-1                     # z = a+bJ, w = sg+ta J ;  ab+sg*ta = 0
    lam = a*a-b*b+sg*sg-ta*ta
    T0 = a*I4+b*Jc; Ts=[A*(sg*I4+ta*Jc) for A in Mc]; C=lam*I4
    r1 = sp.expand((a+b*I)+I*(sg+ta*I)); r2 = sp.expand((a+b*I)-I*(sg+ta*I))
    pu = sp.expand((u-r1)*(u-sp.conjugate(r1))*(u-r2)*(u-sp.conjugate(r2)))
    q2=x0**2+x1**2+x2**2+x3**2
    Mq=C+q2*I4-2*(x0*T0+x1*Ts[0]+x2*Ts[1]+x3*Ts[2])
    pf=sp.Lambda(u,pu)
    rhs=sp.expand(sp.expand(pf(x0+I*r)*pf(x0-I*r)).subs(r**2,x1**2+x2**2+x3**2))
    d=sp.expand(Mq.det()-rhs)
    print(f"   z = {a}+{b}i, w = {sg}{ta}i,  ab+sigma*tau = {a*b+sg*ta},  lambda = {lam}")
    print(f"   C = {lam} * I_4  (positive definite);  tr T_a = {[sp.trace(A) for A in Ts]}")
    print(f"   p(u) = {sp.factor(pu)}")
    print(f"   roots = {sp.roots(sp.Poly(pu,u))}   <-- FOUR SIMPLE roots, real parts 4 and 2")
    print(f"   det M - P_p = {d}   IDENTICALLY ZERO: {d==0}")
    cs=sp.Poly(pu,u).all_coeffs()
    print(f"   Theorem D check (C = lam I => c0 = lam^2, c1 = lam c3): "
          f"{cs[4]}={lam**2}, {cs[3]}={lam*cs[1]}")
    print("   => a SIMPLE conjugate pair OFF the imaginary axis is realisable with C > 0.\n")

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which in ('1','all'): part1()
    if which in ('2','all'): part2()
    if which in ('3','all'): part3()
    if which in ('4','all'): print(SEARCH_TABLE)
    if which in ('5','all'): part5()
