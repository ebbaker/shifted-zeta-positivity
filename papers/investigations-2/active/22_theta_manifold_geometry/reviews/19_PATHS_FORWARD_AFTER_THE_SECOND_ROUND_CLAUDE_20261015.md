# Paths forward after the second round: an assessment

15 October 2026, America/New_York. Prepared for Edward Baker with LLM
assistance. Model: Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. This is an internal assessment, not external refereeing or
formal verification.

Written at Edward's request after [Review 16](16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md),
[Response 17](17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md) and
[Reply 18](18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md). It records, with
the arithmetic and the sources, the ranking of continuation paths given in
the [recorded conversation](../chat-histories/claude-cowork/0002_2026-10-15T23-08-30Z_quaternion-theta-geometry-joint-review-response.json)
of this session, and it takes into account that Edward is following up in
parallel on topological properties of the manifolds defined near a
collision; that work was not in the repository at commit `58871b3` and is
not assessed here beyond the test proposed in Section 2. Nothing in
Reviews 16–18 changes.

## 0. The ranking

In order of expected value: (1) the \(\Lambda\) frontier through an
effective outer theorem, the one lane whose output is a theorem with a
number; (2) the topological work, aimed at the global formula rather than
the local invariants, and tested against the controls; (3) the
consolidation document, written now, possibly as a standalone paper on
collision controls; (4) Response 17's bounded anisotropic-contour test, run
once as specified in Reply 18 §6. Further lifts, identities and sign
criteria should stop, for the reason given in Reply 18 §7: each is true if
and only if RH, so no check is evidence for it.

## 1. The \(\Lambda\) frontier

**The mechanism.** Every published upper bound on the de Bruijn–Newman
constant has three ingredients: a numerical verification of RH to some
height; a barrier computation at that height, showing that no zero of
\(H_t\) crosses a vertical segment in the complex \(x\)-plane during
\(0\le t\le t_0\); and an effective outer theorem stating that for
\(t\ge t_0\) and \(x\ge X_*(t_0)\) all zeros are real. In the normalization
of both manuscripts, \(H_0(x)=\tfrac18\xi(\tfrac12+\tfrac{ix}2)\), so a
verification to height \(T\) covers \(x\le2T\). Writing
\(L(X)=\log(X/4\pi)\) and \(\theta\) for the effective threshold of the
outer theorem (real zeros once \(tL\ge\theta\)), the bound obtained at
verification height \(X\) is
\[
 \Lambda\;\le\;t_0=\frac{\theta}{L(X)},
\]
with the strip term \(y_0^2/2\) of de Bruijn's inequality added only when
reality at \(t_0\) is not established for all \(x\). As I read the
literature: Polymath (2019) used Platt's verification to \(3\cdot10^{10}\)
(\(X=6\cdot10^{10}\), \(L=22.3\)) with an effective threshold
\(\theta\approx4.46\), giving \(t_0=0.2\) and, with a strip of width
\(0.2\), \(\Lambda\le0.22\); Platt–Trudgian (2021) verified RH to
\(3\cdot10^{12}\) (\(X=6\cdot10^{12}\), \(L=26.9\)) and obtained
\(\Lambda\le0.2\) with no strip term; the 2026 self-published claim
\(\Lambda\le0.1787854\), which Review 16 could not verify, is what the same
\(\theta\approx4.8\) gives at \(L=26.9\). Rodgers–Tao give \(\Lambda\ge0\).

**The arithmetic.** At the current verification height the threshold is
the only lever, and each unit of \(\theta\) is worth about \(0.037\) in
\(\Lambda\):

