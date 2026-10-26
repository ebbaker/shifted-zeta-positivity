# What the recurrence research has accomplished

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**, as
recorded in the current session metadata. Recurrence **chat0007**, thread
`01a178d3-5b84-7a81-9cbe-2210fd235c35`, turn
`01a178d3-5edd-7d22-83b6-689aa95f5316`.

**Status: high-level discussion and interpretation of existing results.**
Read the current manuscript, including its appendices, Note18 and Review13,
and the existing continuation. This note adds no theorem, independent
proof audit, numerical experiment, implementation certificate, or change
to the research register. It records the assistant's synthesis in response
to the author's request; the discussion remains open.

## 1. The central accomplishment

The research has developed a controlled finite approximation and evaluation
theory for the canonical negative-time Riemann heat flow
\(h(T,z)=H(-T,z)\), \(T>0\). The [opening brainstorm][opening] proposed
organizing the field into successively more complicated fluctuations.
The [current manuscript][main] now quantifies what retaining those levels
buys, matches the necessary Riemann–Siegel completion, supplies finite
algorithms for the data, and includes the errors of actually evaluating
the resulting expression.

There are two distinct indices: the arithmetic mode \(n\), and fluctuation
weight \(j\). Every arithmetic mode through
\(N=\lfloor\sqrt{X/(4\pi)}\rfloor\) remains. Increasing fluctuation weight
resolves more of the common gamma-factor curvature, including products of
lower corrections. The exact recurrence generates these terms from earlier
levels; Gaussian moments evolve them. A bounded real integral retains the
canonical Riemann–Siegel completion and exact changes of cutoff.

Every finite frozen model solves the heat equation exactly. Its accuracy
comes from the separate comparison with the complete canonical source and
from the paid tails. The finite construction does not require convergence
of an infinite fluctuation series. The earlier ansatz already had a
separate growing-degree outer approximation; the present achievement is
the corresponding fluctuation hierarchy and its effective evaluation,
not the first outer approximation in the project.

## 2. A predictable gain from additional levels

At fixed order \(p\), the manuscript proves natural gamma-scale error
\(O(X^{-(p+3/4)})\), when the completion includes \(C_0\) through
\(C_{2p}\). The estimate simultaneously controls the field, spatial
derivatives through order three, and the first time derivative on fixed
complex charts and any declared fixed compact interval
\(0<\tau\le T\le B<\infty\).

| Approximation | Completion | Natural-scale error allowance |
| --- | --- | --- |
| Earlier elementary short formula | Leading correction | \(O(X^{-3/4})\) |
| Frozen first fluctuation level | Through \(C_2\) | \(O(X^{-7/4})\) |
| Frozen second fluctuation level | Through \(C_4\) | \(O(X^{-11/4})\) |
| Frozen order \(p\ge1\) | Through \(C_{2p}\) | \(O(X^{-(p+3/4)})\) |

The earlier short-form comparison in this table uses \(1\le T\le2\).
These are improved proved upper allowances, not pointwise monotonicity
of actual errors or lower bounds proving the matching order necessary.
The organizing lesson is that arithmetic curvature and completion must
be improved together to obtain the displayed rate.

## 3. Accuracy beyond every fixed inverse power

Let \(L=\log(X/(4\pi))\). Controlling the order-dependent constants
before choosing \(p=\lfloor L/2\rfloor\), \(K=2p\), gives the combined
field/derivative error bound

\[
\frac{\text{combined absolute error}}{\mathcal E_{\mathrm o}(-T,z)}
\le \exp(-L^2/4),\qquad 1\le T\le2,
\]

at the stated sufficient heights. Here \(\mathcal E_{\mathrm o}\) is the
positive two-arm amplitude envelope. This decays faster than any fixed
inverse power of height. It is not relative error divided by the signed
field, which can vanish. The envelope normalization keeps the statement
meaningful near zeros without supplying a zero-location theorem.

The constant control is essential: a theorem for every fixed order does
not automatically allow the order to grow with height. The manuscript
pays the factorial growth, full arithmetic population and true and
artificial tails simultaneously before making that choice.

## 4. An effective construction with honest cost accounting

The finite evaluation theorem supplies gamma derivatives, coefficients,
quadrature data, safe cutoff handling, scale and phase computations, and
rounding allowances. It applies to certified dyadic centers and exact
rational queries with strict frozen descriptor witnesses. It does not
assume an unprovided exact-real comparison oracle.

Sufficient delivered precision is
\(3L^2/(8\log2)+O(L\log L)\) bits for fixed chart data. The total proved
work is the full mode count times a polynomial in precision, log-height,
input length and descriptor-separation cost. Streaming gives polynomial
storage without storing the whole mode population. Since
\(N\asymp\sqrt X\), this is not polynomial total work in \(\log X\).

