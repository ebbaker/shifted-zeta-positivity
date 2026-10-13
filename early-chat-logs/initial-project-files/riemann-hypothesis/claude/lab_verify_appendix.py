"""Symbolic verification of the computations in the extension-uniqueness appendix.

Conventions: q = x0 + x1 i + x2 j + x3 k,  left Cauchy-Fueter operator
D = d/dx0 + i d/dx1 + j d/dx2 + k d/dx3 (applied by LEFT multiplication).
Axial form: F = A(x0, r) + omega * B(x0, r), omega = Im q / r, r = |Im q|.
"""
import sympy as sp

x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3', real=True)

# ---------- quaternion algebra on 4-tuples (1, i, j, k) ----------
def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (
        a1*a2 - b1*b2 - c1*c2 - d1*d2,
        a1*b2 + b1*a2 + c1*d2 - d1*c2,
        a1*c2 - b1*d2 + c1*a2 + d1*b2,
        a1*d2 + b1*c2 - c1*b2 + d1*a2,
    )

E = [(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)]  # 1, i, j, k
COORDS = [x0, x1, x2, x3]

def qadd(p, q):  return tuple(a+b for a, b in zip(p, q))
def qscale(s, p): return tuple(sp.expand(s*a) for a in p)
def qdiff(F, v): return tuple(sp.diff(comp, v) for comp in F)

def CF(F):
    """Left Cauchy-Fueter operator D F = sum_mu e_mu * dF/dx_mu."""
    out = (0, 0, 0, 0)
    for mu in range(4):
        out = qadd(out, qmul(E[mu], qdiff(F, COORDS[mu])))
    return tuple(sp.simplify(c) for c in out)

def lap(F):
    return tuple(sp.simplify(sum(sp.diff(c, v, 2) for v in COORDS)) for c in F)

def qpow(n):
    q = (x0, x1, x2, x3)
    out = (1, 0, 0, 0)
    for _ in range(n):
        out = qmul(out, q)
    return tuple(sp.expand(c) for c in out)

ok = lambda name, cond: print(('PASS' if cond else 'FAIL'), name)

# ---------- 1. axial CRF (Vekua) system ----------
r = sp.sqrt(x1**2 + x2**2 + x3**2)
A = sp.Function('A')(x0, r)
B = sp.Function('B')(x0, r)
F_axial = (A, B*x1/r, B*x2/r, B*x3/r)
DF = CF(F_axial)

Ax = sp.diff(A, x0); Ar = sp.Derivative(sp.Function('A')(x0, sp.Symbol('rr')), sp.Symbol('rr'))
# easier: use substitution variable for r-derivative
rr = sp.Symbol('rr', positive=True)
Af = sp.Function('A')(x0, rr); Bf = sp.Function('B')(x0, rr)
claim_scalar = sp.diff(Af, x0) - sp.diff(Bf, rr) - 2*Bf/rr            # A_x - B_r - 2B/r
claim_vector = sp.diff(Af, rr) + sp.diff(Bf, x0)                      # A_r + B_x

# express DF in terms of rr by substituting r -> rr carefully
def to_rr(expr):
    return sp.simplify(expr.subs(sp.sqrt(x1**2 + x2**2 + x3**2), rr)
                           .subs(x1**2 + x2**2 + x3**2, rr**2))

scalar_part = to_rr(DF[0])
ok("axial system, scalar part  == A_x - B_r - 2B/r",
   sp.simplify(scalar_part - claim_scalar.doit()) == 0)

# vector part should be (A_r + B_x) * x_i / r for i = 1,2,3
for i in (1, 2, 3):
    v = to_rr(sp.simplify(DF[i] / (COORDS[i])))   # divide out x_i
    ok(f"axial system, vector part component {i} == (A_r + B_x)/r * x_{i}",
       sp.simplify(v - claim_vector.doit()/rr) == 0)

# ---------- 2. kernel example (x2 - i x3)^n is Fueter regular, vanishes on C_i ----------
for n in (1, 2, 3, 4):
    # complex number (x2 - i x3)^n placed in the (1, i) slots
    z = sp.expand((x2 - sp.I*x3)**n)
    Fk = (sp.re(z), sp.im(z), 0, 0)
    Fk = tuple(sp.expand(c) for c in Fk)
    ok(f"(x2 - i x3)^{n} Fueter regular", all(sp.simplify(c) == 0 for c in CF(Fk)))
    ok(f"(x2 - i x3)^{n} vanishes on slice C_i",
       all(sp.simplify(c.subs({x2: 0, x3: 0})) == 0 for c in Fk))

# ---------- 3. Fueter images: Delta q^2 = -4, Delta q^3 = -12x - 4 r omega ----------
Dq2 = lap(qpow(2))
ok("Delta q^2 == -4", Dq2 == (-4, 0, 0, 0))
Dq3 = lap(qpow(3))
ok("Delta q^3 == -12 x0 - 4 Im q",
   sp.simplify(Dq3[0] + 12*x0) == 0 and all(sp.simplify(Dq3[i] + 4*COORDS[i]) == 0 for i in (1,2,3)))
# and Delta q^3 is Fueter regular
ok("Delta q^3 Fueter regular", all(sp.simplify(c) == 0 for c in CF(lap(qpow(3)))))

