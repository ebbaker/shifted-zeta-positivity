# CTF-E07 R2: all-radius compact-coefficient bound

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0022**, **Continue radial drift research**.

**Complete — proved analytical return to the frozen [E07 R2 request][packet].**
For the exact prescribed cutoff, weight and drift,
\[
\boxed{B_1\le b_\star=\frac{69}{4}<\frac{455}{24}.}
\tag{1}
\]
Consequently the existing compact constants obey
\[
\boxed{\kappa_1-\kappa_{1,\rm rad}\ge\frac{41}{24}>0,
\qquad \kappa_{1,\rm rad}\le\frac{679}{24}+B_0.}
\tag{2}
\]
At the same actual compression integral B(s), the radial compact upper
allowance is at most exp[-41B(s)/24] times the old allowance, strictly
smaller when B(s)>0. No bound on B through a collision deadline is obtained.

| Next task | Type and recommended model | Readiness and output |
| --- | --- | --- |
| **CTF-E08 — default, R2 assessment** | **E — Sol:** assess this fixed scalar proof and integrate its supported consequence | Ready; the [continuation][next] gives the bounded assessment scope |
| CTF-B02 | B — Astra: any new source-specific estimate needs a conceptual choice | Parent partial; no further candidate is tested here |
| CTF-E03 / CTF-B03 | E — Sol / B — Astra | Gated; no numerical acquisition or coverage extension follows |

The [sole Progress05 register][progress] and [model workflow][workflow]
govern status and routing. The [result index][results] and [avoid index][avoid]
were consulted, especially [controls][controls], [target classification][a01],
[shape-only premises][a02], [scoped claims][a07] and [combined bounds][a12].
This is a numerical-constant milestone under avoid/01, proved by inequalities;
it is not another noncollision reformulation or an RH criterion.

## 1. Fixed coefficient and exact radial reduction

Keep the complete theta source and prepared radial class on
\(\mathscr P=[0,1/2]\times[1,6]\), the conservative feedback equation,
actual fixed-mark spectral jets, and the functional of [Note40][n40].
With \(r=|X|\), the frozen quantities are
\[
\omega=(1+r^2)^{-2},\quad v=\lambda X,\quad
\lambda=1+\frac1{1+r^2},\quad b=\beta X,\quad
\beta=\eta\log r,\quad \eta=h(4r-2),
\]
where h is exactly [Note31][n31]'s exponential cutoff. No cutoff or
coefficient definition is changed.

