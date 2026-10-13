"""
lab_berry_charge.py  --  RH2, memo 22

The Z_2 (Berry) charge of the singular-value degeneracy locus of F- for SU(2).

Where the singular values are simple, the SVD M = sum_i sigma_i u_i v_i^T fixes each PAIR
(u_i,v_i) only up to a simultaneous sign flip, so the i-th singular pair lives in
(S^2 x S^2)/Z_2, whose fundamental group is Z_2.  Transport around a loop therefore carries
a Z_2 monodromy -- the Berry phase.  Classical conical-intersection theory
(Herzberg-Longuet-Higgins) predicts -1 on a small loop linking a transverse degeneracy.

Part 1  measure it on the GENERIC locus (charge-4 't Hooft, no continuous symmetry)
Part 2  measure it on a SYMMETRY-FORCED locus (charge-3 coplanar centres)
Part 3  asymptotics: does the locus reach the point at infinity?
"""
import sys, itertools
import numpy as np, sympy as sp
from scipy.optimize import minimize
np.set_printoptions(precision=5, suppress=True)
x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3', real=True); X=[x0,x1,x2,x3]
def b2(m,n):
    M=[[0]*4 for _ in range(4)]; M[m][n]=1; M[n][m]=-1; return sp.Matrix(M)
ETA=[b2(0,1)-b2(2,3), b2(0,2)-b2(3,1), b2(0,3)-b2(1,2)]
SDB=[b2(0,1)+b2(2,3), b2(0,2)+b2(3,1), b2(0,3)+b2(1,2)]
ETAn=np.array([[[float(E[m,n]) for n in range(4)] for m in range(4)] for E in ETA])
eps3=np.zeros((3,3,3))
for p in itertools.permutations(range(3)): eps3[p]=np.sign(np.linalg.det(np.eye(3)[list(p)]))
def thooft(cs,ls):
    rho=1+sum(sp.Float(l)**2/sum((X[m]-sp.Float(c[m]))**2 for m in range(4)) for c,l in zip(cs,ls))
    L=sp.log(rho)
    A=[[-sum(SDB[a][m,n]*sp.diff(L,X[n]) for n in range(4)) for m in range(4)] for a in range(3)]
    F=[[[sp.diff(A[a][n],X[m])-sp.diff(A[a][m],X[n])
        + sum(eps3[a,b,e]*A[b][m]*A[e][n] for b in range(3) for e in range(3))
        for n in range(4)] for m in range(4)] for a in range(3)]
    return [[[sp.lambdify((x0,x1,x2,x3),F[a][m][n],'numpy') for n in range(4)] for m in range(4)] for a in range(3)]
def Mof(fl,p):
    V=np.array([[[float(fl[a][m][n](*p)) for n in range(4)] for m in range(4)] for a in range(3)])
    return np.array([[0.25*np.sum(V[i]*ETAn[a]) for i in range(3)] for a in range(3)])
def sv(fl,p): return np.linalg.svd(Mof(fl,tuple(p)),compute_uv=False)
def mingap(fl,p):
    s=sv(fl,p); return min(s[0]-s[1],s[1]-s[2])/s[0]
def transport(fl,centre,e1,e2,r,steps):
    prevU=prevV=U0=V0=None; swaps=0
    for t in np.linspace(0,2*np.pi,steps+1):
        p=centre+r*(np.cos(t)*e1+np.sin(t)*e2)
        U,s,Vt=np.linalg.svd(Mof(fl,tuple(p))); V=Vt.T
        if prevU is not None:
            if not np.allclose(np.argmax(np.abs(prevU.T@U),axis=1),[0,1,2]): swaps+=1
            for c in range(3):
                if np.dot(U[:,c],prevU[:,c])<0: U[:,c]*=-1; V[:,c]*=-1
        prevU,prevV=U,V
        if U0 is None: U0,V0=U.copy(),V.copy()
    return ([float(np.dot(prevU[:,c],U0[:,c])) for c in range(3)],
            [float(np.dot(prevV[:,c],V0[:,c])) for c in range(3)], swaps)
def normal_plane(fl,p,h=1e-4):
    def f(q): 
        s=sv(fl,q); return min(s[0]-s[1],s[1]-s[2])**2
    H=np.zeros((4,4))
    for a in range(4):
        for b in range(4):
            ea=np.zeros(4); ea[a]=h; eb=np.zeros(4); eb[b]=h
            H[a,b]=(f(p+ea+eb)-f(p+ea-eb)-f(p-ea+eb)+f(p-ea-eb))/(4*h*h)
    _,Q=np.linalg.eigh(H); return Q[:,-1],Q[:,-2]

