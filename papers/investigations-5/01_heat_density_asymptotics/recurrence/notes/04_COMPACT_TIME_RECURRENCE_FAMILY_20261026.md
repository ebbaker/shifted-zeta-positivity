# R03: fixed compact-time recurrence family, every fixed order

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from rollout turn_context. Recurrence chat0001, thread
`01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Return: HDA-R03-AN01 r1. Proved in-note from named classical inputs;
same-model internal analytical assessment only.** This round consumes the
full fixed-order [R02 theorem][r2] after its [assessment][review2] and
packet disposition were saved; the p=2 fallback is unnecessary. For each
fixed integer p>=1 and each declared fixed `0<tau<=B<infinity`,
\[
 \boxed{\|h-F_{X,B}^{[p,2p]}\|^{(3,1)}_{X;\tau,B}
       \le C_{p,r,b}(\tau,B)X^{-(p+3/4)}}.
\tag{R3.1}
\]
The constant and sufficient onset are specified below, with no log loss.
All N arithmetic modes, both arms, RS terms C_0 through C_(2p), exact
adjacent transfer and the bounded completion integral remain. The
actual frozen residual and residual_z are exactly zero. No uniformity
at tau=0, B=infinity or p=infinity; no manuscript or numerical campaign.
[Inputs][inputs] and [Review03][review] identify evidence and review scope.

## 1. Fixed family, buffers and reusable classical constants

Keep the complete canonical theta source and normalization in the
[continuation r1][continuation], h(T,z)=H(-T,z), h_T=h_zz,
H(0,z)=xi((1+iz)/2)/8. Fix X and all its chart data under differentiation.
Use `R=r+1`, `Y=b+1`, `W=R+Y`, target `Omega_X(r,b)` and enlarged
`Omega_X(R,Y)`, with physical radii `r=ell+2`, `b=1+h_av+2`. Set
\[
 L=\log(X/(4\pi)),\quad a_X=\sqrt{X/(4\pi)},\quad N=\lfloor a_X\rfloor,
 \quad \bar B=\max(1,B),\quad V_B=8\sqrt{\bar B}L.
\tag{R3.2}
\]
The family endpoint B enters the fixed real window, not its variable T.
All real partitions, gamma derivatives, coefficients and endpoints stay
fixed in z,T. Left charts follow only by canonical reflection.

Use R01's fixed constants A,D,C_Gamma,C_tail,g_-,D0 and a0=pi/8;
a sufficiently high sectorial onset gives
\[
 |c_k|\le AD^{k-1}X^{-k},\quad
 \lambda_{\epsilon n}=-a0+\epsilon i v_n/2+\delta_{\epsilon},
 \quad v_n=\log(a_X/n),\quad|\delta_\epsilon|\le D0/X,
\]
\[
 G(X+q)\le C_\Gamma G(X)e^{|q|}\quad(|q|\le V_B),\quad
 G(X)\ge g_-X^{7/4}e^{-\pi X/8}.
\tag{R3.3}
\]
They are independent of tau,B,p after the local/window gates; their
fixed buffer/sector dependence remains. The coefficient bound comes
from an analytic ell'' disk, not a formal infinite asymptotic series.
The real classical RS mismatch is exactly R1.12. With K=2p and
`X-V_B>=X/2`, its sufficient constant is
\[
 C_{2p}=C_\Gamma\frac{2^{7/4}}7
   \Gamma(p+1/2)1.1^{2p+1}(8\pi)^{p+3/4}.
\tag{R3.4}
\]
The canonical real-source global bound is `M_H=int|Phi|`; the moderate
height-sensitive tail uses P=4 and the constant C_tail from Note05.
These original classical inputs are not strengthened at negative time.

The model is the R02 polynomial-Gaussian sum with unchanged partition
coefficients, plus
\[
 \mathcal I_{X,2p,B}(T,z)=\int_{X-V_B}^{X+V_B}
             k_T(z-u)Q_{X,2p}(u)du.
\tag{R3.5}
\]
Q retains real RS data and exact `S_m-S_N`. No real-part operation is
moved outside the complex-kernel integral and no real coefficient is
analytically differentiated.

## 2. Endpoint-dependent complex kernels and local remainder

For integers m>=0 define
\[
 M_m(\tau,B)=\sqrt2e^{R+Y^2/(4\tau)+2B}
 \sum_{k=0}^m{m\choose k}W^{m-k}(8B)^{k/2}
                  \frac{\Gamma((k+1)/2)}{\sqrt\pi},
\]
\[
 M_m^t(\tau,B)=M_m/(2\tau)+M_{m+2}/(4\tau^2).
\tag{R3.6}
\]
For every actual tau<=T<=B and z in the enlarged chart, put
`v=u-Re z` and `q=u-X`. The exact modulus of k is
`(4pi T)^-1/2 exp(y²/(4T))exp(-v²/(4T))`.
Use `|q|<=R+|v|`, `|q|,|z-u|<=W+|v|` and
`|v|<=v²/(8T)+2T`. Integrating first, then using T<=B, proves
\[
 \int |k_T(z-u)|e^{|q|}|q|^mdu\le M_m,
 \quad\int |\partial_Tk_T(z-u)|e^{|q|}|q|^mdu\le M_m^t.
\tag{R3.7}
\]
The normalized integral is
`sqrt(2)(8T)^(k/2)Gamma((k+1)/2)/sqrt(pi)` after rescaling. Thus no
T^-1/2 is silently dropped. Time differentiation uses exactly
`partial_T k=[(z-u)^2/(4T²)-1/(2T)]k`. Both inverse-time factors and
the complex exponential have been retained in R3.6.

Impose `D V_B/X<=1/2`, `2A V_B²/X<=1`. R02's local proof then applies
on this actual window, before integration, without changing its constants:
\[
 |A(q)-P_p(q)|\le eX^{-(p+1)}B_{p+1}(|q|),
\]
\[
 B_m(x)=\sum_{k=1}^m
 \frac{2^{m+k}A^kD^{m-k}}{k!}{m-1\choose k-1}x^{m+k}.
\tag{R3.8}
\]
The full initial population remains
`sum_|epsilon|=1,n<=N |b exp(lambda q)| <= C_pop G(X)X^1/4 exp(|q|)`,
`C_pop=4(4pi)^-1/4`, after `|Re lambda|<=1`.
Therefore the local field allowance is
`C_pop e B_(p+1)[M] G(X)X^-(p+3/4)`, and the **direct** time allowance
uses `B_(p+1)[M^t]`. Its maximal moment degree is 2p+4.
The source mismatch separately costs `C_(2p) M_0` and `C_(2p) M_0^t`
at the same power. We have not merely substituted endpoints into a
previously unproved compact estimate; R3.7 is its differentiated kernel
proof on the entire new interval.

## 3. Shifted moments and all-mode damping for this family

Require
\[
 D0/X\le1-a0,\qquad
 B\{(D0/X)(2a0+L/2)+D0^2/X^2\}\le1.
\tag{R3.9}
\]
Then, directly from R3.3,
\[
 |e^{T\lambda^2}|\le e^{Ba0^2+1}e^{-\tau v_n^2/4},\quad
 |e^{\lambda d}|\le e^{R+Y}e^{Yv_n/2}.
\tag{R3.10}
\]
The first gate also ensures the real-tilt bound used above. Let
`c=(Y-1)/2`, `c_+=max(c,0)`, and
\[
 W_d(\tau)=2^d+\frac{3^d}2\sum_{k=0}^d{d\choose k}
             (8/\tau)^{(k+1)/2}\Gamma((k+1)/2),
\]
\[
 \Pi_d(\tau,B)=4(4\pi)^{-1/4}4^d
 e^{R+Y+Ba0^2+1+(Y+1)/2+2c_+^2/\tau} W_d(\tau).
\tag{R3.11}
\]
The exact shell count `# {j<=v_n<j+1}<=2a_Xe^-j`, with
`cj-tau j²/4<=2c_+²/tau-tau j²/8`, proves
\[
 \sum_{\epsilon,n\le N}|b e^{\lambda d+T\lambda^2}|
              (1+|\lambda|)^d\le\Pi_d(\tau,B)G(X)X^{1/4}.
\tag{R3.12}
\]
The Gaussian integral comparison on `[j-1,j]` gives W_d explicitly.
There is no discarded weakly damped near-cutoff population.

