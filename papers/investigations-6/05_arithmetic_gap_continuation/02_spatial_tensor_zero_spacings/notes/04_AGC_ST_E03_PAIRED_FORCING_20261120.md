# A signed forcing bound from paired exterior spans

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Executor dispatched as gpt-6.2-sol, effort ultra. Serving configuration has no separate attestation. AGC-ST-E03 r1, finite-head inequalities proved on the stated slice, pending assessment.

Use the literal \(H\) of [AGC §1](../../manuscript/sections/01_source.tex), its complete even product and uniform count, and the count-two readout of [E02](03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md). Fix a slice with distinct consecutive real targets \(a<b\), both counted in their cleared cell. Put \(g=b-a>0\), \(D=g^2/4\), and \(Q_\rho=(\rho-a)(\rho-b)\). These are the actual target endpoints and gap at the slice. Every exterior occurrence is counted with its multiplicity. The observable is \(K=24D^2S_2+32D^3S_3\) of [AGC §4](../../manuscript/sections/04_continuation.tex). The inputs and comparator are those of the [B02 decision](../brainstorm/notes/02_AGC_ST_B02_PAIRED_SPANS_20261120.md) and the [frozen request](../research-progress/handoffs/AGC_ST_E03_REQUEST_R1_20261120.md).

## The paired head

For an exterior occurrence let \(r=\rho-b\) on the right or \(r=a-\rho\) on the left, so \(Q_\rho=r(r+g)\). In either coordinate \(x=r/g\), the single-occurrence kernel in \(K\) is
\[
 k(x)=\frac{3}{2x^2(x+1)^2}+\frac{1}{2x^3(x+1)^3}
     =\frac12\big[x^{-3}-(x+1)^{-3}\big].                         \tag{1}
\]
The equality follows from \((x+1)^3-x^3=3x(x+1)+1\). On the positive real axis \(k\) is decreasing and strictly convex, with
\[
 k'(x)=-\tfrac32\big[x^{-4}-(x+1)^{-4}\big],\qquad
 k''(x)=6\big[x^{-5}-(x+1)^{-5}\big]>0.                          \tag{2}
\]

Choose \(J\) disjoint marked real pairs \((l_m,r_m)\), one occurrence from each side, with the prescribed labels \(1\le m\le J\). The normalized nearer-endpoint distances and the span are
\[
 x_{m,-}=\frac{a-l_m}{g},\qquad x_{m,+}=\frac{r_m-b}{g},\qquad
 W_m=r_m-l_m .
\]
The only ordering used on the head is the supplied label of each occurrence, for example the order of adjacent real neighbors on each side. Let
\[
 \eta_m=\frac{x_{m,-}+x_{m,+}}2-m
       =\frac{W_m/g-1}{2}-m,\qquad
 \kappa_m=-k'(m)=\tfrac32\big[m^{-4}-(m+1)^{-4}\big]>0.
\]
Thus an upper bound on the signed mean displacement \(\eta_m\) is the one-sided input for a lower forcing bound. Jensen's inequality and the supporting line at \(m\) give
\[
 \begin{aligned}
 K_J&=\sum_{m=1}^J\big[k(x_{m,-})+k(x_{m,+})\big]\\
    &\ge 2\sum_{m=1}^J k(m+\eta_m)
     \ge 1-\frac1{(J+1)^3}-2\sum_{m=1}^J\kappa_m\eta_m
     =:L_J .
 \end{aligned}                                                   \tag{3}
\]
Here \(2\sum_{m=1}^J k(m)=\sum_{m=1}^J[m^{-3}-(m+1)^{-3}]=1-(J+1)^{-3}\). The linear coefficient of each individual displacement \(x_{m,\pm}-m\) is \(-\kappa_m\); that of each mean displacement \(\eta_m\) is \(-2\kappa_m\). Jensen is an equality for a pair exactly when the two distances agree, and its supporting-line step is an equality exactly when the mean is \(m\). The signed sum across the labels is retained. In particular an upper bound on \(2\sum_m\kappa_m\eta_m\) alone suffices for the linear floor without bounding the positive parts of individual \(\eta_m\)'s.

Once the target and occurrence labels are supplied, a leaf adds \(\kappa_m[(a-l_m)/g-m]\) for each of its left marks and \(\kappa_m[(r_m-b)/g-m]\) for each right mark. A parent adds the children’s signed totals. This gives \(2\sum_m\kappa_m\eta_m\) even when the two marks of one pair lie in different leaves. No extra term occurs at the interface in this linear sum. The Jensen bound instead uses each individual span, so to compute it the parent needs the marks paired by label or their spans. The quadratic allowance below can also be added over leaves by summing the indicated nonnegative individual terms. All labels, marks and the target normalization refer to the physical divisor at the evaluation slice. If a split changes its occurrence assignment, the sums use the reassigned labels. There is no approximation to \(g\) or to the selected positions in (3).

