# A regularized positive family and its singular critical limit

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed. This is an exploratory internal derivation, not specialist
refereeing. No expensive numerical calculation was performed.

## Outcome and scope

**Later continuation:** [uniform frequency tails](SONIN_PHASE_FREQUENCY_TAILS_20260929.md)
now prove full source-smoothed trace finiteness for every sigma>1/2, beyond
the bounded transport region considered here. The
[critical-limit synthesis](SONIN_CRITICAL_LIMIT_STATUS_20260929.md)
records the remaining exact-projection defect and arithmetic discrepancy.
The open-finiteness statements below are retained as the historical scope
of this initial regularization argument.

For every real sigma greater than 1, the regularized finite-place transports
have an unconditional bounded invertible operator-norm limit. Their actual
Sonin projections converge in operator norm, and their fixed-source positive
trace operators converge in trace norm. This constructs a genuine
infinite-place positive family in the absolute-convergence region.

It does not identify that family with the complete critical arithmetic form.
The regularization must eventually be removed, and this cannot be treated
as ordinary Hilbert--Schmidt continuity to one endpoint projection. A natural
phase continuation has an especially informative endpoint: its deformed
Fourier involution becomes plain logarithmic reflection at sigma=1/2, so
the endpoint Sonin projection is zero, and the approaching projections
converge strongly to zero. Any nonzero arithmetic trace limit would have
to retain spectral concentration despite that strong collapse.

The companion [topology and scope review](SONIN_POSITIVE_LIMIT_TOPOLOGY_20260929.md)
proves why one fixed bounded compression cannot realize the global arithmetic
form. The [main program note](SONIN_DIRECT_POSITIVE_LIMIT_PROGRAM_20260929.md)
places the constructions below within the proposed direct-limit investigation.

## 1. Bounded infinite-place limit for sigma greater than 1

Work on the logarithmic Hilbert space H=L2(R), with
U_a h(x)=h(x-a), Fourier convention Fhat(t)=int F(x)exp(-itx)dx, and the
actual cutoff-1 Sonin projection Pi onto K. For a compact smooth source F,
the existing canonical audit supplies the Hilbert--Schmidt map
V_F=C_F Pi:K -> H.

For a prime cutoff R and real sigma>1 define

\[
D_{R,\sigma}=\prod_{p\le R}(I-p^{-\sigma}U_{\log p}),\qquad
A_{R,\sigma}=\Pi D_{R,\sigma}^*D_{R,\sigma}\Pi|_K.
\]

The sum of p^(-sigma) converges. Consequently D_R and its inverses converge
in operator norm. The limiting multiplier is

\[
d_\sigma(t)=\prod_p(1-p^{-\sigma-it})=\frac1{\zeta(\sigma+it)}.
\tag{1}
\]

