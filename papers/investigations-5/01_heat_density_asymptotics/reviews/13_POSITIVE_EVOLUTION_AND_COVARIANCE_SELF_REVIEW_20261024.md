# Positive evolution and covariance: same-assistant review

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from chat 0007's session metadata.

This is the same assistant that derived [Note 31][note]. It is an
analytical rereading, not a distinct-reviewer or specialist audit and
does not fulfill HDA-20. No numerical, machine-symbolic or exact-arithmetic
execution was performed. The complete field proof in Note 30 remains
a shared dependency, with its own same-assistant Review 12.

**Disposition:** retain **proved in-note; same-assistant review only**.
The new result pays the positive all-height endpoint's current, time,
forcing/source and actual covariance terms with absolute error
`C t^(3/2) log^2(2+t+X)/(1+X+t log(2+t+X))^2 <= C/sqrt(t)`.
It also pays compact-time outer evolution across the regulator switch.
The exact model residual is included in the observable equations.
Finite-transition acceptance, all-time joining, numerical onsets and
distinct review remain unfinished.

## 1. Derivative and root input

PE9 applies Cauchy's formula to the holomorphic error on an entire disk
of radius comparable to `1/log(2+t+X)`. The carrier modulus changes by
a bounded factor on that disk. This justifies the powers of the logarithm;
it does not differentiate a real-axis big-O estimate. The fixed transverse
and horizontal buffers include the circles and every larger root disk.
The exterior floor is relative to the carrier sum, not just the real-axis
amplitude, so no transverse exponential factor is lost.

The model's root residue is bounded by the exact formula
`2 A_*'/A_*+Theta_*''/Theta_*'`. Comparing first and second derivatives
at the displaced H root uses a third-derivative estimate along the
displacement segment, producing `O(e omega)` rather than assuming the
root velocity inherits the position error. Pole subtraction leaves
analytic regular parts whose difference is `O(e omega^2)` by the
maximum principle.

The model does not solve heat exactly. PE11 keeps
`c'=P_zz/P_z-E/P_z`; omitting the second term would confuse its actual
zero velocity with the algebraic residue in the current formula. That
term is `O(d/omega)`. Root tracks are local in time and the proof never
differentiates the integer root population or an artificial boundary.

## 2. Uniformity when q is tiny

The new local lemma treats
`w^m(1-w)/(z-root)`, for m=0,1,2. On small disks around the two roots,
the integrable `1/|z-root|` bound gives an O(e) contribution in scaled
coordinates. On their complement, interpolation of the root and the
nonzero analytic unit costs `e/r^2+e/r`. Integration gives
`e(1+|log e|)`; the logarithm depends on the field displacement, not
on a regulator floor. Q(u) is held fixed pointwise in the interpolation,
so no unproved regularity bound on this arbitrary positive function
is used.

Restoring area supplies `1/omega` per pole integral and summing
O(omega) collars removes that factor. The residue difference contributes
`e omega`; the regular part contributes `e omega^2`. Since
`|log e|<=C mathcal L`, the final allowance `e mathcal L^2` covers
all three. The residual quotient has the smaller residue `d/omega`
and a regular part O(d), giving an L1 allowance Cd.

This is a simple-root theorem. It does not extend uniformly to multiple
zeros merely because q is positive. The required collars are proved
for the canonical source in Note 30; they are not inferred from the
general rational formulas or assumed globally at early times.

## 3. Regulator derivatives and tail payments

For late time, differentiation of the explicit source saddle gives
`r_t=2L^2-3 kappa'/kappa+x^2 kappa'/kappa^2` exactly. On
`X<=B0 kappa`, this is `O(mathcal L^2)` and the required spatial and
mixed coefficients are bounded. In the other region, Note 30's
mass-anchored estimate gives exponentially small regulator-to-carrier
ratio. The collar integrals of w and `w h_F` retain the pole's
O(lambda) term; an O(lambda^2) bound alone would be wrong.
Polynomial coefficient growth is absorbed only in this resolved region.

The compact-time extension needs extra work: bounded beta' alone would
leave `e beta' X^2` nonvanishing. Differentiating the specified flat
switch gives `|beta'|<=C_T beta(1+log_+^2(1/beta))`. When
`beta X<=B0`, this is `O_T(log^2 X/X)`, paying
`r_t=O_T(X log^2 X)`. It explains the weaker time-error rate
`O_T(log^2 X/X)` in PE44. The current and covariance do not require
r_t and retain `O_T(log^2 X/X^2)`. These compact-slab constants are
allowed to depend on T; they are not the constants of the late-time
uniform theorem.

