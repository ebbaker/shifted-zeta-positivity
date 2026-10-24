# Analytical manuscript integration and a determinant refinement

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified in the current session metadata.

**Status: maintained analytical manuscript revised; same-assistant review
only.** The author requested inclusion of the new work, analytical emphasis,
brief numerical support and references to notes, and authorized rewriting
the background and other sections. This note records that integration and
one immediate quantitative consequence. It is not a new all-time theorem.

Read the [result index][results], especially [heat geometry][geometry] and
[collision controls][controls], and the [avoid index][avoid], especially
[status][status] and [scope][scope]. This is an approximation/write-up
milestone under [target classification][classification].

## 1. One maintained argument

The [manuscript][main] is now titled **Averaged densities for the theta heat
flow: explicit asymptotics and finite-time approximation**. Its background
explains why a density approximation needs independent differentiated
transport and covariance estimates. It retains the canonical normalization,
physical amplitude and the earlier fixed-regulator proofs.

- Section 1 includes the exact variable-regulator potential forcing,
  curvature correction and current source from Note 14. Both derivatives
  of the curvature correction remain in the density equation.
- Section 2 includes the adaptive negative T-rho profile as well as the
  original fixed-regulator T^2-rho profile.
- Section 4 gives the complete-source score proof, exact finite Bernoulli
  phase representation, differentiated carrier cancellation, weak current
  and regulator transfer, and the final explicit density/current theorem.
  Longer finite moment allowances are referenced to Note 16.
- Sections 5--6 retain determinant/pair-matrix results, the scoped
  fixed-regulator obstruction and the global xi-derivative hierarchy.
- Section 7 gives the global regulator, finite error-function source field,
  complete jet budgets, nonlinear density/current/time stability, actual
  covariance and its Laplacian, and the fixed compact-source endpoint
  failure. Useful transition overlap is explicitly unfinished.

Three short appendix paragraphs summarize prior numerical support, exact
phase identities and floating checks, with note and execution-record
references. No numerical campaign was rerun for this editorial integration.
The author field says "Drafted for Edward Baker" and the acknowledgment
retains the actual model, effort and same-assistant review status.

## 2. A direct improvement to the existing determinant allowance

Let e_s^*=min(e_mu,e_s)=O(kappa^-1) be Note 19's mean allowance and let
eta_loc=s/pi=O(kappa^-1/2) be the unfolded root-location error. The original
Note 12 pairwise logarithm proof gives, unchanged except for its mean input,

\[
\left|\log\frac{\Delta_m(a)}{\Delta_m^{\rm clock}(L)}\right|
\le m(m-1)\frac{e_s^*}{L-e_s^*}
+\frac{4\eta_{\rm loc}}{1-2\eta_{\rm loc}}
\{mH_{m-1}-(m-1)\}.
\]

For m=O(L kappa^(1/3)), its first term is now
O(L kappa^-1/3), replacing O(L kappa^-1/12). The second remains
O(L log(kappa) kappa^-1/6). Hence the manuscript's total bound is

\[
O(L\kappa^{-1/3}+L\log\kappa\,\kappa^{-1/6})=o(1).
\]

This improves one term, not the dominant root-location order. It uses the
same eventual source/carrier gates and retains every exterior-force term.
It is derived from root locations; determinant closeness is not used to
infer every gap. Earlier Notes 12 and 19 retain their historical statements.

## 3. Scope and next step

The generic score and field-stability identities are compatible with
smooth colliding controls. Atomic and polynomial controls lack the smooth
canonical source assumptions; Euler-factor, weighted, reflected and
primitive controls cannot inherit the unchanged theta majorants. A
simple-root collar fails at a covered collision. The late-time results do
not discriminate earlier collisions. The compact-source failure excludes
only a fixed cutoff, not increasing source representations.

The manuscript states: "The construction proves approximability on each
compact slab." A useful all-time bridge additionally needs chosen
transition parameters, complete informative error and endpoint overlap.
Actual clock covariance, outer-height behavior, independent review and
certified onset remain open. HDA-10 is complete at this expanded manuscript
scope; HDA-02--06 and HDA-14 remain partial, and HDA-07--09 remain gated.

The next research task is still Note 20's finite transition slab and full
budget evaluation. The [review][review] and [build record][build] record
production checks separately from mathematical evidence. This revision
has no new manuscript snapshot or Git commit. Chat 0004 retains its unique
registration and is refreshed with the repository tool.

[main]: ../manuscript/main.tex
[review]: ../reviews/07_ANALYTICAL_MANUSCRIPT_INTEGRATION_SELF_REVIEW_20261024.md
[build]: ../manuscript/BUILD_RECORD_20261024.json
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[status]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[classification]: ../../../../avoid/01_restating_the_target.md
