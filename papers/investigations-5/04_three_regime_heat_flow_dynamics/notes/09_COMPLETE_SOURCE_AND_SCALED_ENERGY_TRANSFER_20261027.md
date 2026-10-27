# Complete source interface and finite scaled energy transfer

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.
Chat0004, **Continue collision energy research**, thread
`01a17e2e-8b79-7b91-9be0-f1405597eb03`.

**Status: proved in-note conditional interface and finite error bounds;
same-assistant assessment only.** This is the CE-01/02/03 part of the
[Note08 assignment][assignment]. The direct shifted-source model below
pays its frequency tail after exact low-jet subtraction. A finite
coefficient functional transfers its normalized error to annulus energy.
These are approximation results, not independent collision exclusion.
[Note10][next] tests the complete signed correction and closes this
return's error budget; [Review05][review] records the checks.

The [result index][results], [collision controls][controls], and
[avoid index][avoid] govern the claims, especially [classification][a01],
[control screening][a02], [scope][a07], and [coupled estimates][a12].
The complete prepared operator is imported from [HDC Note12][transport].
The Hermite profile and its source-Cauchy argument are inherited from
[Note07][prior] and its cited BW-10 Note22. No literature priority is claimed.

## 1. Fixed event, fixed wall, and exact source

Write the source variable as v and elapsed physical time as u. Let

\[
 H(t,z)=\int_0^\infty e^{tv^2}\Phi(v)\cos(zv)\,dv,
 \qquad H_t=-H_{zz}.
\]

Fix a real event (t_c,a) of exact finite multiplicity m>=2, with
c=H_z^{(m)}(t_c,a)/m! nonzero. Initially only local real analyticity and
the heat equation are needed; the threshold assumption is added in Note10.
Choose rho>0 so the closed disk |z-a|<=rho contains just this event at
t_c and its boundary Gamma contains no zero. By compactness there is a
complex time disk |t-t_c|<=tau on which Gamma stays zero-free and the
interior count is m. Decrease tau if necessary so all these roots lie in
|z-a|<rho/2. The positive wall floor h_Gamma is conditional on this
event and wall, not an acquired numerical theta floor.

Let H=UP be its complete preparation, P monic of degree m, and b=U_z/U.
Its coefficients and b are holomorphic on a smaller common domain,
including t=t_c. With Q_f(zeta,z)=(f(zeta)-f(z))/(zeta-z), the imported
complete equation is

\[
 P_t=-\mathcal A_H P=-P_{zz}-2\mathcal T_P(bP_z),\qquad
 \mathcal A_H f=\frac1{2\pi i}\oint_\Gamma
                  \frac{H_{zz}}H(\zeta)Q_f(\zeta,z)\,d\zeta.       \tag{1}
\]

Here T_P is analytic remainder modulo P. The quotient is the actual source

\[
 \frac{H_{zz}}H(t,\zeta)=
 -\frac{\int_0^\infty v^2e^{tv^2}\Phi(v)\cos(\zeta v)\,dv}
        {\int_0^\infty e^{tv^2}\Phi(v)\cos(\zeta v)\,dv}.          \tag{2}
\]

Equation (1), unlike individual root velocities, is valid at the event.
For an approximate complete field H_*, retain the joint numerator
H_zz H_*-H H_{*,zz} when estimating its quotient error, and retain the
defect H_{*,t}+H_{*,zz} if it is nonzero. The acquired data are field
floors and complete field/second-spatial-derivative errors on the wall;
a bound on the positive source alone supplies no denominator floor.

A useful explicit exterior payment is available on this same wall.
Put A_1=integral v exp((t_c+tau)v^2+rho v) Phi(v) dv and
B_Gamma=A_1/h_Gamma+2m/rho. On Gamma, |b|<=B_Gamma, since
P'/P is the sum of m root reciprocals and every root lies inside rho/2.
The maximum principle and an interior Cauchy disk give

\[
 \sup_{|z-a|\le\rho/2}|b_z(t,z)|\le 2B_\Gamma/\rho=:B_1.        \tag{3}
\]

All constants are fixed-event quantities. This proves finiteness, not
uniformity in a, m, |c|^{-1}, rho^{-1}, or h_Gamma^{-1}.

## 2. Discriminant identity with the exterior retained

On a small real right-time interval the m roots x_i are real and simple
by the Hermite unfolding (also derived from the gates in Section 4).
Put p=m(m-1)/2 and

