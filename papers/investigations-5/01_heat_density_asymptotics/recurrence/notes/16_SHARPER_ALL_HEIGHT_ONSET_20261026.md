# R05-AN06: a linear sufficient all-height onset

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from this turn's source metadata. Recurrence **chat0006**, thread
`01a178a3-9572-7bf2-b0a0-bd4d47f796ab`, turn
`01a178a3-9a35-7a51-ae02-9e3dadf65497`.

**Return to HDA-R05-AN06 r1. Proved in-note from the named inputs;
same-model internal assessment only.** Write

    R=r+1, Y=b+1, W=R+Y, d=ceil(W), nu=d+1>=4.

For every fixed positive dyadic chart r,b, the sufficient onset can be
replaced by

    L_new=64 nu,                 X_new=2^(128 nu+8).          (S1)

Every accepted [Note09 P1][n9] center with L=log(X/(4pi))>=L_new
meets all uniform classical domains, structural/calibration gates and
half-target truncation gates. X>=X_new is a stronger dyadic sufficient
condition. Keep p=floor(L/2), K=2p, V=8sqrt(2)L and 1<=T<=2.
Notes06/09--11's unchanged delivered-error allocations then give combined
outer-envelope (3,1) error <=exp(-L²/4).

The earlier L_*=2^22 nu^4 and X_*=2^(2L_*+8) in [Note11][n11]
remain valid fallbacks. This is a sharper **sufficient upper allowance**,
not a measured onset, an optimal threshold, or a lower bound for actual
error. No numerical or machine-symbolic research check was needed or
run. [Input versions][inputs], [work record][work] and [Review12][review]
record provenance, composition and limits.

## 1. Frozen scope and where the old loss entered

Keep the complete canonical theta/xi source, h(T,z)=H(-T,z), h_T=h_zz,
H(0,z)=xi((1+iz)/2)/8, canonical gamma branches and the actual two-arm
outer envelope. Both arms, every n<=N=floor(sqrt(X/(4pi))), all C_0
through C_K, exact adjacent-cutoff transfer and the bounded real
completion integral remain. Freeze the chart, p,K,N, coefficients,
partitions and reference endpoints under z,T differentiation. The full
buffered chart is |Re z-X|<=R, |Im z|<=Y; the target retains its original
unit buffers, spatial orders 0--3 and first time derivative.

Use Note11 U2--12 unchanged:

    H=A=C_Gamma=c_o=1, D=4, D0=3, g_-=1/64,
    C_H=M_H^*=1/4, C_tail=640, C_o=C_chi=3^(nu-1),
    C_cal=nu+31, X_cl=64nu.                                 (S2)

The new derivation does not change their complex-disk, real-window,
source or full-chart domains. It uses Note05's simultaneous finite local
and source bounds, rather than substituting a growing p in a fixed-order
asymptotic.

The losses can be separated precisely:

| Cost | Existing bound and its role | Treatment here |
| --- | --- | --- |
| Gaussian moments and true/artificial tails | Note05 G10--19 and Note11 U13 give log Tbar=O(nu²). | Keep the same explicit moment majorant, including direct-time degree 2p+4. |
| Local Bell polynomial and matched RS remainder | Common factorial (2p+4)! and base Qbar^(p+1). | Keep both; no Stirling approximation or hidden order-dependent constant. |
| Multiplication of chart cost by order | G14/U14 upper-bound log Jbar by (6+log Qbar+log Tbar)(p+1)log(p+2). | Retain log Tbar additively instead. |
| Logarithmic growth | C20/U16 further use L log(L+2)<=L^(3/2), forcing a bound quadratic in the already O(nu²) coefficient. | Bound each additive term directly by a fixed fraction of L² for L>=64nu. |
| Moderate/remote true source | Fixed logarithms are O(nu²); moderate height power and remote Gaussian have separate rates. | Keep their different height dependences and pay them separately. |
| Classical/structural/calibration gates | Exponential height dominates the finite chart and window scales. | Prove them continuously below; they do not require the quartic log-height. |

Thus the gain does not require sharper actual Gaussian moments or a new
factorial theorem. The old aggregation obscured a sufficient linear chart
scale. It remains a valid conservative proof, not an incorrect one.

## 2. Additive local and artificial-tail envelope

