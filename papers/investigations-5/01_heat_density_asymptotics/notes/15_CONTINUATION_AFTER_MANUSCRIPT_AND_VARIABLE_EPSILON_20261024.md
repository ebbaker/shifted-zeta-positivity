# Continuation after the analytical manuscript and variable epsilon

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Continuation pointer:** superseded by [Note 17](17_CONTINUATION_AFTER_ADAPTIVE_TRANSPORT_20261024.md); the original checkpoint below is retained.

**Original handoff.** This supersedes [Note 13][old] as the continuation
entry point. The author requested a manuscript of the analytical results,
numerics as supporting material, then an investigation of epsilon varying
with height and time, and finally this handoff. Those bounded deliverables
are now saved. The larger boundary-evolution program remains unfinished.

## Read first and preserve the workflow

Read repository AGENTS.md, LARGE_FILES.md, REFERENCE_WORKFLOW.md and
tools/CHAT_HISTORY.md. Read the [result index][results], especially
[heat geometry][geometry] and [collision controls][controls], alongside
the [avoid index][avoid], particularly [normalization][a08],
[scope][a07] and [evidence/status][a06].

Then read:

1. The [manuscript guide][guide] and [main LaTeX source][manuscript].
2. The [variable-epsilon note][variable], especially VE4--VE17 and
   the fully explicit positive-time prescription VE32--VE34.
3. The [same-assistant assessment][review] and [sole progress ledger][progress].
4. [Notes 11][negative] and [12][positive] for the complete constants
   underlying the manuscript.

Do not edit synced project sources or generated AGENTS files. Save new
derivations in notes, computations and small records in numerics, reviews
in reviews. Maintain the one manuscript directory and concise DRAFT_HISTORY;
do not create dated manuscript snapshot folders.

## Manuscript deliverable

The maintained draft is titled *Averaged densities for the theta heat
flow: two time limits and growing zero populations*, drafted for Edward
Baker with an explicit LLM acknowledgment. It is 15 pages in the checked
export. The main text presents analytical statements and proofs; Appendix C
contains the earlier floating observations and their limitations.
Specific notes and sibling saddle/pair-matrix inputs are cited.

The generated PDF is in the repository's ignored output tree:

    output/pdf/heat_density_asymptotics/heat_density_asymptotics.pdf

From the investigation folder, build it with python3 -B manuscript/build.py.
From another working directory, invoke that script by its absolute path;
it determines the repository root from its own location.
The [build record][build] identifies the sources/export and layout checks.
The editor compiler also succeeded. There are no tracked generated PDFs
or manuscript snapshot folders. No commit was created during this turn.

The draft consolidates the fixed-epsilon results through Note 12.
The subsequent adaptive-regulator results are a separate Note 14, in the
sequence the author requested. A future expansion of the manuscript
should import them explicitly, without silently changing its definitions.

## Earlier analytical results to retain

- At t=-T and fixed epsilon, the exact Gaussian density of
  G_T=Phi(0)sqrt(pi)/(2sqrt(T)) exp(-z^2/(4T)) has explicit O(T^-3)
  absolute error for every real x and |y|<=A sqrt(T).
  Its T^2 rho diffusive stationary profile has O(T^-1) error.
- At positive time, L solves 4pi exp(4L)=2tL+9 and
  kappa=8tL-2t+36. On buffered windows X~kappa^(1/3), the coarse
  physical density is L k_h/pi+O(kappa^-1/2+L^-3).
  The physical intensity grows; pi R/L is the stationary shape.
- Consecutive blocks of size m<=O(L kappa^(1/3)) have squared
  Vandermonde asymptotic
  (pi/L)^(m(m-1)) product_(k=1)^(m-1)(k!)^2, with an explicit
  logarithmic error tending to zero. The signed source-mean error
  O(kappa^-3/4) pays the growing block's scale change. Pair matrices
  satisfy dimension-uniform quadratic-form comparisons.
- At fixed epsilon, a nonzero clock limit cannot be uniform over all
  real heights for the stated escaping-window class. The separate
  xi-derivative hierarchy provides an all-height absolute budget, at
  a conservative degree O(t log^2 t). It has not been evaluated at the
  large degrees in the example.
- Slice density/determinant bounds do not pay a time derivative,
  the exterior zero force, moving normalization, or a reduced PDE's
  stability. The earlier records retain failed finite gates and
  refinement attempts. Do not rerun them without a new purpose.

## New variable-epsilon results

Set q=epsilon^2, r=log q, w=q/(|H|^2+q), S=log(|H|^2+q), and retain
the positive algebraic density rho=q|H_z|^2/[pi(|H|^2+q)^2].

1. The potential forcing is
   B_epsilon=[q_t+(q_xx-q_yy)/2]/(|H|^2+q).
   For epsilon(t,x), its numerator is
   2 epsilon epsilon_t+epsilon epsilon_xx+epsilon_x^2.
