# Review of the ideal discrepancy and signed packet milestone

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This record combines coordinating derivations and separate same-model agent
audits. It is internal mathematical review, not independent specialist
validation or formal proof replay.

## Conclusion

The milestone supplies an exact mixed-discrepancy interface, a new controlled
sector of the actual signed adaptive tail, and a stronger obstruction that
survives complete recombination by total ideal. It does not prove the full
tail moment, a stronger zero-free strip, or quasi-RH implies RH.

The reviewed working tree is based on repository HEAD
`480581447dcd3e93c9c2f9c22a050d9c5100ff9d`. The existing manuscript is unchanged;
its SHA-256 is
`4872eb5e46a763750c63f5edf2dd7b904293dfa186b249759b3404545afb85ca`.
Earlier uncommitted research is preserved. No snapshot folder or new commit
is created for this milestone.

## Mathematical scope

| Record | Checked deduction | Remaining limitation |
| --- | --- | --- |
| [Ideal mixed discrepancy](../short_families/notes/14_SHORT_FAMILY_IDEAL_MIXED_DISCREPANCY_20261008.md) | Logarithmic derivation introduces an ideal von Mangoldt factor exactly; centered Stieltjes and capped Riesz formulas retain both boundaries, the unit, density and low/high edges | No signed power bound for the surviving complete functional |
| [Divisor packet cancellation](../short_families/notes/15_SHORT_FAMILY_DIVISOR_PACKET_CANCELLATION_20261008.md) | Certain (bqr), with nonunit small (b), have exact coefficient zero; a growing family has arbitrary power decay under the complete Schwartz weight | Unit-cofactor semiprimes survive; this is a selected controlled sector |
| [Product barrier](../short_families/notes/16_SHORT_FAMILY_PRODUCT_BARRIER_20261008.md) | The full (Omega\le2) product sector remains oversized for every nonzero fixed smooth complex profile; pure prime powers are affordable | Lower bound is for the selected amplitude, with full-tail cross terms retained |

### Exact mixed discrepancy

The ideal identity

\[
 (\mu_K\lambda_u)*(\Lambda_K\lambda_u)
 =-\mu_K\lambda_u\log N
\]

holds with overlaps and deletion zeros. In the logarithmic bridge, the
first truncation is on the whole product (ab), not separately on (a,b).
The principal von Mangoldt density is one, whereas the free ideal sum has
residue (\kappa_u); the review checked this distinction through the
logarithmic derivative. A zero-integral free profile does not remove this
separate density term.

The Stieltjes increment excludes the lower atom and includes the upper atom.
The Riesz closure contains both low/full and full/low edges with their
intersection subtracted once. Its two partial summations retain their
boundary terms. The review made explicit that an interval with (A\ge B)
is empty and that the fixed-row detector assertion assumes (\int W=0).
No fixed-row bound is silently made uniform in conductors.

At (h=a=2/5,\theta=1/40), the concrete choice (U=V=D^{1/50})
makes the low/low piece empty on (Nu\le D^{17/40}), since

\[
 UVz\asymp D^{27/50},\qquad Y_u\gg D^{11/20}.
\]

The margin is (1/100). The high/high term and both low/high edges remain.

### Divisor packet cancellation

The review recomputed the exact coefficient

\[
 t_{z,Y}(n)=-\sum_{d\mid n,\,Nd>Y}c_z(d).
\]

Under the stated packet conditions, the surviving divisors of (bqr)
are exactly (qre), (e\mid b). The prime (r) cannot share a truncated
factor with a prime of (b), while (q) can carry every divisor of (b).
Thus (c_z(qre)=2\mu_K(e)), including zero for nonsquarefree (e), and

\[
 t_{z,Y}(bqr)=-2\sum_{e\mid b}\mu_K(e)=0\quad(b\ne1).
\]

This takes place within the actual response before squaring; common complex
phases and masks are retained. It is stronger than removing a selected
factor tuple by an absolute estimate.

For (1<Nb\le D^{1/40-\delta}), the cancellation is uniform on the
enlarged row ball (Nu\le D^{17/40}). The review checked the strict
exponent margins against all fixed constants. The uniform (D\log^2 D)
majorant and Schwartz lattice tail then give arbitrary power decay for the
projected packet under the full row weight. It is legitimate to subtract
that complete response vector by the weighted triangle inequality.

The opposite branches at fixed prime (b=p) each have selected energy

\[
 \gg_{W,p,\Phi}DH^{1/6}/\log^4D,
\]

using the same narrow prime windows and coherent rows avoiding (p).
The fixed-cofactor dependence is recorded. Their sum is exactly zero.
This illustration does not lower-bound an unrestricted complex branch sum.

