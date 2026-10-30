# Adaptive radius, a separate analytic neighborhood, and phase-aligned integration by parts

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **max**, existing Investigation05 **chat0048**, *Continue FCG-B03 research*. **FCG-B03 R5**, following the author's adaptive-radius and integration-by-parts suggestions, [Note25][intake] and accepted [Assessment08][assessment]. [Progress06][progress] alone owns live status.

**Return.** Register **C04 R3**, retaining the quadratic row but separating the certified radius from its larger analytic neighborhood and replacing its derivative envelope by a complete-source IBP bound when smaller. Shrinking the inner ball weakly lowers the minimum degree required by this exact bound. A nonzero center discriminant gives an explicit positive radius at **degree one**. The phase-aligned source cutoff has a paid boundary and complete exterior, uniformly for complex parameters. These are proved-in-note sufficient estimates and local certification results, not an RH-equivalent definition or a new theta nonvanishing region.

One finite comparison is [issued to E01 R2/Sol][packet]: a new, fixed center, three nested radii, four degrees and matched information. No source values, numerical code, root search or scan were acquired in this B turn. A second source calculation below records what the theta primitive does to the *complete correlated remainder*, including its boundary cancellation. It is not silently substituted for the selected executable envelope. [Self-assessment09][self] is by the proof author only.

## 1. Fixed physical family and two different radii

Keep the complete source and observation
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
 \qquad H(T,A)=\int_0^\infty e^{Tu^2}\Phi(u)\cos(Au)\,du.
 \tag{1}
\]
Write \(t=T-\tau,x=A-a\), \(h_j=\partial_A^jH(\tau,a)\), \(b=h_2\),
\[
 P=h_0+h_1x+b(x^2/2-t),\quad D_0=h_1^2-2bh_0,
\]
\[
 G=-2b(H-P)+(h_1+bx)(H_A-P_A),\qquad
 (-2b,h_1+bx)\cdot(H,H_A)=D_0+2b^2t+G.
 \tag{2}
\]
These are exactly the complete-source definitions of [Note16][n16]. Its signed Taylor coefficients \(g_{mn}\) are retained, including
\(g_{00}=g_{01}=0\) and \(g_{10}=-h_1h_3\).

Now choose a real **outer analytic radius** \(R>0\) and an **inner certified radius**
\[
 0<r\le R/2,\qquad r<\tau,
 \tag{3}
\]
independently. The outer bidisk is \(|t|,|x|\le R\); the real radius-\(r\) ball lies in its inner rectangle. There is no requirement to reset \(R=2r\) when shrinking \(r\). All quantities at the center and the outer derivative envelope can be reused.

The spatial family is unchanged: \(W_c=(U,U_A)\),
\(\partial_sW_c=\Delta_XW_c+c\operatorname{div}_X(vW_c)\),
\(v=X+X/(1+|X|^2)\) on all \(\mathbb R^3\), with Note16's full radial source and unit Gaussian preparation. The scalar \(c\) remains constant on each certified parameter region. A source cutoff below is an integration device in \(u\), not a spatial boundary condition or a truncated physical source.

## 2. Uniform complex derivative bounds from IBP

Assume \(a>R\). Put \(f(u)=e^{\tau u^2}\Phi(u)\), and for \(j=3,4\) define
\[
 f_j^+(u)=u^j e^{Ru^2}f(u),\qquad
 D_j(u)=(u^jf(u))',
\]
\[
 B_j(u)=e^{Ru^2}\bigl(|D_j(u)|+2R u^{j+1}f(u)\bigr).
 \tag{4}
\]
The complete signed derivative \(D_j\) is formed **before** the absolute value. All integrals below are finite by the complete theta decay and its differentiated majorants accepted in Note24. For \(|t|\le R\),
\[
 |u^je^{(\tau+t)u^2}\Phi(u)|\le f_j^+(u),\qquad
 |(u^je^{(\tau+t)u^2}\Phi(u))'|\le B_j(u).
 \tag{5}
\]
The second formula follows by differentiating \(e^{tu^2}u^jf\); it keeps the real-center derivative cancellation inside \(D_j\).

