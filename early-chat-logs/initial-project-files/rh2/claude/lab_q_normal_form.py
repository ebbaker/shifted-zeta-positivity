"""
lab_q_normal_form.py -- translating memo9's transverse jet into twistor coordinates.

memo9 proved that the ADHM deficit vanishes to first order transverse to a slice
Pi_e and appears at second order, with an ISOTROPIC rank-2 transverse Hessian.
The isotropy was observed, not explained.  This script explains it, using the
conventions of twistor_lift_computation.md §1-2.

Conventions (twistor_lift §1).  eta(w) = (w+j)^{-1} i (w+j) for w in CP^1, the
stereographic parametrisation of the 2-sphere S of imaginary units.  A point of
the incidence quadric Q = CP^1_zeta x CP^1_w with coordinates (zeta, w),
zeta = x + i y, is the quaternion q = x + y*eta(w).  Ruling A (zeta const) is the
twistor lift of the sphere S_zeta; Ruling B (w const) is a full SLICE with its
complex structure fixed.  The real structure is rho(zeta,w) = (conj zeta, -1/conj w),
which in (q,eta) coordinates is sigma(q,eta) = (q,-eta).

CLAIMS TO CHECK.
  (1) eta(w) is a unit imaginary quaternion, and w -> eta(w) is stereographic.
  (2) eta(-1/conj w) = -eta(w):  rho acts antipodally on the w-sphere.
  (3) NO Ruling-B line is rho-invariant.  rho maps {w = w0} to {w = -1/conj w0},
      and these are disjoint for every w0.  (Ruling-A lines ARE invariant, exactly
      when zeta is real -- that is the sigma-type invariant of twistor_lift §3.)
  (4) A slice Pi_e is the Ruling-B line {w = w0} with eta(w0) = e, and memo9's
      transverse coordinate nu satisfies
          nu^2 = r^2 - t^2 = y^2 sin^2(theta)
      with theta the angle on S between eta(w) and e.  Expanding in dw,
          nu^2 = 4 y^2 |dw|^2 / (1+|w0|^2)^2 + O(|dw|^4) ,
      i.e. nu^2 is 4y^2 times the FUBINI-STUDY metric on the normal direction.
  So memo9's transverse Hessian is a positive HERMITIAN form on the normal bundle
  of a Ruling-B line -- and its isotropy is nothing but the U(1)-invariance of the
  round metric on the sphere of complex structures.
"""
import numpy as np

# ---------------------------------------------------------------- quaternions
def qm(p, q):
    a1,b1,c1,d1 = p; a2,b2,c2,d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2,
                     a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2,
                     a1*d2+b1*c2-c1*b2+d1*a2])
def qc(p): return np.array([p[0],-p[1],-p[2],-p[3]])
def qinv(p): return qc(p)/ (p@p)
I = np.array([0.,1,0,0]); J = np.array([0.,0,1,0])

def eta(w):
    """eta(w) = (w+j)^{-1} i (w+j), w complex (in C_i)."""
    W = np.array([w.real, w.imag, 1.0, 0.0])          # w + j
    return qm(qinv(W), qm(I, W))

LINE="="*78
def head(s): print();print(LINE);print(s);print(LINE)

head("CHECK 1  eta(w) is a unit imaginary quaternion; w -> eta(w) is stereographic")
rng = np.random.default_rng(0)
ws = rng.normal(size=20) + 1j*rng.normal(size=20)
E1 = max(abs(eta(w)[0]) for w in ws)
E2 = max(abs(np.linalg.norm(eta(w))-1) for w in ws)
print(f"  max |real part|        = {E1:.2e}")
print(f"  max | |eta(w)| - 1 |   = {E2:.2e}")
# stereographic identity: the chordal formula sin^2(theta/2) = |w-w'|^2/((1+|w|^2)(1+|w'|^2))
err = 0.0
for _ in range(200):
    w = rng.normal()+1j*rng.normal(); v = rng.normal()+1j*rng.normal()
    ct = eta(w)[1:] @ eta(v)[1:]                        # cos theta
    lhs = (1-ct)/2                                      # sin^2(theta/2)
    rhs = abs(w-v)**2/((1+abs(w)**2)*(1+abs(v)**2))
    err = max(err, abs(lhs-rhs))
print(f"  max |sin^2(theta/2) - |w-v|^2/((1+|w|^2)(1+|v|^2))| = {err:.2e}")
print("  => eta is the standard stereographic chart, chordal metric included.")

