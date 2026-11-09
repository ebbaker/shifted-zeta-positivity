# E02 assessment of the Lehmer force bound and acquisition decision

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OA chat0003. The chat registry
exposes no actual model identifier or reasoning effort. Internal
analytical assessment, with read-only LLM checks of groups 2–4 and
shared source premises.

**E02 r1 is complete.** All four groups are accepted at their stated
scope. The bounded source and sign clarifications in
[Note10](../notes/10_TND_OA_E02_LEHMER_SCOPE_CLARIFICATIONS_20261109.md)
leave the algebra and decision intact. The result is an information
diagnostic and a scoped acquisition decision. The positive starting
tuple and quantitative comparison remain unacquired.
[Frozen request r1](../research-progress/handoffs/05_TND_OA_E02_LEHMER_SCREEN_ASSESSMENT_REQUEST_20261109.md),
[Note08](../notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md),
[proof-author self-check](05_TND_OA_B03_DIRECTION_AND_CONTROL_SELF_CHECK_20261109.md),
[classification](../../../../../../avoid/01_restating_the_target.md).

## 1. Normalization and starting evidence — accepted

Let \(\Phi\) denote the branch's kernel in \(H_\lambda\). The sum in
Stopple §2 is \(2\Phi(u/2)\). Write \(\widehat H_t\) for his
deformation \(\Xi_t\). Substituting \(u=2v\) gives
\[
\widehat H_t(\gamma)=
\int_0^\infty e^{tu^2}\,2\Phi(u/2)\cos(\gamma u)\,du
=4\int_0^\infty e^{4tv^2}\Phi(v)\cos(2\gamma v)\,dv
=4H_{4t}(2\gamma).
\]
The two factors of two come from the kernel and the integration
measure. At \(t=0\), Stopple's full \(\Xi\) is \(2\widehat H_0\),
so \(H_0(x)=\Xi(x/2)/8\). Physical height is \(x=2\gamma\) and
Newman time is \(\lambda=4t\). Figure 1 identifies Lehmer's classical
pair \(\gamma_{6709},\gamma_{6710}\) near ordinate \(7005\), hence
physical height near \(14010\), at time zero. The paper's standing
RH assumption remains part of its use of exterior sums.
[Stopple v2, abstract and §§1–3](https://arxiv.org/html/1508.05870v2).

E01 starts at \(\lambda_s>0\) with actual simple roots there,
then follows imaginary time \(\tau=\lambda_s-\lambda\) with
\(0<\Delta\le\lambda_s\le1/2\). A simple time-zero pair gives local
real continuation by the implicit function theorem. It leaves a
specified positive time radius, certified initial enclosures and a
matched baseline to be acquired. Taking the documented zero-time
slice as \(\lambda_s=0\) cannot supply a positive allowed \(\Delta\).
[E01 assessment](03_TND_OA_E01_R1_REGULAR_DEFLATION_ASSESSMENT_20261109.md).

The corrected COSV paper uses the branch's physical normalization
in (1.1)–(1.4). Its Theorem 1.1 gives \(\Lambda>0\) in the
\(g_k(0)\le0\) case, and a lower estimate \(\lambda_k\le\Lambda\)
for \(g_k(0)>0\) under the stated Lehmer condition. Its separate
high-pair tail estimates use a negative-threshold proof case.
They supply no positive-time root enclosure for the Stopple pair.
Theorem 2.2's reported lower bound is (2.18), with (2.19) the
Taylor expansion used after that statement. The assessment uses
the direction and premises without transferring numerical
thresholds between conventions.
[Corrected COSV paper, pp.104–106 and 110](https://etna.ricam.oeaw.ac.at/vol.1.1993/pp104-111.dir/pp104-111.pdf),
[branch source record](../references/03_TND_OA_B03_LEHMER_SOURCE_USE_20261109.md).

## 2. Exterior sum and differential inequality — accepted

With \(\delta=b-a>0\), \(q=\delta^2\), and the stated absolutely
and uniformly convergent derivative of the exterior product, each
zero \(\rho\notin[a,b]\) contributes
\[
\frac1\delta\int_a^b-\frac{dx}{(x-\rho)^2}
=-\frac1{(a-\rho)(b-\rho)}
\]
to \(B\). In the order-one product the exponential linear factor
drops out of the derivative of the logarithmic derivative. The
squared reciprocal tail bounds the derivative series uniformly
on the fixed segment because the far zeros satisfy
\(\inf_{x\in[a,b]}|x-\rho|\ge|\rho|/2\). The finitely many nearer
zeros have positive distance from the segment. Set \(u=a-\rho\)
and \(v=b-\rho\). The endpoint sum plus twice the force term is
\(u^{-2}+v^{-2}-2/(uv)=(v-u)^2/(u^2v^2)\).
For real exterior zeros outside the segment, \(uv>0\), and
summing gives \(G+2B=qS\ge0\) and \(-G/2\le B\le0\).
The upper bound is strict at a slice with at least one exterior
zero. Under \(x=2\gamma\), \(G_\gamma=4G_x\) and
\(q_\gamma=q_x/4\), so \(qG\) is invariant.

If \(G\le G_*\), then \(B\ge-G_*/2\). Multiplication by \(-4q<0\)
reverses the direction and gives \(q'=-8-4qB\le-8+2G_*q\) in
imaginary time. E01 uses \(B\le b_{\rm up}\) to get
\(q'\ge-8-4b_{\rm up}q\), the direction needed for a survival
lower bound. A time-zero value supplies neither uniform exterior
control nor the required improved upper force on the slab.
Complex conjugate exterior zeros can preserve the algebra and
reality of the total when convergence is paid, while losing both
termwise sign arguments. See [Note10](../notes/10_TND_OA_E02_LEHMER_SCOPE_CLARIFICATIONS_20261109.md).

## 3. Exact quartic heat control — accepted

The two derivatives \(h_\tau\) and \(h_{zz}\) equal
\(12z^2+24\tau-10\). At \(\tau=0\) the polynomial is
\((z^2-1)(z^2-4)\), with four simple roots. For the positive
pair \(a=1,b=2\), the exterior distances are \((2,3)\) and
\((3,4)\). Thus
\[
q=1,\qquad G=\frac14+\frac29+\frac1{16}=\frac{77}{144},
\qquad B=-\frac16-\frac1{12}=-\frac14,\qquad
S=\frac1{36}+\frac1{144}=\frac5{144}.
\]
In particular \(qG<4/5\) and \(G+2B=qS\).

As a quadratic in \(w=z^2\), its discriminant is
\(96\tau^2-80\tau+9\), with roots \((10\pm\sqrt{46})/24\).
The smaller one, \(T\), satisfies \(1/8<T<1/4\) from
\(6<\sqrt{46}<7\). For \(0\le\tau<T\), the distinct real \(w\)-roots
have positive sum \(5-12\tau\) and positive product
\(12(\tau-5/12)^2+23/12\), so both are positive. At \(T\),
\(h=(z^2-r^2)^2\) with \(r^2=\sqrt{46}/4\) and
\(h_{zz}(T,r)=8r^2=2\sqrt{46}\). The positive double is
nondegenerate even though there is a simultaneous reflected
double at \(-r\). The discriminant is negative immediately after
\(T\).

Before \(T\) the negative pair contributes
\[
B=-\frac{1}{2a(a+b)}-\frac{1}{2b(a+b)}
=-\frac1{2ab}<0.
\]
The attraction-only equation starting at \(q=1\) would close the gap
at \(1/8\). Here \(q'>-8\) before the event and \(T>1/8\).
The favorable force delays this collision. With
\(F_\lambda=h(1/4-\lambda,\cdot)\) one has
\(\partial_\lambda F=-F_{zz}\) and the event time is
\(\lambda_*=(\sqrt{46}-4)/24>0\).
This checks a finite polynomial heat family, where a small-gap
diagnostic and a favorable sign do not guarantee survival.
No failure of a particular uncomputed E01 box margin is inferred.

## 4. Scoped decision and control premises — accepted

The inspected passages leave three missing inputs for this one
candidate. They are an actual certified positive start, a specific
unmet quantitative comparison, and a full-source budget for
factor floor, confinement and upper force. B02's RT/HDC chart
at \(x=36\) with radius 11 cannot furnish those data at \(x\approx14010\).
Its sufficient redundancy condition \(Q_-Q_+>32D^2\Delta\) is
unevaluated here. Failure of that condition in a future case
would only remove one sufficient implication. It would establish
neither failure of unsigned survival nor a signed-force advantage.
[Note06 §§1–3](../notes/06_TND_OA_B02_CANONICAL_PILOT_AND_REDUNDANT_GAP_GATE_20261109.md).

The [control inventory](../../../../../../result-summaries/12_collision_controls_and_screening.md)
supports the distinctions in Note08. In the canonical import, the
Euler-factor controls lack unchanged coefficients/completion.
Weighted-square controls lack the full unit weights and normalized
reflection. Reflected super-Gaussian controls lack the integer-square
expansion. Shape and positive-primitive controls lack the unchanged
theta source. Finite-source and finite-prime orbit controls lack the
full source/reflection. Fixed-event and finite-profile threshold
controls lack the full profile, theta coefficients and eventual
simplicity. The RH-conditional endpoint control lacks ordinary
Dirichlet-series arithmetic. The variable-kernel control lacks
literal cosine and the physical heat equation. The profile-measure
relaxation lacks an integer divisor of the physical field.
Those failures pertain to the canonical input. The quartic itself
passes the generic real-product identity, and a family with
real positive-time descendants can share it on the slices where
the stated product and adjacency hold. The premise audit neither
replays old certificates nor assigns a quantitative failure on
an unmatched domain. [Control-premise discipline](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope discipline](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The stop applies to this acquisition cycle and inspected evidence.
The evidence leaves other cases and estimators open. E01 remains
accepted with its own premises. [Decision03](../brainstorm/notes/03_TND_OA_B03_PARK_FINITE_PAIR_ACQUISITION_20261109.md),
[post-E02 continuation](../notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md).