\[
 D=\prod_{i<j}(x_i-x_j)^2,\quad
 E=\sum_{i<j}(x_i-x_j)^{-2},\quad
 B=\sum_{i<j}\frac{b(x_i)-b(x_j)}{x_i-x_j}.
\]

For S_i=sum_{j!=i}(x_i-x_j)^{-1}, x_i'=2S_i+2b(x_i).
The triple terms cancel in sum_i S_i^2, leaving 2E. Therefore

\[
 (\log D)'=2\sum_i x_i'S_i=8E+4B.                            \tag{4}
\]

This is a simple-root identity for u>0, not a finite logarithm at u=0.
The polynomial equation (1) is the continuation through u=0.

Set t=t_c+r^2s, z=a+rw, F_r=H/(cr^m), and
q_r(s,w)=r^{-m}P(t_c+r^2s,a+rw). Its unit logarithmic derivative is
beta_r(s,w)=r b(t_c+r^2s,a+rw). On a fixed scaled outer circle containing
exactly the cluster, contour deformation and (1) give

\[
 (q_r)_s=-\frac1{2\pi i}\oint
          \frac{(F_r)_{ww}}{F_r}(\zeta)Q_{q_r}(\zeta,w)\,d\zeta.
                                                                    \tag{5}
\]

Let d_r=Disc(q_r), e_r=r^2E, and
\(\mathcal B_r=\sum_{i<j}(\beta_r(w_i)-\beta_r(w_j))/(w_i-w_j)\).
Then exactly

\[
 I_r:=\int_{r^2}^{4r^2}E(t_c+u)\,du
 =\frac18\log\frac{d_r(4)}{d_r(1)}
       -\frac12\int_1^4\mathcal B_r(s)\,ds,\qquad
 |\mathcal B_r|\le p B_1 r^2.                              \tag{6}
\]

The wall is fixed during differentiation: r,a,c are parameters, not
moving choices. Membership does not change. In coefficient coordinates
q=w^m+sum_{k=1}^m a_k w^{m-k}, the first integrand is explicitly
\(-\nabla Disc(q)\cdot[\mathcal A_{F_r}q]_{\rm coeff}/Disc(q)\).
This, (2), and the complete exterior in (6) specify the source consumer.
An endpoint discriminant at u=0 has not been assumed positive.

## 3. Direct shifted-source hierarchy and its complete tail

The old recurrence [fixed-order theorem][fixed] applies to H(-T,z);
its [moving endpoint theorem][moving] requires T>=1/log(X/(4pi)).
At fixed event height, T=r^2 eventually violates that condition, and
exp(-r^2v^2)exp(t_cv^2)Phi(v) is a different initial source. This proves
failure of that **direct invocation**, not failure of every adaptation.
We therefore test the specified alternate representation, the exact
shifted integral.

Define

\[
 h_n=\frac1{n!}\int_0^\infty e^{t_cv^2}\Phi(v)v^n
                         \cos(av+n\pi/2)\,dv,\qquad
 P_n(s,w)=\sum_{k\le n/2}\frac{n!(-s)^k w^{n-2k}}{k!(n-2k)!}.
                                                                    \tag{7}
\]

Thus h_0=...=h_{m-1}=0 and h_m=c under the event assumption. Both
exponential arms of cos and every theta mode are retained in (7).
The exact parabolic expansion is H(t_c+r^2s,a+rw)=sum_n h_n r^n P_n.

For a fixed N>=0 put L=m+N. Define
K_r(v)=exp(r^2sv^2)cos(av+rwv) and let T_L K_r be its Taylor polynomial
in r through degree L. For a fixed frequency cutoff V>=0 set

\[
 \mathcal H_{N,V}=
 \sum_{n=m}^{L}h_n r^nP_n(s,w)
 +\int_0^V e^{t_cv^2}\Phi(v)[K_r(v)-T_LK_r(v)]\,dv.         \tag{8}
\]

This retains the signed integral on [0,V] and replaces only its remote
remainder. Every term solves the scaled heat equation exactly. V and
all h_n are frozen under differentiation. V=0 is the polynomial baseline.

Choose S>=4 and R large enough for the consumer, and a finite q>0
(an auxiliary radius in the r-plane, distinct from the polynomial q_r).
On |s|<=S+1, |w|<=R+1, |r|<=q the kernel is bounded by
exp(q^2(S+1)v^2+q(R+1)v). Put

