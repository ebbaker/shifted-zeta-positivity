# Squarefree reduction and cofactor compensation: scoped review

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model audits are internal checks, not independent specialist
validation or formal proof replay.

## Main conclusion

[Note 17](../short_families/notes/17_SHORT_FAMILY_SQUAREFREE_TAIL_REDUCTION_20261008.md)
proves, under the manuscript's existing imported analytic package,

\[
 \mathcal E_{\rm nsq}^{(\theta)}(D,H)
 \ll_\varepsilon D^\varepsilon
 \min\{HD^{1-\theta},D^{-\theta/2}B(D,H)\},
\]

where \(B(D,H)=H+DH^{1/6}+H^{5/6}D^{1/3}+H^{1/3}D^{5/6}\).
At \(H=D^{2/5}\), \(\theta=11/20\), the sparse bound is
\(D^{19/24+\varepsilon}\), below \(D^{4/5}\) by a power of \(1/120\).
This controls the **whole nonsquarefree total-product sector**. The full
moment and its squarefree residual remain unproved. In particular it does
not establish a full-family exponent at \(h=2/5\), an improved scalar
Möbius bound, or a new zero-free boundary.

The coordinating derivation and two separate audits checked the following
points in the analytic proof:

- The original Möbius amplitude has zero nonsquarefree projection, giving
  the pointwise relation \(T_{\rm nsq}=-I_{\rm nsq}\).
- Square-divisor inclusion–exclusion retains arbitrary overlaps; its free
  factor is scaled by \(j=k^2/(k^2,d)\), with every deletion zero intact.
- Small square roots are negligible by the all-scale masked completion
  and radical-weighted row mass, with the completion order chosen after
  the positive cutoff gap.
- Fixed binary intervals handle the adaptive divisor prefix. Their
  coefficient vectors are fixed before applying the physical operator;
  no arithmetic row selector is inserted into a completed kernel.
- In \(n=\ell^6n_0\), the auxiliary Möbius variable is squarefree, so
  \((k/(k,\ell))^2\mid n_0\). The sparse column count and convergent
  weighted \(\ell\)-sum give \(B(D,H)/R\).
- Equality belongs to the small sides of both cutoffs. Arbitrarily small
  epsilon losses absorb the strict choice \(R<D^{\theta/2}\).

The new cutoff differs from the packet theorem's \(\theta=1/40\).
Projected sectors cannot be transferred between these representations
merely because the full response vectors are close. After the justified
squarefree reduction, the three factors are pairwise coprime, and the
remaining free-factor sum has acquired restrictions. The original free
completion cannot be applied to it unchanged. The coefficient \(+2\) for
balanced semiprimes requires \(1\le Y_u<\min(Nq,Nr)\); if \(Y_u<1\)
their coefficient is instead \(+1\). These exceptional rows are negligible
at the stated parameters by the full Schwartz weight.

## Supporting compensation results

[Note 18](../short_families/notes/18_SHORT_FAMILY_COFACTOR_COMPENSATION_20261008.md)
proves an actual selected-factor block negligible in full weighted norm.
If the selected factor is at least \(C_0D/z\), the complete cofactor
Möbius inverse vanishes pointwise. Its adaptive tail equals minus the
small-product sum, to which the existing completion applies. Bounded
row-dependent selectors are allowed in this finite coefficient sum.
The illustration of oversized prime pieces explicitly specializes to
\(\nu=1\). Their compensation must cross different total products on
coherent rows. The controlled interval has constant relative width and is
equivalent to an asymmetric change of factor cutoffs; it supplies no new
power-width estimate for the full residual.

[Note 19](../short_families/notes/19_SHORT_FAMILY_EDGE_COMPENSATION_20261008.md)
keeps both low/high edges of the logarithmic bridge. On each nonunit
divisor packet their coefficients are exactly \(-2LJ_b(L)\) and
\(+2LJ_b(L)\), with

\[
 J_b(L)=\int_0^\infty e^{-Lt}\prod_{p\mid b}(1-e^{-t\log Np})\,dt>0.
\]

The positive formula and its sharp fixed-cofactor asymptotic concern a
single packet. They give neither a positive sign across different total
products nor a renewal contraction. Lower bounds apply to selected pieces
with trivial twist, and cannot be promoted to lower bounds for a full edge
or the full tail. The unit-cofactor exception remains explicit.

## Finite replay

Two fresh coordinating runs of each standard-library checker reproduced
the saved JSON record byte-for-byte. These are finite diagnostics, not
certificates of the analytic theorem.

| Checker and record | Result | Scope |
| --- | --- | --- |
| [Squarefree projection](../numerics/check_short_family_squarefree_projection.py), [record](../numerics/short_family_squarefree_projection_record_20261008.json) | 594,360 exact assertions passed | Distinct equal-norm ideal symbols, overlaps, projection signs, sixth-root phases and zeros, cutoff boundaries, sparse witnesses and binary-prefix regrouping |
| [Cofactor inverse](../numerics/check_short_family_cofactor_compensation.py), [record](../numerics/short_family_cofactor_compensation_record_20261008.json) | 18,442 exact assertions passed | Complete cofactor inversion, adaptive split, selectors, complex phases and asymmetric convolution identity |
| [Opposing edges](../numerics/check_short_family_edge_compensation.py), [record](../numerics/short_family_edge_compensation_record_20261008.json) | Five packets; 17 tail divisors, 52 triple terms, 208 phase/deletion checks and 24 rational-log cases passed | All four edge classifications, nonsquarefree cofactors, weak endpoints, unit exception and formal logarithmic identities |

The records' SHA-256 values are respectively
`f3f5768c4a40a207276e9197daf6512f10a1a4b7acd4cd33bdf5597653ebebad`,
`8d3a48a76a835de189e4e3ff041df55fc0713a89e525668e534b50f801c281bb`,
and `3ac3d7a0f7be60030d3133bbe89590d931a2d5b0b83cd84ced0130ea92b96527`.
They identify the retained finite records; no proof step depends on a hash.

The finite models do not validate physical reciprocity, primitive conductor
comparison, Poisson, infinite Euler convergence, ideal counting, prime ideal
asymptotics, the imported de Faveri sieve, or an unbounded signed moment.
The deep inputs retain their manuscript source status. No new Möbius PNT,
conductor-uniform reciprocal bound, or zero-free hypothesis is used in the
main sector theorem.

## Manuscript incorporation

The main sector theorem, its proof and the squarefree-residual corollary are
incorporated in the existing
[manuscript](../short_families/short_family_reductions.tex). The supporting
cofactor and edge refinements remain in their linked research notes.
The desktop editor's native compiler returned success for the saved source.
Final manuscript SHA-256: `373014701a7fa9cdc1562f60c8d10aedc01b2147031c1a0fda4a1453808813dc`.
Static checks found 121 unique labels, 106 resolved references and 18
bibliography entries, with every citation resolved. Research links resolve;
all sixteen files in this addition are below 100 KB and contain no control
characters or trailing spaces. No replacement document, separate PDF,
snapshot folder or new Git commit was created.
