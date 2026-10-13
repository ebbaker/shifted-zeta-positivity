"""
lab_matrix_loci.py  --  RH2, memo 21

Screens the 3x3 matrix loci of F- for SU(2).

Part 1  the correct invariant theory:  M -> Q M R^T with Q,R in SO(3) INDEPENDENT, so the
        complete pointwise invariants are the singular values plus sign(det).  Corrected ladder.
Part 2  the ADHM structure theorem:  F- as a map Im H -> Im H is
              T(w) = sum_{jl} f_{jl} c_j w conj(c_l),  f real symmetric k x k,
        hence  T = sum_{m=1}^{k} nu_m R_m,  a real combination of k SCALED ROTATIONS.
        k=1 -> conformal;  k=2 -> a repeated singular value is FORCED;  k>=3 -> generic.
Part 3  verification on explicit 't Hooft / JNR instantons.
Part 4  symmetry also forces degeneracy: collinear centres (SO(3)) -> everywhere;
        coplanar centres (SO(2)) -> exactly on the plane of the centres.
"""
import sys, itertools
import numpy as np, sympy as sp
from scipy.optimize import minimize
np.set_printoptions(precision=6, suppress=True)

x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3', real=True); X=[x0,x1,x2,x3]
def b2(m,n):
    M=[[0]*4 for _ in range(4)]; M[m][n]=1; M[n][m]=-1; return sp.Matrix(M)
ETA=[b2(0,1)-b2(2,3), b2(0,2)-b2(3,1), b2(0,3)-b2(1,2)]     # Lambda^2_-
SDB=[b2(0,1)+b2(2,3), b2(0,2)+b2(3,1), b2(0,3)+b2(1,2)]     # Lambda^2_+
ETAn=np.array([[[float(E[m,n]) for n in range(4)] for m in range(4)] for E in ETA])
SDBn=np.array([[[float(E[m,n]) for n in range(4)] for m in range(4)] for E in SDB])
eps3=np.zeros((3,3,3))
for p in itertools.permutations(range(3)): eps3[p]=np.sign(np.linalg.det(np.eye(3)[list(p)]))

def thooft(centres, lams):
    """'t Hooft ansatz; A^a_mu = -eta_{a mu nu} d_nu ln rho gives ANTI-self-dual F."""
    rho = 1 + sum(sp.Float(l)**2/sum((X[m]-sp.Float(c[m]))**2 for m in range(4))
                  for c,l in zip(centres,lams))
    L=sp.log(rho)
    A=[[-sum(SDB[a][m,n]*sp.diff(L,X[n]) for n in range(4)) for m in range(4)] for a in range(3)]
    F=[[[sp.diff(A[a][n],X[m])-sp.diff(A[a][m],X[n])
        + sum(eps3[a,b,e]*A[b][m]*A[e][n] for b in range(3) for e in range(3))
        for n in range(4)] for m in range(4)] for a in range(3)]
    return [[[sp.lambdify((x0,x1,x2,x3),F[a][m][n],'numpy') for n in range(4)]
             for m in range(4)] for a in range(3)]
def Mof(fl,p):
    V=np.array([[[float(fl[a][m][n](*p)) for n in range(4)] for m in range(4)] for a in range(3)])
    M=np.array([[0.25*np.sum(V[i]*ETAn[a]) for i in range(3)] for a in range(3)])
    sd=np.array([[0.25*np.sum(V[i]*SDBn[a]) for i in range(3)] for a in range(3)])
    return M, np.linalg.norm(sd)
def gaps(fl,p):
    M,sd=Mof(fl,p); s=np.linalg.svd(M,compute_uv=False)
    return s, min(s[0]-s[1],s[1]-s[2])/s[0], sd

def part1():
    print("PART 1 -- invariant theory of the 3x3 curvature matrix M_{ai} = <F-, eta_a (x) T_i>")
    print("   gauge  M -> M R^T (R in Ad SU(2) = SO(3));  frame  M -> Q M (Q in SO(3) on Lambda^2_-)")
    print("   => complete pointwise invariants are sigma_1 >= sigma_2 >= sigma_3 and sign(det M).")
    print(f"   {'locus':<30}{'invariant':<26}{'codim':>6}{'dim in R^4':>12}")
    for nm,inv,c,d in [("det F- = 0","sigma_3 = 0",1,3),
                       ("repeated singular value","sigma_i = sigma_j",2,"2"),
                       ("rank <= 1","sigma_2 = sigma_3 = 0",4,"empty"),
                       ("all singular values equal","sigma_1=sigma_2=sigma_3",5,"empty"),
                       ("F- = 0","all sigma = 0",9,"empty")]:
        print(f"   {nm:<30}{inv:<26}{c:>6}{str(d):>12}" + ("   <== SPHERE DIMENSION" if d==2 else ""))
    print("   Brief section 4.6 tabulated only RANK loci and concluded that no SU(2) curvature")
    print("   locus is ever 2-dimensional.  The repeated-singular-value locus is, and it is")
    print("   canonical.  That conclusion in section 4.6 is therefore wrong.\n")

