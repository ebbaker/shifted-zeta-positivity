# VCD-GT-E05 r3 — Fixed-event proof and synthesis assessment

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Reviewer dispatch explicitly
**gpt-6.1-sol / ultra**, the same selection as the E03 r2 proof.
Separate backend attestation and lead configuration are unavailable.
The reviewer authored the E03 r1 residual and had no authorship role
in Note06 or Note07. This is a separate internal check with a shared
proof dependency, model selection and source premises.

**Note06 accepted within the frozen conditional scope without
mathematical correction. Note07 accepted after the inherited-source
scope clarification in §4.** Both [assessment request][request] pins and
all seven [E03 r2 execution request][r2request] inputs matched.
The reviewed originals were Note06
`539afbdb2c2ca2711582b6e5d67297334ecc0fa21cf5ccbb349d717fd488d99a`
and Note07
`b9d8ea8a04ed0e967ed6e10bd48102b6e8bf75a4f8b42f70f0bee7012bfb93be`.
[B02 contract][decision] [Result index][results] [Control catalog][controls]
[Local geometry][geometry] [Coefficient cluster][cluster]
[Avoid index][avoid] [Classification][a01] [Control premises][a02]
[Shared-premise reviews][a05] [Scoped exclusions][a07]
[Signed cancellation][a12]

## 1. Geometry and relative residues

At the stipulated exact order-two zero \(a\ne0\) at interior time
\(T\), the disk avoids the origin and lies strictly inside the phase
strip. Its unit \(A_T\) is nonvanishing there. Strict comparisons on
the fixed outer and smaller concentric circles at nearby times give
the uniform count and buffer. The physical modulus is positive on
a fixed outer collar after restricting time. Uniform convergence
there gives the single-valued ratio logarithm. Its stated bound on
the outer circle uses \(Z_*=|a|+\rho\), even if the collar extends to
points of larger modulus. Cauchy's estimate on a slightly larger
compact set bounds the model boundary derivative. The resulting E02
transfer has both denominators and gives \(K_N\to K\), with no
separation condition between the cluster roots. [Note06 §1][proof]
[E01 assessment][assess1] [E02 assessment][assess2]

The sign of the discriminant is correct. With \(\Delta_j=F-G_j\),
\(\log(G_j/F)=-\Delta_j/F+O(\Delta_j^2)\). The additional minus
from contour integration by parts makes the linear term
\((2\pi i)^{-1}\oint (z-a)\Delta_j/F_T\,dz=\Delta_j(T,a)/A_T(a)\).
Squaring the center displacement contributes another quadratic term.
Dividing its bound \(O(p_j(T)^2 Z_*^{4j})\) by the degree-\(j\)
scale \(p_j(T)|a|^{2j}\) leaves
\(O(p_j(T)(Z_*^2/|a|)^{2j})=o(1)\). The normalized monic norm
envelope \(p_j\le B_{j-1}^j/(2j)!\) pays this at \(j=N\) and at
\(j=N+1\) separately.

For the time defect, replacing the center and the inverse model
field in its contour costs \(O(p_N(T) Z_*^{2N}\sup_\Gamma |R_N|)\).
After division by \(h_N^*(T)|a|^{2N-2}/(2N-2)!\), the
remaining factor is \(O(p_N(T) Z_*^{2N}(Z_*/|a|)^{2N-2})\).
The factorial and the logarithmic upper coefficient envelope make
it vanish for fixed geometry. The sign of the linear defect residue
is \(-R_N(T,a)/A_T(a)\). The phases tend to one, giving
\(r_N(T)/D_N(T)\sim(2N)(2N-1)/a^2\) and
\(r_N(T)/D_{N+1}(T)\sim-\Pi_N/(\beta_{N+1}(T)a^4)\).
The sign of \(r_N(T)\) alternates since \(A_T(a)\) is real nonzero.
The denominator has its own relative estimate, so positivity of
each omitted link suffices and no uniform lower bound is used.
The first \(N\) coefficients specify both actual model evaluators.
[Note06 §2][proof] [E03 r1 assessment][assess3]

## 2. Derivative and signed time comparisons

The physical and model contour equations give uniform
\(D_N'\to D'\) using the proved uniform convergence of
\(K_N,D_N,r_N\). The residual converges uniformly by its explicit
factorial scale and the fixed positive outer model floor.
There is no differentiation of a scalar approximation bound.
Since \(D'(T)=2\), a fixed smaller interval has \(D'\ge1\) and
opposite physical endpoint signs. The same strict monotonicity and
endpoint signs follow for large \(N\), giving one model double
time there. The mean-value quotient converges to \(-1/2\) after
division by \(D_N(T)\), yielding the signed leading displacement.
The inherited Note27 establishes local existence and its uncertainty
window. The uniform derivative and displacement conclusions here
refine that result on the fixed interval. [Note06 §3][proof]
[Parent Note27][parent]

