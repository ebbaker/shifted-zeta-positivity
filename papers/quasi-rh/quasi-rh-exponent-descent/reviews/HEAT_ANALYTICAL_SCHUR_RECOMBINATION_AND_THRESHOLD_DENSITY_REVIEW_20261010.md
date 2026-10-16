# Analytical continuation: Schur cones, prescribed coefficients, and threshold density

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. The derivations and cross-audits are
internal LLM work, not independent mathematical validation.

## 1. Outcome and scope

This continuation follows the requested priority of analytical proof discovery.
It develops sufficient Schur cones, an explicit coefficient transformation
with a proved global error, and a stronger necessary threshold condition from
the genuine zero count. It also identifies an obstruction to using one
root-free canonical-product chart on the existing long derivative probe.
No numerical atlas, optimizer, or parameter sweep was expanded.

The new files are:

* [Heat Note 20](../newman_collisions/notes/20_ANALYTIC_SCHUR_CONES_AND_DENSITY_STRENGTHENED_THRESHOLDS_20261010.md):
  analytical order-four Schur cones, scalar tolerances, a conditional
  factorial-normalized multiplicity hierarchy, and density strengthening.
* [Project 09 Note 6](../newman_collisions/09_prime_phase_torus/notes/6_ANALYTIC_COMMON_FACTOR_SMOOTHING_AND_PRIMITIVE_SIGNED_FRONTIER_20261010.md):
  common-factor smoothing of the prescribed difference coefficients, with
  every block/complement term, and three scoped structural checks.
* [Heat Note 21](../newman_collisions/notes/21_DEFLATED_LOCAL_GROWTH_AND_THRESHOLD_MULTIPLICITY_20261010.md):
  local-growth and derivative-average lemmas, genuine count bounds, and
  polynomial models delimiting the general heat/root mechanisms.

All proofs retain their hypotheses. None establishes the missing opposite
signed inequality for the actual prescribed coefficients throughout the
shrinking sector. The ordinary-double and general-m statements do not
constitute a uniform collision exclusion or an RH proof.

## 2. Analytical Schur cones

Note 20 starts from the complete real bounded remainder of Heat Notes 8 and 19.
At a true candidate, the actual finite value and first derivative force the
first two Schur parameters. Regrouping the second through fourth errors
preserves a nonpositive quadratic coefficient in the next free parameter.
Completing that square supplies explicit sufficient bounds using endpoint
maxima and the signs of the forced parameters. The cone permits nonzero
finite value, first and third derivatives and either normalizer sign.

The proof assumes an oriented second derivative bounded away from zero in
remainder units and a nonnegative lower fourth-derivative center. These are
arithmetic hypotheses to prove, not consequences of the two candidate
equations. Failure of the sufficient cone is inconclusive. Boundary Schur
parameters terminate the map and must use Note 19's fixed-jet formulas.

The all-m central extension has constants independent of m after factorial
normalization. It assumes that the lower **finite** jets vanish exactly in
addition to the lower genuine jets. Genuine lower zeros do not imply that
extra condition. For nonzero lower finite jets, further forced Schur steps
and their derivative payments remain necessary. The order-four cone's
positive second derivative itself rules out multiplicity at least three
where that cone is established; it supplies no global multiplicity bound.

## 3. Complete prescribed-coefficient transformation

Project 09 Note 6 groups each ordered pair as n=ja, m=jb with coprime a,b.
It preserves j at most J_* exactly and uses Euler–Maclaurin on the remaining
literal integer intervals. Each interval retains the natural cutoff floors
and one of the four block/complement classes. The prescribed quadratic
log-weight is differentiated exactly. The difference phase is independent
of j; it remains the actual common-height phase in the outer coprime sum.

For any fixed Euler–Maclaurin order r, the total error is

\[
 |R|\le C_r\mathfrak M(Nw_N)^2J_*^{-2r-1},
 \qquad
 \mathfrak M=(1+|\epsilon|)^2
 (1+|\Gamma|+\|\Lambda\|+\|B\|).
\]

The proof is uniform for sufficiently small time and physical parameter
\(1\le\kappa\le3/2\). It includes the low index a=1 and real common
factor values near N. Constants depend on r; they are not asserted to be
numerically optimized or uniformly bounded as r increases.

For bounded dual parameters,
\(J_*=\lceil N^{(1+\delta)/(2r+1)}\rceil\), with
\(0<\delta<2r\), gives \(O_r(N^{-\kappa/4-\delta})\).
The comparison is with the existing physical **upper-budget scale**,
not a lower bound for the actual error at a center. Growing duals keep
their explicit factor \(\mathfrak M\) and candidate payment.

The product sine and cosine sums are exact throughout. The theorem does
not estimate their sign or the sign of the primitive and small-common-factor
difference sums. A positive primitive coefficient mass is proved only for
the original, zero-dual kernel before signed phases are applied. It is not
a signed lower bound and does not apply to the density-strengthened kernel.

Candidate-null duals cannot identically eliminate the homogeneous
sixth-degree cosine kernels because their additions have degree at most
five. This allows cancellations after summation or on restricted states.
An absolute derivative estimate for the product common-factor phase incurs
\((1+|T_{\mathrm{phase}}|)^{2r}\), with
\(|T_{\mathrm{phase}}|\asymp N^2\); its available bound grows even
at the largest nontrivial power cutoff. This diagnoses that specific
estimate and is not a lower bound on its actual oscillatory remainder.

## 4. Genuine density strengthens the necessary sign

The imported uniform count has one absolute, symbolic constant
\(C_{\rm count}\). Set

\[
 D_0=8\pi(4C_{\rm count}+1),\qquad
 X_0=\max\{(4\pi)^2,2D_0,3\}.
\]