Let \(\phi_j=j\pi/2\). Integration by parts for the complex frequency \(A=a+x\) gives
\[
 \partial_A^jH(\tau+t,A)
 =-\frac1A\int_0^\infty
 (u^je^{(\tau+t)u^2}\Phi(u))'\sin(Au+\phi_j)\,du.
 \tag{6}
\]
At infinity the full differentiated source dominates every allowed factor. At zero the factor \(u^j\) vanishes for \(j=3,4\). Also \(|A|\ge a-R>0\); no physical jet is divided by. Therefore two explicit bounds on the whole bidisk are
\[
 M_j=\int_0^\infty f_j^+(u)e^{Ru}\,du,
 \qquad I_j=\frac1{a-R}\int_0^\infty B_j(u)e^{Ru}\,du.
 \tag{7}
\]
For fixed \(\tau,R\), the integral in \(I_j\) is independent of \(a\). Thus this is a genuine complete-source complex derivative envelope with a \(1/(a-R)\) gain, not a named unknown supremum. In particular \(I_j<M_j\) whenever
\(a>R+(\int B_je^{Ru})/M_j\). The cutoff is source-defined and unevaluated. This upper-bound improvement alone proves neither a discriminant lower bound nor efficient global coverage.

### A phase-aligned finite boundary

Fix \(U_j>0\) using the **center** frequency, so
\[
 aU_j+\phi_j=k_j\pi,\qquad k_j\in\mathbb Z.
 \tag{8}
\]
The cutoff stays fixed as \((t,x)\) ranges over the bidisk. Set
\[
 S_j(u)=|\sin(au+\phi_j)|\cosh(Ru)
       +|\cos(au+\phi_j)|\sinh(Ru),
\]
\[
 C_j(u)=|\cos(au+\phi_j)|\cosh(Ru)
       +|\sin(au+\phi_j)|\sinh(Ru).
 \tag{9}
\]
For complex \(|x|\le R\), power-series bounds \(|\cos(xu)|\le\cosh(Ru)\),
\(|\sin(xu)|\le\sinh(Ru)\) give the corresponding bounds on the sine and cosine of \((a+x)u+\phi_j\). Both (9) are at most \(e^{Ru}\).

Integrating by parts only on \([0,U_j]\), leaving the exterior in its original form, gives the exact identity
\[
 H_j=\frac{u^je^{(\tau+t)u^2}\Phi(u)\sin(Au+\phi_j)}A\Big|_{u=U_j}
 -\frac1A\int_0^{U_j}(u^je^{(\tau+t)u^2}\Phi)'\sin(Au+\phi_j)\,du
 +\int_{U_j}^\infty u^je^{(\tau+t)u^2}\Phi\cos(Au+\phi_j)\,du.
 \tag{10}
\]
Here \(H_j=\partial_A^jH\). Although the finite boundary vanishes at \(x=0\), it generally does **not** vanish on the bidisk. Its uniform payment is \(f_j^+(U_j)\sinh(RU_j)/(a-R)\). Consequently another complete bound is
\[
 W_j=\frac{f_j^+(U_j)\sinh(RU_j)+\int_0^{U_j}B_jS_j\,du}{a-R}
            +\int_{U_j}^\infty f_j^+C_j\,du.
 \tag{11}
\]
Use
\[
 \boxed{\mathcal U_j=\min\{M_j,I_j,W_j\},\qquad j=3,4.} \tag{12}
\]
Every entry bounds the same fully summed complex derivative on the same bidisk. Taking their minimum preserves validity and cannot worsen the original fixed-\(R\) moment bound. A strict improvement in the actual coefficient remains a question about which term dominates. The finite boundary and infinite exterior in (11) must both be paid.

## 3. The adaptive C04 R3 coefficient

