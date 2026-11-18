# VCD-GT-CM-E11 r1 — Integer closure assessment

18 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Requested assessor dispatch **gpt-6.1-sol / ultra**.
Independent serving-model and actual effort metadata were unavailable.
The assessor did not author E09 or E10. This separate-agent internal
assessment shares repository premises with both proofs. [Shared premises05][shared]

**Accepted within the frozen domains.** All seven [E11 pins][request]
matched. One full pass checked the two proofs and their requests and
returns, the [B04 contract][b04] and the inherited proof and assessment.
One bounded correction check rechecked the low-order coefficients,
combined target residues and two quartic derivative calculations.
No mathematical correction was required. The recurrences provide
representations of relative integer time evolution.
[Result index][results] · [Cluster18][cluster] · [Avoid index][avoid] ·
[Classification01][class] · [E09 request][e09req] · [E09 return][e09ret] ·
[E10 request][e10req] · [E10 return][e10ret]

## 1. Split recurrence on \(D\ne0\) charts

Use the unchanged complete \(H_t=-H_{zz}\) on the independently paid compact
real count-two tube, \(T\ge64\), \(\ell=1/\log T\),
\(r_0=a\ell\), \(\max(2,4\sqrt d)\le a\le\log T\), \(c\in[T,2T]\)
and \(|D|\le d\ell^2\le r_0^2/16\). The targets \(c\pm s\),
\(s^2=D\), have displacements at most \(r_0/4\). All exterior occurrences
have \(|w_j|\ge r_0\) and \(|\Im w_j|\le1\). Use the inherited source
holomorphy, order-at-most-one product and complete closed-slab unit count.
The primes denote physical time derivatives. [Note41 §§1–2][n41] ·
[GR Note02 §§1, 3][gr02] · [GR E05][gr05]

For the finite derivation put \(x=w-s,\ y=w+s,\ d_0=2s,\ Q=xy\).
With \(f_{m,n}=x^{-m}y^{-n}\), the two differences of powers in
Note08 (8) give the negative divided difference of the product.
That full kernel is symmetric in the two root arguments.
The factor of two from the physical root velocities turns its
unordered sum into the ordered off-diagonal sum. The first
convolution removes \(mP_{m+1,n}\) on the diagonal, the second
removes \(nP_{m,n+1}\). For \(m,n\ge1\) the endpoints \(i=1\)
and \(j=n\) of (8) each leave one first-power factor.
The remaining ranges \(2\le i\le m\) and \(1\le j\le n-1\)
in (1) have both factors of degree at least two, also when
\(m=1\) or \(n=1\). On the \(m\) axis \(i=1,m\) give
\(2P_{1,0}P_{m,0}\), leaving \(2\le i\le m-1\).
On the \(n\) axis \(j=1,n\) give \(2P_{0,1}P_{0,n}\),
leaving \(2\le j\le n-1\). The pure derivative blocks have
\(m=p+1\ge3\) or \(n=q+1\ge3\), so the endpoints are distinct.
These are the convolutions (1)–(2), with the stated empty-sum
convention. [Note08 (1)–(2), (8)][e09]

