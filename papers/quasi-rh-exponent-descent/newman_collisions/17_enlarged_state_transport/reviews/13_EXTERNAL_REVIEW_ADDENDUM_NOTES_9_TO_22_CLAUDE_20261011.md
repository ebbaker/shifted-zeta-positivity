# External review addendum: project 17, Notes 9–22 (commit 06d76f8)

11 October 2026. Prepared for Edward Baker. Reviewer model: Claude Fable 5.1
(`claude-fable-5-1`), Anthropic, in Claude Cowork. Cross-model review of
material prepared with GPT-6 / GPT-6.1-sol / GPT-6-astra (Codex). Source
state: `main` at `06d76f8` ("Changed numbering").

This addendum covers everything added since review 12 (which examined the
folder at `9e98460`): Notes 9–22, internal reviews 6–11, eight checkers
with records, and ~860 new manuscript lines (Notes 9–15 integrated; 16–22
not). Three parallel Claude reviewers split the material (Notes 9–14 with
the manuscript additions; Notes 15–17; Notes 18–22 with the interface
checkers). I verified the two logical points in section 2 myself.

Facts used from the earlier reviews: (A) the threshold expression at an
all-real double zero is `72W²Σ(x−ρ)⁻²`; (B) `q_{T,b}` has Newman constant
exactly `T`; (C) the transport certificate is an equivalence with the
first-jet test; (D) all zeros of `H_t` with `|x| ≤ 6·10¹⁰`, `t ≤ 0.2`, are
real and simple (Polymath 15 + Platt); (E) `H_x² − HH_xx = H²Σ_ρ(x−ρ)⁻²`,
so the two-sign criterion is Laguerre on the stationary sets and its global
form is equivalent to RH.

## 1. Verdict

Unchanged: close with closure note, promise 1/5. No mathematical error was
found in roughly 300 further displayed equations; all eight checkers pass
under `python3 -I` and regenerate their records exactly (modulo
`python_version`/`runtime_seconds`); every certified number was reproduced
by independent code. The new material is of three kinds: correct
representation results and self-obstructions that retire the project's own
Note-8 proposals (Notes 9–14); "weaker" sufficient criteria that are
logically equivalent to their conclusion (Notes 16–17); and a genuine,
standard improvement of the approximation interface (Notes 20–22) that
should be adopted elsewhere but does not leave the region where known
results force every certified sign.

One thing in this batch deserves to outlive the project: the corrected
interface of Note 20, validated here against the genuine `H_t` at moderate
heights (section 4).

## 2. Notes 16–17: the bounded-loss and Hölder-loss criteria

Statements. Let `E = H² + H_x²`. (BL): if locally bounded `C₀, C₁ ≥ 0`
exist with `H_x = 0 ⇒ HH_xx ≤ C₀E` and `H_xx = 0 ⇒ H_xH_xxx ≤ C₁E`, then
there is no joint zero in `Ω`. (HL): the same with `E^{1−δ}`,
`δ < 1/(2⌊M/2⌋)`, given a multiplicity budget `M`. Both proofs are correct
(predecessor-branch rates `HH_xx/E = r/h + O(1)`, odd case via `F = H_x`
with `H = O(h^{r+1})`, sharpness of `δ = 1/(2r)` by the heat polynomial
`P_r`; all verified by sympy).

Both are strictly weaker hypotheses than S0/S1 (e.g. `x² + 2(T−t) + 1`
fails S0 and satisfies (BL0)), but they are weakened exactly to the
conclusion: on any open `Ω`, (BL) holds for some locally bounded
`C₀, C₁` **if and only if** there is no joint zero in `Ω`. The converse is
two lines — if `E > 0` on `Ω` then `C₀ := max(0, HH_xx)/E` and
`C₁ := max(0, H_xH_xxx)/E` are continuous, hence locally bounded, and the
inequalities hold at every point. Note 17 states the converse in its last
section and still calls the criterion "the concrete gain"; it is not a
reduction. On a closed cell, certifying (BL) is certifying `E > 0`, i.e.
the first-jet test of (C). Globally it is `Λ ≤ 0`, i.e. RH.

Tests against the controls (numerical, mpmath): kernel (B) at
`T = 0.05`, `b = 1` has `HH_xx/E = 91.8, 991.9, 9991.9` at
`h = 10⁻², 10⁻³, 10⁻⁴` on its precursor branch (`h·ratio → 1`); the
project's own double-Gaussian control gives `97.3, 997.3, 9997.3`; the odd
control `z³ − 6sz` gives `1/h` exactly. Both violate (BL) and (HL) — as
they must, since they collide and the theorems are true. So proving either
criterion for theta is proving no positive-time collision for theta; no
shape-only argument can do it, and no intermediate estimate is on offer.

