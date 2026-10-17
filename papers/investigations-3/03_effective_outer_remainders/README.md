# Effective outer remainders

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

**Status: two notes filed; Codex audit pending.** On 17 October 2026
Claude Opus 5.5 (`claude-opus-5-5`, Claude Cowork, reasoning effort max)
added two notes and three [check programmes](numerics/README.md).

[Note 01](notes/01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md) takes as consumer the exterior input of
Project 01's strip comparison, Lemma A_p: a floor for
S(x,p,t) = −Im(H_t′/H_t)(x + ip) at a fixed height p ≥ √5. It stops the
inherited four-jet budget, whose unavoidable costs exceed its margin 1/8
by a factor of about 10⁶ at L ≈ 27. Proved: an exact transport identity
(at height p the flowed function is a Gaussian average of the completed
L-function, which can be recentred at the saddle of its Gamma factor;
Lemmas 3.1–3.3) and an explicit remainder for the resulting transport
law (Proposition 4.5, Theorem 4.6). Numerical, by floating evaluation on a
20-point time grid (not outward-rounded): Lemma A_p with no loss at every
height for every primitive χ of conductor q ≥ 1.1·10⁵ (even) or 4.9·10⁴
(odd) at p = √5, and for zeta beyond the X of Polymath's and
Platt–Trudgian's certificates.

[Note 02](notes/02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md) reads Hakimoglu-Brown's preprint
(arXiv:2610.12803v1) against note 01. The preprint's floors have the same
main term as note 01's, and at its height 61/20 note 01's remainder is 1.7
to 4.4 times smaller (floating). Main finding, conditional on the
preprint's unrefereed analytic lemmas and on Polymath's published boundary
computation: its derivative-kernel comparison (Theorem 12), started from
the strip M(0) ≤ 1 that every zero of ξ satisfies, gives Λ ≤ 0.18891 with
no zero-free half-plane as input. The 34-row table is checked in exact
rational and directed-rounding arithmetic. Planning: the same kernel
lowers Project 01's Target A values by 5–13%.

Open: an independent check of the preprint's Lemma 3 and Proposition 11
(the Codex audit), certification of note 01's evaluation, and H12 with the
comparison theorem (Project 01). The 16 October setup itself reported no
result.

Start with the [initial research proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
and the [portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md).
Codex leads the complete remainder budget; Claude audits imports, losses and consumer applicability. These are future model-family responsibilities; record the actual
model and effort when work is performed.

| Folder | Purpose |
| --- | --- |
| [research-overview](research-overview/README.md) | Numbered research proposals and decisions about priorities |
| [notes](notes/README.md) | Incremental derivations and one coordination note per phase |
| [numerics](numerics/README.md) | Reproducible code, parameters and small execution records |
| [reviews](reviews/README.md) | Separate assessments of claims, computations and scope |
| [source-documents](source-documents/README.md) | Reference provenance and links to canonical sources |
| [brainstorm](brainstorm/README.md) | Undeveloped candidate mechanisms with a decision question |
| [manuscript](manuscript/README.md) | A future stable manuscript after a reviewed milestone |
| [chat-histories](chat-histories/README.md) | Canonical records of new project-specific conversations |

The proposal states the opening deliverable, controls, dependencies and
stopping criteria. Its linked earlier results retain their canonical homes;
this project owns only the new work specified there.
Keep this status current at each accepted gate. See [draft history](DRAFT_HISTORY.md),
the [result summaries](../../../result-summaries/README.md) and
[patterns to avoid](../../../avoid/README.md).
