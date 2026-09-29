# Critical review: weighted tail and discrete spectral obstruction

28 September 2026. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured effort not exposed. Root synthesis reviewed against two separately developed mathematical arguments and a bounded numerical subtask. All checks are by agents of the same model family, not independent human refereeing or formal verification.

## Scope and outcome

The [main note](../notes/CCM_WEIGHTED_TAIL_AND_DISCRETE_OBSTRUCTION_20260928.md) advances from the round-7 sharp weighted inequality to a whole-line spectral reduction. The independently developed [prime-return proof](../notes/CCM_PRIME_RETURN_AND_EXTERIOR_COERCIVITY_20260928.md) and [weighted-operator proof](../notes/CCM_WEIGHTED_OPERATOR_SPECTRAL_REDUCTION_20260928.md) agree on the exterior threshold 1/4. The latter additionally establishes local compactness, the essential lower edge, and quantitative fixed-depth localization without a prime number theorem.

No substantive contradiction was found in the new derivations. Their claims remain working mathematical proofs based on the exact Xi-kernel and Weil-form inputs established in the earlier notes. They do not establish the sharp global gap, RH, or the CCM determinant limit.

## Mathematical checks

| Issue | Checked conclusion | Limit retained |
|---|---|---|
| Normalization | Literal kernel has transform Xi/4, weighted mass 1/8, and threshold 1/4 | Rescaling k changes the numerical operator threshold; normalizations must stay consistent |
| Pole cancellation | Both pole ranks cancel in the full-parity jump identity; restricting to even functions gives the stated operator | Products involving the logarithmic multiplier are closed forms, not bounded operators |
| Weighted primes | Shift norms are bounded by C² exp(−2cn), giving an absolutely norm-convergent sum | Individual weighted shifts and K are generally not compact on ordinary L2 |
| Exterior estimate | Both endpoints outside R give the stated superexponential lower defect, uniformly over the exterior form domain | It bounds the complete form; it is not a sharp prime-counting error estimate |
| Domain and core | The positive form has domain av in the logarithmic Fourier space; cutoff and mollification prove the compact smooth core | One must justify multiplication and closure before using spectral identities |
| Local compactness | Compact restriction follows from logarithmic frequency growth and a bounded below on compact intervals | Global compact resolvent does not follow and is false at the threshold |
| Relative compactness | K times the form resolvent is compact, using local compactness and the weighted prime norm tail | Finite-rank operator-norm approximation of all K is not asserted |
| Essential edge | Relative compactness gives the lower bound 1/4; infinitely many exact threshold eigenfunctions give equality | The entire essential spectrum is not identified |
| Zero mode and gap | Positive gamma conductance forces constants as the sole zero mode; discreteness below 1/4 gives an unspecified positive gap | The sharp gap 1/4 remains exactly the missing RH claim |
| Localization | The single-cutoff identity retains every prime jump; its gamma factor 1/2 and prime factor q_n give the stated bound | The tail estimate worsens as spectral depth tends to zero |
| Signed Birman–Schwinger count | The closed-form congruence gives the strict inertia counts without K being positive | The known zero mode contributes one count but is not generally an eigenvector of the compact operator itself |
| PNT proof | The explicit Johnston–Yang estimate is unconditional; Stieltjes endpoints and all required prime powers are included | Its rate bound is much weaker than the exact combined-form lower estimate |

The cutoff localization argument was checked independently against the squared-difference identity. For a normalized eigenfunction with eigenvalue at most 1/4−delta, it gives exterior mass at most e_R/(delta−d_R). The errors vanish superexponentially, but no fixed compact interval is claimed to control all eigenfunctions as delta tends to zero.

## Traps excluded explicitly

1. **Confusing two truncations.** Cutting the positive prime jump energy deletes its long-jump diagonal and leaves gap zero. Cutting only the bounded weighted off-diagonal prime series while retaining the exact complete diagonal is a different, norm-controlled approximation.
2. **Calling a weighted shift compact.** Spatial decay alone does not remove compactly supported high-frequency oscillations. Compactness enters only after using the logarithmic form domain or its resolvent.
3. **Concluding RH from the essential edge.** Discrete eigenvalues may lie in (0,1/4), and infinitely many may approach 1/4. The theorem excludes an essential subthreshold branch, not those eigenvalues.
4. **Replacing all spectral depths by finitely many.** The exact count must equal one for every 0<lambda<1/4. A fixed-depth certificate leaves a threshold layer. Norm errors are amplified by 1/(1/4−lambda).
5. **Claiming determinant convergence.** The positive weighted operator is an alternate precise RH target. The original CCM ground-profile, normalization, and moment requirements are not supplied by this reduction.

## Numerical and source checks

The separate [diagnostic](CCM_PRIME_RETURN_DIAGNOSTIC_20260928.md) contains eight rate calculations, not eigenvalue evidence. All required prime powers are sieved exactly; logarithms, quadratures, and theta values are floating. The 80/110-digit runs match at the saved 45-digit serialization except for working precision and roundoff fields, and their generator hashes match. The Stieltjes replay also checks the finite step bookkeeping. No interval arithmetic, uniform numerical claim, or zero data is used.

Primary inputs were checked in [CCM, Section 3](https://arxiv.org/html/2511.22755v1#S3) for the Weil decomposition and [Johnston–Yang](https://arxiv.org/abs/2204.01980v2) for the unconditional PNT bound. The new spectral and counting deductions are supplied in the local notes, not attributed to those papers.

## Research decision

This is a useful completed reduction: full-support exterior control, essential-edge identification, and a compact problem at each fixed spectral depth are now available. The next theorem to seek is a one-negative-direction bound for the pole-free weighted operator, or a uniform bound on the second Birman–Schwinger eigenvalue up to the threshold. Neither a larger finite-L matrix nor a longer prime-return table supplies that theorem.

Sonin residuals remain deferred. The research indexes are updated; no manuscript snapshot, commit, or push is part of this continuation.
