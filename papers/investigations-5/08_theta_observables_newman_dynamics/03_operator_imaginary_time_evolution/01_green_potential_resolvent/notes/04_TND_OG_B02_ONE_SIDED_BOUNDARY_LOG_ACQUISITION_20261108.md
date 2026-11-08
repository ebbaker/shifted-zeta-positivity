# B02: one-sided boundary-log acquisition through real zeros

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Exact backend identifier and reasoning
effort are unavailable in accessible session metadata. No model switch or
independent assessment is claimed.

**Status:** the local line-sublevel/envelope lemma in section 2 and its
canonical local application in section 3 are **proved in-note, with
proof-author self-check only**. The full finite-source/prime-tail Green
assembly in section 4 is an **E03 target**, not a completed theorem or
computed certificate. No favorable canonical signed upper margin is
acquired. The [sole register](../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md)
owns live status.

## 1. The bounded decision

Keep time zero, the complete theta source, and
\[
 s(z)=\tfrac12-\tfrac i2z,\quad
 F(z)=\frac{s(z)-1}{s(z)}\zeta(s(z))=D_0(z)H_0(z),\quad
 D_0(z)=\frac{16\pi^{s(z)/2}}{s(z)^2\Gamma(s(z)/2)}.
 \tag{1}
\]
On the real boundary the rational factor has modulus one. The inherited
prime decomposition therefore reads
\[
 J_0^{\rm G}(X)=\int_{\mathbb R}K(x-X)\log|F(x)|\,dx-P(X)+G(X,1),
 \quad K(t)=\frac1{16\cosh(\pi t/8)}.
 \tag{2}
\]
Here P and its integer-cutoff error are exactly the
[parent prime proposition](../../manuscript/sections/17_green_strip.tex).
The plus pole correction belongs to (2). It is not an additional atom
in the alternative full two-boundary functional of F.

Two candidates were considered:

| Candidate | Decision and actual missing information |
| --- | --- |
| Replace the quadratic moment by fractional moments, then let their exponent tend to zero | Not selected. The limit recovers the logarithmic mean, so this alone is a representation. No favorable canonical small-exponent bound or uniform remainder was supplied. The short-mollifier theorem does not exclude this class. |
| Acquire the boundary logarithm directly from a pointwise upper modulus envelope | Selected for a bounded acquisition theorem. The line-sublevel calculation below pays the error near real zeros without dividing by the boundary field or approximating it by a zero-free function. The remaining global assembly is fixed as E03. |

The distinction from the
[sibling area-log estimate](../../02_localized_zero_correlations/notes/02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md)
is essential: a two-dimensional integral bound does not control its
one-dimensional trace. We reuse its nested disks and factor-removal
argument, then derive a separate line estimate. The
[sibling harmonic-baseline obstruction](../../02_localized_zero_correlations/notes/04_TND_OC_B02_SIGNED_JENSEN_AND_HARMONIC_DISTANCE_20261107.md)
does not apply: the approximant here may have zeros, and its logarithm is
not discarded as harmonic.

Classification under [avoid01](../../../../../../avoid/01_restating_the_target.md):
(2) is an inherited representation; the explicit error modulus below is
a quantitative acquisition result. Neither is evidence for the universal
vanishing statement already classified in the overview. The exact
canonical value remains to be bounded or computed.

## 2. A line-sublevel lemma and a one-sided logarithmic envelope

