# Round 3: a correction, a reframing, and the novelty verdict on the pencil

**2026-08-24.** Follow-up to `ROUND2_full_YM_and_results.md`. Contains a **correction to a round-2
result**, a reinterpretation that changes what the corrected result means, and the literature
verdict on the Calogero–Moser pencil identity.

---

## 1. Correction: the margin decay exponent in round 2 §6.3 is wrong

**What I got wrong.** I reported that `min_n` of the normalised DBN margin decays like `d^{-1}`
relative to Hermite (`d^{-2}` absolute), with the log-log slope converging to `−1` and `d × min`
saturating at ≈ 4.03. That fit used the *interior* minimum of each row. But the minimum **migrates
to `n = 0` at `d ≈ 9–10`**, and for `d ≥ 10` I was reading a local dip rather than the true row
minimum. `d × min` does not saturate — it peaks at `d = 10` and turns over.

**Corrected data** (finer `n` grid, bracketing bug in the `Λ` bisection also fixed — the previous
run's first attempt returned a constant `−1/2` because a bracket `[−1, −1/2]` was used when the true
threshold lay in `(−1/2, 0)`):

| `d` | `min_n` margin | at `n` | `d × min` | `d^{3/2} × min` | local log-log slope |
|---|---|---|---|---|---|
| 4 | 0.7168 | 8 | 2.87 | 5.73 | — |
| 6 | 0.5666 | 8 | 3.40 | 8.33 | −0.580 |
| 8 | 0.4655 | 8 | 3.72 | 10.53 | −0.683 |
| 10 | 0.3819 | **0** | 3.82 | 12.08 | −0.887 |
| 12 | 0.3057 | **0** | 3.67 | 12.71 | −1.221 |
| 14 | 0.2491 | **0** | 3.49 | 13.05 | −1.328 |
| 16 | 0.2063 | **0** | 3.30 | 13.20 | −1.412 |
| 20 | 0.1471 | **0** | 2.94 | 13.16 | −1.516 |

`d^{3/2} × min` saturates at **≈ 13.2** (12.08 → 12.71 → 13.05 → 13.20 → 13.16), and the local slope
passes through `−3/2` near `d ≈ 18`. So:

> **`min_n Λ(normalised J^{d,n}) ≈ −13.2 · d^{−3/2}` relative to Hermite,
> i.e. absolute normalised margin `≈ −6.6 · d^{−5/2}`.**

Round 2 said `d^{-1}` / `d^{-2}`. The correct exponents are `3/2` and `5/2`.

**What survives.** The qualitative conclusion — **polynomial, not exponential; no cliff** — holds,
and it was the load-bearing part. But the cost is meaningfully higher than I said: certifying
hyperbolicity at degree `d` needs about `5/2` decades of margin per decade of `d`, not `2`.

**One structural observation worth flagging without overclaiming.** The crossover — interior minimum
for `d ≤ 8`, minimum at `n = 0` for `d ≥ 10` — sits exactly at the boundary of the
Griffin–Ono–Rolen–Zagier range (`d ≤ 8` proved hyperbolic for all `n`). That is consistent with how
their method is built: Hermite asymptotics control large `n`, finite checks control small `n`, and
that pairing is well matched precisely to the regime where the hard case is in the interior. I would
not call it more than suggestive.

---

## 2. The reframing: the decay is *forced*, and it is Newman's "barely" made numerical

This changes what §1 means, and I did not see it in round 2.

**The classical Jensen limit.** For `F(w) = Σ b_m w^m` with `γ(m) = m! b_m`,

`J^{d,0}(X/d) = Σ_j [d(d−1)⋯(d−j+1)/(j! d^j)] γ(j) X^j  ⟶  Σ_j b_j X^j = F(X)`.

Verified: relative error at `X = −1` falls `1.25e−5 → 4.15e−6 → 1.38e−6` for `d = 20, 60, 180`; at
`X = −60`, `5.7e−2 → 1.9e−2 → 6.1e−3`. And `F` is `Ξ` in the variable `w = −z²` — the degree-40
truncation of `F` has real roots recovering the first three zeta zeros to nine digits:

| root `w` | `√(−w)` | true `γ_n` |
|---|---|---|
| −199.7904548 | 14.13472514 | 14.13472514 |
| −441.9261506 | 21.02203964 | 21.02203964 |
| −625.5429997 | 25.01085764 | 25.01085758 |

