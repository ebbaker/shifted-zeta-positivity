# Quasi-RH ⇒ RH: what three days taught, and where to go next

11 October 2026. Prepared for Edward Baker. Model: Claude Fable 5.1
(`claude-fable-5-1`), Anthropic, in Claude Cowork. This is a brainstorm,
not a result: nothing below is proved, and every "direction" is a
proposal with a first bounded test and a kill criterion attached. It
draws on the external reviews of all seventeen `newman_collisions`
projects (10–11 October), a structured digest of the four arithmetic
lanes and of `quasi-rh-character-amplification`, and the
`prime-variance-exponents` manuscript. Written with substantial LLM
assistance; the author is responsible for what is adopted.

The program's question: assume a zero-free strip `Re s > σ₀` for ζ (or
for the Hecke family over `Q(√−3)`), with `σ₀ = 11/12` (Oct-5 preprint)
or `7/8` (Sept-30 preprint), and derive RH. Two routes were pursued:
arithmetic exponent descent (make the strip shrink by a self-improving
estimate) and heat-flow collision exclusion (show the de Bruijn–Newman
constant `Λ` is 0).

## 1. Six design rules, each paid for

These are the facts the reviews established. Any new direction should be
checked against them before a line is written.

**R1. No shape-only argument can work.** The kernel
`q_{T,b}(u) = e^{−Tu²}[φ(u)/2 + φ(u−2b)/4 + φ(u+2b)/4]`, `φ = e^{−cosh u}`,
is positive, even, super-exponentially decaying, has all its zeros in a
bounded strip (so it satisfies "quasi-RH"), and has de Bruijn–Newman
constant exactly `T > 0` (so it violates "RH"). Every heat-side mechanism
that used positivity, evenness, decay, moment signs, Laguerre/stationary
signs, radial positivity, Ward identities, memory positivity, or
transport certificates is satisfied by this kernel. The arithmetic input
must be something this kernel lacks: the Euler product, or the specific
Dirichlet coefficients, or the zero density growing like `log x`.

**R2. The Laguerre identity makes every pointwise sign test a tautology.**
`H_x² − H·H_xx = H² Σ_ρ (x−ρ)⁻²`. At an all-real time every stationary
sign holds automatically; the threshold-jet expression equals
`72W²Σ(x−ρ)⁻² > 0` at any all-real double zero; the two-sign criterion on
`(0,∞)×ℝ` is equivalent to RH; the bounded-loss and Hölder-loss criteria
are equivalent to "no joint zero" by a two-line continuity argument. None
of these is a reduction. The only content of any of them is the
precursor statement "no near-real complex pair is visible", which is RH
again.

**R3. Coherent rows carry the whole signal.** In every arithmetic lane the
conditional step consumed its own conclusion on the rows where the family
character is trivial (the `a = 1` row of the quadratic lift; the
sixth-power rows `u = r⁶` of the short families; the boundary-zero modes
of the fixed-scale recurrence). Any hypothesis stated as a family moment
must be tested first by restricting it to those rows; if the restriction
already implies the conclusion, the hypothesis is a restatement.

**R4. The supremum is attained as a bound, not as a zero.** The least
admissible variance exponent `δ*` exists, but zeros may approach the edge
of the strip only at unbounded height. The fixed-scale recurrence
`E(X) ≤ qE(X/b) + CX^{−η}` is provably false when a boundary zero exists
(the edge-mode mean identity cancels exactly), and provides no handle when
it does not. Any descent has to control what happens at unbounded height
with no zero on the edge.