Retain exactly Note11 U13's rational majorants

    Ebar=3^(8nu²), Sbar=32nu, Qbar=2^15 nu²,
    Tbar=Ebar Sbar²,
    Jbar(p)=Tbar(p+2)Qbar^(p+1)(2p+4)!.                      (S3)

They dominate both moment systems at c=theta=1/2, delta=1/4. Note05
G11--14 and G19, and Note11 U14--15, give

    Q_p<=C_Q Jbar(p), C_Q<=3Tbar,
    A_art,p^(1/2)<=C_pop Jbar(p),
    A_mod^(1/2)<=640Tbar, A_far<=16Tbar,
    log Tbar<=18nu², log Qbar<=15+2nu<=23nu/4.               (S4)

Superscript (1/2) labels theta, not a square root. All constants are
finite, and the original Q_p is still Note05 G9's combined field/time
cost. The exact fixed choice

    C_Q=48M_0+M_0^t+49 C_pop exp(1)

also implies 8C_Q>=392 C_pop exp(1)>392 C_pop. This will let the
same majorant pay the artificial tail with its actual half-budget factor.

For every L>=64nu>=256,

    log(L+4)<=L/32,
    p+1<=L/2+1<=129L/256,
    2p+4<=L+4<=65L/64.                                     (S5)

For the first inequality, exp(8)>260 follows already from its terms
through degree four: 1+8+32+512/6+4096/24=297. The derivative of
L/32-log(L+4) is positive for L>=256. Thus this is a continuous
inequality, not a sampled logarithmic estimate.

The fixed part of the local cost is bounded by

    log(24)+(nu-1)log3+2log Tbar<=37nu²,

using log24<4, log3<2 and 4+2nu<=nu² for nu>=4. Since
log(m!)<=m log m at every integer m>=1, S3--5 prove

    log^+(8C_o Q_p)
      <=log(8C_o C_Q Jbar(p))
      <=37nu²+log(p+2)+(p+1)log Qbar+log((2p+4)!)
      <=(592+8+2967+2080)L²/65536
      =5647 L²/65536 <3L²/32.                              (S6)

For transparency the four rational summands are, in order,
37nu²<=592L²/65536;
log(p+2)<=L/32<=8L²/65536;
(p+1)log Qbar<=2967L²/65536;
and (2p+4)log(2p+4)<=2080L²/65536.
There is no order-dependent constant behind S6.

By the second inequality in S4 and 8C_Q>392C_pop,

    log^+(392C_o A_art,p^(1/2))<3L²/32                     (S7)

with the identical S6 majorant. This uses the same chart upper bound;
it does not assume the actual artificial or local costs are equal.

## 3. All four half-target inequalities

The required conditions are exactly [Note10 C19][n10], retaining the
factors **8 and 392**. First, p>=L/2-1 and log X=L+log(4pi)>L give

    (p+3/4)log X-3L²/8
      >=L²/8-L/4>=7L²/64>3L²/32.                           (S8)

S6 therefore closes the local/matched-source gate, with strict margin
larger than L²/64 after the last displayed bound.

For the fixed true-tail costs, S4 and log(392*640)<18 give

    log^+(392C_o A_mod^(1/2)), log^+(392C_o A_far)
      <=18+2nu+18nu²<=20nu²
      <=5L²/1024<L²/32.                                    (S9)

The logarithm bound follows from 392*640<2^18 and exp(1)>2;
18+2nu<=2nu² for every nu>=4. The remote multiplier 392*16 is smaller.
Since L>=256,

    (9/4)log X <=(9/4)(L+3)<=L²/4,
    (1/4)log X <=(1/4)(L+3)<=L²/16.                        (S10)

Combining S9--10 pays the moderate right side by <9L²/32; combining
S7 and S10 pays the artificial right side by <5L²/32. Both are strictly
below the required (61/8)L². These are comparisons of the actual
separate upper allowances, without discarding the height-sensitive
moderate source or the artificial full X^(1/4) population.

For the remote term, X=4pi exp L>12exp L, exp L>=2L and L>=256 imply
X>24L and X>64pi. Therefore

    pi X/8 < X²/512,
    X²/512 >9L²/8 >(3/8+1/32)L².                           (S11)

S9 and S11 imply
X²/256>pi X/8+3L²/8+log^+(392C_o A_far), paying the remote gate.
The favorable X^(-7/4) is still safely dropped as in C19.
Each of the four error terms is at most one eighth of the target after
outer conversion, so truncation uses at most half of exp(-L²/4).

