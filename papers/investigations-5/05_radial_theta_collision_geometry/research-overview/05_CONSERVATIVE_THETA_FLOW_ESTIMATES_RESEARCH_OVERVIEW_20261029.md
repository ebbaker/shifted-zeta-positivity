# Research overview for conservative theta flow estimates

29 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Prepared in the existing Investigation06 chat0004, **List modified evolution equations**; [conversation provenance][history] retains its unique registration.

Resume Investigation05's conservative feedback flow and seek an estimate from the complete theta source that controls its collision-driven concentration. The immediate opportunity is a coupled estimate for the gradient, actual spectral derivatives, and source-relation residual. A useful first result may be a bounded improvement in one of these quantities, with its consequence and remaining gap stated explicitly.

The author selected this return after the [auxiliary-flow comparisons][comparison] in Investigation06. Those comparisons help prioritize the next attempt within the tested families. They establish neither general superiority nor historical novelty of the conservative construction. The present task is an author-requested research plan; the mathematical returns retain their existing evidence status.

This overview supersedes [Overview04][old-overview] for current priorities. **[Progress05][progress] is the sole current register.** Existing CTF task identities are retained. CTF-B02 remains partial after two completed bounded returns; its next round, R3, is ready for conceptual work and has not started. [Continuation32][continuation] remains the detailed source-residual handoff.

## Task routing before research begins

Follow [GPT_RESEARCH_MODEL_WORKFLOW][workflow]. **B** means an unresolved conceptual choice or proof strategy; **E** means work whose route and completion test are specified. Recommendations do not change the author's selected model or effort. Edward Baker chooses the actual model, effort, chat, and when to begin.

| Task | Type and recommended model | Readiness and dependency | Bounded output |
| --- | --- | --- | --- |
| **CTF-B02 R3** | **B — Astra:** a useful coupled functional and signed estimating argument remain to be found | Ready from Notes28–32; default next research task | One admissible functional and one coupled estimate attempt, returning a proved advance, a tractable execution contract, or one precise unresolved inequality |
| **CTF-E06** | **E — Sol:** the manuscript starting point and editorial scope are fixed below | Ready as a separate editorial task; not a prerequisite for B02 | One bounded cleanup pass on the existing flow manuscript, with minimal companion-book attribution/navigation corrections |
| **CTF-E07** | **E — Sol:** routine analytical completion after the route is fixed | Gated on a versioned B02 contract | The specified identities or lemma, with domains, residuals, and error terms checked |
| **CTF-E03** | **E — Sol:** rigorous finite acquisition for a stated estimate | Optional and gated on named quantities actually consumed by B02/E07 | One frozen finite calculation or certificate with complete errors and a stopping limit |
| **CTF-E08** | **E — Sol:** assess one frozen return and integrate supported conclusions | Gated on one completed B02/E07 return and any required E03 evidence | One scoped assessment and a proportionate update of the existing text and research navigation |
| **CTF-B03** | **B — Astra:** extension and threshold transfer require a new conceptual decision | Gated on an assessed substantive canonical gain | One time, height, or threshold-transfer question with its remaining coverage obligations |
| **CTF-E02 R1** | **E — Sol:** arithmetic propagation of already saved data | Existing optional packet; lower priority and unchanged | The known initializer-payment gap audit, with zero new source integration or PDE evolution |

Creating these documents completes no B or E research task. Ordinary inspection, navigation, and chat capture are housekeeping available to the current model. The contracts below separate proof design from its later routine execution.

## The fixed starting construction

Use the original physical normalization and complete source:
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
Newman time is \(t\); auxiliary time is \(s\). With \(r=|X|=e^{2u}\), the initial full signed density is
\[
j_0(t,z;X)=\mathbf1_{r\ge1}
\frac{e^{tu^2}\Phi(u)}{8\pi r^3}\cos(zu).
\]
The change of variables is part of the definition:
\[
4\pi r^2\,dr/(8\pi r^3)=dr/(2r)=du,
\qquad \int_{\mathbb R^3}j_0\,dX=H(t,z).
\]
The density is zero for \(r<1\); the exterior \(r\ge1\) encodes \(u\ge0\). Spatial heat redistributes this density while preserving its complete integral. The initially empty unit ball belongs to the evolved domain. The subscript zero denotes \(s=0\), while Newman time remains free. [Note25][n25] supplies the heat baseline and physical-jet accounting.

