# Complement obstruction and exact parity in the Schur program

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Three same-model agents checked the
constrained-source identification, interior embedding, parity, and physical
shorting. These are internal checks, not independent specialist refereeing.

This continues the [first Schur note](01_schur_completion_20261003.md).
The central finding changes the order of work: uniform nonnegative tails
behind the two endpoint profiles already carry the RH-level arithmetic
positivity problem. They cannot be treated as an independent geometric
preliminary. Parity gives a useful exact simplification but does not remove
this obstruction. No polynomial loss or new global positivity is proved.

## 1. What complement safety means in physical source coordinates

At a fixed source interval and complete finite prime set use

\[
Q=B-K,\quad B\ge\beta I>0,\quad
H=B^{-1/2}KB^{-1/2},\quad \mathcal V=D(B^{1/2}).
\]

Let W have independent physical prepared source columns and put

\[
G_0=W^*B^{-1}W,\quad U=B^{-1/2}WG_0^{-1/2},\quad
E=UU^*,\quad P=I-E,
\]
\[
D=P(I-H)P|_{E^\perp}.
\]

The identity U*B^(1/2)F=G0^(-1/2)W*F and the bijection
B^(1/2):V to the source Hilbert space give

\[
\boxed{D\ge0\ \Longleftrightarrow\
Q[F]\ge0\quad\text{for every }F\in\mathcal V\cap\ker W^*.}
\tag{1}
\]

More quantitatively,

\[
\boxed{D\ge\delta I\ \Longleftrightarrow\
Q[F]\ge\delta B[F]\quad\text{for every }F\in\mathcal V\cap\ker W^*.}
\tag{2}
\]

These are constrained arithmetic sign and coercivity statements. They
are not consequences of B's independently positive gap or the finite
Gram normalization. All active primes must be captured before using the
complete arithmetic Q in these statements.

## 2. Endpoint heads contain entire untouched inner windows

For the existing probe of support diameter ell=1/2, work first in

\[
I_r=(-\ell/2,r+\ell/2),\qquad
W_r=[g,\tau_rg],\qquad S_r=\{p:p\le e^{r+\ell}\}.
\]

Every prepared compact source supported in

\[
J_r=(\ell/2,r-\ell/2),\qquad |J_r|=r-\ell,
\tag{3}
\]

is orthogonal to both physical templates. Suppose D_r is nonnegative
along any unbounded sequence of outer separations. Given an arbitrary
fixed compact prepared source, translate it into one sufficiently large
J_r. Translation preserves its three zero moments and Q, which depends
on the autocorrelation. Equation (1) proves Q nonnegative on that source.
Thus the all-window Weil criterion follows.

The same implication can use only the established special-probe theorem.
For any inner separation t>ell, choose r>t+2ell and put

\[
\widetilde F_{t,r}=\tau_{(r-t)/2}F_t.
\]

Its support fits strictly in J_r, so W_r*Ftilde=0. Nonnegative outer
tail safety implies Q[F_t]>=0. An unbounded outer family proves this
for every t, and hence the existing one-sided/single-probe theorem gives RH.
No density or spanning assertion about translates of g is required.

Consequently

\[
\boxed{\text{Nonnegative two-profile tails on an unbounded family}
\quad\Longleftrightarrow\quad\mathrm{RH}.}
\tag{4}
\]

The converse in (4) uses RH solely as a stated hypothesis: full Weil
positivity makes every constrained tail nonnegative. Positive window
dependent gaps delta_r are at least as strong as the forward implication.
The existing [conditional strict-gap argument](../../reviews/ALL_WINDOW_MECHANISM_OBSTRUCTION_AUDIT_20261003.md)
also supplies the strict converse at each fixed window under RH. It
excludes source null vectors using the superlinear number of distinct
critical zero ordinates and the zero-count limit for nonzero entire
transforms of compact support. It does not assume simple zeta zeros.
If that fixed-window Q gap is alpha_r>0 and ||K||<=k_r, then

\[
B=Q+K\le Q+k_rI\le(1+k_r/\alpha_r)Q,
\]

so Q>=alpha_r/(alpha_r+k_r) B and a strict tail gap exists. No uniform
gap or effective onset is asserted.

The four-profile shell head from the first note has the same problem.
Its templates at 0,j,j+1/2,j+1 leave (ell/2,j-ell/2) untouched. The
exact shell covariance is valid, but it cannot establish the full tail
sign independently of the inner arithmetic problem.

## 3. Explicit conditional adverse tail sources

If RH were false, the [one-sided excursion theorem](../GLOBAL_GROWTH_ONE_SIDED_20261003.md)
would give arbitrarily large positive and negative exponential excursions
of M_g(t). For r>2+ell the prepared normalized sources