The Euler product and its region of validity are stated in
[DLMF 25.2.11](https://dlmf.nist.gov/25.2.E11). The operator claim follows
directly by absolute summability of the translation coefficients; it uses
no zero-location assumption.

Put

\[
\ell_\sigma=\prod_p(1-p^{-\sigma})=\zeta(\sigma)^{-1},\qquad
u_\sigma=\prod_p(1+p^{-\sigma})=\frac{\zeta(\sigma)}{\zeta(2\sigma)}.
\]

For both finite and limiting transports,

\[
\|D\|\le u_\sigma,\qquad \|D^{-1}\|\le\ell_\sigma^{-1},\qquad
\ell_\sigma^2 I\le A\le u_\sigma^2 I.
\tag{2}
\]

A useful coarse tail bound is

\[
\delta_R:=\|D_{R,\sigma}-D_\sigma\|
\le u_\sigma\sum_{p>R}p^{-\sigma}.
\tag{3}
\]

For integer R the final sum is at most R^(1-sigma)/(sigma-1), by comparison
with the integer sum and its decreasing integral. This is a convergence
bound, not an efficient near-critical estimate.

## 2. Fixed-source smoothing survives the infinite-place limit

Set A_sigma=Pi D_sigma*D_sigma Pi on K and

\[
J_{R,\sigma}=D_{R,\sigma}\Pi A_{R,\sigma}^{-1/2},\qquad
J_\sigma=D_\sigma\Pi A_\sigma^{-1/2}.
\]

These are isometries from K, and P_R=J_R J_R*, P_sigma=J_sigma J_sigma*
are the ordinary orthogonal projections onto the transported Sonin spaces.
Since

\[
\|A_R-A\|\le2u_\sigma\delta_R,
\]

the integral representation of x^(-1/2), with the lower bound in (2), gives

\[
\|A_R^{-1/2}-A^{-1/2}\|
\le\frac{\|A_R-A\|}{2\ell_\sigma^3}.
\]

Thus, writing c_sigma=ell_sigma^(-1)+u_sigma^2 ell_sigma^(-3),

\[
\|J_R-J\|\le c_\sigma\delta_R.
\tag{4}
\]

All transports commute with C_F. Therefore

\[
Y_{R,F}:=C_FJ_R=D_RV_FA_R^{-1/2},\qquad
Y_{\sigma,F}:=C_FJ_\sigma=D_\sigma V_FA_\sigma^{-1/2},
\]

and the same computation in Hilbert--Schmidt norm yields

\[
\|Y_{R,F}-Y_{\sigma,F}\|_{\rm HS}
\le c_\sigma\delta_R\|V_F\|_{\rm HS}.
\tag{5}
\]

In particular the actual positive trace operators

\[
C_FP_R C_F^*=Y_{R,F}Y_{R,F}^*
\]

converge in trace norm, because

\[
\|Y_{R,F}Y_{R,F}^*-Y_{\sigma,F}Y_{\sigma,F}^*\|_1
\le2(u_\sigma/\ell_\sigma)c_\sigma\delta_R\,
\mathcal B_\infty[F].
\tag{6}
\]

This proves convergence of the positive quadratic forms
B_R,sigma[F]=||Y_R,F||_HS^2 to B_sigma[F]>=0. Polarization gives mixed
forms. The estimates are uniform for sigma in any interval bounded away
from 1 on the right. They do not justify removing the regularization.

## 3. Where arithmetic identification is still missing

The archimedean calibration remains

\[
\mathcal B_\infty[F]=\Gamma[F]+\mathcal E_\infty[F].
\]

Changing the prime transport weights does not change this real-place error.
For fixed compact source support, define the finite arithmetic sum

\[
\mathcal W_{\sigma,L}[F]
=\sum_{m\log p<L}(\log p)p^{-m\sigma}
\{\kappa_F(m\log p)+\kappa_F(-m\log p)\}.
\]

On pole-neutral sources, Q_sigma,L=Gamma-W_sigma,L is a useful artificial
deformation whose fixed-test limit at sigma=1/2 is the desired arithmetic
form. It must not be confused with the full shifted completed-zeta form:
shifting that completed function also affects its archimedean and pole
normalizations.

The finite-place comparison algebra applies unchanged for these weights:

\[
Q_{\sigma,L}=B_{R,\sigma}+R_{R,\sigma,L},\qquad
R_{R,\sigma,L}=-E_\infty-\Delta_{R,\sigma}-W_{\sigma,L}.
\tag{7}
\]

Every active prime is retained in W, irrespective of the chosen geometric
cutoff. Once R exceeds the active primes, increasing R changes B and Delta
but changes no term of W. Equations (3)--(6) give convergence of Delta for
sigma>1, not cancellation of the right side of (7).

The modified prime weights do occur naturally in the transport phase:

\[
\frac{d}{dt}\arg\frac{d_{R,\sigma}(t)}{\overline{d_{R,\sigma}(t)}}
=2\sum_{p\le R}(\log p)\sum_{m\ge1}p^{-m\sigma}
\cos(mt\log p).
\tag{8}
\]

For sigma>1 the differentiated series converges absolutely. This records
the correct local coefficients, but does not control the compression error
of the positive trace. In particular B_sigma tends to B_infinity, not Gamma,
as sigma tends to infinity; the nonzero real-place error is already visible
before any difficult infinite-prime question.

To prove the desired arithmetic limit one still needs an independent signed
comparison or a theorem showing the complete residual in (7) disappears
on every admissible fixed test under a valid limiting prescription. Writing
that requirement down is not a proof of it.

## 4. Loss of the safe operator topology

The bounds deteriorate already at sigma down to 1:
ell_sigma=1/zeta(sigma) tends to zero, and u_sigma tends to infinity. In fact
d_sigma(0)=1/zeta(sigma) tends to zero. The simple pole and residue are
recorded in [DLMF 25.2](https://dlmf.nist.gov/25.2.i).

The ordinary Euler product outside its absolute-convergence region cannot
be substituted for analytic continuation as a bounded multiplier argument.
Using 1/zeta(sigma+it) farther left raises genuine unbounded-operator and
domain questions; if a zero lies on the chosen line, its reciprocal has a
pole. One must not assume a zero-free half-plane to prove the desired RH
implication. Conversely, a failure of uniform invertibility at sigma=1 is
not by itself an impossibility theorem for a singular form limit.

At one fixed prime a related phenomenon is explicit. With r=p^(-sigma),

\[
\chi D_p\mathcal F_\infty D_p^{-1}\chi
=(1-r^2)\sum_{n\ge0}r^n\chi U_{-n\log p}\mathcal F_\infty\chi
-r\chi U_{\log p}\mathcal F_\infty\chi.
\]

The Hilbert--Schmidt norms of the summands are bounded by
2 r^n p^(n/2), so the displayed series converges in Hilbert--Schmidt norm
for sigma>1/2. At sigma=1/2 that bound ceases to sum, consistent with the
previously proved non-Hilbert--Schmidt critical cutoff. This is a statement
about one finite prime, not an all-prime convergence theorem.

## 5. Unconditional phase continuation and exact endpoint collapse

There is a well-defined phase construction even when the reciprocal zeta
multiplier is not bounded. In Fourier coordinates the fixed real-place
cosine involution has the form

\[
(\widehat{\mathcal F_\infty h})(t)
=e^{-2i\theta(t)}\widehat h(-t),\qquad
\theta(t)=\arg\Gamma(1/4+it/2)-(t/2)\log\pi.
\]

For real sigma define, almost everywhere,

\[
q_\sigma(t)=\frac{\overline{\zeta(\sigma+it)}}{\zeta(\sigma+it)},
\qquad
\mathcal F_\sigma=q_\sigma(D)\mathcal F_\infty.
\tag{9}
\]

Isolated zeros or the isolated pole do not affect the multiplier. Its modulus
is one and q_sigma(-t)=conjugate(q_sigma(t)), so F_sigma is a selfadjoint
unitary involution, without RH. Let R_+ denote the projection onto positive
logarithmic coordinates, and define P_sigma as the orthogonal projection
onto Ran R_+ intersect F_sigma Ran R_+.

For sigma>1 this P_sigma agrees with the transported-space projection above.
Indeed F_sigma=D_sigma F_infinity D_sigma^(-1), and both D_sigma and its
inverse preserve Ran R_+ by their absolutely convergent nonnegative-delay
Dirichlet series. This proves the equality of the two spaces in both
directions. For sigma<=1, (9) is a separate analytic phase continuation;
it has not been shown to be a limit of the corresponding finite-prime
projections. Its smooth traces have not been proved finite here.

The critical-line functional equation gives

\[
\frac{\overline{\zeta(1/2+it)}}{\zeta(1/2+it)}=e^{2i\theta(t)}
\quad\hbox{almost everywhere}.
\]

This follows also from the reality of the Hardy Z function in
[DLMF 25.10.1--25.10.2](https://dlmf.nist.gov/25.10.i), and uses no assumption
about off-line zeros. Consequently

\[
\mathcal F_{1/2}=\mathscr I,\qquad (\mathscr I h)(x)=h(-x),\qquad
P_{1/2}=0.
\tag{10}
\]

Dominated convergence of the unit-modulus multipliers gives
\(\mathcal F_\sigma\to\mathscr I\) strongly as sigma decreases to 1/2.
Writing S_sigma=F_sigma R_+ F_sigma, one has S_sigma -> I_H-R_+ strongly.
Because P_sigma<=R_+ and P_sigma<=S_sigma,

\[
\|P_\sigma v\|=\|P_\sigma S_\sigma R_+v\|
\le\|S_\sigma R_+v\|\longrightarrow0.
\tag{11}
\]

Thus the positive projections themselves collapse strongly. This does not
show that their smoothed scalar traces converge to zero: C_F is not a
globally Hilbert--Schmidt convolution operator, and trace mass may escape
while projections converge strongly to zero.

However, Hilbert--Schmidt convergence C_F P_sigma -> 0, or trace-norm
convergence of C_F P_sigma C_F*, would force the scalar trace to zero.
Such a convergence theorem would therefore be the wrong endpoint target
for a nonzero arithmetic form. The trace operators converge strongly to
zero already, so any trace-norm limit must be zero.

## 6. The legitimate remaining limit question

For any orthogonal projection P, choose an orthonormal basis e_n of its
range and set rho_P(t)=sum_n |ehat_n(t)|^2, allowing infinity. Tonelli gives
the exact smoothing criterion

\[
\|C_FP\|_{\rm HS}^2
=\int |\widehat F(t)|^2\rho_P(t)\,\frac{dt}{2\pi}.
\tag{12}
\]

The quantity is finite exactly when the right side is finite. This is a
positive frequency density at each ordinary projection. Singular limits
of these densities may be measures even when P_sigma tends strongly to
zero. They must not be excluded by demanding an ordinary endpoint factor.

For the phase continuation beyond sigma=1, the next obligations are:

1. Establish a legitimate smoothing/domain statement, or specify finite
   positive cutoffs whose forms are always finite.
2. Prove concentration of the positive frequency measures on fixed tests,
   with the needed weighted tails controlled.
3. Identify that limit with the **complete** arithmetic form, preserving
   the real-place term, every active prime power, and the chosen moment
   constraints, without assuming RH.

One completely defined joint family uses any fixed, source-independent,
nested sequence of finite-rank ambient orthogonal projections E_N converging
strongly to I_H. Set

\[
\mathcal P_{\sigma,N}[F]=\|C_F P_\sigma E_N\|_{\rm HS}^2,
\qquad \sigma>1/2.
\tag{13}
\]

These quantities are finite and positive for every source and every indicated
parameter, without any trace-class claim about C_F P_sigma. In an orthonormal
basis compatible with E_N, they are the partial sums of
sum_j ||C_F P_sigma e_j||_2^2, so they increase with N. For fixed sigma>1,
their N-to-infinity limit is precisely the certified B_sigma of Section 2.
For other sigma, the increasing limit may be infinite; finiteness has not
been proved here.

For every fixed N, equation (11) and boundedness of C_F give
P_sigma,N[F] -> 0 as sigma decreases to 1/2. A nonzero arithmetic limit
therefore requires a coupled N(sigma)-to-infinity prescription, or another
legitimate order of limits, with actual concentration and tail estimates.
It cannot be obtained by first setting sigma=1/2 at fixed N. No successful
coupling rule or arithmetic identification is supplied by this observation.

The sigma>1 theorem is therefore a useful control and baseline. The
critical challenge is a singular arithmetic concentration theorem, not
continued bounded invertibility, uniform finite-rank trace capture, or
Hilbert--Schmidt continuity to a fixed critical projection.
