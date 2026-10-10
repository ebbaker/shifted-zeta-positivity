# Internal review of the complete candidate-current atlas

10 October 2026. Model GPT-6.1-sol (Codex), configured reasoning effort
ultra, verified from the parent chat recording and inherited by delegated
work. These are internal derivation, interval replay and agent checks, not
independent mathematical review.

Reviewed [Note 4](../notes/4_CANDIDATE_CURRENT_ATLAS_AND_THIRTEEN_SIMPLE_ZERO_BRANCHES_20261010.md),
[the new checker](../numerics/check_candidate_current_atlas.py),
[its certificate](../numerics/CANDIDATE_CURRENT_ATLAS_CERTIFICATE_20261010.json)
and [its build record](../numerics/CANDIDATE_CURRENT_ATLAS_BUILD_RECORD_20261010.json).
The Note 2 and Note 3 sources and retained certificates remain preserved.

## Finite result and scope

The exact domain is
\[
 t_0=(2\log22066)^{-1}\le t\le1/20,\qquad
 x_0=4\pi22066^2\le x\le x_0+8.
\]
The atlas proves complete joint nonvanishing of genuine \(H_t,H_t'\),
and exactly thirteen simple genuine heat zeros at every allowed time.
The complete normalized pair has norm greater than 0.03728 uniformly on
the domain. Its 46 closed height strips cover the full exact time interval:
29 are value-pruned and 17 pass both the full paid current test and the
full paid physical derivative test. The minimum candidate current gap is
greater than 0.11934. The thirteen disjoint zero bands have strict opposite
all-time endpoint signs and one strict fully paid derivative sign each.

This result is finite. It gives no current sign uniform in height or
cutoff, no estimate uniform as time tends to zero, no paid threshold-jet
sign and no RH conclusion.

## Analytic checks

1. The exact time domain is distinguished from the slightly larger
   Decimal outer hull. The identity \(t_0(2\log M)=1\), together with
   monotonicity for \(h\ge0,t\ge t_0\), proves the sector lower edge.
   The remaining interval tests prove \(\kappa<2\), \(t\le1/20\),
   and a constant natural cutoff \(N=M=22066\). The endpoint \(1/20\)
   is included exactly.
2. Every genuine cutoff term enters the signed midpoint jets. The true
   carrier, amplitudes and quadratic logarithmic weight are retained.
   Forming the current after complete coherent summation includes all
   block, complement and cross interference. The signed real observation
   retains reflected phase information.
3. The degree-63 global polynomial uses a complete 64th absolute
   frequency moment. On the real height segment, modulus-one phase
   exponentials justify the Taylor bounds with no exponential penalty.
   Algebraic midpoint shifting changes the polynomial expression, not
   the underlying comparison function or its remainder.
4. The physical spatial residual is \(\gamma_n+i\delta_n/2\), retaining
   amplitude drift, carrier curvature and normalizer motion on the entire
   height hull. Both value and first-derivative residual errors are paid.
5. Time transport is at fixed physical height and integer cutoff. The
   phase part of \(\chi_n\) and the mixed multiplier
   \(\gamma_{n,t}+\gamma_n\chi_n\) are included. Both complete time
   budgets are multiplied by the outward upper time increment.
6. The full symmetric/reflected holomorphic disk interface remains the
   analytic input. Both \(\eta\) and \(L\eta\), with cutoff changes
   inside the disk already paid, are added to all genuine observation
   signs. An off-axis real-part formula is never used as a holomorphic
   extension.
7. Value pruning uses the necessary candidate tolerance \(|u|\le\eta/2\).
   Every unpruned strip passes the necessary derivative tolerance
   \(|u'|\le L\eta/2\) in reverse and the rectangular complete-current
   support test in reverse. Actual joint candidates cannot escape through
   a shared strip endpoint, since all intervals are closed.
8. Exact cell adjacency and total width check complete coverage. Every
   retained connected band is independently tested at both endpoints
   for all times; the derivative signs are consistent throughout each
   band. Strict monotonicity gives exactly one zero per band, and the
   value-pruned complement excludes additional zeros.
9. \(H_t=A_tQ_t\) with \(A_t>0\) transfers zeros and simplicity. At a
   zero, \(H_t'=A_tQ_t'\). The uniform lower bound for the normalized
   pair follows from the paid component margin of each cell. Smooth
   genuine heat dependence and the implicit-function theorem give the
   thirteen trapped branches across the certified time interval.
10. The reported Schwarz-Pick candidate quantity is consistent with
    Heat Note 18. The atlas acceptance rules do not depend on that newer
    refinement, so the earlier rectangular interface suffices for the
    finite theorem.

## Arithmetic, preservation and internal replay

The new source hash-checks the preserved Note 3 source before importing it.
The latter checks the preserved Note 2 interval source. A deliberate
substitute dependency containing executable failure code was rejected for
its hash mismatch before that code executed.

The arithmetic inherits 60-digit directed Decimal operations, explicit
Machin pi and reduced trigonometric Taylor enclosures, adjacent endpoints
for correctly rounded monotone logarithm/exponential, and the local
integer-power override using directed repeated multiplication. Sixty-three
rational midpoint-shift controls pass. No ordinary binary float enters a
certificate assertion.

The complete final interval build passed. A second internal agent read
the physical transport, polynomial and candidate-coverage derivations,
then independently checked the retained certificate with Decimal logical
assertions. It confirmed all 46 adjacent cells, 29 positive value gaps,
17 simultaneous positive derivative/current gaps, and all thirteen
all-time endpoint and monotonicity records. That agent then performed a
fresh full arithmetic replay; its final JSON was byte identical to the
retained certificate. These internal checks do not replace independent
mathematical review or formal proof verification.

All older source and certificate hashes match their preserved build
records. The new certificate is about 122 KB and needs no external archive.
The build record binds the source, both preserved dependencies and final
certificate. Hashes identify the files; outward arithmetic proves each
strict sign and complete coverage assertion.
