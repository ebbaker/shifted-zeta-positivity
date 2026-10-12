# Cross-assessment of the two brainstorms, and what is still missing

11 October 2026. Prepared for Edward Baker. Model: Claude Fable 5.1
(`claude-fable-5-1`), Anthropic, in claude.ai. Written with substantial
LLM assistance; the author is responsible for what is adopted. This note
adjudicates between the [Claude brainstorm](NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md)
and the [Codex brainstorm](NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md),
read against GitHub `main` at `779af62` ("More brainstorming from
ChatGPT"), the external reviews
[12](../newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md)
and [13](../newman_collisions/17_enlarged_state_transport/reviews/13_EXTERNAL_REVIEW_ADDENDUM_NOTES_9_TO_22_CLAUDE_20261011.md)
of project 17, and the Polymath 15 paper (arXiv:1904.12438v2), which I
read in full for this note. Section 6 lists what was checked and how.
Nothing here is a result; one item (section 3.1) is a correction to a
fact the external reviews relied on.

## 1. Verdict

The two brainstorms agree on the only conclusion that matters: another
reformulation is not progress unless it supplies an estimate that was
missing before, and the heat lane and the arithmetic lanes should both
stop until such a source is named. That conclusion is consistent with
reviews 12 and 13 and I endorse it.

Where the Codex note corrects the Claude note, it is right in every case
I could check, and three of the corrections are decisive for what to do
next: the proposed "common open problem" D5 is false as stated (section
3.3); the "every zero below `6·10¹⁰` is real for `t ≤ 0.2`" fact is
stronger than what Polymath 15 proves (section 3.1); and the unconditional
`Λ` deliverable D4 is stale, because three public claims below `0.2`
already exist at the same verification height (section 3.2). The Codex
order of deliverables (source audit, moment ledger, interface benchmark,
function-field experiment, density/Weil calculations) should be adopted,
with the modifications in section 5.

What neither note does: name a single explicit property of the theta
kernel that the counter-kernels lack and that a proof could use. Section
4.1 records the one such property I found in the Polymath paper
(solidification, Theorem 1.5), shows that the two existing control
families split it from zero density, and states the bounded test this
leaves.

## 2. Adjudication of the Codex corrections

| Claude claim | Codex correction | Finding | How checked |
| --- | --- | --- | --- |
| D5: common target `Σ_{χ∈𝓕}\|Σ_{n≤N}μ(n)χ(n)w(n)\|² ≪ Q^{1+h−c}` | False for the full family: orthogonality gives `(q−1)Σ\|a_n\|²` when `N < q` | Correct. The diagonal alone is `≍ qN` for `w = 1`; the same holds for the full quadratic family, since `μ(m)μ(n) ≠ 0` with `mn` square forces `m = n`. The target must name the sparse family, the weights and whether the diagonal is subtracted | Exact: `q = 101`, `N = 40` gives `2600 = (q−1)·26` |
| R1: the arithmetic input could be "zero density growing like `log x`" | The counter-kernel already has it: `J_T(z) = 2K_{iz}(1)cos²(bz)`, zeros of `K_{iν}(1)` have counting function `~ R log R/π` | Correct. Zeros of `K_{iν}(1)` in `ν ∈ (0, 60)`: 72 observed; `(R/π)log(2R/e) = 72.4`; leading term `R log R/π`, which after the `z/4` rescaling is the theta rate `R log R/(4π)` | mpmath sign count; Debye asymptotic |
| R5 / reviews' fact (D): all zeros of `H_t` with `\|x\| ≤ 6·10¹⁰` are real and simple for `0 ≤ t ≤ 0.2` | The barrier only excludes zeros above `y₀ = 0.2`; a complex pair below it is not excluded | Correct, and sharper than Codex states; see 3.1 | Polymath Prop. 3.3 and Prop. 3.1(ii), read directly |
| D4: `t₀ ≈ 5/L(X)` is the ceiling of the barrier method; the task is "push `Λ ≤ 0.2`" | Heuristic, not a ceiling; public claims of `0.1787854`, `< 0.158`, `0.1779…` exist | Correct, and the claims are real (section 3.2) | Web: Gomila repository and exposition; Gordon repository; arXiv:2609.37164 |
| D6: test Lemma 18.1 at `κ = 3/4` against Guth–Maynard | The positive-slot case already assumes `β* ≤ 7/8`, so it is not an independent test | Correct; the repository's own ledger says the same ("a zeta-only seven-eighths assumption does not satisfy the positive-slot hypothesis in item 4") | `quasi-rh-character-amplification/notes/GEOMETRY_CONDITIONAL_THEOREM_AND_DEPENDENCY_LEDGER_20261009.md` |
| Weil wildcard: the factors `e^{±aL/2}` cancel, so off-line zeros do not blow up the Weil functional | Two translated packets give `G(ρ)·conj G(1−ρ̄) = −4Φ(a)²sinh²(aL/2)` | Correct; the two-packet identity is exact for any even nonnegative `φ`. The conclusion survives: the detector costs `exp(L/2)` on the prime side and needs a lower bound `a ≥ a_min`, which quasi-RH does not give | Symbolic (sympy, Gaussian `φ`) and by hand for general `φ` |
| D3: over `F_q[T]` the normalized variance is periodic in `log X` with period `log q` | Quasiperiodic (sums of `e^{inθ_j}`), not periodic | Correct. The edge-mode obstruction of R4 survives, since a non-decaying quasiperiodic `E` still contradicts `E(X) ≤ qE(X/b) + CX^{−η}` with `q < 1` | Reasoning only |
| D7: a theorem that the heat route cannot yield RH | A no-go must name its inputs; regularity turns a point event into a positive-measure set | Correct in principle; the persistence calculation (Codex §7) is right, `det D_{(t,x)}(H, H_x) = H_xH_xxx − H_xx² = −H_xx²` at a double zero, and it shows the needed small-value estimate must beat the generic `ε²` order or constant. Codex's own "low priority" label is right | Symbolic |
| "Hypothesis equals conclusion" as a gate (D2, R3) | Equivalence on the coherent rows is not circularity; classify as impossible / equivalent on the restricted rows / stronger / supplied by an independent theorem | Agreed. The reviews' finding is the empirical one: every *proposed source* for a family estimate in this program so far landed in the second class. Codex's four-way label is the right standard for the ledger | — |

## 3. Three corrections that outlive the brainstorms

### 3.1 Fact (D) is not what Polymath 15 proves; here is what is

Reviews 12 and 13 state, and the Claude brainstorm repeats as R5, that
every zero of `H_t` with `|x| ≤ 6·10¹⁰` and `0 ≤ t ≤ 0.2` is real and
simple, "Polymath 15 barrier + Platt". The theorem actually proved
(Prop. 3.3 of arXiv:1904.12438) is: for `0 ≤ t ≤ t₀`, there is no zero
with `0 ≤ x ≤ X` and `y ≥ Y(t) = (y₀² + 2(t₀ − t))^{1/2}`. At `t = t₀ =
0.2` this excludes `y ≥ 0.2` and nothing below it. The argument cannot be
pushed to `y₀ → 0`: the comparison `Im ż_j < Ẏ = −1/Y` in the proof needs
`Y > 0`, and hypothesis (iii) must be verified numerically down to `y₀`.

What is true, and is enough for most of what the reviews used it for:

1. At `t = 0`, every zero with `|x| ≤ 6·10¹²` is real and simple
   (Platt–Trudgian).
2. A real simple zero stays real for all later `t`. By Prop. 3.1(ii), an
   `m`-fold zero at `(t₁, z_j)` resolves for `t > t₁` into
   `z_j + √2(t − t₁)^{1/2}λ_k` with real Hermite roots `λ_k`, and for
   `t < t₁` into the same with an imaginary square root. So a double real
   zero at `t₁` was a complex pair just before `t₁`, never two real
   zeros; real zeros cannot merge in forward time, and by `H_t = H_t^*`
   they cannot leave the axis without merging. (Collisions with an
   incoming pair, `m = 3`, leave the real zero real.)
3. Therefore the only possible non-real zero of `H_t` at `|x| ≤ X` for
   `t > 0` is one that entered from `|x| > 6·10¹²`. No cited theorem
   bounds how far a complex zero can travel in time `0.2`; Theorem 1.5
   is ineffective in `C`, and the Polymath canopy argument only controls
   `y ≥ y₀`.

Consequences. Every "unconditional corollary of (D)" in reviews 12 and
13 (the `N = 22066` cell, the Note-15 window, the Note-19/20/22 cells, all
at `x ≈ 6.1·10⁹`) is unconditional given (1), (2) and the additional
statement "no complex zero travels from beyond `6·10¹²` to within `O(1)`
of `6.1·10⁹` in time `≤ 0.2`". That statement is overwhelmingly plausible
(average speed `3·10¹³` against a typical `O(log x) ≈ 25`) and, as far as
I know, unproved. The verdicts of reviews 12 and 13 do not change: the
certified signs still certify nothing about collisions, and the point
that the probes sit where known results make the sign a foregone
conclusion survives in the form "where (1)–(2) plus a mild unproved
velocity bound make it a foregone conclusion". The closure note should
state (D) in this three-part form, and an erratum line should be added
to reviews 12 and 13 (as a dated addendum, not an edit of the historical
text). A proof of the velocity bound, if it is easy, would be a small
unconditional lemma worth having; I did not find one in an hour.

### 3.2 D4 is stale, and the heat consequence of quasi-RH is publicly exhausted

Three public, not peer-reviewed claims below `Λ ≤ 0.2` were available on
11 October 2026: Gomila, `Λ ≤ 893927/5000000 = 0.1787854` (computer-
assisted, Polymath Theorem 1.2 instantiated at exact parameters, with a
"not yet peer reviewed" label); Gordon, `Λ < 0.158` (`0.1576566…`, with a
partial Lean 4 companion that is explicitly conditional on analytic
inputs); and arXiv:2609.37164v2, a conditional refinement that cites both
and also reports a Raymond claim of `Λ < 0.149396`. All use the same
Platt–Trudgian verification height as the published `0.2`. So the
Claude brainstorm's "ceiling of this method is about `0.19`" is refuted
by the record: `t₀ ≈ 5/L` was never a theorem, and the gains came from
optimizing `(t₀, y₀, X)` and the error budget, exactly the parameters the
corrected interface of Notes 20–22 affects.

A separate public repository claims a kernel-checked `Λ ≤ 9/32` as a
consequence of the quasi-RH preprint. `9/32 = 0.28125` is the
`δ²/2` entry in the Claude brainstorm's table at `σ₀ = 7/8`. So the one
bridge from quasi-RH to the heat flow has been formalized by others and
is weaker than the unconditional bounds, which settles the brainstorm's
reading (i) externally: the heat lane gains nothing from the hypothesis.

What D4 should become is in section 4.2.

### 3.3 D5 must be replaced by the family ledger

The Codex calculation is exact and I reproduced it. The honest statement
of the arithmetic lanes' open problem is not a universal normal form but
the per-family ledger Codex proposes: weights `ω_r`, kernel
`K(m, n) = Σ_r ω_r χ_r(n)χ̄_r(m)`, exact diagonal, exceptional
congruences, coherent mass, and the signed covariance remainder, with the
four-way classification of any proposed estimate. The literature search in
D5 should be run against the corrected family and normalization. I
withdraw the normal form.

## 4. Additions

### 4.1 What the counter-kernel lacks: solidification, and a bounded test

Codex §6 asks for the explicit property of the theta kernel that a proof
could use and the counter-kernels fail. Polymath Theorem 1.5(i) supplies
one: for every `t > 0`, every zero of `H_t` with `x ≥ exp(C/t)` is real,
simple, and within `O(x^{−ct})` of the lattice `g(x_n, t) = n`. Call this
solidification. Its proof is the Riemann–Siegel approximation with the
`n = 1` term dominating, which is the Dirichlet series having leading
coefficient `1` — arithmetic input of the kind R1 asks for.

The two control families in the repository split the properties:

| Control | Positive kernel | `N(R) ~ R log R/(4π)` | Solidification at every `t > 0` | `Λ > 0` |
| --- | --- | --- | --- | --- |
| `q_{T,b}` (kernel B) | yes | yes (section 2) | no: complex pairs at every lattice point `(π/2 + πn)/b` for all `0 < t < T` | yes, `= T` |
| Gaussian controls, e.g. `(16u⁴ + 24)e^{−(1+1/40)u²}` | yes | no (finitely many zeros) | vacuously yes | yes, `= 1/40` |
| theta | yes | yes | yes (theorem) | unknown |

So neither "density" nor "solidification" alone excludes a positive-time
collision, and no control in the repository has both. The bounded test:
construct a positive even kernel whose transform has Riemann–von Mangoldt
density with bounded remainder, solidifies at every positive time, and has
`Λ > 0`. A natural attempt is surgery on a real-rooted member of the
family, e.g. `H_{1/2}` (de Bruijn): replace two real zeros `a, c` by a
complex pair `w, w̄` via `H ↦ H·(1 − z²/w²)(1 − z²/w̄²)/((1 − z²/a²)(1 − z²/c²))`,
and test numerically whether the resulting Fourier kernel stays positive.
*Continue if* no such kernel can be built and the obstruction is
identifiable (then positivity + density + solidification is the first
shape condition with teeth, and it is a theta theorem). *Stop if* one is
built easily (then R1 holds in full and the arithmetic input must be
finer than solidification). Either outcome is a one-paragraph fact for
the closure note; I expect the second.

### 4.2 The honest form of D4: an independent audit of the public `Λ` claims

The repository's one asset the heat lane produced — the corrected
Riemann–Siegel interface of Notes 20–22, independently validated against
the genuine `H_t` in review 13 — is exactly the tool for checking a
barrier certificate. The three public claims are self-labelled as not
reviewed. An independent replay of one of them, cell by cell, with the
repository's interval evaluator and the corrected error ledger, reporting
agreement or a located discrepancy, is a concrete unconditional
deliverable in the repository's own validation culture, and it is more
valuable than a fourth unreviewed number. Order: Gomila's package first
(smallest claimed step, Polymath criterion instantiated directly, fail-
closed certificates designed for replay), then Gordon's. *Stop if* a
package cannot be replayed from source at all; report that as the finding.
If the replay succeeds, the corrected interface's smaller residual tells
whether their `(t₀, y₀)` could be tightened at no new verification
height, which is the benchmark Codex §5 asks for, now with a real
baseline.

### 4.3 D7 as the union of two named no-gos

Codex is right that a universal "no heat method" theorem cannot be
stated. Two named no-gos exist and should be written down together in the
closure note: Note 18's local ambiguity (nothing built from the finite
approximant, a sup-norm disk bound, the heat equation and analyticity can
decide a strict-interior first-jet candidate) and kernel B (nothing built
from positivity, evenness, decay, moment signs, Laguerre or stationary
signs, or density can exclude a positive-time collision). The persistence
calculation of Codex §7 is the quantitative form of the gap between them.
That is D7, and it is enough.

