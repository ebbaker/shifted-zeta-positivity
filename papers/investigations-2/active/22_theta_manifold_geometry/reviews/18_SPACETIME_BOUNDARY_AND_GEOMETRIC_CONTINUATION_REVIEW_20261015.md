# Spacetime boundary and geometric continuation review

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. Three delegated mathematical subtasks developed and cross-reviewed the boundary calculus, theta pilot and surface hierarchy; the coordinating agent independently reviewed and replayed the computations. This is internal LLM-assisted review, not external refereeing or formal verification.

The continuation completes the bounded boundary experiment requested by [Review 13](13_GEOMETRIC_SIMPLIFICATION_AND_TOPOLOGICAL_RH_REVIEW_20261015.md) and clarifies two geometric comparisons raised in [Review 17](17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md). There is now a complete-theta, sign-changing boundary certificate and a fair interior baseline. There are also precise links between real-projective jets, normalized real surfaces, and collision multiplicities. None supplies the missing global theta estimate. The existing manuscript and the two requested source documents are preserved.

## Boundary calculation and the completed finite pilot

[Physical-jet Note 06](../notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md) extends the root-count formula to moving walls:

\[
\operatorname{wind}_{\partial D}(H+iH_x)
=\frac{N_--N_+-Q_a+Q_b}{2}.
\]

Here \(Q_c\) is the signed flux of ordinary real roots through a spatial wall, including tangential contacts by one-dimensional local degree. Thus a finite-height boundary need not avoid every zero of \(H\); it must avoid common zeros of \(H,H_x\). Quadratic, cubic and quartic controls have equal initial and final root counts but negative winding, exposing exactly what would be lost by omitting the walls.

On any segment where \(H_x\) has a fixed strict sign, flux is an endpoint sign difference. On a segment where \(H\) has a fixed sign, it vanishes. A half-plane polygon homotopy similarly computes the full boundary winding using only certified enclosures of the two jet coordinates. No phase-denominator integration or third derivative is needed for the winding step. The universal continuous-loop statement is made through the polygon method; the stronger requirement of nonzero first coordinates at cut endpoints is scoped to the analytic boundary hypotheses where it is available.

The complete-theta pilot uses the exact rectangle

\[
[1/100,1/5]\times[25,45].
\]

All 234 boundary segments have certified nonzero jets; both coordinates take both signs. The exact rational polygon has winding zero. A separate scalar calculation gives two simple \(H\)-zeros on each time face and strictly positive \(H\) on both spatial walls, independently yielding the same degree. This excludes collisions in the rectangle by the same-sign local-index theorem.

The full tails are retained: source plus omitted-mode error is below \(3.729\times10^{-33}\) per midpoint derivative; the whole-box Taylor remainder is below \(4.923\times10^{-17}\) per coordinate; the smallest certified boundary coordinate margin exceeds \(1.906\times10^{-9}\). The pilot uses 76 validated midpoint derivative integrals and 786 exact or interval assertions. The independent analytic audit checked positivity, the primitive mass bound, both geometric tail sums, all 77 required moment orders, interval Taylor evaluation, half-plane homotopy and orientation. Exact polygon vertices are retained in the small receipt for direct rational replay.

The comparison deliberately uses a practical interior baseline: 128 full-time strips and 255 range evaluations, sharing the same integrals and error budgets. The boundary uses 464 segment-range plus 234 vertex evaluations; two additional whole-wall checks support the redundant root count. Boundary execution is faster in this particular implementation because most boundary work uses fixed-time coefficients, but it uses more enclosures. Both methods succeed on this low-height box. This does **not** demonstrate a general computational advantage, a new zero-free frontier, or an improved Newman-constant bound. The stronger continuation threshold proposed by Review 17 remains unmet.

## A smaller carrier and a connection between the two topologies

[Physical-jet Note 07](../notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md) distinguishes real projectivization from complex projectivization. The map

\[
[H:H_x]\in\mathbb{RP}^1,
\qquad q=(H+iH_x)^2/(H^2+H_x^2),
\]

has degree twice the jet winding. Forgetting the overall sign retains the obstruction. This corrects a possible over-reading of Note 04: it is allowing unrestricted filling in \(\mathbb{CP}^1\), or restricting to a single complex spatial slice and canceling factors, that loses the circle obstruction. The actual real spacetime line cannot extend across a collision.

For an arbitrary odd-degree real polynomial \(Q\) of degree \(2g+1\), the normalized surface \(C_Q:y^2=Q(x)\) has deficit

