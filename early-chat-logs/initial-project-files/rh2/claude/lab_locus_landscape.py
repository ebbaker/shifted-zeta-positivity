"""
lab_locus_landscape.py  --  RH2, memo 20

Brief section 6.1: "Is there a canonical locus of a source-free Yang-Mills field on R^4
whose topology is constrained -- in particular, one that provably cannot contain a
2-sphere component?"

Part 1  the structural fact:  d_A F+ = d_A F- = 0 SEPARATELY for source-free YM, so F-
        is a covariantly closed ASD 2-form -- a first-order elliptic (Dirac-type) system.
Part 2  the identification: for an ASD 2-form omega = f1 eta1 + f2 eta2 + f3 eta3 on R^4,
        d omega = 0  <=>  df/dx0 = -curl f and div f = 0  <=>  B = f1 i + f2 j + f3 k is
        purely imaginary FUETER-REGULAR.
Part 3  the equivariant sector is zero-free (the predecessor's Vekua verdict, concretely).
Part 4  a 2-SPHERE DOES OCCUR: explicit polynomial source-free YM field on R^4, not
        (anti-)self-dual, with {F- = 0} = S^2 union two curves.

Run: python3 lab_locus_landscape.py [1|2|3|4|all]
"""
import sys, itertools
import sympy as sp

x0,x1,x2,x3 = sp.symbols('x0 x1 x2 x3', real=True); X=[x0,x1,x2,x3]
r2 = x1**2+x2**2+x3**2
def basis2(m,n):
    M=[[0]*4 for _ in range(4)]; M[m][n]=1; M[n][m]=-1; return sp.Matrix(M)
ETA=[basis2(0,1)-basis2(2,3), basis2(0,2)-basis2(3,1), basis2(0,3)-basis2(1,2)]
SDB=[basis2(0,1)+basis2(2,3), basis2(0,2)+basis2(3,1), basis2(0,3)+basis2(1,2)]
def eps(i,j,k,l):
    p=[i,j,k,l]
    if len(set(p))<4: return 0
    s=1
    for a in range(4):
        for b in range(a+1,4):
            if p[a]>p[b]: s=-s
    return s
def hodge(w):
    return sp.Matrix(4,4, lambda m,n: sp.Rational(1,2)*sum(eps(m,n,a,b)*w[a,b]
                     for a in range(4) for b in range(4)))
def d3(w):
    return {(l,m,n): sp.simplify(sp.diff(w[m,n],X[l])+sp.diff(w[n,l],X[m])+sp.diff(w[l,m],X[n]))
            for l,m,n in itertools.combinations(range(4),3)}

def part1():
    print("PART 1 -- d_A F+ = d_A F- = 0 separately")
    print("   Bianchi  d_A F = 0  and  YM  d_A *F = 0,  with *F = F+ - F-, give")
    print("      d_A(F+ + F-) = 0  and  d_A(F+ - F-) = 0   =>   d_A F+ = d_A F- = 0.")
    print("   So F- is a covariantly CLOSED anti-self-dual 2-form (and co-closed, since")
    print("   d_A^* F- = -*d_A*F- = *d_A F- = 0).  Hence (d_A + d_A^*) F- = 0 with")
    print("   d_A + d_A^*: Omega^even(g) -> Omega^odd(g) elliptic with isomorphism symbol.")
    print("   CONSEQUENCES (Aronszajn / Baer, Invent. Math. 138 (1999) 183-202):")
    print("     * strong unique continuation  -> answers brief section 6.2(1) YES;")
    print("     * dim_H {F- = 0} <= 2, countably 2-rectifiable, locally finite H^2,")
    print("       unless F- == 0.  A genuine dimension theorem, not a generic count.\n")

def part2():
    f=[sp.Function(f'f{a}')(*X) for a in (1,2,3)]
    w=f[0]*ETA[0]+f[1]*ETA[1]+f[2]*ETA[2]
    D=d3(w)
    div=sum(sp.diff(f[a],X[a+1]) for a in range(3))
    curl=[sp.diff(f[2],x2)-sp.diff(f[1],x3), sp.diff(f[0],x3)-sp.diff(f[2],x1),
          sp.diff(f[1],x1)-sp.diff(f[0],x2)]
    tgt=[sp.diff(f[a],x0)+curl[a] for a in range(3)]
    vals=list(D.values())
    print("PART 2 -- d(omega) = 0 for ASD omega  <=>  Fueter regularity")
    print("   *eta_a = -eta_a :", [sp.simplify(hodge(e)+e)==sp.zeros(4,4) for e in ETA])
    print("   div f is one component :",
          any(sp.simplify(v-div)==0 or sp.simplify(v+div)==0 for v in vals))
    print("   (df/dx0 + curl f) are the other three :",
          [any(sp.simplify(v-tgt[a])==0 or sp.simplify(v+tgt[a])==0 for v in vals) for a in range(3)])
    print("   The Fueter operator on B = f1 i + f2 j + f3 k has real part -div f and")
    print("   imaginary part df/dx0 + curl f, so  d omega = 0  <=>  B Fueter-regular.")
    print("   Equivalently, on C^2: omega = i ddbar u with u HARMONIC, and {omega=0} is")
    print("   the vanishing locus of the complex Hessian of a harmonic function.\n")