\[
 M_V=\int_V^\infty e^{(t_c+q^2(S+1))v^2+q(R+1)v}\Phi(v)\,dv.
\]

For 0<|r|<=q/2, geometric Cauchy remainder and unit scaled buffers give

\[
 \boxed{\sup_{|s|\le S,|w|\le R}
 |\partial_s^\ell\partial_w^j(F_r-\mathcal H_{N,V}/(cr^m))|
 \le\frac{2j!\ell! M_V}{|c|q^{m+N+1}}|r|^{N+1}.}          \tag{9}
\]

This holds for any declared fixed finite j,ell; in particular j<=2 and
ell<=1 suffice for (5). The static energy transfer below uses only j=ell=0.
Domination by the complete source justifies the expansion, integrals,
and derivatives. Physical derivatives would additionally cost r^{-j-2ell}.

For completeness the theta tail has a concrete elementary majorant.
The standard source is
Phi(v)=sum_{n>=1}(2pi^2 n^4 e^{9v}-3pi n^2 e^{5v})exp(-pi n^2 e^{4v}).
For v>=0 all its summands are positive, and

\[
 \Phi(v)\le C_\Phi e^{9v}e^{-(\pi/2)e^{4v}},\qquad
 C_\Phi=2\pi^2\sum_{n\ge1}n^4e^{-\pi n^2/2}<\infty.
\]

Let T=max(0,t_c+q^2(S+1)), A=q(R+1)+9. If V>=1 and
T V^2+A V<=(pi/4)e^{4V}, then (Tv^2+Av)e^{-4v} decreases thereafter,
and substitution y=(pi/4)e^{4v} proves

\[
 M_V\le\frac{C_\Phi}{\pi e^{4V}}
                      \exp[-(\pi/4)e^{4V}].              \tag{10}
\]

