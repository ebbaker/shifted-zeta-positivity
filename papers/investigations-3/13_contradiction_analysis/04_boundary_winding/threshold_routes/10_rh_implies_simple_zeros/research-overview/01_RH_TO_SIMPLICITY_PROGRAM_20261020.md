# Parallel program: RH implies simplicity

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**,
verified from session metadata. Same-model internal analysis and review;
no specialist review.

**Chosen goal:** prove that RH implies that every nontrivial zero of
\(\zeta\) is simple. The [opening analysis][note] checks the literature,
transfers the local machinery, and screens the generic arguments.
**No such implication or new theta exclusion has been proved here.**

**Read first for the current discussion:** the six-page [analytic manuscript](../manuscript/main.tex)
([PDF](../manuscript/main.pdf)) consolidates the complete-tail, infimum,
finite-filter and heat-energy estimates. It states the missing opposing
arithmetic estimate and compares the reusable machinery with BW09 in
Section 5. RH simplifies the conditional problem's event setup; it does
not establish a relative-difficulty theorem or supply the missing
multiple-zero exclusion. Numerical and bounded formal checks are cited
as support only. External review of the scaled-tail theorem is a priority.

**Current quantitative advance:** [Note 16 §13](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md) proves under RH alone
(log N)d_N²→K=Σ m_rho²/|rho|² for the complete length-N
Dirichlet-polynomial infimum. Bounded finite two-prime multipliers and
the fixed-taper scaled-tail theorem pay the mixed local profiles and
all exterior zeros, without an inverse-derivative moment. The previous
RH-plus-simplicity value Z is a special case. The true squared
multiplicities remain in K; no exclusion or RH-only upper Z follows.
Section 26 records the ordered choices and scope. The fixed-taper
asymptotic in §24 and separately uniform moving-family upper in §25
retain their stated classes and constants.

This is a separate conditional simplicity program. [Program 03][psc]
continues to govern the original hypothetical positive-threshold surplus;
its unexecuted tasks are not completed or restarted by this document.
The [matching register][progress] governs RHS-00–05. Discussion belongs
in `brainstorm/`; computations, if analytically justified, belong in
`numerics/`; assessments belong in `reviews/`. Preserve [chat 0003][history].

The [result index][results], [local geometry][geometry],
[collision controls][controls] and [avoid index][avoid] apply,
especially [equivalent targets][a01], [control premises][a02],
[scoped exclusions][a07] and [gain before expansion][a20].

## 1. Assumption and conclusion contract

Assume RH and a real zero of exact finite order \(m\ge2\) at \((0,a)\)
for the unchanged theta family, with \(a>0\). Do not assume \(m=2\),
a bounded height, a lower bound for the first nonzero derivative, or
a positive-height asymptotic uniform down to heat time zero.

RH supplies all-realness for every \(t\ge0\), hence simplicity for
every \(t>0\) by local backward splitting. Therefore an independently
forced positive-time multiple zero is a contradiction. The event at
zero is supplied by the negation of the target; no threshold-attainment
theorem is needed.

Primary consumer: for the two outer roots emerging from an \(m\)-fold
event, prove a fully paid finite cap decrease
\[
                     M_{\rm cap}>(m-1)\pi.
\]
The ordinary double-zero version is \(M_{\rm cap}>\pi\). Finite simple
wall continuation, cap regularity, complete source errors and the initial
event charge must all be included. The fixed-index large-time cosine
profile gives precisely the ordinary baseline and is not a surplus.

Comparison consumer: an independently proved Gaussian deficit
\(D_s\le-\delta<0\) excludes the initial event directly, including all
multiplicities. Its proof may use RH in this program. The unquantified
existence of a sufficiently small successful \(s\) is only an equivalent
formulation of simplicity.

## 2. Bounded analytical tasks

The initial table below preserves the opening gates. The current state is
in the [progress register][progress]; the first analytical round is
summarized in §4. “Unexecuted” below describes the opening state only.

| ID | Deliverable and completion gate | Initial status |
| --- | --- | --- |
| RHS-00 | Fix the conditional target, primary literature, normalization and relation to the original programs. | Completed by the opening note and this program. |
| RHS-01 | Transfer local indices, the ordinary and all-multiplicity cap baselines, and screen the exact zero-time Euler-factor control. | Completed analytically in the opening note; no theta inequality. |
| RHS-02 | Derive one quantitative consequence of RH plus the exact \(t=0\) theta/zeta arithmetic, with a named signed term and a bound that distinguishes the \(c=1\) control on its own data. | Next task; unexecuted. |
| RHS-03 | Connect that bound to one finite-contour surplus budget, or justify switching to the matched direct Gaussian consumer. Pay walls, cuts, multiplicities, normalization and all errors. | Gated on RHS-02. |
| RHS-04 | Establish actual coverage: arbitrary event height and multiplicity, or state exactly the excluded class and the unresolved complement. Verify the derived bound analytically; permit a bounded numerical check only with a frozen contract. | Gated on RHS-03. |
| RHS-05 | Review the complete argument and decide whether the claimed result is a theorem, a quantitative partial exclusion, or a scoped failure. | Gated on actual estimates; opening review is not completion. |

### RHS-02: the first research question