The analytical algorithm is now specified with proved termination and
error bounds from its named inputs. A complete certified software
implementation remains unfinished. Earlier finite gamma/Gauss replay is
supporting component evidence; it is neither a premise of the theorem
nor a complete evaluator certificate.

## 5. What the two latest analytical strengthenings add

The [onset proof in the manuscript][onset] replaces sufficient log-height
\(2^{22}\nu^4\) by \(64\nu\), where
\(\nu=\lceil r+b+2\rceil+1\). The exact improvement factor is
\(2^{16}\nu^3\). It keeps fixed chart costs additive instead of
multiplying them unnecessarily by growing-order costs. All original
accuracy and domain requirements remain. This is a substantial improvement
to a sufficient bound; actual heights still depend exponentially on
log-height, and useful runtime is not established. Smaller heights can
also be admitted when their finite gates are certified.

[Note18][n18] then sharpens a different part of the construction:

- Every normalized derivative bound for the coefficient-generating entire
  function, and every coefficient majorant \(D_k\), improves by the common
  factor \(\alpha=1/\sinh\pi<1/10\) on the same domains.
- A separate argument on the larger rectangle used for contour quadrature
  replaces its majorant \(B_c\) by \(B_c/16\).
- Any old certified contour order \(q\) can consequently be replaced by
  \(q-11\), at the same jet truncation tolerance, for every finite order
  and every \(0<\tau_h\le1\) in the stated family. This saves **44 contour
  locations per instantiated four-edge rule**, and \(44(3K+1)\) jet-sum
  terms per supplied coefficient coordinate. Reused samples count once.

The proof keeps the actual denominator in the boundary estimate, proves
where that estimate is maximized, and carries it to the interior and
all derivatives by analyticity. The larger contour region needs its own
bound. The result applies uniformly to an unbounded order/tolerance
family; it was not inferred from a finite set of numerical examples.

These are smaller upper bounds on the same functions, not smaller actual
coefficients. They improve the available allowances and a specified
operation count while preserving the final \(e^{-L^2/4}\) target.
The full integral also contains a cutoff-transfer term. Its bound changes
from \(\mathcal T_X+S_{\rm RS}\) to
\(\mathcal T_X+\alpha S_{\rm RS}\), not to
\(\alpha(\mathcal T_X+S_{\rm RS})\). Other conditioning terms remain too.
Thus the work establishes neither a tenfold whole-evaluator improvement
nor a measured runtime gain or a better asymptotic complexity exponent.

## 6. Interpretation and the next useful discussion

It is useful to separate three kinds of progress: approximation accuracy,
the domain where it is proved, and the resources needed to deliver it.
The hierarchy improved accuracy; the onset proof enlarged the guaranteed
height range; Note18 reduced particular coefficient and evaluation
allowances. None alone supplies the signed inequalities or geometric
control required for zero or physical conclusions.

The existing [AN08 request][an08] asks for a substantive domain extension:
keep the same hierarchy and target while proving uniform control on
\(1/L\le T\le2\). Since \(T\) approaches zero as height grows, that
would connect the present construction more closely to the original
\(T=0\) xi field. It remains a proposed theorem. The complex-kernel and
derivative constants depend on the lower time endpoint, so a fixed-time
result cannot simply be reused with \(\tau=1/L\). Even success would
still exclude \(T=0\) and would not establish RH.

**Next concrete deliverable and owner: Analysis — Sol**, the already
prepared AN08 r1 uniform moving-endpoint comparison and delivered-error
construction. This discussion recommends the existing bounded question;
it does not execute or alter it. A short request, if the author chooses
to proceed: “Continue HDA-R05-AN08 r1; prove the same combined accuracy
uniformly for 1/L <= T <= 2, or identify the precise unpaid inequality,
keeping the source, modes, completion, buffers and error categories.”

The present claims remain *proved in-note/manuscript from named inputs*,
with internal LLM assessments. This reading does not add independent
specialist validation or a fresh audit of the imported coefficient
proofs. Broad R05 remains Partial at full software/certification;
RH, simplicity, noncollision and physical-transfer conclusions are open.
The [result index][results] and [heat cluster][heat] supply the status
context; the [avoid index][avoid], particularly
[shared-premise review][reviewlimits] and [separate bound payments][bounds],
govern this interpretation. The recurrence and heat identities alone do
not exclude the [collision controls][controls].

## 7. Why negative time is specified, and what happens at zero

Follow-up discussion, 26 October 2026. Prepared for Edward Baker with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**;
same chat0007, turn `01a178db-4c62-72f1-b62c-dba8fa4d6804`.
This clarifies existing formulas and theorem scopes; no new uniform
endpoint theorem or research-status change is claimed.

