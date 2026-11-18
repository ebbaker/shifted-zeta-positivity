# VCD-GT-CM-E02 r1 — Complete local complex-power time law

17 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. Requested helper dispatch **gpt-6.1-sol /
ultra**. Independent actual serving model and reasoning effort metadata
were unavailable.

**Proved in-note on the frozen paid tube, pending E04 assessment.**
All five input pins in the [E02 request][request] match. The chart law
is a representation. The uniform complete-divisor and safe-line tail
bounds are intermediate estimates under [Classification01][class].
The [result index][results], [Cluster18][cluster] and [avoid index][avoid]
give the surrounding evidence. [B01 §2][decision] · [E01 audit][audit] ·
[Parent Note41][n41] · [GR E03][gr03] · [GR E05][gr05]

## 1. Domain and logarithms

Work on the compact independently paid count-two real tube
\(I\subset[0,1/2]\) for the complete canonical theta field with
\(H_t=-H_{zz}\). Freeze \(T\ge64\), \(L=\log T\), \(\ell=1/L\),
\(r_0=a\ell\) with \(\max(2,4\sqrt d)\le a\le L\). The counted target
occurrences are \(c\pm\sqrt D\), \(c\in[T,2T]\), with
\(|D|\le d\ell^2\le r_0^2/16\). Put
\[
 w_j=\rho_j-c,\quad x_j=\Re w_j,\quad Q(t,w)=w^2-D(t),\quad
 a_j=Q(t,w_j),\quad \mu_j=\ell^2/a_j,\quad q_0=16/15 .
\]
The exterior occurrences have \(|w_j|\ge r_0\),
\(|\Im w_j|\le1\), and \(|a_j|\ge q_0^{-1}|w_j|^2\). Thus
\(|\mu_j|\le q_0/a^2<1\). Count all multiplicities. The symmetric
coordinates \(c,D\) are locally analytic by the inherited fixed physical
pair contour; both signs of \(D\) and \(D=0\) are allowed. Let
\(C_{\rm u}\ge1\) be the common unit-count and safe-line constant in
[Parent Note41 §1][n41] and [the inherited safe-line input][safe].
In particular
\[
 \#\{\rho:v\le\Re\rho\le v+1\}\le C_{\rm u}\log(2+|v|),\qquad
 \left|\frac{H_z}{H}(t,v\pm4i)\right|\le C_{\rm u}\log(2+|v|).
\]

At a reference time \(t_*\), choose the two centered cuts
\(R_+\in[6,7]\), \(-R_-\in[-7,-6]\) independently. In a physical unit
window \([U,U+1]\), the projections in \([U-1,U+2]\) number at most
\(N_U=3C_{\rm u}\log(4+|U|)\). Deleting intervals of radius
\(\epsilon_U=1/[4(1+N_U)]\) around those projections loses at most
\(1/2\) of the unit window. Projections outside the enlarged window
are at distance at least one. Apply this in the translates of the
two centered windows by \(c(t_*)\). The resulting finite connectors
\(|\Im w|\le4\) are zero-free at \(t_*\) and remain zero-free on a
sufficiently small relative time neighborhood, by continuity and
compactness.

On both closed half-strips outside the cuts and \(|\Im w|\le4\),
\[
 \Re Q\ge x^2-16-1/16\ge x^2/2,\qquad x=\Re w .
 \tag{1}
\]
Use the principal \(\log Q\), defined on a neighborhood of each
half-strip. Its argument is bounded by \(\pi/2\) in modulus. Inside
the central rectangle, enclose each distinct reference exterior
location in its own small disk, with zero-free circle \(\gamma_j\).
Choose pairwise disjoint closed disks in the rectangle away from the
selected pair and \(Q=0\). The target circle \(|w|=r_0/2\) can be
kept disjoint from these disks. The count in the central rectangle,
the two target occurrences and the counts in the exterior circles
remain constant on a smaller time neighborhood. This follows from
the zero-free boundaries, the argument principle and continuity,
and ensures that every central exterior occurrence is accounted for.

