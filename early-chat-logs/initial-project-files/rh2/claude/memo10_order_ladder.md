# The Order Ladder Upstairs, and the Graded Laguerre Hierarchy Run

*Working memo #10 — August 23, 2026. Follows memo 9. Closes the two literature gaps memo 9 flagged, translates memo 9's transverse jet into the twistor coordinates of `twistor_lift_computation.md`, runs `twistor_lift` §5a/§7-step-1 for the first time, and applies the cheapest available screen to the obstruction route. Certified by `lab_q_normal_form.py`, `lab_laguerre_grade{,2,3}.py`, `lab_obstruction_groups.py`; literature claims flagged individually.*

---

## 0. Result

**Four things, of which the first moves the target.**

**(1) The ambitwistor ladder is known order by order, and our discriminant is at the wrong rung.** Buchdahl (1985) and Eastwood (1987) settle what memo 9 §4 could not find:

| step | what it imposes |
|---|---|
| bundle on `A` itself | a generic analytic connection — **no field equations** |
| `A → A⁽¹⁾` | **unobstructed but NOT unique** — spurious extra data at first order |
| `A⁽¹⁾ → A⁽²⁾` | **unobstructed and RIGID** — a unique distinguished first-order extension admitting a unique second; abelian case `H¹(A⁽²⁾,O) ≅` potentials exactly |
| `A⁽²⁾ → A⁽³⁾` | **obstructed: the obstruction IS the Yang–Mills current** `J` |
| beyond | abelian: nothing further (once `J = 0`, all orders free). Non-abelian: at most `N²` obstructions for rank `N` — their identification unread |

So in the ambitwistor correspondence, **order 2 is where rigidity lives and order 3 is where the equation lives.** Memo 9 proved our discriminant appears at transverse order exactly 2. That now reads as a diagnosis rather than a coincidence: *we have been building objects whose information sits at the rigidity rung, not the equation rung.* If the goal is an obstruction (a theorem) rather than imposed data, the target is one rung higher.

Sharper, and the reason to take the parallel seriously rather than as numerology: Buchdahl localises the **curvature** to the second formal neighbourhood of `Q_x ≅ P¹ × P¹` — the quadric of null rays through a spacetime point — while the **current** is the third-order obstruction on `A`. Our discriminant is second-order normal data on the incidence quadric `Q ≅ P¹ × P¹`. Same order, same surface, same rung. It is the curvature slot.

**(2) Memo 9's transverse Hessian is the Fubini–Study metric on the sphere of complex structures.** In `twistor_lift` coordinates a slice `Π_e` is a **Ruling-B line** `{w = w₀}`, whose normal direction in `Q` is one *complex* dimension — memo 9's two real transverse directions. And

```
nu^2  =  r^2 - t^2  =  y^2 sin^2(theta)  =  4 y^2 g_FS(dw, dw) + O(|dw|^4).
```

So the Hessian is a **positive Hermitian form on the normal bundle of a Ruling-B line**, a real multiple of the round metric, and the isotropy memo 9 observed numerically is nothing but the `U(1)`-invariance of that metric. Verified: ratio to the closed form `→ 1.000002` at `|dw| = 10⁻³` across several base points, phase-spread `~10⁻⁶` at `|dw| = 10⁻²`.

**(3) A new no-go, sharpening memo 9 §6: the σ-type invariant is not jet-detectable at any order.** `ρ` acts *antipodally* on the `w`-sphere (`η(−1/w̄) = −η(w)`, verified to `2.3e−16`), so it maps the Ruling-B line `{w = w₀}` to `{w = −1/w̄₀}`, whose complex structure is exactly antipodal — inner product `−1.000000` in every case tested. Hence **no slice is `ρ`-real**, and since the σ-type invariant is a statement about how `ρ` permutes **Ruling-A** components, no finite-order jet along a single Ruling-B line can see it: `ρ` moves the base line to a line at *finite* distance, which no jet reaches.