### The surviving product barrier

After every tuple with the same total ideal has been included, the
(\Omega\le2) sector on inner rows is exactly the negative ordered
prime-pair sum, including the square diagonal. The continuum kernel is

\[
 F_B(v)=\frac2{2B-v}\log\frac B{B-v},\qquad
 B=\log z,\quad v=\log(C/t).
\]

Its power series has positive coefficients at all orders (v^k/B^{k+1}),
(k\ge1). Polynomial approximation to (\overline f/v) on a compact
interval away from zero proves that a nonzero fixed complex profile has a
first nonzero positive logarithmic moment. Quantitative prime counting
therefore gives a finite leading logarithmic order. Coherent rows force
selected energy (\gg DH^{1/6}/\log^{2k_0+2}D), still exceeding the
useful (D^{4/5+\varepsilon}) test budget by (4/15) in power.

This is not a lower bound for the full tail. The cross term with the
(\Omega\ge3) response can compensate it and must remain inside the
square. The result concerns fixed profiles; it does not analyze profiles
whose order or shape varies with (D). Genuine prime powers have full
weighted energy (O_\varepsilon(HD^\varepsilon)), too small even
pointwise on coherent rows to provide the leading compensation. The
prime-only tail is confined to a negligible Schwartz row range.

## Imported inputs

The conductor comparison, character presentation and zero extension are
inherited from the manuscript and its referenced arithmetic sources. Free
sum completion is used only with the qualifications already recorded there.
No new conductor-uniform Möbius or Hecke prime estimate is imported.

The branch-size illustration and product barrier use the previously imported
fixed-field quantitative prime ideal theorem. The statement of
[Das--Kadiri--Ng, Corollary 1.4](https://arxiv.org/html/2508.09480v1)
was checked again; a possible fixed exceptional-zero term is absorbed for
sufficiently large (D). Its proof is not replayed. The local packet theorem
and its full Schwartz controlled-sector estimate do not require prime
asymptotics. The integer complete-functional error bound is not transferred
to ideals without proof.

## Reproducibility

All scripts use only the Python standard library, print deterministic JSON
and write no files. Two fresh coordinating runs reproduced each retained
record byte-for-byte.

| Checker and record | Passing finite checks | Scope |
| --- | --- | --- |
| [Ideal discrepancy](../numerics/check_short_family_ideal_discrepancy.py), [record](../numerics/short_family_ideal_discrepancy_record_20261008.json) | 638 named equalities, including 16 discrepancy integrals and 96 centered Stieltjes cases | Formal ideal monoid, complex sixth-root phases, formal logarithms, exact cutoff and Riesz algebra |
| [Divisor packets](../numerics/check_short_family_divisor_packets.py), [record](../numerics/short_family_divisor_packet_record_20261008.json) | 3,982 assertions in 22 groups | Tuple/product recombination, nonsquarefree cofactors, deletion zeros, boundaries, rational budgets, and actual local split-prime sextic symbols |
| [Product barrier](../numerics/check_short_family_product_barrier.py), [record](../numerics/short_family_product_barrier_record_20261008.json) | 182 assertions in ten groups | Four coefficient cases, series coefficients, partial fractions, polynomial derivative moments, and rational exponents |

The product checker initially used a wrong extraction expression that agreed
at the selected point. Separate review caught it; the checker now uses the
manuscript's ((1+a)/2+5h/12) and tests two further parameter pairs. The
resulting (13/15) value is unchanged.

The local-symbol packet example uses a good-radical proxy, not a computation
of its inducing primitive conductor, and tests the local theorem rather than
membership in the asymptotic growing-cofactor family. The polynomial bump
tests finite calculus; it is not a smooth analytic profile. None of the
records proves reciprocity, Poisson, prime ideal asymptotics, the density
argument for every profile, an asymptotic signed moment, or RH. All files
remain small and comply with the repository's large-file convention.

## Next analytic obligation

At the test point, remove the complete negligible packet vector and seek

\[
 \frac1D\sum_{u\ne0}\Phi(Nu/D^{2/5})
 \left|T_{u,W}(D)-\mathcal P_{u,W}(D)\right|^2
 \ll_{\varepsilon,W,\Phi}D^{4/5+\varepsilon}
\]

for the detecting zero-integral profiles and required twists. The exact
mixed-discrepancy formulation is an interface for this remaining task, not
an additional assumption that makes it automatic. The first bounded test
should retain high/high and both low/high terms together at the displayed
cutoffs, and expose the cross-total-product compensation with the actual
semiprime response. A separate positive majorant for every surviving product
sector cannot meet the budget proved impossible above.
