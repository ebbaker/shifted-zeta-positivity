# E08 additional-agent review of the E07 five-pair proof

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, **gpt-6.1-sol / ultra** by explicit
tool selection. The reviewer is distinct from the pair-comparison and
arithmetic-proof authors, shares their sources and model selection, and
contributed the conditional Green alternative to B04. This is internal
additional-agent assessment. The inherited providers retain their earlier
assessment levels. [Result index][results], [avoid index][avoid].

**Disposition.** Accept the saved [Note18][proof] within [E07 r1][packet]
from the named inputs. No mathematical correction requested. The proof
gives strict width \(567/1000\) at every large real center on its prescribed
heat curve and, separately, for all \(0<t\le t_*\) and
\(|x|\ge4\pi e^{1/t}\) at the same time \(t\). Both sufficient onsets
remain symbolic.

## Exact pair calculation and logarithmic phases

Read [Note14][pairs], [Note17][decision] and the existing primary-source
passage records. Independently replayed the five fixed words acting from
right to left on \(P=(1/6,2/3)\), beginning with \(P=AB(0,1)\).
The outputs agree with all five pairs and all ten tabulated endpoint
values. The consecutive cuts are exactly
\(1/8,4/25,89/500,11/50,9/20,1/2\).
Convexity bounds \(k/v+l-k-1+v/4\) on each piece by the larger endpoint,
at most \(669/20000\). Subtracting this cap from
\((567/1000-1/2)/2\) leaves \(1/20000\), so the primary power
saving at \(c=1\) is at least \(1/160000\). At \(c=tL_x\), the
derivative of the primary exponent at fixed \(v\) is
\(-v(1-v)/4\), while the proof keeps the real complex-log shift
with its favorable sign. Curve drift costs at most \(1/1600000\)
and leaves \(9/1600000>1/200000\). On the common-time range
\(1\le c\le C\), the power only improves. [Exact review record][checks].

The two exact frequencies are
\[
 \tau_D=x/2+\pi t/8-t\arg(z)/4,\qquad
 \tau_R=x/2+\pi t/8+t\arg(z)/4 .
\]
They lie in \([x/2,x]\) once \(x\) is large on both domains.
Montgomery–Vaughan Definitions 16.1–16.2 give the arbitrary-subinterval
bound, with \(\theta=1\), logarithmic phase
\(\tau\log(u)/(2\pi)\), every derivative matching exactly, and conjugation
for the negative sign. It retains \(M/x\). The same source's
Theorems 16.23 and 16.25 justify each A and B operation.
The proof handles any half-open partial interval by its included
integers and bounds a singleton by the primary term. [Montgomery–Vaughan][mv],
[source use03][sources], [E04][e04].

## Complete field and error payments

- The denominator is independently analytic and nonzero. At the worst
  permitted \(c=1-10^{-5}\) and \(y=567/1000\), the real part of
  \(s_t\) is at least \(413399/400000>33/32\). The ordinary Euler
  product gives \(|1/\zeta(s_t)|\le33\), and the elementary carrier
  is already nonzero in the right half-plane.
- The weighted head exponent is at least
  \(3207193/3200000>513/512\). With the exact
  \(K_x=\lfloor e^{L_x/8}\rfloor\), the finite head therefore
  costs \(At\) to remove its heat weight, with the requested summable
  constant \(A\). The ordinary series alone supplies the
  infinite tail, paid by \(32K_x^{-1/32}\ll x^{-1/256}\).
- The dominant tails use the declared real cuts with left-open,
  right-closed clipped dyads through \(N_x=\lfloor e^{L_x/2}\rfloor\).
  Modulus and variation on a clipped dyad are controlled by the
  starting weight times \(2^J(1+J\log 2)\), where direct
  log differentiation gives a fixed \(J\) on each domain. This
  pays Abel summation and shows that the retained block-count
  loss is \(O(1+L_x)\). The inverse term is
  \(O(x^{-1/2})\) per block as the dominant weight is at most one.
- The reflected sum includes \(n=1\) and every other integer
  through the exact cutoff. The primary exponent after the
  carrier has worst endpoints \(-701/6000\) and
  \(-180397/4800000\), strictly below \(-1/32\). Convexity
  pays the intervals between them. For the inverse term pay
  \(O(x^{-y/2}M^{17/16}/x)=O(x^{-1/2})\) per block with
  \(M\le e^{L_x/2}\).
