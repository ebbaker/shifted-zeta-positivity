# VCD-GT-E03 r4 B — the matched whole-interval gap minimum

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, chat0003. Fixed proof support was dispatched
**gpt-6.1-sol / ultra**. Separate backend attestation and actual lead
settings are unavailable.

**Proved in-note from the existing certified inputs for one fixed tube.**
This is the quantitative postprocessing test in [B06 Decision06 §B][decision]
and the [frozen E03 r4 request][request]. It uses the complete physical
theta field, \(H_0(z)=\xi((1+iz)/2)/8\) and \(\partial_tH=-\partial_z^2H\).
[Result index][results] · [Avoid index][avoid] · [Classification][classification]

## 1. The minimum is at the direct endpoint

Use the count-two tube centered at \(a=140101/10\) with contour radius
\(9/10\), on \(I=[0,1/10]\). The paid geometry puts both zeros in
\(|z-a|<3/4\) throughout \(I\). The unordered pair is conjugation
invariant, so \(D=((z_1-z_2)/2)^2\) is real. In particular
\(D\le |D|\le9/16\) by the triangle inequality. The actual drift
enclosure \([-0.615518848,-0.599329616]\) implies \(-5/8\le K\le0\).
The physical identity \(D'=2+4KD\) holds through a double zero.
[Note12 §5][oracle] · [Note15][certificate] · [Assessment08][assessment]

On \(D\ge0\) the identity gives
\[
 D'\ge 2-\frac52D\ge 2-\frac52\frac9{16}=\frac{19}{32}.
\]
On \(D<0\), the nonpositive \(K\) gives \(D'\ge2\). Hence for every
\(t\in I\), \(D(t)\ge D(0)+19t/32\), with no assumption of positivity in
the derivative estimate. The minimum equals \(D(0)\). Its already
certified direct enclosure is
\[
 \boxed{\displaystyle
  \min_{t\in I} D(t)\in
   [0.00142117117778,\ 0.00142118228384].}
\]
The lower endpoint also gives the corresponding affine lower envelope
on \(I\). The proof uses the shared \(K\) band, root radius and existing
endpoint row. No numerical acquisition or replay was performed.
[Note15][certificate] · [Pinned record][record]

## 2. Forward and backward comparison

On any paid real counted tube \([u,v]\) with the same physical gap law,
write \(W_k(x,y)=\exp(4\int_x^y k(s)\,ds)\) for an integrable real \(k\).
The integrating factor gives the exact identities
\[
 \begin{aligned}
 D(t)&=W_K(u,t)D(u)+2\int_u^t W_K(s,t)\,ds,\\
 D(t)&=\frac{D(v)-2\int_t^v W_K(s,v)\,ds}{W_K(t,v)}.
 \end{aligned}
\]
If \(k_-\le K\) and \(0\le L_u\le D(u)\), the first identity gives the
lower envelope
\[
 F_-(t)=W_{k_-}(u,t)L_u+2\int_u^t W_{k_-}(s,t)\,ds .
\]
If \(K\le k_+\) and \(L_v\le D(v)\), put
\(N_+(t)=L_v-2\int_t^v W_{k_+}(s,v)\,ds\). Wherever \(N_+(t)\ge0\),
\[
 D(t)\ge B_+(t)=\frac{N_+(t)}{W_{k_+}(t,v)} .
\]
The actual numerator is at least \(N_+(t)\) and its positive
denominator is at most \(W_{k_+}(t,v)\). If \(N_+(t)<0\), a two-sided
drift band gives the lower bound \(N_+(t)/W_{k_-}(t,v)\), since a
negative lower numerator needs a positive **lower** denominator.

Using \(W_{k_+}\) for that negative numerator can fail. As a scalar
sign check take \(D(0)=1\), \(K=0\) on \([-1,0]\), and \(K=-1/4\)
on \([-2,-1)\). Then \(D(-1)=-1\) and \(D(-2)=2-3e<-3\), whereas
using \(k_+=0\) in both numerator and denominator yields \(-3\).
This example concerns only the scalar equation.

One can also propagate through either sign with both bounds. With
\(y_+=\max(y,0)\) and \(y_-=\min(y,0)\), the lower comparison field
is \(2+4(k_-y_++k_+y_-)\) in physical time and
\(-2-4(k_+y_++k_-y_-)\) in reverse time, with the time argument
reversed in the latter. Each field is the pointwise minimum over
the allowed \(K\) band. A solution starting at a lower anchor stays
below the actual solution because the positive part of their
difference satisfies a Lipschitz differential inequality with zero
initial value. [Note12 §5][oracle] · [Note14 §5][tensor]

## 3. Matched data and cost

Give each method the same source cache, endpoint rows, paid geometry
and angular bounds, \(K\) enclosures and direct moment enclosures on
the same time cells. The existing consumer computes \(D=p_2/2-(p_1/2)^2\)
on each cell before using it in the \(K\) kernel. The small replay record
stores endpoint results and aggregate cell information. A repeated-query
implementation could retain the direct cell enclosures as the shared
consumer computes them, or reproduce them from the same source cache.
Both methods can intersect a direct enclosure with the scalar envelopes
available from the same data.
[Note14 §4][tensor] · [Consumer][code] · [Pinned record][record]

For a constant coefficient \(k\) on a cell of oriented length \(h\), the
solution map is
\[
 y\longmapsto e^{4kh}y+
 \begin{cases}
  (e^{4kh}-1)/(2k),&k\ne0,\\
  2h,&k=0 .
 \end{cases}
\]
It is affine and applies to the constant-band comparisons on each sign
region. In the fixed-sign case, composing the maps and storing the
propagated values at cell boundaries take a linear number of scalar map
operations in the number of cells. Once a query cell is located, either
method can use one partial-cell map for each stored comparison and
intersect with its cached direct interval. No new source calls enter this
scalar step. The operation count assumes the shared paid inputs. Runtime,
precision costs, cache construction and geometry acquisition were unmeasured.

For the declared minimum on the fixed tube, either method can use the
same derivative argument and direct endpoint interval. The earlier
65-call direct row and 196,673-call fine source grid compare recorded
endpoint and grid acquisitions with shared paid geometry. The existing
comparison gives no matched total cost for this minimum or for arbitrary
interior widths. A stronger minimum enclosure or a cost improvement would
need a distinct quantitative comparison after this shared postprocessing.
[Synthesis16 §2][synthesis] · [Continuation17 §§2–3][continuation]
· [Direct comparator precedent][comparators] · [Scope convention][scope]

## 4. Inherited controls

The exact quadratic \(w^2-2(t-1/20)\) shares the counted geometry and
has \(K=0\) and \(D'=2\). Its minimum on \([0,1/10]\) is
\(-1/10\). The nonnegative early-anchor premise for the displayed
forward envelope fails. Its exact backward bracket is negative before
the double and zero at the double. The earlier quartic likewise has a
local event despite its favorable force sign. The generic gap law can
apply to changed sources when their own tube hypotheses are paid.
[Note12 §§5–6][oracle] · [Note14 §§5–6][tensor]

The Euler-factor translates change the canonical completion and
Dirichlet coefficients. Weighted squares fail the conjunction of full
reflection and unchanged unit coefficients. Finite-source, finite-tail,
finite-prime and finite-score controls fail the complete canonical
source identities despite their retained data. The reflected
super-Gaussian, smooth-shape and positive-primitive controls lack
unchanged theta square arithmetic. The atomic and continuous finite-profile
controls lack the full theta profile and coefficients, and retain their
recorded failures of eventual simplicity. The normalized endpoint
control changes ordinary Dirichlet arithmetic and retains its RH
condition. The variable observation fails the literal cosine/Newman
equation, and the actual-profile relaxation lacks an integer zero
divisor of a specified field. The drift bands of these source controls
on the fixed canonical tube are untested here. The same-data result
covers the specified minimum and shared envelope operations on this
tube. It leaves open other estimators, other sources and distinct
interior width or total-cost comparisons.
[Control catalog][controls] · [Control premise convention][premises]

[decision]: ../brainstorm/notes/06_VCD_GT_B06_SOURCE_MODE_AND_MATCHED_ENVELOPE_20261116.md
[request]: ../research-progress/handoffs/VCD-GT-E03-r4.md
[oracle]: 12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[tensor]: 14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md
[certificate]: 15_VCD_GT_E04_CERTIFIED_SIGNED_GAP_20261116.md
[synthesis]: 16_VCD_GT_CANONICAL_SIGNED_GAP_SYNTHESIS_20261116.md
[continuation]: 17_VCD_GT_RESEARCH_CONTINUATION_20261116.md
[assessment]: ../reviews/08_VCD_GT_CANONICAL_GAP_CERTIFICATE_ASSESSMENT_20261116.md
[record]: ../numerics/05_VCD_GT_LEHMER_CERTIFICATE_20261116.json
[code]: ../numerics/vcd_gt_lehmer_certificate.py
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[comparators]: ../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
