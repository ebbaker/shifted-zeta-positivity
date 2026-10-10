# Exact carrier defect and the actual cutoff-edge mass

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed to this session
and is not inferred. This is an internal analytic derivation, not independent
mathematical validation. No external theorem is used beyond the explicitly
imported approximation interface in the project manuscript.

This continues [the paired-source bounds](9_PAIRED_CONTOUR_BOUNDS_ON_THE_SHRINKING_SECTOR_20261010.md) and [the stationary-sign target](5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md). The companion [current analysis](13_PHASE_CURRENTS_RELATIVE_CONES_AND_BANDWIDTH_OBSTRUCTION_20261010.md) gives a complex-channel interface; [the high-height calibration](15_NONVACUOUS_HIGH_HEIGHT_SECOND_STATIONARY_SIGN_20261010.md) pays one genuine branch.

## Result and scope

The complete finite travelling sum admits an exact second-order real
operator which kills its full prescribed Stirling carrier. At genuine `Hxx=0`, the desired
Laguerre sign is a scalar product between the physical slope and a specific
signed arithmetic defect. The defect contains every `n>=2` channel, all
physical drift, and a separately paid holomorphic error; it is not a frozen
frequency approximation.

There is also a concrete asymptotic obstruction to proving that defect small
by absolute weights or the `n=1` carrier alone. On the actual shrinking sector,
the absolute first-derivative mass is concentrated at a bounded logarithmic
distance below the natural cutoff. Its frequency distribution has a nonzero
limit, and the prescribed-carrier defect has asymptotically the same absolute mass
as the carrier's positive coefficient times that entire slope mass. Relative
to the `n=1` slope it grows exponentially. Thus the needed correction is a
signed cancellation problem already in the actual prescribed coefficients;
it is not a small perturbation of the first finite-sum carrier.

This does not establish the required stationary sign, exclude a vanishing
relative margin, or replace the modularly complete transform of Notes 9–10.

## 1. Exact real operator for the full carrier

Use the manuscript's fixed-cutoff dictionary at fixed time. All primes below
mean physical differentiation in `x` with `t,N` fixed, even when the resulting
quantities are evaluated on a shrinking-sector sequence. Write

\[
H=A Q,\qquad F=2\Re\sum_{n\le N}q_n,\qquad Q=F+e,
\]
\[
q_n=e^{i\theta}e^{t\ell_n^2/4-\sigma\ell_n+iT\ell_n},
\quad \ell_n=\log n,
\quad q_n'=(-i\Omega+h\ell_n)q_n,
\quad h=-d+ic,
\]
Here \(s=(1-ix)/2\), \(\alpha=\partial_s m_0\),
\(\sigma=1/2+t\Re\alpha/2\), \(T=(x-t\Im\alpha)/2\),
\(c=(1+t\Re\alpha_s/2)/2\), \(d=t\Im\alpha_s/4\), and
\(\Omega=\Re[\alpha(1+t\alpha_s/2)]/2\), using the prescribed
Stirling carrier \(m_t=m_0+t\alpha^2/4\) of the manuscript.
The symbol \(\alpha_s\) always means its derivative in \(s\).
The natural cutoff is \(N=\lfloor\sqrt{x/(4\pi)+t/16}\rfloor\),
frozen before taking spatial derivatives.
With `A>0`, `theta'=-Omega`, and `lambda=A'/A`, define