**The consequence.** As `d → ∞` at `n = 0`, the Jensen polynomial reconstructs `Ξ` itself. And `Ξ`
sits *exactly* on the knife edge: RH gives `Λ_DBN ≤ 0`, Rodgers–Tao gives `Λ_DBN ≥ 0`, so
`RH ⟺ Λ_DBN = 0`. Therefore

> **the `n = 0` margin must decay to zero. A plateau at a positive value would contradict `Λ = 0`.**

So the decay measured in §1 is not a defect of the Jensen method and not evidence that the Pólya
route is hard for a bad reason. It is Newman's dictum — *the Riemann hypothesis, if true, is only
barely so* — appearing as a measured rate. The map is a **consistency check on `Λ_DBN = 0`, and it
passes.**

What the rate then measures is the *price of finite-`d` certificates*: how much precision in the
moments buys how much hyperbolicity margin. `d^{−5/2}` is the answer, and being polynomial it means
the price is payable in principle.

This also retires a question I raised in round 1. I asked whether the Pólya route was "closable at
all" by looking for a cliff. There is no cliff, but there is also no room: the target margin is
exactly zero, by theorem. The right question is not *whether* the margin vanishes but *how fast* —
and that is now a measured `d^{−5/2}` awaiting a derivation.

---

## 3. Novelty verdict on the pencil identity — and a real proof

### 3.1 A two-line proof (replacing the numerics)

The structural fact I had missed: **`Y` is twice the Lagrange differentiation matrix** at the nodes.
Verified: `Y = 2·S⁻¹DS` with `D_{jk} = ℓ_k'(z_j)`, `S = diag(p₀'(z_j))`, to `3e−16` at `n = 3..7`. So
`X + tY` is the matrix of the operator `z· + 2t·d/dz` on `ℂ[z]/(p₀)` (verified: characteristic
polynomials agree to `5e−14`). Then:

> `[∂², z] = 2∂`, so `e^{t∂²} z e^{−t∂²} = z + 2t∂` (the series terminates). Characteristic
> polynomials are conjugation-invariant, and multiplication-by-`z` on `ℂ[z]/(p₀)` has characteristic
> polynomial `p₀`. Hence `char(z· + 2t∂ mod p₀) = e^{−t∂²}p₀`. ∎

Nice to have a proof rather than six numerical configurations. It also explains why the diagonal of
`Y` is forced: in the integrable-systems parametrisation the diagonal is the Calogero–Moser
*momentum*, left free, and pinning it to `Y_{jj} = Σ_{k≠j} 2/(z_j − z_k)` is exactly the constraint
that makes the `t₂` flow the heat flow.

### 3.2 (B) is known — do not claim it