2. Spatial variation also gives Delta S/(4pi)=rho+C_epsilon.
   The correction has the divergence form
   4pi C_epsilon=2 div(w grad r)-w Delta r-w(1-w)|grad r|^2.
   The curvature density can be negative. A zero-free Gaussian example
   verifies this explicitly, so it must not be used interchangeably with rho.
3. The exact current source is
   rho_t+div j=(1-2w)(r_t rho+grad r dot j).
   Note 14 gives the fixed-filter equations, including both curvature
   correction derivatives, and separately lists moving-filter commutators.
4. For a compact C^2 test kernel psi, the weak error is at most
   K_r(psi)/(4pi) times the integral of log(1+q/|H|^2), where
   K_r=||Delta psi||+2||grad r||||grad psi||
   +(||Delta r||+||grad r||^2)||psi||.
   The earlier disk/floor bias bounds apply with epsilon_max.
   Local multiplicity-sensitive regulator removal rates are retained.
5. At negative time choose epsilon=eta Phi(0)sqrt(pi)/(2sqrt(T)).
   Now T rho, rather than T^2 rho, has a stationary diffusive profile,
   with O(T^-1) error uniformly over all real scaled heights.
   Its exact potential forcing is w/T.
6. For positive time a completely explicit starting prescription is

   epsilon_sad(t,x)=M_0(t) kappa(t)^(-1) exp[-x^2/(2kappa(t))],

   where M_0=2pi^2 exp(q_t(L)) sqrt(2pi/kappa) and
   q_t(u)=tu^2+9u-pi exp(4u).
   This source exponent q_t is distinct from the regulator square q.
   Its regulator bias is O(kappa^-1); the total inner density error
   remains O(kappa^-1/2+L^-3).
   More generally a fixed exponent p>=3/4 in place of 1 preserves
   that rate. This follows from complete-source bounds, not fitted roots.
   The explicit temporal and spatial forcing is in VE33--VE34.

The formula for epsilon_sad is defined beyond the proved window, but its
density error theorem is not. The fixed-epsilon obstruction no longer
applies to a regulator vanishing with height; this does not establish
global clock convergence. A naive envelope match can create an
unbounded background even for a zero-free field.

The [exact script][script] uses rational-coefficient polynomials and the
Python standard library. All 16 cleared identities pass on H=z^2-2t
for constant, time-only, height/time and full space/time regulators.
The [small record][record] includes exact Gaussian coefficients.
These are algebraic controls, not theta interval certificates or an
independent review.

## Next bounded investigation

A useful next choice is the explicit p=1 saddle regulator and the same
fixed compact spatial kernels. Derive a quantitative bound for its
averaged current source and forcing, keeping the near-zero layer and
the correlations with w. The leading r_t includes 2L^2, so static
regulator bias alone does not make the forcing small.
Combine that with a differentiated source/carrier estimate before
claiming an approximate evolution or choosing boundary data.

The complementary task is a positive-time outer-height approximation
for this explicitly chosen regulator through the amplitude turnover.
That requires a new complete complex-saddle estimate; merely extending
the formula beyond X~kappa^(1/3) is not evidence.
If using a published high-height result, inspect its full hypotheses:
the Polymath item in this investigation was only metadata/abstract-checked
in the earlier round.

HDA-02--06 remain partial, HDA-07--09 gated.
HDA-10 (manuscript) and HDA-11 (bounded adaptive-regulator investigation)
are complete at the recorded scope. Independent review and certified
finite source-onset data remain open. No RH or endpoint-simplicity
conclusion is an acceptance target.

## Chat identity and continuation records

This is chat **0002**, actual thread
01a16fb7-14ae-7d23-a933-972eca16a782, title
**Continue heat density investigation**. It has one canonical registration
in this investigation's chat-histories folder; 0001 remains separate.
Use the repository history tool at the beginning and end of each reply,
and the bounded exact-current-turn deferred capture as the last tool
action until trusted native-hook activation is verified. Read current
hashes/counts from the registry; never hand-edit the generated transcript
or prewrite an unsent final answer. A new chat gets its own actual identity.

The requested records have been saved in the research checkout, not in
the synced project mirror. Existing unrelated working-tree changes are
preserved. The next chat should continue from these sources rather than
reconstruct the mathematics from the conversation alone.

[old]: 13_CONTINUATION_AFTER_TWO_TIME_LIMITS_20261024.md
[guide]: ../manuscript/README.md
[manuscript]: ../manuscript/main.tex
[build]: ../manuscript/BUILD_RECORD_20261024.json
[variable]: 14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[negative]: 11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md
[positive]: 12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[review]: ../reviews/04_MANUSCRIPT_AND_VARIABLE_EPSILON_SELF_REVIEW_20261024.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[script]: ../numerics/variable_epsilon_identity_checks.py
[record]: ../numerics/VARIABLE_EPSILON_IDENTITIES_20261024.json
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a08]: ../../../../avoid/08_normalization_and_constant_slips.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a06]: ../../../../avoid/06_status_stronger_than_the_evidence.md
