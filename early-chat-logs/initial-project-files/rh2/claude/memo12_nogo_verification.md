# Full Yang–Mills: Not Closed by the ADHM Theorem — Closed by Positivity Instead

*Working memo #12 — August 23, 2026. Answers a direct question: were the full Yang–Mills equations considered, or only the self-dual/ADHM case? The answer exposed an error of emphasis in memo 7 and produced a sharper diagnosis than any memo so far. Certified by `lab_nogo_verify.py` and its control.*

---

## 0. Result

**The direct answer: partially, and not in the sense that counts.** Memos 9–11 are entirely in the *full* Yang–Mills literature — Witten 1978, Isenberg–Yasskin–Green, Buchdahl, Eastwood, Pool are the **non**-self-dual correspondence; Ward/twistor space is the self-dual one. So the structure of full YM was used throughout (the order ladder, the third-order obstruction = the current). But **no full-YM object was ever built and tested the way memo 7 tested ADHM.** That gap was real, and probing it produced the following.

**(1) Memo 7's collapse theorem does NOT transfer to a class with a different reality condition, because it is exactly the spectral theorem for real symmetric matrices.** There is a closed-form counterexample as soon as symmetry is dropped:

> Take `T_0` = any real matrix with characteristic polynomial `p` (e.g. the companion matrix), `T_1 = T_2 = T_3 = 0`, `λ = 0`, `C = T_0²`. Then
> `M(q) = C + |q|²I − 2x_0T_0 = (T_0 − x_0I)² + r²I`,
> so `det M = ∏_j((x_0 − τ_j)² + r²) = P_p` with `τ_j` the eigenvalues of `T_0` = the roots of `p` — **real or not**.

Verified symbolically at `k = 2` for a *symbolic* monic `p` (`det M − P_p` simplifies to `0` in `a_1, a_0`, with no reality assumption on the roots), and numerically to `10⁻¹³` across the whole standard test set including the memo-5 quartic. Every step of memo 7 §4.4's chain survives on this datum — the trace relation `tr C = tr T_0² + tr T_e²`, `κ = 0`, `λ = 0`, `T_{1,2,3} = 0`, `C = T_0²` — and **the only step that fails is the last one, "`T_0` real symmetric, hence its eigenvalues are real."** For `p = z²+1` the counterexample is `T_0 = [[0,−1],[1,0]]`, `C = −I`, whose eigenvalues are `±i`.

Worse for memo 7's framing: the counterexample **satisfies the nonlinear ADHM equations exactly** (residual `0.0`, since `T_{1,2,3} = 0` and `λ = 0` make them vacuous). Memo 7 reported as a strengthening that "the nonlinear ADHM equations are never used". They are not merely unused — they are *irrelevant*. The entire content of the theorem is the linear part, and within the linear part, the entire content is symmetry.

**So the full-YM direction is not closed by memo 7.** The ambitwistor reality condition (IYG's "reality and currentless conditions", Pool's Minkowski/Euclidean real structures) is not ADHM's, so nothing in memo 7 applies to it.

**(2) But positivity closes it, and that is the real finding.** Searching the same shape `M(q) = C + |q|²I − 2Σx_aT_a` over nested families isolates what does the work:

| `p` | `T` gen, `C` gen | `T` gen, `C` sym | `T` gen, `C` sym **PSD** | `T` **sym**, `C` sym |
|---|---|---|---|---|
| `z²−1` (hyp) | 3.6e−15 | 3.4e−15 | 3.6e−15 | 1.4e−14 |
| `z²+1` (NOT) | **1.4e−14** | **1.2e−14** | **0.618** | **0.978** |
| `z²+z+1` (NOT) | **1.3e−14** | 0.140 | **0.316** | **0.645** |
| `(z−1)((z+2)²+9)` (NOT) | **1.4e−14** | — | **1.17** | **1.83** |

> **`C ⪰ 0` alone — with the four blocks `T_a` completely unconstrained — already forces hyperbolicity.** Thirteen orders of separation, on both non-hyperbolic targets, with `T_a` free.

And the closed-form counterexample necessarily violates it: `C = T_0²` for a conjugate pair `a ± bi` has eigenvalues `(a±bi)²`, which are non-real unless `a = 0` or `b = 0`. For `p = z²+1`, `C = −I` — symmetric, and negative definite.

**(3) The consequence, and it is the sharpest statement this programme has produced about its own failure mode.** Memo 7 §4.2 celebrated exactly this feature:

> "`C` is a sum of squares of symmetric matrices plus a Gram matrix: **the positivity is automatic.** … That is exactly the feature that made this worth testing."

It is now clear that the automatic positivity is *why the test failed*. Restated:

> **In a matching-style dictionary, structural positivity is not a resource — it is the trap.** A class that supplies positivity automatically forces the conclusion (and the argument is circular, landing on the spectral theorem or on Hilbert–Pólya); a class that does not supply it is contentless (every real monic `p` is realised). This is brief §3's rigidity/existence trade-off, localised for the first time to a specific hypothesis rather than to a class.

