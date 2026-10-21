# Cap phase concentration and the finite time quadratic baseline

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this chat's turn metadata.
Internal analytic observations and same-assistant checks; no specialist
review or original theta endpoint exclusion.

The shrinking cap does have a singular limiting phase distribution.
That concentration occurs for every fixed adjacent pair under the
declared late-time assumptions, irrespective of whether its roots share
a multiple birth. Separately, subtracting only the leading small-time
Hermite tube profile leaves a correction even for the exact quadratic
model. These two observations sharpen the HMC-05 comparison; neither
supplies its missing arithmetic estimate.

Read with the [program](../research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md),
[progress](../research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md),
[result index](../../../../../../../result-summaries/README.md),
[heat summary](../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[control register](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../../../avoid/README.md), especially
[target reformulations](../../../../../../../avoid/01_restating_the_target.md)
and [control premises](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).

## Spatial cap phase and collision index

Write \(J=H+iH_x\), \(E=H^2+H_x^2\), and

\[
\rho=-\partial_x\arg J=\frac{H_x^2-HH_{xx}}{E}.
\]

Between adjacent simple real roots \(a<b\), \(H\) has a fixed sign,
and the two endpoint derivatives have opposite signs. The jet stays in
one open half-plane between the endpoints. Consequently its continuous
phase decreases by exactly \(\pi\), as in Note 21 MT3–MT4. This is an
open-cap phase change, not an integer winding number of a closed curve.
An outer interval containing \(m\) successive simple roots has phase
decrease \((m-1)\pi\), whether or not those roots share a birth.

A local index of \(J\) around an isolated zero in the \((t,x)\) plane
is a different quantity: \(J=0\) means \(H=H_x=0\). An initially distinct
simple pair has no such event at either endpoint at time zero. A proposed
space-time index comparison must specify its closed contour, orientation,
boundary nonvanishing and every terminal contribution; the spatial cap
phase does not provide that comparison by itself.

## A shrinking cap necessarily concentrates its phase

Assume RH and the paired real-root product used in Note 19. In an
adjacent gap put \(s=H_x/H\). Then

\[
\rho=\frac{-s_x}{1+s^2},\qquad
-s_x=\sum_r\frac1{(x-r)^2}>0.
\tag{CP1}
\]

The reciprocal-square sum includes all signed roots. At the unique
stationary point \(x_*(t)\in(a,b)\), \(s=0\), and therefore

\[
\rho(t,x_*)=-\frac{H_{xx}}H(t,x_*)
\ge\frac1{(x_*-a)^2}+\frac1{(b-x_*)^2}
\ge\frac8{g(t)^2},\qquad g=b-a.
\tag{CP2}
\]

Thus the phase density must diverge whenever this gap shrinks to zero.
This conclusion uses only the all-real product and adjacency. It does not
require a multiple birth and does not imply \(J=0\) at any finite time.

By Note 20's fixed-label asymptotics, \(a(t),b(t)\to0\),

\[
g(t)\sim\pi/L_t,\qquad L_t\sim\tfrac14\log t.
\]

For the positive measure

\[
d\mu_t(x)=\mathbf1_{[a(t),b(t)]}\rho(t,x)\,dx,
\]

the support shrinks to zero and the mass is exactly \(\pi\). Hence

\[
\mu_t\rightharpoonup\pi\delta_0.
\tag{CP3}
\]

Indeed, for every continuous test function \(f\), the difference from
\(\pi f(0)\) is bounded by
\(\pi\sup_{x\in[a,b]}|f(x)-f(0)|\to0\). For a fixed block of
\(m\) roots the mass is \((m-1)\pi\). This is a statement for each
fixed finite block, not an interchange with an infinite sum of caps.

## The cosine model and terminal regularity

The late-time comparison \(H(t,x)\approx A(t)\cos(L_t x)\) gives
the following exact identities for the comparison function at fixed
\(A>0,L>0\):

\[
\rho_L(x)=\frac{L^2}{\cos^2(Lx)+L^2\sin^2(Lx)},\quad
\int_{(k-1/2)\pi/L}^{(k+1/2)\pi/L}\rho_L\,dx=\pi.
\tag{CP4}
\]

Its height at \(c=k\pi/L\) is \(L^2\). At \(x=c+q/L^2\),

\[
L^{-2}\rho_L(c+q/L^2)\longrightarrow\frac1{1+q^2}.
\tag{CP5}
\]

The peak width is therefore \(L^{-2}\), smaller than the cap width
\(\pi/L\). Nevertheless \(|J|/A\ge1\) for \(L\ge1\): the density
can diverge without the jet approaching zero in this normalization.
The comparison with moving \(A,L\) is not asserted to be an exact heat
solution.

For the actual theta field, a continuous locally uniform terminal limit
of \(H(t,x)/H(t,0)\) on a fixed neighborhood of zero is impossible under
these root asymptotics. Its value at zero is one, while a zero \(x_1(t)\)
approaches zero. Uniform convergence to a continuous function would force
the limiting value at zero to be both one and zero. Rescaling to
\(z=L_t x\) gives the controlled cosine limit, but the physical jet
becomes \(F+iL_tF_z\); the growing derivative factor remains.

An alternative expression for the phase integral could support a direct
contradiction if it proved nonconcentration specifically under a multiple
birth assumption. A bound such as

\[
\int_{a(t)}^{b(t)}\rho\,dx\le\omega(g(t)),
\qquad\omega(\ell)\longrightarrow0
\tag{CP6}
\]

would suffice. CP6 is a description of the missing estimate, not an
established milestone. It cannot hold for all fixed adjacent theta caps,
since CP3 already proves the opposite behavior. Uniform \(L^1\)
boundedness alone also does not suffice: the cap mass is already \(\pi\).
The multiple-birth condition must survive into the proposed estimate.

## The cap image on the higher dimensional jet surface

Investigation 21 [Note 61](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/61_JET_SURFACES_REAL_GAUSS_MAP_AND_ORIENTED_TURNING_20261015.md)
constructs the actual complex surface

\[
X_t(z,w)=(P_t(z),H(t,z),w),\qquad \partial_zP_t=H,
\]

with induced metric

\[
ds^2=(|H|^2+|H_z|^2)|dz|^2+|dw|^2.
\tag{CP10}
\]

The surface has real dimension four and lies in \(\mathbb C^3\).
Its stated embeddings are coassociative in \(\mathbb R^7\) and Cayley in
\(\mathbb R^8\) on the regular locus. These are actual calibrations, not
just terminology; the standard inclusions are verified by
[Lotay Propositions 6.5(b) and 7.3(a)](https://arxiv.org/html/1810.08709).

The physical cap at fixed \(w\) is the real curve
\((P_t(x),H(t,x))\). Its induced length is

\[
\ell_t=\int_a^b\sqrt{H^2+H_x^2}\,dx.
\tag{CP11}
\]

Small coordinate length \(g=b-a\) alone gives no upper bound forcing
\(\ell_t\to0\). In CP4's cosine model, choose \(P=A\sin(Lx)/L\) and
put \(z=Lx\). The curve divided by its amplitude is

\[
\frac1A(P,H)=\left(\frac{\sin z}{L},\cos z\right),\qquad
(k-\tfrac12)\pi\le z\le(k+\tfrac12)\pi.
\tag{CP12}
\]

It is a narrow half-ellipse. Its length divided by \(A\) is

\[
\frac{\ell_L}{A}
=\int_{(k-1/2)\pi}^{(k+1/2)\pi}
  \sqrt{L^{-2}\cos^2z+\sin^2z}\,dz\longrightarrow2.
\tag{CP13}
\]

For \(L\ge1\), the integrand is bounded by one and tends to
\(|\sin z|\), proving the limit by dominated convergence. Thus the
coordinate cap shrinks while this normalized image curve does not.
CP13 is an exact comparison-model calculation, not a new full-surface
theta area estimate.

At an actual common zero \(H=H_z=0\), the differential of \(X_t\)
loses one complex rank and CP10 degenerates. The model
\(H(t,z)=z^2-2t\) gives \((P,H)=(z^3/3-2tz,z^2-2t)\);
at zero time this is a cusp, while all regular complex surface patches
remain calibrated. Adding a coordinate, as in \((z,P,H,w)\), makes an
immersive graph but changes the metric coefficient to \(1+|H|^2+|H_z|^2\).
It does not prove nonvanishing of the physical first jet.

The marked real Gauss direction \([H:H_x]\) retains the signed angle
\(\alpha=\arg(H+iH_x)\). Intrinsic curvature instead squares its signed
numerator, so a curvature magnitude estimate alone need not give the
one-sided angle estimate. Note 61 already distinguishes these quantities.
Its predecessor criterion uses
\(\alpha_j=\arg(h_j+i h_{j+1})\), where \(h_j=\partial_x^jH\) and
\(j=0\) for an even multiplicity, \(j=1\) for an odd multiplicity.
It concerns a *positive* angle increment approaching \(\pi/2\) on an
interval of length \(c\sqrt{T-t}\) before a finite multiple collision.
For \(j=1\), the denominator is \(h_1^2+h_2^2\), not the physical
first-jet energy; the predecessor interval must retain this pair's
nonvanishing. Negative angle increments on later all-real caps remain
allowed. The local calculation can be centered at \(T=0\), using negative
heat times; a corresponding theta-specific one-sided modulus would be a
direct endpoint consumer. Such a modulus has not been proved, and its
derivation from the original arithmetic remains the research task.

For any proposed higher-dimensional replacement, the relevant elementary
estimate is

\[
\left|\int_{\Sigma_t}\Omega_t\right|
\le \operatorname{Vol}_k(\Sigma_t)\,
   \sup_{\Sigma_t}|\Omega_t|_{\mathrm{comass}},
\]

where \(\Sigma_t\) is the actual \(k\)-dimensional integration surface
and \(\Omega_t\) its \(k\)-form. A nonzero limiting flux and vanishing
induced volume force the form norm to diverge; they do not themselves
contradict smoothness at every finite time. A contradiction requires a
separate uniform norm or nonconcentration bound, together with the full
physical-trace comparison and every boundary contribution. CP13 shows
why coordinate shrinkage alone cannot supply the volume premise.

## A finite time correction already present in the quadratic control

This section concerns \(t\downarrow0\), independently of the preceding
\(t\to\infty\) limit. Use the translated heat polynomial
\(H(t,x)=(x-a_0)^2-2t\), set \(\tau=\sqrt{2t}\), and choose
\(\eta=r\tau\). Note 21 MT22 gives, after \(x-a_0=\tau y\),

\[
I^{\rm quad}_{r\tau}(\tau^2/2)
=\pi+2\tau r^2\int_{-1}^{1}
\frac{dy}{4y^2+\tau^2(1-y^2)^2}.
\tag{CP7}
\]

Put \(D_\tau(y)=4y^2+\tau^2(1-y^2)^2\) and
\(J_2=\int_{-1}^1y^2/D_\tau(y)\,dy\). The exact cap-phase identity is

\[
2\tau\int_{-1}^{1}\frac{1+y^2}{D_\tau(y)}\,dy=\pi,
\]

so

\[
I^{\rm quad}_{r\tau}-\pi(1+r^2)=-2\tau r^2J_2.
\tag{CP8}
\]

Since \(0\le y^2/D_\tau\le1/4\),

\[
0\le\tfrac12-J_2
=\frac{\tau^2}{4}\int_{-1}^{1}
\frac{(1-y^2)^2}{D_\tau(y)}\,dy
\le\frac{\pi\tau}{8}.
\]

Consequently the fully bounded comparison is

\[
\boxed{0\le I^{\rm quad}_{r\tau}-\pi(1+r^2)+r^2\tau
\le\tfrac\pi4r^2\tau^2.}
\tag{CP9}
\]

In particular \(I^{\rm quad}_{r\tau}=\pi(1+r^2)-r^2\tau+O_r(\tau^2)\).
The negative correction after subtracting the leading profile is already
compatible with an exact double birth. It is not arithmetic separation.
For a subsequent comparison, subtracting the exact CP7 baseline removes
this known finite-time geometric contribution. No rate or sign for the
remaining theta difference is proved here.

## Scope of the control comparisons

CP1–CP2 use an all-real product; CP3 additionally requires the declared
root limit. The RH-conditional Euler-factor and
close positive endpoint controls satisfy that generic hypothesis, with
their own source data, while failing unchanged theta coefficients or
ordinary Dirichlet arithmetic. Weighted-square and finite-prime controls
without an all-real slice are not assigned CP1. Polynomial controls check
the local heat and phase laws; the quadratic lacks the infinite theta
spectrum and its late-time saddle. CP9 is solely a quadratic comparison,
not a claim that every source has the same next coefficient.

The Hermite normalization in Note 22 was checked against
[DLMF 18.12.16](https://dlmf.nist.gov/18.12.E16), and the paired root law
and local splitting against [Polymath Proposition 3.1](https://arxiv.org/html/1904.12438v2#S3).
The proofs above are direct analytic calculations. No theta quadrature,
event certificate or numerical extrapolation enters them. The companion
[review](../reviews/22_HMC06_GATE_AND_ENDPOINT_LIMIT_REVIEW_20261021.md)
states the program implications.
