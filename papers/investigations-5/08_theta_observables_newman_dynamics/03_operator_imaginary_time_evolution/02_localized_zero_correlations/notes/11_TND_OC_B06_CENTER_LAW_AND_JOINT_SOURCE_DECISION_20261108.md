# B06: one center law and the missing joint source information

8 November 2026, America/New_York. Prepared for **Edward Baker**, with
substantial OpenAI Codex LLM assistance. Authenticated chat0006, thread
01a1bd30-e805-7183-9318-427ca0a63cc9, turn
01a1bd30-eab3-7030-887b-7dfc219d604f. The source records no actual model
or effort configuration; neither is inferred. Root is the sole writer.

**Disposition: B06 complete at bounded selection and missing-input scope.**
Exactly two routes and one focused clarification are considered below.
The new estimates are **proved in-note; proof-author checking only**.
They provide a finite mixed-source-moment interface, not a value or
limiting profile of the canonical covariance. The precise unpaid input
and stop are in §6. The full pair function remains the objective.

Read the [result index](../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../avoid/README.md), particularly
[cluster11](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[classification01](../../../../../../avoid/01_restating_the_target.md),
[shape02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [separate-bounds12](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Classification: quantitative acquisition bookkeeping and a scoped
harmonic-reference obstruction. No RH-equivalent criterion is proposed.
The gains are the explicit errors below, not evidence for a particular
correlation shape.

## 1. Freeze the ensemble and its quantifiers

For each **fixed, finite T>=10**, choose

\[
 I_T=[T,2T],\quad d\pi_T(X)=T^{-1}dX,\quad h_X=h_{\min}=1,
 \quad \ell_T=b_T=\min(1,4\pi/\log T),\quad
 \tau=1/4,\quad \epsilon_T=\tau\ell_T,\quad J_T=\ell_T^2.       \tag{1}
\]

Use exactly the two-sided W_X, theta_+, theta_- and quintic P in
[manuscript §6](../manuscript/sections/12_full_pair_transfer.tex).
Observe zeta,eta in Q={u+iv: |u|,|v|<=1}; no observation tail is discarded.
Physical smoothing is isotropic before unfolding, with unfolded width
tau in both coordinates. All real/nonreal labels, multiplicities and
approximant collar weights remain. This is lambda=0.

T is the sole prospective height parameter. For a given T all scales
are fixed on I_T and epsilon_T>0, so E07's compact-center theorem applies.
As T tends to infinity, epsilon_T decreases and the source constants
change. No uniform source cutoff, unsmoothed limit or convergence of the
correlation function is asserted. The nominal scale ell_T does not assert
a constant actual mean density.

Write r_X for the unfolded first intensity, d_X for its W_X^2 self term,
and

\[
 C_T=\overline R_2-\overline r\otimes\overline r
     =\operatorname{Cov}_{\pi_T}(r_X,r_X)-\mathbb E_{\pi_T}d_X. \tag{2}
\]

The full function is recovered by adding the product of the first
intensities. This is not a transversely vanishing scalar detector.
Use uniform E02 constants

\[
 \mathsf M=4T+26,\quad
 a_*=\log(2\mathsf M/c_0),\quad
 n=\max(1,\lceil a_*/\log(27/26)\rceil),\quad
 \alpha=2/(n+2),\quad m=2n .                                \tag{3}
\]

Here c_0=(3/5)zeta(5)/zeta(5/2). Normalize either reflected field by
mathsf M. Its modulus on the outer disk is at most one and its anchor
is at least c_0/(2 mathsf M), including an approximant with
delta<=min(1,c_0/2). Jensen gives at most m active labels at each center.
Let A_e=1/(2pi epsilon_T^2), and let U,V be E07's explicit
U_(1,epsilon_T), V_(1,epsilon_T). Then, for either field,

\[
 0\le r_X\le R:=J_TmA_e=\frac{m}{2\pi\tau^2},\qquad
 0\le d_X\le D:=J_T^2mA_e^2=\frac{m}{4\pi^2\tau^4}.          \tag{4}
\]

These are population bounds, not covariance cancellation estimates.

## 2. Route A: the arithmetic transform actually required

Use Fourier convention hat f(k)=integral exp(-ik dot u)f(u)d^2u.
For z_j=x_j+iy_j define
a_j(X)=((x_j-X)/ell_T,y_j/ell_T), w_j(X)=W_X(z_j), and

\[
 A_X(k)=\sum_j w_j(X)e^{-ik\cdot a_j(X)},\qquad
 B_X(k)=\sum_j w_j(X)^2e^{-ik\cdot a_j(X)} .
\]

The Gaussian transform and (2) give the four-real-frequency identity

\[
 \widehat C_T(k,q)=e^{-\tau^2(|k|^2+|q|^2)/2}
 \{\mathbb E A_X(k)A_X(q)-\mathbb E A_X(k)\mathbb E A_X(q)
                         -\mathbb E B_X(k+q)\}.             \tag{5}
\]

Covariance is bilinear; no conjugate is inserted in (5).
Centered Cauchy--Schwarz bounds its magnitude by m^2, since |A_X|<=m.
Also |B_X|<=m. Restricting both frequency vectors to disks of radius K
therefore loses at most

\[
 E_{\rm freq}\le
 \frac{m^2+m}{4\pi^2\tau^4}(2e^{-s}-e^{-2s}),\qquad
 s=\tau^2K^2/2 .                                           \tag{6}
\]

Proof: the total two-dimensional Gaussian frequency integral is
2pi/tau^2; its exterior-disk mass is that number times exp(-s).
Take the complement of the product of the disks and divide by (2pi)^4.
A bounded frequency region suffices for fixed tolerance, provided its
entire mixed transform is actually acquired.

Expanding the first term in braces retains the common-center factor

\[
 \frac1T\int_T^{2T}w_j(X)w_l(X)
                  e^{i(k_x+q_x)X/\ell_T}\,dX .              \tag{7}
\]

The other phase retains k_y y_j+q_y y_l separately. The corrected
BGST v3 §3 theorem supplies a dyadic weighted complex-difference
projection; it does not supply (7) or these independent marks.
To match its ordinate band to (1), its height parameter is T/2,
because x=2 gamma. Its logarithm is log(T/2), not automatically log T.
Even a difference transform at all frequencies supplies only an
anti-diagonal slice of a general pair transform; the BGST analytic test
is a further restricted projection.

A finite information screen: translate a pair of real labels together
from near T to the interior of I_T. Their mutual differences and counts
are unchanged, while (7) with k=q=0 changes because the first pair's
window overlap is clipped. Negative reflected labels outside the active
band can preserve evenness. This concerns arbitrary finite configurations;
it is not another zeta zero set or a universal arithmetic impossibility.

**Route A's missing input:** an arithmetic evaluation of the bracket
in (5) on both frequency disks, with Gaussian-weighted L1 error below
the remaining density tolerance. The inspected BGST theorem does not
provide it. Its existing projected value is retained.

## 3. Pay the center boundary

Keep the full integral (7) in the contract. If pi_T is instead replaced
by its normalized restriction to [T+1,2T-1], deleted probability p=2/T
changes a first mean by at most pR, a raw product mean by pR^2,
the product of means by 2pR^2, and the self mean by pD. Hence

\[
 \|C_T-C_{T,\mathrm{core}}\|_\infty
       \le \frac2T(3R^2+D).                                \tag{8}
\]

The same bound applies if pi_T is kept but all labels outside
x_j in [T,2T] are deleted: those labels contribute only on the two edge
strips, and truncated intensities lie between zero and the originals.
These are separate comparisons, not two costs to add when neither
operation is made. With the exact center law the boundary error is zero.
There is no integration by parts in X or stationary extension.
This does not pay for a later noncompact center law.

## 4. Route B and the single focused clarification

Move to xi=z-X, D_sigma=D(sigma 4i,r), r=25/6. Define

\[
 f_{X,\sigma}(\xi)=F_\sigma(X+\xi)/\mathsf M,\quad
 {\cal K}_{\sigma,\zeta}(\xi)=\frac{J_T}{2\pi}
 \Delta_\xi[\theta_\sigma W_0
             G_{\epsilon_T}(\ell_T\zeta-\xi)],
\]
\[
 {\cal D}_{\sigma,\zeta,\eta}(\xi)=\frac{J_T^2}{2\pi}
 \Delta_\xi[\theta_\sigma W_0^2
 G_{\epsilon_T}(\ell_T\zeta-\xi)
 G_{\epsilon_T}(\ell_T\eta-\xi)] .
\]

Both kernels have strict compact support inside D_sigma. W_0 is the
translated W_X; the kernels are independent of X. The exact intensities
are their contractions with log|f_(X,sigma)|. Constant normalization
and zero-free multipliers drop out by the compact Laplacian identity.

**Clarification: can a leading prime/log Gaussian reference provide the
needed source covariance?** If, for every X, a reference h_(X,sigma)
is harmonic on a neighborhood of the whole closed inner disk D_sigma, then

\[
 \int {\cal K}_{\sigma,\zeta}h_{X,\sigma}
 =\int {\cal D}_{\sigma,\zeta,\eta}h_{X,\sigma}=0.             \tag{9}
\]

Twice integrate by parts; the test has compact support. This holds
pathwise for a random harmonic field as well. Its contracted covariance
and all mixed terms with it vanish. Subtracting h therefore leaves
the entire intensity and its covariance in the nonharmonic residual.
The real part of a finite holomorphic prime polynomial is in this class.
Its leading Gaussian law alone cannot supply this planar density.

This obstruction is limited to harmonic replacements on the same planar
supports. It does not exclude boundary/contour methods, nonharmonic
finite-source fields, or estimates retaining the residual. A critical-line
logarithmic CLT is not a planar replacement theorem. The inspected
Fazzari--Gerspach--Minelli statements concern restricted analytic zero
tests and critical-line logs; their finer correlation statement assumes
RH. They do not supply the mixed planar estimate. See
[source-use06](../references/06_TND_OC_B06_JOINT_SOURCE_SCOPE_20261108.md).

## 5. Remove logarithmic singularities without assuming a joint law

This fixes the missing input more concretely than “bound the covariance.”
It is a regularization within Route B, not a third candidate.
For integer M>=1 set

\[
 P_M(t)=-\frac12\sum_{a=1}^M\frac{(1-t)^a}{a},\quad
 Y_{X,\sigma}=1-|f_{X,\sigma}|^2\in[0,1],\quad
 L_{X,\sigma}^{(M)}=P_M(|f_{X,\sigma}|^2).                  \tag{10}
\]

Let B_g=26/3 (the geometric constant) and

\[
 \Lambda=n\pi B_g^2e^{102a_*/n},\quad
 \beta=\frac{n\Lambda}{2},\quad b_M=\beta M^{-1/n}.           \tag{11}
\]

The E02 sublevel estimate applied to t=|f|^2 gives
area{t<u}<=Lambda u^(1/n). Layer cake yields
integral exp(-a t)<=Lambda Gamma(1+1/n)a^(-1/n), for integer a>=1.
Gamma(1+1/n)<=1 follows by concavity of x^(1/n) under the unit exponential
probability law. Since (1-t)^a<=exp(-a t), the nonnegative logarithm
series remainder gives

\[
 \int_{D_\sigma}
  |L^{(M)}_{X,\sigma}-\log|f_{X,\sigma}||\,dA
 \le\frac{\Lambda}{2}\sum_{a>M}a^{-1-1/n}
 \le b_M .                                                \tag{12}
\]

The sublevel bound extends to u>=1; the layer-cake argument drops no
endpoint atom. Local integrability and multiplicities are paid through
n. The bound is uniform in X for fixed T.

Let r_X^(M),d_X^(M) be the kernel contractions with L^(M).
Put g=J_T U beta/pi and v=J_T^2 V beta/pi. The two disks give

\[
 \|r_X-r_X^{(M)}\|_\infty\le gM^{-1/n}=:d_M,\qquad
 \|d_X-d_X^{(M)}\|_\infty\le vM^{-1/n}=:e_M .
\]

For C_T^(M)=Cov(r_X^(M),r_X^(M))-E d_X^(M), telescope both
the raw product and the product of means:

\[
 \|C_T-C_T^{(M)}\|_\infty
 \le4R d_M+2d_M^2+e_M
 =(4Rg+v)M^{-1/n}+2g^2M^{-2/n}.                            \tag{13}
\]

No logarithmic product is bounded pointwise at a zero. The regularization
is nonharmonic: differentiation gives
Delta P_M(|f|^2)=2M|f'|^2(1-|f|^2)^(M-1)>=0.
Thus (9) does not discard its contribution.

Define the **actual same-center mixed source moments**

\[
 \mu_a^\sigma(\xi)=\mathbb E_{\pi_T}Y_{X,\sigma}(\xi)^a,\quad
 \mu_{ab}^{\sigma\upsilon}(\xi,\omega)
 =\mathbb E_{\pi_T}Y_{X,\sigma}(\xi)^aY_{X,\upsilon}(\omega)^b .
                                                               \tag{14}
\]

Expanding the finite polynomial, with H_M=sum_(a=1)^M 1/a, gives

\[
 C_T^{(M)}(\zeta,\eta)
 =\frac14\sum_{a,b=1}^M\frac1{ab}
 \sum_{\sigma,\upsilon}\iint
 {\cal K}_{\sigma,\zeta}{\cal K}_{\upsilon,\eta}
 [\mu_{ab}^{\sigma\upsilon}-\mu_a^\sigma\mu_b^\upsilon]
 +\frac12\sum_{a=1}^M\frac1a\sum_\sigma
                \int{\cal D}_{\sigma,\zeta,\eta}\mu_a^\sigma .
                                                               \tag{15}
\]

The double integral uses xi,omega on the two disks. The plus sign in
the last term comes from subtracting d_X^(M), whose polynomial log
has a minus sign; its signed kernel does not make this a positive term.
The W^2 self subtraction remains present.

Set kappa=J_T r^2 U and nu=J_T^2 r^2 V, bounds on the sums of
absolute kernel integrals. Suppose estimated means and mixed moments
have uniform errors delta_1,delta_2 on the disks and their products.
Clip estimated means to [0,1], which cannot worsen their error.
The error in (15) is at most

\[
 E_{\rm moments}\le
 \frac{\kappa^2H_M^2}{4}(\delta_2+2\delta_1)
               +\frac{\nu H_M}{2}\delta_1 .                 \tag{16}
\]

Both the mixed moment and the product of means must be supplied.
Separate size bounds or replacement of mu_ab by mu_a mu_b do not meet
this input. The moments use the same X, not independent centers.
Their first-intensity polynomial mean also recovers the full pair
function with its explicit first-intensity error.

More directly, the full-pair surrogate is (15) with the bracket replaced
by mu_ab, omitting the product of means. Its polynomial bias is at most
2R d_M+d_M^2+e_M, and its moment-evaluation error is at most
kappa^2 H_M^2 delta_2/4+nu H_M delta_1/2. These are no larger than
(13) and (16). Thus the budgets in §6 also cover the full pair evaluated
by that direct formula. A finite-M surrogate is not asserted to be
the factorial density of a new point-process law, or to be nonnegative.

## 6. Complete-source error, precision interface, and stop

For a common exact finite-source Hhat_(J_c,U_c), keep the *complete*
E02 arithmetic and radial tails and enlarged-disk multiplier:

\[
 \delta=\mathcal B_{2T}
 [5C_2(J_c)I_{17/2}+B_{\rm source}I_{17/2}^{>U_c}]
 \le\min(1,c_0/2),\qquad
 E=C(a_*,n)(\delta/\mathsf M)^\alpha .
                                                               \tag{17}
\]

B_source=5C_2(0); cutoff J_c differs from Jacobian J_T.
The E07 pair error, plus the error in the product of averaged first
intensities, gives the **connected** source error

\[
 E_{\rm source}
 =\frac{J_T^2E}{\pi}(8nA_eU+V).                             \tag{18}
\]

Each first-intensity error is at most J_T E U/pi, and each first
intensity is at most 2nJ_T A_e. One product costs
4nJ_T^2 A_e E U/pi; connected subtraction pays this product cost twice.
All constants are uniform on I_T.

Apply (10)–(16) to the normalized finite-source field. Combine (18),
its polynomial remainder (13), and the actual moment error (16).
No root isolation, matched roots, real-root hypothesis or discarded
collar is implicit.

For a declared absolute unfolded-density tolerance e>0, for example
e=1/100, explicit sufficient choices are:

1. Choose delta so that (18)<=e/3; the two tails in (17) each pay
   delta/(2 mathcal B_(2T)). Finite cutoffs exist for fixed T.
2. Put x_* = min(1, e/[6(4Rg+v)], sqrt(e/[12g^2])) and
   M>=ceil(x_*^(-n)). Then (13)<=e/3.
3. Obtain the finite-source moments (14), for 1<=a,b<=M and both
   disk signs, with delta_1=delta_2 no larger than
   e/{3[(3/4)kappa^2 H_M^2+(1/2)nu H_M]}. Then (16)<=e/3.

Keep the full center interval; otherwise add the applicable (8) cost
and reallocate tolerance. Step 3 is the **precise missing canonical
input**. No values or certified uniform errors for that array have
been acquired. M may be enormous, n grows with log T, and the
complete-source multiplier is costly. This is a finite accuracy
interface, not a practical evaluator, a lower bound on actual errors,
or a complexity lower bound for all methods.

**Decision:** retain Route B's nonharmonic mixed-source formulation
as the faithful access route. Stop its promotion to a canonical profile
until a concrete arithmetic mixed-moment estimate or certified evaluator
supplies step 3 with an explicit finite work budget. Do not issue an
execution task called merely “bound the covariance.” A new formula for
(2), a one-point CLT, or source accuracy alone does not reopen the task.
A paid value for the declared full function would suffice; no sine
profile or zero exclusion is required.

The ready supporting successor is **E08**, a bounded assessment of the
fixed calculations here, not acquisition of the missing moments.
B07 is conditional on a named new joint-input mechanism. E03/E04 remain
the separate pending scalar-work assessments.

## 7. Collision controls and evidence boundary

This is an analytical premise screen against
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md);
the original collision certificates were not numerically rerun.
Generic Fourier identities and bounded-holomorphic regularizations must
pass controls meeting their actual hypotheses.

| Control family | Premise distinguishing canonical-source use |
| --- | --- |
| Euler-factor | Unchanged full theta/zeta coefficients and conductor fail. |
| Weighted-square and finite-tail | Full normalized reflection and unchanged coefficient expansion fail; no finite all-real threshold is inferred. |
| Reflected super-Gaussian | Integer-square theta arithmetic fails. |
| Smooth shape and positive primitive | Complete canonical theta coefficient expansion fails. |
| Finite-prime orbit | Full reflection/all-coefficient identity fails despite selected finite constraints. |
| Atomic threshold and exact finite profiles | Full theta profile/coefficient structure and the stated eventual simplicity fail. |
| RH-conditional theta-close endpoint | Ordinary Dirichlet-series arithmetic fails. |
| Variable observation kernel | Literal cosine oscillator/Newman equation fails. |
| Fractional actual-profile relaxation | Integer zero-divisor realizability is absent. |

No row is claimed to fail the generic error bounds, and no failed
premise proves a favorable theta value. Harmonic annihilation (9)
applies to the named replacement class for every source, including
theta; it is not a collision exclusion. The finite translation screen
is restricted to difference-only data on arbitrary finite populations.

E02/E07 retain their assessed scope; B02/B03/B04 are not promoted.
[Review08](../reviews/08_TND_OC_B06_AUTHOR_SELF_CHECK_20261108.md)
is proof-author checking only. No canonical covariance/profile, RH gain,
Newman evolution, higher-order quantitative transfer, numerical campaign
or manuscript rewrite is claimed. The investigation remains open.
