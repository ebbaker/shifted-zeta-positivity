# What the inverse formula tells us about zero positions

20 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance. The desktop chat records gpt-6.2-astra with reasoning effort max. [Public discussion](../../chat-histories/0003_2026-11-20T17-34-48Z_explain-the-inverse-formula-cutoff.json)

In \(H(T,x)\), \(T\) is heat time and \(x_k(T)\) is the height of the \(k\)-th positive zero. The starting question is what determines the displacement of \(x_k\) from an equally spaced sequence. The inverse series answers it by expressing the phase of an integral in terms of the shape of its source. [Founding calculation, §§3–5](../../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md)

## What moves a zero?

Write \(f_T(u)=e^{Tu^2}\Phi(u)\) and let \(U\) have density \(f_T(u)/H_T(0)\) on the positive half-line. The complex transform
\[
B_T(x)=\int_0^\infty f_T(u)e^{ixu}\,du=H_T(x)+iS_T(x)
\]
starts on the positive real axis. The physical field \(H_T\) vanishes whenever \(B_T\) meets the imaginary axis. Write \(\Theta_T(x)=\arg B_T(x)\), choosing \(\Theta_T(0)=0\) and following the angle continuously while \(B_T\ne0\). Where this angle increases from zero, its successive axis crossings occur at \(q_k=(k-\tfrac12)\pi\). With \(a=\mathbb E_T U\) the inverse series gives the corresponding positions in scaled coordinates, \(Y(q_k)=a x_k\). [Manuscript, phase and counted inverse](../../manuscript/anchors.tex)

Let \(\gamma_j\) be the cumulants of \(U\). On the disk of the logarithm, the real and imaginary parts of \(\log\mathbb E_T e^{ixU}\) give
\[
\frac{H_T(x)}{H_T(0)}
=\exp\!\left(-\frac{\gamma_2x^2}{2!}+\frac{\gamma_4x^4}{4!}-\cdots\right)
 \cos\!\left(ax-\frac{\gamma_3x^3}{3!}+\frac{\gamma_5x^5}{5!}-\cdots\right).
\]
The even cumulants set a positive amplitude on the real interval. The mean sets the spacing of the leading cosine, and the odd cumulants beyond the mean move its crossings. In particular, \(c_1=\gamma_3/(6a^3)\) measures the first effect of asymmetry on the positions. [Founding calculation, §3](../../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md)

One can read a geometric consequence directly from the series. If only the mean entered, \(x_k=(2k-1)x_1\). Forming the ratio cancels the common scale \(1/a\). For fixed \(k\ge2\), the founding large-\(T\) estimate on the higher terms gives
\[
1-\frac{x_k}{(2k-1)x_1}
=-c_1(q_k^2-q_1^2)+o(|c_1|)
=-c_1\pi^2 k(k-1)+o(|c_1|).
\]
The heated source has \(\gamma_3<0\) for sufficiently large \(T\). Thus the second zero falls slightly *inside* three times the first, and every fixed higher zero falls inside its corresponding odd multiple once \(T\) is large enough for that rank. The sign comes from the asymmetry of the source. [Analytical derivation of the sign and the fixed-rank law, §5](../../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md)

## How the explicit series was resummed

