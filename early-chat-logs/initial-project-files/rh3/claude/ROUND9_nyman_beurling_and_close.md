# Round 9: Nyman–Beurling screened, and the programme closed out

**2026-08-26.** Runs the three actions `BRIEF_three_live_routes` §5.4 prescribed for route 5(b), the
last live item after `ROUND8_closures`. Supersedes ROUND8's "what to open the next thread with."

**Verdict.** Nyman–Beurling is **the best-shaped criterion in eight rounds of this programme — it is
the only thing that has passed every screen — and there is nothing to feed it.** Two new results
this round: the criterion is *exactly* marginal, verified numerically, and it is **exponentially
insensitive** to off-line zeros, which removes it from every working mode this project has used. The
geometric search space is now exhausted; what replaces it is a precise specification (§6) of what a
candidate would have to do.

| screen | route 3 | route 4 | route 5(a) | **route 5(b)** |
|---|---|---|---|---|
| Screens A / B (holomorphic, deformation) | pass | pass | pass | **pass** |
| Marginality (`NOTE_existence_loophole` §5.3) | pass, then blind | fail (`d=13`) | n/a | **pass exactly, with a computed constant** |
| Quantifier order / uniformity in `d` | pass | **fail** | n/a | **pass — no `d`** |
| Kernel no-go (round 6 §3) | pass | pass | n/a | **pass — no slack parameter** |
| Degeneration screen (ROUND8) | **fail** — weight vanishes on the target | n/a | n/a | **pass — the floor is attained at the target** |
| A source for the statement | none | none | none | **none** |

Every route dies on the last row. Route 5(b) dies *only* on the last row, which is new.

## 1. It is exactly marginal, and this is now measured

