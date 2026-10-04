# Gaussian localization for height adapted zero detection

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This investigation develops a Gaussian inverse test for the prepared
height-adapted prime scalar. The aim is a finite-interval detector that
handles clustered zeros and specifies every physical and spectral tail
before an arithmetic saving is proposed.

The [opening investigation](INITIAL_INVESTIGATION_20261004.md) establishes
the full Mellin identity, exact pole subtraction, a carrier-uniform weighted
inverse-kernel norm, and finite physical-window error budgets. A power-sum
argument with linked Gaussian parameters supplies a zero-side lower bound
without zero separation or an exposed-zero replacement. Its constants were
initially unevaluated; the continuation below makes them effective.

The [explicit-constants continuation](EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md)
proves an effective global transform lower bound, weighted inverse norm at
most 32, physical and pole constants, and an explicit published zero-count
input. For every carrier magnitude at least 100 it replaces the opening
log-prime-scale cover by \([24(N+1),208N]\), with every displayed omitted
budget below its allowance. It gives one explicit sufficient arithmetic
inequality for a finite-box exclusion. That arithmetic inequality remains
unproved; no new zero-free region or actual zeta-zero certificate is claimed.

The [finite Gaussian Möbius reduction](FINITE_GAUSSIAN_MOBIUS_REDUCTION_20261004.md)
now removes all divisors up to exp(15k) at an explicit cost and leaves a
finite signed sum with dr <= exp(26k) and r < exp(11k). Its upper product
and optional frequency tails fit the detector allowance. Bounding this
sum at every required carrier and Gaussian sample is an alternative
sufficient arithmetic criterion; its signed cancellation is still open.
The [height-uniform Vaughan comparison](HEIGHT_UNIFORM_VAUGHAN_REDUCTION_20261004.md)
also makes the original scalar gate's derivative and cutoff error explicit,
retaining its continuum, product caps, and full prime powers.

Read the parent [overview](../README.md),
[coefficient lemmas](../DETECTOR_LEMMAS_20261004.md), and
[prioritized assessment](../PRIORITIZED_ASSESSMENT_20261004.md) for context.
The internal reviews cover the
[opening analysis](../../../reviews/height_adapted_zero_detection/gaussian_localization/INITIAL_REVIEW_20261004.md),
the
[effective constants](../../../reviews/height_adapted_zero_detection/gaussian_localization/EXPLICIT_CONSTANTS_REVIEW_20261004.md), and the
[arithmetic reductions](../../../reviews/height_adapted_zero_detection/gaussian_localization/ARITHMETIC_REDUCTION_REVIEW_20261004.md).
The [numerics directory](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
contains the initial floating diagnostics and the continuation's exact
rational checks with outward elementary-function enclosures, formal signed
coefficient identities, and effective arithmetic reduction constants. These
check algebra and budgets, not the actual zeta zero set or arithmetic saving.

## Next questions

1. Test one complete signed dyadic estimate for the new finite Gaussian
   target, preserving every product cap and specifying the full carrier
   range. A short Poisson-saddle analysis may reduce the divisor cutoff
   before any large numerical sweep.
2. Run the smaller-guard Gaussian parameter trial through all finite-height
   budgets and compare its arithmetic cost with the proved baseline.
3. Decide whether a count restricted to the right part of the strip can
   reduce the power-sum loss; the current guard count already charges all
   zeros, so splitting off left zeros brings no count saving by itself.
4. Establish an independent arithmetic inequality that beats the explicit
   detector threshold, then compare any exclusion against current classical
   zero-free inputs and verified finite heights.

Save continuation notes here, numerical sources and small records in the
linked numerics directory, and reviews in the linked reviews directory.
Follow the repository large-file policy. Keep the single manuscript and
existing investigation records; milestone history belongs in concise Git
commit or tag entries rather than new manuscript snapshot folders.
