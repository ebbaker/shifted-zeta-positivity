# Wilson–Loewner after the WZW and N4SYM reviews: highest-value next steps

**Status correction, 24 September 2026:** the append proposed in Section 5A was already completed in the [critical-path operator-coupling certificate](../../critical-path/notes/CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md), with an internal all-input bound below 0.951 and specialist review outstanding. This assessment overlooked that later result. The recommendation to perform the same append in Sections 5A, 6, and 7 is superseded by the [arithmetic-storage program](../arithmetic-storage/notes/ARITHMETIC_STORAGE_PROGRAM_AND_GOALS_20260924.md): audit and extend the existing method toward the first prime, while studying the Sonin remainder independently. The original assessment is retained below to preserve its history.

24 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity). **Reasoning effort:** not exposed; not inferred.  
**Baseline:** `6a6e2b9e40fd01f142264071c95d41cfeed9d814`.  
**Status:** comparative research assessment, primary-source checks, one replay of an existing diagnostic, and elementary operator bookkeeping. This is not a specialist proof review, a new positivity certificate, or a physical realization. Recommendations below are judgments about research value, not probability estimates for proving RH.

## 1. Recommendation

The new WZW review and the N4SYM assessment largely agree on the strategic question: the next arithmetic advance is unlikely to come from another match of a spectrum, another finite collection of passive modes, or a more elaborate calculation in an already unsuccessful physical channel. The central work is to relate the **complete arithmetic response to a positive state norm**, including the mixed terms that appear when memory crosses a window boundary or a prime place is adjoined.

The highest-value program has two complementary parts:

1. **Cumulative transfer continuation:** use the existing all-input anchor to test a rigorous normalized append estimate, then address the first-prime interference in the complete transfer.
2. **Arithmetic form realization:** revisit the actual first-prime semilocal comparison, including its compressed metric and signed remainder, rather than rebuilding a positive Sonin space or restarting its normalization calculation.

A focused Suzuki comparison should identify whether canonical systems supply a genuinely new estimate for either part. N4SYM and global modular deformations remain exploratory physical directions, to be reopened only around a specified missing mechanism. The native YM/Loewner hierarchy remains a legitimate separate physics question.

I would **park the tested WZW transfer constructions without declaring a universal closure of WZW, field-dependent Loewner observables, or automorphic scattering**. I would also not spend the next research session reorganizing folders or reconstructing an old manuscript: the latter has been located intact, and neither task addresses the mathematical obstruction.

## 2. What the new WZW review contributes, and what needs correction

