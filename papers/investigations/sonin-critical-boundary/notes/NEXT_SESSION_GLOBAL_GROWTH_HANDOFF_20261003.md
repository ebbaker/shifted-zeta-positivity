# Next session on the global growth criterion and positive trace comparison

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
were not exposed and are not inferred. Analytic and numerical checks were
performed within the same model family. They are not independent specialist
refereeing, and no literature-priority claim is made.

## Purpose and the user preference for the next session

The user wants to **brainstorm before resuming research**. No next proof
route, computation, or manuscript revision has been selected. Start with a
discussion of the available structure and possible ideas; do not interpret
the earlier handoffs as a mandate to launch their suggested next experiment.
This note preserves the mathematical state and the conceptual discussion
that followed the latest manuscript update.

The global subexponential growth bound, all-window Weil positivity, and RH
remain unproved. What has been proved internally is an equivalence reducing
the arithmetic positivity question to a global condition on one carefully
chosen probe. There are also local full-source positivity certificates,
finite-dimensional Gram certificates, a continuous finite-range bound, and
an unconditional global envelope that falls short of subexponential growth.

## Current files and reading order

Repository: `/Users/ebbaker/Documents/shifted-zeta-positivity`.
Investigation: `papers/investigations/sonin-critical-boundary`.
The current manuscript is [manuscript.tex](../manuscript.tex), particularly
the support-adapted finite-product comparison, Section 10 on prepared-source
criteria, and the final scope discussion.

For a new session, the most useful supporting files are:

1. [Global growth outcome](GLOBAL_GROWTH_OUTCOME_20261003.md) and
   [continuation review](../reviews/GLOBAL_GROWTH_CONTINUATION_REVIEW_20261003.md).
2. [Single-probe equivalence proof](SINGLE_PROBE_GROWTH_THEOREM_20261003.md),
   [one-sided continuation](GLOBAL_GROWTH_ONE_SIDED_20261003.md),
   [zero-tail bounds](GLOBAL_GROWTH_ZERO_TAIL_20261003.md), and
   [weighted-energy cutoff obstruction](GLOBAL_GROWTH_WEIGHTED_ENERGY_CUTOFF_20261003.md).
3. For the operator route, [closed source form and relative correction](CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md),
   [all-window mechanism outcome](ALL_WINDOW_MECHANISM_OUTCOME_20261003.md),
   and [finite-set scaling audit](../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md).
4. [Investigation index](../README.md) and [concise manuscript history](../DRAFT_HISTORY.md)
   link the earlier local results and reviews.

Older handoffs and outcomes retain historical statements about the then
current manuscript, uncommitted changes, and next steps. This note gives
the latest continuation context; the linked proof files retain the detail.

## The original positive trace strategy

The independently nonnegative object is a source-smoothed Sonin projection
trace. For a finite prime set S and positive exponent sigma,

\[
B_{S,\sigma}[F]
=\|C_F\Pi_{S,\sigma}\|_{\mathrm{HS}}^2\ge0,
\]

where C_F is convolution by F and Pi is the corresponding orthogonal
projection. Its nonnegativity is established before any arithmetic
subtraction. The finite Euler boundary identity is

\[
B_{S,\sigma}[F]=\Gamma[F]-W_{S,\sigma}[F]+K_{S,\sigma}[F].
\]

Here Gamma is the archimedean form, W is the prime-shift form, and K is
the boundary correction. At sigma=1/2, for a prepared source F whose
support has diameter at most L, a safe choice is S containing all primes
p<=exp(L). All active prime powers are then included, and the pole moments
vanish. Consequently the complete arithmetic form satisfies

\[
\boxed{Q[F]=B_{S,1/2}[F]-K_{S,1/2}[F].}
\]

If active primes are omitted, there is an additional term
`-(W_{1/2}[F]-W_{S,1/2}[F])`; it cannot be silently included in K.
B and K separately depend on the finite-place representation. Adding a
prime that is inactive for Q need not leave B and K separately unchanged.

Thus the missing comparison is K[F]<=B[F] on the relevant source class
for arbitrarily large windows. B>=0 alone does not prove it. The earlier,
stronger proposal K<=0 fails even on prepared mean-zero sources at the
first-prime window. Positive K directions do not imply negative Q: K can
be positive while remaining below B. The stronger spectral comparison
B>=K_+ remains unproved on the support-adapted all-window class. For a
fixed finite S on arbitrarily large supports, the fixed-place obstruction
already rules it out.

