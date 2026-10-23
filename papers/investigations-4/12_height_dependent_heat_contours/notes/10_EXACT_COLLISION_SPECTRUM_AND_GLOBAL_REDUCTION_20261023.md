# Exact collision spectrum and the global upper-bound interface

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Status: **proved elementary finite inequalities and exact information equivalences, with conditional theta applications; no theta spectral upper estimate or new simplicity proportion**. This note was drafted by a separate same-model research agent and requires the program's internal review; no specialist review or priority claim is made.

The local Hermite spectrum is inherited from [Note 06][n6]. The new quantitative conclusions are the sharp improvement **M_0 <= 4q(t)** from its earlier 6q(t) bound, and a two-sided comparison between bounded spectral mass and the frequency of short adjacent gaps. The comparison identifies a concrete missing microscopic estimate, without supplying it. HDC-10 and HDC-11 therefore remain conditional, and HDC-12 remains an assumption audit.

Read the [result index][results], [local heat-geometry register][geometry], [avoid index][avoid], [target-reformulation rule][a01], [control register][controls], [control-premise rule][a02], and [scoped-obstruction rule][a07]. The source and time normalization remain those of [Overview 02][overview]: H_t=-H_zz and 8H(0,z)=xi(1/2+iz/2).

## 1. Complete finite endpoint populations and the exact limit

Fix a finite complete collection of endpoint sites a with multiplicities m_a. Every label at a selected site is included, so N=sum_a m_a. Suppose the selected endpoint sites are real and their positive-time descendants are real and simple for sufficiently small t>0. Write

\[
 L(t)=\sum_{i<j}(x_i(t)-x_j(t))^{-2}(e_i-e_j)(e_i-e_j)^T,
 \qquad q(t)=\operatorname{Tr}\{4tL(t)[I+4tL(t)]^{-1}\}.
 \tag{1}
\]

The finite population need not be the whole zero set. The full field controls its motion; the matrix contains only the selected roots. Put

\[
 M_0=\sum_{m_a\ge2}m_a,\qquad D_0=\sum_a(m_a-1).
\]

Here M_0 counts every label at a nonsimple site, whereas D_0 is the excess multiplicity. They are different quantities.

The inherited local heat law is

\[
 x_{a,j}(t)=a+\sqrt{2t}\,h_{m_a,j}+O(t),
 \tag{2}
\]

where h_{m,j} are the zeros of the probabilists' monic Hermite polynomial He_m. Thus each cluster block of 4tL tends to 2L(h_m). Inter-cluster entries and their diagonal contributions vanish after multiplication by t. The exact limiting spectrum is

\[
 \operatorname{spec}(4tL(t))\longrightarrow
 \bigsqcup_a\{0,1,\ldots,m_a-1\}.
 \tag{3}
\]

For completeness, He_m''-x He_m'+m He_m=0 implies
sum_{j\ne i}(h_i-h_j)^{-1}=h_i/2. Acting with L(h) on the evaluations of the monomial p(x)=x^k gives (k/2)h_i^k plus terms of degree at most k-2. This follows by Taylor expansion of p(h_j) at h_i; the first derivative contributes p'(h_i)h_i/2 and the remaining finite sums have degree at most k-2. The evaluations of degrees 0,...,m-1 form a Vandermonde basis. Hence L(h_m) has spectrum 0,1/2,...,(m-1)/2, proving (3).

Continuity of s/(1+s) on the nonnegative real axis gives the more informative scalar identity

\[
 \boxed{q_0:=\lim_{t\downarrow0}q(t)
       =\sum_a\bigl(m_a-\mathsf H_{m_a}\bigr),
       \qquad \mathsf H_m=\sum_{j=1}^m j^{-1}.}
 \tag{4}
\]

A double contributes 1/2; a triple contributes 7/6; a quadruple contributes 23/12. In particular

\[
 \frac12D_0\le q_0\le D_0,\qquad M_0\le4q_0.
 \tag{5}
\]

The first inequality uses 1/2 <= k/(k+1) < 1 for k>=1. For the second, m-H_m>=m/4 for m>=2: it is equality at m=2 and its increment when m increases is 1-1/(m+1)>=2/3>1/4. The constant 4 is attained by a population consisting of a single double. More generally, the multiplicity of the positive integer k in (3) is the number of endpoint sites with m_a>=k+1, so differences of successive spectral multiplicities recover the numbers of sites of each multiplicity.

