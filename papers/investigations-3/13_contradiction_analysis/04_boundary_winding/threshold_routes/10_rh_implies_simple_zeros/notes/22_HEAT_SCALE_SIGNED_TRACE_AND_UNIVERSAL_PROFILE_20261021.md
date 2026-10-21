# Heat-scale signed trace and its universal endpoint profile

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Status: **proved in-note, conditional on the
specified endpoint event; same-assistant self-review only**. RH supplies
the sharper complete-root concentration bound; the local profile has
the weaker analytic version specified below.
No specialist review or original theta zero exclusion.

This is the first bounded HMC-05 comparison. For the complete signed
residual in [Note 21, MT21][n21], choose thickness
\(\eta=r\sqrt{2t}\), with \(r\) in a fixed bounded interval.
Instead of using a collapsing minimum of \(H^2+H_x^2\), the proof
integrates against the exact physical phase measure. It gives an explicit
\(O(\sqrt t\log(1/t))\) error around a finite Hermite profile, retaining
the entire birth cluster and the complete source remainder.

The improvement is quantitative, but its leading profile is generic.
For a double endpoint the observation tends to \(\pi(1+r^2)\).
For an order-\(m\) endpoint the outer-cap observation tends to
\(\pi[L_{m-1}^{(1)}(-r^2)-1]\). Matching controls have the same
profile. The selected leading-profile discriminator therefore fails;
HMC-05's separating arithmetic estimate remains open.

Read with the [program][program], [progress][progress],
[result index][results], [local heat summary][heat-summary],
[control register][controls] and [avoid index][avoid], particularly
[classification][a01], [control premises][a02], [scoped conclusions][a07]
and [separate payments][a12]. This is an estimate and a precisely scoped
comparison, not a new equivalent simplicity criterion supported by tests.

## 1. Selected observable and distinction from previous results

