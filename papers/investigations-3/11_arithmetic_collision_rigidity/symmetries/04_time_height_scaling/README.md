# S04 Time height scaling and the growing cutoff

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual effort **max**.
Known low-mode asymptotics and proposed uniform signed analysis.

## Question and role

Can the complete signed arithmetic sum, or a useful joint observable, be
described uniformly when time and logarithmic height vary at fixed
\(\kappa=t\log(x/(4\pi))\)? This direction organizes the regimes of
[cutoff reflection][cutoff] and [jet rotation][rotation]. It is not an
asserted symmetry of H: the low-mode amplitudes approximately agree, while
the arithmetic phases change rapidly. See the [program guide][guide] and
[original scaling proposal][brainstorm].

## Established asymptotic structure

In the [current spectral normalization][outer], the low-mode amplitude is
\[
 |w_{t,n}(x)|\approx
 n^{-1/2-\kappa/4}\exp\{(t/4)\log^2n\}.
\]
For each fixed n and fixed positive kappa, along
\(x=4\pi e^{\kappa/t}\) as t decreases to zero, the limit is
\(n^{-1/2-\kappa/4}\). This fixed-mode statement does not justify
interchanging the limit and summation through the natural cutoff
\(N=\lfloor\sqrt{x/(4\pi)+t/16}\rfloor\).

The [earlier collision manuscript][earlier], `prop:absmass`, proves
uniformly on compact subsets of \(0<\kappa<4\) that
\[
 \sum_{N/2\le n\le N}|w_{t,n}(x)|
 =\{2(1-2^{-1/2})+o(1)\}
   \exp\{\kappa(4-\kappa)/(16t)\}.
\]
The growing terminal block therefore cannot be a small absolute tail in
that regime. This is a statement about absolute mass and the specified
leading-pair method, not a lower bound for the signed sum. The same source
contains edge cancellation, derivative-coordinate estimates, and a special
terminal-block limit at kappa=4. Kappa=4 is not thereby established as a
transition for actual collision behavior.

## Read in this order

1. [Original scaling question][brainstorm] and [continuation context][context].
2. [Current weights, phase, and fixed-cutoff contract][outer].
3. [Earlier manuscript][earlier]: `sc:coefficients`, `sc:vector`,
   `sc:coordinateasymptotics`, `prop:absmass`, the derivative-mass formula,
   growing-edge cancellation, and shrinking-time signed targets.
4. [S02][cutoff] and [S03][rotation], to identify which complete error or
   defect the regime analysis is intended to control.

## Bounded first task

Choose a compact kappa interval, such as a stated subinterval of (0,4),
and one complete signed observable. Define exactly what is demodulated or
normalized and why that does not erase the phase information needed by
the physical jet. A comparison of coefficient magnitudes alone is not a
comparison of that observable.

Split the sum into fixed low modes, an explicitly specified intermediate
range, and the moving terminal range. In each range retain amplitude drift,
the actual arithmetic phases, and the derivative coordinate. Match the
ranges with a common remainder estimate; state how cutoff crossings are
handled. Reuse the known terminal-block and edge estimates rather than
rederiving them as new outputs.

First ask whether the chosen decomposition gives a uniform **signed**
error useful to S02 or S03. If it does, test a bounded, feasible collection
of (t,x) pairs at matched kappa with complete certified errors. A finite
experiment only diagnoses the proposed regime; it does not prove the
t-to-zero statement. Do not begin enumeration at exponentially enormous
heights just to display the already-known absolute-mass growth.

## Controls and decision rule

The proposed fixed-kappa relation is not available unchanged for arbitrary
control sources. Identify its reliance on the actual normalized theta
weights and phase data. A generic scaling or heat identity without those
inputs is shared by controls and cannot exclude their events. Apply the
[common premise screen][guide] to any resulting exclusion test.

Pass with a uniform signed asymptotic and explicit useful remainder, an
effective regime boundary for a specified approximation, or a precise
obstruction for the chosen scaling observable. Stop if the work only
reproduces fixed-mode convergence, treats the terminal block absolutely
where its mass grows, or mistakes a diverging bound for diverging physical
amplitude. An amplitude-profile plot alone does not establish symmetry of
the complete first jet.

## Outputs and handoff

Create `notes/`, `numerics/`, and `reviews/` here when needed. Record the
kappa range, time range, resulting heights and cutoffs, all range boundaries,
uniformity statements, phase convention, error payments, and actual
model/effort. Supply S02/S03 with the exact domain where a proposed bound
is useful and with the obstruction outside it. Use the [guide][guide] for
source pins, file sizes, and chat history.

[guide]: ../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[brainstorm]: ../../brainstorm/01_SELF_DUALITY_AND_ADDITIONAL_SYMMETRY_QUESTIONS_20261018.md
[context]: ../../brainstorm/02_SYMMETRY_PROGRAM_CONTINUATION_CONTEXT_20261018.md
[outer]: ../../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[earlier]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[cutoff]: ../02_cutoff_reflection/README.md
[rotation]: ../03_normalized_jet_rotation/README.md
