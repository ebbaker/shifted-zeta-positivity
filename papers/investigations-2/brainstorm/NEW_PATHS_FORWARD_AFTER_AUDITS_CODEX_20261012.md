# Research priorities after the arithmetic and Newman audits

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. Exact serving variant
and configured reasoning effort are not exposed and are not inferred.
Parallel model assessments are internal checks, not independent mathematical
validation. This brainstorm proposes research tasks; it establishes no new
zero-free strip, Newman bound, or RH mechanism.

The best next program has three parts: **independently scrutinize the
arithmetic argument now assembled; investigate the actual small-cofactor
obstruction to a shorter arithmetic moment; and test the stronger Newman
finite-sum inequality before committing to a large computation.** Complete
certificate auditing can proceed alongside that last feasibility study.
The other four investigations should remain bounded support projects until
they identify a source of information that these two main routes lack.

The starting point is the requested
[11 October Codex brainstorm](../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md),
read in full, together with the investigations, dated notes, reviews and
small numerical records. Its distinction between a sufficient estimate and
a circular proof remains essential. So do its exact diagonal tests,
certificate domain contracts, and requirement to stop when a reformulation
supplies no new estimate.

## What has changed since the earlier brainstorm

| Earlier task | Current evidence | Consequence for the next task |
| --- | --- | --- |
| Audit one complete nonempty arithmetic branch | The arithmetic project reports internal closure of the full pinned main-theorem chain under its identified inputs | Move to independent reconstruction and extensions beyond the proved parameter range |
| Benchmark the corrected heat interface | The benchmark is negative for the Gomila certificate's current uniform finite lane | Preserve that stop decision; examine the finite-sum lower bound instead |
| Replay the delicate finite rows and transfer gate | The Newman notes enclose 32 selected row values and reverify the plain-weight Dini gate with substantial slack | Audit the remaining analytic and computational suppliers rather than collect more isolated matching rows |
| Specify the actual covariance families | The other four folders remain scoped; earlier work already supplies much of the bookkeeping | Consolidate once, choose one surviving signed target, and require a matched theorem before expansion |

The arithmetic conclusion is an internal audit conclusion, conditional on
its classical imports and the reviewed interfaces. The Newman conclusion
is partial auditing of a pinned public candidate. Neither changes the
independent-validation status of the underlying mathematical claims.
See the
[arithmetic final assembly review](../arithmetic_source_audit/reviews/FINAL_ASSEMBLY_REVIEW_20261012.md)
and
[Newman finite-lane audit](../newman_certificate_audit/notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md).

The portfolio README contains unresolved merge markers and overlapping
status passages. Resolve that presentation issue before packaging a
portfolio for review; use the dated project records for mathematical
status in the meantime.

## First priority for confidence in the arithmetic argument

Prepare a compact package from which a specialist can reconstruct the
reflection-to-sieve interface without adopting the audit's conclusions.
The current audit considers this interface closed; the next step changes
the level of scrutiny rather than alleging a newly discovered gap.

The package should pair each imported theorem with the actual object to
which it is applied. The most valuable checks are the conjugated cusp
coefficients and phases; reduced denominators when a fixed Fourier
frequency is a nonunit; the fixed ray partition and moving-row uniformity;
simultaneous exceptional-prime terms; and the common Mellin majorant used
before taking row sums. Keep the special Gauss coefficient family visible.
The quadratic large sieve does not become an arbitrary sextic coefficient
estimate by changing notation.

