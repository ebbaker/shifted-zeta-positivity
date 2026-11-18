# VCD-GT-CM-E05 r1 — Signed forcing comparison for the damped Cauchy contour

17 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Requested helper dispatch **gpt-6.1-sol / ultra**.
Independent actual serving model and reasoning effort metadata were unavailable.

**Proved in-note on the stated classes, pending E06 assessment.** All
seven pins in the [frozen request][request] matched. The contour formula
is a representation. This note bounds its full absolute envelope and
tests a signed upper estimate in the enlarged-constant static class.
[B02][decision] · [E04][assessment] · [Result index][results] ·
[Cluster18][cluster] · [Avoid index][avoid] · [Classification01][class] ·
[Scope07][scope] · [Joint bounds12][joint]

## 1. Full two-line envelope and the direct bound

Keep the E04 domain on the independently paid compact real count-two
tube for the complete canonical \(H_t=-H_{zz}\). Freeze \(T\ge64\),
\(L=\log T\), \(\ell=L^{-1}\), \(a,d\) as in E02, and use
\(c\in[T,2T]\), the counted targets \(c\pm\sqrt D\), and the full
exterior divisor, including repeats. Thus \(|\Im w_j|\le1\),
\(|w_j|\ge a\ell\), \(|D|\le d\ell^2\le a^2\ell^2/16\), and with
\(a_j=w_j^2-D,\ \mu_j=\ell^2/a_j,\ q_0=16/15\) and
\(g=q_0/a^2<1\), we have \(|\mu_j|\le g\). Write
\(\delta=D/\ell^2\), \(\mathcal A_u=\sum_j|\mu_j|^u\), and
\(B_n=14C_{\rm u}g^n\) from [Note41 §3][baseline]. In particular
\(\mathcal A_1\le A_1:=B_1L\) holds uniformly on the tube.
The chart value \(Z(u+iv)\) satisfies
\[
 |Z(u+iv)|\le\mathcal A_u e^{\Theta|v|}
             \le \mathcal A_1 g^{u-1}e^{\Theta|v|}\qquad (1\le u\le4).
 \tag{1}
\]
The second bound is occurrence-wise. Take \(\Theta=3\pi/2\) generally,
or \(5\pi/4\) on the compatible charts.
[E02 (6)][e02] · [E08 §1][e08] · [E04 §§2–3][assessment]

Fix \(\epsilon>0\) and use the E03 kernel and two-line difference
\[
 K_\epsilon(p,\delta)
    =\frac{12e^{\epsilon(p-2)^2}}{p-2}
       +\frac{16\delta e^{\epsilon(p-3)^2}}{p-3},\qquad
 \mathcal V(K_\epsilon Z)
    =\frac1{2\pi}\int_{\mathbb R}
       [K_\epsilon(4+iv)Z(4+iv)-K_\epsilon(1+iv)Z(1+iv)]\,dv .
\]
The upward right line minus the upward left line is the limit of
the positive rectangle with its two horizontal edges. The kernel
bound on each vertical is
\(|K_\epsilon(u+iv)|\le C_\epsilon e^{-\epsilon v^2}/\sqrt{1+v^2}\)
with \(C_\epsilon=(12+16d)e^{4\epsilon}\). The full absolute
two-line norm obeys
\[
\begin{split}
 |F|&=|\mathcal V(K_\epsilon Z)|
 \le \frac1{2\pi}\int_{\mathbb R}\sum_{q\in\{1,4\}}
             |K_\epsilon(q+iv)Z(q+iv)|\,dv \\
 &\le\frac{2C_\epsilon\mathcal A_1}{\pi}
        \int_0^\infty
           \frac{e^{-\epsilon v^2+\Theta v}}{\sqrt{1+v^2}}\,dv
 \le C_{\rm env}\,A_1,\qquad
 C_{\rm env}=\frac{2C_\epsilon}{\pi}
           \sqrt{\frac{\pi}{\epsilon}}e^{\Theta^2/(4\epsilon)}.
\end{split} \tag{2}
\]
The middle coefficient \(2\) can be replaced by \(1+g^3\) using
(1) on the right line. The closed-form last bound comes from
completing the square and enlarging the translated integral to
the real line. The direct allowance at the same \(\mathcal A_1\)
is
\[
 |12Z(2)+16\delta Z(3)|
 \le (12g+16d g^2)\mathcal A_1\le C_F L,\qquad
 C_F=12B_2+16dB_3.
 \tag{3}
\]
Thus the simple envelope (2) gives the same height order and a
larger closed-form coefficient. In fact
\(C_{\rm env}/(12+16d)\ge2\sqrt{8e/\pi}>1\) by minimizing
\(e^{4\epsilon}/\sqrt\epsilon\); (3) has coefficient
\(12g+16dg^2<12+16d\). Schwarz folding gives a real integral but
does not change the rate in (2). The group comparison below also
applies after preserving the right-minus-left difference.
[E03 §§1–2, 5][e03] · [E04 §4][assessment]