\[
\Delta(Q)=g+1-b_0(C_Q(\mathbb R))
=\frac{N_{\rm nonreal}(Q)}2+
\sum_{a\in\mathbb R}\left\lfloor\frac{\operatorname{mult}_aQ}2\right\rfloor.
\]

That deficit equals the total collision weight in the polynomial heat evolution \(e^{-sD^2}Q\) from the selected initial time onward, **including** collisions on the initial slice. Normalization at an event has the pre-splitting real-component count; the deficit is left-continuous and drops immediately afterward. The original polynomial degree remains in the formula, so complex square factors are not erased by normalization.

For reciprocal Jensen polynomials the deficit is nondecreasing with degree and nonincreasing with auxiliary heat time. The proof handles repeated roots through an odd-multiplicity Rolle argument. The polynomial family is explicitly identified with O'Sullivan's existing Hermite–Jensen family. Every finite polynomial eventually becomes strictly real-rooted automatically; a uniform finite heat threshold across all degrees is already RH-equivalent. If RH fails, the thresholds increase without bound. This prevents automatic finite-degree regularization from being mistaken for arithmetic progress. The auxiliary time here is not the physical theta heat time.

The principal synthesis is an exact bridge between the two earlier topological formulations, with their marked data and degenerations retained. The component count, parabolic degree theory and Jensen framework are classical ingredients; no priority claim is made.

## Complex multiplicity and the limit of a dimensional collapse

[Physical-jet Note 08](../notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md) generalizes Review 17's cubic control. At an arbitrary analytic heat collision of spatial order \(m\),

\[
\operatorname{ind}_{\mathbb R}(H,H_x)=-\lfloor m/2\rfloor,
\qquad
\dim_{\mathbb C}\mathbb C\{\tau,z\}/(H,H_z)=\frac{m(m-1)}2.
\]

The proof uses Weierstrass preparation and the \(\sqrt\tau\) Hermite splitting: every pair of emerging roots contributes one order to the discriminant. The complex local degree is positive with complex orientations and negative with the declared quaternion orientation. It equals the Milnor-fiber genus of the fixed-time primitive cusp, but that equality of integers does not identify the underlying germs.

The real and quaternion degree magnitudes agree only for double collisions, although their parities always agree. Shrinking a four-dimensional tube while retaining its zero and nonzero boundary preserves the complex degree; its eventual two-dimensional restriction has a different index. A dimensional collapse therefore needs more than an assertion of degree preservation. This conclusion neither proves nor disproves that anisotropic boundary estimates could be quantitatively useful.

The independent audit checked the weighted analytic expansion, Weierstrass cluster, discriminant order, module length and the precise source/target orientation of Investigation 21. Exact discriminants through order 16 and 27 asymmetric perturbations through order 10 pass 198 assertions.

## Verification and next-work threshold

Three fresh scripts pass in independent processes:

| Check | Exact or validated assertions | Scope |
| --- | ---: | --- |
| Moving-wall flux | 2,122 | 88 polynomial domains and two nontransverse-contact controls |
| Complex heat multiplicity | 198 | 15 model discriminants and 27 asymmetric perturbations |
| Complete-theta boundary | 786 | One finite box, whole-boundary homotopy, root-count cross-check and interior baseline |

The **3,106 assertions** are overlapping computational checks, not 3,106 independent mathematical results. General analytic claims rely on the proofs and internal audits. Replays match after removing only explicitly recorded timing fields. The [verification manifest](../numerics/SPACETIME_GEOMETRY_CONTINUATION_CHECKS_20261015.json) binds the scripts, receipts, research notes, review and unchanged manuscript/source inputs. All new files are below 1 MiB; no manuscript snapshot, commit or tag was created.

The bounded pilot should now be treated as completed. A further numerical expansion should identify a shared-budget case giving a material advantage over the practical baseline, or a new theta-specific error estimate. Additional unmarked ambient geometry alone has supplied no such estimate. The project now has a clearer common vocabulary—real-root flux, marked real lines, real-component deficit and complex pairwise multiplicity—with their distinct logical strengths preserved.

Research provenance retains formal replay identity **24**, thread `01a141e7-5787-7f10-9edc-977e32e7606e`, in the [canonical history](../../../formal_replay_crosswalk/chat-histories/0024_2026-10-15T23-30-42Z_explore-spacetime-and-geometry-ideas.json).
