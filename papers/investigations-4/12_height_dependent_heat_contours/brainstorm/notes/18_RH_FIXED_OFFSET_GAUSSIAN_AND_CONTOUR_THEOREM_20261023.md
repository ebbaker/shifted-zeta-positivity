# RH fixed-offset Gaussian comparison and conserved contour continuation

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Status:** analytic proof under initial RH, allowing all multiplicities, at the fixed-offset and real-negative-time scope below. The proof and its limits receive separate same-model internal review in [Review 09](../reviews/09_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_REVIEW_20261023.md); no specialist review or novelty claim. This resolves the concrete candidate in [Continuation 17](17_CONTINUATION_CONSERVED_SPATIAL_CONTOURS_20261023.md). It supplies a canonical wall and material graph without assuming a negative-time zero-free tube. It does not supply a simplicity estimate.

The classification is a **quantitative conditional intermediate result**, not an RH criterion. Consult the [result index](../../../../../result-summaries/README.md), [local-geometry summary](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../../avoid/README.md), [target classification](../../../../../avoid/01_restating_the_target.md), [coupled-estimate discipline](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md). The controls in Section 8 are part of the result's scope, not optional diagnostics.

## 1. The comparison theorem

Write

\[
 F(z)=H(0,z)=\tfrac18\xi(\tfrac12+iz/2),\qquad H_t=-H_{zz},
 \qquad p(z)=F'(z)/F(z).
\]

Assume RH for F, with zeros counted with multiplicity. Fix 0<b_-<b_+, c>0, and put L=log Y. Uniformly for

\[
 Y\le\Re z\le2Y,\quad b_-\le\Im z\le b_+,\quad
 0\le s\le cL^{-2},
\]

as Y tends to infinity,

\[
 \boxed{\frac{H(-s,z)}{F(z)e^{s p(z)^2}}
 =1+s p'(z)\{1+2s p(z)^2\}+O(L^{-2}).} \tag{1}
\]

In particular,

\[
 H(-s,z)=F(z)e^{s p(z)^2}\{1+O(L^{-1})\}. \tag{2}
\]

The same statements hold on any fixed enlarged positive-offset strip and any fixed horizontal end extensions, with changed constants. For each fixed nonnegative integer k, the O(L^-2) remainder in (1) has kth spatial derivative O_k(L^-2) on a smaller strip with a fixed positive margin. The analogous remainder in (2) has derivatives O_k(L^-1). All constants and the sufficiently-large-Y threshold depend only on c, the chosen strips/margins and k; no numerical threshold is asserted. At s=0 the ratios equal 1 and the remainders are exactly zero.

For large enough Y this acquires nonvanishing throughout the stated region, and

\[
 |H(-s,z)|\ge \tfrac12 e^{-C^2c}|F(z)|>0, \tag{3}
\]

where |p|<=CL on the enlarged strip. The factor in (3) is relative to the complete initial field, which can itself be exponentially small. Initial RH is the only zero-location assumption; no simplicity or negative-time nonvanishing is assumed.

A useful consequence, writing p_s(z)=H_z(-s,z)/H(-s,z), is

\[
 p_s=p+2spp'+O(L^{-1}),\qquad
 \partial_zp_s=p'+2s\{(p')^2+pp''\}+O(L^{-1})=p'+O(1).
 \tag{4}
\]

## 2. Initial bounds from the complete zero set

The classical order-one product for the even entire F gives, under RH,

\[
 F(z)=F(0)\prod_{\lambda>0}(1-z^2/\lambda^2),\qquad
 p(z)=\sum_{\lambda>0}\left(\frac1{z-\lambda}+\frac1{z+\lambda}\right).
 \tag{5}
\]

Here the positive lambdas are twice the positive zeta ordinates, repeated according to multiplicity; the displayed pairing fixes the convergence. Evenness removes the possible linear exponential in the order-one product. In particular, for k>=1,

\[
 p^{(k)}(z)=(-1)^k k!\sum_{\lambda\in\mathcal Z}(z-\lambda)^{-k-1},
 \tag{6}
\]

with absolute local uniform convergence off the real axis. The signed multiset mathcal Z includes both signs.

