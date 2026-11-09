# B09: a controlled evolution target for the full marked pair

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Thread
01a1bddb-de9d-7221-8f78-7a510e8e4fb9, redirected here by the author.
Actual recorded model and effort are unavailable; captured configurations
are empty. Root is the sole writer; no model change or delegation.

**Status: conceptual selection and elementary design calculations,
proof-author checked.** B09 selects a fixed E10 proof contract for a
collision-stable time modulus of the **full four-real-coordinate pair
function**, not a closed pair equation or a canonical profile value.
The global targets below remain pending E10. Exactly two candidates and
one analytical clarification were used; no numerical implementation.

Read the [result index][results] and [avoid index][avoid], particularly
[geometry13][geometry], [theta14][theta], [controls12][controls],
[classification01][a01], [premises02][a02], [scope07][a07] and
[sibling reuse15][a15]. Classification: a proposed quantitative evolution
estimate for fixed smoothing. It is not an RH-equivalent criterion.
The gain to prove is a time-error allowance with **no reciprocal
minimum-root-gap factor**, including at interior multiple-zero times.

## 1. Fix the target before comparing routes

Keep B06's complete source, normalization, center law and window. For
each fixed finite \(T\ge10\), let
\[
 X\sim T^{-1}1_{[T,2T]}dX,\quad
 \ell=\min(1,4\pi/\log T),\quad \tau=1/4,\quad
 \epsilon=\ell/4,\quad J=\ell^2,\quad
 Q=[-1,1]+i[-1,1].
 \tag{1}
\]
Here tau is the fixed dimensionless Gaussian width, not a time variable.
Use precisely the \(C^2\) window \(W_X=w_{X,1}\kappa_0\) of
[manuscript §6][window]. Define, for \(u,v\in Q\),
\[
 f_{X,u}(z)=J W_X(z)G_\epsilon(X+\ell u-z),\qquad
 r_{\lambda,X}(u)=\sum_j f_{X,u}(z_j(\lambda)),
\]
\[
 d_{\lambda,X}(u,v)=\sum_j f_{X,u}(z_j)f_{X,v}(z_j),\qquad
 R_{2,\lambda,X}=r_{\lambda,X}\otimes r_{\lambda,X}-d_{\lambda,X},
\]
\[
 \overline R_{2,\lambda}=\mathbb E_XR_{2,\lambda,X},\qquad
 C_\lambda=\overline R_{2,\lambda}
              -\overline r_\lambda\otimes\overline r_\lambda .
 \tag{2}
\]
All sums count multiplicity labels. The diagonal subtraction has \(W_X^2\);
distinct labels at the same location are retained. Neither coordinate
is projected to a difference or stripped of its imaginary mark.

**Declared regime change:** extend the same observations from B06's
lambda=0 slice to \(0\le\lambda\le1/2\), keeping \(T,X,W_X,\ell,\epsilon\)
fixed while time varies. The complete Newman family satisfies
\(\partial_\lambda H=-H_{zz}\). Forward collision time is
\(t=\lambda_{\rm ref}-\lambda\), with \(h_t=h_{zz}\); signs reverse,
absolute moduli do not. No negative-Newman-time extension is requested.

The intended theorem is an explicit bound
\[
 \|\overline R_{2,\lambda}-\overline R_{2,\mu}\|_{\infty,Q^2}
       \le L_2(T)|\lambda-\mu|,
 \qquad
 \|C_\lambda-C_\mu\|_{\infty,Q^2}
       \le L_C(T)|\lambda-\mu|.                         \tag{3}
\]
This is a full-function evolution result. It predicts no sine law,
determinantal law, monotonicity, actual profile or collision exclusion.
The higher-marginal objective remains open; E10 is limited to orders
one and two. No probability normalization by a random local count is used.

## 2. Candidate one: a resummed same-center logarithm estimate

