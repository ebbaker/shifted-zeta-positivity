# R01: a paid second-level fluctuation comparison

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from rollout turn_context. Recurrence chat0001, thread
`01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Return: HDA-R01-AN01 r1. Proved in-note from the named classical
inputs; same-model internal assessment only.** On each full fixed buffered
chart and `1<=T<=2`, the frozen `p=2, K=4` model satisfies
\[
 \|h-F^{[2,4]}\|^{(3,1)}_{X;1,2}\le C_{r,b}X^{-11/4}.
\tag{R1.1}
\]
There is no logarithmic loss. The residual and its first spatial derivative
are exactly zero. The bounded RS integral and every arithmetic mode remain.
This is a natural gamma-envelope estimate, without division by h or a cosine.
The [input record][inputs] matches every planning hash at opening; the
[assessment][review] records scope. No numerical or symbolic campaign,
manuscript edit or evaluated onset is supplied.

## 1. Contract and exact model

Use the [continuation r1][continuation] without changing its normalization:
`h(T,z)=H(-T,z)`, `h_T=h_zz`, `H(0,z)=xi((1+iz)/2)/8`, the complete theta
source, and the two gamma arms in [ansatz Note16][n16]. Freeze the real X,
`L=log(X/(4pi))`, `N=floor(sqrt(X/(4pi)))`, `V=8 sqrt(2)L`, every gamma
coefficient and real partition. Write `d=z-X`, `R=r+1`, `Y=b+1`, `W=R+Y`.
Prove the field comparison on `Omega_X(R,Y)` before taking Cauchy estimates
on `Omega_X(r,b)`. Physical radii remain `r=ell+2`, `b=1+h_av+2`.

For epsilon=+1,-1 put
\[
 w_\epsilon(z)=(1+\epsilon iz)/2,\quad
 M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16,\quad
 \ell_\epsilon=\log M(w_\epsilon),
\]
\[
 b_{\epsilon n}=M(w_\epsilon(X))n^{-w_\epsilon(X)},\quad
 \lambda_{\epsilon n}=\ell_\epsilon'(X)-\epsilon i\log n/2,
 \quad c_{\epsilon k}=\ell_\epsilon^{(k+1)}(X)/(k+1)!.
\]
An analytic logarithm exists on the high-height disk used below. With
`gamma=kappa_2`, `eta=kappa_3`, the initial polynomial is
\[
 P_2(q)=1+\gamma q^2/2+\eta q^3/6+\gamma^2q^4/8.
\tag{R1.2}
\]
The identity `Q_T k_T(d-q)=q k_T(d-q)`, where `Q_T=d+2T partial_d`, gives
\[
 \int_{\mathbb R}k_T(d-q)b e^{\lambda q}P_2(q)dq
 =\left[1+\frac\gamma2 Q_T^2+
  \frac\eta6 Q_T^3+\frac{\gamma^2}8Q_T^4\right]
      b e^{\lambda d+T\lambda^2}.
\tag{R1.3}
\]
All Gaussian integrals here converge absolutely at T>0. Summing exactly
over both arms and `1<=n<=N` gives `U_0+U_1+U_2` as requested.

Keep [Note05 FN12--15][n05] literally, with real initial RS data through
K=4: `f_4=S_m+R_m,4=S_N+Q_X,4`, including the exact transfer `S_m-S_N`.
The model is this finite Gaussian-moment sum plus
\[
 \mathcal I_{X,4}(T,z)=\int_{X-V}^{X+V}k_T(z-u)Q_{X,4}(u)du.
\tag{R1.4}
\]
All real parts remain inside Q before complex-kernel integration. No
analytic derivative of a real RS coefficient or moving cutoff is used.

## 2. A genuine local remainder

The sectorial gamma input in Note05 can be applied on `|z-X|<=X/4`.
Indeed the arguments `(1+epsilon iz)/4` remain a fixed distance in angle
from the negative real ray and have modulus comparable to X. The uniform
digamma expansion [DLMF 5.11.2][digamma], with [sectorial remainders][sector],
and an interior Cauchy estimate give `psi'(v)=1/v+O(|v|^-2)` there.
Explicitly
\[
 \ell_\epsilon''(z)=\frac1{4w^2}+\frac1{4(w-1)^2}
                         -\frac1{16}\psi'(w/2)=O(X^{-1}).
\]
Choose fixed constants H,A>=1 and D>=4, after a fixed classical onset,
so `sup_|q|<=X/4 |ell''(X+q)|<=H/X`. Cauchy then gives, **simultaneously
for all k>=1**,
\[
 |c_{\epsilon k}|\le\frac{H4^{k-1}}{k(k+1)}X^{-k}
                         \le A D^{k-1}X^{-k}.
\tag{R1.5}
\]
This derives an analytic majorant; the separate fixed-k big-O statements
alone would not justify summing a logarithmic remainder. No growing-order
Stirling series is presumed.