For each fixed finite S and fixed window, the closed source operator B
has a positive gap and compact resolvent; K is bounded, and
`H_rel=B^(-1/2) K B^(-1/2)` is compact. The comparison is the upper form
inequality H_rel<=I. This supplies finite-block, complementary-block,
mixed-term, and resolvent certificate frameworks. Their constants and
fixed-window properties do not provide a uniform estimate as S and L grow.

The full-zeta boundary-limit route has an additional issue. Its positive
majorant and fixed Abel limits identify critical-line zero mass. Exact
projection mass survival is not proved, and identification with the full
Weil form must retain off-line zero contributions. The finite-product
identity above avoids asserting that unidentified critical limit. These
two routes should not be conflated.

## Source class and the origin of the fixed probe

The current all-window target is Q>=0 on compact sources with the three
moments

\[
\int F(x)\,dx=\int e^{x/2}F(x)\,dx
=\int e^{-x/2}F(x)\,dx=0.
\]

Complex coefficients and both parities are included. The two exponential
moments implement pole neutrality; the ordinary moment is the additional
zero-mean condition used in this investigation. Smooth sources and their
stated logarithmic form closure have the same all-window sign assertion.

On prepared sources, in the manuscript's Fourier convention,

\[
Q[F]=\int_{\mathbb R}\gamma_\infty(t)|\widehat F(t)|^2\frac{dt}{2\pi}
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \int\overline{F(x)}\{F(x+\log n)+F(x-\log n)\}\,dx,
\]

where `gamma_infinity(t)=Re digamma(1/4+it/2)-log pi`.
For a compact source the active prime-shift sum is finite.

The probe was chosen as one explicit member of this prepared class,
independently of actual primes:

\[
h_0(x)=
\begin{cases}(1-16x^2)^8,&|x|<1/4,\\0,&|x|\ge1/4,
\end{cases}
\qquad
g_0=(-\partial_x^2+1/4)\partial_xh_0,
\qquad g=g_0/\|g_0\|_2.
\]

The derivative enforces zero mean; the second-order preparation enforces
the exponential moments. The normalization is exactly
`||g0||_2^2=146640624550936576/37921101075`.
The zero extension of h0 is C7 and that of g is C4. Thus g is a real odd,
sign-changing prepared bump, not a nonnegative bump or a C-infinity
function. It belongs to the logarithmic form domain. Moment-preserving
mollification in a fixed slightly larger support justifies using it in the
all-window smooth-source criterion.

Its autocorrelation and transforms are

\[
\varphi(u)=\int g(x)g(x+u)\,dx,\qquad
G(z)=\int g(x)e^{zx}\,dx,\qquad
\Phi(z)=\int\varphi(u)e^{zu}\,du=G(z)G(-z).
\]

Set ell=1/2. The function varphi is real and even, supported on
[-ell,ell], with varphi(0)=1. It is positive definite but is not
pointwise nonnegative. In fact Phi(0)=integral varphi=0, so varphi must
take negative values. Preparation also gives Phi(1/2)=Phi(-1/2)=0.

## What signed means in the prime sum

For r>=0 define

\[
M_g(r)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\varphi(\log n-r),
\qquad
P_g(r)=\sum_p\frac{\log p}{\sqrt p}\varphi(\log p-r).
\]

All arithmetic weights are nonnegative. The signs come from varphi.
For P_g, only primes with exp(r-ell)<p<exp(r+ell) contribute. The sum
is the difference between weighted prime contributions in the positive
and negative regions of this fixed moving profile. A useful estimate must
control their imbalance. The positive continuous main density cancels
exactly because its smoothed contribution is exp(r/2)Phi(1/2)=0.

The phrase "signed arithmetic information about actual primes" means
control of this remaining weighted imbalance. It is descriptive shorthand,
not a separate standard hypothesis or a proved restriction on every possible
proof strategy. A sufficiently strong ordinary prime-counting remainder
could also supply the control. Positivity of a counting measure, its leading
PNT density, and preparation alone are insufficient: an explicit positive
continuous counting model in the one-sided note retains exponential
oscillations despite those properties and a fixed error exponent above
one-half. That model is not a model of all Euler-product arithmetic.

## Why one probe detects the whole arithmetic obstruction

The crucial special property is

\[
\Phi(z)\ne0\quad\text{for }\Re z>0,\ z\ne1/2,
\]