Equations (3)-(4) are exact multiplicity encodings, already implicit in Note 06's spectrum; they are not an upper estimate for theta. They hold for a fixed finite population. A growing-height application cannot exchange its height limit with t down to zero without an additional uniform estimate.

## 2. A sharp uniform improvement: M_0 <= 4q(t)

Assume in addition that each adjacent descendant pair from one selected endpoint cluster remains globally adjacent and obeys

\[
 (g^2)'\le8,\qquad g(0)=0,\qquad\hbox{hence}\quad g(t)^2\le8t.
 \tag{6}
\]

For canonical theta this is where **RH first enters this uniform argument**: it supplies the complete real simple system at t>0, and the paired-product calculation in [BW10 Note 19][motion] gives

\[
 (g^2)'=8-4g^2\sum_{r\ne a,b}\frac1{(a-r)(b-r)}\le8.
\]

The sum includes all exterior roots and is absolutely convergent. Global adjacency makes every summand positive. No exterior factor has been set to one. The finite matrix (1) may contain extra edges, which only strengthen the lower comparisons below.

For an even cluster multiplicity partition its labels into adjacent pairs. For an odd multiplicity m>=3, partition into adjacent pairs and one consecutive triple. Retain only the within-pair edges and the two adjacent edges of each triple. Since every retained edge has weight at least 1/(8t),

\[
 4tL(t)\succeq A_*,
 \tag{7}
\]

where A_* is block diagonal, with each pair block equal to one half of the two-vertex path Laplacian and each triple block equal to one half of the three-vertex path Laplacian. Unselected singleton labels have zero blocks. The map f(A)=I-(I+A)^{-1} is operator monotone on positive semidefinite matrices: inversion reverses positive order. Therefore q(t)>=Tr f(A_*).

A pair block has eigenvalues 0,1 and contributes 1/2. A triple block has eigenvalues 0,1/2,3/2 and contributes

\[
 \frac{1/2}{1+1/2}+\frac{3/2}{1+3/2}
 =\frac13+\frac35=\frac{14}{15}>\frac34.
\]

Every block contributes at least one fourth of its number of labels. Consequently

\[
 \boxed{M_0\le4q(t)\quad\hbox{at every covered positive time}.}
 \tag{8}
\]

This improves Note 06's constant 6, which used pairs alone and paid odd clusters by m<=3 floor(m/2). It does not require a new source estimate or an endpoint gap floor. The constant 4 is optimal in this class: H(t,z)=z^2-2t has M_0=2 and q(t)=1/2. The all-simple sufficient threshold remains q(t)<1/2; the improved proportional constant does not lower that threshold.

## 3. Spectral mass versus short adjacent gaps, retaining the deleted diagonals

The next statements are purely finite real geometry and need neither RH nor the heat equation. Let

\[
 y_1<\cdots<y_N,\quad A=L(y),\quad
 B_N(\delta)=\frac1N\#\{1\le i<N:y_{i+1}-y_i<\delta\},
\]
\[
 Q_N(s)=\frac1N\operatorname{Tr}\{sA(I+sA)^{-1}\},\qquad s>0.
 \tag{9}
\]

### Upper bound

Mark every vertex incident to an adjacent gap smaller than delta. If r vertices are marked, then r<=2NB_N(delta). Let G be the unmarked vertices and D the principal submatrix A_GG. Its diagonal still includes interactions with all marked vertices. Those contributions cannot be dropped, and A is not a rank-r perturbation of the graph Laplacian on G.

The unmarked points are delta-separated. Every marked point is also at distance at least delta from every unmarked point: a nearer point on either side would force that unmarked point's nearest original neighbor to be less than delta away. On each side of any unmarked point, the k-th other unmarked point is at least k delta away. Hence

\[
 \sum_{j\in G,j\ne i}|y_i-y_j|^{-2}\le\frac{\pi^2}{3\delta^2}
 \quad(i\in G).
\]

For each marked point b, the nearest unmarked point on either side is at least delta away, and subsequent unmarked points are delta-separated. Therefore the identical estimate holds for sum_{i in G}|y_i-y_b|^{-2}. Summing the first estimate over G and the second over the marked vertices pays the entire principal trace:

\[
 \operatorname{Tr}D
 =\sum_{i\in G}\sum_{j\ne i}|y_i-y_j|^{-2}
 \le\frac{\pi^2 N}{3\delta^2}.
 \tag{10}
\]

Order eigenvalues decreasingly. Cauchy interlacing gives lambda_{j+r}(A)<=lambda_j(D). The top r terms of the bounded filter cost at most r, and f(s lambda)<=s lambda on the remainder. This proves

