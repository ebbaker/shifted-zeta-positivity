# Multiplicity-selective Chern and Hopf observations

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from the current turn metadata.
Analytic derivation and same-assistant assessment; no independent review.

The author's proposed distinction is available: localized defects can
vanish at every simple zero while detecting all higher multiplicities.
The Gauss-area defect of [Note 24][n24] already has weight \(m-1\).
The complex heat-jet intersection in [Investigation 22 Note 08][g08]
has weight \(\binom m2\); below it is expressed as a relative second
Chern number, a Hopf integral and an explicit positive regularized
four-dimensional measure. The intersection count itself is inherited.
These observations do not supply an upper bound for theta.

Read with the [result index][results], [geometry summary][geometry],
[collision controls][controls] and [avoid index][avoid], particularly
[reformulations][a01], [coordinate lifts][a03] and [scoped conclusions][a07].
This is a diagnostic and a dictionary between existing invariants, with
an explicit integral normalization. Vanishing of all relevant defects
is a reformulation of simplicity, not an additional established premise.

## 1. A defect that already removes the simple-zero contribution

At fixed time let \(f(z)=(z-a)^m g(z)\), \(g(a)\ne0\), on a small disk.
Then
\[
(f,f')=(z-a)^{m-1}\big((z-a)g,\,mg+(z-a)g'\big).
\tag{MC1}
\]
The second vector is nonzero at \(a\). Its projective Gauss-area measure
\(\mu_{\rm reg}\) is smooth. Distributionally,
\[
\frac1{4\pi}\Delta\log(|f|^2+|f'|^2)
 =\frac1\pi\mu_{\rm reg}+(m-1)\delta_a.
\tag{MC2}
\]
Here the left side is a distributional measure, not the ordinary density
with the singular point deleted. MC2 follows directly from
\(\Delta\log|z-a|=2\pi\delta_a\); compare the
[Lelong–Poincaré formula][demailly], equation (1.20).

Thus the excess divisor of the common factor of \((f,f')\) vanishes at
a simple zero. The total smooth Gauss area need not vanish there. In
Note 24's heat resolution the extraction is equivalently
\[
\lim_{R\downarrow0}\lim_{t\to0,\ t\ne0}
 \frac{\mu_t(D_R(a))}{\pi}=m-1.
\tag{MC3}
\]
The limits have this order. At a fixed nonzero time the simple-split
configuration has no defect atom.

More generally, the common zero order of
\((f,f',\ldots,f^{(k)})\) is \((m-k)_+\). These successive defects
detect multiplicity above \(k\); their consecutive differences detect
the thresholds \(m\ge k+1\). This elementary hierarchy adds no
arithmetic information.

## 2. The relative second Chern number

Complexify physical heat time and spectral position, and set
\[
G(t,z)=(H(t,z),H_z(t,z)),\qquad H_t=-H_{zz}.
\]
These coordinates are not the elliptic parameter and elliptic coordinate
of the arithmetic hyperkähler family. Suppose \(H(0,z)\) has exact
order \(m\ge2\) at \(a\). Investigation 22 Note 08 proves that \(G\)
has an isolated zero there and
\[
L_m:=\dim_{\mathbb C}\mathcal O_{(0,a)}/(H,H_z)
 =\operatorname{ord}_{t=0}\operatorname{Disc}_z P(t,z)
 =\binom m2,
\tag{MC4}
\]
where \(P\) is the local monic Weierstrass polynomial. In brief,
the \(m\) roots split as \(z_i(r^2)=a+\lambda_i r+O(r^2)\),
with distinct Hermite numbers \(\lambda_i\). Each squared pair
difference contributes one order in \(t=r^2\) to the discriminant.
The resultant identifies this order with the displayed local length.

Let \(B\) be a sufficiently small real four-ball about the event,
with complex orientation, and \(S=\partial B\). The normalized map
\(n=G/\|G\|:S\to S^3\) has degree \(L_m\). Equivalently,
\[
\left\langle c_2(B\times\mathbb C^2,G|_S),[B,S]\right\rangle=L_m.
\tag{MC5}
\]
This is the **relative top Chern/Euler obstruction** specified by the
nonzero boundary section. The top Chern class counts holomorphic
section zeros with their intersection multiplicities; see
[Stacks, Lemma 42.44.1][stacks] and the
[Thom/Euler account][ionel], pp. 43 and 52. A small regular target
perturbation also proves MC5 directly: there are \(L_m\) preimages,
each with positive real Jacobian.

The ordinary bundle on \(B\) is trivial and its absolute \(c_2\) is zero.
There is no contradiction: \(H^4(B)=0\), whereas
\(H^4(B,S;\mathbb Z)=\mathbb Z\). Forgetting the boundary section
forgets the local obstruction. At \(m=1\), \(H_z(0,a)\ne0\); \(G\)
is nonzero on a whole small ball and the relative number is zero.

## 3. A Hopf connection and a positive measure

On \(S\), use the real connection form
\[
\alpha=\operatorname{Im}(n^\dagger dn)
 =\frac{\operatorname{Im}(\overline H\,dH+
                 \overline{H_z}\,dH_z)}{|H|^2+|H_z|^2}.
\]
For the standard unit sphere in \(\mathbb C^2\), with its outward
orientation, \(\alpha_{\rm std}\wedge d\alpha_{\rm std}=2\,dV_{S^3}\).
Since its volume is \(2\pi^2\),
\[
\frac1{4\pi^2}\int_S\alpha\wedge d\alpha=\deg n=L_m.
\tag{MC6}
\]
This is also the Hopf invariant of
\([H:H_z]:S^3\to\mathbb{CP}^1\): the normalized sphere-area pullback
is \(d\alpha/(2\pi)\). This applies
[Whitehead's integral formula as stated by Rudolph, §1][hopf].
Only that formula is used, not an identification with his different
enhanced Milnor invariant.
This uses a three-dimensional link in complex heat spacetime. The
fixed-time projective Gauss map in MC1 still extends across its
spatial zero; its one-dimensional boundary does not carry this Hopf
invariant.

There is a useful explicit bulk version. For \(\epsilon>0\) put
\[
E=|H|^2+|H_z|^2,\qquad
\omega_\epsilon=\frac{i}{2\pi}\partial\bar\partial
                    \log(E+\epsilon^2).
\]
The derivatives here run over both complex variables. Directly,
\[
\boxed{\quad
\omega_\epsilon\wedge\omega_\epsilon
=\frac{2\epsilon^2\,|H_zH_{zzz}-H_{zz}^{\,2}|^2}
       {\pi^2(E+\epsilon^2)^3}\,dV_{\mathbb C^2}\ge0.
\quad}
\tag{MC7}
\]
Indeed the complex Hessian of \(\log(\epsilon^2+\|w\|^2)\)
has determinant \(\epsilon^2/(\epsilon^2+\|w\|^2)^3\), and
\[
\det_{\mathbb C}DG
 =H_tH_{zz}-H_zH_{zt}
 =-H_{zz}^{\,2}+H_zH_{zzz}.
\]
Wedge-squaring contributes \(2/\pi^2\), with
\(dV_{\mathbb C^2}=d\Re t\,d\Im t\,d\Re z\,d\Im z\).

For a second normalization check, the target density has unit mass:
\[
\int_{\|w\|<R}
\frac{2\epsilon^2}{\pi^2(\|w\|^2+\epsilon^2)^3}\,dV_w
=\frac{R^4}{(R^2+\epsilon^2)^2}\longrightarrow1.
\tag{MC8}
\]
Local holomorphic change of variables therefore multiplies its
concentrating mass by the local degree \(L_m\).

Alternatively, set
\[
\alpha_\epsilon=
\frac{\operatorname{Im}(\overline H\,dH+
                 \overline{H_z}\,dH_z)}{E+\epsilon^2}.
\]
Then \(d\alpha_\epsilon=2\pi\omega_\epsilon\), so ordinary Stokes
on the entire ball, followed by smooth boundary convergence, gives
\[
\boxed{\quad
\int_B\omega_\epsilon^2
=\frac1{4\pi^2}\int_S\alpha_\epsilon\wedge d\alpha_\epsilon
\longrightarrow L_m.
\quad}
\tag{MC9}
\]
No interior energy floor or exchange of singular densities with an
integral is used. Off the isolated event, MC7 tends locally uniformly
to zero; positivity and MC9 then give
\(\omega_\epsilon^2\rightharpoonup L_m\delta_{(0,a)}\).
For a small ball about a simple zero the entire integral is
\(O(\epsilon^2)\). Finite \(\epsilon\) has a smooth background;
the exact multiplicity-selective statement is the limit.

The regularized form is the curvature of the auxiliary projective
observation \([H:H_z:\epsilon]\), with normalized Fubini–Study
convention. Its square realizes the local intersection residue. It
is not the ordinary \(c_2\) form of the trivial flat jet bundle, nor
the \(c_2\) of the arithmetic theta line bundle. The singular square
at \(\epsilon=0\) is defined here only by the displayed regularization.

## 4. Which topology changes, and which does not

The following are local weights at the selected zero; the simple
case means an event-free neighborhood for the heat-jet observation.

| Spatial multiplicity | Gauss defect divided by \(\pi\) | Relative \(c_2\) / Hopf number | Primitive-curve Milnor number |
| --- | --- | --- | --- |
| 1 | 0 | 0 | 0 |
| 2 | 1 | 1 | 2 |
| 3 | 2 | 3 | 6 |
| 4 | 3 | 6 | 12 |

[Investigation 22 Note 04][g04] proves that the embedded primitive
curve \((f,\int f)\) has link \(T(m,m+1)\), Milnor number
\(m(m-1)\), and Milnor-fiber genus \(\binom m2\); for \(m=1\)
it is smooth with an unknot link. The numerical equality with MC4
does not identify the two germs. The intrinsic topological disk
alone misses the cusp; the embedding retains it.

The arithmetic theta line bundle in [Investigation 22's construction][asd]
has degree one on each elliptic fiber, independently of physical
heat-zero multiplicity. A line bundle's second Chern class is identically zero.
Its \(c_1^2\) is a different invariant and is not automatically MC5.
The [adapted ASD connection][metric] pulls back flatly to the physical
source path and its natural external two-source product. Transverse
commutators survive before restriction, but no comparison transferring
them to MC7–MC9 has been proved.
The marked hyperkähler family is incomplete and lacks full modular
descent; no compact global Chern identity for this physical detector
has been supplied.

Hyperkähler structure trivializes the canonical bundle, giving
\(c_1(TX)=0\); it does not force \(c_2(TX)=0\).
For example, a K3 surface has second Chern number 24
([Huybrechts, §1.2.4][k3]). That global fact does not identify a
physical jet bundle with \(TX\). More directly, the double model
\(H=z^2-2t\) lives on flat hyperkähler \(\mathbb C^2\) and has
\(\det DG=-4\), hence relative charge one. Even a flat ambient
metric and a trivial jet bundle permit the localized event.

An ordinary quadrupole is not a reliable substitute. A centered
trace-free second moment annihilates every radial profile, including
the double-event inner density \((1+|q|^2)^{-2}dA_q\) from Note 24.
Every unscaled second spatial moment annihilates the point mass
itself. This only rules out that automatic moment discriminator;
it does not exclude observations using additional asymmetric data.
The coincidence statistic \(m(m-1)\), already retained by
[Note 06's diagonal subtraction][n06], is a nonlinear count,
not a spatial quadrupole.

## 5. Control response and the HMC-06 gate

All displayed local counts hold for general analytic heat solutions.
The relevant controls therefore have the same charge at a matching
multiple zero. Their missing theta premises remain separate:

- Quadratic/Hermite and atomic controls lack the unchanged complete
  arithmetic theta source; finite-profile controls also fail the full
  theta growth and threshold-simplicity data.
- Euler-factor controls change the original Euler factor and completion.
- BW10's close positive-source endpoint controls retain the stated
  completion and leading tail but fail ordinary Dirichlet arithmetic.
- Weighted-square and finite-prime controls fail full reflection and
  the canonical coefficients; finite-source examples have no all-real
  heat slice, which is not required for MC4–MC9.
- Reflected, smooth-shape and positive-primitive controls fail the
  unchanged normalized integer-square theta expansion.

No control is being assigned the canonical arithmetic theta section
merely because it admits a local jet construction.

The local detector is therefore available without finding another
collision. Quantization makes an independently proved bound below one
for the normalized localized charge sufficient for exclusion. Such
a bound for every proposed theta endpoint is presently a simplicity
reformulation, not an established estimate. An actual next gain would
be a theta-specific bound for MC9's boundary integral, or a justified
comparison from arithmetic source geometry that forces it below one,
with all boundary terms paid. General complex domains may also enclose
nonreal-time events; those are not automatically physical collisions.

**HMC-05 remains open and HMC-06 gated.** The new formulas make the
requested multiplicity-selective observation explicit; they do not
improve the available arithmetic margin. No new numerical campaign
or manuscript expansion follows.

The internal check here is analytic: the holomorphic Jacobian, target
unit-mass integral, contact-form orientation and Stokes normalization
agree, and the double control has charge one. The all-multiplicity
intersection theorem and its existing finite checks remain in
Investigation 22 Note 08. No independent review, new numerical theta
calculation or new general topological theorem is claimed.


## 6. Global scope of the underlying manifold construction

Clarification on 21 October 2026 for Edward Baker, with substantial LLM
assistance, **gpt-6-astra, actual effort max**. The recent defects are
local, but their defining function and geometric maps are global.

[Investigation 22, manuscript §2][manifold] proves that the complete
source defines a jointly entire function on complex heat spacetime.
For fixed real time, its §5 uses the global primitive and map
\[
P(t,z)=\int_0^z H(t,\zeta)\,d\zeta,\qquad
X_t(z,w)=(P(t,z),H(t,z),w).
\]
This is defined on all of \(\mathbb C^2\). On
\(\Omega_t\times\mathbb C\), where
\(\Omega_t=\{z:|H|^2+|H_z|^2>0\}\), it is a holomorphic immersion
with metric \((|H|^2+|H_z|^2)|dz|^2+|dw|^2\). It therefore supplies
a global noncompact parameter manifold on its regular locus. Its image
need not be globally embedded. Multiple zeros are precisely the points
where this immersion loses rank; the local cusp calculations describe
that degeneration of the global map.

With the displayed primitive normalization, evenness gives
\(H_z(t,0)=0\), and direct differentiation yields
\[
P_t=-H_z,\qquad \partial_tX_t=-\partial_z^2X_t.
\]
The identities hold globally for the parametrized maps, including where
rank drops. They use the fixed spectral coordinate and do not identify
the deformation with Ricci flow or an intrinsic geometric heat flow.
The induced metric is not hyperkähler for a theta slice (manuscript §5).
Adding the coordinate \(z\) makes the graph everywhere immersed, with
coefficient \(1+|H|^2+|H_z|^2\), but does not exclude a physical jet zero.

The separate arithmetic construction in manuscript §8 is defined over
the whole marked elliptic family \(\mathbb H\times\mathbb T^2\).
Its theta section and covariant fourth derivative recover the complete
source along a specified path; the full oscillatory integral then
recovers \(H(t,z)\). Its semi-flat metric is hyperkähler, but incomplete
and not invariant under the full modular group. No identification of
\(H\) with a compact K3 invariant has been established.

[Investigation 22 Note 05][jensen] also constructs a countable family of
compact real hyperelliptic surfaces from Jensen polynomials of complete
theta moments. That is a global RH reformulation; it does not require
simple zeta zeros and supplies no simplicity conclusion. It is not a
single compact surface representing the full heat family.

Finally, the map \(G=(H,H_z):\mathbb C^2\to\mathbb C^2\) used in
MC4–MC9 is itself global. The relative charge is localized by choosing
a bounded neighborhood and retaining its boundary section. A missing
global theta-specific constraint on such charges, rather than absence
of a global geometric representation, is the remaining issue.

[manifold]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[jensen]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md

[n24]: 24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[n06]: 06_SIGNED_CORRELATION_RESOLUTION_AND_MOBIUS_ENERGY_20261020.md
[g08]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md
[g04]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[asd]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/01_COVARIANT_SOURCE_AND_ASD_CONNECTION_20261015.md
[metric]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[demailly]: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/analmeth_book.pdf
[stacks]: https://stacks.math.columbia.edu/tag/0FA9
[ionel]: https://web.stanford.edu/~lindrew/math215B.pdf
[hopf]: https://arxiv.org/pdf/0912.4974
[k3]: https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf
