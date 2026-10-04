# Selective loss program

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Separate agents using the same model
configuration checked the algebra, source domains, head selection, and
residual estimates. These are internal checks, not independent specialist
refereeing.

## 1. Aim and present status

The program follows the proposal to modify the positive Sonin source form
by incorporating favorable boundary contributions, leaving an adverse
remainder that can be controlled as the support grows. The practical
target is a polynomial loss on the existing translated probe. More
generally, any subexponential loss, or a suitable weighted integral bound,
would suffice for the established one-sided growth theorem.

The starting identity is Q=B-K, with B independently nonnegative. Simply
requiring K to be nonnegative does not prove Q nonnegative; the size of K
relative to B still matters. We seek an independently positive revised
main form P and an explicit nonnegative allowance E such that

\[
Q[F]\ge P[F]-E[F],\qquad P[F]\ge0.
\]

An exact identity Q=P-E is also possible in the constructions below. The
allowance need not tend to zero. A polynomial bound on the target sources
already reaches the arithmetic goal. An asymptotic identification with
the Weil form must therefore be understood in the required growth sense,
unless a stronger convergence statement is separately proved.

**Present result:** the finite-head algebra and full-residual certificate
are established, and reflection removes the mixed sum and difference
channel exactly. The next audit identified a substantive obstruction:
nonnegative endpoint-profile complements on unbounded windows already
imply RH. The active replacement uses a known positive archimedean metric
and an explicit adverse response. Its complete weighted prime response
now has an exact causal-energy and signed prime-pair reduction. The
diagonal energy now has explicit unconditional quadratic bounds. A new
outward certificate proves the entire signed off-diagonal sum is less
than -5 for every real Y from 100 through 225. The remaining global target
is a quadratic upper bound on its aggregate positive part, or on the
local smoothed prime energy. The smooth density costs fixed endpoint
caps, and higher powers give a bounded correction. No global bound or
RH proof is established.

The [manuscript](../../manuscript.tex) now summarizes this program in
“Selective source loss and complete prime-response energy,” retaining
short proof summaries and references for the detailed derivations.
See the [integration review](../../reviews/SELECTIVE_LOSS_MANUSCRIPT_INTEGRATION_20261003.md)
and [next-session handoff](../NEXT_SESSION_SELECTIVE_LOSS_20261003.md)
for the compiled source record and precise continuation target.

## 2. The common target

Keep the existing real odd prepared probe

\[
h(x)=(1-16x^2)^8\mathbf1_{|x|<1/4},\qquad
g=\frac{(-\partial_x^2+1/4)\partial_xh}
        {\|(-\partial_x^2+1/4)\partial_xh\|_2}.
\]

Its support diameter is ell=1/2 and its three prepared moments vanish.
Write tau_r g(x)=g(x-r), and use

\[
F_r=(g+\tau_rg)/\sqrt2,\qquad r>\ell.
\]

The source norm is one. The established arithmetic identity is

\[
Q[F_r]=q-M_g(r)+\epsilon_g(r),\qquad
q=Q[g],\qquad |\epsilon_g(r)|\le
b(r)=\frac{\ell e^{-5(r-\ell)/2}}{1-e^{-2(r-\ell)}}.
\]

Thus Q[F_r]>=-E(r) gives M_g(r)<=q+b(r)+E(r). The
[one-sided theorem](../GLOBAL_GROWTH_ONE_SIDED_20261003.md) and
[single-probe theorem](../SINGLE_PROBE_GROWTH_THEOREM_20261003.md) supply
the implication to RH and all-window Weil positivity. They use the
special probe's noncancellation property; this implication is not claimed
for an arbitrary replacement probe.

There are two sufficient global targets:

1. Pointwise: E(r)<=C(1+r)^m for every sufficiently large real r. Even
   E(r)=O_epsilon(exp(epsilon r)) for every epsilon>0 is sufficient.
2. Averaged: for every epsilon>0, the integral of exp(-epsilon r)E(r)
   over large r is finite. In particular polynomial cumulative loss, or
   polynomial unit-shell loss totals, is sufficient. This alternative
   permits occasional large pointwise losses.

The support-adapted prime set must capture all active primes. For r in
[j,j+1], one common source interval of diameter j+1+ell and one common
set S_j={p:p<=exp(j+1+ell)} suffice. Every prime power attached to those
primes is retained in the finite-product definition. Extra primes can
change B and K separately even when Q[F_r] is unchanged, so they cannot
be ignored when estimating a particular allowance.

