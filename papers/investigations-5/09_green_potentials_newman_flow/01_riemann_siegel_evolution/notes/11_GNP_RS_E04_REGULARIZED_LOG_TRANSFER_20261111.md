# GNP-RS-E04 r1 — one-sided regularized logarithmic transfer

11 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex LLM assistance, **gpt-6.1-sol, effort ultra**
by explicit execution dispatch.

**Status: proved in-note from the named inherited inputs**, with
[separate internal same-model assessment][review]. This is the
return to the [frozen E04 r1 request][request]. The estimates pay the
complete Riemann–Siegel approximation error in an upper logarithmic
bound and pay the spatial phase discrepancy for each fixed prefix.
The signed Green margin remains open. These are acquisition estimates
under [avoid01][a01]. The [result index][results], [heat-flow cluster][r11],
[avoidance index][avoid], [control screen][controls] and [scope07][a07]
govern their application. The derivations use elementary estimates and
the inherited [E01][e01], [B02][b02] and [E03][e03] inputs.

## 1. Complete field and upper logarithmic transfer

Use the complete physical theta field \(V_\lambda=H_\lambda/C_-\)
with the exact carrier of E01 (E2). Set \(L_X=\log(X/(4\pi))\),
\(\lambda=c/L_X\) with \(1/2\le c\le1\), and keep that time fixed in
each spatial integral. Write \(W_X=[X-R_X,X+R_X]\),
\(R_X=(32/\pi)\log X\), \(K(t)=1/(16\cosh(\pi t/8))\),
\(d\mu_X(x)=K(x-X)\,dx\) on \(W_X\) and \(q_X=\mu_X(W_X)\).
Thus \(q_X\to1/2\) and \(q_X>0\). Retain the exact critical log
\(I_\lambda(X)\), prime subtraction \(P_{c,\lambda}(X)\),
outer allowance \(C_*/L_X\) and tail
\(T_X=D_VX^{-3}\log^2 X\) of B02 (B2)–(B5).

On \(W_X\), the B02 (B8) arm and its reflection are
\[
 A_\lambda(x)=\sum_{n\le N_x}w_n(\lambda,x)e^{i\nu_\lambda(x)\log n},
 \qquad S_\lambda(x)=A_\lambda(x)+e^{i\phi_\lambda(x)}
                                      \overline{A_\lambda(x)},
\]
\[
 N_x=\left\lfloor\sqrt{x/(4\pi)}\right\rfloor,\qquad
 w_n=n^{-1/2}\exp\{\lambda[(\log n)^2-L_x\log n]/4\},\qquad
 \nu_\lambda(x)=x/2+\pi\lambda/8,\quad
 \phi_\lambda(x)=2\Theta(\lambda,x).
\]
The cutoff varies at its actual real endpoints. At each \(x\) use the
fixed real chart of E03 §1, with the E01 §3.1 provider constants and
buffers. Eventually \(x\ge X/2\), \(L_x\ge16\), and
\(0\le\lambda L_x\le2\) on \(W_X\) for all \(c\). E03 §1 bounds the
normalized CS6 residual by \(2h_9 x^{-3/4}\). The full correction
is bounded by \(g_9 f_9 x^{-1/4}\), since its time factor
\(e^{-\pi^2\lambda/64}\le1\) and the real carrier ratio
\(|C_-(\lambda,x)/C_-(0,x)|=e^{\lambda(L_x^2-\pi^2/4)/16}\ge1\).
The correction bound covers every fractional cutoff. Taking
\(C=2^{3/4}(2h_9)+2^{1/4}g_9 f_9\) and \(X\ge1\) gives
\[
 |V_\lambda(x)-S_\lambda(x)|\le\epsilon_X=CX^{-1/4}
 \qquad(x\in W_X).
 \tag{E04.1}
\]