## Second-order allowance and the direct comparison

For \(x\ge\lambda m\), \(0<\lambda\le1\), the integral Taylor formula gives
\[
 k(x)-k(m)-k'(m)(x-m)
  =(x-m)^2\int_0^1(1-v)\,k''(m+v(x-m))\,dv .
\]
For \(s>0\) one has \(k''(s)=30\int_s^{s+1}y^{-6}\,dy\le30s^{-6}\). Thus if all the chosen distances satisfy \(x_{m,\pm}\ge\lambda m\),
\[
 K_J=L_J+E_J,\qquad
 0\le E_J\le
 15\lambda^{-6}\sum_{m=1}^J
       \frac{(x_{m,-}-m)^2+(x_{m,+}-m)^2}{m^6}
 =:A_J .                                                       \tag{4}
\]
The allowance has the same sign on both sides of the target. Equivalently, the error relative to the linear floor belongs to \([0,A_J]\); no unknown orientation can make it negative. The formula is an upper allowance for the head and is zero for the exact clock configuration.

For the prescribed balanced dilation, take \(x_{m,-}=(1-\delta)m\), \(x_{m,+}=(1+\delta)m\) with \(0<\delta<1\). Then \(W_m=(2m+1)g\), all \(\eta_m=0\), and both (3) floors give the clock value. The actual head lies above it by a strictly positive amount for \(J>0\), bounded by
\[
 \frac{30\delta^2}{(1-\delta)^6}\sum_{m=1}^J m^{-4}.
\]
If the paired relation is dropped and only the common independent upper caps \((1+\delta)m\) are retained, the minimum over that rectangle is \(2\sum_m k((1+\delta)m)\), attained at its simultaneous upper corner. It is strictly below the clock floor for \(J>0,\delta>0\). The difference has linear term \(2\delta\sum_m m\kappa_m\); the error relative to that term is between \(-30\delta^2\sum_m m^{-4}\) and zero by (4) applied at the corner with \(\lambda=1\). This exhibits the loss of the paired cancellation when using those caps. With equal caps the rectangle and Jensen give equality if the available mean bound is just the cap itself, and a strictly smaller mean bound improves the Jensen floor. With exact asymmetric caps attained by known distances the rectangular evaluation is already exact. A direct sum supplied the same spans and quadratic data attains (3)–(4), and a direct sum supplied all exact distances can just evaluate (1). [AGC §4, clock and robust head](../../manuscript/sections/04_continuation.tex)

## The complete exterior and a sign sector

Absolute convergence of the complete \(S_2,S_3\) follows from the inherited count. Their linear combination is real by conjugation, so its omitted part can be summed as real parts of individual occurrences. Every omitted real occurrence has \(x>0\) by adjacency and gives a positive term in (1). For an omitted nonreal occurrence horizontally outside the two endpoints, choose \(r=\rho-b\) if \(\Re\rho>b\), and \(r=a-\rho\) if \(\Re\rho<a\). Then \(\Re r>0\) and
\[
 k(r/g)=\frac{g^3}{2}\big[r^{-3}-(r+g)^{-3}\big]
       =\frac{3g^3}{2}\int_0^g(r+s)^{-4}\,ds ,
 \qquad
 \frac1{Q_\rho}=\frac1g\int_0^g(r+s)^{-2}\,ds .                 \tag{5}
\]
When \(\Re r\ge (1+\sqrt2)|\Im r|\), the argument of \(r+s\) lies in \([-\pi/8,\pi/8]\) for every \(s\ge0\). Both integrands in (5) have nonnegative real part. This supplies \(\Re k(r/g)\ge0\) and \(\Re(1/Q_\rho)\ge0\) on the same sector. The latter is an occurrence-level sign statement, with no estimate for the complete \(M\) used here.

The half-angle \(\pi/8\) is sharp for a uniform ray-angle guarantee of the \(K\) sign over all \(g/|r|>0\). For \(r=|r|e^{i\theta}\) on a fixed ray in the right half-plane,
\[
 \lim_{g/|r|\to0}\frac{k(r/g)}{(g/|r|)^4}
     =\tfrac32 e^{-4i\theta}.
\]
This follows by scaling \(s\) by \(g\) in (5). In any wider sector one can choose \(\theta\) just above \(\pi/8\) so that \(\cos(4\theta)<0\). The real part is then negative for sufficiently small positive \(g/|r|\). This concerns a sector uniform in the ratio and does not require the existence of a theta zero on that ray.