\[
 \boxed{Q_N(s)\le2B_N(\delta)+\frac{\pi^2s}{3\delta^2}.}
 \tag{11}
\]

The proof is valid if every vertex is marked, when the interlacing remainder is empty; N=1 is immediate. Strict versus non-strict gap boundaries can be handled by a decreasing or increasing delta limit.

### Lower bound

The short adjacent edges form disjoint paths. From K short edges one can select a matching of at least K/2 edges. Each selected edge gives one nonzero Laplacian eigenvalue greater than 2/delta^2. Dropping the other edges and using operator monotonicity yields

\[
 Q_N(s)\ge B_N(\delta)\frac{s}{\delta^2+2s}.
 \tag{12}
\]

In particular, for every a>0,

\[
 \boxed{B_N(a\sqrt s)\le(a^2+2)Q_N(s),\qquad
 Q_N(s)\le2B_N(a\sqrt s)+\frac{\pi^2}{3a^2}.}
 \tag{13}
\]

These explicit bounds control arbitrary exceptional clusters and arbitrarily small internal gaps. No inverse-square moment assumption or minimum gap is hidden in them.

## 4. Exact information equivalences and a quantitative sufficient rate

For any sequence of finite ordered configurations and positive scales s_N,

\[
 \boxed{Q_N(s_N)\longrightarrow0
 \quad\Longleftrightarrow\quad
 B_N(a\sqrt{s_N})\longrightarrow0\quad\hbox{for every fixed }a>0.}
 \tag{14}
\]

The forward implication is the first inequality of (13). For the reverse implication take limsup in the second inequality at fixed a, then let a tend to infinity. The rank index may be replaced by any sequence parameter; N need not literally take every integer value.

For spectral tightness define E_N(K)=N^{-1}#{lambda(A)>=K}. The same matching and principal-compression argument gives

\[
 B_N(\delta)\le2E_N(2/\delta^2),\qquad
 E_N(K)\le2B_N(\delta)+\frac{\pi^2}{3K\delta^2}.
 \tag{15}
\]

Consequently

\[
 \lim_{K\to\infty}\limsup_N E_N(K)=0
 \quad\Longleftrightarrow\quad
 \lim_{\delta\downarrow0}\limsup_N B_N(\delta)=0.
 \tag{16}
\]

This proves, for these one-dimensional inverse-square Laplacians, that empirical spectral tightness is exactly absence of a limiting atom at zero in the adjacent-spacing distribution. A mean density or one-point zero count gives neither side. Equation (16) is an information equivalence, not an established statement about theta. Equation (14) is weaker than full fixed-scale tightness when s_N tends to zero; it asks only for the shrinking scales sampled by the filter.

There is a usable rate if independent complete-source information supplies

\[
 B_N(\delta)\le C\delta^\beta+\varepsilon_N
 \quad(0<\delta\le\delta_0),\qquad \beta>0.
 \tag{17}
\]

For s_N small enough that delta=s_N^{1/(beta+2)} lies in that range, (11) yields

\[
 Q_N(s_N)\le
 \left(2C+\frac{\pi^2}{3}\right)s_N^{\beta/(\beta+2)}
 +2\varepsilon_N.
 \tag{18}
\]

This is a quantitative sufficient input, classified as such; no value of beta, C, or epsilon_N has been established here for theta. A truncated pair upper estimate that counts every adjacent pair can supply (17), but real-only pair data do not cover a complex-root population, and a lower pair estimate cannot supply this upper bound.

## 5. Global assembly and the missing theta estimate

Let a growing endpoint target contain N_h labels, counting multiplicity. Cover all but r_h labels by selected complete endpoint clusters; if a spatial cut splits a cluster, pay every excluded label explicitly. Track the selected n_h=N_h-r_h labels to one source-prescribed positive time t_h. Let nu_h>0 be the declared density normalization and put

\[
 y_i=\nu_h x_i(t_h),\quad A_h=L(y)=\nu_h^{-2}L(x(t_h)),
 \quad s_h=4t_h\nu_h^2.
 \tag{19}
\]

No derivative of nu_h is used in this slice-wise argument. Equation (1) is then n_h Q_{n_h}(s_h). Under the complete canonical RH-dependent dynamics of Section 2,

\[
 \boxed{\frac{M_h}{N_h}\le\frac{r_h}{N_h}
 +4\frac{n_h}{N_h}Q_{n_h}(s_h).}
 \tag{20}
\]

Thus r_h=o(N_h) and the microscopic adjacent-gap estimate

