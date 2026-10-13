# Round 12: the programme's four next items, executed — and one novelty claim refuted the same day

**2026-08-26.** Execution of all seven items in `ROUND11` §6. Four new notes published, two existing
notes corrected in place, one screen added. Three verification sweeps against primary sources; one of
them refuted a claim I had already published, which is recorded here in full.

**Headline.**

1. **Item 0 done.** `NOTE_n4_reformulation` rewritten: transcription confirmed against printed
   eq. (4.31), constant corrected from `2.114` to `8.07 × 10⁻⁶`, decay rate corrected to `−π/4`,
   equation references fixed to (4.20)/(4.31), and the Benjamin–Chang collision reframed from a
   referee hazard into an acknowledged shared mechanism the authors cross-cite.
2. **Item 1 done, with a new result.** The compact-free-boson `L`-function note is written. Beyond
   `ROUND11` §1: the on-line property of `Q_Z`'s zeros is **not** a two-term accident. Writing
   `Q(s) = 2Σ A_n cosh((s−½)log µ_n)`, the two-pair lattice case is exactly solvable and **all zeros
   lie on `Re s = ½` iff `A₂ ≥ A₁`** — the larger frequency must carry the larger effective weight.
   Sharp, provable, and verified numerically at the predicted threshold.
3. **Item 2 done.** Perlmutter's Riemann-vs-Maass sum rules written out explicitly. The `j`-dependence
   is pure number theory (`σ_{ρ}(j)j^{−ρ/2}` against Hecke `λ_n(j)` — the Kuznetsov split), all CFT
   data sits in two `j`-independent sequences, and there is a **second RH-detector** of the
   `Dorigoni–Treilis` shape hiding in it (envelope exponent `Re(ρ)/2`). But the constraint has no
   high-energy testing window, and the Selberg trace formula already supplies the qualitative claim.
