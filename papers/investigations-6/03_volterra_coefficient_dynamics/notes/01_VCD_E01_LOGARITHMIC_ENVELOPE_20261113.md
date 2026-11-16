# VCD-E01 — All-degree logarithmic coefficient envelope

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Tool dispatch **gpt-6.1-sol /
ultra**. Separate backend verification unavailable.

**Proved in-note.** For the complete theta source, use the nonnegative
real branch of \(\operatorname{arcosh}\) and put
\(B_n=\operatorname{arcosh}^2(2n+12)/16\).
\[
 \beta_n(\lambda)+\beta_{n+1}(\lambda)\le B_n
 \qquad(n\ge0,\ 0\le\lambda\le1/2),                                     \tag{E1}
\]
\[
 \frac{h_N(1/2)}{h_0(1/2)}\le\prod_{j=0}^{N-1}B_j
 \le\left[\frac{\operatorname{arcosh}(2N+10)}4\right]^{2N}
 \qquad(N\ge1).                                                       \tag{E2}
\]
Degrees are integers. This intermediate estimate supplies the normalized
monic norm factor for fixed-chain quadrature. The
[frozen request](../research-progress/handoffs/VCD-E01-r1.md)
and [verified input manifest](../numerics/01_VCD_B01_E01_INPUTS_20261113.json)
fix the source and method. See the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md), [controls 12](../../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md) and
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. Complete source and score

