# VCD-GT-CM-E03 r1 — Damped Cauchy evolution and complete contour tails

17 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Requested helper dispatch **gpt-6.1-sol / ultra**.
Independent serving-model and actual reasoning-effort metadata unavailable.

**Proved in-note on the frozen paid tube, pending E04 internal assessment.**
All four SHA-256 pins in the [frozen request][request] matched.
The two-line identity and its folded form are representations. The value,
derivative and truncation allowances are intermediate bounds at fixed
damping. [B01 decision][decision] · [E01 audit][e01] · [E02 time law][e02] ·
[E08 branch law][e08] · [Result index][results] · [Cluster18][cluster] ·
[Controls12][controls] · [Avoid index][avoid] · [Classification01][class] ·
[Premises02][premises] · [Scope07][scope] · [Joint estimates12][joint]

## 1. Domain and kernel constants

Keep the independently paid compact real count-two tube \(I\subset[0,1/2]\)
for the unchanged complete field \(H_t=-H_{zz}\). Use the frozen
\(T\ge64\), \(L=\log T\), \(\ell=L^{-1}\), \(\max(2,4\sqrt d)\le a\le L\),
\(c\in[T,2T]\), \(r_0=a\ell\), and \(|D|\le d\ell^2\le r_0^2/16\).
The targets \(c\pm\sqrt D\) lie within \(r_0/4\) of \(c\), counted also
at \(D=0\). For every exterior occurrence use \(w_j=\rho_j-c\),
\(a_j=w_j^2-D\), \(|w_j|\ge r_0\), \(|\Im w_j|\le1\),
\(\mu_j=\ell^2/a_j\), and \(q_0=16/15\). In particular
\(|\mu_j|\le q_0/a^2<1\). The scales are
\(m=\ell^2M\), \(\delta=D/\ell^2\), \(\sigma=(t-t_0)/\ell^2\).
Use the multiplicity-counted \(Z(p,t)\) with E02's principal outer
branches and analytic finite cluster logs. Their argument cap is
\(\Theta=3\pi/2\). [E01][e01] · [E02 §§1–2][e02]

Fix \(\epsilon>0\). For the two calculations below write the generic
kernel on a strip \(b\le u=\Re p\le r\) as
\[
 K(p,t)=\sum_{n\in \mathcal N}\frac{c_n(t)e^{\epsilon(p-n)^2}}{p-n}.
\]
Use these two choices, with \(\epsilon\) fixed separately from all cutoffs.

| Consumer | \((b,r)\) | \(n\) and \(c_n\) | \(C_\epsilon\) | \(\lambda=\min_{q=b,r;\,n\in\mathcal N}|q-n|\) |
| --- | --- | --- | --- | --- |
| \(F\) | \((1,4)\) | \(c_2=12,\ c_3=16\delta(t)\) | \((12+16d)e^{4\epsilon}\) | \(1\) |
| \(m\) | \((3/4,3/2)\) | \(c_1=1\) | \(e^{\epsilon/4}\) | \(1/4\) |

For either row put \(\Lambda(s)=\log(3+2T+|s|)\), and use
\(E_k(\gamma)=\sum_{j\ge0}2^{-j\gamma}(1+(j+1)\log2)^k\)
from E02 (4)–(5). By E02 (6), for \(p=u+iv\) throughout the strip,
\[
 |Z(p,t)|\le A_b e^{\Theta |v|},\qquad
 A_b=4C_{\rm u}L(q_0/a^2)^b+
          2C_{\rm u}(\ell^2 q_0)^b E_1(2b-1)\Lambda(1).
 \tag{1}
\]
The monotonicity in \(u\) uses \(|\mu_j|<1\).
The same upper bound applies to the retained divisor sum.
On vertical sides \(q=b,r\) the kernel satisfies
\[
 |K(q+iv,t)|\le
 C_\epsilon e^{-\epsilon v^2}/\sqrt{\lambda^2+v^2}.
 \tag{2}
\]
On \(\Im p=\pm Y\) with \(b\le u\le r\) and \(Y>0\),
\(|K(p,t)|\le C_\epsilon e^{-\epsilon Y^2}/Y\).
These follow from
\(\Re((p-n)^2)=(u-n)^2-v^2\) and the real-part distances in the table.
The constants are uniform in real time and include the growing-height
and collar parameters through (1).

## 2. Rectangle, limit and exact evolution

