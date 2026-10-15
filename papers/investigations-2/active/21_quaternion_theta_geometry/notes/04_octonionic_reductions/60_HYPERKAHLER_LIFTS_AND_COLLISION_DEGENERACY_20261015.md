---
research_program: ALG
secondary_programs: [PR02, PR02-CORR]
status: exact_hyperkahler_and_kahler_models_collision_degeneracy_identified
---

# Hyperkähler lifts and collision degeneracy

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current conversation metadata. Internal collaborators inherited that configuration. This note derives concrete geometric models from the closed self-dual forms of [Note 50](50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md). It makes no literature novelty claim and proves no new theta sign domain.

The forms do support an exact hyperkähler interpretation, rather than only a quaternionic analogy. A single nonvanishing holomorphic field gives a locally flat hyperkähler metric. A complex combination of the physical first-jet pair gives such a metric whose scale on the real slice is exactly the physical energy. On the physical real slice this construction degenerates precisely at the common zeros one would need to exclude; away from that slice its single complex coefficient can have other zeros. A smooth background hyperkähler metric already exists independently of the theta field; its existence does not prevent those zeros.

## 1. Closed self-dual forms are harmonic, but need not be parallel

Fix real heat time and let \(f(z)\) be holomorphic, with \(z=x+iy\), \(w=u+iv\). The Euclidean metric and orientation are
\[
g_0=|dz|^2+|dw|^2,\qquad \mathrm{vol}_0=dx\wedge dy\wedge du\wedge dv.
\]
Write
\[
\Omega_f=f(z)\,dz\wedge dw,\qquad
\alpha_f=\frac1{\sqrt2}\Re\Omega_f.
\]
As in Note 50, \(*_0\alpha_f=\alpha_f\) and \(d\alpha_f=0\). Hence \(d_0^*\alpha_f=-*_0d*_0\alpha_f=0\), so \(\Delta_{d,0}\alpha_f=0\). These are local differential statements. They do not require an \(L^2\) interpretation on the noncompact four-space.

In the fixed Euclidean frame,
\[
|\alpha_f|_0^2=|f|^2,\qquad
|\nabla^0\alpha_f|_0^2=2|f'(z)|^2.
\tag{1}
\]
Therefore \(\alpha_f\) is parallel exactly when \(f\) is constant on a connected domain. Closedness plus self-duality does not make a nonconstant theta jet into a parallel tensor. Holonomy concerns tensors preserved by the Levi-Civita connection, a stronger condition; see [Joyce, Lectures 13–14, especially slides 5, 21 and 28–30](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/KG13%2B14handout.pdf). The ambient Euclidean metric already has trivial holonomy.

Also, all the \(\alpha_{h_j}\) lie in the real two-plane spanned by \(\Re(dz\wedge dw)\) and \(\Im(dz\wedge dw)\). On the physical real slice the jets are real, so these forms are collinear. They do not themselves provide the three independent forms needed for a hyperkähler triple.

## 2. An explicit locally flat hyperkähler metric

