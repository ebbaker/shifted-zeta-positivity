# Coupled coefficient backward transport on a complete fixed wall

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Status: **proved finite coefficient transport and source-error theorem; canonical coefficient acquisition remains unpaid**. Separate same-model contributing agents checked the contour equations and exact polynomial controls. No specialist review or priority claim.

This combines [Note 09's backward precision audit][backward] with [Note 11's coefficient filter][forest]. The concrete gain is a complete-source, finite-dimensional backward propagator with no internal root-gap denominator. Its matrices are polynomials in one nilpotent coefficient shift and therefore commute. The propagator is a **finite exponential**, and its norm is a finite polynomial in acquired integrated source moments. It need not be polynomial in the terminal heat time, and its constants are not uniform in population size.

Read the [result index][results], [control register][controls], [avoid index][avoid], particularly [target classification][a01], [coupled estimates][a12] and [scope discipline][a07]. This is a finite error theorem with explicit complete-source acquisition costs. It does not establish a useful theta filter upper bound, simplicity proportion, or all-simple theorem.

## 1. Fixed-domain hypotheses and the complete prepared equation

Fix a center \(z_0\), a radius \(R>0\), and the spatial circle \(\Gamma=\{|z-z_0|=R\}\). On a neighborhood of \([t_0,T]\) times its closed disk, suppose \(H(t,z)\) is holomorphic, solves \(H_t=-H_{zz}\), and is nonzero on \(\Gamma\). Its complete interior population has constant multiplicity \(N\), and

\[
 H=UP,\qquad
 P(t,z)=\prod_{i=1}^N(z-z_i(t)),\qquad b=U_z/U.
 \tag{1}
\]

The prepared polynomial is monic and its coefficients are analytic in time, including through internal collisions; \(U\) is holomorphic and nonzero in the disk. No individual root labels, simplicity or reality are needed. A positive wall floor on the full interval is part of the assumptions, not supplied by RH. The interval may include an internal event at \(t_0=0\).

For analytic \(f\), define the analytic remainder

\[
 \mathcal T_P f(z)=\frac1{2\pi i}\oint_\Gamma
 \frac{f(w)}{P(w)}\frac{P(w)-P(z)}{w-z}\,dw.
 \tag{2}
\]

It is a polynomial of degree at most \(N-1\), and \(f-\mathcal T_Pf\) is divisible by \(P\) with analytic quotient. This is Hermite remainder, so it matches all jets required at repeated roots. To check it directly, subtract (2) from Cauchy's formula for \(f(z)\); the difference is \(P(z)(2\pi i)^{-1}\oint f(w)/[P(w)(w-z)]\,dw\). In particular \(\mathcal T_P(Pv)=0\) for analytic \(v\).

The heat equation applied to (1) therefore gives

\[
 \boxed{P_t=-P_{zz}-2\Psi_H[P],\qquad
 \Psi_H[P]:=\mathcal T_P(bP_z).}
 \tag{3}
\]

Every omitted root and nonzero unit remains in \(b\); (3) is not an unforced polynomial heat equation.

There is a stronger direct complete-source form. Put

\[
 Z_H(t,w)=\frac{H_{ww}}H(t,w),\quad
 Q_f(w,z)=\frac{f(w)-f(z)}{w-z},\quad
 \mathcal A_H(t)f=\frac1{2\pi i}\oint_\Gamma Z_H(t,w)Q_f(w,z)\,dw.
 \tag{4}
\]

Then

\[
 \boxed{P_t=-\mathcal A_H P,\qquad
 \mathcal A_H P=P_{zz}+2\Psi_H[P].}
 \tag{5}
\]

Indeed \(H_{zz}/H=P_{zz}/P+2bP_z/P+U_{zz}/U\). The last analytic term integrates to zero against the polynomial \(Q_P\); the first two give the remainders of \(P_{zz}\) and \(2bP_z\). Thus (5) is valid through collisions directly, without a limiting root argument. Unlike the remainder formula considered separately, its acquisition needs no additional floor on \(P\) along the wall: the paid floor is the one for the complete field \(H\).

## 2. The sharp free-heat coefficient norm and its limitation

Write \(\zeta=z-z_0\), \(f=\sum_{j=0}^n f_j\zeta^j\), and use the fixed coefficient norm

\[
 \|f\|_R=\sum_{j=0}^n|f_j|R^j.
\]

For \(s\ge0\), the induced norm of the finite heat operator is exactly

\[
 \boxed{\|e^{s\partial_z^2}\|_{R,n}
 =C_n(s/R^2):=
 \sum_{k=0}^{\lfloor n/2\rfloor}
 \frac{n!}{k!(n-2k)!}(s/R^2)^k.}
 \tag{6}
\]

The coefficient matrix is nonnegative in this weighted basis. Its degree-\(j\) column sum is \(C_j\), which increases with \(j\), so the largest column is the degree-\(n\) column. Equality is attained by \(\zeta^n/R^n\). This proves both the bound and its worst-case sharpness.

