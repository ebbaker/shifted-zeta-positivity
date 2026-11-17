# VCD-GT-B11 dynamic-input audit

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. The recorded executor dispatch was
**gpt-6.1-sol / ultra**. Independent serving-model and actual effort
attestation were unavailable.

Fixed analytical support for B11. The audit checks a retained term in
the existing broad-window calculation and the scale available from the
existing local modulus. These are quantitative intermediate estimates.
[Results][results] · [Controls12][controls] · [Avoid][avoid] ·
[Classification01][classification] · [Premises02][premises] ·
[Scope07][scope] · [Note39][gt39] · [Audit16][audit16]

## 1. Retaining the conjugate contribution

Use the complete canonical \(H_t\) on \(0\le t\le1/2\), \(H_t\)'s
physical equation \(\partial_tH_t=-H_{zz}\), and the width-one strip.
Use [GT Note38][gt38]'s pair class, with \(T\ge32\), \(L=\log T\),
\(\ell=1/L\), \(\max(2,4\sqrt d)\le a\le L\), \(3\le R\le T/4\).
All zeros and pairs use the occurrence convention of that note.
For an exterior occurrence \(\rho\) of a pair \(P=(c,D)\) write
\(y=\Im\rho\) and \(r=|\rho-c|\). Let \(n_-(t)\) count eligible pairs
with \(S_R<0\), \(n_M(t)\) those with \(M<0\), and \(n_h(t)\) those
with \(\Xi_{a,R}\ge h>0\).