Writing \(y=ax\) and \(\Psi(y)=c_1y^3+c_2y^5+c_3y^7+\cdots\), the phase equation is \(Y(q)=q+\Psi(Y(q))\). Lagrange inversion gives an explicit coefficient at every order. The manuscript proves absolute convergence for \(|q|<Q\) under its disk test, even after expanding each coefficient into individual terms. This allows those terms to be summed in a different order. [Original series, §3 and (3)](../../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) · [Counted inverse theorem](../../manuscript/anchors.tex) · [Lagrange inversion](https://dlmf.nist.gov/1.10.vii)

Collecting every term that uses \(c_1\) alone gives the inverse of the cubic phase,
\[
Y_3(q)=q+c_1q^3+3c_1^2q^5+12c_1^3q^7+\cdots,\qquad
Y_3(q)-c_1Y_3(q)^3=q .
\]
For \(h=-c_1>0\), as holds at sufficiently large \(T\), the branch through zero has the closed form
\[
Y_3(q)=\frac{2}{\sqrt{3h}}\sinh\!\left(\frac13\operatorname{arsinh}
\!\left(\frac{3\sqrt{3h}}2q\right)\right).
\]
At order \(q^5\), the coefficient \(3c_1^2\) is already in this sum, and \(c_2\) brings in the fifth cumulant. At order \(q^7\), \(12c_1^3\) is already included, and the additional contribution is \(8c_1c_2+c_3\). [Founding calculation, §4](../../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md)

The higher terms also have an exact regrouping. With \(I(y)=c_2y^5+c_3y^7+\cdots\), the result on the proved disk is
\[
Y(q)=Y_3(q)+\sum_{m\ge1}\frac{1}{m!}
  \frac{d^{m-1}}{dq^{m-1}}\!\left[Y_3'(q)\,I(Y_3(q))^m\right].
\]
Here \(m\) counts factors from \(I\) while each term keeps the cubic summed. Keeping every correction recovers \(Y\). At fixed finite \(T\), the founding note rules out an algebraic closed form for the full continuous \(Y\) by excluding every nonzero polynomial relation \(P(q,Y(q))=0\) near \(q=0\). A transcendental closed form or an expression specific to the discrete \(q_k\) remains possible. [Exact regrouping (4) and the scope of the algebraic obstruction, §7](../../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md)

## Following the same field to large height

At each fixed \(T\), integrating the half-line transform twice by parts gives
\[
B_T(x)=\frac{i\Phi(0)}{x}+O_T(x^{-2}) \qquad (x\to+\infty).
\]
The endpoint \(u=0\) supplies the leading term. It is purely imaginary, so it sets the direction of \(B_T\) while contributing zero to the observable \(H_T=\Re B_T\). The transform eventually stays in the upper half-plane and its angle tends to \(\pi/2\) modulo \(2\pi\). Every sufficiently high real zero is a return to the **same** angle on that continuous tail branch. Between consecutive such zeros Rolle's theorem gives a point where the phase derivative vanishes. This restricts counting by successive levels of this particular half-line argument even if its inverse has been summed exactly on its initial branch. [Note 04, fixed-time endpoint proof and scope](../../notes/04_EZ_HALF_LINE_PHASE_OBSTRUCTION_20261120.md)

The high-zero formula can be related to this observation at the level of the field itself. In Polymath's fixed-time range \(0<t\le1/2\), let \(P_t(x)=M_t((1+ix)/2)\) in the paper's notation and write \(\phi_t=\arg P_t\). Proposition 9.1(i) expresses \(H_t\) on the high real axis as the sum of \(P_t\) and its conjugate with error \(O(|P_t|x^{-ct})\), for some \(c>0\). Since \(H_t/S_t=\cot\Theta_t\) where \(S_t>0\), combining the two formulas gives
\[
\cot\Theta_t(x)
=\frac{2|P_t(x)|}{S_t(x)}
  \bigl(\cos\phi_t(x)+O(x^{-ct})\bigr).
\]
At each high zero the left side returns to zero. On the right the phase of \(P_t\) comes successively close to the odd multiples of \(\pi/2\), and the error relative to its amplitude shrinks. At the zero near a counted clock center \(u_j\), the proof after (104) bounds the sine of \((x-u_j)\log(u_j/(4\pi))/4\) by \(O(u_j^{-ct})\). One spacing corresponds asymptotically to phase advance \(\pi\). This gives a positional error tending to zero even in units of the local spacing. At \(t=1/2\) Note 13 identifies these clock labels with the actual high ranks. The displayed relation concerns the fixed-time high tail. Matching to the growing-\(T\) inverse over a common range remains open. [Polymath, Proposition 9.1, Lemma 9.2 and (104)](https://arxiv.org/html/1904.12438v2#S9) · [Note 13, rank identification](../../notes/13_EZ_CLOCK_RANK_20261120.md)

For further work on resummation the analytic question is where the origin branch first loses regularity, and what happens to the zero labels there. On any regular real segment the exact inverse slope is
\[
\frac{dx}{dq}=\frac{|B_T(x)|^2}
                   {\Im(\overline{B_T(x)}\,B_T'(x))},
\qquad q=\Theta_T(x).
\]
A zero of \(B_T\) makes its angle undefined. At a stationary angle with \(B_T\ne0\) the analytic local inverse fails. Complex singularities may already limit the Taylor series about zero before either event occurs on the real axis. The source integral and this derivative give concrete objects to study when asking how far a resummation can carry a given branch. [Manuscript, phase current](../../manuscript/current.tex) · [Note 04](../../notes/04_EZ_HALF_LINE_PHASE_OBSTRUCTION_20261120.md) · [Result index](../../../../../../result-summaries/README.md) · [Heat-flow cluster](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md) · [Patterns index](../../../../../../avoid/README.md) · [Structural questions before numerical work](../../../../../../avoid/10_numerics_ahead_of_the_question.md)

## Where \(K(T)\) comes from

The founding estimate covers \(q_k\le C a\sqrt\kappa\) for each fixed \(C>0\) once \(T\) is sufficiently large depending on \(C\). Note 11 lets \(C=\sqrt{\log\kappa}/8\) grow with \(T\) and bounds adjacent gaps on the resulting interval. [Founding range, §4](../../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) · [Growing range, §3](../../notes/11_EZ_GROWING_INVERSE_WINDOW_20261120.md)

The source concentrates near its mean with width about \(1/\sqrt\kappa\). Across one source width, the angle \(xU\) varies by about \(x/\sqrt\kappa\). Increasing \(T\) narrows the source, while increasing \(x\) at a fixed \(T\) spreads the angles farther apart. The Gaussian approximation has amplitude \(e^{-x^2/(2\kappa)}\), and controlling its phase requires an error bound relative to that amplitude. [Note 11, §1](../../notes/11_EZ_GROWING_INVERSE_WINDOW_20261120.md)

Put \(D=a\sqrt{\kappa\log\kappa}/2\). For sufficiently large \(T\), the proof constructs the exact inverse on \(|q|<Q\) with \(Q\ge 3D/8\). It states the joint position and adjacent-gap estimates on the smaller interval \(q\le D/4\), keeping \(q/Q\le 2/3\). For a gap both endpoints must fit. The last rank in this interval is
\[
K(T)=\left\lfloor \frac{a\sqrt{\kappa\log\kappa}}{8\pi}+\frac12\right\rfloor .
\]
The choice of \(K(T)\) comes from leaving room inside the inverse disk to bound positions and gaps together. The actual cubic errors at ranks \(K(T)\) and \(K(T)+1\) could occur in either order as far as this estimate is concerned. Inside the stated range the upper bound on position error is \((E/a)(q_k/Q)^5\), where \(E\) bounds the phase approximation. At fixed \(T\), the *allowed* error grows with \(k\) throughout the range. The measured error at an individual zero can be much smaller. As \(T\to\infty\), even the largest bound in the interval tends to zero, while \(K(T)\sim(\sqrt2/(32\pi))\sqrt T(\log T)^2\). An individual fixed-rank zero has height \(x_k(T)\sim 4q_k/\log T\), while the height of the *last included* zero grows like \((\sqrt2/8)\sqrt T\log T\). [Note 11, §3, equations (4)–(6)](../../notes/11_EZ_GROWING_INVERSE_WINDOW_20261120.md)

The number of terms and the number of zeros enter different estimates. For exact input coefficients, keeping the Taylor series through \(q^{2N+1}\) gives position error at most \((B/a)s^{2N+3}/(1-s^2)\), where \(s=q_k/Q\) and \(B\) bounds \(|Y(q)-q|\) on the inverse disk. The stated range \(k\le K(T)\) ensures \(s\le 2/3\). Increasing \(N\) at the same \(k\) tightens the truncation bound. Extending the rank range requires control of the phase and the zero count farther from the origin. [Note 11, §§3–4](../../notes/11_EZ_GROWING_INVERSE_WINDOW_20261120.md)

## Finite illustration

At \(T=1000\) the recorded mean is \(a\approx1.34153249\) and \(q_{40}/(a\sqrt\kappa)\approx0.98771976\). Substitution gives \(15.56246\ldots\) inside the floor, hence a nominal cutoff of 15. Applying the large-time error theorem at this particular \(T\) would also require its finite tests. A separate calculation counts zero 40 directly at \(x_{40}\approx92.49456\). The recorded absolute cubic errors are about \(2.08\times10^{-15}\) at zero 1 and \(6.39\times10^{-6}\) at zero 40. For that same fortieth zero the polynomial through \(q^7\), including \(c_2\) and \(c_3\), has absolute position error about \(3.99\times10^{-11}\). The finite check at 40 uses a direct bracket and a real-phase count. The complex-disk test in that calculation establishes convergence of the infinite series for the first two ranks. [Finite test and count, §6](../../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) · [Recorded intervals](../../../01_jacobi_integer_hierarchy/numerics/08_LARGE_TIME_LOOP_RESUMMATION_20261120.json)

At \(T=1000\), the question in Note 16 is where a fixed-time high-zero estimate becomes effective and whether it overlaps an independently counted range. [Note 16, overlap question](../../notes/16_EZ_ASSESSED_ANCHOR_CONTINUATION_20261120.md)