This does not contradict memo 9's order-2 collapse, and the contrast is instructive. Two different mechanisms were in play:

- **matching + globally real data** (memo 9): the ADHM blocks are real symmetric by hypothesis, so reality is imposed *globally* and a local order-2 jet condition suffices to collapse it. Local.
- **σ-type of divisor components** (`twistor_lift` §3): intrinsically a statement about a point *and its `ρ`-image*, which lie on antipodal Ruling-B lines. **Not local, at any order.**

So a thickened slice can never deliver the σ-type invariant. If §7.2 is pursued, the object is forced to be the antipodal **pair** of Ruling-B lines with their jets — which is at least not slice-statable, so it clears screen 1 by construction.

**(4) The graded Laguerre hierarchy, run for the first time — a good instrument, not a route.** `twistor_lift` §7 lists this as step 1 and it had never been executed. Headline findings:

- **`L₁` detects the memo-5 quartic** (`min_x L₁ = −4.52e−06`), whose value is exactly `f(a)² · (−2/y₀²)` — checked against the closed form to three digits. Since that quartic *passes* Newton/first-Turán (`Σρ² = 1.1298 > 0`), **the classical Laguerre inequality is strictly stronger than Turán on the standard test set.** New calibration point for brief §9.2.
- **The hierarchy is graded by sphere radius.** With a fixed real background at `±1, ±2, ±3, ±4` and one implanted pair of radius `y₀`, the first index `n` with `L_n < 0` is monotone in `y₀`: `y₀ ≤ 0.5 → n = 1`; `0.9 → 2`; `1.5 → 3`; `3.0 → 5`; `6.0 → 7`; `≥ 12 → 8`. The crossover sits where `y₀` passes the nearest-real-root distance. This is exactly the behaviour `twistor_lift` §5a predicted for the Bessel index — obtained here from the *classical* `L_n` without the Bessel machinery.
- **The pointwise moment family is incomplete; the `L_n` family is not (on everything tested).** `P_m(x) = Σ_ρ (x−ρ)^{−2m}` fails to detect any *shielded* pair — one for which some other zero is always closer to every real point — because the `m → ∞` asymptotics are governed by the nearest zero. All four shielded test cases evade `P_m` up to `m = 8`, and `(z²+1)(z²−1)` evades it entirely. `L_n` catches every one of them, at `n = 3, 5, 7, 8` for degrees `4, 6, 8, 10`.
- **Margin `∝ y₀²`, exactly.** `|min L₁|/y₀²` is constant to six digits across `y₀ ∈ [5e−4, 1e−1]`. Same exponent as memo 9's `c₂ ∝ σ²`. Brief §6.4 satisfied in sharp form, twice over by independent routes.
- **No degree-4 counterexample to completeness.** Adversarial search over non-hyperbolic quartics maximising `min_n min_x L_n` returns `9.2e−14`, attained with pair radius `1.1e−08` — i.e. the supremum is `0` and is reached only on the hyperbolic boundary. Λ ≥ 0 shape again.
- Controls clean: all five hyperbolic test polynomials and all ten Jensen truncations `J^{d,n}` (`d = 2..6`, `n = 0,1`) pass every `L_n` and every `P_m`.

**And the honest verdict on (4): it is an instrument, not a route.** See §4 — it supplies no geometry, so Proposition 1 of the brief applies at full strength.