**R5. Below `|x| ≤ 6·10¹⁰`, `t ≤ 0.2`, every zero of `H_t` is real and
simple** (Polymath 15's barrier plus Platt). No numerical probe in that
box can see a collision, and every "certified sign" there is a corollary
of known results. Computable probes of the "opposite sign" at those
heights will always return the sum-of-squares sign, as 09's scan and 13's
pilot did.

**R6. Quasi-RH at the claimed strengths buys less than one expects.**
See section 2. In the heat lane it buys nothing at all.

## 2. What the hypothesis actually provides

| Consequence of `Re ρ ≤ σ₀` | at `σ₀ = 11/12` | at `σ₀ = 7/8` | already known unconditionally |
| --- | --- | --- | --- |
| de Bruijn strip `|Im z| ≤ δ = 2(σ₀−1/2)` | 5/6 | 3/4 | `< 1` |
| `Λ ≤ δ²/2` | 0.347 | 0.281 | `Λ ≤ 0.2` (Platt–Trudgian) |
| critical-line growth via convexity from the strip, exponent `(σ₀−1/2)/2` | 0.208 | 0.188 | 13/84 ≈ 0.155 (Bourgain) |
| zero density `N(σ₀, T)` | 0 | 0 | `≪ T^{0.19}` / `T^{0.29}` (Guth–Maynard) |
| `ψ(x) − x`, `M(x)` | `≪ x^{11/12+ε}` | `≪ x^{7/8+ε}` | `x·exp(−c(log x)^{3/5})` |

Three readings. (i) The heat lane gains nothing from the hypothesis: the
de Bruijn bound only beats 0.2 for `σ₀ < 0.816`. Everything done in
`newman_collisions` was an unconditional attack on `Λ = 0`, which is RH
itself, with no intermediate milestone available (section 1, R2). (ii)
The hypothesis is weaker than Bourgain on the line and barely stronger
than Guth–Maynard on density; what it uniquely provides is a *power
saving in prime and Möbius sums*. Any descent must consume that power
saving and nothing else. (iii) A zero-free strip is, at the level of
prime sums, equivalent to `M(x) ≪ x^{σ₀+ε}`; "descent" means a
self-improving inequality for the Möbius exponent, which is exactly the
kind of bootstrap that does not exist in the literature for a single
L-function. Known strips come from positivity across a family (Deuring–
Heilbronn-type repulsion) or from geometry (Deligne), never from a local
bootstrap. That is the real reason the lanes stall.

## 3. Where the lanes stand, in one paragraph each

**Heat lane (01–17).** Closed. Every mechanism is correct and none is
load-bearing. What survives: the sum-of-squares identity, the control
kernel of R1, 13's validated interval evaluator, and Note 20's explicit
Riemann–Siegel correction (residual `3·10⁻⁷` against `10⁻²`).

**Fixed-scale descent.** The recurrence is contradicted by the edge-mode
identity whenever a boundary zero exists and gives nothing when none
does. The scalar form with the Vaughan decomposition isolates "the signed
cross-scale term after both cutoffs", which is the Möbius bootstrap
restated.

**Integer quadratic lift.** The family moment `𝒲_h ≪ X^{1+h/2+ε}` would
give boundary `1/2 + h/4` for every odd-conductor quadratic L-function;
its `a = 1` row is the ζ conclusion. The entrywise majorant is `≫ X²` for
every `h`. The missing saving at `h = 7/5` is `7/40`, in a signed sum over
separated prime pairs.

**Short sextic families.** Finite extraction is proved; the moment target
`𝔐 ≪ D^{h+a}` with `a + 5h/6 < 3/4` is needed against a sieve floor of
exactly 1; the sixth-power rows alone already force the conclusion; the
complete-cofactor obstruction shows block energy `D^{16/15}` against a
`D^{4/5}` budget, with compensation required across total products to
relative accuracy `D^{−2/15}`.

**Mixed character families.** A 1/700 fourth-moment saving and a 1/5000
second-moment saving are the two targets; the entire proved structure
(thirty-two notes) rests on about twenty imported lemmas from the Sept-30
preprint; the aggregate two-row covariance with actual phases is open and
every absolute, marginal, Hölder, and entrywise route misses it by a
fixed amount (`6.7·10⁻⁵` to `0.23`).

**Character amplification.** Geometry alone gives `7/8 − 1/24000`, with a
hard stall at `0.8749572` for the current parameter family. The next
candidate needs the mixed lane's 1/5000. Everything is conditional on the
same imported lemmas.

The common shape: the open estimate is always "beat the large sieve by a
fixed power for Möbius-weighted sums over a family of length comparable
to the conductor", which, for individual members, is a zero-free strip
for that member. So the arithmetic lanes are asking the external
preprints' question again, one level down.

## 4. Directions

Ordered by expected value. Each has a first bounded test and a kill
criterion; none claims to be a route to RH unless it says so.

### D1. Find the family-to-individual engine in the external proofs

*Idea.* A family method (large sieve, moments, cubic theta) naturally
yields "all but `T^ε` members are zero-free in the region". A claim of a
zero-free strip for *every* member — which is what both preprints assert
— requires an additional mechanism that converts family information into
individual control: either a Deuring–Heilbronn-type repulsion (an
exceptional zero of one member forces the others away, through positivity
of an Euler-product expression), or an amplifier that isolates one member
without losing the saving, or something new. Whatever it is, it is the
only candidate for a "descent engine" that exists anywhere in this
program, because it is the only place where a strip for an individual
L-function is (claimed to be) produced from averages.

*Why it survives R1–R4.* It is not a mechanism proposal; it is a question
about the one object the lanes import but have not understood
structurally. The repository's audits checked local algebra, masks and
exponents; none asked "which step makes the statement hold for the
trivial character?"

*First bounded test.* Write a one-page proof skeleton of the Sept-30
Theorem 1.1 and the Oct-5 Theorem 1.1 with every lemma labelled as
(family average) / (individual) / (conversion), and identify the
conversion step and its positivity input. Then ask: does that step
iterate? If the conversion is repulsion from a hypothetical bad zero, the
iteration is the Deuring–Heilbronn ladder and its limit is computable. If
the conversion is absent, the premise of the whole program is in doubt
and the audits should say so.

*Kill criterion.* The conversion step is an application of the large
sieve to a row that is itself the trivial character (the R3 trap), or it
relies on an estimate the preprint does not prove.

*Promise.* High as a diagnostic; it decides whether the program has a
foundation. Cost: one careful reading, no new mathematics.

### D2. A model-first discipline, as a tool, not a slogan

*Idea.* Turn the "hypothesis equals conclusion" finding into an automatic
gate. Every proposed hypothesis `H` must pass three model tests before a
reduction is written: (a) on the random multiplicative model (Rademacher
`μ`), `H` should hold with high probability — if it fails there, it is
false for generic arithmetic; and the conclusion should *not* follow from
the model's square-root cancellation alone — if it does, `H` is
RH-strength; (b) on the control kernel of R1 and the Gaussian controls,
any "sufficient criterion" must fail — if it holds, the implication is
false; (c) restricted to the coherent rows (R3), `H` must not already
imply the conclusion.

*Why it survives.* It is what the reviews did by hand for seventeen
folders. The repository's culture of exact checkers makes it natural to
encode.

*First bounded test.* A standard-library script that takes a family
moment hypothesis in a declared normal form (row set, weight, exponent)
and evaluates it on the coherent rows symbolically, reporting whether the
coherent-row restriction implies the stated conclusion. Run it on every
target in section 3; the expected output is "restatement" for all of
them, which is the point.

*Kill criterion.* None; this is infrastructure. The cost is a day.

### D3. A function-field testbed for the descent structure

*Idea.* Over `F_q[T]` the Möbius family moments the lanes need are
theorems (Katz equidistribution, Keating–Rudnick-type variance results in
the large-`q` limit), and all zeros are known exactly. This is the one
setting where one can check, with no unproved input, whether the
*reduction structure* — finite extraction, the descent map
`θ ↦ T_a(θ)`, the fixed-scale recurrence — actually does what it is
supposed to do. The reviews already found one thing the testbed will show
immediately: for a geometric L-function every zero sits on the boundary
`δ = 0`, so `E_δ(X)` is periodic in `log X` with period `log q` and the
recurrence `E(X) ≤ qE(X/b) + …` holds with `q = 1` only, confirming the
edge-mode obstruction of R4 in a world where RH is true.

*Why it survives.* It does not propose a mechanism; it tests whether the
existing ones are even consistent with a known RH world. If a reduction
fails in `F_q[T]` with its inputs granted, it cannot work over `Q`.

*First bounded test.* Take Dirichlet L-functions modulo a polynomial of
degree `d`, write the analogue of the short-family moment with the proven
large-`q` asymptotic, and run the finite-extraction theorem. Record what
boundary it outputs and whether the sixth-power rows are doing the work.

*Kill criterion.* The analogue of the short-family target is not implied
by equidistribution at the relevant row length (then the testbed is not
informative at that `h`); or the extraction outputs exactly the input
boundary (then it is a restatement there too, and over `Q` as well).

*Promise.* Moderate as a diagnostic; zero as a route (RH is known there).

### D4. A real, unconditional deliverable: push `Λ ≤ 0.2` with the verified machinery

*Idea.* The de Bruijn–Newman bound is a *frontier* quantity:
`Λ ≤ t₀(X)` where `X` is the RH-verification height and `t₀(X)` is the
time at which the `n = 1` term of the approximant dominates for all
`x ≥ X` — roughly `κ = tL ≈ 5`, i.e. `t₀ ≈ 5/L(X)`. At `X = 6·10¹²`,
`L ≈ 27`, so the ceiling of this method is about `0.19`; Platt–Trudgian's
`0.2` is near it. Two ways to go below: raise the verification height, or
sharpen the reality criterion beyond first-term dominance. Note 20's
corrected interface (residual `O(Z/N)` instead of `O(Z)`) and 13's exact
interval evaluator are exactly the tools for the second: certify, for
`x ≥ X` at a time `t < t₀`, that `H_t` has the Riemann–von Mangoldt number
of real simple zeros using the sharper error, and redo the barrier at
`X ≈ 6·10¹²` (`N ≈ 7·10⁵` terms; the 22066-term cells took 1–2 minutes,
so a barrier strip of width 1 in `x` over `t ∈ [0, t₀]` is a few CPU-days
with the present code, less with Arb).

A note on a mechanism I considered and discarded: the zero dynamics
`ż_j = 2Σ_{k≠j}(z_j − z_k)⁻¹` give, for a complex pair `a ± ib`,
`ḃ = −1/b − 2bΣ_k((a−x_k)² + b²)⁻¹`, so the surrounding real zeros, at
density `L/4π`, drive a pair to the axis in time `O((log L)/L)` — this is
the physics behind first-term dominance, and with window-guaranteed zero
counts (explicit `S(T)` bounds) it is numerically *weaker* than
dominance at every height. It is not a new lever. Also discarded: a
reverse de Bruijn bound tying the strip width to `Λ` (`z³ − 3z` under
forward heat has zeros at `±i√(6s−3)`, beyond `√(2s)`), so "`Λ` small"
and "strip narrow" are not equivalent.

*Why it survives.* It makes no RH claim. It uses the only verified
assets the heat lane produced, for the one purpose they are good at.

*First bounded test.* Reproduce Polymath's barrier at `X = 6·10¹⁰` with
the corrected interface and measure how far below `0.22` the dominance
threshold moves. If the gain is under `0.01`, stop.

*Kill criterion.* The corrected interface lowers `t₀(X)` by less than the
cost of the barrier recomputation justifies; or the reality-for-all-`x ≥ X`
argument cannot be made analytic (it must hold for every height, not a
window; Polymath's Section 8 is the template).

*Promise.* Moderate and real: a published number, improvable, not RH.

### D5. Name the arithmetic problem once and stop reducing it

*Idea.* Every lane's open estimate is an instance of: for a family `𝓕`
of characters of conductor about `Q` and a Möbius-weighted Dirichlet
polynomial of length `N ≍ Q^h` with `h < 1`,
`Σ_{χ∈𝓕} |Σ_{n≤N} μ(n)χ(n)w(n)|² ≪ Q^{1+h−c}` with a fixed `c > 0`. The
large sieve gives `c = 0`; for an individual `χ` a power saving is a
zero-free strip for `L(s,χ)`. Write this once, as the program's open
problem, with the three parameterizations (quadratic lift, short sextic,
mixed) as special cases, and survey what is known: nothing beyond the
large sieve for `h < 1` with Möbius weights, as far as I know; power
savings without Möbius (Burgess-type) exist and are of a different nature;
Matomäki–Radziwiłł-type savings are `o(1)`, not powers.

*Why it survives.* Thirty-two mixed notes and twenty-nine short-family
notes produced reductions of this problem to itself with explicit
constants. A single statement of the problem, with its known tools and
their limits, is worth more than the next reduction.

*First bounded test.* The document. Then one literature search for any
`c > 0` result in this shape for any family and any `h < 1`.

*Kill criterion.* A `c > 0` result exists in the literature for a family
the lanes could use (then it should be imported and the descent map run
once, honestly); or none exists (then the lanes should be closed with
the problem stated).

*Promise.* High as hygiene; it is the honest end state of the arithmetic
lanes.

### D6. Checkable consequences of the imported lemmas

*Idea.* The amplification and mixed lanes import about twenty lemmas
from the Sept-30 preprint and treat them as axioms. Before building more
on them, derive one *qualitatively new, independently checkable*
consequence that they should imply easily — for instance a zero-density
estimate `N_𝓕(σ,T)` for the Hecke family in the strip, or a bound on
`Σ_χ |L(1/2+it,χ)|⁴` of the strength the moment lemmas suggest — and
compare it with what is known unconditionally (Guth–Maynard; standard
fourth moments). If the imports imply something false or implausibly
strong, the foundation is wrong; if they imply something new and
plausible, that consequence is itself a result worth stating.

*Why it survives.* It tests the premise rather than extending it.

*First bounded test.* From the imported Lemma 18.1 (plain fourth at
`κ = 3/4`) and the reflection lemmas, write down the family density bound
they give at `σ = 7/8` and at `σ = 3/4`; compare with Guth–Maynard's
`T^{30(1−σ)/13}`.

*Kill criterion.* The imports imply a density bound strictly stronger
than anything known with no new idea visible (suspect), or a bound weaker
than known (then they cannot be giving an individual strip either).

*Promise.* Moderate; cheap; decisive either way.

### D7. What the heat lane can still say about RH: a precise negative

*Idea.* State, as a theorem of the program, why the heat route cannot
yield RH: a collision at time `Λ > 0` is a pointwise event at one unknown
height; excluding it is a pointwise *lower* bound on the joint first jet
`(F_{t,N}, F'_{t,N}/L)` of a Dirichlet polynomial with coefficients 1,
simultaneously small at one point; measure-theoretic small-value
estimates cannot exclude a measure-zero set; and by R1 no kernel-shape
property can. The only way through would be a theorem about the Dirichlet
polynomial `Σ_{n≤N} n^{−1/2−iT}` that is false for generic smooth-weight
sums, and no such theorem is known or proposed.

*Why it survives.* It is a closure statement, and it prevents a fourth
day of lifts.

*First bounded test.* A one-page note in `newman_collisions/notes/`
collecting R1, R2, R5 and this paragraph, with the three reusable assets
listed.

*Promise.* None toward RH; high as a stop sign.

## 5. Wild cards, labelled as such

These are ideas I could not kill in an hour and could not make concrete
either. They are recorded so they are not re-invented.

*Li's criterion under quasi-RH.* An off-line zero `1/2 + a₀ + iγ₀` makes
`λ_n < 0` for some `n ≲ γ₀² log γ₀ / a₀`. Quasi-RH bounds `a₀` from above,
which is the wrong direction for detection; nothing descends.

*Weil positivity with limited support.* For `h = g * g̃`,
`ĥ(ρ) = ĝ(ρ)·conj(ĝ(1−ρ̄))`, and the two factors at an off-line zero are
`e^{+aL/2}` and `e^{−aL/2}` in size, so off-line zeros do not blow up the
Weil functional exponentially; a strip hypothesis therefore does not
truncate the positivity problem. Weil positivity is RH-or-nothing.

*Nyman–Beurling with weights.* A zero-free strip is equivalent to a
weighted approximation statement; the decay rate of the distances
`d_N^{(σ)}` is in principle computable and tied to zeros near the edge.
A descent here is a statement about rates, which is R4 in another
language. Possibly worth one numerical look, not more.

*Statistics in reverse (Rodgers–Tao).* `Λ ≥ 0` was proved from the
regularity that `Λ < 0` would force on all zeros. `Λ > 0` forces nothing
global — a single complex pair is statistically invisible — so there is
no mirror argument.

## 6. Stop list

Lifts of the heat flow (any kind); stationary-sign or threshold-jet
calibrations below `x = 6·10¹⁰`; transport/multiplier constructions;
further rewritings of `K`, `−H'H'''`, or Laguerre expressions in new
coordinates; reductions of a family moment to itself with explicit
constants; parameter re-optimization of the amplification geometry past
its stall; any "sufficient criterion" not first tested against the
control kernel of R1.

## 7. What is worth writing up regardless

The fixed-probe equivalence theorem (`prime-variance-exponents`), on its
own, as a short unconditional note. The explicit Riemann–Siegel
correction with its holomorphic surrogate and the validation table against
`ξ` (project 17, Note 20), as a computational note. The sum-of-squares
form of the threshold test and the control kernel with Newman constant
exactly `T`, as remarks in the stable heat manuscript. The interval
evaluator and its certificates, as reproducible infrastructure — and, if
D4 succeeds, a new upper bound for `Λ`.
