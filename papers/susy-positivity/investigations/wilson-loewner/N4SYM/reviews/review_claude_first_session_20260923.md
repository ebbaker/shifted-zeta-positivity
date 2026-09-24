# Same-assistant audit of the first N4SYM session (23–24 September 2026)

**Model:** Claude Opus 5.5 (Anthropic), model identifier `claude-opus-5-5` as reported by the runtime (session configuration `claude-fable-5-1`; the serving model can differ). Reasoning effort not exposed.  
**Kind:** an internal audit by the assistant that did the work, plus a separate referee context of the same model. This is **not** an independent specialist review.  
**Scope:** [straight-line response and trace completion](../notes/STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md), [flipped-return analysis](../notes/FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md), and the three check programs in [`../numerics`](../numerics/README.md).

## 1. Referee pass

A separate context was told to be adversarial and to re-derive rather than inherit. It did not use the author's programs; it used its own sympy, mpmath and scipy scripts. It re-derived eleven items of the first note. Nine were confirmed as stated: the Proposition 1 coefficients and Zarembo cancellation, the tree-level signs, the Proposition 2 commutator and χ_R, the total work, the tilt resistor, Loewner scaling, the sliver constants and cusp coefficients, the flipped first equation (with its own SU(2) finite-difference check), and the short-time coefficients. For the remaining two, Propositions 4 and 5, the formulas were confirmed but the report found errors in the surrounding proof steps and hypotheses.

The referee reported these errors, and all have been corrected in the note:

1. **Wrong mechanism for locality.** The note attributed it to Huygens' principle. It follows from one-dimensional conformal symmetry and the integer dimension Δ_D = 2, which holds for line defects in any bulk dimension.
2. **Proposition 4 proof step.** "The bracket is O(Ω⁻⁴)" was wrong for the quantity used. Ω²|F_T|² − ḣ² is O(Ω⁻²), which is still integrable. The same expansion gives the O(log Λ/Λ) rate analytically, so the rate is now proved rather than observed.
3. **Proposition 5 hypothesis and flat onsets.**
   - The hypothesis was stated two-sided, which is incompatible with h ≡ 0 before the onset. It is now stated with one-sided regularity.
   - "Flat onsets diverge" was false: for e^{−1/x^α} the ratio ḣḧ/∫ḧ² tends to 2, so negativity persists.
   - "Every smooth drive" was false: an oscillating C^∞ onset gives a counterexample.
4. **Transfer-function sign.** With ω = ip, pχ(p) = −m_Rp³ + 2πBp⁴, not +m_Rp³. The tilt channel's χ^Φ(p) is −2πBp.
5. **Dimensional remark.** "Tip insertion suppressed by a relative factor s" was dimensionally loose, since γ/|k| = a/12 carries units.
6. **Overclaims in Proposition 1.** Positivity in h and exact vanishing on the Zarembo profile hold for c_R = 0. Hypothesis (b) now allows a finite renormalization condition.
7. **Ledger inconsistencies.** The ledger and text disagreed on the status of the cubic term, and Propositions 2–3 depend on the same axioms as Proposition 1. Both are now stated consistently.

The referee also noted that the weak-coupling antiparallel coefficient has O(λ² log λ) corrections; this is corrected. It also noted that the tilt cutoff remainder is O(ω² log(Λ/ω)/Λ); this is corrected.

## 2. What the author re-checked

- **Units and normalizations.** B₁ = g²C_F/(8π²), from the one-loop expansion of (1/N)tr P exp, is consistent with CHMS eq. (2) at leading order.
- **Program independence.** Each program checks an analytic statement by a route that does not reuse the formula being tested:
  - finite differences of propagators for the tree-level signs;
  - the Hadamard finite part versus the Fourier side;
  - the exact one-loop kernel versus the quadratic formula;
  - directly integrated transports versus insertion formulas;
  - the flowed Feynman integral versus the interacting short-time formula.
- **Tip series.** It was re-derived independently and agrees with all twelve coefficients in the parent record.
- **Determinism.** Each program gives identical output on repeated runs in the cloud workspace. The device runs are recorded separately.

## 3. Residual concerns for a specialist

- **Proposition 1 axiom (b).** It encodes the standard defect-CFT expectation that contact terms are polynomial with regulator-power coefficients. A specialist should confirm that no additional scale enters the Maldacena–Wilson contact terms, for example through the unprotected Φ⁶ insertion at finite coupling.
- **Reflection symmetry.** The ten-dimensional reflection that kills the cubic term is cited, not derived.
- **The a → −a symmetry.** The step "charge conjugation plus orientation reversal plus reflection" should be written out with the fermions.
- **Section 5 of the flipped note.** The thin-sliver erf law is a leading-order approximation. The regime boundaries are stated only up to constants.
- **Near-BPS coefficient H(λ,N).** It is flagged as open. The remark about the near-BPS formula is a hint, not an argument.
- **Literature citations.** The four-point-function references and Drukker–Forini were cited from memory. CHMS equation numbers came through an automated fetch summary. Both should be confirmed by eye before any manuscript use.

## 4. Repository hygiene

- **Package check.** `validation/check_package.py check` already failed at `8b22141`, with six inventory mismatches from the committed proposal. The new files add further mismatches. `refresh` was not run, because it rewrites the curated author and scope fields of `PACKAGE_RECORD.json`. Refresh deliberately when convenient, then restore those fields.
- **Manuscript registration.** No program is registered in `validation/drafts.py`, because N4SYM has no manuscript.
- **Commits.** Nothing has been committed.