Try replacing B06's high polynomial degree by a Laplace cutoff. For its
normalized holomorphic source \(f\), set \(Y=1-|f|^2\in[0,1]\) and
\[
 \mathcal L_S(|f|^2)=\frac12\int_0^S
          \frac{e^{-a}-e^{-a|f|^2}}a\,da,\qquad S>0 .
 \tag{4}
\]
As \(S\to\infty\) this tends to \(\log|f|\) away from zeros.
The apparent opportunity is to estimate the same-center Laplace
covariance directly instead of acquiring every mixed polynomial moment.
It is nonharmonic and therefore is not the harmonic-reference proposal
already excluded in B06.

The needed new information would be a paid estimate of
\(\operatorname{Cov}_X(e^{-a|f_{X,\sigma}(\xi)|^2},
 e^{-b|f_{X,\upsilon}(\omega)|^2})\) on the two disks and \(0<a,b\le S\),
strong enough after the \(1/(ab)\) contractions. At bounded \(a,b\),
\[
 e^{-a|f|^2}=e^{-a}\sum_{j\ge0}\frac{a^jY^j}{j!},\qquad
 \mathbb E[e^{-a|f_\xi|^2-b|f_\omega|^2}]
 =e^{-a-b}\sum_{j,k\ge0}\frac{a^jb^k}{j!k!}\mu_{jk}(\xi,\omega).
 \tag{5}
\]
Uniform convergence follows from \(0\le Y\le1\). Thus this is another
encoding of the same unacquired joint information. Positivity of the
complete source supplies no decay law for this center covariance.

Even its singularity payment is not a demonstrated improvement. With
B06's sublevel constants \(n,\Lambda\), layer cake gives
\(\int e^{-a|f|^2}\le\Lambda\Gamma(1+1/n)a^{-1/n}\).
Integrating the positive tail of (4) yields
\[
 \int|\mathcal L_S(|f|^2)-\log|f||
       \le (n\Lambda/2)\Gamma(1+1/n)S^{-1/n}
       \le (n\Lambda/2)S^{-1/n}.                          \tag{6}
\]
The subtracted \(e^{-a}\) only reduces this tail. This reuses the old
sublevel bound, rather than controlling a product pointwise at zeros.
It retains the same exponent as B06's polynomial regularization.

**Disposition: park this resummation-only candidate.** No new covariance
estimate or justified cost advantage was found from the inspected inputs.
This does not exclude Laplace methods with additional arithmetic
information, nor prove a complexity lower bound. Do not issue an E task
merely to integrate (4) or rename the missing array.

## 3. Candidate two: extend assessed paired calculus to the whole profile

The useful additional input is already available in the **parent**
investigation, beyond B06/E08's time-zero transfer:

| Inherited source | Precisely reused input |
| --- | --- |
| [Parent Note17 §§2–5][p17], accepted by parent E09 | Complete opposite-paired zero dynamics, general \(C^2\) chord cancellation, complete-source count and velocity tails |
| [Parent Note18 §§1–4][p18], accepted by [parent E13][p13r] | Common canonical strip, unit counts, safe-line logarithmic derivative and the \(31A\log(2+X)\) exterior bound |
| [Parent Note19 §§2–4][p19], accepted by parent E13 | Root-multiset continuity, finite multiple events in each compact box, and integration through them without an event-count multiplier |
| [B06 Note11][b06] and [OC E08][e08] | Exact full-pair/self/common-center definitions and fixed smoothing; no acquired profile |

Their internal/shared-premise assessment levels remain unchanged.
The scalar transverse theorem is not presented as a new result.
The proposed increment is its extension to the full marked Gaussian
pair, its self term, and the common-center connected function.

