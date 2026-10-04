# Next session for selective loss and actual prime covariance

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal same-model research and checks, not independent specialist review.

The goal is an independently positive revised main with a controlled adverse
allowance on the translated probe. The global arithmetic estimate is open.
[manuscript.tex](../manuscript.tex) summarizes this continuation in the
subsection labelled sec:selective-loss-summary. No new snapshot or commit is
created by this handoff; detailed history stays in the linked records.

Start with the [program overview](selective-loss-program/overview.md), then
[05: diagonal and finite sign](selective-loss-program/05_quadratic_target_and_finite_sign_20261003.md),
[06: mechanism tests and variance](selective-loss-program/06_global_mechanism_tests_20261003.md),
and [07: weighted energy and analyticity](selective-loss-program/07_weighted_energy_abscissa_20261003.md).
The exact complete-response identities are in
[04](selective-loss-program/04_complete_response_and_signed_pairs_20261003.md).

The continuation requested from this handoff is now recorded in
[08: dyadic prime pairs and arithmetic error](selective-loss-program/08_dyadic_shifted_correlations_20261003.md).
It completes the exact shifted-weight reduction, extracts the unconditional
singular-series main, and audits available correlation inputs. Read its
Section 6 for the current signed arithmetic error target. The actual-prime
estimate remains open.

[09: fitted actual error and central frequencies](selective-loss-program/09_actual_error_projection_and_frequency_20261003.md)
continues that remaining target. It proves R(X)_-=O_g(X^2), removes four
exactly harmless Chebyshev-error trends, and bounds the outer additive
frequencies on the target scale. The unproved part is now the signed
central projection in note 09 (19), or the sufficient fitted-error
mean-square bound in note 09 (12). Both retain RH strength.

The subsequent [subpower note](selective-loss-program/10_subpower_growth_and_investigation_paths_20261003.md) and [manuscript revision review](../reviews/ACTUAL_ERROR_SUBPOWER_MANUSCRIPT_REVISION_20261003.md) record a quantitative relaxation: variance O_delta(X^(2+delta)) for every positive delta already suffices, equivalently central projected energy O_delta(X^(1+delta)). Constants and starting thresholds may depend on delta. One fixed delta between zero and one would exclude zeros strictly right of 1/2+delta/2. The transfer theorem is proved; all these global actual-prime estimates remain open. The manuscript now integrates notes 08–10 and includes prioritized investigation paths.

## 1. Fixed normalization and connection to the positive main

Use zero extensions, a=1/4, ell=1/2, and

