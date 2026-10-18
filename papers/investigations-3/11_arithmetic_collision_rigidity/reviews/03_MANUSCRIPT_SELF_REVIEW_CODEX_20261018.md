# Self-review: Positive Arithmetic Packets for the Theta Heat Flow

18 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewing and authoring model: **gpt-6-astra (Codex)**, reasoning effort **max**.
This is a same-assistant self-review, not an independent assessment.

## Disposition

**Working draft with written proofs of the stated auxiliary estimates and
scoped controls.** The complete signed theta residual is still open. The
canonical source compiles successfully both in the terminal and in the
built-in desktop LaTeX editor. Every printed constant enclosure and strict
headline bound passes the exact-rational checker. These checks do not
validate the analytic proofs independently.

The [manuscript guide](../manuscript/README.md) links the editable source,
23-page reading copy and reproduction instructions. No earlier investigation
is required for its definitions or internal arguments. Section 5 explicitly
states the external high-zero and strip theorems used by the controls.
Those substantial published results are imported, not reproved. Classical
Fourier inversion and Hadamard factorization are also stated at their points
of use. The packet estimates do not depend on the high-zero import.

## Source identity

The [build record](../manuscript/positive_arithmetic_packets/BUILD_RECORD.json)
has SHA-256 `da4cd58f35a9d05bb2d42fce03a00099fcdcad6b196b3b0b5c0b27f8df962986`.
Its canonical source-set digest is `9def46d014fb1006ff3a16378f66bcd1b7991ea526739b65e8bbfccaf791962e`.
The recipe and the prior research-note hashes are in that record. The following
paths are relative to the canonical manuscript project:

| Source | SHA-256 |
| --- | --- |
| `main.tex` | `4c1bb18dd2984d41afd360f40cea2c2d261050e1f02cd920c7eceecbab6d2d6a` |
| `sections/01_theta.tex` | `81f8bb1556f269fccc5ff2d2eb8683f198a0d7944b6e2417e49e5341f7812334` |
| `sections/02_packets.tex` | `5bab1829a92f7032a15d80ad874b15fff252c598b6194c07fab7efcf7d70beac` |
| `sections/03_positivity.tex` | `b58d519f090cd1782736dfe86d4042b8cad9b02f8aed22d056382bc9b54e437e` |
| `sections/04_modular_collisions.tex` | `f0dbdfeaa8aaaf3397e879514d69ccac1ee3b32d65b9d4720fea27a498b61932` |
| `sections/05_controls.tex` | `cda2aeba389128ab2a6b3b1b543e6763d7adf61d57edd2c38041a5f35006a12c` |
| `sections/06_certification.tex` | `74a2ee6178fc7b34c1ebd6fd805d2eeed298025f0bf72aaf96a4772098582c52` |

The constant checker has SHA-256 `8ca6ee691326f2fd4365651d6a7157156aa206ba39d0177d25083f52415dad99`;
the retained constant record has SHA-256 `119ef2bab05561ea0e18ff5ee58bbba5420aaf927c8af279bf3824849b28d27f`.
Hashes identify the reviewed sources; they are not proof certificates.

## Analytic checks

1. **Normalization and regularity.** Recomputed the primitive derivatives,
   the factors 8 and 16, the completed primitive's endpoint, and the Mellin
   substitution yielding H(0,z)=xi((1+iz)/2)/8. The normally convergent
   complex source sums justify real analyticity; superexponential tails
   justify all source, time and spectral differentiations. Whole-line
   Schwartz decay is used only for the complete even theta source.
2. **Finite Euler algebra and boundaries.** Checked the mixed-prime heat
   weight, the common Gaussian formula, the commuting complex-shift
   operator composition, the divergent positive-time infinite-power term
   test, and the half-line change of variables. The lower interval and
   the minus sign for the first reflected derivative are retained. Scalar
   multiplication of heat-evolved factors is not substituted for the
   operator algebra.
3. **Positive modes and quantitative estimates.** Checked the logarithmic
   derivatives of exp(t u^2) phi_n, their strict convexity for n>=2 on
   0<=t<=1/2, and the two-integration positivity identity. Rechecked the
   sinc inequality, interval u<=1/64, kappa/(4096+x^2) lower bound, geometric
   source tails, endpoint moments, and the split at |x|=64. The quotient
   derivatives give the displayed remainder bounds and the carrier
   logarithmic-curvature bound. All are uniform over the real spectral axis.
