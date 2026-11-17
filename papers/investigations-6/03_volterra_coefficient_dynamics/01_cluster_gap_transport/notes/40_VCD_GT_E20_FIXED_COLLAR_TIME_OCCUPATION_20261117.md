# VCD-GT-E20 r1 — Fixed-collar negative-pair time occupation

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded executor dispatch
**gpt-6.1-sol / ultra**. Independent serving-model and actual effort
metadata were unavailable.

**Proved in-note, pending separate internal assessment.** This is the
type E execution of [frozen E20 r1][request] and [Decision19 §2][decision].
All six frozen input hashes matched. The estimate is a quantitative
intermediate bound for the prescribed class of isolated pairs.
[Result index][results] · [Cluster18][cluster] · [Controls12][controls] ·
[Avoid index][avoid] · [Classification01][classification] ·
[Premises02][premises] · [Scope07][scope] · [Joint estimates12][joint] ·
[Predecessor reuse15][reuse]

## 1. Complete-field identity and boundary payments

Use the complete canonical \(H_t\) for \(0\le t\le 1/2\),
\(\partial_t H_t=-H_{zz}\), with zero occurrences \(z_j=x_j+iy_j\)
in \(|y_j|\le1\). Let \(A\) be the common constant for the unit
zero count and the upper safe-line logarithmic derivative in
[TND-O Note21 (2)][o21]. At a fixed \(U\ge 8\), write \(L_U=\log U\)
and use its exact spatial profile and force cluster
\[
 a_U(x)=\chi((x-3U/2)/U),\qquad
 \mathcal C_U=\{j:U/4\le x_j\le11U/4\}.
\]
Here \(0\le\chi\le1\), with compact \(C^2\) support in \([-1,1]\)
and value one on \([-1/2,1/2]\). Thus \(a_U\) is supported in
\([U/2,5U/2]\) and equals one on \([U,2U]\). For fixed even convex
\(g\in C^2([-1,1])\) with \(g(0)=0\), put \(G=\|g\|_\infty\) and
\[
 Q_{U,g}(t)=\sum_j a_U(x_j)g(y_j),\qquad
 \mathcal D_{U,g}(t)=\sum_{j:y_j\ne0}a_U(x_j)\frac{g'(y_j)}{y_j}.
 \tag{1}
\]
Evenness and convexity give \(g'(0)=0\), \(g\ge0\), and
\(g'(y)y\ge0\).

For \(z=x+iy\) in the support strip let \(w=x+4i\) and
\(F_t(z)=H'_t(z)/H_t(z)\). The exterior field is
\[
 E_U(z)=F_t(w)-\sum_{k\in\mathcal C_U}(w-z_k)^{-1}
       +\sum_{k\notin\mathcal C_U}
               \big[(z-z_k)^{-1}-(w-z_k)^{-1}\big].
 \tag{2}
\]
The complete \(F_t(w)\) retains the opposite-paired Hadamard
convention. Cluster removal is finite. For \(u=x_k\) outside
the cluster, \(|x-u|\ge U/4\ge2\) and the difference in (2) is
bounded in modulus by \(5|x-u|^{-2}\). The two unit intervals in a
shell \(h\le |x-u|<h+1\) cost at most
\(2A[\log(2+x)+\log(h+2)]\). Since \(\log(2+x)\le2L_U\), truncating
the difference series at \(|x-u|<m\) for integer \(m\ge2\) leaves at
most
\[
 \frac{10A}{m-1}\big[2L_U+\log(m+1)+1\big].
 \tag{3}
\]
This follows by integration of the decreasing shell majorant and
tends to zero uniformly in the active strip and physical time for
fixed \(U\). Using \(\lfloor U/4\rfloor-1\ge U/16\) gives a total
difference-series bound \(640A L_U/U\). The finite safe-line cluster
sum is at most \(12A L_U^2\), from shells of at most \(4A L_U\)
occurrences with denominator at least \(\sqrt{h^2+9}\), and
\(|F_t(w)|\le2A L_U\). These are the unchanged accepted
[TND-O Note21 (9)–(15)][o21] and [Assessment07 §5][assess]
payments. They give
\[
 \#\mathcal C_U\le 6A U L_U,\qquad |E_U(z)|\le 100 A L_U^2.
 \tag{4}
\]
The first bound covers the cluster's length \(5U/2\) with at most
\(3U\) closed unit intervals. Equations (2)–(3) keep zeros at all
heights, including the negative-height tail. In the full paired
product start with opposite-paired cutoffs containing the cluster.
Evaluate at \(w\), remove the cluster, and pass to the absolute
difference series. The exterior field retains the full pairing
convention even when the removed cluster is nonsymmetric.

For two distinct cluster endpoints \(z_j,z_k\), set
\(p=x_j-x_k\), \(q=y_j-y_k\), and let \((x_s,y_s)\) be their
straight chord parametrized on \([0,1]\). The physical Newman-time
velocity at a simple zero is \(H_{zz}/H_z\), obtained by
differentiating \(H_t(z_j(t))=0\).
Its complete force is twice the sum of the other reciprocals, with
(2) for the exterior part. For \(f(x,y)=a_U(x)g(y)\), symmetrizing
interior forces pairs the gradient differences against
\(p/(p^2+q^2)\) horizontally and \(-q/(p^2+q^2)\) vertically.
Integrating the gradient difference along the chord cancels the mixed
Hessian terms. In the sign convention of [TND-O Note21 (16)–(17)][o21],
\[
 \begin{aligned}
 K(z_j,z_k)&=\int_0^1
    \frac{a_U(x_s)g''(y_s)q^2-a_U''(x_s)g(y_s)p^2}{p^2+q^2}\,ds,\\
 Q_{U,g}'&=-2\sum_{j<k\in\mathcal C_U}K(z_j,z_k)
   +2\sum_{j\ {\rm in\ support}}
       \big[a_U'(x_j)g(y_j)\Re E_U(z_j)
            +a_U(x_j)g'(y_j)\Im E_U(z_j)\big].
 \end{aligned}
 \tag{5}
\]
Use (5) whenever the roots in the support are simple. Repeated
inactive occurrences have zero endpoint gradients, so their
coincident inactive pair kernel is zero. The cluster serves only to
partition the force at a given time.

## 2. Retention and finite-event assembly

For each contributing unordered conjugate pair \(x\pm iy\), \(y\ne0\),
both occurrences are in the cluster and the chord has constant \(x\).
Its complete kernel is vertical and equals
\[
 K=a_U(x)\,\frac{g'(y)-g'(-y)}{2y}
   =a_U(x)\frac{g'(y)}{y}.
\]
On simple relevant-root intervals each nonreal contributing occurrence
belongs to exactly one such pair. Its pair contributes \(-2K\) in (5),
which is the negative of the two terms of (1). Real occurrences make
zero contribution to \(\mathcal D_{U,g}\) by definition. They have
no nonreal conjugate partner, so the limit \(g''(0)\) has no role.

The remaining interior vertical chord terms have
\(a_U(x_s)g''(y_s)q^2\ge0\), hence a nonpositive contribution to
\(Q'\). The exterior imaginary sum is absolutely convergent, with
term magnitudes at most \(2|x-u|^{-2}\). It is the imaginary part
of (2), by the same full-field passage. The exterior is conjugation
invariant. With \(s=x-u\), the negative imaginary part of the two
reciprocals at \(u\pm iv\) is
\[
 \frac{2y(s^2+y^2-v^2)}
      {[s^2+(y-v)^2][s^2+(y+v)^2]}.
\]
The factor \(s^2+y^2-v^2\) is positive since \(|s|\ge U/4\ge2\)
and \(|v|\le1\). The corresponding real-root expression
\(y/(s^2+y^2)\) also has the sign of \(y\). Conjugate grouping
therefore gives \(a_U(x)g'(y)\Im E_U(z)\le0\). The absolute scope
of this grouping is the imaginary field. The horizontal field
uses (2) with opposite pairing.

The interior horizontal cost is at most
\(\|a_U''\|_\infty G(\#\mathcal C_U)^2\), since the factor two in
(5) multiplies at most half the ordered-pair count. The exterior
horizontal cost is at most
\(2\|a_U'\|_\infty G(6AUL_U)(100A L_U^2)\).
These are \(36 A^2\|\chi''\|_\infty G L_U^2\) and
\(1200 A^2\|\chi'\|_\infty G L_U^3\) respectively. Since \(L_U\ge1\),
\[
 Q'_{U,g}+\mathcal D_{U,g}
 \le D_\chi G L_U^3,\qquad
 D_\chi=A^2(36\|\chi''\|_\infty+1200\|\chi'\|_\infty).
 \tag{6}
\]

For fixed \(U,g\), choose local zero-free-boundary rectangles with a
collar around the support. Analyticity and Rouché continuity of the
finite root multisets give continuity of \(Q_{U,g}\), including
support crossings and time endpoints. The multiple-root locus in the
closed padded box \([U/2-1,5U/2+1]\times[-2,2]\) over the closed
time slab is compact. At each multiple root of multiplicity \(m\),
[TND-O Note19 §§2–4][o19] supplies the local Hermite splitting
\(z_j(t_0+s)=z_0+\sqrt{2s}\,h_j+O(|s|)\), with \(m\) distinct
\(h_j\) and an isolating disk exhausting those \(m\) occurrences.
The leading separations dominate the errors for sufficiently small
nonzero \(|s|\) on either available side. Thus each multiple point
is isolated in space and time and compactness gives finitely many
points, hence finitely many event times. The closed box and inward
time neighborhoods also cover boundary events.

On the complementary intervals the absolute chord kernel is bounded by
\(\max\{\|a_U\|_\infty\|g''\|_\infty,\|a_U''\|_\infty G\}\).
The active gradient is bounded by
\(\|a_U'\|_\infty G+\|a_U\|_\infty\|g'\|_\infty\). Together with
(4) this gives a finite common two-sided derivative bound for fixed
\(U,g\). Continuity joins it across the finite partition, giving
absolute continuity on the full slab. The summand in
\(\mathcal D_{U,g}\), defined to be zero at real roots, is Borel
under local root enumeration and bounded by \(\|g''\|_\infty\).
The population bound (4) makes its sum bounded and integrable.
Its possible jumps, for instance at real collisions, are harmless.
Integrating (6) and joining across the finite event partition yields
\[
 \boxed{
 Q_{U,g}(\beta)+\int_\alpha^\beta\mathcal D_{U,g}(t)\,dt
 \le Q_{U,g}(\alpha)+D_\chi G(\beta-\alpha)(\log U)^3
 }\qquad (0\le\alpha\le\beta\le1/2).
 \tag{7}
\]
The derivative of \(Q_{U,g}\) has an integrable density, so there
are no collision atoms. The auxiliary bounds on test derivatives
are used for assembly and do not enter (7).

## 3. Fixed test, support cover and initial allowance

Take \(T\ge64\), \(L=\log T\), \(\ell=1/L\), \(d\ge0\),
\(\max(2,4\sqrt d)\le a\le L\), \(3\le R\le T/4\), and fix
\(r_0=a/L\) throughout the height and time intervals. Use
\[
 g(y)=\frac{y^2}{2}+\frac{|y|^3}{3r_0},\qquad
 \frac{g'(y)}{y}=1+\frac{|y|}{r_0}\quad(y\ne0),\qquad
 G=\frac12+\frac{L}{3a}.
 \tag{8}
\]
The test is even \(C^2\), with \(g''(y)=1+2|y|/r_0\), hence convex.
The three profiles \(U=T/2,T,2T\) have plateaus \([T/2,T]\),
\([T,2T]\), and \([2T,4T]\). Their sum \(A_T\) is at least one
on \(\mathcal B_T=[T/2,5T/2]\), is bounded above by three, and
has support in \([T/4,5T]\). Write \(Q_A=\sum_U Q_{U,g}\) and
\(\mathcal D_A=\sum_U\mathcal D_{U,g}\) over these three profiles.

Fix one \(0<b<1/2\). The uniform canonical exponential transverse
density in [TND-O Note21 (7), (25)][o21] and [Assessment07 §5][assess]
bounds the occurrence count \(N_t(U,v)=\#\{j:U\le x_j\le2U,\
|y_j|>v\}\) by \(B_b U\log U\exp(-bv\log U)\) for \(U\ge8\) and
\(0<v<1\). Layer cake gives, for \(k=2,3\),
\[
 \sum_{U\le x_j\le 2U}|y_j|^k
 =k\int_0^1 v^{k-1}N_t(U,v)\,dv
 \le \frac{k!\,B_b}{b^k}\frac{U}{(\log U)^{k-1}}.
 \tag{9}
\]
The upper integral follows by extending the exponential majorant to
infinity. The formula counts multiplicities, gives zero for real
occurrences and includes \(|y_j|=1\) by thresholds below one.

The five closed bands \([U,2U]\) with
\(U=T/4,T/2,T,2T,4T\) cover \([T/4,5T]\); their union ends at
\(8T\) and shared endpoints may overcount. Each scale is at least
\(16\ge8\) and \(\log U\ge L-\log4\ge (2/3)L\), since
\(L\ge6\log2\). Their scales sum to \(31T/4\).
Consequently the sums on the support of \(A_T\) are bounded by
\(93B_bT/(4b^2 L)\) for \(k=2\) and
\(837B_bT/(8b^3 L^2)\) for \(k=3\).
Multiplying by the coefficients \(3/2\) and \(3/(3r_0)=L/a\),
which pay the overlap factor three, gives
\[
 Q_A(\alpha)\le\frac{B_b}{8}
       \left(\frac{279}{b^2}+\frac{837}{ab^3}\right)\frac{T}{L}.
 \tag{10}
\]
For the three profile scales the exact sum of log cubes is
\(3L^3+6L(\log2)^2\le (19/6)L^3\le4L^3\).
Summing (7) with \(\tau=\beta-\alpha\) and using \(Q_A(\beta)\ge0\)
bounds \(\int_\alpha^\beta\mathcal D_A(t)\,dt\) by (10) plus
\(4D_\chi G\tau L^3\).

## 4. Negative-pair occupation and comparison with the slice bound

Use the [E19 §1][e19] slice class of unordered
conjugation-invariant pairs of occurrences \(\{z_-,z_+\}\) with
\[
 c=(z_-+z_+)/2\in[T,2T],\qquad
 D=(z_+-z_-)^2/4\in\mathbb R,\qquad |D|\le d\ell^2,\qquad
 |\rho-c|\ge r_0\quad\text{for every exterior occurrence}.
 \tag{11}
\]
The two selected occurrences lie within \(r_0/4\) of \(c\).
Count two and the exterior collar are independently paid at the
slice in question. A double counts as one unordered pair. The
class includes \(D<0\), \(D>0\) and \(D=0\). With \(w=\rho-c\),
\(S_R\) sums \(\Re[(w^2-D)^{-1}]\) over exterior occurrences with
\(|\Re w|\le R\), and \(M\) is the complete exterior sum.
Let \(N_-(t)\) and \(N_M(t)\) count qualifying pairs with
\(S_R<0\) and \(M<0\), respectively.

By the [E19 incidence bound][e19], qualifying centers have
separation at least \(3r_0/4\) and a negative summand must have
\(|y|>2r_0/3\), since \(y^2>(|w|^2-D)/2\ge (15/32)r_0^2\).
Its real part \(u\) lies in \(\mathcal B_T\) by the cutoff \(R\).
For that occurrence the eligible centers contributing such a
negative summand all lie within \(|y|+r_0/4\) of \(u\). Packing
this interval gives at most \(5/3+8|y|/(3r_0)\) centers per
occurrence. Each pair with \(S_R<0\) has at least one such occurrence.
Using \(A_T\ge1\) on \(\mathcal B_T\), nonnegativity of the
dissipation and (8) gives
\[
 N_-(t)\le\sum_{\substack{x_j\in\mathcal B_T\\|y_j|>2r_0/3}}
               \left(\frac53+\frac{8|y_j|}{3r_0}\right)
       \le \frac83\mathcal D_A(t).
 \tag{12}
\]
The full sum defining \(M\) is absolutely convergent by unit-shell
counts and the reciprocal-square tail. In the collar,
\(|w^2-D|\ge (15/16)|w|^2\). The omitted terms \(|\Re w|>R\)
have \((\Re w)^2-(\Im w)^2-D>0\) by \(R\ge3\), the width-one
strip and \(|D|\le1/16\). Hence \(M\ge S_R\) and \(N_M\le N_-\).

The two counts are measurable. The target, its collar and all
\(S_R\) summands are determined inside the padded band around
\(\mathcal B_T\). Off its finite multiple-event time set one can use
local simple root charts and the finite collection of unordered
pairs. Their coordinate constraints, collar and cutoffs are Borel.
At exceptional times the counts are defined directly on the
multiset. For \(M\), enlarge the enumerated band in integer steps
and use the uniform reciprocal-square tail for \(c\in[T,2T]\) and
the paid collar. This gives \(M\) as a limit of measurable truncated
sums on the qualifying pairs. The charts serve only to verify
measurability. Pair membership is tested afresh at each time.

Combining (10)–(12) yields the fixed bound
\[
 \boxed{\begin{aligned}
 \int_\alpha^\beta N_M(t)\,dt
 &\le\int_\alpha^\beta N_-(t)\,dt\\
 &\le B_b\left(\frac{93}{b^2}+\frac{279}{ab^3}\right)\frac{T}{L}
       +\frac{32}{3}D_\chi
          \left(\frac12+\frac{L}{3a}\right)\tau L^3 .
 \end{aligned}}
 \tag{13}
\]
Intersect the right side with the [E19 (5), (7)][e19] bounds
\[
 C_b\tau T L e^{-2ba/3},\qquad
 \tau\left(1+\frac{4TL}{3a}\right),
 \qquad C_b=5B_b\left(\frac{31}{9}+\frac4{3b}\right).
 \tag{14}
\]
The sharper slice coefficient \(5B_b(31/9+8/(3ab))\) is also valid.
The zero-duration case has zero integral.

For fixed \(a,b\) and fixed positive \(\tau\), (13) gives
\[
 \frac{1}{TL}\int_\alpha^\beta N_-(t)\,dt
 =O_{a,b}(L^{-2})+O_{a,\chi}(L^3/T),
 \tag{15}
\]
where the time-cost term after division is bounded using
\(\tau\le1/2\), and the inherited source constants are fixed.
For general \(\tau>0\) the corresponding averaged allowance is
\[
 \frac{1}{\tau TL}\int_\alpha^\beta N_-(t)\,dt
 \le\min\left\{C_{a,b},\
      \frac{C_{a,b}}{\tau L^2}+\frac{C_{a,\chi}L^3}{T}\right\}
 \tag{16}
\]
with the packing bound in (14) available as well. The same rates
hold for \(N_M\). When \(\tau\asymp\ell^2\), the starting-moment
allowance after dividing by \(\tau\) is of order \(TL\).
A vanishing normalized averaged allowance from (13) at fixed
\(a,b\) uses \(\tau L^2\to\infty\). This is a comparison of upper
allowances. The theorem bounds pair-time occupation, with changes in
slice membership allowed. Event counts, counts of distinct
trajectories, fractions of eligible pairs, pointwise sign and incoming
pair data lie outside its conclusion.
Any conversion to the number of selected pairs at a snapshot would
require a common interval of independently paid eligibility and
negative visibility. A tube that preserves eligibility alone does not
pay that visibility.

The direct evaluator gets the same complete-source density, common
heat identity, full boundary field, count-two geometry, collar and
signed interaction. It can obtain (13)–(16) by the same retention.
Using only the slice consequence of those data and integrating it gives
(14) and the fixed-duration \(O(1)\) normalized allowance. The gain
comes from the common-time inequality. No evaluator-specific
information or computational advantage is needed.

## 5. Premise screen

The following replay uses [Decision19 §4][decision], [Synthesis39 §4][s39]
and the [collision-control register][controls]. The dissipative sign is
structural. Canonical input pays the uniform moments, strip and
complete-field allowances.

| Control | Failed or untested premise |
| --- | --- |
| Quadratic and even quartic heat controls | Can share the heat equation and local or dissipative identities. Their finite divisors miss the canonical growing count law. An upper occupation bound can hold for a finite control. |
| Euler-factor translates | Positive-source heat evolution survives, but the complete theta source changes and the documented canonical endpoint discrepancy fails. Transfer of the canonical density and moment bound is unproved. |
| Weighted-square, finite-source, finite-score and finite-prime controls | Full reflected unit-weight theta equality fails. The documented endpoint-defective classes also fail the width-one strip. Finite calibration supplies neither uniform density nor the safe-line bound. |
| Reflected super-Gaussian | Shares reflection and heat evolution. The documented source fails order at most one, and canonical complete count, resolvent and moment bounds are unassigned. |
| Smooth shape and positive-primitive controls | Change the arithmetic. Transfer of canonical strip, count and transverse density is untested. |
| Fixed-event atomic and compact-profile controls | Full theta equality fails. The at-most-linear count of the finite-type classes misses the canonical growing main term. |
| RH-conditional endpoint mergers | Retain the RH assumption with changed ordinary Dirichlet arithmetic. Complete uniform count and moment transfer is untested. A double is within (11) if its independent collar is paid. |
| Varied observation kernels and fractional-profile relaxation | The varied kernel lacks the physical cosine/Newman readout and the fractional profile lacks the complete integer divisor. The full-field calculation or the pair incidence cannot be imported on those premises. |
| Note34 identical-count opposite-sign controls | Share the slice geometry, count and moment/density upper-bound forms with enlarged constants. They change the theta source and supply no common physical heat-time family. The slice data do not pay (7). |

In particular [Note34][n34] and [E19 §5][e19] give the last row at
\(T=c\ge64\), \(a=2\), \(d=D=0\), \(R=3\). The closed near cut
includes only the two inserted exterior occurrences at
\(c+2/\log c\), giving \(\ell^2S_R=1/2\) and \(-1/16\) exactly.
The complete \(\ell^2M\) tends to those values with a nonnegative
far correction of order \(O(1/\log c)\). The added conjugate pair
in the latter slice has marks \(2\sqrt3/\log c\) and bounded scaled
transverse height on each dyadic band it enters. The uniform
exponential-density upper-bound form from E19 with its enlarged
constant then also pays the second and third moments by (9).
No controlled evolution over a common time interval is supplied by
these fixed-slice examples. Their signs are compatible with an upper
occupation estimate that permits an isolated adverse slice.

[request]: ../research-progress/handoffs/VCD-GT-E20-r1.md
[decision]: ../brainstorm/notes/19_VCD_GT_B11_FIXED_COLLAR_DECISION_20261117.md
[e19]: 38_VCD_GT_E19_ISOLATED_PAIR_EXCEPTION_COUNT_20261117.md
[s39]: 39_VCD_GT_B09_B10_SOURCE_ESTIMATE_SYNTHESIS_20261117.md
[n34]: 34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md
[o21]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[o19]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md
[assess]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
[results]: ../../../../../result-summaries/README.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[reuse]: ../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md
