# Internal review of complement obstruction and centered dual energy

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Separate same-model agents checked
the source constraints, physical shorting, parity, dual energy, continuum
caps, cutoff edge, and Stieltjes comparison. These are internal checks,
not independent specialist refereeing.

Reviewed the [complement note](../notes/selective-loss-program/02_complement_obstruction_and_parity_20261003.md),
[dual energy note](../notes/selective-loss-program/03_centered_dual_energy_20261003.md),
updated [overview](../notes/selective-loss-program/overview.md), and
[small arithmetic-response package](../numerics/selective_loss_dual_response_20261003/README.md).

## 1. A substantive correction to the work sequence

The prescribed-head tail is exactly the physical constraint W*F=0.
Nonnegative tails behind two endpoint profiles on an unbounded family
already imply all-window Weil positivity because every fixed prepared
source can be translated into an untouched interior gap. The same
argument applies to the four-profile shell head. Inner normalized sum
probes give a direct proof using the established special-probe theorem.

The note makes this RH equivalence explicit and does not assume an
unconditional tail sign. A hypothetical negative compact witness gives
a negative tail at all sufficiently large outer windows. Quantitative
Rayleigh margins depend on the outer B energy and are not claimed uniform.

The support-gap estimate for m_L short templates is correct. Its linear
coverage requirement is a necessary condition for avoiding that particular
embedding argument, rather than a sufficient tail certificate or a lower
bound on all successful head families. Global templates are excluded
from that bounded-support hypothesis.

The original Schur algebra remains valid under its stated complement
hypotheses. Its first note now links the obstruction. The overview changes
the next task accordingly; the earlier endpoint sign is no longer presented
as a routine preliminary.

## 2. Physical shorting and parity checks

The physical matrix G0^(-1)T0 G0^(-1) is the constrained infimum of Q
when the complement is coercive. This follows by minimizing the complete
tail square. Its representation independence concerns fixed physical W
and the same complete arithmetic form. It does not imply that arbitrary
relative spectral losses or approximate enclosures are reference independent.
The inverse formula additionally assumes the source Q operator invertible.

Reflection preserves the source space, form domain, and the source forms.
Its exchange action on g and tau_r g diagonalizes the sum and difference
channels. The mixed entry is exactly zero, including in equivariant
approximate response and residual matrices. No unnecessary mixed-channel
margin is charged to the sum source.

Odd-sector restriction is legitimate for this target, but the inner sum
probe is also odd. The odd endpoint complement therefore has the same
RH-strength sign obligation. The local zero-loss range 1/2<r<=7/10 reuses
the existing width-6/5 certificate; it is not a new continuation theorem.

## 3. Dual energy construction and domains

The digamma series implies gamma(t)>=gamma(0), so A=Gamma+cI>=I
with c=1-gamma(0). This reference is positive without an arithmetic sign
assumption. It is the compressed source form operator, not the global
Fourier multiplier inverse. The variational inequality gives the stated
global Fourier-inverse upper bound without identifying the two inverses.

The polynomial translated source is in D(A), because its Fourier decay
of order six makes the global logarithmic multiplier vector square
integrable. The bounded prime-shift perturbation gives D(Q)=D(A). The
definition X=||T A^(1/2)F||^2 is valid on the form domain; the L2 expression
QF is used only after the operator-domain condition is verified.

The positive-square identity is exact. The minimizing parameter is
epsilon=sqrt(X/a), a=A[F], and the minimum loss is
(sqrt(Xa)-Q[F])/2. Cauchy-Schwarz gives a sign-independent allowance
at most sqrt(Xa). A certified upper value x>=X suffices. The main is
closed because its defining operator is a bounded perturbation of
(1+epsilon)A^(1/2). No finite-rank loss claim is made for this construction.

The reference energy of F_r is uniformly bounded. Polynomial X therefore
implies the existing one-sided criterion. For the converse, RH is stated
before using its positive zero samples. Absolute sixth-power transform
decay and the multiplicity-weighted zero count give a uniformly bounded
zero series for QF before restriction and source projection. This proves
X=O(r) under RH, not unconditionally. The projected prime-response norm
has the same polynomial RH equivalence through the bounded global
archimedean response.

The full residual identity for Ay=QF is correct for y in D(A). Its
upper bound uses the complete residual, including support restriction,
prepared moment projection, active powers, and all numerical errors.
A selected-row residual cannot be substituted.

## 4. Exact continuum and cutoff calculations

The full density window 0<=u<=r+ell yields two fixed cap profiles
v=(-h''-h'/2)/sqrt(nu) and q0=(h''-h'/2)/sqrt(nu). Their squared
combined norm is exactly 917180/580421327, independent of r>ell.
The rational script checks the profile normalization, factored derivative
formula, derivative norms, and zero cross integral.

The density layer r<=u<=r+ell swaps the caps and multiplies them by
exp(r/2). Its actual sinh moment is lambda0 exp(r/4), including that
prefactor. Projection subtracts only an O(1) squared contribution, so
the projected density edge has squared norm exp(r) times the cap
constant minus O(1). This is a continuum cutoff obstruction; no claim
that the actual prime response has that size is made.

Stieltjes integration by parts retains psi(1)-1=-1 and gives the lower
boundary F_r. The upper endpoint kernel vanishes. The derivative signs,
weight e^(-u/2), and change of variables to dx/x^2 were checked.
Young's inequality yields the recorded bound using
Dg=||g'||^2+1/4=1950415853039/2321685308. This is a comparison to
weighted Chebyshev-error energy, not a proof that the energy is polynomial.
Taking this absolute norm may lose the useful signed smoothing.

## 5. Numerical scope and reproduction

The actual finite arithmetic-response pilot includes every active prime
power and all shifted-polynomial support breakpoints at r=2,3,4,5,6.
For the odd response the three-moment projection removes precisely its
sinh component. The denominator sinh(L/2)-L/2 was checked analytically.

Gauss order 16 is exact for its degree-30 raw polynomial integrand in
ideal real arithmetic. Orders 24 and 32 agree near floating precision,
and the sinh moment comparison is stable. These are floating diagnostics,
not rounding enclosures. The root replay reproduced the five reported
values; both runs took less than a second. The moment projection removes
less than 0.13 percent at these samples. No extrapolated exponent, loss
certificate, inverse energy, or global rate is inferred.

The separate fixed-profile script uses exact rational arithmetic, and the
root replay verified its two constants. The floating and exact records
carry hashes of their own generating scripts. Neither hash nor a decimal
value is used as a proof of a global sign.

## 6. Remaining task and repository checks

The new work supplies an obstruction, parity reduction, exact continuum
cancellation, and a positive-reference response target. Polynomial,
subexponential, or suitable weighted-integral control of the full prime
discrepancy or X remains unproved. Available unconditional prime-error
envelopes still give exponential losses. No RH proof or improved
zero-free region is claimed.

Primary references checked for the new comparison were the
[DLMF digamma series](https://dlmf.nist.gov/5.7.E6) and
[Hasanalizade, Shen and Wong's zero-count paper](https://arxiv.org/abs/2107.06506).
The arithmetic explicit formula, probe decay, and one-sided implication
remain the previously linked repository results.

Local links, whitespace, displayed-math delimiters, small-file sizes,
script hashes, and preserved manuscript and draft-history hashes were
checked. No synchronized project reference was edited. No manuscript,
snapshot, commit, push, or large derived data file was created.
