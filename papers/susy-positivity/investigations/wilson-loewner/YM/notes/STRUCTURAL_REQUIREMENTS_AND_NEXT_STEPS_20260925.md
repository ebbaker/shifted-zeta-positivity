# Structural requirements extracted from the YM obstructions, and next steps for the program

25 September 2026. Prepared for Edward Baker by Claude (Anthropic). Model line: claude-fable-5-1 (Fable 5.1) per the runtime environment, session configured as claude-opus-5-5; the serving model may differ. Reasoning effort not exposed.

Companion to the [independent review](../reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md) of the consolidated manuscript. Everything in Section 1 is a direct corollary of theorems proved in the manuscript and rederived in the review; Sections 2–4 are recommendations and are labelled as such.

**Revised 25 September 2026** after the [GPT-6 response](../response/RESPONSE_TO_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md) and my [reply](../response/CLAUDE_REPLY_TO_RESPONSE_20260925.md). The first version stated four conditions R1–R4 more generally than the manuscript proves; Sections 0–2 below are the corrected version (N1–N4). Sections 3–4 are unchanged except for the softened expectation in the filter pass.

## 0. Summary

The YM investigation did not produce a Yang–Mills realization of the Weil form, and the two limits that build its signed identity are independent of the Yang–Mills state. What it did produce is four proved obstruction theorems, each excluding a specified class of mechanisms; stated with their exact scopes (Section 1) they are necessary conditions that any candidate must be checked against, not a proof that no candidate exists. The two remaining physics threads (N4SYM, WZW/Bost–Connes) should be checked against them in one short session before further investment, with the understanding that passing all four validates nothing. The certified arithmetic line (weil-depth, storage-depth, arithmetic-storage, canonical systems) is where the program has cumulative, verifiable results, and it should receive the effort.

## 1. Four necessary conditions (proved, with their exact scopes)

Notation as in the manuscript: 𝒟⁰ the pole-neutral tests, Q the Weil form (1.5), U_t translation in the logarithmic variable, f_λ the modulations (1.11), whose L² norms tend to ‖h‖₂.