Set
\[
 R_0=\frac92,\quad \rho=\frac{13}3,\quad r_0=\frac{25}6,\quad
 B=R_0+r_0=\frac{26}3,\quad
 \kappa=\log(27/26),\quad
 \frac{\rho+r_0}{\rho-r_0}=51.
 \tag{3}
\]
Let f be holomorphic on a neighborhood of the closed disk of radius
R_0, with \(|f|\le1\) there and \(|f(0)|\ge m>0\).
Write
\[
 A=\log(1/m),\qquad
 n=\max\{2,\lceil A/\kappa\rceil\},\qquad
 C=2Bn\,e^{51A/n}.
 \tag{4}
\]
Let \(\Gamma\) be a horizontal segment of length at most one in the
closed disk of radius r_0. Then for every \(t>0\),
\[
 |\{z\in\Gamma:|f(z)|<t\}|\le C t^{1/n}.
 \tag{5}
\]
If g is measurable on that segment and
\(|f-g|\le\epsilon\), with \(\epsilon>0\), then
\[
 \boxed{\quad
 0\le\int_\Gamma
   \{\log(|g|+\epsilon)-\log|f|\}\,d\ell
 \le \frac{C n^2}{n-1}(2\epsilon)^{1/n}.
 \quad}
 \tag{6}
\]
No lower modulus for f on the segment, nonvanishing of g, holomorphy of g,
zero separation or simplicity is assumed.

### Proof of (5)

Jensen's formula bounds the number k of zeros in the open disk of radius
rho, with multiplicity, by \(k\kappa\le A\). Remove exactly these zeros
using disk Blaschke factors
\[
 b_j(z)=\frac{R_0(z-a_j)}{R_0^2-\overline{a_j}z},\qquad
 h=f/\prod_{j=1}^k b_j.
 \tag{7}
\]
The removable values are filled in. The factors have boundary modulus
one, so \(|h|\le1\) on the outer disk. It has no zeros in the open
rho disk, and \(|h(0)|\ge m\). Harnack applied to
\(-\log|h|\ge0\) gives \(|h|\ge e^{-51A}\) on the r_0 disk.
If a residual zero lies on the rho circle, apply Harnack on smaller
circles first and pass to the limit. Thus
\[
 |f(z)|\ge e^{-51A}
       \prod_{j=1}^k\frac{|z-a_j|}{B}\quad (|z|\le r_0).
 \tag{8}
\]
Every distance ratio here is less than one. If \(q=e^{51A}t<1\),
the sublevel set is empty when k=0. Otherwise it is covered by k disks
of radius \(Bq^{1/k}\). Each intersects a line in length at most twice
its radius. Since \(k\le n\) and \(q<1\), the total length is at most
\(2Bn q^{1/n}=Ct^{1/n}\). For q>=1 the same bound exceeds the
segment length and is automatic. This proves (5).

Jensen and Harnack are classical inputs, freshly passage-checked in the
author's lecture notes; [source-use04](../references/04_TND_OG_B02_SIGNED_LOG_SOURCE_USE_20261108.md)
records the exact statements. The constants and one-dimensional
application are derived here, not attributed to those statements.

### Proof of (6)

The triangle inequality gives, away from the finitely many segment zeros,
\[
 0\le\log(|g|+\epsilon)-\log|f|
 \le\log(1+2\epsilon/|f|).
 \tag{9}
\]
For \(h_*=2\epsilon>0\), Tonelli's theorem and (5) give
\[
 \int_\Gamma\log(1+h_*/|f|)\,d\ell
 =\int_0^\infty\frac{h_*}{t(t+h_*)}
          |\{|f|<t\}\cap\Gamma|\,dt.
 \tag{10}
\]
Bound the kernel by \(1/t\) on \((0,h_*)\) and by \(h_*/t^2\)
on \((h_*,\infty)\). The two integrals are at most
\[
 Cn h_*^{1/n},\qquad
 C\frac n{n-1}h_*^{1/n}.
 \tag{11}
\]
Their sum is (6). The deliberate choice n>=2 avoids an endpoint
logarithm at n=1. Formula (5) also proves local integrability of
\(\log^-|f|\), so all integrals used in (6) are defined. Multiple
real zeros remain in the calculation with their true multiplicity.

The same layer-cake estimate gives the useful local tail input
\[
 \int_\Gamma|\log|M f||\,d\ell
 \le\log M+Cn,\qquad M\ge1.
 \tag{12}
\]
Indeed \(|\log|Mf||\le\log M+\log^-|f|\), and integration of
(5) over \(0<t<1\) with measure \(dt/t\) gives Cn.

