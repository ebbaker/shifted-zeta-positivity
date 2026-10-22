# Canonical covariance quadrature and the finite-time transport screen

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, effort
**ultra** (parent turn metadata). **Status: proved in-note in the stated parameterized scope; separate
same-model internal review.** No positive theta endpoint
margin, independent specialist review, or finite-time advantage is claimed.
See [Review 12](../reviews/12_FINITE_TIME_SIGNED_RECONSTRUCTION_OPENING_REVIEW_20261021.md).

This continuation uses [Note 11](11_CANONICAL_QUADRATIC_RESPONSE_AND_HEAD_TAIL_CANCELLATION_20261021.md),
[Note 12](12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md),
the [canonical-source manuscript](../manuscript/source.tex), and the
[finite-time program](../research-overview/03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRAM_20261021.md).
The [result index](../../../../../../../result-summaries/README.md),
[collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../../../avoid/README.md) apply, especially
[target classification](../../../../../../../avoid/01_restating_the_target.md),
[matched controls](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coupled estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [scoped conclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The gain established here is a stronger **direct canonical-law quadrature**:
a signed covariance correction with complete error O(J^-3), a higher-order
remainder than the inherited midpoint payment. The strict comparison
below uses a common x grid. A quantitative theorem gives
strict containment in Note 11's exact cell-range enclosure, not merely in
a weakened norm baseline. Gaussian reconstruction of the same source
quadrature gives exactly the same estimate. Thus this refines the direct
baseline for FTSR-03/04 but does not establish that positive time supplies
additional information.

## 1. The unchanged source and admissible endpoint geometry

Use exactly Note 11's endpoint reference F=F_m, residual E, contour
Gamma={|z-a|=R}, inner radius r<R, external floor delta>0, and actual
wall-ratio bound rho<1. Both reference roots, counted with multiplicity,
lie in |z-a|<r. [Note 13](13_PAID_ENDPOINT_WINDOW_AND_FINITE_TIME_BASELINE_20261021.md)
pays this geometry and rho<=1/15 on an explicit hypothetical-double
family; its R<=a/2 also supplies the positive-real-part premise in §5. A reference double is allowed. Put

\[
 S=L_F(E)+B_F(E,E),\quad
 C_L=4R(R+r)/\delta,\quad
 C_B=(2R(R+r)+R^2)/\delta^2.
\]

The complete discriminant is
\(\Delta_H=\Delta_F+S+R_3\), with exactly the same
\(|R_3|\le C_3(\rho)\) as Note 11. No estimate below replaces the actual
wall-ratio payment or changes that cubic remainder.

Write alpha=pi m^2, beta=pi(m+1)^2, d=beta-alpha,
D0=2alpha-3, gamma=D0/(2alpha), and let a_n,b_n,e_n,E_m,A,eta be
the manuscript's canonical masses, with eta=A/E_m and A=a_(m+1).
The canonical envelope at zero is

\[
 W(u)=\phi_m(u)e^{-d(e^{4u}-1)}
     =\alpha e^d(2\alpha e^{9u}-3e^{5u})e^{-\beta e^{4u}}.
\]

Define \(V_w(z)=\int_0^w W(u)\cos(zu)du\). Note 11 gives
\(E=E_m\int V_wd\lambda_m(w)\), where
\(\lambda_m=\eta\delta_\infty+(1-\eta)\sigma_m\).
Every source mode and the complete source ray remain present.

## 2. Compactifying the actual law without discarding its atom

Set x=e^-4w, with w=infinity corresponding to x=0, and let xi be the
pushforward of lambda_m. Define

\[
 V(x,z)=V_{-\log x/4}(z)\quad(x>0),\qquad V(0,z)=V_\infty(z).
\]

The law has the atom xi({0})=eta. Its distribution function is explicit:

\[
 P(x):=\xi([0,x])=p_m(x^{-1}-1),\qquad 0<x\le1,
 \quad P(0)=\eta.                                      \tag{1}
\]

Indeed \(\lambda_m([w,\infty])=p_m(e^{4w}-1)\). In particular

\[
 E_mP(x)=\sum_{n>m}e^{-e_n(x^{-1}-1)}
       \left(a_n+b_n\frac{\gamma x}{1-(1-\gamma)x}\right). \tag{2}
\]

This is the complete canonical law, not a freely selected density.
Its continuous density q=P' is positive on (0,1), and the n=m+1
exponential component alone gives the explicit floor

\[
 q(x)\ge q_0:=\frac{b_{m+1}\gamma}{E_m}>0.              \tag{3}
\]

To see this, differentiate its term
\((b_{m+1}/E_m)\gamma x/(1-(1-\gamma)x)\). Its derivative is
\((b_{m+1}/E_m)\gamma/(1-(1-\gamma)x)^2\ge q_0\).
All other derivatives in (2) are nonnegative because P is the
pushforward survival function of a positive Laplace mixture.

The infinite atom is retained **exactly** as eta V(0), rather than
represented by a finite midpoint. This is not a tail truncation.

## 3. Complete and explicit contour derivative bounds

Put Z=|a|+R and

\[
 h(x)=\frac{\alpha e^d}{4}
   (2\alpha x^{-13/4}-3x^{-9/4})e^{-\beta/x}.
\]

Then

\[
 V(x,z)=\int_x^1h(s)\cos((z/4)\log s)ds,
\]
\[
 V_x=-h\cos((z/4)\log x),
\quad V_{xx}=-h'\cos((z/4)\log x)
                  +\frac{zh}{4x}\sin((z/4)\log x).       \tag{4}
\]

All x derivatives extend to zero, with V^(k)(0,z)=0 for k>=1,
uniformly on Gamma: e^-beta/x dominates every power of x and log x.
Thus there is no singular final cell.

Here are closed upper bounds sufficient for implementation. For p>0 set

\[
 \mathcal S_p(\beta)=\sup_{0<x\le1}x^{-p}e^{-\beta/x}
 =\begin{cases}e^{-\beta},&\beta\ge p,\\
 (p/(e\beta))^p,&\beta<p.\end{cases}
\]

Put c=alpha e^d/4 and sum over (k,p)=(2alpha,13/4),(3,9/4).
The following constants satisfy
\(\sup_{x\in[0,1]}\|\partial_x^jV(x)\|_\Gamma\le M_j\):

\[
 M_1=c\sum k\mathcal S_{p+R/4},
\]
\[
 M_2=c\sum k\{\beta\mathcal S_{p+2+R/4}
                     +(p+Z/4)\mathcal S_{p+1+R/4}\},    \tag{5}
\]
\[
\begin{split}
 M_3=c\sum k\{&\beta^2\mathcal S_{p+4+R/4}
  +\beta(2(p+1)+Z/2)\mathcal S_{p+3+R/4}\\
  &+[p(p+1)+Zp/2+Z^2/16+Z/4]
                      \mathcal S_{p+2+R/4}\}.
\end{split}
\]

The argument uses |cos(zu)|,|sin(zu)|<=cosh(Ru)<=x^-R/4,
|z|<=Z, and the derivatives of x^-p exp(-beta/x). For the last bound,

\[
 |V_{xxx}|\le x^{-R/4}
 \left(|h''|+\frac{Z|h'|}{2x}
            +\frac{h}{x^2}(Z^2/16+Z/4)\right).
\]

Using the positive absolute coefficients (2alpha,3) in (5) is an
explicit conservative bound, not a deletion of the -3 source term.
Sharper certified suprema can replace any M_j.

Let
\(N_\infty=\int_0^\infty W(u)\cosh(Ru)du\) and
\(M=E_mN_\infty\). These are complete finite constants.

## 4. A signed covariance correction with an O(J^-3) remainder

Separate the atom {0} and divide (0,1] into J cells I_j of width
h=1/J. Put

\[
 p_j=\xi(I_j),\quad
 m_j=p_j^{-1}\int_{I_j}x\,d\xi(x),\quad
 v_j=\int_{I_j}(x-m_j)^2d\xi(x),
\quad t_j=\int_{I_j}|x-m_j|^3d\xi(x).
\]

Every p_j is strictly positive by (3). Define the single common
residual approximation and its covariance correction by

\[
 \bar E=E_m\left(\eta V(0)+\sum_jp_jV(m_j)\right),
 \qquad e_2=\frac{E_m}{2}\sum_jv_jV_{xx}(m_j).           \tag{6}
\]

The same p_j,m_j,v_j are used in the linear and quadratic response.
The elementary conditional-variance bound gives

\[
 \sum v_j\le(1-\eta)h^2/4,\qquad
 \sum t_j\le h\sum v_j\le(1-\eta)h^3/4.
\]

Taylor's theorem in the contour sup norm, with the linear moment
vanishing on each barycentric cell, proves

\[
 \|E-\bar E\|_\Gamma\le\epsilon_2
   :=\frac{E_mM_2}{2}\sum v_j
   \le\frac{E_mM_2(1-\eta)}8h^2,
\]
\[
 \|E-\bar E-e_2\|_\Gamma\le\epsilon_3
   :=\frac{E_mM_3}{6}\sum t_j
   \le\frac{E_mM_3(1-\eta)}{24}h^3.                    \tag{7}
\]

Also \(\|E\|_\Gamma,\|\bar E\|_\Gamma\le M\). The term e_2 can
have either sign and is kept as a signed analytic function. Put

\[
 C_J=L_F(\bar E)+B_F(\bar E,\bar E)
           +L_F(e_2)+2B_F(\bar E,e_2),
\]
\[
 \varepsilon_J=(C_L+2C_BM)\epsilon_3+C_B\epsilon_2^2.    \tag{8}
\]

Then the complete coupled signed response satisfies

\[
 \boxed{S\in[C_J-\varepsilon_J,C_J+\varepsilon_J].}      \tag{9}
\]

In the program's reconstruction-error notation, p0=bar E and

\[
 D_J:=L_F(e_2)+2B_F(\bar E,e_2),\qquad
 \boxed{r_-(T)=D_J-\varepsilon_J,\quad
        r_+(T)=D_J+\varepsilon_J.}                     \tag{9a}
\]

These endpoints enclose
S-L_F(p0)-Q_F(p0). They are independent of T for the fixed
heat-evolved approximation in Section 7. Their asymmetry around zero
is the retained signed covariance correction; no sign of D_J is presumed.

Proof: write e=E-bar E and r=e-e_2. Exact bilinearity gives

\[
 S-C_J=L_F(r)+2B_F(\bar E,r)+B_F(e,e).
\]

Use (7) and Note 11's contour operator bounds. In particular, the
mixed term is evaluated rather than paid separately by its modulus,
and the **entire** residual quadratic term is retained in the last
payment. No independent probability adjustment is made in Q.

The complete discriminant enclosure is

\[
 \Delta_F+C_J+
 [-\varepsilon_J-C_3(\rho),\ \varepsilon_J+C_3(\rho)].  \tag{10}
\]

Acquisition errors must be added as described below. The displayed
positive-law cell variance only controls approximation error; it does
not imply that C_J or Delta_H is positive.

## 5. Matched comparison with the exact Note 11 cell-range enclosure

The comparison uses Note 11's range construction on the declared uniform
x grid, including a separate exact atom. It asserts no fixed-J ordering
against Note 13's equal-N grid, adaptive partitions or optimized meshes.
Within this comparison use the **same** compact cells, atom, exact canonical law,
reference, complete residual, and cubic remainder. Define

\[
 G(x,y)=\frac{E_m}{2}\{L_F(V(x))+L_F(V(y))\}
                    +E_m^2B_F(V(x),V(y)).               \tag{11}
\]

Then S=int int G dxi dxi. Note 11's range method gives

\[
 L_J^{\rm range}=\sum_{i,j}p_ip_j\inf_{I_i\times I_j}G,
 \quad
 U_J^{\rm range}=\sum_{i,j}p_ip_j\sup_{I_i\times I_j}G,  \tag{12}
\]

where I_0={0},p_0=eta and endpoint closures are used in the extrema.
These are **exact** cell extrema, not sample values or weakened
Lipschitz surrogates. The same source data are available to both
methods. Formula (9) additionally uses moments of that law; it does
not purport to dominate every direct method which can use those moments.

Suppose there is a closed rectangle X times Y in (0,1)^2, with side
lengths l_x,l_y>0, on which G_x has fixed sign and |G_x|>=g>0.
Set

\[
 c_*:=gq_0^2l_xl_y/8>0.
\]

For h<=min(l_x,l_y)/4, the union of complete grid cells contained in
each interval has length at least half the interval's length. If
G_x>=g, then in a cell [l,l+h] times [b,b+h] within the rectangle,

\[
 G(x,y)-\inf G\ge G(x,y)-G(l,y)\ge g(x-l),
\]
\[
 \sup G-G(x,y)\ge G(l+h,y)-G(x,y)\ge g(l+h-x).
\]

After integration, (3) gives a contribution at least
g q_0^2 h^3/2 to **each** endpoint slack from that cell. Summing
at least l_xl_y/(4h^2) such cells gives

\[
 S-L_J^{\rm range}\ge c_*h,
 \qquad U_J^{\rm range}-S\ge c_*h.                     \tag{13}
\]

The case G_x<=-g reverses the endpoint roles and yields the same result.
Consequently

\[
 2\varepsilon_J<c_*h                                  \tag{14}
\]

implies strict containment of (9) in (12). Both endpoints improve.
Because epsilon_J<=K_3h^3+K_4h^4 with the explicit constants in (7)-(8),
(14) holds for all sufficiently fine meshes at exact data accuracy.
For an explicit threshold it suffices to enforce

\[
 2K_3h^2+2K_4h^3<c_*,\qquad
 K_3=(C_L+2C_BM)E_mM_3(1-\eta)/24,
\quad K_4=C_B[E_mM_2(1-\eta)/8]^2.
\]

Adding the identical Delta_F and identical cubic interval preserves
strict containment. The proof does not require knowing the sign of S
or Delta_H. It remains valid if H has an actual double in the window.

The rectangle premise is automatic under the manuscript's positive-real-
part two-root assumption, although its constants must be acquired for
an implemented comparison. Indeed V(1)=0, and

\[
 G_x(x,1)=-\frac{E_mh(x)}2K_F(-\log x/4),\qquad
 K_F(u)=L_F(\cos(zu)).                                 \tag{15}
\]

The manuscript's kernel-oscillation lemma makes K_F nonzero on some
finite open interval; that lemma allows a reference double. Choose an
interior point with K_F!=0. Continuity then gives an interior rectangle
with y sufficiently close to 1 and the required g. Thus the containment
statement is a genuine quantitative approximation result in the
possible-double regime, not an assumption of endpoint positivity.

This does **not** compare different experimental data budgets without
accounting for them. Exact-law moments are extra derived quantities
which cost work to acquire, but the full unchanged law is the same
input. No runtime or operation-count advantage is claimed.

## 6. Acquisition, arithmetic tails and complete source rays

The cell masses and moments follow directly from (2), using integration
by parts for raw moments. For k>=1,

\[
 \int_a^b x^k dP(x)=b^kP(b)-a^kP(a)
                      -k\int_a^b x^{k-1}P(x)dx.
\]

For k=0 use P(b)-P(a). In particular the first continuous cell has
mass P(h)-P(0)=P(h)-eta; eta is subtracted exactly once. All infinite
sums must be enclosed. For any N>=m+1, define

\[
 r_N=((N+2)/(N+1))^4e^{-\pi(2N+3)}<1.
\]

The manuscript's successive-ratio proof gives the complete omitted-mass
payment

\[
 \sum_{n>N}(a_n+b_n)
 \le (1+3/D_0)\frac{a_{N+1}}{1-r_N}.                   \tag{16}
\]

Every normalized moment on [0,1] has integrand bounded by one before
normalization; (16), with the interval for E_m, pays its omitted mass.
Conditional means and variances must be evaluated with outward interval
arithmetic, including division by the positive cell masses. Contour
values, Delta_F, and C_J likewise need their own certified enclosures.

If the acquired center C_hat has |C_hat-C_J|<=a_J, use the radius
epsilon_J+a_J in (9). To ensure strict containment even in the ideal
exact range baseline, the sufficient condition is

\[
 2(\varepsilon_J+a_J)<c_*h.                            \tag{17}
\]

If both methods additionally pay the **same** symmetric acquisition
allowance, adding it to each interval preserves already proved strict
containment. If their acquisition contracts differ, use (17) or compare
the fully enlarged endpoints directly. In particular, fixed positive
acquisition error does not permit an unqualified J->infinity claim.

For an endpoint source-ray cutoff U>=0, the complete envelope payment is

\[
 \int_U^\infty W(u)\cosh(Ru)du
 \le\frac{\alpha^2e^d}{2}\beta^{-(9+R)/4}
    \Gamma((9+R)/4,\beta e^{4U}).                      \tag{18}
\]

This follows from W<=2alpha^2 e^d exp(9u-beta e^4u),
cosh(Ru)<=exp(Ru), and v=beta e^4u. The atom's V(0) is
complete and (18) must be paid whenever it is acquired by truncation.

### An explicit mesh and accuracy schedule

Put K=K_3+K_4. Suppose the fully acquired center has a_J<=A h^3
for a declared nonnegative A. A concrete sufficient mesh condition is

\[
 J\ge\left\lceil\max\left\{1,\frac4{l_x},\frac4{l_y},
                       2\sqrt{\frac{K+A}{c_*}}\right\}\right\rceil.
                                                               \tag{18a}
\]

Indeed h<=1 gives epsilon_J+a_J<=(K+A)h^3, and (18a) gives
2(epsilon_J+a_J)<=c_*h/2<c_*h. Thus (17) holds with a factor-two
reserve. These constants depend on the fixed contour and canonical
cutoff; the statement supplies no height-uniform J or numerical g.

There is a simple sufficient moment-accuracy contract behind a_J=O(h^3).
For each cell let d_(j,k)=int_(I_j)x^k dxi, k=0,1,2. Suppose each
raw moment has absolute acquisition error at most kappa h^4, and
the approximating moments are feasible for a nonnegative measure in
that same cell. Assume kappa h^3<=q0/2. Because p_j>=q0h,
the approximate cell mass is >=q0h/2, and

\[
 \sum_j|\widehat p_j-p_j|\le\kappa h^3,\qquad
 |\widehat m_j-m_j|\le4\kappa h^3/q_0,\qquad
 \sum_j|\widehat v_j-v_j|\le4\kappa h^3.               \tag{18b}
\]

The last inequality follows from
v=d2-d1^2/d0: along a segment of feasible moment triples its three
partial derivatives have absolute values at most 1,2,1.
Atom mass and E_m also need O(h^3) absolute accuracy. The acquisition contract must additionally verify normalized
nonnegative approximate weights and these declared error bounds together.
Feasible moment intervals contain the true law, but simply normalizing
arbitrary rounded masses does not automatically preserve the same bounds.

Given bounds delta0>=||bar E-bar E_hat|| and
delta2>=||e2-e2_hat||, direct bilinearity gives the following explicit
center-acquisition payment, before any final contour quadrature error:

\[
 a_J\le(C_L+2C_BM)(\delta_0+\delta_2)
       +C_B\delta_0^2+2C_B\delta_0(\epsilon_2+\delta_2). \tag{18c}
\]

For example, residual acquisition may use

\[
 \delta_0\le E_m\left[N_\infty\tau_p+M_1\tau_m\right]
                   +|E_m-\widehat E_m|N_\infty,
\]

where tau_p includes the atom and the total absolute mass error, and
tau_m=sum hat p_j |m_j-hat m_j|. Source-transform evaluation errors
are added by their normalized weighted average. Similarly

\[
 \delta_2\le\frac{E_m}{2}
       \left(M_2\sum|v_j-\widehat v_j|
           +M_3\sum\widehat v_j|m_j-\widehat m_j|\right)
       +\frac{|E_m-\widehat E_m|M_2}{2}\sum\widehat v_j.
\]

These formulas show concretely that (18b), O(h^3) atom/normalization
accuracy, and O(h^3) uniform V evaluation yield delta0=O(h^3).
Since sum hat v_j<=h^2/4, V_xx evaluations need only O(h) uniform
accuracy to keep delta2=O(h^3). Final L/B evaluations must have
O(h^3) total error. This is an accuracy schedule, not a measured cost
or an assertion that interval acquisition is automatic. A competing
direct method is granted exactly the same moments and accuracy.

## 7. Finite time gives the same covariance estimate for the same data

For a fixed finite T>0 define

\[
 V_T(x,y)=\int_0^{-\log x/4}W(u)e^{Tu^2}\cos(yu)du,
\]

with the complete integral at x=0, and use the same actual law xi:

\[
 E(T,y)=E_m\int V_T(x,y)d\xi(x),
\quad P_T(y)=E_m\{\eta V_T(0,y)+\sum p_jV_T(m_j,y)\}.
\]

For every fixed finite T, complete superexponential source decay and
Gaussian integration give

\[
 \int_{\mathbb R}K_T(z,y)V_T(x,y)dy=V(x,z).             \tag{19}
\]

The same identity holds after two x derivatives. At x=0 all positive
x derivatives of V_T vanish; at the finite nodes the differentiated
fields grow at most polynomially in y, and are Gaussian integrable.
Consequently reconstruction sends P_T to exactly bar E and sends

\[
 \frac{E_m}{2}\sum v_j\partial_x^2V_T(m_j,y)
\]

to exactly e_2. The complete finite-time linear, mixed and quadratic
response therefore produces precisely C_J and (9) when estimated
through the same canonical moment data. There is no T-dependent gain.
Applying extra absolute bounds to the transported expression can lose
accuracy but cannot create new information in this declared data model.

This conclusion is scoped to the exact heat evolution of this fixed
canonical source quadrature. It does not exclude better independently
obtained positive-time information, heat-defect approximations, or
other correlated measurements of E(T).

For completeness, finite numerical y integration has an explicit
payment. Put N_T=int_0^infinity W(u)e^(Tu^2)du. Then
|E(T,y)|,|P_T(y)|<=E_m N_T on the whole real line, so |r_T|<=2E_mN_T.
For Y>R,

\[
 \sup_{z\in\Gamma}\left|
 \int_{|y-a|>Y}K_T(z,y)r_T(y)dy\right|
 \le2E_mN_Te^{R^2/(4T)}
                  \operatorname{erfc}((Y-R)/(2\sqrt T)). \tag{20}
\]

The proof bounds |K_T(z,y)| by the real Gaussian with distance
|y-a|-R and the factor exp(R^2/(4T)). The polynomial tails from
the covariance-correction field can either be integrated as Gaussian
moments or avoided by using its exact endpoint derivative formula (4).
No truncated y integral is identified with complete reconstruction.

A particularly simple complete source bound is available for
0<T<8beta. Since u^2<=e^4u/8, (18) remains valid for
W e^(Tu^2) cosh(Ru) with beta replaced inside the gamma-expression by
beta-T/8. Thus, for example, the whole fixed matching range 0<T<=4beta
has explicit complete heat-moment payments. Larger finite T can also
be treated by the unchanged superexponential envelope; no growing-T
claim is needed here.

## 8. Controls and program status

The proof uses the unchanged canonical coefficients quantitatively in
the law (2), the positive density floor (3), and the complete mass tail
(16). The covariance/Taylor identities themselves are generic, and
must also hold on collision controls when their corresponding source
representation and smoothness assumptions hold. The density floor and
the strict interval improvement do not distinguish collision from
noncollision: a valid increasingly sharp enclosure still contains the
true zero discriminant at a collision.

The control distinctions remain those in the repository register:
Euler-factor sources change the canonical coefficients; finite weighted-
square and finite-prime controls lack the full normalized reflection
conjunction; reflected and primitive-compatible sources lack the canonical
square law; close normalized endpoint controls fail ordinary Dirichlet
series arithmetic. Weighted-square variants may still admit a modified
positive law and a similar covariance estimate, so this theorem does
not use law positivity alone as an exclusion premise. No false sign is
predicted for any of these controls. The polynomial heat double and
the one-mode transfer control in Note 12 satisfy the generic identities.

At a hypothetical theta double, Note 11's head-tail cancellation still
requires Delta_F+S+R3=0. Formula (10) is consistent with that equality
for every J. Refining its quadrature cannot turn the equality into a
strictly positive lower endpoint. A new signed source inequality remains
necessary to exclude that event.

Task disposition: FTSR-03 obtains a complete, quantitative coupled
canonical-error estimate for this approximation. FTSR-04 obtains a
strict improvement over the inherited cell-range direct baseline in
the declared fine-mesh regime, but the same-data optimized direct
method produces the identical interval; **there is no finite-time
advantage**. FTSR-05 passes in its no-exclusion scope. FTSR-06 and
FTSR-07 do not open on the strength of this direct quadrature gain.
No positive margin, all-height result, higher-multiplicity conclusion,
or new manuscript snapshot is supplied.
