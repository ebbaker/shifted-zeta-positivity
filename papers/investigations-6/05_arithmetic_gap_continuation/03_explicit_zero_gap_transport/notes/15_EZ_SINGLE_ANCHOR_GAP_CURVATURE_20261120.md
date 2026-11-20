# Single-anchor gap curvature on a backward time interval

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance. [E09 R1](../research-progress/handoffs/AGC_EZ_E09_REQUEST_R1_20261120.md) records gpt-6.2-astra/ultra lead. This derivation was dispatched to gpt-6.2-sol/ultra. **Proved in-note**, with a [separate internal assessment](../reviews/07_EZ_TIME_CURVATURE_ASSESSMENT_20261120.md). The result is a quantitative estimate on the signed gap remainder from one upper anchor. The relevant measurements are its sign, the error at each partial time, and the time and rank domain. [B06](../brainstorm/notes/07_EZ_B06_ANCHORED_TIME_CURVATURE_20261120.md) · [Result index](../../../../../result-summaries/README.md) · [Patterns index](../../../../../avoid/README.md) · [Target classification](../../../../../avoid/01_restating_the_target.md)

## 1. The jointly tilted Gaussian estimate

Use the saddle at the one upper time \(T\), with \(p_T(u)=Tu^2+9u-\pi e^{4u}\), \(4\pi e^{4L}=2TL+9\), \(\kappa=8TL-2T+36\), \(S=\kappa+2T\) and \(\alpha=2S/(3\kappa^{3/2})\). Define
\[
 W=\sqrt\kappa(U-L),\qquad \lambda=L\sqrt\kappa,\qquad
 r=\tfrac12\sqrt{\log\kappa},\qquad \gamma=2L/\sqrt\kappa,
 \qquad b=\gamma s,
 \qquad y=Lx=\lambda\zeta.
\]
All constants and scales in these definitions stay at the anchor. The physical earlier time is \(t=T-s\). Removing the common nonzero scalar \(e^{-sL^2}\) from the exact tilted source leaves \(e^{-bW-bW^2/(2\lambda)}\) from \(e^{-sU^2}\). Let \(f(w)\) be the unnormalized density in [Note 11 §§1–2](11_EZ_GROWING_INVERSE_WINDOW_20261120.md), extended by zero for \(w<-\lambda\). Define
\[
 a_\pm=-b\pm i\zeta,\qquad A=1+b/\lambda,\qquad v=A^{-1},\qquad
 J_\pm(b,\zeta)=\int_{\mathbb R} f(w)e^{a_\pm w-bw^2/(2\lambda)}\,dw.
\]
Up to the removed scalar and an anchor constant the physical field is \((e^{iy}J_++e^{-iy}J_-)/2\). All bounds below use \(|b|\le3,\ |\zeta|\le r\) and sufficiently large \(T\). The complete source and dominating bounds in the integral give joint holomorphy in the interiors. [Canonical source and inverse](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) · [Direct heat formula](../manuscript/transport.tex)

Let \(g(w)=e^{-w^2/2}/\sqrt{2\pi}\). Note 11 bounds \(f-g(1-\alpha w^3)\) on \(|w|\le w_0=\kappa^{1/12}\) by \(C\kappa^{-1}g(w)(1+w^4+w^6)\). Integrate the model exactly. The Gaussian integral is \(I_\pm=v^{1/2}e^{va_\pm^2/2}\), with the square root continued from \(v=1\). Differentiating it three times in \(a_\pm\) gives the cubic factor \(m_\pm^3+3v m_\pm\), where \(m_\pm=v a_\pm\). For the absolute central error integral complete the real square with Gaussian precision \(\Re A\) and tilt \(\Re a_\pm\). Dividing by \(|I_\pm|\) multiplies its polynomial moment bound \(O(1+(r+3)^6)\) by a bounded square-root factor and by the exponential of
\[
 \frac{(\Re a_\pm)^2}{2\Re A}-\tfrac12\Re(va_\pm^2)
  =\tfrac12(\Im a_\pm)^2+O((r+3)^2/\lambda).
\]
Here \(v=1+O(\lambda^{-1})\), \(\Re A=1+O(\lambda^{-1})\), and \(|a_\pm|\le r+3\). The relative central error is thus \(O(\kappa^{-1}(1+(r+3)^6)e^{(r+3)^2/2+O((r+3)^2/\lambda)})\). Since \((r+3)^2/2=(1/8+o(1))\log\kappa\), this is \(O(\kappa^{-3/4})\).