# ---------- 4. Appell relation d/dx0 (Delta q^n) = n Delta q^{n-1},  n = 2..6 ----------
for n in range(2, 7):
    lhs = qdiff(lap(qpow(n)), x0)
    rhs = qscale(n, lap(qpow(n-1)))
    ok(f"d/dx0 Delta q^{n} == {n} Delta q^{n-1}",
       all(sp.simplify(a - b) == 0 for a, b in zip(lhs, rhs)))
    ok(f"Delta q^{n} Fueter regular", all(sp.simplify(c) == 0 for c in CF(lap(qpow(n)))))

# ---------- 5. dimension-1 recursion check for homogeneous axial monogenics ----------
# degree k axial monogenic polynomial: A = sum a_m x^(k-2m) r^(2m), B = sum b_m x^(k-1-2m) r^(2m+1)
# system: A_x = B_r + 2B/r ;  A_r = -B_x.
# Verify: solution space has dim exactly 1 for k = 0..5 by solving the linear system.
for k in range(0, 6):
    a = sp.symbols(f'a0:{k//2+1}')
    b = sp.symbols(f'b0:{max((k-1)//2+1, 1)}') if k >= 1 else ()
    Ak = sum(a[m]*x0**(k-2*m)*rr**(2*m) for m in range(k//2+1))
    Bk = sum(b[m]*x0**(k-1-2*m)*rr**(2*m+1) for m in range((k-1)//2+1)) if k >= 1 else sp.Integer(0)
    eq1 = sp.expand(sp.diff(Ak, x0) - sp.diff(Bk, rr) - 2*Bk/rr)
    eq2 = sp.expand(sp.diff(Ak, rr) + sp.diff(Bk, x0))
    eqs = []
    for e in (sp.expand(eq1*rr), sp.expand(eq2)):   # clear the 1/r
        p = sp.Poly(e, x0, rr)
        eqs.extend(p.coeffs())
    unknowns = list(a) + list(b)
    sol = sp.linsolve(eqs, unknowns)
    # dimension of solution space = number of free parameters
    free = len(unknowns) - sp.Matrix([[sp.diff(e, u) for u in unknowns] for e in eqs]).rank()
    ok(f"homogeneous axial monogenics, degree {k}: dim == 1", free == 1)

# ---------- 6. x-independent entire axial monogenic => constant ----------
# from the system: A_x = 0 forces B_r + 2B/r = 0 => B = c/r^2 (singular) => B=0, A const.
c = sp.Symbol('c')
Bsol = sp.dsolve(sp.Derivative(sp.Function('B')(rr), rr) + 2*sp.Function('B')(rr)/rr, sp.Function('B')(rr))
print("ODE B_r + 2B/r = 0 general solution:", Bsol)

# ---------- 7. incidence computation: bracket vanishes iff eta(G(w)) = eta(w) ----------
# For unit imaginary u, v: bracket coefficients (1 + u v) and (v - u);
# real part of (1+uv) is 1 - <u,v>, zero iff u=v. Spot-check numerically.
import random
random.seed(7)
def rand_unit_im():
    v = [random.gauss(0,1) for _ in range(3)]
    n = sum(t*t for t in v) ** 0.5
    return (0, v[0]/n, v[1]/n, v[2]/n)
fails = 0
for _ in range(200):
    u, v = rand_unit_im(), rand_unit_im()
    one_plus_uv = qadd((1,0,0,0), qmul(u, v))
    v_minus_u = tuple(a-b for a, b in zip(v, u))
    dot = -qmul(u, v)[0]  # <u,v> = -Re(uv)
    # real part of 1+uv equals 1 - <u,v>
    if abs(one_plus_uv[0] - (1 - dot)) > 1e-12: fails += 1
    # v - u purely imaginary
    if abs(v_minus_u[0]) > 1e-12: fails += 1
ok("incidence bracket: Re(1+uv) = 1 - <u,v>, (v-u) imaginary (200 random)", fails == 0)

# ---------- 8. conjugated extension u f(q) u^{-1}: slice-regularity test ----------
# f(q) = q^2 on slice C_J: Phi(q) = u q^2 u^{-1}. Check d/dx + J d/dy annihilates it iff uJ=Ju.
def conj_ext(u, q):  # u q^2 u^conj (u unit)
    ub = (u[0], -u[1], -u[2], -u[3])
    return qmul(qmul(u, qmul(q, q)), ub)
xx, yy = sp.symbols('xx yy', real=True)
for trial in range(3):
    # random unit u, random unit imaginary J
    import math
    vv = [random.gauss(0,1) for _ in range(4)]
    n = math.sqrt(sum(t*t for t in vv)); u = tuple(t/n for t in vv)
    J = rand_unit_im()
    qpt = tuple(sp.expand(xx*E[0][t] + yy*J[t]) for t in range(4))
    Phi = conj_ext(u, qpt)
    dPhi = tuple(sp.diff(c, xx) for c in Phi)
    dPhiy = tuple(sp.diff(c, yy) for c in Phi)
    dbar = qadd(dPhi, qmul(J, dPhiy))
    # evaluate at a random (x,y)
    val = [sp.N(c.subs({xx: 0.37, yy: -1.21})) for c in dbar]
    is_zero = all(abs(t) < 1e-9 for t in val)
    commut = all(abs(t) < 1e-9 for t in
                 (sp.Matrix(qmul(u, J)) - sp.Matrix(qmul(J, u))))
    ok(f"trial {trial}: dbar_J(u q^2 u^-1) == 0  iff  uJ == Ju   ({'commuting' if commut else 'non-commuting'} pair)",
       is_zero == commut)

print("\nAll checks done.")
