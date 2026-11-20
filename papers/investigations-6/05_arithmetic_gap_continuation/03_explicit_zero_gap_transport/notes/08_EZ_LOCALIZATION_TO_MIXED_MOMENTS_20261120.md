# Initial mixed moments from the explicit large-time zeros

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance. The desktop thread records gpt-6.2-astra with ultra effort. Separate per-turn and contributor settings are unavailable.

The explicit formulas for individual zeros initialize an entire row of the parent's exterior hierarchy for each marked pair. Below is a quantitative large-time estimate for all pairs in a fixed interior fraction of the growing window, at each fixed mixed order. The input is the canonical theta source at a known all-real anchor \(T\). The error includes every exterior occurrence. [Founding Note 08, §§1–4](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) · [Complete product and pair equation](../../manuscript/sections/02_pair_chain.tex) · [Mixed hierarchy](../../manuscript/sections/03_hierarchy.tex)

## A row at a counted anchor

Let \(\mu=\mathbb E_T U\) for the positive-half-line source of the founding note, \(\kappa=8TL_T-2T+36\), \(\ell=\mu\sqrt\kappa\), and \(q_j=(j-\tfrac12)\pi\). Use \(x_{1-j}=-x_j\) for \(j\ge1\). For \(u=x_n\), \(v=x_{n+1}\), the parent's convention for the user's \(S_{n,p,q}\) is

\[
 P^{(n)}_{p,q}=\sum_{\rho\ne u,v}(\rho-v)^{-p}(\rho-u)^{-q},
 \qquad m=p+q\ge2,\quad p,q\in\mathbb Z_{\ge0}.
\]

The two excluded occurrences are the marked pair. Here the targets are distinct simple positive zeros, the complete divisor is real, and exterior occurrences are included with multiplicity. The exact gap equation uses this row in the direction \(M_n=P^{(n)}_{1,1}\), \(g_n=v-u\), \(g_n'=4/g_n-2g_n M_n\). Every time derivative of a fixed row entry on a separated chart uses finitely many entries of the same array and the gap, including the two axis families. The full recurrence raises orders. A finite set of orders alone does not determine its future values. The parent gives the symmetric coordinates through a target merger. [Parent §3, integer split recurrence and symmetric variables](../../manuscript/sections/03_hierarchy.tex)

For fixed \(C>0\), take \(K=K(T)\) with \(q_K\asymp\ell\) and \(q_K\le C\ell\). Fix \(0<\theta<1\). Uniformly for \(1\le n\), \(n+1\le\theta K\), and sufficiently large \(T\),

\[
 \boxed{\displaystyle
 \mu^{-m}P^{(n)}_{p,q}
 =\pi^{-m}\sum_{r\in\mathbb Z\setminus\{0,1\}}(r-1)^{-p}r^{-q}
    +O\!\left((\ell\sqrt\kappa)^{-1}+K^{1-m}\right).}
 \tag{1}
\]

The constant may depend on the fixed order, \(C,\theta\), and the lower comparison constant for \(q_K/\ell\). The lattice sum is absolutely convergent, including on the two axes.

**Explicit positions in the window.** In the normalization of founding Note 08, \(\mu x_j=Y(q_j)\). Its §4 complex-disk estimate gives \(|H_o(y)|=O_C(\kappa^{-1/2})\) on \(|y|\le 4C\ell\), for the odd cumulant correction in \(Y(q)=q+H_o(Y(q))\). Rouché on \(|y|=3C\ell\) gives one solution for \(|q|\le 2C\ell\) for sufficiently large \(T\). It is the inverse through zero, and the equation bounds \(|Y(q)-q|\) there by the same constant. Cauchy's derivative estimate on the interior disk gives \(|Y'(q)-1|=O_C((\ell\sqrt\kappa)^{-1})\) for \(|q|\le C\ell\). Integrating along the real segment between any two indexed levels in this disk therefore controls their difference to that relative accuracy, even for neighbors. Oddness covers the reflected positions. For \(1-K\le i\le K\), \(i\notin\{n,n+1\}\), substituting into both endpoint factors changes each normalized summand by at most \(O_{C,m}((\ell\sqrt\kappa)^{-1})\) times its absolute lattice summand. Their absolute sum is bounded independently of \(n,K\) by translation and \(m\ge2\). [Source disk and cubic remainder](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md)

