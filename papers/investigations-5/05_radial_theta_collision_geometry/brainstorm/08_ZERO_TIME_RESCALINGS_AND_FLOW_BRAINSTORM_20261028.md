# Rescalings of the theta generator at zero time

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.
Chat0014, Add Laplacian motivation to book.

**Status: brainstorm with exact identities derived below; notation and
flow choices remain proposals.** Edward Baker asks for cleaner generating
functions, kernels and three-dimensional formulas, with the present
analysis concentrated at \(t=0\). He also proposes reconsidering the
auxiliary flow, potentially replacing or combining it with Newman flow.
The manuscript remains unchanged. Proposed edits are collected in the
[working change document](../book/changes/01_GENERATING_FUNCTIONS_AND_KERNEL_CHANGE_WORKING_NOTE_20261028.md).
The [continuation](09_GENERATING_THETA_AND_FLOW_CONTINUATION_20261028.md)
extracts the formulas and decisions for the next chat.

The strongest simplification at zero time is the smooth positive potential
\(1+r^{-1}-\Theta(r)\). After multiplication by \(\sqrt r\) and the
change \(u=\tfrac12\log r\), its observation becomes an ordinary Fourier
integral times \(1+z^2\). A three-dimensional cylinder retains the angular
geometry with a constant-coefficient longitudinal operator. The cost is
an ordinary integral defined in a spectral strip, rather than everywhere
in the complex plane. The former subtracted profile retains an entire
integral but has a cusp. Both choices are recorded rather than selecting
one prematurely.

## 1 Keep the theta generator and operator visible

Throughout,
\[
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
\Theta(r)=1+2A(r),\qquad
\Delta_3=\partial_r^2+\frac2r\partial_r.
\]
The inherited source identity is
\[
\Phi(u)=\frac14r^{5/2}\Delta_3\Theta(r),\qquad r=e^{2u}.
\]
Thus, with ordinary Euclidean volume and the classical derivative at
\(r>0\),
\[
H(0,z)=\frac1{64\pi}\int_{\mathbb R^3}
 (\Delta_3\Theta)(|X|)|X|^{-1/2+iz/2}\,dX.
\tag{1}
\]
The integrand extends flatly at zero. This integral is entire in \(z\).
The scalar function \(H\) retains its original normalization. Writing
\(16H\) below removes repeated constants without shifting any zeros;
\(16H-1\) would be a different zero target.

## 2 A smooth potential removes the sphere term at zero time

For this comparison define the explicitly subtracted generator
\[
\boxed{V(r)=1+r^{-1}-\Theta(r)=r^{-1}-2A(r).}
\tag{2}
\]
Modularity gives
\[
V(r)=r^{-1}V(1/r),\qquad
V(r)=1-2r^{-1}A(1/r)\quad(r\downarrow0).
\]
Consequently \(V(|X|)\) extends smoothly to \(V(0)=1\), with all
positive-order derivatives zero at the origin, and
\(V(r)=r^{-1}+O(e^{-\pi r^2})\) at infinity. There is no interface at
\(r=1\). Distributionally on the whole space,
\[
-\Delta_XV(|X|)=(\Delta_3\Theta)(|X|).
\tag{3}
\]
The central point sources of \(1/r\) and \(\Theta\) cancel.

This potential is strictly positive. One direct verification, keeping the
original derivative visible, is
\[
V(r)=\frac1r\int_0^r s^2\Delta_3\Theta(s)\,ds
       +\int_r^\infty s\Delta_3\Theta(s)\,ds>0.
\tag{4}
\]
The derivative \(\Delta_3\Theta\) is positive, and its radial mass
\(\int_0^\infty s^2\Delta_3\Theta(s)\,ds=1\) is the inherited theta
flux normalization. Differentiating (4) verifies (3), and the endpoint
conditions identify (2). Thus \(V\) is the decaying Newtonian potential
of the canonical positive radial source, with this normalization.

Since
\[
-\Delta_3r^{-1/2+iz/2}
=\frac{1+z^2}{4}r^{-5/2+iz/2},
\]
Green's identity yields the cleaner three-dimensional formula
\[
\boxed{
H(0,z)=\frac{1+z^2}{256\pi}
 \int_{\mathbb R^3}
 \big[1+|X|^{-1}-\Theta(|X|)\big]
 |X|^{-5/2+iz/2}\,dX,
\qquad |\operatorname{Im}z|<1.
}
\tag{5}
\]
There is no additive constant or unit-sphere term in (5).

