# E03 — finite Gaussian contour evolution and radial reconstruction

17 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Requested helper dispatch gpt-6.1-sol / ultra.
Actual serving model and effort are unavailable to this helper.

**Proved in-note on the frozen domain, pending E05 assessment.** All four
pins in the [E03 request][request] matched. This is a representation and
regularity result under [classification01][classification]. See the
[result index][results], [cluster18][cluster], [avoid index][avoid],
[scope07][scope] and [joint bounds12][joint]. The [E01 audit][audit] and
[B01 decision][decision] carry the inherited inputs and premise screen.

## 1. Complete slice sums and the phased conversion

Work on the paid compact real tube \(I\subset[0,1/2]\) for the unchanged
complete theta field \(H(t,z)\), with \(H_t=-H_{zz}\). Use the parameters of
the request: \(T\ge64\), \(L=\log T\), \(\ell=L^{-1}\),
\(\max(2,4\sqrt d)\le a\le L\), \(r_0=a\ell\), \(c\in[T,2T]\) and
\(|D|\le d\ell^2\le r_0^2/16\). The selected two occurrences are
\(c\pm\sqrt D\), including \(D=0\). The real \(c,D\) come from the
first two argument-principle moments on a local fixed circle in the
physical \(z\)-plane. They are locally analytic in time by the
zero-free collar and joint holomorphy of the theta source integral.
Write \(w_j=\rho_j-c=x_j+iy_j\) for each exterior occurrence,
\(Q(w)=w^2-D\), and \(a_j=Q(w_j)\). Then \(|w_j|\ge r_0\),
\(|a_j|\ge(15/16)|w_j|^2\) and \(|y_j|\le1\).

The [unit-count bound][count] gives \(O(\log(2+2T+n))\) occurrences in
\(n\le |x_j|<n+1\). For \(n\ge1\), \(|a_j|^{-p}\le(16/15)^p n^{-2p}\).
On the near shell the collar bounds \(|a_j|^{-p}\) uniformly. Thus
\(\sum_j|a_j|^{-p}\) is finite with uniform tails on \(I\), for
\(p=1,2,3\). Define
\[
 S_p=\sum_j a_j^{-p},\qquad
 G_{s,p}=\sum_j e^{-s w_j^2}a_j^{-p},\qquad
 A_{s,p}=\sum_j e^{-s|w_j|^2}a_j^{-p}.
\]
For \(s\in[s_-,s_+]\subset(0,\infty)\),
\(|e^{-s w_j^2}|=e^{-s x_j^2+s y_j^2}\le e^{s_+}e^{-s_-x_j^2}\).
All three sums are absolute and real by conjugation of the full
exterior multiset. In particular,
\[
 S_p=G_{s_0,p}+\sum_{k=1}^{n}(G_{s_k,p}-G_{s_{k-1},p})
                     +(S_p-G_{s_n,p}),\qquad s_0>\cdots>s_n>0 .
 \tag{1}
\]
For \(A\), the same telescope has nonnegative weights summing to one
at each occurrence and still acts on the signed reciprocal powers.
Writing \(s=R^{-2}\), its continuum reconstruction is
\[
 \partial_{\log R} A_{R^{-2},p}
   =\sum_j 2|w_j|^2R^{-2}e^{-|w_j|^2/R^2}a_j^{-p},\qquad
 S_p=\int_0^\infty \partial_{\log R} A_{R^{-2},p}\,\frac{dR}{R}.
 \tag{2}
\]
The per-occurrence density integrates to one by \(u=|w_j|^2/R^2\).
It is bounded by \(2/e\), which pays scale differentiation, and its
integral against \(\sum|a_j|^{-p}\) pays the absolute interchange.
The limits are \(A_{R^{-2},p}\to0\) at \(R\downarrow0\), using the
collar, and \(A_{R^{-2},p}\to S_p\) at \(R\uparrow\infty\), using a
common shell tail followed by uniform convergence on the bounded
shells. At fixed \(R\), \(A_{R^{-2},p}\) is continuous in real time:
around each slice enclose a finite near set by a zero-free rectangle
and track its zero clusters as finite continuous multisets. The paid
collar tracks the selected count. The common exterior tail bound then
gives continuity for the complete sum.

