# Structural requirements extracted from the YM obstructions, and next steps for the program

25 September 2026. Prepared for Edward Baker by Claude (Anthropic). Model line: claude-fable-5-1 (Fable 5.1) per the runtime environment, session configured as claude-opus-5-5; the serving model may differ. Reasoning effort not exposed.

Companion to the [independent review](../reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md) of the consolidated manuscript. Everything in Section 1 is a direct corollary of theorems proved in the manuscript and rederived in the review; Sections 2–4 are recommendations and are labelled as such.

## 0. Summary

The YM investigation did not produce a Yang–Mills realization of the Weil form, and its affirmative identities are independent of the Yang–Mills state. What it did produce is four proved necessary conditions that any "bulk theory reproducing the Weil form" must satisfy. No candidate in the program has been shown to satisfy all four, and the two remaining physics threads (N4SYM, WZW/Bost–Connes) should be tested against them in one short session before any further investment. The certified arithmetic line (weil-depth, storage-depth, arithmetic-storage, canonical systems) is where the program has cumulative, verifiable results, and it should receive the effort.

## 1. Four necessary conditions (proved)

Notation as in the manuscript: 𝒟⁰ the pole-neutral tests, Q the Weil form (1.5), U_t translation in the logarithmic variable, f_λ the unit-norm modulations (1.11).

**R1 — Logarithmic ultraviolet divergence of the source norm** (Proposition 1.2). Any J with ⟨Jf, Jg⟩ = Q(f, g) satisfies ‖J f_λ‖² = ‖h‖² log|λ| + O_h(1) on tests of fixed support and bounded L¹, L², L^∞ norms. Equivalently, by (1.8), the source two-point kernel in the arithmetic variable has the short-distance singularity n_Γ(r) ~ 1/(2r): the source behaves like a field of dimension ½ in log-scale. Consequences: no source of the form ∫ f(x)A(x)dx with a locally integrable Hilbert-valued A, hence no smearing of a bounded observable family on a finite lattice with a smooth positive weight; no limit of such laws with uniform local bounds (Appendix B.4); no finite sum or square-summable direct sum of such sources. A higher-order distributional law is not excluded by R1 alone, but it must reproduce the growth ‖h‖² log|λ| exactly, which requires the 1/r kernel singularity above rather than a finite-order derivative of a bounded kernel. The divergence must come from an infinite-dimensional ultraviolet structure *in the source*, not merely in the state.

