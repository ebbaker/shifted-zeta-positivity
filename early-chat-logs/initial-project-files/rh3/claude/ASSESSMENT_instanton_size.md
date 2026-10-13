# Independent assessment of `BRIEF_instanton_size.md`

**Reviewed 2026-08-24.** All numerical claims below were recomputed from scratch (`sympy`,
`mpmath`); nothing is taken from the brief's own lab scripts.

---

## 1. Summary of the brief

The proposal in one line: `Ξ` is naturally a *product* (Hadamard, over its zeros); the natural
product-shaped scalar in instanton theory is `det f^{-1}(x) = det(2w̄w + Σ_n(a'_n + x_n)²)`, the
ADHM determinant; match them and read off a dictionary.

The chain is:

1. **Target.** RH ⟺ `Ξ` hyperbolic ⟺ every Jensen polynomial `J^{d,n}` hyperbolic (Pólya).
2. **Two universal screens.** (§1.4) The hyperbolic locus `H ⊂ ℝ^d` is not the zero set of
   holomorphic functions on any open `U ⊆ ℂ^d` meeting `ℝ^d` — because `H` contains a nonempty
   *open* subset of the maximally totally real `ℝ^d`, so any holomorphic function vanishing on it
   vanishes identically. (§1.5) `ℂ^d` and `ℂ^d ∖ {disc = 0}` are connected, so no deformation
   invariant and no complex chamber invariant can cut out `H`. Conclusion: a detector must be a
   *non-analytic real* object that jumps across the real discriminant.
3. **Gauge side.** ADHM data `(w, a'_n)`; `f^{-1} = 2w̄w + Σ(a'_n+x_n)²` (DHKM 2.62);
   Osborn's identity `∫tr F² ∝ ∫□² tr log f`.
4. **Three exact facts.** `□²log|x| = −8π²δ` in `ℝ⁴`; at `k=1`,
   `□²(−log(r²+c)) = 96c²/(r²+c)⁴` with total `16π²` for every `c>0`; the 't Hooft factorisation
   `det f^{-1} = φ·∏|x−X_i|²` with the singularities of `logφ` exactly cancelling the point
   charges. Reading: a nonzero scale size is what turns `k` point charges into a smooth field.
5. **Dictionary.** `det f^{-1} = (x_0−X)² + r² + 2ρ²` versus the real quadratic factor
   `(x_0−τ)² + σ²` of a conjugate root pair ⟹ **`Im(zero) = √2 · (instanton size)`**.
6. **Matching rigidity (§5).** `det(D+W) ≥ det D` for `W ⪰ 0`, equality iff `W = 0`; and
   `det D(x) = 0` at real `x` iff the `a'_n` share an eigenvector. Hence `det f^{-1}` is a product
   of real quadratic factors iff `w = 0` **and** `[a'_m,a'_n] = 0`. Independent of `k` and of the
   gauge group.
7. **Verdict.** Passes the Type-A (impossibility) screens — genuinely, and that is unusual — but
   fails on Type B (circularity) *in a fatal location*: the criterion "all sizes vanish" lands on a
   **free modulus**, unconstrained precisely because `∫|F|²` is conformally invariant in `d=4`. The
   only mechanism that makes the size determinate — noncommutative deformation — gives
   `|w|² ≥ |ζ⃗|`, i.e. **bounds the size away from zero**, forcing non-real zeros rather than
   forbidding them.

---

## 2. What checks out

Recomputed independently and confirmed:

| claim | status |
|---|---|
| `□ log r = 2/r²`, `□²log r = 0` away from `0`, `□²log|x| = −8π²δ` | ✅ exact |
| `□²(−log(r²+c)) = 96c²/(r²+c)⁴` | ✅ exact (symbolic) |
| `∫_{ℝ⁴} 96c²/(r²+c)⁴ = 16π²` for **every** `c > 0` | ✅ exact (symbolic, not numeric) |
| `det(D+W) ≥ det D`, `W ⪰ 0`, `D ≻ 0`; equality iff `W = 0` | ✅ 0 violations / 8000 random samples; the proof is right and in fact gives equality-at-one-point ⟹ `W=0`, stronger than stated |
| real roots of `det D` = simultaneous eigenvalues of `a'_n` | ✅ `det D ~ 1e−15` at each simultaneous eigenvalue |
| non-commuting positions ⟹ no real roots | ✅ `min det D ≈ 4.9e+02` over 4000 random `x` at `k=3` |
| `Λ(z² + y₀²) = y₀²/2` | ✅ exact — but see §3 |
| §1.4 and §1.5 proofs | ✅ correct as written |

§5 is the strongest technical content in the brief. The proof is two lines, it is correct, and the
gauge-group-independence argument (`w` enters `f^{-1}` without `x`, so `N` only moves the constant
term) is sound. **The generalisation of matching rigidity to all `k` and all classical groups is a
real, if small, result.**

---

## 3. Errors found

### 3.1 The zero-spacing constant is wrong by a factor of 2 (§4.3)

The brief states `Δ_T ≈ 4π/log T`. Measured against actual zeta zeros:

| height `T` | measured mean gap | `2π/log(T/2π)` | brief's `4π/log T` |
|---|---|---|---|
| 236.5 | 1.6461 | 1.7318 | 2.2990 |
| 1419.4 | 1.1643 | 1.1592 | 1.7314 |
| 5447.9 | 0.9381 | 0.9288 | 1.4607 |

The correct constant is `2π/log(T/2π)`. This propagates: §4.3's `ρ_T ≈ π√2/log T` should be
`π/(√2 log T) = π√2/(2 log T)`. §4.3 is one of the three items §7 lists as surviving.

### 3.2 `Λ = ρ²` is an identity at `k=1` and **false** at `k=2` (§4.2)

The brief's table row "`Λ = ρ²`, the size squared — verified to 8 digits" is presented as a
dictionary success. It is exact at charge one for the trivial reason that a monic real quadratic is
*determined* by `(τ, σ)`, so any function of it is a function of `σ`. Extending the dictionary to
`k=2` — two instantons, sizes `σ_j/√2` — and testing `Λ = max_j σ_j²/2`:

| pairs `(τ, σ)` | measured `Λ` | dictionary prediction | ratio |
|---|---|---|---|
| `(0, 1.0), (3.0, 0.5)` | 0.42976 | 0.500 | 0.86 |
| `(0, 1.0), (0.3, 0.5)` | 0.22008 | 0.500 | 0.44 |
| `(−1, 1.0), (1.0, 1.0)` | 0.40825 | 0.500 | 0.82 |
| `(0, 0.2), (0.25, 0.2)` | 0.01505 | 0.020 | 0.75 |
| `(0, 1.0), (0.0, 0.5)` | 0.17482 | 0.500 | 0.35 |

Not approximately right; the ratio ranges over `0.35–0.86` and depends on the *separation of the
centres*, which the dictionary says is an independent modulus. **The one row of the table with
quantitative content holds only in the case where it is vacuous.**

### 3.3 Misattribution (§4.2)

"Newman's conjecture `Λ = 0`" — Newman conjectured `Λ ≥ 0`, which is now the Rodgers–Tao theorem
(*Forum of Mathematics Pi*, 2020). RH ⟺ `Λ ≤ 0`. The two together give `RH ⟺ Λ = 0`, but that
equality is not Newman's conjecture.

### 3.4 Loose wording (§4.4)

"`Σ|ρ|²` is not a symmetric function of the roots." It *is* permutation-invariant. The true
statement is that it is not a **polynomial in the coefficients** — conjugation is not an algebraic
operation, so `Σρρ̄` escapes the fundamental theorem of symmetric functions. The `2·ReLU(a)`
witness is correct and the conclusion is right; only the phrasing is off.

---

## 4. Where I disagree with the brief's own verdict — it is *too generous*