## 4. Structural, classical and calibration gates at every height

The rate improvement does not waive the non-rate gates of C21. They
can be checked directly, using for all L>=64nu>=256

    W<=nu-1<L/64, V<=12L, X>12exp L>=2L³.                   (S12)

The last inequality uses the positive exponential series term L³/6.

| Required gate | Uniform payment |
| --- | --- |
| Full chart and all classical domains | X>X_cl=64nu, X>4(W+1), and X>64; Note11 U2--12 then retain their disk/window/complex domains. |
| Real window and ellipse width | V<X/4 and 2(V+2)<X/4 follow from 24L+4<L³/2. Hence X-V>X/2. |
| Cutoff span, strong ellipse | Note10 C18 applies at every L>=16: 4(V+2)/sqrt(2pi X)<1/2. Also a(X+V)-a(X-V)<=V/sqrt(2pi X)<1, so at most two exact branches. |
| All retained RS terms | K=2p<=L; V/(4pi)<=L and exp L>=2L give L<=(X-V)/(4pi). This is the retained finite-sum gate, distinct from the real RS remainder's all-K validity. |
| Local curvature and weighted remainder | DV/X<24/L²<1/2; 2AV²/X<128/L<=1/2. |
| Full buffer/tail geometry | V>=8L>max(2R,W+1,64). Optional V<=log²X follows from V<=12L<L². |
| Strong real slope | X>30=10D0 and pi<16/5 give D0/X<1/2-pi/8. This implies the weaker arithmetic slope gate too. |
| Separate damping | X>6(L+2) and X>6 give 2{(3/X)(pi/4+L/2)+9/X²}<3(L+2)/X+18/X²<1. |
| Actual outer calibration | C_cal=nu+31<L and 1+L<2L give C_cal(1+L)<2L²<X. Thus U12's c_o=1 applies on the full rectangle and time interval. |
| Ellipse logarithm | 2V<X/4 implies |Log(1+q/X)|<=1/3 for |q|<=2V, hence |Log((X+q)/(4pi))|<=L+1, as required in Note06 E18. |

The simple pi bounds are the same elementary rational bounds used in
Note10 C18--21. This table explicitly pays the source, moderate,
artificial, remote, buffer, retained-coefficient and stronger quadrature
geometry conditions. Positive reference-node, interior-guard and
rounding tolerances, including epsilon_lambda<=1/2 and the final-circuit
accumulation guard when that arithmetic model is used, remain separately
chosen delivered-error contracts. Height alone does not certify them.

Nothing depends on actual Q_p being monotone. Equations S5--12 hold for
every real L>=64nu and the inequalities L/2-1<=p<=L/2 cover both sides
of every later p jump. Note05's full-population estimate holds at every
N; the bounded correction retains the exact adjacent-cutoff transfer
when N or a real branch cutoff changes. The theorem makes no assertion
of continuity or differentiation with respect to X across those jumps.

P1's strict descriptor witnesses are still required. Excluded descriptor
boundary centers are not admitted, and no uniform positive separation
sigma follows from S1. Accepted centers have finite strict gate witnesses
because the new bounds have slack; the descriptor witnesses retain their
own input/separation cost.

## 5. Unchanged error delivery and quantitative gain

For every accepted exact query, keep

    epsilon_X=(1/(2*3^(nu-1)))exp(-3L²/8),
    (1/(8*3^(nu-1)))exp(-3L²/8)<e
                 <(1/(4*3^(nu-1)))exp(-3L²/8).             (S13)

Retain Note06 E5's scale allowance epsilon_g A_0<=epsilon_X/2 and
each of the five categories <=epsilon_X/20; use Notes09--10's finite
factor-controlled constructions. Their center-normalized evaluation
error is <=epsilon_X, so outer conversion costs at most
3^(nu-1)exp(L²/8)epsilon_X=exp(-L²/4)/2. Adding the proved half-target
truncation closes exactly the original total target for field, spatial
orders0--3 and first time. Input uncertainty and an additional mixed T,z
channel are not newly supplied. The frozen exact residual and residual_z
remain zero; independent rounded channels retain only their paid defects.

For fixed r,b the sufficient delivered precision and bit bounds stay
3L²/(8log2)+O_(r,b)(Llog L), C(N+1)Q^40 work and CQ^20 streamed storage,
with input length and center separation retained. This note changes the
proved starting domain, not the algorithms, population size, internal
arithmetic theorem or an observed runtime.

