# S03-T3: calibrated first jet versus matched direct certification

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**, verified from session metadata. Separate delegated
same-model mathematical, code and control reviews; no specialist human
review.

**Outcome.** S03-T3 is complete as a bounded consumer comparison. The
calibrated pointwise first-jet radius is **`>1.3859351576`**, versus
**`>1.1288659652`** for calibrated scalar transport and
**`>1.3898732635`** for the matched complete-source direct test. The
source test remains stronger. The calibration's already proved complete
first-jet error `<0.000266449` is implemented with its 26 exact dyadic
anchor coefficients and anchor uncertainty paid once. No new residual
allowance or arithmetic cancellation theorem is claimed.

The source direct test also receives the same midpoint propagation as the
calibrated test. Its raw-cell baseline reproduces `>1.3473946960`; claiming
calibration superiority against only that weaker implementation would be
misleading. The stronger source certificate is an implementation refinement
on the already covered B box. This comparison supplies no new region,
complex-domain certificate, second-jet error or matched-cost advantage.
Stop this fixed-box scalar/calibration comparison and retain its reusable
anchor export, evaluator and scoped direction-loss theorem.

The repository [result summaries][summaries] and [patterns to avoid][avoid]
were read, especially [theta bookkeeping][theta], [collision controls][controls],
[reformulations][a01], [scoped exclusions][a07], [normalization][a08] and
[preserving cancellation][a12]. Classification: **complete known-box
interval consumer comparison and a proved scoped scalar/vector inequality**.
The [comparison contract][contract] fixes the primary metric, source data
and cover. A positive old-box radius is validation, not new coverage.

## Fixed domain and information classes

Keep B=`[1/100,1/5] x [999,1001]`, anchor `a=999`, and the same 32 closed
time slabs by 128 closed spatial cells. Write `Q=H/A`, `b=(log A)_x`,
`omega=theta_x<0` and `f=(G_8-Chat_8)/A`, using S02's coherent **full**
analytic family. All modes 1–8 and full profile derivatives remain present;
no center-varying frozen family or jumping cutoff is differentiated.

Use the real phase-scaled jet `W_h=h-i h_x/omega`, with
`Z_h=e^(-i theta) W_h`. Its norm equals the Euclidean norm of
`J_h=(h,-h_x/omega)`. The primary metric is a complete uniform lower
certificate for `|J_Q|` on B. It is not physical energy; physical return
is described below.

Two information classes are kept separate:

1. **Analytic-only:** the full S02 disk residual envelope, explicit phase
   and [S03-T2's complete increment allowance][t2]. The latter is not an
   anchor estimate. No complete-source coefficients are assigned to this
   class.
2. **Source-informed:** exactly the 192-bit complete-source setup used by
   [S03 Note 02][n02], its validated physical tails/majorant and exact
   dyadics, plus its complete correlated residual/anchor theorem. The
   direct source comparator uses the same physical-source data. Both
   192/256-bit consumer runs replay these same inputs; neither acquires
   an extra 256-bit source quadrature.

The original setup is available and matches Note 02's stored SHA-256.
The [anchor export][anchors] also records a canonical mathematical-setup
hash, retaining every mathematical setup field and excluding observational
seconds/callback counts. Later external regenerated inputs must pass source
validation and match that mathematical hash before any cell is evaluated.
The producer validates the original correlated, opening S03 and S02
producer/record pins. It rechecks the exported coefficients, complete
error ledger, every slab allowance, domain and analytic-only increment
against their pinned originals. No changed data are silently substituted.

## Exact anchor calibration and its complete error

Let `G*=1000^(7/4) exp(-125 pi)`, `chi=G*/A`, `tc=21/200`.
The retained exact dyadic time polynomials `p0,p1` have 13 coefficients
each, in ascending powers of `t-tc`. They represent the nominal physical
residual value and physical x derivative at the anchor, divided by G*.
They are exported unchanged from Note 02, not refitted in this task.
Define

\[
 a_0=\chi(t,a)p_0(t),\qquad
 a_1=\chi(t,a)\{p_1(t)-b(t,a)p_0(t)\},\quad
 \psi=\theta(t,x)-\theta(t,a),
\]
\[
 g=a_0\cos\psi+\frac{a_1}{\omega(t,a)}\sin\psi,
 \qquad \widetilde f=f+g.                                \tag{1}
\]

Here `a1` is the normalized residual derivative. The `-b p0` term and
the signed anchor omega are essential. Exact integer/exponent dyadics
are decoded outward without a floating-point conversion or replacement
by runtime midpoints. Large exponent gaps may give a small interval width
at working precision; that evaluation width stays in the interval image.
It is distinct from the physical-to-nominal-anchor uncertainty.

Direct differentiation at fixed t proves

\[
 W_g=e^{i\psi}(a_0-i a_1/\omega_a),\quad
 Z_g=e^{-i\theta_a}(a_0-i a_1/\omega_a)=c(t),
\]
\[
 g_{xx}=-\omega^2g+(\omega_x/\omega)g_x,\quad
 \mathscr R_g=g+g_{xx}/\omega^2-\omega_xg_x/\omega^3=0.
                                                               \tag{2}
\]

For `r=Q-f`, the exact primitive gives
`Z_r(x)=Z_r(a)-i I_r(x)`. If the retained proof supplies
`|Z_r(a)-c|<=epsilon_a` and `|I_r(x)|<=B_r`, then

\[
       |J_Q-J_{\widetilde f}|
       =|Z_r(x)-c|\le\epsilon_a+B_r.                    \tag{3}
\]

The [new record][record] retains per-time-slab payments; globally
`epsilon_a<6.025073e-10` and `epsilon_a+B_r<0.000266449`.
The anchor error appears once. The actual residual anchor is not zero.
The complete increment already includes source quadrature, source and
arithmetic Taylor tails, omitted square modes, retained-source U tails,
normalizer/phase variation and signed partial-cell prefix costs from
Note 02. They are inherited, not dropped or charged a second time.

Equation (3) is a **real first-jet** bound. Equation (2) specifies the
nominal g second derivative for cell propagation, but supplies no new
second-jet error for Q minus the calibrated approximant. It also supplies
no complex-disk extension. Neither normalized residual nor g is assumed
to obey the unmodified physical heat equation.

## Exact comparison with scalar transport

At one fixed t let
`D_a=Z_f(a)+c` and `Delta_f(x)=Z_f(x)-Z_f(a)`. The calibrated nominal
vector is `D_x=D_a+Delta_f`. Using the same anchor ball and increment
allowance, scalar transport pays

\[
 L_{\rm scalar}=|D_a|-|\Delta_f|-\epsilon_a-B_r,
 \qquad
 L_{\rm vector}=|D_a+\Delta_f|-\epsilon_a-B_r.
\]

Triangle inequality proves

\[
                       L_{\rm scalar}\le L_{\rm vector}. \tag{4}
\]

This concerns exactly these vectors and error envelopes. It does not
assert that every interval implementation or every evaluation cost is
ordered. If a separate source anchor is stronger, its full vector/shape
information must be preserved in a fair comparison; one cannot replace
it by the weaker nominal ball and then claim domination. For a common
anchor set K and error set E, directly bounding
`dist(0,K+Delta_f+E)` retains at least the information used by its scalar
triangle lower bound. Costs or different correlated estimators are outside
this scoped inequality.

Since `I_g=0`, calibration does not remove `I_f` from scalar transport.
Its main gain is retaining the vector direction pointwise. The code
evaluates the full signed primitive with the exactly canceled n=1
constant removed before subtraction, and pays its closed-cell variation.

## Shared cell propagation and the strongest direct baseline

For any real twice differentiable q,

\[
 (W_q)_x=q_x-i\{q_{xx}/\omega-q_x\omega_x/\omega^2\}.
                                                               \tag{5}
\]

If a closed spatial cell has midpoint m and half-width h, then

\[
 |W_q(x)|\ge |W_q(m)|-h\sup_{\rm cell}|(W_q)_x|.           \tag{6}
\]

Time is an interval parameter throughout. Every method receives the
better of its raw whole-cell rectangle norm and (6). For the derivative,
the code takes the better of direct (5) and the established generic
`|omega|(|W_q|+|R_q|)` bound. For calibrated q, use
`(W_tilde f)_x=(W_f)_x+i omega W_g` and `R_tilde f=R_f`.
Both identities are exact. Specialized rectangle modulus lower/upper
bounds are used consistently for all complex vectors.

For the source comparator, the source evaluator returns **complete**
physical derivative balls `V_j=H^(j)/G*`, j=0,1,2. Convert by

\[
 Q=\chi V_0,\quad Q_x=\chi(V_1-bV_0),\quad
 Q_{xx}=\chi\{V_2-2bV_1+(b^2-b_x)V_0\}.                  \tag{7}
\]

Use (5)–(6) on these complete balls. Their source error is already paid;
subtracting the separately displayed diagnostic error again would double
count it. Derivative balls need only enclose derivatives of the actual H;
no assumption that three independently truncated source polynomials are
one consistent polynomial is made here. No unavailable derivative above
the source evaluator's established orders is introduced.

## Complete comparison ledger and interpretation

Both 192/256-bit runs certify the following common weak round bounds.
Positive lower bounds exclude a common real physical zero on the old
box. A negative lower certificate is inconclusive.

| Information and consumer | Uniform paid J-radius lower bound |
| --- | ---: |
| Analytic-only full direct, matched cell propagation | `>0.9725295603` |
| Analytic-only scalar using S03-T2 allowance | Inconclusive: computed lower bound about `-0.096725` |
| Source-informed full direct, uncalibrated residual-radius payment | `>1.3850484689` |
| Source-informed scalar, uncalibrated anchor | `>1.1280710163` |
| Source-informed scalar, calibrated anchor | **`>1.1288659652`** |
| Source-informed calibrated pointwise first jet | **`>1.3859351576`** |
| Same complete-source direct, raw cell image | `>1.3473946960` |
| Same complete-source direct, matched propagation | **`>1.3898732635`** |

The source direct certificate exceeds the calibrated certificate by about
0.003938 in the reported lower allowances. This compares specified
certificates, not exact worst-case norms. The raw source row reproduces
the [S02-T2 reference][s02]. Source inputs, cover, physical normalization
and source errors are the same across the source-informed rows. All finite
formula evaluation/range errors are in the interval images; the residual
errors in (3) or the relevant uncalibrated/analytic envelope are subtracted
once. No cover or precision search selects the ordering.

The maximum complete calibrated approximation error remains
`<0.000266449` in J units. The source approximation's first-jet error
diagnostic is `<2.348122e-10` on the same cells. These are distinct from
cell range widths. Calibration compresses source information into two
anchor time polynomials plus an increment allowance, but this computation
does not show it to be a better full-error representation than the source
model that supplied those data.

For physical return,

\[
 (H,H_x)/A=TJ_Q,\quad T=\begin{pmatrix}1&0\\b&-\omega\end{pmatrix},
 \quad \|T\|\le\sqrt{1+b^2+\omega^2},\quad
 \sigma_{\min}(T)\ge\frac{|\omega|}{\sqrt{1+b^2+\omega^2}}.
\]

The per-slab return in the record gives calibrated complete physical
value/derivative error divided by A `<0.000408512`. A positive J radius
excludes a physical common zero because T is invertible; none of these
normalized radii is being reported as E or L0.

## Acquisition, work and reproducibility

The shared 192-bit source acquisition used 173,696 quadrature callbacks,
with its original observed setup time about 9.10 seconds. Calibration
additionally required Note 02's mixed coefficient subtraction, its 256-cell
complex-polydisk majorant, complete 4096-cell residual-prefix calculation
and exact anchor construction; its retained post-source observation was
about 1.25 seconds. These are descriptive historical observations, not
current matched benchmarks or a speed result.

The new comparison loads that exact setup, with no new source quadrature.
Per precision it evaluates 4096 source cells and their 4096 midpoints,
8224 full analytic jets and 8224 stable primitives, including 32 anchors.
Actual consumer times are in the record. These counts describe the joint
comparison implementation, not optimized standalone route costs. Higher
precision replays the same source and anchor theorem. A cost milestone
was not selected and the factor-two cost gate is not tested.

The [numerical guide][numeric] gives export, consumer replay, external
source regeneration and fail-closed identity checks. Only the code, 26
anchor dyadics and small 32-slab records are saved in Git. The complete
source cache remains external. No new large cell archive or manuscript
snapshot is created.

## Controls, review and stopping decision

The [new controls][controlrecord] challenge the actual radius/propagation/
normalization helpers with own-data heat-event and oscillator cases,
nonzero anchor uncertainty, exact dyadic decoding, normalization derivatives,
and altered-input contracts. The constant-ball fixture tests source-payment
bookkeeping; it is not theta data or an event certificate.
Fresh source-specific event data test the
new first-jet helper; Euler's negative-Laguerre witness screens the inherited
sign consumer, not a false demand that a nonzero Euler first jet vanish.
Theta error constants are never transferred to a control.

The analytic premise screen remains explicit: finite-prime/weighted-square
families lack full normalized unchanged theta reflection/coefficient data;
reflected/shape/primitive controls lack the unchanged integer-square source;
Euler factors alter level-one data; polynomial/counter-kernel events lack
the theta source. Generic calibration/rotation identities do not distinguish
theta and supply no global sign. At a genuine event a correctly paid strict
first-jet consumer must reject.

A separate same-model reader [checks the proof, code and 192-bit replay][review].
The final replay agrees in every mathematical run field; observed time is
not an arithmetic identity. 192/256-bit lower certificates can differ
slightly because they are computed lower bounds, not enclosures of one
unique optimizing number.

**S03-T3 Complete.** Calibration has a faithful executable finite first-jet
interface and the scalar direction loss is quantified, but the strongest
same-data direct reference wins. Retain this analytic information and the
stronger direct baseline; stop further tuning of this fixed-box comparison.
EXT-01 remains conditional without a selected new-domain bottleneck and
earned extension. G3's independent arithmetic residual mechanism, S04's
height-uniform input, the real bridge `(1001,exp(2000))` and global complex
exterior remain open. Completion does not assert that other transport
estimates or cost regimes cannot be useful.

[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[contract]: ../../notes/04_S03_CALIBRATED_CONSUMER_COMPARISON_CONTRACT_20261019.md
[n02]: 02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md
[t2]: 04_PHASE_AWARE_ANALYTIC_ALLOWANCE_AND_KERNEL_VARIATION_OBSTRUCTION_20261019.md
[s02]: ../../02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md
[anchors]: ../numerics/S03_T3_ANCHOR_EXPORT_20261019.json
[record]: ../numerics/S03_CALIBRATED_CONSUMERS_20261019.json
[numeric]: ../numerics/README.md
[controlrecord]: ../numerics/S03_T3_CONTROLS_20261019.json
[review]: ../reviews/05_CALIBRATED_CONSUMER_COMPARISON_INTERNAL_REVIEW_20261019.md
