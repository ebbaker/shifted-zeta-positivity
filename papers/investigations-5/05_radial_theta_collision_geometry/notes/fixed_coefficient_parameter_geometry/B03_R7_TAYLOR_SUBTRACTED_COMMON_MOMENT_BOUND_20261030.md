# B03 R7: a Taylor-subtracted remainder paid by an existing complete moment

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual parent **gpt-6-astra / ultra**, existing Investigation05 **chat0049**. Two read-only **gpt-6.1-sol / ultra** contributions check the kernel algebra, primitive transfer, positive-moment shortcut and exact rational constants. These are internal checks sharing inherited premises. [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md) alone owns status.

**B03 R7 return.** Register **C04 R4**, the degree-four direct-inner Taylor tail below, on the old representative ball only. Subtracting the known parameter polynomial before estimating its source kernel replaces the raw outer-G Cauchy payment. An already acquired complete positive moment pays the new tail; no new source integration is required. Both the direct and selected primitive payments satisfy a positive degree-four margin using the explicit saved-input caps below. The direct payment is smaller. The [fixed E02 R7 assessment](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R7_TAYLOR_SUBTRACTED_ASSESSMENT_20261030.md) will verify all source caps, constants, consumer comparisons and scope. **E01 R4 acquisition is skipped**, not represented as performed.

This is a finite sufficient-bound improvement, not an RH-equivalent definition, new physical region or primitive-specific gain. Earlier C04 definitions and the accepted R6 absolute-payment obstruction are unchanged. Same-information scalar Taylor consumers must be checked as well; a successful joint bound must not conceal a scalar separation already supplied by the same inputs.

## 1. Fixed family and the subtraction

Use [Note26](26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md) and the [R7 brief](B03_R7_CONTINUATION_AND_MODEL_HANDOFF_20261030.md), with
\[
 (\tau,a,R,r,N)=(1/4,64,1/32,1/128,4),\qquad t=T_{\rm phys}-\tau,\quad x=A-a.
\]
The complete unit-coefficient theta source, literal cosine, quadratic heat reference, drift, unit Gaussian preparation and full spatial R³ remain fixed. Write h_j=∂_A^jH(τ,a), b=h_2, B=|b| and η=|h_1|. Let K be the complete combined source kernel from Note26(20), with
\[
 G=\int_0^\infty\Phi K,\qquad
 K_{>4}=K-\sum_{m+n\le4}k_{mn}(u)t^mx^n.
\]
All coefficients k_mn are formed before integration, and g_mn=∫Φ k_mn. Put
\[
 E_n(z)=e^z-\sum_{j=0}^{n}\frac{z^j}{j!},\quad
 z_\sigma=tu^2+i\sigma xu,\quad C_\sigma=e^{\tau u^2+i\sigma au},\quad
 A_\sigma=-2b+i\sigma h_1u,\quad \sigma\in\{-1,1\}.
\]
An exact exponential expansion gives
\[
 \boxed{K_{>4}=\frac12\sum_{\sigma=\pm1}C_\sigma
       \{A_\sigma E_4(z_\sigma)+i\sigma bxu E_3(z_\sigma)\}.} \tag{1}
\]
Indeed the un-subtracted σ-summand of K equals
\[
 C_\sigma\{(A_\sigma+i\sigma bxu)e^{z_\sigma}
       +(2b-i\sigma h_1u)+2btu^2+i\sigma bxu+h_1xu^2\}.
\]
The correction outside the exponential has total parameter degree at most one. Truncating through degree four therefore gives (1), including the degree shift caused by multiplication by x.

