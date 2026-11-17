# One canonical signed gap estimate — synthesis and continuation

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, branch chat0002. Lead actual
recorded model/effort unavailable. Analytical, numerical and assessment
helpers explicitly dispatched **gpt-6.1-sol / ultra**; separate backend
attestation is unavailable. All assessment is internal with shared source
premises and model selection; no specialist human review.

**Certified local estimate, internally assessed within scope.** [E05 r6](../reviews/08_VCD_GT_CANONICAL_GAP_CERTIFICATE_ASSESSMENT_20261116.md) accepted the proof, code, replay and clarified comparator/source description. This post-assessment status update leaves the assessed mathematical text unchanged.
This round acquires one useful local canonical signed estimate. It does
not prove the general canonical signed gap estimate, new zero coverage,
a new Newman bound or an all-height descent. The previous
[conditional critical-scale results](11_VCD_GT_CRITICAL_SCALE_SYNTHESIS_AND_CONTINUATION_20261116.md)
retain their scope. The [sole register](../research-progress/01_VCD_GT_RESEARCH_PROGRESS_20261116.md)
owns live task status.

Read [result summaries](../../../../../result-summaries/README.md), especially
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md)
and [approximation18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md);
also [avoid](../../../../../avoid/README.md), especially
[classification01](../../../../../avoid/01_restating_the_target.md),
[premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[numerical scope10](../../../../../avoid/10_numerics_ahead_of_the_question.md),
[known coverage11](../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [sibling stops15](../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).
This is a finite quantitative application and matched method comparison,
not a target-equivalent reformulation supported by checks.

## 1. Acquired local estimate

Keep the literal complete heat field and physical normalization

\[
 H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \qquad H_0(z)=\xi((1+iz)/2)/8,
 \qquad \partial_tH=-\partial_z^2H.
\]

The fixed application has
\(a=140101/10\), \(\rho=9/10\), and \(0\le t\le v=1/10\).
For every such time, the enclosure gives exactly two zeros inside
\(|z-a|<3/4\), and no zeros in the closed annulus
\(3/4\le|z-a|\le21/20\). It consequently acquires the count, collar
and buffer for the original radius-\(9/10\) contour, without labeling
individual roots or assuming their slopes. The fixed positive gauge
\(G_t=e^{\pi a/8}H_t\) changes none of these zeros or coordinates.

Let \(c,D\) be the true pair center and squared half-separation, and
\(K\) the exterior-unit divided difference, including its continuation
through a possible double. The numerical enclosure on the full interval
is contained in

\[
 -0.61552<K(t)<-0.59932,
 \qquad K(t)\le k_U=-59/100.
\]

The same source and certified contour formulas independently give

\[
 \begin{aligned}
 0.17873684703&<D(v)<0.17873685811,\\
 0.00142117117&<D(0)<0.00142118229.
 \end{aligned}
\]

All decimal bounds here are loosened outward from the stored enclosures.
The [certificate record](../numerics/05_VCD_GT_LEHMER_CERTIFICATE_20261116.json)
and [execution note](15_VCD_GT_E04_CERTIFIED_SIGNED_GAP_20261116.md)
own the full arithmetic and predicate results.

For the actual signed cost and weight,

\[
 W(t)=\exp\!\left(4\int_t^vK(s)\,ds\right),\qquad
 B=2\int_0^v W(t)\,dt,
\]

the uniform signed upper bound pays the entire time integral explicitly:

\[
 B\le B_U=\frac{e^{-0.236}-1}{-1.18}<0.178151971244,
 \qquad W(0)\le e^{-0.236}.
\]

With the independently acquired lower endpoint of the incoming gap,

\[
 D(v)-B>0.00058487578,
 \qquad D(0)>0.00074055469
\]

where the second inequality divides the lower positive numerator by the
upper positive weight. The exact law \(D'=2+4KD\) gives the identity
\(W(t)D(t)=D(v)-2\int_t^vW\). The positive full-interval margin therefore
proves \(D(t)>0\) throughout this local interval. Conjugation then makes
the two counted zeros real and distinct. The proof never presumes
whole-interval root reality to evaluate \(K\).

## 2. What retaining the sign changes

The absolute-value cost obeys

\[
 B_{\rm abs}=2\int_0^v\exp\!\left(4\int_t^v|K(s)|\,ds\right)dt
 \ge 2v=0.2>D(v).
\]

Its margin is less than \(-0.02126314189\) even with this elementary
lower bound on its cost. Thus it cannot pay this particular incoming-gap
test. The signed upper bound does pay it, with every source, contour,
coordinate and time allowance included.

The earlier two-level [diagnostic](13_VCD_GT_E04_LEHMER_DIAGNOSTIC_20261116.md)
estimated the actual signed cost as 0.177621833068 and absolute cost as
0.226304207962. Its weighted signed margin was about 0.001115019499;
those sharper numbers remain floating contour/time diagnostics. They
are not substituted for the conservative certified bounds above.

**Direct endpoint evaluation is cheaper and tighter on this input class.**
Its interval for \(D(0)\) above exceeds the transported lower bound in
accuracy. Give it the same already paid collar and angular bounds. The
time-zero source row needs 65 distinct xi evaluations, whereas the fine
transport acquisition used 196,673 xi evaluations on 33 times. This is
not a standalone cost for reacquiring that shared geometry. No equal whole-interval cost or
Jacobi coefficient-prefix comparison is asserted. The result distinguishes
the signed and absolute gap budgets on one canonical tube; it does not
establish transport superiority over the direct complete-source method.

## 3. How the continuous-domain errors were paid

[B04](../brainstorm/notes/04_VCD_GT_B04_CANONICAL_LEHMER_ACQUISITION_20261116.md)
selected the exact imaginary Gaussian convolution of the complete xi
function. [Note12](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md) proves it
by Fubini and the full double-exponential Fourier source. Binet's formula
preserves the high-height gamma decay; Euler summation and analytic
periodization supply explicit source lattice and tail bounds. The fixed
fine lattice has spacing 1/4 and cutoff 12, with gauged absolute error
below \(4.962\cdot10^{-7}\). [Assessment07](../reviews/07_VCD_GT_XI_ORACLE_ASSESSMENT_20261116.md)
accepted that proof and its conditional contour interface within scope.

After the diagnostic succeeded, [B05](../brainstorm/notes/05_VCD_GT_B05_UNIFORM_SIGNED_CERTIFICATION_20261116.md)
selected a constant signed \(K\) bound with a closed time integral.
[Note14](14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md) proves a
coarse radius-five bound for the same field. It pays a degree-32 spatial
and degree-32 time polynomial from the existing 128-by-33 field grid.
The complete error includes sample balls, source quadrature, Fourier
aliasing, spatial truncation and true-field time interpolation. The latter
uses the physical heat equation, a 66th spatial-derivative Cauchy bound
and the exact real Chebyshev–Lobatto node product. No heat equation is
ascribed to the finite polynomial.

The resulting uniform field error on the radius-21/20 disk is below
0.03124 in the fixed gauge. For every time, positive real-part bounds for
\(G_t(z)/(z-a)^2\) on the two collar boundaries give count two and the
principal collar log. The geometry passed at 16 time cells and 64
angular arcs per boundary. Its normalized real-part floors exceed
1,060,600 and 1,160,600 respectively. Derivative allowances cover the
whole cells and arcs, rather than only their centers.

The log moments enclose the actual \(c,D\). Annular Laurent tails pay
the 128-node spatial integration, and the same interval coordinates
enter the rational \(K\) kernel with checked denominators. All 512
time cells passed the uniform signed bound. The endpoint anchors also
use the original endpoint rows and their smaller source allowances,
while retaining the same certified collar and spatial tails.

The fine source grid took about 151 seconds in its recorded environment;
the subsequent enclosure replay took under one second and used no new
xi evaluations. The preliminary coarse diagnostic used an additional
36,897 xi calls. Costs describe these executions, not portable performance
guarantees. Source code and small records are in `numerics/`; the
[archive guide](../ARCHIVES.md) gives reconstruction, both hashes and
external-data locations. Hash agreement identifies inputs; the interval
calculations establish the recorded inequalities.

## 4. Controls, prior stops and remaining research

The exact quadratic \((z-a)^2-2(t-1/20)\) runs through the same collar,
moment and interval logic, including its double at \(t=1/20\). It encloses
\(K=0\), the incoming gap \(1/10\), cost \(1/5\), and a strictly negative
full-interval margin. The certificate does not falsely permit passage
through its collision. The broader control screen is recorded in
Notes12/14: changed positive sources may share the generic heat and
contour identities, but they do not supply the unchanged xi samples
used here. Their missing arithmetic alone is not a proof that every
untested signed inequality fails for them.

The [OA Lehmer stop](../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md)
reported missing acquisition and the wrong direction of an upper exterior
inverse-square sum. This round acquires its own positive-time geometry
through the complete source and does not use that reversed implication.
The OA status is unchanged. The
[primary source-use record](../references/01_VCD_GT_LEHMER_SOURCE_USE_20261116.md)
checks the normalization and time-zero candidate location; it imports
no positive-time certificate or RH premise. Parent B07/E25 and both
unactivated siblings remain unchanged.

This completes the fixed local signed-versus-absolute question with a
same-source direct comparator. It leaves open a general source-sensitive
signed estimate, height-uniform acquisition costs, and applications where
transport offers an advantage over direct evaluation. There is no reason
to repeat the same known-pair certificate at higher precision or scan
other pairs without a new comparison question. The interval already ends
at zero, so subdividing it into E06 slabs would add no descent result.

The next conceptual task, **B06**, is gated on an explicit new mathematical
input or an information-class comparison that the present complete-source
oracle does not already settle. Recommended Astra/ultra; any ensuing fixed
proof or computation goes to Sol6.1/ultra under a new frozen packet. The
question must name the source estimate, actual acquired data, independent
incoming gap, full cost and equally informed direct comparator. No such
new inequality is asserted ready by this continuation. The finite local
cycle may close without closing the investigation or claiming a manuscript
milestone.

On resumption, read this synthesis, Notes12–15, their assessments, the
sole register, root workflows and the result/avoid pointers above. Preserve
the floating-versus-certified distinction and shared-premise review limits.
Refresh the registered chat at turn start; arrange final capture against
the actual current turn only after the real reply is ready to be sent.