For complex numbers \(V,S\), the triangle inequality and
Cauchy–Schwarz applied to \((|S|,\delta)\) and
\((1,|V-S|/\delta)\) give, for every \(\delta>0\),
\[
 \log|V|\le\tfrac12\log(|S|^2+\delta^2)
             +\tfrac12\log(1+|V-S|^2/\delta^2).
 \tag{E04.2}
\]
The inequality at \(V=0\) uses \(\log 0=-\infty\). By the inherited
unit-log estimate \(\log|V_\lambda|\) is integrable on \(W_X\).
Apply (E04.2) with \(S=S_\lambda\) and \(\delta=X^{-1/8}\).
E01 and the exact critical tail then give
\[
 J_\lambda(X)\le
 \int_{W_X}\tfrac12\log(|S_\lambda(x)|^2+\delta^2)\,d\mu_X(x)
 -P_{c,\lambda}(X)+\frac{C_*}{L_X}+T_X
 +\frac{q_X}{2}\log(1+C^2X^{-1/4}).
 \tag{E04.3}
\]
The last term is \(O(X^{-1/4})\) uniformly in the frozen band.

## 2. Phase identity and independent phase average

For any arm \(A\in\mathbb C\), \(\delta>0\), and real \(\phi\), write
\[
 B_\delta(A)=\frac{\delta+\sqrt{\delta^2+4|A|^2}}{2},\qquad
 r_\delta(A)=\frac{\bar A^2}{B_\delta(A)^2}.
\]
Here \(B_\delta-|A|^2/B_\delta=\delta\) and
\(|r_\delta|=1-\delta/B_\delta<1\). Expanding the squared modulus
gives \(|A+e^{i\phi}\bar A|^2+\delta^2=
B_\delta^2|1+e^{i\phi}r_\delta|^2\). Hence
\[
 \tfrac12\log(|A+e^{i\phi}\bar A|^2+\delta^2)
 =\log B_\delta(A)+\Re\log(1+e^{i\phi}r_\delta(A)).
 \tag{E04.4}
\]
The log on the right is the convergent power series at \(1\).
Its \(\phi\)-average over one period is zero term by term. The mean
of the left side is exactly \(\log B_\delta(A)\), which is at most
\(\log(|A|+\delta)\). This includes \(A=0\). For a constant
amplitude, applying quadratic Jensen to the regularized squared
modulus gives the gap
\(q_X\log(1+|r_\delta(A)|^2)/2\), since its mean is
\(B_\delta(A)^2(1+|r_\delta(A)|^2)\).

At \(\delta=0\) and \(A\ne0\), the independent uniform phase average
of \(\log|A+e^{i\phi}\bar A|\) is \(\log|A|\), while its squared
modulus has phase mean \(2|A|^2\). The log average follows by
decreasing \(\delta\) to zero in (E04.4). For \(0<\delta\le1\)
the regularized logs decrease and are bounded above by
\(\tfrac12\log(4|A|^2+1)\); the limit is integrable because
the modulus is \(2|A|\,|\cos(\phi/2-\arg A)|\).
For a variable \(A\) with finite positive second moment and integrable
\(\log|A|\), let \(\mathbf E_X\) be expectation under \(d\mu_X/q_X\)
and average independently over a uniform phase. The exact gap of
quadratic Jensen in this product average, scaled by \(q_X\), is
\[
 \frac{q_X}{2}\log 2+
 q_X\left(\tfrac12\log\mathbf E_X|A|^2-\mathbf E_X\log|A|\right).
 \tag{E04.5}
\]
The amplitude contribution is nonnegative by concavity. For
constant nonzero amplitude the gap is \(q_X\log2/2\), tending
to \(\log2/4\). Formula (E04.5) is a product-average identity.
The actual spatial phase and arm enter (E04.4) together.

## 3. Actual spatial phase for a fixed prefix

