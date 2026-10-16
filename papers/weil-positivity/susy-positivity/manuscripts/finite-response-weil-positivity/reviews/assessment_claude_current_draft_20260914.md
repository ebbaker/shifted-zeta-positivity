# Reassessment: novelty and mathematical usefulness of the current draft

Date: 14 September 2026. Reviewer: Claude (Anthropic, `claude-opus-5`). Requested as a reassessment of the *current* draft, focused on novelty and usefulness, after the revisions responding to [`review_claude_20260914.md`](review_claude_20260914.md).

This supersedes [`assessment_claude_20260914.md`](assessment_claude_20260914.md), which assessed the pre-revision draft and which contained errors that are corrected in Section 3 below. The earlier file is retained unchanged.

## 0. Version verified

| Item | Value |
|---|---|
| Repository commit | `64abada8e9e9de24e778a8a1597ad21a743a82e2` (branch `susy-positivity`, working tree clean) |
| `manuscript.tex` SHA-256 | `de62ec4580a00057f7d5ca7284955a4d6a596f08c99da45ae52a6ccde613c1eb` |
| `derivations.tex` SHA-256 | `7eb5802859c5ca0899ad79f7ec2bbdea508234e2df5f1f7ec86fc985e61dec79` |
| `preamble.tex` / `references.tex` | `29bb4528…` / `e0c62be7…` (unchanged from the reviewed version) |
| Compiled lengths | manuscript 7 pp, derivations 19 pp, per `VALIDATION.json` |

Read in full: current `manuscript.tex`; current `derivations.tex` (all 13 sections plus the review record); [`response_claude_20260914.md`](response_claude_20260914.md); `EVALUATION.md`; `README.md`; `VALIDATION.json`; and the earlier assessment. Note: the request gave the folder as `/Users/ebbaker/...`; on this machine it is `/Users/teddy/Documents/shifted-zeta-positivity/papers/finite-response-weil-positivity`. Manuscript and derivations were not modified.

The revisions are correctly implemented. The cutoff-indexed family `S_{n,N}` with admissibility as a stated hypothesis, the optional status of the certified search, the growth theorem `log log N_min(L) = L/2 + O(log L)`, the image expansion with the uniform remainder `κ_{L,M}` and the norm bound `L·κ_{L,M} = O_L(e^{-ML})`, the completed residual-convergence step, the three-index enclosure notation, and the length-one table with its explicit "upper response, not a certificate" framing are all present and correct.

## 1. Bottom line

**The revisions have made the draft mathematically honest. They have not made it more novel, and the closer I look at the primary literature the less novel it appears.** My earlier assessment was too favourable on the one point I called the paper's real contribution, and wrong on the point I called its most interesting finding.

Specifically: the boundary decomposition is the subordination of the classical method of images, and its Dirichlet-side companion inequality is a published theorem in the fractional-Laplacian literature; the prolate/near-null behaviour I flagged as the most interesting thing here is stated explicitly in Connes–Consani–Moscovici and is the mechanism their construction is built on; and the numerical conclusions I drew from it do not survive the response's qualifications — one of them fails by a factor of 140.

What remains is a careful, correct, explicitly computed assembly with no identified new theorem. That supports an expository research note, not a focused analytic paper, unless one of the two narrow items in Section 8 survives a targeted literature check.

## 2. What I verified before judging novelty

All numbers below are from the check package at [`check_claude_20260914/`](check_claude_20260914/) plus one new script, `recheck.py`, written for this reassessment. They are floating-point diagnostics, not certificates.

## 3. Corrections to my earlier assessment

The response raises five qualifications. **Four are correct and I withdraw the corresponding claims; the fifth is correct as stated but its practical consequence is smaller than the response implies.** I re-ran the relevant computations rather than conceding on argument alone.

### 3.1 Schur congruence preserves inertia, not eigenvalues — correct, claim withdrawn