For an all-real time and an exact-m root x at least X_0, the right-hand
block \((x+D_0,x+2D_0]\) contains at least \(\log x\) roots with
multiplicity. It is disjoint from the forced negative mirror cluster.
Consequently

\[
 S_0\ge\frac m{4x^2}+\frac{\log x}{4D_0^2},\qquad
 \mathscr D_m\ge\frac{\log x}{4D_0^2}q_m^2.
\]

For m=2 the necessary threshold expression therefore uses

\[
 \gamma_{\rm count}=\gamma+\frac{9\log x}{2D_0^2}.
\]

The Schur cones can substitute this coefficient directly; their full-disk
remainder remains the same. In Schur units the gain is of order 1/L, while
in the centered moment dual \(\Gamma_{\rm count}\) is of order L.
These different scales must not be confused.

The centered quadratic physical payment must be recomputed with
\(\gamma_{\rm count}\). If
\(s=\gamma_{\rm count}-\gamma\), the earlier measured payment
increases by at most

\[
 s\{2|g_2|\widehat\delta_2+\widehat\delta_2^2\}.
\]

This is covered by the existing asymptotic upper-budget scale, but the old
measured payment cannot be carried over unchanged. The transformation
theorem retains \(\mathfrak M\): for bounded chosen duals the new
normalizer makes \(\mathfrak M=O(L)\). For example, r=1 and
\(J_*=\lceil N^{2/5}\rceil\) still give
\(O(LN^{-\kappa/4-1/5})=o(N^{-\kappa/4})\).

This is a derived necessary condition for the genuine function under the
imported count and all-real hypotheses. The constant is not made numerical,
and no novelty or arithmetic opposite-sign claim is made.

## 5. Local transfer and multiplicity coverage

Note 21 integrates the full-deflation canonical product on an interval
shorter than the distance d to any remaining root. It proves exponential
upper and lower bounds for the deflated factor and a derivative-average
upper bound in terms of the actual leading jet, next jet, inverse-square
root sum, and normalizer curvature. A closed elementary sufficient
condition avoids quadrature.

The same genuine count gives \(d\le2D_0\). Since the existing long
derivative probe length tends to infinity along the shrinking sector, one
root-free chart cannot span it at sufficiently small time. A root-product
transfer on that probe would have to retain every encountered root and
control the changes of leading jets between charts.

The count jump gives
\(m\le2C_{\rm count}\log(2+x)=O(1/t)\) on the stated sector.
This yields a finite hierarchy on each time interval bounded away from zero
within that sector; it supplies no finite hierarchy uniform as time tends
to zero. The polynomial heat models admit arbitrary multiplicity at an
exact positive threshold and imaginary-axis positivity, but lack the genuine
infinite zero density and prescribed coefficients. They delimit generic
heat and mirror arguments without contradicting the count-based result.

## 6. Validation performed

The Schur derivation's three regroupings, two threshold coefficients, and
fourth-center difference passed six exact integer-coefficient polynomial
identity checks. Separate LLM cross-audits rederived the Schur expansion,
the adverse quadratic sign, completed-square costs, endpoint bounds,
scalar tolerances, and factorial m=2 conversion.

Cross-audits also checked the ratio sine orientation, four floor intervals,
Euler–Maclaurin remainder sign, exact heat-weight derivative recurrence,
weighted-bin cardinality including the final a=1 bin, global remainder
power, primitive coprime count, degree obstruction, and product-phase loss.
For Note 21 they checked the compensated logarithm formula, derivative
envelope, count-block constants, disjoint mirror addition, multiplicity
jump, arbitrary-m threshold examples, and the ordinary-double sharpness
limit. One precision correction was made: for fixed r the accelerated
common-factor exponent requires \(0<\delta<2r\).

Primary-source dependencies were checked against the cited Schur algorithm,
[NIST Euler–Maclaurin identity](https://dlmf.nist.gov/2.10.E1),
[Bernoulli Fourier series](https://dlmf.nist.gov/24.8.E1), and
[Polymath's uniform zero count and canonical-product statements](https://arxiv.org/html/1904.12438v2).
The notes distinguish these imports from their new deductions. No numerical
sweep, interval atlas replay, or external specialist review forms part of
this analytical continuation. Internal checks are not a formal proof audit.

## 7. Next bounded analytical task

The primary task is now a signed estimate of the remaining actual
coprime-ratio and product sums, with the density-strengthened normalizer and
the same dual parameters used in the candidate payment. The common-factor
formula already supplies a vanishing transformation error for a cutoff
that pays the tracked dual scale. A useful next
result must improve the signed main sum, rather than that remainder.

Start with the complete macroscopic block and both mixed classes, retain
the literal cutoff endpoints, and derive an oscillation-preserving product
summation formula together with the outer coprime-ratio formula. Their
remainders must be summed globally before comparison with the physical
payments. The candidate value and derivative equations can enter through
the existing candidate-null dual, with the actual phase and prescribed
weights retained throughout.

A sufficient success criterion is a proved strict negative upper bound
for the transformed full dual plus its transformation error, one-sided
candidate payment, and recomputed physical jet payment on a specified
shrinking subsector. A formula whose primitive coefficients or product
terms are paid by their whole absolute mass does not meet this criterion.
If the sign estimate requires a lower bound on the second derivative,
higher multiplicities and the small-curvature candidates must remain an
explicit separate branch. Parameter endpoints, complementary heights,
and the small-time limit remain requirements of the eventual global argument.

The Schur cone is a supporting target for such an arithmetic identity.
The generic local-to-average route is lower priority until a multichart
transfer supplies the missing actual-jet control. Additional finite
rectangles would not resolve either analytic obligation.
