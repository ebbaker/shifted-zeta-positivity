# J-B06: complete neighboring-index balance and a Gaussian comparison

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor `/root/branch02`, actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. The child rollout records that configuration for turn `01a1999e-eb9b-7d11-904f-cc6de08027c1`; worker identity `01a1999e-eb7f-7741-86d1-a6f113b43845`. It inherits the coordinator's model, instructions and research inputs. This is contributing same-model analytical work, pending the coordinator's comparison, not independent specialist review. The coordinator alone records the parent research chat.

**Disposition: J-B06's bounded evaluation is complete; a named conceptual estimate remains.** The complete factorial budget telescopes explicitly, and one Gaussian comparison would give a quantitative order-raising inequality. An exact two-point relaxation proves that positive association, positive moment normalization and increasing signed averages alone cannot yield even the weaker required neighboring-index comparison. No validity of the Gaussian comparison for canonical theta is established. The accepted order-three baseline, its internal-review status and the negative origin curvature remain unchanged.

| Next action | Type and recommendation | Readiness | Concrete output and stopping rule |
| --- | --- | --- | --- |
| Test one complete-source signed Mellin-curvature comparison, (12) below, at r=3 | **B — Astra**; the needed source-sensitive estimate is not supplied by association | Conceptual follow-up only; no E execution issued | Derive one theta-specific joint bound on (11), covering s>=0, or a precise failed comparison. Treat s in [0,2] and the unbounded tail as separate obligations of the same bound. Stop if the proof needs an unproved D4 sign or a positive density obtained by deleting h's negative part. No derivative escalation, quadrature campaign or coefficient scan. |

Read with [Note15][packet], the [branch brief][brief], [Note14][note14], [Note05][note05] and [accepted Review01][review01]. The [result index][results], especially [theta identities][theta] and [controls][controls], and the [avoid index][avoid], especially [target reformulation][target], [shape premises][shape], [shared review premises][shared], [scope][scope], [premature numerics][numerics] and [joint signed estimates][joint], govern the interpretation below.

## 1. Fixed objects and the status of the proposed estimate

Use the unchanged complete canonical source at physical heat time zero:
\[
 c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,
 \qquad D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},\qquad c_n=0\ (n<0).
\]
These are ordinary coefficients, not the raw moments or the exponential coefficients gamma_n=n!c_n. Use Note14's positive density w_{r,k}, normalization Z_{r,k}, signed observable h_r and
\[
 M_{r,k}=F_{r,k}D_{r,k}=Z_{r,k}A_{r,k},\quad
 F_{r,k}=\prod_{j=0}^{r-1}(2k+2j)!,\quad A_{r,k}=\mathbb E_{r,k}h_r. \tag{1}
\]
At r=3 the accepted R'>0 and K>0 imply coordinatewise increase of h=h_3 and A_{3,k}>=A_{3,0}>0. The same accepted R'>0 gives h_2=1 and D_{2,k}=Z_{2,k}/F_{2,k}>0. Thus the lower-order denominator used below is independently positive; it is not an assumed D4 sign.

The exact inequality equivalent to a next determinant sign is displayed once in (5). It is a reformulation, not a new estimate. The selected **Gaussian envelope** (7) is a stronger sufficient bound, with an explicit quantitative consequence. Its truth for theta is unresolved. The new established negative finding concerns an information relaxation in Section 4, not theta itself.

## 2. Keep A, Z and the factorials together

For k>=1 put q(u)=prod_{j=1}^r u_j^2 and use expectation under mu_{r,k}=w_{r,k}/Z_{r,k}. All q and q^{-1} expectations below are finite: multiplication by q^{±1} produces w_{r,k±1}. Write h=h_r and A=A_{r,k}. Directly,
\[
 \frac{A_{r,k}^2}{A_{r,k-1}A_{r,k+1}}
 \frac{Z_{r,k}^2}{Z_{r,k-1}Z_{r,k+1}}
 =\frac{A^2}{\mathbb E_k(hq)\mathbb E_k(h/q)}.               \tag{2}
\]
This equality cancels normalization factors only after retaining both of them. Define
\[
 Q_{r,k}=\frac{\mathbb E_k(hq)\mathbb E_k(h/q)}{A^2}
 =\frac{M_{r,k-1}M_{r,k+1}}{M_{r,k}^2}.
\]
It is not the product of two expectations under a positive h-weighted probability measure: h can be negative. For r=3 all three M's are positive by the accepted index comparison.

