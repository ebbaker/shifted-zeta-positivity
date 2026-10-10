# Prescribed heat-weight covariance and its signed moment hierarchy

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex); configured reasoning effort: ultra, verified
from the parent chat's local turn context. The checks and review are internal
LLM work, not independent mathematical validation.

This continues [Note 3](3_PAID_DUAL_KERNELS_AND_ACTUAL_FREQUENCY_RELAXATION_LOSS_20261010.md)
and the project 09 task in [Heat Note 17](../../notes/17_TWO_PRIORITY_CONTINUATION_AND_COMPLETE_CURRENT_GEOMETRY_20261010.md).
The prescribed quadratic log-weight has an exact Gaussian coefficient
decomposition. Applying it to the paid dual gives a new signed covariance
with all four arithmetic channels intact. That covariance is exactly an
infinite hierarchy of shifted signed-log dual expressions. A complete
absolute covariance payment has size `Theta(t exp(2 a/t))`, rather than
a vanishing error; the decomposition supplies no free negative sign. This is a precise
obstruction to that specified Gaussian-mixture/absolute-payment method,
not an obstruction to estimates which preserve the covariance's signs.

## 1. Physical state and the new coefficient transform

Keep `kappa in [1,3/2]`, `0<t<=1/20`,
`L=kappa/t`, `x=4 pi exp(L)`, and the complete natural integer cutoff
`N=floor(sqrt(exp(L)+t/16))`. At a center freeze time, cutoff, and
`mu=Omega/c` during raw spatial differentiation. Write

\[
 \ell_n=\log n,\quad \rho_n=\ell_n-\mu,\quad
 w_n=\exp(-\sigma\ell_n+t\ell_n^2/4),\quad
 \phi_n=\theta_t+T\ell_n,\quad \epsilon=d/c.
\tag{1}
\]

All phases have the same physical `T,theta_t`. The drift `d`, carrier,
frequency `c`, and their physical derivatives remain as in Note 2.
The original three-term coefficient control does not have this weight
shape: on `1,2,4`, the prescribed ratio is

\[
 \frac{w_2^2}{w_1w_4}=\exp[-t(\log2)^2/2]<1,
\tag{2}
\]

whereas coefficients `1,2,1` give ratio `4`. Thus the prescribed shape
really adds information. The result below uses that information exactly,
without claiming that log convexity by itself proves the required sign.

Set

\[
 b_n=\exp(-\sigma\mu+t\mu^2/4)
       \exp[-(\sigma-t\mu/2)\rho_n].
\tag{3}
\]

Then `w_n=b_n exp(t rho_n^2/4)`. If `Z` is a real standard Gaussian,
define the auxiliary coefficient tilt

\[
 a_n(Z)=b_n\exp(\sqrt{t/2}\,Z\rho_n).
\tag{4}
\]

Completing the square in the Gaussian integral proves
`E a_n(Z)=w_n`. This is an exact finite coefficient identity. The
auxiliary tilt retains the same phase, common height, carrier, `mu`,
and drift. It does not move to a different physical height or assert
that a tilted sum obeys a separate heat equation. If raw local jets of
a tilted control are wanted, freeze the reweighting `a_n(Z)/w_n` at
the center; then each summand retains the full multiplier `P_j(v_n)`
of Note 2. None of the physical Bell rows is replaced by a pure phase
derivative.

Define the actual five-vector feature

\[
 f_n=\big(\cos\phi_n,\ \rho_n(\sin\phi_n+\epsilon\cos\phi_n),
          \rho_n^2\cos\phi_n,\ \rho_n^3\sin\phi_n,
          \rho_n^4\cos\phi_n\big)^T.
\tag{5}
\]

For `V(Z)=sum a_n(Z) f_n`, its mean is the complete actual vector
`V=(e,u)=(X_0,Z_1,X_2,Y_3,X_4)`, where `Z_1=Y_1+epsilon X_1`.
For any of Note 3's real symmetric dual matrices

\[
 \mathbb Q=\begin{pmatrix}\Lambda&B\\B^T&Q\end{pmatrix},\qquad
 Q=\begin{pmatrix}-\Gamma&0&3/2\\0&2&0\\3/2&0&0\end{pmatrix},
 \quad\Gamma=\gamma/c^2,
\tag{6}
\]

