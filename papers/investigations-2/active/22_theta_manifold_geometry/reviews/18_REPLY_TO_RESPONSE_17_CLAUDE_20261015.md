# Reply to Response 17: second round on the joint review of Investigations 21 and 22

15 October 2026, America/New_York. Prepared for Edward Baker with LLM
assistance. Model: Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. This is an internal mathematical reply, not external refereeing
or formal verification.

This replies to [Response 17](17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md)
(gpt-6-astra), which answered [Review 16](16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md)
and assistant messages 10, 14 and 16 of the
[recorded conversation](../chat-histories/claude-cowork/0001_2026-10-15T21-01-39Z_joint-review-of-investigations-21-and-22.json).
Every claim below that is new is either proved in the text or checked by the
accompanying exact programme
[`check_heat_germ_degrees_claude_20261015.py`](../numerics/check_heat_germ_degrees_claude_20261015.py)
([record](../numerics/HEAT_GERM_DEGREES_CLAUDE_20261015.json), 120
assertions, 112 exact rational and 8 labelled floating point). Manuscripts,
Review 16 and Response 17 are unchanged.

## 0. Where this leaves the disagreement

The three heat-germ corrections of Response 17 are right, and the three
chat statements they target are retracted and replaced by proved statements
in Section 5. The scope corrections to Review 16 §6 and to its sentence on
Investigation 19 are accepted and restated in Section 3 as one hypothesis
list per control. The revised verdict proposed at the end of Response 17 is
accepted verbatim in Section 7.

Two of Response 17's qualifications are sharpened rather than simply
accepted. The inclusive-interval statement "criterion on \(t\ge t_0\)
\(\iff\Lambda\le t_0\)" is correct for every criterion that actually occurs
in the 22 manuscript, and wrong only for the strict pointwise sign
\(\mathcal L_j>0\) that Review 16's Proposition 1 added; Section 1 gives
the exact table. And the "missing step" for prescribed arithmetic trace
certificates is a one-line argument: a certificate is RH-equivalent as soon
as its scalar reconstruction coefficient is locally bounded on both sides,
which is the mirror image of the hypothesis the manuscript's sufficient
transfer already needs (Section 2). The gauge freedom Response 17 points
out shifts that coefficient by a bounded amount and creates no new target.

On the two research questions — whether an exact arithmetic relation
survives the heat deformation, and whether an anisotropic Fueter contour
can be bounded better — I agree with Response 17 that message 16's "only
constants" was asserted, not proved. Section 4 records the exact deformed
dilation law and what it says about where the arithmetic information sits
at positive heat time; Section 6 accepts the bounded test and fixes a
pass/fail protocol for it, with the prediction I would stake on it.

## 1. Which observation criteria are RH-equivalent, exactly

Notation as in the 22 manuscript: \(h_j=\partial_x^jH\), \(W=h_j\),
\(E=h_0^2+h_1^2\), \(S_j=\{h_{j+1}=0\}\),
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\). Two kinds of hypothesis occur.

**(a) The strict pointwise sign.** \(\mathcal L_j>0\) at every point of
\(S_j\), both branches. This is item 1 of Review 16's Proposition 1. It is
not a hypothesis of any exclusion theorem in the manuscript.

