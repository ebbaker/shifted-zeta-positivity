# Self duality and additional symmetry questions

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; actual reasoning
effort: **max**, verified from the authoring turn metadata.

The next research program can investigate one accepted question about known
theta self-duality and three additional symmetry mechanisms. The identities
and asymptotic starting points below are established in the cited sources;
the proposed improvements to signed estimates, cost, or exclusion regions
remain open. No new collision exclusion or Newman bound is asserted.
The [continuation context](02_SYMMETRY_PROGRAM_CONTINUATION_CONTEXT_20261018.md)
records the manuscript state and a suggested first task.

Read the repository [result summaries][summaries] and [patterns to avoid][avoid],
especially the [control comparison][controls], [theta bookkeeping][theta],
[reformulation warning][reformulation], and [limits of separate bounds][separate].
An identity identifying theta is not itself a quantitative estimate for theta.

## The accepted question about known self duality

**Does this known self-duality yield a new quantitative estimate for the
retained oscillatory arithmetic sum?**

The reflection under discussion is the classical modular identity

\[
\Theta(y)=\sum_{n\in\mathbb Z}e^{-\pi n^2y}
=y^{-1/2}\Theta(1/y),\qquad y>0.
\]

With the manuscript's coordinate and normalization,

\[
P(u)=e^u\Theta(e^{4u}),\qquad P(-u)=P(u),\qquad
\Phi(u)=\frac{P''(u)-P(u)}{16}=\Phi(-u).
\]