At zero the exact identity \(8H(0,z)=\xi(1/2+iz/2)\) gives the genuine,
untilted arithmetic object. RH gives the complete real-zero product.
Use their combination to seek a sign or quantitative gap not shared by
\[
 H^{1,p}(0,x)=H(0,x)(1+\cos(\tfrac12x\log p)).
\]
Under RH this control is all-real at zero, has repeated real zeros
there, and has simple all-real positive-time slices. It preserves broad
Euler-product and functional-equation structure. Its actual failures
are the unchanged coefficients and conductor-one completion.

Begin with one written source/product identity and retain the exact
event cancellations. State which passage uses RH, which uses the
unchanged zeta arithmetic, and how that passage changes for the control.
A generic nonnegative Laguerre expression, a positive Gram norm,
or a restatement of \(H(0,a)^2+H_x(0,a)^2>0\) does not pass this gate.
Nor does naming the control's different conductor without a derived
inequality that uses it.

The task may end in a scoped obstruction for its declared estimating
class. That is preferable to expanding a sequence of equivalent targets.
Do not launch a numerical scan to select an apparent sign.

### RHS-03–04: signs and coverage

For a cap split, compare the signed middle phase to the **actual**
endpoint deficit at the same scale. A positive middle contribution
alone is insufficient. An approximation homotopic to an ordinary lobe
establishes that lobe's degree and cannot also supply excess winding.

All-realness makes later collisions impossible; it does not by itself
prove a separately chosen wall chart valid. Establish finite root
continuation and the selected cap/cut positions. An \(m=2\) argument
must explicitly leave \(m\ge3\) unresolved until covered. Differentiating
to reduce multiplicity changes the field and its source, so a theorem
for the original field is not automatically inherited.

No existing finite positive-time box or proportion-of-simple-zeros
theorem proves all-height, all-zero coverage at \(t=0\). Any finite
verification is an explicitly bounded partial result. Estimates using
a curvature floor, a maximum height, or a derivative-ratio bound must
record the remaining class.

## 3. Controls and stop rules

Replay the quadratic, positive atomic family, all-multiplicity heat
polynomials and the \(c=1\) Euler-factor family with their own data.
Use the two-event quartic to check detection, while retaining its
failure of the initial-threshold premise. For the other source controls,
preserve the catalogue's exact reflection, arithmetic and threshold
distinctions; do not manufacture a zero-time all-real slice.

Stop or narrow a proposed estimate if the same premises prove a false
statement for a control, if a gain is only the desired conclusion in
new notation, if wall placement assumes the required sign, or if the
proof only recovers the ordinary cap baseline. These are stopping rules
for the selected argument, not a theorem against the wider program.

The unconditional alternatives in the opening note remain separate.
A single positive-time collision is contradictory **here because RH is
assumed**. Any later claim of an unconditional theorem must remove that
use and supply a direct exclusion or a stronger propagation argument.

## 4. First analytical round, 20 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
effort ultra**, verified from the continuation session. The [first
notes](../notes/README.md) and [round review](../reviews/02_FIRST_ANALYTICAL_ROUND_REVIEW_20261020.md)
record two bounded analytical attempts. Finite root-wall continuation now
follows under RH for every fixed root label and finite positive cap.
The product phase remains exactly the baseline. Exact Poisson and
finite-prime formulas quantify the endpoint Euler control's added double
mass, including its changed coefficient and conductor terms.

The absolute-prime Poisson envelope and optimized squared-sinc
absolute-payment envelope fail at high height; the latter has infimum
`(1/2+o(1)) log(gamma)/log log(gamma)`. The Gaussian product estimate
strengthens the event-compatible positive sign. These are scoped
estimating results. They do not meet RHS-02's opposing-estimate gate,
produce a cap surplus, or exclude any new theta multiple-zero class.

A next attempt must retain signed arithmetic or supply another justified
source of information beyond those declared envelopes. The precise
finite-prime target is in Note 02; its unquantified successful-scale
existence is a simplicity reformulation. These outcomes do not justify repeating the failed envelope
optimizations or starting a numerical sign scan.
The finite-wall subtask is complete; the overall target remains open.

[note]: ../brainstorm/01_RH_IMPLIES_SIMPLICITY_20261020.md
[psc]: ../../09_expanding_contour_later_collision/research-overview/03_ANALYTICAL_PHASE_SURPLUS_PROGRAM_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[history]: ../chat-histories/0003_2026-10-20T18-25-04Z_analyze-simple-zero-contradiction.json
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md


## 5. Signed-prime and coefficient continuation, 20 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
effort ultra**. [Note 03](../notes/03_SIGNED_PRIME_TRANSPORT_AND_EULER_RIGIDITY_20261020.md)
retains the signed Chebyshev error, cancels its exponential main term
against the explicit-formula poles exactly, and then applies a checked
RH error envelope. At microscopic bandwidth the resulting payment is
of order \(\gamma\log^2\gamma\); the exact endpoint control satisfies
the identical input envelope for \(p\ge101\).

There is also an effective arithmetic distinction: nonnegative
logarithmic coefficients reject every nonconstant finite Euler-polynomial
critical-line modification in the declared class, with a negative
prime-power coefficient by exponent \(12^d\) for a degree-\(d\) factor.
An original multiple zero has not been shown to force such a factor.
An isolated polynomial-multiplier control also retains the displayed
gamma factor, conductor one and simple-pole order; it fails the
ordinary Dirichlet-series and logarithmic-positivity premises explicitly.
The positive RHS-02 gate and the strict surplus therefore remain open.
[Review 03](../reviews/03_SIGNED_TRANSPORT_AND_COEFFICIENT_REVIEW_20261020.md)
records the exact scope and a strengthening of the control calculation.
The original task contract is unchanged.