Let \(\mathcal P\) contain the omitted real occurrences and the omitted nonreal occurrences in the sector of (5), and let \(\mathcal N\) be the rest. These are disjoint occurrence collections invariant under conjugation. Write
\[
 \begin{split}
 K_{\mathcal P}&=\sum_{\rho\in\mathcal P}
                \Re(24D^2Q_\rho^{-2}+32D^3Q_\rho^{-3})\ge0,\\
 K_{\mathcal N}&=\sum_{\rho\in\mathcal N}
                \Re(24D^2Q_\rho^{-2}+32D^3Q_\rho^{-3}),\\
 B_{\mathcal N}&=\sum_{\rho\in\mathcal N}
                     (24D^2|Q_\rho|^{-2}+32D^3|Q_\rho|^{-3}).
 \end{split}
\]
The complete result is
\[
 K=L_J+E_J+K_{\mathcal N}+K_{\mathcal P},\quad
 |K_{\mathcal N}|\le B_{\mathcal N},\qquad
 K\ge L_J+K_{\mathcal N}\ge L_J-B_{\mathcal N}.                   \tag{6}
\]
The stronger lower bound in (3) using Jensen can replace \(L_J\) in the lower estimates. The equality in (6) keeps all omitted occurrences, including any nonreal one horizontally between the two endpoints. With an available strip \(|\Im\rho|\le Y\), the possibly adverse collection \(\mathcal N\) lies in the box
\[
 [a-(1+\sqrt2)Y,\ b+(1+\sqrt2)Y]\times[-Y,Y].
\]
It is a finite signed payment on such a slice, uniformly finite for bounded boxes on a compact chart by the uniform count. A supplied enclosure \(n_{\mathcal N}\) for its count and a lower bound \(q_*>0\) for \(|Q_\rho|\) there give \(B_{\mathcal N}\le n_{\mathcal N}(24D^2 q_*^{-2}+32D^3 q_*^{-3})\). A cleared collar separates target and exterior occurrences, and the inequality records the denominator required for a numerical allowance. Without a strip hypothesis (6) still holds with the entire absolutely convergent signed remainder.

For a two-sided estimate the sign information gives no upper payment for \(K_{\mathcal P}\). If an upper bound \(P_*\) for that contribution is supplied, (4) and (6) give
\[
  -B_{\mathcal N}\ \le\ K-L_J\ \le\ A_J+B_{\mathcal N}+P_* .
\]
One way to pay the far part, if using a finite cutoff, is the following direct estimate with the same count input. For \(R_0\ge\max(1,2|a|,2|b|)\) and \(|\rho|>R_0\), \(|Q_\rho|\ge|\rho|^2/4\). This gives the two-sided absolute allowance
\[
 \left|\sum_{|\rho|>R_0,\ \rho\in\mathcal C}
              (24D^2Q_\rho^{-2}+32D^3Q_\rho^{-3})\right|
 \le 384D^2\sum_{|\rho|>R_0}|\rho|^{-4}
       +2048D^3\sum_{|\rho|>R_0}|\rho|^{-6}                      \tag{7}
\]
for either omitted collection \(\mathcal C\) or any subcollection of the exterior. If \(n_t(R)\le C R\log(2+R)\) for \(R\ge1\), the sum with exponent \(p>1\) in (7) is at most
\[
 pC R_0^{1-p}\left(\frac{\log(2+R_0)}{p-1}
                                     +\frac1{(p-1)^2}\right).
\]
This follows by integrating \(p u^{-p-1}(n_t(u)-n_t(R_0))\) from \(R_0\) to infinity and using \(\log(2+u)\le\log(2+R_0)+\log(u/R_0)\). An upper estimate for the complete forcing also needs the retained finite contributions. The lower estimate in (6) spends no upper allowance on the sign-certified collection.

## Scope

The signed finite-head estimate and the explicit complement bound are geometric statements for a known slice. No uniform positive lower bound for an unresolved gap, globally real exterior, or spacetime control of the moving marks is assumed. The exact clock deficit is inherited. The paired mean and second-order remainder compare a correlated input with a rectangular relaxation, and the sector accounts for nonreal omitted occurrences under its stated geometry. The equally informed direct estimator gives the same inequalities. A whole-path application still needs independent control of the signed inputs, target normalization and any adverse exterior on that path.

This is a sufficient finite-head estimate for a single observable. At a true target merger the required \(g>0\) fails, including the atomic collision control. Euler-factor perturbations can preserve the real marks on one slice while changing the complex remainder. Weighted squares and finite-source changes alter normalized coefficients, and finite-prime orbit controls fail full reflection. Reflected and positive-primitive controls lack the canonical square expansion. Fixed-event and finite-profile controls lack the full theta profile or eventual simplicity at the event. The RH-conditional endpoint family fails ordinary Dirichlet arithmetic, and the variable-kernel relaxation fails the physical cosine heat equation. The geometric inequality can hold at cleared control slices where its hypotheses hold. A canonical forcing floor over time has additional inputs. [Premise screen](../research-overview/01_AGC_ST_RESEARCH_OVERVIEW_20261119.md#tests-and-ownership) · [Collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Results index](../../../../../result-summaries/README.md) · [Patterns index](../../../../../avoid/README.md) · [Separate allowances](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