With the exact R2.8 moment polynomial define
\[
 Z_m(B)=m!\sum_{l=0}^{\lfloor m/2\rfloor}
             \frac{B^l(W+2B)^{m-2l}}{l!(m-2l)!}.
\tag{R3.13}
\]
Since `|d+2T lambda|<=(W+2B)(1+|lambda|)`, the entire summed m-th
Gaussian moment is bounded by `Z_m Pi_m G(X)X^1/4`. R2.4's partition
sum thus controls each full level with explicit p,tau,B dependence.
These absolute envelopes retain shifted moments and damping; they are
not a signed leading asymptotic or a claim of monotone approximation.
The error proof itself integrates R3.8 against real initial population,
which is why these n-dependent shifts cause no height logarithms.

## 4. Both tails and the full onset ledger

Define the endpoint tail constants
\[
 D_m=\frac{e^{Y^2/(4\tau)}}{\sqrt{4\pi\tau}}
          2^m(64B)^{(m+1)/2}\Gamma((m+1)/2),\quad
 D_m^t=D_m/(2\tau)+D_{m+2}/(4\tau^2),
\]
\[
 J_m=\frac{e^{Y^2/(4\tau)}}{\sqrt{4\pi\tau}}
  \sum_{k=0}^m{m\choose k}Y^{m-k}(8B)^{(k+1)/2}\Gamma((k+1)/2),
 \quad J_m^t=J_m/(2\tau)+J_{m+2}/(4\tau^2).
\tag{R3.14}
\]
Require `V_B>=max(2R,R+Y+1,32B)`. On |q|>=V_B the real tilt and
kernel satisfy
`-(q-Re d)^2/(4B)+|q|<=-q²/(32B)` and `|z-u|<=2|q|`.
Gaussian splitting therefore gives tail moment bounds
\[
 D_m e^{-V_B^2/(64B)}\le D_m e^{-L^2},\qquad
 D_m^t e^{-V_B^2/(64B)}\le D_m^t e^{-L^2}.
\tag{R3.15}
\]
This checks the prescribed enlarged window even when B<1, since
bar(B)/B>=1. Keep `H_p(x)=1+sum_{j=1}^p C_j(x)` from R2.4. Put
\[
 A_{\rm mod}=C_{\rm tail}\max(D_0,D_0^t),\quad
 A_{{\rm art},p}=C_{\rm pop}\max\{H_p[D],H_p[D^t]\},\quad
 A_{\rm far}=(M_H/g_-)\max(J_0,J_0^t).
\tag{R3.16}
\]
Each expression is explicit in p,tau,B and fixed classical constants.
Polynomial evaluation retains coefficient constant D separately from
moment subscript D_m. The normalized tails, for both field and direct
time, are bounded by
\[
 \begin{array}{ll}
 A_{\rm mod}X^{P-7/4}e^{-L^2},& V_B<|q|\le X/2\quad\hbox{true data},\\
 A_{{\rm art},p}X^{1/4}e^{-L^2},& |q|>V_B\quad\hbox{polynomial completion},\\
 A_{\rm far}X^{-7/4}e^{\pi X/8-X^2/(128B)},& |q|>X/2\quad\hbox{true data}.
 \end{array}
\tag{R3.17}
\]
For the first line, retain the actual height exponential in the real
canonical field. Only in the last line use its global bound M_H; for
X>=4R, `|u-Re z|>=X/4`, and splitting its Gaussian pays both the lost
gamma exponential and the J moments. No true gamma or RS function is
extended along the artificial rays. The polynomial degree is 2p;
direct artificial time needs degree 2p+2.

