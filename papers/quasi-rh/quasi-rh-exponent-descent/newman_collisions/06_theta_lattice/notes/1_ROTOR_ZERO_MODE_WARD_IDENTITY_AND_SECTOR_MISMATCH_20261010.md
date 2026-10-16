# Rotor zero mode, an affine theta Ward identity, and sector mismatch

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. This scout and its review are internal
LLM work, not independent mathematical validation.

This implements direction 06 of [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
Its additional result is an exact affine differential identity relating the
genuine heat function to the heat transform of the zero-mode-subtracted
rotor trace. The identity retains a nonzero endpoint constant. A two-rotor
completion then exhibits an explicit coefficient and odd-endpoint mismatch
unless its spectator sector is projected out. No signed exclusion follows.

## 1. Exact rotor reduction and orientation

On `ell^2(Z)`, let `P e_n=n e_n`, with domain
`sum n^2 |a_n|^2 < infinity`. For every `v>0`, the operator
`exp(-pi v P^2)` is trace class, and polynomial insertions in `P` are trace
class. Write

\[
\vartheta(v)=\operatorname{Tr}e^{-\pi vP^2},\quad v=e^{4u},\qquad
I_v=v^{1/4}(\pi^2v^2P^4-\tfrac32\pi vP^2)e^{-\pi vP^2}.
\]

Pairing `n` and `-n` gives exactly the manuscript's kernel:

\[
\operatorname{Tr}I_v
=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}
=\Phi(u).
\tag{1}
\]

The inserted zero mode is zero. For `u>=0` every nonzero summand is
positive, since `pi n^2 e^{4u}>3/2`. The full kernel's reflection follows
from Poisson duality
`vartheta(v)=v^{-1/2} vartheta(1/v)`; this is also the specialization of
[DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32). This external identity is
the only theta transformation imported here.

The state is `e^{t u^2} I_{e^{4u}}`, and the readout is its trace integrated
against `cos(xu)` on `u>=0`. Newman time has generator multiplication by
`u^2` on this state. It is distinct from the positive rotor Hamiltonian
`pi P^2`. For bounded real times and bounded complex `x`, super-exponential
decay gives absolute trace-norm integration after each fixed spatial
derivative. Therefore

\[
H_t^{(j)}(x)=\int_0^\infty u^je^{tu^2}\Phi(u)
 \cos(xu+j\pi/2)\,du,\qquad 0\le j\le4,
\tag{2}
\]

and `partial_t H_t=-H_t''`. These are fixed-time raw derivatives; there is
no cutoff differentiation or independent phase choice in this realization.

## 2. Removing the zero mode before the logarithmic transform

Set

\[
h(u)=e^u\vartheta(e^{4u}),\qquad
k(u)=e^u(\vartheta(e^{4u})-1),\quad u\ge0.
\]

Direct differentiation gives

\[
\Phi(u)=\frac{h''(u)-h(u)}{16}
=\frac{k''(u)-k(u)}{16}.
\tag{3}
\]

The first expression has even `h` by Poisson duality. In particular
`h'(0)=0`, hence `k'(0)=-1`. The half-line `k` is positive and decays
super-exponentially. In contrast, the even subtraction
`h(u)-2 cosh(u)` decays only like `-exp(-|u|)` and cannot be integrated
against `exp(tu^2)` at positive time. Performing that formally even
subtraction inside a Newman heat transform is a domain error.

The admissible zero-mode-subtracted observation is instead

\[
J_t(x)=\int_0^\infty e^{tu^2}k(u)\cos(xu)\,du.
\tag{4}
\]

It is jointly entire, has `partial_t J_t=-J_t''`, and uses the same actual
height `x` as `H_t`. Two integrations by parts in (3) give

\[
16H_t(x)=1+(2t-1-x^2)J_t(x)+4txJ_t'(x)-4t^2J_t''(x).
\tag{5}
\]

All infinity boundary terms vanish; the remaining term is `-k'(0)=1`.
Thus (5) is an affine identity, not a homogeneous positivity constraint.
At `t=0` it becomes `16H_0=1-(1+x^2)J_0`.

For `J_j=J_t^{(j)}(x)` and `a=2t-1-x^2`, its differentiated form is