The strip is essential to this ordinary integral. If
\(b=\operatorname{Im}z\), radial absolute integrability is controlled
by \(r^{-1/2-b/2}\) at zero and \(r^{-3/2-b/2}\) at infinity.
Both ends converge precisely for \(-1<b<1\). The corresponding Green
boundary terms vanish in that strip. At \(z=\pm i\), the integral
in (5) diverges; its vanishing prefactor must not be used to infer a zero
of \(H\). The product continues analytically to the original entire
function, whose value there is \(H(0,\pm i)=1/16\).

Although \(V\) is a smooth spatial potential, the density
\(V(r)r^{-5/2}\) relative to Euclidean volume is singular at zero and
has a power tail. This replaces the earlier flat Schwartz density with a
different admissible class. Its total integral is finite; smoothness of
\(V\) does not make that weighted density smooth.

## 3 The square-root rescaling is selected by two independent simplifications

Set \(x=\log r\) temporarily. For an angularly dependent profile,
\[
\Delta_X\big[r^{-a}F(x,\omega)\big]
=r^{-a-2}\left[
 \partial_x^2+(1-2a)\partial_x+\Delta_{\mathbb S^2}+a(a-1)
\right]F.
\tag{6}
\]
The choice \(a=1/2\) is the unique power that removes the longitudinal
first derivative. It is also the power that turns the weight-one Kelvin
relation into ordinary reflection: if \(f(r)=r^{-1}f(1/r)\), then
\(e^{x/2}f(e^x)\) is even in \(x\). These are structural reasons to
use \(\sqrt r\), not merely a way to shorten one formula.

Return to the original logarithmic source coordinate
\(u=\tfrac12\log r\), and define
\[
\boxed{
G(u)=\frac12e^uV(e^{2u})
=\cosh u-\frac12e^u\Theta(e^{2u}).
}
\tag{7}
\]
The theta origin of \(G\) should be displayed whenever it is introduced.
It is smooth, positive and even, and
\[
G(u)=\frac12e^{-|u|}-e^{|u|}A(e^{2|u|}),\qquad
G(u)\sim\frac12e^{-|u|}.
\tag{8}
\]
The absolute-value expression is useful for tails; (7) makes smoothness
at zero immediate. The two cusp contributions in (8) cancel.

Equation (5) now becomes
\[
\boxed{
16H(0,z)=(1+z^2)\int_{\mathbb R}G(u)e^{izu}\,du,
\qquad |\operatorname{Im}z|<1.
}
\tag{9}
\]
Its differential origin is especially short:
\[
\boxed{(1-\partial_u^2)G=8\Phi.}
\tag{10}
\]
Indeed \((\partial_u^2-1)[e^u\Theta(e^{2u})]=16\Phi\), while
\((\partial_u^2-1)\cosh u=0\). Alternatively,
\[
G(u)=4\int_{\mathbb R}e^{-|u-v|}\Phi(v)\,dv
\tag{11}
\]
is the unique solution of (10) decaying at both ends, and proves its
positivity directly. Formula (11) explains the exponential tail gained
by inverting the second-order operator.

For real \(z\), \(1+z^2\) never vanishes. The zeros and their
multiplicities in (9) are exactly those of the Fourier integral. At a
real zero \(a\), its derivative also vanishes exactly when
\(\int iuG(u)e^{iau}\,du=0\). This is a transparent reformulation of
cancellation, not an exclusion argument.

## 4 Keep a genuinely three-dimensional integral on a cylinder

The change \(X=e^{2u}\omega\) identifies punctured Euclidean space
with \(\mathcal C=\mathbb R\times\mathbb S^2\). Let
\(d\sigma=d\omega/(4\pi)\) and use the normalized product measure
\[
d\mu=du\,d\sigma=\frac{dX}{8\pi|X|^3}.
\tag{12}
\]
Then (9) has the three-dimensional form
\[
\boxed{
16H(0,z)=(1+z^2)
\int_{\mathcal C}
 \left[\cosh u-\frac12e^u\Theta(e^{2u})\right]
 e^{izu}\,d\mu.
}
\tag{13}
\]
There are still two angular variables; their initial dependence is
constant. The logarithmic measure has absorbed the Euclidean powers.