Let \(A\ge1\) be the same enlarged absolute constant as parent Note18
(4), including lambda=0:
\[
 \#\{j:x\le\Re z_j\le x+1\}\le A\log(2+|x|),\quad
 |H_\lambda'/H_\lambda(x+4i)|\le A\log(2+|x|).
 \tag{7}
\]
It is a proved finite constant, **not a measured numerical value**.
The zeros remain in \(|\Im z|\le1\). For
\(\mathcal C_X=\{j:|\Re z_j-X|\le3\}\) and active support
\(|\Re z-X|\le1\), parent Note18 supplies
\[
 n_X\le12A L_X,\quad m_X\le2A L_X,\quad
 |E_X(z)|\le31A L_X,\qquad L_X=\log(2+X).                 \tag{8}
\]
Here \(E_X\) is the complete exterior logarithmic derivative after
removing the finite cluster, with the parent's pairing convention.
No independent root inventory or small-gap lower bound enters (8).

For any real \(C^2\) test \(f\) supported horizontally in that window,
write \(F_1=\sup_{|y|\le1}|\nabla f|\) and
\(F_2=\sup_{|y|\le1}\|D^2f\|_{\rm op}\). In collision time its paired
kernel is
\[
 K_f(z_j,z_k)=
 \frac{(f_y(z_j)-f_y(z_k))e-(f_x(z_j)-f_x(z_k))d}{d^2+e^2}
 =\int_0^1\frac{f_{yy}(z_\theta)e^2-f_{xx}(z_\theta)d^2}
                       {d^2+e^2}\,d\theta .             \tag{9}
\]
Here \(d=\Re(z_j-z_k)\), \(e=\Im(z_j-z_k)\).
The mixed derivatives cancel. In particular \(|K_f|\le F_2\);
the bound survives small separations, though the diagonal value can
depend on approach direction. The local-plus-exterior chain rule and
(8) suggest the fixed E10 scalar target
\[
 \left|\partial_\lambda\sum_j f(z_j)\right|
 \le 2m_Xn_XF_2+2m_XF_1(31A L_X)
 \le A^2L_X^2(48F_2+124F_1).                            \tag{10}
\]
This is a direct extension of the parent's calculation, not an import
of all-real dissipation into a complex cloud. Inactive repeated roots
have zero gradient; they need no assigned velocity.

The parent's exterior subtraction has an actual cutoff error
\[
 e_M(X)=\frac{10A}{M-1}
       [L_X+\log(M+1)+1],\qquad M\ge2\text{ integer}.       \tag{11}
\]
It truncates only the absolutely convergent difference series in parent
Note18 (11); the complete safe-line resolvent is retained. The scalar
derivative error is at most \(2m_XF_1e_M(X)\).
This is not a finite set of independently evolving zeros.

## 4. Explicit constants to freeze for E10

On the canonical strip \(\kappa_0=1\), including its first two derivatives
at the endpoints. Thus only the horizontal cutoff differentiates.
Its derivative bounds are \(w_1=15/4\), \(w_2=24\).
For the normalized planar Gaussian,
\[
 \|G_\epsilon\|_\infty=(2\pi\epsilon^2)^{-1},\quad
 \|\nabla G_\epsilon\|_\infty=
 (2\pi\epsilon^2)^{-1}/(\epsilon\sqrt{\mathrm e}),\quad
 \|D^2G_\epsilon\|_{\infty,\rm op}\le
 (2\pi\epsilon^2)^{-1}/\epsilon^2 .
\]
Define
\[
 a_0=\frac{J}{2\pi\epsilon^2}=\frac1{2\pi\tau^2},\quad
 a_1=a_0\left(\frac{15}4+\frac1{\epsilon\sqrt{\mathrm e}}\right),\quad
 a_2=a_0\left(24+\frac{15}{2\epsilon\sqrt{\mathrm e}}
                         +\frac1{\epsilon^2}\right).     \tag{12}
\]
These bound the value, gradient and Hessian of every \(f_{X,u}\)
on the strip, uniformly in \(u\in Q\) (in fact in the whole observation
plane). The Gaussian Hessian eigenvalues are
\(-G_\epsilon/\epsilon^2\) and
\((|w|^2/\epsilon^4-1/\epsilon^2)G_\epsilon\);
their absolute maxima justify the last estimate.
For \(f_{X,u}f_{X,v}\), use
\[
 F_1\le2a_0a_1,\qquad F_2\le2a_0a_2+2a_1^2.             \tag{13}
\]