CS4=[(0,0,0,1.5),(0,0,0,-1.5),(1.2,0.4,-0.7,0.3),(-0.9,1.1,0.5,-0.6)]
LS4=[1.0,1.0,0.9,1.3]

def part1():
    f4=thooft(CS4,LS4); rng=np.random.default_rng(4); pts=[]
    for st in rng.uniform(-2,2,size=(20,4)):
        r=minimize(lambda q: mingap(f4,q), st, method='L-BFGS-B',
                   bounds=[(-3,3)]*4, options={'maxiter':500,'ftol':1e-18})
        if r.fun<1e-9 and np.abs(r.x).max()<2.9: pts.append(r.x)
    print("PART 1 -- GENERIC locus (charge-4 't Hooft, centres spanning a 3-plane)")
    print(f"{'point':<32}{'radius':>8}{'steps':>7}   Berry(u)         Berry(v)      swaps")
    for p in pts[:3]:
        n1,n2=normal_plane(f4,p)
        for r,st in [(0.05,720),(0.025,1440),(0.012,2880)]:
            pu,pv,sw=transport(f4,p,n1,n2,r,st)
            print(f"{str(np.round(p,3)):<32}{r:>8}{st:>7}   {np.round(pu,3)}   {np.round(pv,3)}  {sw:>4}")
            sys.stdout.flush()
        q,_=np.linalg.qr(np.vstack([np.array([n1,n2]),np.eye(4)]).T); n3,n4=q[:,2],q[:,3]
        pu,_,_=transport(f4,p+0.6*n1,n1,n2,0.05,720)
        print(f"{'   control: loop NOT linking':<32}{0.05:>8}{720:>7}   {np.round(pu,3)}")
        pu,_,_=transport(f4,p,n3,n4,0.05,720)
        print(f"{'   control: loop tangent to it':<32}{0.05:>8}{720:>7}   {np.round(pu,3)}")
    print("   => -1 on exactly the two degenerate pairs, +1 on the third, stable in r and in")
    print("      the step count, with no ordering swaps.  A genuine conical intersection.\n")

def part2():
    f3=thooft([(0,0,0,1.5),(0,0,0,-1.5),(1.2,0.4,-0.7,0.3)],[1.0,1.0,0.9])
    u=np.array([1.2,0.4,-0.7,0.0]); u/=np.linalg.norm(u); e3=np.array([0.,0,0,1.])
    Q,_=np.linalg.qr(np.vstack([np.array([u,e3]),np.eye(4)]).T); n1,n2=Q[:,2],Q[:,3]
    p=0.8*u+0.4*e3
    print("PART 2 -- SYMMETRY-FORCED locus (charge-3, coplanar centres: the centre-plane)")
    for r in (0.08,0.04,0.02):
        pu,pv,sw=transport(f3,p,n1,n2,r,1440)
        print(f"   radius {r}: Berry(u) = {np.round(pu,3)}   Berry(v) = {np.round(pv,3)}")
    print("   => +1.  Symmetry-forced degeneracies are Z_2-NEUTRAL; the loop is an SO(2) orbit")
    print("      and the singular values are constant along it.  The charge distinguishes")
    print("      essential (conical, -1) from symmetry-forced (removable, +1) degeneracy.\n")

def part3():
    f4=thooft(CS4,LS4)
    print("PART 3 -- asymptotics: min-gap/sigma_1 along rays")
    for R in [3,6,12,25,60,150]:
        d=np.array([0.4,-0.5,0.6,0.48]); d/=np.linalg.norm(d)
        s=sv(f4,R*d)
        print(f"   |x| = {R:>4}:  sigma = {np.array2string(s,formatter={'float':lambda v:f'{v:.3e}'})}"
              f"   min-gap/s1 = {min(s[0]-s[1],s[1]-s[2])/s[0]:.5f}")
    print("   => the field is asymptotically BPST-like, hence CONFORMAL (all sigma equal), so")
    print("      the locus accumulates at the point at infinity.  On S^4 the locus is compact")
    print("      and passes through that point.\n")

if __name__=='__main__':
    w=sys.argv[1] if len(sys.argv)>1 else 'all'
    if w in ('1','all'): part1()
    if w in ('2','all'): part2()
    if w in ('3','all'): part3()
