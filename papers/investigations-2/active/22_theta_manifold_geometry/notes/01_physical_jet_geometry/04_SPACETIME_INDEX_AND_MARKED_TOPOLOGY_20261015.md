# Spacetime winding and marked topology of theta collisions

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. Internal mathematical review is not external refereeing or formal verification.

The physical first jet admits a useful topological reduction: on any compact spacetime region with a nonzero boundary jet, its winding counts every interior collision with the same sign. The full spacetime map detects both parity branches using only \((H,H_x)\). This is an application of classical parabolic zero-number and mapping-degree theory, not a new general topological principle. A second reduction identifies the local embedded singularity of the manuscript's primitive curve. Neither result makes the underlying unmarked manifold topology an arithmetic discriminator.

The source conventions and the RH bridge are those of the [Investigation 22 manuscript](../../manuscript/theta_manifold_geometry.tex), §2, and the positive-time collision section of [Investigation 21](../../../21_quaternion_theta_geometry/manuscript/quaternion_theta_geometry.tex). The [continuation note](../00_research_coordination/11_SCALAR_MANUSCRIPT_AND_POSITIVE_TAIL_CONTINUATION_20261015.md) correctly leaves the theta-specific scalar trace estimate open.

## One first jet on spacetime

Let a real analytic field satisfy \(H_t=-H_{xx}\), with no identically zero spatial slice. Write

\[
J=(H,H_x),\qquad E=H^2+H_x^2,
\]

and orient the source plane by \(dt\wedge dx\) and the target by its displayed component order. On \(E>0\), the phase one-form is

\[
\beta=\frac{H\,dH_x-H_x\,dH}{E}
=\frac{(H_xH_{xx}-HH_{xxx})\,dt
 +(HH_{xx}-H_x^2)\,dx}{E}.
\tag{1}
\]

Locally \(\beta=d\arg(H+iH_x)\). Its spatial coefficient is the manuscript's \(-\mathcal L_0/E\); its temporal coefficient is essential. For the cubic control

\[
H=x^3-6(t-T)x,\qquad
\mathcal L_0=3x^4+36(t-T)^2\ge0,
\]

the spatial Laguerre sign alone permits a triple collision. The complete spacetime first jet has local index \(-1\) there. The second stationary branch remains necessary for the manuscript's spatial criteria, but is unnecessary for this spacetime criterion.

## Local index at every finite multiplicity

**Proposition.** If \(H(T,\cdot)\) has exact order \(m\ge2\) at \(a\), then \((T,a)\) is an isolated zero of \(J\) in the real spacetime plane and

\[
\operatorname{ind}_{(T,a)}J=-\left\lfloor\frac m2\right\rfloor.
\tag{2}
\]

**Proof.** Put \(c=\partial_x^mH(T,a)/m!\ne0\). The heat Taylor series gives, uniformly on compact sets of \((\tau,y)\),

\[
\begin{aligned}
\rho^{-m}H(T+\rho^2\tau,a+\rho y)&=c\,p_m(\tau,y)+O(\rho),\\
\rho^{1-m}H_x(T+\rho^2\tau,a+\rho y)&=c\,\partial_yp_m(\tau,y)+O(\rho),\\
p_m(\tau,y)&=\sum_{k=0}^{\lfloor m/2\rfloor}
 \frac{m!(-\tau)^k y^{m-2k}}{k!(m-2k)!}.
\end{aligned}
\tag{3}
\]

The polynomial solves

\[
2\tau p_m''-y p_m'+m p_m=0.
\tag{4}
\]

