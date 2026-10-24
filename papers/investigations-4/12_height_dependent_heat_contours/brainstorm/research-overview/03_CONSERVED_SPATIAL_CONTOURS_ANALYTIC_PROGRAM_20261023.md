# Analytic conservation laws and spatial contours toward the book proof

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Current continuation after the book theorem:** use [Overview 04](../../research-overview/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRAM_20261023.md) and its [progress register](../../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md) for the next arithmetic work inside the acquired contour. This earlier overview retains its program history; the fixed-offset theorem is now an input, and the multiplicity-sensitive arithmetic estimate remains open. Updated 23 October 2026 for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**.

The objective is to prove an analytic estimate for the unchanged theta heat field that makes its conserved spatial-contour dynamics useful in a proof toward RH implying simple zeros. The immediate aim is a canonical comparison theorem controlling an actual transported contour and the collision-sensitive quantity it carries. The eventual theorem may concern individual zeros, an exceptional count, a proportion, or another substantive intermediate result. Its form should follow the strongest argument obtained.

The author has now requested the completed fixed-offset result and full proof at the center of [book.tex](../../manuscript/book.tex), under the title *Conserved heat contours toward simple zeta zeros*. The [revision note](../notes/20_THEOREM_CENTERED_BOOK_REVISION_20261023.md) and [same-model internal review](../reviews/10_THEOREM_CENTERED_BOOK_REVIEW_20261023.md) record this intermediate manuscript milestone. Its all-multiple control and complete collision-resource obligations are central to the selection. RH implying simple zeros remains unresolved. The broader conservation-law exposition remains in [main.tex](../../manuscript/main.tex), through [conserved_contours.tex](../../manuscript/conserved_contours.tex). **Analytical results and their proofs govern this program. Numerics always have a supporting role.**

