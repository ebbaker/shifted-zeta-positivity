# Signed cutoff lemma and the outer threshold eight thirds

14 October 2026 (America/New_York). Prepared for Edward Baker with substantial
LLM assistance. Recorded parent model **gpt-6-astra**, reasoning effort
**ultra**, verified from this turn's source metadata. Parallel analytic
work checked the arithmetic, cutoff bookkeeping and source constraints.
Internal review is not external peer review or formal verification.

This continues the recommended lemma in
[Note 30](30_THETA_SIGNED_CUTOFFS_AND_ANALYTIC_LOG_LOSS_20261014.md).
The result is a proved restriction of that target to a new unbounded
subdomain, not a proof on the whole suggested strip beginning at theta=5/2.
The new arithmetic argument lowers the sufficient outer-sign threshold
from three to **8/3**, with a fixed positive margin and an unevaluated
height cutoff. The exact signed cutoff estimate follows there with a
prescribed locally bounded coefficient; its allowed additive-tail version
has zero energy loss and height-uniform tail constants.

## 1. Statements and scope

Use H_t=-H_xx, h_k=partial_x^k H, E=h_0^2+h_1^2 and
L_j=h_{j+1}^2-h_j h_{j+2}, j=0,1. Put

\[
 L=\log(x/(4\pi)),\quad \theta=tL,\quad \omega=L/4.
\]

Keep the analytic carrier of [Note 17](17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md):

\[
 s_+=(1+ix)/2,\quad
 Q=M_t(s_+)\zeta\bigl(s_++\tfrac t2\alpha(s_+)\bigr),
 \qquad \Gamma=|M_t(s_+)|.
\]

Here M_t(s)=M_0(s) exp(t alpha(s)^2/4), alpha=M_0'/M_0, with the
explicit nonvanishing Stirling carrier M_0 given in that note and the
Polymath source below. No physical jet enters a denominator in this
definition.

**Theorem 1 (new outer subdomain).** For each fixed epsilon>0 there is
X_epsilon<infinity such that uniformly for

\[
 x\ge X_\varepsilon,\qquad 0<t\le1/2,\qquad
 \theta\ge8/3+\varepsilon,                         \tag{1}
\]

Q is nonzero and, writing phi=arg Q,

\[
 \frac1{2|Q|}
 \left(h_0,\frac{h_1}{\omega},\frac{h_2}{\omega^2},
                  \frac{h_3}{\omega^3}\right)
 = (\cos\phi,-\sin\phi,-\cos\phi,\sin\phi)
                       +O_\varepsilon(L^{-1}).     \tag{2}
\]

Consequently E>0 and both full forms L_0,L_1>0 in (1), after increasing
X_epsilon. This implies both stationary signs, without imposing
stationarity on an individual block. Reflection gives the full signs at
negative heights. The boundary theta=8/3 is not included.

**Theorem 2 (recommended cutoff lemma on the new subdomain).** Fix
a=pi/16. Use exactly Note 19's common-carrier moments on

\[
 \Omega_N=\{(v,n):0\le v\le V_N=\tfrac12\log N,
                              \ n\le e^{2v}\},
\]

and form h_k^(N) and L_j^(N) from the retained moments with all their
cross terms. The full E and full stationary sets remain the observations.
There are explicit source-defined A_j(t,x), independent of N and locally
bounded, such that for every integer N>=8 throughout (1),

\[
 \boxed{L_j^{(N)}\ge-A_j(t,x)E,\qquad j=0,1.}     \tag{3}
\]

This is Note 30 equation (5) with p=0. The coefficients are not uniformly
bounded as height tends to infinity. With the additive allowance explicitly
permitted in Note 30, a sharper statement is

\[
 \boxed{L_j^{(N)}\ge-e^{-2ax}B_j e^{-cN^2}
                         \ge-B_j e^{-cN^2},}       \tag{4}
\]

with source constants B_j,c>0 independent of t,x,N. Thus (4) has A_j=0.
All constants and proofs of the cutoff statements are in Section 5.

