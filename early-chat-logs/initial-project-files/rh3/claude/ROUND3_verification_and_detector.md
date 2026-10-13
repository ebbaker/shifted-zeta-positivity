# Round 3: independent verification, two corrections, and a working off-axis detector

**2026-08-25 (session of 2026-08-24).** Independent re-examination of `BRIEF_instanton_size.md`,
`ASSESSMENT_instanton_size.md`, and `ROUND2_full_YM_and_results.md`. Nothing below reuses the
earlier rounds' scripts; every number was recomputed from scratch (`numpy`, `scipy`, `sympy`,
`mpmath`). Scripts in §8.

**Headline.** The Round-2 mathematics is sound: the Calogero–Moser pencil identity, the Λ-via-pencil
characterisation, the k=2 Λ table, the Hermite benchmark, and every spot-checked margin-map entry
reproduce exactly. Two corrections to Round 2's §6.3 are needed — the "worst case at n ≈ 8–12"
claim and the fitted `−2/d²` law are both artifacts of excluding the `n = 0` boundary column,
where the true minimum lives and decays like `~d^{−3}` (still polynomial; the qualitative
conclusion survives). And the requested new instrument now exists in prototype: a **Coulomb
velocity-residual detector** that localises a hypothetical off-axis zero from on-axis data alone,
distinguishes it from an unresolved on-axis pair by the **sign of a quadrupole moment**, and
converts any detection into a local De Bruijn–Newman margin through the pencil. On synthetic
injections it recovers `(τ, σ)` to machine precision; its measured noise floor on the actual `Ξ`
with 300 zeros is `4·10^{−4}`, which covers the entire σ-range allowed by the Polymath bound
`Λ ≤ 0.2` with two to three orders of magnitude to spare.

---

## 1. Verification of the earlier rounds

### 1.1 Round 2 §2 — all confirmed

| claim | independent result |
|---|---|
| pencil identity `e^{−t∂²}p = det(zI − X − tY)` | max relative coefficient error `2.8e−10` at `n=7` (conditioning-limited), `1.2e−15` at `n=2`; real and complex-conjugate configurations, four times each |
| `rank([X,Y] + 2I) = 1` | second singular value `< 2e−15` at `n = 3, 5, 7` |
| `Λ(p) = inf{t : spec(X+tY) ⊂ ℝ}` | reproduces `Λ(z²+y₀²) = y₀²/2` exactly at `y₀ = 0.5, 1, 2` |
| the k=2 Λ table in `ASSESSMENT` §3.2 | all five rows reproduced to 5 decimal places via the pencil (0.42976, 0.22008, 0.40825, 0.01505, 0.17482) |
| CM reduction `z̈_j = −8Σ(z_j−z_k)^{−3}` | finite-difference check, relative error `~5e−7` at `n = 3, 5, 8` |

A remark worth recording: the pencil identity is in fact a **theorem, not an observation** — the
eigenvalues of `X + tY` under the rank-one condition solve the CM second-order system (Wilson/Moser
linearisation), the heat-flow roots solve the same second-order ODE (Rodgers–Tao Thm 11 plus one
differentiation), and both trajectories share initial position `z_j` and initial velocity `Y`'s
row sums; uniqueness of the ODE gives the identity for `t` before the first collision, and
polynomial identity extends it to all `t`. So the numerical verification is confirmation of a
two-line proof, not of a conjecture.

### 1.2 Brief and Round-2 spot checks — all confirmed

`□²(−log(r²+c)) = 96c²/(r²+c)⁴` and its `16π²` normalisation: exact, symbolic. `det(D+W) ≥ det D`:
0 violations in 2000 random PSD perturbations. `ξ(1/2) = 0.49712077818831410991…`: Round 2's
correction of the brief's reference value is right, and my independently computed `4M₀` matches it
to all 20 digits checked. Mean zero gap at `T ≈ 1419`: measured 1.1541 against `2π/log(T/2π)
= 1.1592` and the brief's `4π/log T = 1.7314` — the assessment's factor-of-2 correction stands.
`Λ(normalised H_d) = −1/(2(d−1))`: confirmed at `d = 3…12` (drift `< 1%`, my bisection threshold,
not the formula). Margin-map entries `(3,0), (4,3), (6,8), (8,8), (10,12), (12,8), (16,8)`:
**all seven reproduce to 4 decimal places** from independently computed moments.

