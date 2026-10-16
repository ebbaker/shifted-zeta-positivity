# Explicit theta correction and stationary cell internal review

11 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort unavailable and not inferred.
Separate-agent internal LLM audit, not independent mathematical validation.

## Scope and verdict

Reviewed [Note 20](../notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md),
[the corrected checker](../numerics/check_theta_corrected_stationary_cell.py), and
[its retained record](../numerics/THETA_CORRECTED_STATIONARY_CELL_RECORD_20261011.json), the retained
`check_high_stationary_s1_cell.py` used for its finite-sum method, and the
primary [Polymath Corollary 6.4 and Proposition 6.6](https://arxiv.org/html/1904.12438v2#S6.SS3).

The analytic correction, holomorphic comparison, physical error coupling,
and claimed bounded stationary branch pass this audit. The published
approximation theorem remains an explicit imported mathematical input.
The old coarse disk bound is retained only for comparison and does not
enter the new certificate.

The staged source hash agrees with the record:

```text
4506be2bd91b89424d96315897922dbda2158041e359b23725306dd19bbaabee
```

## Analytic checks

Direct substitution into the prescribed Stirling formula reproduces the
correction sign, prefactor, heat exponent, and combination `u-v/tau`.
The correct parameter is `a=sqrt(tau/(2*pi))`, as implemented. The code's
stable `logpref` follows from

\[
 \Re m_0((1-ix)/2)=\tfrac78\log(1+x^2)-5\log2
 +\tfrac14\log\pi-\tfrac14-\tfrac x4\arctan x.
\]

The real-amplitude derivative bound `J` follows using
`tau'=1/2` and `p'=-1/(4*pi*a)`. The claimed bounds on `u,v,u',v'`
are conservative on the checked `|p-1|<=0.01` range. The comparison
cost includes its necessary factor two and its full tau ratio.

The normalizer factor `K` bounds the ratio of the published complex
normalizer to the symmetric holomorphic extension of the real amplitude.
The finite-sum error uses safe upper-half-disk bounds; conjugation supplies
the lower half. Cutoff constancy is checked on the enlarged disk.

The pointwise printed correction is not holomorphic. The proof correctly
replaces it by a local frozen exponential at each physical center and
pays the discrepancy. Thus `-C/A*(-pi/8)^j` is the comparison's jet,
not an unsupported differentiation of the printed correction. All
normalizer terms through the third derivative are included in the
Cauchy-error convolution.

## Numerical adaptation and record checks

The finite source method is unchanged from the retained checker: all
22,066 terms and moments through order eleven are regenerated at the
new center. The absolute twelfth moment pays Taylor remainders through
the third jet. Spatial transport now covers the entire interval from
offset zero to `58.571`; time transport covers the final rectangle.
The eight subcells have width `0.0005` and cover the rectangle without gaps.

A separate exact-rational check of the saved decimal endpoints verified
all eight physical signs, interval products, four whole-rectangle hulls,
candidate flags, candidate band, endpoint signs, and the reported quotient
enclosure. This is a record-consistency check, not a second complete
22,066-term replay.

The remainder has `eta < 3.135063e-7`. Its physical third-jet payment is
less than `0.015346692`, with the normalizer terms included. The record
gives `Hx/A < -2.76859` and `Hxxx/A > 97.46819` throughout. Therefore
the physical `Hxx` is strictly increasing; its opposite endpoint signs
give exactly one zero for every stated time. The only candidate subcell
is `x0+[58.5690,58.5695]`, where

\[
 H_xH_{xxx}/A^2<-270.41505.
\]

The positive quotient is computed only after the slope has been
separated from zero. Monotonicity of `Hxx/A` is neither needed nor claimed.

The final checker also eliminates the common leading amplitude using the
genuine stationary equation. Writing `K_j=f_j-c*kappa^j+delta_j`,
`kappa=-pi/8`, and `K_2=0` gives exactly

\[
 K_1=f_1-f_2/\kappa+\delta_1-\delta_2/\kappa,
 \qquad K_3=f_3-\kappa f_2+\delta_3-\kappa\delta_2.
\]

The code pays the first error with `error_2/(-kappa)`, using the full
positive interval for the denominator, and the second with the upper
absolute endpoint of kappa. A separate exact-rational recalculation
verified that both saved conditional intervals enclose these expressions,
including all source errors. On the genuine stationary set in the
candidate band it proves

\[
 -2.796432<K_1<-2.666693,\qquad
 97.585075<K_3<97.713396,\qquad K_1K_3<-260.229467.
\]

These broader intervals furnish a second sign certificate after the
leading amplitude is eliminated; they do not replace the sharper
whole-jet product bound above. The source and record hash were checked
again after this final addition.

## Scope retained

This is a source-specific improvement of the resolved stationary sign.
It does not establish bounded or Hölder stationary loss as the joint
first jet vanishes, provide a predecessor neighborhood outside the
rectangle, or enlarge collision-exclusion coverage. The old coarse
interface already separates the slope on this rectangle.

The derivation is patchwise: source-theorem range, fixed cutoff,
holomorphic normalizer, and the stated p range must accompany any reuse.
No extrapolation to other cutoff transitions or the full shrinking
sector is justified by this record.

## Analytic extension of the profile bounds

The all-phase analytic corollary also checks. On the rectangle
`|Re p|<=5/4`, `|Im p|<=1/4`, the only denominator zeros are the removable
ones at `p=+-1/2`. On its vertical edges `|2 cos(pi p)|>=sqrt(2)`;
on horizontal edges the lower bound `2 sinh(pi/4)` is larger. The numerator
has modulus below `exp(5*pi/16)+sqrt(2)*cosh(pi/8)<5`. Maximum modulus
therefore gives `|C0|<4` throughout. A Cauchy circle of radius `0.24`
around any real `|p|<=1.01` fits inside the rectangle and gives
`|C0'|<50/3<17`.

Consequently the general profile constants `(U,V,U1,V1)=(4,4,17,17)`
are justified for every natural phase on a stable-cutoff patch. The
same comparison proof then uses

\[
 J_{\rm all}=\frac3{\tau_-}+\frac1{\tau_-^2}
 +\frac{17+17/\tau_-}{4\pi a_-}.
\]

This analytic corollary requires no change to the numerical record,
which keeps its sharper local constants. It does not handle changes of
the integer cutoff or prove a uniform stationary-loss estimate.


## Retained notes and scope of validation

Note 20 includes the explicit source theorem, its fixed-center and analytic
normalizer conventions, the removable-point extension, physical derivative
constraints, the outward stationary certificate, and the remaining cutoff
and vanishing-energy obligations. The checker intentionally uses larger
normalizer-convolution errors and a larger slope majorant than the sharp
constant-center theorem; both are safe overpayments.

[Note 21](../notes/21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md)
is a separate exact-source formulation. Its four Hermite coefficients
follow by Gaussian integration by parts with the complete theta source;
the positive norm follows by Hermite Parseval. The source's decay justifies
absolute Fubini and square integrability. The stationary covariance
inequalities are identified as unproved reformulations. No numerical xi
quadrature or new sign claim is attributed to that note.

The principal 22,066-term outward replay passed after the final checker
changes. A second agent's independent scalar source ledger on a slightly
smaller rectangle and a radius near 1/L agrees in scale and constants;
that auxiliary diagnostic is not a dependency of the retained certificate.
Local links, source syntax, saved source hash, and file sizes were checked
before saving. The manuscript was not changed or recompiled for these
research-note additions.


The final integration audit checked both retained notes, including the
exact derivative cancellation used in the sharper global slope bound.
The opening asymptotic gain is restricted to radius-1/L shrinking-sector
disks. The cutoff identity `C0(p+2)+C0(p)=exp(i pi(p^2/2+p+3/8))`
was independently checked by cancellation of the two numerators; its
use is limited to a starting identity for future edge matching. No paid
cutoff-crossing estimate is claimed.
