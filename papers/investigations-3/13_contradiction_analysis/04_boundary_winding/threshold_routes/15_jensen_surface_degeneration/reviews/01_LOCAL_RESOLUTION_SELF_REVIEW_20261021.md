# Self-review of the opening local-resolution comparison

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6-astra (Codex)**,
reasoning effort **max**. This is a **same-assistant self-review** of
[Note 01][note] and its [implementation][code]. It is not independent
LLM review, cross-model review, or specialist human review.

## Assessment

Retain the analytic compression and local E5 estimate, the interval
zero-count certificates, and the scoped failed speed comparison. Keep
the broader investigation in reserve. The evidence does not give a
global simplicity theorem or a reason to grow the current campaign.

## Mathematical checks

1. **Normalization.** The acquired coefficient is xi^(2k)(1/2)/(2k)!,
   not gamma_k. Multiplication by b_(d,k) therefore constructs the
   prescribed F_d. The conversion is s=-z^2/4, H=f/8 and
   H_z=-z f'/16. Conventional zeta height is z/2. Near negative s,
   evaluating i sqrt(-s) avoids a false branch-cut enclosure.
2. **Full tails.** The coefficient tail uses b in [0,1] and the exact
   full value f(2R). The differentiated tail uses monotonicity of
   k(k-1)2^-k for k>=3. The bound is valid for all omitted indices,
   rather than a finite truncation check. Source acquisition is through
   the complete xi identity and rigorous special functions.
3. **Local gain.** The signed T_K''(c) is enclosed before absolute
   values. The term r T_K'''(R) controls movement across the full disk;
   the differentiated infinite tail is then added. No derivative floor
   at an unlocated or hypothetical zero is assumed.
4. **Remainder conversion.** The series coefficients used in C_R are
   f^(j)(R)/j!, giving 3 R^4 a_4 + 3 R^3 a_3 + R^2 a_2/2. These factors
   agree with the inherited E6 normalization. The positive-root formula
   for the degree is rechecked by the actual ball error inequality.
5. **Zero counts.** The polynomial comparison is against P'(c)(s-c),
   with P(c), second derivative, coefficient rounding and omitted tail
   paid. The additional E4/E5 payment transfers that count to f. A count
   of one includes multiplicity; conjugation symmetry makes the root
   real. It does not establish the global order of this zero.
6. **Surface scope.** A local full-F_d count is not global
   squarefreeness. Genus figures are conditional on the inherited RH
   premise or global squarefreeness. No full surface or period was built.

## Numerical audit

The script completes at consumer precisions 192 and 256, with central
coefficient working precisions 1024 and 1088. Both runs select degrees
203199427483 and 46031859 and certify every required positive margin.
The direct interval second-derivative upper bounds differ slightly
between precisions because interval special-function algorithms can
return different overestimates; neither the proof nor the script assumes
monotone tightening. Both complete direct margins remain positive.

The failed naive 192-bit coefficient acquisition is retained in the
record, and the guard-bit amendment is documented. The infinite-product
control's outer radius was reduced from 0.1 after an inconclusive
third-derivative enclosure; its final 0.01 disk and both split disks
certify the intended counts. The theta comparison disk never changes.

The exact quadratic control and the full infinite-product double control
pass. The latter has simple finite Jensen roots in two disjoint disks
containing no limiting zero, while its limiting function has an exact
double at -1. This is the required false-simplicity screen.

The measured refinement/direct ratios, 17.2 and 38.5, fail the declared
<=0.5 gate. Timings include all per-method mathematical acquisitions;
imports are common and excluded. One execution per precision supports
only an observed result for this implementation. Reused coefficients,
shorter prefixes, different working precision, or another acquisition
algorithm have not been compared. No universal lower bound is asserted.

## Status and remaining work

The bounds are proved in-note and the stated finite inequalities are
interval-certified, subject to the numerical library and implementation
as trusted inputs. There is no independent verification of that software
stack. Repeating precision is an internal consistency check, not independent
validation. The formal all-multiplicity problem, hypothetical theta
double/triple cluster constants, periods, arithmetic separation and global
HMC gates remain unresolved.

The existing [control register][controls] and the warnings on
[same-model review][a05] and [scope][a07] govern interpretation. This
research round is not a manuscript milestone or a portfolio closure.

[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[code]: ../numerics/check_local_jensen_resolution.py
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[note]: ../notes/01_LOCAL_RESOLUTION_AND_COMPLETE_COST_COMPARISON_20261021.md
