# Internal review: centered theta residual and shared arithmetic

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Independent reviewing agent; the reviewer did not author Note 16, its
analytic or geometric inputs, or the numerical pilot. Parent-verified
inherited configuration: **gpt-6-astra (Codex)**, reasoning effort **ultra**.
The reviewer authored the separate endpoint/coverage auditor described below.

**Assessment:** the reviewed note and bounded certificate are mathematically
consistent. The independent full numerical replay passes all 32 closed
cells. The exact four-jet identities, shared theta carrier, complete tail
payments, and stated limitation on absolute first-channel dominance check
out. No further mathematical correction is required in the reviewed version.
The global small-time collision-region estimate remains open.

## Version binding and replay evidence

| Reviewed file | SHA-256 |
|---|---|
| `16_THETA_CENTERED_RESIDUAL_AND_SHARED_ARITHMETIC_20261014.md` | `5898a93a7652b23f40de57fb653ecb7f4591a0421a6b0f18e86d8b19aa81b302` |
| `certify_phase_centered_residual.py` | `6da9b9c05b465a0067809f9e11bb7d7414f51330afe91c2c38e7cb02fc939afb` |
| `check_shifted_contour_payments.py` (imported) | `b6f0114e1a4de2e1848f20ab0ab2f1022d9b55015184a879ae0c0536a62d6ad6` |
| `check_theta_centered_residual_identities.py` | `0d1c04507f232166b475025930ecfde386207d43007bf652babd8045dfc5cc11` |
| `audit_theta_centered_residual_record.py` | `acdb78b91c8dff8af31f21b84d808fb0296a7f64ad8503575969825a1aa551a6` |

The producer certificate retained as
`THETA_CENTERED_RESIDUAL_100_104_20261014.json` has SHA-256
`aee1f000150a90e1269faa9a8cfafa6251d581ec0f586f0b09d554ef8822741d`.
It was reviewed under the staging filename
`PHASE_CENTERED_RESIDUAL_100_104_20261014.json`; the bytes are identical.

The reviewer reran the full driver using the bundled Python runtime,
python-flint, and 192-bit Arb/Acb precision. The independent record
`/tmp/inv21-residual/PHASE_CENTERED_RESIDUAL_INDEPENDENT_REPLAY_20261014.json`
has SHA-256
`147123dd64d0a2e78f404dc2505c3912927fa46192845ccfe524ac4ce4e0bc11`.
It reports **PASS on all 32 cells** and agrees with the producer record
in every field except elapsed wall time. This is a full recomputation,
not merely a check of the producer's `PASS` flag.

The final algebra checker independently replayed with **9 exact rational
polynomial identities passing**. The separate portable record auditor
passed **548 checks**, including comparison with the independent full
replay; its ordinary invocation without `--compare-record` runs 547
checks. It verifies source-file hashes, exact closed-cell coverage,
endpoint-derived norm and residual bounds, cone slack, strict stationary
margins, and the stated physical and normalized norm floors. A deliberately
duplicated cell was rejected with a nonzero exit status, including under
optimized Python. The first smaller exploratory endpoint audit had 294
checks; the retained portable auditor adds source binding, shape checks,
summary bounds, and norm-floor checks.

The retained [record auditor](../numerics/audit_theta_centered_residual_record.py)
and [audit record](../numerics/THETA_CENTERED_RESIDUAL_RECORD_AUDIT_20261014.json)
have a different scope from the numerical driver and the algebra checker.
They do not formalize the quadrature library or the analytic tail lemmas.

## Four-jet algebra and stationary consequences

The contour identity

\[
u^2-b^2=-(i(u+ia))^2-2a\,i(u+ia)-(a^2+b^2)
\]

gives exactly `C_j=-h_(j+2)-2a h_(j+1)-mu h_j`, with
`mu=a^2+b^2`. Therefore the drift vanishes separately in each scalar
stationary observation and `L_j=mu h_j^2+h_j C_j` there. It does not
vanish from the vector radial pairing on all of `h_1 h_2=0`; the note
correctly retains the remaining `2a h_0 h_1` term on `h_2=0`.

The cone `C_0^2+C_1^2 <= eta^2 E` yields the stated first sign bound
and second bounded-loss bound. A common coefficient is indeed
`K=eta^2/(4mu)`, since

\[
\frac{\eta^2}{4\mu}-(\eta-\mu)
=\frac{(\eta-2\mu)^2}{4\mu}\ge0.
\]

Both sum-of-squares identities were independently expanded. The
`eta/2` term in the first stationary multiplier is necessary; omitting
it leaves a defect `eta^2 h_1^2` away from stationarity. It is present
in the reviewed note and checker. The phase-balanced evolution and its
variable-time-parameter correction are also correct. None of these
identities divides by the physical observation.

The weaker paid signed estimate (9a) follows by expanding
`mu(p+delta)^2+(p+delta)(q+epsilon')`, retaining the nonnegative
`mu delta^2` contribution as available slack and bounding the other
three error terms. It can succeed when the stronger two-component
relative cone fails.

## Shared theta representation and complete tails

The identity `phi_n(z)=n^(-1/2) phi_1(z+(log n)/2)` follows exactly
from the powers 9, 5, and 4 in the source. Translating each already
shifted horizontal channel gives Note 16's shared carrier, including
the staircase cutoff and both the real and imaginary logarithmic
weights. At the common phase center, the displayed Dirichlet-like
weights and heat factor have the correct exponents. The center is a
critical point of the specified common exponential phase; it is not
asserted to be a saddle of the complete prefactor.