For the [Note28][n28] feedback, keep a physical mark \(p=(T,a)\) fixed and prepare the full parameter family by one unit of heat smoothing, \(j^p(0,t,z)=K_1*j_0(t,z)\). Let
\[
U=j^p(s,T,a),\qquad V=\left.\partial_zj^p(s,T,z)\right|_{z=a},\qquad W=(U,V).
\]
The same propagator acts on both components and on the running parameter family. Its equation is
\[
W_s=\Delta W+\alpha(s)\operatorname{div}(vW),\qquad
v(X)=X+\frac{X}{1+|X|^2},
\]
\[
G=\int|\nabla W|^2,\qquad
D=\int(\operatorname{div}v)|W|^2,\qquad
\alpha=2G/D,\qquad E=\int|W|^2=E_0>0.
\]
All spatial integrals are over R^3. The mark is held fixed when taking running spectral derivatives; derivatives of the mark itself have the additional response terms in Note28. The conserved vector mass is m=(H(T,a),H_z(T,a)).

In the stated prepared Schwartz/moment class, a first-jet zero forces finite breakdown:
\[
m=0\ \Longrightarrow\ S_{\max}\le S_*=
\frac{60}{7(5\pi^2)^{2/5}}\frac{P^{4/5}}{E_0^{2/5}},
\qquad P=\int |X|\,|W_0(X)|\,dX.
\]
No nondegeneracy of the physical double event is needed for this implication. Global regularity is already classified as a reformulation of pointwise noncollision. A separating advance would be an independently proved theta bound preventing breakdown through a paid deadline; repeating that equivalence is not a new estimate.

## Established results and the remaining estimate

| Source | Established contribution | Limit to retain |
| --- | --- | --- |
| [Note25][n25] and [Note27][n27] | Conserved-density heat, loss of leading diffusion modes at collision, and a completed floating baseline measurement | Generic diagnostic; no measured advantage over direct acquisition in the tested comparison |
| [Note28][n28] and [Review16][r16] | Energy-normalized feedback, local construction, continuation criterion, and explicit collision deadline | Same-assistant analytical checks; the fixed generic initializer payments cannot reach their paid deadline |
| [Note29][n29] and [Review17][r17] | Positive carrier, sharp mass–energy–moment inequality, and quantitative regularity from a physical first-jet margin | The comparison does not acquire that margin or enlarge the previously separated domain |
| [Note31][n31] and [Review18][r18] | Actual-theta preparation defect, forced residual evolution, sphere cancellation, and origin-domain obstruction for the uncut operator | The fixed zero-residual substitution fails; coupled estimates retaining the residual remain open |
| Investigation06 [R1][r1] and [R2][r2] | Scoped failures of the tested normalized source responses and two algebraic relative-recovery comparisons | These tests do not exclude all auxiliary flows or prove the conservative flow superior |

The exact gradient consumer is
\[
G'=-2\|\Delta W\|_2^2+\frac{2G}{D}\mathcal K,
\]
where Note31 equation (21) gives the full drift-production expression \(\mathcal K\). The intended advance is a justified use of the negative diffusion term together with additional signed source information.

For the fixed source operator, write \(\rho_T=e^{Tu^2}\Phi(u)/(8\pi r^3)\) on the exterior and
\[
\mathcal A_T=r\log r\bigl(\partial_r-\partial_r\log\rho_T\bigr),
\quad \mathcal R=\mathcal A_TW-(aV,V+aJ_2),
\]
where J_2 is the actual second running spectral derivative. Use Note31's smooth whole-space extension of this operator. Its residual satisfies
\[
\mathcal R_s=L_s\mathcal R+[\mathcal A_T,L_s]W,
\qquad L_s=\Delta+\alpha\operatorname{div}(v\,\cdot).
\]
The preparation residual is nonzero for actual theta data on the proved interval. The commutator contains second spatial derivatives. At r=1 the combination (aV,V+aJ_2)+R cancels; separately estimating its singular quotients loses a cancellation required for finiteness. The inner-ball energy and the extension's coefficient terms also remain. No finite closed derivative hierarchy has yet been established.

