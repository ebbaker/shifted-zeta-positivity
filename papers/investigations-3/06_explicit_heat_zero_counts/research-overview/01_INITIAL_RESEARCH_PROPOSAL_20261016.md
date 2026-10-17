# Explicit heat zero counts: an initial research proposal

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Drafting model: **gpt-6-astra (Codex)**; reasoning effort **ultra**.
Status: **initial proposal; not executed**. No explicit counting constant,
new zero-count theorem, computational saving, or Newman bound is claimed.

This proposal implements the count item in the
[portfolio plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md).
Its purpose is to extract usable numerical constants from an existing
uniform theorem for one declared application. It follows
[Claude's reply, Section 4](../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md)
without treating an untested application as either proved or universally
excluded.

## Target and classification

[Polymath, Theorem 1.5(iv) and Section 9](https://arxiv.org/html/1904.12438)
already gives time-uniform local and cumulative counting estimates for the
zeta heat deformation. Extracting explicit constants is an analytic
infrastructure milestone. It is not discovery of the first asymptotic and
does not imply RH.

Use the physical coordinate \(z=x+iy\), related to the zeta ordinate by
\(\Im s=x/2\). Count zeros with multiplicity, and specify half-open spatial
intervals and boundary-zero conventions before applying the argument
principle. For \(X\ge4\pi\), the published comparison function is

\[
g(X,t)=\frac{X}{4\pi}\log\frac{X}{4\pi}-\frac{X}{4\pi}
       +\frac{11}{8}+\frac{t}{16}\log\frac{X}{4\pi}.
\]

The local \(O(\log(2+X))\) bound and cumulative error are uniform for
\(0<t\le1/2\), without the outer real-zero restriction used in stronger
parts of the theorem. Keep the heat-dependent drift explicit. Any extension
to \(t=0\), a different normalization, or a bounded low-height region needs
its own stated treatment.

## First bounded deliverable

Prepare one consumer specification and constant-extraction ledger, then
derive one explicit local upper-count bound on a declared domain. The
default analytic scope is \(0<t\le1/2\), \(X\ge200\), with unit windows;
change it only for a stated consumer need. A possible target is

\[
\#\{\rho:H_t(\rho)=0,\ X<\Re\rho\le X+1\}
\le A\log(2+X)+B,
\]

with numerical \(A,B\) and multiplicities included. This displayed estimate
is the task, not an already established explicit result. The first note
must identify the off-axis contours, nonvanishing bounds, comparison
functions, and every hidden constant in the chosen proof route. If the
proof requires an unevaluated compactness constant, expose and bound it or
restrict the domain explicitly; do not silently inherit it as numerical.

The deliverable includes one independent analytic review and a small
reproducible consumer budget. It does not include a high-volume zero survey,
a replacement of all existing winding certificates, or a new Newman-bound
campaign. If no active consumer can specify an error tolerance, retain this
as a staged proposal after the ledger rather than optimizing constants
without an application.

## Choose the consumer before optimizing

The requested inequality depends on the intended use:

| Consumer | Information required | What the first upper bound cannot supply |
| --- | --- | --- |
| Distant-zero interaction tail | Upper counts in consecutive windows and a summable distance kernel | Control of close-zero separation or a small derivative denominator |
| Lower population for attraction | Two-sided cumulative errors on a specified wider window | A lower population from an upper count alone |
| Exact interior count in a certificate | A certified interval identifying one integer, or a boundary argument-principle calculation | Reality, simplicity or absence of collisions from a total count alone |

The initial consumer should be one existing zeta-certificate calculation or
an explicitly requested distant-tail inequality. An attraction application
must propagate the corrected individual-zero normalization and count error
before predicting a gain. A failed parameter choice does not establish
inferiority at every height.

## Phases and model responsibilities

Roles designate model families, not fixed future settings. Record each
contribution's actual model and effort. Separate authorship from review and
keep a single writer responsible for each file.

| Phase | Lead | Independent responsibility | Gate |
| --- | --- | --- | --- |
| Consumer and proof ledger | Codex | Claude checks normalization, counting conventions and imported hypotheses | One quantitative tolerance and a complete list of constant obligations |
| Constant extraction | Codex | Claude audits off-axis estimates, compactness replacements and uniformity in time | Explicit constants on the declared domain, or a precisely localized obstruction |
| Numerical budget | Codex | Claude checks that the consumer needs the inequality actually proved | Certified arithmetic where needed and a transparent gain-versus-error comparison |
| Optional extension | Assigned after review | The other model audits the changed domain | A specific consumer justifies cumulative counts, low heights or conductor dependence |

Cross-model checks remain internal LLM review. Finite tests check arithmetic
and implementation; they cannot establish the universal analytic bound.

## Acceptance, stopping rules and dependencies

Accept the analytic output when all constants and cutoffs are evaluable,
the time and height domain is complete, and boundary multiplicities are
handled. Accept its proposed application only when the resulting error is
smaller than a numerical tolerance declared in advance. If the error consumes
that gain, stop the application and preserve any useful explicit theorem.
Reopen optimization only for a changed estimate, domain, or consumer budget.

The [Dirichlet-family proposal](../../01_dirichlet_newman_families/research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
may later request a uniform conductor-dependent analogue. Zeta constants
are not that analogue. A family velocity argument also needs control of
nearby zeros and multiple events; a distant-tail count alone is insufficient.

The [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
need not have the zeta source or its precise asymptotic normalization.
They do share many generic positivity and symmetry assumptions and test
any implication claimed from those assumptions alone. A count theorem can
remain valid in the presence of collisions; it is not required to reject
them. A later noncollision application must identify the additional
premise or quantitative inequality that fails at a control's actual
collision. Include multiple and boundary zeros in any finite counting
diagnostic rather than assuming simplicity.

Canonical repository starting points are
[summary 11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[summary 13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md)
and the
[carrier calculation](../../../investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md).
Follow [avoid 08](../../../../avoid/08_normalization_and_constant_slips.md),
[10](../../../../avoid/10_numerics_ahead_of_the_question.md),
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md): preserve
normalizations, identify the consumer before computation, distinguish a
machinery benchmark from new coverage, and check every imported estimate.

Read the [avoid index](../../../../avoid/README.md) and [result-summary index](../../../../result-summaries/README.md) before starting or revising this proposal.