The factorial factor is exactly
\[
\begin{aligned}
 B_{r,k}&=\frac{F_{r,k-1}F_{r,k+1}}{F_{r,k}^2}\\
 &=\prod_{j=0}^{r-1}\frac{(2k+2j+2)(2k+2j+1)}{(2k+2j)(2k+2j-1)}\\
 &=\frac{(2k+2r)(2k+2r-1)}{2k(2k-1)}.
\end{aligned}                                                    \tag{3}
\]
The even and odd factors telescope separately. Hence
\[
 \frac{D_{r,k}^2}{D_{r,k-1}D_{r,k+1}}=\frac{B_{r,k}}{Q_{r,k}}. \tag{4}
\]
Together with Desnanot–Jacobi and positive D_{r-1,k}, this gives precisely
\[
 D_{r+1,k}>0\quad\Longleftrightarrow\quad Q_{r,k}<B_{r,k},      \tag{5}
\]
when the neighboring rth determinants are positive. For r=3,k=1 the budget is B=28; for fixed r and large k, B=1+2r/k+O_r(k^{-2}). A uniform constant bound on Q greater than 1 would not suffice in that limit.

There is also a useful exact signed two-copy formula:
\[
 Q_{r,k}-1=\frac1{2A^2}\mathbb E_{\mu_k\otimes\mu_k}
 \left[h(u)h(v)\frac{(q(u)-q(v))^2}{q(u)q(v)}\right].         \tag{6}
\]
It follows by exchanging u and v in the product of the two expectations. Opposite signs of h produce negative contributions. Replacing h(u)h(v) by its absolute value discards that cancellation; no such replacement is used here.

## 3. One selected comparison and its usable conditional consequence

The proposed comparison is
\[
 \boxed{Q_{r,k}\le G_{r,k}:=\frac{2k+2r-1}{2k-1}\qquad(k>=1).} \tag{7}
\]
This leaves the strict factorial factor B/G=(k+r)/k. If (7) holds and the needed lower-order determinants are positive, then
\[
 \frac{D_{r,k}^2}{D_{r,k-1}D_{r,k+1}}\ge\frac{k+r}{k},
 \qquad
 D_{r+1,k}\ge\frac{r}{k+r}\frac{D_{r,k}^2}{D_{r-1,k}}>0.      \tag{8}
\]
At the pilot r=3 this would prove the fully quantified order-four inequality with factor 3/(k+3), including k=1. It is stronger than merely D4,k>0 and is not claimed as a new known coefficient range.

**Why this comparison is normalized to a Gaussian.** For Phi(u)=e^{-a u^2}, a>0, elementary moment integration gives c_n=c_0 t^n/n!, t=1/(4a). Factoring (k+j)! from column j of the reciprocal-factorial matrix leaves the falling-factorial polynomials (k+j)^{underlined i}. Their leading coefficients are one, so their determinant is the Vandermonde product prod_{j=0}^{r-1}j!. Consequently
\[
 D^{G}_{r,k}=c_0^r t^{rk}\prod_{j=0}^{r-1}\frac{j!}{(k+j)!},
 \quad \frac{(D^{G}_{r,k})^2}{D^{G}_{r,k-1}D^{G}_{r,k+1}}=\frac{k+r}{k},
 \quad Q^{G}_{r,k}=G_{r,k}.                                  \tag{9}
\]
The falling factorial vanishes for i>k+j, agreeing with the zero convention at negative coefficient indices. Also g_i=Phi^{(2i)}/Phi is a monic degree-i polynomial in R, so h_r=1. This checks all-order normalization exactly; Gaussian equality is not theta evidence.

### A precise continuous sufficient obligation at r=3

For real s>=0 define w_s=q^s w_0, Z(s)=int w_s, M(s)=int h w_s and A(s)=M(s)/Z(s). These are Mellin interpolants of the determinant integrals; no noninteger integration-by-parts identity with zero negative coefficients is asserted. The integer identity (1) is all that the order induction uses.

The accepted signed-averaging argument extends to every real tilt q^s, s>=0: it is increasing, the lattice inequality is unchanged, and the same compact exhaustion is integrable. Thus A(s)>=A(0)>0 for all real s>=0. This separately justifies taking log M(s); integer determinant positivity alone would not do so.

