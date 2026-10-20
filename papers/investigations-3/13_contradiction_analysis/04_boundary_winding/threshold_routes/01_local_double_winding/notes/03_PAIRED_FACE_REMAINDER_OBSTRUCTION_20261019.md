# BW-01: what paired time faces retain at a double event

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**; actual effort
**max**, verified from recorded turn metadata.

**Result: a scoped obstruction to the payment selected in [Contract 02][contract],
proved below and checked in a [same-assistant assessment][review].** Odd
time pairing cancels the even time terms, but its leading term is the
nonzero collision curvature. Complete absolute remainder bounds on a
shrinking parabolic rectangle recover winding -1; a consumer retaining
only those bounds cannot force winding zero. This closes that particular
attempt, not BW-01. No theta event, theta exclusion, new region, improved
Newman bound or computational advantage has been obtained.

The local degree theorem is [inherited][index], not a new result of this
note. The additions here are an explicit component error threshold, the
paid odd-face observation, and an information-class comparison explaining
why this proposed payment does not provide the desired contradiction.
No literature-priority claim is made. See the [result summaries][results],
[local-law cluster][laws], [control cluster][controls], and
[patterns to avoid][avoid], especially [target restatements][a01],
[scoped conclusions][a07] and [signed recombination][a12].

## 1. Explicit whole-boundary estimate

Use the source, parameters, orientation and D_r of Contract 02. Write
s=t-T, z=x-a and h2=Hxx(T,a). Suppose

\[
B_3\ge\sup_{D_R}|H_{xxx}|,\quad
B_4\ge\sup_{D_R}|H_{xxxx}|,\quad
k_j=B_j/|h_2|.
\]

The complete moments M3(T+R^2), M4(T+R^2) are valid choices. These
are upper bounds, not estimates of actual remainders. Taylor expansion
first in space at T and then in time gives

\[
\begin{aligned}
H(T+s,a+z)&=h_2(z^2/2-s)+R_0,\\
|R_0|&\le B_3(|z|^3/6+|sz|)+B_4s^2/2,\\
H_x(T+s,a+z)&=h_2z+R_1,\\
|R_1|&\le B_3(z^2/2+|s|).
\end{aligned} \tag{1}
\]

For the first line, H(T,a+z)=h2 z^2/2+O(B3 |z|^3/6),
Hxx(T,a+z)=h2+O(B3 |z|), and Htt=Hxxxx. For the second,
Hxt=-Hxxx. All paths stay in D_R. Thus (1) pays the entire
closed rectangle, including all corners and both spatial walls.

In the fixed scaled coordinates of Contract 02,

\[
F_r=(H/(h_2r^2),H_x/(h_2r)),\quad Q=(y^2/2-\tau,y),
\]
\[
|F_{r,0}-Q_0|\le e_0=\frac76 k_3r+\frac12 k_4r^2,\qquad
|F_{r,1}-Q_1|\le e_1=\frac32 k_3r. \tag{2}
\]

On the boundary of [-1,1]^2 the **exact** minimum of |Q| is 1.
On tau=1 its square is 1+y^4/4; on tau=-1 it is
1+2y^2+y^4/4; on y=+/-1 it is 1+(1/2-tau)^2.
The only zero of Q is the origin, with Jacobian determinant -1.
Consequently

\[
\eta=(e_0^2+e_1^2)^{1/2}<1
\quad\Longrightarrow\quad
\min_{\partial D_r}|F_r|\ge1-\eta>0,
\qquad W(D_r)=-1. \tag{3}
\]

Indeed every straight-line interpolation from Q to F_r stays nonzero
on the boundary. Both the source-coordinate change and the constant
target-coordinate change have positive determinant. This argument needs
no assumption that H itself is nonzero on the walls; that assumption
would actually fail for the quadratic control on this rectangle.

For any fixed hypothetical event the complete moments are finite, so
one can choose r small enough for (3). For example, with positive k3,k4,

\[
0<r\le\min\{R,(8k_3)^{-1},(8k_4)^{-1/2}\}
\]

gives e0<=5/24, e1<=3/16 and eta^2<=181/2304<1.
This is an event-dependent analytic radius; h2 has not been measured and
no uniform radius or numerical theta certificate follows. The existence
of such local negative degree was already known. Formula (2) specifies
what the selected estimating rule actually certifies.

## 2. The signed opposite-face observation

Keep the entire source sum inside the pair before taking any norm. For
s>0 and |z|<=r,

\[
A_s(z)=-\int_0^\infty e^{Tu^2}\Phi(u)
 \frac{\sinh(su^2)}s\cos((a+z)u)\,du.
\]

Since 0<=sinh(v)-v<=v^3 e^v/6 for v>=0,

\[
|A_s(z)-H_{xx}(T,a+z)|\le \frac{s^2}{6}M_6(T+s). \tag{4}
\]

The exponential in the remainder is included in M6(T+s). This is also
the central-time-difference remainder obtained from Httt=-Hxxxxxx;
it is not a new arithmetic sign theorem. With s=r^2,

