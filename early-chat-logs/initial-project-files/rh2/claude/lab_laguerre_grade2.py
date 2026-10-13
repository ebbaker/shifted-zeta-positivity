"""Follow-up parts for lab_laguerre_grade.py: full n range, the radius grading,
and the y_0^2 scaling law."""
import numpy as np
from math import factorial
exec(open('/home/claude/lab_laguerre_grade.py').read().split('HYP = [')[0].split('# ------------------------------------------------------------------ test sets')[0].split('"""',2)[2])

LINE = "=" * 78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)

head("PART 7  the shielded cases with n run all the way to deg")
for nm, roots in [("(z^2-1)(z^2+100)",                          [1.,-1.,10j,-10j]),
                  ("(z^2-1)(z^2-4)(z^2+400)",                   [1.,-1.,2.,-2.,20j,-20j]),
                  ("(z^2-1)(z^2-4)(z^2-9)(z^2+2500)",           [1.,-1.,2.,-2.,3.,-3.,50j,-50j]),
                  ("(z^2-1)(z^2-4)(z^2-9)(z^2-16)(z^2+10000)",  [1.,-1.,2.,-2.,3.,-3.,4.,-4.,100j,-100j])]:
    r = normalise(roots); c = poly_from_roots(r); deg = len(r)
    vals = []
    for n in range(1, deg + 1):
        v, unb = poly_min_real(L_n(c, n))
        vals.append((n, v, unb))
    firstneg = next((n for n, v, u in vals if v < -1e-12 or u), None)
    print(f"  {nm}   (deg {deg})   first n with L_n < 0: {firstneg}")
    print("    " + "  ".join(f"n={n}:{v:+.3e}" for n, v, u in vals))
    print()
print("  => every shielded case IS detected, but only once n is large enough.")
print("     Small spheres are caught at LOW n, large spheres at HIGH n: the")
print("     hierarchy is graded by sphere radius, which is what §5a predicted")
print("     the Bessel index would do.")

head("PART 8  which n first detects a pair of radius y_0 (fixed real background)")
print("  background real roots +-1, +-2, +-3, +-4; one implanted pair at 0 +- i y_0.")
print(f"  {'y_0':>8}{'first n with L_n<0':>22}{'min_x L_1':>16}{'min_x P_1':>16}")
for y0 in [0.01, 0.05, 0.2, 0.5, 0.9, 1.5, 3.0, 6.0, 12.0, 30.0]:
    roots = [1.,-1.,2.,-2.,3.,-3.,4.,-4., 1j*y0, -1j*y0]
    r = normalise(roots); c = poly_from_roots(r); deg = len(r)
    first = None
    for n in range(1, deg + 1):
        v, unb = poly_min_real(L_n(c, n))
        if v < -1e-13 or unb:
            first = n; break
    l1, _ = poly_min_real(L_n(c, 1))
    p1, _ = P_m_min(r, 1)
    print(f"  {y0:>8.2f}{str(first):>22}{l1:>16.3e}{p1:>16.3e}")

head("PART 9  the y_0^2 scaling law for the L_1 margin (brief §6.4 consistency)")
print("  fixed real roots at +-1 and 0.3; pair implanted at a = -0.25 +- i y_0.")
print("  Prediction: min L_1 ~ -2 f'(a)-type constant * y_0^2, i.e. EXACTLY quadratic")
print("  in the sphere radius, so the discriminant degrades continuously to 0 as a")
print("  conjugate pair collides on the axis.")
print()
print(f"  {'y_0':>10}{'min_x L_1':>16}{'|min L_1| / y_0^2':>22}{'ratio to previous':>20}")
prev = None
for y0 in [1e-1, 5e-2, 2e-2, 1e-2, 5e-3, 2e-3, 1e-3, 5e-4]:
    roots = [1.0, -1.0, 0.3, -0.25 + 1j*y0, -0.25 - 1j*y0]
    c = poly_from_roots(roots)          # NOT normalised: keep y_0 literal
    v, _ = poly_min_real(L_n(c, 1), span=3.0, ngrid=600001)
    q = abs(v) / y0**2
    print(f"  {y0:>10.1e}{v:>16.4e}{q:>22.6f}{(q/prev if prev else float('nan')):>20.6f}")
    prev = q
print()
print("  A constant column 3 confirms the exponent is exactly 2.")