## 6. Zero deflation and rational resolution, 20 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
effort ultra**. [Note 04](../notes/04_ZERO_DEFLATION_AND_RATIONAL_RESOLUTION_20261020.md)
gives explicit location, membership and complete-tail costs for subtracting
certified neighboring zeros. For a fixed-width Poisson sample, a complete
radius `H=c log(gamma/(2pi))` deletion leaves actual tail tending to
`delta^2/(pi c)` and involves asymptotically `(c/pi) log^2(gamma/(2pi))`
zeros counted with multiplicity. This is a sharp cost for that residual,
not a prohibition against using additional zero or tail information.

Higher logarithmic derivatives sharpen a nonnegative rational kernel
while staying in the convergent Euler half-plane. The complete absolute
prime envelope nevertheless has fully optimized infimum
`(1/(4sqrt(pi))+o(1)) log(gamma)/sqrt(log log(gamma))`, over both its width
and derivative order. A short positive-coefficient combination audit
retains the fixed-width logarithmic scale. [Review 04](../reviews/04_DEFLATION_AND_RESOLUTION_REVIEW_20261020.md)
checks uniformity, endpoints, controls and certification precision.

These are bounded quantitative outcomes. Finite walls identify an
exterior inverse-square sum but give no effective upper bound for the
deflation budget. Neither the strict RHS-02 estimate nor a cap surplus
has been obtained. Signed arithmetic and successful all-height certified
deflation remain unresolved; the original task gates are unchanged.

## 7. Close positive sources and exact normalization, 20 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
effort ultra**. [Note 05](../notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md)
constructs, under RH, positive sources arbitrarily close to theta in the
uniform relative norm, yet with exact double zeros at time zero. It
merges consecutive distinct high zeros and preserves the leading theta
tail, functional equation, displayed completion, pole residue one and
normalization at positive real infinity. A complete source bound also
pays every stated finite heat-jet error. The added doubles tend to
infinity; every fixed bounded set of original zeros is eventually kept.

The arithmetic failure is explicit: the de-completed function has an
algebraic large-real correction, excluding an ordinary Dirichlet series
absolutely convergent in any right half-plane. This control screens the
named structural premises and fixed positive approximation tolerance;
it does not screen exact theta arithmetic or errors paid against a
proved height-dependent nonzero margin. A separate polynomial control
retains any fixed slack below theta's strong log-concavity floor. No
claim combines the two controls' preservation lists.

The finite horizontal-shift consumer is exactly an average of the
earlier Poisson consumers, and its positive Euler quotient supplies a
lower bound instead of the needed small upper bound. [Review 05](../reviews/05_SOURCE_CONTROL_AND_SHIFT_AUDIT_20261020.md)
checks the source divisions, tail, normalization, heat statements and
these scoped comparisons. RHS-02's positive estimate, the strict cap
surplus and exclusion of any original multiple zero remain open.

## 8. Signed correlations and one-event precision, 20 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
effort ultra**. [Note 06](../notes/06_SIGNED_CORRELATION_RESOLUTION_AND_MOBIUS_ENERGY_20261020.md)
assesses three quantitative alternatives to independently paying primes.
For the chosen full-window squared-sinc second moment, excluding every
multiple zero requires excess below two and the sharp bandwidth floor
`liminf Delta W/N^(3/2)>=1/2`. This includes clustered configurations
and precedes arithmetic error. The exact prime quadratic form and a
separate exterior-zero payment prevent confusing a full explicit formula
with its finite-window projection.

For the Fejér prime sum, the exact minimum over universal multiplicative
phases is `-C_V+1+o(1)`: such positivity saves only one additive unit,
leaving the optimized leading logarithmic cost unchanged. Actual-height
and event-conditioned information are outside that relaxation.

The reciprocal-zeta calculation gives the sharp local energy forced by
a multiplicity-m zero. A double requires cubic divergence with coefficient
at least `16/|rho zeta''(rho)|^2`; the unchanged Möbius correlation must
carry it. Verified RH bounds still permit this cost, and shifted
negative-moment theorems do not allow an arbitrary zero-shift limit at
fixed height. [Review 06](../reviews/06_CORRELATION_AND_MOBIUS_ENERGY_REVIEW_20261020.md)
checks all constants, limits, imports and scopes. These are costs for
declared attempts, not a new event exclusion or completion of RHS-02.
The original strict-surplus and all-zero gates remain open.

## 9. Local consumers and finite Jensen margins, 20 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
effort ultra**. [Note 07](../notes/07_LOCAL_CORRELATION_AND_JENSEN_MARGIN_COMPARISONS_20261020.md)
proves that every tested nonnegative localized quadratic certificate
implies a matched linear certificate at the same bandwidth, with at least
half its strict margin and with all exterior zeros retained. Its direct
quadratic diagonal can cost twice the linear bandwidth. The finite
whole-line projection is also dominated by its original Fejér test;
this does not permit omitting the full formula's exterior zeros.

