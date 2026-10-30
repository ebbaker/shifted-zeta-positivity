# Fixed flow boundedness and local collision geometry

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **xhigh**, Investigation05 **chat0045**, *Review fixed coefficient research*.

**Status: explanatory derivation from the existing fixed-flow estimates, with same-assistant checking only.** Every fixed finite c>0 gives a global bounded flow, including at a collision. The collision removes its stationary component. Uniform noncollapse and finite stationary energy matching provide exact alternative statements. Regional noncollapse is logically equivalent to nonvanishing on the chosen compact set, but is an analytically distinct proof strategy from nonlinear feedback control or pointwise coefficient matching. No theta lower estimate is derived here. This clarification does not execute FCG-B03 R2 or select a new mechanism.

The source estimates are the [fixed-compression note][fixed], [parameter-family note][family], [B01 comparison][b01], and [stationary partition-function calculation][stationary]. Follow the [result index][results], especially [local collision geometry][geometry], and the [avoid index][avoid], especially [reformulations][a01], [scoped conclusions][a07] and [circular constants][a14].

## 1. Fixed finite compression gives bounded evolution at every mark

Let p=(T,A), J(p)=(H,H_A), and use the complete prepared source and original drift:

\[
 \partial_sW_c=\Delta W_c+c\operatorname{div}(vW_c),\qquad
 v(X)=X+\frac{X}{1+|X|^2},\qquad c>0.
\]

The same c is fixed across time and physical parameters. On a compact physical set K in the prepared moment domain, let

\[
 \ell_K=\sup_{p\in K}\|W_0(p)\|_1,\qquad
 E_{0,K}=\sup_{p\in K}\|W_0(p)\|_2^2.
\]

Both are finite. Positivity and conservation of the common propagator imply ||W_c(s;p)||_1<=ell_K. With E_c=||W_c||_2^2, G_c=||grad W_c||_2^2 and d=div v<=6, the inherited Nash inequality gives

\[
 E_c'=-2G_c+c\int d|W_c|^2
 \le-2c_N E_c^{5/3}\ell_K^{-4/3}+6cE_c,
 \qquad c_N=\frac35(6\pi^2)^{2/3}.
\]

Therefore, for nontrivial data,

\[
 \sup_{s\ge0,\,p\in K}E_c(s;p)
 \le \overline E_{K,c}:=
 \max\left\{E_{0,K},\left(\frac{3c}{c_N}\right)^{3/2}\ell_K^2\right\}<\infty.
 \tag{1}
\]

The zero-data case is immediate. The inherited gradient inequality
G_c'<=-2||Delta W_c||_2^2+10cG_c+30cE_c, together with G_c^2<=E_c||Delta W_c||_2^2, supplies a uniform H1 bound as well. Global smooth finite-time evolution follows from the fixed linear equation and the prepared smooth data, as in [the fixed-flow proof][fixed]. None of these estimates assumes J!=0.

Consequently, the proposed distinction based solely on finite or bounded fixed-c evolution is false: the boundedness property holds for every finite positive c on both sides of a collision.

## 2. The collision removes the stationary component

Define

\[
 \mathcal V(X)=\tfrac12\bigl(|X|^2+\log(1+|X|^2)\bigr),\qquad
 p_c=Z(c)^{-1}e^{-c\mathcal V},\qquad Q(c)=\|p_c\|_2^2>0.
\]

The conserved vector mass is int W_c=J, and the inherited compact-uniform estimate is

\[
 W_c(s;p)=J(p)p_c+R_c(s;p),\qquad
 \sup_K\|\partial_p^\nu R_c(s;p)\|_2^2
 \le C_{K,\nu,c}e^{-cs/2}.
 \tag{2}
\]

At any collision p0, including higher multiplicity, J(p0)=0, so E_c(s;p0)<=C exp(-cs/2) tends to zero. At a noncollision, E_c tends to Q(c)|J|^2>0. The scalar comparison carrier can retain positive mass while this signed vector field decays; the two masses must not be identified.

Changing c changes the drift strength, stationary spatial profile, and quantitative relaxation bounds. Larger c gives more weight to smaller values of V; indeed d E_{p_c}[V]/dc=-Var_{p_c}(V)<0. The squared-error rate in (2) is proportional to c, but its constants also depend on c, so (2) does not assert monotonic transient norms as c varies. For every c, the coefficient of the stationary profile remains the same J. No finite c restores a missing stationary component.

