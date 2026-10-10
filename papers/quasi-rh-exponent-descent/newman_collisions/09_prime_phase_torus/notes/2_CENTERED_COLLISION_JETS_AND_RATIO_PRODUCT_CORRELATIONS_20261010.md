# Centered collision jets and ratio/product arithmetic correlations

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. The accompanying checks and review
are internal LLM work, not independent mathematical validation.

This continues [Note 1](1_ACTUAL_ORBIT_JETS_AND_EXACT_FINITE_HEAT_RESIDUAL_20261010.md)
and the first priority in [Heat Note 15](../../notes/15_SIXTEEN_PROGRAM_INITIAL_RESULTS_AND_FIVE_PRIORITIES_20261010.md).
It proves a paid reduction of the fourth-jet threshold test to three
centered signed logarithmic moments. It then transforms that quadratic
moment expression into two exact arithmetic channels, indexed by reduced
integer ratios and divisor products. Both channels, their actual common
height, and every mixed block/core term are retained. A bounded attempt
using third-derivative cancellation and separate block bounds loses a
positive power of the cutoff. No opposite threshold sign is proved.

## 1. Center at the actual endpoint frequency

Use the complete cutoff and `kappa in [1,3/2]`, `0<t<=1/20`,
`L=kappa/t`, `x=4 pi exp(L)`. Freeze `t`, its natural integer cutoff `N`,
and the following centering value during all raw spatial differentiation:

\[
\mu=\frac{\Omega}{c},\qquad \rho_n=\log n-\mu,
\qquad M_k=\sum_{n\le N}q_n\rho_n^k=X_k+iY_k,
\quad q_n=w_ne^{i\phi_n}.
\tag{1}
\]

The genuine data have `c=1/2(1+tU/2)>0`, `d=tV/4`, and
`q_n'/q_n=-i Omega+(-d+ic) log n`. In the chosen sector `c` is uniformly
bounded above and away from zero. For example the explicit formula
`alpha'=-1/(2s^2)-1/(s-1)^2+1/(2s)` bounds `|alpha'|<=1/x+6/x^2`;
`x>10^9` makes `0.49<c<0.51` a generous reserve.

For the local derivative calculation write

\[
v_n=A+B\rho_n,\qquad
A=-i\Omega+(-d+ic)\mu,\qquad B=-d+ic.
\tag{2}
\]

At the center, `A=-d mu` is real. Its *derivatives* are
`A^{(k)}=-i Omega^{(k)}+B^{(k)} mu`, with `mu` frozen, and are generally
complex. Replacing those derivatives by derivatives of `-d mu` would
silently differentiate a moving centering and lose terms.

The two paid candidate coordinates become especially simple:

\[
X_0=F_N/2,\qquad e_1:=F_N'/2=A X_0-dX_1-cY_1.
\tag{3}
\]

At a genuine collision, the full approximation gives

\[
|X_0|\le\eta_N/2,\quad |e_1|\le L\eta_N/2,
\qquad |cY_1+dX_1|\le(L+|A|)\eta_N/2.
\tag{4}
\]

Thus the first centered sine moment is tied to the first centered cosine
moment with the actual amplitude drift; it is not simply set to zero.
The unobserved `Y_0` remains unrestricted by these two coordinates.

## 2. Exact third and fourth raw signed-log rows

For `j=2,3,4`, write the complete Bell multiplier as
`P_j(v_n)=sum_{k=0}^j p_{jk} rho_n^k`, so
`F_N^{(j)}/2=Re sum_k p_{jk} M_k`. The independent coefficient rows are

\[
\begin{array}{c|lll}
j=2&p_{20}=A^2+A'&p_{21}=2AB+B'&p_{22}=B^2
\end{array}
\]

\[
\begin{aligned}
p_{30}&=A^3+3AA'+A'',\\
p_{31}&=3A^2B+3(AB'+BA')+B'',\\
p_{32}&=3AB^2+3BB',\qquad p_{33}=B^3,
\end{aligned}
\tag{5}
\]

\[
\begin{aligned}
p_{40}&=A^4+6A^2A'+3(A')^2+4AA''+A''',\\
p_{41}&=4A^3B+6(A^2B'+2ABA')+6A'B'
          +4(AB''+BA'')+B''',\\
