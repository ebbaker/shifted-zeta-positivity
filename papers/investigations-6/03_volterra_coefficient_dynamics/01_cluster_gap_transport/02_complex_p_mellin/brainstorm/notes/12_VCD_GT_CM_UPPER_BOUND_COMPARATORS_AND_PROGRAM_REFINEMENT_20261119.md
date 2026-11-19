# Upper-bound comparators before backward gap continuation

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Guarded chat configuration: **gpt-6-astra,
reasoning effort max**. Status: **literature comparison and prospective
program refinement; same-assistant source checks**. No new Newman bound,
canonical continuation estimate, certificate replay campaign, manuscript
milestone or main B/E task activation.

Read-first routing: [result index][results], [Cluster11][heat],
[Cluster18][approx], [avoid index][avoid], [classification01][class],
[premises02][premises], [scope07][scope], [joint bounds12][joint] and
[imports16][imports]. Under classification01 this is a comparison of
established/reported methods and a prospective quantitative experiment,
not a new RH criterion. Sources and inspection limits are in
[Receipt03][receipt]; exact parameter bookkeeping is in [Record07][record].

## 1. What each source contributes

**Platt–Trudgian.** Theorem 1 of [arXiv:2004.09765v1][pt] verifies RH
through the exact height 3,000,175,332,800, using interval computation and
a completeness count. Section 3.4, Corollary 2, obtains Lambda <= 0.2 by
supplying that height to Polymath's existing criterion. This is stronger
finite input to that criterion; it supplies neither a new moment evolution
law nor the fine gap data needed by our proposed continuation. Their
Section 2 explicitly distinguishes finding enough sign changes from
isolating every zero more accurately than the verification requires.

**Gomila.** The [public explanation][blog] and [proof package][package]
apply the same Polymath criterion at the Platt–Trudgian verified height.
The package presents Lambda <= 0.1787854 as a computer-assisted proof
awaiting peer review. Its mechanism is a certified lower bound for the
full arithmetic approximation, an infinite-tail argument, and a barrier
valid throughout the time interval. This reading does not independently
replay its certificate corpus.

The exact choices are X=6,000,000,185,827, t0=129/800 and
y0^2=87677/2500000. Consequently

\[
 t_0+y_0^2/2=0.16125+0.0175354=0.1787854.
\]

The required zeta height is X/2=3,000,000,092,913.5. The exact verified
height leaves 175,239,886.5 of reserve. Replacing the verified endpoint by
the rounded headline 3e12 would incorrectly suggest a small uncovered
interval. These are arithmetic checks of reported parameters, not a
verification of their analytic admissibility. [Proof note][proof].

## 2. The proof target is a strip, not a list of real gaps

[Polymath Theorem 1.2][poly] combines three inputs: initial zero exclusion
up to X/2; final-time exterior exclusion above imaginary height y0; and
an intervening spatial barrier throughout 0<=t<=t0. It concludes

\[
 \Lambda\le t_0+\frac{y_0^2}{2}.
\]

The extra time y0^2/2 is essential: a global strip of half-width y0
contracts to the real axis under the heat flow. The criterion does not
require all zeros to be real and individually separated already at t0.
Thus a real-pair continuation argument starting at t0 cannot simply import
Gomila's conclusion as its separated starting configuration. A later
all-real time and quantitative simplicity/separation information are
separate inputs.

The same accounting applies to the 0.2 bound. The repository's
[parameter review][parameter-review] records the relevant Polymath row
as t0=0.186 with an approximately 0.014 strip payment; treating 0.2 as
the row's t0 and setting the payment to zero changes the argument.

## 3. Arithmetic cancellation must reach the final inequality

Gomila's [native-binding lemma][binding] explains the finite-sum step.
An Euler mollifier reorganizes arithmetic coefficients before taking
absolute values. Exact convolution and a bound for the mollifier transfer
the result back to a lower bound for the original normalized sum f_t.
A positive intermediate bound also justifies division by the mollifier.
This is a quantitative transfer, not free removal of an analytic factor.

For our purposes the most useful prior work is the repository's
[October audit][audit] and its [subsequent review][audit-review], both
pinned to a74738deb6d5e0f76887cb36901da08b68dca705. The web commit listing
returned that same revision, and the pinned proof/native-binding documents
were read here. The earlier internal audit examined the analytic links,
32 independently certified finite rows and the barrier gates. Its full
independent producer/corpus audit remained unfinished. The external
package's own broader replay claims do not change that local scope.

Its central lesson concerns retaining the Riemann–Siegel correction C.
Schematically, the two approximations are

\[
 H_t/B_t=f_t+\delta_0,
 \qquad H_t/B_t=(f_t-C_t/B_t)+\delta_1,
 \qquad |\delta_1|\ll |\delta_0|.
\]

