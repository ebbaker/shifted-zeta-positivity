# E13 r1 source use for certified zeta balls

9 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex assistance. Recorded thread settings `gpt-6.1-sol` /
`ultra`. The per-turn backend configuration and the assisting
agent's backend settings were unavailable.

The [fixed E13 request](../research-progress/handoffs/27_TND_OC_E13_R1_CONTOUR_CENTROID_EVALUATOR_REQUEST_20261109.md)
uses scalar and cubic-series evaluations of
\(Z(z)=\zeta(1/2-iz/2)\). The isolated runtime was Python 3.12.14,
python-flint 0.9.0 and FLINT 3.6.0. The passages below were inspected
on 9 November for obligation P5 and its implementation in
[the contour evaluator](../numerics/e13_contours.py).

- Fredrik Johansson, *Rigorous high-precision computation of the
  Hurwitz zeta function and its derivatives*, arXiv:1309.2877v1,
  11 September 2013. Section 2, Theorem 1, gives a coefficientwise
  Euler–Maclaurin remainder bound for \(\zeta(s+x,a)\) when
  \(\Re(a)+N>1\) and \(\Re(s)+2M>1\). We inspected the theorem
  and its argument in the online PDF, pp. 3–4. This supplies the
  algorithm's remainder input. A bounded local PDF retrieval failed
  at DNS resolution. [Pinned preprint](https://arxiv.org/abs/1309.2877v1),
  [theorem in the PDF](https://arxiv.org/pdf/1309.2877v1#page=3),
  [BibTeX](e13_zeta_ball_sources.bib).
- python-flint 0.9.0, `acb_series.zeta`, forwards to
  `acb_poly_zeta_series` with the lesser of the series precision
  and the context cap. The execution uses four coefficients, through
  cubic order, and the exact linear input slope \(-i/2\).
  [Pinned Python wrapper](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/acb_series.pyx#L484).
- The scalar `acb.zeta` wrapper reaches `acb_dirichlet_zeta`
  via `acb_zeta`. Here the inputs are away from the pole and
  below the Riemann–Siegel cutoff \(24p^{3/2}\) at every allowed
  precision \(p\). The ordinary or reflected path therefore
  uses the same Euler–Maclaurin routine with one output
  coefficient. [Pinned Python wrapper](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/acb.pyx#L658),
  [pinned scalar bridge](https://github.com/flintlib/flint/blob/v3.6.0/src/acb/zeta.c#L20),
  [pinned scalar dispatch](https://github.com/flintlib/flint/blob/v3.6.0/src/acb_dirichlet/zeta.c).
- FLINT 3.6.0, `acb_poly_zeta_series` calls
  `acb_dirichlet_zeta_jet` for \(a=1\) and composes its jet with
  the nonconstant input. For a four-coefficient jet, the zeta code
  takes the Euler–Maclaurin path, using reflection when the real
  midpoint is negative. The Euler–Maclaurin implementation forms
  its coefficientwise remainder from the input ball, checks the
  required strict convergence inequalities with ball arithmetic,
  and adds the magnitude bound outward to the components of each
  coefficient. This encloses \(Z^{(k)}(z)/k!\) for every \(z\) in
  the segment input, including the variation over the segment.
  [Pinned series implementation](https://github.com/flintlib/flint/blob/v3.6.0/src/acb_poly/zeta_series.c),
  [pinned jet dispatch](https://github.com/flintlib/flint/blob/v3.6.0/src/acb_dirichlet/zeta_jet.c),
  [pinned remainder bound](https://github.com/flintlib/flint/blob/v3.6.0/src/acb_poly/zeta_em_bound.c).

The execution relies on the library's rigorous outward arithmetic for
the scalar `acb.zeta`, the zeta series and the elementary ball
functions. This was a selected call-chain and remainder inspection.
The wrapper was also exercised on a noncanonical complex input ball.
The contour code separately checks nonvanishing, argument branches,
integer winding, the centered midpoint remainder and the Euclidean
centroid radius. The prior argument-principle and critical-strip
source records still apply. [B07 source-use08](08_TND_OC_B07_CERTIFIED_EVALUATOR_SOURCE_USE_20261108.md),
[B10 r2 source-use14](14_TND_OC_B10_R2_CONTOUR_MOMENT_SOURCE_USE_20261109.md).
