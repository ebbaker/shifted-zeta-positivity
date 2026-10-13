# Connes §6.6(i): already a theorem at the wrong end, and the one experiment nobody has run

**2026-08-26 (v2, same day — v1 is superseded and its central claim is withdrawn).** Execution of
`ROUND11` §6 item 3, ranked there the highest-value item overall. The question was: *can certified
SDP machinery be pointed at Connes' §6.6 item (i) — "the smallest eigenvalue of the Weil quadratic
form `QW_λ` is simple with even eigenvector"?*

> **v1 → v2.** v1 derived a Beurling–Deny/Perron–Frobenius argument for §6.6(i) and flagged it as
> possibly new, subject to a literature check. **The check refuted it.** Masatoshi Suzuki, *Weil's
> quadratic form via the screw function* ([2606.09096](https://arxiv.org/abs/2606.09096), Jun 2026,
> rev. Aug 2026), **Theorem 1.4**, proves exactly that statement by exactly that architecture —
> Beurling–Deny → irreducibility → Lenz–Stollmann–Veselić → positivity-improving semigroup →
> Perron–Frobenius simplicity → fixed sign → even. v1 also had a construction error (§2 below).
> Both are corrected here. **What survives is better than what was withdrawn**, and it is §§3–5.

**Headline.**

1. **§6.6(i) is a theorem — for sufficiently small `a = log λ`.** Suzuki Theorem 1.4, verbatim:
   *"For sufficiently small `a > 0`, the lowest eigenvalue `λ_a` is positive, simple, and satisfies
   `λ_a = log(1/a) + µ₁ − log(2π) + ψ(2) − 1 + O(a)` … Furthermore, the corresponding eigenfunction
   is even."*
2. **But small `a` is the trivial end, and RH needs `a → ∞`.** At small `a` the form is dominated by
   the shift `log(1/a)·‖v‖²`, which diverges to `+∞`; the whole difficulty of Weil positivity is at
   large `a`, where `ε(λ)` collapses like `e^{−4πλ²}`. **§6.6(i) is settled where it is easy and open
   where it matters.** As far as I can find, nobody has written that down.
3. **The two literatures have not met.** Suzuki cites Connes–Consani–Moscovici
   [2511.22755](https://arxiv.org/abs/2511.22755) but **not** Connes–van Suijlekom
   [2511.23257](https://arxiv.org/abs/2511.23257) and **not** Connes' 2026 survey
   [2602.04022](https://arxiv.org/abs/2602.04022) (the string "Suijlekom" does not occur in his
   paper). Connes' survey does not cite Suzuki. Groskin's numerics
   ([2605.20224](https://arxiv.org/abs/2605.20224)) do not cite Suzuki. **Three groups, one operator,
   no citations between two of the three pairs.**
4. **The concrete open experiment is the odd sector.** Groskin already runs `dps = 500` Galerkin
   numerics on `QW_λ` out to prime cutoff `c = 100`, with a genuinely rigorous ingredient (an Arb
   interval `LDLᵀ` factorization certifying no negative even-sector eigenvalues). But he
   **diagonalizes the even block only** — *"Only the even sector is diagonalized"*, *"The odd-sector
   zero, if any, is not probed here."* And §6.6(i) at large `a` is precisely the comparison
   `µ_even < µ_odd`. **Nobody has computed the odd sector. That is cheap, unoccupied, and exactly the
   missing datum.**
5. **The near-degeneracy is real and is the whole content.** In my own grid computation the two
   lowest eigenvalues differ by 1–5% of their own size, and **which of them is even flips as the grid
   is refined**. §6.6(i) at large `a` is not a general spectral question — it is one near-degenerate
   pair and a parity assignment.

---

## 1. The operator, and the identification with Suzuki's

Connes ([2602.04022](https://arxiv.org/abs/2602.04022) §6.4, eq. **(19)** in v1 — *not* (16), a
reference `ROUND11` should fix): *"There is … for each `λ>1` a canonical lower bounded, unbounded
selfadjoint operator `A_λ` with compact resolvent, in the Hilbert space `L²([λ^{−1},λ], du/u)` such
that `QW_λ(f,f) = ⟨A_λ f | f⟩`."* Then: *"The numerical computation of the smallest eigenvalue
`ε(λ)` … shows that `ε(λ)` tends exponentially fast to 0 as a function of `µ = λ²`."*

Suzuki's `A_a` **is the same operator in additive coordinates**, and he says so — §1.1, verbatim:
*"(here we reformulate their results, originally stated on `[1/λ, λ]`, in terms of the variable
`a = log λ`)"*. So `A_a ≅ A_λ` under `u = e^x`, `a = log λ`, and `λ_a = ε(λ)`.

What Suzuki adds is a **concrete realization**. His Theorem 1.1: `A_a` is the **Friedrichs extension
of `B_a = D* G_a D` on `H¹₀(−a,a)`**, where `D = i d/dx`, `(Gu)(x) = ∫g(x−y)u(y)dy`, and `g` is the
**screw function** of `ζ` — a *continuous* function replacing the distributional kernel
`k(t) = Σ_{ξ(1/2+iγ)=0} e^{−iγt}`. That is what makes the Dirichlet-form argument available; the
abstract form operator does not obviously support it.

---

## 2. Correction to v1: the pole terms, and where the Metzler claim actually holds

v1 built the operator from `−Σ_v W_v` and found its off-diagonal Schwartz kernel to be everywhere
non-positive — verified, 0 positive entries out of 159 600. **That part is correct, but `−Σ_v W_v` is
not `Q_W`.** The explicit formula is

> `f̂(i/2) − Σ_ρ f̂(ρ) + f̂(−i/2) = Σ_v W_v(f)`,

so `Q_W(F) := Σ_ρ f̂(ρ) = [f̂(i/2) + f̂(−i/2)] − Σ_v W_v(f)`, and for `f = F * F̃` the two pole terms
are

> `|∫F(t)e^{t/2}dt|² + |∫F(t)e^{−t/2}dt|²`,

**two rank-one positive operators with strictly positive kernels `e^{(t+s)/2}` and `e^{−(t+s)/2}`.**
They lift the spectrum — and they **break the Metzler property**. v1's "constrain to
`ĝ(±i/2) = 0`" was standing in for them; numerically the two agree to five digits
(`e₀ = +0.0745186` with the pole terms vs `+0.0745297` constrained, at `x = 13, N = 400`), which is
the check that the two formulations are the same problem. Suzuki imposes **no** constraints — the
string `±i/2` does not occur in his paper — because the pole terms carry that job.

> **Corrected scope.** `−Σ_v W_v` is Metzler; `Q_W` is not. Suzuki obtains positivity-improving
> anyway, but in the *derivative* realization on `H¹₀`, where the pole terms become the spectral shift
> `log(1/a) − (2A+1)` and the rescaled limiting form
>
> `𝓛(w) = ¼∫∫ |w(x)−w(y)|²/|x−y| dx dy − ½∫|w(x)|² log(1−x²) dx`
>
> is manifestly Beurling–Deny: **jumping kernel `|x−y|^{−1}`, killing measure `−log(1−x²) ≥ 0`.**
> That jumping kernel is exactly the `a → 0` limit of `(1/a)·1/(2 sinh|a(x−y)|)` — the kernel v1
> identified. **The identification was right; the realization was wrong.**

---

## 3. What Suzuki proves, and why it is at the wrong end

The chain, with the load-bearing quotes:

- **§5.1, positivity.** *"We claim that `inf_{‖v‖=1} 𝓛̄(v) > 0.`"* Proof by contradiction: `𝓛 ≥ 0`
  termwise; if `𝓛(vₙ) → 0` the jumping term vanishes, forcing a subsequence to converge to a
  constant, but *"the second term in (4.4) is strictly positive for constant functions"*. Hence
  *"for sufficiently small `a > 0`, we obtain `λ_a = inf_w R(a,w) > 0`."*
- **§5.2, positivity improving.** Markov property from *"the Beurling–Deny representation (4.4) …
  [Fukushima–Oshima–Takeda, Theorem 3.2.1]"* via the unit contraction; irreducibility from
  *"Because the jumping kernel `|x−y|^{−1}` is positive on `(−1,1)²`, the above identity cannot hold
  when both `A` and `Aᶜ` have positive measure"*; then *"By [Lenz–Stollmann–Veselić, Theorem 1.4],
  the irreducibility implies that the associated semigroup `{e^{−tT} | t>0}` is positivity
  improving."* Note the operator is **`T`**, the limiting `a`-independent operator of `𝓛̄` — not
  `A_a`.
- **§5.3, simplicity and parity.** Simplicity for `T` by the standard argument (*"two functions that
  are positive almost everywhere cannot be orthogonal to each other"*); transfer to `λ_a` by Kato
  analytic perturbation (*"as `a → 0+`, this operator has the same multiplicity for its lowest
  eigenvalue as `T`"*); then, verbatim:

> *"As discussed in Section 4.5, the eigenspaces … decompose into even and odd parts. In particular,
> since the lowest eigenvalue is simple, its eigenfunction must be either even or odd. However, since
> the eigenfunction corresponding to the lowest eigenvalue has a fixed sign, it must be even."*

**Every step is conditioned on small `a`, and the conditioning is not cosmetic.** The transfer to
`λ_a` is a *perturbation off `a = 0`*: `R(a,v) = log(1/a) − (2A+1) + 𝓛(v)/‖v‖² + O(a)`, valid *"for
`0 < a < (1/2)log 2`"*. The `log(1/a)` shift is what makes `λ_a` positive at all at that end, and it
`→ +∞` as `a → 0`. Meanwhile RH needs `a → ∞`, where `ε(λ) ≈ C λ⁹ e^{−4πλ²}` collapses.

> **So the honest statement is: `§6.6(i)` holds unconditionally near `a = 0`, by a Dirichlet-form
> argument; the `a → ∞` case — the only one that bears on RH — is untouched, and the small-`a` proof
> gives no leverage on it, because the whole argument is a perturbation off the wrong endpoint.**

Suzuki knows what he has supplied, and says so: *"In our framework, however, the simplicity of `λ_a`
and the evenness of the corresponding eigenfunction follow naturally for sufficiently small `a`."*
What he does not say — because he is not writing about Connes' §6.6 — is that the Connes programme
needs the other end.

---

## 4. The near-degeneracy, and the one experiment nobody has run

My own computation (`c1_weilform.py`, piecewise-constant grid on `[−L/2, L/2]`, `L = 2 log λ`, with
the pole terms restored):

| `x = λ²` | `N` | `e₀` | `e₁` | gap | gap/\|e₀\| | parity of `e₀` |
|---|---|---|---|---|---|---|
| 13 | 400 | `+0.0745186` | `+0.0751278` | `6.1 × 10⁻⁴` | 0.8% | even |
| 13 | 800 | `+0.0891987` | `+0.0900620` | `8.6 × 10⁻⁴` | 1.0% | even |
| 30 | 400 | `−0.1841104` | `−0.1802583` | `3.9 × 10⁻³` | 2.1% | even |
| 30 | 800 | `−0.0491356` | `−0.0467909` | `2.3 × 10⁻³` | 4.8% | **odd** |
| 60 | 400 | `−1.0830592` | `−1.0027261` | `8.0 × 10⁻²` | 7.4% | even |
| 60 | 800 | `−0.5357437` | `−0.5306773` | `5.1 × 10⁻³` | 0.9% | even |

The bottom drifts toward `0` as the grid refines, matching `ε(λ) → 0⁺`. The two lowest eigenvalues
form a **near-degenerate even/odd pair**, and at `x = 30` the parity of the numerically-lowest one
**flips between `N = 400` and `N = 800`**. A crude grid cannot settle this — as it should not, since
the true `ε` at `x = 13` is of order `10⁻⁶⁷` and the grid returns `10⁻²`.

> **§6.6(i) at large `a` is therefore a single, sharply posed question: within one near-degenerate
> pair of opposite parity, is the even member the lower?**

And here is the gap in the existing numerics. Groskin ([2605.20224](https://arxiv.org/abs/2605.20224),
v4 Aug 2026, 46 pp) runs a Fourier/cosine Galerkin discretization of the Connes–van Suijlekom
`QW_λ` at `dps = 500`, prime cutoffs `c = 13 … 67` and `c = 100`, recovering `γ₁,…,γ₁₀` to
**307–329 matching digits** at `c = 100, N = 250`, with the smallest positive even eigenvalue
reaching `~10⁻³³⁴`. He includes one rigorously certified ingredient — *"A cutoff-free evaluation of
the archimedean entries, certified by a rigorous interval `LDLᵀ` factorization in Arb, leaves the
`c = 100` even sector with no negative eigenvalues at `N = 100, 150` and `200`."* He is scrupulous
about the rest: *"We make no claim of proof"*, *"We do not claim any progress on RH"*, and Remark 2.1
concedes that simplicity and evenness are treated *"as numerical conditions, not as analytically
established hypotheses of the continuum theorem."*

But:

> *"Only the even sector is diagonalized."* — *"The odd-sector zero, if any, is not probed here."*

> ### The experiment
>
> **Compute the odd sector at the same cutoffs and precision, and compare `µ_odd⁽¹⁾` against
> `µ_even⁽¹⁾`.** The blocks decouple identically, so this is a re-run of existing code on the other
> block — hours, not months. Outcomes:
>
> - `µ_even < µ_odd` with a clean margin at every `c` up to 100 → the first numerical evidence that
>   §6.6(i) survives to large `a`, and a measured gap to extrapolate.
> - The margin shrinking with `c` → a quantitative obstruction, and far more informative.
> - `µ_odd < µ_even` at some `c` → **§6.6(i) is false at that `c`, and Connes' Letter's central claim
>   fails there.** That would be the single most valuable negative result available in this area.
>
> Nobody has looked. This is the cheapest high-value experiment the programme has identified in
> twelve rounds.

---

## 5. What certified SDP can and cannot do, revised

The original question, answered with the field state now known.

**The statement decomposes into two certifiable inequalities.** `A_λ` commutes with `t ↦ −t`, so it
block-diagonalises, and §6.6(i) is `µ_even⁽¹⁾ < µ_odd⁽¹⁾` and `µ_even⁽¹⁾ < µ_even⁽²⁾`. Upper bounds
are easy and rigorous (evaluate the form on a trial function in interval arithmetic — every
ingredient is explicit). Lower bounds are the SDP part, and are exactly the shape the certified
Fourier-optimization machinery handles: a positivity certificate for `A_λ|_{odd} − µ` on a finite
truncation plus a rigorous tail bound. Groskin's Arb `LDLᵀ` step is a working instance of the
even-sector half.

**The scale of the target**, from Fuchs' asymptotic (`ε(λ)` tracks `1 − χ₂`, `L = 2 log λ = log x`):

> `1 − χ₂ ≈ C x^{9/2} e^{−4πx}`, `C = 2^{14/3}/(√2 π⁵) ≈ 0.0587`

| `x = λ²` | `1 − χ₂` | decimal digits |
|---|---|---|
| 13 | `10⁻⁶⁷` | ~77 |
| 30 | `10⁻¹⁵⁸` | ~168 |
| 60 | `10⁻³²¹` | ~330 |
| 100 | `10⁻⁵³⁸` | ~547 |
| 300 | `10⁻¹⁶²⁷` | ~1 637 |
| 1000 | `10⁻⁵⁴⁴⁵` | ~5 455 |

Roughly `5.5x` decimal digits on a matrix of dimension `~4x`. Groskin's `dps = 500` at `c = 100` sits
right at that line, which is why he reports `~10⁻³³⁴` rather than the predicted `~10⁻⁵³⁸` and has to
extrapolate (his Aitken-`Δ²` gives `log₁₀|λ_∞^even| ≈ −536.8`, against Connes' §6.4 heuristic
`≈ −530.4` — agreement to 1%, which is a good independent check on both).

> ### Verdict
>
> **Certified SDP cannot prove §6.6(i) for all `λ`, and therefore cannot advance RH along this line.**
> It can do two finite things, and both are worth doing: (a) settle the **odd sector** at the cutoffs
> Groskin already reached, which nobody has; (b) turn Connes' Letter's *"proved modulo a condition of
> uniqueness of the minimum"* into an unconditional theorem at a specific `x`. At `x = 13` (b) needs
> ~77 digits and a matrix of dimension ~50 — trivial — and it would make the statement *"the 50
> numbers agreeing with the zeta zeros to between `2.6 × 10⁻⁵⁵` and `10⁻³` provably lie on the
> critical line"* unconditional. **Note that Suzuki's theorem does not do (b): `x = 13` means
> `a = log√13 ≈ 1.28`, which is not "sufficiently small".**

---

## 6. Corrections to the record

- **`NOTE_connes_weil_dirichlet_form` v1 §2 is withdrawn** as a novelty claim. The Beurling–Deny /
  Perron–Frobenius route to §6.6(i) is Suzuki, Theorem 1.4 and §§5.1–5.3.
- **v1's operator omitted the pole terms** `f̂(±i/2)` and so was `−Σ_v W_v`, not `Q_W`. The Metzler
  property holds for the former and fails for the latter (§2).
- **`ROUND11` §4 cites Connes eq. (16) for the `A_λ` construction; it is eq. (19)** in v1 of the
  survey. (16) is the Hermite operator.
- **`ROUND11` §4 recorded §6.6 as "two specific technical facts."** Item (i) is now *proved for small
  `a`* and *open for large `a`*; the record should say so, and should say that the small-`a` proof
  gives no leverage on the large-`a` case.
- **New to the record entirely: the Suzuki screw-function programme.**
  [2206.03682](https://arxiv.org/abs/2206.03682) (JLMS **108** (2023)) introduces the screw function
  of `ζ`; [2301.00421](https://arxiv.org/abs/2301.00421) (Canad. J. Math.) identifies the
  Weil-distribution Hilbert space with a de Branges space;
  [2606.09096](https://arxiv.org/abs/2606.09096) unifies *"Yoshida (1992), Bombieri (2001, 2003),
  Connes–Consani (2023), and Connes–Consani–Moscovici (2025+)"*. A **screw function** is defined by
  *"the kernel `g(t−u) − g(t) − g(−u) + g(0)` is nonnegative"* — i.e. `−g` is conditionally negative
  definite, the Lévy–Khinchine/Beurling–Deny object. **So the positivity structure the programme has
  been circling is, in the number-theory literature, Kreĭn's screw-function theory.** This should
  have been on the radar and was not.
- **Also new: Nakamura–Suzuki**, *On infinitely divisible distributions related to the Riemann
  hypothesis*, [2306.08317](https://arxiv.org/abs/2306.08317) (*Statist. Probab. Lett.* **201**
  (2023)) — an RH equivalence via infinite divisibility, with Lévy measure
  `ν_ζ = Σ_γ (m_γ/γ²)δ_{−γ}` supported on the **zeros**. That is a *consumer* by the Remmen test
  (built from the zeros), but it is the probabilistic dictionary and belongs in the ledger.

---

## 7. What to do next on this item

1. **Run the odd sector** (§4). Cheapest high-value experiment available. Groskin's code and data are
   public (`pip install connes-cvs`, Zenodo 10.5281/zenodo.19546514).
2. **Ask whether Suzuki's argument can be pushed off `a = 0`.** Everything is a perturbation off the
   `a → 0` limiting form `𝓛` with jumping kernel `|x−y|^{−1}`. The true kernel is
   `(1/a)/(2 sinh|a(x−y)|)`, which is still positive for every `a`, so the **irreducibility** step
   survives at any `a`. What fails at large `a` is the **Markov/unit-contraction** step, because the
   prime terms enter with the wrong sign and grow in number like `λ²`. **Isolating exactly which
   inequality breaks, and at which `a`, is a well-posed question and is the natural sequel to
   Suzuki's Theorem 1.4.** That is the item to work.
3. **Tell the two groups about each other.** Suzuki does not cite Connes–van Suijlekom or Connes'
   survey; Connes' survey does not cite Suzuki; Groskin cites neither Suzuki nor the screw-function
   line. Suzuki's Theorem 1.4 supplies, at one end, the hypothesis the others assume. A one-paragraph
   note pointing this out is worth writing and costs nothing.
4. **Retrieve Kotani's "Riemann's Zeta function and Kreĭn's string"** (unpublished, ResearchGate
   348522988, ~Jan 2021), cited by Suzuki [2206.03682] §9 — *"The corresponding string is the one
   named Zeta string by S. Kotani"*. Whether it is the same object as Burnol's Kreĭn string
   (`ROUND11` §3.7c) is an open identification and is item 4 of `ROUND11` §6.

---

## 8. Reproduction

| script | produces |
|---|---|
| `c1_weilform.py` | §1 the operator from Connes' §4.1 formulas; the off-diagonal sign test for `−Σ_v W_v`; the correction adding the pole terms; §4 the near-degenerate spectrum and the parity flip; §5 the precision table |

`numpy`, `sympy`.

**Sources.** Connes, [2602.04022](https://arxiv.org/abs/2602.04022) §§4.1, 5, 6.1–6.6, 7 — read in
full · Connes–van Suijlekom, *Comm. Math. Phys.* **406** (2025) 312,
[2511.23257](https://arxiv.org/abs/2511.23257) · Connes–Consani–Moscovici, *Zeta spectral triples*,
[2511.22755](https://arxiv.org/abs/2511.22755) · Connes–Consani, *Enseign. Math.* **69** (2023) 93 ·
**Suzuki, [2606.09096](https://arxiv.org/abs/2606.09096) Theorem 1.1, Theorem 1.4, §§4.5, 5.1–5.3** ·
Suzuki, [2206.03682](https://arxiv.org/abs/2206.03682) (JLMS **108** (2023)) ·
Suzuki, [2301.00421](https://arxiv.org/abs/2301.00421) (Canad. J. Math.) · Nakamura–Suzuki,
[2306.08317](https://arxiv.org/abs/2306.08317) · **Groskin,
[2605.20224](https://arxiv.org/abs/2605.20224) v4** · Kim–Hong–Kim–Choi–Jang–Kim,
[2607.24830](https://arxiv.org/abs/2607.24830) (first numerical realization of Suzuki's operator, P1
FEM, 30 digits, uncertified) · Fukushima–Oshima–Takeda, *Dirichlet Forms and Symmetric Markov
Processes*, Thm 3.2.1 · Lenz–Stollmann–Veselić, Thm 1.4 · Kato, *Perturbation Theory*, Ch. VIII §3 ·
Fuchs, *J. Math. Anal. Appl.* **9** (1964) 317 · Yoshida, *Adv. Stud. Pure Math.* **21** (1992) 281 ·
Bombieri, *Remarks on Weil's quadratic functional… I* (2001).
