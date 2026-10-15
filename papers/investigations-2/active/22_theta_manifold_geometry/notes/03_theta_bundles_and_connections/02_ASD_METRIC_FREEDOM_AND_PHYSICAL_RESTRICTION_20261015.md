# ASD metric freedom and the physical restriction

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

## Scope and result

The theta line bundle has a genuine ASD Chern connection on its marked semi-flat hyperkähler family. The metric originally used to produce that connection grows rapidly along the physical cusp. This growth is not determined by the ASD curvature: another Hermitian metric on the same holomorphic line bundle has the same curvature, preserves the vertical source operator, and restricts to unit norm and zero connection along the physical path.

The physical path and its external two-source product pull back the connection to a flat connection. Direct differentiation in those source variables therefore introduces no ambient ASD curvature term. Transverse theta-jet differentiation, however, must occur before restriction and gives explicit lower-jet commutators. These results identify what the physical transform retains. They do not prove a signed theta estimate or exclude a collision.

## 1. Classification of base-only ASD metric changes

Write τ=p+iq, z=r+τs, and use the manuscript's metric and connection

\[
 h=\exp\!\left(-2\pi(\operatorname{Im}z)^2/q\right),\qquad
 A=2\pi i s\,dz-\pi i s^2\,d\tau,\qquad
 F=-2\pi i\,dr\wedge ds.
\]

For a smooth real function b=b(p,q), set h_b=e^b h. Then

\[
 A_b=A+\frac12(b_p-i b_q)d\tau,\qquad
 F_b=-2\pi i\,dr\wedge ds
       +\frac i2(b_{pp}+b_{qq})\,dp\wedge dq.
\]

The semi-flat Hodge star interchanges q dp∧dq and dr∧ds. Hence

\[
 \boxed{F_b\text{ is ASD}\iff b_{pp}+b_{qq}=4\pi q.}
\]

Every base-only solution on the upper half-plane has the form

\[
 b=\frac{2\pi}{3}q^3+2\operatorname{Re}g(\tau),
 \qquad g\text{ holomorphic on }\mathbb H.
\]

Indeed the difference from the displayed particular solution is harmonic; the simply connected upper half-plane supplies its global harmonic conjugate. Every such metric has the same curvature

\[
 F_b=2\pi i\bigl(q\,dp\wedge dq-dr\wedge ds\bigr).
\]

All base-only corrections leave the relative operator D=∂z+2πis unchanged. This classifies base-only rescalings, not all ASD connections on the total space.

## 2. A metric adapted to the physical path

Choose g(τ)=−πiτ³/3. Its real and imaginary parts are

\[
 2\operatorname{Re}g=2\pi p^2q-\frac{2\pi}{3}q^3,
 \qquad \operatorname{Im}g=-\frac\pi3p^3+\pi pq^2.
\]

Thus

\[
 \boxed{\widetilde h=e^{2\pi p^2q}h},\qquad
 \widetilde A=\widehat A+dg
             =A-\pi i(q^2+\tau^2)\,d\tau
\]

has the same ASD curvature as the original metric h_hat=e^{2πq³/3}h. On

\[
 \gamma(u)=(\tau=iq,z=0),\quad q=e^{4u},\quad u\ge0,
\]

one has identically

\[
 \gamma^*\widetilde h=1,\qquad\gamma^*\widetilde A=0.
\]

The original representative instead satisfies

\[
 \gamma^*\widehat h=e^{2B(u)},\qquad
 \gamma^*\widehat A=dB,\qquad
 B(u)=\frac\pi3e^{12u},\quad B'(u)=4\pi e^{12u}.
\]

The new metric descends through fiber translations on the same marked family. It supplies neither full modular descent nor a complete ambient metric.

Keeping the arithmetic section θ fixed while changing h_hat to h_tilde changes its norm. This is not a unitary gauge change of one fixed Hermitian metric. There is a holomorphic isometry

\[
 (L,\widetilde h)\longrightarrow(L,\widehat h),\qquad
 v\longmapsto e^{g(\tau)}v,
\]

which also changes θ to e^gθ. If using this isometry, transport both the section and the observation covector. The physical source formula is fixed in the marked arithmetic frame. Thus ASD curvature alone does not select the norm of the distinguished arithmetic section; an estimate using it must specify the metric and its physical-path normalization.

## 3. The precise cusp conclusion

Isolating the n=1 theta term and bounding the tail gives

\[
 \Phi(u)=2\pi^2q^{9/4}e^{-\pi q}
 \left(1-\frac3{2\pi q}+O(e^{-3\pi q})\right).
\]

For the source section S=Φe in the marked holomorphic frame,

\[
 \|S\|_{\widehat h}^2\sim4\pi^4q^{9/2}
 e^{2\pi q^3/3-2\pi q},\qquad
 \|S\|_{\widetilde h}^2=\Phi^2.
\]

The first is not integrable against du=dq/(4q) or induced path length dℓ=√q dq. The second is integrable against both, including fixed polynomial source weights and physical heat weights on compact time intervals. Divergence is a real obstruction for the specified h_hat norm, not an intrinsic obstruction from the shared ASD curvature. Both representatives retain infinite ambient Yang–Mills action because their curvature and ambient metric agree.

