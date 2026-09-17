# Wilson lines: deformation flows for the shifted Weil family

17 September 2026. A new investigation, opened from a proposal of Edward
Baker's. Its object is a **flow**, not a value: deform a Wilson line, and ask
whether the differential equation its deformation obeys --- fixed by the
variation of the endpoints together with the non-Abelian Stokes theorem --- is
the differential equation the shifted Weil family already obeys, equation (1.7)
of the [shared background](../../background.pdf).

It exists because every candidate this program has tested so far was asked to
reproduce a *value*, and Section 6.5 of the
[inverse-bulk manuscript](../inverse-bulk-realization/manuscript.pdf) showed how
cheap values are: the states reachable by one magnetic insertion are every
function analytic past the unit circle. A flow is rigid --- a generator and an
initial condition determine it, and there is nothing left to tune --- so matching
one is a different kind of claim.

The [working manuscript](manuscript.pdf), *Deformation flows for the shifted Weil
family: the transfer as an all-pass filter*, version 0.3, collects the results in
a self-contained draft. It inputs no shared
background; it cites the background by equation number for the shifted family and
the two companion manuscripts for results quoted by number. Reviewed versions are
preserved in [drafts/](drafts/README.md). See the [build guide](BUILD.md).

**Nothing here is a construction. No source is built, no positivity is proved,
and nothing assumes the Riemann hypothesis.**

## The results

**The transfer is an all-pass filter.** $|K_\omega(i\tau)|=1$ for every real
$\tau$ and every $\omega$ --- exactly, unconditionally, by the functional
equation alone. Under RH it is inner in the right half-plane, with zeros at
$\omega+i\gamma_\rho$, so the transfer is unitary and causal and the
contraction defect is an exact boundary flux,
$\langle f,D_{\omega,L}f\rangle=\int_{L/2}^{\infty}|(V_\omega f)(x)|^2dx$:
Weil positivity on $I_L$ says the flow pushes mass out of the leading endpoint
and never pulls it in. The zeros are the filter's **resonances**: each
contributes a Lorentzian of width $\omega$ and mass $4\pi\omega$ to
$|K_\omega-1|^2$, and the Weil form is the total resonant response of the input.
The archimedean symbol is the filter's **group delay**, which is why the density
identity $b(\tau^2)+w_0=2\theta'(\tau)$ holds and why the contact is not a
separate ingredient. See the
[inner-function note](notes/INNER_FUNCTION_AND_RESONANCE_20260917.md).

**The contraction region has no boundary, and Problem 8.1 is answered.**
$L\mapsto\lVert V_{\omega,L}\rVert$ is nondecreasing with supremum
$\lVert V_\omega\rVert$, and that supremum is $1$ or $\infty$ with nothing
between: for each $\omega$, contraction at every $L$ is *equivalent* to $\xi$
having no zero at distance more than $\omega$ from the critical line. So under RH
the region is the whole quadrant, **the flow formulation does not escape the
criticality**, and the "critical path" in $(\omega,L)$ that the earlier
`papers/shifted-zeta` programme looked for does not exist. What the plane is good
for is the opposite: monotonicity means a single certified Rayleigh quotient above
one would *disprove* a zero-free strip, so it is a disproof instrument and nothing
else. See the [critical-path note](notes/CRITICAL_PATH_20260917.md).

**The generator boundary is an artifact, and $\kappa_L$ is a zero-placement
precision.** The earlier programme's $\kappa_L=\lVert X\rVert_{Q\to Q}$ is,
in the spectral form, the ratio of derivative samples to value samples of
$\widehat F$ at the Riemann zeros --- the inverse of the accuracy with which an
interval-supported function can put its own spectral zeros on them. That gives
$\kappa_L\sqrt{m_L}\approx\mathrm{const}$, which the three recorded horizons
confirm across twenty orders of magnitude ($0.0144$, $0.0077$, $0.0061$), and
hence a generator boundary $\omega_*(L)\asymp\sqrt{m_L}$ that collapses
superexponentially *even under RH*. It sits eleven orders of magnitude below the
scale at which anything is detectable at $L=\log7$, and the gap widens.

**The cumulative criterion is positive-realness.** On the critical line
$(1-K_\omega)/(1+K_\omega)=i\tan\Psi$ exactly, so the Cayley coordinate of the
earlier programme is a reactance and the contraction criterion is that the
transfer's impedance be a positive-real function. That is the Krein--Nevanlinna
circle, and it is a second independent reason to read the companion
investigation's top open item.