For any valid bounds \(U_3,U_4\) on this bidisk, define
\[
 e_0(z)=(z^3/6+z^2)U_3+(z^2/2)U_4,
 \qquad e_1(z)=(z+z^2/2)U_3,
\]
\[
 M_G(R;U)=2|b|e_0(R)+(|h_1|+R|b|)e_1(R).
 \tag{13}
\]
The same complex Taylor paths as Note16 give \(|G|\le M_G\) on the outer bidisk. With \(q=r/R\), Cauchy's bound gives the exact total-degree tail factor
\[
 T_N(q)=\sum_{k>N}(k+1)q^k
       =\frac{q^{N+1}((N+2)-(N+1)q)}{(1-q)^2}.
 \tag{14}
\]
Thus define, before any sign is known,
\[
 \Gamma_N(r;R,U)=\sum_{1\le m+n\le N}|g_{mn}|r^{m+n}
                       +M_G(R;U)T_N(r/R),
\]
\[
 d_N(r;R,U)=|D_0|-2b^2r-\Gamma_N(r;R,U),\qquad
 c_N=\frac{d_N}{1+h_0^2+h_1^2+b^2}.
 \tag{15}
\]
The selected R3 version uses (12). The unchanged R2 definition is recovered at \(R=2r,U_j=M_j(2r)\), because \(T_N(1/2)=(N+3)/2^N\). This is a new coefficient revision, not a reinterpretation of the accepted old certificate.

If \(d_N>0\), the exact row identity gives
\[
 |(H,H_A)|\ge\mu:=\frac{d_N}{\sqrt{4b^2+(|h_1|+r|b|)^2}}>0.
 \tag{16}
\]
The denominator cannot vanish under that premise. With precisely the coefficient \(c_N>0\), Note16's scalar carrier gives the same all-time spatial floor, with
\[
 L=\int_0^\infty e^{(\tau+r)u^2}\Phi(1+u)\,du,\quad
 R_2=\int_0^\infty e^{(\tau+r)u^2+4u}\Phi(1+u)\,du,
\]
\[
 \overline N=\max\{R_2+6L,3L/c_N\},\quad
 E_{c_N}(s;p)\ge\frac{3\mu^2}{16\pi}
                  \left(\frac{\mu}{2\overline N}\right)^{3/2}>0.
 \tag{17}
\]
This retains unit preparation, all spatial tails and \(s\ge0\). The flow does not improve the source margin.

### Radius and degree monotonicity

Hold the center, \(R\) and \(U_j\) fixed. Every term of \(\Gamma_N\) is nondecreasing in \(r\), as is \(2b^2r\); hence shrinking \(r\) cannot decrease \(d_N\). Also
\[
 \Gamma_N-\Gamma_{N+1}
 =M_G(N+2)q^{N+1}
       -r^{N+1}\sum_{m+n=N+1}|g_{mn}|\ge0
 \tag{18}
\]
by the same Cauchy bounds. Therefore increasing degree cannot worsen the *exact* margin, and the smallest successful degree weakly decreases as the inner radius shrinks. Interval implementations may have additional enclosure loss; exact monotonicity must not be confused with monotonic rounded outputs.

At fixed \(R\), the uncomputed tail is \(O(r^{N+1})\). In the earlier coupled choice \(R=2r\), its geometric factor stayed constant as \(r\) changed, while \(M_G(2r)\) supplied the smallness. Separating the radii makes this additional geometric reduction available; it does not guarantee superiority at every chosen radius.

### An explicit degree-one radius

Let \(D=|D_0|>0\), \(L_0=2b^2+|h_1h_3|\), and \(M=M_G(R;U)\). For \(q\le1/2\),
\[
 T_1(q)=\frac{q^2(3-2q)}{(1-q)^2}\le8q^2,
 \qquad d_1\ge D-L_0r-8M(r/R)^2.
\]
Choose the fully source-defined radius
\[
 \boxed{r_*=min\left\{\frac R2,\frac\tau2,
          \frac D{4(1+L_0)},\ R\sqrt{\frac D{32(1+M)}}\right\}.}
 \tag{19}
\]
Then \(r_*>0\) and every \(0<r\le r_*\) has \(d_1\ge D/2>0\). The added ones merely avoid zero denominators. This uses the explicit center discriminant, not an unknown minimum over a region. If \(D_0=0\), this coefficient fails for every radius; a nonzero physical jet can still have \(D_0=0\).

