# Handoff: Writing the Zero-Sphere Program Paper (LaTeX)

*Context-transfer document for a fresh session. Everything needed to write the arXiv paper without
the originating conversation. Read this first, then the project docs listed in §1.*

## 0. Decisions already made (do not re-litigate)

- **Sole author: Edward B. Baker III** (edwardbaker86@gmail.com). AI assistance goes in a substantive
  acknowledgement, NOT authorship (journal/arXiv norms; also stronger for credibility). Agreed text,
  adapt as needed: *"The synthesis of this program, the twistor-lift and explicit-formula computations,
  the numerical experiments, and substantial portions of the exposition were carried out with Claude
  (Anthropic) as a research assistant in August 2026; all mathematical claims were reviewed by the
  author, who takes sole responsibility for them. Code and archival materials are available at [Zenodo
  DOI — placeholder until deposit]."*
- **This is a program paper, not a proof claim.** The intro must say so plainly (see §11 of
  `claude/zero_sphere_program.md` for the agreed framing). The no-go theorems and the two hardness
  checks (Davenport–Heilbronn; De Bruijn–Newman) are features — lead with intellectual honesty.
- **Name:** "the zero-sphere program". Working title: *"The zero-sphere program: a quaternionic–twistor
  framework for the Riemann Hypothesis."* Author may prefer a variant.
- **Venue:** arXiv math.NT, cross-list math.CV (math.DG optional). Journal decision deferred. arXiv
  license: CC BY 4.0 (per the interest-protection strategy). Include code as arXiv ancillary files
  (`anc/` directory).
- The historical manuscripts (Quat_Riemann 2015 etc.) will be deposited unaltered on Zenodo as a
  program archive, cited by this paper; do NOT rework them into the paper beyond citation.

## 1. Source documents (all in this Claude project; use project_read)

- `claude/zero_sphere_program.md` — the external program document. **The paper is essentially the
  LaTeX-ification and rigor-upgrade of this document.** Its structure, claims, verification legend,
  and reference list are the skeleton.
- `claude/RH_program_synthesis.md` — memo 1: program synthesis, function-class analysis, literature.
- `claude/twistor_lift_computation.md` — memo 2: incidence quadric, lift, equivariant invariant,
  degree no-go (compressed proofs).
- `claude/memo3_explicit_formula_bridge.md` — memo 3: certified explicit formula, quadratic form,
  two-involutions finding.
- `claude/lab_RESULTS.md`, `claude/lab_xi_lib.py`, `claude/lab_run_experiments.py`,
  `claude/lab_explicit_formula.py` — numerics (all certified values below come from these).
- Project file uploads: the author's underlying manuscripts (`Quat_Riemann.pdf`, `Thol.pdf`,
  `Tconffinal.pdf`, `Tconf2.pdf`, `ASDYM_sym.pdf`, `Generalized_Isothermal.pdf`).
- `claude/outreach_and_protection.md` — private; do not cite in the paper.

## 2. Paper outline (≈25–30 pp, amsart)

1. **Introduction.** Program statement; the reformulation in one paragraph; honesty clause; summary
   of results (two structure theorems, two no-go theorems, one certified criterion, one organizing
   question); roadmap; provenance paragraph (2015–2026 arc + AI-assistance disclosure).
2. **Preliminaries.** Slice regular functions, intrinsic class, representation formula, pointwise
   algebra closure for intrinsic functions, zero-structure theorem — ALL CITED, not reproved (verify
   exact statements/numbering in Gentili–Struppa 2007, Gentili–Stoppato; the book Gentili–Stoppato–
   Struppa *Regular Functions of a Quaternionic Variable* is the clean citation source). Rotated
   coordinates: s = 1/2 + iz, Ξ(z) = ξ(1/2+iz), ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s). The extension
   Ξ(q) = 4∫₀^∞Φ(u)cos(qu)du (Φ as in memo 1/lab; constant 4 certified — see table §5 below).
   **Theorem A (reformulation):** RH ⟺ Z(Ξ_ℍ) contains no 2-sphere. Immediate from cited zero
   structure; state as theorem for citability.
