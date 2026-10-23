# Curved common-time transport, wall stability and height-graph corrections

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Proof development and control checks by a contributing same-model agent; no independent specialist review or priority claim.

**Status: finite conditional transport and stability estimates proved in-note.** The new quantitative part is a relative-value wall estimate for the complete prepared polynomial, including a discriminant enclosure through internal collisions; it does not require differentiating the wall approximation or assuming an internal gap. A separate, explicitly conditioned estimate controls the filtered spectrum. Height-dependent sampling has additional slope, orientation and area terms, and a contraction estimate quantifies one valid comparison with a common-time population. No canonical theta wall, resolvent floor, growing-height bound or simplicity improvement is acquired here.

This completes a finite analytical interface for HDC-08, while its canonical-source acquisition remains open. Use the [program](../research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md), [spectral consumer](06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md), and [complete force estimate](07_COMPLETE_SOURCE_FORCE_AND_FILTER_RESIDUAL_20261023.md). The [result index](../../../../result-summaries/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../avoid/README.md), [target classification](../../../../avoid/01_restating_the_target.md), [coupled-estimate rule](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md) govern the interpretation. These are finite estimates and diagnostics, not an RH-equivalent simplicity assertion counted as progress.

## 1. Hypotheses and complete source budgets

Let H(tau,z) be holomorphic in both variables on a neighborhood of the compact set under discussion and satisfy H_tau=-H_zz. No RH assumption enters Sections 1–8. Let gamma:[0,1]→C be piecewise C1. A family of positively oriented C1 Jordan curves Gamma_s, with interiors Omega_s, has a compact swept neighborhood on which H(gamma(s),w) is nonzero on the walls. Require a continuous isotopy of the curves and no population entry or exit. Equivalently, the wall floor is positive on the compact parameterized wall; Section 2 gives a quantitative way to establish it. Every zero inside each wall is included with multiplicity. Let N be this common count and assume N≥2 when discussing the discriminant and pair matrix.

For the unchanged canonical theta source, set

\[
 A_m(T,Y)=\int_0^\infty u^m e^{Tu^2+Yu}\Phi(u)\,du,
 \quad
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
 \tag{1.1}
\]

Every summand is positive for u≥0. Double-exponential decay makes A_m finite for finite T,Y, and on Re tau≤T, |Im z|≤Y,

\[
 |\partial_\tau^r\partial_z^mH|\le A_{m+2r}(T,Y).
 \tag{1.2}
\]

This is a complete-source upper budget. It is not a lower bound for H or H_z. Any use of a truncated source must bound both the u-tail and n-tail, and use the resulting error in the strict inequalities below. The present note uses the exact source representation and heat equation, but obtains no favorable theta-specific oscillatory cancellation or reflection estimate.

## 2. Common-time moving-wall theorem

Define p_k(s)=(2pi i)^(-1) integral_Gamma_s z^k H_z/H dz. Then p_0=N, and the monic prepared polynomial P_s(z)=product_{j=1}^N(z-z_j(s)) is reconstructed by Newton identities from p_1,...,p_N, regardless of internal multiplicities. Local time neighborhoods with fixed nearby walls give holomorphic coefficients. Their values agree on overlaps, so this defines the same transported polynomial along the entire path, even when labels are permuted or collide.

The exact derivatives are

\[
 \dot p_0=0,\qquad
 \dot p_k=\frac{k\dot\gamma}{2\pi i}
 \oint_{\Gamma_s}z^{k-1}\frac{H_{zz}}H\,dz\quad(k\ge1).
 \tag{2.1}
\]

To prove this, write the curve as w(s,theta). Its motion contributes the theta derivative of w^k(H_z/H)w_s, whose closed integral is zero. The remaining term is gamma' times integral z^k partial_z(H_tau/H) dz; integrate by parts and use H_tau=-H_zz. This argument is valid with a zero-free annular neighborhood of each wall; zeros inside do not affect the differentiation. Thus no physical wall-motion term is being silently dropped: it cancels as an exact derivative for this particular holomorphic moment observable.

For a quantitative survival test, suppose a starting wall floor m_0>0 is known. Along each parameterized wall trajectory,