Use the common integer modulus cutoff \(N>4T+8\), including all ties.
The same two-line integral of \(Z-Z_N\) equals the exact signed
residue remainder
\[
 F-F_N=12[Z(2)-Z_N(2)]+16\delta[Z(3)-Z_N(3)],\quad
 |F-F_N|\le12R_2(N)+16dR_3(N),
 \tag{4}
\]
where \(F_N=12Z_N(2)+16\delta Z_N(3)\) and
\[
 R_n(N)=2C_{\rm u}(\ell^2q_0)^n E_1(2n-1)3^{2n-1}
                      N^{1-2n}\log(3+2T+N),\qquad
 E_1(\gamma)=\sum_{k\ge0}2^{-k\gamma}(1+(k+1)\log2).
\]
This is the sharper branch-independent value allowance, of orders
\(\ell^4 N^{-3}\log N\) and \(d\ell^6N^{-5}\log N\). It costs
the direct comparator exactly the same. For \(Y\) cut verticals add
the E03 (6) bound with \(A_b=A_1\), \(Y>\Theta/(2\epsilon)\);
the horizontal contribution for finite rectangles is E03 (4)
with \(r-b=3\). The strip-wide, coarser integrated \(N\) bound
remains E03 (9). The separate \(m\) contour uses E03's fixed
\([3/4,3/2]\) strip and residue error \(R_1(N)\).
The independent spatial boundary cutoff \(X\ge7\) and derivative
tails, including the differentiated kernel and the finite spatial
connectors, are exactly E02 (15a) and E03 §§3–4. The \(N,Y\)
limits for values and the \(X,Y\) limits for differentiation hold
at fixed \(T,\epsilon\) in the orders authorized there. No derivative
of a sharp \(N\) cutoff is used. [E02 §§2, 4][e02] ·
[E03 (4), (6), (8)–(16)][e03] · [E04 §4][assessment]

## 2. Group contour norms and signed residues

For each occurrence define \(f_j(p)=\exp(p(2\log\ell-\log a_j))\)
with its assigned log. Take any partition into single occurrences
or prescribed finite groups \(G\), and write \(Z_G=\sum_{j\in G} f_j\).
For \(q=1,4\) put \(I_{q,G}(v)=K_\epsilon(q+iv,\delta)Z_G(q+iv)\).
The positive-rectangle residue identity for a group, with its
horizontal terms vanishing by the same Gaussian bound, yields
\[
 \frac1{2\pi}\int_{\mathbb R}[I_{4,G}(v)-I_{1,G}(v)]\,dv
       =F_G:=\sum_{j\in G}(12\mu_j^2+16\delta\mu_j^3).
 \tag{5}
\]
For a conjugate pair with matched branches and multiplicities the
pair value is \(2\Re(12\mu^2+16\delta\mu^3)\) per matched pair.
If the group is conjugation-closed with compatible logs, its
weighted integrand has Schwarz symmetry and (5) is also
\(\pi^{-1}\int_0^\infty\Re[I_{4,G}(v)-I_{1,G}(v)]\,dv\).
An absolute contour estimate for each group therefore satisfies
\[
 |F_G|\ \le\frac1{2\pi}\int_{\mathbb R}|I_{4,G}-I_{1,G}|\,dv
      \ \le\frac1{2\pi}\int_{\mathbb R}(|I_{4,G}|+|I_{1,G}|)\,dv .
 \tag{6}
\]
For Schwarz groups the folded absolute real-difference norm,
\(\pi^{-1}\int_0^\infty|\Re(I_{4,G}-I_{1,G})|\,dv\), also lies
between \(|F_G|\) and the first absolute integral in (6).

