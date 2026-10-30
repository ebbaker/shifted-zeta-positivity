# E08 R11 assessment: primitive tests and uniform full-energy closure

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0034**, *Continue radial theta collision
research*. Type **E — execution**, fixed request **CTF-E08 R11**.

**Disposition: accepted without mathematical correction at
(T,A)=(1/4,2), within the inherited prepared radial solution class.**
All ten obligations of the [frozen request][packet] are covered below.
[Notes75][n75]–[76][n76] retain their issued bytes. The earlier preliminary
trace-sign correction is already present in the issued Note75; it is not
an outstanding correction or a new correction by this assessment.

This is the parent's different-model internal assessment of Astra/ultra's
proof, supported by three read-only Sol/ultra contributing audits. Those
contributors belong to this assessment, and all checks share inherited
PDE, source and R10 premises. Neither contributor agreement nor the model
change provides independent specialist review, formal verification or an
interval certificate. The [record][record] separates file checks from the
mathematical judgment. [Progress05][progress] owns live disposition.

## 1. Full adjoint, cutoff and sphere specialization — pass

Use Note75 (1)–(6), with b=hX, beta=sigma X, h=zeta log r and
omega=(1+r²)^(-2). Direct divergence gives
\[
 \operatorname{div}(\omega\beta Z)
 =\omega\left[\sigma rZ_r+
  \left(3\sigma+r\sigma'-\frac{4\sigma r^2}{1+r^2}\right)Z\right].
\]
Thus eta=2C1*(omega Z) has exactly Note75 (4)'s sign, divergence,
weight derivative, zeta' and zeta'' terms. On the neighborhood where
zeta=1, sigma=r lambda' log r−lambda, so
sigma'=log r(lambda'+r lambda''). At r=1, lambda=3/2,
sigma=−3/2, sigma'=0. Reflection gives ell_T'(1)=−3,
c'(1)=3 and gamma(1)=−9/2. Hence
\[
 \boxed{\eta_j(1)=\tfrac34 Z_{j,r}(1)-\tfrac32 Z_j(1).}
\]
This terminal value is distinct from either transported initial-support
trace. There is no imposed vanishing of those traces. Coefficients with
the cutoff vanish near the origin; v and d themselves do not.

## 2. Distributional test and Gaussian preparation — pass

Pairing the divergence with a scalar f in H1 gives
\[
 |\langle\eta_j,f\rangle|
 \le2\|Z_j\|_2(B_1\|\nabla f\|_2+B_0\|f\|_2).
\]
Only the existing residual norm is required. Since Jj=P_(s,0)K1 Fraw_j,
the adjoint order is chi=K1 P_(s,0)* eta. Its kth derivative is
\(\langle\eta_j,P_{s,0}D_x^kK_1(x-\cdot)\rangle\), k=0,1,2.
Derivatives act on the Gaussian before propagation, so the proof neither
commutes derivatives through P nor differentiates the feedback path.

With C_G=(8pi)^(-3/2), the Fourier Gaussian has coordinate variance 1/4:
\[
 (E_0^{\rm seed},E_1^{\rm seed},E_2^{\rm seed})/C_G
 =(1,1/4,3/16),\qquad
 (G_0^{\rm seed},G_1^{\rm seed},G_2^{\rm seed})/C_G
 =(3/4,5/16,21/64).
\]
These seed energies are distinct from the preserved field energy E0.
The L1 seed costs are 1, 1/sqrt(pi), and at most 1. The last uses
D_e²K1=((x·e)²/4−1/2)K1 and variance 2 under K1. No new unknown norm
or feedback derivative enters.

## 3. Finite-path and uniform transported seeds — pass

Note75 (10) follows from E'<=6alpha E and
G'<=10alpha G+30alpha E. Multiplication by exp(−10B) leaves
\[
 30E_k\int_0^s\alpha e^{-4B}
 =\tfrac{15}{2}E_k(1-e^{-4B(s)}).
\]
This finite-B payment does not require a physical mass floor.

For the uniform version retain the full Fourier deficit:
\[
 (2\pi)^{-3}\int_{|\xi|<R}(R^2-|\xi|^2)\,d\xi
 =\frac{R^5}{15\pi^2}.
\]
Optimizing R³=6pi²E/m² gives
G>=cN E^(5/3)m^(-4/3), cN=(3/5)(6pi²)^(2/3).
For all seed L1 norms <=1 and alpha<=alpha_bar, comparison yields
E<=E*=max{C_G,(3alpha_bar/cN)^(3/2)}. Then
\[
 G'\le-2G^2/E_*+10\bar\alpha G+30\bar\alpha E_*.
\]
Its positive normalized root is
(5alpha_bar+sqrt(25alpha_bar²+60alpha_bar))/2, exactly Note75 (11).
All initial seed gradients are <=3E*/4. This proves the claimed
uniform gradient barrier, including alpha_bar=0. Uniformity spends
R10's paid alpha_bar; it does not supply that premise.

## 4. Primitive coefficients, tail and both endpoints — pass

Because r'=2r and r''=4r, differentiation gives exactly
\[
 (\partial_u^2-1)(c_j\chi(r))
 =(c_j''-c_j)\chi+4r(c_j'+c_j)\chi_r+4r^2c_j\chi_{rr}.
\]
The extra 4r c_j term is essential and is present. Complete theta decay,
with exp(−pi exp(4u)) dominating all fixed exp(Tu²), polynomial and r²
factors, pays the absolute integral and the infinity boundary terms.
For j=0, c0(0)=1 and c0'(0)=0; the endpoint is
chi_0(1)/16+A_theta(1)chi_0,r(1)/4. For j=1, both values vanish.
Neither evolving sphere compatibility nor primitive positivity removes
the two j=0 terms. The sqrt(2) endpoint and sqrt(3) bulk Cauchy–Schwarz
costs in Note75 (17) give its (18) with no missing factor. Multiplication
by alpha and Young's inequality give the stated alpha_bar² allowance.
It is an absolute bound with no proved strict signed benefit.

## 5. Bochner reconstruction and the direct comparator — pass

The exact radial measure gives
\[
 K_1F_j^{\rm raw}=\int_0^\infty\Phi(u)c_j(u)k_{e^{2u}}\,du.
\]
Spherical averages of translated Gaussian derivatives bound k_r,
partial_r k_r and partial_r² k_r uniformly in L1 intersect H1. The
third Gaussian derivatives needed for the last H1 norm are known seed
costs, already included in G_2; they are not residual derivatives.
Theta domination justifies the two Banach-valued integrations by parts,
with both endpoint terms of Note75 (21).

To spell out the continuity at the operator passage: P is bounded on
L1 intersect H1 on each finite regular path by contraction and the E/G
estimates above. Also
\[
 \|\omega C_1f\|_2\le B_1\|\nabla f\|_2+B_0\|f\|_2.
\]
Therefore propagation, weighted C1 and the final L2 pairing preserve the
Bochner identity and its truncation limit. The entire joint expression
reconstructs the same prepared source that the direct method receives.
The relaxed independent-Z optimization is unchanged by representing
that source differently; it asserts no obstruction for the constrained
actual theta trajectory.

## 6. Fixed common-path jets and normalization — pass

Preparation and the positive conservative scalar propagator contract L1,
including signed data. Thus ||Jj||1<=Mj for each fixed integer j. The
same Fourier estimate and exact scalar energy identity give
\[
 Q_j'\le-2c_NM_j^{-4/3}Q_j^{5/3}+6\bar\alpha Q_j,
 \qquad
 Q_j\le M_j^2\mathcal D(K),\quad
 \mathcal D(K)=\max\{e_+,(2K/c_N)^{3/2}\}.
\]
Gaussian Young pays the initial e+ term. All Mj are finite; the constant
varies with j. This is not uniformity in order or a parameter domain.

The assessed M2/M0<1/72 converts to M2/(M0+M2)<1/73, hence precisely
Q2/E0<=D(K)/(73²e_-). The e_- formula in Note76 (3) follows from
the time-zero carrier inequality, the paid floor
mu>=mu_*=(70/73)M, and R0/M<26/3, including the full preparatory 6M.
There is no 72² normalization after changing the denominator to M.

The premise chain is Note55's full-source slope -> Note67's positive
physical mass floor -> positive carrier moment floor -> K -> these
barriers. Note67 acquires K within the lifespan before invoking its
continuation criterion. No global existence or uniform residual theorem
is used circularly. E0>0 alone does not supply the physical mass floor.

## 7. Coefficient costs and the entire residual — pass

For Cb, on r>=1 use log r<=r and r²/(1+r²)²<=1/4.
On [1/2,1], use log2<3/4 and
max r/(1+r²)²=9/(16sqrt(3))<1/3. Below 1/2 the coefficient vanishes.
Thus Cb<=1/4.

Solve the full gamma identity for c' and integrate from c(1)=0.
On [1/2,1] the two payments are at most 4B0 log2<3B0 and
(27/25)log2<3/4; the elementary series gives log2<25/36.
On [1,infinity) they are at most 5B0/8 and
\[
 \tfrac14\int_1^\infty\log t\,[-d'(t)]\,dt
 =\frac{3\log2-1}{8}<\tfrac34.
\]
The displayed integral follows by integration by parts and t² substitution.
Consequently Cc<=3B0+3/4 with all cutoff variation paid by B0.

The exact residual and T=(2V,V)+(0,2J2) then give
\[
 \sqrt{Y}\le\tfrac14\sqrt G+
 (3B_0+3/4+\sqrt5)\sqrt{E_0}+2\sqrt{Q_2}.
\]
For q=D(K)/(73²e_-) or the smaller actual-moment allowance, put
\[
 y=\left[\sqrt K/4+3B_0+3/4+\sqrt5+2\sqrt q\right]^2,
 \qquad F_*=E_0(K+y+q).
\]
Then F_R<=F_* for all auxiliary time. This uses the genuine residual,
its nonzero preparation defect, actual jets, and the whole inner ball.
There is no division into singular sphere quotients. R(1)=−T(1)
remains a combined compatibility relation. Uniformity is weighted;
a global unweighted residual norm is not inferred.

## 8. Complete production and sliding dissipation — pass

Note47 (20)–(21) supplies exactly
\[
 F'+D_R+\alpha H_{\rm rad}
 \le(\kappa_0+\kappa_1\alpha)(F+E_0),\quad
 \kappa_0=8+A_2^2+A_1+A_0,\quad
 \kappa_1=274/25+B_1+B_0.
\]
C0 consumes one N and leaves D_R=N+2||grad Z||²+2||grad J2||².
C1, source/cutoff terms, radial remainder and inner-region costs are
retained. The r=2 split partitions a volume integral, with no new flux.
With C*=kappa0+(2K/3)kappa1, integration yields
\[
 \int_t^{t+\ell}(D_R+\alpha H_{\rm rad})\,ds
 \le F_*+C_*(F_*+E_0)\ell\quad(t\ge0,\ \ell>0).
\]
Only the nonnegative endpoint F(t+ell) is dropped. The cumulative
bound is F(S)+integral_0^S(...)<=F(0)+C*(F_*+E0)S. It is linear,
not finite total dissipation or pointwise uniform dissipation.

## 9. Matched comparison and finite crossover — pass

Both envelopes hold, so their minimum is valid. Construction gives
F_*>=F(0), while Xi=kappa0 s+kappa1 B(s)>=(kappa0+kappa1 a_*)s.
The crossover
\[
 s_c=\frac{\log[(F_*+E_0)/(F(0)+E_0)]}
            {\kappa_0+\kappa_1a_*}\ge0
\]
is finite and correctly directed: s>sc makes F_* strictly smaller than
the older displayed exponential allowance. This compares sufficient
allowances, without claiming actual energy growth or optimal constants.
The direct comparator has the same source, physical mass and retained
diffusion. It pays the entire declared consumer. R11's stop rule applies;
no primitive-specific gain, new acquisition saving or second mechanism
is supplied by this assessment.

## 10. Sign and control scopes — pass

For Note75's oscillatory compact radial triples, a_b a1>0 on 3/4<r<1
and a_b a1<0 on r>1. Cos² averaging gives exactly
4pi integral r²omega² a_b a1 phi² as I1/n² tends to its limit.
Those triples satisfy the algebraic residual definition but fail the
fixed theta/cosine/unit-preparation/common-path conditions. The result
screens a coefficient-geometry-only semidefiniteness claim; actual
source–residual–path correlation remains unresolved.

| Control | Exact premise or limitation |
| --- | --- |
| Gaussian-polynomial / normalized positive primitive | The unchanged theta sum is absent. Primitive transfer and normalized completion alone are shared; an actual double event has zero mass and fails R10's positive physical floor. |
| Fixed-theta polynomial/variable observation kernel | Literal cosine fails in the physical-margin payment. Theta's K cannot be imported at its zero-mass mark. |
| Positive weighted-square | Can pass sufficient low-mark moment bounds. A collision at another frequency does not contradict this one-mark theorem; at an admitted double event the positive mass premise fails. |
| Reflected, finite-prime and endpoint controls | Retain their recorded admission domains; an admitted double event fails the positive mass premise. No new ratios or locations are acquired here. |
| Euler-factor Laguerre witnesses | A negative Laguerre witness is not automatically a double event; no zero-mass statement is manufactured. |
| Atomic/profile controls | Must first meet the inherited smooth prepared solution hypotheses and actual path/mass premises. |

Finite-path Gaussian test bounds can hold inside a colliding control's
regular lifespan. Their constants depend on that path interval and give
no global contradiction. The uniform theorem retains R10's physical
margin; it supplies no margin-free regularity, larger physical domain,
uniform-in-order jet bound, bounded total B, convergence, RH conclusion
or literature-priority result.

## Consequence and continuation

The accepted scientific baseline now includes uniform full weighted
residual energy, each fixed common-path jet and complete fixed-window
dissipation at the already covered mark. The primitive test costs are
paid, while its additional signed utility remains unproved. Parent B02
stays partial and E03/B03 stay gated. [Return78][return] records the concise
research consequence; [Continuation79][next] provides the model/history
handoff. **Next: [E] CTF-E05 R4 — Sol**, proportionate integration under
the [bounded packet][integration]. No manuscript was changed here.

This assessment follows the [result index][results] and [avoid index][avoid],
especially [collision controls][controls], [geometric results][geometry],
[target reformulation][a01], [shared premises][a05], [scope][a07],
[separate bounds][a12] and [quantitative utility][a20]. All 17 issued
input hashes and the frozen request match at intake and completion;
139 protected inherited files retain their baseline bytes. These are
identity checks, not proof certificates.

[packet]: ../research-progress/handoffs/CTF-E08_PRIMITIVE_TEST_AND_UNIFORM_CLOSURE_R11_20261029.md
[n75]: ../notes/75_PRIMITIVE_TEST_COSTS_AND_SIGNED_COMPARISON_R11_20261029.md
[n76]: ../notes/76_UNIFORM_RESIDUAL_AND_FIXED_JET_CLOSURE_R11_20261029.md
[record]: ../numerics/30_PRIMITIVE_R11_E08_ASSESSMENT_RECORD_20261029.json
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[return]: ../notes/78_PRIMITIVE_R11_E08_RESEARCH_RETURN_20261029.md
[next]: ../notes/79_PRIMITIVE_R11_ASSESSMENT_AND_MODEL_CONTINUATION_20261029.md
[integration]: ../research-progress/handoffs/CTF-E05_UNIFORM_RESIDUAL_INTEGRATION_R4_20261029.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
