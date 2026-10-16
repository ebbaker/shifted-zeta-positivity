# Real and complex multiplicities of a heat collision

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. Internal mathematical review is not external refereeing or formal verification.

A collision of spatial multiplicity \(m\) has real spacetime index \(-\lfloor m/2\rfloor\), but its holomorphic complexification has local degree \(m(m-1)/2\). This generalizes the cubic counterexample in [Review 17](../../reviews/17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md). The integers measure different phenomena. A boundary deformation within a fixed dimension cannot identify them. The result clarifies what an anisotropic contour would need to estimate; it establishes no advantage or impossibility for such estimates.

## The local discriminant theorem

Let \(H(t,x)\) be real analytic near \((T,a)\), satisfy \(H_t=-H_{xx}\), and have exact spatial order \(m\ge2\) there. Complexify and translate the event to \((\tau,z)=(0,0)\). Then the holomorphic map

\[
G(\tau,z)=(H(\tau,z),H_z(\tau,z))
\]

has an isolated zero with complex intersection multiplicity

\[
\boxed{\quad \dim_{\mathbb C}\mathbb C\{\tau,z\}/(H,H_z)
=\frac{m(m-1)}2=:L_m.\quad} \tag{1}
\]

With the complex orientations, its real four-dimensional local degree is \(+L_m\). With the quaternion orientation declared in [Investigation 21 Note 4](../../../21_quaternion_theta_geometry/notes/4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md), it is \(-L_m\).

**Proof.** The heat Taylor expansion has weighted leading part

\[
H(\tau,z)=c\,p_m(\tau,z)+\text{terms of weighted degree greater than }m,
\quad c\ne0,
\qquad
p_m(\tau,z)=\sum_{k=0}^{\lfloor m/2\rfloor}
\frac{m!(-\tau)^kz^{m-2k}}{k!(m-2k)!}, \tag{2}
\]

where \(\tau\) has weight two and \(z\) weight one. Consequently

\[
F(r,w)=r^{-m}H(r^2,rw)
\]

extends holomorphically to \(r=0\), with \(F(0,w)=c\,p_m(1,w)\). The latter has \(m\) distinct real Hermite roots \(\lambda_1,\ldots,\lambda_m\). The analytic implicit function theorem supplies \(m\) branches

\[
w_i(r)=\lambda_i+O(r),\qquad z_i(r)=r\lambda_i+O(r^2). \tag{3}
\]

Apply Weierstrass preparation in the spatial coordinate: \(H=UP\), where \(U\) is a holomorphic unit and \(P\) is monic of degree \(m\) in \(z\), with \(P(0,z)=z^m\). Its \(m\) roots are exactly the cluster (3). Their discriminant satisfies

\[
\operatorname{Disc}_z P(r^2,z)
=\prod_{i<j}(z_i(r)-z_j(r))^2
=r^{m(m-1)}\left(\prod_{i<j}(\lambda_i-\lambda_j)^2+O(r)\right). \tag{4}
\]

The left side is analytic in \(r^2\), and the leading constant is nonzero. Therefore

\[
\operatorname{ord}_{\tau=0}\operatorname{Disc}_zP=L_m. \tag{5}
\]

In particular, the discriminant has no other sufficiently small zero: \(H,H_z\) have no other common zero near the origin, including at complex time. Also \((H,H_z)=(P,P_z)\), since \(U\) is a unit. Weierstrass division identifies \(\mathbb C\{\tau,z\}/(P)\) with \(\mathbb C\{\tau\}[z]/(P)\). This ring is free of rank \(m\) over the one-variable convergent power-series ring. Multiplication by \(P_z\) has determinant \(\operatorname{Res}_z(P,P_z)\), which differs from the discriminant only by a sign. Diagonal reduction over that discrete valuation ring shows that the cokernel has complex dimension equal to the determinant's order of vanishing. This proves (1). Equivalently, this is the usual local discriminant/intersection formula; see Simon and Weimann, [§2.5, printed pp. 11–12](https://weimann.users.lmno.cnrs.fr/Disc.pdf).

