# Round 6: the unscreened sweep — one closure, one reframing, and three live targets

**2026-08-26.** Six parallel literature sweeps, run deliberately *without* pre-screening, following a
methodological correction from the user: the project's adversarial discipline is correct at the
verification stage and corrosive at the generation stage, so ideas were to be listed first and
screened second. One sweep died to an API error and is unfinished (§9).

**Headline.** The Males–Ono check closes negative and cleanly — my hypothesis was wrong and round 2's
dismissal was right. But the sweep overturned something more important: **the `d`-uniformity gap is
not a quantitative deficit, it is a change of quantifier order**, and the framing I have been using
for it (and stated in rounds 2–4) was wrong. Two further findings sharpen our own screens into
theorems and one reverses a round-5 dismissal. Three genuinely unexplored targets emerged, one of
which sits on machinery we already built.

---

## 1. The Males–Ono check: closed, negative

**Identity correction first.** `arXiv:2204.05465` is **Johnston–Males**, *Exact formulae and Turán
inequalities for Vafa–Witten invariants of K3 surfaces*, Proc. Edinb. Math. Soc. **66** (2023)
845–861. **Ono is not an author.** Round 2 and round 5 both referred to it as "Males–Ono et al.";
that was wrong, and it mattered to my reasoning — I had weighted it as a paper with Ono's hand on the
uniformity question, which it is not.

**The result is GORZ-shaped and silent on uniformity.** Theorem 1.7, verbatim: *"For fixed `r` and
`p`, as `n → ∞` the Vafa–Witten invariants `α_{1,r}(n)` and `α_{3,p}(pn)` each satisfy all order `k`
Turán inequalities."* The order `k` is a fixed parameter per inequality; the statement is an
`n → ∞` statement per `k`. The engine is GORZ, quoted in the paper as "for all but finitely many
`n`." **No `N(k)`, no discussion of `k`-dependence, effective or otherwise.** The paper is silent,
not negative.

**What the proof consumes, stratified:**

| layer | consumed | where |
|---|---|---|
| partition functions as twisted `η`-combinations | algebraic geometry (Tanaka–Thomas, Jiang–Kool, Jiang) — quoted, not proved | Thms 1.1–1.3 |
| exact coefficient formulae | modularity: circle-method / Rademacher expansion of `η`-quotients | Lemma 1.4, Thm 1.5 |
| asymptotic expansion with error | same, differentiated | Thm 1.6 |
| **hyperbolicity / Turán** | **only the asymptotic expansion, fed to GORZ** | Thm 1.7 |

So modularity and integrality are **upstream of the only step that touches hyperbolicity**.
Integrality of the counting invariants plays no role at all. **My hypothesis — that an exact
Rademacher formula might buy uniformity — is refuted: the exact formula is used to manufacture an
asymptotic expansion, and the asymptotic expansion is all the hyperbolicity step sees.**

Round 2 §3.3's one-paragraph dismissal ("an inherited toolkit, not a link") was correct. My
objection to it in this session was wrong.

## 2. The reframing: uniformity in `d` is a quantifier-order problem, not an error-term problem

This is the round's most important finding and it corrects the framing used in rounds 2–4 and
throughout this session.

### 2.1 What I had been saying, and why it was wrong

I described the gap as: *GORZ matches the renormalized Jensen polynomial to `H_d` and bounds the
error; `H_d`'s minimum root gap shrinks with `d` while the error grows; hence `N(d)` grows.* The
quantitative facts are right — `min-gap(H_d) ≍ π/√(2d) ≍ 2.22 d^{−1/2}` at the centre, root spread
`≍ √d`, so `min-gap / spread ≍ 1/d` — but **this is a feature of the GORZ *method*, not of the
problem.**

