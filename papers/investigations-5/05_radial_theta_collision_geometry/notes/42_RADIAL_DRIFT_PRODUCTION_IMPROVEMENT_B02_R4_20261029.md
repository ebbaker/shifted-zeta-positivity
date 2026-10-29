# CTF-B02 R4: one radial drift-production improvement

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Investigation05 **chat0021**, **Continue CTF-B02
R4 estimate**. Parent/drafting session **gpt-6.1-sol, actual recorded effort
ultra**; author-requested conceptual contribution **gpt-6-astra / max**
through a delegated agent, verified from its recorded turn metadata.

## Proposal recorded before testing

**Type B; one supporting estimate in the unchanged Note40 functional.**
Keep the physical rectangle P=[0,1/2] x [1,6], complete theta source,
unit heat preparation, whole-space radial solution, actual fixed-mark J2,
weighted residual R and F=G+||omega R||_2^2+||J2||_2^2. Keep the exact
cutoff, every commutator term, nonzero preparation residual, sphere
cancellation and inner-ball energy.

Retain the exact radial coefficient a(r)=2 lambda_rad(r)+d(r) in K.
Complete the weighted radial square with h(r)=10-a(r) and
f'+3f/(2r), aiming at K<=10G+c_rad E0 for a proved explicit c_rad<30.
No second candidate, source relation, observable or PDE is introduced.

Quantitative comparison: improve the conditional gradient allowance
(G(0)+3E0) exp(10B)-3E0 for B>0, replace Note40's 30+B0 alpha E0
coefficient, and give an improved local interval using N>=G^2/E0.
Compare also with direct analysis retaining diffusion under the old K
bound, using exactly the same information. This generic geometric gain
uses radiality and smooth prepared decay, not a favorable theta
arithmetic sign. The complete source remains in the actual fields,
operator and coefficient budgets.

The exact Gaussian-polynomial control remains admitted; its initial
residual under the theta operator includes both preparation commutator
and raw source mismatch. No collision exclusion or paid deadline is a
comparison target of this bounded lemma.

The sole [Progress05][progress] records this proposal before testing.
Stop with one proved bounded gain, fixed versioned E07 route, or precise
scoped unresolved inequality. No numerical stage is included.

## Analytical return

**Return — proved in-note, with internal LLM checks.** The one frozen
supporting estimate holds with
\[
\boxed{\mathcal K\le10G+\frac{21}{4}E_0,}
\tag{1}
\]
improving the old allowance \(10G+30E_0\). The proof gives an exact
nonnegative remainder, sharper conditional gradient control, the stated
replacement in the weighted estimate, and a strictly longer local
interval even against the old estimate retaining diffusion. It is a
**generic radial geometric gain**, not a theta arithmetic separator.
Parent B02 remains partial; the collision deadline remains unpaid.

| Next task | Type and recommended model | Readiness and bounded output |
| --- | --- | --- |
| **CTF-E08: R4 assessment — default** | **E — Sol:** check one complete proof and integrate supported conclusions | Ready; assess this note against Notes28/40 and the controls, then integrate proportionately in the existing manuscript and compile |
| CTF-E07 | E — Sol | No new execution packet is needed: the bounded analytical proof is complete |
| CTF-E03 / CTF-B03 | E — Sol / B — Astra | Remain gated; no numerical acquisition or coverage extension follows |

The [result index][results] and [avoid index][avoid] were consulted.
Under [avoid/01][a01], this is a changed quantitative allowance rather
than a restatement of noncollision. The [control register][controls]
and [avoid/02][a02] require admission of the exact colliding control.
The scope is the inherited radial prepared solution class, following
[avoid/07][a07]. The gain comes from combining the spatially varying
terms before estimating them, as required by [avoid/12][a12]; it changes
explicit bounds under [avoid/20][a20]. No literature or numerical input
is imported for the new square calculation.

### 1. Domain, source, and the signed starting point