The exact conversion at a slice is
\[
 \Delta_{s,p}=A_{s,p}-G_{s,p}
 =\sum_j\frac{e^{-s(x_j^2+y_j^2)}
                 [1-e^{2s y_j^2-2is x_jy_j}]}{a_j^p}.
 \tag{3}
\]
A nonreal conjugate pair with \(w=x+iy\) and \(a_j=|a_j|e^{i\theta}\)
contributes
\[
 \frac{2}{|a_j|^p}
 \left[e^{-s(x^2+y^2)}\cos(p\theta)
       -e^{-s(x^2-y^2)}\cos(2sxy+p\theta)\right].
\]
The branch of \(\theta\) is immaterial for integer \(p\). Real
occurrences contribute zero to (3). Integrate the exponential along
the segment between \(w^2\) and \(|w|^2\), of length \(2|wy|\), to get
\[
 |\Delta_{s,p}|
 \le 2s\sum_j e^{-s x_j^2+s y_j^2}
                       |w_j y_j|\,|a_j|^{-p}.                  \tag{4}
\]
The finite positive \(s\)-range makes the right side summable and
retains the vertical amplification. At each fixed slice, the absolute
majorant \(e^{s_+}\sum_j|a_j|^{-p}\) also gives
\(G_{s,p}\to S_p\) as \(s\downarrow0\). This is a slice limit. No
\(s\downarrow0\) interchange with a time derivative or \(s\uparrow\infty\)
endpoint for \(G\) is used.

## 2. Contours and slice passage to the safe lines

Use \(h(t,w)=H_z(t,c+w)/H(t,c+w)\),
\(E(w)=e^{-s w^2}\), \(f=E/Q^p\), and
\(\Gamma=\{|w|=r_0/2\}\) counterclockwise. For a meromorphic integrand
\(B\), set
\[
 \mathscr I B=\frac1{2\pi i}\oint_\Gamma B(w)\,dw,\qquad
 \mathscr O B=\frac1{2\pi i}\int_{\mathbb R}
                   [B(x-4i)-B(x+4i)]\,dx .
\]
The outer orientation is counterclockwise, with the lower edge from
left to right and the upper edge from right to left. Both \(Q=0\)
poles lie inside \(\Gamma\), along with the target occurrences. The
annulus between the rectangle and circle has residue \(m f(w_j)\)
at an exterior zero of multiplicity \(m\).

For each fixed slice, choose the two cuts independently in distant
unit windows in the physical abscissa. In \([U,U+1]\) the count in
\([U-1,U+2]\) is at most \(N_U=C\log(3+|U|)\). Delete the intervals of
radius \(\epsilon_U=1/[4(1+N_U)]\) around those projections. The
deleted length is at most \(1/2\). A remaining abscissa \(v\) is at
distance at least \(\epsilon_U\) from every projection, including
those outside the enlarged window. Put \(x=v-c\) on the centered
vertical edge. The complete opposite-paired product gives, at equal
abscissa, the absolutely convergent difference
\[
 h(t,x+iy)-h(t,x+4i)
   =\sum_\rho\left(\frac1{v+iy-\rho}-\frac1{v+4i-\rho}\right).
 \tag{5}
\]
Subtracting the two log derivatives before summation cancels the
product regularizers. On \(-4\le y\le4\) the near shell
\(|\Re\rho-v|<1\) costs \(O(\log(2+|v|)/\epsilon_U)\), since the
safe-line divisor distance is at least 3. The shells
\(n\le|\Re\rho-v|<n+1\), \(n\ge1\), cost
\(O(\sum_{n\ge1}n^{-2}\log(2+|v|+n))=O(\log(2+|v|))\).
With the [safe-line bound][safe] this gives
\(|h(t,x+iy)|\ll\log^2(2+|v|)\) on the chosen edge. For \(|x|\ge1\)
the resulting absolute edge integral is
\[
 O\!\left(e^{16s_+} e^{-s_-x^2}|x|^{-2p}\log^2(2+|v|)\right).
\]
The omitted exterior zero tails are bounded, up to a fixed constant,
by \(e^{s_+}\sum_{n\ge N} n^{-2p}\log(2+2T+n)e^{-s_- n^2}\), where
\(N\) is the integer part of the smaller centered cut distance.
Taking the two cuts to infinity at the slice proves
\[
                      G_{s,p}=(\mathscr O-\mathscr I)(f h).    \tag{6}
\]
The horizontal integrals converge absolutely by the safe-line bound
and the Gaussian majorant below. The construction of (6) requires
only a sequence of cuts at the chosen slice.

## 3. Real-time differentiation, inner residues, and cross terms