## 3. Canonical local application, including height dependence

For any real v, center the disks at \(c_v=v+4i\), and take the
real segment \(I_v=[v-1/2,v+1/2]\). Its distance from c_v is at most
\(\sqrt{65}/2<25/6\). Throughout the outer disk,
\(1/4\le\Re s\le19/4\). The fractional-part identity, with the pole
at s=1 already canceled, gives
\[
 F(z)=1-(s-1)\int_1^\infty\{u\}u^{-s-1}\,du,\qquad
 |F(z)|\le2|v|+25.
 \tag{13}
\]
The elementary bound uses
\(|s-1|\le |v|/2+6\) and \(\Re s\ge1/4\). At c_v the
absolutely convergent Euler product gives
\[
 |F(c_v)|\ge c_0:=\frac35\frac{\zeta(5)}{\zeta(5/2)}>0.
 \tag{14}
\]
Unlike a lower bound on the real segment, this safe-line anchor is
unconditional. The argument works for every real v, including v=0:
F has its removable value at s=1 and has no pole in these disks.

Define
\[
 M_v=2|v|+26,\quad A_v=\log(M_v/c_0),\quad
 n_v=\max\{2,\lceil A_v/\kappa\rceil\},\quad
 C_v=2Bn_v e^{51A_v/n_v}.
 \tag{15}
\]
For any boundary approximant \(\widehat F\) with
\(\sup_{I_v}|F-\widehat F|\le\delta>0\), (6) applied to
\(f=F/M_v,\ g=\widehat F/M_v,\ \epsilon=\delta/M_v\) gives
\[
 \boxed{\quad
 0\le\int_{I_v}
       [\log(|\widehat F|+\delta)-\log|F|]\,dx
 \le {\cal E}_v(\delta)
 :=\frac{C_v n_v^2}{n_v-1}
       \left(\frac{2\delta}{M_v}\right)^{1/n_v}.
 \quad}
 \tag{16}
\]
Also
\[
 \int_{I_v}|\log|F||\,dx\le\log M_v+C_vn_v.
 \tag{17}
\]
These are absolute error bounds for the actual logarithm, not mean-square
residual bounds and not estimates of J itself.

Since \(A_v/n_v\le\kappa\), the prefactor in (16) is
O((log(2+|v|))^2), while \(1/n_v\) is of order
1/log(2+|v|). To make the local allowance at most h, one sufficient
explicit choice is
\[
 \delta\le\frac{M_v}{2}
       \left(\frac{h(n_v-1)}{C_v n_v^2}\right)^{n_v}.
 \tag{18}
\]
Thus the price of small h becomes severe at large height. This is not
a uniform positive Hölder exponent, useful complexity theorem or
canonical discriminating smallness estimate.

As a simple scale check, the real-double-zero factor \(F(x)=x^2\)
has
\[
 \int_{\mathbb R}\{\log(x^2+\delta)-\log x^2\}\,dx
 =2\pi\sqrt{\delta}.
 \tag{19}
\]
Substitute x=sqrt(delta)u and integrate
log(1+u^(-2)) by parts on the positive half-line. There is no fixed
positive error floor, but no Lipschitz error either. This is an
algebraic factor check, not a canonical source control. The conservative
exponent in (16) is not claimed sharp.

## 4. Selected E03 assembly and its exact unpaid value