For a disk with reference center \(w_*\), put \(Q_*=Q(t_*,w_*)\).
Choose \(\theta_*\in[-\pi,\pi]\) representing its argument, using
either endpoint for a negative-real \(Q_*\). Shrink the spatial
disk and time neighborhood until
\(\lvert Q(t,w)/Q_*-1\rvert<1/2\) on a neighborhood of the closed disk.
There use
\[
 L_j(t,w)=\log|Q_*|+i\theta_*+
                       \log_{\rm pr}(Q(t,w)/Q_*).
 \tag{2}
\]
This one logarithm follows every occurrence inside the disk, including
through their mergers. Its argument has modulus at most
\(\Theta=3\pi/2\), since \(Q/Q_*\) has positive real part. The same cap
works in every chart after this shrinking and allows either negative-axis
boundary value at the reference point. There is no assumption of a
uniform chart width as \(T\) varies. The construction gives a finite
cover of \(I\) by relative open charts, which may be chosen with smaller
closed subintervals still covering \(I\). These logarithms and cuts
define the local \(Z\):
\[
 f_p(t,w)=\exp\!\big(p(2\log\ell-\log Q(t,w))\big),\qquad
 Z(p,t)=\sum_j f_p(t,w_j).
 \tag{3}
\]
In (3) and every spatial integral, the \(\log Q\) on a given part is
that part's specified logarithm.

## 2. Complete value and cutoff bounds

Let \(p=u+iv\), \(u>1/2\), and
\(\Lambda(s)=\log(3+2T+|s|)\). A horizontal shell
\(n\le|x_j|<n+1\), \(n\ge1\), has at most \(2C_{\rm u}\Lambda(n)\)
occurrences. The near shell \(|x_j|<1\) has at most \(4C_{\rm u}L\).
For \(k=1,2\) and \(\gamma>0\) put
\[
 E_k(\gamma)=\sum_{j\ge0}2^{-j\gamma}(1+(j+1)\log 2)^k .
\]
For each integer \(m\ge1\), dyadic blocks give
\[
 \sum_{n\ge m} n^{-2u}\Lambda(n)
 \le E_1(2u-1)m^{1-2u}\Lambda(m).
 \tag{4}
\]
Indeed the block \([2^j m,2^{j+1}m)\) has \(2^j m\) integers and
\(\Lambda(2^{j+1}m)\le\Lambda(m)+(j+1)\log2\), while
\(\Lambda(m)\ge1\). The same block-length argument gives
\[
 \int_X^\infty x^{-2u}\Lambda(x)^k\,dx
 \le E_k(2u-1) X^{1-2u}\Lambda(X)^k\quad (X\ge1).
 \tag{5}
\]
The branch weight is exactly \(|\mu_j|^u e^{v\Im\log Q(t,w_j)}\).
It follows that for each chart, with bounds uniform in its time,
\[
 \begin{aligned}
 |Z(u+iv,t)|
 &\le e^{\Theta|v|}\mathcal A_u(t),\qquad
       \mathcal A_u(t)=\sum_j|\mu_j|^u,\\
 \mathcal A_u(t)
 &\le 4C_{\rm u}L(q_0/a^2)^u+
     2C_{\rm u}(\ell^2q_0)^u E_1(2u-1)\Lambda(1),\\
 \mathcal A_u(t)&\le(q_0/a^2)^{u-b}\mathcal A_b(t)
                              \qquad(u\ge b>1/2).
 \end{aligned}                                                 \tag{6}
\]
For a canonical modulus cutoff let \(Z_N\) include \(|\rho_j|\le N\)
with all tied occurrences included. Take an integer \(N>4T+8\).
Every omission has \(|x_j|>N-1-2T>N/2\), by the strip and the center
bound. Thus the omitted denominators are on the principal tails.
For \(1/2<b\le u\le r<\infty\), (4) at \(m=\lfloor N/2\rfloor\ge N/3\)
gives uniformly over all charts
\[
 |Z-Z_N|\le
 2 C_{\rm u}(\ell^2 q_0)^u e^{\pi|v|/2}
 E_1(2b-1) 3^{2r-1} N^{1-2u}\Lambda(N).
 \tag{7}
\]
In particular \(\Lambda(N)=O(\log N)\) in this range. For a
centered value cutoff retaining \(|x_j|<N\) with \(N\ge8\) integer,
the same estimate holds with \(3^{2r-1}\) removed, directly using
the shells at \(m=N\). These are value estimates. No derivative is
taken of either cutoff or of root labels. Absolute locally uniform
convergence of the entire-in-\(p\) terms gives slice holomorphy on
\(\Re p>1/2\).