To justify the complete comparison, on each vertical
\(\sum_G|I_{q,G}(v)|\le
C_\epsilon e^{-\epsilon v^2+\Theta|v|}\mathcal A_1/\sqrt{1+v^2}\).
Thus the sum of group norms is finite by (2), and summation and
integration interchange absolutely. On the two horizontals
the group sum is bounded using \(|p-n|\ge Y\) for each kernel
pole \(n\), giving the E03 (4) bound with \(A_1\) and \(r-b=3\).
It tends to zero as \(Y\to\infty\).
Also \(\sum_G|F_G|\le (12g+16dg^2)\mathcal A_1\). Hence \(F=\sum_G F_G\)
and a triangle inequality applied group by group is at least
\(\sum_G|F_G|\), the signed-residue norm for the same grouping.
Retaining joint signs across groups is available on either side of (5).
This comparison concerns the indicated use of absolute norms.

## 3. Complete static witness with Schwarz symmetry

Reuse [GR E06 §§3–4(i)][grproof] and its [E07 assessment][grreview].
Take \(c=T=e^L,\ L\ge16,\ a=4,\ d=1,\ D=0,\ b_{\rm core}=8\),
and \(J=\lfloor L\rfloor\). Remove every occurrence of \(H_0\)
in the closed bands \(|\Re \rho\mp c|\le3\) by dividing by the
polynomial with those factors. Insert at \(+c\) the double target,
\(J\) occurrences at each \(w=\pm b_{\rm core}\ell\), and
\(J+1\) at each \(w=\pm i b_{\rm core}\ell\). Insert their negations
at \(-c\). The quotient and multiplication give the inherited
real-even order-one entire fields and complete width-one strip.
The centered collar at \(+c\) is \(4/L\); the real and imaginary
core displacements have modulus \(8/L\), the remaining original
background has \(|\Re w|>3\), and every reflected insertion has
\(|\Re w|\ge c\). The reflected target is exterior to the selected
pair.

For each band the operation removes at most \(12C_{\rm u}L\)
occurrences and inserts \(4J+4\le5L\), all insertion projections
within \(1/2\) of their band center. A unit interval meeting new
occurrences meets only one band and has start \(v_0\) with
\(|v_0|\ge c-2\). The complete unit count therefore uses
\(C_{\rm u}+5\). On the positive axis the cumulative count change
is zero for \(x<c-3\) and at most
\((12C_{\rm u}+5)L\le(24C_{\rm u}+10)\log(2+x)\) thereafter,
so the inherited growing main term and logarithmic discrepancy
persist with enlarged constants. The static safe-line constant
may be taken as \(C_{\rm u}+5(24C_{\rm u}+10)\). For each fixed
\(0<\beta<1/2\) the broad transverse tail bound inherits its density
constant enlarged from \(B_\beta\) to \(B_\beta+e^{16\beta}\), and
the static local averaged moments follow with the corresponding
enlarged constants in GR E06 §3. All these enlargements are fixed
in \(L\). The construction changes the source and can change the
exact projected counts. [GR E06 §3][grproof] · [GR E07][grreview]