For the actual theta coefficients, a hypothetical multiplicity-m zero
produces a finite Jensen Hermite cluster with spacing `d^-1/2` and positive
Laguerre margin `d^(1-m)`. Complete coefficient errors establish these
rates. The existing strict finite Jensen theorem under RH allows repeated
limiting zeros, so continuity supplies no strict endpoint margin.
[Review 07](../reviews/07_LOCAL_CORRELATION_AND_JENSEN_MARGIN_REVIEW_20261020.md)
checks both comparisons and the separate finite-zeta conditioning attempt,
which yielded no signed-prime gain. These are precise costs and scoped
comparisons; RHS-02's positive estimate, strict surplus and all-zero
coverage remain open.

## 10. Reciprocal precision and broader kernel costs, 20 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
effort ultra**. [Note 08](../notes/08_RECIPROCAL_PRECISION_AND_BANDLIMITED_ARITHMETIC_COSTS_20261020.md)
uses a checked RH reciprocal estimate to make a fixed finite zeta sum
accurate to `o(1)` for `delta zeta'/zeta` at `delta=c/log gamma`, with
cutoff `gamma^(1+epsilon)`. It also improves the recorded reciprocal-energy
upper envelope to logarithmic power `2+epsilon`. These fill a declared
precision gap and sharpen a bound; neither supplies the opposing sign,
endpoint coefficient lower bound, or subcubic energy needed for exclusion.

A separate discrete Poisson argument forces a first-prime-harmonic cost
`(I^2/pi^2+o(I^2)) exp(pi/I)` for nonnegative kernels with arbitrary Fourier
signs and `I Delta<=eta<2`, for fixed `eta`. Under complete gamma and pole
budgets, Fejér attains the class's sharp leading `1/2` envelope coefficient.
The unrestricted kernel class is not closed by this result.
[Review 08](../reviews/08_RECIPROCAL_PRECISION_AND_KERNEL_REVIEW_20261020.md)
checks source ranges, the complete energy saddle and kernel constants,
and records the canonical-system route's missing simplicity premise.
The original strict-surplus and all-zero gates remain open.

## 11. Arithmetic controls, translated kernels and stable extraction

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**. [Note 09](../notes/09_ARITHMETIC_CONTROLS_TRANSLATED_KERNELS_AND_STABLE_EXTRACTION_20261020.md)
adds a normalized positive ordinary-Dirichlet control with every prescribed
finite coefficient block unchanged, residue one, uniformly small changes
to logarithmic weights, and RH-sized prime-counting error. Under RH it
has inserted multiple critical-line zeros. It fails the exact functional
equation and entire completion; it is not a theta-flow counterexample.

The same note constructs nonnegative translated kernels with
I Delta tending to three, I tending to zero, and absolute prime payment
tending to zero. The two-copy boundary case makes the fixed gap below
I Delta=2 in Note 08 essential. Complete archimedean budgets are paid.
The subsequent return-height proof in §12 excludes a full-envelope
improvement for this uniform-alignment construction.

A separate positive product kernel uses signed combinations at geometric
widths with error amplification below two. Under a certified noncentral
gap of order 1/log gamma, its sufficient finite-sum cutoff is
gamma^(1+o(1)), improving the matched single-width scheme's
gamma^(3/2+o(1)) for the declared elementary Euler-sum algorithm.
Section 14 updates the matched comparison using Riemann–Siegel. It extracts the actual integer multiplicity; no estimate
forces that integer to be one. [Review 09](../reviews/09_CONTROLS_KERNELS_AND_EXTRACTION_REVIEW_20261020.md)
checks the three distinct premise lists and quantitative bounds.
The signed arithmetic, strict-surplus and all-zero gates remain open.


## 12. Uniform prime-phase returns and complete height cost

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**. [Note 10](../notes/10_UNIFORM_PRIME_PHASE_RETURN_HEIGHT_COST_20261020.md)
uses Granville–Soundararajan's zero-free-rectangle approximation under RH
at two cutoffs. It proves that Note 09's uniform root-of-unity returns
satisfy `log X<=(2+o(1)) log log R`, with a second-order refinement.
All higher prime powers are paid. The two-/three-copy complete envelopes
therefore have leading coefficients at least one/three-halves against
`log gamma/log log gamma`, exceeding the Fejér coefficient one-half.

This resolves the unpaid return-height comparison for the stated sums and
scalar squares. Their small discrete prime payments remain valid.
[Review 10](../reviews/10_PRIME_PHASE_RETURN_HEIGHT_REVIEW_20261020.md) records the separate same-model checks.
Other phase configurations and kernels remain outside the result; no
opposing signed estimate, strict cap surplus or original-zero exclusion
has been obtained. The [progress register][progress] retains those gates.


## 13. Complete absolute-prime envelope: the full admissible class

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**. [Note 11](../notes/11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md)
removes the mass-bandwidth and translated-family restrictions from the
leading-cost comparison. Under RH, every admissible nonnegative
bandlimited kernel with the displayed gamma and pole budgets has
complete absolute-prime envelope at least
`(1/2-o(1)) L/log L`. The centered Fejér sequence attains that leading
constant. No bound on bandwidth or Fourier signs is added.

The proof keeps every prime power and every zero in a smoothed explicit
formula. A continuous Gram identity pays the entire upper Fourier tail
through the kernel's logarithmic pair moment M; averaged Poisson recovers
the normalization factor two. The standalone inequality
`C+I M >= c I^3 exp(pi/I)` prices small prime payment and spread jointly.
The gamma budget itself gives `M<=(1+o(1))L`.
[Review 11](../reviews/11_GENERAL_KERNEL_ENVELOPE_REVIEW_20261020.md) checks all exchanges, constants and scope.