\[
h(v)=(1-16v^2)^8\mathbf1_{|v|<a},\qquad
g_0=-h'''+h'/4,\quad
\nu=\frac{146640624550936576}{37921101075},\quad g=g_0/\sqrt\nu.
\]

The real odd g has norm one, is C^4, and its constant and two exponential
prepared moments vanish. With tau_r g(x)=g(x-r),
F_r=(g+tau_r g)/sqrt2 has norm one for r>ell. Center this pair by
translation through -r/2 when using the manuscript's I_L=(-L/2,L/2),
L=r+ell; its form value and the correspondingly translated source metric
are unchanged. Keep

\[
G(s)=\int g(v)e^{-sv}dv
=s(1/4-s^2)H_h(s)/\sqrt\nu.
\]

These notes use exp(-sv); the manuscript uses exp(+sv), so this G(s)
is the manuscript's G(-s). Preserve this sign conversion in Laplace
formulas. Its only right-half-plane zero is s=1/2, which cancels the zeta-pole
contribution; it cancels no offcritical nontrivial-zero pole.

The finite Sonin identity is Q=B-K. The active construction uses the known
positive archimedean metric A=Gamma+c_A I>=I, c_A=1-gamma_infinity(0),
with its closed realization on the prepared source interval. Its inverse
is the compressed source inverse, not automatically the global Fourier
multiplier inverse.
Put f_r=QF_r, a_r=A[F_r]<=a_*=2(Q[g]+c_A), and
X(r)=<f_r,A^(-1)f_r>. The exact squared forms in note 03 give
Q=P_epsilon-E_epsilon with P,E>=0 on these sources and an optimized
allowance at most sqrt(a_r X(r)), without arithmetic complement positivity.

Let R_ar be the complete arithmetic response's squared prepared-projection
norm, and N(r)=J(r+a)-(p*p)(r). Then R_ar(r)<=N(r)<=2J(r+a), and
X(r)<=(C_Gamma+sqrt(R_ar(r)))^2.
Consequently quadratic J would give a linear adverse allowance in r.
The existing one-sided probe theorem would then imply RH. See
[03](selective-loss-program/03_centered_dual_energy_20261003.md) for domains,
the source metric, full residuals, and the constants.

## 2. Proved diagonal and bounded continuum sign

The exact causal signal and signed decomposition are

\[
p(y)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(y-\log n),\quad
J(Y)=\int_0^Yp(y)^2dy=D(Y)+\Theta(Y),
\]
\[
K_Y(u,v)=\int_0^Yg(y-u)g(y-v)dy,\quad
D(Y)=\sum_n\frac{\Lambda(n)^2}{n}K_Y(\log n,\log n).
\]

Theta is the full signed off-diagonal sum. Take Theta_+=max(Theta,0)
only after that sum. Every finite window includes log n<Y+a. Cutting at
e^Y, or replacing partial packets by whole ones, changes the result.

For every real Y>=0, note 05 proves unconditionally

\[
\max(0,Y^2/4-48)\le D(Y)\le2\log2\,(Y^2+17/16).
\]

Its outward certificate also proves |p(y)|<4.97 for every real
1<=y<=225, hence

\[
\Theta(Y)<-5\quad(100\le Y\le225),\qquad
\Theta_+(Y)\le25(1+Y)\quad(0\le Y\le225).
\]

These cover whole real intervals. They use complete low-zero enumeration,
the published critical height T_*=3*10^12, sixth-power tails, and outward
192/256-bit records. The unknown tail still carries delta_*exp(y/2);
finite verification does not bound unbounded y. No inverse or source-wide
Sonin complement was numerically certified.

See the [certificate package](../numerics/selective_loss_quadratic_target_20261003/README.md)
and [internal review](../reviews/SELECTIVE_LOSS_QUADRATIC_TARGET_REVIEW_20261003.md).
The finite r allowance applies only when r+a is within the certified range.

## 3. Exact next global target

Let w(t)=t^(-1/2)g(-log t) on [e^(-a),e^a], zero elsewhere, and
V(x)=sum Lambda(n)w(n/x). Then int w=0 and

\[
p(\log x)=x^{-1/2}V(x),\qquad
J(Y)=\int_1^{e^Y}|V(x)|^2\,dx/x^2.
\]

The concrete sufficient target, for all sufficiently large real X, is

\[
\int_X^{2X}|V(x)|^2dx\le C_gX^2\log(2X).
\tag{T}
\]

Shell summation gives quadratic J and Theta_+. The variance diagonal is
already O_g(X^2log X). The missing input is the signed actual-prime cross
term, retaining e^(-a)X<n,m<2e^aX and |log(n/m)|<ell.

Equivalently let a_0=e^(-a), theta(t)=t/a_0-1,
Delta_theta(u)=psi((1+theta)u)-psi(u)-theta*u, and
B(U;theta,eta)=int_U^(2U)Delta_theta(u)Delta_eta(u)du. Note 06 proves

\[
\int_X^{2X}|V|^2dx=a_0^{-1}
\iint w'(t)w'(s)B(a_0X;\theta(t),\theta(s))\,dt\,ds.
\]

This retains signed covariance. Uniform Selberg bounds are sufficient but
may discard cancellation. The X^2-scale theorem cited in note 06 assumes
RH; unconditional X^3 relative-error estimates do not supply (T).

For this noncancelling probe, polynomial J, quadratic Theta_+, and (T)
are RH-strength. RH gives the stronger bounded p and O(X^2) variance.
Do not present (T) as a routinely available weakened consequence of PNT.

## 4. Settled barriers and first continuation steps

Settled barriers: dropping the differential endpoint loses exponential
continuum cancellation. An O(Y) frame norm and quadratic trace do not
control the coherent prime sum. A sparse integer-grid PNT model with
D=Y^2/2+O(1) still has exponential Theta_+. The cumulative autocorrelation Phi(s)=int_0^s phi(t)dt changes sign; entrywise
clipping and separate insertion Cauchy bounds cost exponentially.
Endpoint-only Schur tail positivity on unbounded windows already implies RH.

For J_epsilon=int exp(-2epsilon y)p(y)^2dy, the convergence abscissa is
alpha_*=sup(Re rho-1/2). Known J_(1/2)<infinity supplies no small-weight
rate. Quadratic J is equivalent to J_epsilon=O(epsilon^-2). A Hardy
certificate additionally needs half-plane analyticity and uniform L2
control of order epsilon^-2. A finite meromorphic line norm is insufficient; retain residues
and horizontal pieces in any contour shift.

Completed continuation:

1. Note 08 gives the exact W_X and shifted correlations, including both
   cap blocks and their complete proportional shift range. Whole-packet
   substitution creates an artificial positive continuum error of order X^3.
2. Its diagonal has leading term (3/2)X^2log X. An unconditional
   Montgomery--Soundararajan singular-series mean identity yields a
   negative model main with exactly that leading coefficient. The model
   calculation does not approximate the actual prime pairs by itself.
3. The actual signed error R(X) in note 08 (16) remains open. The next
   target is R(X)_+<=C_gX^2log(2X), uniformly for sufficiently large real X.
   Available almost-all-shift logarithmic errors, and even hypothetical
   individual square-root errors, cost too much when summed absolutely.

Next steps are to estimate this combined signed error, using its exact
partial-summation formula in note 08 (19), or to identify a new arithmetic
input that controls it. Translate every proposed theorem through that
formula, retaining caps, exceptional shifts, proportional shifts, and
uniform real-X endpoints. Record RH or Hardy hypotheses explicitly. The
[floating diagnostic](../numerics/selective_loss_dyadic_pairs_20261003/README.md)
and [internal audit](../reviews/SELECTIVE_LOSS_DYADIC_CORRELATION_REVIEW_20261003.md)
verify the reduction's limited scope.

Current narrower obligations from note 09:

1. For every sufficiently large real X, bound the central projection
   int_1^2 |s int_{-X^(1/11)}^{X^(1/11)} f_X(xi) w_hat(s*xi) dxi|^2 ds
   by C_g X log(2X), with f_X the centered sum over every integer in
   AX<n<2BX. The outer frequency contribution is already controlled
   unconditionally; no more finite-range enlargement is needed for that
   lemma.
2. Alternatively, bound int_{AX}^{2BX}|psi(t)-t-best_fit(t)|^2dt by
   C_g X^2log(2X), with best_fit in span{1,t,sqrt(t),log(t)}. Those trends
   are annihilated exactly before taking the norm. The raw mean-square
   theorem audited in note 09 assumes RH; finite trend removal alone is
   defeated by the existing discrete PNT countermodel.
3. Retain joint frequency phases and complete physical caps in any
   proposed input. Global Parseval, coefficient-only large-sieve bounds,
   and the tested classical exponential-sum estimate miss the central
   square-root scale. No actual-prime upper theorem has been obtained.

The [actual remainder and fitted-error package](../numerics/selective_loss_arithmetic_remainder_20261003/README.md)
and [internal review](../reviews/SELECTIVE_LOSS_ACTUAL_ERROR_REVIEW_20261003.md)
record the finite checks and the unproved global scope.

Seek a signed actual-prime estimate or a precise arithmetic obstruction.
Enlarging the finite certificate cannot replace that obligation. Save
derivations in the program folder, numerics in numerics, and reviews in
reviews; preserve existing work.


## Author-selected quantitative continuation

The author has selected the [subpower milestones program](subpower-milestones/README.md)
for continued investigation. Its first continuation records a proved
complete-cap short-interval transfer and its exact exponent budget,
finite quadratic variance certificates, and a generic non-bootstrap
theorem. The [ledger](subpower-milestones/MILESTONES.md) and
[internal review](../reviews/SUBPOWER_FIRST_INVESTIGATION_REVIEW_20261003.md)
give the statements and limitations. The manuscript source is unchanged
by this notes-only continuation.

For the next global attempt, require one candidate arithmetic lemma with
a genuine fixed relative saving X^(-kappa), kappa>0, at h=X^(3/4), or
an estimate retaining the signed short-interval covariance. All support
and averaging errors are already on the X^2 scale in this gate. The
tested classical mean-square input gives only a subpower saving and
does not reduce global delta. The structural estimates and any finite
prime prefix cannot by themselves furnish an exponent-descent rule.
Do not promote the finite variance bounds to global delta milestones.
