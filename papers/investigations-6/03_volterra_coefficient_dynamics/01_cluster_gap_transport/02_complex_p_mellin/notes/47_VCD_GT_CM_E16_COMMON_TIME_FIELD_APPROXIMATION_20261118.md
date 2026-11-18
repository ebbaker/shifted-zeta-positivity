# E16 r4 — One initialized divisor over the common time interval

18 November 2026, America/New_York. Prepared for **Edward Baker**, with
substantial OpenAI Codex LLM assistance. Requested helper configuration:
`gpt-6.1-sol`, effort `ultra`; independently recorded serving-model and
effort metadata are unavailable. The requested configuration is not a
serving attestation.

**Proved in-note, pending the separate E40 assessment:** the field and
spatial-jet part of [E16 r4][r4], with the unchanged [r1 contract][r1].
The contour/transport continuation is [Note48][n48]. This is a quantitative
approximation result, not a zero-exclusion criterion or a short-moment-head
closure. The [result index][results], [cluster18][cluster] and [avoid
index][avoid] were read; the classification and scope are those of
[pattern01][class] and [pattern07][scope]. The complete control screen is
in Section 7 below, following [controls12][controls] and [pattern02][premises].

| Task | Type / routing | Fixed scope and completion |
| --- | --- | --- |
| E16 r4, field component | E — execution; Sol, because the product/Gaussian/Cauchy route is frozen | One initial divisor, one fixed supplied tube, explicit uniform field errors and spatial jets through order 3, finite input and uncertainty accounting |
| E40 | E — execution; separate nonauthor internal assessment | Check the complete field/contour/transport proof on its recorded inputs before promotion |

The seven byte counts and SHA-256 identities in the [r4 manifest][pins]
were checked before proof execution and all match. The source version is
r4, not the historical r1/r2/r3 source binding. The proof uses the product
and source established in the pinned [framework][framework], the
[collision-regular hierarchy][hierarchy], and [B05 Note15][b05]. No external
theorem or reference is newly imported. This component writes only this
note; the sole progress register and guarded public-chat recorder remain
with the lead writer.

## 1. Fixed data and exact pair conventions

Keep the unchanged source

\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \qquad H_t=-H_{zz},
 \tag{1}
\]

and the independently supplied canonical tube
\(I=[t_0,t_1]\subset[0,1/2]\), with \(\Delta=t_1-t_0\).
The fixed height, \(\ell=1/\log T\), counted target pair, both signs of
\(D\), integer multiplicities, strong collar and independent anchors are
exactly those of the framework. This note neither constructs that tube
nor transfers the separate negative-time E38 numerical domain into it.

Write \(h_0=H(t_0,0)>0\). There is no zero at the origin. Use one
representative \(\rho_\nu\) per opposite pair of **occurrences** at
\(t_0\). Thus a zero of multiplicity \(m\) at each of \(\rho,-\rho\)
gives \(m\) factors. Changing a representative's sign changes no factor.
The representative multiset of squares is conjugation closed. The
canonical product from the framework is

\[
 H_0(z):=H(t_0,z)=h_0\prod_\nu(1-z^2/\rho_\nu^2).
 \tag{2}
\]