This closes this complete absolute-payment optimization as a route to an
all-height simplicity bound. The near-zero prime-payment examples remain
valid, and Note 10 retains its stronger family-specific return result.
A signed arithmetic estimate or another justified consumer is still
needed; RH-to-simplicity, strict surplus and all-zero coverage remain open.


## 14. Matched finite evaluation, reciprocal costs and signed gap kernels

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**. [Note 12](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md)
imports a classical Riemann–Siegel value formula and pays derivative alias,
small-denominator and combination errors. Both existing gap-certified
extraction schemes now have sufficient leading summand exponent one-half.
The earlier exponent comparison remains specific to its Euler algorithm;
no matched direct first-jet advantage or simplicity margin is established.

The same note gives an exact Riesz Möbius remainder and the double-zero
residue that survives a functional-equation contour shift. Its sufficient
logarithmic length is of order (log gamma)^2 under the stated bound; that
is not a necessary lower bound. The endpoint-energy assessment retains
all exterior forces and identifies the missing inverse-jet estimate.
No pre-zero real-root interval follows from RH.

[Note 13](../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md)
proves exact nonnegative-companion dominance for a certified-gap polynomial
kernel class and a uniform full-prime-payment comparison for its quartic
family. It does not transfer signed gamma/pole budgets or rule out general
sign-changing kernels. [Review 12](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md)
checks these bounded conclusions. The original RHS-02 signed-arithmetic,
strict-surplus and all-zero gates remain open.


## 15. Original theta-mode cancellation and completed kernel scopes

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, ultra**. [Note 14](../notes/14_EXACT_THETA_MODE_GRAM_CANCELLATION_20261020.md)
keeps the exact positive theta modes and their entire signed Gram sum.
The diagonal is asymptotic to c_theta a^(-4), while the complete first-jet
energy is O(a^5 exp(-pi a/4)). The cross term therefore cancels the diagonal
to exponentially small relative accuracy at every large height. This
screens the stated diagonal-coercivity approach on the original source;
it supplies no lower bound or multiple-zero exclusion.

[Note 11 §7](../notes/11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md)
extends the full absolute-payment theorem to the stated strip-analytic
class with infinite Fourier support. [Note 13 §6](../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md)
extends exact gap replacement to general sign changes confined to a
certified central gap, including asymmetric gaps and non-even kernels.
Neither transfers an unverified gamma/pole budget or bounds retained
signed arithmetic. [Review 13](../reviews/13_STRIP_KERNEL_GAP_REPLACEMENT_AND_THETA_GRAM_REVIEW_20261020.md)
checks these extensions and records why the attempted scalar mollifier
and the checked density estimate add no one-event consequence. The
RHS-02 signed estimate and all subsequent global gates remain open.


## 16. Remote-gap completion and bounded event-conditioned attempts

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, ultra**. [Note 13 §§7–8](../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md)
uses an independently proved empty interval near ordinate zero. Its
remote signed multiplier cannot improve the complete envelope of any
fixed even sinc power at any bandwidth once the event height is sufficiently
large. Exact signed poles, the full gamma term and all prime powers are
included. A separate lemma covers target-vanishing remote additions paid
individually; §9 now treats a coherent addition with a different conclusion.

The localized reciprocal-energy and coherent theta-tail attempts did
not supply an event-conditioned lower bound, and the original primitive
identity gives exactly the existing contact condition. [Review 14](../reviews/14_REMOTE_GAP_COMPLETE_PAYMENT_AND_EVENT_ATTEMPTS_REVIEW_20261020.md)
checks these statements without counting another criterion as a result.
The signed-estimate and strict-surplus gates remain unmet.


The coherent continuation in [Note 13 §9](../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md) proves
0<=U(f+a r_delta)−S_gamma(f)<=K_f,q,g delta^(1/2−q), with
a=(gamma²−g²)delta^(q+1/2) and delta gamma integral. It preserves the
target value and zero-side positivity by using the independently empty
remote interval. Its Fourier phase cancels the height phase at every
prime power. An explicit quartic specialization pays all-zero leakage
from the paired xi product; only the base's finite prime set remains in
the coherent residual.

This is a quantitative reduction of overpayment, not a new signed bound:
the limit is precisely the existing signed base sum. At a multiple zero
that sum still includes its full multiplicity. The large negative poles
are canceled exactly by positive prime payments, so these signed kernels
lie outside Note 11's hypotheses. [Review 15](../reviews/15_COHERENT_REMOTE_GAP_SATURATION_REVIEW_20261020.md) checks the
construction and explicit constants. The RHS-02 opposing arithmetic
estimate, strict surplus and all-zero exclusion remain open. This
continuation follows the [result index](../../../../../../../result-summaries/README.md)
and [quantitative-gain rule](../../../../../../../avoid/20_volume_without_a_gain.md).
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**, 20 October 2026.


## 17. Endpoint phase energy and arithmetic rechecks

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. [Note 12 §4](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) proves
the physical phase-energy coefficient pi m(m−1)/(4t) at an isolated
order-m event. A positive derivative scaling beta=sqrt(2t) changes the
outer-cap cost to C_m/sqrt(2t), with C_2=pi+2, while preserving its
(m−1)pi phase. The full spacetime form retains the d beta term. Thus
phase-energy integrability depends on the representation and cannot
be substituted for the invariant winding surplus.

