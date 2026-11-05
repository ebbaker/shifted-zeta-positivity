# MC11-B01 r1: two signed-transfer routes and a scoped stop

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6-astra (Codex), actual recorded effort max**. Existing thread `01a1aa32-c540-7671-aa14-f080cfbedd5d`, MC11 history0004. **B — brainstorm**, r1; one writer, no subagent or independent assessment.

**Disposition: complete with a scoped stop; no E05 proof contract is issued.** Exactly two mechanisms were compared: high-energy corner-cofactor domination, and first-mode comparison using a collected absolute determinant payment. The first has an unproved signed cofactor margin. The second admits a useful all-index scalar bound, but its uniform relative-error certificate eventually becomes vacuous and its sharper correlated version still lacks reference signs and conditioning. These findings do not show that a canonical determinant is negative or exclude every signed-comparison method.

**Quantitative partial result, proved below:** for the unchanged complete excited spectrum, the moment ratios ρ_j=h_j/b_j strictly decrease with j. The accepted finite-index anchor therefore yields
\[
0<\rho_j\le\frac1{39999}\quad(j\ge1),\qquad
0<\rho_0<\frac1{200}.
\tag{1}
\]
This is an unsigned coefficient bound on every index, not a determinant margin. Its proof uses the canonical source formula and the inherited validated j=1 allowance. New arguments here have **proof-author checking only**; [AR-E04 is the next assessment](../research-progress/handoffs/09_MC11_B01_SCOPED_STOP_AND_AR_E04_MODEL_CONTINUATION_20261105.md). The [sole register](../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) owns status, and [activation versions](../research-progress/handoffs/09_MC11_B01_R1_INPUT_VERSIONS_20261105.json) preserve the input snapshot.

| Continuation | Type | Recommended model | Readiness | Output |
| --- | --- | --- | --- | --- |
| **MC11-AR-E04 r1 — default next** | E | **Sol**, fixed claim-by-claim analytic assessment | Ready, unstarted; frozen packet linked above | Assess Notes07–09 and the exact scope of this stop |
| MC11-E05 | E | Sol if a future contract exists | Reserved, not executable | No signed lemma with a paid margin survived B01 r1 |
| MC11-B01 revision, only with new input | B | Astra, a new quantitative choice would remain | Not activated | A source-specific signed bound or reference margin outside the stopped implementations |

## 1. Fixed target, ranges and evidence class

Keep BR01's selected free cylinder, V=0, fixed probe and external source map. Do not change its readout or introduce a potential-deformed determinant. In the original source-energy notation put
\[
\phi_E(u)=e^u(2X^2-3X)e^{-X},\quad X=Ee^{4u},\quad E_n=\pi n^2,
\]
\[
a_j(E)=\int_0^\infty\frac{u^{2j}}{(2j)!}\phi_E(u)\,du,
\quad b_j=a_j(\pi),\quad h_j=\sum_{n\ge2}a_j(E_n),\quad
c_j(s)=b_j+s h_j,\quad0\le s\le1.
\tag{2}
\]
All j≥0 use the **raw full-half-line source moments**. In particular b_0 is not an endpoint-compensated Green coefficient or the earlier compact c_0^*. AR-E03 proves finiteness, positivity, complete-sum integration and the pairing identity for
\[
M_{q,k}(s)=[c_{k+j-i}(s)]_{0\le i,j<q},\qquad
D_{q,k}(s)=\det M_{q,k}(s),\quad q\ge1,\quad k\ge q-1.
\tag{3}
\]
The intended growing-order application includes k=q−1,q,q+1 at every q. The ranges below cover all n≥2 and s∈[0,1]. No lower-shift negative-index convention is added; those pairings retain AR-E03's odd endpoint entries.

The [accepted E01 note](01_MC11_E01_R1_PROOF_AND_RATIONAL_REPLAY_20261104.md) supplies the single-level slope and finite anchor. [E04 Review02](../reviews/02_MC11_E04_R1_THREE_ORBITAL_RETURN_ASSESSMENT_20261104.md) preserves the opposite directions at q=2 and q=3, with their complete error payments. [AR-E02 Note07](07_MC11_AR_E02_R1_BOUNDED_POTENTIAL_DEFECT_AND_RIGIDITY_20261105.md) supplies a scalar resolvent defect in its own class; [AR-E03 Note08](08_MC11_AR_E03_R1_SOURCE_MEMBERSHIP_AND_ENDPOINT_PAIRINGS_20261105.md) supplies the representation. Neither provides signs of (3) as q grows.