### 1.3 Not re-verified

Round 2 §5 Result 1 (flat ADHM measure → β=2 gas on the commuting locus) — plausible on standard
grounds (Hermitian diagonalisation Jacobian is the squared Vandermonde) but not recomputed.
DHKM equation-level citations — taken as checked in Round 1. Round 2 §3's literature landscape —
consistent with everything my own sweep found.

---

## 2. Two corrections to Round 2 §6.3

### 2.1 The worst case is the `n = 0` edge, not the interior dip

Round 2 §6.3(b) says every row of the margin map "dips to a minimum near `n ≈ 8–12` and recovers."
Round 2's **own table** contradicts this for `d ≥ 12`: the `n = 0` entry (0.3057 at `d=12`, 0.2063
at `d=16`) is below the interior dip (0.3340, 0.2521). The §6.3(c) "min_n" column silently used the
interior dip. The true minimum over `n ≥ 0` sits at the `n = 0` boundary for all `d ≥ 12`, i.e. in
the low-`n`, high-`d` corner — which is also where the GORZ theorem gives least, so the map agrees
with the expected geography of the problem rather than revising it.

### 2.2 The `−2/d²` law is not the edge law; the edge is `~d^{−3}`-ish and still steepening

Recomputed `Λ(normalised J^{d,0})` at 120 digits of moment precision up to `d = 40`:

| d | Λ_norm | d²·\|Λ\| | local log-log slope |
|---|---|---|---|
| 8 | −0.034841 | 2.230 | −2.001 |
| 16 | −0.006877 | 1.760 | −2.445 |
| 24 | −0.002378 | 1.370 | −2.672 |
| 32 | −0.001071 | 1.097 | −2.805 |
| 40 | −0.000564 | 0.903 | −2.891 |

`d²|Λ|` does not saturate at 4.03/2 — it decays. The local slope steepens monotonically toward −3
with shrinking increments (0.27, 0.18, 0.13, 0.10, 0.075, 0.059, 0.047 per 4 steps of `d`),
consistent with convergence to a `d^{−3}` law and **inconsistent with exponential decay** (which
would steepen the log-log slope linearly in `d`). So Round 2's headline conclusion — polynomial,
no cliff, uniformity gap quantifiable — survives, but the exponent is wrong and the "saturation at
4.03" is an artifact. The item ranked #2 in Round 2 §8 should target the `n = 0` edge and the
exponent 3 (or whatever the GORZ asymptotic actually yields there), not `−2/d²`.

### 2.3 Novelty check on the pencil (Round 2 §8 item 1)

Searched: Hall–Ho, *The heat flow conjecture for polynomials and random matrices*, Lett. Math.
Phys. (2025) — states the transport conjecture, does **not** contain the pencil identity.
Jalowy–Kabluchko(–et al.) heat-flow papers (arXiv:2308.11685 and successors) — PDE/transport
viewpoint, no pencil. Marcus–Spielman–Srivastava finite free probability gives the identity **in
expectation** (`E det(zI − A − G_t)` = heat-flowed characteristic polynomial for Gaussian `G_t`);
Round 2's identity is the deterministic derandomisation with the specific CM matrix. The closest
prior work is Kasman, *Bispectral KP solutions and linearization of Calogero–Moser* (CMP 172,
1995) and Wilson 1998, which have the linearisation but not the heat-flow reading. Verdict
unchanged from Round 2, now with a searched basis: **plausibly unstated in the literature, worth a
short note, check Kasman §linearisation before claiming it.**

---

## 3. The detector — what was asked for, built and tested

