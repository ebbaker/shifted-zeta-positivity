# Sharp finite-sum bounds: initial research proposal

16 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Model: **gpt-6-astra (Codex)**; reasoning effort **ultra**.

**Status: initialized proposal.** This document specifies a bounded feasibility
study; it reports no new proof, certificate or Newman bound. The
[portfolio plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md)
sets the shared review gates and dependencies.

## Objective and inherited baseline

Determine whether the sharper finite-sum inequality already identified in the
Newman-certificate audit supports a complete, useful improvement in parameters
or certification cost. The target is the actual certificate conclusion
\(\Lambda\le t_0+y_0^2/2\), with initial verification, intermediate-time
barrier, final-time nonvanishing and the infinite exterior all accounted for.
A favorable finite row alone is not the target.

The [existing audit](../../../../papers/investigations-2/newman_certificate_audit/README.md)
remains the canonical home for its pinned public package, producer audit,
stored-row checks, tail analysis and barrier review. Those results and their
unresolved obligations are inherited by reference, not duplicated here.
This project owns the proposed sharper inequality and its new feasibility work.

At the historical pinned package's weakest row, the ordinary lower bound was
independently enclosed near \(7.91366746\times10^{-7}\). A floating evaluation
of the sharp weight gave approximately \(0.077\) at the same parameters.
At \(t_0=0.157\), four sampled first rows remained positive, suggesting the
historical candidate \(t_0+y_0^2/2\approx0.1745354\). These sharp-weight values
are exploratory, not certificates or a comparison with every currently
available method. The [finite-lane note, Section 5](../../../../papers/investigations-2/newman_certificate_audit/notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md)
states their provenance and remaining work.

## First bounded task

Keep the inherited verification height \(X\) and strip parameter \(y_0\)
fixed. Select one smaller heat time only after checking the exact certificate
contract. Derive the sharp-weight native binding and a valid transfer over the
whole required \(y\)-interval, retaining zeros and kinks of the absolute-value
terms. Monotonicity in a bound for the auxiliary coefficient \(\gamma\) does
not by itself supply this \(y\)-transfer.

In the same feasibility note, recalculate the all-index tail and complete
approximation allowance at that heat time. Existing barrier and verification
inputs may be reused only after their domains are explicitly shown to cover
the new application. The original tail's corrected contraction reserve is
about \(0.0395\), but lowering the heat time changes its inputs; that reserve
cannot simply be carried over.

The first deliverable is one proof-and-budget ledger: each inequality, its
domain, its imported source, its numerical allowance and its remaining
verification obligation. Test selected difficult rows and leg transitions
only when the analytic contract makes their meaning clear. Do not start a
multi-million-row sweep to discover whether the tail or transfer theorem works.

## Phases and model responsibilities

| Phase | Claude responsibility | Codex responsibility | Gate |
| --- | --- | --- | --- |
| Contract | Lead sharp binding, transfer and tail derivations | Check normalization, inherited domains and required coverage | One complete statement with no hidden parameter transfer |
| Bounded feasibility | Specify analytic constants and critical cases | Independently implement outward row checks and an error ledger | Positive complete margins on the declared pilot, with a viable infinite tail |
| Certificate design | Review uniformity and any amortized bounds | Lead producer, seams, coverage and independent replay design | Cross-model acceptance before full production |
| Completion | Audit the final mathematical chain | Assemble hash-bound evidence and coverage report | Every claimed domain covered, or a scoped negative conclusion |

These are proposed model-family responsibilities. Actual serving models,
effort settings and review independence are recorded when the work occurs.
Each file has one writer; a reviewer produces a separate assessment.

## Controls, dependencies and exclusions

Use [summary 11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
for the corrected interface and certificate contract, and
[summary 12](../../../../result-summaries/12_collision_controls_and_screening.md)
for controls. Weighted-square and reflected sources lack the complete
arithmetic input used by this theta application. Euler-factor controls change
the Dirichlet coefficients and conductor; their theta approximations cannot
be reused unchanged. A generic lower-bound lemma must state its full input
class, and any claimed application to a control must retain that control's
own coefficients and errors. A collision-free control box may legitimately pass.

The corrected Riemann–Siegel residual belongs to its corrected center; it
cannot be inserted into an incompatible uniform finite-sum inequality.
The [cross-model audit](../../../../papers/investigations-2/newman_certificate_audit/reviews/CROSS_MODEL_REVIEW_OF_CLAUDE_AUDIT_CODEX_20261013.md)
and [Review 20](../../../../papers/investigations-2/active/22_theta_manifold_geometry/reviews/20_ADDITIONAL_PATHS_FORWARD_ASSESSMENT_CODEX_20261016.md)
govern that scope. Refresh the public-source comparison and pin its revision
before presenting a gain as competitive or novel.

## Completion, stopping and reopening

Success is a fully justified parameter improvement, a measurable reduction in
certification cost at equal coverage and accuracy, or a precise obstruction
to this sharp-weight design. The existing audit's unreplayed producer rows
remain unresolved until actually checked; samples do not discharge them.

Stop the proposed campaign if uniform transfer fails, the tail consumes the
margin, complete coverage is unaffordable under its declared budget, or the
method changes neither attainable parameters nor cost. Distinguish an
inconclusive computation from a disproved inequality. Reopen only with a new
lower-bound mechanism, improved complete budget, or documented coverage method
that addresses the recorded obstruction.

Apply [avoid 04](../../../../avoid/04_counts_and_precision_as_evidence.md),
[avoid 09](../../../../avoid/09_round_floors_and_fitted_laws.md),
[avoid 10](../../../../avoid/10_numerics_ahead_of_the_question.md) and
[avoid 12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Keep large regenerable sweeps outside Git under
[LARGE_FILES](../../../../LARGE_FILES.md). Preserve small records, source pins
and replay instructions; update the status and concise history at each accepted gate.

Read the [avoid index](../../../../avoid/README.md) and [result-summary index](../../../../result-summaries/README.md) before starting or revising this proposal.