## 3. The three approaches

| Approach | Quantity to control | Why it is promising | Main unresolved input |
| --- | --- | --- | --- |
| 1. Signed Schur completion | A finite adverse allowance after the full complement and mixed response are retained | Harmless directions remain in the positive main; source overlaps are explicit and parity removes their mixed entry | An unconditional enlarged-head tail certificate and the loss of all added modes; endpoint-only tail safety is RH-equivalent |
| 2. Controlled source and dual lifting | Centered residual energy, or a local smoothed prime energy | The reference gap is at least one, the source energy is bounded, and the prime diagonal already has polynomial cost | An upper polynomial bound on the aggregate signed off-diagonal pair energy, including complete boundary caps; the sharper dual target remains available |
| 3. Prime-place normalization | Signed old/new response when one whole prime is inserted | Same-prime power packets are disjoint, so the exact self energy is at most (log p)^2/(p-1), with polynomial cumulative cost | An aggregate cancellation law for the first-order cross term with earlier primes |

Approach 1 remains the starting construction. Its complement audit made
the bridge to Approach 2 the active route. The complete-response analysis
now gives Approach 3 an exact insertion identity: the self term is
controlled, while the signed first-order cross term remains open. This
is not yet a normalization or cancellation theorem for the Sonin operator.
The diagonal cost must not be mistaken for a bound on a coherent sum
of all prime channels.

## 4. First approach and its first results

At a fixed window let H=B^(-1/2)KB^(-1/2) and v=B^(1/2)F. Choose a finite
orthogonal head E and retain its full coupling to P=I-E. If the tail
D=P(I-H)P is at least delta times the tail identity, the exact Schur
matrix is

\[
S=I-H_{00}-G^*D^{-1}G,\qquad G=PH|_{E\mathcal H}.
\]

The full form is the sum of a nonnegative completed tail square and
the finite form of S. This produces an independently positive main and
a finite loss without dropping mixed columns. Approximate tail solves
give a certified matrix lower bound when their full residual energy is
enclosed.

A concrete head can be built from physical prepared templates W:

\[
G_0=W^*B^{-1}W,\qquad U=B^{-1/2}W G_0^{-1/2}.
\]

U is an isometry and the head coordinates are exactly
U*B^(1/2)F=G_0^(-1/2)W*F. Thus known source correlations replace unknown
overlaps with relative eigenvectors. Keep the Gram normalization and
mixed response as joint matrices; replacing them by unrelated worst
scalar bounds can lose the cancellation being sought.

For W=[g,tau_r g], the target overlap vector is (1,1)/sqrt(2). A positive
matrix allowance can charge the sum and difference directions separately.
Its charge on F_r is exactly the sum-direction allowance; the difference
allowance may be much larger. This is a precise selective target, provided
the full complement is certified safe. The two-template head alone has
not been shown to have a safe complement on growing windows.

For a common unit-shell head built from g and three translates at j,
j+1/2,j+1, the integrated physical overlap matrix is explicit and
independent of j. This gives a continuous-separation quantity to pair
with a common certified allowance matrix.

The complete derivations, limitations, and next tasks are in
[First Schur completion results](01_schur_completion_20261003.md).

The exact shell calculation also identifies a limitation: for the fixed
four-template family, the covariance satisfies I/32<Xi<=I/2. Its average
loss therefore controls the total positive allowance and the pointwise
loss, up to fixed constants. It cannot hide a large charge in a direction
that remains uncharged across the entire shell. This favors investigating
the adaptive two-template construction before relying on averaging alone.

The two-template construction now has an important qualification. Its
physical complement is precisely the source constraint W*F=0, and every
source in the growing gap between the profiles satisfies it. Nonnegative
tail safety on unbounded windows is therefore already equivalent to RH.
Odd parity simplifies the matrix but still leaves smaller odd translated
probes in that gap. See
[Complement obstruction and parity](02_complement_obstruction_and_parity_20261003.md).

The exact physical Schur coefficient is the infimum of Q subject to
W*F=d. It is consequently independent of the positive reference B for a
fixed physical W, whenever the safe-tail hypotheses hold. Changing B can
improve conditioning or enclosure errors, but cannot change that exact
constrained infimum. Inactive-prime changes cancel there exactly.

The [centered dual energy note](03_centered_dual_energy_20261003.md) supplies
a replacement certificate. With A=Gamma+cI>=I and f=QF_r, its target is
X(r)=<f,A^(-1)f>. The reference energy A[F_r] is uniformly bounded,
and an exact positive-square split gives Q[F_r]>=-sqrt(A[F_r]X(r)).
A polynomial bound on X therefore suffices. No nonnegative arithmetic
complement is assumed.

