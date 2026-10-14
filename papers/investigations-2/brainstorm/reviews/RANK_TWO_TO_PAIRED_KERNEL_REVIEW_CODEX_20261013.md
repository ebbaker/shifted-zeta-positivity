# Rank-two addition to paired kernels: completed identity and sector obstruction

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded configuration: `gpt-6-astra` (Codex), reasoning effort **ultra**,
verified from the parent conversation's current-turn configuration.
Parallel derivations, code review and replay are internal checks, not
independent specialist validation or formal verification.

**Decision.** The requested 09-to-06 calculation now has its complete
unequal-scale identity and a definite negative answer to the first
factorization candidate. The two lattice cosets cannot be treated as
independently positive Fourier channels. The same-parity coset fails for
both paired kernels, in the positive folded construction and also in a
different smooth, resummed construction. The complete kernels and their
conditional stationary signs remain open. Any continuation must retain
the cancellation between cosets and add an estimate for the physical sum.

This continues the [first research pass](PRIORITY_RESEARCH_FIRST_PASS_CODEX_20261013.md)
and executes the next identity task selected in the
[active-directions review](ACTIVE_DIRECTIONS_REVIEW_CODEX_20261013.md).
The derivations have their principal homes in the
[09 identity note](../../inactive/09_rank_two_theta_addition/notes/1_COMPLETE_TWO_COSET_REDUCTION_20261013.md)
and the [06 factorization note](../../active/06_paired_kernel_factorization/notes/1_FOLDED_PARITY_CUSP_AND_FACTORISATION_OBSTRUCTION_20261013.md).
The [checker and numerical guide](../../inactive/09_rank_two_theta_addition/numerics/README.md)
give reproduction instructions; the [source and execution record](../numerics/RANK_TWO_TO_PAIRED_KERNEL_EXECUTION_20261013.json)
pins this continuation.

## 1. The exact transfer now available

For independent positive scales `a,b`, use

\[
k=n+m,\qquad \ell=n-m,\qquad
an^2+bm^2=\frac{(a+b)(k^2+\ell^2)+2(a-b)k\ell}{4}.
\]

The image is exactly `(2Z)^2` together with `(2Z+1)^2`. The unequal-scale
mixed term survives. The genuine source insertion is
`P(z)=16z²−24z`, obtained by applying `D_u²−1` to `exp(u−z)` with
`z=pi n² exp(4u)`. Its constant term vanishes, so the original zero axes
are killed rather than silently discarded. The pair normalization is
`exp(p+q)/256` before modular inversion and `exp(−p−q)/512` in each
individual Poisson-transformed sector. The latter retains its signed
characteristic and the derivatives of the modular prefactor.

