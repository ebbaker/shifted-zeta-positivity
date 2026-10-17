# Initial proposal: Sonin mixed-prime response

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.
Status: **initialized; one analytic calculation proposed**. No new mixed-response
identity, sign estimate or numerical certificate is claimed.

The first question is whether the actual Sonin projection produces a useful,
controlled interaction between two added primes. The target is one exact
mixed-response identity and an assessment of the estimate it makes possible.
The eventual support-adapted inequality \(K_S\le B_S\) is the full Weil
positivity target; renaming it is not an intermediate achievement.

## Starting point and unresolved claim

Read [result summary 07][sonin-summary], the [place-addition laws][addition]
(especially A3, A9 and A10), and the [finite Euler identity][euler].
They retain the inverse compressed metric and distinguish the complete
arithmetic form from a partial sum over places. Generic positive matrices
already permit either sign of a one-prime response.

[Claude's reply][reply], §5, proposes that accumulation of mixed responses
over a specified set of primes reduces to the Weil form on a span of translates.
That identification has not been supplied as a proved identity in the
exchange. The inverse metric can produce return terms. Establishing the
precise relationship is therefore part of this project's first task.

Fix a prepared source \(f\), its actual support interval \(I_L\), a finite
place set \(S\), and distinct primes \(p,q\notin S\). Define the four terms
using a single preparation convention and compare
\[
\Delta_p\Delta_q B_S[f]
=B_{S\cup\{p,q\}}[f]-B_{S\cup\{p\}}[f]
-B_{S\cup\{q\}}[f]+B_S[f].
\]
If preparation itself changes, explicitly transport the same underlying
input through all four terms and include its changes in the formula.
An identity obtained by silently changing \(f\) is not the proposed
comparison. Define every inverse on its proper range, in particular
\(\operatorname{Ran}\Pi_\infty\) where required.

## Work and model responsibilities

| Phase | Deliverable and owner | Review and gate |
| --- | --- | --- |
| 0: fixed contract | Codex writes the four operators, domains, source convention, active-prime rule and trace-class hypotheses. | Claude checks that the comparison uses the same source and the actual Sonin projection. |
| 1: exact mixed response | Codex derives the finite difference with the full compressed inverse, including return and boundary terms. Save one derivation note. | Claude independently derives or tests the claimed translate-span reduction: equality, additional terms, or a proved failure of that reduction. |
| 2: estimate selection | Claude proposes one bound on the actual arithmetic source, stating its support and place dependence. | Codex checks whether the hypothesis is weaker than the desired positivity and whether the constant remains useful. |
| 3: optional bounded check | Codex implements only a finite diagnostic specified by the reviewed formula, with projection and truncation errors accounted for. | Claude reviews what it measures and the final scoped disposition before any enlargement. |

These are assignments to model families. Record each execution's actual
model and effort; no future session settings or completed reviews are
implied. Keep one writer per note and separate review files.

The phase-1 acceptance criterion is an equality with justified operator
products, traces and inverses, plus an explicit comparison with the
translate-span claim. Merely applying an abstract resolvent identity is
insufficient if no conclusion about the actual source follows. A precise
obstruction to that claimed reduction is a valid bounded outcome.

For phase 2, choose a numerical or symbolic margin before computation:
for example, a mixed contribution bound that reduces a named residual
budget on a declared finite support, including its dependence on \(p,q,S,L\).
No prime-pair sweep is part of the initial task.

## Controls, stopping and dependencies

Apply the generic two-dimensional sign control from the place-addition
note and the smooth-density/two-channel controls routed by
[summary 04][positive-summary]. They test generic projection algebra, not
the full Sonin source. Identify the precise arithmetic or preparation
premise that a claimed sign estimate uses and that each relevant control
fails. Apply the [collision screen][controls] if a later claim implies
heat-flow noncollision. Do not demand that an unrelated control satisfy
the Sonin hypotheses.

Stop after the exact derivation and one cross-model reconciliation if the
only proposed estimate is equivalent to \(K_S\le B_S\), if a generic
positive-matrix argument is the entire mechanism, or if the fixed-support
budget cannot improve after all return terms are paid. Write a scoped
disposition, not a general exclusion of collective prime interactions.
Reopen for a new actual-Sonin estimate, a different preparation with proved
compatibility, or a precisely identified return-term cancellation.

This project can begin independently of the finite-sum and family lanes.
Its old proofs and certificates remain in their canonical homes. It does
not reopen routine support or trial-dimension enlargement.
Follow [avoid 01][a01], [07][a07], [10][a10] and [12][a12], alongside the
[avoid index][avoid] and [result index][results]. The
[portfolio plan][portfolio] controls expansion and closeout.

[sonin-summary]: ../../../../result-summaries/07_sonin_critical_boundary.md
[positive-summary]: ../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[addition]: ../../../weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md
[euler]: ../../../investigations/sonin-critical-boundary/notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md
[reply]: ../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[avoid]: ../../../../avoid/README.md
[results]: ../../../../result-summaries/README.md
[portfolio]: ../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md
