# Positive channel absorption: an exponential ambient obstruction and a selective source construction

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are not exposed and are not inferred. Three separate same-model
agents checked the channel factorization, translated-source geometry,
regularity, and scaling. These are internal checks, not independent
specialist refereeing. No literature-priority claim is made.
Repository baseline: `5052fc961dc755718f2cf88516e78096eb9e8edf`;
the existing global-growth continuation remains uncommitted and was
preserved.

## 1. Outcome and the authorized direction

This continuation follows the user's proposal to modify the positive
Sonin trace by incorporating boundary contributions, leaving a favorable
or adequately bounded remainder. The intended initial target is the
normalized translated source

\[
F_r=(g+\tau_rg)/\sqrt2,\qquad r>\ell=1/2,
\]

with the existing prepared polynomial probe, not a newly chosen profile.
The source is real, its squared L2 norm is one, and all three moments
vanish. Translate it simultaneously when a centered support interval is
required. Its support diameter is L=r+ell. The finite prime set must grow
with this diameter; a safe choice throughout is

\[
S_r=\{p:p\le \mathsf X_r\},\qquad \mathsf X_r=e^{r+\ell}.
\]

The continuation gives three concrete analytic results:

1. An exact independently positive ambient main term, expressed as
   squared norms of explicit boundary channels. It avoids a scalar
   inverse-gap estimate.
2. An unconditional obstruction: its adverse remainder is at least a
   positive constant times exp(r/2). The same barrier applies to every
   positive ambient-operator splitting of the phase difference with
   legitimate smoothed traces. It does not refute source-form absorption.
3. A selective positive construction on the relative source space. It
   absorbs every correction mode up to the energy threshold one and
   leaves only a finite-rank excess at each fixed window. A finite
   approximation gives an explicit source-weighted loss certificate.

The global bound on that selective loss remains unproved. No new
all-window positivity theorem, zero-free region, or RH proof is obtained.
No large numerical run, manuscript revision, snapshot, commit, or push
is part of this continuation.

## 2. The precise sufficient remainder bound

Write q=Q[g] and retain the established identity

\[
Q[F_r]=q-M_g(r)+\epsilon_g(r),\qquad
|\epsilon_g(r)|\le b(r),
\]
\[
b(r)=\frac{\ell e^{-5(r-\ell)/2}}{1-e^{-2(r-\ell)}}.
\tag{1}
\]

If a construction supplies Q[F_r]=P_r[F_r]+R_r[F_r], with P_r[F_r]>=0
and R_r[F_r]>=-E(r), then

\[
M_g(r)\le q+b(r)+E(r).
\tag{2}
\]

It is enough that E(r)=O_epsilon(exp(epsilon r)) for every epsilon>0,
eventually at every real r. A fixed constant or polynomial loss would
therefore suffice. This implication uses the
[one-sided theorem](GLOBAL_GROWTH_ONE_SIDED_20261003.md), including its
special-probe noncancellation and real-axis regularity. The remainder
need not tend to zero or be nonnegative. A bounded set of separations or
isolated samples does not establish (2) globally.

Under the existing sign convention Q=B-K, the absorbed construction is
P=B-A, R=A-K. A favorable exact split needs K<=A<=B. Adding the same
positive form to B and K preserves their difference and does not improve
the comparison. The new constructions below distinguish positive
ambient channels from positive quadratic forms on the source space.

## 3. Exact ambient boundary channels

Fix a finite S and exponent 1/2. Use the operators and conventions of the
[finite Euler identity](FINITE_EULER_BOUNDARY_IDENTITY_20261003.md):

\[
\mathcal Q=V^*PV-P,
\quad T=\chi\mathcal FP,\quad C=\chi\mathcal F\chi,
\quad s=(I-C^2)^{1/2},\quad U=T^*s^{-1}.
\]

Here Q is the arithmetic scalar form, whereas mathcal Q is the ambient
selfadjoint difference of projections. Put L_op=P-T*T. The exact gap
ensures s is invertible for fixed S, and U is an isometry from chi H
onto (P-Pi)H. The subspace M=U chi H direct-sum chi H reduces mathcal Q;
in these coordinates

