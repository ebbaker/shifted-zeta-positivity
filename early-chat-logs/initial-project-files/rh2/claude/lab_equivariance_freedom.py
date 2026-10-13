"""
lab_equivariance_freedom.py -- how much freedom is there in "an equivariant
member of C attached to Xi"?

Proposition 1 (brief §1.3) is a statement about THEOREMS of the quantified form
"P(f) => f has an equivariant extension in C".  A reader may object: to prove RH
we need only ONE function, so why does a quantified statement matter?  The
objection is correct, and answering it properly requires knowing how much
freedom the phrase "Xi admits an equivariant member of C" actually has.

Three checks.

  (1) EQUIVARIANCE <=> AXIAL FORM.  F(u q ubar) = u F(q) ubar for all unit
      quaternions u  iff  F(q) = A(x_0, r) + omega B(x_0, r) with A, B real and
      omega = Im q / r.

  (2) AXIAL + SLICE DATA => UNIQUE.  An equivariant F is determined on all of H
      by its restriction to a SINGLE slice.  So "F is equivariant and restricts
      to f on a slice" has NO freedom at all: F = R f, the rotational extension.

  (3) AXIAL + REAL-AXIS DATA ONLY => MASSIVELY NON-UNIQUE.  If one prescribes F
      only on the real axis, uniqueness fails (this is the appendix's
      Proposition A.5).  So the freedom, when there is any, comes from weakening
      "restricts to f" -- which is exactly what brief §7.1's "transform, not
      matching" proposes.

  (4) And the structural fact: for an equivariant F, the off-axis zero set is
      {A = B = 0} x S^2 -- so "no sphere in the zero set" and "no off-axis zero"
      are THE SAME CONDITION, hence for F = R f it is verbatim hyperbolicity of f.
"""
import numpy as np

def qm(p, q):
    a1,b1,c1,d1 = p; a2,b2,c2,d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
def qc(p): return np.array([p[0],-p[1],-p[2],-p[3]])
def conj_by(u, q): return qm(qm(u, q), qc(u))     # u q ubar, |u| = 1

LINE = "="*78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)

def axial(A, B):
    """build F(q) = A(x0,r) + omega B(x0,r) from real functions A, B."""
    def F(q):
        x0 = q[0]; v = q[1:]; r = np.linalg.norm(v)
        if r < 1e-14:
            return np.array([A(x0, 0.0), 0.0, 0.0, 0.0])
        w = v / r
        b = B(x0, r)
        return np.array([A(x0, r), b*w[0], b*w[1], b*w[2]])
    return F

rng = np.random.default_rng(0)
def rand_unit_q():
    u = rng.normal(size=4); return u/np.linalg.norm(u)

head("CHECK 1  equivariance <=> axial form")
# an axial F, from the stem of z^3 - 2z  (A + iB = G(x0 + i r))
def stem(z): return z**3 - 2*z
A1 = lambda x0, r: stem(complex(x0, r)).real
B1 = lambda x0, r: stem(complex(x0, r)).imag
F1 = axial(A1, B1)
worst = 0.0
for _ in range(400):
    q = rng.normal(size=4); u = rand_unit_q()
    worst = max(worst, np.abs(F1(conj_by(u,q)) - conj_by(u, F1(q))).max())
print(f"  axial F (stem z^3-2z):  max |F(u q ubar) - u F(q) ubar| = {worst:.2e}   -> EQUIVARIANT")

# a NON-axial F: add a term depending on the direction of Im q, not just |Im q|
def F2(q):
    out = F1(q).copy()
    out[1] += 0.3 * q[2]          # breaks the axial form
    return out
worst2 = 0.0
for _ in range(400):
    q = rng.normal(size=4); u = rand_unit_q()
    worst2 = max(worst2, np.abs(F2(conj_by(u,q)) - conj_by(u, F2(q))).max())
print(f"  non-axial F:            max |F(u q ubar) - u F(q) ubar| = {worst2:.2e}   -> NOT equivariant")

head("CHECK 2  axial + one slice  =>  determined on all of H (no freedom)")
print("  Take two equivariant F, G agreeing on the single slice C_I with I = j.")
print("  Reconstruct both at random points off that slice and compare.")
# G built from the SAME slice data must reproduce A, B, hence F, everywhere
I = np.array([0.,0,1,0])                            # the imaginary unit j
def restrict_to_slice(F, x0, y):
    q = np.array([x0, 0.0, y, 0.0])                 # x0 + y*j
    return F(q)