The request: a tool that could *diagnose off-axis zeros* and open a genuinely geometric approach.
The instrument below is assembled entirely from parts the three rounds validated: the Hadamard
product (Round 1's product object, minus the gauge theory), the CM velocity field (Round 2's flow),
and the pencil (Round 2's margin machinery).

### 3.1 Principle: the zeros' Coulomb field, measured on the axis

For the even, order-1, genus-1 function `Ξ` with zero multiset `{±ρ_k}`, at any simple real zero
`γ_j`:

> `V_j ≡ Ξ''(γ_j)/Ξ'(γ_j) = Σ_{ρ ≠ γ_j} 2/(γ_j − ρ)`  — the sum over **all** zeros, hidden ones
> included.

The left side is measurable to arbitrary precision from `Ξ` alone; the right side is the CM/heat
velocity, i.e. the 2D Coulomb field of the full zero gas evaluated at `γ_j`. Define the residual

> `R_j = V_j − Σ_{visible} 2/(γ_j − γ_k) − tail_j`

with the tail estimated from the Riemann–von Mangoldt density. If the visible list is complete,
`R ≡ 0`. A hidden off-axis quadruple `±(τ ± iσ)` contributes the **smooth, localised** field
`4(x−τ)/((x−τ)² + σ²)` — a Lorentzian dipole; the competing hypothesis, an unresolved on-axis pair
`τ ± a`, contributes `2/(x−τ−a) + 2/(x−τ+a)`. Both have the same monopole `4/(x−τ)`, but the next
multipole has **opposite sign**:

> off-axis: `4/(x−τ) − 4σ²/(x−τ)³`  versus  on-axis pair: `4/(x−τ) + 4a²/(x−τ)³`.

This is the electrostatics of the situation: the hidden charge's second moment enters the on-axis
field with a sign that records whether the displacement is perpendicular or parallel to the axis.
**The sign of the quadrupole coefficient is a clean off-axis discriminant**, and fitting the exact
two-parameter models recovers `(τ, σ)` or `(τ, a)`.

### 3.2 Test results

**Synthetic injection** (80 true ordinates; zeros #45–46 replaced by a hidden configuration at
their midpoint; detector sees only the remaining real zeros):

| hidden truth | OFF-model fit | PAIR-model fit | verdict |
|---|---|---|---|
| quadruple `σ = 0.8` | `τ` exact, `σ = 0.8000`, rms `2e−16` | rms `1.6e−2` | OFF-AXIS ✓ |
| quadruple `σ = 0.2` | `τ` exact, `σ = 0.2000`, rms `2e−16` | rms `1.1e−3` | OFF-AXIS ✓ |
| real pair `a = 0.3` | rms `2.4e−3` | `τ` exact, `a = 0.3000`, rms `2e−14` | ON-AXIS ✓ |
| real pair `a = 0.9` | rms `2.3e−2` | `τ` exact, `a = 0.9000`, rms `1e−16` | ON-AXIS ✓ |
| nothing hidden | `R ≡ 0` identically | — | NULL ✓ |

Model discrimination ratios are `10^{−12}` or better on noiseless data; the near-field shape
matches the Lorentzian-dipole prediction to all printed digits.

**Null test on the actual `Ξ`** (`V_j` from `mpmath` derivatives of `ξ(1/2+iz)` at 30 dps; visible
sum over the first 300 zeros; smooth RvM tail):

| `γ_j` | `V_j` measured | predicted | residual |
|---|---|---|---|
| 103.73 | −2.114262 | −2.114431 | `+1.7e−4` |
| 146.00 | −2.544240 | −2.544487 | `+2.5e−4` |
| 202.49 | −1.380817 | −1.381187 | `+3.7e−4` |

The residual is small, systematic (positive, growing toward the truncation point — clearly
tail-model error, reducible with a second-order density or larger `K`), and defines the noise
floor: `~4e−4` with `K = 300`. Against it, the *smallest distinguishable* hidden `σ` at
measurement distance `d` scales as `(noise·d³/4)^{1/2}`: **σ_min ≈ 0.03 at `d = 2`, ≈ 0.11 at
`d = 5`.** Since Polymath's `Λ ≤ 0.2` already confines any off-axis zero to `σ ≤ √(2Λ) ≈ 0.66`
(up to interaction corrections), the detector's sensitive band covers the entire allowed range
with large margin — and the floor drops further with more visible zeros and better tail modelling.

### 3.3 The pencil as the margin meter

The same local data feeds Round 2's pencil, giving the detector a second, quantitative output.
Sliding 15-zero windows over the first 80 zeros: the local backward collision time `β` tracks the
Lehmer-pair heuristic `min-gap²/8` but includes the environment exactly (e.g. window #21–35:
`β = −0.0915` against naive 0.0893). With an injected quadruple, the local forward Λ is the
interaction-corrected version of `σ²/2`:

| injected σ | local Λ (pencil) | naive `σ²/2` |
|---|---|---|
| 0.2 | 0.01971 | 0.02000 |
| 0.5 | 0.11487 | 0.12500 |
| 0.8 | 0.26350 | 0.32000 |

This is exactly the correction the `ASSESSMENT` §3.2 table showed the size dictionary could not
express, now computed rather than merely exhibited. A detection therefore converts directly into a
certified-style local lower bound on Λ — the quantitative bridge to Csordas–Smith–Varga (Constr.
Approx. 1994), whose Lehmer-pair machinery is the on-axis dual of the same statement.

### 3.4 Honest positioning

What this is: a **local, localising, quantitative** diagnostic. Turing's method — the existing
technology behind every RH verification — certifies completeness by *counting* (argument principle
against `N(T)`) and reports only "a zero is missing somewhere below `T`"; it cannot say where, or
whether the miss is off-axis, and it produces no margin. The velocity-residual detector localises
`τ`, estimates `σ`, distinguishes off-axis from unresolved-pair with a sign, and outputs a local Λ
margin through the pencil. Its inputs (`Ξ''/Ξ'` at zeros) are computable wherever zeros are
computable, and nothing in §3.1 is specific to `ζ` — it works verbatim for any L-function in the
Selberg class with an even completed form, which is where verification is thinnest and a suspicious
region most likely to arise.

What this is not: a proof route. Turning the prototype into a *certificate* requires interval
arithmetic on `V_j` and a rigorous tail bound (the fluctuating part of the tail is controlled by
known explicit bounds on `S(u)`); that is engineering, not a new idea. And detecting off-axis zeros
that are *not there* proves nothing — the instrument's value is (i) as verification infrastructure,
(ii) as the concrete realisation of the geometric reading the three rounds converged on: the zeros
as a 2D Coulomb gas whose on-axis field is exactly measurable, with hidden charge an inverse-source
problem that is *solvable* because perpendicular displacement carries a signed multipole signature.

### 3.5 Relation to the arithmetic boundary

The three-line convergence of Rounds 1–2 (circularity, lossiness, equilibrium-vs-deviation) is
unchallenged by anything here — reinforced, in fact: the detector works precisely because it
consumes the *analytic* structure (Hadamard product, heat flow, potential theory) and never
pretends to supply the arithmetic. It measures where zeros are; it cannot say where they must be.
The missing ingredient remains arithmetic. The detector is the best available use of the geometry
short of that ingredient.

---

## 4. Revised priority list

1. **Harden and write up the detector (§3).** Rigorous tail bounds (explicit `S(u)` estimates,
   interval arithmetic), the multipole sign discriminant as a lemma, the CSV bridge, and the
   L-function generalisation. This is the publishable "new tool" the project was looking for:
   modest but real, novel as far as searched (localisation + sign discriminant + margin meter;
   existing verification technology has none of the three), and useful to people who verify GRH
   numerically. Effort: weeks.
2. **The `n = 0` edge law (§2.2), replacing Round 2's item 2.** Extend past `d = 40`, stabilise the
   exponent, then attempt the derivation from the GORZ asymptotic *at the boundary column* with
   effective errors. The corrected target is `Λ(J^{d,0})` decay; the `−2/d²` interior fit was
   aimed at the wrong column. Effort: weeks.
3. **The pencil note (Round 2 item 1), unchanged**, now with the ODE-uniqueness proof of §1.1 and
   the searched novelty basis of §2.3. Effort: days.
4. **Unchanged do-not-pursue list** (Round 2 §8 item 4), with one addition: do not pursue the
   interior `−2/d²` fit.

## 5. Errors found this round, summarised

Round 2 §6.3(b): worst case wrongly placed at the interior dip (`n ≈ 8–12`); it is at `n = 0` for
`d ≥ 12` by Round 2's own table. Round 2 §6.3(c): `d·min → 4.03` saturation and the `−2/d²` law are
artifacts of the same exclusion; edge slope is `→ −3`-ish and unconverged at `d = 40`. Both
corrections strengthen rather than weaken the qualitative conclusion (polynomial, no cliff).
No errors found in Round 2 §2 (pencil), §5 (GUE, unverified but standard), or in any checked claim
of the `ASSESSMENT`; the `ASSESSMENT`'s own corrections to the brief (gap constant, `ξ(1/2)`,
Newman attribution, k=2 failure of `Λ = ρ²`) all confirm.