The Riemann--von Mangoldt estimate, in this normalization, is

\[
 N_F(X)=\#\{0<\lambda\le X\}
 =\frac X{4\pi}\log\frac X{4\pi}-\frac X{4\pi}+O(\log(2+X)).
 \tag{7}
\]

Endpoint conventions change the stated remainder at most by its order. In particular every unit real interval centered near v contains O(log(2+|v|)) zeros, including multiplicity. For y in a compact subinterval of (0,infinity), partitioning into unit intervals about x shows

\[
 \sum_{\lambda\in\mathcal Z}|x+iy-\lambda|^{-k-1}
 \le C_k\sum_{n\ge0}\frac{\log(2+|x|+n)}{(1+n)^{k+1}}
 \le C_k\log(2+|x|),\quad k\ge1. \tag{8}
\]

Constants absorb the finitely many central intervals and the positive lower bound on y. Thus p', p'', and every fixed higher derivative are O(log(2+|x|)). This does not require a bound on multiplicities sharper than (7).

To bound p itself without taking the absolute value of an unpaired sum, fix B>max{b_++1,1}. At z=x+iB, the functional equation writes

\[
 8F(z)=\xi(w),\qquad w=(1+B)/2-ix/2.
\]

The real part of w exceeds 1 by a fixed amount. The absolutely convergent Euler logarithmic derivative, the polynomial factors in xi, and the digamma estimate give

