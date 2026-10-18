# Focused check of the sine-tail comparison and initial manuscript

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex), reasoning effort ultra**.
**Review type: internal same-model adversarial check.** The drafting agent
and three assisting agents share the model; this is not independent
cross-model or specialist human review.

## Disposition and scope

No substantive defect was identified in the checked argument. The
[round-3 note](../notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md)
and [manuscript](../manuscript/main.tex) contain a written proof that
removes H12 from the comparison through sine-tail approximation, giving
Lambda_chi <= 0.27 for primitive q >= 10^12 and the rate
O((log q)^(-4/7)). This disposition records the checks below and preserves
the source status **proved in-note; internal same-model checks only**.
Specialist review and a priority audit remain outstanding.

The separate H12 assertion is not proved for the original character flow.
The exact scalar record retains its original conditional-contract wording;
the new analytic proof supplies its consumer. No GRH or zero-time conclusion
is inferred from the conductor-aspect limit.

## Versions checked

| Artifact | SHA-256 |
| --- | --- |
| [Round-3 note](../notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md) | `c1fdd827e3f1e344f1e4f8bcdd9435767602a24017982fe14a28a4953c245886` |
| [Manuscript source](../manuscript/main.tex) | `a820f8103f9720fedce6ade79cf447354fddfdd1143ee58c6f09a8500411dce2` |
| [Compiled PDF](../manuscript/main.pdf) | `73739071597d6b53a041492fe8b97cd9c7d53de3c28f0375224c79c37d9fc2ba` |
| [Exact scalar programme](../numerics/certify_dirichlet_scalar_conditional_20261017.py) | `0b7d513728d6c20ae380bb9b3ea9bc01a8c8963be1d9efd5aab970a4535b4cf9` |
| [Scalar record](../numerics/DIRICHLET_SCALAR_CONDITIONAL_CERTIFICATE_20261017.json) | `ff6e250a2340bdc88e00c6c2a9043257d50076c44231d7d0b7fd633de4030837` |

Earlier rounds retain their dated mathematical scope. Their only new
content is a dated literature correction in round 1 and a continuation
pointer in round 2. The relocation receipt records the earlier move-time
identity; it is not a claim about the later annotated bytes.

## Analytic checks

1. **Initial floor on the whole real line.** In the central region,
   reciprocal-square summability controls omitted true-zero contributions.
   Outside it, the positive sine-lattice Poisson sum loses only O(1/R)
   when its central block is removed. A strict C_1 < C input handles the
   truncation error. Finite polynomials alone would fail this check.
2. **Correct strip import.** Cardon, arXiv:1401.0237v2, Theorem 1.5,
   printed p. 3, applies to the genus-one approximants with no quadratic
   exponential factor and phi(z)=exp(-t z^2). The Fourier-only strip
   theorem is insufficient here. The resulting strip is
   sqrt(max(1-2t,0)); both the operator and its Gaussian representation
   are justified in the required class.
3. **Confinement for fixed approximants.** The rational-sine expansion
   controls the whole imaginary Gaussian line, including negative rational
   degree and unbounded integration variable. The real part remains large,
   away from the canceled rational poles. Rouché disks have one real zero
   each, uniformly on bounded time intervals, and the complement is
   zero-free. Constants may depend on R, which the limiting argument permits.
4. **Heat limit and nonzeroness.** Canonical truncations and lattice tails
   have a common sub-Gaussian majorant. This permits dominated convergence
   through the heat operator. Composition with the real Gaussian is the
   identity by Fubini and the angular mean, so the limit is nonzero.
5. **Compact comparison and endpoints.** Round 2's complete Burgers
   characteristics and first-contact argument apply to each fixed
   approximant. Strict scalar margins pass through C_1 increasing to C.
   Hurwitz handles the half-planes and heat continuity handles equality.
   The generic endpoint statement was clarified to avoid using an
   undefined generic Newman constant.
6. **Dirichlet normalization and arithmetic.** The phase, conjugate-pair
   convention, Hermitian real-entire property, and factor 1/2 in the
   logarithmic derivative agree with round 1. The finite scalar programme
   was replayed successfully; its stored record was byte-identical.
   C > 6.105 and J_6(0.27) > 1/2 suffice. No new conductor sweep is needed.

## Controls and source correction

The periodic flow exp(t) cos(z) - cosh(0.9) has nonreal zeros at t=0.27.
Its actual floor is less than one, and the exact inequality
J_C(0.27) <= 435483/1000000 < 1/2 for C <= 1 prevents a false conclusion.
This screens the quantitative comparison without claiming to prove H12
from generic strip premises. Other collision controls fail the specific
primitive-character completion or Euler-product allowance; the general
comparison can still apply to their actual floors.

Ki–Kim–Lee, Section 6, Example 1, already prove a qualitative strict bound
below 1/2 for real primitive characters. Their complex-character example
is a self-dual combination, distinct from the individual non-even family.
The correction is recorded in the initial note, source ledger, round 3,
and manuscript. The present literature search does not establish priority.

## Manuscript verification and next analytic task

The source compiled twice with pdfLaTeX to six pages, without warnings,
unresolved references, or overfull/underfull boxes in the final log. All
six rendered pages were visually inspected. The author field says
"Drafted for Edward Baker" and the acknowledgment names the model, effort,
and substantial LLM assistance. The
[build record](../manuscript/BUILD_RECORD.json) binds source and PDF.

The next analytic task is to seek a sharper positive-time lower bound
for S, or a sharper paired-zero comparison, with an explicit numerical
improvement over 0.27 or the exponent 4/7. Specialist review of the
general comparison should precede relying on it as an externally validated
result. Standalone character H12 is a separate optional problem, no longer
a prerequisite for this theorem.