Classification under [avoid/01](../../../../../../../avoid/01_restating_the_target.md): this note gives an unsigned quantitative lemma, sufficient-error formulas, and a research decision about two specified mechanisms. It does not propose a new RH criterion. The [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../avoid/README.md), [joint-payment caution](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scope caution](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) delimit the interpretation.

## 2. Route A: endpoint concentration and the corner cofactor

For q≥2, k≥q−1, set m=k−q+1≥0 and collect equal coefficient indices **before taking bounds**:
\[
A_\ell(q,k;s)=\sum_{j-i+q-1=\ell}\operatorname{cof}_{ij}M_{q,k}(s),
\qquad0\le\ell\le2q-2.
\tag{4}
\]
Deleting row q−1 and column 0 leaves the shifted lower-order block, so
\[
A_0=(-1)^{q-1}D_{q-1,k+1}(s).
\tag{5}
\]
The exact level and complete excited-spectrum responses are
\[
\chi_{q,k}(E;s)=\sum_{\ell=0}^{2q-2}A_\ell a_{m+\ell}(E),\qquad
\partial_sD_{q,k}(s)=\sum_{\ell=0}^{2q-2}A_\ell h_{m+\ell}.
\tag{6}
\]
The latter includes every excited level and every common-path mixed term. At each finite q the cofactors are polynomials in s; no inverse matrix or invertibility assumption is needed.

For E≥4π the accepted logarithmic slope is
\[
-\partial_u\log\phi_E(u)\ge\lambda(E)
=4E-9-\frac{12}{2E-3}>40.
\]
Integration against u^r/r!, r≥1, gives λJ_r≤J_(r−1), because the endpoints vanish. Therefore for every m,ℓ≥0,
\[
0<\frac{a_{m+\ell}(E)}{a_m(E)}\le\lambda(E)^{-2\ell},\qquad
0<\frac{h_{m+\ell}}{h_m}\le40^{-2\ell}.
\tag{7}
\]
The complete-sum inequality follows by summing the one-level inequalities with positive weights. Thus the full normalized remainder obeys
\[
\left|\frac{\partial_sD_{q,k}}{h_m}-A_0\right|
\le\mathcal B_{q,k}(s):=
\sum_{\ell=1}^{2q-2}|A_\ell(q,k;s)|40^{-2\ell}.
\tag{8}
\]
Replacing 40 by λ(E_n) gives the analogous all-n level bound. No spectral exterior has been dropped.

The precise proposed sign margin would be
\[
\eta_{q,k}:=\inf_{0\le s\le1}
\{D_{q-1,k+1}(s)-\mathcal B_{q,k}(s)\}>0.
\tag{9}
\]
If (9) were independently proved, (5)–(8) would give the alternating response sign, including all levels, at that (q,k). **No positive lower bound for (9) is obtained here.** E04 proves a fixed-order signed response using its own enclosed cofactors, actual n=2 moments and separate higher-energy bound. This does not assert that the particular coarse sufficient margin (9) is positive even at q=3. Neither E02's scalar defect nor E03's Hilbert bounds controls these signed minors for general q,k. A positive lower-order minor alone is insufficient: its magnitude must dominate all the other collected cofactors.

Even a response-sign theorem would not finish positivity transfer. One still needs a positive D_(q,k)(0) and, for a decreasing response, a paid loss. The available complete upper payment is
\[
|D_{q,k}(1)-D_{q,k}(0)|\le
h_m\int_0^1\bigl(|A_0(s)|+\mathcal B_{q,k}(s)\bigr)\,ds.
\tag{10}
\]
To certify positivity from it, the right side must be below an independently proved reference margin. No such growing-order margin is supplied. Displaying (9) or (10) is a record of the unpaid obligations, not an issued E05 lemma.

**Route-A disposition:** stop this proposed transfer from the slope/endpoint-concentration data and the fixed-order cofactor boxes. This is a missing-premise decision, **not a proof that (9) is false for theta**. An induction on lower-order minors is not intrinsically circular, but it must actually initialize and propagate the quantitative shifted margins; that argument is absent. The all-index Green representation has not furnished it.

