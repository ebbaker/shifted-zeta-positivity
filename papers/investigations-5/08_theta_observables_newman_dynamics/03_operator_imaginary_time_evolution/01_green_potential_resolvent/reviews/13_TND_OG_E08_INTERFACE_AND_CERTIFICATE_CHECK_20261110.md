# E08 r1 interface assessment and certificate checks

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, exact-turn **gpt-6.1-sol / ultra**.
Internal proof/code-author assessment of E08, with inherited E03 and
E07 premises. B05 r2's exact model is unavailable, so cross-model
independence is unverified.

**Stage A accepted without mathematical correction. Stage B passed
all four fixed cases.** All 27 files in [Inputs26][inputs] match.
The separate [directed record][record] carries the four results and
the [research note][note] states the acquired scope.

## Stage A rederivations

1. **Note14 (3), complete census and reciprocal floor.** On each
   boundary the error radius is strictly below the lower polynomial
   modulus. Rouché transfers multiplicity counts. Disjoint contained
   subdisks whose counts sum to the outer count exhaust the roots.
   With the resulting true knots, each boundary factor lies between
   \(A-s\) and \(A+s\). After removal of all zeros, maximum modulus
   for \(U\) and \(1/U\) proves both bounds throughout the disk.
   The same Rouché argument on the four sides of the rectangle
   transfers the direct winding. [DLMF §1.10(iv)–(v)][dlmf]
2. **(4)–(6), deflation errors.** The simplex moments for the
   evaluation weight \(t_x^j\) and the single knot-shift weight
   \(t_x^jt_k\) are \(j!/(n+j)!\) and \(j!/(n+j+1)!\).
   The entire convex disk contains every segment in the comparison.
   Taking the directed coefficient sum as \(M_{p,k}\) includes
   all local derivative terms through \(k=7\). Under
   \(e_0/\mu_0\le1/1024\), the factor error contribution is at most
   \(\frac12(1/1024)/(1-2/1024)=1/2044\).