## 6. Sources for this round

Hall–Ho, *The heat flow conjecture for polynomials and random matrices*, Lett. Math. Phys. (2025).
Jalowy et al., *Zeros of random polynomials undergoing the heat flow*, arXiv:2308.11685.
Marcus–Spielman–Srivastava, *Finite free convolutions of polynomials*, arXiv:1504.00350 / PTRF 2022.
Kasman, *Bispectral KP solutions and linearization of Calogero–Moser particle systems*, CMP 172 (1995).
Csordas–Smith–Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann
Hypothesis*, Constr. Approx. 10 (1994). Stopple, *Lehmer pairs revisited*, arXiv:1508.05870.
Rodgers–Tao, arXiv:1801.05914. Booker, *Turing and the Riemann hypothesis*, Notices AMS (2006);
Booker, *Artin's conjecture, Turing's method, and the Riemann hypothesis*, Exp. Math. 15 (2006).

## 7. Status of every new claim

**Proved here.** The pencil identity's ODE-uniqueness proof sketch (§1.1). The opposite-sign
multipole expansion (§3.1; two lines of Taylor expansion). The velocity identity `V_j = Σ 2/(γ_j−ρ)`
(partial fractions of the genus-1 even Hadamard product).

**Measured.** Everything in the §1 tables; the §2.2 edge table (120-dps moments, `d ≤ 40`); all §3.2
and §3.3 tables. Machine noise floors as stated.

