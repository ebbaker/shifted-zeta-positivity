# Assessment of the positive-carrier B02 return

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, Investigation05 chat0010, **Continue radial theta collision**.

**Same-assistant analytical assessment.** [Note29][note] is the proof source. No independent specialist or separate-model review, numerical implementation, PDE run, or interval certification is reported.

## What was checked

The candidate remains [Note28][n28]'s flow, with the same marked spectral derivative, unit weighting, preparatory heat time1 and non-affine drift. The new positive carrier is an auxiliary comparison solution driven by the already determined alpha. It does not determine a different feedback law. Its raw multiplier1+u² dominates the Euclidean norm of (cos Au,-u sin Au).

Spherical integration of rho gives the original q_T(u)du, without an extra interior copy. The carrier mass is M=P0+P2. Its initial second moment is the complete e^(4u)(1+u²) source moment plus6M. Both occurrences of6 come from the three-dimensional heat convention Delta, not Delta/2. The unit ball is included after smoothing and throughout the flow.

The quotient equation has drift 2 grad(log h)+alpha v. In the quadratic relative-energy identity, diffusion contributes exactly -2 integral h|grad(W/h)|². The drift cancels after complete integration; no derivative of alpha is omitted. The proof uses |W/h|<=1 and spatial cutoffs to remove the tails on compact lifespan intervals. The classical time-dependent scalar identity was checked in Michel–Mischler–Perthame, Lemma1.1; [reference12][reference] records the scope and external reading copy. The two signed components are summed; no positivity assumption on U or V is used.

The preparatory convolution bound gives F(0)<=P0. The decomposition F=|m|²/M+integral h|W/h-m/M|² is exact. Its constant part contains the physical first jet. Positive carrier mass alone therefore does not give the lower bound needed by the regularity estimate.

## Constants and direction of inequalities

For the moment inequality, the truncated-parabola integral is
\[
 \int(1-r^2/L^2)_+^2\,dX=32\pi L^3/105.
\]
Optimizing the resulting bound gives
\[
 c_3=\frac37(15/(14\pi))^{2/3},\qquad
 R\ge c_3\|W\|_1^{7/3}E^{-2/3}.
\]
The test field C(1-r²/L²)_+ times a fixed unit vector has mass 8pi C L³/15, energy32pi C² L³/105 and second moment8pi C L⁵/35. It checks equality algebraically. Sharpness is for the general moment inequality, not for theta trajectories or a nonlinear blow-up rate.

With r_mu=c3 mu^(7/3) E0^(-2/3), R>=r_mu and R'<=6M-2alpha R imply
\[
 B\le\tfrac12\log(R_0/r_\mu)+3Ms/r_\mu.
\]
Inserting this into Note28's G+3E0 comparison gives power5 on R0/r_mu and exponential rate30M/r_mu. The proof first works within the existing lifespan and then uses the continuation theorem. It does not assume global existence at the start.

Using an upper energy budget to lower-bound r_mu is in the correct direction. Rearrangement at time0 gives the lower energy budget c3^(3/2) mu_under^(7/2) Rbar^(-3/2), allowing a uniform alpha estimate as well.

At collision breakdown, R tends to0 by the integrated moment inequality and dominated convergence on the finite lifespan. The powers in
\[
 F\le\|W\|_1\le c_3^{-3/7}E_0^{2/7}R^{3/7},\qquad
 \|W\|_\infty\ge c_3^{3/7}E_0^{5/7}R^{-3/7}
\]
follow by rearranging the same inequality and using fixed L2 energy. They are moment-based bounds, not estimates in the remaining time.

## Direct theta comparison and controls

The theta specialization uses Note16's unchanged projection H-(A/2)H_a and the monotone ratio P4/P0. The positive uniform margin requires A_+^4 P4(T_+)<24P0(T_+). It is not extended to equality, where this explicit paid margin vanishes. The resulting flow bounds therefore cover the strict interior of an already separated region, with no new exclusion range.

For the exact Gaussian-polynomial control, direct Gaussian integration gives P0=9 sqrt(pi)/4 and P2=21 sqrt(pi)/32 at its collision time, hence M=93 sqrt(pi)/32>0. Its physical first jet is zero and its initial relative energy is positive. All generic comparison premises hold, yet the relative energy tends to zero at the finite endpoint. The value A_*^4 P4/P0=123 agrees with Note16 and correctly fails the direct margin test.

The [registered controls][controls] retain their actual hypotheses. Smooth controls satisfy the common carrier algebra on their moment domains; modified coefficients, full reflection or complete square arithmetic remain their respective missing canonical premises. None of those distinctions was used as a separating input in this return. Atomic cases are not newly admitted, and conditional endpoint examples are not promoted to unconditional applications.

## Assessment and next boundary

**The stated bounded return is supported by the in-note derivations.** It supplies a quantitative converse and a precise failure of this positive-carrier route to produce an independent margin. The argument is compatible with Note28's exact collision theorem.

The control refutes the universal inference from positive initial relative energy and monotone dissipation to a positive uniform floor. It does not exclude every quantitative combination of canonical moment values. This does not close B02's broader theta-specific estimate problem. The next route must retain additional signed canonical information and prove its propagation; merely naming a favorable production inequality is not an acquired estimate. [Continuation30][continuation] fixes that next question and its stop rule.

No E03 acquisition is warranted just to evaluate the new upper bounds on a domain whose noncollision is already established. E02 remains its separately frozen optional audit. The existing manuscript and prior mathematical notes were preserved. The reference, navigation and live progress files are updated as housekeeping; no manuscript milestone or snapshot is claimed.

[note]: ../notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n28]: ../notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[reference]: ../references/12_GENERAL_RELATIVE_ENTROPY_CARRIER_COMPARISON_20261028.md
[continuation]: ../notes/30_CONSERVATIVE_CARRIER_COMPARISON_CONTINUATION_20261028.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md

File checks: all links in the new notes, assessment, reference annotation and updated navigation resolved; the reference catalog parsed; whitespace/conflict and file-size checks passed. The manuscript SHA-256 remained 50f5a00509a570daf0b33d6bd418f1aa8cb37749ab4ebcd2477c140bc5ec3f77. These are document-integrity checks, not additional mathematical evidence.