My earlier assessment wrote "the smallest eigenvalue of `S₁` is ≈ 9.35×10⁻⁷" and identified it with the localized spectral gap studied by Yoshida and Bombieri. That identification is invalid: `λ_min(S_{L,N})` is not `λ_min(W_L)`. The equivalence in Theorem 4.1 is an inertia statement, and the response's 2×2 example (`W = [[2,1],[1,2]]`, eigenvalues 1 and 3, scalar Schur complement 3/2) settles the point.

Measured at `L = 1`, `N = 4` (`recheck.py`):

| K | `λ_min(W_K)` | `λ_min(U_{1,4,K})` | ratio |
|---|---|---|---|
| 200 | 9.360445·10⁻⁷ | 9.378363·10⁻⁷ | 1.00191 |
| 800 | 9.334545·10⁻⁷ | 9.352409·10⁻⁷ | 1.00191 |
| 2000 | 9.332442·10⁻⁷ | 9.350301·10⁻⁷ | 1.00191 |
| 4000 | 9.331974·10⁻⁷ | 9.349833·10⁻⁷ | 1.00191 |

They are different numbers, differing by a stable 0.19%, exactly as the response says. The `U` column also independently confirms the new table in D §13.2: my `K = 200` value `9.378363·10⁻⁷` matches the draft's tabulated `9.3784·10⁻⁷` to all displayed digits, from a separate assembly. My *conclusion* about the order of magnitude of the localized gap survives, but only because `λ_min(W_K)` — the compression minimum, which by min–max is an upper bound for `inf Q_L` and decreases to it as the cosine core fills out — was computed separately in `chk3`. The Schur spectrum was the wrong object to cite for it, and the draft is right to say so in D §13.2.

### 3.2 A truncated residual Gram is not a lower enclosure — correct, claim withdrawn

`chk3_operator_and_schur.py` formed the Gram from rows `K … 5999` only. The response's counterexample reproduces exactly (`recheck.py`): with `A = 0`, `H = I₂`, `B = (0,1)ᵀ`, `Y = 0`, retaining only residual row 0 gives the value **0.0** where the exact Schur complement is **−1.0**. Omitting a positive Gram tail destroys the lower-bound property.

Consequently my statements that "the lower enclosure is below `U_K` by less than 3·10⁻⁶ at `K = 4000`" and that "the enclosure gap decays empirically like `K^{-3/2}`" describe a truncated object and establish neither a certified gap nor an asymptotic rate. Both are withdrawn. The quantity I was tracking is a diagnostic of a partial sum, not of `L_{L,N,K}`.

### 3.3 Working precision is not an interval certificate — correct, and my count was wrong

I said "ten of them below double precision" of the twelve `L = 2` values. Against machine epsilon ≈ 2.2·10⁻¹⁶ the correct count is **five** (6.5e-30, 1.6e-26, 2.5e-23, 2.5e-20, 1.6e-17); against a realistic noise floor `‖W‖·ε ≈ 2·10⁻¹⁵` it is still five. The response's correction is right and my figure was careless. The broader point — that 50-digit working precision without enclosed rounding and truncation error is a diagnostic, not a bound — I had stated, but it deserved more weight than I gave it when drawing conclusions.

### 3.4 A small norm gap is sufficient, not necessary — correct, thresholds withdrawn

My claim that the `2^{-m}` tolerance is "informative only for `m ≳ 20` at `n = 1` and `m ≳ 100` at `n = 2`" assumed an isotropic error `L_K = S − εI`. The response's example (`S = diag(10⁻⁶, 2)` certified by `diag(10⁻⁶, 1)` with norm gap 1) shows a direction-dependent certificate can do better, and the actual lower matrix `U − d_K^{-1}R_K^*R_K` is a Gram correction, which is anisotropic. The stated thresholds are withdrawn.

I would keep one weaker observation, which the draft already makes in D §13.2: whatever the geometry of the error, a certificate must resolve the small eigenvalue *in the direction where it is small*, so the conditioning question does not disappear — it changes shape. The draft's formulation ("one sufficient test, not a necessary condition") is the right one.

