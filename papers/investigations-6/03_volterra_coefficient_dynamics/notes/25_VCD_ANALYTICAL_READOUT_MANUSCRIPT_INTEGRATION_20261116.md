# Analytical readout manuscript integration and reading guide

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, chat0004. The actual model and
reasoning effort are unavailable in the recorded configuration. No helper
was dispatched for this integration. Earlier source-note dispatches and
assessments retain their own recorded provenance.

**Status: manuscript integration with same-assistant analytical and document
checking.** The user requested additional mathematical background and
systematic incorporation of the relevant analytical results. The
[editable manuscript](../manuscript/main.tex) now develops those results
as one argument. This is not execution of B07 or E25 and supplies no new
canonical zero-confinement theorem.

Read the [result index](../../../../result-summaries/README.md), especially
[cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
and [avoid index](../../../../avoid/README.md). The relevant patterns are
[01: restating the target](../../../../avoid/01_restating_the_target.md),
[02: control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07: scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[12: signed aggregate versus separate bounds](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [13: a factor is not the target](../../../../avoid/13_a_factor_is_not_the_target.md).

## Classification and organization

The exact spectral, memory, midpoint and quadrature formulas are identities.
The coefficient and complex error bounds are quantitative estimates with
explicit constants and domains. The directed contour theorem and local
zero-displacement lemma are conditional results: their hypotheses must be
established on the intended canonical regions. The unquantified exhausting
zero-strip assertion is classified once in manuscript §10.3 as an
RH-equivalent reformulation, not supported by finite checks. The polynomial
phase derivation and elementary perturbation lemma are background tools;
no novelty claim is made for the classical methods.

The systematic reading route is:

| Manuscript location | Development and source |
| --- | --- |
| §§1–2, equation (2.3) | Variable dictionary; complete source; probability normalization, which changes no zeros; source versus observation variables. Original analytical draft, with expanded explanation. |
| §§3–4 | Moving basis, Volterra flow, multiplication operator, fixed-vector complex domain and logarithmic envelope. Earlier draft and E04; no bounded whole-space complex propagator is assumed. |
| §5, equations (5.2)–(5.11) | Jacobi readout, Gauss exactness through degree 2N−1, first missing return path, compact complex convergence, Gaussian counterexample, and polynomial phase from Christoffel–Darboux. E04 and discussion24, with elementary background derivations. |
| §6 | Real-height boundary memory; midpoint bilinear square sum; finite midpoint readout equals the direct head. E04/E13 and the bare-head specialization of E15. The more general shared-kernel theorem is not reissued here. |
| §7, Theorem 7.1 | Complete factorization F−G_N=L_N E_N and exact second/fourth moments. E21, with a self-contained normalized-simplex and confluent-interpolation proof. |
| §8, Theorem 8.1 | Explicit degree-only exponential-moment constants, complex phase estimate and real parity brackets. E22. The error factor being nonzero does not make F nonzero. |
| §9, Theorem 9.2 | Positive-amplitude directed set, pointwise exclusion, conditional contour count, and equal-coefficient comparison with the next physical head. E24. |
| §10, Lemma 10.1 | Exact successive-degree identity; phase/Wronskian background; local zero motion under slope, curvature and perturbation bounds; multiplicity-aware cluster counts. Discussion24 and standard complex analysis. |
| §11, Proposition 11.1 | All-degree canonical-score source characterization, derived through the polynomial Stein identities and a distributional equation. E08. Control scopes and checked reference routes follow. |
| Appendix A | Original fixed-initial-chain real-height heat/quadrature bound, retained with its normalization and proof. |

The B05 source-Fourier estimates and their scoped failed uniform consumer
remain in [synthesis19](19_VCD_B05_CANONICAL_FOURIER_ESTIMATE_SYNTHESIS_20261116.md).
The smooth finite-information controls and general midpoint calibration
results retain their source notes. They are not prerequisites for the
signed quadrature-error development and have not been folded into new
manuscript claims.

## What a candidate connecting lemma must add

The polynomial phase identity (5.11) differentiates in the source
coordinate and has a positive sum of squares in its numerator.
Equation (10.2) explains the corresponding algebra for a real function
and companion. No such positive identity has been established for the
actual Fourier readouts. The common real parity brackets also rule out
exactly one simple next-head zero and no other zeros between two
same-head zeros in the stated common sign range, if those endpoints
exist. This is not an assertion that the canonical endpoints exist or a
universal exclusion of phase methods.

The local lemma isolates another possible input: a lower bound for the
readout slope, or a boundary separation bound for a cluster, with useful
degree dependence. Upper bounds for the error and the second derivative
are already available. Simplicity is a hypothesis only of the particular
local lemma; the larger program allows multiple zeros and nonreal zeros
of finite approximants.

**The polynomial phase identity is not a phase identity for the Fourier
readout.** Likewise, **the error phase estimate is not a zero-location
theorem for the physical field.** These are the two distinctions the
expanded background is intended to make easy to discuss.

## Control screen

Applied as a premise comparison against
[catalog12](../../../../result-summaries/12_collision_controls_and_screening.md)
and the already recorded [B06 screen](23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md).
No numerical certificates were rerun.

| Control family | Premise comparison and retained scope |
| --- | --- |
| Positive finite weighted-square sources | Pass the even-measure error law, common cosh bound, envelope and phase estimate. They fail the unchanged complete coefficients/full reflection. The manuscript derives the shared bound analytically; collision certificates are supporting witnesses only. |
| Finite canonical score/head and selected-prime controls | Preserve their stated finite data, but fail complete reflection or all-degree canonical identity. Finite data do not replace Proposition 11.1. No fixed compact zero location is asserted. |
| Euler-factor translates | Retain generic even-source quadrature identities; the already tested c=1/2, p=23, time-zero example fails the envelope at index zero. This is not a claim that every Euler-factor member fails every bound. |
| Reflected super-Gaussian | Has the exponential moments for the exact law; fails the exponential score-confinement premise used for the common quantitative bound. |
| Smooth shape/positive-primitive sources | Fail unchanged canonical arithmetic. Their weak confinement comparison is untested here; failure of the source formula is not proof that every derived inequality fails. |
| Atomic and compact triangular sources | Atoms permit nondegenerate quadrature only before the monic norm vanishes; both classes lack a strictly positive full-line density for the confinement lemma. The generic finite-stage identities may still hold. |
| RH-conditional endpoint constructions | Retain the RH premise and do not supply unchanged theta arithmetic; no unconditional theta exclusion follows. |
| Fixed source with changed observation | Fails the literal exponential/Fourier readout premise. |
| Finite-profile positive-measure relaxation | Does not identify the complete source or an actual physical zero configuration. |
| E10 smooth finite-data freedom | Preserves its specified data and common envelope while varying the next defect. Its zero geometry remains open; it is not relabeled a nonreal-zero construction. |

Christoffel–Darboux applies to all positive nondegenerate Jacobi heads,
including controls. Rouché and the local perturbation lemma apply to all
functions meeting their stated inequalities. A control can pass such a
local test on one disk. Rejection is required only of an asserted global
conclusion on a domain containing the prohibited zero, not on every local
disk.

## References, checks and artifacts

The classical probability representation is supported by de Boor's
confluent interpolation and simplex formulas, with the simplex volume
normalization derived in full. The earlier
[passage record04](../references/04_QUADRATURE_ERROR_PHASE_PASSAGES_20261116.md)
is preserved. Equation (52), printed pp.63–64, was re-inspected online for
this integration. Topping's 29 July 2024 notes, §§9.8–9.9,
Theorems 9.18 and 9.21, were re-inspected for multiplicity counts and
strict Rouché comparison; see the earlier
[record02](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md).
Teschl and Romanov retain the versions and limited scopes in
[record05](../references/05_READOUT_PHASE_SEARCH_PASSAGES_20261116.md).
These are passage checks, not a literature-wide novelty review.
No local third-party PDF copy or hash is asserted.

The [assessment09](../reviews/09_VCD_READOUT_MANUSCRIPT_ASSESSMENT_20261116.md)
and [build record11](../numerics/11_VCD_READOUT_MANUSCRIPT_BUILD_20261116.json)
record the analytical checks, build, reference resolution and page
inspection. The user expressly allowed the ignored root output folder:
the [PDF](../../../../output/pdf/volterra_coefficient_dynamics/volterra_coefficient_dynamics.pdf)
is there; TeX, this guide and small records remain in the investigation.
No manuscript snapshot folder or numerical research campaign was created.
Hashes identify artifacts; they do not validate mathematical claims.
