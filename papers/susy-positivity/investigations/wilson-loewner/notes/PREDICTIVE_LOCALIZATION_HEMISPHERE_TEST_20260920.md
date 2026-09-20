# A predictive localization control: free hypermultiplet, hemisphere, and endpoint degree

Date: 20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided model identity).
Effort setting: not exposed in this session; not inferred.
Status: literature-based physical setup with new comparison calculations and
floating-point cross-checks. Not independently reviewed by a specialist.

## Result and scope

A specified, already localized free-hypermultiplet boundary problem predicts a
Gaussian hemisphere wavefunction. Its Fourier–Mellin transform is a **single
gamma function**. Thus a one-sided gamma factor can occur in a supersymmetric
boundary amplitude without prescribing an arithmetic tower of Gaussian modes.
The fully paired circle determinant instead gives a hyperbolic cosine. These
are different observables/stages of gluing, and their difference matters.

This calculation does **not** derive the complete arithmetic factor. With the
explicit comparison convention

\[
 s=\tfrac12-i\sigma=\frac{p+1/2}{2},\qquad p=\tfrac12-2i\sigma,
 \tag{1}
\]

the complete prime-free factor requires the boundary descendant
\(T=N(2N-1)\), where \(N=-x\partial_x\) and
\(x=4\pi r|Y|^2\). A neutral pair of elementary scalar endpoints gives only a
linear polynomial in the Mellin variable. Under (1), it cannot supply both
arithmetic cancellations. The required quadratic descendant exists in the
protected operator algebra, but choosing it to fit the target is not a
prediction of an open Wilson line.

The degree obstruction is explicitly **conditional on (1)**. Changing the
unproved affine dictionary can turn the required quadratic into a linear
polynomial. Therefore the next decisive task is to derive the physical
spectral-parameter dictionary and the observable together. Increasing the
number of numerically sampled modes will not decide this issue.

No cumulative-positivity estimate, new horizon, arithmetic Loewner driver, or
physical realization of the arithmetic transfer is established here.

## 1. Inputs and the selected physical problem

Local background: current `manuscript.tex`, `supplementary-information.tex`,
`sections/s_localization.tex`, `sections/03_free_kernel.tex`, the fixed-window
and endpoint sections, and
`notes/LOCALIZATION_AND_THE_POLE_CANCELLATION_20260920.md`.
The arithmetic anchor and cumulative-append results remain separate inputs;
this calculation does not alter their status.

We select one free three-dimensional N=4 hypermultiplet on a round hemisphere
\(HS^3\) of radius \(r\), with the Higgs-branch supersymmetric boundary
polarization of Dedushenko [G, §§4.2, 4.3.2]. There is no dynamical gauge field
in this free control. The corresponding mirror description is the
\(U(1)\), one-flavor Coulomb boundary state, not an assumed four-dimensional
Wilson realization.

An explicit charge in [G, (78)–(79), text after (107)] is

\[
 \mathcal Q^H=Q_1^++Q_2^-
 =\mathcal Q_1^{\ell+}+\mathcal Q_1^{r-}
   +\mathcal Q_2^{\ell-}+\mathcal Q_2^{r+}.
 \tag{2}
\]

The superscripts refer to the two sphere supersymmetry algebras used in that
reference. This is a conformal/spherical charge; the repository's obstruction
for a fixed Poincare charge does not exclude it. We do not assert that (2)
has already been embedded into the desired four-dimensional defect geometry.

The boundary polarization fixes
\(q_1|=Y,\ \widetilde q_2|=\bar Y\), with the fermionic and auxiliary
completion given by [G, (80)–(82)]. On its localization locus,
\(G=-iY/(2r)\), \(\bar G=i\bar Y/(2r)\), and the boundary fermions vanish.
In the free theory this means
\(\partial_\perp q_2|=-Y/(2r)\) and the conjugate condition. Replacing these
curvature-dependent conditions by naive zero Neumann data would change the
problem. We use this specified polarization and its established localized
state, rather than claim a fresh derivation of the full fluctuation complex.

Wang [W, §5.1] places a related one-dimensional hypermultiplet sector on the
boundary of the localized gauge theory and allows endpoint-matter bilocals.
His full normal-fluctuation determinant is left unevaluated [W, §4.4]. Nothing
below fills that gap or assumes it equals one.