Fix an integer \(M\ge1\) and a real \(\delta>0\), independent of
\(X,c\). Increase the onset so \(N_x\ge M\) on \(W_X\).
Let \(A_{\lambda,M}\) be the sum over \(n\le M\) and
\(S_{\lambda,M}=A_{\lambda,M}+e^{i\phi_\lambda}
\overline{A_{\lambda,M}}\). Because \(w_n\le n^{-1/2}\) for
\(n\le N_x\), the finite sum is uniformly bounded by
\(U_M=\sum_{n\le M}n^{-1/2}\). With time fixed,
\[
 \partial_x\log w_n=-\lambda\log n/(4x),\qquad
 \nu_\lambda'(x)=1/2,\qquad
 \phi_\lambda'(x)=L_x/2+\pi\lambda/(8x),\qquad
 \phi_\lambda''(x)=1/(2x)-\pi\lambda/(8x^2).
\]
Thus \(\|A_{\lambda,M}'\|_\infty\) is bounded in terms of \(M\),
\(\min_{W_X}\phi_\lambda'\ge L_X/4\) for large \(X\) and
\(\|\phi_\lambda''\|_\infty=O(X^{-1})\). Put
\(r(x)=r_\delta(A_{\lambda,M}(x))\). On the disk \(|A|\le U_M\)
the map \(A\mapsto r_\delta(A)\) is smooth with bounded first
derivatives, because \(B_\delta(A)\ge\delta\). Since
\(B_\delta(A)\le U_M+\delta\), we have
\(|r|\le\rho=U_M/(U_M+\delta)<1\) and
\(\|r'\|_\infty=O_{M,\delta}(1)\).

Set \(m=\min_{W_X}\phi_\lambda'\). Integration by parts, retaining
both endpoints of \(W_X\), gives for \(k\ge1\)
\[
 \left|\int_{W_X}r(x)^k e^{ik\phi_\lambda(x)}\,d\mu_X(x)\right|
 \le
 \frac{\rho^k(2\|K\|_\infty+\|K'\|_1)
          +k\rho^{k-1}q_X\|r'\|_\infty}{km}
 +\frac{q_X\rho^k\|\phi_\lambda''\|_\infty}{km^2}.
\]
The kernel norms on the right are over the real line. Divide by \(k\)
and sum the power series in (E04.4). Both
\(\sum_{k\ge1}\rho^k/k^2\) and \(\sum_{k\ge1}\rho^{k-1}/k\)
converge, so the modulus of the integral of the signed series is
\(O_{M,\delta}(1/L_X)\).
In particular there is a constant \(C_{M,\delta}\) uniform in
\(X,c\) for this discrepancy.

For the complete field retain
\[
 E_M(X,c)=\int_{W_X}|V_\lambda-S_{\lambda,M}|^2\,d\mu_X.
\]
Applying (E04.2) with \(S_{\lambda,M}\) and Jensen to its second
term with \(d\mu_X/q_X\) yields the complete upper bound
\[
 \boxed{\begin{aligned}
 J_\lambda(X)\le{}&
 \int_{W_X}\log B_\delta(A_{\lambda,M})\,d\mu_X-P_{c,\lambda}(X)\\
 &+\frac{q_X}{2}\log\!\left(1+\frac{E_M(X,c)}{q_X\delta^2}\right)
    +T_X+\frac{C_*+C_{M,\delta}}{L_X}.
 \end{aligned}}
 \tag{E04.6}
\]
The complete field, and therefore its correction, enters \(E_M\).
Formula (E04.6) holds for fixed \(M,\delta\). In (E04.3) the choice
\(\delta=X^{-1/8}\) pays the complete approximation error and leaves
the full spatial phase term of (E04.4).

## 4. First unpaid estimate and control screen

For the fixed-prefix route the first unpaid transfer input is an
every-center bound on \(E_M(X,c)\), including at exceptional centers.
If \(h>0\) is the headroom below \(m_*\) after paying the other terms
of (E04.6), the exact residual cap for that bound is
\(E_M(X,c)<q_X\delta^2(e^{2h/q_X}-1)\).
Even a negligible residual payment would leave the signed envelope
\(\int\log B_\delta(A_{\lambda,M})\,d\mu_X-P_{c,\lambda}\) to be
controlled within the defect margin. The full-arm route needs
control of the integrated phase term at growing cutoff before
replacing it by a phase average. The fixed-prefix constants give no
such estimate. For example, a relative phase already present in
the unregularized squared modulus is
\(\phi_\lambda(x)-\nu_\lambda(x)\log(mn)\). Its derivative at
\(m=n=N_x\) is
\((L_x-2\log N_x)/2+\pi\lambda/(8x)=O(x^{-1/2})\),
whereas the carrier derivative alone is of order \(L_x\).
This example identifies a failure of the derivative lower bound
for that relative phase. It gives no lower bound on the integrated
phase discrepancy.

For comparison, a direct specialization of [E03 §§1–3][e03] gives
for \(c=1\) and fixed \(M\)
\[
 \lim_{T\to\infty}\frac1T\int_T^{2T} E_M(X,1)\,dX
   =\sum_{n>M} n^{-3/2}.
 \tag{E04.7}
\]
In E03's auxiliary normalized formula subtract the two fixed
prefix arms at the auxiliary time. The remaining arms use precisely
the weights with \(M<n\le N_x\) and the same correction and residual.
Their squared-modulus error is bounded by the same absolute power
sums as for the full arms. The same-arm and cross-arm estimates use
the same actual pair intervals, phase derivatives and amplitude
variation bounds with pairs restricted to \(m,n>M\). Their summed
error bounds therefore only decrease. The diagonal of the two
arms tends uniformly on \([T,2T]\) to \(2\sum_{n>M}n^{-3/2}\) by the
same \(n^{-5/4}\) majorant. The fixed-time comparison uses the
identical weight and phase derivative bounds for the remaining
terms, and the same Fubini edges and kernel mass \(1/2\) apply.
The limit is a dyadic mean with positive tail for each fixed \(M\).
For each fixed \(M,\delta\), there are arbitrarily high centers with
\(E_M(X,1)\ge\frac12\sum_{n>M}n^{-3/2}\), so the residual payment
in (E04.6) cannot tend to zero uniformly in \(X\) for that pair.
The size of the payment relative to the available headroom for
a chosen pair remains undecided.

The [B02 §5][b02] and [E03 §5][e03] screens use the
[collision controls][controls] on their recorded domains.
The scalar regularization, equal-arm identity and fixed-prefix
phase argument apply to any data meeting their corresponding
algebraic and differentiability assumptions. The theta-specific
use of those inequalities consumes these further premises.

| Control family | First premise unavailable for the literal theta application |
| --- | --- |
| Euler-factor and translated sources | The complete normalized theta field, including its unchanged Dirichlet weights and prime subtraction. |
| Weighted squares and finite-prefix or finite-tail modifications | The full unchanged square coefficients together with canonical reflection in the inherited Riemann–Siegel estimate. |
| Finite-prime orbits | Full source reflection and all canonical coefficients despite matching selected primes and measurements. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | The ordinary theta/zeta Dirichlet arithmetic in the field estimate. |
| Atomic and finite-profile controls including continuous extensions, and heat counter-kernels | The complete canonical theta field and its Riemann–Siegel formula. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic despite the retained completion data. |
| Fixed theta amplitude with variable readout | The actual cosine readout and its physical Newman equation. |
| Relaxed positive Green profiles | Identification with the exact theta field and its integer zero measure. Finite profile constraints do not supply the complete boundary log. |

The control screen identifies absent premises. The generic
inequalities allow boundary zeros and yield no exclusion on their
own. The proof completes the bounded transfer and fixed-prefix
calculation, leaving the actual signed all-center estimate open.

[request]: ../research-progress/handoffs/03_GNP_RS_E04_REGULARIZED_LOG_TRANSFER_R1_20261111.md
[e01]: 03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md
[b02]: 05_GNP_RS_B02_JENSEN_AND_SHIFTED_ZETA_COMPARISON_20261111.md
[e03]: 07_GNP_RS_E03_COHERENT_JENSEN_OBSTRUCTION_20261111.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md

[review]: ../reviews/07_GNP_RS_B03_E04_INDEPENDENT_REVIEW_20261111.md
