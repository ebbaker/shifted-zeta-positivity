# Working manuscript changes for the generating functions and kernel

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.
Chat0014, Add Laplacian motivation to book.

**Status: working change list, not implemented.** Accumulate and refine the
proposed changes for this chat here. Apply the agreed changes to
[the manuscript](../main.tex) together only after Edward Baker finalizes
this document and requests implementation. The choice of kernel and
auxiliary evolution remains open.

## Change 01 Make the generating theta functions primary

Edward Baker requests that the exposition center on
\[
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
\Theta(r)=1+2A(r),\qquad r>0.
\]
These are the generating profiles from which the source and observation
are built. The abbreviations \(Q(r)=\Delta_3\Theta(r)\) and
\(q_t(u)=e^{tu^2}\Phi(u)\) hide the differential structure and the
separate time weight. In the proposed exposition, display those
operations explicitly in the principal definitions and formulas for
\(H\), the spatial density, and the observation kernel. Derived notation,
if retained for a later calculation, should remain secondary.

Keep the operator visible:
\[
\Delta_3 f(r)=f''(r)+\frac2r f'(r),\qquad
\Phi(u)=\frac12r^{5/2}\Delta_3 A(r)
       =\frac14r^{5/2}\Delta_3\Theta(r),\qquad r=e^{2u}.
\]
The earlier motivating identity can likewise be written without a new
primitive symbol:
\[
(\partial_u^2-1)\big[e^u A(e^{2u})\big]
=4e^{5u}(\Delta_3 A)(e^{2u})=8\Phi(u).
\]

The selection of \(A\) or \(\Theta\) as the principal notation is still
open. \(A\) displays the decaying Gaussian sum; \(\Theta\) displays the
simple inversion relation \(\Theta(r)=r^{-1}\Theta(1/r)\). Both formulas
below are recorded so that this choice can be made on mathematical and
expository grounds.

### Direct formulas for H with the Laplacian visible

