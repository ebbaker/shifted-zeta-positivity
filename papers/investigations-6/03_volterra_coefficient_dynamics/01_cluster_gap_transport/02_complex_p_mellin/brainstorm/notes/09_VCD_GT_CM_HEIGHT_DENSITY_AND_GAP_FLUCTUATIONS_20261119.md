# Height-dependent density and the fluctuating gap chain

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual recorded model and effort unavailable;
none is inferred. Status: **explanatory continuation and correction of
emphasis**. No new theorem, source evaluation, certificate, manuscript
milestone or task activation.

Edward's correction is adopted: the stationary uniform chain is only
an algebraic normalization control, not the appropriate primary picture
of the canonical zeros. The height-dependent reference and the actual
deviations from it must enter even the introductory discussion.
The current manuscript already develops that distinction in
[printed §15][canonical]; the previous explanation failed to foreground it.

Read-first routing: [result index][results], [avoid index][avoid],
[Cluster18][cluster], [Controls12][controls],
[classification01][classification], [premises02][premises],
[scope07][scope] and [normalization08][normalization].
The formulas below are existing manuscript results or elementary
changes of scale. The displayed numerical comparison is a rounded
readout of an existing certificate, not a new estimate.

## 1. The smooth density is a starting input

The manuscript normalizes \(H(0,x)=\xi((1+ix)/2)/8\), so a critical-line
zeta ordinate gamma corresponds to x=2 gamma. In this coordinate the
classical smooth counting main term is
\[
 \overline N(X)=\frac{X}{4\pi}
                  \left(\log\frac{X}{4\pi}-1\right),\qquad
 \nu(X)=\overline N'(X)=\frac1{4\pi}\log\frac{X}{4\pi},
 \qquad d_X=\nu(X)^{-1}.
\]
These source passages were checked in the [reading receipt][reading].
The density is the derivative of the smooth main term, not a derivative
of the discrete counting staircase or its error term.
Thus the mean spacing decreases like \(4\pi/\log X\).
The counting law concerns the full zero population; it does not itself
make all zeros real or prove a lower bound for each real gap.

For the positive-time canonical comparison, §15 uses the more precise
reference clock
\[
 G(X,t)=\overline N(X)+\frac{11}{8}
                         +\frac{t}{16}\log\frac{X}{4\pi},
 \qquad G(q_n(t),t)=n.
\]
Its local reference spacing is
\[
 d(X,t)=\frac1{G_X(X,t)}
       =\left[\frac1{4\pi}\log\frac{X}{4\pi}+\frac{t}{16X}\right]^{-1}.
\]
The clock constant 11/8 belongs to this phase-label convention; it
need not be identified with the smoothed counting constant.
The reference points q_n are globally nonuniform.

“Unfolding” means measuring positions using the smooth count G, or
measuring nearby distances in units of d. It removes the known mean
scale while retaining deviations of the actual points from the reference.
At t=0 it gives no assertion that these deviations or the normalized
individual gaps are uniformly small.

## 2. Density and local geometry enter M differently

Fix a reference height and a positive length d, held constant for
the following rescaling. For an adjacent real pair set
\[
 \delta_n=\frac{g_n}{d},\qquad \mu_n=d^2M_n .
\]
Writing the cumulative distances of [§4][lattice] in the same units
makes its all-gap formula
\[
 \mu_n=\sum_{m\ge1}
 \left[
 \frac1{\mathcal L_m(\mathcal L_m+\delta_n)}
 +\frac1{\mathcal R_m(\mathcal R_m+\delta_n)}
 \right],
 \quad
 \mathcal L_m=L_{n,m}/d,\quad\mathcal R_m=R_{n,m}/d .
\]
This is exact on the full real ordered chain. It does not set any
normalized neighboring gap to one. Far from the reference height,
the normalized gaps still reflect the varying global density.
If only a real block is known, retain the remaining complete complex
exterior rather than assigning it positive real-gap denominators.

The pair equation becomes
\[
 D_n'=2-\delta_n^2\mu_n.
\]
The height scale and the dimensionless local geometry now have distinct
roles. A density-scale value of M does not imply a density-scale target
gap, or that the two terms in this equation nearly cancel.

With \(\tau=(t-t_*)/d^2\), the exact rescaled gap equation is
\[
 \frac{d\delta_n}{d\tau}=\frac4{\delta_n}-2\delta_n\mu_n.
\]
This explains the characteristic mean-spacing-squared physical time
scale. It is a scale statement, not a prediction of a collision time.
For a much smaller isolated gap, its own squared size is a shorter scale.
If d is instead allowed to follow the center and time, extra terms are
required: for \(U=D/d(t)^2\),
\[
 U'=\frac{D'}{d^2}-2U\,\frac{d'}d.
\]
Unfolding is not a license to keep the original evolution unchanged.

M is nonlinear in the cumulative gap sums. Replacing each sum by its
mean before taking reciprocal products generally changes the quantity
being estimated. A slowly varying mean density, a short anomalous
configuration and a distant weighted tail must therefore be distinguished.

## 3. An existing canonical example, at its actual height

Use the inherited endpoint rows in
[Record16][source-record], re-read with no source computation. The
pair lies near x=14010.16. The reference d(X,t) above is about 1.791
at both displayed times. This use of d is a choice of units, not an
assertion that the asymptotic clock theorem has reached its onset there.

| Physical t | Pair gap g | g/d | d²M | D'=2-4DM |
| --- | ---: | ---: | ---: | ---: |
| 0 | 0.075397 | 0.04210 | 1.9554 | 1.99653 |
| 0.1 | 0.845546 | 0.47212 | 1.9366 | 1.56833 |

