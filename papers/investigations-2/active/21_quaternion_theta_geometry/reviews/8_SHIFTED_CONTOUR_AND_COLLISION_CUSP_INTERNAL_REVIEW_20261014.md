# Internal review of shifted contour payments and collision localization

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
The parent session verified its actual current-turn configuration in the
recorded rollout; this reviewing subtask inherited that configuration.

This independent internal LLM review audits the analytic assertions of
[Note 12](../notes/12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md),
its checker replay, and
[Note 13](../notes/13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md).
It also derives the collision region left by the imported uniform localization
theorem. It is not specialist refereeing or formal verification. The
contour identity and all displayed error payments are valid. They do not
establish a positive stationary surplus at every height.

## 1. Complete-source contour identity

On a compact subset of the strip |Im z|<pi/8, Re exp(4z) has a positive
minimum. Every differentiated theta summand is bounded there by a fixed
polynomial in n times exp(-c n^2), with c>0. This proves the normal
convergence used in Note 12.

For Theta(z)=exp(z) theta(exp(4z)), differentiating the n-th nonzero
summand twice and subtracting the summand gives

\[
\frac{2e^z}{16}
\bigl(16\alpha_n^2e^{8z}-24\alpha_ne^{4z}\bigr)
e^{-\alpha_ne^{4z}}=\phi_n(z).
\]

The constant theta summand disappears under the same operation. This
checks the factor 1/16 in equation (1). Jacobi reflection gives evenness
of the complete Phi, and its real coefficients give Schwarz reflection.
Together they imply Phi(iy) is real.

For a fixed real t,x and every integer k>=0, the left contour segment is

\[
\int_0^{ia}(iz)^k e^{tz^2}\Phi(z)e^{ixz}\,dz
=i\int_0^a(-v)^k e^{-tv^2-xv}\Phi(iv)\,dv.
\]

It is purely imaginary. The right segment vanishes uniformly because
cos(4v)>=cos(4a)>0 for 0<=v<=a. Taking real parts proves the physical
jet identity (2). The argument applies to the complete source first.
Taking a finite raw theta sum before shifting would leave a real
vertical contribution and would invalidate the stated approximation.

The strict restriction a<pi/8 is essential to this proof. At a=pi/8,
the absolute damping exp(-pi n^2 exp(4u) cos(4a)) disappears and the
displayed source summands fail to tend to zero as n grows. This review
does not extend the contour identity to that boundary.

## 2. Every index and integration tail is paid

For n>=m, the ratio of consecutive positive majorant summands
alpha_n^r exp(-c alpha_n exp(4u)), r=1,2, is at most the rho of
equation (3). Both its polynomial ratio and its exponential ratio
decrease with n, and the exponential ratio decreases with u. Thus one
geometric denominator pays both parts of the source on the whole
horizontal half-line.

The exponent inequality in equation (5) follows from the quadratic
lower bound for exp(4u). Its remaining quadratic coefficient is
nonpositive under 8 beta>=tau. The linear coefficient is strictly
negative under lambda>0. Expansion of (u+a)^k and exact integration
against exp(-lambda u) gives S_k(lambda,a), including the factorial
and the denominator lambda^(r+1). This proves equation (4) without
an omitted-index or integration cutoff.

For the complete integration tail, the largest consecutive-index ratio
occurs at n=1,u=U and is 16 exp(-3b). For
L(u)=tau u^2+9u-pi c exp(4u), the condition 8b>=tau gives
L''(u)<=0 throughout u>=U, and L'(U)=-lambda_U. The tangent-line
bound then proves equation (7). Replacing the integration tail of the
retained indices by that of all indices overpays a positive majorant.
Adding equations (4) and (7) consequently covers every omitted point
of the index/integration domain. The double payment of their overlap
is harmless.

These are exact analytic errors. An enclosure of the retained finite
integral must still include its actual validated quadrature radius.

## 3. The moving family has the stated scale

For x>=41, the chosen a_x lies strictly inside the allowed strip and
sin(4/x)>=2/x. With m from equation (10),

\[
\beta\ge p\log x+32,\qquad m^2\ge2x/\pi.
\]

The elementary logarithm inequality therefore gives

\[
-\log\rho\ge4\pi m/x-4/m\ge2\pi m/x>0.
\]

For d>0, exp(d)>=1+d implies
(1-exp(-d))^(-1)<=1+1/d. This proves the precise growing denominator
bound in equation (11); no fixed denominator margin is being assumed.

For fixed p>0, m=O(sqrt(x log x)), alpha=O(x log x), and
exp(-beta)<=exp(-32)x^(-p). Using the displayed denominator and the
bounded S_k proves equation (12). Its stated logarithmic exponent 3/2
is conservative: retaining S_k=O(1/log x) would improve that exponent,
but the looser claim is sufficient and valid. The big-O assertion is
derived from the explicit formulas, not used in place of their errors
at any finite x.