\[
\widetilde F_r^\pm=
\frac{\tau_1g\pm\tau_{r-1}g}{\sqrt2}
\tag{5}
\]

are orthogonal to both endpoint profiles. Their arithmetic values are

\[
Q[\widetilde F_r^+]=q-M_g(r-2)+\epsilon_g(r-2),
\]
\[
Q[\widetilde F_r^-]=q+M_g(r-2)-\epsilon_g(r-2).
\tag{6}
\]

The decaying archimedean correction cannot cancel the hypothetical
excursions. The plus source is negative along large positive excursions;
the minus source is negative along large negative excursions. Their
relative energy vectors lie in the prescribed complement.

More strongly, fix any one compact negative witness of width L0. It fits
in J_r for every sufficiently large r, and so the full endpoint tail
would be negative at every such outer window. This is conditional on
RH being false, not evidence of an actual negative source.

For an embedded unit witness with Q[F]=-nu<0,

\[
\inf\operatorname{spec}D_r\le-\frac{\nu}{B_r[F]}<0.
\tag{7}
\]

The margin is not uniformly estimated; B_r[F] changes with the outer
prime set. Metric normalization cannot remove this negative direction.

## 4. A necessary support coverage condition

Suppose m_L physical templates on an interval of length L each have
support diameter at most a, independent of L. Their support hulls have
total union length at most m_L a and leave at most m_L+1 open interval
components. When L-m_L a>0, one untouched gap has length at least

\[
d_L\ge\frac{L-m_La}{m_L+1}.
\tag{8}
\]

If m_L=o(L), these gap lengths tend to infinity. Nonnegative prescribed
complements along that growing family therefore again imply RH by
translation of arbitrary prepared inner sources.

To keep every untouched gap below a fixed d, a necessary geometric
condition is

\[
\boxed{m_L\ge\frac{L-d}{a+d}.}
\tag{9}
\]

This is a requirement for avoiding the untouched-window mechanism. It
is not an unconditional lower bound on all successful heads, a sufficient
tail certificate, or an obstruction to polynomial-size heads. Globally
supported templates, such as physical images of B spectral vectors,
are outside the bounded-support hypothesis. Their actual weighted loss
and full complement still require estimates.

## 5. Exact physical shorting and cancellation of the reference metric

At one fixed window assume the full safe-tail hypothesis D>=delta I.
With normalized head matrix

\[
S=I-H_{00}-G^*D^{-1}G,\qquad T_0=G_0^{1/2}SG_0^{1/2},
\]

the exact physical coefficient is

\[
C_{\rm phys}=G_0^{-1}T_0G_0^{-1}
             =G_0^{-1/2}SG_0^{-1/2}.
\]

For every d in the physical coefficient space,

\[
\boxed{d^*C_{\rm phys}d
=\inf\{Q[F]:F\in\mathcal V,\ W^*F=d\}.}
\tag{10}
\]

Indeed c=G0^(-1/2)d fixes the relative head coordinate. The Schur
completion attains its minimum over the relative tail at w=D^(-1)Gc,
corresponding to F=B^(-1/2)(Uc+w) in V. This proves (10) without
assuming S positive.

The exact physical matrix therefore depends on Q, W, and the source
window, rather than on the chosen positive reference B. Extra primes
inactive throughout that window change the intermediate Gram and
resolvent terms but cancel in this exact coefficient once all active
primes are already captured. Approximate lower matrices need not preserve
that cancellation automatically. Changing B can help a certificate's
conditioning and error bounds; it cannot change this intrinsic constrained
infimum for a fixed W.

If the source operator Q is invertible and the safe-tail hypothesis
holds, block inversion additionally gives

\[
C_{\rm phys}=(W^*Q^{-1}W)^{-1}.
\tag{11}
\]

Invertibility is an extra hypothesis. No inverse formula is asserted at
a zero mode. Neither (10) nor (11) gives a tame bound: the constrained
infimum can deteriorate near tail instability.

## 6. Reflection removes the mixed physical channel

Center the interval at r/2 and let R_rF(x)=F(r-x). It preserves the
three-moment space, exchanges the exponential moment conditions, and
preserves the logarithmic form domain. The source forms Q and B are
reflection invariant. For B this follows from the even frequency
measure of the real Sonin projection in the
[finite Euler identity](../FINITE_EULER_BOUNDARY_IDENTITY_20261003.md);
translation changes only the source Fourier phase. The arithmetic bulk
is even, so K=B-Q is also invariant. Their selfadjoint realizations,
inverses, and square roots commute with reflection in the domain sense.

