# Review of the finite-time comparison and source-acquisition return

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Chat0005, thread `01a17e41-99d3-79c1-b932-2bae84ad0d47`.

**Internal same-model review, including separate read-only agents; no
specialist or cross-model validation.** This assesses [Note12][n12],
[Note13][n13], and [the continuation][n14]. The actual model and effort
were read from this turn's session metadata. No interval theta evaluator
or new coverage experiment was run.

## Results and scope

Note12 strengthens Note10's asymptotic energy statement to an exact
finite-time lower inequality on the declared isolating all-real interval.
It keeps the exterior's sign and gives an explicit reflected-cluster
floor. The complete logarithmic coefficient remains kappa_m. This is
geometric information compatible with colliding controls.

Note13 supplies a conditional constructive approximation without inserting
exact event-cancelled low moments. All theta modes beyond K, the entire
frequency tail, and retained-integral quadrature have explicit payments.
It includes both a conservative midpoint baseline and an analytic source
quadrature with exponential convergence in order. Fixed-coefficient
rounding and point evaluation still require their stated enclosures.
The small number of derivative terms is not a runtime or bit-complexity
claim. No signed theta margin or new bound on Lambda follows.

## Mathematical checks

1. **Factors and centered dynamics.** Note09 uses b=U_z/U, whereas
   Note12 uses the full exterior velocity B=2b. Thus B_x=-2 sum_ext
   gap^(-2). Triple cancellation gives sum f_i^2=2E and sum y_i f_i=p.
   The square defect is E-p^2/(2V), and V'=4p-2S. These factors give
   kappa=p/8=m(m-1)/16, including 1/8 and 3/8 for doubles and triples.

2. **Global premise and singular endpoint.** Exterior realness and
   order-one growth justify the sign and differentiated product. They
   cannot be inferred from a local event alone. The cluster remains
   isolated and simple for u>0. V(0)=0 and bounded exterior derivatives
   justify integration to zero; no individual velocity is used there.
   Reflection gives lambda_ref=m/[2(|a|+rho)^2] with rho<|a|.

3. **Comparison and normalization.** From S>=lambda V, integration
   gives V<=2p(1-exp(-2lambda u))/lambda and hence the displayed energy
   and integral lower bounds. The lambda->0 limit is kappa/u. The
   constant term kappa lambda agrees with -2kappa gamma. No positive-lambda
   equality model is claimed in the order-one heat class.

4. **Raw source tails.** Positivity, 2n^2e^(4v)>=n^2+e^(4v), and a
   geometric n-tail give Cbar=(8/3)pi^2e^(-pi/2). The explicit frequency
   gate bounds the full integral by Cbar e^(-L)/(4L). Frequency, omitted
   modes, and quadrature each consume epsilon/4; fixed-coefficient error
   has the fourth quarter. There is no discarded arithmetic tail.

5. **Quadrature.** The source derivative in Note13 (10) has coefficients
   30pi^2,-15pi,-8pi^3. The complex Lipschitz midpoint bound has factor
   1/(4M). Analytic disks of radius 1/16 stay in cos(4Im v)>0. Cauchy
   gives geometric Taylor tails, and integrating the even terms produces
   (2k+1)! in the denominator. Each derivative of the heat integrand
   still solves heat. The derivative-term count is fixed-parameter only;
   its height cost is explicit in |a|d.

6. **Derivative and transfer domains.** K,V,orders and nodes are frozen
   in s,w. Holomorphic buffers justify Cauchy in these variables, not in
   the real resolution r. The source approximant is not inserted into
   Note10's complex-r parity argument. Note09's static energy transfer
   remains conditional on its count, amplitude and discriminant gates.

7. **Source-side stop list.** Existing finite-Gram and positive-multiplier
   controls were read and linked, rather than offered as a fresh arithmetic
   proposal. Existing compact HDC certificates were also checked before
   proposing any first-jet implementation. Literal theta coefficients
   distinguish what is evaluated but do not by themselves distinguish a
   derived inequality; the return claims no excluding inequality.

The final read-only review corrected the finite-profile control screen:
its documented threshold models pass the all-real comparison. Finite-prime
local controls do not supply that global premise. It also corrected one
formula-formatting character and made the replay's pi^2<10 substitute
explicit. No outstanding mathematical objection was reported after these
corrections.

## Replay and review provenance

The standard-library [replay][script] and [small record][record] check:

- Exact rational variance, shape-defect and exterior identities for m=2..12,
  with real exterior poles. A positive exterior-slope negative control
  violates the required compression premise.
- Integer-verified conservative frequency/mode schedules for three
  (m,N) choices and six radii, including very small symbolic radii. These
  are parameter illustrations, not measured canonical c or event data.
- Exact analytic-quadrature integration of monomials through degree 2q-1
  for q=1..5, and detection of the first omitted even term.

The replay passed. Its hash identifies the script; it does not validate
theta zeros. Three same-model agents supplied read-only derivation,
source/control, and review checks. One checked both the midpoint extension
and its constants; another separately checked the analytic quadrature and
growing-order count. The authoring assistant assembled and checked the
complete statements. Their shared model and inherited premises limit the
independence of this review.

CE-02 has a new finite source-acquisition sub-result but remains Partial.
CE-04 has a finite-time lower comparison, with exclusion still open.
CE-05 retains zero strict margin. CE-06 has no new excluded slab. CE-07
has new explicit acquisition dependencies, not an endpoint theorem.
CE-08 integrates this assessed return. Parent TRD statuses are unchanged.

[n12]: ../notes/12_FINITE_TIME_CLUSTER_ENERGY_COMPARISON_20261027.md
[n13]: ../notes/13_UNCONDITIONED_SOURCE_ACQUISITION_AT_COLLISION_SCALE_20261027.md
[n14]: ../notes/14_SECOND_RETURN_AND_NEXT_CANONICAL_CALCULATION_20261027.md
[script]: ../numerics/02_check_finite_time_and_source_acquisition_20261027.py
[record]: ../numerics/02_FINITE_TIME_AND_SOURCE_ACQUISITION_CHECKS_20261027.json