## 3. Route B input: a monotone ratio carries the scalar anchor to all indices

For x=πe^{4u} and n≥2, divide a single excited source density by the retained density:
\[
r_n(x)=\frac{\phi_{\pi n^2}(u)}{\phi_\pi(u)}
=n^2\frac{2n^2x-3}{2x-3}e^{-(n^2-1)x}.
\tag{11}
\]
Direct differentiation gives
\[
\frac{d}{dx}\log r_n(x)
=-(n^2-1)\left[1+\frac6{(2n^2x-3)(2x-3)}\right]<0.
\tag{12}
\]
The total ratio r(u)=Σ_(n≥2)r_n(πe^{4u}) is bounded and strictly decreasing. To justify the complete sum, x≥π>3 implies
\[
0<r_n(x)<2n^4e^{-3(n^2-1)}<\frac{2n^4}{20^{n^2-1}}.
\tag{13}
\]
Here e³>20 follows already from the positive exponential series through degree eight. For t_n=n⁴/20^(n²−1), n≥2,
\[
\frac{t_{n+1}}{t_n}\le\frac{(3/2)^4}{20^5}<\frac1{1000},
\quad
r(u)<\frac{2(16/20^3)}{1-1/1000}=\frac4{999}<\frac1{200}.
\tag{14}
\]
These are complete analytical spectral bounds, not fitted constants. Strict decrease follows from (12) for each positive term and convergence, without exchanging an unjustified derivative of the infinite sum.

Let μ_j be the probability measure with density
\[
d\mu_j(u)=\frac{u^{2j}\phi_\pi(u)}{(2j)!b_j}\,du,
\qquad\rho_j:=\frac{h_j}{b_j}=\mathbb E_{\mu_j}r.
\tag{15}
\]
Tonelli applies to the nonnegative full source. The successive measure is obtained by tilting μ_j by u²; factorials cancel in this probability normalization. Hence
\[
\rho_{j+1}-\rho_j
=\frac{\operatorname{Cov}_{\mu_j}(u^2,r(u))}
       {\mathbb E_{\mu_j}u^2}<0.
\tag{16}
\]
For completeness twice the covariance is the integral over μ_j×μ_j of
\((u^2-v^2)(r(u)-r(v))\). It is negative off the diagonal, and μ_j has a positive density on u>0. Boundedness of r and the finite moments from E03 justify all these integrals. This proves strict decrease for every integer j≥0, with all n included.

E01 Note01 §2, accepted by [Review01](../reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md), gives at j=1
\[
h_1\le\epsilon c_1^*,\quad b_1\ge(1-\epsilon)c_1^*,\quad
c_1^*>0,\qquad\epsilon=1/40000.
\tag{17}
\]
Only this already assessed finite anchor is used; no new moment is acquired. Dividing (17) and using (16) proves (1). In particular
\[
1\le\frac{c_j(s)}{b_j}\le1+\frac{s}{39999}\quad(j\ge1),
\qquad 1\le\frac{c_0(s)}{b_0}<1+\frac{s}{200}.
\tag{18}
\]
The sharper constants at indices 2–5 are not needed, and the compact reference c_0^* has not been inserted at j=0.

This is compatible with the stronger far-index decay already proved in [RGD Note07 §3](../../10_radial_green_determinants/notes/07_RGD_B03_R2_EXACT_PAYMENT_OBSTRUCTION_AND_TRUE_TAIL_20261104.md):
\[
\rho_j\le128e^{-j/(16\log j)},\qquad j\ge e^{16}.
\tag{19}
\]
For j≥1 its full first-mode coefficients are the same b_j; its separate endpoint-compensated zero coefficient is not imported. Equation (1) is a simple bound over the previously uncovered indices, not a claim to improve (19) at infinity. None of these scalar estimates supplies a reference determinant sign or condition bound.

## 4. Route B consumer: exact collection, complete payment and its limit