\[
\mathcal Q|_{\mathcal M}
=\begin{pmatrix}-C^2&sC\\Cs&C^2\end{pmatrix},
\qquad \mathcal Q\Pi=-\Pi,
\qquad
\mathcal Q^2=\operatorname{diag}(L_{\rm op},C^2).
\tag{3}
\]

Let d=|C|, j=sign(C), with sign(0)=0, and define

\[
\alpha=\sqrt{d(1-d)/2},\qquad
\beta=\sqrt{d(1+d)/2},
\]
\[
W_+\xi=U\alpha\xi+j\beta\xi,
\qquad W_-\xi=U\beta\xi-j\alpha\xi.
\tag{4}
\]

The second summands lie in chi H. Functional calculus gives
alpha beta=ds/2, j d=C, and j squared equals one on the range of d.
Direct multiplication of the two columns proves

\[
\mathcal Q_+=W_+W_+^*,\qquad
\mathcal Q_-=\Pi+W_-W_-^*,\qquad
W_\pm^*W_\pm=d\le\|C\|I.
\tag{5}
\]

No estimate of 1/sqrt(g_S) is taken in these identities. The isometry U
still uses the exact inverse boundary metric; dropping that metric would
not give (3)--(5).

For a smooth compact prepared source F, and for the particular g and
F_r covered by the extension below, set

\[
N_S[F]=\|C_FW_-\|_{\rm HS}^2,\qquad
E_S[F]=\|C_FW_+\|_{\rm HS}^2.
\]

Write Q_S[F]=Gamma[F]-W_S[F]. The finite Euler trace identity then yields

\[
\boxed{Q_S[F]=\underbrace{B_S[F]+N_S[F]}_{P_S[F]\ge0}
                  -\underbrace{E_S[F]}_{\ge0},
\qquad K_S[F]=E_S[F]-N_S[F].}
\tag{6}
\]

The identification Q_S[F]=Q[F] requires S to contain every active prime
for F. This capture hypothesis holds for S_r,F_r and for any S,g, since
g has diameter less than log 2. Without capture the omitted arithmetic
term must be retained. The trace construction is not asserted here for
arbitrary sources in the logarithmic form closure beyond the stated
smooth class and the specific probe extension.

This is an actual independently positive main term, not a main term
whose positivity assumes Q_S>=0. Its state-space contraction in (5) does
not imply E<=B: W_+ lies in the boundary complement, whereas B smooths
the Sonin projection.

### Trace classes and the nonsmooth probe

For smooth compact sources a(D)mathcal Q is trace class by the inherited
cutoff lemma, with a=|Fhat| squared. Since

\[
a(D)|\mathcal Q|=a(D)\mathcal Q\operatorname{sign}(\mathcal Q),
\]

it too is trace class. The positive-product trace identity then proves
that C_F mathcal Q_plus C_F* and C_F mathcal Q_minus C_F* are positive
trace class, with traces equal to those of a(D)mathcal Q_plus/minus.
One can justify that identity with finite spectral cutoffs and monotone
convergence of the positive sandwich. Thus (6) never cancels two
undefined positive traces.

For completeness, the existing g is C4 rather than smooth, so a finite
regularity extension is needed. The sixth distributional derivative of
x^j g is a finite compactly supported measure for every nonnegative
integer j. Integration by parts gives

\[
\partial_t^j\widehat g(t)=O_j((1+|t|)^{-6}).
\tag{7}
\]

For fixed S, derivatives of v_S grow at most as powers of log(2+|t|).
For w=a_g or w=a_g v_S, derivatives of t^k w through any fixed finite
order are integrable when k<=4. Integrating by parts eight times shows
that the inverse kernels h_w have four continuous derivatives satisfying
h_w^(k)(u)=O((1+|u|)^(-8)), k<=4.

Here is a direct trace-class justification for the resulting Hankel
blocks. Extend h_w(x+z), x,z>=0, by multiplying by smooth cutoffs that
are one on [0,infinity) and zero on (-infinity,-1]. For the harmonic
oscillator H_osc=-d squared/dx squared+x squared+1, the kernel obtained
by applying H_osc,x H_osc,z lies in L2(R squared), by the preceding
derivative and decay bounds. If A is its Hilbert--Schmidt operator,
the extended block is H_osc^(-1) A H_osc^(-1). The inverse oscillator
is Hilbert--Schmidt, with squared norm pi squared/24; hence this block
is trace class. Compression gives [P,w(D)] in S1. The identity

