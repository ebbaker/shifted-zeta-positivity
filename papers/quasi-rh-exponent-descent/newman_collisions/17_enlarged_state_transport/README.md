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
conditional certificate lemma. The continuation constructs regular tree
multipliers, proves sharp residual formulas and a restricted-prime
obstruction, and certifies one bounded physical cell. Uniform multiplier
bounds and signed theta correlations remain open.

Continuation record: GPT-6 (Codex), 10 October 2026; the active reasoning
effort is not exposed to this session and is not inferred.

## Entry points

- [Working manuscript](enlarged_state_transport_and_heat_flow.tex): exact
  structures, conditional visibility, sharp transport residuals, the
  primes 2 and 3 obstruction, and a bounded regular calibration.
- [Sharp adjoint residuals](notes/2_SHARP_ADJOINT_RESIDUALS_AND_RESTRICTED_PRIME_OBSTRUCTION_20261010.md):
  explicit tree witnesses, optimality and the effective obstruction for
  retaining only primes 2 and 3 when L is at least 160.
- [Bounded regular cell](notes/3_REGULAR_ADJOINT_CELL_CERTIFICATE_20261010.md):
  complete N=22066 outward certificate with paid margin greater than
  0.5552583, conditional on the imported disk interface.
- [Project overview and milestones](notes/1_PROJECT_OVERVIEW_AND_PROOF_TARGETS_20261010.md):
  conceptual direction, priorities, failure tests, and coverage obligations.
- [Reviews](reviews/): scoped internal checks and manuscript review.
- [Numerics](numerics/): project-specific experiments and small records;
  reuse the [shared exact checker](../13_microlocal_phase_space/numerics/check_enlarged_state_identities.py)
  and [identity record](../13_microlocal_phase_space/numerics/ENLARGED_STATE_IDENTITY_RECORD_20261010.json)
  rather than copying their sources.
- [Draft history](DRAFT_HISTOR.md): concise milestone index. Future
  milestones point to commits or tags; no manuscript snapshot folders.

The immediate continuation is a uniform correlated estimate for the
complete source, with a residual gap and controlled multiplier growth.
Unrestricted pointwise transport optimization exactly reproduces the
correlated first-jet test; the primes 2 and 3 alone cannot achieve the
printed residual gap at large scale. The bounded cell is a calibration,
and the same recorded subcells also pass separate scalar tests. The
parallel route seeks a theta-specific signed gradient/score correlation.
The shared algebra checker supplies finite exact controls, not a theta
sign or collision certificate. Keep research in `notes/`, computations in
`numerics/`, and reviews in `reviews/`, following the repository
[large-file policy](../../../../LARGE_FILES.md).
