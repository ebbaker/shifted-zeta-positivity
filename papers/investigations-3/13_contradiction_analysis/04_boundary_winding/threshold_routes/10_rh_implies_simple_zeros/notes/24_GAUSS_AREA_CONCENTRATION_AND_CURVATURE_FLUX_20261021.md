# Gauss area concentration and curvature flux at a multiple endpoint

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.
Analytic derivation with same-assistant review and finite exact checks.

The jet surface has a finite, nonzero concentration of curvature at a
multiple endpoint. With the Gauss sphere normalized to area \(\pi\), an
isolated zero of multiplicity \(m\) contributes \(\pi(m-1)\) of concentrated
Gauss area. The corresponding curvature integral of the complex curve
contributes \(-2\pi(m-1)\). Thus an alternative surface integral can remain
bounded while its density becomes singular. This answers the proposed
bounded-integral test for the induced jet surface; it supplies no theta
endpoint exclusion.

Read with [Note 23](23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md),
the [HMC program][program], [result index][results], [geometry summary][geometry],
[controls][controls], and [avoid index][avoid], particularly
[reformulations][a01], [shared premises][a02], and [scope][a07].
This is a quantitative local concentration law and a scoped diagnostic.
It does not claim a new exclusion criterion as progress toward simplicity.

## 1. The observation and its normalization

Translate a proposed endpoint to \((t,z)=(0,0)\). Let \(H\) be holomorphic
jointly near that point, real on the real \((t,z)\) slice, satisfy
\(H_t=-H_{zz}\), and have
\[
H(0,z)=z^m g(z),\qquad m\ge2,\quad g(0)\ne0.
\]
The original theta field and finite heat polynomials meet the local
analytic hypothesis. Set
\[
\mathscr E_t=|H|^2+|H_z|^2,\qquad
D_t=HH_{zz}-H_z^2,\qquad
d\mu_t=\frac{|D_t|^2}{\mathscr E_t^2}\,dx\,dy.
\tag{GA1}
\]
The energy is complex jet energy; on the real slice it agrees with the
physical energy. It is not the physical-line denominator used off that
line in HMC Note 21.

On the regular locus, the Gauss map \([H:H_z]\) takes values in
\(\mathbb{CP}^1\) with metric
\(|d\zeta|^2/(1+|\zeta|^2)^2\), whose area is \(\pi\).
The determinant identity in Investigation 21 [Note 61][g61] gives
\[
d\mu_t=\frac14\Delta\log\mathscr E_t\,dx\,dy,\qquad
K_t\,dA_t=-2\,d\mu_t,\qquad dA_t=\mathscr E_t\,dx\,dy.
\tag{GA2}
\]
Here \(K_t\) is the Gaussian curvature of the complex curve
\(z\mapsto(P(t,z),H(t,z))\), with \(P_z=H\).
The curvature normalization agrees with the complex-curve specialization
of [Kawakami–Watanabe, equations (24)–(25)][kw].

Choose a small fixed disk \(D_R\) on which \(g\) is nonzero. For sufficiently
small nonzero real \(t\), every zero of \(H(t,\cdot)\) in that disk is
simple, so \(\mathscr E_t>0\) throughout the closed disk. To justify this
without a denominator assumption, choose \(\tau^2=2t\). Uniformly for
bounded complex \(y\),
\[
\frac{H(t,\tau y)}{g(0)\tau^m}
=\operatorname{He}_m(y)+O(\tau).
\]
The Hermite roots are simple; the implicit-function theorem or disjoint
Rouché disks supplies their \(m\) simple perturbations, for either ray of
\(\tau\). A separate Rouché argument on \(\partial D_R\) counts exactly
\(m\) zeros. This excludes additional common zeros in the disk.
No all-real-root hypothesis is needed.

Consequently the area has the exact boundary expression
\[
A_t(R):=\mu_t(D_R)
=\frac14\int_{\partial D_R}\partial_n\log\mathscr E_t\,ds.
\tag{GA3}
\]
There is no omitted inner boundary for \(t\ne0\).

## 2. The finite concentration law