Let
\[
P_{q,k}(z)=\det[z_{k+j-i}]_{0\le i,j<q}
          =\sum_\alpha\gamma_\alpha z^\alpha,
\qquad
\mathcal A_{q,k}(b)=\sum_\alpha|\gamma_\alpha|b^\alpha>0,
\tag{20}
\]
where identical monomials have first been **collected exactly** and every monomial has degree q. This uses the existing [RGD collected-polynomial method](../../10_radial_green_determinants/manuscript/sections/01_green.tex), equation `eq:green-det-norm`. It is not a new determinant perturbation theorem. The positive monomial b_k^q ensures the polynomial is nonzero. Always |D_(q,k)(0)|≤A_(q,k)(b).

From c_j(s)=b_j(1+sρ_j), the complete signed difference is
\[
D_{q,k}(s)-D_{q,k}(0)=
\sum_\alpha\gamma_\alpha b^\alpha
 \left[\prod_j(1+s\rho_j)^{\alpha_j}-1\right].
\tag{21}
\]
In particular its full absolute payment, retaining each coefficient ratio, is
\[
\mathcal R_{q,k}(s)=
\sum_\alpha|\gamma_\alpha|b^\alpha
 \left[\prod_j(1+s\rho_j)^{\alpha_j}-1\right],
\quad |D_{q,k}(s)-D_{q,k}(0)|\le\mathcal R_{q,k}(s).
\tag{22}
\]
This finite polynomial expression at each q includes all mixed powers of s; the h_j already contain every excited level. There is no omitted higher-order determinant term.

For k≥q all used indices are positive, so (18) implies
\[
\mathcal R_{q,k}(s)\le U_q(s)\mathcal A_{q,k}(b),
\qquad U_q(s)=\left(1+\frac{s}{39999}\right)^q-1.
\tag{23}
\]
For k=q−1 there is exactly one matrix entry with index zero, at the bottom left. Every collected monomial thus has degree at most one in b_0, giving instead
\[
\mathcal R_{q,q-1}(s)\le U_q^-(s)\mathcal A_{q,q-1}(b),
\quad U_q^-(s)=\left(1+\frac{s}{200}\right)
               \left(1+\frac{s}{39999}\right)^{q-1}-1.
\tag{24}
\]
The factor for a monomial omitting b_0 is no larger than (24). This covers all three neighboring shifts without treating the zero coefficient as a positive-index one.

The required **dimension-dependent reference margin** is
\[
\mu_{q,k}=\frac{D_{q,k}(0)}{\mathcal A_{q,k}(b)}.
\tag{25}
\]
When D_(q,k)(0)>0 it lies in (0,1]. The sufficient positivity certificate supplied by (23) is μ_(q,k)>U_q(1), and the lower-shift version needs μ_(q,q−1)>U_q^−(1). No positive lower bound for (25) at growing q is available from the present evidence.

There is also a rigorous limit on this **uniform-envelope certificate**. For N=39999, the binomial theorem gives (1+1/N)^N>2. Therefore U_q(1)>1 for q≥39999, so μ>U is impossible regardless of the conditioning of a positive reference. Equation (24) likewise exceeds one for q≥40000. These are explicit sufficient failure thresholds of the displayed allowance, **not measured first failures, counterexamples, or negative canonical determinants**. Algebraic collection has already occurred, so this is not merely an artifact of paying each permutation separately.

Even an optimal fixed uniform envelope cannot prove every diagonal order by this rule: by (16) the smallest such envelope for k=q is the positive constant ρ_1. For k=q+1 it is ρ_2, and for k=q−1 it is ρ_0. For any fixed ε>0, (1+ε)^q−1 eventually exceeds one. The numerical ceiling changes if the constant improves; the limitation of a fixed uniform envelope remains.

**What is not stopped:** (22), with its actual nonuniform ratios and correlations, is not proved too large for the canonical matrices. The large-index decay (19) may help it. No lower bound for the actual signed difference is inferred from the large upper allowance. But to issue E05 for (22) one must still supply a proof route for positive reference signs and a quantitative comparison of R to that margin. E02/E03 and (1) do not do so. Describing that unpaid comparison as the next lemma would leave the mechanism unspecified.

