# Continuation for analytic conserved spatial contours

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

## Research mandate

Continue analytical research toward a result and proof suitable for [book.tex](../../manuscript/book.tex), in support of RH implying simple zeros. The theorem form remains flexible. The conservation-law material is presently provisional and belongs in [main.tex](../../manuscript/main.tex), where the author requested it be placed. Do not move it into the book merely because the formal derivations compile or have been internally checked. **Numerics always play a supporting role in an identified analytic argument.**

Use the new [research overview](../research-overview/03_CONSERVED_SPATIAL_CONTOURS_ANALYTIC_PROGRAM_20261023.md) and [SCF progress file](../research-progress/03_CONSERVED_SPATIAL_CONTOURS_PROGRESS_20261023.md). SCF-01–04 support the overarching [SIMP goals](../research-progress/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRESS_20261023.md); the OBF/HDC registers retain their technical status. Read the [result index](../../../../../result-summaries/README.md), [local geometry summary](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../../avoid/README.md), [controls](../../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../../avoid/01_restating_the_target.md), and [coupled-estimate discipline](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## What the author means by the contour

The geometry is **z=T+i epsilon(T,t)**, with real heat time t and canonical H_t=-H_zz. Epsilon depends on height and time. This is a spatial contour, not a boundary at heat time t-epsilon(T,t). The author suggested zero-flux buffeting, possible natural averaging without smoothing, integral preservation, a Lagrangian/Noether interpretation, and the rigidity of an infinite conserved hierarchy. No smoothing, stationarity, white noise or statistical cancellation has been assumed.

The most natural initial law is H_t+partial_z H_z=0. Its literal-current velocity p=H_z/H preserves every material subarc of H dz. The positive density |H|^2 and metric |H|^2|dz|^2, the primitive image P(t,Z), and the primitive-path Noether action agree with it. The adjoint field action yields an infinite hierarchy; its complete Fourier values determine H. These explicitly time-dependent invariants encode linear heat evolution. They have not yielded a new coercive theta estimate or an autonomous Hamiltonian integrability theorem.

The physical first-jet connection and regularized zero-current actions preserve different quantities. Keep the original Chern–Hopf three-form, spatial circulation, scalar zero count and complex H dz integral distinct. A closed integral of entire H vanishes; a conserved mean does not control repeated inward crossings; a regular outer boundary can enclose a double zero.

## Read these sources first

1. [Note 16](16_NATURAL_CONTOUR_EVOLUTION_20261023.md) and [Review 07](../reviews/07_SPATIAL_CONTOUR_EVOLUTION_REVIEW_20261023.md): full derivations, normalization, actions, hierarchy, controls and limitations.
2. [Provisional manuscript section](../../manuscript/conserved_contours.tex), included by main.tex after `contours.tex`; [integration review](../reviews/08_CONSERVED_CONTOURS_MANUSCRIPT_REVIEW_20261023.md) and [build receipt](../../manuscript/CONSERVATION_BUILD_RECORD_20261023.json).
3. The new overview and progress file for the immediate analytic task. [Note 13](13_COMPLETE_XI_LOGARITHMIC_HEAT_ANCHOR_20261023.md) supplies the previously derived Gaussian/complete-xi apparatus, with an exterior Euler-region scope that must not be silently moved into the critical strip.
4. The book's complete relative-flux and source-residual arguments, and [Note 12](12_HERMITE_CLUSTER_DOMINATION_AND_JOINT_CONSUMER_20261023.md) for the joint consumer, when an acquired estimate can actually supply their complete inputs.

The earlier arithmetic study is preserved in [Note 15](15_BROADER_MOLLIFIER_TESTS_AND_CONJUGATE_MOMENT_20261023.md) and [Review 06](../reviews/06_BROADER_MOLLIFIER_AND_CONJUGATE_REVIEW_20261023.md). It closes only specified fixed-rank/high-smoothing positive-norm comparisons. Do not restart those searches or describe them as a universal simplicity ceiling. The conjugate direction still needs an unproved discrete holomorphic square-moment input.

## First concrete analytic target

**Proposed target only; not proved or imported as a theorem in the manuscript.** Under RH at t=0, allowing multiplicities, fix positive offsets 0<b_-<b_+ and c>0. Set L=log Y and p_0=H_z(0,z)/H(0,z). Investigate the uniform estimate

\[
 H(-s,z)=H(0,z)\exp\{s p_0(z)^2\}
 \bigl(1+O_{b_-,b_+,c}(L^{-1})\bigr),
 \quad 0\le s\le cL^{-2},
\]

for Y<=Re z<=2Y and b_-<=Im z<=b_+, with enough extra strip margin for Cauchy differentiation. Here s is a heat duration; epsilon(T,t) continues to denote the spatial height. This target assumes only initial RH, not a negative-time zero-free tube. It does not propose uniformity as b_- tends to zero, a complex-time extension, or a 1/log Y heat interval.

A possible proof has three substantive obligations. First derive p_0, p_0' and p_0''=O(log Y) on the enlarged strip from initial RH and complete zero-count bounds, with multiplicities retained. Second use the exact Gaussian convolution and extract the full complex linear exponential: H(0,z+u)/H(0,z)=exp(p_0(z)u+O(Lu^2)) locally. Its Gaussian integral is exp(s p_0^2); retain the phase when comparing relative error. Third control the entire omitted Gaussian tails after dividing by the small complete field H(0,z). This requires a uniform initial lower estimate and the gamma, polynomial and zeta factors, not an absolute small tail alone. A sufficient tail route is a proved ratio bound C Y^A(1+|u|)^A exp(a_0|u|), followed by Gaussian domination outside a fixed local radius. All constants, strip margins and the s=0 limit need a written proof.

If the estimate and its analytic remainder are proved, differentiate on a smaller strip and derive the actual material lift: p(-s,z)=p_0(z)+O(1), partial_z p(-s,z)=O(L), displacement O(1/L), and Z_a=1+O(1/L) for an initially flat arc. Bootstrap within a paid finite spatial buffer, including horizontal end extensions. This would acquire the wall nonvanishing and tangent control rather than assume them. It would remain a fixed-offset contour lemma; earlier nonreal population and one-sided collision flux would still require an additional estimate.

The exact tangent ratio is Z_a=H(0,Z_0)Z_{0,a}/H(t,Z). Its continuous phase matters for graph preservation. Avoid requiring separation from every global primitive critical value: another branch can share a critical value while the selected branch remains regular. Conversely, critical-value avoidance alone does not prevent escape. The canonical primitive has the conserved finite real asymptotic value pi Phi_even(0)/2. Use a branch-local buffer and account for its boundary image or another genuine escape bound.

If this candidate only reproduces existing wall control without improving a relevant estimate, state that scope and revise the target. The goal is a useful analytic result for the eventual proof, not completion of this particular formula at any cost. Compare a claimed gain with direct estimation from the same canonical information.

## What remains open

SCF-01 is the canonical estimate; SCF-02 is its justified contour consequence; SCF-03 is the strongest supported collision/simplicity transfer; SCF-04 is the selective book proof. All remain open at their intended scope. A complete Fourier hierarchy with different constants can coexist with collisions, even with positive source and positive-time real zeros. Theta-specific values may distinguish the canonical problem, but their effective use must be shown. Conserved weighted length and area degenerate at zeros and at the finite primitive end, so positivity by itself supplies no escape or collision barrier.

No new simplicity proportion, global graph theorem, stochastic cancellation or complete physical-cap bound was established by this manuscript incorporation. The new section includes the proved identities and controls; the microscopic target above is an explicit next research question.

## References and chat records

Use the [citation catalog](../../references/README.md) and [BibTeX list](../../references/sources.bib). Noether, Cole, Hopf, Ibragimov's two distinct articles, Anco and Papanicolaou–Kallitsi–Smyrlis are included in main.tex. The archived ALGA volume contains Ibragimov's 2006 article, not the separate 2007 JMAA article. Preserve inspection scope and retrieval status. Add each relevant newly discovered paper under the root [reference workflow](../../../../../REFERENCE_WORKFLOW.md); external PDFs stay outside Git.

This chat is **history 0007, Begin continuation research**, thread `01a16b04-b6e2-7823-bfac-b364f4bea3aa`, in the current brainstorm `chat-histories/`. Preserve its unique existing number, filename and first-capture identity. The [verification receipt](../chat-histories/VERIFICATION_SPATIAL_CONSERVATION_20261023.json) checks the local records and exact public-source correspondence at a stated snapshot, with any wider-registry limitation reported separately. It verifies provenance, not mathematical correctness.

At each subsequent reply follow [tools/CHAT_HISTORY.md](../../../../../tools/CHAT_HISTORY.md): refresh at the beginning and before finishing, then arrange the bounded exact-turn final capture as the last tool action. Do not insert an unsent response into a history. Snapshot hashes and counts change legitimately on later refreshes. Native-hook activation has not been independently verified here; retain the bounded follow-up workflow.