A directly calculable sufficient target is the squared norm R_ar of
the complete prime-power response after the three-moment source projection.
The smooth density part cancels to fixed endpoint caps of squared norm
917180/580421327. The remaining response is a complete weighted prime
discrepancy. Cutting its density window at e^r instead of e^(r+ell)
creates an exponential edge even after moment projection. Keep that
boundary cancellation intact.

The [small response pilot](../../numerics/selective_loss_dual_response_20261003/README.md)
checks only r=2,3,4,5,6. It evaluates the actual finite arithmetic response,
with floating quadrature comparisons, and establishes no asymptotic rate.

The [complete response and signed-pair note](04_complete_response_and_signed_pairs_20261003.md)
sharpens the target. For p(y)=sum Lambda(n)/sqrt(n) g(y-log n), set
J(Y)=int_0^Y p(y)^2dy. The actual response has unprojected energy
N(r)=J(r+1/4)-(p*p)(r), and R_ar<=N<=2J. The complete finite pair
expansion is J=D+Theta, where D(Y)=Y^2/2+o(Y^2) unconditionally.
Thus only the upper side of the signed aggregate Theta is unbounded:
Theta>=-D is automatic. A polynomial bound on Theta_+ after summing
all signed pairs would give a polynomial loss; a quadratic bound would
give a linear allowance in r. Termwise positive pair mass is exponential.

The [dyadic shifted-correlation continuation](08_dyadic_shifted_correlations_20261003.md)
now supplies the exact pair weight with both cap blocks and isolates the
usual prime-pair singular-series main. An unconditional mean theorem for
that explicit series gives a negative leading term
\(-\tfrac32X^2\log X\), canceling the dyadic diagonal's leading term in
the model. The actual prime-pair error remains uncontrolled. Its signed
aggregate positive part on the \(X^2\log X\) scale is the next precise
arithmetic obligation; even individual square-root correlation errors
would be too costly if summed absolutely. See the
[small real-shell diagnostic](../../numerics/selective_loss_dyadic_pairs_20261003/README.md)
and [internal audit](../../reviews/SELECTIVE_LOSS_DYADIC_CORRELATION_REVIEW_20261003.md).

The [actual-error continuation](09_actual_error_projection_and_frequency_20261003.md)
now proves a quadratic bound for the remainder's negative part and an
unconditional bound at the target scale for its outer additive-frequency
contribution. The remaining signed central projection is supported inside
\(|\alpha|\le X^{-10/11}\), with smoothing concentrated at scale \(1/X\).
An alternative exact comparison removes the four trends
\(1,t,\sqrt t,\log t\) from \(\psi(t)-t\) before taking its local
mean-square norm. The needed fitted-error bound remains unproved and
RH-equivalent. The [actual remainder and fitted-error diagnostics](../../numerics/selective_loss_arithmetic_remainder_20261003/README.md)
give only small floating checks; see the
[internal review](../../reviews/SELECTIVE_LOSS_ACTUAL_ERROR_REVIEW_20261003.md).

The [subpower continuation](10_subpower_growth_and_investigation_paths_20261003.md) now proves that variance O_delta(X^(2+delta)) for every positive delta, subexponential cumulative J, and physical weighted-energy finiteness for every positive weight are equivalent to RH for this probe. Constants and starting thresholds may depend on delta. The corresponding central projected energy target is O_delta(X^(1+delta)). A bound at one fixed delta between zero and one would exclude zeros strictly right of 1/2+delta/2. These are transfer results and open estimate targets; no actual-prime global bound has been obtained. The manuscript integrates notes 08–10 and provides suggested investigation paths.

Higher prime powers give an o(1), uniformly bounded correction to p,
so the remaining energy target can be reduced to primes alone. Weighted
unprojected response and local energy have an exact coercive integral
identity. That lower bound does not hold geometrically after moment
projection; the actual arithmetic equivalence uses the full transform
and pole-inclusive explicit formula. The fixed-width top Gram block
records all truncation and moment corrections explicitly.

The [signed decomposition pilot](../../numerics/selective_loss_signed_pairs_20261003/README.md)
checks r=2,...,10 and separates D, Theta, the reflected cross term, and
the moment subtraction. The signed off-diagonal sum is negative at
these nine samples, but no continuous or global sign estimate is
inferred. See the [internal audit](../../reviews/SELECTIVE_LOSS_SIGNED_PAIRS_REVIEW_20261003.md).