On \(u\ge0\), let \(\rho=\pi e^{4u}\), \(r_m=m^2\rho\),
\(s_m=e^u r_m(2r_m-3)e^{-r_m}\), and \(\Phi=\sum_{m\ge1}s_m\).
The [complete source](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex)
gives its actual smooth even reflection. Each \(s_m>0\), since
\(r_m\ge\pi>3\). With \(r_m'=4r_m\), its logarithmic derivative is
\[
 1+4+\frac{8r_m}{2r_m-3}-4r_m
 =9+\frac{12}{2r_m-3}-4r_m .
\]
For \(j=0,1\), the \(j\)-th derivative of \(s_m\) on \(u\ge0\) is
\(e^u\) times a degree \(2+j\) polynomial in \(r_m\) times \(e^{-r_m}\).
Its absolute value is bounded by a constant times
\[
 e^u\rho^{2+j}e^{-\rho}\,m^{4+2j}e^{-\pi(m^2-1)} .
\]
The \(m\)-factor is summable and the \(u\)-factor bounded on compact
intervals, justifying local uniform convergence and termwise
differentiation. With \(\rho(u)=\pi e^{4|u|}\), reflection gives
\[
 |\Phi^{(j)}(u)|\le C_j e^{|u|}\rho(u)^{2+j}e^{-\rho(u)}
 \qquad (j=0,1)
\]
on the full line, with constants depending only on the source.

Set \(W_\lambda=e^{\lambda u^2}\Phi\) and \(V_\lambda=-\log W_\lambda\).
For \(u\ge0\), \(\Phi'/\Phi\) is the mean of the summand scores with
positive weights \(s_m/\Phi\) summing to one. The inequalities
\(12/(2r_m-3)<4\) and \(2\lambda u\le u\) give
\[
 V_\lambda'(u)\ge 4\pi e^{4u}-13-u .                                     \tag{1}
\]
The mean uses the exact sum. Both \(V_\lambda\) and \(uV_\lambda'(u)\)
are even.

## 2. A convex lower bound

Write \(t=|u|\). If \(t\le1/2\), (1) gives
\(uV_\lambda'(u)\ge-13t-t^2\ge-27/4\).
The tail of \(\cosh 2=1+2+\sum_{k\ge2}4^k/(2k)!\) starts at \(2/3\)
and has successive ratios at most \(2/15\), so \(\cosh 2\le3+10/13<4\).
In this case \(\cosh(4u)-11<-7<-27/4\).

If \(t\ge1/2\), then \(4\pi-1/t>10\), and
\(10e^{4t}\ge10+40t\ge13+t\) since \(39t\ge39/2>3\). Thus
\[
 (4\pi t-1)e^{4t}\ge t(13+t),\qquad
 uV_\lambda'(u)\ge e^{4t}\ge\cosh(4t).
\]
The two cases give, uniformly in the allowed heat times,
\[
 uV_\lambda'(u)\ge\cosh(4u)-11 .                                        \tag{2}
\]

## 3. Monic integration by parts and Jensen

Let \(P_n=P_n(u;\lambda)\) be monic orthogonal polynomials for
\(W_\lambda du\), with \(h_n=\int P_n^2W_\lambda du>0\),
\(\beta_n=h_n/h_{n-1}\) for \(n\ge1\) and \(\beta_0=0\).
Existence at each finite degree follows from positivity on the whole
line and finite moments. The bounds from §1 and
\(W_\lambda'=e^{\lambda u^2}(2\lambda u\Phi+\Phi')\) show that any
fixed polynomial times \(W_\lambda\) or \(W_\lambda'\) is absolutely
integrable and tends to zero at both ends. The relevant bounds are
constant multiples of
\[
 (1+|u|)^k e^{u^2/2+c|u|}\rho(u)^d e^{-\rho(u)}
\]
for fixed \(k,c,d\). The logarithm of this expression is at most
\(-\rho(u)/2\) for large \(|u|\), because \(\rho(u)\) grows
exponentially in \(|u|\) and the other logarithmic terms are at most
quadratic. The same bound covers multiplication of \(P_n^2W_\lambda\)
by \(\cosh(4u)\) after increasing \(c\).

Integrate \((uP_n^2W_\lambda)'\) over the full line. The boundary term
vanishes, and \(uP_n^2W_\lambda'=-uV_\lambda'P_n^2W_\lambda\)
is integrable by the preceding \(W_\lambda'\) bound. The polynomial
\(uP_n'-nP_n\) has degree less than \(n\), with the zero polynomial
at \(n=0\). Orthogonality gives
\[
 0=h_n+2nh_n-\int uV_\lambda'P_n^2 W_\lambda\,du,\qquad
 \mathbb E_{\nu_n}[uV_\lambda']=2n+1,\quad
 d\nu_n=P_n^2W_\lambda\,du/h_n .                                       \tag{3}
\]
In \(uP_n=P_{n+1}+\beta_nP_{n-1}\), evenness removes the diagonal
and the term with \(P_{-1}\) is omitted at \(n=0\). Squaring in the
weighted norm gives
\[
 \mathbb E_{\nu_n}[u^2]=h_{n+1}/h_n+\beta_n
                       =\beta_{n+1}+\beta_n .                          \tag{4}
\]
For \(n\ge1\) the second squared term is \(\beta_n^2h_{n-1}/h_n=\beta_n\).
The first term alone gives (4) at zero.

The series \(f(v)=\cosh(4\sqrt v)=\sum_{k\ge0}16^kv^k/(2k)!\)
is convex for \(v\ge0\), since its partial sums are convex there and
their finite-valued pointwise limit preserves convexity. Jensen with
(2)–(4) gives
\[
 \cosh(4\sqrt{\beta_n+\beta_{n+1}})
 \le\mathbb E_{\nu_n}[\cosh(4u)]\le2n+12 .
\]
Taking the nonnegative inverse and squaring proves (E1). Each fixed
degree allows this integration by parts. The score constant \(11\)
is common to all degrees and heat times, and the boundary term is
zero for every degree. A uniform tail estimate for growing derivative
order is unnecessary.

## 4. Fixed initial norm factor

From (E1) at \(n=j-1\), \(\beta_j\le B_{j-1}\) since
\(\beta_{j-1}\ge0\). At \(\lambda=1/2\) multiply for \(1\le j\le N\)
and telescope the norm ratios. The increasing \(B_j\) are bounded
over \(0\le j<N\) by \(B_{N-1}=\operatorname{arcosh}^2(2N+10)/16\).
This proves (E2). The polynomial is monic for either \(W_{1/2}du\) or
its probability normalization \(W_{1/2}du/h_0(1/2)\). Its squared norm
for the latter is \(h_N(1/2)/h_0(1/2)\), as used with \(J(1/2)\).
Here \(a_n=\sqrt{\beta_n}\), \(Z_\lambda=h_0(\lambda)\) and
\(H_\lambda(z)=Z_\lambda\langle e_0,e^{izJ(\lambda)}e_0\rangle/2\).
The norm factor can enter the separate JCH readout error estimate.

## 5. Actual control screen

The [B01 screen](../brainstorm/notes/01_VCD_B01_LOGARITHMIC_ENVELOPE_DECISION_20261113.md)
specifies sources and qualifiers. These checks concern the indicated
proof premises and, where shown, the envelope itself. The collision
witnesses retain their source evidence without a new numerical replay.

| Catalog control | Result of the screen |
| --- | --- |
| Inherited \(2+2e^{\lambda-T}\cos x\) | The three atoms lack a positive absolutely continuous density and score. At the inherited event (with \(T\) in range), \(\beta_1+\beta_2=1>B_1\), since the first three terms of \(\cosh4\) give \(1+8+256/24>14\). Its Volterra flow remains regular. |
| Euler-factor shifts | The translates change the input summand scores. At \(\lambda=0,c=1/2,p=23\), the normalized second moment of the even shifted mixture is the theta second moment plus \(ca^2/(1+c)=(\log23)^2/12\) for \(a=\tfrac12\log23\). This exceeds \(3/4\) since \(e<11/4\) (the series from \(1/3!\) has ratios at most \(1/4\)) and \((11/4)^3<23\). But \(\cosh\sqrt{12}>1+6+6=13>12\), so \(B_0<3/4\). This is a failure of (E1) at the one catalog prime. Other primes are untested here. |
| Three- and four-node positive weighted squares | Every fixed positive weight cancels in its summand score, so (1) holds for their positive averages. The even extensions are locally absolutely continuous with the same tail type. The two half-line integrations by parts have zero junction terms because of the factor \(u\). Thus both actual controls satisfy (E1) even at their catalog collisions, and (E2) follows. They fail full smooth reflection and the complete canonical coefficients, premises unneeded by the proof. |
| Reflected super-Gaussian | The logarithmic derivative of the positive mixture of translates of \(e^{-u^4}\) is an average of cubic polynomials. The heat weight and Gaussian factor contribute linear terms. Thus \(uV'_\lambda=O((1+|u|)^4)\), and (2) fails eventually. Its coefficient bound was untested. |
| Smooth shape and positive-primitive controls | The sources use freely small damping in \(\exp[-\delta\cosh(4u)]\) and lack the exact theta summand score. The weaker (2) and (E1) remain untested across the allowed damping families. The catalog constructions retain their sufficiently-small-damping qualification. |
| Finite-prime-orbit square sources | Full canonical reflection fails. Bounded nonnegative weights can retain the half-line score and domination, so a locally absolutely continuous even extension can retain the envelope. The estimate does not enforce infinite arithmetic compatibility. |
| Atomic and finite-profile threshold families | The atoms fail the positive density and score premise. The triangular compact extensions lack a globally positive full-line density on which \(V=-\log W\) is defined. No blanket coefficient-bound failure is assigned. |
| RH-conditional normalized endpoint controls | The perturbations fail ordinary Dirichlet series arithmetic, and the exact theta sum-to-score derivation is unavailable. Their (2) and (E1) are untested here. The catalog construction remains RH-conditional. |
| Fixed theta amplitude, altered observation | The score and recurrence are unchanged, so the same estimate holds. The altered observation fails the full physical cosine/Newman equation. |

The weighted-square witnesses delimit the result to a quantitative
approximation allowance. They preclude collision exclusion based on
this allowance alone within the displayed score class.
