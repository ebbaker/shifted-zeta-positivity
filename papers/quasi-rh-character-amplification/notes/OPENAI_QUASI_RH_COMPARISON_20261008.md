# OpenAI quasi Riemann hypothesis comparison

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Scope: mathematical comparison and conditional transfer of the announced
results, not independent specialist verification of the new proof.

The October 5 OpenAI paper addresses the same first fixed-strip milestone
as our recent prime-variance program, using substantially different
arithmetic machinery. Its closest local relatives are the signed Möbius
reductions and the amplification question in the large-values scout.
The older complete-Weil-form, Sonin, and physical-realization programs
have a more distant methodological relationship.

## Published mechanism

[The Quasi-Riemann Hypothesis](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf),
Theorem 1.1, states nonvanishing for Re(s)>11/12 for all Dirichlet
L-functions and finite-order Hecke L-functions over Q(sqrt(-3)).

Sections 2 and 3 embed a smoothed Möbius sum in sextic character twists
over Eisenstein integers. Rows indexed by prime sixth powers reproduce
the target sum up to a controlled error. A family mean-square estimate
therefore bounds that particular sum. Poisson summation converts the
Möbius coefficients into cubic Gauss sums. Cubic theta transformation
then produces quadratic characters, allowing a quadratic large sieve.
Cube completion is undone by Möbius inversion; a transfer using two
Poisson summations closes the remaining estimates by finite scale
iteration. Mellin holomorphy excludes zeros beyond 11/12.

The iteration preserves a ratio of auxiliary scales; it does not iterate
the zero-free boundary toward 1/2. The amplification repeats a target
arithmetic sum across character parameters, rather than producing more
zeros or more height samples. These distinctions matter for any attempted
adaptation.

## Comparison with our program

Our [manuscript](../../prime-variance-exponents/manuscript.tex), Theorem 1.1 and Section 3, relates
the prepared prime response to a closed strip through its true Laplace
transform and noncancellation of forbidden-zero poles. It supplies a
faithful quantitative criterion. The open arithmetic task is to prove a
fixed power saving for that response.

The [signed Mellin continuation](../../prime-variance-exponents/notes/SIGNED_MELLIN_CONTINUATION_20261004.md)
retains the joint Möbius signs, product caps, boundary terms, and a signed
two-frequency kernel. The OpenAI construction suggests a possible source
of additional arithmetic structure beyond those reductions. It is not a
direct estimate for our existing covariance, nor an application of our
probe identities.

Our [large-values scout](../../prime-variance-exponents/notes/programs/09_large_values_zero_detection/PRELIMINARY_INVESTIGATION_20261004.md)
identified a missing amplification step: one large detector value need
not contradict a positive-power density bound. The new paper's family
embedding is a useful conceptual counterpart. Adapting it to our
polynomial would require an actual arithmetic identity and a matching
family bound; merely enlarging a sampling range would not suffice.

For the [earlier program](../../../README.md), the target is a lower
bound on the complete Weil form for all inputs and support lengths.
The new argument instead obtains upper bounds on nonnegative mean
squares of signed arithmetic sums. Shared use of quadratic expressions
does not identify the positivity problems.

## Exact transfer to our variance exponent

Our fixed-probe theorem states

\[
\mathcal V_g(X)=O(X^{2+\delta})
\quad\Longleftrightarrow\quad
|\Re\rho-\tfrac12|\le\tfrac\delta2
\quad\text{for every nontrivial zeta zero}.
\]

Consequently a zero-free half-plane Re(s)>theta, together with the zeta
functional equation, gives delta=2theta-1 and variance O(X^(1+2theta)).
This is our deduction from the announced theorem and our internally
reviewed equivalence, not a variance theorem stated in the new paper.

| Input | Resulting delta | Bound for our fixed variance |
| --- | --- | --- |
| October 5 theorem, theta=11/12 | 5/6 | O(X^(17/6)) = O(X^(3-1/6)) |
| Announced companion, theta=7/8 | 3/4 | O(X^(11/4)) = O(X^(3-1/4)) |
| RH endpoint, theta=1/2 | 0 | O(X^2) |

The [release catalogue](https://github.com/openai/math/blob/main/CONTENTS.md)
identifies the September 30 paper as the stronger 7/8 result. Its
[formalization scope](https://github.com/openai/math/blob/main/lean/docs/003.md)
describes the 7/8 statements; that documentation is not a local replay or
audit of the Lean proof. The October 5 argument was the subject of this
comparison; the stronger companion's proof was not reviewed here.

If accepted, either result supplies the first fixed saving that our
October 4 records leave open. The next research question would become
improving the exponent or understanding whether the new family symmetry
can control our signed forms more sharply. Neither result supplies RH,
arbitrary-support central Weil positivity, or an exponent-descent rule.
Historical status files should retain their dated claims until a separate
source-verification and update task establishes the new baseline.

## Provenance

The [release README](https://github.com/openai/math) attributes the
collection to an unreleased internal OpenAI model and says the 11/12
writeup was human edited for readability. This does not identify that
model with this Codex session or establish any historical connection to
our project. The comparison concerns mathematical structure.

The linked PDF was read from a temporary location outside the repository,
consistent with LARGE_FILES.md. SHA-256 of the inspected PDF:
`f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18`.
No third-party PDF, generated dataset, or manuscript snapshot is added.