The [quadratic-target continuation](05_quadratic_target_and_finite_sign_20261003.md)
proves max(0,Y^2/4-48)<=D(Y)<=2 log(2)(Y^2+17/16) for every real Y>=0.
Its [outward certificate](../../numerics/selective_loss_quadratic_target_20261003/README.md)
gives |p(y)|<4.97 for every real 1<=y<=225, which proves Theta(Y)<-5
throughout 100<=Y<=225. This bounded interval gives a corresponding
linear selective allowance; it supplies no global RH input.

The [global mechanism tests](06_global_mechanism_tests_20261003.md)
identify an essential endpoint cancellation and a gap between frame
bounds and a coherent sum. A discrete PNT model with the correct diagonal
can still have exponential loss. They formulate a sufficient actual-prime
variance bound of size X^2 log X for the existing signed kernel. The
[weighted-energy analysis](07_weighted_energy_abscissa_20261003.md)
identifies the exact energy convergence abscissa with the rightmost zero
real part and specifies the analyticity needed for a legitimate Hardy
bound. All these global formulations retain RH strength.

## 5. Guardrails from the completed work

- The [positive-channel analysis](../POSITIVE_CHANNEL_ABSORPTION_20261003.md)
  proves an exponential adverse-loss obstruction for positive ambient
  operator splits. The source-form construction is essential here.
- Fixed-window compactness gives finite heads at each window. It gives
  neither uniform head size nor a global loss bound.
- Every complement and residual estimate must include the full omitted
  space. A compressed numerical solve or small sampled residual is
  insufficient.
- Matrix negative parts are not operator-monotone. A certified lower
  matrix supplies its own valid positive-main construction; it need not
  dominate the exact spectral loss on a chosen source.
- A head chosen to contain only the target energy vector can repackage
  the unknown Weil value. Independent arithmetic, complement, and
  mixed-channel estimates are needed to make it useful.
- Sharp prime cutoffs can create an artificial weighted-energy boundary
  term. Complete smoothing windows and the
  [cutoff analysis](../GLOBAL_GROWTH_WEIGHTED_ENERGY_CUTOFF_20261003.md)
  must be respected.

## 6. Work sequence and records

| Stage | Required result | Status on 3 October 2026 |
| --- | --- | --- |
| Fixed-window algebra | Positive main, finite loss, exact source coordinates, full-residual enclosure | Established in the first approach note |
| Continuous-shell geometry | Exact integrated overlap matrix for the existing probe | Small exact calculation recorded with the first approach |
| Endpoint complement audit | Identify the strength of the prescribed physical tail | Nonnegative endpoint tails on an unbounded family are RH-equivalent; parity does not remove this obstruction |
| Safe enlarged-head construction | An unconditional full tail bound and accounting for every added mode | Open; existing worst-scalar bounds are too costly |
| Known positive dual reference | Gap-one reference, positive-square split, full residual enclosure, complete density cancellation | Established in the centered dual energy note |
| Complete response reduction | Causal energy, controlled diagonal, full boundary Gram, prime-only reduction, and exact insertion identity | Established in the signed-pair note; nine floating samples remain diagnostic |
| Explicit quadratic diagonal | Global upper and lower polynomials without a PNT rate | Established: max(0,Y^2/4-48)<=D(Y)<=2 log(2)(Y^2+17/16) |
| Continuous signed-pair theorem | Sign of the complete aggregate pair sum on a bounded interval | Certified: Theta(Y)<-5 for every real 100<=Y<=225 |
| Global mechanism audit | Test factorization, frames, ordinary PNT, and variance/Hardy inputs | Endpoint and coherent-vector gaps identified; structural countermodel established; actual-prime variance target specified |
| Dyadic shifted correlations | Exact cap weights, diagonal and continuum normalization, singular-series main, and arithmetic input audit | Established in note 08; the singular-series leading main cancels the diagonal in the model; actual signed correlation errors remain open |
| Actual error localization | Constant-order model main, negative-part bound, removable Chebyshev trends, and additive outer frequencies | Established in note 09; the positive remainder and signed central projection remain open |
| Subpower quantitative relaxation | Exact dyadic and weighted transfers, all-exponent central target, and fixed-exponent zero-free implication | Established in note 10; the actual-prime estimates remain open and RH-equivalent when all positive exponents are required |
| Weighted response estimate | A polynomial or subexponential bound on X, local prime energy, or the aggregate signed off-diagonal loss | Open; the finite theorem does not imply a global estimate |
| Arithmetic conclusion | Apply the established one-sided theorem after the global bound is proved | Conditional on the preceding estimate |

