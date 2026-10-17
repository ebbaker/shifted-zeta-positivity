# Dirichlet Newman families: an initial research proposal

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Drafting model: **gpt-6-astra (Codex)**; reasoning effort **ultra**.
Status: **initial proposal; not executed**. No new approximation, finite-height
transfer theorem, numerical verification, or upper bound is claimed.

This proposal implements the family item in the
[portfolio plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md).
It follows Claude's [reply, Section 8](../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md),
with the unproved transfer and uniformity obligations made explicit.

## Target and classification

The eventual target is a quantitative upper bound for the de Bruijn–Newman
constants of specified primitive Dirichlet characters, possibly outside an
explicit exceptional set. A positive numerical upper bound is a milestone,
not an RH-equivalent reformulation. The initial deliverable is a feasibility
contract, not that milestone.

Start with primitive nonprincipal characters of prime conductor \(q>2\).
This keeps the family size explicit and avoids mixing primitive and induced
functions. Treat both parities. Fix the phase-normalized completed function
so that its functional equation is Hermitian, and use

\[
s=(1+iz)/2,\qquad
H_{t,\chi}(z)=\int_{\mathbb R}e^{tu^2}\Phi_\chi(u)e^{izu}\,du.
\]

The normalization must establish reality on the real axis and
\(\Phi_\chi(u)=\overline{\Phi_\chi(-u)}\). Complex characters do not generally
give an even \(H_{t,\chi}\). Cover both signs of \(\Re z\), or explicitly
prove and use the relation between conjugate-character pairs.
[Dobner, Section 2 and Theorems 1–3](https://arxiv.org/html/2005.05142v2)
provides the general existence and strip-contraction framework. It does not
supply the conductor-uniform upper bound sought here.

## First bounded deliverable

Produce one normalization and transfer-contract note, with an independent
review, before a conductor sweep or approximation implementation. The note
must contain: a normalization table for both parities and both height
directions; a hypothesis ledger for heat evolution and strip contraction;
and a proposed deterministic implication whose missing steps are identified.

The global contraction theorem says that an initial strip of half-width
\(\Delta\) contracts to half-width \(\sqrt{\max(\Delta^2-2t,0)}\). Its
contrapositive can force an initial off-line zero somewhere. It does not
locate that zero below a finite height. In particular, a finite-box barrier
and a density estimate cannot be combined without proving the required
localization or transport statement.

For a later almost-all route, the desired contract has the form

\[
\{\chi:\Lambda_\chi>\lambda\}
\subseteq\{\chi:Z_\chi(\sigma_*,T_*)\ge1\}
\cup E_{\rm barrier}\cup E_{\rm approximation},
\]

where \(Z_\chi\) counts initial zeros with \(\Re s>\sigma_*\) and
\(|\Im s|\le T_*\).
This is a proposed target, not an established inclusion. Its threshold,
finite height, boundary conditions and exceptional events must be derived.
If no defensible inclusion is available, the deliverable is the precise
missing lemma and a decision about the narrower per-character route.

## Phases and model responsibilities

Roles below designate model families. Record the actual model identifier and
effort for each future contribution. Keep one writer per note and separate
review files; cross-model review is internal review, not specialist validation.

| Phase | Lead | Independent responsibility | Output and gate |
| --- | --- | --- | --- |
| Normalization and contract | Claude | Codex checks symmetry, both height signs and finite-height quantifiers | Reviewed hypothesis ledger and transfer statement, or an explicit unresolved lemma |
| Uniform approximation | Claude | Codex checks joint parameter domains and every error payment | Explicit conductor-dependent approximation before predicting an exterior threshold |
| One deterministic benchmark | Codex | Claude checks applicability of the analytic contract | One parameter set with verification, barrier and exterior costs accounted for |
| Family density route | Claude | Codex checks the exceptional-set implication and cardinalities | A derived exceptional exponent, only after all constituent estimates apply |

The approximation phase should begin on a declared joint domain in
\((q,x,t,y)\). The formal heat shift involving \((t/4)\log(qx/4\pi)\) is a
motivation, not proof that conductor replaces physical height. Correction
terms, growing sum lengths and small-height errors must be included.
[Polymath's zeta approximation and certificate](https://arxiv.org/html/1904.12438)
is a proof template; its numerical contract is not automatically a theorem
for characters.

## Quantitative acceptance, dependencies and stopping rules

Accept the first phase only when every hypothesis has a source or a stated
proof obligation, the two height directions are covered, and no global
contrapositive is silently localized. Accept a later numerical milestone
only with a computable bound below \(1/2\), complete parameter coverage and
certified errors. An almost-all claim also needs an explicit exceptional
bound smaller than the actual family size on its stated range.

Compare the first derived exterior threshold with verified GRH heights for
one chosen parameter set. No overlap stops that benchmark with those inputs;
it does not close per-character research. Failure of conductor to lower that
threshold rejects the proposed height trade in that regime. Reopening needs
a changed approximation, parameters, verification range or barrier estimate.

The [explicit-count proposal](../../06_explicit_heat_zero_counts/research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
is a potential dependency only after a consumer specifies the required
inequality. Zeta count constants do not transfer to characters. Local upper
counts can control distant-zero tails; they do not bound near-collision
velocity denominators or establish simplicity.

The control screen must respect the family. Euler-factor modifications
need not be primitive Dirichlet \(L\)-functions and therefore do not refute
a theorem using that exact hypothesis. Weighted-square, reflected and
primitive-compatible theta controls likewise need not have the character
completion or coefficients. They remain tests of any generic intermediate
heat-flow assertion whose hypotheses they do satisfy; retain their actual
normalizations and state the failed family premise explicitly.

Use [summary 11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
for the existing certificate obligations and
[summary 12](../../../../result-summaries/12_collision_controls_and_screening.md)
for control scope. The governing rules are
[avoid 01](../../../../avoid/01_restating_the_target.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[10](../../../../avoid/10_numerics_ahead_of_the_question.md) and
[16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md): classify the
target, limit negative conclusions to their tested class, delay campaigns
until the theorem contract is usable, and verify imported hypotheses.

Read the [avoid index](../../../../avoid/README.md) and [result-summary index](../../../../result-summaries/README.md) before starting or revising this proposal.