The identity `e^{−t∂²}p₀(z) = det(z − X − tY)` is Wilson's tau-function formula restricted to the
second time. Wilson, *Collisions of Calogero–Moser particles and an adelic Grassmannian*,
*Invent. Math.* **133** (1998) 1–41, gives `τ(t) = det(X + Σ_{i≥1} i·t_i·Z^{i−1})` for
`rank(XZ − ZX + I) = 1`; setting `t₁ = z`, `t₂ = t` and the rest to zero collapses it to the pencil.
Restated with attribution in Kasman, [arXiv:math-ph/0502012](https://arxiv.org/abs/math-ph/0502012)
§4.2; earlier linearisation in Kasman, *CMP* **172** (1995) 427
([hep-th/9412124](https://arxiv.org/abs/hep-th/9412124)); Shiota, *J. Math. Phys.* **35** (1994)
5844. Made fully explicit for heat flow in *Exceptional Hermite Polynomials and Calogero–Moser
Pairs*, [arXiv:2507.21935](https://arxiv.org/abs/2507.21935), Remark 4.2, whose Example 5.2 is
literally `τ(x,y) = x² − 2y = e^{−y∂_x²}x²`.

Pole-dynamics ancestry: Airault–McKean–Moser, *CPAM* **30** (1977) 95–148.

### 3.3 (C) appears to be unwritten — that is where the contribution sits

`Λ(p₀) = inf{ t : spec(X + tY) ⊂ ℝ }` was not found anywhere. A site-restricted arXiv search for
papers containing both "de Bruijn–Newman" and "Calogero–Moser" returns **nothing**. Checked
directly: Rodgers–Tao [1801.05914](https://arxiv.org/abs/1801.05914) contains none of *determinant,
matrix, eigenvalue, Calogero*; Polymath15 [1904.12438](https://arxiv.org/abs/1904.12438) likewise;
Tao's *Heat flow and zeroes of polynomials* posts derive the root ODE with no matrix model.
Hall–Ho [2202.09660](https://arxiv.org/abs/2202.09660) Remark 2.8 *does* note the CM equations of
motion and even the momentum constraint — and stops there, with no pencil, no rank-one condition, no
DBN.

So the two literatures are disjoint at exactly this point. The novelty is the bridge, not a hard
theorem: (C) follows from (B) in one line.

### 3.4 The mathematically interesting question the bridge exposes

There is a mature literature on hyperbolic and definite matrix pencils — Higham–Mackey–Tisseur,
Al-Ammari–Tisseur (*LAA* **436** (2012)), Niendorf–Voss (*LAA* **432** (2010)) — but it treats
Hermitian coefficient matrices and definiteness *at a point*. The question

> **for which pencils `X + tY` is the spectrum real for all `t ≥ t₀`?**

appears not to be addressed. Under (B), the Pólya–Schur/Laguerre fact that heat flow preserves
hyperbolicity becomes a non-obvious *monotonicity* statement about this specific pencil family. That
is a well-posed question in matrix analysis, independent of RH, and it is the most promising thing
the bridge produces.

For completeness, the certificate side is entirely standard: `p` real-rooted ⟺ there is `H ≻ 0` with
`HX = X*H` (i.e. `X` is `H`-self-adjoint), and `H` is the Bezoutian / Hankel matrix of Newton sums.
Hermite (1856); the definitive treatment is Krein–Naimark, *Linear and Multilinear Algebra* **10**
(1981) 265–308; also Gantmacher vol. II ch. XV, Bochnak–Coste–Roy Thm. 4.57.

**Caveat carried from the sweep:** Wilson (1998) and Kasman (1995) could not be read in full text.
Before writing anything up, read Wilson's KP-flow sections and Shiota (1994) directly.

---

## 4. Revised next steps

**1. A short note, correctly scoped.** Not "a new determinantal formula" — (B) belongs to Wilson.
The note is: *the De Bruijn–Newman threshold is the reality threshold of a linear pencil on
Calogero–Moser space*, plus the pencil-hyperbolicity question of §3.4. Cite Wilson/Kasman for the
identity, verify against the primary sources first. This is a genuine but modest contribution:
connecting two literatures that have zero overlap.

**2. Derive `min_n margin ≈ 13.2·d^{−3/2}` from the GORZ asymptotic.** Still the highest-value item,
and §2 sharpens it: this is now *the rate at which Jensen approximants approach the `Λ = 0` knife
edge*. A derivation would turn a fitted constant into a quantitative form of Newman's dictum. Before
that, extend the map to `d ≤ 40` to confirm the `3/2` exponent past the current `d = 20` — the
saturation of `d^{3/2}·min` is convincing but four points wide.

**3. The N=4 SYM bootstrap-positivity question.** Unchanged from round 2 §8.3, and still the only
live seam on the physics side.

**4. Retired.** Round 2 §8's framing of item 1 as a possibly-new identity — superseded by §3.2 here.

---

## 5. Method note

Two bugs found and fixed in my own round-2 pipeline, both worth recording because they were the kind
that produce plausible output rather than errors:

- The `Λ` bisection bracketed `[−1, −1/2]` when the initial probe at `t = −1` was non-hyperbolic,
  instead of falling back to `[−1, 0]`. Result: `Λ = −1/2` exactly for every input — caught only
  because the ratio column came out as exactly `d − 1` in every cell.
- The round-2 minimum-extraction read interior dips rather than row minima once the minimum migrated
  to `n = 0`, silently changing the fitted exponent from `3/2` to `1`.

Neither would have been caught by spot-checking individual values.

## 6. Reproduction

| script | produces |
|---|---|
| `margin2.py` | §1, corrected margin map and decay |
| `jlimit.py` | §2, the Jensen limit to `Ξ` and the zeta-zero recovery |
| `proof.py` | §3.1, `Y` as the Lagrange differentiation matrix and the operator identity |
| `pencil.py`, `cmflow.py` | round-2 verifications, unchanged |
