# S06-T2 bounded completed-current internal review

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**. Separate delegated same-model review and execution;
no independent quadrature implementation or specialist human review.

**Disposition: pass as a scoped unsuccessful bounded comparison.**
The complete current estimate signs 60 of 64 cells at both precisions;
the same-ball direct first-jet consumer signs all 64. The four current
failures yield no positive uniform current radius, while the direct
physical radius is greater than 0.0190407974544 in units of sqrt(E)/Gc.
Every successful current cell has a strictly smaller extracted radius
than the direct certificate. S06-T2 is complete only as this bounded
attempt; its quantitative benefit gate failed and the broader independently
useful arithmetic/geometric estimate remains open.

The [research note][note] was checked against the unchanged T1 derivation,
the frozen [comparison contract][contract], source evaluator and tail
theorem. The repository [result summaries][summaries] and [patterns to
avoid][avoid] govern the scope, especially [collision controls][controls],
[scoped exclusions][scope] and [same-model review][same-model].

## Mathematical checks

With a=165+4t+x^2 and beta=2tx/a, the twice-centered observation is

\[
 \mathcal R=\mathcal L_0-\beta(\mathcal L_0)_x
 =\frac{64}{11ta}\left(J_{2c}-\frac{11t^3}{16}\mathcal L_1\right).
\]

The physical current factor and the sign in the beta derivative term
agree with T1. Dividing by the fixed Gc squared gives exactly the code's
normalized quadratic r; the Cauchy extraction returns sqrt(E)/Gc.
No derivative of Gc, the frozen contour or the cutoff is taken.

For even ft, direct product differentiation first gives
L0=(1/8) integral integral (u-v)^2 ft(u)ft(v) cos(x(u+v)).
Reflecting v gives the note's (u+v)^2 cos(x(u-v)) kernel. Its x derivative
is minus (u-v)sin(x(u-v)); hence the plus beta sine term is correct.
All products use the complete decaying physical source. The four raw
C2 product pieces cannot be integrated separately at the negative cusp.
The primitive relation 8hj=Ij+delta_j0/2 gives the lower-edge contribution
(-I2+beta I3)/128, with zero constant corner after the full subtraction.

For v=(V0,V1) and w=(-V2+beta V3,V1-beta V2), r=v dot w.
The exact Cauchy identity is

\[
 \|v\|^2\|w\|^2-(v\cdot w)^2=(v_0w_1-v_1w_0)^2\ge0.
\]

A complete positive lower ell and independent finite upper M therefore
give sqrt(E)/Gc >= ell/M. This uses a higher-jet upper bound obtained
from source data, rather than assuming first-jet positivity.

On a common Cartesian input set, select a least-norm allowed first-jet
pair and any allowed higher jets/coefficient. Then ell<=r<=D M at that
point, proving C<=D for this scalar extraction and information class.
The source need not realize every tuple in the Cartesian set: validity
of the declared interval consumer is precisely over that larger set.
This is not a universal prohibition on correlated current estimates,
different information sources, algorithms or cost regimes. The computed
direct lower endpoints are conservative certificates for the exact
Cartesian projection distance. S03's phase-scaled reference is a different
norm and is not numerically compared with these physical radii.

## Acquisition and complete payments

The producer preserves the original expanded contour integrand and
acquires all 52 midpoint orders 0 through 51 afresh, at both 192 and
256 bits. For j=3, degree 24 in space and 12 in time require order 51
in the polynomial. The time remainder of a retained spatial coefficient
can require 3+24+2(12+1)=53; the positive order-53 moment covers it.
The original infinite tail theorem permits every nonnegative integer
derivative order. Both physical tails are evaluated at j=3, and all
admissibility conditions are checked through order 53. No second-order
tail constant is substituted for h3.

Every complete Vj ball includes outward polynomial evaluation and its
quadrature, Taylor, omitted-mode and retained-source payments. The
explicit residual-error bound B11+B02+abs(beta)(B12+B03) follows by
expanding each quadratic product with its complete component error.
It is diagnostic; the current test already consumes complete Vj balls
and does not subtract it again. No midpoint propagation requiring h4
is used. The new higher moment, tails and extra midpoint coefficient
are charged; callback/timing observations supply no speed comparison.

## Separate execution, exact record checks and controls

The reviewer freshly ran the final producer at 192 and 256 bits.
Every non-timing run field matches the corresponding author execution.
The saved whitespace-compacted records parse to the identical objects;
their stored hashes and canonical hashes are in the [review receipt][receipt].
Duplicate full execution records stay outside the repository.

A separate exact-Fraction validator checks all 64 cells at each precision:
closed-cover identity; all four complete component payments; propagation
of all acquired coefficient radii through order 51; own derivative-order
tails; polynomial-image-plus-error containment; beta and signed-current
interval arithmetic; denominator and Cauchy quotient; direct lower-radius
arithmetic; the explicit quadratic residual-error ledger; and every
reported sign/no-gain/minimum decision. It rejects 22 altered-record
fixtures. These are reviewer record-integrity tests, not claims that the
producer has an external source-cache loader.

The actual producer rejects 17 invalid-input/API fixtures, including
nonfinite or wrong-length jets, reversed/outside domain, incomplete or
negative/nonfinite error ledgers, invalid execution metadata and an
altered same-name contract. Three synthetic exact-event jet fixtures
challenge the actual helper at its declared B geometry and reject.
They are explicitly synthetic, rather than uncomputed control h3 data.

Four fresh own-source event cases, one exact backward-heat polynomial
event and the inherited Euler witness are replayed. At every actual
event h0=h1=0, the exact new
formula gives r=0 for every finite own-source h2,h3. This analytic
substitution needs no new h3 quadrature; no such four-jet control
certificate is claimed. The [control record][control-record] states this
distinction, source receipt identities and the missing theta premise
for each family. No theta error constant is transferred to a control.
Euler's negative-L0 point tests the inherited Laguerre-positivity claim;
it need not invalidate a noncollision certificate at its nonzero first
jet, and no new r-sign claim is made there.

The failed current intervals are enclosure failures. Neither their
negative lower endpoints nor the zero failure marker asserts a negative
physical current or a physical collision. The same four failures remain
at both precisions. The note's scoped stopping decision and task status
therefore match the evidence.

[note]: ../notes/05_BOUNDED_COMPLETED_CURRENT_AND_DIRECT_COMPARISON_20261019.md
[contract]: ../notes/04_S06_T2_BOUNDED_CURRENT_COMPARISON_CONTRACT_20261019.md
[receipt]: ../numerics/S06_T2_INTERNAL_REVIEW_20261019.json
[control-record]: ../numerics/S06_T2_CONTROLS_20261019.json
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[same-model]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