For the integration tail, put ell=log x. Equation (10) gives
exp(4U)=x(ell+8)^2 and U<=ell/2+2. Hence

\[
\begin{aligned}
L_U&\le\tfrac12(\ell/2+2)^2+9(\ell/2+2)-6(\ell+8)^2\\
&=-\tfrac{47}{8}\ell^2-\tfrac{181}{2}\ell-364.
\end{aligned}
\]

This checks every coefficient in equation (13). The same estimates
give rho_U<1, lambda_U>0 and 8b>=tau. For fixed k, S_k grows at
most polynomially in ell, so the normalized complete integration tail
is smaller than every fixed negative power of x.

The common physical prefactor is exp(-a_x x)=e exp(-pi x/8).
Thus this construction removes the exponential mismatch of a fixed
real-axis truncation. It supplies absolute normalized errors; it does
not supply a lower bound for the exact normalized observation.

## 4. Physical jets and stationary error targets

Each h_k must be formed as a physical x derivative before a_x, m(x)
and U(x) are selected for its enclosure. Differentiating the adaptive
finite approximation would introduce moving-parameter and cutoff
terms. Note 12 explicitly avoids that operation.

For C_k=exp(pi x/8)h_k, direct differentiation checks
C_(k,t)=-C_(k+2) and C_(k,x)=C_(k+1)+(pi/8)C_k. Consequently the
physical Laguerre form is exactly the positive factor exp(-pi x/4)
times C_(j+1)^2-C_j C_(j+2).

At a genuine stationary point C_(j+1)=0, expanding
-(p_j+e_j)(p_(j+2)+e_(j+2)), with |e_k|<=epsilon_k,
gives equation (16). If a finite Laguerre expression is retained,
|p_(j+1)|<=epsilon_(j+1) additionally pays its square. No unknown
physical norm, amplitude or curvature occurs in a denominator.

The mathematical step still needed is strict positivity of the paid
expression on every remaining stationary set, or a direct paid norm
gap there. Small absolute errors alone cannot establish either sign.

## 5. Imported localization and the remaining collision cusp

The primary source is
[Polymath, arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2).
Its Theorem 1.5(i) supplies an absolute C>0, uniform for 0<t<=1/2,
such that every zero with x>=exp(C/t) is real. The theorem does not
specify a numerical C. Part (ii), with its argument-principle proof in
Section 9, counts one zero with multiplicity in each stated disk;
simplicity follows there. Thresholds on its index and spatial variable
can be aligned by enlarging C. Only part (i) is needed below.

Suppose H(T,a)=H_x(T,a)=0 at 0<T<=1/2. The manuscript's local
Hermite splitting supplies nonreal zeros z_h of H(T-h,.) for arbitrarily
small h>0, with Re z_h tending to a. Evenness and the uniform
localization theorem give

\[
|\Re z_h|<\exp(C/(T-h)).
\]

Passing to the limit proves

\[
\boxed{|a|\le\exp(C/T).}
\]