The local degree of an isolated holomorphic map zero equals its positive complex intersection multiplicity: a small generic regular target has that many preimages, each with positive real Jacobian \(|\det_{\mathbb C}DG|^2\). The declared quaternion output reverses one real coordinate, changing the sign and not the magnitude. ∎

This proof uses arbitrary analytic higher-order terms compatible with the heat equation. It does not assume spatial symmetry or an exact polynomial model. Swapping the two complex input coordinates preserves their real four-dimensional orientation; swapping the real input order \((t,x)\) would reverse the two-dimensional index and must not be done silently.

## Three different geometric counts

The [real spacetime theorem](04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md) gives

\[
I_{\mathbb R}=-\lfloor m/2\rfloor. \tag{6}
\]

This counts pairs of nonreal spatial roots that become real as time passes through the event. Equation (4) instead multiplies differences between **every unordered pair** of the \(m\) emerging roots. Each squared difference contributes one time order, producing \(L_m=\binom m2\).

The primitive fixed-time curve \(z\mapsto(H(T,z),\int_a^zH(T,\zeta)\,d\zeta)\) has link \(T(m,m+1)\), Milnor number \(m(m-1)\), and Milnor-fiber genus \(L_m\), as established in Note 04. Thus its Milnor-fiber genus equals the complex collision multiplicity. This is a numerical identity between invariants of two different germs, not an identification of their spaces or a new index theorem.

| Spatial order \(m\) | Real spacetime index | Holomorphic degree | Declared quaternion degree | Primitive Milnor-fiber genus |
| --- | --- | --- | --- | --- |
| 2 | −1 | 1 | −1 | 1 |
| 3 | −1 | 3 | −3 | 3 |
| 4 | −2 | 6 | −6 | 6 |
| 5 | −2 | 10 | −10 | 10 |
| 6 | −3 | 15 | −15 | 15 |

The magnitudes agree only for a double event. Their parities always agree, because

\[
L_{2r}-r=2r(r-1),\qquad L_{2r+1}-r=2r^2. \tag{7}
\]

A parity comparison therefore cannot justify equality of the integer counts. Moreover, a complex domain can contain common zeros with nonreal time or spectral coordinate; such zeros need not correspond to physical real collisions at all.

## What changes when a contour becomes thin

For a fixed isolated event, every sufficiently small four-dimensional bounded neighborhood with nonzero boundary map has the same degree \(+L_m\), or \(-L_m\) in the declared quaternion convention. The neighborhood may have independently chosen spectral and heat-time widths. Changing its aspect ratio while retaining the enclosed zero and a nonzero boundary preserves that integer.

Its intersection with the real spacetime plane has the two-dimensional index (6). Sending the transverse widths to zero changes dimension. There is no degree-preserving argument that converts the former integer into the latter; for \(m\ge3\), (1) and (6) explicitly prevent such an identification. For collections of double events the numerical weights happen to match, but one must still justify exclusion of additional nonreal complex events and any limiting boundary terms.

Conversely, these different multiplicities say nothing by themselves about the sharpness of boundary estimates. An anisotropic contour could have different error bounds, or retain different cancellation, while representing the same data. The relevant experiment must compare a rigorously controlled error, domain, or cost. The local degree calculation neither supplies that improvement nor rules it out.

## Exact controls and scope

The [checker](../../numerics/check_complex_heat_multiplicity.py) verifies the exact model identity

\[
\operatorname{Disc}_z p_m(\tau,z)
=2^{m(m-1)/2}\left(\prod_{k=1}^m k^k\right)\tau^{m(m-1)/2} \tag{8}
\]

for \(2\le m\le16\). It also checks the predicted discriminant order for 27 asymmetric heat solutions

\[
p_m+a p_{m+1}+b p_{m+2},\qquad
2\le m\le10,\quad (a,b)\in\{(1,0),(-2,0),(1,1)\}. \tag{9}
\]

At time zero the additional roots are nonzero and simple, so they add no discriminant order at the selected event. The [receipt](../../numerics/COMPLEX_HEAT_MULTIPLICITY_CHECKS_20261015.json) records **198 exact assertions**, python-flint version, and script identity. These are controls for algebra and conventions. The general theorem is proved above; no numerical theta collision, new theta sign estimate, or publication-priority claim follows.
