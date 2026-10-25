# Gamma outer density: same-assistant analytical review

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this conversation's session metadata. The reviewer is the
same assistant that derived and wrote [Note 27][note]. This is neither
independent nor specialist review and does not complete HDA-20. No
numerical, machine-symbolic or interval execution was used. File/link
checks are housekeeping rather than validation of the mathematics.

**Disposition:** retain Note 27 as **proved in-note, same-assistant
review only**, with compact-time quantifiers. HDA-19 advances within
**Partial**: its static adaptive outer density is now controlled on every
fixed compact interval strictly above 64. Joint time/height uniformity,
inner overlap, instantiated onset and positive evolution/covariance
budgets remain open. HDA-18 remains gated; no Sol assignment is issued.

## 1. Normalization, source and published scope

The convolution has variance t/2 in the s-coordinate: averaging
`H(0,z-2iv)` with `exp(-v^2/t)/sqrt(pi t)` produces `exp(tu^2)` in
the complete source. This fixes the factor `t alpha^2/4`. The exact
completion is `M(w)=w(w-1) pi^(-w/2) Gamma(w/2)/16`, since the
canonical field is xi/8. Both the 1/16 and the s-coordinate's 1/2
are retained. There is no finite source cutoff or omitted mode prefix.

Polymath's equation (35) is explicitly for every t>0 and is a legitimate
input here. Its Theorem 1.5, stated for 0<t<=1/2, is not imported above
64. Note 27 proves the needed compact-time approximation from that exact
identity, the functional equation, the Dirichlet series and sectorial
Stirling estimates. Its exact gamma factor differs from the paper's
Stirling M_0 and from the positive inner saddle mass. There is no claim
of a new literature result about eventual high real zeros.

## 2. The three convolution regions and quantitative loss

On the right arm `Re(s+v)>=2`, zeta is 1 plus its entire arithmetic
tail. On the left, `xi(w)=xi(1-w)` and v -> -v give exactly the second
arm centered at 1-s, with the correct lower endpoint 1+sigma. The
middle interval has length 3. After reflection into real part [1/2,2],
Euler summation with N=ceil x gives a sufficient polynomial zeta bound.
The gamma exponential remains `exp(-pi x/8)` throughout this estimate.

The logarithmic gamma Taylor remainder is O(v^2/x) up to x^(1/3).
The Gaussian's tilted mean is O(t log x), so on a fixed I its second
moment pays O(log^2 x/x). This estimate retains the bounded
`exp(t (Im alpha)^2/4)` loss from taking absolute values. It would be
incorrect to drop that factor when t grows, or to divide by the possibly
zero pair P. The denominator in GO7 is the sum of the two amplitudes.

The positive far tail uses a global ray estimate for log|M(w+v)/M(w)|,
not bounded-real-part Stirling outside its range. The bound
`C v+(v/2)log(x+v)` is dominated by v^2/(2t_b) for all v>=x^(1/3)
after a contract-dependent onset. The gamma's height decay is thus kept
when comparing to the carrier. Both extensions of the linear Gaussian
are paid, including its lower-end missing tail.

The arithmetic factor 2^(-v) changes the real Gaussian tilt by -log 2.
Dividing Gaussian amplitudes gives the power `x^(-t_a log(2)/4)`.
For t_a>64 this is smaller than x^-1. The bounded middle and missing
lower tail have decay `exp(-t_a log^2(x/(4pi))/16+O_I(log x))` relative
to the carriers and are absorbed eventually. All constants are finite
and uniform for the declared compact I, but no numerical constants or
finite certified onset have been delivered. That limitation is explicit.

## 3. Root control is stronger than a pointwise field error

The product square root A is nonzero on the far-right strip and positive
on the real axis. Its logarithmic derivative is bounded because the two
leading logarithms cancel. The phase derivative is
`omega=(1/2) Re(alpha+(t/2)alpha alpha')`, with leading term
`(1/4)log(x/(4pi))`; its second spatial derivative is O(1/x) on a fixed
buffer. Cauchy estimates on larger sectors justify the gamma derivatives;
no derivative of an unqualified real-axis error is used.

