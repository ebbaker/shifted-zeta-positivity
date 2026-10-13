# Full Yang–Mills: A Deep Dive

*Working memo #17 — August 24, 2026. Written in response to a direct challenge: that full (non-self-dual) Yang–Mills is the most promising remaining direction, that it has the most freedom, and that we have not shown it fails. The first two are right, the third was right when it was made, and this memo is the attempt to settle it. Certified by `lab_ym_landscape.py`; the substantive inputs are other people's theorems and are cited individually.*

---

## 0. Verdict

**I withdraw the claim that full YM was closed.** Memo 12 §4 and memo 13 §3 said it was closed three ways. Auditing those:

| the closure I claimed | status now |
|---|---|
| the **obstruction** reading is dead (memo 11's theorem) | **stands, and is genuinely universal.** In the ambitwistor picture source-free YM *is* the third-order extension condition, so "RH ⟺ the bundle extends" is exactly the shape memo 11 excludes. |
| the **matching** reading dies on positivity (memo 12 §3.5) | **downgraded to a conjecture** by memo 16 §3 — verified only in the ADHM shape at `k = 2,3`. It does not close full YM. |
| the degeneracy locus is where the object fails to exist (Pool Thm IV.5) | **stands, but kills one dictionary, not the direction.** |

So the *existence* reading — "RH ⟺ there exists a YM solution with property `X`" — was untouched. Existence statements are projections, hence can have interior, and memo 11's scope section says so explicitly. The challenge was correct.

**And the case for the direction is stronger than I gave it credit for.** One point in particular I under-weighted: after gauge fixing, the YM system `d_A^* F_A = 0` is a **determined** second-order elliptic system, so local solutions on a domain are parametrised by boundary data — infinite-dimensional. The ASD equations are **overdetermined** (first order, 3 equations for 4 unknowns modulo gauge), which is the structural reason instanton moduli are a finite `8k−3` and full YM has no analogue. **This is the only place in the entire programme that answers memo 15's criticism that every construction so far is finite.** *(Folklore; I found no citable theorem, so it is flagged.)*

**But the literature delivers a hard negative on the other half, and it is not our computation.** The programme needs two things (brief §1.4): existence cheap, and **isolation as a theorem**. Full YM buys the first at exactly the cost of the second:

> **Every rigidity theorem in the subject has the form "small ⟹ (anti-)self-dual, or flat".** Bourguignon–Lawson–Simons, Min-Oo, Dodziuk–Min-Oo, Gerhardt, Nakajima, Feehan I/II, Feehan's discreteness theorem, Gursky–Kelleher–Streets, Vieira. **Not one isolates a non-self-dual solution.**

And the gap is now known **explicitly and sharply**: on the round `S⁴` with `G ⊂ SO(E)`, any YM connection with `F⁺ ≢ 0` satisfies

`∫|F|² ≥ 8π²|κ| + 16π²`

— at least **two charge-one instanton actions** above the Bogomolny minimum (Gursky–Kelleher–Streets, Comm. Math. Phys. **361** (2018); restated as `δ = 2` by Dayaprema–Waldron, arXiv:2412.21050, who note it is consistent with all known examples). So the analytic tools live *exactly and only* in a neighbourhood of the self-dual stratum, which is where the freedom isn't.

**Three quantitative aggravations** (`lab_ym_landscape.py`):

1. **The gap is additive, not multiplicative.** `16π²` regardless of charge, so the relative gap `2/|κ| → 0`. The theorems isolate the ASD stratum and get no stronger where the freedom is.
2. **Non-self-dual solutions are not even isolated from each other.** Sadun's family (Comm. Math. Phys. **163** (1994)) is a **continuous two-real-parameter family**. And none is a local minimum: Taubes (CMP **91** (1983)) gives Morse index `i ≥ 2(|κ|+1)`, and Bourguignon–Lawson (CMP **79** (1981)) says any *weakly stable* YM field on `S⁴` for `SU(2), SU(3), U(2)` is `(A)SD`.
3. **The sector gets less rigid with energy, not more.** Sadun's family has index `= rt` with `c₂ = (r²−t²)/8`, nullity `12` independent of `(r,t)`; index/`|c₂|` stays `O(1)`, matching the Gursky–Kelleher–Streets index-energy bound (CMP **376** (2020)). High-energy non-self-dual solutions are deep saddles.

**And the decisive item, which is also not our computation.** In Sadun's family — the standard construction of non-self-dual YM fields on `S⁴` — the solutions are parametrised partly by the **holonomy around a 2-sphere** `S₊ ⊂ S⁴` (a singular orbit of the `SO(3)` action), and the family includes connections with a holonomy singularity along exactly that 2-sphere (classification: Sibner–Sibner, CMP 1992).

> The programme needs "**no 2-sphere in the degeneracy locus**" as a theorem about the class. In the very sector where full Yang–Mills has its freedom, a 2-sphere is the **standard** degeneracy locus rather than a forbidden one.

**Net verdict.** Not closed — I am not going to make that mistake a third time — but the direction is in materially worse shape than the challenge assumed, and for reasons external to this programme. What remains is one specific, well-posed, unexplored question (§4), and it is a genuine one.

---

## 1. Two corrections to earlier memos

Before the substance, two things I got wrong that bear directly on this.

**(a) The current is not a degree of freedom of YM solutions.** Memo 12 §0(5) and memo 14 §4(g) flagged as "one genuine gap" that full YM supplies a nonzero current `*J`, which self-dual theory lacks, and that an *inequality* on the current would survive memo 11's theorem. That was a misreading of Pool §III. The YM equations *with* current are `D_AF = 0`, `D_A(*F) = *J`; the **source-free** YM equations have `*J = 0`; and Pool's Theorem V.4 says the third-order obstruction **is** `*J`. So:

> A source-free YM solution has `*J = 0` by definition. The current is not a feature of YM solutions — it is the obstruction to being one. A connection with `*J ≠ 0` is not a YM field at all; it is the order-0 object, where there is no isolation of any kind.

So that "gap" does not exist. **Withdrawn.** The genuine advantage of full YM over self-dual is not an extra field; it is simply that `{D^*F = 0} ⊋ {F = *F}` and the former is much bigger.

**(b) Stability is dead too, and by a screen already in the brief.** The one inequality-shaped condition native to the holomorphic category is slope stability (Hitchin–Kobayashi / Donaldson–Uhlenbeck–Yau): `μ(F) < μ(E)` for all subsheaves. It is an inequality, so memo 11's Theorem does not touch it — but **Corollary A does**. Stability is an *open* condition in holomorphic families, so `{a : E_a` stable`}` is open in `ℂ^d` and has nonempty interior there; the hyperbolic locus `H` has **empty** interior in `ℂ^d` (it lies inside `ℝ^d`). Hence `{stable} ≠ H`, and the same for `{semistable}` whenever the stable locus is nonempty. **So the only holomorphic-native inequality in the subject is excluded on parity grounds.**

That matters because it removes what looked like the best surviving candidate: in the complexified/ambitwistor setting there is otherwise **no positivity at all**. Mason–Skinner's ambitwistor YM action `S[A,G] = ∫tr(F∧G − (ε/2)G∧*G)` is indefinite — a Chalmers–Siegel first-order action with an auxiliary field, built for BCFW recursion, with no Bogomolny bound. And in split signature LeBrun–Mason record that solutions are *generically non-analytic or only finitely differentiable*: regularity is lost, not gained, and there is no removable-singularity theorem and no gap theorem.

> **The dichotomy:** the holomorphic setting has the freedom but no positivity; the real/Euclidean setting has the positivity but its theorems all conclude self-duality. Same shape as memo 12's positivity dichotomy and memo 13's rationality dichotomy, one level up.

---

## 2. What full YM actually offers, item by item

| requirement (brief §1.4) | self-dual / ADHM | full YM |
|---|---|---|
| existence cheap (big solution space) | **no** — `8k−3` | **YES** — infinite-dimensional |
| the PDE system | overdetermined (1st order) | **determined** (2nd order elliptic) |
| nonzero current available | no | **no** (see §1a) |
| Bogomolny / energy bound | yes, with equality | yes, strict |
| **isolation theorem for the class** | gap theorems nearby | **none known** |
| solutions isolated in moduli | yes (smooth moduli) | **no** — continuous families |
| weakly stable members | yes (minima) | **none** (Taubes; Bourguignon–Lawson) |
| **2-sphere excluded from the degeneracy locus** | n/a (no jumping over the domain) | **no — it is the generic locus** |

Two rows are the whole story: the second (freedom, in full YM's favour) and the last two (isolation, decisively against). That is brief §3's rigidity/existence trade-off — but for the first time instantiated by an external literature at the level of a whole PDE theory rather than by our own matrix computations.

**Non-self-dual solutions do exist, abundantly**, which is worth recording since it is the premise the direction needs: Sibner–Sibner–Uhlenbeck (PNAS **86** (1989) 8610) produced infinitely many non-minimal finite-action critical points on `S⁴` by min–max over a topologically nontrivial loop, via the correspondence with monopoles on hyperbolic `ℋ³`; Bor (CMP **145** (1992)) proved existence by minimising within a symmetric class and showing the linearised self-duality equation has no solution with those symmetries; Sadun–Segert (Bull. AMS **24** (1991), Theorem 1 and Corollary 2) give one on **every** `SU(2)` bundle over `S⁴` with `c₂ ≠ ±1`; Parker (Duke **66** (1992), Cor. 5.2) the same by equivariant Morse theory. Yau's Problem 117 — that every YM field on `S⁴` is `(A)SD` — is false. The premise is sound. It is the isolation half that fails.

---

## 3. Screening the candidate degeneracy loci

The direction needs a canonical locus of a source-free YM field whose sphere-freeness is a theorem. Every candidate, screened:

| candidate locus | verdict |
|---|---|
| real **jumping locus** | **empty** over the domain, by Pool's Theorem IV.5 (the correspondence *requires* `E|_{τ^{-1}(x)}` trivial for every `x ∈ U` to produce a connection). Asking for a nonempty one is asking for the object not to be a YM field. |
| the **current** `*J` | zero for any YM solution (§1a). |
| `{F⁻ = 0}` (locally self-dual locus) | `F⁻` is a section of `Λ²₋ ⊗ 𝔤`, rank `3·dim𝔤 = 9` for `SU(2)`; generic zero set has codimension `9 > 4`, i.e. **empty**. Useless as a discriminant, in the opposite direction. |
| `{F = 0}` (flat locus) | rank 18. Empty. |
| **rank-drop loci of `F⁻`** | see the dimension ladder below — and their classes are Thom polynomials in characteristic classes (Fehér–Némethi–Rimányi), hence deformation invariants, hence brief §6.3. |
| **slope stability** | dead by Corollary A (§1b). |
| the **energy gap used as a criterion** | `∫|F|² < 8π²|κ| + 16π² ⟹ F⁺ ≡ 0 ⟹ ASD ⟹` back inside ADHM, where memo 7's Theorem 4 already gives hyperbolicity from the matching alone. The energy hypothesis is redundant and the loop closes. |

**The dimension ladder, which is the cleanest kill in this memo.** The zero set of `RΞ` is a union of **2-spheres** (one per conjugate pair) and **points** (one per real zero). Any locus proposed to match it must be able to be 2-dimensional. For `F⁻` a `3 × d` matrix of functions (`d = dim 𝔤`), the rank loci have codimension `(3−r)(d−r)`:

| `G` | `d` | `rank ≤ 0` | `rank ≤ 1` | `rank ≤ 2` |
|---|---|---|---|---|
| `SU(2)`, `SO(3)` | 3 | 9 → empty | 4 → **points** | 1 → **hypersurface** |
| `U(2)` | 4 | 12 → empty | 6 → empty | **2 → 2-dimensional** |
| `SU(3)` | 8 | 24 → empty | 14 → empty | 6 → empty |
| `SO(4)` | 6 | 18 → empty | 10 → empty | 4 → points |

> For `SU(2)` — the case the whole programme has used — **no curvature rank locus is ever 2-dimensional.** They are empty, points, or a hypersurface. So no such locus can *be* a union of 2-spheres, before any analysis. And the two non-empty ones are dead anyway: the 0-dimensional one is counted by a characteristic number (brief §6.3), and a hypersurface can contain spheres, so it supplies no isolation theorem.

**`U(2)` is the single exception**, and it is the one concrete thing in this memo worth pursuing: `dim 𝔲(2) = 4`, so `{rank F⁻ ≤ 2}` has codimension `(3−2)(4−2) = 2` — a genuinely **2-dimensional** canonical locus, which *can* be a union of 2-spheres. And `U(2)` is inside Bourguignon–Lawson's stability hypothesis, so the stability theorem is available there.

*Caveat, stated because memo 16 exists.* These are **generic** codimensions. For a particular YM field a locus can be larger than generic. So the ladder **excludes matching by dimension** but does **not** by itself supply an isolation theorem, which would need the reverse implication: that the locus can never be 2-dimensional for *any* member of the class. That is exactly the gap in §4.

---

## 4. What is genuinely left

One question, and it is well-posed and unexplored.

> **Is there a canonical locus of a source-free Yang–Mills field on `ℝ⁴` whose topology is constrained — in particular, one that provably cannot contain a 2-sphere component?**

The literature search found **nothing**: no structure theorem, no dimension bound, no topological constraint on `{F⁻ = 0}`, on the rank loci beyond their characteristic classes, or on any other canonical subvariety of a YM field. Nobody appears to have asked. Absence of literature is not impossibility, and I am not going to close a direction on it — twice burned.

Three sub-questions, in order of cheapness:

1. **Unique continuation for `F⁻`.** Does `F⁻ = 0` on an open set imply `F⁻ ≡ 0` for a source-free YM connection? I could not find this stated either way. For real-analytic metrics YM connections are real-analytic in a suitable gauge, so `{F⁻ = 0}` is a *real*-analytic subvariety — which gives no topological constraint, but does bound its dimension. This is a day's work and it is the gate: without it, none of the loci are even well-behaved.
2. **The `U(2)` slot.** Build or find a `U(2)` YM field on `S⁴` (or `ℝ⁴`) and compute `{rank F⁻ ≤ 2}` for Sadun's family or an equivariant ansatz. Is it ever a 2-sphere? If it *is*, that is bad news of exactly Sadun's kind. If it provably never is, that is the isolation theorem and it unlocks the direction.
3. **The energies of the known non-self-dual solutions.** Nobody has published a numerical action for any Sibner–Sibner–Uhlenbeck / Sadun–Segert / Bor / Parker solution. Dayaprema–Waldron's "consistent with the known examples" is an assertion without numbers. Sadun's reduced ODE system is explicit and integrable numerically; recovering even one action value would test the sharp GKS bound directly and is a self-contained computation.

**And the honest prior.** (1) is likely to work and is necessary but far from sufficient. (2) is the real gate, and Sadun's evidence — that 2-spheres are where the non-self-dual solutions live, as *singular orbits* of the very symmetry group one would use — points against it. (3) is worth doing regardless because it is the one place where a number would replace an assertion.

---

## 5. A notational coincidence, flagged so it does not mislead

Sadun's quadrupole family carries fractional Chern number `c₂ = (r² − t²)/8`. Brief §2.5's discriminant is `r² − t²`. The Lehmer-pair margin (memo 15) is `Δ²/8`.

**These are unrelated.** Sadun's `(r,t)` are holonomy/bundle parameters of an `SO(3)`-equivariant ansatz; ours are `(|Im q|, ⟨Im q, e⟩)`, radial and axial coordinates on `ℍ`; Lehmer's `Δ` is a zero gap. All three are quadratic forms in two parameters, which is why they look alike. I record the coincidence explicitly because it is exactly the kind of pattern-match that would generate a spurious lead, and because I would otherwise have been tempted by it.

---

## 6. Assessment

The challenge was right on all three counts it made: full YM was not shown to fail, it does have the most freedom, and gravity is harder. The closure I claimed rested on a conjecture (memo 12 §3.5) that memo 16 had to downgrade, plus a misreading of what the current is (§1a).

What this dive adds is that the freedom and the isolation are **the same trade-off**, now documented externally: the YM system is determined where the ASD system is overdetermined — that is the freedom, and it is real and it answers memo 15's finiteness criticism. And every isolation theorem in the subject concludes self-duality — that is the cost, and it is documented across nine independent papers, with a sharp explicit constant, and with the non-self-dual sector demonstrably becoming *less* rigid as one moves into it.

Plus one thing I did not expect: for `SU(2)`, the curvature rank loci are never 2-dimensional, so they cannot match a zero-sphere set at all. That narrows the candidates to `U(2)`, and gives a concrete object to compute.

**Recommendation.** Pursue §4(1) and §4(3) — both are self-contained and cheap, and (3) replaces an assertion with a number. Treat §4(2) as the decision point: if the `U(2)` rank-2 locus can be a 2-sphere, the direction is closed by the same mechanism that closed everything else; if it provably cannot, the direction has its isolation theorem and becomes the best thing in the programme. I would put maybe 15% on the latter, mostly because nobody has looked.

**Unconfirmed, and material.** The infinite-dimensionality of the local YM solution space (folklore, no citation found — but the determined/overdetermined ellipticity contrast is solid). The actions of the known non-self-dual solutions (nobody has published one). Gursky–Kelleher–Streets Corollary 1.2's displayed constant, reconstructed from their normalisation and independently corroborated by Dayaprema–Waldron's `δ = 2`, but not read off the PDF. Whether unique continuation holds for `F⁻`. Two of the supporting items are 2026 preprints and unrefereed.

---

*Certified by `lab_ym_landscape.py`: Q1, the additive gap and its vanishing relative size; Q2, Sadun's index/nullity table against Taubes' bound; Q3, the requirement-by-requirement comparison; Q4, the rank-locus dimension ladder and the `U(2)` exception. The substantive inputs are published theorems, cited individually above; nothing in Q1–Q3 is our own mathematics, which is the point — the trade-off is being read off other people's work rather than derived from our own family.*