The Hölder "relaxation" is numerically empty at the certified heights:
Note 17's Blaschke budget at the Note-15 window evaluates to
`M ≈ 4.3·10¹⁰` (near-optimal `R = 2X`), forcing `δ < 2.3·10⁻¹¹`, so
`E^{1−δ}/E = 1 + 5·10⁻¹⁰` even at `E = 10⁻²⁰`. The actual multiplicity
there is 1 by (D).

## 3. Notes 18–19: the interface cannot decide its own targets

Note 18 proves, correctly, that at any strict-interior first-jet candidate
(`a*² + |s*| < 1` in the Schur–Pick body) there exists a real polynomial
backward-heat solution with an exact double zero at `(t₀, x₀)` that stays
inside the tube `|H/A − F| < η` on all nearby disks. The construction
(Schwarz–Pick realization of the first two Taylor coefficients, a free third
parameter, truncation with strict slack, finite heat series) is complete.
Consequence: nothing built from the finite approximant, a sup-norm disk
bound, the heat equation and analyticity can exclude a collision — or prove
(BL0) — at a strict-interior first-jet candidate. This is the `F → H`-side
form of (C), and it closes the door Notes 16–17 had just opened. The note
says "extra information about the genuine theta preparation is essential";
(B) adds that the extra information must be arithmetic.

Note 19 certifies, at the weakest second-stationary point of the `N = 22066`
survey (offset 58.57), that two functions inside the coarse tube share
value, slope and `H_xx = 0` with `G` and have opposite signs of
`H_xH_xxx` (`+371` and `−913`). Correct and nearly tautological: the
coarse third-derivative payment `6ηL³ = 472` exceeds the nominal third
jet `97.7`, and the extremal Schur function `w³` realizes the Cauchy
bound. Together with the survey (43 of 408 second-stationary points pass
the coarse payment at `N = 22066`; 317 of 468 at `N = 100000`), this is a
correct limitation statement about Note 15's "the full third-jet payment
can be overcome locally": that was the exception, not the rule. What
neither note says: by (D) and Laguerre for `H'`, the genuine sign at every
`H_xx = 0` point in this window was never in doubt; the "ambiguity" is an
artifact of the error interface, and its "resolution" in Note 20 certifies
a sign already known.

## 4. Notes 20–22: the explicit Riemann–Siegel correction

This is the one substantive technical advance in the batch. Note 20
retains Polymath's `C` term (Corollary 6.4, `A + B − C`, instead of
Corollary 6.5, `A + B`), derives the closed form
`C = (−1)^{N+1}(√π/4)e^{−πx/8 − tπ²/64}τ^{3/2}[u − v/τ]` (the phase of
`M₀(iτ)Ue^{iπ/8}` cancels exactly; verified by hand), and, since `C` is
not holomorphic in `z`, replaces it by the surrogate
`C(t, X)e^{−π(z−X)/8}` paid by an explicit FTC bound so that Cauchy applies.
Note 22 proves the entering reflected term matches the correction jump
across a natural cutoff change (identity `C₀(p+2) + C₀(p) = e^{iπ(p²/2+p+3/8)}`,
verified to 170 digits) with cost `O(Z/N²)`.

Independent validation against the genuine `H_t` — the test the folder does
not contain. With `H₀ = ξ(1/2 + ix/2)/8` via mpmath and
`H_t(x) = E[H₀(x + i√(2t)Z)]` for `t > 0`, the normalized residual
`|H − G|/A` versus `|H − G + C|/A`:

| x | t | N | uncorrected | corrected | gain |
| --- | --- | --- | --- | --- | --- |
| 5000 | 0 | 19 | 1.8·10⁻¹ | 1.2·10⁻⁴ | 1.5·10³ |
| 5000 | 0.05 | 19 | 1.6·10⁻¹ | 1.1·10⁻⁴ | 1.4·10³ |
| 10⁵ | 0.05 | 89 | 4.5·10⁻² | 1.4·10⁻⁵ | 3.4·10³ |
| 4·10⁵ | 0.1 | 178 | 1.5·10⁻² | 5.4·10⁻⁸ | 2.8·10⁵ |

