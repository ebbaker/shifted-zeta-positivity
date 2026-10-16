# Physical channels: WZW pilot, the collar theorem, YM obstructions, the through-defect network

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

- **SU(2)\(_2\) WZW pilot identities.** The deterministic Loewner reduction
  \(\dot M=-\nu(2Q^2+\dot uQ)M\) with its balance equation; the generator
  matrices; Cardy-state growth \(0.436388495438834\) at \(\dot u=4\); the KZ
  blocks; \(G_s+G_o=2n_\gamma\); \(c_n=J_{2\omega}(n)/n^{\omega+1/2}\); and the
  anomaly coincidence \(\nu/4=c/24\) only at level \(k=2\). Verified in the
  cross-model review (40 cases).
- **The collar theorem.** A bounded, self-adjoint, causal scalar operator is
  a multiplication operator, so no reflected readout can equal the transfer
  \(V\). "Airtight", with the framing corrected: it excludes building
  \(V\) by reflection, not the form \(Q\).
- **YM obstructions N1–N4.** Logarithmic ultraviolet growth; no bounded
  intertwiner from the class sector to the Bost–Connes module; an
  absolutely continuous current; the tested positive prime completion has
  domain \(\{0\}\). A four-question filter for any physical candidate.
- **The through-defect reflection network: what holds and what does not.**
  The free off-diagonal kernel is exactly \(n_\gamma\) and all kets share
  the bulk charge; but Gram positivity is only conditional on OS positivity
  under the reflection, the continuum norm diverges, and the same-model
  review says "do not yet promote the positive-pairing claim". Proved
  instead: the smeared covariance is positive, \(M_\rho I-T_\rho\to b(-\partial^2)\),
  and the contact-subtracted covariance is negative and cannot be fixed by
  any finite contact term (Proposition "The sign of the subtraction").
- **N=4 SYM.** The straight-line channel is closed as an arithmetic
  candidate; the finite-mass channel fails the front-and-tangent test;
  "no scale, so no fixed delays".

## Status

Pilot identities: "specialist review outstanding" in the note, "verified"
in the cross-model review. Collar: proved. YM: "proof", with scopes
narrowed by the errata of the cross-model verification; "Closure of the
program is a research judgment, not a theorem". Network: the positive
pairing is unproved.

## Caveats

The WZW closure was recommended on 24 September (four sibling results
jointly supersede it) but was parked, not executed, and no closing note
exists. The "fourth diagram" question in Wilson lines is really the
uncomputed cross-arc exchange and piercing-point terms; "Only their sum can
be the full gauge-independent interacting response." A positive state space
is not a causal contraction; a symmetry of the action is not OS
reflection; matching one factor (the Haar measure on one copy of SU(2), the
Robin Gaussian) is not realizing the target.

## Reusable for

A finite BCFT benchmark; the collar theorem as a "name the target first"
lemma; the N1–N4 filter; the sign-of-subtraction rule for any Gram
construction.

## Where

- Pilot: [SU(2) level-2 pilot](../papers/susy-positivity/investigations/wilson-loewner/notes/SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md); [WZW program assessment (cross-model)](../papers/susy-positivity/investigations/wilson-loewner/WZW/reviews/review_claude_wzw_program_assessment_20260924.md); [records](../papers/susy-positivity/investigations/wilson-loewner/WZW/numerics/records/wzw-program-review-20260924.json).
- Collar: [bounded arithmetic readout test](../papers/susy-positivity/investigations/wilson-loewner/WZW/notes/BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md); [lessons from WZW](../papers/susy-positivity/investigations/wilson-loewner/notes/LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md); [cross-program priorities](../papers/susy-positivity/investigations/wilson-loewner/notes/CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md).
- YM: [README](../papers/susy-positivity/investigations/wilson-loewner/YM/README.md), [structural requirements](../papers/susy-positivity/investigations/wilson-loewner/YM/notes/STRUCTURAL_REQUIREMENTS_AND_NEXT_STEPS_20260925.md), [cross-model verification](../papers/susy-positivity/investigations/wilson-loewner/YM/reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md), [reply](../papers/susy-positivity/investigations/wilson-loewner/YM/response/CLAUDE_REPLY_TO_RESPONSE_20260925.md), [electric and buffered obstructions](../papers/susy-positivity/investigations/wilson-loewner/YM/notes/FULL_ELECTRIC_AND_BUFFERED_SOURCE_OBSTRUCTIONS_20260926.md).
- Network: [free kernel](../papers/susy-positivity/investigations/wilson-loewner/sections/03_free_kernel.tex), [reflection](../papers/susy-positivity/investigations/wilson-loewner/sections/08_reflection.tex), [reflection junction](../papers/susy-positivity/investigations/wilson-loewner/notes/REFLECTION_JUNCTION_AND_BULK_RESPONSE_20260919.md), [statement ledger](../papers/susy-positivity/investigations/wilson-loewner/sections/10_outlook.tex), [N=4 SYM README](../papers/susy-positivity/investigations/wilson-loewner/N4SYM/README.md).
