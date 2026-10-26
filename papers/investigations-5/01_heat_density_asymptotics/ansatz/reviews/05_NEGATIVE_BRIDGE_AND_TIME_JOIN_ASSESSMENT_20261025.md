# Assessment: negative-time bridge and the time join through zero

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
ansatz chat0001, thread `01a175aa-a487-79a1-85a8-6f465fdb36bf`.

**Review type: same-model internal analytical assessment.** A separately
assigned same-model check audited the source remainder, kernel losses,
cutoff transfer, tails and joined theorem. This shares the model and
classical inputs with the derivation; it is not human, cross-model or
independent specialist validation. No numerical, machine-symbolic,
exact-arithmetic or interval research was executed.

## Evidence and disposition

Reviewed [HDA-A02-AN02 r1][packet], the proved crossover estimates and
residual of [Note04][n04], the fixed-negative-time construction of
[Note05][n05], and the complete staged [Note06][n06]. The named classical
RS and gamma inputs are the inputs already checked for Note05; this
continuation requires no new evolved positive-time theorem or unqualified
fixed-time constant. The [input manifest][inputs] records opening versions.

Accept **NB16--17**: the unchanged finite representation of Note05 has
field, spatial derivatives j<=3 and direct first time errors bounded by
`C E_o(-T,z) exp(-L_X^2/4)` uniformly for `4/L_X<=T<=2` on every
declared fixed buffered chart. The new lower endpoint tends to zero;
the note proves its uniformity instead of inserting that endpoint into
Note05's former `[1,2]` estimates.

Accept **NB20--24**: the time-only join to Note04 gives a chartwise
representation throughout `-2<=t<=0`, including T=0, with the stated
field/spatial/time errors and the actual signed heat residual. The simple
uniform relative bounds are `X^-1/4 Lambda^j` for spatial j<=3,
`X^-1/4 Lambda^2` for the first time derivative and `X^-1/4 Lambda`
for the heat residual. These tend to zero; the more precise branch and
overlap allowances remain in the note.

Close **HDA-A02-AN02 r1** at its bounded bridge-and-join analytical scope.
HDA-A02 remains **Partial** as a broader negative-time/short-formula
program. No blocking analytical flaw was found in the staged note.
Constants and finite onsets remain analytical and unevaluated.

## What was checked

1. **Envelope comparison remains uniform down to zero.** NB3 is proved
   again from the explicit elementary amplitude: the positive arm sum
   is `|A_o| cosh(Im Theta_o)>=|A_o|`. Fixed-chart logarithm and gamma
   calibration errors stay bounded for `0<=T<=2`. This supplies the
   nonvanishing comparison envelope without division by H, a cosine or
   a root-dependent quantity.

2. **The kernel lemma retains every new time loss.** NB6 starts with
   the exact complex kernel modulus and the factor `T^-1/2`. Substituting
   `q=Re(d)+sqrt(T)v` cancels that normalization with dq, after which
   each j-th spatial derivative costs
   `D_j=T^-j/2(1+B/sqrt(T))^j`. The remaining Gaussian moment is uniform
   for `0<T<=2`. On the bridge the transverse factor is at most
   `exp(b^2 L_X/16)` and `D_j<=C Lambda^j`; neither is asserted to be
   bounded as T decreases. The explicit first T-derivative kernel is
   exactly the second spatial-derivative kernel, including its
   `-1/(2T)+(d-q)^2/(4T^2)` factor.

3. **The growing RS order and exact cutoff transfer survive unchanged.**
   NB8 retains `S_m-S_N` exactly in real initial data. Its partitions,
   center cutoff, integration endpoints and orders do not depend on z
   or T, and the cutoff-span gate leaves at most one adjacent mode.
   The real part is taken before multiplication by the complex kernel,
   preserving target holomorphy. The full source remainder includes
   `Gamma((K+1)/2)` growth. After all new kernel and outer-carrier
   losses, NB10 still has leading exponent `-(3/8)L_X^2`, with
   `(1/2)L_X log L_X+O(L_X)+j log Lambda` corrections. Its strict
   margin permits the final coefficient c=1/4.

4. **Gamma curvature and all arithmetic modes remain accounted for.**
   NB11 uses the n-independent analytic curvature factors and exact
   Taylor coefficients from Note05. Their Cauchy bounds are uniform in
   J. The complete initial population costs `G(X)X^1/4`; the uniformly
   bounded real exponential tilts are retained. With `J=ceil(3L_X)`,
   the local arithmetic error has leading exponent `-(7/8)L_X^2`,
   including the new transverse and derivative factors before onset
   absorption. A first gamma linearization or a fixed subset of modes
   is not substituted.

