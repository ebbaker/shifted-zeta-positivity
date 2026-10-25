# Chat0021: research results, dependencies and remaining work

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol, actual recorded effort ultra**
for this chat's research turns. Thread
`01a1751b-9ac5-7192-9f6c-b9f59ec30827`, registered uniquely as chat0021,
“Prove HDA-17 positive-source bound.”

## What the chat established

This chat developed a chain of four analytical results for the **same
complete IC23 construction**: a smaller positive source, a finite
evaluator/error ledger, an exact phase-index constructor using authorized
onset freedom, and polynomial additional-accuracy-bit evaluator/filter
cost at a fixed descriptor and query box for explicit rational/dyadic
scalar inputs and canonical providers. General computable scalar inputs
retain their own provider costs. These are proved-in-note
results with same-model internal assessments. No numerical or exact-
rational research algorithm was executed, and no independent full-chain
review or useful uniform height-cost theorem was obtained.

| Stage | Research result | Scope and limitation |
| --- | --- | --- |
| [Note58](58_POSITIVE_ANALYTIC_SOURCE_COMPRESSION_20261025.md), [Review37](../reviews/37_POSITIVE_ANALYTIC_SOURCE_COMPRESSION_ASSESSMENT_20261025.md) | Canonical complex square-root branch; positive squared-polynomial source; four-jet error and finite constructor cost | Fixed-b descriptor O(R^2 log R) bits for IC23. Source storage/construction, not evaluated runtime. |
| [Note59](59_EVALUATOR_WORKING_PRECISION_AND_CONTINUOUS_FILTER_20261025.md), [Review38](../reviews/38_EVALUATOR_FILTER_LEDGER_ASSESSMENT_20261025.md) | Cancellation-safe entire-moment evaluator; explicit provider, arithmetic, coordinate and continuous-filter errors for every retained scalar | Initially from certified fixed descriptor including exact phase integer. Finite sufficient cost can be prohibitive. |
| [Note60](60_EXACT_PHASE_INDEX_BY_DYADIC_ONSET_SELECTION_20261025.md), [Review39](../reviews/39_EXACT_PHASE_INDEX_ASSESSMENT_20261025.md) | Full implicit gamma-saddle phase expansion; four-onset separation; rational exact-ceiling selector | Uses the author's explicit “Use existing onset freedom” clarification. Previously fixed arbitrary-onset equality remains outside scope. |
| [Note61](61_POLYNOMIAL_ACCURACY_EVALUATOR_AND_FILTER_COST_20261025.md), [Review40](../reviews/40_COMPLETE_EVALUATOR_COST_ASSESSMENT_20261025.md) | Efficient log-Gamma/profile providers; rational high-order quadrature; complete polynomial accuracy-bit evaluator/filter cost | Descriptor and query box fixed, with explicit scalar encodings; arbitrary computable scalar costs retained separately. Constants can still grow exponentially with height. |

