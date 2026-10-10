# 17. Enlarged-state transport and heat-flow visibility

Prepared for Edward Baker with substantial LLM assistance, 10 October 2026.
Model: GPT-6.1-sol (Codex), reasoning effort ultra, verified from the
recorded drafting-turn configuration. Internal LLM checks are not
independent mathematical validation.

This project joins program 09's prescribed arithmetic transport with
program 13's coherent chord dynamics, retaining theta preparation and
matched boundary channels. Its principal target is an effective first-jet
source-to-observation bound excluding genuine heat-flow collisions on a
specified domain. The initial results are exact identities and a
conditional certificate lemma; useful bounded multipliers and signed
theta correlations remain open.

## Entry points

- [Initial manuscript](enlarged_state_transport_and_heat_flow.tex): compact
  self-contained derivation, conditional visibility certificate, and proof
  targets.
- [Project overview and milestones](notes/1_PROJECT_OVERVIEW_AND_PROOF_TARGETS_20261010.md):
  conceptual direction, priorities, failure tests, and coverage obligations.
- [Reviews](reviews/): scoped internal checks and manuscript review.
- [Numerics](numerics/): project-specific experiments and small records;
  reuse the [shared exact checker](../13_microlocal_phase_space/numerics/check_enlarged_state_identities.py)
  and [identity record](../13_microlocal_phase_space/numerics/ENLARGED_STATE_IDENTITY_RECORD_20261010.json)
  rather than copying their sources.
- [Draft history](DRAFT_HISTOR.md): concise milestone index. Future
  milestones point to commits or tags; no manuscript snapshot folders.

The immediate continuation is a regular adjoint-transport construction
with a complete residual gap and controlled multiplier growth. The
parallel route seeks a theta-specific signed gradient/score correlation.
The shared algebra checker supplies finite exact controls, not a theta
sign or collision certificate. Keep research in `notes/`, computations in
`numerics/`, and reviews in `reviews/`, following the repository
[large-file policy](../../../../LARGE_FILES.md).
