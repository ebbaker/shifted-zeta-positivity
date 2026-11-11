# GNP-RS-B05 — a paid adaptive phase and the signed tangent boundary

11 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Conceptual work and this note:
**gpt-6-astra, actual dispatched effort ultra**. Bounded E06 execution
and contributing separate-agent internal assessment: **gpt-6.1-sol,
ultra**. These dispatch settings do not identify the coordinating chat's
unavailable model configuration.

**Status:** B05 and the [frozen E06 request][request] are complete at
their stated decision and inherited-input analytical-proof scopes under
the [Note15 brief][brief]. The analytical source is [E06 Note17][e06],
with the contributing separate-agent [internal assessment][review].
They acquire the overhead of an explicit
growing Euler comparison and obstruct one signed tangent implementation.
They do not acquire the favorable signed Green value at every center.
Inherited inputs retain their internal-review scope; no specialist review
or literature-priority claim is made.

## 1. What is being tested

Read the [result index][results], [heat-flow cluster11][r11],
[collision controls12][controls] and [avoidance index][avoid], particularly
[target classification01][a01], [premise screening02][a02],
[scoped exclusions07][a07] and [separate-payment caution12][a12].
The two tests below retain the complete physical theta field
\(V_\lambda=H_\lambda/C_-\), \(\partial_\lambda H=-H_{zz}\),
\(\lambda=c/L_X\), \(c\in[1/2,1]\), \(L_X=\log(X/(4\pi))\),
the exact critical-log tail \(T_X\), E01 allowance \(C_*/L_X\),
kernel \(K\), window \(W_X\), and original margin
\(m_*=\sin(\pi/8)/(2\cosh(\pi/8))\) at \(d=1/2,r=1\).
Physical time is fixed throughout each spatial integral.

The first test asks whether *one explicit growing cutoff* can have all
reference-phase and approximation costs paid jointly. The second asks
whether keeping the exact signed cross term in a tangent-log upper
estimate escapes the fixed-reference residual obstruction. These are
different from rerunning E05's fixed-prime mean law.

The adaptive result is an **every-center acquisition estimate** on the
whole original \(c\) band. The tangent result is a **scoped obstruction**
on \(c=1\), not a result about all nonlinear signed methods. Neither
is an RH reformulation or a favorable uniform signed-value estimate.

## 2. An explicit growing reference has a uniformly paid phase

