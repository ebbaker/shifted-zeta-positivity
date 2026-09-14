# Positive factorizations and supersymmetric extensions of Weil forms

Companion brief to the working manuscript, version 0.2, 11 September 2026.

This is the companion brief for the positive-factorizations attempt.
The [program overview](../../PROGRAM_OVERVIEW.md) records the later shared
research direction and distinguishes subsequent round-4 results.

The [manuscript](manuscript.pdf) is the detailed mathematical record. This brief preserves the motivation and the current decision about where to investigate next. The [LaTeX source](manuscript.tex) contains the statements, proofs, references, and certificate description.

## Why keep both formats?

There is enough material for a working manuscript: explicit constructions, several obstruction arguments, an exact rational sign certificate, and a connection to existing extension theory. Organizing those results as a paper makes their hypotheses and dependencies easier to scrutinize.

The direction toward RH is still exploratory. We have not found the arithmetic principle that forces the proposed positive completion. Markdown remains useful for keeping the motivation, alternative models, and lessons from dead ends visible without turning every proposal into a theorem or conjecture. The manuscript is not yet a submission draft: priority review and independent mathematical review remain outstanding.

## How this direction arose

The initial research attempted to extend xi into higher-dimensional settings and constrain zeros through rotational symmetry. The recurring difficulty was that the new descriptions reproduced information already present in the complex formulation. The lesson was that additional coordinates need an independent constraint or dynamics to become mathematically useful.

The researcher's physics background then motivated investigations of gauge theory and ideas inspired by AdS/CFT. The shifted program made a surviving question concrete: could an independently positive internal system produce the exact zeta boundary response? Here a bulk can be a linear field system or a network; no AdS geometry or conformal field theory has been established.

Finite-depth certificates provide substantial benchmarks. They do not explain why positivity should persist at every depth. Supersymmetry was proposed because an independently specified operator A and a positive inner product yield a nonnegative Hamiltonian A* A. The missing task is to derive the arithmetic form or boundary response from that construction. Choosing A to be the unknown target's spectral square root assumes the desired sign.

BRST would have a specific role if a candidate model introduced gauge redundancy. Nilpotence alone does not establish positivity of the physical quotient. Likewise, a supertrace is a difference of traces and need not be positive. These distinctions are part of the model design, not reasons to discard supersymmetry.

## What has been established in these investigations

1. **An explicit small-window factor.** For total length L ≤ 1/4 and shift 0 ≤ ω ≤ 1/2, the exact prime-free form factors into nonlocal differences and a multiplication term. Elementary estimates prove a uniform lower bound above 0.099. This is a structural example inside an already certified region, not an extension of the project's depth results.

2. **An exact positive auxiliary-field tower.** The gamma kinetic multiplier is a sum of positive terms with masses aₖ = 2k + 1/2. Each term is obtained by minimizing a local positive energy over an auxiliary field. The infinite tower produces the required logarithmic Fourier growth. Its square-root map is closed on explicit positive component spaces and gives a graded supercharge. This explains why a local enlarged system can avoid the growth obstruction to a local first-order factor acting directly on the boundary input.

3. **A stronger pairwise obstruction.** Independent phases, unequal weights, and separate vector channels attached to two-point couplings cannot reproduce the complete gamma form at L = 2/3. A necessary comparison form has a negative direction, with an exact rational bound below −1/25. The negative comparison form is not the Weil form itself.

4. **Finite pairwise networks retain that restriction under elimination.** A positive comparison matrix remains positive after internal nodes are eliminated through Schur complements. This is a finite-network result, with passage to singular continuum limits left conditional on the necessary convergence.

5. **Coherent mixing can escape the comparison obstruction.** The positive toy energy

   E(f,u) = |f₁ + f₂ − u|² + |f₃ + u|²

   reduces to ½|f₁ + f₂ + f₃|². Its boundary comparison matrix is not positive, even though the boundary energy is. Several amplitudes enter the same square before elimination. The example supplies a possible type of coupling, but has no arithmetic content and is positive before supersymmetric packaging.

6. **Boundary terms and primes impose further constraints.** A natural growing Green-function replacement has a negative Robin boundary direction. The first-prime correction is indefinite: it can be neither an independent positive additive channel nor the change produced by eliminating an auxiliary field while keeping the bare boundary block fixed. Its couplings and diagonal terms must be derived jointly.

7. **The global input space matters.** No closable map on ordinary whole-line L², defined on every smooth compactly supported input, can have squared norm equal to the full Weil form. The proof uses the expanding-support Fourier-sampling obstruction. Finite intervals, appropriate test-function spaces, and unbounded boundary observables remain possible. Extra output components do not remove this restriction.

8. **A complete central odd-sector factor.** Reflection folding makes the odd off-diagonal kernel negative. The explicit cubic `phi(x)=x(1-4x^2/(5 ell^2))`, with `ell=L/2`, gives a weighted difference factor for the whole odd gamma form, including the normalization and pole term. An exact rational scalar certificate proves a floor of `1/100` for `L<=7/10`. This covers the full Weil form on odd inputs for `L<=log(2)`; above `log(2)` the theorem concerns gamma alone. It is an explicit symmetry-sector construction, not a new depth record or a canonical arithmetic supercharge.

9. **The first prime can stabilize a negative gamma direction.** At `L=1`, the unit input `sqrt(12)*x` has gamma form below `-0.12`, while the full form on that input exceeds `0.26`. The proposed independent-edge remainder is below `-0.58`. All three signs are certified by exact fractions. After folding, the prime adds energy to one cap-reflection channel and subtracts it from the other; both must be accounted for jointly. See [round 3](INVESTIGATION_round3.md).

## What remains missing

The auxiliary tower gives the kinetic term. The complete gamma form also contains the fixed negative normalization and the odd pole contribution. The tower alone does not account for those terms within an independently positive joint system. Round 3 now supplies an explicit complete factor on the central odd subspace using reflection and a cubic trial weight; the even subspace is still open in this construction.

A useful supersymmetric extension must supply a geometric or arithmetic reason for coherent component mixing. It must then identify its boundary observable exactly, including normalization, endpoints, and the prime shifts. A guessed coupling matrix, a fitted factor, or a positive inverse-spectral realization conditioned on the desired sign does not provide this explanation.

The immediate benchmark is now the even central prime-free sector through the known positive slab, followed by a shift-uniform completion. The next benchmark is the first prime with its two reflected cap channels; the simple independent-edge remainder has been disproved. These are focused construction problems; an interacting gauge theory is not yet required by the evidence.

The current assessment is therefore that the enlarged-space avenue is useful enough to continue, while its RH relevance remains conditional on finding the missing arithmetic coupling rule. The calculations clarify what a successful model must do; they do not establish that one exists.

## How to use the draft

Use the manuscript for checking claims and proofs. Use this brief when considering a new model or deciding whether a failed model teaches something transferable. The two original exploratory notes remain separate historical records; this brief incorporates the stronger restrictions found in the second investigation.

The supplied checks require Python and NumPy, without any zeta-zero archive. The rational certificate is distinguished from floating-point identity diagnostics. See the [package README](README.md) for build instructions and the current verification ledger.