The qualification applies to the new sharp heat-evolution/evaluation
theorem. It does not mean that the exact field is singular at zero,
that the coefficient estimates cease to hold there, or that earlier
research omitted zero time.

The [canonical source formula][source] is

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad \partial_tH=-\partial_z^2H.
\]

For negative original time, put \(T=-t>0\). The multiplier becomes
\(e^{-Tu^2}\), suppressing high frequencies, and \(h(T,z)=H(-T,z)\)
satisfies the ordinary forward heat equation. Its real-data Gaussian
convolution is the mechanism used by the recurrence proof. In the
original convention, the strongest current \(1\le T\le2\) theorem
therefore means \(-2\le t\le-1\).

For positive original time the multiplier \(e^{tu^2}\) amplifies high
frequencies. The canonical integral still exists because \(\Phi\) decays
super-exponentially, but substituting negative \(T\) into the real
Gaussian convolution destroys its decay. That particular smoothing
argument does not extend by changing the sign. Selected introductory
passages of the existing [Polymath source][primary] were checked for the
normalization, source decay and backward-heat convention; no new reading
of its full coefficient proof is claimed.

At zero the exact identity is

\[
H(0,z)=\tfrac18\xi\!\left(\tfrac{1+iz}{2}\right).
\]

The damping factor is one. Rapid source decay permits the exact field
and its fixed derivatives to pass continuously through zero on compact
z sets. On the real axis the Gaussian kernel tends to a delta mass, so
its convolution recovers the initial field. This delta statement is
about real target points; it is not a positive-kernel argument for
uniform recovery on a fixed complex strip. RH is precisely the assertion
that every zero of this zero-time function is real.

The limiting difficulty is visible in the [kernel and moment estimates][moments].
For \(z=x+iy\),

\[
|k_T(z-u)|=(4\pi T)^{-1/2}
             e^{y^2/(4T)}e^{-(x-u)^2/(4T)}.
\]

Taking absolute values loses oscillatory cancellation and introduces
\(e^{Y^2/(4\tau)}\) on the buffered chart. Direct time differentiation
also introduces inverse powers \(\tau^{-1}\) and \(\tau^{-2}\).
These bounds are not uniform as the lower endpoint \(\tau\downarrow0\).
This describes the limitations of these estimates, not a divergence of
the canonical field. The imported real RS remainder controls initial
values; smoothing was also used to obtain the complex-chart and derivative
comparisons. Those conclusions do not follow at zero by substitution.

The finite arithmetic blocks themselves have a regular algebraic
specialization: the [moment formula][hierarchy] gives
\(\mathcal H_m(d,0)=d^m\), and the recurrence operator becomes
\(\mathcal Q_0=d\). This observation does not supply a uniform endpoint
extension of the complete branchwise retained integral or its error
ledger. Likewise Note18's estimates on \(F_0,C_k\) and contour jet
delivery do not involve heat time; they remain valid for the same
coefficient inputs at zero. What remains unproved is their composition
into the same full high-accuracy theorem through zero.

There is already a separate, weaker result at and across zero:
[ansatz Note04][crossover], CS3 and CS6–7, proves a complex zero-time
comparison and a buffered signed-time comparison on \(|t|L\le8\).
At \(t=0\), the field allowance is \(O(X^{-3/4})\) relative to its
outer envelope; its spatial and time channels retain the stated powers
of \(1+L\). Constants and sufficient onsets were not numerically
instantiated there. It retains its proved-in-note, internal-assessment
status and its own approximation. It does not already provide the
recurrence construction's \(e^{-L^2/4}\) total evaluation guarantee.

Thus the question is how to preserve the sharper accuracy and delivered
error control while approaching and eventually joining zero time.
**Next analytical deliverable remains Analysis — Sol, [AN08 r1][an08]**,
with \(1/L\le T\le2\); the lower endpoint is positive at every finite
height. Its success would still require a separate argument to include
\(T=0\). No additional task is needed merely to explain the distinction.
The existing result/avoid references above continue to govern status;
no zero-reality conclusion follows from smoothness or evaluation accuracy.

[opening]: 01_RECURRENCE_AND_GENERALIZED_TRANSFORM_HIERARCHIES_20261026.md
[main]: ../manuscript/main.tex
[onset]: ../manuscript/sections/11_calibration_and_onset.tex
[n18]: ../notes/18_UNIFORM_RS_BOUND_STRENGTHENING_20261026.md
[an08]: ../research-progress/handoffs/HDA-R05-AN08.md
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[reviewlimits]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[bounds]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md

[source]: ../manuscript/sections/02_heat_and_source.tex
[moments]: ../manuscript/sections/04_comparison.tex
[hierarchy]: ../manuscript/sections/03_hierarchy.tex
[crossover]: ../../ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[primary]: https://arxiv.org/html/1904.12438v2#S1
