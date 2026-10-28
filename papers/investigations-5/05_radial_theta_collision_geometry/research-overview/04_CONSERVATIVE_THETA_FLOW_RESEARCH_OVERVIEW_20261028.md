# Research overview for conservative theta flows and collision amplification

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0008, **Continue radial theta investigation**.

**Aim:** find a simple spatial evolution of the explicit theta integrand that preserves the entire observation H(t,a) and makes a hypothetical collision H=H_a=0 yield a useful quantitative constraint. The radial density may change, and no preferred direction is required. The immediate tasks are to measure the existing heat diagnostic's finite-time usefulness and decide what stronger conservative dynamics, if any, is worth developing.

This is a new program overview. It supersedes overview03 for current priorities while retaining its results and task meanings. The [new progress register][progress] is the sole live ledger, and [continuation26][continuation] gives the next-session routing. The initial planning return added no mathematical theorem or numerical result. **28 October B01 return:** [Note28][return28] now supplies a conservative feedback magnifier and finite collision deadline; [assessment16][review16] states its proof scope. Global regularity is a pointwise reformulation. The generic initializer payments are analytically too weak, so B02 is the substantive next task and [E02 R1][packet2] is an optional scalar loss audit. Progress04 owns their live status.

## Established starting point

[Note25][n25] gives the complete signed density and ordinary spatial heat flow:
\[
j_0(t,a;X)=\mathbf1_{|X|\ge1}\frac{Q_t(|X|)}{32\pi\sqrt{|X|}}
              \cos(a\log|X|/2),\qquad
\partial_sj_s=\varepsilon\Delta j_s.
\]
Here s is auxiliary time and t is physical Newman time. The whole-space Gaussian convolution preserves H and every finite spectral derivative. The initially empty unit ball is part of the evolved domain and cannot be omitted later.

At the spatial origin,
\[
F_{s,k}:=(4\pi\varepsilon s)^{3/2}\partial_a^k j_s(0)
=\partial_a^kH-\frac{M_{2,k}}{4\varepsilon s}+\mathcal R_{s,k},
\qquad |\mathcal R_{s,k}|\le\frac{A_{4,k}}{32\varepsilon^2s^2}.
\]
At a collision, k=0 and k=1 both lose their leading diffusion coefficients. This is an explicit extra-decay diagnostic, not yet growing amplification or a theta-specific exclusion. The exact Gaussian-polynomial control has the same cancellation. [Review14][review14] records the same-assistant verification scope.

The source is the complete theta sum. Note25 gives termwise evolution and source-truncation error bounds; [Note24][n24] supplies the corresponding bounded projected-flow interface. [Note23][n23]'s projected descent and local signed adjoint remain available alternatives. [Note22][n22]'s fixed-width multiplicative comparison has no gain over its matched radial calculation; that scoped result is not a restriction on conservative flows.

## The mathematical questions that would advance the program

Three advances should be distinguished.

1. **Finite-time information:** determine the actual moment allowances, useful auxiliary scales and cost of the heat diagnostic on a fixed theta/control sample. Its asymptotic powers are already proved; reproducing them alone is not new evidence.
2. **A useful mechanism:** find a conservative evolution and observable whose collision-dependent behavior yields more than a rescaled conserved mass or a coordinate change. Possibilities include growth, concentration, signed energy transfer or a stronger finite-time comparison. A growing instability is not required if another effect gives an actual estimate.
3. **Canonical separation:** prove a quantitative bound from the complete theta data which is incompatible with the proposed collision behavior on a stated domain. Generic amplification can also occur for controls; the source-specific comparison must do the separating work.

The long-term threshold application needs additional uniform time, height, multiplicity and tail coverage. A pointwise diagnostic or finite sample is not that theorem.

## Admissible systems and comparison rules

The required invariant is
\[
\int_\Omega j_s(t,a;X)\,dX=H(t,a)
\]
as a differentiable parameter family. A continuity equation with zero complete net flux is one sufficient construction. Each candidate must specify the domain, boundary/tail terms, initial data and observation, as well as the actual evolution of its spectral derivatives. In a nonlinear flow, an independently assigned second field is not automatically ∂_a j_s. The pointwise physical heat law need not survive unchanged; all parameter corrections must be included so the integrated physical observation is still correct.

The known fixed-kernel uniqueness statement is limited: a frequency-independent source tested against the unchanged cosine kernel at every frequency still has its original radial marginal. Evolving the full signed density, or source and phase together, avoids imposing that stronger factorization.

For every proposed gain, compare against the same direct theta information with the full error and boundary allowances. A formula involving division by H²+H_a² does not by itself create independent collision information. A time rescaling or added geometry is useful only if its resulting estimate or evaluation cost is useful.

## Task types and model routing

Follow the [repository guidance][workflow]. **B / brainstorm** means a conceptual choice or difficult proof strategy remains; these tasks are assigned to Astra with their specific reason below. **E / execution** includes routine analysis as well as numerics once the route is fixed; these tasks are assigned to Sol. Types and recommendations are set now, before any of the new research runs.

### Conceptual and analytical decisions