Let \(\mathscr C_\gamma B=(2\pi i)^{-1}\int_\gamma B(p)\,dp\).
For \(q=b,r\), \(V_q(Y)\) runs upward from \(q-iY\) to \(q+iY\).
Let \(\mathcal H_Y(B)\) be the normalized integrals of \(B\) over the
bottom edge from \(b-iY\) to \(r-iY\), and top edge from \(r+iY\) to
\(b+iY\). At every time in the local chart, E02 gives holomorphy of
\(Z\) on \(\Re p>1/2\). Counterclockwise residue evaluation gives
\[
 \sum_{n\in\mathcal N}c_n(t)Z(n,t)
   =\mathscr C_{V_r(Y)}(K Z)-\mathscr C_{V_b(Y)}(K Z)+\mathcal H_Y(K Z).
 \tag{3}
\]
At a pole the damping evaluates to one. If \(\delta=0\), the
candidate pole at 3 is removable. Define
\(\Phi_\theta(Y)=e^{-\epsilon Y^2+\theta Y}\) and
\(\kappa_\theta(Y)=2\epsilon Y-\theta\).
Equations (1)–(2) give
\[
 |\mathcal H_Y(K Z)|\le
 \frac{(r-b)C_\epsilon A_b}{\pi Y}\,\Phi_\Theta(Y).
 \tag{4}
\]
Both vertical lines converge absolutely. For \(Y>\theta/(2\epsilon)\),
\(\Phi_\theta(v)\le\Phi_\theta(Y)e^{-\kappa_\theta(Y)(v-Y)}\)
when \(v\ge Y\). In particular,
\[
 \int_Y^\infty\Phi_\theta(v)\frac{dv}{v}
 \le \frac{\Phi_\theta(Y)}{Y\kappa_\theta(Y)} .
 \tag{5}
\]
Let \(V_q\) be the full upward line and write
\(\mathcal V(B)=\mathscr C_{V_r} B-\mathscr C_{V_b} B\)
with the strip of the chosen row. The absolute error in \(\mathcal V(KZ)\)
from omitting \(|v|>Y\) is at most
\[
 \frac{2C_\epsilon A_b}{\pi}\,
       \frac{\Phi_\Theta(Y)}{Y\kappa_\Theta(Y)} .
 \tag{6}
\]
The factor \(2/\pi\) includes the two tails on each of two lines.
The same bound holds for \(Z_N\). Equations (4) and (6) pay both ways
of taking the height limit of (3). They also apply with a smaller
uniform branch cap, such as E08's \(5\pi/4\) on compatible charts.

In the \(F\) row write \(K_\epsilon=K\). The \(m\) row uses
\(G_\epsilon=e^{\epsilon(p-1)^2}/(p-1)\) and its own \(\mathcal V\).
Use \(Z(n)=\ell^{2n}S_n\), and \(M=S_1\) is the negative of the
inherited physical interaction \(K\). This gives
\[
 \begin{aligned}
 F&=\mathcal V(K_\epsilon Z)=12Z(2)+16\delta Z(3)
                         =\ell^4(12S_2+16DS_3),\\
 m&=\mathcal V(G_\epsilon Z)=Z(1),\\
 M'&=2M^2-\ell^{-4}\mathcal V(K_\epsilon Z),\\
 m_\sigma&=2m^2-\mathcal V(K_\epsilon Z),\qquad
 \delta_\sigma=2-4m\delta .
 \end{aligned}                                                 \tag{7}
\]
The unscaled derivative uses physical \(t\). The nonlinear term
stays local. The right lines in (7) are part of the formula.
The inherited exact cost is
\(W(x,y)\delta(x)=\delta(y)-2\int_x^y W(u,y)\,du\),
\(W(x,y)=\exp(-4\int_x^y m)\), with an independently paid tube and
terminal value, and equality allowed at the initial endpoint.
[E01][e01] · [Parent Note41][n41] · [Assessment19][a19]

## 3. Complete divisor limit and exact residue error

