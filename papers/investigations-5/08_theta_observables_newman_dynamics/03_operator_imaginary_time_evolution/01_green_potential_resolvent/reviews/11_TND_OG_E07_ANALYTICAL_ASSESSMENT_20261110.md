# E07 r1 claim-level analytical assessment

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Exact-turn local provenance records
**gpt-6.1-sol, ultra**. Internal LLM assessment with inherited premises.
The B05 author's actual model/effort is unavailable, so model
independence is unverified.

**Disposition: accepted, all eight claims.** The acceptance is for
the conditional calculations and scoped comparison in [Note12][b05].
[Note13][calc] rederives the key estimates and tests the edge cases.
All 25 entries of the issued [Inputs23][inputs] match. The one allowed
additive correction was unnecessary. [Check10][author] was read as
the proof author's account. De Boor's [versioned §9 (52)][deboor]
was rechecked through the [canonical OA record][source].

| Request23 claim | Equations and verdict | Assessment |
| --- | --- | --- |
| 1. Regular complex deflation | (2)–(3), **accepted** | Newton–Hermite remainder uses actual roots with the stated multiplicities. Convexity and a holomorphic neighborhood cover all arguments and segments. Simplex moments give both constants, including the repeated real and order-zero cases. |
| 2. Literal source derivatives | (1), (4), **accepted** | \((iu)^k\) and \(e^{b|u|}\) give the weighted source moment with the inherited \(1/2\), and both omissions are retained. \(n+3\) pays the highest derivative, \(n+2\) for exact knots. Deflate \(H_0\) and evaluate \(D_0\) separately on the real line. |
| 3. Factor and root logs | (5)–(8), **accepted** | The true modulus stays at least \(\mu_v-e_{v,0}\). Centered superlevel intervals give the factor 4 in the integrated root bound. \(\rho=0\), endpoints, repeated knots, and vertical height changes through the axis are covered. The \(z^2+\eta\) control retains square-root root motion. |
| 4. Signed product rule and panel budget | (9)–(13), **accepted** | Both primitives differentiate to the required integrands. Interpolation pays the curvature factor \(1/8\), the kernel error on the full singular \(L^1\) term, and patch rounding. The 793024 panel limit and \(<1/500\) error are conditional design arithmetic. |
| 5. Complete two-sided acquisition | (14)–(15), **accepted** | Compact errors and both inherited tails are added as radii. The pole appears once in the central expression. The upper-minus-true error costs \(2\mathcal R\). Finite evaluation and rounding remain in the numerical radius. |
| 6. Green cusp, ranges and tail | (16)–(19), **accepted** | Monotone corner extrema, multiplicities and both cusp bounds hold. Exact core completeness and integer alignment are required by the stated tail proof. The shifted-slab test exercises that alignment premise. |
| 7. Direct comparator | §6, **accepted** | An occupied cell meeting \(D\), even at a corner, gives \(U_i\ge m\). Nonnegative other terms rule out the strict Green pass. Since \(r<R\), a complete core covers \(D\). The identical cells then give direct exclusion. |
| 8. Scope and full cost | (20), §§7–9, **accepted** | The displayed rule counts \(O(\sum_v(1+n_v)N_v)\) panel operations apart from factor evaluation. Charge source/derivatives, root certificates, floors, factor and product evaluation, and tails/prime. Give common input to both consumers at the same acquisition cost. Neither a measured speedup nor canonical signed smallness is established. |

## Collision-control check

This is the analytical premise screen in [controls12][controls] and
[avoid02][shape], applied to the canonical use of these conditional
bounds. Generic quadrature and log estimates can hold for a control
using its own certified data.

| Family | Premise changed or absent |
| --- | --- |
| Fixed and growing Euler factors | Conductor-one coefficients and the canonical prime baseline change. |
| Three-/four-weighted squares and finite theta/zero-tail sources | Complete normalized theta coefficients together with full reflection fail. Square support, finite endpoints and small source differences leave the missing premise unpaid. |
| Finite-prime orbits | Full reflection fails even with selected primes and finite prefixes fixed. They give no general completeness or deflated-floor input. |
| Reflected super-Gaussian, smooth shape and positive primitive | Reflection, positivity and endpoint data leave the complete integer-square theta arithmetic and xi/zeta identity absent. Reflection rigidity applies to the normalized weighted-square class with the full conjunction. |
| BW-01 atoms and exact finite-profile families including continuous extensions | The full theta coefficients and profile growth are missing. The stated eventual-simplicity premise also fails in the families for which the source records it. |
| RH-conditional normalized endpoint perturbations | Ordinary Dirichlet-series arithmetic fails. The completion, functional equation and residue may be preserved as specified. |
| Fixed amplitude with variable readout | The full physical cosine/Newman equation changes. |
| Three-profile relaxation | Positive real weights matching finite profiles do not furnish the integer divisor and complete source. |
| Earlier counter-kernels and smooth density | The kernels lack the literal theta transform and anchor. The smooth-density control replaces the discrete prime measure. |
| Two-channel exclusion | The specified support and norm-factorization architecture define its exclusion class. The signed log calculation lies outside that class. |

A finite box can avoid a control's defects. A real double has zero
interior Green mass, and its event time cannot be shifted to time
zero for this check. See [avoid01][target] for classification,
[avoid07][scope] for scoped exclusions and [avoid11][known] for the
known-region cost comparison.

## Evidence and remaining input

The proofs remain conditional on certified actual-root matching,
uniform factor floors and paid derivative and numerical enclosures.
The \(X=1500\) comparison continues to inherit the OC census
certification at its original scope. [Record07][record] performs
rational proof arithmetic only. No E06 replay, root acquisition,
field evaluation or measured canonical cost was part of E07.
The decisive missing input is a **literal-source patch cover with
certified cluster counts, radii and factor floors**, derivative
enclosures sufficient for (14), and a fully charged comparison with
direct exclusion on the same \(D\). [Continuation15][cont] parks B05 r2
pending a concrete proposal for that input. No field run is ready.

[b05]: ../notes/12_TND_OG_B05_DEFLATED_LOG_AND_CELL_RANGE_DECISION_20261110.md
[calc]: ../notes/13_TND_OG_E07_ANALYTICAL_ASSESSMENT_CALCULATIONS_20261110.md
[author]: 10_TND_OG_B05_PROOF_AUTHOR_CHECK_20261110.md
[inputs]: ../research-progress/handoffs/23_TND_OG_E07_INPUTS_20261110.json
[record]: ../numerics/07_TND_OG_E07_EXACT_ASSESSMENT_RECORD_20261110.json
[cont]: ../continuation-notes/15_TND_OG_E07_RESULTS_AND_MODEL_CHANGE_20261110.md
[source]: ../../03_collision_constraints/references/01_TND_OA_B01_SOURCE_USE_20261109.md
[deboor]: https://arxiv.org/pdf/math/0502036v1#page=19
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[shape]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[known]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
