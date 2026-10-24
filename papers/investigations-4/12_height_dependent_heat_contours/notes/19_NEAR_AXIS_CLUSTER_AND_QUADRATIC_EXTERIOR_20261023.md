# A complete near-axis cluster comparison with exterior curvature

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Derived and checked by separate agents using the same model; this is internal research, not independent specialist validation. No priority claim is made.

## Result and place in the program

This note continues the [arithmetic-inside-contours overview](../research-overview/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRAM_20261023.md) and its [progress register](../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md), taking the near-axis branch. Under RH, retaining every zero in a fixed-radius cluster and the quadratic term of its exterior analytic factor gives a complete comparison at spatial scale $1/\log Y$ and backward time $1/(\log Y)^2$. The additive error is $O((\log Y)^{-1/2})$ times the actual absolute Gaussian integral of the quadratic model, uniformly even when the cluster degree is $O(\log Y)$. A real-rooted polynomial control shows that dropping the quadratic exterior term can leave an order-one error in this information class.

This is a proved supporting estimate, not an RH-equivalent criterion, a relative error against the model's value, or a multiplicity-restricting arithmetic estimate. It extends the *domain of comparison* beyond [book.tex](../manuscript/book.tex), Theorem 1.1; it does not extend that theorem's nonvanishing conclusion through a possible multiple zero. The all-multiple control in the book passes the new estimate. The positive arithmetic goal remains open.

The [result index](../../../../result-summaries/README.md), [local-geometry summary](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../avoid/README.md), [target classification](../../../../avoid/01_restating_the_target.md), [shared-premise screening](../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md) govern this distinction. The [review](../reviews/16_BOOK_AND_NEAR_AXIS_CLUSTER_REVIEW_20261023.md) records the manuscript audit and checks of this result. All manuscripts were left unchanged.

## Complete cluster and explicit model

Use $F(z)=H(0,z)=\xi(1/2+iz/2)/8$, with $H_t=-H_{zz}$. Assume RH, retaining multiplicity. The book supplies the paired order-one product, the local $O(\log Y)$ zero count, a fixed-positive-offset logarithmic bound, and the complete Gaussian identity

\[
 H(-s,z)=\mathbb E F(z+u),\qquad u\sim N(0,2s).
\]

Fix $r,K,c>0$, put $L=\log Y$, and let $a\in[Y,2Y]$. Retain **all** signed zeros with $ |\lambda-a|\le r$, repeated with multiplicity:

\[
 P(v)=\prod_{|\lambda-a|\le r}(v-(\lambda-a)),\quad
 m=\deg P,\quad U(v)=\frac{F(a+v)}{P(v)}.
\]

Removable values are filled in. Thus $U(0)\ne0$, even if $a$ is a multiple zero. The exterior data are

