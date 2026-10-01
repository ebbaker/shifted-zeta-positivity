# Initial manuscript: provenance and scope

30 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Exact serving variant and configured reasoning effort were not exposed; neither is inferred.

## Source state

The source investigation was read at repository commit eb8fb0a707785285946276f0ff08cb0acbadb3c5, with no pre-existing working-tree changes reported. The manuscript is a new synthesis, not an independently refereed result.

Original research and review files remain in the Wilson–Loewner arithmetic-storage investigation.

| Manuscript material | Principal research source |
|---|---|
| Phase conventions, bounded causal transport, and strong endpoint collapse | [Regularized positive family](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_REGULARIZED_POSITIVE_FAMILY_20260929.md) |
| Exact metric, block identities, boundary resolvent, and Abel approximation | [Phase boundary trace](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PHASE_BOUNDARY_TRACE_20260929.md) |
| Uniform unit-window mass and full Schwartz source tails | [Frequency tails](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PHASE_FREQUENCY_TAILS_20260929.md) |
| Critical localization, endpoint return measure, rational example, and Abel crossover | [Critical boundary model](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CRITICAL_BOUNDARY_MODEL_20260929.md) |
| Pole and zero crossings; non-even complex sources | [Arithmetic crossings](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PHASE_ARITHMETIC_CROSSINGS_20260929.md) |
| Combined scope and remaining exact-projection issue | [Critical-limit synthesis](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CRITICAL_LIMIT_STATUS_20260929.md) |

Relevant prior internal checks:
[phase-boundary review](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/reviews/SONIN_PHASE_BOUNDARY_TRACE_REVIEW_20260929.md) and
[critical-limit review](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/reviews/SONIN_CRITICAL_LIMIT_REVIEW_20260929.md).
These are LLM-assisted internal checks, not independent specialist verification.

## Consolidation decisions

- Keep one self-contained manuscript, including bibliography, so the native LaTeX editor can compile it without extra project files.
- State the actual projection and its inverse compressed metric explicitly.
- Prove the unit-window estimate on every bounded sigma strip, extracting the pole factor as well as the zero factors.
- Use the unit-window bound for phase variation to justify the full-source contour passage. The parallel Hadamard-product proof in the source crossing note is not repeated.
- Extend the operator statements to arbitrary Schwartz frequency multipliers where the proofs already apply; compact smooth position sources follow by Fourier transform.
- Define the complete arithmetic form for general sources with its explicit pole term. For prepared sources this reduces to the form in the original synthesis.
- Keep the rational comparison model separate from assertions about the actual global zeta phase.
- Keep finite-prime certificates, scalar traces, and compressed-moment calculations in their original research records. They are not needed in the proofs of this manuscript.
- Do not assert a universal coupled Abel schedule, exact-projection convergence, a semilocal prime-cutoff limit, or RH.

## Attribution and publication work remaining

The manuscript cites Connes–Consani's archimedean trace correction, their quasi-inner framework, Connes–Consani–Moscovici's semilocal transport, Burnol's Sonine-space work, Connes's earlier spectral interpretation, and standard two-subspace algebra. The scalar explicit formula and the abstract projection identities are treated as background techniques.

The proposed contribution is the particular phase family's uniform estimates and critical-boundary analysis. A complete theorem-by-theorem priority comparison with Hardy/model-space and Hankel-operator literature remains necessary before a submission. No first-in-the-literature claim is made.

The author field says “Drafted for Edward Baker.” The acknowledgement records substantial GPT-6 (Codex) assistance and the outstanding author verification. Future manuscript milestones should update the draft history using commits or tags. This drafting task does not create a commit, tag, release, or arXiv submission.
