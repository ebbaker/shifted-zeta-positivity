# Research program: asymptotics and evolution of averaged zero density

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**,
verified from this turn's metadata.

**Purpose.** Construct an unnormalized smoothed function that accurately
represents the average behavior of the zeros. Determine its asymptotic
values, derive the evolution it actually obeys with fluctuation corrections,
solve a compatible boundary problem, and refine those solutions against
the canonical heat field.

The [progress register][progress] is the sole task/status ledger.
The [opening brainstorm][opening] supplies candidate asymptotic models;
the [filtered-equation note][filtered] supplies the exact starting
identities. The [first-round continuation][round-one] now links a fixed
contract, local closure pilot, asymptotic covariance calculations and a
conditional regulator-bias bound. A uniform theta approximation and an
independently validated evolution closure remain open.

The [result index][results], especially [heat geometry][geometry] and
[collision controls][controls], and the [avoid index][avoid] apply.
This is a quantitative approximation milestone under
[target classification][a01]. Its useful output is a function, a domain,
averaging scales and an error budget. Generic identities alone do not
count as accuracy evidence.

## 1. The object and the comparison target

Retain the source manuscript's normalization:
\[
H_t=-H_{zz},\qquad
\rho_\epsilon=
\frac{\epsilon^2|H_z|^2}
{\pi(|H|^2+\epsilon^2)^2},\qquad \epsilon>0.
\]
The research function is
\[
R_{\epsilon,\ell_x,\ell_y,\tau}=\mathcal F_{\ell_x,\ell_y,\tau}\rho_\epsilon,
\tag{P1}
\]
where \(\mathcal F\) is a positive, unit-weight spatial/time average.
No division by total density mass is made. The averaging can be spatial,
temporal, or both; the final choice and scale dependence are part of
the research.

To quantify how this represents zeros themselves, also define
\[
\nu_t=\sum_{H(t,a)=0}m_a\delta_a,\qquad
R_{\rm zeros}(t,z)=
\int k_\tau(s)\int K_{\ell_x,\ell_y}(z-a)\,d\nu_{t-s}(a)\,ds.
\tag{P2}
\]
Keep fixed positive spatial smoothing when using (P2) as a smooth
function, unless spatial regularity from time averaging alone is
separately proved. A time average of moving point measures can remain
spatially singular.

The book's compact measure limit motivates (P2), but a quantitative
regulator-bias bound
\(\|R_\epsilon-R_{\rm zeros}\|_X\le E_{\rm reg}\) must be obtained in the
chosen regime. In particular the fixed-\(\epsilon\), negative-time
\(T^{-3}\) density from the brainstorm can be regularization background
on a region with no zeros. Matching that term is not by itself a
description of a nonzero zero population.

The opening contract must specify the domain, kernels, scales, norm \(X\),
and limits being taken. Treat fixed regions, diffusive spatial scales,
and growing height/rank as distinct regimes. For centered time averages,
provide data on both sides of the observation time; for causal evolution,
choose a one-sided kernel and state its history data.

## 2. Determine asymptotic values and fluctuation scales together

At \(t=-T\to-\infty\), start from the Gaussian field and its differentiated
source expansion in [Note 01][opening]. Determine leading values and
corrections for \(R_\epsilon\), its required derivatives and its current,
with the spatial/time averaging widths retained. Compare the fixed-region
and \(z=\sqrt T\,\zeta\) regimes, and separate any regulator background
from the target zero measure.

At \(t\to+\infty\), start from the complete-source saddle and the
analytically averaged cosine slice. Determine the absolute mean
intensity, transverse shape and time trend, then pay the carrier,
source-tail and uniformity errors. Fixed finite root-label information
must not be silently promoted to growing-height averages.

For both signs of time, derive the asymptotics of the fluctuation term
below as well as the mean function. A term small in value can contribute
at leading order after the derivatives in the evolution equation.
Endpoint calculations must specify uniformity in the full averaging
buffer, and any joint order of \(t,\epsilon,\ell_x,\ell_y,\tau\) limits.

## 3. The exact evolution identifies what the closure must retain

Let
\[
U=\mathcal F\log(|H|^2+\epsilon^2),\quad
T_{ij}=\mathcal F(S_iS_j)-U_iU_j,\quad Q=T_{xx}-T_{yy},
\qquad S=\log(|H|^2+\epsilon^2).
\]
The [derivation][filtered] gives, for fixed filters and regulator,
\[
\boxed{
R_t=-\tfrac12(R_{xx}-R_{yy})
-\frac1{8\pi}\Delta\!\left(U_x^2-U_y^2+Q\right),
\qquad \Delta U=4\pi R.
} \tag{P3}
\]
The compatible potential equation is
\[
U_t=-\tfrac12(U_{xx}-U_{yy})
-\tfrac12(U_x^2-U_y^2+Q). \tag{P4}
\]
These are exact identities, not yet a usable closed model.

