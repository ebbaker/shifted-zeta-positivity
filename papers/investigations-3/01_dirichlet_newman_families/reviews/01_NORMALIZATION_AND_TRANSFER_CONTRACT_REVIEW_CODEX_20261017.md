# Review of the normalization and transfer contract

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: **gpt-6.1-sol (Codex), reasoning effort ultra**, as recorded in
this session. Three same-model subagents assisted with separate analytic
and numerical checks; the reviewer reconciled their findings. This is an
**internal cross-model LLM review** of Claude Opus 5.5's work, not independent
specialist human review.

## Disposition

**Accept the normalization and elementary strip reductions; request targeted
revisions to the contract and its reporting. No quantitative upper-bound
milestone is accepted.** Lemma 1.1, Corollary 3.2, the paired-zero algebra of
Proposition 3.3, and Lemma 3.4 check out. Proposition 3.1 remains a proof
sketch. Lemma A has a character-conjugation convention error; Lemma
\(A_p\), confinement H12, and every character-specific barrier remain open.

The investigation has delivered a useful feasibility contract and a more
specific analytic question. It has not supplied an unconditional bound
below \(1/2\) for any character, a conductor threshold, or a family theorem.
The correct next work is a bounded analytic estimate for \(A_p\) and H12,
after the repairs below. A conductor sweep, density campaign, or manuscript
milestone would be premature.

## Scope and version

Reviewed the [coordination note](../notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md),
[initial proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md),
two numerical programmes and their records, and the investigation's status
and source ledgers. Repository HEAD at inspection was
`efba736a0494695a0909edd531679d7b678f7e84`; the file identities below pin the
actual material reviewed. Line references refer to these versions.

| File | SHA-256 |
| --- | --- |
| Note 01 | `8e6ea15793b0a753a789f6f03dc86174438c8df507afd2a0d4671249c7f76b4e` |
| Initial proposal | `d74769e6f0d6be45d972ec5f377645e5bfbb8ef40ccea19937af8095854e0a17` |
| Normalization programme | `b6a1b383aa73a6c453aec9d91e62056cdd91f928fd04ccedb99a1fc2a6ca6273` |
| Normalization record | `d37d6cb71fad823733f5d8838641cdea4867ac637db8d1901b8bed6b10822857` |
| Benchmark programme | `07ec4ac02e4ef73c90c4e621a688d8ac6296132501c9fa5ce8b353a7ed06fafc` |
| Benchmark record | `828f89b02f427a089ed186e60b97d5fab10b89cd62c8e65c3b8fdc12df8310bd` |