In [TND-O Note21 (16)–(17)][o21] write its spatial weight as \(p_U\),
with plateau \([U,2U]\), and use a fixed even convex \(C^2\) test \(g\)
with \(g(0)=0\). The contribution to the Newman-time derivative of
\(Q_{U,g}=\sum_j p_U(x_j)g(y_j)\) from an unordered active conjugate
pair \(\{x+iy,x-iy\}\), \(y\ne0\), is exactly
\[
 -2K_{p_Ug}=-2p_U(x)\frac{g'(y)-g'(-y)}{2y}
           =-2p_U(x)\frac{g'(y)}{y}.
\]
The horizontal difference is zero and the chord has constant \(x\).
On a simple relevant interval every active nonreal occurrence has one
distinct conjugate with the same weight in the same finite force
cluster. Thus the contribution is \(-p_U(x)g'(y)/y\) per nonreal
occurrence. Discarding the other favorable vertical terms, and keeping
Note21's curvature, horizontal and signed exterior estimates, yields
\[
 Q_{U,g}'(t)+\sum_{j:\,y_j\ne0}p_U(x_j)\frac{g'(y_j)}{y_j}
 \le D_\chi\|g\|_\infty(\log U)^3.
 \tag{1}
\]
There is no quotient at a real zero. Coincident inactive rows are zero.
At a multiple active event the formula is used on its complementary
intervals. Note21 §4, using [Note19 §§2–4][o19], pays the finite event set
in a padded box, continuity of the counted moment and its absolute
continuity. The retained nonnegative sum is locally measurable and
bounded for fixed \(U,g\), because \(g'(y)/y\) is bounded by
\(\|g''\|_\infty\) and the support count is finite. Integrating (1)
therefore requires no root charts at the events and introduces no
endpoint or event term.

For \(g(y)=y^2+(L/a)|y|^3\), \(g\) is \(C^2\) at zero and
\(g'(y)/y=2+3L|y|/a\). This dominates the B10 per-witness incidence
\(5/3+8L|y|/(3a)\). Such a witness is nonreal and has real part in
\(\mathcal B=[T/2,5T/2]\). Sum (1) at \(U=T/2,T,2T\), whose plateaus
cover \(\mathcal B\), including endpoints. The three supports lie in
\([T/4,5T]\). The uniform dyadic density in Note21 (7) and layer cake
give \(\sum |y|^k=O_b(T/L^{k-1})\) on their union for \(k=2,3\),
using scales \(T/4,T/2,T,2T,4T\) and fixed \(0<b<1/2\).
Thus the combined starting moment at any \(\alpha\) is
\(O_b((1+a^{-1})T/L)\). With \(\Delta=\beta-\alpha\),
\[
 \int_\alpha^\beta n_M(t)\,dt\le\int_\alpha^\beta n_-(t)\,dt
 \ \ll_{b,\chi}\ (1+a^{-1})\,T/L+(1+L/a)L^3\Delta .
 \tag{2}
\]
The first inequality uses the positive far terms in GT Note38. This
argument restricts the incidence comparison to plateau-covered zeros.
It imposes the collar anew at each counted slice.

For the transverse exception count, fix a nonreal occurrence with real
part \(u\). At any eligible center where it is an exterior contributor,
\[
 \ell^2\frac{y^2}{r^4}\le \frac{\ell^2}{r^2}
 \le \frac{2\ell^2}{(a\ell)^2+(u-c)^2}.
\]
The centers are separated by at least \(3a\ell/4\). Summing the last
kernel in center shells of width \(a\ell\) bounds the total from this
occurrence by \(C/a^2\): each two-sided shell contains at most four
centers and the resulting \(\sum_{j\ge0}(1+j^2)^{-1}\) converges.
Every contributing occurrence has \(u\in\mathcal B\). The inequality
\(h n_h(t)\le\sum_P\Xi_{a,R}(t,c)\) and (1) with \(g(y)=y^2\) give
\[
 \int_\alpha^\beta n_h(t)\,dt
 \ \ll_{b,\chi}\ \frac{T/L+L^3\Delta}{a^2h}.
 \tag{3}
\]
Each count is measurable by local enumeration of finite multisets, or
by bounded-window sums with the cutoff inequalities defining
membership. The absolutely convergent far sum also gives measurability
for \(M\). The intervals of integration lie in \([0,1/2]\).

For fixed \(a\), fixed \(h\), and a fixed positive duration, (2)–(3)
save \(L^{-2}\) over the \(O(TL)\) height-band scale. At
\(\Delta\asymp\ell^2\) the starting moment still costs \(O(T/L)\),
the same height order as the slice count times that duration. A single
pair lasting that long contributes order \(\ell^2\) to the count
integral. Neither bound resolves one such pair.

## 2. Persistence and the full exterior field

For a general real \(C^2\) test \(f\) supported in \(|x-X|\le1\),
[TND-OC Note17 (2)–(3), §3][oc17] proves the global Lipschitz bound
\[
 \left|\sum_j f(z_j(t))-\sum_j f(z_j(s))\right|
 \le A^2\log^2(2+X)
       (48\|D^2f\|_\infty+124\|\nabla f\|_\infty)|t-s|.
 \tag{4}
\]
The derivative norms are on the width-one strip. The Hessian chord
cancels its mixed terms, and the finite-event joining uses the same
constant on each simple interval. [TND-O Note17][o17] pays opposite
grouping in the distant real force. [Note18][o18] pays the safe-line
bound \(|E_X(z)|\le31A\log(2+X)\) outside the force cluster
\(|\Re\rho-X|\le3\), for \(|x-X|,|y|\le1\).

Given an eligible pair at \(t_0\), freeze its center \(c_0\). Put
\(r_0=a\ell\). Take a nonnegative radial \(C^2\) bump supported in
\(r_0/4<|z-c_0|<r_0\) and equal to one for
\(5r_0/16\le |z-c_0|\le15r_0/16\). Its initial sum is zero and
its derivative norms in (4) are \(O(r_0^{-j})\) for \(j=1,2\).
For \(|t-t_0|\le k_aL^{-4}\) inside the time slab, with \(k_a>0\)
sufficiently small, its sum stays below one. Consequently the entire
plateau contains no root. The argument principle on a fixed circle in
the plateau keeps exactly two occurrences inside. The symmetric
coordinates \(c,D\) there are analytic in time, including at a double,
by fixed-contour moments. The moving center is within \(5r_0/16\)
of \(c_0\), the half-gap is at most \(5r_0/16\), and all exterior
occurrences have \(|\rho-c|\ge10r_0/16\). This continuation guarantees
reduced clearance and a modified half-gap bound. It need not preserve
membership in the original B10 class.

On this tube let \(Q(z)=(z-c)^2-D\), set \(\sigma=(t-t_0)/\ell^2\),
\(w=(z-c(t))/\ell\), \(\delta=D/\ell^2\), and
\(U(\sigma,w)=(H_t/Q)(c(t)+\ell w)\). Write \(b=U_w/U\),
\(w_\pm=\pm\sqrt{\delta}\), \(C=\ell c'(t)\), and
\(K=(b(w_+)-b(w_-))/(w_+-w_-)\) including its derivative value
at a double. [GT Note21 §1][gt21] and [Note24 §1][gt24] give
\(K=-\ell^2 M\). The pair law is
\[
 C=b(w_+)+b(w_-),\qquad
 \partial_\sigma\delta=2+4\delta K .
\]
Dividing the heat equation by \(H_t=Q(H_t/Q)\) and changing to
the moving variables gives the analytic identity
\[
 \frac{U_\sigma}{U}
 =-b_w-b^2+Cb+
   \frac{2Cw+\partial_\sigma\delta-2-4wb}{w^2-\delta}.
 \tag{5}
\]
The apparent poles are removable by the pair law and by analytic
continuation at a double. On \(|w|\le a/2\), the nearest exterior
distance is at least \(a\ell/8\). The safe-line exterior field and the
\(O(L)\) unit-cluster count give \(|b|\ll_a L\). By Cauchy and the
pair law, \(|C|,|K|,|\partial_\sigma\delta|\ll_a L\), and
\(|b_w|\ll_a L\) on \(|w|=7a/16\). There \(|w^2-\delta|\)
is at least \(24a^2/256\). Equation (5) and Cauchy on the interior
circle \(|w|=3a/8\) bound
\(|b_\sigma|=|\partial_w(U_\sigma/U)|\ll_a L^2\).
Finally
\[
 K=\frac1{2\pi i}\oint_{|w|=3a/8}\frac{b(w)}{w^2-\delta}\,dw ,
 \qquad
 \left|\partial_t(\ell^2M)\right|\ll_a L^4 .
 \tag{6}
\]
The contour denominator is at least \(11a^2/256\), so differentiating
the integral costs \(O_a(L^2)\) in \(\sigma\). Exterior
multiplicities, even at exterior collisions, never enter a reciprocal
gap. This modulus and the collar give persistence on time \(L^{-4}\)
for a fixed nonzero normalized sign margin, with the constant
depending on that margin. Time \(L^{-2}\) still requires a stronger
bound and a longer tube.

The same short-tube estimate up to \(O(L^{-1})\) endpoint errors
applies to the full exterior transverse sum. Use a radial smooth
cutoff, zero through \(3r_0/8\) and one from \(r_0/2\) out, and a
horizontal smooth cutoff supported in \(|x-c|\le1\) and one for
\(|x-c|\le1/2\). Multiply these by
\(\ell^2 y^2/|z-c|^4\). The gradient and Hessian are
\(O_a(L)\) and \(O_a(L^2)\). Equation (4) handles each frozen
center, and changing centers costs \(O_a(L^2)|c(t)-c(s)|\)
by the same support count. The pair law gives \(|c'|\ll_a L^2\).
Unit shells bound the omitted horizontal tail by \(O(L^{-1})\).
The original hard radial cutoff can jump at boundary equality. The
reduced cutoff on the paid tube has a strict margin to both the
selected and exterior groups.

## 3. Cross-check of the exact signed evolution

The proposed scalar evolution in the same physical time passes the
finite-to-complete check. Write \(w_j=\rho_j-c\) for exterior marks,
\(m_j=(w_j^2-D)^{-1}\), \(S_p=\sum_j m_j^p\), and \(M=S_1\).
Conjugation makes each \(S_p\) real. For a polynomial with simple roots,
put \(P=\sum_jw_jm_j\), \(V=\sum_jw_jm_j^2\). The center velocity is
\(-2P\). The exterior velocity relative to the center is
\[
 w_j'=4w_jm_j+2P+2\sum_{k\ne j}(w_j-w_k)^{-1}.
\]
Using \(D'=2-4DM\), the derivative of \(M\) is
\[
 (2-4DM)S_2-8(S_2+DS_3)-4PV
 -4\sum_{j<k}\frac{w_jm_j^2-w_km_k^2}{w_j-w_k}.
\]
The pair quotient equals
\(-m_jm_k-(D+w_jw_k)(m_j^2m_k+m_jm_k^2)\).
The final term therefore sums to
\(2(M^2-S_2)+4D(MS_2-S_3)+4(PV-S_2-DS_3)\), giving
\[
 M'=2M^2-12S_2-16DS_3 .
 \tag{7}
\]

For the canonical extension, freeze any \(t_*\) in the pair tube.
Take the polynomial obtained by truncating the opposite-paired
Hadamard product of \(H_{t_*}\) and evolve that polynomial by its
own heat equation locally about \(t_*\). The finite identity at
\(t_*\) extends across repeated roots by time-continuity of
the counted pair contour formulas and Hermite splitting. On the
fixed pair contour the polynomial products and all spatial
derivatives converge locally uniformly to the canonical ones.
Their time derivative at \(t_*\) is minus their second spatial
derivative. The argument-principle moments give convergence of
\(c,D\) and their time derivatives at \(t_*\). For \(M\) the
contour is minus \((2\pi i)^{-1}\oint (H_t'/H_t)/Q\,dz\), since
the deflation term integrates to \(\oint Q'/Q^2\,dz=0\). This
also gives convergence of the time derivative there. The \(S_p\)
are absolutely convergent on the paid collar. This proves (7)
without differentiating an infinite sum of individual velocities
or assuming a common polynomial heat interval. The canonical
even product has no remaining linear exponent. A constant term
in a logarithmic derivative would cancel between an exterior
velocity and the center velocity in the relative equation.

On any independently paid tube with a fixed microscopic exterior
collar and a fixed bound on \(|\delta|\) strictly below the squared
normalized collar, the unit count gives
\(\ell^4|S_2|+\ell^6|S_3|=O(L)\). With \(m=\ell^2 M\), (7) gives
\[
 |m_\sigma-2m^2|\le C L .
\]
For \(B=\sqrt{CL/2}\), the lower barrier from a paid left endpoint
\(\sigma_0\) is \(-B\coth(2B(\sigma-\sigma_0))\). It solves
\(m_\sigma=2m^2-CL\) and diverges to \(-\infty\) at the left
endpoint. Comparison from an interior starting time followed by
a limit proves the bound. At a fixed positive normalized elapsed
time it is \(-O(\sqrt L)\). The forcing uses absolute shell
bounds, and the identity does not impose a favorable sign on
\(S_2,S_3\) for complex marks. The barrier itself assumes the
paid duration.

## 4. Scope of the estimates

The O18–19 modulus for the fixed unsigned \(Q_{X,R}\) costs
\(O(R^{-2}L^2)\), already \(O(L^4)\) per unit physical time at
\(R\asymp\ell\). OC17's full blurred factorial pair estimate costs
\(O(L^5)\) per unit physical time. Its fixed blur and unconditional
counting do not encode a selected exterior witness or a count-two
void. [OG Discussion10 §§3–5][og10] gives the pair normalization
and paid visibility conditions, and retains the all-real scope of
the dissipative estimates it discusses. Equations (1)–(3) instead
use complex-conjugate dissipation in the complete broad-window
balance. They require an actual time trajectory. The time estimate
does not yield a stronger count on an arbitrary slice or a
probability relative to the possibly sparse population of eligible
pairs. The signed pair law also still needs an incoming value.

GT Note39's controls retain their stated scope. Quadratic and quartic
heat controls share local pair evolution, and the quartic in O17
can have unfavorable spatial flux. They lack the canonical
population law. GT Note34's opposite-sign divisors meet the fixed
slice count and moment bounds with enlarged constants and fail the
unchanged theta identity. A common controlled heat interval for
those divisors remains unpaid, and an aggregate allowance is
compatible with either selected sign. The other catalog controls
retain the premise failures in GT Notes37–39. In particular the
changed observation kernel lacks the physical cosine heat equation,
and fractionally weighted occurrences lack the integer divisor
required by the incidence argument. No canonical sharpness of
the modulus in (6) is inferred from the instantaneous snapshot
controls in O18.

[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[gt21]: ../notes/21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md
[gt24]: ../notes/24_VCD_GT_FOURIER_GROUPING_AND_DEFLATED_CURVATURE_20261116.md
[gt38]: ../notes/38_VCD_GT_E19_ISOLATED_PAIR_EXCEPTION_COUNT_20261117.md
[gt39]: ../notes/39_VCD_GT_B09_B10_SOURCE_ESTIMATE_SYNTHESIS_20261117.md
[audit16]: 16_VCD_GT_B09_PREDECESSOR_RATE_AUDIT_20261117.md
[o17]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/17_TND_O_E08_LOCALIZED_TRANSVERSE_CALCULUS_20261107.md
[o18]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md
[o19]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md
[o21]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[oc17]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/17_TND_OC_E10_R1_FULL_MARKED_PAIR_EVOLUTION_PROOF_20261108.md
[og10]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/01_green_potential_resolvent/brainstorm/notes/10_TND_OG_COLLISION_DYNAMICS_AND_PARALLEL_PROBES_20261108.md