## 4. Physical and two-source restriction

Every two-form pulls back to zero on a one-dimensional path. Here the stronger explicit statements above give zero connection in the adapted arithmetic frame and the exact connection dB in the original frame. On a path segment there is no nontrivial curvature holonomy.

For the external tensor product on the two-source product, the original arithmetic-frame connection is

\[
 \mathcal A=dB(u)+dB(v),
\]

and its curvature is

\[
 \pi_1^*\gamma^*F_b+\pi_2^*\gamma^*F_b=0.
\]

In particular the two tangential covariant derivatives commute. A dual or conjugate factor gives the appropriate sign changes and the same flatness conclusion. This concerns the natural external product, not arbitrary extensions away from it.

In the original metric take the unitary frame e_U=e^{−B}e along γ. The source and physical test covector have coefficients

\[
 S=e^B\Phi\,e_U,\qquad
 \kappa_{t,x}=e^{-B}e^{tu^2}\cos(xu)\,e_U^*.
\]

Their pairing is exactly e^{tu²}Φ cos(xu). Differentiating source and dual together cancels the two connection terms. Taking the source norm before the pairing loses this cancellation. The same paired cancellation occurs in each variable of the complete two-source correlation.

The [complete signed correlation calculation](03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md) retains the full arithmetic kernels and lower endpoints. It acquires no new direct curvature term merely by rewriting these one-dimensional derivatives covariantly.

## 5. Transverse commutators before restriction

Flat pullback does not justify commuting all ambient theta jets. In a marked holomorphic chart near the zero section set

\[
 a=2\pi is=\pi(z-\bar z)/q,\quad c=\pi/q,\quad
 X=4q\partial_q\big|_{p,z,\bar z},\quad
 N_b=\nabla_X^{(b)}.
\]

The chosen X extends the physical tangent in this chart. Since lattice translations depend on τ, it is not asserted to be a global horizontal vector field on the quotient. All following commutators are computed before restricting to z=0.

The connection in this direction is

\[
 N_b=X+4\pi q s^2+\beta_b,
 \qquad\beta_b=2q b_q+2iq b_p.
\]

Because β_b is base-only,

\[
 [X,\mathcal D]=-4a,\qquad
 [4\pi q s^2,\mathcal D]=2a,\qquad
 [\beta_b,\mathcal D]=0,
\]

so [N_b,D]=−2a. Using [D,a]=c and [D,c]=0 gives

\[
 \boxed{[N_b,\mathcal D^k]
 =-2ka\mathcal D^{k-1}-k(k-1)c\mathcal D^{k-2}.}
\]

For k=1 the final term is absent. At the zero section a=0, but for k≥2

\[
 [N_b,\mathcal D^k]\big|_0
 =-k(k-1)\frac\pi q\mathcal D^{k-2}\big|_0.
\]

The fourth-jet commutator therefore contributes −12πq^{−1}D². Setting the first-order commutator to zero at the zero section before taking higher derivatives would wrongly discard this term. These terms are independent of the base rescaling and already occur before the ASD correction.

Combining this with Jacobi heat gives the arithmetic-coefficient recurrence

\[
 J_k'=\frac q\pi J_{k+2}-(2k+1)J_k
       -k(k-1)\frac\pi qJ_{k-2},
 \qquad J_k=(\mathcal D^k\vartheta)(0,iq).
\]

The negative-index term is absent for k=0,1. The base coefficient β_b occurs on both sides of the covariant identity and cancels in the fixed arithmetic coefficients. The [correlation note](03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md) supplies its detailed use for the complete source and exact endpoint terms.

## 6. Precise no-go scope and remaining opportunity

A new curvature-sign term cannot arise solely from tangential covariant differentiation on the physical path and its external two-source product. Nor is the original cusp growth a curvature-invariant obstruction.

This does not rule out a theta-specific estimate using transverse identities, modular information, an independently motivated metric normalization, or global boundary conditions. On the two-dimensional zero section the curvature remains

\[
 F_b\big|_{z=0}=2\pi i q\,dp\wedge dq.
\]

Transverse p-variation therefore retains nonzero curvature. A useful proposal must explain how that information enters the prescribed physical observation with phase cos(xu). Identifying its external spectral variable with the elliptic base coordinate p requires a new justified transform identity.

The signed estimate remains open. The sharpened task is to use information beyond the flat restricted connection, retain all lower-jet commutators, and control the complete physical observation after arithmetic and spectral cancellation.

## Exact checks and provenance

This continues the [initial ASD construction](01_COVARIANT_SOURCE_AND_ASD_CONNECTION_20261015.md). The [metric checker](../../numerics/check_asd_path_metric.py) passes 35 exact rational assertions covering the displayed base potentials, their holomorphic difference, the physical-path normalization, and external-product restriction. The classification and convergence arguments are analytic proofs above; finite checks do not establish them. The [review](../../reviews/02_CONNECTION_BRIDGE_AND_INNER_TURNING_REVIEW_20261015.md) records the internal comparison.