Let \(P_*\) be a differentiable monic reference polynomial of degree \(N\), let \(\Psi_*\) be its declared complete reference forcing, and set

\[
 d_*=P_{*,t}+P_{*,zz}+2\Psi_*.
\]

For \(E=P-P_*\), \(n=N-1\), exact backward Duhamel gives

\[
 E(t)=e^{(T-t)\partial_z^2}E(T)
 +\int_t^T e^{(s-t)\partial_z^2}
       \{2(\Psi_H[P]-\Psi_*)+d_*\}(s)\,ds.
 \tag{7}
\]

Consequently an **independently acquired joint** allowance
\(\|2(\Psi_H[P]-\Psi_*)+d_*\|_R\le\varepsilon_F\) yields

\[
 \|E(t)\|_R\le C_n((T-t)/R^2)\|E(T)\|_R
 +\int_t^T C_n((s-t)/R^2)\varepsilon_F(s)\,ds.
 \tag{8}
\]

For a constant residual bound, the last kernel integral is explicitly
\(\sum_{k\le n/2} n!(T-t)^{k+1}/[k!(n-2k)!(k+1)R^{2k}]\).
At fixed degree and scale the free terminal factor has degree \(\lfloor n/2\rfloor\) in the interval length. This is not a closed source theorem if the asserted residual bound still depends on the unknown coefficient error. The next section closes the equation using complete wall data instead.

## 3. Complete source matrices commute and have a finite exponential

Define the plain degree-lowering shift

\[
 \mathsf S\zeta^j=\zeta^{j-1}\ (j\ge1),\qquad \mathsf S1=0,
\]

which is **not** differentiation. Set

\[
 M_k(t)=\frac1{2\pi i}\oint_\Gamma
       (w-z_0)^k Z_H(t,w)\,dw.
 \tag{9}
\]

For a monomial, \(Q_{\zeta^j}=\sum_{l=0}^{j-1}(w-z_0)^{j-1-l}\zeta^l\), so on degree at most \(n\),

\[
 \boxed{\mathcal A_H(t)=\sum_{j=1}^n M_{j-1}(t)\mathsf S^j.}
 \tag{10}
\]

All these matrices commute, even when the complete source varies with time. They are strictly triangular, with zero diagonal. Write

\[
 m_j(t,s)=\int_t^s M_{j-1}(u)\,du,
 \qquad
 \mathcal U_H(t,s)=
 \exp\!\left(\sum_{j=1}^n m_j(t,s)\mathsf S^j\right).
 \tag{11}
\]

The exponential terminates at order \(n\); no infinite matrix series or root separation is involved. It satisfies \(\partial_t\mathcal U_H=-\mathcal A_H(t)\mathcal U_H\) and \(\mathcal U_H(s,s)=I\), hence is the exact backward propagator. The same formula on degree \(N\) transports the full monic polynomial.

There is an exact norm formula. If

\[
 v_k(t,s)=[u^k]\exp\!\left(\sum_{j=1}^n
             \frac{m_j(t,s)}{R^j}u^j\right),
\]

then

\[
 \boxed{\|\mathcal U_H(t,s)\|_{R,n}
       =B_n(t,s):=\sum_{k=0}^n|v_k(t,s)|.}
 \tag{12}
\]

Indeed the weighted degree-\(l\) column sum is \(\sum_{k=0}^l|v_k|\), maximized at \(l=n\). Replacing each integrated moment by an upper bound on its modulus produces an explicit positive-coefficient majorant \(\widehat B_n\).

For a simple wall-only version, let

\[
 V(t,s)=\int_t^s\sup_\Gamma|Z_H(u,w)|\,du.
\]

Cauchy's contour bound gives \(|m_j|/R^j\le V\), whence

\[
 \boxed{B_n(t,s)\le\mathcal B_n(V):=
        \sum_{l=0}^n {n\choose l}\frac{V^l}{l!}.}
 \tag{13}
\]

To see the coefficient, majorize the series by
\(\exp(Vu/(1-u))\) through degree \(n\); summing its coefficients through that degree gives (13) by the binomial identity
\(\sum_{k=l}^n {k-1\choose l-1}={n\choose l}\).
This is a finite polynomial in the **acquired integral \(V\)**. It is stronger than the crude exponential Gronwall bound for the same operator norm, but says nothing by itself about how \(V\) grows with terminal time or height.

## 4. A closed coefficient error theorem from wall-source differences

Let a reference field \(H_*\), with a complete monic prepared polynomial \(P_*\) of the same degree, also be nonzero on \(\Gamma\). It need not solve the heat equation. Define \(Z_*=H_{*,zz}/H_*\), \(\mathcal A_*\) by (4), and

\[
 d_*=P_{*,t}+\mathcal A_*P_*.
 \tag{14}
\]

Then the **closed** error equation is

\[
 E'=-\mathcal A_H E-r,
 \qquad r=(\mathcal A_H-\mathcal A_*)P_*+d_*.
 \tag{15}
\]