Put \(L=\log(2+2T)\) and freeze the following **proof targets**:
\[
 \begin{split}
 R_*&=2ALa_0,\\
 L_1&=A^2L^2(48a_2+124a_1),\\
 L_d&=A^2L^2[96(a_0a_2+a_1^2)+248a_0a_1],\\
 L_2&=2R_*L_1+L_d,\qquad L_C=4R_*L_1+L_d .
 \end{split}                                             \tag{14}
\]
Here \(0\le r_{\lambda,X}\le R_*\).
Apply (10) first to \(f_{X,u}\), then to \(f_{X,u}f_{X,v}\).
The product identity (2) gives \(L_2\); the connected subtraction costs
one further \(2R_*L_1\), giving \(L_C\). Averaging uses the same X in
the raw product and fixed full interval \([T,2T]\).

**The single focused clarification:** a bound for the derivative of this
entire smoothed function does not require a closed two-point evolution
equation. Its exact force expansion can contain triples. Here all such
terms are bounded through the complete pathwise scalar calculus and
the population/exterior bounds (7)–(11), before averaging. No factorization
of a third intensity, rare-pair conditioning, or ensemble law is assumed.
This does not compute the signed derivative or a selected pair's force.

E10 must join simple intervals using parent Note19's finite-event
argument in the fixed padded box
\([T-2,2T+2]\times[-2,2]\). Smooth support crossings carry the derivatives
of W already included in (12), not a hard-boundary deletion. The same
uniform constants then yield (3), and the corresponding \(L_1,L_d\)
bounds, across multiple-zero times. The event count does not multiply
the allowance. This assembly is a proof obligation, not assumed here.

For clarity the full-pair exterior-cutoff derivative error can be bounded
by
\[
 (4R_*m_*a_1+4m_*a_0a_1)e_M^*,\quad
 m_*=2AL,\quad
 e_M^*=\frac{10A}{M-1}[L+\log(M+1)+1].                    \tag{15}
\]
For the connected derivative replace \(4R_*m_*a_1\) by
\(8R_*m_*a_1\). Integration multiplies these errors by the time length.
No source or observation tail is discarded: the theorem uses the exact
canonical family, and the Gaussian remains untruncated. Any numerical
source approximation must separately pay B06/E08's errors.

The expected coarse growth of (14) is \(O_A((\log T)^5)\) as \(T\to\infty\)
with the prescribed shrinking epsilon. That is an upper allowance, not
a lower bound on actual evolution, an optimal rate or a height-uniform
small-error result. A fixed positive blur is essential.

## 5. Actual consequence, and a collision control

If E10 proves (3), any independently acquired approximation
\(\widehat R_0\) with error \(e_0\) at lambda=0 would satisfy
\[
 \|\overline R_{2,\lambda}-\widehat R_0\|_\infty
                \le e_0+L_2\lambda,\quad 0\le\lambda\le1/2. \tag{16}
\]
The analogous connected allowance uses \(L_C\).
This is additive transport of supplied data, not acquisition of
\(\widehat R_0\), a numerical value for A, or a favorable collision margin.
It constrains how fast the full blurred profile can change.

Use the exact local heat polynomial \(H_\lambda(z)=z^2-2\lambda\),
with W=1 near its two roots, as a diagnostic. Write
\(F(u,v)=G_\epsilon(u)G_\epsilon(v)\) in physical coordinates and
\(D_x=\partial_{\Re u}-\partial_{\Re v}\),
\(D_y=\partial_{\Im u}-\partial_{\Im v}\).
Direct Taylor expansion of the two ordered label products gives
\[
 (\partial_\lambda R_2)_{0+}=2D_x^2F,\quad
 (\partial_\lambda R_2)_{0-}=-2D_y^2F,\quad
 [\partial_\lambda R_2]_0=2(D_x^2+D_y^2)F.                \tag{17}
\]
For example \(R_2(0,0)=2(2\pi\epsilon^2)^{-2}
\exp(-2|\lambda|/\epsilon^2)\), with nonzero slope jump.
The profile is Lipschitz through the collision and generally not \(C^1\).
Multiplicity labels give its nonzero value at the double root.
This algebraic control lacks theta arithmetic; it confirms that (3)
can permit a collision. It is not a canonical witness or a certified run.

