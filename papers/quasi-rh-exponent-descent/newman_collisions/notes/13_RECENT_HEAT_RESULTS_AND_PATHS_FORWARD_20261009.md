# Recent heat results and paths forward

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex). Reasoning effort: ultra, verified from the current
chat's recorded configuration. The parallel same-model audits are internal
checks, not independent mathematical validation.

This overview records the continuation in Heat Notes 8–12 and the inputs it
provides for the [stable heat manuscript](../newman_collision_reductions.tex).
The main advance is a more precise reduction to genuine signed arithmetic:
the approximation errors are paid, growing endpoint sets can be removed by
actual-phase cancellation, a complete derivative average is positive, and an
all-real threshold collision has an explicit higher-jet sign constraint.
The missing implication remains local: neither the joint value/derivative
vector nor the threshold jet expression has yet been shown incompatible with
the actual collision conditions.

The investigation has not proved RH, excluded an actual positive-time heat
collision, or established a new competitive Newman bound. It has established
which parts of the proposed route now have proofs, which proposed mechanisms
fail within their stated scope, and where a new arithmetic input must enter.

## 1. The common interface is now explicit and fully paid

The most recent results concern the shrinking-time sector

\[
1\le\kappa\le2,\qquad 0<t\le1/20,\qquad
L=\kappa/t,\quad x=4\pi e^L,\quad
N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor,
\]
\[
\mathfrak a=\frac{\kappa(4-\kappa)}{16},\qquad
\mathfrak b=\frac{\kappa(\kappa+4)}{16}.
\]

All spatial derivatives hold time and the relevant integer cutoff fixed.
The scale \(L\) in a translated derivative coordinate is also held at its
center value. Differentiating the scaling curve or a jumping cutoff would
give different quantities from those in the collision equation.

Write \(H_t=A_tQ_t\), where the manuscript's symmetric analytic normalizer
\(A_t\) is nonvanishing, and let \(F_{t,N}\) be the genuine fixed-cutoff
approximant. [Note 8](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md)
proves on the complex disk of radius \(1/L\)

\[
|Q_t-F_{t,N}|\le\eta_N\le5e^{-\mathfrak b/t},\qquad
|Q_t'-F_{t,N}'|\le L\eta_N.
\tag{1}
\]

This is the full error, including the effective approximation, conversion to
the symmetric normalizer, reflected analytic terms, every possible cutoff
change, and the Cauchy derivative payment. More generally, the same disk
gives \(j!\eta_NL^j\) for each fixed spatial derivative order \(j\).
The imported approximation is
[Polymath, Theorem 1.3](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3),
with the local deductions printed in the investigation.

The exact real-axis vector has the form