At zero time factor the vector, not just its projective quotient:
\[
(H,H_z)=z^{m-1}\bigl(zg,\,mg+zg'\bigr),\qquad
\mathscr E_0=|z|^{2m-2}e(z),
\]
\[
e(z)=|zg(z)|^2+|mg(z)+zg'(z)|^2>0.
\tag{GA4}
\]
The canceled Gauss map \([zg:mg+zg']\) is regular through zero. Let
\(d\mu_{\rm reg}=\frac14\Delta\log e\,dx\,dy\) be its smooth
nonnegative Gauss-area measure.

Boundary convergence in GA3 is smooth and gives
\[
\boxed{\lim_{t\to0,\ t\ne0}A_t(R)
=\pi(m-1)+\mu_{\rm reg}(D_R).}
\tag{GA5}
\]
Indeed the outward derivative of \((2m-2)\log|z|\) contributes
\((1/4)(2\pi R)(2m-2)/R=\pi(m-1)\). The remaining boundary integral
equals \(\mu_{\rm reg}(D_R)\).

In fact the right side of GA3 is real analytic in \(t\) through zero:
the fixed circle has a uniform positive energy floor and its jets are
analytic in real time. It defines a real-analytic extension of \(A_t(R)\)
whose value at zero is GA5. Directly integrating only the canceled
endpoint density instead gives \(\mu_{\rm reg}(D_R)\). These differ by
\(\pi(m-1)\). Thus the alternative expression removes any singularity
in the integral's time dependence without removing the concentrated
mass. Passing the pointwise limiting density through the integral is
the unjustified step; there is no uniform-integrability conclusion.

This also proves the local weak limit
\[
\boxed{\mu_t\rightharpoonup
\mu_{\rm reg}+\pi(m-1)\delta_0.}
\tag{GA6}
\]
For clarity, no interchange of an unbounded inner window and time is used.
On each closed annulus away from zero the densities converge smoothly.
GA5 bounds the total mass on a fixed disk and identifies the mass on
every smaller disk. Splitting a continuous compactly supported test
function at radius \(\epsilon\), the error in replacing it by its value
at zero on the small disk is bounded by its modulus of continuity times
that uniformly bounded mass. Take \(t\to0\), then \(\epsilon\to0\).

Equivalently, \(\Delta\log|z|=2\pi\delta_0\) gives the defect in
\(\frac14\Delta\log\mathscr E_0\). This agrees with
[Demailly's Lelong–Poincaré formula (1.20), p. 12][dem]; the boundary
argument above proves the needed special case directly. The canceled
Gauss map by itself omits the defect. In the induced metric the
corresponding curvature measure has atom \(-2\pi(m-1)\), consistent with
the existing cone angle \(2\pi m\).

### An explicit boundary error

Take bounds \(M_j\ge |H_{z^j}(t,z)|\), \(0\le j\le4\), for
\(|t|\le t_*\) and \(z\in\partial D_R\). Put
\[
\begin{aligned}
b&=2(M_0M_2+M_1M_3),\\
c&=2(M_0M_1+M_1M_2),\\
d&=2(M_0M_3+M_1M_2+M_1M_4+M_2M_3),\\
e_R&=\min_{\partial D_R}\mathscr E_0>0.
\end{aligned}
\]
Then \(|\partial_t\mathscr E|\le b\),
\(|\partial_n\mathscr E|\le c\), and
\(|\partial_t\partial_n\mathscr E|\le d\). For
\(|t|b\le e_R/2\),
\[
\boxed{\left|A_t(R)-\pi(m-1)-\mu_{\rm reg}(D_R)\right|
\le \pi R|t|\left(\frac d{e_R}+\frac{2cb}{e_R^2}\right).}
\tag{GA7}
\]
This follows by differentiating
\(\partial_n\log\mathscr E=\mathscr E_n/\mathscr E\), using the floor
\(e_R/2\) on the fixed boundary, and integrating GA3. If \(b=0\) the
condition on \(t b\) is automatic. The disk must also meet the earlier
simple-splitting condition.

For the theta source one may take the complete moments
\[
M_j=\int_0^\infty u^j e^{t_*u^2+Ru}\Phi(u)\,du,
\]
with the source-tail payments of Note 21. The boundary floor is an
explicit event-dependent input, not an asserted uniform-in-height floor.
GA7 proves finite area convergence; it is not a small-area bound.

## 3. A closed formula for the double control

For \(H(t,z)=z^2-2t\), write \(t=-s\), \(s>0\).
On \(|z|=R\), put \(q=R^2\). Then
\[
\mathscr E_{-s}(Re^{i\theta})
 = a+b_0\cos 2\theta,\quad
a=q^2+4q+4s^2,\quad b_0=4sq.
\]
The elementary circle mean is
\((2\pi)^{-1}\int\log(a+b_0\cos2\theta)\,d\theta
=\log((a+\sqrt{a^2-b_0^2})/2)\).
For example, write \(a+b_0\cos2\theta
=C|1+\lambda e^{2i\theta}|^2\) with
\(C=(a+\sqrt{a^2-b_0^2})/2\) and \(|\lambda|<1\);
the log of the last factor has mean zero by its convergent series.
Differentiation in GA3 yields the exact expression
\[
\boxed{\frac{A_{-s}(R)}{\pi}
=1+\frac{R^4-4s^2}
{\sqrt{(R^4+4R^2+4s^2)^2-16s^2R^4}}.}
\tag{GA8}
\]
The denominator is positive. Its square minus the squared numerator is
\(8q(q^2+2q+4s^2)>0\); hence \(0<A_{-s}(R)<2\pi\).
The whole-plane area is exactly \(2\pi\) for every \(s>0\).

At fixed \(R>0\),
\[
A_{-s}(R)\longrightarrow
\pi+\frac{\pi R^2}{R^2+4}.
\tag{GA9}
\]
At the finer shrinking scale \(R=Cs\),
\[
A_{-s}(Cs)\longrightarrow
\frac{\pi C^2}{1+C^2}.
\tag{GA10}
\]
For example, \(C=1\) captures asymptotically \(\pi/2\), even though
that coordinate disk shrinks to a point. The remaining local concentration
is captured by taking larger fixed \(C\) after the small-time limit.

Changing the time from \(-s\) to \(+s\) is a rotation \(z\mapsto iz\)
in this energy: \(\mathscr E_{+s}(iz)=\mathscr E_{-s}(z)\).
Thus the disk areas are exactly equal before and after the event.
On the marked real line, however, the central angular derivatives are
\(+1/s\) and \(-1/s\). This gives an exact control showing why unsigned
Gauss area loses the orientation needed by the predecessor criterion.

More generally the pure degree-\(m\) heat polynomial has whole-plane
Gauss area \(\pi m\) for nonzero time: GA3 at \(R\to\infty\) uses
\(\log\mathscr E_t=2m\log R+O(R^{-1})\) with differentiated error.
At zero time its canceled Gauss map has area \(\pi\). The difference is
exactly GA6's \(\pi(m-1)\).

## 4. The local surface profile and its curvature norms

The real inner profile is already proved in Investigation 22
[Inner turning Note 01][inner]; it is not a new result of this round.
Here is its complex-disk consequence. At multiplicity \(m=2r+j\), put
\(W=\partial_z^jH\), \(j\in\{0,1\}\),
\(k=\partial_z^{2r}W(0,0)/r!\), and let \(\chi(s)\) be the full
stationary predecessor of \(W\).
On every fixed complex disk \(|q|\le C\), with
\(z=\chi(s)+(s/r)q\), joint analyticity gives
\[
W=k s^r(1+O_C(s)),\quad
W_z=k s^r(q+O_C(s)),\quad
W_{zz}=k r s^{r-1}(1+O_C(s)).
\tag{GA11}
\]
The real proof's convergent power series extends to bounded complex
coordinates and retains its derivative remainders. In particular \(W\)
is zero-free there for small \(s\). Therefore
\[
d\mu_{W,-s}
 =\left(\frac1{(1+|q|^2)^2}+O_C(s)\right)dA_q,
\quad
\mu_{W,-s}(|z-\chi(s)|\le Cs/r)
=\frac{\pi C^2}{1+C^2}+O_C(s).
\tag{GA12}
\]
This is a genuine two-dimensional concentration, with finite mass.

The induced curve area and curvature satisfy uniformly on that disk
\[
dA_W=\frac{|k|^2}{r^2}s^{2r+2}
(1+|q|^2)(1+O_C(s))\,dA_q,
\]
\[
K_W=-\frac{2r^2}{|k|^2}s^{-2r-2}
(1+|q|^2)^{-3}(1+O_C(s)).
\tag{GA13}
\]
Consequently, for fixed \(p\ge1\),
\[
\int |K_W|^p\,dA_W
=2^p r^{2p-2}|k|^{2-2p}s^{(2r+2)(1-p)}
\left\{\int_{|q|\le C}(1+|q|^2)^{1-3p}\,dA_q+O_C(s)\right\}.
\tag{GA14}
\]
The \(p=1\) integral has finite nonzero limit
\(2\pi C^2/(1+C^2)\), whereas every \(p>1\) integral diverges.
All unnormalized derivatives of a polynomial control remain uniformly
bounded on a fixed compact neighborhood, so those derivative upper
bounds alone cannot supply a uniform \(p>1\) curvature bound.

For \(j=1\) this is the surface of \(W=H_z\), with energy
\(|H_z|^2+|H_{zz}|^2\), not the original first-jet surface.
Its local concentration count at the endpoint is \(m-2\), whereas GA6
for the original first jet has count \(m-1\). The earlier real
comparison \(E_1/E\to1+|q|^2\) holds on the real inner window; it
must not be replaced by equality.

## 5. The four-dimensional integral

For the actual complex surface \(X=(P,H,w)\), let \(\omega_t\) and
\(\operatorname{Ric}_t\) be its Kähler and Ricci forms. Note 61 gives
\[
\omega_t=\frac i2(\mathscr E_t\,dz\wedge d\bar z+dw\wedge d\bar w),
\qquad \operatorname{Ric}_t=-2\,d\mu_t.
\]
The last identity treats \(d\mu_t\) as a two-form in the \(z\) plane.
For any bounded transverse domain \(B\subset\mathbb C_w\),
\[
\boxed{-\int_{D_R\times B}\operatorname{Ric}_t\wedge\omega_t
=2\,\operatorname{Area}(B)\,A_t(R).}
\tag{GA15}
\]
Thus the concentrated contribution is
\(2\pi(m-1)\operatorname{Area}(B)\), supported on
\(\{0\}\times B\) in the limit. If \(B\) also shrinks, the raw contribution
shrinks with its area. Dividing by that area restores the same finite
two-dimensional concentration. The scalar-curvature integral has twice
the magnitude in GA15, since scalar curvature is \(2K_t\).
The coassociative or Cayley inclusion does not alter these induced
metric calculations.

This result concerns this induced product surface and this curvature
form. It is distinct from Note 21's physically weighted polarized
Stokes integral, and supplies no comparison theorem for arbitrary
nonproduct surfaces or different quaternionic/octonionic observations.

## 6. Control screen and implication for HMC

The concentration theorem requires only a local analytic heat family
and a finite multiple event. Substitution of the catalogued event germs
therefore gives the same mass law in each applicable control:

| Control | Response to this calculation | Original-theta premise it does not preserve |
| --- | --- | --- |
| Pure and asymmetric heat polynomials | GA6 and GA12–GA14 apply; the pure double has exact GA8 | Complete theta source, arithmetic and infinite zero set |
| Euler-factor controls at their finite events | Same local law; no all-real slice is required by it | Unchanged Euler coefficients and original completion data |
| Weighted-square and finite-prime controls | Same local law at their certified or proved events | Full source reflection and unchanged coefficients; no all-real heat slice is asserted |
| Reflected super-Gaussian and smooth positive-primitive controls | Same law at their double events | Canonical integer-square theta expansion |
| BW10 Note 05 close positive endpoint controls | Same double concentration while retaining their RH-conditional all-real positive-time evolution | Ordinary Dirichlet-series arithmetic |

This screen uses the already established analytic event germs; no new
source quadrature or damping threshold is claimed. The identities are
expected to pass these controls. They cannot distinguish theta from them.
For the older counter-kernel and smooth-density controls, application is
only at any verified finite analytic heat event, not an assumption of
their satisfying the theta arithmetic or global root hypotheses.

Bounded Gauss area, bounded absolute total curvature, smooth ambient
calibration and uniform upper bounds on the unnormalized jets are all
compatible with the collision. The **specific proposed inference from
bounded surface integral to absence of a singular endpoint fails for
this observation**. The signed real-angle bound remains unproved.
A uniform integrability or stronger curvature estimate would add an
assumption absent from these bounds; merely naming it is another
conditional reformulation, not a new HMC milestone.

HMC-05 remains open and HMC-06 gated. The immediate usable output is the
paid concentration formula and exact control, which prevent mistaking a
finite geometric integral for endpoint regularity. The first
source-dependent correction in the original signed tube observation
remains a different calculation, with the exact quadratic baseline of
Note 23 removed. No result here settles its sign.

## 7. Verification

The [finite replay][checker] checks the complex determinant normalization,
both signs of the heat polynomials, the endpoint common factor, the
pure radial boundary flux, asymmetric complex inner coefficients for
both parity branches, and the exact quadratic disk formula. Its
[record][record] includes rational square-root enclosures and binds its
two existing algebra dependencies. These checks do not prove the
analytic limits or estimate theta.

[Review 23][review] audits the boundary proof, signs, normalization,
parity scope and control response. It is by the same assistant.

[program]: ../research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[g61]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/61_JET_SURFACES_REAL_GAUSS_MAP_AND_ORIENTED_TURNING_20261015.md
[inner]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/02_signed_turning_control/01_INNER_TURNING_PROFILE_20261015.md
[kw]: https://link.springer.com/article/10.1007/s12220-024-01721-7
[dem]: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/analmeth_book.pdf
[checker]: ../numerics/check_hmc_gauss_concentration.py
[record]: ../numerics/HMC_GAUSS_CONCENTRATION_CHECKS_20261021.json
[review]: ../reviews/23_GAUSS_AREA_AND_CURVATURE_FLUX_REVIEW_20261021.md