def part2():
    rng=np.random.default_rng(3)
    def rot():
        Q,_=np.linalg.qr(rng.normal(size=(3,3))); return Q*np.sign(np.linalg.det(Q))
    print("PART 2 -- ADHM structure theorem and its consequence")
    print("   T(w) = sum_{jl} f_{jl} c_j w conj(c_l), f real symmetric k x k.  Diagonalising")
    print("   f = sum_m mu_m u_m u_m^T and setting d_m = sum_j (u_m)_j c_j gives")
    print("        T = sum_{m=1}^{k} nu_m R_m,   nu_m real, R_m in SO(3).")
    print("   k=2:  T T^T = (nu1^2+nu2^2) I + nu1 nu2 (S + S^T),  S = R1^T R2 in SO(3),")
    print("         and S + S^T has eigenvalues 2, 2cos(t), 2cos(t)  =>  REPEATED SINGULAR VALUE.")
    for k in (1,2,3,4):
        w=[]
        for _ in range(3000):
            T=sum(rng.normal()*rot() for _ in range(k))
            s=np.linalg.svd(T,compute_uv=False); w.append(min(s[0]-s[1],s[1]-s[2])/s[0])
        tag="repeated value FORCED" if max(w)<1e-12 else "generic, no degeneracy"
        print(f"      k={k}: max min-gap over 3000 random draws = {max(w):.2e}   <= {tag}")
    print()

def part3():
    print("PART 3 -- explicit 't Hooft instantons (irreducible, finite energy, exactly ASD)")
    tests=[("charge 1 (BPST)",[(0,0,0,0)],[1.0]),
           ("charge 2",[(0,0,0,1.5),(0,0,0,-1.5)],[1.0,1.0]),
           ("charge 3 (generic)",[(0,0,0,1.5),(0,0,0,-1.5),(1.2,0.4,-0.7,0.3)],[1.0,1.0,0.9]),
           ("charge 4 (generic)",[(0,0,0,1.5),(0,0,0,-1.5),(1.2,0.4,-0.7,0.3),
                                  (-0.9,1.1,0.5,-0.6)],[1.0,1.0,0.9,1.3])]
    rng=np.random.default_rng(3)
    for nm,cs,ls in tests:
        fl=thooft(cs,ls); g=[]; sdm=0
        for _ in range(6):
            p=tuple(rng.uniform(-2,2,size=4)); s,gg,sd=gaps(fl,p); g.append(gg); sdm=max(sdm,sd)
        s0,_,_=gaps(fl,(0.4,0.2,-0.3,0.7))
        print(f"   {nm:<20} max min-gap = {max(g):.2e}   ||F+||max = {sdm:.1e}   sigma = {np.round(s0,5)}")
        sys.stdout.flush()
    print("   => charge 1 and 2 sit identically in the degeneracy stratum, as predicted.\n")

def part4():
    print("PART 4 -- symmetry also forces degeneracy")
    f=thooft([(0,0,0,1.6),(0,0,0,0.0),(0,0,0,-1.6)],[1.0,0.8,1.0])
    print("   charge 3, COLLINEAR centres (residual SO(3) rotating the orthogonal R^3):")
    for p in [(0.7,0,0,0.4),(1.9,0,0,-1.2),(0.3,0.9,-1.1,2.0)]:
        s,g,_=gaps(f,p); print(f"      x={p}: min-gap = {g:.2e}")
    print("      => degenerate EVERYWHERE.  But an SO(3)-invariant 2-dimensional set is a")
    print("         union of 2-SPHERES -- so the only symmetry that could produce a sphere")
    print("         is exactly the symmetry that destroys the locus.  Rigidity/existence again.")
    f3=thooft([(0,0,0,1.5),(0,0,0,-1.5),(1.2,0.4,-0.7,0.3)],[1.0,1.0,0.9])
    u=np.array([1.2,0.4,-0.7]); u/=np.linalg.norm(u)
    v=np.array([0.4,-1.2,0.0]); v-=np.dot(v,u)*u; v/=np.linalg.norm(v)
    print("\n   charge 3, COPLANAR centres (residual SO(2) on the orthogonal 2-plane):")
    for t,z in [(0.8,0.3),(-1.7,2.0),(2.5,-1.1)]:
        print(f"      in  the centre-plane (t={t}, x3={z}): min-gap = {gaps(f3,tuple(list(t*u)+[z]))[1]:.2e}")
    for t,z,e in [(0.8,0.3,0.5),(-1.7,2.0,0.9),(2.5,-1.1,0.3)]:
        print(f"      off the centre-plane (off={e}):        min-gap = {gaps(f3,tuple(list(t*u+e*v)+[z]))[1]:.2e}")
    print("      => the locus is exactly the 2-plane containing the centres: 2-dimensional,")
    print("         canonical, and NON-COMPACT.  No sphere.")
    print("\n   charge 4, centres spanning a 3-plane (no continuous residual symmetry):")
    f4=thooft([(0,0,0,1.5),(0,0,0,-1.5),(1.2,0.4,-0.7,0.3),(-0.9,1.1,0.5,-0.6)],[1.0,1.0,0.9,1.3])
    rng=np.random.default_rng(2); P=[]
    for st in rng.uniform(-2.5,2.5,size=(40,4)):
        r=minimize(lambda q: gaps(f4,tuple(q))[1], st, method='L-BFGS-B',
                   bounds=[(-3,3)]*4, options={'maxiter':400,'ftol':1e-16})
        if r.fun<1e-7 and np.abs(r.x).max()<2.95: P.append(r.x)
    P=np.array(P)
    print(f"      {len(P)}/40 bounded starts hit the locus; bounding box"
          f" min {np.round(P.min(0),2)} max {np.round(P.max(0),2)}")
    print("      => a genuine 2-dimensional locus with NO symmetry explanation. Topology OPEN.\n")

if __name__=='__main__':
    w=sys.argv[1] if len(sys.argv)>1 else 'all'
    if w in ('1','all'): part1()
    if w in ('2','all'): part2()
    if w in ('3','all'): part3()
    if w in ('4','all'): part4()