\[
\mathcal V_N(x)=\left(F_{t,N}(x)/2,\;2F_{t,N}'(x)/L\right)
=\sum_{n\le N}w_n
\bigl(\cos\phi_n,\;r_n\sin\phi_n-c_n\cos\phi_n\bigr).
\tag{2}
\]

Here \(w_n,\phi_n,r_n,c_n\) are the exact heat weights, logarithmic
phases, scaled frequencies, and amplitude drift from Note 8. In particular,
the derivative coordinate retains the drift \(c_n\). Every genuine collision
\(H_t(x)=H_t'(x)=0\) requires

\[
|\mathcal V_N(x)|^2\le\frac{17}{4}\eta_N^2.
\tag{3}
\]

The approximation is therefore already small enough to support an arithmetic
collision test. The obstacle is proving a signed inequality for (2), rather
than further reducing its analytic remainder by a constant factor.

## 2. What the continuation proves

| Result | Achievement | Mathematical scope |
| --- | --- | --- |
| [Note 8: signed vector and phase obstructions](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md) | Prints the exact signed pair kernel and the exponential error in (1); proves an actual adjacent-packet cancellation and an independent-phase zero-vector construction. | The packet obstruction concerns packetwise coercivity. The constructed independent phases are a relaxation. Neither is an actual heat collision. |
| [Note 9: genuine edge cancellation and averages](9_GENUINE_SIGNED_EDGE_CANCELLATION_AND_AVERAGED_PROBES_20261009.md) | Removes the last \(\lfloor N^{3/4}\rfloor\) genuine terms with decaying signed value and derivative payments; proves positive mean square for the complete genuine value on a sufficient translated interval. | The retained sum still has \(N-o(N)\) terms. An upper bound on a removed tail is not a lower bound on the retained core. |
| [Note 10: multiplicative relaxation](10_COMPLETE_MULTIPLICATIVE_PHASE_OBSTRUCTION_20261009.md) | Constructs an exact zero of the complete twisted joint vector, preserving all composites, weights, local derivatives, and the leading phase. | The unit-modulus twist is completely multiplicative but need not arise from the genuine height orbit. No twisted heat remainder theorem is asserted. |
| [Note 11: derivative cores and joint probes](11_ASYMMETRIC_DERIVATIVE_CORES_AND_JOINT_PROBES_20261009.md) | Removes a larger \(\lfloor N^{7/8}\rfloor\) derivative edge, pays raw jets, and proves a complete derivative average on the shorter sufficient range \(Dt^2e^{2\mathfrak a/t}\). | The value and derivative cores have different cutoffs. Their two coordinates do not form a function and its derivative. The averaged lower bound permits an isolated common zero. |
| [Note 12: threshold jets](12_THRESHOLD_COLLISION_JETS_AND_PAID_LAGUERRE_TEST_20261009.md) | Derives a necessary normalized fourth-jet inequality from all-real threshold information, and pays its complete quadratic approximation error. | The missing input is the strict opposite signed inequality for the genuine arithmetic jets. The all-real hypothesis is essential. |

The actual-phase edge estimates are a substantive gain over absolute tails.
With

\[
K_v=N-\lfloor N^{3/4}\rfloor,
\qquad K_d=N-\lfloor N^{7/8}\rfloor,
\]

every genuine collision must satisfy the asymmetric core conditions

\[
|F_{t,K_v}(x)/2|\le\eta_N/2+40N^{-1/24},
\]
\[
|2F_{t,K_d}'(x)/L|\le2\eta_N+800N^{-1/24}/L.
\tag{4}
\]

These are exact finite-tail subtractions after (1), using the actual phases.
The wider derivative edge is possible because the endpoint derivative
frequency becomes small. Its cancellation proof uses
[Arias de Reyna's explicit derivative estimate](https://arxiv.org/html/2407.02094v1)
and an explicit Abel-variation ledger. It does not assume a new holomorphic
approximation at the reduced cutoff.

The complete derivative result is also genuinely signed. There is an absolute
\(D\), and a sufficiently small uniform time range, such that for
\(H_d=Dt^2e^{2\mathfrak a/t}\),

\[
\frac1{H_d}\int_0^{H_d}
\left(\frac{2F_{t,N}'(x+y)}L\right)^2dy\ge\frac14,
\qquad
\frac1{H_d}\int_0^{H_d}
\left(\frac{2Q_t'(x+y)}L\right)^2dy\ge\frac18.
\tag{5}
\]

The joint energy inherits the derivative lower bound. The weighted local-gap
inequality in
[Montgomery–Vaughan, Theorem 2 and Corollary 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
removes the earlier logarithm, and the derivative-weighted frequency budget
supplies the factor \(t^2\). Both signs of every reflected frequency are
included. The final near-zero-frequency term is omitted only during the
intermediate gap estimate and restored before (5).

Physical movement across the interval is paid, including changing weights,
phases, normalizers, and the possible one-term change of natural cutoff.
Remainders are paid on small complex disks at the translated centers, rather
than on a single disk as large as \(H_d\). The freezing estimate has a strict
exponential reserve; on the earlier, larger value-probe interval it is
\(O(L^2e^{(5\mathfrak a-\kappa)/t})=o(1)\), since
\(5\mathfrak a-\kappa\le-1/16\). The shorter derivative interval inherits
this payment. Thus (5) concerns the complete physical functions, not just a
polynomial with artificially frozen phases.

## 3. Why the tested mechanisms stop short of exclusion

The absolute last-block value mass has size \(e^{\mathfrak a/t}\), and its
scaled derivative mass has size \(te^{\mathfrak a/t}\). Both diverge in this
sector. Endpoint frequency suppression helps signed estimates, but it does
not make the whole endpoint block a small absolute perturbation of the
leading term. The ordinary exponent-pair calculation in Note 9 likewise
leaves a positive upper-bound exponent for the explicitly surveyed hull in
[Trudgian–Yang](https://arxiv.org/html/2306.05599v3). This diagnoses the cited
upper-bound method; it does not prove growth of the actual signed sum or
exclude other arithmetic transformations.

Actual phases also defeat a simple positive packet comparison. At
\(x=4\pi M^2\), \(t=\kappa/(2\log M)\), the genuine terms (M-1,M)
have diagonal energy asymptotic to
\(2\cos^2(\pi/8)w_M^2\), but their joint packet energy is only
\(O(w_M^2/M^2)\). Their adverse cross term cancels almost the entire
diagonal. The same obstruction survives any fixed number of bounded
translations of that packet. It does not settle the complete sum or probes
over longer ranges.

The multiplicative construction strengthens the independent-phase
obstruction. Note 10 retains all composite terms and uses isolated primes, a
bounded complete residual, and a contraction argument to close both
coordinates exactly. Its only external asymptotic import beyond the shared
coefficient facts is the classical
[prime number theorem](https://dlmf.nist.gov/27.12#E4). Consequently, a positive
joint bound valid for every completely multiplicative unit-modulus twist
cannot furnish the missing genuine inequality. The actual height orbit is
more restrictive: changing height also moves the weights, cutoff, carrier,
normalizer, and derivative data. Approximation of a finite list of prime
phases does not pay those simultaneous movements.

The averaged theorem has a different limitation. The paid curvature budget
is \(|Q_t''|\le M_2=C_2e^{\mathfrak a/t}\). At a collision it gives

\[
\frac1H\int_0^H\left(\frac{2Q_t'(x+y)}L\right)^2dy
\le\frac{4M_2^2H^2}{3L^2}.
\tag{6}
\]

With this budget, a small Taylor upper bound is available only at scales of
order \(Le^{-\mathfrak a/t}\). The ratio of the sufficient averaging range
in (5) to that scale is

\[
\frac{H_d}{Le^{-\mathfrak a/t}}
=\frac{Dt^2}{L}e^{3\mathfrak a/t}\longrightarrow\infty.
\tag{7}
\]

This is the deficit of the proved average plus the available absolute Taylor
conversion. It is not a theorem that such long probes are necessary, or that
the actual curvature must be large at a collision. The positive-measure
consequence of (5) also allows isolated common zeros.

Finally, the heat equation, real-rootedness at a threshold, and generic
Laguerre signs permit a positive collision. Note 12 gives an exact even
quartic backward-heat flow with a freely chosen positive all-real threshold;
it saturates the forced-mirror jet inequality. Earlier manuscript results
give a separate positive-kernel example. These examples have their stated
general analytic scope. They are not zeta heat collisions, and the quartic
does not have the genuine theta kernel or the arithmetic coefficients.
They explain why a new signed arithmetic implication is required.

## 4. The two precise remaining targets

The first target is direct local nonvanishing. Write
\(h_n=(\cos\phi_n,r_n\sin\phi_n-c_n\cos\phi_n)\) and
\(D_N=\sum_{n\le N}w_n^2|h_n|^2\). A sufficient complete actual-phase
estimate in this sector is

\[
2\sum_{n<m}w_nw_m h_n\!\cdot h_m
>-D_N+\frac{17}{4}\eta_N^2.
\tag{8}
\]

It retains every phase-difference, phase-sum, and drift contribution. A proof
conditional on both candidate coordinates in (3), or on the paid core
conditions (4), can be equally sufficient. An absolute tail estimate alone
cannot replace (8).

The second target uses extra information available specifically at an
all-real threshold. Put \(b_x=\partial_x^2\log A_t\) and
\(\gamma=18b_x+9/x^2=O(x^{-2})\). At an all-real-time multiple zero,
with \(q_j=Q_t^{(j)}(x)\), Note 12 proves

\[
\mathscr L(q)=2q_3^2-3q_2q_4-\gamma q_2^2\ge0.
\tag{9}
\]

This follows by deflating two root copies from the genuine order-one
Hadamard product and retaining the forced mirror root. The canonical-product
input is stated in
[Polymath, Section 3](https://arxiv.org/html/1904.12438v2#S3). The factor 9
is explicit. The normalizer is applied locally after the genuine product
argument; no global real-root product for \(Q_t\) is assumed.

For a fixed retained cutoff \(K\), let \(f_j=F_{t,K}^{(j)}(x)\) and use
proved errors \(|q_j-f_j|\le\delta_j=j!\eta_NL^j+\tau_j\), for
\(j=2,3,4\). The exact measured payment is

\[
\begin{split}
\Delta={}&4|f_3|\delta_3+2\delta_3^2
+3\bigl(|f_2|\delta_4+|f_4|\delta_2+\delta_2\delta_4\bigr)\\
&+|\gamma|\bigl(2|f_2|\delta_2+\delta_2^2\bigr).
\end{split}
\]

A genuine arithmetic implication

\[
\boxed{\quad \mathscr L(f)<-\Delta \quad}
\tag{10}
\]

at every putative threshold collision would contradict (9). The strict
negative sign, not the approximation of the expression, is missing.
The complete cutoff already has

\[
\Delta_N=O\bigl(L^4e^{-\kappa^2/(8t)}
+L^6e^{-2\mathfrak b/t}\bigr)=o(1).
\]

The common value cutoff \(K_v\) also has a vanishing payment, with an
additional \(O(N^{-1/6})\). Individual jet tails at the deeper derivative
cutoff \(K_d\) vanish, but the available product budget has exponent
\(11/24-\kappa/4\), positive below \(\kappa=11/6\). Thus one must retain
the measured payment there; small individual errors do not automatically
give small quadratic errors.

These two targets have different logical scopes. The manuscript's absence
of *all* positive-time real collisions is an RH-equivalent endpoint route.
For an RH contradiction it is enough instead to exclude every putative
positive **threshold** collision, because failure of RH gives
\(\Lambda>0\), all zeros are real at \(\Lambda\), and a finite nonzero
multiple zero occurs there. The all-real hypothesis makes (9) available at
that threshold; it is not available at an arbitrary earlier collision when
other zeros may still be nonreal.

Either RH application needs global coverage of the possible threshold
parameters. Uniformity as \(t\downarrow0\) with \(\kappa\in[1,2]\)
does not cover all positive times, all heights, or the other relations
between time and height. Even complete exclusion in this sector would be
a local theorem rather than an RH proof.

Higher multiplicity is another explicit obligation. At multiplicity at
least four, \(q_2=q_3=0\), so (9) can be vacuous. At exact multiplicity
\(m\ge2\), full deflation instead gives

\[
\frac{q_{m+1}^2}{(m+1)^2}
-\frac{2q_mq_{m+2}}{(m+1)(m+2)}
-\left(b_x+\frac{m}{4x^2}\right)q_m^2\ge0.
\tag{11}
\]

This supplies a hierarchy, not an exclusion theorem. Applying it requires
the corresponding \(m,m+1,m+2\) jet errors, or a separate argument that
bounds or eliminates higher multiplicities. Ordinary transversality alone
does not resolve this obligation or rule out an ordinary positive collision.

## 5. Prioritized bounded research tasks

The following are proposed investigations. None is claimed to supply the
missing implication. Each should end in a proved signed input or a precise
method-specific obstruction.

1. **Test the threshold jet sign conditioned on an actual candidate.**
   Start on one specified closed subinterval of \(\kappa\in[1,2]\), at
   the complete cutoff or \(K_v\). Keep the genuine common height and
   impose both paid value/derivative candidate conditions. Seek a relation
   among the signed second, third, and fourth jets that forces (10), rather
   than bounding each jet separately. Pay the normalizer term \(\gamma\)
   and every product with the measured \(\Delta\); the existing uniform
   vanishing-error ledger is available. Success is a strict negative margin larger
   than that payment at all candidates in the chosen region. A failure
   result should identify an actual-phase finite-core configuration allowed
   by the candidate thresholds, or show exactly where the proposed signed
   relation loses its margin. A positive absolute upper bound is not such
   a relation.

2. **Derive one correlated transformation for a macroscopic genuine block.**
   Choose a fixed relative block, for example \(\nu N<n\le N\) with
   a specified \(0<\nu<1\), and keep its actual logarithmic phase and
   heat weight. Derive one explicit summation transformation and retain its
   complex derivative multipliers and its correlations with the remaining
   core. The target is a conditional signed contribution to (8) or (10),
   not another triangle-summed block upper bound. Pay endpoint terms,
   transformed remainders, drift terms, and the shared analytic error before
   making a sign claim; use fixed-time raw derivatives. Success is one
   useful uniform inequality after recombining the complete sum. Failure is
   a printed transformed adverse term or remainder that is too large at the
   required collision margin. Neither the adjacent-packet example nor the
   multiplicative-twist construction answers this actual-orbit question.

3. **Investigate a collision-conditioned local-to-average transfer.**
   Keep the complete physical derivative in (5) and impose
   \(Q_t(x)=Q_t'(x)=0\). Seek a signed arithmetic control of its nearby
   growth or of a correlated translated-probe integral. All changing phases,
   cutoff corrections, and higher derivative remainders must be paid.
   A sufficient success criterion is a candidate-conditioned mean-square
   upper bound strictly below \(1/8\) on a range where (5) applies, or a
   new paid local average on a much shorter range. For comparison, a pure
   curvature argument on \(H_d\) would require
   \(M_2<\sqrt{3/32}\,L/H_d\), vastly stronger than the present absolute
   budget. Failure should retain the quantitative gap (7), or identify the
   actual adverse correlation preventing the new conditional estimate.
   Improving only the constant \(D\) cannot close its exponential gap.

4. **Pay and test the first nonvacuous higher-multiplicity cases.**
   Treat exact multiplicities three and four first, using (11) and the
   candidate vanishing of the preceding jets. Print the fifth- and
   sixth-derivative multipliers and their signed-tail variation bounds
   before using them. The complete analytic payment remains
   \(j!\eta_NL^j\); each quadratic expression needs its own measured
   product payment. Success is a strict paid opposite sign, a genuine
   arithmetic restriction eliminating one of these multiplicities, or a
   proved multiplicity bound adequate for a later finite hierarchy. Failure
   is a compatible paid actual-phase configuration or a quantified loss in
   the proposed higher-jet estimate. The quartic example warns that the
   deflated real-root inequality alone cannot be the eliminating input.

5. **Prepare the coverage ledger before an endpoint claim.**
   Make a bounded map of the regions reached by a successful local signed
   theorem: the present shrinking sector, fixed positive-time large-height
   localization, compact height/time regions, and the uncovered transitions.
   Record the exact overlap hypotheses and error margins; do not assign an
   effective value to an unprinted counting constant. Any compact arithmetic
   certificate should be aimed at a specific remaining candidate region and
   pay value, derivative, cutoff, and complex-neighborhood errors. Success
   for this task is a complete, checkable list of what is covered and the
   precise additional estimates needed. An RH conclusion would require that
   this list eventually contain no possible positive threshold collision,
   including higher multiplicities. A broad zero grid without that analytic
   interface would not meet the checkpoint.

## 6. Evidence, records, and review status

The three continuation reviews are
[the signed shrinking-time review](../../reviews/HEAT_SIGNED_SHRINKING_COLLISION_REVIEW_20261009.md),
[the genuine signed-input review](../../reviews/HEAT_GENUINE_SIGNED_INPUT_REVIEW_20261009.md),
and [the local-jet and derivative review](../../reviews/HEAT_LOCAL_JET_AND_DERIVATIVE_INPUT_REVIEW_20261009.md).
They state the imported inputs, uniformity ranges, error ledgers, and limits
of each mechanism. Earlier numerical and attraction results retain their
separate conditional and positive-bound scope in the manuscript.

Three small exact checkers accompany this continuation:

| Checker and retained record | Passing assertions | What the checks support |
| --- | ---: | --- |
| [Signed vector checker](../../numerics/check_signed_heat_collision_scout.py), [record](../../numerics/signed_heat_collision_scout_record_20261009.json) | 3,930 | Finite signed-kernel identities, signing and partition invariants, scalar error reserves, and exponent identities. |
| [Genuine input checker](../../numerics/check_genuine_signed_heat_input.py), [record](../../numerics/genuine_signed_heat_input_record_20261009.json) | 186,693 | Finite edge and contraction reserves, surveyed rational hull data, cyclic partitions, isolated primes, and formal prime-exponent orthogonality. |
| [Local-jet checker](../../numerics/check_local_heat_jet_input.py), [record](../../numerics/local_heat_jet_input_record_20261009.json) | 2,386 | Normalized-jet and heat identities, finite real-root deflation models, complete perturbation payments, and scalar/exponent reserves. |

The reviews report byte-identical fresh runs and source-hash bindings for the
retained records. These are reproducible finite checks, not numerical
evaluations of the genuine heat function at huge height. They do not certify
the imported analytic theorems, prime asymptotics, canonical products,
uniform limits, actual-phase signs, collision exclusion, or RH. Their
assertion counts are not independent evidence for the missing analytic
implication. Specialist mathematical review and a separate literature review
remain necessary before treating these continuation results as independently
validated or claiming novelty.