The [source identities][source] and [rigidity proof][rigidity] already
characterize this law. For even real coefficients of at most polynomial
growth, full modular reflection of
\(\Theta_a(y)=\sum_{n\in\mathbb Z}a_ne^{-\pi n^2y}\) forces
\(a_n=a_0\). Normalization \(a_0=1\) gives the ordinary theta coefficients.
Within this class, evenness of the analytic arithmetic source and the
primitive endpoint \(\psi_a'(0)=-a_0/2\) recover the full law. Arbitrarily
extending a half-line source evenly does not impose that arithmetic identity.

The law cancels all inverse-power endpoint contributions in the complete
source transform, as proved in the [modular cancellation section][cancellation].
It leaves the oscillatory arithmetic sum carrying the zero information.
Neither coefficient rigidity nor endpoint cancellation gives a lower bound
on \(E=H^2+H_x^2\).

The earlier statement that “the controls fail the full reflection law” must
retain its scope: the finite-prime-compatible square-series controls fail
full reflection, while reflected smooth controls retain reflection and fail
the normalized integer-square expansion. Together, full reflection and that
arithmetic expansion select theta. No additional undiscovered exact
reflection, or dramatic simplification from one, has been established.

## Reflection within a moving cutoff interval

For the heat Riemann–Siegel correction, put

\[
a=\sqrt{\frac{x}{4\pi}+\frac{t}{16}},\qquad
N=\lfloor a\rfloor,\qquad p=1-2(a-N).
\]

The published leading profile is

\[
C_0(p)=
\frac{\exp\!\left(\pi i(p^2/2+3/8)\right)
-i\sqrt2\cos(\pi p/2)}{2\cos(\pi p)},
\qquad C_0(-p)=C_0(p),
\]

with removable singularities at \(p=\pm1/2\). Dividing the remainder
\(R_{t,N}(\sigma+iT)\) by the explicit nonzero multiplier in Proposition
6.3 gives \(\widehat R=C_0(p)+O_{\leq}(\widetilde\varepsilon)\), where

\[
\widetilde\varepsilon=
\left(\frac{0.397\,9^\sigma}{a-0.865}+\frac{5}{3(T-6)}\right)
\exp\!\left(\frac{3.49}{T-4}\right),
\quad a=\sqrt{\frac{T+\pi t/8}{2\pi}}.
\]

This holds for \(0\le\sigma\le1\), \(T\ge100\), and \(0<t\le1/2\);
on the real spectral axis \(T=x/2\). Thus the normalized remainder has
an even leading profile with error \(O(a^{-1})\).
[Polymath, §6.2, equation (53) and Proposition 6.3](https://arxiv.org/html/1904.12438v2#S6.SS2).

The transformation to investigate is
\(a\mapsto2N+1-a\) within an open interval \((N,N+1)\): it sends
\(p\mapsto-p\). Its exactly preserved quantity is \(C_0\), and its
approximate counterpart is the remainder after the published normalization.
The amplitude, phase, and spectral height change under this transformation;
it is not a reflection of the complete \(H_t\).

**Proposed quantitative use.** Retain the signed correction while combining
it with modes near the cutoff, before applying error bounds. The current
[exterior contract][outer], particularly `eq:rs-eta`, instead includes the
correction in the absolute error \(E_m^C\). The question is whether a
combined treatment yields a smaller uniform error, fewer retained terms,
or a stronger certified margin on an explicitly chosen domain.

The published value estimate does not by itself pay for differentiated
errors. A usable first-jet estimate must control the value and first
derivative; a Laguerre estimate also needs the second derivative. Natural
cutoff crossings need a fixed-cutoff analytic representation or a proved
transition formula. Differentiating the floor-defined cutoff is invalid.
The local manuscript already shows how to pay for cutoff changes in a
holomorphic disk, though its current payment takes absolute values.

## Approximate rotation of the normalized first jet

Use the nonvanishing normalization \(\mathcal A_t\) and real phase
\(\vartheta_t\) defined by `eq:rs-normalization` in the
[exterior section][outer]. The leading pair has

\[
Q_t=H_t/\mathcal A_t\approx2\cos\vartheta_t,\qquad
J_t=\left(Q_t,-\frac{\partial_xQ_t}{\partial_x\vartheta_t}\right)
\approx2(\cos\vartheta_t,\sin\vartheta_t).
\]

Here \(\partial_x\vartheta_t\ne0\) is required. In the established exterior
regime the error and the phase derivative are controlled. The suggested
symmetry is translation in phase: advancing \(\vartheta_t\) by \(\Delta\)
approximately rotates \(J_t\) by angle \(\Delta\). A phase advance of
\(\pi\) approximately reverses both coordinates, and \(2\pi\) approximately
returns them. The leading model preserves radius two.

**Proposed quantitative use.** Investigate whether the actual arithmetic
contributions admit a rotation description with a controlled change of
radius on a useful region beyond the present leading-pair proof. A real
collision is precisely \(Q_t=\partial_xQ_t=0\), so the required gain is an
independently proved error or drift estimate keeping the jet away from the
origin on that region.

The [earlier collision manuscript][earlier], subsection “A conditional
amplitude and phase criterion” (`lem:phase`), already writes
\(F=2m\cos\phi\), with \(m=|P|\) and
\(\phi'=\vartheta'+\operatorname{Im}(P'/P)\), and gives an error-paid
exclusion criterion. It does not prove the required many-term amplitude
lower bound or phase-speed estimate. Rewriting that criterion as radial
nonvanishing is a reformulation; the proposed work is to prove a new
quantitative estimate for the genuine arithmetic phases.

A further existing obstruction matters here. In the same manuscript,
`sc:packet` proves that two genuine adjacent cutoff terms can nearly cancel
in the joint value/derivative vector, defeating a positive constant
packetwise bound by their separate diagonal energies. It does not rule out
larger groupings or a bound for the complete signed sum.

## Approximate scaling between time and logarithmic height

The natural combined parameter is

\[
\kappa=t\log\frac{x}{4\pi}.
\]

For the weights in `eq:rs-definitions` of the [current manuscript][outer],

\[
|w_{t,n}(x)|\approx
n^{-1/2-\kappa/4}\exp\!\left(\frac t4\log^2n\right).
\]

For each fixed \(n\) and fixed \(\kappa>0\), as \(t\downarrow0\) with
\(x=4\pi e^{\kappa/t}\), this tends to \(n^{-1/2-\kappa/4}\).
Changing \((t,x)\) while preserving \(\kappa\) therefore approximately
preserves the low-mode amplitude profile. It does not preserve the
rapidly changing arithmetic phases.

**Proposed quantitative use.** Seek a uniform scaling description of the
complete signed sum, including modes near the growing cutoff, to identify
where cutoff pairing or a first-jet estimate can remain effective.

The [earlier collision manuscript][earlier], proposition `prop:absmass`,
already proves the essential obstruction. With the natural cutoff \(N\),
uniformly for \(\kappa\) in compact subsets of \((0,4)\),

\[
\sum_{N/2\le n\le N}|w_{t,n}(x)|
=\left(2(1-2^{-1/2})+o(1)\right)
\exp\!\left(\frac{\kappa(4-\kappa)}{16t}\right).
\]

Consequently, the fixed-mode limit cannot be interchanged with summation
through the growing cutoff using a small absolute tail in that regime.
This excludes the specified leading-pair-plus-absolute-tail method, not
signed cancellation. The same source contains shrinking-time signed
reductions and edge cancellation; those are prior work to build upon.

## Controls and the meaning of a successful next step

The [control replay record][replay] preserves the fresh replay run during
this discussion. All five tested event boxes rejected the strict first-jet
and signed-margin acceptance tests. The separate Euler-factor witness at
\(p=41\), \(t=1/5\), \(x=168413/100000\) had
\(\mathcal L_0\approx-5.299994533574705\times10^{-6}\). That witness is
not a double-event enclosure. These checks validate the existing rejection
interface; they do not test or validate any proposed symmetry estimate.

| Control class | Premise missing from the complete theta application |
| --- | --- |
| Finite-prime orbit controls | Full normalized analytic reflection; finitely many prime identities and measurements still survive |
| Three-square and four-square controls | Full reflection and the unchanged complete coefficient sequence |
| Reflected super-Gaussian, smooth shape, and positive-primitive controls | The exact normalized theta integer-square source expansion; reflection alone survives |
| Euler-factor controls | The unchanged normalized theta coefficients and level; their negative-Laguerre witness screens claimed global signed bounds |
| The earlier counter-kernels and polynomial heat events | The exact theta arithmetic source; generic heat-flow or jet geometry survives |
| Smooth-density and two-channel controls | The evaluated complete theta source and its signed estimate; auxiliary positivity alone is shared |

The [control summary][controls] specifies which constructions have certified
event boxes and which remain analytic existence statements. In particular,
no effective event height is supplied for the finite-prime orbit theorem,
and no numerical event box is inferred for the smooth primitive control.
Control rejection is required on a domain containing the event, or for a
claim contradicted by the witness; a collision-free control box may pass a
valid local certificate.

The suggested order is **cutoff reflection first**, **first-jet rotation
second**, with **time–height scaling** organizing their regimes. The
self-duality question remains the common source-level question. Each attempt
should identify its transformation, preserved quantity, explicit defect
bound, and intended quantitative improvement. A smaller proved error,
measured cost improvement under matched error requirements, enlarged
certified region, or precise obstruction for a named method is a milestone.
A restated global nonvanishing condition is not one. Preserve the scope of
negative conclusions as required by [avoid 07][scope].

[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[reformulation]: ../../../../avoid/01_restating_the_target.md
[separate]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[source]: ../manuscript/positive_arithmetic_packets/sections/01_theta.tex
[rigidity]: ../manuscript/positive_arithmetic_packets/sections/05_controls.tex
[cancellation]: ../manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex
[outer]: ../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[earlier]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[replay]: ../numerics/SYMMETRY_BRAINSTORM_CONTROL_REPLAY_20261018.json
