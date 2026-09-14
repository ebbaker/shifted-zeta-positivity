<!--
Date: 27 August 2026 (third pass; §2 gap items closed same day).
Thread: psi_omega_margin (Paper 1) — post-fold-in next steps.
Status: live. Redacted for the public repository per notes/REDACTION_CHECKLIST.md
        (items 1, 4, 5 applied: draft correspondence removed, "the author" used,
        internal paths rewritten to repository paths). The full round-by-round
        research log is kept in the private project store; see STATUS.md.
-->

# Next steps for the psi_omega_margin paper (Ψ_ω)

**27 August 2026 (third pass; §2 gap items closed same day).** Executes the four next steps of
the round-13 recheck (§6 of that record). Everything below is verified (analytically, numerically,
or both) and was folded into `psi_omega_margin.tex` on 27 Aug 2026. Status at a glance:

| step | status | what it added to the paper |
|---|---|---|
| 1. Push the window with zero-free regions | **done, folded in** | strengthened window prop + new endpoint law `t₊ ≈ 0.72(½−ω)⁻²` |
| 2. Dirichlet / Selberg-class margin | **done, folded in** — prime side derived + verified; Selberg-class conventions aligned; zero locations justified | new section; Siegel-zero blindness proposition |
| 3. Phase transition at ω_c | **done, folded in — theorem with full proof** | new theorem + corollary (graded analogue of Suzuki Thm 1.6) |
| 4a. Bombieri §8 priority check | **done (machine read, two passes)** | priority claim for Thm 1.7 stands; human skim of §8 still advised |
| 4b. Letter to Suzuki | see note below | author action |

---

## 1. The window pushed through the zero-free regions

**Mechanism.** Beyond the verification height `T_v = 3·10¹²` every zero has
`β ≤ 1 − ν(τ)` with (MTY 2212.06867) `ν_cl(τ) = 1/(5.558691 log τ)` and
`ν_KV(τ) = 1/(55.241(log τ)^{2/3}(loglog τ)^{1/3})`; `ν := max(ν_cl, ν_KV)` is admissible. So the
high-zero part of the remainder improves from `S·e^{(½−ω)t}` to

> `|R_high(t)| ≤ e^{(½−ω)t} E(t)`,
> `E(t) = (1/π) ∫_{L_v}^∞ (L − log 2π) exp(−L − ν̃(L)t) dL`, `L = log u`, `L_v = log T_v = 28.73`,

with `E(0) = S = 2.96·10⁻¹²` recovering the earlier bound. The two regions cross at `L_x = 8928`
(`u = 10³⁸⁷⁷`): ν_cl governs the entire practically relevant range; ν_KV takes over only when
`½−ω ≲ 2·10⁻⁵`.

**Damping measured:** `E(t)/S` = 0.74 (t=50), 0.55 (t=100), 0.16 (t=300), 2.4·10⁻³ (t=1000),
1.7·10⁻⁸ (t=3000), 7.4·10⁻²⁴ (t=10⁴).

**New windows** (upper endpoint `t₊` of unconditional positivity; `t₋` unchanged, < 0.0017ω):

| ω | t₊ old (S only) | t₊ new (damped) | x = e^{t₊} |
|---|---|---|---|
| 0.05 | 55.06 | 55.84 | 10^24.3 |
| 0.10 | 63.67 | 64.68 | 10^28.1 |
| 0.20 | 87.98 | 89.86 | 10^39.0 |
| 0.25 | 107.19 | 109.94 | 10^47.8 |
| 0.30 | 136.02 | 140.42 | 10^61.0 |
| 0.40 | 282.06 | 300.89 | 10^130.7 |
| 0.45 | 580.82 | 663.59 | 10^288.2 |
| 0.49 | 3079.1 | **7262.3** | 10^3154 |
| 0.494 | — | 20 178 | 10^8763 |
| 0.497 | — | 80 694 | 10^35050 |
| 0.499 | — | 726 493 | 10^315500 |

**Endpoint law (clean).** For ½−ω below ~0.01 the binding zeros sit at
`L* = √(t/c)`, `c = 5.558691`, and the window endpoint obeys