For \(w\ge-\sqrt\kappa/4\) with \(|w|>w_0\), the source is bounded by \(C e^{-cw^2}\) as in Note 11, and the modulus of the tilt is bounded by \(e^{(r+3)|w|+3w^2/(2\lambda)}\). For sufficiently large \(T\) this still leaves a Gaussian tail with a fixed positive exponent at \(w_0\). The Gaussian model has the same type of bound over its full tails including \(w<-\lambda\). In the remaining source interval \(-\lambda\le w<-\sqrt\kappa/4\), the far-left estimate from Note 11 is \(C e^{-c\kappa}\). Integration against the complex tilt costs at most \(C\lambda e^{(r+3)\lambda+3\lambda/2}\), using the actual left endpoint. The exponent loss is \(o(\kappa)\). Division by \(|I_\pm|\) costs at most \(e^{O((r+3)^2)}\) on these tails. The relative tail errors are smaller than every inverse power of \(\kappa\).

Write \(\eta=\kappa^{-3/4}\). We obtain uniformly
\[
 J_\pm=I_\pm\{1-\alpha(m_\pm^3+3v m_\pm)+O(\eta)\} .            \tag{1}
\]
The perturbation of one is \(O(\alpha(1+r^3)+\eta)=o(1)\). Its square costs \(O(\alpha^2(1+r^6)+\eta^2)=o(\eta)\). Consequently the logarithms defined by the small-disk branch satisfy
\[
 \log J_\pm=\tfrac12\log v+\tfrac12v a_\pm^2
     -\alpha(m_\pm^3+3v m_\pm)+O(\eta).                             \tag{2}
\]
The remainder in (2) is jointly holomorphic and uniformly bounded by \(C\eta\). This uses a Gaussian-relative estimate before the logarithm.

## 2. Invert the counted phase with room for adjacent differences

Define \(\Theta_b(y)=y+(\log J_+-\log J_-)/(2i)\), using \(\zeta=y/\lambda\). The field is a nonvanishing exponential amplitude times \(\cos\Theta_b(y)\) and the common time scalar. The odd Gaussian term in (2) is \(-vb(y/\lambda)\). Since \(1-vb/\lambda=v\), the phase is
\[
 \Theta_b(y)=v y-\alpha\{(3v^3b^2+3v^2)y/\lambda-v^3(y/\lambda)^3\}
                +O(\eta).                                        \tag{3}
\]
Indeed \(m_+^3-m_-^3=2iv^3(3b^2\zeta-\zeta^3)\) and \(m_+-m_-=2iv\zeta\). The remainder is odd in \(y\), since \(J_+\) and \(J_-\) exchange under \(y\mapsto-y\).

In the variable \(p=v y\), the correction to \(p\) in \(\Theta_b(p/v)\) is \(O(\alpha(1+r^3)+\eta)\) on \(|p|\le3\lambda r/4\) by (3). On \(|p|=\lambda r/2\), Rouché gives a unique simple solution of \(\Theta_b(p/v)=q\) for \(|q|\le\lambda r/4\), since \(|p-q|\ge\lambda r/4\). Uniqueness and the implicit theorem give a joint holomorphic inverse \(y=Y_b(q)\) on the open domain and room beyond the retained \(q\)-interval. For real \(b,q\) the inverse is real by conjugation. Cauchy in \(p\) on a disk of radius comparable to \(\lambda r\) gives positive slope \(1+O((\alpha(1+r^3)+\eta)/(\lambda r))\) in the \(p\)-variable on the real interval through the inverses. The factorization and \(\Theta_b(0)=0\) count every positive real zero through \(Y_b(\lambda r/4)/L\). In particular for \(0\le b\le1\) the same simple consecutive pair has positions \(Y_b(q_n)/L,Y_b(q_{n+1})/L\), where \(q_j=(j-\tfrac12)\pi\) and \(q_{n+1}\le\lambda r/8\).

