# Gravitational Instantons and Full Gravity: Rationality Without Content

*Working memo #13 — August 23, 2026. Answers a direct question: were gravitational instantons and full (non-self-dual) gravity considered? They had not been. Three sub-routes, three verdicts, and one genuine sharpening of brief §6.5. Certified by `lab_ade_rigidity.py`; literature flagged per item.*

---

## 0. Result

**Not previously considered. Now screened, and the answer is more interesting than "no".**

**(1) ALE gravitational instantons supply exactly the object brief §6.5 says is missing — a definite `ℤ`-lattice — and at every rank.** This is the first construction in the whole programme with that property, and it deserves to be stated plainly.

By Kronheimer, every ALE hyperkähler 4-manifold is the minimal resolution of `ℂ²/Γ` for a finite `Γ ⊂ SU(2)`, and `H²(X; ℤ)` is the corresponding **ADE root lattice** with intersection form `= −(Cartan matrix)`: even, negative definite, with the `(−2)`-classes exactly the roots. Verified inventory (`lab_ade_rigidity.py` Part 1): `A_n` (`n ≥ 1`), `D_n` (`n ≥ 4`), `E₆`, `E₇`, `E₈`, all even and negative definite, with `det = n+1, 4, 3, 2, 1`.

**And this evades memo 5's obstruction.** Memo 5 / `Lab_Tower_Check.py` Part 1 found a *rank gap* in the compact hyperkähler Hodge–Riemann tower: with `b₂ ∈ {7, 8, 23, 24}` the primitive pieces have dimensions `C(b+m−1, m) − C(b+m−3, m−2)`, and only

`{1, 7, 8, 23, 24, 27, 35}` — **7 of the first 40 ranks**

are reachable, while RH needs a definite form of *every* rank `d`. The ALE side has `A_d` for every `d ≥ 1`, so **all 40 of 40**. Memo 5's rank obstruction is specific to the compact Hodge–Riemann tower and does not transfer. On rank alone, the ALE route is not excluded.

**(2) It fails instead on *content*, and the failure is sharp.** The lattice is **rigid**: it is determined by `Γ` alone and carries no moduli. All continuous data in Kronheimer's theory lives in the periods `α₁, α₂, α₃ ∈ ℝ³ ⊗ 𝔥`, not in the form. And the only discriminant the ALE *existence* theorem can express is Kronheimer's nondegeneracy condition — the complement of a **finite union of real linear subspaces of codimension 3**, one per root `ξ` (all three periods annihilate `ξ`).

So: can a finite union of linear subspaces bound the hyperbolic locus? No. The boundary of `H` is the discriminant hypersurface, and (`lab_ade_rigidity.py` Part 3, symbolic):

| `d` | `deg(disc)` | irreducible factors | linear factors |
|---|---|---|---|
| 2 | 2 | 1 | 0 |
| 3 | 4 | 1 | 0 |
| 4 | 6 | 1 | 0 |
| 5 | 8 | 1 | 0 |

The discriminant is irreducible of degree `2(d−1)` and is never a product of linear forms. **No finite union of linear subspaces has `H` as its closure**, so the ALE existence condition cannot express hyperbolicity — at any `d`, and independently of everything else.

**(3) The real contribution: brief §6.5 sharpens into a dichotomy.** The brief says the missing ingredient is *rationality*. Reading the gravitational-instanton inventory against this programme's own objects makes the statement much more precise. Every construction to hand falls into exactly one of two classes:

| object | form varies with `Ξ`? | defined over `ℚ`? |
|---|---|---|
| ADE root lattice (ALE instanton) | **no** | yes |
| `−I_k` (ALF compactification, Etesi–Hausel) | **no** | yes |
| Hirzebruch–Jung string (toric Ricci-flat) | **no** | yes |
| Beauville–Bogomolov form `q_X` | **no** | yes |
| trace form of `J^{d,n}` (`Lab_Tower_Check` Part 3) | yes | **no** |
| ADHM `C = ΣT_a² + Re(λ†λ)` | yes | **no** |
| memo 9's transverse Hessian `c₂` | yes | **no** |

> **The rationality wall is exactly the statement that no known construction is in both classes.** Class (a) has rationality without content — entries are small fixed integers (`0, ±1, 2`) carrying no dependence on `Ξ`. Class (b) has content without rationality — entries are power sums of roots of polynomials whose coefficients are the moments `M_k = ∫Φ(u)u^k du`. Weil's argument needs *one object with both*.