The quadratic quantitative target remains Theta_+(Y)<=C(1+Y)^2,
with all signs summed before taking the positive part and with the complete
top-top cap block. The explicit quadratic diagonal makes this equivalent
to J(Y)=O((1+Y)^2). A concrete sufficient next target is the fixed-kernel
actual-prime variance estimate integral_X^(2X)|V(x)|^2dx<=C_g X^2 log X,
with V and its precise centering defined in note06. This must use arithmetic
information beyond positive weights, ordinary PNT, and frame/trace bounds. An alternative is a polynomial unit-shell bound for the local
smoothed prime signal p_P, keeping the signed g before squaring. The
positive-A dual energy remains a sharper target when the L2 response
bound is too expensive. Absolute pair clipping and separate insertion
Cauchy estimates have exponential cost and do not close this obligation.
Note 08 now isolates the complete singular-series model main and gives the
equivalent target \(\mathcal R(X)_+=O_g(X^2\log(2X))\) for the combined
signed actual-prime error. Its equation (19) specifies the exact partial
sums and signed derivatives a proposed arithmetic theorem must control.
Note 09 supplies a sharper equivalent central-frequency target in its
equation (19), after controlling the outer piece unconditionally. Its
equation (12) gives an alternative fitted Chebyshev-error norm target,
retaining four exactly harmless trends rather than charging their size.
For the ultimate implication, the less restrictive all-delta subpower target in note 10 permits logarithmic or subpower losses without a uniform small-weight polynomial rate. Prioritize the exact central projection and calculate the exponent delivered by a proposed unconditional arithmetic input, retaining both caps, real endpoints, and exceptional-shift costs. A single fixed exponent below three in physical variance would already give a substantial zero-free half-plane milestone.
For a continued Schur route, use an unconditional enlarged-head certificate
and retain every added source loss. Endpoint-only nonnegative tails cannot
be assumed as a preliminary.

Keep each approach's research notes in this folder and link them here.
Put numerical sources and small records in the investigation's numerics
folder, and reviews in its reviews folder. Update this overview when an
obligation is proved, refuted, or replaced. Detailed history belongs in
the linked notes; manuscript milestones belong in the existing concise
draft history when a manuscript milestone actually occurs.

The [dedicated subpower milestones program](../subpower-milestones/README.md) now organizes the author's preferred quantitative investigation around global delta bounds. Its [baseline note](../subpower-milestones/01_baseline_and_exponent_budget_20261003.md) establishes the fixed-exponent zero-strip equivalence and transfers a stronger known PNT envelope while retaining delta=1. The first genuine power saving and any exponent-descent rule remain open. The central signed projection is one possible method within that program.

The first continuation proves a [short-interval mean-square transfer](../subpower-milestones/02_short_interval_transfer_and_gate_20261003.md), obtains [finite quadratic variance bounds](../subpower-milestones/03_finite_range_variance_20261003.md) through explicitly stated continuous ranges, and establishes a [finite-prefix structural obstruction](../subpower-milestones/04_structural_nonbootstrap_20261003.md) to exponent bootstrap. The tested short-interval input supplies no fixed power saving. The next global obligation is an actual-prime input supplying positive kappa in the gate, or an improvement retaining the signed covariance. The [internal review](../../reviews/SUBPOWER_FIRST_INVESTIGATION_REVIEW_20261003.md) records the proof and rational-certificate checks.

## 7. Starting references

- [Global growth handoff](../NEXT_SESSION_GLOBAL_GROWTH_HANDOFF_20261003.md).
- [Positive channel absorption](../POSITIVE_CHANNEL_ABSORPTION_20261003.md)
  and its [internal review](../../reviews/POSITIVE_CHANNEL_ABSORPTION_REVIEW_20261003.md).
- [Closed source comparison](../CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md).
- [Full mixed relative tails](../ALL_WINDOW_EFFECTIVE_RELATIVE_TAILS_20261003.md).
- [Spatial prime reduction](../ALL_WINDOW_SPATIAL_PRIME_REDUCTION_20261003.md).

This program extends the existing source-relative comparison by making
the tolerated loss selective. Its algebra uses the existing B and K;
it is not a separate unconditional solution of the global comparison.