**R2 — Non-geometric arithmetic translation** (Appendix B.2 and Theorem 7.2). On the source closure the translation Jf ↦ JU_t f is a unitary group; under RH it has pure point spectrum at the zero ordinates with multiplicities as norm weights, and it is unbounded in both directions and non-periodic. Any unitary group implementing a smooth flow that admits a global transversal section on a full-measure invariant set (Theorem 7.2's flow-box argument needs nothing else) has Lebesgue spectrum and is excluded. A geometric evolution (a flow on a configuration space, a Loewner-type driving, a boost or dilation acting smoothly on a manifold) cannot be the arithmetic translation. The translation must act on something like an infinite tower or a profinite/adelic fiber.

**R3 — Multiplicative isometries without extra channels** (Theorems 4.1, 6.1 and eq. (7.9)). The prime terms require a semigroup a ↦ V_a with V_aV_b = V_{ab} whose mixed limits are a^{−1/2}⟨f, U_{log a}g⟩. In the SU(2) class sector each V_a creates a − 1 extra phase channels carrying norm Σ_{j=1}^{a−1}ρ(2πj/a)/(aρ(0)) > 0, and these channels are exactly what defeats recentering (7.9) and positivity (Section 5.4). The channel-free structure is the Haar limiting module L²(ℝ × ẑ) with 𝒱_a*𝒱_a = 1 and 𝒱_a𝒱_a* = 1_{aẑ}, i.e. the Bost–Connes relations, and Theorem 6.1 shows the compact-group class sector cannot host it. A candidate must contain (a copy of) this module: its Hilbert space must carry the profinite integers or the finite ideles, not only representation labels of a compact Lie group.

**R4 — No termwise positivity** (Proposition 8.1, Theorem 8.2, and m₊(0) < 0). The prime part of Q enters with a negative sign and the archimedean contact constant is negative; the naive positive completion Σ_a Λ(a)‖(I − V_a)F‖² has domain {0}, and coercive constrained completions diverge. A bulk theory cannot produce Q as a sum of manifestly positive prime contributions. Positivity must arise globally, for example as the norm of a projection onto the complement of an absorption spectrum (the Connes trace-formula picture), never as Σ_a (positive term)_a.

These four are the transferable output of the YM folder. They are stated for the complete Weil form on 𝒟⁰; a candidate that realizes only a finite prime cutoff, only the archimedean part, or only a signed identity has not met them.

## 2. Applying the filter to the remaining physics threads (recommendation; to be carried out, not yet done)

I have not re-audited the N4SYM and WZW folders in this session; the following are the questions the filter poses, with the outcome I expect from the folder READMEs and the 24 September cross-program assessment.

- **N4SYM displacement/Loewner hierarchy.** R2 is the decisive test: the evolution there is a geometric driving of a Wilson line (smooth-field equations, finite-mass string endpoint, Loewner driver). If the arithmetic translation is identified with that evolution, Theorem 7.2's argument applies and the thread fails R2 regardless of how the memory kernel is completed. R1 is also open: the memory kernels found so far are bounded single exponentials, which cannot produce log|λ|. Expected outcome: a sharp negative, provable in one session by transcribing the flow-box argument.
- **WZW / Bost–Connes orbit weights.** R3 is satisfied by construction (the Bost–Connes system is where the isometries live). The WZW manuscript already reports "ordinary-norm limitations", which is R1 failing for the sources tested there. R2 needs a precise statement: the Bost–Connes time evolution has pure point spectrum at {log n}, not at the zero ordinates; in Connes' picture the zeros are the absorption spectrum of the adele-class-space representation, and the Weil form is the complement of a positive contribution — which is R4 in its intended form. Expected outcome: either the thread reduces to Connes' construction (and should say so and close), or it identifies one Wilson-line ingredient that Connes' picture lacks and that satisfies R1 and R2; there is no third possibility that keeps the thread open.
- **Fixed-slab YM (this folder).** Fails R1 (Theorem 3.1 and Appendix B.4), R2 (Theorem 7.2), R3 (Theorem 6.1), and its only completion attempt fails R4. Closed.

## 3. Ranked next steps

1. **Freeze the YM manuscript as a negative-result record** (one short session). Apply the nine edits listed in the review's Section 4: the universality statement, the Burnol / Adams / Bost–Connes identifications with citations, the qualification of Theorem 10.4, the two dropped controls, the ledger row for the zero-list check, the `np.trapz` fix, the `DRAFT_HISTORY.md` rename, and the outline alignment. Rebuild, refresh `BUILD_RECORD.json`, commit, tag. The document is then citable inside the program as "why a finite lattice with a smooth weight cannot work".

2. **Run the filter** (one session). Write a short cross-program note under `../notes/` stating R1–R4 with their proofs referenced to the YM manuscript, then test N4SYM and WZW against each, with a one-paragraph proof or counterexample per condition. Expected: two sharp negatives, or one surviving thread with a precisely stated missing ingredient. Either result is worth more than another mechanism note.

3. **Return the effort to the arithmetic line.** The 24 September handoff (`../arithmetic-storage/notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_CLOSURE_20260924.md`) left two options that have certified momentum: B1 (semilocal Sonin residual from Connes–Consani and the semilocal Sonin paper, evaluated on the weak directions behind its Table 2) and C1 (canonical systems: the ω-string Hamiltonian at small ω against the prime impulses at log 2 and log 3, and the shrinking-join regime left open by Proposition 1). Both produce interval-certified statements in the existing weil-depth pipeline. R3 and R4 above give C1 a sharper target: the canonical-system Hamiltonian is a candidate for the "global, non-termwise" positivity mechanism of R4, and it does not need a physical state at all.

4. **If a bulk-side thread is to be kept alive**, the honest comparison point is Connes' adele class space, where R2–R4 hold by construction and R1 is the archimedean local factor (Burnol's conductor operator, which is exactly what Section 5 of the YM manuscript rediscovers). The program's distinctive angle — effective operators from Wilson lines — would have to supply something that picture lacks. The one concrete candidate visible from the YM work is the holonomy interpretation of the Adams operations: traversing a loop a times is ψᵃ on characters, and the Euler product Σ a^{−s}ψᵃ is the Bost–Connes Hamiltonian's partition structure. A note asking whether a Wilson-line observable can realize the *adelic* (not compact-group) version of that structure with an R1-divergent norm would be the last bulk-side question worth one session.

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
    STRUCTURAL_FILTER_R1_R4_<date>.md stating the four conditions in
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