That is a better statement of §6.5 than "rationality is missing", because it is a **screen**: for any proposed object, ask whether the form varies with `Ξ`'s data and whether it is defined over `ℚ`. Everything so far answers yes to exactly one.

**(4) Full (non-self-dual) gravity is the obstruction ladder, only longer — so it is *more* deeply in the shape memo 11 excludes, not less.** Confirmed order numbers (LeBrun, via the Atiyah–Dunajski–Mason review, verbatim): *"The existence of fifth-order formal neighbourhoods corresponds to vanishing of the Bach tensor of the space-time and, when the space-time is algebraically general, a sixth-order extension corresponds to the space-time being conformally Einstein."* Compare Yang–Mills at third order. And at order zero the situation is the same as for YM: Isenberg–Yasskin's non-self-dual nonlinear graviton encodes an **arbitrary** complex Riemannian metric as a deformation of projective ambitwistor space, with no field equations imposed. Existence free, equations as extension obstructions — dead by memo 11's Theorem and Corollary B.

**(5) Hitchin's monopole spectral curves — brief §7.3's one untested lead — are now closed, and they decompose exactly along this programme's own axis.** The three conditions (Hitchin 1982, 1983; as restated by Houghton–Manton–Romão) on a curve `S ∈ |O(2k)|` in mini-twistor space:

| condition | type | verdict |
|---|---|---|
| `σ(S) = S`, i.e. `α_j(ζ) = (−1)^j ζ^{2j} \overline{α_j(−1/\bar ζ)}` | **totally real linear slice** — `ℝ`-linear, not holomorphic; fixed locus of an antiholomorphic involution | the right shape, but imposed by hand: carries no information |
| `L²|_S` trivial | **complex-analytic vanishing** (a point of `Jac(S)`) | dead by memo 11's **Theorem** |
| `H⁰(S, L^s(k−2)) = 0`, `0 < s < 2` | **generic / non-vanishing** | dead by memo 11's **Corollary A** |

So the entire field-equation content of the monopole correspondence is holomorphic vanishing, and its one genuinely region-like ingredient is a non-vanishing condition — the other parity, which Corollary A also excludes. **Brief §7.3's "structurally closer than ADHM, untested" is now tested and closed.** It is also the first place Corollary A has earned its keep.

**(6) Positivity in gravity is worse than in gauge theory, not better.** The generalized positive action conjecture is **false**: LeBrun, *Counter-examples to the generalized positive action conjecture*, Comm. Math. Phys. **118** (1988) 591–596, exhibits complete locally asymptotically flat scalar-flat 4-manifolds with **negative mass**. So there is no positivity theorem to recruit in the ALF category at all. Where positivity does hold — Hitchin's result that all `L²` harmonic 2-forms on a 4-dimensional hyperkähler quotient are anti-self-dual, hence the `L²` intersection form is negative definite — it is precisely the Hodge-index family memo 5 already worked and memo 12's screen 0″ predicts will be circular.

**(7) One item worth recording that has the right shape and is not a route.** Jiang, *Positivity of Riemann–Roch polynomials and Todd classes of hyperkähler manifolds*, arXiv:2008.04685, J. Algebraic Geom. **32** (2023). For compact hyperkähler `X` of dimension `2n` there is a polynomial `RR_X` with `χ(L) = RR_X(q_X(c₁(L)))` for every line bundle `L`, in the single Beauville–Bogomolov quadratic form. Jiang **proves** all coefficients of `RR_X` are positive, and **conjectures** (Conjecture 1.3) that all its roots are negative real numbers — indeed negative even integers in arithmetic progression. The four known deformation types give binomial coefficients: `K3^[n] : C(t/2+n+1, n)`, `Kum_n : (n+1)C(t/2+n, n)`, `OG₆ : 4·C(t/2+3, 3)`, `OG₁₀ : C(t/2+6, 5)` — roots negative even integers in every case.

This is the **same logical shape as RH via Jensen polynomials**: coefficient positivity proved, real-rootedness conjectured, on an object that is a lattice with a quadratic form. It is not a route — the coefficients are Todd/Chern data of `X` with no slot to load `Ξ` into, and no literature connects it to `ζ`. But it is a structural analogue on the correct side of the rationality dichotomy (the BB form is integral), and if a testbed for "positivity ⇒ hyperbolicity" mechanisms is ever wanted, this is one with a live open conjecture attached. Note also that the programme already touches this circle: `Lab_Tower_Check.py` Part 1 computes `dim H^m` for exactly these four deformation types.

---

## 1. What the inventory of definite forms actually is

Screening question: does any gravitational-instanton family realise *arbitrary* definite integral forms, or arbitrary large-rank ones? Answer: no, and the restriction is rigidity rather than rank.

