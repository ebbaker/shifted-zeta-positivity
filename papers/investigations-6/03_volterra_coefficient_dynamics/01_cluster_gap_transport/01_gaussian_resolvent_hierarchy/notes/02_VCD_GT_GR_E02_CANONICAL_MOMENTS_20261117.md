# VCD-GT-GR-E02 r1 — Canonical integer moments and resolvent

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Requested helper dispatch **gpt-6.1-sol /
ultra**. Independent serving-model and actual effort metadata unavailable.

**Proved in-note on the independently paid count-two tube, pending separate
internal assessment.** This is an exact moment evolution and generating
series. The signed forcing and transport allowances still require estimates.
The four frozen input hashes matched. See [request][request], [return][return],
[B01][b01], [E01 audit][audit], [result index][results], [Controls12][controls],
[avoid index][avoid], [Classification01][a01], [Premises02][a02],
[Scope07][a07] and [Joint estimates12][a12].

## 1. Counted moments and their derivatives

Use the unchanged complete even canonical theta field \(H(t,z)\), with
\(\partial_tH=-H_{zz}\) in physical time \(0\le t\le 1/2\). Use
the source envelope, order-at-most-one product, width-one strip
\(|\Im\rho|\le1\) and uniform complete unit count
\(\#\{\rho:v\le\Re\rho\le v+1\}\le C_{\rm u}\log(2+|v|)\) of
[Note41 §1][n41] and the [E01 audit][audit], including time zero.
On a separately paid compact tube \(I\) take \(T\ge64\),
\(L=\log T\), \(\ell=L^{-1}\) fixed, \(d\ge0\),
\(\max(2,4\sqrt d)\le a\le L\) and \(r_0=a\ell\).
The two target occurrences are conjugation-invariant, with midpoint
\(c\in[T,2T]\), \(D\in\mathbb R\), \(|D|\le d\ell^2\le r_0^2/16\),
and distance at most \(r_0/4\) from \(c\). Put \(u=z-c(t)\),
\(Q=u^2-D(t)\) and, for each exterior occurrence \(\rho_j\),
\[
 w_j=\rho_j-c,\qquad a_j=w_j^2-D,\qquad m_j=a_j^{-1},
 \qquad S_p=\sum_j m_j^p,\quad M=S_1,\quad T_2=\sum_j w_jm_j^2.
\]
All occurrences are counted with multiplicity. The collar
\(|w_j|\ge r_0\) gives \(|a_j|\ge(15/16)|w_j|^2\).
The unit count gives absolute sums for \(S_p\), integer \(p\ge1\),
and \(T_2\), whose far summands are \(O(|\rho|^{-2p})\) and
\(O(|\rho|^{-3})\), respectively. These bounds are uniform on \(I\)
for fixed \(T\). All these moments are real by conjugation.

At each \(\tau\in I\) use the positive fixed circle
\(\Gamma=\{|z-c(\tau)|=r_0/2\}\) and denote its normalized integral
by \(\langle\,\cdot\,\rangle_\Gamma=(2\pi i)^{-1}\oint_\Gamma(\,\cdot\,)\,dz\).
The canonical source envelope gives joint holomorphy in time and space.
The contour is zero-free on a small complex-time neighborhood of
\(\tau\) and counts two zeros there by Rouché. For \(F=H\), or a finite
polynomial heat field with the same local separation, set \(B=F_z/F\).
The target coordinates and their derivatives come from
\[
 J_k=\langle z^kB\rangle_\Gamma\quad(k=1,2),\qquad
 c=J_1/2,\qquad D=J_2/2-c^2,\qquad
 \dot J_k=\langle z^k\dot B\rangle_\Gamma.                         \tag{1}
\]
They are analytic through a double. On \(\Gamma\), at fixed \(z\),
\[
 \dot B=-F_{zzz}/F+F_zF_{zz}/F^2,\qquad
 \dot Q=-2u\dot c-\dot D.                                       \tag{2}
\]
For \(f=Q^{-p}\) or \(uQ^{-2}\), the only poles of \(f\) are inside
\(\Gamma\) and \(\langle f\rangle_\Gamma=0\) by its decay at infinity.
An exterior log-derivative pole contributes
\(\langle f/(z-\rho_j)\rangle_\Gamma=-f(\rho_j)\), by the
residue theorem including infinity. The complete paired product
log derivative converges uniformly on \(\Gamma\) by the
inverse-square tail. Equivalently, the individual genus-one
regularizers \(1/\rho_j\) disappear under the integral of \(f\).
The same computation applies to finite products.

For \(h=Q_z/Q=2u/Q\), the target term \(Q^{-p}h=-(Q^{-p})_z/p\)
has zero residue at every pole. The term \(uQ^{-2}h=2u^2/Q^3\)
has zero **sum** of residues by \(O(z^{-4})\) decay. For \(D\ne0\)
its individual residues at \(u=\pm\zeta\), \(\zeta^2=D\), are
\(\mp1/(8\zeta^3)\), obtained from the second derivative of
\(2u^2/(u+\zeta)^3\) at \(+\zeta\) and reflection. At \(D=0\)
the term is \(2u^{-4}\), with zero residue at the double. In both
cases \(\partial_t(fh)\) also has zero integral, by differentiating
the zero contour identity. In particular at the double
\(\partial_t(2u^2/Q^3)=8\dot c\,u^{-5}+6\dot D\,u^{-6}\).
Thus the target contribution cancels in both differentiated
formulas as the combined derivative of \(fh\).

The exterior poles now give \(S_p=-\langle Q^{-p}B\rangle_\Gamma\)
and \(T_2=-\langle uQ^{-2}B\rangle_\Gamma\). These fixed-contour
expressions extend holomorphically in time locally, including
through exterior multiplicities. In particular,
\[
 \begin{aligned}
 \dot S_p&=-\left\langle
 Q^{-p}\dot B-pQ^{-p-1}\dot Q\,B\right\rangle_\Gamma,\\
 \dot T_2&=-\left\langle
 uQ^{-2}\dot B-\dot c\, Q^{-2}B-2uQ^{-3}\dot Q\,B
 \right\rangle_\Gamma .                                         \tag{3}
 \end{aligned}
\]
At the endpoints of \(I\) these yield the inward physical derivatives.
Equations (1)–(3) use the full \(B\) in (2).

## 2. Finite law and cancellation before taking the limit

Start with a polynomial heat field at a slice with simple roots.
The root velocity is \(F_{zz}(\rho)/F_z(\rho)=2\sum_{\xi\ne\rho}
(\rho-\xi)^{-1}\). Put \(P=\sum_j w_jm_j\) and \(T_3=\sum_j w_jm_j^3\)
in this finite calculation. At the target roots \(z_\pm=c\pm\zeta\),
the average velocity gives \(c'=-2P\), from the sum of
\((z_\pm-\rho_j)^{-1}\). The target-target terms give \(2\) in \(D'\).
For each exterior pole the difference of those reciprocals,
divided by \(2\zeta\), is \(-m_j\). Hence
\[
 D'=2-4DM,\qquad
 w_j'=4w_jm_j+2P+2\sum_{k\ne j}(w_j-w_k)^{-1}.
\]
Differentiating \(m_j^2\) and pairing the opposite velocities gives
\[
 S_2'=(-12-8DM)S_3-16DS_4-8P T_3-8\sum_{j<k}h_{3,jk},
 \qquad
 h_{3,jk}=\frac{w_jm_j^3-w_km_k^3}{w_j-w_k},                     \tag{4}
\]
using \(w_j^2m_j^4=m_j^3+Dm_j^4\).
For \(u=w_j,\ v=w_k,\ A=m_j,\ B_0=m_k\), one has
\((uA-vB_0)/(u-v)=-(D+uv)AB_0\). Since either \(x=A\) or
\(x=B_0\) satisfies \(x^3=(A^2+AB_0+B_0^2)x-AB_0(A+B_0)\),
\[
 h_{3,jk}=-AB_0(A+B_0)-(D+uv)AB_0(A^2+AB_0+B_0^2).
\]
Summing the three terms with positive signs first, removing the
diagonal of each product sum, gives
\[
 -\sum_{j<k}h_{3,jk}
 = (MS_2-S_3)
   +D(MS_3+S_2^2/2-3S_4/2)
   +P T_3+T_2^2/2-3(S_3+DS_4)/2 .
\]
The spatial diagonal is \(\sum_j w_j^2m_j^4=S_3+DS_4\).
Substitution in (4) cancels \(P T_3\) and \(DMS_3\), giving
\[
 \boxed{S_2'=8MS_2-32S_3+4DS_2^2-40DS_4+4T_2^2.}               \tag{5}
\]
This cancels the inverse-first-power \(P\) **before** taking a
complete-divisor limit.

At a multiple slice of a finite heat field, perturb the finitely
many factors to distinct roots and initialize their polynomial
heat evolutions at that same slice. Preserve the target count and
separation, which have a strict contour margin. The moment
coordinates and derivatives in (1)–(3) converge under the
perturbation by coefficient and contour convergence, since the
denominators on \(\Gamma\) stay bounded away from zero.
The finite rational sums on the right of (5) converge by the
exterior separation. This proves (5) for finite heat fields at
multiple target or exterior roots too.

## 3. Complete canonical passage

At every reference time \(\tau\), truncate the [Note41 §1][n41]
product \(H(\tau,0)\prod_{\{\rho,-\rho\}}(1-z^2/\rho^2)\) by
\(|\rho|\le N\), retaining all ties, opposite pairs, conjugates and
multiplicities. For \(N>2T+r_0\) the truncation contains the target
exactly. The strip and unit count give
\[
 \sup_{\tau\in I}\sum_{|\rho|>N}|\rho|^{-2}
   =O\!\left(\sum_{n\ge\lfloor N\rfloor-1}\frac{\log(2+n)}{n^2}\right)
   =O(\log N/N).
\]
Indeed \(|\Im\rho|\le1\) makes \(|\Re\rho|\ge\sqrt{N^2-1}\) in
the tail, and each real unit shell on either side has the displayed
count. The inverse-square estimate makes the omitted product
uniformly \(1+O_K(\log N/N)\) on any fixed compact \(K\) in \(z\).
Since \(H\) is bounded on \(I\times K\), the slices converge uniformly
there. Applying Cauchy's formula on a larger compact set gives the
same convergence for the spatial derivatives through degree three.

Initialize \(F_{\tau,N}(s,z)\) from the truncated slice at
\(s=\tau\) by \(e^{-(s-\tau)\partial_z^2}\), a terminating sum
on polynomials. At \(s=\tau\) its first time jet on \(\Gamma\)
is determined by the spatial derivatives in (2). A finite cover
of \(I\) by local closed time subintervals and their fixed circles
supplies positive minima for \(|H|\) and \(|Q|\) on the corresponding
boundaries. Equations (1)–(3) therefore give uniform convergence
of the first moment derivatives at their reference slices. The
retained exterior summands have the exact same \(c,D\) there.
For \(N>4T+4\), omitted roots satisfy \(|w_j|\ge|\rho_j|/2\).
Thus each \(S_1,\ldots,S_4,T_2\) tail tends to zero uniformly by
the same unit-shell estimates. Applying (5) to \(F_{\tau,N}\)
at \(s=\tau\) and taking the limit proves (5) for \(H\), uniformly
in the reference slice on the compact paid tube at fixed height.
The argument uses only the slice and its heat jet.

## 4. Resolvent domain

At each time let \(A_*(t)=\inf_j|a_j(t)|\). For \(|\eta|<A_*(t)\),
\[
 \mathcal R(\eta,t)
   =\sum_j\frac1{a_j(t)-\eta}
   =\sum_{n\ge0}\eta^nS_{n+1}(t),\qquad
 A_*(t)\ge r_0^2-|D(t)|\ge15r_0^2/16.                           \tag{6}
\]
The geometric double series is bounded in absolute value by
\(\sum_j|a_j|^{-1}/(1-|\eta|/A_*)\). It converges uniformly
on compact subdisks of the common tube disk
\(|\eta|<r_0^2-\sup_I|D|\). In particular \(M=\mathcal R(0,t)\)
and \(S_2=\mathcal R_\eta(0,t)\). At a slice with exterior
occurrences, local finiteness and \(|a_j|\to\infty\) in the
far tail give a nearest denominator value of modulus \(A_*\).
There the resolvent has a simple pole of residue minus the number
of occurrences with that denominator, since all remaining summands
converge locally normally. Thus \(A_*\) is the Taylor radius.
An empty exterior has zero resolvent and infinite radius.

The direct local formula is
\(\mathcal R=-\langle B/(Q-\eta)\rangle_\Gamma\) whenever the contour
encloses the targets and both shifted poles \(u^2=D+\eta\), and
excludes every exterior zero. The residue argument of §1 applies
with \(f=(Q-\eta)^{-1}\), including at coincident kernel poles.
At its reference slice the default \(r_0/2\) circle requires
\(|D+\eta|<r_0^2/4\). A centered disk sufficient for this is
\(|\eta|<r_0^2/4-|D|\), at least \(3r_0^2/16\) uniformly.
For a compact subdisk \(|\eta|\le b<r_0^2-\sup_I|D|\),
choose \(\sqrt{\sup_I|D|+b}<r<r_0\) and center the radius-\(r\)
circle at the reference midpoint. The strict margins persist
locally in time. More generally at a reference slice choose
\(\max(|D|,|\eta|)<\beta<A_*\) and take the boundary
\(|Q(\tau,z)|=\beta\). This is a smooth simple closed curve
since along a ray from \(c(\tau)\), \(|u^2-D|=\beta\) has a
unique positive radial solution with nonzero radial derivative.
It contains the targets and shifted poles with strict margins.
Using that curve fixed near \((\tau,\eta)\) gives a local joint
holomorphic resolvent representation on the slice domain.

## 5. Scope and premise screen

The denominator-only nonclosure example in [Note44 §6][n44] is
for generic polynomial heat fields. With fixed target roots
\(\pm1/2\), the exterior sets \(\{2,3\}\) and \(\{2,-3\}\)
have the same \(c,D\) and all \(S_p\). Their \(T_2\) values
are \(32/225\pm48/1225\), so (5) gives different \(S_2'\).
This excludes determination of \(S_2'\) from \(c,D\) and the
resolvent in that polynomial class. Canonical closure and
quantitative signs remain open.

The [Controls12][controls] screen here is documentary, using
[Note44 §7][n44] and [B01][b01]. The identity itself applies to
the quadratic and even quartic heat controls, whose finite
divisors fail canonical growing population, though they may
satisfy a coarse upper unit count. Euler-factor controls change
theta and its canonical endpoint count discrepancy. Weighted-square
and endpoint-defective finite-source controls fail full normalized
reflected theta equality and the uniform strip in the documented
classes. Finite-prime controls likewise fail full source reflection.
The reflected super-Gaussian fails the imported order premise.
Smooth-shape and positive-primitive controls change theta arithmetic.
Fixed-event atomic and finite-profile controls change the source and
fail theta's eventual simplicity and full profile growth at their
thresholds. RH-conditional endpoint controls retain their RH premise
and fail ordinary Dirichlet-series arithmetic. Changed observation
kernels fail the physical cosine/Newman law and fractional-profile
relaxations lack the full integer divisor. The exact-count
opposite-sign slice controls retain their tested projected data and
supply no canonical common-time tube. A local collar, heat law or
upper unit count can survive several of these changes.

[request]: ../research-progress/handoffs/VCD-GT-GR-E02-r1.md
[return]: ../research-progress/handoffs/VCD-GT-GR-E02-return-r1.md
[b01]: ../brainstorm/notes/01_VCD_GT_GR_B01_COUPLED_STATE_DECISION_20261117.md
[audit]: ../reviews/02_VCD_GT_GR_E01_INPUT_AUDIT_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[n44]: ../../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