**The generator, written out.** The background defined $G_{\omega,L}$ by naming
its symbol; the manuscript gives the operator, its domain and its adjoint status,
and shows that the three factors of $\xi$ deliver the three terms of the target
exactly. The whole shift dependence is one scalar factor: the shifted form is the
central form with every off-diagonal kernel multiplied by $\cosh(\omega(x-y))$
and every prime atom by $\cosh(\omega\log n)$, the diagonal unchanged. The flow
identities of the background are therefore general --- they carry the whole Weil
form, not its archimedean part.

**The pole term is invisible on the imaginary axis.** Its symbol has identically
zero real part at $p=i\tau$, so a Fourier-multiplier reading of the generator
recovers the archimedean term and the prime delays and drops the contact and
poles entirely. They reach the form only through the right half-plane Laplace
realization.

**The shift flow is abelian.** Truncation to an interval is multiplicative on
causal kernels, so the transfers and their generators lie in one commutative
algebra and the path-ordered solution of the flow equation collapses to an
ordinary exponential. The non-Abelian Stokes theorem has nothing to act on along
$\omega$, and the missing non-commutativity has to be supplied transverse to it.
The inner-function note explains why in one word: an all-pass filter is a phase.

**The shift is an angle.** It acts on inputs by the hyperbolic rotation generated
by multiplication by $x$, so it is a geometric deformation and its
gauge-theoretic analogue is a cusp rather than a coupling that can be dialled.

**The endpoint direction is an endpoint equation, and it is flat.** The
$L$-derivative of the compressed transfer is rank one, at the leading end, with
the boundary value of the evolved field as its coefficient --- a fixed tail and a
moving head, and the point through which the defect flux passes. The resulting
two-parameter connection is flat because mixed partials commute, so there is no
curvature to extract; and it does not close on the form domain, since endpoint
evaluation is not form-bounded and the smoothing the shift supplies misses the
trace threshold at every admissible shift, by exactly the borderline.

**The primes are the atoms of the connection.** The generator's kernel is a
continuous part plus atoms at the prime periods $m\log p$ --- the L\'evy
decomposition the companion investigation's ninth selection rule requires, here a
property of the connection rather than of a prepared state. A flat connection
with punctures has monodromy, and that is the surviving place for a non-abelian
datum; it is currently one-dimensional exactly because those residues are
scalars.

**Conformal symmetry is aligned with the target, not in tension with it.** The
Weil form is exactly invariant under translations in $x$; with $x=\log r$ that is
dilation in $r$, and reflection is inversion, so its exact symmetry group is
precisely the residual conformal group of a ray with one end pinned at the
origin. The transformation that destroys the prime atoms, $r\mapsto r^\lambda$,
is not a Möbius map at all. Positivity is moreover invariant along a conformal
orbit, so the whole orbit of the target is an equally good target. See the
[conformal correction note](notes/CONFORMAL_CORRECTION_20260917.md).

**The object is a scattering matrix, and the operator class is an open Wilson
line.** Causality, unimodularity, resonances at $\omega+i\gamma_\rho$ and a phase
derivative equal to the density of states are the defining properties of a
one-channel $S$-matrix, and $K_\omega$ is a ratio --- a reflection coefficient.
A holonomy fails not on unitarity but on the group delay, which must grow like
$\log\tau$. An **open Wilson line**, a bilinear in matter fields joined by a
line rather than a character, is unbounded by construction and so satisfies
Condition 7.1 structurally; and a ray ending on a defect has the pinned tail and
moving head that the manuscript's rank-one endpoint variation describes.
Conformal compactification tames the spectral infinity (it is the Cayley
transform already in hand) and the length infinity (ray to semicircle), but not
the trace obstruction, and it costs the absolute scale the prime atoms fix. See
the [scattering note](notes/SCATTERING_AND_OPEN_WILSON_LINES_20260917.md).

**The margin is a frame bound, and the scale is the prime cutoff.** Under RH,
$\lambda_{\min}(Q_{0,L})$ is the lower frame bound of the Riemann zeros as a
sampling set for the Paley--Wiener space $PW_{L/2}$, whose generating function is
$\xi$ itself --- so the de Branges route and the margin question are the same
question. A counting argument then gives strict positivity a reason: the zeros
have superlinear density and a function of exponential type $L/2$ has a linear
zero budget, so no nonzero one can vanish on them. The budgets cross at
$\tau_c=2\pi e^L$ with maximal deficit $D(L)=2e^L-\frac74$ exactly, and since
$e^L$ is the prime cutoff, **the sampling crossover is the explicit-formula
balance**. The same note warns that the recorded margins are basis-dependent
upper bounds and cannot be fitted to a decay law. See the
[sampling note](notes/SAMPLING_AND_THE_DEFICIT_20260917.md).

