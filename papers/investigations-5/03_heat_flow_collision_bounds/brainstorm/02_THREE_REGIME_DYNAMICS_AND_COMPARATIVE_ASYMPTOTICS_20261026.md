# Three heat-flow regimes: conditional dynamics and comparative asymptotics

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Thread `01a17b22-e902-7773-ad5a-14022601a13a`,
“Summarize heat-flow collision bounds,” chat0002.

**Status: exploratory research synthesis and proposed work sequence.**
The author proposes returning to Investigation01's description of the
equations across time and height, now conditioning on three possible zero
geometries. The elementary deductions below organize inherited heat
splitting and weak-density facts. They are not a new canonical arithmetic
estimate, a uniform asymptotic theorem, or evidence selecting a regime.
Checking is by this assistant only; no numerical or symbolic research
execution, independent review, manuscript change or live-task update
occurred.

## 1. The organizing question

Keep the one canonical solution

\[
H_t=-H_{zz},\qquad H(0,z)=\xi((1+iz)/2)/8.
\]

Consider three mutually exclusive hypotheses about it:

1. \(\Lambda>0\).
2. \(\Lambda=0\), with at least one multiple zero at time zero.
3. \(\Lambda=0\), with all time-zero zeros simple.

They constrain the same source and equations; they are not independently
chosen initial data. The proposed change is to derive the conditional
behavior of density, potential, current and fluctuations first, and then
ask which quantitative features can be estimated from the complete theta
source. A useful outcome can be a response law or a multiplicity-density
bound well before a theorem excluding every event.

Investigation01 supplies field approximations and exact observable
equations. Investigation02 supplies endpoint geometry and implications.
Investigation03 supplies concrete lessons about counts, enclosing walls,
resolution and transfer losses. Its P/J inequalities remain possible
applications; they need not determine the first exploratory observable.

## 2. The conditional dynamical picture

| Hypothesis | Behavior at the relevant endpoint | What a comparison must retain |
| --- | --- | --- |
| \(\Lambda=T>0\) | There are nonreal zeros at time zero. The existing canonical reduction gives a finite multiple event at time T. Just below T, that event has nonreal descendants; above T all zeros are real and simple. | The position of T, its finite exceptional region, and the shifted source. A later high-height clock does not exclude the earlier event. |
| \(\Lambda=0\), some multiple zeros | All endpoint zeros are real. A multiple site has nonreal descendants immediately below zero and real simple descendants above it, with square-root splitting. | Local multiplicities and their distribution over height. A finite or sparse exceptional set can be invisible to normalized bulk averages. |
| \(\Lambda=0\), all simple | Every fixed bounded complex region is free of nonreal zeros for sufficiently small negative time. Nevertheless nonreal zeros exist somewhere at every negative time. | The moving region in which those zeros occur and the deterioration of compact stability as its size grows. Simplicity alone gives no rate. |

