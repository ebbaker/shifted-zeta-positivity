# Assessment of radial integrand preservation and angular flows

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0007. **Same-assistant internal assessment, not independent specialist review.**

The revised [manuscript][ms], Sections 9–10, incorporates the user's radial-integrand invariant and explicit auxiliary flows. [Note20][n20] supplies the technical return; [Brainstorm02][b02] separates further proposals. The new results are finite-parameter representation, concentration and equation identities. They do not establish a theta-specific collision exclusion.

## Mathematical checks

The radial and volume normalizations were checked: H=(1/8)∫r^(3/2)Q_t cos(z log r/2)dr becomes (1/(32π))∫r^(−1/2)F_{s,t} cos(z log r/2)d³X when PF_{s,t}=Q_t. The r-to-u Jacobian is retained. PΔ=Δ_3P follows from the spherical Laplacian's zero integral; the compact first-harmonic potential example has the coefficient χ″+2χ′/r−2χ/r². The Darboux density differs by the displayed total derivative, so preserving that pairing is not mislabeled as uncorrected pointwise preservation.

For the normalized exponential flow, differentiating Z_s=P(e^(sq)) gives the auxiliary equation and variance derivative. The cap normalization, exact exterior mass, angular first moment coth(s)−1/s and square norm s coth(s) follow by elementary integration. The transport profile follows from the inverse characteristic Jacobian of dv/ds=1−v². It is kept distinct from the exponential family. Removable values at s=0 are stated; no limiting smooth operator at infinity is claimed.

The full differential operator was checked by applying A_s L_λ A_s^(−1) to a test field, retaining both the first-order drift and zero-order derivative terms. Its forcing is A_sQ_t. The transformed boundary operator cancels the radial derivative of A_s exactly. Since A_s is independent of the running t,λ, the physical derivative observations and the stated time law follow without omitted parameter terms. The selected response and finite-s inverse are explicit; no general spectral-domain theorem is used.

In the collision-adapted profile, m(u)>0 and n(u) is smooth. The candidate frequency is frozen when constructing q; it does not vary with the running z. The second component of the vector moment is bH_a, including its minus sign from differentiating cosine. The bound m≤1+bu pays the weighted cap tail. The curve localizes angular directions at the existing radii, not the radial support or the physical event itself. Radial derivatives of the moving cap axis are included in the operator-cost formulas. Fixed-parameter derivative bounds are not promoted to all-height uniform bounds.

The Gaussian-polynomial control retains its exact collision and hence its zero vector moment after concentration. The other registered smooth controls pass the same generic projection calculation on their stated convergence domains; no numerical certificate was rerun. Their failed canonical premises are identified in Brainstorm01 and the control register. Atomic controls are not treated as smooth forced fields.

**Angular concentration does not, by itself, exclude a collision.** The complete induced weighted energy pulls back to the original energy identity. The ordinary full norm with positive radial weight cannot decrease under normalized angular redistribution. These conclusions concern those comparisons, not every localized signed estimate, every possible objective, or every nonmultiplicative deformation.

## The proposed projected Laplacian flow

Brainstorm02's annular prototype uses G=0 at both radial boundaries and PG=0 initially. Averaging its equation gives the homogeneous radial heat equation for PG. For smooth solutions, this keeps PG=0. Orthogonality of P in Euclidean volume and integration by parts then give dE/ds=−∫|∂_sG|². The statements are explicitly conditional on the required solution regularity. Existence, global smooth joins, complete response/boundary realization and a collision-sensitive objective remain future work. The prototype does not assume positivity of Q+G, consistent with the user's sole-invariant requirement.

## Document and record checks

The final manuscript compiles to **13 pages** with latexmk/pdfLaTeX and also succeeds in the desktop editor compiler. The final terminal log contains no warnings, unresolved references, overfull boxes or underfull boxes. All thirteen pages were rendered and visually inspected; the title, equations, page transitions, references and margins are legible. Earlier mathematical Sections 2–8 match the pre-edit source exactly. The author field and LLM acknowledgment remain, with the user's proposal credited.

The [build record][build] retains source/PDF hashes and verification details. The PDF stays in the ignored shared output folder; no manuscript snapshot was created. The milestone history and current program navigation were updated. The DLMF convention check is recorded in annotation09 and extends the existing reference catalog. These production and algebra checks do not constitute numerical evidence for RH or independent review.

**Disposition:** retain the explicit finite-s constructions and the broadened invariant in the manuscript. Treat the steered-tube estimate and projected Laplacian descent as candidate next tasks. No new theta bound or completed positive-threshold contradiction is claimed.

[ms]: ../radial_deformations_and_zero_dynamics.tex
[n20]: ../notes/20_AUXILIARY_ANGULAR_FLOWS_AND_COLLISION_LOCALIZATION_20261027.md
[b02]: ../brainstorm/02_AUXILIARY_FLOWS_FOR_COLLISION_LOCALIZATION_20261027.md
[build]: ../numerics/13_ANGULAR_FLOW_MANUSCRIPT_BUILD_RECORD_20261027.json
