# Gradient covariance closure and an actual-theta pilot

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.


**Status:** small-width expansion derived in-note; 17 bounded floating
comparisons on the theta integral. Same-assistant checks only. This
advances HDA-05–06 but supplies neither a solved reduced evolution nor a
uniform theta error bound. The [contract][contract] fixes the scope.

## 1. A first approximation to the required fluctuation term

Keep the [exact filtered equations][identities]
\[
U_t=-\tfrac12(U_{xx}-U_{yy})-\tfrac12(U_x^2-U_y^2+Q),\qquad
R=\Delta U/(4\pi),
\]
where \(Q=\operatorname{Var}_{\mathcal F}(S_x)-
\operatorname{Var}_{\mathcal F}(S_y)\) and
\(S=\log(|H|^2+\epsilon^2)\). A fixed positive regulator makes these
fields smooth even at a multiple zero. Smoothness does not imply small
variation over a chosen averaging window.

Let the independent, even filter coordinates have variances
\(v_t=\tau^2/11,v_x=\ell_x^2/11,v_y=\ell_y^2/11\).
Taylor expansion suggests the computable closure
\[
\boxed{Q_\nabla=
 v_t(U_{xt}^2-U_{yt}^2)
 +v_x(U_{xx}^2-U_{xy}^2)
 +v_y(U_{xy}^2-U_{yy}^2).} \tag{1}
\]
Its coefficients come from the kernel moments; no data fitting is used.
This is a standard type of small-filter expansion, not a novelty claim.
The [reference catalog][refs] records Clark–Ferziger–Reynolds at
abstract/metadata depth and Nabavi–Kim equation (6.3)/§6.3 as related
gradient-closure background. No turbulence stability conclusion or
unchecked theorem is imported into this theta calculation.

**Local expansion.** Suppose the averaging supports, scaled together by
\(\delta\), remain in a compact buffer and \(S\) has uniformly bounded
\(C^7\) derivatives there. For a symmetric product kernel,
\[
Q-Q_\nabla=O(\delta^4)\quad\hbox{in }C^2_{x,y}. \tag{2}
\]
Here the widths in (1) include \(\delta\), and \(\epsilon>0\) is fixed.
The constants depend on the buffer, derivatives, regulator and kernel.
Equation (2) is not uniform as \(\epsilon\downarrow0\).

To see this, for smooth \(f,g\) expand both about the observation point.
The constant terms cancel in \(\mathcal F(fg)-(\mathcal Ff)(\mathcal Fg)\),
odd moments vanish, and the quadratic contribution is
\(\sum_\alpha v_\alpha f_\alpha g_\alpha\).
The remainder is \(O(\delta^4)\). Also
\(\partial_\alpha\mathcal Ff=f_\alpha+O(\delta^2)\), so replacing
unfiltered derivatives in this quadratic expression by filtered ones
changes it by \(O(\delta^4)\). Apply this to \(f=g=S_x\), then
\(f=g=S_y\), and subtract. Applying up to two spatial derivatives to
the same Taylor argument gives (2); \(C^7\) is a sufficient smoothness
assumption. No step assumes \(\mathcal F^2=\mathcal F\), and no
cross-correlation has been set to zero by a projection assumption.

For spatial-only isotropic smoothing, \(v_x=v_y=v\), (1) simplifies to
\[
\boxed{Q_\nabla=v(U_{xx}^2-U_{yy}^2)
       =4\pi vR(U_{xx}-U_{yy}).} \tag{3}
\]
Thus the mean density explicitly contributes to the fluctuation term.
A provisional potential equation is
\[
U_t=-\tfrac12(1+4\pi vR)(U_{xx}-U_{yy})
    -\tfrac12(U_x^2-U_y^2),\qquad R=\Delta U/(4\pi). \tag{4}
\]
Its mixed-sign spatial operator remains. This note proves no
well-posedness, positivity preservation or stability estimate for (4).
With time averaging, (1) involves time derivatives of the mean; it is
not automatically an explicit instantaneous evolution law. An auxiliary
history model or an implicit formulation needs separate analysis.

## 2. Test the derivative that actually enters density evolution

Replacing \(Q\) by \(Q_\nabla\) in the density equation has consistency
defect \(\Delta(Q_\nabla-Q)/(8\pi)\), evaluated on the exact mean fields.
For stable calculation of the exact term, differentiate the covariance
and use \(\Delta S=4\pi\rho\):
\[
\boxed{\Delta Q=
2\{\operatorname{Var}_{\mathcal F}(S_{xx})-
   \operatorname{Var}_{\mathcal F}(S_{yy})\}
+8\pi\{\operatorname{Cov}_{\mathcal F}(S_x,\rho_x)
       -\operatorname{Cov}_{\mathcal F}(S_y,\rho_y)\}.} \tag{5}
\]
For example \(\Delta(S_x^2)=2(S_{xx}^2+S_{xy}^2)+8\pi S_x\rho_x\);
the two \(S_{xy}^2\) terms cancel after subtraction. This proves (5).
It directly retains correlations involving the local density, and avoids
subtracting nearby values to obtain the exact \(\Delta Q\).

