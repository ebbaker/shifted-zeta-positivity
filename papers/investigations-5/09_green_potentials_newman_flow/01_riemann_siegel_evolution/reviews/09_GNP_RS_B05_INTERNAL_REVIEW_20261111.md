# GNP-RS-B05 and E06 internal assessment

11 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance, **gpt-6.1-sol, actual dispatched effort
ultra**. This is a separate-agent, different-model review of the
gpt-6-astra / ultra [B05 decision][b05] and a separate-agent,
same-model review of the gpt-6.1-sol / ultra [E06 proof][e06]. I
developed and shared the fixed-reference tangent proof before reviewing
its use in E06. The review therefore shares proof development as well
as the inherited HDA, E01, E03, E04 and E05 inputs. Their review status
is unchanged. This is an analytical check with no new data certificate
or specialist human review.

I accept B05 and E06 at their stated scopes. The growing finite-Euler
reference has a uniformly paid phase and normalization on the full
original band. Its every-center arithmetic residual remains unpaid.
For fixed \(P\) at \(c=1\), the tested signed tangent allowance is
unbounded at arbitrarily high centers, uniformly over regulators
chosen separately at each center. The [result index][results],
[heat-flow cluster][r11], [avoidance index][avoid] and
[control screen][controls] govern these conclusions.

## Growing reference and whole-phase estimate

At fixed spatial \(P,c,\lambda\), the canonical finite-Euler logarithm
has absolute geometric sums for its two derivatives. Because
\(\nu_\lambda'=1/2\), twice the first derivative uses the prime sum
with coefficient one and twice the second uses coefficient \(1/2\).
Together with \(\sum_{n\le P}n^{-5/8}\le(8/3)P^{3/8}\), this
gives the stated \(D_1(P),D_2(P)\) in (E06.1). Subtracting the
reference angle gives \(\psi'=\phi_\lambda'-2(\Im\ell_P)'\).
On the frozen window, \(\phi_\lambda'\ge L_X/2-R_X/X\), so
the two \(L_X/8\) gates indeed give \(\psi'\ge L_X/4\). The
bound \(D=\|\psi''\|_\infty\) in (E06.2) includes both parts
of the carrier second derivative.

The unit-arm factorization puts the reference angle inside
\(e^{ik\psi}\) and leaves the amplitude of the \(k\)-th
coefficient constant. The integration by parts on the finite
window pays both endpoints, \(K'\) and \((1/\psi')'\).
Using \(2\|K\|_\infty+\|K'\|_1=1/4\), \(q_X\le1/2\), and
\(\sum_{k\ge1}\rho^k/k^2\le2\) gives exactly
\(2/L_X+16D/L_X^2\). This bound is uniform in
\(\rho=b_\delta^{-2}<1\), so it is uniform in every
\(\delta>0\) fixed within the integral. For the reference
zeros, apply monotone convergence to a constant minus the
uncentered regularized log. Its limit integral is finite by
the two-sided uniform bound and \(q_X\log b_\delta\to0\).
This establishes (E06.4) with the zeros included.

At \(P=\lfloor L_X^2\rfloor\), both derivative costs are
\(O(L_X^{3/4}(\log L_X)^2)=o(L_X)\), and the onset
\(D\le L_X\) gives \(18/L_X\). The same argument pays the
phase for \(P\le L_X^\gamma\) with fixed \(\gamma<8/3\).
No derivative of the cutoff or physical time is taken in the
window. The omitted prime powers all exceed \(P\), giving the
\(O(L_X^{-3})\) cost by E01. The reference log is bounded by
\((8/(3\kappa))P^{3/8}\) on the whole line. Multiplying by the
kernel exterior mass \(O(X^{-4})\) pays its exterior separately
from the exact critical-log tail. The reciprocal product satisfies
\(|E_P|^{-1}\le\exp((8/3)P^{3/8})\). Applying it to the full
E04 correction and residual bound gives (E06.5), a relative
field approximation of size \(X^{-1/4+o(1)}\).

The upper allowance (E06.6) retains the exact complete-field
\(R_{P(X)}\). In particular the small field approximation error
does not estimate the arithmetic difference between the retained
arms and the reference. The first unpaid step is a uniform
short-window bound for this exact residual at the chosen
regulator and margin. The E05 ordered fixed-\(P\) limits
supply no bound at the growing cutoff.

## Fixed-reference signed tangent

Write \(w=V/E_P\), \(a=1+e^{i\psi}\), \(h=|a|^2+\delta^2\)
and \(H=4+\delta^2\). The logarithm tangent at \(h\) is an
upper bound for \(\log|w|\), with the exact signed cross term
retained in \(|w|^2\). Since \(h\le H\) and
\(h/H\ge |a|^2/4\), its integrated lower bound before the last
scalar inequality is
\[
 \frac{q_X}{2}\log H-\frac{q_X}{2}+\frac{Z}{2H}
 +\int_{W_X}\log|a|\,d\mu_X-q_X\log2,\qquad
 Z=\int_{W_X}|w|^2\,d\mu_X .
\]
Applying \(t-1\ge\log t\) to \(t=Z/(q_XH)>0\) removes \(H\)
and yields (E06.7). The integrated reference log is \(O_P(1/L_X)\)
by (E06.4). For fixed \(P\), \(\sup|E_P|=B_P<\infty\)
and \(Z\ge M(X,1)/B_P^2\). E05 gives arbitrarily high centers
with \(M(X,1)\) arbitrarily large. At those centers the lower
bound for the majorant grows independently of \(\delta\),
because \(q_X\to1/2\) and the restored reference log minus
the prime baseline stays bounded. This proves the stated
obstruction for the fixed-reference tangent with a regulator
constant on the window. It gives no lower bound for \(J\).

B05's exact signed log difference is integrable as the difference
of the true and reference logs. Expanding a relative residual
through a simple reflected-reference zero would require additional
denominator control. If the field residual were nonzero at such
a point, its quotient by the reference would have a nonintegrable
squared modulus locally. Neither note asserts this mismatch for
the actual field. The signed nonlinear value and a varying-reference
tangent are outside the proved obstruction.

The premise screens apply at the controls' actual witness domains.
The generic phase and tangent inequalities retain their own scope.
The canonical field comparison and moment use the complete unchanged
theta arithmetic, reflection and provider correction. Finite-prime
compatibility lacks full reflection and coefficient data. Reflected
and primitive-compatible controls lack ordinary theta/zeta arithmetic,
and variable readouts lack the physical cosine/Newman evolution.
The bounded pass supplies neither an exceptional-center exclusion nor
a premise for a further execution task. [Continuation][next]

[b05]: ../notes/16_GNP_RS_B05_ADAPTIVE_AND_SIGNED_DECISION_20261111.md
[e06]: ../notes/17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md
[next]: ../notes/18_GNP_RS_B05_E06_RETURN_AND_MODEL_CHANGE_20261111.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