The bounded [Hopf/Julia check](../notes/01_FINITE_WALLS_ARITHMETIC_RESOLUTION_AND_GAUSSIAN_SCREEN_20261020.md) returns exactly the existing
Poisson multiplicity bound. The [bare Euler-heat check](../notes/14_EXACT_THETA_MODE_GRAM_CANCELLATION_20261020.md)
retains formal logarithmic positivity but has no convergent half-plane
at positive time; completion supplies essential mixed derivatives.
[Review 12 §5](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) records the independent internal checks.
These additions follow the existing result/avoid indexes and do not
supply the RHS-02 opposing signed estimate, a new exclusion, or a reason
to activate the deferred BW09 numerical energy campaign.


## 18. Exact ratio energy and the prescribed Möbius approximant

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. [Note 15](../notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md) computes
the exact first-order weighted energy of both the completed and direct
zeta ratios under RH. Each distinct zero of multiplicity m contributes
c_m=m(1−binom(2m,m)/4^m), divided by its weight denominator. Exact
positive Poisson mass controls the complete tail, without a uniform gap
or inverse-derivative assumption. At the standard weight, one double
conjugate pair adds 1/[2(gamma²+1/4)] above the simple-count baseline Z/2.
The available Schur upper is Z, so this remains an event-compatible
identity. A polynomial control confirms that product geometry alone
cannot supply the missing half-linear upper.

[Note 12 §5](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) quantifies a different obstruction: an exact
double zero forces positive limsup error for the prescribed linear-log
Möbius polynomial, at least 4/(|rho|^4 |zeta''(rho)|²). Higher multiplicity
forces unbounded limsup. This is an extraction from Wei–Wu's proof,
with its complete norm retained. Their existing convergence result
already implies simplicity; BCF's sharp upper assumes simplicity, and
RH's constructive damped approximation uses different coefficients.
The grouped-pole calculation records its unpaid remainder separately.

[Review 12 §6](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) records the separate same-model checks.
The [result index](../../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../../avoid/README.md), particularly the
checked-import and quantitative-gain rules, retain the distinction
between these precise costs and the still-missing opposing estimate.
No original multiple zero is excluded, and RHS-02 remains open.


## 19. Heat crossover and the retained arithmetic payment

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. [Note 15 §5](../notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md) resolves
the ratio-energy transition on heat intervals t=v epsilon². Its exact
Hermite profile decreases from the multiple-zero coefficient c_m to m/2;
the double profile is 1+1/[4(1+r²)]. Positive Poisson mass justifies the
global joint limit. The coefficient of 1/v in the large-v excess is one-quarter of the
weighted multiplicity excess K_sigma−M_sigma, linking this heat comparison with
Burnol's arithmetic lower constant. This measures an event-compatible
heat loss, without a contrary uniform time estimate. The original source
controls its smooth linear harmonic mass, which is a different quantity.

Section 6 retains the original arithmetic: its Möbius Gram diagonal
has order 1/epsilon, the complete norm tends to one, and the absolute
double correlation sum diverges. The required first-order coefficient
therefore depends on signed cancellation at absolute scale epsilon.
[Note 12 §6](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) also pays the finite-cutoff comparison:
**Superseded candidate:** the proposed vanishing truncation bound at
damping 2/log N is now ruled out for this exact untapered sequence by
Note 12 §7, even if all critical zeros are simple. The necessary
comparison in §6 remains valid; see the scope correction below.
[Review 12 §7](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) records the separate same-model checks.
The existing result/avoid indexes and RHS-02 acceptance gate remain in force.


## 20. Fixed-damping closure and complete arithmetic remainders

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

[Note 12 §7](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) proves that the untapered polynomial
with damping a/log N cannot converge for any fixed a>0. The complete
squared norm has limsup at least exp(-2a) times the squared limsup of M(x)/sqrt(x).
It is positive at a simple critical zero and infinite at a multiple one;
under RH the same holds for the truncation remainder. This closes the
specific candidate in §19, including the all-simple case. Other tapers,
growing damping parameters and optimized polynomials are not excluded.

[Note 15 §7](../notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md) also computes the exact error of the
natural exponentially smoothed prime-error linearization. Its squared
norm is epsilon times sum d_m/|rho|²+o(epsilon), with d_1=0 and d_2=1/4.
The primary RH mean square has squared multiplicity, so the linearization
does not provide the missing simple-zero upper constant. Section 8 proves
that independent-prime randomization and Jensen add variance with liminf
at least one, while the actual ratio error tends to zero. Section 9's
complete heat identity retains the known event-compatible loss.

These scoped failures narrow the estimates to pursue; they do not prove
simplicity or rule out every use of signed arithmetic. The acceptance
gate remains an actual opposing bound for the unchanged source, with
all zeros and cross terms retained. The [result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md), and
[review 12 §8](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) govern continuation; another reformulation
or reoptimization of these closed payments does not satisfy that gate.


## 21. The cost of increasing damping or endpoint flatness

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

