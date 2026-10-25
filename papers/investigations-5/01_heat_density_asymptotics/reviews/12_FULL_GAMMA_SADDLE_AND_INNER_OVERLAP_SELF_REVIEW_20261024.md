# Full gamma saddle and inner overlap: same-assistant review

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from chat 0007's session metadata.

This is the same assistant that derived and wrote [Note 30][note]. It is
not a distinct-reviewer or specialist assessment and does not complete
HDA-20. No numerical, machine-symbolic or exact-arithmetic execution was
performed. The checks below are analytical rereadings of the proof.

**Disposition:** retain the result as **proved in-note; same-assistant
review only**. The full gamma saddle supplies a static all-height
positive endpoint and actual overlap with the inner approximation. The
positive evolution/covariance and finite-transition obligations remain
unfinished. HDA-19/HDA-16 stay Partial and HDA-18 stays Gated.

## 1. Model, source and branch

The model uses the exact factor `M(w)=w(w-1)pi^(-w/2)Gamma(w/2)/16`.
It replaces Note 28's linear exponential by the full implicit saddle
`p=w+t alpha(p)/2`, and includes `B^(-1/2)`, where
`B=1-t alpha'(p)/2`. This is not Polymath's Stirling M_0 or the inner
source mass M_0. All three remain distinct in the note.

The existence claim specifies the large branch rather than assuming
uniqueness among every solution of a meromorphic equation. In its
rectangle, Re p is of order t log R, |p| is comparable to
`N=1+X+t log R`, and the fixed-point derivative is O(1/log R).
The map sends the rectangle into itself and is a strict contraction
after an eventual onset. The nonnegative imaginary increment requires
a check near the real axis; FS9's proof supplies it by integrating
Re alpha' when Im p<=Re p, then using the leading argument when
Im p>=Re p. Negative imaginary parts follow by conjugation.

The branch extends holomorphically in w by uniqueness and B!=0.
The derivative estimates use a fixed sector margin, not a sector that
approaches the negative real axis. M is zero-free in Re p>1 and B stays
near 1, so the logarithms and square root used for phase are legitimate.
The theorem covers a buffered strip, without claiming a global entire
saddle model at all parameters.

## 2. Contour accounting and the decisive error

The exact xi convolution is valid for every positive t. Splitting it
at real parts 2 and -1 and reflecting the left arm produces two gamma
times ordinary-zeta integrals and a bounded middle. No approximate
reflection is used.

Each arm is shifted vertically by Im(p-w). Both connectors remain in
the formula. All deformed arms and connectors satisfy Re(w+v)>=2,
so they cross no gamma singularity or zeta pole. The finite right face
vanishes before the infinite-ray formula is asserted. This fixes the
analyticity issue that would arise from shifting isolated meromorphic
factors through unspecified regions.

The central cancellation is exact:
`exp(-(v_*+u)^2/t) M(p+u) / [exp(-v_*^2/t) M(p)]`
equals `exp(-B u^2/t+E_p(u))`. The first-order term vanishes by the
saddle equation, and the full quadratic term enters B. On u>=-a/2,
the bounds `|E_p(u)|<=C|u|^3/|p|^2` and a separate real Gaussian
majorant hold, including arbitrarily large positive u. The proof does
not require the cubic remainder to be uniformly small on that whole
half-line: `|e^E-1|<=|E|max(1,e^(Re E))`, together with bounds for
both complete exponents, makes its integral a third Gaussian moment.
That moment divided by sqrt(t) is O(t^(3/2)), giving the stated
`t^(3/2)/N^2` field error.

For the leftover horizontal segment, integrating the logarithmic
derivative loses at most C Re p. Its Gaussian separation costs
`a^2/t asymp t log^2 R`, which dominates that loss uniformly. The
connector costs at most exp(Ct) more and has the same negligible bound.
The bounded middle is compared to M(2+i tau), which never vanishes;
compact bounded-height behavior is included. Thus no large-height
Stirling formula is being used at tau=0.

The arithmetic estimate includes every Dirichlet mode through
`|zeta-1|<=3*2^(-Re w)`. Its tilted Gaussian integral gives
`R^(-t log(2)/8)`. With t>=32 this is smaller than the principal error
after an eventual onset. The polynomial middle factor times
exp(-c t log^2 R) is also smaller. These facts justify FS20's
simplification to FS7; the separate payments remain visible.