A sufficient **complete** onset consists of:

| Obligation | Gates, in addition to fixed classical RS/gamma onsets |
| --- | --- |
| Full target buffers/analytic logarithm | X>=max(1,4(R+Y+1)), L>=16, V_B<=X/4 |
| Window and canonical real source | X-V_B>=X/2, a(X+V_B)-a(X-V_B)<1 |
| Retained RS coefficient size | 2p<=a_min², a_min=sqrt((X-V_B)/(4pi)) |
| Weighted local remainder | D V_B/X<=1/2, 2A V_B²/X<=1 |
| Entire mode population/shifted moments | Both gates R3.9 |
| Gaussian tail domination | V_B>=max(2R,R+Y+1,32B) |
| True moderate tail at required rate | L²>=(P+p-1)log X+log^+ A_mod |
| Artificial tail at required rate | L²>=(p+1)log X+log^+ A_art,p |
| True remote tail at required rate | X²/(128B)>=pi X/8+(p-1)log X+log^+ A_far |

Here `log^+t=max(0,log t)`. These inequalities put each tail below
`X^-(p+3/4)` and retain every order/endpoint constant before absorption.
For every fixed p,tau,B,r,b they are eventually satisfied. This gives
sufficient analytical height-onset dependence, without a numerical X0
or a claim of endpoint-independent onset. Possible original log²X
real-chart restrictions can also be retained as `V_B<=log²X`; this is
eventual and does not change the proof, which uses the real RS theorem
at every positive u in the window.