No theta modes, completion terms, or remote tail have silently vanished.
The kernel/source normalization was rechecked in [Polymath's primary text][poly].

**Gain and debit.** A raw cutoff pays M_V/(|c|r^m); (8) pays
2M_V r^{N+1}/(|c|q^{m+N+1}). The gain is obtained by retaining the
complete low moments, not by asserting that the omitted source is small
relative to H. N=2 gives a useful r^3 normalized error and retains the
first coupled curvature in Note10. It is sufficient for this return.

If moments are supplied with errors epsilon_n, add, before any conclusion,

\[
 \frac1{|c|}\sum_{n=0}^{L}\epsilon_n |r|^{n-m}
                    \sup_K|P_n|                         \tag{11}
\]

and the differentiated versions when needed. For n<m these allowances
blow up unless the exact event cancellations are imposed or actually
resolved to the required precision. An error in c and its normalization
also needs payment. Exact (7) defines coefficients; it is not a certified
oscillatory evaluator. Consequently CE-02 is **Partial**: (9)-(10) are
a direct finite source-tail theorem, but no independent arithmetic
hierarchy that excludes an event has been acquired. Merely increasing N
would refine the same allowed collision.

## 4. A coefficient transfer without physical gap denominators

Here are fully specified, finite constants for transferring any actual
normalized field error. They may be conservative; no superiority over
equally informed root-disk constants is asserted.

For q=w^m+a_1w^{m-1}+...+a_m define the coefficient polynomials

\[
 \mathscr D(a)=\prod_{i<j}(w_i-w_j)^2,\quad
 \mathscr Q(a)=\sum_{i<j}\prod_{(k,l)\ne(i,j),\ k<l}(w_k-w_l)^2.
                                                                    \tag{12}
\]

Both are symmetric polynomials in the roots and hence explicit finite
polynomials in a; e(q)=Q/D. For m=2, Q=1 and D=a_1^2-4a_2.
For m=3, Q=(a_1^2-3a_2)^2. This is an algebraic energy functional, not
the discriminant derivative with its exterior deleted.

Choose R>2 max_i|h_i|+1, where h_i are roots of P_m(1,w).
On Gamma_R, uniformly for real 1<=s<=4, the baseline P_m has floor
mu=(R-2 max|h_i|)^m. Let M_k=binom(m,k)R^k. For a coefficient
polynomial A=sum_nu A_nu a^nu define

\[
 A_{abs}(M)=\sum_\nu|A_\nu|M^\nu,\qquad
 L_A=\sum_{k=1}^m(\partial_k A)_{abs}(M).
\]

Define b_0=0 and

\[
 b_k=\frac1k\sum_{i=1}^k\{m b_{k-i}+i\binom m{k-i}\},
 \qquad C_{coef}=\max_{1\le k\le m}R^k b_k.                \tag{13}
\]

If analytic fields f,g have exactly m zeros in Gamma_R, |g|>=h there,
and |f-g|<=delta<h, set ell_delta=-log(1-delta/h). Their power sums obey

\[
 p_k(f)-p_k(g)=-\frac{k}{2\pi i}\oint_{\Gamma_R}
                       w^{k-1}\log(f/g)\,dw,
 \quad |\Delta p_k|\le kR^k ell_\delta.                   \tag{14}
\]

Only the boundary logarithm is used; it is not presumed holomorphic
across internal zeros and poles. Newton's identities, |p_i|<=mR^i,
and |a_k|<=M_k give |Delta a_k|<=R^k b_k ell_delta by induction.

Let d_*=Disc(P_m(1,.))=2^p product_{k=1}^m k^k>0, d_0=d_*/2.
The formula follows from P_m'=mP_{m-1} and the three-term recurrence
by induction on the resultant. Choose epsilon_*<mu/2 so that

\[
 L_{\mathscr D} C_{coef}
       [-\log(1-\epsilon_*/\mu)]\le d_*/2.               \tag{15}
\]

Any field with sup_Gamma_R|f-P_m|<=epsilon_* has m zeros and
|D(q_f)|>=d_0, since D(P_m(s,.))=s^p d_*. The same argument on the
straight field homotopy from P_m proves its real zeros remain real and
simple when f is real on the real axis. Thus (15) derives a scaled
discriminant floor from the hypothetical unfolding; it assumes no
physical gap at t_c.

For two such fields, take h=mu-epsilon_* and delta<=h/2. The coefficient
box is convex, so the polynomial mean-value bound proves

\[
 |e(q_f)-e(q_g)|\le K_m\delta,\qquad
 K_m=\frac{2C_{coef}}h
 \left(\frac{L_{\mathscr Q}}{d_0}
       +\frac{\mathscr Q_{abs}(M)L_{\mathscr D}}{d_0^2}\right).
                                                                    \tag{16}
\]

It follows by integration that |I(f)-I(g)|<=3K_m delta when delta is
uniform on the annulus. No time derivative of an error bound is used.
The constants retain every m,R,count and scaled-discriminant cost.

For the actual model (8), choose r small so f=F_r and
g=H_{N,V}/(cr^m) both meet (15). The inherited source-Cauchy estimate
2M_0 r/(|c|q^{m+1}) and (9) provide explicit sufficient gates.
Then

\[
 |I_r-I_{N,V,r}|\le
 \frac{6K_m M_V}{|c|q^{m+N+1}}r^{N+1}.                    \tag{17}
\]

This acquires CE-03's local conditional transfer. It does not give
energy for a larger unisolated window: choose W inside the isolating
disk so E_W=E_cl, or separately pay additional clusters and pairs.
The physical count and wall are fixed before r tends to zero.

## 5. Handoff to the signed calculation

The new source-tail payment and coefficient transfer remove no part of
the leading Hermite energy. The expression to test next is the coupled
curvature
2h_{m+2}/h_m-(h_{m+1}/h_m)^2, together with the exact exterior term (6).
[Note10][next] computes its coefficient before taking absolute values,
tests both the energy and the specified transverse consumer, and records
the supported limits. All claims here pass applicable analytic colliding
controls; the explicit screen is there. The old negative-time recurrence
has not been relabeled as a positive-time theorem.

[assignment]: 08_COLLISION_ENERGY_CONTINUATION_20261027.md
[prior]: 07_COLLISION_SCALE_RESOLUTION_AND_PROOF_MECHANISMS_20261027.md
[next]: 10_COUPLED_CURVATURE_AND_ENERGY_BUDGET_20261027.md
[review]: ../reviews/05_COLLISION_ENERGY_FIRST_RETURN_SELF_ASSESSMENT_20261027.md
[transport]: ../../../investigations-4/12_height_dependent_heat_contours/notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
[fixed]: ../../01_heat_density_asymptotics/recurrence/notes/03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md
[moving]: ../../01_heat_density_asymptotics/recurrence/notes/20_MOVING_LOWER_ENDPOINT_20261026.md
[poly]: https://arxiv.org/html/1904.12438v2
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
