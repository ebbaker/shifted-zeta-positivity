# Audit: thermal boundary coupling and front rigidity

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Reviewer/model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review type:** same-assistant mathematical and numerical audit, not an independent specialist review.

**Artifacts:** [research note](../notes/THERMAL_BOUNDARY_COUPLING_AND_FRONT_RIGIDITY_TEST_20260923.md), [program](../numerics/check_thermal_boundary_structure.py), [203-case record](../numerics/records/thermal-boundary-structure-20260923.json).

## Assessment

This test advances from static thermal gates to native occupation-changing probes and their conservative linear response. It retains the complete modular half-shift response inside the boundary connection, so its exclusion does not reuse the finite-Euler truncation defect.

The decisive statement is an elementary finite-spectral-mass theorem for the specified parallel boundary architecture. Positive spectral mass finite in total implies admittance of order \(p^{-1}\), which can only change the known \(p^{-1/2}\) core response at a subleading order. The target requires a different exponent. The anchored temperature tangent likewise fails by an explicit asymptotic calculation.

The resulting recommendation to park this regular boundary-load branch is justified within that scope. The note does not promote it to a theorem excluding distributed, strongly coupled, or singular-domain quantum/automorphic models.

## Mathematical and physical checks

1. **Native energy exchange.** The bounded isometry probe \(B_\ell=v_\ell+v_\ell^*\) changes occupation energy and has a nonzero commutator with \(H_S\). For a bounded real prescribed effort, the perturbed microscopic Hamiltonian is self-adjoint on the original domain. The thermal state in the response calculation is the uncoupled Gibbs state, not a conjectured interacting KMS state.

2. **Response sign and normalization.** With interaction \(-U B\), the retarded convention is \(i\theta(t)\langle[B(t),B]\rangle\). Since \([v,v^*]=-P_0\), this yields \(2(1-q)\sin(\epsilon t)\), with positive Laplace susceptibility \(2\epsilon(1-q)/(p^2+\epsilon^2)\). Measuring the derivative of the conjugate coordinate gives the extra factor \(p\) in the admittance. Real fixed coupling coefficients enter as their squares.

3. **Bosonic control.** Using the unbounded ordinary bosonic ladder instead of the bounded Bost–Connes isometry gives a state-independent commutator and hence temperature-independent linear susceptibility. The manuscript's isometry is not silently replaced by a bosonic creation operator.

4. **Exactness boundary.** The Kubo susceptibility is exact for linear response about the bare thermal state. Its positive oscillator realization is an exact linear model. This is not an exact finite-coupling derivation of the full interacting quantum radiation system. The note states that distinction before using the connected model and again in its status and numerical scope.

5. **Thermal noise.** The unsymmetrized correlation has weights 1 and \(q\), while the symmetric fluctuation has weight \(1+q\); response has weight \(1-q\). The coth relation checks the relative normalization. Zero coherent perturbation is not a zero-energy thermal state. The ordinary coherent energy identity is not asserted to control inclusive quantum noise without a thermal-energy account.

6. **Port connection.** Effort continuity and flow addition, with the prior outgoing orientation, give \(f=a+I/2\), \(g=ra+I/2\). Solving gives the stated fractional expression with \(J=\lambda Y/2\). The factor of two follows from the norm-normalized power-wave variables. The original full \(\xi(p)/\xi(p+1)\) is retained; there is no finite Euler substitution.

7. **Energy and analyticity.** The driven oscillator has positive quadratic storage and supplied power \(\operatorname{Re}\bar U I\). The port equations split the external radiation deficit into this storage and the known causal core deficit. Analyticity of the connected response follows from addition of positive-real admittances and their Cayley transform. The numerator/denominator modulus identity is a separate algebraic check. No assumed positivity of the unknown target enters this argument.