These are rounded floating-point readouts of the recorded interval data.
[Readout04][readout] preserves the input strings, source hash and
formulas; its [script][readout-script] does not produce outward enclosures.
The source certificate and its original scope are unchanged.

The background scale barely changes, the complete interaction changes
modestly, and the selected gap changes substantially. At t=0 the
environmental interaction is on the density scale, but the target
gap is only about 4.2% of the mean. Consequently its intrinsic term
dominates D': an order-one normalized environment does not compensate
for a very small squared target gap.

Crucially, M and its higher exterior moments exclude the two target
zeros. If those two approach one another while all other zeros stay
a fixed distance away, every fixed exterior moment can remain finite.
Their regularity through a merger does not prevent it. Higher orders
preferentially resolve nearby *exterior* zeros and distinguish an
isolated close pair from a crowded multi-zero cluster.

## 4. The actual head/tail and time distinctions in the manuscript

In §15's fixed slab \(I=[t_0,t_*]\), \(t_0>0\), sufficiently high
canonical zeros follow the nonuniform clock. The published localization
onset is exponential in 1/t. The manuscript passes from this input
to a controlled local head and a complete tail, rather than replacing
the entire divisor by a constant-spacing chain.

Specifically, with \(L=\log(X/(4\pi))\), radius \(R=1\) or \(L^2\),
and \(E_R=LX^{-c_*t_0}+R^2/X\), its clock-head/complete-tail lemma
gives, on the stated all-real simple slices,
\[
 d^2M=2+O\!\left(E_R+\frac1{RL}\right).
\]
The local comparison uses actual consecutive labels and a paid curvature
error for G. The far estimate includes every remaining occurrence,
including negative heights and the low-height region. Its unit-shell
counts retain logarithmic height dependence.

The constant 2 here is the leading value of an increasingly accurate
local comparison after rescaling, not a postulate of global uniformity.
It is justified in that regime by both the source localization and the
complete tail bound. The stronger source-jet argument below can handle
nonreal low zeros as well.

The dependency is important: the source localization already implies
g/d close to one, hence separation of the target, before this M estimate
is obtained. It is not a deduction of separation from mean density.
[Discussion10](10_VCD_GT_CM_SOURCE_LOCALIZATION_AND_DYNAMICAL_INFORMATION_20261119.md)
traces that input and distinguishes the general conditional barrier
from the current canonical acquisition, which extends no known coverage.

As \(t_0\downarrow0\), the available cutoff diverges and the localization
error no longer supplies the same small bound. The logarithmic counting
scale survives, but the stated individual-spacing control does not
extend by this argument. This is a limitation of these estimates,
not a theorem denying every possible time-zero exterior estimate.

Thus the existing high-positive-time comparison and the compact
Lehmer-pair certificate address different regimes. A favorable complete
control at one selected pair is not a global result; the high-region
asymptotic is not automatically a practical bound at that pair.

## 5. The nonvanishing factor in a canonical local model

There is a more relevant version of the factor discussion than the
elementary polynomial example. In its proved high positive-time regime,
§15 constructs an actual holomorphic residual in the local representation
\[
 H(t,q+w)=A_q e^{-\pi w/8}
   \left[2i\sin\!\left(\tfrac14\log(q/(4\pi))\,w\right)
                      +E_{n,t}(w)\right].
\]
The statement is local on a small spatial disk with controlled residual;
it is not a global sine model or a t=0 approximation asserted here.
The logarithmic frequency incorporates the height-dependent spacing.

The exponential factor has no zeros, yet its logarithmic slope contributes
\(-\pi/4\) to the physical root velocity \(H_{zz}/H_z\).
The manuscript pays residual derivatives and a denominator floor to prove
the corresponding velocity estimate. The leading velocity is shared by
neighboring high zeros and cancels in their difference. Gap motion depends
on the remaining variations. This is the canonical setting in which
zero-location information, common motion and relative motion separate.

## 6. Research implication and control screen

The useful question is whether the clock-based head/tail organization
and the coupled gap state can give sharper *complete* bounds in a
less regular regime, while retaining the errors in both normalized
gaps and environmental moments. An exact subtraction of a reference
interaction is bookkeeping until its remainder is controlled. A finite
quantitative success would improve a paid tube, region or cost at
the same source information; no such gain is claimed here.

The analytical screen from [Discussion06][screen] is retained:
finite changes to a divisor can preserve its leading counting density,
so density alone is not a canonical-source premise. Euler-factor controls
can retain the leading logarithmic density while changing lower-order
counting terms and the full source; no agreement with the exact reference
clock is asserted. Finite-prime controls fail unchanged full theta/source
identity despite their specified finite agreements.
Weighted-square/finite-source subclasses with
nonreal zeros fail the complete-real-chain premise. Quadratic/quartic
controls obey the local pair law and still reach D=0; they fail literal
theta identity. Static divisor surgery does not supply a canonical common
heat path. No new certificate replay or claim that the present estimates
distinguish every colliding control is made.

[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[cluster]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[normalization]: ../../../../../../../avoid/08_normalization_and_constant_slips.md
[canonical]: ../../manuscript/sections/13_canonical_time.tex
[lattice]: ../../manuscript/sections/14_coupled_lattice.tex
[reading]: ../references/02_HEIGHT_DENSITY_SOURCE_CHECK_20261119.md
[source-record]: ../../numerics/16_VCD_GT_CM_EXTENDED_SOURCE_CERTIFICATE_20261118.json
[readout]: ../numerics/04_HEIGHT_DENSITY_AND_PAIR_READOUT_20261119.json
[readout-script]: ../numerics/density_gap_readout_20261119.py
[screen]: 06_VCD_GT_CM_RESEARCH_POSITION_AND_PATHS_DISCUSSION_20261118.md
