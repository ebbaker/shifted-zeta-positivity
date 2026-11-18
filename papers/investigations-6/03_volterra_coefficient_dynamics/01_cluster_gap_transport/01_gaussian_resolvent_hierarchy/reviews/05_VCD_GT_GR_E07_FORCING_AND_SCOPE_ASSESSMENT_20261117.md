# VCD-GT-GR-E07 r1 — Forcing transfer, transport and scalar scope

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Requested helper configuration
**gpt-6.1-sol / ultra**. Actual serving model and reasoning effort were
unavailable to this assessor. Separate-agent internal assessment with
shared premises. [Frozen request][request] · [Shared premises05][shared]

**E06 and E10 accepted within their frozen scopes.** E06 proves a
quantitative approximation, a conditional transport comparison and two
fixed-slice witnesses. E10 proves a limit on the specified scalar
relaxation. Both compare with a direct evaluator supplied the same data.
[E06][e06] · [E10][e10] · [Result index][results] · [Avoid index][avoid] ·
[Classification01][class] · [Scope07][scope]

## Fixed-physical-scale forcing and conditional cost

The collar gives \(\lvert w^2-D\rvert\ge(15/16)|w|^2\), including
negative \(D\) and \(D=0\). In the normalized occurrence sum the near
bound is \(4C_{\rm u}(q_0/a^2)^pL\), and the two horizontal shells cost
at most \(2C_{\rm u}q_0^p L^{-2p}(4L+3)\). Since \(L\ge3\) and
\(a\le L\), these give the stated \(B_p L\). The shell bounds also
pay all tails uniformly on the paid tube at fixed \(T\). Conjugate
occurrences pair to give real weighted and unweighted moments.
For physical \(s>0\), \(\Re w^2\ge-1\) in the strip, so the
occurrence-wise integral for \(1-e^{-sw^2}\) costs
\(se^s q_0|w^2-D|\). In the radial case it costs \(sq_0|w^2-D|\).
The resulting first and second absolute moment sums have prefactors
\(\ell^4\) and \(\ell^4|D|\). Their normalizations give the common
factor \(L^{-1}\) in (2). The implied constant depends on the
specified scale and collar parameters. [E06 §1][e06] · [Note41 §3][n41]

