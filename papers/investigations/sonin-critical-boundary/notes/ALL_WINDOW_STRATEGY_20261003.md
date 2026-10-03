# Strategies for controlling all support windows

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed and are not inferred. Three separate same-model discussions examined arithmetic scaling, operator continuation, and numerical cost. This is a research strategy, with an exact centering identity below, not an all-window theorem or specialist review.

The recommendation is to use the next local certificate as a test of a scalable comparison mechanism. Prioritize estimates that retain signed prime cancellation and measure the correction relative to source energy. Treat the present low-band certificate as a reliable baseline, and finite-window continuation as a way to test those estimates. Repeated certificates without a general bound or a proved termination mechanism would not establish the all-window result.

## The target and what the local result supplies

For I_L=(-L/2,L/2), retain the same three source conditions for every L:

\[
F\in C_c^\infty(I_L;\mathbb C),\qquad
\int F=\int e^{x/2}F=\int e^{-x/2}F=0.
\]

The last two conditions are preparation F=(-d²/dx²+1/4)h; the first is the already justified fixed mean condition. With all active primes captured,

\[
Q[F]=B_{S_L}[F]-K_{S_L}[F],\qquad S_L=\{p:p\le e^L\}.
\]

At L=1 the [completed certificate](REVISED_B_LOCAL_OUTCOME_20261003.md) gives Q>=0.09||F||² and Q>=B/9000. It uses independent arithmetic coercivity and an explicit correction norm bound. It does not prove the stronger unweighted spectral-part inequality B>=K_plus.

The all-window target is Q>=0 on the displayed class for arbitrarily large L. A positive comparison fraction theta_L may depend on L and tend to zero. A fixed positive lower bound for Q in L2 is not required. Under the RH zero-sampling representation, long prepared packets concentrated in a frequency gap illustrate why a support-independent L2 gap would be inappropriate; this is a conditional diagnostic, not an ingredient of the proposed proof. That argument alone does not disprove a uniform relative fraction Q/B.

