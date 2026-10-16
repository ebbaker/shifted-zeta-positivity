# STATUS — omega-string ("Paper 2")

**Title.** *The shifted zeta string: an unconditional inverse-spectral family and its RH
endpoint.*

**Stage.** Working draft **v5**, 13 pp., frozen 28 August 2026 pending human specialist
review. **Not released**: no tag includes this folder's sources as a released manuscript, and
no DOI covers them. Sources are committed as a working draft at the author's request
(8 September 2026), as an exception to the sources-only-when-released default recorded in
`papers/README.md`.

**Provenance and review record.** Developed August 2026 with substantial language-model
assistance under the author's direction; five adversarial referee-style passes
(rounds 15–19), each with independent numerical recomputation. The full round-by-round
record lives in the project notes (`ROUND15`–`ROUND19`; to be mirrored under `notes/` per the
redaction checklist).

**Verification status.**
- Theorems 1.1, 1.2, 1.5, 1.6(i), 1.6(ii) and Remarks 6.1, 6.3: proved in-paper; key steps
  (residue lemma, Fourier block, convergence tables, endpoint length) reproduced by the
  scripts in this folder.
- Theorems 1.3, 1.4, 1.6(iii): rest on Kasahara, Japan. J. Math. 1 (1975) — Theorem 2 +
  Example 1 (D_{1/2} = 1) and Theorem 1 respectively — **source-verified against the original
  paper** (8 Sept 2026 session; hand-obtained PDF), including constants, endpoint orientation,
  and the h(s) = q(−s) and left-continuity conventions.
- Numerical sections: the six spectral-formula checks and the discrete-inverse (Herglotz
  peeling) results are as recorded; the peeling pipeline itself ran in an earlier session
  workspace and is scheduled for the numerics-polish pass (see paper, Open Problem 3).
- **No external human review yet.**

**Blocking items before release.**
1. ORCID in the author block (author name and email filled as of 9 Sept 2026; no institutional affiliation by the author's decision); final acknowledgements wording (the source still carries the placeholder "[Complete as appropriate.]").
2. One-pass renumbering of all `\cite{Margin}` references against the actually released
   companion (Paper 1) — citations carry statement names for exactly this purpose.
3. `blueprint/` + `statements/ledger.yaml` entries; `VERIFICATION_STATUS.md` per the release
   checklist in `papers/README.md`.
4. Human specialist review (outreach in progress).

**Companion dependency.** Cites Paper 1 (`../psi-omega-margin`, concise version,
"Quantitative asymptotics for Suzuki's shifted screw functions") for the margin asymptotics
(Thm 2.4), the linear-margin bound (Cor 3.1), and the critical-shift dichotomy (Thm 3.4);
numbers current as of the 28 Aug project copy of the concise draft.