The principal new item is [Claude's 24 September program assessment](../WZW/reviews/review_claude_wzw_program_assessment_20260924.md), added with an exact/floating diagnostic at the baseline commit. I compared it with the earlier collar, interface and thermal-load audits, the N4SYM assessment, the original exclusion notes, and later qualifications elsewhere in the project.

### Findings worth retaining

- **The pilot is a sound bounded calculation.** Its exact finite algebra and the distinction between tensor and gluing pairings survive the new review. I replayed its accompanying review program: 40/40 controls passed, including 24 exact rational controls. This does not revalidate every BCFT or continuum assertion.
- **The fermion/even-tower dictionary is useful.** For positive u,
  \[
  G_s(u)=\frac1{2\sinh(u/2)},\qquad
  G_o(u)=\frac1{2\cosh(u/2)},\qquad
  \frac{G_s+G_o}{2}=\frac{e^{-u/2}}{1-e^{-2u}}=n_\Gamma(u).
  \]
  It corrects an overly restrictive single-tower spacing comparison and connects the SU(2) level-2 fermion sector to the [earlier even-tower analysis](../../wilson-lines/notes/REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md). It matches the separated gamma tower, not the renormalized contact, poles, prime terms, or a complete positive physical readout. A sum of spin-structure expressions still needs an actual preparation, projection and adjoint if used as a norm.
- **The thermal coefficient identity has a clear antecedent.** The identity
  \[
  c_n(\omega)=J_{2\omega}(n)/n^{\omega+1/2}
  \]
  links the Bost–Connes calculation to [fractional dimension](../../fractional-dimension/README.md). The positive KMS interpretation is the additional result; the arithmetic coefficient formula itself was already present. This calls for cross-referencing, not another coefficient-fitting program.
- **The existing regular-load exclusions remain actionable.** The [finite-place interface audit](../WZW/reviews/review_codex_finite_place_interface_20260923.md) and [thermal front audit](../WZW/reviews/review_codex_thermal_boundary_structure_20260923.md) justify parking those particular architectures. More modes with finite total response spectral mass do not resolve their front mismatch.

### Qualifications that change the research conclusions

| Review claim or recommendation | Assessment in the broader record |
|---|---|
| Reflection positivity should target the Weil form rather than a nonlocal causal transfer. | Correct as a distinction, but not an exclusive choice. Reflection may also construct the **cumulative defect**. The parent already proposed this explicitly. A reflected transfer, a reflected form and reflected storage are three different objects. |
| Positivity of the shifted form is equivalent to contractivity of the transfer. | Do not use this as a fixed-(omega,L) equivalence. The integrated identity in Section 3 is the correct link. Instantaneous positivity is sufficient along a path, and stronger than the cumulative property sought. |
| The far-field theorem closes Loewner arithmetic constructions. | It closes the specified translation-invariant map-induced transport, not arbitrary field-dependent Wilson observables. The [19 September opening note](OPENING_NOTE_20260919.md) already explains this scope and corrects the earlier Bessel-clock argument. The review does not incorporate that qualification. |
| Horocycle dimension excludes all deformations that remain scattering matrices. | The standard scalar Eisenstein identification has a fixed offset. The cited sibling note explicitly labels its extension beyond the written modular example a **reading**. It is not a proved classification of arbitrary operators, fields, boundary conditions or multichannel scattering. Require an explicit way around the fixed-offset mechanism; do not promote it to a universal no-go theorem. |
| Nothing in the branch derives log(n) delays. | Too broad. The [modular Hodge benchmark](../WZW/notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) contains native arithmetic weights at half shift; the controlled thermal loops also have real logarithmic flight lengths, although their geometry was supplied as a model assumption and their amplitudes fail. The unsolved task is the **complete variable-shift family with the correct norm**. |
| The spectrum condition is the only mechanism that could supply the required innerness. | Too strong. Positive energy provides analytic tools, but causality/analyticity do not establish an ordinary-norm Schur bound. Independent passive state-space or canonical-system constructions are also possible mechanisms. The physical norm and energy balance must still be derived. |
| The quarter-shift survey closes noncompact WZW possibilities. | It is a useful filter for the **surveyed amplitudes and allowed dictionaries**. Its own discussion contains qualifications and corrected rigidity claims. It does not classify all observables or deformations of those theories. Repeating a failed amplitude is low value; a different observable would need a fresh, explicit rationale. |
| Unique-KMS symmetry behavior and the finite-Euler pole imply an adelic realization is compulsory from the start. | They motivate joint archimedean/arithmetic constructions, but do not establish uniqueness of that architecture. The coefficient probabilities remain meaningful in the unique-KMS range. Finite-window identities remain legitimate even when the same finite Euler product is not a globally passive transfer. |

These qualifications do not make the parked candidates promising. They make the reasons for parking them accurate and specify what a genuinely different proposal would have to change.

## 3. Keep the three positivity targets distinct

Use the parent's notation
\[
Q_{\omega,L}[g]=\operatorname{Re}\langle g,G_{\omega,L}g\rangle,
\qquad D_{\omega,L}=I-V_{\omega,L}^{*}V_{\omega,L}.
\]
On the stated smooth domain, the [prescribed shift-flow note](SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md) gives
\[
\langle f,D_{\omega,L}f\rangle
=2\int_0^\omega Q_{s,L}[V_{s,L}f]\,ds,
\qquad
Q_{0,L}[f]=\lim_{\omega\downarrow0}
\frac{\langle f,D_{\omega,L}f\rangle}{2\omega}.
\]

There are therefore three legitimate construction targets:

1. **Central form:** an independently positive pairing equal to the complete Q at zero shift on its test domain.
2. **Cumulative storage:** independently defined amplitudes B with D = B*B and the ordinary input/output norms.
3. **Transfer:** an independently defined channel equal to V, whose energy balance then establishes contractivity.

A self-adjoint causal scalar operator is multiplication, so a nonlocal reflected compression cannot itself be V. This theorem does not exclude a reflected construction of Q or D. Conversely, self-adjointness alone makes neither Q nor D positive, and a positive Gram kernel needs an exact identification including contacts and poles.

Analyticity is also insufficient: the causal stable scalar response 2/(p+1) is analytic in the right half-plane but has gain greater than one near zero frequency. In a physical proposal the missing condition is a correctly normalized passive energy identity, not merely an analytic susceptibility. The N4SYM finite-mass calculation is a useful demonstration of how to obtain such an identity from internal states, but its force/velocity work norm has not been identified with the arithmetic signal norm.

## 4. The Sonin comparison: useful, but not a new starting point

### What the published base case actually supplies

Connes–Consani's [archimedean paper, Theorem 1](https://arxiv.org/html/2006.13771v1) gives positive Sonin-trace dominance for multiplicative test functions supported in [2^(-1/2),2^(1/2)] with transform vanishing at i/2 and 0 in the introduction's convention. Without the zero-frequency condition, the comparison retains a negative rank-one correction. The logarithmic source interval has width log(2). These hypotheses cannot simply be dropped when importing the theorem into an unrestricted finite-window transfer problem. The paper also explains why prescribed transform zeros are compatible with a global RH criterion; that is different from a same-window all-input norm bound.

The repository had already recorded this distinction in [inverse-bulk outlook, the discussion of Connes–Consani](../../previous/inverse-bulk-realization/sections/08_outlook.tex), alongside its reading of Yoshida's unrestricted prime-free result. For the operational all-input starting point here, use the project's own [certified EMA anchor](../../critical-path/notes/EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md), rather than silently identifying these different statements.

The [semilocal Sonin stability theorem](https://arxiv.org/html/2310.18423v1), Theorem 4.13 and Section 4.8, transports the spaces by a bounded invertible map; the inner product depends on the places. It is not an isometric inclusion supplying monotone norm domination. [Quasi-inner functions and local factors](https://arxiv.org/abs/2008.10974) likewise concerns a compact off-diagonal Hardy-space block, not its vanishing or the innerness of the required shifted quotient.

### What was already calculated locally

The [14 September canonical semilocal comparison](/Users/ebbaker/.codex/.chatgpt-projects/g-p-6a90684bbcb881918a5a1f5740bfbc65/output/semilocal-pairing-comparison-20260914/COMPARISON.md) survives in local project material outside the repository. Its existence and subsequent change of direction are recorded in the repository's [brainstorm assessment](../../../brainstorm/ASSESSMENT.md). It is an internally checked calculation, not an independently certified theorem; its actual Sonin trace was not numerically evaluated. Its essential formulas make the next task substantially more specific.

Let Pi be the archimedean Sonin projection, a = log(2), r = 1/sqrt(2), and U_a the unitary translation on the whole logarithmic scaling line. For adjoining place 2, put
\[
M_2=I-rU_a,\quad G_2=M_2^*M_2,
\quad A_2=\left.\Pi G_2\Pi\right|_{\operatorname{Ran}\Pi}.
\]
The actual orthogonal projection onto M_2 Ran(Pi) is
\[
\Pi_2=M_2\Pi A_2^{-1}\Pi M_2^*.
\]
The metric inverse is essential. For smooth scaling preparation F, with convolution operator C_F and \(K_F=C_F^*C_F\), the positive smoothed pairing is
\[
\mathcal B_2[F]=\|C_F\Pi_2\|_{\mathrm{HS}}^2.
\]
The comparison records
\[
Q_L[F]=\mathcal B_2[F]+P_L^{\rm pole}[F]
-\mathcal E_\infty[F]-\Delta_2[F]
-\frac{\log2}{\sqrt2}\langle F,(U_a+U_{-a})F\rangle
\]
for log(2) < L < log(3), with the full contact inside the archimedean term. The extra coupling is
\[
\Delta_2[F]=\operatorname{Tr}_{\operatorname{Ran}\Pi}
\left(A_2^{-1}\Pi G_2(I-\Pi)K_F\Pi\right).
\]
It has no sign supplied by positivity of G_2. The earlier note gives a convergent inverse expansion, but its trace-ideal estimates and the approximation of the actual Pi still need to be controlled for a rigorous numerical evaluation. It also derives that the one-prime small-cutoff Fourier operator is compact but not Hilbert–Schmidt, obstructing a direct copy of the unweighted archimedean square-trace argument.

Thus **the next semilocal result should concern this residual or a demonstrably different preparation that improves it**. Reproving positivity of the metric, writing another Gram completion, or asserting stability under adjoining places would repeat completed groundwork. A failure of this particular comparison would also be informative if it identifies what arithmetic relation the preparation misses.

## 5. Two concrete calculations that make the priorities reviewable

### A. Carry memory across an append

The [critical-path handoff](../../critical-path/notes/RESEARCH_CONTINUATION_AFTER_EMA_ANCHOR_20260920.md) already specifies
\[
L=\tfrac12,\quad h=\tfrac1{20},\quad\omega=10^{-3},\qquad
V_{\omega,L+h}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix}.
\]
With strictly positive diagonal defects, contraction reduces by the Schur complement to
\[
\left\|(I-ZZ^*)^{-1/2}Y(I-X^*X)^{-1/2}\right\|\le1.
\]

The important unknown is the normalized mixed block Y. The EMA memories and pole states must pass across the join; resetting them manufactures a different system. The existing anchor controls all inputs, but its scalar lower bound may lose too much after normalization. Measure that loss before increasing numerical dimension.

**Deliverable:** an all-input enclosure for this mixed block, or a quantified obstruction in the proposed bound, with endpoint and complementary-input control. Certifying the larger central form by an unrelated method is a useful control, not a solution of this continuation problem. This is a method test within known positive windows, not a new depth record. One successful append does not establish iteration to unbounded depth.

### B. Isolate the first-prime interference in the actual transfer

Write K_omega = A_omega Z_omega with A_omega the **complete gamma/rational factor**, and let T_omega,L be its causal finite-window convolution operator. Let S_a be the truncated delay on L2(0,L). On log(2) < L < log(3), causality and the Euler expansion give exactly
\[
V_{\omega,L}=T_{\omega,L}+c_2(\omega)S_aT_{\omega,L},
\qquad c_2(\omega)=\frac{2^\omega-2^{-\omega}}{\sqrt2}.
\]
Expanding the adjoint product yields the elementary identity
\[
\begin{aligned}
D_{\omega,L}={}&I-T^*T
-c_2T^*(S_a+S_a^*)T
-c_2^2T^*S_a^*S_aT.
\end{aligned}
\]
The first-prime cross term is sign-indefinite, and the delayed-output square is subtracted. The missing result is a state interpretation or inequality for the **combination**, not positivity of each piece. This finite-window identity does not assert global passivity of a gamma factor times a finite Euler product.

This calculation and the semilocal form comparison are related questions, not identical formulas: one concerns finite-shift output interference; the other concerns the central form and a changing Sonin projection. Comparing them requires the shift-limit/domain identity of Section 3 and retention of both pole directions. An explicit map between their state variables would be a high-value result; merely renaming their positive operators would not.

**Deliverable:** either an independently defined storage identity for the displayed defect, or a rigorous comparison identifying which signed coupling remains. A few positive eigenvalues or an arbitrary square root of the desired deficit do not meet this criterion.

## 6. Portfolio ranking and stopping criteria

Impact denotes progress toward all-input positivity at arbitrarily large support, or a physical construction explaining it. Feasibility refers to the next bounded task, not to eventual completion of the RH program.

| Direction | Impact / near-term feasibility | Recommendation and condition for further investment |
|---|---|---|
| Normalized cumulative append from the existing anchor | **High methodological impact; comparatively concrete** | First computational/analytic task. Obtain a genuine mixed-block bound with all input complements, or identify the precise estimate that fails. Promote only if the state structure or bound has a plausible iteration mechanism. |
| Complete first-prime transfer storage | **Very high direct relevance; difficult** | Main arithmetic objective after the append calibration, or an independent analytic route. Work on the full mixed terms above; do not optimize another scalar passive filter. |
| Actual semilocal first-prime residual | **High structural payoff; difficult but well specified** | Re-audit the existing comparison and evaluate/bound the actual projection coupling on a declared input family, with honest tails. Then seek a bound on the negative residual relative to the positive pairing. Do not require the residual itself to be everywhere nonnegative if a weaker domination suffices. |
| Suzuki canonical-system comparison | **High potential, uncertain added value** | Identify the exact kernel, determinant/invertibility and Hamiltonian-positivity obligations in the small-shift range. Compare those with the two preceding residuals. If it only restates the same unresolved sign, retain it as organization rather than a separate main project. |
| Global modular or arithmetic bulk deformation | **High conditional upside; low present readiness** | Retain as the strongest physical benchmark with arithmetic already built in. Specify one interaction outside the tested fixed-core/load/clock classes; derive its domain, energy, variable front and fixed-delay action before detailed fitting. A changed formal dimension or an infinite mode count is not a mechanism. |
| N4SYM non-protected response or new defect background | **Moderate physical value; low current arithmetic return** | One bounded feasibility task only. Explain the fixed-theory parameter, physical time, stationarity and norm. A driven rotating source may supply pump energy and a two-time response; a scale-free cusp alone need not supply a length scale. |
| N4SYM quartic kernel, corner corrections, YM hierarchy closure | **Potentially substantial physics value; low direct arithmetic impact** | Continue when the physical objective is explicit or a named realization requires the calculation. They do not yet explain prime weights or the arithmetic signal norm. |
| More WZW levels, blocks, regular thermal loads, or repeated coefficient matching | **Low in the tested architectures** | Park. Reopen only with a distinct preparation/readout or coupling that addresses a demonstrated obstruction. |
| Folder migration, reconstructed manuscripts, or new snapshots | **Low mathematical value** | Navigation/provenance repairs should be small. Follow the current no-new-snapshots policy. No reconstruction is required for the recovered WZW version. |

The [thermal continuation](../WZW/notes/CONTINUATION_AFTER_THERMAL_INTERFACE_TESTS_20260923.md) and [N4SYM assessment](../N4SYM/reviews/PROGRAM_ASSESSMENT_CODEX_20260924.md) already favor storage/canonical directions. This note sharpens that agreement in two ways: begin cumulative continuation from its existing all-input anchor rather than another sampled pilot, and begin semilocal work from its existing residual rather than a generic positivity theorem.

Suzuki's [primary construction](https://arxiv.org/abs/1204.1827) is explicit and unconditional for omega > 1; it does not supply the needed small-shift extension. That restriction must remain visible in any comparison. The N4SYM assessment also identifies prior literature for nonlinear dilaton localization, so that item begins with reconciliation, not a new discovery program.

## 7. Practical sequence

**First, a bounded consolidation pass.** Cross-link the fermion/Jordan identities, record the precise scope of each parked architecture, and distinguish Q, D and V in new tasks. Reconcile the N4SYM dilaton claim with the literature. Preserve the historical notes rather than rewriting them into broader no-go statements.

**Then give the next substantive session to the normalized append.** Use the specified L = 1/2 to 11/20 test and carry the existing state realization across the join. Report the bound, its weak directions, and whether its loss can be controlled under repetition. Avoid calling an isolated successful certificate a new horizon.

**Maintain the semilocal comparison as a separate structural task.** Its first deliverable is a checked, quantitatively usable version of the actual Pi-dependent first-prime residual, including contact and pole normalization. It does not have to wait for the append calculation to succeed. A candidate inequality must distinguish the arithmetic measure from the project's negative smooth-density control.

**Use the first-prime defect as the shared benchmark.** Once either approach produces a nontrivial estimate or state map, test it on the full first-prime interference. Later, repetition and mixed-prime checks at 4, 3 and 6 discriminate a mechanism from a single-echo coincidence. Support cutoffs must include every intervening integer label; a two-prime model is not automatically a full window through log(6).

**Run the canonical-system audit only against a precise missing estimate.** Ask whether its explicit arithmetic kernel gives new control over that estimate. This keeps the literature comparison focused and avoids cycling between equivalent formulations of the unresolved positivity.

## 8. Provenance, review scope and preservation

The WZW assessment's call for new dated snapshots conflicts with the author's current instruction: manuscript milestones belong in a concise history file pointing to commits/tags; new snapshot folders are deprecated. A repository history gap is worth documenting, but historical practice does not override that instruction.

The earlier WZW source and PDF are present in the [local 23 September package](/Users/ebbaker/.codex/.chatgpt-projects/g-p-6a90684bbcb881918a5a1f5740bfbc65/output/wzw-manuscript-20260923/WZW/manuscript.tex). The PDF SHA-256 is `904bb620fdaebf686a6e19789042cebf8150a46ac7356d210e5a8c99443cec4a`, exactly the historical value recorded in the live WZW build record. It may be absent from the reviewed Git tree, but it is recoverable without reconstruction. No new copy, snapshot, folder migration or manuscript revision was made here.

The semilocal comparison cited above is local working material outside Git, with SHA-256 `6c1d50c6b53e8f261efcb3d49e43dfa8e8affcb16e816964f054825487b3e12c`. The essential formulas and qualifications have been included here so the recommendation does not depend on access to that machine-specific path. Reuse of that calculation should start with a technical audit, not with an assumption of independent validation.

The fresh replay of `WZW/numerics/check_wzw_program_review.py` passed 40/40 controls, 24 exact. Its source hash agrees with the review. No new large numerical experiment was run, and the previous N4SYM replay is not counted as fresh work in this note. The [compact provenance record](../numerics/records/cross-program-assessment-20260924.json) identifies the review, replay and recovered artifacts. The first-prime defect formula is a direct adjoint-product expansion; the priority rankings and broader implications are assessment. Neither supplies a new sign theorem.
