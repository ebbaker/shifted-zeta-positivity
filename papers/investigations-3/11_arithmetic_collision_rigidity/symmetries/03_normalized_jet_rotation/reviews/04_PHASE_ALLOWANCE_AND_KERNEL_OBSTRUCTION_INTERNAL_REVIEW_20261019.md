# S03-T2 internal adversarial review

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**, inherited from the parent research session. Separate
delegated same-model audit and fresh replay; this is not independent
specialist human review.

**Assessment.** The phase-aware analytic-only allowance and the supplementary
absolute-kernel-variation obstruction are mathematically sound in their
stated classes. Fresh 192-bit runs reproduce the main allowance
`0.81225936960969203517623561120287517272` and the one-cell assigned
midpoint variation payment lower bound `4037.451363978925115445836183698233...`.
There is no new arithmetic cancellation estimate, source-informed residual
improvement, physical sign, coverage, or Newman bound.

## Scope and comparison gate

I read the repository instructions, result-summary and avoid entry points,
the overview's S03-T2 requirement, the current tracker, S03 Notes 01 and 03,
the final [S03-T2 Note 04][note], the imported S02 full analytic evaluator,
and both new checkers. The final note's claims were checked against the
written derivations and latest replay outputs. The relevant
standing cautions are [reformulations][a1], [controls][controls],
[same-model review][a5], [scoped exclusions][a7], and
[preserving cancellation][a12]. This is a bounded estimate judged by its
number, together with a failure theorem for an explicitly prescribed payment
rule. It is not a reformulation proposed as evidence for RH.

The overview expressly allows a reusable analytic-only estimate to pass the
same-information gate without beating source-informed values. On that
basis S03-T2 may be recorded complete for this declared analytic-only branch
and precise failed-estimate deliverable. The independent arithmetic-source
cancellation obligation stays open. S03-T3 may assess the consumer value;
this review does not authorize an extension from the known B box.

## Independent derivation of the complete allowance

For a real-symmetric holomorphic residual on a radius-rho disk,
Schwarz-Pick gives `rho |r_x|/eta <= 1-(r/eta)^2`. Hence the normalized
real first jet lies in the ellipse with semiaxes `eta` and `eta K`, where
`K=max(1,1/(rho w_-))`. This follows since
`a^2+(1-a^2)^2<=1` for `|a|<=1`; it does not assume independent residual
value and derivative extremizers.

At phase separation delta, the support of the difference of the two
rotated ellipses is at most

    eta sqrt(2(1+K^2+(K^2-1)|cos(delta)|)).

Indeed, for a unit direction e, the two ellipse support squares sum to at
most `1+K^2+(K^2-1)|cos(delta)|`; Cauchy bounds the sum of their square
roots. Both endpoint phases are the prescribed explicit phase. The absolute
cosine is essential once delta exceeds pi/2.

The exact primitive makes the residual increment equal in modulus to the
endpoint difference. For small delta, the complete Cauchy defect bound is
`eta D delta`, with

    D=1+2/(rho^2 w_-^2)+w'_+/(rho w_-^3).

Splitting at delta=23/50 therefore pays every prefix: the near branch pays
all smaller separations, while the far support bound is valid through
`delta_max<=2w_+<pi-23/50`. No numerical integration, complete-source jet,
old residual polynomial, or unproved residual heat equation is used.
The imported complete eta pays the entire residual; it must not be added
again as a source tail. The phase cover is closed in both parameters.

The fresh replay returns near payment `<0.800041`, far payment
`<0.812260`, and independent endpoint payment `<0.827470`. The paid ratio
is `<0.981619`, a reduction greater than `1.83812%` in this information
class. The retained source-informed allowances `<0.002011747` and
`<0.000266448` remain substantially stronger and unchanged.

For `r=1/5`, the complete endpoint increment is
`(2/5)|sin((theta(1001)-theta(999))/2)|`. The certified phase bounds put the
half separation in `[w_-,w_+]` below pi/2, so its uniform lower bound is
`(2/5)sin(w_-)>0.3553758`. This is a valid limitation of the disk-envelope
class only: the constant residual is not asserted to satisfy the exact
source or its prescribed heat forcing.

## Supplementary variation obstruction

The auxiliary checker independently differentiates the normalizer and phase
at `t=21/200,x=1000`, holding the source contour fixed. I verified the
product-rule multiplier

    B=(i zeta-b-i omega-mu)Gamma+Gamma_x,
    Gamma_x=-2 b_x(i zeta-b)-b_xx-mu_x(i zeta-b)
            +mu b_x+2 omega omega_x.

The reverse triangle lower bound for the first theta square and upper
bounds for squares 2 through 11 give a strictly positive retained source
modulus on the whole u interval `[59/100,3/5]`. Its exponential scale is
computed in modulus, preserving the factor `1/2` in the two shifted
channels. The point lies on a boundary of the declared closed spatial and
time cells, so it bounds from below the supremum used by the payment rule.
No point sample is promoted into a uniform residual estimate.

For a rule that separately pays the absolute spatial derivative of each
shifted source channel inside the u integral, even one width-1/64 cell's
assigned midpoint Lipschitz radius is `>4037.45136`. This is an obstruction
to that prescribed nonnegative variation budget even if the zero-order
source/arithmetic discrepancy was retained signed. It is not a lower bound
on the actual quadrature error, combined signed derivative, residual, or
all possible quadrature methods. Other tails and payments are nonnegative
in that class and cannot repair the failure; they are not set to zero.

## Verification and adversarial controls

Both latest 192-bit runs completed successfully, after the generic K
calculation was made outward safe and script/source provenance pins were
added to the kernel record. Every 192-bit mathematical record field and
producer/source hash agrees exactly with the corresponding authoring run. The analytic allowance
checker freshly evaluates the 4096 closed phase cells and verifies the
inherited matched S02 source pins. The replay agrees with the authoring
record's mathematical values; precision agreement alone is not evidence
for the theorem.

The polynomial collision uses its own disk allowance 5, actual endpoint
identity `|I_r|=sqrt(5)`, exact physical-anchor equality, and the actual new
helper's strict rejection. Three oscillator checks confirm only the generic
identity. The missing-absolute-cosine mutation has an explicit ellipse
witness; the long-phase fallback, zero residual and six invalid inputs are
also exercised. These are meaningful mechanism tests rather than new
source acceptance tests. The existing source-specific controls remain
relevant to inherited consumers. No new strict theta sign interface was
introduced.

No mathematical blocking finding remains. Any public classification must
keep the arithmetic obligation open, retain the strongest source-informed
comparators, identify the same-model status, and leave the existing real
bridge and global complex exterior gaps unchanged.

[note]: ../notes/04_PHASE_AWARE_ANALYTIC_ALLOWANCE_AND_KERNEL_VARIATION_OBSTRUCTION_20261019.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a1]: ../../../../../../avoid/01_restating_the_target.md
[a5]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a7]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