The last observation is already recorded in [02's simplicity review][simple].
For completeness, enclose a fixed compact set in a slightly larger domain
whose boundary has no time-zero zeros. There are finitely many zeros
inside. Each simple real zero continues uniquely and remains real by
conjugation; the complement stays zero-free by compactness. A common
short time interval works for that domain. It need not work for every
domain simultaneously.

In regime 3 define

\[
R_*(s)=\inf\{|z|:H(-s,z)=0,\ \Im z\ne0\},\qquad s>0.
\]

The threshold property ensures the set is nonempty. Compact stability
implies \(R_*(s)\to\infty\) as \(s\downarrow0\). This is a qualitative
consequence, with no asserted rate or monotonicity. It uses complex radius;
turning it into a horizontal-height statement needs the relevant transverse
confinement. On any prescribed bounded transverse strip, compact stability
does exclude nonreal zeros in every fixed horizontal window eventually.

By contrast, in regime 2 a window containing a multiple endpoint retains
nonreal descendants for all sufficiently small s. In regime 1 a window
containing a nonreal time-zero zero has a nonzero transverse contribution
already at zero. Thus finite-location disappearance and escape beyond
every compact set are distinct dynamical mechanisms.

## 3. A descriptive weak moment, before asking for an exclusion bound

Choose a fixed nonnegative smooth compact cutoff \(\chi\), and count zeros
with multiplicity. Set

\[
Y_\chi(s)=\sum_{H(-s,z)=0}\chi(z)(\Im z)^2.
\]

Only finitely many zeros contribute. The inherited Hermite splitting at a
real endpoint a of multiplicity m is

\[
z_j(-s)=a+i\sqrt{2s}\lambda_j+O(s),\qquad
\sum_{j=1}^m\lambda_j^2=m(m-1).
\]

It gives, in either RH regime and for this fixed cutoff,

\[
Y_\chi(s)=2s\sum_{H(0,a)=0}\chi(a)m_a(m_a-1)+o(s).
\tag{1}
\]

This is the existing V moment interpreted as a conditional response law,
rather than immediately demanding a favorable upper bound for it.
The three predictions have precise window qualifications:

- Regime 1: a cutoff seeing an off-axis time-zero zero has
  \(Y_\chi(s)\to Y_\chi(0)>0\), by continuity of the local zero measure.
- Regime 2: a cutoff positive at a multiple endpoint has
  \(Y_\chi(s)=c_\chi s+o(s)\), with \(c_\chi>0\).
- Regime 3: for every fixed compact cutoff,
  \(Y_\chi(s)=0\) for all sufficiently small s, depending on that cutoff.

For a complete finite window with buffered boundaries and weight one at
its endpoint sites, put

\[
N_R=\sum_a m_a,\qquad M_R=\sum_a m_a(m_a-1).
\]

Then (1) reads \(\lim_{s\downarrow0}Y_R(s)/(2s)=M_R\). The corresponding
inherited ordered positive-time energy law is
\(\lim_{t\downarrow0}tE_R(t)=M_R/8\). These measure the same multiplicity
weight through two different responses; neither coefficient has been
estimated favorably for the canonical field here.

The author's percentage suggestion fits this description. A positive
fraction of zero labels belonging to multiple sites forces a positive
lower bound for \(M_R/N_R\). A single fixed multiple zero contributes
positive absolute mass but vanishes after normalization by an increasing
N_R. With unbounded multiplicity, the weighted ratio, rather than just
the fraction of distinct sites, is the appropriate statistic. A bound
excluding a positive proportion would be a useful result even if sparse
multiple zeros remained possible.

The order of limits is essential: (1) fixes the window before taking
\(s\downarrow0\). It does not justify substituting a growing \(R=R(s)\),
or taking the high-height limit first. Those are proposed research tasks.

## 4. What can imitate a multiple-zero response

The exact two-root heat field

\[
F(t,z)=z^2-a^2-2t,\qquad a>0,
\]

has simple time-zero roots, yet its full negative-time moment is

\[
Y(s)=4(s-a^2/2)_+.
\tag{2}
\]

For fixed a it is eventually zero. If a varies with the observation
scale and \(a^2\ll s\), it is almost \(4s\), the double-zero response.
This control has negative threshold and is not a canonical example of
regime 3. It demonstrates the local resolution problem: simplicity alone
does not provide uniform rates over a family of arbitrarily close pairs.
A growing-window law must therefore retain the distribution of small
nonzero gaps and cluster interactions, as well as exact multiplicities.

Other established comparisons are also relevant. [BW10 Note22][profile]
already proves a quantitative heat-scale profile and shows that its
leading term is universal at a fixed multiplicity. [HDC Note18][allmultiple]
constructs a positive-source control with no simple endpoint zeros and
the same coarse counting law and fixed-offset estimates. Thus even a
large multiple-zero population need not change a leading one-point
counting asymptotic. Transverse response, correlations, or subleading
terms are better candidates than count alone.

## 5. Connecting this to Investigation01's equations

The Book retains the actual potential U, density R, current J and signed
covariance Q. In particular Q is the filtered difference of gradient
variances, not a freely selectable closure. The equations, regulator
terms and joining defects in [Book Section5][physical] remain the starting
point for a conditional comparison.

There is a concrete limitation in the existing physical prescription.
Near time zero its regulator is positive and independent of height, and
its spatial filter widths are fixed. Its documented tail law is
\(R_H/\log X\to0\) for every fixed \(t\le64\). The transition at64 is
created by the prescribed regulator; it is not the Newman threshold.
The existing global approximation can therefore be accurate while its
leading observable suppresses the distinctions under discussion.

Keep that original tuple intact and study a separately specified family
of diagnostics with controlled resolution. For example, with one fixed
nonzero normalization A and auxiliary constant regulator \(\eta>0\),

\[
\rho_\eta=\frac{\eta^2|(H/A)_z|^2}
 {\pi(|H/A|^2+\eta^2)^2},\qquad
Y_{\chi,\eta}(s)=\frac1{4\pi}\int
 \log(|H(-s,z)/A|^2+\eta^2)\,
 \Delta[\chi(z)(\Im z)^2],dA(z).
\]

At each fixed s, regulator removal gives Y_chi. This uses the inherited
weak potential identity and is compatible with Investigation01's method
of evaluating smooth primitives instead of sampling narrow peaks. It
does not identify the auxiliary diagnostic with the original physical R.
For normalized field error delta on the fixed support, the sufficient
transfer allowance is

\[
|\Delta Y_{\chi,\eta}|
\le\frac{\|\Delta(\chi y^2)\|_1}{4\pi}\frac{\delta}{\eta}.
\tag{3}
\]

To resolve the linear response with this estimate requires
\(\delta/\eta=o(s)\), as well as an independently controlled regulator
bias. Neither an arbitrarily small regulator nor the required accuracy
is supplied for free. Moving tests change their derivative norms; moving
filters introduce their own evolution terms.

One useful local calibration makes the solution-profile idea explicit.
At a fixed real event (T,a) of order m, put
\(c=\partial_z^m H(T,a)/m!\ne0\), \(t=T+\sigma s\),
\(z=a+\sqrt{s}\zeta\), and

\[
P_m(\sigma,\zeta)=e^{-\sigma\partial_\zeta^2}\zeta^m.
\]

Taylor expansion using the heat equation gives

\[
H(T+\sigma s,a+\sqrt{s}\zeta)
=c s^{m/2}\{P_m(\sigma,\zeta)+O(\sqrt{s})\}.
\tag{4}
\]

The remainder and its spatial derivatives are uniform on fixed bounded
scaled sets, with event-dependent constants. For the auxiliary density
formed directly from H, choose
\(\eta_s=|c|s^{m/2}\varepsilon\), fixing \(\varepsilon>0\) during the
limit. Then

\[
s\rho_{\eta_s}(T+\sigma s,a+\sqrt{s}\zeta)
\longrightarrow
\frac{\varepsilon^2|\partial_\zeta P_m|^2}
 {\pi(|P_m|^2+\varepsilon^2)^2}.
\tag{5}
\]

The same field supplies the corresponding current and covariance; their
full means must be retained. Equations (4)-(5) are elementary local
calibrations, not a new all-height theorem. They expose the regulator
scale needed to resolve an event and the dependence on the actual local
coefficient c. A canonical source approximation must resolve that scale.
Their leading profiles are universal, so source-dependent corrections,
population statistics and global matching are where new discrimination
would have to enter.

## 6. A comparative asymptotic program

| Stage | Concrete output | What would constitute a gain |
| --- | --- | --- |
| Conditional atlas | For each regime, map negative time, the neighborhood of zero, any positive threshold, and the large-positive region; specify height, transverse width, regulator and averaging scale together. | Identify an actual response coefficient, exponent, support/escape constraint or controlled difference, rather than only relabeling an endpoint test. |
| Local-to-averaged response | Extend the finite-window law to weighted height windows, with explicit dependence on multiplicities, small gaps, exterior interactions and boundary flux. | A uniform remainder under stated quantitative population assumptions, or an exact explanation of the scale at which a proposed average loses the signal. |
| Moving-window analysis | Study the region containing nonreal zeros as time approaches zero, and compare fixed-window limits with joint time/height limits. | A source-derived rate or distributional bound; qualitative escape alone is an inherited consequence of regime3. |
| Equation comparison | Insert the conditional models into the exact U/R/J/Q system and compare their complete terms with the retained-arithmetic field formulas. | A new canonical estimate for a regime-dependent term, or a rigorously narrower class of possible responses. Q is computed from H, not selected to enforce a preferred regime. |

Remote-time and fixed-positive-time high-height formulas remain useful
boundary/matching information. They need not have distinct leading terms
in the three regimes. Polymath's positive-time theorem already permits
regular high zeros beyond a time-dependent onset without RH. The more
promising comparison is therefore joint time, height and resolution,
including exceptional regions and subleading response.

**Suggested first bounded task:** develop a complete weak-potential
response comparison on a declared family of windows. Start from (1),
retain the close-pair calibration (2), quantify both regulator bias and
source transfer (3), and identify exactly which assumptions permit the
window to grow. Return a quantitative response/error theorem or a scoped
failure before selecting a numerical campaign. This starts with
conditional solution behavior and can support a positive-proportion
result, a sparse-event statistic, or a later P/J/V/E application.

## 7. Controls, provenance and limits

The screening here is analytical against the existing records; no control
certificate was rerun. Hermite polynomials satisfy the local laws exactly
and lack the complete theta source. The translated quadratic
\(z^2-2(t-T)\) realizes a positive-threshold local model, while (2)
tests resolution of simple pairs. Positive atomic and theta-close
endpoint controls retain genuine multiple events and the same leading
profiles; they fail the original normalized theta arithmetic. Euler-factor
controls change the coefficients/completion; their applicable all-real
premises must be checked at the specified parameter. Weighted-square and
finite-tail controls do not supply the all-real interval used for an RH
population argument. Reflected, smooth/positive-primitive, finite-prime
and finite-profile controls retain only their named structural data and
do not supply the full unchanged canonical source. The HDC all-multiple
control actually passes the coarse count/wall estimates, so absence of
the theta identity is not itself an acquired distinguishing inequality.

The [result index][results], [heat-flow cluster][heat],
[local-geometry cluster][geometry], [control cluster][controls] and
[avoid index][avoid] apply. In particular, this proposal follows
[target classification][classification] and the [control requirement][screen]:
the three-regime taxonomy and exact local signatures are descriptions
and diagnostics, not evidence that a regime is impossible. No new
all-height rate, favorable sign, multiplicity proportion, global
contradiction or scientific-status upgrade is claimed.

Primary local inputs are [01's unified overview][overview],
[Book canonical atlas][canonical], [Book physical equations][physical],
[Summary76][summary76], [02's positive-threshold analysis][threshold],
[02's simplicity review][simple], [J/P/V/E specifications][targets],
[03's handoff][handoff], [BW10's profile comparison][profile] and
[HDC's all-multiple control][allmultiple].
Primary-source spot checks used [Rodgers–Tao v5][rt] for the threshold
classification and [Polymath v2][poly], Proposition3.1 and Theorem1.5,
for local splitting and positive-time high zeros. These sources already
belong to the repository reference workflow; no new PDF was downloaded.

This note and [the earlier synthesis](01_HIGH_LEVEL_PROGRESS_AND_STRATEGIES_20261026.md)
remain in the requested brainstorm folder. The sole
[chat0002 archive](../chat-histories/0002_2026-10-27T02-14-07Z_summarize-heat-flow-collision-bounds.json)
continues under its existing identity.

[overview]: ../../01_heat_density_asymptotics/research-overview/02_BOOK_UNIFIED_HEAT_FLOW_RESEARCH_OVERVIEW_20261026.md
[canonical]: ../../01_heat_density_asymptotics/book/sections/01_canonical.tex
[physical]: ../../01_heat_density_asymptotics/book/sections/05_physical.tex
[summary76]: ../../01_heat_density_asymptotics/notes/76_CHAT0028_RESEARCH_SUMMARY_20261026.md
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[simple]: ../../02_heat_flow_rh_applications/rh_simple_zeros/notes/01_RODGERS_TAO_REVIEW_AND_RH_SIMPLICITY_20261026.md
[targets]: ../../02_heat_flow_rh_applications/rh_simple_zeros/notes/02_TARGET_BOUNDS_FOR_RH_TO_SIMPLICITY_20261026.md
[handoff]: ../notes/08_CHAT0001_RESULTS_AND_HANDOFF_20261026.md
[profile]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[allmultiple]: ../../../investigations-4/12_height_dependent_heat_contours/brainstorm/notes/18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md
[results]: ../../../../result-summaries/README.md
[heat]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classification]: ../../../../avoid/01_restating_the_target.md
[screen]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[rt]: https://arxiv.org/abs/1801.05914v5
[poly]: https://arxiv.org/html/1904.12438v2

## New investigation home

26 October 2026 — At Edward Baker’s request, this proposal now has its own
[Investigation04 overview](../../04_three_regime_heat_flow_dynamics/research-overview/01_THREE_REGIME_DYNAMICS_RESEARCH_OVERVIEW_20261026.md)
and [TRD progress register](../../04_three_regime_heat_flow_dynamics/research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md).
This brainstorm remains the founding analysis; the unique chat0002 history
continues at its existing location. The new program also incorporates the
[Dobner functional-approximation comparison](../../04_three_regime_heat_flow_dynamics/references/01_DOBNER_FUNCTIONAL_APPROXIMATION_20261026.md).
Prepared with substantial LLM assistance, **gpt-6-astra, actual effort max**.