Keep the original complete theta source and \(H_t=-H_{xx}\), with
\(8H(0,z)=\xi(1/2+iz/2)\). Suppose, for this conditional calculation,
that \(H(0,\cdot)\) has exact multiplicity \(m\ge2\) at \(a_0>0\).
Put
\[
\tau=\sqrt{2t},\quad
a_m=H^{(m)}(0,a_0)/m!\ne0,\quad
p_\tau(z)=\frac{H(\tau^2/2,a_0+\tau z)}{a_m\tau^m},
\quad P=\operatorname{He}_m.
\tag{HT1}
\]
Let \(\lambda_1<\cdots<\lambda_m\) be the roots of \(P\), and
\(\nu_i\in(\lambda_i,\lambda_{i+1})\) the roots of \(P'\).
At sufficiently small positive time, let \(a_i(t),a_{i+1}(t)\)
be the two actual root walls corresponding to these adjacent Hermite
roots. They are adjacent in the full real spectrum. All other birth
roots remain in \(p_\tau\), and are not discarded by pair deflation.

The observable is exactly Note 21's normalized tube integral
\[
I_\eta^{(i)}(t)=\int_{a_i}^{a_{i+1}}
 \frac{\overline Q_\eta(t,x)}{H(t,x)^2+H_x(t,x)^2}\,dx,
\quad Q=|H_x(x+iv)|^2-\operatorname{Re}(H(x+iv)\overline{H_{xx}(x+iv)}),
\]
where the bar averages over \(-\eta\le v\le\eta\), and
\(R_\eta^{(i)}=I_\eta^{(i)}-\pi\). Its complete signed two-source
formula is MT21; it is not replaced by separate absolute source sectors.
The physical cap phase remains exactly \(\pi\).

[Note 12, Section 4][n12] already gives the physical phase peaks of width
\(2t/m\), their Lorentzian limit, and phase-energy asymptotics. Those
are inherited inputs and are not claimed again as new results here.
The present output is the transverse tube profile, a finite complete-source
error bound for it, and its matched control comparison. Investigation 21
[Note 57][g57] treats a different circle current on the predecessor side
of a collision; its radius constants are not transferred to this tube.

## 2. Complete-source normal-form error

For each bounded complex \(z\)-set,
\[
p_\tau(z)=P(z)+O(\tau)
\]
with derivatives. The normalization is the probabilists' one,
\(e^{zs-s^2/2}=\sum\operatorname{He}_n(z)s^n/n!\), as in
[DLMF 18.12.16](https://dlmf.nist.gov/18.12.E16).
The same heat/root scaling appears in
[Polymath, Proposition 3.1(ii)](https://arxiv.org/html/1904.12438v2#S3).
Here is a complete and explicit remainder for the application below.

Choose \(0<r_*<\infty\), a compact real interval \(J\) containing the
selected Hermite gap and small endpoint neighborhoods, and
\(Y\ge\max_{x\in J}|x|+r_*\). Choose any \(R>0\) and set
\[
M=\int_0^\infty e^{R^2u^2/2+R(Y+1)u}\Phi(u)\,du,
\qquad C=\frac{2M}{|a_m|R^{m+1}},\qquad
\delta_j=j!C\tau\quad(0\le j\le3).
\tag{HT2}
\]
Then, for \(0<\tau\le R/2\),
\[
\sup_{|z|\le Y}|p_\tau^{(j)}(z)-P^{(j)}(z)|\le\delta_j.
\tag{HT3}
\]
Indeed, \(f(w,z)=H(w^2/2,a_0+wz)\) is entire in \(w,z\), and on
\(|w|\le R,|z|\le Y+1\) its absolute value is at most \(M\).
Expanding the full source using the displayed generating function gives
the \(w^n\) coefficient \(H^{(n)}(0,a_0)\operatorname{He}_n(z)/n!\).
The coefficients below \(m\) vanish by the stated event, and the
\(m\)-th is \(a_mP\). Cauchy's coefficient bound sums the remainder
geometrically to \(C\tau\) after division in HT1. Cauchy's estimate
on the additional unit \(z\)-disk gives HT3. This argument retains the
complete cancellation that creates the event; no source summand is
declared small relative to the vanishing field.

The moment \(M\) is finite and has Note 21 MT18–MT19's explicit source
and theta-index tail bounds, with \(T=R^2/2\) and transverse allowance
\(R(Y+1)\). Numerical quadrature, if attempted, would need its own
certified error. No such evaluation is claimed. Dependence on the fixed
event through \(|a_m|^{-1}\) is explicit; this is not an all-height
or multiplicity-uniform estimate.

## 3. Exact phase measure and quantitative concentration

Write the scaled actual endpoints as \(\alpha_\tau,\beta_\tau\)
and the unique critical point between them as \(\nu_\tau\).
On their open gap define
\[
s_\tau(y)=p_\tau'(y)/p_\tau(y),\quad
L_\tau(y)=p_\tau'(y)^2-p_\tau(y)p_\tau''(y),
\quad
d\sigma_\tau(y)=\frac{\tau L_\tau(y)}
 {p_\tau'(y)^2+\tau^2p_\tau(y)^2}\,dy.
\tag{HT4}
\]
Under RH the full product in [Note 19][n19] gives
\[
-s_\tau'(y)=\sum_{\text{all scaled roots }z_j}(y-z_j)^{-2}
\ge (y-\alpha_\tau)^{-2}+(\beta_\tau-y)^{-2}
\ge\frac8{(\beta_\tau-\alpha_\tau)^2}.
\tag{HT5}
\]
The sum is absolutely convergent. The remaining birth roots and all
exterior roots have their correct positive contributions in this
inequality. In particular \(s_\tau\) decreases from \(+\infty\)
to \(-\infty\), with its unique zero at \(\nu_\tau\), and
\[
d\sigma_\tau=\frac{-\tau s_\tau'}{\tau^2+s_\tau^2}\,dy,
\qquad \int d\sigma_\tau=\pi.
\tag{HT6}
\]
This is exactly the physical cap phase measure; no derivative rescaling
has changed its denominator.

Suppose the scaled gap length is at most \(d_*>0\) and put
\(\kappa=8/d_*^2\). From HT5,
\(|y-\nu_\tau|\le\min(d_*,|s_\tau(y)|/\kappa)\). Changing variables
in HT6 proves
\[
\int|y-\nu_\tau|d\sigma_\tau\le
\mathcal C(\tau):=\frac{\tau}{\kappa}
 \left[\log\left(1+\frac{\kappa^2d_*^2}{\tau^2}\right)+2\right].
\tag{HT7}
\]
The exact integral of the majorant is
\(\tau\log(1+(\kappa d_*/\tau)^2)/\kappa
+2d_*[\pi/2-\arctan(\kappa d_*/\tau)]\); the last summand is at most
\(2\tau/\kappa\). Therefore any Lipschitz observable \(B\) satisfies
\[
\left|\int B\,d\sigma_\tau-\pi B(\nu_\tau)\right|
\le \operatorname{Lip}(B)\mathcal C(\tau).
\tag{HT8}
\]
This estimates the reciprocal-energy concentration after integration,
without substituting a collapsing physical minimum into the entire cap.

For any real entire \(p\), define
\[
A_r[p](y)=\frac1{2r}\partial_r|p(y+ir)|^2
\quad(r>0),\qquad A_0[p]=p'^2-pp''.
\tag{HT9}
\]
Equivalently, \(A_r\) is the average of the Hermitian Laguerre numerator
over \([-r,r]\). The identity follows from
\(Q[p]=\tfrac12\partial_v^2|p(y+iv)|^2\).
Under the exact scaling HT1, the factors \(a_m^2\tau^{2m-2}\) cancel,
and Note 21's observation becomes
\[
I_{r\tau}^{(i)}(\tau^2/2)
=\int_{\alpha_\tau}^{\beta_\tau}
       \frac{A_r[p_\tau](y)}{L_\tau(y)}\,d\sigma_\tau(y).
\tag{HT10}
\]
The ratio has a regular limit on the entire scaled gap, including its
endpoints. Its denominator is the nonzero Laguerre numerator of the
scaled field, not a claimed positive floor for physical \(E\) at zero.

## 4. Explicit error around the Hermite profile

The following finite constants make the limiting statement quantitative.
Choose \(\rho>0\) so that the neighborhoods of
\(\lambda_i,\nu_i,\lambda_{i+1}\) of radius \(\rho\) are disjoint,
the critical neighborhood lies between the two root neighborhoods, and
\(P'\), respectively \(P''\), has no zero on the root, respectively
critical, neighborhoods. Let
\[
J=[\lambda_i-\rho,\lambda_{i+1}+\rho],\quad
d_*=\lambda_{i+1}-\lambda_i+2\rho,
\]
\[
\sigma_r=\min_{|y-\lambda_i|\le\rho\ \text{or}\ |y-\lambda_{i+1}|\le\rho}|P'(y)|>0,
\quad \sigma_c=\min_{|y-\nu_i|\le\rho}|P''(y)|>0,
\]
\[
\mu=\min_{[\lambda_i+\rho,\lambda_{i+1}-\rho]}|P|>0,
\quad l_0=\min_J(P'^2-PP'')>0,
\quad B_j=\max_{|z|\le Y}|P^{(j)}(z)|\quad(0\le j\le3).
\tag{HT11}
\]
These are constants of known finite polynomials. Positive lower bounds
and upper bounds may replace the exact extrema; elementary polynomial
root isolation can enclose them. No unknown theta-zero separation is
hidden in this definition. Positivity of \(l_0\) follows either from
the real-root product away from the zeros or from \(P'^2>0\) at each
simple zero, followed by compactness.

Require \(\tau\le\min(R/2,1/2)\) and
\[
\delta_0\le\tfrac12\min(\sigma_r\rho,\mu),\quad
\delta_1\le\tfrac12\min(\sigma_r,\sigma_c\rho),\quad
\delta_2\le\sigma_c/2.
\tag{HT12}
\]
Sign changes and derivative floors then isolate the two actual roots and
the critical point in those neighborhoods, and exclude any intervening
root in the middle interval. In particular
\(|\nu_\tau-\nu_i|\le\delta_1/\sigma_c\). This proves the required
rank membership rather than treating formal nearby roots as the cap.

Set
\[
\Delta=\delta_1(2B_1+\delta_1)+B_0\delta_2+B_2\delta_0+\delta_0\delta_2,
\quad N_j=B_j+\delta_j,
\quad U=N_1^2+N_0N_2,\quad D=N_1N_2+N_0N_3,
\]
\[
U_0=B_1^2+B_0B_2,\quad D_0=B_1B_2+B_0B_3.
\]
In addition require \(\Delta\le l_0/2\), and put \(l=l_0/2\),
\[
K=D/l+UD/l^2,\qquad K_0=D_0/l_0+U_0D_0/l_0^2.
\tag{HT13}
\]
All these conditions hold for sufficiently small \(\tau\) at the fixed
event. The bounds HT3 imply, uniformly for \(y\in J\), \(0\le r\le r_*\),
\[
|A_r[p_\tau]-A_r[P]|\le\Delta,\quad
|L_\tau-(P'^2-PP'')|\le\Delta,\quad L_\tau\ge l,
\]
\[
\operatorname{Lip}(A_r[p_\tau]/L_\tau)\le K,
\quad \operatorname{Lip}(A_r[P]/(P'^2-PP''))\le K_0.
\]
For the derivative allowance, differentiate the full Hermitian numerator:
\(\partial_y Q[p]=\operatorname{Re}(p'\overline{p''}-p\overline{p'''})\).
The cancellation here gives \(D\), rather than a separately paid
three-term derivative bound.

Define the universal profile
\[
\Gamma_{m,i}(r)=\frac{A_r[P](\nu_i)}{mP(\nu_i)^2},\qquad
\Gamma_{m,i}(0)=1.
\tag{HT14}
\]
The Hermite equation gives \(P''(\nu_i)=-mP(\nu_i)\), so this is
the limiting ratio in HT10. Combining HT8 with the ratio difference and
critical-point displacement bounds yields
\[
\boxed{\left|I_{r\tau}^{(i)}(\tau^2/2)-\pi\Gamma_{m,i}(r)\right|
\le K\mathcal C(\tau)+\pi\left[
\frac{\Delta}{l}\left(1+\frac{U_0}{l_0}\right)
+K_0\frac{\delta_1}{\sigma_c}\right].}
\tag{HT15}
\]
This is uniform for \(0\le r\le r_*\). Its right side is
\(O_{a_0,m,i,r_*}(\tau\log(1/\tau))\), with every constant specified
above. No derivative of an uncontrolled asymptotic, source cutoff without
a tail, or physical endpoint floor is used.

**Local analytic version.** The leading profile does not require an
all-real spectrum elsewhere. Under HT3 and HT11–HT13 alone,
\(L_\tau\ge l\) and \(|p_\tau|\le N_0\) imply
\(-s_\tau'\ge l/N_0^2\) between the two isolated real roots.
Use \(\kappa=l/N_0^2\) in HT7–HT15 instead of HT5's
\(8/d_*^2\). This \(\kappa\) stays bounded below as
\(\tau\downarrow0\), so the same uniform error order and profile follow.
For a general analytic heat germ, replace HT2's source integral by a
bound on \(H(w^2/2,a_0+wz)\) in a sufficiently small polydisk. The
same Cauchy argument applies. This local version is what is used for
controls without an all-real heat slice; it does not assert HT5 for them.

## 5. Profiles, outer-cap formula, and thickness regimes

For the real-root polynomial \(P\), write
\(|P(y+ir)|^2=\sum_{n=0}^m\ell_n(y)r^{2n}\). Its product over roots
shows \(\ell_n(y)\ge0\), and \(\ell_2(\nu_i)>0\) for \(m\ge2\).
Thus \(\Gamma_{m,i}\) is a polynomial in \(r^2\), with constant
one and strictly positive higher coefficients at the critical point.
In particular
\[
\Gamma_{2,1}(r)=1+r^2,\qquad
\Gamma_{3,1}(r)=\Gamma_{3,2}(r)=1+\tfrac32r^2+\tfrac14r^4.
\tag{HT16}
\]
The next coefficient for every fixed \(m,i\) is
\[
\Gamma_{m,i}(r)=1+\frac{4m-2-\nu_i^2}{6}r^2+O(r^4).
\tag{HT17}
\]
Indeed, at \(P'=0\),
\(Q_{vv}=3P''^2+PP''''\), while the Hermite equation gives
\(P''''=m(m-2-\nu_i^2)P\). This verifies HT17 without a fitted law.

The outer-cap sum has a particularly simple exact expression:
\[
\boxed{\sum_{i=1}^{m-1}\Gamma_{m,i}(r)
=(m-1)+\sum_{j=1}^{m-1}\binom m{j+1}\frac{r^{2j}}{j!}
=L_{m-1}^{(1)}(-r^2)-1.}
\tag{HT18}
\]
Here \(L_n^{(1)}\) is the associated Laguerre polynomial in
[DLMF 18.5.12](https://dlmf.nist.gov/18.5.E12); the finite sum in HT18
specifies the normalization independently.

To prove HT18, use the standard Gaussian probability measure. Its monic
Hermite norms are \(\int\operatorname{He}_j\operatorname{He}_k
=j!\,\mathbf1_{j=k}\), obtained by integration by parts.
The Gaussian quadrature nodes \(\nu_i\), roots of
\(\operatorname{He}_{m-1}\), have weights
\[
w_i=\frac{(m-1)!}{P(\nu_i)^2}.
\]
For clarity, the finite quadrature fact follows by division by
\(\operatorname{He}_{m-1}\): orthogonality reduces a polynomial of
degree at most \(2m-3\) to its interpolant at these nodes.
The Christoffel–Darboux identity, obtained by telescoping the Hermite
recurrence, gives the weights as
\((m-2)!/[(m-1)\operatorname{He}_{m-2}(\nu_i)^2]\), equal to the
displayed value because \(P(\nu_i)=-(m-1)\operatorname{He}_{m-2}(\nu_i)\).
Hence these discrete inner products agree with the Gaussian ones for
Hermite degrees at most \(m-2\).

The shift formula from the generating function reduces at a node to
\[
P(\nu_i+ir)=
-\left(m-1+\binom m2r^2\right)\operatorname{He}_{m-2}(\nu_i)
+\sum_{k=3}^m\binom mk(ir)^k\operatorname{He}_{m-k}(\nu_i).
\]
Discrete orthogonality therefore gives
\[
\sum_iw_i|P(\nu_i+ir)|^2
=\left(m-1+\binom m2r^2\right)^2(m-2)!
+\sum_{k=3}^m\binom mk^2r^{2k}(m-k)!.
\]
Apply \((2rm(m-1)!)^{-1}d/dr\) and simplify to get HT18, with
continuous extension at \(r=0\). This proves all multiplicities;
the finite replay below is not the proof of that quantifier.

Summing HT15 over the \(m-1\) adjacent caps gives
\[
I_{r\sqrt{2t}}^{\mathrm{outer}}(t)
=\pi[L_{m-1}^{(1)}(-r^2)-1]+O(\sqrt t\log(1/t)),
\]
\[
R_{r\sqrt{2t}}^{\mathrm{outer}}(t)
=\pi[L_{m-1}^{(1)}(-r^2)-m]+O(\sqrt t\log(1/t)).
\tag{HT19}
\]
The physical baseline is \((m-1)\pi\), not \(\pi\), in the second
line. The outer error is explicitly the sum of HT15's bounds.
For a double this sharpens Note 21's polynomial lower witness to the
actual conditional theta statement
\[
R_{r\sqrt{2t}}(t)=\pi r^2+O(\sqrt t\log(1/t)).
\tag{HT20}
\]

For bounded nonnegative schedules \(r(t)=\eta(t)/\sqrt{2t}\), the
uniform estimate and the positive \(r^2\) coefficient imply
\[
R_\eta^{(i)}(t)\longrightarrow0
\quad\Longleftrightarrow\quad r(t)\longrightarrow0.
\tag{HT21}
\]
The same equivalence holds for the outer cap. Thus fixed positive heat-scale
thickness retains a nonzero trace payment, while thinner tubes recover
the cap. Their vanishing thickness does not provide a nonzero contour
extension through the original event. Unbounded \(r(t)\), a uniform
height/multiplicity limit, and differentiated endpoint error estimates
are outside this theorem.

## 6. What the selected HMC-05 comparison decides

The estimating class tested here retains only the leading profile at a
fixed multiplicity and the bounded heat-scale tube parameter, or a finite
collection/continuous functional of those profiles. In this class the
data are exactly \(\Gamma_{m,i}\) and HT18. They have no dependence
on the source beyond the heat equation and the assumed multiplicity.
Consequently equal-multiplicity comparison models have identical leading
data; a rule using only those data cannot distinguish them.

This is a **scoped obstruction to a leading-profile discriminator**.
It is not an impossibility theorem for an arithmetic bound below the
conditional profile. Such an independently proved bound for the original
theta source would exclude the assumed event; it is precisely additional
information absent from this argument. The finite error HT15 is a useful
coherent payment, but not that separating estimate.

| Control | Response to this comparison | Premise not shared with the original theta application |
| --- | --- | --- |
| Exact Hermite heat polynomial of degree \(m\), translated to positive height | Same \(\Gamma_{m,i}\), with zero normal-form error; all birth roots retained | No complete theta source or infinite spectrum; analytic constants replace HT2 |
| Positive atomic \(1+e^t\cos z\) | Double at \((0,\pi)\), all-real positive-time slices, same limit \(\pi(1+r^2)\) | Not the normalized theta expansion; its own source moments are finite |
| Euler-factor control with \(c=1\), under RH | An exact double away from original roots has the same double profile and phase measure | Changed completion and coefficients; choose an exact-double point, or use its actual higher multiplicity |
| Close positive endpoint controls of [Note 05][n05], under RH | Exact added doubles, all-real later slices, same profile; complete majorant moments can be arbitrarily close multiplicatively to theta's | Original ordinary Dirichlet arithmetic fails; the event coefficient and error constants are not asserted uniformly close |
| Weighted-square and finite-prime controls | The local analytic version of HT15 gives the same profile at their actual events, with its own constants | No all-real heat slice: HT5's complete-root bound is unavailable; original normalized theta coefficients also fail |
| Reflected and positive-primitive controls | The local analytic version applies at their events; no all-real-product application is assumed | No original normalized integer-square expansion; their local data alone do not distinguish theta |

These rows show why the profile, including its
improved treatment of the singular physical denominator, is not a
separating arithmetic gain. The close-source control's pointwise bound
\(|\widetilde\Phi/\Phi-1|\le\varepsilon_{b,c}\) implies
\((1-\varepsilon_{b,c})M\le\widetilde M\le
(1+\varepsilon_{b,c})M\) for the complete majorant in HT2.
This does not compare the event-normalizing \(a_m\) or upgrade local
similarity to identical complete arithmetic.

**Decision:** stop treating the leading heat-scale tube profile or its
generic positivity as the prospective theta discriminator. HMC-05's
first comparison is complete, with a quantitative error estimate and this
scoped negative result. HMC-05 as a whole remains open; HMC-06 remains
gated. A further comparison must use information beyond these common
leading data, for example a proved signed estimate for the complete
remainder after subtracting \(\pi\Gamma_{m,i}\), retaining its
nonuniversal jet/source dependence. No sign or improved rate for that
remainder has been established here.

## 7. Verification scope

The [standard-library replay][script] checks exact polynomial identities
for the frozen degrees \(2\le m\le8\): heat normalization, individual
profiles modulo \(\operatorname{He}_{m-1}\), the coefficient HT17,
and the independently proved outer formula HT18. It also checks rational
fixtures for the phase-measure change of variables. The [receipt][replay]
records both the script and its existing helper hashes. These checks do
not certify a theta event, numerical error threshold, energy floor or
the universal analytic limits. [Review 21][review] is a same-assistant
self-review. The canonical manuscript is unchanged in this round.

[program]: ../research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md
[progress]: ../research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[n21]: 21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[n19]: 19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[n12]: 12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md
[n05]: 05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[g57]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md
[results]: ../../../../../../../result-summaries/README.md
[heat-summary]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[script]: ../numerics/check_hmc_endpoint_trace_algebra.py
[replay]: ../numerics/HMC_ENDPOINT_TRACE_ALGEBRA_REPLAY_20261021.json
[review]: ../reviews/21_HEAT_SCALE_TRACE_AND_CONTROL_REVIEW_20261021.md