\[
\left|\frac{A_{r^2}(z)}{h_2}-1\right|
\le k_3r+\frac{r^4M_6(T+R^2)}{6|h_2|}. \tag{5}
\]

Thus sufficiently accurate pairing fixes the normalized odd difference
near **+1**, the value required by the ordinary collision model. The
even time terms really do cancel, improving this particular remainder's
order. It does not change the degree or produce the contrary sign.
Equation (5) alone is not a boundary certificate: (1)--(3) pay the
spatial walls and the rest of both time faces as well.

The cancellation H(T,a)=Hx(T,a)=0 used in (1) belongs to the **complete**
field. It is not valid to set the retained n<=4 contributions individually
to zero. Neither the finite head nor its tail separately satisfies the
event equations.

## 3. Complete source and numerical error ledger

The source normalization agrees with [Polymath, equations (3)--(4)][polymath]
and the repository [predecessor][predecessor]. For u>=0 every theta mode
phi_n is positive. The moment choices therefore bound each physical
spatial derivative without differentiating an error allowance.

For the frozen N=4, U=1 split, an explicit complete enclosure can use
the following adaptation of the [existing tail proof][walls]. Put
alpha_n=pi n^2, b=T+R^2<1 and

\[
\mathcal B_N=
\frac{4\pi(N+1)^2e^{-\pi(N+1)^2}}
 {1-4e^{-\pi(2N+3)}}.
\]

For every j=0,...,6 the omitted modes on [0,1] contribute at most
e^b B_N/8. This follows from u^j<=1, e^(b u^2)<=e^b and
integral(phi_n)<(4 alpha_n-1)e^(-alpha_n)/8, followed by the
displayed geometric majorant.

For u>=1 use u^j<=exp(j(u-1)). The exponent
b u^2+(9+j)u-j-alpha_n exp(4u) is strictly concave there, and its
tangent at one has negative slope. Hence the **all-mode** exterior is
at most

\[
\mathcal T_6(b)=
\frac{2\pi^2 e^{b+9-\pi e^4}}
 {(4\pi e^4-15-2b)(1-16e^{-3\pi e^4})}. \tag{6}
\]

Both denominators are positive for b<1. For successive mode majorants
the denominator ratio is at most one, the n^4 ratio at most 16, and the
exponential ratio at most exp(-3 pi e^4). Using j=6 gives a common
allowance for all required orders. The low-source omitted-mode integral
and the all-mode exterior are disjoint and exhaust the missing source.

A retained signed integral or moment upper enclosure must therefore add

\[
\delta_j^{\rm quad}+e^b\mathcal B_4/8+\mathcal T_6(b) \tag{7}
\]

to its outward finite-integral result. Quadrature error includes rounding.
No actual value of delta_quad, acquired h2, or theta boundary margin is
reported here: there was **no theta quadrature run**. Equations (6)--(7)
specify complete admissible payments; the proof above instead uses the
exact finite moments directly. There is no RS edge correction, contour
shift, cutoff crossing or parameter interpolation hidden in this real
integral calculation.

If separately acquired physical boundary values have complete component
allowances delta0,delta1, their scaled allowance is

\[
\eta_{\rm eval}=
\sqrt{\left(\frac{\delta_0}{|h_2|r^2}\right)^2+
       \left(\frac{\delta_1}{|h_2|r}\right)^2}. \tag{8}
\]

It must be added where such numerical enclosures are actually used.
Fixed nonzero assigned allowances worsen as r shrinks. In particular,
making eta_eval<1 requires r^2>delta0/|h2| and r>delta1/|h2|
when those allowances are nonzero. This is a condition on that payment,
not a lower bound on the true numerical error. Reacquisition or correlated
remainders can change it.

If h2 is replaced by a nonzero approximation hhat2 with certified
|h2-hhat2|<=d2, the errors about Q acquire, respectively,
3d2/(2|hhat2|) and d2/|hhat2|, in addition to (1) divided by
|hhat2|r^2 and |hhat2|r. A numerical sign/scale claim needs a certified
nonzero denominator. If T or a is enclosed rather than exact, its full
parameter variation is also owed. Those acquisition tasks remain unperformed.

## 4. Matched direct comparison and the precise stopping scope

Consider a boundary consumer that retains only Q and the nonnegative
component bounds |F0-Q0|<=e0, |F1-Q1|<=e1. This information class
contains Q itself for **every** e0,e1>=0. A conclusion justified for
every boundary curve allowed by those data cannot be W=0, since Q
has W=-1. When eta<1, the entire admitted class has degree -1.
For larger allowances this argument asserts no universal degree, but
the admitted Q still prevents a zero-degree conclusion.

The matched direct method receives the same centered quadratic model
and whole-rectangle remainder bounds. It also cannot exclude the center
zero: Q is an admissible interior field. Thus neither formulation yields
collision exclusion from this reduced information. This is a logical
comparison, not a runtime benchmark or a proof that direct methods are
always stronger.