[Note 12 §§8–9](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) gives two further quantitative
scope boundaries. For an order-m critical zero, damping
c loglog N/log N cannot converge when c<=m−1, with the explicit
normalized lower coefficient m²/|rho zeta^(m)(rho)|². A fixed smooth
taper whose first nonzero endpoint derivative has order k likewise
has a positive full-error limsup at multiplicity k+1 and an infinite
limsup at higher multiplicity. These results retain the original
coefficients and complete norm. They neither prove convergence above
those thresholds nor cover infinitely flat or N-dependent tapers.

[Note 15 §9.1](../notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md) checks the heat consumers separately:
the actual ratio energy increases between fixed positive times at small
epsilon, while fixed integrable time averages have the simple first-order
mass even if the initial endpoint is multiple. Such averages cannot
exclude that endpoint. The positive-source cosh control also disproves
universal positivity of the renormalized difference J−H/2. It lacks
the unchanged theta tail and ordinary Dirichlet arithmetic, so this is
a structural scope limit rather than a theta-specific impossibility.
Section 8.3 shows exact binary prime-product coefficient matching forces
independence and hence the already proved Jensen variance cost.

The [result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md), and
[review 12 §9](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) retain the acceptance gate: an actual
opposing estimate using the unchanged source. Merely choosing a parameter
outside a proved obstruction is not such an estimate. RH implies
simplicity remains open in this investigation.


## 22. Actual Gevrey local transfer and the preceding global-upper gap

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

[Note 12 §§10–12](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) supplies a concrete transfer result:
under RH, fixed Gevrey-flat logarithmic tapers admitting the specified
compact extension have the actual local
profile (GF2) at every fixed zero, with its true multiplicity. A complete
xi-product reciprocal bound and rapid Fourier decay pay all external
heights. Finite-window exhaustion then proves the prescribed-polynomial
lower bound (GF13), without simplicity, inverse-jet moments or global
tightness. It strengthens the isolated-model calculation to an actual
lower estimate for the unchanged Möbius coefficients.

The exact local costs also satisfy a sharp simultaneous simple/double
tradeoff. With K=Σm²/|rho|² and A,B the exact simple/double masses,
the actual liminf is at least K+[sqrt(B(4A+9B))−3B]/2. This exceeds
K when A,B>0 for one common taper; only the two-order model optimization is sharp. Section 26 shows that this common-taper gap does not persist for the full polynomial infimum. Every
fixed flat taper costs more than m² at each order separately. The
[Lean check](../numerics/lean/README.md) verifies the abstract
projection identity from supplied Hilbert-space hypotheses, not the
analytic transfer or a zeta theorem.

For the explicit flat profile, the old coefficient obstruction vanishes,
but the tested absolute transfer from damped approximants has a growing
allowance. At this stage no matching global upper bound or convergence
theorem had been established. **That missing-upper status is superseded
for fixed compact Gevrey order 1<sigma<2 by §23 and Note 16.** The local
proof and the failed absolute-transfer allowance retain their stated
scopes. Changing tapers need a separate uniform argument. Section 24
now supplies the fixed-class global constant; an opposing arithmetic
estimate is still required to exclude an original multiple zero. See the [review §10](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md),
[result index](../../../../../../../result-summaries/README.md) and
[scope/payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).


## 23. Complete Gevrey approximation: the preceding rate checkpoint

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review, novelty or optimality claim.

[Note 16](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md) proves under RH, for each fixed normalized compact
Gevrey taper of order 1<sigma<2,
E_(N,w)≪_(w,B)(loglog N)^B/log N whenever B>1+2sigma.
Its exact convolution retains the original Möbius coefficients. An
adaptive nearby-zero cluster estimate and a complementary moving-line
reciprocal estimate give uniform domination at every height; the
zero-free distance decomposition then supplies the complete rate.
“The proof bounds the actual norm at all heights.” This is an actual
upper estimate and convergence theorem, superseding the earlier unpaid
global-norm status for this fixed class.

The distance d_N² is the infimum over length-N Dirichlet polynomials,
so d_N²≤E_(N,w) directly. For every fixed B>3, choose one sufficiently
large fixed p>1 with B>3+2/p in w_p; then
d_N²≪_B(loglog N)^B/log N. No N-dependent choice of p is needed or
licensed. The same note pays the whole fixed-height norm with its
first-order profile sum and proves that sum converges for sigma<2;
neither statement alone permitted a global first-order limit. Section 24
now proves that limit by an additional actual scaled-tail estimate.

[Note 12 §13](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) separately proves an actual lower rate for
the prescribed moving almost-linear flat family. At an exact order-m
zero, m≥2, its scaled norm has liminf at least A_m/|rho|² after
multiplication by eta_N^(2m−3)log N, under the displayed uniform
transfer condition. At eta_N=(log N)^(-theta), a double gives a
growing (log N)E cost; an exact triple with 1/3<theta<1/2 makes E
diverge while the extracted coefficient tends to zero. The fixed-taper
upper theorem does not apply uniformly to this moving family.

[Review 16](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md) checks the primary inputs, complete tails,
normalizations and scope. The checkpoint's wording was “The extra
logarithmic factor leaves room for multiple zeros.” That logarithmic loss
is superseded by §24; its original-zero exclusion and RH-to-simplicity
limitations remain. The original RHS-02–05
exclusion gates remain open; a stronger arithmetic comparison must
remove an actual remaining allowance, not restate those gates. See the
[result index](../../../../../../../result-summaries/README.md) and
[complete-payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).


## 24. Complete fixed-taper asymptotic and the infimum distance

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal audits;
no specialist review, priority or best-known-bound claim.