\[
 |H(\gamma(s),w(s,\theta))-H(\gamma(0),w(0,\theta))|
 \le\int_0^s[A_2|\dot\gamma|+A_1|w_s|]\,du.
 \tag{2.2}
\]

The A_m may vary with the local enclosing box. If the right side is uniformly <m_0, the wall survives and the complete population is constant. More generally, restart this inequality from separately certified mesh walls. This is a sufficient source-based test, not a claim that an arbitrary proposed wall passes it. With wall length ell_s, |z|≤R_s and floor m_s,

\[
 |\dot p_k|\le \frac{k|\dot\gamma|\ell_sR_s^{k-1}}{2\pi}\frac{A_2}{m_s}.
 \tag{2.3}
\]

For high bands, use a fixed centered coordinate y=(z-c)/r to avoid artificial powers of the height. If c or r varies, the coordinate derivatives must also be included. For normalized moments \(\widehat p_k=\sum_j[(z_j-c)/r]^k\),

\[
 \dot{\widehat p}_k
 =\frac{k\dot\gamma}{2\pi i r}\oint_{\Gamma_s}
 y^{k-1}\frac{H_{zz}}H\,dz
 -\frac{k\dot c}{r}\widehat p_{k-1}
 -\frac{k\dot r}{r}\widehat p_k.
 \tag{2.4}
\]

Here r is nonzero and differentiable; a positive real r is convenient for norm bounds.

## 3. Relative-value wall errors control the prepared polynomial without internal gaps

At a fixed common time, let H_* be a holomorphic reference with no zeros on Gamma, and suppose complete source estimates prove

\[
 |H/H_*-1|\le\eta<1\quad\hbox{on Gamma}.
 \tag{3.1}
\]

Rouche's theorem gives the same complete count N. The principal logarithm
ell(w)=Log(H/H_*) exists in a wall collar and is single valued around Gamma. Put

\[
 K=-\log(1-\eta),\qquad |\ell|\le K.
\]

The ratio need not be holomorphic or nonzero throughout the interior; H and H_* can have different internal zeros. Only the collar is used. For fixed c,r>0 and y=(w-c)/r, integration by parts yields the exact, gap-free relation

\[
 \boxed{\widehat p_k-\widehat p_{*,k}
 =-\frac{k}{2\pi i r}\oint_\Gamma y^{k-1}\ell(w)\,dw.}
 \tag{3.2}
\]

Consequently, if |y|≤R on Gamma,

\[
 |\widehat p_k-\widehat p_{*,k}|
 \le E_k:=\frac{k\,\operatorname{length}(\Gamma)}{2\pi r}R^{k-1}K.
 \tag{3.3}
\]

For the circle |w-c|=r this becomes E_k=kK. A known constant or polynomial part of ell should be removed before bounding (3.2): its closed integrals vanish. More generally, only the indicated contour coefficients of ell enter. Thus this estimate retains cancellations that a separate estimate of H_z/H-H_{*,z}/H_* would lose. It also uses only a C0 relative error on the same wall, whereas the naive logarithmic-derivative comparison additionally requires derivative errors or a larger analytic collar for Cauchy estimates. This is an information/stability gain, not a theta sign gain. For an explicit information-class comparison, on |z|=r take H_*=z^N and H=z^N[1+eta(z/r)^m], with 0<eta<1. Their internal prepared polynomials are identical and (3.2) is exactly zero, whereas sup_Gamma|partial_z log(H/H_*)| is at least m eta/[r(1+eta)] and is unbounded as m grows. These are admissible holomorphic snapshots (and polynomial initial data for the heat equation); the comparison is not asserted to preserve the canonical theta source. It shows concretely why differentiating a mere C0 wall-error budget is not justified.

Here is an explicit coefficient enclosure. Write the normalized monic polynomials as

\[
 \widehat P(y)=y^N+c_1y^{N-1}+\cdots+c_N,
 \quad \widehat P_*(y)=y^N+c_{*,1}y^{N-1}+\cdots+c_{*,N}.
\]

Define nonnegative numbers d_m, m≤N, by formal truncated series

\[
 \sum_{m=0}^N d_m w^m
 =\exp\left(\sum_{k=1}^N E_k w^k/k\right)-1\pmod{w^{N+1}},
 \quad d_0=0.
\]

