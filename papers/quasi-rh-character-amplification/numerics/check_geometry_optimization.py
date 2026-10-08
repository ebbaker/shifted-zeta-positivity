"""Exact geometry checks; external analytic lemmas are assumptions.

Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Serving variant and configured reasoning effort are not exposed.
Uses only Python's standard library; emits a small JSON record.
"""
from fractions import Fraction as F
import json

# Sparse exact polynomials in (delta,y).
def const(c):
    return {(0, 0): F(c)} if c else {}

def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}

def scale(c, p):
    return {k: c*v for k, v in p.items() if c*v}

def mul(*ps):
    out = const(1)
    for p in ps:
        new = {}
        for (i,j),v in out.items():
            for (k,l),w in p.items():
                new[i+k,j+l] = new.get((i+k,j+l), F(0)) + v*w
        out = {k:v for k,v in new.items() if v}
    return out

def conv(a,b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):
            out[i+j] += v*w
    return out

def at(coeffs, y):
    return sum(c*y**i for i,c in enumerate(coeffs))

def entry(q):
    return {"exact":str(q), "decimal":float(q)}

e = F(1,6000)
ell, b = F(1,6)+e, F(1,8)
lx, ly = (1-ell-b)/2, (1-ell+b)/2
h = 1-lx+ell
M = lx+ly
sigma = F(11,12)-ell/4
low = lx/2+b/12
signal_constant = lx/2-1+h/6
assert h == (1+3*ell+b)/2
assert M+ell == 1 and ly-lx == b
assert sigma+signal_constant == low
assert sigma == F(20999,24000)
assert signal_constant == -F(11,16)
assert low == F(4499,24000)
# Full rescaled low loss, including its d=ell endpoint.
assert ell < F(1,5)
loss = lambda d: -d+max(F(0),5*ell-1+d)/8
kink = 1-5*ell
low_points = [F(0),ell] + ([kink] if 0 <= kink <= ell else [])
assert max(map(loss,low_points)) == 0
assert lx-ell > 0 and ly-ell > 0
assert ly-ell-F(11,6)*b > 0
assert b < F(3,8)*(1-3*ell)

# Source endpoint rational function with kappa fixed at 3/4.
d, y = {(1,0):F(1)}, {(0,1):F(1)}
alpha_minus_d = add(const(F(5,6)),scale(-1,d))
py = add(const(7),scale(18,y),scale(8,mul(y,y)))
jy = add(const(185),scale(170,y),
         mul(d,add(const(-138),scale(12,y),scale(96,mul(y,y)))))
Q = add(const(370),scale(340,y),
        mul(d,add(const(-1896),scale(-3016,y),scale(-208,mul(y,y)))),
        mul(d,d,add(const(2448),scale(6288,y),scale(4512,mul(y,y)),scale(1536,mul(y,y,y)))))
perturbation = add(scale(120,jy),scale(-96,mul(d,y,jy)),
                   scale(864,mul(alpha_minus_d,d,py)))
N = add(Q,scale(-e,perturbation))
# Reconstruct directly from E=F+(h/2)T and T=12*(alpha-d)*d*py/jy.
Fpart = add(const(-F(1,4)+5*ell/4+b/6),
            scale(-1,mul(d,add(const(b/2),scale(ell,y)))))
N_direct = add(scale(-96,mul(jy,Fpart)),
               scale(-576*h,mul(alpha_minus_d,d,py)))
