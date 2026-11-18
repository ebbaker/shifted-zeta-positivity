# VCD-GT-GR-E06 r1 — Fixed-scale forcing transfer and microscopic cost

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Requested executor configuration
**gpt-6.1-sol / ultra**. Actual serving model and reasoning effort were
unavailable to the executor.

**Proved in-note, pending separate internal assessment.** The six
[frozen input pins][request] match. The transfer is a quantified
approximation on the paid canonical tube. The Riccati consumer is
conditional on a signed bound throughout that tube. The two comparators
concern fixed-slice real-even entire divisor fields. [B02][b02] ·
[Result index][results] · [Cluster18][cluster] · [Avoid index][avoid] ·
[Classification01][class] · [Scope07][scope] · [Joint bounds12][joint]

## 1. Complete fixed-physical-scale transfer

Keep the complete canonical \(\partial_t H=-H_{zz}\) on the independently
paid compact count-two tube \([t_0,t_1]\subset[0,1/2]\). Freeze \(T\ge64\),
\(L=\log T\), \(\ell=L^{-1}\), \(d\ge0\),
\(\max(2,4\sqrt d)\le a\le L\), \(r_0=a\ell\). The real coordinates
satisfy \(T\le c\le2T\), \(|D|\le d\ell^2\le r_0^2/16\). The two
targets are within \(r_0/4\) of \(c\) and each exterior occurrence has
\(|w_j|=|\rho_j-c|\ge r_0\), \(|\Im w_j|\le1\). Put
\[
 a_j=w_j^2-D,\quad \mu_j=\ell^2/a_j,\quad
 S_p=\sum_j a_j^{-p},\quad M=S_1,\quad m=\ell^2M,\quad
 \delta=D/\ell^2,\quad q_0=16/15.
\]
Sum over occurrences, including multiples. All estimates below use
\(|w_j|^2\le q_0|a_j|\), so \(D\) can have either sign or be zero.
[E02][e02] · [E03][e03] · [E05][e05]

Take \(C_{\rm u}\ge1\) as in [Note41 §3][n41]. The closed unit count
bounds the band \(|\Re w|<1\) by \(4C_{\rm u}L\) and each shell
\(n\le|\Re w|<n+1\), \(n\ge1\), by
\(2C_{\rm u}(2L+\log(n+1))\), using two unit intervals in each case.
The kernel bound is \(q_0/a^2\) on the near band and \(q_0\ell^2/n^2\)
on shell \(n\). For \(p=1,2,3\), the far sum is at most
\(10C_{\rm u}q_0^p L^{1-2p}\) since
\(\sum_{n\ge1}n^{-2p}\le2\),
\(\sum_{n\ge1}n^{-2p}\log(n+1)\le3\) and \(L\ge3\).
The near bound is \(4C_{\rm u}q_0^p a^{-2p}L\). Thus
\[
 \sum_j|\mu_j|^p\le B_p L,\qquad
 B_p=14C_{\rm u}q_0^p/a^{2p}.
 \tag{1}
\]
The summable shell majorants give uniform absolute tails on the
whole tube at fixed \(T\). For fixed physical \(s>0\), write
\[
 \begin{split}
 G_{s,p}&=\sum_j e^{-sw_j^2}a_j^{-p},&
 A_{s,p}&=\sum_j e^{-s|w_j|^2}a_j^{-p},\\
 F&=\ell^4(12S_2+16DS_3)
    =12\sum_j\mu_j^2+16\delta\sum_j\mu_j^3,&
 F_s&=\ell^4(12G_{s,2}+16DG_{s,3}).
 \end{split}
\]
Let \(F_s^{\rm rad}\) use \(A\) in place of \(G\). Their weighted sums
are absolute with the same uniform tails times \(e^s\) or \(1\).
Conjugation makes all of them real. Every occurrence has
\[
 1-e^{-sw^2}=sw^2\int_0^1 e^{-usw^2}\,du,\qquad
 |1-e^{-sw^2}|\le s e^s |w|^2\le s e^s q_0|w^2-D|.
\]
The first inequality uses \(\Re w^2\ge-1\). In the radial case
\(0\le1-e^{-s|w|^2}\le s|w|^2\), giving the same estimate with \(e^s\)
replaced by \(1\). Subtract the weighted sum from each full moment
before taking the absolute bound:
\[
 \begin{split}
 |F-F_s|
 &\le s e^s q_0\ell^4
       \left(12\sum_j |a_j|^{-1}+16|D|\sum_j|a_j|^{-2}\right)\\
 &\le \boxed{\epsilon_s(L)=
     s e^s q_0(12B_1+16d B_2)/L}.
 \end{split} \tag{2}
\]
For \(F_s^{\rm rad}\) replace \(e^s\) by \(1\) throughout (2). The
constants are explicit in \(s,a,d,C_{\rm u}\). The \(O(L^{-1})\) rate
holds with these parameters fixed, or uniformly over their ranges
where the displayed coefficient is bounded. No time derivative of
the radial observation enters. The complements include every exterior
occurrence and the weights use the physical \(w_j\).

