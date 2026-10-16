# Review of the Gaussian endpoint calculation and the next bounded task

20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: not exposed in this session; not inferred.
Status: fresh internal LLM review, not independent specialist or different-model review.
Reviewed repository state: f84ed5f; clean working tree at review start.

## Assessment

No material algebraic error was found in the Gaussian mode-preparation
calculation. Its negative conclusion is supported for the specific coupling,
charged endpoint, and ordinary radial response that it defines. The construction
really excites an infinite protected composite tower, but the resulting
spectral weights have a Bose factor that prevents the requested component match.

The physical scope is appropriately limited: this is a spatially nonlocal
mode preparation, not a derived local supersymmetric hemisphere interaction
or Wilson observable. The proof concerns this family, not every Gaussian
construction, every protected observable, or localization in general.
The arithmetic cumulative-positivity problem receives no new certificate
from this result. No changes to the reviewed calculation or manuscript are
required on the basis of this review.

Reviewed files are the Gaussian endpoint note, source audit, checker, saved
record and handoff; the preceding Hodge note and current SI S12; and the
critical-path append handoff, scalar-obstruction note and EMA anchor.

## Analytical checks

1. **Stable preparation.** For
   `H_g=(N_a+N_b+1)/2-g(a^dagger b^dagger+ab)`, direct Bogoliubov
   substitution gives a gap `Omega=sqrt(1/4-g^2)` when `|g|<1/2`.
   With `lambda=tanh(eta)`, `q=lambda^2`, the relations
   `g=lambda/(1+q)` and `Omega=(1-q)/(2(1+q))` agree with the
   ground-state recurrence. The preparation Hamiltonian is explicitly
   switched off before evolution by `D=(N_a+N_b)/2`.
2. **Endpoint coefficients.** The unit-norm prepared vacuum has
   coefficients `sqrt(1-q) lambda^k` in `|k,k>`. Applying the charged
   creation endpoint and normalizing gives
   `(1-q) sqrt(k+1) lambda^k |k+1,k>`. Its weights therefore are
   `(1-q)^2(k+1)q^k`, with total one. Ordinary creation/annihilation
   adjoints, rather than tilded localized Weyl generators, are used.
3. **Response.** Summing the geometric derivative gives
   `G_q(u)=(1-q)^2 exp(-u/2)/(1-q exp(-u))^2`. The endpoint expectation
   and its stated energy derivative at zero agree. A scalar matrix
   element of this kind is not an arbitrary-input arithmetic transfer.
4. **Additional projection.** Restricting, for comparison only, to even
   `k>=2` gives weights proportional to `(2n+1)q^(2n)`. The first two
   successive equality tests demand `q^2=3/5` and `q^2=5/7`.
   This is an exact incompatibility for every common normalization.
   The extra projection is not derived from the neutral pair Hamiltonian.
5. **Singular limit.** At `q -> 1`, normalized states converge weakly to
   zero and their fixed-positive-time response vanishes. Removing the
   common vanishing factor instead gives the distributional coefficients
   `sqrt(k+1)`. Heat regularization reproduces the stated stable-family
   relation. The full singular response has leading term `1/u^2`; its
   selected even part has leading term `1/(2u^2)`. The desired component
   has `1/(2u)`. The corresponding positive derivative integral diverges
   logarithmically for the candidate. These observations support the
   scoped obstruction without numerical extrapolation.
6. **Limits of the argument.** A fixed finite-norm ket has a finite
   response at zero under a strongly continuous contraction semigroup.
   This excludes an exact singular covariance for such a ket, but does
   not exclude distributional point-field responses with a stated regulator.
   Neither the signed arithmetic pole nor the prescribed finite contact
   term is supplied by the Gaussian positive correlator.

## Primary-source scope

