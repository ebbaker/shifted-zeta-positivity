# Continuation: the concrete joint-coupling problem

12 September 2026.

## Best candidate and what to retain

Continue with the **relative channel complex whose derivative carries coherent translations**, using the exact history/endpoint rules of the loop model. Its positive ambient metric, harmonic quotient, actual adjoint, arbitrary-input preparation, and infinite-channel domain are specified. It is the strongest remaining candidate because its revised coupling produces arithmetic delta translations without merely declaring them to be part of a boundary metric. It also exposes its errors as explicit kernels.

This preference is a research judgment. The model's successful undeformed form is still the pre-existing gamma kinetic form. The revised model matches a singular part of a *variation*, not the full form, and the norm is not invariant under varying the arithmetic coupling.

Keep these formulas visible:

\[
Q_{0,L}=K+w_0\|f\|^2+2|C|^2-2|S|^2
-\sum_{p^m<e^L}{\log p\over p^{m/2}}\langle f,(T_{m\log p}+T_{m\log p}^*)f\rangle.
\]

For one prime, the derivative coupling gives its delta translations plus translates of $k(x)=-[j(|x|)+|x|j'(|x|)]$. For product composition of two primes, the residual kernel is a four-translate sum of

\[
V(x)=-\tfrac14[j(t)+3t j'(t)+t^2j''(t)]_{t=|x|}.
\]

These are continuous integrable functions, with $k(0)=-1/4$, $V(0)=-1/16$; they cannot be discarded as ultraviolet errors. At finite interval length a removed delta translation does not imply that its continuous remainder is removed.

## Next calculation, with a success/failure test

Start with $\log2<L\le\log3$, where only the first prime is active in the target. Keep the full gamma tower, not a finite tower extrapolation. Introduce one additional **explicit** block in the relative differential or injection, permitting it to mix the $a_0=1/2$ mode, the pole boundary amplitudes, and the first-prime history. Solve its linear equilibrium equations.

The calculation should answer one question: can that block cancel the translated $k$ kernel, supply exactly $w_0\|f\|^2+2|C(f)|^2-2|S(f)|^2$, and leave a nonnegative ordinary component energy? The block must be defined before matching. Its negative-looking contributions must arise from elimination or coherence, with all positive diagonal costs retained. Merely subtracting $k$, choosing a target-dependent Schur complement, or assuming a contraction between the two sides of the full-form norm difference does not meet this test.

There are concrete ways for the experiment to terminate usefully:

* An explicit finite block with a proved nonnegative bare energy and all-input trace theorem yields a genuine restricted completion.
* A rank/kernel argument shows the chosen pole block cannot cancel the translated $k$ function. This rejects that block, not all couplings.
* A boundary condition needed for the growing propagator reintroduces the negative Robin mode; record its test vector and try a coupled, rather than isolated, stabilization.
* A domain estimate shows the required infinite mixing does not define a closed differential on the stated component space. A different topology is then a substantive change, not a notation change.

Before trying all lengths, test the two-prime case $L=5/4$: $\log2,\log3$ act, while their forward sum does not. The mixed adjoint cap at $\log(3/2)$ and the continuous remainder at $\log6$ distinguish a full construction from a principal-symbol match. Above $L=\log4$, the repeated-2 coefficient must be $(\log2)/2$, with the same rule fixing the first repetition. The determinant sign obstruction prohibits a fixed finite primitive sector from accomplishing a uniform reversal of all repetitions by ordinary trace alone.

## An alternative finite-slab theorem

If the joint kernel block resists construction, the existing later report gives a precise, smaller target: for the central even gamma sector at $L\le7/10$, evaluate

\[
s_L=a_L-\langle b_L,F_L^{-1}b_L\rangle,
\]

where $F_L\ge11/100$ is independently established on the even mean-zero subspace, $a_L$ is the constant-input energy, and $b_L$ is its coupling to that subspace. The residual estimate in [the even-sector report](../../investigations/positive-factorizations/archive/progress-reports/EVEN_SECTOR_REDUCTION_round4_20260911.md) gives a way to certify this scalar with an explicit response ansatz. This is a useful restricted theorem but does not by itself supply the arithmetic selection mechanism or a factor of $F_L$.

## What remains before a full arithmetic realization

The outstanding requirements are a jointly positive completion of the exact contact and pole terms, a rule selecting the channel and defect data, control of mixed cycles and Gram terms, and all-input existence/domain estimates at unboundedly many lengths. No common strictly positive gap is required. No simultaneous bounded/closable whole-line $L^2$ preparation should be imposed. Separate finite-interval realizations would suffice for the stated RH criterion if their exact full identities were actually proved.

In particular, merely evaluating the present product deformation at finite coupling cannot complete the task: equation (11a) of the coherent-deformation note gives the wrong repeated-prime coefficients. A continuation needs a mechanism beyond that scalar product, even if it cancels the first-order continuous residuals.

Avoid spending the next pass on bigger numerical positivity sweeps. The current obstruction is a missing joint construction, now expressed by explicit residual kernels and finite-interval interface equations. Numerical work should resolve a specific identity, residual bound, or failure of a proposed block.
