# Backward filtered-pair transport, source residuals and terminal precision

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Status: **proved finite conditional transport estimates and scoped precision diagnostics; no theta simplicity upper bound**. Internal algebra checks only; no independent specialist review or literature priority claim.

This addresses HDC-09 in the [analytical overview][overview]. The main new quantitative conclusion is that the scalar backward gap implementation has an explicit, very large condition factor for the actual fixed-rank late theta regime:

\[
 \log A(t_0,T)\sim \frac{T(\log T)^2}{2\pi^2}.
 \tag{1}
\]

Consequently the inherited algebraic late-time gap error does not close that implementation's absolute-error budget. This conclusion concerns the scalar estimate that treats the exterior coefficient and its residual by separate absolute bounds. It does **not** exclude a joint correlated source/root transport, another observable or a better source theorem. A general matched-reference finite-population theorem below retains the complete source residual, moving normalization and a paid inverse condition factor. Exact quadratic and Hermite controls determine which subleading terminal information cannot be discarded.

Read the [result index][results], [control register][controls], [avoid index][avoid], particularly [target classification][a01], [coupled estimates][a12] and [scoped exclusions][a07]. The inherited inputs are [LHCT Note 06][lhct] (complete forced root dynamics), [BW10 Note 19][motion] (paired product and adjacent-gap equation), [BW10 Note 20][saddle] (differentiated fixed-rank saddle) and [HDC Note 06][spectral] (the finite spectral consumer). HDC-07's [source-force note][source] gives compatible wall estimates. No literature theorem beyond those local inputs is newly imported.

## 1. Scope, population and terminal data

Work on a declared interval \(I=[t_0,T]\), \(t_0>0\). At each time a real-type heat field \(H_t=-H_{zz}\) has a complete population of \(N\) distinct real roots

\[
 x_1(t)<\cdots<x_N(t),\qquad H(t,z)=U(t,z)\prod_{i=1}^N(z-x_i(t)),
 \qquad b=U_z/U.
 \tag{2}
\]

A common or moving zero-free spatial wall encloses exactly this population, and the relevant interior tubes lie in its zero-free-unit domain. Every omitted root and nonzero analytic factor belongs to \(U\). The identities below hold without RH whenever these real-population hypotheses hold. **RH first enters a canonical theta application when it supplies the complete real positive-time continuation from time-zero labels.** The local late-time anchor itself does not require RH.

The terminal theorem accepts either a rigorously enclosed root vector or a rigorously enclosed gap. A terminal value of the scalar filter alone generally does not identify a root configuration when \(N>2\); it is not silently used as root-vector data. The theorem supplies an early-time conclusion only if its stated tube, residual and error inequalities are verified on the entire interval. A local terminal approximation is not such a verification.

Population changes are excluded from a single application of the theorem. If walls or height cuts change membership, apply the theorem on separate intervals and pay an explicit transfer error at each change. Following fixed endpoint labels avoids an unrecorded membership change; it does not by itself prove a spatial wall.

## 2. A matched-reference theorem for a complete finite population

Let \(\alpha(t)>0\) be a prescribed \(C^1\) scale, set

\[
 y_i=\alpha x_i,\quad a=\alpha'/\alpha,
 \quad S_i(y)=\sum_{j\ne i}(y_i-y_j)^{-1}.
\]

Choose a differentiable ordered reference \(c(t)\), with physical reference points \(x_i^*=c_i/\alpha\), and a real analytic reference unit logarithmic derivative \(b_*(t,z)\). Declare its **entire motion defect**

\[
 \eta_i=c_i'-\{2\alpha^2 S_i(c)+a c_i+2\alpha b_*(t,x_i^*)\}.
 \tag{3}
\]

This defect is zero when the reference is an exactly matched heat flow with the same normalization. It need not be zero for a clock or saddle ansatz. Put \(d=y-c\), and define

\[
 K_{ij}^{\rm edge}
   =\frac1{(y_i-y_j)(c_i-c_j)},
 \qquad
 K=\sum_{i<j}K_{ij}^{\rm edge}(e_i-e_j)(e_i-e_j)^T,
\]
\[
 D_i=\int_0^1 b_z(t,x_i^*+\theta(x_i-x_i^*))\,d\theta,
 \qquad
 r_i=2\alpha(b-b_*)(t,x_i^*)-\eta_i.
 \tag{4}
\]

The exact matched equation is