| class | forms available |
|---|---|
| ALE hyperkähler | `−(ADE Cartan)`: `A_n, D_n, E₆, E₇, E₈` (Kronheimer) |
| ALF hyperkähler | `A_k` and `D_k` only — multi-Taub-NUT and Cherkis–Hitchin–Ivanov–Kapustin–Lindström–Roček (Gao Chen) |
| ALF, compactified | `−I_k`, definite and **diagonalizable over `ℤ`** (Etesi–Hausel, hep-th/0602053) |
| ALG | tied to 7 Kodaira fibre types on rational elliptic surfaces |
| ALH | one fixed model, the `(ℝ × T³)/ℤ₂` resolution, 8 curves |
| toric Ricci-flat, non-hyperkähler | tridiagonal Hirzebruch–Jung strings (Nilsson, arXiv:2301.10212, Thm 1) |
| compact hyperkähler (K3, `T⁴`) | **indefinite** (`U³ ⊕ E₈(−1)²`, `U³`) — no definite form at all |

Every entry is a single fixed matrix determined by discrete data, from a very thin list. At each rank `d` the ALE side offers **at most three** forms (`A_d`; `D_d` for `d ≥ 4`; plus `E_d` for `d = 6,7,8`), all root lattices — which by Witt is the unique class of definite lattices generated by norm-2 vectors. A hyperbolicity criterion needs the form itself to vary over a `d`-real-parameter family; nothing here does.

Worth noting for completeness: in the *closed* smooth 4-manifold category, Donaldson's theorem says a definite intersection form is diagonalizable over `ℤ`, so arbitrary definite forms are unavailable there too. The ADE forms appear only because ALE spaces are open.

## 2. New screen

Offered for brief §8, following memo 11's screen 0 and memo 12's screen 0″:

> **Screen 8′ (rationality dichotomy — replaces the old screen 8).** Ask two questions of the proposed object's form: **(i) does it vary with `Ξ`'s data?** and **(ii) is it defined over `ℚ`?** Weil's argument needs both. Every construction examined in this programme answers yes to exactly one: geometric forms with integral entries (ADE root lattices, `−I_k`, Hirzebruch–Jung strings, the Beauville–Bogomolov form) are rigid and carry no `Ξ`-dependence; forms that carry `Ξ`-dependence (Jensen trace forms, the ADHM Gram, memo 9's Hessian) have entries built from the moments `M_k = ∫Φ(u)u^k du` and no known `ℚ`-structure. A proposal that does not answer yes to both is capped exactly where §6.5 says, and the screen tells you which half is missing.

The old screen 8 asked "does anything supply a `ℚ`-structure?" That was answerable "no" for everything, which made it uninformative. The two-question version distinguishes *why* each candidate fails, and it identifies what a working object would have to look like: a family whose integral intersection form varies with `d` real parameters. Nothing in the gravitational-instanton literature is of that kind, and Donaldson plus Witt suggest nothing in 4-manifold topology is.

## 3. Assessment

Gravity is closed three ways, none of them new mechanisms:

1. **Full gravity** is the ambitwistor obstruction ladder at orders 5 and 6 — memo 11's Theorem and Corollary B, exactly as for Yang–Mills at order 3.
2. **Gravitational instantons via matching** would fall to memo 12's positivity dichotomy, and in the ALF category there is no positivity theorem to have (LeBrun 1988).
3. **Gravitational instantons via existence** fail on §0(2): the ALE existence condition expresses only unions of linear subspaces, and `∂H` is an irreducible hypersurface of degree `2(d−1)`.

What the excursion contributed is §0(3) — the rationality dichotomy — which is a strictly better statement of brief §6.5 than the brief has, and §0(5), which closes the last untested lead in brief §7.3. Both are negative results, which by the brief's own accounting (§7.4 item 4) is the category most of this work has been in.

`PROGRAM_CLOSED.md` stands. Nothing here reopens anything, and after memos 9–13 the brief's §7 has no live leads left: §7.1 and §7.2 closed by memo 11, §7.3 closed here, and §7.4's items 1–3 all require an object satisfying both halves of screen 8′.

**Update 2026-08-24: Kronheimer read directly, and the paper is now primary-sourced.** Every claim in §0(1)–(2) is confirmed from *The construction of ALE spaces as hyper-Kähler quotients*, J. Diff. Geom. **29** (1989) 665–683:

- **The sign is resolved.** §4, verbatim: *"the nondegeneracy condition (∗) in Theorem 1.1 just says that the `α_i` do not all lie in the kernel of any one root"* — so the condition is `α_i(Σ) ≠ 0` for some `i`, as suspected.
- **The lattice.** §4, verbatim: *"The exceptional set in the minimal resolution of `ℂ²/Γ` is a union of 2-spheres whose intersection matrix is the negative of a Cartan matrix"*, and *"`H²(X_ζ;ℤ)` is the root lattice. Under this last identification, the classes `Σ` with `Σ·Σ = −2` are the roots."*
- **The linearity, which is what §0(2) turns on.** Proposition 2.8: the bad set is a union of **codimension-3** subspaces `ℝ³ ⊗ D_θ`, one per root. Proposition 4.1(i): the period map `σ : Z → 𝔥` is a **linear isomorphism**. So the discriminant available from ALE existence is linear in the periods, exactly as §0(2) assumed.
- Also confirmed: the McKay correspondence is one-to-one between finite subgroups of `SU(2)` and the simply-laced diagrams `A_r, D_r, E₆, E₇, E₈`; and Theorem 1.2 (from the companion Torelli paper) gives exhaustiveness, so Nakajima's positive-mass route is an alternative proof rather than a necessary one.

**A strengthening, from Anderson–Kronheimer–LeBrun, *Complete Ricci-Flat Kähler Manifolds of Infinite Topological Type*, Comm. Math. Phys. **125** (1989) 637–642.** The natural objection to §0(2) is "what about infinitely many centers?" They answer it: the Gibbons–Hawking ansatz with infinitely many sparsely distributed centers gives a complete hyperkähler 4-manifold with **infinitely generated `H₂`**, plumbed *"according to the 'Cartan matrix' `A_∞`"*, and — verbatim — *"we have produced an **infinite-dimensional family** of such metrics on `M`"*, the moduli being the positions `{p_j} ⊂ ℝ³`, recoverable from the metric up to isometry of `ℝ³`.

So **infinite rank and infinite-dimensional moduli are both available, and the form is still rigid**: it is `A_∞` regardless of where the centers sit. The moduli live in the positions — i.e. in the periods — exactly as in the ALE case. §0(2) and §0(3) survive the strongest version of the objection.

*(One honest caveat: their construction requires `Σ_j 1/‖p_0 − p_j‖ < ∞`, a **convergence** condition on the centers, which is the only genuinely non-linear condition anywhere in this literature. It is not usable as stated — for centers at the zeta zeros `Σ 1/γ_j` diverges, so the hypothesis fails outright — but it is the one place the available conditions are not linear-plus-finite, and I have not excluded it.)*

**Still unconfirmed, and worth resolving if any of this is pursued.**
1. **LeBrun, *Thickenings and conformal gravity*, Comm. Math. Phys. 139 (1991) 1–43.** Abstract verified; full text unread. The abstract says the correspondence is for vanishing *Bach and Eastwood–Dighton* tensors, while ADM's one-liner gives 5th order ↔ Bach and 6th ↔ conformally Einstein. The natural reconciliation (5th = Bach, 6th = Bach + Eastwood–Dighton) is **unconfirmed**; the order numbers 5 and 6 themselves are confirmed via ADM.
2. **Nakajima's positive-mass theorem** for ALE Ricci-flat 4-manifolds (Adv. Stud. Pure Math. **18-I** (1990) 385–396) — this is what makes Kronheimer's ADE list exhaustive. Bibliographic data confirmed, theorem text unread.
3. **Kronheimer's companion Torelli paper** (J. Diff. Geom. **29** (1989) 685–697) was not read directly; Theorem 1.2 above is quoted from the announcement in the paper that was.

**Novelty status: assume known.** §0(1)–(2) are readings of the standard ALE classification against a screen. §0(3) is a bookkeeping observation. The discriminant-irreducibility check in Part 3 is classical. Nothing here is a new mathematical result; the value is entirely in the screening.

---

*Certified by `lab_ade_rigidity.py`: Part 1, the ADE Cartan matrices with their evenness, definiteness, determinants and multiplicity per rank; Part 2, the rank comparison against memo 5's Hodge–Riemann tower (`7` of `40` versus `40` of `40`); Part 3, symbolic irreducibility and non-linearity of the discriminant for `d = 2,3,4,5`; Part 4, the rationality dichotomy table. Literature established by a dedicated search pass with per-item confidence flags; Kronheimer 1989 (both papers), LeBrun CMP 139 (1991), LeBrun CQG 2 (1985) and Nakajima 1990 were NOT read directly and every statement about them is from secondary sources that agree with one another.*