- The correction uses the bounded removable quotient and its
  separate carrier payment, uniformly at fractional cutoffs.
  It costs \(O(x^{-(1+y)/4})\).
  The two-carrier remainder after division is
  \(O_D(x^{-3/4})(1+O(x^{-y/2}))\); the cited provider has
  already paid the true and artificial Gaussian exteriors,
  underlying source, and chart/cutoff joins. The curve uses the
  fixed-buffer CS6 provider within \(c\le8\). The finite
  common-time window uses [Note12's separately proved extension][e05],
  whose review retains the original zero-time input and internal
  assessment status. [E06][e06].

## Uniform onsets and the two time quantifiers

The curve has one \(X\)-dependent heat time fixed on its entire
closed rectangle. The clock drift bound follows from
\(|L_x-L_X|\le1/(X-1)\). Both finite arm cutoffs can be
recentered pointwise without changing the exact field, and the
two clock gates ensure one finite onset for every real center.
The curve factor \((1+L_X)(X-1)^{-\kappa}\) decreases when
\(L_X\ge1/\kappa\), since its logarithmic derivative is
\(1/(X(1+L_X))-\kappa/(X-1)\). The two gates with 4224 pay
\(33\) times the full comparison by \(1/64\).
The independent carrier, known initial strip and conjugation pay
strict width at each center. This checks the full rectangular
comparison in the frozen request.

The common-time order is \(C_P\), then \(C\ge\max(8,C_P)+1\)
and \(D=C+1\), base growth constants, Gaussian window,
enlarged fixed charts and local constants, provider onset,
comparison prefactors, then \(L_*\). For the resulting
\(t_*=1/L_*\), \(0<t\le t_*\) and \(x\ge4\pi e^{1/t}\)
imply \(L_x\ge1/t\ge L_*\). The head term satisfies
\(At\le A/L_*\); the other half of the allowed error follows from
decrease of \((1+L)(4\pi e^L)^{-\kappa}\) for \(L\ge1/\kappa\).
This yields the same normalized threshold across
\(1\le tL_x\le C\). At \(tL_x=C\) the finite-window proof
and the published all-real tail overlap, since
\(x\ge4\pi e^{C/t}>e^{C_P/t}\). Initial strip contraction,
conjugation and evenness supply the remaining transverse
coordinates and negative heights at the common fixed time.
[Polymath Theorem 1.5(i)][outer], [Polymath §3][poly].

The gain from the previous common-time width \(4/7\) is
\(31/7000\). The new width is below E03's A-chain allowance
threshold by \(727/644000\). This comparison crosses the
specific A-chain allowance using five fixed A/B words.
The exact replay verifies the declared arithmetic and byte
provenance, with all 17 E01 inputs matching.
The control screen uses the unchanged canonical coefficients,
reflection, source/profile identification and actual heat and
logarithmic phases named in Note18. These premises fail for
the respective controls. The new width preserves the separate
compact-height, time-zero and intermediate-barrier obligations.
The conditional local Poisson moment in [Note15][green] remains
unpaid. [Collision controls12][controls], [scope07][scope].

[proof]: ../notes/18_GNP_BB_E07_FIVE_PAIR_WIDTH_20261113.md
[packet]: ../research-progress/handoffs/GNP-BB-E07-r1.md
[pairs]: ../notes/14_GNP_BB_B04_BROADER_PAIR_COMPARISON_20261113.md
[decision]: ../notes/17_GNP_BB_B04_DECISION_AND_EXECUTION_CONTRACT_20261113.md
[checks]: ../numerics/14_GNP_BB_E07_REVIEW_CHECKS_20261113.json
[sources]: ../references/03_GNP_BB_B04_SOURCE_USE_20261113.md
[e04]: 03_GNP_BB_E01_E03_ADDITIONAL_AGENT_REVIEW_20261113.md
[e05]: ../notes/12_GNP_BB_E05_COMMON_TIME_TAIL_20261113.md
[e06]: 05_GNP_BB_E05_COMMON_TIME_REVIEW_20261113.md
[green]: ../notes/15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[outer]: https://arxiv.org/html/1904.12438v2#S1.Thmtheorem5
[poly]: https://arxiv.org/html/1904.12438v2#S3