\[
 \boxed{d'=(-2\alpha^2K+aI+2\operatorname{diag}D_i)d+r.}
 \tag{5}
\]

Indeed, subtract the two motions and use the pair identity
\(S_i(y)-S_i(c)=-\sum_{j\ne i}(d_i-d_j)/[(y_i-y_j)(c_i-c_j)]\).
The factor \(2\) in front of \(D_i\) is unchanged by normalization: the factor \(\alpha\) in the velocity cancels the \(\alpha^{-1}\) in the physical displacement. All three terms in (3) are necessary.

**Finite backward theorem.** Suppose a proposed tube \(\|d(t)\|_\infty\le\rho(t)\) has

\[
 2\rho(t)<\min_i(c_{i+1}-c_i),
 \qquad b_z(t,z)\ge-B(t)
 \tag{6}
\]

on every real segment in (4), and that \(\|r(t)\|_2\le\varepsilon(t)\). Write \(c_{ij}=|c_i-c_j|\) and set

\[
 \Lambda(t)=2\max_i\sum_{j\ne i}
     \frac1{c_{ij}(c_{ij}-2\rho)},
 \qquad k(t)=2\alpha(t)^2\Lambda(t)+2B(t)-a(t),
\]
\[
 \mathcal A(t,s)=\exp\!\left(\int_t^s k(v)\,dv\right),
 \qquad
 E(t)=\mathcal A(t,T)E_T+
       \int_t^T\mathcal A(t,s)\varepsilon(s)\,ds.
 \tag{7}
\]

Then \(\|d(t)\|_2\le E(t)\) on every interval on which the tube holds, provided \(\|d(T)\|_2\le E_T\). If the walls and all tube estimates are valid as a priori bounds, \(E(T)<\rho(T)\), and \(E(t)<\rho(t)\) throughout \(I\), the usual first-exit argument proves the tube and the conclusion on all of \(I\).

**Proof.** The mixed weights are positive and at most \([c_{ij}(c_{ij}-2\rho)]^{-1}\), so the graph row-sum bound gives \(0\preceq K\preceq\Lambda I\). The symmetric coefficient matrix in (5) is therefore at least \(-kI\). Reverse time. The largest eigenvalue of the reversed coefficient is at most \(k\); differentiating the Euclidean norm, or using its upper Dini derivative at zero, and applying the integrating factor proves (7). This uses no commutation of the evolving matrices. A first backward tube exit would have \(\|d\|_\infty=\rho\) but \(\|d\|_\infty\le\|d\|_2\le E<\rho\), a contradiction. At a changing wall or reference chart, its explicitly enclosed transfer error is added before the next application.

This is an inverse bound, not the inversion of a forward contraction inequality. In particular the **upper** eigenvalue bound \(\Lambda\), not the coercive lower bound in LHCT's forward theorem, pays the reverse instability.

The same theorem holds directly in the maximum norm, with terminal error \(\|d(T)\|_\infty\le E_T\) and residual allowance \(\|r\|_\infty\le\varepsilon\), using exactly the same \(k\). Indeed, the maximum absolute row estimate for the reversed equation gives the logarithmic norm
\(\max_i[4\alpha^2\sum_{j\ne i}K^{\rm edge}_{ij}-a-2D_i]\le k\).
The upper Dini derivative of \(\|d\|_\infty\) proves (7) and the same first-exit argument. This version avoids converting a componentwise source error into a \(\sqrt N\) Euclidean error; either version may supply \(E\) in (9).

For a unit-spaced clock \(c_i=c_1+i-1\) and \(\rho<1/2\),

\[
 \Lambda\le4\sum_{j\ge1}\frac1{j(j-2\rho)}
 \le\frac{2\pi^2}{3(1-2\rho)}.
 \tag{8}
\]

Thus the interaction part of the norm condition factor need not acquire an artificial factor \(N\). A componentwise force allowance costs \(\sqrt N\) in the Euclidean version and no such factor in the maximum-norm version. Constants for non-clock reference populations retain their actual gaps. The factor from \(-a\) is exactly \(\alpha(t)/\alpha(s)\). Dividing the normalized root error by \(\alpha(t)\) shows that a change of scale alone does not remove physical inverse instability.

### The early filtered-spectrum conclusion

Let \(d_*(t)=\min_i(c_{i+1}-c_i)\) and \(\theta(t)=2E(t)/d_*(t)<1\). Pairwise comparison and the min--max principle give

\[
 L_x(t)\preceq
  \alpha(t)^2(1-\theta(t))^{-2}L_c(t),
\]
\[
 \boxed{
 q(t)\le\sum_{j=1}^N
 \frac{4t\alpha(t)^2(1-\theta(t))^{-2}\lambda_j(L_c(t))}
 {1+4t\alpha(t)^2(1-\theta(t))^{-2}\lambda_j(L_c(t))}.}
 \tag{9}
\]

This is a proved finite-population conclusion with explicit input errors. Under the endpoint and adjacency hypotheses of HDC Note 06, a verified right side below \(1/2\) excludes every multiple endpoint in that population. A right side \(o(N)\), with independently paid complete height coverage, gives the weaker density-one conclusion. Neither input inequality has been proved for canonical theta by (7)--(9).

## 3. How complete source information pays the residual

The theorem does not permit \(b\) to be dropped. For a positively oriented simple zero-free wall \(\Gamma\) enclosing the complete population, write \(Q=H_z/H\). Cauchy subtraction of the internal poles gives

\[
 b(z)=\frac1{2\pi i}\oint_\Gamma\frac{Q(w)}{w-z}\,dw,
 \qquad
 b_z(z)=\frac1{2\pi i}\oint_\Gamma\frac{Q(w)}{(w-z)^2}\,dw.
 \tag{10}
\]

Suppose the relevant physical tube is distance at least \(d_\Gamma\) from the wall. If \(Q_\Gamma\ge\sup_\Gamma|Q|\), a valid fallback is

\[
 B_{\rm wall}:=\frac{\operatorname{length}(\Gamma)}{2\pi d_\Gamma^2}Q_\Gamma.
 \tag{11}
\]

The displayed quantity is an admissible choice for the allowance \(B\); it need not be the optimal allowance. Under the complete all-real theta product, a finite consecutive block has \(b_z\le0\) on its interior real interval, since the exterior derivative is a sum of negative inverse squares. It is a lower bound on that derivative which is needed in (6), so its negative sign does not supply favorable reverse stability.

If \(b_*\) is obtained from a reference field \(H_*\) with its complete reference population inside the same wall, put

\[
 J=H_zH_*-HH_{*,z},\qquad
 Q-Q_* = \frac{J}{HH_*}.
 \tag{12}
\]

With wall floors \(|H|\ge m>0\), \(|H_*|\ge m_*>0\) and an enclosure \(|J|\le J_\Gamma\), one obtains

\[
 \|b-b_*\|_{\rm tube}\le
  \frac{\operatorname{length}(\Gamma)}{2\pi d_\Gamma}
  \frac{J_\Gamma}{mm_*},
\]
\[
 \boxed{\varepsilon(t)\le
  \frac{\alpha\sqrt N\operatorname{length}(\Gamma)}{\pi d_\Gamma}
    \frac{J_\Gamma}{mm_*}+\|\eta(t)\|_2.}
 \tag{13}
\]

This is a source-based finite error bound with no actual internal-gap denominator in the force acquisition. Its geometric interaction cost remains in \(\Lambda\), as it must. Estimate \(J\) together before applying absolute values: if the two source representations are available, their products give a complete double integral whose signed cancellation is preserved by (12). The [HDC-07 note][source] supplies another paid relative-wall route. No favorable theta value of \(J_\Gamma/(mm_*)\) across the full early-to-late interval is asserted here.

For the maximum-norm theorem, omit \(\sqrt N\) from (13) and replace \(\|\eta\|_2\) by \(\|\eta\|_\infty\). This pays the complete componentwise residual without an unnecessary population factor.

For comparison, if only \(|H-H_*|\le e_0<m_*\), \(|H_z-H_{*,z}|\le e_1\), \(|H_*|\ge m_*\), and \(|H_{*,z}|\le M_{1,*}\) are known, then

\[
 |Q-Q_*|\le\frac{e_1}{m_*-e_0}
   +\frac{M_{1,*}e_0}{m_*(m_*-e_0)}.
 \tag{14}
\]

This is a fallback, not a replacement for the correlated numerator. Every field error, wall floor and derivative bound in (11)--(14) is for the complete source with a justified tail. A real-axis terminal approximation does not automatically supply a complex wall estimate.

For a moving-frequency clock ansatz \(H_*=A(t)\cos(\ell(t)z)\), the reference field generally does **not** solve the heat equation. With \(\alpha=\ell/\pi\), its selected reference roots have constant \(c_i\); at those roots its finite reference unit obeys \(b_*(x_i^*)=-S_i(x^*)\). Hence (3) gives \(\eta_i=-a c_i\). This explicit term must be retained in (13). Declaring a clock stationary in scaled coordinates is not permission to delete its physical motion or normalization defect.

## 4. A sharper two-root theorem: regular squared gap and exact filter

For a complete two-root cluster \(a(t)<b(t)\), put

\[
 g=b-a,\quad h=g^2,\quad
 S(t)=-\frac{\mathfrak b(t,b(t))-\mathfrak b(t,a(t))}{b(t)-a(t)},
 \qquad \mathfrak b(t,z)=U_z(t,z)/U(t,z).
 \tag{15}
\]

The distinct font \(\mathfrak b\) separates the unit logarithmic derivative from the upper root \(b(t)\). Equivalently,
\(S=-\int_0^1\partial_z\mathfrak b(t,a+\theta g)\,d\theta\).
For a globally adjacent pair in the complete all-real theta product,

\[
 S(t)=\sum_{r\ne a,b}\frac1{(a-r)(b-r)}\ge0,
\]

with the absolutely convergent convention in BW10 Note 19. The complete equations and the two-root filter are

\[
 \boxed{h'=8-4Sh,\qquad q_2(t)=\frac{8t}{h(t)+8t}.}
 \tag{16}
\]

The sign and normalization matter: the unit divided difference equals \(-S\), **not** \(-S/2\). It gives \(g'=4/g-2Sg\). Unlike \(g\), the variable \(h\) has no internal square-root singularity at an isolated double event.

Let a nonnegative prescribed reference \(h_*\) and a prescribed coefficient \(S_*\) have the declared defect

\[
 \rho_*=h_*'-8+4S_*h_*.
\]

Define \(A(t,s)=\exp(4\int_t^s S)\). Exact subtraction gives

\[
 h(t)-h_*(t)=A(t,T)[h(T)-h_*(T)]
 +\int_t^T A(t,s)\{4(S-S_*)h_*+\rho_*\}(s)\,ds.
 \tag{17}
\]

Thus, if \(h(T)\ge h_*(T)-E_T^-\), \(0\le S\le B_S\) and
\(4(S-S_*)h_*+\rho_*\ge-e_-(t)\), the explicit allowance

\[
 E_-(t)=e^{4\int_t^T B_S}E_T^-
 +\int_t^T e^{4\int_t^s B_S}e_-(s)\,ds
 \tag{18}
\]

gives \(h(t)\ge h_*(t)-E_-(t)\). In particular, whenever this lower bound is nonnegative,

\[
 q_2(t)\le\frac{8t}{h_*(t)-E_-(t)+8t};
 \qquad h_*(t)-E_-(t)>8t\Longrightarrow q_2(t)<1/2.
 \tag{19}
\]

Without the nonnegativity condition one retains the trivial \(q_2<1\). A convenient absolute residual allowance is
\(e_-=4\epsilon_S h_*+|\rho_*|\) when \(|S-S_*|\le\epsilon_S\). Equation (17) permits a sharper **one-sided** residual if a source sign has actually been proved. An upper bound for \(q_2\) requires a lower bound for \(h\); using the reverse inequality would give the wrong conclusion.

For source acquisition, the coefficient itself has the complete wall formula

\[
 S=-\frac1{2\pi i}\oint_\Gamma
       \frac{H_w/H}{(w-a)(w-b)}\,dw.
 \tag{20}
\]

It remains bounded through an isolated double birth when the two-root wall and the nonvanishing unit persist. If the reference endpoints differ, a comparison \(S-S_*\) must also pay their displacement. For example, let \(\beta_1\) bound \(|b_z-b_{*,z}|\) on all joining segments and let \(B_{2,*}\) bound \(|b_{*,zz}|\). Then

\[
 |S-S_*|\le\beta_1+
     \frac{B_{2,*}}2(|a-a_*|+|b-b_*|),
 \tag{21}
\]

by the integral divided-difference formula. Such endpoint errors can be supplied by (7). For a pair cut from an \(m>2\) birth, the two-root unit is not nonvanishing at the endpoint; (20)'s bounded-unit conclusion is unavailable as \(t\downarrow0\). Track the full cluster or retain its explicit singular compression instead.

## 5. Sharp endpoint controls and terminal precision

For the exact heat polynomial

\[
 H_s(t,z)=z^2-2(t+s),\qquad s\ge0,
\]

the endpoint is double at \(s=0\) and consists of two simple real roots at \(s>0\). Here

\[
 h_s(t)=8(t+s),\quad S=0,\quad
 q_s(t)=\frac{t}{2t+s},\qquad
 \frac12-q_s(T)=\frac{s}{2(2T+s)}.
 \tag{22}
\]

The stable unfiltered quantity is \(h(T)-8T=8s\); it has **unit** terminal absolute-error amplification. However a terminal filter error has a different scale. Exact reconstruction is

\[
 q(t)=\frac{tq(T)}{T+2(t-T)q(T)},\qquad
 \left.\frac{\partial q(t)}{\partial q(T)}\right|_{q(T)=1/2}
       =\frac{T}{t}.
 \tag{23}
\]

An uncertainty interval of radius \(\epsilon_T\ge s/[2(2T+s)]\) about the simple model's exact terminal filter value also contains the double model's value \(1/2\). It therefore cannot distinguish these two endpoints from that scalar datum. For fixed \(s>0\), the necessary scale is \(O(s/T)\); an error \(o(1/T)\) separates each fixed positive \(s\) eventually, but no positive finite error works uniformly over all arbitrarily small \(s>0\). This is a two-model information statement, not an assertion that a particular theta error must have that size.

The corresponding all-multiplicity control is

\[
 P_{m,s}(t,z)=e^{-(t+s)\partial_z^2}z^m,
 \qquad x_j(t)=\sqrt{2(t+s)}\,h_j,
\]

where \(h_j\) are the roots of \(\mathrm{He}_m\). Its pair-Laplacian eigenvalues are \(k/[4(t+s)]\), \(k=0,\ldots,m-1\), and

\[
 q_{m,s}(t)=\sum_{k=1}^{m-1}\frac{kt}{(k+1)t+s},
 \qquad q_{m,0}=m-H_m,
\]
\[
 q_{m,0}-q_{m,s}(T)
  =\sum_{k=1}^{m-1}\frac{ks}{(k+1)((k+1)T+s)}
  =\frac{s}{T}(H_m-H_m^{(2)})+O_m(s^2/T^2).
 \tag{24}
\]

Thus perfect leading Hermite convergence can coexist with an \(m\)-fold endpoint. The \(T^{-1}\) terminal distinction is present for every fixed \(m\ge2\), not merely doubles. These models satisfy the generic finite real-root and heat hypotheses, but not the unchanged theta source; a theta-specific improvement remains possible.

For an adjacent subpair of the pure \(m\)-fold birth, let \(d=h_{j+1}-h_j\). Then

\[
 h(t)=2d^2t,\quad
 S(t)=\frac{1/d^2-1/4}{t},\quad
 A(t_0,T)=(T/t_0)^{4/d^2-1}.
 \tag{25}
\]

The exponent is nonnegative by the full adjacent-gap law. It is zero for the quadratic birth and positive for an adjacent subpair of a higher birth. The coefficient \(S\sim t^{-1}\) is precisely the omitted within-cluster force; replacing it by a bounded two-root unit loses the multiple-endpoint control.

## 6. The actual fixed-rank late theta regime

Fix an adjacent positive rank pair \(k,k+1\), and suppose its positive-time continuation to a fixed \(t_0>0\) is available. Under RH this continuation and real adjacency hold. Use the scalar saddle scale \(\ell(t)\), **not** the symbol for the pair matrix, determined by

\[
 4\pi e^{4\ell}=2t\ell+9,\qquad
 \kappa=8t\ell-2t+36,\qquad \ell'/\ell=2/\kappa.
 \tag{26}
\]

The complete-source theorem in BW10 Note 20 supplies the following **fixed \(K=k+1\)** terminal regime. Write \(V_t(u)=tu^2+9u-\pi e^{4u}\). Its finite conditions DS7 are \(\ell\ge1/4\), \(\kappa\ge32\), \(t/\kappa\le1/(4e)\), and \(V_t(\ell-1/4)\ge V_t(0)\). Require these, \(\Delta_0<\sqrt{2\pi}\), and, with fixed \(0<\beta<\pi/4\) and \(Z=(K-1/2)\pi+\beta\),

\[
 \epsilon_0=ZM_1/\ell<\sin\beta,
 \qquad \epsilon_1=(1+Z)M_1/\ell<\cos\beta.
 \tag{27}
\]

All \(M_p,\Delta_p\) are the complete source/tail allowances defined there. Its root enclosures give

\[
 |\ell x_j-(j-1/2)\pi|\le e_T=\arcsin\epsilon_0,
 \quad
 \left|g(T)-\frac\pi{\ell(T)}\right|\le\frac{2e_T}{\ell(T)},
\]
\[
 \left|h(T)-\frac{\pi^2}{\ell(T)^2}\right|
 \le\frac{4\pi e_T+4e_T^2}{\ell(T)^2}
 =O_K\!\left(\frac1{\ell(T)^3\sqrt{\kappa(T)}}\right).
 \tag{28}
\]

The last estimate uses its \(e_T=O_K((\ell\sqrt\kappa)^{-1})\). More specifically, the **explicit allowance** there has \(M_1\sim\sqrt{2/\pi}\,\kappa^{-1/2}\), since \(\Delta_0,\Delta_1\to0\), \(G_1=2\) and \(G_0=\sqrt{2\pi}\). Hence at fixed \(Z>0\),

\[
 \frac{4\pi e_T+4e_T^2}{\ell(T)^2}
 \sim\frac{4\pi Z\sqrt{2/\pi}}{\ell(T)^3\sqrt{\kappa(T)}}.
 \tag{28a}
\]

This asymptotic concerns the proved error allowance, not the unknown actual error. These are algebraic errors with declared rank and sufficient onset conditions, not a uniform growing-rank assertion or a numerical onset certificate. The differentiated theorem also gives \(g'=-\pi\ell'/\ell^2+O_K((\ell\kappa^{5/4})^{-1})\); no location remainder is differentiated here.

The scalar condition factor can now be evaluated asymptotically without guessing an exterior force. Equation (16) implies exactly

\[
 \log A(t_0,T)
 =8\int_{t_0}^T\frac{ds}{h(s)}
    -\log\frac{h(T)}{h(t_0)}.
 \tag{29}
\]

The saddle theorem gives \(h(t)\sim\pi^2/\ell(t)^2\), \(\ell(t)\sim(\log t)/4\). Therefore

\[
 \log A(t_0,T)
 \sim\frac8{\pi^2}\int^{T}\ell(s)^2\,ds
 \sim\frac{T(\log T)^2}{2\pi^2},
\]

proving (1). The fixed early portion contributes only a constant, and the logarithm of \(h(T)/h(t_0)\) is \(O(\log\log T)\), negligible on the displayed scale.

For the implementation (18), a fixed acceptable early gap error \(E_0\) requires at least

\[
 E_T^-\le E_0/A(t_0,T),
 \qquad
 \int_{t_0}^T A(t_0,s)e_-(s)\,ds\le E_0
 \tag{30}
\]

after a suitable split of the budget between the two terms. If one uses an upper enclosure for \(S\), the condition factor can only increase. The explicit algebraic **allowance** in (28a), multiplied by the condition factor in (1), diverges and hence cannot certify such a fixed early error. This does not prove that the unknown actual saddle remainder is bounded below by that allowance; it proves that the available stated allowance does not close (30).

The large factor is not a contradiction with the actual late gap being very regular. In the exact scalar reconstruction

\[
 h(t_0)=A(t_0,T)h(T)-8\int_{t_0}^T A(t_0,s)\,ds,
 \tag{31}
\]

the two terms can be enormous and cancel. Treating their errors independently loses that correlation. The fixed sine heat field \(e^t\sin z\), with adjacent gap \(\pi\), already has \(S=2/\pi^2\) and \(A=e^{8(T-t_0)/\pi^2}\), although its exact stationary reference has zero residual. This confirms the need to keep joint source information; it prevents interpreting (1) as a universal lower bound for every estimator or every field-to-field inverse problem.

## 7. Field smoothing, root inversion and growing height

Decreasing real heat time genuinely smooths the complete field. For the canonical Fourier integral and \(s=T-t>0\),

\[
 H(t,x)=\frac1{\sqrt{4\pi s}}\int_{\mathbb R}
 e^{-(x-y)^2/(4s)}H(T,y)\,dy.
 \tag{32}
\]

The source has sufficient decay to interchange the integrals; the Gaussian multiplies each Fourier mode by \(e^{-su^2}\). Thus bounded whole-real-line terminal field errors contract in the supremum norm under (32). This assertion concerns the full unnormalized terminal field on the entire real line. It is not supplied by finitely many root positions, a local normalized cosine approximation or a scalar \(q(T)\).

Recovering individual zeros is another map. A simple-zero perturbation estimate divides a field error by a verified derivative floor; at an \(m\)-fold zero the generic displacement scale is a fractional power of the field error. A wall Rouché bound preserves total multiplicity but need not decide whether it is concentrated at one multiple zero or split among simple roots. The quadratic family (22) exhibits this distinction exactly: its field difference is the constant \(2s\), while its terminal filter distinction decays as \(s/T\). Stable field smoothing alone therefore does not establish simplicity.

For growing-height use of (7)--(9) or (17)--(19), the additional obligations are concrete:

1. A declared rank/height/time family, complete endpoint populations and tracked walls, with an explicit allowance for any omitted endpoint labels.
2. Terminal enclosures uniform in that rank range and in every needed spatial derivative or complex wall strip. Fixed \(K\) in (27) is not sufficient.
3. Uniform bounds for the actual interaction condition factors, source residuals, wall floors, reference defects and their **integrated amplified** errors. A small pointwise residual is insufficient.
4. A justified treatment of changing populations, normalization and reference charts. Omitting \(o(N)\) labels is a root-count payment, not automatically an \(o(1)\) pair-statistic payment.
5. An early comparison for which the full right side of (9) is \(o(N)\) for density one, or strictly below \(1/2\) for the stronger finite-population conclusion. Choosing an early time after inspecting unknown endpoint separations would only restate the target.

In particular the fixed-rank \(T\to\infty\) regime leading to (1) is distinct from high height at a fixed positive time, and from the proposed \(t_h\nu_h^2\to0\) regime. This note proves no interchange between them.

## 8. Controls, checks and resulting status

| Control | Result and exact scope |
| --- | --- |
| Simple and double quadratic heat polynomials | Pass the finite dynamics; (22)--(23) give the exact terminal information loss and sharp filter sensitivity. They fail the unchanged theta-source premise. |
| Shifted Hermite families for all fixed multiplicities | Pass the full finite equations; (24)--(25) retain multiple endpoint modes and singular within-cluster compression. Their leading terminal geometry does not discriminate simplicity. They lack the theta source. |
| Stationary sine heat field | Its complete exterior unit cancels internal repulsion. It passes the generic wall/motion identities and demonstrates that scalar inverse conditioning and zero exact residual can coexist. Its source is atomic rather than canonical theta. |
| Euler-factor and close positive endpoint controls | Generic equations apply on the real simple intervals actually established for them. Changed source data or failure of ordinary Dirichlet arithmetic precludes transferring the canonical source constants; no discrimination follows merely from the generic theorem. |
| Weighted-square / finite-prime controls | No complete all-real positive-time system is assigned without proof. They fail the full normalized reflection hypotheses and cannot be used as if they supplied the global adjacent-real spectrum. Their local analytic heat identities survive. |
| Reflected, smooth and positive-primitive controls | They lack the unchanged integer-square source. Generic local source and preparation identities remain valid on their actual domains; an unproved global real continuation is not assumed. |

The accompanying [exact-rational replay][replay] and [small execution record][record] check the mixed-Laplacian subtraction, the two-root force factor, the exact backward quadratic filter reconstruction and its derivative, and the Hermite filter coefficient identity. They check algebra only; they do not certify source walls, a theta onset or a global upper bound.

HDC-09's **finite analytical transport and precision deliverable is obtained in conditional form**: (7), (9), (13), (18)--(19) have declared hypotheses, complete residuals and explicit amplification. The scalar late-theta absolute-error implementation is quantitatively insufficient with the currently stated saddle allowances, by (1), (28)--(30). A useful canonical estimate on the joint residual, or an alternative stable source observable retaining the endpoint distinction, remains open. No new RH-conditional simplicity proportion or all-simple theorem is asserted.

[overview]: ../research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md
[spectral]: 06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md
[source]: 07_COMPLETE_SOURCE_FORCE_AND_FILTER_RESIDUAL_20261023.md
[lhct]: ../../11_late_heat_caps_and_charge_transport/notes/06_PAIR_DISTANCE_MATRICES_AND_FORCED_HEAT_DISSIPATION_20261022.md
[motion]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[replay]: ../numerics/04_check_backward_transport_20261023.py
[record]: ../numerics/04_BACKWARD_TRANSPORT_CHECKS_20261023.json