For \(0<\tau_N=o(N^{-2})\), the coordinate error is factorial
small and physical coordinate motion is \(O(\tau_N)\). Taking
square roots places both unordered model zeros within \(o(1/N)\)
of \(a\), including at a merger. The units converge on the
whole disk by quotient comparison on its boundary and the maximum
modulus principle. The kernel \((z-c_N)/Q_N\) is the half-sum of
the two Cauchy kernels, which coalesce without any singular
root-separation denominator. The norm ratio is \(1+o(1)\) by the
\(O(\log^2(N+1))\) bound on
\((\log h_N^*)'=\beta_N+\beta_{N+1}-\beta_1\).
Localization pays the high power in the residual relative to its
nonzero value at \((T,a)\). Thus \(r_N(t)/r_N(T)\to1\) uniformly,
and the bounded \(K_N\) also gives \(W_N\to1\) uniformly.
[Note06 §4][proof]

It follows that the actual signed integral is asymptotic to
\(\tau_N r_N(T)\). For \(\tau_N=N^{-3}\) its magnitude relative
to the actual endpoint error \(|D_{N+1}(T)|\) is asymptotic to
\(16N/(\beta_{N+1}(T)a^4)\) and grows at least as
\(N/\log^2(N+1)\). The same fixed-circle absolute safety allowance
is larger than the actual integral in this regime by the factor in
(11), asymptotic to a positive constant times
\((Z_*/|a|)^{2N-2}\) for fixed valid floors. With \(e=D-D_N\),
\((W_N e)'=W_N[4(K-K_N)D-r_N]\), which gives the plus sign for
the signed defect in (12) after integrating from the later time.
The incoming difference and transferred interaction remain in
the comparison, and the defect magnitude supplies no lower bound
for the complete signed correction. [Note06 §4][proof]

## 3. Synthesis, control scope and inherited source clarification

The synthesis accurately assigns the E01 time-uniform law and
E02 coordinate comparison to supporting work and distinguishes
the r1 allowance from the r2 actual signed term on shrinking
slabs. It retains the modulus, collar, time and coefficient costs,
and the unacquired canonical inputs. It claims no acquired
canonical event or tube, new numerical certificate, uniform
over-height comparison, or exclusion of jointly compensated
transport. The exact quadratic screens strict gap passage and
fails the positive Jacobi-source premise. The weighted-square
controls have the needed time-uniform coefficient and cosh bounds
on their own fixed-event tubes. Their full canonical reflection and
equal square weights fail. That arithmetic is unused here, and
the local collisions remain distinct from finite all-real
thresholds. The other controls retain their individual premises
and the broader positive-source statement is restricted to the
named uniform laws, heat tilt and finite norm/regularity conditions.
[Note06 §5][proof] [Note07 §§1–5][synthesis] [Control catalog][controls]

S03's dominance comparison indeed uses the same first-jet
approximant, phase and norm with independent endpoint envelopes.
It is cited for the scope lesson and supplies no transferred
theorem for GT's contour discriminant. The source-sensitive BW08
bound is a lower bound on the deflated curvature. With
\(h_T=A_T'/A_T\) and \(K(T)=h_T'(a)\), its curvature equals
\(-K(T)\) whenever the local deflation is defined. Its displayed
quantitative bound assumes a double at **\(a\ge20\)** on an
all-real theta slice at **\(T>0\)**. The pinned synthesis gives
the all-real and positive-time conditions but omits the height
gate. Record that gate explicitly in §4. An event-value bound
alone does not pay the integrated cost over a GT tube. The
source's restricted analytic, same-assistant-reviewed status
stays in force. [S03 source][s03] [BW08 Note03, (1)–(4)][bw08]

No numerical runs, proof edits or shared-status edits were made
for this assessment.

The lead applied the height gate in §4 and repaired “avoiding the
origin” in §3. The diff against the original pinned bytes contains
only those two edits. The corrected synthesis reviewed here is
`0e713a2966fcab34185734b81cd6ceb73fcbce7936fef0ad12128f1401a2ff0c`.
The clarification is complete and no mathematical correction remains.

[request]: ../research-progress/handoffs/VCD-GT-E05-r3.md
[r2request]: ../research-progress/handoffs/VCD-GT-E03-r2.md
[decision]: ../brainstorm/notes/02_VCD_GT_B02_FIXED_EVENT_DECISION_20261116.md
[proof]: ../notes/06_VCD_GT_E03_FIXED_EVENT_DEFECT_20261116.md
[synthesis]: ../notes/07_VCD_GT_RESEARCH_SYNTHESIS_20261116.md
[assess1]: 02_VCD_GT_E01_TIME_EXTENSION_ASSESSMENT_20261116.md
[assess2]: 03_VCD_GT_E02_COORDINATE_TRANSFER_ASSESSMENT_20261116.md
[assess3]: 04_VCD_GT_E03_RESIDUAL_ASSESSMENT_20261116.md
[parent]: ../../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md
[s03]: ../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md
[bw08]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