## 2. Conditional Riccati and gap transport

Suppose \(F_s\le Q\) throughout the paid tube, for a real scalar \(Q\)
which may depend on \(T\). Define \(K_{\rm eff}=Q+\epsilon_s(L)\).
The radial version uses its own \(Q\) and the radial error in (2).
With \(\sigma=(t-t_0)/\ell^2\), the accepted law gives
\[
 \dot m=2m^2-F\ge 2m^2-K_{\rm eff},\qquad m(0)\ge-A_0,\quad
 A_0=B_1L,\qquad \dot\delta=2-4m\delta.
 \tag{3}
\]
Here dots denote derivatives in \(\sigma\). Use
\(K_+=\max(K_{\rm eff},0)\) and \(h=\sqrt{K_+/2}\). For \(h>0\) set
\[
 f(\sigma)=\cosh(2h\sigma)+(A_0/h)\sinh(2h\sigma),
 \qquad g(\sigma)=\sinh(2h\sigma)/(2h).
\]
For \(h=0\) use \(f(\sigma)=1+2A_0\sigma,\ g(\sigma)=\sigma\).
The replacement is exact for \(K_{\rm eff}\ge0\). For \(K_{\rm eff}<0\)
it discards the favorable additive drift \(|K_{\rm eff}|\) in (3).

