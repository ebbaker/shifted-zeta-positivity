# Finite product recovery at high rank

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance. The [E11 R1 request](../research-progress/handoffs/AGC_EZ_E11_REQUEST_R1_20261120.md) records gpt-6.2-astra/ultra lead. This derivation was dispatched to gpt-6.2-sol/ultra. This is a fixed-time position estimate using the all-real product of [parent Jacobi Note 07 §3](../../01_jacobi_integer_hierarchy/brainstorm/notes/07_LARGE_TIME_FACTORIZATION_AND_BACKWARD_PROPAGATION_20261120.md) and the [branch anchor section](../manuscript/anchors.tex). The quantitative gains to measure are the interval width in local spacing units and the moment order and precision that buy it. [Result index](../../../../../result-summaries/README.md) · [Patterns index](../../../../../avoid/README.md) · [Target classification](../../../../../avoid/01_restating_the_target.md)

## 1. Bound the products that cross a rank cut

At a fixed all-real anchor write \(F(z)=H_T(z)/H_T(0)=\prod_i(1-b_i z^2)\), \(b_i=x_i^{-2}\), where the positive zeros \(x_i\) are indexed with multiplicity and \(\sum_i b_i<\infty\). Put \(B_j=\prod_{i\le j} b_i\), \(B_0=1\), and \(E_{j,h}=e_j((b_i^h)_i)\) for integer \(h\ge1\). Choose \(\theta_j\in[b_{j+1},b_j]\) for \(j\ge1\) and put
\[
 A_j=\sum_{i\le j}(\theta_j/b_i)^h,\qquad
 C_j=\sum_{i>j}(b_i/\theta_j)^h .
\]
Selecting \(j\) indices deletes exactly as many indices from the first \(j\) as it includes from the tail. Their threshold powers cancel. In particular, with \(a=((\theta_j/b_i)^h)_{i\le j}\), \(c=((b_i/\theta_j)^h)_{i>j}\),
\[
 1\le\frac{E_{j,h}}{B_j^h}
   =\sum_{r=0}^j e_r(a)e_r(c)
   \le\sum_{r\ge0}\frac{(A_jC_j)^r}{(r!)^2}
   \le e^{A_jC_j}.                                                   \tag{1}
\]
The inequality uses \(e_r(a)\le A_j^r/r!\) and its tail analogue, obtained first for a finite tail and then by monotone convergence. The bound uses matched removals and insertions and gives a small error if their product of sums is small.

Suppose \(D_j\ge A_jC_j\) and the finite-input coefficient enclosure is \(0<L_j\le E_{j,h}\le U_j\). Use \(D_0=0\), \(L_0=U_0=1\). From \(x_k^{2h}=B_{k-1}^h/B_k^h\) one obtains
\[
 \left(\frac{L_{k-1}e^{-D_{k-1}}}{U_k}\right)^{1/(2h)}
 \le x_k \le
 \left(\frac{U_{k-1}e^{D_k}}{L_k}\right)^{1/(2h)}.                  \tag{2}
\]
The logarithmic width equals \(\big(D_{k-1}+D_k+\log(U_{k-1}/L_{k-1})+\log(U_k/L_k)\big)/(2h)\).

At a general all-real anchor a counted head through \(J\ge j+1\) can supply interval bounds \(\underline b_i,\overline b_i\). Take a known threshold in \([\overline b_{j+1},\underline b_j]\) whenever that interval is nonempty. Bound \(A_j\) using \(\underline b_i\) and the known part of \(C_j\) using \(\overline b_i\). If \(b_{J+1}\le\beta\le\theta_j\) and \(\sum_{i>J}b_i\le S\), the rest of \(C_j\) is at most \((\beta/\theta_j)^{h-1}S/\theta_j\). Monotonicity supplies \(\beta=\overline b_J\) whenever that value is at most \(\theta_j\), and \(\sum_i b_i=m_2/2\) gives a bound on \(S\) by subtracting the certified lower head sum. A strict split certifies geometric decay for fixed \(j\). Indeed if \(\max(\theta_j/b_j,b_{j+1}/\theta_j)\le q<1\), then \(A_j\le j q^h\) and \(C_j\le q^{h-1}\sum_{i>j}b_i/\theta_j\). At a repeated factor the split can lack a strict margin. The general fixed-rank convergence in the anchor section still applies there, with its older interval when only the moments are available. The growing large-time inverse supplies a finite counted head at a specified \(T\). The asymptotic geometry used for the distant tail comes from a distinct fixed-time theorem.