Sign, prefactor, `τ^{3/2}` amplitude, the `u − v/τ` combination and the
heat exponent are all right. At the `N = 22066` cell the certified
residual `η* < 3.135063·10⁻⁷` reproduces digit for digit (ledger:
`K = 1.28507`, `E_AB = 2.41·10⁻⁸`, `Z = 1.928·10⁻³`, `B_C = 1.126·10⁻⁴`,
surrogate `1.44·10⁻⁶`), as do the corrected `H_xx = 0` point (offset
`58.5690878` in the certified band `[58.5690, 58.5695]`),
`H_xH_xxx/A² ≈ −270.65` (certified `< −270.41505`), and Note 22's edge
numbers (`Λ_edge = 2.9957·10⁻¹⁰`, matching cost `1.48469·10⁻¹²`, real-edge
mismatch `3.92003701457·10⁻¹³`). The old `η ≈ 0.0096` is `3·10⁴` times
larger; the stable manuscript's own `η_N ≈ 2.5·10⁻³` is `8·10³` times
larger.

Recommendation: the stable manuscript's `prop:diskerror` and project 13's
certificates should adopt (14)–(15) (fixed cutoff) or (24)–(25) (through
one cutoff change) of Notes 20/22. It depends on nothing beyond Polymath
Cor. 6.4 + Prop. 6.6, Stirling algebra, and the parent's normalizer bounds,
and holds for all `0 < t ≤ 1/2`. It does not change (D): every certified
cell remains at `x ≈ 6.1·10⁹`, and the candidate body of (C) shrinks to
width `O(Z/N)` but is, by Note 18, exactly as undecidable from inside as
before (Note 22 §8 says so).

Note 21 (`H_t(x) = E[H₀(x + i√(2t)Z)]`, Hermite moments recovering the
four jets) is textbook Stein/Gaussian integration by parts; (4)–(6) are
(BL0)/(BL1) rewritten, as the note says. Evaluating `ξ` at
`x ≈ 6·10⁹` to the required accuracy is the Riemann–Siegel problem again.

## 5. Notes 9–14 and the manuscript integration

Note 9 (paired contours): all constants (`D₀ = 11.2613`, `b = 4π − 39/4`,
`γ = 23/40`, `b± `, `2^{13/2}`) re-derived and numerically sane (bounds
hold with ratios `10⁻³`–`10⁻⁸`). At contour height `a_x = π/8 − 4π/x` the
theta decay parameter is `≈ 32π/x`, so the series is truncated at
`n ~ √x` and the product index at `P ~ x`: this is the approximate
functional equation with explicit constants, ~15× longer than the trivial
`N² = x/4π`. Applies verbatim to kernel (B). No sign (§8, admitted).

Note 10 (Mellin–Bessel): identities (A1)–(A16) verified by hand and
mpmath (the Bessel channel at `P = 2` to 17 digits; `𝓛₀(H₀; 2)` to 7
digits via the transform; `J'_{0,1}(0) = 0.0048719` inside the certified
hull). The full-line collapse (A5) is `ξ(q₊)ξ(q₋)/32`; the fixed product
channels are the terms of the Dirichlet series of `ζ(q₊)ζ(q₋)` times
gamma factors, which does not converge on the physical line. A correct
self-correction of Note 8's "arithmetic channels" proposal.

Note 11 (quasi-RH prime counting): exponent arithmetic correct
(`23/24 + β/12`, gain `3/80` at `β < 1/20`; `87/41 − 71/41 = 16/41`).
Inputs beyond the assumed strip: its Corollary 1.2 at modulus 3; short-family
Note 24's uniform partial summation; Note 28's continuum lower bound
extended to `β < 1/2`; the coprime lattice count. Given these, the
conclusion is that a positive sub-sum of the coherent sixth-power rows has
size `D^{1−o(1)}` — i.e. Möbius sums with trivial character cannot be
bounded column by column — an obstruction, correctly labelled.

On the 33/41 step, sharper than review 12 §6: `A_{p⁶}(D)` is `A₁` with
`p` masked (`χ_n(p⁶) = 1` for `p ∤ n`), and the extraction uses (H2) only
on the `D^{5/41}` sixth-power rows, where (H2) reads
`D^{5/41}(|A₁| − O(D^{33/41}))² ≪ D^{71/41}`, i.e. `|A₁| ≪ D^{33/41}`.
The hypothesis consumed is the conclusion, with the assumed 11/12 paying
only the masks.