No collision application is claimed. The Green consumer would still
need its one-point term, unsmoothing/background/tails, an acquired
strict upper value, and a same-time visibility fraction. A gap consumer
would still need its initial gap, isolation and signed exterior bound.
Neither follows from an unsigned time modulus.

## 6. Premise screen and stopping rule

This is an analytical screen against the existing [control register][controls],
not a rerun of its numerical witnesses.

| Control | Canonical premise absent; effect on this proposed estimate |
| --- | --- |
| Euler-factor | Unchanged theta/xi coefficients and completion fail. The local cancellation still applies; common canonical strip/count/resolvent constants cannot be assigned without proof. No collision is rejected. |
| Weighted-square / finite-tail | Full normalized reflection and complete unit weights fail. Only instances satisfying the actual analytic heat hypotheses enter local calculus; a finite endpoint match supplies no global canonical estimates. |
| Reflected super-Gaussian | Complete integer-square theta arithmetic fails. Generic smooth marginal calculus can apply on a paid compact domain and permits the recorded collision. |
| Smooth shape / positive primitive | Exact theta coefficient expansion fails. Positivity and primitive endpoints do not provide the missing joint estimate in candidate one; local heat cancellation is compatible with collision. |
| Finite-prime orbit | Full reflection/all-coefficient identity fails despite the selected finite constraints. No uniform canonical strip or exterior budget is transferred from those constraints alone. |
| Atomic and finite-profile threshold | Complete theta profile/growth and the source's specified eventual-simplicity premises fail. Finite analytic divisor calculus may apply; infinitely many simultaneous events globally are not an obstruction to a finite compact calculation. |
| RH-conditional theta-close endpoint | Ordinary Dirichlet-series arithmetic fails. Its doubles do not refute a Lipschitz estimate; common numerical canonical constants are not asserted for it. |
| Variable observation kernel | The literal cosine/Newman equation fails. The heat-velocity step then lacks its premise. |
| Fractional-profile relaxation | Integer labelled-divisor realizability fails. A general positive fractional measure is not the root multiset used in the finite-event proof. |

No control is claimed to fail (3) at its collision merely because it
lacks theta arithmetic. This is a regularity/transport goal, deliberately
compatible with collisions, rather than a proposed separating inequality.

**Decision:** select candidate two and freeze [E10 r1][request].
Stop B09 at that contract; do not execute it here. Success for E10 is the
full marked pair and connected bounds with all inherited hypotheses,
tail and collision-crossing obligations, or a precise failed clause.
A need for a new closure, different time range, sharper signed
arithmetic estimate or third candidate returns to a dated B09 revision.
No E09 activation, manuscript milestone, investigation closure, new
root-summary claim or external branch-status change occurs.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a15]: ../../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md
[window]: ../manuscript/sections/12_full_pair_transfer.tex
[b06]: 11_TND_OC_B06_CENTER_LAW_AND_JOINT_SOURCE_DECISION_20261108.md
[e08]: ../reviews/09_TND_OC_E08_CLAIM_LEVEL_ASSESSMENT_20261108.md
[p17]: ../../notes/17_TND_O_E08_LOCALIZED_TRANSVERSE_CALCULUS_20261107.md
[p18]: ../../notes/18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md
[p19]: ../../notes/19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md
[p13r]: ../../reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
[request]: ../research-progress/handoffs/23_TND_OC_E10_R1_FULL_PAIR_EVOLUTION_REQUEST_20261108.md