5. **Artificial tails are uniform as T decreases.** The polynomial is
   bounded on `V<|q|<=R/2`. On the remaining ray its logarithmic degree
   growth, bounded linear tilt and fixed-degree derivative polynomial
   are dominated by the available `q^2/T` exponent. This remains
   uniform for `0<T<=2`: the polynomial degree is O(log X), whereas
   `R^2=X^(2/3)`, and rescaled derivative polynomials are controlled by
   Gaussian decay as `|q|/sqrt(T)` increases. After the displayed
   transverse and D_j factors are retained, Gaussian splitting and
   rescaling justify both artificial terms in NB12. No true RS
   correction is extended into unbounded complex arguments.

6. **Both genuine source tails keep the right comparison scale.**
   NB14 first retains the gamma height exponential and a fixed real
   zeta-growth power on `V<|q|<=X/2`. Its preabsorption bound includes
   `D_j exp(TL_X^2/16+b^2/(4T)-V^2/(16T))`; its worst leading
   coefficient is `-15/8` for `V=8L_X`, `T<=2`. The global bounded
   source estimate is used only on `|q|>X/2`, producing NB15 with
   `-X^2/(128T)`. It remains super-Gaussian after outer normalization.
   All inverse-time, polynomial height and transverse losses are
   included before they are absorbed at a finite onset.

7. **The exact heat identity is used after the field comparison.** For
   each frozen X, the correction integral has bounded, fixed real
   initial data and fixed endpoints; the arithmetic part is a finite
   sum of full Gaussian transforms of exponential-polynomial data.
   They are entire in z and smooth for T>0. Dominated differentiation
   on positive-time compact subsets and the explicit uniform estimates
   justify use on the moving bridge domain. The domain constraint is
   not differentiated. Their residual is exactly zero, and the first
   time error consumes the already proved second spatial error.

8. **The overlap and derivative-of-cutoff term are real obligations.**
   Both models have proved comparisons on `4<=TL_X<=8`. NB19 uses a
   smooth time-only cutoff with the chart center L_X frozen; the
   piecewise definition avoids evaluating the bridge formula at T=0.
   Near zero the join equals Note04's model, so it inherits the proved
   through-zero regularity. Since `partial_t chi(TL_X)=-L_X chi'`,
   NB22 correctly contains `+L_X chi'(E_c-E_b)`, and NB23 correctly
   contains `-L_X chi'(F_b-F_c)`. The difference is bounded by comparing
   both models to the same H, not by differentiating an error allowance.

9. **Residual support and final scope are accurately stated.** Only
   the derivative-of-chi contribution is confined to `4<TL_X<8`.
   The crossover residual persists below that transition, and the total
   residual is zero for `TL_X>=8`. NB23 retains both contributions.
   The overlap factor `delta=X^-3/4 exp(TL_X^2/16)` is at most
   `C X^-1/4` where used; it is at most `C X^-1/2` on `TL_X<=4`.
   These facts justify NB24 and its logarithmic factors. This is a
   time-only chartwise join; it does not eliminate a physical spatial
   joining obligation.

## Limits and continuation

This result covers only the negative interval `[-2,0]`, its declared
fixed buffers, and reflection to left-height charts. It does not cover
T>2, growing T, arbitrary compact endpoints or the negative infinite-time
overlap. Note05's short natural-gamma-scale formula remains separate;
the bridge does not improve that formula's outer allowance or establish
correction dominance, a single elementary leading phase or amplitude.

The finite representation still has all N growing arithmetic modes,
growing K,J and a bounded correction integral. No evaluated numerical
onset, coefficient-provider conditioning, working precision, quadrature
cost, useful runtime, interval certificate or independent specialist
validation is supplied.

No physical U,W,R,J,Q transfer, root collar, collision exclusion,
simplicity statement, spatial joining-defect cancellation or RH conclusion
is accepted. The complete source, normalization, physical q, averaging
kernel and signed unnormalized observables are unchanged. Parent HDA-17
Partial, HDA-18 Gated and HDA-20 unfulfilled remain. The control screen
depends on the full canonical completion and ordinary coefficient
sequence, not Gaussian smoothing or positivity alone. Consult
[result summaries][results] and [avoid][avoid], especially shared-premise
review05, scope07, normalization08, cancellation12, unchecked-imports16
and status19.

**Next owner: Analysis — Sol.** The separately prepared [HDA-A03-AN01
packet][next] addresses the regulator branch: a corrected one-arm
comparison on one bounded switch neighborhood and the associated center
change against the actual physical rounding scale. That packet is
prepared only; this assessment proves none of its requested results and
does not dispatch it. General compact-negative-time parameterization
remains possible follow-through. No specific resistant estimate in the
accepted bridge requires Astra escalation.

[packet]: ../research-progress/handoffs/HDA-A02-AN02.md
[inputs]: ../notes/06_NEGATIVE_BRIDGE_INPUTS_20261025.json
[n04]: ../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[n05]: ../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[n06]: ../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md
[next]: ../research-progress/handoffs/HDA-A03-AN01.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