For `x=|q|<=V`, impose
\[
 DV/X\le1/2,\qquad 2AV^2/X\le1.
\tag{R1.6}
\]
Let `f(s)=sum_{k>=1}c_k q^{k+1}s^k`, `g(s)=exp f(s)` for 0<=s<=1.
The convergent geometric majorant gives
\[
 |f(s)|\le2Ax^2/X,\qquad
 |f^{(j)}(s)|/j!\le 2^{j+1}AD^{j-1}x^{j+1}X^{-j}
 \quad(j=1,2,3).
\]
Taylor's integral remainder for g at s=0, using
`g'''/6=e^f(f'''/6+f'f''/2+(f')^3/6)`, proves
\[
 |A_\epsilon(q)-P_2(q)|\le e X^{-3}\mathcal B_3(x),
\quad
 \mathcal B_3(x)=16AD^2x^4+32A^2Dx^5+\frac{32}3A^3x^6.
\tag{R1.7}
\]
The coefficients through s^2 are exactly R1.2. This is the paid weighted
remainder, including mixed and repeated curvature. Replacing x by V in
R1.7 before Gaussian integration would give an unnecessary logarithmic
loss; that weaker estimate is not used.

## 3. Kernel and full-population payments

The exact initial-value identity is [Note05 FN4][n05]:
`h(T,z)=int_R k_T(z-u)H(0,u)du`. Fix tau=1, B=2 in the following explicit
constants; their parameter notation is retained to show each cost:
\[
 M_m=\sqrt2 e^{R+Y^2/(4\tau)+2B}
 \sum_{k=0}^m {m\choose k}W^{m-k}(8B)^{k/2}
                    \frac{\Gamma((k+1)/2)}{\sqrt\pi},
 \qquad M_m^t=\frac{M_m}{2\tau}+\frac{M_{m+2}}{4\tau^2}.
\tag{R1.8}
\]
With `v=u-Re z`, `|q|, |z-u| <= |v|+W` and
`|q|<=R+|v|`. Use `|v|<=v^2/(8T)+2T`. Gaussian integration proves
\[
 \int |k_T(z-u)|e^{|q|}|q|^mdu\le M_m,
 \quad \int |\partial_T k_T(z-u)|e^{|q|}|q|^mdu\le M_m^t.
\tag{R1.9}
\]
For the second inequality use the **differentiated kernel**
\[
 \partial_T k_T(z-u)=
   \left(\frac{(z-u)^2}{4T^2}-\frac1{2T}\right)k_T(z-u).
\tag{R1.10}
\]
This displays the complex factor `exp(Y^2/(4tau))`, both inverse-time
factors, and moments through degree eight for R1.7.

At real X, `|b_epsilon,n|=G(X)n^-1/2`; after a slope onset
`|Re lambda|<=1`. Therefore the complete real initial population satisfies
\[
 \sum_{\epsilon,n\le N}|b_{\epsilon n}e^{\lambda_{\epsilon n}q}|
 \le C_{\rm pop}G(X)X^{1/4}e^{|q|},
 \qquad C_{\rm pop}=4(4\pi)^{-1/4}.
\tag{R1.11}
\]
No fixed-n approximation or n-dependent transverse power is discarded.
Integrating R1.7 with R1.9 and then summing R1.11 pays the local field
error by `G(X)X^-11/4 C_pop e B_3[M]`, where polynomial evaluation
`B_3[M]` replaces x^m by M_m. The direct time cost is `C_pop e B_3[M^t]`
at the identical power. Fixed q-moments absorb the window's growth.

For initial RS mismatch the checked [Polymath v2 Proposition6.2,
(56), with (38)][rs] gives at real sigma=1/2 and positive integer K
\[
 |H(0,u)-f_K(u)|\le\frac{2^{7/4}}7 G(u)a_u^{-1/2}
       \Gamma((K+1)/2)(1.1/a_u)^{K+1}.
\tag{R1.12}
\]
This is solely a real initial-data import. On `X-V>=X/2`, let C_Gamma be
fixed so `G(X+q)<=C_Gamma G(X)e^{|q|}`. For K=4, R1.12 is at most
`C_4 G(X)e^{|q|}X^-11/4`, with the explicit sufficient constant
\[
 C_4=C_\Gamma\frac{2^{7/4}}7\Gamma(5/2)1.1^5(8\pi)^{11/4}.
\tag{R1.13}
\]
Thus its field/time costs are `C_4 M_0` and `C_4 M_0^t`. All five RS
coefficients and the exact adjacent transfer remain in the model; they
are not estimated away or analytically extended.