The brief's verdict is "not viable, by circularity landing on a free modulus." I agree with the
conclusion but think three sharper and more decisive objections are available, and each is
independent of the circularity argument.

### 4.1 The faithfulness test fails: a hard theorem becomes trivial

The brief records, in a table cell and without comment, that Rodgers–Tao's `Λ ≥ 0` translates to
`ρ² ≥ 0`, "automatic, and empty."

That is not a curiosity — it is a diagnostic, and it is the sharpest single objection in the file.
`Λ ≥ 0` is a hard theorem: a substantial paper resting on a delicate analysis of the zero dynamics
under heat flow. **A faithful dictionary maps hard theorems to hard theorems.** One under which a
Forum-of-Math-Pi result becomes "a square is non-negative" has demonstrably discarded the structure
that made it hard. The dictionary is not merely circular; it is *lossy*, and one can point at
exactly what it lost.

### 4.2 It maps an interacting system onto a free one — this is measurable

This is the structural core, and it is testable rather than rhetorical.

- **ADHM side.** The moduli `(X_i, ρ_i)` are independent coordinates on a smooth manifold. Sizes do
  not interact with sizes, positions do not interact with positions, and there is no canonical
  dynamics on moduli space at all. Freedom is the whole content of the space.
- **Ξ side.** The zeros are not independent. They are roots of one entire function, rigidly
  constrained by the explicit formula, by `N(T)`, by GUE pair correlation. And the one natural flow
  on them — the heat/De Bruijn–Newman flow, which is the flow the entire hyperbolicity question is
  phrased through — is a strongly interacting Coulomb gas,

  > `ż_j = 2 Σ_{k≠j} 1/(z_j − z_k)`.

Running that flow on the `k=2` configuration `(τ,σ) = (0, 1.0)` and `(0.35, 0.30)`:

```
    t            centres              sigmas
   0.00     +0.0000, +0.3500      1.0000, 0.3000
   0.02     -0.0345, +0.3845      0.9046, 0.2411
   0.05     -0.1011, +0.4511      0.7609, 0.0476
   0.10     -0.2479                0.5306    (+ real roots +0.2896, +0.9062)
   0.15     -0.4198                0.3194    (+ real roots +0.3627, +1.1769)
   0.1748   -0.5016                0.2025    (+ real roots +0.4107, +1.2925)
   0.20     — all four roots real: -0.6859, -0.4723, +0.4573, +1.4009
```

The "centres" migrate by `0.50` and `0.94` — displacements **larger than the initial size of the
second instanton** — while the two "sizes" collapse on completely different timescales, coupled to
each other and to the separation. Under any dictionary in which `(X_i, ρ_i)` are the free ADHM
moduli, this dynamics is not expressible: it is precisely the interaction that ADHM moduli space is
built to *not* have.

So the dictionary does not just fail to constrain the sizes. It maps the rigidly correlated object
onto the maximally uncorrelated one, and the correlations are where the arithmetic lives.

### 4.3 The §4.3 reformulation is not a statement about gauge theory

§7 lists `ρ_T ∼ 1/log T` accumulation on the Uhlenbeck boundary as a survivor. It is not, for two
reasons that have nothing to do with the factor of 2 in §3.1 above:

- An ADHM instanton of charge `k` has action `8π²k/g²`. `Ξ` has infinitely many zeros, with density
  `(1/2π)log(T/2π)` *growing* with `T`. The corresponding "configuration" has infinite charge and
  infinite action. It is not a Yang–Mills field.
- Uhlenbeck compactification compactifies the moduli space of **fixed** charge `k`. There is no
  Uhlenbeck boundary for `k = ∞`. The phrase names a space the object does not live in.

The brief presents this as "the first version of the target that is not finite-dimensional," i.e.
as progress past the objection that finite constructions probe the easy part. It is better read as
the point at which the gauge theory stops applying: the escape from finite-dimensionality is
achieved by leaving the category.

### 4.4 §4.4's punchline is backwards