\[
16H_t^{(j)}(x)=\mathbf1_{j=0}
 +(a+4tj)J_j-2jxJ_{j-1}-j(j-1)J_{j-2}
 +4txJ_{j+1}-4t^2J_{j+2},\qquad0\le j\le4,
\tag{6}
\]

where terms with negative indices are omitted. This prints the genuine
fourth readout in terms of the sixth `J` jet, without inventing a closure.
One can check the time orientation directly: the operator on the right
of (5), including its time dependence, commutes with the backward-heat
equation in the required sense. The constant term also solves that equation.

At a genuine common zero, (5) and (6) impose

\[
1+aJ_0+4txJ_1-4t^2J_2=0,
\quad -2xJ_0+(a+4t)J_1+4txJ_2-4t^2J_3=0.
\tag{7}
\]

These are genuine theta relations rather than relations for independent
arithmetic phases. They have no forced sign: `J_0,J_2,J_3` are oscillatory
observations of a positive density. For `t>0`, (6) expresses the next
`J_{j+2}` in terms of lower jets and the specified `H` jet. Thus (7) is
consistent as an algebraic jet system. Algebraic consistency is not a
construction of an actual theta collision. It shows why simply calling
(7) a Ward identity does not prove exclusion.

## 3. An explicit two-rotor completion

Consider two independent rotors with partition trace
`Z(v)=vartheta(v)^2`. Insert `I_v` in the first factor and the ordinary
heat kernel in the second. Its reduction is

\[
\operatorname{Tr}(I_v\otimes e^{-\pi vP^2})
=\Phi(u)\vartheta(e^{4u}).
\tag{8}
\]

It changes the kernel already at `u=0` by the strict factor
`vartheta(1)>1`. Differentiating the modular identity at `v=1` gives
`vartheta'(1)=-vartheta(1)/4`; consequently (8) has derivative
`-Phi(0) vartheta(1)` at `u=0`, rather than zero. Its cosine transform has
an artificial leading inverse-square endpoint term: for
`f=e^{tu^2}Phi(u)vartheta(e^{4u})`, two integrations by parts give
`int f cos(xu) du=-f'(0)/x^2+O(x^{-4})` for fixed time. This is a concrete
failure to preserve the full theta odd-endpoint cancellation, not a small
unpaid correction.

Multiplying the spectator trace by `e^u` restores evenness but produces
the different kernel `Phi(u)h(u)`. Dividing by the entire spectator trace
or projecting it to its zero mode gives the exact original kernel. The
projection `|0><0|` has spectator trace one. This is an exact completion
with a declared sector map, but its extra channel has then contributed
no surviving collision constraint. These statements concern this product
completion only, not all compact-boson constructions. Oscillator sectors
have not been silently identified with a rank-one rotor.

## 4. Arithmetic error interface and continuation

Equations (1)–(7) are exact full-kernel formulas. If they are evaluated
through the manuscript's fixed finite approximant, use its common center
`L=kappa/t`, `x=4 pi exp(L)` and natural integer `N` frozen locally. With
`H=AQ`, compute `H^{(j)}=sum_{k=0}^j binom(j,k) A^{(k)}Q^{(j-k)}`;
`Q^{(j)}` and `F_{t,N}^{(j)}` differ by at most `j! L^j eta_N`.
No cutoff truncation of the theta trace in (1) inherits theta reflection
automatically. The manuscript's fixed-theta-truncation obstruction remains
the relevant control.

A continuation can insert (6) into the all-real threshold form
`2q_3^2-3q_2q_4-gamma q_2^2`, using the full normalization and measured
quadratic payment from Note 13. Its bounded objective should be a
candidate-conditioned *signed* constraint on the actual `J` moments,
including the sixth moment needed by (6), not another positive rotor norm.
This scout reaches exact representation and a specific completion
obstruction. It establishes no signed exclusion or endpoint coverage.

The [checker](../numerics/check_theta_lattice_scout.py) uses exact rational
polynomials to verify the integration-by-parts operator, its first four
derivatives, and its heat compatibility. These finite formal checks do not
validate an actual theta sign, an asymptotic interchange, or a collision
claim. The analytical decay and boundary justification is the argument
above; specialist review remains outstanding.