With X the two-coordinate exchange matrix and W=[g,tau_r g], oddness
of g gives R_rW=-WX. Therefore G0, C0, the exact raw Schur matrix T0,
and C_phys all commute with X. The physical sum direction
d_plus=(1,1)/sqrt(2) is odd about r/2; the difference direction
d_minus=(1,-1)/sqrt(2) is even. Their mixed entry is exactly zero.

This can be preserved in approximate solves. Replace arbitrary response
columns Y0 by

\[
\overline Y_0=(Y_0-R_rY_0X)/2.
\tag{12}
\]

The full residual then has the same equivariance. Its Gram matrices and
signed response matrix commute with X. Certified error matrices can be
averaged with X without invalidating order against a symmetric target.

For a symmetry-preserving lower raw matrix M0, define

\[
a=d_+^*G_0^{-1}M_0G_0^{-1}d_+,\qquad
d=d_-^*G_0^{-1}M_0G_0^{-1}d_-.
\]

The first note's joint positive allowance test passes with

\[
\ell_+=\max(0,-a),\qquad \ell_-=\max(0,-d).
\tag{13}
\]

The artificial positive margin needed for a general mixed two-by-two
matrix is unnecessary here. The target is charged exactly ell_plus.
All of this remains conditional on the stated safe complement and full
residual bounds.

## 7. Odd reduction and its remaining obstruction

Since the target F_r is odd about r/2, its comparison may be carried
out entirely in the odd source sector. The even tail need not be proved
safe for this scalar goal. Within the odd sector use the one physical
template f=F_r, define

\[
\kappa=\langle f,B_{\rm odd}^{-1}f\rangle,
\quad b=B_{\rm odd}^{-1}f,
\quad j_0=P B_{\rm odd}^{-1/2}K_{\rm odd}b,
\]

and retain the full odd complement D. Here P projects away from the
normalized odd head vector B_odd^(-1/2)f/sqrt(kappa). If that odd
complement is safe, the exact scalar coefficient is

\[
a_{\rm exact}=
\frac{\kappa-\langle b,Kb\rangle-\langle j_0,D^{-1}j_0\rangle}
     {\kappa^2}
=\inf_{\substack{F\ {m odd}\,,\ F\in\mathcal V\\
                 \langle f,F\rangle=1}}Q[F].
\tag{14}
\]

For response y and residual rho=j0-Dy, a certified N>=<rho,D^(-1)rho>
gives the lower numerator

\[
m=\kappa-\langle b,Kb\rangle
  -2\Re\langle j_0,y\rangle+\langle y,Dy\rangle-N.
\tag{15}
\]

Then Q[f]>=-max(0,-m/kappa^2). Keeping the joint numerator is essential;
separate worst inverse-Gram and norm bounds can destroy cancellation.

However the centered inner sum source in Section 2 is also odd. It is
orthogonal to the outer f and lies in the odd complement. Nonnegative
odd-tail safety along unbounded endpoint windows therefore still implies
RH. Parity halves the finite work; it does not turn this tail sign into
an easier preliminary assertion.

The previous local certificate supplies a valid continuous seed:
for 1/2<r<=7/10, a common width-6/5 interval and S={2,3} give
D_odd>=3I/6916003. The exact infimum (14) is at least 3/2000 because
the existing all-source bound is Q[F]>=3||F||^2/2000 and
<f,F>=1 forces ||F||>=1. The exact odd Schur loss vanishes there.
This reuses the [two-prime certificate](../ALL_WINDOW_EXTENSION_OUTCOME_20261003.md)
and does not extend it to a larger window.

## 8. Consequence for the active program

The earlier finite Schur algebra remains valid. The corrected global
sequence should not begin by demanding a nonnegative arithmetic complement
behind two or four compact profiles. There are two routes that retain an
independently positive main and a tolerated loss:

1. Augment the odd head with modes having a genuinely unconditional full
   tail certificate. Their source loss must be retained. The existing
   k/b_(n+1) bound proves fixed-window existence but has prohibitive
   growing-window cost; no better rate is established here.
2. Use a known positive reference energy and an explicit weighted adverse
   response, without requiring the unknown arithmetic tail to be
   nonnegative. The [centered dual energy continuation](03_centered_dual_energy_20261003.md)
   gives that construction and a concrete projected prime-response target.

The exact parity and physical shorting results improve the organization
and prevent artificial losses. The interior-gap result identifies why
the original endpoint complement obligation cannot be assumed or obtained
from its finite source covariance. The needed global cancellation estimate
remains open.

See the [continuation review](../../reviews/SELECTIVE_LOSS_COMPLEMENT_AND_DUAL_REVIEW_20261003.md)
for the internal checks and scope.
