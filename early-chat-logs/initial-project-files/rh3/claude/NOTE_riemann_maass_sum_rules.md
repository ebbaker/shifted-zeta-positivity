# Riemann vs. Maass: unpacking Perlmutter (11.19), and where the sum rules actually live

**2026-08-26.** Execution of `ROUND11` §6 item 2, the highest-value item in the physics column.
Perlmutter ([2509.21672](https://arxiv.org/abs/2509.21672)) §11.2 observes that discreteness of a
CFT spectrum forces the Riemann-zeta and Maass-cusp-form pieces of the spinning density to conspire,
and writes:

> *"(11.19) implies relations between the Riemann zeta zeros `{ρ_n}` and the Maass cusp form spectral
> parameters `{u_n}`. This can be turned into a quantitative, not just a qualitative, constraint as an
> infinite set of sum rules polynomial in the Riemann and Maass data. … It would be very exciting to
> make this observation fully rigorous."*

and, in the Introduction:

> *"the set of non-trivial Riemann zeta zeros and the set of parity-even `SL(2,ℤ)` Maass cusp form
> eigenvalues are not mutually independent."*

This note does four things the paper does not: writes the sum rules down explicitly (§2); observes a
**growth asymmetry** between the two families that has an RH-detector shape (§3); derives a
**conditional no-go** from that asymmetry and shows why the natural place to test the constraint is
the *bottom* of the spectrum, not the top (§4); and places the claim against prior art — the Selberg
and Kuznetsov trace formulae — which turns out to be closer than expected but **not** to subsume it
(§5).

**Headline.**

1. **The sum rules factorise cleanly.** All CFT dependence sits in two `j`-independent sequences —
   the residues `r_m` of `Q_Z` at the zeta poles, and the Maass overlaps `(Z,φ_n)`. The entire
   `j`-dependence is pure number theory: `σ_{ρ_m}(j) j^{−ρ_m/2}` on the Riemann side against the
   Hecke eigenvalue `λ_n(j)` on the Maass side. **That is exactly the Eisenstein-vs-cusp split of the
   Kuznetsov formula**, which is the right home for this object and is not named in the paper.
2. **The two families grow differently, and the exponent is `Re(ρ)/2`.** The zeta terms carry an
   envelope `λ^{Re(ρ_m)/2}` in the spin-`j` density; the Maass terms carry `λ^0`. On RH the exponent
   is exactly `1/4`. **This is a second, independent RH-detector of the same shape as the
   Dorigoni–Treilis one** — and it is in a different physical setting.
3. **Conditional no-go.** If the support of the zeta-plus-Maass part had gaps at large energy, the
   growth asymmetry would force *every* residue `r_m` to vanish — contradicting the paper's own
   Appendix D. So Appendix D and (11.19) together **predict** that this part of the density is
   asymptotically gapless. Cardy growth supplies exactly that, doubly-exponentially fast (§4).
4. **The constraint has no high-energy testing window.** The mean level spacing in the natural
   variable collapses like `exp(−2π√((c−1)λ/3))`. Any usable form of (11.19) has to be read near the
   twist threshold. **That is the opposite of the paper's stated objective** — *"to find and solve
   constraints that act on high-energy states alone"* (§1).
5. **Correction to the record.** The first level-1 Maass form, `u = 9.53369526`, is **odd**. The
   parity-even subset relevant here starts at `u = 13.77975135…`. The even subset is sparser than the
   full spectrum, which is what the Selberg trace formula constrains — so the prior-art objection in
   §5 is weaker than it first looks.

---

## 1. Setup, in the paper's notation

The spin-`j` Virasoro primary density splits (Perlmutter (11.6)) as

> `ρ_j(λ) = ρ_j^{(D)}(λ) + ρ_j^{(ζ)}(λ) + ρ_j^{(φ)}(λ)`

with `λ = ∆ − (c−1)/12`. The Dirichlet part is already discrete — **(11.16)**, a delta comb at
`λ = (j/2)(d²/(jµ) + jµ/d²)` over core frequencies `µ` and divisors `d | j` — which is the paper's
"pleasant surprise" and is special to Virasoro (Appendix J: `N > 1` gives a continuous density). The
other two, from **(11.8)**:

```
ρ_j^{(ζ)}(λ) = 2Θ(λ−j)/√(λ²−j²) · Σ_m Res_{s=(1+ρ_m)/2}[a_j^{(s)} Q_Z(s)] cosh(ρ_m y_j(λ)/2) + c.c.
ρ_j^{(φ)}(λ) =  Θ(λ−j)/√(λ²−j²) · Σ_n b_j^{(s_n)} (Z,φ_n) cos(u_n y_j(λ))
```

with `y_j(λ) = cosh^{−1}(λ/j)`, `s_n = 1/2 + iu_n`, and the Eisenstein Fourier coefficient
`a_j^{(s)} = 2σ_{2s−1}(j)/j^{s−1/2}` (Perlmutter (11.2); same as Di Ubaldo–Perlmutter
[2307.03707](https://arxiv.org/abs/2307.03707) (2.3)). The discreteness condition is **(11.19)**:

> `ρ_j^{(ζ)}(λ) + ρ_j^{(φ)}(λ) = Σ_k c_j^{(k)} δ(λ − λ_j^{(k)})`.

---

## 2. The sum rules, written out

Two elementary moves make the structure visible.

**(a) The residue factorises, and the `j`-dependence is a divisor sum.** `a_j^{(s)}` is a *finite*
sum, `2Σ_{d|j}(d²/j)^{s−1/2}`, hence **entire in `s`** — it contributes no poles and no zeros of its
own. So

> `Res_{s=(1+ρ_m)/2}[a_j^{(s)} Q_Z(s)] = a_j^{((1+ρ_m)/2)} · r_m`,  `r_m := Res_{s=(1+ρ_m)/2} Q_Z(s)`,

and at that pole `s − 1/2 = ρ_m/2`, `2s−1 = ρ_m`, so

> **`a_j^{((1+ρ_m)/2)} = 2 σ_{ρ_m}(j) · j^{−ρ_m/2}`.**

Verified numerically to `10⁻³¹` for `j = 1,2,6,12` (`m1_riemann_maass.py`), and the underlying
identity `2σ_{2s−1}(j)/j^{s−1/2} = 2Σ_{d|j}(d²/j)^{s−1/2}` to `5·10⁻³⁰` across `j = 1…20` and four
complex `s`. **The CFT data enters only through the `j`-independent sequence `{r_m}`.**

**(b) The Jacobian cancels.** Change variable to `y = y_j(λ)`, so `λ = j cosh y` and
`√(λ²−j²) = j sinh y`, while `dλ = j sinh y dy`. The `1/√(λ²−j²)` prefactor is exactly cancelled, and
discreteness in `λ` is equivalent to discreteness in `y`. Both terms become bare oscillatory sums.

Putting these together, and normalising the Maass forms so `b_1^{(n)} = 1` (whereupon
`b_j^{(n)} = λ_n(j)`, the Hecke eigenvalue — standard, cf. Then, *Math. Comp.* **74** (2005) 363):

> ### The sum rules
>
> For every `j ≥ 1`,
>
> ```
> G_j(y) := 4 Re Σ_m r_m σ_{ρ_m}(j) j^{−ρ_m/2} cosh(ρ_m y/2)
>         +      Σ_n (Z,φ_n) λ_n(j) cos(u_n y)
> ```
> must be a locally finite sum of delta functions in `y`. Equivalently, for every test function `w`
> supported away from that delta set,
>
> ```
> 4 Re Σ_m r_m σ_{ρ_m}(j) j^{−ρ_m/2} ŵ_cosh(ρ_m)  +  Σ_n (Z,φ_n) λ_n(j) ŵ_cos(u_n)  =  0
> ```
> with `ŵ_cosh(ρ) = ∫ cosh(ρy/2) w(y) dy` and `ŵ_cos(u) = ∫ cos(uy) w(y) dy`.

That is Perlmutter's "infinite set of sum rules polynomial in the Riemann and Maass data", made
explicit: **linear in `(r_m, (Z,φ_n))`, and polynomial in the arithmetic data through `σ_ρ(j)` and
`λ_n(j)`.**

At `j = 1` the divisor sum is `1` and the Hecke eigenvalue is `1`, so the first rule sees both
sequences bare:

> `4 Re Σ_m r_m cosh(ρ_m y/2) + Σ_n (Z,φ_n) cos(u_n y) = discrete.`

---

## 3. The growth asymmetry, and a second RH-detector

`cos(u_n y)` is bounded. `cosh(ρ_m y/2)` is not: its envelope is `e^{y·Re(ρ_m)/2}`. Since
`e^y ≈ 2λ/j` at large `λ`,

> **the zeta part of the spin-`j` density carries an envelope `λ^{Re(ρ_m)/2}`, while the Maass part
> carries `λ^0`.**

| `Re ρ` | envelope exponent in `λ` |
|---|---|
| `1/2` (RH) | `0.250` |
| `0.60` | `0.300` |
| `0.75` | `0.375` |
| `0.99` | `0.495` |

So **RH ⟺ the zeta contribution to the spinning density has envelope exactly `λ^{1/4}`**, and an
off-line zero with `Re ρ = σ > 1/2` produces `λ^{σ/2}`, strictly larger. Structurally this is the
same detector as `NOTE_n4_reformulation` §3.4 — "the envelope exponent is a fixed linear function of
`Re ρ`, and RH is the statement that it takes its critical-line value" — arising in a completely
different physical setting (a 2d CFT spinning density versus a 4d N=4 integrated correlator).

The same five-slot screen applies, with the same answer on the last slot: **nothing in the CFT forces
the exponent.** Worth recording as a second data point on the shape rather than as a new route.

*(Note that the `s = ρ_m/2` poles of `Q_Z`, allowed by (4.14), do not appear here: §11.1 deforms the
contour rightward from `σ = 1/2` to `σ = 1` and picks up only the `Re s > 1/2` family, which on RH is
`Re s = 3/4`.)*

---

## 4. A conditional no-go, and where the constraint can be tested

The asymmetry has teeth. Take a fixed smooth bump `w`, translate it to height `Y`, and pair:

- **Zeta part.** `∫cosh(ρ y/2) w(y−Y) dy ≈ ½ e^{ρY/2} Ŵ(ρ)` with `Ŵ(ρ) = ∫e^{ρt/2}w(t)dt`, which
  decays faster than any polynomial in `Im ρ` because `w` is smooth and compactly supported. On RH
  this gives `∫ρ_j^{(ζ)} w_Y = 2 e^{Y/4} · P_j(Y)`, where
  `P_j(Y) = Re Σ_m r_m σ_{ρ_m}(j) j^{−ρ_m/2} Ŵ(ρ_m) e^{iγ_m Y/2}` is **Bohr almost-periodic** in `Y`
  (absolutely convergent, provided `r_m` grows at most polynomially).
- **Maass part.** `∫ρ_j^{(φ)} w_Y = Re Σ_n (Z,φ_n)λ_n(j) ŵ(u_n) e^{iu_n Y}` — almost-periodic, and
  **not** growing.

If `w_Y` can be chosen supported away from the delta set for a relatively dense set of heights `Y`,
then `e^{Y/4}P_j(Y) + Q_j(Y) = 0` there, so `P_j(Y) = −e^{−Y/4}Q_j(Y) → 0` along that set. A Bohr
almost-periodic function vanishing in the limit along a relatively dense set is identically zero
(modulo a uniformity condition on the vanishing set — flagged, not proved here). That would force
`r_m Ŵ(ρ_m) = 0` for every `m` and every admissible `w`, hence **`r_m = 0` for all `m`** — i.e. `Q_Z`
has no zeta poles at all, in flat contradiction with **Appendix D**, which proves (under a weak
assumption) that an irrational Virasoro CFT with a convergent series must have at least one.

The escape is the hypothesis, and it fails decisively:

> **There is no large-`y` window free of spectrum.** With `λ = j cosh y` and `dy ≈ dλ/λ`, the mean
> `y`-spacing is `δ_y ~ 1/(λ ρ_Cardy(λ))`, and `ρ_Cardy(λ) ≈ (2/λ)e^{2π√((c−1)λ/3)}`.

| `c` | `y` | `λ` | mean `δ_y` |
|---|---|---|---|
| 3 | 2 | 3.76 | `2.4 × 10⁻⁵` |
| 3 | 5 | 74.2 | `3.2 × 10⁻²⁰` |
| 3 | 10 | `1.1 × 10⁴` | `7.6 × 10⁻²³⁵` |
| 25 | 5 | 74.2 | `1.6 × 10⁻⁶⁷` |
| 25 | 20 | `2.4 × 10⁸` | `10⁻¹²⁰²¹⁰` |

So two things follow.

1. **Appendix D and (11.19) together predict that `ρ_j^{(ζ)} + ρ_j^{(φ)}` is asymptotically
   gapless.** Not merely "discrete" — its support must close up fast enough to defeat the argument
   above. Cardy growth supplies that with enormous room, so the prediction is consistent; but it is a
   real constraint, and it is not in the paper.
2. **The sum rules are only testable at small `y`** — near the twist threshold `λ = j`, where the
   spectrum is sparse and individual states are resolvable. Perlmutter's stated objective in §1 is
   *"to find and solve constraints that act on high-energy states alone."* **(11.19) is the opposite
   kind of constraint.** That is not a defect — low-lying spectral constraints are exactly what the
   modular bootstrap trades in — but it relocates the item, and it means the natural collaborators
   are the twist-gap people (his own (11.18)) rather than the black-hole-microstate people.

---

## 5. Prior art: the Selberg and Kuznetsov trace formulae

This is the screen the project always runs: *is the physics producing a new arithmetic relation, or
recovering a known one?* The answer is more interesting than either.

**The Selberg trace formula already links `{u_n}` to the Riemann zeros.** For `PSL(2,ℤ)\H` — one
cusp — the trace formula carries a continuous-spectrum term built from the scattering matrix

> `φ(s) = √π Γ(s−1/2)ζ(2s−1) / (Γ(s)ζ(2s)) = ξ(2s−1)/ξ(2s)`,

appearing as `(1/4π)∫h(t)(φ′/φ)(1/2+it)dt` together with `¼h(0)(1−φ(1/2))`. Since
`φ′/φ(s) = 2(ξ′/ξ)(2s−1) − 2(ξ′/ξ)(2s)`, it has poles exactly at the non-trivial zeros of `ζ(2s−1)`
and `ζ(2s)`. So the trace formula ties `Σ_n h(u_n)` to a sum over Riemann zeros, and has since 1956.
Zworski puts the underlying fact plainly: *"the zeros of the Riemann zeta function … are the
resonances of the Laplacian on the modular surface."* The systematic version — that the
continuous-spectrum term of the trace formula *is* an explicit formula over `L`-function zeros — is
Wong, [1608.02296](https://arxiv.org/abs/1608.02296).

**But it does not subsume Perlmutter's claim, for two specific reasons.**

- **Parity.** The Selberg trace formula constrains the *full* spectrum `{u_n}`, weighted by `h`.
  Perlmutter's statement is about the **parity-even** subset (his footnote 55 restricts to even Maass
  forms, which are the ones relevant to parity-invariant CFT observables). Separating parities
  requires a reflection-twisted trace formula, so "Selberg already did this" is not literally the same
  statement. The even subset is genuinely sparser: **the first, second, fourth, fifth and sixth
  level-1 forms are all odd.**
- **Fourier coefficients.** The Selberg trace formula never sees `b_j^{(n)}`. (11.19) does — the
  `j`-dependence is the whole content. The formula that carries Fourier coefficients, with exactly
  the `λ_n(j)`-vs-`σ_{2it}(j)` split derived in §2, is **Kuznetsov**:
  `Σ_n ν_n(m)\overline{ν_n(j)} h(u_n)/cosh(πu_n) + (1/π)∫ σ_{2it}(m)σ_{2it}(j)(mj)^{−it}|ζ(1+2it)|^{−2}h(t)dt = Σ_c c^{−1}S(m,j;c)k^*(·) + δ_{mj}(·)`.
  (11.19) is *linear* in `b_j^{(n)}`, not bilinear, because one index is contracted against the CFT
  through `(Z,φ_n)`.

> **Verdict on prior art.** The qualitative claim — that the two sets are not independent — is
> classical in the Selberg sense and should be cited as such rather than presented as new. What is
> new is (i) the parity-even restriction and (ii) the appearance of the Fourier coefficients, which
> puts the object in the Kuznetsov family. **Any write-up must lead with the Selberg statement and
> then say precisely what (11.19) adds to it.** Without that, a number-theory referee closes the
> paper at the abstract.

**Unclaimed.** No published work derives sum rules relating `{ρ_n}` to `{u_n}` beyond the trace
formula. None of the four adjacent physics papers — Di Ubaldo–Perlmutter
[2307.03707](https://arxiv.org/abs/2307.03707), Haehl–Reeves–Rozali
[2309.00611](https://arxiv.org/abs/2309.00611) and
[2309.02533](https://arxiv.org/abs/2309.02533), Boruch et al.
[2503.00101](https://arxiv.org/abs/2503.00101) — states such relations. Perlmutter 2509.21672 has six
citations and **none pursues §11.2.**

---

## 6. Honest assessment against the ledger

`ROUND11` ranked this "the first item in the physics column where a physical requirement yields a
*new relation* on the zeros rather than restating a known one." That ranking needs adjusting in both
directions.

**Down.** The relation is **not** pure arithmetic. The CFT data `{r_m}` and `{(Z,φ_n)}` enter
linearly and cannot be removed from a single theory. To get a statement about `{ρ_n}` and `{u_n}`
alone one has to eliminate them — which requires the constraint to hold across a family of CFTs
large enough to make the elimination non-vacuous. That is a landscape statement, and the landscape
is exactly what nobody knows (his own Discussion: *"there is no obvious non-perturbative meaning of
a 'family of CFTs'"*). **The elimination step is the whole difficulty, and it is not a technical
gap — it is the same open problem the rest of the paper is about.**

**Up.** The mechanism is a genuine *producer*, not a consumer: discreteness of a spectrum is a
physical input that does not mention `ζ`, and the output is a constraint that does. On the Remmen
test — *could someone compute the observable having never computed a zeta zero?* — the answer is
yes: `ρ_j(λ)` is the CFT's own spin-`j` density. **This passes where every relabelling fails.** It is
the cleanest producer in the ledger, and the fact that its payload is conditional on the landscape is
a separate matter from its provenance.

**Where it lands.** Not a route to RH. A well-posed and unclaimed problem in the interface, whose
honest statement is:

> *Discreteness of a parity-invariant Virasoro CFT spectrum imposes, for every `j`, a linear relation
> between the residues of `Q_Z` at the Riemann-zeta poles (weighted by `σ_{ρ}(j)j^{−ρ/2}`) and the
> Maass overlaps (weighted by Hecke eigenvalues `λ_n(j)`). Making this a relation between `{ρ_n}` and
> `{u_n}` alone requires eliminating the CFT data across a family.*

That is worth writing to Perlmutter, together with §3 (the growth asymmetry he does not note), §4
(the gapless prediction and the small-`y` testing window), and §5 (the Selberg/Kuznetsov placement,
which the paper needs before it meets a number theorist).

---

## 7. What to do next on this item

1. **Do the elimination on the one solvable case.** For the compact free boson, `Q_Z^{(c=1)}` has
   **no** zeta poles at all (Appendix D's contrapositive), so all `r_m = 0` and (11.19) collapses to
   *"the Maass part alone is discrete"* — a check, not a constraint. Narain at `c = 2` gives
   `Q_Z = 2E_s(ρ)E_s(σ)`, still no zeta poles. **Find the simplest CFT where `r_m ≠ 0`.** By
   Appendix D that means an irrational Virasoro CFT with a convergent series, which is exactly the
   hard case. Worth knowing whether *any* example is computable.
2. **Test at small `y`.** §4 says the constraint is only usable near the twist threshold. Write
   (11.19) at `λ` slightly above `j` and see what it says about the lightest spin-`j` states —
   compare against (11.18), Perlmutter's own twist-gap bound, which came from the Dirichlet part
   alone and is only valid if the other two parts do not cancel it.
3. **Settle the almost-periodicity step in §4** — the uniformity condition on the vanishing set. If
   it holds, §4's conditional no-go becomes an unconditional prediction of gaplessness.
4. **Ask whether the `λ^{Re(ρ)/2}` envelope is constrained by anything.** Same question as
   `NOTE_n4_reformulation` §5 item 4, in a second setting. Two independent negatives would be worth
   recording jointly; a positive in either would be a different paper.

---

## 8. Reproduction

| script | produces |
|---|---|
| `m1_riemann_maass.py` | §2 — the `a_j^{(s)}` identity and the residue factorisation, numerically; §3 — the envelope exponents; §4 — the mean-spacing collapse; §5 — the corrected parity-even Maass data |

`mpmath`, `sympy`.

**Sources.** Perlmutter [2509.21672](https://arxiv.org/abs/2509.21672) §§4, 5.1, 11, 11.1, 11.2,
Appendices D and J — read in full · Di Ubaldo–Perlmutter
[2307.03707](https://arxiv.org/abs/2307.03707) eqs. (2.2)–(2.3) · Selberg trace formula for
`PSL(2,ℤ)`: Hejhal, *The Selberg Trace Formula for PSL(2,ℝ)* Vol. 2; Iwaniec, *Spectral Methods in
Automorphic Forms* §10; Goldfeld, *Trace Formulae* Prop. 4.2 (`M(s) = √πΓ(s−1/2)ζ(2s−1)/(Γ(s)ζ(2s))`)
· Wong [1608.02296](https://arxiv.org/abs/1608.02296) (trace-formula term = explicit formula over
`L`-zeros) · Zworski, *Mathematical study of scattering resonances* (zeta zeros as modular-surface
resonances) · Kuznetsov formula: Blomer [1912.08137](https://arxiv.org/abs/1912.08137) eq. (5) ·
Hecke normalisation: Then, *Math. Comp.* **74** (2005) 363 · Maass eigenvalue data: LMFDB level-1
Maass forms, Booker–Strömbergsson–Venkatesh, *IMRN* (2006) · Haehl–Reeves–Rozali
[2309.00611](https://arxiv.org/abs/2309.00611), [2309.02533](https://arxiv.org/abs/2309.02533) ·
Boruch–Di Ubaldo–Haehl–Perlmutter–Rozali [2503.00101](https://arxiv.org/abs/2503.00101).
