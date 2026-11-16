# VCD-E11 r1 assessment of smooth next-defect freedom

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance. Recorded assessment dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable. The assessment
worker is separate from the E10 author, worked on E07, and shares the
proof worker's dispatched model and inherited sources. This is an
internal LLM assessment under [avoid 05][a05]. No specialist review
was conducted.

**Accepted without mathematical correction in the stated class.** All
six [E11 input hashes][request] and all four [E10 prerequisite hashes][e10req]
match. The disposition applies to [Note 10][proof] at SHA-256
`4ac3829a49f7e37136007bfc32b4810802a992667985e283bacbc2fa1deb32b4`
and to the matching [E10 return][e10return]. The [result index][results],
[catalog][catalog] and [avoid index][avoid] retain the distinction between
a finite information obstruction and a zero theorem.

## Functional tests and scaling

The \(N+1\) even moments and \(N-1\) lower adjacent score tests give
\(2N\) real constraints at \(\lambda=0\). Restriction to positive-half-line
bumps loses none of the tested information because \(V'\) and each
\(q_jq_{j-1}\) are odd, so their product is even. Equality of the
functionals on every bump implies equality of their continuous
integrands at every positive point, by strict positivity of the theta
density. The target product has degree \(2N-1\) with nonzero leading
coefficient, above the degrees of all lower adjacent products. Any
linear dependence would consequently give \(V'Q=P\) with
\(\deg Q=2N-1\), \(\deg P\le2N\), contrary to the exponential score
asymptotic in [E06 §2][e06]. The quotient argument through the image of
the finite constraint map works without assuming its rows are
independent. The smooth even bump direction can therefore satisfy every
constraint while its target is nonzero. For \(N=1\), the lower score
list is empty and the same degree argument applies.

The compact multiplier is identically one near zero and on both tails.
The condition \(|\epsilon|\|h\|_\infty<1/2\) ensures strict positivity
for either sign of \(\epsilon\). The zeroth moment preserves the
unnormalized mass, so \((1+\epsilon h)\mu\) is the stated probability.
Evenness supplies all odd moments. Matching the even moments through
\(2N\) fixes the full Gram matrix on degrees through \(N\), hence fixes
each \(q_j\) and the links through \(a_N=\kappa_{N-1}/\kappa_N\). The
unchanged canonical score in the common basis gives the exact difference
\(e_j=\epsilon a_j L_j(h)\). This vanishes below \(N\). Both nonzero
signs at \(N\) are available with the same retained data. The proof
requires no quantitative lower bound on \(|L_N(h)|\) or uniform choice
of \(h\) as \(N\) grows.

## Envelope and source class

The change in the logarithmic score is
\(-\epsilon h'/(1+\epsilon h)\), uniformly bounded by
\(2|\epsilon|\|h'\|_\infty\). Adding a common heat tilt adds
\(-2\lambda u\) to both scores. In the confinement argument in
[manuscript §4][ms], the canonical slack for \(|u|\le1/2\) is at least
\(-27/4+11-4=1/4\). For \(|u|\ge1/2\) it is at least
\(e^{4|u|}-\cosh(4u)+11=11+\sinh(4|u|)\).
The score change after multiplication by \(u\) is bounded by
\(2|\epsilon|\|u h'\|_\infty\). Taking that bound below \(1/4\) preserves
the same confinement inequality simultaneously for
\(0\le\lambda\le1/2\). The common tails and compact smooth modification
satisfy all integrability and boundary hypotheses of the confinement
lemma, so the unchanged coefficient envelope follows. Both conditions
on \(|\epsilon|\) allow arbitrarily small nonzero values of either sign.

For the constant square-coefficient representation, the ratio bound
in [Note 10 §2][proof] follows from
\(j^4\le 2j^4-3j^2/\rho\le 2j^4\) for \(j\ge1\), \(\rho\ge\pi>3\).
For \(m>k\) the exponential ratio decreases with \(\rho\). The ratio
at \(u\ge u_0\) is therefore bounded by four times its value at \(u_0\),
and tends to zero at infinity. Absolute convergence of the proposed
series and the theta series at \(u_0\) permits dominated convergence
after division by \(s_k\), where \(k\) is the first changed coefficient.
The limit \(b_k-1\ne0\) contradicts agreement on the tail. If all
coefficients are one, the series gives theta everywhere, contrary to
the nonzero bump. This verifies failure of the specified representation
with the same modes, constant coefficients, and absolute convergence
at one positive point. In particular it applies to positive
coefficients in a pointwise convergent representation.

## Finite cut and scope

Under the retained lower defects, the odd products of degrees
\(1,3,\ldots,2N-3\) span the required odd tests. Parity adds the even
tests, so \(\mathcal D\) vanishes through degree \(2N-2\), including
for \(N=1\). The recurrence gives entrywise commutation with the
same signs as [E08 §2][e08]. Every retained defect entry vanishes by
the degree bound. Among \(E_{N,i},E_{i,N}\) for \(i<N\), only
\(E_{N,N-1}=E_{N-1,N}=e_N/a_N\) can be nonzero. That entry appears in the
two boundary terms with opposite signs, so the commutator supplies no
equation for it. The retained canonical-score compression equals the retained
derivative pairing, which is unchanged by moment equality. Its
finite-node term also agrees because \(J_N\) and the canonical symbol
are unchanged. Hence the retained correction of [E05][e05] is preserved.

The obstruction concerns exact propagation of the next canonical
defect from the specified finite data among positive smooth even
sources. Exact retained data are at time zero. The modification
preserves the full endpoint jet and literal Fourier observation,
while the complete square expansion fails in the class checked above.
[E07][e07] retains a positive square expansion and has a first
uncancelled odd endpoint. Its inherited nonreal-zero conclusion applies
to those finite-mode changes. E10's smooth control supplies no
Fourier-zero test or obstruction to a growing-degree confinement
argument using additional quantitative inputs. The [E07 screen][e07]
and the [scoped exclusions pattern][a07] delimit that comparison.
No mathematical correction or response is pending.

[request]: ../research-progress/handoffs/VCD-E11-r1.md
[e10req]: ../research-progress/handoffs/VCD-E10-r1.md
[e10return]: ../research-progress/handoffs/VCD-E10-r1-return.md
[proof]: ../notes/10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md
[e08]: ../notes/08_VCD_E08_FULL_SCORE_RIGIDITY_20261116.md#2-entrywise-commutation-and-the-cut
[e07]: ../notes/07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md
[e06]: ../notes/06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md#2-exponential-reference-with-an-explicit-bounded-error
[e05]: ../notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md
[ms]: ../manuscript/main.tex
[results]: ../../../../result-summaries/README.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