## The next conceptual round

**CTF-B02 R3 — B, Astra.** Start with the fixed flow, complete source, preparation, and physical observation above. The unresolved choice is an admissible coupled functional and a plausible way to estimate its production. Discovering that choice is the work; the author need not supply the missing theorem in advance.

Take one marked point or one explicitly stated compact rectangle inside \(0\le T\le1/2\) and \(0<a_-\le a\le a_+<\infty\). Specify the proposed domain and functional before testing its estimate. In this round attempt **one** coupled functional or one named supporting lemma. Retain the actual spectral jets, nonzero residual, full commutator, unit-sphere cancellation, and origin-admissible whole-space domain. Identify which property of the complete theta source enters the proposed signed bound.

The return must explain the implication for G, alpha, or an explicitly quantified part of their control, and compare it with the same direct source information. A bounded residual estimate or improved production bound is a valid intermediate result when its gain and remaining transfer obligation are clear. An independently known lower bound for |m| may be used for comparison, but it cannot be presented as a newly acquired collision restriction.

Complete the round with one of: a proved bounded advance; a fixed analytical route for E07; or one precise failed or unresolved inequality. A failure retains its tested class. Stop at that result. A different PDE, source relation, observable, or second candidate requires a recorded B02 revision before it is tested. No numerical search or automatic enlargement follows from an inconclusive estimate.

## Execution contracts and conceptual return boundaries

**CTF-E06 — E, Sol, manuscript cleanup.** The main working text is [Conservative Theta Flows and Collision Amplification][manuscript]. Its existing Sections 3–7 already contain conservation, feedback, carrier, residual, and the open estimate; [Note34][n34] records the prior refocus. Reuse that source and its proofs. Make one editorial pass that clarifies the spatial density and Jacobian, keeps the two times and fixed mark distinct, states the remaining estimate early, and repairs any stale routing or unsupported novelty wording. Keep the author field and LLM acknowledgment.

The separate [book companion][book] is background for transform and cylinder formulations. [Note35][n35] identifies its scalar Mellin identity as classical. Correct that attribution in the companion where needed and link the current flow program; a full book rewrite or merger is outside this pass. Preserve useful source derivations without requiring the research to pass through their alternative notation. Geometric or notational changes that alter the evolved field, invariant, or proof need a B02 decision. A short change note, resolved references, and successful built-in compilation of each edited TeX source complete E06. Keep any generated PDF in the repository output directory and report the actual layout-check scope. E06 is independent of B02 and is not a prerequisite for beginning the estimate.

**CTF-E07 — E, Sol, fixed analytical completion.** Begin only when B02 supplies a versioned list of identities or lemmas, hypotheses, domain, proposed method, and acceptance condition. Complete exactly that list with all boundary, residual, and higher-derivative terms. Routine algebra and domination arguments are permitted. A new proof strategy or functional returns to B02; a failed premise is an acceptable scoped return. No PDE simulation is included by default.

**CTF-E03 — E, Sol, finite rigorous acquisition.** Preserve its original purpose. Before execution, the issued packet must specify the quantities consumed by the proof, finite cases, source cutoffs, quadrature or exact method, precision/refinement limits, total work cap, and stopping criterion. Retain source, arithmetic, integration, propagation, and tail errors. A certificate must replay and reject a deliberately altered input. If the estimate is analytical, no numerical stage is required. A changed estimate or domain returns to B02.

**CTF-E08 — E, Sol, assessment and integration of one return.** Check one frozen B02/E07 result and any required E03 evidence against its actual claim, controls, and source versions. Recompute only its stated checks within their limits. Record same-assistant, same-model, cross-model, and specialist-review status accurately; changing models alone supplies no specialist independence. Integrate only supported conclusions into the existing text and navigation, and compile edited TeX. A new scientific interpretation returns to B02; do not turn review into another candidate search. Apply the repository's inclusion rules before updating result or avoid summaries. This new task does not reopen the completed historical E04/E05 integrations.