At \(\tau\ne0\), a common zero of \(p_m,p_m'\) would contradict uniqueness for this second-order ordinary differential equation. At \(\tau=0\) the only common zero is \(y=0\). Thus the polynomial pair is bounded away from zero on the compact weighted sphere \(\max(\sqrt{|\tau|},|y|)=1\). Taking \(\rho=\max(\sqrt{|t-T|},|x-a|)\) in (3) proves isolation of the original zero. The same estimates give a nonzero straight-line boundary homotopy to the polynomial pair. Positive rescaling of each target coordinate preserves degree; multiplication of both coordinates by \(c\) has positive determinant even when \(c<0\).

At \(\tau=1\), \(p_m\) is a rescaled Hermite polynomial and has \(m\) simple real zeros. At \(\tau=-1\), it is a polynomial in \(y^2\) with strictly positive coefficients when \(m\) is even, and \(y\) times such a polynomial when \(m\) is odd. There are respectively zero and one real roots, with the latter simple. Choose \(R\) large enough that \(p_m(\tau,\pm R)\ne0\) for \(|\tau|\le1\), which is possible from its leading term uniformly in \(\tau\).

For a rectangle \([t_-,t_+]\times[a,b]\) on whose spatial walls \(H\ne0\), with simple zeros on its time faces, let \(N_-,N_+\) be their real root counts. Along a time face the phase increment equals its endpoint arctangent difference minus \(\pi\) times the root count: \(\arctan(H_x/H)\) jumps upward by \(\pi\) at every simple zero, whereas the true phase is continuous. The endpoint terms cancel with the two spatial walls in the oriented boundary integral. Consequently

\[
\operatorname{wind}_{\partial D}(H+iH_x)
=\frac{N_- -N_+}{2}.
\tag{5}
\]

Apply this to the polynomial rectangle, with \(N_-=m\bmod2\) and \(N_+=m\). Homotopy gives (2). This proves the formula for arbitrary analytic higher-order perturbations, not only symmetric polynomial models. ∎

For a double event the sign is also immediate:

\[
\det D_{(t,x)}(H,H_x)
=-H_{xx}^2+H_xH_{xxx}=-H_{xx}^2<0.
\]

The finite exact controls in [the checker](../../numerics/check_spacetime_topology.py) test the model identities and boundary count formula; the analytic proof above supplies isolation and the all-multiplicity statement.

## Boundary winding is a complete compact collision test

Let \(D\) be a bounded Jordan domain whose closure lies in an analytic domain, and assume \(E>0\) on its boundary. Isolation and compactness make the interior collision set finite. Additivity of Brouwer degree gives

\[
\frac1{2\pi}\oint_{\partial D}\beta
=-\sum_{(T,a)\in D:\,H=H_x=0}
 \left\lfloor\frac{m(T,a)}2\right\rfloor.
\tag{6}
\]

In particular, boundary winding zero is equivalent to absence of interior collisions. Merely knowing degree zero would not exclude zeros of a general planar map; the heat equation's sign law is the indispensable extra input. Equation (5) needs its nonvanishing spatial-wall hypothesis. Equation (6) only needs the full boundary jet to be nonzero and remains valid when \(H\) itself vanishes on that boundary.

The normalized boundary map \(J/|J|:\partial D\to S^1\) extends continuously to an \(S^1\)-valued map on \(\overline D\) exactly when its winding vanishes. Equivalently, the prescribed boundary section has zero relative Euler obstruction in \(H^2(\overline D,\partial D;\mathbb Z)\). The underlying oriented plane bundle is trivial and has no nonzero absolute Euler class; the boundary section is essential. The extension need not initially be the actual normalized jet, but (6) forces the actual jet to be nonzero as well.

For theta, Investigation 21 proves that RH is equivalent to no first-jet zero at any positive time. Positivity \(H(t,0)>0\) and evenness allow use of \(x>0\) only. For example, the fixed rectangles

\[
D_n=[1/(n+2),1]\times[0,n],\qquad n\ge1,
\tag{7}
\]

exhaust all possible positive-time positive-height events: there are none above \(t=1/2\) by the threshold theorem and local splitting. Therefore RH is equivalent to the statement that for every \(n\), the boundary jet on \(D_n\) is nonzero and its normalized circle map has degree zero, or equivalently extends over the rectangle. The terminal time \(1/2\) is deliberately in the interior of sufficiently large rectangles. No simplicity assertion about \(H(0,\cdot)\) is added.

Uniform nonreal-zero confinement also gives a stabilized formulation. Call \(a>0\) regular if its time slice has no multiple real zero. For regular \(0<a<1/2\), choose \(b>1/2\), and then \(R\) beyond all positive-height events in \([a,b]\). Such a radius exists: a hypothetical event at \(T\ge a\) has nonreal predecessors at times at least \(a/2\); the bound \(|\Re z|<e^{C/t}\) confines its limiting real height. The quantity

\[
\nu(a)=-\operatorname{wind}_{\partial([a,b]\times[0,R])}(H+iH_x)
\tag{8}
\]

is independent of larger boundary-regular radii, is nonnegative, and increases by \(\lfloor m/2\rfloor\) when \(a\) moves downward across an event, with contributions added for simultaneous events. It equals the number, with multiplicity, of nonreal zeros of \(H(a,z)\) in \(\Re z>0,\Im z>0\). Indeed these zeros cannot cross the imaginary axis because \(H(t,iy)>0\), escape to infinity on a compact positive-time interval, or cross the real axis at a simple real zero. Here both the inherited strip bound \(|\Im z|\le1\) and real-height confinement are used. They also make the total number finite; collisions between nonreal zeros preserve this multiplicity count. Local splitting removes exactly \(\lfloor m/2\rfloor\) at each positive-real event; none remain at time \(b\). This interpretation connects (8) to the ordinary argument principle and further limits any novelty claim.

## A boundary certificate can avoid an interior energy floor

If an approximation \(\widetilde J\) on \(\partial D\) satisfies

\[
\|J-\widetilde J\|<\|\widetilde J\|\quad\hbox{everywhere on }\partial D,
\tag{9}
\]

then the straight-line homotopy is nonzero on that boundary, and the two maps have the same winding. A validated polygonal enclosure can certify this without integrating the denominator in (1). If its winding is zero, (6) excludes all interior collisions, even when no useful interior lower bound for \(E\) has been computed. Uniform control along every boundary segment is necessary; sampling alone is insufficient.

The quantized analytic target is especially simple:

\[
\oint_{\partial D}\beta>-2\pi.
\tag{10}
\]

Given a nonzero boundary jet, its left side is already a nonpositive integer multiple of \(2\pi\), so this strict bound forces zero. Proving (10) throughout an exhaustion is still an RH-strength task. A finite pilot should use a box where neither jet component has one fixed sign, compare costs with interior stationary tests, and record complete source tails and boundary interpolation errors.

The full source supplies exact bilocal numerators. With \(w_t(u)=e^{tu^2}\Phi(u)\), write \(u,v\ge0\). Then

\[
\begin{aligned}
H_xH_{xx}-HH_{xxx}&=\iint w_t(u)w_t(v)K_t(u,v;x)\,du\,dv,\\
HH_{xx}-H_x^2&=\iint w_t(u)w_t(v)K_x(u,v;x)\,du\,dv,\\
K_t&=-\tfrac14\big[(u-v)^2(u+v)\sin(x(u+v))
 +(u-v)(u+v)^2\sin(x(u-v))\big],\\
K_x&=-\tfrac14\big[(u+v)^2\cos(x(u-v))
 +(u-v)^2\cos(x(u+v))\big].
\end{aligned}
\tag{11}
\]

These follow by symmetrizing the products of the cosine-transform derivatives and using addition identities. They retain the coupled phases but establish no favorable theta bound. A useful source argument must preserve cancellation or certify a boundary homotopy; positivity of the source does not suffice.

## Embedded knots and the information lost by unmarked topology

At a fixed-time order-\(m\) zero, put \(f(z)=(z-a)^m g(z)\), \(g(a)\ne0\), and \(P'=f\). The plane curve germ parametrized by \((f,P-P(a))\) has leading orders \((m,m+1)\). Choosing a local parameter with \(f=s^m\) gives \(P-P(a)=c s^{m+1}+\cdots\), \(c\ne0\). For \(m\ge2\), the two initial orders are coprime, so the germ has one Puiseux pair and embedded link the torus knot \(T(m,m+1)\). Higher terms do not add another characteristic pair. Its Milnor number is \(m(m-1)\), and its Milnor fiber has genus \(m(m-1)/2\). For \(m=1\) the germ is smooth and its link is the unknot. These are standard plane-curve singularity facts applied to this canonical primitive curve, not a claim of analytic equivalence to the monomial cusp.

| Spatial multiplicity | Spacetime index | Transverse embedded link | Milnor fiber genus |
| --- | --- | --- | --- |
| 1 | No collision | Unknot | 0 |
| 2 | −1 | Trefoil \(T(2,3)\) | 1 |
| 3 | −1 | \(T(3,4)\) | 3 |
| 4 | −2 | \(T(4,5)\) | 6 |

Thus another exact reformulation is that the **local source-parametrized branches** of the primitive curve at real spectral points have only unknotted links at every positive time. This concerns the embedded transverse germ. Global self-intersections between distinct source parameters would be additional phenomena and must not be counted as physical collisions. The added flat \(w\)-factor in the manuscript does not change the transverse germ.

The cusp itself is homeomorphic to a disk: its local normalization is one-to-one. Its product with a complex line remains a topological four-manifold. Similarly, the metric cone of angle \(2\pi m\) is topologically a disk. Bare intrinsic topology therefore misses the event. It is the embedding, the degenerate metric, or the marked section that carries the obstruction.

Even the holomorphic projective Gauss map removes the common factor:

\[
[f:f']=[(z-a)g:mg+(z-a)g'],
\tag{12}
\]

so it extends across the zero with value \([0:1]\), and the affine ratio \(f/f'\) has derivative \(1/m\) there. Extendability into \(\mathbb{CP}^1\) cannot detect the collision. The spacetime map into the real circle retains a nontrivial \(\pi_1\). Allowing its image to move freely into \(S^2\), unit quaternions \(S^3\), or unit octonions \(S^7\) makes every loop null-homotopic. Any useful enlarged carrier must preserve the marked physical plane or corresponding relative data.

The theta line bundle's degree-one class, the marked elliptic family, and the auxiliary ASD/hyperkähler geometries are useful structures but do not vary with this collision index. Investigation 21's positive-source collision controls and Investigation 22's metric freedom prevent inferring the required phase behavior from those structures alone.

## Literature and publication scope

Angenent explicitly relates the parabolic zero-number change to the mapping degree of \((u_x,u)\), proves a same-sign Jacobian rule, and discusses perturbing degenerate zeros in **§3** of [Inflection Points, Extatic Points and Curve Shortening](https://people.math.wisc.edu/~angenent/preprints/extatic.pdf), pp. 7–8. Reversing heat time and fixing the component/orientation conventions gives the mechanism used here. His [The zero set of a solution of a parabolic equation](https://math.jhu.edu/~js/Math745/angenent.par1.pdf), J. reine angew. Math. 390 (1988), 79–96, is the broader zero-set reference. The local proof above specializes the analytic case and records the exact multiplicity weight.

The global theta input is documented in [Polymath, Effective approximation of heat flow evolution of the Riemann xi function](https://arxiv.org/abs/1904.12438), especially its nonreal-zero confinement theorem, and in Investigation 21's explicit collision reduction. Standard algebraic-link references include [Oblomkov and Shende, The Hilbert scheme of a plane curve singularity and the HOMFLY polynomial of its link](https://arxiv.org/abs/1003.1568); the cusp-link interpretation itself is classical.

A useful publication would need a contribution beyond relabeling existing criteria: for example, a boundary certificate with a demonstrated computational advantage, a new arithmetic homotopy estimate, or a rigorous comparison theorem relating the signed scalar trace to the relative topological obstruction. The separate [compact real surface criterion](05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md) answers the manifold question more literally, while carrying its own classical-input and novelty limitations.
