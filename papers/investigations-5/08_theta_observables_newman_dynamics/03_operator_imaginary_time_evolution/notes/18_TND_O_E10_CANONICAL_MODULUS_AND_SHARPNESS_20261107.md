# E10 r1: canonical localized modulus and instantaneous sharpness

7 November 2026 UTC; 6 November 2026 America/New_York. Prepared for
**Edward Baker** with substantial OpenAI Codex assistance. Tool-selected
executor dispatch configuration: **gpt-6.1-sol, ultra**, retained for
this follow-up assignment. This records configuration provenance, not
independent verification of the serving backend.

**Task:** TND-O-E10 r1, Type E, under frozen
[request22](../research-progress/handoffs/22_TND_O_E10_REQUEST_20261107.md),
[inputs22](../research-progress/handoffs/22_TND_O_E10_INPUTS_20261107.json)
and [B04 Decision08](../brainstorm/notes/08_TND_O_B04_SAFE_LINE_CANONICAL_ESTIMATE_DECISION_20261107.md).
All ten frozen byte counts and hashes matched before work. The
post-dispatch [E09 assessment](../reviews/06_TND_O_E09_LOCALIZED_CALCULUS_ASSESSMENT_20261107.md)
and [return21](../research-progress/handoffs/21_TND_O_E09_RETURN_20261107.json)
were separately read and hash-verified: E08 was accepted without
mathematical correction. They are additional assessment inputs, not
retroactive changes to inputs22. The E09 dependency is satisfied.