The finite lower barrier \(v=-f'/(2f)\le0\) has \(v(0)=-A_0\) and
\(\dot v=2v^2-K_+\). An integrating factor for
\((m-v)'-2(m+v)(m-v)\ge0\) gives \(m\ge v\). The bound retains the
initial layer at \(\sigma=0\). After positive elapsed \(\sigma\) it
implies \(m\ge-h\coth(2h\sigma)\) if \(h>0\), and
\(m\ge-1/(2\sigma)\) if \(h=0\). The first follows by bounding
\(f'/2f\) by \(h\coth(2h\sigma)\) using \(\cosh^2-\sinh^2=1\).
In particular \(h\coth(2h\sigma)\le h+1/(2\sigma)\).
For all paid scaled times \(0\le x\le y\),
\[
 \int_x^y(-m)_+\,du\le\tfrac12\log\frac{f(y)}{f(x)},\qquad
 W(x,y):=\exp\left(-4\int_x^y m(u)\,du\right)
     \le \left(\frac{f(y)}{f(x)}\right)^2.
 \tag{4}
\]
If \(K_+\asymp L\), \(f(y)^2\le(1+A_0/h)^2e^{4hy}\)
gives the inherited \(O(L)\exp(O(y\sqrt L))\) allowance, with constants
depending on \(B_1\) and the comparability constants. For \(K_+=0\)
the multiplier in (4) uses the exact linear \(f\).

The solutions \(f,g\) of \(u''=2K_+u\) have
\(f(u)g'(u-x)-f'(u)g(u-x)=f(x)\). Integrating the derivative of
\(g(u-x)/f(u)\) pays the inhomogeneous cost:
\[
 \int_x^y W(u,y)\,du\le \frac{f(y)}{f(x)}g(y-x),\qquad
 W(x,y)\delta(x)=\delta(y)-2\int_x^y W(u,y)\,du .
 \tag{5}
\]
The exact margin on the right has the sign of \(\delta(x)\), and
equality gives \(\delta(x)=0\), including the initial endpoint.
An independent lower anchor at \(y\) at least
\(2f(y)g(y-x)/f(x)\) suffices for \(\delta(x)\ge0\).
Strict separation gives strict positivity. Equality with the
conservative allowance guarantees nonnegativity. In the forward
direction the same identity uses independent \(\delta(x)\) as the
incoming value and gives
\[
 |\delta(y)|\le(f(y)/f(x))^2|\delta(x)|
                +2f(y)g(y-x)/f(x).
\]
In physical time \(W\) integrates \(M\) over the corresponding interval
and the inhomogeneous cost in \(D\) has the additional factor
\(\ell^2\). Neither the count bound on \(m(0)\) nor \(Q\) acquires
either \(D\) anchor or pays tube persistence. Equations (3)–(5) follow
from the signed forcing input. An equally informed direct evaluator
gets exactly the same \(F_s\) or \(F_s^{\rm rad}\), \(Q\), source, tube
and anchor, and can apply the same transfer and comparison. This
calculation establishes no separate acquisition or evaluation gain.
[Note41 §§3–4][n41] · [Note44 §1][n44] · [E05][e05]

## 3. Band surgery and uniform static premises

Use [Note34 §§1–2][n34] with \(c=T=e^L\), \(L\ge16\),
\(a=4,d=1,D=0,b=8\). Erase all occurrences of \(H_0\) in the closed
bands \(|\Re\rho\mp c|\le3\) by dividing by their monic polynomial
\(P_c\). Its full multiplicities make \(B_c=H_0/P_c\) entire with the
complete remaining divisor. Multiply \(B_c\) by the monic polynomials
for the insertions below at \(+c\) and their negations at \(-c\).
These divisors are closed under conjugation and negation so the
resulting fields are real even. For each fixed \(c\), outside a
sufficiently large disk \(|P_c|\ge1\), and the insertion polynomial
has finite degree. The resulting order is at most one and equals
one by the growing count below and Jensen's formula. The width-one
strip survives. The target at \(c\) is a double and the nearest
other positive-band insertion has distance \(b/L\) in (i), \(1/2\)
in (ii). Both distances are at least \(4/L\). The background has
\(|\Re w|>3\) and the opposite insertions have \(|\Re w|\ge c\).
Thus the slice has the specified counted disk and collar. Along
arbitrarily large \(c\) with \(H_0(c)\ne0\), the fields differ from
the canonical time-zero field even up to nonzero normalization.
The construction supplies snapshots, with no common-time heat
family or paid tube for these fields.

The following constants suffice uniformly in \(c\):

- **Counts.** There are at most \(12C_{\rm u}L\) removed occurrences
  per band by six closed unit intervals. Each band receives at most
  \(4\lfloor L\rfloor+4\le5L\) occurrences, all within horizontal
  distance \(1/2\) of its center. Each closed unit interval containing
  an insertion meets just one set of insertions, with start \(v\)
  satisfying \(|v|\ge c-2\). Thus the complete unit count has
  constant \(C_{\rm u}+5\). In the cumulative count
  \(0<\Re\rho\le X\), the change is zero for \(X<c-3\) and
  is at most \((12C_{\rm u}+5)L\le(24C_{\rm u}+10)\log(2+X)\)
  otherwise. Note34's \(X\log X\) main term and \(O(\log(2+X))\)
  discrepancy persist with enlarged constant, including edge cuts.
  The exact projected counting measures may change.
- **Static safe line.** The change in the logarithmic derivative at
  \(v+4i\) is a signed finite sum of at most \((24C_{\rm u}+10)L\)
  reciprocal distances. For \(|v|\ge c/2\), distances are at least
  \(3\), and \(\log(2+|v|)\ge L/2\). For \(|v|<c/2\), the horizontal
  distances are at least \(c/3\). Since \(L/c\le1\) and
  \(3/\log 2<5\), the inherited safe-line constant can be enlarged
  by \(5(24C_{\rm u}+10)\).
- **Broad transverse bounds.** For \(U\ge8,\ 0<v<1\), let the
  inherited time-zero bound in \([U,2U]\) be
  \(B_\beta U\log U\,e^{-\beta v\log U}\) for each fixed
  \(0<\beta<1/2\). Deleting occurrences can only lower this count.
  When (i) adds nonreal occurrences in the band, there are at most
  \(2(\lfloor L\rfloor+1)\le3L\), and \(v<b/L\) is needed for them
  to count. Here \(L/2\le\log U\le2L\), giving
  \(U\log U\,e^{-\beta v\log U}\ge4L\,e^{-16\beta}\).
  When (ii) adds nonreal occurrences, there are two and \(v<1/2\).
  Then \(U^{1-\beta v}\log U\ge8^{1-\beta/2}\log8>2\).
  A common bound therefore uses \(B_\beta+e^{16\beta}\).
  Reflection gives the corresponding negative-band bound. The
  dyadic second moment follows with coefficient
  \(2(B_\beta+e^{16\beta})/\beta^2\) by layer cake. The broader
  local averaged moments of [TND-O Note21 §6][density] follow by its
  static count, cover, weighted Hölder and layer-cake argument with
  \(J=4(C_{\rm u}+5)\) and
  \(\widetilde B_\beta=5(B_\beta+e^{16\beta})
  +6(C_{\rm u}+5)16^\beta\) in (29)–(30) there.

For complete tails, each reference shell \(n\le|\Re w|<n+1\),
\(n\ge3\), of the retained background has count at most
\(2C_{\rm u}(2L+\log(n+1))\). For every physical power \(k\ge2\) the
absolute sum of \(|w|^{-k}\) there and over all more distant shells
is at most \(10C_{\rm u}L\) by the sums in §1. All opposite-band
insertions together incur at most \(5L c^{-k}\). Thus the full
noncore absolute sum is at most \((10C_{\rm u}+5)L\) for each
\(k\ge2\), including the reflected target. These estimates use the
original whole background after removal and all reflections.
The exterior sums are real by conjugation.

## 4. Two fixed-slice comparisons

**(i) Linear forcing at a negative interaction.** Write \(N=\lfloor
L\rfloor\). At \(+c\) insert the target double and \(N\) occurrences at
each displacement \(\pm b\ell\), \(N+1\) at each \(\pm ib\ell\).
Reflect them at \(-c\). For \(D=0\) the core values of \(\mu\) are
\(1/b^2,-1/b^2\), respectively. With the complete tails from §3,
\[
 \boxed{m=-2/b^2+O(L^{-1}),\qquad
 F=12(4N+2)/b^4+O(L^{-3}).}
 \tag{6}
\]
The error constants can be taken as \(10C_{\rm u}+5\) and
\(12(10C_{\rm u}+5)\), respectively. For the companion
\(T_2=\sum_j w_j a_j^{-2}\) and \(\tau_2=\ell^3T_2\), the local
core cancels exactly in \(\pm w\) pairs, and the full
\(\tau_2=O(L^{-2})\) by the \(k=3\) tail. In a paid canonical
evolution the law for \(s_p=\ell^{2p}S_p\) is
\[
 \dot s_2=8ms_2-32s_3+4\delta s_2^2-40\delta s_4+4\tau_2^2.
\]
The same identity holds in the established local polynomial heat
class. At this slice these quantities specify only the algebraic
right side. No evolution derivative or uniform heat interval has
been acquired here. [E02][e02]

The enlarged unit count and collar give the same order of transfer
in (2) for these static fields by the occurrence proof. Thus
\(F_s\) and \(F_s^{\rm rad}\) also grow linearly in \(L\) at any
fixed physical \(s>0\) although \(m<0\) for all sufficiently large
\(L\). The fixed-slice strip, collar, count, broad transverse upper
bounds and even a fixed negative \(m\) margin allow forcing of
order \(L\). This obstruction concerns those static inputs.

**(ii) Microscopic Gaussian and its complement.** At \(+c\) insert
the target double and just the exterior pair at \(\pm i/2\).
Reflect all insertions at \(-c\). Fix \(\alpha>0\) and put
\(s=\alpha L^2\). Each core occurrence has \(a_j=-1/4\), so
the two squared terms contribute \(32\) to \(S_2\) and
\(32e^{s/4}\) to \(G_{s,2}\). In the full noncore tail
\(|\Re w|\ge3,\ |\Im w|\le1\) implies
\(\Re w^2\ge8\), and the \(k=4\) bound of §3 pays it:
\[
 \begin{split}
 S_2&=32+O(L),\\
 G_{s,2}&=32e^{s/4}+O(Le^{-8s}),\\
 S_2-G_{s,2}&=32(1-e^{s/4})+O(L(1+e^{-8s})).
 \end{split} \tag{7}
\]
The radial observation is \(A_{s,2}=32e^{-s/4}+O(Le^{-9s})\).
All errors are uniform in \(c\) and bounded by the displayed scale
times \(10C_{\rm u}+5\). The actual holomorphic Gaussian term
\(F_s=12L^{-4}G_{s,2}\) is asymptotic to
\(384L^{-4}e^{\alpha L^2/4}\), and its retained complement has the
opposite leading term. Their sum \(F=12L^{-4}S_2=O(L^{-3})\)
is small. Equivalently the full radial-to-holomorphic conversion
\(A_{s,2}-G_{s,2}\) pays the same leading exponential. This is an
actual cancellation on the changed slice, and demonstrates the cost
of bounding the two parts separately in this class. Any direct
comparator receives the same divisor and signed values, including
the complete background. Equation (7) makes no canonical
microscopic lower-bound claim.

## 5. Control replay and scope

The documentary replay uses the actual premises in [E01][e01],
[Note44 §7][n44] and [Controls12][controls]. Quadratic and quartic
heat controls retain local heat algebra and lack canonical growing
counts. Euler-factor controls change theta arithmetic and the
canonical endpoint discrepancy. Weighted-square, finite-source,
finite-score and finite-prime controls change full reflected
unit-weight theta equality. Their documented endpoint-defective
subclasses also fail the fixed strip. The reflected super-Gaussian
fails order at most one. Smooth and positive-primitive controls
change theta arithmetic, with canonical strip, count and density
transfer unpaid. Atomic and finite-type profile controls change
the source and lack canonical growing counts. RH-conditional
endpoint mergers keep the RH hypothesis and change ordinary
Dirichlet-series arithmetic. Changed observations lose the physical
cosine/Newman equation, and fractional profiles lack the integer
divisor. Note34 and the present surgery examples change the
canonical theta field and lack a paid common-time heat tube.
The strip and a coarse count can hold even in modified classes.
[Premises02][premises] · [Scope07][scope]

The acquired canonical estimate is the fixed-physical-scale
complement (2), with a conditional consumer in (3)–(5). A signed
bound \(Q\) over a paid tube remains to be supplied. The slice
comparisons leave canonical source-sensitive or integrated forcing
estimates open.

[request]: ../research-progress/handoffs/VCD-GT-GR-E06-r1.md
[b02]: ../brainstorm/notes/03_VCD_GT_GR_B02_FORCING_CONTRACT_20261117.md
[e01]: ../reviews/02_VCD_GT_GR_E01_INPUT_AUDIT_20261117.md
[e02]: 02_VCD_GT_GR_E02_CANONICAL_MOMENTS_20261117.md
[e03]: 03_VCD_GT_GR_E03_GAUSSIAN_EVOLUTION_20261117.md
[e05]: ../reviews/03_VCD_GT_GR_E05_INITIAL_PROOFS_ASSESSMENT_20261117.md
[n34]: ../../notes/34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[n44]: ../../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md
[density]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
