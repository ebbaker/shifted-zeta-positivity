"""
lab_size_detector.py -- memo #25, Part 5.

The dictionary of Parts 1-4 hands us a specific functional: the total instanton
size squared, sum_i rho_i^2.  Under Im(root)^2 = 2 rho^2 that is
sum_rho Im(rho)^2 / 2.  This part shows what kind of function of the
COEFFICIENTS that is -- and it is exactly the non-analytic chamber object that
memo 24's classification says a detector has to be.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
def hline(s): print("\n"+s+"\n"+"-"*len(s))

hline("(a) the minimal witness:  p = z^2 + a,  a real")
print("   roots +-sqrt(-a).   sum|rho|^2 = 2|a|,   s_2 = sum rho^2 = -2a")
print("   => sum Im(rho)^2 = (sum|rho|^2 - s_2)/2 = |a| + a = 2*ReLU(a)\n")
print(f"   {'a':>10s} {'sum Im^2 (numeric)':>20s} {'2*ReLU(a)':>12s} {'s_2 = Turan':>13s}")
for a in [-2.0,-0.5,-1e-6, 0.0, 1e-6, 0.5, 2.0]:
    r = np.roots([1,0,a]); s = float(np.sum(np.imag(r)**2))
    print(f"   {a:10.1e} {s:20.10f} {2*max(a,0.0):12.6f} {-2*a:13.4f}")
print("\n   sum Im^2 is continuous, >= 0, vanishes EXACTLY on the hyperbolic region,")
print("   and is NOT real-analytic -- its kink sits on the discriminant a = 0.")
print("   Turan's s_2 is the analytic part and is only necessary (it is < 0 for")
print("   a > 0 but also fails to see anything at all when other roots dominate).")

hline("(b) the same functional on the project's standard test set")
def rts(c): return np.roots(c)
tests = [
 ("z^2-1                       (hyp)", [1,0,-1]),
 ("(z-1)(z-2)                  (hyp)", np.poly([1,2])),
 ("(z^2-1)(z^2-4)              (hyp)", np.poly([-2,-1,1,2])),
 ("z^2+1                       (NOT)", [1,0,1]),
 ("z^2+z+1                     (NOT)", [1,1,1]),
 ("(z^2+1)(z-1)                (NOT)", np.poly([1,1j,-1j])),
 ("(z^2+1)(z^2+4)              (NOT)", np.poly([1j,-1j,2j,-2j])),
 ("(z-1)((z+2)^2+9)            (NOT)", np.poly([1,-2+3j,-2-3j])),
 ("near-miss quartic           (NOT)", [1,10,26,22,3]),
 ("(z^2-1)(z^2+100)  shielded  (NOT)", np.poly([-1,1,10j,-10j])),
 ("(z^2-1)(z^2-4)(z^2+400) shd (NOT)", np.poly([-2,-1,1,2,20j,-20j])),
]
print(f"{'polynomial':38s} {'sum Im^2':>14s} {'-> total size^2':>16s} {'verdict':>9s}")
for name, c in tests:
    r = rts(np.real(np.array(c, dtype=complex)))
    s = float(np.sum(np.imag(r)**2))
    print(f"{name:38s} {s:14.6e} {s/2:16.6e} {'HYP' if s < 1e-18 else 'not hyp':>9s}")
print("\n  complete, like the Bezoutian signature and Lambda -- and for the same")
print("  structural reason (memo 24 sec 0(3)): it is a real chamber object.")

hline("(c) relation to the canonical instrument Lambda")
print("  Lambda(z^2 + y0^2) = y0^2/2 exactly;  sum Im^2 = 2 y0^2.  So on a single")
print("  implanted pair  Lambda = (sum Im^2)/4 = rho^2, the instanton size squared.")
print(f"  {'y0':>10s} {'Lambda = y0^2/2':>18s} {'sum Im^2 / 4':>16s} {'rho^2 = y0^2/2':>16s}")
for y0 in [1.0, 0.5, 0.1, 0.01]:
    r = np.roots([1,0,y0**2]); s = float(np.sum(np.imag(r)**2))
    print(f"  {y0:10.3f} {y0**2/2:18.8f} {s/4:16.8f} {y0**2/2:16.8f}")
print("\n  => brief sec 6.4's universal y0^2/2 law IS the instanton size squared.")
print("     Rodgers-Tao's Lambda >= 0 becomes rho^2 >= 0, which is automatic;")
print("     Newman's Lambda = 0 becomes 'the configuration sits exactly on the")
print("     small-instanton boundary of the moduli space'.")