[Note 16 §11](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md) retains the complete ratio before subtracting
its constant. Telescoping every nearby zero factor produces actual decay
away from the nearest zero; one additional Gevrey moment has the same
leading exponent as the earlier cluster bound. Its full remote
convolution tail is small even after multiplication by log N. Integrating
the actual nearest-zero cells, with no separation assumption, proves
sup_N (log N)E^(|t|>T)≪T^(sigma−2+eta), 0<eta<2−sigma.
Together with the fixed-height theorem, this yields the complete limit
(log N)E_(N,w)→Σ C_m(w)/|rho|² for every fixed compact order 1<sigma<2.
This supersedes both the previous logarithmic loss and its unpaid
global first-order passage. All zeros and completion terms remain.

The direct infimum upper and Burnol lower give d_N² of order 1/log N
under RH. With simplicity additionally assumed, each fixed almost-linear
flat taper has coefficient (1+d eta)Z. Taking N→infinity first for each
fixed eta, then eta↓0, gives (log N)d_N²→Z without an inverse-derivative
moment. This concerns the infimum over polynomials, not convergence of
the original linear Möbius polynomial or a prescribed changing taper.

[Review 16](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md) records independent same-model checks.
The fixed-taper constant still contains the actual C_m, and Burnol's
lower constant contains m². They remain compatible at a multiple zero;
an opposing arithmetic bound is still missing. RH ⇒ simplicity is not
proved. The result and complete-payment guards remain in force.


## 25. A separately paid upper for slowly moving almost-linear tapers

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal audits;
no specialist review, priority or necessary-threshold claim.

[Note 16 §12](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md) fixes one Gevrey cutoff of order 1<sigma<2
and proves the actual full-norm bound E_(N,eta)≤C exp(C eta^(-a))/L,
where L=log N, L^(-theta_0)≤eta<1/4, 0<theta_0<1 is fixed, and
a>1/(2−sigma) is fixed. The kernel, cluster moments, two height regimes
and complete exterior integrals have explicit uniform parameter payment;
this is not an application of the fixed-taper theorem with changing
constants. For eta_N=(log L)^(-kappa), 0<kappa<2−sigma, choose a with
kappa a<1. The actual error is then at most L^(-1+o(1)) and tends to zero.

The already proved order-m JL lower rate requires L E to be at least
a positive multiple of (log L)^(kappa(2m−3)) at a fixed m≥2 event.
It is compatible with this exponential-in-eta allowance. The preceding
fixed-taper tail gap is closed, and this declared moving class now has
a full upper, but no opposing multiplicity-free constant or moving
first-order asymptotic follows. Larger kappa and arbitrary taper schedules
are not ruled out. [Review 16](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md) checks these uniformities
and scope; RH ⇒ simplicity remains unproved.

## 26. Exact RH infimum constant through finite Dirichlet multipliers

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal audits;
no specialist review, analytic formalization or priority claim.

[Note 16 §13](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md) proves under RH alone
(log N)d_N²→K=Σ m_rho²/|rho|², with distinct zeros of both signs.
For a fixed finite zero set, products of two-prime Dirichlet peaks
select fixed tapers adapted to each multiplicity. Their support is at
most 6^k; shortening the base polynomial to floor(N/6^k) preserves the
length-N class. The mixed local-profile limit retains every cross term,
and the complete scaled-tail theorem supplies summable domination.
The finite set, tapers and peak degree are fixed before N tends to
infinity. Burnol's lower constant then matches the upper. Real
coefficients suffice; no effective threshold or convergence statement
for the original linear Möbius polynomial is supplied.

The same-taper tradeoff in §22 remains valid for its stated class,
but is not a lower gap for the general infimum. The earlier simple-zero
Z corollary in §24 remains valid as the special case K=Z. In general,
K−Z=Σ m_rho(m_rho−1)/|rho|², with a double conjugate pair contributing
4/(gamma²+1/4). Thus the attained upper retains the full multiple-zero
cost and does not prove simplicity. The fixed-taper and moving-family
results are unchanged. [Review 16](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md) includes the
adversarial analytic-input recheck and separate same-model mixture
checks. The [result index](../../../../../../../result-summaries/README.md)
and [complete-payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
continue to require an actual opposing estimate for an original event.

## 27. Exact finite filters and a paid root-isolation scale

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist validation, formalization or priority claim.

[Note 16 §14](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md) gives bounded finite Dirichlet filters
whose profiles are exact at every node of a fixed finite set. The whole
remaining profile tail is paid with a constant independent of filter
degrees. For two nodes at a small gap Delta, the least logarithmic
length for exact unit-bounded isolation lies between pi/|Delta| and
pi/|Delta|+log 2, improving the preceding binomial inverse-square gap
cost. Bernstein's inequality supplies the lower bound for arbitrary
complex coefficients; a sharp larger-supremum tradeoff is also retained.

In the original heat coordinates, a double cluster at t=v/(log N)²
requires v≥pi²/2 for exact unit-bounded isolation of its two roots with
length at most N. This is an isolation cost, not a heat-family infimum
bound: using the same taper at both roots does not require isolation.
The fixed-zeta convolution is not transferred to the heat family.
The exact K result in §26 and all previous taper scopes remain unchanged;
no zeros are excluded. [Review 16 §10](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md) checks the
constants and limits under the existing
[complete-payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