The classical comparison is Jacobi's [theta addition identity](https://dlmf.nist.gov/20.7.E14)
and the [modular inversion formulas](https://dlmf.nist.gov/21.5).
The unequal-scale insertion, physical projection and endpoint ledger
are derived locally in the 09 note. Equal-scale calibration is not used
as a substitute for that derivation.

After differentiating and then folding the complete source, let

\[
A(u)=\sum_{n\ge1,\,2\mid n}\phi_n(u),\qquad
B(u)=\sum_{n\ge1,\,2\nmid n}\phi_n(u),\qquad u\ge0.
\]

The two cosets become exactly

\[
F_0=A\otimes A+B\otimes B,\qquad
F_1=A\otimes B+B\otimes A.
\]

Thus an even-even transformed coset means **same parity** of the original
indices; it contains their odd-odd pairs as well as their even-even pairs.
Both physical kernels are retained:

\[
J_{j,t}(s)=\int_{\mathbb R}r^2(r^2-s^2)^j
m_t(s+r)m_t(s-r)\,dr,\qquad j=0,1.
\]

In particular the signed factor for `J_1` is not replaced by its absolute
value. The source-series, integration and cutoff bounds are explicit in
the 09 note. Folding a theta parent before differentiating creates
additional delta endpoints; the recorded construction differentiates
first and tracks the distinction.

## 2. Folded positive sectors: analytic obstruction and finite witness

Put `h=(log 2)/2`. The complete even subtotal satisfies

\[
A(u)=2^{-1/2}\Phi(u+h),\qquad
A'(0+)=-c<0,\qquad B'(0+)=c,
\]

where `c` is approximately `0.03949868261495417`; the 06 note gives an
explicit positive leading term and a tail bound. The even extensions
`A(|u|),B(|u|)` therefore have opposite cusps. Their sum is the smooth
genuine source.

Let `h_A,h_B` be their heated half Fourier transforms, so `H=h_A+h_B`,
and write `L_j(f)=(f^(j+1))²−f^(j) f^(j+2)`. The same-parity response is

\[
C_j(t,x)=\widehat J^{\rm same}_{j,t}(2x)
=L_j(h_A)+L_j(h_B).
\]

The complete half-line endpoint expansions prove

\[
C_0(t,x)=-4c^2x^{-6}+O_T(x^{-8}),\qquad
C_1(t,x)=-24c^2x^{-8}+O_T(x^{-10}),
\]

uniformly on each compact real time interval as `x` tends to positive
infinity. Thus both same-parity kernels fail positive definiteness at
every fixed time, including positive times. This analytic statement is
stronger than a diagnostic at a selected frequency; its frequency
threshold is not made effective by the expansion alone.

The outward checker supplies a concrete witness at `t=0,x=60`
(kernel Fourier frequency `120`). The following displayed intervals
are rounded **outward** from the retained 60-digit record:

| Response | Complete enclosure |
| --- | --- |
| Folded same-parity `J_0` | `[-2.53642e-14, -2.50907e-14]` |
| Folded same-parity `J_1` | `[-1.08815e-16, -1.07228e-16]` |

The computation uses 1,024 Simpson panels on `[0,1]`, exact source
derivative polynomials, directed arithmetic and explicit trigonometric
remainders. It pays every omitted theta index `n>=4`, the entire source
tail `u>=1`, and the fourth-derivative quadrature error. It is a negative
**Fourier** witness; a negative pointwise value of `J_1` would not prove
failure of positive definiteness.

There is also a matrix obstruction. The leading polarized two-source
response is a negative multiple of
`[[1,-1],[-1,1]]`. Its contrast direction is negative and its physical
sum direction annihilates that term. No invertible constant real change
of the two source coordinates makes this entire response matrix positive
semidefinite. This leaves open a construction aimed only at the physical
sum, or one with genuinely different source information.

## 3. Smooth raw sectors: a separate negative witness

The cusp argument does not apply to the already-resummed whole-line
sources

\[
A_{\rm raw}(u)=2^{-1/2}\Phi_e(u+h),\qquad
B_{\rm raw}(u)=\Phi_e(u)-A_{\rm raw}(u).
\]

These are smooth, integrable after heating, and generally not even;
`B_raw` is signed. Their exact first transform is

\[
h_{A,\rm raw}(t,x)=2^{-1/2}e^{th^2-ihx}H_t(x+2ith).
\]

Resummed integrability does not permit full-line termwise integration
of individual theta summands at positive heat. Those summands have a
nonintegrable negative-half-line tail after heating. The raw calculation
uses the smooth shifted complete source instead.

At `t=x=0`, put `H=H_0(0)>0` and
`I_2=integral_0^infinity u² Phi(u) du>0`. Exact algebra gives

\[
C_{0,\rm raw}(0,0)
=(2-\sqrt2)HI_2-\frac{h^2}{\sqrt2}H^2,
\]
\[
C_{1,\rm raw}(0,0)
=(2-\sqrt2)I_2^2-(1+\sqrt2)h^2HI_2.
\]

The same positive-half-line source cells and full tails enclose these
moments and give the following outward-rounded intervals:

| Response | Complete enclosure |
| --- | --- |
| Raw same-parity `J_0` at zero frequency | `[-3.12462e-4, -2.91420e-4]` |
| Raw same-parity `J_1` at zero frequency | `[-1.31661e-5, -1.21197e-5]` |

Although a raw sector kernel is not generally even, replacing it by its
Hermitian part leaves its real zero-frequency value unchanged. Therefore
this particular repair still fails positive definiteness. Strict
negativity also persists on some positive-time interval by continuity;
no explicit positive endpoint for that interval is certified here.

This does not refute the complete response: at this same point the full
values are exactly `L_0(H)=H I_2>0` and `L_1(H)=I_2²>0`. A different
reflected construction with cross terms is a new candidate, not excluded
just by the negative sector calculation above.

## 4. The remaining target and the research decision

For the folded construction, put `D=h_A−h_B`. The two exact responses are

\[
C_j=\tfrac12\{L_j(H)+L_j(D)\},\qquad
O_j=\tfrac12\{L_j(H)-L_j(D)\}.
\]

The algebraic cusp contributions cancel between cosets. The complete
`H` and its derivatives decay faster than every inverse power on the real
axis, so estimating the sectors' leading tails does not determine the
much smaller physical response. The two-coset identity alone supplies
no sign inequality for that remainder.

The actual downstream obligations remain

\[
-H_tH_t''\ge0\quad\text{where }H_t'=0,\qquad
-H_t'H_t'''\ge0\quad\text{where }H_t''=0,
\]

on the required predecessor neighborhoods, with their time and height
coverage. Separate stationarity of the parity components is not an
admissible substitute.

The first 09 identity task is complete and usable. In 06, close the
specific independent-coset autocorrelation attempt. Reopen work through
this identity only with a named estimate controlling the complete
cross-coset expression, or a new source-derived factorization whose
extra information is explicit. A further modular rewrite, an invertible
constant change of parity coordinates, or a finite collection of passing
full-kernel samples does not meet that gate. This assessment does not
close direction 06 as a whole and establishes no RH conclusion.

## 5. Verification and provenance

The checker separates exact rational polynomial identities, finite
binary64 calibrations, and outward sign enclosures. Exact checks retain
the mixed quadratic term, insertion polynomial, zero axes, lattice
bijection, both Fourier normalizations and both raw origin formulas.
Finite calibrations also check the unequal-scale modular identity with
its characteristic and differentiated prefactor; these calibrations
carry no independent tail certification.

The integrating agent read the source and error bounds and reran the
complete checker into a temporary file. Its mathematical record matched
the retained record exactly after removing only runtime. The unchanged
interval implementations are hash-bound dependencies; their hashes
identify the implementation and are not substitutes for the arithmetic.
Notes, links, JSON records, sizes and whitespace were checked. No large
derived dataset or manuscript snapshot was created. The earlier
first-pass record remains a historical snapshot, even where this
continuation updates the current overview files.