## 3. Collars and the physical regulator

The phase derivative is positive and of order log R; its spatial
variation is O(1/N), and the analytic carrier's logarithmic derivative
is bounded after cancellation of the two large real logarithms.
The complete field estimate therefore supplies the same physical
simple-root collars and zero-free unit bounds required by Note 28's
arbitrary-positive-q lemma. A small absolute field error alone would
not have sufficed. Kernel-edge collars and their full disks are included
in the fixed buffer.

The L1 potential/weight comparison gives the static spatial jets through
order four. It preserves the physical additive potential normalization.
The density comparison then uses both adaptive curvature terms in the
weak identity. The bounded-beta-X regime can use that identity directly;
the complementary regime must pay regularization versus zero measure.

The large-time regulator step needed a new argument. The old separate
bound `log E_0=O(t log^2 t)` is too large at intermediate heights.
FS26 instead uses the independently proved field estimate at zero and
Note 12's complete-source mass estimate to show `A_0 asymp M_0`.
This is noncircular: the field proof precedes the density proof and
does not use q or the mass anchor. The formula for P_* contains no
measured or fitted mass. The global bound on the logarithmic amplitude
derivative then pays motion from zero to X.

For beta X larger than a sufficiently large fixed B_0, the regulator
quadratic exponent beats the linear-in-X amplitude loss. The compact
time remainder is handled separately, including the flat regulator
switch. The bias is exponentially small in X; in that regime t<=C(1+X),
so it is legitimately absorbed into the principal field rate. This
does not assert a divisor interpretation for an unresolved regulator.

## 4. Quantifiers, overlap and normalization

The theorem is for t>=32 and sufficiently large t+|x|, with constants
independent of both variables and fixed spatial widths/transverse strip.
It implies an outer threshold independent of t, and an all-real-height
theorem at sufficiently large t. The uniform height and time errors
in FS29--FS30 follow from the displayed denominator; compact-time error
is O_T(X^-2). The onsets exist but have no numerical value here.

At late time the global regulator equals Note 19's inner regulator.
The two estimates therefore apply to exactly the same unnormalized
averaged density on its buffered growing window. Their triangle
inequality proves FS31. This pays actual static overlap without equating
individual asymptotic terms or using a coarse phase location as an exact
one. The inner source/collar gates remain explicit and eventual.

The previous exponential outer threshold and lack of overlap remain
accurate descriptions of Note 28's model/proof. They are superseded as
the current HDA-19 starting point by a different model. No universal
failure of the older representation was proved or is now claimed.

## 5. Residual and limits

I rederived the implicit derivatives used for the heat residual. With
alpha evaluated at p,
`p_w=1/B`, `p_t=alpha/(2B)`, and
`D=alpha+t alpha''/(4B^2)`.
The derivative of D has the three terms in FS21, including
`t^2(alpha'')^2/(4B^4)`. In
`partial_t log S-(D^2+D')/4`, the alpha^2, alpha'/B and
t alpha alpha'' terms cancel. The remaining coefficients are
`-t alpha'''/(16B^3)` and `-5t^2(alpha'')^2/(64B^4)`.
Both compositions with (1 +/- iz)/2 contribute -1/4 to the second
z derivative. This verifies the sign and the 5/64 coefficient in FS33.

The bound is O(t/N^3) relative to the carrier sum. It is not zero and
does not by itself propagate an observable error. The static estimate
has not been differentiated; positive current/time, source forcing,
potential-time, actual Q and Delta Q estimates remain open. The new
model still retains a spatial average and an implicit special-function
saddle, rather than a fixed finite elementary density formula.

The complete xi/reflection/ordinary-arithmetic premises distinguish this
canonical application from each control family listed in Note 30.
The local collar lemma itself can hold on simple-root subdomains of a
control and is not an exclusion principle. There is no RH, early-time
global simplicity, novelty or independent-validation claim.

**Next: Analytical — Astra.** Establish the positive all-height
time/current/potential-time comparison, then actual covariance and its
Laplacian, using the complete shifted source and the retained residual.
These are the missing HDA-16 obligations before full matching and
HDA-18 assembly. No numerical packet has been issued.

[note]: ../notes/30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md