### 3.5 The suggested spectral mechanism — correct, and it fails quantitatively

This is the most consequential correction, and the response understates how badly my claim fails. I asserted that the near-null eigenvalue "is" the Fourier mass leaking outside the zero-free window. The response correctly observes that the zero-side expression samples `|F̂|²` at the zero ordinates and is not the continuous out-of-band mass. Measuring both on the same near-null eigenvector at `L = 1` (`recheck.py`):

| Quantity | Value |
|---|---|
| eigenvalue `λ_min(W_400)` | 9.340215·10⁻⁷ |
| zero-side sum `2 Σ_γ |F̂(γ)|²` (300 zeros) | 9.043295·10⁻⁷ |
| continuous out-of-band mass `(1/2π)∫_{|τ|>γ₁}|F̂|²` | 1.267670·10⁻⁴ |
| in-band mass | 0.9998732 |
| **zero-sum / out-of-band ratio** | **0.0071** |

The two quantities differ by a factor of about 140. The eigenvalue equals the zero-side sum — that is just the explicit formula, verified to 8·10⁻²³ in the original review — but it is emphatically *not* the out-of-band mass. My proposed mechanism is false as stated, and a concentration estimate on the continuous mass would not have bounded the eigenvalue even approximately.

What is true, and is a sharper statement than the one I made, is that `|F̂|` is far smaller *at the zero ordinates* than off-band concentration alone would predict. Turning that into a theorem would require relating the ordinate values to the concentration profile, which I have not done and which is not obviously easy. The draft is right not to have absorbed my version.

I also accept the response's point that computations at `n = 1` and `n = 2` do not establish super-exponential decay of `λ_min` in `n`. That claim is withdrawn.

## 4. The boundary theorem, assessed against primary literature

Theorem 3.1 asserts: `T_L = b(H_N) + K_L` with `K_L` bounded and positive; equality of operator and form domains; `‖K_L‖_ess = π/2`; the finite-input tail `η_{h,J}`; and (D §5.2) an image expansion with an exponentially small positive remainder.

### 4.1 The decomposition and the comparison bracket

The bracket `b(H_N) ≤ T_L ≤ b(H_D)` and the identity `T_L = b(H_N) + K_L` are both consequences of two standard ingredients that the paper supplies but does not identify as standard:

1. **Subordination.** `b` is a Bernstein function, so `b(A) = ∫(1 − e^{-tA}) ν(dt)` up to affine terms; here the paper works with the equivalent one-mass resolvent representation, summing `(2/a)(s/(a²+s))` over `a_k = 2k + ½`.
2. **Heat-kernel (equivalently resolvent) domination on an interval.** `p_N ≥ p_free ≥ p_D` pointwise, with `p_N − p_free` given exactly by the method of images. Applying (1) to (2) yields both inequalities *and* the identity, with `K_L` the subordination of the image terms — which is precisely the kernel displayed in D (5.9).

