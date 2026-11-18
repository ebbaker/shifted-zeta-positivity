# E38 — Actual Lobatto cardinal norm and the fixed source refinement

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Helper requested/selected model
**gpt-6.1-sol**, reasoning effort **ultra**, by recorded dispatch;
independent serving-model attestation is unavailable. This proof and its
implementation have the same author. Separate preflight and final
nonauthor assessment are required; the sole progress register owns status.

**Status at proof submission: proved in-note, awaiting nonauthor preflight;
no dependent new-budget numerical certificate has been executed.** This is
the bounded E38 execution of [Continuation43][n43]. Under
[classification01][class] it is a finite source-error and enclosure-width
milestone, not an RH-equivalent reformulation. Read the
[result index][results], especially [cluster18][cluster] and
[controls12][controls], and the [avoid index][avoid], especially
[premises02][premises], [scope07][scope] and [joint12][joint].

| Task | Type | Recommended model | Dependency | Output and limit |
| --- | --- | --- | --- | --- |
| E38 | E — execution | Sol; route, source and comparison are fixed | Nonauthor acceptance of Sections 1–4 before dependent execution | Actual cardinal proof, fixed-budget source/geometry/path replay and at least tenfold width reduction against Record19; at most two correctness repairs and one main run, 1200-second cap |
| Nonauthor assessment | E — execution | Sol; verification of fixed proof and record | E38 proof, then E38 record | Check the DCT-I normalization, source payment, complete geometry/path semantics, common-budget comparison and controls |

The physical source, counted pair, exact interval
`I=[-3/10000,1/10]`, degree32 in each variable, 224-bit arithmetic,
128-node contour, archived 33-by-128 source array and prescribed
geometry schedule remain those of [Note39][n39]. The whole-time
consumer is fixed at 512 closed cells. No new xi evaluation, altered
precision, source scan or changed true-field/time/derivative payment is
permitted. The primary statistic is `min_I D`; both the independent-moment
and centered direct estimators receive the same refined source budget.

## 1. The cardinal functions of the implemented DCT-I

Put `n=32`, `h_0=h_n=1/2`, and `h_j=1` otherwise. The inherited
`tensor_coefficients` in [the GT consumer][base] uses ascending nodes

    x_j=cos((n-j) pi/n),  j=0,...,n,

and its returned unprimed coefficient of `T_k(x)` is exactly

    a_k=(2 h_k/n) sum_(j=0)^n h_j y_j T_k(x_j).             (1)

Indeed `endpoints[j]` and `endpoints[k]` in that function are these h
weights, and `cosine[k][j]=cos((n-j)k pi/n)=T_k(x_j)`.
The prior spatial DFT is linear and does not alter this time formula.
Thus the implemented exact interpolant has cardinal functions

    ell_j(x)=(2 h_j/n) sum_(k=0)^n h_k T_k(x_j) T_k(x).     (2)

Here is an explicit normalization check. For `theta_j=j pi/n`, the
endpoint-half-weighted cosine sum is half the real sum over all 2n
roots of unity. It is n for frequency 0 or 2n and zero for every
integer frequency between 1 and 2n-1. Applying
`2 cos u cos v=cos(u-v)+cos(u+v)` therefore gives

    sum_j h_j T_k(x_j)T_l(x_j)
       =delta_(kl) n/(2h_k),   0<=k,l<=n.                (3)

Reversing the cosine grid only multiplies its kth vector by `(-1)^k`,
so it leaves (3) unchanged. Substitution into (2) shows
`ell_j(x_i)=delta_(ij)`; each ell has degree at most n. Consequently
(2) is the actual Lagrange cardinal polynomial, with no omitted endpoint
factor and no assumed alternative node order.

## 2. Interior and exterior operator norm

Using (2) twice and then (3) gives the exact identity

    sum_j ell_j(x)^2/h_j=(2/n) sum_k h_k T_k(x)^2.         (4)

For real `x in [-1,1]`, `|T_k(x)|<=1` and `sum_k h_k=n`.
Cauchy–Schwarz applied to `sqrt(h_j)` and
`|ell_j(x)|/sqrt(h_j)` yields

    sum_j |ell_j(x)| <= sqrt(n)*sqrt(2)=sqrt(64)=8.        (5)

