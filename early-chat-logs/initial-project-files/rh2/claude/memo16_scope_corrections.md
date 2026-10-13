# Two Scope Corrections, and the Pattern They Share

*Working memo #16 — August 24, 2026. Two of this programme's negative results have been framed more broadly than their proofs support. Both were caught by a reader pushing on them, both corrections narrow the claim without changing any computation, and the pattern they share is worth naming because it predicts where the next such correction will be. Certified by `lab_equivariance_freedom.py` and `lab_jet_scope.py`.*

---

## 0. Summary

| result | as framed | as proved | status of the framing |
|---|---|---|---|
| **Proposition 1** (brief §1.3) | "any route of this shape is a hyperbolicity-criterion factory, not a proof mechanism" | a statement about *theorems of a quantified form*; silent on the single-function approach | **overstated** — Proposition 1 closed nothing. §1.2's identity is the load-bearing fact. |
| **The jet-order theorem** (memo 9, brief §2.7a) | "whatever object is built from `Ξ`, the reality information must appear at transverse order `≥ 2`" | a rigidity statement about one finite-dimensional polynomial family, which **fails one step outside it** | **overclaimed** — the screen is family-specific, not universal. |

**The pattern.** Both are cases of a *family-specific* rigidity result being read as a *universal* structural principle. Sorting the whole document by that criterion (§3) leaves exactly two genuinely universal results — §1.5's no-go theorem and §1.2's equivariance identity — and everything else family-specific. That is a smaller universal core than the brief's framing suggests, and it is the honest inventory.

---

## 1. Proposition 1 does not close the strategy

### 1.1 The objection, which is correct

Proposition 1 says: *if* one proves "`P(f) ⟹ f` admits an equivariant extension in `𝒞`" quantified over all real entire `f`, *then* `P ⟹` hyperbolic. But RH concerns **one** function. If one exhibits, for `Ξ` alone, an equivariant member of `𝒞` — by any means, with no `P` anywhere — RH follows and Proposition 1 says nothing.

That is right. And the brief's phrase "criterion factory, not a proof mechanism" is bad for a second reason: **every** serious attack on RH is a criterion plus a verification. Weil positivity is a criterion. Hilbert–Pólya is a criterion. Li's criterion is a criterion. Being a criterion is not the defect; being a *circular* criterion is.

### 1.2 What is load-bearing instead

The fact with teeth is the sentence above Proposition 1 in brief §1.2, and it applies to the single-function version exactly as much as to the quantified one.

Equivariance forces the axial form `F(q) = A(x_0,r) + ω·B(x_0,r)` with `A, B` real (verified: axial `⟹` equivariance to `2.5e−14`; break the axial form and equivariance fails by `1.45`). Since `1` and `ω` are `ℝ`-independent,

`F(q) = 0 ⟺ A(x_0,r) = 0 and B(x_0,r) = 0`

— a condition on `(x_0, r)` **only**. So the off-axis zero set is `{A = B = 0} × S²`: every off-axis zero carries its entire sphere. Verified on the rotational extension of `(z²+1)(z−1)`, which vanishes at `i`, `j`, `k` and `(i+j+k)/√3` — the whole sphere — because the stem has the pair `±i`.

> **For an equivariant `F`, "sphere-free" and "the stem has only real zeros" are the same statement.** Not equivalent by a theorem; literally the same condition, relabelled. So the class-membership condition applied to a symmetric member is not a tool for proving hyperbolicity.

### 1.3 And there is no freedom to search over

An equivariant `F` is **recovered exactly** from its restriction to a single slice: reading `A, B` off the slice and rebuilding reproduces `F` to `0.00e+00` over 500 random points of `ℍ`. Hence:

> "Equivariant, and restricts to `Ξ` on a slice" determines `F` **uniquely**: `F = RΞ`, the rotational extension.

So the single-function question is not a construction problem. It is one yes/no about one predetermined object: **is `RΞ ∈ 𝒞`?** — and since `RΞ` is determined by `Ξ`, that is a condition on `Ξ` in quaternionic clothing.

Freedom returns only if one weakens "restricts to `Ξ`". Prescribing `F` on the real axis alone leaves an infinite-dimensional family (verified: `B + cr` agrees on all of `ℝ` to `0.00e+00` and differs off it by `0.50`, `1.25` for `c = 1, −2.5`) — this is the appendix's Proposition A.5. That weakening is exactly what brief §7.1's "transform, not matching" proposed, and it is why that was the live direction.