**CTF-B03 — B, Astra, later coverage.** After an assessed substantive canonical gain, choose one extension in physical time, height, or threshold transfer. State the relevant reduction and its hypotheses before claiming a global consequence. The fixed feedback theorem already detects any simultaneous first-jet zero in its admitted class; domain coverage and a global threshold implication remain separate obligations.

## Controls and evidence

Read the [result index][results] and [avoid index][avoid], especially [collision controls][controls], [target classification][a01], [coordinate reformulations][a03], [scoped failures][a07], [numerical scope][a10], and [useful gain before expansion][a20].

The immediate control is
\[
\Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2},\quad T_c=1/4,
\quad H_*(T_c,z)=\frac{\sqrt\pi}{16}(z^2/4-6)^2e^{-z^2/16}.
\]
It collides at a=2sqrt(6), satisfies the generic prepared feedback hypotheses on its moment domain, and breaks down by its own deadline. It fails the literal canonical source premise; that distinction must actually be used by any excluding estimate. A generic diagnostic or intermediate identity should still behave correctly on this control. For other premises, use the registered weighted-square, finite-prime, reflected/primitive, and Euler-factor controls with their actual domains and witness locations. Do not assign every control the same failed premise.

New work belongs in notes, numerics, and reviews with actual model and effort. Retain failed evidence and complete source terms. The comparison record in Investigation06 remains there; the existing chat0004 history is linked rather than copied or relocated. Future milestones use commits or tags when available and concise entries in DRAFT_HISTORY.md, with no new manuscript snapshot folders.

## Continuation prompt

> Continue [B] CTF-B02 R3 in Investigation05 from Overview05, Progress05, Notes28–32, and the Investigation06 comparison summary. Follow GPT_RESEARCH_MODEL_WORKFLOW. Keep the conservative feedback equation, complete theta source, unit heat preparation, and actual marked spectral derivatives. Choose one origin-admissible coupled functional or supporting lemma that could improve gradient or residual control on a stated bounded physical domain. Retain the source residual, full commutator, sphere cancellation, and inner-ball energy. Explain the canonical input, the control outcome, and the implication for the existing gradient balance. Return a bounded advance, a fixed E07 contract for Sol, or one precise unresolved inequality. Keep manuscript cleanup in E06; issue numerics only for quantities a specified estimate consumes. Save the result and update Progress05 with actual model, effort, evidence status, and the next B/E task.

[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[old-overview]: 04_CONSERVATIVE_THETA_FLOW_RESEARCH_OVERVIEW_20261028.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[continuation]: ../notes/32_SOURCE_RELATION_COMMUTATOR_CONTINUATION_20261028.md
[n25]: ../notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[n27]: ../notes/27_CONSERVATIVE_HEAT_BASELINE_E01_RETURN_20261028.md
[n28]: ../notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: ../notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n31]: ../notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n34]: ../notes/34_CTF_E05_MANUSCRIPT_REFOCUS_RETURN_R1_20261028.md
[n35]: ../notes/35_CLASSICAL_THETA_MELLIN_ATTRIBUTION_20261028.md
[r16]: ../reviews/16_CONSERVATIVE_FEEDBACK_MAGNIFIER_B01_ASSESSMENT_20261028.md
[r17]: ../reviews/17_POSITIVE_CARRIER_AND_REGULARITY_B02_ASSESSMENT_20261028.md
[r18]: ../reviews/18_CANONICAL_SOURCE_RELATION_PROPAGATION_ASSESSMENT_20261028.md
[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[book]: ../book/main.tex
[comparison]: ../../06_auxiliary_collision_flows/notes/06_APPROACH_SUMMARY_AND_GOALS_FOR_NEXT_BRAINSTORM_20261029.md
[r1]: ../../06_auxiliary_collision_flows/notes/02_COSINE_QUARTIC_RESPONSE_COMPARISON_AND_SCOPED_FAILURE_20261029.md
[r2]: ../../06_auxiliary_collision_flows/notes/04_SIGNED_SQUARE_MODE_DAMPING_AND_ENDPOINT_CORRECTION_20261029.md
[history]: ../../06_auxiliary_collision_flows/chat-histories/0004_2026-10-29T11-58-02Z_list-modified-evolution-equations.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