For \(N\ge1\), let \(m_N=\#\{\nu:|\rho_\nu|\le N\}\) and set

\[
 P_N(0,z)=h_0\prod_{|\rho_\nu|\le N}(1-z^2/\rho_\nu^2),\qquad
 P_N(\tau,z)=e^{-\tau\partial_z^2}P_N(0,z),\quad0\le\tau\le\Delta,
 \tag{3}
\]

where the exponential terminates. Here \(\tau=t-t_0\), and the same
polynomial is initialized only once. Retain every modulus tie, conjugate
and multiplicity. The omitted sum is, consistently,

\[
 E_N=\sum_{|\rho_\nu|>N}|\rho_\nu|^{-2}
     =\tfrac12\sum_{\substack{\rho\text{ an occurrence}\\|\rho|>N}}
                        |\rho|^{-2}.
 \tag{4}
\]

It is not the complete-occurrence sum itself. \(N\) is a divisor cutoff,
not the number of retained hierarchy rows.

At the initial time the supplied complete unit count is

\[
 \#\{\rho:v\le\Re\rho\le v+1\}
       \le C_u\log(2+|v|),\qquad C_u\ge1.
 \tag{5}
\]

The complete strip \(|\Im\rho|\le1\) is retained. Only the count, product,
normalization and finite near-origin data are needed for the following
field estimate; safe-line bounds and the collar enter the later contour
application. All constants are allowed to depend on these fixed inputs.

## 2. A common absolute-product envelope and the inverse-square tail

Let \(A_*(x)=\#\{\nu:|\rho_\nu|\le x\}\). For \(x\ge1\), covering
\([-x,x]\) by the integer unit intervals gives

\[
 A_*(x)\le\tfrac12(2x+3)C_u\log(3+x)
       \le Kx\log(2+x),\qquad K=5C_u.
 \tag{6}
\]

The factor \(1/2\) is exact because opposite occurrences have equal
modulus and none is zero. The deliberately loose last inequality uses
\((2x+3)/2\le5x/2\) and \(\log(3+x)\le2\log(2+x)\).

Supply the finite near-origin multiset \(\{|\rho_\nu|<1\}\), or upper
bounds for the following two quantities:

\[
 q=\#\{\nu:|\rho_\nu|<1\},\qquad
 C_0=\prod_{|\rho_\nu|<1}\max(1,|\rho_\nu|^{-2}).
 \tag{7}
\]

An empty product is one. Define

\[
 g_0=h_0C_0,\qquad A=2q+8K,\qquad
 G(r)=g_0\exp\{A(1+r)\log(2+r)\}\quad(r\ge0).
 \tag{8}
\]

Then every finite partial absolute product, and the full absolute
product, obey

\[
 h_0\prod_\nu(1+r^2/|\rho_\nu|^2)\le G(r).
 \tag{9}
\]

Here and below a finite partial product is bounded by the full one.
For the near factors,
\(\prod_{|\rho|<1}(1+r^2/|\rho|^2)\le C_0(1+r)^{2q}\).
For the remaining factors, the layer-cake identity and (6) give

\[
 \begin{split}
 \sum_{|\rho_\nu|\ge1}\log(1+r^2/|\rho_\nu|^2)
 &\le2Kr^2\int_1^\infty\frac{\log(2+u)}{u^2+r^2}\,du.
 \end{split}
 \tag{10}
\]

For \(r\ge1\), split the integral at \(r\). Its two contributions are
at most \(2Kr\log(2+r)\) and
\(2Kr[\log(2+r)+1]\), respectively. We used

\[
 \int_b^\infty\frac{\log(2+u)}{u^2}\,du
 =\frac{\log(2+b)}b+\tfrac12\log(1+2/b)
 \le\frac{\log(2+b)+1}b.                 \tag{11}
\]

Their sum is at most \(6Kr\log(2+r)\), since \(\log3>1\).
For \(0\le r\le1\), (10) is at most
\(2Kr^2(\log3+1)<5Kr^2\), hence at most
\(8K(1+r)\log(2+r)\). Together with the near factors these prove (9)
with the explicit, \(N\)-independent order-one envelope (8).

The same layer-cake calculation, with all ties retained, gives for
\(N\ge1\)

\[
 \begin{split}
 E_N
 &=\int_N^\infty 2u^{-3}
       \#\{\nu:N<|\rho_\nu|\le u\}\,du\\
 &\le2K\int_N^\infty\frac{\log(2+u)}{u^2}\,du
 \le\frac{2K[\log(2+N)+1]}N.
 \end{split}                                                   \tag{12}
\]

Thus \(E_N=O(\log N/N)\), with an explicit constant. No count asymptotic
or lower population bound was used.

## 3. Initial product error, including a bounded sharpening

The frozen contract's global initial estimate holds exactly as proposed:

\[
 |H_0(z)-P_N(0,z)|
 \le G(|z|)\{\exp(|z|^2E_N)-1\}.                 \tag{13}
\]

Indeed factor (2) into the retained and omitted products and use
\(|\prod(1+a_\nu)-1|\le\prod(1+|a_\nu|)-1
\le\exp(\sum|a_\nu|)-1\) on the latter.

A telescoping estimate sharpens (13) within the same frozen product
route:

\[
 \boxed{|H_0(z)-P_N(0,z)|\le |z|^2G(|z|)E_N.}       \tag{14}
\]

For a finite product ending at a larger complete cutoff, put
\(a_\nu=-z^2/\rho_\nu^2\) and add omitted factors one at a time.
Each difference is \(a_\nu\) times a product of a subset of the other
factors. Its modulus, including \(h_0\), is bounded by
\(|z|^2|\rho_\nu|^{-2}G(|z|)\), by (9). Sum these bounds and pass to
the convergent canonical product. This proves (14), without division
by a possibly vanishing factor. It therefore holds at every \(z\),
including zeros and multiple zeros. In particular no zero-free disk
was smuggled into this estimate.

This is an elementary estimate sharpening, not a new approximation or
changed premise. It removes the need for the sufficient
\(E_N\le1/[16(1+\Delta)]\) condition in the contract's exponential-error
route. Both (13) and its originally proposed route remain valid.

## 4. The imaginary Gaussian shift and an explicit field constant

Let \(X\) be a real standard normal random variable. For the polynomial,
the terminating Taylor expansion and
\(\mathbb E X^{2k}=(2k)!/(2^k k!)\) give

\[
 P_N(\tau,z)=\mathbb E P_N(0,z+i\sqrt{2\tau}X).
 \tag{15}
\]

The factor \(\sqrt{2\tau}\), the imaginary shift, and the negative
heat sign all agree: the term of index \(k\) is
\((-\tau)^k\partial_z^{2k}P_N(0,z)/k!\).

For the unchanged canonical source, Fubini is justified directly.
For \(\tau\in[0,\Delta]\),

\[
 \begin{split}
 \mathbb E|\cos((z+i\sqrt{2\tau}X)u)|
 &\le e^{|\Im z|u}\mathbb E e^{\sqrt{2\tau}|X|u}
 \le2e^{|\Im z|u+\tau u^2}.
 \end{split}
 \tag{16}
\]

Multiplication by \(e^{t_0u^2}\Phi(u)\) gives an integrable majorant
uniformly on compact \(z\)-sets, by the pinned double-exponential source
decay and \(t_0+\tau\le t_1\). The Gaussian exponential expectation
inside the cosine is \(e^{\tau u^2}\); thus

\[
 H(t_0+\tau,z)=\mathbb E H_0(z+i\sqrt{2\tau}X).
 \tag{17}
\]

This argument uses the literal unchanged source and does not infer a
general backward-heat existence theorem from a product alone.

Here is a completely explicit domination constant. Set

\[
 \begin{gathered}
 \lambda=\frac1{8(1+\Delta)},\qquad
 \epsilon=\frac{\lambda}{2A},\qquad
 b=2\epsilon-1-\log\epsilon,\\
 B_\lambda=A b+\frac{A^2(\epsilon+b)^2}{2\lambda},\qquad
 M_\lambda=g_0e^{B_\lambda}.
 \end{gathered}                                               \tag{18}
\]

Since \(A>0\), these are finite specified constants. The elementary
inequality \(\log y\le\epsilon y-1-\log\epsilon\) gives
\(\log(2+r)\le\epsilon r+b\). Therefore

\[
 A(1+r)\log(2+r)
 \le\tfrac\lambda2r^2+A(\epsilon+b)r+A b
 \le\lambda r^2+B_\lambda,
 \qquad G(r)\le M_\lambda e^{\lambda r^2}.
 \tag{19}
\]

The second inequality uses
\(Lr\le\lambda r^2/2+L^2/(2\lambda)\) with
\(L=A(\epsilon+b)\).

For \(|z|\le R\), put \(r=R+\sqrt{2\Delta}|X|\). Then
\(r^2\le2R^2+4\Delta X^2\) and
\(1-8\lambda\Delta=(1+\Delta)^{-1}>0\). Direct Gaussian integration
gives

\[
 \mathbb E e^{4\lambda\Delta X^2}=\sqrt{1+\Delta},\qquad
 \mathbb E X^2e^{4\lambda\Delta X^2}=(1+\Delta)^{3/2}.
 \tag{20}
\]

In particular define

\[
 \boxed{\mathcal C(R,\Delta)=
 M_\lambda e^{2\lambda R^2}
 \left[2R^2\sqrt{1+\Delta}+4\Delta(1+\Delta)^{3/2}\right].}
 \tag{21}
\]

Equations (19)–(20) prove the finite bound
\(\mathbb E[r^2G(r)]\le\mathcal C(R,\Delta)\). They also prove
integrable, \(N\)-independent domination of both initial fields in
(15)–(17), since their moduli are at most \(G(r)\).
Applying (14) inside the two exact Gaussian formulas now yields

\[
 \boxed{\sup_{\substack{t\in I\\|z|\le R}}
 |H(t,z)-P_N(t-t_0,z)|\le\mathcal C(R,\Delta)E_N,\quad N\ge1.}
 \tag{22}
\]

This proves the rate by an evaluated majorant; qualitative dominated
convergence is not being used to assert a quantitative rate. The constants
are very conservative. Their finiteness is an analytical result, not a
claim of practical numerical affordability.

For completeness, the unsharpened frozen route is paid by the same
calculation: if \(E_N\le\eta=1/[16(1+\Delta)]\), then (13) is at most
\(E_Nr^2G(r)e^{\eta r^2}\). Use (18)–(19) with \(\lambda=\eta\)
to bound \(G(r)\), and then integrate \(r^2e^{2\eta r^2}\).
The resulting constant is the right side of (21) with
\(M_\eta e^{4\eta R^2}\) in place of
\(M_\lambda e^{2\lambda R^2}\); (20) still holds because
\(1-16\eta\Delta=(1+\Delta)^{-1}\).

## 5. Spatial jets through order three

Fix any physical enlargement \(h>0\). At each \(t\in I\), apply Cauchy's
formula on the circle of radius \(h\) about each \(|z|\le R\) to the
entire field difference. From (22), for \(j=0,1,2,3\),

\[
 \boxed{\sup_{\substack{t\in I\\|z|\le R}}
 |\partial_z^jH(t,z)-\partial_z^jP_N(t-t_0,z)|
 \le C_j(R,h,\Delta)E_N,\qquad
 C_j=\frac{j!}{h^j}\mathcal C(R+h,\Delta).}
 \tag{23}
\]

For \(j=0\), (22) itself is the slightly sharper choice. Thus the same
initialization has a compact-space, common-time
\(O(\log N/N)\) bound for all required jets. The enlarged radius and
the factor \(j!h^{-j}\) must be retained in each contour chart's budget.
No global strip statement about the evolved \(P_N\) was used.

These errors also pay first physical-time field jets through
\(\partial_t(H-P_N)=-\partial_z^2(H-P_N)\) and
\(\partial_t\partial_z(H-P_N)=-\partial_z^3(H-P_N)\).
Logarithmic derivatives require the additional contour lower bound for
\(|H|\); that division and its explicit threshold belong to Note48.

## 6. Finite closure, supplied data, and input uncertainty

The coefficient meaning is finite and exact. Write
\(P_N(\tau,z)=\sum_{k=0}^{m_N}a_k(\tau)z^{2k}\). Then

\[
 a_k'=-(2k+2)(2k+1)a_{k+1},\quad a_{m_N+1}=0,
 \qquad
 a_k(\tau)=\sum_{j=0}^{m_N-k}\frac{(-\tau)^j}{j!}
       \frac{(2k+2j)!}{(2k)!}a_{k+j}(0).
 \tag{24}
\]

Reality and evenness persist, as do degree and its leading coefficient.
This is a closed linear system of \(m_N+1\) real polynomial coefficients.
Their induced divisor moments retain all moment orders; no independent
assignment \(S_n=T_n=0\) is made above a short head. The degree-
\(m_N\) real polynomial in \(z^2\), including its scale, has
\(m_N+1\) real coefficient data. A zero-list realization equivalently
supplies \(h_0\), \(m_N\) opposite-pair representatives with conjugation
relations and integer multiplicities. A generic nonreal conjugate pair
of representatives uses two real parameters for those two entries;
real representatives' squares use one each. In all cases
\(m_N\le KN\log(2+N)\) by (6).

The actual initial inputs needed for this theorem are:

1. The complete canonical divisor through \(N\), with all modulus ties,
   conjugates and multiplicities, and \(h_0\).
2. A supplied valid \(C_u\) for the complete initial count, and the finite
   near-origin data (7), already contained in an exact list for \(N\ge1\).
3. The unchanged source identity and its stated integrability, plus the
   fixed time horizon and spatial radii used in (18)–(23).
4. For the observable application, the separately acquired canonical
   count-two tube, cleared contours, collar, scales and gap anchors.

These are finite retained data plus complete analytical count/source
inputs. Knowing theoretically which canonical zeros must be supplied is
not an acquisition or certificate of their values or completeness. No
canonical zeros were computed for this proof.

Input errors require a weighted payment. For example, if the supplied
initial even polynomial has coefficient errors
\(\delta P_0(z)=\sum_{k=0}^{m_N}\delta a_kz^{2k}\), define

\[
 \begin{split}
 U(R,\Delta)&=\sum_{k=0}^{m_N}|\delta a_k|
      \sum_{j=0}^{2k}\binom{2k}{j}R^{2k-j}(2\Delta)^{j/2}\mu_j,\\
 \mu_j&=\mathbb E|X|^j,
 \quad\mu_0=1,\quad\mu_1=\sqrt{2/\pi},\quad
 \mu_j=(j-1)\mu_{j-2}\ (j\ge2).
 \end{split}                                                   \tag{25}
\]

The finite sum is precisely
\(\mathbb E\sum_k|\delta a_k|(R+\sqrt{2\Delta}|X|)^{2k}\).
The Gaussian formula proves that the evolved error is at most
\(U(R,\Delta)\) on the same disk and interval. Its spatial-jet error
is at most \(j!h^{-j}U(R+h,\Delta)\). Thus the right side of (23)
becomes

\[
 \frac{j!}{h^j}
       [\mathcal C(R+h,\Delta)E_N+U(R+h,\Delta)].
 \tag{26}
\]

All degree-dependent weights are displayed; a small unweighted maximum
coefficient error is not an \(N\)-independent stability theorem.

If the acquisition error is specified in factors, put
\(\alpha_\nu=\rho_\nu^{-2}\), use matched supplied factors
\(\widetilde\alpha_\nu\) with the same finite count and multiplicities,
and put \(w_\nu=\max(|\alpha_\nu|,|\widetilde\alpha_\nu|)\).
Finite telescoping gives the initial bound

\[
 |\widetilde P_0(z)-P_N(0,z)|
 \le\left[|\widetilde h_0-h_0|+
       h_0|z|^2\sum_{\nu\le m_N}
             |\widetilde\alpha_\nu-\alpha_\nu|\right]
       \prod_{\nu\le m_N}(1+|z|^2w_\nu).
 \tag{27}
\]

Its Gaussian integral is another explicit finite weighted-polynomial
budget of the form (25). Conversion of a root enclosure uses the exact
identity
\(|\widetilde\rho^{-2}-\rho^{-2}|
=|\widetilde\rho-\rho||\widetilde\rho+\rho|/
(|\widetilde\rho|^2|\rho|^2)\); its nonzero denominator needs payment.
Missing roots or uncertain multiplicities are not covered by an assumed
matching. Their effect must instead be included in an independently valid
initial polynomial/field error.

Likewise, if a supplied initial-field error is represented by
\(\delta f_0(z)=\int_0^\infty\delta\psi_0(u)\cos(zu)\,du\), a valid
source-acquisition budget is

\[
 V(R,\Delta)=\int_0^\infty|\delta\psi_0(u)|
                           e^{\Delta u^2+Ru}\,du<\infty.
 \tag{28}
\]

Under this stated weighted condition, the same Fubini calculation bounds
the evolved error by \(V(R,\Delta)\), and Cauchy gives the corresponding
jet payment. If the initial uncertainty decomposes into polynomial and
source errors, add \(U+V\) in (26). This is error accounting for supplied
data of the unchanged target, not authorization to replace its physical
source. An additional uniformity claim needs uniform weighted budgets;
none follows from coefficientwise convergence alone.

## 7. Premise-level control screen and disposition

This is a fixed-height approximation milestone under [pattern01][class].
It proves convergence with the actual inverse-square-tail rate; it assumes
no sign for any exterior denominator or forcing. Consequently its generic
parts are expected to preserve collisions. The following analytical
screen uses the documented control sources, rather than new numerical
checks. An absent literal theta identity is a failure of the **canonical
application identification**, not automatically a failure of the generic
growth/count approximation hypotheses.

| Control class | Actual premise check and consequence |
| --- | --- |
| Finite even quadratic/quartic heat fields | If the chosen initial value at the origin is nonzero, their finite paired products are exact once the divisor is included; hence the approximation reproduces their collisions. A control initialized with a zero at the origin fails the particular nonzero-normalization convention (2), not heat flow or collision regularity. No lower growing-count premise is required here. |
| Euler-factor translates | They fail literal unchanged theta/completed initial data. A surviving order-one product, count bound and Gaussian representation can still satisfy this approximation theorem for their own field, including its collision; no derived error bound here rejects them. |
| Weighted-square, finite-source, finite-score and finite-prime controls | Their full reflected unit-weight theta identification fails; the documented endpoint-defective subclasses also fail the canonical fixed strip. Whether a member meets the displayed generic count/product bounds must be checked separately. Where it does, approximation preserves its event. Preserving finitely many scores or prime identities does not supply the missing canonical identity. |
| Reflected super-Gaussian control | It fails the order-at-most-one paired-product input used here, as well as canonical arithmetic; its stronger-than-order-one growth cannot be silently put into (8). This failure says nothing about other approximation methods for that control. |
| Smooth shape and positive-primitive controls | Literal theta arithmetic fails; the specific canonical strip/count/product transfer is unpaid. No newly proved failure of a derived coarse envelope is asserted. They would be approximated, with their collisions, if the generic inputs were independently supplied. |
| Atomic threshold and finite-profile controls | Their canonical source/full-profile identity fails. Atomicity and absent canonical lower population asymptotics are not failures of this theorem: some such fields have an order-one product, suitable upper count and exact Gaussian evolution. Such controls are included wherever those inputs hold, with their collisions intact. |
| RH-conditional endpoint mergers | Ordinary Dirichlet arithmetic changes and RH remains a premise of their construction. The generic approximation can still apply to their own field; it supplies neither an original-theta collision exclusion nor a new RH assertion. |
| Changed observation kernels with fixed amplitude | They fail the physical cosine readout and the associated Newman heat evolution used in (16)–(17). No conclusion about other kernel evolutions is inferred. |
| Fractional-profile positive-measure relaxations | Integer zero-occurrence/divisor realization is not supplied. A fractional relaxed mass is not the canonical product input (2). |
| Complete static divisor surgery / identical-count controls | Static count/growth alone supplies no unchanged canonical common-time source representation. Initializing their own polynomial heat field would be a new control evolution, not identification with the canonical tube. The static sign obstruction retains its static-class scope. |
| Scalar hierarchy equilibria | A finite or canonical divisor/source realization has not been supplied; satisfying the consumer ODEs is not the input (2). |
| Counter-kernels \(q,q_{T,a}\), smooth-density and two-channel screens | These are controls for broader shape/sign/factor mechanisms. No identification with (1)–(2) is supplied. If a counter-kernel does satisfy its own version of the present generic inputs, the approximation remains valid and preserves its collision. The smooth-density and two-channel results concern their stated spectral/factor classes, not a failure of the field-error estimate. |

The control catalog, rather than any shared positive-source or count-only
identity, owns the distinguishing premise statements. This proof supplies
no new signed arithmetic margin, all-real exterior assumption, global
strip for evolved polynomials, tube acquisition, anchor acquisition,
uniform-height limit, simultaneous order/divisor limit or computational
advantage over direct residues with the same finite data. Its finite
coefficient closure differs from the short-head truncation considered
in B05. The one permitted proof pass needed no changed source, domain,
approximation or new mathematical premise; the telescoping sharpening
was the bounded local estimate refinement described in Section 3.

**Component disposition:** steps 1–3 and spatial jets of E16's frozen
route are proved with the explicit constants (8), (12), (18), (21), (23).
Note48 owns the paid contour/transport continuation. The separate E40
assessment, not this author's self-check, determines promotion readiness.
This component warrants no new numerical campaign.

[r4]: ../research-progress/handoffs/VCD-GT-CM-E16-r4.md
[r1]: ../research-progress/handoffs/VCD-GT-CM-E16-r1.md
[pins]: ../research-progress/handoffs/VCD-GT-CM-E16-inputs-r4.json
[b05]: 15_VCD_GT_CM_B05_BBGKY_TRUNCATION_RECONSIDERATION_20261118.md
[hierarchy]: 09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[framework]: ../manuscript/sections/01_framework.tex
[n48]: 48_VCD_GT_CM_E16_COUNTED_MOMENT_AND_TRANSPORT_TRANSFER_20261118.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