**Result, proved in-note:** for the complete canonical zero set,
\[
 \boxed{|\partial_\lambda Q_{X,R}|
 \le C(\|\chi\|_\infty+\|\chi'\|_\infty+\|\chi''\|_\infty)
             R^{-2}\log^2(2+X)}
 \tag{1}
\]
uniformly for \(X\ge10,\ 0<R\le1,\ 0\le\lambda\le1/2\), on intervals
with simple relevant roots. No minimum-gap parameter occurs. An
explicit even polynomial family satisfies the used coarse premises
uniformly at its snapshots and has
\[
 Q_s\le-\frac{3249}{5000}\frac{m^2}{R^2}
       <-\frac{m^2}{2R^2}.
 \tag{2}
\]
For \(m=\lfloor\log(2+X)\rfloor\), this shows sharpness in the
instantaneous coarse-premise class. It is not an all-time canonical
sharpness claim. At fixed \(R\), (1) costs \(\log^2X\); at
\(R\asymp1/\log X\), it costs \(\log^4X\). No favorable sign or
collision envelope follows.

| Declared successor | Type / model | Dependency and output |
| --- | --- | --- |
| TND-O-B06 / E12 | B — Astra; then E — Sol | Select and prove the extension across relevant multiple-root times and its integrated form |
| TND-O-B05 | B — Astra | Decide which genuine collision consumer remains, naming its additional endpoint or flux input |

Only this note and
[return22](../research-progress/handoffs/22_TND_O_E10_RETURN_20261107.json)
are owned outputs. The sole register, E08/E09 files and manuscript are
not changed.

## 1. Fixed family and the two coarse canonical inputs

Use
\[
 H_0(z)=\tfrac18\xi(\tfrac12+iz/2),\quad
 \partial_\lambda H=-H_{zz},\quad s=\lambda_*-\lambda,
 \quad L(u)=\log(2+|u|),\quad L_X=\log(2+X).
 \tag{3}
\]
Zeros \(\zeta_k=\xi_k+i\eta_k\) are counted with multiplicity and
opposite pairing. On this Newman interval \(|\eta_k|\le1\).
Let \(F_\lambda=H_\lambda'/H_\lambda\).

The fresh primary-source check is Polymath,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2),
Theorem 1.5(iv) and its §9 proof at (105) and the following paragraphs.
These give unit-window counts and
\(|F_\lambda(u+4i)|=O(L(u))\), with absolute constants for
\(0<\lambda\le1/2\). The stronger tail-realness threshold is not
required. Proposition 9.1(ii), unlike part (i), has an absolute large
height threshold on its fixed upper strip.

After a fixed enlargement of constants to include closed endpoints,
negative horizontal coordinates and the endpoint argument below, there
is one absolute \(A\ge1\) such that
\[
 \begin{split}
 |F_\lambda(u+4i)|&\le A L(u),\\
 n_\lambda([u,u+1])
 :=\#\{k:u\le\xi_k\le u+1\}&\le A L(u)
 \end{split}
 \qquad(u\in\mathbb R,\ 0\le\lambda\le1/2).
 \tag{4}
\]
Reflection handles negative coordinates. The complete-source
regularity in M §2 gives locally uniform convergence of \(H_\lambda\)
and \(H_\lambda'\) to their time-zero values. The line \(\Im z=4\)
is zero-free for every parameter in question. For each fixed real \(u\),
passing to \(\lambda\downarrow0\) in the positive-time resolvent
bound therefore gives the same bound at zero. The constant is
independent of \(u\), so this pointwise limit establishes the
all-\(u\) statement; uniform convergence on an unbounded line is not
assumed.

For explicit endpoint count continuity, fix \([u,u+1]\). Choose
\(0<\epsilon<1/2\) so that the vertical sides of
\[
 \{u-\epsilon<\Re z<u+1+\epsilon,\ |\Im z|<2\}
\]
contain no zero of \(H_0\). Only finitely many choices are excluded
in the bounded region; the horizontal sides are zero-free by the
strip. Uniform convergence on this boundary and the argument principle
keep its total multiplicity fixed for sufficiently small positive
\(\lambda\). The time-zero unit count is no larger than this total.
Covering its width \(<2\) by two unit intervals at positive time bounds
it by \(4A_{\rm old}L(u)\), since
\(\log(3+|u|)\le2L(u)\). This proves (4) at zero after one absolute
constant enlargement. Boundary multiplicities cause no loss.

The imported source estimates are only upper counts and a safe-line
resolvent. No full lower zero-density asymptotic is used.

## 2. Local algebra without a minimum gap

Let \(\chi\in C_c^2([-1,1])\), \(0\le\chi\le1\), and
\[
 a(x)=\chi((x-X)/R),\qquad f(x,y)=a(x)y^2,\qquad
 Q=\sum_jf(x_j,y_j),\qquad
 A_q=\|a^{(q)}\|_\infty.
 \tag{5}
\]
Relevant supported zeros have simple local charts. Exterior zeros,
including those in the larger cluster below, may repeat.

For a selected simple root the complete paired dynamics in \(s\)
are \(z_s=-2\sum'_{k\ne j}(z_j-\zeta_k)^{-1}\).
For finite indices, pairing the chain-rule terms gives the kernel
\[
 K_{jk}
 =\frac{(f_y(z_j)-f_y(z_k))e-(f_x(z_j)-f_x(z_k))d}{d^2+e^2}
 =\int_0^1\frac{2a(x_t)e^2-a''(x_t)y_t^2d^2}{d^2+e^2}\,dt.
 \tag{6}
\]
Indeed the chord integrand before simplification contains
\(ed f_{yx}-de f_{xy}=0\). With strip height one,
\[
 |K_{jk}|\le K_0:=\max(2A_0,A_2).
 \tag{7}
\]
This rederives the finite algebra used from accepted E08. No reciprocal
gap remains. Coincident inactive repeated roots have zero kernel,
defined by their zero endpoint gradients.

Fix the local cluster
\[
 \mathcal C_X=\{k:|\xi_k-X|\le3\},\qquad n=\#\mathcal C_X,
 \quad m_a=\#\{j:|x_j-X|\le R\}.
 \tag{8}
\]
Covering \([X-3,X+3]\) by six closed unit intervals, and
\([X-1,X+1]\) by two, (4) gives
\[
 n\le12A L_X,\qquad m_a\le2A L_X.
 \tag{9}
\]
For the first inequality, \(\log(X+4)\le2L_X\); for the second,
the interval starts are \(X-1,X\). These upper bounds may double-count
endpoint roots, which is harmless.

## 3. The exterior field from safe-line subtraction

Let \(z=x+iy\) be active, so \(|x-X|\le R\le1\), \(|y|\le1\),
and put \(w=x+4i\). Define the exterior field by removing the finite
cluster from the complete opposite-paired logarithmic derivative.
For a root outside \(\mathcal C_X\),
\[
 |x-\xi_k|>2,\qquad
 \left|\frac1{z-\zeta_k}-\frac1{w-\zeta_k}\right|
 \le\frac5{|x-\xi_k|^2}.
 \tag{10}
\]
Thus
\[
 E_X(z)=F_\lambda(w)-\sum_{k\in\mathcal C_X}\frac1{w-\zeta_k}
       +\sum_{k\notin\mathcal C_X}
            \left(\frac1{z-\zeta_k}-\frac1{w-\zeta_k}\right).
 \tag{11}
\]
The first term retains the canonical opposite pairing. The last
series is absolutely convergent, as now quantified. Formula (11)
also defines the exterior field at an active root, without evaluating
the singular full logarithmic derivative there.

For integer \(h\ge2\), place the exterior roots with
\(h\le|x-\xi_k|<h+1\) in its two unit intervals. From (4),
their total number is at most
\[
 2A\{L_X+\log(h+2)\},
 \tag{12}
\]
because their interval starts have magnitude at most \(X+h+2\) and
\(\log(X+h+4)\le L_X+\log(h+2)\).
Consequently
\[
 \sum_{k\notin\mathcal C_X}|x-\xi_k|^{-2}
 \le2A\sum_{h=2}^{\infty}\frac{L_X+\log(h+2)}{h^2}
 \le5A L_X.
 \tag{13}
\]
For the last inequality use
\(\sum_{h\ge2}h^{-2}\le1\) and
\[
 \sum_{h\ge2}\frac{\log(h+2)}{h^2}
 \le\int_1^\infty\frac{\log(t+2)}{t^2}\,dt
 =\log3+\tfrac12\log3<3;
\]
then \(L_X>2\). The integral test applies because its integrand is
decreasing for \(t\ge1\).

There is also an explicit full-index remainder. Truncating the last
series in (11) to \(|x-\xi_k|<M\), integer \(M\ge2\), leaves at most
\[
 \frac{10A}{M-1}\{L_X+\log(M+1)+1\}.
 \tag{14}
\]
Indeed the relevant inverse-square shell sum is bounded by
\[
 \frac{2A}{M-1}\{L_X+\log(M+1)+1\},
\]
using the same integral test and
\(\tfrac12\log(1+2/(M-1))\le1/(M-1)\).
This tends to zero uniformly in the declared time range and in the
active strip at fixed \(X,R\).

At the safe point \(|w-\zeta_k|\ge3\) for local roots. Equations
(4), (9), (10), (13) now give
\[
 \begin{split}
 |E_X(z)|
 &\le A\log(2+x)+n/3+
           5\sum_{k\notin\mathcal C_X}|x-\xi_k|^{-2}\\
 &\le (2+4+25)A L_X
 =\boxed{31A L_X}.
 \end{split}
 \tag{15}
\]
Here \(x\ge9\), so \(\log(2+x)\le\log(X+3)\le2L_X\).

To justify the grouping in (11), start with full radial Hadamard
cutoffs containing all of \(\mathcal C_X\), subtract that finite
cluster, and compare the remaining terms at \(z,w\). Accepted E08
pays the paired resolvent cutoff, while (14) pays the absolute
difference series. Removing a finite cluster that is not
opposite-symmetric does not change the limiting convention. No
absolute harmonic sum of the exterior field is used.

## 4. Canonical modulus and its exact width/height loss

Split the root dynamics into local interactions and the field \(E_X\).
The finite chain rule gives
\[
 Q_s=
 2\sum_{\substack{j<k\\j,k\in\mathcal C_X}}K_{jk}
 -2\sum_{\rm active\ j}
       \{f_x(z_j)\Re E_X(z_j)+f_y(z_j)\Im E_X(z_j)\}.
 \tag{16}
\]
An inactive endpoint has zero gradient. Adding its zero row before
pairing is legitimate even if that root repeats; no velocity is
assigned to a repeated inactive root.

At most \(m_an\) unordered local pairs contribute. Also
\[
 |\nabla f|\le G:=A_1+2A_0.
\]
Combining (7), (9), and (15),
\[
 \begin{split}
 |Q_s|
 &\le2m_anK_0+2m_aG(31A L_X)\\
 &\le A^2L_X^2\{48K_0+124G\}\\
 &\le A^2L_X^2(344A_0+124A_1+48A_2).
 \end{split}
 \tag{17}
\]
Since \(A_0=\|\chi\|_\infty\),
\(A_1=R^{-1}\|\chi'\|_\infty\),
\(A_2=R^{-2}\|\chi''\|_\infty\), and \(R\le1\), (1) holds with,
for example,
\[
 C=344A^2.
 \tag{18}
\]
The numerical prefactors here are explicit relative to the one
absolute primary-source constant \(A\); that constant has not been
numerically evaluated. The sign reversal
\(\partial_\lambda Q=-Q_s\) preserves this modulus.

All time uniformity is explicit in (4), (14), and (15).
There is no RH or global-simplicity hypothesis. The derivative is
asserted on simple relevant-root intervals, with the natural
one-sided interpretation at endpoints of the parameter domain.
The proof does not cross active collisions or assert a global
integrated theorem. Those are the declared B06/E12 obligations.

For fixed \(R>0\), the upper cost is \(O_\chi(\log^2X)\).
For \(R\asymp L_X^{-1}\), it is \(O_\chi(L_X^4)\), with constants
also depending on the stated comparison constants for \(R\).
This controls variation; it is not a small mass, favorable sign,
or improvement of the real/simple positive-time benchmark.

## 5. Exact fixed polynomial sharpness construction

Let
\[
 \chi(t)=(1-t^2)^3\quad(|t|<1),\qquad \chi(t)=0\quad(|t|\ge1),
 \quad t_j=\tfrac7{10}+\frac{j}{10(m+1)},\quad 1\le j\le m,
 \tag{19}
\]
where \(m\ge2\), \(X\ge10\), \(0<R\le1/10\), and
\(p_j=X+Rt_j\). The zero-extended \(\chi\) is \(C_c^2\);
\(0\le\chi\le1,\ |\chi'|\le6\), and on \([7/10,4/5]\),
\[
 \chi''(t)=6(1-t^2)(5t^2-1)
 \ge6\frac9{25}\frac{29}{20}
 =\frac{783}{250}>3.
 \tag{20}
\]

Define the even real monic polynomial
\[
 P_0(z)=\prod_{j=1}^m
       [(z-p_j)^2+\tfrac14][(z+p_j)^2+\tfrac14],
 \quad
 P(s,z)=\sum_{\ell=0}^{2m}\frac{s^\ell}{\ell!}
                          \partial_z^{2\ell}P_0(z).
 \tag{21}
\]
It has \(4m\) distinct snapshot roots \(\pm p_j\pm i/2\), and its
finite exact heat orbit satisfies \(P_s=P_{zz}\). Only the positive
cluster is active for \(a(x)=\chi((x-X)/R)\).
Use \(Q_s=2\sum_{j<k}K_{jk}\), counting the following three classes.

**Same-height active pairs.** Here \(y_j=y_k=\pm1/2\),
so the mean-value theorem and (20) give
\[
 K_{jk}=-\frac14\frac{a'(p_j)-a'(p_k)}{p_j-p_k}
       \le-\frac3{4R^2}.
 \tag{22}
\]
There are \(2\binom m2=m(m-1)\) unordered pairs; their total
contribution to \(Q_s\) is at most
\(-3m(m-1)/(2R^2)\).

**Opposite-height active pairs.** There are \(m^2\) pairs, including
the vertical conjugate pairs. Their exact kernel is
\[
 K_{jk}
 =\frac{a(p_j)+a(p_k)
       -\tfrac14(a'(p_j)-a'(p_k))(p_j-p_k)}
             {1+(p_j-p_k)^2}\le2.
 \tag{23}
\]
The derivative \(a'\) is increasing throughout this cluster by (20).
Thus this entire class contributes at most \(4m^2\).

**Active versus reflected inactive pairs.** There are
\((2m)(2m)=4m^2\). Their horizontal distance
\(d=p_j+p_k\ge2X\), and \(|e|\le1\). At the active endpoint
\(|f_y|\le1,\ |f_x|=|a'|/4\le3/(2R)\). Hence
\[
 K_{jk}\le\frac1{4X^2}+\frac3{4RX}.
 \tag{24}
\]
After the global factor two this class contributes at most
\(2m^2/X^2+6m^2/(RX)\). Pairs with both endpoints inactive
have exactly zero kernel.

Combining all classes,
\[
 Q_s\le-\frac{3m(m-1)}{2R^2}
           +4m^2+\frac{6m^2}{RX}+\frac{2m^2}{X^2}.
 \tag{25}
\]
Since \(m(m-1)\ge m^2/2,\ R^2\le1/100,\ R/X\le1/100\),
\(R^2/X^2\le1/10000\), this yields exactly
\[
 Q_s\le
 \left(-\frac34+\frac1{25}+\frac3{50}+\frac1{5000}\right)
       \frac{m^2}{R^2}
 =-\frac{3249}{5000}\frac{m^2}{R^2}
 <-\frac{m^2}{2R^2}.
 \tag{26}
\]
No numerical approximation, search, or spacing adjustment is involved.

## 6. Uniform instantaneous premises of the sharpness family

Now choose \(m=\lfloor L_X\rfloor\). Since \(L_X>2\),
\(m\ge2\) and \(m\ge L_X/2\). Thus
\[
 |Q_s|\ge\frac{L_X^2}{8R^2}.
 \tag{27}
\]
This lower rate has the same width/height order as (1).
The following bounds have constants independent of \(X,R,m\).

1. **Strict snapshot strip and full opposite pairing.**
   Every root has imaginary part \(\pm1/2\); the complete polynomial
   product includes all opposite and conjugate partners.
2. **Full origin-centered zero count.**
   \(N(r)=0\) for \(r<X\). For \(r\ge X\),
   \[
    N(r)\le4m\le4\log(r+2)\le r\log(r+2).
    \tag{28}
   \]
3. **Local horizontal counts, all real centers.**
   A radius-one horizontal window intersects at most one cluster
   and contains at most \(2m\) roots. If nonempty its center \(u\)
   has \(|u|\ge X/2\), whence
   \[
    \#\{k:|\xi_k-u|\le1\}\le4\log(2+|u|).
    \tag{29}
   \]
   Here \(L_X\le2\log(2+|u|)\). Literal closed unit intervals also
   satisfy the form (4), with for example the absolute constant 8.
4. **Safe-line resolvent, all real centers.**
   At \(u+4i\) every denominator has modulus at least \(7/2\).
   For \(|u|\ge X/2\),
   \[
    |P_0'/P_0(u+4i)|\le8m/7
                  \le(16/7)\log(2+|u|).
    \tag{30}
   \]
   For \(|u|<X/2\), all horizontal distances exceed \(X/2\), so
   \[
    |P_0'/P_0(u+4i)|\le8m/X
       \le\tfrac45\log12\le4\log2\le4\log(2+|u|).
    \tag{31}
   \]
   The middle inequality uses that \(\log(X+2)/X\) decreases for
   \(X\ge10\); \(\log12\le5\log2\) proves the next one.

The family therefore satisfies every **slice-wise upper premise**
actually used in the canonical proof, with uniform absolute constants.
It is a finite-zero model and does not satisfy a full lower zero-density
asymptotic; none was used. Simplicity and the strict strip persist on
some parameter-dependent short heat interval by local root continuity.
The argument supplies no common interval for the family, and does not
place the polynomial orbits under canonical strip/control hypotheses on
the whole \([0,1/2]\).

Consequently the sharpness statement concerns instantaneous estimates
from the strip, upper counts, paired product and safe-line resolvent
alone. It does not exclude a stronger actual-theta estimate using
additional arithmetic or time-dependent information.

## 7. Interpretation, source use and bounded disposition

The gained canonical estimate pays the distant field at cost
\(\log X\), then the active population at another \(\log X\), while
the exact local cancellation removes a spurious minimum-gap loss.
The source/Jensen route by itself did not provide this local field
payment. The new modulus is a fixed-order theorem with unbounded
height and explicit width loss, using complete canonical zeros.

The sharpness control is even, real, simple and strictly strip-bounded
at every snapshot; it fails the complete theta source/arithmetic
premise. Other reflected/positive-primitive and Euler-factor controls
retain the calculus when their actual global hypotheses hold.
Weighted-square controls lack complete reflection, so only local
finite-cluster statements are automatically shared. No unproved
canonical small-flux or endpoint-mass estimate is assigned to any
control. This is the screening required by the
[result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[patterns index](../../../../../avoid/README.md),
[classification01](../../../../../avoid/01_restating_the_target.md),
[controls02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
All-window vanishing remains an RH reformulation; the present result
is the quantified modulus and its scoped sharpness test.

The existing Polymath2019 record and
[receipt10](../references/10_TND_O_B03_R4_BENCHMARK_SOURCE_CHECK_20261106.md)
identify the same pinned article. The primary HTML was freshly
checked on 7 November 2026 UTC at Theorem 1.5(iv), its absolute
constant convention, Proposition 9.1(ii), and §9 proof(iv), (105)
onward. The imported estimates have no exponential height restriction;
the endpoint and exterior-subtraction arguments here are explicit.
No full-paper or independent specialist audit, new article/PDF,
numerical value of the source constant, or priority claim is made.

The exact E08 inputs and the post-dispatch E09 acceptance were checked;
finite algebra was also rederived in §2. One concretely independent
read-only follow-up was sent to the existing polynomial checker:
verify only the frozen sharpness constants and all-center snapshot
premises while the executor handled the canonical proof. Its contract
was the actual pre-work message, with no separate frozen packet file.
It inherited the executor's selection, wrote no files and returned
the derivation by message. The executor checked and incorporated it.
These remain internal LLM checks with shared inherited premises.

One local consistency pass checked the safe-line endpoint, closed
window counts, shell remainder, \(31A\) field constant, \(344A^2\)
modulus constant, time sign, pair counts, sharpness arithmetic and
all-real-center bounds. No mathematical correction or new construction
was required. The preliminary provisional status ended when the
unchanged E08 package received E09 acceptance.

No numerical or symbolic research run, shared-file edit, manuscript
revision, new snapshot, commit or push was performed. No source
transcript exists for this worker; none was fabricated or registered.

**Next:** the declared **[B] TND-O-B06 — Astra / [E] TND-O-E12 — Sol**
extension must pay relevant multiple-root times before an integrated
claim. **[B] TND-O-B05 — Astra** must identify a genuine collision
consumer and its additional canonical input; (1) alone has neither a
sign nor a collision-time conclusion.
