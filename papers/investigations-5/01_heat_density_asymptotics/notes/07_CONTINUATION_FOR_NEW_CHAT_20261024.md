# Continuation for a new chat: averaged unnormalized heat density

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.


## Author's objective and current state

Continue investigation `papers/investigations-5/01_heat_density_asymptotics`
in `/Users/ebbaker/Documents/shifted-zeta-positivity`. The author wants the
**average shape of the unnormalized density**, allowing spatial averaging,
time averaging, or both. Determine both time limits and the correct
averaged evolution with local fluctuation contributions, then solve a
compatible boundary problem and refine it against the actual theta flow.
Do not switch to normalized probability densities, individual peaks or
root-coordinate fitting.

The first bounded round is complete. Its main results are:

- Fixed-region, fixed-regulator negative-time mean R is of order T^-3.
  With equal independent spatial variances v, Q first appears at T^-5;
  its coefficient includes the spatial fourth moment. Source-anchored U
  is available through T^-3. The leading density correction is captured
  by the local gradient closure even when its leading potential correction
  differs by a spatial constant.
- The complete-period cosine model has explicit U, R and Q. Additional
  transverse/time smoothing needs a further variance correction. This
  gives a smooth mean-shape model with matching covariance, but its
  positive-time transfer to theta remains open.
- A moment-based small-window closure improved potential and density
  consistency defects by at least 15.2-fold and 30.1-fold, respectively,
  over omitting Q in 17 floating theta samples. These are defects on
  source-derived mean fields, not errors of an evolved reduced solution.
- An explicit logarithmic-potential bound connects spatially smoothed
  regularized density to smoothed zero counts. The theta lower-bound
  constants and temporal uniformity have not been paid.

No boundary-matched solution, uniform theta approximation, independent
review, interval certificate or RH/simplicity result has been obtained.

## Read these first; do not restart the opening work

1. Repository `AGENTS.md`, `LARGE_FILES.md`, `REFERENCE_WORKFLOW.md` and
   `tools/CHAT_HISTORY.md`.
2. [Result summaries][results], especially [heat geometry][geometry] and
   [collision controls][controls]; [avoid index][avoid], especially
   [target restatement][a01], [shape-only arguments][a02],
   [status stronger than evidence][a06], [scoped exclusions][a07] and
   [unchecked imports][a16]. Keep their original status words.
3. The [sole progress ledger][progress] and [overview][overview].
4. [Note 02: exact averaged evolution][identities],
   [Note 03: bounded contract][contract],
   [Note 04: local closure and theta comparisons][closure],
   [Note 05: both time-limit models and covariance][limits], and
   [Note 06: regulator bias][regulator].
5. [First-round same-assistant assessment][review] and
   [numerical guide][numerics].

The source is the current working-tree
`papers/investigations-4/12_height_dependent_heat_contours/manuscript/book.tex`.
It is concurrently modified by other work; do not edit or reset it for
this investigation. The opening note records its earlier inspected hash.
The repo has unrelated changes outside this investigation. Preserve them.
No commit was made for this round, and no manuscript snapshot was created.

## Exact conventions to preserve

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\qquad H_t=-H_{zz},
\]
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\quad H(0,z)=\xi(1/2+iz/2)/8.
\]
Set \(D=|H|^2+\epsilon^2\), \(S=\log D\),
\(\rho=\epsilon^2|H_z|^2/(\pi D^2)\), \(U=\mathcal F S\),
\(R=\mathcal F\rho\), and
\(Q=\mathcal F(S_x^2-S_y^2)-(U_x^2-U_y^2)\). Then
\[
U_t=-\tfrac12(U_{xx}-U_{yy}+U_x^2-U_y^2+Q),\quad
R=\Delta U/(4\pi),
\]
\[
R_t=-\tfrac12(R_{xx}-R_{yy})
     -\tfrac1{8\pi}\Delta(U_x^2-U_y^2+Q).
\]
The compatible smooth current is
\(J=\mathcal F[\epsilon^2H_{zz}\overline{H_z}/(\pi D^2)]\), with
\(R_t+\partial_x\Re J+\partial_y\Im J=0\).
The density alone does not fix the harmonic/additive part of U.
The total theta density mass on the plane is infinite; keep local
windows and their boundary fluxes.

## Recommended next bounded research step

Advance **HDA-04/HDA-06**, alongside an actual **HDA-02** regulator check.
The main missing step is a quantitative coarse-average link to theta,
not another derivation of the already exact filtered equations.

1. Choose and write a new scale contract that averages over several real
   periods while preserving a finite transverse resolution. Declare a
   finite positive-time range, x/y buffer, fixed regulator and current
   or weak density error norm. Distinguish this from the small-window
   pilot. Do not quietly impose a normalized density or change epsilon
   with amplitude. If scales depend on time, derive their commutators.
