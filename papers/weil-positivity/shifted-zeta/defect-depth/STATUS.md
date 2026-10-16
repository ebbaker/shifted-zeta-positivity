# STATUS — defect-depth ("Paper 3")

**Title.** *Detection depth of spectral defects in shifted zeta strings.*

**Stage.** Working draft **v1**, 15 pp., dated 29 August 2026, produced immediately after the
Ihara-laboratory GO verdict (`ROUND6_closeout`). **Not released**: no tag includes this
folder's sources as a released manuscript, and no DOI covers them. Sources are committed as a
working draft at the author's request (9 September 2026), as an exception to the
sources-only-when-released default recorded in `papers/README.md`. (The folder slug is `defect-depth/`; some earlier planning
documents wrote `defect_depth/`.)

**Provenance and review record.** Developed August 2026 with substantial language-model
assistance under the author's direction, out of the finite graph-zeta laboratory ("Ihara
lab"): six investigation rounds (LAB_ihara rounds 1–5 plus the ROUND6 manuscript-gate
close-out), each with independent numerical recomputation and standing QC (control rows,
precision escalation, exact integer arithmetic where applicable). The round-by-round record
lives in the project notes (`LAB_ihara_round1`–`round5`, `ROUND6_closeout`; to be mirrored
under `notes/` per the redaction checklist).

**Verification status.**
- Theorem 1 (resolvent compactification: Taylor-jet identity, string-length invariance,
  contraction transform B = A(s₀+A)⁻¹): proved in-paper; moment lemma certified numerically
  at 8·10⁻¹³¹, operator lemma at 10⁻¹⁶ (`code/`, r5_w1 and round-5 inline runs).
- Theorem 3 (CF/Hankel first-anomaly index) and Theorems 4–5 (rank-one and rank-two
  Christoffel–Darboux determinant thresholds): proved in-paper; certified at 10⁻¹¹² and
  10⁻²⁸⁵/10⁻²⁷³ respectively (rounds 2–4).
- Theorem 6 (fixed-defect depth n_ε/log(1/ε) → 1/(2g) at ω > 0 via Stahl–Totik regularity)
  and Proposition 7 (quartet location and weight): proved in-paper; W1 table (8 cases,
  unfitted prediction column) reproduces it on the genuine broadened measure.
- Lemma A (signed a.c. cut correction does not preempt the atom threshold): proved in-paper
  by density domination; flagged in ROUND6 as the one drafting-time gap, now closed.
- Theorem 8 (zeta sensitivity, safe forms A and B) and Theorems 9–10 (time-domain envelope
  law ηt* = 2 log τ + loglog τ + log(S_ω/η) + o(1), and the envelope/first-negative bracket
  under transversality): proved in-paper; amplitude-2 certification at 10⁻⁸, constant
  convergence across τ = 10²…10¹², bracket verified at τ = 20…1280 (round-6 inline runs,
  recorded in `ROUND6_closeout`).
- The high-height τ² log τ/η law is stated as a proposition with numerics only (the
  documented discrete/continuum crossover; unscaled real-ζ table at s₀ = 200 included as an
  honest exhibit). The ω ↓ 0 uniformity is stated as an open problem.
- **17 bibliography entries still carry `%% VERIFY` markers** (release checklist item 2 not
  started). Figures 1–5 are placeholder comments; no figure scripts are committed yet.
- **No external human review yet.**

**Blocking items before release.**
1. Author block, ORCID, affiliation; acknowledgements.
2. Bibliography verification (remove all 17 `%% VERIFY` markers against sources).
3. Companion citations are placeholders (`MarginPaper`, `StringPaper`, `ROUND6`,
   `LabRecord`): renumber/resolve against the actually released companions and the mirrored
   notes, per the cross-citation policy in `papers/README.md`.
4. Generate Figures 1–5 from committed scripts.
5. The round-6 inline verification scripts (amplitude certification, s₀ five-point scan,
   unscaled real-ζ suite, bracketing runs) are recorded in `ROUND6_closeout` but were not
   saved as standalone files; reconstruct them into `code/` before release.
6. `blueprint/` + `statements/ledger.yaml` entries; `VERIFICATION_STATUS.md` per the release
   checklist in `papers/README.md`.
7. Human specialist review.

**Companion dependency.** Cites Paper 1 (`../psi-omega-margin`) for the margin slope
(ξ′/ξ)(½+ω) and the linear-margin bound, and Paper 2 (`../omega-string`) for the shifted
zeta-string construction and its Weyl function; citations carry statement names pending
release of both.
