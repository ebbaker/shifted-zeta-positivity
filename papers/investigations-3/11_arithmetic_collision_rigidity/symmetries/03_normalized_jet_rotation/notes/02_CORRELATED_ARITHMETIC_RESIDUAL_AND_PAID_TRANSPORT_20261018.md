# S03 correlated arithmetic residual and paid transport

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning
effort ultra**, verified from this turn's metadata. Parallel same-model
analysis, implementation and internal review; no independent specialist
review.

**Bounded result.** On `[1/100,1/5] x [999,1001]`, with the prescribed
normalizer, phase and full corrected eight-mode approximation, the complete
signed residual-defect integral has a uniform certified bound below
`0.000266448`. Independent residual endpoints evaluated using the **same
complete source data** pay `0.002011747`. The ratio of the two certified
allowances is below `0.132446`. This is a finite estimate of the actual
arithmetic residual, with every source, approximation and propagation
error retained. It is not an all-height arithmetic theorem or new coverage.

## Contract and relation to the opening round

The [opening S03 note][opening] proved that scalar transport with two
independent endpoint errors is dominated by the ideal direct first-jet
test using the same approximation and envelopes. Its scope explicitly
leaves a smaller estimate of the complete residual integral open. This
continuation supplies such a bounded estimate. The primary gate is a
strict decrease against independent endpoints from the **same** new
source data and fixed cover, not merely against the older `0.827470`
S02 disk payment.