For \(Q=w^2\), take real logs on the real core denominators and
opposite arguments \(+\pi,-\pi\) on the two imaginary core
locations, with every repeated occurrence at a location carrying
its log. Use the principal log on the **entire noncore**
since \(|\Re w|>3,\ |\Im w|\le1\) gives \(\Re(w^2)>8\) there.
These assignments are spatially analytic on small zero-cluster
neighborhoods at the slice. Conjugation permutes the full
occurrence list and conjugates its logs. The complete sum is
\[
 Z(p)=b_{\rm core}^{-2p}\big[2J+2(J+1)\cos(\pi p)\big]+R(p),
 \qquad
 R(p)=\ell^{2p}\sum_{\rm noncore}\exp(-p\log_{\rm pr}(w^2)).
 \tag{7}
\]
In particular the phase cap is \(\pi\) on the slice and \(\pi/2\)
on the remainder. For \(u\ge1\) the retained original shells
\(n\le|\Re w|<n+1,\ n\ge3\), have count at most
\(2C_{\rm u}(2L+\log(n+1))\). Their absolute physical-power sum
with exponent \(2u\) is at most
\(2C_{\rm u}(4L+3)\le10C_{\rm u}L\), using the exponent-two
series from [Note41 §3][baseline]. The opposite-band insertions,
including its double target, cost at most \(5Lc^{-2u}\), hence
\[
 |R(u+iv)|\le (10C_{\rm u}+5)L^{1-2u} e^{\pi |v|/2}
                        \qquad (1\le u\le r)
 \tag{8}
\]
for every fixed finite \(r\). For \(b>1/2\) the same shell count
with \(n^{-2b}\), and the finitely many reflected insertions,
give normal convergence on compact subsets of \(u>1/2\).
The full \(Z\) is therefore holomorphic on that half-plane and
\(Z^\sharp=Z\) there. The occurrence bound (1) with the enlarged
count works on \([1,4]\), and the same monotonicity from
\(\mathcal A_{3/4}\) gives a finite envelope on \([3/4,3/2]\).
For both fixed-\(\epsilon\) kernels the Gaussian bound therefore
pays the complete vertical integrals and the vanishing
horizontal edges, with the value cutoff estimate at fixed
\(T,\epsilon\) from the same enlarged unit count and strip.
The Schwarz property extends to the full weighted integrands
because \(\delta\) and the other kernel coefficients are real.
These are slice properties.

Using (8) at the integer residues gives
\[
 \begin{split}
 m&=-2/b_{\rm core}^2+R(1),&
 |R(1)|&\le(10C_{\rm u}+5)L^{-1},\\
 F&=12(4J+2)/b_{\rm core}^4+12R(2),&
 |12R(2)|&\le12(10C_{\rm u}+5)L^{-3}.
 \end{split} \tag{9}
\]
Thus \(m\le-1/64\) eventually and \(F/L\to3/256>0\).
The static class consisting of such collar-counted real-even
order-one entire slices, with the width-one strip, the growing
count, safe-line and broad transverse bounds at the stated fixed
enlarged constants, and with complete holomorphic \(Z\), compatible
Schwarz symmetry and fixed-\(\epsilon\) Gaussian integrability,
admits no uniform \(o(L)\) forcing upper bound even after adding
\(m\le-1/64\). It also rules out that bound for the version with
\(m<0\). The quantifier allows the enlarged constants and the
family need not satisfy any particular smaller canonical constant.
The witness supplies neither the unchanged theta source nor a
common paid canonical heat tube. Imposing E02's time law would
change the class in this exclusion.

## 4. Exact consumer and scope