## 4. True and artificial tails, with sufficient onsets

Here set tau=1,B=2 as above. Define
\[
 D_m=\frac{e^{Y^2/(4\tau)}}{\sqrt{4\pi\tau}}
      2^m(64B)^{(m+1)/2}\Gamma((m+1)/2),\qquad
 D_m^t=D_m/(2\tau)+D_{m+2}/(4\tau^2),
\]
\[
 J_m=\frac{e^{Y^2/(4\tau)}}{\sqrt{4\pi\tau}}
 \sum_{k=0}^m{m\choose k}Y^{m-k}(8B)^{(k+1)/2}\Gamma((k+1)/2),
 \qquad J_m^t=J_m/(2\tau)+J_{m+2}/(4\tau^2).
\tag{R1.14}
\]
If `V>=max(2R,R+Y+1,32B)`, then, for |q|>=V,
\[
 -(q-\Re d)^2/(4B)+|q|\le-q^2/(32B),\qquad |z-u|\le2|q|.
\]
Splitting this exponent proves tail moments bounded by
`D_m exp(-V^2/(64B))=D_m exp(-L^2)`, and the direct-time versions by
`D_m^t exp(-L^2)`. The displayed D's also majorize `(2|q|)^m` moments.

For true data on `V<|q|<=X/2`, retain Note05's height-sensitive bound
`|H(0,X+q)|<=C X^P exp(-pi X/8+pi|q|/8)`, with P=4 admissible.
Since `G(X)>=g_- X^7/4 exp(-pi X/8)`, normalized true moderate tails
are at most
\[
 A_{\rm mod}X^{P-7/4}e^{-L^2},\quad
 A_{\rm mod}=C_{\rm tail}\max(D_0,D_0^t).
\tag{R1.15}
\]
The complete artificial initial polynomial obeys, for X>=1,
`|P_2(q)|<=1+A|q|^2+AD|q|^3+(A^2/2)|q|^4`. Its full-population tail is
\[
 A_{\rm art}X^{1/4}e^{-L^2},\quad
 A_{\rm art}=C_{\rm pop}\max_{D\to D,D^t}
    (D_0+AD_2+AD D_3+(A^2/2)D_4).
\tag{R1.16}
\]
In R1.16 `AD_2` means A times D_2, while `AD D_3` means A times the
coefficient-majorant constant D times D_3; the D_m's are moment constants.
No true gamma or RS function is extended to the artificial rays.

Only on `|q|>X/2` use `M_H=int_0^infinity|Phi|` and `X>=4R`. Then
`|u-Re z|>=X/4`. Gaussian splitting gives the remote normalized bound
\[
 A_{\rm far}X^{-7/4}e^{\pi X/8-X^2/(128B)},\quad
 A_{\rm far}=(M_H/g_-)\max(J_0,J_0^t).
\tag{R1.17}
\]
The gamma height exponential has been paid explicitly, rather than
lost by applying the global bound already at the near edge V.

In addition to the classical RS/gamma onsets and R1.6, sufficient gates are
\[
 L\ge16,\quad X\ge\max(1,4R),\quad X-V\ge X/2,\quad V\le X/4,
 \quad a(X+V)-a(X-V)<1,\quad4\le a_{\min}^2,
\]
\[
 V\ge\max(2R,R+Y+1,32B),\qquad |\Re\lambda_{\epsilon n}|\le1,
\]
\[
 L^2\ge(P+1)\log X+\log^+ A_{\rm mod},\quad
 L^2\ge3\log X+\log^+ A_{\rm art},
\]
\[
 X^2/(128B)\ge\pi X/8+\log X+\log^+ A_{\rm far}.
\tag{R1.18}
\]
The tail gates put each of the three tails, for field and direct time,
below `X^-11/4`. They are eventual for fixed r,b. `4<=a_min^2` suffices
for the retained-coefficient size estimate from Note05's odd/even ratio
bound; retaining exact Q needs no new coefficient derivative estimate.
These are analytical sufficient onsets, not certified numerical heights.

## 5. Error table, jets, time and residual

Splitting the exact canonical convolution at the fixed real window,
insert `H0=S_N+Q_X,4+(H0-f_4)`. Subtract R1.3--4. The complete ledger,
after division by G(X), is

