# First subpower investigation: internal proof and certificate review

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Different agents using the inherited model checked the derivations and
source inputs. This is internal review, not independent specialist refereeing.

The continuation establishes an arithmetic transfer, finite variance
certificates and a generic obstruction. It proves no fixed global delta
below one and no exponent-descent rule for the actual prime coefficients.
The author-selected program remains organized around that global target.

## Short-interval transfer and source audit

Reviewed [note 02](../notes/subpower-milestones/02_short_interval_transfer_and_gate_20261003.md).
Finite Fubini gives exact centering, including noninteger endpoints.
Symmetric averaging cancels the first Taylor term; the C^2 zero extension
controls atoms in the expanded band. Elementary Chebyshev gives the
h^2/x pointwise approximation and h^4/X squared error.

The explicit gate is

\[
\mathcal V_g(X)\le3X^2S_{A,B}(X,h)/h^2+C_{\rm app}^2h^4/X.
\]

Its reverse-triangle refinement proves that the signed averaged
projection Q_h has exactly the same admissible global powers as Vcal
when h=X^(3/4). The double integral retains every cap and cross term.
A fixed relative saving X^(-kappa) in the raw mean square would give
every delta>max(0,1-kappa,4 tau-3) at h=X^tau. The endpoint is not
asserted when the extra factor L(X) is unbounded.

Two agents checked the primary Saffari–Vaughan paper, including visual
inspection of printed pages 19, 24, 25 and 28. Its stated lemmas use
theta; the proof first establishes psi. The note derives the additive
psi bound from that relative estimate rather than silently changing
the lemma's quantity. At h=X^(3/4), the length conditions and all
shifted dyadic cover intervals are satisfied for sufficiently large
real X. The resulting estimate supplies only a subpower saving on
X cubed; it leaves delta=1 and is weaker than the program's existing
Johnston–Yang baseline. This limitation is specific to the tested
arithmetic input and absolute transfer, not every signed covariance method.

Primary source: [Saffari–Vaughan](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf),
Section 6, especially (6.2), (6.12)–(6.18), (6.19), (6.21).
No downloaded third-party paper is stored in the repository.

## Finite-range variance theorem

Reviewed [note 03](../notes/subpower-milestones/03_finite_range_variance_20261003.md)
and the [certificate package](../numerics/subpower_finite_variance_20261003/README.md).
The complete linear formula gives |p(y)|<=b+R_H exp(y/2), y>=1.
Its sixth-power transform decay yields R_H=O(H^-5 log H).
The twelfth-power autocorrelation tail is not substituted for it.
Integrating the square of b sqrt(x)+R_H x on the entire shell gives
the exact three coefficients 3/2, (4/5)(2^(5/2)-1), and 7/3.

The new generator hash-checks both old outward records and their original
generator, verifies their scope and overlapping enclosures, and rounds
b<4.96 and R_H<1.56e-51 using exact fractions. Root and a separate agent
successfully ran this rational transfer. All-real-X conclusions follow
from monotonicity of the normalized positive budget, not grid sampling:

| Range | Exact rational budget | Proved strict coefficient |
| --- | --- | --- |
| e<=X<=10^99 | 37.8311431296 | 38 |
| e<=X<=10^100 | 39.84376128 | 40 |
| e<=X<=10^102 | 71.4265728 | 72 |

The certificate imports earlier 192/256-bit Arb/Acb calculations; those
zeros were not regenerated in this continuation. The published
[Platt–Trudgian theorem](https://arxiv.org/pdf/2004.09765) verifies the
height 3e12 used here. The
[Hasanalizade–Shen–Wong zero count](https://arxiv.org/pdf/2107.06506)
supplies the global tail majorant. These inputs and the analytic proof
remain separate from the rational check. No large data or zero cache is added.

For a fixed admissible variance ceiling and low cutoff, the certified
range scales as H^10/(log H)^2. At fixed H the upper allowance retains
a cubic term. These finite results do not prove a smaller global delta.

## Structural non-bootstrap theorem

Reviewed [note 04](../notes/subpower-milestones/04_structural_nonbootstrap_20261003.md).
The greedy construction retains any prescribed actual coefficient prefix
and tracks a monotone oscillatory counting function to O(log x).
Beyond that prefix the coefficients are zero or log n. It satisfies PNT
and the diagonal, frame, trend-annihilation and outer-frequency estimates.

The complete dyadic phase integral has an explicitly positive minimum
for nonzero gamma. This gives variance of exact order X^(2+delta)
for all sufficiently large real X, rather than a subsequence statement.
Both error powers are smaller. The exact Stieltjes identity for A2(t)
is qualified by t>=log N, after the retained prefix has entered; the
review identified and corrected that minor qualifier.

The model is not the actual Euler-prime sequence. It establishes that
the listed generic structural hypotheses and finite arithmetic prefix
cannot imply a universal exponent descent. A successful actual-prime
argument must use an additional arithmetic condition or a signed estimate
not supplied by those controls. No impossibility theorem for the actual
zeta function is claimed.

## Integration and next obligation

The program index, milestone ledger, investigation README, selective-loss
overview and handoff link these results. Detailed research stays in those
notes; the current manuscript is not revised in this continuation.
No new draft snapshot or manuscript-history entry is needed.

The next bounded global attempt should state a lemma for a fixed positive
kappa at h=X^(3/4), or an estimate of the exact signed short-interval
projection, before substantial calculation. All support and averaging
costs in that gate are already O(X^2). A smaller variance constant or
longer finite range is useful but belongs in the finite ledger, not the
global delta column.