> `t₊(ω) ≈ (4/c)(½−ω)⁻² = 0.7196(½−ω)⁻²`

— verified: prediction 7.2·10⁵ / 8.0·10⁴ / 2.0·10⁴ at ω = 0.499 / 0.497 / 0.494 against computed
726 493 / 80 694 / 20 178. Ultimately (½−ω < 2·10⁻⁵) KV takes over and
`t₊ ≍ (½−ω)^{−5/2−o(1)}`. As ω → ½⁻ the window diverges, interpolating continuously to the
unconditional (PNT) endpoint ω = ½ where Ψ_ω ≥ 0 outright — the window quantifies *how* the
family becomes unconditional at its trivial end.

**Structure stated in the paper:** the two inputs enter separably — the verification
height controls the *level* `S` (hence `t₊ ≈ (½−ω)⁻¹ log(1/S)` for moderate ω), the zero-free
region controls the *decay* of `E(t)` (hence the endpoint law near ω = ½). Gains at moderate ω
are 1–7%; the entire action of zero-free technology is at the PNT end. This sharpens the
recheck's verdict on the zero-density section: density/zero-free inputs control the onset, and now
we know by exactly how much.

**Folded in as:** the window proposition's bound was replaced by the `E(t)` version (the `S` form
kept as the simple corollary), with the new table rows and the endpoint law and its two-regime
remark.

---

## 2. The margin for Dirichlet L-functions (and the Selberg-class scope)

**Setting.** χ real primitive mod q, `a = (1−χ(−1))/2`,
`ξ(s,χ) = (q/π)^{(s+a)/2} Γ((s+a)/2) L(s,χ)`; for real primitive χ the root number is +1, so
`ξ(s,χ) = ξ(1−s,χ)` and the zero set has the full ±/conjugation symmetry — every step of the ζ
analysis transfers verbatim. Define Ψ_{ω,χ} by Suzuki's zero-side series over the zeros of
ξ(·,χ). Then, **unconditionally** (lowest zeros of the tested χ are far above ½, so convergence
and positivity arguments carry over):

> `Ψ_{ω,χ}(t) = (ξ′/ξ)(½+ω,χ)·t + (ξ′/ξ)′(½+ω,χ) + R`, `|R| ≤ A*_χ(ω)e^{−(ω−ϑ_χ)t}`,

with the same proofs. Everything checked numerically for q = 3, 4, 5 (`code/c7_dirichlet.py`):
functional equation and reality of ξ(½+it,χ) to 20 digits; zero counts to T = 60 match the
Riemann–von Mangoldt prediction (44/44.98, 50/50.47, 54/54.73 — no missed zeros); closed forms
`A_χ = ω⁻¹(ξ′/ξ)(½+ω,χ)`, `B_χ = (ξ′/ξ)′(½+ω,χ)` match direct zero sums with the
tail-limited discrepancy constant across ω (−3·10⁻³, −1.3·10⁻³, −8·10⁻⁴), the same signature
as the ζ check.

**The marginality mechanism is universal, and the margin grows with the conductor.**
`(ξ′/ξ)(½,χ) = 0` numerically (≤ 10⁻²¹) for all three characters — forced by ε = +1, exactly as
for ζ. Margin scale `B_χ(0) = (ξ′/ξ)′(½,χ) = Σ_γ γ⁻²`:

| L-function | B(0) | slope at ω = 0.25 |
|---|---|---|
| ζ | 0.046210 | 0.011552 |
| χ mod 3 | 0.113402 | 0.028340 |
| χ mod 4 | 0.156030 | 0.038978 |
| χ mod 5 | 0.156914 | 0.039206 |

Higher conductor ⟹ lower first zero ⟹ larger margin: among GRH-graded criteria of this family,
**ζ is the most marginal member**. If ξ_F has a central zero of order m (possible for ε = −1 or
higher rank; impossible for real primitive Dirichlet), the central term contributes
`m[t/ω − (1−e^{−ωt})/ω²] ≥ 0` and the slope acquires a pole `~ m/ω`: those families are
non-marginal at every ω > 0.

**Siegel-zero blindness (verified).** A hypothetical real zero pair
`β₀ = ½+δ, 1−β₀` gives γ = ±iδ, and its series contribution is **positive** and exponentially
growing:

> pair term `= (δ+ω)² e^{(δ−ω)t}/(δ²−ω²)² · (1+o(1)) > 0`

(numerics: at δ = 0.4, ω = 0.1, t = 40: computed 1.80832·10⁶ vs predicted 1.808·10⁶). The phase
locks at α = π, where a complex quartet oscillates. Consequently the shifted criterion for
Dirichlet L-functions reads (in the sharpened form proved as Proposition 9.3 of the paper):
**Ψ_{ω,χ} eventually ≥ 0 ⟺ every non-real zero has Re ρ ≤ max(½+ω, β₀)**, β₀ the
largest real zero — real zeros can even shield larger non-real ones, since their positive
exponential dominates the oscillation (the amplitude comparison uses τ² ≫ (δ−ω)²). The
criterion cannot see Siegel zeros. Mechanism on the Landau side: the transform's singularity at
the real point of its convergence abscissa is exactly what a real zero supplies *without*
violating non-negativity. (Consistent with the sensitivity proposition requiring τ₀ > 0.)

### 2a. The arithmetic (prime-side) formula — derived and verified

For real primitive χ mod q with parity `a = (1−χ(−1))/2` and `α := (½+ω+a)/2`:

> `Ψ_{ω,χ}(t) = (t/2)[ψ(α) + log(q/π)] + ¼[ψ′(α) − e^{−2αt}Φ(e^{−2t},2,α)]
>              − Σ_{n≤e^t} Λ(n)χ(n) n^{−½−ω}(t − log n)`.

There is no pole block: ξ(s,χ) is entire, so the ζ-formula's `4[…]` term has no analogue.
The derivation mirrors Suzuki §2 through the Laplace identity
`∫₀^∞ Ψ_{ω,χ}e^{izt}dt = −z⁻²(ξ′/ξ)(½+ω−iz, χ)`; the one nontrivial block is the lemma

> `∫₀^∞ ¼[ψ′(α) − e^{−2αt}Φ(e^{−2t},2,α)]e^{izt}dt = −(1/2z²)[ψ(α−iz/2) − ψ(α)]`, Im z > 0,

proved per-k by partial fractions (the per-k identity reduces to `(i/z)·(iz/2) = −½`; algebra
checked by hand) and confirmed numerically to 10⁻²² at two test points. Equality with the
zero-side series follows by uniqueness of Fourier transforms, using `(ξ′/ξ)(½,χ) = 0` (verified
≤ 10⁻²¹), so the Hadamard expansion has no constant term, exactly as for ζ. `Ψ_{ω,χ}(0) = 0`
since `Φ(1,2,α) = ζ(2,α) = ψ′(α)` (numerically: 1.4·10⁻¹¹ at t = 10⁻¹²).

End-to-end check **using no zeros** (Λχ sieved to e¹⁵), against the margin main term
`(ξ′/ξ)(½+ω,χ)t + (ξ′/ξ)′(½+ω,χ)`:

| q | ω | t | Ψ_{ω,χ} (primes) | main term | diff | envelope A_χ e^{−ωt} |
|---|---|---|---|---|---|---|
| 3 | 0.2 | 15 | 0.453394387 | 0.453442922 | −4.9·10⁻⁵ | 5.6·10⁻³ |
| 3 | 0.3 | 15 | 0.623230515 | 0.623246169 | −1.6·10⁻⁵ | 1.3·10⁻³ |
| 3 | 0.4 | 15 | 0.792818095 | 0.792822628 | −4.5·10⁻⁶ | 2.8·10⁻⁴ |
| 4 | 0.2 | 15 | 0.625643432 | 0.623673320 | +2.0·10⁻³ | 7.8·10⁻³ |
| 4 | 0.3 | 15 | 0.857335265 | 0.856912535 | +4.2·10⁻⁴ | 1.7·10⁻³ |
| 4 | 0.4 | 15 | 1.089635320 | 1.089544900 | +9.0·10⁻⁵ | 3.9·10⁻⁴ |
| 5 | 0.2 | 15 | 0.626961767 | 0.627312662 | −3.5·10⁻⁴ | 7.8·10⁻³ |
| 5 | 0.3 | 15 | 0.861994613 | 0.862061187 | −6.7·10⁻⁵ | 1.7·10⁻³ |
| 5 | 0.4 | 15 | 1.096327440 | 1.096339640 | −1.2·10⁻⁵ | 3.9·10⁻⁴ |