The right-hand inequality has a direct published analogue. [Musina and Nazarov, *On fractional Laplacians*, arXiv:1308.3606](https://arxiv.org/abs/1308.3606) define the "Navier" fractional Laplacian as the spectral power `Σ_j λ_j^s |(u,φ_j)|²` and the "Dirichlet" one as the restricted/integral operator `∫|ξ|^{2s}|Fu(ξ)|²dξ` on the zero extension, and their **Theorem 2** states `((−Δ_Ω)_N^s u, u) ≥ ((−Δ_Ω)_D^s u, u)`. Translating the terminology: *spectral ≥ restricted*, which is exactly `T_L ≤ b(H_D)`. Their abstract further records that the difference is "positive definite and positivity preserving" — the same structural statement the paper makes for the Neumann-side difference, proved there for `s ∈ (0,1)` rather than for this particular Bernstein function.

So the comparison structure is published, for a different (and more studied) `b`. What the manuscript adds on this axis is that it carries out the construction for the archimedean multiplier `b(s) = Re ψ(¼ + i√s/2) − ψ(¼)` and writes the Neumann-side difference down explicitly rather than only asserting its positivity.

I found no source stating the Neumann-side identity in closed form for any `b`. That is a narrow gap, and plausibly only because nobody needed it: once subordination and images are on the table, the derivation is two steps.

### 4.2 The essential norm `π/2`

This is the one genuinely quantitative assertion in the theorem, and it rests on a classical fact. In logarithmic coordinates the Carleman kernel `1/(x+y)` becomes convolution by `[2 cosh(u/2)]⁻¹`, whose integral is `π` — the paper's own proof uses exactly this. The norm of the Carleman operator on `L²(0,∞)` being `π` is Hilbert's inequality (Hardy–Littlewood–Pólya); its purely absolutely continuous spectrum `[0,π]` is classical, and [Yafaev, arXiv:1210.5709](https://arxiv.org/abs/1210.5709v2) — which the paper cites — is the modern treatment of the Carleman operator and its Hankel perturbations. Localizing to a finite interval, where the far field is Hilbert–Schmidt and only the two corner singularities survive, is a routine Weyl-sequence argument.

The constant `π` here is the standard archimedean constant of this subject, not an exotic one: the same `∫ du / (2 cosh(u/2)) = π` underlies [Burnol's conductor operator `log|x| + log|y|`](https://arxiv.org/abs/math/9902080v1), which is the dilation-invariant form of the same archimedean multiplier.

**Conclusion for §4:** the decomposition, the positivity, the domain equalities and the essential norm are each a direct consequence of known results. The explicit Neumann-side kernel with its exponential remainder bound, and the value `π/2` for this specific operator, appear not to have been written down. That is novelty of exposition and bookkeeping, not of mathematics. I was wrong to call this "publishable on its own merits" in the earlier assessment.

## 5. The response construction, assessed separately

Two things must be separated here, and the current draft separates them correctly.

**Standard.** The Schur complement of a block operator with coercive lower-right block; the identity `S = C(Y) − R_Y^*H^{-1}R_Y`; the operator-monotone inversion `H ≥ Λ ⟹ H⁻¹ ≤ Λ⁻¹`; Galerkin orthogonality and the resulting two-sided enclosure; convergence of the enclosure gap; the tolerance reformulation. Every one of these is textbook operator theory or textbook numerical analysis. The draft says so ("the localization and Schur principles are standard").

**The paper's own input.** The unconditional coercivity of the high sector — `H ≥ δ₀I` with an explicit admissible cutoff — obtained from the Neumann comparison plus the crude remainder bound `β_L`. This is what makes a *two-sided* enclosure possible at all.

**Is there a demonstrable advantage over existing finite restrictions?** In principle, yes, and it is worth stating precisely because it is the strongest structural claim the paper can make. A truncation `QW_λ^N` in the sense of [CCM §5](https://arxiv.org/html/2511.22755v1) gives `ε_N ≥ inf QW_λ` by min–max: a positive `ε_N` is a *necessary* condition for positivity and can never certify it. The Schur complement is an exact equivalence (`Q_L ≥ 0 ⟺ S_{L,N} ⪰ 0`), and the lower enclosure `L_{L,N,K}` is, unlike any truncation, an object whose positivity would certify the form's positivity.

**Is the advantage demonstrated?** No. The advantage is purchased entirely with the coercivity input, and the price is recorded in the paper's own Section 6: `log log N_min(L) = L/2 + O(log L)`. No arithmetic estimate on the entries of `A`, `B` or `H` is supplied anywhere in the manuscript or companion; the construction is arithmetic only in that the entries happen to contain prime data. And the one worked instance (`L = 1`) produces upper responses only, with no lower enclosure attempted. So the advantage is real as a statement about the *shape* of the criterion and unrealized as a statement about what can be computed or proved.

## 6. The near-null / prolate comparison

This is where my earlier assessment was most wrong, and the requested comparison settles it.

**CCM already state the prolate approximation.** In [*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755v1), "Prolate wave operator" is a listed key word, and the text states that **"the eigenfunction associated with the lowest eigenvalue of `QW_λ` is well approximated by prolate spheroidal wave functions."** Section 7 (Outlook) builds on "the deformation of the harmonic oscillator called the prolate wave operator" `PW_λ := −∂_x((λ² − x²)∂_x) + (2πλx)²`, and Section 8 ("The missing steps") explicitly frames the connection "between the world of the Weil quadratic form and that of information theory, as developed through the theory of prolate wave functions by D. Slepian and his collaborators." The surrounding programme — [Connes–Moscovici, *Prolate spheroidal operator and Zeta*](https://arxiv.org/abs/2112.05500) and [*The UV prolate spectrum matches the zeros of zeta*, PNAS 2022](https://www.pnas.org/doi/10.1073/pnas.2123174119) — is built on precisely this structure.

**Normalizations match closely.** CCM define `QW_λ` as the restriction of `QW` to `L²([λ⁻¹, λ], d*u)` with `d*u = du/u`; substituting `u = e^x` gives additive interval length `L = 2 log λ`. Their numerical work uses `λ = √12, √13, √14`, i.e. `L = log 12 ≈ 2.485`, `log 13 ≈ 2.565`, `log 14 ≈ 2.639`, with truncation `N = 120` (basis `V_n`, `|n| ≤ N`, dimension 241). The manuscript works at `L = 1` and `L = 2` with `N_min(2) = 131` and compressions of a few hundred modes. **These are the same regime**, in interval length and in matrix size.

**So the observations reproduce known behaviour.** The qualitative facts — that the lowest eigenvector of the localized Weil form is prolate-like, and that the lowest eigenvalues of the truncations are very small — are exactly the phenomena CCM describe and exploit; the smallness of `ε_N` is the mechanism by which their construction extracts the zeta ordinates. Observing it in a different basis, at a nearby length, with a Schur complement in place of a truncation, is a rediscovery.

**Does anything quantitative remain?** CCM report only the differences between computed eigenvalues and known zeros, not the value of `ε_N` itself, so the numerical magnitudes here are not in that paper. But a number without an error bound or a law is not a result, and Section 3.5 above shows that my proposed explanation of the magnitude was wrong by two orders of magnitude. The honest verdict is that no quantitative contribution has been established on this axis by either side.

**One consequence worth recording.** The paper should cite CCM §§7–8 and the prolate programme, not only CCM §§3–5. The current citation ("Proposition 3.4 and Sections 4–5") stops just short of the sections most relevant to the behaviour the paper's own length-one table exhibits.

Separately, the space of numerically realizing the localized Weil operator is active: [Kim et al., *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator* (arXiv:2607.24830, July 2026)](https://arxiv.org/abs/2607.24830) does finite-element discretization of Suzuki's operator and claims "Weil's positivity criterion is realized in operator form." I have not verified that paper's quality, and it does not do the boundary decomposition, but it should be checked before any numerical claim is framed as first-of-its-kind.

## 7. The obstruction claim: I overstated it, and withdraw it

My earlier assessment wrote that note 20 establishes "this framework, as it stands, has no route in." That conflates three different things, and the distinction requested is the right one:

| Route (note 20) | What is actually shown | Correct category |
|---|---|---|
| A — ordered response / tail budget | An explicit 2×2 family where the truncated-inverse inference gives the wrong sign (`a − F_ℓ > 0` while `a − H⁻¹ < 0`) | **Failed inference.** One proposed sufficient inequality is refuted; the route is not shown impossible |
| B — boundary-resolved Galerkin | "Missing lemma B" is stated and not proved | **Unresolved.** Nothing is excluded |
| C — physical contraction | Proved *exactly equivalent* to `D_N ≤ G` | **Equivalent reformulation.** Circular as a proof strategy, not an obstruction |
| D — prime discrepancy | Shown to be "a restatement of Weil positivity, not a new proof" | **Equivalent reformulation** |

None of these is an impossibility theorem. The smooth-density result (`Q_2^dens < −2979/6125`) *is* a genuine negative theorem, but its scope is narrow and correctly stated in the manuscript: replacing the prime measure by its leading density destroys positivity, so gamma data, poles and leading density alone cannot suffice. It says nothing about routes that use signed prime information — note 20 says so itself ("does not exclude every use of explicit prime-counting bounds together with additional structure").

The current manuscript's wording — a finite collection "does not by itself establish" the criterion — is correctly scoped, and my proposed stronger framing should not be adopted.

## 8. Contribution-by-contribution comparison

Verdicts: **K** already known · **C** direct consequence of known results · **P** potentially new (narrow; needs a targeted check) · **U** unresolved, evidence missing.

| # | Item | Closest primary source | Verdict |
|---|---|---|---|
| 1 | `RH ⟺ localized Weil positivity on every interval` | Yoshida 1992 (via [Suzuki §1](https://arxiv.org/abs/2606.09096v2): "RH is equivalent to its positive definiteness for every a>0") | **K** |
| 2 | Explicit matrices for the localized Weil form in a basis; finite truncations and their smallest eigenvalue | [CCM §§4–5](https://arxiv.org/abs/2511.22755v1) | **K** |
| 3 | Bracket `T_L ≤ b(H_D)` (restricted ≤ spectral) | [Musina–Nazarov Thm 2](https://arxiv.org/abs/1308.3606), for `s ∈ (0,1)` | **C** (same proof pattern; new `b`) |
| 4 | Bracket `b(H_N) ≤ T_L` | Subordination + `p_N ≥ p_free` (method of images); no direct citation found | **C** |
| 5 | Identity `T_L = b(H_N) + K_L`, `K_L ⪰ 0`, domain equalities | Subordination of the image identity; positivity analogous to Musina–Nazarov | **C** |
| 6 | **Explicit image kernel for `K_L` with exponential operator-norm remainder `L·κ_{L,M}`** | No prior statement located for any `b` | **P** |
| 7 | **`‖K_L‖_ess = π/2` for this operator** | Carleman norm `π` classical (Hilbert / Hardy–Littlewood–Pólya; [Yafaev](https://arxiv.org/abs/1210.5709v2)); localization routine | **C**, with **P** for the specific constant |
| 8 | Finite-input tails `η_{h,J}`, compressed `O(J⁻¹)` tail, explicit cosine/pole/shift entries | Elementary computation in this basis | **P** (narrow; bookkeeping) |
| 9 | Unconditional coercive high sector with admissible cutoff (`β_L`, `δ₀ = 1/16`) | The paper's own step; no analogue located | **P** (this is the paper's real input) |
| 10 | Schur identity, residual identity, operator-monotone inversion, Galerkin two-sided enclosure, tolerance reformulation | Textbook | **K** |
| 11 | `RH ⟺ S_{n,N} ⪰ 0 for all n and admissible N` | Item 1 + item 9 + item 10 | **C** |
| 12 | `log log N_min(L) = L/2 + O(log L)` | Property of the paper's own bound | **P** (new, limited interest: it quantifies a limitation) |
| 13 | Smooth-density obstruction `Q_2^dens < −2979/6125` | No prior explicit version located | **P** (narrow, honest, low weight) |
| 14 | Extremely small lowest eigenvalues of the localized form / truncations | [CCM §§5–8](https://arxiv.org/abs/2511.22755v1); `ε_N` is central to their Theorem 1.1 | **K** |
| 15 | Prolate character of the minimal eigenvector | [CCM](https://arxiv.org/abs/2511.22755v1) ("well approximated by prolate spheroidal wave functions"), §§7–8; [Connes–Moscovici](https://arxiv.org/abs/2112.05500), [PNAS 2022](https://www.pnas.org/doi/10.1073/pnas.2123174119) | **K** |
| 16 | Quantitative law for `λ_min` vs interval length; mechanism for its size | Not in CCM; not established here (§3.5 refutes my version by a factor 140) | **U** |
| 17 | Advantage of exact elimination over finite restrictions | Structurally real (§5); not demonstrated computationally or arithmetically | **U** |
| 18 | Any arithmetic estimate on the entries of `S_{n,N}` | None supplied anywhere in the package | **U** |

**Nothing in the table is graded "established new theorem."** The strongest entries are 6, 7, 9 and 12, and each is either a routine consequence made explicit or a quantification of the construction's own limitation.

## 9. What would a rigorous length-one certificate actually add?

My earlier assessment called this "the highest-value addition." Having looked at what it would be competing with, **I withdraw that recommendation.** The calculation should not be undertaken on the strength of the current evidence.

**What it would prove.** That `S_{1,4} ⪰ 0`, equivalently that the full localized Weil form is nonnegative on functions supported in an interval of additive length 1. This is *implied by* RH and implies nothing about RH: positivity at a fixed length is a necessary condition only, since the cofinal argument needs all lengths. It cannot be a step toward the conjecture.

**What it would compete with.** Three things, and it is worse placed against each than I assumed:

1. **Yoshida's theorem** already gives unconditional positivity for sufficiently small support, reproved by [Bombieri](https://eudml.org/doc/252338) ("prove again Yoshida's theorem that it is positive definite if `t` is sufficiently small"). The threshold is not made explicit in the sources I could read, so whether length 1 is inside or outside the proved range is *unknown to me* — and that is precisely the check that must come first.
2. **Connes–Consani's archimedean result** covers support in `[2^{-1/2}, 2^{1/2}]`, additive length `log 2 ≈ 0.693`, but for `W_∞` only, not the full form. Not directly comparable, and the manuscript should not claim it is.
3. **CCM's own numerics** already work at `L ≈ 2.5` with 241 basis functions and exhibit the positive lowest eigenvalue as the input to their construction. The *numerical* fact that the form is positive at a length greater than 1 is, in substance, already in the literature.

So a certificate at `L = 1` would upgrade a numerically-evident and probably already-proved fact to a computer-assisted verification of one instance, at a length where the qualitative behaviour is documented. Its value is real but small, and it is contingent on a literature question that has not been answered.

**Cost.** The response is right that the cost is not established. The honest statement of what the certificate needs: the full residual Gram including its tail (not the truncation I used); interval or ball arithmetic through the digamma evaluations, the cosine/pole/shift integrals and the image-kernel columns; explicit treatment of the `1/[2(x+y)]` and `1/[2(2L−x−y)]` corner singularities in every column and Gram integral; and enough resolution to separate an eigenvalue near `10⁻⁶` from zero in the direction where it is small. `K` of order `10⁴` is a guess, not an estimate. Given the program's history with ball-matrix archives in the weil-depth and storage-depth papers, this is plausibly weeks of work.

**Recommendation on this item:** do the literature check (what is the best proved unconditional support length for the *full* localized Weil form?) as a cheap first step. Only if length 1 lies strictly beyond the proved range does the computation become worth costing out — and even then it is a modest, single-instance result, not a headline.

## 10. Recommendation

**Retain as an expository research note; do not pursue a focused analytic paper on the present material.**

The reasoning, stated plainly:

- The RH equivalence is item 11: a direct consequence of Yoshida plus the coercivity input plus textbook linear algebra. It cannot carry a paper.
- The boundary theorem is items 3–8: a correct, well-executed, explicit assembly of subordination and the method of images, with a classical constant. Its most citable pieces (the explicit image kernel; `π/2`) are plausibly unwritten, but they are consequences, not theorems, and neither is used to prove anything the paper does not already get more cheaply.
- The near-null observations are items 14–15: known, and central to an active programme the paper does not currently cite in the relevant place.
- The numerical material is diagnostics, correctly labelled as such in the current draft after the revisions.
- No arithmetic estimate exists anywhere in the package (item 18), which is the thing that would make the construction more than a change of variables.

That is a coherent, honest, carefully documented research note. It is not a paper with a result. The current draft is already written almost exactly as such a note should be written — the revisions moved it decisively in that direction — and the remaining gap is the framing in the title and abstract, which still promise an RH-equivalent conjecture as the headline.

**What would change this verdict.** In rough order of value:

1. **An arithmetic estimate on the entries.** Any inequality on `A`, `B` or `H` that uses the prime data rather than a crude norm bound — even a partial one, even at a single length — would convert the construction from a reformulation into a method. This is the missing lemma B of note 20, and it is the only item on this list that would make the equivalence interesting.
2. **A serious engagement with the prolate connection.** Not a rediscovery of the phenomenon, but a statement relating the Schur/cutoff picture to the prolate wave operator of Connes–Moscovici, or a quantitative account of `λ_min` that CCM do not have. Item 16 is genuinely open; the question is whether this framework offers any purchase on it.
3. **The boundary theorem as a short standalone note**, *if* the literature check confirms the explicit kernel and `π/2` are unwritten. Three or four pages, framed as "an explicit form of the Neumann-side difference for the archimedean multiplier," citing Musina–Nazarov for the Dirichlet-side analogue. Low impact, defensible, and honest.
4. The length-one certificate, subject to Section 9.

**On posting.** If the note is posted as a note — repository plus Zenodo, as the rest of the program is handled — nothing further is needed beyond the framing fix and the CCM §§7–8 citation. If arXiv is still intended, the case for retitling is now stronger than it was yesterday: an abstract whose headline is an RH-equivalent conjecture, backed by items that are individually known or routine, is the profile least likely to survive moderation and most likely to be dismissed by the specialists who would otherwise find the explicit formulas useful.

## 11. Separation of established findings from editorial judgment

**Established by this reassessment (checkable against the cited sources):**

- Musina–Nazarov Theorem 2 is the published analogue of the manuscript's `T_L ≤ b(H_D)`, with "Navier" = spectral and "Dirichlet" = restricted.
- CCM state that the lowest eigenvector of `QW_λ` is well approximated by prolate spheroidal wave functions, and their `ε_N` is the smallest eigenvalue of the truncation; the prolate connection is developed in their §§7–8 and in the Connes–Moscovici programme.
- CCM's interval is `[λ⁻¹, λ]` with `d*u = du/u`, i.e. additive length `2 log λ`; their numerics at `λ = √12, √13, √14` correspond to `L ≈ 2.49–2.64` with `N = 120`.
- Suzuki's paper contains no boundary decomposition, no essential-norm computation and no cosine-basis matrix entries.
- The three numerical corrections in §§3.1, 3.2 and 3.5 are reproduced computations, not opinions: the 1.00191 ratio, the `0.0` versus `−1.0` counterexample, and the factor-140 discrepancy between the zero-side sum and the out-of-band mass.

**Editorial judgment (mine, and contestable):**

- That items 6, 7, 8 and 12 are "narrow" rather than substantial.
- That the material supports a research note rather than a paper.
- That the length-one certificate is not currently worth its cost.
- The ordering of the four items in Section 10.
- The remark about arXiv moderation.

**Not established either way:**

- Whether the explicit image kernel and the `π/2` constant are genuinely unwritten for any `b` (I searched; absence of evidence).
- The best proved unconditional support length for the full localized Weil form (Section 9).
- The quality and overlap of Kim et al. (arXiv:2607.24830).
- Item 16 in every respect.

## 12. Limits of this reassessment

I verified the current sources and re-ran the specific computations reported in §3; I did not re-derive the full manuscript, which the [14 September review](review_claude_20260914.md) already did for the pre-revision version and whose mathematical conclusions the revisions do not disturb. Literature comparisons rest on abstracts, introductions and targeted section reads of the cited papers, not on complete readings; for CCM in particular I read the prolate statements and the definition of `QW_λ` but not the full text of Sections 7 and 8. A negative novelty finding based on searching is weaker than a positive one: where I say "no prior statement located," that is a search result, not a proof of absence.

Nothing here bears on the correctness of the manuscript, which I continue to believe is sound, and nothing here fills any line of `REVIEW_LOG.md`.
