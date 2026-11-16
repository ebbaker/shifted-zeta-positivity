# VCD-E07 r1 — finite canonical-score information control

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex assistance. Type E; parent B02 decision04. Helper explicitly requested gpt-6.1-sol/ultra; actual lead backend/effort unavailable. One fixed analytical construction and catalog screen, one correction pass; no numerics. Root owns shared files.

## Fixed question and route

At lambda=0, for any prescribed finite coefficient head and finite canonical-score matrix entries, can a distinct positive finite theta-mode perturbation preserve them exactly, while having nonreal Fourier zeros? Use f(u)=sum over a finite chosen set of modes m>=2 of c_m s_m(u) on u>=0, and the even extension. Impose homogeneous linear constraints preserving mass, sufficiently many even moments to fix the chosen q_n/a_n, and integrals V_theta'(u) q_i(u)q_j(u) for the specified finite i,j. Any finite extra real linear observations/endpoints may be included. More modes than constraints gives nonzero coefficients; prove independence of the finite modes and positivity after small scaling, and preserve the first mode. Invoke the inherited finite-source theorem section 3 with exact scope, not a fresh universal claim.

Additionally prove or qualify: both scores differ by a bounded function on the real line (a.e. if necessary), hence every canonical adjacent defect relative to n is O(log(n+2)/n) under the shared envelope, although the control has nonreal zeros. Arbitrarily small coefficient scaling should make the bounded score difference arbitrarily small for the fixed finite direction. The same canonical score is used throughout. This is not a claim that one nonzero perturbation matches infinitely many exact constraints; not a counterexample to compact shrinking strips or a growing-degree induction. State any finite smoothness preserved and the eventual loss of full smooth reflection explicitly.

Read result-summaries/README.md, avoid/README.md, catalog12, investigation manuscript source/envelope/score formulas, B02 decision04, E05 if available, and the pinned inherited source below. Screen every relevant catalog family: actual pass/fail/untested, not source-name differences. Establishing one actual member passing the chosen finite premises suffices to reject a universal zero claim from those premises.

Outputs only: notes/07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md and research-progress/handoffs/VCD-E07-r1-return.md. Completion is proof/corrected scoped failure plus control ledger. New conceptual obstacle returns to B03. No shared navigation/status edits or chat capture.

## Pinned sources
- `papers/investigations-6/03_volterra_coefficient_dynamics/brainstorm/notes/04_VCD_B02_SCORE_INFORMATION_DECISION_20261116.md` SHA-256 `6dc1ea4600f93f9c78451778c499c566f739fd36e9d55966d78f1255056b7d38`
- `papers/investigations-3/07_source_measurement_audit/notes/round-2/01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md` SHA-256 `4ea14decf622ce05110afafc56c991008f109cbca6f0a9fdb9d57c876ea79a71`
- `papers/investigations-6/03_volterra_coefficient_dynamics/manuscript/main.tex` SHA-256 `18346543517c374c5e55d095b6c6847a0ef21f2e18917fff428d54901cf60dcc`
- `result-summaries/12_collision_controls_and_screening.md` SHA-256 `116d99af6515c30d4ecc4a6485da35932d0e5062e7cb5d949f7c1f5f1b5a9e92`