| Source | Field | Direct first T derivative |
| --- | --- | --- |
| Initial canonical RS mismatch | C_4 M_0 X^-11/4 | C_4 M_0^t X^-11/4 |
| Local weighted-order remainder, both arms and all N | C_pop e B_3[M] X^-11/4 | C_pop e B_3[M^t] X^-11/4 |
| True moderate tail | R1.15, absorbed to X^-11/4 | Included through D^t |
| Artificial exponential-polynomial tail | R1.16, absorbed to X^-11/4 | Included through D^t, through degree six |
| True remote tail | R1.17, absorbed to X^-11/4 | Included through J^t |
| Exact cutoff transfer and retained Q | Retained inside the same integral | Fixed data/endpoints; kernel differentiated |

Let `A_f=C_4 M_0+C_pop e B_3[M]+3` and
`A_t=C_4 M_0^t+C_pop e B_3[M^t]+3`. The field bound `G(X)A_f X^-11/4`
holds on the enlarged chart. Radius-1/2 Cauchy disks give factors
`a!2^a<=48` for 0<=a<=3 on the target chart. With
`C_chi>=sup_target G(X)/|G(z)|`, a sufficient norm constant in R1.1 is
`C_chi(48 A_f+A_t)`. All errors are compared to the same canonical h.
The first-time estimate came from R1.10, not a differentiated allowance.

For `L_heat=partial_T-partial_d^2`, `[L_heat,Q_T]=0`. The base frozen
exponentials solve heat exactly, as does R1.4 because its endpoints,
partitions and data are fixed. Therefore
\[
 (\partial_T-\partial_z^2)F^{[2,4]}=0,\qquad
 \partial_z(\partial_T-\partial_z^2)F^{[2,4]}=0.
\tag{R1.19}
\]
Consequently `E_T=E_zz` is a further identity-level check after the
independent reconstruction bound. Zero residual does not pay mismatch.

## 6. Comparisons, failed shortcuts and disposition

Degree-four Taylor truncation is `P_2+c_3 q^4`; it additionally includes
`kappa_4 q^4/24`, of weight three. Thus the old growing-degree theorem
cannot be obtained by renaming its degree as p, or vice versa.
On a single carrier
\[
 (\gamma/2)Q_T^2e^{\lambda d+T\lambda^2}
 =\frac\gamma2[(d+2T\lambda)^2+2T]e^{\lambda d+T\lambda^2}.
\]
At d=0 the frozen **p=1** arithmetic expression agrees pointwise with
Note10's target-centered first correction, evaluated at X. The latter
re-centers h,beta,gamma at every target z and has a nonzero differentiated
residual. Its spatial derivatives and error theorem are not transferred.
The p=2 term adds further information even at d=0.

Preserved failed/insufficient estimates: coefficient counting without
R1.7 cannot establish accuracy; fixed-mode convergence misses X^1/4;
using K=1 with p=2 leaves an X^-5/4 RS allowance; bounding q by V creates
avoidable logarithms; zero residual does not control the initial mismatch.
At fixed T>0, conversion of R1.1 to the smaller outer envelope still
allows `X^-11/4 exp(TL^2/16-pi^2 T/64)`, which grows. This failure of an
upper allowance is not a lower bound on actual error.

This is an approximation milestone under [avoid01][a01], not an RH
criterion. The [result index][results], [heat cluster][heat],
[controls12][controls] and [avoid index][avoid], especially [02][a02],
[07][a07] and [12][a12], retain their source status. Euler-factor and
finite-prime controls fail unchanged full canonical coefficients;
weighted-square/cutoff controls fail the full canonical completion;
reflected, smooth and positive-primitive controls lack the same complete
gamma/arithmetic identity. Their suitable heat identities remain valid;
this comparison excludes no collisions.

**Disposition — Analysis, Sol:** accept R1.1 and R1.19 at bounded r1 scope,
with named classical inputs and same-model internal review. R01-AN01 r1
CLOSED; R01's requested finite p=2 comparison Complete. R02 may now consume
the weighted-remainder mechanism. Parent HDA-A02 Partial, HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled are unchanged. Next: **Analysis — Sol**,
R02-AN01 r1, every fixed order, after saving this note and assessment.

[inputs]: ../numerics/R01_ANALYTICAL_INPUTS_20261026.json
[review]: ../reviews/01_FIRST_FINITE_FLUCTUATION_ASSESSMENT_20261026.md
[continuation]: 01_ANALYSIS_CONTINUATION_20261026.md
[n16]: ../../ansatz/notes/16_GAUSSIAN_FLUCTUATION_HIERARCHY_20261026.md
[n05]: ../../ansatz/notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[digamma]: https://dlmf.nist.gov/5.11.E2
[sector]: https://dlmf.nist.gov/5.11.ii
[rs]: https://arxiv.org/pdf/1904.12438v2
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