\[
\mathcal Q a_g(D)=V^*[P,(v_Sa_g)(D)]-[P,a_g(D)]
\tag{8}
\]

establishes a_g(D)mathcal Q in S1 by taking adjoints. It also establishes
the positive clipped traces. Translated pairs have the same decay with
constants depending on r. Smooth frequency cutoffs converge in these
finite kernel norms, proving the diagonal trace identity as well.
All these constants are fixed-S, fixed-r finiteness statements, not
uniform bounds along the growing family.

## 4. Why every full positive ambient split loses exponentially

In this section S captures all active primes of the source; otherwise
the same inequalities use Q_S in place of Q. Let
Z_F=C_F mathcal Q C_F*, a selfadjoint trace-class operator. In the
Fourier convention dt/(2pi), the diagonal trace identity and a bounded
real multiplication test h(D) give

\[
\operatorname{Tr}(h(D)Z_F)
=-\int h(t)|\widehat F(t)|^2\phi'_S(t)\frac{dt}{2\pi}.
\]

First take smooth compact h with |h|<=1, then approximate sign(phi'_S)
on a fixed compact frequency interval J. Trace-norm duality gives

\[
\|Z_F\|_1\ge
\int_J |\widehat F(t)|^2|\phi'_S(t)|\frac{dt}{2\pi}.
\tag{9}
\]

On the other hand the decomposition into the two positive clipped
sandwiches gives

\[
\|Z_F\|_1\le P_S[F]+E_S[F]=Q[F]+2E_S[F].
\]

Consequently

\[
\boxed{E_S[F]\ge\tfrac12
\left(\int_J |\widehat F(t)|^2|\phi'_S(t)|\frac{dt}{2\pi}-Q[F]\right).}
\tag{10}
\]

The same argument applies to any splitting -mathcal Q=A-D with
positive ambient operators A,D and legitimate source-smoothed traces:
the loss Tr(C_F D C_F*) must satisfy (10). Neither spectral clipping
nor another positive ambient splitting can circumvent it.

### The growing-prime asymptotic

Put S_X={p:p<=X}, R=log X. Its phase derivative is

\[
\phi'_X(t)=\gamma_\infty(t)
-2\Re\sum_{p\le X}\sum_{m\ge1}
                   (\log p)p^{-m(1/2+it)}.
\]

The ordinary prime number theorem, in the form theta(u)=u+o(u), and
partial summation imply, uniformly on every fixed bounded t interval,

\[
\sum_{p\le X}(\log p)p^{-1/2-it}
=\frac{X^{1/2-it}}{1/2-it}+o(\sqrt X).
\tag{11}
\]

Indeed the error term from partial summation is bounded by
X^(-1/2)|theta(X)-X| plus
O_T(integral_2^X |theta(u)-u|u^(-3/2)du), both o(sqrt X).
The m>=2 terms are bounded uniformly in t by
sum_(p<=X) log(p)/(p(1-p^(-1/2)))=O(log X), using theta(u)=O(u).
The bounded archimedean multiplier on that interval is negligible.
Thus

\[
\phi'_X(t)=-2\sqrt X\Re\frac{e^{-iRt}}{1/2-it}
                         +o(\sqrt X).
\tag{12}
\]

Only ordinary PNT is imported here; see
[NIST DLMF 27.12](https://dlmf.nist.gov/27.12).
No improved prime-counting remainder is asserted.

Choose any fixed compact interval J of positive length on which
a_g(t)=|ghat(t)| squared has positive integral. With
theta_0(t)=arctan(2t), the absolute leading oscillation in (12) is

\[
\frac{2\sqrt X}{\sqrt{1/4+t^2}}
                 |\cos(Rt-\theta_0(t))|.
\]

The absolutely convergent Fourier series of |cos|, or approximation by
trigonometric polynomials and the Riemann--Lebesgue lemma, gives

\[
\lim_{X\to\infty}\frac1{\sqrt X}
\int_J a_g(t)|\phi'_X(t)|\frac{dt}{2\pi}
=\frac4\pi\int_J\frac{a_g(t)}{\sqrt{1/4+t^2}}\frac{dt}{2\pi}>0.
\tag{13}
\]

Since ell<log 2, Q[g]=q is independent of S_X. Equations (10)--(13)
therefore force E_(S_X)[g]>=c_J sqrt(X) for sufficiently large X,
with c_J>0.

For the moving pair with r=R-ell,

\[
|\widehat F_r(t)|^2=a_g(t)(1+\cos(rt)).
\tag{14}
\]

Multiplication by the second term in (14) does not change the limit in
(13). The harmonics of |cos(Rt-theta_0(t))| have frequencies 2kR;
combining them with plus or minus (R-ell) leaves a frequency tending
to infinity for every integer k. Absolute convergence of that Fourier
series permits uniform truncation before applying Riemann--Lebesgue.

Preparation and ordinary PNT also give M_g(r)=o(exp(r/2)). For primes,
partial summation on the fixed-ratio moving window replaces theta(dp)
by dp with o(exp(r/2)) error, and the continuous main term is exactly
exp(r/2)Phi(1/2)=0. Squares have canceled main term and o(1) remainder;
higher powers are o(1), as proved in the existing one-sided note.
Equation (1) therefore gives Q[F_r]=o(sqrt(mathsf X_r)). Applying (10) yields

\[
\boxed{E_{S_r}[F_r]\ge c_J e^{r/2}\quad\text{for all sufficiently large }r.}
\tag{15}
\]

More precisely its liminf divided by sqrt(mathsf X_r) is at least
(2/pi) integral_J a_g(t)/sqrt(1/4+t squared) dt/(2pi)>0.
This is an unconditional asymptotic bound, not an effective first
separation or a numerical certificate.

Although 0<=a_r<=2a_g gives E_(S_r)[F_r]<=2E_(S_r)[g], that useful
positive comparison cannot supply a subexponential bound: both losses
already have the obstruction (15). The full ambient split has removed
an inverse-gap constant by replacing signed channel cancellation with
an exponential positive/negative trace cancellation. This rules out
this particular way of implementing the user's proposal, not the
proposal itself.

## 5. The source crossing strip has only linear nuclear growth

There is a separate exact geometric calculation relevant to any more
selective return estimate. Put phi=autocorrelation(g), a_g=|ghat| squared,
and X_r=P a_r(D) chi. For r>ell its kernel is

\[
X_r(x,y)=\phi(x-y)+\tfrac12\phi(x-y-r),\qquad x>0>y.
\tag{16}
\]

The omitted term phi(x-y+r) is zero. The remote part is supported on
x-y in [r-ell,r+ell], rather than on the whole crossing triangle.
For r>2ell, the local and remote strips are disjoint, and

\[
\|X_r\|_{\rm HS}^2
=\int_0^\ell u\phi(u)^2du+\frac r4\|\phi\|_2^2.
\tag{17}
\]

The exact crossing factorization from the closed-source note gives
the upper bound ||X_r||_1<=(r+ell)/2. For a lower bound translate the
negative input y=z-r and compress both z and x to
I=(ell/2,r-ell/2). The local term vanishes and the compression equals
one half of 1_I a_g(D)1_I, a positive operator with trace (r-ell)/2
because phi(0)=1. Compression cannot increase trace norm. Therefore

\[
\boxed{(r-\ell)/2\le\|X_r\|_1\le(r+\ell)/2.}
\tag{18}
\]

Thus smoothing and all three moments do not reduce the nuclear norm
below linear growth. Linear growth itself is compatible with the
desired subexponential remainder; the old absolute return estimate
multiplies it by a gap constant that deteriorates with S. Neither
(18) nor a small operator norm proves a signed boundary bound.

## 6. Selective absorption at the relative source threshold

Fix S,L and the closed three-moment source space with its logarithmic
form domain V. Use the internally proved positive source operator
B>=beta_L I, bounded correction K, and compact selfadjoint

\[
H=B^{-1/2}KB^{-1/2},\qquad v=B^{1/2}F.
\]

These are established in the
[closed-source analysis](CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md)
and [general-window audit](../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md).
Their arithmetic identification requires capture of all active primes.
The exact form identity is Q[F]=<v,(I-H)v>.

Instead of the earlier I-H_plus main term, whose positivity is the
unproved comparison, clip at the threshold one:

\[
P_{\rm rel}[F]=\langle v,(I-H)_+v\rangle\ge0,
\qquad E_{\rm rel}[F]=\langle v,(H-I)_+v\rangle\ge0.
\]

Then

\[
\boxed{Q=P_{\rm rel}-E_{\rm rel}.}
\tag{19}
\]

The main is independently nonnegative for every fixed S,L, whether
or not Q is positive. Because H is compact, only finitely many
eigenvalues exceed one. If He_j=lambda_j e_j, normalized, then

\[
E_{\rm rel}[F]=\sum_{\lambda_j>1}(\lambda_j-1)
                  |\langle B^{1/2}e_j,F\rangle|^2.
\tag{20}
\]

The vectors B^(1/2)e_j exist: for lambda_j nonzero,
e_j=lambda_j^(-1) B^(-1/2)K B^(-1/2)e_j lies in V. Thus (20) is a
bounded finite-rank quadratic form on ordinary source L2, not merely
a finite-rank operator on the relative coordinate v. If ||K||<=k,

\[
\|B^{1/2}e_j\|\le\frac{k}{|\lambda_j|\sqrt{\beta_L}},
\qquad
\operatorname{Tr}E_{\rm rel}
\le\frac{N_H(1)k^2}{4\beta_L}.
\tag{21}
\]

The latter uses (lambda-1)/lambda squared<=1/4. It proves fixed-window
finiteness only. Current bounds on k, beta_L and the eigenvalue count
do not make (21) subexponential along growing windows. It should not
replace the actual source overlaps in (20).

This construction is different from the ambient splitting in Section 4:
it splits the compressed relative source operator after signed boundary
cancellation. It does not provide a positive ambient decomposition of
-mathcal Q, so (15) is no obstruction to it. Its remaining loss still
carries the unresolved arithmetic difficulty. Under RH that exact loss
is zero at every support-adapted window; its vanishing is not assumed.

## 7. A finite, source-weighted excess certificate

Suppose J is a finite-rank selfadjoint approximation with the **full**
relative operator error

\[
\|H-J\|\le\eta<1.
\tag{22}
\]

Put c=1-eta>0 and define

\[
A_J=(cI-J)_+\ge0,\qquad D_J=(J-cI)_+\ge0.
\]

D_J has finite rank, since it vanishes on the complement of Ran J.
The operator inequality H<=J+eta I gives

\[
I-H\ge cI-J=A_J-D_J.
\]

Consequently the independently positive main term
P_J[F]=<v,A_Jv> satisfies

\[
\boxed{Q[F]-P_J[F]\ge-\mathcal L_J[F],\qquad
\mathcal L_J[F]=\langle v,D_Jv\rangle.}
\tag{23}
\]

No operator-monotonicity of the positive-part function is used here.
In fact G_J=eta I-(H-J)>=0 gives the exact decomposition

\[
Q[F]=P_J[F]+\langle v,G_Jv\rangle-\mathcal L_J[F].
\]

Thus the first two terms together are an independently positive main
once (22) is established; evaluating them is unnecessary for the lower
bound (23).
If J e_j=lambda_j(J)e_j, the loss is

\[
\mathcal L_J[F]=
\sum_{\lambda_j(J)>1-\eta}
(\lambda_j(J)-1+\eta)
|\langle e_j,B^{1/2}F\rangle|^2.
\tag{24}
\]

To make it a bounded L2 source form require Ran J contained in V;
then the overlaps are <B^(1/2)e_j,F>. An ordinary operator-norm
approximation alone does not certify those source energies. They need
their own full-column or form-norm enclosures.

The previously proved mixed-column approximations are legitimate
candidates. If E_n is the exact first-n-mode B spectral projection,

\[
J_n=E_nH+HE_n-E_nHE_n,\qquad
\operatorname{rank}J_n\le2n,\qquad
\|H-J_n\|\le k/b_{n+1}.
\tag{25}
\]

Their ranges lie in V, since B eigenvectors do and H maps the source
Hilbert space into V. Both the actual spectral subspace and the full
columns H E_n must be certified; a numerical head cannot simply be
declared to be E_n. Plain compression omits the mixed columns and
does not give (25). These inherited facts are recorded in
[effective relative tails](ALL_WINDOW_EFFECTIVE_RELATIVE_TAILS_20261003.md).

For the moving pair, one concrete sufficient target is

\[
\boxed{\mathcal L_{J_r}[F_r]
=O_\varepsilon(e^{\varepsilon r})
\quad\text{for every }\varepsilon>0,}
\tag{26}
\]

with (22) established for each sufficiently large real r, S_r capturing
all active primes, and (24) retaining the source-weighted overlaps.
Equations (1), (23), and the one-sided theorem then imply RH. The
certificate need not establish lambda_max(J_r)+eta_r<=1: approximate
supercritical modes are permitted if their weighted loss meets (26).
The chosen eta<1 retains a strictly positive complementary main term.
At eta=1 the complementary main term vanishes and D_J=J_plus is still
finite rank. If eta>1, c<0 and the complementary block gives an
infinite-rank loss.

## 8. A gap-free primal residual estimate

There is also a concrete improvement to the inherited boundary residual
certificate that can support a later selective calculation. Write
A_boundary=TT*=I-C squared and factor a finite crossing approximation
X_N=V_0 W_0*. For approximate primal and dual columns Y,Z, the exact
identity in the [boundary residual note](FINITE_EULER_BOUNDARY_RESIDUAL_CERTIFICATE_20261003.md)
has residuals

\[
r_b=TV_0-A_{\rm boundary}Y,
\qquad r_d=CW_0-A_{\rm boundary}Z,
\]

and corrected-scalar error
2 Re <r_d,A_boundary^(-1)r_b>_HS. The primal residual factors as

\[
r_b=T(V_0-T^*Y).
\]

Since A_boundary^(-1/2)T is a coisometry, its norm is one. Therefore

\[
\boxed{\|A_{\rm boundary}^{-1/2}r_b\|_{\rm HS}
\le\|V_0-T^*Y\|_{\rm HS}.}
\tag{27}
\]

More precisely the weighted residual norm equals
||(P-Pi)(V_0-T*Y)||_HS. The unprojected bound (27) can retain a
Sonin component annihilated by T and therefore be pessimistic.

This yields the improved full-residual bound

\[
|K_N-\widehat K_N|
\le2\|V_0-T^*Y\|_{\rm HS}
       \|A_{\rm boundary}^{-1/2}r_d\|_{\rm HS}.
\tag{28}
\]

If a dual preimage r_d=T e_d is explicitly supplied and its full norm
is controlled, the right side can instead be bounded by
2||V_0-T*Y||_HS ||e_d||_HS, with no scalar inverse gap. Onto-ness of T
guarantees existence of a preimage at each fixed S, but does not give
the required uniform bound. Choosing the canonical preimage by an
uncontrolled inverse merely hides the gap. Source truncation error and
finite evaluation error must still be included. No residual norms are
computed here.

## 9. What remains to be learned before a larger computation

The constructive distinction is now precise. A positive state-space
split pays exponential absolute phase mass. A source-level split can
retain the cancellations, but requires source-weighted information on
the small set of correction modes exceeding the energy threshold.
The number of those modes may grow; no uniform rank is asserted or needed
by the sufficient criterion.

At the two already certified local windows the exact excess in (20) is
zero, as a consequence of the known arithmetic positivity. Repeating
that fact would not supply a new geometric mechanism. Existing absolute
gap and counting estimates do not justify a large spectral computation.

The useful next bounded task is to obtain a rigorous bound on the
source-weighted excess (24), or a joint completion-of-squares estimate
that bounds the same loss without resolving every B eigenvector. The
dual lifting in (28) provides a concrete boundary-level target for such
a calculation. These estimates must retain mixed channels, the inverse
compressed metric, and all active shifts. Their hypotheses, residuals
and continuous-r coverage must be explicit. No such global estimate or
numerical source-excess certificate is claimed in this note.

The [internal review](../reviews/POSITIVE_CHANNEL_ABSORPTION_REVIEW_20261003.md)
records the cross-checks, scope restrictions, and file validation.