Every row sits inside the envelope and decays in both ω and t at the predicted rate. The
differences are ~10× the ζ case — as they must be: A_χ is ≈3× larger and the lowest zeros are
lower (6.02 for q = 4 vs 14.13), so the leading damped oscillation is bigger.

### 2b. Selberg-class alignment (Suzuki arXiv:2209.12832)

The setting there: the **extended** class `S♯` (axioms S1–S3; functional equation
`ξ_F(s) = ω·conj ξ_F(1−s̄)` with root number ω, |ω| = 1; no Euler product needed), completed
function `ξ_F(s) = s^{m_F}(s−1)^{m_F}Q^s Π Γ(λ_j s+μ_j) F(s)`, screw function

> `g_F(t) = −iB_F t − (m₀/2)t² + Σ_{γ≠0} m_γ (e^{−iγt}−1)/γ²`, `iB_F = (ξ_F′/ξ_F)(½)`,

m₀ the central zero order, zeros indexed by `F(½−iz)` exactly as here. Its Theorem 1.1:
**GRH_F ⟺ Re(−g_F(t)) ≥ 0 for all t ≥ some t₀ — under the hypothesis that F has no real zeros
off s = ½**; the arithmetic side (its Thm 4.1) needs the semi-extended class `S♯♭` (F′/F a
Dirichlet series — the §2a formula is its χ-instance). No shifted family appears there (its
ω is the root number, not a shift). Three consequences, folded in as the paper's Selberg-class
remark:

1. **The Siegel-blindness observation is the quantitative face of the real-zero hypothesis.**
   That paper assumes real zeros away; here we compute exactly what one does (positive
   contribution, rate δ−ω, amplitude `(δ+ω)²/(δ²−ω²)²`), i.e. *why* the hypothesis cannot be
   dropped.
2. **Even the unshifted general criterion is only "eventually"** in `S♯` (unlike ζ's pointwise
   Thm 1.7) — so an explicit threshold t₀ is more valuable in the general class than for ζ.
3. **The marginality mechanism is universal in `S♯`**: the functional equation forces
   `(ξ_F′/ξ_F)(½)` purely imaginary (`s ↦ ½` in the FE gives `(ξ′/ξ)(½) = −conj (ξ′/ξ)(½)`),
   so the margin slope `Re(ξ_F′/ξ_F)(½+ω)` vanishes at ω = 0 for *every* F — self-dual or not.
   Non-self-dual F is handled through `Re[·]`, equivalently the pair (F, F̄), which restores the
   ±γ symmetry the ζ proofs use; a central zero of order m₀ adds the positive term
   `m₀[t/ω − (1−e^{−ωt})/ω²]`, making those families non-marginal at every ω > 0.

### 2c. Zero locations for the tested characters — closed

(a) **No real zeros:** `L(σ,χ) > 0` on a 200-point grid of (0,1) for q = 3, 4, 5 (minima
0.335, 0.502, 0.0024; the q = 5 dip approaching σ = 0 is the trivial zero at s = 0 of an even
character, outside the open interval). (b) **No missed complex zeros:** a finer rescan (step
0.02) of q = 3 confirms 44 zeros to T = 60 against the Riemann–von Mangoldt 44.98 — the
"deficit" is the next zero sitting at 60.027, just past the cutoff. (c) **Literature:** GRH is
verified for all primitive characters of modulus q ≤ 400 000 to height max(10⁸/q, ·) — for
q ≤ 5 beyond 2·10⁷ — by Platt (arXiv:1305.3087; Math. Comp. 85 (2016), 3009–3027), covering
everything this section needs many times over. This also discharges, for these characters, the
real-zero hypothesis in the Selberg-class Theorem 1.1.

---

## 3. The phase transition at ω_c — theorem and proof