An upper bound \(F_s\le Q\) on the entire paid tube gives
\(\dot m\ge2m^2-(Q+\epsilon_s)\). The finite barrier uses
\(K_+=\max(Q+\epsilon_s,0)\), makes the loss of favorable drift
explicit when \(Q+\epsilon_s<0\), and retains \(v(0)=-A_0=-B_1L\).
Indeed \(f''=2K_+ f\), \(f(0)=1\), \(f'(0)=2A_0\), and \(f\)
is positive and nondecreasing. Then \(v=-f'/2f\) solves the
comparison equation, and an integrating factor gives \(m\ge v\).
The positive-time coth bound (or \(-1/(2\sigma)\) at \(K_+=0\))
leaves the finite initial bound intact. Integration gives
\(\int_x^y(-m)_+\le \frac12\log(f(y)/f(x))\) and
\(W(x,y)\le(f(y)/f(x))^2\). [E06 §§1–2][e06] · [Note41 §4][n41]

The Wronskian of \(f(u)\) and \(g(u-x)\) is \(f(x)\), since
\(g(0)=0\) and \(g'(0)=1\). Consequently
\(\int_x^y f(u)^{-2}\,du=g(y-x)/(f(x)f(y))\); multiplying by
\(f(y)^2\) gives the claimed bound on \(\int_x^y W(u,y)\,du\).
The cost to compare with a terminal \(\delta(y)\) is **twice**
that integral. The physical \(D\) cost carries the extra \(\ell^2\),
since \(m\,d\sigma=M\,dt\). The exact backward margin equals
\(W(x,y)\delta(x)\), so margin equality permits \(\delta(x)=0\)
at \(x=0\) as well as at any other paid endpoint. Equality with
the upper cost allowance yields nonnegativity. Tube persistence
and the terminal anchor for backward inference are separate
inputs. The forward estimate likewise uses its own initial
\(\delta(x)\). [E06 §2][e06] · [Normalization08][normal]

## Fixed-slice witnesses

Both bands are erased with full multiplicities. The remaining entire
quotient and reflected insertions preserve real evenness and the
strip. Polynomial division outside a large disk and finite-degree
multiplication give order at most one for each fixed \(c\). The
positive-horizontal count forces order at least one by applying
Jensen to a disk of twice the radius containing those occurrences.
Each band loses at most \(12C_{\rm u}L\) and gains at most \(5L\).
Any unit interval meeting inserted occurrences has
\(\log(2+|v|)\ge L\) for its start \(v\) and meets only one band.
Thus \(C_{\rm u}+5\) works uniformly. Cumulative positive counts
change only for \(X\ge c-3\), by at most
\((12C_{\rm u}+5)L\le(24C_{\rm u}+10)\log(2+X)\), including cuts
inside the band. The safe-line change is a signed sum of at most
\((24C_{\rm u}+10)L\) reciprocal terms. Vertical distance at least
three for \(|v|\ge c/2\) and horizontal distance at least \(c/3\)
otherwise justify the stated enlarged constant. Exact equality of
the projected counting measures is unnecessary. [E06 §3][e06] ·
[Note34 §§1–2][n34]

For the broad positive-height density, added nonreal occurrences
require \(c\in[U,2U]\). When (i) contributes, \(v<8/L\),
\(L/2\le\log U\le2L\) and \(U\ge8\), so
\(U\log U\,e^{-\beta v\log U}\ge4L e^{-16\beta}\) pays at most
\(3L\) additions after enlarging \(B_\beta\). In (ii) the two
additions require \(v<1/2\), and
\(U^{1-\beta v}\log U\ge 8^{1-\beta/2}\log8>2\).
Reflection gives the negative-height counterpart. The dyadic layer
cake and the static local covering and Hölder argument give the
claimed second and averaged higher moment bounds with the enlarged
constants. In the local argument the large-height cover has total
coefficient at most \(5\) times the new density constant, and the
small-height cover uses \(6(C_{\rm u}+5)16^\beta\).
These are spatial bounds at a slice. [E06 §3][e06] · [TND-O Note21 §6][density]

The surviving background has \(|\Re w|>3\) and costs at most
\(10C_{\rm u}L\) in every absolute inverse power \(k\ge2\).
All opposite-band insertions, including the reflected targets,
add at most \(5Lc^{-k}\). In (i), \(2N\) positive and \(2N+2\)
negative occurrences of \(\mu\) with magnitude \(b^{-2}\)
give the stated \(m\) and \(F\), with the complete tail errors
\(O(L^{-1})\) and \(O(L^{-3})\). The odd core for \(\tau_2\) cancels
in opposite displacements, leaving \(O(L^{-2})\) from \(k=3\).
The \(s_2\) law evaluated on these moments supplies an algebraic
right side at the slice. The time derivative law applies on the
paid canonical or established finite-polynomial heat domains.
[E06 §§3–4][e06] · [E02][e02]

In (ii), the two core terms give \(32e^{s/4}\) to \(G_{s,2}\).
All other terms have \(\Re w^2\ge8\), and their full \(k=4\)
sum is \(O(L)\) before weighting. Thus the holomorphic tail
is \(O(Le^{-8s})\), the radial tail is \(O(Le^{-9s})\), and the
unweighted \(S_2\) is \(32+O(L)\). At \(s=\alpha L^2\) the actual
normalized leading term \(384L^{-4}e^{\alpha L^2/4}\) cancels
against the opposite leading term of the retained complement,
leaving \(F=O(L^{-3})\). The cancellation is exhibited by the two
actual terms. The changed fields supply no common-time canonical
tube or estimate from below for canonical Gaussian amplification.
[E06 §4][e06] · [Joint bounds12][joint]

## Scalar equilibrium and remaining signed input

With \(h=\gamma\sqrt L\), the nonzero terms in \(\dot s_2\)
are \(-4h^3/3-h^3/18+4\tau^2\), so the equilibrium requires
\(\tau^2=25h^3/72\). The forcing is \(2h^2\), and
\(\delta=-1/(2h)\) gives \(4m\delta=2\). The bounds on \(\gamma\)
pay \(s_2\le B_2L\) and \(F\le KL\). The thresholds on \(L\) pay
\(\gamma\sqrt L\le BL\), \(1/(2\gamma\sqrt L)\le d\), and
\(5\gamma^{3/2} L^{3/4}/(6\sqrt2)\le B_\tau L\).
The \(s_3,s_4\) envelopes and all time moduli on the displayed
scalars follow from their zero values or constant time dependence.
For \(\Delta>0\) the exact \(W=e^{4h\Delta}\) and
\(C=(W-1)/(2h)\) give margin \(-W/(2h)\) and rule out improving
the height exponent using those scalar equations and envelopes
alone. The example has a negative terminal gap and supplies no
realized divisor or common-time canonical family. The paid
positive-anchor class and the full Gaussian time equations are
outside this exclusion. [E10 §§1–3][e10]

The documentary screen uses [E01][e01] and [Controls12][controls].
Euler-factor changes fail unchanged theta arithmetic and the
documented endpoint discrepancy. Weighted-square, finite-source,
finite-score and finite-prime controls fail full reflected unit-weight
theta equality, and the documented endpoint-defective subclasses
fail the strip. The reflected super-Gaussian fails the order bound.
Smooth and positive-primitive controls change theta arithmetic.
Atomic and finite-type controls lack the growing count, and the
RH-conditional mergers change ordinary Dirichlet arithmetic.
Changed observations lose the physical readout, and fractional
profiles lack the integer divisor. Quadratic and quartic heat
controls lack the growing count; the static surgery examples keep
coarse counts but change the source and lack the common-time tube.
The scalar equilibrium only imposes the four scalar relations.
[Premises02][premises] · [Scope07][scope]

Forcing transfer provides no bound on the retained signed observable.
An equally informed direct calculation can use the same complete
observations, tube and anchor, apply the same comparison and integrate
the scalar equilibrium exactly. There is no unconditional improvement
of the inherited \(O(\sqrt L)\) negative-side allowance after a fixed
scaled buffer or the \(O(L)\exp(O(\sqrt L))\) multiplier bound on a
fixed scaled interval. The pointwise input still needed is a
source-sensitive signed upper bound on the complete
\(12s_2+16\delta s_3\) on the paid canonical tube, or on the
fixed-physical-scale signed \(F_s\) with the full complementary error
added. A uniform \(Q=o(L)\) suffices for an improved height exponent
through this comparison. An integrated route would have to bound
the complete transport multiplier or its actual cost on the same
tube. Backward gap inference requires an independently paid terminal
gap that meets the full cost. [E06 §2][e06] · [E10 §2][e10] ·
[Note41 §4][n41]

One proof pass and one bounded correction check completed. Both E07
proof hashes, the six E06 inherited-input hashes and the E10 decision
hash matched. The recheck covered the Wronskian and factor of two,
the broad cover constants and the scalar thresholds. No required
proof correction was found.

[request]: ../research-progress/handoffs/VCD-GT-GR-E07-r1.md
[e06]: ../notes/05_VCD_GT_GR_E06_FORCING_TRANSFER_AND_COST_20261117.md
[e10]: ../notes/06_VCD_GT_GR_E10_SCALAR_ENVELOPE_LIMIT_20261117.md
[e02]: ../notes/02_VCD_GT_GR_E02_CANONICAL_MOMENTS_20261117.md
[e01]: 02_VCD_GT_GR_E01_INPUT_AUDIT_20261117.md#scope-at-the-return-gate
[n34]: ../../notes/34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[density]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md#6-local-moments-of-every-order-uniformly-in-time
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[shared]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[normal]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
