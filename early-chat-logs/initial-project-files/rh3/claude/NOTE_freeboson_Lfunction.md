# The compact free boson's L-function: the zeros of the analytic factor lie on the critical line

**2026-08-26.** A short note on Perlmutter, *CFT and the Riemann zeta function* / L-functions for CFT
([2509.21672](https://arxiv.org/abs/2509.21672)), §10.2. Everything here is elementary; the point is
that it is elementary and unstated, and it answers a question the paper poses.

**Claim.** For the compact free boson at radius `r`, the analytic factor `Q_Z^{(c=1)}` of the CFT
`L`-function has zeros — the paper records only the absence of *poles* — and **every one of them lies
on `Re s = 1/2`, unconditionally**, at

> `s = 1/2 + iπ(2k+1)/(4 log r)`, `k ∈ ℤ`.

At the self-dual radius `r = 1` the factor is the constant `4` and there are none. So the full zero
set of `L_Z^{(c=1)}` is

> `{ρ/2} ∪ {(1+ρ)/2} ∪ {1/2 + iπ(2k+1)/(4 log r)}` —
> the Riemann zeros twice over, rescaled, plus an explicit arithmetic-free on-line family.

**And the property is not a two-term accident.** Writing any reciprocal analytic factor as
`Q(s) = 2Σ_n A_n cosh((s−1/2)log µ_n)` with `A_n = a_n µ_n^{−1/2}`, the two-pair lattice case is
exactly solvable: **all zeros lie on `Re s = 1/2` iff `A₂ ≥ A₁`**, i.e. iff the larger frequency
carries the larger effective weight (§5). Since `A_n` weights high frequencies up and Cardy growth
forces the heavy end of the spectrum to be large, the on-line regime is the physically natural one.
That is a suggestive alignment, not a theorem about CFTs — but it gives §3.1(vi) a candidate answer.

The `c = 1` statement itself matters for three reasons: it is the exact contrapositive of §10.2.1's warning about Epstein
zetas; the linear-in-`T` density of that family **is** the subleading term footnote 26 says the
spectral-gap bound controls, and it vanishes exactly where §10.2.2 says the bound saturates; and it
means the "simplest CFT has the simplest L-function" reading extends to the zeros, not just the
factorisation.

---

## 1. Setup

Perlmutter §10.2 gives, for the compact boson at radius `r`:

- **(10.33)** `Q_Z^{(c=1)}(s) = 2(r^{2s−1} + r^{1−2s})`
- **(10.34)** core frequency set `S_core^{(c=1)} = {r², r^{−2}}`
- **(10.35)** `L_Z^{(c=1)}(s) = 2^{s+1/2}(r^{2s−1} + r^{1−2s}) ζ(2s) ζ(2s−1)`,
  `Λ_Z^{(c=1)}(s) = 4√π · 2(r^{2s−1}+r^{1−2s}) Λ(s) Λ(1−s)`

with `Λ(s) = π^{−s}Γ(s)ζ(2s) = ξ(2s)`. His reading: *"The meaning of these Riemann zeta factors was
originally unclear in [32], but the L-function perspective gives their appearance a certain
synergistic explanation: the 'simplest' CFT has the 'simplest' L-function!"*

**Independent derivation** (done before §10.2 was in hand, from in-window equations only, and
recorded here because it is a check on the transcription). Start from BCFMP
[2107.10744](https://arxiv.org/abs/2107.10744) **(3.12)**:

```
(Z^{c=1}, E_s) = 2 Λ(s) (r^{1−2s} + r^{2s−1}),      Λ(s) = Λ(1/2 − s)
```

Send `s → 1−s` and use `Λ(1−s) = Λ(s−1/2) = π^{1/2−s}Γ(s−1/2)ζ(2s−1)`. Compare with Perlmutter
**(3.8)** `(Z, E_{1−s}) = (2π)^{1/2−s}Γ(s−1/2) L_Z(s)/ζ(2s)` and **(3.36)**
`Q_Z(s) = 2^{1/2−s}L_Z(s)/[ζ(2s)ζ(2s−1)]`. This gives (10.33) and (10.35) exactly, constants
included.

Three numerical checks (`p1_freeboson.py`, `mpmath`, `dps = 40`):

| check | source | result |
|---|---|---|
| derivation reproduces (3.8) from (3.12) | — | rel. diff `~3 × 10⁻³¹`, four radii × two points |
| `Q_Z(s) = Q_Z(1−s)` | Perlmutter **(3.37)** | holds to `10⁻³¹` — *emerges*, was not imposed |
| `Q_Z(s) ~ µ₁^{−s}` as `s → ∞` | Perlmutter **(5.10)** | `Q(s+1)/Q(s) → r²` exactly, so `µ₁ = r^{−2} = λ₁` |

The last two are the paper's own constraints on `Q_Z`, satisfied without adjustment.

---

## 2. The zeros

`Q_Z^{(c=1)}(s) = 0` iff `r^{2s−1} = −r^{1−2s}`, i.e. `r^{2(2s−1)} = −1`, i.e.
`2(2s−1)\log r = iπ(2k+1)`:

> **`s = 1/2 + iπ(2k+1)/(4 log r)`, `k ∈ ℤ`.**

Spacing `π/(2 log r)` in the ordinate; `Re s = 1/2` for every `k`.

**They cannot leave the line.** `|r^{2s−1}| = r^{2Re s − 1}` and `|r^{1−2s}| = r^{1−2Re s}`. Equality
of moduli — necessary for cancellation — forces `2Re s − 1 = 1 − 2Re s` whenever `r ≠ 1`. There is no
room; this is a two-term exponential sum, and the "critical line" here is just the axis of symmetry
of `s ↦ 1−s` that (3.37) already asserts.

Verified to `10⁻³¹` at the predicted points for `r = 0.7, 1.6, 3.0`; a scan over `Re s ∈ [−2,4]`
returns no off-line zero; at `r = 1`, `Q_Z ≡ 4`.

**Why it is worth stating.** §10.2.1 warns, correctly and in general, that *"Epstein zetas do not obey
a Generalized Riemann Hypothesis and, lacking an Euler product, can even have zeros in the half-plane
of absolute convergence."* The `c = 1` core Epstein zeta is the case where that failure does **not**
occur — trivially, but explicitly. Since the paper records the absence of poles and the reciprocity of
`S_core` (Appendix D: *"these two features are one and the same: convergence of the series down to the
critical line implies reciprocity"*) but never asks where `Q_Z` vanishes, the zero-side statement
completes the picture for the one CFT where it can be completed by hand.

---

## 3. The density bound: the zero family is the subleading term

This started as an apparent tension and ended as a mutual confirmation, so it is worth writing out.

The `Q_Z` zeros have density **linear** in `T` — spacing `π/(2 log r)` gives `~ 4T log r/π` up to
height `T` — while `N_ζ(T) ~ T log T`. So an added zero family at linear density looked like it might
sit awkwardly against the strict density inequality (5.8).

**Footnote 26 resolves it, and identifies the family:**

> *"Since the `s → ∞` asymptotic (5.10) is exponential, not factorial, on account of the cancelling
> gamma factors, the spectral gap controls a **subleading correction** to this. The correction can be
> shown to be of the form `N_{L_Z}(T) − N_ζ(T) ∼ −T log µ₁` times a positive constant."*

`−T log µ₁ = 2T log r` with `µ₁ = r^{−2}` — the same linear-in-`T` count, up to the positive constant.
**The excess zeros the density bound predicts are exactly the analytic factor's zeros.**

And §10.2.2 closes it at the endpoint:

> *"At `c = 1`, the gap is bounded as `λ₁ ≤ 1/2`, with saturation at the self-dual radius `r = 1`.
> Indeed, the self-dual boson saturates the density bound: at `r = 1`, `Q_Z^{(c=1)}(s)` is constant."*

With `µ₁ = 2λ₁` and `S_core = {r², r^{−2}}`, `λ₁ = min(r², r^{−2})/2 ≤ 1/2`, equality iff `r = 1` —
and at `r = 1` the zero family is empty, consistent with saturation. Both directions check.

---

## 4. What this is and is not

**Is:** a completed description of the zero set of the one CFT `L`-function that is fully explicit; a
worked contrapositive to the Epstein-zeta warning; and a consistency check on (5.8)/footnote 26 that
runs through an object the paper does not compute.

**Is not:** evidence for anything about `ζ`. The on-line family is arithmetic-free — it comes from
`r^{2(2s−1)} = −1` and would be there for any two-term reciprocal frequency set. It is a remark, and
its value is that it makes the `c = 1` case a complete worked example rather than a partial one.

**The open question this touches.** §3.1(vi) asks which CFT data controls the analytic factor's
analytic structure. For `c = 1` the answer is now complete on both sides: poles absent because
`S_core` is finite and reciprocal; zeros present, on-line, and counted by the spectral gap. §5 asks
what happens beyond two terms, and the answer is sharper than expected.

---

## 5. Beyond two terms: the on-line property is a coefficient-dominance condition

Not a two-term accident, and not generic either. The reduction is one line.

For any reciprocal frequency set, write `Q(s) = Σ_n a_n(µ_n^{−s} + µ_n^{−(1−s)})` — the form that
makes `Q(s) = Q(1−s)` automatic. Put `x = s − 1/2`. Since
`µ^{−s} + µ^{−(1−s)} = 2µ^{−1/2}cosh(x log µ)`,

> **`Q(s) = 2 Σ_n A_n cosh(x log µ_n)`, with `A_n := a_n µ_n^{−1/2} > 0`.**

So *all zeros lie on `Re s = 1/2`* iff the cosine sum `Σ_n A_n cos(y log µ_n)` has only real zeros.
The `c = 1` free boson is the one-term case `A cosh(x log µ) = 0`, which is on-line for free.

**The lattice case is exactly solvable.** If the frequencies are commensurable, `µ_n = µ^{k_n}`, set
`w = µ^x`; then `Re s = 1/2 ⟺ |w| = 1`, and `Q = 0` becomes a self-inversive polynomial in `w`.

For two pairs with `k = (1,2)` — `S_core = {µ^{±1}, µ^{±2}}` — clearing denominators gives
`A₂(w⁴+1) + A₁w(w²+1) = 0`; with `v = w + 1/w` this is `A₂v² + A₁v − 2A₂ = 0`, and `|w| = 1 ⟺ v`
real with `|v| ≤ 2`. The larger root is harmless; the smaller one satisfies `|v| ≤ 2` iff
`A₁ + √(A₁²+8A₂²) ≤ 4A₂`, i.e. iff `8A₁A₂ ≤ 8A₂²`. So:

> **All zeros lie on `Re s = 1/2` if and only if `A₂ ≥ A₁`** — the *larger* frequency must carry the
> larger effective weight. Sharp, with equality as the exact boundary.

Confirmed numerically at `µ = 0.4` (`p2b_lattice.py`): the predicted threshold `a₂* = √µ = 0.6324555`
separates `a₂ = 0.6325` (4 roots, none off-line) from `a₂ = 0.6324` (2 off-line), and the off-line
deviation grows continuously from there — `|Re s − 1/2| = 0.0084, 0.21, 0.46, 0.96, 2.04` at
`a₂ = 0.6324, 0.60, 0.50, 0.30, 0.10`.

Dominance is **sufficient but not necessary** in general: at `k = (1,3)` the zeros stay on the line
well past the dominance threshold (`a₂ = 0.399` against `a₂* = µ = 0.4`), and three pairs
`k = (1,2,3)` with `a_n ≡ 1` are entirely on-line even though `A₃ < A₁ + A₂`. Off-line zeros appear
once the top frequency is suppressed hard enough (`a₃ = 0.05` at `k = (1,2,3)`).

**Why this is the interesting direction.** `A_n = a_n µ_n^{−1/2}` weights the *high* frequencies up.
In a CFT the high-energy density of states is not free to be small — Cardy growth forces it up. The
regime in which these toy factors keep their zeros on the critical line is precisely the regime where
the heavy end of `S_core` dominates, which is the physical regime; the off-line examples are all
built by artificially suppressing the largest frequency. That is a suggestive alignment and nothing
more — these are truncated toy factors, not a CFT's actual `Q_Z`, which is an infinite series with
its own convergence structure. But it converts §3.1(vi) from "which data controls the analytic
structure" into a concrete question with a candidate answer: **the effective coefficients
`a_n µ_n^{−1/2}`, and whether they are non-decreasing in `µ_n`.** Appendix D's argument already runs
on exactly this tension — Cardy growth versus reciprocity — from the pole side.

---

## 6. Reproduction

| script | produces |
|---|---|
| `p1_freeboson.py` | §1–3 — the derivation, the three consistency checks, the predicted zero locations at `r = 0.7, 1.6, 3.0`, the `r = 1` degeneration, the off-line scan |
| `p2b_lattice.py` | §5 — the `cosh` reduction, the self-inversive polynomial, the sharp `A₂ ≥ A₁` threshold, and the `k = (1,3)` / three-pair counterexamples to necessity |

`mpmath` only.

**Sources.** Perlmutter [2509.21672](https://arxiv.org/abs/2509.21672) §§3.1, 5, 10.2, 10.2.1,
10.2.2, fn 26, Appendix D — read in full · Benjamin–Collier–Fitzpatrick–Maloney–Perlmutter
[2107.10744](https://arxiv.org/abs/2107.10744) eq. (3.12).