| Effective threshold \(\theta\) | \(\Lambda\le\theta/26.9\) at \(X=6\cdot10^{12}\) |
| --- | --- |
| \(4.5\) (Polymath's constants) | \(0.167\) |
| \(4\) | \(0.149\) |
| \(3.5\) | \(0.130\) |
| \(3\) | \(0.112\) |
| \(61/24\approx2.54\) (Investigation 21's threshold) | \(0.095\) |
| \(2\) (the ideal: \(\operatorname{Re}s>1\) for the carrier) | \(0.074\) |

Equivalently, the outer region at \(t_0=0.1\) starts at
\(4\pi e^{2.54/0.1}\approx1.35\cdot10^{12}\) for the \(61/24\) threshold
and at \(4\pi e^{45}\) for \(\theta=4.5\); the first is inside the verified
range by a factor of four, the second is unreachable.

**Where Investigation 21 actually stands.** Its main theorem proves the
four-jet asymptotic with strict Laguerre signs on \(tL\ge61/24\),
\(x\ge X_*\), with \(X_*\) "finite, presently unevaluated". The only
explicit statement is the conservative region \(tL\ge5\),
\(x\ge4\pi\exp(10^9)\), and the explicit sum estimate behind the sharper
theorem (Proposition "explicit sum", with \(A_0=36138917/16\approx2.3\cdot10^6\)
in its \(A_0/\ell\) term and unevaluated exponent-pair constants) needs
\(L\ge100002\) before it says anything; Investigation 22's refined outer
budget (Note 06/01) still needs \(L-1\ge31{,}424{,}688\) after a factor-3974
improvement. The needed \(L\) is \(27\). So the theorem as it stands is six
orders of magnitude in \(L\) away from the regime where it would matter,
and the threshold \(61/24\) is an attractive asymptotic statement, not yet
an effective one.

**The project, stated so that it can fail.** Find the smallest \(\theta\)
for which an outer theorem with constants of order one can be proved, and
evaluate \(X_*(t_0)\) for it. The bounded first step is not the
exponent-pair machinery: it is to determine how far Polymath's own
absolutely convergent regime can be pushed below \(\theta\approx4.5\) by
sharper explicit bounds on the same quantities (the tail of the weighted
Dirichlet polynomial, the Riemann–Siegel-type remainder at complex time),
since every tenth of a unit there is \(0.004\) in \(\Lambda\) for free at
the current height. The exponent-pair route toward \(61/24\) is the stretch
goal, with Review 16's kill criterion unchanged: if \(X_*(0.15)\) exceeds
\(10^{13}\) or the constants cannot be evaluated, the lane is closed and the
frontier belongs to verification height alone. A new \(t_0\) also needs the
barrier at \(X=6\cdot10^{12}\) over \([0,t_0]\), which is a sub-interval of
what Platt–Trudgian computed if their barrier was at that height, and a
cheap computation otherwise.

**Why this lane and not the others.** It is the one place where the
program's analysis differs from the literature by a quantity (\(61/24\)
against \(4.5\)); it uses theta-specific inputs of all three kinds that
Investigation 19 identifies (the complete coefficient sum, which is (D1);
verification and barrier, which are (D2) and (D3)), so the controls do not
screen it; and its output is a theorem. It is explicit analytic number
theory with no geometry in it, and it should be judged only on whether it
beats the published constants.

## 2. The topological work near the collision

**What is settled.** The local topology at an \(m\)-fold collision is
completely classified by \(m\): the transverse link of the primitive curve
is the torus knot \(T(m,m+1)\) with Milnor number \(m(m-1)\) (Note 01/04),
the four-dimensional local degree of \((H,H_z)\) is \(\binom m2\) and the
real spacetime index is \(-\lfloor m/2\rfloor\) (Reply 18, Proposition
5.1), and the real zero curve has a fold with respect to the time
projection (two real zeros merge going backward in \(t\), which is the
\(m=2\) germ \(x^2+2(T-t)\)). Every one of these is a detector: it
distinguishes a collision from a regular point and tells its multiplicity,
and it carries no information about whether a collision occurs. RH is the
global statement that no detector fires at positive time.

**Where to aim.** A topological route therefore needs the global half: a
formula that counts the detectors without locating the zeros. The
spacetime winding of Note 01/04 is the honest version of that, and it is
worth writing down what it is on a box, because it fixes the cost
accounting. On \([t_1,t_2]\times[0,X]\) the winding of \((H,H_x)\) proves
exactly one thing, the absence of multiple real zeros inside. For
\(\Lambda\le t_0\) one would take \(t_1=t_0\), \(t_2=1/2\), and add the outer
theorem for \(x\ge X\). The top edge is free (all zeros real and simple at
\(t=1/2\)); the left edge is free (\(H(t,0)>0\), \(H_x(t,0)=0\)); the right
edge is a barrier-type computation at \(x=X\); and the bottom edge at
\(t=t_0\) is a count of the sign changes of \(H_{t_0}\) on \([0,X]\), which
is a computation of the same size as the RH verification to height
\(X/2\), redone at heat time \(t_0\). That is why the published proofs put
the bottom edge at \(t=0\), where the count already exists (Turing's
method is the argument principle on that edge), and transport reality
forward with a barrier in the complex \(x\)-plane; the real-box winding
cannot replace the complex barrier, because a conjugate pair hovering over
\([0,X]\) is invisible to it until it collides. So the winding is the right
language for the finite certificate, with the honest cost that comes with
it, and not a cheaper route to \(\Lambda\); its benchmark value (Review 16
§8, item 4) is against interval checks of \(E>0\) on one cell, not against
Polymath.

**The control test.** Whatever invariant the parallel work proposes, the
four controls of Reply 18 §3 all have nonzero winding on a box around their
collisions, so an argument that the invariant vanishes for theta must use
a premise that all four fail. One such premise exists and is legitimate:
*theta is a section of the degree-one line bundle on the integer lattice
with its full multiplier* \(z\mapsto z+\tau\). Controls \(A\) and \(B\)
fail it because unequal weights break the full multiplier (Note 05/01 §2);
\(C\) has no lattice; \(D=\Phi_{c,p}\) is a positive combination of theta
functions on the three isogenous lattices \(\mathbb Z\), \(p\mathbb Z\),
\(p^{-1}\mathbb Z\) (conductor \(p^2\) in Investigation 19's terms), not a
section on \(\mathbb Z\). An argument built on exactly that premise passes
the control test by construction; the burden it then carries is the
transfer, how a property of the section is supposed to constrain the
\(x\)-zeros of its heat transform, which is where every geometric attempt
so far has stopped (22 §8.5; Review 16 §5). One geometric fact locates the
difficulty. The Newman deformation multiplies the source along the geodesic
\(\operatorname{Re}\tau=0\) by \(e^{tu^2}=e^{t\,d(iy,i)^2/16}\), a Gaussian
in the hyperbolic distance from the elliptic point \(i\) (since
\(u=\tfrac14\log y\) and \(d(iy,i)=|\log y|\)). The deformed source is a
function on one geodesic, and the only element of the modular group
carrying that geodesic to itself is the inversion \(S\), which fixes \(i\):
that is the geometric content of "only the functional equation survives
the flow". A surface-level structure, the bundle, the elliptic family, its
monodromy or its characteristic classes, can therefore enter only through
a construction that leaves the geodesic, for instance the orbit of the
geodesic under the modular group, or a two-dimensional extension of the
deformation whose restriction to the geodesic is Newman's. The first thing
to settle, on paper and before building more structure, is which of these
the proposed invariant uses and how the one-dimensional flow is supposed
to see it. When the notes are in the repository I will review them against
exactly this test; it is quick and decisive either way.

**The Jensen-surface formulation.** RH \(\iff\) the real hyperelliptic
curves \(y^2=J_{2g+1}(x)\) are M-curves (Note 01/05) is correct and is
Pólya's Jensen-polynomial criterion in the vocabulary of real curves; for
hyperelliptic curves the M-curve condition is just "all roots real", so
the topology of real curves adds no constraint beyond hyperbolicity. The
decision on whether it is worth a remark belongs to a literature check:
Pólya (1927); Csordas–Varga on Turán inequalities; Dimitrov–Lucas on the
higher-order Turán inequalities for \(\xi\); Griffin–Ono–Rolen–Zagier
(2019), who prove hyperbolicity of the Jensen polynomials \(J^{d,n}\) of
\(\xi\) for every degree \(d\) and all large shifts \(n\) by showing they
converge to Hermite polynomials; O'Sullivan's account, cited in Review 13.
The Hermite limit is worth one remark in that check: the same Hermite
polynomials are the heat germs of Note 01/04, because large shifts probe
the source at large \(u\), which is the outer region of Section 1 in the
coefficient variable. If the M-curve phrasing is absent from that
literature, it is a remark in the consolidated paper, not a standalone
result; the absence of an RH proof is not the test, as Response 17 says.

## 3. The consolidation document, now

Review 16 §8 item 2 asked for one short document with three lists: proved
facts worth keeping, RH-equivalent reformulations, and closed mechanisms
with the control that closed each. After Reply 18 it should contain the
endpoint table (Reply 18 §1), the certificate proposition (§2), the
per-control hypothesis table (§3), and the classification rule
(reformulation versus milestone, §7), with Investigation 19's controls and
the statement of what any upper-bound proof must use. I would write it
before any of the other lanes, for two reasons. It is the document that
stops the criterion treadmill, because every later proposal is sorted by
its rule. And it is the publishable part of the last two days: a short
paper on collision controls for the de Bruijn–Newman flow, consisting of
the Euler-factor controls, the weighted-square and reflected controls, the
reflection rigidity theorem, the per-control table and the screening
corollary, with the certified numerics, is a sharp negative result that
stands on its own. Review 13's publication threshold applies: attributed
classical ingredients, no rediscovered principles presented as new, and
one new structural statement, which here is the screening theorem and the
two complementary control families.

## 4. The anisotropic test, last

Response 17's bounded comparison, in the protocol of Reply 18 §6: one
cell of 21's height-112 region, the bidisc family
\(\Omega_{\rho,\sigma}\), the target \(\mathcal L_0\) at a stationary point
with small \(E\), every boundary contribution kept, the theta-specific
input named on a face, the control test on \(A\)'s predecessor, and a cost
comparison with the direct method. One week; pass or fail by its numbers.
My prediction is recorded there and is falsifiable.

## 5. What I would stop

Lifts of the heat flow of any kind, further rewritings of the Laguerre
expressions in new coordinates, and further sign criteria. Reply 18 §7
gives the reason: an RH-equivalent reformulation is true if and only if
RH, so identities, polynomial replays, rational surrogates and numerical
checks test the identity, not the criterion, and should not be counted as
progress. The same rule classifies any new proposal at the outset: if it
implies RH and RH implies it, it is a reformulation and is stated once; if
it does not imply RH, it is a milestone and is judged by its number against
the published ones.

## Provenance

Sources: the three reviews above and the recorded conversation; 21's
manuscript (main theorem, Proposition "An explicit outer region",
Proposition "explicit sum" with its constants); 22's Note 01/04, Note 01/05,
Note 05/01 §2, Note 06/01 and Review 13; Investigation 19's screening
section. The Polymath, Platt–Trudgian and Rodgers–Tao statements are
quoted from memory of the published results and from Review 16's web
check; the 2026 claims are unverified. No file in the repository was
modified other than the addition of this note and its README entry;
nothing was committed. The session's chat record is kept in this
investigation's `chat-histories/claude-cowork/` registry by the standing
project instruction.
