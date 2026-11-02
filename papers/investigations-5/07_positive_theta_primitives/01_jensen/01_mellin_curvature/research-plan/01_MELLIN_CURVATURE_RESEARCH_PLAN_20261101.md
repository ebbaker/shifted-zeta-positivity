# Research plan for J-B10 signed Mellin curvature

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Documentation task **J-E08**; no mathematical execution.

**Contract r1:** one bounded conceptual assessment at determinant order three, with the complete canonical theta source at physical time zero. This plan fixes the task's scope; the [sole Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns live status. It is ready for the author's separate session and has not been executed.

| Work | Type and recommendation | Readiness | Required output |
| --- | --- | --- | --- |
| J-B10: select and assess one theta-specific joint curvature estimate | **B — Astra**; the signed input and useful comparator remain conceptual choices | Ready for brainstorming; Gaussian bound unproved | One worked estimate, scoped failure or exact surviving obligation |
| Fixed finite verification, if it becomes the sole remaining step | **E — Sol** | Gated; no execution contract or numerical task issued | Separately specified expression, domain, errors, limits and acceptance test |

Edward Baker chooses the actual model and effort. Record the running session's actual metadata. This plan recommends neither automatic model changes nor new agent dispatch.

## Question and fixed inputs

Use the notation and exact expression \(\mathcal C_3(s)\) in the [overview](../research-overview/01_MELLIN_CURVATURE_RESEARCH_OVERVIEW_20261101.md) and [initial assessment, Section 3](../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md). Keep \(\Phi,h_3,w_s,A(s),M(s)\) and all normalization factors unchanged. The selected sufficient target is
\[
\mathcal C_3(s)\le\kappa_3(s),\qquad s\ge0.
\]
The accepted real-tilt positivity justifies \(\log M\). Do not assume a noninteger Toeplitz endpoint identity or import positivity for higher-order real tilts.

## Bounded work sequence

1. **Choose the quantitative input.** Name one actual theta identity, differential relation or complete integral estimate and identify the joint expression it controls. State what it adds beyond positive association and increasing \(A\). Compare at most one concrete alternative input or an integrated comparator within this investigation; the sibling signed-averaging task has its own session. Select one attempt before expanding algebra.
2. **Work the selected estimate.** Keep the carrier variance, centered-square covariance and squared-covariance term together. If using the signed two-copy formula from the initial return, retain opposite-sign contributions. State any exact finite algebra and its purpose before executing it. Do not substitute coefficient acquisition or a numerical search for the missing input.
3. **Account for the full domain.** Treat \([0,2]\), needed for \(k=1\), the remaining compact range, and the unbounded tail. Retain origin, coincident-node and full-source tail terms. A partial proof is recorded on its actual domain with the complement explicitly unpaid.
4. **Classify the result and return.** Explain the conditional order-four consequence and what is missing at arbitrary finite order. If the pointwise Gaussian bound fails, specify whether the integrated Gaussian comparison or only the exact sign condition survives. A revised comparator is a new target, not success on the original one.

## Controls and stopping rule

Reuse the initial return's claim-specific screen. Gaussian equality checks normalization. The two-point relaxation defeats association-only inference but lacks canonical theta/Toeplitz realization. Euler-factor, weighted-square, reflected and positive-primitive controls require their actual hypotheses to be checked; failure of literal canonical reconstruction does not determine an untested quantitative inequality. A positive-time collision is not a counterexample to this time-zero finite-order claim.

Stop this assessment after the one chosen estimate either produces a usable result or reaches a precise obstruction. In particular stop if it assumes the desired \(D_4\) sign, discards \(h_3\)'s negative part, bounds only the carrier variance, or merely restates \(Q<B\). No unbounded derivative escalation, precision campaign, PDE/root simulation or repeated coefficient scan follows a failure.

## Deliverables and acceptance

Save the mathematical return as **`notes/03_J_B10_SIGNED_MELLIN_CURVATURE_RETURN_YYYYMMDD.md`**, using the actual local date and next unused number if another file appears first. Include the selected input and exact versions, comparator, domain, complete argument or obstruction, endpoint/tail accounting, controls, small-index and growing-order consequences, actual model/effort, and one next B/E recommendation. A proof, scoped failed comparison, or exact surviving term can complete J-B10; a restated goal cannot.

Small support belongs in this direction's `numerics/`; any subsequent assessment belongs in `reviews/` and must state its review relationship. Update local navigation and deliver a clear chat summary. Do not rewrite this issued plan or the continuation note with the result; link the dated return. The overview can later summarize accepted findings without upgrading their status.

If a finite certificate is the only remaining obligation, prepare a separate E/Sol request with fixed formula, cases, precision/refinement caps, error budgets and acceptance criteria. Do not execute it within this B task. If the mechanism needs redesign, record the exact decision required before recommending another B task.

## Parallel ownership and shared updates

The author will run J-B10 and J-B11 in separate chats. This session owns new work under **`papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/`**. The sibling folder and all prior mathematical notes, numerical evidence, review records and replay manifests are read-only inputs. Do not make this task depend on an unreviewed sibling result. If a useful connection appears, state it conditionally with the exact input version.

The [Jensen progress register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) remains the sole live task ledger. At start and finish, update only this task's row and its dated return entry. **Serialize every shared-file update** using the same POSIX advisory lock, `papers/investigations-5/07_positive_theta_primitives/01_jensen/research-progress/.jensen-progress.lock`: acquire an exclusive `fcntl.flock`, reread the current file while holding it, apply only the relevant edit, write atomically, then release. Keep that whole transaction in one process; locking only the final write is insufficient. The other session uses the same lock. Allocate any new task ID only under that lock after checking the current register. Lock files are ignored; the lock does not replace chat-history locking. For separate clones, this local lock is insufficient: designate one shared-file writer and provide proposed register updates in the other return.

Keep branch README/index updates local. Leave portfolio summaries, the parent overview and milestone history for a later coordinated integration. If a new inspected source must enter the common catalog, prepare its entry first and serialize that narrow update with the same shared lock. Never edit the sibling's task row or rebuild a shared file from an earlier read. These rules address [parallel-writer failures](../../../../../../avoid/17_parallel_writers_and_broken_registries.md).

A genuinely new chat registers its actual identity and title under **`papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/chat-histories/`** using [the capture tool](../../../../../../tools/CHAT_HISTORY.md). An already registered chat preserves its unique existing home; do not re-register or move it as routine setup. This preparation chat remains parent Jensen history0005; do not reuse its identity. Refresh at turn start and arrange bounded exact-turn capture at the end unless trusted completion hooks are verified active.


## Evidence and research standards

Use the [result index](../../../../../../result-summaries/README.md), especially [theta identities](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), with the [avoid index](../../../../../../avoid/README.md), especially [target reformulation](../../../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). Keep the source's status words and internal-review qualifications. An identity, a sufficient conjecture, a numerical observation and a proved estimate are different outputs.

The [common reference catalog](../../../references/README.md) retains inspection limits. Inspect a primary source before importing a new theorem and record the relevant hypotheses and checked passages. A broad literature survey or certificate replay is not needed merely to start this question.
