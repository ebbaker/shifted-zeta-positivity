# Book rewrite: same-assistant assessment

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.
Chat0015, Draft book rewrite change note.

**Status: exact identities integrated into an initial book draft;
same-assistant analytical and layout checking.** No new collision
exclusion, numerical certificate, or independent specialist review.

## Implemented scope

The [book](../book/main.tex) now follows the original
[rewrite plan](../book/changes/02_REWRITE_20261028.md): brief xi and
de Bruijn-Newman background, the Gaussian coefficient calculation,
smooth potential V, generator G, and the cylinder observation. It retains
the original H normalization. The later alternative is preserved
byte-for-byte in [change03](../book/changes/03_THREE_DIMENSIONAL_NOTATION_ALTERNATIVE_20261028.md)
and is also developed in manuscript Section 4 as a separate normalized
three-dimensional presentation. This follows the user's final instruction
to include both, without replacing the original notation throughout.

## Analytical checks

- Source normalization: Dobner's source is 4 Phi, hence xi_t=8H in
  the stated coordinate. The whole-line H integral has factor 1/2.
- The Gaussian coefficients select dimension three; the regular radial
  Laplacian is distinguished from its distributional point source.
- The potential V=1+1/r-Theta has cancelling central sources and no
  sphere interface. Its positive Newtonian representation has radial
  mass 1, and its stated endpoints fix the normalization.
- The square-root conjugation gives (1-d_u^2)G=8 Phi. The decaying
  inverse is G=4 exp(-|.|)*Phi, giving the factor 16 in its observation.
- Euclidean and cylinder measures agree through dX=8 pi r^3 dmu;
  cylinder metric volume is pi dmu. Both original and normalized
  three-dimensional formulas retain these constants.
- The potential and G integrals converge in |Im z|<1. The P companion
  retains its additive 1 and proves H(0,+/-i)=1/16 by continuation.
- Spherical-mean inversion has coefficient 8/pi. Recovering V adds
  the factor 2/sqrt(r), giving 16/(pi sqrt(r)). Fourier uniqueness
  applies to integrable means; the displayed pointwise inverse uses
  the stated Schwartz hypothesis.
- Spectral differentiation retains the derivative of 1+z^2. At a
  zero, its extra term vanishes, yielding the two cancellation equations.
- Newman evolution acts through L^{-1}u^2L on the source-defined class;
  direct multiplication of G by exp(tu^2) is not substituted for it.
- The four differential relations in the combined-flow proof give
  the displayed secant/tangent solution and its admitted interval.
  The linear combination transports existing zeros; it supplies no
  additional collision exclusion.

## Controls and limits

Manuscript Section 6 includes the inherited positive Gaussian-polynomial
control, its explicit double zeros, and the local time domain. Its
missing premises are the canonical integer-square expansion, completion,
and double-exponential tails. The Green transform and linear benchmark
retain its event where defined. Euler-factor, weighted-square, reflected,
and positive-primitive controls are distinguished by the separate failed
premises in the existing control register. No new numerical run is needed
or claimed for these exact inherited formulas.

The [result index](../../../../result-summaries/README.md), especially
[geometric realizations](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md),
and [pattern index](../../../../avoid/README.md), especially
[coordinate re-realizations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
retain their force. This is an expository milestone, not a new estimate.
The auxiliary evolution and any canonical separating estimate remain open.

## Build and visual verification

The saved source compiled successfully with both local latexmk and the
desktop LaTeX compiler. The final local log has no LaTeX, overfull, or
underfull warnings; all 65 labels are unique and all references resolve.
All 11 pages were rendered at 110 dpi and visually inspected in page
contact sheets: no observed clipping, overlap, broken symbols, or missing
equations. The PDF is an ignored reading copy under the shared output
folder. [Build record20](../numerics/20_BOOK_REWRITE_BUILD_RECORD_20261028.json)
records source/PDF hashes, the preserved alternative, and verification scope.