## 2. Closed-circle control: what retaining both mode directions predicts

For the twisted free hypermultiplet on the sphere, put
\(u^a(\varphi)=(\cos(\varphi/2),\sin(\varphi/2))\) and form the polarized
fields \(q=u^aq_a\), \(\tilde q=u^a\tilde q_a\). The twist makes them
antiperiodic. At a fixed real mass/background \(\mu\), choose conventions

\[
 D_\mu=\partial_\varphi+\mu,\qquad
 S=\ell\int_0^{2\pi}\tilde qD_\mu q\,d\varphi,
 \qquad \ell=-4\pi r.
 \tag{3}
\]

These are the conventions of [D, (6.2)–(6.4)]. The mass is a physical
background parameter, not the coefficient of a Q-exact localizing term.
The latter coefficient cannot supply the arithmetic shift.

The mode weights are \(\mu+i(n+1/2)\), \(n\in\mathbb Z\). Pairing opposite
frequencies gives the convergent determinant ratio

\[
 \frac{Z_{\rm circ}(\mu)}{Z_{\rm circ}(0)}
 =\prod_{n=0}^{\infty}
 \frac{(n+1/2)^2}{(n+1/2)^2+\mu^2}
 =\frac1{\cosh\pi\mu},\qquad
 Z_{\rm circ}(\mu)=\frac1{2\cosh\pi\mu}.
 \tag{4}
\]

The absolute normalization in (4) uses the standard free-hyper sphere
normalization \(Z(0)=1/2\); the relative determinant is independently fixed.
There is no zero Fourier mode. This is not the same assertion as removing
the arithmetic tower's lowest boson.

The inverse of \(D_\mu\), before the factor \(1/\ell\), is

\[
 G_\mu(t)=\tfrac12(\operatorname{sgn}t+\tanh\pi\mu)e^{-\mu t},
 \qquad -2\pi<t<2\pi.
 \tag{5}
\]

It has unit jump at zero and antiperiodic boundary values. Its Fourier
integral is \(\int_0^{2\pi}G_\mu(t)e^{-i(n+1/2)t}dt
=(\mu+i(n+1/2))^{-1}\), so it retains both mode directions. Multiplying
by the inverse parallel transport \(e^{\mu t}\) removes the separation
dependence on each ordering sector. If only the gauge background is
transported and a separate flavor mass remains, a regular mass exponential
remains instead. A bulk Wilson curve with an enclosed-area contribution is
outside this boundary-arc calculation.

At zero mass the localization equations in [D, (5.73)] indeed have a
holomorphic and an antiholomorphic solution. The twisted field combines
both, and the physical integration cycle relates the tilded fields to their
conjugates [D, §§5.4.3–5.5]. Keeping only the holomorphic half of (4) would
change that cycle; holomorphy alone does not authorize dropping it.

For the direct real-mass test \(\mu=p\), the shifted determinant predicts

\[
 K^{\rm circ}_\omega(p)=
 \frac{\cosh\pi(p+\omega)}{\cosh\pi(p-\omega)}
 \longrightarrow e^{2\pi\omega}.
 \tag{6}
\]

The arithmetic symbol below instead tends to \((2\pi/p)^\omega\).
Taking the reciprocal of (6) still leaves a nonzero constant limit. Its
central logarithmic derivative is bounded, unlike the arithmetic logarithmic
growth. A nonzero affine real-mass identification and a fixed finite rational
factor do not fix this asymptotic mismatch. This statement does not cover an
arbitrary nonlinear parameter map or a different observable.

For completeness, the simple abelian Gaussian average also has an explicit
obstruction. For fixed \(t>0\), set
\(Z_t(m)=\int_{\mathbb R}e^{-ta^2}/[2\cosh\pi(a+m)]\,da\). Dominated
convergence, using the majorant \(e^{-ta^2-\pi a}\), gives

\[
 e^{\pi m}Z_t(m)\longrightarrow
 \sqrt{\pi/t}\,e^{\pi^2/(4t)},\qquad
 \frac{Z_t(m-\omega)}{Z_t(m+\omega)}\longrightarrow e^{2\pi\omega}.
 \tag{7}
\]

This is a statement about the specified reduced integral, not a substitute
for the unknown determinant in the coupled four-dimensional problem.