finite Gaussian integrability gives the exact formula

\[
 \boxed{\quad
 \mathcal K_{\Lambda,B}(V)
  =\mathbb E\mathcal K_{\Lambda,B}(V(Z))
       -\operatorname{tr}(\mathbb Q\,\mathcal C_t),\quad
 \mathcal C_t=\operatorname{Cov}(V(Z)).\quad}
\tag{7}
\]

The matrix `C_t` is positive semidefinite. Its contraction with the
indefinite `mathbb Q` has no automatic sign. Positivity of the Gaussian
measure therefore supplies no Jensen inequality for the signed dual.
At the exact actual candidates only the *mean* lower coordinates vanish;
the auxiliary tilted lower coordinates generally do not vanish.

## 2. Four covariance channels and an exact signed hierarchy

The Gaussian product expectation computes the covariance explicitly:

\[
 \boxed{\quad
 \mathcal C_t=\sum_{n,m\le N}w_nw_m
       \big(e^{t\rho_n\rho_m/2}-1\big) f_nf_m^T.\quad}
\tag{8}
\]

Let `D_c,D_s,P_c,P_s` be Note 3's exact dual kernels, with precisely
the same `Lambda,B,epsilon,Gamma`. Consequently

\[
\begin{split}
 \operatorname{tr}(\mathbb Q\mathcal C_t)
 =\sum_{n,m\le N}w_nw_m\big(e^{t\rho_n\rho_m/2}-1\big)
 \{&D_c\cos(T\log(n/m))+D_s\sin(T\log(n/m))\\
   &+P_c\cos(2\theta_t+T\log(nm))\\
   &+P_s\sin(2\theta_t+T\log(nm))\}.
\end{split}
\tag{9}
\]

In pair coordinates `h=log(nm)-2mu`, `delta=log(n/m)`, the new multiplier
is `exp[t(h^2-delta^2)/8]-1`. Thus both ratio and product grouping
remain exact, with the multiplier included *inside* each reduced-ratio
or divisor-product coefficient sum. The true pair weight is still

\[
 w_nw_m=(nm)^{-\sigma}
   \exp[t\log^2(nm)/8+t\log^2(n/m)/8].
\tag{10}
\]

Neither multiplier nor phase permits dropping a sine term, the product
channel, diagonal pairs, squares, or any of the four block/core classes.
The covariance is evaluated on the same complete common-height orbit.

There is a second exact description. For `k>=0` define

\[
 V^{[k]}=\sum_{n\le N}w_n\rho_n^k f_n
   =\big(X_k,\ Y_{k+1}+\epsilon X_{k+1},\
          X_{k+2},\ Y_{k+3},\ X_{k+4}\big)^T.
\tag{11}
\]

Expanding the exponential in (8), with the finite cutoff held fixed,
gives an absolutely convergent rank-one series

\[
 \mathcal C_t=\sum_{k\ge1}\frac{(t/2)^k}{k!}
                    V^{[k]}(V^{[k]})^T,
\]
\[
 \boxed{\quad
 \mathcal K_{\Lambda,B}(V)
 =\mathbb E\mathcal K_{\Lambda,B}(V(Z))
  -\sum_{k\ge1}\frac{(t/2)^k}{k!}
      (V^{[k]})^T\mathbb QV^{[k]}.\quad}
\tag{12}
\]

For zero dual parameters the leading covariance term is

\[
 \frac t2\big(2Y_4^2+3X_3X_5-\Gamma X_3^2\big).
\tag{13}
\]

With dual parameters, (13) additionally contains the lower coordinates
`X_1,Y_2+epsilon X_2`, coupled to `X_3,Y_4,X_5`, and their quadratic
dual terms. The two actual candidate conditions constrain `V^{[0]}`;
they do not constrain these shifted lower coordinates. Enforcing them
at every Gaussian tilt would add hypotheses absent from the research
problem. Formula (12) exposes exactly the signed correlations which a
Gaussian coefficient decomposition has to retain.

For example, truncation after order `r` has the rigorous measured bound