## 3. Spatial contours and physical time

Set \(h(t,w)=(H_z/H)(t,c(t)+w)\) and let \(\mathcal C B\) denote
\(1/(2\pi i)\) times the following sum, with the prescribed branch of
any power substituted on each part:
\[
 \begin{aligned}
 &\sum_j \oint_{\gamma_j} B(w)\,dw\\
 &\quad+\int_{R_+}^{\infty}[B(x-4i)-B(x+4i)]\,dx
       +\int_{R_++4i}^{R_+-4i}B(w)\,dw\\
 &\quad+\int_{-\infty}^{-R_-}[B(x-4i)-B(x+4i)]\,dx
       +\int_{-R_--4i}^{-R_-+4i}B(w)\,dw .
 \end{aligned}                                                 \tag{8}
\]
The circles are counterclockwise. In each tail rectangle the lower
edge goes rightward and the upper edge leftward. The right tail's
finite connector goes down and the left tail's finite connector goes
up. These connectors are part of the value and the derivative law.

For the value law first close each tail in a distant unit window,
using the projection clearance at the chosen slice. The outer right
edge is upward and the outer left edge downward. Since \(h\) has
residue equal to the zero multiplicity and the powers are holomorphic
throughout each enclosed region, these residues give the finite
part of (3) in the two rectangles and all the near circles. Here
the two enclosed half-strip sections and all near circles exclude
the target pair.

To remove the outer edges, let \(v_0\) be a physical cut with
\(|v_0-U|\le1\) and clearance \(\epsilon_U\), and write
\(\lambda=\log(3+|v_0|)\). The once-subtracted canonical product
logarithmic derivative gives
\[
 h(t,v_0-c+iy)-h(t,v_0-c+4i)
 =\sum_\rho\left(\frac1{v_0+iy-\rho}-\frac1{v_0+4i-\rho}\right).
 \tag{9}
\]
This difference is absolutely convergent, with the product
regularizers canceled before summation. At \(|y|\le4\) the near
shell contributes at most \(16C_{\rm u}\lambda/(3\epsilon_U)\).
On shell \(n\ge1\) the denominators have product modulus at least
\(n^2\), and its count is at most
\(2C_{\rm u}(\lambda+\log(n+1))\). Use
\(\sum_{n\ge1}n^{-2}\le2\) and
\(\sum_{n\ge1}n^{-2}\log(n+1)\le3\), as in [Note41 §3][n41].
Since \(1/\epsilon_U\le4+24C_{\rm u}\lambda\), the safe-line
bound and the two shell estimates give
\(|h(t,v_0-c+iy)|\le240C_{\rm u}^2\lambda^2\).
Writing \(x=v_0-c\), the absolute integral before the factor
\(1/(2\pi i)\) on this outer edge is at most
\[
 1920 C_{\rm u}^2(\ell^2\,2)^u e^{\pi|v|/2}
                   |x|^{-2u}\Lambda(x)^2 ,
 \tag{10}
\]
which tends to zero. This needs a sequence of remote cleared cuts
at each single slice. The derivative below uses the limiting
formula at every slice and no motion of these cuts. The horizontal
integrals are absolute by the next estimates, and the omitted
values vanish by (4). Therefore
\[
 Z(p,t)=\mathcal C(f_p h).
 \tag{11}
\]