### 4.4 On D1: what the source audit should return

Codex's refinement (audit one complete nonempty cube-tail branch of the
October 5 argument, with the decreasing parameter and base case named) is
the right first task, and I would add the one question the Claude note
asked: at which step does the conclusion become true for the trivial
character? If that step is the application of a mean square to a row that
is itself the trivial character, the finding is the R3 trap inside the
source; if it is a genuine repulsion or amplification mechanism, it is the
only candidate descent engine in the program. Either answer is the most
useful single sentence this program can produce in the next session.

## 5. Recommended order

| Order | Deliverable | Source |
| --- | --- | --- |
| 1 | Dependency map and one complete imported recurrence branch, answering the trivial-character question | Codex 1, Claude D1 |
| 2 | Exact moment ledgers for one sextic family and one quadratic lift, with the four-way classification of each proposed estimate | Codex 2, replacing D5 |
| 3 | Independent replay of one public `Λ` certificate with the corrected interface; benchmark as a by-product | §4.2, replacing D4 |
| 4 | Closure note for the heat lane: fact (D) restated as in §3.1, the two no-gos of §4.3, the feature table of §4.1 with the surgery test's outcome, the divisor-pair identity, the corrected interface | reviews 12–13 §8, §7 |
| 5 | One matched function-field experiment, only after the ledger fixes the family | Codex 4, Claude D3 |
| 6 | Erratum addenda to reviews 12 and 13 for fact (D) | §3.1 |