For integer \(N>4T+8\), use E02's canonical modulus cutoff retaining
\(|\rho_j|\le N\), including all tied occurrences. Write \(Z_N\) with
the same logs. By E02 (7) and \(\ell^2q_0<1\),
\[
 |Z-Z_N|\le B_N e^{\pi|v|/2},\qquad
 B_N=2C_{\rm u}(\ell^2 q_0)^b E_1(2b-1)3^{2r-1}
             N^{1-2b}\Lambda(N)
 \tag{8}
\]
on the full strip, where all omitted powers have principal logs.
For \(Y\) finite, replacing \(A_b,\Theta\) in the bounds on \(KZ\)
by \(B_N,\pi/2\) pays the cutoff on the rectangle. An explicit bound
on the two full verticals is
\[
 |\mathcal V(K(Z-Z_N))|
 \le \frac{2C_\epsilon B_N}{\pi\lambda}
         \sqrt{\frac{\pi}{\epsilon}}\,
         e^{\pi^2/(16\epsilon)} .
 \tag{9}
\]
Indeed for \(\theta\ge0\) the half-line integral of
\(e^{-\epsilon v^2+\theta v}\) is at most
\(\sqrt{\pi/\epsilon}\,e^{\theta^2/(4\epsilon)}\), by completing the
square and enlarging to a full translated line. Using the same
normalization as in (6) with \(\lambda^{-1}\) yields (9).
Thus one can first take \(N\to\infty\) on each finite rectangle, then
\(Y\to\infty\). The uniform-in-\(N\) tail bound and (9) also justify
the two full verticals of the limit and joint passage if \(N,Y\)
both tend to infinity at fixed \(\epsilon,T\).

The sharper signed value remainder uses the **same** rectangle
on \(Z-Z_N\). Let \(F_N=\mathcal V(K_\epsilon Z_N)\), with full
verticals. Then
\[
 \begin{aligned}
 F-F_N&=12(Z(2)-Z_N(2))+16\delta(Z(3)-Z_N(3)),\\
 |F-F_N|&\le12\,R_2(N)+16d\,R_3(N),\\
 R_n(N)&=2C_{\rm u}(\ell^2q_0)^n E_1(2n-1)3^{2n-1}
                       N^{1-2n}\Lambda(N).
 \end{aligned}                                                  \tag{10}
\]
The first line evaluates the complete signed remainder before applying
absolute values. \(R_n\) follows from E02 (7) at the integer, using
the dyadic shell bound at exponent \(n\) and \(\lfloor N/2\rfloor\ge N/3\).
The two terms in (10) have orders \(\ell^4N^{-3}\log N\) and
\(d\ell^6N^{-5}\log N\) with explicit constants displayed.
The \(m\) row analog gives \(|m-\mathcal V(G_\epsilon Z_N)|\le R_1(N)\).
For cut verticals add the error (6) to the appropriate residue
allowance. These are bounds for cutoff values.

## 4. Physical differentiation and the independent spatial limit

