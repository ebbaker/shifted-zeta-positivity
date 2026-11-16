# TN6-E01 r1 — Coefficient bound to finite-chain scalar depth

13–14 November 2026, America/New_York. Prepared for **Edward Baker**
with substantial OpenAI Codex LLM assistance. Execution dispatch
**gpt-6.1-sol / ultra**. Actual backend model and effort unavailable.
**Status: proved in-note from the two acquired branch bounds.**

The [frozen request][request] has SHA-256
460ae66336dcfbecc8387baa57d650d3d63ee193ce5403c9f5575dc2478c2e9c.
The [input manifest][manifest] has SHA-256
284db6eb028fde1697b7647a207827b9acf4eb1f5d22c655db9dd83c28e666ab
and all nine hash and size checks passed. After issuance the
[JCH-E02 assessment][jreview] accepted the pinned JCH proof without
correction, SHA-256
d04f8e6a4fc9e2f619ab5c2f46a39b416c5ead0baad411b85db914d36c2c3ed3.
Both providers have same-worker internal assessments sharing
their sources. The shared proof uses the frozen transfer only.

This is the intermediate absolute approximation milestone selected in
[TN6-B01][decision]. See the [result index][results], [avoid index][avoid],
[controls 12][controls], [classification rule][a01], [control-premise
rule][a02] and [scope rule][a07].

## 1. Match the normalized monic norm and scalar observation

Keep the [complete theta source][source] \(\Phi\) and the fixed time
slice \(W_*=e^{u^2/2}\Phi\), with \(Z_*=\int_{\mathbb R}W_*\,du>0\)
and \(d\mu_*=W_*\,du/Z_*\). In the VCD notation
\(h_N(\lambda)=\int P_N(u;\lambda)^2 e^{\lambda u^2}\Phi(u)\,du\)
is unnormalized. Dividing the measure by the positive constant
\(h_0(1/2)=Z_*\) preserves the monic polynomials and the ratios of
adjacent norms. Thus the norm factor in [JCH-E01][jch] is
\[
 h_N^*=\int P_N(u;1/2)^2\,d\mu_*(u)
       =\frac{h_N(1/2)}{h_0(1/2)}
       =\prod_{j=1}^N\beta_j(1/2),\qquad
 a_j=\sqrt{\beta_j(1/2)} .
\]
The fixed \(J_*=J(1/2)\) is the multiplication operator in the
orthonormal basis of \(\mu_*\), with \(a_j\) linking sites \(j-1\)
and \(j\). The finite \(J_N\) uses sites \(0,\ldots,N-1\) and its own
square in the evolution. The omitted edge \(a_N\) enters \(h_N^*\);
it is outside \(J_N\). All time dependence uses
\(\lambda=1/2-\tau\) and the factor \(e^{-\tau J_N^2}\) on this
fixed basis. The readout has normalization \(Z_*/2=H_{1/2}(0)\):
\[
 H_N(\tau,x)=\frac{Z_*}{2}\langle e_0,
                 e^{-\tau J_N^2}e^{ixJ_N}e_0\rangle .
 \tag{T1}
\]
On \(0\le\tau\le 1/2\), \(|x|\le X<\infty\), \(X\ge0\), define
\(E_N(\tau,x)=|H_{1/2-\tau}(x)-H_N(\tau,x)|/(Z_*/2)\). For every
integer \(N\ge1\), JCH-E01 R2 gives
\[
 E_N(\tau,x)\le h_N^* S_N(\tau,x),\qquad
 S_N(\tau,x)=\sum_{k=0}^N\frac{\tau^kx^{2N-2k}}{k!(2N-2k)!}.
 \tag{T2}
\]
At the fixed slice, [VCD-E01][vcd] E2 gives
\[
 h_N^*\le\prod_{j=0}^{N-1}\frac{\operatorname{arcosh}^2(2j+12)}{16}
       \le\left(\frac{L_N}{4}\right)^{2N},\qquad
 L_N=\operatorname{arcosh}(2N+10)>0 .
 \tag{T3}
\]
The first product times \(S_N\) is an optional sharper algebraic
allowance. The transfer uses the base slice only.

## 2. Uniform explicit error and sufficient depth

The product of the power series for \(e^{\tau r^2}\) and
\(\cosh(xr)\) has coefficient \(S_N(\tau,x)\) at \(r^{2N}\)
by matching \(2k+2(N-k)=2N\). All coefficients are nonnegative
for the stated real parameters. For each \(r>0\),
\[
 S_N(\tau,x)\le r^{-2N}e^{\tau r^2}\cosh(xr)
             \le r^{-2N}e^{\tau r^2+Xr}.
\]
Substituting \(r=L_N/2\) and using \(\tau\le1/2\) gives
\[
 \boxed{\sup_{0\le\tau\le1/2,\,|x|\le X} E_N(\tau,x)
    \le\exp\left[-N\log4+\frac{XL_N}{2}+\frac{L_N^2}{8}\right].}
 \tag{T4}
\]
The factor \(4^{-N}\) comes from
\(((L_N/4)/(L_N/2))^{2N}\). This also proves convergence for fixed
\(X\) as \(N\to\infty\), since \(L_N\le\log(4N+20)\).