**Control of all omitted zeros.** The even product gives the exact tail budget
\[
 W_1(K)=\sum_{j>K}x_j^{-2}=\tfrac12\mathbb E_T U^2-\sum_{j=1}^K x_j^{-2}.
\]
It includes the variance term \(\mathbb E_T U^2=\mu^2+\operatorname{Var}_T(U)\). In the present window,
\[
 \frac{W_1(K)}{\mu^2}=\sum_{j>K}q_j^{-2}+O_C(\ell^{-2})=O_C(K^{-1}).
 \tag{2}
\]
Indeed the cosine product gives \(\sum_{j\ge1}q_j^{-2}=1/2\), and saddle variance gives \(\operatorname{Var}_T(U)/\mu^2=O(\ell^{-2})\). The founding estimate \(|Y(q_j)-q_j|\ll_C\kappa^{-1/2}(q_j/\ell)^3\), with \(Y(q_j)\asymp q_j\), gives a reciprocal-square error \(O_C(\kappa^{-1/2}\ell^{-3})\) per known zero. Summing it through \(K=O_C(\ell)\) proves (2). [Source and complete-product identities](../manuscript/anchors.tex)

For \(R=x_K\asymp K/\mu\), choose fixed \(\theta<\theta'<1\). Eventually \(0<u<v\le\theta'R\), since \(q_{n+1}/q_K\le\theta+o(1)\) and \(Y\) has the slope bound above. Both distances from \(\pm x_j\), \(j>K\), to the targets are at least \((1-\theta')x_j\). The absolute tail of the row is therefore at most \(2(1-\theta')^{-m}R^{2-m}W_1(K)\). After normalization this is \(O(K^{1-m})\). The omitted half-integer lattice on each side has the same normalized order by comparison with \(\sum_{k\ge(1-\theta)K}k^{-m}\). Combining the two tail bounds with the interior estimate proves (1). At finite \(T\) the higher even source moments can recover the signed tail to geometric accuracy. [Complete anchor and computable remainder](09_EZ_COMPLETE_ANCHOR_FROM_ZERO_FORMULAS_20261120.md)

## Finite localization error and the gap equation

For a finite anchor, the founding contour series and the inverse series both supply indexed position intervals. Suppose a retained exterior occurrence and the two endpoints have midpoint estimates \(\hat\rho,\hat v,\hat u\) with respective error radii \(e_i,e_+,e_-\). Put \(b_+=|\hat\rho-\hat v|-(e_i+e_+)\), \(b_-=|\hat\rho-\hat u|-(e_i+e_-)\). When both are positive the absolute error in its mixed summand is at most
\[
 b_+^{-p}b_-^{-q}
 \left(\frac{p(e_i+e_+)}{b_+}+\frac{q(e_i+e_-)}{b_-}\right).
\]
Integrate the two partial derivatives of \(d_+^{-p}d_-^{-q}\) along the straight segment from estimated to actual signed separations. Their moduli have the displayed denominator floors throughout. Thus explicit intervals, source moments and an exterior remainder give actual row enclosures wherever the one-zero labels and distances are established. Shared endpoint errors may allow sharper treatment.

For \((p,q)=(1,1)\) the sum in (1) telescopes to \(2\), giving \(2/\pi^2\) after normalization, while \(\mu g_n=\pi(1+O_C((\ell\sqrt\kappa)^{-1}))\). These leading terms cancel in \(g_n'\). The absolute remainder in (1) leaves its sign unresolved. Retaining the variance term in the full radial tail resolves the sign on a smaller growing index range in [Note 09, (4)](09_EZ_COMPLETE_ANCHOR_FROM_ZERO_FORMULAS_20261120.md). The earlier signed large-time result supplies a comparison on its own domain. [Large-time transport theorem](../manuscript/transport.tex)

**Continuation.** Equation (1) gives initial data for growing-index families and an explicit order-by-order accuracy. The largest physical heights it covers have size \(O_C(\sqrt\kappa)\) as \(T\to\infty\). At any fixed anchor it therefore leaves an unbounded height range open. A continuation needs a bound on the errors that higher orders feed back into \(P_{1,1}^{(n)}\) along a common backward time interval, together with continued pair counts and control of all remaining heights. Constants that grow with order or with the double-scaling parameter \(C\) must be accounted for in that step. No time differentiation of (1) is justified by its value estimate.

**Classification and controls.** This is a fixed-order asymptotic at an already all-real large-time anchor. The product and localization parts apply wherever their hypotheses are verified. For the Euler-factor controls the shifted source changes the cumulants and the complete radial budget. The weighted-square controls change the weights and lack a complete all-real anchor. The reflected control has the super-Gaussian source, and the primitive-compatible control has a different source despite its matched endpoint data. The canonical saddle estimates used for (1) have only been supplied for theta. At a double target a one-simple-zero label at each distinct endpoint fails, including for the reflected and primitive controls at their witnessed collisions. A bound for (1) on a separated interval asserts no exclusion at such an event. [Result index](../../../../../result-summaries/README.md) · [Control families and their witness domains](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns index](../../../../../avoid/README.md) · [Milestone classification](../../../../../avoid/01_restating_the_target.md) · [Numerics and structural questions](../../../../../avoid/10_numerics_ahead_of_the_question.md)