For `x<-1`, use the ascending grid in the Lagrange product

    ell_j(x)=prod_(m!=j)(x-x_m)/(x_j-x_m).

The n numerator factors have sign `(-1)^n=+1`, while its denominator
has n-j negative factors. Since n is even,

    sign ell_j(x)=(-1)^(n-j)=(-1)^j=T_n(x_j).             (6)

No factor vanishes there. Exact reproduction of the degree-n polynomial
T_n now gives

    sum_j |ell_j(x)|=sum_j ell_j(x)T_n(x_j)=T_n(x).       (7)

The equality extends to x=-1 by continuity. For `u>=1`,
`T_n(u)=cosh(n arcosh u)` is increasing; n even also gives
`T_n(-u)=T_n(u)`. Combining (5)–(7), with `X=503/500`, proves

    sup_(x in [-X,1]) sum_j |ell_j(x)|
        <=max(sqrt(64),T_32(X))<17.                     (8)

The last strict inequality can be checked with integers alone, without
a floating library. The recurrence `A_0=1`, `A_1=503`,
`A_(k+1)=1006 A_k-250000 A_(k-1)` gives
`T_k(503/500)=A_k/500^k`. Reduction at k=32 gives numerator

    1803430947144682413866830693604378620008431854098058020625044410533190410003841

and denominator

    108420217248550443400745280086994171142578125000000000000000000000000000000000.

Seventeen times this denominator minus the numerator equals the positive
integer

    39712746080675123945839067874522289415396270901941979374955589466809589996159.

Equation (8) is an upper bound, not an assertion that the interior maximum
equals eight. The exact exterior equality is used only on the stated
left extension. No derivative norm is replaced by (8).

## 3. Complex nodal errors and distinct arithmetic enclosure

At each fixed `|w|<=21/20`, let the exact spatial polynomial P_j(w) be
the degree32 DFT reconstruction from the archived mathematical decimal
midpoints at time node j. The inherited spatial proof pays

    |G_(t_j)(a+w)-P_j(w)|<=E_node
      =E_sample+E_alias+E_spatial_tail.                  (9)

These are arbitrary complex disk errors; no common phase or real-valued
nodal-error assumption is available or needed. Since the cardinal
functions are real on the real x interval, triangle inequality gives

    |I_n[G_(t_j)(a+w)-P_j(w)](x)|
         <=E_node sum_j |ell_j(x)|<=17 E_node.           (10)

The same conclusion holds for complex errors by triangle inequality
even without the reality observation. Correlations between different
spatial coefficients are therefore retained at the level required by
the time interpolation operator; separately varying all transformed
time coefficients was the enlargement responsible for 1100.

There are two different enclosures here. Equation (9) compares the true
field with the **exact** spatial polynomial made from the archive's
chosen decimal midpoint values. The inherited loader converts these
decimal values to Arb/Acb balls, including every power-of-ten conversion.
The DFT roots, DCT-I cosine factors, coefficient sums and products are
then all evaluated with outward rounding. Each returned Acb coefficient
therefore contains the exact coefficient of that one mathematical P.
`ExtendedField` keeps those coefficient balls, builds `acb_poly` bases
with outward arithmetic, and evaluates those balls without extracting
their centers. This already encloses transform, conversion and
polynomial-evaluation arithmetic. That arithmetic is **not** an
independent nodal source error and is not discarded or replaced by17.

The execution records coefficient rectangle radii and an absolute
`sum_(m,k) R^m T_k(X) hypot(rad Re A_mk,rad Im A_mk)` upper diagnostic
on the disk, separately from (9). It is an audit of arithmetic already
inside the coefficient balls, not another source allowance to be added
twice. All later circle/time construction and evaluation continue to
use their ball coefficients. A consumer using coefficient midpoints
instead would need a separate explicit arithmetic allowance and is
outside this implementation.

## 4. Only the nodal interpolation factor changes

In [Note39][n39], the complete true-field time remainder uses the same
radius-five majorant `4*10^20`, radius gap `5-21/20`, derivative order66,
Lobatto node product, and the conservative exterior product factor2:

    E_time=(4*10^20)*66!*(1/20)^33*2 /
             (33!*2^31*(5-21/20)^66).                  (11)

Keep every term in (9), (11), and every spatial/time polynomial
derivative weight `T_k(X)` and `k U_(k-1)(X)` unchanged. The only
replacement is

    E_old=1100 E_node+E_time,
    E_new=  17 E_node+E_time.                           (12)

Both independent-moment and centered direct estimators use this same
E_new, the same newly enclosed geometry, logarithm boxes and annular
tail formulas. Their assembly uses [Note42][n42]'s paid square range
and exact-midpoint rule for h. Geometry is recomputed on the full I;
the fixed 512-cell time enclosure pays count/clearance, D,M,F and the
regular identity `D_t=2-4DM`. Its bounds `|D|<1/5` and
`0<M<77/125` imply `D_t>942/625=1.5072`, retaining the proof when D
is negative. Thus `min_I D=D(-.0003)` follows on the full source tube,
not from endpoint samples. All annular tails remain separately paid.

The frozen comparison requires the new outward centered width to be
at most one tenth of the **lower bound** on Record19's centered width.
The record also reports the residual centered-versus-independent gain
under E_new, without confusing it with the source-accounting gain.
Common archive validation, polynomial/error reconstruction, coefficient
audit, geometry and path work, endpoint/log preparation and the two
assemblies are charged separately. No equality of total arithmetic or
runtime and no source-acquisition speed advantage is asserted.

## 5. Collision controls and scope

The cardinal theorem is generic and applies equally to collision
controls; it is not an arithmetic discriminator. Execute the exact
quadratic `w^2-2(t-1/20)` with zero true-field error through the same
geometry, 512-cell path and endpoint log/moment machinery. At t=.05,
both estimators must retain D=0. Across its collision the strict D and
F>=.3 gates fail; count two and annular clearance can still pass.

The [controls12 catalog][controls] imposes the following explicit
premises, inherited from [Note39 §6][n39] and [Note41 §5][n41]:

| Control | Premise absent from this canonical application |
| --- | --- |
| Quadratic, quartic, cosine | Literal xi/theta source and canonical population; quadratic also fails the quantitative gap/forcing contract across its collision |
| Euler-factor translates | Unchanged complete normalized theta coefficients and completion |
| Weighted-square, finite-tail/score perturbations | Full reflected unit-weight theta source equality |
| Finite-prime orbit controls | Full reflection and complete canonical arithmetic |
| Reflected super-Gaussian | Canonical order-one class and literal theta arithmetic |
| Smooth shape, positive primitive, finite profile | Full canonical arithmetic/profile/count transfer |
| Atomic profiles | Complete canonical population, full theta profile and documented eventual simplicity |
| RH-conditional normalized endpoints | Ordinary Dirichlet arithmetic changes; RH remains an input |
| Changed observation kernel | Literal cosine/Newman readout |
| Fractional profiles | Integer divisor multiplicity |
| Static surgery, relaxed scalar errors | Established common canonical heat tube; no divisor realization is supplied |

A control can pass a certificate on a collision-free box. The required
rejection concerns a domain containing its collision and the strict gap
conclusion. Neither (8) nor a narrower enclosure for this one canonical
pair establishes an all-height claim, an improved Newman bound, a common
finite-polynomial approximation tube, hierarchy truncation stability,
recursive convergence or the separate census's missing forward tube.

## 6. Execution return

**Completed interval execution, pending separate final nonauthor
assessment.** The nonauthor proof preflight accepted Sections1–4 without
required correction before the first new-budget run. The
[new consumer][code] verified all eleven E38 frozen input pins, the
fourteen inherited source pins, both archive hashes, and used zero new
source calls. Canonical and quadratic geometry both passed the first
16-time-cell/64-arc attempt. Both full paths used exactly512 closed cells.
All canonical source, count, clearance, forcing and monotonicity gates
passed; the quadratic retained its collision and failed both strict path
gates as required. The [small Record22][record] holds the full outward
balls, arithmetic and cost records.

| Quantity | Certified conservative summary |
| --- | --- |
| E_node | `<0.000480614603` |
| Old E | `<0.528676064` |
| New E | `<0.008170448251` |
| Unchanged E_time | `<1.145383e-15` |
| Uniform coefficient-radius diagnostic, already inside coefficient balls | `<3.922e-54` |
| New centered width | `<2.29767333e-8` |
| New independent-moment width | `>2.38011517e-8` |
| Old Record19 centered width | `>7.80046922e-7` |
| Width factor over Record19 centered | `>33.9494` |
| Source-accounting width reduction versus Record19 centered | `>97.0544%` |
| Residual centered reduction versus new independent moments | `>3.4637%` |

The resulting whole-minimum enclosure lies inside

    [0.00082198577487, 0.00082200875162].                 (13)

This improves a centered direct estimator by sharper source-error
accounting. Both estimators use identical refined data, logarithm boxes
and tails; the remaining3.46% correlation gain is a separate comparison.
The full-time enclosure gives `D<.179119` and
`.599312<M<.615573`, so the fixed bounds in Section4 establish
`D_t>1.5072` everywhere on I and justify (13) for `min_I D`.
The full-time forcing floor is greater than `.40539857`.

The centered width's existing-data decomposition is

    2*S(w^2-h*w)                  =1.18700482146...e-8,
    epsilon2+2*|h|*epsilon1        =1.11066850419...e-8,
    width of (Gamma-h)^2          =3.37093734109...e-17.   (14)

The log-rectangle term contributes about51.66% and the annular-tail
term48.34%; remaining nominal and endpoint rounding is enclosed in
the reported width. This is not an assertion that log-rectangle support
is purely the scalar source error: those boxes also contain the retained
polynomial/evaluation arithmetic. Equation (14) was derived from the
same computed R_h, h and epsilon data and requires no new acquisition.
It identifies why another comparable large gain cannot come solely
from further reducing nodal source amplification while retaining the
present tail allowances.

The primary run passed all mathematical gates in about1.483 seconds.
Its exact script and record hashes, and the external retained reading
copy `/private/tmp/vcd-gt-cm-E38-primary-20261118.json`, are recorded in
Record22. Two bounded accounting repairs followed: first remove an
unused repeated endpoint integration and derive that old direct interval
from the already prepared logs; then state the actual duplicate-log
cost in the inherited F consumer and the decomposition (14). The first
repair's successful record is retained at
`/private/tmp/vcd-gt-cm-E38-repair1-20261118.json`. All31 selected
canonical/control mathematical result fields matched the primary
exactly after both repairs. No mathematical/source/target parameter
changed. The final author execution took about1.405 seconds; no further
author run or repair is permitted by this packet.

Each inherited full-F time-cell consumer computes65 logarithms twice.
The two512-cell paths therefore evaluate133120 complex logarithms;
the two shared endpoint preparations add130, and the separately
retained quadratic collision consumer adds130: **133380 actual complex
logarithm evaluations** in total. This is distinct from128 represented
contour nodes and65 shared log rectangles per estimator endpoint.
Common archive, coefficient, geometry, path and endpoint preparation
is charged to both estimators. Both assemblies and all repeated timing
diagnostics are charged separately. Neither equal total cost nor a
speed saving is claimed.

Replay the frozen consumer with a new output path:

```sh
/private/tmp/vcd-gt-lehmer/venv/bin/python \
  papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/numerics/vcd_gt_cm_cardinal_source.py \
  --cache-dir /private/tmp/vcd-gt-lehmer \
  --output /private/tmp/vcd-gt-cm-E38-nonauthor-replay.json
```

These temporary locations are observed reading copies, not permanent
availability promises. The inherited normal-path and `VCD_GT_ARCHIVES`
fallback remain available and fail closed if either archive identity is
missing or wrong. Old inputs, Notes38–43, numerical records16–21,
shared registers, manuscript, history and E16 bindings are preserved by
this author. No new manuscript snapshot, PDF or large derived file was
created. Final E39 assessment owns the nonauthor disposition; this note
does not assign itself independent or specialist review.

[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[base]: ../../numerics/vcd_gt_lehmer_certificate.py
[n39]: 39_VCD_GT_CM_E34_EXTENDED_SOURCE_AND_FORCING_20261118.md
[n41]: 41_VCD_GT_CM_B10_R3_CORRELATION_SELECTION_20261118.md
[n42]: 42_VCD_GT_CM_E36_CORRELATED_DISCRIMINANT_20261118.md
[n43]: 43_VCD_GT_CM_CORRELATION_GAIN_CONTINUATION_20261118.md
[code]: ../numerics/vcd_gt_cm_cardinal_source.py
[record]: ../numerics/22_VCD_GT_CM_CARDINAL_SOURCE_REFINEMENT_20261118.json