With c_{*,0}=1, one has

\[
 \boxed{|c_m-c_{*,m}|\le C_m:=\sum_{j=0}^m|c_{*,j}|d_{m-j}.}
 \tag{3.4}
\]

Indeed product_j(1-y_jw)=exp(-sum_k p_hat_k w^k/k), so the actual generating function is the reference one times exp(-sum delta p_hat_k w^k/k). The exponential coefficientwise majorant proves (3.4); moments above N cannot affect the first N coefficients. The formula remains valid through collisions. If all reference roots satisfy |y_j|≤1, binomial(N,j) may replace |c_{*,j}|, though using the actual coefficients is usually sharper.

Neither (3.3) nor (3.4) is automatically useful uniformly as N grows. Their rank dependence is explicit, and an exponential coefficient majorant can be expensive. No high-rank control is claimed from a fixed relative wall error.

## 4. Discriminant transport and a gap-free enclosure

Let Delta=product_{i<j}(z_j-z_i)^2. It is a holomorphic function of the prepared coefficients, so it continues through every internal collision while the complete wall survives. On regular root-label charts, factor H=UP with U nonvanishing inside the wall and put b=partial_z log U. Heat-root differentiation gives

\[
 z_i'=2\sum_{j\ne i}(z_i-z_j)^{-1}+2b_i,
\]
\[
 \frac d{ds}\log\Delta
 =\dot\gamma\left[8\sum_{i<j}(z_i-z_j)^{-2}
 +4\sum_{i<j}\frac{b_j-b_i}{z_j-z_i}\right].
 \tag{4.1}
\]

The triple sums cancel algebraically, without a reality assumption. At a zero of Delta the logarithmic differential has its usual integer residue, so a curved detour retains the event count. A global log branch is not assumed. Along a closed event-free loop the labels may permute while Delta returns to itself.

For an enclosure not containing an inverse internal gap, let S_* be the (2N-1)-square Sylvester matrix of the normalized monic P_hat_* and its derivative, and let M=2N-1. From (3.4) define

\[
 \varepsilon_S^2
 =\sum_{j=1}^N[(N-1)+N(N-j)^2]C_j^2.
 \tag{4.2}
\]

This is the squared Frobenius bound for S-S_*: there are N-1 shifted P rows and N shifted P' rows. The determinant derivative and adjugate norm yield

\[
 \boxed{|\widehat\Delta-\widehat\Delta_*|
 \le E_\Delta:=M\varepsilon_S(\|S_*\|_2+\varepsilon_S)^{M-1}.}
 \tag{4.3}
\]

The sign relating the resultant to the discriminant has modulus one. In unscaled coordinates Delta=r^{N(N-1)} Delta_hat. Formula (4.3) follows by integrating d/dv det(S_*+vE); |Tr(adj(A)E)|≤M||A||_2^{M-1}||E||_2, valid even when A is singular.

Thus |Delta_hat_*|>E_Delta proves absence of an internal collision on that slice, and a uniform version proves it on a path. It is not circular: the reference discriminant and the wall error are separately supplied data. But it may be extremely conservative for large N or a small reference discriminant. When the reference itself collides, (4.3) remains an absolute enclosure and does not certify noncollision. One may instead enclose the exact resultant with correlated coefficients. The scalar determinant estimate is a transparent fallback, not an optimal conditioning claim.

## 5. The filtered observable needs a separate resolvent condition

On simple-root segments set

\[
 L=\sum_{i<j}(z_i-z_j)^{-2}(e_i-e_j)(e_i-e_j)^T,
 \quad R_a=(I+aL)^{-1},\quad q_a=\operatorname{Tr}(I-R_a).
\]

Root permutations conjugate L and preserve q_a. Its exact common-time transport is

\[
 \dot q_a=\operatorname{Tr}\{R_a[\dot aL+a\dot\gamma L_\tau]R_a\}.
 \tag{5.1}
\]

For a complex path, require delta(s)=sigma_min(I+aL)>0. Then

\[
 |\dot q_a|\le N\delta^{-2}
 \|\dot aL+a\dot\gamma L_\tau\|_2.
 \tag{5.2}
\]

