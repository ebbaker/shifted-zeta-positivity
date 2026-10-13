# Round 11: the free-boson L-function derived, a refuted gap, and the seam that is actually empty

**2026-08-26.** Execution of `ROUND10` §10 items 1–3, then verified against the primary PDFs supplied
by the user. One computation, two sweeps, four papers read in full.

**Sources now verified.** All four PDFs were obtained directly and read in full: Perlmutter
2509.21672, Burnol math/0112254, Connes 2602.04022, Dorigoni–Treilis 2307.07491. Every claim below
that was previously "reconstructed" or "single-source" is now marked confirmed or corrected.

**Headline.**

1. **The free-boson derivation is confirmed exactly, including the constant.** Perlmutter's own
   eq. **(10.33)** is `Q_Z^{(c=1)}(s) = 2(r^{2s−1} + r^{1−2s})` and **(10.35)** is
   `L_Z^{(c=1)}(s) = 2^{s+1/2}(r^{2s−1}+r^{1−2s})ζ(2s)ζ(2s−1)` — what §1.2 derived from three
   in-window equations. **The zeros of the analytic factor are not discussed in the paper**, and
   they all lie on `Re s = 1/2`. The (5.8) density tension is resolved, in favour of the derivation.
2. **The Connes ↔ Fourier-optimization seam is confirmed empty, now airtight.** The full 111-item
   bibliography of Connes 2602.04022 is visible: **no Cohn, no Elkies, no Carneiro, no Chirre, no de
   Laat, no Milinovich, no Soundararajan, no sphere packing, no Fourier optimization, no
   semidefinite programming.** Round 10's "strong but not airtight" caveat is lifted.
3. **The missing step in the Connes architecture is narrower than `ROUND10` recorded.** The
   convergence `k̂_λ → Ξ` is **proved** (Fact 6.4, with an explicit rate). What remains (§6.6) is two
   specific technical facts, not an open-ended limit question.
4. **The Sonin identity is confirmed from Connes' own text**, and Burnol supplies two things the
   record did not have: a structural no-go for the naive Hilbert–Pólya limit, and an exact spanning
   threshold.
5. **The Dorigoni–Treilis transcription was exact.** The printed eq. **(4.31)** matches
   `NOTE_n4_reformulation` §2 character for character. The last provisional flag in the programme is
   lifted.

---

## 0. Dorigoni–Treilis §4.2: the transcription was exact

`ROUND10` §2 verified the residue formula by derivation, because the paper's §4.2 was unreachable.
It is now read. The printed **eq. (4.31)**, small-`y` expansion of the Fourier zero mode, contains:

> `Σ_{ρ_n}  2 ξ(t+s₁+s₂−1) ξ(t+s₁−s₂) ξ(t+s₂−s₁) ξ(t+1−s₁−s₂)`
> `        ───────────────────────────────────────────────────────  y^t  |_{t = 3/4 + iρ_n/2}`
> `        (1−t−λ)(t−λ) Γ(s₁) Γ(s₂) π^{1/2−t} Γ(t−1/2) ζ′(2t−1)`

**Character-for-character what `NOTE_n4_reformulation` §2 recorded from the seminar slides.** The
"two renderings disagreed by one unit in some arguments" worry is fully discharged: nothing was
wrong. One bookkeeping fix — the equation is **(4.31) in §4.2**, not (3.36)–(3.37); those are the
Mellin–Barnes kernel `U(a,b,r,s|t)`, which the agent recovered correctly and which is the *other*
half of the picture (the `τ₂ → ∞` side). The note should cite (4.20) for the contour representation
and (4.31) for the residues.

Three things worth adding to the record from §4.2:

1. **They report the same numerics we recomputed.** Figure 2 subtracts everything but the zeta
   contributions and compares against the first **10** zeros — *"consistent with the numerical data
   within a `10⁻¹⁹` error over the whole range of `y` considered"*; Figure 3 does it with the first
   **50**. So the sum is convergent in practice, which is what `NOTE_n4_reformulation` §3.2 asserted
   — with the corrected constant `8.07·10⁻⁶` (`ROUND10` §2.2), not `2.114`.
2. **Footnote 7 is an erratum to their own earlier paper**: *"The contribution from these poles was
   inadvertently missed in [37]."* The zeta-zero terms were missing from Dorigoni–Kleinschmidt–Treilis
   2208.14087 and added here.
3. **The N=4 line and the 2d CFT line are the same phenomenon, acknowledged in print.** Footnote 5:
   *"We are extremely grateful to Nathan Benjamin and Cyuan-Han Chang for pointing out that such
   non-perturbative corrections have to be present and for bringing [95] to our attention where very
   similar results were obtained in the spectral decomposition for the partition function of certain
   2-d conformal field theories."* And §4.2: *"Equation (4.36) is directly analogous to the crossing
   equation (3.22) derived in [95]"* — [95] being Benjamin–Chang 2208.02259.

> **So the `3/4` collision flagged in `NOTE_n4_reformulation` §4 item 5 is not a referee risk to be
> managed — it is a shared mechanism the authors themselves identified and cross-cite. Any write-up
> should lead with that rather than defend against it.**

Their own closing assessment, verbatim: *"We do not know why Riemann hypothesis should play any rôle
in the strong coupling limit of string theory, nonetheless, we find this observation extremely
fascinating and in need of further exploration."*

## 1. The compact free boson: `§10.2` derived

### 1.1 Retrieval failed; the PDF was then supplied directly

Worth recording because it cost a full agent-run. The paper is **101 pages**, not 73. Every automated
route — arXiv PDF/HTML, ar5iv, mirrors, reader proxies, aggregators — hits a fixed content window
(PDF ends mid-§5.3, p. 33; HTML at p. 6). §10.2 is p. 63, §12 p. 73, Appendix D p. 78. **Three
separate fetches fabricated §10.2 content, two of them mutually contradictory.** The blocker was the
window, not access: supplying the PDF directly resolved it instantly.