The Hodge identity and its common kernel were rechecked directly in
[Dedushenko--Pufu--Yacoby, Section 3.1, equations (3.1)--(3.5)](https://arxiv.org/html/1610.00740v2#S3.SS1).
They support using canonical Higgs states without asserting that ordinary
dilation preserves all twisted representatives.

[Gluing II, Section 4.3.2, equations (125)--(135)](https://arxiv.org/html/1807.04278v3#S4.SS3.SSS2)
distinguishes the free chiral ring, boundary Weyl-algebra actions and the
hemisphere amplitude. These formulas do not derive the new nonlocal
Gaussian preparation. The new note makes no such attribution.

This review checks the inherited Hodge distinction and the new oscillator
argument; it is not a complete specialist audit of all supersymmetry,
interface locality or boundary-state functional analysis.

## Reproduction

The command

    python3 -B numerics/check_gaussian_pair_endpoint.py --output /tmp/gaussian-pair-review-replay.json

passed. The replay was byte-identical to the saved record: four rational
coupling checks, 25 Wick-weight levels, three independent finite squeeze-ODE
runs, 20 response comparisons, and nine regulator checks, together with the
reported short-distance samples. Maximum fine-run amplitude discrepancy was
`7.516763860263372e-12`; maximum ODE-response discrepancy was
`4.134470543704083e-13`.

Saved/replayed record SHA-256:
`2ed726894a733c9d239d2aed0ef909825f8b8809fe3efc8e37c1de47abdd6f6c`.

Current package and all five manuscript snapshot identity checks passed.
The existing 299-case ledger was validated by the inventory checker, not
rerun in this review; its earlier replay remains a separate recorded event.
Finite RK integration is a diagnostic, not an interval certificate.

## A planning lemma for the arithmetic continuation

The following observation is derived in this review, not a result of the
Gaussian calculation. It sharpens the next task's metric feasibility check.
For fixed finite M, consider the proposed cumulative lower operator

\[
 K_{M,\ell}=2\int_0^\omega V_{s,\ell}^*
       (T_{M,\ell}-s^2I/8)V_{s,\ell}\,ds,
 \qquad \ell=L,h.
\]

**This operator is compact and cannot alone be a coercive metric on the
infinite-dimensional input space.** Here the needed hypotheses hold in the
prime-free test: `T_M` is bounded; every positive-shift `V_s` is compact;
`V_s` is norm-continuous for `s>0`; and `sup_{0<s<=omega} ||V_s||` is finite.
The last bound can be taken as one using the inherited anchor and restriction.

For completeness, positive-shift compactness follows by approximating the
locally integrable causal kernel in L1 by bounded kernels on the finite
interval; their operators are Hilbert--Schmidt and Young's inequality gives
norm convergence (SI Proposition S10.3). On any closed shift interval away
from zero, the explicit beta/pole kernel has an integrable common majorant
and is L1-continuous in shift, giving operator-norm continuity.

Truncate the displayed integral at `s=epsilon>0`. Its integrand is a
norm-continuous family of compact operators, so the truncated integral is
compact. The omitted operator norm is at most

\[
 2\epsilon C^2(\|T_{M,\ell}\|+\omega^2/8),\qquad
 C=\sup_{0<s\leq\omega}\|V_{s,\ell}\|.
\]

Thus the full integral is a norm limit of compact operators. A compact
self-adjoint operator on infinite-dimensional L2 cannot dominate `c I`
for any `c>0`: its quadratic forms on an orthonormal sequence tend to zero.
Even a positive finite-tower lower form loses a uniform floor through this
integration. The unbounded full tower need not have this limitation.

This does **not** obstruct the actual defect: at fixed positive shift,
`E=I-X^*X` and `F=I-ZZ^*` are identity minus compact operators and retain
a positive floor by the anchor. It obstructs using the finite-tower integral
by itself as an invertible all-input replacement metric.

If `E>=delta I` and `E>=K`, valid combinations include
`E>=theta delta I+(1-theta)K`, `0<=theta<=1`; if `K>=0`, any `theta>0`
retains a floor. The two inequalities do not justify adding the two lower
bounds. Output metrics require the stipulated reflection. Alternative
routes may keep the exact identity-minus-compact structure or obtain
separate high-frequency/corner estimates. Their effectiveness is unproved.

## Recommended next session

Return to the bounded cumulative append at `L=1/2`, `h=1/20`, `omega=1e-3`.
First establish feasible coercive lower metrics and an energy-aware split
that handles the logarithmically concentrated join directions. Then control
all four mixed blocks, including both complements. The target remains an
all-input bound for normalized cumulative coupling below one, or a precise
obstruction to the chosen estimate. Do not substitute an enlarged central
certificate or another localization fit for that task.

Retain the Gaussian result as a useful scoped physical exclusion. Resume
that branch only with a new independently specified action or observable;
weight flattening chosen to match arithmetic is not such an input.
Specialist review of both the supersymmetry interpretation and the EMA
anchor remains outstanding.
