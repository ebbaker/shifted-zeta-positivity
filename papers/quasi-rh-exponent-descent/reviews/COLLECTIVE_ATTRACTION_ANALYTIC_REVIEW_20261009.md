# Review of analytic collective attraction and landing times

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Three parallel same-model analyses supplied the kernel, counting, and
landing audits. These are internal checks, not independent mathematical
validation or external refereeing.

The [new heat note](../newman_collisions/notes/6_ANALYTIC_COLLECTIVE_ATTRACTION_AND_LANDING_20261009.md)
passes the scoped checks below. It advances the selected collective-attraction
route at positive time and defers expansion of the compact numerical cover.
There is no new numerical bound for the Newman constant.

## Exact field and logarithmic derivative

The exact field \(E\) and projected field \(G\) are distinguished throughout.
At a simple maximal nonreal zero, the own conjugate gives exactly minus two
in \((y^2)'=-2-4y^2E\). External real roots and conjugate pairs have positive
contributions, and \(E\ge G\).

The independently derived comparison factor

\[
 K(\eta/y)=\min\{1,(\eta^2-y^2)/(4y^2)\},\qquad\eta>y,
\]

is verified by two universal polynomial identities with nonnegative factor
certificates on the whole permitted parameter domains. A real external root
has ratio at least one. The excluded zero-denominator configuration would
coincide with the target root; limiting distinct configurations prove sharpness.
The near-probe result concerns \(E\), not \(G\).

The own-pair subtraction in the probe cancels the baseline term exactly
when \(y<\eta\le\sqrt5\,y\). This yields
\((y^2)'\le-(\eta^2-y^2)L_\eta/\eta\), while the classical speed bound
remains available. Probe floors must be established for the true function
with paid approximation and derivative errors.

## Uniform all-zero counting and globality

[Polymath, Theorem 1.5(iv)](https://arxiv.org/html/1904.12438#S1.Thmtheorem5)
counts all zeros with multiplicity and explicitly has error constants
independent of \(0<t\le1/2\). The time-dependent main term is retained.
The moving count block is strictly to the right of the own pair. A fixed
count block supplies the compact spatial sector. Negative abscissae follow
by evenness.

The choices \(D=8\pi(4A+1)\),
\(X_* =\max\{(4\pi)^2,2D,3\}\), \(n=\log X_*\), and
\(B=X_*+2D\) have sufficient endpoint-error reserve. They prove the global
floor \(G\ge n/(B^2+4w)\). No root is assumed real, no neighbor is located,
and no horizontal sector-transport premise is needed for this floor.

The weaker global floor and a stronger sector probe bound must be assembled
using the minimum across all allowed sectors. Overlapping count and probe
contributions cannot be added without another argument.

## Landing comparison and exceptional times

Differentiation of the displayed landing function gives exactly the inverse
speed for the count floor. The strict gain and its rational lower bound are
correct. Compact positive-time confinement and the published local Hermite
splitting justify continuation across maximum switches and isolated multiple
roots. A field value at a multiple root is not inserted into the simple-zero
identity.

The epsilon-start argument handles an initial estimate at time zero without
assuming a maximal nonreal root is attained there. Its landing stays inside
the time range of the count theorem. An improved endpoint cannot be iterated
by treating it as a backward strip estimate.

## Effective constants and imported scope

The count constant \(A\) is unprinted. Extracting a useful value requires
quantifying the source's extended imaginary-range approximation, Jensen
growth estimates, sufficient cutoff, and finite initial segment. The global
floor is explicit in \(A\); it is not presently a certified decimal bound.

A quantitative extraction should rederive the heat-weight exponents from
the definitions. In particular, \(s_*=s+(t/2)\alpha(s)\) and
\(\alpha(s)\sim\tfrac12\log(x/(4\pi))\) give a \(t/4\) logarithmic
coefficient. The displayed \(t/2\) coefficient in the asymptotic proof of
Proposition 9.1 should not be copied into a numerical constant ledger.
The note imports the published qualitative counting theorem rather than
claiming to have reconstructed its proof with effective constants.

Starting from the original unit strip only recovers the known
\(\Lambda<1/2\). Literature novelty and a competitive numerical endpoint
remain unclaimed. The new useful interfaces are the sharp exact-field probe
factor and the explicit state-dependent global landing comparison.

## Finite verification

[The standard-library checker](../numerics/check_collective_attraction_algebra.py)
checks nine universal polynomial identities by coefficient equality and
supplementary rational substitutions. The
[record](../numerics/collective_attraction_algebra_record_20261009.json)
binds its source hash. It performs no heat-function evaluation or zero-location
search. These finite checks do not establish the imported analytic theorems,
an effective value of \(A\), or a new numerical Newman bound.

The next bounded analytic checkpoint is an effective off-zero
logarithmic-derivative floor for a chosen positive-time range, with complete
spatial coverage requirements and an explicit landing gain.