These results prove the requested type of estimate on the portion
theta>=8/3+epsilon of the suggested strip. They do not establish its lower
portion 5/2<=theta<=8/3, the smaller cusp, or the finite bridge from 112
to X_epsilon. The decisive advance is arithmetic outer coverage; the
cutoff conclusions use that independently proved coverage. No logarithmic
loss is needed in this subdomain, so this does not demonstrate a new
logarithmic-loss mechanism in the remaining cusp.

## 2. Two complete maximal block estimates

For T>=1 and any interval I of integers in (M,2M], M>=1, use

\[
 \left|\sum_{n\in I}n^{-iT}\right|
 \ll T^{1/14}M^{5/7}+T^{-1/14}M^{29/28},           \tag{5}
\]

and

\[
 \left|\sum_{n\in I}n^{-iT}\right|
 \ll T^{1/9}M^{11/18}+M/T.                         \tag{6}
\]

The primary inputs are Olivier Robert, *On van der Corput's k-th derivative
test for exponential sums*, Theorem 3 and Section 5.2, equation (20),
[author PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
[published DOI](https://doi.org/10.1016/j.indag.2015.11.009).
The derivative theorem gives (5) from lambda_4 comparable to T/M^4;
an interval of length J<=M has bound J lambda_4^(1/14)+
J^(3/4) lambda_4^(-1/14), which is at most (5).

For (6), the standard A and B operations are

\[
 \mathsf A(k,l)=\left(\frac{k}{2k+2},\frac{k+l+1}{2k+2}\right),
 \qquad \mathsf B(k,l)=(l-1/2,k+1/2).
\]

Their exact chain is

\[
 (0,1)\xrightarrow{B}(1/2,1/2)
 \xrightarrow{A}(1/6,2/3)
 \xrightarrow{A}(1/14,11/14)
 \xrightarrow{B}(2/7,4/7)
 \xrightarrow{A}(1/9,13/18).
\]

Robert defines the estimate on arbitrary segments I_f contained in
[M,2M], with complete bound (T/M)^k M^l+M/T. Its class includes the
exact logarithmic phase (alpha=0). The factor 2pi in the phase is absorbed
in the constant. Thus (6) is already maximal over shortened intervals;
no unproved completion rule or omitted secondary term is used. Conjugation
handles the opposite phase sign. Empty and one-point blocks are harmless.

## 3. Uniform weighted replacement above eight thirds

Follow [Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
on the shrinking complex disc |z-x|<=1/L. Write z=u+iv,
ell=log(u/(4pi)), theta_u=t ell and

\[
 w_\pm(z)=\sigma+i\tau,\qquad
 N_{\rm RS}=\left\lfloor\sqrt{u/(4\pi)+t/16}\right\rfloor.
\]

The Riemann--Siegel cutoff N_RS is distinct from the source cutoff N in
Theorem 2. For sufficiently large x, the inherited disc estimates give

\[
 \theta_u\ge8/3+\varepsilon/2,\quad |\tau|\asymp u,
 \quad \sigma\ge1/2+\theta_u/4-\delta,
 \quad 0\le\delta=O(L^{-1})\le\varepsilon/100.     \tag{7}
\]

It suffices to take 0<epsilon<=1, by decreasing a larger margin. In
particular sigma>=7/6. All estimates below are uniform up to t=1/2,
including growing theta_u.

For fixed r>=0, set

\[
 S_r=\sum_{n\le N_{\rm RS}}(\log n)^r
                   e^{t\log^2n/4}n^{-w}.
\]

We prove S_r-(-1)^r zeta^(r)(w)=O_(epsilon,r)(L^-1).
Split at Y=exp(ell/4). The low-index discrepancy is at most

\[
 \frac t4\sum_{n\ge2}(\log n)^{r+2}
                         n^{-(1/2+3\theta_u/16-\delta)}. \tag{8}
\]

Let theta_0=8/3+epsilon/2 and s=theta_u-theta_0>=0. The exponent
in (8) is at least 1+epsilon/16+3s/16, because
3epsilon/32-delta>=epsilon/16. Thus (8) is bounded by

\[
 \frac{D_{\varepsilon,r}}{4\ell}
               (\theta_0+s)2^{-3s/16}=O_{\varepsilon,r}(\ell^{-1}),
 \qquad D_{\varepsilon,r}=
 \sum_{n\ge2}(\log n)^{r+2}n^{-1-\varepsilon/16}<\infty.
\]

The omitted ordinary zeta tail is O_r(ell^r exp(-ell/24)), using
sigma>=7/6. It remains to bound the weighted high indices Y<n<=N_RS.
On each exact dyadic block (M,min(2M,N_RS)], the weight

\[
 W_r(y)=(\log y)^r e^{t\log^2y/4}y^{-\sigma}
\]

is decreasing for large ell: its logarithmic derivative multiplied by y
is at most 4r/ell-1/2+delta+O(1/u)<0. Abel summation therefore bounds
the weighted block by a constant times W_r(M) times either (5) or (6).
Every shortened final block is included.

Put beta=log M/ell. Choose (5) for 1/4<=beta<=5/13 and (6) for
5/13<=beta<=1/2+O(1/(u ell)). Apart from logarithmic factors, the powers
of exp(ell) in the bounds are

\[
 \begin{aligned}
 E_{4a}&=\frac{1+3\beta}{14}
              -\frac{\theta_u}{4}\beta(1-\beta)+\delta\beta,\\
 E_{4b}&=-\frac1{14}+\frac{15\beta}{28}
              -\frac{\theta_u}{4}\beta(1-\beta)+\delta\beta,\\
 E_{Pa}&=\frac{1+\beta}{9}
              -\frac{\theta_u}{4}\beta(1-\beta)+\delta\beta,\\
 E_{Pb}&=-1+\frac\beta2
              -\frac{\theta_u}{4}\beta(1-\beta)+\delta\beta.
 \end{aligned}                                                   \tag{9}
\]

At theta_u=8/3 and delta=0 the principal endpoint values are

| exponent | left endpoint | right endpoint |
| --- | --- | --- |
| E_4a, beta in [1/4,5/13] | 0 | -2/507 |
| E_Pa, beta in [5/13,1/2] | -2/507 | 0 |

Both quadratics are convex, so these endpoint checks control their full
intervals. Also E_4b-E_4a=-1/7+9beta/28<=-1/52 on its interval,
and E_Pb<=-3/4 before the small disc perturbation. Nothing is discarded.
Increasing theta_u by epsilon/2 subtracts at least 3epsilon/128 from
each principal exponent, since beta(1-beta)>=3/16. The perturbation
delta beta costs at most epsilon/200. The excess beta beyond 1/2 costs
o(1), uniformly because theta_u<=ell/2. After increasing x, all four
exponents are at most -epsilon/100. There are O(ell) dyadic blocks, so

\[
 \sum_{Y<n\le N_{\rm RS}}(\log n)^r
           e^{t\log^2n/4}n^{-w}
       =O_{\varepsilon,r}(\ell^{r+1}e^{-\varepsilon\ell/100}).
\]

Combining the three pieces proves the claimed weighted replacement. The
fixed gap epsilon is essential: both the low-index summability margin and
some high-block endpoint margins vanish at the boundary 8/3.

## 4. Complete analytic comparison and physical signs

The input is D.H.J. Polymath, *Effective approximation of heat flow
evolution of the Riemann xi function*, Theorem 1.3, equations (13)--(24):
[primary paper](https://arxiv.org/html/1904.12438v2#S1).
The two analytic branches and all imported errors are as matched in
Notes 17 and 19. We change their arithmetic bound, not the approximation
formula or its hypotheses.

The complete positive weight sum in e_A+e_B is still O(u^(1/4)), and
the per-index error multiplier is O(L^2/u). Hence

\[
 e_A+e_B=O(L^2u^{-3/4}),\qquad
 e_{C,0}\ll\exp[-\ell/4-\theta_u\ell/16]
                       \ll u^{-5/12}.              \tag{10}
\]

This includes all three imported errors. Carrier magnitudes on the disc
are comparable to Gamma. The upper-half-disc comparison and Schwarz
reflection therefore give the analytic estimate

\[
 H(t,z)-(Q_+(z)+Q_-(z))=O_\varepsilon(\Gamma/L)
                  \quad (|z-x|\le1/L).             \tag{11}
\]

The half-plane sigma>=7/6 gives
zeta(7/6)^(-1)<=|zeta(w)|<=zeta(7/6), together with bounded fixed-order
logarithmic derivatives. Therefore Q is nonzero and |Q| is comparable
to Gamma. Cauchy's estimate applied after (11) yields all four physical
jets. No moving floor cutoff is differentiated. The carrier calculation
of Note 17 applies with 7/6 in place of 5/4 and proves (2).

Increase X_epsilon until omega>=1 and every component error in (2) is
at most 1/8. Note 17's exact phase-uniform algebra then gives

\[
 E\ge2|Q|^2\ge\frac{2\Gamma^2}{\zeta(7/6)^2},\quad
 L_0\ge\frac{31}{16}|Q|^2\omega^2>0,\quad
 L_1\ge\frac{31}{16}|Q|^2\omega^4>0.              \tag{12}
\]

These constants follow from normalized norm >=1/2 and normalized
Laguerre forms >=31/64, including the factor 4|Q|^2. This proves
Theorem 1 and supplies a source-derived energy envelope for Theorem 2.
It assumes no lower bound on a sampled physical energy.

As a consequence, any hypothetical sequence of positive-time real
collisions (T_k,x_k), 0<T_k<=1/2, with |x_k| tending to infinity must
satisfy limsup T_k log(|x_k|/(4pi))<=8/3. This improves the analogous
threshold-three consequence and does not assert the existence of a collision.

## 5. Exact cutoff estimate and complete Gaussian remainder

Let

\[
 a=\pi/16,\quad \beta_0=\pi\cos(4a)=\pi/\sqrt2,
 \quad C_0=2(2\pi^2+3\pi),\quad c=\beta_0/2,
 \quad D_0=C_0/(2\beta_0),
\]

and define fixed complete-source moments

\[
 \mathsf M_k=C_0\int_0^\infty(v+a)^k
          \exp\{v^2/2+10v-\beta_0e^{4v}\}\,dv,
                  \qquad 0\le k\le3.              \tag{13}
\]

These finite positive constants are prescribed from the existing source
majorant. They dominate every retained absolute moment for 0<=t<=1/2.
The exact paired identity in Note 19, with both its Hermitian and
bilinear sectors, gives

\[
 |L_j^{(N)}|\le e^{-2ax}\mathsf M_j\mathsf M_{j+2}.
                                                               \tag{14}
\]

One may verify the factor by using
(y+z)^2+(y-z)^2=2(y^2+z^2) inside the two pair integrals, including
their factor 1/4. This is stronger than separately bounding the three
jet products by unrelated constants.

Set

\[
 A_j(t,x)=
 \frac{e^{-2ax}\mathsf M_j\mathsf M_{j+2}\zeta(7/6)^2}
      {\Gamma(t,x)^2}.                             \tag{15}
\]

The denominator is the explicitly nonzero analytic carrier, not E. Thus
A_j is independently prescribed, independent of N, and locally bounded
through every finite point of (1). Equations (12)--(14) prove (3), with
a spare factor two. This is an existence theorem with an unevaluated
X_epsilon; it does not provide a practical numeric height cutoff or a
globally bounded A_j. The growth of (15) at large height is permitted by
the stated locally bounded-loss target.

For the sharper paid-tail result, the omitted common-coordinate moment
T_k^(N) is bounded by the integral in (13) over v>=V_N. For v>=1,

\[
 \log(v+a)\le v,\qquad
 v^2/2+13v\le(\beta_0/2)e^{4v}.
\]

For the second inequality, e^{-4v}(v^2/2+13v) is decreasing there,
and its value at one is less than beta_0/2. Consequently, when N>=8,

\[
 T_k^{(N)}\le \frac{C_0}{2\beta_0N^2}e^{-cN^2}
                  \le D_0 e^{-cN^2},\qquad k\le3. \tag{16}
\]

The complete pair-tail payment from Note 19 is

\[
 |L_j-L_j^{(N)}|\le e^{-2ax}
 (R_jT_{j+2}+R_{j+2}T_j+T_jT_{j+2}),
\]

where R_k<=mathsf M_k. It includes retained/omitted, omitted/retained
and omitted/omitted pairs. Therefore, with

\[
 B_j=(\mathsf M_j+\mathsf M_{j+2})D_0+D_0^2,
\]

we obtain |L_j-L_j^(N)|<=e^{-2ax}B_j exp(-cN^2). Theorem 1's full
positivity proves (4). These constants are uniform in positive height
and 0<=t<=1/2. The inequality for L_j^(N) is asserted only in (1),
where the independent sign input holds.

## 6. Why the cutoff qualification matters

The raw cutoff does not inherit exact full stationarity: h_{j+1}=0
does not imply h_{j+1}^{(N)}=0. The proof never makes that substitution.
Nor does a sharp common-coordinate boundary remove the endpoint effects
in Note 22. They are contained in the retained moments and complete tail.

At a hypothetical E=0, the exact unpaid target would require
L_j^(N)>=0 for every N. That is stronger than the full identity L_j=0
and is not implied by it. This observation is a limitation of the
formulation, not a theta counterexample. The additive version (4) is the
more stable formulation of the current result.

A possible future observation retaining the full amplitude is

\[
 J_j^{(N)}=-h_j h_{j+2}^{(N)}\quad\text{on }h_{j+1}=0.
\]

It has exact difference J_j^(N)-L_j=h_j(h_{j+2}-h_{j+2}^(N)), whence

\[
 |J_j^{(N)}-L_j|\le\sqrt E\,e^{-ax}T_{j+2}^{(N)}. \tag{17}
\]

In particular J vanishes at E=0 without an extra cutoff-positivity
condition. This preserves all source terms in its amplitude factor.
Equation (17) is an exact error bound, not a new signed estimate for J
in the remaining cusp. A theorem there must still identify the actual
theta arithmetic controlling its adverse product.

## 7. Validation and continuation

The [exact rational checker](../numerics/check_hybrid_cutoff_lemma.py)
and [small receipt](../numerics/HYBRID_CUTOFF_LEMMA_CHECKS_20261014.json)
check the exponent-pair arithmetic, endpoint values, convexity and error
margins. They also retain the weaker 27/10 threshold obtained using only
third- and fourth-derivative tests as an independent arithmetic check.
All **84** checks pass. The parent replay was byte-identical to the
independent producing agent's receipt. Checker SHA256:
`582c5ff42deabec1c59aae3a36c54e46d046840d7974d991132fcfdeccd6a05f`;
receipt SHA256:
`b3a8bbb8a86bef1b7118b490ce171b14c16d27a7091ea21207240ed73c0e5f1b`.
Finite algebra checks do not prove the external exponent-pair theorem,
infinite-source bounds, or complex-disc comparison; those are the written
arguments and identified source inputs above.

Reproduce from the repository root:

```sh
python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/check_hybrid_cutoff_lemma.py --output /tmp/inv21-hybrid-cutoff-replay.json
```

The [internal review](../reviews/22_SIGNED_CUTOFF_AND_THRESHOLD_EIGHT_THIRDS_REVIEW_20261014.md)
audits the claimed subdomain and both cutoff versions. No numerical sweep,
new quadrature, or finite-height certificate was run. The finite cover
through 112 is unchanged; the new asymptotic height is unevaluated.
No manuscript revision, commit, tag or snapshot folder was made.

The next arithmetic gap is explicit: controlling the combined physical
observation when theta<=8/3, particularly the rest of the suggested
5/2-to-13/4 strip. The current proof pays small indices absolutely and
uses a hybrid block estimate at larger indices. At theta=8/3 its endpoint
margins vanish. Continuing by setting epsilon=0 is invalid; reaching the
lower strip needs a different estimate or a different split with genuinely
improved arithmetic input.

This is the same chat, thread `01a13d83-a46b-74f0-bb7c-121d159a60a0`,
registered as investigation-21 history 10. Its recorded current turn is
`01a13d8f-6ec4-7583-810c-ed920ba56c29`, with gpt-6-astra and ultra effort.
The shared recorder refreshed the prior final reply at this turn's start;
the bounded worker will capture the actual completed final response.