On the canonical paid tube keep
\(\sigma=(t-t_0)/\ell^2,\ m=\ell^2 M,\ m_\sigma=2m^2-F\)
and \(\delta_\sigma=2-4m\delta\), with both signs of \(D\).
For a complete signed upper bound \(F\le Q\) throughout that tube,
the inherited comparison uses \(K_+=\max(Q,0)\) and \(A_0=B_1L\).
Let \(f''=2K_+f,\ f(0)=1,\ f'(0)=2A_0\), and
\(g_{\rm tr}''=2K_+g_{\rm tr},\ g_{\rm tr}(0)=0,\ g_{\rm tr}'(0)=1\).
The lower barrier \(-f'/2f\) pays the finite initial layer.
For paid scaled \(x\le y\) the requirements are
\[
 \begin{gathered}
 W(x,y)=e^{-4\int_x^y m},\quad W(x,y)\le[f(y)/f(x)]^2,\quad
 \int_x^y W(u,y)\,du\le \frac{f(y)}{f(x)}g_{\rm tr}(y-x),\\
 W(x,y)\delta(x)=\delta(y)-2\int_x^y W(u,y)\,du .
 \end{gathered} \tag{10}
\]
The exact terminal cost includes the factor \(2\), and the
physical \(D\) cost multiplies by \(\ell^2\). Gap inference uses
an independent terminal anchor and retains equality at \(\delta(x)=0\),
also at the initial endpoint. Forward comparison uses the independent
incoming gap. Applying the direct \(Q=C_F L\) retains the
\(O(\sqrt L)\) interior negative allowance after a fixed scaled
buffer and \(O(L)\exp(O(\sqrt L))\) upper multiplier for fixed
collar parameters and fixed scaled duration.
[Note41 §§3–4][baseline] · [Assessment19][baselinecheck] · [GR E06 §2][grproof] · [GR E07][grreview]

The equally informed direct comparator receives the same complete
divisor, branch assignments, signed residues, \(m\) information,
cutoff errors, physical tube and anchors. It applies the same
Riccati and transport equations. The new exclusion concerns the
specified static inputs, including the complete complex-index
properties. A signed upper forcing estimate using the canonical
dynamics, or an integrated bound for the complete canonical cost
in (10), remains open.

The documented controls are screened at these premises.
Quadratic and quartic collision fields lack the canonical growing
population yet share the local contour algebra. Euler translates
change theta arithmetic and endpoint discrepancy. Weighted-square
and finite-source/score/prime controls fail the full reflected
unit-weight theta expansion, and the documented endpoint-defective
subclasses fail the strip. The reflected super-Gaussian fails the
order bound. Smooth and positive-primitive controls change theta
arithmetic, with strip/count/safe-line transfer unpaid. Atomic
and finite-profile controls lack the canonical population and full
profile. RH-conditional endpoint mergers change ordinary Dirichlet
arithmetic and retain RH as a premise. Changed observations lack
the physical cosine readout and fractional profiles lack integer
multiplicities. The GR surgery changes the source and supplies no
common paid canonical dynamics. The scalar equilibrium supplies no
realized divisor. This is a documentary check of the actual premises.
[Controls12][controls] · [Premises02][premises] · [E01][audit] ·
[E04 §5][assessment] · [GR E07][grreview]

[request]: ../research-progress/handoffs/VCD-GT-CM-E05-r1.md
[decision]: ../brainstorm/notes/02_VCD_GT_CM_B02_SIGNED_BOUND_CONTRACT_20261117.md
[assessment]: ../reviews/03_VCD_GT_CM_E04_CONTOUR_PROOFS_ASSESSMENT_20261117.md
[audit]: ../reviews/02_VCD_GT_CM_E01_INPUT_AUDIT_20261117.md
[e02]: 03_VCD_GT_CM_E02_COMPLEX_POWER_TIME_LAW_20261117.md
[e08]: 04_VCD_GT_CM_E08_CONJUGATION_AND_BRANCH_DEFECT_20261117.md
[e03]: 05_VCD_GT_CM_E03_DAMPED_CAUCHY_EVOLUTION_20261117.md
[grproof]: ../../01_gaussian_resolvent_hierarchy/notes/05_VCD_GT_GR_E06_FORCING_TRANSFER_AND_COST_20261117.md
[grreview]: ../../01_gaussian_resolvent_hierarchy/reviews/05_VCD_GT_GR_E07_FORCING_AND_SCOPE_ASSESSMENT_20261117.md
[baseline]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[baselinecheck]: ../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

