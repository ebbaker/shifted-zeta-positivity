# Canonical-energy U4 source scope review

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred.

Reviewed [the U4 note](../notes/8_CANONICAL_ENERGY_CROSSWALK_20261013.md)
against `openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, with focused
parallel checks of arithmetic/normalization and quantifiers/weights. These
are same-team, same-family assessments by contributors to the source pass,
not independent mathematical validation. No new mathematical compilation,
VM mutation or network access was used for these checks.

**Finding: no concrete mathematical defect found in the conditional
paper-level derivation.** The genuine presentation of the supplied O5
character, including its original defining-modulus zeros, remains an input.
The note explicitly preserves the earlier trace/Gauss dictionary obligation
and classifies the newly assembled Lean applications as uncompiled.

The substantive checks were:

- The target uses squarefree ideal columns and labels counted once, and all
  nonzero element rows. Primary-generator changes reindex the full row ball
  and do not divide its energy by six. The moving fourth-power label is
  retained rather than replaced by the terminal U1 label.
- The normalized energy has one scalar inside each norm square. Covering
  labels below `2F` halves the target energy at the enlarged normalizer and
  doubles the source RHS, giving the stated factor four. After profile
  dilation, the original outer normalizer adds a further `a_j`, producing
  the stated `a_j^2` contribution.
- `secondLabelWeight 0` is the ninth power of the label-divisor count. The
  unit ideal is a divisor of every nonzero label, so dropping to unit weights
  is valid without a divisor-count estimate or epsilon loss. The two source
  predicates named `Admissible` are distinguished and their required
  hypotheses are kept explicit.
- The existential mode degree precedes the rational period, and the energy
  constant precedes the freely enlarged natural pool cap. That cap is
  distinct from O5's physical outer parameter. The chosen cap covers the
  entire fixed reference profile, not merely the target annulus.
- The rational period covers the character modulus and all original `S`
  primes. Its additional exclusions are restored by a finite squarefree
  factor decomposition using the source's positive fourth-power CRT law.
  The outside scalar is bounded by one. Shared factor/label primes give
  zero; surviving multiplied labels are admissible and injectively indexed.
  Rank labels may contain pool-excluded primes, which is essential here.
  The decomposition keeps `XF` and the full row support unchanged.
- The fixed reference annulus lets the derivative order be chosen before
  arbitrary support intervals and fixed arithmetic data. The canonical
  clipped-energy theorem supplies homogeneous quadratic Fourier dependence.
  The `J+2` integration-by-parts order and finite dyadic partition give the
  stated ordinary smooth seminorm bound without changing that order.
- Both canonical margins hold after dilation and restoration, with fixed
  threshold enlargement, `Mcap=C0`, `Fcap=C0+1` and gap `kappa/2`. The shifted
  column scale below one is handled by direct unit-weight counting with
  constant `2*128^4`, retaining both squared-amplitude and outer counts.
  Bounded outer scales, including one, use direct counting without logs.

All 38 selected Lean files and 43 anchor excerpts match the byte identities
in the [source-contract record](../numerics/canonical_energy_crosswalk_20261013.json)
and the preserved closure manifest. The root additionally rechecked all
2,926 copied OAI files for byte count, SHA-256 and Git blob SHA-1. These
identity checks do not verify a new proof term.

Editorial checks corrected two malformed squarefree conditions, the
`Mellin/LogProfiles.lean` link, the September 30 `build/paper.tex` link and
the exact declaration label `mem_idealDivisors`. The source-contract record
was regenerated after final note edits so its note hash identifies the
saved version. None of these corrections changed the derivation.

The outstanding formal work is explicit: supply the input character and
coefficient agreement, compile the unit-weight dyadic specialization,
assemble the extra-prime restoration and image-label terms, prove the
fixed-annulus ordinary/logarithmic seminorm conversion and partition, and
compile the moving/bounded-scale substitutions. This review does not close
U4 formally, certify U5--U7, or replace a Claude/external review.

The separately preserved zeta comparator acceptance is evidence for its
nominated universal target under the recorded checker assumptions. It does
not compile or certify the O5 application assembled here.