For \(0<\epsilon\le1\), let \(D=\log(1/\epsilon)\),
\(K=X+D+1\ge1\) and \(A=\log(16K)\). Set
\[
 \boxed{N=\left\lceil 4K\log(16K)\right\rceil .}       \tag{T5}
\]
To bound \(A\), the first five terms of \(e^3\) sum to more than
\(16\), giving \(\log 16<3\), while \(\log K\le K-1\).
Thus \(A\le3K\). The ceiling bounds \(4KA\le N<4KA+1\) give
\[
 4N+20\le16KA+24\le48K^2+24\le72K^2\le256K^2 .
\]
Since \(\operatorname{arcosh} y=\log(y+\sqrt{y^2-1})\le\log(2y)\)
for \(y\ge1\), it follows that \(L_N\le\log(4N+20)\le 2A\).
Now \(\log4>1\), by integrating \(1/t\) from \(1\) to \(2\)
and doubling, so the exponent in (T4) is at most
\[
 -4KA+XA+\frac{A^2}{2}
 \le-4KA+KA+\frac32 KA
 =-\frac32 KA\le -D .
\]
In the last step, \(A\ge\log16>1\) and \(K\ge D\).
Hence the bound in (T4) at (T5) is at most \(\epsilon\). The physical
absolute error is at most \(H_{1/2}(0)\epsilon\). At \(X=0\) or
\(\epsilon=1\), \(K\ge1\) and the same inequalities hold, including
\(K=1\). Formula (T4) is valid at \(N=1\), with \(L_1>0\), and
(T5) always yields \(N\ge1\). The corner \((\tau,x)=(0,0)\)
has exactly zero error by normalization; the pure-height and pure-time
edges are included by the nonnegative series with zero powers set to
one. The sufficient depth has order \(K\log(K+1)\) for this bound.

## 3. Matched evaluation and the actual collision controls

Direct Gaussian quadrature for this same complete normalized source
has exactly the \(N\)-site scalar output in (T1). The gain in (T4) and
(T5) is a known remainder and sufficient depth without computing
\(h_N^*\) or enclosing a separate Gaussian source moment. To evaluate
the scalar or certify a computed approximation still requires the
\(a_1,\ldots,a_{N-1}\) of \(J_N\), \(Z_*\), and the enclosures for
source integration, coefficient acquisition and finite evaluation.
The bound is measured in units of the fixed base mass. Relative
accuracy would require a separate lower margin for the varying
readout. These estimates cover real scalar absolute error. Actual
state-prefix error and a speed advantage remain unestablished.

The [B01 screen][decision] and provider screens distinguish failed
premises from failed inequalities. The following checks use their
stated actual witnesses.

| Witness | Application of the transferred estimate |
| --- | --- |
| Three atoms \(F_\lambda(x)=2+2e^{\lambda-T}\cos x\) | At \((T,\pi)\) the three-site scalar is exactly zero and has zero error. The atomic density/score premise fails. At the event \(\beta_1+\beta_2=1>B_1\), since \(\cosh4>14\). This failure of the VCD coefficient envelope at the event coexists with exact finite termination. |
| Euler-factor shifts | At \(c=1/2,\ p=23,\ \lambda=0\), VCD's checked second moment violates \(B_0\). The untranslated theta score formula fails, while the generic JCH estimate is available. This particular failure concerns the VCD bound at time zero. The \(\lambda=1/2\) norm envelope and scalar bound for these sources were untested. |
| Three- and four-square controls | Their positive square summands preserve the score inequality, and their even locally absolutely continuous extensions allow integration by parts with zero junction term. They also satisfy the generic quadrature hypotheses. Both providers and the transfer can hold at the certified positive-time events \(T=1/4\) and \(T=1/100\). The full reflection and unmodified theta coefficient premises fail for these controls. |
| Reflected super-Gaussian event | The exponential lower confinement premise fails since its score times \(u\) grows at most polynomially. Its moments support JCH. The VCD coefficient envelope remains untested. |
| Smooth shape and positive-primitive witnesses | They lack the exact summand score formula. The generic JCH argument applies from their tails. The weaker VCD score or coefficient inequalities remain untested for the sufficiently-small-damping constructions. |
| Finite-prime-orbit controls | Positive modified weights can preserve the score in the stated even extension class, with altered arithmetic and no full reflection. The generic scalar bounds are source-by-source and apply on boxes containing the relevant event. |
| Fixed-event and finite-profile threshold families | Atomic supports terminate exactly and fail the positive-density score premise. Compact triangular extensions have the JCH moments but lack a positive full-line density. The coefficient envelope was untested as a general statement across these families. |
| RH-conditional endpoint controls | Their construction retains its RH hypothesis. They fail ordinary Dirichlet-series arithmetic and the unchanged summand formula is unavailable. The score and envelope were untested. The scalar estimates apply when the actual source has the required moments and the chosen box includes the event under consideration. |
| Fixed source and altered kernel | The source coefficient bound is unaffected. The changed kernel fails the cosine/Newman observation premise of the transfer. |

At a zero in the box a valid scalar allowance dominates the absolute
approximate value, including on the exact atomic example. In particular
the weighted-square controls prevent reading the transferred approximation
allowance as a collision exclusion within the score class used here.

[request]: ../research-progress/handoffs/TN6-E01-r1.md
[manifest]: ../numerics/04_TN6_E01_INPUT_MANIFEST_20261113.json
[decision]: ../brainstorm/notes/01_TN6_B01_COEFFICIENT_TO_SCALAR_DECISION_20261113.md
[source]: ../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex
[jch]: ../02_jacobi_chain_height_flow/notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md
[jreview]: ../02_jacobi_chain_height_flow/reviews/01_JCH_E02_FINITE_CHAIN_ASSESSMENT_20261113.md
[vcd]: ../03_volterra_coefficient_dynamics/notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../avoid/01_restating_the_target.md
[a02]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