## 3. A boundary amplitude really does produce one gamma factor

Let \(\epsilon=(4\pi r)^{-1}\) and \(x=|Y|^2/\epsilon\). The empty
hemisphere predicts [G, (128)]

\[
 \Psi_0(Y,\bar Y)=\sqrt{4r}\,e^{-x},\qquad
 \int_{\mathbb C}d^2Y\,|\Psi_0|^2=\frac12.
 \tag{8}
\]

Use the Fourier–Mellin boundary transform of [G, (138)] with integer angular
label \(B\). Angular integration of the neutral vacuum enforces \(B=0\).
Writing \(s=1/2-i\sigma\), its radial part is simply

\[
 \widehat\Psi_0(\sigma,B)
 =\frac{\delta_{B,0}}{\sqrt{2\pi}}
   \int_0^\infty x^{s-1}e^{-x}dx
 =\frac{\delta_{B,0}}{\sqrt{2\pi}}\Gamma(s).
 \tag{9}
\]

The integral first holds for \(\Re s>0\), with meromorphic continuation.
Its poles \(s=0,-1,-2,\ldots\) are simple and one-sided. Neither their
multiplicity nor the gamma function was imposed using the arithmetic target.
This is a prediction of the chosen localized boundary problem, already
consistent with its mirror hemisphere amplitude [G, (135)]. It concerns a
wavefunction's analytic divisor, not a derived list of positive physical
Hamiltonian energies or a new computation of a one-loop mode complex.

There is no conflict with (4). On the real \(\sigma\) contour the vacuum
gluing density is

\[
 \frac{|\Gamma(1/2-i\sigma)|^2}{2\pi}
 =\frac1{2\cosh\pi\sigma},\qquad
 \int_{\mathbb R}\frac{d\sigma}{2\cosh\pi\sigma}=\frac12.
 \tag{10}
\]

In [G]'s Coulomb polarization this is written using the phase-valued measure
\(\mu_{\rm glue}=\Gamma(1/2+i\sigma)/\Gamma(1/2-i\sigma)\) and two
vacuum amplitudes. The equality of these functions does not identify the
circle mass with the spatial Laplace variable of the arithmetic problem.

## 4. Predicting the response to actual scalar insertions

The free boundary operator algebra acts on wavefunctions by

\[
 Q_L=Y,\qquad \widetilde Q_L=-\epsilon\partial_Y,
 \qquad [\widetilde Q_L,Q_L]=-\epsilon.
 \tag{11}
\]

The right action supplies the conjugate-coordinate version; [G, (125)–(126)]
fixes its ordering. For neutral radial states define
\(N=Q_L\widetilde Q_L/\epsilon=-x\partial_x\). Then

\[
 N e^{-x}=x e^{-x},\qquad
 (N-1)e^{-x}=(x-1)e^{-x},\qquad
 \mathcal M[Nf](s)=s\mathcal M[f](s).
 \tag{12}
\]

The last equation follows by integration by parts. Boundary terms vanish
for a polynomial times \(e^{-x}\) and \(\Re s>0\).
Consequently the ordered scalar pair, its opposite ordering, and the
symmetric ordering predict respectively

\[
 s\Gamma(s),\qquad (s-1)\Gamma(s),\qquad
 (s-1/2)\Gamma(s),
 \tag{13}
\]

up to fixed field-normalization constants. A pair at opposite poles giving
\(Y\bar Y\Psi_0\) gives the first of these. No parameter fit is used in
(12)–(13). Any neutral two-elementary-scalar insertion in this free sector,
including its constant contact mixing, lies in the span of
\(\Gamma(s)\) and \(s\Gamma(s)\). We exclude derivative/composite
endpoints, additional current insertions, interacting dressing, and
nonconstant boundary transport from this degree statement.

## 5. Comparison with the complete arithmetic target

For \(\Re p>1\), \(0\leq\omega\leq1/2\), the local prime-free transfer is

\[
 K^<_\omega(p)=\pi^\omega
 \frac{\Gamma((p+5/2-\omega)/2)}{\Gamma((p+5/2+\omega)/2)}
 \frac{p-1/2-\omega}{p-1/2+\omega}.
 \tag{14}
\]

The symbol (14) describes the kernel before the first integer delay. It is
not a claim that the full arithmetic transfer has this Laplace symbol beyond
the prime-free window. Its useful auxiliary amplitude is

