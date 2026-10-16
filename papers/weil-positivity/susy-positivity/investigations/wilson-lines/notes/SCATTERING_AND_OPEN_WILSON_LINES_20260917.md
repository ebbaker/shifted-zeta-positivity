# Why a scattering matrix, why an open Wilson line, and what conformal symmetry costs

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Research note,
answering three questions put by Edward Baker against the
[inner-function note](INNER_FUNCTION_AND_RESONANCE_20260917.md) and the
[critical-path note](CRITICAL_PATH_20260917.md): why the scattering matrix is the
natural object, whether his *Supersymmetric open Wilson lines*
(JHEP 03 (2011) 140, [arXiv:1102.4948](https://arxiv.org/abs/1102.4948)) is
relevant, and whether the conformal symmetry of Yang--Mills could be used to
compactify and tame the infinities.

**No manuscript change has been made.** Section 5 lists what this recommends.

*Reading scope.* I have read the abstract, the operator definition and the setup
discussion of arXiv:1102.4948 through automated extraction, **not the whole
paper**. Everything attributed to it below is from those parts and is marked;
where I extrapolate, I say so.

---

## 0. Summary

1. **The scattering matrix is not a choice.** Four properties of the transfer
   symbol $K_\omega$ --- causality, unimodularity on the critical line,
   resonances just off the axis, and a phase derivative equal to a density of
   states --- are the *defining* properties of a one-channel $S$-matrix. Nothing
   was imported; the program's own shifted transfer already is one. And
   $K_\omega$ is a *ratio*, which is what a reflection coefficient is.
2. **The 2011 paper supplies exactly the operator class the program's
   conditions demand, and it is relevant for a reason sharper than the framing.**
   An open Wilson line is a **bilinear in matter fields joined by a line**, not a
   trace of a holonomy. That removes the obstruction behind manuscript
   Condition 7.1 at a stroke: the exclusion there rests on the boundedness of a
   *character*, and a bilinear whose endpoints carry operator-valued
   distributions is unbounded by construction. Condition 7.1 should be rewritten
   from a prohibition into a prescription.
3. **The geometry matches the manuscript's endpoint result exactly.** A ray
   ending on a defect has a pinned end and a free end; manuscript
   Proposition 6.1 found the endpoint variation is rank one at the *leading* end
   only, causality having killed the trailing one. Fixed tail, moving head. And
   the paper's conformal map of the ray to a semicircle is the compactification
   of exactly the direction the manuscript could not close.
4. **Conformal symmetry is the right symmetry for half the problem --- the half
   that is not the bottleneck --- and it carries a cost the paper itself
   quantifies.** Its result that in non-superconformal $\mathcal N=2$ theories
   *all BPS open Wilson lines have vanishing expectation value* is, in this
   program's terms, the statement that protection and an absolute scale cannot be
   had together in that class. The Weil form fixes an absolute scale twice over.
5. Two of the three infinities do compactify, and one of them already has:
   the **spectral** compactification is the Cayley transform the critical-path
   note identified, and the **geometric** one is the ray-to-semicircle map. The
   **trace** obstruction does not compactify --- it is local --- and the fix for
   it is the one the open Wilson line forces anyway: smear the endpoint.

---

## 1. Why the scattering matrix is forced

The inner-function note establishes four facts about
$K_\omega(p)=\xi(\frac12+p-\omega)/\xi(\frac12+p+\omega)$. Listed together they
are a definition.

| Fact | Scattering name |
|---|---|
| $k_\omega$ supported in $[0,\infty)$; $K_\omega$ analytic in a right half-plane | causality, via Paley--Wiener |
| $\lvert K_\omega(i\tau)\rvert=1$, exactly and unconditionally | unitarity on the energy shell |
| poles at $\operatorname{Re}p=-\omega$, i.e. at $-\omega+i\gamma_\rho$ | resonances of width $\omega$ |
| $-\,d\varphi/d\tau=2\theta'(\tau)=b(\tau^2)+w_0$ | Wigner--Smith time delay $=$ density of states |

The last line is the Birman--Krein relation in this setting: the phase of the
determinant of a one-channel $S$-matrix is $-2\pi$ times the spectral shift
function, and here $\Psi/\pi\to N(\tau)$, the zero-counting function. So **the
Riemann zero counting function plays the role of the Krein spectral shift, and
the zeros are the resonances.** The argument-principle bookkeeping of Section 4
of the inner-function note is then Levinson's theorem.

Two further points make the identification specific rather than suggestive.

**$K_\omega$ is a ratio, and a ratio is a reflection coefficient.** A
half-infinite line with a boundary condition at one end has exactly one
scattering channel, and its entire $S$-matrix is a single unimodular reflection
coefficient: outgoing amplitude over incoming amplitude. $K_\omega$ is literally
that shape --- $\mathcal F$ at the reflected argument over $\mathcal F$ at the
argument --- with the functional equation supplying the reflection.

**A holonomy cannot do this.** Manuscript Condition 7.1 says a holonomy in a
finite-dimensional representation of a compact group is unitary, so its character
is bounded and every pairing built from it is bounded on $L^2$. In scattering
language the failure is sharper: such a holonomy has a **bounded group delay and
no resonances**, whereas the required delay grows like $\log\tau$ and the
required resonance set is infinite with density $\frac1{2\pi}\log(\tau/2\pi)$.
Unitarity was never the missing property; the delay was.

*Caveat, and it is the program's standing one.* Reading $\tau$ as an energy and
$x$ as a scattering coordinate is an identification the program does not make
(the caveat attached to selection rule 4). Section 3.5 below is the first
motivated reason to make it, and it is still an assumption.

*And a caution about the neighbourhood.* Zeros-as-resonances is old --- it is the
Berry--Keating and Connes territory the program already cites. Nothing in this
section claims the idea. What is this program's own is that the object arrives
**from its own shifted transfer**, with the constants fixed: the delay is
$2\theta'$ exactly, and the resonance widths are exactly $\omega$.

## 2. Open Wilson lines are the right operator class

### 2.1 What the operator is

From arXiv:1102.4948, the open Wilson line is
\[
 OW_i^{\,j}[\tilde C]=\bar\psi^{\,j}(x_j)\;
 P\exp\!\left[\int_{\tilde C}\!ds\,\Big(iA_\mu\dot x^\mu
 +n^k(s)\Phi_k\,|\dot x|\Big)\right]\psi_i(x_i),
\]
a **bilinear in matter fields joined by a Wilson line**, the endpoint fields
transforming in the fundamental and antifundamental, which is what makes the
contraction gauge invariant. The line carries a scalar coupling against
*arclength*, as in the Maldacena--Wilson construction. The paper's two settings
are $\mathcal N=2$ with fundamental hypermultiplets, and $\mathcal N=4$ coupled to
a three-dimensional defect hypermultiplet, where the supersymmetric configuration
is a semicircle related to a **ray ending on the defect** by a conformal
transformation.

### 2.2 It dissolves the obstruction behind Condition 7.1

Manuscript Condition 7.1 (W1) is stated as a prohibition: a holonomy in a
finite-dimensional representation of a compact group has a bounded character, so
selection rule 2 --- unboundedness relative to $\lVert f\rVert_{L^2}$ --- excludes
it. The whole force of that argument is that the object is a **trace of a group
element**.

An open Wilson line is not. Its endpoints carry $\psi$ and $\bar\psi$, which are
operator-valued distributions, so the operator is unbounded by construction and
the exclusion has nothing to act on. The rule is satisfied structurally rather
than evaded.

> **Recommendation.** Rewrite Condition 7.1 from "the connection must be
> unbounded in an infinite-dimensional representation" --- which reads as a
> prohibition with no positive content --- to: *the object must be a bilinear in
> unbounded endpoint operators joined by a transport, not a character; and its
> group delay must grow like $\log\tau$ with smooth part $2\theta'(\tau)$.* The
> first clause names the class; the second is the quantitative test.

### 2.3 The geometry already matches the manuscript

Manuscript Proposition 6.1: the $L$-derivative of the compressed transfer is
**rank one, at the leading endpoint only**, with the boundary value of the
evolved field as its coefficient; causality kills the trailing endpoint. Fixed
tail, moving head.

A ray ending on a defect is that geometry: one end pinned on the defect, one end
free. And the coefficient of the rank-one variation --- "the boundary value of the
evolved field" --- is, in the open Wilson line, literally the endpoint field
$\psi$ at the moving end. The two descriptions are the same object, arrived at
from the arithmetic side and from the gauge side independently.

This also says which end is which: the **defect is the trailing endpoint**, the
one causality makes invisible, and the free end is where the contraction defect's
flux passes (inner-function note, Proposition 2).

*Qualification, added after this note was written.* The match is with
$\partial_L$ at fixed $\omega$. Along a path in which the shift also moves, the
motion is endpoint **plus bulk**, and the bulk term is the whole Weil generator;
see the [path-derivative note](PATH_DERIVATIVE_CORRECTION_20260917.md). What
survives without qualification is the stronger, non-differential statement that
the defect *itself* is a boundary flux at every $(\omega,L)$.

### 2.4 Problem 6.5 is the usual fact that fields are distributions

Manuscript Proposition 6.3 obstructs the endpoint flow: point evaluation is not
bounded relative to the form, and the shift's smoothing misses the trace
threshold at every admissible $\omega$, by exactly the borderline. In the open
Wilson line that obstruction is familiar and has a standard resolution: an
endpoint field is a distribution and must be **smeared**. Problem 6.5 ("close the
endpoint flow, or show it cannot be closed") should therefore be restated as:
*with what profile must the endpoint operator be smeared, and does the smeared
flow close on the form domain?* Condition 7.3 answers the first half --- the
smearing must produce an effective defect dimension $\Delta=\frac12$ --- which is
the marginal case and therefore the tightest smearing the domain permits. That
the obstruction is borderline is then not a coincidence but the statement that
the required operator sits exactly at the edge of what can be smeared.

## 3. Conformal symmetry: what it compactifies, and what it costs

### 3.1 The spectral compactification is already in hand

The conformal map that compactifies the right half-plane is the Cayley transform,
and the critical-path note has already found it to be the natural coordinate:
$Z_\omega=(I-V)(I+V)^{-1}$, with $(1-K_\omega)/(1+K_\omega)=i\tan\Psi$ on the
critical line. Under it, $K_\omega$ becomes an inner function of the **disc**, a
Blaschke product whose zeros are the images of $\omega+i\gamma_\rho$ and
accumulate at the single boundary point corresponding to $\tau=\infty$. The
logarithmically divergent group delay is exactly that accumulation. So the
$\tau\to\infty$ infinity does compactify, the compactification is conformal, and
it is the Krein--Nevanlinna picture --- which is also where the companion
investigation's top open item sits. Two routes, one destination.

### 3.2 The geometric compactification tames $L$, but not the criterion

The ray-to-semicircle map of arXiv:1102.4948 compactifies the free end of the
line. In the program's variables that is the $L\to\infty$ limit, and turning it
into a boundary point of a compact family is a real gain in framing: the limit
becomes the closing-up of the semicircle rather than an unbounded process.

It does not change what lives there. Corollary C of the critical-path note ---
contraction at every $L$ is equivalent to the absence of zeros at distance more
than $\omega$ --- is a statement about the zero set of $\xi$ and is invariant
under any reparametrization of the line. Compactifying moves the difficulty to
the boundary point; it does not remove it. That is worth saying plainly, because
"tame the infinity" and "remove the content" are easy to confuse, and here the
content is entirely at the infinity.

### 3.3 The cost, which the 2011 paper itself quantifies

The program has a standing no-go: **exact scale invariance is incompatible with
the target.** A scale-invariant theory has no absolute scale, and the Weil form
fixes one twice over --- dilation destroys the prime atoms at $m\log p$ and shifts
the density symbol. This is why the RG fixed point was closed in the companion
investigation's open directions.

The 2011 paper makes the tension concrete in one class. Its finding, as extracted:
in non-superconformal $\mathcal N=2$ theories with fundamental hypermultiplets,
**all BPS open Wilson lines have vanishing expectation value**; nontrivial
protected operators appear only in the superconformal case, with $2N_c$
fundamental hypermultiplets. So within that class:

> protection requires conformality, conformality forbids an absolute scale, and
> the target requires one.

That is a genuine obstruction and not a framing problem. It also inverts the
preference recorded in the program's defect survey, which ranks supersymmetric
cases higher because they offer more explicit identities: **here the explicit
identities are available exactly where the required structure cannot be.** Pure
Yang--Mills, whose dimensional transmutation manufactures an absolute scale, has
the feature the target needs and none of the identities. That trade should be
stated in the manuscript.

### 3.4 Where an absolute scale could come from

Not from a single defect. A flat conformal defect through the origin still
preserves dilations about a point on it, so it fixes no scale. **Scales are
separations.** In the radial coordinate $r=e^x$ of a ray, the prime atoms at
$x=m\log p$ sit at $r=p^m$, so the structure required is invariance under
$r\mapsto pr$ for every prime, and not under continuous dilation --- invariance
under the multiplicative semigroup of positive integers rather than under
$\mathbb R_+$.

That is the atomic connection of manuscript Section 6.4 in geometric dress: the
connection's kernel is continuous plus atoms at $m\log p$, and a flat connection
with punctures has monodromy. The punctures are at integer radii. I record that
the named object in that direction is the Bost--Connes system, and that this is
adjacent literature this program has not entered; I am not proposing it as a
route, only naming where the symmetry lives.

### 3.5 The principal series, and why everything here is marginal

One further reading, which is the first motivated reason to identify the
arithmetic coordinate with a ray's radial logarithm.

For a one-dimensional conformal system the dilatation eigenvalue is the conformal
weight $\Delta$, and the unitary principal series of $SL(2,\mathbb R)$ is
$\Delta=\frac12+i\tau$ with $\tau$ real. That is the **critical line**. In this
reading:

- the critical line is the principal series;
- the zeros $\rho=\frac12+i\gamma$ are principal-series data;
- the shift $\omega$ moves off the principal series, which is exactly the
  detection-threshold reading of the critical-path note;
- the Riemann hypothesis is the statement that nothing leaves the unitary line.

And Condition 7.3 falls into place. It requires an effective defect dimension
$\Delta=\frac12$: the **edge of the principal series**, the most marginal unitary
weight there is. That explains the coincidence recorded as manuscript
Remark 6.4 --- the Gagliardo borderline, the transfer's $(2+|\tau|)^{-1/2}$ gain,
and the trace threshold $r>\frac12$ are three faces of one exponent, and the
exponent is the principal-series edge. Neither the displacement operator
($\Delta=2$) nor the protected scalar insertion ($\Delta=1$) sits there, which is
the exclusion Condition 7.3 already records.

*Status: this is a reading, not a result. It rests on the identification the
program declines to make, and the neighbourhood --- conformal quantum mechanics,
$SL(2,\mathbb R)$ and the zeros --- is crowded.*

## 4. What to check, cheapest first

1. **The delay test on a specific open Wilson line.** Condition 7.1's revised
   form is one computation: take a protected open Wilson line two-point function
   in the defect setting, extract the phase of its spectral kernel as a function
   of the dilatation eigenvalue, and compare its derivative with $2\theta'(\tau)$.
   A bounded delay kills the candidate; a delay growing like $\log\tau$ with the
   wrong coefficient kills it too. This needs no arithmetic and no positivity.
2. **The vanishing theorem as a selection rule.** Establish whether "BPS $\Rightarrow$
   vanishing expectation unless superconformal" extends beyond the $\mathcal N=2$
   fundamental-hypermultiplet class of the 2011 paper. If it does, it is a
   general obstruction of the same kind as the program's own exclusions and
   belongs in the selection index; if it does not, the exception is where to look.
3. **Smearing profile for the endpoint.** Section 2.4: find the profile making
   the endpoint operator $\Delta=\frac12$, and test whether the smeared endpoint
   flow closes on the form domain. This is manuscript Problem 6.5 restated in a
   form that has a standard method attached.
4. **Separations, not defects.** Section 3.4: ask what configuration of a defect
   system has its conformal symmetry broken to the multiplicative semigroup of
   integers, before asking whether any gauge theory realizes it.

## 5. Recommendations for the manuscript (none made)

1. Rewrite **Condition 7.1** as Section 2.2 proposes: a bilinear in unbounded
   endpoint operators, plus the $\log\tau$ delay test.
2. Add a remark to **Section 6** recording the geometric match of Section 2.3,
   and restate **Problem 6.5** as the smearing question of Section 2.4.
3. Add the scale/conformality trade of Section 3.3 to **Section 7**, with the
   2011 vanishing result cited, and the consequent inversion of the survey's
   preference for supersymmetric cases.
4. Add **Section 1**'s table as the justification for the scattering reading,
   replacing the single sentence in the inner-function note's Section 7, and keep
   its caution about the crowded neighbourhood.
5. Add arXiv:1102.4948 to the references.

## 6. Status of each claim

- **Section 1**'s table is a restatement of results proved or verified in the
  inner-function note; the Birman--Krein and Levinson identifications are
  standard readings, not new results. The reflection-coefficient reading is
  structural, not a derivation from a named scattering system.
- **Section 2.1** is extracted from arXiv:1102.4948; I have not read the whole
  paper. **Sections 2.2--2.4** are this program's own deductions from it.
- **Section 3.1** is established in the critical-path note. **Section 3.2** is a
  written argument. **Section 3.3** rests on the extracted vanishing statement and
  on the program's existing no-go; the extrapolation beyond the paper's stated
  class is flagged as open in Section 4.2.
- **Sections 3.4 and 3.5** are readings and are labelled as such. Section 3.5
  rests on an identification the program explicitly declines to make.
- No source is constructed, no positivity is proved, nothing assumes the Riemann
  hypothesis, and no gauge theory is matched or excluded.
