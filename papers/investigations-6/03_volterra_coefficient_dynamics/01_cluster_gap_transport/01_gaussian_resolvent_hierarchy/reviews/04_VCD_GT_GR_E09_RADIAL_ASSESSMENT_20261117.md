# VCD-GT-GR-E09 r1 — Compact radial weak-law assessment

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. The requested helper configuration was
**gpt-6.1-sol / ultra**. Actual serving model and reasoning effort were
unavailable to this assessor. This is an internal assessment by a separate
agent using the shared premises of [E08][proof]. [Shared premises05][shared]

**E08 accepted within its frozen scope, with no required correction.**
On the independently paid canonical count-two tube, each compact \(J_p\),
\(p=1,2,3\), is Lipschitz in normalized time with constant \(C_pL^2\).
The weak law for the compact forcing has an \(L^\infty\) density.
The full radial moments and forcing have the exact increment identities
with the continuous Gaussian horizontal complements retained. This is
a regularity and representation estimate under [Classification01][class].
[Frozen E09][request] · [Frozen E08][e08request] · [Result index][results] ·
[Cluster13][cluster] · [Avoid index][avoid]

## Cutoffs and complete force

- **Test extension and complement.** Since \(d\le a^2/16\), on
  \(|u|\ge a/3\) the denominator modulus is at least
  \(|u|^2-d\ge (7/16)|u|^2\). The quintic and its first two derivatives
  match the constant pieces at both joins. This gives the claimed spatial
  \(C^2\) extension and continuous \(D\)-derivative, including at the
  inner-cutoff joins. Every target is in \(|w|\le r_0/4\), where all test
  derivatives vanish, and every exterior occurrence is in \(|w|\ge r_0\),
  where the inner cutoff leaves the rational Gaussian test unchanged.
  Thus \(J_p\) equals the exterior sum with the horizontal cutoff. The
  complementary weight \(1-\kappa\) includes both transition bands and
  all farther shells. The \(16/15\) collar factor, the complete shell
  count and \(e^{-\alpha L^2n^2}\le e^{-\alpha L^2}\) give the coefficient
  \(2C_{\rm u}(4L+3)\le10C_{\rm u}L\) in (2) after factoring out
  \((16/15)^p L^{-2p}e^{-\alpha L^2}\). The absolute tails tend to zero
  uniformly on the tube at fixed \(T\). Finite multiset continuity on
  local zero-free contours gives continuous \(E_p\). [E08 §1][proof] ·
  [Note41 §3][n41]
- **Fixed charts and safe-line subtraction.** The reference boundaries
  are zero-free locally. With center drift below \(1/4\), the cluster
  covers the support and both targets, is contained in \(|\Re w|<3\),
  and has at most \(12C_{\rm u}L\) occurrences. Outside it the horizontal
  distance from any test point to a root is at least \(1/4\). In (3),
  evaluate the complete opposite-paired log derivative at \(s=c+x+4i\),
  remove the finite cluster at \(s\), and use the absolutely convergent
  difference from \(s\) to \(z\). This retains every exterior occurrence
  and every term of the canonical conditional force. Evenness and the
  paired Hadamard product used in Note41 account for the exponential
  prefactor. Differences cancel the genus-one regularizers, and finite
  cluster removal from the canonical limit works for a nonsymmetric
  cluster. The separate bounds \(2C_{\rm u}L\), \(4C_{\rm u}L\),
  \(16(4+1/3)C_{\rm u}L\) and \(200C_{\rm u}L\) sum to less than
  \(280C_{\rm u}L\). The last uses \(|s-z|\le5\), denominators at
  least \(n/2\) for \(n\ge4\), and the complete two-direction shell
  counts. [E08 §2][proof] · [Note40 §1][n40] · [Note41 §§1, 3][n41]