### 1.4 What Proposition 1 is actually for

The strategy, however executed, ends at: *`𝒞` is sphere-free (a theorem about `𝒞`) plus `RΞ ∈ 𝒞` (to be verified), hence RH.* **The geometry supplies the implication and can never supply the verification.** Proposition 1 is the accounting device that catches the specific failure mode where the implication turns out to be a triviality.

It caught that three times: memo 7 (the implication was the spectral theorem, so `RΞ ∈ 𝒞` unwound to self-adjointness, i.e. Hilbert–Pólya, i.e. the conclusion); memo 8 (the condition was contentless); brief §5 (the condition was unsatisfiable). Three real instances — but note that in each case the *closing argument* was the specific computation, not Proposition 1.

**Three cases, by how `F` is attached to `Ξ`, and what actually kills each:**

| attachment | freedom | what closes it |
|---|---|---|
| restricts to `Ξ` on a slice | **none** — `F = RΞ` forced | §1.2's identity; §2 (the extension carries the same stem on every slice, so nothing was added) |
| matched by zero loci (memo 7's dictionary) | freedom in the ADHM data | §3.5 (positivity forces the collapse); §4.4 (the implication is the spectral theorem) |
| built by a transform (§7.1) | most | §1.5 (the equational no-go) |

The bottom two rows die by mechanisms Proposition 1 knows nothing about. **Proposition 1 closed nothing.**

---

## 2. The jet-order theorem is rigidity, not detection

### 2.1 The objection, which is also correct

Memo 9 says the second transverse jet along a slice forces hyperbolicity. But a jet is infinitesimal. How can it constrain zeros far from the slice, outside every neighbourhood it sees?

It cannot, and it does not claim to. **The theorem never locates a zero.** The chain is:

`2nd transverse derivative of the deficit = 0` `⟹` `S = 0` `⟹` `T_0` real symmetric `⟹` spectrum real `⟹` `p` hyperbolic.

The last three arrows are **algebra** — the spectral theorem for real symmetric matrices. Nothing in the chain is a statement about zeros in a neighbourhood. What the jet detects is a *parameter* of a finite-dimensional family; hyperbolicity then follows from the parameter by an identity.

Measured at the slice point `x_0 = 0.37`, `t = 0.83` inside the R1 family (`lab_jet_scope.py` Part A): value and first derivative vanish to `10⁻¹³` in every case; the second derivative is `0.000000` for `z²−1` and `8.000000`, `6.000000`, `1.244856` for `z²+1`, `z²+z+1` and the memo-5 quartic. The 2nd derivative is the only nonzero entry, and it is nonzero exactly for the non-hyperbolic targets.

### 2.2 Why local implies global here, and only here

The R1 family is finite-dimensional and everything in it is a polynomial, so local data pins down global data cheaply. That is the entire reason the theorem works. It is a **rigidity** statement about a family, not a statement that infinitesimal information sees hyperbolicity.

**And one step outside the family it fails completely — not merely at order 2, but at all orders at once.** Memo 12's datum (`T_0 =` companion matrix of `p`, which is *not* symmetric; `T_1=T_2=T_3=0`; `λ=0`; `C = T_0²`) gives `M(q) = (T_0 − x_0I)² + r²I` identically, so the deficit is **identically zero on all of `ℍ`**. Verified (`lab_jet_scope.py` Part B): global relative sup of `|det M − P_p|` is `1.6e−14`, `1.3e−14`, `1.7e−13` for `z²+1`, `z²+z+1`, the memo-5 quartic — with every transverse jet vanishing to `10⁻⁸` or better, and `p` **not hyperbolic**.

> So outside the R1 family, not merely the 2-jet but the **full global matching condition** — agreement at every point of `ℍ`, to every order — fails to force hyperbolicity. The order-2 threshold is entirely a fact about the R1 family, which is to say about ADHM's reality condition.

### 2.3 The corrected statement

Sorted by what is actually proved:

- **Order 0 empty.** Proved for R1 (memo 8, Theorem 5: every real monic `p` arises). Elsewhere it is a well-supported *principle* — brief §2, five independent instances — not a theorem.
- **Order 1 empty.** Proved for R1 only. The mechanism is that the deficit is **even** in `ν`, which follows from `M` depending on `q` only through `(x_0, t, ν²)`, which follows from `T_a = e_aS`. A general family's deficit need not be even, and then order 1 is not empty.
- **Order 2 collapse.** Proved for R1 only, and §2.2 shows it fails one step outside.

**So memo 9 §5's screen** — *"whatever object is built from `Ξ`, the reality-of-zeros information must appear as an obstruction at transverse order `≥ 2`; an obstruction living at order 0 or 1 is provably empty"* — **is withdrawn as stated.** The defensible version:

> Within a family whose deficit depends on `q` only through `(x_0, t, ν²)`, orders 0 and 1 are empty by evenness, and the discriminant is the transverse Hessian. That is a property of the family, to be **checked** for each new one rather than assumed.

Brief §8's screen 1′ survives with its "normal 1-jet" clause intact for the R1 family, but should carry the same caveat.

**What is not affected.** Brief §2.7(b) — that the transverse Hessian is the Fubini–Study metric on the sphere of complex structures — is a coordinate identity and stands. Brief §2.7(c) — that no Ruling-B line is `ρ`-invariant, so the σ-type invariant is not jet-local at any order — is a statement about `ρ` alone, independent of any family, and stands.

---

## 3. The pattern, and the honest inventory

Both corrections are the same mistake: a rigidity result about **one finite-dimensional family** read as a **universal structural principle**. It is an easy mistake to make here because the family-specific results kept agreeing with each other, which felt like evidence of a general law rather than of a shared setting.

Sorting everything in the document by scope:

**Genuinely universal — two items.**

- **§1.5, the equational no-go.** About `ℝ^d ⊂ ℂ^d` being totally real. Independent of every class, family, construction and dimension. This is the one result that closes things by itself.
- **§1.2, the equivariance identity.** For any equivariant `F`, sphere-freeness *is* hyperbolicity of the stem. Independent of `𝒞`.

**Family-specific, however many instances agree.**

- §2.5's deficit formula, §2.7(a)'s jet order, §3.5's positivity dichotomy, §4.4's Theorem 4, §4.5's Theorem 5, §4.6's thresholds — all inside quaternionic ADHM data.
- §5's dimension count — inside the totally-real class.
- §6.5's rigidity — inside the gravitational-instanton inventory.

**Structural but not proved.**

- §2's transverse-sphere principle. Five instances, no theorem. It should be read as a heuristic with a good track record, which is how it has in fact been used.

**Consequence for §8.** The checklist mixes screens of both kinds without marking them. Screens **0** and **1″** rest on universal facts. Screens **1′**, **6**, **7** and **0″** rest on family-specific results and are heuristics when applied to a new family — still worth running first, because they are cheap and have been right, but a proposal that fails one has not been *refuted*, only flagged. That distinction should be in the checklist and is not.

**And a prediction, since the pattern has now recurred twice.** The next result most likely to need this correction is **§3.5** (positivity is the trap), which is currently the load-bearing claim for closing full Yang–Mills. It is verified only inside the ADHM shape `M = C + |q|²I − 2Σx_aT_a`, at `k = 2,3`. Its generalisation — "any class supplying structural positivity collapses" — is exactly the kind of extrapolation that §§1–2 above show has failed twice. It should be labelled a conjecture, and the proof asked for in brief §7.4(1) should be understood as also being a test of whether the statement is even true beyond the ADHM shape.

---

*Certified by `lab_equivariance_freedom.py`: equivariance `⟺` axial form (`2.5e−14` vs `1.45`); an equivariant `F` recovered from one slice to `0.00e+00` over 500 points; non-uniqueness from real-axis data alone; and the sphere in the zero set of the extension of `(z²+1)(z−1)`. And by `lab_jet_scope.py`: the deficit jets inside the R1 family at a slice point, showing the 2nd derivative as the only nonzero entry; and memo 12's datum having identically vanishing deficit on all of `ℍ` (global relative sup `10⁻¹⁴`) with `p` non-hyperbolic. No new computations — both scripts re-derive facts already in memos 8, 9 and 12 in the form the objections asked for.*