Keep precisely \(\mathcal P=[0,1/2]\times[1,6]\), the full theta source,
unit Gaussian preparation, and the smooth whole-space extension
\(\eta(r)=h(4r-2)\) from [Note31][n31]. Rotational invariance and
uniqueness preserve radiality of the prepared pair \(W=(U,V)\).
All spatial integrals include the inner ball. The actual fixed-mark
running derivative \(J_2\), residual \(R=\mathcal A_TW-\Theta\),
\(\Theta=(aV,V+aJ_2)\), weight \(\omega=(1+r^2)^{-2}\), and functional
\(\mathcal F=G+Y+Q\) are those of [Note40][n40]. In particular,
\(Z=\omega R\), \(Y=\|Z\|_2^2\), \(Q=\|J_2\|_2^2\), and
\(N=\|\Delta W\|_2^2\). The jet equation is \(J_{2,s}=L_sJ_2\),
without a mark derivative of alpha.

Start with the full signed identity, not a zero-residual substitution:
\[
\begin{split}
\mathcal F'={}&-2N-2\|\nabla Z\|_2^2-2\|\nabla J_2\|_2^2
+2\int|\nabla\log\omega|^2|Z|^2
+2\langle Z,\omega\mathscr C_0W\rangle\\
&+\alpha\left\{\mathcal K+\int h_\omega|Z|^2
+\int d|J_2|^2+2\langle Z,\omega\mathscr C_1W\rangle\right\}.
\end{split}
\tag{2}
\]
Here \(\mathscr C_0,\mathscr C_1\) are exactly Note40 (8), including
\(-\Delta c_T\), \(b\cdot\nabla d-v\cdot\nabla c_T\), and every
cutoff derivative. The actual preparation residual is still
\([\mathcal A_T,K_1*]W^{\rm raw}\). The exact identity
\((\Theta+R)(1)=0\) is retained; no separate singular quotient by
\(r\log r\) is estimated. This proof does not reconstruct the gradient
from that quotient.

The complete-source properties used are radiality and the smooth
weighted decay supplied by its full tail and unit preparation; the
complete reflected source still defines the unchanged operator and
finite budgets. The numerical coefficient gain below uses radiality,
the fixed drift, and decay, **not** the unit square coefficients or a
new favorable theta sign. The exact control has the same geometric
properties. No source-specific separator is implied by the word theta.

### 2. Exact radial square and coefficient improvement