Let T=log q, m_s=E_s T and C_s=Cov_s(h,T). Differentiating the complete integrals gives
\[
 (\log M)''(s)=
 \operatorname{Var}_s(T)
 +\frac{\operatorname{Cov}_s(h,(T-m_s)^2)}{A(s)}
 -\left(\frac{C_s}{A(s)}\right)^2.                           \tag{10}
\]
All three terms are part of the signed logarithmic curvature. Association gives C_s>=0 but does not control the central-square covariance: (T-m_s)^2 is not increasing. Even a sharp variance bound for the positive carrier alone therefore leaves an unpaid term. This is the precise gap not covered by increasing A.

Define the explicit positive comparison function
\[
 \kappa_r(s)=\sum_{j=0}^{r-1}\sum_{n=0}^{\infty}
 \frac1{(s+j+\tfrac12+n)^2}.                               \tag{11}
\]
The selected source obligation is the **joint** bound
\[
 \operatorname{Var}_s(T)
 +\frac{\operatorname{Cov}_s(h,(T-m_s)^2)}{A(s)}
 -\left(\frac{C_s}{A(s)}\right)^2
 \le\kappa_3(s)\qquad(s>=0).                              \tag{12}
\]
It is sufficient for (7) at r=3. Indeed, with the triangular weight tau_k(s)=1-|s-k| on [k-1,k+1],
\[
 \log Q_{3,k}=\int_{k-1}^{k+1}\tau_k(s)(\log M)''(s)\,ds.
\]
Direct integration and telescoping of the positive series give
\[
 \int_{k-1}^{k+1}\tau_k(s)\kappa_r(s)\,ds
 =\sum_{j=0}^{r-1}\log\frac{k+j+\tfrac12}{k+j-\tfrac12}
 =\log G_{r,k}.                                            \tag{13}
\]
For completeness, each summand with b=k+j+1/2+n integrates to log[b^2/(b^2-1)]; the product over n telescopes to (k+j+1/2)/(k+j-1/2). This uses only elementary integration and the displayed convergent series, not an imported concentration theorem. At k=1 the interval is [0,2], with no negative-s continuation or uncomputed negative-index moment.

Equation (12) is presently **unproved for theta**. Its explicit comparison function and quantitative consequence make it a falsifiable sufficient estimate, but its formulation alone earns no positivity progress. A proof which simply invokes (5) or existing D4 positivity to bound its integral would be circular as a new mechanism. The pointwise bound (12) is stronger than the integrated requirement and could fail even if (7), or merely D4 positivity, holds.

## 4. Exact failure of the association-only comparison

Here is a finite information-relaxation test, not a modified theta source. Take the two-point chain q in {1,128}, base weights 128 and 1, and increasing h-values 1 and 2. Then, for every real s>=0,
\[
 Z(s)=128+128^s,\quad M(s)=128+2\,128^s,\quad
 A(s)=\frac{128+2\,128^s}{128+128^s}>0.
\]
A is strictly increasing; Z is a positive moment function and hence log-convex; positive association holds on a two-point chain. At s=k=1, mu_1 assigns probability 1/2 to each point. The finite expressions under examination are A=3/2, E(hq)=257/2 and E(h/q)=65/128. Exact rational arithmetic gives
\[
 Q_{3,1}=\frac{16705}{576}>28=\frac{16128}{576}>7=G_{3,1}.
                                                                  \tag{14}
\]
If the relaxed sequence is defined by D_k=M(k)/F_{3,k}, its neighboring ratio is exactly 16128/16705<1. This is the specified failed comparison: **monotonicity of A, positive-moment Z and association do not pay even the full factorial budget**. All computations in (14) are displayed finite rational expressions; no source sample or numerical acquisition is involved.

This relaxation does not claim D_k comes from a single Toeplitz coefficient sequence, nor h from a derivative-ratio determinant. It does not satisfy literal canonical reconstruction and is not a counterexample to theta, Review01, or an estimate using that missing differential structure. Its role is to identify what cannot follow from only the normalized information inherited from the accepted first-order comparison. The Gaussian comparison remains a possible theta-specific estimate, not a rejected universal theorem that was ever proved.

## 5. Boundaries, tails, controls and increasing order

For r=3, w_s and w_s h are locally integrable with every fixed power of log q, uniformly on compact s intervals in s>=0. Near zero the source and its even derivatives are bounded, the determinant factors introduce no poles, and integral_0^1 u^{2s}|log u|^m du is finite. Coincident-node singularities in h are removable; equivalently use w_s h=(prod u_j^{2s})V(u^2)Delta_3 to avoid quotient estimates. At infinity each fixed derivative has double-exponential decay and only fixed polynomial/exponential growth precedes it, dominating every finite power u^{2s}|log u|^m. These bounds justify (10), compact exhaustion and (13); they are not estimates of the sign in (12). All tails remain in the expectation. Full evenness supplies the original integer coefficient endpoint identity; it is never inferred from a finite theta truncation.