The coupled norm in (5.2) is deliberate. Replacing it by |a'| ||L||+|a gamma'| ||L_tau|| loses exact heat-birth cancellation. Singular values, rather than distances from the eigenvalues alone, are required for a potentially nonnormal complex matrix. On a distinct real-root slice with a≥0, R_a has norm≤1; that positivity cannot be transported to a general complex path.

Here is a fully explicit stability alternative to integrating (5.2). Suppose disjoint reference disks centered at w_i contain exactly one actual root z_i each, and source Rouche tests establish |z_i-w_i|≤rho_i. Let d_ij=w_i-w_j and rho_ij=rho_i+rho_j<|d_ij|. Define

\[
 E_{ij}=\frac{\rho_{ij}(2|d_{ij}|+\rho_{ij})}
 {|d_{ij}|^2(|d_{ij}|-\rho_{ij})^2},\qquad
 E_L=2\max_i\sum_{j\ne i}E_{ij}.
 \tag{5.3}
\]

The difference-of-reciprocals identity bounds each edge error by E_ij. Absolute row and column sums give ||L-L_*||_2≤E_L. If

\[
 \delta_*:=\sigma_{\min}(I+aL_*)> |a|E_L,
 \tag{5.4}
\]

then the actual resolvent exists, delta≥delta_*-|a|E_L, and

\[
 \boxed{|q_a-q_{a,*}|\le
 \frac{N|a|E_L}{\delta_*(\delta_*-|a|E_L)}.}
 \tag{5.5}
\]

This is the resolvent identity followed by |Tr A|≤N||A||_2. Each disk's boundary test includes the complete exterior field: it does not replace H by the internal polynomial without an error. Unlike Sections 3–4, this estimate pays internal root isolation; that limitation is explicit. The whole-cluster wall alone does not imply (5.4).

As a symmetric rational function of the roots, q_a is rational in the prepared coefficients and a, hence meromorphic through internal discriminant zeros when a is holomorphic in time. Removability requires a separate local calculation. For a Hermite heat birth of multiplicity m at tau=0 and a=4tau, the limit is

\[
 \lim_{t\downarrow0}q_{4t}=\sum_{k=1}^{m-1}\frac{k}{k+1}=m-H_m,
 \tag{5.6}
\]

for the isolated m-root cluster; other separated finite clusters add their own limits. This finite nonzero signature follows from Note 06's spectrum and is not erased by regularization.

## 6. A height graph is a different, generally nonholomorphic field

Let theta(x)=h(x)+i sigma, with h real C2 and sigma fixed (C1 suffices for the degree and contraction conclusions), and define F(z)=H(theta(Re z),z) on a planar domain Omega. The proposed negative graph is h=-epsilon. Wirtinger differentiation gives

\[
 F_z=H_z+\tfrac12h'H_\tau=H_z-\tfrac12h'H_{zz},
 \qquad F_{\bar z}=\tfrac12h'H_\tau=-\tfrac12h'H_{zz},
 \tag{6.1}
\]
\[
 dF/F=(H_z/H)dz-h'(x)(H_{zz}/H)dx.
 \tag{6.2}
\]

Thus the winding on a zero-free graph wall is

