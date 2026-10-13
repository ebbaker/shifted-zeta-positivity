# Paper status — **PROGRAM CLOSED 2026-08-23**

> **STOP.** This program is closed by the author's decision of 2026-08-23. There is no
> live publication pipeline. **All action items below are cancelled** — they are retained
> only as a record of what the plan had been. Nothing here should be resumed without an
> explicit instruction from the author.
>
> See `claude/PROGRAM_CLOSED.md` for the closure decision and the reasons, and
> `claude/memo4_geometric_reformulation.md` / `memo5_lorentzian_test.md` /
> `memo6_obstruction_and_assessment.md` for the structural review that preceded it.
>
> Summary of the closure: the geometric route is closed on five independent grounds
> (slice regularity contributes nothing and the project's own appendix proves it; the
> twistor lift sits on the Castelnuovo–Severi degeneracy locus and this is forced by the
> definition; the conjecture family is RH-trivial or RH-orthogonal for structural
> reasons; the Lorentzian bridge reduces exactly to the first Turán inequality; the
> trace-form route is vacuous over ℝ and circular in the commutative case). The
> operator/Hilbert–Pólya route via Connes–Consani–Moscovici is *not* closed but was not
> taken. **Nothing is to be published**: the author declined on the correct grounds that
> he cannot vouch for proofs he did not verify — a position now also aligned with arXiv's
> May 2026 policy on unvetted AI-generated content.

---

## Historical record (unchanged below this line)

**Draft v1 complete**: `claude/zero_sphere_paper.tex` (25 pp, amsart, compiles clean with pdflatex;
figures `lab_results.pdf` / `bridge_results.pdf` regenerated as vector PDF from the lab code;
ancillary bundle = xi_lib.py, explicit_formula.py, run_experiments.py, run_bridge.py,
run_validation.py + README, ~413 lines).

### What was done beyond the handoff
- New-source review (see `claude/paper_addendum_new_sources.md`): Quat_Exp folded into §5.3
  (sector grounding, closes handoff gap #4 at the honest level: E_ℓ machinery cited, grading
  lemma proved directly, correspondence flagged as foundational open work in Problem 6);
  quadric-immersion rigidity (Prop 3.2/3.5) proved from classical facts (Griffiths–Harris,
  Zak — Li–Peterson misattribution avoided); YM_sym cited for provenance framing.
- Headline results lettered Theorem A–F per handoff (A reformulation, B lift, C dichotomy,
  D linear no-go, E degree no-go, F rate criterion).
- Maximality handled honestly: handoff option (i) as stated is FALSE for arbitrary local
  extensions (Q is a hypersurface — extensions always exist); the paper proves the
  fibration-compatible version (naive extension: no open holomorphy off Q) + global quadric
  immersion rigidity, and says exactly this.
- Theorem F split: (a) unconditional upper bound (RH ⟹ bounded; exponential growth in any
  window disproves RH); (b) exact rate + full equivalence under a non-accumulation hypothesis,
  with Remark 7.4 flagging the gap. **Session-4 fix applied**: (b)'s hypothesis now reads
  "either Y=0, or Y>0 and [non-accumulation]" — the previous statement was vacuous under RH;
  proof opens with the Y=0 branch; Remark 7.4 updated. Recompiled clean, still 25 pp.
- Adversarial review (2 agents) fixed: j₀→i₀ in the two-involutions divided-difference identity
  (real error); factor-4 constant in the anomaly lemma; degree-no-go homotopy labels;
  linear no-go completed conic enumeration + clean (t,s)-family proof; elementary
  sufficiency remark for the Laguerre equivalence; all numerics re-certified against fresh runs.
- Laguerre equivalence now fully citable: CV1990 Thm 2.9 (necessity) + Csordas–Vishnyakova 2013
  Thm 2.3 (sufficiency, NO order/genus restriction — verified verbatim from the published PDF).
- **Role (author decision, session 4/5)**: the 25pp paper is kept as internal reference for
  future papers / a possible review article; it is NOT cited by the arXiv preprint and is not
  itself headed to arXiv in this form.

### Second Involution Conjecture resolved as stated (2026-08-18, session 2)
`claude/second_involution_resolution.tex` (13 pp, compiles clean) proves **Conjecture 6.1 of
`second_involution_intro.tex` is TRUE unconditionally, but by a loophole**, and repairs it:

- **Theorem (adaptive encoding)**: N=2, Λ(ε)=log 2 (ε-independent), |c_j−c|≤σ, error 0.
  Mechanism: the sample points c_j may be chosen AFTER c, so one can *encode* D(c) into
  F(c₁)−F(c₂) by IVT, where F(c)=Re Z(c,log 2); a fixed Möbius-type semialgebraic S decodes.
  All information flows through the selection map, none through arithmetic.
- **Uniform oscillation lemma (unconditional, keeper)**: F(c)=Re Z(c,log 2) is real-analytic and
  has osc ≥ r(a,σ)>0 on EVERY window [c−a,c+a]. Guinand–Weil decomposition + frequency-log 2
  extraction + Bohr-hull compactness. Caveat: r collapses (but stays >0) in zero deserts.
