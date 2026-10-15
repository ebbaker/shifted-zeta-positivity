---
research_program: PR02
secondary_programs: [ALG, PR02-CORR]
status: proved_geometric_realization_and_conditional_turning_criterion
---

# Jet surfaces, their real Gauss maps, and oriented turning

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified and supplied by the coordinator. This is an analytic construction and conditional criterion. No new theta sign region or RH conclusion is claimed.

The first jet defines a genuine immersed Kähler surface whose induced metric contains exactly the physical energy. Its intrinsic curvature squares the signed Laguerre observation, so that curvature does not retain its sign. The real projective Gauss map retains the sign and yields a distinct sufficient target: exclude positive quarter-turn concentration on shrinking spatial intervals. The target is not yet proved for the complete theta source.

## 1. A genuine surface carrying the first-jet energy

Fix a real heat time and write `f(z)=H(t,z)`. Let `P'=f`, with `P` entire for the theta field. On

\[
\Omega_t=\{z:\mathcal E(t,z):=|f(z)|^2+|f'(z)|^2>0\},
\]

define the holomorphic map

\[
X_t:\Omega_t\times\mathbb C\longrightarrow\mathbb C^3,
\qquad X_t(z,w)=(P(z),f(z),w).
\tag{1}
\]

Its two complex tangent vectors are `(f,f',0)` and `(0,0,1)`, hence it is an immersion with induced real Riemannian metric

\[
\boxed{g_t=\mathcal E(t,z)|dz|^2+|dw|^2.}
\tag{2}
\]

This is a product of a complex curve and a flat complex line. On the physical real slice, `\mathcal E(t,x)=E(t,x)`. The parameter domain with (2) is a genuine smooth Riemannian manifold. The image is an immersed complex surface; global injectivity or absence of self-intersections is not asserted. At a common zero `f=f'=0`, the map loses one complex rank and (2) ceases to be a Riemannian metric there.

The induced Kähler form is

\[
\omega_t=\frac i2\{\mathcal E\,dz\wedge d\bar z+dw\wedge d\bar w\}.
\]

Each embedded local image patch is calibrated by the ambient `\omega_0^2/2`, hence is minimal. This is the usual complex-submanifold calibration; see [Lotay, Theorem 3.1 and Theorem 2.3](https://arxiv.org/pdf/1810.08709).

There are also literal exceptional-calibration realizations. Viewed in `{0}\times\mathbb C^3\subset\mathbb R^7` with the standard `G_2` form `dr\wedge\omega_0+\Re\Omega_3`, the surface is coassociative. Viewed as `(P,f,w,0)` in `\mathbb C^4\cong\mathbb R^8`, it is Cayley for

\[
\Psi_0=\tfrac12\omega_0^2+\Re\Omega_4,
\]

because the holomorphic four-form pulls back to zero and the first term pulls back to the induced volume. These standard inclusions are [Lotay, Propositions 6.5 and 7.3](https://arxiv.org/pdf/1810.08709). The ambient metrics here are flat, with trivial holonomy contained in the stated groups. No new metric with holonomy exactly `G_2` or `Spin(7)` has been constructed.

## 2. Curvature and the limitation of induced special holonomy

Set

\[
D=f f''-(f')^2.
\]

Differentiating `\mathcal E` and using the two-by-two Gram determinant gives

\[
\partial_z\partial_{\bar z}\log\mathcal E
=\frac{\mathcal E(|f'|^2+|f''|^2)
-|f'\bar f+f''\overline{f'}|^2}{\mathcal E^2}
=\frac{|D|^2}{\mathcal E^2}.
\tag{3}
\]

For the real metric convention `ds^2=\mathcal E(dx^2+dy^2)`, its Gaussian curvature is therefore

\[
\boxed{K_t=-\frac1{2\mathcal E}\Delta\log\mathcal E
=-\frac{2|D|^2}{\mathcal E^3}\le0.}
\tag{4}
\]

The four-dimensional product has scalar curvature `2K_t`; its Ricci tensor is `K_t` times the curve metric in the first factor and zero in the flat factor. Its Ricci form is

\[
\boxed{\rho_t=-i\frac{|D|^2}{\mathcal E^2}
\,dz\wedge d\bar z.}
\tag{5}
\]

The Levi-Civita holonomy preserves both product factors and is contained in `U(1)\times\{1\}\subset U(2)`. If `D` is nonzero somewhere on a connected patch, the restricted holonomy contains the nontrivial rotation group of the curved factor. In particular this induced metric is not Ricci-flat and cannot have restricted holonomy contained in `SU(2)`.

Conversely, `D\equiv0` on a connected patch implies `f=Ae^{bz}` there, with `A\ne0`, including the constant case `b=0`. To prove this, choose a subpatch where `f\ne0`; `(f'/f)'=D/f^2=0`, and holomorphic identity continuation gives the conclusion. Thus Ricci-flatness is exceptionally restrictive for this particular construction. An entire nonzero even decaying theta field cannot be such an exponential. This statement concerns the induced metric (2), not every possible auxiliary metric one could put on its underlying manifold.

On the physical line `D=-\mathcal L_0`, so

\[
K_t(t,x)=-2\mathcal L_0(t,x)^2/E(t,x)^3.
\tag{6}
\]

Intrinsic curvature records the magnitude and loses the sign of the stationary loss.

## 3. The Gauss map preserves the relevant direction

The nonconstant tangent direction of (1) has projective Gauss map

\[
G_0(t,z)=[H(t,z):H_z(t,z)]\in\mathbb{CP}^1.
\tag{7}
\]

Normalize the Fubini–Study metric by `ds_{FS}^2=|d\zeta|^2/(1+|\zeta|^2)^2`. Direct differentiation in either projective chart gives

\[
G_0^*ds_{FS}^2=\frac{|D|^2}{\mathcal E^2}|dz|^2,
\qquad \rho_t=-2G_0^*\omega_{FS}.
\tag{8}
\]

The real-reflection symmetry puts the physical image in `\mathbb{RP}^1`. On a real interval where `E>0`, take a continuous real lift

\[
\alpha_0(t,x)=\arg(h_0+i h_1).
\]

Its derivative is

\[
\boxed{\partial_x\alpha_0
=\frac{h_0h_2-h_1^2}{h_0^2+h_1^2}
=-\frac{\mathcal L_0}{E}.}
\tag{9}
\]

Consequently the desired first stationary lower bound is exactly an upper bound on the oriented angular velocity of this real Gauss map. A positive scalar curvature norm cannot replace that orientation.

For the second observation use the surface `(H,H_z,w)` and the Gauss map

\[
G_1=[h_1:h_2],\qquad E_1=h_1^2+h_2^2,
\qquad \partial_x\alpha_1=-\mathcal L_1/E_1.
\tag{10}
\]

This denominator is **not** the physical energy off the second stationary set, and `E_1` can vanish even when `E>0`. Every assertion using `\alpha_1` is therefore restricted to intervals where `(h_1,h_2)\ne(0,0)`. On `S_1` with `h_1\ne0`, `E_1=h_1^2\le E`; hence the source-prescribed bound `\alpha_1'\le\kappa` with `\kappa\ge0` would suffice for `\mathcal L_1\ge-\kappa E`. It is a stronger sufficient condition than the physical-energy bound in general. On an odd collision predecessor, the manuscript proves `E/E_1=1+O(s^2)`.

## 4. Calibrated geometry alone accepts both Laguerre signs

Fix `\varepsilon>0` and consider

\[
f_+(z)=\varepsilon+z^2,\qquad f_-(z)=\varepsilon-z^2,
\qquad P_\pm(z)=\varepsilon z\pm z^3/3.
\]

At the real center,

\[
E_\pm=\varepsilon^2,\quad
\mathcal L_{0,+}=-2\varepsilon,\quad
\mathcal L_{0,-}=2\varepsilon,
\quad K_+=K_-=-8/\varepsilon^4.
\tag{11}
\]

Their complex surfaces are unitarily congruent after rotating the domain:

\[
\operatorname{diag}(-i,1,1)X_+(iz,w)=X_-(z,w).
\tag{12}
\]

Thus these intrinsic and calibrated geometries cannot distinguish favorable from adverse real turning unless the marked physical real slice and its orientation are retained. Both slices admit exact backward-heat extensions. In particular `H(t,z)=z^2-2(t-T)` is calibrated at all its regular points and develops a double zero at `(T,0)`; on its predecessor `x=0`, `\alpha_0'=1/(T-t)`.

The positive-source collision control in [Note 56](../05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) also admits these generic holomorphic constructions, so the issue persists beyond the polynomial example.

At a fixed-time zero `f(z)=c(z-a)^m+O((z-a)^{m+1})`, `m\ge2`, (2) has curve factor

\[
\mathcal E\sim m^2|c|^2|z-a|^{2m-2}.
\]

The completion is at finite radial distance and has asymptotic cone angle `2\pi m`. This is a degenerating immersion, not a smooth Riemannian point rescued by calibration.

One can make an everywhere immersive graph `(z,P,H,w)` in `\mathbb C^4`, which is again a complex calibrated surface and hence Cayley. Its metric is `(1+\mathcal E)|dz|^2+|dw|^2`, so it remains regular at a physical joint zero. This construction makes explicit why merely finding a smooth calibrated manifold is insufficient: its metric no longer vanishes at the physical energy scale.

## 5. A distinct signed target: exclude positive quarter-turn concentration

Let `W=h_j` with `j=0` or `1`, and define `\alpha_j=\arg(W+iW_x)` on real intervals on which that pair never vanishes. Suppose a finite collision has multiplicity `2r+j`, `r\ge1`, at `(T,x_*)`. Let `s=T-t` and let `x=\chi(s)` be the full stationary predecessor. With `k=h_{2r+j}(T,x_*)/r!\ne0`, the local heat expansion of [Note 57](57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md) gives, uniformly for `0\le y\le c` with any fixed `c>0`,

\[
W(T-s,\chi(s)+\sqrt{s}y)
=ks^r\{F_r(y)+O(\sqrt{s})\},
\]
\[
W_x(T-s,\chi(s)+\sqrt{s}y)
=ks^{r-1/2}\{F_r'(y)+O(\sqrt{s})\},
\]
\[
F_r(y)=\sum_{\ell=0}^r
\frac{r!}{(r-\ell)!(2\ell)!}y^{2\ell}.
\tag{13}
\]

Here `F_r(y)\ge1` on the interval and `F_r'(c)>0`. Thus `W` has one nonzero sign throughout that interval for small `s`; in particular all angle lifts are regular there, including for `j=1`. At its left endpoint `W_x=0`. Choose any continuous lift and subtract its initial angle, which is an integer multiple of `\pi`. At the right endpoint,

\[
\frac{W_x}{W}
=s^{-1/2}\frac{F_r'(c)}{F_r(c)}\{1+O(\sqrt{s})\}
\longrightarrow+\infty.
\]

Because `W` retains its sign, the angle difference is the ordinary arctangent of that positive ratio, without a wrap ambiguity. Therefore

\[
\boxed{\alpha_j(T-s,\chi(s)+c\sqrt{s})
-\alpha_j(T-s,\chi(s))\longrightarrow\pi/2.}
\tag{14}
\]

Every finite collision produces a positive quarter-turn in a vanishing spatial interval, irrespective of its multiplicity.

**Conditional oriented-continuity criterion.** On a domain covering the required predecessors and their sufficiently short right-hand spatial intervals, suppose that for each compact local neighborhood there is a prescribed modulus `\omega(\ell)\to0` as `\ell\downarrow0`, uniform in its time and stationary starting point, such that for both `j=0,1`,

\[
\alpha_j(t,x+\ell)-\alpha_j(t,x)\le\omega(\ell)
\tag{15}
\]

whenever `h_{j+1}(t,x)=0`, `h_j(t,x)\ne0`, the segment lies in that neighborhood, and `(h_j,h_{j+1})` never vanishes on it. The difference uses the continuous lift along the segment. Then no finite collision covered by this domain can occur. For the complete theta field, coverage of all candidate positive-time events yields RH by the manuscript's existing collision reduction.

**Proof.** A hypothetical collision selects its parity branch `j`. The segments in (13) satisfy every regularity condition in (15), while their lengths tend to zero and their angle increments tend to `\pi/2`, contradicting (15).

A concrete sufficient version of (15) is `\omega(\ell)=C\ell^\beta`, with fixed `\beta>0` and source-prescribed locally bounded `C`. Equivalently on regular segments, the signed integral being bounded is

\[
\int_x^{x+\ell}
\frac{h_jh_{j+2}-h_{j+1}^2}{h_j^2+h_{j+1}^2}\,dy.
\tag{16}
\]

The coefficients in a proposed modulus must be supplied from the complete theta source, not fitted to an observed energy floor. Formula (16) specifies the observation; it does not provide its bound. It also keeps the branch-specific denominator explicit.

This criterion is implied by a uniform upper bound on the angular derivative throughout each tested interval. It is not claimed to be weaker than, or implied by, the manuscript's bound imposed only at stationary points: their domains and required data differ. The advantage of (15) over a bound on absolute turning or curvature is that arbitrarily large favorable negative turning remains permitted. For `f_-(x)=\varepsilon-x^2`,

\[
\alpha_-'(x)=\frac{-2\varepsilon-2x^2}
{(\varepsilon-x^2)^2+4x^2}<0,
\]

so every rightward increment is negative even as the magnitude of its central curvature diverges.

## 6. What this adds and what remains open

The immersed surface, induced metric, curvature formulas, projective Gauss map, exceptional-calibration inclusions, and quarter-turn concentration law are proved above. They make the relevant geometric distinction precise: calibration and intrinsic curvature do not select the sign, while the marked real Gauss map does.

The new possible source target is uniform one-sided continuity of the complete real jet direction on short intervals beginning at full stationary points. It is a condition that can be tested on controls and in a frozen certified pilot, with regularity of the whole interval retained. A fixed-time removable projective singularity is insufficient: at a zero of multiplicity at least two the spatially extended map `[W:W_x]` tends to `[0:1]`, whereas the stationary predecessors in (13) equal `[1:0]`. The issue is uniform behavior as heat time changes.

No such modulus has been established for theta. The theorem is a geometric reformulation with a new integrated sufficient target, not an RH proof or evidence that generic calibrated-manifold theorems provide the missing arithmetic estimate.
