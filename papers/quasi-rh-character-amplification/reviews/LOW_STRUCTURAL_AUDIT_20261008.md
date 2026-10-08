# Source audit of the compensated low estimate and variable geometry

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and configured reasoning effort are not exposed and are not inferred.

## Status and scope

This is an adversarial, source-level audit of the parameter transfer through the low side of the September 30 quasi-RH paper. I inspected the actual source text of Sections 6.1, 12, 14.1–14.4, 15, and the slot-choice discussion in Section 20.6, with particular attention to equations (6.2), (12.5), (14.11)–(14.16), and (15.1)–(15.8). The source PDF SHA-256 supplied with this investigation is `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.

Source: [September 30 paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf). The source PDF and extracted text remain outside the repository.

The conclusions below are conditional on the source reflection and hybrid norm machinery. They validate the applicability and exponent algebra of the low-side transfer; they do not independently prove the cubic-theta reflection, replay Lean, validate the high estimate, or establish a new zero-free theorem. No parameter-transfer gap was found in the reviewed low-side steps. In particular, the source does not require the numerical choice b=1/8 in the additive Gram estimate or the physical finite probe.

## 1. Coefficient and support audit

The physical expression remains source (12.5), with original prime-slot windows held at their original scales in every subset summand. For a fixed rescaled subset J, the rescaled tuple is frozen before applying row estimates. It changes only X', Y', and the row-ball size Q; it does not become a moving coefficient in the completed-row Hilbert space. The surviving marked slot factors are products of individual bounded coefficients, independent of the row and of the dual variables.

The exact separation (6.2) is stated for independent positive X, Y, Z. Its factor Q^{-1/2}, additive row, completed row, common finite ray decomposition, and annular row cutoff therefore survive the geometry change. The factor of absolute value one depending on the row norm can be discarded in Cauchy–Schwarz, and the fixed zero mask can be removed only inside the resulting positive sum, exactly as in the source.

For Lemma 14.3, the low application has f=1 and puncture rho=1. All non-slot moving primes belong to the row; those in A_0 occur in the powerful row part, so 2A_0 <= O up to fixed logarithmic offsets. The actual residual-row annulus must be retained until the common-profile kernel amplitude is extracted. The source expressly does this before positive row enlargement; changing the log-lengths does not authorize re-evaluating the kernel at the artificially added shorter rows.

The fixed-row restrictions remain independent of surviving active slots and dual variables, except for the explicit collision mask already handled by Lemma 14.2. The slot system stays disjoint before ray and excluded-set restrictions. No canceled local character zero, extra prime mask, or arbitrary residual coefficient has been introduced.

Lemma 14.3 is uniform for log-lengths in fixed bounded ranges. Thus none of its stated geometric premises singles out M=5/6, ell=1/6, or b=1/8. Its source proof is still an external dependency; this audit does not replace that proof.

## 2. The previous one-parameter perturbation

Keep ell=1/6, b=1/8 and set

    h=13/16+r, lx=17/48-r, ly=23/48-r, M=5/6-2r.

For a rescaled subset of total length d in [0,ell], write M'=M-2d and ell'=ell-d. The source's actual-row calculation on p.103 gives

    T_d <= H-3d-2r + small losses,

because M'+ell'-1=-3d-2r. Hence its comparison max(H,v+ell_b)=H+small losses continues to hold for r>=0. The unspecialized identity (15.3), rather than its baseline numerical specialization, gives

    sum_m |B_m^J|^2 << Z^[M' + (d-1/6+4r)_+/4 + epsilon].

The additive Gram estimate (15.4) still applies, since P_a=q_{b_*}^{-1}Z^b and the required dominance P_a^2/Y' << P_a^(1/6) holds when

    ly-ell-11b/6 = 1/12-r >= 0.

The tuple count, physical coefficient, and square root of X' give the exact factor Z^{-d} from source (15.8). Therefore the remaining exponent is

    f_r(d) = -d + (d-1/6+4r)_+/8.

This function is continuous and decreasing in d: its slopes are -1 and -7/8. Consequently its maximum is at d=0, yielding the full low-side envelope

    L(r) = 3/16-r/2 + (4r-1/6)_+/8,     0 <= r <= 1/12.

At the upper endpoint the Gram dominance uses a fixed implied constant rather than a positive exponent gap; a strict range r<1/12 is convenient if later choices require an open region. All residual X', Y', and row lengths stay positive throughout this stated range.

For 0<=r<=1/24, the positive-part correction vanishes, recovering the clean low estimate in the existing parameter-extension note. For r>=1/24, L(r)=1/6. Coupled only to the exact principal signal C_r(s)=s-11/16-r/3, this particular low certificate gives the boundary

    sigma_low(r) = 7/8-r/6                  for 0<=r<=1/24,
                 = 41/48+r/3               for 1/24<=r<=1/12.

Its minimum is 125/144 at r=1/24. This is a minimum of this coarse displayed-estimate certificate, not an intrinsic barrier and not a statement that the high estimate or contour domains reach it. It does prove that the low side places no obstacle to increasing the previously chosen r=1/100000 while remaining below 1/24.

## 3. A broader two-parameter geometry

A more useful family preserves the source identity M+ell=1 exactly. Take positive ell,b and define

    lx=(1-ell-b)/2,   ly=(1-ell+b)/2,
    M=1-ell,          h=(1+3ell+b)/2.

Then ly-lx=b and h=1-lx+ell, so the high-side scale identity is preserved. Sufficient low-side conditions are

    0 < ell < 1/3,
    0 < b <= 3(1-3ell)/8.

The source geometry is one member of this region. There is no lower bound on a fixed positive b in the Gram proof. A small b can increase the target-dependent threshold required for P_a>=1, since that condition is Z>=q_{b_*}^{1/b}; this is compatible with the source's allowed quantifiers. This observation does not cover b=0, where its stated P_a>=1 hypothesis need not hold.

For any rescaled subset,

    M'=1-ell-2d,   ell'=ell-d,   0<=d<=ell,
    M'+ell'-1=-3d,
    1+3ell'-2M'=5ell-1+d.

Thus the actual-row dual comparison on p.103 is literally the same as in the source, and the two branches obtained from (15.3) give

    sum_m |B_m^J|^2 << Z^[M'+(5ell-1+d)_+/4+epsilon].

The required positive scales satisfy

    M' >= 1-3ell > 0,
    lx-d >= (1-3ell-b)/2 > 0,
    ly-d >= (1-3ell+b)/2 > 0.

The last source condition used to absorb the third Gram term becomes

    ly-d-11b/6 >= (1-3ell)/2-4b/3 >= 0.

This is exactly the displayed sufficient upper bound on b. Since P_a=q_{b_*}^{-1}Z^b, no numerical replacement for b=1/8 is otherwise needed in (15.4) or its proof. All scales stay in fixed polynomial ranges in Z.

Combining the Gram estimate with the completed-row estimate and source (15.8), the subset contribution has excess

    f(d)=-d+(5ell-1+d)_+/8.

Again f is decreasing. The resulting low exponent is therefore

    L(ell,b) = lx/2+b/12+(5ell-1)_+/8
             = (1-ell)/4-b/6+(5ell-1)_+/8.

In particular, for ell<=1/5 the original clean form lx/2+b/12 remains valid. It is not necessary that ell=1/6.

The exact principal affine exponent simplifies to

    C(s)=s+lx/2-1+h/6=s-2/3-b/6.

The associated low-side boundary is

    sigma_low(ell)=11/12-ell/4+(5ell-1)_+/8.

It is independent of b. It decreases to 13/15 at ell=1/5 and increases thereafter as 19/24+3ell/8. This is a statement about the low-side certificate alone. It neither proves the high estimate at 13/15 nor licenses reusing Euler domains whose left endpoint is larger.

## 4. Concrete examples and prime supply

At ell=1/6, b=1/16:

    lx=37/96, ly=43/96, h=25/32, M=5/6,
    lx-ell=7/32, ly-ell=9/32,
    ly-ell-11b/6=1/6.

Thus halving b has ample low-side slack. It keeps the boundary at 7/8 while changing the high-side row scale and scalar exponents.

At ell=1/5, b=1/16:

    lx=59/160, ly=69/160, h=133/160, M=4/5,
    lx-ell=27/160, ly-ell=37/160,
    ly-ell-11b/6=7/60.

Again there is ample Gram and residual-length slack; the low certificate alone reaches 13/15.

The moment prime-supply condition is separate from the low proof. If the inherited sufficient threshold remains ell/(h+zeta)>7/37, its strict zeta=0 form in this family is

    53ell > 7(1+b).

For either example above the inequality has positive slack, so some fixed zeta>0 is allowed. The source chooses a sufficiently fine fixed even slot count K and disjoint annular windows. Its construction applies to any fixed positive ell with a positive supply gap. Width decrements, mesh, and real losses must still be chosen before the target. The internal centered-amplifier pool separation is a mesh condition in the selected row base; it does not require b=1/8.

This supply calculation does not independently validate the inverse or fourth-moment capacity bounds. Those bounds and any different supply demand from the optimized high argument remain to be checked there.

## 5. Boundaries of the conclusion

The following would invalidate a broader claim and have not been silently assumed:

- Reusing numerical specializations of (15.2), (15.3), or (15.7) without replacing them by the formulas above.
- Treating the good-prime product or principal multiplier as already controlled below its published Euler region.
- Assuming the high estimate, witness count, small-row estimate, or continuation theorem is automatically stable throughout the low-admissible region.
- Changing the marked expression, independent coefficient class, or physical slot windows while retaining these estimates.
- Interchanging the fixed real choices with target-dependent heights and arithmetic lower thresholds.

The immediate useful improvement is therefore to optimize ell and b within this explicitly source-audited low region and then independently certify every high and contour inequality. The low proof does not force the previously chosen b=1/8 or ell=1/6.

## 6. Assessment of the selected candidate

The selected candidate is

    ell=1001/6000, b=1/8,
    lx=4249/12000, ly=5749/12000,
    h=3251/4000, M=4999/6000.

It satisfies all of the sufficient low-side conditions above, with exact margins

    M-2ell = 999/2000,
    lx-ell = 749/4000,
    ly-ell = 1249/4000,
    ly-ell-11b/6 = 997/12000,
    1/5-ell = 199/6000.

The complete subset calculation is necessary: for this ell, the source's old specialized assertion `sum |B_m^J|^2 << Z^(M'+epsilon)` does not follow uniformly from its two displayed energy branches. The general bound is instead

    sum |B_m^J|^2 << Z^[M'+(d-199/1200)_+/4+epsilon].

Its possible excess is harmless after the actual tuple factor is restored:

    f(d)=-d+(d-199/1200)_+/8 <= 0,  0<=d<=1001/6000.

The source notes that the endpoint with no surviving marked slots has a sharper first-branch bound, but that refinement is not needed here. The displayed positive-part estimate and the monotonicity of f already cover every subset, including a slot system with arbitrarily fine fixed mesh.

Thus the clean low exponent is

    L=lx/2+b/12=4499/24000.

The principal affine exponent remains exactly C(s)=s-11/16 because b is unchanged and M+ell=1. Its equality with this low exponent occurs at

    sigma=20999/24000=7/8-1/24000.

Finally, the strict prime-supply inequality has margin

    53ell-7(1+b)=5803/6000 > 0.

Equivalently, ell/h-7/37=5803/360861>0. A sufficiently small fixed positive frequency extension therefore retains that inherited supply threshold. (This last ratio is only a supply check; the root investigation separately audits the high moment and contour requirements.)

**Low-side verdict for the selected candidate:** the source-scoped transfer passes, conditional on the imported Lemma 14.3, Gram/Poisson machinery, and coefficient conventions stated above. In particular, the derived boundary 20999/24000 is not ruled out by the low argument. This audit alone does not establish it as a zero-free theorem.