Writing \(p=vY_b(q)\), (3) first gives \(|p-q|=O(\alpha(1+r^3)+\eta)\). Substituting \(q\) for \(p\) on the right of the inverse equation incurs at most \(O((\alpha(1+r^2)/\lambda)(\alpha(1+r^3)+\eta))=o(\eta)\). Replacing \(v\) by one inside the order-\(\alpha\) part of \(Y_b\) costs \(O(\alpha(1+r^3)/\lambda)=o(\eta)\). Therefore, on \(|q|\le\lambda r/4\),
\[
 Y_b(q)=q/v+\alpha\{(3b^2+3)q/\lambda-(q/\lambda)^3\}
                  +R_Y(b,q),\qquad |R_Y|\le C\eta.                \tag{4}
\]
For real \(q\) on the entire retained segment \([0,\lambda r/8]\), Cauchy on disks of radius \(\lambda r/16\) gives \(|\partial_q R_Y|\le C\eta/(\lambda r)\), uniformly for complex \(|b|\le3\). With \(D_* =\pi^2/(4L^2)\), the normalized squared half-gap is \(((Y_b(q_{n+1})-Y_b(q_n))/\pi)^2\). Subtract (4) before squaring to obtain the joint time bound
\[
 \begin{split}
 H_n(b)&:=D_n(T-s)/D_*=P_n(b)+R_n(b),\\
 P_n(b)&=(1+b/\lambda)^2+\frac{2\alpha}{\lambda}
       \left(3b^2+3-\frac{q_{n+1}^3-q_n^3}{\pi\lambda^2}\right),\\
 |R_n(b)|&\le C\eta/\lambda\qquad (|b|\le3).                       \tag{5}
 \end{split}
\]
Here \(H_n\) denotes the normalized gap readout on the complex disk. The omitted cross correction from replacing \(1/v\) by one in the order-\(\alpha\) gap term is \(O(\alpha(1+r^2)/\lambda^2)\), its square is \(O(\alpha^2(1+r^2)^2/\lambda^2)\), and the adjacent remainder is \(O(\eta/(\lambda r))\). All fit (5). In particular the Cauchy savings apply to a shared inverse remainder for both endpoints.

## 3. Curvature and the anchored time tail