Use E05's unreflected reference, now with
\[
 P=P(X)=\lfloor L_X^2\rfloor,\qquad
 E_P(x)=\prod_{p\le P}
 \left(1-p^{-\sigma_c}e^{i\nu_\lambda(x)\log p}\right)^{-1},
 \quad \sigma_c=\tfrac12+c/4,
 \quad \nu_\lambda(x)=x/2+\pi\lambda/8.
 \tag{1}
\]
Freeze \(P,c,\lambda\) at the center throughout \(W_X\). The cutoff
is not differentiated in the spatial integral. Write
\[
 \psi=\phi_\lambda-2\Im\log E_P,\qquad
 \frac{S_P^{\rm ref}}{E_P}=1+e^{i\psi},\qquad
 b_\delta=\frac{\delta+\sqrt{\delta^2+4}}2.
\]
The finite-Euler logarithm is its absolutely convergent prime-power
logarithm; it introduces no branch zero. The regularized reference log is
\[
 \tfrac12\log(|1+e^{i\psi}|^2+\delta^2)
 =\log b_\delta+
    \Re\sum_{k\ge1}\frac{(-1)^{k+1}b_\delta^{-2k}}{k}e^{ik\psi}.
 \tag{2}
\]
The crucial estimating choice is to differentiate the **whole** phase
\(\psi\). Its Fourier coefficient has constant modulus. With
\(\kappa=1-2^{-5/8}>0\), elementary integer sums give
\[
 2|\partial_x\arg E_P|\le
 D_1(P):=\frac{8}{3\kappa}P^{3/8}\log P,
\]
\[
 2|\partial_{xx}\arg E_P|\le
 D_2(P):=\frac{4}{3\kappa^2}P^{3/8}(\log P)^2.
 \tag{3}
\]
These bounds are uniform in \(c\). Eventually
\(\psi'\ge L_X/4\) on \(W_X\), while
\(\|\psi''\|_\infty=O(X^{-1}+D_2(P))\).
One integration by parts in the \(k\)-th harmonic supplies an extra
\(1/k\), including both window endpoints and the kernel derivative.
Since \(\sum_{k\ge1}b_\delta^{-2k}/k^2\le2\), the resulting
discrepancy is bounded by
\[
 \frac{2}{L_X}+
 \frac{16\|\psi''\|_\infty}{L_X^2}=O(L_X^{-1})
 \tag{4}
\]
at (1), **uniformly for every \(\delta>0\)**. Thus the regulator may
be chosen separately at each center. No claim of a uniform bound follows
from the older fixed-\(P,\delta\) notation alone; (3)–(4) pay its growth.
Since \(\|\psi''\|_\infty\le L_X\) eventually on this schedule,
the displayed discrepancy is then at most \(18/L_X\).
The same bound at \(\delta=0\) follows through the locally integrable
reference zeros, by a bounded periodic primitive or the decreasing
regularization limit.

All other comparison costs are paid on this schedule:
\[
 \text{omitted prime-log tail}=O(L_X^{-3}),\qquad
 \text{reference-log exterior}=O(L_X^{3/4}X^{-4}),
 \tag{5}
\]
\[
 \sup_{W_X}\left|\frac{V_\lambda-S_\lambda}{E_P}\right|
 \le C X^{-1/4}\exp(O(L_X^{3/4}))=X^{-1/4+o(1)}.
 \tag{6}
\]
Here \(S_\lambda\) is the **complete retained two-arm approximation**;
the numerator in (6) contains the retained correction and provider
residual. The bound uses
\(|E_P^{-1}|\le\exp(\sum_{p\le P}p^{-5/8})
\le\exp((8/3)P^{3/8})\). Its constants and the finite onset depend
only on the fixed inherited source/provider data and the displayed
elementary bounds, not on the center or \(c\). No numerical onset is
claimed.

Consequently the exact residual
\[
 R_{P(X)}(X,c)=\int_{W_X}K(x-X)
        \frac{|V_\lambda(x)-S_{P(X)}^{\rm ref}(x)|^2}{|E_{P(X)}(x)|^2}
        \,dx
 \tag{7}
\]
enters an upper allowance with all remaining costs tending to zero:
\[
 J_\lambda(X)\le q_X\log b_\delta+
 \frac{q_X}{2}\log\left(1+\frac{R_{P(X)}(X,c)}{q_X\delta^2}\right)
 +O(L_X^{-1})+T_X+O(L_X^{3/4}X^{-4}).
 \tag{8}
\]
The \(O(L_X^{-1})\) includes E01, the full reference phase and the
smaller omitted-prime cost; its upper constant is independent of
\(\delta\). In (8) the field is exact. Equation (6) is a separate
paid acquisition input, not a substitute value for (7).

**The adaptive reference is now admissible; its every-center residual
is not estimated.** E05 first fixes \(P\) and then takes the height
limit. Substituting \(P(X)\) into that mean law is invalid. Neither its
density result nor its fixed-reference unboundedness decides (7) on
the explicit growing schedule (1).

## 3. Keeping the signed cross term does not save a tangent majorant

This second test fixes a finite \(P\). Put
\[
 w=V_\lambda/E_P,\quad a=S_P^{\rm ref}/E_P=1+e^{i\psi},
 \quad b=w-a,\quad h=|a|^2+\delta^2.
\]
Concavity of the scalar logarithm gives the pointwise upper majorant
\[
 \log|w|\le G_\delta:={\tfrac12}\log h-\tfrac12+
                   \frac{|w|^2}{2h}.
 \tag{9}
\]
It retains the **exact signed cross term** in
\(|w|^2=|a|^2+2\Re(\bar a b)+|b|^2\). Thus its failure is not
merely the result of first replacing that cross term by its modulus.
It is still a tangent upper envelope, not the full nonlinear logarithm.

Let \(Z=\int_{W_X}K|w|^2\), and put \(H=4+\delta^2\).
Since \(|a|\le2\), we have \(h\le H\) and
\(h/H\ge|a|^2/4\). Integrating (9)'s right side and using
\(u-1-\log u\ge0\) gives the regulator-independent lower bound
\[
 \int_{W_X}K G_\delta
 \ge\frac{q_X}{2}\log(Z/q_X)
      +\int_{W_X}K\log|a|-q_X\log2.
 \tag{10}
\]
The reference logarithm is \(O_P(L_X^{-1})\), including its zeros,
by the whole-phase estimate. For the fixed reference, \(|E_P|\le B_P\)
implies \(Z\ge M(X,1)/B_P^2\) on \(c=1\). E05 proves that this
**exact** moment \(M\) is unbounded at arbitrarily high centers.
Thus the integrated tangent allowance is unbounded there for each fixed
\(P\), independently of any center-dependent choice \(\delta(X)>0\).
Restoring the bounded fixed-reference prime difference and paid tails
does not change that conclusion.

**Stop this fixed-reference tangent-log family as an every-center
method.** It fails even with the exact signed cross term. The statement
does not cover a growing-reference tangent, spatially varying tangent
heights, or other genuinely nonlinear signed bounds. It is a lower
bound on this majorant, not a lower bound on the actual Green value.

## 4. The unpaid signed information and the stopping decision

The adaptive test leaves the explicit arithmetic residual (7) without
a usable every-center bound. A fully nonlinear treatment instead leaves,
for example, the signed quantity
\[
 \int_{W_X}K(x-X)
   \bigl(\log|V_\lambda(x)|-
         \log|S_{P(X)}^{\rm ref}(x)|\bigr)\,dx.
 \tag{11}
\]
Both logarithms are integrable with their zeros retained. This is a
difference of integrable logarithms, not a holomorphic logarithm of a
zero-free quotient. Formula (11) only identifies the unacquired data;
its renaming supplies no progress under [avoid01][a01]. Expanding a
quotient through reference zeros would need additional denominator and
small-value estimates, which this pass does not provide. No failure of
such an estimate for the actual theta field is asserted without proof.

The acquired gain is narrower and concrete: the reference can now grow
as \(\lfloor L_X^2\rfloor\), with its actual phase, prime tail,
exterior and complete field-error normalization paid uniformly over the
full original band. The signed tangent alternative has a precise scoped
failure. Neither supplies the missing exceptional-center arithmetic
input. E05's zero-density result at \(c=1\) remains unchanged and is
not strengthened here to an every-center or all-\(c\) statement.

**Stop the bounded B05/E06 pass here. The every-center value-acquisition
lane is parked pending an additional arithmetic estimate. No next
execution or B06 task is issued merely to rename (7) or (11).** If new
conceptual work is subsequently requested, GPT-6 Astra at ultra effort
is appropriate; GPT-6.1 Sol at ultra effort follows only after a new
proof route and quantitative acceptance test are fixed. Parent time-zero,
OC and OA work is unchanged. No field scan, candidate-zero search or
manuscript expansion was undertaken.
The [return and continuation][next] records the completed pass and its
remaining boundary.

## 5. Collision-control premise check

Apply the [E05 screen][e05] and [controls12][controls] at the actual
points of use. The whole-phase estimate and scalar tangent inequality
are generic mathematical tools, not zero-exclusion premises.

| Control family | Canonical premise unavailable for unchanged source conclusions |
| --- | --- |
| Euler-factor and translated sources | Their completion, arithmetic arms and prime subtraction differ from E01/E03/E05. The exact theta moment used in (10) is not their moment law. |
| Weighted-square, finite-prefix/tail and finite-prime-orbit controls | Full unchanged square coefficients together with canonical reflection are absent; agreement at the selected finite primes does not supply the complete field or its rational-frequency moments. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Their positivity and reflection do not supply ordinary theta/zeta Dirichlet arithmetic. |
| Atomic and finite-profile controls, continuous extensions and heat counter-kernels | Selected moments and anchors do not identify the full canonical HDA field, correction and residual. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic fails despite retained completion and residue; their conditional status is preserved. |
| Fixed theta amplitude with variable readout | The literal cosine observation and physical Newman equation are absent. |
| Actual-theta three-profile relaxation | A relaxed positive measure is not the exact complete field and integer zero measure. |

The control screen does not move a control witness into this shrinking
time band. A generic bound can hold on a collision-free control window;
it cannot exclude a zero on an actual witness domain. No favorable
inequality in this note claims otherwise.

[brief]: 15_GNP_RS_B04_E05_RETURN_AND_MODEL_CHANGE_20261111.md
[request]: ../research-progress/handoffs/05_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_R1_20261111.md
[e05]: 14_GNP_RS_E05_FINITE_EULER_RESIDUAL_20261111.md
[e06]: 17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md
[review]: ../reviews/09_GNP_RS_B05_INTERNAL_REVIEW_20261111.md
[next]: 18_GNP_RS_B05_E06_RETURN_AND_MODEL_CHANGE_20261111.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