8. **Spectral-mass theorem.** For finite positive mass \(C\), \(pY(p)=\int p^2/(p^2+\Omega^2)\,d\nu\) converges to \(C\), bounded above by it. Subtraction in the connected transfer then gives \(S-K=\lambda C/(2p)+o(p^{-1})\). This leaves the leading exponent unchanged. The theorem includes infinitely many modes if their total response spectral mass remains finite.

9. **General native scope.** Pairing Gibbs transitions gives a positive response measure with mass \(\operatorname{Tr}\rho[B,[H,B]]\), when the sum is finite. Finite combinations of native finite-energy-jump isometries meet this requirement. Boundedness of an arbitrary \(B\) alone is not sufficient for an unbounded Hamiltonian, and the note explicitly avoids that overstatement.

10. **Anchor and tangent.** A nonzero positive added load changes the beta-one reference response. The additional switch \(\lambda=1-\beta\) is therefore a favorable calibration, not a native consequence of temperature. Its derivative produces \(-Y_1(1-K)^2/(2K)\); the derivative of \(Y_\beta\) is suppressed at first order by the zero switch. A smooth microscopic amplitude vanishing at the reference has an even weaker, zero first tangent. The target logarithm cannot be matched by a finite calibration constant.

11. **Time and reference conventions.** All dynamical variables use a common radiation-time unit conjugate to \(p\), with the prior fixed physical-time conversion made explicit. At a regular exterior port the prompt load precedes the target's common delay. The favorable zero-extra-lead calculation is identified as a control, not relabeled as the regular geometric port.

12. **Short-time and endpoint checks.** The finite oscillator load kernel is continuous from the right at zero. Its calibrated transfer correction therefore has a finite step front, while the arithmetic beta derivative has the \(u^{-1/2}\log u\) singularity. Positive native transition frequencies also preserve the zero-frequency slope, and vanishing hot-limit commutator weights return the boundedly switched response to the half-shift core. These secondary observations support, but are not needed for, the high-frequency theorem.

13. **Required-load diagnostic.** Solving algebraically for \(Y^{(1)}_{\rm required}=a_{1/2}K/(1-K)^2\) identifies the spectral behavior an alternative would need. It is not presented as a physical construction or a proven positive-real function. Infinite spectral mass is outside this theorem, not automatically physically inadmissible or automatically successful.

## Numerical audit

The program has **203 passing floating controls** using Python 3.10.0, mpmath 1.3.0 and 60 decimal digits. All recorded comparisons are explicit; they do not constitute interval arithmetic.

Occupation sums use true infinite-ladder diagonal matrix elements through occupation 400, with a tail bound. The commutator is not computed using a truncated shift that would introduce an artificial upper-boundary projection. The retarded susceptibility is also checked by direct time-to-Laplace quadrature.

The load's supplied work is integrated from its explicit driven trajectories and compared with quadratic storage. Independent linear boundary equations are solved for the actual full modular response, then compared with the closed formula, flux identity and contractive bound. The suite separately checks the spectral-mass estimate, exponent preservation, calibrated target mismatch, exterior-port prompt term and endpoint behavior.

The source program hash is stored in the compact numerical record. No sibling program, zero table, external numerical dataset, nonlinear microscopic simulation or finite-grid proof is used. Earlier numerical suites remain unchanged. The analytic exclusion does not depend on the finite high-frequency sample values.

## Research decision and remaining work

The agreed stopping criterion is met for this class. Further finite-place modes or coefficient tuning in the same regular passive parallel-load architecture cannot change the required front exponent. Retain the thermal coefficient law as a separate result and park this realization branch.

The suggested main continuation is a cumulative storage construction for the complete arithmetic transfer on its first nontrivial time window. It remains a proposed research task, not a result of the present test. Any future return to thermal scattering should begin with a concrete mechanism outside the excluded assumptions and an independently justified energy/domain construction.

Manuscript TeX and PDFs were not revised or rebuilt. Navigation and file-identity records identify this separate addendum. This audit was performed by the same assistant as the research and is not an independent specialist review.