\[
 F_{\rm ar}(p)=\pi^{-p/2}(p-1/2)\Gamma(p/2+5/4),\qquad
 K^<_\omega=F_{\rm ar}(p-\omega)/F_{\rm ar}(p+\omega).
 \tag{15}
\]

Under the **comparison assumption** (1), the vacuum gives the preliminary
pole ladder \(p=-1/2,-5/2,-9/2,\ldots\). The actual two-scalar descendant
\(N\Psi_0\) gives \(s\Gamma(s)=\Gamma(s+1)\), removing its lowest pole.
This reproduces the gamma part in (14) under the assumed map. It does not
give the remaining zero at \(p=1/2\), or the corresponding rational ratio.

The complete amplitude requires

\[
 T=N(2N-1),\qquad
 T e^{-x}=(2x^2-3x)e^{-x},\qquad
 \mathcal M[Te^{-x}](s)=s(2s-1)\Gamma(s)
 =(p-1/2)\Gamma(s+1).
 \tag{16}
\]

One root cancels the lowest gamma pole; the other supplies the required
arithmetic zero. In the neutral polynomial vacuum module and with (1) fixed,
this is the unique polynomial of minimal degree, up to scale. A linear
polynomial cannot vanish both at \(s=0\) and \(s=1/2\). Equality of the
shift ratios for an interval of \(\omega\) fixes the amplitude up to a
constant after the prescribed normalization has been included.

Equation (16) is an **inverse comparison**, not a physical selection rule.
It identifies a quartic/composite boundary insertion to test. It does not
show that the original open line contains it or that a new Grassmann mode
survives. In this algebra the same factor can arise from a bosonic composite;
the arithmetic Berezin representation does not uniquely identify its physics.

The dependence on the dictionary must not be hidden. If instead one declares
\(s=(p+5/2)/2\), the required factor becomes
\((2s-3)\Gamma(s)\), supplied algebraically by \((2x-3)e^{-x}\). Thus a
different unproved offset changes the required degree. Neither this offset
nor (1) has been derived from spatial radial evolution. Formula-fitting has
many solutions until that dictionary is fixed independently.

Three further gaps remain even for (16):

1. The transform in (9) is in the **magnitude of a boundary field**, not
   automatically in the radial coordinate of the defect cylinder. Its real
   contour maps under (1) to \(\Re p=1/2\). The right-half-plane values in
   (14) require analytic continuation. The shifts \(p\mapsto p\pm\omega\)
   become \(\sigma\mapsto\sigma\pm i\omega/2\), not real-mass shifts.
   In particular, polynomial degree in the boundary variable is not the
   spatial angular-momentum index in the earlier free covariance
   \(\sum_{\ell\geq0}e^{-(\ell+1/2)|u|}P_\ell(v)\). A matching pole
   ladder does not identify those two spectra.
2. The factor \(\pi^{-p/2}\) is external to (9). A Mellin-coordinate
   rescaling or finite counterterm can insert an exponential in \(p\), but
   choosing it to match \(\pi^\omega\) does not explain the repository's
   fixed local finite part. A normalization must come from the dictionary.
3. A meromorphic boundary amplitude does not yet define a causal response
   on arbitrary inputs. Complete output, the identity limit, the ordinary
   adjoint, and cumulative contraction remain separate requirements.

For example, with \(p=2\), \(\omega=0.1\), (14) is approximately
\(0.926537840004\). The single-pair gamma ratio including the external
\(\pi^\omega\) is \(1.058900388576\); its missing rational factor is
exactly \(7/8\). The real-mass circle ratio is approximately
\(1.874447321909\). These numbers illustrate different predictions, not
alternative positivity certificates.

## 6. An explicit adjoint check

Strip the common normalization from (8), so the radial gluing norm of the
free real-coordinate control is \(\int_0^\infty|f(x)|^2dx\). Mellin
Plancherel on \(s=1/2-i\sigma\) gives

\[
 \int_0^\infty|P(N)e^{-x}|^2dx
 =\int_{\mathbb R}\frac{|P(1/2-i\sigma)|^2}{2\cosh\pi\sigma}\,d\sigma.
 \tag{17}
\]

