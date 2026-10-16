# Continuation note, 17 September 2026

**Author: Claude Opus 5 (Anthropic).** Context note for the inverse-bulk
investigation. It records what this session covered and the state it found, and
**deliberately proposes no next steps**: the investigator is opening a new
direction in a separate session, and this note is not to prejudge it. The
ordered programme as it stood is in
[CONTINUATION_20260915.md](CONTINUATION_20260915.md) (read its section 0 first)
and in [NEW_SESSION_PROMPT.md](NEW_SESSION_PROMPT.md); nothing here supersedes
either.

## 1. What this session was

A reading session, not a calculation session. No manuscript source, check
programme, record or snapshot was modified. Two notes were added: this one and
[EXCLUSION_MAP_20260917.md](EXCLUSION_MAP_20260917.md).

The session read the investigation README, the 15 September handoff and new-
session prompt, the exclusion, pole-term, mirror-dressing and subtraction-form
notes, sections 2, 7 and 8 of the manuscript source, and the relevant sections
of the analysis, gauge-transfer and sphere/Schur notes. It then produced, on
request, a synthesis of everything the investigation has excluded — organised by
kind of argument rather than by chronology, with each scope clause made explicit
— for the purpose of seeing where the loopholes are. That synthesis is the
exclusion-map note.

## 2. State found in the repository

- The working manuscript is at **version 0.6**, 42 pages, built 16 September:
  corrected saturation figures in Section 7.6, Remark 7.12 on Suzuki's
  unconditional small-interval results, and Section 7.7 carrying the jump form
  (Prop. 7.13) and the necessary condition (Prop. 7.14).
- `BUILD_RECORD.json` at the investigation root is **stale**, so
  `validation/drafts.py check` fails here; `drafts/2026-09-16-v06/` is present
  but untracked in git. Recorded as state, not as an action item.
- The 16 September work spun off a separate investigation,
  `papers/susy-positivity/investigations/previous/source-selection-rules`, whose
  manuscript 0.1 is *A jump-process presentation of the localized Weil form* and
  which carries its own continuation note. That investigation is where the jump
  form and the Collatz-Wielandt necessary condition are developed.
- The notes in this folder and manuscript 0.6 agree; the 15 September handoff
  describes 0.5 and predates the three changes listed above.

## 3. What came out of the conversation

Two things that were not in the notes before, both recorded in the exclusion-map
note with their status:

**(a) Theorem 7.5 excludes a particular pair of channels, not two-channel
architectures.** Reading the interference bound as
`|A[f] - B[f]| <= sqrt(Q_L[f])(sqrt(A[f]) + sqrt(B[f]))` shows the two channel
norms must agree to within `sqrt(Q_L)`, so each would have to carry roughly half
of everything. The symmetric split `A' = B' = (K + sum_p B_p)/2` satisfies the
bound identically, and — given `Q_L >= 0` and `-R_L >= 0`, the second by a
one-line Cauchy-Schwarz criterion that holds with a wide margin at every `L`
evaluated — admits maps `G, S` with those channel norms and
`\|(G+S)f\|^2 = Q_L`. The construction is an abstract Gram space and uses RH on
`I_L`, so it establishes nothing arithmetic; it bounds what Theorem 7.5 may be
quoted for. Section 3.3 of the exclusion-map note carries the proof and the
verification table.

**(b) One soft spot in the exclusion chain, and one untested corner.** The
`alpha`-scan of section 5 of the exclusion note — the repair in which each
channel absorbs a constant and a share of the pole term — is numerical evidence
only, with a floor at `5e-8` that is the discretisation; making it a theorem
needs a rigorous lower bound on `lambda_min(Q_L)` against the fixed difference
form. That scan moved constants and pole shares between channels but never an
operator share of the gamma energy or of the prime references, so the family
`A' = K - M`, `B' = sum_p B_p + M` with `M` a positive form is untested — and by
(a) it is the family the bound is least able to constrain.

Neither point changes any published statement. Theorem 7.5 is correct as stated
and scoped; the manuscript already says the exclusion is specific to the pair
`(K, sum_p B_p)` and that a source not separated into two channels is untouched.

## 4. The rest of the session

The remainder was exposition of material already recorded: the two facts that
power the exclusions (the spectral smallness of the target, and the rigidity of
Corollary 2.2), the four families of argument — positivity on a subspace,
the interference bound, kernel-support and atom arguments, and
domain/boundedness arguments — the two exclusions that were themselves withdrawn
and why, and the live surface that no argument touches. All of it is in the
exclusion-map note in the same order.