## 2. High-rank allowance at a fixed positive all-real time

At the comparison time \(T=1/2\), all zeros are real by the known Newman upper bound. Write \(u_n\) for the Polymath clock centers, the solutions of \(g(u_n,1/2)=n\). Their Theorem 1.5(i)–(ii) gives exactly one zero per sufficiently high clock disk and excludes all other sufficiently high zeros. Section 9 gives positional error \(O(u_n^{-c/2}/\log u_n)\) for a fixed \(c>0\). Thus the centers correspond to consecutive ranks up to one fixed shift, and \(g'(x,1/2)\sim\log x/(4\pi)\) gives
\[
 x_i\sim\frac{4\pi i}{\log i},\qquad
 \Delta_i=x_{i+1}-x_i\sim\frac{4\pi}{\log i},\qquad
 x_i/\Delta_i\asymp i.                                             \tag{3}
\]
Only the two-sided bounds and the limiting ratios at \(\lfloor j/2\rfloor,2j\) enter the exchange estimate. The fixed shift is immaterial for this geometry. [Polymath v2, Theorem 1.1 and Theorem 1.5](https://arxiv.org/html/1904.12438v2#S1) · [Proof after (104)](https://arxiv.org/html/1904.12438v2#S9)

For each fixed \(T>0\), Ki–Kim–Lee Theorems 1.3–1.4 give an eventually real simple tail with \(\Delta_i\log x_i\to4\pi\) in the present normalization \(\Xi_\mu(w)=8H_{4\mu}(2w)\). If the full divisor at \(T\) is all real, the eventual indexing differs from the positive product ranks by only a fixed integer. For \(D(x)=x\log x-x\), the mean-value theorem gives \(D(x_{i+1})-D(x_i)\to4\pi\), since \(\Delta_i/x_i\to0\). Telescoping gives \(D(x_i)/i\to4\pi\), and inversion gives \(x_i\sim4\pi i/\log i\) and the rest of (3). This imports the geometry at the chosen time without requiring clock centers or a counted prefix. It requires all-reality as a separate product premise. [Ki–Kim–Lee, Theorems 1.3–1.4](https://doi.org/10.1016/j.aim.2009.04.003) · [Prior primary-passage receipt and normalization](../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/references/07_TND_O_B03_COMPLEX_ZERO_STATISTICS_SOURCE_USE_20261106.md)

For large \(j\) set \(\theta_j=(b_j b_{j+1})^{1/2}\). By (3) the adjacent differences \(\log b_i-\log b_{i+1}\) are at least \(c_0/j\) for \(\lfloor j/2\rfloor\le i\le2j\), with a fixed \(c_0>0\). On the part of the head and tail in this range, the logs of the reciprocal weights before taking power \(h\) are therefore at least \(c_0(r+1/2)/j\), where \(r=j-i\) on the head and \(r=i-j-1\) on the tail. The two sums there are each at most \(e^{-c_0h/(2j)}/(1-e^{-c_0h/j})\).

On the far head each unpowered ratio \(\theta_j/b_i\) is at most a fixed \(q_0<1\), since \(x_{\lfloor j/2\rfloor}/x_j\to1/2\). Thus this part costs at most \(j q_0^h\). On the far tail \(b_i/\theta_j\le q_0<1\) after increasing \(q_0\), since \(x_{2j}/x_j\to2\). Also \(\sum_{i>2j} b_i\ll\log^2(j)/j\) by (3) and the integral of \(\log^2 x/x^2\). As \(\theta_j^{-1}\asymp j^2/\log^2 j\), this part costs at most \(Cj q_0^{h-1}\). For \(h\ge j\) both far bounds are \(O(e^{-c_1 h/j})\) after decreasing \(c_1>0\). Combining with the near sums in (1) shows that for some fixed positive constants, \(D_j=C_2e^{-c_2 h/j}\) is admissible for every sufficiently large \(j\) and \(h\ge j\).

Applying (2) with \(j=k-1,k\) proves that for \(h\ge k\) the interval width in units of \(\Delta_k\) is
\[
 O\!\left(\frac{k}{h}\big(e^{-c_2h/k}+\tau\big)\right),              \tag{4}
\]
provided both coefficients have relative enclosure radius at most \(\tau\le1/4\) about the exact value. The estimate holds at all sufficiently large ranks for each fixed positive all-real \(T\), with a time-dependent onset. The threshold was used to prove an allowance independent of the exact positions, so evaluating the finite-order coefficient requires no exact \(b_i\) or \(\theta_j\). A numerical implementation would need computable geometric constants or the certified split and tail bounds from §1. The asymptotic theorem gives no effective connection to the low counted head and no onset uniform as \(T\) varies.

## 3. Moment interval propagation

Let \(G(v)=F(\sqrt v)=\sum_{m\ge0}(-1)^m a_m v^m\) with \(a_m=m_{2m}/(2m)!\). Use integer \(h\) and \(\omega=e^{2\pi i/h}\). Pairing the factors over roots of unity gives
\[
 \prod_{\ell=0}^{h-1}G(\omega^\ell v)
    =\prod_i(1-b_i^h v^h),\qquad
 (-1)^j E_{j,h}=[v^{jh}]\prod_{\ell=0}^{h-1}G(\omega^\ell v).        \tag{5}
\]
Local absolute convergence of the products justifies regrouping. These coefficients depend only on the coefficients of \(G\) through degree \(N=kh\) for \(j\le k\), since a higher Taylor term cannot contribute to degree \(jh\). All required normalized even moments have order at most \(2kh\).

For \(R>0\) use \(\|P\|_R=\sum_m |[v^m]P|R^m\). Rotation of \(v\) preserves this norm and it is submultiplicative, also in the truncated ring through degree \(N\). If \(\widetilde P\) is the center polynomial assembled from the coefficient intervals, \(d_R\) is their radii summed with the weights \(R^m\), and \(U_R=\|\widetilde P\|_R+d_R\), the telescoping difference of the products in (5) yields
\[
 |\widetilde E_{j,h}-E_{j,h}|
       \le\frac{h U_R^{h-1}d_R}{R^{jh}}.                             \tag{6}
\]
Any additional error evaluating the polynomial coefficient is included in the enclosure of \(\widetilde E_{j,h}\) before using (2). Equation (6) is an absolute interval error bound from the input radii alone. It does not require either a tail integral or a data value at imaginary height.

To bound sufficient precision, use \(M_R=G(-R)=F(i\sqrt R)\), so the exact truncated polynomial has norm at most \(M_R\). If \(d_R\le\eta M_R\), one may use \((1+2\eta)M_R\) for \(U_R\). With \(E_{j,h}\ge B_j^h\) this gives relative radius at most
\[
 h\eta(1+2\eta)^{h-1}\left(\frac{M_R}{R^j B_j}\right)^h .            \tag{7}
\]
Take \(R=(4\pi k/\log k)^2\), which is asymptotic to \(x_k^2\) by (3), and split the exact imaginary-axis product at \(j=k-1,k\). Then
\[
 \frac{M_R}{R^jB_j}=\prod_{i\le j}(1+x_i^2/R)\prod_{i>j}(1+R/x_i^2)
                   \le e^{C_3 k} .                                  \tag{8}
\]
Indeed \(x_i^2/R=O(1)\) for each head factor, and \(\sum_{i>j}R/x_i^2=O(k)\) by (3). Use \(\eta=2^{-p}\) with \(p\ge C_4 kh+\log_2(h/\tau)+O(1)\) to obtain (4), allowing a constant factor in \(\tau\) for converting (6) into interval endpoints. This is a sufficient bit count in the stated norm. Uniform relative radii \(2^{-p}a_m\) per normalized coefficient imply the norm bound, including the weighted low orders. Taking \(\tau=e^{-c_2h/k}\) retains the exact-data error scale. For a prescribed spacing accuracy \(0<\varepsilon\le1/4\), a sufficiently large \(h\asymp k(1+\log(1/\varepsilon))\) and \(\tau\asymp\varepsilon\) suffice, with \(O(kh+\log(1/\varepsilon))\) input bits in this norm. Moment generation and arithmetic cost are separate questions. At a general anchor (6) still applies, and an available certified lower bound for \(B_j\) can be used in (7) to price the relative allowance.

## 4. Comparison and controls

At \(t=1/2\), [Note 13](13_EZ_CLOCK_RANK_20261120.md) supplies the eventual clock rank used to put both approximations on the same zero. With the full published displacement, the clock alone gives \(O(u_k^{-c/2})\) in spacing units once ranks are matched. Equation (4) can be tuned below that proved error scale by paying for higher moments and their precision. For example \(\varepsilon=k^{-A}\) at fixed \(A>0\) costs a sufficient moment order and bit budget of \(O_A(k^2\log k)\) for this product argument. [Note 14](14_EZ_DIRECT_MOMENTS_AT_HIGH_RANK_20261120.md) uses the same coarse clock and the same normalized moments directly. It obtains the prescribed accuracy from the shorter prefix of order \(O(k+\log(1/\varepsilon))\) at sufficient relative precision \(O(k+\log(1/\varepsilon))\) per normalized coefficient. These are demonstrated sufficient budgets for the two constructions.

The estimate is an initialization result at an already all-real time and allows a check on finite information. A cosine lattice and the upper-time atomic \(e^t\cos x+c\) control satisfy the abstract product and split estimates with their own moments and spacing scales. They lack the clock growth in (3). At the atomic double the strict gap premise fails. The controls in the catalogue screen the canonical application as follows.

- Euler-factor controls change the full normalized source. Weighted-square and nonzero finite-tail controls fail the all-real divisor premise at their reported times and at every finite anchor in the proved finite-source class.
- Reflected super-Gaussian and smooth primitive controls lack the complete normalized theta square expansion. The finite-prime orbit and finite-profile controls can preserve a specified finite family of observations while changing the full source or profile. At a nonreal divisor they fail the all-real premise, and at a tested merger the strict split there fails.
- The fixed-event atomic control does not supply the simple high tail of (3) at its threshold. The RH-conditional endpoint control changes ordinary Dirichlet arithmetic, with strict separation failing at the added doubles at time zero.
- The changed-observation controls lack the literal cosine map from the normalized source moments to \(G\). The relaxed three-profile control has fractional masses, which fail the integer-multiplicity premise. The finite canonical-score controls change the complete source despite preserving their fixed score rows and have nonreal zeros by their finite-source theorem.

For any other source meeting the product and quantitative separation assumptions, the representation and bounds apply to its own factors. The result gives an upper-anchor interval. The backward gap law needs a separate time-dependent margin. [Parent control analysis](../../01_jacobi_integer_hierarchy/brainstorm/notes/07_LARGE_TIME_FACTORIZATION_AND_BACKWARD_PROPAGATION_20261120.md) · [Collision catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