\[
 A=\frac{U'(0)}{U(0)}\in\mathbb R,\qquad
 B=(\log U)''(0)
   =-\sum_{|\lambda-a|>r}\frac1{(a-\lambda)^2}\le0.
\]

Uniformly, $m\le C_rL$ and $|A|+|B|\le C_rL$. For

\[
 0\le s\le cL^{-2},\qquad |w|\le KL^{-1},\qquad d=1-2sB\ge1,
\]

define the quadratic-exterior comparison

\[
 Q_s(w)=U(0)d^{-1/2}
 \exp\!\left(\frac{Aw+Bw^2/2+sA^2}{d}\right)
 \left(e^{(s/d)\partial_v^2}P\right)
       \left(\frac{w+2sA}{d}\right).                       \tag{1}
\]

The differential exponential is a finite series on $P$. Exterior real zeros reduce the effective polynomial heat time to $s/d\le s$. Their influence has not been discarded or replaced by a selected set of roots.

To state the error without assuming a floor, put

\[
 \mu=\frac{2s(A+B\Re w)}d,\quad \sigma=\sqrt{\frac{2s}d},\quad
 M=d^{-1/2}\exp\!\left(A\Re w+\frac B2\Re(w^2)
                    +\frac{s(A+B\Re w)^2}d\right).
\]

Here $\mu,\sigma$ are real. Define the absolute Gaussian envelope

\[
 \mathcal E_s(w)=|U(0)|M\mathbb E|P(w+\mu+\sigma X)|,
 \qquad X\sim N(0,1).                                    \tag{2}
\]

**Theorem.** There are constants $C,\kappa>0$, depending on the fixed parameters and the book's initial estimates, such that for all sufficiently large $Y$,

\[
 |H(-s,a+w)-Q_s(w)|
 \le C\left(\frac{(m+1)^{3/2}}{L^2}+e^{-\kappa L^2}\right)
                  \mathcal E_s(w).                       \tag{3}
\]

The factor in parentheses is $O(L^{-1/2})$ for $m\le C_rL$, and $O(L^{-2})$ at bounded degree. Uniformity includes the zero locations, internal gaps and multiplicities. No lower bound for $P,Q_s,F$, or $H$ is assumed. Time is real. No estimate of derivatives of (3), nor complex-time extension, is asserted.

The scale in (2) is the integral of the absolute value of the model integrand, not the absolute value $|Q_s(w)|$ of its possibly cancelling integral. For $s>0$ it is positive. At $s=0$, use $\mu=\sigma=0$; the quadratic initial approximation need not equal $F(a+w)$ away from $w=0$. Expanding $P(w+\mu+\sigma X)=\sum c_kX^k$ gives the optional, larger coefficient bound $\mathcal E_s(w)\le |U(0)|M\sum|c_k|\mathbb E|X|^k$; the theorem does not require that additional loss.

## Proof: exterior estimates and the entire tail

The book's zero count bounds the number of roots in each fixed-length interval at height $v$ by $O(\log(2+|v|))$. Grouping exterior roots by their distance from $a$ gives

\[
 S_j=\sum_{|\lambda-a|>r}|a-\lambda|^{-j}=O_{r,j}(L),
 \qquad j\ge2.                                           \tag{4}
\]

Let $q=U'/U$. At any fixed $b>0$,

\[
 q(ib)=p(a+ib)-\sum_{|\lambda-a|\le r}
                  \frac1{ib-(\lambda-a)}=O(L),\qquad p=F'/F.
\]

On the segment from (0) to $ib$, $|q'|\le S_2$; integration proves $A=O(L)$. Reality gives $A\in\mathbb R$, while $B=-S_2$. On $|v|\le r/2$, the absolutely convergent exterior sum gives $q''(v)=O_r(L)$. Therefore the analytic logarithm continued from zero satisfies

\[
 \log\frac{U(v)}{U(0)}=Av+\frac B2v^2+R_3(v),\qquad
 |R_3(v)|\le C_rL|v|^3.                                  \tag{5}
\]

A local Taylor bound alone would not pay the complete Gaussian tail. Translate the order-one Hadamard product and remove the finite cluster to obtain

\[
 \frac{U(v)}{U(0)}=e^{Av}\prod_{|\lambda-a|>r}
 \left(1+\frac{v}{a-\lambda}\right)e^{-v/(a-\lambda)}.     \tag{6}
\]

The product converges locally uniformly by (4); each displayed factor has zero logarithmic derivative at zero, so its linear exponential coefficient is exactly $A$. The elementary inequality

\[
 |1+t|\le \exp(\Re t+|t|^2/2)
\]

follows from $1+x\le e^x$ applied to $x=2\Re t+|t|^2\ge-1$. It yields, for **every** complex $v$,

\[
 \left|\frac{U(v)}{U(0)}\right|
 \le e^{A\Re v+S_2|v|^2/2},\qquad
 \left|\frac{U(v)}{U(0)e^{Av+Bv^2/2}}\right|
 \le e^{S_2(\Re v)^2}.                                   \tag{7}
\]

Thus the full exterior factor costs a quadratic exponent of size $O(L)$, while the Gaussian precision is of order $L^2$. This remains valid across the exterior zeros and arbitrarily far from the cluster. There is no division by the vanishing cluster polynomial in the estimate of the field.

## A Gaussian polynomial lemma

Let $R$ be a nonzero complex polynomial of degree at most $m$, $n=m+1$, $X\sim N(0,1)$, and $N=\mathbb E|R(X)|>0$. Write $\phi$ for the standard Gaussian density. There is an absolute $C$ such that

\[
 \frac{|R(x)|\phi(x)}N\le Ce^{-x^2/8},\qquad |x|\ge4\sqrt n. \tag{8}
\]

For fixed $j\ge0$, $0\le t\le1/16$, and $h\ge4\sqrt n$, it follows that

\[
 \frac{\mathbb E[|R(X)|(1+|X|)^je^{tX^2}]}N
       \le C_jn^{j/2}e^{16tn},\qquad
 \frac{\mathbb E[|R(X)|e^{tX^2}1_{|X|\ge h}]}N
       \le Ce^{-h^2/32}.                                \tag{9}
\]

Here is an elementary proof, including the complex-coefficient case. Set $b=\sqrt n$, $S=\max_{[-b,b]}|R|$, and expand $R(b\cos\theta)=\sum_{k=0}^ma_k\cos(k\theta)$. The cosine integral formulas imply $|a_0|\le S$, $|a_k|\le2S$, so the derivative in $\theta$ is at most $n^2S$. Around a maximum, an angular interval of length $1/(4n^2)$ has modulus at least $3S/4$. Its image under $x=b\cos\theta$ has length at least $cb/n^4$, even at an endpoint. The Gaussian density on $[-b,b]$ is at least $ce^{-n/2}$. Thus

\[
 N\ge cS n^{-7/2}e^{-n/2}.
\]

The same expansion is the polynomial identity $R(by)=\sum a_kT_k(y)$. For $|y|\ge1$, the elementary Chebyshev formula gives $|T_k(y)|\le(2|y|)^k$; the resulting geometric sum yields $|R(x)|\le4S(2|x|/\sqrt n)^m$. If $v=|x|/\sqrt n\ge4$, then

\[
 n/2+m\log(2v)-x^2/2
 \le n\{1/2+\log(2v)-v^2/2\}\le-x^2/4.
\]

Consequently $|R(x)|\phi(x)/N\le Cn^{7/2}e^{-x^2/4}\le Ce^{-3x^2/16}$, since $n^{7/2}\le Ce^n$ and $x^2\ge16n$. This proves (8). Splitting the first integral in (9) at $4\sqrt n$, and using $t\le1/16$ in its tail, proves its first assertion; the same Gaussian tail bound proves the second. The constants include degrees zero and one. No polynomial norm comparison is imported.

## Proof: Gaussian comparison in the absolute envelope

Integrating $U(0)P(w+u)e^{A(w+u)+B(w+u)^2/2}$ against the Gaussian gives (1). One may verify this for each monomial by finite Gaussian moment differentiation; it requires no contour translation for the original field.

For its absolute weight, completion of the **real** square gives exactly

\[
 \mathbb E_u\!\left[e^{A\Re(w+u)+(B/2)\Re((w+u)^2)}f(u)\right]
       =M\mathbb E_X f(\mu+\sigma X).                    \tag{10}
\]

This is the origin of (2). In particular, the real tilted mean $\mu$ in (10) is distinct from the complex argument $(w+2sA)/d$ in (1). Uniformly,

\[
 1\le d\le1+C/L,\quad |w+\mu|\le C/L,\quad
 \sigma\le C/L,\quad |v|\le C(1+|X|)/L,
 \qquad v=w+\mu+\sigma X.
\]

On $|v|\le r/2$, (5) and $|e^R-1|\le|R|e^{|R|}$ give

\[
 |e^{R_3(v)}-1|
 \le \frac{C}{L^2}(1+|X|)^3e^{C(1+X^2)/L}.              \tag{11}
\]

For the exponential bound use $|v|^3\le(r/2)|v|^2$ on this local disk. We do not integrate a cubic exponential over the whole real line.

For $s>0$, apply (9) to the nonzero polynomial $R(X)=P(w+\mu+\sigma X)$, with $j=3$, $t=C/L$ and $n=m+1\le C'_rL$. The exponential $e^{16tn}$ stays uniformly bounded. Equations (10)–(11) therefore give the local error $C(m+1)^{3/2}L^{-2}\mathcal E_s(w)$.

On $|v|>r/2$, sufficiently large $L$ implies $|X|\ge\kappa_0L\ge4\sqrt n$. By (7), the sum of the exact and quadratic absolute integrands, relative to the weight in (10), is at most $2e^{C(1+X^2)/L}$. The tail assertion in (9) pays this entire contribution by $Ce^{-\kappa L^2}\mathcal E_s(w)$. This proves (3) for $s>0$. At $s=0$, (5) gives the result directly. If $P(w)=0$, both the actual field and the model vanish and $\mathcal E_0(w)=0$; the statement is $0\le0$, without division. This completes the proof.

## A precise failure of the linear exterior approximation

This control concerns the local degree/exterior-derivative information class, not the unchanged theta source or its global count. Fix $R>r$. Take even $m=m_L$ and integers $n=n_L$ with $m/L\to\mu_0>0$, $n/L\to\nu_0>0$, and set

\[
 F_L(v)=v^m(1-v^2/R^2)^n,\qquad s=c/L^2.
\]

All roots are real, the local cluster is $P=v^m$, and the exterior coefficients are $A=0$, $B=-2n/R^2=O(L)$. At $w=0$, the linear-exterior model is $\mathbb E_u u^m$. Under the probability measure proportional to $u^me^{-u^2/(4s)}du$, $u^2/(2s)$ is chi-square with $m+1$ degrees of freedom. Therefore $nu^2/R^2\to2c\mu_0\nu_0/R^2$ and $nu^4\to0$ in probability. Uniform integrability follows from

\[
 \mathbb E\bigl|(1-u^2/R^2)^n\bigr|^2
 \le\mathbb E e^{2nu^2/R^2}
 =(1-8sn/R^2)^{-(m+1)/2}=O(1).
\]

Consequently

\[
 \frac{(e^{s\partial_v^2}F_L)(0)}{(e^{s\partial_v^2}v^m)(0)}
 \longrightarrow e^{-2c\mu_0\nu_0/R^2}\ne1.               \tag{12}
\]

The quadratic model has ratio $(1+4sn/R^2)^{-(m+1)/2}$, with precisely the limit in (12). A uniform $o(1)$ linear-exterior error therefore fails for this declared growing-degree class. Bounded degree, additional cluster information and other theta-specific approximations are outside this conclusion.

The small [exact-rational diagnostic](../numerics/10_check_quadratic_cluster_20261023.py) evaluates the finite Gaussian moments for $m=n=L$, $R=2$, $c=1$, $L=16,32,64,128,256$; its [record](../numerics/10_QUADRATIC_CLUSTER_DIAGNOSTIC_20261023.json) retains exact ratios. At $L=256$, the full/linear ratio is approximately $0.605641$, while the quadratic model's relative error is about $0.000493$. The limiting ratio is $e^{-1/2}$. Decimal square roots and exponentials are floating displays; the analytical proof, not this finite sample, establishes the limit. These are polynomial-control data, not theta-zero data.

## What this pays, and what still requires arithmetic

The comparison pays the interaction of the complete exterior factor with a possibly large local cluster, including the full Gaussian tail. It gives a finite polynomial reference with a vanishing additive error and permits the multiple zero being investigated. Direct Gaussian integration using only a linear exterior carrier has the order-one failure (12); retaining the quadratic carrier fixes that specific approximation loss.

It does not bound the absolute Gaussian envelope relative to the model on a useful contour. Cancellations can make $\mathcal E_s(w)$ much larger than $|Q_s(w)|$. Thus (3) alone supplies neither a root count, an earlier-nonreal population bound, nor a bound on the complete resource $\mathcal R_Y$. The canonical inputs consumed here are RH, the complete product, local count, logarithmic anchor and exact Gaussian identity; the Euler anchor has only paid a coarse $O(L)$ bound.

The book's $G_0=F(z/2)^2[1+\cos((\log2)z/4)]$ has those same inputs and satisfies every estimate above, while having no simple zeros. This explicitly screens the inequalities actually used. The other [registered controls](../../../../result-summaries/12_collision_controls_and_screening.md) must be assessed at their declared initial slice: positivity, square support, reflection or a positive primitive do not by themselves supply the all-real initial product and count hypotheses. A control with nonreal initial zeros fails that premise; a control satisfying the hypotheses is admitted, not excluded, by this transfer theorem. None of this establishes a universal obstruction to complete theta arithmetic.

For clarity, the named registered families are screened at the hypotheses actually consumed:

| Family | Premise check for this transfer estimate |
| --- | --- |
| Euler-factor \(F(z)(1+c\cos az)\) | For \(0<c<1\), the added zeros are nonreal, so the initial all-real premise fails. Under RH with \(c\ge1\), all added zeros are real, and the local count, fixed-strip logarithmic orders and Gaussian identity pass; no collision exclusion follows. Its exact canonical theta source is absent. |
| Finite weighted-square controls | The finite-source audit in the cited summary proves they have nonreal zeros at every real heat time. The initial all-real premise fails, even though selected reflection endpoints and positivity hold. |
| Reflected super-Gaussian control | Full reflection and positivity do not supply the unchanged integer-square theta source. This review does not establish the required high-height local count and all-real initial slice for that control; it therefore makes no application or rejection claim for inequality (3). |
| Smooth shape and positive-primitive controls | Their positive auxiliary primitive and endpoint data do not impose the canonical square expansion. The complete initial-product/count hypotheses must be checked for a chosen slice before applying (3); these controls are not excluded by positivity or primitive data. |

The absent canonical identities in the last two rows are not covert hypotheses used in the proof of (3). The table records the distinction between a failed premise, an admitted control, and premises not verified here. The explicit all-multiple \(G_0\), which passes every premise, is the decisive screen for any attempted simplicity inference from this estimate.

There is an additional useful check on $G_0$: all its cluster multiplicities are even, so $P(v)\ge0$ for real $v$ and $U(0)>0$. For real $w$ and $s>0$, its quadratic model integrand is nonnegative, and $\mathcal E_s(w)=Q_s(w)>0$. Thus even a genuine relative comparison on this real near-axis line is compatible with a field having no simple endpoint zeros. The missing discrimination is not merely an artifact of a loose norm.

The next substantive question is whether the *actual* cluster polynomial and exterior data admit a multiplicity-sensitive bound that changes the conclusion for theta while failing on $G_0$. A model-boundary comparison must pay cancellation in its Gaussian integral as well as the complete-field error; an estimate of the resource must still retain earlier mass and one-sided end influx. Those estimates have not been acquired here, and no simplicity goal is marked complete.