p_{42}&=6A^2B^2+6(2ABB'+B^2A')+3(B')^2+4BB'',\\
p_{43}&=4AB^3+6B^2B',\qquad p_{44}=B^4.
\end{aligned}
\tag{6}
\]

These include all raw carrier, amplitude, and frequency derivatives. To
apply both candidates without losing their tolerances, set
`p_{j0}=u_0+i v_0`, `p_{j1}=u_1+i v_1` in each row. Exact elimination
of `Y_1` using (3) gives

\[
\begin{split}
F_N^{(j)}/2={}&-v_0Y_0+(u_1+d v_1/c)X_1
 +\Re\sum_{k=2}^j p_{jk}M_k\\
 &+(u_0-A v_1/c)X_0+(v_1/c)e_1.
\end{split}
\tag{7}
\]

At a genuine collision the last line has absolute bound

\[
\frac{\eta_N}{2}|u_0-A v_1/c|
 +\frac{L\eta_N}{2c}|v_1|.
\tag{8}
\]

This is an exact candidate-conditioned transformation, not a constraint
on freely chosen phases. In particular `Y_0` enters through the imaginary
lower-row coefficients; it has not been discarded by treating `S=0`.

## 3. A paid reduction to three centered moments

At the center let `b_n=i c rho_n` and `epsilon_n=-d log n`, so
`v_n=b_n+epsilon_n`. Define the exact finite residual payments

\[
E_j=2\sum_{n\le N}w_n|P_j(v_n)-(ic\rho_n)^j|,
\qquad j=2,3,4.
\tag{9}
\]

The residual polynomials, with no hidden differentiation, are