The brief's closing flourish is "the geometry computes exactly the quantity the coefficients
cannot." Read carefully, that is a statement that the detector is **not a function of the available
data**. A detector must be computable from what you are given. Hermite's 1856 Bezoutian *is*: its
signature is a polynomial expression in the coefficients and it counts distinct real roots exactly.
`Σ Im(ρ)²` is defined by taking imaginary parts of the roots — "all imaginary parts vanish iff all
roots are real" is a tautology dressed as a criterion. §4.4 is strictly weaker than 19th-century
technology, and the sentence identifying this as a strength is the place where the brief's
self-assessment slips.

The brief does note "the gap between them is the entire problem," so this is a framing error rather
than a factual one — but the framing is doing work it should not.

---

## 5. Verdict

**I agree the program is not a route to a proof, and I would state the reason more strongly than
the brief does.**

The succinct, independently checkable version, in four sentences:

> 1. The only content in the identification is that a real quadratic with no real roots has the
>    form `(t−τ)² + σ²` with `σ² > 0`, and that `det f^{-1}` at charge one has that form with
>    `σ² = 2ρ²`. Every theory containing a positive constant added to a perfect square matches `Ξ`'s
>    Hadamard product equally well, so the match transfers no information.
> 2. Consequently the criterion produced ("all sizes vanish") is a relabelling of "all imaginary
>    parts vanish," which is RH itself, and the relabelling lands on a free modulus that no equation
>    in the theory constrains.
> 3. Two independent confirmations that the dictionary is lossy rather than merely circular: it
>    sends the hard Rodgers–Tao theorem to `x² ≥ 0`, and it sends the strongly interacting
>    De Bruijn–Newman zero flow onto free, non-interacting moduli — the latter is measurable, and
>    the `Λ = ρ²` row fails numerically as soon as `k ≥ 2`.
> 4. The unique deformation that makes the size determinate (noncommutative, `|w|² ≥ |ζ⃗|`) bounds
>    it away from zero, so the only version of the geometry with real dynamics is the one in which
>    the model's analogue of RH is false.

Point 4 deserves more emphasis than the brief gives it, because of an adjacency the brief misses —
see §6.2 below. It turns §6.4 from "a mechanism that points the wrong way" into a closure of the
whole family.

---

## 6. What to do instead

### 6.1 Publish §5 as a short note, detached from RH

`det(D+W) ≥ det D` on ADHM data, giving matching rigidity for all `k` and all classical groups, is
clean and correct. It says: *the ADHM determinant degenerates to a product of point factors only on
the small-instanton, commuting-position locus.* Before writing, check it against Nakajima's
*Lectures on Hilbert Schemes of Points on Surfaces* and Donaldson–Kronheimer — the brief's own
novelty prior ("assume it is known until checked") is the right one. **Effort: days. Payoff: a small
correct thing, with no bearing on RH.**

### 6.2 The adjacency the brief missed — and why it closes the program rather than opening it

Worth checking, because if it holds it is the sharpest possible ending. The noncommutative
deformation of rank-1 ADHM (`μ = [X,Y] + ij = ζ`) is, at `ζ ≠ 0`, the **Calogero–Moser space** of
`k` particles — the same deformation of `Hilb^k(ℂ²)` that Nekrasov–Schwarz use to resolve the
small-instanton singularity. Meanwhile the De Bruijn–Newman flow on roots is exactly a repulsive
`k`-particle Coulomb system in `ℂ`.

So the interacting dynamics the dictionary needs *does* have a geometric home, and it is the
`ζ ≠ 0` deformation — the very one for which the brief proves `|w|² ≥ |ζ⃗|`. Stated as a single
sentence:

> **The deformation that installs the correct dynamics is the deformation that bounds the sizes away
> from zero. There is no member of this family in which the dynamics is right and the conclusion is
> available.**

That is a stronger and more final closure than §6.4's, and it is worth verifying the CM
identification carefully (Wilson; Nakajima; Nekrasov–Schwarz) before relying on it.

### 6.3 The one experiment that could still resurrect a geometric approach