## 5. The comparison norm and the actual residual

Let `s_p=p+3/4` and define
\[
 A_{f,p}(\tau,B)=C_{2p}M_0+C_{\rm pop}e B_{p+1}[M]+3,\quad
 A_{t,p}(\tau,B)=C_{2p}M_0^t+C_{\rm pop}e B_{p+1}[M^t]+3.
\tag{R3.18}
\]
In the exact initial-data heat convolution, split at the fixed window.
On it insert `H0=S_N+Q_X,2p+(H0-f_2p)`. Retain Q, subtract the finite
whole-line transform of `P_p`, and use R3.4,7,8,17. This proves on the
enlarged chart
`|E|<=G(X)A_f,p X^-s_p` and **directly**
`|E_T|<=G(X)A_t,p X^-s_p`. The errors paid are independently source
mismatch, local weighted-order defect, moderate true tail, artificial
tail and remote true tail; none is replaced by a residual argument.

Both h and F are holomorphic in z on the buffers. Radius-1/2 Cauchy disks
give `|partial_z^a E|<=a!2^a G(X)A_f,p X^-s_p`, 0<=a<=3, on the target.
With the fixed chart comparison `C_chi>=sup_target G(X)/|G(z)|`, take
\[
 \boxed{C_{p,r,b}(\tau,B)
       =C_\chi[48 A_{f,p}(\tau,B)+A_{t,p}(\tau,B)]}.
\tag{R3.19}
\]
This is a concrete majorant for R3.1. C_chi has no endpoint dependence.
The equal-endpoint case tau=B is the restriction of the same smooth
T>0 functions; its time derivative is defined on a neighborhood, not
by differentiation of a one-point allowance.

Every finite frozen U_j is a full Gaussian transform of exponential-
polynomial initial data. The fixed bounded integral has piecewise
bounded data and permits dominated T and z differentiation on compact
positive-time intervals. Therefore exactly
\[
 (\partial_T-\partial_z^2)F_{X,B}^{[p,2p]}=0,\qquad
 \partial_z(\partial_T-\partial_z^2)F_{X,B}^{[p,2p]}=0.
\tag{R3.20}
\]
The error equation `E_T=E_zz` is now a cross-check and supplies the
alternative time factor `8 A_f,p` on the target, if useful. R3.6 and
R3.18 retain the actual direct-kernel costs rather than hiding them in
this alternative. There is no moving time/window constraint to
differentiate, localized-error commutator, or unaccounted boundary term.

## 6. Endpoint deterioration and precise limits

| Quantity | Dependence that remains |
| --- | --- |
| Field/local kernel moments | exp(Y²/(4tau)+2B), powers of sqrt(B) through degree 2p+2, W shifts |
| Direct first time | In addition, tau^-1 and tau^-2, moments through 2p+4 |
| Entire evolved population | exp(B pi²/64+2c_+²/tau), W_d(tau) with powers through tau^-(d+1)/2 |
| Shifted moment reconstruction | Z_m(B), including d+2T lambda and powers B^l, m<=2p |
| RS order constants | Gamma(p+1/2)1.1^(2p+1)(8pi)^(p+3/4) |
| Artificial tails | Full H_p coefficients and moments through 2p+2 for time |
| Tail and height onset | V_B>=32B, local B L²/X gates, R3.9, log A_mod/art/far and p log X |

Every displayed majorant degenerates in at least one joint limit. It is
not claimed optimal. In particular the onset is not uniform as tau->0,
B->infinity or p->infinity. The prescribed window agrees with R01--02
when tau=1,B=2; their constants and gates specialize consistently.
For overlapping compact families with different B, their models need
not be identical because their retained integrals have different endpoints.
Comparing through the same h gives the sum of their paid norm allowances;
this is not an additional physical join.