> **Standing rule: when a needed source is a long PDF, ask for the file rather than spending agent
> time on retrieval. The fabrication risk is not hypothetical — it fired three times on this paper.**

### 1.2 The derivation, from in-window equations only

Inputs, all verbatim from printed sources:

- **BCFMP** [2107.10744](https://arxiv.org/abs/2107.10744) **(3.12)** — the paper Perlmutter's §10.2
  explicitly builds on: `(Z^{c=1}, E_s) = 2 Λ(s)(r^{1−2s} + r^{2s−1})`, with
  `Λ(s) := π^{−s}Γ(s)ζ(2s) = ξ(2s)` and `Λ(s) = Λ(1/2−s)`.
- **Perlmutter (3.8):** `(Z, E_{1−s}) = (2π)^{1/2−s} Γ(s−1/2) L_Z(s)/ζ(2s)`.
- **Perlmutter (3.36):** `Q_Z(s) = 2^{1/2−s} L_Z(s)/[ζ(2s)ζ(2s−1)]`.

Send `s → 1−s` in (3.12) and use `Λ(1−s) = Λ(1/2−(1−s)) = Λ(s−1/2) = π^{1/2−s}Γ(s−1/2)ζ(2s−1)`:

> **`L_Z(s) = 2^{s−1/2} · ζ(2s) · ζ(2s−1) · 2(r^{2s−1} + r^{1−2s})`**
>
> **`Q_Z(s) = 2 (r^{2s−1} + r^{1−2s})`**

This is exactly the abstract's *"for a compact free boson, the `L`-function is a product of Riemann
zeta functions times an analytic factor."* The two zetas are `ζ(2s)` and `ζ(2s−1)`; the analytic
factor is `2^{s−1/2}Q_Z(s)`.

**Three checks, two of them independent of the derivation** (script `p1_freeboson.py`):

| check | source | result |
|---|---|---|
| derivation reproduces (3.8) from (3.12) | — | rel. diff `~10⁻³¹` at four radii × two points |
| **`Q_Z(s) = Q_Z(1−s)`** | Perlmutter **(3.37)** | holds to `10⁻³¹` — *emerges*, was not imposed |
| **`Q_Z(s) ~ μ₁^{−s}`** as `s → ∞` | Perlmutter **(5.10)** | `Q(s+1)/Q(s) → r²` exactly, so `μ₁ = r^{−2}` = the lightest scalar dimension `λ₁` |

The second and third are Perlmutter's own printed constraints on `Q_Z`, and the derived expression
satisfies both without adjustment. That is strong evidence the reconstruction is his.

### 1.3 The answer, and the paper's own version

**Confirmed verbatim.** Perlmutter §10.2:

> **(10.33)** `Q_Z^{(c=1)}(s) = 2(r^{2s−1} + r^{1−2s})`
> **(10.34)** core frequency set `S_core^{(c=1)} = {r², r^{−2}}`
> **(10.35)** `L_Z^{(c=1)}(s) = 2^{s+1/2}(r^{2s−1}+r^{1−2s}) ζ(2s)ζ(2s−1)`,
> `Λ_Z^{(c=1)}(s) = 4√π · 2(r^{2s−1}+r^{1−2s}) Λ(s)Λ(1−s)`

Identical to §1.2, constant included. He adds the reading: *"The meaning of these Riemann zeta
factors was originally unclear in [32], but the L-function perspective gives their appearance a
certain synergistic explanation: the 'simplest' CFT has the 'simplest' L-function!"*

**On the zeros of the analytic factor — the paper is silent.** What Perlmutter records is the
absence of **poles** and the *reciprocity* of `S_core` (invariance under inversion of every element),
noting via Appendix D that *"these two features are one and the same: convergence of the series down
to the critical line implies reciprocity."* He does not ask where `Q_Z^{(c=1)}` vanishes. So:

> **`Q_Z = 0` ⟺ `r^{2(2s−1)} = −1` ⟺ `s = 1/2 + iπ(2k+1)/(4 log r)`, `k ∈ ℤ`.**

Since `|r^{2s−1}| = r^{2Re s−1}` and `|r^{1−2s}| = r^{1−2Re s}`, equal moduli force `Re s = 1/2`
whenever `r ≠ 1`. Verified to `10⁻³¹` at the predicted points for `r = 0.7, 1.6, 3.0`; a scan over
`Re s ∈ [−2,4]` finds no off-line zero; at `r = 1`, `Q_Z ≡ 4`.

This is elementary — a two-term exponential sum — so it is a remark, not a result. But it is the
remark that answers the reach question, and it is worth stating against §10.2.1's general warning
that *"Epstein zetas do not obey a Generalized Riemann Hypothesis and, lacking an Euler product, can
even have zeros in the half-plane of absolute convergence."* The `c = 1` core Epstein zeta does
obey it, trivially.

> **The full zero set of the compact-boson `L`-function is `{ρ/2} ∪ {(1+ρ)/2} ∪ {1/2 + iπ(2k+1)/(4 log r)}`
> — the Riemann zeros twice over, rescaled, plus an explicit arithmetic-free on-line family.**

### 1.4 The density-bound tension: resolved, and it confirms the derivation

`ROUND11` v1 flagged an apparent conflict — the `Q_Z` zeros have density linear in `T` while
`N_ζ ~ T log T`, so (5.8)'s strict inequality looked marginal. **Perlmutter's footnote 26 resolves
it, and the resolution is a mutual confirmation:**

> *"Since the `s → ∞` asymptotic (5.10) is exponential, not factorial, on account of the cancelling
> gamma factors, the spectral gap controls a **subleading correction** to this. The correction can be
> shown to be of the form `N_{L_Z}(T) − N_ζ(T) ∼ −T log µ₁` times a positive constant."*

The bound is about the **subleading, linear-in-`T`** term — which is exactly the density of the
`Q_Z` zero family I derived (spacing `π/(2 log r)` gives `~4T log r/π` in a disc of radius `T`,
against `−T log µ₁ = 2T log r` up to the constant). And §10.2.2 closes it explicitly:

> *"At `c = 1`, the gap is bounded as `λ₁ ≤ 1/2`, with saturation at the self-dual radius `r = 1`.
> Indeed, the self-dual boson saturates the density bound: at `r = 1`, `Q_Z^{(c=1)}(s)` is constant."*

With `µ₁ = 2λ₁` and `S_core = {r², r^{−2}}`, `λ₁ = min(r², r^{−2})/2 ≤ 1/2`, equality iff `r = 1`.
**So the excess zeros the density bound predicts *are* the analytic factor's zeros, and they vanish
exactly at the self-dual radius where the bound is saturated.** Independent confirmation of both.

### 1.5 Appendix D: the find I did not expect

Appendix D proves — conditional on a weak assumption — that **in an irrational Virasoro CFT,
`Q_Z(s)` must have at least one Riemann zeta pole**, provided its series converges. The argument is
clean: no poles ⟹ convergence down to `σ = 1/2` ⟹ `Q_Z(s) = Q_Z(1−s)` forces reciprocity of the
frequency set `{µ_n} = {µ_n^{−1}}` ⟹ but Cardy growth makes `{µ_n}` dense at high energy ⟹ an
accumulation point at `λ = 0` ⟹ contradicts finiteness of a torus partition function. **The `c = 1`
free boson is the explicit contrapositive** (`{µ_n} = {r², r^{−2}}`, manifestly reciprocal, not
irrational).

And the consequence Perlmutter draws is the item worth carrying forward. Those poles force
cancellations among spin sectors (§11.2, eq. 11.19), and since spinning modes depend on Maass cusp
form data while the scalar mode does not:

> *"(11.19) implies relations between the Riemann zeta zeros `{ρ_n}` and the Maass cusp form spectral
> parameters `{u_n}`. This can be turned into a quantitative, not just a qualitative, constraint as an
> infinite set of sum rules polynomial in the Riemann and Maass data. … It would be very exciting to
> make this observation fully rigorous."*

> **This is physics ⟹ arithmetic, producing a constraint that involves the Riemann zeros, derived
> from nothing but discreteness of a CFT spectrum. It is not a location statement. But it is the
> first item in the ledger where a physical requirement yields a *new relation* on the zeros rather
> than restating a known one — and it is explicitly unwritten.** Ranked below the §4 architecture,
> above everything else in the physics column.

---

## 2. Bootstrap positivity vs Weil positivity: `ROUND10`'s gap is refuted

`ROUND10` §5 recorded, from two searches, that *"nobody has looked"* and called it a clean unworked
seam. **That was a search artifact and the finding is withdrawn.**

### 2.1 It was done in 2022, and it is the Benjamin–Chang paper itself

Their title is *"Scalar Modular Bootstrap and Zeros of the Riemann Zeta Function."* Abstract,
verbatim: *"Rather remarkably, our crossing equation contains information about all nontrivial zeros
of the Riemann zeta function. As a result, we rephrase the Riemann hypothesis purely as a statement
about the asymptotic density of scalar operators in certain two-dimensional conformal field
theories."* They use **SDPB** as the linear-programming solver (§3.4).

**Correction to `ROUND10` §5:** the sign-indefiniteness obstruction is in the **2022** paper, not
only the 2025 one. Verbatim from 2208.02259 §3.3: *"One immediate problem is that not every term in
(3.22) is sign-definite."* and *"The term `ε_c(µ)` is not sign-definite, and the infinite terms
`δ_{k,c}(µ)` are also not sign-definite for any `k`."*

### 2.2 The lesson is negative, and sharper than recorded

Both papers resolve the obstruction the same way — **by deleting the arithmetic**. Verbatim from
2505.18314 §3.3: *"To keep only the sign-definite terms, we should apply functionals that annihilate
terms of the form `y^{(1+z_k)/2}`, where `z_k`'s are the nontrivial zeros."* And the annihilation is
free, from the functional equation: *"due to the `ζ(1−s)` factor, we have `F^φ[t^{1−z_k}] = 0`."*

> **In the modular-bootstrap setting, positivity and arithmetic content are in direct competition:
> the functionals that make the problem positive are precisely the ones that project the zeta zeros
> out of the sum rule.** That is a much stronger statement than "the residues are not sign-definite,"
> and it is the real reason the Benjamin–Chang exercise has no bootstrap-shaped solution.

Also verbatim, and worth having: *"Since the Riemann hypothesis has already been checked up to
imaginary part `3×10¹²`, we emphasize that our numerics are **not** an independent check of the
Riemann hypothesis."*

### 2.3 The real bridge is Fourier optimization, and it is mature

The bootstrap-shaped attack on zeta exists, is a decade old, and lives in analytic number theory.

- **Carneiro, Milinovich & Soundararajan**, *Fourier optimization and prime gaps*,
  [1708.04122](https://arxiv.org/abs/1708.04122), Comment. Math. Helv. **94** (2019). Extremal
  problems over `F ∈ L¹(ℝ)` with `F̂` bandlimited, or with `F̂(t) ≤ 0` for `|t| ≥ 1`, applied
  through the **Guinand–Weil explicit formula** (their Lemma 6). Theorem 5: on RH there is a prime
  in `[x, x + (22/25)√x log x]`.
- **Their §7.2 is the Cohn–Elkies bridge, written out.** Verbatim: *"The following extremal problem
  in Fourier analysis was proposed by Cohn and Elkies in connection to the sphere packing problem …
  **This is the multidimensional analogue of our extremal problem (1.4) with the additional
  constraint that `F ≥ 0`.**"* The sphere-packing LP bound and the RH prime-gap bound are the same
  extremal problem differing by one constraint.
- **Chirre, Gonçalves & de Laat**, *Pair correlation estimates for the zeros of the zeta function via
  semidefinite programming*, [1810.08843](https://arxiv.org/abs/1810.08843), Adv. Math. **361**
  (2020) — SDP applied directly to zeta zeros.
- **Chirre, Pereira Júnior & de Laat**, *Primes in Arithmetic Progressions and Semidefinite
  Programming*, [2005.02393](https://arxiv.org/abs/2005.02393) — extends Guinand–Weil over all
  Dirichlet characters mod `q`, reduces to SDP, solves with SDPA-GMP.

**And the chain closes back to physics.** Modular bootstrap ≡ Cohn–Elkies LP for sphere packing
(**Hartman–Mazáč–Rastelli** [1905.01319](https://arxiv.org/abs/1905.01319);
**Afkhami-Jeddi–Cohn–Hartman–de Laat–Tajdini** [2006.02560](https://arxiv.org/abs/2006.02560), JHEP
12 (2020) 066 — Cohn and de Laat coauthoring with bootstrap physicists) ≡ Carneiro-style Fourier
optimization minus one constraint ≡ prime/zero bounds via Guinand–Weil. **Every link is published;
the chain has never been traversed end to end in one paper, and never toward Weil positivity.**
**David de Laat is the junction node**, appearing on both the sphere-packing/bootstrap side and the
zeta/SDP side.

**Known ceiling:** every result in the Fourier-optimization line is **conditional on RH or GRH**. The
method consumes the critical line and produces sharper arithmetic. It has never been run in reverse
to establish positivity of the Weil form. The sharp constants `C(∞), C⁺(∞)` are unknown in
dimension 1.

### 2.4 The template to imitate

**Kravchuk, Mazáč & Pal**, *Automorphic Spectra and the Conformal Bootstrap*,
[2111.12716](https://arxiv.org/abs/2111.12716), **Comm. Amer. Math. Soc. 4 (2024) 1–63**. Bootstrap
positivity + `PSL₂(ℝ)` representation theory + SDP ⟹ **unconditional** upper bounds on the Laplacian
spectral gap of hyperbolic surfaces, near-sharp to ten digits (genus 2: `λ₁ ≤ 3.8388976481` vs. Bolza
`3.838887258`).

Why this is the right model rather than the modular bootstrap: it is **unconditional** — positivity
alone produces new theorems; it lives in the **Selberg trace formula** setting, the geometric twin of
the Weil explicit formula; the positivity is honest, coming from inner products rather than being
projected away; and it was **published as mathematics**. It is the existence proof that a *different*
spectral decomposition in the same family has usable positivity.

### 2.5 The seam that is actually empty — now airtight

> **Connes ↔ Fourier optimization. Confirmed empty against the complete bibliography.**

`ROUND10` and `ROUND11` v1 rested this on ~60–70% of visible text with the bibliography unreachable.
The full PDF is now read. Connes 2602.04022 has **111 references**, and the following are **absent
from all of them**: Cohn, Elkies, Viazovska, sphere packing, Carneiro, Chirre, Milinovich,
Soundararajan, de Laat, Gonçalves, "Fourier optimization", "extremal function", semidefinite
programming, linear programming bounds. The caveat is lifted.

The fit remains exact. Connes' §5 extremises the Weil quadratic form over test functions supported
on primes `< 13`; Carneiro–Milinovich–Soundararajan and Chirre–Gonçalves–de Laat extremise
functionals against the Guinand–Weil explicit formula with certified SDP numerics. Same formula,
same kind of extremal problem, no contact.

**One correction to `ROUND10` §3.2.** Connes' 2026 survey *does* mention Faddeev–Pavlov — §3.1.2,
one sentence: *"The scattering approach, developed by Faddeev and Pavlov, interprets the zeros of
`ζ(s)` as resonances (poles of the scattering matrix) of a certain quantum mechanical system."* The
"absence from the expository canon" claim should be scoped to **Bombieri, Sarnak and Conrey**, which
is where it was verified. Connes mentions it and does not treat it as a route.

**Also worth recording from §4.1**: Yoshida's theorem (positivity of `W_∞` on test functions
supported in `(1/2, 2)`) is proved by *numerical* analysis, and Connes' own assessment is that *"it
does not provide any conceptual reason for this positivity that would have a chance to continue to
hold when primes are involved."* That is the honest status of archimedean positivity beyond
Connes–Consani's own Theorem 7.1.

---

## 3. Burnol: a vacuity theorem for the whole genre, and a falsification test we should be running

### 3.1 What the paper proves

Burnol, *An adelic causality problem related to abelian L-functions*,
[math/0001013](https://arxiv.org/abs/math/0001013), J. Number Theory. Working in `L²(C_K, d*u)` on
the idele class group, with `E: 𝒮(𝔸_K) → (C_K → ℂ)`,
`φ ↦ √|v| Σ_{q∈K^×} φ(qv) − (∫φ dx)/√|v|` (Definition 1.1 — essentially Connes' adelic-to-idelic map
with Tate/Iwasawa pole subtraction), and `D₊ = E(𝒮_{≤1})^⊥`, `D₋ = E(𝒮̃_{≤1})^⊥`:

> **Theorem 1.7.** *"The Riemann Hypothesis holds for all abelian L-functions of K if and only if
> `D₋ ⊥ D₊`."*
>
> **Theorem 1.11.** *"`V(closure(E(𝒮_{≤1}))) ⊂ H²` with equality if and only if the Riemann
> Hypothesis holds for all abelian L-functions of K."*

Causality is the Lax–Phillips axiom `D₋ ⊥ D₊`. **Proved unconditionally** — a genuine iff, via
Beurling–Lax invariant-subspace theory plus Tate–Iwasawa.

### 3.2 The Nyman–Beurling relation, classified

**A proved variant, not an identity — and he says so.** §2 opening, verbatim: *"When considering only
the Riemann zeta function, Theorem 1.11 boils down to a variant of Nyman's criterion."* Abstract:
*"an adelic variation on a theme initiated by Nyman and Beurling."*

Different Hilbert space (`L²(C_K, d*u)`, not `L²((0,1),du)`), different spanning family
(`E(𝒮_{≤1})`, not dilates of the fractional part), different shape (subspace equality, not
membership of a single vector) — but §2 is a *proved chain* of equivalences reducing it to Nyman at
`K = ℚ`. What is genuinely new: simultaneity over all abelian `L`-functions of `K`, coverage of
function fields, and the repackaging of the closure gap as poles of a scattering operator.

### 3.3 The remark, verbatim, with its scope resolved

Introduction, ~p. 2:

> *"The connection between our scattering process and the Riemann zeta function (or more generally an
> abelian L–function) is the following: each 'bad' zero (Re(ρ) > 1/2) appears as a pole of the
> scattering operator, where there should be none, if the process was causal. **But if the Riemann
> Hypothesis holds, then the scattering itself is of a trivial nature, and says absolutely nothing on
> the zeros on the critical line.**"*
>
> *"We point out that the same holds with the positivity criterion of Weil: the Weil distribution if
> of positive type if and only if the Riemann Hypothesis holds, but beyond that, positivity tells
> nothing on the location of the zeros except that they are indeed on the critical line."*

**Scope: his own adelic construction, explicitly extended by him to Weil positivity — not asserted of
Faddeev–Pavlov, and not asserted of scattering criteria in general.** (Faddeev–Pavlov is discussed in
an earlier, separate paragraph and never referenced after this one.) `ROUND10` §3.2 left the scope
open; it is now settled.

> **This is a vacuity statement about the whole equivalence genre, from a serious practitioner, in
> print: a criterion that becomes trivial exactly when it is satisfied cannot be a route to a proof —
> only a route to a contradiction from a bad zero. By his own extension it applies to Connes–Consani's
> Weil positivity. It applies to Nyman–Beurling and Báez-Duarte. It applies to our round-9 route.**

Use it as a design constraint, not a discouragement: **for any construction, ask what it still tells
you when RH holds.**

### 3.4 The falsification test we are not running

Burnol's own stated limitation, final sentence of his introduction:

> *"An obvious deficiency of this paper is its inability to achieve an alternative proof of the
> Riemann Hypothesis in the function field case, where it is not an hypothesis but a well-known
> theorem."*

His framework **covers function fields, where RH is a theorem, and still cannot reproduce it.**

> **New screen, cheap and discriminating: run any Nyman–Beurling-flavoured or scattering-flavoured
> architecture against the function-field case first. If it cannot reproduce Weil's theorem there, it
> is not carrying arithmetic.** This is not in any of our existing screens and it should be.

### 3.5 The Sonin space is the same object — established

- **Burnol/de Branges** (CRAS 2002): the Sonine space is the orthogonal complement of
  `L²(−λ,λ) + ℱ·L²(−λ,λ)`.
- **Connes–Consani** [2006.13771](https://arxiv.org/abs/2006.13771) **Definition 4.4**:
  `S(α,β) := {ξ ∈ L²(ℝ)_ev | ξ(q) = 0 ∀|q| ≤ α, (ℱξ)(p) = 0 ∀|p| ≤ β}`, described as *"the
  well-known infinite dimensional Sonin's space."*

Same object. And **Connes–Consani credit Burnol in print** (*The Scaling Hamiltonian*): *"In [7],
J. F. Burnol found a spectral realization of the zeros of zeta, closely related to the spectral
realization of [10], but using the Sonine spaces implemented by L. de Branges in his approach to
RH."*

> **So the Burnol line and the Connes–van Suijlekom architecture of `ROUND10` §4.1 share a concrete
> Hilbert-space object, and Connes says Burnol got a spectral realisation of the zeros inside it.**
> That makes available to the §4.1 architecture: Burnol's explicit de Branges structure functions
> `E_λ(z)` (CRAS 2002), his completeness/minimality results for the zeros in extended Sonine spaces
> ([math/0203120](https://arxiv.org/abs/math/0203120)), and his `HP_λ` spaces — an existing,
> worked-out Hilbert–Pólya proposal built to interface with the BBLS distance function.

### 3.6 Nyman–Beurling: the quantitative barrier

- **Best unconditional lower bound:** BBLS (Adv. Math. 2000) `liminf d_N² log N ≥ Σ_{Re ρ=1/2} 1/|ρ|²`,
  sharpened by **Burnol** (Adv. Math. **170** (2002) 56–70) to `Σ_ρ m_ρ²/|ρ|²` — **multiplicity
  squared**. Note `Σ_ρ 1/|ρ|² = 2 + γ − log 4π ≈ 0.0461`.
- **Conjectured asymptotic, unproved:** `d_N² ~ (2 + γ − log 4π)/log N`. **Bettin–Conrey–Farmer**
  [1211.5191](https://arxiv.org/abs/1211.5191) prove it conditionally on RH *and* on
  `Σ_{|Im ρ|≤T} 1/|ζ′(ρ)|² ≪ T^{3/2−δ}` — their stated obstruction, verbatim: *"This generates some
  issues concerning convergence of certain sums of `1/ζ′(ρ)`, which force us to assume condition
  (2)."*
- Best unconditional upper bound is of shape `≪ (log log N)^{5/2+ε}/√(log N)` — exponent `1/2`
  against a conjectured `1`, so upper and lower bounds are still a **square** apart.
- **The lower bound *is* the conjectured answer.** The entire content of the approximation problem is
  already accounted for by the zeros; there is no slack for a new mechanism to live in. This is
  §3.3's vacuity, quantified.
- The one line attempting to make the criterion *produce* arithmetic short of RH:
  **Alouges–Darses–Hillion**, JTNB (2022) — sufficient conditions for a zero-free strip
  `1/2 < σ ≤ σ₀ < 1`. Worth watching.

**Correction to check:** the theorem is Báez-Duarte, Balazard, Landreau and **Saias** — not Voros.
If `ROUND9_nyman_beurling_and_close.md` attributes it to Voros, fix it there.

### 3.7 What §§5–6 actually contain — three things new to the record

Now read in full. Beyond the lower bound, Burnol's habilitation supplies three items the programme
did not have.

**(a) A structural no-go for the naive Hilbert–Pólya limit.** He constructs Hilbert vectors
`Y^λ_{s,k}` from the Báez-Duarte operator `U` (scale-invariant, multiplier
`U(s) = [ζ(1−s)/ζ(s)]·[s/(1−s)]`) satisfying `(A, Y^λ_{s,k}) = (−d/ds)^k[(s−1)/s · ζ(s)/s]`, such
that **the only ones exactly perpendicular to `A` and its contractions are the `Y^λ_{ρ,k}` with
`ζ(ρ) = 0`, `k < m_ρ`** — "this connects the Nyman–Beurling criterion with the so-called
Hilbert–Pólya idea." The asymptotics are
`lim_{λ→0}|log λ|^{−1−k−l}(Y^λ_{s₁,k}, Y^λ_{s₂,l}) = 0` for `s₁ ≠ s₂` and `= 1/(k+l+1)` for
`s₁ = s₂`, so the rescaled `X^λ_{s,0} = Y^λ_{s,0}/√|log λ|` become **orthonormal in the limit**.
Then, verbatim:

> *"The limit can not work inside `L²((0,∞))` because this is a separable space! In fact one shows
> without difficulty that the vectors `X^λ_{s,k}` weakly converge to 0 as `λ → 0`."*

> **The Hilbert–Pólya vectors become asymptotically orthonormal and simultaneously weakly converge to
> zero. The limiting "Hilbert–Pólya space" cannot live in a separable Hilbert space.** That is a
> structural obstruction of exactly the type the programme collects, from inside the construction
> rather than imposed on it, and it is not in any of our notes.

**(b) An exact spanning threshold.** Theorem 6.20/6.30: the evaluators `Z^λ_{ρ,k}` attached to the
nontrivial zeros **span the Sonine space `K_λ` if and only if `λ ≥ 1`** — and for a Dirichlet
`L`-function of conductor `q`, iff `λ ≥ 1/√q`. Below threshold, `K_λ = W'_λ ⊥ Z_λ`, and `HP_λ` (the
perpendicular complement of the co-Poisson space) is *defined* as the deficiency. So the
Hilbert–Pólya shortfall is not vague: it is measured by `λ < 1`, exactly.

**(c) The Krein string of zeta — introduced and abandoned.** Whether `W_λ ⊂ W'_λ` is strict is tied
to Krein spaces of entire functions of finite exponential type attached to the measure
`|ζ(1/2+iτ)|² dτ/2π` on the critical line. Verbatim:

> *"It seems that this Krein string is considered here for the first time, but we add immediately
> that we do not provide anything beyond mentioning it!"*

**A concrete object attached to `ζ`, named by a serious practitioner in 2002, explicitly undeveloped,
and — as far as this round could tell — still undeveloped.** It sits in the same de Branges/Sonine
world that Connes–Consani now use for Weil positivity. Worth a search of its own.

**(d) A decomposition matching the programme's own split.** Note 5.6: `D(λ)²` has two components —
distance to the subspace `M_Λ`, where *"the first step has absolutely no arithmetic, it is a problem
of analysis"*, and the additional distance inside it, where the `Y^λ_{ρ,k}` are the obstructions.
That is the product-side/coefficient-side split of `NOTE_existence_loophole` §6, arrived at
independently and 20 years earlier.

**(e) §7, for the record, is speculation and he says so.** Zeta as a *"multiplicative wave-field
renormalization"*; each `L`-function a universality domain; the zeros as critical exponents of an RG
flow; a conjectured Kramers–Wannier-style duality exchanging the number-theoretic low-temperature
phases with a single random-matrix hot phase, with `λ` as temperature, whose interaction with the RG
flow *"would result in a property of causality equivalent to the Riemann Hypothesis"*. No content
beyond the picture — but it is the same instinct as our boundary-data framing, and it ends where
ours does, at class field theory.

---

## 4. The Connes architecture, corrected and sharpened

`ROUND10` §4.1 recorded the missing step as "convergence as `x → ∞`." Reading §§6–7 makes it
narrower and more tractable, and it also shows the architecture is more complete than recorded.

**What is proved.**

- **Theorem 6.1** (Connes–van Suijlekom, *Comm. Math. Phys.* **406**:312), verbatim: *"Let `L > 0`,
  `D` be a real distribution on the interval `[0,L]` and `D̃` the associated even distribution on
  `[−L,L]`. Assume that the quadratic form with Schwartz kernel `D̃(x−y)` defines a lower-bounded
  selfadjoint operator on `L²([−L/2, L/2])`, and that the minimum of its spectrum is a simple,
  isolated eigenvalue, with even eigenfunction `η`. Then all the zeros of the entire function
  `η̂(z)`, `z ∈ ℂ`, Fourier transform of `η` lie on the real line."* Proof via Carathéodory–Fejér on
  Toeplitz matrices plus Hurwitz. **The theorem never mentions zeta.**
- **Fact 6.4, and this is the part `ROUND10` got wrong**: *"The Fourier transform of `k_λ` converges,
  when `λ → ∞`, towards the Ξ-function of Riemann uniformly on closed substrips of the open strip
  `ℑ(z) < 1/2`,"* with the difference controlled on `ℑ(z) = α` by `cλ^{−1/2−α}(1−2α)^{−1}`.
  **The convergence of the approximating family to `Ξ` is a theorem, with a rate.**

**What is missing — §6.6, in full:**

> *"In order to apply Theorem 6.1 one needs to show that the smallest eigenvalue of the Weil
> quadratic form `QW_λ` is simple with even eigenvector. The analogue of this property is known for
> the prolate wave operator. Moreover it still remains to show that `k_λ` is a sufficiently good
> approximation of `θ_x`, `λ = √x`."*

So the gap is **two specific technical facts**: (i) simplicity and evenness of the minimal
eigenvalue of `QW_λ` — the hypothesis of Theorem 6.1, known for the prolate analogue; (ii) that the
prolate-built `k_λ` really approximates the true minimal eigenvector `θ_x`. Not an open-ended limit
question. The Letter's *"this is something which at this point is not proved"* is about the
composite; the components are separately identified.

**And both spectral regimes now have operators**, which `ROUND10` did not record:

| regime | object | status |
|---|---|---|
| infrared | rank-one perturbations `D^{(λ,N)}_log` of the scaling spectral triple on `[λ^{−1}, λ]`, whose spectrum *is* the approximation to the low-lying zeros; regularized determinants `det_reg(D^{(λ,N)}_log − z)` conjecturally → `Ξ` | [30], Zeta Spectral Triples |
| ultraviolet | the prolate wave operator `PW_λ` restricted to the **Sonin space** — selfadjoint, discrete spectrum, negative eigenvalues `ν_k` with `2√ν_k` (at `λ = √2`) reproducing the UV behaviour of the zeros | Connes–Moscovici, PNAS **119** (2022) |

The UV half is what fixes the defect Connes names in §3.4.2 — that comparing zeros to GUE requires a
height-dependent rescaling, so *"any correspondence between zeta zeros and random matrix eigenvalues
must be inherently local and cannot arise from a simple, fixed spectral operator."*

**The Sonin space is the joint.** Connes §7.2, verbatim: *"the main source of positivity is due to
the Sonin space, first introduced in the context of RH by Burnol [9–11]."* It carries archimedean
Weil positivity (Theorem 7.1: `W_∞(g*g^*) ≥ Tr(ϑ(g)Sϑ(g)^*)`) **and** the UV spectral realisation.
Burnol's papers are references [9], [10], [11]. §3.5 also records that the whole NCG line originated
in **Bost–Connes** — *"a system of quantum statistical mechanics exhibiting phase transitions and
having the Riemann zeta function as partition function"* — which corrects the framing in
`ROUND10` §7: Bost–Connes is not a dead end but the historical root of the live architecture, even
though its own rigidity is aimed at Hilbert's twelfth problem.

## 5. Corrections to Round 10 and to Round 11 v1

1. **`ROUND10` §5's "clean unworked gap" between bootstrap positivity and Weil positivity is
   withdrawn** (§2). Benjamin–Chang 2022 *is* that connection; the sign-indefiniteness quote is in
   the 2022 paper, not only the 2025 one; and the correct lesson is that bootstrap positivity is
   purchased by annihilating the zeta content.
2. **`ROUND10` §10 item 1 asked the wrong question.** "Is the analytic factor zero-free?" — it is
   not, and that is the better outcome (§1.3).
3. **`ROUND10` §4.1 mis-stated the missing step** as open-ended convergence. `k̂_λ → Ξ` is proved
   with a rate (Fact 6.4); what remains is two named technical facts (§4).
4. **`ROUND10` §3.2's "absent from the expository canon" must be scoped to Bombieri, Sarnak and
   Conrey.** Connes' 2026 survey does mention Faddeev–Pavlov, in one sentence (§2.5).
5. **`ROUND10` §7 framed Bost–Connes as a dead end.** It is the historical root of the live
   architecture — Connes' own footnote 8 — even though its rigidity targets Hilbert's twelfth
   problem (§4).
6. **`ROUND11` v1's (5.8) density tension is resolved**, and resolves in favour of the derivation
   (§1.4).
7. **`ROUND11` v1 under-reported `ROUND10`'s Connes item**: both IR and UV regimes have operators
   (§4).
8. Perlmutter is **101 pages**, unpublished, and defeated ~40 automated retrieval attempts with three
   fabrications. The fix was to ask for the file (§1.1).
9. **`NOTE_n4_reformulation` §2's transcription caveat is withdrawn entirely** (§0); its equation
   reference should be **(4.31)/§4.2**, not (3.36)–(3.37). Its §4 item 5 should be rewritten: the
   Benjamin–Chang connection is cross-cited by the authors, not a hazard.

## 6. What to do next

0. **Rewrite `NOTE_n4_reformulation`.** Formula confirmed against print (§0), constant corrected to
   `8.07·10⁻⁶` (`ROUND10` §2.2), equation references fixed, §4 item 5 reframed. It is the one
   writable item in the programme and every caveat on it is now discharged. **Do this first — it is
   an afternoon.**
1. **Write the free-boson note.** `L_Z`, `Q_Z`, the on-line zero family, the density-bound
   consistency. It is now a page: the formulas are confirmed against §10.2, the derivation is
   independent, and the zero observation is unremarked in the paper. Perlmutter poses the question in
   §3.1(vi) and is the natural recipient.
2. **The Riemann–Maass sum rules** (§1.5, Perlmutter §11.2 and Appendix D). The first item in the
   physics column where a physical requirement — discreteness of a CFT spectrum — yields a *new*
   relation on the Riemann zeros rather than restating a known one. Explicitly unwritten, explicitly
   flagged by the author as *"very exciting to make rigorous"*. **Highest-value physics item.**
3. **Connes ↔ Fourier optimization** (§2.5), now airtight. Concretely: can Chirre–Gonçalves–de Laat's
   certified SDP machinery be pointed at `QW_λ` — in particular at §6.6's item (i), simplicity and
   evenness of the minimal eigenvalue, which is a finite-dimensional extremal fact at each cutoff?
   **Highest-value item overall.**
4. **The Krein string of `ζ`** (§3.7c). Attached to `|ζ(1/2+iτ)|²dτ/2π`, named 2002, undeveloped,
   in the same Sonine/de Branges world Connes–Consani now use. Cheap to scope: does anything exist?
5. **Record Burnol's weak-convergence obstruction** (§3.7a) in `NOTE_existence_loophole`'s screen
   list. Any construction proposing a limiting Hilbert–Pólya space must say how it evades
   separability.
6. **Run the function-field falsification test** (§3.4) against our round-9 Nyman–Beurling route.
7. **Do not pursue:** the modular bootstrap as a route to Weil positivity (§2.2); Perlmutter's sum
   rule as a location statement (RH-insensitive by his own 4.38); further automated retrieval of long
   PDFs when the file can be supplied.

## 7. Reproduction

| script | produces |
|---|---|
| `p1_freeboson.py` | §1.2–1.3 — the derivation, the three consistency checks, the zero locations, the off-line scan |

Dependencies: `mpmath`.

**Retrieval note.** Perlmutter 2509.21672 defeated ~40 automated attempts across arXiv (abs/pdf/html,
v1, cache-busting variants, fragment anchors), ar5iv, `web3`/`export`/`xxx.lanl.gov` mirrors,
`r.jina.ai`, microlink, `md.dhr.wtf`, textise, bytez, papers.cool, emergentmind, alphaxiv, synthical,
scite and INSPIRE — and produced three fabricated "§10.2" readings in the process. Burnol
math/0112254 §§5–6 and the Connes 2602.04022 bibliography were likewise beyond every HTML truncation
point. **All four were resolved in one step by the user supplying the PDFs.** The blocker is a fixed
content window, not access control.

## 8. Sources

Perlmutter [2509.21672](https://arxiv.org/abs/2509.21672) v1, 101 pp., read in full — §3.3
(3.35)–(3.37), §4 (4.14), §5.1 (5.8) and fn. 26, §10.2 (10.33)–(10.35), §10.2.2, §11.2, App. D ·
BCFMP [2107.10744](https://arxiv.org/abs/2107.10744) (3.12) · Benjamin–Chang
[2208.02259](https://arxiv.org/abs/2208.02259) §3.3 · BCFR
[2505.18314](https://arxiv.org/abs/2505.18314) §3.3 · Carneiro–Milinovich–Soundararajan
[1708.04122](https://arxiv.org/abs/1708.04122) §7.2 · Chirre–Gonçalves–de Laat
[1810.08843](https://arxiv.org/abs/1810.08843) · Chirre–Pereira–de Laat
[2005.02393](https://arxiv.org/abs/2005.02393) · Hartman–Mazáč–Rastelli
[1905.01319](https://arxiv.org/abs/1905.01319) · Afkhami-Jeddi–Cohn–Hartman–de Laat–Tajdini
[2006.02560](https://arxiv.org/abs/2006.02560) · Kravchuk–Mazáč–Pal
[2111.12716](https://arxiv.org/abs/2111.12716) (Comm. AMS 4 (2024) 1–63) · **Connes
[2602.04022](https://arxiv.org/abs/2602.04022), read in full incl. all 111 references** — §3.1.2,
§3.4.2, §4.1, §5, §§6.1–6.6, §§7.1–7.6 · Connes–van Suijlekom
[2511.23257](https://arxiv.org/abs/2511.23257) (Comm. Math. Phys. 406:312), Thm 6.1 ·
Connes–Moscovici, PNAS 119 (2022) no. 22 · Connes–Consani, Selecta Math. 27 (2021) no. 77 (Weil
positivity, archimedean) and Enseign. Math. 69 (2023) 93–148 (spectral triples and ζ-cycles) ·
Yoshida, Adv. Stud. Pure Math. 21 (1992) 281–325 · **Burnol
[math/0112254](https://arxiv.org/abs/math/0112254) v6 (Forum Math. 16 (2004) 789–840), read in
full** — §§2, 5, 6, 7; Thm 5.1, Note 5.6, Thm 6.14/6.28, Thm 6.20, Thm 6.30, Def. 6.15 ·
Burnol, Adv. Math. 170 (2002) 56–70 · Burnol [math/0001013](https://arxiv.org/abs/math/0001013)
(J. Number Theory) · Báez-Duarte–Balazard–Landreau–Saias, Adv. Math. 149 (2000) 130–144 ·
Bettin–Conrey–Farmer [1211.5191](https://arxiv.org/abs/1211.5191) · Alouges–Darses–Hillion, JTNB
(2022) · de Branges, J. Math. Anal. Appl. 9 (1964) 433–457 · Krein, Izv. Akad. Nauk SSSR 11 (1947)
· Dym–McKean, *Gaussian processes, function theory, and the inverse spectral problem* (1976) ·
Dorigoni–Treilis [2307.07491](https://arxiv.org/abs/2307.07491)