The RGD finite-mode PF-infinity obstruction concerns its **endpoint-compensated** sequence and all contiguous minors; it is not used to declare any raw b_j block in (3) negative. Its [algebraic small-defect controls](../../10_radial_green_determinants/manuscript/sections/03_pairs.tex), accepted with their scope in [RGD Review12](../../10_radial_green_determinants/reviews/12_RGD_E04_R7_PAIR_REFERENCE_ASSESSMENT_20261104.md), have no established realization by this positive smooth theta source. They reinforce the need for dimension-sensitive information but are not counterexamples to the present canonical family.

**Route-B disposition:** stop the unchanged-ground, fixed-uniform-relative-envelope, collected-absolute-payment implementation as an all-order proof mechanism. Retain (1), (16) and the complete formulas (21)–(24). The sharper nonuniform implementation remains **unresolved for lack of reference signs/conditioning**, not disproved.

Related literature distinguishes absolute and relative determinant sensitivity: [Ipsen–Rehman (2008), publisher abstract](https://epubs.siam.org/doi/10.1137/070704770). Only the abstract and metadata were inspected; no theorem from that article is imported. Its author-hosted reading copy and hash are recorded in the [reference receipt](../references/MC11_B01_REFERENCE_RECEIPT_20261105.json). The proof of (21)–(24) is the displayed algebra and the existing repository method.

## 5. Collision-control screen

Apply the [control cluster](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [avoid/02](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md) to the actual premises, rather than to geometry alone.

| Control | Premises that survive | Literal canonical premise absent; what is not asserted |
| --- | --- | --- |
| Positive weighted-square controls | Single-level slope, decreasing ratios for positive excited weights, and generic cofactor/polynomial identities | Complete unit weights and canonical anchor (17) cannot be imported unchanged. Some reweightings could satisfy the same small bound; no uncomputed failure of (9) or (25) is claimed |
| Euler-factor modifications | Positive-source/Hilbert identities and determinant perturbation algebra | Unchanged unit-square source and its validated anchor. Their positive-time collision does not refute MC11's time-zero fixed-order result |
| Reflected super-Gaussian control | Reflection, positive Hilbert/Fock metrics and determinant algebra | Literal complete square expansion used in (11)–(17); reflection alone gives no cofactor margin |
| Smooth shape/positive-primitive controls | Their positive auxiliary channel and relevant shape/endpoint properties | Exact arithmetic source and canonical coefficient payment; no determinant-margin failure is newly computed |

The canonical quantitative input here is (17) for the fixed complete unit-weight spectrum. The extension (16) is generic for positive reweightings having the stated density-ratio structure. Neither becomes a theta-specific signed inequality simply because it was evaluated on theta. In particular no collision control is claimed to violate the generic equations (6), (16) or (21). Route A lacks its discriminating quantitative sign premise; route B lacks its canonical reference margin. Those are precisely the reasons a signed E05 contract is not issued.

## 6. Completion, evidence and reopening condition

This B task has compared its two routes and reached a **scoped research stop**. The new monotone-ratio proof and extension of the accepted scalar anchor are proved in-note with same-assistant checks only. The uniform-payment ceiling is an analytical statement about that certificate. Route A and the nonuniform version of Route B have missing estimates, not known false canonical inequalities. No independent review, numerical acquisition, larger determinant case, moment table, new potential or source change occurred.

Before writing, the neighboring RGD source/payment results were consulted. This avoids rerunning its already stopped compact-reference campaign or presenting its collected-polynomial formula as new. The proof-author checks cover the sign in (12), factorial cancellation and strict covariance in (16), the compact-to-full denominator in (17), the unique zero-index entry in (24), and the distinction between an allowance ceiling and a lower bound on an actual error. AR-E04 should check these exact points against the frozen inputs.

**No all-order determinant gain is obtained. E05 remains reserved and unactivated.** Reopen B01 with a dated revision only when there is a specified route to a quantitative signed cofactor bound, or to source-sensitive reference signs/conditioning and complete correlated error payment. An additional finite-order value, a smaller fixed scalar allowance or another positive representation alone does not meet that condition. This does not forbid a new method or close MC11 as a whole.

**Next: [E] MC11-AR-E04 r1 — Sol.** Assess the finished model/source proofs and this decision's auxiliary bounds and scoped conclusions. The [continuation and model-change packet](../research-progress/handoffs/09_MC11_B01_SCOPED_STOP_AND_AR_E04_MODEL_CONTINUATION_20261105.md) freezes that assessment, with E05 explicitly absent.
