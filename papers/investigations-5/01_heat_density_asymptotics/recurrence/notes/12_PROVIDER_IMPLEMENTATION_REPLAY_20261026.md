# R05-N01: bounded scalar/gamma and Gauss implementation replay

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from turn metadata. Recurrence chat0003, thread
`01a176ea-3f14-7972-bc9c-9aeb6fb50fd4`, turn
`01a17838-69d0-76c1-82a0-8e808ec78797`.

Return to [HDA-R05-N01 r1][packet]. **Complete at its bounded component scope; N01 CLOSED.** All 36 gamma
cases and all 15 Gauss base rules (45 exact affine deliveries) passed
production and separate-process certificate replay. The installed archive
consumer also checked source/data hashes and replayed all 51 certificates.
Broad HDA-R05 remains **Partial** at the remaining providers and field
evaluator. No complete canonical field certificate follows.
This is a bounded component implementation and finite certificate replay;
it is not the complete canonical field evaluator. [Inputs][inputs],
[execution record][record], code and [Review10][review] delimit the claim.

## Question, matrix and limits

Can the explicit shifted-Stirling gamma jets and exact Legendre
variation-count Gauss providers of [Note10][n10] deliver their declared
errors on the small N01 matrix in a reproducible implementation?

- Gamma: u in {1,32,256,4096}, J in {0,2,8}, P in {32,64,128},
  all 36 combinations. Outputs are normalized Taylor coefficients of
  the analytic log Gamma at (1+iu)/4, orders zero through J, each with
  complex absolute error <=2^-P.
- Gauss: s in {1,2,4,8,16}, P in {32,64,128}, 15 base constructions;
  three exact affine maps give 45 delivery records. Max base-node and
  total base-weight error are each <=2^-P. The intervals are [-1,1],
  [0,1/2], [3/8,3/8+2^-12].
- Total computation <=900 seconds, successful-worker measured peak RSS<=512 MiB,
  Gauss depth<=8192, sign-count queries<=250000, gamma expansion terms
  plus recurrence shifts<=4096 and primitive refinement<=8192 bits.
  Each primitive series also has an additional 4096-term cap. The gamma
  terms/shifts count refers to C1/C3's expansion and recurrence; aggregate
  elementary-series terms are reported separately. All computation,
  including separate-process replay, is charged to one persisted budget.
  The runner allocates at most 60 seconds to each child, within that total.

The standard-library Python Fraction/int backend is available; no external
package or system software is installed. Exact rational operations carry
no arithmetic error; dyadic output rounding is paid explicitly. No
optional floating-reference agreement is used as certificate evidence.
Environment and actual versions are in the execution record.

## Construction and certificate contract

### Gamma

The producer uses exact rational log/atan series with range reduction,
explicit scalar tails, a pi enclosure and separate dyadic centers/radii.
All complex-log arguments have positive real part. The gamma recurrence selects
the analytic unwrapped log Gamma branch. It uses m=P+2J+4,a=m+1 and
C1/C3's shifted Stirling expansion, an exact Bernoulli triangular table,
C4's analytic remainder, and explicit log-input/term-quantization costs.
Its complex L1 error radius bounds absolute complex error as well.

The gamma replayer bypasses the producer's refinement choices: it checks
the actual range-reduction identities, finite series orders and tails,
branch/type bindings, each scalar/complex center and radius, Bernoulli
recurrence digest, normalized coefficient formulas, C4 remainder and
all final jets. It shares finite formula helpers with the producer;
it does not independently prove those formulas or Python's arithmetic.
All 156 normalized jet channels pass. No external floating-reference
comparison was used or needed for the stated certificate replay.

### Gauss

Exact Legendre sign variation counts isolate all roots, retaining singleton
roots and correct open-interval endpoint conventions. We retain the same
C8--14 root/weight algorithm and use a certified local stopping refinement:
exact rational interval evaluation of J_s/P_s' on each bracket may prove
a separated denominator, positive true weight and the requested delivery
errors earlier than C12's very conservative global depth. The global
reference depth remains recorded as a bound; it is not treated as a
mandatory iteration count or evidence that the provider cannot work.
The interval argument is the P9/P11 quotient construction with local
separation paid directly, and it leaves the requested errors unchanged.

The Gauss replayer is separately coded: it rebuilds Rodrigues polynomials,
checks exact endpoint signs and root counts, complete disjoint root
coverage, singleton conventions, separated derivative intervals and
positive true-weight enclosures. It recomputes rational weights, output
error radii, all exact affine maps and all 558 polynomial-moment channels.
The moment checks are explicitly labeled shared-premise consistency
checks rather than independent mathematical validation. The s=1 cases
exercise exact midpoint roots; the short mapped interval introduces no
reciprocal-length loss. All orders include every reference node/weight.

## Evidence and measured work