For a declared family, take all integer nu>=4 and
r=b=(nu-3)/2, positive dyadic radii with the prescribed chart integer.
The improvement, in fact valid on every positive dyadic chart, is

    L_*/L_new=2^16 nu³>=2^22.                               (S14)

| nu | r=b | Earlier sufficient L_* | New sufficient L_new | Exact ratio |
| --- | --- | --- | --- | --- |
| 4 | 1/2 | 2^30 | 256 | 2^22 |
| 8 | 5/2 | 2^34 | 512 | 2^25 |
| 16 | 13/2 | 2^38 | 1024 | 2^28 |

These are symbolic substitutions in proved bounds, not numerical
certificates or evaluations of the field. The dyadic center in S1 obeys

    log(X_new/(4pi))=(128nu+8)log2-log(4pi)>64nu+1,

because log2>1/2 and log(4pi)<3. The binary exponent decreases from
2^23nu^4+8 to 128nu+8, a strict difference 2^23nu^4-128nu. No huge
integer center is expanded. Even the smaller bound is not a practical
evaluation guarantee or a sharp minimal onset. No claim that linear
chart dependence is necessary is made.

## 6. Inputs, checks, controls and disposition

The new proof is elementary algebra from Notes05/10/11 and unchanged
Notes06/09 delivery. Exact file versions are in the input manifest.
Two read-only subagents examined additive costs and gates; a subsequent
read-only assessment checked the written proof. These checks share the
same model and inherited inputs and are not independent specialist review.
No finite research inequality check, provider replay, full-field sweep,
zero search or search near the sufficient height was run.

Selected inherited primary passages were re-read online: [DLMF5.11(ii)](https://dlmf.nist.gov/5.11#ii), the complex log-gamma/digamma omitted-term
bounds; and [Polymath v2 Proposition6.2 and (56)](https://arxiv.org/html/1904.12438v2#S6.SS2), the real RS expansion at
Tprime>0 and positive integer K. This is a selected hypothesis/formula
check, not a fresh audit of the full classical proofs. Earlier coefficient
proof-access and source-review limitations in Notes06/09--11 remain.

Under [avoid01][a1] this is an approximation/evaluation milestone, not
an RH-equivalent criterion. Read the [result index][results],
[heat-flow cluster][heat], [control screen][controls] and
[avoid index][avoid], particularly [shared-premise limits][a5] and
[separate error bounds][a12]. Euler-factor/finite-prime controls fail
unchanged complete canonical coefficients; weighted-square and finite
cutoff controls fail the complete canonical xi/RS completion; reflected,
smooth and positive-primitive controls fail the same full gamma/arithmetic
identity. Atomic finite-profile controls also fail the canonical complete
source; RH-conditional endpoint controls fail ordinary Dirichlet arithmetic.
Their heat evolution may survive. This is an applicability screen only:
no collision, zero, RH or physical-consumer exclusion follows.

**Disposition:** AN06 r1 is Complete and CLOSED at its bounded analytical
scope following Review12. Broad R05 stays Partial at complete evaluator
software/certification. R04/R06 NOT_STARTED, HDA-A02 Partial, HDA-17
Partial, HDA-18 Gated and HDA-20 unfulfilled remain unchanged. N02 r1
is a separate supporting task with its original cases/caps, unexecuted
here. The next analytical target should be a specified uniform improvement
to coefficient/integral bounds at identical accuracy; no new task is
silently executed. [Continuation17][next] gives the precise handoff.

[n5]: 05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md
[n6]: 06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md
[n9]: 09_FINITE_PROVIDER_ALGORITHMS_20261026.md
[n10]: 10_EFFICIENT_PROVIDERS_AND_TOTAL_COST_20261026.md
[n11]: 11_EXPLICIT_CALIBRATION_AND_HEIGHT_ONSET_20261026.md
[inputs]: 16_SHARPER_ONSET_INPUTS_20261026.json
[work]: 16_SHARPER_ONSET_WORK_RECORD_20261026.json
[review]: ../reviews/12_SHARPER_ONSET_ASSESSMENT_20261026.md
[next]: 17_ANALYTICAL_CONTINUATION_AFTER_ONSET_20261026.md
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a1]: ../../../../../avoid/01_restating_the_target.md
[a5]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