The repository [result summaries][summaries] and [patterns to avoid][avoid]
were read, especially [local geometry][geometry], [collision controls][controls],
[reformulations][target], [scope][scope] and [preserving cancellation][cancellation].
This is a quantitative finite approximation milestone. No global exclusion
criterion is introduced. The [program guide][guide], [S02 analytic
correction][s02] and [Note 07's rotation identity][n07] fix the conventions.
The earlier [transport Note 20][old20] already retains correlated physical
jet errors for a leading correction; [Note 22][old22] handles its cutoff
transition. Here the object is the residual **after** the full S02 analytic
correction, evaluated from the complete physical source on the pilot.

Keep `H_t=-H_xx`, `Q=H/A`, `omega=theta_x`, and
`f=(G_8-Chat_8)/A` exactly as before. All eight modes and the signed
correction are retained. The natural cutoff is 8 on this pilot; it is
never differentiated. Define `r=Q-f`,

\[
 W_r=r-i r_x/\omega,\qquad Z_r=e^{-i\theta}W_r,
 \qquad R_r=r+r_{xx}/\omega^2-\omega_xr_x/\omega^3.
\]

The quantity being bounded is

\[
 I_r(t,x)=i\{Z_r(t,x)-Z_r(t,999)\}
 =\int_{999}^{x}e^{-i\theta(t,y)}\omega(t,y)R_r(t,y)\,dy. \tag{1}
\]

The signed omega is negative here. The increment is zero at the anchor;
the actual residual and its derivative at the anchor are not zero.

## Subtract the arithmetic approximation before taking ranges

Use the fixed physical scale

\[
 G_*=1000^{7/4}e^{-125\pi},\quad
 V=H/G_*,\quad \widehat V=(G_8-\widehat C_8)/G_*,\quad
 \Delta=V-\widehat V,\quad \chi=G_*/A.
\]

Only V and the finite source integral from which its Taylor data are
computed obey the unmodified physical heat equation. Neither the
normalized residual nor its approximation is propagated as a heat solution.
The normalization is applied after constructing the physical residual.

Let `tc=21/200`, `xc=1000`, `h=x-xc`, `delta=t-tc`. The [complete
source evaluator][evaluator] supplies midpoint derivatives `v_j`, `0<=j<=50`,
as exact dyadic quadrature midpoints with outward radii. Complete source
reflection precedes the retained modes 1–11 and source cutoff `U=2`.
Its omitted-mode and source tails are retained separately.

Construct one consistent physical polynomial with spatial degree 26 and
time degree 12. Its residual coefficients are

\[
 d_{\ell k}=
 \frac{(-1)^k v_{\ell+2k}}{\ell!k!}
 -[h^\ell\delta^k]\widehat V(t_c+\delta,x_c+h),
 \quad P=\sum_{\ell=0}^{26}\sum_{k=0}^{12}d_{\ell k}h^\ell\delta^k.
                                                               \tag{2}
\]

Subtract the complete approximation at the coefficient level, before
interval evaluation. Differentiate this **same** P to obtain P_x and
P_xx. Using three independently truncated source polynomials as if they
were derivatives of each other would give incorrect edge accounting.

The approximation's mixed coefficients are explicit. For each reflected
channel and integer n, its physical mode is

\[
 e^{\mathfrak m_0(s)-s\log n}
 e^{t(\alpha(s)-\log n)^2/4}.
\]

Time coefficients are powers of `(alpha-log n)^2/4`, divided by `k!`.
The full correction satisfies the exact identity

\[
 \partial_t\widehat C_8=(\pi/4)\partial_x\widehat C_8
                       +(\pi^2/64)\widehat C_8.                \tag{3}
\]

This follows from its exponential prefactor and dependence on
`v=x/2+pi*t/8`; it supplies every mixed coefficient using spatial
derivatives through order 38. Principal logarithms and square roots keep
the original branches. Both holomorphic channels are retained on complex
domains; a real-part formula is not used to define their continuation.

Nominal signed coefficients in (2) preserve the cancellation. Quadrature
radii are retained conservatively in coefficient balls. Reusing an Arb
object is not a claim of exact covariance for the repeated coefficient
uncertainties. These radii are paid throughout; their small independent
diagnostic envelope is printed and is not added twice.

## Complete differentiated remainder

For `j=0,1,2`, the differentiated polynomial has spatial degree `26-j`.
The complete source's finite-integral majorant through order 52 gives

\[
 E_{H,j}\le M_{52}
 \left\{\frac{1}{(27-j)!}+e\frac{(19/200)^{13}}{13!}\right\}
       +T_{{\rm modes},j}+T_{{\rm source},j}.                 \tag{4}
\]

The largest retained midpoint index is `26+2*12=50`; the largest time
remainder index is `26+2*13=52`. The differentiated spatial remainder
uses index 27. Thus no unavailable derivative bound is assumed.
Quadrature radii already enter (2), with their propagated supremum
reported separately.

The approximation's own Taylor tail is also paid. A fixed 256-cell cover
of the enclosing complex rectangle bounds `|Vhat|` on the polydisk
`|h|<=8`, `|delta|<=2` by `Mhat<3719520`. The cover checks that the
correction denominator excludes zero. Both logarithmic channels avoid
their cuts and poles, and the square-root arguments avoid the negative
axis. Therefore Cauchy's coefficient bounds apply to the complete analytic
expression.

Put `q=1/8`, `v=(19/200)/2`, and
`S_j(q)=(d/dq)^j[q^27/(1-q)]`. A safe rectangular tail for order j is

\[
 E_{\widehat H,j}\le
 \frac{\widehat M\,8^{-j}}{1-v}
 \left\{S_j(q)+\frac{v^{13}j!}{(1-q)^{j+1}}\right\}.     \tag{5}
\]

This comes from summing the omitted spatial and temporal coefficient
series; their overlap may be counted twice. Equations (4)–(5) and the
coefficient balls imply `|Delta_j-P_j|<=epsilon_j`, with

\[
 (\epsilon_0,\epsilon_1,\epsilon_2)
 <(3.191\,10^{-11},\ 6.815\,10^{-12},\ 3.553\,10^{-12}). \tag{6}
\]

These are in fixed G* units. The quadrature diagnostic is below
`6.733e-13` at each physical order and is already present in P. The
source beyond U is below `1.17e-435`; omitted modes and source Taylor
errors are small but remain in (6). Computed elementary constants use
outward arithmetic, including rational factorial reciprocals.

## Correlated defect and signed integration

Let `a=(log A)_x`. Direct differentiation of `r=chi Delta` gives

\[
 R_r=\chi(C_0\Delta+C_1\Delta_x+C_2\Delta_{xx}),
\]
\[
 C_0=1+\frac{a^2-a_x}{\omega^2}
          +\frac{\omega_xa}{\omega^3},\quad
 C_1=-\frac{2a}{\omega^2}-\frac{\omega_x}{\omega^3},\quad
 C_2=\omega^{-2}.                                      \tag{7}
\]

Form `C0 P+C1 P_x+C2 P_xx` at the coefficient level before taking
ranges. Its added defect error is bounded by
`chi*(|C0|epsilon0+|C1|epsilon1+|C2|epsilon2)` and is below
`1.526e-9` after normalization. The main cancellation is between the
residual and its second derivative, not an assumption that they are
independently small.

Use the opening round's 32 closed time slabs and 128 closed spatial
cells, including every boundary. On a time slab and spatial cell
`X_j=[x_j,x_(j+1)]`, enclose the complete complex integrand of (1) by
`F_j`, with its error included. For every `x in X_j`,

\[
 I_r(t,x)\in
 \sum_{k<j}|X_k|F_k+[0,|X_j|]F_j.                      \tag{8}
\]

The inclusion follows by integrating whole-cell range enclosures, so no
additional quadrature approximation is made. Partial last cells in (8)
cover possible interior maxima. Take moduli after signed complex prefix
summation. All elementary-function rounding, parameter variation and phase
uncertainty are in the interval images.

## Matched comparison and interpretation

The [192-bit run][r192] and [256-bit replay][r256] consume the same fresh
192-bit source setup, validated against the current source and manuscript
hashes. Rebuilding that setup took about 9.10 seconds and 173,696 callbacks;
it also passed the earlier signed and wall consumers. Its cache stays
external and is regenerated by the command in the [reproduction guide][reproduce].
The second precision run replays the new calculation, not a second source
quadrature. No cover was enlarged to obtain the result.

| Uniform paid residual increment | Allowance |
| --- | ---: |
| Old independent joint disk endpoints | `<0.827470` |
| Independent endpoints from the same fresh source model | `<0.002011747` |
| Complete defect integrated in absolute value | `<0.000374760` |
| Complete signed complex prefix integral | **`<0.000266448`** |

Most of the improvement over the old disk error comes from more accurate
source information; it is not attributed to endpoint correlation. The
matched ratio is below `0.132446`. The absolute-integral comparison
separately shows the effect of preserving the residual/second-derivative
cancellation. Signed spatial integration further reduces that allowance
by about 29 percent. These compare specified certified upper bounds, not
optimal norms or exact worst-case errors.

At the center, the residual is about `-0.0008022144`, its derivative about
`-0.0001434195`, and its defect about `-2.5881e-6`, with explicit paid
remainder intervals in the record. The global complete defect bound is
`<0.000346826`. The point illustrates the correlation; equations (2)–(8)
and the full closed cover establish the uniform claim.

The opening record supplies the nominal slab bound
`gap=inf(|W_f(999)|-|I_f(x)|)`, with all signed finite evaluation costs
included. On each identical time slab the new paid transport radius is
`gap-e_anchor-B_correlated`; the matched independent version is
`gap-2e_anchor-e_slab`. Their uniform lower bounds are respectively
**`>1.124460`** and **`>1.122848`**. Both now pass on the existing pilot.
The script validates the opening record's code, inherited source pins,
slab count and geometry before consuming its nominal bounds.

The same-data direct first-jet radius bound exceeds `1.336516` and remains
stronger. Moving the old inconclusive disk transport result to a pass is
largely due to the stronger source information: the independent calculation
with that information passes too. Correlation improves its matched scalar
transport margin by about `0.001612`. No performance advantage or new
covered region is asserted.

One useful interpretation is an oscillator calibration. With the **actual**
anchor residual data, let

\[
 g=r(t,999)\cos(\theta-\theta_0)
    +\frac{r_x(t,999)}{\omega(t,999)}\sin(\theta-\theta_0).
\]

Then `R_g=0`, `Z_g` is constant, and `|W_(r-g)|=|I_r|`.
For an executable calibration, choose the exact dyadic midpoint of each
coefficient ball in (2), obtaining `P_mid`. Use `chi*P_mid` and its
normalized x derivative at 999 as the two nominal anchor coefficients.
The two anchor polynomials are exported in each small run record as 13
exact dyadic time coefficients each. Their sums at `h=-1` use exact
rational arithmetic, so coefficient exponent gaps cannot discard terms.
The complete bound for the anchor error is below `6.026e-10` uniformly
in time. The checker's resulting bound is

\[
 \left\|\left(Q-f-g_{\rm mid},
       -\frac{\partial_x(Q-f-g_{\rm mid})}{\omega}\right)\right\|_2
 <0.000266449.                                         \tag{9}
\]

Thus the result supplies a calibrated complete first-jet approximation on
the pilot, not just a formal interpretation with unknown anchor values.
It identifies an almost rotating residual there without inferring a
uniform rotation law for all arithmetic modes.

For return to physical units put `J=(Q,-Q_x/omega)`. The exact matrix is
`(H,H_x)/A = T J`, with `T=[[1,0],[a,-omega]]`. Consequently

\[
 E/A^2=\|TJ\|_2^2,\qquad
 \sigma_{\min}(T)\ge
 \frac{|\omega|}{\sqrt{1+a^2+\omega^2}}.
\]

The already checked pilot bounds `|a|<0.390946`, `|omega|<1.094473`
give `||T||<=||T||_F<1.534`. Equation (9) therefore returns a complete
physical value/derivative error, divided by the local positive A, below
`0.000408734`. The positive paid jet radii above exclude a common physical
zero because T is invertible; normalized radii are not physical energies.

## Controls and next obligation

The new signed-prefix integrator is checked on an exact oscillator
residual, a constant residual, and a polynomial heat event. At the event
`H=x^2-2(t-tc)`, with `A=1`, `theta=x`, `f=2 cos x`, anchor -1 and
event 0, `R_r=x^2+2` and `|I_r(0)|=sqrt(5)=|W_H(-1)|`.
The strict propagation consumer must reject it using its own exact
polynomial error data. A zero-defect oscillator residual tests exact
cancellation; it does not supply a nonzero anchor automatically.

The [fresh source-specific replay][control-record] separately rejects the
five prior event boxes and the Euler negative-Laguerre witness using their
own source errors. These checks do not substitute theta constants into a
control. Finite-prime and finite-square controls lack full normalized theta
reflection/coefficient data; reflected, shape and primitive controls lack
the unchanged theta square series; Euler controls change level-one data;
counter-kernels and polynomial events lack the exact theta source; auxiliary
positive realizations lack the required complete physical comparison.
See [the control summary][controls] for the different scopes and which
constructions have effective event boxes.

The bounded matched correlation gate passes. The next arithmetic question
is whether the nearly oscillator residual can be bounded from its analytic
mode and correction structure at growing height, rather than by a new
complete-source setup on each pilot. No such uniform estimate is proved
here. The real bridge `(1001,exp(2000))` and global complex exterior remain
open. The manuscript remains unchanged.

[opening]: 01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[cancellation]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[s02]: ../../02_cutoff_reflection/notes/01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md
[n07]: ../../../notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md
[old20]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md
[old22]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
[evaluator]: ../../../numerics/high_height_consumer/high_height_consumer.py
[r192]: ../numerics/S03_CORRELATED_RESIDUAL_192_20261018.json
[r256]: ../numerics/S03_CORRELATED_RESIDUAL_256_20261018.json
[reproduce]: ../numerics/README.md
[control-record]: ../numerics/S03_CORRELATED_CONTROLS_20261018.json