The [progress file](../research-progress/03_CONSERVED_SPATIAL_CONTOURS_PROGRESS_20261023.md) owns SCF-01–04. These support the broader [SIMP program](02_ANALYTIC_RH_TO_SIMPLICITY_PROGRAM_20261023.md); existing OBF/HDC registers retain their tasks. [Note 16](../notes/16_NATURAL_CONTOUR_EVOLUTION_20261023.md) and [Review 07](../reviews/07_SPATIAL_CONTOUR_EVOLUTION_REVIEW_20261023.md) contain the derivations and their scope. Follow the [result index](../../../../../result-summaries/README.md), [local heat-geometry summary](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../../avoid/README.md), and especially [target classification](../../../../../avoid/01_restating_the_target.md), [coupled estimation](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [collision screening](../../../../../result-summaries/12_collision_controls_and_screening.md).

## The analytic mechanism

The contour is spatial, z=T+i epsilon(T,t), with real heat time t and H_t=-H_zz. It is not the earlier backward-time face. The native conservation law H_t+partial_z H_z=0 selects velocity u=H_z/H when its spatially constant current freedom is fixed to zero. It preserves H dz on every material subarc. For the canonical even field, the primitive

\[
 \mathcal P(t,z)=\int_0^z H(t,w)\,dw
\]

satisfies P_t=-H_z, and the contour is the continuation of the inverse image of its initial primitive image. No smoothing term is assumed. The positive conserved metric |H|^2|dz|^2 and area density |H|^2 give the same motion. The adjoint and primitive-path actions explain the Noether structure; the regularized zero current and physical-jet connection provide alternative observables with different material velocities.

The complete Fourier invariants determine H from the actual theta profile. The adjoint heat-polynomial invariants provide a discrete hierarchy. These explicit time-dependent invariants encode the linear evolution; their number or completeness alone is not a quantitative constraint on collisions. Positive-source collision controls have their own complete conserved data. The proposed analytic gain must use the particular canonical values and retain the cancellations they imply.

## Canonical comparison contract and its completed fixed-offset instance

Seek one **canonical contour comparison theorem**, starting with a prescribed compact initial arc and a finite height/time window chosen for its relevance to the eventual simplicity argument. Its proof should estimate displacement and the true tangent transport from complete theta information, with explicit endpoints, scale dependence, normalization and remainders. Do not begin by assuming an unknown zero-free tube, a favorable minimum of |H|, or the desired strain bound and call the resulting conditional flow theorem the arithmetic result.

The exact tangent identity gives a concrete object to estimate:

\[
 Z_a(t)=\frac{H(t_0,Z_0)}{H(t,Z(t))}Z_{0,a},
 \qquad
 \frac d{dt}\log Z_a=\partial_z(H_z/H)(t,Z(t)).
\]

Its continuous argument controls turning and loss of graph structure; its modulus controls stretching. A useful proof can estimate the coupled ratio or its integrated logarithmic derivative directly. Replacing them immediately by separate suprema can discard the desired cancellation. A finite interval on which the tangent remains in the right half-plane gives a graph, but the research task is to prove the canonical estimate that ensures this, not to restate that sufficient condition.

A promising comparison uses a fully specified analytic reference F and the numerator

\[
 H_zF-HF_z,
 \qquad
 \frac{H_z}{H}-\frac{F_z}{F}
 =\frac{H_zF-HF_z}{HF}.
\]

Use the book's complete-source residual and reference machinery only where its assumptions apply. Derive the coupled numerator and its tangent derivative before estimating; retain every carrier derivative, reference heat defect and small-value denominator. A comparison must acquire its reference floor and relative error from actual analytic inputs. An exterior Euler-region anchor alone does not supply a critical-strip floor. The reference, scale and normalization may change if the proof indicates a stronger route.

The first continuation should identify the exact source information that could bound this ratio on a useful window, carry out that estimate, and compare it with the corresponding direct estimate from the same information. A new uniform canonical bound is a substantive result even before its strongest global consequence is known. Another coordinate identity or a generic Gronwall theorem is supporting material already largely available.

### The completed fixed-offset theorem and its limitation

Under RH for the initial field, allowing multiplicities, the completed estimate is the following. Fix 0<b_-<b_+ and c>0, set L=log Y and p_0=H_z(0,z)/H(0,z). Then

\[
 H(-s,z)=H(0,z)e^{s p_0(z)^2}\bigl(1+O_{b_-,b_+,c}(L^{-1})\bigr),
 \qquad 0\le s\le cL^{-2},
\]

uniformly for Y<=Re z<=2Y and b_-<=Im z<=b_+, with an enlarged strip for analytic differentiation. **This estimate is now proved at the displayed scope in [Note 18](../notes/18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md)**, with the first correction s p_0'(1+2s p_0^2) and O(log^-2 Y) analytic remainder. RH supplies fixed-strip logarithmic bounds, and horizontal integration of p_0 controls the entire relative Gaussian tail. No negative-time floor is assumed. [Review 09](../reviews/09_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_REVIEW_20261023.md) records separate-agent same-model internal checks.

The proof gives the actual material graph, paid end coverage, O(1/log Y) displacement/tangent deviation, and upward motion as heat time runs backward. No shrinking-offset or complex-time uniformity is included. Its estimates are also satisfied by G_0(z)=F(z/2)^2[1+cos((log 2)z/4)], a positive-source field with the same coarse zero count and no simple initial zeros. Thus the next substantive target is a multiplicity-sensitive estimate distinguishing that control, using the acquired wall as an input. [Continuation 19](../notes/19_CONTINUATION_AFTER_FIXED_OFFSET_THEOREM_20261023.md) records the remaining obligations.

The book now proves an explicit resource corollary: a smooth symmetric window covering [Y,2Y] has zero-free upper and lower transitions, so only its horizontal end regions contribute nonreal influx. The earlier interior nonreal population and this complete one-sided end influx remain in the multiplicity bound, with coverage and current-limit obligations retained. This is an exact use of the acquired wall, not an upper bound for either remaining term.

## Continue the inverse branch and pay its geometry

The contour must remain on a defined inverse branch in a controlled region. Separation from every global critical value is not required for a selected regular branch; a different branch can have the same image value. Critical-value separation alone is insufficient for an entire primitive: inverse lifts can also escape toward asymptotic values. Here the canonical real-axis limit is already finite and conserved,

\[
 \lim_{x\to+\infty}\mathcal P(t,x)
 =\tfrac12\int_{\mathbb R}H(t,x)\,dx
 =\tfrac\pi2\Phi_{\mathrm{even}}(0).
\]

This follows from real-axis decay, evenness and the zero-frequency invariant. A finite-buffer proof must control its spatial boundary and the image through which a lift could leave; a global proof needs asymptotic-value control as well as critical values. Preserving weighted length is not an independent barrier: the metric degenerates at zeros and has finite length toward this high-height end. A global fixed nonzero Im P level is not the default bounded-width contour. Start with the actual image of the chosen initial arc.

The analytic comparison should therefore produce enough displacement, branch and continuous tangent-angle control to justify its own moving domain. Keep ordinary contour regularity distinct from simplicity of enclosed zeros. A regular boundary can pass through time while a double zero occurs inside it.

## Turn contour control into a mathematical consequence

After obtaining a source estimate, determine what it actually bounds. For the nonreal-resource route, pay the earlier nonreal population, one-sided relative inward current, height ends, real-axis cutoffs and complete coverage. Signed conservation of a mean or circulation does not bound repeated entries. For regularized currents, fixed-regulator identities do not justify a limit along regulator-dependent moving windows without a uniform argument.

Use the existing sharp finite consumers, including the joint heat/spectral consumer where its assumptions are available, only after the complete required input is bounded. If the new estimate instead controls a different collision-sensitive observable, derive its strongest honest consequence and compare with relevant known results. No fixed percentage, density conclusion or preselected width law is imposed. RH and additional hypotheses must enter at named steps.

For the original topological route, the physical Chern–Hopf three-form still requires its complete boundary, caps, connecting faces and excisions. Conserved line circulation from a first-order action is a different quantity. The alternative action is worth pursuing if it yields a better analytic estimate for that complete observable, not merely another expression for its invariance.

## What belongs in the book

Promote a result when there is a coherent analytic proof with a substantive role: a useful canonical estimate, its necessary transfer, and a stated mathematical consequence or an independently significant intermediate theorem. The proof must explain where actual theta data improve what generic heat geometry supplies, retain all necessary errors and coverage, and survive the relevant [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md). Controls with different invariant values do not disprove a theorem that quantitatively uses the complete theta data; shared formal conservation laws do not distinguish theta by themselves.

The book should present the successful argument selectively. Keep exploratory alternatives, failed comparisons, lengthy diagnostic calculations and detailed audit records in the notes and reviews. If a stronger mechanism replaces H dz, revise the program and manuscript around it. The initial inclusion in main.tex was a provisional exposition checkpoint. The author-directed book rewrite now completes SCF-04 only as an intermediate theorem-centered manuscript milestone; the multiplicity-sensitive analytic objective and SCF-03 remain open. The author has also authorized dated standalone book TeX files alongside Git history for convenient preservation of rewrites, without new snapshot folders. See the [manuscript guide](../../manuscript/README.md).

## Supporting calculations and continuation

Numerics may check an algebraic sign, test a proposed inequality against a control, or certify a finite constant needed by an identified proof. They must name the analytic claim they support and the outcome that would force its revision. A height scan, fitted width, statistical picture or successful finite computation does not establish the uniform analytic estimate. No numerical campaign is a goal of this overview.

Likewise, stochastic averaging is a possible analytic question about the deterministic field along an adaptive contour. A covariance or cancellation estimate must be proved in the relevant ensemble before it is used; zero mean alone does not bound accumulated displacement. Add smoothing only if an identified analytic instability warrants it and the altered balance is included in the proof.

Continue from the [book revision and research handoff](../notes/20_THEOREM_CENTERED_BOOK_REVISION_20261023.md), retaining [Note 19](../notes/19_CONTINUATION_AFTER_FIXED_OFFSET_THEOREM_20261023.md) and the completed theorem in [Note 18](../notes/18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md) as its analytical sources. Save analytic derivations in `notes/`, assessments in `reviews/`, and only necessary supporting computations in `numerics/`. Add relevant articles to the [reference collection](../../references/README.md), following the root [reference workflow](../../../../../REFERENCE_WORKFLOW.md). The preceding conservation chat remains history 0007; this proof round has its own history 0008. History 0007’s earlier [verification receipt](../chat-histories/VERIFICATION_SPATIAL_CONSERVATION_20261023.json) records a point-in-time integrity check.