The Li, Nyman–Beurling and Rodgers–Tao wildcards stay parked, as both
notes say.

## 6. Checks performed

Labelled numerical and symbolic computations, run in this session with
mpmath 1.3.0 and sympy 1.14.0; they are not standard-library checkers and
are not registered through `validation/endpoint_matter.py`.

- Orthogonality floor: for `q = 101`, `N = 40`,
  `Σ_{χ mod q}|Σ_{n≤N}μ(n)χ(n)|² = 2600 = (q−1)·#{n ≤ 40 squarefree}`,
  exactly.
- Counter-kernel density: sign changes of `e^{πν/2}K_{iν}(1)` on
  `ν ∈ (0, 60)` at step `0.02`: 72, against `(R/π)log(2R/e) = 72.4` from
  `K_{iν}(1) ~ (2π/ν)^{1/2}e^{−πν/2}sin(ν log(2ν/e) + π/4)`.
- Two-packet Weil identity: with `φ = e^{−u²}`,
  `G(ρ) = 2Φ(a)sinh(aL/2)`, `G(1−ρ̄) = −2Φ(a)sinh(aL/2)`, product
  `−4Φ(a)²sinh²(aL/2)`, symbolically; the general-`φ` case is the same
  two-line substitution using `Φ(−a) = Φ(a)`.
- Heat Jacobian: `det D_{(t,x)}(H, H_x) = H_xH_xxx − H_xx²` under
  `H_t = −H_xx`, equal to `−H_xx²` at a double zero.
- Polymath 15: Theorem 1.2, Prop. 3.1(ii), Prop. 3.3 and Theorem 1.5 read
  from arXiv:1904.12438v2; Prop. 3.3 excludes only `y ≥ (y₀² + 2(t₀−t))^{1/2}`.
- Public `Λ` claims: Gomila repository and exposition (`0.1787854`, "not
  yet peer reviewed"); Gordon repository (`0.1576566… < 0.158`, Lean
  companion conditional on analytic inputs, no external review);
  arXiv:2609.37164 (conditional, cites both, reports a Raymond claim of
  `< 0.149396`); a kernel-checked `Λ ≤ 9/32` from quasi-RH in a separate
  public repository. None is treated here as a validated bound.
- Lemma 18.1 hypothesis status: confirmed in the repository's own
  dependency ledger.

No collision exclusion, threshold result, zero-free strip, or RH
conclusion is claimed or refuted in this note.
