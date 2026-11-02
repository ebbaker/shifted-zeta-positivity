# Research plan for J-B11 integrated signed averaging

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Documentation task **J-E08**; no mathematical execution.

**Contract r1:** one bounded conceptual assessment of the complete order-four, index-zero-to-one signed comparison. J-B11 is distinct from completed J-B05. The [sole Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns live status. The author has selected this investigation for an independent parallel session; no quantitative theta input has yet been chosen and no execution has begun.

| Work | Type and recommendation | Readiness | Required output |
| --- | --- | --- | --- |
| J-B11: select a signed theta input and assess the complete covariance | **B — Astra**; local monotonicity fails and a different quantitative input must be chosen | Ready for conceptual selection; covariance estimate unproved | One worked bound, scoped failure or exact missing relation, with positive-anchor accounting |
| Fixed finite verification, if justified by the return | **E — Sol** | Gated; no numerical task issued | Separate complete formula, domain, endpoint/tail errors, limits and acceptance test |

The author chooses actual model and effort. Record actual session metadata. Preparing this plan does not run the task, dispatch agents, or select a model automatically.

## Question and fixed objects

Keep the complete canonical theta source at physical time zero, the positive carrier \(w_{4,0}\), unchanged signed observable \(h_4\), and \(q=\prod_{j=1}^4u_j^2\) from the [overview](../research-overview/01_SIGNED_AVERAGING_RESEARCH_OVERVIEW_20261101.md). The default sufficient target is a theta-specific proof of
\[
\operatorname{Cov}_{4,0}(h_4,q)\ge0,
\qquad
A_{4,1}-A_{4,0}=
\frac{\operatorname{Cov}_{4,0}(h_4,q)}{E_{4,0}q},
\qquad A_{4,0}>0.
\]
The identity is established; the selected covariance sign is open. The known negative fourth-coordinate derivative and negative configurations must be allowed. Known \(D_{4,1}>0\) is a baseline for interpreting the pilot, not an input to a new sign mechanism.

## Bounded work sequence

1. **Select one additional signed theta input.** Identify a concrete identity or quantitative relation for the full covariance, with a named information source. Explain why it supplies more than the failed pointwise premise or generic source positivity. Compare at most one alternative input and then choose one attempt. If no credible added relation can be stated, return that specific gap instead of starting acquisition.
2. **State the comparison before estimating.** The default is nonnegative full covariance. A weaker anchor-preserving bound must be declared explicitly, with the allowed negative contribution paid from the actual positive anchor. It is a changed comparator. Do not count the exact reformulation of \(A_{4,1}>0\) as an acquired estimate.
3. **Work through the complete signed balance.** Retain the mixed origin/tail configurations in the obstruction, separated and coincident nodes, and the unbounded integration domain. Show how the favorable and unfavorable contributions are compared. A region decomposition must keep every remainder and its sign/size payment. Justify all origin endpoints and full-source tails. If introducing a continuous index tilt, pay differentiation and integrability; do not assume order-four real-parameter positivity from the order-three result.
4. **Return the scoped outcome.** State whether the chosen target was proved, refuted, or left with an identified uncontrolled term. Explain the finite \(r=4,k=0\to1\) consequence and the additional work needed for more indices or growing order. Do not depend on an unproved result from the parallel J-B10 session.

## Controls and stopping rule

The canonical mixed-node obstruction is a constraint on the proposed mechanism, not a discarded exception. Gaussian \(h_4=1\) checks normalization and a zero covariance; it is not evidence of a theta sign. The original return's other controls lack particular canonical source premises or have untested covariance signs. Name those precise limits; do not infer the fate of this inequality from a collision elsewhere or from finite endpoint matching.

Stop after one selected estimate reaches a result or a precise obstruction. Stop immediately if it reinstates unchanged-\(h_4\) coordinatewise monotonicity, removes its negative region, assumes the covariance sign it must prove, or spends an unbounded remainder without paying the anchor. Do not replace a failed mechanism with a derivative scan, coefficient campaign or an open-ended numerical integration.

## Deliverables and acceptance

Save **`notes/03_J_B11_INTEGRATED_SIGNED_AVERAGING_RETURN_YYYYMMDD.md`** with the actual local date and next unused number if needed. Include the chosen theta input, exact source versions, complete covariance/comparator, positive-anchor calculation, covered domain and remaining tails, controls, proof or scoped failure, small-index/growing-order consequences, actual model/effort, and one next B/E recommendation.

A worked bound, an established scoped failure, or an exact information gap reached after the chosen attempt can complete this bounded task. Merely repeating that \(\operatorname{Cov}\ge0\) is wanted cannot. Any revised target must be distinguished from the default. Save fixed finite algebra or small support in this direction's `numerics/`; reviews belong in `reviews/`. Preserve J-B05 and its evidence unchanged, update local navigation, and deliver the findings in chat.

Do not overwrite this issued plan with the return. Recommend a separate E/Sol task only after its expression, finite cases, errors, work limits and acceptance criterion are fixed; no such task is ready now. A redesign requires a stated B decision rather than silently changing the source or observable.

## Parallel ownership and shared updates

The author will run J-B11 and J-B10 in separate chats. This session owns new work under **`papers/investigations-5/07_positive_theta_primitives/01_jensen/02_signed_averaging/`**. The sibling folder and all prior mathematical notes, numerical evidence, review records and replay manifests are read-only inputs. Do not make this task depend on an unreviewed sibling result. If a useful connection appears, state it conditionally with the exact input version.

The [Jensen progress register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) remains the sole live task ledger. At start and finish, update only this task's row and its dated return entry. **Serialize every shared-file update** using the same POSIX advisory lock, `papers/investigations-5/07_positive_theta_primitives/01_jensen/research-progress/.jensen-progress.lock`: acquire an exclusive `fcntl.flock`, reread the current file while holding it, apply only the relevant edit, write atomically, then release. Keep that whole transaction in one process; locking only the final write is insufficient. The other session uses the same lock. Allocate any new task ID only under that lock after checking the current register. Lock files are ignored; the lock does not replace chat-history locking. For separate clones, this local lock is insufficient: designate one shared-file writer and provide proposed register updates in the other return.

Keep branch README/index updates local. Leave portfolio summaries, the parent overview and milestone history for a later coordinated integration. If a new inspected source must enter the common catalog, prepare its entry first and serialize that narrow update with the same shared lock. Never edit the sibling's task row or rebuild a shared file from an earlier read. These rules address [parallel-writer failures](../../../../../../avoid/17_parallel_writers_and_broken_registries.md).

A genuinely new chat registers its actual identity and title under **`papers/investigations-5/07_positive_theta_primitives/01_jensen/02_signed_averaging/chat-histories/`** using [the capture tool](../../../../../../tools/CHAT_HISTORY.md). An already registered chat preserves its unique existing home; do not re-register or move it as routine setup. This preparation chat remains parent Jensen history0005; do not reuse its identity. Refresh at turn start and arrange bounded exact-turn capture at the end unless trusted completion hooks are verified active.


## Evidence and research standards

Use the [result index](../../../../../../result-summaries/README.md), especially [theta identities](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), with the [avoid index](../../../../../../avoid/README.md), especially [target reformulation](../../../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). Keep the source's status words and internal-review qualifications. An identity, a sufficient conjecture, a numerical observation and a proved estimate are different outputs.

The [common reference catalog](../../../references/README.md) retains inspection limits. Inspect a primary source before importing a new theorem and record the relevant hypotheses and checked passages. A broad literature survey or certificate replay is not needed merely to start this question.
