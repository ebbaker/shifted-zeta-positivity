# Inverse bulk realization of the localized Weil form

15 September 2026. Fit the **complete** localized Weil pairing to an
independently positive field-theoretic or observable-sector norm.
The intended contribution is an exact matching theorem, potentially
conditional on construction of a credible specified theory. An already
completed construction is not an eligibility requirement.

The [current working manuscript](manuscript.pdf), *Sphere and Schur sources for
the localized Weil form*, collects the present results in a self-contained
draft. Its [TeX source](manuscript.tex) has internal equation labels and does
not input the shared background. Reviewed versions are preserved in
[drafts/](drafts/README.md); version 0.5 is current and versions 0.1 to 0.4
are preserved unchanged.
See the [build guide](BUILD.md) and [coverage map](MANUSCRIPT_COVERAGE.md).

Start with the [broad program overview](../../brainstorm/INVERSE_BULK_AND_DEFECT_DIRECTIONS.md)
for the ideas and alternatives. The
[current focused investigation](notes/SCHUR_DRESSED_RETURNS_AND_GLUING.md)
constructs dressed Schur return states, computes their full local norm,
and tests their magnetic domain and two-prime gluing.
No system has yet supplied the full Weil pairing. The working manuscript
records the preliminary source results and open joint matching problem;
it does not announce a completed reduction to a particular field theory.

## Reading map: broad material and focused calculations

| Document | Scope | Role |
|---|---|---|
| [Working manuscript](manuscript.pdf) | Synthesis of current results | Self-contained target, exact source calculations and proofs, scoped exclusions, and the remaining full matching problem. |
| [Dated drafts](drafts/README.md) | Version history | Complete buildable snapshots with PDFs and file hashes; earlier versions are preserved unchanged. |
| [Program overview in brainstorm](../../brainstorm/INVERSE_BULK_AND_DEFECT_DIRECTIONS.md) | Broad | Motivation, the conditional-construction goal, broadened boundary concepts, candidate families, and criteria for a specific paper. |
| [Defect-observable survey](notes/DEFECT_OBSERVABLE_SURVEY.md) | Broad | Literature comparison and alternatives, including Liouville, integrable defects, gauge networks, and arithmetic/free-field controls. |
| [Foundational analysis](notes/ANALYSIS.md) | General framework, with specific model tests | Full matching target, physical positivity, rational-feedback obstruction, positive gamma refinement, and the original junction proposal. |
| [Two-channel exclusion](notes/INTERFERENCE_BOUND_AND_TWO_CHANNEL_EXCLUSION.md) | Focused; current | Why the gamma-plus-prime architecture cannot be completed, with certificates and the extent of the exclusion. |
| [Mirror reference and subtraction form](notes/MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md) | Focused; current direction | The prime-free subtraction form of the target and the two objects left to construct. |
| [Dressed Schur returns and gluing](notes/SCHUR_DRESSED_RETURNS_AND_GLUING.md) | Focused; current | One fixed Schur parameter, an exact positive local prime norm, its compulsory contact, magnetic domain requirements, and a mixed-return gluing test. |
| [Sphere and Schur pairings](notes/SPHERE_AND_SCHUR_PAIRINGS.md) | Focused; first comparison | Gaussian boundary gamma data, interacting rank-one norms, conformal Wilson pairing, Schur local-factor and common-state tests, and the next source choices. |
| [Gauge-transfer test](notes/GAUGE_TRANSFER_TEST.md) | Focused; earlier | Winding versus transfer, a positive disk model, and two first-prime preparations with exact mismatches. |
| [Notes index](notes/README.md) | Navigation | Reading order and the status of each retained note. |
| [Mirror dressing and reachable states](notes/MIRROR_DRESSING_AND_REACHABLE_STATES_20260915.md) | Focused; current | Why the mirror prime reference is reachable in the elementary Schur representation, the characterisation of reachable output states, and why weight-matching in a positive sector carries little information. |
| [The pole term needs no mechanism](notes/POLE_TERM_NEEDS_NO_MECHANISM_20260915.md) | Focused; current | Why no ghost pair is required or possible, the quantitative smallness of the pole form's negative direction inside the prime-free form, and the corrected construction target. |
| [Gamma compression presentation](notes/GAMMA_COMPRESSION_PRESENTATION_20260915.md) | Focused; current construction target | The target as a compression of the gamma energy, with both sides manifestly positive and an explicit source on the dominating side. |
| [Continuation note](notes/CONTINUATION_20260915.md) | Handoff | Where the investigation stands, the ordered next steps, and what not to redo. |
| [Exclusion map](notes/EXCLUSION_MAP_20260917.md) | Synthesis; current | Every exclusion so far, by kind of argument, with each scope clause explicit, and what remains untouched by any of them. |
| [Context note, 17 September](notes/CONTINUATION_20260917.md) | Handoff; context only | What the reading session of 17 September covered and the state it found. No next steps. |
| [Reviews](reviews/README.md) | Assessment | Dated reviews of manuscript versions, with the revisions each prompted. |
| [Checks and records](numerics/README.md) | Supporting calculations | Small reproducible algebra programs and their explicitly scoped results. |