4. **Modular cancellation and event scale.** Repeated integration by parts
   gives the endpoint expansion. Derivative asymptotics are obtained from
   differentiated integrals, not by differentiating unspecified errors.
   Reflection cancels every odd endpoint. The omitted fixed finite-prime
   remainder leaves the negative inverse-square asymptotic. Checked the
   normalized drift equation, exact Laguerre identity, Taylor remainder,
   stationary branch derivative and the ratio -1/s+O(1). The factor 1/|c|
   in the normalized event error is explicit. Finite imaginary shifts do
   not lie in the bounded collision coordinate window.
5. **Coefficient rigidity and orbit controls.** Checked the Gaussian
   distribution uniqueness argument, the primitive reflection-defect ODE,
   finite-dimensional orbit nullspace, and nonvanishing of the first odd
   endpoint. The high-zero input is verified against Polymath Theorem 1.5
   and its argument-principle count; Theorem 3.2 supplies the global strip.
   Hadamard factorization gives eventual negative logarithmic curvature
   for the base theta transform; the orbit perturbation has positive
   logarithmic curvature eventually. Their ratio has one nondegenerate
   extremum in each sufficiently high gap. Freezing its multiplier gives
   the claimed double event. The perturbations retain the measurements
   and positivity but fail full modular reflection. The manuscript states
   the control result for 0<T<=1/2 and claims no uniform onset as T tends
   to zero, prescribed finite abscissa, or finite Newman threshold.
6. **Survival of the packet bounds.** The controlled coefficients lie in
   [1-eta,1+eta]. A lower-bound factor 1-eta and upper-bound factor 1+eta
   give exactly the stated k_eta estimates. Thus these auxiliary estimates,
   even with arbitrarily close constants, do not exclude the controls.

## Quantitative and document checks

The new [standard-library checker](../numerics/certify_manuscript_constants.py)
uses rational Machin enclosures and an explicitly bounded exponential
series, with outward dyadic rounding after each operation. It verifies all
Table 1 endpoints as well as the strict bounds 10.75, 117, 0.000263,
7.3e-25, 7.9e-24 and 1.7e-22. The [record](../numerics/MANUSCRIPT_CONSTANTS_20261018.json)
retains rational intervals and the script identity. It is an additional
implementation by the same assistant, not independent review. Earlier
Arb packet/boundary checks remain separately scoped in the prior reviews;
this manuscript task does not claim to have rerun those unchanged programs.

The final terminal build has no LaTeX warnings, undefined references or
box warnings. The native compiler also returned success. All 23 pages
were rendered, contact sheets were reviewed, and the title, contents,
representative long formulas, control proof, constant table and references
were inspected at readable resolution. Text extraction found no empty
pages or unresolved-reference markers; a glyph-boundary check found no
text outside the relaxed interior page rectangle. This is layout and
reproducibility checking, not proof verification.

## Claim classification and remaining work

Under [the target-restatement screen](../../../../avoid/01_restating_the_target.md),
the positive carrier and explicit uniform bounds are auxiliary quantitative
results; the signed identity and event matching equations are identities
and necessary conditions. No RH-equivalent criterion is offered as a new
theorem. The [control screen](../../../../result-summaries/12_collision_controls_and_screening.md)
is instantiated by the full orbit construction. The premise that its
coefficients fail is the complete modular reflection, not a finite prime
identity or a finite list of linear tests. The controls' scope remains the
stated class, following [the scoped-exclusion rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The manuscript says: “The identity alone does not reduce the strength of
the missing estimate.” A bound on the complete signed residual at physical
energy scale is still needed. The packet error controls a positive
arithmetic tail; it does not give a relative bound for the vanishing full
field. This is the specific cancellation lesson in
[pattern 12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
See the [result summaries](../../../../result-summaries/README.md) and
[patterns index](../../../../avoid/README.md) for repository-wide context.

This milestone is a self-contained write-up and a reproducible constant
certificate. It is not a theta collision exclusion, an RH proof, an
independent specialist review, or a novelty assessment. A specialist
review of the analytic proofs remains appropriate before publication.