Note 12 (carrier defect): all identities sympy-exact. The decisive one is
not stated: on `H'' = 0`, `BH' − 𝓡 ≡ −H'''` identically (arbitrary
`a, b`), so the "sign-oriented sufficient criterion" (13) =
`eq:carrier-signed-test`, which the manuscript's program section calls
"the needed next estimate", is `sgn(K₁)(−K₃) ≥ ε` with `ε_R ≈ 6L³η_N` —
the S1 test with the Note-15 budget (`463` vs `472`). The edge-mass
theorem says Dirichlet-polynomial mass sits at the cutoff edge where the
channel defect tends to `b`; correct, one paragraph.

Note 13 (phase currents, cones): (1), (2), (7) are rewritings of
`−H'H'''`; the relative cone hypothesis (each of `F', F''` nearly
single-frequency) fails exactly when there is cancellation, so it is
stronger than the target (admitted). The narrow-band counterexample is the
project-12 review's "positive-definite functions can have double zeros"
in Laguerre form.

Note 14 (fixed-product saddles): saddle `P = x/4π = N²`, width `√x`,
`ϑ_P ∋ −(x/2) log P`; "every fixed channel changes sign" is
"`P^{−ix/2}` oscillates". The `O(ℓ⁻¹)` bracket in (8)–(9) is correct
(deviation `0.64, 0.44, 0.34` at `x = 2·10³, 2·10⁴, 2·10⁵` against
`π/ℓ_P = 0.72, 0.47, 0.35`). Internal review 7's order-circle Bessel bound
for the endpoint is a real improvement.

Note 15 (high-height S1 cell): `x ∈ [6118670944.104, 6118670944.164]`,
`t ≈ 0.049991` — inside the box of (D). There `H_x` has only real zeros
near the cell, so `−H_xH_xxx = H_x²Σ_{ρ'}(x−ρ')⁻² > 0` at every
`H_xx = 0` point unconditionally. Independent replay: `H_xx = 0` at offset
`87.4106236`, `H_xH_xxx/A² = −35916.67` (certified `(−58146.06,
−13941.95)`), `−H_xxx/H_x = 17.27` (certified `(6.657, 28.063)`), the
latter being `Σ(x−ρ')⁻²` over the two nearest zeros of `H_x` at distance
`≈ 0.34`. Forced, as anticipated.

Manuscript integration: every transcribed constant agrees with the notes;
no conditional result is cited as unconditional; compile hash matches.
Two presentational issues: `eq:carrier-signed-test` should be identified as
S1; `prop:high-second-sign` should state that its rectangle lies inside
the box where the sign is a theorem.

## 6. Checkers and hygiene

All eight pass; runtimes here: paired boundary 1.8 s, cofactor transfer
<0.1 s, correlated jets 0.7 s, high S1 cell 66 s, disk ambiguity 67 s,
corrected cell 94 s, cutoff matching 18 s, survey 17 s + 114 s. Records
regenerate exactly except `python_version`/`runtime_seconds`; the survey's
root-array hashes are declared non-portable and differ under numpy 2.5
while all counts and weakest rows agree to `10⁻¹⁴`. Assertion counts:
"43 exact checks" in the cofactor checker are three distinct facts;
the correlated-jet counts (625/9375/…) are a `5⁴` grid over about six
identities. `DRAFT_HISTOR.md` is still misnamed and has no rows past
`22d6977` (Notes 16–22 absent). Notes 16–22 are not in the manuscript
(stated). Internal reviews 6–11 are same-model restatements; none mentions
(D), Laguerre, or the equivalence in section 2.

## 7. What to add to the closure note

Beyond review 12 §8: (BL)/(HL) ⇔ no joint zero in `Ω`, with the `1/h`
blow-up rates for (B) and the Gaussian control, and the budget figure
`M ≈ 4·10¹⁰`; Note 18's proposition as the `F → H`-side form of (C); on
`H'' = 0`, `BH' − 𝓡 ≡ −H'''`, so the carrier test is S1; the product
channels are the Dirichlet-series terms of `ζ(q₊)ζ(q₋)` and the matched
contour is the approximate functional equation with constants; (H2) on the
sixth-power rows is the 33/41 conclusion plus masks; (D) for the Note-15,
19, 20 and 22 cells; and the corrected interface of Notes 20/22 with the
validation table above, as a drop-in replacement for `prop:diskerror` and
project 13's `η`.

What should stop: stationary-sign calibrations below `x = 6·10¹⁰`; any
plan to obtain a signed residual bound near a vanishing joint first jet
from approximation-theoretic inputs (Note 18 shows this is impossible
without theta-specific information, and (B) shows that information must
be arithmetic); further rewriting of `−H'H'''`. Nothing in Notes 9–22
proposes a candidate for the arithmetic input.

No collision exclusion, threshold result, or RH conclusion is claimed or
refuted in this review.