For real \(0\le s\le s_*:=\gamma^{-1}=\sqrt\kappa/(2L)\), Cauchy in \(b\) bounds the first two derivatives of \(R_n\) by \(O(\eta/\lambda)\), with constants independent of the pair and partial time. Using \(d/dt=-\gamma\,d/db\) gives
\[
 \begin{split}
 \frac{D_n'(T-s)}{D_*}&=-\frac4\kappa\{1+b/\lambda+6\alpha b+O(\eta)\},\\
 \frac{D_n''(T-s)}{D_*}&=\frac8{\kappa^2}+\frac{32LS}{\kappa^3}
                          +O(L\kappa^{-9/4})
                         \sim\frac{32L}{\kappa^2}.                 \tag{6}
 \end{split}
\]
In the second line the quadratic Gaussian part contributes \(\gamma^2(2/\lambda^2)=8/\kappa^2\), while the cubic source correction contributes \(\gamma^2(12\alpha/\lambda)=32LS/\kappa^3\). Since \(S/\kappa\to1\) and \(L\to\infty\), the curvature is positive. The first derivative is negative uniformly. Use the exact anchor slope \(E_n(T)=D_n'(T)=2-g_n(T)^2M_n(T)\). Integrating the remainder derivative twice, or subtracting the constant and linear terms of \(R_n\), gives
\[
 \frac{D_n(T-s)-D_n(T)+sE_n(T)}{D_*}
      =\left(\frac4{\kappa^2}+\frac{16LS}{\kappa^3}\right)s^2
                   +O(L\kappa^{-9/4}s^2) .                         \tag{7}
\]
This is uniform down to \(s=0\), where both sides of the estimate vanish. For all sufficiently large \(T\) the term on the left is strictly positive at every \(s>0\) in the slab. The backward path has \(D_n(T-s)\ge D_n(T)>D_*/2\), since (5) gives \(D_n(T)/D_*=1+o(1)\). The next right level satisfies \(q_{n+2}\le\lambda r/8+\pi<\lambda r/4\), and the next left level is in the same count or is the reflection of the first positive level. Their distances from the respective nearest endpoints are \((\pi/L)(1+o(1))\) by (4). The count plus this clearance gives a separated two-root chart, for example a circle about the pair midpoint of radius \(g_n\) at each real time. At these large times the full field is all real.

The holomorphic function in (5) has the quadratic part \(P_n\) and the bounded remainder \(R_n\). For each Taylor degree \(m\ge2\) use a Cauchy circle of radius 2 about \(b=0\). In physical units this gives
\[
 \left|\frac{D_n(T-s)-\sum_{j=0}^m(-s)^jD_n^{(j)}(T)/j!}{D_*}\right|
 \le \frac{C\eta}{\lambda}
          \frac{(|b|/2)^{m+1}}{1-|b|/2} \qquad (|b|\le1).          \tag{8}
\]
For degree one, (7) displays the nonzero quadratic contribution and the error that survives at partial time \(s\). The Taylor budget (8) is a joint estimate for the gap readout on a strict time disk. The real interval length \(s_*\sim 2\sqrt{2T/\log T}=o(T)\) ends at a still-large time.

## 4. The complete exterior and finite anchor coefficients

On the separated chart, the [parent split recurrence](../../manuscript/sections/03_hierarchy.tex) identifies the derivatives of the actual gap. In physical time \(D_n'=E_n=2-4D_nM_n\) and \(M_n'=2M_n^2-12P^{(n)}_{2,2}-16D_nP^{(n)}_{3,3}\). In particular, writing \(D=D_n\), \(M=M_n\) and omitting the label on the split moments,
\[
 \dot E_n=-8M+8DM^2+4D(12P_{2,2}+16D P_{3,3}).                      \tag{9}
\]
For higher derivatives one may use the unreduced split recurrence, which raises the maximum total pole order by at most two per differentiation. Thus a Taylor jet through degree \(m\) uses only rows of order at most \(2m\) if generated by differentiating \(D_n'=2-4D_nP_{1,1}\) in that form. The equivalent symmetrized formula (9) uses a row of order six even for degree two. The Cauchy estimate controls the sum of all omitted terms reaching the single scalar gap. Independently enclosing individual evolving rows would require their own analytic estimates.

For the finite jet at \(T\), use the counted head through \(q_K\le\lambda r/4\) with maximum such \(K\), and the endpoints in \(q_{n+1}\le\lambda r/8\). Equation (4) at \(b=0\) gives a lower bound \(R\) on unlocated positive exterior roots and an upper bound \(A_0\) on the targets with \(A_0/R\le2/3\) for all sufficiently large \(T\). The ratio follows by choosing strict margins about the limiting ratio \(1/2\) from the two levels. [Note 09, (1)–(3)](09_EZ_COMPLETE_ANCHOR_FROM_ZERO_FORMULAS_20261120.md) pays for every unlocated exterior pair via the complete radial powers \(U_j\) from the even log-moment coefficients minus the counted head. For a split row of order \(m_r=p+q\) and \(A_0/R<\sigma<1\), keeping radial expansion terms of degrees \(d<J\) leaves error at most
\[
 \frac{2R^{2-m_r}U_1}{(1-\sigma)^{m_r}}
             \left(\frac{A_0}{R\sigma}\right)^J .                 \tag{10}
\]
Each retained degree \(d\) with \(m_r+d\) even uses source moments through order \(m_r+d\). Propagate the actual widths of the radial-power subtractions and the uncertain target factors in each retained coefficient. For a retained head occurrence with position uncertainty \(d_i\), and target position uncertainties \(d_+,d_-\), take positive lower distances \(l_+,l_-\) throughout their input enclosures. Its row uncertainty is bounded by
\[
  \frac{p(d_i+d_+)}{l_+^{p+1}l_-^q}
     +\frac{q(d_i+d_-)}{l_+^p l_-^{q+1}}
\]
by the derivative bounds for the two reciprocal powers. Terms with zero numerator from the two exponents are omitted. The same target enclosures enter every row and the gap. Increase \(J\) or refine the input intervals until the particular finite jet combinations meet their required widths. This evaluation uses anchor coefficients and clearance only.

For example, the dimensionless variables \(L^2D\), \(M/L^2\), \(P_{2,2}/L^4\), \(P_{3,3}/L^6\) are bounded at the anchor by the counted spacing and the radial tail. In their coordinates (9) is a polynomial for \(L^{-2}D_n''\), whose leading size by (6) is \(8\pi^2 L/\lambda^4\). Errors \(O(\lambda^{-6})\) in the scaled variables give \(O(\lambda^{-6})\) error in the polynomial and suffice for its sign. The [finite-source and exterior budget below](#finite-precision-for-the-complete-exterior-at-the-anchor) details sufficient acquisition bounds for these scaled rows. A width assigned to the delivered head positions is a requirement on their enclosure, while uncertainties of raw cumulants propagate through the inverse as in [Note 11 §4](11_EZ_GROWING_INVERSE_WINDOW_20261120.md).

For a general finite Taylor output, let \(d_j\) be an absolute error bound for the normalized coefficient \((-1)^j D_n^{(j)}(T)/(D_*\gamma^j j!)\), including rounding and any scale uncertainty. Add \(\sum_{j=0}^m d_j|b|^j\) to (8). For instance \(\sum_{j=2}^m d_j=O(\eta/\lambda)\) adds at most \(O((\eta/\lambda)b^2)\). For the first two coefficients, absolute errors of order \(D_*\eta/\lambda\) in \(D_n(T)\) and \(D_*\gamma\eta/\lambda\) in \(E_n(T)\) give normalized uncertainties \(O(\eta/\lambda)\). Report those two uncertainties as separate constant and linear terms at each partial time. The signed statement (7) uses the exact shared anchor values. Comparing independently rounded levels to resolve its quadratic increment at an individual \(b>0\) requires \(d_0+d_1|b|\) small compared with \((\alpha/\lambda)b^2\). The complete analytic input in (5) supplies the higher-order envelope beyond the chosen jet degree.

## 5. Equal-input comparison and scope

Direct evolution evaluates the same weighted field from the complete law at \(T\), either as the tilt in §1 or by the full-product heat formula in [the branch manuscript](../manuscript/transport.tex). On the real path the counted phase allows direct signed brackets and satisfies \(\pi=\int_{Y_b(q_n)}^{Y_b(q_{n+1})}\Theta_b'(y)\,dy\). With the same joint disk and the same spatial Cauchy margin applied to (3), this gives the gap expansion at the precision of (5). The exact counted roots are holomorphic in \(b\), so direct use of their shared error on the same time disk also gives (6)–(8). Independent endpoint enclosures instead contribute errors that need not tend to zero with \(s\). The gain in the anchored estimate is its signed, partial-time remainder and its identification with the coupled gap jets from one source, with the same estimates available to direct analytic evaluation.

The [branch current theorem](../manuscript/transport.tex) estimates the drift using source bounds along a large-time interval and a fixed-multiple spatial saddle window. The present proof starts with one law at large \(T\), pays for its time remainder on \([T-s_*,T]\) and uses the growing prefix \(q_{n+1}\le\lambda r/8\). The [spatial sibling, (8)–(11)](../../02_spatial_tensor_zero_spacings/notes/05_AGC_ST_E04_CANONICAL_FORCING_20261120.md) uses the published high labels on a fixed slab \([t_0,t_*]\subset(0,1/2]\), with a direct two-time comparator there. Its slab and the present one are distinct. The curvature sign, partial-time error and rank count are asymptotic at large \(T\). The time onset is unevaluated, and extension to a fixed low time remains open.

The stationary cosine satisfies the general recurrence and has zero curvature. Its atomic source lacks the canonical Gaussian saddle and its tilt has no cubic contribution of the form (1). The atomic \(e^t\cos x+c\) control can have an all-real upper anchor, with loss of simplicity and the separated path at its backward collision. Euler-factor and finite-prime variants alter the complete theta terms. Weighted squares and finite-tail variants with nonreal divisors fail the all-real premise for (10). Reflected and smooth positive-primitive controls lack the full normalized theta square expansion. Fixed-event and finite-profile controls change the complete source or profile and can lack a separated chart at the event. The RH-conditional endpoint control changes ordinary Dirichlet arithmetic. Changed-observation controls fail the literal heat-cosine tilt. The finite-profile relaxation also fails the integer divisor premise. The signs here use the quantitative canonical log expansion and apply to the specified counted paths as long as their disk estimates hold. [Branch control screen](07_EZ_ZERO_FORMULAS_AND_MIXED_HIERARCHY_CONTINUATION_20261120.md) · [Control catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)

## Finite precision for the complete exterior at the anchor

Supplement to B06/E09, 20 November 2026, for Edward Baker. OpenAI Codex lead gpt-6.2-astra/ultra with a separate gpt-6.2-sol/ultra finite-input check. The estimates here pay for obtaining \(D_n(T)\), \(E_n(T)\), and its first derivative from actual head positions and source coefficients. The complex time remainder in the main proof also uses the full canonical source envelope.

Work in \(y=Lx\), set \(\lambda=L\sqrt\kappa\), and let \(\nu_m=\mathbb E_T(U/L)^m\). Retain the largest counted head inside Note 11's prefix; its last \(y\) is comparable to \(K\asymp\lambda r\). (Here \(K\) is the number of positive roots.) For the target \(q_{n+1}\le\lambda r/8\), one may use an outer lower radius \(R\asymp K\) from the last head zero and an endpoint allowance \(A\) with \(z=A/R\le2/3\) eventually. Choose \(\sigma=5/6\). In the notation of [Note 09, (1)–(2)](09_EZ_COMPLETE_ANCHOR_FROM_ZERO_FORMULAS_20261120.md), for \(m=p+q\in\{2,4,6\}\) take \(H=\lceil C\log\lambda\rceil\) with \(((2/3)/\sigma)^H\le\lambda^{-6}\). The omitted radial tail in each normalized row is \(O(\lambda^{-6})\), since \(R^{2-m}\le1\) eventually and \(U_1\le\nu_2/2=O(1)\). The required radial source moment orders are at most \(H+5\).

The retained \(U_j\) subtract known head powers from the full log-product coefficient. Put \(J=\lfloor(H+5)/2\rfloor\). On \(|v|\le1\), check that \(\sum_{j=1}^J \overline{\nu}_{2j}/(2j)!<3/4\) or use any fixed upper bound less than one with strict clearance for the input errors. This holds eventually since \(\mathbb E\cosh(U/L)\to\cosh 1\) by the same weighted saddle bounds. An error \(\delta\) in the sum of the radii of the normalized coefficients perturbs the logarithm of the truncated cosine polynomial by \(O(\delta)\) on this disk. Cauchy and the factor \(-j\) in the radial trace then cost \(O(j\delta)\) in each power sum. For head positions with maximum radius \(\eta_{\rm pos}\) in \(y\), \(y_i-\eta_{\rm pos}\ge i\) eventually, and the summed error of the \(2j\)-th inverse powers is \(O(j\eta_{\rm pos})\). This charges the subtraction even when its result is much smaller than either operand. With \(|h_d|\le{m+d-1\choose d}A^d\) in Note 09, summing the propagated errors for \(d<H\) costs at most
\[
 O\big((\delta+\eta_{\rm pos})H^7\max(1,A)^H\big).
\]
The uncertainty in the marked endpoints entering \(h_d\) costs \(O(\eta_{\rm pos})\) when the true \(U_j\) are held fixed: differentiate the convergent tail expansion with its fixed radial clearance; the absolute derivative sums are bounded by the corresponding convergent geometric series. The finite exterior head likewise costs \(O(\eta_{\rm pos})\), using separated head spacings and summable reciprocal products. The preceding error bound for \(\delta U_j\) can then be used with the *upper* endpoint bound \(A\). It suffices that \(\delta,\eta_{\rm pos}\ll\lambda^{-6}/(H^7\max(1,A)^H)\). This is \(O(\log^2\lambda)\) sufficient absolute bits in these scaled data. Since \(g_y=L g\asymp1\), the error in \(E=2-g_y^2 M_y\) is \(O(\lambda^{-6})\). The quantity \(L^{-2}D''\) is a polynomial in \(D_y=L^2D\) and the dimensionless rows of orders 2, 4 and 6, bounded on these data. Its error is \(O(\lambda^{-6})\), smaller than its signal of order \(L/\lambda^4\). For finite \(T\) the inequalities must be checked with their actual enclosures.

Head positions can themselves be obtained to this precision from the full odd phase. In \(y\) its linear coefficient is \(a/L\) and the holomorphic odd correction has bound \(M\) on \(|y|\le\lambda r\) as in [Note 11](11_EZ_GROWING_INVERSE_WINDOW_20261120.md). On \(X=\lambda r/2\) the Taylor tail after degree \(P\) is \(O(M2^{-P})\). Choose \(P=O(\log^2\lambda)\) to make this much smaller than \(\eta_{\rm pos}\). The coefficients through \(P\) come from the logarithm of the truncated series of \(\mathbb E e^{vU/L}\). Check that \(\sum_{m=1}^P\overline\nu_m(1/4)^m/m!<1/2\), valid eventually since the full positive sum tends to \(e^{1/4}-1\). If the supplied coefficients have total radius \(\delta_{\rm head}\) weighted at \(1/4\), Cauchy on that circle bounds the \(m\)-th log coefficient error by \(O(4^m\delta_{\rm head})\). Thus \(\delta_{\rm head}\ll\eta_{\rm pos}(4X)^{-P}\) suffices for \(O(\eta_{\rm pos})\) phase error on \(|y|\le X\). The counted head lies strictly inside and the real phase slope is bounded below, converting the phase error into \(O(\eta_{\rm pos})\) positional errors. This gives a conservative complete acquisition budget of moment order \(O(\log^2\lambda)\) and \(O(\log^3\lambda)\) absolute bits in the stated weighted coefficient norm. The direct phase calculation can use these same data. These estimates price the anchor input, with no measured running time or evaluated onset.