def part3():
    print("PART 3 -- the SO(3)-equivariant sector is ZERO-FREE")
    print("   An SO(3)-equivariant field on R^3 valued in R^3 must be radial: B = phi(x0,r) xhat.")
    print("   A radial field is curl-free, so df/dx0 = -curl f gives d(phi)/dx0 = 0, and")
    print("   div B = 0 gives d(r^2 phi)/dr = 0, hence phi = c/r^2.")
    print("   => B = c xhat / r^2, which has NO ZEROS at all.  This is the predecessor's")
    print("      Vekua obstruction in concrete form: the equivariant class is sphere-free")
    print("      for the trivial reason, and that is exactly why it was useless.\n")

def part4():
    f1=sp.expand(-sp.Rational(5,2)*x0**2*x2 - x0*x1*x3 + sp.Rational(1,2)*x2*(r2-1))
    f2=sp.expand( sp.Rational(5,2)*x0**2*x1 - x0*x2*x3 - sp.Rational(1,2)*x1*(r2-1))
    f3=sp.expand( x0*(-5*x0**2 + 6*x1**2 + 6*x2**2 + 3*x3**2 - 3)/3)
    F=[f1,f2,f3]
    om=sp.Matrix(f1*ETA[0]+f2*ETA[1]+f3*ETA[2]); omp=sp.Matrix(SDB[0])
    Fm=sp.Matrix(om+omp); star=sp.simplify(hodge(Fm))
    div=sum(sp.diff(F[a],X[a+1]) for a in range(3))
    curl=[sp.diff(F[2],x2)-sp.diff(F[1],x3), sp.diff(F[0],x3)-sp.diff(F[2],x1),
          sp.diff(F[1],x1)-sp.diff(F[0],x2)]
    print("PART 4 -- an explicit source-free YM field on R^4 whose {F-=0} contains a 2-SPHERE")
    for a in range(3): print(f"   f{a+1} =", F[a])
    print("   Fueter:  div f =", sp.simplify(div), "  df/dx0 + curl f =",
          [sp.simplify(sp.diff(F[a],x0)+curl[a]) for a in range(3)])
    print("   F = omega- + omega+  with omega+ = e01+e23 constant self-dual.")
    print("   dF  = 0 (Bianchi) :", all(v==0 for v in d3(Fm).values()))
    print("   d*F = 0 (YM)      :", all(v==0 for v in d3(star).values()))
    print("   F- = omega :", sp.simplify((Fm-star)/2-om)==sp.zeros(4,4),
          "   F+ = omega+ nonzero  => NOT (anti-)self-dual")
    print("   ZERO SET:")
    for a in range(3): print(f"     f{a+1}|_(x0=0) =", sp.factor(sp.expand(F[a].subs(x0,0))))
    print("     on {x1=x2=0}:  f1=f2=0 and f3 =", sp.factor(sp.expand(F[2].subs({x1:0,x2:0}))))
    print("     => {F-=0} = S^2  U  {x1=x2=x0=0}  U  {x1=x2=0, x3^2-(5/3)x0^2=1}")
    print("        the 2-dimensional part is exactly the unit 2-sphere in the hyperplane x0=0.")
    E=sp.expand(sum(Fm[m,n]**2 for m in range(4) for n in range(4))/2)
    print(f"   |F|^2 is a polynomial of degree {sp.total_degree(E)}  => INFINITE energy on R^4;")
    print("   holonomy is abelian => REDUCIBLE.  Both caveats matter: see memo 20 section 3.\n")

if __name__=='__main__':
    w=sys.argv[1] if len(sys.argv)>1 else 'all'
    if w in ('1','all'): part1()
    if w in ('2','all'): part2()
    if w in ('3','all'): part3()
    if w in ('4','all'): part4()
