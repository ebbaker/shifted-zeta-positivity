# Internal review: RH and the translated-kernel return height

20 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6-astra (Codex), reasoning effort ultra**, verified from
recorded metadata. Separate same-model internal checks; no specialist
review or novelty claim.

**Verdict: pass.** The separate source/derivation audit checked [Note 10](../notes/10_UNIFORM_PRIME_PHASE_RETURN_HEIGHT_COST_20261020.md), including the primary approximation, the complete prime-power tail, the phase-separation constant, and the conversion to the full kernel envelope. No mathematical correction is needed.

## Primary-source check

[Granville–Soundararajan, *Extreme values of |zeta(1+it)|*, Lemma 2.1, PDF p.3](https://arxiv.org/pdf/math/0501232) permits `sigma_0=1/2` and `sigma=1`. Under RH its open rectangle to the right of the critical line is zero-free, regardless of multiplicities on the boundary. For `y>=e^4`, `t>=y+3`, its stated error specializes to

\[
O\!\left(\log t\,(\log y)^2/\sqrt y\right).
\]

This is the all-height zero-free-rectangle lemma, not the paper's later exceptional-set approximation. Taking real parts removes any logarithm-branch issue.

## Two-cutoff and phase audit

For fixed `delta>0`, the two cutoffs `(log t)^(2+delta/2)` and `(log t)^(2+delta)` satisfy the source hypotheses eventually, and both errors tend to zero. Subtraction compares the same value of `Re log zeta(1+it)`, so the real prime-power shell is `o(1)`.

The discarded higher-power shell has the claimed **absolute** bound

\[
\sum_{p^k>y_0,\ k\ge2}\frac1{kp^k}=O(y_0^{-1/2}).
\]

Indeed primes above `sqrt(y_0)` contribute `O(sum_{n>sqrt(y_0)} n^-2)`; for each smaller prime the geometric tail beginning at the first power exceeding `y_0` is `O(1/y_0)`. Thus no higher-power phase assumption is being used. PNT and partial summation give the positive limiting reciprocal-prime shell mass stated in the note.

With `t=dR`, the return condition implies `|p^(-it)-1|<=d epsilon_Delta`, and hence `Re p^(-it)>=1-d^2 epsilon_Delta^2/2`. Only `epsilon_Delta->0` is needed. There is no missing factor `epsilon_Delta log log y`: the proof compares a shell of bounded positive mass and pays all higher powers independently.

The sharper chord constant also checks. If every relative angle to `omega`, where `omega^d=1`, lies strictly inside `(-pi/(2d),pi/(2d))`, then every `Re p^(-idR)` is uniformly positive. A fixed chord bound below `2 sin(pi/(4d))` forces precisely this angle condition, contradicting the shell's real sum. The note correctly states a lower limit with an `o(1)` allowance, not strict separation at the limiting constant.

## Full-envelope and scope audit

The result is `limsup log X/log log R<=2`, for fixed `d`. For the declared target heights comparable with `R`, this gives `Delta<=(1/pi+o(1)) log L`. Combining `I~d/Delta`, the already paid gamma estimate, the exact-pole negative-part budget, and `C>=0` yields

\[
\liminf\frac{U(\gamma)}{L/\log L}\ge\frac d2.
\]

Both translated-sum and scalar-square versions have the required mass and height budgets. The constants are lower bounds, not claimed attainable optima. The conclusion closes this fixed fully aligned family; it neither invalidates Note 09's small-prime-payment examples nor proves a barrier for arbitrary kernels, arbitrary translations, or partially aligned phases. It excludes no original multiple zero and uses no simplicity assumption.

## Dyadic refinement checked

The proposed refinement uses `ell=log log t`, `y_0=A(log t)^2 ell^6`, and `y_1=2y_0`. For fixed `A`, the two source errors sum to `O(A^-1/2/ell)`, while PNT gives reciprocal-prime shell mass `(log 2)/(2ell)(1+o(1))`; the higher-power tail is negligible on this scale. A fixed sufficiently large `A` makes the source error smaller than the positive aligned-prime contribution. Consequently an aligned return satisfies

\[
\log X\le 2\log\log(dR)+6\log\log\log(dR)+O(1).
\]

This refinement is included in Note 10 (H14). Its unspecified constant depends on the primary lemma's implied constant; it should not be presented as a numerically explicit search bound. It does not change the leading full-envelope coefficient `d/2`.


The coordinating agent separately checked the primary source and full
gamma/pole budgets from Note 09. A further same-model audit checked the
whole argument and stressed that the limiting chord threshold belongs to
the original fixed-positive-mass shell, not to the refined dyadic shell
with fixed A. The final note states that distinction.
The final integration audit corrected equation-reference formatting and
confined the approach to I Delta=2 from below to the translated sum;
the scalar-square version need not approach from below.

The parallel assessment retaining the exact functional-equation pair in
the finite-zeta calculation did not produce an opposing signed estimate.
No theorem about the unrestricted signed arithmetic is inferred from
that unsuccessful assessment. No new numerical scan, certificate,
manuscript or snapshot was made. The existing 265 rational fixtures were
unchanged and were not rerun for this analytical argument.

The [progress register](../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md)
retains the original positive-estimate, strict-surplus and all-zero gates.