\[
 p(x+iB)=-\frac i2\left[\frac1w+\frac1{w-1}
 -\frac12\log\pi+\frac12\psi(w/2)+\frac{\zeta'}\zeta(w)\right]
 =O(\log(2+|x|)). \tag{9}
\]

For bounded x use compactness and Euler nonvanishing. Integrating p' down the vertical segment from B to the chosen y and applying (8) proves

\[
 \boxed{|p(x+iy)|+|p'(x+iy)|+|p''(x+iy)|
 \le C\log(2+|x|)} \tag{10}
\]

on every fixed positive-offset strip, for all real x. Any further fixed number of derivatives obeys the same bound. The Euler anchor is used only to initialize p; the passage into the critical strip is paid by RH and (8), not by continuing an Euler product there.

Classical inputs were checked against [Elkies's course notes](https://people.math.harvard.edu/~elkies/M259.06/zeta2.pdf), equations (1)--(4), and [DLMF 25.4](https://dlmf.nist.gov/25.4), [5.11](https://dlmf.nist.gov/5.11). Elkies denotes by xi the meromorphic completion; his (s^2-s)xi(s)/2 is the entire xi used here. His product includes multiplicities. The additional [Trudgian source](https://arxiv.org/abs/1208.5846v2), Corollary 1, also supplies a sufficient O(log T) counting error; no version-specific numerical coefficient is used. See the [reference catalog](../../references/README.md) for exact inspection and retrieval scope.

## 3. The complete relative tail is paid before the local calculation

For s>0 the exact real Gaussian convolution is

\[
 H(-s,z)=\frac1{\sqrt{4\pi s}}\int_{\mathbb R}
       e^{-u^2/(4s)}F(z+u)\,du. \tag{11}
\]

Insert the full cosine transform of the theta source and integrate the real Gaussian to get its heat multiplier e^{-s v^2}. Fubini is justified by the superexponential source decay at fixed Im z; this is also the normalization used in [Note 13](13_COMPLETE_XI_LOGARITHMIC_HEAT_ANCHOR_20261023.md). There is no truncation of the source.

RH makes the upper half-plane zero-free for F. Along every real segment at fixed positive height,

\[
 \frac{F(z+u)}{F(z)}
 =\exp\left(\int_0^u p(z+v)\,dv\right),
\]

so (10) gives the global relative bound

\[
 \boxed{\left|\frac{F(z+u)}{F(z)}\right|
 \le\exp\{C|u|\log(2+|\Re z|+|u|)\},\quad u\in\mathbb R.} \tag{12}
\]

This already divides by the small complete F(z). It includes shifts through u approximately -Re z and arbitrarily large shifts. A separate polynomial lower bound for zeta or an absolute estimate on an omitted tail is unnecessary: (12) pays the same obligation directly. It is a somewhat larger majorant than the sufficient polynomial-times-exponential bound proposed in Note 17, but still adequate for this clock.

Fix a small positive radius r independent of Y. For x in [Y-O(1),2Y+O(1)], v>=r and large Y,

\[
 C v\log(2+|x|+v)\le v^2/(8s),\qquad 0<s\le c/L^2. \tag{13}
\]

Indeed log(2+|x|+v)<=C_0+L+log(1+v), while (L+log(1+v))/v is at most L/r+C_r. This grows only linearly in L; 1/(8s) grows at least quadratically. Therefore the normalized relative tail in (11) over |u|>r is at most

\[
 C e^{-r^2/(16s)}. \tag{14}
\]

Dividing also by e^{s p(z)^2} costs at most exp(s|p|^2)<=exp(C^2c), a constant for each fixed c. Thus this entire tail is O(L^-M) for every fixed M, uniformly down to s=0. The same argument pays tails of the local exponential and each of its fixed polynomial factors.

## 4. Gaussian extraction and the first correction

On |u|<=r, write the local logarithmic ratio, using (10), as

\[
 \log\frac{F(z+u)}{F(z)}=p u+\tfrac12p'u^2+R_3(z,u),
 \qquad |R_3(z,u)|\le CL|u|^3. \tag{15}
\]

Here the logarithm is its analytic branch continued from u=0, not a principal argument chosen point by point. Let A=p'u^2/2. With r fixed and small, the elementary exponential remainder gives

\[
 |e^{A+R_3}-1-A|
 \le C\{L|u|^3+L^2|u|^4\}e^{CLu^2}. \tag{16}
\]

Let E_s denote integration against the real centered Gaussian of variance 2s. For every fixed j>=0,

\[
 \frac{E_s[|u|^j e^{(\Re p)u+CLu^2}]}{|e^{s p^2}|}
 \le C_{j,c}\bigl(\sqrt{s}+sL\bigr)^j. \tag{17}
\]

To verify this uniformly, put d=1-4CLs>=1/2 for large Y and complete the real square. The new variance is 2s/d, its mean is 2s Re p/d, and its scalar mass is d^{-1/2}exp(s(Re p)^2/d). Relative to |e^{s p^2}| the exponent is

\[
 s(\Im p)^2+s(\Re p)^2(d^{-1}-1)=O_c(1).
\]

This explicitly pays the oscillatory cancellation; it does not replace the full complex exponential by its absolute Gaussian transform. In our range sqrt(s)+sL=O_c(L^-1). Applying (17) to (16) gives a relative error O(L^-2). Equation (14) covers the omitted parts of both original and approximating integrals.

Finally the exact complex Gaussian moments are

\[
 E_s[e^{pu}]=e^{sp^2},\qquad
 E_s[u^2e^{pu}]=(2s+4s^2p^2)e^{sp^2}.
\]

Inserting them proves (1), hence (2). All estimates are uniform on a fixed enlarged positive-offset strip. The remainder in (1) is holomorphic in z there, because F and e^{sp^2} do not vanish. Cauchy's estimates on fixed disks prove the claimed derivative bounds. For large Y its full ratio lies in a disk about 1 of radius O(L^-1), so its analytic logarithm exists. Differentiating that logarithm yields (4). This also proves the nonvanishing used to define p_s, rather than presupposing it.

The calculation is for **real s>=0 only**. No complex-time statement or uniformity as b_- decreases to zero is being asserted.

## 5. Material graphs and their actual finite buffer

Fix b in [b_-,b_+]. Let z_a=a+ib, initially for a in [Y-d,2Y+d] with a fixed d>0. Choose a containing rectangle with another fixed horizontal margin and with positive lower and finite upper imaginary margins. Prove (1)--(4) on a still larger rectangle, leaving a fixed Cauchy margin. The labels and all end extensions are part of this construction.

For backward duration s solve

\[
 \partial_s Z(s,a)=-p_s(Z(s,a)),\qquad Z(0,a)=z_a. \tag{18}
\]

The acquired bounds |p_s|<=KL and |partial_z p_s|<=KL hold on the containing rectangle. Until exit, |Z-z_a|<=KLs<=Kc/L. For sufficiently large Y this is less than half the distance to each side of that rectangle. A first-exit contradiction and ordinary local ODE continuation therefore give (18) on the full interval [0,c/L^2]. This uses an actual spatial buffer; neither global critical-value avoidance nor an assumed proper primitive is needed.

For J=partial_a Z,

\[
 J_s=-(\partial_zp_s)(Z)J,\qquad J(0)=1,
\]

and hence, with the continuous logarithm starting at zero,

\[
 |\log J|\le Kc/L,\qquad J=1+O(L^{-1}),\qquad \Re J>0. \tag{19}
\]

Thus each transported arc is a graph over its advected real interval, its continuous tangent angle is O(L^-1), and its slope is O(L^-1). The fixed initial horizontal extensions and displacement bound ensure that the graph still covers the whole target interval [Y,2Y]; they do not force its endpoints to remain fixed.

More precise integration of (4), using |Z-z_a|=O(sL), gives

\[
 \boxed{Z(s,a)=z_a-s p(z_a)+O(L^{-2}),\qquad
 J(s,a)=1-s p'(z_a)+O(L^{-2}).} \tag{20}
\]

For the first formula the integrand error is O(sL^2+L^-1); its integral is O(L^-2). For the second, partial_z p_s(Z)=p'(z_a)+O(1), and J=1+O(L^-1); integration gives the same remainder. These bounds are uniform, including a in the extended label interval.

The exact material identity remains

\[
 H(-s,Z(s,a))J(s,a)=F(z_a). \tag{21}
\]

Indeed differentiating the left-hand side using (18) gives zero. For the canonical primitive of the even field, P(t,z)=integral_0^z H(t,w)dw, P_t=-H_z, and

\[
 \frac d{ds}P(-s,Z)=H_z-Hp_s=0. \tag{22}
\]

Therefore this is the selected inverse-primitive lift. It cannot escape to the conserved finite asymptotic value on this time window because it remains in the paid finite rectangle. Other inverse branches may share its primitive value; their critical values are irrelevant to this local uniqueness statement.

## 6. The backward motion is upward at these offsets

Equation (5) gives the convergent positive-kernel identity

\[
 -\Im p(x+iy)=\sum_{\lambda\in\mathcal Z}
             \frac{y}{(x-\lambda)^2+y^2}>0. \tag{23}
\]

It has an upper bound CL by (8). It also has a lower bound kappa L, uniform in the fixed y strip. To see this, write the absolute constant in the remainder of (7) as C_1. Choose a fixed R sufficiently large that the main term of N_F(x+R)-N_F(x-R), namely (R/(2pi))log x+O_R(1), exceeds its two O(log x) errors. Endpoint multiplicities can be covered by using a slightly wider fixed window. This supplies at least k_R log x zeros in |lambda-x|<=R. Each contributes at least b_-/(R^2+b_+^2). Thus

\[
 \kappa L\le-\Im p(x+iy)\le KL. \tag{24}
\]

Use the appropriate enlarged strip constants when applying this along the lift. Equation (4) changes p by O(1), so for large Y

\[
 \tfrac12\kappa L\le\partial_s\Im Z(s,a)\le K' L,
 \qquad \tfrac12\kappa sL\le\Im Z(s,a)-b\le K'sL. \tag{25}
\]

The upper spatial contour moves upward when heat time runs backward. If written as y=epsilon(x,-s), the fixed-x graph derivative is also positive for sufficiently large Y: from (18), partial_s[epsilon(x,-s)]=-Im p_s+(Re p_s)epsilon_x; the slope term is O(1), whereas the first term is bounded below by a positive multiple of L. This is a deterministic fixed-offset statement, with no smoothing or stochastic model. It is not a sign theorem for the regularized relative zero current or for the physical Chern--Hopf form.

## 7. Matched direct comparison and exactly what was gained

From the same initial information, a direct unextracted estimate gives

\[
 \left|H(-s,z)/F(z)-1\right|
 \le C sL^2 e^{C sL^2}+\text{negligible tail}. \tag{26}
\]

For example, expand F(z+u)/F(z)=1+pu+O(L^2u^2 e^{CL|u|}); the odd linear term integrates to zero. At s=c/L^2 this is only O_c(1), and its triangle-inequality zero-free test needs a sufficiently small c. Retaining e^{sp^2} gives a relative error tending to zero and hence nonvanishing for **every prescribed fixed c**, with a c-dependent height threshold. The first correction improves that relative approximation to O(L^-2).

This is a real gain over the specific one-step additive estimate (26), not a proof that every direct method is weaker. The Gaussian comparison itself is a direct field estimate. Material conservation supplies its geometric transfer, not an additional arithmetic gain over the same field calculation. The proof uses the complete xi product, RH, a coarse zero count and one Euler-region logarithmic anchor. It does not exploit new cancellations among the complete theta invariant values, and its analytic bounds are shared by a broader class.

No optimization of c growing with Y, larger heat interval, near-axis strip, or effective threshold is included. Improving the order of a fixed-offset expansion by itself does not address the missing multiplicity statistic.

## 8. Collision screening and the next actual estimate

The proof is compatible with endpoint multiplicities by construction. Here is a complete screening of the relevant classes.

| Control | Premise or scope check | Consequence for this result |
| --- | --- | --- |
| Euler-factor family F(z)(1+q cos(az)), 0<q<1 | The factor has nonreal zeros, so initial all-realness fails; positivity alone does not repair this. | Its positive-time collisions do not contradict the RH-conditioned lemma. |
| The same family at q=1 | Under canonical RH, all initial zeros are real, including infinitely many zeros of multiplicity at least two supplied by 1+cos(az). Its added log derivative is -a tan(az/2), bounded with all fixed derivatives on every fixed positive strip. The counting law is (7) plus aX/pi+O(1), so the literal canonical count is changed, while its unit-count upper bound and fixed-wide-window lower bound persist. Shifted positive theta sources justify the Gaussian formula. | The analytic proof applies with that modified counting law, and the modified field still has multiple endpoint zeros. It fails the exact canonical source identity, but **does not fail the coarse acquired estimates**. The theorem is not a simplicity discriminator. |
| Finite weighted-square controls | They fail full theta reflection and, by the repository's finite-source audit, have nonreal zeros at every real heat time. | The initial all-real premise is unavailable. Their positive source/support constraints are not a replacement. |
| Reflected super-Gaussian control | It lacks the exact theta arithmetic and canonical xi Euler anchor; the registered hypotheses do not supply the complete all-real initial zero set and the logarithmic bounds used here. | Do not infer that it fails every possible fixed-strip inequality. No collision exclusion is claimed from those shared formal identities. |
| Smooth shape/positive-primitive controls | They lack the canonical square-source/xi data; their retained positivity and endpoint asymptotics do not establish this proof's initial real-zero/product inputs. | They screen hierarchy/positivity arguments, not the stated RH-conditional comparison. |
| Quadratic F(z)=(z-a)^2 | Initial all-realness allows a double, and the Gaussian evolution is H(-s,z)=(z-a)^2+2s. | Its fixed-offset wall is regular for sufficiently small s despite the interior double; the near-axis calculation below is exact. |

For the local quadratic model centered at a, at z=a+i beta/L and s=kappa/L^2,

\[
 \frac{H(-s,z)}{F(z)}=1-\frac{2\kappa}{\beta^2},\qquad
 e^{sp(z)^2}=e^{-4\kappa/\beta^2}. \tag{27}
\]

At kappa=beta^2/2 the first expression vanishes and the second does not. In this family |p'|=2L^2/beta^2; the O(L) fixed-offset derivative hypothesis has broken down. This shows that the same local generic argument cannot pass through a double at that shrinking offset. To place the example literally in the height band as Y increases, take the translated family a=Y; the field then depends on Y. The preceding q=1 control separately supplies a fixed field with multiple zeros at arbitrarily high heights. Neither control permits a shrinking-offset extension **from real-rootedness and the same generic argument alone**. It is not an impossibility theorem for a canonical theta estimate with additional arithmetic information.

### A positive-source control with no simple zeros and the same coarse count

The q=1 factor alone adds O(Y) multiple zeros among Theta(Y log Y) zeros, so by itself it screens an every-zero conclusion, not every possible proportion argument. The following stronger control addresses that distinction. Set

\[
 a_*=(\log2)/4,\qquad
 G_0(z)=F(z/2)^2\{1+\cos(a_*z)\}. \tag{28}
\]

Under canonical RH all its zeros are real and all have even multiplicity. Counts with multiplicity add even when the two factors share a zero, and the cosine factor has double zeros at the odd multiples of pi/a_*. Hence

\[
 \begin{aligned}
 N_G(X)&=2N_F(X/2)+a_*X/\pi+O(1)\\
 &=\frac X{4\pi}\log\frac X{4\pi}-\frac X{4\pi}+O(\log X).
 \end{aligned} \tag{29}
\]

Thus even the two displayed main terms in (7) are unchanged. If p_G=G_0'/G_0, then

\[
 p_G(z)=p(z/2)-a_*\tan(a_*z/2). \tag{30}
\]

The tangent and each fixed derivative are bounded on every fixed positive-offset strip. Equations (10), (12), and all the local Gaussian hypotheses therefore hold for G_0. The exact canonical Euler factorization is absent; the Euler **logarithmic bound actually consumed** by the proof is nonetheless already supplied by (30).

For source verification, write F(z)=integral_R rho(u)e^{izu}du, where rho=Phi_even/2 is positive, even and superexponentially decaying. Put rho_2(u)=2rho(2u), q=rho_2*rho_2. Then the full Fourier density of G_0 is

\[
 \rho_G(u)=q(u)+\tfrac12q(u-a_*)+\tfrac12q(u+a_*)>0. \tag{31}
\]

It is even and superexponentially decaying. For example, if rho_2(v)<=C exp(-d exp(k|v|)), split its convolution into |v|>=|u|/2 and |u-v|>=|u|/2. Bound the large-argument factor by its tail supremum and integrate the other L^1 factor; the result is at most C' exp(-d exp(k|u|/2)). Finite shifts retain this property. Consequently integral_R e^{tu^2}rho_G(u)e^{izu}du exists for every real t and gives the same exact heat equation and Gaussian continuation.

The proof of (1)--(25), with field-dependent constants, applies to this control, which has **zero simple zeros** at time zero. This excludes extracting any positive simplicity proportion from the *existence* of the displayed fixed-offset asymptotic bounds, initial real-rootedness, the coarse count (29), positive source and formal conserved hierarchy alone. It does not exclude an inequality using actual theta coefficients, exact invariant values or sharper quantitative constants that the control fails. The canonical source identity is the failed premise; none of the coarse acquired bounds is the distinguishing premise.

The acquired high outer wall has no zero crossings during the interval, but it does not bound the nonreal zeros already inside at its earlier endpoint. Doubles and higher clusters unfold inside this wall. The earlier-population term, small real-axis cutoff, height-end coverage and any one-sided inward current required by the [existing consumer](12_HERMITE_CLUSTER_DOMINATION_AND_JOINT_CONSUMER_20261023.md) remain unpaid. Ordinary boundary regularity does not eliminate any of them.

**Continuation decision:** retain this theorem as the completed fixed-offset subproblem under SCF-01/02. Before making more expansion terms or moving it into the book, identify an observable that distinguishes the all-multiple control (28) and is sensitive to an endpoint multiplicity. The next substantive task is either a bound on the complete earlier nonreal resource at s approximately L^-2, or a near-axis comparison that keeps the exact local zero/cluster factor and obtains a new bound on its multiplicity-sensitive part from canonical arithmetic. The outer wall is now available as an analytic input. A shrinking-strip floor that already excludes the quadratic local model must not simply be assumed.

SCF-03, useful SIMP-01/02 completion, and SCF-04 book selection remain open. No manuscript is changed by this research note. The execution chat is the separately registered **history 0008**, thread `01a16b52-9407-7e80-8f09-3d5b3303e5b2`; history 0007 remains intact.