On a domain where \(f\ne0\), define
\[
\boxed{g_f=|f(z)|^2|dz|^2+|dw|^2.}
\tag{2}
\]
Choose a local holomorphic primitive \(F'=f\). Then \(\zeta=F(z)\) is a local coordinate and
\[
g_f=|d\zeta|^2+|dw|^2.
\tag{3}
\]
Thus this metric is locally Euclidean, in particular hyperkähler. Its hyperkähler forms can be written
\[
\omega_1=\frac i2\bigl(|f|^2dz\wedge d\bar z+dw\wedge d\bar w\bigr),
\quad \omega_2=\Re\Omega_f,\quad \omega_3=\Im\Omega_f.
\tag{4}
\]
All three are closed. Their mixed wedge products vanish and
\[
\omega_i\wedge\omega_j=2\delta_{ij}\,\mathrm{vol}_{g_f},
\qquad \mathrm{vol}_{g_f}=|f|^2\mathrm{vol}_0.
\tag{5}
\]
Equation (3) proves directly that the associated complex structures satisfy the quaternion relations and the forms are parallel. No existence theorem or nonlinear metric equation is needed for this particular construction. It realizes \(\alpha_f=\omega_2/\sqrt2\) as a parallel form after changing the metric.

This is a genuine, but flat, hyperkähler construction. It does not produce irreducible holonomy equal to \(\mathrm{Sp}(1)\). Its restricted holonomy is trivial, contained in \(\mathrm{Sp}(1)\). The distinction between “contained in” and “equal to” matters here; hyperkähler metrics are Ricci-flat, as explained in [Joyce, Lectures 13–14](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/KG13%2B14handout.pdf).

If \(f\) has a zero of order \(m\ge1\), then \(g_f\) degenerates in the \(z\) directions. Locally \(F-F(z_0)\) has order \(m+1\); after a nonsingular holomorphic coordinate change it is a nonzero constant times \(\zeta^{m+1}\). The metric completion in the \(z\)-plane has cone angle \(2\pi(m+1)\). It is not a positive definite smooth metric through the original zero. The map to \(F\)-space is ramified there, rather than a valid local coordinate change removing the event.

## 3. Encoding both physical jets in a single hyperkähler coefficient

Let \(H=H(t,z)\) and put
\[
f_t(z)=H(t,z)+iH_z(t,z).
\tag{6}
\]
For real \(x\),
\[
|f_t(x)|^2=H(t,x)^2+H_x(t,x)^2=E(t,x).
\tag{7}
\]
Consequently (2) gives a hyperkähler metric whose \(z\)-coefficient on the physical slice is exactly the first-jet energy. It is defined wherever \(f_t\ne0\). Its real-slice nondegeneracy is equivalent to \(E>0\), so asserting that it extends as a nondegenerate metric through every candidate collision would assume the desired exclusion.

At a nondegenerate collision \(H=H_z=0\), \(H_{zz}=d\ne0\), one has \(f_t'=id\ne0\). The hyperkähler metric therefore has the simple-zero, angle-\(4\pi\) degeneration described above. This makes the obstruction explicit.

One can always keep the smooth flat metric \(g_0\), which is hyperkähler everywhere, including at a collision. Then the theta-dependent forms are harmonic but generally not parallel, as in (1). This supplies a background geometry, not a nonvanishing theorem for the physical jets.

## 4. Conformal invariance separates self-duality from special holonomy

For an oriented four-dimensional metric, a conformal change \(\widetilde g=e^{2\sigma}g\) leaves the Hodge star on two-forms unchanged. Hence all the closed self-dual forms above remain closed, self-dual and Hodge-harmonic for every such conformal metric. The metric need not be hyperkähler.

For a concrete example take \(\widetilde g=e^{2x}g_0\). A direct Christoffel-symbol computation gives \(\operatorname{Ric}(\widetilde g)=-2(dy^2+du^2+dv^2)\), and hence
\[
\operatorname{Scal}(\widetilde g)
= -6e^{-2x}\ne0.
\tag{8}
\]
Thus this metric is not Ricci-flat and cannot be hyperkähler, although the same nonconstant \(\alpha_f\) are closed and self-dual for it. This is an explicit separation of pointwise Hodge type, closedness, harmonicity, parallelness, and holonomy reduction.

There is a related pitfall in normalizing the forms while retaining the fixed Euclidean metric. Where \(f\ne0\),
\[
d(\alpha_f/|f|)=-d\log|f|\wedge(\alpha_f/|f|).
\tag{9}
\]
A nonzero self-dual two-form is symplectic; wedge multiplication by it maps one-forms isomorphically onto three-forms. Therefore the normalized form in (9) is closed only if \(|f|\) is constant, which for holomorphic \(f\) forces \(f\) constant. Pointwise orthonormalization can destroy the differential equations. The explicit anisotropic metric (2) avoids this problem, but pays for it by degenerating at zeros.

## 5. Compactification and Bochner arguments require new global data

The forms in Note 50 are globally exact on \(\mathbb C^2\): if \(F'=f\), then
\[
\alpha_f=d\{\Re(F(z)\,dw)/\sqrt2\}.
\tag{10}
\]
On a compact oriented four-manifold without boundary, a globally exact self-dual form must vanish. Indeed, if \(\alpha=d\beta\) and \(*\alpha=\alpha\),
\[
\int_M |\alpha|^2\,\mathrm{vol}
=\int_M\alpha\wedge\alpha
=\int_Md(\beta\wedge\alpha)=0.
\tag{11}
\]
Consequently a nontrivial compact hyperkähler reinterpretation cannot preserve both this global exactness and self-duality without changing other data. It must introduce nontrivial periods/cohomology, boundaries, singularities, or a primitive that fails to descend. For instance, forms may descend to a quotient even when their primitives do not; the missing period information is then substantive.

The noncompact Euclidean construction supplies no automatic substitute. Any nonzero \(\alpha_f\) here is independent of \(w\), so it is not square integrable over all of \(\mathbb C^2\). The integration-by-parts boundary hypotheses of a global Bochner or vanishing argument are therefore absent. One cannot infer parallelness from the local harmonic equation by discarding those boundaries.

## 6. Consequence for a geometric continuation

The existing forms are harmonic self-dual forms on a flat hyperkähler background. Away from zeros, the physical combination \(H+iH_z\) yields another flat hyperkähler structure with physical energy as its real-slice metric coefficient. These are exact interpretations. Their existence alone gives no independent geometric prohibition on collisions: the physical metric degenerates there, whereas the fixed background remains smooth irrespective of the theta jets.

A useful special-holonomy continuation must therefore supply additional structure whose regularity is established through candidate collisions without first assuming \(E>0\). If it uses a compact manifold, its global periods and the failure of the original primitive to descend must be specified and paid. If it uses a noncompact metric or a holomorphic family, its boundary behavior and the relation of its tensor norms to the original physical energy must be proved. No assertion excluding every other hyperkähler construction is intended.