The implementation evaluates \(H,H_z,H_{zz},H_{zzz}\) from the theta
integral. In particular
\[
\rho_x=2\Re j-2\rho S_x,\quad
\rho_y=-2\Im j-2\rho S_y,\quad
\rho_t=-\frac{2\epsilon^2\Re(H_{zzz}\overline{H_z})}{\pi D^2}
       -2\rho S_t.
\]
It checks the differentiated equation in the equivalent form
\[
R_t+\tfrac12(R_{xx}-R_{yy})
+\frac{U_{xx}^2-U_{yy}^2}{4\pi}
+U_xR_x-U_yR_y+\frac{\Delta Q}{8\pi}=0. \tag{6}
\]
It also compares (5) with spatial finite differences and checks
\(R_t+\partial_x\Re J+\partial_y\Im J=0\) separately.
The latter uses finite differences of the undivided smooth current.

## 3. Floating comparison against the unchanged theta integral

The [script][script] and [execution record][data] hold all 17 cases.
The theta series is evaluated through \(n=8\), with the truncation and
quadrature choices in the contract. These are evaluations of the actual
theta formula with numerical truncations, not an interval-certified
complete-source oracle. All numbers below are observed values.

Representative cases at \(c_1=(0,28,1/2)\), \(\epsilon=10^{-4}\):

| Halfwidths (time, x, y) | Mean density R | Exact Q | Omit-Q density defect | Gradient density defect |
| --- | ---: | ---: | ---: | ---: |
| (0, 0.25, 0.25) | 0.19939141 | 0.0094009854 | 0.0071698 | 4.857e-07 |
| (0, 1, 1) | 0.17299448 | 0.087037427 | 0.0470364 | 0.000583334 |
| (0.25, 0, 0) | 0.20083897 | 0.00380921 | 0.00161639 | 1.56219e-06 |
| (0.25, 0.5, 0.5) | 0.19316673 | 0.036406466 | 0.0246034 | 0.000149743 |

The last two columns are absolute density-equation defects, not relative
errors in \(R\) and not errors of a newly solved evolution. Across all
17 tested cases, the potential defect improved by at least **15.2-fold**
and the density defect by at least **30.1-fold** over omitting \(Q\).
The best ratios should not be overinterpreted: a leading coefficient can
nearly cancel at a particular point. Centers 2 and 3 were not used in the
initial scouting, but this remains one implementation and a sparse pilot.

Numerical audit:

- The algebraic potential and density residuals were below \(4\cdot10^{-15}\).
  These test jet algebra and averaging bookkeeping, not source accuracy.
- Changing the source quadrature from 160 to 224 nodes changed the sampled
  density by at most \(3.9\cdot10^{-12}\), and \(\Delta Q\) by at most
  \(4.4\cdot10^{-10}\), at the original filter order.
- The first 20-to-28 filter refinement failed the \(10^{-7}\) target for
  \(\Delta Q\) in the wide-window, half-regulator case: the change was
  \(6.63\cdot10^{-5}\). Refining that case to 40 nodes reduced the next
  change to \(1.84\cdot10^{-8}\). This failure and repair remain in the record.
- Finite-difference steps 0.02 and 0.01 were insufficient for several small
  defects. Steps 0.005 and 0.0025 were added. The change between the two
  finest Richardson density-defect estimates was at most
  \(6.5\cdot10^{-9}\); every case met the contract's diagnostic target.
  The analytic/finite-difference \(\Delta Q\) discrepancy was at most
  \(1.26\cdot10^{-8}\), or \(5.1\cdot10^{-10}\) after division by \(8\pi\).
  The separate current residual was below \(3.4\cdot10^{-10}\).

Refinement differences are diagnostics, not rigorous error bounds. The
cutoff and theta-tail error were not enclosed with interval arithmetic.
The pilot does not certify a continuous box, a long-time trajectory,
regulator removal or a large population of zeros. In particular, these
modest widths should not be described as many-period coarse averaging.

## 4. Control screen and interpretation

The exact heat polynomial \(H=z^2-2t\) has a double event at \((0,0)\).
Its centered spacetime windows around \((0,0.2,0.1)\), with halfwidths
0.2, 0.1 and 0.05 and \(\epsilon=1\), check (1), (5), (6) and current
consistency. The largest window includes the event. All exact identities
continue to hold; no collision exclusion follows. The potential closure
error decreases with shrinking widths, as expected. The polynomial fails
the unchanged theta-source premise. The exact cosh example in Note 02
still excludes only a correction forced to vanish whenever density
variance vanishes.

Apply the repository's [collision-control screen][controls]: the
Euler-factor sources alter the canonical arithmetic data; the weighted
square sources alter its weights and full reflection; the reflected
super-Gaussian and primitive-compatible shape constructions do not have
the unchanged theta square expansion. Our generic smooth-filter identity
and local Taylor expansion are allowed to hold for every such control,
including at its collision. They do not use the theta-only premise to
exclude anything. Their old certificates were not rerun in this round.

The quantitative output is limited to the stated defects on the stated
samples. The [status rule][status] and [scoped-exclusion rule][scope]
apply. A next closure test should increase averaging scale relative to
the regulator layer and period, with a new accuracy contract. The
[whole-period model and time-limit note][limits] gives a separate route
for that regime; extrapolating (1) without a scale condition is unjustified.

[contract]: 03_FIRST_BOUNDED_AVERAGING_CONTRACT_20261024.md
[identities]: 02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md
[limits]: 05_ASYMPTOTIC_MEAN_SHAPES_AND_FLUCTUATIONS_20261024.md
[script]: ../numerics/averaged_theta_round1.py
[data]: ../numerics/AVERAGED_THETA_ROUND1_20261024.json
[refs]: ../references/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[status]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