The target velocities have relative signs \(+2/d_0\) and
\(-2/d_0\); their first-power terms are \(-2P_{1,0}\) and
\(-2P_{0,1}\). In (7) the mixed pair-sum endpoints cancel each
moving-coordinate drift up to \(-d_0MP_{p+1,q}\) and
\(+d_0MP_{p,q+1}\), respectively, by
\(x^{-1}-y^{-1}=d_0/Q\). On each pure axis the two endpoints
cancel the whole first-power term. Each derivative includes
the two target force terms with coefficient \(-2\) in its
block. Adding the respective diagonal removals gives exactly
\(p+3,q+2\) and \(p+2,q+3\) in (3), and the axis coefficients
in (4). For degree two on the \(p\) axis the convolution
is \(C_{3,0}=P_{2,0}^2\); on the \(q\) axis
\(C_{0,3}=P_{0,2}^2\). With one exterior occurrence the
\(p=2\) formula reduces to
\(-8x^{-4}-4x^{-3}y^{-1}+4d_0^{-1}x^{-3}\), also obtained
by differentiating \(x^{-2}\) with the direct velocity.
The other axis follows under label exchange. The target difference
gives \(d_0'=4/d_0-2d_0M\), \(s'=1/s-2sM\) and
\(D'=2-4DM\). The combined first-power difference converges as
\(\sum_j d_0/Q_j\) at common cutoff, with no separate absolute
\(P_{1,0}\) or \(P_{0,1}\) premise. [Note08 (3)–(8)][e09]

For \(p=q=n\), the difference \(P_{n+1,n}-P_{n,n+1}\)
is \(d_0S_{n+1}\), and the sum \(P_{n+2,n}+P_{n,n+2}\)
is \(2S_{n+1}+d_0^2S_{n+2}\). Substituting these gives
Note08 (10). At \(n=1\) the convolution leaves \(2M^2\) after
the cancellation of \(d_0^2MS_2\). At \(n=2\), writing the
crossed products via their pair sums and differences cancels
the \(T_2T_3\) and \(d_0^4S_2S_3\) terms. The remaining convolution
is \(4MS_2+2T_2^2+d_0^2MS_3+(d_0^2/2)S_2^2\), and substituting
into (10) cancels \(d_0^2 MS_3\) and gives the inherited
\(S_2'\), including \(+4T_2^2\). Label exchange swaps \(p,q\)
and changes the signs of \(d_0,A_d\). This transforms the
actual moment equations by symmetry of the divided differences.
For real time conjugation fixes the moments when \(s\) is real
and swaps the two indices when \(s\) is purely imaginary.
[Note08 §§4–5][e09] · [GR E05][gr05]

## 2. Collision-regular \(S,T\) rows

Use \(m_j=Q_j^{-1}\), \(S_n=\sum_jm_j^n\) for \(n\ge1\) and
\(T_n=\sum_j w_jm_j^n\) for \(n\ge2\). The inverse first-power
drift \(P=T_1\) is a finite-calculation symbol. Factoring
\(A^k-B^k=(A-B)C_k\) gives the first divided difference (3).
The identities \(A^k=C_kA-AB C_{k-1}\),
\(B^k=C_kB-AB C_{k-1}\) give the second, including \(k=1\).
For the pair sums (4), the even-term \(u+v\) makes the two
ordered sums equal and cancels the unordered factor \(1/2\).
Each diagonal there removes \(T_{h+1}\). The three terms of the
negative odd divided difference \(-\mathcal O_{n+1}\)
remove respectively \(S_{n+1}\), \(D S_{n+2}\), and
\(S_{n+1}+D S_{n+2}\) per convolution term. The last is the
exact \(w^2=Q+D\) diagonal. [Note09 (2)–(4)][e10]

In the \(S_n'\) derivation, differentiating \(Q^{-n}\) and
symmetrizing gives (5). The \(T\)-convolution has length
\(n+1\), with endpoints \(T_1T_{n+1},T_{n+1}T_1\).
They cancel \(-4nPT_{n+1}\). The corresponding \(D S\)
endpoints cancel the \(-4nDS_1S_{n+1}\) part of \(nD'S_{n+1}\).
The diagonal counts and the target terms then give
\(-4n(n+2)S_{n+1}-4n(n+3)DS_{n+2}\) and the two displayed
convolutions in (1). This includes \(n=1\), where the second
interior convolution is empty.
[Note09 (1), (4)–(5)][e10]

For the odd weight \(f=wQ^{-n}\),
\(f_w=(1-2n)Q^{-n}-2nD Q^{-n-1}\).
The two \(r=1\) endpoints in the pair sums of (6) cancel
the \(P S_n\) and \(DP S_{n+1}\) terms; the \(r=n+1\) endpoint
in the \(D\)-weighted convolution cancels the interaction part
of \(nD'T_{n+1}\). The surviving ranges are \(2\le r\le n\)
in both convolutions. Summing the first diagonal and direct
terms gives \(2n+4(1-2n)+2n(1-2n)=-4(n^2+n-1)\).
The \(D\)-weighted coefficient is \(-8n-4n(n+1)=-4n(n+3)\).
Thus all \(n\ge2\) give the odd row, and \(n=2\) is
\[
 T_2'=(6S_1+8DS_2)T_2-20T_3-40DT_4 .
\]
Substituting \(n=1,2\) into the even row gives the two inherited
laws in (7). The cancellations take place before complete
passage. [Note09 (1), (4), (6)–(7)][e10] · [GR Note02 §2][gr02]

## 3. Target contours, limits and coalescing labels

At a reference time the positive stationary circle of radius
\(r_0/2\) contains both targets and excludes the exterior. Local
counted moments recover analytic \(c,D\). For either split kernel
or the regular rational weights the contour integral of the
weight alone vanishes by decay at infinity. A retained exterior
pole contributes minus the weight at its location, and a constant
or the genus-one log-derivative regularizers vanish after
integration. The target term is the weight times \(Q_z/Q\);
its combined integral is zero by decay at infinity and
inclusion of all poles. Individual contributions may survive:
for \(p=2,q=0\) the factor
\((z-z_+)^{-2}/(z-z_-)\) contributes \(-d_0^{-2}\) at \(z_+\)
and \(+d_0^{-2}\) at \(z_-\), while \((z-z_+)^{-3}\) has
zero residue. For diagonal powers the target term is a
spatial derivative. The total zero integral differentiates
as one identity on the fixed contour, including at the double
for the regular weights. The fixed-\(z\) derivative retains
the moving kernel, \(Q_t=-2(z-c)c'-D'\), and the full heat
derivative \(-H_{zzz}/H+H_zH_{zz}/H^2\).
[Note08 §3][e09] · [Note09 §3][e10] · [GR E05][gr05]

At polynomial multiples, perturbing factors at the reference
slice preserves the separated contour count. Each perturbed
field has its own heat evolution from that slice. The first
contour jets and the already canceled finite right sides then
converge. At a canonical reference slice, keeping all ties,
conjugates, opposite pairs and multiplicities in the modulus
cutoff retains exactly the target factors for sufficiently
large \(N\). The inherited \(O(\log N/N)\) omitted product
tail pays compact spatial convergence through order three.
The heat law gives the corresponding first time jets on each
fixed collar, including the jets of \(c,D\). On a split chart
the extra weight derivative uses \(s'=D'/(2s)\) with \(s\)
bounded away from zero on compact subcharts. The value tails
for \(N>4T+8\) are \(O(N^{1-p-q}\log N)\),
\(O(N^{1-2n}\log N)\), and \(O(N^{2-2n}\log N)\) for the
split, even and odd moments respectively. They follow by
summing the inherited unit count against the far powers
\(p+q,2n,2n-1\). Constants may depend on the fixed indices.
The time-jet passage is uniform at fixed \(T\) on compact
paid subcharts, with a finite fixed-height cover across
\(D=0\) for the regular moments. The proof passes separately
initialized slice jets, including at repeated exterior
locations and paid endpoints. It supplies no uniform-order
limit or common time interval for the truncated heat flows.
[Note08 §3][e09] · [Note09 §3][e10] · [GR Note02 §3][gr02]

For \(k=\max(p,q)\) the split weight has denominator \(Q^k\)
and numerator \((w-s)^{k-p}(w+s)^{k-q}\), of degree at most
\(2k-2\) in \(w\). An even term reduces by
\(w^{2j}=(Q+D)^j\) and \(j\le k-1\), hence brings in \(S_1\)
or higher. An odd term has \(j\le k-2\) and brings in
\(T_2\) or higher. The coefficients are polynomial in \(s\)
after \(D=s^2\). Conversely the identities
\(S_n=P_{n,n}\), \(T_n=(P_{n-1,n}+P_{n,n-1})/2\)
follow directly from \(xy=Q\) and \(x+y=2w\).
The split and regular families describe the same relative
moments on a labeled \(D\ne0\) chart. At \(D=0\) the regular
family is analytic in physical time, including the components
recovered as divided antisymmetric combinations. Raw split
values alone coalesce there. The deflated contour also shows
a joint analytic extension in time and an independent \(s\)
near zero, with the actual counted target deflated. Substituting
\(s^2=D(t)\) gives \(P_{p,q}=A(t)+sB(t)\).
With \(D'(t_*)=2\), an unsymmetrized derivative behaves as
\(B(t_*)/s\) if \(B(t_*)=(p-q)\sum_jw_j(t_*)^{-p-q-1}\ne0\).
The coefficient's nonvanishing at a canonical merger remains
unproved. [Note08 §5][e09] · [Note09 §4][e10]

## 4. Quartic cross-check and disposition

In the even quartic
\(F(\tau,z)=(z^2-b^2)^2-\tau(12z^2-4b^2)+12\tau^2\),
\(-F_{zz}=F_\tau\). At the simultaneous doubles the Laurent
coefficients of \(F_\tau/F\) at \(+b\) are \(-2\) and
\(-4/b\) at orders \(-2,-1\). The target factor derivative
therefore gives \(D'(0)=2,\ c'(0)=2/b\), independently
of the recurrences. Exterior reflection gives mean \(u_0=-2b\)
with mean velocity \(8/u_0\). The even Taylor trace over the
exterior pair gives the derivative
\(2(8/u_0)f_w+4f_D+2f_{ww}\) at \((u_0,0)\).
With \(f=Q^{-n}\) this is \(8n(n-3)u_0^{-2n-2}\);
with \(f=wQ^{-n}\) it is \(8(n^2-4n+2)u_0^{-2n-1}\).
Independently, in the even recurrence (1) the coefficient
of \(u_0^{-2n-2}\) at \(D=0\) is
\(8n^2+8n(n-1)-8n(n+2)\). In the odd recurrence the coefficient
of \(u_0^{-2n-1}\) is \(8(2n-1)(n-1)-8(n^2+n-1)\).
These match at every allowed index. For \(b=1\),
\(B(0)=2T_2(0)=-1/2\) for \(P_{2,0}\), and the individual
split derivative has a genuine square-root singularity in this
finite polynomial family. [Note08 §5][e09] · [Note09 §5][e10]

The polynomial heat controls admit the algebra through a
counted collision and lack the canonical growing divisor.
Euler translates change the arithmetic and canonical count
discrepancy while a coarse upper count can survive.
Weighted-square and finite-source/score/prime changes fail the
full reflected unit-weight theta equality. The documented
endpoint-defective subclasses fail the fixed strip. The reflected
super-Gaussian fails the order input used for the canonical
product. Smooth-shape and positive-primitive sources change
theta arithmetic, with strip/count transfer unpaid. Atomic and
finite-profile controls lack canonical population growth and full
profile. RH-conditional endpoint mergers change ordinary
Dirichlet arithmetic and assume RH. Changed observations lose
the physical cosine readout, and fractional profiles lack
integer occurrences. Changed static slices lack a common paid
canonical heat tube and the scalar equilibrium lacks a realized
divisor. This was a documentary screen of the actual premises.
[Controls12][controls] · [Premises02][premises] · [Scope07][scope] ·
[CM E04 §5][cm04]

**B04 closure test satisfied.** Every displayed relative
moment derivative has a finite algebraic expression in the
enlarged infinite family together with the gap coordinate.
The absolute midpoint retains its inherited contour drift.
A finite truncation, an arbitrary-sequence infinite-ODE
well-posedness theorem and a signed forcing or transport gain
remain outside these proofs. The earlier denominator-only
nonclosure comparison keeps its specified finite polynomial
class. It leaves room for the enlarged family proved here and
does not settle a canonical denominator-only classification.
No frozen input, manuscript, register or history changes, new
literature imports or numerical campaigns were needed.
[Note44 §6][n44] · [GR E05][gr05] · [B04][b04]

[request]: ../research-progress/handoffs/VCD-GT-CM-E11-r1.md
[b04]: ../brainstorm/notes/04_VCD_GT_CM_B04_SPLIT_POLE_CLOSURE_CONTRACT_20261118.md
[e09req]: ../research-progress/handoffs/VCD-GT-CM-E09-r1.md
[e09ret]: ../research-progress/handoffs/VCD-GT-CM-E09-return-r1.md
[e10req]: ../research-progress/handoffs/VCD-GT-CM-E10-r1.md
[e10ret]: ../research-progress/handoffs/VCD-GT-CM-E10-return-r1.md
[e09]: ../notes/08_VCD_GT_CM_E09_SPLIT_POLE_INTEGER_HIERARCHY_20261118.md
[e10]: ../notes/09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[n44]: ../../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md
[gr02]: ../../01_gaussian_resolvent_hierarchy/notes/02_VCD_GT_GR_E02_CANONICAL_MOMENTS_20261117.md
[gr05]: ../../01_gaussian_resolvent_hierarchy/reviews/03_VCD_GT_GR_E05_INITIAL_PROOFS_ASSESSMENT_20261117.md
[cm04]: 03_VCD_GT_CM_E04_CONTOUR_PROOFS_ASSESSMENT_20261117.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[shared]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md

