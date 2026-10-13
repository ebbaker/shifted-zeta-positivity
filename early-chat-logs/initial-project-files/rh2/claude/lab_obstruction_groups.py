"""
lab_obstruction_groups.py -- a cheap first-pass screen on the OBSTRUCTION route.

Buchdahl (Trans. AMS 288 (1985) 431-469) sets up Griffiths obstruction theory for
extending a bundle across formal neighbourhoods, and Buchdahl/Eastwood establish
the ambitwistor ladder: order 1 unobstructed but non-unique; order 2 unobstructed
and RIGID; order 3 obstructed, with obstruction = the Yang-Mills current.

brief §7.2 asks for a bundle on the incidence quadric Q = P^1_zeta x P^1_w whose
jumping divisor's sigma-type encodes reality of zeros.  Before building anything,
apply the cheapest possible screen: IS THE OBSTRUCTION GROUP EVEN NONZERO?

Model used here (NAIVE, see caveat).  Q is a smooth quadric surface, i.e. a degree-2
hypersurface in CP^3, so its normal bundle is N = O_{P^3}(2)|_Q = O(2,2) and the
conormal is O(-2,-2).  Modelling the order-n obstruction group as
    H^1( Q, End(E) tensor (N^*)^{n+1} ) = H^1( Q, End(E) tensor O(-2m,-2m) ),  m = n+1,
and computing by Kunneth:
    h^1(P^1 x P^1, O(a,b)) = h^0(O(a)) h^1(O(b)) + h^1(O(a)) h^0(O(b)),
    h^0(P^1, O(k)) = max(k+1, 0),   h^1(P^1, O(k)) = max(-k-1, 0).

CAVEAT, stated up front: Buchdahl's actual obstruction lives in
H^1(X, R^2_{X^(n)}(End E)) for a sheaf R^2 built from the jet filtration, which is
NOT simply End E tensor a power of the conormal bundle.  The computation below is
therefore a first-pass numerology, good for spotting a VANISHING (which would kill
the route cheaply) and not good for claiming a nonvanishing.  Treat a nonzero entry
as "not excluded", never as "an obstruction exists".
"""
def h0(k): return max(k + 1, 0)
def h1(k): return max(-k - 1, 0)
def h1_Q(a, b): return h0(a) * h1(b) + h1(a) * h0(b)

LINE = "=" * 78
print(LINE); print("h^1(Q, O(a,b)) on Q = P^1 x P^1  (nonzero only for mixed signs)"); print(LINE)
print("      b:  " + "".join(f"{b:>6}" for b in range(-8, 3)))
for a in range(-8, 9):
    print(f"  a={a:>3}   " + "".join(f"{h1_Q(a,b):>6}" for b in range(-8, 3)))
print()
print("  => h^1(Q,O(a,b)) != 0 iff (a >= 0 and b <= -2) or (a <= -2 and b >= 0):")
print("     the two rulings must enter with OPPOSITE signs.  A symmetric twist")
print("     O(-c,-c) has h^1 = 0 for every c, so a bundle whose End is built from")
print("     symmetric line bundles has NO obstruction at any order.")

print()
print(LINE)
print("the model bundle from twistor_lift: E = O + O(-d,0),  End E > O(d,0) + O(-d,0)")
print(LINE)
print("""  twistor_lift §3: the zero divisor of the product-type lift F x id is
  Z(F) x P^1_w = sum over zeros of {zeta = zeta_i}, i.e. the pullback of a degree-d
  divisor from P^1_zeta.  So O(Z) = O(d,0) -- ASYMMETRIC between the rulings, which
  is exactly the sign pattern the table above requires.  Orders m = n+1:""")
print()
print("  Convention: the obstruction to extending from Q^(m-1) to Q^(m) involves the")
print("  m-th power of the conormal bundle.  Row m is therefore the obstruction to")
print("  REACHING the m-th formal neighbourhood Q^(m).")
print()
print(f"  {'reach Q^(m)':>12}   h^1(Q, O(d-2m, -2m))  for d =")
print("                 " + "".join(f"{d:>6}" for d in range(0, 15, 2)))
for m in (1, 2, 3, 4, 5):
    row = "".join(f"{h1_Q(d - 2*m, -2*m):>6}" for d in range(0, 15, 2))
    print(f"  {('m = %d' % m):>12}   {row}")
print()
print("  nonzero iff d >= 2m.  So:")
for m in (1, 2, 3, 4):
    print(f"    reaching Q^({m}): needs deg >= {2*m}"
          + ("      <-- the Yang-Mills slot in the ambitwistor ladder" if m == 3 else ""))
print()
print("  READING.  The obstruction group is nonzero exactly when the divisor degree")
print("  is large enough relative to the order -- and the THIRD-order slot, the one")
print("  that carries the field equation in the ambitwistor correspondence, first")
print("  opens at degree 6.  So the Jensen truncations J^{d,n} of Xi with d >= 6 are")
print("  the smallest ones for which a third-order obstruction is not excluded on")
print("  dimension grounds alone.  Below d = 6 the route is dead for free.")
print()
print("  What this does NOT say: that any such obstruction is nonzero, or that it")
print("  encodes reality of zeros.  See the caveat in the docstring.")
