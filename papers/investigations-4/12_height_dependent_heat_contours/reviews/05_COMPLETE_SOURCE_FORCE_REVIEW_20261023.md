# Independent same-model review of HDC Note 07

23 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Reviewer: a separate same-model research agent, not the drafting agent. No specialist or cross-model review is claimed.

Reviewed source: [Note 07](../notes/07_COMPLETE_SOURCE_FORCE_AND_FILTER_RESIDUAL_20261023.md), drafted as `/private/tmp/hdc07_source_force.md`. Review basis: the complete displayed proof, the imported BW10 Note 19 source-tail constants, and direct independent symbolic derivation of signs and coefficients. No numerical evidence is used to promote a conditional claim.

## Disposition

**The finite force, tail, wall and source-truncation estimates are mathematically sound under the stated hypotheses.** One comparison sentence should be narrowed as described below. The final source-specific near-force bound has not been acquired; HDC-07 has a quantitative partial milestone, and HDC-10/HDC-11 remain open. The draft already says this clearly and should not be promoted to full HDC-07 completion merely because all finite algebra is now proved.

## Equations (1)-(4): coupled filtering and force error

Starting from W'=-2W[4W-2 sum_k((x_i-x_k)(x_j-x_k))^{-1}+2D_ij b], the factor in W+tW' is exactly the bracket in (1). Thus the exterior term is -16t sum c_ij D_ij b, with the negative sign in (2).

The trace identity sum c_ij=Tr(R^2 L)=J/(4t) is exact, because F=4tLR and L commutes with its own resolvent. It never uses commutation with L'. For a nonzero eigenvalue a of 4tL, J receives a/(1+a)^2<=1/4 and <=a/(1+a). The constant mode gives the stated N-1 rather than N. Therefore the divided-difference error in (4) is 16t beta times J/(4t), namely 4 beta J. All these estimates use the same exact roots and filter; the draft correctly warns that they do not control errors in approximate roots.

## Equations (5)-(9): complete real exterior and cutoff

The paired canonical product gives b divided differences as minus the exterior sum in (5). Any spatial constant in a logarithmic derivative would cancel anyway. The sum is absolutely convergent after taking a divided difference; no conditional reciprocal summation is being reordered.

A consecutive block has all exterior roots outside its hull, so each denominator product is positive. D_ij b is nonpositive, hence Q_b is nonnegative. For any selected population within [-A,A], the tail |r|>R_c>A also has this sign. The elementary denominator estimate is

|(x_i-r)(x_j-r)| >= r^2(1-A/R_c)^2.

The imported sum of 1/r^2 is B_T(R_c)=2C_T(log R_c+2)/R_c. Thus beta=B_T/(1-A/R_c)^2 and (7) follows with its stated sign. For R_c>=2A, beta<=4B_T, giving 8(N-1)C_T(log R_c+2)/R_c in (8). Integrating the pointwise error yields (9); finite-cutoff membership changes do not invalidate that integral because the argument does not differentiate the cutoff membership.

The original BW10 constants match the draft. The bound keeps T-dependence through C_T and retains the root enclosure A. It is legitimate to call this a canonical-source tail estimate and a quantitative gain over replacing Rv by v. It is not a bound for the retained local coupled expression. In backward transport the omitted nonnegative derivative term is subtracted, so dropping it gives a conservative upper endpoint estimate, as the draft states.

## Equations (10)-(12): wall values and logarithmic derivatives

The relative wall condition eta<1 gives a single-valued logarithm in a neighborhood of the wall with |ell|<=-log(1-eta). It need not extend throughout the interior. This is sufficient: Cauchy subtraction cancels all internal zero poles in H'/H and G'/G, leaving their exterior logarithmic derivatives. Along the closed contour,

integral ell'(w)/(w-z) dw = integral ell(w)/(w-z)^2 dw,

so the first identity in (11) has the correct positive sign. Taking its divided difference gives exactly the sum of the two cubic kernels displayed in (11), also with positive signs. Each kernel is bounded by d^-3 and the two kernels supply the factor 2, yielding ell_Gamma epsilon_ell/(pi d^3). Applying (4) gives (12). Distinct roots are needed for the real positive filter algebra; the analytic force representation itself extends through interior collisions, as stated.

The affine-reference contribution is -4aJ because D_ij(az+c)=a. A general holomorphic reference need not be real-type; its force error can still be bounded in modulus, but any later signed lower bound for the total residual must either take real parts or supply real reference data. The present norm statement is valid.

**Wording correction recommended.** The displayed beta_abs=ell_Gamma sup|H'/H|/(2pi d^2) is the original bound for the entire H-force. The relative wall bound estimates the residual after retaining b_G. The sufficient inequality 2epsilon_ell/d<sup|H'/H| does compare these two numerical radii correctly, but the next sentence's phrase "for the same retained reference" is too strong as written. For a literal same-reference derivative comparator use

beta_resabs=ell_Gamma sup|H'/H-G'/G|/(2pi d^2),

and compare 2epsilon_ell/d with that supremum. Alternatively say explicitly that the displayed comparison is with the original unreferenced whole-force radius, and that paying b_G can change the total bound. The following caveat already acknowledges the latter issue; this is a comparison clarification, not a flaw in (11)-(12).

## Equations (13)-(14): full-source truncation

For n>=1 and u>=0 each theta summand is positive since 2pi n^2 e^(4u)-3>0, and it is bounded above by its positive first term. Ratios of consecutive positive majorants are at most 16exp[-pi(2m+1)] for all n>=m. The inequalities u^2<=e^(2u)/e^2 and u<=e^(2u)/(2e) give the stated b. Completing the square in v=e^(2u) gives

b v-pi m^2 v^2 <= b^2/(2pi m^2)-(pi m^2/2)v^2.

The substitution w=(pi m^2/2)e^(4u) produces the factor 1/4 in the integral; together with 2pi^2m^4 it gives pi^2m^4/2. This verifies the first term of (13). The same calculation for the complete source above U gives C_Phi/4 and the second incomplete gamma function. Overlap is safely overcounted. Complex time enters only via Re tau<=T and |cos(zu)|<=e^(Y u), so the declared complex domain is supported.

Equation (14) is the direct relative-error bound after division by the acquired reference floor. The gate eta<1, interior count, quadrature error and reference-factor acquisition are correctly left unpaid. An x-independent absolute source error does not imply an x-independent relative error, and the draft explicitly warns about that failure.

## Controls and status

The pure quadratic and Hermite births have zero source-tail error but nonzero bounded collision mass, so they correctly prevent the finite tail estimate from being read as a simplicity argument. The stationary sine control confirms why exterior force is necessary. The registered canonical-source failures are named without assigning an unsupported all-real interval to weighted-square or reflected controls. The distinction between the generic wall lemma and the canonical tail theorem is maintained.

This review supports recording a finite canonical distant-force error milestone and a relative wall-value force interface. It does not support marking the signed local source problem complete or inferring q=o(N), q<1/2, density-one simplicity, or an RH-free endpoint reality theorem.

Integration disposition, 23 October 2026: the recommended comparator clarification was applied before installation. Note 07 now states both the whole-force comparison and the literal same-reference residual comparison. No mathematical formula was changed.
