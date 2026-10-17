# Theta-specific signed cutoffs and analytic logarithmic loss

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 14 — Review quaternion theta handoff](../chat-histories/0014_2026-10-15T02-29-33Z_review-quaternion-theta-handoff.json), [Chat 13 — Continue quaternion theta geometry](../chat-histories/0013_2026-10-15T00-47-29Z_continue-quaternion-theta-geometry.json). Use this investigation’s [local registry](../chat-histories/index.json) and [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

14 October 2026 (America/New_York). Prepared for Edward Baker with substantial
LLM assistance. Recorded parent model **gpt-6-astra**, reasoning effort
**ultra**, verified from this chat's source turn metadata. Parallel internal
analytic readings and an independent internal audit support the arguments.
This note proves two general implications and proposes arithmetic targets;
it proves no new theta sign estimate or coverage theorem.

The starting sources, read in order, are [Handoff 29](29_COLLISION_ANALYSIS_CONTINUATION_AND_CHAT_HISTORY_HANDOFF_20261014.md),
[Note 28](28_COLLISION_SCALES_AND_DELAYED_COMPARISONS_20261014.md),
[Review 20](../reviews/20_COLLISION_BEHAVIOR_AND_LOGARITHMIC_LOSS_REVIEW_20261014.md),
and [Note 27](27_RESULTS_ASSESSMENT_AND_RESEARCH_PATHS_20261014.md).
Source formulas come from [Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md),
with the limitations of [Notes 21](21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md)
and [22](22_PROPER_SOURCE_FILTERS_AND_THETA_CORRELATIONS_20261014.md) retained.

## Research position

Write h_k=partial_x^k H, E=h_0^2+h_1^2,
L_j=h_{j+1}^2-h_j h_{j+2}, and S_j={h_{j+1}=0}, for j=0,1.
The manuscript already proves the stationary predecessor and universal
collision pole L_j/E=-r/s+O(1), where s=T-t and r=floor(m/2).
Note 28 refines its finite part, explains stronger canceling poles in a
positive-delay split, and proves the conditional logarithmic-loss criterion.
None of those statements supplies the missing theta-specific estimate.

Preserve the exact stationary combination

\[
 \tfrac12P_j+Q_j=L_j-\mu h_j^2,
 \qquad \mu=(\pi/16)^2+(1/4)^2.
\]

Separate nonnegative loss budgets for P and Q can destroy cancellation of
orders s^{-r}, although the total normalized deficit has only order s^{-1}.
Changing the delay cannot change the combined current observation.

The promising interpretation of logarithmic slack is **quantitative**:
it may allow a source cutoff to grow while tolerating polynomial growth of
the estimate's constant. It is not a weaker qualitative local condition
for the present analytic stationary germs, as the following lemma shows.

## 1. Local analytic rigidity of logarithmic losses

**Lemma.** Let S be a semianalytic set near a finite point p. Let E>=0 and
L be real analytic in an ambient neighborhood. Fix M>0 and finite q>=0.
Suppose on S near p that

\[
 L\ge-K E[1+\log_+(M/E)]^q,                         \tag{1}
\]

where K is bounded there and the right side is defined as zero at E=0.
Then on a possibly smaller neighborhood in S there is a finite C>=0 with

\[
 L\ge-CE.                                         \tag{2}
\]

Conversely (2) implies (1), with K=C. The resulting C is an existence
constant; this argument does not construct it from the theta source.

**Proof.** If (2) fails in every neighborhood, choose z_n tending to p
in S, with E(z_n)>0, -L(z_n)>0 and E(z_n)/[-L(z_n)] tending to zero.
Consider the semianalytic graph

\[
 Z=\{(z,u):z\in S,\ E(z)>0,\ -L(z)>0,\ u>0,
                         \ E(z)=u[-L(z)]\}.
\]

Its closure contains (p,0). Real analytic curve selection gives an arc
(z(rho),u(rho)) from (p,0) into Z for rho>0. The analytic functions on
this arc have finite nonzero leading terms

\[
 u(\rho)=a\rho^k(1+o(1)),\qquad
 E(z(\rho))=b\rho^m(1+o(1)),\qquad a,b>0,
\]

with k,m positive integers. Here E(p)=0 follows from u tending to zero
and local boundedness of L. Consequently (1) would require

\[
 u(\rho)^{-1}\le K[1+\log_+(M/E(z(\rho)))]^q
                  =O((1+|\log\rho|)^q),
\]

contradicting u^{-1} of order rho^{-k}. At E=0, (1) already gives L>=0.
This proves the assertion. QED.

The external input is analytic curve selection, as stated and proved in
Jesús M. Ruiz, *Basic Properties of Real Analytic and Semianalytic Germs*
(1986), (7.2), printed p.40:
[published article](https://www.numdam.org/item/PSMIR_1986___4_29_0.pdf).
The graph argument above is the application needed here.

For theta, S_j is analytic and E=0 already implies L_j=0 on S_j.
The lemma applies separately to both stationary sets, including singular
points and the semianalytic restriction t<=1/2. A strip defined using
theta=t log(x/(4pi)) is also semianalytic locally where x>4pi.
Bounds patch on compact subsets where the requisite stationary
neighborhoods are covered. No uniform constant at infinity or as t tends
to zero follows. Arbitrarily selected non-semianalytic sets of samples
are not covered by this argument.

Thus Note 28's logarithmic target remains a valid, potentially useful
estimate, but a locally bounded coefficient in it does not permit a
logarithmic-only blowup of the adverse analytic ratio on a full stationary
germ. The distinction between an explicitly proved source bound and a
nonconstructive local existence statement is essential. This lemma cannot
be used to define a proof coefficient by taking the observed quotient.

## 2. How a cutoff family can produce the logarithm

**Conditional transfer lemma.** Suppose that, on a declared stationary
domain, independently established nonnegative A,B, a constant c>0, a
finite p>=0 and an integer N_0>=1 give, for every integer N>=N_0,

\[
 L_j\ge-A N^p E-B e^{-cN^2}.                       \tag{3}
\]

The constants are uniform in N and locally uniform through candidate
events. Then, for every fixed M>0, a source-prescribed locally bounded C
gives

\[
 L_j\ge-C E[1+\log_+(M/E)]^{p/2}.                 \tag{4}
\]

**Proof with constants.** Put ell=1+log_+(M/E),
d=log_+(B/M) when B>0 and d=0 when B=0, and choose for E>0

\[
 N=\left\lceil\max\left\{N_0,
             \sqrt{c^{-1}\log_+(B/E)}\right\}\right\rceil
\]

with the logarithm taken as zero when B=0. Then B exp(-cN^2)<=E,
and log_+(B/E)<=d+log_+(M/E)<=(1+d)ell. Hence

\[
 N\le D\sqrt\ell,\qquad
 D=N_0+1+c^{-1/2}\sqrt{1+d},
 \qquad C=AD^p+1
\]

works. If the parameters vary, require A,B,N_0,c^{-1} locally bounded
and keep p fixed; the same formula remains locally bounded. At E=0,
let N tend to infinity in (3). QED.

The choice of N in this proof optimizes a family already proved for
**every** N with the same prescribed constants. It does not choose source
coefficients after seeing an adverse quotient. Proving only one finite
cutoff, or using constants that secretly depend on an energy floor, does
not establish (3).

There is a natural theta realization of the remainder scale. In Note 19's
common-carrier domain, take

\[
 V_N=\tfrac12\log N,\qquad
 \Omega_N=\{(v,n):0\le v\le V_N,\ n\le e^{2v}\}.
\]

This retains all entering indices up to the common endpoint; it is not
an independently truncated raw-index rectangle. The complete moment
majorant has the form

\[
 (v+a)^k\exp\{\tau v^2+10v-\pi\cos(4a)e^{4v}\}.
\]

For fixed 0<a<pi/8, bounded time and sufficiently large N, its omitted
moments are bounded by B_k exp(-cN^2), with a smaller c>0 absorbing
the polynomial and logarithmic factors. Note 19's complete pair-tail
payment then bounds |L_j-L_j^{(N)}| by the same type of remainder on
positive heights. All retained/omitted and omitted/omitted sectors are
included. This tail implication follows from the existing majorant; it
does not control the sign of L_j^{(N)}.

The missing arithmetic input can therefore be stated concretely as

\[
 \boxed{L_j^{(N)}\ge-A_jN^p E
       \quad\text{on the full }S_j,\quad N\ge N_0,\quad j=0,1.} \tag{5}
\]

An additional exp(-cN^2) payment on the right is equally acceptable.
Here L_j^{(N)} uses all retained jet cross terms, while E and stationarity
refer to the full physical jets. The coefficient A_j must be prescribed
or independently derived, locally bounded through candidate events, and
independent of N. A robust version using retained energy and a paid
stationary defect could also suffice: E_N<=2E+O(exp(-2cN^2)) and
|h_{j+1}^{(N)}|=O(exp(-cN^2)) at full stationarity. Polynomial factors
can be absorbed by decreasing c in those additive errors.

Equation (5) is a new **target**, not an established theta inequality or
evidence that it is easier than the final problem. The contribution of
(3)–(4) is to specify exactly which deterioration of a finite-resolution
arithmetic estimate the logarithmic criterion can afford.

## 3. Three concrete mechanisms and their missing inputs

| Mechanism | Cancellation retained | Exact missing input | Assessment |
| --- | --- | --- | --- |
| Complete paired blocks with growing cutoff | Both Hermitian and bilinear sectors, independent coordinates, all retained index pairs; current stationary combination before absolute bounds | A signed inequality such as (5) with at most polynomial cutoff cost, physical E, and complete endpoint and pair-tail payments | Best match to logarithmic slack; the central arithmetic task remains unproved |
| One-sided cumulative theta moments | Full physical amplitude multiplied by a cumulative signed moment, followed by integration in cutoff | Control of the aligned overshoot of the actual theta partial Fourier integral, stated below; source positivity alone is insufficient | More explicit diagnostic for a mechanism, but stronger than control of the final integrated sign |
| Improve the outer common-carrier approximation below three | Arithmetic phase inside each block and the two conjugate carrier branches | Stronger maximal weighted exponential-sum estimates, uniform on the shrinking complex disc, with all imported errors and derivative payments | Plausible route to new coverage while theta>2 has a fixed margin; does not settle the inner cusp or generate a logarithmic energy estimate |

For the third route, the nominal zeta argument has real part
1/2+theta/4. On theta>=2+eta, eta>0, nonvanishing of this carrier is
available in the absolutely convergent region. The unproved step below
the existing threshold three is the complete weighted-sum replacement
with sufficiently small error. Neither an assumed nonzero carrier near
theta=0 nor an assumed bound for zeta'/zeta there is an admissible input.
The underlying effective heat-flow approximation is in D.H.J. Polymath,
*Effective approximation of heat flow evolution of the Riemann xi function*
(2019), Theorem 1.3:
[primary paper](https://arxiv.org/html/1904.12438v2#S1).
No improved exponent or threshold is asserted here.

### Cumulative moment formulation and a stress test

On the original real source define, for j=0,1,

\[
 a_j(u)=e^{tu^2}\Phi(u)u^j\cos(xu+j\pi/2),\quad
 W=h_j=\int_0^\infty a_j(u)\,du,\quad
 F_j(r)=\int_0^r a_j(u)\,du.
\]

At full stationarity, L_j=W integral u^2 a_j(u)du. Integration by parts
gives the exact identity

\[
 L_j=\int_0^R2r\{W^2-WF_j(r)\}\,dr
       +W\int_R^\infty(u^2-R^2)a_j(u)\,du.          \tag{6}
\]

Thus the source-prescribed upper bound

\[
 WF_j(r)\le W^2+A_j E\quad\text{for every }r\ge0  \tag{7}
\]

would give L_j>=-A_jR^2 E-B sqrt(E) exp(-c e^{4R}).
Here the complete real-source envelope supplies explicit constants. For
0<=t<=1/2, k<=3 and R>=1,

\[
 \int_R^\infty u^k e^{tu^2}\Phi(u)\,du
 \le2\pi e^{-4R}\exp[-(\pi/2)e^{4R}]
 \le2\pi\exp[-(\pi/2)e^{4R}].                      \tag{8}
\]

Indeed, for u>=1, k log u+tu^2+9u<=u^2/2+12u<=(pi/2)e^{4u};
combine this with Phi(u)<4pi^2 exp(9u-pi e^{4u}) and integrate the
remaining decreasing exponential using its derivative. The tail in (6)
is bounded by the same k=j+2 moment. Thus B=2pi and c=pi/2 suffice.

For an explicit optimization, let ell=1+log_+(M/E),
R=1+(log ell)/4 and c_0=(pi/2)e^4. The tail payment is at most
2pi exp(-c_0)E/sqrt(M), since c_0>=1/2. Also
R^2<=(25/16)ell, using log ell<=sqrt(ell) for ell>=1.
Consequently (7), if proved uniformly, would give the prescribed q=1 bound

\[
 L_j\ge-\left(\tfrac{25}{16}A_j+
               \frac{2\pi e^{-c_0}}{\sqrt M}\right)
                 E[1+\log_+(M/E)].                \tag{9}
\]

Keeping the sharper R^2 expression instead yields a squared iterated-log
loss. These are conditional deductions. A less strong, integrated version
of (7) would preserve more cancellation in r.

The positive weight Phi does not make a_j positive. Even the positive
two-frequency heat family

\[
 H_*(t,x)=e^t\cos x+e^{-3T}e^{4t}\cos(2x)
\]

has H_*(T,pi)=partial_x H_*(T,pi)=0. At x=pi and t=T-s,
W=-3e^T s+O(s^2), W_x=0, W_{xx}=-3e^T+O(s), so
E=9e^{2T}s^2+O(s^3) and L_0=-9e^{2T}s+O(s^2).
For a cutoff 1<r<2, F_0(r)=-e^{T-s}, and
WF_0(r)=3e^{2T}s+O(s^2), violating (7) for bounded A_0.
This is a positive atomic-source control outside the theta class, not a
theta counterexample. The polynomial controls of Note 28 also reject
any generic analytic-heat argument that would assert the desired bound.

To prove (7) or its integrated counterpart, the special arithmetic input
must constrain the cumulative signed theta moment relative to the full
amplitude. Evenness, rapid decay, the heat equation, and positive source
weights alone do not supply it: the manuscript's existing
`prop:hc-positive-source-control` extends the collision obstruction to
strictly positive, even, entire sources with superexponential real-axis
decay ([manuscript](../manuscript/quaternion_theta_geometry.tex)).
Modular recombination may help cancel
boundary terms, but cancellation of those terms is not this inequality.

## 4. Recommended next lemma and stopping conditions

Prioritize a **uniform signed cutoff estimate of the form (5)** on one
predeclared unbounded strip, for example

\[
 x\ge X_0>112,\quad 0<t\le1/2,\quad
 5/2\le t\log(x/(4\pi))\le13/4,
\]

with both stationary sets included. The upper part overlaps known outer
coverage; the lower part would add information. The choice is a research
target, not a proved domain. Require fixed p<infinity and a priori
coefficient rules before evaluating signs. A result on this strip leaves
both the smaller cusp and the finite transition explicit.

The first analytic question is which relation among the actual theta
block amplitudes can establish the negative-part bound in (5). Existing
block modulus estimates and absolute tail payments do not provide it.
Retain the stationary condition only on the full sum; both pair sectors,
all source coordinates, and staircase entries remain mandatory. Entry
phases that cancel in x must not be credited with oscillatory decay.

Reject a proposed argument if it replaces physical E by an unproved
positive block-energy sum, drops bilinear or mixed sectors, bounds P and Q
separately without restoring their cancellation, or produces its loss
coefficient by division by measured E. A cutoff estimate whose cost
outgrows every fixed power of N may still be useful, but the simple
finite-log transfer above no longer applies automatically.

No broad numerical sweep or further finite-height certification was run.
The height-112 certificate, outer threshold-three theorem, and unresolved
inner cusp and finite bridge retain exactly their previous scope. No
manuscript revision, commit, tag, or snapshot folder was made. The
[internal assessment](../reviews/21_THETA_SIGNED_CUTOFF_AND_LOG_LOSS_REVIEW_20261014.md)
records the validation boundary.

## Chat identity and preservation

This new chat is **Continue collision and logarithmic loss…**, thread
`01a13d83-a46b-74f0-bb7c-121d159a60a0`, registered as **10** in this
investigation's history folder:
[public archive](../chat-histories/0010_2026-10-15T03-03-19Z_continue-collision-and-logarithmic-loss.json).
The title, including its ellipsis, is the actual title returned by the app.
This is distinct from archive 11 in the formal replay folder and from that
folder's older archive 10. Current counts, provenance, configuration and
hashes are in the local [registry](../chat-histories/index.json).
The source metadata records creation at 2026-10-15T03:03:19.946Z,
or 14 October 23:03:19.946 EDT, and gpt-6-astra with ultra effort.
The shared recorder and bounded exact-turn worker preserve the actual
public text; native completion-hook activation has not been verified.