2. Start from the positive complete-source representation
   \(H/H(t,0)=\mathbb E_t\cos(uz)\), using the probability measure
   proportional to \(e^{tu^2}\Phi(u)du\) only as a source-integral tool;
   the **target density remains unnormalized**. Source mean/variance and
   higher centered moments can bound a complex-field carrier approximation.
   The existing fixed-label saddle result does not give the required
   growing-number-of-periods or complex-buffer uniformity.
3. Compare period/coarse means using Note 05 (10) and the total-covariance
   rule (13). Keep both the phase-cell covariance and the extra variance
   from transverse/time averaging. Compare with the local gradient model
   only where its derivative bounds justify the scale. Evaluate the
   differentiated covariance or a declared weak counterpart.
4. Use Note 06 to pay a regulator-bias bound or a clearly scoped numerical
   convergence study. Prefer a logarithmic-potential/cluster estimate;
   do not resolve and fit individual peaks merely to represent the mean.
   Successive regulator differences are diagnostic, not by themselves
   a certified limit error. Near changing multiplicity, simple-zero
   lower bounds may fail to be uniform in time.
5. Keep boundary matching gated until asymptotic traces, source anchors,
   fluxes and residual propagation have quantitative budgets. A useful
   alternative bounded task is to compute explicit negative-time
   derivative remainder constants for Note 05, without repeating its
   coefficient algebra. The mixed-sign PDE has no established forward
   stability theorem here.

At large positive time, raw amplitudes can overflow and the fixed-regulator
layer can be far narrower than floating resolution. Use scaled source
integrals and log-potential/weak-average calculations with the original
normalization accounted for. Do not treat a failed raw density quadrature
as a mathematical obstruction. The current evaluator is scoped to the
recorded finite cases, not arbitrary large positive times.

## Numerical evidence and reproducibility

`numerics/averaged_theta_round1.py` uses Python 3 plus NumPy. The
small JSON record stores versions, script hash, all 17 samples,
quadrature refinements, finite-difference steps, negative-time checks,
12 cosine covariance checks and the colliding polynomial control.
The previous simple cosine-average script uses only the standard library.

The first-round filter is the product kernel
\(k(q)=315(1-q^2)^4/256\) on \([-1,1]\), with variance 1/11 and fourth
moment 3/143. Primary epsilon is 1e-4, with three sensitivity cases at
5e-5. Centers and widths are fully listed in Note 03. The baseline filter
orders are 20/28; the widest half-regulator case needed 40 nodes.
Source quadrature uses 160/224 nodes and eight theta summands.
Finite-difference steps extend to 0.0025. These are floating diagnostics,
not rigorous truncation bounds or an independent implementation.

Do not rerun the whole pilot just to reproduce the same status. Reuse
its record unless code changes, a failure, or the next mathematical
question requires a rerun. Keep large arrays and third-party PDFs outside
Git; catalog relevant references when found. No new external filtering
theorem has yet been imported beyond the catalog's inspected scope.

## Files, progress and chat capture

Incremental derivations go in `notes/`, code and small records in
`numerics/`, and assessments in `reviews/`. Update the existing
`research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md`;
do not create a competing ledger. Include intended author, LLM assistance,
actual model/effort, dates, and explicit evidence/status. At the end,
refresh this handoff or write a dated successor with links.

This conversation's canonical history is in [chat-histories][history],
thread `01a16f70-d7f8-7b00-b2fe-11a9070d630e`, history number 0001.
Its filename is
`0001_2026-10-24T19-43-48Z_start-density-approximation-study.json`.
Preserve its identity; never overwrite it with a new chat. A **new** chat
must register its own actual thread id/title and source through
`tools/refresh_chat_history.py` in this same investigation's history
folder. Refresh at the beginning and end and use the documented exact-turn
bounded deferred capture as the last tool action unless a trusted hook
is verified active. Read current hashes and message counts from the
registry rather than copying stale values into this note.

[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a06]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a16]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[overview]: ../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md
[identities]: 02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md
[contract]: 03_FIRST_BOUNDED_AVERAGING_CONTRACT_20261024.md
[closure]: 04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md
[limits]: 05_ASYMPTOTIC_MEAN_SHAPES_AND_FLUCTUATIONS_20261024.md
[regulator]: 06_REGULATOR_BIAS_FOR_SMOOTHED_ZERO_COUNTS_20261024.md
[review]: ../reviews/01_FIRST_RESEARCH_ROUND_SELF_REVIEW_20261024.md
[numerics]: ../numerics/README.md
[history]: ../chat-histories/README.md