\[
\begin{aligned}
P_2-b^2={}&2b\epsilon+\epsilon^2+v',\\
P_3-b^3={}&3b^2\epsilon+3b\epsilon^2+\epsilon^3
                  +3(b+\epsilon)v'+v'',\\
P_4-b^4={}&4b^3\epsilon+6b^2\epsilon^2+4b\epsilon^3+\epsilon^4
 +6(b+\epsilon)^2v'+3(v')^2+4(b+\epsilon)v''+v'''.
\end{aligned}
\tag{10}
\]

Consequently the leading centered jets are

\[
g_2=-2c^2X_2,\qquad g_3=2c^3Y_3,\qquad g_4=2c^4X_4,
\quad |F_N^{(j)}-g_j|\le E_j.
\tag{11}
\]

These payments concern the *complete* sum. They do not remove a
macroscopic block or assert a new approximation theorem at a smaller
cutoff.

The residuals vanish rapidly in the genuine sector. The explicit alpha
formula gives `|V|=O(1/x)`, `t log n=O(1)`, hence
`epsilon_n=O(1/x)` uniformly. Its fixed-time raw derivatives satisfy
`v_n^{(k)}=O_k(x^{-k})` for `k>=1`. This uses derivatives at fixed `n`,
not along the scaling relation between time and height. Moreover

\[
\sum_{n\le N}w_n(1+|\rho_n|)^j
=O_j(e^{\mathfrak a/t}),\qquad
\mathfrak a=\kappa(4-\kappa)/16.
\tag{12}
\]

For clarity, `mu=log N+O(1/N)`, by the floor estimate and explicit
alpha data. Writing `y=log(N/n)`, the weight density after summation
comparison is bounded by a constant times
`N w_N exp(-y/2+t y^2/4+O(t y/N))`. The last term also retains the
natural-cutoff floor displacement. Since
`t y<=kappa/2+o(1)`, its exponent is at most
`-(1/2-kappa/8-o(1))y`. On this closed kappa interval that coefficient
is uniformly positive. Polynomial `y` moments are integrable. The
finite low-index endpoint contributes only a polynomial in `L`, absorbed
by `exp(mathfrak a/t)`. This is also the manuscript's complete absolute
jet budget, expressed in centered coordinates.

Equations (9)–(12) prove the uniform asymptotic payment

\[
E_j=O_j(e^{\mathfrak a/t}/x),\qquad j=2,3,4.
\tag{13}
\]

The measured formula (9), not an unprinted constant in (13), is the
available numerical payment at a particular center.

Retain the exact normalizer term
`gamma=18 partial_x^2 log A_t+9/x^2`, and put
`widehat delta_j=j! L^j eta_N+E_j`. The complete measured payment is

\[
\begin{split}
\widehat\Delta={}&4|g_3|\widehat\delta_3+2\widehat\delta_3^2
 +3(|g_2|\widehat\delta_4+|g_4|\widehat\delta_2
                   +\widehat\delta_2\widehat\delta_4)\\
 &+|\gamma|(2|g_2|\widehat\delta_2+\widehat\delta_2^2).
\end{split}
\tag{14}
\]

Let `Gamma=gamma/c^2`. Then the exact leading expression is

\[
\mathscr L(g)=4c^6\mathcal K,\qquad
\mathcal K=2Y_3^2+3X_2X_4-\Gamma X_2^2.
\tag{15}
\]

At a putative all-real threshold collision, a sufficient excluding input
is now the explicit arithmetic inequality

\[
\boxed{\quad \mathcal K<-\widehat\Delta/(4c^6).\quad}
\tag{16}
\]

Its measured errors are complete. The new centering residual does not
worsen the previous vanishing-error order: `g_j=O_j(exp(a/t))`,
`gamma=O(x^{-2})`, and `2a-kappa=-2b`, where
`b=kappa(kappa+4)/16`. Therefore

\[
\widehat\Delta
=O\left(L^4e^{-\kappa^2/(8t)}+L^6e^{-2\mathfrak b/t}\right)=o(1).
\tag{17}
\]

No opposite sign in (16) has been proved. The all-real hypothesis and
higher-multiplicity obligations remain exactly those of Note 13. The
centered reduction makes the missing signed moment correlation explicit;
it does not turn small residuals into nonvanishing.

## 4. Exact ratio and divisor-product channels

The quadratic expression in (15) has a correlated arithmetic transform
that retains both kinds of real-axis interference. For each ordered pair
put

\[
h=\log(nm)-2\mu,\qquad \delta=\log(n/m),
\quad \rho_n=(h+\delta)/2,\quad\rho_m=(h-\delta)/2.
\]

Product-to-sum gives, exactly,

\[
\mathcal K=\sum_{n,m\le N}w_nw_m
 \{D(h,\delta)\cos(T\delta)
      +P(h,\delta)\cos(2\theta_t+T\log(nm))\},
\tag{18}
\]

where

\[
\begin{aligned}
D(h,\delta)&=\frac{(h^2-\delta^2)^2(5h^2+\delta^2)}{128}
                       -\frac{\Gamma(h^2-\delta^2)^2}{32},\\
P(h,\delta)&=\frac{(h^2-\delta^2)^2(h^2+5\delta^2)}{128}
                       -\frac{\Gamma(h^2-\delta^2)^2}{32}.
\end{aligned}
\tag{19}
\]

The leading coefficients in both channels are nonnegative, but their
cosine factors are signed. Dropping the phase-sum channel would change
the threshold expression. Positivity of the coefficient weights does not
provide the negative sign sought in (16).

Let `sigma=1/2+t alpha_r/2`. The true heat weights factor in pair
coordinates as

\[
w_nw_m=(nm)^{-\sigma}
 \exp\{\tfrac t8\log^2(nm)+\tfrac t8\log^2(n/m)\}.
\tag{20}
\]

This retains the mixed heat coupling. Group the difference channel by
coprime positive integers `a,b`, writing `n=ja,m=jb`:

\[
\mathcal D=\sum_{(a,b)=1\atop\max(a,b)\le N}
 \mathcal A_{a,b}\cos(T\log(a/b)),
\quad
\mathcal A_{a,b}=\sum_{j\le N/\max(a,b)}
 w_{ja}w_{jb}D(\log(j^2ab)-2\mu,\log(a/b)).
\tag{21}
\]

Group the sum channel by integer products:

\[
\mathcal P=\sum_{k\le N^2}\mathcal B_k
 \cos(2\theta_t+T\log k),
\quad
\mathcal B_k=\sum_{n\mid k\atop n\le N,\ k/n\le N}
 w_nw_{k/n}P(\log k-2\mu,\log(n^2/k)).
\tag{22}
\]

Then `K=D+P` exactly. The inner coefficients share (20), while the
outer phases share the *same* actual `T` and carrier. These are divisor
and reduced-ratio correlations of the genuine cutoff, not independent
Euler factors or new phase variables. The diagonal ratio `(a,b)=(1,1)`
and all product-square terms remain included.

For the declared block `B={n:N/2<n<=N}`, retain the pair partition
`B x B`, `B x C`, `C x B`, `C x C`, where `C` is its complete
complement. Equations (21)–(22) can be restricted to any partition simply
by retaining its pair indicator in the inner coefficient. In particular
the mixed terms are not estimated away by a new scalar cutoff theorem.

## 5. A bounded block estimate and its exact loss

The tested fallback is to estimate the centered block moments separately
by the third-derivative theorem, then recombine by absolute cross payments.
It is a genuine-phase calculation, but it loses the needed sign.

On `N/2<u<=N`, the real logarithmic phase has
`f'''(u)=T/(pi u^3) asymp 1/N`. Its lower and upper derivative constants
are uniform, and every partial interval has length at most `N/2`.
[Arias de Reyna, equation (2)](https://arxiv.org/html/2407.02094v1)
therefore gives the partial-sum exponent `5/6`. The integer intervals of
at most three terms are bounded trivially. On this block,
`|rho|<=log 2+O(1/N)`, and `w_N<=1.01 N^{-s_kappa}`,
`s_kappa=1/2+kappa/8`; each fixed polynomial moment coefficient has total
variation `O_j(N^{-s_kappa})`. Exact Abel summation yields

\[
|M_{j,B}|=O_j(N^{5/6-s_\kappa}),\qquad0\le j\le4.
\tag{23}
\]

The exponent lies in `[7/48,5/24]` and is positive. Unlike a shrinking
edge, a fixed-proportion block has bounded, rather than vanishing,
centered frequency range; higher raw jets acquire no extra negative
power of `N` here.

For clarity, writing moments as block plus complement expands the leading
part exactly as

\[
\begin{split}
2Y_3^2+3X_2X_4={}&2Y_{3,C}^2+3X_{2,C}X_{4,C}
 +2Y_{3,B}^2+3X_{2,B}X_{4,B}\\
 &+4Y_{3,C}Y_{3,B}
   +3(X_{2,C}X_{4,B}+X_{2,B}X_{4,C}).
\end{split}
\tag{24}
\]

The gamma part has its own square/cross expansion. Applying (23) and
the complete moment budget `O(N^{1-s_kappa})` to (24) gives a mixed
absolute payment with exponent

\[
(1-s_\kappa)+(5/6-s_\kappa)=5/6-\kappa/4
\in[11/24,7/12],
\tag{25}
\]

and a block-quadratic payment with exponent
`5/3-2s_kappa=2/3-kappa/4 in [7/24,5/12]`. Both are positive.
Even if both candidate equations (4) are imposed, these estimates have
not supplied a relation cancelling the mixed higher moments in (24).
Thus this specified separate-moment/absolute-recombination mechanism
cannot pay an `o(1)` signed threshold margin. These positive exponents
describe the available *upper bounds*, not growth of an actual sum or a
no-go theorem for correlation-preserving transformations.

The useful next task is to estimate the two channels (21)–(22) *together*
conditional on (4), on one stated closed kappa interval, or to derive a
theta relation forcing the required opposition between `X_2` and `X_4`.
The exact measured criterion is (16). Program 13's coherent macroscopic
block transformation can supply correlations for this target; separate
positive block norms cannot. No arithmetic condition has yet forced its
strict negative sign, and no RH or priority claim is made.

The [continuation checker](../numerics/check_centered_prime_collision.py)
verifies the independent rows, candidate elimination, residual
polynomials, signed pair kernel, complete ratio/product regrouping,
quadratic perturbation payment, and exponent reserves by exact finite
arithmetic. Its finite formal phase controls are not actual large-height
heat evaluations or signed certificates for (16).