3. **Twistor geometry.** Conventions from Baker's *Twistor holomorphicity*/Tconffinal (fibration,
   η(w) stereographic, real structure σ). Content from memo 2, upgraded:
   - Lines L_ζ = {[ζw, ζ, w, 1]}; Plücker conic; incidence quadric Q = {z₁z₄ = z₂z₃} ≅ CP¹_ζ×CP¹_w
     = {(q,η): q ∈ C_η}; two rulings (sphere-lifts / fixed-J slices); real structure
     ρ(ζ,w) = (ζ̄, −1/w̄).
   - **Theorem B (lift):** intrinsic slice regular f ⇒ F×id is holomorphic ρ-equivariant on Q,
     covering f. Proof: direct (memo 2 §2 has it; write out the chart identity q = (w+j)^{-1}ζ(w+j)).
   - **Maximality.** Two options, decided by what can be proven cleanly in the new thread:
     (i) STRONG: no non-Möbius intrinsic f extends holomorphically to any CP³-neighborhood of any
     point of Q. Memo 2 proves the naive fiber-preserving extension fails off Q (d(q²) intertwining
     computation); upgrading to arbitrary extensions needs a jet argument at Q — attempt it, but do
     not overclaim. (ii) SAFE fallback: state the verified computation (naive extension holomorphic
     exactly on Q) + cite Baker's rigidity theorem (twistor conformal ⇒ Möbius, Tconffinal Prop 3.1)
     as the global complement. Use (ii) if (i) resists.
   - **Theorem C (equivariant dichotomy):** zero divisor of the lift = union of first-ruling lines;
     real zero ⇒ σ-fixed component; sphere ⇒ σ-swapped pair; homology classes equal (2·[ruling] per
     pair either way). In Y = Q/σ: ℝP² vs S² components; RH ⟺ all components nonorientable. Proofs
     in memo 2 §3, short; write in full.
   - Literature positioning: Gentili–Salamon–Stoppato JEMS 2014 (twistor lifts/OCS), Altavilla–
     Sarfatti Math. Z. 2019 (ruled surfaces), Salamon–Viaclovsky Math. Ann. 2009 (OCS rigidity).
     Claim of novelty for the product-form lift on Q + equivariant-divisor RH formulation must be
     softened by a genuine literature check (the new thread has web access — search Altavilla's and
     Stoppato's recent papers before asserting).
4. **No-go theorems.**
   - **Theorem D (linear):** every continuous R-linear functional of any rotational extension
     (slice extension R, or Fueter-side Q_ℓ of Baker 2015) factors through the complex Ξ; hence no
     such functional separates real zeros from spheres. Proof: linearity + injectivity + density
     (Laurent/Runge argument generalizing Baker 2015 §4). State topology hypotheses carefully.
   - **Theorem E (degree):** for intrinsic slice regular f, at q = x+yJ (y>0) the real Jacobian
     satisfies det df = |f'(z)|²·|∂_s f(z)|², where ∂_s f(q) = (f(q)−f(q̄))(q−q̄)^{-1} is the
     SPHERICAL DERIVATIVE (standard object — cite Gentili–Stoppato); in particular intrinsic maps
     are orientation-preserving off the degenerate set. Consequently the S³-degree of f/|f| equals m
     at a real zero of multiplicity m and 2m at a sphere of multiplicity m — identical to the complex
     count; deformation-invariant counts cannot detect spheres. Proof ingredients (memo 2 §4 +
     this handoff): split T_qℍ = C_J ⊕ C_J^⊥; df = f'(z) on C_J; df = ∂_s f(z) (acting by left
     multiplication) on C_J^⊥ [verify: for f = q^m this gives Σq^i q̄^{m−1−i} = (q^m−q̄^m)/(q−q̄) ✓];
     sphere local degree via global homotopy consistency (q²+t family) + the [S³_R] = [S²×S¹]
     homology matching in ℍ∖S².
5. **Hardness checks.** DH function: definition (χ mod 5 with χ(2)=i; κ = (√(10−2√5)−2)/(√5−1);
   Λ_DH(s) = (5/π)^{s/2}Γ((s+1)/2)·½[(1−iκ)L(s,χ)+(1+iκ)L(s,χ̄)]; Ξ_DH(z) = Λ_DH(½+iz) real, even —
   cite Titchmarsh §10.25 and Spira for off-line zeros); computed spheres (table §5). De Bruijn–
   Newman Λ ≥ 0 (Rodgers–Tao 2020). Formulate the two checks as requirements on any candidate
   sphere-excluding mechanism.
6. **Positivity hierarchy.** −(logΞ)''(x) = Σ_ρ(x−ρ)^{−2}; pair term negative exactly on |x−a|<y₀;
   Laguerre L₁ ≥ 0 necessary; generalized Laguerre family ⟺ Laguerre–Pólya membership ⟺ RH (cite
   Csordas–Varga precisely — pull the actual theorem; the memo cites at abstract level only). Sector
   functionals E_ℓ with j_ℓ tags; **Lemma (grading):** real zeros vanish from ℓ≥1 sectors; sphere of
   radius y₀ enters sector ℓ at order y₀^{2ℓ} (trivial from j_ℓ asymptotics — prove). Numerics §5.