## 3. Local energy and sensitivity at a nondegenerate double

Take a small closed parameter ball K around an isolated collision p0 with no other zeros of J. This means collisions, not ordinary simple zeros of H. Isolation alone does not imply nondegeneracy. In this section additionally assume

\[
 b=H_{AA}(p_0)\ne0,\qquad d_0=H_{AT}(p_0).
\]

Because H_T=-H_AA,

\[
 J(p_0+\delta p)=M\delta p+O(|\delta p|^2),\qquad
 M=\begin{pmatrix}-b&0\\d_0&b\end{pmatrix},\qquad \det M=-b^2.
 \tag{3}
\]

Write delta p=(t,a). Equation (2) gives the limiting energy

\[
 E_{c,\infty}(p_0+(t,a))
 =Q(c)\left[b^2t^2+(d_0t+ba)^2\right]+O(|(t,a)|^3).
 \tag{4}
\]

Thus the limiting energy has a strict nondegenerate quadratic minimum at zero. Its Hessian is 2Q(c)M^T M, positive definite. Equivalently, |J(p)| is bounded above and below by positive multiples of |p-p0| nearby. These claims concern the stationary limit; a finite-time energy surface need not attain zero at p0.

There is also nonzero absolute parameter response at the event:

\[
 \|\partial_T W_{c,\infty}(p_0)\|_2^2+
 \|\partial_A W_{c,\infty}(p_0)\|_2^2
 =Q(c)(2b^2+d_0^2)>0.
\]

Consequently the ratio of this response energy to E_{c,infinity}(p) is comparable to |p-p0|^{-2} on the punctured ball. This is relative sensitivity; the field and its unnormalized parameter derivatives remain regular. It is the local form of B01's C02 signature. B01's C01 predecessor pole and the index -1 give further, already recorded signatures. For an isolated higher-order event, vanishing stationary mass still holds, but the quadratic formula and exponents here require replacement by the appropriate higher-order expansion.

## 4. An exact uniform noncollapse criterion

For a compact K in the prepared domain, the following statements are equivalent:

1. J(p)!=0 for every p in K.
2. For some fixed c>0 there is epsilon>0 with E_c(s;p)>=epsilon for every s>=0 and p in K.
3. The same property holds for every fixed c>0, with epsilon allowed to depend on c and K.

**Proof.** Under (1), compactness gives mu_K=min_K|J|>0. By (2), choose S so that ||R_c||_2<=sqrt(Q(c)) mu_K/2 uniformly on K for s>=S. The reverse triangle inequality gives E_c>=Q(c)mu_K^2/4 there. On [0,S] times K, E_c is continuous and strictly positive: if W_c were zero in L2, its conserved mass would be zero, contrary to J!=0. Its compact minimum is therefore positive. This proves (1) implies (3), and (3) implies (2) is immediate. If J(p0)=0 anywhere in K, equation (2) forces E_c(s;p0) to zero for every c, contradicting (2). This proves the converse.

Together with (1), a collision-free compact family therefore has energy bounded above and bounded away from zero for all auxiliary time. A ball containing a collision still has the upper bound but cannot have the positive lower bound. The punctured ball also has no uniform lower bound over all its parameters and all times, since its limiting energy approaches zero at the removed center. Every closed annulus avoiding the center does have such a bound.

This equivalence uses nonvanishing to prove its floor. It cannot establish theta nonvanishing without an additional, independently derived source estimate.

## 5. A finite coefficient for stationary energy matching

A second precise version of the user's intuition asks for the eventual energy to equal a prescribed E_tar(p)>0, for example the actual initial energy E0(p). At each mark the condition is

\[
 |J(p)|^2Q(c_*(p))=E_{\rm tar}(p).
 \tag{5}
\]

For the unit-mass density used here, [Note90][stationary] gives

\[
 Q(c)=\frac{Z(2c)}{Z(c)^2},\qquad Q'(c)>0,\qquad
 (c/(8\pi))^{3/2}\le Q(c)\le(c/\pi)^{3/2}.
\]

The derivative is positive because (log Q)'=2(E_{p_c}[V]-E_{p_{2c}}[V])>0. Hence Q maps (0,infinity) continuously and strictly increasingly onto (0,infinity). If J!=0, (5) has a unique finite solution and

