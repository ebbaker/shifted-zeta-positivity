# N4SYM: accomplishments, obstacles, arithmetic prospects, and priorities

24 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity). **Reasoning effort:** not exposed; not inferred.

**Scope:** assessment of the N4SYM manuscript source, principal research notes, three internal audits, proposal and continuation records, against the parent Wilson–Loewner, WZW and critical-path programs. Baseline: `688eb8d763f1bf9ba436a99f575fe4c8e22eb681`. This is a different-assistant assessment and numerical replay, not an independent specialist review or a complete proof audit. No new arithmetic realization or positivity theorem is supplied.

## Assessment

The investigation has made substantial progress in specifying physical observables, deriving their responses, and identifying why the simplest proposed arithmetic identifications fail. Its strongest transferable lesson is a concrete positive storage-and-radiation account, together with sharply scoped exclusions. It has not yet produced a convincing route to the completed arithmetic transfer.

I would retain N4SYM as a controlled physical laboratory, but would not make further calculations in the already-tested channels the main arithmetic priority. Several attractive physics continuations do not address the missing parameter action, prime-delay mechanism, or ordinary signal norm. A significant missing literature reference also changes the immediate continuation plan.

## What has been accomplished

### Straight-line benchmark

The [straight-line calculation](../notes/STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md) connects shape variation to displacement and internal-scalar correlators, fixes the quadratic response through the Bremsstrahlung function B up to a perimeter counterterm, checks the Zarembo cancellation, and derives the local linear response

\[
\chi_R(\nu)=m_R\nu^2+2\pi iB\nu^3.
\]

Here frequency is denoted by nu to distinguish it from the arithmetic shift. The protected dimension-two displacement gives a contact-supported commutator. Changing B cannot change this response into a variable fractional front. This is a strong negative result for the specified linear displacement channel, valid much more broadly than one perturbative computation.

The distinction between positive total radiated work and the indefinite renormalized finite-time Schott contribution is useful. Neither a positive spectral density nor total-work positivity alone proves the required ordinary-L2 contraction.

### Genuine Loewner contours

The work diagnoses three different completions of a growing trace. Constant scalar charge on both legs produces the unwanted thin-sliver attraction; the tangent-coupled supersymmetric completion is trivial; reversing the scalar charge on the return chord produces a nontrivial family with an exact identity at zero driver.

For this flipped return, the [first two evolution equations](../notes/FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md) retain scalar, curvature, transport and tip terms and have noncommuting classical-background controls. The fixed-resolution short-time expansion is checked independently against a one-loop integral. The analysis distinguishes vertex excision, flow and rounding and explains why their limiting laws differ. These are concrete gains on the original genuine-trace question.

The [corner study](../notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md) identifies the effective coupling g approximately equal to lambda times |s|/3, with s = a sqrt(t). It obtains the two-loop corner expansion and a planar classical strong-coupling function with F(0) approximately 0.1750. Its all-orders one-loop-exactness statement remains conditional on the multi-angle antiparallel bound and is only order by order. The strong-coupling window is a different order of limits and does not prove nonperturbative exactness.

The closure audit is another useful outcome: it exhibits the transverse, matter, transport and ordered-insertion terms that cannot be eliminated by the available Schwinger–Dyson identities. A listed residual is progress, but it is not a closed evolution or a norm-controlled infinite hierarchy.

### Finite mass and positive storage

The [finite-mass calculation](../notes/FINITE_MASS_MEMORY_AND_QUARTIC_RESPONSE_20260924.md) supplies an explicit memory channel in the zero-temperature planar classical-string approximation:

\[
F=m\ddot Y,\qquad X=Y+z_m\dot Y,\qquad
W(T)=\frac m2\dot Y(T)^2+\frac{\sqrt\lambda}{2\pi}\int_{-\infty}^{T}\ddot Y(t)^2dt.
\]

For an initially static string this is positive at every time. The Schott contribution appears in the small-z_m expansion of the stored square. This makes the energy-accounting lesson unusually concrete: keeping the physical internal state can restore a positive account that a singular subtraction/truncation obscures.

