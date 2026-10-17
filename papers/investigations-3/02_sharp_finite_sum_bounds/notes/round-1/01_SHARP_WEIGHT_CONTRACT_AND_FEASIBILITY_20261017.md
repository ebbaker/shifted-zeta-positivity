# Sharp finite sum contract and first feasibility budget

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded session model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**. Same-model subagents assisted with the derivation, tail
calculation and arithmetic check. These are internal checks, not cross-model
or specialist review.

**Status: round one in progress.** The sharp native binding and sufficient
strip-transfer gate are derived below. Outward arithmetic encloses one
sharp row and a revised infinite-tail budget at the proposed time.
The [17 October continuation](02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md)
now certifies the gate on all four finite legs. The remaining finite-row
floors and complete coverage remain open; **no new bound for the de
Bruijn–Newman constant is established**.

The [opening proposal](../../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
asks for a proof-and-budget ledger before a full producer campaign. This is
that first ledger. It follows the [result-summary index](../../../../../result-summaries/README.md),
[heat-flow cluster 11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[control cluster 12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../avoid/README.md), particularly
[01](../../../../../avoid/01_restating_the_target.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../../avoid/08_normalization_and_constant_slips.md),
[10](../../../../../avoid/10_numerics_ahead_of_the_question.md) and
[12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. Fixed target and inherited domains

Set
\[
t_*=157/1000,\qquad X=6000000185827,\qquad
 y_0^2=87677/2500000,\qquad y_1^2=1-2t_*=343/500.
\]
The proposed conclusion is the quantitative milestone
\(\Lambda\le t_*+y_0^2/2=872677/5000000=0.1745354\), conditional on
completing every hypothesis of Polymath Theorem 1.2. This is a positive
numerical-bound target, not an RH-equivalent reformulation and not a claim
of competitiveness with all public bounds.

The primary theorem was re-read in [Polymath, arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2),
Theorem 1.2. Its initial verification uses \(0\le T\le X/2\); its final
region is \(x\ge x_*:=X+\sqrt{1-y_0^2}\), \(y_0\le y\le y_1\) at
\(t=t_*\). Its curved intermediate barrier is contained in
\[
[X,X+1]\times[0.1809,1]\times[0,0.16125].
\]
Indeed its lower ordinate is at least \(y_0>0.1809\), its width is less
than one, and \(t_*<0.16125\). Thus the existing barrier can be inherited
on its audited status; reducing time does not require a new barrier mesh.
The initial verification is also unchanged. See the canonical
[audit ledger](../../../../investigations-2/newman_certificate_audit/notes/1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md)
and [barrier audit](../../../../investigations-2/newman_certificate_audit/notes/5_BARRIER_CERTIFICATE_AUDIT_20261013.md).
This round does not independently regenerate those inputs.

The finite windows retain the four historical prime sets and seams:

| Natural indices | Euler primes |
| --- | --- |
| 690988 through 728999 | 2, 3, 5, 7, 11 |
| 729000 through 818999 | 2, 3, 5, 7 |
| 819000 through 1027999 | 2, 3, 5 |
| 1028000 through 3840000 | 2, 3 |

Write \(q_N=N^2-t_*/16\), \(x_N=4\pi q_N\), and
\(W_N=[x_N,x_{N+1})\). The first cutoff remains 690988: the old
\(x_{690988}<x_*<x_{690989}\) margins exceed five million, whereas the
change in each edge from time 0.16125 is less than 0.004. Adjacent
half-open windows tile without gaps; the tail starts at \(x_{3840000}\)
and overlaps the last finite window.

## 2. Native sharp lower bound

Use the canonical audit's notation
\[
b_t(m)=e^{(t/4)\log^2m},\quad
\lambda_d=(-1)^{\omega(d)}\prod_{p\mid d}b_t(p),\quad D=\prod_{p\in P}p,
\]
\[
 B_{N,n}=\sum_{\substack{d\mid D,\ d\mid n\\n/d\le N}}\lambda_d b_t(n/d),
\qquad
 A_{N,n}(y)=\sum_{\substack{d\mid D,\ d\mid n\\n/d\le N}}
 \lambda_d b_t(n/d)(n/d)^y.
\]
Both leading coefficients are one. Define the frozen quantities
\[
 g=e^{y/50-(y/2)\log q_N},\quad
 \sigma=\frac{1+y}{2}+\frac{t_*}{4}\log q_N
 -\frac{t_*}{2x_N^2}\left(1-3y+\frac{4y(1+y)}{x_N^2}\right)_+,
\]
\[
 k=\frac{t_*y}{2(x_N-6)},\quad
 M=\sum_{d\mid D}|\lambda_d|d^{-\sigma},\quad
 C=\sum_{m=2}^N b_t(m)(m^k-1)m^{y-\sigma},\quad K=gC.
\]
For real \(B,A\), \(0\le g<1\), put
\[
 U_g(B,A)=\max\left(\frac{|B-gA|}{1-g},\frac{|B+gA|}{1+g}\right)
 =\frac{|B-g^2A|+g|A-B|}{1-g^2},
\]
\[
 V_N(y)=\sum_{n=2}^{DN}U_g(B_{N,n},A_{N,n}(y))n^{-\sigma},
\quad
 L_N^\sharp(y)=\frac{(1-g)(1-V_N(y))}{M}-K.
 \tag{1}
\]
If \(L_N^\sharp>0\), then \(|f_{t_*}(x+iy)|\ge L_N^\sharp(y)\)
throughout \(W_N\). There is exactly one division by the Euler majorant
\(M\); the \(\kappa\)-correction is \(K\), without an extra division.

For completeness, let \(T_\Gamma(w)=w+\Gamma\bar w\), \(r=|\Gamma|<1\).
Then
\[
 T_\Gamma^{-1}(Bz+\Gamma A\bar z)
 =\frac{(B-r^2A)z+\Gamma(A-B)\bar z}{1-r^2}.
\]
Apply this identity to the two mollified sums, with
\(\Gamma=\gamma E/\bar E\), and use
\(|T_\Gamma(w)|\ge(1-r)|w|\). Here \(E\ne0\) already follows from
\(\sigma>1.6>(t_*/4)\log p\) for every Euler prime used. The function
\(U_r(B,A)\) is nondecreasing in \(r\). To see this, reduce to \(B\ge0\);
its three formulas are \((B-rA)/(1-r)\), \((B+rA)/(1+r)\), and
\((rA-B)/(1-r)\), on \(A\le B\), \(B\le A\le B/r^2\), and
\(A\ge B/r^2\), respectively. Their derivatives are nonnegative.
Thus replacing \(r\) by \(g\) is safe when \(V_N<1\). Bound the
\(\kappa\)-perturbation by \(gC\), then use \(|E|\le M\) to obtain (1).

The inherited window directions give \(|\gamma(x,y)|\le g_N(y)\),
\(\Re s_*(x,y)\ge\sigma_N(y)\), and \(|\kappa(x,y)|\le k_N(y)\).
This proves the freeze using the nonnegative normalized mass \(U_g\).
The unnormalized weight
\[
 W_g=(1-g)U_g=\max\left(|B-gA|,\frac{1-g}{1+g}|B+gA|\right)
\]
need not increase with \(g\); its monotonicity must not be substituted
for the argument above. The binding agrees with the canonical
[sharp-inequality review](../../../../investigations-2/newman_certificate_audit/reviews/1_CROSS_MODEL_REVIEW_OF_NOTES_1_2_20261012.md),
section 3.3. Polymath's related inequality is Lemma 8.5 in section 8.5.

## 3. Strip transfer with branch changes retained

The sufficient task, now certified in [Note 02](02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md), is to prove \(V_N(y)\le V_N(y_0)\) for every
required \(N\) and \(y\in[y_0,y_1]\). This is not inherited from the
plain-weight Dini certificate.

Here is an explicit gate. For each \(n\), let \(L=\log n\),
\(\ell=g'/g=1/50-\tfrac12\log q_N\), and, for \(e\in\{-1,1\}\), set
\[
 z_e=B+egA,\qquad d_e=1+eg,\qquad u_e=|z_e|/d_e,
 \qquad v'=g(\ell A+A').
\]
Define \(\mathcal D(z,w)=\operatorname{sgn}(z)w\) if \(z\ne0\),
and \(\mathcal D(0,w)=|w|\). Since the right slope of \(\sigma\)
is at least \(1/2\), including its positive-part kink,
\[
 D^+(u_en^{-\sigma})\le\frac{n^{-\sigma}}{d_e}
 \left[\mathcal D(z_e,ev')-
 \left(\frac L2+\frac{eg'}{d_e}\right)|z_e|\right]. \tag{2}
\]
Check the bracket for every active branch \(u_e=\max(u_-,u_+)\);
at a tie both branches must pass. This retains zeros and changes of
active branch. Finite summation and the Dini monotonicity theorem then
prove the desired transfer.

The inherited divisor patterns can reduce the number of distinct cases.
With
\[
 r_d(L)=\exp\left[\frac{t_*}{4}
 (\sum_{p\mid d}\log^2p+\log^2d-2L\log d)\right],
\quad C_0=\sum_{d\text{ active}}(-1)^{\omega(d)}r_d,
\quad C_y=\sum_{d\text{ active}}(-1)^{\omega(d)}r_dd^{-y},
\]
we have \(B=b_t(n)C_0\), \(A=b_t(n)e^{yL}C_y\).
Remove the positive \(b_t(n)\) factor in (2) and substitute
\(z_e=C_0+e\,g e^{yL}C_y\),
\(v'=g e^{yL}[(L+\ell)C_y+\partial_y C_y]\).
The full feasible \((L,\ell,y)\) domain must be enclosed. The old
substitution of the smallest feasible \(N\) into the plain gate has no
proved monotonicity for the added rational terms in (2).

The other two directions are available analytically. \(M_N\) decreases
because \(\sigma'_N\ge1/2\). For every summand of \(K_N\), the
logarithmic rate is at most
\[
 \ell+\tfrac12\log N+\rho_N\log N+1/y_0,
 \qquad\rho_N=t_*/[2(x_N-6)].
\]
For \(t\le0.162\), \(N\ge690988\), use
\(q_N>N^2/2\), \(\ell<0.52-\log N\),
\(\rho_N<0.081/N^2\), \(\log N>13\), and \(y_0>0.187\).
The rate is less than
\(0.52-6.5+0.081/N+1000/187<-0.631\), so \(K_N\) decreases.
When \(V_N(y_0)<1\), a proof of (2) therefore makes (1) nondecreasing.

If termwise monotonicity fails, a certified slab bound on the *sum* of
active derivatives remains possible. On \(J=[a,b]\), an upper bound
\(H_J\) gives
\(V_N(y)\le V_N(a)+(b-a)\max(H_J,0)\).
Insert this into (1), using \(g(a)\), \(M(a)\), and \(K(a)\), provided
the numerator stays positive. This is a fallback contract, not a
completed or costed strip certificate.

### Exact obstruction to automatic inheritance

In the generic real signed finite-sum class, take
\[
 n=16,\quad \sigma=\sigma_0+y/2,\quad g=4^{-y},\quad B=1,
 \quad A(y)=-1+3\cdot4^y-16^y.
\]
This has \(A(0)=B\). At \(y=1/2\), write \(a=\log2\); then
\(g=1/2\), \(A=1\), \(A'=-4a\), and \(g'=-a\).
The old sufficient plain bracket is
\[
 g|A'|+g'|A|-\tfrac{\log n}{2}(|B|+g|A|)=-2a<0.
\]
Both normalized branches tie at \(U_g=1\), but their weighted right
slopes, after division by \(16^{-\sigma}a\), are \(2\) and \(-10/3\).
Thus \(D^+(U_g16^{-\sigma})=2a16^{-\sigma}>0\).
The [exact rational replay](../../numerics/round-1/check_transfer_counterexample.py)
records these coefficients. This disproves generic inheritance only;
it does not show that the theta coefficients fail the new transfer.

## 4. Outward numerical pilots

The [run plans](../../numerics/round-1/PILOT_RUN_PLAN.md) declare the
single-row scope and resource cap. A same-model arithmetic check prompted
one replay with an explicit interval bound on the \(G^{-\sigma}\)
scalars. The final code and record have matching source hashes.

### One sharp row

At \(N=690988\), \(t=t_*\), \(y=y_0\), the
[pilot](../../numerics/round-1/certify_sharp_pilot.py) encloses
\[
 0.0017755269101384707588
 < L_{690988}^{\sharp}(y_0)
 <0.0017755269101384708095. \tag{3}
\]
It enumerates the active integers by \(n=Gk\),
\(G=\gcd(n,D)\), with \(\gcd(k,D/G)=1\). There are 11,024,402
nonleading terms and 22,111,615 incidences. These are coverage accounting,
not evidence for the strip transfer. The 110-bit fixed-point sum allowance
is below \(4.54\times10^{-20}\); scalar tables use the inherited
45-digit directed Decimal machinery. The new absolute-value/max weight
uses 1-Lipschitz error bounds. Four small direct enumerations and 324
exact weight identities passed. The positive table-sum correction uses
an allowance \(10^{-35}\); fewer than 3,840,000 positive additions,
table errors \(\le10^{-40}\), and 45-digit rounding give a smaller
relative accumulation error. The recorded run used 96.4 seconds and
about 132 MiB of peak resident memory.

The [full record](../../numerics/round-1/SHARP_PILOT_RECORD_20261017.json)
certifies a point in \(y\) and one window in \(x\) via section 2.
It says nothing about the minimum over other indices or the full strip.

### Complete approximation allowance at the new time

The hash-pinned [budget adapter](../../numerics/round-1/check_t157_tail_budget.py)
re-evaluates the inherited U1–U5 bounds, without dropping the Riemann–Siegel
\(C\)-term allowance:
\[
 e_A+e_B<2.159\times10^{-12},\qquad
 e_{C,0}<2.829422\times10^{-7},\qquad
 E_{\max}<2.829444\times10^{-7}<3\times10^{-7}. \tag{4}
\]
This is uniform for every \(N\ge690988\) and \(y_0\le y\le y_1\)
at the exact new time. Its numerical gates pass after replacing historical
time/target/floor regression comparisons with the declared new contract.
The old bound \(2.334949\times10^{-7}\) is not reused. Equations (3)–(4)
give a pilot margin greater than 0.0017752269101384707 on that one
\(x\)-window at \(y_0\). A smaller retained-\(C\) residual from a
different approximation center is not inserted into this estimate.

### Infinite tail at the unchanged starting index

The old head \(M=153814\), re-evaluated at \(t_*\), produces an
OV-free contraction *upper bound* about 1.15923637. This budget does not
close; it is not a negative theorem about the true source or all heads.
The fixed larger head \(M=600000\), with \(N_*=3840000\), does close:
\[
 D'_{\rm upper}=P+TR+M_{\max}AB<0.962436,
 \qquad M_{\max}<1.631077,
\]
\[
 \mathrm{err}_{\rm tail}<1.491\times10^{-8},\qquad
 \frac{1-D'_{\rm upper}}{M_{\max}}-\mathrm{err}_{\rm tail}
 >0.02303064. \tag{5}
\]
These are outward bounds under the inherited tail reductions for all
\(N\ge N_*\), the full \(y\)-interval, and every corresponding
\(x\)-window. The [tail record](../../numerics/round-1/TAIL_T157_M600000_RECORD.json)
and [inherited-head diagnostic](../../numerics/round-1/TAIL_T157_M153814_RECORD.json)
preserve all raw legacy checks and identify which are superseded.

Two inherited facts are essential: OV is redundant padding, and the
contraction estimate can first be reduced in \(y\), then in \(N\).
The latter order requires the A-cap all-index gate only on the narrow
\(y_0\)-box; its lower bound is 1.10728. Both error caps still require
and pass their gates on the full extended hull (lower bound at least
1.97475). The legacy extended-hull A-cap check does not pass and is not
asserted. See [audit note 4, sections 3.2 and 3.5](../../../../investigations-2/newman_certificate_audit/notes/4_TAIL_LEMMA_AND_UNIFORM_ERROR_BUDGET_AUDIT_20261012.md).
This is a change in reduction order with a written justification, not
permission to discard an adverse required gate.

The extended hull is now
\([1872719/10^7,8282512/10^7]\), covering \(\sqrt{0.686}\); the old top
0.8231039 would not suffice. The support, eleven rational mollifier
coefficients, error head 3000 and finite error head 2000 remain those of
the inherited tail checker. Head 600000 was chosen after preliminary
floating exploration, not as a preregistered measured optimum. The
[tail run plan](../../numerics/round-1/PLAN.md) distinguishes that exploration
from the fixed reproducible two-head test. The larger-head run used
97.5 seconds and about 510 MiB, within its declared per-case caps.

## 5. Proof and budget ledger

| Link | Domain and allowance | Evidence and remaining obligation |
| --- | --- | --- |
| Initial verification | Unchanged \(X/2\) and \(y_0\) | Imported Platt–Trudgian input and historical package application |
| Intermediate barrier | New curved barrier inside the old closed rectangle | Inherited barrier audit; no new replay asserted |
| Sharp native binding and window freeze | All four finite legs; (1), including \(K\) | Derived in section 2; generic real paired-sum lemma |
| Full strip transfer | All finite indices, \(y_0\le y\le\sqrt{0.686}\) | [Note 02](02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md) certifies gate (2) uniformly on all four legs |
| One row at \(y_0\) | \(N=690988\); lower bound (3) | Outward arithmetic only for that row; other rows and seams **open** |
| Approximation error | All \(N\ge690988\), full strip at \(t_*\); (4) | Recomputed inherited U1–U5 machinery, hash-pinned |
| Infinite exterior | All \(N\ge3840000\), full strip; margin (5) | Recomputed inherited caps, larger head, OV-free reverse-order proof |
| Final conclusion | \(\Lambda\le0.1745354\) | **Not established** until all finite floors/coverage are supplied |

The historical producer's unreplayed rows at time 0.16125 remain an
inherited audit issue. None is new sharp-row evidence at time 0.157.
Uniform transfer is now certified in Note 02. A full producer run remains gated on the floor/coverage design and round-level review.

## 6. Collision controls and scope

The generic sharp algebra applies to any real paired coefficients; it
has no premise that excludes the controls. Its positivity condition
\(V_N<1\) and the correct approximation allowance carry the application.
On a region containing a control's collision, a valid approximation and
positive complete margin cannot both hold. A collision-free control box
may legitimately pass, as required by summary 12.

| Control | Premise missing from this specific theta application |
| --- | --- |
| Euler-factor controls \(\Phi_{c,p}\) | The unchanged zeta coefficients/conductor and resulting theta approximation; their own coefficients and errors must replace these inputs |
| Weighted-square controls | The complete unweighted theta expansion and its full reflection/arithmetic input |
| Reflected and positive-primitive controls | The complete integer-square theta coefficients, even when reflection or primitive endpoints agree |
| Earlier positive counter-kernels \(q\), \(q_{T,a}\), smooth-density and two-channel controls | The finite paired theta approximation with the explicit error bounds used here |

Thus the screen rejects transfer of the theta-specific error budget to
these sources; it does not purport to exclude them by positivity or
shape. The exact example in section 3 separately tests the *generic
inheritance implication* and disproves it in its stated finite-sum class.

## 7. Source pins and next decision

The inherited public package remains pinned to
[`a74738deb6d5e0f76887cb36901da08b68dca705`](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/tree/a74738deb6d5e0f76887cb36901da08b68dca705).
A local primary-source copy's revision and native-binding hash were
checked: `NATIVE_BINDING.md` SHA-256
`c9eb17be5011e65ff7dcc7bbedc7e68a819479ec9b3fb3c6dd63b2fcb57cdaa4`.
The Polymath TeX source has the inherited SHA-256
`0115d452da906c5bbaacb1ee0ce851e568d8d5f62f27c71a4bf8d281b5788647`;
Theorem 1.2 and the location of Lemma 8.5 were also checked in the arXiv
HTML. Exact inherited helper hashes and adapter substitutions are stored
in the numerical records. No third-party PDF is saved here, and no new
literature-best or novelty comparison is asserted.

The [bounded implementation of (2)](02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md)
is now complete, including actual integer feasibility and branch changes
on all four legs. Next design the finite floors, leg transitions and any
amortized producer. Cross-model review belongs to the coherent round output
before expansion, under the portfolio's updated cadence. No manuscript or
manuscript snapshot is created at this stage.