assert N == N_direct
A = [N.get((2,i),F(0)) for i in range(4)]
B = [N.get((1,i),F(0)) for i in range(3)]
C = [N.get((0,i),F(0)) for i in range(2)]
assert A == [F(306126,125),F(786048,125),F(564168,125),F(192192,125)]
assert B == [-F(47352,25),-F(75386,25),-F(5204,25)]
assert C == [F(3663,10),F(1683,5)]
D = [4*a-bb for a,bb in zip(conv(A,C),conv(B,B))]
assert D == [F(467172,625),F(680072136,625),F(3248881292,625),F(884272016,125),F(1266754928,625)]
assert all(c > 0 for c in A+D)
# Coefficientwise D(y) >= (D(0)/A(0))*A(y) on every y>=0.
dominance = [D[i]*A[0]-D[0]*A[i] for i in range(len(A))]
assert all(c >= 0 for c in dominance) and D[-1] > 0
N_lower = D[0]/(4*A[0])
# J=(alpha-delta)D_x+delta*P_x <= alpha*3=5/2 for
# 0<=delta<=alpha, since 0<P_x<=D_x<=3 on 0<=x<=1/2.
adaptive = N_lower/F(25920)
assert N_lower == F(12977,170070)
assert adaptive == F(12977,4408214400) > F(1,400000)

floor = F(7,1200)-F(32,25)*e
middle = F(241,9600)-F(329,400)*e
small = F(63,800)-F(51,100)*e
assert min(floor,middle,small) > adaptive
principal_w, principal_z = ly/20, h/600
assert min(principal_w,principal_z) > adaptive
zeta = F(1,6400000)  # one sixteenth of the clean adaptive margin.
assert 2*zeta < F(1,400000)/4
assert ell/(h+zeta) > F(1,5) > F(7,37)
assert sigma > F(87,100)

# The y=0 endpoint constrains further increases of e in this geometry.
# Its discriminant complement is 576*(49-286020e-1162800e^2).
c0=4*2448*370-1896**2
c1=4*(6048*370-2448*22200)+2*1896*11520
c2=-4*6048*22200-11520**2
assert [c0,c1,c2] == [576*49,-576*286020,-576*1162800]
barrier_poly = lambda v: F(49)-286020*v-1162800*v*v
barrier_lo, barrier_hi = F(1711975385,10**13), F(1711975386,10**13)
assert e < barrier_lo < barrier_hi
assert barrier_poly(barrier_lo)>0>barrier_poly(barrier_hi)
# Vertex stays in the live delta range throughout this narrow root interval.
vertex = lambda v: (1896-11520*v)/(2*(2448+6048*v))
assert all(F(1,50)<vertex(v)<F(3,4) for v in [barrier_lo,barrier_hi])

result = {
    "scope":"Exact algebra and exponent feasibility only; external analytic lemmas are assumed.",
    "geometry":{k:entry(v) for k,v in {"e":e,"ell":ell,"b":b,"lx":lx,"ly":ly,"h":h,"sigma":sigma,"low":low,"signal_constant":signal_constant}.items()},
    "variance_delta":entry(2*sigma-1), "variance_exponent":entry(1+2*sigma),
    "certificate":{
        "identity":"10368*J*(-E)=A(y)*delta^2+B(y)*delta+C(y)",
        "A":[str(v) for v in A],"B":[str(v) for v in B],"C":[str(v) for v in C],
        "four_AC_minus_B_squared":[str(v) for v in D],
        "coefficientwise_dominance":"verified exactly",
        "N_lower":entry(N_lower), "adaptive_lower":entry(adaptive),
        "simple_adaptive_margin":entry(F(1,400000)),
    },
    "margins":{k:entry(v) for k,v in {"floor":floor,"middle":middle,"small":small,"principal_w":principal_w,"principal_z":principal_z,"frequency_extension":zeta,"slot_supply_above_one_fifth":ell/(h+zeta)-F(1,5),"gram":ly-ell-F(11,6)*b}.items()},
    "fixed_b_endpoint_barrier":{
        "polynomial":"49-286020*e-1162800*e^2",
        "root_interval":[entry(barrier_lo),entry(barrier_hi)],
        "vertex_interval_endpoint_values":[entry(vertex(v)) for v in [barrier_lo,barrier_hi]],
        "scope":"Obstruction to increasing ell with b=1/8, the same moment envelope, and the same low exponent; not a universal zero-free barrier.",
    },
}
print(json.dumps(result,indent=2,sort_keys=True))
