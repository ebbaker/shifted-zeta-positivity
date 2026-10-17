# Initial proposal: constructive stable models

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.
Status: **initialized; gated on one explicit model family**. No stable
approximation or theta convergence theorem is asserted.

Seek a family whose real-zero property follows from a proved construction
and whose approximation to the actual theta heat flow can be controlled.
The first milestone is much smaller: specify one family, verify its
independent stability mechanism, and derive the first nontrivial
coefficient or heat-compatibility inequality. A global stable limit proving
RH is an RH-strength objective, not a weaker estimate supported by finite
checks.

## What is inherited

The [earlier stability program][old] remains the canonical source for its
moment normalization, spin scout and rejected alternatives. In that
normalization,
\[
I_{2k}(t)=\int_0^\infty u^{2k}e^{tu^2}\Phi(u)\,du,\qquad
a_k(t)=\frac{I_{2k}(t)}{(2k)!},\qquad
\gamma_k(t)=k!a_k(t).
\]
Coefficient Toeplitz tests use \(a_k\); the stated Jensen tests use
\(\gamma_k\). Generic Hankel moment positivity is not either of those
properties. Source-density Pólya-frequency positivity and coefficient
positivity are different assertions. Preserve those distinctions.

[Claude's reply][reply], §3, accepts the corrected Jensen degree bound in
the [preceding response][response]. A theorem giving hyperbolicity at
sufficiently large coefficient shift for each fixed degree supplies no
uniform physical-height margin or all-degree theta theorem. A table of
favorable Jensen polynomials is not this project's first deliverable.
Use [summaries 11][s11], [13][s13] and [14][s14] to locate what is already
known before proposing another stable realization.

## Bounded proposal and assignments

Claude should nominate **one** family, with an exact formula and parameter
domain. Possible choices include a stability-preserving operator applied
to a known stable seed, or an admissible ferromagnetic spin family.
Neither is selected by this overview. Selection must include the precise
primary theorem and a check of all its input hypotheses. If no candidate
passes that check, a short disposition completes the opening phase.

| Phase | Owner and required output | Gate and other-model responsibility |
| --- | --- | --- |
| 0: nominate | Claude specifies the approximants, independent stable seed or admissible elementary transforms, theorem, and intended theta limit. | Codex audits the actual coefficients and detects any assumption of theta's unknown stability. |
| 1: compatibility | Claude derives the first exact coefficient constraint and the heat evolution of the same family. | Codex checks normalization and one obstruction or inequality using the actual theta moments. |
| 2: bounded diagnostic | Codex encloses only the finitely many entries needed to decide that compatibility question. | Claude reviews the uncertainty and explains what passing or failing means. |
| 3: convergence proposal | Claude supplies a complex-compact convergence route, with tail and differentiated convergence estimates needed by the claimed application. | Codex audits whether the majorant and parameter choices can hold uniformly. Expansion requires a new applicable estimate. |

The model names specify future responsibilities; record actual serving
models and effort when the work occurs. Each phase has one note owner and
a separate cross-model review. This is internal LLM review.

For a spin proposal with \(S=\sum_i b_i\sigma_i\), the same parameters must
produce the required heat weighting: \(e^{tS^2}\) adds pair coupling
\(2tb_ib_j\). Independently fitting a new distribution at each \(t\)
does not establish compatibility. Use the earlier equal-weight exclusion
before proposing a larger version of that family. Unequal amplitudes are
a possibility to test, not evidence of existence.

For an operator proposal, state its stability-preserving domain, action on
the chosen seed, and the topology of convergence. A formal exponential of
the heat operator needs its own convergence and domain justification.
Do not build in a sequence of heat thresholds tending to zero unless
that property has been proved independently.

## Acceptance, controls and stopping

The opening phase passes only with a specified construction and one
nontrivial compatibility inequality whose terms can be bounded or whose
failure can be established. A finite moment match can reject a particular
family; passing it cannot establish the limiting theorem. A bounded
diagnostic must state its required enclosure accuracy before execution.

Screen any proposed sufficient mechanism against the [controls][controls]:
weighted-square sources retain positivity and square support but lack full
reflection; reflected sources retain reflection but lack the required
integer-square source; primitive-compatible controls retain the auxiliary
positive channel without the full arithmetic source. Euler-factor
controls test premises preserved by their modification. Name the
construction hypothesis or quantitative inequality each relevant control
fails; “theta is special” is not that hypothesis. A finite certificate
need reject a control only on a domain containing its contrary witness.

Stop the candidate after one nomination/compatibility/review cycle if its
stability theorem assumes the target, its only progress is finite moment
fitting, heat parameters must be independently refitted, or no credible
noncircular complex-compact convergence route is available. The justified
majorant is required at the later convergence gate. A useful exact obstruction is a
successful project output. Reopen only for a different construction or a
new inequality addressing the named failure, not a larger fit.

This project is independent of the source-measurement audit: poor
conditioning for fixed finite measurements does not exclude constructive
approximation with other admissibility or convergence hypotheses.
Keep global RH-strength claims distinct from bounded milestones under
[avoid 01][a01], [02][a02], [14][a14] and [16][a16].
The [avoid index][avoid], [result index][results] and
[portfolio plan][portfolio] govern further development.

[old]: ../../../investigations-2/active/13_stability_jensen_lee_yang/notes/INITIAL_RESEARCH_PROGRAM_20261013.md
[reply]: ../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md
[response]: ../../../brainstorm/investigations-3/reviews/02_RESPONSE_TO_CLAUDE_BRAINSTORM_CODEX_20261016.md
[s11]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[s13]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[s14]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a14]: ../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[a16]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[avoid]: ../../../../avoid/README.md
[results]: ../../../../result-summaries/README.md
[portfolio]: ../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md