The latest note gives an explicit electric dressing and one magnetic
insertion whose positive norm has every required single-prime repetition
coefficient. All primes use the same Schur quantization parameter. The
norm also fixes the known positive contact: this is an explicit Schur
realization of the existing positive prime reference, not a full Weil
identity. A simple coherent sum produces forbidden mixed returns.

**Version 0.2 settles what that construction can become.** The manuscript now
records the target in spectral form, and proves that the architecture the
dressed construction leads to cannot be completed: by an elementary
interference bound, no coherent source has the positive gamma energy and the
summed positive prime references as its two channel norms. The bound fails at
explicit test functions --- the indicator of the interval already violates it
at \(L=5/4\) --- and fails by a growing factor as \(L\) increases. The
negative contact and the rank-two pole term must therefore come from a
compression or projection inside one space, not from further positive
channels. That, rather than another prime-channel identity, is the next
object to construct.

**The narrowed direction now has a concrete form.** A mirror of the positive
prime reference, carrying the same atoms with the opposite sign and a strictly
smaller contact, turns the target into a *difference*,
\(Q_L = A_L - \sum_p \tilde B_p\), in which \(A_L\) contains no prime
translations at all and is robustly positive where \(Q_L\) barely is. Weil
positivity on \(I_L\) becomes one domination statement. This is Section 7.5 of
version 0.4; its derivation and the open pieces are in the
[subtraction-form note](notes/MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md).

**The pole term now has a specification rather than a list of options.** In the
coordinates given by the evaluations at \(s=0\) and \(s=1\) the rank-two pole
form is off-diagonal -- the hyperbolic pairing of the two poles, with each
evaluation a null vector -- and every source for the localized form carries a
unitary involution exchanging them, which for a compatible realization is the
functional equation acting on the zeros. A realization must therefore supply a
null pair, not a removed state, and the subtraction may act only on the
reflection-odd part. This is Section 2.5 of version 0.4; the prime-free
inequality (8.1) is settled for \(L\le\log 2\) by Yoshida and for
\(L\ge\log 7\) here, leaving the compact window \(\log 2<L<\log 7\). See the
[prime-free note](notes/PRIME_FREE_ARCHIMEDEAN_INEQUALITY_20260915.md).

**Remark 7.10 is settled and its answer narrows nothing.** The mirror weight
is produced by one magnetic insertion on an admissible electric preparation at
the same fixed \(q\) as the positive reference, and in fact every output state
analytic past the unit circle is reachable. So the mirror does not require its
own protected sector, and the appearance of a prime weight in a positive sector
is a statement about the dressing rather than about the representation. This is
Section 6.5 and Corollary 7.10 of version 0.5; the research is in the
[mirror-dressing note](notes/MIRROR_DRESSING_AND_REACHABLE_STATES_20260915.md).