Write `ω_c = Θ − ½ = ϑ` (Suzuki Thm 11.1). The normalised slope is an order parameter with a
first-order transition at ω_c, and RH is exactly the statement that the transition is
continuous.

> **Theorem (order parameter).** For 0 < ω < ½:
> (i) If ω ≥ ω_c then Ψ_ω(t)/t → (ξ′/ξ)(½+ω) as t → ∞; in fact
> Ψ_ω(t) = (ξ′/ξ)(½+ω)t + O(1), the O(1) being |B(ω)| + A*(ω).
> (ii) If ω < ω_c then for every ε < ω_c − ω,
> `limsup e^{−εt}Ψ_ω(t) = +∞` and `liminf e^{−εt}Ψ_ω(t) = −∞`.
>
> Hence m(ω) := liminf Ψ_ω(t)/t equals −∞ on (0, ω_c) and (ξ′/ξ)(½+ω) ≥ 0.0462ω on
> [ω_c, ½). If ω_c > 0, m jumps by at least 0.0462·ω_c at ω_c; under RH (ω_c = 0),
> m(ω) = (ξ′/ξ)(½+ω) → 0 continuously. **RH ⟺ the transition is continuous.**

> **Corollary (graded Suzuki Thm 1.6).** `Θ ≤ ½+ω ⟺ Ψ_ω(t) = (ξ′/ξ)(½+ω)·t + O(1)`.

*Proof.* (i) is the asymptotic theorem of the paper (remainder ≤ A*(ω)e^{−(ω−ϑ)t} ≤ A*(ω)).

(ii) Both parts by the Landau mechanism. Suppose, for contradiction, that
`Ψ_ω(t) ≥ −Ce^{εt} − D` for all t ≥ 0 (the liminf case; the limsup case uses
`Ψ_ω ≤ Ce^{εt}+D` and the same lines with signs flipped). Set
`f(t) := Ψ_ω(t) + Ce^{εt} + D ≥ 0`. From the series, `|Ψ_ω(t)| ≤ ωA t + |B| + A*e^{(ϑ−ω)t}`
(the remainder bound `|R| ≤ A*e^{(ϑ−ω)t}` holds with no ordering assumption between ϑ and ω, and
A* converges unconditionally), so the Laplace transform `F(z) = ∫₀^∞ f(t)e^{izt} dt` converges
for `Im z > ϑ−ω` and equals there

`F(z) = −z⁻²(ξ′/ξ)(½+ω−iz) + iC/(z−iε) + iD/z`

(term-by-term transforms; absolute convergence as in Suzuki §2). Let σ_c ≤ ϑ−ω be the abscissa
of convergence. Since f ≥ 0, Landau's theorem (Widder II.5b) makes iσ_c a singularity of F. The
singularities of the closed form on the ray `{iy : y > ε}` would be poles of
(ξ′/ξ)(½+ω−iz) at z = i(β−½−ω) with β a **real** zero of ξ in (½, 1] — and there are none.
So σ_c ≤ ε, F is analytic in Im z > ε, hence (ξ′/ξ)(½+ω−iz) has no poles there: every zero
satisfies Re ρ ≤ ½+ω+ε. But ω+ε < ω_c means some zero has Re ρ > ½+ω+ε — contradiction. So no
such C, D exist, i.e. `liminf e^{−εt}Ψ_ω(t) = −∞`. ∎

Remarks: (a) this is the sharp form of "the criterion is not saturated at ω > 0":
below ω_c, Ψ_ω oscillates in *both* directions at exponential rate arbitrarily close to
ω_c−ω; at and above ω_c it is linear + O(1). (b) The corollary upgrades Suzuki's Thm 1.6
(RH ⟺ Ψ = O(1)) to the graded family with the sharp linear term, and gives yet another
equivalent: `ω_c = inf{ω : Ψ_ω(t) − (ξ′/ξ)(½+ω)t is bounded}`. (c) For ζ the proof uses only
"no real zeros in (½,1]"; for Dirichlet L the same proof shows the ε-window statement modulo
real zeros — matching §2's Siegel-blindness exactly. Proof checked against the numerics: at
(ω,t) = (0.2, 15): Ψ_ω/t = 0.01233 vs slope + B/t = 0.01232.