It depends on the full wall quotients, the known reference polynomial and its declared defect. It does not replace the unknown internal force by an assumed independent quantity.

Suppose independently acquired source estimates give

\[
 \sup_\Gamma|Z_H-Z_*|\le\eta_Z(t),\qquad
 \|d_*(t)\|_R\le\eta_d(t).
\]

Put \(W_R(P_*)=\sum_{j=1}^N j|p_{*,j}|R^j\), where \(p_{*,j}\) are coefficients in powers of \(\zeta\). Then

\[
 \|r(t)\|_R\le
   \varepsilon_r(t):=\eta_Z(t)W_R(P_*(t))+\eta_d(t),
 \tag{16}
\]

because \(\|Q_{P_*}(w,\cdot)\|_R\le W_R(P_*)/R\) on \(\Gamma\). The exact solution and finite error theorem are

\[
 E(t)=\mathcal U_H(t,T)E(T)+
       \int_t^T\mathcal U_H(t,s)r(s)\,ds,
\]
\[
 \boxed{\|E(t)\|_R\le
  \widehat B_{N-1}(t,T)\|E(T)\|_R+
  \int_t^T\widehat B_{N-1}(t,s)\varepsilon_r(s)\,ds.}
 \tag{17}
\]

Here \(\widehat B\) may be computed from individually enclosed integrated moments or replaced by (13). Every term is acquired from terminal coefficients, complete wall-source data, and the reference. Internal collisions cause no singularity in this theorem while the wall and source bounds survive.

For a prepared reference field, its defect itself has the wall formula

\[
 d_*(z)=\frac1{2\pi i}\oint_\Gamma
 \frac{H_{*,t}+H_{*,ww}}{H_*}(w)Q_{P_*}(w,z)\,dw.
 \tag{18}
\]

It vanishes for an exact heat reference. For an arbitrary polynomial approximation without a reference field, use the direct polynomial definition (14); (18) is not available by declaration alone.

### First-order source acquisition and the joint numerator

The source difference in (16) is exactly

\[
 Z_H-Z_*=
 \frac{H_{zz}H_*-HH_{*,zz}}{HH_*}.
 \tag{19}
\]

Estimate this complete numerator together when the source representation permits it. It contains all exterior roots, oscillatory source terms and tails. No separate per-root division by \(H_z\) occurs.

For a transparent fallback, suppose on \(\Gamma\)

\[
 |H_*|\ge m_*>0,\quad |H-H_*|\le e_0<m_*,\quad
 |H_{zz}-H_{*,zz}|\le e_2,\quad |H_{*,zz}|\le M_{2,*}.
\]

Then

\[
 \boxed{\eta_Z\le
 \frac{e_2}{m_*-e_0}+
 \frac{M_{2,*}e_0}{m_*(m_*-e_0)}.}
 \tag{20}
\]

This is first order in the field/second-derivative errors when the relative wall error is small. If \(H-H_*\) is analytic in a larger disk of radius \(R+d\) and its absolute boundary error is at most \(e_{\rm out}\), maximum modulus and Cauchy's estimate give \(e_0\le e_{\rm out}\) and \(e_2\le2e_{\rm out}/d^2\). Alternatively use complete-source derivative bounds directly. A relative logarithm on an annulus alone does not justify differentiating it from one boundary without the missing interior information; the entire field-difference argument just given does.

For canonical theta, bounds for \(H,H_{zz}\) and their approximation errors come from the unchanged complete source, retaining both integration and source-index tails. Those formulas give upper allowances; a positive oscillatory wall floor is a separate obligation. This note supplies no such favorable theta wall package.

## 5. A correlated endpoint version and the fair direct comparison

If both fields are exact heat fields, their propagators are polynomials in the same shift and commute, including across the two sources. On degree \(N\),

\[
 E(t)=\mathcal U_H(t,T)E(T)
       +[\mathcal U_H(t,T)-\mathcal U_*(t,T)]P_*(T).
 \tag{21}
\]

This keeps integrated source differences together instead of integrating separate instantaneous forcing bounds. Suppose
\(|m_{*,j}|/R^j\le a_j\),
\(|m_j-m_{*,j}|/R^j\le e_j\). Define nonnegative coefficients, truncated at degree \(N\), by

\[
 d_k=[u^k]
 \exp\!\left(\sum_{j=1}^N a_j u^j\right)
 \left[\exp\!\left(\sum_{j=1}^N e_j u^j\right)-1\right].
 \tag{22}
\]

Then a valid sharper structured allowance for the second term of (21) is

\[
 \sum_{j=0}^N |p_{*,j}(T)|R^j\sum_{k=1}^j d_k
 \le\|P_*(T)\|_R\sum_{k=1}^N d_k.
 \tag{23}
\]

The first term still uses the degree-\(N-1\) norm (12), since the leading monic coefficient cancels. Formula (22) is first order in small integrated moment errors; its higher terms and all normalization factors remain explicit.

For an exact heat field, the same moments are endpoint-wall data:

\[
 m_j(t,T)=-\frac1{2\pi i}\oint_\Gamma
 (w-z_0)^{j-1}\log\frac{H(T,w)}{H(t,w)}\,dw.
 \tag{24}
\]

The logarithm is lifted continuously in time on the zero-free wall. Its time derivative is \(-Z_H\); any constant branch change integrates to zero. The ratio has zero spatial winding because the complete root count is unchanged. This proves (24), not merely a formal logarithm identity.

Thus equally informative direct endpoint-wall estimates obtain the same integrated coefficient data. For example, endpoint relative comparisons \(|H/H_*-1|\le\eta_s<1\), \(s=t,T\), give logarithm bounds \(K_s=-\log(1-\eta_s)\) and
\(|m_j-m_{*,j}|/R^j\le K_t+K_T\); evaluating the joint contour difference may be sharper. Such a bound already includes early endpoint source information and is not a free consequence of terminal asymptotics.

A common complex-time path has the same commuting formula with \(m_j=\int_\gamma M_{j-1}\,d\tau\). Absolute source errors must be integrated on the actual path. Analytic endpoint equality alone gives no curved-contour estimation advantage. The intended gain here is the finite coefficient condition theorem, not a claim that moving a contour improves source accuracy.

## 6. Terminal precision, controls and the earlier scalar instability

To attain a prescribed early coefficient allowance \(E_0\), (17) requires the explicit sum of its terminal and integrated-source terms to be at most \(E_0\). For the free heat equation the worst-case terminal allowance is reduced by the exact polynomial factor (6). For complete-source transport the corresponding factor is (12), with its acquired moments. No assertion that existing late-theta errors meet these budgets is made.

Several sharp controls fix the interpretation.

**Unforced heat polynomials.** For \(H=P\), \(b=0\) and \(\Psi=0\); (3) reduces exactly to polynomial heat evolution. Formula (7) has zero forcing residual for two such fields. A monic degree-\(N\) terminal perturbation in degree \(N-1\) attains the factor in (6) under backward heat evolution. Source splitting must preserve this cancellation; bounding \(\mathcal A_HE\) and \(E_{zz}\) separately can manufacture a spurious forcing error.

The fixed-source operator norm (12) and the free-heat norm (6) nevertheless describe different error models. For \(H=z^3-6tz\), the complete source operator is \(\mathcal A_H=6\mathsf S^2\): on a quadratic error it produces a constant \(6(T-t)\), whereas \(e^{(T-t)\partial_z^2}\) produces \(2(T-t)\). Both transport the actual odd cubic correctly. When two different polynomial heat fields are compared in (15), their source-quotient difference supplies the remaining term; it cannot be set to zero merely because both units equal one.

**Quadratic endpoint precision.** For \(P_s(t,z)=z^2-2(t+s)\), \(s\ge0\), the difference from \(P_0\) is the constant \(-2s\). Its coefficient error transports with factor one, while the filtered terminal difference is \(s/[2(2T+s)]\) and its inverse local sensitivity at the double is \(T/t\), as proved in Note 09. Stable complete coefficient transport and sensitive terminal spectral compression are compatible.

**Why Note 09's scalar exponential is not contradicted.** A symmetric two-root cluster with fixed center zero has \(P=z^2-h/4\) and the complete gap law \(h'=8-4Sh\). Its source moment is

\[
 M_1=h'/4=2-Sh.
\]

