# GNP-RS-B03 and E04 internal assessment

11 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance, **gpt-6.1-sol, actual dispatched effort
ultra**. This is a separate-agent, different-model check of the
gpt-6-astra / ultra [B03 proof][b03] and a separate-agent, same-model
check of the gpt-6.1-sol / ultra [E04 proof][e04]. The checks share the
inherited E01, E03 and HDA inputs. The HDA provider's review status is
unchanged. This assessment adds no new data certificate and has had no
specialist human review.

I accept B03 (8) and E04 (E04.1)–(E04.7) at their stated scope.
B03 obstructs the corrected quadratic-Jensen expression at arbitrarily
high centers in the \(c=1\) subfamily. E04 pays the complete-field
approximation error and proves a fixed-prefix phase estimate while retaining
its complete residual. The signed Green margin remains open. The [result
index][results], [heat-flow cluster][r11], [avoidance index][avoid] and
[control screen][controls] govern the scope of these claims.

## B03 corrected quadratic-Jensen expression

At a fixed nonzero arm amplitude \(a\), independent uniform phase gives
quadratic mean \(2a^2\) and log mean \(\log a\). Thus the scaled cosine
loss is \(q_X\log2/2\). An amplitude distribution contributes its own
Jensen gap. The subtraction in B03 (7) defines a diagnostic using
this ideal independent phase law.

Negating B03 (8) gives the eventual strict upper bound
\(\mathcal B_{\rm ph}<m_*+1/1000\). Dropping the nonnegative tail and
outer allowances and exponentiating yields exactly
\[
 M(X,1)<2q_X\exp\!\left(2[m_*+1/1000+P_{1,1/L_X}(X)]/q_X\right).
\]
The prefactor tends to one. Replacing \(q_X\) by \(1/2\) and
\(P_{1,1/L_X}(X)\) by \(P_{1,0}(X)\) changes the exponent by a
uniform \(o(1)\). Uniform boundedness of the exponents allows the
same replacement after exponentiating. The E03 dyadic moment law then
requires \(\zeta(3/2)\le e^{4(m_*+1/1000)}\mathfrak E\), where
\(\mathfrak E\) is the dyadic mean of \(e^{4P_{1,0}}\).

The finite-prime mean factors because each nonconstant torus character
has nonzero frequency by unique factorization. Each prime block has
mean zero, with its own harmonics retained in one block. Its amplitude
bound \(b_p\) gives an exponential mean at most
\(\cosh(4b_p)\le e^{8b_p^2}\) by the convex chord inequality.
Absolute summability justifies uniform passage to the full exponential
and hence \(\mathfrak E\le\exp(8\sum_p b_p^2)\).

I reproduced the exact scalar fractions in B03 (12) and (16). A second
set of rational bounds also proves the stated margin without using the
sharper \(p=2,3\) first-coefficient budgets. Write \(u_p=p^{-11/4}\).
Then \(u_2<3/20\) and \(u_3<1/20\) by fourth powers. Keeping the first
denominator at \(p=2\) and using \(1/k\le1/2\) for \(k\ge2\) gives
\[
 b_2\le(16/17)u_2+u_2^2/[2(1-u_2)]<31/200,\qquad
 b_3\le u_3+u_3^2/[2(1-u_3)]<13/250.
\]
For \(p\ge5\), \(b_p\le(20/17)u_p\). The integer tail comparison and
\(\sqrt5>2\) give
\[
 \sum_{p\ge5} b_p^2
 \le (20/17)^2\left(5^{-11/2}+\int_5^\infty t^{-11/2}\,dt\right)
 < (20/17)^2(1/6250+1/5625)<1/2000.
\]
Hence \(\sum_p b_p^2<27229/10^6<11/400\). Even with these looser
bounds, \(4(m_*+1/1000)+8\sum_p b_p^2<118/125\) using E03's
\(m_*<9/50\). The same Taylor majorant gives
\(e^{118/125}\le83337/32125<13/5<\zeta(3/2)\), the required
contradiction. The positive \(1/1000\) margin also preserves failure
at \(m_*\) after adding a uniform \(o(1)\) term to the diagnostic.

## E04 transfer and phase calculation