That closes the full-YM direction on a basis memo 7 could not have provided, and it does so *because* full YM is a gauge theory: the Yang–Mills action density `tr(F ∧ *F)` is precisely the kind of structural positivity that was the reason to recruit gauge theory for a Weil-type argument in the first place. Whatever supplies the positivity supplies the collapse.

**(4) A structural point from Pool that generalises memo 7/8's `λ = 0` defect.** Pool's Theorem IV.5 (the generalized Ward correspondence) requires `E|_{τ⁻¹(x)}` to be **trivial for every `x ∈ U`** in order to produce a connection at all. That triviality condition is exactly "no jumping over `U`". So:

> **In both correspondences, the jumping/degeneracy locus is precisely where the gauge-theoretic object fails to exist.** A genuine YM field has *no* jumping locus on its domain. Asking for a nonempty jumping locus is asking for the object not to be a YM field there.

Memos 7 and 8 recorded this as an ADHM artifact (`λ = 0` ⟹ the last row of `Δ` vanishes ⟹ not a *regular* ADHM datum). It is not an artifact. It is structural to the correspondence, self-dual and full alike, and it is the Fueter/Vekua situation of brief §2.3 again: the class is sphere-free for a trivial reason (no spheres at all), and the symmetric member with prescribed spheres is not in it.

**(5) The one genuine gap, honestly labelled.** Full YM does supply a degree of freedom ADHM structurally lacks: **the current `*J ≠ 0`** (self-dual fields are currentless). By memo 11's screen 0, "`*J = 0`" is equational and dead — but an *inequality* on the current, or on the action density Pool also computes, is **regional**, and is therefore not killed by screen 0, not killed by memo 10's jet-locality argument, and untested. It is a gap, not a lead: there is no candidate transform carrying `Ξ`'s data to a YM field, and by brief Proposition 1 an inequality would be a hyperbolicity criterion again rather than a mechanism. And by (3) above, an inequality on a positive quantity is exactly the shape that collapses.

---

## 1. Scope: what was and was not done

For the record, because the distinction is what made the question productive.

**Done.** The full-YM correspondence was read and used structurally: memo 9 §4 established the third-order characterisation; memo 10 §1.1 got the ladder order by order from Buchdahl and Eastwood; memo 11 §1 got it from Pool's Memoir directly, with exact cohomology groups and the Lemma V.1 cancellation mechanism. Memo 11's no-go was then proved at the level of the whole holomorphic category, which does cover full YM as a special case.

**Not done.** No full-YM analogue of memo 7 was constructed: no non-self-dual object was built from a polynomial and tested for the matching condition, and no full-YM reality condition was written down and checked for the collapse. Memos 9–11 addressed the *obstruction* reading of the gauge-theoretic route and left the *matching* reading in the full-YM class untouched, on the implicit assumption that memo 7 covered it. §0(1) shows that assumption was wrong.

**What the gap turned out to contain.** Not a live lead — a sharper reason for the closure, plus corrections to memo 7.

## 2. The counterexample, and where memo 7's proof breaks

Take `M(q) = C + |q|²I − 2Σ_{a=0}^{3} x_a T_a` — memo 7's shape, with no reality, symmetry or positivity imposed. Set `T_0` = companion matrix of `p`, `T_1 = T_2 = T_3 = 0`, `C = T_0²`. Then

```
M(q) = T_0^2 - 2 x_0 T_0 + (x_0^2 + r^2) I = (T_0 - x_0 I)^2 + r^2 I
```

and diagonalising `T_0` over `C` gives `det M = ∏_j ((x_0 − τ_j)² + r²)`, which is `P_p` by definition. Nothing requires `τ_j ∈ R`.

Walking memo 7 §4.4 on this datum (`lab_nogo_verify.py` Part 4), with `p = z²+1`, `T_0 = [[0,−1],[1,0]]`, `C = −I`:

| memo 7 step | on the counterexample |
|---|---|
| `tr C = tr T_0² + tr T_e²` for every unit `e` | `−2 = −2 + 0` — **holds** |
| `e ↦ tr T_e²` constant on `S²`, so `tr(T_aT_b) = κδ_{ab}` | `κ = 0` — **holds** |
| `2κ + ‖λ‖² = 0`, both terms `≥ 0`, so `κ = 0`, `λ = 0` | **holds** |
| `tr T_a² = 0` with `T_a` real symmetric forces `T_a = 0` | **holds** (they are already `0`) |
| `C = T_0²` | **holds** exactly |
| `τ_j` are eigenvalues of `T_0` real symmetric, **hence real** | **FAILS**: `eig(T_0) = ±i` |

The theorem's entire content is the last row. Its converse is what the theorem actually asserts, and that direction is fine: 400 random real symmetric `4×4` matrices give `max |Im eigenvalue| = 0` exactly.

## 3. Which hypothesis is load-bearing

The four-family table is in §0(2). Reading it carefully, three separate statements are supported and one is not:

**Supported.** (i) The widest family — `T_a` and `C` both arbitrary real — is **contentless**: an exact closed form exists for every real monic `p`, hyperbolic or not. This is rigorous, not empirical (symbolic verification for symbolic `p` at `k = 2`). (ii) `C ⪰ 0` with `T_a` unconstrained restores the collapse, on both non-hyperbolic targets tested, with `~13` orders of separation from the hyperbolic controls. (iii) Symmetry of the `T_a` independently restores it, which is memo 7.

**Not supported.** That any single hypothesis is *the* one. Symmetry of `C` alone is enough for `z²+z+1` (residual `0.140`) but not for `z²+1` (`1.2e−14`, where the closed form has `C = −I`, symmetric), so it is `p`-dependent. Neither positivity nor symmetry is necessary given the other; both are sufficient. The honest formulation is the dichotomy in §0(3), not a single culprit.

**Status of (ii).** Empirical: `k = 2` and `k = 3`, three non-hyperbolic targets, 25 random starts per family. Strong (the residual plateaus are `0.618` and `0.316` against `10⁻¹⁵` controls) but **unproven**. A proof would be the sharpest available form of the circularity diagnosis and is the one concrete calculation this memo leaves open. Sketch of where to start: the `u^{k}` coefficient of the slice identity gives `p = charpoly(T_0 + iT_e)` for every unit `e`, and the `u^{k−1}v^{k−1}` coefficient gives `tr C = tr T_0² + tr T_e²`, hence `κ = 0` — but for general real `T_a`, `tr T_a² = 0` no longer forces `T_a = 0`. What `C ⪰ 0` adds is `tr C ≥ 0`, hence `tr T_0² ≥ 0`; that alone is too weak, so the argument must use the higher coefficients or the `e`-independence more fully.

## 4. Consequence for the question asked

Full Yang–Mills does not rescue the gauge-theoretic route, for three independent reasons, of which only the second is new to this memo:

1. **The obstruction reading is dead in the holomorphic category** — memo 11 §0(3), which applies to full YM verbatim, since Witten/IYG/Pool's third-order condition is exactly an equational condition on holomorphic data.
2. **The matching reading dies on positivity** — §0(3). A class supplying structural positivity forces the conclusion; one that does not is contentless. Full YM supplies it (the action density), which is why it was attractive.
3. **The degeneracy locus is where the object fails to exist** — §0(4), now known to be structural rather than an ADHM artifact.

And the thing full YM genuinely adds over the self-dual case — a nonzero current — is the subject of the gap in §0(5), which is regional rather than equational and hence not covered by (1), but is covered by (2) if it is a positivity, and lacks any candidate construction either way.

## 5. Errata to memo 7

Three items, all in §4.4's "Independently verified, and stronger than first stated":

- **Item 2** ("the nonlinear ADHM equations are never used ... the collapse is forced before the interesting equations are consulted") is correct but under-strong. The counterexample of §2 *satisfies* the nonlinear equations exactly. They are irrelevant to the collapse, not merely unused.
- **Item 3** ("Symmetry of the `T_a` is load-bearing in exactly one place — `κ = ‖T_1‖_F² ≥ 0` — and fails for general real matrices") is **wrong as stated**. Symmetry is load-bearing in a *second and decisive* place: the final step, "`T_0` real symmetric hence its eigenvalues are real." Without it, the entire chain including the `κ` step goes through and the conclusion is false.
- **"Positive semidefiniteness of `C` is not needed anywhere"** is true of that proof and misleading as a claim about the theorem. `C ⪰ 0` is independently sufficient to force hyperbolicity with all symmetry dropped (§0(2)), so it is not inert; on the present evidence it is the more robust of the two hypotheses.

Memo 7's §8 reading — "'`p` hyperbolic' is exactly the spectral theorem for real symmetric matrices" — is not only intact but is now the whole story, and its §4.2 remark about automatic positivity should be read as identifying the trap rather than the resource.

## 6. New screen

Offered for brief §8, to sit immediately after memo 11's screen 0:

> **Screen 0″ (positivity audit).** If the class supplies positivity structurally — a PSD Gram, a sum of squares, an energy or action density, a Hodge-index form — then before computing anything, drop *every other* condition the class imposes and ask whether that positivity alone already forces the conclusion. In the ADHM shape it does, with the four blocks completely unconstrained. If it does, the argument is circular no matter what else the class contributes; and if it does not, check whether the class without positivity is contentless, which in the ADHM shape it is. Structural positivity is the feature that recommends a class for a Weil-type argument and the feature that makes it circular. Expect both.

---

*Certified by `lab_nogo_verify.py`: Part 1, the closed-form counterexample on the standard test set (`10⁻¹³` or better, with the symmetry and PSD status of each datum recorded); Part 2, exact symbolic verification at `k = 2` for symbolic monic `p` (`det M − P_p → 0`); Part 3, the three-family search; Part 4, memo 7's proof chain step by step on the counterexample plus the symmetric-matrix converse. The control isolating positivity from symmetry (`D1`/`D2`/`E2`) is in the same results file. Part 1 and Part 2 are exact; Part 3 and the control are searches, and the claim that `C ⪰ 0` alone forces hyperbolicity is empirical and explicitly unproven. Pool's Theorem IV.5 triviality condition is quoted from Mem. AMS 358 read directly.*