**The pole term needs no mechanism, and Section 8.2 needs a correction.** The
ghost pair asked for there cannot exist in a realization --- by
Corollary 2.2 a compatible one is evaluation on the zeros in a positive
\(\ell^2\) --- and is not needed, because under the subtraction form the pole
term sits inside the positive prime-free form \(A_L\), absorbed by the same
domination that absorbs the negative contact. Its negative direction is rank
one, bounded by \(2(\sinh(L/2)-L/2)\), and far from binding: below \(\log 2\)
the binding direction of \(A_L\) is even, where the pole form is *positive*.
The construction target is therefore the first half of
Problem 8.3 --- a positive source for \(A_L\), reflection covariant, with no
prime translation --- and then the mirror references as a compression of it.
The claim is withdrawn in Section 8.2 of version 0.5; the research is in the
[pole-term note](notes/POLE_TERM_NEEDS_NO_MECHANISM_20260915.md).

**The construction target is now one compression of the gamma energy.** Splitting
the pole form by parity puts its positive half on the source side and its
negative half on the subtracted side, giving \(Q_L=K_+-T_L\) with
\(K_+\) the gamma energy plus a constant and a rank-one term --- manifestly a
norm, with an explicit source --- and \(T_L\) the negative contact, the odd
pole direction and every mirror prime reference, manifestly positive. Weil
positivity on \(I_L\) is then the single domination \(T_L\preceq K_+\), with no
unproved inequality anywhere in the presentation: in particular the prime-free
inequality (8.1) is not a prerequisite for the construction programme. This is
Section 7.6 of version 0.5, and Problem 8.3 is restated accordingly; the
research is in the
[gamma-compression note](notes/GAMMA_COMPRESSION_PRESENTATION_20260915.md).

## Working direction

Continue with charge-neutral Schur RG/interface preparations that retain
the full gauge and Weyl terms, alongside sphere boundary/vortex modules
with an actual correspondence on the Gaussian normalization control.
Every candidate must now also pass the interference bound of Section 7.4
for each decomposition whose channel norms it computes separately, and must
produce the contact and the signed poles from one mechanism. Compare the
compressed-scaling-action mechanism of Connes and Consani, cited in the
manuscript, which produces a negative archimedean contact by projection.
A failed identity changes the choice of source or model;
it does not initiate progressively more complicated residual estimates.
Retain the other systems as alternatives. Use this working manuscript to
develop the current calculations; specialize the proposed field-theory
reduction when a concrete joint source and complete matching results justify it.
Only the forward construction-to-RH direction belongs to this program.

## Reproduction and preservation

Run from this directory:

```sh
python3 numerics/check_matching.py
python3 numerics/check_gauge_transfer.py
python3 numerics/check_sphere_schur.py
python3 numerics/check_dressed_schur.py
python3 numerics/check_explicit_formula.py
python3 numerics/check_channel_bound.py
python3 numerics/check_mirror_subtraction.py
python3 numerics/check_mirror_dressing.py
python3 validation/drafts.py check --replay
```

The programs print small records and do not overwrite the preserved
results in `numerics/records/`. The three original research notes now
live in `notes/`, with their filenames retained and navigation repaired.
The earlier check programs and records are preserved unchanged; the
generic `checks.json` is now `numerics/records/matching-checks.json`.
Successive focused notes and their checks document each continuation separately.
The [draft tool](validation/README.md) records reviewed builds and saves new
versions without overwriting historical drafts.
Follow the repository's [large-file policy](../../../../LARGE_FILES.md).

Related material: [shared framework](../../PROGRAM_OVERVIEW.md),
[ground-state geometry](../arithmetic-ground-state-geometry/README.md),
[earlier assessment](../../brainstorm/ASSESSMENT.md), and
[finite-response novelty assessment](../../manuscripts/finite-response-weil-positivity/EVALUATION.md).
