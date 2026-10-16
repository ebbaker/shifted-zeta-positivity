# Verification status

**Paper:** *Archimedean first-slab positivity for shifted zeta canonical systems* — preprint v1.0, 5 September 2026
**Last updated:** 5 September 2026

This file mirrors Section 13 of the paper and is the place where the status
will be kept current between preprint versions. The manuscript is a
computer-assisted result prepared with substantial language-model assistance.
It has been through two adversarial referee-style review rounds and one
clean-room reimplementation of the certificate. No unresolved error in the
main proof chain was identified in those internal reviews; the independent
human checks listed below remain pending. What it has **not** had is a human reader who has derived
the central steps on paper and will stand behind them.

Legend: ✅ independently reproduced · 🔶 reproduced by automated means only, human confirmation pending · ⬜ not yet checked

## 1. Changes made when the working draft became this preprint (5 Sept 2026)

These were the "fix before archiving" items of the internal checklist.

| # | Item | Resolution in v1.0 |
|---|---|---|
| 0.3 | State that the certified margin is a valid lower bound for the form on all of `D_log`. | Done, with a correction: the certified Weyl–Schur margin *m* is the head's clearance over `κ²/d_tail`, but the exact block-Schur condition for `Q ⪰ c·I` is `(λ_head − c)(d_tail − c) ≥ κ²`. Solving gives `c = m − κ²m/(d(d−m))`, i.e. `c_even = 6.11594…·10⁻⁴` (not `6.11635·10⁻⁴`) and `c_odd = 5.26131…·10⁻²`. Theorem B now states `c_* = 6.1159·10⁻⁴`; Lemma 7.1 and Remark 7.2 give the argument. The correction is ~4·10⁻⁸ and changes nothing else. |
| 0.4 | Pin "equivalent" in §1.1 to the exact statement in Suzuki [1]. | Done. §1.1 and the abstract now quote [1, Prop. 1.2] (for `ω₀ > 0`: `ζ(s) ≠ 0` for `Re s > 1/2+ω₀` ⟺ `Θ_ω` meromorphic inner for **every** `ω > ω₀`), [1, Thm. 2.2] (innerness ⟺ Hankel mapping property) and [1, Lemma 4.1] (innerness ⟹ isometry). The former single-shift "equivalence" is gone. |
| 0.6 | Insert the missing line in the §6.3 case split (`a ≤ t₀` cannot occur since `a ≥ L/2 = 0.3466 > t₀ = 0.2812`). | Done (Lemma 6.1). |
| — | §9.3 said the strict known-range extension `ω > 1/2` rested on an unreproduced Paley–Wiener argument. | Corrected: Suzuki [1, Lemma 4.4] (hypothesis "`ω > 1/2` and `a > 1`") already proves `‖H_{ω,a}‖ < 1` for every finite section, via his support Lemma 4.3 and compactness. §9.3 now cites it and positions Theorem A as the complementary `0 < ω ≤ 1/2` result. 🔶 (statement and hypothesis taken from automated reading of [1]; confirm against the PDF). |
| 0.1, 0.2, 0.5 | Stale sentences in the Investigation 12/14 write-ups. | Not applicable to this deposit (preprint only). **Must be fixed before any code/write-up release:** Inv 12 §4 old derivation of Prop 4.1; Inv 12 §8.4 "not yet independently implemented"; Inv 14 §9 ledger overstating the kernel-norm audit. |

## 2. Independently reproduced from the printed definitions ✅

By two recomputations independent of both the primary Arb code and the
clean-room audit (one during the referee rounds, one while preparing v1.0):

- All algebraic identities in §§2.2, 3.1, 3.3, 4.1, 6.1, 6.2, 10.2, 10.4.
- Laplace transform of the explicit impulse (3.6) against `K_ω` (3.3): `1.5e−17` at `ω = 1/2`, `~1e−10` at `ω = 0.3` (quadrature-limited at the `t^{ω−1}` singularity).
- Proposition 4.2 (bounded shift difference) as a statement, to 30 digits at `ω = 0.1, 0.3, 1/2`; and every step of its proof: digamma integral representation, cancellation of the divergent `e^{−2t}` summands, rational kernel `4cosh(t/2)(cosh ωt − 1)`, bridge identity for `R(t)`, full multiplier identity.
- Lemma 4.1 (endpoint): delta mass `→ −π`; corrected formula agrees with `Q₀ + C_{1/2}` for `f = 1` to `7.5e−8` (quadrature floor); uncorrected formula off by `0.2402`.
- §6.3 chain: `t₀ = log ρ`, closed form of `h`, `sign(dh/dt) = sign N(q)`, `N′` grouping, `N(1) = −2`, `N(√ρ) = 3ρ²−1`, `t_m`, `h(t_m)`, `h(log2−t₀)`, `∫₀^{log2}|h| = 0.012293050401142319559…`, `L/2 > t₀`, and the monotonicity of the absolute row integral in `b`.
- `β* = 1.5299869819194765…`, `d_tail = 1.5176929819194764…`, both Schur losses to 17 digits.
- Taylor remainder `1.532967865231399e−12`.
- Head minima and margins of §7.2 by an independent 16-mode Legendre reconstruction (consistent to the interval-widening penalty `2.26e−5` even, `8.65e−6` odd).
- The block-Schur coercivity constants of Remark 7.2.
- Investigation 14 sample `T₁` entries to 13 digits; all row counts (724, 783, 1360).
- All reference metadata, including that [5] is X. Zhu on v2.