## 4. Exact identities and signs

I rederived the three time identities PE22 from
`F_t=-F_zz+E`. The signs of the residual contributions are positive
for S_t and negative for w_t; multiplying w_t by `(1-2w)` gives
the displayed chi_t identity. This retains the w and chi correlations
needed when the exact weak density identity is differentiated.

The current identity is
`pi j=partial_bar V0+(partial_bar r)V1`. The sign of the regulator
term is positive: differentiating `(1-w)` first produces its negative,
which is moved to the other side. Written through `F_zz conjugate(F)/D`,
the identity is smooth at a zero; no point mass is dropped.
It also avoids division by F_z at the intervening stationary points.

The differentiated weak density formula PE26 includes all six groups:
S_t, w_t grad r, w grad r_t, w_t Delta r, w Delta r_t, and the two
terms from differentiating chi times `|grad r|^2`. The latter are
chi_t times the squared gradient and `2 chi grad r dot grad r_t`.
Both time and spatial curvature derivatives are therefore retained.

PE33's residual density variation has coefficient 2 in the numerator
variation and coefficient -4 in the denominator variation. Varying the
weak identity with delta q=0 yields PE34 with coefficients 2,-4,-2.
This bounds the actual residual correction at narrow peaks without
a pointwise reciprocal-regulator loss. The signed regulator source
is defined first by its original formula, then bounded using the exact
current identity; it is not defined from the comparison error.

The local fields F=z and F=z-a(t), with constant spatial q, check the
current/stress cancellation and the indispensable moving-field residual.
These are hand calculations in the note, not a numerical validation.

## 5. Actual covariance and kernel orders

PE28 follows from `square D/D=square S+S_x^2-S_y^2` for each field.
It is independent of any heat equation. Thus it estimates the signed
gradient-square integrand of the actual covariance; it does not choose
Q to repair an equation. Keeping that signed combination is essential:
separate positive gradient-square integrals can acquire logarithmic
dependence on a shrinking regulator.

The subtraction of the squared filtered gradients is separately paid.
The L1 first-gradient bound is O(mathcal L), using integrable simple
poles and the regulator split. The static potential-jet differences
are O(e), so product differences through two spatial derivatives cost
`O(e mathcal L)`, below the main allowance. Delta Q is therefore
estimated from the exact differentiated kernel pairing, not by
differentiating an error estimate for Q.

The chosen compact kernel has bounded weak derivatives through order
four. The strongest pairings use two derivatives for the density or
signed stress and two more for the reported spatial derivatives. No
fifth derivative or boundary delta is silently used. Boundary values of
U, its normal derivative and J inherit the full-buffer bounds.

## 6. Quantifiers, strengths and remaining work

The all-height endpoint is for t above one eventual threshold and a
fixed transverse strip. Its `O(t^-1/2)` error is absolute. It does not
resolve every small inner transport scale: the sharper inner theorem
remains necessary for an error `o(L/kappa)`. The differentiated overlap
with Note 19 is a valid triangle inequality with the same q, at the
coarser absolute rate; it does not create missing clock potential or
covariance observables.

The model equations keep their residual corrections, bounded by
`d<=1/(t^2 log^3(2+t))`. A small residual is not used as a stability
theorem. The field comparison and direct nonlinear estimates are the
reason the observables are close. Neither the eventual endpoint nor
the compact-time outer result supplies the finite-height transition
core or the derivative/covariance terms from a future splice.

HDA-16 and HDA-19 can be marked complete at these explicitly stated
comparison scopes, consistent with the earlier eventual-scope task
labels. This is not completion of HDA-18, numerical onset selection,
HDA-20, or the broader approximation program. The theorem remains
dependent on the same-assistant full-saddle proof. The source control
screen is explicit; the generic pole/stress identities may also hold
on simple-root subdomains of colliding control fields.

**Next: Analytical — Astra.** Derive the finite-core and joining error
contract for HDA-17/HDA-18, using these endpoint and outer comparisons.
That contract should identify the finite source/jet accuracy that the
global approximation actually consumes before any numerical request.

[note]: ../notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md
