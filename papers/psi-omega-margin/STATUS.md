# STATUS — psi-omega-margin ("Paper 1")

**Title.** *The margin in the shifted screw-function criterion for zero-free half-planes*
(full, 21 pp.). **Concise companion:** *Quantitative asymptotics for Suzuki's shifted screw
functions* (9 pp.) — the intended submission.

**Stage.** Working draft. **Not released**: no tag includes this folder's sources as a released
manuscript, and no DOI covers them. Sources are committed as a working draft at the author's
request (8 September 2026), as an exception to the sources-only-when-released default recorded in
`../README.md`.

## Provenance and review record

Developed August 2026 with substantial language-model assistance under the author's direction.
Referee-style rounds 12–14, plus a full adversarial recheck (the "round 13" recheck) in which
every identity was re-derived from Suzuki's source and every numerical value independently
recomputed; the four next-step investigations were then carried out and folded in on 27 August
2026. The round-by-round record lives in the private project store; per the redaction checklist it
is to be mirrored under the repository's top-level `notes/` when that migration is done. The
mathematical substance of those notes is summarised, clean, in
`supplementary/DERIVATION_AND_VERIFICATION.md`.

## Verification status

- **Main results** (closed forms for A, B; the exact decomposition and damped remainder; the
  linear margin and its onset threshold; the critical-shift dichotomy; the sensitivity of the
  criterion to a violating zero): proved in-paper, and reproduced numerically by the scripts in
  `code/` — see `supplementary/DERIVATION_AND_VERIFICATION.md` for the mapping and the outcomes.
- **Two corrections** were made to an earlier draft during the recheck and are recorded in the
  derivation note (§4): the earlier "universal threshold u* ≈ 0.3748/ω" was withdrawn (vacuous as
  stated under RH, and Suzuki's §11 already gives pointwise non-negativity), and an error constant
  that was loose by a factor 2 was fixed. Both are corrected in the current sources.
- **Unconditional window:** rests on Platt–Trudgian (RH verified to 3·10¹²) and the explicit
  zero-free regions of Mossinghoff–Trudgian–Yang; the endpoint law is derived and numerically
  confirmed (`code/c5_window.py`, `code/c6_window_kv.py`).
- **Dirichlet / Selberg-class section:** the closed forms, prime-side formula, and Siegel-zero
  blindness are proved and checked for q = 3, 4, 5 (`code/c7_dirichlet.py`,
  `code/c8_prime_side_chi.py`); the general extended-Selberg-class conventions are aligned with
  Suzuki, arXiv:2209.12832. Zero locations for the tested characters are discharged by Platt,
  Math. Comp. 85 (2016).
- **Priority check:** Bombieri, Rend. Lincei 11 (2000), §8 was retrieved and machine-read (two
  passes); it does not pre-empt Suzuki's Theorem 1.7. A human skim of §8 is still advised before
  submission — see `supplementary/NEXT_STEPS.md` §4a.
- **No external human review yet.** The two genuinely new arguments — the phase-transition proof
  and the Dirichlet Siegel-blindness proposition — should have an independent human check before
  release.

## Redaction record

`supplementary/NEXT_STEPS.md` is a redacted copy of the project's next-steps note. Applied items
from `../../notes/REDACTION_CHECKLIST.md`: **1** (the draft letter to Suzuki removed, reduced to a
one-line description), **4** ("the author", not "the user"), **5** (internal `claude/…` paths and
session/tooling references rewritten to repository paths). `supplementary/DERIVATION_AND_VERIFICATION.md`
was authored clean for the repository. The tracking table in `REDACTION_CHECKLIST.md` has **not**
been ticked: that records human sign-off, which is still outstanding. The raw research-log notes
(the original derivation note and the round-13 recheck) have deliberately **not** been dropped
into this folder; their home is the top-level `notes/` migration.

## Blocking items before release

1. ORCID in the author block (author name and email are filled in both `.tex` files as of 9 Sept 2026; the papers carry no institutional affiliation by the author's decision); acknowledgements wording.
2. Human skim of Bombieri §8 (retire the machine-read caveat); independent human check of the
   phase-transition proof and the Dirichlet Siegel-blindness proposition.
3. `blueprint/` + `statements/ledger.yaml` entries; `VERIFICATION_STATUS.md` per the release
   checklist in `../README.md`; `CITATION.cff` and `.zenodo.json`; license stated.
4. One-pass renumbering of cross-citations against released companions (Papers 2–3); author
   sign-off on the redaction-checklist tracking table for the committed supplementary note.
5. Send (or decide against) the Suzuki letter (`supplementary/NEXT_STEPS.md` §4b).

## Companion dependency

Cited by Paper 2 (`../omega-string/`) for the margin asymptotics, the linear-margin bound, and the
critical-shift dichotomy; Paper 2 references the **concise** version here. Cross-citations in this
program carry statement names ("linear margin", "critical-shift dichotomy"), not theorem numbers,
so numbering may move before release without breaking references.