**N1 — Logarithmic ultraviolet growth of the source norm** (Proposition 1.2). Any J with ⟨Jf, Jg⟩ = Q(f, g) satisfies ‖J f_λ‖² = ‖h‖² log|λ| + O_h(1). Consequently no law bounded on a fixed support by an ordinary input norm, ‖Jf‖ ≤ C_I‖f‖_∞ (or the L¹, L² analogues), realizes Q; in particular no smearing ∫ f(x)A(x)dx with locally integrable ‖A‖, and no direct sum of such laws with square-summable constants. *Scope.* Derivative-type laws are not excluded: Jf = ∫ f′A with a bounded family A(x)(τ) = a(τ)e^{−iτx}, a² = log(2+τ²)/(2(1+τ²)), has exactly the required growth (the response's counterexample, confirmed numerically). Equivalently, by (1.8), the *form kernel* of any realization has the short-distance singularity n_Γ(r) ~ 1/(2r); that singularity can arise as a second derivative of a bounded covariance. The finite link-function space of a lattice slab is infinite-dimensional and is not excluded by N1 alone.

**N2 — Pure point arithmetic translation** (Appendix B.2; Theorem 7.2). On the source closure the translation Jf ↦ JU_t f is a unitary group; under RH it has pure point spectrum with atoms exactly at the zero ordinates, spectral measure Σ m_γ|f̂(γ)|²δ_γ on Jf, unbounded in both directions and non-periodic. *Excluded:* any unitary group implementing a flow with a global transversal section on a full-measure invariant set (Theorem 7.2's flow-box argument: Lebesgue spectrum), and any group of Lebesgue or mixing spectral type. *Not excluded by this alone:* smooth flows with pure point spectrum, such as the Kronecker flow on 𝕋² (eigenvalues m + √2 n); such a candidate must have the zero ordinates among its eigenvalues and needs its own spectral analysis. Identifying the induced translation with a preselected native flow is an extra hypothesis.

**N3 — No bounded winding-preserving recovery** (Theorems 4.1, 6.1; eq. (7.9)). In the class sector the prime terms arise from V_a, whose limiting structure is the Haar module L²(ℝ × ẑ) with isometries 𝒱_a, 𝒱_a*𝒱_a = 1, 𝒱_a𝒱_a* = 1_{aẑ} (the Bost–Connes isometry relations); each 𝒱_a e_0 f keeps all a branches, with norms a^{−1}‖f‖² and (1 − a^{−1})‖f‖². Theorem 6.1: no nonzero bounded map from that module into the class sector intertwines all V_a. *Scope.* This excludes bounded recovery of the winding module while preserving the specified relations, and explains why recentering loses exactly (7.9). It does not show that every source with pairing Q factors through the module or must realize the prime terms by these operators.

**N4 — The tested positive completions diverge** (Proposition 8.1; Theorem 8.2; m₊(0) < 0). The decomposition Σ_a Λ(a)‖(I − V_a)F‖² has domain {0} in the class sector, and coercive constrained completions with a fixed bounded readout diverge; the archimedean contact constant is negative. *Scope.* A different positive decomposition, auxiliary field, projection or independently defined renormalization is not excluded (‖u − v‖² has negative cross terms and is positive). Heuristically, positivity of Q is not manifest term by term and must be produced globally; that is a heuristic, not a theorem.

These four are the transferable output of the YM folder. Applied to a candidate they ask: is the source a bounded smearing (N1)? does its translation have a global section or continuous spectral type (N2)? is its prime structure recovered by a bounded winding intertwiner (N3)? is its completion the excluded one (N4)? A candidate answering "no" to all four has cleared four specific obstructions and nothing more.

## 2. Applying the filter to the remaining physics threads (recommendation; to be carried out, not yet done)

I have not re-audited the N4SYM and WZW folders in this session; the following are the questions the filter poses, with the outcome I expect from the folder READMEs and the 24 September cross-program assessment.

- **N4SYM displacement/Loewner hierarchy.** N2 is the decisive test: the evolution there is a geometric driving of a Wilson line (smooth-field equations, finite-mass string endpoint, Loewner driver). If the arithmetic translation is identified with that evolution, the question is whether the flow admits a global transversal section (then Theorem 7.2 applies and the thread fails N2) or has continuous spectral type for another reason; a pure-point flow is not excluded by N2 alone. N1 is also open: the memory kernels found so far are bounded single exponentials, which cannot produce log|λ| unless a derivative-type law is specified. Expected outcome: either a sharp negative through the global-section or spectral-type check, or a precisely stated pure-point candidate whose eigenvalues would have to be the zero ordinates.
- **WZW / Bost–Connes orbit weights.** N3 does not bite (the Bost–Connes system is where the isometries live). The WZW manuscript already reports "ordinary-norm limitations", which is N1 failing for the sources tested there. N2 needs a precise statement: the Bost–Connes time evolution has pure point spectrum at {log n}, not at the zero ordinates; in Connes' picture the zeros are the absorption spectrum of the adele-class-space representation, and the Weil form is the complement of a positive contribution — which is the global positivity that N4's heuristic points at. Expected outcome: either the thread reduces to Connes' construction (and should say so and close), or it identifies one Wilson-line ingredient that Connes' picture lacks and that satisfies N1 and N2; there is no third possibility that keeps the thread open.
- **Fixed-slab YM (this folder).** Every mechanism the investigation proposed lies in an excluded class: the winding/electric law fails N1 (Theorem 3.1), current-covariant laws fail N2 (Theorem 7.2 with Corollary 10.3), winding recovery fails N3 (Theorem 6.1), and the tested completion fails N4. Closure in full generality is not a theorem; the pause is a judgement.

## 3. Ranked next steps

1. **Freeze the YM manuscript as a negative-result record** (one short session). Apply the nine edits listed in the review's Section 4: the universality statement, the Burnol / Adams / Bost–Connes identifications with citations, the qualification of Theorem 10.4, the two dropped controls, the ledger row for the zero-list check, the `np.trapz` fix, the `DRAFT_HISTORY.md` rename, and the outline alignment. Rebuild, refresh `BUILD_RECORD.json`, commit, tag. The document is then citable inside the program as "why a finite lattice with a smooth weight cannot work".

2. **Run the filter** (one session). Write a short cross-program note under `../notes/` stating N1–N4 with their proofs referenced to the YM manuscript, then test N4SYM and WZW against each, with a one-paragraph proof or counterexample per condition. Expected: two sharp negatives, or one surviving thread with a precisely stated missing ingredient. Either result is worth more than another mechanism note.

3. **Return the effort to the arithmetic line.** The 24 September handoff (`../arithmetic-storage/notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_CLOSURE_20260924.md`) left two options that have certified momentum: B1 (semilocal Sonin residual from Connes–Consani and the semilocal Sonin paper, evaluated on the weak directions behind its Table 2) and C1 (canonical systems: the ω-string Hamiltonian at small ω against the prime impulses at log 2 and log 3, and the shrinking-join regime left open by Proposition 1). Both produce interval-certified statements in the existing weil-depth pipeline. N3 and N4 above give C1 a sharper target: the canonical-system Hamiltonian is a candidate for the global positivity mechanism that N4's heuristic points at, and it does not need a physical state at all.

4. **If a bulk-side thread is to be kept alive**, the honest comparison point is Connes' adele class space, where the pure-point translation and the isometry relations of N2–N3 are built in and N1 is the archimedean local factor (Burnol's conductor operator, which is exactly what Section 5 of the YM manuscript rediscovers). The program's distinctive angle — effective operators from Wilson lines — would have to supply something that picture lacks. The one concrete candidate visible from the YM work is the holonomy interpretation of the Adams operations: traversing a loop a times is ψᵃ on characters, and the Euler product Σ a^{−s}ψᵃ is the Bost–Connes Hamiltonian's partition structure. A note asking whether a Wilson-line observable can realize the *adelic* (not compact-group) version of that structure with an N1-divergent norm would be the last bulk-side question worth one session.

**Not recommended:** further Monte Carlo loop hierarchies (Appendix A's residuals cannot bear on obstructions that are representation-theoretic and analytic); repairing individual winding phases; pursuing Theorem 10.4 as a route (its hypothesis is at least as strong as RH); any "arbitrary Hilbert embedding" of Q presented as progress; more finite-append certificates in arithmetic-storage (already excluded by that handoff).

## 4. Proposed prompt for the next session

```
Continue the RH program in the shifted-zeta-positivity repo. Two things are queued.

(A) YM closure: papers/susy-positivity/investigations/wilson-loewner/YM. Read
    reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md (Sections 3-4) and apply its
    nine edits to the manuscript sources; rebuild with latexmk; refresh BUILD_RECORD.json;
    rename DRAFT_HISTOR.md; fix np.trapz in numerics/check_positive_hierarchy.py and rerun
    it; add the ledger row for numerics/check_probe_against_zeros.py. Ask me before any git
    operation. Do not add results; this is a freeze.

(B) Filter pass: write papers/susy-positivity/investigations/wilson-loewner/notes/
    STRUCTURAL_FILTER_N1_N4_<date>.md stating the four conditions in
    YM/notes/STRUCTURAL_REQUIREMENTS_AND_NEXT_STEPS_20260925.md with proofs referenced to
    the YM manuscript, then test N4SYM (papers/.../N4SYM) and WZW (papers/.../WZW) against
    each condition with a one-paragraph proof or counterexample. Prefer a sharp negative to a
    vague positive. End with a continuation note and CHANGELOG entry.

After (A) and (B), the default is the arithmetic-storage handoff, option C1 (canonical
systems), unless (B) leaves a surviving thread with a precisely stated missing ingredient.

STANDARDS: classify every statement (proof / computer-assisted / floating / heuristic);
model line at the top of every file; READMEs and CHANGELOG in the same pass; small records
under numerics/records; no draft snapshot folders (DRAFT_HISTORY.md points at commits/tags).
```