\[
 \frac1{n_h}\#\{i:x_{i+1}(t_h)-x_i(t_h)
                    <2a\sqrt{t_h}\}\longrightarrow0
 \quad\hbox{for every fixed }a>0
 \tag{21}
\]

would imply density-one simplicity under RH. Equation (21) is equivalent to the desired q/n_h upper estimate by (14). It is **not** obtained from RH or from the present analysis. The mean-density normalization cancels in (21), clarifying that the actual unpaid scale is sqrt(t_h). If s_h tends to zero, uniform tightness in (16) is a stronger sufficient alternative. If (17) is proved, (18) and (20) give the explicit proportional rate, with a separately paid coverage loss.

This is the exact HDC-10/HDC-11 interface. It avoids a stronger inverse-square trace hypothesis, but does not claim that its source proof is easier. Source-prescribed times are indispensable: choosing them after resolving the unknown endpoint gaps only rephrases simplicity. The all-simple route still needs q<1/2 on complete covering blocks, and an o(N) bound does not imply it.

### Published high-height clocks saturate this filter

**Imported facts, checked against the primary source.** [Polymath, Theorem 1.5 and its Section 9 proof after equation (104)](https://arxiv.org/html/1904.12438) give complete real simple high zeros for 0<t<=1/2 after an onset exp(C/t). The clock centers xi_n solve g(xi_n,t)=n, where

\[
 g(x,t)=\frac{x}{4\pi}\log\frac{x}{4\pi}-\frac{x}{4\pi}
        +\frac{11}{8}+\frac{t}{16}\log\frac{x}{4\pi}.
\]

The theorem statement displays a coarser error; its proof establishes the uniform sharper location bound

\[
 |r_n(t)-\xi_n(t)|\le K\frac{\xi_n^{-ct}}{\log\xi_n}.
 \tag{22}
\]

Here c,K are absolute constants. The one-zero disks and the converse localization identify every zero in the high region, after enlarging the absolute onset constant. Constants are not numerically specified. The finer Theorem 1.3 Riemann--Siegel formula also applies at small t, but does not by itself bound microscopic gaps.

**Deduction from those facts.** Take consecutive clock centers in [X,2X], with X>=exp(C_0/t), C_0 sufficiently large, and the complete corresponding N-root block. Enlarging C_0 also pays the rank-onset condition in Theorem 1.5(ii). Put

\[
 \nu_X=g_x(X,t)=\frac1{4\pi}\log\frac{X}{4\pi}+\frac{t}{16X},
 \qquad s=4t\nu_X^2.
\]

The derivative g_x is increasing on this high interval. The mean value theorem bounds every clock gap by 1/nu_X. Paying both location errors in (22), uniformly over the whole block, gives

\[
 r_{n+1}-r_n\le\frac1{\nu_X}
          +\frac{2KX^{-ct}}{\log X}
 \le\frac{C_g}{\nu_X}.                                  \tag{23}
\]

For example C_g=2 is valid after enlarging C_0 until
2K(nu_X/log X)exp(-cC_0)<=1; nu_X/log X is uniformly bounded. This uses the log denominator in the **proved** root error. The theorem statement's coarser O(X^(-ct)) error alone would not justify (23) uniformly at onset. The published disjoint one-zero disks provide another direct route to a fixed C_g. No temporal derivative of the root-location remainder has been taken.

Let P_N be the unweighted path Laplacian. Keeping only consecutive edges in the actual population proves

\[
 L(r)\succeq\frac{\nu_X^2}{C_g^2}P_N,
 \qquad \operatorname{spec}(P_N)
 =\{4\sin^2(\pi k/(2N)):0\le k<N\}.
\]

The eigenvalues follow by applying P_N to the discrete cosine vectors cos(pi k(j-1/2)/N), 1<=j<=N. Inverse order and the decreasing function
f(u)=[1+(4s/C_g^2)sin^2(pi u/2)]^(-1) now yield

\[
 \frac{N-q}{N}\le\frac1N\sum_{k=0}^{N-1}f(k/N)
 \le\frac1N+\int_0^1f(u)\,du
 =\frac1N+\frac1{\sqrt{1+4s/C_g^2}}.
\]

The integral is elementary after theta=pi u/2 and v=tan theta. Consequently

\[
 \boxed{1-\frac1N-\frac1{\sqrt{1+4s/C_g^2}}
      \le\frac qN\le1-\frac1N.}                         \tag{24}
\]

Thus for growing blocks with s tending to infinity, q/N tends to **one**, its maximal large-rank value. This is a deterministic spectral consequence proved here, not an endpoint multiplicity conclusion. The high-height theorem supplies its actual-theta hypotheses without RH.

Indeed s is asymptotic to t log^2 X/(4pi^2). The onset t log X>=C_0 forces s to infinity along growing heights, while the earlier tightness-based sufficient route asks for s to tend to zero. In that microscopic regime t log X tends to zero and the imported error form X^(-ct) is not small. The stronger conclusion (24) shows that applying the currently published clock regime **directly** to the unmodified q cannot establish q=o(N): q is nearly saturated even though these positive-time zeros are simple. It does not exclude backward transport after subtracting a matched reference and paying its complete residual, or a new complete-source microscopic estimate. Completeness of the endpoint labels at t=0 is a separate obligation for any simplicity application; the late block statement alone supplies none.

## 6. Information-class controls and assumptions without RH

**Hermite and double controls.** They satisfy the heat equation, real descendant dynamics and the finite inequalities. Their limits (4) are positive. They falsify any universally vanishing q conclusion based only on that information. The double attains the constant in (8); a triple checks why the pair-only constant 6 was avoidable.

**Simple quadratic and nonuniform limits.** For H(t,z)=z^2-a^2-2t, a>0,

\[
 q(t)=\frac{2t}{a^2+4t}.
\]

Every fixed a has q(t) tending to zero, but a sequence a_h^2=o(t_h) has q(t_h) tending to 1/2. Therefore endpoint simplicity plus local heat analyticity supplies no uniform vanishing estimate for an arbitrarily prescribed time schedule. This obstruction is to that information class and limit exchange, not to complete-theta estimates.

**A growing-rank real configuration control.** Put y_{2k-1}=k and y_{2k}=k+epsilon_N for k=1,...,N/2, with epsilon_N down to zero. Its one-point count has fixed positive mean density, while B_N(delta) tends to 1/2 for every fixed small delta>0. At least N/2 eigenvalues are at least 2/epsilon_N^2. Thus mean density alone does not imply (16). This is a finite-configuration example, not asserted to be a theta heat slice.

**Sine/cosine field.** A stationary equally spaced root set, such as H(t,z)=e^t sin z, has B_N(delta)=0 below its spacing and bounded normalized spectra, consistently with (11). Finite-block evolution must still retain the exterior unit; this example does not license deleting exterior forces.

**Registered source controls.** The [control register][controls] distinguishes their premise failures. Euler-factor controls change the canonical Dirichlet coefficients and can have positive Newman threshold; they cannot be assigned the canonical all-real interval without proof. Weighted-square controls lack full reflection and have no all-real heat time; reflected and positive-primitive controls lack the canonical integer-square coefficient data, and an all-real global interval has not been supplied for them. Finite-prime controls fail full reflection. RH-conditional normalized endpoint controls do have real positive-time descendants and pass the generic spectral implications while retaining an endpoint double; ordinary Dirichlet-series arithmetic fails. Smooth-shape, source-positivity, primitive-positivity and fixed finite observation premises therefore do not by themselves establish the unpaid small-gap upper bound. A sparse added double need not violate a density-one estimate; those controls screen the all-simple threshold, not automatically every averaged claim. The large-density Hermite/configuration controls separately screen a universal averaged conclusion in their stated classes. No assertion is made that each registered control violates every possible quantitative input.

**RH-free boundary.** Sections 3-4 use only distinct real numbers. The local Hermite computation at a real multiple endpoint does not require RH if local reality is otherwise proved. Section 2 and the canonical use of Section 5 require the complete real-root gap law, supplied here by RH; real selected roots alone do not control a possibly complex exterior population. Late real anchors do not repair this implication. For instance H(t,z)=z^2+a^2-2t has a real simple late slice but two simple nonreal roots at t=0, and q(t)=2t/(4t-a^2) tends to zero as t tends to zero. A vanishing multiplicity signature does not establish endpoint reality. Across complex slices L is no longer Hermitian positive semidefinite, and the order/interlacing arguments in this note do not apply. HDC-12 still needs an independent endpoint-reality theorem or a complete nonreal-root count.

The actual gains are the constant 6 to 4 in the finite transfer and the explicit two-sided gap/filter bounds. The outstanding task is an independent complete-theta proof of (21), or a stronger estimate with a usable rate such as (17), together with declared all-height coverage. These findings do not finish HDC-10, HDC-11, or the RH-free program.

[n6]: 06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md
[overview]: ../research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md
[motion]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