7. **Explicit-formula bridge.** EF in rotated coordinates (statement as in memo 3 §1; conventions:
   g(u) = (1/2π)∫h(r)e^{−iur}dr; pole term h(i/2)+h(−i/2); archimedean Re ψ(¼+it/2) − log π; prime
   term −2Σ Λ(n)n^{−1/2}g(log n)) — cite Iwaniec–Kowalski Thm 5.12 AND report the numerical
   certification (table §5). Gaussian family h_{c,λ}; Z(c,λ) prime-computable, λ = log-prime scale.
   **Lemma (diagonal anomaly):** real zeros contribute O(1) to |Z|² uniformly in λ; sphere (a,y₀)
   contributes 2cosh(2λy₀)e^{−((a−c)²−y₀²)/σ²} + O(e^{λy₀}); cross terms bounded via N(T) ≪ T log T
   against Gaussian tails — write the bookkeeping. **Theorem F (rate):** limsup_λ log|Z(c,λ)|/λ =
   sup_ρ y_ρ = Θ − ½ for every window; RH ⟺ subexponential growth. HONESTY REMARK (mandatory): this
   is a Gaussian-mollified form of the classical zero-free-region ↔ prime-error equivalence; the
   novelty is the organization, not the wall. ℓ-decomposition: sinh(2z)/2z = Σ(2ℓ+1)i_ℓ(z)²
   (Gegenbauer addition theorem — find the classical citation; certified numerically); j_ℓ ↔ i_ℓ
   Wick rotation linking the unitary and analytic families.
8. **Two involutions + open problems.** The organizing statement (memo 3 §5, program doc §8):
   ρ↦1−ρ (holomorphic, EF-visible) vs ρ↦ρ̄ (antiholomorphic, sphere-defining); conjugate-paired sums
   Σ F(γ,γ̄) as the missing tool; the scalar instance Σ1/(ρ(1−ρ)) = 2+γ_E−log4π vs Σ1/(ρρ̄).
   Ranked open problems 1–6 from program doc §9, each with its hardness-check annotation.
9. **Formalization targets.** Program doc §10. Verify current mathlib status before asserting
   (search: mathlib quaternion slice regular; Loeffler–Stoll zeta/L formalization; Kontorovich–Tao
   PrimeNumberTheoremAnd status as of writing).
10. **Numerical appendix.** Methods (quadrature parameters, precision), certified-values tables
    (§5 below), code manifest, reproduction instructions (~3 min runtime).

## 3. Style and rigor guidance

- amsart; numbered theorems/lemmas/remarks; no "verification legend" in the paper — instead each
  numerical claim points to the appendix, each cited theorem to a precise reference.
- Tone: sober, concrete, self-limiting. Every section that could be over-read gets a Remark fencing
  it (the reformulation is a relabeling until §§3–7 add structure; the rate theorem reduces to
  classical facts at exponential scale; etc.). The paper's credibility strategy IS the honesty.
- **Citation warning:** all literature in the memos was verified at title/abstract level only.
  Before final text, pull exact theorem statements for: Gentili–Stoppato zero structure; GSS 2014
  main theorems; Salamon–Viaclovsky main theorems; Csordas–Varga Laguerre equivalences; Rodgers–Tao;
  Iwaniec–Kowalski 5.12; Titchmarsh on DH; Gegenbauer addition theorem for modified spherical
  Bessel functions.
- Figures: regenerate as vector PDF via the lab code (matplotlib savefig .pdf) rather than reusing
  PNGs. Two figures suffice: lab_results (3-panel) and bridge_results (rate plot).

## 4. Known gaps / proof obligations (be honest where they land)

1. Strong maximality of Q (see §2.3 above) — attempt, fallback ready.
2. Linear no-go: precise function-space topology (suggest: uniform convergence on compacts;
   extensions as continuous linear maps between Fréchet spaces; injectivity from the representation
   formula).
3. Cross-term bookkeeping in the rate theorem (Gaussian tails vs zero density — routine but must be
   written).
4. The claim "E_ℓ tags = spherical-harmonic content of the extended zero set" (memo 1/6) is
   motivational; either make it precise via the plane-wave expansion of Baker 2015 §8 or present the
   tags as definitions with the motivation in a remark.

## 5. Certified numerical values (quote these; all reproducible from project code)

