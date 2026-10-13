# Why Λ = 0 Is Eerie, What It Actually Says, and Why It Closes the Loophole Rather Than Opening It

*Working memo #15 — August 24, 2026. Follows up a throwaway remark: that memo 11's no-go theorem lets holomorphic equations reach the **boundary** of hyperbolicity and never hyperbolicity itself, and that `Λ ≥ 0` places `Ξ` exactly on that boundary. The remark deserved the attention. It has a precise resolution, it turns out to close the theorem's one loophole rather than open it, and it yields a unification of every quantitative law this programme measured. Certified by `lab_dbn_distance.py`, `lab_jensen_margin.py`; literature flagged per item.*

---

## 0. Result

**The observation, stated properly.** Memo 11's theorem says the hyperbolic locus `H ⊂ ℂ^d` is not a complex-analytic set, so no holomorphic equation cuts it out. But `∂H` is *contained in* the analytic set `{disc = 0}` — a holomorphic equation reaches the **boundary**. And Newman's conjecture `Λ = 0` (with Rodgers–Tao's theorem `Λ ≥ 0`) says `Ξ` sits exactly on the boundary of the Laguerre–Pólya class under the De Bruijn–Newman heat flow. So: does `Ξ`'s boundary position let equations reach it after all?

**(1) No — and the reason is the substantive finding. `∂LP` has two kinds of point, and `Ξ` is on the wrong kind.**

For a polynomial, `∂H = {`hyperbolic, with a repeated root`}` — the boundary is reached by a **collision**, and collisions are exactly what `disc = 0` detects. That stratum is analytic.

`Ξ` is not there. Its zeros are simple (all computed ones, conjecturally all), and — verified here — every Jensen polynomial `J^{d,n}` for `d ≤ 14`, `n = 0,1` has `d` **distinct** real roots, with normalised minimum gap `1.00, 0.49, 0.31, 0.23, 0.18, 0.15, 0.12, …, 0.062`. So every truncation is an **interior** point of `H_d`. `Ξ` reaches `∂LP` by a different route:

> The backward-flow margin of the consecutive pair at height `T` is `≈ Δ_T²/8`, and the mean gap `Δ_T ≈ 4π/\log T → 0`. So `inf_j (`margin`_j) = 0` while **every individual margin is strictly positive**. `Ξ` is at distance zero from the non-hyperbolic region, and the distance is realised by no single pair — only in the limit `T → ∞`.

So `Ξ` is an **asymptotic** boundary point, not a collision boundary point. The analytic stratum of the boundary is the collision stratum; equations reach that one. They do not reach `Ξ`'s.

A sharp corollary of the same computation: **for every `t < 0`, `H_t` has infinitely many non-real zeros.** The pairs whose margin falls below `|t|` are those with `Δ_T < √(8|t|)`, i.e. all pairs above height `exp(4π/√(8|t|))` — a cofinite set. So the exit from `LP` at `t = 0` is not transverse; it is **infinitely degenerate**, with the "first" collision happening at height `∞` and no finite witness. That is the precise content of Tao's gloss on Newman: *"the reality of all the zeroes is destroyed by applying heat flow for even an arbitrarily small amount of time."*

**(2) Λ = 0 is not a coincidence.** It is forced by the conjunction of two facts, one of which is RH:

- `Λ ≤ 0` is RH.
- `Λ ≥ 0` follows from the zeros being *locally irregular at all heights*. An infinite arithmetic progression is an **exact** fixed point of the zero dynamics (verified: for `x_j = jΔ`, `Σ_{m≠0} 1/m = 0` by symmetry), so a perfectly regular configuration flows backwards forever. Rodgers–Tao's proof is the rigorous version: assume `Λ < 0`, then the zeros of `H_0` must be in local equilibrium — *"locally behave (on average) as if they were equally spaced in an arithmetic progression"* — contradicting Montgomery's pair correlation.
- And the *amount* of backward margin that irregularity buys is `≈ Δ²/8` with `Δ ≍ 1/\log T`, so irregularity forces `Λ ≥ 0` but **can never force `Λ > 0`**. The Lehmer-pair lower bounds satisfy `λ ≥ −1/(8g)` with `g ≍ \log² T`; they approach `0` from below and provably cannot cross it. Historically: `≥ −50`, `> −0.0991`, `> −4.379×10⁻⁶`, `> −1.14541×10⁻¹¹`, then `≥ 0`.

So `Λ = 0` is the unique value compatible with (i) all zeros real and (ii) GUE-like close pairs at every height with density growing like `\log T`. **The boundary position is a statement about zero statistics, not about hyperbolicity per se** — which is exactly why it feels like it comes from somewhere else.

**(3) The unification, and this is the payoff. Every quantitative law this programme measured is the same quadratic.** Define, for a real polynomial `p`, its DBN threshold

`Λ(p) := inf { t : H_t has only real zeros }`, where `H_t = exp(−t ∂²_z) p`,

computable in closed form. Then (`lab_dbn_distance.py`):

| quantity | law | source |
|---|---|---|
| `Λ(z² + y_0²)` | `= y_0²/2` **exactly** (verified to 10 digits, `y_0 = 2 … 0.02`) | this memo |
| Lehmer-pair bound, small-gap limit | `→ −Δ²/8` | Csordas–Smith–Varga |
| memo 9's transverse Hessian `c_2` | `∝ σ_p²` | memo 9 |
| memo 10's Laguerre margin `min_x L_1` | `∝ y_0²`, constant to six digits over 2.5 decades | memo 10 |

These are not four analogies. They are one quantity. Measured directly, with an implanted pair at radius `y_0`:

| `y_0` | `Λ(p)/y_0²` | `|min L_1|/y_0²` | `|L_1|/Λ` |
|---|---|---|---|
| 1e−1 | 0.4747 | 0.5242 | 1.1044 |
| 1e−2 | 0.49971 | 0.53167 | 1.06396 |
| 1e−3 | 0.499997 | 0.531738 | 1.063481 |

Both are exactly quadratic, and their ratio is constant — the *same* quantity up to a constant. And the constant is where they differ: **`Λ/y_0² → 1/2` universally**, independent of the other roots (measured `0.4997, 0.4999, 0.4991, 0.4998, 0.4977` across five different real backgrounds), while `|L_1|/y_0²` varies over **five orders of magnitude** with the background (`0.025` to `2177`).

> So `Λ` is the *canonical* quadratic — the collision time of the pair, determined by the pair alone to leading order — and every discriminant this programme found is a configuration-dependent multiple of it.

**Consequence for brief §6.4.** The brief lists "no uniform separation; the discriminant must degrade continuously as the sphere radius → 0" as a **consistency requirement to be checked** against `Λ ≥ 0`. It is not. It is a *description of what every such discriminant is*: a configuration-dependent multiple of the De Bruijn–Newman distance to the boundary, which is `y_0²/2`. Any proposal in this family will satisfy §6.4 automatically, and §6.4 therefore has no screening power — it should be demoted from a screen to an identity.

**(4) `Λ(p)` is a strictly better instrument than anything in the brief's toolkit.** On the standard test set plus the shielded cases (roots normalised to max modulus 1):

| `p` | `Λ(p)` | `min_x L_1` | verdict |
|---|---|---|---|
| `z²−1`, `(z−1)(z−2)`, `(z²−1)(z²−4)` (hyp) | `−0.500, −0.031, −0.034` | `+` | both correct |
| `z²+1`, `z²+z+1`, `(z²+1)(z−1)`, `(z²+1)(z²+4)`, `(z−1)((z+2)²+9)` | `+0.500, +0.375, +0.369, +0.175, +0.255` | `−` | both correct |
| memo-5 quartic | `+3.88e−05` | `−4.52e−06` | both correct |
| `(z²−1)(z²+100)` | `+0.170` | **`+0.0198`** | **`L_1` FAILS** |
| `(z²−1)(z²−4)(z²+400)` | `+0.101` | **`+5.35e−07`** | **`L_1` FAILS** |

`Λ(p) ≤ 0` iff `p` is hyperbolic, on every case — it is a *complete* signed distance, where `L_1` is only necessary and the shielded cases defeat it outright. It is of course a restatement rather than a criterion (computing `Λ` means detecting when the flowed polynomial becomes hyperbolic), but as a **measuring instrument** for calibrating proposals it dominates `L_1`, `P_m` and Turán, and it should replace them in brief §9.2.

**(5) Three things the eerie fact tells us, in increasing order of importance.**

- *It explains §6.4 mechanistically* — item (3).
- *Any certificate for `Ξ` must be zero-margin in the flow direction.* `Λ = 0` means the margin is exactly `0`. So no strict inequality with a uniform positive margin can certify `Ξ`; a working certificate must either be an equality case, or measure a direction transverse to the heat flow. That is a genuine design constraint and it is new.
- *The difficulty is localised at `T → ∞`, and every construction in this programme is finite.* The boundary-ness of `Ξ` is invisible at any finite height or degree: truncations are interior, with positive margin. Every object this programme built — charge-`k` ADHM data, degree-`d` Jensen truncations, rank-`r` lattices, order-`m` thickenings — is finite. **They are all structurally probing the part of the problem that is not hard.** This is the first criticism of the programme's method that does not come from the geometry, and I think it is the most serious one in memos 9–15.

---

## 1. The setup, verified

**Conventions** (Rodgers–Tao / Polymath15 / Newman–Wu, unanimous):

`H_t(z) := ∫_0^∞ e^{tu²} Φ(u) cos(zu) du`, with `H_0(z) = (1/8)·ξ(1/2 + iz/2)`.

Note the factor-2 rescaling: zeros of `H_0` are `x_j = 2γ_j`. Since `Λ` has units of (length)², this is a factor-4 trap in any numerical statement. Newman's theorem: there is `Λ ∈ (−∞, 1/2]` with `H_t` having only real zeros **iff** `t ≥ Λ`. RH `⟺ Λ ≤ 0`.

`e^{tu²}` as a Fourier multiplier means `∂_t H = −∂_{zz} H` — the *backward* heat equation for `H`. Despite the name, **increasing `t` is the direction that makes zeros real.** Toy check: `H_0 = z²+1 ⟹ H_t = z²+1−2t`, real iff `t ≥ 1/2`, which is exactly de Bruijn's threshold saturated by a single pair at distance 1. ⚠️ Newman's own 1976 paper uses `b = −λ`, so all his inequalities flip; the transcription of his sign conventions is internally inconsistent in the copies reachable, and should be checked against a printed page before being relied on.

**Newman's actual words** (Remark 2, p. 250, *Fourier transforms with only real zeros*, Proc. Amer. Math. Soc. **61** (1976) 245–251):

> "The Riemann hypothesis is the statement that `b₀ > 0`; we make the complementary conjecture that `b₀ < 0`. This new conjecture is a **quantitative** version of the dictum that the Riemann hypothesis, if true, is only barely so."

("quantitative", not "qualitative" — corroborated by Newman's own later survey; one OCR of the same page reads "qualitative".)

**The zero dynamics** (Rodgers–Tao eq. (5)):

`∂_t x_k(t) = 2 Σ_{j ≠ k} 1/(x_k(t) − x_j(t))`

— repulsion, inversely proportional to separation, first-order. So running `t` **downward** makes the zeros **attract**, and collisions produce conjugate pairs. `Λ ≥ 0` is exactly *"the backward flow starting from the actual zeta zeros collides immediately."*

**Gradient structure.** With `𝓗(t) = Σ_{j≠k} log(1/|x_j − x_k|)` and `E(t) = Σ_{j≠k} |x_j − x_k|^{−2}`:

`∂_t x_k = −∂𝓗/∂x_k`,  `∂_t 𝓗 = −|∇𝓗|² = −4E(t)`,

the second identity because of the Stieltjes-type identity `Σ_k (Σ_{j≠k}(x_k−x_j)^{−1})² = Σ_{j≠k}(x_j−x_k)^{−2}`. So the flow is gradient descent for the 1-D log-gas energy, `E` is simultaneously the interaction energy and the squared gradient, and `E = 0` exactly on arithmetic progressions.

**The framing this corrects.** It is tempting to read `Λ = 0` as "`Ξ` is at a critical point" or "a phase transition". It is neither: the flow is strictly dissipative at `t = 0` (`∂_t 𝓗 = −4E < 0`), and `Ξ` is not stationary. `Λ` is the **backward existence time** — the blow-up time of the backward semiflow, computed from the actual zero configuration. `Ξ` sits at the boundary of the *domain* of the backward flow, not at a critical point of anything. (No source in the literature claims a phase-transition interpretation; Newman–Wu discuss Lee–Yang zeros and Dyson Brownian motion and explicitly stop short of one.)

## 2. Why `Λ = 0`, assembled

The logical chain, with each link sourced:

1. **An arithmetic progression is an exact backward-eternal solution.** (Rodgers–Tao, footnote 2, with the `cos` example; and the elementary symmetry computation.)
2. **Backward flow requires near-equilibrium; irregularity obstructs it.** Rodgers–Tao make this rigorous: `Λ < 0 ⟹` zeros of `H_0` locally an AP `⟹` contradiction with pair correlation.
3. **Irregularity buys only `O(Δ²)` of backward time**, and `Δ ≍ 1/\log T`. Hence `Λ ≥ 0` is forced but `Λ > 0` is not obtainable from local statistics.
4. **GUE `⟹` infinitely many Lehmer pairs `⟹ Λ ≥ 0`** (Tao); Rodgers–Tao replaced the GUE hypothesis with unconditional pair-correlation input.
5. **RH `⟹ Λ ≤ 0`.**

And the asymmetry of the two bounds is itself informative: the lower bound is provably capped at `0` (`≥ −1/(8g)`, `g ≍ \log²T`), while the upper bound decays like `O(1/\log X)` in the RH verification height (Polymath15: `Λ ≤ 0.22`, unconditional, with the barrier at `γ ≈ 3×10^{10}`). **`Λ = 0` is inaccessible from both sides by any finite computation.** That is the same "finite constructions probe the easy part" point as §0(5), arriving from the numerical side.

## 3. The two kinds of boundary point

This is the resolution of the eerie feeling, stated as sharply as I can.

**Finite dimensions.** `H_d ⊂ ℝ^d` is closed with nonempty interior; `∂H_d = {`all roots real, at least two equal`}`. To leave `H_d` you must merge two real roots and split them off-axis. So every boundary point is a **collision** point, and `{disc = 0}` — a holomorphic equation — contains that stratum. This is why memo 11's theorem, while excluding an equational characterisation of `H`, does *not* exclude one of `∂H`.

**Note also that `{disc = 0} ⊋ ∂H`:** a repeated root can be a repeated *conjugate pair*, or coexist with non-real roots. Separating `∂H` from the rest of `{disc = 0}` requires the predicate "all roots real" — hyperbolicity again. So even the boundary is not cleanly characterised holomorphically; the equation reaches a set *containing* it.

**Infinite dimensions.** `LP` is closed under locally uniform limits, and closed under the semigroup `e^{−t∂²}`, `t ≥ 0`. The curve `t ↦ H_t` lies in `LP` exactly for `t ≥ Λ`, so `Λ = 0` puts `H_0 = Ξ/8` on `∂LP`. But the mechanism is **not** collision: `Ξ` has simple zeros. It is accumulation — `inf_j (`margin`_j) = 0` with every margin positive. Hence:

> **`∂LP` is stratified by how the boundary is reached.** The collision stratum is analytic and is what holomorphic equations detect. `Ξ` lies on an accumulation stratum, which is not analytic — it is a statement about the whole infinite configuration, invisible to any finite-order or finite-dimensional condition.

**So the loophole closes.** The equations reach the wrong stratum. And the closure is for a reason with the same flavour as the theorem itself: analyticity sees collisions, not limits.

## 4. The finite-dimensional shadow: measured, and honestly not found

If `Ξ`'s boundary-ness is a `T → ∞` phenomenon, the natural test is whether its Jensen truncations become "barely" hyperbolic as `d` grows. Measured (`lab_jensen_margin.py`, 60-digit moments, `d = 2 … 14`, `n = 0,1`), against the Hermite polynomial of the same degree — the `n → ∞` attractor of `J^{d,n}` by Griffin–Ono–Rolen–Zagier:

| `d` | `Ξ` min gap | Hermite min gap | ratio |
|---|---|---|---|
| 4 | 0.3139 | 0.3178 | 0.988 |
| 6 | 0.17829 | 0.18552 | 0.961 |
| 8 | 0.12359 | 0.13007 | 0.950 |
| 10 | 0.09365 | 0.09979 | 0.938 |
| 12 | 0.07468 | 0.08079 | 0.924 |
| 14 | 0.06157 | 0.06778 | 0.908 |

`Ξ`'s Jensen root gaps run **2–9% tighter** than the Hermite attractor's, consistently, with the deficit growing slowly in `d`. That is a real, reproducible measurement.

**But it does not establish a boundary shadow, and I do not want to over-read it.** Two honest caveats. First, at `n = 0,1` the truncations are nowhere near the `n → ∞` regime in which GORZ prove convergence to Hermite, so the deficit may be a finite-`n` artifact rather than a `Ξ`-specific tightness. Second, the Laguerre-margin column in the same run decays by roughly two orders of magnitude *per degree* for both `Ξ` and Hermite — a generic feature of hyperbolic polynomials with roots in a fixed range — and beyond `d ≈ 11` it falls to `10⁻²⁶` and below, where the double-precision evaluation of the margin is no longer trustworthy (it goes spuriously negative at `d = 12,13,14`). Those negatives are artifacts and should not be quoted.

**Conclusion of the experiment, which is a negative and is expected:** no `Ξ`-specific boundary shadow is detectable at `d ≤ 14`, `n ≤ 1`. That is consistent with §3 — the boundary-ness lives at `T → ∞`, and low-degree low-`n` truncations probe low heights. It also fits GORZ needing `n ≥ c e^d`: exponential depth in `n` to control degree `d`.

## 5. The literature gap, and what it points at

The one thing the search did not find: **nobody treats `∂LP` as a geometric object.** No local structure near `Ξ`, no transversality analysis of the curve `t ↦ H_t` at `t = 0`, no stratification. Given this programme's whole vocabulary — transverse rigidity, jet order, equality loci — that is the natural place to look, and §0(1) and §3 above are the first two structural facts about it:

- the exit of `t ↦ H_t` from `LP` at `t = 0` is **infinitely degenerate**, not transverse (infinitely many pairs collide for every `t < 0`);
- `∂LP` is **stratified** into a collision stratum (analytic, reachable by `disc = 0`) and accumulation strata (not analytic), with `Ξ` on the latter.

Whether that stratification is useful is open. What it does immediately is explain why memo 11's theorem has no loophole at `Ξ`, and it predicts that any construction hoping to certify `Ξ` must be sensitive to the tail of the zero sequence, not to any truncation of it.

## 6. Assessment

The remark was worth chasing. It did not open a crack in memo 11's theorem — it explained why the theorem has none, by identifying which stratum of the boundary is analytic and showing `Ξ` is not on it. Along the way it produced the one genuine unification in memos 9–15: `Λ(p) = y_0²/2` is the canonical distance to hyperbolicity, and memo 9's `c_2`, memo 10's Laguerre margin and the Lehmer-pair bound are all configuration-dependent multiples of it. That demotes brief §6.4 from a screen to an identity, and it supplies a better instrument (`Λ(p)`, a complete signed discriminant) than anything the brief's §9.2 currently uses.

The uncomfortable finding is §0(5)'s third item. Every object this programme built is finite — finite charge, finite degree, finite rank, finite order of thickening — and the difficulty in RH, as located by `Λ = 0`, is entirely in the `T → ∞` tail. That is not a statement about quaternions or twistors or positivity. It is a statement about the method, and unlike the geometric no-gos it would apply equally to a construction that cleared every screen in brief §8.

**Unconfirmed.** Newman's own sign conventions (see §1); the internal numbering and exact form of Rodgers–Tao's local-equilibrium proposition; whether their final contradiction invokes Montgomery directly or the Conrey–Ghosh–Goldston–Gonek–Heath-Brown estimate; whether Csordas–Smith–Varga's `Δ` is in `x = 2γ` units or `γ` units (a factor of 4 in `Λ`, unresolved and relevant to any numerical use of their formula); Ki–Kim–Lee's statement that for `t > 0` all but finitely many zeros of `H_t` are real. The claim in §0(1) that infinitely many pairs collide for every `t < 0` is my own inference from the gap asymptotics plus the Lehmer margin, not a quoted result, and it neglects the interaction correction `g`.

**Novelty status: assume known.** `Λ(p)` for polynomials is the obvious finite-dimensional analogue and its `y_0²/2` anchor is a two-line computation. The identification of the programme's discriminants as multiples of it is bookkeeping. The stratification remark in §3 is the only item I would guess is not written down somewhere, and I would not bet on that either.

---

*Certified by `lab_dbn_distance.py`: Part 1, the `Λ(z²+y_0²) = y_0²/2` anchor to 10 digits; Part 2, `Λ(p)` on the standard test set plus two shielded cases, with the sign agreement column showing `L_1` failing where `Λ` does not; Part 3, both `Λ` and `|min L_1|` exactly quadratic in `y_0` with constant ratio; Part 4, `Λ/y_0² → 1/2` universally across five real backgrounds while `|L_1|/y_0²` varies by five orders of magnitude. And by `lab_jensen_margin.py`: 60-digit moments, `J^{d,n}` for `d ≤ 14`, `n = 0,1`, all hyperbolic, gaps against the Hermite attractor — with the Laguerre-margin column flagged as precision-limited beyond `d ≈ 11`.*