For a geometric operator, equip the cylinder with
\[
g_{\mathcal C}=du^2+\frac14g_{\mathbb S^2},\qquad
\Delta_{\mathcal C}=\partial_u^2+4\Delta_{\mathbb S^2},\qquad
\mathcal L=1-\Delta_{\mathcal C}.
\tag{14}
\]
Its ordinary volume is \(dV_{\mathcal C}=\pi d\mu\).
The Euclidean metric is \(4e^{4u}g_{\mathcal C}\), so using the product
metric changes the metric, not just the notation for the original
Euclidean metric. The complete operator identity is
\[
\Delta_X\big[r^{-1/2}F(u,\omega)\big]
=-\frac14r^{-5/2}\mathcal L F.
\tag{15}
\]
In this form the kernel calculation is just
\[
\boxed{\mathcal L e^{izu}=(1+z^2)e^{izu}.}
\tag{16}
\]
This is the most economical differential formulation found in the
brainstorm. It also retains a clear place for nonradial fields.

If \(x=\log r\) is preferred instead, the product cylinder has unit
sphere radius and operator \(-\partial_x^2-\Delta_{\mathbb S^2}+1/4\).
It replaces \(z\) by the frequency \(z/2\). The \(u\)-convention keeps
the original spectral parameter and the factor \(1+z^2\), at the cost
of a sphere of radius \(1/2\). Both conventions are exact.

## 5 The Mellin parameter gives a second clean notation

Set
\[
\lambda=\frac{1+iz}{2},\qquad 1+z^2=4\lambda(1-\lambda).
\]
Using the standard Mellin convention
\(\mathcal M V(\lambda)=\int_0^\infty V(r)r^{\lambda-1}\,dr\),
\[
\boxed{
16H(0,z)=\lambda(1-\lambda)\mathcal M V(\lambda),
\qquad 0<\operatorname{Re}\lambda<1.
}
\tag{17}
\]
Equivalently, with Euclidean volume,
\[
16H(0,z)=\frac{\lambda(1-\lambda)}{4\pi}
 \int_{\mathbb R^3}
 \big[1+|X|^{-1}-\Theta(|X|)\big]|X|^{\lambda-3}\,dX.
\tag{18}
\]
Kelvin symmetry gives \(\mathcal M V(\lambda)=\mathcal M V(1-\lambda)\).
The real \(z\)-axis becomes \(\operatorname{Re}\lambda=1/2\).
This notation makes the reflection and spectral prefactor simple, but
\(u,z\) remain preferable if the emphasis is spatial Fourier geometry.
The symbol \(\lambda\) avoids overloading the intended auxiliary
parameter \(s\).

