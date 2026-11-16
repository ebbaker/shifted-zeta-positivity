# ITP-E01 r1 — Uniform strip transfer from exact cell phases

13 November 2026, America/New_York. Intended author **Edward Baker**;
substantial OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol /
ultra**; independent backend metadata unavailable. **Proved in-note** for
the exact complete-source construction. All error bounds are analytical
allowances. The [frozen request](../research-progress/handoffs/ITP-E01-r1.md)
and [input manifest](../numerics/01_ITP_E01_R1_INPUT_MANIFEST_20261113.json)
were verified before execution. All 22 input identities matched.

## 1. Statement and normalization

The [fixed specification](01_ITP_B01_FIXED_TRANSFER_TARGET_20261113.md)
uses the [GNP source chapter](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex).
Keep the positive, smooth, even complete source
\(W_\lambda=e^{\lambda u^2}\Phi\), the readout
\(H_\lambda(z)=\tfrac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du\), and
\(\tau=\tfrac12-\lambda\). Thus \(H_0(z)=\xi(\tfrac12-iz/2)/8\).
Throughout, \(0\le\lambda\le\tfrac12\) and \(z=x+iy\). Write
\(\|g\|_{1,b}=\int_{\mathbb R}e^{b|u|}|g(u)|\,du\) for \(b\ge0\).

For integral \(L\ge0\), put \(h=2^{-L}\),
\(I_j=[jh,(j+1)h)\), \(c_j=(j+\tfrac12)h\), and set
\(m_j(\lambda)=\int_{I_j}W_\lambda\). Define \(P_h f\) to be the cell
average and \(A_L(\lambda,z)=\tfrac12\int_{\mathbb R}P_hW_\lambda(u)e^{izu}\,du\).
For an integer \(U\ge1\), write \(A_{L,U}\) for the same readout with
only cells inside \([-U,U]\). Here \(U/h\) is an integer and the
retained index range is \(-U/h\le j<U/h\).