If there is appetite for one more swing at the gauge side, this is the test worth running, because
it is cheap and decisive in both directions.

**Does the natural measure on instanton moduli space reproduce GUE pair correlation?**

Montgomery–Odlyzko: zeta zeros repel with the GUE two-point function. Under the dictionary, zeros
map to instanton centres. So ask: under the natural (hyperkähler `L²`, or Nekrasov-partition-function)
measure on `ℳ_k`, do the simultaneous eigenvalues of the `a'_n` exhibit GUE repulsion?

- If **no** (my prediction, since positions are free moduli) — the dictionary demonstrably fails to
  reproduce the single most robust known statistic of the zeros, and the program is closed on
  positive evidence rather than on a structural argument.
- If **yes** — that would be a genuine surprise and would mean the measure, not the determinant, is
  the object worth studying. Note that any such measure will come from the *deformed* theory, which
  loops back to §6.2.

Either outcome is informative. **Effort: a week of numerics.**

### 6.4 Where effort actually pays: the `(d,n)` margin map

The brief lists this under "Not done," and it is the only unfinished item with value independent of
the instanton picture.

State of the art (Griffin–Ono–Rolen–Zagier, PNAS 2019 / Adv. Math.): `J^{d,n}` is hyperbolic for all
`n` when `d ≤ 8`, and for each fixed `d` for all `n ≥ N(d)`, via the fact that suitably renormalised
Jensen polynomials converge to the **Hermite polynomial `H_d`**, which is hyperbolic with
well-separated roots. RH needs all `d` and all `n`. **The entire gap is uniformity in `d` versus
`n`.**

The computation: map the Hermite (Bezoutian) hyperbolicity margin of `J^{d,n}` over a grid in
`(d, n)`, alongside the `H_d`-approximation error. This measures where the GORZ mechanism runs out
and lets you conjecture the growth of `N(d)` — polynomial or exponential. That shape is the thing
that would tell you whether the Pólya route is closable at all.

This is concrete, runnable here, and I can build it if you want.

### 6.5 The brief's own closing line is right, and should be the pivot

> "The missing ingredient is arithmetic, not geometric. No choice of manifold, gauge group,
> dimension, or moduli space supplies rationality of the moments of `Φ`."

This is the best sentence in the document and it generalises past rationality. The zeros of `Ξ` are
constrained by modularity of `θ`, by the Euler product, by the explicit formula. A dictionary whose
target is a moduli space of free parameters has, by construction, no slot for any of that. Weil
positivity worked in the function-field case because the Hodge index theorem supplied the inequality
on a **rigid integral lattice** — rigidity and integrality were the payload, and the geometry was
the delivery mechanism. Here the geometry delivers a space whose defining property is that it has
neither.

Any future geometric attempt should be screened by a single question asked *first*: **what on the
geometric side is rigid, integral, or arithmetic, and which constraint on the zeros does it carry?**
If the answer is "nothing — the relevant data are moduli," stop before building the dictionary.

---

## 7. Reproduction

`audit1.py` (§2 rows 1–3, symbolic), `audit2.py` (§3.2 `Λ` table, §4.2 flow table),
`audit3.py` (§3.1 gap measurements, §2 rows 4–6). Dependencies: `sympy`, `mpmath`, `numpy`.

## 8. Sources consulted

- Griffin, Ono, Rolen, Zagier, *Jensen polynomials for the Riemann zeta function and other
  sequences*, PNAS 116 (2019); arXiv:1902.07321.
- Griffin, Ono, Rolen, Zagier et al., *Jensen Polynomials for the Riemann Xi Function*,
  arXiv:1910.01227.
- Rodgers, Tao, *The De Bruijn–Newman constant is non-negative*, Forum of Math. Pi (2020).
- Polymath15, upper bound `Λ ≤ 0.22`.
- DHKM, *The Calculus of Many Instantons*, Phys. Rept. 371 (2002); hep-th/0206063 — as cited in the
  brief; not independently re-read.