\[
\begin{split}
\left|\operatorname{tr}(\mathbb Q\mathcal C_t)
 -\sum_{k=1}^{r}\frac{(t/2)^k}{k!}
          (V^{[k]})^T\mathbb QV^{[k]}\right|
 \le{}&\|\mathbb Q\|_{\rm op}
       \frac{(t/2)^{r+1}}{(r+1)!}\\
 &\times\sum_{n,m\le N}w_nw_m
   |\rho_n\rho_m|^{r+1}e^{t|\rho_n\rho_m|/2}
                      \|f_n\|\|f_m\|.
\end{split}
\tag{14}
\]

This follows from the real exponential Taylor remainder, including
negative `rho_n rho_m`. It is a finite directly measurable payment,
not a claim that any fixed truncation gives the needed signed margin.

## 3. Uniform size of the specified absolute covariance envelope

Define the coefficient/feature triangle envelope

\[
 \mathcal E_t=\sum_{n,m\le N}w_nw_m
       |e^{t\rho_n\rho_m/2}-1|\,\|f_n\|\|f_m\|.
\tag{15}
\]

**Envelope proposition.** Uniformly for `kappa in [1,3/2]`, as
`t -> 0+` with the natural cutoff and actual common-height data,

\[
 \boxed{\quad
 \mathcal E_t\asymp t(Nw_N)^2
            \asymp t\exp(2\mathfrak a/t),\qquad
 \mathfrak a=\kappa(4-\kappa)/16.\quad}
\tag{16}
\]

The constants do not depend on the actual phases. This is a statement
about the explicitly positive envelope (15), not about the signed
covariance (9). In particular it is not a lower bound for (9).

Here is a discrete proof keeping the full cutoff. The actual alpha and
floor estimates in Note 2 give
`mu=log N+O(1/N)`,
`sigma-t log N/2=1/2+o(1)`, `epsilon=O(t/x)`, and
`N w_N asymp exp(a/t)`, uniformly. Put `y_n=log(N/n)`.
Exactly,

\[
 \frac{w_n}{w_N}
 =\exp\big[(\sigma-t\log N/2)y_n+t y_n^2/4\big].
\tag{17}
\]

Partition `y_n` into intervals `[j,j+1)`. Since `j<=log N`, each
contains at most `2N exp(-j)` indices. Moreover
`|rho_n|<=y_n+O(1/N)` and
`||f_n||<=C(1+y_n)^4` with a uniform `C`. The inequality
`|exp(z)-1|<=|z| exp(|z|)` bounds (15) by `C t(Nw_N)^2` times
a double sum of polynomial factors in `j,k`, whose exponential factor
is bounded by

\[
 \exp\big[-(1/2-o(1))(j+k)+t(j+k+2+o(1))^2/4+O(1)\big].
\tag{18}
\]

The addition of `t|rho_n rho_m|/2` to the two heat exponents is
essential: their quadratic envelope is the square of the *sum* of
the two log distances. Since `j+k<=2log N=kappa/t+o(1)`, the
coefficient of `j+k` in (18) is at most
`-1/2+kappa/4+o(1)<=-1/8+o(1)`. For sufficiently small time it is
at most `-1/16`. All its fixed polynomial moments have a uniform
summable majorant. This proves the upper bound in (16), and also
`sum w_n asymp Nw_N` by the one-bin version of the same argument.

For the lower bound keep only the indices
`N exp(-2)<=n<=N exp(-1)`. There are at least `cN` such indices
for a uniform positive `c`, their weights are at least `c w_N`,
and, for large `N`, `rho_n` lies in `[-2.1,-0.9]`. Hence
`rho_n rho_m>=0.81` and
`exp(t rho_n rho_m/2)-1>=0.405t`. For every carrier and every
actual phase,

\[
 \|f_n\|^2\ge\cos^2\phi_n+\rho_n^6\sin^2\phi_n
                 \ge0.9^6.
\tag{19}
\]

That complete subblock supplies `c t(Nw_N)^2` to (15). No phase
independence, irrational orbit density, or numerical estimate is used.
The same proof without the feature factors establishes the analogous
zeroth coefficient-covariance envelope. It does not assign its scale
to each separately signed kernel.