- **Complete field.** Recenter the inherited real HDA charts pointwise.
  The normalized CS6 residual is at most \(2h_9x^{-3/4}\) since the
  carrier moduli agree at real \(x\). The normalized complete correction
  is at most \(g_9f_9x^{-1/4}\) because the time factor is at most one
  and the ratio of carrier moduli at times \(\lambda,0\) is at least one.
  Both are uniform through fractional cutoffs. On the window \(x\ge X/2\),
  the constant in (E04.1) bounds their sum. Cauchy–Schwarz gives the
  one-sided log inequality even at a vanishing approximant. At
  \(\delta=X^{-1/8}\), the resulting transfer payment is \(O(X^{-1/4})\).
  The exact critical log outside the window is controlled by the
  inherited \(T_X\), and the outer payment remains \(C_*/L_X\).
- **Reflected factorization.** With \(a=|A|\), \(B^2-\delta B=a^2\),
  so \(B^2+a^4/B^2=2a^2+\delta^2\). The cross coefficient is
  \(\overline A^2\), as in (E04.4). The convergent Fourier log has zero
  independent phase mean, including when \(A=0\). For constant amplitude
  the regularized quadratic gap is \(q_X\log(1+|r|^2)/2\), since the
  mean square with the regulator added is \(B^2(1+|r|^2)\).
  Taking \(\delta\downarrow0\) at fixed nonzero amplitude recovers the
  gap used in B03.
- **Spatial phase.** With \(\lambda\) fixed, the derivatives are
  \(\partial_x\log w_n=-\lambda\log n/(4x)\), \(\nu'=1/2\) and
  \(\phi'=L_x/2+\pi\lambda/(8x)\). For fixed prefix and regulator,
  \(r\) and its derivative are bounded through zeros of the arm, with
  \(|r|\le\rho<1\). Integrating its \(k\)-th harmonic by parts costs
  \(1/(k\min\phi')\) and pays both endpoints, \(K'\), \(k r^{k-1}r'\),
  and the derivative of \(1/\phi'\). The extra Fourier \(1/k\) makes
  the sum finite. The constants may depend on the fixed prefix and
  regulator. The full population contains the relative phase
  \(\phi-\nu\log(mn)\), whose first derivative for \(m=n=N_x\) can be
  \(O(x^{-1/2})\). The fixed-prefix proof gives no growing-prefix bound.
- **Complete residual.** Jensen applies to the nonnegative transfer
  cost under \(d\mu_X/q_X\), producing the exact factor
  \(q_X\log(1+E_M/(q_X\delta^2))/2\). For positive remaining budget \(h\),
  the strict cap is \(E_M<q_X\delta^2(e^{2h/q_X}-1)\).
  For fixed \(M\) at \(c=1\), subtracting the same prefix at both times
  in the E03 comparison restricts the two-arm sums to \(m,n>M\) and
  preserves the pairwise bounds and Fubini edge estimates. The diagonal
  limit is \(2\sum_{n>M}n^{-3/2}\) before the kernel mass \(1/2\).
  This proves (E04.7) from E03 and rules out a uniformly vanishing
  residual payment in \(X\) for fixed \(M,\delta\). A sufficiently small
  fixed payment within the defect budget is a separate question.

The premise screens in B03 §6 and E04 §4 agree with the controls and
[avoidance guidance][a02]. The Euler-factor controls change the arithmetic
arms and prime subtraction. Weighted-square and finite-prime controls
lose complete unchanged arithmetic with canonical reflection. Reflected,
smooth and primitive-compatible controls lack the ordinary theta/zeta
Dirichlet arithmetic. Finite-profile data do not supply the complete
field, and variable readouts lack the actual cosine/Newman evolution.
The generic phase and logarithm inequalities remain applicable wherever
their own premises hold. The remaining estimate concerns the complete
envelope and actual phase after prime subtraction at every large center,
or a fixed-prefix implementation that pays its full local residual and
still fits the same signed margin. [Continuation][next]

[b03]: ../notes/10_GNP_RS_B03_SIGNED_LOG_ACQUISITION_20261111.md
[e04]: ../notes/11_GNP_RS_E04_REGULARIZED_LOG_TRANSFER_20261111.md
[next]: ../notes/12_GNP_RS_B03_E04_RETURN_AND_MODEL_CHANGE_20261111.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