Burnol (*A lower bound in an approximation problem involving the zeros of the Riemann zeta function*,
[math/0103058](https://arxiv.org/abs/math/0103058), improving Báez-Duarte–Balazard–Landreau–Saias,
*Adv. Math.* **149** (2000) 130) proves **unconditionally**, in the discrete form quoted by
Bettin–Conrey–Farmer ([1211.5191](https://arxiv.org/abs/1211.5191)):

> `liminf_{N→∞} d_N² log N ≥ Σ_ρ m_ρ² / |ρ|²`,

zeros counted by the **square** of multiplicity. The conjectured asymptotic (Landreau–Richard,
*Experiment. Math.* **11** (2002) 349, Conjecture 3.1: "`d²_n ∼ (2 + γ − log 4π)/log n`") is
`C/log N` with `C = 2 + γ − log 4π`. On the critical line `ρ(1−ρ) = ¼ + t² = |ρ|²`, so the two
constants are the same sum. Verified:

| quantity | value |
|---|---|
| `2 + γ − log 4π` | `0.0461914179322` |
| `Σ_ρ 1/\|ρ\|²`, first 250 zeros (both signs, to `t = 470.77`) | `0.0426024249815` |
| Riemann–von Mangoldt tail | `0.00359471` |
| total | `0.04619713349` |
| relative difference | `1.24 × 10⁻⁴` (tail-estimate limited) |

> **The conjectured limit of `d_N² log N` is the unconditional lower bound itself. The criterion is
> conjectured to converge exactly to its own floor: no slack anywhere.**

That is `NOTE_existence_loophole` §5.3's falsification criterion 4 — *a positivity mechanism that
degenerates marginally at the arithmetic point rather than holding with room to spare* — satisfied,
for the first time in this programme, and with the degeneration constant in closed form. Balazard–de
Roton note that equality would imply RH **and** simplicity of the zeros, so the marginality is
doubly tight. It also passes the ROUND8 degeneration screen in the Kenyon–Okounkov–Sheffield shape
rather than the route-3 shape: the structure's natural degeneration *is* the target locus.

Numerical support, and it is the only substantive computation in the literature: Landreau–Richard
reach `N = 20 000` and find `d_N √log N ≈ 0.21377` against the predicted
`√C = 0.21492` — 0.5%.

## 2. It is exponentially insensitive to off-line zeros — and this is what kills it

Balazard–Saias–Yor (*Notes sur la fonction ζ de Riemann, 2*) prove
`(1/2π)∫_{Re s=1/2} log|ζ(s)|/|s|² |ds| = Σ_{Re ρ>1/2} log|ρ/(1−ρ)|`, and RH ⟺ the left side is
zero. So the natural measure of an RH violation in this framework is
`signal(δ, t) = log|ρ/(1−ρ)|` for `ρ = ½ + δ + it`, i.e. `≈ δ/(¼ + t²)`. Setting that against the
baseline `C/log N`:

> **`log N ≳ (2 + γ − log 4π) · t² / δ`** to see a zero at height `t`, distance `δ` off the line.

| height `t` | `δ` | signal | `log N` needed | `N` needed |
|---|---|---|---|---|
| 14.13 (first zero) | 0.1 | `5.0e−4` | 92 | `10^40` |
| 14.13 | 0.01 | `5.0e−5` | 923 | `10^401` |
| 10 | 0.01 | `1.0e−4` | 463 | `10^201` |
| 100 | 0.01 | `1.0e−6` | 46 193 | `10^20060` |
| 1000 | 0.001 | `1.0e−9` | `4.6e7` | `10^2.0e7` |

And the power of the existing numerics, inverted: at `N = 20 000` (`log N = 9.90`) the computation
can only distinguish a zero with

| height `t` | smallest detectable `δ` |
|---|---|
| 1 | 0.0058 |
| 2 | 0.0198 |
| 5 | 0.118 |
| 10 | **0.469** |

Since `δ ≤ ½` always, **the best computation in the Nyman–Beurling literature has essentially no
power against a violation above height ~5**, and none at all above ~10. The agreement to 0.5% at
`N = 20 000` is therefore consistency with the conjectured constant, not evidence for RH.

Two consequences, and the second is the fatal one.

- **The criterion cannot be used as a detector or a control.** Every other item in this programme was
  screened by *measuring* something — exact Sturm counts, DBN margins, reachable cones. Nyman–Beurling
  admits no such use: the measurement has no power. This also means the Davenport–Heilbronn control
  the brief asked for cannot be run numerically even in principle. *(It cannot be run structurally
  either — see §3.)*
- **Any mechanism supplying the density must supply the limit exactly, in closed form.** Approximate,
  asymptotic, variational or physical arguments that get within `o(1)` of the floor are worth nothing:
  the whole content is in whether `d_N² log N` reaches `Σ 1/|ρ|²` or stops above it, and the gap in a
  violating case is `O(δ/t²)`. The `t²/δ` scaling is constant-independent, so this survives any
  order-one error in the comparison below.

*(Honest scope: identifying the limiting `d_N²` with the Balazard–Saias–Yor functional up to an
order-one constant is my own scale comparison, not a cited theorem. The `t²/δ` scaling — which is all
the conclusion uses — is unaffected by that constant. Flagged rather than dressed up.)*

## 3. Discrimination is genuine, but the D–H control is unavailable

Anne de Roton generalised the criterion to the Selberg class (*Généralisation du critère de Beurling
et Nyman pour l'hypothèse de Riemann*, C. R. Acad. Sci. Paris **340** (2005) 191,
[numdam](http://www.numdam.org/articles/10.1016/j.crma.2004.11.023/); thesis
*Généralisation du critère de Beurling–Nyman à la classe de Selberg*, Bordeaux 2003; quantitative
version *Bull. SMF* **134** (2006) 417). Her Theorem 2.3 is an honest equivalence: `F` non-vanishing
in `Re s > ½` ⟺ `B_F` dense in `L²(0,1)`. **So the criterion is a genuine zero-localisation
statement and cannot be fooled** — it passes the round-5 genericity worry that sank the N=4
reformulation.

But the specific Davenport–Heilbronn control is **not available**: D–H has no Euler product, and de
Roton's axioms require one (`log F(s) = Σ b_n n^{-s}` with `b_n` supported on prime powers). Searches
for Nyman–Beurling applied to Davenport–Heilbronn or the extended Selberg class returned nothing. So
the honest status is: *the criterion demonstrably distinguishes within the class where it is defined,
and D–H lies outside that class.* The Euler product being a hypothesis rather than a conclusion is
itself informative — the criterion carries arithmetic in its construction, which is why it is not
generic.

## 4. The supply side: nothing, and the three near-misses each fail differently

- **de Branges** is the only programme offering a *sufficient* condition from a Hilbert-space
  structure — and Conrey–Li ([math/9812166](https://arxiv.org/abs/math/9812166), IMRN **2000** no. 18,
  929) refuted its concrete instance: they "give examples showing that de Branges' positivity
  conditions, which imply the generalized Riemann hypothesis, are not satisfied by defining functions
  of reproducing kernel Hilbert spaces," concluding "these positivity conditions are too strong for
  Hilbert spaces of entire functions associated with the Riemann zeta function and the Dirichlet
  `L`-functions." The de Branges *theorems* stand; the hypothesis is false for the functions that
  matter. **Sufficient condition, unverifiable — the exact opposite failure mode from everything else
  in this project, which produced verifiable conditions with no content.**
- **Connes** has a genuine geometry where positivity would be a consequence rather than a restatement,
  and by his own 2026 survey ([2602.04022](https://arxiv.org/abs/2602.04022)) the open step is that
  "the approximating zeros produced by this method converge to the actual zeros … While the numerical
  evidence in support of this is overwhelming, evidence alone is not a proof," with the concession
  that "a complete proof along these lines may encounter serious obstacles." His survey lists
  Beurling–Nyman only as one equivalence among many; there is no worked bridge.
- **Burnol's Lax–Phillips causality** ([math/0001013](https://arxiv.org/abs/math/0001013), J. Number
  Theory **87** (2001) 253) is the only genuinely *physical* structure built explicitly on the
  Nyman–Beurling theme: "I associate to a global field K a Lax-Phillips scattering which has the
  property of causality if and only if the Riemann Hypothesis holds for all the abelian L-functions
  of K." An **iff** — a translation into scattering language, not a source.

**Absences, reported as absences.** No connection in the refereed literature between Nyman–Beurling
and random matrix theory, a Hamiltonian, Hilbert–Pólya, or any quantum structure. The
Bettin–Conrey / cotangent-sum industry ([1111.0931](https://arxiv.org/abs/1111.0931), and Bettin
IMRN 2015, Maier–Rassias, Goubi) is arithmetic-statistical refinement and claims no RH consequence.

## 5. Round 1's question, in the new formulation

*What on the geometric side is rigid, integral, or arithmetic, and which constraint on the zeros does
it carry?*

For the first time the answer is not "nothing." The Báez-Duarte Gram matrix entries are **Vasyunin /
cotangent sums** — functions on `ℚ` satisfying a reciprocity formula, generalising the Dedekind sum
(Bettin–Conrey, verbatim: "we find a reciprocity formula for the Vasyunin sum"). That is genuine
rigid arithmetic sitting inside the criterion.

**But it is on the criterion's own side.** The Vasyunin sums are built from `ζ`; they are not
supplied from outside. This is exactly the delivery/payload split of `NOTE_existence_loophole` §6.3 —
the arithmetic is present and is the *wrong* arithmetic, being a repackaging in Weil's sense rather
than a transported constraint. Hermite's positivity failed the same way. So the payload question is
unchanged, and the answer is still no.

## 6. What a candidate would have to do — the specification, and the closure

Eight rounds have converged to a checklist that no known structure meets. A geometric or physical
source for RH must:

1. deliver on the **coefficient side**, not the product side (`NOTE_existence_loophole` §6.3);
2. be **uniform in `d`**, or avoid `d` entirely — which selects Nyman–Beurling-type targets over
   Pólya-type ones (round 6 §2.2);
3. **degenerate exactly at the arithmetic point**, not hold with room to spare (§5.3) — the ABJM /
   mirror-curve family of §5.2(a) is still the untested candidate here;
4. have its **natural degeneration coincide with the target locus** rather than avoid it (ROUND8) —
   the Kenyon–Okounkov–Sheffield shape, not the route-3 shape;
5. supply its statement **exactly and in closed form**, since the target admits no approximate,
   asymptotic or numerical version (§2 above);
6. and carry arithmetic that is **transported, not repackaged** — rigid or integral structure whose
   constraint on the zeros is not already a consequence of the Hadamard product (round 1 §6.5).

Conditions 1–4 are each individually satisfiable by something in the literature. **No object in this
survey satisfies 5, and nothing at all satisfies 6.** Condition 6 has been the answer since round 1
and every subsequent round has re-derived it from a new direction; condition 5 is new this round and
is the one that removes the last working mode.

**This closes the programme as a search.** What it leaves is not a wall but a specification, and the
specification's binding constraint is item 6 — which is Weil's observation about the function-field
case, restated: integrality and rigidity are the payload, geometry is only delivery. No amount of
better geometry helps.

## 7. What is worth writing up

Two small measurable things, neither bearing on RH:

- **The VW/K3 Jensen measurement** (route 4, `BRIEF` §4.3) — hyperbolic at every shift for `d ≤ 8`,
  at the `n = 0` edge for `d ≤ 12`, failing at `d = 13`. A second worked example after `p(n)` of
  "for each `d`, all large `n`" holding while "all `d`, all `n`" fails. Days of work.
- **The power analysis of §2** — that the Nyman–Beurling approximation problem needs
  `log N ≳ C t²/δ`, hence that `N = 20 000` has no power above height ~10, and that the 0.5%
  agreement at `N = 20 000` is consistency with the conjectured constant rather than evidence for RH.
  I have not found this stated in the literature, but it is elementary given Balazard–Saias–Yor and
  Landreau–Richard, so **assume it is known until a search says otherwise** — that check has not been
  done and should be, before anything is written.

Route 3's closure (`NOTE_4d_anisotropic_cycles`) is publishable only as a negative and probably not
worth it, with one exception: *"Perotti's four-dimensional Jensen formula, specialised to
real-coefficient slice-preserving functions, equals classical Jensen plus `Re(p₂)/(4R²)`"* is a clean
small statement in quaternionic function theory with no RH content, and the observation that
`dV₃ = 4πy² ds` makes every `SO(3)`-invariant integral blind to the real axis may be of interest to
that community.

## 8. Methodological record

- My "RH ⟺ `ζ(s)/s` is outer" phrasing from the previous round is **not standard and should not be
  cited as such** — a targeted search found no source stating it. The substance is Balazard–Saias–Yor's
  Jensen-equality form, and they do place the problem explicitly in Hardy spaces and invoke the
  singular inner factor. Recorded because I stated it with more confidence than it deserved.
- The §2 comparison is flagged in place as a scale estimate rather than an identity, and the
  conclusion is stated in the form that survives the missing constant.
- Two literature verdicts this round rest on extraction layers rather than direct PDF reads (BBLS
  *Adv. Math.* is paywalled; the exact indexing of its sum over zeros is **unverified** — Burnol
  writes it over all non-trivial zeros, Bettin–Conrey–Farmer restrict to `Re ρ = ½`). This does not
  affect §1's conclusion, which only needs the two constants to coincide, and that was checked
  numerically rather than taken from a source.

## Reproduction

`nb1.py` — §1 (the constant `2+γ−log 4π` against `Σ_ρ 1/|ρ|²` from the first 250 zeros plus the
Riemann–von Mangoldt tail) and §2 (the signal `log|ρ/(1−ρ)|`, the required `log N`, and the inverted
power of `N = 20 000`). Deps: `mpmath`. `mp.zetazero` dominates the runtime; 250 zeros is enough for
`10⁻⁴`.