**Theorem.** With \(V_8=\sup_{0\le\lambda\le1/2}\|W'_\lambda\|_{1,8}\)
and \(T_8(U)=\tfrac12\int_{|u|>U}e^{8|u|}W_{1/2}(u)\,du\), one has
\[
 V_8<868,\qquad
 \sup_\lambda\|W_\lambda-P_hW_\lambda\|_{1,8}
 \le \frac{he^{8h}}2 V_8.
\]
Both field estimates are uniform on \(0\le\lambda\le1/2\),
\(x\in\mathbb R\), \(|y|\le8\):
\[
 |H_\lambda(z)-A_L(\lambda,z)|\le\frac{he^{8h}}4V_8,\qquad
 |H_\lambda(z)-A_{L,U}(\lambda,z)|
 \le \frac{he^{8h}}4V_8+T_8(U).
\]
At \(U=2,L=30\) the latter allowance is less than \(5\cdot10^{-7}\),
so the requested \(10^{-6}\) test passes at the original tuple. Exact
integration of the selected piecewise-constant density gives the same
field as the dyadic ratio construction. For the matching point-phase
lattice with full-line masses, the uniform error on the real axis is
at least \(Z_\lambda/2\) for each fixed \(L,\lambda\), where
\(Z_\lambda=\int_{\mathbb R}W_\lambda>0\).

## 2. Cell averages, weighted convergence and exact phase

For an absolutely continuous \(f\) on \(I=[a,a+h]\), write
\(\bar f=h^{-1}\int_I f\). The triangle inequality and Tonelli give
\[
 \int_I|f-\bar f|
 \le\frac1h\int_I\int_I|f(v)-f(w)|\,dv\,dw
 \le\frac2h\int_a^{a+h}(t-a)(a+h-t)|f'(t)|\,dt.
\]
The last kernel counts the ordered pairs with derivative point \(t\)
between their endpoints. Its maximum is \(h/2\). On a length-\(h\)
cell the ratio of the maximum to the minimum of \(e^{b|u|}\) is at most
\(e^{bh}\), since \(|\,|u|-|v|\,|\le|u-v|\). Cellwise application and
summation yield
\[
 \|f-P_h f\|_{1,b}\le\frac{he^{bh}}2\|f'\|_{1,b},\qquad
 \|P_h f\|_{1,b}\le e^{bh}\|f\|_{1,b}.
\]
The second inequality follows by bounding the cell mean of \(|f|\) and
comparing the same weight extrema. These inequalities need only local
absolute continuity and the indicated integrability. The GNP envelope
and §3 supply these hypotheses for \(W_\lambda\) uniformly in the specified
time interval. The first inequality is the prepared-amplitude convergence.

On each integer slab the inherited ratios run in coarse-to-fine order.
Writing \(f_k=P_{2^{-k}}W_\lambda\) on that slab and \(R_k=f_k/f_{k-1}\),
\(f_0\prod_{k=1}^L R_k=f_L\) exactly. Positivity makes all denominators
positive. On a fixed slab, \(W_\lambda\) and its first derivative have
uniform lower-positive and upper-absolute bounds, respectively, by
continuity on the slab closure times the compact time interval. The
parent-cell oscillation bounds \(|R_k-1|\) by the derivative bound times
\(2^{1-k}\) divided by that local minimum. This recovers the inherited
local uniform product and the gates at level \(k\) act on the first \(k\)
bits. The topology across slabs is convergence of the prepared amplitudes
in weighted \(L^1\). No global source floor or global operator-norm product
is used.

On \(I_j\), write \(u=jh+s\) with \(s\in[0,h)\). Under normalized
Lebesgue measure on that cell, \(s=\sum_{k>L}2^{-k}b_k\) almost everywhere,
so the unresolved exponential factors multiply to \(e^{izs}\). The
conditional mean of their product is
\(h^{-1}\int_0^h e^{izs}\,ds=e^{izh/2}\operatorname{sinc}(zh/2)\).
This holds for complex \(z\), with \(\operatorname{sinc}(0)=1\). The
product of the unresolved factors converges uniformly on bounded \(z\)
sets since the sum of their binary offsets past scale \(k\) is at most
\(2^{-k}\). The mean is an exact integral at each \(z\). Combining it
with the phase at \(jh\), the prepared amplitude \(m_j/h\) and the cell
length gives
\[
 A_L(\lambda,z)=\frac12\operatorname{sinc}(zh/2)
       \sum_{j\in\mathbb Z}m_j(\lambda)e^{izc_j}.
\]
The same identity for the retained cells gives \(A_{L,U}\). This is
exactly the scalar integration baseline for \(P_hW_\lambda\) on the same
domain, including the phase within each cell. For each fixed \(h\) the
series converges absolutely and locally uniformly in \(z\): on
\(|\Im z|\le b\) its absolute sum is bounded by
\(e^{bh/2}\|W_{1/2}\|_{1,b}\), finite by the GNP envelope. Consequently both
fields are entire in \(z\). The phase product's local uniformity in \(z\)
and the all-real-height estimate for its integrated readout have different
quantifiers.

The Fourier factor \(1/2\) and \(|e^{izu}|\le e^{8|u|}\) give the full-line
field estimate. For the cutoff, split the true integral into \([-U,U]\)
and its complement. Pay the same local cell difference bound on the
inside. On the outside, \(0<W_\lambda\le W_{1/2}\) gives \(T_8(U)\).
This pays the true tail once. The bound never uses \(|x|h\).

## 3. Complete-source constants and exact allowance

On \(u\ge0\), set \(\rho=\pi e^{4u}\). The GNP recurrence
\(P_{j+1}(r)=(1-4r)P_j(r)+4rP_j'(r)\) gives
\(P_0=2r^2-3r\) and \(P_1=-8r^3+30r^2-15r\), with absolute coefficient
sums 5 and 53. These polynomials in the source envelope are separate from
the cell-average operator \(P_h\). Put
\[
 C_d(0)=\sum_{n\ge1}n^{2d}e^{-\pi(n^2-1)},\qquad
 B_0=5C_2(0),\qquad B_1=53C_3(0).
\]
The inherited envelope is \(|\Phi^{(j)}(u)|\le B_je^{u}\rho^{j+2}e^{-\rho}\)
for \(j=0,1\) on \(u\ge0\), from applying the polynomial bound to each
node \(n^2\rho\) and comparing \(e^{-n^2\rho}\) to
\(e^{-\rho-\pi(n^2-1)}\). Differentiating the heat multiplier and using
\(2\lambda\le1\) gives
\[
 |W'_\lambda(u)|\le e^{u^2/2+u}(B_1\rho^3+uB_0\rho^2)e^{-\rho}.
\]
For \(a_n=n^6e^{-\pi(n^2-1)}\), \(n\ge2\), the ratio
\(a_{n+1}/a_n\le(3/2)^6e^{-15}<1/2\), using \(\pi\ge3\), \(e>2\)
and \((3/2)^6<12\). Also \(a_2=64e^{-3\pi}<1/8\). Hence
\(C_2(0)\le C_3(0)\le 1+2a_2<2\), with \(B_0<10\), \(B_1<106\).
Using \(\pi\ge3\), \(e^{4u}\ge1+4u+8u^2\) gives
\[
 \rho/2-(u^2/2+9u)\ge \tfrac32-3u+\tfrac{23}2u^2
 =\tfrac{23}2(u-3/23)^2+30/23>0.
\]
The inequality \(\rho/4\ge3(1+4u)/4\ge u\) follows from the linear
exponential bound. Therefore
\(e^{8u}|W'_\lambda(u)|\le (B_1+B_0/4)\rho^3 e^{-\rho/2}\).
By evenness of \(|W'_\lambda|\), \(du=d\rho/(4\rho)\) on the positive
half-line, and \(\int_0^\infty\rho^2e^{-\rho/2}\,d\rho=16\),
\[
 V_8\le 8B_1+2B_0<868.
\]
The same inequality \(u^2/2+9u\le\rho/2\), now with the \(j=0\)
envelope and source evenness, gives
\[
 T_8(U)\le\frac{B_0}{4}\int_{\rho_U}^\infty\rho e^{-\rho/2}\,d\rho
         =\frac{B_0}2(\rho_U+2)e^{-\rho_U/2},\qquad \rho_U=\pi e^{4U}.
\]

For \(U=2\), \(\rho_2\ge3(1+8+8^2/2)>64\) and
\((r+2)e^{-r/2}\) is decreasing for \(r>0\). Thus
\(T_8(2)<5(64+2)e^{-32}<330/2^{32}\). For \(h=2^{-30}\),
\(8h<1/2\) and the exponential series is bounded by the geometric
series \(e^{8h}\le(1-8h)^{-1}<2\). The cell term is less than
\(1736/2^{32}\), so the complete allowance is
\[
 \frac{he^{8h}}4V_8+T_8(2)<\frac{2066}{2^{32}}<\frac{1}{2\cdot10^6}.
\]
The final rational inequality is \(4{,}132{,}000{,}000<4{,}294{,}967{,}296\).
There was no correction pass, diagnostic, source-mass evaluation or
floating-point claim.

## 4. Point-phase lattice comparison

For the specified full-line baseline
\(B_L(\lambda,x)=\tfrac12\sum_{j\in\mathbb Z}m_j(\lambda)e^{ixc_j}\),
set \(x_k=2\pi k/h\) for positive integers \(k\). All the phases
\(e^{ix_k(j+1/2)h}\) are \((-1)^k\), hence
\(B_L(\lambda,x_k)=(-1)^k Z_\lambda/2\). The exact source tends to zero
at both infinities and has \(W'\in L^1\), so integration by parts gives
\(|H_\lambda(x)|\le\|W'_\lambda\|_1/(2|x|)\) for \(x\ne0\). It follows
that \(|H_\lambda(x_k)-B_L(\lambda,x_k)|\to Z_\lambda/2\) and
\[
 \sup_{x\in\mathbb R}|H_\lambda(x)-B_L(\lambda,x)|\ge Z_\lambda/2.
\]
This lower bound concerns the actual error of that fixed-cell
center-phase class in the supremum over all real heights. It does not rule
out quadrature on bounded height windows or other phase architectures.
Direct integration of the same step density has exactly \(A_L\) (or
\(A_{L,U}\) at the cutoff), so the comparison establishes no speed gain
relative to that integration baseline.

## 5. Time, arithmetic and cost

The exact orbit is \(\partial_\tau W=-u^2W\), with
\(\tau=\tfrac12-\lambda\). Each exact \(m_j\) projects the complete orbit
at that time. Differentiating a cell mean in \(\tau\) gives
\(-P_h(u^2W)\) by the source domination. In general this differs from
\(-u^2P_hW\); on any positive-mass cell the former is constant while the
latter varies within it. Thus \(P_h\) and multiplication by \(u^2\) do
not commute. The finite level has no exact closed time evolution supplied
by this construction. The exact source masses, the exact sinc and exact
contraction have zero source truncation and zero arithmetic error in the
ideal theorem. The separate spatial cutoff and cell projection costs are
paid explicitly in §3.

For future computed masses, let \(\delta m_j\) include all passed-through
source, integration, core and compression errors and let \(e_{\rm readout}\)
be a separately established absolute readout arithmetic error. The centered
integral representation \(\operatorname{sinc}(zh/2)=h^{-1}
\int_{-h/2}^{h/2}e^{izv}\,dv\) yields \(|\operatorname{sinc}(zh/2)|\le e^{4h}\)
on the specified strip. Consequently the computed-minus-ideal field
satisfies
\[
 |\delta A_{L,U}|\le\tfrac12 e^{4h}
   \sum_{-U/h\le j<U/h} e^{8|c_j|}|\delta m_j|+e_{\rm readout}
\]
at all real heights if the stated arithmetic error is established with
that uniformity. For example, at the tested tuple it suffices to establish
\(\sum_j e^{8|c_j|}|\delta m_j|\le10^{-6}/(2e^{4h})\) uniformly in time
and \(e_{\rm readout}\le \tfrac14\cdot10^{-6}\) uniformly on the stated
field domain. Each term then spends at most \(\tfrac14\cdot10^{-6}\).
No computed bound is asserted. There are \(2U/h=2^{32}\) formal masses
at the tested tuple. Their acquisition is unresolved, the ratio gates
act on growing prefixes, and no bound on rank, cost, gamma-normalized
error, relative error near zeros or Green-log error follows.

## 6. Control screen and status

This is a quantitative approximation milestone in the sense of
[avoid 01](../../../../avoid/01_restating_the_target.md). Its achieved
number is an absolute transfer bound. Apply the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md), [controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[control premises 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scoped exclusions 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
as in the [B01 screen](../brainstorm/notes/01_ITP_B01_EXACT_CELL_PHASE_DECISION_20261113.md).
The catalog's existing witnesses are checked against the actual hypotheses
analytically. The transfer theorem for regular densities makes no zero
claim, so a smooth control can satisfy it at a collision.

| Catalog witness | Applicability and distinguishing premise |
| --- | --- |
| Euler-factor translated sources | For every fixed translation, multiplying the shifted double-exponential tail by the allowed heat/exponential weights still gives the required integrability, including for the first derivative. These sources change the complete normalized theta source. The acquisition of the numerical constant 868 uses the unchanged theta expansion and applies to it only. |
| Three- and four-weight square sources and finite source changes | Their one-sided finite perturbations retain integrable piecewise derivatives for the continuous even reflection, so the projection estimate can apply despite endpoint derivative mismatches. Complete coefficients and full smooth reflection are absent as a conjunction. Their positive event times do not give finite all-real thresholds in the source classes covered by the finite-source audit. |
| Finite-prime orbit controls | Selected-prime identities, a finite coefficient prefix and finite measurements can survive a bounded square-source change. Full reflection and unchanged infinite coefficients fail. Weighted one-sided derivative bounds and continuous even reflection can still suffice for the estimate. |
| Reflected super-Gaussian and smooth shape/positive-primitive controls | Derivatives of the quartic translated profiles or the damped Gaussian polynomials with fixed positive damping retain sufficient decay on the stated time band. Local ratios and projection estimates are compatible with their actual events. The normalized arithmetic square expansion is absent even when reflection and primitive data agree. |
| Three-atom chain, BW-01 and atomic finite-profile thresholds | The absolutely continuous density and weighted \(W^{1,1}\) hypotheses fail. Exact atomic networks can nonetheless exhibit the stated collisions. These sources also fail the unchanged full theta profile and eventual threshold simplicity. |
| Continuous finite-profile extensions | Finite sums of triangular densities, multiplied by the bounded heat factor on compact support, have the needed integrable weak derivative. Zero-mass cells do not admit the strictly positive ratio construction, while the cell-average estimate still applies. Complete coefficients, full profile and eventual threshold simplicity fail. |
| RH-conditional normalized endpoint controls | Their construction remains conditional. It changes the complete source and fails ordinary Dirichlet-series arithmetic. The stated smooth, super-Gaussian derivative decay permits the weighted estimate, which does not rule out their doubles. |
| Fixed amplitude with variable observation kernel | Retaining the unchanged source and finitely many observation terms does not give the literal Fourier/Newman readout. The sinc evaluation only consumes the exponential kernel in this request. |
| Actual-profile relaxed positive measure | The relaxed measure in the zero-profile problem is neither an integer zero configuration nor a specified source density on the Fourier variable. Its fitted profile does not satisfy the prescribed complete-source readout premises. |
| Earlier Gaussian counter-kernels ([summary 11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)) | Smooth noncanonical source kernels can have enough weighted regularity. The canonical complete theta expansion and its specific domination constants are not supplied by these controls. |

The analytic bound and the scoped lattice lower bound meet the frozen
E01 test. The inherited local products have their original provenance and
scope. No numerical control replay, new arithmetic theorem or new
literature import was used.
