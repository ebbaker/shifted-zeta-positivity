# Moving heat contours across zero with a height dependent backward width

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. Same-assistant derivation and assessment.

**Status: finite-cluster transport identities, a conditional collision-free radius, and an estimating target for the time-zero cap; no new canonical-theta bound.** The proposed contour has its right face at a small positive time, interpreted as \(0^+\), and its left face at \(t=-\epsilon(h)\). The author's refined objective is to estimate the original time-zero integral through a deformed representative that may be easier to bound. Moving with the projective first jet gives a precise zero-flux construction. The derivative of the complete root-source product contains the inverse-square interaction energy used by Rodgers–Tao, plus an explicit analytic-factor term. A two-root reduction already present in the repository supplies a benchmark for choosing the backward width without dividing by an unknown interior gap.

This continues [the author's continuation note](01_CONTINUATION_STRUCTURAL_CANCELLATION_RODGERS_TAO_AND_BACKWARD_HEAT_20261023.md). It follows the [result index](../../../../result-summaries/README.md), [local heat geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [control register](../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../avoid/README.md), and the rules on [classification](../../../../avoid/01_restating_the_target.md), [matching control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md). The finite radius below is a quantitative sufficient condition, not an RH-equivalent statement advertised as progress. Its theta inputs remain to be established.

## The contour and what zero charge means

Write \(H_\tau=-H_{zz}\), \(\tau=t+i\sigma\), \(z=x+iy\), and \(G=(H,H_z)\). Use \(h=x\) for positive height in the \(H\) variable, twice the zeta ordinate, and \(H_{\max}\) for the height cutoff. At each finite cutoff choose a fixed right face \(t=\delta_{H_{\max}}>0\) and a left face \(t=-\epsilon(h)<0\). The intended \(0^+\) face means taking a controlled limit \(\delta_{H_{\max}}\downarrow0\); it is not permission to remove \(t=0\) from the enclosed region.

For a compact four-dimensional domain \(W\) with regular complete boundary, the repository's normalized physical Chern–Hopf form satisfies

\[
Q(W)=\int_{\partial W}\mathcal C
=\sum_{p\in W:G(p)=0}\binom{m_p}{2}\in\mathbb Z_{\ge0}.
\tag{1}
\]

Consequently a rigorously computed complete upper bound \(Q(W)<1\) proves \(Q(W)=0\). One does not need to establish exact cancellation numerically. The charge counts all complex joint zeros in the chosen thickened domain, not only real pair-creation events. The imaginary-time thickness and the spatial boundary must be specified.

If \(W\) is subdivided into cells with regular shared faces, then

\[
\int_{\partial W}\mathcal C
=\sum_\nu\int_{\partial W_\nu}\mathcal C.
\tag{2}
\]

Every shared face cancels with the opposite orientation. This holds even when some cells contain events. It is possible to certify each complete cell integral below one instead of paying one absolute error over the entire population. But a cell enclosing an event retains a positive integer charge however small it becomes. Singular derivatives compensate for its shrinking volume.

A smoothly tilted left face has \(dt=-\epsilon'(x)\,dx\), which must enter the full three-form pullback. A practical first construction uses height bands and constant time faces, retains all joining faces, and cancels them before estimation. The graph cannot simply be treated as a holomorphic spatial slice. See [the earlier collar calculation](../../../investigations-4/notes/13_HEIGHT_DEPENDENT_BACKWARD_HEAT_CONTOURS_20261023.md).

## Estimating the original integral through the deformation

Let \(I_0\) be the physical cap at zero, \(I_{-\epsilon}\) its deformed negative-time cap with the same forward parameter orientation, and \(S_\epsilon\) every other outward face of the swept collar. The exact balance is

\[
\boxed{I_0=I_{-\epsilon}-S_\epsilon+Q_-,
\qquad I_0\ge I_{-\epsilon}-S_\epsilon.}
\tag{A}
\]

If the collar is event-free, the original cap equals the **complete** deformed representative \(I_{-\epsilon}-S_\epsilon\). If a lower bound for \(I_0\) is the objective, event exclusion is unnecessary: any independently proved lower bound on that complete representative transfers through (A). For an upper bound or exact equality, the event term must also be addressed.

This is a legitimate way for a deformation to be useful without changing the invariant. A more tractable representative can make its value easier to estimate. The target is a proved bound

\[
I_{-\epsilon}-S_\epsilon\ge L_\epsilon
\]

that improves the attainable lower bound, required data, or proof complexity relative to direct evaluation of \(I_0\). It need not create a strict gain in the exact value. Events in the negative collar lower the exact deformed representative by their charge, so allowing them can still weaken the bound.

Zero-flux projective spatial sides do not generally remove the imaginary-time faces. On a regular flat band with the same population and radius, their sum is exactly \(I_{-\epsilon}-I_0\). They must be retained together with the cap. A changed radius, a height-dependent graph and incomplete chart coverage add their own connecting pieces. This is the precise place to preserve the cancellations before estimating.

If \(G\) vanishes on the time-zero cap, (A) requires explicit excisions and their contributions. The original cross-zero contour with right face \(\delta>0\) can still enclose such an event; taking \(\delta\downarrow0\) does not justify discarding its charge.

## What has already been studied

The closest established ingredients are the following.

| Source | Relation to this proposal |
| --- | --- |
| [Csordas, Smith and Varga, 1994](https://doi.org/10.1007/BF01205170), with an accessible implementation in [Csordas, Odlyzko, Smith and Varga, 1993](https://etna.ricam.oeaw.ac.at/vol.1.1993/pp104-111.dir/pp104-111.pdf) | Lehmer-pair analysis follows close real zeros under heat deformation and controls exterior interactions. The latter paper's Theorem 1.1 and equation (2.19) explicitly display the leading negative-time scale −gap²/8. These are lower bounds for the Newman constant; they are not automatic survival certificates for every local pair. |
| [Rodgers–Tao, corrected text, Sections 4 and 7–8](https://arxiv.org/html/1801.05914) | Their real-zero dynamics and localized renormalized interaction energies supply the closest successful cancellation mechanism. Their proof assumes a fixed all-real negative-time interval for contradiction and obtains relaxation forward in \(t\). This does not supply an unconditional estimate on our shrinking collar. |
| [Papanicolaou, Kallitsi and Smyrlis, 2021, Section 4](https://ejde.math.txstate.edu/Volumes/2021/44/papanicolaou.pdf) | Complex caloric multiple zeros are isolated, and individual zero branches satisfy differential equations between ramification events. This directly supports the trajectory viewpoint. Their forward-heat sign convention must be reversed here. |
| [Hall–Ho, 2025, Section 3](https://link.springer.com/article/10.1007/s11005-025-01946-9) | Polynomial heat-root dynamics and their Calogero–Moser connection are established background. The paper distinguishes its exact finite identities from its large-population conjectures. |

The focused primary-source search did not identify a theorem combining a height-dependent collar across zero, this particular first-jet three-form, and Rodgers–Tao renormalization to exclude theta collisions. That is a limited literature finding, not a priority claim. The repository already contains the [projective-wall calculation](../../../investigations-4/manuscript/topological_zero_transport/boundary.tex) and a [two-root discriminant equation](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md); these should be reused.

## A precise flow for points away from a zero

On a patch where \(H_z\ne0\), set

\[
q=\frac{H}{H_z},\qquad \mathcal L_c=H_z^2-HH_{zz}.
\]

Where additionally \(\mathcal L_c\ne0\), holding \(q\) fixed defines the holomorphic velocity

\[
\boxed{v=\frac{dz}{d\tau}
=-\frac{q_\tau}{q_z}
=\frac{H_zH_{zz}-HH_{zzz}}{H_z^2-HH_{zz}}.}
\tag{3}
\]

At a zero, \(v=H_{zz}/H_z\), the usual zero velocity. Thus the proposed extension of zero motion to nearby points has a concrete choice: transport the projective coordinate of the physical first jet. It is a flow adapted to this observable, not a unique particle flow carried by the heat equation.

Let \(z=Z(\tau,q)\) be an actual inverse chart and \(b(\tau,q)=H_z(\tau,Z(\tau,q))\ne0\). Then

\[
G=b(q,1),\qquad
\mathcal C=\frac{d\arg b\wedge\omega(q)}{4\pi^2},
\quad \omega(q)=\frac{2\,d\Re q\wedge d\Im q}{(1+|q|^2)^2}.
\tag{4}
\]

On a material side \(|q|=\rho\), with constant \(\rho\), the pullback of \(\omega\) vanishes. This is an exact absence of flux for the desired three-form. The associated root-disk cap on an oriented complex-time edge \(e\) is

\[
I(e)=\frac{k_\rho}{2\pi}\Im\int_e d\log\mathscr D,
\quad k_\rho=\frac{\rho^2}{1+\rho^2},\qquad
\mathscr D(\tau)=\prod_{j=1}^m H_z(\tau,z_j(\tau)).
\tag{5}
\]

Three qualifications matter. Charts can fail at \(\mathcal L_c=0\) even when \(G\ne0\); \(H_z=0,H\ne0\) needs another projective chart; and a globally regular root-tube covering is itself a substantive continuation conclusion. It cannot be assumed while proving that the region has no events. Varying \(\rho\) along a tube introduces side terms. Finite cells and joining complements must cover the entire event-relevant region.

## The trajectory derivative and the inverse-square energy

Let \(D_\tau=\partial_\tau+v\partial_z\) along (3). Direct substitution of the heat equation gives

\[
\boxed{D_\tau\log H_z
=\kappa(\tau,z)
=\frac{H_{zz}^{,2}-H_zH_{zzz}}{H_z^2-HH_{zz}}.}
\tag{6}
\]

At a simple root this is

\[
\kappa_j
=\left(\frac{H_{zz}}{H_z}\right)^2
-\frac{H_{zzz}}{H_z},\qquad
\frac{d}{d\tau}\log\mathscr D=\sum_j\kappa_j=:K_{\mathscr D}.
\tag{7}
\]

This is the direct derivative of the quantity in the physical cap, including its analytic factor. It can be estimated before taking differences of large endpoint integrals.

To expose the interaction terms, factor a finite simple cluster as

\[
H(\tau,z)=U(\tau,z)\prod_{j=1}^m(z-z_j(\tau)),\qquad
a=\partial_z\log U,
\]

with \(U\ne0\) near the selected roots. Set \(S_{r,j}=\sum_{k\ne j}(z_j-z_k)^{-r}\) and \(a_j=a(\tau,z_j)\). Elementary differentiation gives

\[
\kappa_j=S_{1,j}^2+3S_{2,j}+2a_jS_{1,j}+a_j^2-3a_z(\tau,z_j).
\]

The distinct-triple terms in \(\sum_j S_{1,j}^2\) cancel, leaving \(\sum_j S_{2,j}\). Pairing the remaining terms yields the exact finite identity

\[
\boxed{K_{\mathscr D}
=8\sum_{j<k}\frac1{(z_k-z_j)^2}+\mathcal B_U,}
\tag{8}
\]

\[
\mathcal B_U
=2\sum_{j<k}\frac{a_k-a_j}{z_k-z_j}
 +\sum_j\left(a_j^2-3a_z(\tau,z_j)\right).
\tag{9}
\]

For a monic polynomial heat solution, \(U=1\), so \(\mathcal B_U=0\). For theta, it retains the surrounding zeros and analytic normalization. Divided differences of \(a\) extend across an internal collision when \(U\) is a unit on a neighborhood of the entire cluster. This prevents them from being mistaken for new pair singularities.

The calculation sharpens the proposed connection: the inverse-square interaction is exactly part of the material derivative of the complete cap source. Equation (8) is generic algebra, not a theta-specific inequality or a claim of novelty.

## Where the Rodgers–Tao subtraction enters

For ordered real roots choose positive reference separations \(r_{jk}=\xi_k-\xi_j\), and put \(d_{jk}=z_k-z_j\), \(u_{jk}=d_{jk}/r_{jk}>0\). The elementary identity underlying the renormalization is

\[
\frac1{d_{jk}^2}
=\frac1{r_{jk}^2}-\frac{2(d_{jk}-r_{jk})}{r_{jk}^3}
 +\frac{V(u_{jk})}{r_{jk}^2},
\qquad V(u)=u^{-2}-1+2(u-1).
\tag{10}
\]

Thus (8) becomes a reference term, a summed linear correction, a relative interaction energy, and \(\mathcal B_U\). On the positive real axis,

\[
V(u)=\frac{(u-1)^2(2u+1)}{u^2}\ge0.
\]

The linear correction must be summed with the cutoff and exterior terms before estimating. A finite interval or nonuniform reference does not make it vanish automatically. If the reference itself moves, its derivative also belongs in any comparison with a reference source product.

For complex gaps use the analytic expression \(\widehat V(u)=u^{-2}-1+2(u-1)\), not the nonholomorphic expression with absolute values. It has no general positivity. In a verified strain disk \(|u-1|\le r<1\), its exact factorization gives

\[
|\widehat V(u)|\le\frac{3+2r}{(1-r)^2}|u-1|^2.
\tag{11}
\]

Such a disk already excludes zero gaps. It is legitimate in a bootstrap only if estimates derived from independent data keep the solution strictly inside it up to the first possible failure. A conditional real-energy bound from an already all-real interval cannot simply be imported as that bootstrap.

For an actual material segment of length \(\eta>0\), with a single logarithm and the required chart bounds,

\[
\log b(\tau-\eta,q)-\log b(\tau,q)
=-\eta\kappa(\tau,q)
 +\eta^2\int_0^1(1-s)\,(D_\tau\kappa)(\tau-s\eta,q)\,ds.
\tag{12}
\]

The error is at most \(\eta^2\sup|D_\tau\kappa|/2\). The same formula holds for \(\log\mathscr D\) with \(K_{\mathscr D}\). It is the requested Taylor estimate along a trajectory; the remaining task is to bound its summed renormalized coefficients and denominators on the complete complex-time geometry.

At an ordinary double collision, \(\mathscr D\) has a simple zero, so \(K_{\mathscr D}\) has residue one. Subtracting a holomorphic reference contribution leaves that residue unchanged. Renormalization can improve the estimate of the regular background; it cannot erase the charge of an actual collision. The singularity \(V(u)\sim u^{-2}\) as \(u\downarrow0\) is precisely what a successful a priori energy bound would have to control.

There is also a direct real-to-cap estimate on a regular flat band. Suppose the selected roots are real at real \(t\), the tubes have constant projective radius \(\rho\), and their source product is holomorphic and nonzero through \(t+i[-Y,Y]\). Reality symmetry gives

\[
I_t=\frac{k_\rho}{\pi}\int_0^Y
        \Re K_{\mathscr D}(t+i\sigma)\,d\sigma.
\tag{B}
\]

If \(M_2=\sup_{0\le\sigma\le Y}|K_{\mathscr D}''(t+i\sigma)|\), Taylor's integral remainder, and the fact that \(K_{\mathscr D}'(t)\) is real, imply

\[
\left|I_t-\frac{k_\rho Y}{\pi}K_{\mathscr D}(t)\right|
\le\frac{k_\rho Y^3}{6\pi}M_2.
\tag{C}
\]

Combining this with (8)–(10) gives, for example, the conditional lower bound

\[
I_t\ge\frac{k_\rho Y}{\pi}
\left[
8\sum_{j<k}r_{jk}^{-2}
-16\sum_{j<k}\frac{d_{jk}-r_{jk}}{r_{jk}^3}
+\mathcal B_U(t)
\right]-\frac{k_\rho Y^3}{6\pi}M_2.
\tag{D}
\]

Here only the nonnegative real relative-energy term was dropped. The linear correction, analytic factor, transverse remainder and complete connecting faces remain. This identifies a concrete route from real renormalization to the physical observable while displaying the additional information it needs. No favorable theta bound on those remaining terms is asserted. In particular, shrinking \(Y\) also changes the entire domain and its closures.

## A collision-free radius that does not assume an interior gap

For a proper isolated two-root cluster, use the existing [two-root equation](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md). The monic quadratic factor \(P\) and

\[
\Delta(\tau)=(z_2-z_1)^2
\]

are holomorphic even if the roots collide. On a fixed outer circle \(\Gamma_R\), containing the two roots in an inner disk of radius \(r<R\),

\[
\Delta'=8+A\Delta,\qquad
A(\tau)=\frac4{2\pi i}\oint_{\Gamma_R}\frac{H_z(\tau,z)}{H(\tau,z)P(\tau,z)}\,dz.
\tag{13}
\]

An independently verified wall floor \(|H|\ge m>0\) and wall upper bound \(|H_z|\le L\) give

\[
|A|\le K:=\frac{4RL}{m(R-r)^2}.
\tag{14}
\]

This bound requires a fixed two-root population and an exterior collar over the whole proposed time domain. It does **not** require the two interior roots to be distinct. The analytic coefficient is defined by the wall integral, not by dividing \(\Delta'-8\) by \(\Delta\).

Anchor at the real right face \(\tau_0=\delta>0\), with \(\Delta_0=\Delta(\delta)\ne0\). Suppose the time domain is star-shaped about \(\delta\), (13) holds on a neighborhood of it, and \(|A|\le K\). Then

\[
\boxed{\quad |\tau-\delta|<T_K(\Delta_0)
\quad\Longrightarrow\quad \Delta(\tau)\ne0,\qquad
T_K(\Delta_0)=
\begin{cases}
K^{-1}\log(1+K|\Delta_0|/8),&K>0,\\
|\Delta_0|/8,&K=0.
\end{cases}\quad}
\tag{15}
\]

**Proof.** Put \(\mu(\tau)=\exp[-\int_\delta^\tau A(w)dw]\). The exact integrating-factor identity gives

\[
\mu(\tau)\Delta(\tau)=\Delta_0+8\int_\delta^\tau\mu(w)dw.
\]

On the straight segment of length \(r_\tau=|\tau-\delta|\), \(|\mu(\delta+s e^{i\theta})|\le e^{Ks}\). Hence the integral term has modulus at most \(8(e^{Kr_\tau}-1)/K\), or \(8r_\tau\) if \(K=0\). Under (15) it is strictly smaller than \(|\Delta_0|\); the right side and therefore \(\Delta\) do not vanish. This proves the finite-cluster claim without an interior noncollision assumption.

For a rectangular time cell \([ -\epsilon,\delta]+i[-Y,Y]\), a sufficient complete condition is

\[
\boxed{\sqrt{(\delta+\epsilon)^2+Y^2}<T_K(\Delta_0).}
\tag{16}
\]

For real-time continuation alone, set \(Y=0\). When \(\Delta_0>0\), the two real roots remain real and simple until the left endpoint. When \(\Delta_0<0\), the same noncollision conclusion holds but the roots remain nonreal; zero charge alone is not reality.

The radius is sharp for the isolated quadratic model \(H=z^2-a^2-2\tau\), where \(K=0\) and the collision occurs at \(\tau=-a^2/2\). In particular, for a collision at zero, \(H=z^2-2\tau\), \(\Delta_0=8\delta\) and \(T_0=\delta\). No positive backward width can satisfy (16). Thus letting the right face approach \(0^+\) does not bypass an endpoint multiple zero.

Equation (15) is an elementary sufficient consequence of the existing scalar equation, not a sharper established theta theorem. It is a useful direct comparator: any proposed topological renormalization should receive the same wall data and be compared with this coupled integrating-factor estimate, rather than with separate absolute endpoint bounds.

## How the width can depend on height

The mean-spacing normalization is

\[
\ell(h)=\tfrac14\log\frac{h}{4\pi},\qquad
\epsilon(h)=\frac{c(h)}{\ell(h)^2}.
\tag{17}
\]

Typical gaps of scale \(\pi/\ell(h)\) suggest time increments of order \(\ell(h)^{-2}\). This is a scaling argument, not a lower bound for every gap. For the two-root pilot at a finite cutoff, the actual available width is constrained by

\[
\epsilon_j<\sqrt{T_{K_j}(\Delta_{0,j})^2-Y_j^2}-\delta_{H_{\max}},
\tag{18}
\]

provided the right side is positive and all isolation bounds hold. Close pairs can force \(c(h)\) much smaller than a fixed constant. Height alone does not determine the local width, and a monotone law is a convenient conservative envelope rather than a proved monotonicity of individual collision distances. Once positive certified widths \(b_j\) are available on increasing height bands, \(\epsilon_j=\theta\min_{k\le j}b_k\), \(0<\theta<1\), gives a decreasing choice. Shared faces still have to be handled consistently.

For the quadratic model the dimensionless parameter controlling a step is its duration divided by the squared gap. A Taylor step that is tiny compared with mean spacing squared can still be too large for an exceptional close pair. A finite uniform bound on an appropriate real relative energy up to the first possible collision could prevent this compression; deriving that bound with constants independent of an interior gap floor is the prospective role for renormalization. Complex-time control remains an additional requirement for (1).

## What a collar across zero would establish

At a fixed compact height window, if the full time-zero jet already has a positive minimum, continuity gives some event-free collar. That existence statement alone is generic. The substantive result would be an explicit width derived from independent source estimates, or a demonstrably cheaper certificate.

A collar containing \(t=0\) excludes multiple zeros there in its covered spatial region. It does not, by itself, exclude simple off-real zeros. To deduce reality at zero one also needs a real-root anchor and complete control of the population and spatial boundaries. A sequence of successful finite certificates gives only the ranges it covers unless an all-height theorem supplies the remaining coverage.

Extending the right edge to a larger positive time requires fresh quantitative continuation or an all-real global anchor. Event-freeness on the negative side does not automatically propagate. For example \(H=z^2-2(\tau-\tau_*)\), \(\tau_*>0\), has no event near zero and has one later. This control lacks theta's source, but defeats a generic topological implication of automatic extension.

[Polymath's Theorem 1.5](https://arxiv.org/html/1904.12438) gives high-height reality and localization for positive time in the regime \(h\ge\exp(C/t)\). It does not automatically anchor a face \(\delta\) of order \(\log^{-2}h\): that regime would require roughly \(t\log h\gtrsim C\). Bridging to \(0^+\) at the proposed microscopic time scale needs additional information. Rodgers–Tao's conclusion \(\Lambda\ge0\) rules out a fixed negative all-real slice; it does not rule out shrinking finite-height collars, nor does event-freeness mean all-realness.

## Control screen and the next calculation

All generic transport and factorization identities above survive the repository's collision controls. On a domain that actually contains a collision, the sufficient inequality (16) must fail or its independent population/wall hypotheses cannot all hold. The following source distinctions indicate where a future theta estimate would need information; they are not evidence that any weak bound derived from that information already rejects a control.

| Control family | Premise absent from a complete canonical-source application |
| --- | --- |
| Euler-factor controls | Unchanged theta source and arithmetic coefficients |
| Finite weighted-square controls | Full reflection and the complete normalized coefficient sequence |
| Reflected super-Gaussian and positive-primitive controls | The unchanged arithmetic square expansion |
| Finite-prime compatible controls | Full reflection and simultaneous complete arithmetic, beyond the specified finite constraints |
| Normalized endpoint controls conditional on RH | Ordinary Dirichlet-series arithmetic; closeness is not an all-height simplicity margin |

Two elementary controls test the specific new calculation. The quadratic event has \(K_{\mathscr D}=1/(\tau-\tau_*)\), so its charge persists after subdivision or regular reference subtraction. For \(H=e^{\ell^2\tau}\sin(\ell z)/\ell\), a fixed population has constant gaps but \(K_{\mathscr D}=m\ell^2\); the analytic-factor term in (9) is essential. The [exact arithmetic check](../numerics/check_material_jet_energy_20261023.py) verifies the finite algebra, not a theta estimate; the [self-review](../reviews/01_MOVING_COLLAR_AND_MATERIAL_ENERGY_SELF_REVIEW_20261023.md) records the scope.

The next bounded experiment is one finite height band. For the author's refined cap objective, estimate \(I_{-\epsilon}-S_\epsilon\) directly as a coupled expression, using (8) and the transverse estimate (C) where their hypotheses are paid. Compare its certified lower bound with a direct bound for \(I_0\) from the same source information. If exact equality or collision exclusion is also required, establish complete spatial-wall data and a right-cap discriminant enclosure and compare the allowable width with (15). A sharper transferred bound, larger certified width, lower data cost, or a useful bound on exceptional colliding cells would justify extending the construction. No new manuscript or snapshot is needed for that comparison.