4. **Item 3: my own claim refuted, and something better found.** I derived a Beurling–Deny /
   Perron–Frobenius proof of Connes' §6.6(i) and published it. **Suzuki
   [2606.09096](https://arxiv.org/abs/2606.09096) Theorem 1.4 already has it, by the same
   architecture** — found by the verification sweep four hours later. The note is withdrawn and
   replaced. What replaced it is stronger: **§6.6(i) is proved at small `a` and open at large `a`,
   which is the end that bears on RH**, and there is a cheap unrun experiment (§4.4).
5. **The Suzuki screw-function programme was entirely absent from this project's record.** Three
   papers, a JLMS and a Canad. J. Math. among them, unifying Yoshida, Bombieri, Connes–Consani and
   Connes–Consani–Moscovici. Plus two 2026 numerics papers on the same operator. **This is the
   largest single gap the record has had, and it sat in the middle of the item ranked highest.**

---

## 1. Item 0 — `NOTE_n4_reformulation`, rewritten

Published. Three substantive changes and one reframing.

- **Transcription discharged.** Printed eq. **(4.31)**, §4.2 matches the seminar-slide transcription
  character for character. The load-bearing caveat in v1 §2 is removed. Correct citations are
  **(4.20)** for the Mellin–Barnes contour representation and **(4.31)** for the residues; (3.36)–(3.37)
  are the kernel `U(a,b,r,s|t)`, the `τ₂ → ∞` side.
- **Numerics corrected.** `|β₁| = 4.010 × 10⁻⁶`, not `1.86`. `Σ_{n≤80}|β_n| = 4.0342 × 10⁻⁶` over
  positive ordinates, `8.0685 × 10⁻⁶` over all zeros — not `2.114`. Decay
  `log|β_n| = −0.795γ_n − 2.337`, which now matches the Stirling estimate `−π/4 = −0.7854`
  essentially exactly; v1's `−0.674` had a residual discrepancy I explained away with `1/ζ′(ρ)`.
  **There was no discrepancy; the fit was wrong.** The clean agreement is itself a check on the
  formula. The headline bound becomes `|oscillatory part| ≤ 8.07 × 10⁻⁶ · τ₂^{3/4}`.
- **§4 item 5 reframed.** Dorigoni–Treilis footnote 5 thanks Benjamin and Chang by name and cites
  their paper; §4.2 says *"(4.36) is directly analogous to the crossing equation (3.22) derived in
  [95]"*. So the `3/4` collision is a shared `SL(2,ℤ)` mechanism the authors identified in print, not
  a risk to be managed. Any write-up leads with it.
- **Footnote 7 recorded**: *"The contribution from these poles was inadvertently missed in [37]"* —
  an erratum to Dorigoni–Kleinschmidt–Treilis [2208.14087](https://arxiv.org/abs/2208.14087).
- **Their own numerics recorded**: Figures 2 and 3 test the residual against 10 and 50 zeros with
  `10⁻¹⁹` agreement. So the independent value added by §3.2 is the *uniform bound with its constant*,
  not the convergence check.

---

## 2. Item 1 — the free boson, and a sharp threshold beyond it

Published as `NOTE_freeboson_Lfunction`. `ROUND11` §1's content plus one new section.

**The question `ROUND11` left open** — does "zeros of `Q_Z` on the critical line" survive beyond a
two-term `S_core`? — is answered, and sharply.

For any reciprocal frequency set, `Q(s) = Σ_n a_n(µ_n^{−s} + µ_n^{−(1−s)})`. Put `x = s − ½`; since
`µ^{−s} + µ^{−(1−s)} = 2µ^{−1/2}cosh(x log µ)`,

> **`Q(s) = 2 Σ_n A_n cosh(x log µ_n)`, `A_n := a_n µ_n^{−1/2} > 0`,**

so all zeros lie on `Re s = ½` iff the cosine sum `Σ A_n cos(y log µ_n)` has only real zeros. In the
lattice case `µ_n = µ^{k_n}` this becomes a self-inversive polynomial in `w = µ^x`, with
`Re s = ½ ⟺ |w| = 1`. For `k = (1,2)`: `A₂(w⁴+1) + A₁w(w²+1) = 0`, and with `v = w + 1/w` this is
`A₂v² + A₁v − 2A₂ = 0` with `|w| = 1 ⟺ v` real, `|v| ≤ 2`. The smaller root satisfies `|v| ≤ 2` iff
`8A₁A₂ ≤ 8A₂²`:

> **All zeros on the critical line ⟺ `A₂ ≥ A₁`.** Sharp, with equality the exact boundary.

Confirmed at `µ = 0.4`: the predicted threshold `a₂* = √µ = 0.6324555` separates `a₂ = 0.6325`
(4 roots, none off-line) from `a₂ = 0.6324` (2 off-line), with the deviation growing continuously
(`|Re s − ½| = 0.0084, 0.21, 0.46, 0.96, 2.04` at `a₂ = 0.6324, 0.60, 0.50, 0.30, 0.10`). Dominance
is **sufficient but not necessary** in general: `k = (1,3)` stays on-line past its threshold, and
three pairs with `a_n ≡ 1` are entirely on-line although `A₃ < A₁ + A₂`.

**Why this is the interesting direction.** `A_n = a_n µ_n^{−1/2}` weights the *high* frequencies up,
and Cardy growth forces the high-energy density up. So the regime where these toy factors keep their
zeros on the line is the physically natural one, and the off-line examples are all built by
artificially suppressing the largest frequency. That converts Perlmutter §3.1(vi) — *which CFT data
controls the analytic factor's analytic structure* — from a slogan into a candidate answer: **the
effective coefficients `a_n µ_n^{−1/2}`, and whether they are non-decreasing in `µ_n`.** Appendix D's
argument already runs on the same tension (Cardy growth versus reciprocity) from the pole side.

Caveat stated in the note: these are truncated toy factors, not a CFT's actual `Q_Z`, which is an
infinite series with its own convergence structure.

---

## 3. Item 2 — Riemann vs. Maass

Published as `NOTE_riemann_maass_sum_rules`. Four things the paper does not do.

**(a) The sum rules, explicitly.** `a_j^{(s)} = 2σ_{2s−1}(j)/j^{s−1/2}` is a *finite* divisor sum,
hence entire, so the residue factorises: `Res[a_j^{(s)}Q_Z(s)] = 2σ_{ρ_m}(j)j^{−ρ_m/2} · r_m` with
`r_m = Res Q_Z` independent of `j`. Changing variable to `y = cosh^{−1}(λ/j)` cancels the Jacobian.
With Hecke normalisation `b_1^{(n)} = 1` (so `b_j^{(n)} = λ_n(j)`):

> `G_j(y) = 4 Re Σ_m r_m σ_{ρ_m}(j) j^{−ρ_m/2} cosh(ρ_m y/2) + Σ_n (Z,φ_n) λ_n(j) cos(u_n y)`
> must be a locally finite sum of deltas, for every `j ≥ 1`.

All CFT data is in the two `j`-independent sequences `{r_m}` and `{(Z,φ_n)}`; the `j`-dependence is
`σ_ρ(j)` against `λ_n(j)` — **the Eisenstein-vs-cusp split of the Kuznetsov formula**, which is the
right home for the object and is not named in the paper.

**(b) A second RH-detector.** `cos(u_n y)` is bounded; `cosh(ρ_m y/2)` has envelope
`e^{y·Re(ρ_m)/2}`, and `e^y ≈ 2λ/j`. So the zeta part of the spin-`j` density carries envelope
`λ^{Re(ρ_m)/2}` and the Maass part `λ^0`:

> **RH ⟺ the zeta contribution has envelope exactly `λ^{1/4}`.**

Structurally the same detector as `NOTE_n4_reformulation` §3.4, in a completely different physical
setting. Same screen, same answer on the last slot: nothing in the CFT forces the exponent.

**(c) A conditional no-go, and where the constraint can be tested.** Pairing against a bump
translated to height `Y` gives `e^{Y/4}P_j(Y) + Q_j(Y) = 0` with both `P_j` and `Q_j` Bohr
almost-periodic. If the support of `ρ_j^{(ζ)} + ρ_j^{(φ)}` had gaps along a relatively dense set of
heights, `P_j ≡ 0` would follow and every residue `r_m` would vanish — contradicting the paper's own
Appendix D. **So Appendix D and (11.19) together predict that this part of the density is
asymptotically gapless.** Cardy supplies that with room: the mean `y`-spacing is
`~1/(λρ_Cardy(λ))`, which at `c = 3` runs `2.4 × 10⁻⁵ → 3.2 × 10⁻²⁰ → 7.6 × 10⁻²³⁵` at
`y = 2, 5, 10`. **Consequence: (11.19) has no high-energy testing window; it is only usable near the
twist threshold.** That is the opposite of the paper's stated objective — *"to find and solve
constraints that act on high-energy states alone."*

**(d) Prior art, and it is closer than expected but does not subsume.** The Selberg trace formula for
`PSL(2,ℤ)` carries the scattering term `φ(s) = √πΓ(s−½)ζ(2s−1)/(Γ(s)ζ(2s)) = ξ(2s−1)/ξ(2s)`, whose
logarithmic derivative has poles at the non-trivial zeros — so `{u_n}` and `{ρ_n}` have been tied
together since 1956. Zworski: *"the zeros of the Riemann zeta function … are the resonances of the
Laplacian on the modular surface."* Two reasons it does not subsume Perlmutter's claim: **parity** —
he restricts to parity-even forms, and separating parities needs a reflection-twisted trace formula;
and **Fourier coefficients** — the trace formula never sees `b_j^{(n)}`, and the `j`-dependence is
the whole content of (11.19). **Any write-up must lead with the Selberg statement.**

**Correction to the record.** The first level-1 Maass form, `u = 9.53369526`, is **odd**; the
parity-even subset relevant here starts at `u = 13.77975135…`. The 1st, 2nd, 4th, 5th and 6th
level-1 forms are all odd, so the even subset is genuinely sparser.

**Honest re-ranking.** `ROUND11` called this "the first item where a physical requirement yields a
*new relation* on the zeros." Down: the relation is **not** pure arithmetic — `{r_m}` and
`{(Z,φ_n)}` enter linearly and can only be eliminated across a family of CFTs, which is the
landscape problem the rest of the paper is about. Up: it is a genuine *producer* — discreteness of a
spectrum is an input that does not mention `ζ`, and `ρ_j(λ)` passes the Remmen test outright.
**Unclaimed**: Perlmutter 2509.21672 has six citations and none pursues §11.2.

---

## 4. Item 3 — Connes §6.6(i): what I got wrong, and what is actually there

The full record, because the failure mode is the one this project keeps hitting.

### 4.1 What I did

Built `A_λ` explicitly from Connes' §4.1 formulas in the log variable, found its off-diagonal Schwartz
kernel to be everywhere non-positive (0 positive entries out of 159 600), rewrote the archimedean part
as a Beurling–Deny jump form with kernel `1/(2 sinh|t−s|)`, and concluded: positivity-improving
semigroup → Perron–Frobenius → simple positive ground state → even by reflection symmetry. That is
verbatim Connes' §6.6 item (i). Verified numerically: ground state strictly positive, even to
`10⁻¹⁵`. Published with the caveat *"Not checked: whether the Beurling–Deny reading is in the
literature. Verify before writing anything up."*

### 4.2 What the check found

**Suzuki, *Weil's quadratic form via the screw function*,
[2606.09096](https://arxiv.org/abs/2606.09096) (Jun 2026, rev. Aug 2026), Theorem 1.4**:

> *"For sufficiently small `a > 0`, the lowest eigenvalue `λ_a` is positive, simple, and satisfies
> `λ_a = log(1/a) + µ₁ − log(2π) + ψ(2) − 1 + O(a)` as `a → 0+`, for some constant `µ₁ > 0`.
> Furthermore, the corresponding eigenfunction is even."*

Proved in §§5.1–5.3 by exactly the architecture above: Markov property from *"the Beurling–Deny
representation (4.4) … [Fukushima–Oshima–Takeda, Theorem 3.2.1]"*; irreducibility because *"the
jumping kernel `|x−y|^{−1}` is positive on `(−1,1)²`"*; *"By [Lenz–Stollmann–Veselić, Theorem 1.4],
the irreducibility implies that the associated semigroup … is positivity improving"*; simplicity
because *"two functions that are positive almost everywhere cannot be orthogonal"*; and evenness
because *"since the eigenfunction corresponding to the lowest eigenvalue has a fixed sign, it must be
even."*

And Suzuki says his `A_a` **is** Connes' `A_λ`: *"(here we reformulate their results, originally
stated on `[1/λ, λ]`, in terms of the variable `a = log λ`)"*.

### 4.3 And a construction error of my own

My operator was `−Σ_v W_v`, not `Q_W`. The explicit formula is
`f̂(i/2) − Σ_ρ f̂(ρ) + f̂(−i/2) = Σ_v W_v(f)`, so `Q_W` carries the two pole terms
`|∫F e^{t/2}|² + |∫F e^{−t/2}|²` — **rank-one positive operators with strictly positive kernels**,
which lift the spectrum and **break the Metzler property**. My "constrain to `ĝ(±i/2)=0`" was
standing in for them (the two agree to five digits numerically), but the Metzler claim holds only for
`−Σ_v W_v`. Suzuki gets positivity-improving anyway, in the *derivative* realization
`B_a = D*G_a D` on `H¹₀(−a,a)` where the pole terms become the shift `log(1/a) − (2A+1)` — and the
rescaled limiting jumping kernel `|x−y|^{−1}` is exactly the `a → 0` limit of
`(1/a)/(2 sinh|a(x−y)|)`. **The kernel identification was right; the realization was wrong.**

### 4.4 What survives, and it is better

**Suzuki's theorem is at the wrong end.** Every step is a perturbation off `a = 0`, valid *"for
`0 < a < ½log 2`"*, and the positivity at that end comes from the `log(1/a)` shift, which diverges to
`+∞`. RH needs `a → ∞`, where `ε(λ) ≈ Cλ⁹e^{−4πλ²}` collapses.

> **§6.6(i) is proved where it is easy and open where it matters, and the small-`a` proof gives no
> leverage on the large-`a` case.** I have not found this stated anywhere.

**The two literatures have not met.** Suzuki cites Connes–Consani–Moscovici
[2511.22755](https://arxiv.org/abs/2511.22755) but **not** Connes–van Suijlekom
[2511.23257](https://arxiv.org/abs/2511.23257) and **not** Connes' survey — "Suijlekom" does not occur
in his paper. Connes' survey does not cite Suzuki. Groskin
([2605.20224](https://arxiv.org/abs/2605.20224)) cites neither.

**The one experiment nobody has run.** Groskin runs `dps = 500` Galerkin numerics on `QW_λ` out to
prime cutoff `c = 100`, recovering `γ₁,…,γ₁₀` to **307–329 matching digits**, with one rigorously
certified ingredient (*"a rigorous interval `LDLᵀ` factorization in Arb"*). But: *"Only the even
sector is diagonalized."* — *"The odd-sector zero, if any, is not probed here."* And §6.6(i) at large
`a` is exactly `µ_even < µ_odd`.

> **Compute the odd sector at the cutoffs Groskin already reached.** The blocks decouple identically;
> this is a re-run of public code (`pip install connes-cvs`) on the other block. `µ_even < µ_odd` with
> a clean margin → first evidence §6.6(i) survives to large `a`. Margin shrinking with `c` → a
> quantitative obstruction. `µ_odd < µ_even` at some `c` → **§6.6(i) is false there and the Letter's
> claim fails**, which would be the most valuable negative result available in this area.
>
> **Cheapest high-value experiment identified in twelve rounds.**

**My own numerics survive as the reason it matters.** With the pole terms restored, the two lowest
eigenvalues form a near-degenerate even/odd pair with gap `0.8–7.4%` of `|e₀|`, and at `x = 30` the
parity of the numerically-lowest flips between `N = 400` and `N = 800`. §6.6(i) at large `a` is one
near-degenerate pair and a parity assignment — nothing more general.

### 4.5 The lesson, recorded

`NOTE_existence_loophole` §10 records a standing policy: *"for every claim of the form 'X cannot
happen', run the control that would show X happening in a case where it does."* This failure is the
dual: **for every claim of the form "X is new", run the search that would show X is old — before
publishing, not after.** I published with the caveat attached rather than resolving it first, which
cost a same-day retraction. The caveat was correctly placed; the ordering was wrong.

---

## 5. Items 4 and 5 — the Kreĭn string, and the separability screen

**Item 5 done.** `NOTE_existence_loophole` now carries **§5.4, the separability obstruction**, and
`§8` carries it as **falsification criterion 5**: any construction proposing a *limiting*
Hilbert–Pólya space must say how it evades separability, since Burnol's `X^λ_{s,k}` become
asymptotically orthonormal while weakly converging to zero — *"The limit can not work inside
`L²((0,∞))` because this is a separable space!"* Test attached: ask a candidate to name the Hilbert
space its limiting objects live in.

**Item 4 scoped.** Burnol's Kreĭn string — attached to `|ζ(½+iτ)|²dτ/2π`, *"considered here for the
first time"*, 2002 — is **genuinely undeveloped**. `math/0112254` has **30 citations** and *none of
them picks up the string*: Suzuki's seven cite it for de Branges/Sonine spaces; Lagarias' *Hilbert
spaces of entire functions and Dirichlet L-functions* does not mention Kreĭn, string, `|ζ(½+it)|²`,
or Burnol at all.

**One exception, and it is an open identification.** Suzuki [2206.03682] §9: *"The corresponding
string is the one named **Zeta string** by S. Kotani [12]"* — S. Kotani, *Riemann's Zeta function and
Kreĭn's string*, **unpublished**, ResearchGate 348522988 (~Jan 2021). But Kotani/Suzuki's string is
the Kreĭn partner of `q_ξ(z) = Q_ξ(√z)/√z`, built from the **screw function**; Burnol's is attached
to the **measure on the critical line**. **Whether they are the same string is unverified, and no
source asserts the identification.** Retrieving Kotani's note is step one.

Worth flagging for the programme, because it makes items 3 and 4 the same object:
**Kotani–Watanabe, *Kreĭn's spectral theory of strings and generalized diffusion processes*** (LNM
923, 1982) — Kreĭn strings ↔ generalized diffusion processes. That is the standard Markov reading of
a string, it is Kotani's own, and nobody has applied it to the zeta string. The Weil form's
Dirichlet-form structure (§4) and the Kreĭn string (item 4) would then be two faces of one
generalized diffusion.

**Item 6 (function-field falsification test against round 9) and item 7 (do-not-pursue): unchanged,
not run this round.**

---

## 6. Corrections to the record

| where | correction |
|---|---|
| `NOTE_n4_reformulation` §3.2 | envelope constant `2.114` → `8.07 × 10⁻⁶`; decay `−0.674` → `−0.795 ≈ −π/4`; whole `β_n` table |
| `NOTE_n4_reformulation` §2, §5 | eq. refs (3.36)–(3.37) → **(4.20)** and **(4.31)**, §4.2 |
| `NOTE_n4_reformulation` §4 item 5 | referee hazard → acknowledged shared mechanism (fn 5, eq. 4.36) |
| `ROUND11` §4 | Connes' `A_λ` construction is eq. **(19)** in v1 of the survey, not (16); (16) is the Hermite operator |
| `ROUND11` §4 | §6.6 item (i) is *proved for small `a`* (Suzuki Thm 1.4) and *open for large `a`* |
| `ROUND10`/`ROUND11` bibliography | the **Suzuki screw-function programme** was entirely absent — [2206.03682], [2301.00421], [2606.09096], plus Nakamura–Suzuki [2306.08317], Groskin [2605.20224], Kim et al. [2607.24830] |
| `NOTE_connes_weil_dirichlet_form` v1 §2 | novelty claim **withdrawn**; operator omitted the pole terms `f̂(±i/2)` |
| `ROUND9` BBLS attribution | **checked, no fix needed** — it already reads "Báez-Duarte–Balazard–Landreau–Saias", and correctly credits the `m_ρ²` refinement to Burnol [math/0103058] |
| `NOTE_riemann_maass_sum_rules` §5 | first level-1 Maass form `u = 9.5337` is **odd**; first parity-even is `13.77975135…` |

**Ledger addition.** Nakamura–Suzuki [2306.08317] (*Statist. Probab. Lett.* **201** (2023)) give an RH
equivalence via infinite divisibility, with Lévy measure `ν_ζ = Σ_γ (m_γ/γ²)δ_{−γ}` supported on the
**zeros**. A *consumer* by the Remmen test — built from the zeros — but it is the probabilistic
dictionary and belongs on the shelf.

**Screen addition.** A **screw function** is defined by *"the kernel `g(t−u) − g(t) − g(−u) + g(0)`
is nonnegative"* — i.e. `−g` conditionally negative definite, the Lévy–Khinchine/Beurling–Deny
object. **The positivity structure this programme has been circling for four rounds is, in the
number-theory literature, Kreĭn's screw-function theory.** Any future positivity claim should be
checked against it first.

---

## 7. What to do next

0. **Run the odd sector** (§4.4). Public code, hours of compute, three informative outcomes and no
   uninformative one. **Do this first.**
1. **Push Suzuki's argument off `a = 0`.** The **irreducibility** step survives at any `a` — the true
   jumping kernel `(1/a)/(2 sinh|a(x−y)|)` is positive for every `a`. What must fail at large `a` is
   the **Markov / unit-contraction** step, because the prime terms enter with the wrong sign and grow
   in number like `λ²`. **Isolate exactly which inequality breaks and at which `a`.** Well-posed, and
   the natural sequel to Suzuki's Theorem 1.4.
2. **Tell the three groups about each other.** One paragraph, costs nothing, and Suzuki's Theorem 1.4
   supplies at one end precisely what Connes–van Suijlekom assume.
3. **Retrieve Kotani's note** and settle whether the "Zeta string" is Burnol's Kreĭn string.
4. **Write the `NOTE_n4_reformulation` paper**, and send it to Dorigoni. Every caveat is discharged;
   §5 step 1 of the old plan is done.
5. **Send the free-boson note to Perlmutter**, with §5 (the `A₂ ≥ A₁` threshold) as the substantive
   part rather than the `c = 1` remark.
6. **Item 6 from `ROUND11`** — the function-field falsification test against round 9's
   Nyman–Beurling route — still not run.
7. **Do not pursue:** the modular bootstrap as a route to Weil positivity; Perlmutter's sum rule as a
   location statement; further automated retrieval of long PDFs when the file can be supplied.

---

## 8. Reproduction

| script | produces |
|---|---|
| `n1_residues.py`, `n2_checks.py` | §1 — corrected `β_n` table, decay fit, envelope constant, non-degeneracy, converse exponents |
| `p1_freeboson.py` | §2 — the `c = 1` derivation, three consistency checks, the on-line zero family |
| `p2b_lattice.py` | §2 — the `cosh` reduction, the self-inversive polynomial, the sharp `A₂ ≥ A₁` threshold, the counterexamples to necessity |
| `m1_riemann_maass.py` | §3 — residue factorisation, envelope exponents, mean-spacing collapse, corrected Maass data |
| `c1_weilform.py` | §4 — the operator, the off-diagonal sign test, the pole-term correction, the near-degenerate spectrum and parity flip, the precision table |

`mpmath`, `numpy`, `sympy`.

**Notes published this round.** `claude/NOTE_n4_reformulation.md` (rewritten) ·
`claude/NOTE_freeboson_Lfunction.md` (new) · `claude/NOTE_riemann_maass_sum_rules.md` (new) ·
`claude/NOTE_connes_weil_dirichlet_form.md` (new, then corrected same day) ·
`claude/NOTE_existence_loophole.md` (§5.4 and criterion 5 added) ·
`claude/ROUND11_freeboson_and_positivity.md` (v2 published).

**Sources new to the record this round.** Suzuki [2606.09096](https://arxiv.org/abs/2606.09096),
[2206.03682](https://arxiv.org/abs/2206.03682) (JLMS **108** (2023)),
[2301.00421](https://arxiv.org/abs/2301.00421) (Canad. J. Math.) · Nakamura–Suzuki
[2306.08317](https://arxiv.org/abs/2306.08317) · Groskin
[2605.20224](https://arxiv.org/abs/2605.20224) · Kim–Hong–Kim–Choi–Jang–Kim
[2607.24830](https://arxiv.org/abs/2607.24830) · Connes–Consani–Moscovici
[2511.22755](https://arxiv.org/abs/2511.22755) · Kotani, *Riemann's Zeta function and Kreĭn's string*
(unpublished) · Kotani–Watanabe, LNM **923** (1982) · Lenz–Stollmann–Veselić · Fukushima–Oshima–Takeda
· Wong [1608.02296](https://arxiv.org/abs/1608.02296) · Zworski, *Mathematical study of scattering
resonances* · Blomer [1912.08137](https://arxiv.org/abs/1912.08137) (Kuznetsov) ·
Booker–Strömbergsson–Venkatesh, *IMRN* (2006) · LMFDB level-1 Maass forms · Then, *Math. Comp.* **74**
(2005) 363.