Local density fluctuations satisfy
\(\Delta(S-U)=4\pi(\rho_\epsilon-R)\). They affect \(Q\) through
gradient correlations, cross terms and unresolved harmonic data.
Use these relations to construct \(Q_{\rm model}\). A bare local
density variance need not supply the entire correction; Note 02 gives
an explicit control. Ordinary smoothing is not an idempotent ensemble
average, so its cross terms cannot be dropped without justification.

Study a hierarchy: first measure the exact correlations from the complete
field, then test a small closure using the mean density, potential and
selected fluctuation statistics, and add gradient, nonlocal or temporal
memory terms only when the errors require them. Do not assume \(Q\) has
a fixed sign or is lower order. If a density-only equation cannot close
at the requested accuracy, retain auxiliary fields.

In parallel use the independent current balance
\[
R_t+2\Re\partial_zJ=0,\qquad J=\mathcal F j.
\tag{P5}
\]
The modeled fluctuation contribution must agree with this transport and
its physical boundary flux.

## 4. Solve with compatible asymptotic and boundary data

Once the two asymptotic regimes and a usable closure have error budgets,
formulate a finite-domain problem whose boundary data approximate them.
Specify which fields and derivatives are prescribed on each boundary,
how the outer domains will grow, and the full averaging buffers.

Supply the boundary/harmonic information for \(U\), the source
normalization, and a compatible finite-time anchor or complete-source
constraint. The two leading time limits alone do not select theta:
the compact spectral perturbation in Note 01 preserves them while
changing the intermediate field.

Analyze existence, uniqueness or the remaining solution family for the
chosen approximate problem. Do not assume an ordinary forward
parabolic solver applies to (P3), or prescribe incompatible data at
both time ends. If several solutions remain, use actual source data
and evolution constraints to select among them.

Candidate implementations are source-compatible cosine quadrature on
bounded time slabs, matched Gaussian/saddle expansions, and a reduced
potential-density system with a controlled fluctuation closure. Preserve
positivity and reflection symmetries of \(R\), the absolute density scale,
and local mass/flux balances throughout.

## 5. Constrain and improve the solutions against the actual equations

Compare the candidate with independent complete-source calculations of
\(R,U,J,Q\), using the same averaging kernels and regulator. Refine the
solution family or closure using:

- The exact density/potential and averaged-current identities.
- Complete theta-source data and compatible spatial boundary traces.
- The two asymptotic value expansions and their derivative corrections.
- Measured density fluctuations and gradient/cross correlations.
- Symmetries, nonnegativity and unnormalized local mass balance.
- Time intervals, heights and averaging widths reserved from fitting.

Track the density residual in (P3), the potential constraint defect,
the closure discrepancy after its required derivatives, and boundary
and initial/anchor errors separately. A small PDE residual is not an
accuracy theorem: quantify how errors propagate in the chosen problem,
or label the comparison as numerical on its tested domain.

For a candidate \(R_{\rm model}\), the basic target decomposition is
\[
\|R_{\rm model}-R_{\rm zeros}\|_X
\le
\|R_{\rm model}-R_\epsilon\|_X
+\|R_\epsilon-R_{\rm zeros}\|_X.
\tag{P6}
\]
Bound or measure the first term through actual-field validation and
stability; bound the second through the regulator-to-divisor comparison.
Report all terms with the same domain, scale choices and norm.

## 6. Execution sequence and success conditions

1. **Define the comparison:** averaging, domain, regulator protocol and
   accuracy measures (HDA-01), plus the zero-measure bridge (HDA-02).
2. **Acquire the anchors:** negative and positive time values, derivatives
   and fluctuation scales (HDA-03–04); audit the exact filtered equations
   (HDA-05).
3. **Close the evolution:** approximate the required fluctuation
   correlations and quantify their contribution (HDA-06).
4. **Solve the boundary problem:** use paid asymptotics and compatible
   source data (HDA-07).
5. **Refine and validate:** constrain those solutions against the actual
   equations and independent averaged theta data (HDA-08), then review
   the deliverable (HDA-09).

The first successful result is a reproducible smoothed function or small
family of functions, with explicit averaging choices, asymptotic values,
fluctuation correction, boundary conditions and a stated error against
the true averaged zero behavior. It may be a bounded-domain numerical
result before a uniform analytic theorem.

Use the [opening control screen][opening] and Note 02's nonzero-covariance
control when choosing a closure. Generic exact evolution must work on
those controls; canonical asymptotic constants must use the actual
theta source. A failure is scoped to the tested model and regime under
[avoid 07][a07]. No simplicity or RH conclusion is an acceptance criterion.

Keep derivations in notes, computations and small records in numerics,
and assessments in reviews. Update the progress register after each
bounded research step, retaining incomplete dependencies and measured
errors. Record milestones in the investigation's history without new
manuscript snapshots.

[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[opening]: ../notes/01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md
[filtered]: ../notes/02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md

[round-one]: ../notes/07_CONTINUATION_FOR_NEW_CHAT_20261024.md