\[
\beta_n=\lambda-i\Omega+h\ell_n,\qquad
\rho=\frac{\Omega'}{\Omega},
\]
\[
a=2\lambda+\rho,\qquad
b=\lambda^2+\Omega^2+\lambda\rho-\lambda'. \tag{1}
\]
We work where `Omega != 0`; it is positive at all sufficiently large points
of the manuscript's sector. The real operator

\[
D=\partial_x^2-a\partial_x+b \tag{2}
\]
kills both real and imaginary parts of the prescribed carrier
`A exp(i theta)=exp(m_t(s))`. Indeed its logarithmic derivative is
`beta_1=lambda-i Omega`, and
`beta_1'+beta_1^2-a beta_1+b=0` by (1).

More usefully, for every smooth scalar `q`,

\[
D(Aq)=A\mathcal Dq,
\qquad \mathcal D=\partial_x^2-\rho\partial_x+\Omega^2. \tag{3}
\]
The exact individual channel defect is

\[
\mathcal Dq_n=E_nq_n,
\]
\[
\boxed{E_n=\ell_n\{h'+(-2i\Omega-\rho)h\}+\ell_n^2h^2.} \tag{4}
\]
In particular `E_1=0` exactly, without discarding any Stirling-carrier drift.
The complete finite-sum identity is

\[
D(AF)=2A\Re\sum_{n\le N}E_nq_n. \tag{5}
\]
Nothing in (4) gives a sign to the real part of this sum.

## 2. Exact genuine stationary identity

Set `R=DH`, and suppose `b != 0`. Differentiating (2), then using `H''=0`,
gives

\[
H'''=-(b-a')H'-b'H+R'.
\]
The stationary equation itself gives `bH=R+aH'`. Hence

\[
\boxed{\mathscr L_1(H)
=B H'^2-H'\mathcal R\quad\hbox{on }H''=0,} \tag{6}
\]
\[
B=b-a'+a\frac{b'}b,
\qquad \mathcal R=R'-\frac{b'}bR. \tag{7}
\]
These are exact identities for the genuine `H`. Define

\[
v=\lambda-\frac{b'}b,
\qquad Z_n=E_n'+\left(\beta_n-\frac{b'}b\right)E_n. \tag{8}
\]
Then the full approximation supplies

\[
\frac{\mathcal R}{A}
=2\Re\sum_{n\le N}Z_nq_n+\mathcal E,
\qquad
\mathcal E=(\partial_x+v)\mathcal D e. \tag{9}
\]
The `n=1` term vanishes in (9) also. Expanding the error operator,

\[
\mathcal E=e'''+(v-\rho)e''+
 (\Omega^2-\rho'-v\rho)e'
 +(2\Omega\Omega'+v\Omega^2)e. \tag{10}
\]
Thus the imported radius-`1/L` bound `|e|<=eta_N` pays

\[
|\mathcal E|\le \epsilon_R: =\eta_N\big[
6L^3+2|v-\rho|L^2+
|\Omega^2-\rho'-v\rho|L+
|2\Omega\Omega'+v\Omega^2|\big]. \tag{11}
\]
Likewise

\[
\left|\frac{H'}A-p_0\right|\le\epsilon_1=(L+|\lambda|)\eta_N,
\qquad p_0=2\Re\sum_{n\le N}\beta_nq_n. \tag{12}
\]
Let `r_0=2 Re sum Z_n q_n`. If `B>0`, `|p_0|>epsilon_1`, and

\[
\operatorname{sgn}(p_0)(Bp_0-r_0)
\ge B\epsilon_1+\epsilon_R, \tag{13}
\]
then (6) proves `L_1(H)>=0` at the genuine stationary point. This is a
sign-oriented sufficient criterion, not an absolute-smallness requirement.
The stronger but sometimes convenient requirement
`|r_0|+epsilon_R <= B(|p_0|-epsilon_1)` also suffices.

If `H'=0`, (6) already gives zero; no division by the potentially vanishing
physical slope occurs in (6). The finite certificate (13) nevertheless has
no automatic uniform reserve near a collision. Error estimates (11)–(12)
remain absolute, and cancellation must supply the required relative margin.

## 3. The leading frozen defect and what it removes

For `L=log(x/(4 pi))`, `t=kappa/L`, `1<=kappa<=3/2`, the exact elementary
formula for `alpha` in the manuscript gives, uniformly in `kappa`,

\[
\lambda=-\frac\pi8+O(x^{-1}),\quad
\Omega=\frac L4+O(t/x+x^{-2}),\quad
h=\frac i2+O(t/x),\quad
\rho=O((xL)^{-1}), \tag{14}
\]
\[
b=\frac{L^2}{16}+\frac{\pi^2}{64}+o(1),
\qquad B/b\longrightarrow1. \tag{15}
\]
These are physical derivatives at fixed `t`: one must not differentiate
`kappa=tL` as if it were fixed while constructing (1)–(13).

The leading channel frequency is `omega_n=L/4-ell_n/2`, and (4) reads

\[
E_n=\frac{L\ell_n-\ell_n^2}{4}+o(1)
=\frac{L^2}{16}-\omega_n^2+o(1) \tag{16}
\]
uniformly for `n<=N`. Here the `o(1)` is legitimate since the accumulated
error is `O(L^2 t/x+L/x)`, tending to zero. Formula (16) removes the
`n=1` carrier exactly at leading order, but its coefficient approaches the
full `L^2/16` at the natural cutoff where `omega_n` approaches zero. Thus
it cannot be called a uniformly small channel correction.

For completeness, the large-`x` inputs in (14) follow directly from

\[
\Re\alpha=\frac L2+\frac14\log(1+x^{-2})-\frac1{1+x^2},
\qquad
\Im\alpha=\frac{3x}{1+x^2}-\frac12\arctan x,
\]
\[
\alpha_s=\frac{i}{x}+O(x^{-2}),
\qquad
\lambda-i\Omega=-\frac i2\alpha(1+t\alpha_s/2).
\]
Differentiating these rational/logarithmic expressions supplies all the
bounds needed for (14)–(16), including `E_n'=O(L/x)` and `b'/b=O(1/(xL))`.

## 4. Exact cutoff-edge limit of the absolute coefficient masses

Let `w_n=|q_n|`, with the exact natural integer cutoff and exact `sigma`
from the manuscript. Define

\[
M_1=\sum_{n\le N}w_n|\beta_n|,
\qquad M_R=\sum_{n\le N}w_n|Z_n|.
\]
Then, uniformly for `1<=kappa<=3/2` as `L` tends to infinity,

\[
\boxed{M_1\sim C_*\exp\{(4-\kappa)L/16\},\qquad
M_R\sim b C_*\exp\{(4-\kappa)L/16\},} \tag{17}
\]
where the positive universal constant is

\[
C_* =\int_0^\infty e^{-y/2}
\sqrt{(\pi/8)^2+y^2/4}\,dy. \tag{18}
\]
Consequently,

\[
\boxed{\frac{M_R}{bM_1}\to1,\qquad
\frac{M_R}{b|\beta_1|}\sim
\frac{4C_*}{L}\exp\{(4-\kappa)L/16\}\to\infty.} \tag{19}
\]
Here `w_1=1`. The claim concerns actual prescribed amplitude coefficients;
no phases have been changed or independently selected.

**Proof.** Put `ell_N=log N=L/2+o(1)` and `y=ell_N-log n`. The exact
weights satisfy

\[
Nw_N=\exp\{(4-\kappa)L/16\}(1+o(1)),
\]
\[
\frac{w_n}{w_N}
=\exp\{(\sigma-t\ell_N/2)y+ty^2/4\},
\qquad \sigma-t\ell_N/2=1/2+o(1). \tag{20}
\]
For each bounded `y>=0`, the physical coefficients have limits

\[
\beta_n\to-\frac\pi8-\frac{iy}{2},
\qquad E_n/b\to1,
\qquad E_n'/b\to0,
\qquad Z_n/b\to-\frac\pi8-\frac{iy}{2}. \tag{21}
\]
The counting change `n=N e^{-y}` contributes `N e^{-y}dy`; combining it
with (20) gives the limiting measure `e^{-y/2}dy`, proving (17) on every
bounded `y` interval by ordinary Riemann sums.

To justify the entire range, for all sufficiently large `L`, uniformly in
`kappa`,

\[
\frac{w_n}{w_N}\le C(N/n)^{3/4},\qquad
|\beta_n|+|Z_n|/b\le C(1+\log(N/n)). \tag{22}
\]
The first bound follows because
`ty^2/4 <= (kappa/8+o(1)) y` on `0<=y<=ell_N`, and
`1/2+3/16<3/4`. The second follows from (4), (8), and the uniform physical
coefficient expansions: `|E_n|/b` is bounded, while `beta_n` is bounded by
`C(1+y)` after the leading carrier and cutoff frequencies cancel.

After division by `Nw_N`, the contribution of `n<=N exp(-Y)` is therefore
bounded by a constant times

\[
\int_0^{e^{-Y}}u^{-3/4}(1+|\log u|)\,du
+N^{-1/4}(1+\log N),
\]
which tends to zero uniformly as first `L` and then `Y` tend to infinity.
This proves dominated Riemann-sum convergence. It proves uniformity in
`kappa` as well, since all compact-`y` limits and tail bounds are uniform.
Finally `|beta_1|~L/4`, giving (19). QED.

## 5. Implication for the next signed estimate

The natural positive carrier coefficient in (6) is of order `L^2/16`.
The absolute arithmetic correction in (9) is not lower order than this
coefficient times the whole derivative mass. It is exponentially larger
than this coefficient times the `n=1` derivative. Therefore a proof based
on treating all remaining channels as an absolute perturbation of the
first carrier cannot reach an unbounded part of the shrinking sector.

Even the optimistic replacement of the actual observed slope by its full
absolute coefficient mass yields a defect ratio tending to one, so this
triangle calculation supplies no fixed relative reserve. This statement
does not rule out a reserve tending to zero with `L`; proving any useful
reserve would still require control of the actual observed slope and its
phase correlation with the defect.

The next concrete source target is (13), or its relative analogue, for

\[
2\Re\sum_{n\le N}\beta_nq_n
\quad\hbox{and}\quad
2\Re\sum_{n\le N}Z_nq_n,
\]
under the complete physical equation `Hxx=0`. The cutoff-edge limit (21)
shows where the largest absolute payments sit. It does not authorize
removing the lower-index complement, exchanging raw Mellin sums on the
physical line, or omitting any matched endpoint from Notes 9–10.

The operator and mass theorem explain why the lifted coordinate change
can give a useful normal form without making its genuine theta correction
small. Any eventual benefit has to come from the signed arithmetic response
of that correction, with the stationarity condition and remainder both paid.
