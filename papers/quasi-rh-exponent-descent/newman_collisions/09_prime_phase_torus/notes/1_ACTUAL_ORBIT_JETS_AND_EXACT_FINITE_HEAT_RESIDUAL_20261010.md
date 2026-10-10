# Actual orbit jets and the exact finite heat residual

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. This scout and review are internal
LLM work, not independent mathematical validation.

This implements direction 09 of [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The additional initial results are the exact candidate-conditioned curvature
identity for the actual coupled orbit and a closed formula for the finite
approximant's heat-equation residual. They identify signed log moments and
normalizer terms that an orbit argument must control. Neither formula has
the missing exclusion sign.

## 1. State, orbit, generator, and readout

Choose `kappa in [1,3/2]`, `0<t<=1/20`,
`L=kappa/t`, `x=4 pi exp(L)`, and the manuscript's natural integer cutoff
`N=floor(sqrt(exp(L)+t/16))`. On a local neighborhood freeze that integer
cutoff and time; `L` remains the scale at its center. The relative block
tested below is `N/2<n<=N`, with every complementary term retained.

Let `Z_p=exp(i T log p)` with `T=(x-t alpha_i)/2`, and put

\[
\mathcal P_{t,x}(Z)=\sum_{n\le N}w_n\prod_{p\le N}Z_p^{\nu_p(n)},
\quad S=e^{i\theta_t}\mathcal P_{t,x}(Z),\quad
S_z=e^{i\theta_t}\sum_{n\le N}w_nz_n\prod_pZ_p^{\nu_p(n)}.
\tag{1}
\]

Here `w_n,theta_t,r_n,c_n` are exactly the manuscript's common-height
data and `z_n=r_n-i c_n`. The reduction is
`V_N=(Re S,Im S_z)=(F_N/2,2F_N'/L)`. The enlarged space is the finite
monomial span in the prime torus, with its Haar `L^2` norm. The arithmetic
initial data comprise all integers and composites up to `N`, together
with their actual weights and the reflected carrier. The admissible
physical states form the coupled orbit (1), not the full torus with
arbitrarily frozen coefficients.

Unique prime factorization gives (1) directly. The established Bohr/torus
framework is discussed in [Bailleul–Lefevre, introduction](https://www.impan.pl/shop/en/publication/transaction/download/product/90280).
No external almost-periodicity theorem or quantitative density assertion
is used in the results below.

For `D=sum_{p<=N} log p partial_{arg Z_p}`, a monomial has
`D=i log n` and `D^2=-log^2 n`. The heat coefficient is thus generated
by `-D^2/4`, the backward torus-heat sign. On this finite span it is a
bounded operator. On the infinite torus span its positive-time exponential
is unbounded; a finite-polynomial identity is not an infinite semigroup
construction. Physical evolution also moves `T`, the weights, and carrier.

## 2. Exact raw spatial jets along the orbit

Use `alpha'=U+iV`, `d=tV/4`, and

\[
c=\tfrac12(1+tU/2),\quad
\Omega=\tfrac12\Re\{\alpha(1+t\alpha'/2)\},\quad
a=-i\Omega,\quad\beta=-d+ic.
\]

For `q_n=w_n exp(i phi_n)` one has exactly

\[
q_n'=(a+\beta\ell_n)q_n,\qquad \ell_n=\log n.
\tag{2}
\]

The real part `-d ell_n` is the amplitude drift. All derivatives in this
note hold `t,N` fixed. Put `v_n=a+beta ell_n`; its four raw multipliers are

\[
1,\quad v_n,\quad v_n^2+v_n',\quad
v_n^3+3v_nv_n'+v_n'',\quad
v_n^4+6v_n^2v_n'+3(v_n')^2+4v_nv_n''+v_n'''.
\tag{3}
\]

Summing `2 Re(q_n times multiplier)` gives `F_N^{(j)}`, `0<=j<=4`.
The torus-coordinate evolution is `Z_p'=ic log p Z_p`; coefficient
movement adds `-d log n`, and carrier movement adds `-i Omega`.
Consequently the raw derivative is not just a derivative of a polynomial
at torus phases with its coefficients held still.

Define the signed logarithmic moments

\[
C_j=\sum_{n\le N}w_n\ell_n^j\cos\phi_n,\qquad
Y_j=\sum_{n\le N}w_n\ell_n^j\sin\phi_n.
\]

Then

\[
F_N/2=C_0,\qquad F_N'/2=\Omega Y_0-cY_1-dC_1,
\tag{4}
\]

and exact differentiation yields

\[
\begin{split}
F_N''/2={}&-\Omega^2C_0+\Omega'Y_0
 +(2\Omega c-d')C_1-(2\Omega d+c')Y_1\\
 &+(d^2-c^2)C_2+2dcY_2.
\end{split}
\tag{5}
\]

At an exact finite candidate `F_N=F_N'=0`, equations (4) imply
`C_0=0` and `Omega Y_0=cY_1+dC_1`, but do not imply `S=0` or
`S_z=0`. Hidden imaginary and real quadratures remain. Formula (5) is
an explicit candidate-conditioned curvature identity. It places the
uncontrolled signed second log moments next to the actual drift terms;
it does not force curvature to be small or of one sign.

At a genuine heat collision the paid candidate is approximate. Replace
`C_0=0` in (5) by `|C_0|<=eta_N/2` and (4)'s zero by
`|Omega Y_0-cY_1-dC_1|<=eta_N L/2`. The resulting discarded curvature
term has the measured bound `Omega^2 eta_N/2`. Keeping it explicitly is
essential. This is an algebraic identity at actual phases, not a numerical
survey of possible candidates.

## 3. The finite heat residual, including the normalizer

Write the unnormalized minus-branch summand as

\[
b_n(s,t)=\exp\{m_0(s)-s\ell_n+\tfrac t4(\alpha(s)-\ell_n)^2\},
\quad m_0'=\alpha,\quad s=(1-ix)/2.
\]

With `h=alpha-ell_n`, `B=1+t alpha'/2`, direct differentiation gives

\[
\partial_t b_n-\tfrac14\partial_s^2b_n=R_n b_n,
\qquad
R_n=\tfrac14\left[h^2(1-B^2)-\alpha'B-\tfrac t2h\alpha''\right].
\tag{6}
\]

The plus branch uses `s -> 1-s`. Since both branches have
`partial_x^2=-partial_s^2/4`, their sum satisfies

\[
\partial_tG_N+G_N''=R_G,
\quad R_G=\sum_{n\le N}\{R_n(s)b_n(s)+R_n(1-s)b_n(1-s)\}.
\tag{7}
\]

Already at `t=0`, `R_n=-alpha'/4`. The finite approximant therefore
does not obey the exact scalar heat equation. It is an approximation to
the genuine heat solution, not a heat-invariant finite torus manifold.

For the actual analytic normalizer `A=A_t(x)`, set
`b=A'/A` and `rho=A''/A+partial_t A/A`. Equations (7) and `G=AF` give

\[
\partial_t F_N=-F_N''-2bF_N'-\rho F_N+R_G/A,
\qquad
\partial_t Q=-Q''-2bQ'-\rho Q.
\tag{8}
\]

Both sides use the same normalization and time orientation. Formula (8)
is the exact price of proposing autonomous finite-torus dynamics. No
uniform bound on the time derivative of the approximation remainder is
claimed from a spatial Cauchy estimate. A new dynamical argument would
need to pay `R_G` or prove its required signed cancellation directly.

## 4. Block correlations and the actual stopping point

Split the full projected vector as `V_N=A_core+B_edge`, using the stated
relative block. Orthogonality in Haar torus norm yields useful averages,
but at one physical height

\[
|V_N|^2=|A_{\rm core}|^2+|B_{\rm edge}|^2
 +2A_{\rm core}\!\cdot B_{\rm edge}.
\tag{9}
\]

At a paid candidate, `|V_N|^2<=epsilon^2`,
`epsilon^2=17 eta_N^2/4`, so necessarily

\[
2A_{\rm core}\!\cdot B_{\rm edge}
\le\epsilon^2-|A_{\rm core}|^2-|B_{\rm edge}|^2.
\tag{10}
\]

Thus the missing information is precisely a restriction preventing this
adverse cross correlation at the same actual height. Positive separate
block norms, Haar orthogonality, and retaining every composite supply no
such restriction. The manuscript's complete multiplicative-twist zero
construction refutes a lower bound uniform on the unrestricted torus;
it does not settle the narrower moving physical orbit considered here.

Formula (5) offers a bounded continuation: impose the two paid candidate
conditions on a closed subinterval of `kappa`, retain the complete cutoff,
and seek a signed relation involving `C_2,Y_2` and the corresponding third
and fourth log moments from (3). A theta Ward relation from program 06 or
the global-character restriction from program 08 would need to constrain
these *actual* moments. A threshold application must keep `gamma` and
the measured quadratic payment `Delta` from Note 13, and cover higher
multiplicity separately. Spatial jet errors remain
`j! L^j eta_N`; formulas (3) and (8) do not reduce those payments by fiat.

The scout reaches exact orbit representation, one candidate-conditioned
identity, and an exact finite-dynamics mismatch. It proves no paid opposite
threshold sign, pointwise joint lower bound, collision exclusion, or RH
conclusion. A new arithmetic constraint beyond the printed identities
remains the continuation's required output.

The [checker](../numerics/check_prime_torus_scout.py) verifies the raw-jet
recurrence, drift-containing curvature identity, finite heat residual,
prime monomial encoding, and correlation partition on exact rational
formal models. It does not evaluate the genuine heat function at the
exponentially large center or certify a new actual-phase sign.