\[
 \deg(F,\Omega,0)=\frac1{2\pi i}\oint_{\partial\Omega}
 [(H_z/H)dz-h'(H_{zz}/H)dx].
 \tag{6.3}
\]

All H-values here are sampled at theta(x). This is the topological degree of F. It equals an unsigned zero count only after proving positive local orientations (or otherwise accounting for negative indices). At a graph zero with H_z≠0, write v=H_zz/H_z, the frozen-time root velocity. Its real Jacobian is

\[
 J_F=|H_z|^2\Re(1-h'v).
 \tag{6.4}
\]

Indeed F_x=H_z(1-h'v), F_y=iH_z and J=Im(conj(F_x)F_y). The sufficient transversality/orientation condition |h'v|<1 gives J>0. A zero with H_z=0 has J=0; graph sampling does not regularize an actual multiple zero into this transverse theorem.

There is also a bulk correction for moments. If all graph zeros are isolated and transverse, Stokes' theorem on Omega with small disks removed gives, for k≥1,

\[
 \boxed{\sum_{F(\zeta)=0}\operatorname{ind}_\zeta(F)\zeta^k
 =\frac1{2\pi i}\oint_{\partial\Omega}z^k\frac{dF}{F}
 +\frac{k}{\pi}\int_\Omega z^{k-1}\frac{F_{\bar z}}F\,dA.}
 \tag{6.5}
\]

The local integrand is O(1/|z-zeta|) and is integrable at transverse zeros. The sign follows from dz wedge dbar z=-2i dA. Equation (6.5), together with (6.1), displays both the slope term on the boundary and the nonholomorphic area term. Using only the common-time contour moment (2.1) on this graph would miss both. In particular, the graph samples do not inherit a holomorphic prepared polynomial in a single time variable or the common-time evolution equation for L.

A finite source-based degree comparison is possible without resolving graph zeros. For a constant tau_0=u_0+i sigma, assume |h(x)-u_0|≤epsilon_tau on the boundary, all interpolating times lie in the source box, and

\[
 \min_{\partial\Omega}|H(\tau_0,z)|>
 \epsilon_\tau A_2.
 \tag{6.6}
\]

The straight time homotopy has no boundary zero, by (1.2), hence the graph degree equals the complete frozen-time zero count. To turn this into an unsigned count one must additionally establish positive orientation of all graph zeros. Even then it provides no simplicity exclusion at the frozen endpoint.

## 7. A complete graph-population comparison with explicit slope loss

The following stronger finite lemma makes mixed-time sampling reviewable. Fix an interval I=[u_-,u_+] and the horizontal time segment u+i sigma. Suppose a single fixed spatial domain has a zero-free wall for every u∈I, and its complete N roots have simple C1 branches z_i(u). Root simplicity, continuation and completeness must be certified, for example by disjoint moving disks; they are not consequences of a wall floor alone. Assume h(Re z) belongs to I for every z in the closed spatial domain, and

\[
 \kappa_i:=\sup_{u\in I}|h'(\Re z_i(u))\Re z_i'(u)|<1.
 \tag{7.1}
\]

Then the scalar map u↦h(Re z_i(u)) is a contraction of I into itself. There is exactly one graph zero zeta_i=z_i(u_i) on each branch, and every graph zero in the domain is one of these. At it, 1-h' Re v>0, so the orientation is positive. This criterion can be weaker than |h'v|<1; both imply the necessary positivity.

Let u_0∈I, V_i=sup_I |z_i'|, and delta_i=|h(Re z_i(u_0))-u_0|. Then

\[
 |u_i-u_0|\le\frac{\delta_i}{1-\kappa_i},\qquad
 \boxed{|\zeta_i-z_i(u_0)|\le
 \frac{V_i\delta_i}{1-\kappa_i}.}
 \tag{7.2}
\]

The first inequality follows by inserting u_0 in the fixed-point equation and using the contraction bound; integration of z_i' gives the second. If a global time-deviation bound is smaller, use its minimum with the first bound. Source enclosures of |H_zz|/|H_z| on the root tubes pay V_i. Equations (5.3)–(5.5), with rho_i from (7.2), then compare the mixed-time matrix with its common-time matrix, provided the separation and resolvent tests pass.

This is a genuine graph-error estimate with a visible amplification 1/(1-kappa_i). It also explains the limit of the construction: it assumes an already simple common-time tube and becomes unstable near a tangency. It cannot establish endpoint simplicity by presupposing that same simple tube through the endpoint. The RH-conditional matching consumer in Note 06 applies to a common positive time; a mixed-time q may be used only after paying a comparison such as (5.5). Real mixed-time roots alone do not justify importing the common-time gap compression.

For piecewise constant bands, sum the complete oriented boundaries before estimating. Shared interfaces cancel only for identical time, field and orientation. If two neighboring bands use different times, retain the connecting face. Equations (6.2) and (7.2) quantify what a smooth interpolation adds; they do not authorize discarding a join.

## 8. Matched direct comparison and the physical-cap distinction

At a given endpoint wall, the same relative source bound (3.1) gives the direct coefficient/discriminant enclosure (3.2)–(4.3), whether or not the endpoint was reached along a curved path. For a shared holomorphic finite coefficient-error model on a simply connected event-free time domain, coefficient transport has path-independent endpoint values, so changing the path does not change the exact propagated coefficient uncertainty. This is a scoped equality of information, not a universal comparison of source acquisition cost.

If instead one encloses a moment-derivative residual by a uniform scalar allowance e, a path of length ell_gamma pays ell_gamma e, whereas a straight admissible path pays its length times e. The same statement applies to a q-derivative residual on a domain satisfying the independent resolvent condition. A detour can still win when source errors or resolvent constants are substantially better on it; the actual integrated budget must show this. Neither shorter source tail estimates alone nor analytic path equality supplies that gain. The relative-wall method improves on separately differentiated errors under the stated C0 information, but an equally informed direct wall method receives exactly the same improvement.

No physical cap is used to prove this note. Its discriminant is not the entire physical root product. For H=UP,

\[
 \mathscr D=\prod_i H_z(\tau,z_i)
 =(-1)^{N(N-1)/2}\Delta\prod_iU(\tau,z_i).
 \tag{8.1}
\]

Consequently a physical-cap application must retain this analytic factor and the full complement and joining faces specified in [Note 03](03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md). Equation (2.1)'s moment-wall cancellation is not a proof that those physical spatial faces have zero flux.

## 9. Controls, verification and scope

The following controls were checked independently during this derivation. They are tests of the finite formulas and failure modes, not evidence for an RH-equivalent claim.

1. **Double and triple heat births.** H=z²-2tau has Delta=8tau and q_(4tau)=1/2; H=z³-6tau z gives q_(4tau)=7/6. Thus the discriminant can pass through zero while the bounded filter retains a nonzero collision signature. The coupled derivative in (5.1) vanishes in these pure scaling models, whereas separately bounding the two terms would give a spurious nonzero cost.
2. **A resolvent pole without a collision.** For H=z²-1-2tau, q_(4tau)=2tau/(1+4tau). The pole at tau=-1/4 occurs with distinct roots; the discriminant vanishes at -1/2. Therefore a discriminant-only contour test cannot replace (5.4).
3. **Graph tangency with simple frozen roots.** For H=z²-9-2tau and h(x)=(x²-9)/2 on 1<x<2, F(x)=0 along the entire real interval. All these frozen-time roots are simple, all sampled times are negative, and h'v=1. This falsifies any unqualified claim that simple frozen roots imply isolated graph zeros or holomorphic graph counting.
4. **Negative graph orientation.** For H=z²-1-2tau and h(x)=x²-1, the graph zero z=1 has H_z=2, h'v=2, and J_F=-4. A small surrounding disk has degree -1 although it contains one graph zero. The correction in (6.3) is essential.
5. **Exterior-force control.** The stationary sine heat field satisfies the transport and wall theorems. Its nonzero exterior unit must be retained in (4.1); finite internal roots by themselves do not solve the unforced heat polynomial equation.
6. **Published source controls.** Euler-factor, weighted-square, reflected, positive-primitive and close-endpoint controls all satisfy the generic local holomorphic heat formulas when their specified finite walls and charts exist. None is rejected by the estimates merely because it differs from theta. On a path including a collision, any claimed positive discriminant lower bound must fail; at a graph tangency the graph criterion fails; a simplicity-producing upper filter threshold fails on a matching collision population. No global real-root premise is assigned to weighted-square or reflected controls without proof. The canonical-source identity is absent in the controls listed in the register, but this note has not extracted a quantitative theta advantage from that absence.

A small supporting check also evaluates (3.4), (4.3) and (5.5) on declared finite polynomial populations. Its floating matrix calculations are algebra diagnostics, not certified enclosures. The analytic proofs above carry the conclusions.

**Unpaid application data:** a prescribed theta population and full source error that pass (2.2) or (3.1); reference coefficient/discriminant data; any root disks and singular-value floor needed by (5.4); and, for a smooth graph, either degree/orientation data or the complete contraction hypotheses (7.1). Uniform rank/height scaling and a q bound strong enough for either simplicity target remain open. The scoped comparison in Section 8 excludes an advantage from path relabeling with identical analytic information; it does not exclude better source estimates on a genuinely better contour.