The direct primary comparison is with Dunn–Radziwiłł, while the audit did
not directly read Patterson's original proof. In particular,
[Dunn–Radziwiłł Lemma 5.2](https://arxiv.org/html/2109.07463v3#S5)
assumes coprime Fourier support; the local reconstruction supplies the
additional nonunit treatment. Match the precise Hecke-family hypotheses in
[Goldmakher–Louvel Theorem 1.1](https://arxiv.org/html/1112.1642v2#S1)
to the completed family rather than cite a generic large-sieve slogan.
The detailed local starting points are the
[theta primary-source comparison](../arithmetic_source_audit/notes/THETA_PRIMARY_SOURCE_COMPARISON_20261012.md),
[cusp and uniformity audit](../arithmetic_source_audit/notes/THETA_CUSP_AND_UNIFORMITY_AUDIT_20261012.md),
and
[sieve and summation audit](../arithmetic_source_audit/notes/COMPLETED_MEAN_SQUARE_SIEVE_AND_SUMMATION_20261012.md).

**Bounded deliverable:** a theorem-to-application contract and one
self-contained reconstruction of the most delicate interface, with exact
source revisions. An independent mathematical review would be the next
substantial gain in confidence. Further model agreement is useful checking
but does not supply that review.

A complementary diagnostic could evaluate both sides of a few complete
theta reflection identities with rigorously bounded infinite tails.
Choose adversarial examples: a nonunit frequency, each nonidentity cusp,
shared squarefree and cube factors, and a simultaneous exceptional-prime
collision. Unlike the existing finite arithmetic checks, this would test
an analytic identity. A mismatch beyond the enclosure is actionable;
agreement remains diagnostic. Begin only if both truncation bounds can be
justified. More millions of finite assertions about already checked
identities would add less information.

The quantitative introduction corollaries, effective constants, and later
stronger strips are outside the assembled main-theorem audit. A targeted
audit of one such consequence is reasonable if a particular application
needs it. It should preserve conductor and height dependence explicitly;
qualitative fixed-character continuation alone does not supply an
effective family estimate.

## Highest priority for new arithmetic

The useful target is a genuinely shorter moment for the original Möbius
family. Fix the field, character, exclusions, and smooth profile as in the
existing work, and retain the physical deletion zeros:

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(p^6)=\mathbf1_{p\nmid n}.
\]

For one fixed \(0<h<1\) and \(a\ge0\), the proposed new estimate is

\[
(M_{h,a})\qquad
\sum_{0<Nu\le D^h}|A_u(D)|^2
\ll_{\nu,S,W,h,a,\varepsilon}D^{1+a+h+\varepsilon}
\quad\text{for every }\varepsilon>0.
\]

The existing
[short-family extraction refinement](../../quasi-rh-exponent-descent/short_families/notes/1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md)
already shows that finite reuse of this single moment removes the
prime-mask error. Its conditional consequence is

\[
|A_1(D)|\ll D^{b+\varepsilon},\qquad
b=\frac{1+a}{2}+\frac{5h}{12}.
\]

For a zero-free conclusion, the moment must hold for every admissible
smooth profile, or a profile class with no common Mellin zero. A single
fixed profile supplies its own Möbius-sum bound.

Thus there is no extraction problem left to solve by another iteration
scheme. The analytic moment is the missing input. It beats the audited
\(11/12\) boundary when \(a<5(1-h)/6\), and beats \(7/8\) when
\(a+5h/6<3/4\). For example, \(h=2/3,a=0\) would give \(7/9\),
through the already known finite chain
\(1\to8/9\to64/81\to7/9\). This is a measure of the proposed
estimate's strength, not evidence that it is available. A fixed positive
\(h\) leaves a positive distance from \(1/2\).

The audit now localizes where an extension must work. With original row
length \(H_{\rm orig}=D^h\), the initial scale formulas suggest

\[
\mathcal H\lesssim\frac{D^2}{H_{\rm orig}B^2},\qquad
\Sigma=D/B,\qquad
\frac{\mathcal H}{\Sigma}\lesssim\frac{D^{1-h}}B.
\]

Here \(B\) is the original cofactor shell, and \(\mathcal H\) is the
dual row length. These formulas diagnose the proposed extension; the
initial reduction and every subsequent estimate still need justification
in the new range. For \(B\) larger than \(D^{1-h}\) by a fixed
power, the familiar positive-gap geometry is available at the level of
scales. The small shells, including \(B=1\), lack that gap. Start there,
rather than repeat the entire old induction.

One plausible probe is to retain the exact signed return restriction
\(\tau(r)\mathbf1_{f'\mid k'}\) longer, before enlarging the ranges
by positivity. Reparametrize \(k'=f'm\), retain the exclusion
\((r,n)=1\), and measure whether the actual restricted sum is smaller
than the envelope used in the existing proof. The
[return ledger](../arithmetic_source_audit/notes/TWO_POISSON_RETURN_AND_TERMINATION_20261012.md)
and
[signed arithmetic ledger](../arithmetic_source_audit/notes/TWO_POISSON_ARITHMETIC_LEDGER_20261012.md)
give the exact starting objects.

The mandatory negative control is the unit sector. When \(F=R=1\),
the returned ratio is still \(\mathcal H'/\Sigma'=\mathcal H/\Sigma\).
The restriction \(f'\mid k'\) retains \(f'=1\); a cube cutoff below
one retains the unit cube. Saving on large twists or nonunit cubes alone
therefore cannot close the extension. Increasing the independent transfer
target can create a gap only by paying the larger target; it does not
supply the desired bound at the original scale \(\Sigma=XF\).

**Bounded deliverable:** one exact small-\(B\) branch, including its
unit descendants, with an explicit target saving and a named analytic
input. Continue if a modified transform, a signed covariance estimate, or
an arithmetic convolution identity supplies information beyond the
current envelopes. Stop the extension attempt if all it does is return
the same unit sector at the same ratio.

Keep three families distinct: the original \(\mu_K\nu\) moment above,
the canonical Gauss coefficient energy, and the auxiliary compensated
responses in the old short-family program. Their normalizations and
coefficients differ. A theorem for one does not automatically control the
others. In particular, the
[deletion-mode covariance ledger](../../quasi-rh-exponent-descent/short_families/notes/29_DELETION_MODE_COVARIANCE_AND_FULL_RESPONSE_LEDGER_20261009.md)
shows why subtracting a scalar coherent mean does not repair those
auxiliary responses: local deletion modes and the full complement still
need payment.

## Newman auditing and the sharp finite-sum option

The corrected-interface benchmark should stay closed for the present
uniform triangle lane. The smaller residual belongs to a different
corrected center; it cannot simply replace the error budget around the
old sum. The finite lane's lower-bound mechanism is the relevant lever.
The reported local sensitivity estimate of a possible gain around
\(10^{-8}\) is useful scale information, not a proved global optimum.
See the
[benchmark](../newman_certificate_audit/notes/2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md)
and
[cross-model review](../newman_certificate_audit/reviews/1_CROSS_MODEL_REVIEW_OF_NOTES_1_2_20261012.md).

Complete the audit in four concrete pieces:

1. Match the barrier's derivative majorants and prism gate to Polymath
   Lemma 8.4, including the certified constant-cutoff contract
   \(N=690988\), normalization, \(B_t\ne0\), and the extension to
   \(t=0\).
2. Independently map the uniform \(E_{\max}\) calculation from its
   analytical inequalities to the interval code.
3. Audit the infinite tail's contraction, monotonicity gates, and overlap
   with the finite lane.
4. Check the finite producer's frozen-weight and amortized calculations,
   remainder bounds, coverage, and strict parsing. The 32 selected row
   values evaluated at \(t_0\) do not independently certify all 3,149,013
   rows or every time box.

The old text-extraction obstacle is no longer a reason to defer the first
task: the primary
[Polymath HTML contains Section 8 and Lemma 8.4](https://arxiv.org/html/1904.12438v2#S8).
Its published derivative statement excludes natural cutoff jumps. Verify
the constant-cutoff contract for this barrier and require explicit jump
handling wherever a different certificate crosses a natural cutoff.

For a possible improvement, the new audit identifies a bounded experiment.
At the same \(X\) and \(y_0^2=0.0350708\), the sharp weight is
positive at four sampled leg starts at \(t'=0.157\). The corresponding
objective would be

\[
t'+y_0^2/2=0.1745354.
\]

This is a candidate value, not a bound. The samples do not establish the
whole finite lane, its \(y\)-transfer, its error budget, or its tail.
The existing initial-height hypothesis and barrier domain can be reused
at smaller \(t'\), conditional on the validity of their suppliers.
The final-time height range expands to
\(y\le\sqrt{1-2t'}\approx0.82825\); the changed transfer and tail
must cover it.

**Test the tail and the transfer before a full sweep.** The present
tail contraction is close to one, \(D_{\rm tail}\approx0.99972\).
Lowering time lowers the relevant exponent and may force a much later
tail start \(N_*\). Screen that cost first. In parallel, derive the
sharp \(y\)-transfer using the reviewed expression

\[
U_g(b,a)=\frac{|b-g^2a|+g|a-b|}{1-g^2},\qquad 0\le g<1,
\]

with the full normalizer and correction costs. Its monotonicity in the
\(\gamma\)-bound already supports the window-freeze argument; its
dependence on \(y\), including absolute-value switch surfaces, needs
new control. The old plain-weight Dini gate is not the new gate.

If termwise monotonicity fails, try one bounded alternative: certify the
aggregate sharp bound on a short lower \(y\)-strip and switch to the
plain lane where it becomes safely positive. That requires enclosures at
every join, every row window, and the tail. Failure of a termwise proof
does not disprove aggregate positivity; an expensive partition with no
useful certified gain should end the attempt.

Only after those gates close should a pilot certify difficult row runs
and estimate the full sweep cost. A later tiny joint parameter search can
stay inside the existing barrier rectangle:
\(t'\le0.16125\), \(y_0'\ge0.1809\), with \(y_0'\le1\) and
the criterion's other conditions. This is a domain inclusion, not
validation of the old barrier or the new final-time lane.

There is also a concrete cost improvement to try before parameter or
mollifier searches. The exploratory replay scans the full \(DN\)
range, while the certified checker already enumerates contributing terms
by gcd patterns. Port that sparse enumeration and cache reusable
logarithms. Benchmark one unchanged row and one sharp row before expanding
the search. A larger mollifier is a later experiment, since each added
prime enlarges the divisor-pattern transfer problem.

## Compare other certificate methods before a bound campaign

A sharp Gomila lane could be a useful proof or software contribution even
if it is not the strongest publicly claimed bound. The
[Gomila package](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit)
still labels its \(0.1787854\) claim as not peer reviewed. The pinned
[Gordon version 1.0.0](https://github.com/stefangordon/dbn-upper-bound/blob/v1.0.0/README.md)
claims \(0.157656619\ldots\) and explicitly retains analytic inputs
in its partial Lean theorem. A prospective \(0.1745354\) result would
not outperform that numerical claim; the claims' validation status must
remain separate from the numerical comparison.

Before extending an optimization campaign, compare the criterion,
source inputs, covered domains, proof-to-code obligations, and source
availability of the two methods. In particular, identify whether the
second method supplies a phase-sensitive lower bound or other information
lost by the current triangle lane. Such a comparison can locate an
actual new analytic lever without running another giant sweep. A partial
formal theorem is useful only with its remaining assumptions printed.

[Planat version 2](https://arxiv.org/abs/2609.37164v2) offers a different
comparison: collective contraction and off-zero logarithmic derivatives,
with its claimed improvement stated relative to the unreviewed base
certificate. A bounded theorem-to-interface comparison is reasonable;
using that claim as an established rigidity theorem would exceed its
present review boundary.

The question for another corrected-evaluator benchmark is whether a
pinned method actually loses feasibility or time to approximation error
in a domain covered by the interface. The negative Gomila benchmark does
not answer that question for every method. Require a specific difficult
cell and complete budget before reopening evaluator work.

## Use the quadratic covariance as a precise diagnostic

The quadratic checkpoint is valuable because it names an actual signed
form and pays several sectors already. Use its prepared profile
\(\ell\), including \(\widehat\ell(1)=0\), rather than an arbitrary
prime weight. At the existing example,

\[
Q=X^{3/5},\quad \Delta=X^{3/8},\quad
J_Q(k)=\sum_{\substack{a\le Q\\a\ \mathrm{odd\ squarefree}}}
a^{-1/2}(k/a),
\]

\[
F(X)=\sum_{\substack{p,q\ \mathrm{odd\ primes}\\|p-q|>\Delta}}
c_p\overline{c_q}J_Q(pq),
\qquad c_p=\log p\,\ell(p/X).
\]

The
[separated-prime checkpoint](../../quasi-rh-exponent-descent/integer_quadratic_lift/notes/3_SEPARATED_PRIME_PAIR_CHECKPOINT_20261009.md)
gives

\[
\mathcal W_{7/5}(X)=F(X)+O_\varepsilon(X^{67/40+\varepsilon}).
\]

The desired estimate is the **one-sided** bound
\(F(X)\ll X^{17/10+\varepsilon}\). The diagonal, prime-power
terms, and near pairs fit below that budget. Entrywise absolute values
still cost at least order \(X^2\). The previously available favorable
scalar/sieve combination has exponent \(15/8\), leaving a saving
\(7/40\) to find. This is substantial new information, not a small
normalization improvement. The full target also controls the simultaneous
odd quadratic family, including the principal row; it does not concern
zeta alone. See the
[quadratic strength and barrier note](../../quasi-rh-exponent-descent/integer_quadratic_lift/notes/2_QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md).

**Bounded deliverable:** match one named dispersion, bilinear, or spectral
input against this exact kernel, prepared profile, squarefree-removal
masks, and conductor range. Keep the signed pair sum intact until the
candidate input acts. Classify what it actually supplies: a smaller
sector, the full target, or a mismatch. Continue only if it beats the
known envelopes on a surviving sector and accounts for its complement.

This is a good diagnostic project, but I would prioritize the
source-informed small-cofactor sextic probe for fresh arithmetic. The
latter has a fully audited transform structure to interrogate; the
quadratic route presently needs a major new signed estimate.

## Keep the remaining experiments small and faithful

**Function fields.** Start after choosing an integer ledger. Specify the
field, character order, nonprincipal base twist, row and modulus degrees,
deletion masks, and limiting regime. Compute diagonal, coherent mass, and
signed covariance exactly for one small matched family. For a sextic
model, include the residue-field conditions needed for order six. For a
quadratic model, keep the analogue of the prepared probe and principal
mask. Untwisted polynomial Möbius sums in degree at least two vanish and
would conceal the intended signal. A large-field fixed-degree theorem
does not control growing degrees automatically. Continue only if a
matched theorem or exact model reveals information beyond known diagonal
and coherent terms. See the
[function-field scope](../function_field_covariance/README.md).

**Heat counterkernels.** Complete the feature table first: full counting
law, linear term, remainder, simplicity, and quantifiers in positive heat
time. The existing counterkernel already survives a leading-density test.
One finite-zero surgery is worth studying only with a global positivity
strategy, such as a positive margin on a compact kernel interval and an
analytic tail comparison. Changing finitely many zeros alters a count by
\(O(1)\) at the surgery time; it does not automatically preserve the
required heat evolution or eventual reality and simplicity. An early
necessary moment condition may reject a candidate, but passing it does
not prove positivity. Continue for a counterexample satisfying every
declared feature or a precise construction obstruction, not because a
bounded scan looks positive. See the
[counterkernel scope](../heat_counterkernel_features/README.md).

**Weil packets.** Run one complete cost comparison at declared
\(a\ge a_{\min}>0\) and \(|\gamma|\le T\). The negative contribution
\(-4\Phi(a)^2\sinh^2(aL/2)\) is real information, but all other zeros,
archimedean and pole terms, the prime side, error, and conditioning still
matter. The support reaches a prime scale of order \(e^{L+2w}\).
There is no supplied positive lower bound on displacement, so this should
remain a finite detection experiment. Continue if the complete certified
test improves the existing basis at the same target and cost. See the
[Weil scope](../weil_two_packet_detector/README.md).

**Joint-jet persistence.** Keep the earlier brainstorm's sublevel-area
idea parked unless an actual-source estimate is identified. A collision
with Lipschitz budget \(K\) forces area at least
\(\pi\varepsilon^2/K^2\) on an interior patch. A nondegenerate
collision naturally has sublevel order \(\varepsilon^2\), so an
ordinary estimate of that order need not exclude it. Another conditional
criterion would add little; a source-specific improvement of the order or
constant, with uniform budgets, would be the advance.

## Suggested order and stopping decisions

| Order | Next deliverable | Continue when |
| --- | --- | --- |
| 1 | Arithmetic import contracts and specialist reconstruction package | Independent scrutiny supports the actual deep interface or identifies a precise correction |
| 2 in parallel | Newman barrier, error-budget, tail and producer audit | Every supplier and its domain can be checked from the pinned source |
| 3 | One small-cofactor short-moment branch, retaining the unit sector | A named new input produces a paid saving or contraction there |
| 4 in parallel | Sharp Newman tail and transfer feasibility test | Both close with a credible full-lane cost and a useful certified objective |
| 5 | Exact covariance consolidation and one theorem match | The source controls a surviving signed target beyond current envelopes |
| 6 | One matched function-field model | The family, masks, limit and mechanism match the chosen arithmetic target |
| Optional | One counterkernel construction or finite Weil comparison | It answers the stated conjunction or improves the complete finite detection problem |

For a near-term concrete certificate contribution, the sharp-lane pilot
has the clearest measurable outcome. For a stronger arithmetic theorem,
the small-cofactor short-moment problem is the most directly motivated
new target. For confidence in the existing claims, completing the
remaining independent review obligations has the highest value. None
currently provides a path all the way to RH.

Save follow-on derivations in each investigation's `notes/`, reproducible
code and small records in `numerics/`, and scoped assessments in
`reviews/`. Follow [LARGE_FILES.md](../../../LARGE_FILES.md): large sweeps
remain external with reproducible parameters, stored and canonical-content
hashes, a tracked lookup guide, and hash-bound consumers. Keep manuscript
sources stable and record notable milestones in concise `DRAFT_HISTOR.md`
entries; do not create draft snapshot folders.