Both the original K and its coefficientwise subtraction vanish with their first u-derivative at zero. Formula (1) also gives K_{>4}=O(u⁵) uniformly on compact parameter sets. Complete differentiated theta decay pays infinity. Thus
\[
 G-\sum_{m+n\le4}g_{mn}t^mx^n
  =\int_0^\infty\Phi K_{>4}
  =\frac18\int_0^\infty\psi[(K_{>4})_{uu}-K_{>4}]. \tag{2}
\]
For any finite fixed U the exact alternative retains
\[
 \frac{\psi'(U)K_{>4}(U)-\psi(U)(K_{>4})_u(U)}8
 +\frac18\int_0^U\psi[(K_{>4})_{uu}-K_{>4}]
 +\int_U^\infty\Phi K_{>4}. \tag{3}
\]
No finite boundary is set to zero. The selected estimate uses the whole-line identity (2), not a truncated version of (3).

## 2. Uniform polynomial envelopes on the inner bidisk

For |t|,|x|≤r put
\[
 w=r(u^2+u),\quad s=(\tau+r)u^2+ru,\quad
 D=s'=2(\tau+r)u+r,
\]
\[
 p_b=\frac{2w^5}{120}+\frac{ruw^4}{24},\quad
 p_h=\frac{uw^5}{120},\quad p_S=\frac{w^5}{120},\qquad
 P_0=Bp_b+\eta p_h. \tag{4}
\]
Define the positive-coefficient differential operator
\[
 \mathscr L P=P''+2(D+a)P'
              +[(D+a)^2+2r+1/2]P. \tag{5}
\]
Then
\[
 |K_{>4}|\le e^sP_0,\qquad
 |(K_{>4})_{uu}-K_{>4}|\le e^s\mathscr LP_0. \tag{6}
\]

Here is the derivative accounting. Let
\[
 H_0=(2B+\eta u)E_4(w)+BruE_3(w).
\]
From (1), |K_{>4}|≤e^(τu²)H_0. Since |z_σ|≤w, |z_σ'|≤w'=r(2u+1), |z_σ''|≤w''=2r, differentiating its analytic exponential tails gives derivative envelopes H_0',H_0'' for the bracketed expression. These are derivatives of the positive majorant, not derivatives of an arbitrary pointwise inequality. Coefficientwise,
\[
 E_n(w)\preceq e^w\frac{w^{n+1}}{(n+1)!}:
 \quad\frac1{k!}\le\frac1{(n+1)!(k-n-1)!}\quad(k\ge n+1).
\]
Composition with w and multiplication by nonnegative-coefficient polynomials preserve this order, as do derivatives. Therefore H_0^(j)≤(e^wP_0)^(j) for j=0,1,2. With |2τu+iσa|≤2τu+a and |2τ−1|=1/2, the product rule yields exactly (5)/(6). There is no extra +1 in (5).

For an explicit rational implementation, with c=r⁵/120,
\[
 p_b=c u^5(1+u)^4(2u+7),\qquad p_h=c u^6(1+u)^5.
\]
Their coefficient lists, starting at powers five and six, are [7,30,50,40,15,2]c and [1,5,10,10,5,1]c. The two primitive polynomials have degree at most twelve and thirteen and vanish to order at least three. Every polynomial used below has nonnegative coefficients and zero constant term.

## 3. The selected primitive estimate is dominated by the direct estimate

The actual polynomial-envelope integrals
\[
 T_D^+=\int_0^\infty\Phi e^sP_0,\qquad
 T_P^+=\frac18\int_0^\infty\psi e^s\mathscr LP_0
\]
are full-source tail bounds. Applying the exact primitive identity to S=e^sP_0, whose lower and upper boundary terms vanish, gives
\[
 T_P^+-T_D^+
 =\frac18\int_0^\infty\psi e^s
       [2aP_0'+(2aD+a^2+1)P_0]>0 \tag{7}
\]
when (B,η)≠(0,0). This is a statement about these particular derivative-triangle envelopes. It is not a rejection of every primitive estimate or of signed source integration. It also is not the old R6 first-t obstruction: that coefficient has actually been removed.

## 4. Pay both tails with one already acquired complete moment

Set
\[
 T_0=17/64>\tau+r=33/128,\quad \delta=4-r=511/128,\quad
 X_1=\int_0^\infty u e^{T_0u^2+4u}\Phi(u)du. \tag{8}
\]
X_1 is the **positive moment** acquired at 384 bits in E01 R2, not the signed jet h_1. No new integral is evaluated here. For P(u)=Σ_{k≥1}p_k u^k with p_k≥0 define the explicit rational functional
\[
 \mathcal C(P)=\sum_{k\ge1}p_k\frac{(k-1)!}{\delta^{k-1}}.
\]
The exponential series gives u^k≤[(k−1)!/δ^(k−1)]u e^(δu). Consequently
\[
 \int_0^\infty\Phi e^sP\le X_1\mathcal C(P). \tag{9}
\]
All source modes and the whole exterior remain in X_1. The termwise identity
\[
 \Phi_n/\psi_n=z(2z-3)>9,\quad z=\pi n^2e^{4u}>3
\]
proves ψ<Φ/9. Thus the selected explicit payments are
\[
 \boxed{\widehat T_D=X_1[B\mathcal C(p_b)+\eta\mathcal C(p_h)],\qquad
 \widehat T_P=\frac{X_1}{72}
       [B\mathcal C(\mathscr Lp_b)+\eta\mathcal C(\mathscr Lp_h)].} \tag{10}
\]
Applying (9) to \mathscr LP_0 is valid because it too vanishes at zero; P(0)=0 alone would not guarantee this for a general P.

The following are exact rational coefficients, independently checked in the fixed Sol algebra contribution and to be replayed by E02:

| Polynomial | Exact C value | Strict rational upper cap |
| --- | --- | --- |
| p_b | 1989705625478911 / 217205108433542126803400320 | 9.161e−12 |
| p_h | 881126540079433 / 173424703764906291869589943 | 5.081e−12 |
| Lp_b | 247535379492981804236892593407 / 5575489793485205047839689437222010880 | 4.440e−8 |
| Lp_h | 183125734587832495414844581961 / 7419466886643072342307503391719915520 | 2.469e−8 |
| p_S | 532944860489673 / 217205108433542126803400320 | 2.454e−12 |

Coefficientwise, \mathscr LP_0≥a²P_0; hence the hatted payments satisfy
\[
 \widehat T_P\ge\frac{512}{9}\widehat T_D>\widehat T_D \tag{11}
\]
for nonzero (B,η). This is a second explicit comparison of the **common-moment** payments (10); it must not be confused with a universal ratio between the integrals in (7).

## 5. Degree-four certificate and its exact coefficient

Let
\[
 F_4=\sum_{1\le m+n\le4}|g_{mn}|r^{m+n},\quad
 D_0=h_1^2-2bh_0,
\]
where g_mn are the full signed coefficients of Note16. Define the new direct coefficient **C04 R4** by
\[
 \Gamma_4^D=F_4+\widehat T_D,\quad
 d_4^D=|D_0|-2b^2r-\Gamma_4^D,\quad
 c_4^D=\frac{d_4^D}{1+h_0^2+h_1^2+b^2}. \tag{12}
\]
Define Γ_4^P,d_4^P similarly with \widehat T_P for comparison. These are **direct inner remainder bounds**: do not multiply either new tail by a Cauchy factor. The old accepted comparator remains
\[
 \Gamma_4^C=F_4+M_C T_4(1/4),\qquad T_4(1/4)=19/2304.
\]
From the accepted full-source record, the following conservative rational caps are sufficient and must be verified from its binary intervals in E02:
\[
 B<1.18\,10^{-11},\quad\eta<4.20\,10^{-10},\quad X_1<0.0096,
\]
\[
 |D_0|>1.905\,10^{-19},\quad F_4<5.722\,10^{-22},\quad
 2b^2r<2.141\,10^{-24}. \tag{13}
\]
The exact coefficient caps above give
\[
 \widehat T_D<2.153\,10^{-23},\qquad
 \widehat T_P<1.453\,10^{-21}.
\]
Therefore
\[
 d_4^D>1.899\,10^{-19},\qquad d_4^P>1.884\,10^{-19}>0. \tag{14}
\]
These inequalities follow even from the coarsened saved-source caps, without acquiring the proposed four new integrals. The old degree-four C margin is negative in R5; its degree-eight case was positive on this same ball. The asserted gain is **a degree-four sufficient certificate on an already certified ball**, not a minimum-degree theorem or new coverage. E02 will verify the exact hatted enclosures and the baseline comparison before accepting this return.

The exact row gives |J|≥μ_D=d_4^D/K_r, where
\[
 K_r=\sqrt{4b^2+(|h_1|+r|b|)^2}.
\]
For c=c_4^D>0, the inherited fixed-flow theorem applies unchanged. The original E01 R2 complete L,R2 moments were acquired at the larger T_0, so they conservatively pay the carrier on the present ball. E02 may report the resulting exact-defined-c all-time floor using these saved inputs; it must not substitute a rounded c as the definition. C01 still imports compact-uniform derivative convergence and supplies no acquired start time.

## 6. The strongest matched scalar consumers supplied by these inputs

The new moment payment applies also to the separate scalar Taylor remainders. Put
\[
 f_{mn}=\frac{(-1)^m h_{2m+n}}{m!n!},\qquad
 f^A_{mn}=\frac{(-1)^m h_{2m+n+1}}{m!n!}.
\]
The degree-four polynomial of H_A is built separately using f^A: it is not merely the derivative of the degree-four polynomial of H. Both use the same h_0,…,h_9 and X_1 already available for the row. On the same bidisk,
\[
 |H|\ge |h_0|-\sum_{1\le m+n\le4}|f_{mn}|r^{m+n}-X_1\mathcal C(p_S),
\]
\[
 |H_A|\ge |h_1|-\sum_{1\le m+n\le4}|f^A_{mn}|r^{m+n}-X_1\mathcal C(p_h). \tag{15}
\]
The same caps pay these tails by 2.356e−14 and 4.878e−14. Their finite sums/signs remain for E02's fixed saved-input assessment. If a scalar floor passes, do not describe the case as exercising an actual simple-zero crossing. Any positive component floors also give a direct Euclidean box-distance lower bound. The same-information direct row strip retains at least μ_D; no flow or coordinate advantage is asserted. Retaining only R5's older coarse scalar floors would not be a fair comparison after deriving (9).

## 7. Fixed-degree limitation inherited by this new payment

This is a scope check, not another numerical campaign. At fixed τ=1/4,r=1/128,T0 and degree four, X1 and c_b=C(p_b),c_h=C(p_h)>0 do not depend on center frequency a. For the *new common-moment direct rule* let
\[
 \nu(a)=\max\{2|h_0(a)|/(X_1c_b),\ |h_1(a)|/(X_1c_h)\}.
\]
Then exactly
\[
 d_4^D\le(\nu(a)-1)\widehat T_D-2b^2r-F_4. \tag{16}
\]
The accepted complete-source IBP bounds in [Note22](22_FIXED_DEGREE_TAIL_AND_QUADRATIC_TIME_LIMITS_B03_R4_20261030.md) give |h0|≤V0/a, |h1|≤V1/a with finite source-defined V0=∫|(e^(τu²)Φ)'| and V1=∫|(ue^(τu²)Φ)'|. Thus every
\[
 a\ge\max\{2V_0/(X_1c_b),V_1/(X_1c_h)\}
\]
is rejected by this fixed-radius, fixed-degree, positive common-moment payment. If B=η=0, d=0 directly. This merely applies the accepted linear-budget versus quadratic-discriminant argument to the explicitly new rule; it gives no numerical height, no actual theta collision and no rejection of adaptive r,N or signed phase-retaining estimates. The finite degree reduction must not be extrapolated into an efficient high-frequency schedule.

## 8. Controls, status and next dependency

At any genuine collision inside the tested ball, the exact row forces every valid d≤0. Apply the [control register](../../../../../result-summaries/12_collision_controls_and_screening.md) to each control's own source, derivative/moment domain and event ball. Gaussian-polynomial and weighted-square controls do not share the unit theta source; weighted-square/finite-prime controls fail their recorded full reflection; Euler-factor sources alter arithmetic and their negative-Laguerre witnesses do not themselves locate collisions; reflected/positive-primitive controls lack full theta square arithmetic. Atomic/finite-profile sources require their own admissible moment/primitive formulation. Conditional endpoint controls retain their RH hypothesis and arithmetic failure. Changed observation kernels fail literal cosine/Newman reconstruction; relaxed profiles are not physical events. No source datum or event is transferred to (1/4,64).

The moment-compression inequality (9) is generic. The actual theta source supplies the signed jets and complete moment; its termwise relation ψ<Φ/9 is used only for the primitive upper payment. A colliding control can satisfy upper-moment estimates and still fail the positive signed discriminant margin. Positivity of a primitive and boundary cancellation alone do not distinguish theta.

**Next fixed task: E02 R7/Sol**, not new acquisition: verify this proof, the five rational constants, all saved-input caps, complete matched consumers, fixed-degree scope and any inherited flow consequences. B04 remains gated. No manuscript, DRAFT_HISTORY, prior source record or issued packet is changed. Parent is the sole progress/history writer. Read the [result index](../../../../../result-summaries/README.md), [theta summary](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [avoid index](../../../../../avoid/README.md), especially [target classification](../../../../../avoid/01_restating_the_target.md), [separate bounds](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [scoped negatives](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [noncircular inputs](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).