with a double zero at z=1/2. Writing `H0(z)=integral h0(x)exp(zx)dx`,

\[
G(z)=\frac{z(z^2-1/4)H_0(z)}{\|g_0\|_2},\qquad
\frac{H_0(z)}{H_0(0)}={}_0F_1(;19/2;z^2/64).
\]

An elementary differential-equation energy argument proves that all zeros
of H0 are purely imaginary. This establishes the required noncancellation;
it is not assumed for an arbitrary compact probe.

Since ell<log 2, the exact Laplace identity has no lower-endpoint correction:

\[
\int_0^\infty e^{-sr}M_g(r)\,dr
=-\Phi(s)\frac{\zeta'}{\zeta}(1/2+s),\qquad\Re s>1/2.
\]

A hypothetical zero rho with Re rho>1/2 produces a genuine pole at
`s=rho-1/2` with residue `-m_rho Phi(rho-1/2)`. The probe cannot cancel
it. Subexponential growth or the appropriate weighted integrability would
make the Laplace transform holomorphic on Re s>0, excluding that pole.
The double zero at s=1/2 cancels the zeta-pole contribution there.

This proves the following equivalences for this fixed g:

- RH and all-window Q>=0 on the stated source class.
- Every two-source translate Gram is positive semidefinite, equivalently
  q>=0 and |C_g(r)|<=q for all real r, where q=Q[g] and
  `C_g(r)=Q(g,tau_r g)`, `tau_r g(x)=g(x-r)`.
- M_g is bounded, or `|M_g(r)|=O_epsilon(exp(epsilon r))` for every epsilon>0.
- `integral_0^infinity exp(-epsilon r)|M_g(r)|dr<infinity` for every epsilon>0.
- `integral_0^infinity exp(-2epsilon r)|M_g(r)|^2dr<infinity` for every epsilon>0.

The later Landau argument proves that either one-sided eventual
subexponential envelope alone suffices, with the choice of sign fixed:
`M_g(r)<=C_epsilon exp(epsilon r)` for every epsilon>0, or the corresponding
lower bound. Weighted L1 or L2 control of only the positive part or only
the negative part also suffices. Constants and starting separations may
depend on epsilon.

The real-axis regularity used in this argument is established without RH.
Positivity applies to the constructed tail or signed part, allowing
Landau's Laplace boundary lemma. Analytic continuation of a signed
transform by itself does not establish the necessary integral bounds.

The prime-power correction satisfies
`M_g(r)-P_g(r)=o(1)`. Squares have zero main term by Phi(0)=0 and an o(1)
PNT remainder; powers k>=3 contribute O((1+r)exp(-r/6)). Hence all the
growth and signed-part integral criteria can use primes alone.

Every hypothetical zero `rho=1/2+alpha+i gamma`, alpha>0, forces

\[
\limsup_{r\to\infty}e^{-\alpha r}M_g(r)\ge m_\rho|\Phi(\alpha+i\gamma)|,
\qquad
\liminf_{r\to\infty}e^{-\alpha r}M_g(r)\le-m_\rho|\Phi(\alpha+i\gamma)|.
\]

There is no rightmost-zero or spectral-gap assumption. These are
limsup/liminf assertions, not effective bounds on the first violating
separation or on every sufficiently large separation.

## The conceptual point settled in the conversation

The user asked whether g effectively covers all relevant test functions.
The precise answer is **complete detection through arithmetic, not a
proved spanning or approximation claim**. We have not shown that translates
of g generate every admissible source. The sufficiency argument goes
through the noncancellation property, the Laplace identity, RH, and then
the complete explicit formula for arbitrary sources.

Generic pairwise covariance positivity does not imply positivity of every
larger Gram matrix. The older mechanism note correctly states that fact
and discusses a complete family of probes. The newer result establishes
pairwise sufficiency for this special profile using its exact arithmetic
transform. These statements are compatible. Do not import the later
sufficiency into an arbitrary covariance or arbitrary bump function.

We have proved that the global condition is sufficient, and conversely
necessary. We have not proved that this g actually satisfies that condition.
Checking Q[g]>=0 alone or checking finitely many translates cannot do so.
The family of separations remains unbounded and retains the full support
quantifier and the full difficulty of RH.

## The bridge back to the positive trace

For `F=a g+b tau_r g`, the polarized arithmetic matrix is

\[
Q\big|_{\operatorname{span}\{g,\tau_rg\}}
=\begin{pmatrix}q&C_g(r)\\C_g(r)&q\end{pmatrix},
\qquad q\approx1.4669400310052846>0.
\]

For r>ell, the supports are separated and

\[
C_g(r)=-M_g(r)+\epsilon_g(r),\qquad
|\epsilon_g(r)|\le b(r)
:=\frac{\ell e^{-5(r-\ell)/2}}{1-e^{-2(r-\ell)}}.
\]

The union of the two supports has diameter r+ell. After a simultaneous
translation it fits the usual centered source interval, and the support-
adapted identity identifies this matrix with the restriction of B-K.
Therefore a proof that B-K is positive on every such two-source space
would suffice for the all-source conclusion, by the special-probe theorem.
It would be enough even to derive the weaker scalar growth condition.

This gives the B machinery a potentially narrower target, but it does not
yet supply the missing comparison. The proof of the single-probe theorem
does not use independent positivity of B to bound M_g. It uses the
arithmetic identity and zero detection. B>=0 controls its own cross term;
without control of K and its relation to B, that does not control the
cross term of Q=B-K. The finite prime set and projection also change as
r grows. Keeping a fixed finite S while sending r to infinity drops
active arithmetic and invalidates the identification with full Q.

The operator route, the scalar signed-prime route, or a combination remain
available subjects for brainstorming. No argument currently transfers the
independent positivity of B into the required global scalar bound.

## Established quantitative results and their scope

| Result | Established scope | What it does not establish |
|---|---|---|
| Q>=0.09 times the squared source norm and Q>=B/9000 | Every prepared mean-zero complex source of width L=1, S={2} | All windows or the stronger comparison B>=K_+ |
| Q>=(3/2000) times the squared source norm and Q>=(3/6916003)B | Every such source of width L=6/5, S={2,3} | A uniform continuation to unbounded L |
| Seven-source Gram strictly greater than I/20 | Translates of g at 0,2,...,12 and all their complex linear combinations | All sources of width 12.5 or every translate |
| Absolute value of M_g below 1.47931505787654, hence below 1.48 | Every real r in [2,500] | Exact pairwise positivity or a global subexponential envelope |

The first two results are full-source certificates with complementary
errors included, obtained using independent arithmetic coercivity estimates.
Their comparison to B does not constitute a new global positivity proof
from Sonin geometry. See the [first-window outcome](REVISED_B_LOCAL_OUTCOME_20261003.md),
[two-prime outcome](ALL_WINDOW_EXTENSION_OUTCOME_20261003.md), and
[joint seven-source package](../numerics/single_probe_joint_20261003/README.md).

The continuous-range estimate uses an unconditional absolutely convergent
zero expansion and twelfth-power transform decay. If zeros through height T
are verified critical, then for r>ell,

\[
|M_g(r)|\le q+\delta_T(1+e^{r/2})+b(r).
\]

At T=3*10^12, `delta_T<1.058e-116` and
`delta_T(1+exp(250))<3.961e-8`. The positive verified low-zero mass is
bounded by q+delta_T using the zero expansion at r=0; individual low
ordinates need not be enumerated. The published verification, explicit
zero-count bound, and exact profile constants are mathematical inputs.
The [scalar package](../numerics/global_growth_20261003/README.md) passed
192-bit and 256-bit outward runs and a rational-endpoint replay. It does
not rerun the published zero verification. The bound 1.48 exceeds q.

Known zero-free regions give the unconditional asymptotic envelope

\[
M_g(r)=O_c(e^{r/2-c\sqrt r}),\qquad
0<c<2\sqrt{11/5.558691}=2.813455638\ldots.
\]

The zero-tail note also records a Vinogradov--Korobov improvement to the
sublinear saving. These remain exponential with linear rate 1/2. No new
zero-free region is claimed. The relevant published inputs and checked
bibliographic details are linked in the outcome and review; a finite
verified height does not settle arbitrarily large separations.

## Obstacles that should remain visible during brainstorming

- The positive correction directions rule out K<=0 and fixed-rank penalty
  domination of that correction. They do not rule out K<=B or prove a
  negative full Weil form.
- Separate worst-case scalar bounds on Gamma and the prime-shift operator
  lose their joint structure. The current analysis forces doubly
  exponential ranks for that particular class of tail certificates, not
  for every possible method. A finite-rank source removal cannot reduce
  the bare arithmetic norm in the required way.
- The centered reference Gamma+J, with kernel J(x,y)=exp(-|x-y|/2), has a
  growing negative block. Its negative index is at least
  `max(0,ceil(L t_*/pi)-4)`, where `t_*/pi` is certified near 1.949925482.
  A fixed-dimensional repair cannot make it positive on every window.
  See the [explicit index proof](CENTERED_NEGATIVE_INDEX_SHARPENING_20261003.md).
- Taking absolute values term by term in M_g gives a main scale exp(r/2)
  and destroys the needed cancellation, even though the signed continuous
  density is canceled exactly.
- Sharp prime truncation creates an artificial edge. For M_X restricted
  to n<=X, the final smoothing window contributes asymptotically a strictly
  positive constant times `X^(1-2epsilon)` to the squared weighted error
  relative to M_g. It diverges for 0<epsilon<1/2 and stays nonzero at
  epsilon=1/2, even under RH. Subtracting the explicit partial-density
  term removes the leading edge, but PNT alone leaves an error too large
  for the desired small weights. The correct finite energy is
  `integral_0^R exp(-2epsilon r)|M_g(r)|^2 dr`, using every prime power
  n<=exp(R+ell). No uniform bound on these complete-window energies has
  been established in the current work.
- A certificate search can be complete conditional on a positive gap at
  a fixed window. That does not prove gaps at all windows, termination of
  every search, or nonaccumulation of adaptive continuation steps.

## Open questions for discussion

These are optional prompts, not a selected plan or claims of feasibility.
The user may prefer a different direction.

- What additional geometric information in B and K might control their
  difference on widely separated probe pairs while the prime set grows?
- Does the exact correction or inverse metric provide a usable relation
  between diagonal and off-diagonal terms beyond positivity of B alone?
- Is it more promising to pursue one-sided signed-prime control, a
  weighted-energy estimate with complete windows, or an operator comparison?
  What new input would each actually require?
- Would varying the probe while preserving the noncancellation property
  expose a useful estimate, or merely change constants in an equivalent
  reformulation? Any proposed replacement needs its transform zeros and
  admissibility checked.
- Which established positive structure is still not being used in the
  arithmetic reformulation? Conversely, are some contemplated estimates
  simply RH-equivalent statements in another notation?

The next session should distinguish a proved implication, an unproved
estimate, a heuristic mechanism, and an experiment that could discriminate
between mechanisms. There is no need to commit to one of these options
before discussing the user's ideas.

## Manuscript and repository state

At preparation of this handoff, HEAD is
`5052fc961dc755718f2cf88516e78096eb9e8edf`. The global-growth continuation
is in the working tree, not committed. It modified manuscript.tex, README.md,
and DRAFT_HISTORY.md and added the GLOBAL_GROWTH notes, review, and numerical
package. This handoff adds one note and its README link. Inspect current
status when resuming rather than assuming this recorded state is unchanged.
Preserve all existing modifications; do not reset or replace the checkout.

The current manuscript SHA-256 is
`7a23e9797bd3207e7c6fea3fb7510cac6a208ae28f841be4767963776dd1f2bf`.
It is 129,498 bytes and compiled successfully in the desktop built-in editor
after the global-growth additions, with no repairs. The recorded source
checks found 185 unique labels, 207 resolved references, and 22 bibliography
items. The author field is "Drafted for Edward Baker" and the LLM
acknowledgement is present. This handoff does not alter the manuscript.

Research belongs in this investigation's notes directory, numerics in
numerics, and reviews in reviews. Follow the repository
[large-files policy](../../../../LARGE_FILES.md): keep sources and small
records, not large regenerated arrays or third-party PDFs. Do not create
manuscript snapshot folders; use the existing DRAFT_HISTORY.md for concise
manuscript milestones. The synced ChatGPT project's sources directory is
read-only reference material.

The recorded numerical runtime was Python 3.10.0, python-flint 0.9.0, and
FLINT 3.6.0. The session used `PYTHONPATH=/private/tmp/sonin-moment-python-deps`;
that temporary path is not a durable dependency guarantee. Reproduction
commands and source bindings are in each numerical package README. No
large prime sieve, zero enumeration, new certificate run, manuscript
compilation, commit, or push is needed merely to begin the brainstorming
session. When manuscript edits are eventually requested, edit the existing
file in place, retain the open editor, and use its built-in compiler.