A bound |f_t|>=L cannot automatically use the smaller allowance for
delta1. It needs a bound for |f_t-C_t/B_t|. Paying |C_t/B_t| separately
can spend the recovered margin. This was the obstruction for the audited
uniform triangle estimate; it is not a theorem excluding phase-sensitive
bounds or other mollifiers. The review explicitly scopes the earlier
approximately 1.2e-8 sensitivity figure to a local, nonrigorous calculation.

The blog now also reports a later 0.1782354 calculation at the same
verified height, with its mathematical review still pending. It attributes
the change to a retuned lower-time construction. That calculation was not
audited here. It reinforces why the earlier construction's apparent limit
must not be called a universal limit imposed by the verified height.

## 4. Refinement of the proposed experiment

[Discussion11][previous] remains a useful starting point: the full
arithmetic approximation persists beyond the regime where its n=1 terms
give a clock. Its forced residual equation is exact for the stated
reference field. The literature comparison changes what should be
measured next:

1. Choose one common domain and retain the full arithmetic reference,
   including any correction whose smaller remainder is being claimed.
   Specify a fixed cutoff or pay its changes, contour floors, spatial
   derivatives, time dependence and exterior/boundary data.
2. Compare complete margins using that same information. For a real pair,
   use the error in the integrated drift of D=g^2/4; for a Polymath
   certificate input, use the actual nonvanishing or barrier margin.
   These are different deliverables. A smaller residual norm alone is
   neither deliverable.
3. Ask whether preserving arithmetic phases and dependencies in the
   drift gives a longer certified interval than direct evaluation of the
   same complete source. For H=P+E, the candidate joint numerator is
   P E_zz-P_zz E; any cancellation must survive division, contour
   integration, center error and the nonzero heat defect of P.

The finite milestone is a numerical improvement in the complete margin
or certified time interval at matched inputs, not merely another identity.
A global Lambda improvement would additionally require complete height
coverage, the appropriate initial data and cleared interfaces. A useful
local gain can be investigated before that assembly, with its scope stated.

No new experiment is executed in this reconnaissance. The immediate
structural question is which dependence in the arithmetic source the
existing separate bounds lose, and whether retaining it improves the
chosen final quantity enough to matter.

## 5. Collision screen and scope

The analytic premise screen in [Discussion06][screen] was reapplied to
the unchanged-source proposal using [Controls12][controls]. Euler-factor,
weighted-square, finite-source/score/prime and positive-primitive controls
fail the specified full theta arithmetic/source identity; finite-profile
and atomic controls fail its full profile. The reflected super-Gaussian
also lacks the imported order-one product premise. RH-conditional endpoint
controls change ordinary Dirichlet arithmetic and assume RH in their
construction; changed observation kernels fail the physical Newman
readout. Static divisor surgery supplies no common source heat path.
These failures do not establish that a future coarse bound distinguishes
the controls; the bound itself still has to do so.

The generic residual transfer passes the essential collision test only
if it preserves H=P=z^2-2(t-T), E=0: exact approximation still collides at
t=T. Discussion11's [existing exact check][control-record] shows that
the integrated shrinking allowance exhausts the initial D at the merger,
so strict positive margin fails. The strong-collar quartic and annular
controls remain tests of a generic contour transfer; literal canonical
source equality fails, but their collisions cannot disappear through
normalization. No new universal exclusion or impossibility result is
claimed.

[pt]: https://arxiv.org/html/2004.09765v1
[poly]: https://arxiv.org/html/1904.12438v2
[blog]: https://www.judegomila.com/posts/riemann-lambda-0.1787854
[package]: https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/tree/a74738deb6d5e0f76887cb36901da08b68dca705
[proof]: https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/blob/a74738deb6d5e0f76887cb36901da08b68dca705/PROOF_NOTE.md
[binding]: https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/blob/a74738deb6d5e0f76887cb36901da08b68dca705/NATIVE_BINDING.md
[receipt]: ../references/03_PLATT_TRUDGIAN_GOMILA_METHOD_COMPARISON_20261119.md
[record]: ../numerics/07_UPPER_BOUND_PARAMETER_BOOKKEEPING_20261119.json
[previous]: 11_VCD_GT_CM_POLYMATH_ERROR_STRUCTURE_AND_BACKWARD_USE_20261119.md
[screen]: 06_VCD_GT_CM_RESEARCH_POSITION_AND_PATHS_DISCUSSION_20261118.md
[control-record]: ../numerics/06_POLYMATH_RESIDUAL_ALGEBRA_20261119.json
[results]: ../../../../../../../result-summaries/README.md
[heat]: ../../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[approx]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[avoid]: ../../../../../../../avoid/README.md
[class]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[imports]: ../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[audit]: ../../../../../../investigations-2/newman_certificate_audit/README.md
[audit-review]: ../../../../../../investigations-2/newman_certificate_audit/reviews/CROSS_MODEL_REVIEW_OF_CLAUDE_AUDIT_CODEX_20261013.md
[parameter-review]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/reviews/20_ADDITIONAL_PATHS_FORWARD_ASSESSMENT_CODEX_20261016.md