The local theorem makes one finite execution contract concrete. Let R
be a positive integer, Q>=2 an integer prime-power cutoff, and retain the
literal source approximant \(\widehat F=D_0\widehat H\).
Proposed E03 will construct and verify
\[
 U_{R,Q,\delta}(X)=
 \int_{X-R}^{X+R}K(x-X)\log(|\widehat F(x)|+\delta)\,dx
 +{\cal T}(X,R)-P_Q(X)+\beta_Q+G(X,1),
 \quad \beta_Q=\tfrac23Q^{-3/2},
 \tag{20, E03 target}
\]
where \({\cal T}\) bounds the absolute omitted logarithmic tail and
\(\delta\) pays the full compact source, radial and eventual arithmetic
errors. The fixed [E03 request](../research-progress/handoffs/09_TND_OG_E03_SIGNED_LOG_ACQUISITION_REQUEST_20261108.md)
specifies the proposed tail constant, segment sum, source multiplier,
rounding extension and ordered limits.

Its quantitative completion test is
\[
 0\le U_{R,Q,\delta}(X)-J_0^{\rm G}(X)
 \le {\cal E}_{X,R}(\delta)+2{\cal T}(X,R)+2\beta_Q,
 \tag{21, E03 target}
\]
with the right side tending to zero by finite ordered choices for
each tuple (X,d,r). The two factors of two are intentional: an upper
tail allowance replaces a signed tail, and an upper prime allowance
replaces a signed truncation error.

**B02 stops here, at the concrete E contract.** Equations (20)–(21)
are not promoted to an assembled canonical theorem in this note.
Even after E03, exclusion requires an independently established
\[
 U_{R,Q,\delta}(X)+\text{certified evaluation error}
 <m(d,r)=\frac{\sin(\pi/8)d}{\cosh(\pi r/8)}.
 \tag{22, unpaid}
\]
Error tending to zero does not make the unknown value small. No
all-center, defect-conditioned, unbounded-height smallness or exclusion
is supplied. No numerical certificate has been run.

## 5. Controls and scope

The analytical premise screen uses
[result index](../../../../../../result-summaries/README.md),
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).
It does not rerun old numerical certificates.

| Control or prior obstruction | Exact consequence for this route |
| --- | --- |
| Fixed-prime translated-source family of OG Note01 | Its common source bounds and O(eta) data with Theta(sqrt(eta)) Green response are compatible with a deteriorating sublinear error modulus. It lacks the literal xi/q-zeta identity used in (13)–(14). No theta-only Lipschitz claim is made. |
| Growing-prime Euler controls | Generic local lemma applies if its own anchor and growth are paid. The canonical arithmetic constants, unchanged conductor/residue and P in (2) cannot be assigned to the control. |
| Weighted squares, finite prefixes/tails and finite-prime orbits | Their matched finite data do not supply the complete normalized theta source and full reflection. A finite approximant here is only a measured approximation to that complete source, never a replacement physical source. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Local holomorphy and their named positivity/reflection properties may support the generic lemma. They do not supply the exact canonical F, safe Euler anchor or prime subtraction. |
| Atomic/finite-profile, RH-conditional endpoint and variable-readout controls | Only their actual local analytic data may be used; their missing full source/arithmetic/readout premises are not silently supplied. Added real multiple zeros are explicitly allowed by (6). |
| E02 short-polynomial quadratic residual floor | It concerns one bounded-complex polynomial per padded interval, fixed theta<1/2 and its sufficient quadratic residual. No such residual or small-mollifier premise is used here. |
| OC harmonic-baseline/full-disk absolute-log floor | The direct approximant can have zeros and its measured logarithmic integral is retained. No harmonic baseline is substituted or annihilated, and no area bound is read as a trace bound. |

The generic acquisition lemma does **not** reject a control containing
a genuine defect. A correctly assembled certificate for that control
would converge to its own positive J, with its own normalization and
errors. Naming absent canonical identities does not establish (22).
This is a method for retaining signed information already present in the
complete source, not an additional arithmetic sign theorem.

The [proof-author check](../reviews/02_TND_OG_B02_BOUNDARY_LOG_SELF_CHECK_20261108.md)
records the local proof checks and the explicit E03 boundary.
Follow [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [shared-premise05](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md).
No manuscript, numerics, sibling edit, commit or push is part of B02.