- **Repaired conjectures**: 6.1′ non-adaptive and 6.1″ class-uniform over 𝒳. *(2026-08-23: both
  now known to be contentless — 6.1′ is RH-trivial, 6.1″ RH-orthogonal. See memo4 §1.)*
- **Lower bound**: non-adaptive CONTINUOUS semialgebraic estimators at scale Λ cannot resolve an
  isolated defect quadruple at height x₀ unless Λ ≥ (1−o(1)) log log x₀.
- **Adversarial review done** (2 agents): constants independently reproduced (B₂=0.540667,
  C₀=2.6975, C₁=3.7164, a₀=43.98); several fixes applied. Numerics certified.

### The arXiv preprint — `claude/zero_sphere_condensed.tex` *(never submitted)*
19 pp, amsart, compiles clean, two figures, fully standalone. Title: "The zero-sphere program
for the Riemann Hypothesis and the Second Involution Conjecture". Structure: §§1–7 program with
full proofs, §8 two involutions + gateway prop + original Conj, §9 resolution (encoding thm +
oscillation lemma + diagnosis), §10 repair (6.1′/6.1″ + Hölder lemma + log log x₀ lower bound),
§11 numerics/reproducibility, acknowledgements with the AI-contribution note.
Two adversarial review rounds; no blockers; 12 + 7 findings fixed. Cites↔bibitems bijective (38).
**Known defect, never fixed (harmless, but in the central slogan): §8 states ι_R : ρ↦ρ̄ as
γ↦γ̄; in the rotated variable it is γ↦−γ̄.**

**arXiv package built** (`zero_sphere_arxiv_submission.tar.gz`) and smoke-tested; never submitted.

### Appendix — uniqueness of the canonical extension (2026-08-23, session 6)
`claude/appendix_extension_uniqueness.tex` (11 pp, standalone, compiles clean). Answers "why is
slice regularity the natural definition": **Thm A multiplicative rigidity** (the slice extension
is the unique continuous unital ℝ-algebra morphism with T(id)=q; same-stem-on-every-slice is
forced by Frobenius); **Vekua mismatch** (equivariant Fueter + holomorphic slice restriction ⟹
constant); **classification** (every equivariant linear extension factors through the Fueter map;
weight 2 ⟹ the Fueter map); **twistor moduli + incidence rigidity** (slice regular ⟺ G=id ⟺ the
product lift F×id). Identities sympy-verified (`claude/lab_verify_appendix.py`, 35+ PASS).
No human review. Bib entries carry [verify] flags.

*(2026-08-23: this appendix is, in retrospect, the sharpest no-go in the project — it proves the
dictionary is canonical AND carries no information. It is also the artifact with the clearest
independent audience, in the slice-regular community.)*

---

## Cancelled action items (retained as record only)

1. ~~Full paper F(b) fix~~ — was DONE (session 4).
2. ~~Author read-through of the preprint~~ — **CANCELLED.** The read-through existed only
   because publication was the plan. Nothing is being published, so the obligation is void.
3. ~~Zenodo deposit (blocking for submission)~~ — **CANCELLED as a blocker.** Remains
   *available* as a voluntary terminal deposit with no review obligation: memos, lab code,
   drafts and historical manuscripts as one versioned, explicitly-unreviewed record with a
   per-artifact status line. Not required for anything.
4. ~~Verbatim citation checks~~ (Iwaniec–Kowalski Thm 5.12; GSS book numbers; Titchmarsh §10.1;
   the appendix's [verify] entries) — **CANCELLED.** Only mattered for submission.
5. ~~arXiv submission (math.NT primary, cross-list math.CV, CC BY 4.0)~~ — **CANCELLED.**
6. ~~Outreach (Tier A/B/C plan in `outreach_and_protection.md`)~~ — **CANCELLED**, not merely on
   hold. Do not draft or send contact emails.

## Citation-verification notes (from web-verified pass, 2026-08-17/18; retained)
- DOI 10.1002/mma.1238 = Bory Reyes–Shapiro, MMAS 33(9) 1089–1101 (2010) — CONFIRMED.
- De Bie–Xu published IMRN 2011 no. 22, 5123–5163; odd-dim Clifford–Fourier kernel open.
- Novelty check: no prior product-form lift F×id on the incidence quadric / zero-sphere RH
  formulation found; closest: GSS 2014 eq. (5.6) degenerates to product form for intrinsic f.
- mathlib: quaternions yes, slice analysis no; zeta functional equation formalized
  (Loeffler–Stoll); PNT proved in Lean. HOL Light Fueter-regular formalization:
  Gabrielli–Maggesi ITP 2017.
- *(2026-08-23) Terminology note: "incidence quadric" is not standard; the canonical incidence
  quadric in twistor theory is the 4-dimensional Klein quadric Gr(2,4) ⊂ CP⁵. The object in
  these papers is the tautological P¹-bundle over a regulus, mapping to a Segre quadric surface.*