This advances the original [HDA-17-AN05 r1](../research-progress/handoffs/HDA-17-AN05.md)
source-compression packet and its subsequent analytical consumers. The
[sole progress register](../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
owns status; the [research overview](../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md)
owns the global objective and contracts.

## 1. Positive source compression: Note58

The inherited Notes54--55 prescription already supplied a finite
all-real-time/all-height analytical construction, with improved fixed-core
source conditioning. Its specified sufficient source descriptor had
log size pi R/32+O(log^2 R) at fixed parameters. This chat did not
reprove the entire inherited contour/transfer chain; it addressed the
next source representation and its consumers.

Note58 factors the **full** canonical source as Phi=A(1+R_tail),
proves an explicit normally convergent complex tail bound <1/2 on
Re u>-1/16, |Im u|<1/16, and constructs the canonical analytic
square root h with h^2=Phi and |h|<9. Thus real positivity was not
used in place of a complex branch proof. The branch includes all
canonical arithmetic modes.

A finite polynomial approximates h on[0,U]. Dyadic coefficient
rounding followed by squaring produces a nonnegative source f=p^2
on[0,U], zero beyond U. Its exact heat field G obeys

    |partial_z^j(G-H)|<=51epsilon/256,
    j=0,1,2,3, every t<=b, every real x, |Im z|<=4.

The error ledger separates source tail, arithmetic modes, approximation,
nodal data and coefficient rounding. At fixed b, with q_s=log(1/epsilon),
the degree is O_b(q_s log q_s), fractional coefficient precision is
O_b(q_s), and descriptor size is O_b(q_s^2 log q_s). For the unchanged
IC23 tolerance schedule this gives O_b,eta,theta(R^2 log R) bits,
with a finite polynomial constructor bound from certified recipe data.
AN05 closes at this bounded analytical source-construction scope.

The one source is fixed once per full target and then used throughout
time and height. No fixed-b asymptotic is substituted into a joint
accuracy/upper-time runtime theorem. Huge fixed constants remain.

## 2. Evaluation and continuous error ledger: Note59

Source storage does not determine working precision. Note59 expands
the Gaussian moments as an entire joint series in tU^2 and izU,
with no division by t or z. A finite factorial/common-denominator
implementation pays coefficient cancellation, coordinate rounding,
truncation and final arithmetic explicitly, including t=0,z=0.
It evaluates the same stored source, not a new approximation to H.

The nonsource providers cover normalized gamma logarithms, implicit
saddles and their jets, the fixed-index moving phase, the physical
regulator and flat profiles. Every raw scalar in the complete tuple
has a finite magnitude/derivative/error recursion. Continuous K
integration has a remainder between nodes; equation sums retain their
own component budgets. The signed covariance is recombined using the
**actual full filtered means**, including Delta Q.

With additional error schedule

    zeta(t,x)=theta/[4(1+t^2)(1+x^2)],

the inherited analytical comparison plus evaluation error remains
<=3theta_r/4 at each separately allocated scalar target. Additional
errors vanish at both time endpoints and both height ends. No finite
height cutoff, normalized surrogate density or omission of joining
defects is introduced. Early G use remains unbounded in real height.

The original sufficient gamma/profile/midpoint algorithms were finite
but could be exponential in requested accuracy bits and in height.
The first missing from-scratch discrete input was identified precisely:
an arbitrary-precision phase enclosure alone does not decide its literal
ceiling if equality might occur. Note59's original body is preserved;
its appended continuation points to Note60's scoped resolution.

## 3. Exact phase index with authorized onset freedom: Note60

The author expressly authorized **“Use existing onset freedom.”**
The construction therefore selects a member of Note54's original
admissible family before fixing X0 and all dependent source data.
It does not replace the literal ceiling rule by an upper integer.

For the actual full implicit gamma saddle at t=64, Note60 proves

    Theta(64,x)=x[log(x/(4pi))-1]/4
                 +4pi log(x/(4pi))+7pi/8+E(x),
    |E(x)|<=2^16(1+log x)^2/x, x>=exp(1000).

Expanding from q=ix/2 avoids applying the inherited EF3 outside its
right-half-plane domain. Completing the square pays the actual saddle
displacement and fixes the logarithmic correction and constant for the
unwrapped EV11 phase lift.

Let Q_j=Theta(64,2^(K+j))/pi for four consecutive admissible exponents,
K>=2048. The integer combination

    Q_3-5Q_2+8Q_1-4Q_0=4 log 2+error,
    |error|<1/100,

has integer distance >19/100. Since the coefficient absolute sum is18,
at least one Q_j has integer distance >1/100. Fixed-length elementary
rational series yield phase centers within2^-19. Radius1/1000 intervals
and exact rational1/200-margin comparisons identify a winner and its
**exact original ceiling**. Exact ties at rejected rational tests cause
no difficulty; no equality oracle is used.

The sufficient K includes **all** onset gates: the positive-band C_b^+
enlargement, target delta=theta/64 and pre-switch bridge maximum. The
winner precedes X0,R_c,L,sigma, source tolerance and coefficients.
Selector work is polynomial in K, the binary height length, not in
log K or the complete descriptor encoding. No equality theorem for
an arbitrary previously prescribed exponent is asserted.

## 4. Improved complete cost: Note61

The inherited flat-profile estimates already imply global Gevrey-3
spatial derivative bounds. Explicit algebra/reciprocal/log/exp rules
propagate them through every retained raw scalar and the polynomial
kernel factors, including smooth spatial seams and fixed time rows.

A composite rational degree-n interpolation rule with n=O(log(1/e))
and O(A n^2) panels per axis has O(A^2 n^6) tensor nodes. Its error
is proved from pure-axis derivatives. Negative weights are allowed
and their full amplification is paid: node accuracy loses only O(n)
bits. Rational weights share a common denominator, so exact summation
does not multiply a denominator for every node. Endpoint nodes use
the kernel's interior polynomial representatives, consistent with the
unchanged weak convolution.

Shifted Stirling with O(P) shifts and terms computes normalized
log Gamma and fixed polygamma jets at P-bit accuracy, with a proved
sectorial remainder and Cauchy derivative bounds. Efficient elementary
logarithms, finite Bernoulli recurrences and explicit arithmetic replace
the old1/delta-length product. This is not a unit-cost Gamma-value
oracle; downstream magnitude and cancellation costs remain.

The same rational high-order rule constructs the flat normalizer and
partial integrals with O(P^3) nodes. Tail tests avoid evaluating huge
inverse-distance exponents near flat endpoints. The inherited source,
implicit phase and regulator providers then all have polynomial
additional-accuracy-bit cost at a fixed descriptor and query box.

Combining those providers with **all** Note59 circuits, for exact
rational/dyadic independent parameters and the explicit canonical
recipes, gives the safe
bound C_(descriptor,Q)(1+p+I)^40 bit work and
C_(descriptor,Q)(1+p+I)^8 working storage. Here p is additional output
accuracy bits and I is query encoding length. General computable scalar
inputs retain their stated provider costs as a separate factor; fixing
an arbitrary computable real does not make its digits cheap. These are sufficient
polynomials with potentially enormous, computable constants; no useful
uniform height/time/descriptor-size runtime follows.

## 5. What remains unpaid

Raw density has genuine narrow peaks: the local model F=a(z-c),
delta=sqrt(q)/|a| has rho(c)=1/(pi delta^2). The present smoothness
constants still use inverse physical q floors, so height can be very
expensive even though additional-accuracy cost is now polynomial.

Note61 pays a separate useful lemma for weak logarithmic/simple-pole
primitives: on radius-h simple-root disks their L1 tails cost O(h^2
B_log) and O(h), with only logarithmic q dependence. Existing Note31
weak identities expose these primitives while retaining direct time
rows, signed heat terms and actual covariance. Deleting disks directly
from raw density/current/heat terms would lose mass or dipoles and is
not an admissible shortcut.

**Next: Analysis — Sol.** Complete the weak-filter height-cost ledger:
construct all relevant collars/guards; pay retained-domain normalized
providers, every weak-test and band commutator, L1 post-filter caps and
actual mean products; then prove the optional coordinate trace/time
moduli. The last moduli need special care at fourth kernel derivatives.
The puncture lemma alone does not close that complete consumer.

HDA-17 remains **Partial**, HDA-18 **Gated**, HDA-20 **unfulfilled**.
The distinct full inherited source/contour/collar/transfer/join audit
must include Notes54--55 and this chat's Notes58--61. Same-model
parallel checks and Reviews37--40 do not supply that independence.
HDA-21 remains a separate observable/window/limit/response specification.

The [result index](../../../../result-summaries/README.md),
[cluster13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md)
and [avoid index](../../../../avoid/README.md) bound interpretation.
Generic evaluation lemmas can hold for colliding controls; they prove
no sign or collision exclusion. The canonical full-source premises
and control-specific failures are recorded in each research note.

## Records and unchanged production scope

The [chat archive](../chat-histories/0021_2026-10-25T22-08-25Z_prove-hda-17-positive-source-bound.json)
retains the sole original registration and public history. Only the
authorized refresh tool updates it. Opening input manifests and small
zero-run records accompany each research turn. This summary is a
research index, not a second transcript or a proof source replacing
the detailed notes.

No source coefficients, gamma/phase/field samples, precision search,
numerical/exact-rational/machine-symbolic research runs or interval
campaigns occurred in this chat. Algorithms and costs were derived
on paper. Hashes, links and sizes are housekeeping, not mathematical
certificates. Manuscript remains through Notes54--55; no manuscript
production, DRAFT_HISTORY milestone, new snapshot or commit was made
in this chat. All user-requested analytical continuations and the
onset clarification were incorporated without changing chat identity,
model or recorded effort.