The actual theta coefficient sequence is much more information than this
tube. The conclusion is specifically about a consumer that **discards**
its signed information after obtaining absolute remainder bounds. It does
not preclude an arithmetic proof that no genuine theta event can satisfy
the assumed cancellations, or a boundary argument using additional
coupled signed data. It also does not obstruct boundary certification on
an event-free region with an unresolved interior norm.

**Stop the centered quadratic model plus symmetric absolute-remainder
payment as a source of zero winding.** Merely shrinking its radius,
increasing its Taylor order or certifying its inherited negative degree
more accurately does not supply the missing incompatible arithmetic fact.

## 5. Controls and checkable numerical record

The [checker][checker] uses exact rational arithmetic and enclosures of
every complete boundary segment. Strict coordinate halfplanes transfer
degree to an exact polygon; no sampling-based winding is used. The
[receipt][receipt] includes input SHA-256 hashes and Git parent
b39c6cc9b4756bc14c2e500e327169db88571d1f. Those hashes identify sources,
not mathematical validity. The setup documents were uncommitted.

| Control | Observed exact interface outcome |
| --- | --- |
| Q0=y^2/2-tau and its derivative | Full boundary; winding -1; exclusion refused |
| Even quartic, T=1/4, a=1, r=1/8 | Full boundary; winding -1; exclusion refused |
| Negative of that quartic | Winding -1; multiplication of both components preserves degree |
| Constant 1 | Full boundary; winding zero; exclusion accepted |
| Quartic traversed backwards | Raw winding +1, corrected physical winding -1 |
| Quadratic event on the boundary | Inconclusive; no nonzero boundary certificate |
| Constant with uncertainty reaching zero | Inconclusive |
| Omitted spatial wall | Rejected as incomplete coverage |

For the quartic control the **own-source** derivative bounds are
h2=8, B3=27, B4=24 on the stated box. Formula (2) gives

\[
e_0=33/64,\quad e_1=81/128,\quad
\eta^2=10917/16384<(41/50)^2.
\]

The scaled boundary margin is therefore >9/50 and the physical first-jet
norm is >9/400 on that control's boundary. Its interior still contains
the double event. These are polynomial-control margins, **not theta
margins**. Its odd pair equals Hxx(T,a+z) exactly, because the sixth
spatial derivative is zero. Its all-real threshold and sharp mirror
equality are inherited from the predecessor; the PDE, event jets, pair
identity and mirror equality were checked exactly here.

The wider screens distinguish the hypotheses as follows.

| Family | Relevant shared input and failed theta premise |
| --- | --- |
| Quadratic/Hermite | Local heat geometry; no complete theta source. Higher-multiplicity Hermite events also fail h2!=0 and are outside this contract. |
| Even threshold quartic | Evenness, positive threshold, all-real forward evolution and mirror equality; no theta source or infinite arithmetic zero structure. |
| Positive-kernel q and q_(T,a) | Heat/positivity and threshold where established; no canonical theta coefficients. Their own moments must be used. |
| Weighted squares / finite-prime controls | Selected arithmetic structure and local events; full normalized reflection or complete coefficients fail. Their event times are not supplied as all-real thresholds. |
| Reflected smooth / positive-primitive controls | Reflection or auxiliary positivity; no complete normalized theta square expansion. No numerical event location is invented. |
| Euler modifications | Generic heat and functional identities, including positive thresholds in the known class; unchanged theta coefficients fail. |
| Smooth-density / two-channel positive constructions | Auxiliary positivity lacks the complete signed physical comparison; not asserted to be threshold controls. |

The non-polynomial rows are analytical premise screens based on the
[control summary][controls], not newly run source certificates. None
justifies substituting theta tails into an altered source.

## 6. What the next BW-01 attempt must change

BW-01 remains open. A continuation needs an independently estimated
**signed theta relation** excluded by the quadratic remainder tube,
or a declared computational problem where cheaper complete boundary
acquisition can beat the matched direct method. The odd-face observation
in (4), estimated only through M6, does neither. Before another numerical
campaign, specify the retained signed quantity and how it uses the exact
theta coefficients beyond the moment norms. The all-real threshold jet
constraints may be inputs, but their incompatible arithmetic bound is
still missing and belongs with the named BW-08/sibling consumer.

No claim covers multiplicity greater than two, uniformly small positive
T, unbounded a with a fixed numerical budget, or all possible simultaneous
threshold events. The conditional local estimate applies separately to
each ordinary event; it excludes none of them. No manuscript was created.

[contract]: 02_PAIRED_FACE_CONTRACT_20261019.md
[review]: ../reviews/01_PAIRED_FACE_SELF_REVIEW_20261019.md
[checker]: ../numerics/check_paired_face_contract.py
[receipt]: ../numerics/PAIRED_FACE_CONTROLS_20261019.json
[results]: ../../../../../../../result-summaries/README.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[index]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[walls]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[predecessor]: ../../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[polymath]: https://arxiv.org/html/1904.12438v2#S1
