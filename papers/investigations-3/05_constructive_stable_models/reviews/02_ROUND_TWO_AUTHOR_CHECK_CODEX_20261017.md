# Round-two author check: weak closure, rollback and diverging heat

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6.1-sol (Codex), effort ultra**.

**Kind: same-model author check.** The root author and two same-model agents
read both final derivations, after three agents checked components and
primary sources. Shared context and model family limit independence.
This is not cross-model review, specialist human review or an accepted
manuscript milestone. Round-two cross-model review remains pending.

## Exact versions

| Note | SHA-256 |
| --- | --- |
| [01_WEAK_CLOSURE_AND_ALL_BASE_TIMES_CODEX_20261017.md](../notes/round-2/01_WEAK_CLOSURE_AND_ALL_BASE_TIMES_CODEX_20261017.md) | `06bbad8a48d2772053ef5c0194293eb45137a696de1da3b0006fbd4837a26c4f` |
| [02_DIVERGING_HEAT_TILTS_AND_NEWMAN_CLASS_CODEX_20261017.md](../notes/round-2/02_DIVERGING_HEAT_TILTS_AND_NEWMAN_CLASS_CODEX_20261017.md) | `77305b4abe9aac8a15cd909cb2c2d474a355bdf331d99f6af41bf8dcbe969da5` |

## Claims and checks

- Newman–Wu's Definition 6, Theorem 7 and Proposition 13 were checked in the
  primary source. The variance bound, normal-family argument, exponential
  uniform integrability and heat-domain restriction agree. The convergence
  claim concerns unnormalized heat transforms.
- The quartic-network persistent-site result correctly extends to weak
  convergence. Its rectangle condition implies (11a); they are not called
  equivalent.
- For every fixed target time t0 >= 0, fixed rollback by t0 + delta leaves
  elapsed time tau_n - delta >= 0. Lee–Yang, weak closure and Rodgers–Tao
  exclude every subsequence tau_n >= delta. If tau_n -> 0, bounded untilting
  returns the independent seeds to the certified odd-dilation floor.
  The probability-normalized floor includes division by H0(0).
- The exact Gaussian convolution has variance 1/(2 lambda_n), coefficient
  d_n = lambda_n - 4 a_n lambda_n^2 and product coefficients
  c_nj = 4 lambda_n^2/r_nj^2. Integrability forces d_n > 0. Newman's
  equation (1.5) and Theorem 2 cover its product-density subclass.
- The weak closedness of Newman's class, the quartic lower bound and the
  theta/Bessel contradictions were checked analytically. The discrete
  exception includes the point mass at zero. No tail comparison decides
  theta stability, since the stable Bessel control is excluded too.
- The harmonic Rademacher example and explicit multiplier G(z) = 1-z^2
  retain h log h leading growth; no general fixed-multiplier exclusion is
  claimed. The surviving interacting classes are stated explicitly.

Two precision corrections found during the final read were applied:
replace “equivalently” by “in particular” for (11a), and include the
coincident two-point law at zero. The multiplier example and unnormalized
complex-time wording were also made explicit. No substantive mathematical
gap was found within the stated hypotheses.

## Imports, validation and disposition

Primary inputs checked: [Newman–Wu, Theorem 7 and Proposition 13](https://arxiv.org/pdf/1708.08820),
[Rodgers–Tao, Theorem 1](https://arxiv.org/pdf/1801.05914),
[Newman, Theorem 2 and equation (2.2)](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf),
and [Cardon, Theorem 1 and Lemma 1](https://mathdept.byu.edu/cardon/papers/FourierRealZeros.pdf).
The finite-spin Lee–Yang import and odd-dilation certificate remain those
checked in the [round-one review](01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md).
No new numerical certificate, manuscript build or large derived output
was needed. No novelty claim is made for the classical mechanisms.

Disposition: retain the proofs as scoped in-note results pending
cross-model round-two review. The opening search is closed; no larger
moment fit is warranted. Reopen only for a named admissible construction
with a proved stable-control approximation and a theta-specific estimate.
