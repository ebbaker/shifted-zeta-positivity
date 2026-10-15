# Covariant theta source and an explicit ASD connection

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

## The marked family and conventions

Work on the marked elliptic family over the upper half-plane, with `τ=p+iq`, `q>0`, and `z=r+τs`. Fiber coordinates `r,s` are periodic with period one. The theta section is

\[
\vartheta(z,\tau)=\sum_{n\in\mathbb Z}e^{\pi i n^2\tau+2\pi i nz}.
\]

It transforms by `exp(-π i n²τ-2π i nz)` under `z ↦ z+m+nτ`. In the corresponding holomorphic frame, the squared norm

\[
h=e^{-2\pi(\operatorname{Im}z)^2/q}
\]

is compatible with this multiplier. Use the Chern convention `A=∂log h`, `F=dA`. Direct differentiation gives

\[
A=2\pi i s\,dz-\pi i s^2\,d\tau,
\qquad F=\frac\pi q(dz-s\,d\tau)\wedge(d\bar z-s\,d\bar\tau)
       =-2\pi i\,dr\wedge ds.
\]

This has fiber degree one in the convention `c₁=iF/(2π)`. The connection is unitary with respect to `h`; the displayed frame itself is holomorphic, not unitary.

## The source is a covariant fourth jet

The vertical derivative is

\[
\mathcal D=\nabla_{\partial_z}=\partial_z+2\pi i s.
\]

Its iterates transform as smooth section coefficients under fiber translation. They are not holomorphic jets: `[∂_{bar z},D]=-π/q`. At the zero section,

\[
\mathcal D^2\vartheta=\vartheta_{zz}+\frac\pi q\vartheta,
\qquad
\mathcal D^4\vartheta=\vartheta_{zzzz}
 +\frac{6\pi}{q}\vartheta_{zz}
 +\frac{3\pi^2}{q^2}\vartheta.
\]

For `y=e^{4u}`, the complete physical source is exactly

\[
\Phi(u)=\frac{y^{1/4}}{16\pi^2}
 \left[y^2\mathcal D^4\vartheta-3\pi^2\vartheta\right]_{z=0,\,\tau=iy}.
\]

Substitution of the preceding fourth-jet formula recovers the ordinary source operator `y^{1/4}(y²∂_y²+(3/2)y∂_y)θ(0,iy)`. In particular, the correction term cannot be discarded. The physical field becomes

\[
H(t,x)=\frac1{64\pi^2}\int_1^\infty
 e^{t(\log y)^2/16}y^{1/4}
 \left[y^2\mathcal D^4\vartheta-3\pi^2\vartheta\right]_{0,iy}
 \cos\!\left(\frac{x\log y}{4}\right)\frac{dy}{y}.
\]

This is a coefficient identity in the specified marked frame. The positive physical heat parameter is distinct from Jacobi evolution in `τ`.

## A nonflat hyperkähler background and an ASD correction

The metric

\[
g=q(dp^2+dq^2)+q^{-1}(dr+p\,ds)^2+q\,ds^2
\]

has the parallel triple

\[
\omega_I=q\,dp\wedge dq+dr\wedge ds,
\qquad \omega_J+i\omega_K=d\tau\wedge dz.
\]

The closed, normalized triple and the constant Hermitian determinant give a hyperkähler metric. The totally geodesic base slices have sectional curvature `1/(2q³)`, so this metric is nonflat.

The original theta curvature is not ASD. Set

\[
\widehat h=e^{2\pi q^3/3}h.
\]

The base correction is `∂(2πq³/3)=-π i q²dτ`, hence

\[
F_{\widehat\nabla}=2\pi i(q\,dp\wedge dq-dr\wedge ds).
\]

For the hyperkähler orientation, the Hodge star interchanges `q dp∧dq` and `dr∧ds`. Thus this curvature is ASD. Its closure gives the abelian Yang–Mills equation. Because the correction vanishes on `∂_z`, the vertical operator `D` and complete source formula are unchanged.

## Scope and next use

This is an actual theta line bundle with an actual abelian ASD connection. It is not yet a global compactification of the physical problem. The metric descends through fiber translations but not the full modular action; the base term transforms by `|cτ+d|^{-6}`. It is incomplete toward `q=0`. The norm squared of the real curvature `F_hat/i` is the constant `8π²`, while the total volume on the marked family is infinite. The connection therefore does not have finite global action. The new Hermitian factor also grows at the cusp and does not automatically compare with physical cancellation.

The useful next calculation is the complete two-source identity before estimating absolute values. It must retain the line connection, its curvature and commutators, the arithmetic section, the heat multiplier, the phase, and all endpoints. A signed estimate relative to the physical energy remains the objective.

The [manuscript](../../manuscript/theta_manifold_geometry.tex), Section 8, supplies the full derivation. The [two new exact checkers](../../numerics/README.md) independently check the connection/source algebra. Their 49 overlapping assertions are finite algebra checks, not a theta sign or collision-exclusion certificate.