If a comparison keeps the same prescribed compression \(S\) and has coefficient difference \(E=-\delta h/4\), then \(\delta M_1=4SE\). The constant-coefficient homogeneous propagator in (11) is one, but the **source residual** in (15) is \(4SE\); the closed equation becomes \(E'=-4SE\) and gives exactly the scalar factor \(\exp(4\int S)\). Calling this residual independently known would be circular. Note 09 estimated an uncorrelated compression implementation; the present theorem instead consumes independently acquired complete source-quotient differences or moments. It has not proved those differences small for canonical theta.

**Stationary sine field.** For \(H=e^t\sin z\), \(Z_H=-1\) is analytic, all moments (9) vanish, and the complete prepared polynomial is stationary. Equation (3) then has \(\Psi=-P_{zz}/2\), which cancels its internal heat term. The source propagator is exactly the identity. This is an exact test that exterior forcing is retained, not a theta source model.

**Repeated roots and higher multiplicities.** The contour remainder in (2) matches repeated-root jets, so (3)--(24) remain finite through a complete internal Hermite birth on a surviving wall. They do not erase the endpoint signature: the filter from Note 11 still tends to \(m-H_m\). Its denominator/error precision must still be checked after converting the coefficient enclosure.

All broader registered controls satisfy the local analytic identities on the walls they actually possess. Euler-factor and close endpoint controls change the canonical source data; weighted-square and finite-prime controls lack the full reflection/global real continuation assumptions used by the endpoint consumer; reflected and positive-primitive controls lack the unchanged integer-square source. None is rejected merely by (5) or (17), and no unproved all-real interval is assigned to it.

## 7. Feeding the filter and remaining domain costs

The output of (17) or (21)--(23) is a complete coefficient uncertainty set. If only a scalar norm allowance \(E_0\) is retained, it gives individual coefficient errors \(|e_j|\le E_0/R^j\); keeping the full vector or correlated set is preferable. Apply Note 11's coefficient polynomial \(D\), complete residual \(G-q_*D\), and explicit nonzero denominator test to obtain an early scalar filter enclosure. This requires no individual root disks. It still requires a useful reference filter value and adequate denominator/residual margins, and then the separate real-population and coverage hypotheses for a simplicity conclusion.

The following costs remain explicit:

- A **fixed** zero-free wall for the entire interval is stronger than a sequence of moving walls. Neither RH nor a fixed-rank late saddle theorem supplies it. For a fixed disk centered at the origin, the fixed-rank late asymptotics place each fixed positive rank inside it eventually; thus that disk cannot retain one fixed finite population as \(T\to\infty\). This example is not an assertion about arbitrary off-axis disks. Subdivide into justified fixed-domain charts if needed and pay each coefficient transfer.
- The center and radius in this note are fixed. For \(P=R(t)^N\widehat P(t,(z-z_0(t))/R(t))\), the normalized equation acquires \((z_0'/R)\widehat P_\zeta+(R'/R)(\zeta\widehat P_\zeta-N\widehat P)\), as well as the transformed source equation. These terms are not contained in the fixed-basis formulas.
- Polynomial amplification in integrated moments is not automatically polynomial amplification in late time or height. The source quotient uses a wall floor; its size and error can be expensive. The degree and coefficient-majorant costs also grow with \(N\).
- The heat-birth filter scale still requires appropriately scaled coefficient/source accuracy, as in Note 11. Transporting a coefficient vector stably in one fixed norm does not automatically supply that microscopic norm at a shrinking endpoint wall.

The finite task is therefore complete at the analytical interface level: the complete prepared ODE, an optimal free-heat norm, a closed finite source propagator, first-order wall acquisition bounds, a correlated endpoint version and sharp controls are proved. The next useful application would have to acquire a concrete canonical wall/moment error package and demonstrate that the resulting filter budget passes. That source estimate and all growing-height simplicity conclusions remain open.

The accompanying [exact-rational replay][replay], [small execution record][record], and [separate same-model review][review] check prepared remainders, repeated-root jets, finite heat matrices, complete-source shift operators, their commutation/composition and the distinct error models above. They check finite algebra and the stated analytical proof, not a theta wall or a source-accuracy certificate.

[backward]: 09_BACKWARD_FILTER_TRANSPORT_AND_TERMINAL_PRECISION_20261023.md
[forest]: 11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[replay]: ../numerics/06_check_coefficient_transport_20261023.py
[record]: ../numerics/06_COEFFICIENT_TRANSPORT_CHECKS_20261023.json
[review]: ../reviews/10_COUPLED_COEFFICIENT_TRANSPORT_REVIEW_20261023.md

## Appendix A. Complete source-wall error budgets

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Contributing-agent derivation and internal same-model checks; no specialist review or priority claim.

**Status: proved finite wall/remainder identities and explicit coefficient error bounds; no theta acquisition.** This supports the [prepared-polynomial backward theorem in Note 12](12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md). It compares complete populations using their outer-wall data, with no internal root labels or gap floor. A direct complete-source quotient removes the need to divide by the prepared polynomial on the acquisition wall. The missing wall floors, derivative errors and full time-range control remain explicit inputs.

Use [Note 08](08_CURVED_CONTOUR_TRANSPORT_AND_HEIGHT_GRAPH_20261023.md) for prepared-polynomial acquisition, [Note 11](11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md) for the scalar filter consumer, the [result index](../../../../result-summaries/README.md), [control register](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md). In particular the [coupled-estimate rule](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) forbids separating terms whose exact cancellation is part of the finite heat law.

### A.1. Analytic remainder without internal interpolation nodes

Let H and H_* be jointly holomorphic in the common time and z on the stated domain. Fix a center z_0 and write xi=z-z_0. A common zero-free wall Gamma encloses the complete N-root populations of H=UP and H_*=U_*P_*, with P and P_* monic of degree N and both units holomorphic and nonvanishing inside a neighborhood of the wall and its interior. Internal multiplicities are allowed. Put b=U_z/U and b_*=U_{*,z}/U_*.

For a polynomial f and a monic P define

\[
 Q_P(w,z)=\frac{P(w)-P(z)}{w-z},
\]

and for any function f holomorphic inside Gamma define its analytic remainder by

\[
 T_Pf(z)=\frac1{2\pi i}\oint_\Gamma
      \frac{f(w)}{P(w)}Q_P(w,z)\,dw.
 \tag{S1}
\]

The removable diagonal in Q_P is interpreted polynomially. This is a polynomial in z of degree at most N-1. Cauchy's formula gives f-T_Pf=P times a holomorphic function inside the wall, so (S1) is the unique Hermite interpolation remainder at the complete zeros with multiplicities. For polynomial f it is ordinary polynomial division. No individual root chart occurs.

If H_tau=-H_zz, differentiating H=UP and taking the remainder gives exactly

\[
 \boxed{P_\tau=-P_{zz}-2\Psi_H(P),
 \qquad \Psi_H(P):=T_P(bP').}
 \tag{S2}
\]

The terms involving U_tau/U and U_zz/U multiply P and disappear under T_P. The exterior unit is still present in b; it has not been discarded.

A reference need not solve the heat equation. Its complete defect is

\[
 d_*:=P_{*,\tau}+P_{*,zz}+2T_{P_*}(b_*P_*')
 =T_{P_*}\left(\frac{H_{*,\tau}+H_{*,zz}}{U_*}\right).
 \tag{S3}
\]

With delta P=P-P_*, the coefficient difference therefore obeys

\[
 \delta P_\tau=-\delta P_{zz}
 -2[\Psi_H(P)-\Psi_{H_*}(P_*)]-d_*.
 \tag{S4}
\]

In a backward Duhamel formula the bracket and d_* have positive integral signs. This is consistent with the definition of the reference defect and must not be reversed.

### A.2. Explicit coefficient norms and a single combined force numerator

Use the fixed norm ||f||_R=sum_j |f_j|R^j for f=sum_j f_j xi^j, with R>0. Suppose Gamma is the circle |w-z_0|=r, r≥R. For P=sum_{j=0}^N p_j xi^j define

\[
 D_r(P)=\sum_{j=1}^Nj|p_j|r^{j-1},\qquad
 K_{r,R}(P)=\sum_{j=1}^N|p_j|
       \sum_{k=0}^{j-1}r^{j-1-k}R^k.
 \tag{S5}
\]

Then |P'(w)|≤D_r(P) and ||Q_P(w,.)||_R≤K_(r,R)(P). At r=R these two budgets are equal. For a general wall replace r in the powers by sup|w-z_0| and the circle factor r below by length(Gamma)/(2pi).

The full force difference has the single exact numerator

\[
 \Psi_H(P)-\Psi_{H_*}(P_*)
 =\frac1{2\pi i}\oint_\Gamma
 \frac{\mathcal J(w,.)}{P(w)P_*(w)}\,dw,
\]
\[
 \mathcal J=bP'P_*Q_P-b_*P_*'P Q_{P_*}.
 \tag{S6}
\]

All factors in this expression are evaluated on the same wall and from the same coefficient/source data. If |P|≥m_P>0 and |P_*|≥m_*>0 there, a directly acquired coefficient bound J_R≥sup_Gamma ||mathcal J||_R gives

\[
 \boxed{\|\Psi_H(P)-\Psi_{H_*}(P_*)\|_R
       \le r J_R/(m_Pm_*).}
 \tag{S7}
\]

Acquire the combined numerator before taking absolute values. In particular a signed uncertainty model shared by b, P and P_* should be propagated through (S6), rather than replaced automatically by their separate suprema.

There is a reference-based fallback that avoids individual root displacement. With Psi_b(P)=T_P(bP'), split exactly

\[
 \Psi_H(P)-\Psi_{H_*}(P_*)
 =\{\Psi_b(P)-\Psi_b(P_*)\}
  +T_{P_*}[(b-b_*)P_*'].
 \tag{S8}
\]

The last term evaluates the complete source-force error at the **reference polynomial**, not at unknown actual roots. If beta_0≥sup_Gamma|b-b_*|, its norm is at most

\[
 r\,\beta_0\,D_r(P_*)K_{r,R}(P_*)/m_*.
 \tag{S9}
\]

For the first term, linearity of Q in P gives

\[
 \frac{Q_P}{P}-\frac{Q_{P_*}}{P_*}
 =\frac{Q_{\delta P}}P-
   \frac{Q_{P_*}\delta P(w)}{PP_*},
\]
\[
 \Psi_b(P)-\Psi_b(P_*)
 =\frac1{2\pi i}\oint_\Gamma b\left[
 \frac{\delta P'Q_P}{P}
 +P_*'\left(\frac{Q_{\delta P}}P
 -\frac{Q_{P_*}\delta P(w)}{PP_*}\right)\right]dw.
 \tag{S10}
\]

This identity also permits a direct coupled enclosure. For an explicit coefficient-tube fallback put n=N-1, e=||delta P||_R, v=(r/R)^n, k_delta=nv/r, K_*=K_(r,R)(P_*), and D_*=D_r(P_*). Then

\[
 |\delta P(w)|\le ve,\qquad
 |\delta P'(w)|,\ \|Q_{\delta P}(w,.)\|_R\le k_\delta e.
\]

If e≤e_0, m_*-ve_0=m_0>0 and |b|≤B on the wall, (S10) gives

\[
 \|\Psi_b(P)-\Psi_b(P_*)\|_R\le L_\Psi e,
\]
\[
 L_\Psi=rB\left[
 \frac{k_\delta(K_*+k_\delta e_0+D_*)}{m_0}
 +\frac{D_*K_*v}{m_0m_*}\right].
 \tag{S11}
\]

All constants are finite outer-wall quantities. A Gronwall closure using only (S11) can reintroduce exponential growth. That is a property of this coarse remainder closure; it is not necessary in the stronger direct source-quotient route below.

### A.3. Nested relative walls acquire the unit error

Let a larger circle Sigma, radius r_2>r about the same center, be zero-free for both fields. Require that the complete prepared populations are the same N zeros counted on both walls, so the annulus contains no extra zero of either field and both units extend nonvanishing through the whole outer domain. If

\[
 |H/H_*-1|\le\eta<1\quad\hbox{on Sigma},\qquad
 \ell(w)=\operatorname{Log}(H/H_*),\quad K=-\log(1-\eta),
\]

then the outer-wall Cauchy projection and integration by parts give

\[
 b(z)-b_*(z)=\frac1{2\pi i}\oint_\Sigma
       \frac{\ell(w)}{(w-z)^2}\,dw.
\]

Consequently a valid inner-wall input for (S9) is

\[
 \boxed{\beta_0\le\frac{r_2}{(r_2-r)^2}K.}
 \tag{S12}
\]

A known constant in ell may be subtracted exactly; a nonconstant analytic part can change the unit force and must be retained. Known contour coefficients can be integrated before estimating the remainder. One may take B≤sup_Gamma|b_*|+beta_0 in (S11).

Importantly this is a formula for the analytic **unit projection** of the logarithmic derivative. When the actual internal roots differ, ell need not extend holomorphically through the interior. The same outer relative bound does not, by itself, justify applying interior Cauchy derivative bounds to the full log(H/H_*) on the inner wall. This distinction prevents replacing source-derivative acquisition by an invalid gap-free log estimate.

### A.4. A complete source quotient eliminates the prepared-polynomial floor

Put Z_H=H_zz/H on the wall, and for any polynomial f define the coefficient operator

\[
 \mathcal C_H[f](z)=\frac1{2\pi i}\oint_\Gamma
       Z_H(w)\frac{f(w)-f(z)}{w-z}\,dw.
 \tag{S13}
\]

Then the spatial factorization alone proves

\[
 \boxed{\mathcal C_H[P]=P_{zz}+2\Psi_H(P).}
 \tag{S14}
\]

Indeed H_zz/H=P_zz/P+2bP'/P+(b_z+b²). The last term is analytic inside the wall and its integral against Q_P is zero; the first remainder is P_zz. This proof applies at multiple internal roots, without an appeal to singular root velocities. For an actual heat field,

\[
 P_\tau=-\mathcal C_H[P].
 \tag{S15}
\]

Likewise the reference defect has the direct acquisition formula

\[
 \boxed{d_*=\frac1{2\pi i}\oint_\Gamma
    \frac{H_{*,\tau}+H_{*,zz}}{H_*}Q_{P_*}\,dw.}
 \tag{S16}
\]

It requires only the reference field floor on Gamma. It follows either from (S3) or by differentiating the prepared coefficients for a general analytic reference field.

The complete force difference is therefore

\[
 \boxed{2[\Psi_H(P)-\Psi_{H_*}(P_*)]
 =\frac1{2\pi i}\oint_\Gamma
   [Z_H Q_{\delta P}+(Z_H-Z_{H_*})Q_{P_*}]\,dw
  -\delta P_{zz}.}
 \tag{S17}
\]

This route uses no separately acquired floor for P or P_*. Only the complete field wall floors occur in Z. The subtraction of delta P_zz in (S17) is essential: for two unforced polynomial heat flows it cancels the entire integral, leaving zero unit force. Estimating the two sides separately would create a spurious residual.

Writing

\[
 \mathcal J_2=H_{zz}H_*-HH_{*,zz},\qquad
 Z_H-Z_{H_*}=\mathcal J_2/(HH_*),
 \tag{S18}
\]

retains the complete source correlation in the required second-jet difference. If the field floors are m_H and m_H*, and J_2 bounds this joint numerator on Gamma, then

\[
 \beta_Z:=\sup_\Gamma|Z_H-Z_{H_*}|
 \le J_2/(m_Hm_{H_*}).
\]

In particular the reference source residual has the direct bound

\[
 \boxed{\|\mathcal C_H[P_*]-\mathcal C_{H_*}[P_*]\|_R
   \le r\,\beta_Z\,K_{r,R}(P_*).}
 \tag{S19}
\]

This evaluates the quotient difference at the reference coefficient vector and never inserts a force bound times an unproved root displacement.

For clarity about source costs, if only |H-H_*|≤e_0 and |H_zz-H_{*,zz}|≤e_2 on Gamma are supplied, with |H_*|≥m_*^H>e_0 and |H_{*,zz}|≤M_{2,*}, then

\[
 \beta_Z\le\frac{e_2}{m_*^H-e_0}
 +\frac{M_{2,*}e_0}{m_*^H(m_*^H-e_0)}.
 \tag{S20}
\]

If instead a complete **absolute** error E_0 is known on the larger circle Sigma and H-H_* is holomorphic inside it, the maximum principle and Cauchy disks give e_0≤E_0 and e_2≤2E_0/(r_2-r)². This uses the holomorphic field difference, not a logarithm with internal zeros and poles. A relative outer error can be converted to E_0≤eta sup_Sigma|H_*|, but that amplitude cost may be poor. Direct acquisition of the correlated numerator (S18) can be substantially better; no advantage is assumed without a numerical or analytic budget.

Complete theta derivative upper bounds are supplied by the moments A_j of Note 08. The field floor and joint oscillatory numerator in (S18) remain separate lower/correlated source inputs. Both source tails and all rounding errors must be paid. Nothing in (S13)–(S20) supplies such a floor merely from source positivity.

### A.5. Finite coefficient propagation and exact controls

The operator C_H lowers polynomial degree. In the xi basis it is a polynomial in the plain backward shift S(xi^j)=xi^(j-1) for j≥1 and S(1)=0: its coefficients are the wall moments of Z_H. Thus all C_H(t) on the fixed coordinate chart commute, and their finite coefficient propagators truncate. Note 12 develops this direct source propagation, including its complete reference residual. The gain is polynomial dependence on the accumulated, independently supplied wall-moment budgets at fixed degree. Those budgets themselves need not grow polynomially with elapsed time; their acquisition is not free.

The simpler free-heat comparison makes the avoided overpayment explicit. On degree at most n=N-1,

\[
 \|e^{s\partial_z^2}\|_{R\to R}
 =C_n(s/R^2):=\sum_{k=0}^{\lfloor n/2\rfloor}
   \frac{n!}{k!(n-2k)!}(s/R^2)^k\quad(s\ge0).
 \tag{S21}
\]

Monomial column sums prove this exact norm; the maximum occurs at degree n. A generic norm-Gronwall estimate would instead pay exp(n(n-1)s/R²). For quadratic populations n=1, C_1=1. For cubic populations n=2, C_2=1+2s/R² rather than exp(2s/R²). This is a proved finite error-gain in the stated coefficient norm, not a claim that the source force is absent in theta.

The controls retain that force:

- **Unforced quadratic and cubic heat polynomials.** For H=P, b=0, (S14) gives C_H[P]=P_zz and (S17) vanishes for the unit-force difference. The exact backward coefficient error is the truncated heat operator. P=z²-2t and P=z³-6tz verify the factors and signs through their collisions.
- **Nonzero constant unit force.** If P_0 is a monic initial polynomial and kappa is constant, the genuine heat field \(H=e^{\kappa z-\kappa^2t}(e^{-t\partial_z^2}P_0)(z-2\kappa t)\) has b=kappa and prepared equation P_tau=-P_zz-2kappa P_z. Its inverse coefficient propagator e^(s(D²+2kappa D)) is again a finite polynomial, now retaining drift. Dropping the unit would omit the root displacement 2kappa t. This is a special algebraic control, not a description of theta's unit.
- **Stationary sine exterior cancellation.** For H=e^(ell²t)sin(ell z), the complete quotient Z_H=-ell² is analytic, hence C_H[P]=0 for every finite complete prepared population. Equation (S14) forces Psi_H(P)=-P_zz/2. A quadratic population has Psi=-1; the symmetric cubic P=z³-d²z, d=pi/ell, has Psi=-3z. Deleting this unit remainder predicts false root motion. The wall must exclude the next sine zeros and include every selected one.

For negative or complex common time, the identities hold on every analytically prepared wall domain where the listed field/unit conditions hold. Coefficient norms use absolute path increments; no Hermitian positivity is imported. A moving spatial wall can be treated on overlapping fixed-wall charts, using the same prepared coefficients and paid wall transitions. A height-dependent time graph is not a common holomorphic time coordinate and still requires Note 08's separate correction terms.

### A.6. Review disposition and remaining inputs

The identities, wall-norm constants, reference evaluation and polynomial-versus-exponential comparison above were checked directly. The [exact-rational replay](../numerics/06_check_coefficient_transport_20261023.py), [small record](../numerics/06_COEFFICIENT_TRANSPORT_CHECKS_20261023.json), and [separate same-model review](../reviews/10_COUPLED_COEFFICIENT_TRANSPORT_REVIEW_20261023.md) support the main Note 12; they do not acquire theta wall data. In particular the following errors are excluded by the controls: dropping b, reversing the reference-defect sign, omitting delta P_zz from (S17), applying Cauchy estimates to an unproved interior logarithm, or treating a complete quotient floor as automatically supplied by a polynomial floor.

These estimates do not supply a canonical theta wall or force/residual bound on an early-to-late time slab. A finite application must acquire the complete population, common charts, field floors, appropriate outer source errors and any reference heat defect. A direct coefficient propagator can then retain the complete source information without internal gap conditioning. Its final discriminant/filter and endpoint conclusion still requires the separate error thresholds of Notes 08 and 11; polynomial coefficient transport alone does not prove simplicity.