For the Gaussian example in Note22, \(D_0\ne0\) except at \(y=2\), so degree one succeeds on some adaptive radius at every other center. Its independent time constraint scales as
\(r<q_0|2-y|/(y-1)^2\sim2q_0^2/a^2\), where \(q_0=\beta-\tau\). Formula (19) can be much smaller because it also pays the tail. This explicitly separates local feasibility from an efficient covering of high frequencies. No suitable theta radius schedule, uniform center-discriminant lower bound or global coverage has been proved.

## 4. What the positive theta primitive does to the full remainder

The earlier [primitive identity][primitive] is
\(\Phi=(\psi''-\psi)/8\), with
\(\psi=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}}\), \(\psi'(0)=-1/2\).
Rather than separately reconstructing \(H\) and \(H_A\), form their residual kernel first:
\[
 \mathscr R=e^{\tau u^2}\left[e^{tu^2}\cos((a+x)u)-\cos(au)
       +xu\sin(au)+(x^2/2-t)u^2\cos(au)\right],
\]
\[
 \mathscr K=-2b\mathscr R+(h_1+bx)\partial_x\mathscr R,
 \qquad G=\int_0^\infty\Phi(u)\mathscr K(u)\,du.
 \tag{20}
\]
The constant and quadratic terms in the Taylor expansion in \(u\) cancel exactly: \(\mathscr R,\partial_x\mathscr R=O(u^4)\). In particular \(\mathscr K(0)=\mathscr K'(0)=0\). Two integrations by parts therefore yield
\[
 \boxed{G=\frac18\int_0^\infty\psi(u)(\mathscr K''-\mathscr K)\,du.}
 \tag{21}
\]
There is **no lower endpoint constant** for this combined remainder, although the reconstruction of \(H\) alone has its essential \(1/16\). This cancellation occurs before estimation and does not discard a term.

On a finite source interval the exact formula is instead
\[
 G=\frac{\psi'(U)\mathscr K(U)-\psi(U)\mathscr K'(U)}8
   +\frac18\int_0^U\psi(\mathscr K''-\mathscr K)\,du
   +\int_U^\infty\Phi\mathscr K\,du.
 \tag{22}
\]
Choosing \(aU=k\pi\) does not cancel this whole boundary. For example at \(x=0\),
\(\mathscr R(U)=(-1)^ke^{\tau U^2}(e^{tU^2}-1-tU^2)\), generally nonzero. Frequency derivatives in \(\mathscr K'\) also survive. A bound based on (22) must retain their joint expression and the complete exterior; no improved bound from (22) is claimed here. The executable choice (11) instead uses a sine-zero boundary for each of the two derivative envelopes and explicitly pays its complex-neighborhood variation.

A boundary moving with the actual parameter \(A\) would require Leibniz terms when differentiating the core and exterior; the two pieces compensate only when both are retained. Freezing the boundary at the center as in (8) avoids that extra derivative bookkeeping.

There is also a simple limitation of keeping only a fixed number of favorable cosine lobes. If \(U(a)=K/a\) for fixed \(K\), then \(\int_0^{U(a)}f\to0\), while \(\int_{U(a)}^\infty f\to\int_0^\infty f>0\). A scalar lower bound obtained by paying the exterior by its whole positive mass is at most \(2\int_0^{U(a)}f-\int_0^\infty f\), eventually negative. This rejects only that scalar, absolute-exterior rule. It does not reject the complete remainder (22), signed exterior estimates or phase-aligned cutoffs near a fixed positive source radius. The earlier [localization loss][localization] has a related, separately scoped warning.

## 5. Matched comparison and the finite question

The exact direct first-jet consumer receives the same row and \(\Gamma_N\); its strip distance is
\((|D_0+2b^2t|-\Gamma_N)_+/|(-2b,h_1+bx)|\) when the row is nonzero. It is at least as strong as (16). Any gain here comes from a smaller acquired source allowance or a radius/degree tradeoff, not from the spatial flow.

The same information supplies scalar comparison floors
\[
 |H|\ge |h_0|-r|h_1|-|b|(r+r^2/2)-e_0(r),\qquad
 |H_A|\ge|h_1|-r|b|-e_1(r).
 \tag{23}
\]
These may already explain a successful small ball. For C01, use
\(B_2=|b|+r(U_3+U_4)\) and \(C=1+B_2/\mu\) when \(\mu>0\).
Then the inherited argument gives \(\mathcal L+C|J|^2\ge|J|^2\), followed by eventual spatial C01 positivity at \(c=1\) with its accepted uniform derivative-convergence dependency. No start time is acquired by that comparison.

Freeze, **before testing**, the single new center and outer neighborhood
\[
 \tau=1/4,\quad a=64,\quad R=1/32,
\]
\[
 r\in\{1/64,1/128,1/256\},\quad N\in\{1,2,4,8\},
 \quad U_3=41\pi/128,\quad U_4=21\pi/64.
 \tag{24}
\]
Indeed \(64U_3+3\pi/2=22\pi\), \(64U_4+2\pi=23\pi\), and both cutoffs are at least one. The center is a declared dyadic test point; it was not selected from a theta evaluation or root bracket.

Compare (A) the old coupled moment allowance at \(R=2r\), (B) the separate fixed-\(R\) moment allowance, and (C) the fixed-\(R\) IBP minimum (12). Use identical acquired center jets and all complete source information for the direct/C01 comparisons. The question is **which paid error allowances and minimum passing degrees improve on these fixed radii**, not whether another positive example supports RH. Also report (19) for B/C if the center discriminant is certified nonzero; a downward-rounded radius obtained by that predeclared formula is explicitly data-derived, not an a-priori fixed-ball success.

The [frozen packet][packet] fixes all inputs, quadrature/panel limits, precisions and stops. A rigorous improvement, no improvement, exact rejection or unresolved return can complete the comparison. No new frequency, arbitrary radius search or degree beyond eight is permitted. No numerical result is claimed in this note.

## 6. Complete tails and controls

For implementation, every component needed to majorize \(\Phi\) or \(\Phi'\) has form
\(C\lambda_n^p e^{q_0u-\lambda_ne^{4u}}\), \(\lambda_n=\pi n^2\), with
\[
 (C,p,q_0)=(2,2,9),\quad(30,2,9),(15,1,5),(8,3,13).
 \tag{25}
\]
The last three sum to a bound for \(|\Phi_n'|\); their role is tail payment, not replacement of the signed \(D_j\) in the computed core. After multiplying by \(u^k e^{Tu^2+Yu}\), omitted modes \(n\ge m\) have bound
\[
 \frac{C\pi^p m^{2p}e^{-\pi m^2}}{1-\rho_m}
       \frac{k!}{\beta_m^{k+1}},\quad
 \beta_m=4\pi m^2-q_0-Y,\quad
 \rho_m=((m+1)/m)^{2p}e^{-\pi(2m+1)},
 \tag{26}
\]
provided \(\beta_m>0,\rho_m<1,T\le8\pi m^2\). This is Note16's proof with the displayed power and exponential changed explicitly. The ratios decrease with mode number. For a retained mode beyond \(U>0\), the bound is
\[
 \frac{C\lambda_n^p U^k e^{TU^2+(q_0+Y)U-\lambda_ne^{4U}}}
 {4\lambda_ne^{4U}-(q_0+Y)-2TU-k/U},
 \tag{27}
\]
when the denominator is positive and \(16\lambda_ne^{4U}>2T\). It follows from the negative logarithmic derivative and concavity, as before. Endpoint omitted-mode values are bounded by the first omitted component divided by its geometric-ratio complement at that endpoint. All guards require outward arithmetic.

For \(B_j\), use the tail majorant
\(e^{(\tau+R)u^2}[j u^{j-1}\Phi+2(\tau+R)u^{j+1}\Phi+u^j\sum|\Phi_n'|]\).
The inequality \(||D_j|-|D_{j,M}||\le|D_j-D_{j,M}|\) pays omitted modes even when the finite/core derivative changes sign. Absolute-value core quadrature must not be passed to an analytic integrator as though it were holomorphic. Bounded real interval panels are specified in the packet. The complete tails are retained for both the IBP integrals and all original signed jets.

The [collision-control register][controls] and Note16's actual screen remain applicable:

| Class | Applicable premise and limit |
| --- | --- |
| Gaussian-polynomial and three-/four-square event controls | On their own event-containing balls with their own valid derivative envelopes, the exact row forces \(d_N\le0\) for every \(r,R,N\) that contains the event. A smaller ball that excludes it is no longer that collision test. Their full unit theta coefficients fail. |
| Euler-factor controls | Use their own complete sources and derivative budgets. Included actual collisions reject positivity; negative-Laguerre witnesses alone do not locate those collisions. Original arithmetic coefficients fail. |
| Reflected, smooth-shape and positive-primitive controls | IBP and suitable local decay can be shared. Full theta square arithmetic and a paid positive margin are not supplied by shape or a favorable phase endpoint. Use their own moment domains and actual event balls. |
| Finite-source, finite-prime and exact finite-profile controls | Preserved finite measurements do not determine the required complete source envelopes. Atomic sources need not admit the derivative-integral IBP formula; their Taylor/row collision test remains valid in its own moment domain. Retain failed reflection, arithmetic and growth premises from the register. |
| Conditional endpoint / variable-observation controls | Retain RH-conditional scope for the former and the failure of literal cosine/heat reconstruction for the latter. No event or derivative budget is transferred to theta. |
| Relaxed actual-profile measures | They are not physical collision events; no rejection of a theta ball is inferred from them. |
| Positive Gaussian without zeros | Adaptive (19) works where its center discriminant is nonzero, while a fixed radius can fail as accepted in R4. This is a generic capability check, not theta evidence. |

The center condition \(D_0\ne0\) is sufficient and can fail at noncolliding points. Neither the new bounds nor radius adaptation prove it for every theta center. No finite cover of an arbitrary compact, global nonvanishing, or asymptotic computational saving is claimed. This pass supplies concrete source estimates and radius/degree mathematics; their numerical usefulness is the next bounded question.

Follow the [result index][results], [avoid index][avoid], [classification][a01], [scoped negatives][a07], [separate-bound warning][a12] and [noncircular constants][a14]. There is no manuscript, result-summary or milestone promotion. [Note27][next] records the model-change continuation and the preserved chat identity.

[intake]: 25_CONTINUATION_AFTER_E02_R4_AND_MODEL_HANDOFF_20261030.md
[assessment]: ../../reviews/fixed_coefficient_parameter_geometry/08_FCG_E02_R4_COEFFICIENT_LIMITS_ASSESSMENT_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[n16]: 16_QUADRATIC_HEAT_BEZOUT_COEFFICIENT_B03_R3_20261030.md
[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R2_ADAPTIVE_RADIUS_IBP_COMPARISON_20261030.md
[self]: ../../reviews/fixed_coefficient_parameter_geometry/09_ADAPTIVE_RADIUS_IBP_B03_R5_SELF_ASSESSMENT_20261030.md
[next]: 27_CONTINUATION_ADAPTIVE_RADIUS_IBP_AND_MODEL_HANDOFF_20261030.md
[primitive]: ../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md
[localization]: 03_POISSON_LOCALIZATION_AND_RELATIVE_LOSS_B02_20261030.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