3. **(7)–(9), log curvature and known multiplier.** Subtract the
   midpoint of the log-modulus range and extract the second Fourier
   coefficient on a circle of radius \(t\) about the point.
   The coefficient modulus is bounded by \(\lambda/t^2\), and
   the derivative introduces the factor 2. Send \(t\) up to
   \(A-|x-c|\). Differentiating the analytic gamma multiplier
   along the real line gives the displayed
   \(-1/(2s^2)+\psi'(s/2)/16\) before taking its real part.
   The trigamma series at real part \(1/4\) costs
   \(16+\int_0^\infty(x+1/4)^{-2}dx=20\). Hence \(13/4\)
   bounds curvature and \((13/4)(1/2)^2/8=13/128\)
   pays the endpoint interpolation envelope. [DLMF 5.15.1][gamma]
4. **(14)–(16), source and all polynomial errors.** Reflecting the
   half-integral gives the positive-half-line cosine integral.
   For \(k\le7,b\le2\), \(u^k e^{-(8-b)u}\le1\), using the maximum
   \([k/(e(8-b))]^k\) for \(k>0\). Thus the same inherited source
   majorant pays both omissions at every derivative order.
   The finite cosine integral has Taylor derivative of order 65
   bounded by its \(u^{65}e^{Au}\) moment, itself at most
   \(2^{64}\bar B_0\bar{\mathcal Q}\) by the inherited source bound
   and \(u\le2\). Taylor along the complex segment gives
   \(A^{65-k}/(65-k)!\); coefficient radii carry the falling factorial.
   Midpoint integration cancels odd terms and the normalized order-16
   interval coefficient gives remainder \(2h^{17}/17\) times its
   absolute upper bound. This is exactly \(2h^{17}/17!\) times the
   unnormalized derivative bound. The source jet stays on the
   analytic positive-half-line expression.
5. **Rational design checks.** With the declared conditional maxima,
   \(B_*\le4109/4\), \(S\le35970\), and
   \(C<34933/320<110\). The 264 patches at 256 panels each give
   \(67584\) panels and radius below \(110/512^2<1/2000\).
   The repeated-root-label budget is \(1056\).
   The root error is bounded by \(264\,2^{-24}\cdot24
   =99/262144<1/2000\). Exact arithmetic with the saved E06 tail
   endpoints verifies the conditional \(J_{\rm up}-J<17/1000\)
   using all terms and the two-sided factor 2. These are design
   checks. The pilot uses none of the integration panels.

## Code and directed evidence

The [coefficient evaluator][source] uses Arb formal series with 17
terms, interval centers for order-16 remainders and point centers for
the midpoint terms. The coefficient midpoint is an exact dyadic
and its Arb radius covers the sum of all Taylor remainders and
operation enclosures. The checker compares the required radius
directly, avoiding acceptance caused by outward inflation in a
test interval constructor. The proof check covers the interval
recurrences. The solver is only a deterministic proposer of knots.

The [contour evaluator][contours] encloses the full polynomial arc
in a convex box avoiding zero with modulus lower bound
\(>\epsilon_0\). Such a box is contained in an open half-plane
through zero. Consequently the lifted endpoint angle difference
is the principal argument of the endpoint ratio. The directed sum
in turns must enclose a unique integer, with all arc tests charged.
Small circles use polynomial translation, with every translated
coefficient operation enclosed. Synthetic division then uses the
exact dyadic knot list with interval arithmetic. Accepted source
radii and geometry are checked again by the [driver][driver].

Before canonical execution, synthetic tests confirmed an outer count
of two for \(z(z-1/4)\) and refusal to certify completeness from its
one occupied small disk alone. A strict contour rejected \(z-1\) on
the unit circle. Missing counts, understated/non-enclosing coefficient
radii, and zero boundary margin were rejected. Deflation of \(z^2\)
and \(z^2+\eta\) with repeated zero knots gives the constant 1.
For the latter, actual roots still move by \(\sqrt{\eta}\).
With one nonroot knot 1 the divided difference is \(z+1\), and
with zero knots the polynomial is unchanged. No singular-primitive
code was needed. The execution record was checked again by exact
rational comparisons of stored endpoints and count intervals.
The numerical run reached only 128 bits, with per-case limits retained.

## Collision controls and scope

The [controls12][controls] map in [Note14 §8][design] remains in
force. Euler factors change conductor-one coefficients and the prime
baseline. Weighted-square and finite-tail controls lack complete
theta coefficients plus normalized reflection. Finite-prime orbits
lose full reflection. Reflected and smooth/primitive controls lack
the complete square arithmetic and xi/zeta identity. BW-01 and
finite-profile families lack the full coefficient/profile input,
including eventual simplicity where their hypotheses fail.
Normalized endpoint perturbations fail ordinary Dirichlet arithmetic
while preserving the specified completion and functional equation.
Variable readouts change the physical cosine/Newman equation.
Three-profile relaxations lack integer divisor/full-source
realizability. Older counter-kernels lack the literal transform
and anchor, and smooth density changes the discrete prime measure.
The two-channel exclusion retains its specified factorization and
support class. Generic contour and deflation arguments can apply
with each control's own certified source. No real double or other
event is moved to time zero to make a comparison.

The four passes are interval certificates of local acquisition
and the known-region direct target. They establish neither a
full-cover cost nor a signed Green estimate. The direct success
gives the same target its already acquired exclusion comparator.
The remaining covers and all full-integration evaluations require
a separately issued contract.

[dlmf]: https://dlmf.nist.gov/1.10#iv
[gamma]: https://dlmf.nist.gov/5.15.E1
[design]: ../notes/14_TND_OG_B05_R2_CONTOUR_CONDITIONING_AND_COST_20261110.md
[inputs]: ../research-progress/handoffs/26_TND_OG_E08_INPUTS_20261110.json
[record]: ../numerics/09_TND_OG_E08_DIRECTED_PILOT_20261110.jsonl
[note]: ../notes/15_TND_OG_E08_LITERAL_SOURCE_ACQUISITION_RESULTS_20261110.md
[source]: ../numerics/e08_source.py
[contours]: ../numerics/e08_contours.py
[driver]: ../numerics/e08_literal_source_pilot.py
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