\[
 \pi\left(\frac{E_{\rm tar}}{|J|^2}\right)^{2/3}
 \le c_*\le
 8\pi\left(\frac{E_{\rm tar}}{|J|^2}\right)^{2/3}.
 \tag{6}
\]

At a collision it has no finite solution. If E_tar is continuous and strictly positive near a nondegenerate double, (3) and (6) give

\[
 c_*(p)\asymp |p-p_0|^{-4/3}.
 \tag{7}
\]

Here the comparison constants are uniform on a sufficiently small punctured ball. For E_tar=E0, positivity and continuity of the prepared initial energy are inherited from the nonzero complete source and Gaussian preparation. On a compact collision-free region, c_*(p) stays bounded, but generally varies with p. It is not one common coefficient giving exact energy matching at all marks, and matching the limit does not preserve energy along the transient trajectory.

The singular object in (7) is the parameter-dependent matching coefficient, not any fixed-c solution. Establishing its finiteness from |J|>0 restates noncollision. A theta-specific independent upper bound for it would require new information; none is obtained by defining it.

## 6. Relation to the normalized flow and controls

The original feedback alpha(s)=2||grad W||_2^2/int d|W|^2 enforces E(s)=E0. Its stated collision theorem gives finite-time breakdown at J=0. Freezing alpha removes that constraint and permits decay. The originally proposed global-existence dichotomy holds for the normalized equation. The revised proposal of one common fixed coefficient and a uniform lower bound over a parameter ball is a separate regional problem. It does not require matching a coefficient at each point or controlling the nonlinear feedback trajectory; see the author clarification below.

The Gaussian-polynomial control at (1/4,2 sqrt(6)) and the three-positive-square control at its certified high-frequency event satisfy these prepared-class hypotheses and are nondegenerate doubles. They have bounded fixed flows, vanishing stationary fields, the same quadratic energy minimum, divergent relative sensitivity and divergent matching coefficients. The former fails theta's complete arithmetic source relation; the latter fails unit coefficients and full reflection. No excluding theta premise is supplied by these generic diagnostics. The [wider control register][controls] retains its separate domains and multiplicity qualifications.

The new content is the explicit local expansion and compact noncollapse clarification drawn from inherited estimates. This is not a theta exclusion, all-multiplicity local expansion, physical-domain extension or independent assessment. [Progress06][progress] retains FCG-B03 R2 as ready and unstarted.


## 7. Regional noncollapse is a distinct proof strategy

**Author clarification, 30 October 2026, same chat0045, actual gpt-6-astra / xhigh.** The author's proposal seeks a ball and one finite coefficient giving a uniform lower bound across that ball. The previous discussion blurred logical equivalence of the eventual conclusion with equivalence of the analytical problem. Fixed-flow upper boundedness remains automatic at collisions, but this does not dismiss the regional lower-bound strategy.

For a closed parameter ball B in the prepared domain, the intended target can be written

\[
 \exists\ c_B\in(0,\infty),\ \delta_B>0,\ S_B<\infty:
 \quad \|P_s^{c_B}W_0(p)\|_2^2\ge\delta_B
 \quad\text{for every }p\in B\text{ and }s\ge S_B.
 \tag{8}
\]

All three constants are common across B. A collision in B defeats (8) for every finite c_B. A lower bound derived from the complete theta source would therefore exclude collisions in B. It would not assume such exclusion merely because the converse implication can be proved using compactness. The compactness proof in Section 4 establishes the equivalence; it does not supply the proposed source-derived proof of (8).

This differs from evolving the nonlinear feedback at each mark and bounding its response. It also differs from the parameter-dependent stationary matching coefficient c_*(p) in Section 5. Equation (8) asks for one common c_B and a lower bound, without requiring energy conservation or exact stationary matching anywhere.

The distinction changes the available calculations. The same spatial operator L_c acts at every physical parameter, so

\[
 \partial_s\partial_p^\nu W_c=L_c\partial_p^\nu W_c,
 \qquad U_{c,T}=-U_{c,AA}.
\]

