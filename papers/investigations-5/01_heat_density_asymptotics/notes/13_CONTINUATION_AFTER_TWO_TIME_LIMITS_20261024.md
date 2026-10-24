# Continuation after the two time limits and Vandermonde bounds

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Historical handoff; superseded by
[Note 15](15_CONTINUATION_AFTER_MANUSCRIPT_AND_VARIABLE_EPSILON_20261024.md).**
This records the state before the requested manuscript and variable-epsilon
extension; its fixed-epsilon scope is retained for those earlier results.

This handoff extended [Note 10][old]. The author clarified
the priority as t->+/-infinity for all heights, suggested a stationary
state, and asked to use the Vandermonde results in Investigation 4/12.
The density remains unnormalized with fixed epsilon; height-dependent
averaging is permitted. Do not silently replace that target with a
normalized density or remove the regulator.

Read repository AGENTS.md, LARGE_FILES.md, REFERENCE_WORKFLOW.md and
tools/CHAT_HISTORY.md, plus the [result index][results] and [avoid index][avoid].
Read [Notes 11][negative] and [12][positive] and the
[same-assistant review][review]. They are proved-in-note estimates, not
independently reviewed theorems or certified numerical onsets.

## Results to preserve

- At t=-T, average the exact density of
  G_T=Phi(0)sqrt(pi)/(2sqrt(T)) exp(-z^2/(4T)). Its error is bounded
  explicitly by Note 11 (5), O(T^-3) uniformly for all real x and
  |y|<=A sqrt(T). The self-similar profile T^2 rho(-T,sqrt(T)z) has
  O(T^-1) error. Preserve the epsilon crossover in the denominator.
- At positive time, L solves 4pi exp(4L)=2tL+9 and
  kappa=8tL-2t+36. The physical coarse approximation is
  R=L k_h/pi, with absolute error O(kappa^-1/2+L^-3) for kernels
  whose buffers fit in X~kappa^(1/3). Every fixed height eventually fits.
  The normalized stationary shape is pi R/L -> k_h. The physical
  density grows like log(t)/(4pi), so it is not stationary without scaling.
- The new carrier estimate cancels exp(mu |y|) at the same point, and
  the density transfer counts only disks that meet the averaging support.
  The weighted DS8 extension pays all source moments and tails.
- A growing consecutive block, m<=O(L kappa^(1/3)), has
  Delta_m=(pi/L)^(m(m-1)) product_(k=1)^(m-1)(k!)^2 exp(±V_m),
  with explicit V_m->0. The signed mean bound |mu-L|=O(kappa^-3/4)
  is essential for this choice of growing m. The rescaled Hessian also
  converges by dimension-uniform matrix bounds. Do not infer a stationary
  force law or backwards stability from these slice statements.
- A nonzero globally uniform clock limit fails at fixed epsilon for
  bounded transverse support and horizontal windows escaping to infinity:
  H and H_z vanish at large height at every fixed finite t. This is a
  scoped noncommutation of limits, not a universal no-go theorem.
- A finite xi-derivative hierarchy supplies an all-height absolute bound
  2^(-N-1) A(t,Y,epsilon), with N=O(t log^2 t) for a prescribed inverse-
  power tolerance. It is expensive (formula N~406877 at t=1024 in the
  recorded example) and has not been evaluated. Do not present it as a
  simple positive-time outer asymptotic or a practical numerical solution.

The [record][data] preserves failed conservative finite gates, source and
contour refinements, and non-theta determinant controls. Reuse it unless
a new question requires recomputation. No model was fitted, no theta root
finding was used, no manuscript was edited and no commit was created.

## Next useful work

1. Develop a positive-time outer-height approximation through the
   fixed-epsilon turnover, preferably a complete complex-saddle estimate
   with a directly usable density/log-potential error. The inner clock
   cannot remain uniform over all heights. The Polymath reference in the
   catalog was only metadata/abstract-checked in this round; inspect its
   actual hypotheses before importing a large-height theorem.
2. Alternatively sharpen the explicit source concentration allowances
   and certify a finite growing-window onset, or pay differentiated
   current/covariance remainders needed by the eventual boundary solve.
   Generic energy relaxation without the complete exterior unit is not
   a substitute for those estimates. Retain variable-filter commutators.

Update the existing [sole progress ledger][progress]; do not create a
parallel status folder. HDA-02--04 remain partial, HDA-07--09 gated.
Register new research chats here under their own actual identity.
This chat is **0002**, actual thread id
`01a16fb7-14ae-7d23-a933-972eca16a782`, title **Continue heat density
investigation**, distinct from 0001. Use the history tool at turn start
and end; make the exact-current-turn deferred final capture the last
tool action unless trusted hook activation is verified. Preserve the
registry's identity and provenance, and never prewrite an unsent reply.

[old]: 10_CONTINUATION_AFTER_COARSE_TRANSFER_20261024.md
[negative]: 11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md
[positive]: 12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[review]: ../reviews/03_TWO_TIME_LIMITS_AND_VANDERMONDE_SELF_REVIEW_20261024.md
[data]: ../numerics/TWO_TIME_LIMITS_ROUND3_20261024.json
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