The complete logarithmic-radius exponential representation is
\[
\boxed{\begin{aligned}
H(t,z)&=\frac1{16}\int_0^\infty
 e^{\frac t4(\log r)^2}\,r^{\frac32+\frac{iz}{2}}
 \left(\Theta''(r)+\frac2r\Theta'(r)\right)\,dr\\
&=\frac18\int_0^\infty
 e^{\frac t4(\log r)^2}\,r^{\frac32+\frac{iz}{2}}
 \left(A''(r)+\frac2rA'(r)\right)\,dr.
\end{aligned}}
\]
Equivalently, on the original exterior half of the source,
\[
H(t,z)=\frac14\int_1^\infty
 e^{\frac t4(\log r)^2}r^{3/2}
 \left(A''(r)+\frac2rA'(r)\right)
 \cos\!\left(\frac z2\log r\right)\,dr.
\]
These identities retain the manuscript's normalization, for real \(t\)
and complex \(z\). The theta tails and reflection justify convergence.
The radial Laplacian acts on the generating profile before multiplication
by the time weight. Inserting that weight inside the Laplacian would
introduce additional derivative terms and change the formula.

For the existing whole-space observation, the same identity reads
\[
H(t,z)=\frac1{64\pi}
\int_{\mathbb R^3\setminus\{0\}}
 e^{\frac t4(\log|X|)^2}|X|^{-1/2}
 (\Delta_3\Theta)(|X|)\,
 e^{\frac{iz}{2}\log|X|}\,dX.
\]
Thus its proposed density formula is
\[
\rho(t;X)=\frac{e^{\frac t4(\log|X|)^2}}{64\pi\sqrt{|X|}}
 (\Delta_3\Theta)(|X|),\qquad X\ne0.
\]
This keeps the generating profile, differential operator, time weight,
and spectral phase separately visible. Here the Laplacian is the
classical radial derivative on \(r>0\). The distributional Laplacian
of \(\Theta(|X|)\) also contains \(-4\pi\delta_0\); that point source
is not part of this ordinary integral.

## Change 02 Display a kernel transform with the generating function as input

Edward Baker also requests the kernel-transform equation in terms of
\(A\) or \(\Theta\). In the formulas above, the transform acts on a
weighted Laplacian of the generating function. If the generating function
itself is to be the input, the following exact exterior representation
is available and should be considered in the notation discussion:
\[
\boxed{
H(t,z)=\frac1{16}+\int_1^\infty A(r)\,\mathcal K_t(z,r)\,dr,
}
\]
where
\[
\boxed{
\mathcal K_t(z,r)=\frac14\frac d{dr}
\left[r^2\frac d{dr}
 \left(e^{\frac t4(\log r)^2}r^{-1/2}
       \cos\!\left(\frac z2\log r\right)\right)\right].
}
\]
Writing the derivatives explicitly gives
\[
\mathcal K_t(z,r)=
\frac{e^{\frac t4(\log r)^2}}{16\sqrt r}
\left[
 \big(t^2(\log r)^2+2t-z^2-1\big)
       \cos\!\left(\frac z2\log r\right)
 -2tz\log r\sin\!\left(\frac z2\log r\right)
\right].
\]
Equivalently,
\[
H(t,z)=\frac1{16}
 +\frac12\int_1^\infty\big(\Theta(r)-1\big)
       \mathcal K_t(z,r)\,dr.
\]
The subtraction of \(1\) retains the decay of \(A\) at infinity.

### The boundary contribution and the kernel convention

For the derivation only, set
\(f_{t,z}(r)=e^{t(\log r)^2/4}r^{-1/2}\cos(z\log r/2)\).
Two integrations by parts give
\[
\frac14\int_1^\infty f_{t,z}(r)(r^2A'(r))'\,dr
=\frac14\big[r^2(f_{t,z}A'-f_{t,z}'A)\big]_1^\infty
 +\frac14\int_1^\infty A(r)(r^2f_{t,z}'(r))'\,dr.
\]
The outer boundary vanishes because \(A\) and its derivatives have
Gaussian decay. At \(r=1\), \(f_{t,z}(1)=1\) and
\(f_{t,z}'(1)=-1/2\). Differentiating the inversion identity at \(1\)
gives
\[
\Theta'(1)=-\frac12\Theta(1),\qquad
A'(1)+\frac12A(1)=-\frac14.
\]
The boundary term is therefore \(+1/16\), independent of \(t,z\).
It cannot be omitted: this is a transform with a fixed additive boundary
contribution. Equivalently, \(H(t,z)-1/16\) is the linear kernel transform
of \(A\) displayed above.

This representation puts both physical-time and spectral dependence in
\(\mathcal K_t\), while leaving \(A\) independent of \(t,z\).
The kernel has no auxiliary parameter \(s\). Its cosine arises from
folding the original even source onto the exterior region; this identity
does not finalize a choice of cosine over the whole-space exponential
kernel. No integration by parts through the singular origin is used.

## Change 03 Calculate the kernel explicitly and keep the spatial domain visible

Edward Baker requests the exact kernel calculation in three-dimensional
volume measure and an explanation of the change from \((0,\infty)\) to
\([1,\infty)\). The exterior representation in Change 02 is an alternative
obtained by returning to the original half-line observation. It does not
replace the full-space representation.

### Why the two radial domains appeared

The original cosine formula has \(u\ge0\). Under \(r=e^{2u}\), this
is \(r\ge1\), or the exterior of the unit sphere in three dimensions.
The exponential formula uses the even extension to all \(u\in\mathbb R\),
so its radial domain is \(0<r<\infty\). Reflection pairs the interior
\(r<1\) with the exterior \(r>1\). Folding the two halves together
changes the exponential to a cosine and doubles the prefactor:
\[
\begin{aligned}
H(t,z)&=\frac1{16}\int_0^\infty
 e^{t(\log r)^2/4}r^{3/2+iz/2}\Delta_3\Theta(r)\,dr\\
&=\frac18\int_1^\infty
 e^{t(\log r)^2/4}r^{3/2}\Delta_3\Theta(r)
 \cos\!\left(\frac z2\log r\right)\,dr.
\end{aligned}
\]
The domain and prefactor must always be stated together. The previous
reply switched to the folded exterior representation to transfer the
Laplacian onto a kernel acting on the decaying function \(A\); that
choice of domain was not explained clearly enough.

### The differential calculation in three dimensions

For the calculation, write \(r=|X|\), \(L=\log r\), and
\[
w_{t,z}(r)=r^{-1/2}v_{t,z}(L),\qquad
v_{t,z}(L)=e^{tL^2/4+izL/2}.
\]
The derivatives of a radial profile give
\[
\begin{aligned}
w_{t,z}'(r)&=r^{-3/2}\left(v_{t,z}'(L)-\tfrac12v_{t,z}(L)\right),\\
w_{t,z}''(r)&=r^{-5/2}\left(v_{t,z}''(L)-2v_{t,z}'(L)
                                  +\tfrac34v_{t,z}(L)\right),\\
\Delta_Xw_{t,z}(|X|)&=r^{-5/2}\left(v_{t,z}''(L)-\tfrac14v_{t,z}(L)\right).
\end{aligned}
\]
Primes on \(v\) denote differentiation with respect to \(L\).
Since
\[
v_{t,z}'=\frac{tL+iz}{2}v_{t,z},\qquad
v_{t,z}''=\left(\frac t2+\frac{(tL+iz)^2}{4}\right)v_{t,z},
\]
the exact result is
\[
\boxed{
\Delta_X w_{t,z}(|X|)
=\frac{e^{tL^2/4}r^{-5/2+iz/2}}4
 \left[(tL+iz)^2+2t-1\right].
}
\]
In particular, the polynomial in the kernel is
\[
(tL+iz)^2+2t-1=t^2L^2+2itzL+2t-z^2-1.
\]
All these are classical identities for \(r>0\).

For the earlier cosine weight
\(f_{t,z}(r)=e^{tL^2/4}r^{-1/2}\cos(zL/2)\), symmetrizing the
exponential calculation in \(z\) gives
\[
\boxed{
\Delta_Xf_{t,z}(|X|)=\frac{e^{tL^2/4}}{4r^{5/2}}
\left[
 (t^2L^2+2t-z^2-1)\cos(zL/2)
 -2tzL\sin(zL/2)
\right].
}
\]
Symmetrization, rather than taking a real part, also covers complex \(z\).

### The exact exterior formula with three-dimensional volume

Because \(dX=r^2\,dr\,d\omega\) and \(\int_{\mathbb S^2}d\omega=4\pi\),
Change 02 becomes
\[
\boxed{
H(t,z)=\frac1{16}
 +\int_{|X|>1}A(|X|)\,\mathcal K^{\mathrm{ext}}_t(z,X)\,dX,
}
\]
where the fully evaluated spatial kernel is
\[
\boxed{
\mathcal K^{\mathrm{ext}}_t(z,X)
=\frac{e^{tL^2/4}}{64\pi r^{5/2}}
\left[
 (t^2L^2+2t-z^2-1)\cos(zL/2)
 -2tzL\sin(zL/2)
\right],\qquad r=|X|>1.
}
\]
Equivalently, \(\mathcal K^{\mathrm{ext}}_t=\Delta_Xf_{t,z}/(16\pi)\).
The radial kernel in Change 02 and this spatial kernel use different
measures: \(\mathcal K_t(z,r)=4\pi r^2\mathcal K^{\mathrm{ext}}_t(z,X)\).
This accounts for the different powers of \(r\) and factors of \(\pi\).

### A full-space kernel transform with the generator displayed

The unmodified full-space formula remains
\[
\boxed{
H(t,z)=\frac1{64\pi}\int_{\mathbb R^3}
 (\Delta_3\Theta)(|X|)\,
 e^{t(\log|X|)^2/4}|X|^{-1/2+iz/2}\,dX.
}
\]
The integrand extends flatly at zero. This is the simplest whole-space
formula if the Laplacian stays on the generating profile.

To move the Laplacian onto the kernel over the full space, subtract the
explicit harmonic backgrounds at the two ends. Modularity gives
\[
\Theta(r)-\max\{1,r^{-1}\}
=\begin{cases}
\Theta(r)-r^{-1}=2r^{-1}A(1/r),&0<r<1,\\
\Theta(r)-1=2A(r),&r\ge1.
\end{cases}
\]
The difference is positive, flat at zero, rapidly decaying at infinity,
and continuous at \(1\). We keep it written in terms of \(\Theta\)
so that the subtraction is visible in the transform. The exact formula is
\[
\boxed{
H(t,z)=\frac1{16}
 +\int_{\mathbb R^3}
 \left[\Theta(|X|)-\max\{1,|X|^{-1}\}\right]
 \mathcal K^{\mathrm{full}}_t(z,X)\,dX,
}
\]
with the fully evaluated exponential kernel
\[
\boxed{
\mathcal K^{\mathrm{full}}_t(z,X)
=\frac{e^{tL^2/4}r^{-5/2+iz/2}}{256\pi}
 \left[t^2L^2+2itzL+2t-z^2-1\right],
\quad r=|X|>0,\quad L=\log r.
}
\]
Thus \(\mathcal K^{\mathrm{full}}_t=\Delta_Xw_{t,z}/(64\pi)\).
The product in the integral extends flatly at the origin. The integral
converges absolutely for every real \(t\) and complex \(z\); the endpoint
bounds are locally uniform in the parameters. The formula therefore uses
all \(0<r<\infty\), keeps the exponential phase, and has no auxiliary
parameter \(s\) in its kernel.

The equivalent \(A\)-version replaces the bracket by
\(A(r)-\tfrac12\max\{r^{-1}-1,0\}\) and multiplies the displayed
kernel by \(2\). Both versions expose the same fixed subtraction.

### Why the unit sphere still contributes 1 over 16

For this verification only, denote the displayed subtracted profile by
\(F(r)=\Theta(r)-\max\{1,r^{-1}\}\). It is continuous at \(1\),
but its radial derivative has the jump
\[
F'(1+)-F'(1-)=\Theta'(1)-\bigl(\Theta'(1)+1\bigr)=-1.
\]
Off the unit sphere, \(\Delta_3F=\Delta_3\Theta\). Let
\(\delta_{\mathbb S^2}\) denote surface measure as a distribution:
\(\langle\delta_{\mathbb S^2},\varphi\rangle
=\int_{|X|=1}\varphi\,dS\). Then
\[
\Delta_XF(|X|)=(\Delta_3\Theta)(|X|)-\delta_{\mathbb S^2}.
\]
There is no central point source in this equation because \(F\) is
flat at zero. Applying Green's identity separately inside and outside
\(|X|=1\), retaining the derivative jump, gives
\[
\int_{\mathbb R^3}(\Delta_3\Theta)(|X|)w_{t,z}(|X|)\,dX
=\int_{\mathbb R^3}F(|X|)\Delta_Xw_{t,z}(|X|)\,dX
 +\int_{|X|=1}w_{t,z}(1)\,dS.
\]
All endpoint terms at zero and infinity vanish by the decay of \(F\).
On the unit sphere \(w_{t,z}(1)=1\), so the last term is \(4\pi\).
Dividing by \(64\pi\) gives the required \(1/16\). This derivation
uses the piecewise smooth profile and its surface term; it does not
assume \(F\) is smooth across the unit sphere.

At \(t=0\), \(z=\pm i\), the polynomial in the full kernel vanishes
identically, so the formula returns \(H(0,\pm i)=1/16\), consistent
with the original theta flux normalization.

### Why simply moving the Laplacian onto the kernel can fail

The original \(\Delta_3\Theta\) decays at both ends. The undifferentiated
\(\Theta\) instead approaches \(1/r\) at zero and \(1\) at infinity;
\(A\) approaches \(1/(2r)-1/2\) at zero. For \(t\ge0\), pairing these
raw profiles with the differentiated kernel generally produces divergent
end integrals or nonvanishing boundary terms. The preceding full-space
subtraction makes the formula valid throughout the stated time range.

This restriction is scoped: for real \(t<0\), the Gaussian in \(\log r\)
forces the bare weight and its derivatives to vanish sufficiently rapidly
at both ends. In that range one also has the simpler, unregularized identity
\[
H(t,z)=\int_{\mathbb R^3}\Theta(|X|)
                  \mathcal K^{\mathrm{full}}_t(z,X)\,dX,
\qquad t<0,
\]
with no additive constant. It cannot be carried to \(t\ge0\) by
silently discarding the endpoint terms. The subtracted formula above
has no such restriction.

The manuscript change under discussion should distinguish three choices:
the full-space pairing with \(\Delta_3\Theta\), the exterior pairing
with \(A\), and the full-space pairing with the explicitly subtracted
\(\Theta\). These are equivalent canonical observations with different
kernels and boundary bookkeeping, not a selected auxiliary evolution.

## Related zero-time rescaling brainstorm

Edward Baker subsequently requests focusing on \(t=0\) and reconsidering
how auxiliary and Newman evolution should be related. The
[rescaling brainstorm](../../brainstorm/08_ZERO_TIME_RESCALINGS_AND_FLOW_BRAINSTORM_20261028.md)
compares the smooth potential \(1+r^{-1}-\Theta(r)\), the square-root
rescaling and the three-dimensional cylinder. Its
[continuation](../../brainstorm/09_GENERATING_THETA_AND_FLOW_CONTINUATION_20261028.md)
summarizes the formulas and flow choices. These remain options for this
working change list; the manuscript has not been changed and no preferred
flow or relaxation of the invariant has been approved.

## Decisions to settle before the combined manuscript revision

- Choose whether \(A\), \(\Theta\), or both should lead the definitions.
- Decide whether the main kernel pairing should keep the Laplacian on
  the generator, use the exterior transform, or use the full-space transform
  with the explicit harmonic-background subtraction and surface contribution.
- Decide which secondary abbreviations, if any, remain useful after the
  generating function and its operators are visible.

Further proposed changes from this chat should be added to this same
working document. These are expository choices and exact rewritings of
the existing source; no auxiliary evolution has been selected.

## Sources and scope

The formulas specialize the identities in
[founding Note01, Sections 2 and 3](../../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md)
and [the current manuscript, Sections 1 and 3](../main.tex).
The exterior boundary calculation agrees with Note01's primitive
reconstruction. Change 03 derives the corresponding full-space formula
by a direct radial differentiation and a piecewise Green identity. This
is same-assistant analytical checking, not an independent review.
The [continuation](../../brainstorm/07_NATURAL_AUXILIARY_EVOLUTION_CONTINUATION_20261028.md)
keeps the kernel open. The repository
[result index](../../../../../result-summaries/README.md), especially
[geometric realizations](../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md),
and [pattern index](../../../../../avoid/README.md), especially
[re-realizations](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
provide the scope: these changes expose existing structure and do not
supply a new collision-exclusion mechanism.