The Mellin normalization and strip criterion are the classical ones in
[NIST DLMF 1.14.32 and its following paragraph](https://dlmf.nist.gov/1.14.iv).
No Mellin inversion theorem is needed for (17).

## 6 Compare the alternatives before choosing a definition

| Choice | What becomes simpler | What must remain visible |
| --- | --- | --- |
| Original \(\Delta_3\Theta\) with Euclidean volume | Direct source identity and entire spectral integral | Laplacian on the generator and the radial weights |
| \(V=1+r^{-1}-\Theta\) | Smooth positive potential; pure power kernel; no sphere term | Ordinary integral only in \(|\operatorname{Im}z|<1\); weighted Euclidean density is singular |
| \(G=\tfrac12\sqrt r\,V\), \(u=\tfrac12\log r\) | Fourier character, reflection, and \(1-\partial_u^2\) | Rescaling and the exponential tails |
| Same \(G\) on the three-dimensional cylinder | Operator \(1-\Delta_{\mathcal C}\), with angular geometry retained | Explicit product metric and normalized volume |
| Mellin variable \(\lambda\) | Factor \(\lambda(1-\lambda)\) and reflection \(\lambda\mapsto1-\lambda\) | Real spectral observations now lie on a vertical line |
| Squared radius \(y=r^2\) | The original summands become \(e^{-\pi n^2y}\) | The spatial operator becomes \(4y\partial_y^2+6\partial_y\); less clean for geometry |

For comparison with the earlier all-complex integral, put
\[
P(u)=e^{|u|}A(e^{2|u|})
=\frac12\big[e^u\Theta(e^{2u})-e^{|u|}\big].
\]
It has double-exponential tails and a derivative jump of \(-1\) at zero.
The previous formula is exactly
\[
16H(0,z)=1-(1+z^2)\int_{\mathbb R}P(u)e^{izu}\,du,
\qquad z\in\mathbb C.
\tag{19}
\]
The relation
\(G=\tfrac12e^{-|u|}-P\) converts (19) to (9) in the common strip.
Thus the clean smooth formula and the entire-integral formula differ by
an explicitly known Green kernel. The choice is between smoothness and
stronger tail decay, with the correction retained exactly.

**Working preference:** keep \(\Theta\) primary, show \(V\) as its
explicit harmonic subtraction, and use \(G\) only when the square-root
rescaling or cylinder operator is being used. Do not replace the visible
chain by unexplained abbreviations. Keep (5) and (13) side by side until
the intended geometry of the auxiliary flow is settled.

## 7 What these changes permit in a later flow discussion

This section records Edward Baker's subsequent suggestion to treat
Newman time as one possible flow direction and to consider a different
or unified auxiliary flow. The zero-time formulas remain the main result;
no new flow is selected here.

### Exact observation preservation still fixes the radial average

For an integrable later cylinder field \(G_s(u,\omega)\), retaining
all real observations with the kernel in (13) fixes its spherical mean
\(\overline G_s(u)\), by Fourier uniqueness and \(1+z^2\ne0\).
Thus a change of variables alone does not create new radial freedom under
the old exact-pairing invariant. Angular freedom remains. A unique,
rotation-equivariant evolution from radial data stays radial unless
additional fields or asymmetric data are supplied.

### A natural auxiliary heat flow if zero preservation is sufficient

Ordinary cylinder heat,
\[
\partial_sG_s=\Delta_{\mathcal C}G_s,\qquad s\ge0,
\tag{20}
\]
is positive and nontrivial even on radial initial data. Define its observed
function by the right side of (13), divided by \(16\). Then
\[
\boxed{H_s(z)=e^{-sz^2}H(0,z).}
\tag{21}
\]
This preserves every zero and its multiplicity and allows exact recovery
of the original function by multiplication by \(e^{sz^2}\). It preserves
the zeros rather than the numerical value of each pairing. Consequently
(20) is an option only if the earlier invariant is deliberately broadened
to permit this known nonvanishing factor. The kernel and density still
have no auxiliary spectral entanglement: the kernel is fixed and the
spatial field is independent of \(z\).

### Newman flow transported to the same generating variable

For the canonical analytic heat family, the inherited relation
\(H_t=-H_{zz}\) determines its time expansion from \(H(0,z)\).
On the cylinder generator the corresponding exact evolution is
\[
\partial_tG_t=\mathcal L^{-1}u^2\mathcal L G_t.
\tag{22}
\]
Here \(\mathcal L G_t=8e^{tu^2}\Phi(u)\) in the radial canonical
sector. These statements use the source-defined analytic class and the
decaying inverse of \(\mathcal L\); they are not an unrestricted
backward-heat well-posedness assertion. Directly multiplying the
exponentially decaying \(G\) by \(e^{tu^2}\) is not this evolution.

### A first unified flow can be solved exactly

A natural linear benchmark, with constants \(\alpha,\beta\ge0\), is
\[
\partial_\tau G=
\alpha\mathcal L^{-1}u^2\mathcal L G+\beta\Delta_{\mathcal C}G.
\tag{23}
\]
Equivalently, the differential source \(\mathcal L G\) obeys diffusion
plus a quadratic potential. Its observation satisfies
\[
\boxed{\partial_\tau\mathscr H
=-\alpha\partial_z^2\mathscr H-\beta z^2\mathscr H,
\qquad \mathscr H(0,z)=H(0,z).}
\tag{24}
\]
This equation alone does not assert global existence of an arbitrary
spatial state. For the canonical observation its exact solution in the
following interval provides a useful comparison.

For \(\alpha\beta>0\), define
\[
\gamma=2\sqrt{\alpha\beta},\quad
c(\tau)=\sec(\gamma\tau),\quad
T(\tau)=\frac12\sqrt{\frac\alpha\beta}\tan(\gamma\tau),\quad
b(\tau)=\frac12\sqrt{\frac\beta\alpha}\tan(\gamma\tau).
\]
Then
\[
\boxed{
\mathscr H(\tau,z)=\sqrt{c(\tau)}\,e^{-b(\tau)z^2}
 H\big(T(\tau),c(\tau)z\big),
\quad 0\le\tau<\frac\pi{4\sqrt{\alpha\beta}}.
}
\tag{25}
\]
For verification, substitution reduces (24) to
\[
T'=\alpha c^2,\quad c'=4\alpha bc,\quad
b'=4\alpha b^2+\beta,\quad
(\log\sqrt c)'=2\alpha b,
\]
with initial values \(T=b=0\), \(c=1\). The displayed trigonometric
functions satisfy these identities. At \(\beta=0\) one has
\(\mathscr H=H(\alpha\tau,z)\); at \(\alpha=0\) one has
\(\mathscr H=e^{-\beta\tau z^2}H(0,z)\).

In this specific constant-coefficient linear combination, the nonzero
Gaussian factor and positive spatial scaling transport the same zeros
as Newman flow at the rescaled time \(T(\tau)\). A collision at
\((T,A)\) is transported to \(z=A/c(\tau)\) with the same multiplicity.
This is a precise scope limitation, not an exclusion of nonlinear,
coupled-field, nonradial or differently constrained unified flows.

The two separate directions are not commuting flows on the observation:
\[
[-\partial_z^2,-z^2]=4z\partial_z+2.
\]
A two-parameter construction therefore needs a compatibility rule;
one combined evolution parameter is already well-defined by (24).

As a collision check, the explicit positive-source double-zero control
in [Note01, Section 7](../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md)
is transported by (25) as well, on its admitted local time interval.
Its missing premise is the canonical integer-square theta arithmetic;
the linear combination (24) imposes no new condition using that premise.
Hence this benchmark cannot supply a new collision exclusion by itself.

## 8 The next useful design decision

First decide whether direct integral convergence for every complex spectral
argument is required, or whether a strip representation with analytic
continuation is acceptable. The smooth potential is the latter option.
Then choose whether the auxiliary flow must preserve the entire
observation exactly or may preserve it up to a known nonvanishing factor.
The latter admits the simple radial cylinder heat flow (20); the former
still fixes the spherical mean. Then decide whether Euclidean spatial
geometry or the cylinder geometry is the intended setting. These choices
should precede new nonlinear terms or a proposed collision diagnostic.

A productive next comparison would keep the displayed theta generator
and operator, explain what geometry the auxiliary evolution changes, and
identify an observable that distinguishes a double cancellation from a
simple zero. The benchmark (25) identifies what a proposed combined flow
must add beyond a rescaling of existing heat dynamics.

## Sources and verification scope

The [founding radial note](../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md),
[current transform manuscript](../book/main.tex), and
[working changes](../book/changes/01_GENERATING_FUNCTIONS_AND_KERNEL_CHANGE_WORKING_NOTE_20261028.md)
supply the normalization and endpoint data. The
[result index](../../../../result-summaries/README.md), especially
[geometric realizations](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md),
and [pattern index](../../../../avoid/README.md), especially
[coordinate re-realizations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
limit the interpretation: the identities here improve the formulation,
not a collision bound.

Selected primary-reference checks on 28 October 2026:
[NIST DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), at zero theta argument
and parameter \(ir^2\), gives the inherited inversion;
[NIST DLMF 1.14.32 and the following strip statement](https://dlmf.nist.gov/1.14.iv)
fix the Mellin convention. The half-power conjugation, potential,
cylinder normalization, endpoint comparison, and unified-flow formula
are derived explicitly above. No external nonlinear-PDE theorem is
imported. Checking is by the same assistant, not independent specialist
review; no numerical campaign or manuscript revision is claimed.