The valid norm/triangle bound is
`|tr(mathbb Q C_t)|<=||mathbb Q||_op E_t`.
For every dual, `||mathbb Q||_op>=2`, since its fixed `Y_3` diagonal
is `2`. Thus this chosen covariance payment is at least
`c t exp(2 a/t)` for *every* dual; for uniformly bounded dual matrices
it has exactly that order. Larger dual parameters cannot reduce it.
This positive exponent differs from the complete physical jet payment
of Note 2,

\[
 \widehat\Delta
 =O\big(L^4e^{-\kappa^2/(8t)}+L^6e^{-2\mathfrak b/t}\big)=o(1),
 \qquad \mathfrak b=\kappa(\kappa+4)/16.
\tag{20}
\]

Therefore positivity of the Gaussian tilt measure followed by this
absolute covariance payment cannot itself supply a vanishing signed
error. A separately established negative margin of larger order could
still dominate it; no theorem rules out such a margin. The scoped loss
is that the coefficient decomposition plus absolute recombination gives
no new opposite sign and pays an exponentially large envelope.

## 4. The paid target after this transform

At a genuine candidate retain both original tolerances,
`|X_0|<=eta_N/2` and
`|A X_0-c Z_1|<=L eta_N/2`, where `A=-d mu`. Retain all
physical Bell residuals `E_j` of Note 2, the spatial errors
`j! L^j eta_N`, and the exact normalizer
`gamma=18 partial_x^2 log A_t+9/x^2`. Thus Note 3's actual dual
payment `Pi_{Lambda,B}` and `widehat Delta/(4c^6)` remain present.

Suppose one proves integrable auxiliary upper bounds `U(Z)` for the
*unconditioned tilted states* `K_dual(V(Z))`, and a signed lower bound
`C_lower` for the complete contraction (9). Then the concrete sufficient
criterion furnished by (7) is

\[
 \boxed{\quad
 \mathbb E U(Z)-C_{\rm lower}
       +\Pi_{\Lambda,B}+\widehat\Delta/(4c^6)<0.\quad}
\tag{21}
\]

The same dual parameters occur in both terms and their payment. One
cannot apply a candidate-only untilted theorem to every `V(Z)`: their
candidate coordinates are generally nonzero. The exact hierarchy (12)
provides an alternative task, namely a lower bound for its full signed
series, together with an upper bound for the tilted average. A finite
hierarchy truncation must pay (14).

[Heat Note 18](../../notes/18_CORRELATED_HOLOMORPHIC_PAYMENTS_AND_CANDIDATE_COVERAGE_20261010.md)
additionally derives a correlated candidate domain from the holomorphic
approximation disk. In the present coordinates its necessary condition
is

\[
 (2X_0/\eta_N)^2+
      2|A X_0-cZ_1|/(L\eta_N)\le1.
\tag{22}
\]

This can replace the rectangular candidate box when maximizing a dual
payment. It does not constrain the auxiliary covariance directions in
(11). Formula (21), with a rigorously reduced payment if available,
still requires the new signed arithmetic input. No such bound is proved
here; collision exclusion, higher multiplicity, and endpoint coverage
remain outstanding.

## 5. Verification scope

The [standard-library checker](../numerics/check_prescribed_heat_covariance.py)
verifies Gaussian moments, the prescribed quadratic-weight centering,
all four covariance kernel signs, complete block/core recombination,
and the signed hierarchy through degree 12 in `sqrt(t/2)`. Its rational
unit-complex controls use one common phase generator on powers, with
the genuine quadratic heat coefficient shape retained as an exact
formal series. They verify identities; they are not evaluations of the
actual exponentially large arithmetic center. The uniform asymptotic
bounds are proved above, not inferred from finite tests.

The [source-bound record](../numerics/prescribed_heat_covariance_record_20261010.json)
and [internal review](../reviews/4_PRESCRIBED_HEAT_COVARIANCE_INTERNAL_REVIEW_20261010.md)
record the checks and their scope. All files are small sources or records
under [LARGE_FILES.md](../../../../../LARGE_FILES.md). Earlier notes and
the stable manuscript are preserved. There is no new RH, Newman-bound,
or literature-priority claim.