The remaining outer-carrier conversion at each fixed T>0 still permits
\[
 X^{-(p+3/4)}e^{TL^2/16-\pi^2T/64}.
\tag{R3.21}
\]
It grows as X->infinity with p fixed. This preserves the failed estimate
and its scope: an upper allowance fails to prove outer smallness; no
lower bound on the actual error or universal obstruction follows.
No fixed-p comparison supplies a regulator-uniform physical transfer,
coefficient-provider conditioning, working precision, quadrature cost or
useful runtime. N is still of order sqrt(X), and the bounded integral
has not been removed.

For a proposed joint limit, the first unpaid step is a **simultaneous
parameter bound** on the displayed Bell/moment/RS constants and tail
onsets along the proposed p(X),tau(X),B(X), before outer normalization.
This note establishes neither such a joint parameter choice nor its
resulting inequality. For a continuous-s extension, the first new input
is a uniform s/partial_s comparison between the bounded deformation and
whole-line coefficients, including the differentiated artificial tails
in the same norm. The exact generating identity alone does not pay it. A canonical comparison
away from s=1 would additionally require a specified complete initial-data/
completion family: the local A_s deformation alone does not define xi data
for s different from one.

## 7. Three-round disposition and next deliverable

| Round | Proved scope | Rate in the requested (3,1) norm | Retained limit |
| --- | --- | --- | --- |
| R01-AN01 r1 | p=2,K=4; 1<=T<=2; full fixed buffers | X^-11/4, no logs | Integral, all modes, onset/cost limits |
| R02-AN01 r1 | Each fixed p>=1,K=2p; 1<=T<=2 | X^-(p+3/4), no logs | Constants and onsets depend on p |
| R03-AN01 r1 | Each fixed p>=1,K=2p; declared 0<tau<=T<=B<infinity | Same exponent, explicit R3.19 | Endpoint-dependent constants/onsets; no joint limit |

All three are proved in-note from named inputs, with same-model internal
assessments only. The frozen residual and its first spatial derivative
are zero in every row; this does not erase the independently paid
initial RS and gamma-polynomial mismatches. The broader ansatz program
can consume the new **natural-scale** fixed-order/compact-family field
and jet/time allowances. Its outer-scale, cost and physical questions
remain separate.

The [result index][results], [heat cluster][heat], [controls12][controls]
and [avoid index][avoid] apply, especially [reformulations01][a01],
[shared premises02][a02], [scope07][a07] and [separate bounds12][a12].
The control screen remains explicit: Euler-factor/finite-prime controls
fail full unchanged ordinary coefficients; weighted-square/cutoff
controls fail the full canonical xi/RS completion; reflected, smooth and
positive-primitive controls lack the same gamma/arithmetic identity.
Their suitable heat identities survive. No collision/RH conclusion or
physical-transfer result follows from these approximation theorems.

**Disposition — Analysis, Sol:** accept R3.1--20 with [Review03][review].
R03-AN01 r1 CLOSED; bounded R03 fixed compact-family question Complete.
R01 and R02 were saved and assessed in dependency order before activation.
HDA-A02 remains Partial; parent HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled remain. No fourth direction is executed.

**Recommended next deliverable — Analysis, Sol, subject to a new request:**
a bounded controlled-order-growth audit of these explicit constants on
[1,2], asking whether some declared `p(X)<=c L` with `K=2p` and the same
window meets an outer-carrier error target. First bound the simultaneous
logarithms of B_(p+1)[M], Gamma(p+1/2), H_p[D], and every onset along that
range; retain all modes and the integral. Return the paid range or the
first failed inequality, without numerical or manuscript work. This
choice directly addresses R3.21. It is a future R05 question, not an
inferred growing-order consequence of the three accepted fixed-order rows.

[r2]: 03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md
[review2]: ../reviews/02_FIXED_ORDER_HIERARCHY_ASSESSMENT_20261026.md
[continuation]: 01_ANALYSIS_CONTINUATION_20261026.md
[inputs]: ../numerics/R03_ANALYTICAL_INPUTS_20261026.json
[review]: ../reviews/03_COMPACT_TIME_RECURRENCE_ASSESSMENT_20261026.md
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
