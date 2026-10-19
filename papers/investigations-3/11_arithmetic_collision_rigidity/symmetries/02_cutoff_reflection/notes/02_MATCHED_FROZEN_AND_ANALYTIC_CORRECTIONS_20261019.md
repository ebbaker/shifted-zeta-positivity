# S02-T1: matched frozen-exponential and full analytic correction

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6.1-sol (Codex), actual reasoning effort ultra**, verified from root session metadata. Separate delegated same-model mathematical, code and control audits are internal LLM review; no specialist review.

**Result.** On both declared boxes the full analytic correction does **not** beat the strongest frozen-exponential comparator under the shared first-derivative continuation ledger. Select the frozen formula for S02-T2's local physical jets. Restoring the earlier analytic ninth-mode matching sharpens the crossing allowance from approximately 0.431777199 to 0.229588635 for the full formula and 0.229588317 for the frozen formula. This gain is implementation of an established matching estimate, not superiority of the newer analytic correction. No evaluated whole-cell field, physical margin, speed gain or new collision coverage is claimed.

The [matched comparison contract](../../notes/02_S02_MATCHED_CORRECTION_COMPARISON_CONTRACT_20261019.md) extends INT-01. The [opening S02 note](01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md) supplies the exact full correction and source constants. The earlier [transport Note 20](../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md) and [Note 22](../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md) supply the frozen exponential, physical correlation and analytic cutoff matching. [Note 21](../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md) is a separate exact-source formulation, not a stronger error constant for these boxes.

## 1. Objects, metric and fixed coverage

Keep B=[1/100,1/5] x [999,1001], C=[1/100,1/5] x [1017,1019], and radius R=1/2 at every real center X. The upper disk unions lie in x=[998.5,1001.5] or [1016.5,1019.5], 0<=y<=1/2. Use exactly the opening rational covers: t/x/y grids 4/24/8 and 8/64/16, with 768 and 8192 complex cells, plus the same t/x real slices. Both retained runs use 192 and 256 bits without a parameter or grid search.

Write k=pi/8, Q=H/A, and use the original symmetric nonvanishing normalizer A, not the positive arithmetic carrier or the fixed Gc. Fix N=8 on each analytic disk. The natural cutoff is 8 on B and 8 or 9 on C. Put

\[
 v=z/2+\pi t/8,\quad a=\sqrt{v/(2\pi)},\quad p_N=2N+1-2a,
\]
\[
 J_N(t,z)=\sqrt v\{vD(p_N)-I(p_N)\},\quad
 B_t=(-1)^{N+1}\frac{\sqrt\pi}{4}e^{-\pi^2t/64},
\]

with the opening note's real-symmetric analytic profiles D,I. The full and frozen corrections are

\[
 C_N^{an}(t,z)=B_te^{-kz}J_N(t,z),\qquad
 C_{N,X}^{fr}(t,z)=B_te^{-kz}J_N(t,X).
\]

Compare F_an=(G8-C8_an)/A and F_fr,X=(G8-C8_fr,X)/A by the **complete uniform normalized disk residual eta**. Cauchy then pays the same factors (1,2,8) for Q derivatives through order two. All finite terms 1–8 are retained; mode 9 is part of the exact source transition. No derivative acts on a jumping cutoff.

The frozen center X is a parameter held fixed while differentiating in z. At z=X the two correction values agree exactly. Their first and second derivatives generally differ. In particular, differentiating the diagonal function X↦G8(X)-C8(t,X) would yield the full analytic jets, not the selected frozen jets. T2 must respect this distinction.

## 2. Shared complete source and transition ledger

