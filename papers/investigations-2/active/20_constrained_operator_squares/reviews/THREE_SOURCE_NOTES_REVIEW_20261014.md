# Review of the three heat and operator source notes

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: gpt-6-astra (Codex), reasoning effort **ultra**.
This is an internal mathematical review, not independent specialist
validation or a literature novelty assessment.

All three documents are by Edward B. Baker III and bear the title
Notes on the continuum sigma limit. They explore different applications
of a shared resolvent/heat representation. Their exact seeds survive
separately from their incomplete operator implementations and approximations.
The documents themselves remain unchanged at the supplied locations;
the [source manifest](../SOURCE_DOCUMENTS.json) records their identities.

## Source map

| Supplied file | Document date | Pages | Main direction |
| --- | --- | --- | --- |
| [Continuum sigma](</Users/ebbaker/Library/Mobile Documents/com~apple~CloudDocs/Tex/Greens_Function_Integral/Notes/10-31-17/Continuum_sigma.pdf>) | 22 November 2017 | 9 | Heat-scale Coulomb splitting, smoothed density squares and an attempted conjugation implementation |
| [Heat Quantum](</Users/ebbaker/Library/Mobile Documents/com~apple~CloudDocs/Tex/Greens_Function_Integral/Heat_Quantum/Heat_Quantum.pdf>) | 28 February 2018 | 6 | Imaginary-time integral representation of a trial state and a proposed correlated-state approximation |
| [Dirac operator flow](</Users/ebbaker/Library/Mobile Documents/com~apple~CloudDocs/Tex/Greens_Function_Integral/Dirac_operator_flow/Dirac_operator_flow.pdf>) | 17 August 2018 | 15 | First-order Dirac kernels, spectral splitting and a proposed constrained operator square |

The 2017 date is taken from the document, not its directory name.
The common identity is -L^{-1}=integral_0^infinity exp(tL)dt on a
domain where the integral exists. Pointwise decay of a kernel alone is
not a sufficient abstract operator hypothesis: convergence, zero modes,
boundary behavior and exchanges of operators with integrals matter.

## The 2017 Coulomb construction

The sound central identity is the semigroup factorization on pages 3--4,
equations (23)--(25). Let

\[
 K_\tau(x)=(4\pi\tau)^{-3/2}e^{-|x|^2/(4\tau)},\qquad
 \rho_s=K_s*\rho.
\]

Then, on a finite-particle sector with the usual smeared-field
interpretation,

\[
 \iint K_\tau(x-y):\rho(x)\rho(y):\,dx\,dy
 =\int:\rho_{\tau/2}(x)^2:\,dx.
 \tag{1}
\]

It follows simply from K_{\tau/2}*K_{\tau/2}=K_\tau.
Using the Coulomb normalization of equation (18),

\[
 V_{ee}=2\pi e^2\int_0^\infty d\tau
          \int:\rho_{\tau/2}(x)^2:\,dx
       =4\pi e^2\int_0^\infty ds\int:\rho_s(x)^2:\,dx .
 \tag{2}
\]

Equation (46)'s coefficient pi e^2/2 does not match this normalization.
Normal ordering cannot be erased:

\[
 \int:\rho_s(x)^2:\,dx
 =\int\rho_s(x)^2\,dx-K_{2s}(0)N .
 \tag{3}
\]

For the fixed-N position representation, rho_s(x)=sum_i K_s(x-X_i).
The subtracted terms are exactly i=j; the remaining Gaussian pair terms
are nonnegative for the same-sign particles considered here. Thus this
particular normal-ordered operator is nonnegative, but it is not the
unsubtracted density norm. Splitting the two divergent small-s
integrals in (3) and forgetting their cancellation is invalid.

A positive heat cutoff gives a concrete regularization:

\[
 V_{ee}^{(a)}
 =e^2\sum_{i<j}
 \frac{\operatorname{erf}(|X_i-X_j|/(2\sqrt a))}
 {|X_i-X_j|},\qquad a>0 .
 \tag{4}
\]

This is obtained by integrating K_tau from a to infinity. It decreases
with a, tends to the Coulomb pair form as a decreases to zero, and tends
to zero as a increases without bound. These elementary facts provide a
well-defined scale decomposition; they do not establish novelty or a
new many-body approximation advantage.

### The conjugation argument needs replacement

A single invertible similarity preserves products. Heat smoothing does
not: for f=exp(ikx), g=exp(-ikx),

\[
 T_\tau(fg)=1,\qquad
 (T_\tau f)(T_\tau g)=e^{-2\tau k^2}.
 \tag{5}
\]

Thus one similarity cannot implement heat smoothing on the full algebra
of multiplication observables. The proposed spin-trace construction in
equations (30)--(33) also does not establish its claim. Even in the
favorable abstract Clifford model D^2=L, normalized spin trace gives
cosh(s sqrt(L)), not exp(s^2 L); for L<=0 this is wave-type cosine
evolution. Equation (33) misses the square root. Its operator-valued
inference after taking a trace requires an additional argument.

A corrected implementation uses a Gaussian average of translation
automorphisms alpha_y:

\[
 T_\tau(B)=(4\pi\tau)^{-d/2}
 \int_{\mathbb R^d}e^{-|y|^2/(4\tau)}\alpha_y(B)\,dy .
 \tag{6}
\]

For bounded observables this has the natural operator interpretation;
density fields should first be smeared. If alpha_y is conjugation by
the translation unitary, (6) produces heat-smoothed density. Smoothing
the two densities in (1) independently is essential. A common
translation leaves the already integrated translation-invariant pair
interaction unchanged.

For a selfadjoint Dirac operator, spectral calculus also gives

\[
 e^{-\tau D^2}
 =\frac1{\sqrt{4\pi\tau}}\int_{\mathbb R}
 e^{-s^2/(4\tau)}e^{isD}\,ds .
 \tag{7}
\]

Averaging the first-order propagators is different from selecting one
propagator. The failure of multiplicativity has an exact square defect
for scalar smooth functions:

\[
 T_\tau(f^2)-(T_\tau f)^2
 =2\int_0^\tau T_{\tau-s}
          (|\nabla T_sf|^2)\,ds .
 \tag{8}
\]

This follows by differentiating T_{\tau-s}((T_sf)^2).
It is an example of a useful positive square with its correct domain of
application. It supplies no stationary Laguerre sign for Newman time.

Additional corrections to retain when rebuilding the 2017 argument:
the positive scale increment is sigma_{i+1}-sigma_i;
the change sigma=2sqrt(tau) transforms the measure density
v(r,sigma)d sigma=K_tau(r)d tau;
equation (20) needs a minus sign with the definition in (19).
Equations (49), (56) and (57) use incompatible time factors.
The creation/annihilation commutators (53)--(54) have opposite signs:
a similarity that smooths one inverse-smooths the other, so it does not
smooth their product as asserted. Inverse heat operations need domain
control.

## The February 2018 quantum variant

Pages 3--4, equations (14)--(19), have a sound exact core. For
A=H+E_s I >= alpha I>0, u(t)=exp(-tA)rho and
Psi=integral_0^infinity u(t)dt,

\[
 \langle\Psi,A\Psi\rangle=2\int_0^\infty\|u(t)\|^2dt,\qquad
 \|\Psi\|^2=4\int_0^\infty t\|u(t)\|^2dt.
 \tag{9}
\]

The state obtained by integrating a path of Slater determinants need
not itself be one determinant. This is a legitimate way to define a
correlated trial family, but its approximation quality is not proved.
Section 4 is only a heading.

Page 5 identifies the important unresolved issue: replacing the exact
evolution by approximate dynamics need not preserve the variational
meaning of (9). The newly saved
[finite-time residual theorem](../notes/RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md)
addresses this exact issue algebraically. It adds both the evolution
defect and the terminal endpoint. The corrected quotient is the actual
Rayleigh quotient of the integrated state. A useful research result
would bound those corrections economically for a stated approximation.

A simple example explains why the correction matters. With A=aI and
approximate u(t)=exp(-bt)v, the uncorrected quotient is b, whereas the
true Rayleigh quotient is a. Choosing b<a violates the supposed upper
bound. Recovering a with the residual is a consistency check; useful
many-body performance remains to be demonstrated.

The variational equations (21)--(25) also need a careful treatment of
complex variations, real-valued functionals and endpoint domains when
used beyond this exact spectral core. No optimization algorithm is
validated by their formal appearance alone.

## The August 2018 Dirac variant

The operator factorization D^2=-Delta and the spectral splitting of
first-order kernels supply useful machinery. The notes correctly notice
that exp(sD) is not dissipative on both spectral halves. This first-order
flow differs from the square root of the heat semigroup.

The page 12 square completion is unfinished as an identity.
Normal-order/self-energy terms are needed when passing from a
density-linear field square to a pair interaction. Expanding the proposed
F=G_{1/2}+sqrt(nu)a produces number-changing cross terms rather than the
kinetic term appearing in the constrained functional.
The [relocated research note](../notes/DIRAC_SQUARES_AND_STATIONARY_LAGUERRE_ENERGY_20261014.md)
records the precise theta connection and these limitations.

## What the new project can aim to deliver

The common lesson is to preserve the term that the formal simplification
would discard: product defects in smoothing, residuals in approximate
dynamics, and oscillatory or stationary terms in the theta application.

The most immediately bounded quantum result is a computable residual
bound plus a small interacting-system comparison. The theta result would
require a genuinely source-specific constrained square or an improved
complete signed estimate. The stationary identity

\[
 \mathscr L_j(H;t,x_s(t))
 =\tfrac12\,d[\partial_x^jH(t,x_s(t))]^2/dt
\]

provides the right local energy target; it does not convert the forward
heat constructions above into a positivity proof for backward Newman
time.

The original notes therefore support concrete research questions even
though their applications were unfinished. Before choosing a manuscript,
compare the corrected constructions with the literature and demonstrate
one nontrivial theorem, useful bound, or computational advantage.
The project need not claim RH progress to justify a quantum-methods
result, and a quantum result would not by itself settle the theta sign.