The k=0 anchor remains D_{r,0}=c_0^r. The first nontrivial induction test is k=1, where q^{-1} cancels exactly to w_0. The anchor supplies no neighboring upper bound. For arbitrary r, (2)–(9) retain explicit r dependence. To iterate one needs a proof of (7) for every finite r, not a list of pilots. Using the continuous route additionally requires M_r(s)>0 on every real slab; the accepted order-three monotonicity does not provide that for r>=4. A discrete proof of (7) would avoid this extra interpolation obligation. Constants may depend on r, but for each fixed r the allowed relative curvature still shrinks as k grows.

| Control | Premise actually missing or untested for this claim |
| --- | --- |
| Two-point relaxation (14) | Fails canonical derivative-determinant/source realization; demonstrates failure of the retained association-only information. It has no assigned physical collision. |
| Gaussian | Satisfies the generic representation and gives equality in (7); h_r=1 checks normalization. It is not canonical theta. |
| Euler-factor source | Positive even source but changed arithmetic reconstruction; its R'/K and signed comparison (12) are untested here. A positive-time collision gives no sign for this time-zero finite-order comparison. |
| Weighted-square and finite-prime perturbations | Fail complete canonical arithmetic and, in the relevant finite-endpoint constructions, full reflection. Matching finitely many odd endpoints does not authorize the growing-order integral identities. No Q or curvature sign is assigned. |
| Reflected super-Gaussian and smooth shape/positive-primitive controls | May retain evenness and decay but fail literal theta reconstruction. Their shape information does not supply (12); neither failure nor success of that quantitative inequality is inferred from collision. |

No additional external theorem is imported. The source identities, finite FKG application and integration-by-parts normalization are inherited from the inspected repository sources with their recorded primary-inspection limits. The determinant telescoping, Gaussian determinant calculation, Mellin differentiation and two-point comparison above are derived explicitly. No reference-catalog addition is requested.

## 6. What changed and what should happen next

The brief's qualitative competition between A, Z and factorials is now an exact budget (3), a selected stronger estimate (7) with the quantitative consequence (8), and a precise unpaid signed covariance term in (12). The failure of an association-only proof is established in the stated relaxation. There is still no new canonical higher-order estimate, no additional positive coefficient range, no induction theorem for growing r and no RH conclusion.

**Next: [B] signed Mellin-curvature comparison — Astra.** This recommendation stays conceptual: use the complete theta derivative structure to prove or refute one bound on the joint expression (10) relative to kappa_3(s), with the [0,2] slab explicitly included and a separate analytical tail. The deliverable is a source-sensitive inequality with its exact domain and payments, or a scoped failure of this Gaussian-envelope mechanism. If the only available proof input is increasing A, stop at (14). If a viable finite sign certificate becomes the sole remaining step, freeze its expression, domain, endpoint/tail bounds and acceptance test before recommending an E task to Sol. None is ready or authorized by this return.

## Input versions

The working tree includes uncommitted research; hashes identify the actual read inputs and are not mathematical certification.

| Input | SHA-256 |
| --- | --- |
| Note15 packet | `2d2fd23efd67b019c484ec551f779f1feaf4ffe08046ba457de6d5a3b1ec1f1a` |
| Note14 | `d8b9160e158317462d75a59d7535f500898cfb51345284d33287cf24eafd14f0` |
| Note05 | `32f8289741bac117b45399855558b554e1f1430adc7169a8229bfd69448e3cf2` |
| Branch02 brief | `6bfc02a07bdf2333a798ce794f4646565ae9fdf5bfdefdc1e60e55145cef86ef` |
| Accepted Review01 | `c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe` |
| Live register, active first-wave read | `256ecfd8290d14d91616932f83cdf39f9aba68023764f82533e2d5b0c0e25dc9` |

[packet]: ../../notes/15_CONTINUATION_PARALLEL_BRANCH_EVALUATION_20261101.md
[brief]: 00_INITIAL_BRANCH_BRIEF_20261101.md
[note14]: ../../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md
[note05]: ../../notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md
[review01]: ../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md
[results]: ../../../../../../result-summaries/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[shape]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[shared]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[numerics]: ../../../../../../avoid/10_numerics_ahead_of_the_question.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