Set \(q=r^2\). The radial eigenvalue of \(Dv\) and the divergence are
\[
\lambda_{\rm rad}=1+\frac{1-q}{(1+q)^2},\qquad
 d=3+\frac{3+q}{(1+q)^2}.
\]
Since each gradient is radial, the gradient part of \(\mathcal K\)
has coefficient
\[
 a_v(q)=2\lambda_{\rm rad}+d
 =5+\frac{5-q}{(1+q)^2},\qquad
 h_v(q)=10-a_v(q)=\frac{q(11+5q)}{(1+q)^2}\ge0.
\tag{3}
\]
Also
\[
 V_v(q)=-\Delta d=\frac{30-20q-2q^2}{(1+q)^4}.
\]
For either smooth radial component \(f\), completing one square gives
\[
\int_0^\infty r^2h_v|f'|^2\,dr
=\int_0^\infty r^2h_v\left|f'+\frac{3f}{2r}\right|^2\,dr
+\int_0^\infty r^2\left(\frac{3h_v'}{2r}
 -\frac{3h_v}{4r^2}\right)|f|^2\,dr.
\tag{4}
\]
The prime on \(h_v\) denotes its radial derivative. The integrated
boundary term is \(rh_v|f|^2\); it vanishes at zero since
\(h_v=11r^2+O(r^4)\), and at infinity by the inherited decay.
There is no boundary at \(r=1\). The apparent \(1/r\) in the square
is harmless: its radial integrand is \(O(r^2)\) near zero.

The resulting effective potential is exactly
\[
 C_v(q)=V_v-\frac{3h_v'}{2r}+\frac{3h_v}{4r^2}
 =\frac{21-119q+67q^2+15q^3}{4(1+q)^4},
\]
\[
 p_v(q):=\frac{21}{4}-C_v(q)
 =\frac{q(203+59q+69q^2+21q^3)}{4(1+q)^4}\ge0.
\tag{5}
\]
Define the manifestly origin-admissible remainder
\[
\mathscr H_{\rm rad}(W)=
\int\frac{11+5q}{(1+q)^2}
 \left|X\cdot\nabla W+\frac32W\right|^2
+\int p_v(q)|W|^2\ge0.
\tag{6}
\]
Multiplying (4) by \(4\pi\), summing over the two components, and
using (3)–(5) proves the exact whole-space identity
\[
\boxed{\mathcal K=10G+\frac{21}{4}E_0-\mathscr H_{\rm rad}(W).}
\tag{7}
\]
Equation (1) follows immediately. Both terms in (6) are smooth at the
origin and retain the whole inner-ball contribution. This is one
supporting lemma inside the frozen functional, not a newly evolved
field or alternate source relation.

### 3. Gradient and joint weighted consequences

From \(G'=-2N+\alpha\mathcal K\), (7) yields
\[
 G'+2N+\alpha\mathscr H_{\rm rad}
 =\alpha\left(10G+\frac{21}{4}E_0\right).
\tag{8}
\]
With \(B(s)=\int_0^s\alpha\), discarding the nonnegative terms and
integrating proves
\[
\boxed{G(s)\le
 \left(G(0)+\frac{21}{40}E_0\right)e^{10B(s)}
 -\frac{21}{40}E_0.}
\tag{9}
\]
For the same actual B, this upper allowance is smaller than Note28's
by exactly \((99/40)E_0(e^{10B}-1)\), strictly positive when B>0.
The compression exponent remains 10; no independent deadline bound
for B has appeared.

Use precisely Note40's coefficient budgets and Young payments in (2).
For \(\mathscr D=N+2\|\nabla Z\|_2^2+2\|\nabla J_2\|_2^2\), only
the gradient production changes:
\[
\begin{split}
\mathcal F'+\mathscr D+\alpha\mathscr H_{\rm rad}\le{}&
 [A_1+\alpha(10+B_1)]G\\
&+[8+A_2^2+A_1+A_0+\alpha(265/24+B_1+B_0)]Y\\
&+6\alpha Q+[A_0+\alpha(21/4+B_0)]E_0.
\end{split}
\tag{10}
\]
Thus \(30+B_0\) is replaced by \(21/4+B_0\), with no other
coefficient, forcing term, or dissipation payment altered. Set
\[
\kappa_{1,\rm rad}=\frac{265}{24}+B_1+B_0\le\kappa_1,
\qquad M_{\rm rad}=\kappa_0s+\kappa_{1,\rm rad}B(s).
\]
This simplification follows because that entry dominates
\(10+B_1,6,21/4+B_0\). The compact constant decreases strictly only
if \(B_1<455/24\); this note does not acquire that additional bound.
The expanded coefficient improvement in (10) is unconditional.
The integrated result is
\[
 e^{-M_{\rm rad}(s)}(\mathcal F(s)+E_0)
 +\int_0^s e^{-M_{\rm rad}(q)}
  (\mathscr D+\alpha\mathscr H_{\rm rad})(q)\,dq
 \le\mathcal F(0)+E_0.
\tag{11}
\]
The same fixed-ball residual bound from Note40 remains valid.

### 4. Local comparison retaining diffusion

For Schwartz fields, \(G=-\langle W,\Delta W\rangle\), so
\(N\ge G^2/E_0\). Put \(g=G/E_0\); nonzero L2 data imply
\(g_0>0\). Since \(\alpha\le2g/3\), (8) gives
\[
 g'\le\frac{14}{3}g^2+\frac72g.
\tag{12}
\]
Let
\[
 \delta(s)=1-\frac{4g_0}{3}(e^{7s/2}-1),\qquad
 L_{\rm rad}=\frac27\log\left(1+\frac{3}{4g_0}\right).
\]
Scalar comparison, initially before both the lifespan and L_rad, gives
\[
 g(s)\le\frac{g_0e^{7s/2}}{\delta(s)},\qquad
 \alpha(s)\le\frac{2g_0e^{7s/2}}{3\delta(s)},\qquad
 B(s)\le-\frac17\log\delta(s).
\tag{13}
\]
The last inequality integrates the alpha bound, since
\(\delta'=-(14/3)g_0e^{7s/2}\). If the maximal lifespan ended
strictly before L_rad, (13) would keep G bounded at that endpoint,
contradicting Note28's continuation criterion. Therefore
\[
\boxed{S_{\max}\ge L_{\rm rad}.}
\tag{14}
\]
All displayed finite bounds hold on the **open** interval s<L_rad;
equality of the maximal lifespan with the endpoint is allowed.
Continuity and compactness from Note40 give the uniform version with
\(\Gamma_0=\max_{p\in\mathcal P}G(0;p)/E_0(p)<\infty\):
\(S_{\max}(p)\ge(2/7)\log(1+3/(4\Gamma_0))>0\).
No numerical value of Gamma_0 is acquired.

Equations (11) and (13) also give an explicit local weighted allowance
\[
 \mathcal F(s)+E_0\le(\mathcal F(0)+E_0)e^{\kappa_0s}
                 \delta(s)^{-\kappa_{1,\rm rad}/7}.
\tag{15}
\]
It becomes singular at L_rad and supplies no extension through a
collision deadline by itself.

For the **matched direct comparison**, retain the same diffusion in
the old estimate \(\mathcal K\le10G+30E_0\). It gives
\(g'\le(14/3)g^2+20g\) and
\[
 L_{\rm old,diff}=\frac1{20}\log\left(1+\frac{30}{7g_0}\right).
\]
For every g_0>0,
\[
 L_{\rm rad}>L_{\rm old,diff}>
 \frac1{20}\log\left(1+\frac3{g_0}\right)=L_{28}.
\tag{16}
\]
For the first strict inequality use
\(L(A,b)=\int_{g_0}^\infty du/(Au^2+bu)\), A=14/3:
decreasing b from 20 to 7/2 strictly increases the integral.
The second follows from 30/7>3. Thus the improvement does not merely
recover diffusion that the published Note28 comparison dropped.
The proof uses only the same E0, G0 and drift information; direct
analysis can use this lemma equally. No acquisition-cost or new
physical first-jet-information advantage is claimed.

### 5. Controls, evidence, and completion boundary

The exact source
\(\Phi_*(u)=(64u^4+6)e^{-17u^2/4}\) has its collision at
\((T,a)=(1/4,2\sqrt6)\in\mathcal P\). Its smooth prepared radial
fields satisfy (7)–(16). With the same theta operator its residual is
\[
 R_{*,0}=[\mathcal A_T,K_1*]W_*^{\rm raw}
       +K_1*(M_T^*W_*^{\rm raw}),\quad
 M_T^*=r\log r\{(\log\rho_{*,T})'-\ell_T'\}.
\tag{17}
\]
The raw mismatch in the second summand is retained. Note28's theorem
still gives its finite upper deadline
\[
 S_{\max,*}\le
 \frac{60}{7(5\pi^2)^{2/5}}
 \frac{P_{*,0}^{4/5}}{E_{*,0}^{2/5}}<\infty.
\]
The lower interval (14) and this upper deadline coexist. No extra
premise excluding this control is used, and no bound through that
deadline is asserted.

The other [registered controls][controls] retain Note40's distinct
premises and witness domains: weighted-square and finite-prime changes
do not give the full reflected unit coefficients; the reflected
super-Gaussian lacks square arithmetic; smooth-shape and
positive-primitive data do not identify the complete source;
Euler-factor controls change the arithmetic/conductor. Their geometric
radiality is no failed premise of this lemma. The weighted-square
witnesses near 44.13 and 83.53 remain outside this rectangle, and the
reflected witness at pi/4 remains below it. High-gap and conditional
witnesses keep their original location and hypothesis qualifications.
Atomic sources remain outside the imported smooth source-function
statement. No new witness is placed in this rectangle.

**R4 is complete as one proved bounded improvement.** The full theta
source and all residual/jet/domain obligations are unchanged. No
simulation, scan, optimization, quadrature, interval certificate,
second candidate, or manuscript edit was made. The gain is generic:
source-specific signed information and independent compression control
through a paid collision deadline remain unresolved. E03/B03 remain
gated. The current manuscript still presents the assessed Note40
version until E08 assesses and integrates this return.

The conceptual selection and proof were contributed by **gpt-6-astra /
max**, verified from its recorded turn metadata: thread
`01a187ed-fa07-7203-82ee-32d4d8e51ed5`, turn
`01a187ed-fa17-7611-a8b2-c3f733e9f861`. Parent **gpt-6.1-sol / ultra**
checked the same algebra and scalar consequences and prepared this
note; a separate read-only **gpt-6.1-sol / ultra** agent independently
rederived (3)–(16), and another checked source/domain/control accounting.
These are internal LLM checks with shared imported premises, including
a different-model check of the Astra contribution; they are not
independent specialist review. Only the parent public chat has the
unique Investigation05 chat0021 registration. Subagent traffic is not
part of that public archive.

**Next: [E] CTF-E08 — Sol, R4 assessment and integration.** Check this
one proof, origin/boundary algebra, exact control admission, coefficient
and matched lifespan comparisons; integrate only supported conclusions
in the existing manuscript and compile it. Preserve the issued R1
packet, Notes39–41, and Review22 as their dated versions. A failed
premise or a new source-specific estimate returns to B02; no E03 or
second candidate starts automatically.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n31]: 31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md

[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md


### Input identity and public history

The following inputs were preserved byte-for-byte through this return;
hashes identify the inputs and do not validate a proof.

| Input | SHA-256 |
| --- | --- |
| `notes/39_WEIGHTED_RESIDUAL_COUPLED_ESTIMATE_B02_R3_20261029.md` | `36cb00f7d07a8740c1e429b3eaa3870ef87ce95e38279610e179d6ce5dea0594` |
| `notes/40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md` | `abbb999e364006ea3558869a29d39a648922c85f0df71e09fa23dd1c0b90440e` |
| `notes/41_WEIGHTED_CLOSURE_CONTINUATION_20261029.md` | `6fdc34a7e47aa4baf17336457d9514d37d908a1018122e852613776b97aa5654` |
| `reviews/22_WEIGHTED_RESIDUAL_CLOSURE_E08_ASSESSMENT_20261029.md` | `ba81165bbe88c0f394d293ae91db3f244bd4e995c8716630124630ddfe9ea377` |
| `research-progress/handoffs/CTF-E07_WEIGHTED_RESIDUAL_CLOSURE_REQUEST_R1_20261029.md` | `618911e546f098e976202a00b6b8b4233937867fc0574cf44bbf7dcd96ba099b` |
| `radial_deformations_and_zero_dynamics.tex` | `392196ad7422539d44e72622be3535d34c5d5fc81d8e7c950c0d139a5789a544` |
| `book/main.tex` | `b954e99f992ff44fafc2745661257e2d5ce730360c3f9292862b195469f95abb` |

Parent thread `01a187ec-edf4-7df2-9876-4e6fc8e540af`; turn
`01a187ed-3547-7f41-9e7e-c57681026176`. The [unique public archive][history]
retains chat0021; current capture counts and hashes belong to its registry.

[history]: ../chat-histories/0021_2026-10-29T13-50-14Z_continue-ctf-b02-r4-estimate.json