The covariance split follows from
`(v-d_n)^2-b^2=(b-d_n)^2-b^2+2(b-d_n)(v-b)+(v-b)^2`.
In particular `delta_n=-b log n+(log n)^2/4` has the stated sign
and coefficient. The resulting products must retain all cross-index
terms. This is an exact reorganization, not a relative approximation.

For `0<=d_n<=v` and nonnegative time, `|A_n|<=n^(-1/2)` and the
partial sum of these absolute weights is at most `2 exp(v)`. This
gives the exponent `tau v^2+10v-pi cos(4a) exp(4v)` in the shared
majorant. Its second derivative is nonpositive on the tail under the
stated hypothesis `8 beta_V>=tau`. The tangent-line integral proves
(19). Multiplication by the centered residual is paid by
`S_(j+2)+b^2 S_j`, since `0<=v-d_n<=v`. The same conservative
degree-two replacement is valid for the original complete-index and
integration payments. Their overlaps may be overpaid safely.

The lower bound on the sum of absolute weights follows by retaining
indices between `ceil(M/2)` and `M`: each contributes at least
`M^(-1/2) exp(-t v^2)`. For fixed contour and
`t=theta/log x`, the right side has order
`x^(1/4-theta/16)`. The claimed divergence for `0<=theta<4` is
correct. It obstructs pointwise absolute first-channel dominance;
it is neither a lower bound for the modulus of the arithmetic sum nor
a statement about the fully integrated observation. The note preserves
this distinction.

The shared-carrier formulas and their new tail bounds were reviewed
analytically. They are not the retained quadrature representation used
in the finite pilot, which uses the existing complete shifted source.

## Whole-cell numerical proof and independent record audit

The driver takes the complete-source contour identity before truncating
the theta indices. Its finite center integrals are enclosed by Acb, and
both the entire omitted-index half-line and the complete integration
tail are paid. The Note 12 tail formulas hold for every nonnegative
integer jet order, so their use through orders 28 and 29 is valid.

The positive majorant integrates the absolute bounds on both source
prefactors and uses
`|u+ia|^r <= (u+a)^r` and
`|exp(t(u+ia)^2)| <= exp(u^2/2)` on the full time range. The uniform
normalization factor is correctly bounded by
`exp((c-a)x_c+a delta_x)`. The driver encloses the majorant's retained
integral and pays both of its complete tails. All moment integrands are
entire functions of the integration variable, so the Acb callbacks do
not ignore a branch restriction.

The Taylor transport first expands in time at fixed spatial position,
then expands each retained coefficient in space at the time center.
The remainder indices are correct: `r+2ell+12` for the spatial terms
and `r+16` for the time term. This needs center jets through 28 and
complete moment bounds through 29. The centered residual sequence
obeys the same recurrences because `a,b` are frozen on each cell.
Its coefficients are combined before transport; no derivatives of an
adaptive center or cutoff are silently discarded. The remainders are
uniform through all closed-cell boundaries, including `t=0`.

The exact rational audit reconstructs each dyadic endpoint, checks
the Cartesian cover of `[0,1/2] x [100,104]`, independently derives
the energy floors and residual-square upper bounds, and verifies the
positive cone slack. It finds 24 stationarity exclusions and 8 strict
stationary sign certificates for each of `j=0,1`. The second strict
sign is checked directly; it is not inferred from the cone alone.
The source and record hashes are checked against the actual files.

The replay yields a maximum certified `C^2/E` upper bound below
`0.072976664101`, minimum `mu` above `0.406343590205`, and a direct
physical norm floor above `4.58534762062436e-16`. The simpler statements

\[
|F|>4\cdot10^{-16},\qquad e^{\pi x/4}E>2700
\]

are also independently certified in the record auditor using rational
arithmetic: `pi<22/7`, a positive Taylor expansion with a geometric
remainder bounds the exponential, and the resulting deliberately wider
bounds still prove both inequalities on every cell. Thus the advertised
floors do not rely on rounded display strings. The source driver also
rounds its endpoint-derived energy lower bounds, residual upper bounds,
and aggregate norm floors outward explicitly.

With `eta=1/3` and `mu>=2/5`, the cone gives
`L_0>=E/15` on `h_1=0` and `L_1>=-5E/72` on `h_2=0`, as claimed.
Evenness reflects the band. Combining the new direct norm bound with
the established height-100 certificate therefore supports the stated
bounded exclusion and the previous `|F|>1e-16` floor through height 104.
The earlier certificate itself was not rerun in this review.

## Scope and remaining work

The finite cone proof is not circular: complete jet enclosures first
establish an independent positive energy floor on each bounded cell,
after which the residual cone is checked without an unverified norm
division. That procedure nevertheless supplies no relative theorem
through a hypothetical zero in the unbounded region.

The remaining obligation is a theta-specific signed estimate, or the
relative cone with locally bounded loss, throughout the padded
small-time region with the updated cutoff `X_0=104`. It must retain
the arithmetic cross terms, staircase transitions, and all contour and
derivative remainders. The positive-source collision controls of Note 15
continue to exclude an argument based only on generic positivity or
regularity. The note does not claim an arbitrary-height sign or an RH
proof; those qualifications should remain in any later manuscript use.