**Kim–Lee** (*A note on the zeros of Jensen polynomials*, J. Korean Math. Soc. 2022,
[arXiv:2105.05386](https://arxiv.org/abs/2105.05386)) get `N(Ξ; d) = O(d^{1/2+ε})` — **polynomial,
sublinear** — by a Gauss–Lucas plus Obreschkoff argument with **no Hermite comparison and no
asymptotics at all.** The ranking of known thresholds:

| result | threshold | wedge |
|---|---|---|
| GORZ 2019 ([1902.07321](https://arxiv.org/abs/1902.07321)) | `n ≥ N(d)`, non-effective | — |
| GORTTW 2022 ([1910.01227](https://arxiv.org/abs/1910.01227)) | `n ≥ c e^{d/2}` | `d ≲ 2 log n` |
| **Kim–Lee 2022** | **`n ≫ d^{1/2+ε}`** | **`d ≲ n^{2−ε}`** |
| Holland 2026 ([2608.08682](https://arxiv.org/abs/2608.08682), **unrefereed**) | `n ≳ d^{5/3}/log^{2/3}` | `d ≲ n^{3/5}` |

So the wedge is far wider than round 2–4 assumed, and the best result got there by abandoning the
method whose limitation I was describing as the obstruction.

### 2.2 The actual structure of the gap

Every known result has the form **"`J^{d,n}` is hyperbolic when `d ≤ f(n)`"** for some finite `f`.
But `Ξ ∈ LP` follows already from hyperbolicity of `J^{d,0}` for **all** `d`. So:

> **RH is the single vertical line `n = 0`, `d → ∞` — the one direction in which every known wedge is
> empty by construction. Improving `f` from `2 log n` to `n^{2−ε}` to `n^{100}` does not move toward
> RH at all. The gap is a change of quantifier order, not a quantitative deficit.**

This appears to be unwritten. Ki's Oberwolfach report (OWR 2022/13) and Kim–Lee's own remarks
acknowledge the barrier in a sentence each; the only sustained treatment found is a
non-peer-reviewed preprint whose regime is out of date by a factor `d^{3.5}`.

### 2.3 A sharp negative that constrains every candidate mechanism

For the partition function `p(n)`, the higher-order Turán inequality (hyperbolicity of `J^{3,n}_p`)
**fails** for `n < 95` and holds only for `n ≥ 95` (Chen–Jia–Wang; proved by GORZ and by
Larson–Wagner). So `Σ p(n)z^n/n!` is **not** in the Laguerre–Pólya class, yet `J^{d,n}_p` is
hyperbolic for each fixed `d` once `n` is large.

> **Therefore no method using only the GORZ-type asymptotic hypothesis can ever prove uniformity —
> the hypothesis is satisfied by a sequence for which the conclusion is false.** Any uniform
> mechanism must use something `Ξ` has that `p(n)` lacks.

Candidates for that "something," in the sweep's judgement: the functional equation / the `z ↔ −z`
symmetry of `Ξ`; positive-definiteness of the DBN kernel; or verified zero data.

### 2.4 The two mechanisms of the right shape

**(a) Finite-verification-in / uniform-out.** GORTTW Thm 1.2 and Kim–Lee Thm 4: verified RH up to
height `T` ⟹ `J^{d,n}` hyperbolic for **all `n`** when `d ≲ T²`. Kim–Lee with `T ≥ 3·10¹²` gives
`d ≤ 9·10²⁴` for **every** `n`. This is the transpose of everything else in the literature and the
only shape that points at the target line. Its limit is that `d` grows only quadratically in
verified height.

**(b) A uniform root-separation mesh.** **Iskander–Jain**, *Hyperbolicity of Appell polynomials of
functions in the δ-Laguerre–Pólya class*, Res. Number Theory **6** (2020),
[arXiv:2002.09906](https://arxiv.org/abs/2002.09906). A polynomial is `δ`-hyperbolic if its roots are
real, simple, and separated by at least `δ`; the `δ`-Laguerre–Pólya class is the local-uniform
closure of `δ`-hyperbolic polynomials. Their Thm 1.3 / Cor. 1.4 give hyperbolicity **for all `d ≥ 0`**
— genuinely uniform, because the mesh `δ` is `d`-independent *by construction* and `H_d` never
appears.

> **This is the only route to `d`-uniformity anyone has walked, and it has been executed only for
> Bessel-type special functions — never for an arithmetic sequence, never for a counting function,
> never for `Ξ`.** (Their target is the first term of the Hardy–Ramanujan–Rademacher expansion for
> `p_α(n)`, not `p(n)` itself.)

### 2.5 Nobody has uniformity for any natural sequence

Surveyed and confirmed `N(d)`-shaped without exception: `p(n)` (Chen–Jia–Wang `d=3` only;
Larson–Wagner effective with `N(d) ≤ (3d)^{24d}(50d)^{3d²}` — doubly exponential), modular form
coefficients (GORZ Thm 7), plane partitions (Ono–Pujahari–Rolen), unimodal sequences
(Banerjee–Bringmann–Kane, `d=3`), `k`-regular partitions (`d=3`), broken `k`-diamonds, cubic
overpartitions, Wright's-circle-method families (Bal–Haraldson–Males–Thompson). Where a result
covers all orders the threshold is per-order and non-effective or `d`-explosive; where a threshold is
small and explicit the order is fixed at 2 or 3.

**And it is provably unavoidable at that generality:** Kim–Lee's hypothesis class (real entire, order
`< 2`, zeros in a horizontal strip) *contains functions with non-real zeros*, so by Pólya no such
function has all Jensen polynomials hyperbolic — hence `N(d) → ∞` is forced for any theorem stated at
that generality. Ki says the same qualitatively: *"too general to control zeros of genuine zeta
functions."* **The `d`-direction cannot be closed by anything that is not specific to `Ξ`.**

## 3. The kernel side: our marginality screen is a theorem, and it is sharper than we stated

Round 4/5's marginality screen (`Ξ` is a boundary point, so mechanisms holding "with room to spare"
are wrong-shaped) turns out to have a rigorous kernel-side form we never wrote down.

**Newman 1976** (PAMS **61** 245–251) **completely characterized** the class `𝒫` of even nonnegative
measures whose Fourier transform stays real-rooted after multiplication by `e^{-bt²}` for *every*
`b > 0`:
`f(t) = K t^{2m} e^{-αt⁴-βt²} ∏_j (1 + t²/a_j²) e^{-t²/a_j²}`, with `Σ a_j^{-4} < ∞`.
Decay **no faster than Gaussian-quartic**. But `Φ(u) = O(e^{9u/2 - π e^{2u}})` decays **doubly
exponentially**. `Φ` misses this by an entire regime, not narrowly.

**The no-go, which is rigorous and which we had only as a heuristic screen:**

> Let `P` be any kernel criterion such that (i) `P(K)` implies `∫K cos(zu)du` is real-rooted, and
> (ii) `P` is stable under `K ↦ e^{-εu²}K` for some `ε > 0`. Then `P(Φ)` is **false** — otherwise
> `H_{-ε}` would be real-rooted, giving `Λ ≤ -ε < 0`, contradicting Rodgers–Tao.

**So no robust kernel criterion can ever verify RH.** Only *exactly critical* criteria — closed,
tight, zero slack — can work. This is the rigorous content of Newman's "if RH is true it is only
barely so," and it is the right general form of round 5's screen.

**Important corollary, to avoid a misreading:** `Φ`'s failure of Newman's criterion is *not* evidence
against RH. It is exactly equivalent to `Λ > -∞`, which is compatible with RH.

### 3.1 Total positivity is provably dead for `Φ` — my own thread, killed

I floated total positivity (Pólya frequency sequences, Aissen–Schoenberg–Whitney–Edrei) as the most
promising uniform-by-construction mechanism. **It is provably unavailable.** By Schoenberg, a Pólya
frequency function's bilateral Laplace transform is `1/ψ` with `ψ` of Laguerre–Pólya type, hence
zero-free where finite. `Φ`'s super-exponential decay makes `∫Φ(u)e^{-su}du = 2Ξ(is)` entire on all
of `ℂ`, and `Ξ` has infinitely many zeros. Contradiction.

> **`Φ` is PF₂ (log-concave) but provably not PF∞. Any program placing the Riemann `Φ` in a total
> positivity class is attempting something false.**

This also explains the failure mode of the one preprint occupying exactly that intersection
([arXiv:2602.01248](https://arxiv.org/abs/2602.01248), unrefereed, no affiliation): its kernel's
transform has `Ξ`'s zeros as *poles*, not zeros, and the "single remaining problem" of bridging the
reciprocal is the entire theorem.

### 3.2 What `Φ` does have — and a reversal of round 5's Lee–Yang dismissal

Unconditionally true of `Φ`, all theorems: **log-concave** (`V = -log Φ` convex); **`V'(t)/t`
increasing** (Csordas–Varga, Constr. Approx. **4** (1988) 175–198, settling a 1927 Pólya
conjecture); **`V'` convex on `[0,∞)`** (Newman, *The GHS inequality and the Riemann hypothesis*,
Constr. Approx. **7** (1991) 389–399).

That last one has a consequence round 5 got wrong. By Ellis–Monroe–Newman (CMP **46** (1976)
167–182), `V'` convex on `[0,∞)` is exactly the GHS condition, so:

> **The normalized Riemann kernel `Φ du / ∫Φ` is a bona fide GHS-class single-site spin measure, and
> RH is *exactly* a Lee–Yang statement: RH ⟺ `Φ du` lies in the Lee–Yang class of even single-site
> measures. Its one-site partition function `∫e^{hs}Φ(s)ds` **is** `Ξ`, and "all zeros on the
> imaginary `h`-axis" **is** RH.**

Round 5 recorded "the route terminates at Lee–Yang" as a *failed* closure on the grounds that
Lee–Yang has no gauge content. The gauge point stands (Elitzur forbids the local order parameter;
Fisher zeros are the wrong complex plane). But the framing understated the connection: RH is not
*analogous* to a Lee–Yang problem, it *is* one, exactly. And Simon–Griffiths (1973) locate the
failure precisely: `φ⁴` measures are Lee–Yang, `φ⁶` are not, Newman's class **is** `φ⁴`, and `Φ`
decays faster than quartic — a "super-confining" single-site potential, past where Lee–Yang is
automatic.

### 3.3 The one live kernel candidate

**Csordas' positive-definiteness of the derived kernels** `K_n(t; Φ_λ) = ∫Φ_λ(s+t)Φ_λ(s−t)(·)ds`
(Comput. Methods Funct. Theory **15** (2015) 373–391, [arXiv:1309.0055](https://arxiv.org/abs/1309.0055),
Open Problem 4.10: show failure for `λ < 0`). This is the most promising family found **precisely
because it is not obviously Gaussian-stable**, so it escapes the §3 no-go. Also still open and
necessary: the Laguerre inequality `L₁(x) = Ξ'(x)² − Ξ(x)Ξ''(x) ≥ 0` (Open Problem 4.7), verified
numerically only for `|x| < 1.09·10⁹`. That a *necessary* condition for RH at this level is unproven
is a sobering calibration of the program's reach.

## 4. Spectral realizations: Bombieri–Garrett is a quantitative no-go, not a slogan

Round 5 cited Bombieri–Garrett ([2002.07929](https://arxiv.org/abs/2002.07929)) for
"self-adjointness is permissive, not generative." The actual result is much stronger.

They construct designed pseudo-Laplacians whose discrete spectrum, if any, consists of `s(s−1)` for
zeros of `ζ_k` — so self-adjointness *does* force those onto the critical line (the permissive
half). The generative half fails for a *quantitative* reason: eigenvalue spacings for `T̃_θ` must
exceed roughly `(1/2 − ε)π/log T` by regularity of `arg ζ`, whereas Montgomery pair correlation
predicts ≈ **11.3%** of consecutive zero pairs are closer than that. Hence:

> **At most ≈ 94% of the zeros of `ζ` can appear among the spectral parameters of any *single*
> designed pseudo-Laplacian.** The Hilbert–Pólya program in this form cannot capture all zeros, no
> matter how the operator is designed.

Independently, Sierra's own review of the `xp` family concedes *"one needs to fine tune a parameter
to see each individual zero."* Two unrelated directions converging on **one operator per zero, not
one operator for all zeros**. (Bender–Brody–Müller is separately refuted by Bellissard,
[1704.02644](https://arxiv.org/abs/1704.02644): the momentum operator has deficiency indices
`n₊ = 1, n₋ = 0`, so admits no self-adjoint extension, and the claimed eigenfunction is not in the
stated space at `Re z = 1/2`.)

**Void:** nobody has asked whether the 94% ceiling can be evaded by a coherent *family* of
pseudo-Laplacians — a spectral sheaf over the `θ`-parameter — rather than a single operator, even
though both Bombieri–Garrett's `θ` and Sierra's fine-tuning are literally one-parameter families.
Nobody has run the Bombieri–Garrett spacing argument against a Davenport–Heilbronn control.

## 5. Three live targets, unscreened

### 5.1 Jensen polynomials of gauge-theoretic counting sequences — never attempted

> **Nobody has studied Jensen polynomials, Turán inequalities, higher-order Turán inequalities, or
> hyperbolicity for *any* gauge-theoretic counting sequence** — Nekrasov `Z_k`, Donaldson–Thomas,
> Pandharipande–Thomas, Gopakumar–Vafa, Vafa–Witten (the Johnston–Males paper treats VW *invariants*
> of K3, which is the closest, and even it is an `η`-quotient computation).

The technology is mature, the asymptotics are available to comparable precision from
modularity/wall-crossing, and the intersection is empty. Nearest existing foothold, and it is
suggestive: **Heim–Neuhauser, with Appendix B by Ken Ono**, *Dominant zeros of Nekrasov–Okounkov
polynomials*, [arXiv:2606.15394](https://arxiv.org/abs/2606.15394) — `NO_n(z)` has a unique zero of
maximal modulus, real, negative, simple, proved by realizing the zeros as eigenvalues of an explicit
nonnegative primitive Hessenberg matrix `M_n^h` and applying **Perron–Frobenius**. They explicitly do
*not* prove full real-rootedness or any total-positivity statement.

> **Concrete unasked question: is `M_n^h` totally nonnegative, and is `{A_{n,k}}` a Pólya frequency
> sequence?** They got *one* real zero from *nonnegativity*; all real zeros would need *total*
> positivity. Also open (Hong–Zhang, Res. Number Theory **7** (2021) 17): log-concavity of `A_{n,k}`
> is proved for `k ≪ n^{1/6}/log n` and monotonicity for `k ≫ √n log n`, with the intermediate range
> open.

Note this target survives §3.1's kill: the total-positivity obstruction applies to `Φ`, not to a
gauge-theoretic sequence. And per §2.5 it would be the first uniform-in-`d` result for any natural
sequence if it worked — which is also a reason for calibrated pessimism.

### 5.2 The unwalked chain to Nyman–Beurling

Every link below is published. **No paper traverses more than two.**

> Chern–Simons Stokes constants (integers, conjecturally DT invariants; Garoufalidis–Gu–Mariño)
> → resurgence → **quantum modular forms** (Garoufalidis–Zagier,
> [2111.06645](https://arxiv.org/abs/2111.06645), SIGMA **20** (2024) 055)
> → **McSpirit–Rolen** ([2505.00799](https://arxiv.org/abs/2505.00799)): *L*-function functional
> equations are the computational **input** to Stokes constants of quantum modular forms
> → **Bettin–Conrey** (*Period functions and cotangent sums*, Algebra & Number Theory **7** (2013)
> 215–256, [1111.0931](https://arxiv.org/abs/1111.0931)): quantum-modular-type period functions
> carry **Vasyunin sums**
> → Vasyunin sums are exactly the objects in the **Nyman–Beurling–Báez-Duarte–Vasyunin criterion for
> RH.**

Two things make this worth taking seriously. First, quantum modularity is the one place in the whole
landscape where **physics produces new arithmetic rather than consuming known arithmetic** — the
quantum modular form was invented because Chern–Simons asymptotics demanded it. Second, the chain
terminates at Nyman–Beurling, which is the RH criterion this project has never used and which is
structurally much more hospitable to a physical construction than Pólya's (a density statement in a
Hilbert space rather than a hyperbolicity statement about polynomials).

Nobody has asked whether Chern–Simons Stokes constants, read through McSpirit–Rolen, correspond to
any *L*-function at all. Caveat: integrality of the Stokes constants is conjectural, verified
numerically only for `4₁` and `5₂`.

### 5.3 The unused KP directions — and a hole in our own screen

This came out of the user's observation that operations may be trivial on a slice and nontrivial off
it. Applied to our own machinery it produces a concrete question, and it exposes a gap in round 5's
marginality screen.

Round 3 §3.1 recorded, without pursuing it: *"in the integrable-systems parametrisation the diagonal
is the Calogero–Moser momentum, left free, and pinning it to `Y_jj = Σ_{k≠j} 2/(z_j − z_k)` is
exactly the constraint that makes the `t₂` flow the heat flow."* Round 4 §3 then established that
the pencil identity is **Wilson's tau function** `τ(t) = det(X + Σ_{i≥1} i·t_i·Z^{i−1})` restricted
to `t₁ = z`, `t₂ = t`, rest zero.

So: the CM fibre over a given characteristic polynomial is a family of data all projecting to the
same polynomial, and **`t₃, t₄, …` — the higher KP flows — are entirely unused directions on an
object we have already verified.** They are nontrivial off the projection and trivial on it, in
exactly the user's sense.

> **The hole.** Rodgers–Tao gives `Λ ≥ 0` in the **`t₂` (heat-flow) direction**, and RH ⟺ `Λ = 0`
> makes `Ξ` a boundary point of the hyperbolic locus *in that direction*. Round 5's marginality
> screen then rejects any positivity mechanism holding "with room to spare" — but *with room to spare
> in `t₂`*. **A mechanism robust in a `t₃` or `t₄` direction is not refuted by Rodgers–Tao at all.**
> The screen has nothing to say about the higher flows, and we applied it as though it did.

Well-posed questions this generates, none of which the notes ever asked: do the higher KP flows
preserve hyperbolicity? Is there a DBN-type constant for each flow, and is `Ξ` marginal in those
directions or interior? Does the hyperbolic locus have a boundary point reachable in a `t_i`
direction where the margin does *not* collapse?

Independent corroboration that this region is empty: the sweep's own void list records that **nobody
has connected the Rodgers–Tao / DBN heat flow to any gauge-theoretic or instanton flow**, despite
both being one-parameter families of spectral configurations with a critical value at `t = 0`. Our
round-2 pencil result *is* that connection, and it remains unwritten.

## 6. Arithmetic gauge theory and `F₁`: the void has a structural reason

- **Minhyong Kim's arithmetic gauge theory has no RH contact**, by the practitioners' own accounting
  (the nLab "Relation to *L*-functions" section is an empty header; Kim's own ACS I calls it a
  "far-fetched possibility"). Its one genuine *L*-function result
  ([2207.03732](https://arxiv.org/abs/2207.03732), Bull. LMS **56** (2024)) concerns **`p`-adic
  valuations** of Kubota–Leopoldt `p`-adic *L*-functions, not zeros, and the authors state plainly:
  *"we do not achieve this goal."*
- **The dimension mismatch is the reason, not neglect.** Under Mazur–Kim–Reznikov, `Spec O_K` is a
  **3-manifold**, so the natural gauge theory is Chern–Simons — which is what Kim built. Donaldson
  and Seiberg–Witten theory is **4-dimensional**, and its lattice theorems concern `H²(X;ℤ)` on a
  closed 4-manifold. There is no arithmetic object in that role. Under Scholze's "`Spec ℤ` is
  3-dimensional" heuristic the product would be 6-dimensional, so even a constructed product need not
  invite 4-manifold tools. **My "four-manifold attached to ζ" framing from earlier this session was
  a rhyme presented as a bridge; this is the correct version.**
- **Connes–Consani *did* build the `C × C` analogue.** The square of the arithmetic site, with
  Frobenius correspondences `Ψ(λ)` and the proved composition law `Ψ(λ)∘Ψ(λ′) = Ψ(λλ′)`
  ([1502.05580](https://arxiv.org/abs/1502.05580), Adv. Math. **291** (2016) 274–329). What is
  missing, in their words: *"the definition of a suitable Weil cohomology which would allow one to
  understand the above equality as a Lefschetz formula"*; and for the Riemann–Roch strategy
  ([1805.10501](https://arxiv.org/abs/1805.10501)), *"an appropriate definition of the sheaf
  cohomology (as idempotent monoid) `H¹`"*, with the worst step being that *"in the lift from
  characteristic 1 to characteristic 0 one loses the automorphisms."*
  → **"Define `H¹` for the tropical/characteristic-1 structure sheaf on the square of the scaling
  site" is the single most precisely posed open problem the sweep found.**
- **Connes' 2026 position is that the live route is analytic, not intersection-theoretic.**
  Extremizing the Weil quadratic form on test functions supported on primes `< 13` produces
  approximations to the first 50 zeros (accuracy `2.6·10⁻⁵⁵` to `10⁻³`) that **provably lie exactly
  on `Re = 1/2`**. The unproved step is convergence, verbatim: *"This is something which at this
  point is not proved."* So the finite object is positive and on-line; the limit is the whole
  difficulty — **a different failure mode from the function-field case, where finite-dimensionality
  is free from cohomology.**
- **Calibrated pessimism about importing lattice positivity:** Grothendieck's **Hodge standard
  conjecture** — the positivity-on-an-integral-lattice statement — is still **open in characteristic
  `p`**, where RH is *proved*. Deligne routed around it. Positivity on an integral lattice appears to
  be *harder* than the weight statement it is meant to deliver.
- **Clean voids:** Donaldson diagonalizability, Furuta `10/8`, Rokhlin have **never** been pointed at
  arithmetic by anyone credible. No 4-manifold has been attached to `Spec ℤ`. Nobody has proposed
  importing lattice-signature technology into the Weil positivity problem — it has been attacked with
  operator theory only.
- **Function-field calibration:** Langlands there *does* yield RH-analogue statements (Drinfeld;
  L. Lafforgue, Invent. Math. **147** (2002) — Ramanujan–Petersson and Deligne purity), via Weil II
  on moduli of shtukas. Nothing touches `ζ` itself, because `ζ` has no motive carrying a Frobenius of
  the right kind. **Geometric Langlands is connected to RH exactly where the geometry exists, and
  blocked in our case by the missing geometry** — a structural reason, not neglect.

## 7. Also found, worth recording

- **`Ξ` as a physical object: producing it is cheap; the positivity is the whole problem.**
  Angelantonj–Cardella–Elitzur–Rabinovici ([1012.5091](https://arxiv.org/abs/1012.5091)) show the
  graded density of states of a stable closed-string vacuum has **zeta zeros as its oscillation
  frequencies**, with RH controlling a convergence rate — a legitimate published case, but the
  implication runs RH ⟹ physics. Remmen (PRL **127** 241602) likewise; and **Duhr–Kshirsagar**
  ([2303.09904](https://arxiv.org/abs/2303.09904), JHEP 08 (2023) 203) deflate it cleanly: the
  construction works for *any* even entire function with only real zeros, so it is Hermite–Biehler
  membership repackaged, with no arithmetic input or output. **This is the same "shape-matching
  transfers no information" failure as round 1's, in a new costume.**
- **No physical system in the literature has `Φ` as a density of states.** The available link is
  Lee–Yang/GHS, where `Φ` is a *single-site spin measure*, not a DOS. Unexploited observation:
  `θ(x) = Σ e^{-πn²x}` is the partition function of a free particle on a circle / the heat kernel on
  `S¹`, and `Φ` is built from `θ`-derivatives — no paper develops this into a model.
- **The positive Grassmannian / amplituhedron has never been connected to real-rootedness,
  hyperbolicity, or Lorentzian polynomials, or to number theory of any kind.** Karp's corpus confirms
  it from the other end; his `2110.02301` is *Wronskians, total positivity, and real Schubert
  calculus*, engaging real-rootedness only via Mukhin–Tarasov–Varchenko, with no Pólya frequency
  sequences and no coefficient sequences.
- **Effective Hermite asymptotics are not the bottleneck.** Shi–Nemes–Wang–Wong
  ([2109.01054](https://arxiv.org/abs/2109.01054)) give computable Plancherel–Rotach error bounds
  with `n`-independent constants; Krasikov ([math/0401310](https://arxiv.org/abs/math/0401310)) gives
  explicit non-asymptotic Hermite zero bounds. **The Hermite half of a GORZ-type argument is solved
  effectively; the arithmetic half is not.**
- **Certification complexity, relevant to whether uniform-in-`d` is plausible at all:** exponential
  lower bounds on spectrahedral representations in `d` (Raghavendra–Ryder–Srivastava–Weitz);
  coNP-hardness of stability testing from degree 3 (Chin). Generic convex-geometric certification is
  ruled out; structure-specific is not, with the Lorentzian-polynomial precedent showing a
  local-condition-propagates mechanism can exist.

## 8. Corrections to earlier rounds and to this session

1. **`arXiv:2204.05465` is Johnston–Males, not "Males–Ono et al."** (rounds 2 and 5 both wrong).
2. **The `d`-uniformity gap was mis-framed in rounds 2–4 and throughout this session** as an
   error-term-versus-root-gap tension. That is a property of the GORZ method. The gap is a change of
   quantifier order (§2.2), and the best threshold (Kim–Lee, `d^{1/2+ε}`) was obtained by abandoning
   asymptotics entirely. **The margin map and edge law measure the price of finite-`d` certificates
   along a direction that does not approach the target line.** Their value as measurements stands;
   their framing as "the critical path to RH" does not.
3. **Round 5's Lee–Yang dismissal understated the connection.** RH *is* a Lee–Yang statement exactly
   (§3.2). The gauge-content point stands.
4. **Round 5's marginality screen was applied more broadly than it licenses** — it is a statement
   about the `t₂`/heat-flow direction only (§5.3).
5. **My total-positivity suggestion this session is provably dead for `Φ`** (§3.1).
6. **My "four-manifold attached to ζ" framing was a rhyme presented as a bridge** (§6).
7. **Round 5's Bombieri–Garrett citation understated it**: there is a hard ≈94% ceiling (§4).

## 9. Not done

- **The nonlinear-hyperbolicity-preserver sweep died to an API error**, with its last output reading
  "This is a direct hit on nonlinear preservers. Let me fetch it." Unrecovered. This covered
  composition, finite free convolution, determinantal pencils, Mukhin–Tarasov–Varchenko Wronskians,
  tropical/amoeba maps, Graeffe iteration, **`q`-analogues of Pólya's criterion**, and quaternionic
  slice-regularity. The `q`-analogue question matters most: if a `q`-Pólya criterion exists, `q`-series
  objects (Nekrasov, Vafa–Witten, Chern–Simons) become admissible inputs rather than analogues.
  **Re-run this.**
- Two sweeps exhausted their 200-call web-search budgets; tails unswept were the 2024–26
  Maass-form/eta-quotient literature and a confirmatory pass on gauge-theoretic RH claims.
- Not verified: `Φ > 0` re-derived from scratch (load-bearing for §3); the exact constant in
  `Disc(H_n)`; DLMF §18.16(v) verbatim for the Hermite root gap (the `d^{-1/2}` figure is a standard
  computation, consistent with Krasikov's edge bounds, but not fetched).

## 10. Method note

The unscreened protocol worked and should be kept. Of the seven corrections in §8, five are to claims
I had *screened and accepted*, and the two most valuable findings (§2.2, §5.3) came from directions
that pre-screening would have closed — §2.2 because I was confident I knew the shape of the gap, and
§5.3 because the marginality screen appeared to cover it. The standing rule *"for every claim that X
cannot happen, run the control that would show X happening"* needs a companion: **when a screen is
inherited rather than re-derived, re-derive it before applying it to a new candidate.**

---

**Sources.** Full citation lists are in the six sweep reports. Principal: Johnston–Males
[2204.05465](https://arxiv.org/abs/2204.05465) (Proc. Edinb. Math. Soc. 66 (2023) 845) · GORZ
[1902.07321](https://arxiv.org/abs/1902.07321) (PNAS 116 (2019) 11103) · GORTTW
[1910.01227](https://arxiv.org/abs/1910.01227) (Adv. Math. 2022) · Kim–Lee
[2105.05386](https://arxiv.org/abs/2105.05386) (JKMS 2022) · Iskander–Jain
[2002.09906](https://arxiv.org/abs/2002.09906) (Res. Number Theory 6 (2020)) · Ki, Oberwolfach OWR
2022/13 · Larson–Wagner [1904.12727](https://arxiv.org/abs/1904.12727) · Chen–Jia–Wang
[1706.10245](https://arxiv.org/abs/1706.10245) · Newman, PAMS 61 (1976) 245 · Newman, Constr. Approx.
7 (1991) 389 · Newman–Wu [1901.06596](https://arxiv.org/abs/1901.06596) (Bull. AMS 57 (2020)) ·
de Bruijn, Duke 17 (1950) 197 · Csordas–Varga, Constr. Approx. 4 (1988) 175 · Csordas
[1309.0055](https://arxiv.org/abs/1309.0055) · Ellis–Monroe–Newman, CMP 46 (1976) 167 ·
Simon–Griffiths (1973) · Rodgers–Tao [1801.05914](https://arxiv.org/abs/1801.05914) · Bombieri–Garrett
[2002.07929](https://arxiv.org/abs/2002.07929) · Bellissard
[1704.02644](https://arxiv.org/abs/1704.02644) · Heim–Neuhauser–Ono
[2606.15394](https://arxiv.org/abs/2606.15394) · Hong–Zhang
[2008.10069](https://arxiv.org/abs/2008.10069) · Garoufalidis–Zagier
[2111.06645](https://arxiv.org/abs/2111.06645) · McSpirit–Rolen
[2505.00799](https://arxiv.org/abs/2505.00799) · Bettin–Conrey
[1111.0931](https://arxiv.org/abs/1111.0931) · Connes–Consani
[1502.05580](https://arxiv.org/abs/1502.05580), [1805.10501](https://arxiv.org/abs/1805.10501),
[2006.13771](https://arxiv.org/abs/2006.13771) · Connes
[2602.04022](https://arxiv.org/abs/2602.04022) · Kim
[1510.05818](https://arxiv.org/abs/1510.05818), [2207.03732](https://arxiv.org/abs/2207.03732) ·
Lorscheid [1801.05337](https://arxiv.org/abs/1801.05337) · Deninger
[0709.2801](https://arxiv.org/abs/0709.2801) · Milne, *RH over Finite Fields* · L. Lafforgue, Invent.
Math. 147 (2002) · Angelantonj et al. [1012.5091](https://arxiv.org/abs/1012.5091) ·
Duhr–Kshirsagar [2303.09904](https://arxiv.org/abs/2303.09904) · Karp
[2110.02301](https://arxiv.org/abs/2110.02301) · Shi–Nemes–Wang–Wong
[2109.01054](https://arxiv.org/abs/2109.01054) · Krasikov
[math/0401310](https://arxiv.org/abs/math/0401310).