Rouche circles have radius a fixed phase size divided by omega, not the
much smaller regulator scale. They first provide exactly one simple root
in each circle. Conjugation then makes that unique root real. The
identity `|cos(u+iv)|^2=cos^2 u+sinh^2 v` and the phase-coordinate
lower Lipschitz bound exclude other zeros in the support. An improved
root displacement O(delta/omega) follows within those circles.

The actual-root collars are disjoint and fit in the enlarged buffer.
The exterior field floor is c A_X, and the quotient reciprocal principle
gives the physical slope floor c A_X omega inside each collar. No actual
minimum or root separation was supplied by sampling. The proof uses the
whole complex buffer, including disks crossing the averaging support's
edge. This is the required extra work before transferring a shrinking
regulator; a small absolute field error alone would not suffice.

## 4. Adaptive weak bias, normalization and phase

The weak comparison uses the original physical density and q. Dividing
by A for the root argument never replaces q in that density. For
`r=2log E_0-beta u^2`, the retained derivatives are
`r_u=-2beta u`, `Delta r=-2beta`, so the weak-test constant grows as
O(1+X^2). There is no positive regulator floor over the height tail.

There are O(omega) simple collars, each of radius O(1/omega) and slope
O(A_X omega). Summing their logarithmic integrals gives the factor
`lambda_X^2[1+(1+log(1+C/lambda_X^2))/omega]`. The ratio lambda_X
compares the largest regulator on the full horizontal buffer to the
physical amplitude A_X. Its Gaussian decay absorbs the growing weak-test
constant and logarithm, yielding GO26. This payment is separate from
moving zeros to the frozen lattice.

The latter movement has size O((delta+1/X)/omega) per root and
O(omega) roots, yielding O(delta) absolute density error. Compact support
and global Lipschitz continuity of the averaging kernel pay entries and
exits at its endpoints. The finite Bernoulli identity is the exact
Note 19 periodization, evaluated at v=theta/omega and p=pi/omega.
Its phase shift has the same half-integer convention as the roots of
cos theta. The five endpoint coefficients follow from the degree-eight
kernel and retain its scale ell^(-m-1). No phase truncation is hidden.

Dropping that phase gives O(p^4), hence O((log X)^-4), absolute error.
The leading unnormalized density grows like `k_h(y) log X/(4pi)`;
there is no unit-mass rescaling. Evenness of the original field,
regulator and filters supplies the negative-height statement.

## 5. Uniformity and claims not paid

GO33 is a useful additional warning with a proof: Note 25 gives the
zero limiting ratio R/log X at and below 64, whereas Note 27 gives the
positive ratio k_h(y)/(4pi) above 64 for |y|<h. Each finite-height ratio
is continuous in time. Therefore that displayed limiting profile is not
approached uniformly on an interval crossing 64. This is a regulator
layer, not a discontinuity of the canonical heat flow and not a universal
obstruction to a time/height-dependent interpolating formula.

At the other end, the present compact-time constants are not uniform
as t_b tends to infinity. The real tilt, gamma curvature and absolute
Gaussian integration losses must be paid anew in a joint analysis.
No overlap with the inner |x|~kappa^(1/3) clock follows by placing the
two fixed-scope formulas next to one another.

The approximation P is not asserted to solve the heat equation. Static
density error cannot be differentiated to obtain current or time error.
Source-anchored potential and actual Q/Delta Q have not been compared in
this note. The full adaptive equations, forcing, curvature and current
source remain unchanged. The old cutoff obstruction and all prior
failed numerical evidence retain their exact scopes.

The collision-control table names the missing canonical completion,
reflection or full arithmetic premise for every listed family. It is a
premise audit, not a fresh numerical check or a global event exclusion.
The result class is an approximation milestone, not an RH reformulation.

**Next recommendation: Analytical — Astra.** Track the time-dependent
outer error and regulator layer, then obtain a justified route toward
inner/outer overlap. Those are analytical gaps; there is not yet a
bounded numerical question that would resolve them. An independent
specialist audit remains separately available under HDA-20.

[note]: ../notes/27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md