**(5) A cheap screen on the obstruction route, with a usable number.** Modelling the order-`m` obstruction group on `Q` as `H¹(Q, End E ⊗ (N*)^m)` with `N = O(2,2)` (Q is a quadric hypersurface in `CP³`), Künneth gives `h¹(Q, O(a,b)) ≠ 0` **iff the two rulings enter with opposite signs**. Consequences: a bundle whose `End` is built from *symmetric* line bundles `O(−c,−c)` has **no obstruction at any order** — dead for free. For the asymmetric bundle the lift actually produces, `E = O ⊕ O(−d,0)` (since `Z(F̃) = Z(F) × P¹_w` has class `O(d,0)`), the group is nonzero iff `d ≥ 2m`. So **the Yang–Mills rung `m = 3` first opens at degree 6**, and the Jensen truncations `J^{d,n}` with `d ≥ 6` are the smallest for which a third-order obstruction is not excluded on dimension grounds. Below `d = 6` this route is dead without any construction being attempted. *(Caveat, stated in the script too: Buchdahl's actual obstruction lives in `H¹(X, R²_{X⁽ⁿ⁾}(End E))`, not in a plain conormal twist, so this is numerology fit for spotting a vanishing and not for claiming a nonvanishing.)*

---

## 1. The literature gaps, closed

### 1.1 Gap 1 — the order-by-order ladder

Two freely available primary sources settle it, and they agree.

**Buchdahl**, *Analysis on analytic spaces and non-self-dual Yang–Mills fields*, Trans. Amer. Math. Soc. **288** (1985) 431–469. Verbatim from the Introduction:

> "if the intersection of U with every null line in M is connected and simply connected, then (a) `E_A` extends (nonuniquely) to `U''(1)`"
> "(b) there is a unique such extension `E_A(1)` admitting a further (unique) extension to a bundle `E_A(2)` on `U''(2)`"
> "the obstruction `ω3(E_A(2))` to extending `E_A(2)` to `U''(3)` corresponds to the Yang-Mills current `J` under the transform for cohomology"

and from the abstract: "the Yang-Mills field and current are identified in terms of the Griffiths obstructions to extension, including a proof of Martin's result that 'current = obstruction to third order'." *(“Martin” is almost certainly an OCR corruption of “Manin”; the Introduction attributes exactly this to Manin, who "cast these results in an invariant form: by using the obstruction theory of Griffiths, he identified the field and current". Flagged, not proven.)*

**Eastwood**, *Supersymmetry, twistors, and the Yang–Mills equations*, Trans. Amer. Math. Soc. **301** (1987) 615–635, gives the abelian/linearised version cohomologically: with `G` the holomorphic potentials mod gauge,

> `H¹(A, O) ≅ G`. There is an exact sequence `0 → {…} → H¹(A⁽¹⁾, O) → G → 0`.
> `H¹(A⁽²⁾, O) ≅ G`.
> "For `N ≥ 3`, `H¹(A⁽ᴺ⁾, O) ≅` holomorphic source-free Maxwell fields on `M`, i.e. for which the current `J` vanishes."

So first order is onto the potentials but has a kernel of junk; **second order is where the correspondence becomes rigid**; third order is where the equation appears; and in the abelian case nothing further is imposed — third order *saturates*. In the non-abelian case Buchdahl asserts "All higher order obstructions are identified, there being at most `N²` for a bundle of rank `N`", which I could not read. **Still unconfirmed:** the identification of the ≥4th obstructions and whether they vanish automatically on YM solutions.

Buchdahl also localises the **field**: `F(∇)` corresponds to "the difference between `E_A|Q_x⁽²⁾` and the trivial extension of `E_A|Q_x` to `Q_x⁽²⁾`", where `Q_x := P(L₂) × P(T/L₂) ≅ P¹ × P¹` with neighbourhoods `Q_x⁽ⁿ⁾` cut by `I_x^{n+1}`. **Curvature = second-order data on a `P¹ × P¹`; current = third-order obstruction on `A`.** That is the sentence that makes §0(1) more than a coincidence of small integers.

Attribution chain, all as quoted in Buchdahl/Eastwood: Witten, Phys. Lett. B **77** (1978) 394–398; Green–Isenberg–Yasskin, Phys. Lett. B **78** (1978) 462–464; Manin, *Gauge fields and holomorphic geometry*, J. Soviet Math. **21** (1983) 465–507; R. Pool, *Yang–Mills fields and extension theory*, Mem. Amer. Math. Soc. **358** (1987), 63 pp. — "used explicit power series calculations to obtain the same results", its §V being "Extensions of bundles over `A`" (paywalled, unread, and the single most likely place for a cleaner order-by-order statement than the above).

For calibration, the gravitational ladder runs further: fifth-order neighbourhoods ⟺ Bach-flat, sixth order (algebraically general) ⟺ conformally Einstein (LeBrun, *Thickenings and conformal gravity*, Comm. Math. Phys. **139** (1991) 1–43, via the Atiyah–Dunajski–Mason review). Order is a genuinely discriminating invariant in this literature.

### 1.2 Gap 2 — Eastwood–LeBrun, and the `N ↔ order` dictionary

Citation confirmed: M. G. Eastwood and C. R. LeBrun, *Thickenings and supersymmetric extensions of complex manifolds*, Amer. J. Math. **108** (1986) no. 5, 1177–1192. **The paper itself remains unread** (JSTOR/MUSE inaccessible, no preprint, nothing on LeBrun's own page).

**The dictionary is `n ↔ N`, not `n ↔ 2N`** — established from Eastwood 1987, which cites EL86 for the machinery. Verbatim:

> "Superambitwistor space of order `N` as introduced by Witten involves adjoining `2N` extra anticommuting variables."
> "Since `ξ_j` and `ψ_j` are anticommuting variables, it follows that `(ξ_j ψ_j)^{N+1} = 0`. Therefore there is a map `A[N] → A⁽ᴺ⁾` defined by `X = 2 ξ_j ψ_j`."

So the even nilpotent is the *quadratic* `X = 2ξ·ψ`, nilpotent of order exactly `N+1`, and the `N`-extended super ambitwistor space maps onto the order-`N` thickening. `N = 3 ↔` third order, consistent with the ADM sentence quoted in memo 9 §4.

**Not every thickening comes from a supermanifold** — confirmed via Bettadapura, *Obstructed thickenings and supermanifolds*, arXiv:1608.07810 (J. Geom. Phys. **139** (2019) 25–49): "The obstructed thickenings will never give rise to a supermanifold whereas the unobstructed thickenings may or may not." His Theorem 3.17, attributed to EL86 p. 1188, gives the obstruction to a first-order extension of an order-`m` thickening as `H²(M, T_M ⊗ ∧^{m+1}E)` for `m` odd and `H²(M, ∧^{m+1}E ⊗ E^∨)` for `m` even.

**Whether EL86 says anything about real structures or equivariance: unknown.** Not negative — unread.

### 1.3 Gap 3 — equivariant thickenings under a free antiholomorphic involution

**A genuine gap.** No literature was found on thickenings or formal neighbourhoods equivariant for an antiholomorphic involution, free or otherwise; the thickening literature (Eastwood–LeBrun, LeBrun, Manin school, Sämann, Bettadapura) is uniformly holomorphic-category. Two candidate hiding places remain unchecked because paywalled: LeBrun's *Thickenings and gauge fields* (CQG **3** (1986) 1039–1059) and *Thickenings and conformal gravity*.

What exists is adjacent and closer than expected:

- **The CR route is the de facto real substitute.** Mason–Skinner replace the holomorphic third-order thickening by "a smooth bundle `E` over `PT × PT*` with smooth `∂̄`-operator satisfying `∂̄_a² = O((Z·W)⁴)` at `A`". Borsten–Jurčo–Kim–Macrelli–Sämann–Wolf, *Ambitwistor Yang–Mills theory revisited*, arXiv:2408.16727, push this to a **CR ambitwistor space `L := R⁴ × CP¹ × CP¹`** whose reality `τ` acts by the **antipodal (hence fixed-point-free) map on each `CP¹`**, with an "augmented CR ambitwistor space" playing the role of the thickening — explicitly "without invoking higher formal neighborhoods". That is structurally very close to `(Q, ρ)`: our `ρ = (conjugation) × (antipodal)` is the mixed variant of their `(antipodal) × (antipodal)`, free for the same reason.
- **Buchdahl's `Q_x⁽ⁿ⁾` is literally "`P¹ × P¹` with jets"** — the working object of the ambitwistor correspondence already is our surface with normal jets. What is missing in the literature is only the `ρ`-equivariant version.
- **LeBrun's twistor CR manifolds, citation now pinned:** C. R. LeBrun, *Twistor CR manifolds and three-dimensional conformal geometry*, Trans. Amer. Math. Soc. **284** (1984) no. 2, 601–616 (verified against the free AMS PDF; the *J. Diff. Geom.* attributions floating in recent arXiv papers are extraction noise). It defines an **anti-CR involution `ρ` acting without fixed points** — the antipodal map on the `S²` fibres — which is the closest published instance of the structure §0(3) needs. Also relevant and confirmed: LeBrun, *The first formal neighbourhood of ambitwistor space for curved space-time*, Lett. Math. Phys. **6** (1982) 345–354.
- **Descent framing.** `ρ = conj × antipodal` exhibits `P¹ × P¹` as the complexification of a product of an isotropic and an anisotropic real conic, so the real form has **no real points** and the `ρ`-equivariant category is Galois descent to it. Textbook real algebraic geometry; not carried over to formal neighbourhoods of a swapped divisor anywhere I could find.

## 2. The transverse jet, in twistor coordinates

Conventions from `twistor_lift` §1–2: `η(w) = (w+j)^{-1} i (w+j)`, a point of `Q = P¹_ζ × P¹_w` with `ζ = x + iy` is `q = x + y·η(w)`, Ruling A is `ζ = const` (the lift of the sphere `S_ζ`), Ruling B is `w = const` (a full slice with its complex structure fixed), and `ρ(ζ,w) = (ζ̄, −1/w̄)`.

**A slice is a Ruling-B line.** `Π_e = {w = w₀}` with `η(w₀) = e`. Then `Im q = y η(w)`, so `r = |y|` and `t = ⟨Im q, e⟩ = y⟨η(w), η(w₀)⟩ = y cos θ`, giving

```
nu^2 = r^2 - t^2 = y^2 sin^2(theta).
```

`η` is the standard stereographic chart — verified, including the chordal identity `sin²(θ/2) = |w−v|²/((1+|w|²)(1+|v|²))` to `3.3e−16` over 200 random pairs. Expanding at `w = w₀`,

```
nu^2 = 4 y^2 |dw|^2 / (1 + |w_0|^2)^2 + O(|dw|^4),
```

which is `4y²` times the Fubini–Study metric. Measured ratios to this closed form: `0.999998`, `1.000277`, `0.999207` at `|dw| = 10⁻³` for base points `w₀ = 0, 0.4−0.9i, 1.7+0.6i`, converging as `|dw| → 0`. Phase-spread of `ν²` over 12 directions: `1.1e−16` at `w₀ = 0` (exact, by symmetry) and `1.3e−06` at `w₀ = 0.4−0.9i` with `|dw| = 10⁻²`, i.e. `O(|dw|³)` as it must be.

**Therefore:** memo 9's `c₂` is the coefficient of a positive Hermitian form on the normal bundle of a Ruling-B line, and "second transverse jet along a slice" = "second-order normal data along a Ruling-B line of `Q`". The rank-2 isotropy is the `U(1)`-invariance of the round metric on the sphere of complex structures — the same `2` as the `−(2/r)B` Vekua trace term, now identified as a complex dimension rather than a coincidence.

**And no slice is real.** `η(−1/w̄) = −η(w)` to `2.3e−16`; the base and image Ruling-B lines carry exactly antipodal complex structures (inner product `−1.000000` at every `w₀` tested); `w₀ = −1/w̄₀` would need `|w₀|² = −1`. Ruling-A lines, by contrast, satisfy `ρ(L_ζ) = L_ζ̄` and are invariant exactly when `ζ` is real — which *is* the σ-type invariant. Hence §0(3).

## 3. The graded Laguerre hierarchy

Definitions as in `twistor_lift` §5a:

```
L_n(f)(x) = sum_{j=0}^{2n} (-1)^{n+j} f^(j)(x) f^(2n-j)(x) / ( j! (2n-j)! ) ,     L_1 = f'^2 - f f'' ,
P_m(x)    = sum_rho (x - rho)^{-2m} .
```

`P_1 = L_1/f²`. For a monic polynomial of degree `d`, `L_n` is nontrivial only for `n ≤ d`, and `L_d = 1` identically, so the family is finite: `n = 1, …, d−1` carry the content.

All roots normalised to `max|ρ| = 1` (brief §9.1). Full tables in `lab_laguerre_grade*_RESULTS`; the summary:

| set | outcome |
|---|---|
| 5 hyperbolic controls | no detection at any `n ≤ d` or `m ≤ 8`, as required |
| 7 standard non-hyperbolic (brief §9.2) | `L_n` detects all: `n = 1` for six of them, `n = 2` for `(z²+1)(z²−1)`. `P_m` detects all but `(z²+1)(z²−1)` |
| 4 shielded non-hyperbolic (new) | `L_n` detects all, at `n = 3, 5, 7, 8` (degrees `4, 6, 8, 10`). `P_m` detects **none** up to `m = 8` |
| 10 Jensen truncations of `Ξ` | pass everything |

Three findings worth keeping.

**(i) `L₁ >` Turán.** The memo-5 quartic `X⁴+10X³+26X²+22X+3` has `Σρ² = 1.1298 > 0` (passes Newton/first-Turán, which is why brief §9.2 calls it the single most useful test) and `min_x L₁ = −4.52e−06 < 0`. The value is not a numerical accident: at `x = a = −0.254256` the pair contributes `−2/y₀²` to `P₁` and `f(a)² = 1.760e−10`, giving `L₁(a) = −4.52e−06` — matching to every digit reported. So the Laguerre inequality is a strictly finer instrument than Turán on this set, and any future discriminant should now be asked to beat `L₁`, not `Turán`.

**(ii) The index grades by sphere radius.** Fixed real background `±1, ±2, ±3, ±4`, one implanted pair of radius `y₀`:

| `y₀` | 0.01 | 0.05 | 0.20 | 0.50 | 0.90 | 1.50 | 3.0 | 6.0 | 12 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|
| first `n` with `L_n < 0` | 1 | 1 | 1 | 1 | 2 | 3 | 5 | 7 | 8 | 8 |

Monotone, with the `n = 1 → 2` crossover where `y₀` passes the nearest-real-root distance. That is precisely the role `twistor_lift` §5a hoped the Bessel index `ℓ` would play (`j_ℓ(λ y₀) = O((λ y₀)^ℓ)`), and it is already present in the classical family. **A practical consequence: a hierarchy truncated at low `n` is blind to large spheres, and one truncated at high `n` is blind to small ones.** Any single-index test is therefore radius-selective, which is worth knowing before designing one.

**(iii) Pointwise grading is defeated by shielding; the differential grading is not.** As `m → ∞`, `P_m(x)` is dominated by the nearest zero to `x`: `~2|x−z₀|^{−2m} cos(2mφ)` for a pair at angle `φ`, `~|x−ρ|^{−2m} > 0` for a real zero. So `P_m` detects a pair iff that pair is strictly nearest to *some* real point, i.e. iff `y₀ <` dist(`a`, other zeros). Construct pairs violating this — `(z²−1)(z²+100)`, pair radius 10 against real roots at distance 1 — and the whole pointwise family goes blind, confirmed to `m = 8` in four cases. `L_n` survives because it is not a pointwise evaluation of the zero measure; its high-`n` end is a Newton-type condition on high derivatives. (Sanity: for a monic quartic, `min_x L₃ = (3/4)a₃² − 2a₂` in the coefficients, which gives `−1.98` for `(z²−1)(z²+100)` — matching the computed value exactly.)

**(iv) No degree-4 counterexample to completeness.** Maximising `min_n min_x L_n` over non-hyperbolic quartics (60 Nelder–Mead starts) returns `9.19e−14`, at pair radius `1.12e−08` — the optimiser walks to the hyperbolic boundary. So the supremum of the margin over non-hyperbolic quartics is `0`, attained only in the collapse limit. Yet again the Λ ≥ 0 shape. Degree 6 (four real roots plus one pair, 40 starts) behaves identically: best margin `1.58e−12` at pair radius `1.18e−05`. In both degrees the worst index at the optimum is `n = 1`, i.e. the binding constraint is the classical Laguerre inequality itself. Hyperbolic controls under the same objective return `1.0`, `0.531`, `6.9e−04`, `3.1e−02` — all positive, as Laguerre–Pólya requires.

**(v) Margin `∝ y₀²` exactly.** Real roots at `±1, 0.3`, pair implanted at `−0.25 ± i y₀`, un-normalised:

| `y₀` | 1e−1 | 5e−2 | 2e−2 | 1e−2 | 5e−3 | 2e−3 | 1e−3 | 5e−4 |
|---|---|---|---|---|---|---|---|---|
| `|min L₁|/y₀²` | 0.5242 | 0.5301 | 0.5315 | 0.5317 | 0.5317 | 0.5317 | 0.5317 | 0.5317 |

Constant to six digits over two and a half decades: the exponent is exactly 2, matching memo 9's `c₂ ∝ σ²` from an entirely independent direction.

## 4. Screening, and why §3 is an instrument rather than a route

Running brief §8 on the `L_n` hierarchy exposes a genuine ambiguity in **screen 1** which is worth fixing, because taken literally the screen would discard the classical hierarchies — wrongly.

`L_n ≥ 0` is a condition on the **real axis**, and brief §2.6 explicitly rules out "any invariant computed from one 2-plane of data — including the real axis of a second slice". Yet `L₁` demonstrably detects non-hyperbolicity. The resolution:

> The transverse-sphere principle is a statement about **what the geometry adds**, not about **what is knowable**. The stem carries all the information — it *is* `f`. What the principle says is that passing to `H` and restricting to a slice recovers only the stem, so the *geometric* construction has contributed nothing. Conditions on the stem and its `ζ`-jets (Laguerre, Turán, Jensen) are perfectly informative about `f`; they are simply not geometric gains.

In `twistor_lift` coordinates the distinction is clean: `L_n` uses jets along **Ruling A** (the `ζ` direction, i.e. the stem's own derivatives); the transverse-sphere principle is about restriction along **Ruling B** (which slice). These are the two rulings, and the principle constrains one of them. **Screen 1 should read: "is the condition determined by the restriction of the geometric object to a Ruling-B line (a slice), or by its normal 1-jet along one? If so it carries no information."** Memo 9 supplies the 1-jet clause; this supplies the ruling clause.

With that fixed, the `L_n` hierarchy passes screens 2, 3, 5, 6 (non-deformation-invariant; degrades as `y₀²`, no uniform separation; nonlinear in `f`; no PDE class involved) — and fails the ones that matter for a *route*:

- **Screen 8 (rationality): untouched.** Same as always.
- **Proposition 1, at full strength.** The hierarchy supplies no geometry at all, so it cannot be anything but a hyperbolicity criterion factory. Its `n`-th member is a necessary condition; the family is conjecturally (Csordas–Varga, **inherited and not verified here**) equivalent to Laguerre–Pólya membership, which for `Ξ` *is* RH. Restating RH as an infinite family of inequalities is where this route begins and ends.

So the honest value of §3 is instrumental, and real: it sharpens the standard test set (`L₁ >` Turán), gives a radius-grading law for any future graded family, supplies four new shielded test cases that defeat a natural naive hierarchy, and confirms the `y₀²` degradation law a second time. It is not a proof mechanism and should not be pursued as one.

## 5. Where that leaves the harder question

Memo 9's formulation was: *is there a transform carrying `Ξ`'s data to a bundle whose second-order extension obstruction is reality of zeros?* Section 0(1) says the "second" was wrong. Revised:

> Is there a construction attaching to `Ξ` (or to its Jensen truncations `J^{d,n}`) a holomorphic bundle on the incidence quadric `Q`, such that the **third**-order Griffiths obstruction to extending it into `CP³` is nonzero exactly when `Ξ` has a non-real zero?

Three things now constrain the answer before any construction is attempted.

1. **Order 2 is the rigidity rung, not the equation rung.** Whatever is built, second-order data should be *determined* (as `A⁽²⁾` is), and the discriminating information should sit at the third-order obstruction. Memo 9 showed the matching paradigm puts everything at order 2 — which, read through the ladder, is exactly why it collapses instead of obstructing.
2. **The object cannot be a thickened single slice** (§0(3)), and by §2 it also cannot be built from a `ρ`-invariant Ruling-B line, because there are none. The forced shape is: antipodal **pair** of Ruling-B lines, or an object on `Q` itself, with `ρ`-equivariance imposed by descent to the (pointless) real form.
3. **Dimension screen, with a number.** §0(5): symmetric bundles have vanishing obstruction groups at every order; asymmetric ones of divisor degree `d` first admit a nonzero third-order group at `d = 6`. So the smallest candidate objects are the `J^{d,n}` with `d ≥ 6` — which the project already computes, and which §3 confirms are hyperbolic and pass every classical test.

**The concrete next calculation**, and it is finite: for `E = O ⊕ O(−d,0)` on `Q` built from the zero divisor of the lift `F̃ = F × id`, compute the actual Griffiths obstruction class at the third order (not just its ambient group) using Buchdahl's `R²` sheaf rather than the naive conormal twist, and determine whether it depends on `F` only through `Z(F)` as a *divisor* — because if it does, it cannot distinguish real zeros from conjugate pairs, and the route dies for exactly the reason everything else in this programme has died. That is the test to run, and the prior should be that it dies. But it is a well-posed, finite cohomological computation on `P¹ × P¹`, which is more than the programme has had to work with before.

**Unchanged, as always:** brief §6.5. Rationality is untouched by everything above, `PROGRAM_CLOSED.md` stands, and nothing here reopens it.

**Novelty status: unchecked, assume known.** §2 is stereographic projection plus a Taylor expansion. §0(3) is the observation that a product involution's fixed locus is the product of the fixed loci. §3 is a numerical run of classical inequalities (Laguerre, Newton, Csordas–Varga) — the *radius-grading* observation (ii) and the *shielding* obstruction (iii) are the only candidates for being new, and both are elementary asymptotics that someone in the Laguerre–Pólya literature has very likely written down. §0(5) is Künneth on `P¹ × P¹`. The literature statements in §1 carry their own flags; the three that matter and remain open are Pool's Memoir §V, the ≥4th-order non-abelian obstructions, and whether Eastwood–LeBrun treats real structures.

---

*Certified by: `lab_q_normal_form.py` (stereographic identity, antipodal action of `ρ`, no `ρ`-real Ruling-B line, the `ν² = 4y² g_FS` expansion and its isotropy); `lab_laguerre_grade.py` (the `L_n`/`P_m` run over hyperbolic controls, the brief §9.2 set, four new shielded cases, and the Jensen truncations); `lab_laguerre_grade2.py` (full `n` range on the shielded cases, the radius-grading table, the `y₀²` scaling law); `lab_laguerre_grade3.py` (adversarial completeness search); `lab_obstruction_groups.py` (the `h¹(Q,O(a,b))` screen, with its caveat). Literature in §1 established by a dedicated search pass; primary texts of Witten 1978, Green–Isenberg–Yasskin 1978, Pool 1987 and Eastwood–LeBrun 1986 were NOT accessible, and every statement about them is from Buchdahl, Eastwood 1987, Bettadapura, or the Atiyah–Dunajski–Mason review, which agree with one another.*
