# Internal review of the microlocal manuscript

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. These are internal derivation,
arithmetic and parallel agent checks, not independent mathematical review.

Reviewed manuscript:
[Microlocal observations, coherent currents, and finite zero atlases for the Riemann heat flow](../microlocal_coherent_currents_and_zero_atlases.tex).
Its background includes all five microlocal notes and reviews, the prime
phase torus manuscript, and Heat Note 22. The new support refinement is
saved in [Note 6](../notes/6_CORRELATED_CURRENT_SUPPORT_AND_MANUSCRIPT_SYNTHESIS_20261010.md).

## Analytical and scope checks

- The Wigner convention, genuine theta state and domains, Gaussian
  variance relation, coherent-overlap normalization, entire reconstruction,
  Husimi drift/contact terms and negative momentum diffusion are retained.
  Positive genuine Husimi data are not used to assert positive evolution
  on arbitrary phase space states or scalar collision exclusion.
- All Gaussian jet and analytic normalizer derivatives are retained.
  The finite heat residual is printed. The finite approximant is not
  assigned an autonomous Newman heat equation.
- The doubled density and complete energy contain both phase differences
  and reflected phase sums. Centered block derivatives and Bell jets retain
  amplitude drift, physical carrier motion and the full complement.
- The current necessary condition requires the explicit imported full-disk
  interface. The sharp correlated support follows from maximizing
  A(1-y^2)+By on [0,1]. Sharpness is for that necessary body and does not
  imply attainment by an arithmetic candidate.
- The current cancels the carrier phase value but retains its spatial
  motion. The height-dependent gauge correction is printed explicitly.
- Every finite genuine zero theorem is conditional on the imported
  analytic approximation interface. Its normalization, reflection,
  possible disk cutoff changes, and both eta and L eta are kept.
- The four domains are exact closed disconnected windows. Natural cutoff
  constancy is checked locally; rounded hulls are distinguished from exact
  endpoints. There is no gap, entire-cell or cutoff-boundary coverage claim.
- Complete signed midpoint jets, physical spatial residual, fixed-height
  time/mixed derivatives and real Taylor remainder are correct. Polynomial
  translation is an exact algebraic identity evaluated outward. Rational
  controls are sanity checks, not formal verification of the implementation.
- All-time strict endpoint and derivative signs give exact counts and
  simplicity. Both baseline current and newer Schur acceptance are
  conjoined with a paid derivative condition already sufficient for joint
  exclusion. No additional curved-body arithmetic exclusion is claimed.
- The density-strengthened threshold coefficient and complete quadratic
  payment agree with the prime-torus background. The leading reflection
  fixes the threshold quadratic and changes the cutoff range. Overlapping
  complete product representations are not added as disjoint terms.
- No uniform current/threshold sign, shrinking-time exclusion, new Newman
  bound or RH conclusion is claimed.

Three parallel readers found no substantive mathematical error in their
assigned sections. The audit corrected the carrier-invariance wording,
disambiguated the theta density notation, made the stationary coefficient
and real-index weight explicit, and clarified complete-transform overlap.
LaTeX alignment separators and a missing delimiter were corrected before
successful native compilation. All labels, cited keys and environment
pairs also pass a source consistency check.

## Fresh arithmetic replays

Replays use Python 3.10.0 with bytecode writes disabled. Existing sources
and certificates were preserved. Each fresh output is byte-identical to its
retained record; arithmetic establishes the signs, hashes identify files.

| Retained record | Bytes | SHA-256 |
| --- | ---: | --- |
| SCOUT_CHECK_RECORD_20261010.json | 805 | 0dc97e5a9287e8c24398f02ddf45ab2b99ef52f886c0521c3f1b9d6e831fc194 |
| COMPLETE_CURRENT_RECTANGLE_CERTIFICATE_20261010.json | 12943 | 980031983c6c05b70f6bbd101dad13a2a4354dfc4c4a6b735909ddc93df423e2 |
| CANDIDATE_CURRENT_ATLAS_CERTIFICATE_20261010.json | 121956 | 8b4e46c82823c80c8cef9e079023a0b883a4bfa2a9b23dd0ded01d976b4054a5 |
| MULTI_CUTOFF_M22067_CERTIFICATE_20261010.json | 93581 | 0b61f4ed0f58ac6f3509db1eb8e36d6dc6dd754299a83384c9192e0dea60614c |
| MULTI_CUTOFF_M22068_CERTIFICATE_20261010.json | 91664 | d134c7b15eafad0a3849036700ccb2d6a0b1dbbadfc22a2cd4bd7dac0ac60645 |
| MULTI_CUTOFF_M22080_CERTIFICATE_20261010.json | 100136 | 7ca0ebd79f4f682efd823bb887d129690bfa5aefe76d6943a438e816281f0ca3 |

The complete rectangle replay took about 49 seconds in this environment.
The full atlas/family replays passed. All dependency/source hashes matched
their retained build records. A separate exact-rational inspection checks
all 135 closed atlas leaves: the stored normalized floors are conservative
relative to 2a0-eta_up or 2a1/L_up-eta_up, every remaining derivative gap
is strict, stored Schur lower bounds are conservative, and all zero bands
have opposite endpoint signs and their claimed strict derivative sign.
The compact summary checker and record are saved under numerics.

The old block source's general Decimal power routine has a weaker rounding
contract than directed elementary multiplication. The later rectangle
source overrides integer powers locally and recomputes the negative block
current. Supplementary division using that corrected interval class and
the exact rebuilt genuine endpoint weight gives

\[
-181.169105451889321242609862567243883438237799394208451566079
\le\mathcal J_B/w_M^2\le
-181.169105451889321242609862567243883438237083427191561508913.
\]

This lies strictly inside the manuscript's wider displayed enclosure.
The rectangle JSON itself stores the raw block current, not this ratio;
the ratio check uses its certified current and the printed weight formula.

## Files and completion

The stable working source is a standalone .tex file. The built-in editor
compiler reports success; no external LaTeX installation is required.
The manuscript, this review, Note 6, the summary checker/record, and the
concise project DRAFT_HISTOR.md are small files. No draft snapshot folder,
large generated data or new Git commit is created. Existing research
sources and retained numerical certificates remain preserved.
