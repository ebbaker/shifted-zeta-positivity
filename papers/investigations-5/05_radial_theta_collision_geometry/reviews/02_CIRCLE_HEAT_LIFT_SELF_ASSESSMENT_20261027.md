# Circle heat lift: analytical self-assessment

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0001, thread `01a17e9c-bfd5-7782-a76f-b2a2eaa82417`.

**Scope: same-assistant assessment of [Note03][note], with exact operator algebra. This is not independent mathematical review.** The return meets the handoff's scoped-obstruction option for one specified circle heat lift. It does not establish a canonical collision exclusion or a smaller sufficient sign theorem.

## What was checked

1. **Physical normalization.** With s=r²=e^(2x), the period-one heat equation is K_s=L K/(4 pi). Consequently D K=c L K, c=e^(2x)/(2 pi). Applying the prescribed radial source gives G=w(3c L+c²L²)K, and G(t,x,0)=4 exp(tx²/4)Phi(x/2). Its Fourier coefficient is (4p²−6p)w exp(−p), with no lost factor of two: positive and negative n both remain in the series. Physical B is still −8H.
2. **Source and physical time.** U=cLF and V=c²L²F have P-eigenvalues 2 and 4. Physical time remains multiplication by x²/4. The time/x compatibility holds because the derivative of h in time cancels the commutator with the multiplier. This is a two-channel PDE on a circle, not a finite scalar state or physical forward heat.
3. **Operator residual.** Direct differentiation gives [P,A]=(4cL+t)D+4cL. The sign in A(PY)=PG−[P,A]Y is retained. The exact checker verifies normal-form operator composition, including [P²−6P+8,A]=PC+CP−6C; this is an operator coefficient check rather than evaluation on finitely many trial functions.
4. **Residual is actually nonzero.** On any nonzero Fourier mode, C y=0 on a far tail would force either y=0 or an exp(−x) tail, up to a convergent multiplicative correction. The prescribed solution has a super-exponential tail and nonzero source. This contradiction proves nonzero residual for the canonical response, without assuming a collision. It does not prove a sign for the residual's observed integral.
5. **Boundary costs.** The sign of the Volterra derivative gives DE(0)=+integral cos(sqrt(lambda)s) C Y ds. Its lambda derivative includes both the differentiated cosine and C Y_lambda. Differentiating PY at zero separately gives G−(lambda+t/2)Y−2cLY−(cL+1/2)beta. A physical beta zero does not remove L beta.
6. **Reflection and tails.** The full Jacobi transform maps the real auxiliary argument to an imaginary one. The source transformation keeps the Gaussian prefactor and the argument derivative. At the physical point it restores exact evenness. The individual U,V channels have nonintegrable inner asymptotics at positive time; only 3U+V cancels them. The radial mass, infinity constant and central charge remain the time-dependent M_t, distinct from the zero circle mean.
7. **Finite closure scope.** Every nonzero Fourier coefficient of G is positive for x≥0. A transverse polynomial annihilator must therefore vanish at infinitely many distinct eigenvalues. This proves the absence of a finite L-invariant linear circle space containing G. It does not exclude nonlinear modular equations, coefficients depending on the circle coordinate, nonlocal operators, or scalar identities after point restriction.
8. **Boundary-vector asymptotic.** The substitution p=q+v, q=pi n², gives Note03 (26) with coefficient 2(q+v)−3 and log factor x=(1/2)log(1+v/q). Dividing by q yields the limit −2 for the scaled boundary coefficient. An integrable exp(−v) times subexponential majorant proves compact-parameter uniformity. This is a large lattice-index limit, not an all-height physical estimate. It proves beta is never the zero circle function; it leaves beta(0)=B unresolved.
9. **Current and control scope.** The finite-upper-end Wronskian has the plus outer-boundary term shown in Note03 (29). Circle averaging removes cross-mode terms and changes the physical observation. Nonzero beta alone does not determine the sign or nonvanishing of the averaged Wronskian. The localized energy retains rho''/2. The inherited Gaussian control still has N/I0=27 and C/I0=−27. Weighted-square controls also satisfy the auxiliary mode PDE, while failing full reflection and unchanged infinite coefficients.

## Replay and limitations

The [standard-library checker][checker] passed and produced the [small record][record]. It uses exact rational polynomial coefficients and a full Leibniz rule for differential-operator composition. It also rechecks the inherited Gaussian cancellation without changing the founding record. No floating theta samples, finite-region certificates, measured speedup, or large derived data were produced.

The convergence, nonzero-residual proof, polynomial-annihilator argument and large-index limit are analytical proofs in Note03, not certified by the finite algebra replay. The DLMF definition, heat normalization and full-argument modular transformation were checked in the [reference annotation][refs]. Earlier transverse and current work is linked explicitly to prevent a novelty claim based on rerealization.

## Decision

Stop the selected homogeneous transfer and unweighted-circle-current inference. The return's information gain is the exact nonzero commutator, the actual canonical boundary mismatch, and the stated finite linear transverse obstruction. It supplies no favorable new physical sign. Keep broader RTC-03 open; RTC-04 still lacks a characteristic candidate. RTC-05 is the preferred next alternative, with full physical boundary accounting. Numerical refinement of RTC-06 is not justified by these identities alone.

No investigation closeout or manuscript milestone is declared. Independent mathematical review, a useful canonical mechanism and all-multiplicity/all-height transfer remain outstanding.

[note]: ../notes/03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md
[checker]: ../numerics/02_check_circle_heat_lift_20261027.py
[record]: ../numerics/02_CIRCLE_HEAT_LIFT_CHECKS_20261027.json
[refs]: ../references/01_CIRCLE_HEAT_AND_JACOBI_NORMALIZATIONS_20261027.md