For a marked nonlinear feedback family, differentiation instead includes the additional term (partial_p alpha^p) div(v W^p). The fixed family also has one common spatial overlap kernel in the complete-source bilinear formulas. These facts permit the investigation of joint parameter estimates, complete-source identities, and common propagation arguments without differentiating an unknown feedback coefficient.

It is therefore plausible that the fixed-family formulation could make some theta-specific information easier to use. No such comparative advantage has yet been established. The endpoint is still Q(c_B)|J(p)|^2; changing representation supplies no automatic lower bound. Nevertheless, equivalence to nonvanishing is a classification of the target, not a reason to identify the proof strategy with nonlinear feedback or reject it. A useful new mechanism would explain how the complete source and parameter relations prove (8), or another uniform collision-incompatible estimate, without inserting the unknown positive minimum of |J|.

A positive boundary or parameter-averaged bound would not alone establish (8), since either can coexist with an isolated interior zero. The Gaussian-polynomial and weighted-square events continue to defeat a source-independent regional lower bound in their respective moment domains. They do not refute a theta-specific argument using premises they fail.

The author's regional interpretation is retained for subsequent conceptual work. This clarification does not execute the bounded R2 mechanism comparison, select a new candidate, or assess its feasibility.


## 8. Nonpositive coefficients and a source derived positivity certificate

30 October 2026, same chat0045, actual **gpt-6-astra / xhigh**. The regional positive lower-bound conclusion changes for c<=0, although global finite-time regularity of the fixed linear equation remains. These elementary estimates concern the same original drift and complete prepared data.

At c=0 the equation is ordinary heat flow. Young's inequality on R3 gives, for s>0,

\[
 E_0(s;p)=\|K_s*W_0(p)\|_2^2
 \le(8\pi s)^{-3/2}\|W_0(p)\|_1^2\longrightarrow0.
 \tag{9}
\]

Here the subscript 0 denotes the fixed coefficient c=0, not initial time. The estimate is uniform on a compact parameter ball with bounded initial L1 norms, irrespective of J.

For c<0, write d=div v>=3. Multiplication by negative c reverses the useful comparison, so the exact energy identity gives

\[
 E_c'=-2G_c+c\int d|W_c|^2\le3cE_c,
 \qquad E_c(s;p)\le E_c(0;p)e^{3cs}\longrightarrow0.
 \tag{10}
\]

This is again uniform on a compact parameter ball with bounded initial energy. The drift velocity -cv points outward for negative c. The globally Lipschitz velocity permits global finite-time evolution; the energy decays. Signed mass is conserved while spreading over space, which is compatible with vanishing L2 norm. The expression exp(-cV) is not integrable for c<=0, so the normalized stationary density p_c and its partition-function formulas from the positive-c analysis are unavailable there.

Thus c<=0 forces decay even at noncolliding marks. Positive c is necessary for the regional noncollapse property, but it is not by itself sufficient: colliding controls still decay for every positive c. For c>0 the inherited limit distinguishes J=0 from J!=0.

The author's suggestion of an analytically defined coefficient c_B whose positivity is the difficult source estimate is a legitimate possible research design. It requires a theorem connecting this particular source-defined coefficient to the regional lower bound. One possible logical structure is: define a finite real c_B from complete theta data on B, prove a conditional regional estimate giving a positive lower bound when c_B>0, and establish c_B>0 from that data. The conditional estimate and the positivity proof are separate obligations; neither is supplied by choosing a convenient positive constant such as 1.

Such a coefficient could encode a useful signed source inequality. Its defining formula must not assume min_B|J|>0 or use a normalized p_c before positivity and integrability are established. These are scope and dependency requirements, not a requirement to solve the sign problem before exploring the design. Gaussian-polynomial and weighted-square controls satisfy the decay laws above; any proposed positivity certificate needs a premise or quantitative condition that they fail. No concrete certificate formula or new execution task is selected by this observation.

[fixed]: ../CHAT0042_FIXED_COMPRESSION_AND_NORMALIZATION_COMPARISON_20261030.md
[family]: ../CHAT0042_FIXED_FLOW_PARAMETER_FAMILY_AND_COLLISION_INDEX_20261030.md
[b01]: 01_COLLISION_SIGNATURE_COMPARISON_20261030.md
[stationary]: ../90_CARRIER_FEEDBACK_DEFECT_AND_STATIONARY_CANDIDATE_R13_20261029.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[results]: ../../../../../result-summaries/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