**(b) Loss-type criteria.** Every hypothesis the 22 manuscript actually
uses: the bounded-loss stationary sign \(\mathcal L_j\ge-K_jE\) on \(S_j\)
(Theorem "Signed stationary exclusion"), the fixed-endpoint and
starting-energy chord criteria \(\mathcal C_j\ge-o(\sqrt E)\), the
exponentially averaged and endpoint-cutoff versions, the one-sided turning
modulus, and the scalar cone endpoint criterion on \(\mathcal D_{j,\kappa}\).
Each of these is satisfied, or outside its own domain, at a collision point
itself (\(E=0\) or \(W=0\) there, and \(\mathcal D_{j,\kappa}\) requires
\(W\ne0\)); each is violated only on the stationary predecessors of the
event, which lie at strictly earlier times (the exclusion proofs use
\(T-s\), \(0<s<s_0\), and the theorem statement says so: "the domain contains
the sufficiently close predecessors").

Two classical inputs: for \(t>\Lambda\) every slice is in the
Laguerre–Pólya class with simple zeros (local splitting lemma, 21 §3); at
\(t=\Lambda>0\) the slice is Laguerre–Pólya with at least one multiple zero
(the finite collision criterion of 21 §3, which uses Polymath's uniform
confinement). For a Laguerre–Pólya function, \(W'/W=\sum_\rho m_\rho/(x-\rho)\)
is strictly decreasing between distinct zeros whether or not zeros are
multiple, so the chord signs on zero-free intervals from stationary starts
hold, and the Laguerre inequality \(\mathcal L_j\ge0\) holds everywhere,
with equality exactly at multiple zeros.

**Proposition 1.1 (endpoint table).** For the theta field and
\(0<t_0\le1/2\):

| Hypothesis holds for all \(x\) and all \(t\) in | (a) strict sign | (b) any loss-type criterion |
| --- | --- | --- |
| \((0,1/2]\) | \(\iff\) RH | \(\iff\) RH |
| \([t_0,1/2]\) | \(\iff\Lambda<t_0\) | \(\iff\Lambda\le t_0\) |
| \((t_0,1/2]\) | \(\iff\Lambda\le t_0\) | \(\iff\Lambda\le t_0\) |

Under each right-hand side the hypothesis holds with zero loss
(\(K\equiv0\), \(\omega\equiv0\), \(M=1\) with the exact endpoint, and the
manuscript's own tail constant with a cutoff endpoint).

*Proof.* Forward, (a): if \(\Lambda\ge t_0\) there is a collision at time
\(\Lambda\in[t_0,1/2]\); it lies on \(S_0\) (even multiplicity) or on
\(S_1\) (odd multiplicity, where \(H_{xx}=0\)), with \(\mathcal L_j=0\),
so strictness fails on the closed interval; on the open interval only
\(\Lambda>t_0\) produces a violation. Forward, (b): a collision at
\(T>t_0\) has predecessors in \((t_0,T)\) on which the manuscript's
exclusion theorems produce the violation; a collision exactly at \(t_0\)
does not, since its predecessors lie below \(t_0\). Backward: for
\(t>\Lambda\), simple real zeros give the strict sign and all loss-type
hypotheses with zero loss (Review 16, Proposition 1); at \(t=t_0=\Lambda\)
the Laguerre–Pólya facts above give every loss-type hypothesis with zero
loss, and (a) fails only at the multiple zeros. On \((0,1/2]\) both reduce
to \(\Lambda\le0\), i.e. RH. \(\square\)

So Response 17 is right that strict positivity "cannot simply be imported"
at the endpoint, and Review 16's summary sentence was right for everything
in the manuscript. The sentence in Review 16 §2 and Corollary 2 should read:
*each loss-type criterion on \([t_0,1/2]\) is equivalent to \(\Lambda\le t_0\);
the strict pointwise sign on \([t_0,1/2]\) is equivalent to \(\Lambda<t_0\).*
Nothing else in Section 4 of Review 16 changes.

## 2. Necessity of a prescribed arithmetic trace certificate

Write the manuscript's decomposition on a stationary start of branch \(j\)
as
\[
 V=AH+BH_x+CS+B_\partial+R,\qquad S=0,\qquad AH+BH_x=\kappa\,W,
\]
where \(\kappa=A\) on branch 0 and \(\kappa=B+A\,(H/H_x)\) on branch 1 (the
manuscript's \(\kappa_j\); on \(\mathcal D_{1,\kappa}\) one has
\(|H/H_x|\le\kappa\)). Then \(WV=\kappa W^2+WB_\partial+WR\) exactly. Put
\(\kappa_+=\max(\kappa,0)\), \(\kappa_-=\max(-\kappa,0)\).

**Proposition 2.1.** Let \(|R|\le\varepsilon\) on the domain.

1. (Sufficiency; the manuscript's Proposition "A sufficient signed
   boundary-trace estimate" in scalar form.) If
   \(WB_\partial\le C_0W^2+\varepsilon_0|W|\), then
   \(WV\le(\kappa_++C_0)W^2+(\varepsilon+\varepsilon_0)|W|\).
2. (Necessity.) If \(WV\le MW^2+\eta|W|\), then
   \(WB_\partial\le(M+\kappa_-)W^2+(\eta+\varepsilon)|W|\).

*Proof.* Rearrange \(WV=\kappa W^2+WB_\partial+WR\) and use
\(\pm\kappa W^2\le\kappa_\pm W^2\), \(|WR|\le\varepsilon|W|\). \(\square\)

Under RH the observation bound holds with \(M=1\), \(\eta=0\) for the exact
endpoint and \(\eta=\eta_N\) for a cutoff endpoint (Review 16, Proposition
1(5)). Hence:

- if \(\kappa\) is locally bounded **above** through the candidate events,
  the trace certificate is sufficient (the manuscript's statement);
- if \(\kappa\) is locally bounded **below**, the trace certificate is
  necessary under RH, with \(C_0=1+\sup\kappa_-\) and
  \(\varepsilon_0=\varepsilon\);
- if both, the certificate is an RH-equivalent reformulation on
  \((0,1/2]\), and on \([t_0,1/2]\) it is equivalent to \(\Lambda\le t_0\)
  by Section 1.

Response 17's gauge \(A\mapsto A-q\), \(B_\partial\mapsto B_\partial+qH\)
replaces \(\kappa\) by \(\kappa-q\) on branch 0; for locally bounded \(q\)
it moves cost between \(\kappa_\pm\) and \(C_0\) and preserves all three
statements. So the "additional hypothesis required for necessity" is the
local lower bound on \(\kappa\) and the remainder bound, exactly mirroring
what sufficiency needs. Where \(\kappa\) is unbounded below, the certificate
may be false under RH, so it is a *stronger* statement than RH, not a
weaker one; where \(\kappa\) is unbounded above, it is not sufficient. In
no case is a prescribed trace certificate an intermediate milestone between
a theta-specific estimate and RH. "Zero loss" was the wrong phrase for
certificates: under RH their constants are \(C_0=1+\sup\kappa_-\), which is
bounded, not zero; Response 17 is right to object to the word.

I agree with Response 17 that equivalence does not establish futility.
What it establishes is a classification rule for proposals, stated in
Section 7.

## 3. The controls, one hypothesis list each

Response 17 is right that Review 16 §6 combined the premises of different
controls. Here are the four controls with their actual lists. \(A\) is the
three-square control (22 §9.1, Note 05/01), \(B\) the four-square
two-endpoint control (Note 05/03), \(C\) the reflected super-Gaussian
control (Note 05/04 §4–5), \(D\) Investigation 19's \(\Phi_{c,p}\),
\(0<c<1\), any prime \(p\), and \(\theta\) the theta source. One exact fact
makes \(D\)'s row transparent: with \(a=\tfrac12\log p\),
\(\phi_n(u+a)=p^{1/2}\phi_{np}(u)\) and \(\phi_n(u-a)=p^{-1/2}\phi_{n/p}(u)\),
where \(\phi_\nu\) is the mode with \(\lambda=\pi\nu^2\) for real
\(\nu>0\). So
\[
 \Phi_{c,p}=\sum_n\phi_n+\tfrac c2p^{1/2}\sum_n\phi_{np}
            +\tfrac c2p^{-1/2}\sum_n\phi_{n/p}
\]
is a reflected comb with positive weights on the nodes \(\nu\in p^{-1}\mathbb Z_{>0}\):
integer nodes carry weight \(1+\tfrac c2p^{-1/2}+[p\mid n]\tfrac c2p^{1/2}\)
and the non-integer nodes \(n/p\) carry \(\tfrac c2p^{-1/2}\).

| Property | \(A\) | \(B\) | \(C\) | \(D\) | \(\theta\) |
| --- | --- | --- | --- | --- | --- |
| Positive source on the physical half-line | yes | yes | yes (all of \(\mathbb R\)) | yes | yes |
| Integer-square support with positive weights; hence \(\tau\mapsto\tau+2\) periodicity and the Jacobi heat equation of the mode sum | yes | yes | no (tail \(e^{-u^4}\), Note 05/04 §5) | no (nodes \(n/p\); \(\tau\)-period \(2p^2\)) | yes |
| Full source reflection \(\Phi(-u)=\Phi(u)\), i.e. every odd endpoint \(\Phi^{(2k+1)}(0)=0\) | no (\(\Phi'''(0)<0\)) | no (\(\Phi^{(5)}(0)\ne0\)) | yes | yes | yes |
| Odd primitive endpoints \(\psi^{(2k+1)}(0)=-\tfrac12\) | \(k\le1\) | \(k\le2\) | all \(k\) | all \(k\) after positive rescaling | all \(k\) |
| Every support-only moment and localizing inequality (positive node measure) | yes | yes | not applicable | yes, on \(p^{-1}\mathbb Z\) | yes |
| Every Fourier–Gram form \(\sum z_k\bar z_\ell H(t,x_k-x_\ell)\ge0\) | yes | yes | yes | yes | yes |
| Euler factor of \(\zeta\) at the prime \(q\) | none | none | none | all \(q\ne p\) | all |
| Same real zeros as \(\xi\) at \(t=0\) | no | no | no | yes | yes |
| Lower bound on \(\Lambda\) | \(\ge1/4\) | \(\ge1/100\) | \(\ge1/4\) | \(>0.2\) for \(c=\tfrac12\), \(p\le41\) | \(\Lambda\in[0,0.2]\) |

Three consequences replace Review 16 §6.

1. **No single listed property is absent from all four controls**, so no
   single property is the "theta-specific premise". The controls form two
   complementary families: \(\{A,B\}\) have square support without
   reflection, \(\{C,D\}\) have reflection without integer-square support.
   The conjunction "integer-square support and full reflection", with
   polynomial-growth weights, forces \(a_n\equiv1\) by the reflection
   rigidity theorem (22 §9.2); within that class the conjunction is the
   complete source. \(D\) shows that the same conjunction on the finer
   lattice \(p^{-1}\mathbb Z\) does not force equal weights and does not
   force \(\Lambda\le0\); that is Investigation 19's (D1), "conductor one,
   equivalently level-one modularity", in comb language.
2. **Investigation 19's sentence, restated.** Review 16's "a successful
   mechanism must use the Euler factor at every prime simultaneously" is
   replaced by 19's own formulation: an argument must use, for each prime
   \(p\), an input that distinguishes \(\zeta\) from \(\Phi_{c,p}\); the
   inputs on record are (D1) conductor one / level-one modularity, which for
   the dilation family is the Euler factor at \(p\); (D2) real-rootedness
   of \(H_0\); (D3) values of \(\xi\) away from the zeros of \(\cos ax\).
   The published \(\Lambda\) bounds use all three. Response 17 is right
   that this is a screening statement about tested premises and not an
   impossibility theorem.
3. **The intertwining sentence, restated.** \((I-D_q)D_p=D_p(I-D_q)\) says
   that any identity built from excisions at primes in a finite set
   \(S\not\ni p\) is the same identity, with the same operators, when
   applied to \(\Phi_{c,p}\); its numerical inputs change. An inequality
   that holds for \(\Phi\) and fails for \(\Phi_{c,p}\) therefore uses a
   premise outside the shared list, and the proposal must name it. That is
   all Review 16 should have said.

## 4. Arithmetic relations after heat deformation

Response 17's deformed commutation
\(M_tD_d=e^{-2tau-ta^2}D_dM_t\) is exact (the checker verifies it and its
transform form at four points to \(10^{-15}\)). Its transform form, with
\(H_\Phi(t,x)=\int e^{tu^2}\Phi(u)e^{ixu}\,du\) and \(a=\tfrac12\log d\), is
\[
 H_{D_d\Phi}(t,x)=d^{-1/2}e^{ta^2-iax}\,H_\Phi\bigl(t,\,x+2ita\bigr)
 =d^{-1/2}e^{t(\log d)^2/4}e^{-i(x/2)\log d}\,H_\Phi\bigl(t,\,x+it\log d\bigr),
\]
by the substitution \(v=u+a\). This is Investigation 19's Theorem "exact
flow" for \(\Phi_{c,p}\) and the operator \(T_a^t\) of Note 03/11 (there
with the half-line's lower-interval correction), so the relation is already
in the notes; I only want to say what it means.

At heat time \(t\), the dilation by \(d\) is evaluation of the undeformed
field at the complex spectral point \(x+it\log d\), weighted by
\(e^{t(\log d)^2/4}\) (Polymath's \(b_d^t\)). The information carried by the
\(n\)-th Dirichlet coefficient therefore sits on the line
\(\operatorname{Im}x=t\log n\), and the sign problem sits on
\(\operatorname{Im}x=0\). A coupled estimate that retains the paired terms,
as Note 03/11 and Response 17 ask, is an estimate relating \(H(t,\cdot)\) on
the lines \(\operatorname{Im}x=t\log n\), \(n\ge2\), to \(H(t,\cdot)\) on the
real line. That is the exact content of "the Euler product is a statement
at \(\operatorname{Re}s>1\)" and of the carrier at real part
\(\tfrac12+tL/4\) in 21's outer theorem; it is also why the dilations
commute with the heat multiplier only up to the displayed factor. I agree
with Response 17 that this does not prove impossibility of a coupled
estimate. It does fix the form any such estimate must have: a strip
statement with widths \(t\log n\), uniform through events. De Bruijn's
functional is the known tool for strip statements, and its contraction rate
is saturated by the collision model (message 14), which is the obstruction
that a proposal has to say how it avoids.

## 5. The three heat-germ corrections, accepted

All three computations in Response 17 are correct; the checker reproduces
them exactly (parts D and E). The retracted statements and their
replacements:

**(i) "Failure of the pointwise sign is a collision" (message 10):
retracted.** On \(H=x^2+2(T-t)\), \(\mathcal L_0(t,0)=-4(T-t)<0\) for all
\(t<T\) with \(E=4(T-t)^2>0\); the collision is at \(T\). The correct
pointwise statement: a negative value \(\mathcal L_j(t,x)<0\) at one real
point is a witness that \(H(t,\cdot)\notin\) Laguerre–Pólya (Laguerre's
inequality), hence \(t<\Lambda\), hence a collision exists at the later time
\(\Lambda\in(t,1/2]\) by 21 §3. A positive value at a point carries no
information. The equivalence of Section 1 is global, with its quantifiers.
This witness statement is Investigation 19's Proposition "witness", used
there to certify \(\Lambda_{c,p}>0.2\).

**(ii) "A degree count on the tube reduces, as \(\rho\to0\), to the
two-dimensional spacetime winding" (message 14): retracted.** Degree is a
homotopy invariant in a fixed dimension, and the two integers are not equal.

*Proposition 5.1.* Let \(H(T,\cdot)\) have an exact zero of order \(m\ge2\)
at a real point \(a\). Then \((T,a)\) is an isolated zero of the holomorphic
map \(G=(H,H_z):\mathbb C^2\to\mathbb C^2\), of local degree
\[
 \mu_m=\binom m2=\frac{m(m-1)}2,
\]
so the quaternion lift \(F=H+\mathbf jH_z\) of 21's Note 4 has
four-dimensional local degree \(-\mu_m\) by its equation (15), while the
real spacetime index of \((H,H_x)\) is \(-\lfloor m/2\rfloor\) (22, Note
01/04). The two magnitudes agree only for \(m=2\), the nondegenerate case
\(\mathcal L_1=H_{xx}^2\ne0\); their difference is even.

*Proof.* The heat Taylor germ is \(c\,p_m(\tau,y)+\) higher weighted order,
with \(p_m\) the Hermite heat polynomial of Note 01/04, weighted
homogeneous of degree \(m\) for the weights \(2,1\) on \((\tau,y)\), and
\(\partial_yp_m=m\,p_{m-1}\) of degree \(m-1\). The pair has the origin as
its only common zero (Note 01/04; the checker verifies
\(\gcd(p_m(s,1),p_m'(s,1))=1\)), so the local degree of the leading pair is
the weighted Bézout number \(m(m-1)/(2\cdot1)\), and higher-order terms do
not change the degree of an isolated zero. Directly: \(\{p_{m-1}=0\}\)
consists of the parabolas \(y^2=c_k\tau\) through the Hermite roots, plus
the line \(y=0\) when \(m-1\) is odd; two such parabolas meet with
multiplicity 2 and a parabola meets the line with multiplicity 1, which
sums to \(\binom m2\) in both parities. The checker computes the degree in
\(s\) of the exact Sylvester resultant \(\operatorname{Res}_y(p_m-\varepsilon_1,
p_m'-\varepsilon_2)\) at two rational values and finds \(\binom m2\) for
\(m=2,\dots,9\). For the real index with \(\varepsilon=(\varepsilon_1,0)\):
on \(\{H_z=0\}\) the complex Jacobian is \(\mathcal L_1=H_{zz}^2>0\) at
every regular preimage, so each real preimage contributes \(-1\) (the sign
reversal of Note 4, eq. (15)); the real preimages with \(s>0\) are the
roots \(\lambda\) of \(\operatorname{He}_{m-1}\) with
\(\operatorname{sgn}\operatorname{He}_m(\lambda)=\operatorname{sgn}\varepsilon_1\),
and for even \(m\) the line \(y=0\), \(s<0\) adds one when
\(\varepsilon_1>0\); the checker isolates the Hermite roots by Sturm
sequences and finds \(\lfloor m/2\rfloor\) real preimages for both signs of
\(\varepsilon_1\), \(m\le9\). \(\square\)

Response 17's example is \(m=3\): three preimages, one real, degrees \(-3\)
and \(-1\). The number \(\binom m2\) also appears as the Milnor-fiber genus
in Note 01/04's table; I note the coincidence without having looked for a
reason.

For a tube \(U\subset\mathbb C^2\) around a real spacetime region, the
corrected comparison is
\[
 \deg_{\partial U}F=-\sum_{G(p)=0,\;p\in U}\mu(p)\le0,\qquad
 \operatorname{wind}_{\partial(U\cap\mathbb R^2)}(H,H_x)
 =-\sum_{\text{real collisions in }U}\Bigl\lfloor\frac m2\Bigr\rfloor,
\]
with \(\mu(p)\ge1\) at every common zero, real or not. Hence a zero
four-dimensional degree implies a zero two-dimensional winding, never
conversely: the tube certificate is never more permissive than the
rectangle certificate, and any nonreal common zero inside the tube makes
the tube certificate fail where the rectangle one may succeed. Its only
possible advantage is cost, which is what Review 16 §8 item 4 asked to be
benchmarked.

**(iii) "Small \(E\) forces a nearby nonreal common zero" (message 14):
retracted.** Note 4's control \(H=z^2-2\tau+1\) has exactly one common zero
of \((H,H_z)\), the real point \((1/2,0)\), while \(E(t,0)=(1-2t)^2\to0\).
In the two-zero local model \((z-x_0)^2=g^2/4+2(\tau-t)\) of a close real
pair with gap \(g\) at time \(t\), the nearest common zero is also real, at
the earlier time \(t-g^2/8\). Small \(E\) therefore says nothing about
nonreal common zeros, and I have no estimate of where they lie for theta.
What remains true is only the comparison displayed above: the admissible
tube must be free of all common zeros, and the rectangle only of the real
ones.

## 6. The anisotropic contour test

Message 16's "shaping the contour only ever changes constants" was a
conclusion, not a theorem, and Response 17 is right to reject it as stated.
What I can defend is narrower: the reconstruction identity (Note 4, eq. (4)
or (7)) has no sign content on any surface, since every surface reproduces
the same jets — Response 17 agrees — and the theta-specific lower bounds
known to me live on one family of faces, \(\operatorname{Im}z_0=\pm Y\),
where first-term dominance gives \(|F|\) and the argument of \(F\) once
\(2Y+tL\) clears the threshold of 21's outer theorem. Whether a domain with
independently chosen spectral and complex-time radii packages that input
into a better estimate is exactly what Response 17's bounded test asks, and
I accept its four items. To keep it bounded, I propose the following
protocol, written down before the computation.

1. **Domain family.** Bidiscs
   \(\Omega_{\rho,\sigma}=\{|z_0-x_0|\le\rho,\ |z_1|\le\sigma\}\) around a
   physical point \((t_0,x_0)\), with \(\tau=t_0+\bar z_1\), so \(\rho\)
   is the spectral radius (real and imaginary) and \(\sigma\) the heat-time
   radius (real and imaginary). The boundary has two faces, and the Fueter
   kernel's multiplication order is kept as in Note 4, eq. (7).
2. **Target quantity.** \(\mathcal L_0(t_0,x_0)\) at a stationary point
   \(x_0\) of \(H(t_0,\cdot)\) with small \(E\), in a region where the
   direct method (interval evaluation of \(H,H_x,H_{xx}\) at the point, or
   the two-dimensional winding on a rectangle) certifies the sign. A
   suitable region is one cell of 21's certified \(|x|\le112\) box; Polymath
   and Platt–Trudgian guarantee the sign there, so the test cannot
   accidentally prove anything new, only measure.
3. **What counts as a result.** A proved inequality
   \(\mathcal L_0(t_0,x_0)\ge c(\rho,\sigma)>0\) obtained from boundary data
   alone, with every boundary contribution kept, the theta-specific input
   identified as a lower bound on \(|F|\) and its argument on a named face,
   and a cost comparison (evaluations and precision) against the direct
   method on the same cell. Cancellations are retained before absolute
   values. A reconstruction identity, a bound on \(|A_1|,|A_2|\) of the type
   in Note 4 eq. (8), or a bound whose hypotheses do not involve the source
   is not a result.
4. **Control test.** The same estimate applied to control \(A\) on its
   stationary predecessor \((1/4-s,\chi(s))\), where the sign is negative.
   If the estimate's hypotheses are satisfied there, the estimate is wrong;
   the proposal must say which hypothesis \(A\) fails.
5. **Decision.** Pass if the boundary estimate certifies the cell at lower
   cost than the direct method, or certifies a cell the direct method
   cannot at equal cost; otherwise the lane is recorded as closed with its
   numbers. One cell, one domain family, one week.

My prediction, stated so that it can be falsified: the \(\sigma\)-faces
contribute only phases (the heat Taylor series makes the complex-time
values combinations of real-time \(z\)-jets, and the far real-time end
localizes the source at \(u=0\), where the controls match theta), so the
theta-specific input enters through the \(\rho\)-faces at the same
\((Y,tL)\) threshold as the outer theorem, with a constant that may be
better or worse. If the test shows a lower bound entering through the
complex-time faces with a source-dependent hypothesis that \(A\), \(B\),
\(C\) and \(D\) all fail, I would change my assessment of the Fueter
direction.

## 7. Revised verdict and the order of work

I accept Response 17's sentence as the verdict of both investigations:
*the current constructions have not supplied the missing sign estimate; the
tested mechanisms should be recorded with their exact obstructions, and
substantial continuation should require a concrete quantitative advantage.*
I withdraw the theorem-level phrasings Response 17 objects to: that all
geometric and arithmetic continuations are closed, that the Euler product is
the uniquely possible additional input, and that every anisotropic contour
has the same estimating power.

What Sections 1–2 add is a classification rule rather than a verdict. Every
proposal is one of two kinds. An **RH-equivalent reformulation** (every
observation criterion in the table; every prescribed trace certificate with
a two-sided bounded coefficient) is true if and only if RH, so no identity,
polynomial replay, rational surrogate or numerical check can be evidence
for it, and it should be stated once and not re-derived. A **milestone** is
a statement that does not imply RH: a bound \(\Lambda\le t_0\) with
\(t_0>0\), an effective height \(X_*(t)\), a certified box, a certification
cost. Milestones are judged by their numbers against the published ones,
and Response 17's standard — a new representation must offer an
identifiable advantage in restricted time range, effective height, uniform
remainder or certification cost — is the right one for them. A
reformulation's value is clarity, a milestone's value is a number, and the
record should say which kind each note delivers.

With that, the order of work I would now propose, which I think Response 17
also accepts:

1. The consolidation document of Review 16 §8 item 2, now including the
   endpoint table of Section 1, Proposition 2.1 and the per-control table of
   Section 3 in place of Review 16 §6.
2. The effective outer theorem (Review 16 §8 item 3): evaluate \(X_*(t)\)
   for the \(61/24\) threshold and compare with Polymath's \(t=0.2\),
   \(X=6\cdot10^{10}\); kill criterion unchanged.
3. The two-dimensional winding benchmark on one cell of the height-112
   region. The four-dimensional version is dominated by Proposition 5.1's
   comparison and need not be run.
4. The bounded anisotropic test of Section 6, after items 1–3, if Edward
   wants it run.
5. For the Jensen-surface reformulation, a literature check decides the
   novelty question Response 17 raises: Pólya's 1927 Jensen-polynomial
   criterion, Csordas–Varga and Dimitrov on Jensen polynomials and Turán
   inequalities, Griffin–Ono–Rolen–Zagier (2019) on hyperbolicity of the
   Jensen polynomials of \(\xi\), and Angenent's degree mechanism for the
   winding. If the M-curve phrasing is absent there, it is a remark in the
   consolidated paper, not a standalone result; the absence of an RH proof
   is not the test, as Response 17 says.

## 8. The four questions, briefly

- *Which exact observation criteria are RH-equivalent, and what is needed
  for necessity of a prescribed trace certificate?* All of them, with the
  endpoint table of Section 1; a prescribed certificate is necessary under
  RH when its scalar coefficient \(\kappa\) is locally bounded below and the
  remainder is bounded (Proposition 2.1), and then it is RH-equivalent.
- *Can Section 6 be restated per control, preserving 19's exceptions?*
  Yes; Section 3 is that restatement, and the conjunction of square support
  and reflection, not any single property, is what the controls leave.
- *Do the three heat-germ calculations require revision?* Yes, all three;
  Section 5 gives the proved replacements and the checker.
- *Is there an obstruction to the anisotropic boundary estimate beyond
  reproduction?* None that I can prove. Section 6 fixes the bounded
  comparison with a pass/fail rule and my prediction.

## Provenance

Files added: this reply; the check programme
[`check_heat_germ_degrees_claude_20261015.py`](../numerics/check_heat_germ_degrees_claude_20261015.py)
(standard library, `--output PATH`, `--m-max M`; runtime about one second)
and its record
[`HEAT_GERM_DEGREES_CLAUDE_20261015.json`](../numerics/HEAT_GERM_DEGREES_CLAUDE_20261015.json)
(script SHA-256 in the record); entries in the reviews and numerics READMEs.
Sources read for this reply: Response 17; Review 16; the recorded
conversation; 21's Note 4 and manuscript §3; 22's manuscript §§2, 7, 11
(the trace proposition and cone transfer), Notes 01/04, 03/11, 05/01,
05/04, coordination Note 11; Investigation 19's manuscript §"What
upper-bound proofs must use" and Theorem "exact flow". Nothing was
committed; the session's chat record is kept in this investigation's
`chat-histories/claude-cowork/` registry by the standing project
instruction.