## 3. Checked against Suzuki's statements 🔶

Against automated readings of arXiv:1204.1827 (two independent extractions agreed on every item below):

- Suzuki's `γ(s) = ½ s(s−1) π^{−s/2} Γ(s/2)` is our `Γ_∞(s)`.
- His Mellin formula `∫₀^∞ g_ω(x) x^s dx/x = γ(s−ω)/γ(s+ω)` (Sect. 3.1) is our transfer `K_ω(p)` at `s = p + 1/2`.
- Our layer formula (2.5) is his eq. (2.3) in logarithmic coordinates; his Prop. 2.1 is consistent with (2.1), (2.3), the Sect. 3.1 formula and the Dirichlet series `Σ c_ω(n) n^{−w} = ζ(w−ω)/ζ(w+ω)`, with matching domains.
- `H_{ω,a} = P_a H_ω P_a` (his (2.5)–(2.6)) corresponds to our centered interval of length `L = 2 log a`; the first prime layer enters exactly when `L > log 2`.

**This is the single most important outstanding human check (item C1 below).** A factor or shift here would move the `log 2` threshold. A step-by-step protocol for doing C1 and C2 by hand, designed so the checker is not anchored by the preprint, is `../../../verification/first-slab/PROTOCOL_C1_C2.md` (6 Sept 2026).

## 4. Not yet human-verified ⬜

### Part A — self-checkable, elementary (half a day each)
- **A1** Proposition 4.2 on paper, including the endpoint extension `ω ↑ 1/2`.
- **A2** Lemma 4.1 (endpoint) bookkeeping.
- **A3** Lemma 6.1 (row maximum), including the inserted line `a ≥ L/2 > t₀`.
- **A4** The Volterra identities (2.10) by change of variables.

### Part B — functional analysis of §8 (several days)
- **B1** `s ↦ V_{s,L}` is `C¹` in operator norm: the multiplier bounds in §8.1 are stated with `O(·)` and no constants. Weakest-supported claim in the paper.
- **B2** Weighted-to-unweighted transfer and that all adjoints from §8.4 on are unweighted.
- **B3** `V_s L² ⊂ D_log` and the closure step (8.7).
- **B4** The improper strong-operator integral of §8.5.
- **B5** Strictness (§8.6) with the corrected `c_*`.

Failure of B1–B4 would leave Theorem C unproved and Theorem A resting on the routes of §11; it would not make Theorem A false.

### Part C — analytic number theory
- **C1** Human confirmation of the normalization chain against Suzuki's paper (Section 3 above), ideally with Suzuki himself.
- **C2** Originality search for (a) the off-center kernel identity of Prop. 4.2 and (b) the shift-radial energy identity, against [4], [5], [12], [13] and newer work.
- **C3** The rewritten §1.1 equivalence statement and the §9.3 citation of [1, Lemma 4.4].

### Part D — repository (needs the code)
- **D1** The inherited Investigation 7 central certificate: Binet bound `w₀(τ) ≥ β*` for `|τ| ≥ 30` and the spherical-Bessel Legendre-tail majorants (couplings `1.4084884e−9` / `2.2191643e−10`, deviations `9.78e−24` / `2.43e−25`). Both implementations take these as given.
- **D2** The interval `LDLᵀ` and box-construction code (no reviewer has read it).
- **D3** Full primary-vs-audit row diff, not just summary minima.
- **D4** Version-pinned rerun of both implementations in clean environments with archived logs and manifests. Two clean reruns so far (5 Sept, 9 Sept 2026) reproduce all result tables byte-for-byte; see `../../../verification/first-slab/CERTIFICATE_RERUN_20260909.md`. Logs enter the repository with the code.
- **D5** Fix items 0.1, 0.2, 0.5 in the Investigation write-ups before releasing them.

## 5. Optional strengthening (not verification)
- Promote the positivity-horizon crossings `L*_odd ≈ 0.7429`, `L*_even ≈ 0.8199`, `ω*_even ≈ 0.8611` from floating diagnostics to interval certificates.
- Extend the box sweep to `ω ≈ 0.85`: since `dD/ds = 2V*Q_sV`, certifying `Q_s ⪰ 0` on `[1/2, ω]` gives `D_ω ⪰ D_{1/2} ≻ 0` without any Paley–Wiener argument.
- Double the box count to 512 (box radius `2.42e−5` is now the second-largest erosion of the even margin after the Schur loss `9.96e−5`).