| Evidence | Actual finite result |
| --- | --- |
| Gamma cases / delivered channels | 36 / 156, all delivered and replayed |
| Gauss base constructions / mapped rules | 15 / 45, all delivered and replayed |
| Moment consistency checks | 558, all pass |
| Targeted altered-data rejection checks | 10 rejected; two positive controls pass |
| Final installed hash-bound archive replay | All 51 certificates pass |
| Total computation, including failed launch, controls and final replay | 50.4055 seconds (rounded upward), below 900 seconds |
| Primary-run child peak RSS | 20430848 bytes, about 19.5 MiB; every successful worker checked<=512 MiB |
| Gamma expansion terms plus shifts per case | 72--296 |
| Gamma fractional output-grid bits / max requested primitive bits | 47--145 / 50--151 |
| Gamma aggregate primitive series terms per case / largest one series | 1150--30261 / 73 |
| Gamma largest observed Fraction numerator / denominator | 9056 / 9196 bits |
| Gauss isolation depth / sign queries per case | 1--147 / 1--2241 |
| Global C12 reference depth | 34--113247; six bounds exceed 8192 |
| Gauss tracked integer / Fraction operand size | 2395 / 113246 bits; includes global conditioning constants |

At s=16, P=32,64,128, the actual certified depths are 51,83,147 while
the global sufficient reference depth is 113247. The interval stopping
refinement therefore makes a material difference on this small matrix;
it is not an unproved claim that the global conditioning bound is sharp.
The original fixed-chart polynomial upper bounds are neither fitted nor
sharpened by these samples.

The three primary execution records retain the initial failure and final
case statuses. The final 51-certificate installed replay took 13.997 seconds
rounded upward and used the documented archive fallback, after checking
all expected code and data hashes. Detailed results, raw byte hashes,
canonical mathematical-content hashes and measurement methods are in the
execution manifest. The 51 regenerable certificate files total 3645034
bytes (largest 201229 bytes) and are retained outside Git; see
[ARCHIVES.md](../ARCHIVES.md). Hashes identify exact evidence, not its
mathematical validity.

The time figures describe these finite programs on this machine, not an
asymptotic fitted law or an end-to-end field cost. Process peak RSS is
measured with resource.getrusage. This Darwin runtime rejected both
address-space/data-limit setup attempts, including a backend setup probe
outside the filesystem sandbox. The successful worker instead samples
RSS with a watchdog and checks its process high-water value against the
512 MiB acceptance ceiling. No hard OS address-space cap is claimed. Exact temporary-bit figures state
their instrumentation coverage rather than imply every hidden language-runtime operand is seen.

## Scope, controls and disposition

**Numerics — Sol:** accept the stated finite provider deliveries and
certificate replay; N01 r1 CLOSED, requested bounded task Complete.
Broad R05 remains Partial. The code is a component implementation with
finite evidence, not a verified general field-evaluation library.

A first launch failed at process-limit configuration before gamma import
or calculation; [the preserved failure record](../numerics/01_N01_INITIAL_LIMIT_FAILURE_20261026.json)
includes its exact traceback and the subsequent unrun cases. It used
0.128 seconds of the shared budget. After the runner repair, the same
frozen gamma provider delivered every requested case. This is an execution
harness failure, not a failed gamma error bound; it was not erased or
counted as a successful delivery.

Preflight inspection also found and repaired primitive certificate-type
confusion: an angle child must certify atan, and log2pi's pi child must
certify pi. Input labels are now bound to mathematical replay inputs;
valid capped certificates are never counted as successful delivery;
source copies are frozen/hashed; and conservative child-time reservations
survive interruption. Focused tests alter final gamma centers/radii,
primitive kinds, Gauss weights/radii/root counts and mapped endpoints,
plus worker input labels and nonfinite JSON. All 10 are rejected. These
software corrections do not change any analytical formula or frozen
mathematical contract.

No final matrix cell reaches a requested mathematical cap, fails a
certified inequality or has a replay mismatch. The observational timing,
RSS and hidden-runtime limitations remain as stated; checker agreement
is not independent specialist or formal validation. Next **Analysis and
numerics — Sol**, [N02 r1](../research-progress/handoffs/HDA-R05-N02.md),
READY_FOR_SOL, not executed: pole-safe F_0 normalized jets and weighted
C_k software before composing the retained integral. The packet has its
own finite matrix, analytic-method obligations and stop limits.

Preserve the full canonical source,
all 2N arithmetic arms/modes, retained real RS integral and exact transfer
in the analytical theorem; this standalone test computes none of the full
field. It does not run at [Note11][n11]'s explicit enormous sufficient
height or extend the accepted descriptor class. No RH, physical-transfer,
regulator-uniform or joint-time conclusion follows.

This is finite software evidence for named provider contracts under
[avoid01][a1], not an RH criterion. The [result index][results],
[heat cluster][heat], [collision controls][controls], [avoid index][avoid]
and [shared-premise caution][a5] remain governing context. Those controls
lack the complete canonical theta/xi source and all-mode initial matching;
a heat identity alone supplies neither. Code/replay share mathematical
premises and remain same-model internal work, not independent specialist
validation or formal proof. Notes09--12 are not yet integrated into the
manuscript. R04/R06 NOT_STARTED; HDA-A02 Partial, HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain unchanged.

[packet]: ../research-progress/handoffs/HDA-R05-N01.md
[inputs]: 12_PROVIDER_REPLAY_INPUTS_20261026.json
[record]: ../numerics/01_PROVIDER_REPLAY_20261026.json
[review]: ../reviews/10_PROVIDER_REPLAY_ASSESSMENT_20261026.md
[n10]: 10_EFFICIENT_PROVIDERS_AND_TOTAL_COST_20261026.md
[n11]: 11_EXPLICIT_CALIBRATION_AND_HEIGHT_ONSET_20261026.md
[a1]: ../../../../../avoid/01_restating_the_target.md
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a5]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