## Reading map

| Document | Role |
|---|---|
| [Working manuscript](manuscript.pdf) | The consolidated results, self-contained, 18 pages. |
| [Dated drafts](drafts/README.md) | Complete buildable snapshots with hashes. |
| [Deformation flow and the shift](notes/DEFORMATION_FLOW_AND_THE_SHIFT_20260917.md) | The opening note, written before the manuscript; carries a status header saying which of its two claims the manuscript supersedes. |
| [Notes index](notes/README.md) | Navigation and status of each note. |
| [Checks and records](numerics/README.md) | One reproducible program and its scoped results. |
| [Reviews](reviews/README.md) | Dated assessments. None yet. |

## What is open

Manuscript 0.3 carries every result in the notes. The ranked pathway is in
Section 10 of the manuscript and in the
[continuation note](notes/CONTINUATION_20260917.md); in short:

1. **The group-delay test on a specific open Wilson line** --- the first test in
   this program that a gauge theory can fail, needing no arithmetic and no
   positivity.
2. **The lower frame bound of the zeros on $PW_{L/2}$** --- which is what "how
   the margin collapses" means, now that the margin has been identified.
   Recomputing the margins in a basis adapted to the deficit band is a
   prerequisite: the recorded values cannot test any law.
3. **Suzuki, arXiv:2301.00421, promoted from reading to machinery** --- the de
   Branges question and the frame-bound question coincide.
4. **Manuscript Problems 8.6 and 8.7**, which are the two forms of one question.
5. **The conformal congruence at the endpoint** --- positivity is invariant along
   a conformal orbit, so the semicircle form is an equally good target on a
   compact contour, but its Jacobian degenerates exactly where the trace
   obstruction lives.
6. **Whether the vanishing theorem generalizes** beyond the class of
   arXiv:1102.4948.

## Relation to the sibling investigations

This investigation inherits their constraints and must not re-derive them.

- [Inverse bulk realization](../inverse-bulk-realization/README.md) supplies the
  target, the rigidity of Corollary 2.2, the two-channel exclusion, and the
  [exclusion map](../inverse-bulk-realization/notes/EXCLUSION_MAP_20260917.md)
  with each scope clause made explicit. Two entries of that map govern the work
  here: no accumulated exclusion touches any actual gauge theory, and the
  exclusions that do exist are statements about *channel decompositions*, which
  a flow is not --- so they neither block this direction nor may be quoted as if
  they did.
- [Source selection rules](../source-selection-rules/README.md) supplies the nine
  necessary conditions a candidate must satisfy. Rule 2 (unboundedness) is what
  killed the Wilson-*loop* benchmark; rule 7 (criticality) is the decisive
  question for this direction and is not settled here; rule 9 (the jump
  structure) is realized on the connection by the manuscript's Section 6.4.
- The [gauge-transfer test](../inverse-bulk-realization/notes/GAUGE_TRANSFER_TEST.md)
  already rejected literal Wilson-loop winding as the prime repetition law, in a
  rigorously constructed two-dimensional Yang--Mills control. That exclusion is
  about winding, not about lines.
- The [bottleneck brainstorm](../../brainstorm/inverse-bulk-brainstorm/BOTTLENECK_AND_OPERATOR_SEARCH_20260916.md),
  Section 4B, is where lines were first distinguished from loops and where the
  criterion behind the distinction --- unbounded spectral variable --- was
  identified.

## Conventions

Research notes go in [`notes/`](notes/README.md) and reviews in
[`reviews/`](reviews/README.md), with the model named at the top of anything
written by a language model. Check programs go in
[`numerics/`](numerics/README.md): standard library only, JSON printed to
standard output, a preserved record under `numerics/records/`, and registration
in the `CHECKS` dictionary of `validation/drafts.py`. Snapshot before replacing a
manuscript version: `drafts.py save YYYY-MM-DD-vNN`. Keep every file under 1 MiB
and follow the repository's [large-file policy](../../../../LARGE_FILES.md).

## Reproduction

```sh
python3 numerics/check_causal_commutation.py
python3 validation/drafts.py check --replay
```

Related: the [program index](../../README.md) and the
[program overview](../../PROGRAM_OVERVIEW.md).
