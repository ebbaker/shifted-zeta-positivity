# Internal review of dyadic prime correlations

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Separate agents using the inherited model configuration checked the
derivation and source hypotheses. These are internal checks, not
independent specialist refereeing or a novelty assessment.

The [continuation note](../notes/selective-loss-program/08_dyadic_shifted_correlations_20261003.md)
completes the handoff's exact shifted-pair reduction. Its new unconditional
result extracts the explicit singular-series model main. The error of the
actual prime correlations remains open; no RH proof is established.

## Exact weights and complete support

Changing variables \(x=\sqrt{nm}e^z\) gives the factor \(\sqrt{nm}\),
integrand \(e^{2z}g(z+\delta)g(z-\delta)\), and both capped limits
in equation (2). The alternative ratio-coordinate calculation agrees.
The factor two in the shifted expansion counts each unordered pair once.

The exact support is \(h<2(B-A)X\) and
\(\max(AX,h/(B/A-1))<n<2BX-h\), without rounding real \(X\).
Vanishing weights make boundary-atom conventions immaterial. The two
altered pair blocks are disjoint because \(B<2A\); they differ from the
regions where a single packet is partial.

The continuum row cancellation uses \(\int w=0\). Replacing cap
weights by whole packets over the complete active coordinate band creates
the positive \(X^3\) square in equation (9). Discarding atoms outside
\([X,2X]\) is a different boundary error. Both are checked separately.

## Diagonal and singular series normalization

The conversion \(\int w^2=\int g^2=1\) gives coefficient
\(\int_1^2t\,dt=3/2\). The actual diagonal's leading asymptotic uses
PNT for \(\sum\Lambda(n)^2\), not a pair conjecture. Equation (7)
is an exact continuum logarithmic diagonal, correctly distinguished from
a stronger constant-order asymptotic for the actual diagonal.

The collapse is \(H_X(h)=X^2F(h/X)\). The properties \(F(0)=3/2\)
and \(\int_0^\infty F=0\) fix both the trapezoid baseline and leading
singular-series coefficient. Its additive autocorrelation of \(w\) is
distinct from the earlier logarithmic autocorrelation.

[Montgomery and Soundararajan, equation (16)](https://arxiv.org/pdf/math/0409258)
uses an ordered-pair sum equal to twice the triangular sum \(T(H)\).
This gives the essential factor one half in equation (13). Real endpoint
interpolation adds only \(O(1/H)\) to the smooth main's error.
Distributional twice partial summation has normalization \(X^{-2}\);
\(T(0)=T'(0)=0\) and compact support remove boundary terms.
The identity \(\int qF''=F(0)\) fixes the logarithmic sign and constant.
The bounded initial interval is handled separately, without using the
large-argument error at zero.

Thus the explicit model main is
\(-\tfrac32X^2\log X+O_g(X^2)\), canceling the leading diagonal
in the model. Actual correlations enter only through \(\mathcal R\)
in equation (16); this error is not bounded by the singular-series theorem.

## Remaining target and arithmetic hypotheses

Equation (17) is exact. Consequently
\(\mathcal R(X)_+=O_g(X^2\log(2X))\), after the complete signed sum,
is equivalent to the dyadic target and retains its RH strength.
Equation (19) keeps all caps and vanishing endpoints. Its derivative has
pointwise size \(O_g(1)\) and total variation \(O_g(X)\), uniformly in
active shifts. The density-one parity obstruction is restricted to blocks
of length comparable to \(X\), not shrinking support intervals.

[Matomäki, Radziwiłł, and Tao](https://arxiv.org/pdf/1707.01315),
Theorem 1.3 and footnote 6, were checked directly. The quoted theorem has
a restricted range and exceptional shifts, but the authors also describe
proportional-range extensions. Range alone is not asserted to be a
fundamental obstruction. Even granting those extensions and cap uniformity,
absolute logarithmic errors cost \(X^3\) times logarithmic savings;
hypothetical individual square-root errors cost \(X^{5/2+\epsilon}\).
Neither supplies the required signed aggregate cancellation.

The singular-series input is unconditional. Montgomery--Soundararajan's
actual-prime moment theorem has separate tuple hypotheses, including a
one-point RH-strength estimate. The needed Selberg scale in note 06 also
assumes RH. Neither is accepted as an unconditional actual-correlation bound.
The higher-power reduction correctly uses the signal's bounded correction
and the triangle inequality, without claiming a controlled mixed variance
before the prime signal is bounded.

## Numerical replay and saved scope

The [diagnostic](../numerics/selective_loss_dyadic_pairs_20261003/README.md)
was run by its author and rerun by the coordinating agent with the existing
Python 3.10 and NumPy 1.25.1. All assertions passed. Four noninteger shells
and samples around genuine support transitions check direct squares, two
pair coordinates, shifted grouping, symmetry, and support. The largest
principal direct-square/pair residual is about \(1.68\times10^{-10}\).

Independent continuum quadratures confirm complete cancellation, shift
collapse, and both artificial \(X^3\) boundary errors. Whole-packet
replacement gives coefficient about 0.0277206222438185; discarding atoms
outside \([X,2X]\) gives about 0.0065923154786104. These are floating
comparisons, not outward enclosures, real-interval certificates, or global
arithmetic estimates. The small record retains the script hash and parameters.

The note, numerics, and review use the existing investigation folders.
The overview, index, and handoff point to the current target. Existing
manuscript edits and other research were preserved. No new manuscript
milestone, snapshot, commit, or push was created.