At every zero-free point of the spatial formula, the centered heat
law and the fixed \(\ell\) give
\[
 h_t=-h_{ww}-2h h_w+c'h_w,\qquad
 (f_p)_t=pD'f_p/Q,\qquad (f_p)_w=-2pw f_p/Q,\qquad
 (f_p)_{ww}=\big[-2p/Q+4p(p+1)w^2/Q^2\big]f_p .
 \tag{12}
\]
The \(t\) derivative here holds \(w\) fixed. Put
\[
 B_p=\big[(f_p)_t-(f_p)_{ww}-c'(f_p)_w\big]h+(f_p)_w h^2,\qquad
 \mathcal P_p=-f_p h_w+(f_p)_w h-f_p h^2+c'f_p h .
 \tag{13}
\]
Then \(\partial_t(f_p h)=B_p+\partial_w\mathcal P_p\). The estimates
below justify differentiation in (11). The last term integrates to
zero on each circle. On each tail the primitive agrees at the two
connector junctions and tends to zero at the ends of the safe lines,
so the integrated endpoint contributions cancel. This proves
\[
 \boxed{\displaystyle
       \partial_t Z(p,t)=\mathcal C\big((f_p)_t h+f_p h_t\big)
                         =\mathcal C B_p .}
 \tag{14}
\]
Both laws retain the complete \(h\), including the full \(h^2\) term.

## 4. Independent bounds for the differentiated spatial integral

The product differentiated in \(w\) gives the absolutely convergent
reciprocal-square and twice reciprocal-cube sums for \(h_w\) and
\(h_{ww}\). On the safe lines the near denominator modulus is at
least \(3\), with count at most \(2C_{\rm u}\log(3+|c+x|)\).
On shell \(n\ge1\) the distance is at least \(n\) and the count
is at most \(2C_{\rm u}(\log(3+|c+x|)+\log(n+1))\). With the same
elementary shell sums as above, both lines satisfy
\[
 |h|,\ |h_w|,\ |h_{ww}|\le A\Lambda(x),\qquad A=24C_{\rm u}.
 \tag{15}
\]
On the full compact tube take \(C_c=\sup_I|c'|\) and
\(C_D=\sup_I|D'|\). These are finite by the inherited pair contour.
Explicit upper choices follow from [Note41 (3)–(4) and §3][n41]:
\(C_c\le16C_{\rm u}L^2/a+190C_{\rm u}L\) and
\(C_D\le2+4d(14C_{\rm u}q_0/a^2)L\). Thus
\[
 |h_t|\le C_h\Lambda(x)^2,\qquad C_h=A(1+C_c)+2A^2.
\]
For \(J=1+|p|\) and \(|x|\ge6\), (1), \(|w|\le2|x|\) and (12) give
\[
 \begin{gathered}
 |f_p|\le (2\ell^2)^u |x|^{-2u}e^{\pi|v|/2},\qquad
 |(f_p)_t|\le 2 C_D J|f_p|/x^2,\\
 |(f_p)_w|\le 8J |f_p|/|x|,\qquad
 |(f_p)_{ww}|\le 68 J^2 |f_p|/x^2 .
 \end{gathered}
\]
In particular \(|f_p h|\le A |f_p|\Lambda(x)\); either integrand in
(14) is bounded by \(C_{\rm sl} J^2 |f_p|\Lambda(x)^2\) with
\[
 C_{\rm sl}=C_h+A(2C_D+68+8C_c)+8A^2 .
\]
The same bounds make \(\mathcal P_p\) vanish at each infinite endpoint.
For \(X\ge7\), truncation of the horizontal rays of (8) beyond
\(|x|=X\), keeping both finite connectors and all circles, therefore
has the errors
\[
 \begin{aligned}
 \big|\mathcal C(f_p h)-\mathcal C^{[X]}(f_p h)\big|
 &\le \frac{2A}{\pi}(2\ell^2)^u e^{\pi|v|/2}
                  E_1(2b-1)X^{1-2u}\Lambda(X),\\
 \big|\mathcal C B_p-\mathcal C^{[X]} B_p\big|
 &\le \frac{2C_{\rm sl}}{\pi}(2\ell^2)^u J^2 e^{\pi|v|/2}
                  E_2(2b-1)X^{1-2u}\Lambda(X)^2 .
 \end{aligned}                                                 \tag{15a}
\]
The second bound also holds with \(\partial_t(f_p h)\) in place of
\(B_p\). The factor \(2/\pi\) counts the four rays and the Cauchy
normalization. The \(\log X,\log^2 X\) forms hold for \(X>4T+8\).
This spatial boundary truncation is separate from the divisor
value cutoff \(N\). It is a bound on the omitted safe-line integrals
in (8), with no new vertical closure imposed at \(X\).

On a compact subchart let \(\kappa>0\) be the minimum of \(|Q|\) on
the finite contour pieces, \(W\) the maximum of \(|w|\), \(P\) their
total length and \(A_{\rm ch}\ge1\) a common maximum of the moduli
of \(h,h_w,h_{ww}\) there. Clearance makes these finite, and
\(\kappa>0\) by (1) and (2). Write
\[
 R_{b,r}=\max\{(\ell^2/\kappa)^b,(\ell^2/\kappa)^r\},\quad
 C_{\rm ch}
 = A_{\rm ch}\big(1+C_c+C_D/\kappa+2/\kappa+
                         4W^2/\kappa^2+2C_cW/\kappa\big)
         +(2+2W/\kappa) A_{\rm ch}^2 .
\]
The finite pieces contribute at most
\((P/(2\pi))R_{b,r} C_{\rm ch}J^2 e^{\Theta|v|}\) to each integral
in (14) and to (11). These constants are named chart quantities
at fixed \(T\). Bounding the four full rays by their enlargements
\(|x|\ge6\) with (5) gives for \(b\le u\le r\)
\[
 |\partial_t Z(p,t)|\le
 \left[
 \frac{P R_{b,r} C_{\rm ch}}{2\pi}
 +\frac{2 C_{\rm sl}}{\pi}
   \max_{u_0\in\{b,r\}}\big((2\ell^2)^{u_0} 6^{1-2u_0}\big)
   E_2(2b-1)\Lambda(6)^2
 \right]J^2 e^{\Theta|v|}.                                    \tag{16}
\]
The exponent \(u\) in (7) and (15a) can be replaced in the power
of the cutoff by \(b\); the scale prefactors are bounded by their
endpoint maxima on the real-part strip.

The integrands on fixed finite pieces are \(C^1\) in real time
by clearance. At each safe-line point the field and its derivatives
are continuous in time and the bounds give a common integrable
majorant on compact \(p\) sets and compact time subcharts. Dominated
differentiation and continuity under the integral give local
real-time \(C^1\), including mergers and inward endpoint derivatives.
Dominated integration for compact \(p\) sets also gives holomorphy
in \(p\) of the derivative. This proof uses real-time uniformity
on the paid interval. The bound in (16) has the polynomial times
finite exponential growth in \(|\Im p|\) needed against fixed
Gaussian damping on bounded real-part strips.

## 5. Transitions and integer compatibility

On an overlap of two time charts \(A,B\), their principal logs
agree on the common tails, in particular for \(|x|\ge7\). Around
any overlap time, refine the two finite assignments with small
fixed circles around the finitely many distinct affected zero
locations. Each disk lies in both relevant spatial log domains,
and the circles keep their counts on a smaller time neighborhood.
For each refined cluster \(C\) the difference of the two analytic
logarithms there is \(2\pi i k_C\) with constant integer \(k_C\);
continuity and (2) give \(k_C\in\{-1,0,1\}\). If \(Z_{A,C}\) is
the cluster trace in chart \(A\), then
\[
 Z_B-Z_A=\sum_C(e^{-2\pi i k_C p}-1) Z_{A,C},\qquad
 \partial_t Z_B-\partial_t Z_A
    =\sum_C(e^{-2\pi i k_C p}-1)\partial_t Z_{A,C}.
 \tag{17}
\]
The cluster integrals and their differentiated laws on this
refinement are finite and \(C^1\). These local expressions agree
pointwise on every overlap because they come from the occurrence
values with multiplicity. Equivalently group the affected
occurrences by \(k_C\) on the overlap and use their locally
represented traces. In this description a merger is contained
in one common local refinement disk. The finite cover thus
supplies a branch atlas with the exact finite transitions (17).
There is no assertion of a single noninteger branch across all
chart changes.

At every positive integer \(n\) the transition corrections for
the value and derivative vanish. The value is then identically
\(\ell^{2n}S_n\) in real time. At \(n=1,2\), uniqueness of the
derivative of that already identified observable and the inherited
laws give
\[
 \begin{aligned}
 \partial_t Z(1)&=\ell^2(2M^2-12S_2-16DS_3),\\
 \partial_t Z(2)&=\ell^4(8MS_2-32S_3+4DS_2^2-40DS_4+4T_2^2),
       & T_2&=\sum_j w_j a_j^{-2}.
 \end{aligned}                                                 \tag{18}
\]
These use [Parent Note41 §2][n41] and [GR E05's assessment of
the integer law][gr05]. In particular (14) includes the spatial
information entering \(4T_2^2\). A denominator-only autonomous
closure is outside this result.

## 6. Collision controls and disposition

This is the documentary replay of the controls at the actual
premises of (11)–(16). The algebra and the tail estimates use the
heat law, integer zero counts and clearance, fixed strip and upper
unit count, complete product subtraction and safe-line bound.
No collision exclusion or improved signed forcing follows from
these structural ingredients. [Controls12][controls] · [CM
overview][overview] · [E01 audit][audit] · [Premises02][premises] ·
[Scope07][scope]

| Control | Failed premise or unpaid transfer |
| --- | --- |
| Quadratic and quartic heat collisions | Lack the canonical growing population. Local residue and heat algebra and coarse upper counts can hold. |
| Euler-factor translates | Change ordinary theta arithmetic and the canonical projected count discrepancy. The loose upper count can survive this change. |
| Weighted-square, finite-source, finite-score and finite-prime controls | Lose full reflected unit-weight theta equality. The endpoint-defective subclasses also fail the inherited fixed strip. |
| Reflected super-Gaussian | Fails the order-at-most-one input for the inherited paired product. Convergence of different complex-power representations is untested. |
| Smooth positive shape and positive-primitive controls | Change theta's arithmetic square expansion. Their complete canonical strip, count and safe-line transfers are unpaid. Reflection rigidity requires the full normalized reflected integer-square class. |
| Fixed-event atoms and finite/compact profiles | Fail complete theta equality, canonical growing population and full profile. The fixed-event threshold examples lack eventual simplicity there. |
| RH-conditional endpoint mergers | Change ordinary Dirichlet arithmetic and retain RH as a premise. This law admits an endpoint double, with no transfer of canonical count inferred. |
| Changed observations and fractional profiles | The former change the physical cosine/Newman readout. The latter lack the integer occurrence divisor. |
| GR changed static slices and scalar equilibrium | The static slices change the source and lack a common paid canonical heat tube; coarse slice estimates can survive. The scalar relaxation lacks a realized divisor and retains a negative terminal anchor. |

E03 may use the chartwise law, the value bound (6), the independent
space cutoff errors and the strip-growth bound (16) under assessment.
The conjugation identity is assigned separately to E08. The proof
requires no growing order, global complex-time strip, numerical
test, improved signed forcing or new tube acquisition.

[request]: ../research-progress/handoffs/VCD-GT-CM-E02-r1.md
[decision]: ../brainstorm/notes/01_VCD_GT_CM_B01_DAMPED_CAUCHY_DECISION_20261117.md
[audit]: ../reviews/02_VCD_GT_CM_E01_INPUT_AUDIT_20261117.md
[overview]: ../research-overview/01_VCD_GT_CM_RESEARCH_OVERVIEW_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[gr03]: ../../01_gaussian_resolvent_hierarchy/notes/03_VCD_GT_GR_E03_GAUSSIAN_EVOLUTION_20261117.md
[gr05]: ../../01_gaussian_resolvent_hierarchy/reviews/03_VCD_GT_GR_E05_INITIAL_PROOFS_ASSESSMENT_20261117.md
[safe]: ../../../manuscript/sections/transverse_interactions.tex
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md