The imported source is [D.H.J. Polymath, Corollary 6.4 and Proposition 6.6](https://arxiv.org/html/1904.12438v2#S6.SS3). Its hypotheses 0<t<=1/2, x>=200 and 0<=y<=1 hold on both upper rectangles. The original formulas, including the 0.397 reflected-channel error and the printed correction's exp(-kiy) factor, were checked against this primary source. The published error theorem is imported, not re-proved or certified by our scalar computations.

Let C_m_pub(t,x+iy)=exp(-kiy) C_m(t,x), where m is the natural cutoff. This printed correction is not holomorphic. For **either** holomorphic correction C*, the exact identity is

\[
 H-G_8+C^*=(H-G_m+C_m^{pub})
 +(G_m-G_8)-(C_m^{pub}-C_8^{pub})
 +(C^*-C_8^{pub}). \tag{1}
\]

Thus both formulas can use the same complete two-sum error, corrected published residual and earlier **printed-jump** matching. This avoids charging the full analytic formula the wider direct interval transition from the opening execution. It also avoids treating the earlier printed-jump theorem as an unpaid direct analytic-jump theorem.

Use the opening K*, W* and P* bounds. Here W(t,x) is the exact real prefactor/A(t,x), and

\[
 P_*\ge \sup\frac{e^{t\pi^2/64}|M_0(iv_x)|}{|A(t,z)|},\qquad v_x=x/2+\pi t/8,\quad x=\Re z,
\]

with the same explicit K factor and square-root multiplier paid as in the opening note. The corrected source contribution is Epub=P* tilde_epsilon. It is smaller here than the older K Z B_C majorant; both are reported so improving old source data is not credited to the full analytic formula.

For C, transport Note 22 gives

\[
 E_{edge}=2P_*(e^{\Lambda_{edge}}-1), \tag{2}
\]

where m=9, v_-=x_-/2+pi epsilon/8, a_-=sqrt(v_-/(2pi)), a_+=sqrt(v_+/(2pi)), d=max|a_±-9|, and E=max|log(a_±/9)|. With sigma*=(1+R)/2, Delta=sqrt(sigma*^2+(pi t_+/8)^2), D0=3/(2v_-), D1=1/(2T_-)+3/(2T_-^2), Ds=D0+Delta D1, the complete exponent is

\[
 \Lambda_{edge}=\sigma_*E+\frac{t_+E^2}{4}
 +\frac{2\pi d^3}{3a_-}+\Delta D_0+\frac{\Delta^2D_1}{2}
 +\frac{t_+}{4}\{2(E+\pi/4)D_s+D_s^2\}. \tag{3}
\]

The min/max time and rectangle endpoints cover the entire moving cutoff. The logarithmic endpoint refinement is explicitly permitted by Note 22. Equation (2) has the factor 2 for the two reflected channels; P* bounds a single channel. On C, Lambda_edge<0.003454090 and Eedge<0.004112207. The older K Z prefactor gives <0.004161480. Both are much below the opening direct signed interval transition <0.206301. Set Eedge=0 on B.

Equation (1) pays printed-jump matching first and then continues only the **fixed N=8** profile. No separate continuation of the ninth-mode analytic jump is silently omitted. Profile denominator lower bounds are positive on every actual cell. The code also verifies the formal real |p8|<21/20 range before reporting the literal historical global-profile ledger. Its removable-point algebra checks remain supplementary; no nearly singular cell is numerically divided without a valid continuation.

## 3. The decisive matched continuation comparison

Let M_R be a bound for |J8_x| on the real enclosing projection and M_C a bound for |J8_z| on the upper complex rectangle, both uniform in time. For the frozen correction, the real path from X to x has length at most R. For the analytic correction, the vertical path from x to x+iy has length at most R. Consequently,

\[
 \eta_{fr}=E_{AB}+E_{pub}+E_{edge}+K_*W_*R M_R,
\]
\[
 \eta_{an}=E_{AB}+E_{pub}+E_{edge}+K_*W_*R M_C. \tag{4}
\]

These are direct Q-residual bounds. They do not import a fixed A(X) physical theorem as though it already divided by A(z). The original historical theorem is reported separately with its fixed-center normalization and a conservative additional K when converted to Q. This larger conversion is **not** used as the strongest comparator.

The exact real set is contained in the complex set, so its exact derivative supremum is no larger. Therefore this shared one-slope ledger cannot by itself provide strict superiority for the full analytic formula when the frozen method receives equally sharp inputs. For the computed outward allowances the code separately checks the strict ordering; it does not assume that two independent interval upper bounds inherit an ordering automatically.

The [small matched record](../numerics/S02_MATCHED_CORRECTION_20261019.json) reproduces the same displayed allowances at 192/256 bits. Every table entry below is rounded upward:

| Complete Q-disk allowance | B | C |
| --- | ---: | ---: |
| Two-sum error, common | 0.014170854 | 0.015415604 |
| Corrected published residual, common | 0.209082990 | 0.206433297 |
| Analytic printed-jump matching, common | 0 | 0.004112207 |
| Frozen continuation | 0.003044488 | 0.003627210 |
| Full analytic continuation | 0.003045404 | 0.003627528 |
| Frozen total eta | **0.226298331** | **0.229588317** |
| Full total, same edge | **0.226299246** | **0.229588635** |
| Original full total | 0.226299246 | 0.431777199 |

The full/frozen ratios are below 1.000004047 and 1.000001386; their positive allowance differences are approximately 9.157174e-7 and 3.179918e-7. Thus this is a small but decisive representation choice. The crossing full/opening ratio is below 0.531729409; the substantial crossing gain restores earlier matching work and is shared by the frozen comparator.

At real centers, the frozen Q-error triples are below

\[
 B:\ (0.226298331,\ 0.452596661,\ 1.810386642),
\]
\[
 C:\ (0.229588317,\ 0.459176634,\ 1.836706533). \tag{5}
\]

These are error allowances around exact analytic approximants. Evaluation and range errors of their finite sums are not yet paid by (5); that is S02-T2. No extra source truncation or quadrature is introduced in this envelope comparison, because the imported complete arithmetic approximation already pays its omitted contributions. All scalar and profile arithmetic uses outward Arb/Acb rounding.

## 4. Physical jet and correlation handoff

With b=(log A)_x, b'=partial_x b and c=C8(t,X)/A(t,X), let r=(H-G8+C8_fr,X)/A(z). At z=X,

\[
 \frac{(H-G_8,H_x-G_{8,x},H_{xx}-G_{8,xx})}{A(X)}
 =-c(1,-k,k^2)
 +(r,r_x+br,r_{xx}+2br_x+(b^2+b')r). \tag{6}
\]

In Q coordinates the retained correction is

\[
 -c\,(1,-k-b,(k+b)^2-b'). \tag{7}
\]

The leading physical error is one common signed vector, not three freely chosen errors. The real-center grids enclose |b|<0.390946 on B and <0.390977 on C. The inverse and physical normalizer matrices must be retained when comparing to Gc units or S03 phase-scaled data.

After retaining the correction, componentwise physical residual allowances divided by A are below

\[
 B:\ (0.226298331,\ 0.541066962,\ 2.198855326),
\]
\[
 C:\ (0.229588317,\ 0.548940239,\ 2.230856812).
\]

For a correlated consumer, apply D+k **before** absolute estimation. The common vector cancels exactly, giving

\[
 \frac{(D+k)(H-G_8)}{A}=r_x+(b+k)r,
\]
\[
 \frac{(D+k)^2(H-G_8)}{A}
 =r_{xx}+2(b+k)r_x+((b+k)^2+b')r. \tag{8}
\]

The signed cancellation is material: |b+k|<0.001862 on B and <0.001829 on C, rather than the much larger |b|+k. The record bounds the actual combinations, including their second-order b' term. For the frozen method their first/second demodulated allowances are below (0.453017812,1.812071622) on B and (0.459596440,1.838386121) on C. These are bounds for different correlated observables; they are not ranked as improvements of an identical scalar component norm.

## 5. Validation, scope and decision

The [portable comparison](../numerics/compare_correction_representations.py) freshly reconstructs the opening budget and the matched budget at both precisions, pins source identities, verifies exact correction/normalizer identities and rejects changed domain/radius contracts. Series checks confirm equal correction values but distinct derivatives at X=1000,1018, verify (7), and detect the missing continuation if one wrongly identifies the printed jump with the analytic jump.

A separate reader's [192-bit replay](../numerics/S02_MATCHED_REVIEW_REPLAY_192_20261019.json) agrees. The [mechanism audit](../numerics/S02_MECHANISM_GUARD_AUDIT_20261019.json) independently checks b,b' by analytic series, mutation failures for omitted normalizer terms, the physical/demodulated chain rules and invalid domain/grid/radius choices. The [fresh controls](../numerics/S02_MATCHED_CONTROLS_20261019.json) reject five source-specific event boxes through the unchanged signed consumer and the Euler negative-Laguerre witness. They use their own errors and conservatively re-enclosed display balls, not theta constants. They test the downstream acceptance expression, not the imported theorem or a new S02 physical consumer.

The analytic family screens remain: finite-prime and finite square controls lack complete normalized reflection/coefficient data; reflected super-Gaussian and smooth positive-primitive families lack the exact unchanged theta integer-square expansion; Euler-factor families lack the unchanged level-one source data. Generic heat/counter-kernel and geometric identities do not supply the theta remainder constants. Finite-prime/smooth-primitive existence constructions have no supplied effective event box here. A valid local certificate may pass a control's collision-free domain.

[Internal Review 02](../reviews/02_MATCHED_CORRECTION_INTERNAL_REVIEW_20261019.md) classifies the result as a **matched estimating comparison with a scoped no-gain result for the full analytic first-derivative continuation ledger**. It is not a theorem about the ordering of actual approximation errors: the real-center value errors are identical because the correction values agree, and the actual derivative errors need not follow the allowance ordering. It is not universal optimality or a no-go theorem for full analytic corrections with different estimates.

S02-T1 is complete: the strongest applicable frozen comparator has been tested, its earlier edge estimate restored and a representation selected. Stop this bounded comparison without expanding the mesh. S02-T2 becomes Ready on B using disk-wise frozen centers, whole-cell finite-sum evaluation and complete return costs; C remains a separate declared stage. The single full analytic expression remains available for a consumer needing a shared analytic residual across an entire box, including the existing S03 construction. Do not propagate a family with changing frozen centers or the normalized residual by the unmodified heat equation.

No new physical lower bound, consumer margin, coverage, matched cost gain or Newman bound follows. Complete-source consumer records remain separate comparisons; this result does not claim to improve them. The global real bridge 1001<|x|<exp(2000) on the stated slab and global complex exterior stay open.

Follow the [result summaries](../../../../../../result-summaries/README.md) and [patterns to avoid](../../../../../../avoid/README.md), especially [collision screening](../../../../../../result-summaries/12_collision_controls_and_screening.md), [normalization](../../../../../../avoid/08_normalization_and_constant_slips.md), [cancellation](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [scoped conclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [target reformulations](../../../../../../avoid/01_restating_the_target.md). This milestone is judged by its explicit allowances and selection decision, not by reformulating global nonvanishing.