- **Chain rules and target force.** Off the chart events a zero moves
  by \(H_{zz}/H_z\), twice the regular term of the logarithmic
  derivative at that zero. Its test contribution differentiates
  with relative velocity \(\rho'-c'\) and with \(D'\psi_D\).
  The reality of \(c\) makes its term \(-c'\partial_x\psi\).
  For an active exterior displacement \(w\), the two target forces
  combined give \(4w/(w^2-D)\), with the factor two from the heat
  velocity included. Both are present as cluster pairs in (5), even
  though each target gradient is zero. The outer horizontal cutoff
  gradient remains in the test derivative. The inner gradient is
  included in the extended derivative and vanishes at every root,
  while it can contribute to the Hessian on a chord. Chart membership
  is fixed locally and support crossings use the zero extension.
  [E08 §3][proof]

## Real symmetrization and bounded assembly

For a displacement \(p_1+iq_1\) between distinct cluster roots, the
reciprocal vector is \((p_1,-q_1)/(p_1^2+q_1^2)\). The gradient
difference in (5) is the chord integral of the Hessian applied to
\((p_1,q_1)\). In the reciprocal contraction the cross terms are
\(p_1q_1(\psi_{xy}-\psi_{yx})=0\), componentwise over \(\mathbb C\).
The numerator left under the chord integral is
\(p_1^2\psi_{xx}-q_1^2\psi_{yy}\). The factor two and its sign in
(5) follow from the ordered velocities. The Hessian norm bound pays the
chord uniformly to a merger, without a sign claim for the complex test.
[E08 (5)–(7)][proof]

With \(G,K_2,F_\delta\) as in E08, the four physical-time bounds
from (5) are \(N^2L^2K_2\), \(2N C_{\rm ext} G L^2\),
\(N L G C_c L^2\) and \(N L^2 F_\delta(2+4dBL)\).
The center estimate comes from both deflated-field values in Note41 (3).
Since \(\dot\delta=D'=2-4\delta m\), the complete bound on \(|m|\)
gives the last term in (7). Multiplication by \(L^{-2}\) and
\(N\le N_0L\) yield each displayed contribution to \(C_pL^2\).
At fixed \(p,a,d,\alpha,C_{\rm u}\) the test norms and constants are
independent of \(T\), chart and interval duration. [Note41 §§1, 3][n41] ·
[E08 (6)–(7)][proof]

The fixed closed space-time box contains every chart cluster, and its
multiple-zero locus is closed by continuity of \(H,H_z\). The canonical
slices are nonzero entire functions. At each multiple point the local
Hermite splitting exhausts the isolating disk and separates the leading
roots by order \(\sqrt{|t-t_*|}\) on both available sides. Each such
space-time point is isolated, and compactness gives finitely many
points and event times, including the inward treatment at endpoints.
Neither a uniform event separation nor a global root labeling enters
the estimate. Continuity of the finite multiset sum across chart and
support changes and at the events joins the derivative bounds with
only the elapsed normalized time summed. This proves (8), with the
weak density on the tube interior and no event atoms for \(J_p\).
[Inherited Hermite assembly §§2–4][hermite] · [Note40 §2][n40] · [E08 §3][proof]

## Forcing scope and comparator

The product rule for \(16\delta J_3\) gives
\(16\delta\ell^2\mathcal L_3+16(2-4\delta m)J_3\). With
\(|J_3|\le B_3L\) the extra term has the required \(O(L^2)\) size.
The exact increment of \(12A_2+16\delta A_3\) adds \(R(v)-R(u)\)
for \(R=12E_2+16\delta E_3\). E08 bounds \(R\) by (9) and proves
its continuity. The \(L^\infty\) weak density and absolute continuity
are established for \(J_p\) and \(12J_2+16\delta J_3\). Absolute
continuity of \(A_p\) and of the full radial forcing is unestablished
by this argument. A continuous remainder of uniformly small size
alone gives no derivative bound. Use the exact remainder increment
when applying (10). The full Riccati forcing also includes
\(12U_2+16\delta U_3\) with the exact
\(1-e^{-\alpha |w|^2/\ell^2}\) weight. [E08 §§1, 4][proof] ·
[Note41 (13)][n41]

An equally informed direct calculation has the same canonical field,
paid pair, cutoffs, center and discriminant, complete velocities,
safe-line subtraction and occurrence counts. Applying the same
test chain rule directly to those velocities gives the same compact
law and complement allowance. The accepted modulus gives no
improved signed forcing or adverse-cost estimate. A transport
comparison would also give both methods the same paid incoming
value. [B03 decision][decision] · [Assessment19][a19]

The documentary premise screen is retained. Euler-factor translates
change the canonical source and fail the documented endpoint matching.
Smooth shape and positive-primitive controls change theta arithmetic.
Finite-source, finite-score and finite-prime changes lose full
reflected theta equality. The endpoint-defective classes lose the
documented width-one strip. The reflected super-Gaussian fails the
order premise, and the fractional-profile relaxation loses the counted
integer divisor. The fixed-event and finite-profile classes lack
canonical population growth, the RH-conditional sources change
ordinary Dirichlet arithmetic, and varying the observation kernel
loses the physical cosine readout. The equal-count sign slices
supply no common canonical time tube. Finite heat polynomials may
share the compact weak law despite collisions. The E01 quartic cusp
concerns failure of time \(C^1\) in its finite polynomial class and is
consistent with the accepted Lipschitz conclusion. [E08 §5][proof] ·
[E01 audit][e01] · [Controls12][controls] · [Premises02][premises] · [Scope07][scope]

One assessment and one bounded correction check were completed. The
E09 proof pin and the five E08 inherited-input pins matched. The
correction check rechecked the absolute shell constants, the mixed
chord contraction, the normalized derivative and the forcing scope.
No proof edits were required.

[request]: ../research-progress/handoffs/VCD-GT-GR-E09-r1.md
[e08request]: ../research-progress/handoffs/VCD-GT-GR-E08-r1.md
[proof]: ../notes/04_VCD_GT_GR_E08_RADIAL_WEAK_LAW_20261117.md
[decision]: ../brainstorm/notes/02_VCD_GT_GR_B03_RADIAL_WEAK_REPAIR_20261117.md
[e01]: 02_VCD_GT_GR_E01_INPUT_AUDIT_20261117.md
[n40]: ../../notes/40_VCD_GT_E20_FIXED_COLLAR_TIME_OCCUPATION_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[a19]: ../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md
[hermite]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[shared]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
