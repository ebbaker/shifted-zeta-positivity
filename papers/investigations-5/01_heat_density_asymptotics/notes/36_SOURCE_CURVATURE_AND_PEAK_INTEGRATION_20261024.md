# Source-curvature gains and peak integration

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from session metadata. Thread
`01a170a3-5f6e-7aa2-9e33-bcae4835c782`, chat **0011**.

**Status: routine bounds proved in-note; bounded floating diagnostic and
same-model internal assessment. No continuous numerical acceptance.**
This is the return to [HDA-17-AN02 r1](../research-progress/handoffs/HDA-17-AN02.md),
continuing [Note 35](35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md).
The canonical source, physical regulator, normalization, fixed kernel and
AN01 component targets are unchanged. Read the
[result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially
[classification](../../../../avoid/01_restating_the_target.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [separate cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
This is a quantified approximation milestone, not an RH-equivalent reformulation.

## Decision and quantitative gain

**Close AN02 r1 as a completed bounded floating diagnostic with retained
failure. Prioritize a higher-order positive finite source, retaining the
new curvature/weight bounds and composite integration.** The remaining
source allowance is much larger than the remaining filter indicator.
No t=96 field computation was made because the predeclared t=64 gate fails.
HDA-17 remains Partial without an accepted core; HDA-18 remains Gated.

The [record](../numerics/SOURCE_PEAK_DIAGNOSTIC_20261024.json),
[diagnostic](../numerics/source_peak_diagnostic.py),
[source-budget implementation](../numerics/source_accuracy_improvements.py),
[exact controls](../numerics/check_source.py),
[control record](../numerics/SOURCE_CONTROLS.json) and
[assessment](../reviews/19_SOURCE_CURVATURE_AND_PEAK_ASSESSMENT_20261024.md)
retain the evidence. All ten frozen input hashes match. Prior source notes,
AN01 records and the manuscript remain unchanged.

At t=64, the source interpolation allowances improve as follows. The two
uniform columns compare the same finite interpolant, before changing any
field mesh. Uniform384 is evaluated only in the source ledger.

| Source mesh | Old LC4, order 0 | New continuous cap/chord formula, order 0 | New order 2 |
| --- | ---: | ---: | ---: |
| uniform 192 | 0.0563935 | 0.0211953 | 0.00437064 |
| uniform 384 | 0.0113742 | 0.00445718 | 0.000906060 |
| uniform 768 | 0.00255806 | 0.00102328 | 0.000206579 |
| adaptive 768 | — | 0.000104980 | 0.0000192557 |

The uniform improvement is 2.50--2.66 times; the single source-only adaptive
mesh gives another 9.75 times in order 0, for **24.37 times** versus old
uniform 768. The adaptive order 0--3 interpolation allowances are
[1.04980e-4,4.23706e-5,1.92557e-5,9.34631e-6]. Its widths range from
0.000475676 to 0.00951350, with 642 of 768 midpoints below 0.6, where the
weighted source error is concentrated. These are floating evaluations of
continuous inequalities, not interval-certified bounds.

### Full local error rows and attribution

All 91 externally targeted local rows are retained for each of the six
field observations. Source ratios below are allowance/(0.8 target), not
measured actual errors or lower bounds on possible errors.

| Source | Worst source ratio at y=0 | Worst source ratio at y=1/2 |
| --- | ---: | ---: |
| uniform 192 | 915116 | 241488 |
| uniform 768 | 21043.6 | 6238.26 |
| adaptive 768 | 2056.73 | 613.466 |

Each maximum is Delta Q. The adaptive Delta Q allowances are 16.4538 and
4.90773 against the 0.008 source allocations. At y=1/2, adaptive allowances
for R,R_t,U,Q,signed source are respectively
0.000128107,0.000315211,0.000999259,0.0496540,0.00000131295.
Some rows are useful, but the requested whole norm is not paid.
This is a scoped failure of the declared piecewise-linear estimates and
meshes, not a lower bound on their actual errors or a universal obstruction
to source approximations.

The record separates source-ledger gains from tightened nonlinear caps.
For example uniform 192,y=0,Delta Q gives old-ledger/frozen-cap allowance
49471.1; the new source errors with those same caps give 18631.8; explicitly
recomputing the smaller caps then gives 7320.93. For uniform 768,y=0 those
values are 444.900,179.093,168.349. Source variants are compared separately
under identical caps so the signed-source improvement is not hidden in
an interpolation comparison. At adaptive 768,y=1/2 the old product-source,
tightened product-source and signed-radial source allowances are
2.26014e-6,1.73530e-6,1.31295e-6. At y=0 they are
1.37752e-4,8.41609e-5,6.91768e-5. The signed improvement is genuine at
the stated envelope level; it does not sign the physical source itself.

### Integration, evaluator and arithmetic ledger

The composite 8/12 *weak observable* filter indicator has maximum
change/(0.1 target) 0.00320013, for W_t,x on uniform 192,y=0. The selected
*direct observable* filter indicator has maximum 0.786370, for R_t,x on
uniform 192,y=0; its change is 9.67603e-6 against 1.23047e-5. Report both:
the smaller two-jet weak figure does not describe the direct four-jet route.
Both are sampled refinements, with no continuous remainder or arithmetic
certificate. Direct/weak identity disagreement has maximum allocation
ratio 0.000520763 among the selected direct rows; it is a cross-check,
not another enclosure.

The positive error-envelope integrations have their own indicators.
Their maximum is 169.227 on uniform 192 R_t at y=0. At adaptive 768 the
maximum is **1.01162**, from Delta Q at y=0: change 0.00101162 against
0.001. It is slightly above the allocation and remains unpaid. At y=1/2
that ratio is 0.069752. The source bottleneck 2056.73 is on a substantially
larger scale, so further filter refinement is secondary in this bounded
comparison. No slight overrun is rounded into acceptance.

The adaptive y=1/2 Delta Q tensor 64/composite 12 disagreement is 0.0255005,
whereas composite 8/12 changes it by 1.78072e-7. The adaptive comparison
uses the same 8-point source rule in both filters. Historical tensor values
for the identical uniform finite fields use the old source rule; their
comparison is labeled as such and still has unpaid evaluator arithmetic.
The large filter gains justify retaining composite integration for the
next representation trial; they do not establish convergence on D.

The six requested error categories remain distinct:

- **Interpolation:** dominates every nonzero mapped source allowance. SP1--4
  reduce the same complete-source approximation allowance without changing
  canonical data or the cutoff.
- **Omitted modes:** the fixed four-mode source has a positive LC3 remainder,
  mapped separately. It is negligible here, so no new mode count was tried.
- **Complete tail:** FB7 remains positive; its log10 values at order 0 and2
  are approximately -483.767 and -483.415. Mapped logarithmic tails are kept
  instead of treating underflow as zero.
- **Nodal arithmetic:** the old unproved candidate
  `1e-12 Phi_N(binary64 node)+1e-300` has observed discrepancy ratios
  0.0858899,0.106694,0.102076 for uniform 192,uniform 768,adaptive 768,
  respectively, against 80-digit source evaluations. These are finite checks,
  not rounding bounds. New source-cap/chord arithmetic is also explicitly
  unpaid and is distinct from this nodal candidate.
- **Later evaluator:** the weak source-rule 8/12 indicator has maximum
  allocation ratio 2.55795e-10. Its tiny difference pays neither a continuous
  source-quadrature truncation remainder nor elementary-function rounding.
  The direct four-jet evaluator category is separately unpaid. No new
  120-digit check was made.
- **Spatial filter:** weak/direct observable refinements, positive-envelope
  refinements and tensor/composite disagreements are all retained separately.
  None is a continuous integration error bound. The |Delta K| interior kink
  is retained, not mistaken for an axis-split polynomial integrand.

Measured main execution is 132.472860 seconds. Six exact controls took
0.385188 seconds; source/normalization checks were below one second.
A conservative total debit of 142.473 seconds includes 10 seconds for all
auxiliary work, below the 30-minute cap. The fine rule uses 36864 points,
**9 times** tensor 64's 4096, while the coarse composite uses 16384. There
are 90112 field evaluations per observation when the fine support is
reevaluated with the second source rule; unique rule positions total 53248
per observation before any cross-center coincidences. The main source-node
by field-point work count is 3,001,024,512, plus 50,331,648 for the adaptive
tensor 64 comparisons. Thus the integration gain has an explicit finite
cost; order labels alone are not a cost comparison. Large arrays were
regenerated in memory, not saved in Git. The JSON record is below 1 MiB.

The delivered script adds a fail-closed pre-switch guard, evaluator-scope
labels and work/direct-filter summaries after the measured calculation;
the executed and delivered main-source hashes are both retained. These
reporting/guard additions do not change the arithmetic of the executed
t=64 path. The environment and all exact hashes are in the record.

## Stopping and next deliverable

The packet's t=96 gate required source and integration indicators within
allocation. It fails, so no switch-time field extension is performed.
No larger source count, cutoff, precision, root search, endpoint/onset
calculation or spatial splice is justified by this result. CJ27 is still
unpaid: source gates fail, arithmetic/filter enclosures and endpoint field
errors/residuals are unavailable. No observable estimate substitutes for
the required endpoint field error.

**Next: Analysis and numerics — Sol.** Freeze a new bounded representation
comparison at the same t=64 points: cubic Hermite source cells using
canonical Phi_N and Phi_N' at the selected nodes, a continuous complete
Phi^(4) interpolation remainder, and a linear fallback wherever cubic
Bernstein coefficients cannot establish nonnegativity. This seeks a
higher-order source error while retaining positive source moments and
an exact finite heat field. Compare at fixed cell/coefficient cost and
reuse the composite rule; preserve separate nodal-value and nodal-derivative
arithmetic and all tails. Do not enlarge the switch-time slab before this
source question is resolved. This is tractable Sol work; no new Astra
mechanism is needed. Spatial assembly remains a separate open problem.



## Sharper complete-source interpolation

Write A=pi n^2 exp(4u). The complete source summand has

    Phi_n''(u)=pi^(-1/4)n^(-1/2) exp(-A) A^(5/4) P(A),
    P(A)=-75+330A-224A^2+32A^3.                         (SP1)

Note 23 LC5 bounds the signed polynomial by four separately maximized
positive monomials. A tighter continuous cell cap keeps this cubic intact.
For A in [l,l+d], its Bernstein coefficients are

    P(l), P(l)+dP'(l)/3,
    P(l)+2dP'(l)/3+d^2P''(l)/6, P(l+d).                (SP2)

The Bernstein basis is nonnegative and sums to one. Thus |P| is at most
the largest absolute coefficient on the entire interval. Multiply that
cap by max_[l,l+d] A^(5/4)exp(-A), attained at clamp(5/4,l,l+d), and
pi^(-1/4)n^(-1/2). Sum n=1,...,8, and retain the positive complete
LC5 remainder n>=9. This is an inequality on the continuous cell, not a
sampled curvature envelope. The published numerical evaluation is binary64
and does not enclose its arithmetic.

A second valid cap is

    |Phi''(c)|+(h/2) sup_cell |Phi'''|,
    Phi_n'''=pi^(-1/4)n^(-1/2)exp(-A)
      [-375A^(5/4)+3270A^(9/4)-4232A^(13/4)
                     +1440A^(17/4)-128A^(21/4)].       (SP3)

A positive monomial cap gives the third-derivative supremum. For n>=9,
all A exceed the largest monomial maximum; the geometric mode ratio is
(1+1/9)^10 exp[-19pi exp(4a)]<1 on each cell starting at a.
The same argument with exponent8 gives the second-derivative tail.
Use the minimum of LC5, SP2 and SP3 as the final complete-source cap.
The midpoint cap uses all retained signed modes plus their positive tail,
not the truncated source alone. No field/zero information selects a cap.

### Integrated positive weights

For source order j=0,1,2,3 and t=64,Y=1,
W_j=u^j exp(tu^2+Yu) is convex on u>=0. This follows either by twice
differentiating or from its power series with nonnegative coefficients.
Replace W_j on each of eight or twelve equal subintervals of a source
cell by its secant chord. Convexity gives a continuous upper bound. The
interpolation kernel (u-a)(b-u)/2 and both linear hats are nonnegative,
so their integrals against the chord upper-bound all three LC2 weights.
Their integrands are polynomials of degree at most three and are integrated
exactly in the algebraic formula. For constant W the formulas recover
h^3 W/12 and hW/2, checking the interpolation factor and hats.

Consequently the *chord integration truncation* is paid by a continuous
inequality; floating endpoint/exponential/summation arithmetic remains
unpaid. The separate Gaussian8/12 LC2 values are diagnostic comparisons,
not the upper-bound proof. These source-ledger evaluation issues are
separate from later finite-field quadrature and spatial-filter integration.
Interpolation, omitted modes, complete tail and the historical candidate
nodal arithmetic allowance are kept distinct throughout.

### One adaptive source mesh

The sole adaptive test has 768 cells. On a fixed 4096-cell pilot, use the
continuous curvature cap B_i and the endpoint weight to define density

    rho_i=[B_i exp(64 b_i^2+b_i)(1+b_i^3)]^(1/3).        (SP4)

Normalize by its peak, floor it at 0.05, then exactly invert the cumulative
integral of this piecewise-constant density to select 768 quantiles. The
floor and pilot size are declared before observing the field. The factor
1+u^3 majorizes u^j for every j=0,1,2,3. This is a cost heuristic, not an
assertion of optimality. Its final source-cell bounds are recomputed over
the actual returned cells; no pilot sample is used as a final supremum.
All nodes remain in [0,1.5], with exact fixed endpoints and positive spacing.
The source values still use four canonical modes and the same positive
piecewise-linear interpolant family, whose exact field solves heat.

## Integration and source-transfer implementation

The composite spatial rule uses normalized quarter points plus the known
interior zeros of k',k'',k''',k'''' as axis boundaries. There are 16 panels
per direction; Gaussian orders 8/12 give 128/192 nodes per direction,
16384/36864 field points. These boundaries remove kinks of each separable
|K_(i,j)| through order 4; they do **not** remove the generally curved zero
set inside |Delta K|=|K_xx+K_yy|. That remaining kink and all continuous
filter remainders remain unpaid.

The layout is fixed from the kernel, shared by every mesh at each center,
and selected without a field-root search. Centers remain the existing
t=64,x=4,y=0 and 1/2. Only uniform 192, uniform 768 and adaptive 768 fields
are evaluated; uniform 384 is a source-budget comparison only. Source-cell
Gaussian rules are8/12. Composite integrals are summed over the complete
support *before* forming actual covariance, squared mean gradients and
LC9/10 mean products. Separately forming a covariance for each panel would
change the observable and is not done.

New source ledgers are compared both with old frozen caps and with explicitly
recomputed tighter caps. For each declared cap family, every pointwise local
map is a positive four-column map in d0,d1,d2,d3; the same columns map its
interpolation/mode/nodal contributions separately. Complete-tail contributions
retain a logarithmic mapped allowance. The direct source uses only orders 0,1,2.
The signed/product pointwise choice is frozen after the full error vector
selects it, before source categories are mapped; both maps are valid within
the stated caps. The signed radial map is analytically no worse under the
same caps, so this selection is an implementation cross-check.

The full numerical local table is **t=64 only**. C and C_t are zero there;
B=r_t W and r_x=0. This table is not an implementation of the complete
switch-time local contract. The adaptive signed-source and companion
curvature/time formulas below are analytical results, with their residual
premises stated separately. No numerical switch-time application is claimed.

The finite-field observable evaluator uses the exact weak identities for
the actual U,W,R,J,Q, times, forcing and source. A separate pointwise
rho,j,rho_t,s evaluator supplies selected direct comparisons, including
actual Q/Delta Q formed from physical gradients. Agreement is diagnostic;
it does not certify either formula's implementation arithmetic.
The source-rule 8/12 indicator stored in the record uses the weak evaluator,
which consumes jets 0,2. The direct four-jet evaluator's source quadrature
and rounding remain separately unpaid; no four-jet refinement certificate
is inferred from the two-jet indicator.

## Direct adaptive signed-source and companion formulas

## 1. Safe direct product transfer

At a fixed physical point let H and F be holomorphic and use the same
positive q=q(t,x), with r=log q. Write h=H or F, p=h_z, v=h_zz,
D=|h|^2+q, w=q/D, and

    rho=q|p|^2/(pi D^2),
    j=q v conjugate(p)/(pi D^2),
    s=(1-2w)[r_t rho+r_x Re j].

Take the existing LC6--LC7 allowances E_rho,E_j,E_w and common caps
rho_*=A_* P1^2 and j_*=A_* P1 P2. Here Pj>=|F_j|+d_j bounds both
jets and their straight interpolation. Let

    m=(|F|-d0)_+, M=|F|+d0,
    w_-=q/(q+M^2), w_+=q/(q+m^2),
    p_*=max(|1-2w_-|,|1-2w_+|) <= 1.

The direct positive pointwise envelope is

    E_s^product = p_* (|r_t| E_rho+|r_x| E_j)
                +2 E_w (|r_t| rho_*+|r_x| j_*).             (AS1)

Indeed telescope the factor (1-2w) and the bracket separately, using
|delta(1-2w)|<=2E_w. No heat equation is used, so (AS1) still compares
the independently defined signed sources when F has a residual. At
r_x=0 and p_*=1 it reduces exactly to Note23's older local source bound.

This uses source-error orders 0,1,2 only. It neither needs d3 nor obtains
the source by differentiating an allowance for density or current.

## 2. Sharper signed radial coefficient

The reviewer-proposed coefficient has been independently differentiated.
Retain the sign before taking absolute values:

    s=A_s(|h|) T_h,
    T_h=r_t |p|^2+r_x Re(v conjugate(p)),
    A_s(u)=q(u^2-q)/[pi(q+u^2)^3].                         (AS2)

For q fixed at this point,

    A_s'(u)=4qu(2q-u^2)/[pi(q+u^2)^4],
    A_s''(u)=4q(2q^2-17qu^2+5u^4)/[pi(q+u^2)^5].          (AS3)

Define a_s=max_[m,M]|A_s| and a_s1=max_[m,M]|A_s'|. Their complete
finite candidate sets are:

* a_s: both endpoints, and sqrt(2q) when it belongs to [m,M];
* a_s1: both endpoints, and
  sqrt(q(17-sqrt(249))/10), sqrt(q(17+sqrt(249))/10)
  when they belong to [m,M].

An endpoint zero or a collapsed interval is evaluated directly. The
interior zeros of A_s or A_s' are minima of their absolute values and
need not be added to a nondegenerate maximum list. The root candidates
in the second line follow by solving 5(u^2/q)^2-17(u^2/q)+2=0;
there is no missing pi or power of q.

Since

    |delta T| <= 2|r_t| P1 d1+|r_x|(P1 d2+P2 d1),
    |T| <= T_*:=|r_t|P1^2+|r_x|P1P2,

the sharper direct envelope is

    E_s^radial = a_s [2|r_t|P1 d1+|r_x|(P1 d2+P2 d1)]
                 +a_s1 T_* d0.                           (AS4)

This is a real gradient bound along the complex h segment; the gradient
norm of the radial map is |A_s'|. It stays smooth and valid at h=0 or
multiple events, since q>0. It uses the actual sign-changing multiplier
of rho and j before absolute values. It is not a replacement of a signed
average by the average of a magnitude.

With the same LC6 interval and standard caps, (AS4) is analytically no
worse than (AS1): A_s=(1-2w)A where A=q/[pi(q+u^2)^2], so

    a_s<=p_* A_*,
    a_s1<=p_* A1+2w1 A_*.

Both direct envelopes may be retained as an implementation cross-check;
their minimum remains a valid bound. The signed-radial form is the default
direct local source transfer when those maxima have been enclosed.

The explicit positive error coefficients in (AS4) are

    lambda0=a_s1 (|r_t|P1^2+|r_x|P1P2),
    lambda1=a_s (2|r_t|P1+|r_x|P2),
    lambda2=a_s |r_x|P1.                                  (AS5)

Thus E_s^radial=lambda0 d0+lambda1 d1+lambda2 d2. For source ledgers,
freeze these coefficient caps using the total declared d_j interval and
map interpolation, omitted modes, complete tail and nodal arithmetic
through that same positive row separately. Do not recompute a smaller
amplitude interval for an individual error category and then add the
resulting rows without a separate argument.

## 3. Spatial averaging and the coefficient derivatives

For every listed fixed spatial derivative alpha,

    |partial^alpha K*(s_H-s_F)|
        <= |K_alpha|*E_s,                                  (AS6)

where E_s is either valid envelope above, evaluated throughout the full
filter support at the integration points. In particular r_t and r_x
remain functions of the integration point. They may not be replaced by
their observation-center values.

No regulator coefficient derivative has been discarded in (AS6). It
integrates by parts the derivative of the whole product s, rather than
differentiating only rho,j,w. Expanded before that integration by parts,

    partial^alpha s = sum_(beta<=alpha) binom(alpha,beta)
      partial^beta(1-2w)
      sum_(gamma<=alpha-beta) binom(alpha-beta,gamma)
       [(partial^gamma r_t)(partial^(alpha-beta-gamma)rho)
        +(partial^gamma r_x)(partial^(alpha-beta-gamma)Re j)].

Thus r_tx,r_txx,r_xx,r_xxx occur where appropriate in an expanded x
derivative; (AS6) transfers all of them together to K_alpha. For the
physical r=a(t)-beta(t)x^2, r_xxx=0 exactly, while r_tx and r_txx
are generally nonzero. The full fixed-filter integration identity avoids
new pointwise derivative caps and does not assume those coefficients
vanish. It also avoids new source-error orders.

For alpha through two use the same compact C3 kernel as before.
A Laplacian may use |Delta K|*E_s, or the sum of |K_xx| and |K_yy|
convolutions. A positive-envelope integral is a numerical upper bound
only once its continuous support and integration arithmetic are enclosed;
sampled/refined values remain diagnostics.

## 4. Cheap companion envelopes for W_t, C and C_t

The current canonical H versus exact finite-source F comparison has
E_H=E_F=0, as in the standing contract. Retain that premise here.
At a point, with a,b_*,w1 from LC6, define for j=1,2,3 and m=0,1,2

    v_(m,j)=a d_j+Pj b_* d0+m Pj a E_w,
    V_(m,j)=w^m h_j conjugate(h)/D.

The same product telescope as CJ5 proves |delta V_(m,j)|<=v_(m,j).
It introduces no new jet order beyond the older d0 through d3 contract.

Put c_F=w(1-w), L1=V_(1,1), and

    E_wt=|r_t|E_w+2v_(1,2),
    E_ct=|r_t|E_w+2v_(1,2)+4v_(2,2).                      (AS7)

The 1-Lipschitz cubic w(1-w)(1-2w) justifies the r_t term in E_ct.
The pointwise curvature identity simplifies before comparison to

    4pi C=w r_xx+c_F r_x^2-4r_x Re L1.

Therefore

    E_C=[(|r_xx|+r_x^2)E_w+4|r_x|v_(1,1)]/(4pi).         (AS8)

This is tighter than separately bounding w_x in the unsimplified
curvature formula. For its time derivative all coefficient derivatives
remain:

    4pi C_t = w_t r_xx+w r_txx+(c_F)_t r_x^2
             +2c_F r_x r_tx-4r_tx Re L1-4r_x Re(L1)_t.

For exact heat fields direct differentiation gives

    (L1)_t = r_t(1-2w)L1 - V_(1,3) - pi conjugate(j)
             +4 L1 Re V_(0,2).

Use the caps L1_*=w_+P1 a and V0_*=P2 a, and set

    E_L1t=|r_t|[p_*v_(1,1)+2L1_* E_w]
           +v_(1,3)+pi E_j
           +4[L1_*v_(0,2)+V0_*v_(1,1)].                 (AS9)

Then a pointwise time-curvature envelope is

    E_Ct=[|r_xx|E_wt+|r_txx|E_w+r_x^2 E_ct
           +2|r_x r_tx|E_w+4|r_tx|v_(1,1)
           +4|r_x|E_L1t]/(4pi).                        (AS10)

Filter W_t,C,C_t with |K_alpha| exactly as in (AS6). For square C
one may use |square K|*E_C; no pointwise C_xx or C_yy is required.
For averaged B the direct companion is |K_alpha|*(|b|E_w), with the
unchanged full physical b=r_t+(r_xx+r_x^2)/2.

These optional time envelopes assume the existing exact heat fields.
For a general residual F_t=-Fzz+E, W_t and c_t have their CJ17 Z terms,
and (L1)_t has the additional exact term

    w E_z conjugate(F)/D + q F_z conjugate(E)/D^2
      -4L1 Re(E conjugate(F)/D).                         (AS11)

Those residual terms are not silently dropped or paid by AS7--AS10.
The direct source envelopes AS1--AS6 themselves require no heat or E_z
assumption. No source time derivative is requested or introduced; it
would have additional input requirements.

## 5. Six selected exact-rational checks

[check_source.py](../numerics/check_source.py) is standard-library only. It uses degree-four exact
fraction Taylor jets; all recorded differential differences are rational
zeros. The common regulator in these controls is
q=(2+t+t^2+x^2)^2>=49/16, with nonzero spatial and time coefficients at
the noncentral points. The six field-pair/point controls are:

* H=10z, F=(10+t)z at (t,x,y)=(1,1,0),(1/2,1,0);
* H=10(z^2-2t), F=H+tz at (1,2,0),(1/2,2,0),(0,0,0);
* H=10(z^2-2t), F=H+tz^2 at (1,2,0).

The first two families have E=z and E_z=1; the last has E=z^2+2t
and E_z=2z, which is 4 at its selected point. Thus the previously
untested nonzero E_z term in the residual balance is explicitly present.
At the central double event E_z=1 even though E=F=F_z=0.

Each case checks twenty differential identities: the prior CJ15--18 and
adaptive balances, signed radial source factorization, simplified
curvature and C_t, and both components of AS11's residual-aware L1 time
identity. Each also checks, in exact rational arithmetic, that both AS1
and AS4 bound the actual source difference. The five noncentral amplitude
intervals lie above 2sqrt(q), where all required LC6/radial maxima occur
at their lower endpoints; the sixth collapses to zero. This allows exact
rational maxima without numerical radicals. The signed-radial/product
envelope ratios are about 0.561,0.770,0.649,0.900,0.639 for those five
noncentral cases. These are controls, not predictions for the theta
observations or evidence of continuous accuracy.

The sole retained control execution took **0.385187792 seconds** in
Python3.10.0 on macOS27.0.1 arm64. The script SHA-256 is
`d8884c641aa073f43adb0396322a0ed5e7699c8078d31396d9a18a25306f4258`.
[SOURCE_CONTROLS.json](../numerics/SOURCE_CONTROLS.json) records exact inputs, differences, envelopes,
environment and runtime. No source mesh, theta observation, quadrature
refinement, web lookup, repository file or chat history was changed by
this delegated analysis.


## Control screen and review scope

The generic holomorphic transfer allows colliding controls. Euler-factor
controls change the canonical source; weighted-square controls change
weights/full reflection; reflected controls lack the canonical integer-square
expansion; smooth/positive-primitive controls lack the unchanged theta
arithmetic; atomic controls fail the C2 source-density premise. None is
excluded by the generic signed-source inequalities. Polynomial controls
here deliberately pass holomorphy and positive q, including a double event,
but fail canonical source representation. The new source-cap constants
apply to the unchanged theta expansion only. These catalog premise checks
and selected exact controls support no RH or simplicity inference.

The assessment includes a separate same-model subagent's read-only audit
of the formulas, code, data and decision. Shared prior source premises
remain shared. This is not independent specialist review or HDA-20.
The manuscript, all prior notes and numerical records, and other chats'
transcripts are unchanged. No commit or manuscript snapshot was made.

## Reproduction

With NumPy and mpmath available, run from the numerics folder, choosing
an external/ignored output path for regeneration:

```sh
python3 check_source.py
python3 source_peak_diagnostic.py --repo /path/to/shifted-zeta-positivity --output /tmp/SOURCE_PEAK_DIAGNOSTIC_20261024.json
```

The check writes its small source-control record beside itself. The
diagnostic imports the frozen AN01 evaluator and kernel module, generates
the source-only mesh deterministically and writes the small JSON record.
Record hashes identify this numerical environment and data, not a proof
or a guarantee of bitwise portability across arithmetic libraries.