| Task | Model | Question and bounded deliverable | What permits execution |
| --- | --- | --- | --- |
| **CTF-B01** | **Astra** | Define a useful collision-sensitive observable and assess at most two conservative flow classes. Start with the linear isotropic baseline and, if needed, one response/jet-coupled conservative alternative. Derive the observation and jet accounting, identify the needed regularity, and select one candidate or record a scoped failure. | A versioned candidate equation, domain, initial data, observable, expected comparison, controls and finite test contract for E02. |
| **CTF-B02** | **Astra** | For the selected mechanism, find the additional canonical theta estimate and compare it with the matched direct calculation. The unresolved issue is a new signed/coercive relation, not the computation of already specified integrals. | A proved finite-domain estimate or a precise remaining premise; issue E03 only for quantities that the resulting argument actually needs. |
| **CTF-B03** | **Astra, later** | Determine whether an actual canonical result has the uniformity needed for the existing positive-threshold reduction, including multiplicities and endpoints. | A transfer theorem or an explicit coverage gap; no automatic height scan. |

B01 may begin from Note25 without waiting for numerics. E01 is recommended first as a small, separately bounded measurement of the baseline; its success is not an invented mathematical prerequisite for B01. The subsequent Note28 return supplies B02's candidate; B03 still needs a substantive canonical result. Consult Progress04 for live status.

### Numerical work and calculations with an established method

| Task | Model | Fixed work and deliverable | Boundary requiring brainstorm |
| --- | --- | --- | --- |
| **CTF-E01** | **Sol** | Evaluate the central heat diagnostic, its moment allowances and matched direct observations on the frozen finite theta/control grid in [request R1][packet]. Return reproducible code, a small record, costs and a short disposition of finite-time usefulness. | A new observable, PDE, source, analytical mechanism or broader scan is required. |
| **CTF-E02** | **Sol** | Complete routine identities/error accounting and implement the one candidate frozen by B01; execute only its declared finite comparison. | Candidate equations or proof strategy need revision, rather than routine correction or bounded refinement. |
| **CTF-E03** | **Sol** | Obtain specified rigorous finite quantities/certificates for the bound supplied by B02, with source, arithmetic, integration and tail errors separated. | A new uniform estimate or a changed theorem premise is needed to make certification meaningful. |
| **CTF-E04** | **Sol** | Integrate accepted returns into the existing manuscript and navigation, check the saved source with the built-in compiler, and record the actual verification scope. | A new mathematical assertion or interpretation needs a conceptual decision. |

E02–E04 do not inherit a running model's ownership. Straightforward proof completion belongs in E; a coding task that still requires choosing its scientific question belongs in B until that choice is made.

## Initial decisions, subsequent return and success conditions

**Initial default: [E] CTF-E01 — Sol, request R1.** Note27 has completed its fixed question about finite-time allowances and matched acquisition cost. It does not close conservative dynamics.

**B01 subsequently completed; next substantive task: [B] CTF-B02 — Astra.** Note28 selects one candidate and proves its collision deadline. It also proves that the first generic paid lifespan is always less than one hundredth of the upper deadline. B02 must derive an independent canonical estimate or a precise failed bound. The optional E02 audit measures the size and source of that known payment gap; it cannot reverse the analytic comparison.

No task should be enlarged because its assigned model happens to have time or context remaining. At a declared boundary, update the live ledger and show the next task's B/E shorthand, model and reason before dependent work begins.

## Controls, evidence and records

Use the [result index][results] and [avoid index][avoid], especially [geometric realizations][geometry], [collision controls][controls], [target classification][a01], [control-premise screening][a02], [scope][a07], [numerics before a question][a10], and [tests of known results][a11].

The Gaussian-polynomial control collides at (T_c,2√6), has the required moments on t<T_c+4, and satisfies the generic heat theorem. No hypothesis of that theorem fails for it. The other registered controls have their listed missing theta arithmetic/reflection inputs; a new canonical estimate must identify which premise it uses and why the corresponding control fails it. Atomic sources remain outside the current L¹-density statement.

Keep proved identities, floating measurements, interval certificates and proposed mechanisms separate. New work goes to notes, numerics and reviews with actual model/effort recorded. The existing manuscript remains the sole source; no new snapshot or replacement document is needed. Historical LOC/RDZ/RTC/RLC tasks keep their original scope through the crosswalk in the new register.

[progress]: ../research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md
[continuation]: ../notes/26_CONSERVATIVE_THETA_FLOW_CONTINUATION_20261028.md
[packet]: ../research-progress/handoffs/CTF-E01_BASELINE_HEAT_MEASUREMENTS_REQUEST_R1_20261028.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[n25]: ../notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[n24]: ../notes/24_EXPLICIT_THETA_FLOW_AND_COLLISION_MAGNIFICATION_SCOPE_20261027.md
[n23]: ../notes/23_PROJECTED_ANNULAR_FLOW_RESPONSE_AND_LOCAL_ADJOINT_20261027.md
[n22]: ../notes/22_STEERED_TUBE_GREEN_IDENTITY_AND_MATCHED_COMPARISON_20261027.md
[review14]: ../reviews/14_PROJECTED_FLOW_MANUSCRIPT_AND_COLLISION_SCOPE_20261027.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a11]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md

[return28]: ../notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[review16]: ../reviews/16_CONSERVATIVE_FEEDBACK_MAGNIFIER_B01_ASSESSMENT_20261028.md
[packet2]: ../research-progress/handoffs/CTF-E02_FEEDBACK_DEADLINE_PAYMENTS_REQUEST_R1_20261028.md