**Folded in as:** a new section between the threshold and window sections; the corollary absorbed
the earlier standalone remark.

---

## 4a. Bombieri, Rend. Lincei 11 (2000), §8 — priority check

An earlier round flagged this as "the one place a priority claim for Suzuki's Thm 1.7 could
break"; the PDF had resisted retrieval. **Retrieved** via the Biblioteca Digitale Italiana di
Matematica (bdim.eu, item RLIN_2000_9_11_3_183_0) and machine-read twice with targeted prompts.

Findings, consistent across both passes: §8 does use characteristic functions Φ of `[−t,t]` —
but as generators of a **finite-dimensional vector space** `V` (spanned by `Φe^{x/2}, Φe^{−x/2},
Φe^{−iγx}`) on which eigenvalues of finite approximations to the Weil form are studied
(Lemma 8: (L[F],F) real on V; Theorem 8 concerns a finite multiset with zeta-like symmetries).
The paper's RH equivalences (Theorems 1 and 2) quantify over **all** of `C₀^∞((0,∞))`; no
statement of the form "RH ⟺ positivity of W on a one-parameter family," and no statement about
`t ↦ W(Φ_t * Φ̃_t)` as a function of t, appears.

**Conclusion:** Suzuki's Thm 1.7 priority claim (RH ⟺ Weil positivity on the rectangle family
alone, i.e. Ψ ≥ 0 pointwise) stands against Bombieri 2000. Caveat for the record: this is a
machine read of a scanned PDF (two passes, consistent); a final human skim of §8 before
submission is still recommended, and the paper's introduction needs no change either way.

## 4b. Letter to Suzuki

A draft letter to M. Suzuki — asking whether the shifted family Ψ_ω or Theorem 11.1 was pursued
further, whether there was a reason the shifted family does not reappear in the later
Selberg-class work, and inviting corrections on attribution — was prepared on 27 August 2026. It
is kept in the private project store and is not reproduced here (per the redaction checklist,
item 1). Sending it is an author action still outstanding.

---

## 5. Remaining before a submission-ready draft

1. Author block, ORCID, affiliation; acknowledgements wording.
2. Human skim of Bombieri §8 to retire the machine-read caveat in §4a.
3. Send (or decide against) the Suzuki letter of §4b.
4. Independent human check of the two genuinely new arguments — the phase-transition proof (§3)
   and the Dirichlet Siegel-blindness proposition (§2) — before release.
5. Repository release-checklist items for this folder (see `papers/README.md`): blueprint +
   statements-ledger entries, `VERIFICATION_STATUS.md`, `CITATION.cff` and `.zenodo.json`,
   cross-citation renumbering against the released companions.

## 6. Reproduction

| script | produces |
|---|---|
| `code/c6_window_kv.py` | §1: E(t), damping table, new windows, endpoint-law verification |
| `code/c7_dirichlet.py` | §2: ξ(s,χ) checks, zero lists (q=3,4,5), closed-form vs zero-sum tables, conductor trend, Siegel-pair positivity |
| `code/c8_prime_side_chi.py` | §2a: transform lemma check (10⁻²²), prime-side Ψ_{ω,χ} vs main term, Ψ(0)=0 |
| (inline) | §2c: L(σ,χ) grid positivity; q=3 fine rescan locating the zero at 60.027 |
| (analytic) | §3 proof; transforms re-checked symbolically: ∫te^{izt} = −z⁻², ∫e^{(ε+iz)t} = i/(z−iε) |

`mpmath`, `numpy`. Sources this round: MTY arXiv:2212.06867 (both explicit regions);
Platt–Trudgian BLMS 53 (2021); Platt arXiv:1305.3087 = Math. Comp. 85 (2016) 3009–3027 (GRH
verification, q ≤ 400000); Suzuki arXiv:2209.12832 (S♯ conventions, g_F, Thms 1.1 and 4.1);
bdim.eu RLIN_2000_9_11_3_183_0 (Bombieri 2000, §§1–2, 8, 12); Widder, The Laplace Transform,
II.5b; Suzuki JLMS 108 (2023) §§2, 7, 11.