For |a|>1 this is equivalent to T log|a|<=C. The strict inequality
for each preceding zero becomes non-strict in the limit. Claiming a
strict upper bound with the unchanged C would be unjustified.
An enlarged C'>C gives a convenient collision exclusion at
|a|>=exp(C'/T), with no boundary ambiguity.

Combining this original deduction with the verified height-41 gap gives

\[
41<|a|\le\exp(C/T),\qquad0<T\le1/2.
\]

Thus any unresolved collision is in a cusp approaching t=0 as height
grows. On any fixed time band t>=t_*>0, only the bounded region
|x|<=exp(C/t_*) requires further treatment, but the quoted theorem
does not provide a computable value for that endpoint. As t_* tends
to zero those endpoints diverge. No single finite-height certificate
therefore fills the cusp.

For quantitative extraction from the source, equation (21) and the
definition of s_* give a leading (t/4)log(x/(4pi)) shift of Re s_*.
The preliminary-asymptotic proof after equation (99) displays t/2
instead. This apparent factor-two inconsistency should be recomputed
before extracting numerical constants; the review uses the stated
qualitative localization theorem and extracts no such constants.

## 6. Independent implementation replay

The final
[checker source](../numerics/check_shifted_contour_payments.py)
was inspected and independently executed with Python 3.12.14,
python-flint 0.9.0 and 256-bit Arb/Acb arithmetic, writing its result to
an external temporary file. The regenerated JSON equals the complete
[stored record](../numerics/SHIFTED_CONTOUR_PAYMENT_CHECKS_20261014.json),
including the exact source SHA-256. There is no elapsed-runtime field to
remove before comparison.

The implementation uses the correct entire finite-source integrand,
physical powers (iz)^k and common exponential normalization. It rejects
nonfinite quadrature, unpaid tail hypotheses and insufficient selected
quadrature accuracy. Its floating-point proposal for the integer cutoff
is followed by both rigorous ceiling comparisons; floating-point
rounding does not decide the accepted cutoff. The quadrature's returned
ball radius and the separate analytic omitted-domain errors are both
retained in each final enclosure.

The finite replay checks all four jet payments at five heights,
41,100,1000,10^6,10^12, with N=22,37,135,5610,7606860. At the largest
height it evaluates explicit tail formulas; it does not integrate
millions of retained summands. The eight shifted/direct complete-jet
comparisons are only at x=41 and t=0,1/2, with the stated finite
parameters. An independent comparison of the recorded exact dyadic
upper endpoints verifies that all sixteen normalized quadrature radii
are below 8.8*10^(-54). These selected-point agreements test the
implementation and are not a stationary-sign certificate or an
arbitrary-height numerical evaluation.

## 7. Normalized signed targets in Note 13

Equations (1)--(3) in Note 13 agree with the non-strict collision bound
proved in Section 5 above. Taking C'>C provides time-height padding for
the predecessor branches, while the existing closed norm gap supplies
the spatial padding at X_0. The one-sided predecessors at the upper
time endpoint stay in the covered time range. No numeric value for C
or simplicity at time zero is assumed.

Equations (4)--(5) are the exact physical normalization. On a
differentiable stationary branch, the chain rule gives

\[
\frac d{dt}Z_j=-Z_{j+2}+c\chi'Z_j,
\]

so equation (6) has the required positive drift term
c chi' Z_j^2. Omitting it would wrongly identify normalized-amplitude
growth with the physical Laguerre observation.

At genuine stationarity, r_(j+1)=-p_(j+1). Inserting this equality in
the exact expanded form proves equation (7), including its negative
r_(j+1)^2 term. Equation (8), with its non-strict comparison, implies
Q_j>=0; strict positivity requires a strict comparison. Nonnegativity
already suffices for the manuscript's collision criterion.

For the bounded-loss alternative, L_k<=|Z_k| gives N_low<=N. Since
K_j>=0, equation (9) implies

\[
Q_j\ge Q_{j,\mathrm{finite}}-E_j
\ge-K_jN_{\rm low}\ge-K_jN.
\]

Both inequality directions are correct. The local boundedness required
of K_j through every candidate zero remains a separate condition; an
uncontrolled quotient by N would not provide it. Whole-cell variation
and every quadrature error must be paid before a pointwise target is
promoted to a cell certificate. Note 13 states these qualifications.
No correction is needed to equations (1)--(9).

## 8. Final manuscript transcription check

The current stable
[manuscript](../manuscript/quaternion_theta_geometry.tex)
was read again in the subsections labeled
`sec:height-100-certificate` and `sec:shifted-contours`. The higher-height
statement agrees with the separately replayed records and
[their independent numerical review](9_HIGHER_HEIGHT_CERTIFICATES_INTERNAL_REVIEW_20261014.md):
510 cells, the declared orders and N=4, both stated stationary margins,
the exact rational norm floor, its minimizing cell, and the reflected
closed strip through height 100. The manuscript's convenient norm floor
10^(-16) is weaker than the certified rational floor and is valid.

The contour propositions, adaptive-scale corollary and their proofs
correctly transcribe Note 12. The conditions p>0, x>=41, uniform
0<=t<=1/2, the strict strip bound, growing geometric denominator, and
complete integration exponent are retained. The frozen endpoint
construction specifies Y>=41 and preserves its separate quadrature and
parameter-variation obligations.

The cusp paragraph now specifies 0<T<=1/2 and retains the non-strict
collision inequality with strict C'>C padding. The normalized moving
branch has the correct scale drift. A missing local definition of r_k
in the first transcription was identified and has been corrected to
Z_k=p_k+r_k, |r_k|<=epsilon_k before the stationary expansion; the
revised passage was reread. Its conclusion asks for a nonnegative
surplus and makes no all-height positivity claim. No further mathematical
transcription error was found. Compilation and page-layout inspection
are the parent session's separate checks.

## 9. Assessment

Note 12 proves a useful all-height approximation theorem with complete
absolute four-jet payments at the exponential gamma scale. Its formulas
and qualifications pass this analytic audit. The imported uniform
localization theorem further identifies the moving region that a global
stationary argument must cover. Neither result supplies its missing
strict theta-specific stationary surplus. RH remains unproved.