This is a concrete Hilbert-space identity for this control, not an
identification with the arithmetic storage metric. On the natural test
domain, integration by parts gives \(N^\dagger=1-N\). Thus the centered
generator \(N-1/2\) is skew-adjoint, and its Mellin eigenvalue is
\(-i\sigma\). Twisted multiplication/differentiation operators should not
silently be declared ordinary adjoints.

The exact norms and a deliberately wrong operation are:

| State | Correct squared norm | Reusing the vacuum gluing phase with the same analytic polynomial on both sides |
|---|---:|---:|
| \(e^{-x}\) | \(1/2\) | \(1/2\) |
| \(Ne^{-x}\) | \(1/4\) | \(0\) |
| \(Te^{-x}\) | \(3/4\) | \(1/2\) |

The wrong column integrates \(P(s)^2/[2\cosh\pi\sigma]\), rather than
\(|P(s)|^2/[2\cosh\pi\sigma]\). It is not a claimed formula from [G]. It
demonstrates why a vacuum identity involving a gluing phase cannot be
promoted unchanged to the ordinary norm of every inserted state. The correct
orientation/conjugation of the bra matters. The sign change in
\((2x^2-3x)e^{-x}\) is likewise not negative Hilbert-space norm.

The elementary moment evaluations use
\(\int x^n e^{-2x}dx=n!/2^{n+1}\) and
\(\int e^{it\sigma}\operatorname{sech}(\pi\sigma)d\sigma
=\operatorname{sech}(t/2)\). They require no numerical extrapolation.

## 7. Reproduction and next decision

From this investigation directory run:

```sh
python3 numerics/check_localization_hemisphere.py \
  --output /tmp/localization-hemisphere-replay.json
```

The script uses only the Python standard library. The small committed record
is `numerics/records/localization-hemisphere-checks-20260920.json`; its
provenance companion records hashes and the repository state. Independent
quadratures check the Green-function Fourier coefficients, the paired-mode
product with analytic tail inequalities, the Mellin moments, gamma reflection,
both adjoint columns, and the target comparison on twelve \((p,\omega)\)
pairs. Orders 24 and 40 per integration piece both pass. The largest recorded
gamma-reflection discrepancy is below \(6.7\times10^{-13}\), dominated by
the fixed lower integration cutoff; the transfer-ratio discrepancies are
below \(10^{-14}\). These floating-point records are diagnostics, not
rational interval certificates. The exact identities and the conditional
degree obstruction are the mathematical content.

The productive continuation is now **the physical dictionary and the actual
bilocal's boundary state**, before a larger determinant calculation. Start
from a definite conformal open-line geometry and the free boundary sector.
Determine whether its spatial dilation generator becomes the Mellin generator
used here, including weight, orientation and scale; then compute the endpoint
and any forced current/contact terms. If that does not yield (16) under a
derived map, state the obstruction without adding an insertion to fit it.

This gives the localization suggestion a test with consequences: the gamma
structure has a real boundary-localization antecedent, while the cancellations,
normalization and physical response remain hypotheses that can now be checked
separately. It supplies no extra arithmetic positivity, smoothing credit, or
averaging-variance credit. The cumulative-defect program remains the route to
the required positivity statement.

## Primary references

- [D] M. Dedushenko, S. Pufu and R. Yacoby, *A one-dimensional theory for
  Higgs branch operators*, arXiv:1610.00740v2, especially §§3–6,
  [full text](https://arxiv.org/html/1610.00740v2).
- [G] M. Dedushenko, *Gluing II: Boundary Localization and Gluing Formulas*,
  arXiv:1807.04278v3, especially §§4.2 and 4.3.2,
  [full text](https://arxiv.org/html/1807.04278v3). The Fourier–Mellin identity
  used here is explicit in §4.3.2; the separate proposed microscopic mirror-wall
  derivation in §4.3.3 is called conjectural by the author and is not assumed.
- [W] Y. Wang, *Taming Defects in N=4 SYM*, arXiv:2003.11016v3,
  especially §§4.4 and 5.1,
  [full text](https://arxiv.org/html/2003.11016v3).

LLM disclosure: this note, its comparisons, and the diagnostic script were
prepared with the model recorded above. The cited localization results are
external inputs; the new algebraic comparison and its scope need specialist
review before manuscript promotion. Historical notes and manuscript snapshots
were not changed.
