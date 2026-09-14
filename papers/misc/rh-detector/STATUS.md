# STATUS — rh-detector

**Title.** *A certified velocity-residual detector for off-axis zeros of the Riemann
Ξ-function, and the De Bruijn–Newman flow as a matrix pencil on Calogero–Moser space.*

**Stage.** Working draft, 10 pp., dated 25 August 2026. **Not released**: no tag includes
this folder's sources as a released manuscript, and no DOI covers them. Sources are
committed as a working draft at the author's request (9 September 2026), as an exception to
the sources-only-when-released default recorded in `papers/README.md`. (This folder was
listed as `offaxis-detector/` in earlier planning documents; the slug is `rh-detector/`.)

**Provenance and review record.** Developed August 2026 with substantial language-model
assistance under the author's direction, in the detector thread of the RH3 project
(project notes `NOTE_offaxis_detector`, `NOTE_pencil_and_DBN`,
`ROUND3_verification_and_detector`, `ROUND4_certificates_and_edge_law`; to be mirrored
under `notes/` per the redaction checklist). This thread is **separate from Papers 1–3
and the first-slab preprint**: it was written on 24–25 August 2026, *before* the Suzuki
line of work began, and is unrelated to that program; the manuscript carries no companion
cross-citations.
The original session workspace was lost in a service outage around 24–25 August 2026;
every script in `code/` was regenerated from the notes' specifications on 25 August and
every number appearing in the paper was recomputed fresh in that session. The regenerated
1001-ordinate zeta cache matches the author's saved copy of the original digit-for-digit,
and the Dirichlet-beta null test run on the author's original 70-zero cache reproduces the
recorded residuals. Scripts re-run under the pinned environment on 9 September 2026
(smoke tests: `v1_pencil.py`, `h3_certified.py`; outputs unchanged).

**Verification status.**
- Lemma 2.1 (velocity identity) and Lemma 2.2 (multipole sign discriminant): proved
  in-paper; elementary.
- Certified null test (Table 1): recomputed 25 Aug at K = 1000 with the exact
  Riemann–von Mangoldt decomposition, the exactly computable boundary term
  S(U) = +0.153426, and Trudgian's unconditional |S(u)| bound; observed residuals ~10⁻⁷
  against certified bands ~10⁻³. **Certificates are rigorous modulo floating point** —
  high-precision arithmetic (mpmath, 25–30 digits), not interval arithmetic.
- Certified thresholds (§4.2): pure threshold arithmetic from the Table 1 bands;
  recomputed 25 Aug.
- Synthetic injections (Table 2): double-precision fits; correct model and parameters
  recovered in all four cases, empty control at machine zero; recomputed 25 Aug.
- Theorem 5.1 (pencil identity = Wilson's tau-function formula, with the De Bruijn–Newman
  reading): full ODE-uniqueness proof in-paper; identity verified numerically for
  n = 2…7 (relative coefficient error ≤ 5·10⁻¹²), Λ(z²+y₀²) = y₀²/2 and the unit-variance
  Hermite benchmark −1/(2(d−1)) reproduced, five k = 2 thresholds matched against direct
  root tracking to 2·10⁻¹¹.
- Margin meter (Table 3): pencil thresholds with and without the local zero environment;
  recomputed 25 Aug.
- Dirichlet beta port (§6): 70 zeros by sign scanning; residuals with the
  **uncertified** smooth-density tail only; the certified version needs the χ-analogue
  of the exact θ/π + 1 + S decomposition and explicit |S(u,χ)| constants.
- Attribution: the pencil identity itself is Wilson's (Invent. Math. 133, 1998; stated in
  determinantal form in Kasman–Milson–Gekhtman, SIGMA 22 (2026) 036); the paper claims
  only the De Bruijn–Newman reading (Corollaries 5.2–5.3). This reading was not found in
  the De Bruijn–Newman literature, but the search (25 Aug, conversational web search) was
  **not exhaustive**; the Csordas school in particular deserves a systematic pass.
- Bibliography entries were verified against sources/arXiv conversationally on 25 Aug;
  no `%% VERIFY` markers, but release checklist item 2 (systematic re-verification)
  has not been performed.
- **No external human review yet.**

**Blocking items before release.**
1. Author block, ORCID, affiliation; finalize acknowledgements wording jointly with the
   companion papers.
2. Systematic novelty search for Corollary 5.2 (Λ as pencil reality threshold) in the
   De Bruijn–Newman and hyperbolicity-preserver literature (Csordas–Norfolk–Varga,
   Csordas–Smith–Varga and successors).
3. Interval-arithmetic (e.g. Arb) port of the certificate pipeline (V_j, theta integrals,
   ε_j) — mechanical but required before the word "certified" is used without the
   floating-point caveat.
4. Explicit |S(u,χ)| constants and exact counting decomposition for the certified
   Dirichlet-L port of §6.
5. Systematic bibliography re-verification (release checklist item 2).
6. `blueprint/rh-detector/statements.md` + `statements/ledger.yaml` entries;
   `VERIFICATION_STATUS.md`, `CITATION.cff`, `.zenodo.json` in this folder.
7. Human specialist review.