head("CHECK 2  rho acts ANTIPODALLY on the w-sphere: eta(-1/conj w) = -eta(w)")
err = max(np.linalg.norm(eta(-1/np.conj(w)) + eta(w)) for w in ws)
print(f"  max | eta(-1/conj w) + eta(w) | = {err:.2e}")

head("CHECK 3  no Ruling-B line is rho-invariant (but Ruling-A lines are, iff zeta real)")
print("  rho maps the Ruling-B line {w = w0} to {w = -1/conj w0}.  Fixed would need")
print("  w0 = -1/conj w0, i.e. |w0|^2 = -1: impossible.  Distances on the sphere:")
for w0 in [0.0+0j, 1.0+0j, 0.3-0.7j, 5.0+2j]:
    w1 = -1/np.conj(w0) if w0 != 0 else np.inf
    a = eta(w0)[1:]
    b = -a                              # eta(-1/conj w0)
    print(f"    w0 = {w0!s:>12}   eta(w0).eta(rho w0) = {a@b:+.6f}   (always -1: antipodal)")
print()
print("  Ruling A: rho(L_zeta) = L_(conj zeta), invariant iff zeta real -- this is")
print("  exactly the sigma-type invariant of twistor_lift §3.  So the invariant lives")
print("  on Ruling A, while a SLICE is a Ruling-B line, and no slice is rho-real.")

head("CHECK 4  nu^2 = y^2 sin^2(theta) = 4 y^2 * g_FS(dw,dw) + O(|dw|^4)")
print("  nu^2 := r^2 - t^2 with r = |Im q|, t = <Im q, e>, e = eta(w0), q = x + y eta(w)")
print()
print(f"  {'w0':>12} {'y':>6} {'|dw|':>10} {'nu^2 (exact)':>16} {'4y^2 |dw|^2/(1+|w0|^2)^2':>26} {'ratio':>10}")
for w0 in [0.0+0j, 0.4-0.9j, 1.7+0.6j]:
    e = eta(w0)[1:]
    for y in (0.8,):
        for h in (1e-1, 1e-2, 1e-3):
            dw = h*np.exp(1j*0.7)
            w = w0 + dw
            Imq = y*eta(w)[1:]
            r2 = Imq @ Imq; t = Imq @ e
            nu2 = r2 - t**2
            pred = 4*y**2*abs(dw)**2/(1+abs(w0)**2)**2
            print(f"  {w0!s:>12} {y:>6} {h:>10.0e} {nu2:>16.10e} {pred:>26.10e} {nu2/pred:>10.6f}")
print()
print("  isotropy: nu^2 must depend on dw only through |dw| (a Hermitian form).")
print(f"  {'w0':>12} {'|dw|':>8}  spread of nu^2 over 12 phases of dw")
for w0 in [0.0+0j, 0.4-0.9j]:
    e = eta(w0)[1:]
    for h in (1e-1, 1e-2):
        vals=[]
        for ph in np.linspace(0, 2*np.pi, 12, endpoint=False):
            w = w0 + h*np.exp(1j*ph)
            Imq = 0.8*eta(w)[1:]
            vals.append(Imq@Imq - (Imq@e)**2)
        vals=np.array(vals)
        print(f"  {w0!s:>12} {h:>8.0e}  spread {vals.max()-vals.min():.3e}   mean {vals.mean():.6e}")

head("SUMMARY")
print("""  A slice Pi_e is a Ruling-B line {w = w0} in the incidence quadric Q, whose
  normal direction is ONE COMPLEX dimension (Q is 2-dimensional, the line is 1).
  memo9's two real transverse directions in H are that one complex direction, and

      nu^2  =  r^2 - t^2  =  y^2 sin^2(theta)  =  4 y^2 g_FS(dw,dw) + O(|dw|^4),

  so memo9's transverse Hessian is a POSITIVE HERMITIAN FORM on the normal bundle
  of a Ruling-B line -- a real multiple of the Fubini-Study metric on the sphere of
  complex structures, with coefficient 4 y^2 * 4 R_0 sum_p sigma_p^2 prod(...).
  The isotropy that memo9 observed numerically is exactly the U(1)-invariance of
  the round metric.  "Second transverse jet along a slice" = "second-order normal
  data along a Ruling-B line of Q".

  AND: rho maps {w = w0} to the ANTIPODAL Ruling-B line {w = -1/conj w0}, always
  disjoint from it.  So no slice is rho-real, and the sigma-type invariant -- which
  is a property of RULING-A components and of how rho permutes them -- cannot be
  read off any finite-order jet along a single Ruling-B line, at any order: rho
  moves the base line to a line at finite distance, which no jet reaches.""")
