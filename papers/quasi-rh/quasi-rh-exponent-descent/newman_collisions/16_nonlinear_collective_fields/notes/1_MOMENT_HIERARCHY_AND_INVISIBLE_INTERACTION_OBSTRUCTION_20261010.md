# Exact moment hierarchies and invisible density interactions

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Checks are internal LLM work.

This scouts program 16 of
[Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The new bounded outputs are a local finite-moment nonclosure argument and
an injectivity obstruction to adding invisible interactions to the density
itself. They do not exclude hidden interacting fields or arithmetic constraints.

## 1. Genuine normalization and all missing jets

Retain the full positive theta kernel of the
[manuscript](../../newman_collision_reductions.tex), and put

\[
Z_t=H_t(0)>0,\quad \rho_t(u)=e^{tu^2}\Phi(u)/Z_t\ (u\ge0),\quad
m_j=\int_0^\infty u^j\rho_t(u)du.
\]

All displayed time and spatial derivatives converge locally uniformly
because the theta tail dominates every fixed Gaussian and exponential.
The exact nonlinear state equations are

\[
\dot Z_t=m_2Z_t,\qquad
\partial_t\rho_t=(u^2-m_2)\rho_t,\qquad
\dot m_j=m_{j+2}-m_2m_j.
\tag{1}
\]

For chi_t(x)=int rho_t cos(xu)du and J_j=partial_x^j chi_t,

\[
\partial_t\chi_t=-\chi_t''-m_2\chi_t,\qquad
\dot J_j=-J_{j+2}-m_2J_j\quad(0\le j\le4).
\tag{2}
\]

Thus the fourth spatial jet depends on the sixth, the third on the fifth,
and the fourth unsigned moment depends on the sixth. Restoring H=Z chi
gives H_t=-H_xx exactly. The state is positive; its oscillatory readouts
have no automatic positive sign.

Two honest monotonic quantities are

\[
\dot m_2=m_4-m_2^2=\operatorname{Var}_{\rho_t}(u^2)>0,\qquad
\partial_t^2\log Z_t=\operatorname{Var}_{\rho_t}(u^2)>0.
\tag{3}
\]

The strict inequalities use the positive density on intervals. They concern
the readout at x=0, where H never vanishes; they do not give visibility at
an oscillatory candidate x>0.

## 2. Why a finite moment list has no universal regular closure

Suppose a rule m_{2r+2}=F(m_2,...,m_{2r}) is claimed for all densities
in a neighborhood of a strictly positive density with a finite next
moment. Choose an interval [a,b] inside (0,infinity). In the inner product
int_a^b f g rho du, subtract from u^{2r+2} its orthogonal projection
onto span{1,u^2,...,u^{2r}}. Let the nonzero residual be p, extended by
zero outside that interval. It is bounded and satisfies

\[
\int u^{2k}p\rho\,du=0\ (0\le k\le r),\qquad
\int u^{2r+2}p\rho\,du=\int p^2\rho\,du>0.
\tag{4}
\]

For epsilon small, rho_plus/minus=rho(1 plus/minus epsilon p) are
positive probability densities. Their first r even moments agree and
their next moments differ. They retain the original tails, including
super-exponential tails when rho is theta. Hence F cannot hold on this
nearby class. Smooth compactly supported residuals can instead be obtained
by solving the same finite orthogonality constraints in a bump-function
space; the bounded construction is already enough for the stated domain.

An exact finite witness is rho_plus/minus=(1 plus/minus P_6(u)/100)/2
on [-1,1], using

\[
P_6=(231u^6-315u^4+105u^2-5)/16.
\]

Its coefficient-sum bound proves positivity, and exact integration gives

\[
\int_{-1}^1u^{2k}P_6du=0\ (k=0,1,2),\qquad
\int_{-1}^1u^6P_6du=32/3003.
\tag{5}
\]

This proves nonclosure through m_4, and is retained in the exact
[checker](../numerics/check_moment_nonclosure.py) and
[record](../numerics/moment_nonclosure_record_20261010.json).
The compactly supported control is not itself the genuine theta state.

Another restricted obstruction concerns constant-coefficient recurrences.
If all genuine even moments obey a finite constant recurrence corresponding
to a nonzero polynomial P(u^2), then
int u^{2k}P(u^2)rho du=0 for every k>=0. Taking the linear combination
that forms P gives int P(u^2)^2 rho du=0, impossible for a positive density
on every interval. The full theta moment sequence therefore has no such
finite recurrence. This says nothing about nonlinear identities specific
to the one-parameter theta family.

In particular that family already has the exact one-dimensional coordinate
t. Writing each moment as its unknown function of t is a parametrization,
not a derived predictive closure or a new collision theorem. The scout
does not claim that every finite representation of the theta family is
impossible.

## 3. An interaction invisible to the complete readout must vanish

Consider the proposed density architecture

\[
\partial_t\rho=(u^2-m_2)\rho+R_t(u),\qquad \int R_tdu=0,
\tag{6}
\]

where R_t is integrable and the same Z'=m_2Z is used. The reduced equation
has the additional term Z int R_t cos(xu)du. If the genuine scalar heat
equation is required for every real x, this cosine transform must vanish
for every x. Its even extension to the line has zero Fourier transform;
Fourier injectivity for L1 gives R_t=0 almost everywhere.

Allowing Z'/Z=m_2+c instead requires int R cos=-c chi for every x,
so R=-c rho. Its zero mass then forces c=0. Extra normalization does not
create a nontrivial invisible density interaction. The hypotheses are a
full cosine readout on an even L1 density and exact equality for every x.
Hidden fields, nonlocal reductions, or interactions whose effect is paid
as an error rather than zero are outside this obstruction. At one chosen
x, vanishing of two readouts leaves a large source kernel and does not
force R=0.

## 4. The candidate-conditioned signed target

Define C_j=int u^j rho cos(xu)du and S_j=int u^j rho sin(xu)du. At
an ordinary candidate collision C_0=S_1=0 and

\[
H_2=-Z C_2,\qquad H_3=Z S_3,\qquad H_4=Z C_4.
\]

Let b=partial_x log A and use the normalized jets q_j of Note 13.
At an exact collision their fourth-jet expression equals

\[
A^2\mathscr L(q)
=2H_3^2-3H_2H_4-9H_2^2/x^2
=Z^2(2S_3^2+3C_2C_4-9C_2^2/x^2).
\tag{7}
\]

All normalizer terms cancel here only after imposing both exact collision
equations. They must be retained in approximate candidate tests. The
all-real-threshold necessity is that (7) is nonnegative. A useful new
arithmetic result would force its strictly negative paid opposite. The
constraints C_0=S_1=0 do not make the cosine-weighted measure positive,
so unsigned moment Hankel positivity cannot decide the sign of C_2 C_4.

The next bounded task is a theta-specific relation on these signed moments,
using either the arithmetic score identities of program 03 or the lattice
Ward identity of program 06, with the measured payment of Note 13.
Generic moment closure and an invisible source in the density are now
precisely delimited. No signed exclusion or parameter coverage is proved.
