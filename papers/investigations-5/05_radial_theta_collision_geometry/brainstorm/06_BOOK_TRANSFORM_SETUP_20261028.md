# A fixed theta transform and the meaning of preservation

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Chat0013, Review theta collision strategy.

## The requested setup

Edward Baker proposed separating the spectral argument from the density,
making the kernel independent of the auxiliary parameter, and clarifying
the variables before choosing any new evolution. The resulting
[Book manuscript](../book/main.tex) uses
\[
H(t,z)=\int_{\mathbb R^3}\rho(t;X)K(z,X)\,dX,\qquad
K(z,X)=e^{iz\ell(X)},\quad \ell(X)=\tfrac12\log|X|.
\]
The density is independent of \(z\), and the kernel is independent of both
\(s\) and \(t\). We use \(j=\nabla_X\rho\) for the spatial gradient; this
does not define a conservation flux. The third Cartesian coordinate is
\(w\), so \(X=(x,y,w)\) does not reuse spectral \(z\).

The spatial construction distributes the source coordinate \(u\) over
spheres with radius \(r=e^{2u}\). It is a realization of a source measure
in three dimensions. Integration maps this density to the spectral
function; no inverse from arbitrary spectral functions to arbitrary
spatial densities is assumed.

## Whole-space normalization

Jacobi reflection gives \(Q(r)=r^{-5}Q(1/r)\), so
\(\Phi(u)=r^{5/2}Q(r)/4\) is even and positive. Writing
\(q_t=e^{tu^2}\Phi\) on the whole real line gives
\[
H(t,z)=\tfrac12\int_{\mathbb R}q_t(u)e^{izu}\,du,\qquad
\rho(t;r)=\frac{q_t(\log r/2)}{16\pi r^3}
=\frac{e^{t\log^2r/4}Q(r)}{64\pi\sqrt r}.
\]
With normalized spherical measure \(d\sigma\),
\(dX=8\pi r^3\,du\,d\sigma\), hence
\(\rho\,dX=q_t\,du\,d\sigma/2\).
The exterior half of the old source is halved before adding its reflected
interior. Each region contributes half of the cosine observation. This
retains the original normalization and yields a smooth density flat at
the origin, without an interface jump at \(r=1\).

## What can be recovered

The transform factors through the logarithmic-radius distribution
\[
g_\rho(u)=8\pi e^{6u}\overline\rho(e^{2u}),\qquad
\overline\rho(r)=\int_{\mathbb S^2}\rho(r\omega)\,d\sigma.
\]
Fourier inversion recovers \(g_\rho\); prescribing radiality then recovers
\(\rho\). Angular information is lost. The explicit positive family
\(\rho(r)[1+\varepsilon(\omega_1^2-\omega_2^2)]\), \(|\varepsilon|<1\),
has exactly the same transform. Higher dimension alone is not the
argument for noninvertibility; this family supplies the ambiguity.

For the canonical even source, the exponential and cosine kernels agree.
For unrestricted later densities they impose different constraints:
the exponential kernel sees all of \(g_\rho\), whereas the cosine kernel
sees only its even part. The manuscript uses the exponential kernel and
makes this choice explicit; it is not a claim that this kernel is optimal.

## Reconciling integrand and integral preservation

The latest discussion distinguishes
\[
\rho_s=\rho
\ \Longrightarrow\
\mathcal T\rho_s=\mathcal T\rho
\ \Longrightarrow\
\int\rho_s\,dX=\int\rho\,dX.
\]
Keeping the kernel fixed defines a single observation map. Requiring
constant output for every \(z\) is a further condition, not part of
merely having a well-defined transform. Total mass fixes only \(H(t,0)\).

For the chosen exponential kernel, Fourier uniqueness turns preservation
of every observation into
\[
g_{\rho_s}=q_t/2,\qquad \overline{\rho_s}(t;r)=\rho(t;r).
\]
Thus the full three-dimensional integrand may change, but after angular
integration the one-dimensional integrand is fixed. This recovers the
radial content of the earlier pointwise-preservation intuition without
requiring the spatial density itself to remain radial.

All allowed densities can be written, for \(r>0\), as
\(\rho_s(t;r\omega)=\rho(t;r)A_s(t;r,\omega)\) with spherical mean
\(A_s=1\). Positive densities require \(A_s\ge0\); signed densities need
the stated absolute exponential moments. Radial members are fixed.
Nonradial changes and couplings across radii remain possible, subject to
the fixed average on each sphere. This characterizes representations; it
does not specify a flow.

## The exponential choice confirmed

Edward Baker asked how the chosen kernel relates to the original
cosine formula, then explicitly preferred retaining the exponential
kernel. We keep it as the primary observation. It makes the spectral
variable Fourier-conjugate to the source label; cosine is recovered
from the initial evenness.

Had we retained only the cosine observation on the reflected whole space,
the condition would instead be
\(g_{\rho_s}(u)+g_{\rho_s}(-u)=q_t(u)\).
Redistribution between reciprocal radii would then be possible in addition
to angular changes. The exponential kernel also retains the odd part of
the marginal, making the stronger constraint an intentional choice.
This distinction is already explicit in manuscript Section 4.3.

Subsequent clarification in this chat: the exponential kernel remains a
working preference, not a finalized choice. The
[next continuation](07_NATURAL_AUXILIARY_EVOLUTION_CONTINUATION_20261028.md)
will brainstorm the kernel together with the auxiliary evolution, while
retaining spectral-independent density and an s-independent kernel.

## Status and relation to the earlier strategy

The earlier conservative heat construction evolves a spectral-dependent
integrand separately for each observation. Its conservation of an
unweighted integral should not be silently transferred to a single
spectral-independent density with fixed kernel. The new setup identifies
the compatibility condition a future construction must satisfy.

A collision remains simultaneous cancellation of the observations
\(H\) and \(H_z\); it does not assert a local zero of \(\rho\).
No new collision-exclusion criterion, canonical estimate, or numerical
flow experiment is introduced, and the existing B02 estimate remains open.

The [result index](../../../../result-summaries/README.md), especially
[geometric realizations](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md),
and [pattern index](../../../../avoid/README.md), especially
[re-realizations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
supply the scope: these are exact setup identities, not a sign theorem.
See the [same-assistant assessment](../reviews/20_BOOK_TRANSFORM_SETUP_ASSESSMENT_20261028.md)
and [build record](../numerics/18_BOOK_TRANSFORM_SETUP_BUILD_RECORD_20261028.json).