**Estimated, not rigorous.** The RvM smooth tail and hence the `4e−4` noise floor; the
`σ_min ~ (noise·d³/4)^{1/2}` scaling (order-of-magnitude); the `d^{−3}` edge exponent (unconverged
at `d = 40`).

**Not done.** Interval-arithmetic certification of `R_j`; the fluctuating-tail bound via explicit
`S(u)` estimates; the GORZ derivation at the `n = 0` edge; extension of the detector to any actual
L-function beyond `ζ`; Kasman/Wilson check before claiming pencil novelty.

## 8. Reproduction

| script | produces |
|---|---|
| `v1_pencil.py` | §1.1 — pencil identity, rank-one, Λ-via-pencil, k=2 table, CM reduction |
| `v2_spot.py` | §1.2 — biharmonic identities, `det(D+W)`, `ξ(1/2)`, gap constant, Hermite benchmark |
| `v3_margin.py` | §1.2 — moment recomputation, margin-map spot checks |
| `v4_edge.py` | §2.2 — the `n = 0` edge to `d = 40` at 120 dps |
| `d1_synthetic.py` | §3.2 — injection test, multipole fit, near-field shape |
| `d2_modelfit.py` | §3.2 — exact model comparison (the working discriminator) |
| `d3_nulltest.py` | §3.2 — null test on actual `Ξ`, noise floor |
| `d4_margin_meter.py` | §3.3 — sliding-window β, injected-quadruple local Λ |

Dependencies: `numpy`, `scipy`, `sympy`, `mpmath`. Zero caches: `zeros80.json`, `zeros301.json`.