The source spaces are nested by extension by zero, and Q is the same arithmetic form on their common elements. Thus positivity on any unbounded sequence L_j suffices to cover every compact source. A theorem covering all j, or an algorithm accompanied by a proof that its certificates succeed for every j, would close the quantifier. A finite list of successful runs does not. The fixed additional moment condition is compatible with the restricted criterion in [Connes and Consani, Appendix C, Proposition C.1](https://alainconnes.org/wp-content/uploads/Selecta.pdf); do not add a growing list of source constraints silently.

## Why direct repetition may become ineffective

For each L the active arithmetic multiplier is

\[
q_L(t)=\gamma_\infty(t)
-2\sum_{p^m<e^L}(\log p)p^{-m/2}\cos(t m\log p).
\]

Endpoint shifts contribute zero. Prime powers, not only new primes, are events: after log 3 comes log 4. Let C_L denote the sum of the positive amplitudes in the displayed trigonometric polynomial. The current sufficient frequency cutoff uses gamma_infinity(T)>lambda+C_L. Because gamma_infinity(T) grows logarithmically, this forces a very large safe cutoff when C_L grows. Partial summation from the [prime number theorem](https://dlmf.nist.gov/27.12) gives C_L asymptotic to 4e^(L/2). Thus this particular worst-case cutoff has doubly exponential scale in L. This is a barrier in the bound, not a theorem that the true form requires that cost.

The Legendre rank must also resolve the product LT. The transported boundary-gap estimate deteriorates through products of (1-p^(-1/2))/(1+p^(-1/2)), making the certified correction norm increasingly pessimistic. Raising arithmetic precision does not repair either loss.

There is a second loss: the bound Q>=lambda I-P_E(lambda-q_L(D))_+P_E discards helpful positive-frequency contributions before source compression. Failure of this lower bound does not imply failure of Q>=0. Record the distinction between an insufficient error budget, a poor majorant, and an actual negative source value.

## Strategy 1 Preserve prime cancellation before estimating

This is the main arithmetic candidate. Introduce the continuous prime-density form

\[
W_{\rm cont}[F]=\int_{\mathbb R}e^{|u|/2}\kappa_F(u)\,du.
\]

It is finite for every compact source. The normalization corresponds to replacing the prime measure sum Lambda(n)delta_(log n) by e^u du on u>0. No prime-number estimate is assumed in making this definition.

There is an exact simplification on the pole-neutral class:

\[
e^{|u|/2}=2\cosh(u/2)-e^{-|u|/2},\qquad
\int\kappa_F(u)e^{u/2}\,du
=\overline{\int e^{-x/2}F(x)\,dx}\int e^{x/2}F(x)\,dx=0.
\]

The analogous negative exponential pairing also vanishes. Therefore

\[
W_{\rm cont}[F]=-J[F],\qquad
J[F]=\int_{\mathbb R}\frac{|\widehat F(t)|^2}{t^2+1/4}\frac{dt}{2\pi}\ge0.
\]

Defining the exact signed discrepancy E=W-W_cont gives

\[
\boxed{Q[F]=\Gamma[F]+J[F]-E[F].}
\]

This identity is checked for complex sources. It isolates cancellation of the exponentially growing smooth prime density before absolute bounds. It is not a positivity theorem: gamma_infinity(0)+4 is negative, so even the displayed main multiplier needs a low-frequency analysis. Moreover E is not known to be small. Regrouping alone just adds J to both sides of the comparison.

The useful new theorem would control the signed discrepancy on the prepared source space, with a separately controlled low-frequency block. It must exploit source smoothing, moment cancellation, or arithmetic structure; importing RH-strength prime-error estimates would be circular. The next numerical diagnostic should compare the raw absolute-amplitude bound with estimates of the centered discrepancy on identical source spaces. A large reduction would justify developing this route; a mere change of notation would not.

## Strategy 2 Control the correction relative to energy

The [closed-source analysis](CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md) supplies, at the first-prime window, a positive source operator B and a compact selfadjoint relative correction

\[
H_L=B_L^{-1/2}K_LB_L^{-1/2}.
\]

On that domain, Q>=0 is equivalent to H_L<=I. A useful all-window mechanism would separate a controllable high-energy complement from the finite collection of relative eigenmodes near one, while retaining all mixed terms. For a source projection E, a sufficient Schur bound is

\[
H_{11}\le\vartheta_L I< I,\qquad
I-H_{00}-\frac{H_{01}H_{10}}{1-\vartheta_L}\ge0.
\]

The proposed theorem is an estimate for the complementary and mixed blocks with explicit dependence on L and the active places. Merely defining H_L or checking its first few eigenvalues is not such an estimate. Infinite positive index is compatible with this approach: positive directions may have small relative size. No uniform gap below one is assumed.

The two-prime case requires a fresh compactness and tail argument. The one-prime kernel has isolated resonances at integer multiples of log p. With primes 2 and 3, logarithms of ratios of smooth frequencies can form a dense set; log 2/log 3 is irrational. This does not establish that every candidate resonance survives the coefficients, or that the kernel is noncompact. It does invalidate carrying over the phrase “finitely many translated singularities” without proof. Fixed-place L2 summability of kernel terms is a plausible replacement lemma, but constants as the prime set grows remain an additional obligation.

For the next experiment, estimate relative spectral tails and mixed blocks, rather than pursuing K<=0 or a finite list of scalar moment penalties. The arithmetic certificate can calibrate the result without being presented as an independent Sonin derivation.

## Strategy 3 Validated continuation with fixed places on each interval

This is the most practical bridge between local calculations and the two analytic candidates. Over a bounded range L in [L0,L1], preselect S_star containing every prime active at L1 and keep the Sonin operators fixed. The arithmetic form then agrees with Q on every source in that range. Adding an inactive place changes B and K equally on old sources, so a jump in their separate spectra is not evidence of a jump in Q.

A continuation theorem could transfer a finite-block certificate between nearby L, using a common reference interval after dilation and rigorous bounds on the change in the full form. It needs a quantified modulus in an energy-relative or resolvent topology; pointwise compactness does not supply that modulus or bare L2 operator-norm continuity. The source moment projection also changes under dilation and must be included. Another route is simply to certify successive larger endpoints: each certified Q endpoint automatically covers smaller supports. This avoids an unnecessary demand for a separate certificate at every real L.

One tempting estimate fails: a new prime shift just inside the support boundary is not small in bare L2 operator norm. Two narrow prepared packets at separation log p retain normalized correlation 1/2 there, even when the overlap region is arbitrarily short. The prime-shift contribution becomes small relative to their archimedean energy because that energy grows logarithmically as the packets narrow. Threshold bounds must therefore be energy-weighted, with full edge and cross-block control.

This route needs a recurrence or a proof that loss budgets remain coverable for an unbounded sequence. It cannot rely on generic monotonicity in places, already ruled out by the earlier signed-increment analysis. A table of finite certified windows would be useful evidence but would leave this theorem open.

An adaptive rule also needs a nonaccumulation argument: repeatedly taking a smaller successful step could converge to a finite limiting window. A useful continuation theorem would combine a margin update with a bound ensuring that the accepted step lengths have a divergent sum. Record the cross-block budget relative to the remaining diagonal margin when testing such a rule.

## Strategy 4 A source-local limiting comparison

As an alternative to all-window constants, seek for each fixed source

\[
Q[F]\ge B_j[F]-\epsilon_j[F],\qquad B_j[F]\ge0,
\quad\epsilon_j[F]\longrightarrow0.
\]

The rates may depend on F. This would suffice without one uniform lower bound or comparison fraction over all sources. The existing [moving source-tail criteria](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_DIRECT_PLACE_TAIL_CRITERIA_20260929.md) identify source-smoothed tails and signed place increments relevant to convergence.

The unresolved tasks are quantitative tails along the growing family and identification of the limit with the complete arithmetic form. Fixed-place convergence does not imply convergence along a growing place set. The global zeta-phase endpoint route additionally retains its off-line-zero and exact-projection mass obligations. This is a separate conceptual route, not a consequence of the new local certificate. Keep it as a secondary option unless a concrete tail estimate emerges.

## What the next certificate should test

Use L=6/5 as a proposed next anchor: log 3<L<log 4, so the active delays are log 2 and log 3. This is a suggested experiment, not a certified result. Keep S_star={2,3} over the comparison range [1,6/5] when comparing B and K; do not transfer the old B fraction from S={2} without recalculating its representation-dependent bound.

Before a new certificate, derive the general-L formulas and predict the cutoff, rank, integration cells, and error budget. Under unitary dilation to y in (-1/2,1/2), use phase tLy, constraint functions 1 and e^(plus/minus Ly/2), plane-tail argument LT/2, and ||d v_t/dt||<=L/sqrt(12) for unit-normalized plane waves. The low-band operator then has an overall factor L in its Fourier integral. Forgetting that factor would invalidate a length-one code generalization.

Record four separate margins: the arithmetic lower bound, the true error allowance, the loss from the chosen negative-part majorant, and the correction-to-B conversion. Compare the raw and centered prime formulations on identical source spaces. Include both parities, complex polarization, and active prime powers. A failed sufficient bound must be classified before increasing precision or matrix size.

The deliverable should be one additional full-space certificate or a quantitatively identified obstruction in the method, together with a statement of which proposed all-window estimate it supports. Do not begin an unbounded window sweep. The [session handoff](NEXT_SESSION_ALL_WINDOW_HANDOFF_20261003.md) gives the exact starting state and reading order.
