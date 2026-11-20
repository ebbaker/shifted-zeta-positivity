# AGC-JH-E02 r1 — signed degree increment and physical-time compatibility

19 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. Recorded helper dispatch gpt-6.2-sol,
effort ultra. This is dispatch provenance, without independent backend
attestation. Lead settings are unavailable in the canonical public-history
metadata. Derivation and one internal correction check under
[request r1](../research-progress/handoffs/AGC_JH_E02_REQUEST_R1_20261119.md).

| Next task | Type | Recommended model | Dependency | Expected output |
| --- | --- | --- | --- | --- |
| AGC-JH-B02 | B | Astra/ultra | Assess E01 and E02 | Decide whether a source-conditioned signed allowance can give a complete margin against direct evaluation. |

**Status:** exact infrastructure and conditional allowances for one fixed
chart. The input requirements remain symbolic. Read the
[result index](../../../../../result-summaries/README.md) and
[patterns index](../../../../../avoid/README.md), particularly
[collision controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[target classification01](../../../../../avoid/01_restating_the_target.md),
[premise screening02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [joint errors12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The interface establishes no canonical numerical margin or degree sign.

## 1. Chart and a finite acquisition formula

Use the complete theta cosine field, normalized as $F_t=2H(t,\cdot)/Z_t$,
and real physical time in a compact interval $I\subset[0,1/2]$. Write
$G_-=G_{N,t}$, $G_+=G_{N+2,t}$ for the moving canonical Jacobi heads,
$N\ge2$. Their residuals are
$$
 R_j=(\partial_t+\partial_z^2+\beta_1)G_j
    =\beta_j\beta_{j-1}\partial_{\beta_{j-1}}G_j
 \quad (j=N,N+2).
\tag{1}
$$
Here and below subscripts $-,+$ on quantities label degree, whereas the
two roots of a given field are denoted $\zeta_{j,1},\zeta_{j,2}$. Put
$\delta X=X_+-X_-$, $B_j=\partial_z G_j/G_j$, $U_j=R_j/G_j$,
and $V_j=G_{j,zz}/G_j$. The positively oriented circle is
$\Gamma=\{|z-a|=r\}$, $a\in\mathbb R$, with a common open zero-free
collar and exactly two zeros of each field inside, with multiplicities.
They obey $|\zeta_{j,k}-a|\le r-b$, $0<b\le r$. Set
$$
 \langle f\rangle=\frac1{2\pi i}\oint_\Gamma f(z)\,dz,
 \quad w_j=z-c_j,\quad Q_j=w_j^2-D_j,
 \quad g=2r-b,\quad d_*=(r-b)^2 .
$$
On the circle both root distances are at least $b$, hence
$|Q_j|\ge b^2$, $|w_j|\le g$, and $|D_j|\le d_*$. The coordinates
are real and analytic in physical time even at a target double.
These hypotheses require independent acquisition on the selected chart.

Let $L_j=(-1)^j(\prod_{k=1}^j\beta_k)z^{2j}/(2j)!$ and use the
complete error laws $F_t-G_{j,t}=L_jE_j$ of
[VCD error law](../../../03_volterra_coefficient_dynamics/manuscript/sections/error_law.tex).
For $A_j=\beta_{j+1}z^2/[(2j+1)(2j+2)]$, add the consecutive
[VCD degree increments](../../../03_volterra_coefficient_dynamics/manuscript/sections/zero_geometry.tex).
Their $E_{N+1}$ terms cancel since $L_{N+1}=-A_N L_N$. The
signed, shared increment is
$$
 d_G:=G_+-G_-=L_N(E_N-A_NA_{N+1}E_{N+2}).
\tag{2}
$$
The characteristic laws in (2) belong to the same source and time.
With $|E_j-1|\le e_j$, a complex pointwise enclosure for
$d_G/L_N$ is the disk centered at $1-A_NA_{N+1}$ with radius
$e_N+|A_NA_{N+1}|e_{N+2}$. The expression extends at $z=0$.
Use a law's own strip and time hypotheses when acquiring $e_j$.

There is a wholly finite expression for this same increment. Let
$P_j(\xi)=\det(\xi-J_j)$ and $m_j(\xi)=((\xi-J_j)^{-1})_{00}$.
On adding a final site the Schur complement and the endpoint
resolvent entry from [VCD gap transport](../../../03_volterra_coefficient_dynamics/manuscript/sections/gap_transport.tex) give
$$
 m_{j+1}-m_j=\frac{h_j^*}{P_jP_{j+1}},
 \qquad h_j^*=\prod_{k=1}^j\beta_k .
$$
Indeed the change is $\beta_j((\xi-J_j)^{-1})_{0,j-1}^2/
[\xi-\beta_j((\xi-J_j)^{-1})_{j-1,j-1}]$, where the squared
entry is $h_{j-1}^*/P_j^2$ and the bracket is $P_{j+1}/P_j$.
Summing the two rational increments uses
$P_{N+2}+\beta_{N+1}P_N=\xi P_{N+1}$. Therefore on a spectral
contour $\Sigma$ enclosing both node lists,
$$
 d_G(t,z)=\frac{h_N^*}{2\pi i}
       \oint_\Sigma\frac{\xi e^{iz\xi}}{P_N(\xi)P_{N+2}(\xi)}\,d\xi .
\tag{3}
$$
Node overlap is allowed. Formula (3) is a joint numerator enclosure
option for the direct comparator as well.

For example, put $m=2N+2$ and let $X$ be the uniform probability
simplex average of the two combined node lists (exactly $m$ knots,
with repetitions). Expanding the contour with numerator $e^{iz\xi}$
and using the simplex monomial moments gives
$(iz)^{m-1}\chi(z)/(m-1)!$, where $\chi(z)=\mathbb E e^{izX}$.
Apply $\partial_z/i$ to insert $\xi$ in (3). Then
$$
 d_G=L_N\left(\chi+\frac{z\chi'}{2N+1}\right),\qquad
 \sigma^2:=\mathbb E X^2
    =\frac{\operatorname{tr}J_N^2+\operatorname{tr}J_{N+2}^2}
           {(2N+2)(2N+3)} .
\tag{4}
$$
The node lists are symmetric so $\mathbb E X=0$. For
$\Lambda\ge\|J_{N+2}\|$, $|X|\le\Lambda$. Second-order and
first-order Taylor integral remainders for $\chi-1$ and $\chi'$
give, for $Y\ge|\Im z|$, the entirely finite bound
$$
 \left|\chi+\frac{z\chi'}{2N+1}-1\right|
 \le |z|^2\left(\frac12+\frac{1}{2N+1}\right)
           \mathbb E[X^2e^{Y|X|}]
 \le |z|^2\left(\frac12+\frac{1}{2N+1}\right)\sigma^2 e^{Y\Lambda}.
\tag{5}
$$
This optional enclosure prices complex phase without an omitted-chain
oracle. Its usefulness against the other available enclosures is untested.

**Link accounting.** Exact degree-only finite acquisition via (3) or (4)
uses the prefix through $\beta_{N+1}$. The two time derivatives and
defects in (1), including their spectral formula, use at most
$\beta_{N+2}$. The explicit prefactors in (2) consume through
$\beta_{N+2}$, but the exact $E_N,E_{N+2}$ as separate characteristic
laws still depend on the full theta source. If supplied exact second or
fourth phase moments at degree $N+2$ are used as extra information,
they require links through $\beta_{N+3}$ or $\beta_{N+4}$,
respectively. The inherited uniform phase envelope uses a priori
theta bounds in place of acquiring those extra links. No derivative
of a characteristic error law is needed in physical time.

## 2. Branch and the nonlinear coordinate payment

The ratio $G_+/G_-$ has zero winding on $\Gamma$ by equality of counts,
and admits a holomorphic logarithm $\ell$ on the annular collar.
Fix a branch at one time and continue it by integrating the ratio's
time logarithmic derivative. This is valid on the interval by clearance.
A sufficient bounded branch condition, given $m_->0$ with
$m_-\le\inf_\Gamma|G_-|$, is
$\theta=\sup_\Gamma |d_G/G_-|<1$ throughout the time cell. The series for
$\log(1+d_G/G_-)$ then gives $\|\ell\|_\Gamma\le-\log(1-\theta)$
and extends to a collar by strictness. A cleared straight homotopy of
the shared numerator gives the alternative bound
$\|\ell\|_\Gamma\le\sup|d_G|/\inf_{0\le s\le1,\Gamma}|G_-+s d_G|$.
Equal counts and a cleared collar give existence even where these
sufficient magnitude bounds fail. A branch shift by a spatial constant
drops out of the contour formulas below. The fixed chart incurs no
transition payment. A changed contour or changed target pair needs
its own count/clearance and identity of the retained pair.

On a fixed time slice, use the centered power moment
$p_{k,j}=\langle(z-a)^k B_j\rangle$. Then $c_j=a+p_{1,j}/2$,
$D_j=p_{2,j}/2-p_{1,j}^2/4$. Since $\delta B=\ell_z$,
integration by parts gives $\delta p_k=-k\langle(z-a)^{k-1}\ell\rangle$.
Thus with $\bar c=(c_++c_-)/2$,
$$
 \delta c=-\tfrac12\langle\ell\rangle,\qquad
 \delta D=-\langle(z-c_-)\ell\rangle-(\delta c)^2
          =-\langle(z-\bar c)\ell\rangle .
\tag{6}
$$
The first formula for $\delta D$ uses only the reference center and
the shared log. Its negative real square has its own uncertainty.
If $L\ge\|\ell\|_\Gamma$, take
$a_c=rL/2$, $a_D=rgL$. More tightly, find the range of the same
functional (6) over the joint permissible logs, retaining the
center-square term and its correlation. Define
$$
 A_Q=2g a_c+a_D,\qquad
 Q_--Q_+=(2z-c_--c_+)\delta c+\delta D .
\tag{7}
$$
The right side both fixes the sign of the kernel change and gives
$\|Q_+-Q_-\|\le A_Q$. Independently acquired smaller allowances for
the complete coordinate increments can substitute for $a_c,a_D$.

## 3. Exterior moments, changing kernels and their allowances

For the finite fields,
$|G_j(z)|\le e^{\|J_j\||\Im z|}$ and $G_j(0)=1$ by their positive
finite spectral measures. Jensen at $2R$ gives
$n_j(R)\le2R\|J_j\|/\log 2$. Thus the inverse-square zero sum
converges absolutely by dyadic summation. The order-at-most-one
Hadamard factorization already used in
[VCD exterior divisor](../../../03_volterra_coefficient_dynamics/manuscript/sections/source_curvature.tex)
and [AGC complete products](../../manuscript/sections/02_pair_chain.tex)
pairs opposite roots and leaves at most a linear exponential;
evenness removes the latter. This gives fixed-order product passage
on the cleared collar, with multiplicities and without any root
reality or simplicity requirement. In particular the canonical
theta zero-count estimate is unnecessary for the finite fields.

For $k^S_{n,j}=Q_j^{-n}$ ($n\ge1$) and $k^T_{n,j}=w_jQ_j^{-n}$
($n\ge2$), the complete exterior moment is $X_j=-\langle k_j B_j\rangle$.
The same holds for the split weight
$k_j=(z-\zeta_{j,1})^{-p}(z-\zeta_{j,2})^{-q}$ in the integer
domain $p,q\ge0$, $p+q\ge2$. Each rational weight decays at least
quadratically at infinity. A target pole in $B_j$ makes zero
combined residue, and an exterior pole at $\rho$ makes total
residue $-k_j(\rho)$ inside the target contour. The regularizer
constants give zero integral. These facts reproduce the
[AGC trace argument](../../manuscript/sections/03_hierarchy.tex)
for both heads. For every indicated weight, exactly,
$$
 \delta X=\langle (\partial_z k_+)\ell\rangle
             -\langle(k_+-k_-)B_-\rangle .
\tag{8}
$$
An equivalent formula exchanges $k_+$ for $k_-$ in the first term
and $B_-$ for $B_+$ in the second. Equation (8) uses one log and
the kernels generated by (6), including at $D_j=0$ in the S/T form.

For $B_*\ge\|B_-\|_\Gamma$, an explicit complete bound is
$a_X=r(C_X L+H_X B_*)$, where
$$
\begin{array}{c|cc}
 X & C_X\ \text{for }|\partial_z k_+| & H_X\ \text{for }|k_+-k_-|\\ \hline
 S_n & 2n b^{-(2n+1)} & n A_Q b^{-(2n+2)}\\
 T_n & b^{-2n}+2ng b^{-(2n+1)} &
       a_c b^{-2n}+ng A_Q b^{-(2n+2)} .
\end{array}
\tag{9}
$$
Factor each $Q_j$ to differentiate. For the kernel difference,
telescope the two reciprocal powers using the individual $b^2$ floors,
then subtract the numerator $w_j$ for the odd row. This proof does
not require an interpolated pair polynomial to stay clear. For split
weights with selected labels one can take $C_X=(p+q)b^{-(p+q+1)}$
and $H_X=(p|\delta\zeta_1|+q|\delta\zeta_2|)b^{-(p+q+1)}$ by
telescoping the individual linear factors. At a slice labels can be
matched with $|\delta\zeta_i|\le a_c+\sqrt{a_D}$, since the
smaller of $|s_+-s_-|,|s_++s_-|$ is at most $\sqrt{|\delta D|}$ for
$s_j^2=D_j$. Transport through a collision uses (8) in S/T; no
differentiation of the square-root matching is needed.

In particular $M=S_1$. With $\mathcal F_j=12S_{2,j}+16D_j S_{3,j}$,
retain
$$
 \delta\mathcal F=12\delta S_2+
       16(D_+\delta S_3+S_{3,-}\delta D).
\tag{10}
$$
For a magnitude envelope its allowance is
$12a_{S_2}+16(d_*a_{S_3}+r B_* b^{-6}a_D)$, since
$|S_{3,-}|\le r B_* b^{-6}$. Joint signed evaluation uses the
same logs, coordinates and denominators in (6)–(10).

## 4. Two-field time identity and boundary cancellation

The common scalar heat normalization cancels. Exactly on the collar,
$$
 \ell_t+\ell_{zz}+(B_++B_-)\ell_z=\delta U,\qquad
 \delta U=\frac{R_+G_--R_-G_+}{G_+G_-}
          =\frac{\delta R-U_-d_G}{G_+}.
\tag{11}
$$
Indeed $V_j=B_{j,z}+B_j^2$ and
$G_{j,t}/G_j=U_j-V_j-\beta_1$. In particular
$$
 \ell_t=\delta U-\delta V
       =\frac{\delta R-d_{G,zz}-(U_--V_-)d_G}{G_+}
       =\frac{d_{G,t}-(G_{-,t}/G_-)d_G}{G_+}.
\tag{12}
$$
The two leading Taylor terms of $\delta R$ and $d_{G,zz}$
at the origin agree and cancel, since $d_G$ starts at $L_N$ and
$R_N$ starts at $-\partial_z^2L_N$. Equivalently
$\delta R-d_{G,zz}=(\partial_t+\beta_1)d_G$ vanishes to order
$2N$ at the origin. This local order statement gives no uniform
gain on an arbitrary contour. For any differentiable collar test
$k(t,z)$, (11) also gives
$$
 \langle k\,\delta U\rangle
 =\frac{d}{dt}\langle k\ell\rangle
  -\langle[k_t-k_{zz}+(k(B_++B_-))_z]\ell\rangle .
\tag{13}
$$
Thus a residual-only time integral generally has an interior payment.

For the gap law let $r_j=-\langle w_j U_j\rangle$. Direct counted
moments yield $\dot c_j=-\langle G_{j,t}/G_j\rangle/2$ and, by
(1), $\dot D_j=2-4D_jM_j+r_j$. All are identities at a double.
The complete raw difference is
$$
 -4\delta(DM)+\delta r
    =-\langle(z-\bar c)\ell_t\rangle+\dot{\bar c}\langle\ell\rangle
    =\frac{d}{dt}\,\delta D .
\tag{14}
$$
For example, substitute $\ell_t=\delta U-\delta V$ and the mean
center drift into the right side. Both changed center terms are
included. Integrating by parts in time gives exactly the two
unweighted endpoint values in (6).

The common-reference *weighted* version gives an endpoint identity
on every $[u,v]\subset I$. Put
$W_-(t;v)=\exp(-4\int_t^v M_-(s)\,ds)$, so
$\partial_t W_-=4M_-W_-$. Because
$\delta(DM)=M_-\delta D+D_+\delta M$,
$$
 \boxed{\int_u^v W_-(t;v)\,[\delta r-4D_+\delta M](t)\,dt
        =\delta D(v)-W_-(u;v)\delta D(u).}
\tag{15}
$$
The full signed integrand is the derivative of $W_-\delta D$.
Its absolute integral **after** cancellation is bounded by
$a_D(v)+W_-(u;v)a_D(u)$, where the absolute value is outside
the integral. Equation (6) gives a signed endpoint enclosure as well.
Using (15) budgets the complete relative transport; it supplies no
standalone small bound for the time integral of either summand.
For each field independently, its own weight
$W_j(t;v)=\exp(-4\int_t^v M_j)$ gives
$W_j(u;v)D_j(u)=D_j(v)-\int_u^v W_j(2+r_j)$. Thus a comparison
of separate weights also pays their difference, with
$$
 |W_+(t;v)-W_-(t;v)|\le
 W_-(t;v)\left(e^{4\int_t^v a_M(s)\,ds}-1\right).
$$
For example, the difference of the two own-weight costs
$\int_u^v W_j(2+r_j)$ is
$\delta D(v)-W_+(u;v)\delta D(u)-(W_+-W_-)(u;v)D_-(u)$.
This exhibits the remaining weight payment.

For comparison with [E01's request](../research-progress/handoffs/AGC_JH_E01_REQUEST_R1_20261119.md),
write $\gamma_j=-\langle U_j\rangle/2$ and
$\mathfrak r_{k,j}=\langle k_z U_j\rangle-
\langle(k_c\gamma_j+k_D r_j)B_j\rangle$ for the extra moment force.
This follows by differentiating $-\langle kB_j\rangle$ using
$B_{j,t}=-V_{j,z}+U_{j,z}$. In particular
$\mathfrak r_{M,j}=-2\langle w_jQ_j^{-2}U_j\rangle+
2\gamma_j T_{2,j}+r_jS_{2,j}$. The complete E01 low law implies
$$
 (\delta M)'=2(M_++M_-)\delta M-\delta\mathcal F+
                 \delta\mathfrak r_M .
\tag{16}
$$
With $A(t)=\exp(-2\int_u^t(M_++M_-))$, the integral of
$A(\delta\mathfrak r_M-\delta\mathcal F)$ is
$A(v)\delta M(v)-\delta M(u)$. This uses all of (10) and exchanges
only the *complete* combination for endpoints. A finite moment
truncation would need additional estimates.

## 5. Enclosure inputs and matched comparison

Absolute time-integrand bounds can be made from joint spatial ones.
For $m_+\le\inf_\Gamma |G_+|$, $m_+>0$, let $U_*\ge\|U_-\|$.
From the cross numerator in (11) and the changed center,
$$
 \|\delta U\|\le(\|\delta R\|+U_*\|d_G\|)/m_+,\qquad
 |\delta r|\le r(g\|\delta U\|+a_c U_*).
\tag{17}
$$
The centered residual is exactly
$\delta r=-\langle(z-\bar c)\delta U-\delta c(U_++U_-)/2\rangle$.
Use this or the equivalent reference-centered formula before
absolute values when enclosing the signed integrand. For the
$\ell_t$ integrand use the combined numerator of (12). Where the
right side of (17) is bounded by $a_r(t)$, one can intersect the
endpoint allowance in (15) with
$\int_u^v W_-(a_r+4d_*a_M)$, which also records the short-interval
decay when its integrand is uniformly bounded. With a
sup bound $u_j$ for $|U_j|$ and $b_j^B$ for $|B_j|$,
the explicit bound for the individual $M$ force is
$r u_j[2/b^3+r b_j^B/b^3+r g b_j^B/b^4]$.
It follows from the derivative bound for $k^S_1$, the two center
forces, and $|S_{2,j}|\le rb_j^B/b^4$, with
$|T_{2,j}|\le rb_j^B/b^3$ from its two linear factors at the roots
when estimating $2T_2$ via $-(k^S_1)_z$. These unsigned choices
are optional relaxations of the shared contour functionals.

For approximate contour evaluations, floors $m_j>0$ and
$|Q_j|\ge b^2$ must themselves be enclosed. The following
rules specify the input and quadrature payments. A tilde denotes an
evaluated quantity, $e_X$ a uniform pointwise error. For any
quotient $Y/G_j$ with evaluated denominator cleared,
$$
 e_{Y/G_j}\le(e_Y+\|\widetilde{Y/G_j}\|e_{G_j})/m_j .
$$
For $Y=d_G,G_{j,z},G_{j,zz},R_j$ this pays the readout, its jets,
and the defect. A symmetric collar of width $h>0$ with field
error $e$ supplies first and second jet errors $e/h$ and $2e/h^2$
by Cauchy's estimates when the radius-$h$ disks lie in its domain.
For $q=d_G/G_-$, if $q$ and $\tilde q$ both lie in $|q|\le\theta<1$,
then $e_\ell\le e_q/(1-\theta)$. Use the same enclosure of $q$
for both coordinate moments. With a reference center error $e_{c_-}$,
let $q_0,q_1$ be the contour quadrature allowances for the
evaluated $\ell$ and $(z-\tilde c_- )\tilde\ell$ integrals. The
errors from (6) satisfy
$$
 e_{\delta c}\le (r e_\ell+q_0)/2,\qquad
 e_{\delta D}\le r(g e_\ell+e_{c_-}\|\tilde\ell\|)+q_1+
           e_{\delta c}(2|\widetilde{\delta c}|+e_{\delta c}).
$$
For an evaluated $Q_j$ use
$e_{Q_j}\le(2g+e_{c_j})e_{c_j}+e_{D_j}$ and lower floor
$b^2-e_{Q_j}$ when positive. Reciprocal powers and spatial
derivatives in (8) or (17) use the individual exact and evaluated
floors, with
$|Q^{-n}-\tilde Q^{-n}|\le n e_Q/\min(b^2,b^2-e_Q)^{n+1}$.
For every product $XY$ used in these contour formulas the integration
error is bounded by
$r(\|X\| e_Y+e_X\|\tilde Y\|)+q_{\Gamma,XY}$, where
$q_{\Gamma,XY}$ encloses numerical quadrature of the evaluated
integrand. Apply this also to changes of kernels and denominator
quotients. Interval evaluation of the combined formulas can retain
common dependence throughout.

In time, if the integral of $M_-$ for a given endpoint pair has
error $e_P$ including the time quadrature and integrated spatial
error, then the error of $W_-$ is at most
$e_W=\tilde W_-(e^{4e_P}-1)$. The allowance for a computed
right side of (15) is
$$
 e_{\delta D(v)}+\tilde W_-(u;v)e^{4e_P}e_{\delta D(u)}
      +e_W|\widetilde{\delta D(u)}|.
$$
The exact endpoint evaluation itself needs no time quadrature
for the combined forcing; time quadrature for the weight remains
payable. Signed numerical integration of any remaining forcing
requires a separate time remainder. Uniform all-subinterval claims
require the input enclosures and weight errors uniformly in the
time arguments. Point samples alone provide no such enclosure.

By (15), an endpoint budget can replace accumulated separate
absolute heat/degree defect budgets for this particular combined
transport. The matched direct evaluator has those same endpoints,
the same logarithm (6), and the same ratio data; an identity
alone leaves that comparator's available information unchanged.
A genuine gain requires an independently acquired signed
theta input, cheaper acquisition, or a tighter allowance under
an explicit common information contract. Extending the interface
to the limiting theta cluster would still pay its count, floor
and tail transfer. A small degree increment does not specify the
sign of either gap.

## 6. Control screen and check

The source/premise screen uses the recorded event and preservation
classes in [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md).
The conclusions here are conditional identities and magnitude
bounds on cleared charts, including local collision charts where
the hypotheses hold.

| Control | Missing literal premise for the theta application |
| --- | --- |
| Euler-factor | Complete canonical theta amplitude and ordinary Dirichlet coefficients. |
| Weighted-square, finite-tail and finite-score controls | Complete canonical square coefficients and reflection identities. A finite matched head or score prefix is insufficient. The finite-score construction has no prescribed compact zero location. |
| Reflected super-Gaussian | Canonical square arithmetic. Its source hypotheses alone do not give the theta order-one divisor passage. |
| Smooth shape and positive primitive | Exact theta square expansion, despite the preserved shape and auxiliary positivity. |
| Finite-prime orbits | Full theta reflection and coefficient identities despite the selected orbit invariants. |
| Atomic and finite-profile controls, including compact continuous extensions | Complete theta profile and growth; the atomic cases have terminating source chains, and the stated threshold profiles fail theta's eventual simplicity. |
| RH-conditional endpoint controls | Ordinary Dirichlet arithmetic, despite the stated normalization, completion and tail properties. |
| Fixed-amplitude variable kernels | Full cosine observation/oscillator and its physical heat equation. |
| Actual-profile positive-measure relaxation | An actual compatible divisor of the prescribed entire field. |

The missing literal premises do not screen a coarse quantitative
inequality that a control may also satisfy. No sign inequality
was selected here. The count/collar arguments permit a double
root in the interior, and no negative statement extends beyond
the comparison and hypotheses displayed above. In the symbolic
heat check $Y(z,t)=(z-a)^2-2(t-t_*)$ with normalization scalar
zero, $M=0$ and $D'=2$; a pair of such fields with different
$t_*$ has constant $\delta D$, verifying the orientation in
(14)–(15). At $N=2$ the numerators of $m_2,m_4$ are $\xi$ and
$\xi(\xi^2-\beta_2-\beta_3)$, respectively, and their difference
over $P_2P_4$ has numerator $\xi\beta_1\beta_2$, checking (3)
with its first omitted path. Direct contour normalization and the opposite-paired
product were checked against the frozen sources. This is an
internal algebra check with inherited premises and no specialist review.