- Ξ normalization: Ξ_int/ξ(½+ix) = 0.500000 before the factor-4 fix at x ∈ {0, 5, 20, 30}
  (i.e. ξ(½+ix) = 4∫Φcos); ξ(½) = 0.497120778; Ξ_int(14.134725...) ≈ −1.8e−18.
- EF certification (σ=2, 250 zeros; zero side vs pole+arch+prime): (c,λ)=(20,0): 1.86901176,
  |Δ|=1.09e−10; (20,1): 0.96584078+1.42563531i, 1.19e−9; (20,2): −0.85353747+1.53365468i, 6.35e−9;
  (20,3): −1.80938739+0.21232192i, 1.84e−8; (35,2): −0.38300486+0.14677138i, 4.79e−9.
- DH off-line zeros (Newton on f_DH, dps 25): 0.808517182457+85.6993484854i;
  0.6508300806+114.1633427i; 0.5743560505+166.4793059i → spheres (a; y₀) = (85.699348; 0.308517),
  (114.163343; 0.150830), (166.479306; 0.074356). DH on-line zeros in [74,97] (14 of them):
  74.325, 75.909, 77.226, 78.717, 80.328, 81.925, 83.109, 87.647, 89.439, 90.725, 92.183, 93.781,
  95.349, 96.292.
- Laguerre: rel. min L₁[Ξ] = +0.173 on [0,52] (float64 floor ~1e−34 beyond x≈55); L₁[Ξ_DH]<0 on
  [85.417, 85.982] (pred. [85.391, 86.008]) and [114.025, 114.302] (pred. [114.013, 114.314]);
  control [78,82] min ≈ +7.18e2 (units: after sign-preserving rescale W = e^{πx/4}Ξ_DH; note
  L₁[Gf] = G²L₁[f] for G = e^{cx}).
- Sector energies (λ∈[0,2], weight e^{−λ²}, 20 real ordinates + implant at a=28): log-log slopes
  2.000 / 4.000 / 6.000 for ℓ=1,2,3; E₁(real only) = 0 exactly; DH per-sphere E₁ = 4.360e−3,
  1.062e−3, 2.593e−4 (ratios 4.11, 4.10 vs (y₀/y₀')² = 4.18, 4.11).
- Rate experiment (σ=2, λ∈[0.5,25], fit on λ>15): zeta(250 real) −0.0003; zeta+implant(y₀=0.1)
  0.0961; DH+sphere 0.3085 (true 0.30852); DH on-line control −0.0089. |Z|² at λ=25: 3.22, 4.66e2,
  2.05e7, 5.75. (Implant fit biased low: e^{2·25·0.1}=e⁵ barely clears background — say so.)
- i_ℓ identity: |Σ_{ℓ<80}(2ℓ+1)i_ℓ(z)² − sinh(2z)/(2z)| ≤ 3e−14 at z ∈ {0.5, 1, 2, 4}.

## 6. Logistics

- arXiv ancillary: `anc/xi_lib.py`, `anc/run_experiments.py`, `anc/explicit_formula.py`, README
  with runtimes (~3 min total; deps: numpy, scipy, mpmath, matplotlib).
- Zenodo archive DOI: placeholder [DOI] in acknowledgements + references until the author deposits
  (archive = historical manuscripts + memos + code; the author also mentions an unposted
  Clifford-analysis rederivation manuscript — include if he uploads it).
- Reference list seed: program doc §12. BibTeX everything; verify against actual publications.
- Abstract draft (edit freely): *"We describe a research program on the Riemann Hypothesis organized
  around the canonical extension of the completed zeta function Ξ to the quaternions as an intrinsic
  slice regular function. The zero set of this extension consists of real points and round
  2-spheres, and RH is equivalent to the absence of spheres. We develop three faithful formulations
  of this dichotomy: twistor-geometric (the zero divisor of an induced self-map of an incidence
  quadric is σ-invariant component-by-component), a positivity hierarchy graded by spherical Bessel
  tags whose bottom rung is the Laguerre inequality, and an explicit-formula criterion — a
  numerically certified, prime-computable quadratic form that grows subexponentially in its
  frequency window if and only if RH holds, with growth rate equal to twice the largest sphere
  radius. Two no-go theorems delimit the framework: no linear functional of a rotational extension,
  and no deformation-invariant degree count, distinguishes real zeros from spheres. The organizing
  statement is that RH asserts the agreement, on the zero set, of the holomorphic involution
  ρ ↦ 1−ρ with the antiholomorphic involution ρ ↦ ρ̄; the central open problem is to import the
  latter into explicit-formula arithmetic. The Davenport–Heilbronn function serves as control
  throughout, and all numerical claims are reproducible from included code."*