The product and counts give absolute reciprocal-square and cube
series for \(h_w\) and \(h_{ww}\), respectively. On either safe line
the near divisor distance is at least 3, and the \(n\)-th horizontal
shell contributes \(O(n^{-2}\log(2+|c+x|+n))\) or
\(O(n^{-3}\log(2+|c+x|+n))\). Conjugation gives the lower-line log
bound from the upper one. With \(\Lambda_T(x)=\log(2+2T+|x|)\), all
three quantities \(h,h_w,h_{ww}\) are \(O(\Lambda_T(x))\) uniformly
on \(I\). At zero-free points the heat law gives the centered time
derivative
\[
 h_t=\partial_w\!\left(-H_{zz}/H\right)+c'h_w
                    =-h_{ww}-2h h_w+c'h_w.                  \tag{7}
\]
Here \(H_{zz}/H=h_w+h^2\) at \(z=c+w\). Thus \(h_t\) on the safe
lines is \(O((1+|c'|)\Lambda_T(x)^2)\).

On \(\Gamma\), \(|Q|\ge3r_0^2/16\) and the distance to every zero is
at least \(r_0/4\). Equation (5) with the same abscissa and the
corresponding derivative shell bounds now give
\(|h|=O(L/r_0)\), \(|h_w|=O(L/r_0^2)\),
\(|h_{ww}|=O(L/r_0^3)\), since \(r_0\le1\).
At any reference slice use the circle centered at that slice's
center \(c_*\) in the physical plane, fixed for nearby time. Its
moments with weights \(z-c_*,(z-c_*)^2\) are
\(2(c-c_*)\) and \(2((c-c_*)^2+D)\). Their derivatives are bounded
using the fixed-\(z\) heat derivative \(-h_{ww}-2h h_w\) on the
reference circle. This gives \(c'=O(L^2/r_0)\) and \(D'=O(L^2)\)
uniformly on \(I\). The centered \(h_t\) is bounded there by (7).
The local analytic moment construction and clearance make \(h\)
locally analytic in time on the inner circle, including target
mergers.

On \(w=x\pm4i\), \(|Q|\ge x^2+16-r_0^2/16\). With \(s\) frozen,
\[
 f_t=pD'E/Q^{p+1},\qquad f_w=-2w(s+p/Q)f,\qquad
 f_{ww}=\big[4w^2(s+p/Q)^2-2(s+p/Q)+4p w^2/Q^2\big] f .
\]
The absolute values of \(fh\), its time derivative, and the
integrands used below after integration by parts are bounded on
both lines by
\[
 C_{T,p}(1+s_+)^2\, e^{16s_+}\,
 \frac{(1+|x|)^2\,\Lambda_T(x)^2}{(1+x^2)^p}e^{-s_-x^2}.
 \tag{8}
\]
This is integrable and uniform for real \(t\in I\) and
\(s\in[s_-,s_+]\). On the compact inner contour the analogous
bounds follow from clearance and \(|E|\le e^{s_+r_0^2/4}\).
For each fixed zero-free contour point the integrands and their
time derivatives are continuous. These bounds justify real-time
differentiation of (6) and give a continuous derivative through
exterior as well as target mergers, with inward derivatives at
tube endpoints. They use neither time-uniform cuts nor a complex-time
outer strip.

For the signs in the differentiated law, the meromorphic identity
\[
 \partial_t(fh)
 = (pD'E/Q^{p+1}-f_{ww}-c'f_w)h+f_w h^2
      +\partial_w[-f h_w+f_w h-fh^2+c'fh]
\]
follows from (7). The exact derivative integrates to zero on the
inner circle and on both infinite lines, where its primitive tends
to zero at each end by (8). It follows that
\[
 \boxed{\displaystyle
 G_{s,p}'=(\mathscr O-\mathscr I)
 \left[(pD'E/Q^{p+1}-f_{ww}-c'f_w)h+f_w h^2\right].}         \tag{9}
\]
If \(s\) varied, the first coefficient of \(h\) would also include
\(-s'w^2f\). Both \(s\) and \(\ell\) are fixed here.

For an explicit accounting of the subtracted residues, let
\(g=h-2w/Q\), holomorphic in the inner disk after division by the
two target factors. The same division works to \(|w|<r_0\) at
every real slice. On \(|w|=3r_0/4\) the divided field is analytic
in time locally by clearance. Applying the Cauchy formula on that
circle and differentiating under the compact integral gives a
holomorphic \(g_t\) on a neighborhood of the closed inner disk.
Write \(R_n(B)=\mathscr I(B/Q^n)\) for a holomorphic \(B\). For \(D\ne0\),
\(R_n(B)\) is the sum over the two roots \(r^2=D\) of
\[
 \frac1{(n-1)!}\left(\frac{d}{dw}\right)^{n-1}
                      \frac{B(w)}{(w+r)^n}\Big|_{w=r}.
\]
At \(D=0\) it is the coefficient \([w^{2n-1}]B(w)\).
Expanding \(E=e^{-sD}e^{-sQ}\) and using
\(\mathscr I(w/Q)=1\) gives
\[
 \begin{aligned}
 \mathscr I(fh)
   &=2e^{-sD}(-s)^p/p!+R_p(Eg),\\
 \mathscr I\big((pD'E/Q^{p+1}-f_{ww}-c'f_w)h+f_wh^2\big)
   &=-2sD'e^{-sD}(-s)^p/p!
          +pD'R_{p+1}(Eg)+R_p(Eg_t).
 \end{aligned}                                               \tag{10}
\]
The second line differentiates the first on the fixed centered
circle, with \(g_t\) at fixed \(w\). In (9) the field is the full \(h\)
and its square retains all interactions. In particular for any
finite decomposition \(M=S_1=\sum_k M_k\) made by (1), including
its complement, the inherited \(2M^2\) is
\(2\sum_k M_k^2+4\sum_{k<l}M_kM_l\).

## 4. A radial cusp in the finite polynomial heat class

Take the even real polynomial \(P(\tau,z)=
(z^2-b^2)^2-\tau(12z^2-4b^2)+12\tau^2\), \(b>0\), with
\(\tau=t-t_*\). It solves \(P_\tau=-P_{zz}\). On a small
two-sided interval, select the cluster near \(b\). The cluster near
\(-b\) stays separated and is the complete exterior. The first
cluster has center \(c(\tau)\) and discriminant \(D(\tau)\). Reflection
gives exterior center \(-c(\tau)\) and the same discriminant. At
\(\tau=0\), evaluating the differentiated target factorization at
\(z=b\) gives \(-8b^2=-4b^2D'(0)\), so \(D'(0)=2\).
Put \(u=-2c(\tau)\), and let \(F(w,\bar w)=e^{-s w\bar w}/(w^2-D)^p\).
The two exterior displacements are \(u\pm\sqrt D\). Expanding in
\(w,\bar w\) at \(u\), their summed radial weight is
\[
 2F(u,\bar u)+(F_{ww}+F_{\bar w\bar w})(u,\bar u)D
               +2F_{w\bar w}(u,\bar u)|D|+O(|D|^{3/2}).
\]
The smooth parameter dependence of \(u,D\) preserves the remainder
near the collision. At \(\tau=0\),
\[
 F_{w\bar w}(u,\bar u)
   =-sF(u,\bar u)\big(1-su^2-2pu^2/(u^2-D)\big)
   =sF(u,\bar u)(2p-1+su^2)>0.
\]
Thus the radial sum has unequal one-sided derivatives. The
corresponding holomorphic cluster sum is locally analytic by the
finite contour formula. This cusp is a regularity example in the
finite polynomial heat class with a separated exterior double.

## 5. Controls and the quantitative consumer

The [Controls12][controls] premise screen for this representation
uses [Note44 §7][note44] and the [E01 scope check][audit] as its
documentary checks. Quadratic and quartic heat fields share local
heat and contour algebra and fail canonical population growth.
Euler-factor controls change theta arithmetic and its projected
count discrepancy. Weighted-square and finite-source/prime controls
fail full theta reflection with unit weights, and their documented
endpoint-defective classes fail the fixed strip. The reflected
super-Gaussian fails order at most one. Smooth and positive-primitive
sources change theta arithmetic, with strip and count transfer unpaid.
Fixed-event atomic and finite-profile fields fail complete theta
equality and canonical population growth. RH-conditional endpoint
controls retain RH and change ordinary Dirichlet arithmetic. Changed
observations fail the physical cosine readout and fractional profiles
fail the integer divisor. Exact-count opposite-sign slices lack a
canonical common-time tube. The finite quartic calculation above
checks the regularity distinction within its class.

For the [inherited Riccati bound][baseline], with \(m=\ell^2M\)
and \(\sigma=(t-t_0)/\ell^2\), the equation is \(m_\sigma=2m^2-\mathcal F\)
with complete normalized signed forcing \(\mathcal F=\ell^4(12S_2+16DS_3)\).
At one finite scale the exact
holomorphic part is \(\ell^4(12G_{s,2}+16DG_{s,3})\) and its complement
is \(\ell^4[12(S_2-G_{s,2})+16D(S_3-G_{s,3})]\). For radial data
substitute \(G=A-\Delta\) in both terms. The remaining consumer is
a height-uniform improvement of the upper allowance \(KL\) for the
complete forcing, or of the backward cost
\(\exp(-4\int_{\sigma_1}^{\sigma_2}m(\sigma)\,d\sigma)\),
on the paid tube with its initial layer and incoming \(D\). Any
comparison must give the direct estimate the same acquired data.
For \(s\) of order \(L^2\), (8) exposes the \(e^{16s_+}\) cost of the
fixed safe lines and (4) exposes vertical amplification at the
zeros. Finite-scale differentiability gives no height-uniform
microscopic estimate or signed forcing improvement.

[request]: ../research-progress/handoffs/VCD-GT-GR-E03-r1.md
[audit]: ../reviews/02_VCD_GT_GR_E01_INPUT_AUDIT_20261117.md
[decision]: ../brainstorm/notes/01_VCD_GT_GR_B01_COUPLED_STATE_DECISION_20261117.md
[baseline]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[note44]: ../../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md#7-controls-scope-and-the-next-quantitative-question
[count]: ../../../manuscript/sections/exterior_height.tex
[safe]: ../../../manuscript/sections/transverse_interactions.tex
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