The response has only one exponential memory scale. The derived dilaton readout is a single delay times a quartic polynomial in frequency, with the same one-pole factor when expressed in the physical trajectory. It therefore fails the variable-front test in the approximation examined. Passivity of this driven force/velocity system does not identify a normalized arithmetic scattering map.

### Quartic response

The work identifies the connected four-point functions and coincident-source terms needed beyond quadratic order, validates the transcribed dimension-one input against crossing/OPE constraints, and rejects the dimension-two transcription. Non-protected anomalous dimensions provide a plausible source of power-law nonlinear memory.

The explicit third-order retarded kernel has not been calculated. The manuscript itself labels the memory claim a proof sketch. Single discontinuities of Euclidean logarithms should not substitute for the full nested-commutator calculation, all orderings, and contact terms. Even a successful calculation would describe cubic response, not the desired linear transfer. In the native time of the undeformed straight line, scale covariance also prevents a hierarchy of nonzero fixed delays.

## A literature omission that changes the next steps

[Chernicoff, Güijosa and Pedraza, arXiv:1106.4059](https://arxiv.org/abs/1106.4059) already compute the dilaton-coupled field for arbitrary quark motion, including finite mass. Section 3 derives a total-derivative reduction and dependence on data at one retarded event. Section 4.1, particularly equations (49)–(52), discusses the older Callan–Güijosa calculation and its approximation limits. Equation (49) contains the massless linear factor exp(i nu r)(1-i nu r).

Consequently, nonlinear dilaton localization is already a literature result in the relevant classical setting. The proposed second-order calculation should become a check against that result. The suggested new correction of the 1999 paper must also be reassessed against the 2011 discussion; an algebra-error claim is not established by this review. The specific finite-mass polynomial still merits a term-by-term comparison with the published formula.

This source was checked through the primary PDF text, including Sections 1.2 and 4.1. The web PDF screenshot service failed, so I do not claim visual verification of every equation. The qualitative priority correction does not depend on deciphering an uncertain formula.

## Why arithmetic contact remains difficult

The target is

\[
K_\omega(p)=\frac{\xi(\tfrac12+p-\omega)}{\xi(\tfrac12+p+\omega)}.
\]

Its relevant structure includes an identity endpoint, the high-p front (2 pi/p)^omega and its logarithmic tangent, the full gamma/rational completion, and translated contributions at log(n) with the prescribed multiplicative coefficients. A positive realization must explain the ordinary signal norm and accumulated storage without assuming the desired contraction.

Four gaps remain:

1. **Parameter action.** Neither the normalization B nor Loewner capacity is an identified arithmetic shift. Varying bulk lambda changes the theory; changing a time scale generally moves delays rather than changing their amplitudes at fixed locations.
2. **Channel construction.** A Wilson expectation on a Euclidean shape family is not yet an input/output map. A susceptibility with an energy balance still needs preparation, readout and norm identification before it becomes the required scattering operator.
3. **Arithmetic structure.** No tested N4SYM construction derives the log(n) support or the Euler coefficient law. Adding one relaxation time, a temperature, or a smooth background supplies structure, but not that structure automatically. An infinite thermal pole tower is not a finite rational function and deserves its own analysis; its existence alone gives no prime-delay mechanism.
4. **Control and scope.** Smooth-field identities are not full renormalized quantum evolution theorems. One-loop rounded finiteness is not all-orders control. The corner bound is conditional, and the finite-mass rationality result is restricted to its stated background and approximation.

The no-scale statement is about the specified native-time straight-line observables. It should not be promoted to an exclusion of every observable, background, readout or coupling in N4SYM. Conversely, escaping a theorem's hypotheses does not supply evidence of arithmetic matching.

The most promising retained connection is methodological: construct actual internal states and their positive energy before eliminating them. The finite-mass example makes that principle explicit. It supplies no justification for identifying its stored square with the arithmetic norm deficit.

## Recommended next steps, ranked by broader-program impact

Impact here measures progress on the all-input, all-length arithmetic positivity objective, not just calculational sophistication. High impact does not imply high probability of success.

| Priority | Bounded next task | Impact and decision criterion |
|---|---|---|
| 1 | Reconcile the dilaton calculation with the 2011 paper; audit source equations, claim scope and novelty; obtain specialist review of the main analytical claims. | **High immediate value for reliability and allocation of effort; low direct arithmetic gain.** It prevents redundant work and establishes which physics claims remain new. Do this before extending the manuscript. |
| 2 | Return the main arithmetic effort to independently defined cumulative storage for the complete transfer on log(2) < L < log(3), retaining the archimedean response and first-prime interference. | **Very high direct relevance, uncertain feasibility.** Produce a derived positive state energy or an explicit unresolved cross term. Do not define storage as the desired deficit and call that a proof. |
| 3 | Relate that calculation to the existing critical-path anchor and to an explicit canonical-system construction. Audit the small-shift obstruction in Suzuki's construction. | **High to very high relevance.** Seek an operator estimate or state representation that controls omitted inputs and extends in support length; another isolated finite matrix is insufficient. |
| 4 | Before a long N4SYM calculation, perform a short feasibility audit of one independently motivated observable/background at fixed bulk theory: input, output, stationarity, deformation parameter, front exponent, and positive norm. | **Potentially high, currently speculative.** Require a mechanism changing the relevant front while retaining delay locations. A rotating external source requires accounting for pump work and may give a two-time/Floquet response, not a scalar convolution. An ideal cusp by itself need not introduce a length scale. |
| 5 | Calculate the complete Lorentzian cubic tilt kernel, including source-contact terms, only if its role in the previous candidate is clear; otherwise treat it as a physics project. | **Moderate N4SYM value; low-to-moderate direct arithmetic value.** It settles the claimed nonlinear memory and its support. It cannot by itself remove the native straight-line delay obstruction. |
| 6 | Establish the multi-angle bound, extract the three-loop corner, or study the classical kink's quantum resolution. | **Potentially substantial physics value; low present arithmetic impact.** These refine a Euclidean observable without supplying a causal signal channel. Prioritize them if the objective is a physics paper. |
| 7 | Register replay/build provenance and update stale repository-status statements. | **Useful, bounded supporting work.** No reason to defer an assessment, but important before distributing a reviewed manuscript. |

For priorities 2–3, see the [current WZW continuation](../../WZW/notes/CONTINUATION_AFTER_THERMAL_INTERFACE_TESTS_20260923.md) and [critical-path index](../../../critical-path/README.md). The latter already has an all-input finite-window anchor; the next issue is cumulative depth coupling, not rediscovering a positive sampled matrix. Suzuki's [primary paper](https://arxiv.org/abs/1204.1827) gives an explicit unconditional canonical construction for omega > 1; extension to all positive shifts remains the substantive obligation.

A possible preliminary comparison for priority 4 is the scalar-strength deformation of a Wilson line studied by [Beccaria–Giombi–Tseytlin](https://arxiv.org/abs/1712.06874). It changes a defect coupling while retaining the bulk theory, and is described by an RG flow between conformal endpoints. This is a candidate to assess, not a ready continuous family of conformal exponents or an arithmetic proposal. Direct coupling to a non-protected operator also differs from the unit-vector tilt family already tested. The fixed exponent at fixed bulk coupling and the missing delay mechanism still have to be addressed.

I would allocate the next arithmetic research session to priorities 2–3 after the focused correction in priority 1. Continue N4SYM arithmetic exploration only through a bounded task with explicit success and stopping criteria. Do not run prime fits or add modes to the existing single-pole channel: the demonstrated front mismatch is already decisive for that construction.

## Verification and provenance

All seven existing diagnostic programs were rerun with bytecode writes disabled and outputs outside the repository. All 472 cases passed: 72 straight-line, 77 trace-completion, 47 flipped-return, 56 corner, 20 rounding/closure, 107 finite-mass and 93 quartic-input. These include expected-rejection controls for the faulty dimension-two transcription; “all pass” does not rehabilitate that transcription. They are diagnostics, not interval certificates or a specialist proof review. Six outputs have floating-point differences from the stored records; all case outcomes agree. The [compact replay record](../numerics/records/codex-assessment-replay-20260924.json) records source/output hashes and comparisons with the existing records. Cross-platform byte identity is not claimed.

The reviewed checkout was clean and at `688eb8d` before this assessment. README and continuation statements that all three sessions were uncommitted are historical and no longer describe the inspected checkout. This review adds no manuscript revision, commit, or snapshot. Original notes and manuscript remain unchanged.
