# Arguments whose premises the controls also satisfy

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

An argument for the theta sign uses only properties that a known
colliding source also has: positivity, evenness, decay, moment positivity,
the Jacobi heat equation of the mode sum, Hecke relations at finitely many
primes, a positive-definite Gram form, radial positivity. Such an argument,
if it worked, would prove a false statement for the control; so it cannot
work, and any identity valid on the shared class can only move the
unknown sign, never fix it.

## What it looks like here

Exact identities (associators, bilocal kernels, covariant jets, Hecke
correspondences, dictionary entries between two realizations) presented as
"cancellations" or "constraints", with a remark that the sign remains
open; positive constructions in which "nothing in the model selects
primes"; winding counts and radial positivity that hold for every even
measure.

## Evidence

- [19's initial program](../papers/investigations-2/active/19_euler_factor_controls/notes/INITIAL_RESEARCH_PROGRAM_20261013.md): "An exact identity that every control also satisfies is a rewriting, not a constraint."
- R1 of the [11 October brainstorm](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md): "No shape-only argument can work."
- [Inverse-bulk review](../papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/reviews/review_claude_opus_5_20260915.md): "nothing in the model selects primes — \(r=p^{-1/2}\), \(d=\log p\) are inserted by hand"; the [exclusion map](../papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/notes/EXCLUSION_MAP_20260917.md) concludes that a prime weight in a positive sector "should no longer count as evidence".
- [Review of the lifted theta directions](../papers/investigations-2/brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md) §4: the Lagarias–Li Hecke relations are no constraint because "\(\Phi_{c,p}\) satisfies all of them".
- [Reply 18](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md) §3: no single listed property is absent from all four controls; square support and reflection are each satisfied by two of them, and their conjunction is theta itself.
- [Close-and-merge recommendations](../papers/investigations-2/active/CLOSE_AND_MERGE_RECOMMENDATIONS_CLAUDE_20261013.md) on folders 14 and 16: "The Volterra flow holds for every even measure" and radial positivity "is Bochner positive-definiteness of \(H_t(|z|)\), which is generic".

- [Finite-prime orbit controls, 18 October](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md):
  "No single perturbed source is claimed to pass every prime or every endpoint
  condition." Each fixed finite prime list, even with exact infinite coefficient
  compatibility at those primes and finite exact linear tests, still admits
  colliding sources; complete reflection is the failed premise. This does not
  exclude a controlled infinite assembly or finite formulas using full theta
  data. Added for Edward Baker with substantial LLM assistance, **gpt-6-astra,
  max**; [same-assistant assessment](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/01_OPENING_ROUND_SELF_REVIEW_CODEX_20261018.md).

- [S04-T2 Note 02](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md) explicitly limits its new
  phase-matched energy floor: “an averaged energy bound may hold at a
  source's isolated collision.” The source-specific RS premises justify
  the average, while energy-to-pointwise exclusion still needs an
  additional argument. Entry added 19 October 2026 for Edward Baker with
  substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.

- [S06-T1 Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/03_SECOND_TRANSVERSE_COMPLETION_AND_CURRENT_FEASIBILITY_20261019.md), 19 October 2026:
  “At a nondegenerate physical collision the observation is nonzero and
  the centered current is strictly positive.” Completion and a favorable
  auxiliary current do not by themselves make a collision test. The
  reflected source has convergent differential completion and E=0;
  canonical theta arithmetic is its failed premise. This screens the
  stated current-sign/generic energy-payment attempt, not theta-specific
  estimates. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/reviews/04_SECOND_TRANSVERSE_COMPLETION_INTERNAL_REVIEW_20261019.md). Added for Edward
  Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.

## What it cost

The 09-to-06 continuation, 02's continuation and 17's pilot ended at
unchanged gates; the inverse-bulk Theorem 6.2 was rated "a dictionary
entry"; the octonionic and hyperkähler sections of 21–22 were found
sign-blind by their own text.

## Instead

Run the controls before writing the note: \(\Phi_{c,p}\) for all \(p\)
([19's screening corollary](../papers/investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex)), the weighted-square and reflected controls of 22, the counter-kernels \(q\) and \(q_{T,a}\) of the collision manuscript, the smooth-density and two-channel controls of the SUSY packages ([result-summaries 12](../result-summaries/12_collision_controls_and_screening.md), [04](../result-summaries/04_positive_constructions_and_scoped_obstructions.md)). State which premise each control fails; if none, the argument is a rewriting. This is house rule 1 of [`CONTRIBUTING.md`](../CONTRIBUTING.md) ("run the control") and rule 3 of the [investigations-2 README](../papers/investigations-2/README.md): "Model tests must preserve the hypotheses they challenge."
