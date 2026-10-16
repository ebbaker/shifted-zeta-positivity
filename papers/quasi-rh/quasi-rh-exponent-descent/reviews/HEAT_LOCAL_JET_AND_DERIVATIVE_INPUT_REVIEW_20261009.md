# Review of local heat jets and derivative inputs

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model audits are internal checks, not independent validation.

## Results prepared for the next manuscript review

[Heat Note 11](../newman_collisions/notes/11_ASYMMETRIC_DERIVATIVE_CORES_AND_JOINT_PROBES_20261009.md)
adds an asymmetric genuine-phase core reduction: the value coordinate keeps
cutoff \(K_v=N-\lfloor N^{3/4}\rfloor\), while the derivative coordinate
can use \(K_d=N-\lfloor N^{7/8}\rfloor\). The paid candidate-collision
bounds are

\[
|F_{t,K_v}(x)/2|\le\eta_N/2+40N^{-1/24},\qquad
|2F_{t,K_d}'(x)/L|\le2\eta_N+800N^{-1/24}/L.
\]

Both use the genuine phases, the same time, fixed integer cutoffs, and the
complete existing disk error \(\eta_N\). The derivative cutoff removes a
larger growing set of terms. This reduction is not a lower bound for either
retained sum.

The same note proves positive mean square of the complete genuine scaled
derivative, and hence the complete joint vector, on the sufficient range
\(H_d=Dt^2e^{2\mathfrak a/t}\). The normalized derivative means are at
least \(1/4\) for \(F_{t,N}\) and \(1/8\) for \(Q_t\), uniformly for
sufficiently small time and \(\kappa\in[1,2]\). The weighted Hilbert
estimate removes the earlier logarithm; derivative weighting supplies the
factor \(t^2\). Every reflected frequency and final cutoff term is retained,
and physical movement, normalization, reflection, cutoff changes, and
Cauchy derivative errors are paid.

[Heat Note 12](../newman_collisions/notes/12_THRESHOLD_COLLISION_JETS_AND_PAID_LAGUERRE_TEST_20261009.md)
adds an exact necessary condition at an all-real threshold collision.
Deflating two copies of the root and retaining its forced mirror root gives

\[
\mathcal J(Q):=2(Q_t''')^2-3Q_t''Q_t''''
 -(18\partial_x^2\log A_t+9/x^2)(Q_t'')^2\ge0.
\]

It holds at every multiplicity at least two. It does not assume that the
normalized function itself has a global real-root product. The global
product is used for \(H_t\), followed by exact local normalization.
At multiplicity at least four the second and third derivatives vanish,
so this particular fourth-derivative condition is uninformative; the note
states the higher-order hierarchy separately.

The measured approximation error for \(\mathcal J\) is explicit. Its full
fixed-cutoff analytic payment tends to zero despite growing absolute jets.
The original cutoff \(K_v\) also pays the quadratic test with a vanishing
signed-tail error \(O(N^{-1/6})\). The deeper cutoff \(K_d\) pays individual
derivatives but does not automatically pay their products uniformly on
\([1,2]\). This distinction is essential to the new interface.

## Mechanisms checked and limits retained

The signed edge argument imports
[Arias de Reyna's explicit derivative estimate](https://arxiv.org/html/2407.02094v1).
At the deeper edge its three terms give a partial-sum bound
\(20N^{17/24}\); exact coefficient variation supplies the derivative
payment. The critical scalar reserve is \(36\cdot11^6<20^6\).
Raw derivatives two through four are handled directly with their Bell
polynomial multipliers, rather than differentiating a cutoff scaling curve
or applying an unpaid complex-disk estimate to the tail.

The all-order diagnostic is scoped to the cited fixed-order derivative
estimate followed by Abel summation. In this family the third-derivative
bound gives the best short-edge exponent for each fixed raw derivative
order. Peeling a macroscopic endpoint block and adding the resulting upper
bounds by the triangle inequality leaves a positive exponent. This proves
a deficit of that upper-bound method, not growth of the actual signed sum
or an obstruction to other arithmetic transformations.

For the averaged derivative theorem, the imported input is the weighted
local-gap inequality in
[Montgomery--Vaughan, Theorem 2 and Corollary 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf).
The reflected frequencies have local gaps at least \(1/(8n)\) after the
single near-zero-frequency endpoint is temporarily omitted. The exact
weighted budget is
\(\sum nw_n^2(r_n^2+c_n^2)=(8t^2/\kappa^2+o(t^2))e^{2\mathfrak a/t}\).
The endpoint is restored before the final statement. The shorter range
is sufficient; no necessary-range theorem is claimed.

At a candidate collision, the paid absolute curvature estimate converts
this derivative average only on the scale \(Le^{-\mathfrak a/t}\).
The ratio of the proved averaging interval to that scale is
\(Dt^2e^{3\mathfrak a/t}/L\), which diverges. Thus the improvement does
not yet exclude a pointwise collision. The limited positive-measure
consequence likewise permits isolated double zeros.

The threshold test uses the all-real, order-one heat function and its
Hadamard product, as in
[Polymath's heat-flow framework](https://arxiv.org/html/1904.12438v2).
It requires the all-real hypothesis; it is not a constraint on an arbitrary
real collision before the threshold. The backward heat equation and the
Laguerre evolution alone supply no maximum-principle exclusion. An exact
even polynomial backward-heat flow has a freely prescribed positive
all-real threshold and saturates the mirror-jet inequality. This model
shows sharpness within that general analytic class; it is not the zeta
heat function or a positive Fourier-kernel example.

## Validation and remaining input

The [standard-library checker](../numerics/check_local_heat_jet_input.py)
and [small record](../numerics/local_heat_jet_input_record_20261009.json)
check symbolic normalized-jet and backward-heat identities, exact exponent
and scalar reserves, finite perturbation models of the complete bound,
and finite real-root polynomial deflation models.

All 2,386 exact assertions pass. The record binds the checker source by
SHA-256; two fresh runs reproduced it byte for byte. Internal cross-reviews
checked the coordinate factors, reflected local gaps, raw-jet multipliers,
normalization cancellations, general deflation formula, and quadratic error
products against their stated mathematical inputs.

These checks do not certify imported theorems, canonical products, analytic
limits, genuine phases, huge-height heat calculations, or collision
exclusion. Same-model internal reviews do not establish literature novelty
or replace independent mathematical review.

The next signed target now has an additional threshold interface: show
that both paid collision coordinates being small forces the genuine
fourth-derivative expression below its negative paid-error threshold, or
prove a stronger local joint lower bound directly. No such implication is
established in this round. The higher-multiplicity hierarchy also remains
unresolved. Results here are confined to the stated shrinking-time range;
no global collision exclusion or RH claim follows.

The stable manuscript remains unchanged for the user's planned progress
review. This continuation adds numbered research notes, a scoped review,
small calculation records, additive indexes, and a concise history entry.
No draft snapshot or Git commit is created.
