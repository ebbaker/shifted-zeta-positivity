# E13 r1 proof and implementation check

9 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex assistance, OC chat0010. Recorded thread settings
**GPT-6.1 Sol / ultra**. The exact per-turn backend and helper settings
are unavailable. Separate internal helpers checked the analytical
constants, contour and runtime interfaces, and ordered kernel. This is
an internal LLM assessment with shared source premises.

[Request27][request] and [Inputs27][inputs] fix the six obligations.
All mathematical input hashes matched. P1–P6 passed on the first check under the
frozen proof, source, observable and declared gates.

| Gate | Disposition and check |
| --- | --- |
| P1 | Pass. On the closed rectangle, $s=1/2-iz/2$ has imaginary part in $[-1006,-494]$. Thus the zeta pole, trivial zeros and the zeros/poles of the completion factors are absent there. The affine map preserves multiplicity and $H_0(z)=\xi(s)/8$ gives the same divisor. The open canonical strip is the classical critical-strip result. |
| P2 | Pass. $u^2\le r_u/12$ and the positive theta majorant give $\mathcal M<8640/1331<7$. The first term on $[0,1/10]$ gives $H_0(0)>1/7290$. Jensen at zero with the doubled disk gives $N_{\rm disk}(r)\le2r^2+40$, including boundary labels by a limit. Two slabs per omitted shell give omitted weight $<2^{-44}$ uniformly in the center. For $N\le1024$, the ordered omitted pairs are bounded by $2(N+b)b<2^{-32}$. |
| P3 | Pass. For $0<a\le1/2$ the Gaussian $e^{-at^2}$ and its first two derivatives have modulus at most one. Integrate the opposite height weight over the whole line to bound the gradient by $9/T$ and the Hessian row sums by $18/T$. For the diagonal, the bounds on $I_T$, $I'_T$, $I''_T$ are $(2,2,8)/T$, and transverse derivative bounds $1,2$ give $4/T,10/T$. The center integration range stays fixed during differentiation. |
| P4 | Pass. Residues give the unweighted centroid of the multiset of labels. Its complex displacement sum vanishes in both real coordinates. Apply the second-order bound in each argument of the raw sum and then to $D(z)=K(z,z)$. The error is $(18N+5)S_2/T$ before centroid rounding. Subtract $n_C$ same-label terms, which leaves $n_C(n_C-1)$ in a collapsed cell. |
| P5 | Pass. A compact convex zero-free image box lies in an open half-plane through zero. Its segment increment is the endpoint-ratio principal argument, checked strictly inside $(-\pi,\pi)$. The outward sum divided by $2\pi$ must contain a unique nonnegative integer. Inherited boxes contain clipped segment images. The midpoint rule cancels the linear term on the symmetric real segment parameter, and the integral remainder is bounded by $L^3\sup\lvert G_C''\rvert/24$. The cubic zeta jet uses the factor $-i/2$. The quotient jet gives $G_C''=2[(z-a_C)R_2+R_1]$ where $R=Z'/Z$. The interval denominator must exclude zero. The final centroid check uses a Euclidean upper bound from the entire complex ball to an exact dyadic point. |
| P6 | Pass at proof/preflight scope. Exact-rational replay gives analytic cap $1208254589/536870912000<1/400$ and combined cap $2550431869/536870912000<1/200$. The run may use the proved improvement $S_2\le r^2\sum_{n_C>1}n_C$ and the observed count. The symmetric center/gap factors are shared, and both ordered mark products are summed. The exterior allowance is added to the outward arithmetic ball. The process supervisor enforces elapsed time independently of FLINT calls. |

The version-pinned scalar and cubic wrapper chain and the
Euler–Maclaurin coefficient remainder were inspected for the actual
isolated runtime. The evidence uses those outward library enclosures.
[Source-use15](../references/15_TND_OC_E13_FLINT_SOURCE_USE_20261109.md).

## Synthetic execution controls

The retained contour self-test has one simple real root and two double
nonreal roots. It obtains count 5 and multiplicities 1, 2, 2, covers the
three known centroids by the Euclidean balls, and encounters four rejected
candidate cuts. An additional helper check used a double nonreal root
on a prescribed cut and confirmed the complete count and enclosed
centroids after the next cut choices. The kernel was compared with a
direct ordered sum for synthetic unequal marks, multiplicities and
centers at the two finite edges. Empty and singleton divisors give zero
factorial contribution. The repeated-root check retains both ordered
pairs. These controls lack the complete canonical source identity.

The [collision-control inventory][controls] is screened as in
[Note20 §7][note]. The Euler-factor controls change the source identity.
Weighted-square, finite-tail and finite-prime controls lose full
normalized reflection or the complete unit-coefficient expansion.
Reflected super-Gaussian, smooth-shape and positive-primitive controls
lose that complete arithmetic expansion. Atomic and finite-profile
controls lose the complete theta growth/profile. The RH-conditional
theta-close control loses ordinary Dirichlet-series arithmetic. The
variable-kernel control loses the physical cosine/Newman equation. The fixed-time centroid lemma
uses the divisor and the smooth test. The fractional
relaxation lacks a realizable integer divisor. This review applies a premise screen to the existing collision
certificates.

This evaluation is classified as a finite projected source measurement
under [avoid01][classification]. Its success condition is the paid
projection enclosure, as prescribed by [avoid11][purpose]. The complete
joint marked profile, asymptotic correlations, and positive-time
collision constraints require separate evidence. Apply the scoped
reading in [avoid07][scope].

## Executed disposition

The [execution record](../numerics/18_TND_OC_E13_R1_EXECUTION_20261109.json)
reports the first exhausted gate during centroid quadrature. The 2,000,000
source calls comprise 1,801,138 scalar and 198,862 cubic calls. The
elapsed time was 462.85 seconds. The gate was reached before the finite
kernel pass.

A source-free audit read the entire retained trace. It matched the
stored hash and event counts, reconstructed exact edge coverage and
shared fragment containment, checked the longest-side cuts and
parent/child counts, and verified that the 388 occupied leaves
sum to the outer 388. For each of the 91 completed centroids the
moment segments cover all four oriented edges. The displayed
Euclidean bounds also pass when rounded outward and reparsed.
The maximum squared leaf diameter was `625/17179869184`, the
maximum cell depth 38, and the maximum retained segment depth 20.
The audit checks the recorded structure and radii. The arithmetic
certificate uses the outward library calls from the execution.

The appropriate disposition is a certified finite census and partial
centroid evidence with a named work-limit stop. The proposed B10 r3
decision concerns the method for paying the projection width.
[Continuation24](../continuation-notes/24_TND_OC_AFTER_E13_AND_MODEL_CHANGE_20261109.md).

[request]: ../research-progress/handoffs/27_TND_OC_E13_R1_CONTOUR_CENTROID_EVALUATOR_REQUEST_20261109.md
[inputs]: ../research-progress/handoffs/27_TND_OC_E13_R1_INPUTS_20261109.json
[note]: ../notes/20_TND_OC_B10_R2_CONTOUR_CENTROIDS_AND_GAUSSIAN_ESTIMATE_20261109.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[purpose]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