# read A,B off the slice, rebuild, compare off-slice
def rebuild_from_slice(F):
    def Ahat(x0, r): return restrict_to_slice(F, x0, r)[0]
    def Bhat(x0, r): return restrict_to_slice(F, x0, r)[2]
    return axial(Ahat, Bhat)
G1 = rebuild_from_slice(F1)
worst3 = 0.0
for _ in range(500):
    q = rng.normal(size=4)
    worst3 = max(worst3, np.abs(F1(q) - G1(q)).max())
print(f"  max |F(q) - (rebuilt from slice)(q)| over 500 random q = {worst3:.2e}")
print("  => an equivariant F is RECOVERED from its restriction to one slice.")
print("     So 'equivariant, and restricts to f on a slice' determines F uniquely:")
print("     F = R f, the rotational extension.  There is nothing to search over.")

head("CHECK 3  axial + real axis only  =>  NOT determined")
print("  Two equivariant functions agreeing on all of R but differing off it:")
A0 = lambda x0, r: stem(complex(x0, r)).real
for c in (0.0, 1.0, -2.5):
    Bc = lambda x0, r, c=c: stem(complex(x0, r)).imag + c*r      # r = 0 on the axis
    Fc = axial(A0, Bc)
    on_axis = max(np.abs(Fc(np.array([x,0.,0.,0.])) - F1(np.array([x,0.,0.,0.]))).max()
                  for x in np.linspace(-3, 3, 200))
    off = np.abs(Fc(np.array([0.4, 0.3, -0.5, 0.2])) - F1(np.array([0.4, 0.3, -0.5, 0.2]))).max()
    print(f"    c = {c:>5}:  max difference ON the real axis = {on_axis:.2e};"
          f"   at one off-axis point = {off:.4f}")
print("  => prescribing F on R alone leaves an infinite-dimensional family")
print("     (appendix Prop. A.5).  Freedom exists ONLY if one weakens")
print("     'restricts to f on a slice'.  That is brief §7.1's proposal.")

head("CHECK 4  for an equivariant F, sphere-free == no off-axis zero == hyperbolic")
print("  F = A + omega B with A, B real, and 1, omega are R-independent, so")
print("  F(q) = 0  <=>  A = 0 AND B = 0 -- a condition on (x_0, r) ONLY.")
print("  Hence the off-axis zero set is {A = B = 0} x S^2: every off-axis zero")
print("  carries its entire sphere.  Demonstrated on the rotational extension of")
print("  a polynomial with one conjugate pair:")
def stem2(z): return (z**2 + 1) * (z - 1)          # zeros: +-i and 1
A2 = lambda x0, r: stem2(complex(x0, r)).real
B2 = lambda x0, r: stem2(complex(x0, r)).imag
F3 = axial(A2, B2)
print(f"  {'point q':<34}{'|F(q)|':>12}")
for lab, q in [("1              (real zero)", np.array([1.,0,0,0])),
               ("0 + 1*i        (on the sphere)", np.array([0.,1,0,0])),
               ("0 + 1*j        (same sphere)", np.array([0.,0,1,0])),
               ("0 + 1*k        (same sphere)", np.array([0.,0,0,1])),
               ("0 + (i+j+k)/sqrt3  (same sphere)", np.array([0.,1,1,1])/np.sqrt(3)*1.0)]:
    qq = q.copy()
    if lab.startswith("0 + (i+j+k)"): qq = np.array([0.,1,1,1])/np.sqrt(3)
    print(f"  {lab:<34}{np.linalg.norm(F3(qq)):>12.2e}")
print()
print("  The whole 2-sphere |Im q| = 1, x_0 = 0 is in the zero set, because the")
print("  stem has the conjugate pair +-i.  So for an equivariant F:")
print("      F is sphere-free  <=>  the stem has only real zeros.")
print("  The two are the SAME statement.  This -- not Proposition 1 -- is the")
print("  structural fact, and it is what makes the class-membership condition a")
print("  relabelling rather than a tool.")
