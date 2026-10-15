---
research_program: PR02-CORR
parent_program: PR02
secondary_programs: [ALG]
status: literature_assessment_and_exact_source_bridge_no_signed_estimate
---

# Theta jet bundles and a semi-flat hyperkähler family

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current conversation metadata. This research note gives exact local constructions and a literature assessment; it does not claim a new theta sign estimate.

The most promising geometric continuation is to let the geometry carry the actual theta section and its lattice, rather than merely place arbitrary holomorphic jet data in a self-dual frame. There is already an exact, elementary bridge to the theta line bundle on a family of elliptic curves. A local semi-flat hyperkähler realization of that family is available. What is not available is a geometric inequality which survives the physical positive-heat weighting and oscillatory reconstruction at the scale of the central physical energy.

## 1. An exact arithmetic-geometric bridge

Use the explicit convention
\[
 \vartheta(z,\tau)=\sum_{n\in\mathbb Z}
        e^{\pi i n^2\tau+2\pi i n z},\qquad \Im\tau>0.
\]
For each \(\tau\), this is a section of the degree-one theta line bundle on
\(E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z)\). Its multipliers are
\[
 \vartheta(z+1,\tau)=\vartheta(z,\tau),\quad
 \vartheta(z+\tau,\tau)=e^{-\pi i\tau-2\pi iz}\vartheta(z,\tau).
\]
The theta heat equation is
\[
 4\pi i\,\partial_\tau\vartheta=\partial_z^2\vartheta.
\]
These are the standard line-bundle/heat-connection structures explicitly treated in Andersen–Blaavand, §6, especially pp. 18–19 of [arXiv:1106.1564](https://arxiv.org/pdf/1106.1564). Boer–Looijenga give a Hodge-theoretic unitary structure on abelian conformal blocks in [arXiv:0711.0895](https://arxiv.org/abs/0711.0895). Such unitarity is a statement about the bundle's Hermitian inner product, not a sign for the present oscillatory physical transform.

For the actual source, let \(y=e^{4u}\), so \(\tau=iy\), and put
\[
 P(u)=y^{1/4}\vartheta(0,iy),\qquad
 \Phi(u)=\frac{(\partial_u^2-1)P(u)}{16}.
\]
Writing \(D=y\partial_y\) gives the exact identities
\[
 \boxed{\Phi(u)=y^{1/4}
       \left(y^2\partial_y^2+\frac32y\partial_y\right)
                              \vartheta(0,iy),}
 \tag{1}
\]
\[
 \boxed{\Phi(u)=y^{1/4}
   \left[\frac{y^2}{16\pi^2}\partial_z^4
         +\frac{3y}{8\pi}\partial_z^2\right]
            \vartheta(z,iy)\bigg|_{z=0}.}
 \tag{2}
\]
Indeed \(\partial_u=4D\), and conjugating \(D\) by \(y^{1/4}\) replaces it by \(D+1/4\). The zeroth-order term cancels. Also \(\partial_y=i\partial_\tau=(4\pi)^{-1}\partial_z^2\). These calculations prove (1)–(2) directly; no new geometric theorem is asserted.

This exhibits the complete source as a prescribed theta **jet** along the zero section of an actual elliptic family. Ordinary \(z\)-derivatives do not retain the same automorphy multipliers: differentiating the second multiplier creates lower-jet terms. Therefore a global version must use the theta jet bundle and its transition laws, or an explicitly specified connection. Simply calling the separate derivatives theta sections would be incorrect.

The physical heat flow is different from the Jacobi heat equation. Under \(y=e^{4u}\), its multiplier and Fourier phase are
\[
 e^{tu^2}=\exp\{t(\log y)^2/16\},\qquad
 e^{ixu}=y^{ix/4}.
\]
For example the physical half-line transform is exactly
\[
 H(t,x)=\frac14\int_1^\infty
 e^{t(\log y)^2/16}y^{1/4}
 \left(y^2\partial_y^2+\frac32y\partial_y\right)\vartheta(0,iy)
 \cos\!\left(\frac x4\log y\right)\frac{dy}{y}.
 \tag{3}
\]
The modular inversion \(y\mapsto1/y\) preserves the squared-log heat weight; the established reflection symmetry must be retained. Nevertheless (3) is a weighted Mellin/Fourier reconstruction along a real path in moduli. The theta heat connection does not by itself intertwine this with its own heat parameter or give a positive contraction estimate for (3).

## 2. A local hyperkähler family is concrete, but global completion is additional work

Over the upper half-plane write \(\tau=p+iq\), \(q>0\), and use fiber coordinates \(r,s\in\mathbb R/\mathbb Z\), with \(z=r+\tau s\). The standard local semi-flat model is
\[
 g=q(dp^2+dq^2)+q^{-1}(dr+p\,ds)^2+q\,ds^2.
 \tag{4}
\]
Define
\[
 \omega_I=q\,dp\wedge dq+dr\wedge ds,\qquad
 \omega_J+i\omega_K=d\tau\wedge(dr+\tau ds)=d\tau\wedge dz.
 \tag{5}
\]
All three forms are closed. In the orthonormal coframe
\[
 e^1=\sqrt q\,dp,\quad e^2=\sqrt q\,dq,\quad
 e^3=q^{-1/2}(dr+p\,ds),\quad e^4=\sqrt q\,ds,
\]
they have the standard hyperkähler algebra
\[
 \omega_I=e^{12}+e^{34},\quad
 \omega_J=e^{13}-e^{24},\quad
 \omega_K=e^{14}+e^{23},\qquad
 \omega_a\wedge\omega_b=2\delta_{ab}\,\mathrm{vol}_g.
\]
The closed compatible triple gives a hyperkähler metric. In the holomorphic coordinates $(\tau,z)$, write $\eta=dz-s\,d\tau$. The metric is $q|d\tau|^2+q^{-1}|\eta|^2$, whose Hermitian determinant is one. Its Kähler form is $\omega_I$, so its Ricci form vanishes and $d\tau\wedge dz$ is parallel.

This metric is genuinely nonflat. The surfaces with $r,s$ fixed are totally geodesic: the coordinate metric has no base/fiber cross terms and its base block is independent of $r,s$. Their metric is $q(dp^2+dq^2)$, with Gaussian curvature
\[
K_{\mathrm{horizontal}}=-\frac{1}{2q}(\partial_p^2+\partial_q^2)\log q=\frac{1}{2q^3}>0.
\]
The [exact checker](../../numerics/check_theta_manifold_geometry.py) independently computes the inverse metric, Levi-Civita curvature and zero Ricci tensor, as well as the closed triple and source differential operator. Its [execution receipt](../../numerics/THETA_MANIFOLD_GEOMETRY_CHECKS_20261015.json) records 55 exact assertions. This verifies local identities, not completeness or modular descent. This is the local semi-flat construction, not a new existence theorem. Its fibers are the elliptic curves used in (1)–(3), and the theta line bundle lives on those fibers. Thus a curved four-dimensional setting need not be chosen arbitrarily.

Gross–Wilson's [*Large complex structure limits of K3 surfaces*](https://arxiv.org/abs/math/0008018), Example 2.2 and Remark 2.7, gives the standard semi-flat construction, and supplies the global elliptic-K3 context: their construction glues a semi-flat metric on the smooth fibration to local models at singular fibers. That theorem does not identify the present physical transform or its sign with a K3 invariant.

The simple formulas (4)–(5) are given on the upper-half-plane cover. They do **not** assert descent under the whole modular group or a complete metric at every cusp. For example \(d\tau\wedge dz\) transforms by \((c\tau+d)^{-3}\) under the usual modular change \((\tau,z)\mapsto((a\tau+b)/(c\tau+d),z/(c\tau+d))\); the base factor $q|d\tau|^2$ is multiplied by $|c\tau+d|^{-6}$. A modular descent needs additional data. A global compactification, any singular fibers, metric corrections, boundary terms, and the theta line-bundle connection all have to be specified and checked. These are mathematical obligations, not harmless notation choices.

## 3. What special holonomy cannot supply by itself

**Conformal replacement.** On an oriented four-manifold, changing \(g\) to \(e^{2f}g\) leaves the Hodge star on two-forms unchanged. A fixed top-form pairing \(\alpha\wedge\beta\) is unchanged, and its coefficient relative to the volume form is multiplied by the positive factor \(e^{-4f}\). Therefore it cannot reverse the sign of the physical polarized pairing. Atiyah–Hitchin–Singer's original paper discusses conformal invariance and the SD/ASD decomposition in §1: [primary article](https://www.math.miami.edu/~cscaduto/teaching/782-fall-2023/notes/AHS.pdf). The last sign observation is a direct deduction here.

**Compact hyperkähler rigidity.** Choose the orientation making the three parallel Kähler forms self-dual. Then scalar curvature and \(W^+\) vanish. For a self-dual harmonic two-form \(\alpha\), the Weitzenböck identity reads
\[
 0=\Delta\alpha=\nabla^*\nabla\alpha+
       (\mathrm{Scal}/3-2W^+)\alpha=\nabla^*\nabla\alpha.
\]
On a compact manifold without boundary, integration gives
\(\int|\nabla\alpha|^2=0\), so \(\alpha\) is parallel. Their pairings relative to this metric must then be constant; this statement does not force arbitrary coordinate coefficients to be constant. There is a stronger obstruction to extending the whole present family while preserving its local forms. At a physical real point with $H\ne0$, $\alpha_H$ and $\alpha_{H_z}$ are proportional, with real ratio $c=H_z/H$. If both were parallel, $\alpha_{H_z}-c\alpha_H$ would vanish throughout the connected patch, forcing $H_z=cH$. A nonzero entire even decaying theta field cannot satisfy that identity. Thus retaining the whole family requires additional bundle-valued objects, noncompactness, boundaries, or singularities; each changes the analytic problem. Reversing orientation exchanges the labels SD and ASD and does not remove this specific obstruction on the parallel-triple side. This observation does not exclude the abundant harmonic forms in the opposite Hodge sector.

**Twistor and Yang–Mills methods.** The original Atiyah–Hitchin–Singer paper gives the geometric/holomorphic correspondence for appropriate self-dual connections; Hitchin's [1987 self-duality paper](https://doi.org/10.1112/plms/s3-55.1.59) produces rich hyperkähler moduli geometry. To use either here one must first specify the bundle, connection, reality structure, relevant equations, and an exact map back to both physical Laguerre quantities. A flat line-bundle connection has zero curvature and cannot simply be declared to have the nonzero theta form as curvature. An abelian twistor encoding of the already-proved closed forms adds a representation, but the existing collision controls still belong to that generic class. A nonabelian construction must also restore gauge-covariant transport and every commutator term; the rejected 2014 bilocal scalar-kernel identity cannot be reinstated by appealing to twistor theory.

**Exceptional holonomy and calibrations.** Harvey–Lawson's original [*Calibrated geometries*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6313-11511_2006_Article_BF02392726.pdf), especially II.4 and IV, establishes the mass-minimizing consequences of calibrated tangent planes and develops the exceptional examples. Joyce's [survey](https://arxiv.org/abs/math/0406011) describes associative and coassociative geometry for \(G_2\), and Cayley geometry for \(\mathrm{Spin}(7)\). These give useful nonlinear PDE and deformation tools. However, an octonionic packaging of the jet vector does not prove that a graph is associative or Cayley: those are additional first-order nonlinear equations. [Note 61](../02_signed_cusp_control/61_JET_SURFACES_REAL_GAUSS_MAP_AND_ORIENTED_TURNING_20261015.md) now supplies actual coassociative and Cayley inclusions for the holomorphic jet surface, by checking the calibration pullbacks. These inclusions remain regular only off its branch set and also hold for the collision controls. Linear Fueter/Dirac conditions occur as linearizations in appropriate graph models, not automatic proofs of the full calibration condition. Even a proved calibrated-volume inequality would need an exact identification with the complete signed stationary observation and a loss bounded by \(E=h_0^2+h_1^2\). Volume or total Yang–Mills energy is a different quantity.

## 4. A discriminating next task

A bounded first task would be to construct (1)–(2) intrinsically as a theta jet-bundle expression over a chosen level cover of the elliptic family, record its Hermitian connection, and derive its exact covariant derivative and curvature identities. Then insert that expression into the **complete** two-source correlation or polarized boundary current before taking norms or splitting sectors.

A successful continuation must produce a signed identity with all of the following visible: the actual integer theta lattice, the full factor \(e^{t(u^2+v^2)}\), the physical spectral phase, the exact central-energy term, and all connection/commutator/cusp boundary remainders. It must imply a prescribed locally bounded coefficient on both full stationary branches. The controls from Notes 53 and 56 are appropriate tests: a mechanism that uses only generic positivity, source shape, fixed primitive positivity, or local self-dual algebra will also accept those controls and cannot provide the desired conclusion.

A reasonable research order is: theta-bundle/elliptic-family connection first; a concrete semi-flat or globally completed hyperkähler model if it supplies a useful identity; nonabelian/twistor or \(G_2\)/\(\mathrm{Spin}(7)\) upgrades only when their extra PDE can be verified for this source and give a new signed estimate. This is a feasibility assessment. No such energy-relative estimate is proved here, and no theta sign domain is enlarged.