For r>0, differentiating these radial vector fields gives
\[
(b\cdot\nabla)v=\beta(\lambda+r\lambda')X,\qquad
(v\cdot\nabla)b=\lambda(\beta+r\beta')X.
\]
Thus their difference is \(r(\beta\lambda'-\lambda\beta')X\).
Since \(\beta'=\eta'\log r+\eta/r\), define
\[
C(r)=\frac{r}{(1+r^2)^2}
 \left|\eta\{r\lambda'\log r-\lambda\}
             -\lambda r\eta'\log r\right|,
\qquad B_1=\sup_{r\ge0}C(r).
\tag{3}
\]
The vector field b is identically zero near the origin, so C has its
smooth zero continuation there. In particular the eta' term in (3)
has not been omitted.

We shall use only the elementary bounds
\[
0\le\eta\le1,\quad \lambda\le2,\quad
p(r):=\frac r{(1+r^2)^2}\le\frac12,\quad
\frac{r^2}{(1+r^2)^2}\le\frac14,\quad
|r\lambda'|=\frac{2r^2}{(1+r^2)^2}\le\frac12.
\tag{4}
\]
Indeed \(2r\le1+r^2\) proves the bound on p, and
\((1+r^2)^2\ge4r^2\) proves the other rational bounds.

## 2. The exact cutoff derivative

For 0<t<1 put A=exp(-1/t), D=exp(-1/(1-t)). Direct differentiation gives
\[
h'(t)=\frac{AD}{(A+D)^2}
       \left(\frac1{t^2}+\frac1{(1-t)^2}\right)\ge0.
\tag{5}
\]
For 0<t<=1/2 the prefactor is at most
A/D=exp(-1/t+1/(1-t)). Here exp(1/(1-t))<=exp(2), while
\[
t^{-2}e^{-1/t}\le4e^{-2},\qquad
(1-t)^{-2}e^{-1/t}\le4e^{-2}.
\tag{6}
\]
For the first inequality set x=1/t>=2; the derivative of x^2 exp(-x)
is x(2-x)exp(-x)<=0. For the second use (1-t)^(-2)<=4 and
exp(-1/t)<=exp(-2). Equations (5)–(6) give h'<=8 on this half.
The identity h(1-t)=1-h(t) gives h'(1-t)=h'(t), so
\[
0\le h'\le8\quad(0<t<1),\qquad
0\le\eta'\le32\quad(1/2<r<3/4).
\tag{7}
\]
The constant extensions are smooth and flat at the endpoints, and eta'
vanishes outside the transition. No extremum search is used.

## 3. Three domains, including the entire exterior

**Zero region, 0<=r<=1/2.** Both b and its derivatives vanish, so C=0.

**Transition, 1/2<r<3/4.** We have
\(|\log r|\le\log2<1\), since \(\log2=\int_1^2du/u<1\).
Apply (4) and (7) to the two terms of (3):
\[
p\eta\bigl(|r\lambda'||\log r|+\lambda\bigr)
\le\frac12\left(\frac12+2\right)=\frac54,
\]
\[
p\lambda r|\eta'||\log r|
=\lambda|\eta'||\log r|\frac{r^2}{(1+r^2)^2}
\le2\cdot32\cdot\frac14=16.
\tag{8}
\]
In the derivative term the two powers of r are paid together; no large
independent bound on r is needed. Therefore C<=69/4 on the transition.

**Exterior, r>=3/4.** Here eta=1 and eta'=0 exactly. For 3/4<=r<=1,
\(|\log r|\le\log(4/3)<1\), so the first estimate in (8) gives C<=5/4.
For every r>=1,
\[
0\le\log r=\int_1^r\frac{du}{u}\le r-1\le r,
\qquad p\log r\le\frac{r^2}{(1+r^2)^2}\le\frac14.
\]
Consequently the whole infinite tail satisfies
\[
C(r)\le p\lambda+(p\log r)|r\lambda'|
\le1+\frac14\frac12=\frac98.
\tag{9}
\]
These inequalities include r=1; smoothness covers both cutoff endpoints.
The three domains exhaust all space. Their largest allowance is 69/4,
proving (1). This single conservative bound is independent of T, a and
the logarithmic derivative of the source.

## 4. Strict compact coefficient and exponential comparison

Use the exact constants of Note40 and [Note42][n42], already integrated
in manuscript Section7.4, equation (7.25):
\[
\kappa_1=\max\{10+B_1,265/24+B_1+B_0,6,30+B_0\},
\qquad \kappa_{1,\rm rad}=265/24+B_1+B_0.
\]
Because B0 and B1 are nonnegative, the radial entry dominates the first
and third entries. Thus
\[
\kappa_1-\kappa_{1,\rm rad}
=\max\{0,455/24-B_1\}
=455/24-B_1\ge\frac{41}{24}.
\tag{10}
\]
In particular \(\kappa_1=30+B_0\) and
\(\kappa_{1,\rm rad}\le265/24+69/4+B_0=679/24+B_0\).

Let \(\mathcal F=G+\|\omega\mathcal R\|_2^2+\|J_2\|_2^2\)
and \(B(s)=\int_0^s\alpha(q)dq\). On the same compact subinterval
of the inherited lifespan, compare the compact **upper allowances**
\[
U_{\rm old}(s)=(\mathcal F(0)+E_0)
   e^{\kappa_0s+\kappa_1B(s)},\qquad
U_{\rm rad}(s)=(\mathcal F(0)+E_0)
   e^{\kappa_0s+\kappa_{1,\rm rad}B(s)}.
\]
The source, data, kappa0 and actual B are the same. Since alpha>=0,
\[
\boxed{\frac{U_{\rm rad}(s)}{U_{\rm old}(s)}
=e^{-(455/24-B_1)B(s)}\le e^{-41B(s)/24}.}
\tag{11}
\]
For B(s)>0 this ratio is strictly less than one. At B=0 the allowances
coincide. In particular the inherited radial weighted estimate gives
\[
\mathcal F(s)+E_0\le(\mathcal F(0)+E_0)
    e^{\kappa_0s+(679/24+B_0)B(s)}.
\tag{12}
\]
This compares bounds on the same energy; it is not a ratio between
different solutions or their actual energies. All other source/data
budgets are retained. Direct analysis with the same fixed information
can use (1) as well; no acquisition-cost or physical first-jet gain is claimed.

## 5. Controls, retained terms and completion boundary

The scalar proof uses only the prescribed cutoff, drift and weight.
It uses no theta sign or arithmetic distinction. The exact control
\(\Phi_*(u)=(64u^4+6)e^{-17u^2/4}\) still collides at
\((T,a)=(1/4,2\sqrt6)\in\mathscr P\) and remains admitted by the
prepared radial estimates. With the **same theta operator**, retain
both preparation-residual terms from Note40 (23) and Note42 (17):
\[
\mathcal R_{*,0}=[\mathcal A_T,K_1*]W_*^{\rm raw}
 +K_1*(M_T^*W_*^{\rm raw}),\qquad
M_T^*=r\log r\{(\log\rho_{*,T})'-\ell_T'\}.
\tag{13}
\]
Its raw mismatch does not vanish as theta's does. The joint sphere
cancellation \((\Theta+\mathcal R)(1)=0\), actual fixed-mark J2,
full commutator, all other cutoff derivatives, and inner-ball energy
remain. None is replaced by a zero residual or a separate singular quotient.
Its finite collision deadline is compatible with (11)–(12); B has not
been controlled through that deadline.

The other [registered controls][controls] keep their distinct premises
and locations, as checked in Note40, Section4:

| Control | Distinction retained; no new rejection by B1 |
| --- | --- |
| Weighted-square | Complete unit coefficients/full reflection fail; registered witnesses near 44.13 and 83.53 are outside a in [1,6] |
| Finite-prime orbit | Selected-prime identities do not give full reflection; high-gap events have no fixed compact location |
| Reflected super-Gaussian | Full reflection survives, complete square arithmetic fails; pi/4<1 |
| Smooth shape / positive primitive | Named shape/primitive data do not identify the complete source; no event location in this rectangle is imported |
| Euler-factor | Arithmetic/conductor differ from literal theta; negative Laguerre witnesses are not automatically double events in this box |
| RH-conditional endpoint | Original RH assumption and escaping-height qualifications remain |
| Atomic / continuous compact | Atoms are outside the imported smooth source-function class; smoothing does not identify the complete theta amplitude |

No control fails the scalar cutoff/drift inequality itself. No new
collision exclusion, threshold transfer, numerical campaign or alternate
functional is inferred. E07 R2 is complete at its declared one-proof
boundary. Parent B02 remains partial, and E03/B03 remain gated.

The parent derived and checked this proof with two read-only delegated
checks: scalar calculus and the compact/control accounting. Both use
the same model and inherited ultra effort. These are internal LLM checks
with shared imported premises, not E08 execution or independent specialist
review. No formal assessment or manuscript integration is asserted here.
No optimization, floating sampling, interval arithmetic, source quadrature,
PDE evolution, second coefficient or external literature acquisition was used.

**Next: [E] CTF-E08 — Sol**, assess this frozen return and integrate only
its supported compact consequence; [Note45][next] gives the continuation.

## Input identity and public history

All six frozen input hashes in R2 matched. These identities bind the
bytes read and preserved, not the validity of their mathematical claims.

| Input | SHA-256 |
| --- | --- |
| Note31 | `9d2a9832f3a128d3bb2c3fc37eb7ab83547f2f9d35c16c82847ef7994795b8ec` |
| Note40 | `abbb999e364006ea3558869a29d39a648922c85f0df71e09fa23dd1c0b90440e` |
| Note42 | `895a3f9524bb871d66f6ceae840e55f013f2a012df934abb78499dd73261634c` |
| Note43 | `e2e0bf9f529cd255885e444ea350095e323074372711cd4d14e407cc1e569706` |
| Review23 | `44c40831c6eb9103dba4d793e029a934ca02c42fdd5ef378b47bf451a69ba8a0` |
| Manuscript | `394ce86b6a5ab432015f1b4b3ed86bed3896070618fbe84afc196e44fb7bd238` |
| Issued E07 R2 request | `8fedc5dfa97842a02445fc32fb17dab2b097205bf23435f4551129d21baa4116` |

The issued R1/R2 requests, Notes39–43, Review23, manuscript and companion
were preserved. Only the E07 R2 progress entry and current navigation
are refreshed alongside this return and continuation. No manuscript
snapshot, build or numerical record is created for this analytical task.

Actual model/effort were read from the recorded turn context: thread
`01a1880f-c572-7ab1-910d-9b92d72e4e85`, turn
`01a18810-84ee-78f0-8b43-b23a8690db27`.
The [unique public archive][history] is chat0022; current capture counts,
times and hashes belong to its registry. Subagent correspondence is excluded.

[packet]: ../research-progress/handoffs/CTF-E07_RADIAL_COMPACT_COEFFICIENT_REQUEST_R2_20261029.md
[next]: 45_RADIAL_COMPACT_GAIN_CONTINUATION_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[n31]: 31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n42]: 42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[history]: ../chat-histories/0022_2026-10-29T14-28-17Z_continue-radial-drift-research.json
