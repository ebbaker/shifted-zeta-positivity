# Review of phase controlled delay and the cusp extension through 112

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model **gpt-6.1-sol**, reasoning effort **ultra**, verified
from the session metadata. The separate internal reviewing agent inherited
that configuration. This is internal LLM analysis and computation review,
not external peer review or formal verification.

**Assessment: approved within the stated scope.**
[Note 25](../notes/25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md)
proves the prescribed smooth delay's uniform outer comparison, including
the zeta phase. New paid interval calculations extend the finite physical
norm and both stationary-sign implications from height 104 to 112. A
stronger finite comparison holds for every earlier time, on both genuine
new stationary branches. The unbounded inner cusp and the unevaluated
finite transition remain open.

## Analytic theorem

For \(\delta=t/[2(1+t\log(1+x^2))]\), the bound
\(\tau L>\theta-\theta/(2+4\theta)\ge91/30\) on
\(\theta\ge13/4\) places both comparison times in Note 19's proved
four-jet region with one fixed margin \(1/30\). The assertion is uniform
when time decreases with height. Earlier stationarity is not imposed,
and the pointwise theorem requires no stationary branch denominator.

The full carrier ratio is used. Its zeta logarithmic-derivative integral
is bounded on the entire segment \(\Re w\ge5/4\), using the elementary
upper bound 18 for the absolute prime-power sum. Together with the gamma
term this gives \(|D|<5/4\), \(\cos D\ge7/32\) eventually. Current
stationarity gives the retained leading term \(\cos D\), with uniform
\(O(1/L)\) error. The earlier/current amplitude ratio is
\(O(e^{-L/80})\), giving the claimed eventual normalized margins
\(1/8\) and \(1/2\) for retained and absorption products.

The proof correctly retains the arithmetic phase in the moving-time
regime. It does not replace the zeta factors by 1, as was permissible
only on fixed positive-time slices in Note 24. The sharper sufficient
threshold \((11+\sqrt{217})/8+\varepsilon\) inherits the earlier-time
four-jet hypothesis; no assertion is made at zero margin.

The complex complete-source multiplier, conjugation in polarization,
independent source variables and indices, and all three omitted-pair
sectors are retained. The moving delay has its full spatial and temporal
chain rules. Higher derivative identities use complete source moments,
rather than differentiating an approximate four-jet statement. The tangent
form without a jet denominator is an identity, not a proof through a
singular branch. Physical parity, with the delayed drift kept in the
error, establishes the theorem at negative heights.

The theorem's domain already has favorable full Laguerre signs by
Note 19. It repairs this particular comparison mechanism and adds no
asymptotic sign coverage or evaluated height cutoff.

## Source payments and finite coverage

The source quadratures use python-flint 0.9.0, 192 bits, complete-index
and integration-tail payments, center jets through order 28, and full
moment bounds through order 29. The source contour identity is established
before raw-index truncation. The two omitted domains include their whole
complements; their overlap is conservatively overpaid.

The fixed cell normalization is constant in space and time. Its variation
against the contour factor is paid before spatial transport. The
space-order-12 and time-order-8 tensor Taylor remainders use the exact
heat equation and full source moments. No hidden moving centering enters
those physical jet arrays.

The two exact closed Cartesian covers have 32 cells each. All 64 whole-cell
norm floors are positive. All 128 stationary observations are either
excluded or have a strictly positive Laguerre form under the actual
stationarity condition. The shared boundaries at 104 and 108 join the
new bands to the previous cover without a missing time or spatial edge.
Evenness of the physical energy and Laguerre forms supplies negative
heights. An independently checked rational exponential bound gives
\(|F|>10^{-17}\) on both new bands; the older cover has a larger floor.

The raw driver's original uniform \(1/9\) residual-cone criterion remains
`INCOMPLETE`: 24 enclosures in the first band and 16 in the second fail
that sufficient test. Their original statuses and failed-cell lists are
preserved. Whole-cell norm positivity and pointwise stationary-sign
implications are separate valid conclusions. No failed cone is relabeled
as a successful one, and no such failure is called a negative Laguerre
form.

The only possible current stationary windows are \(107<x<108\) for
\(j=0\) and \(109<x<110\) for \(j=1\). Paid opposite endpoint signs
and strict whole-cell next-derivative signs prove exactly one genuine
regular branch on each of the eight closed time slabs. All other current
stationary points are excluded. Thus no uncounted branch creation or
boundary entry is omitted.

## Every earlier time on both new branches

The fixed half-time comparison passes all 16 cases. The stronger causal
test also passes every case for every \(0\le s\le t\), retaining
\(a=\pi/16\), \(b=1/4\), \(\lambda=1/2\), and zero losses.
It includes the smooth height-dependent rule on these finite branches.
This assertion is stated for the positive heights actually tested;
physical norm and full stationary-sign reflection require no additional
finite delayed-product claim with an unchanged drift.

For a current slab \(k\), the union of all earlier paid slabs
\(0,\ldots,k\) overcovers the causal triangle. Current and earlier time
displacements are independent, while their physical spatial displacement
is shared. Forming the difference of spatial coefficient arrays before
ranging that displacement encloses the combined absorption observation.
Both full remainders are added with coefficients 1 and 1/2. Intersections
with the stationary identity use only current stationarity.

The original coarse eight undecided verdicts are preserved. The refinement
changes enclosure arithmetic, with the same fields, domain, centering,
fraction, and losses. It certifies retained/absorption normalized margins
\(15511,7559\) on the first branch and \(6910,3371\) on the second.
No physical energy quotient is used to select or fit a loss.

The optional source-directory argument originally bound reported paths
without checking the actual imported helper files. Review identified
that reproducibility gap. The final auditor now verifies both imported
helper hashes; the independent final replay includes those checks.
The band-selection provenance is explicit: 108–112 was selected after
104–108 succeeded, before its own evaluation, using identical parameters.
No jointly blinded selection is claimed.

## Validation and reproducibility

The [21-check symbolic receipt](../numerics/PHASE_CONTROLLED_DELAY_IDENTITY_CHECKS_20261014.json)
passes exact cleared-polynomial derivative identities and rational
positivity budgets. It checks finite algebra and does not replace the
uniform analytic proof.

The [finite audit](../numerics/FIXED_CUSP_BAND_EXTENSION_AUDIT_20261014.json)
passes **1,321 checks**, including both actual import bindings. The
separate reviewing agent's exact replay is byte-identical to that saved
JSON, including all rational enclosures and every coarse/refined verdict.
The [independent review receipt](PHASE_CONTROLLED_CUSP_INDEPENDENT_REVIEW_20261014.json)
records its scope and evidence.

The parent separately reran both complete quadrature computations at
192 bits. Every field of both regenerated records matches after excluding
only `elapsed_seconds`. The [continuation validation receipt](../numerics/PHASE_CONTROLLED_CUSP_CONTINUATION_CHECKS_20261014.json)
binds those runs, source hashes, and canonical content. This is a fresh
quadrature replay in the recorded environment, in addition to exact
postprocessing replay. It is not an independent formal proof of Arb or
of the analytically reviewed source lemmas.

Reproduction commands and the remaining signed target are in Note 25.
All new permanent files are below 1 MiB. The manuscript retains its
previous integrated version; no new manuscript snapshot, commit, or tag
is part of this continuation.