On a compact subchart of E02, let \(C_Z\) denote the bracket in E02 (16)
for the chosen \(b,r\), using its finite circle/connector and safe-line
constants. With \(J=1+|p|\), E02 supplies there
\[
 |Z_t(p,t)|\le C_Z J^2e^{\Theta|v|}.
 \tag{11}
\]
Here and below \(t\) is physical time. The full derivative kernel is
\[
 \begin{split}
 (K_\epsilon Z)_t&=K_\epsilon Z_t+
           \frac{16(D'/\ell^2)e^{\epsilon(p-3)^2}}{p-3}Z,\\
 (G_\epsilon Z)_t&=G_\epsilon Z_t .
 \end{split}                                                     \tag{12}
\]
For the \(F\) row set \(C_{\epsilon,t}=16(C_D/\ell^2)e^{4\epsilon}\)
with \(C_D=\sup_I|D'|\) as bounded in E02 (15). For the \(m\) row
take \(C_{\epsilon,t}=0\). The same kernel bound as in (2)
holds for \(K_t\), with \(C_{\epsilon,t}\) in place of \(C_\epsilon\).
On either vertical \(J\le U+|v|\) with \(U=1+r\). Equations (1),
(2), (11) and (12) give a Gaussian-integrable majorant for the
complete time derivative, uniform on each compact subchart. Dominated
differentiation and continuity under the integral give
\[
  \frac{d}{dt}\mathcal V(KZ)=\mathcal V(K_t Z+K Z_t).
 \tag{13}
\]
The derivative of the finite rectangle's horizontal contribution
is bounded by
\[
 \frac{r-b}{\pi Y}\,
       [C_\epsilon C_Z(U+Y)^2+C_{\epsilon,t}A_b]\,\Phi_\Theta(Y).
 \tag{14}
\]
For \(Y>\Theta/(2\epsilon)\), the derivative's omitted vertical tails
have bound
\[
 \frac{2\Phi_\Theta(Y)}{\pi}
 \left[
  C_\epsilon C_Z(1+U/Y)^2
      \left(\frac{Y}{\kappa_\Theta(Y)}+\frac{1}{\kappa_\Theta(Y)^2}\right)
  +\frac{C_{\epsilon,t}A_b}{Y\kappa_\Theta(Y)}
 \right].
 \tag{15}
\]
Here \((U+v)^2/v\le(1+U/Y)^2 v\) for \(v\ge Y\), and the
exponential bound preceding (5) integrates \(v\). This also proves
that a differentiated finite-rectangle calculation has the same
limit. Both statements use the full \(Z_t\) and retain moving \(c,D\)
through the E02 law.

For clarity, the spatial boundary cutoff \(X\ge7\) in E02 (15a)
omits the tails of the four safe horizontal rays in its spatial
contour. It leaves both finite connectors and all finite cluster
circles. Denote the cut value by \(Z^{[X]}\) and its physical derivative
by \(Z_t^{[X]}\). For the derivative of the cut value use E02's
\(\partial_t(f_p h)\) form on the cut contours. The integrated-by-parts
\(B_p\) form at finite \(X\) would also require its primitive endpoint
terms. Put
\[
 \begin{aligned}
 U_0(X)&=\frac{2A}{\pi}(2\ell^2)^b E_1(2b-1)
                              X^{1-2b}\Lambda(X),\\
 U_1(X)&=\frac{2C_{\rm sl}}{\pi}(2\ell^2)^b E_2(2b-1)
                              X^{1-2b}\Lambda(X)^2 ,
 \end{aligned}
\]
where \(A,C_{\rm sl}\) are the explicit safe-line constants in E02
(15)–(15a). The inequalities \(2\ell^2<1,\ X\ge7\) let one bound all
real parts on the strip by \(b\) in these prefactors. Then
\(\lvert Z-Z^{[X]}\rvert\le U_0(X)e^{\pi|v|/2}\) and
\(\lvert Z_t-Z_t^{[X]}\rvert\le U_1(X)J^2e^{\pi|v|/2}\).
For a full vertical difference, the resulting physical derivative error
is at most
\[
 \frac{2}{\pi\lambda}\int_0^\infty
   [C_\epsilon U_1(X)(U+v)^2+C_{\epsilon,t}U_0(X)]
              e^{-\epsilon v^2+\pi v/2}\,dv .
 \tag{16}
\]
The analogous value error uses \(C_\epsilon U_0(X)\) in the brackets.
All Gaussian moments here are finite at fixed \(\epsilon>0\).
This supplies derivative convergence through spatial-boundary integrals.
It allows taking \(X\to\infty\) first on each finite \(p\)-rectangle
and then \(Y\to\infty\), or taking \(X\to\infty\) in the full verticals
by (16). The sharp divisor cutoff \(N\) supplies only (8)–(10).
There is no differentiation of a sharp \(N\) cutoff or of zero labels.

## 5. Folding and chart transitions

On E08's compatible charts take \(B=KZ\). Since \(K^\sharp=K\) at real
time, E08 gives \(B^\sharp=B\) for \(B^\sharp(p)=\overline{B(\bar p)}\).
The same property holds for \(G_\epsilon Z\). Writing an upward line
with \(p=q+iv\) gives
\[
 \mathcal V(B)=\frac1\pi\int_0^\infty
                \Re\,[B(r+iv)-B(b+iv)]\,dv .
 \tag{17}
\]
For a finite rectangle, the two horizontals in (3) are still present.
One may fold each vertical as in (17) with upper limit \(Y\) and carry
both horizontals, or use E08 (9) to fold the full upper arc into the
lower arc with its opposite reflected orientation.

For the alternative \(+\pi\) boundary prescription at a fixed slice,
put \(B_+=KZ_+\) and \(\mathcal D_B=B_+-B_+^\sharp\). By E08 (5), (7),
\[
 \mathcal D_B(p,t)=-2iK(p,t)\,\ell^{2p}\sin(\pi p)
                              \sum_{j:a_j<0}|a_j|^{-p}.
 \tag{18}
\]
The finite near sum includes both conjugate locations with all
multiplicities. For either kernel, the exact fold on a line is
\[
 \mathscr C_{V_q}B_+
  =\frac1\pi\int_0^\infty\Re B_+(q+iv)\,dv
   +\frac1{2\pi}\int_0^\infty \mathcal D_B(q-iv)\,dv .
 \tag{19}
\]
Absolute convergence follows from (1)–(6) for \(B_+\) and its reflection,
with twice the bound for their difference. In the two-line fold take the right-minus-left
difference of both terms on the right of (19). The complete closed
contour formula has the same integer residues for this prescription.
The \(+\pi\) slice convention has no asserted time differentiability.

For charts \(A,B\) use the finite overlap correction of E02 (17)
and E08 (6),
\[
 \Delta Z=Z_B-Z_A=\sum_C(e^{-2\pi i k_Cp}-1)Z_{A,C},
 \tag{20}
\]
with occurrence multiplicities and constant integer shifts on a local
refinement. Its integer values at the residue positions vanish.
Consequently \(K\Delta Z\) has removable poles and integrates to zero
on the complete finite rectangle. The same conclusion holds for
\(\mathcal D_B\) in (18) since the sine vanishes at the residue
positions. The regular values after pole removal can be nonzero.
Apply (4)–(6) to the differences using twice the stated envelope.
This proves
\[
  \mathcal V(K\Delta Z)=0,\qquad \mathcal V(\mathcal D_B)=0 .
 \tag{21}
\]
It proves equality of the full correction integrals on the two
vertical lines. Each line's correction must be kept in its line formula
and (19) still contains the lower-half defect integral.

On overlaps of analytic time charts, (20) also holds after
differentiation of the cluster traces. Its integer derivatives vanish.
Thus \((K\Delta Z)_t=K_t\Delta Z+K\Delta Z_t\) is again regular at the
residue positions, and (14)–(15) apply to its horizontal/vertical
bounds. The integer observables in (7) and their physical derivatives
therefore glue on the finite real-time chart cover, with inward
derivatives at paid endpoints. A maximum over the compact subchart
constants supplies uniformity on this fixed tube. This uses an atlas
of noninteger logs.

## 6. Scope and quantitative gate

The proof uses the local heat and contour laws, a counted isolated
pair, the exterior strip and unit-count upper bound, inherited
order-one product and safe-line control for the time law, and local
analytic logs or the explicit slice correction. It reuses E01 and
E02 §6's documentary screen. In that screen finite polynomial
collisions lack the canonical growing population yet share the local
residue algebra. Euler factors change canonical endpoint discrepancy
and arithmetic, with the coarse upper count still possible. The
documented endpoint-defective weighted-square and finite-source/prime
classes fail the fixed strip. The reflected super-Gaussian fails the
order-at-most-one input for the inherited product. The smooth and
positive-primitive controls change arithmetic with strip/count/safe-line
transfer unpaid. Atomic/finite-profile controls lack the canonical
population and profile. Conditional endpoint mergers assume RH and
change ordinary Dirichlet arithmetic. Changed observations and
fractional profiles fail the physical readout and integer divisor,
respectively. GR changed static slices lack the canonical common-time
tube and its scalar equilibrium has no realized complete divisor.
These distinctions identify the inherited premises used. The added
Gaussian in \(p\) is an analytic contour device and supplies no
collision discriminator. [E01][e01] · [E02 §6][e02] · [E08 §5][e08] ·
[Controls12][controls]

The damping, real edges, and residue orders \(2,3\), separately \(1\),
are all fixed. The proof pays \(N,Y\), and independently \(X\) for the
spatial derivative, at fixed \(T\) with the displayed height dependence.
There is no \(P\) limit, right-real-edge limit, \(\epsilon\downarrow0\)
limit or extension past \(\Re p=1/2\). No signed upper improvement over
the direct \(C_F L\) forcing allowance or improved transport cost is
proved. The useful quantitative comparison remains with the equally
informed signed residue sum. E04 assesses the three coupled proofs
before their quantitative use.

[request]: ../research-progress/handoffs/VCD-GT-CM-E03-r1.md
[decision]: ../brainstorm/notes/01_VCD_GT_CM_B01_DAMPED_CAUCHY_DECISION_20261117.md
[e01]: ../reviews/02_VCD_GT_CM_E01_INPUT_AUDIT_20261117.md
[e02]: 03_VCD_GT_CM_E02_COMPLEX_POWER_TIME_LAW_20261117.md
[e08]: 04_VCD_GT_CM_E08_CONJUGATION_AND_BRANCH_DEFECT_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[a19]: ../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