This review follows the [result-summary index](../../../../result-summaries/README.md)
and [avoid index](../../../../avoid/README.md), especially
[summary 08](../../../../result-summaries/08_character_channels_ccm_and_detector.md),
[summary 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid 01](../../../../avoid/01_restating_the_target.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md), and
[16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
The target is a positive quantitative upper-bound milestone, not an
RH-equivalent criterion. Any negative conclusion below is restricted to
its tested assumptions.

The note has since been moved into `notes/round-1`, with relative links
rebased. Its [relocation receipt](../notes/round-1/RELOCATION_20261017.json)
records both hashes; the table above retains the as-reviewed identity.
The [round-2 continuation](../notes/round-2/02_BURGERS_FLOOR_AND_CONDITIONAL_COMPARISON_CODEX_20261017.md)
addresses the analytic repairs and is not independently assessed by this
original review. The note now also carries a dated literature correction.
The [round-3 proof and manuscript check](02_SINE_TAIL_AND_MANUSCRIPT_CHECK_CODEX_20261017.md)
records the later comparison without H12; the disposition above remains
the historical assessment of round 1.

## What checks out

**Normalization.** Direct Mellin substitution recovers the factor
\(4\alpha_\chi(\pi/q)^{\mathfrak a/2}\) in the kernel. The phase condition
\(\alpha_\chi\varepsilon(\chi)=\bar\alpha_\chi\), Hermitian functional
equation, reality on the real axis, conjugate-character relation, and
\(z=2\gamma+i(1-2\beta)\) are consistent. Complex characters require both
height directions as the note states. Dobner's Fourier normalization and
strip theorem agree with the ledger. Polymath's factor \(H_0=\xi/8\) is
also consistent. These imports were checked against
[Dobner, equations (4)–(8) and Theorems 1–3](https://arxiv.org/pdf/2005.05142v2)
and [Polymath](https://arxiv.org/pdf/1904.12438v2).

**Conditional baseline.** Corollary 3.2 follows from the initial strip and
de Bruijn contraction, and all four displayed constants are algebraically
correct. The hypotheses concerning the claimed half-planes remain
conditional. This review does not re-audit their underlying proofs or
formalizations.

**Paired-zero inequality.** The polynomial numerator in note lines 386–392
has the correct sign when \(p^2\ge5h^2\). Removing the zero's own conjugate
pair yields exactly the term \(8Q/(p^2-Q)\). Real zeros have half-pair
weight. With the regularization repair below, the vertical calculation
needs no evenness. It agrees with
[Hakimoglu-Brown, Section 4 and equation (18)](https://arxiv.org/html/2610.12803v1).

**Time-zero floor.** Lemma 3.4 has the correct sign, factor \(1/2\),
digamma argument, and Euler-product allowance. The reflected point is
\((1+p+ix)/2\) for the same character. Monotonicity of
\(\Re\psi(\sigma+i\tau)\) and the absolutely convergent Euler product give
the stated uniform lower bound. This supplies an explicit arithmetic
input at time zero; it does not establish its positive-time persistence.

**Conditional comparison.** Given a valid \(A_p\), positivity of \(g\),
and H12, the nonlinear comparison has the intended form. If
\(T_b=\int_b^a g(Q)^{-1}\,dQ\), then
\(\Lambda_\chi\le T_b+b/2\); the limit \(b\downarrow0\) is legitimate
because \(g(0)=2\). Strict comparison barriers and backward Hermite
splitting address multiple contacts. The note correctly leaves H12 open;
zeta confinement in the cited preprint is not a character-family theorem.

## Required revisions

### R1. Correct the character orientation in open Lemma A

Note lines 336–342 use \(\chi(n)\) in the dominant sum at
\(s_B=(1+y-ix)/2\). The established normalization instead gives the exact
identity

\[
H_{0,\chi}(x+iy)=\bar\alpha_\chi(q/\pi)^{s_B/2}
\Gamma\!\left(\frac{s_B+\mathfrak a}{2}\right)L(s_B,\bar\chi).
\]

Thus the intended gamma-normalized dominant sum carries
\(\bar\chi(n)\), and the reflected sum carries \(\chi(n)\). This is
invisible for real characters and matters for complex ones. The
[Dirichlet functional equation](https://dlmf.nist.gov/25.15.E5) confirms
the conjugation. Correct the formula or explicitly relabel the family and
its normalizer throughout. The still-unspecified normalizer and error mean
this is a defect in an open contract, not a counterexample to a completed
approximation theorem.

### R2. Complete the non-even barrier proof without splitting divergent sums

The expression in lines 261–265 separates \(\sum_k1/z_k\) from the
canonical Hadamard terms. Conjugate pairing makes the counterterms real;
it does not prove that their real sum converges. For example,
\((z^2+h^2)/\Gamma(1-z)\) is real entire of order one, has highest simple
zero \(ih\), and contributes the divergent harmonic sum from its positive
integer zeros. Keep genus-one terms together and include a possible
factor \(z^m\), or take imaginary parts before separating sums. The
vertical velocity then has absolutely convergent paired contributions.

State the needed order and reality properties for \(H_{t,\chi}\) at each
time, rather than only for an initial \(H\) in Proposition 3.3. The kernel's
double-exponential decay gives the required upper growth bound
\(\log\max_{|z|\le R}|H_{t,\chi}(z)|=O_{\chi,T}(R\log(2+R))\) on bounded
time intervals. This does not prove H12.

There is also a strictness point missing from Proposition 3.1's sketch.
The printed proof of [Polymath, Proposition 3.3, pp. 15–16](https://arxiv.org/pdf/1904.12438v2)
uses the extra zero \(-x-iY\) to obtain \(y'<-1/Y\). A non-even character
has no such automatic partner. Supply strict negativity from another zero
or conjugate pair, using the barrier geometry and the Dirichlet flow's
infinitely many zeros, or use a strict perturbation argument. The two-sided
rectangle correctly removes the original imaginary-axis positivity
requirement. These are repairable proof obligations; retain “proof sketch”
until they are written.

Finally, lines 320–325 call the exceptional-set inclusion a direct
contrapositive, although the proposal counts \(\Re s>\sigma_*\) and the
proposition assumes exclusion at \(\Re s\ge\sigma_*\). A short limiting
argument repairs this: increase \(y_0\) slightly, shrink the barrier width,
cover the added final exterior strip with the original barrier, apply the
criterion, and let the increase tend to zero. At \(\lambda=1/2\), the
unconditional strip bound already suffices. Write this argument before
using the strict counting convention.

### R3. Restrict the stopping conclusion to the tested row transfers

Lines 497–515 and 652–658 demote first-term dominance at existing verified
heights. The benchmark tests two transfers of published parameter rows,
using unmollified leading components. It optimizes neither mollifiers nor
the full parameter space. Every displayed triangle margin is negative,
including those at the published calibration rows. Consequently these
tests establish neither a feasible first-term certificate nor a lower
bound ruling another one out.

The justified decision is to demote **these leading-order row-transfer
models** relative to the proposed strip comparison. Other dominance
arguments remain untested. This is a research-priority decision, not an
obstruction theorem. Also replace “keeps both components at their
calibration values” with “keeps them comparable”: the Polymath A-tail
changes from approximately 1.83764 to 1.74475, and its B-part from 0.681844
to 0.685997.

### R4. Qualify byte reproducibility and numerical terminology

Both programmes were replayed with their documented commands, directing
output to temporary files:

```sh
python3 -I check_character_normalization_claude_20261017.py
python3 -I benchmark_family_contract_claude_20261017.py
```

The actual runtime was Python **3.10.0**, macOS **27.0.1**, **arm64**
(`/Library/Frameworks/Python.framework/Versions/3.10/bin/python3`). All four
source/record hashes in the numerical README match. The benchmark output
is byte-identical to its stored record. The normalization output has hash
`6be33b5e7947673715ddacbe14a2fb9e57620f20ab1f35109381f68810a7ed9a`,
with 256 differing scalar leaves, mainly near-roundoff residuals. Its
worst transform discrepancy is \(3.6648607808\cdot10^{-9}\), versus
\(3.66486038042\cdot10^{-9}\) stored; quoted zero differences stay below
\(2.9\cdot10^{-13}\). The substantive normalization diagnostics survive.

Restrict the byte-identity claim in `numerics/README.md` lines 54–56 and
the normalization programme's opening docstring to tested environments.
Rounding to 12 significant figures does not make small floating residuals
portable. Keep exact file identity distinct from tolerance-based agreement.

In note lines 564–565, replace “integrated exactly” and unqualified
“optimized” with numerical integration and minimization over the stated
grid. The programme uses Simpson quadrature and 801 candidate heights.
An independently derived closed-form rational integral reproduced all 28
large-conductor times within \(4.7\cdot10^{-13}\); sampled quadrature and
grid refinements do not change the displayed three-decimal conclusions.
These remain diagnostics, not interval certificates.

### R5. Count conjugacy classes, not distinct constants

Note lines 517–519 and the benchmark output label counts of 938 and 92,718
as distinct values/classes of \(\Lambda_\chi\). They count primitive
characters modulo conjugation. Different classes can have the same
constant; under GRH and Dobner's lower bound all would equal zero. Replace
this with “conjugacy classes requiring checks” or “potentially distinct
constants.” The counting arithmetic itself checks out.

## The next estimate must include an actual loss budget

The zero-loss tables are correctly marked planning, but Section 6 permits
\(\delta\le C/4\). That loss materially changes the conductor at which
the comparison beats the conditional baseline. Replacing the floor by
\(0.75C_{q,\mathfrak a}(p)\), with \(a=1\), \(b=0\), and minimizing over
the same height grid gives:

| Conductor | Even characters | Odd characters |
| --- | ---: | ---: |
| \(10^8\) | 0.304975690408 | 0.297795323367 |
| \(10^{12}\) | 0.230829525276 | 0.226271097914 |

These values were independently recomputed from the rational ODE integral;
the [check programme](../numerics/check_comparison_loss_codex_20261017.py)
and [small execution record](../numerics/CHECK_COMPARISON_LOSS_CODEX_20261017.json)
are saved with the numerics.
At \(10^8\), both exceed the conditional baseline 0.2811856084; at
\(10^{12}\), both beat it. The large-conductor plan survives this bounded
sensitivity check, but the zero-loss table does not determine a threshold
for a theorem allowing the stated loss.

The next deliverable should therefore specify a conductor/parity range,
reference height, time interval, and explicit loss function
\(\delta(q,\mathfrak a,p,t)\), prove its uniformity in every real \(x\),
and evaluate the comparison with that loss. H12 may depend on the fixed
character; the floor/loss estimate needs the uniformity asserted for the
family. For Target B, a barrier covering the whole longer comparison
interval is an additional obligation. Neither Platt's verified initial
heights nor the scalar ODE supplies it. The quoted verification-height
formulas agree with [Platt's abstract](https://arxiv.org/abs/1305.3087).

## Controls, limits, and acceptance gate

The control discussion distinguishes the actual family premises. The
Euler-factor controls fail the specific Euler-product logarithmic-derivative
allowance; the other listed controls do not have the full primitive
character completion and arithmetic input. Their collisions therefore do
not refute the family target. They still screen intermediate claims that
use only the properties those controls share. The paired-zero inequality
is general and is not the family-specific gain; the unresolved positive-time
arithmetic estimate is where that gain must enter.

No counterexample to the proposed large-conductor mechanism was found.
No proof of \(A_p\) or H12 was supplied by this review. The precedence
search has not been repeated exhaustively, and the claimed quasi-RH
half-planes and Hakimoglu-Brown's full certificate chain were not independently
validated here. No checked theorem is promoted to a novelty claim.

After R1–R5 and the short endpoint completion, the contract can serve as
the first-phase deliverable with its missing analytic lemmas explicit.
The gate for a numerical milestone remains a complete, applicable estimate
with certified errors and a bound below \(1/2\); the zero-loss planning
tables and successful replay do not meet it. No new manuscript milestone
or result-summary promotion is warranted by this review alone.
