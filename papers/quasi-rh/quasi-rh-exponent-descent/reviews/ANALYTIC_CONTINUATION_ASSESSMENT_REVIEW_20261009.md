# Review of manuscript results and analytic continuation

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate same-model read-throughs are internal checks, not independent
specialist review or formal verification.

Reviewed artifact:
[Analytic continuation toward RH and results for the manuscript](../notes/ANALYTIC_RH_CONTINUATION_AND_MANUSCRIPT_RESULTS_20261009.md).
The review covers the manuscript inventory, the distinction between
positive-time improvement and an endpoint mechanism, the proposed collision
scout, and the status of the arithmetic alternatives.

## Manuscript inventory and source status

The heat inventory matches Notes 1 to 7. Complete scoped derivations exist
for the finite threshold-collision reduction, positive-kernel obstruction,
theta-cutoff Wronskian obstruction, fixed-cutoff analytic-neighborhood and
derivative interface, exact-field probe comparison, and count-derived global
landing law. The effective high-sector result is a worked corollary; the
compact rectangles are local examples.

The inventory correctly keeps the following qualifications with the results:

- Positive-time localization, local Hermite splitting, the threshold
  property, the effective Riemann–Siegel approximation, and the all-zero
  counting theorem are imported inputs.
- The count constant remains unprinted. Its explicit symbolic dependence
  is not a certified numerical value.
- The near-probe comparison concerns the exact field \(E\); the statement
  for the projected field \(G\) has a more restricted probe range.
- Sharpness is proved for permitted pairwise geometry. It is not a claim
  that the extremal geometry occurs for zeta.
- The \(E>4\) result requires maximal nonreal height at most \(0.2\),
  abscissa at least \(10^{16}\), and time in \([0.2,0.3]\).
- The tiny gain over the historical \(0.22\) canopy and the conditional
  \(0.217352\) sector landing are not headline or record claims.

The heat package has not been integrated into a manuscript source in this
turn. The existing short-family and mixed-family sources remain separate
conditional investigations. The continuation's recommended manuscript
organization is supported by the existing results; originality in the
literature remains unestablished.

The source check confirmed the scopes of
[Polymath, Theorems 1.3 and 1.5 and Proposition 3.1](https://arxiv.org/html/1904.12438),
and [Rodgers and Tao's lower bound](https://arxiv.org/abs/1801.05914).
The [recent projected-field comparison](https://arxiv.org/html/2609.37164v2#S2.Thmproposition3)
is explicitly attributed. Its numerical certificates and later candidate
endpoints are not inputs to the continuation.

## Positive-time attraction and the endpoint obstruction

For a finite constant field floor \(h>0\), expansion of
\(\log(1+2hw)/(4h)\) gives a gain \(hw^2/2+O(w^3)\).
The state-dependent count floor is finite at \(w=0\) and has the same
quadratic scale. Both are compatible with the ordinary collision law
\(w(t)=2(T-t)+O((T-t)^2)\) at a positive \(T\).
The assessment therefore correctly says that the tools are improving while
the missing mechanism toward zero has not been supplied.

The optional task near the published barrier has a distinct positive-time
payoff. It still needs global spatial coverage or a smaller left envelope
and a separator persisting after the old canopy time. The continuation does
not infer an earlier strip from a later upper bound on \(\Lambda\), or extend
the published barrier beyond its proved time range.

## Collision reduction and the new comparison lemmas

The finite threshold-collision argument in Heat Note 1 uses a uniform
positive-time cutoff before compactness. It does not infer compactness from
the weaker assertion of finitely many nonreal zeros at each separate time.
The converse uses local Hermite splitting at every real multiplicity at
least two, rather than assuming all collisions are double.

At an exact double root, the Jacobian with coordinate order \((x,t)\)
has determinant \((H'')^2>0\); with order \((t,x)\) it is negative.
The final continuation uses the correct order. Nondegeneracy describes
an ordinary collision and does not exclude it.

The error-paid amplitude and phase lemma, equation (8), passes the
algebraic review. At a candidate common zero the value error bounds
\(|2m\cos\phi|\), and
\[
 m|\sin\phi|\ge\sqrt{m^2-\epsilon_0^2/4}.
\]
The amplitude derivative term costs at most
\((m_1/m_0)\epsilon_0\), while the phase term supplies
\(2\Omega\sqrt{m_0^2-\epsilon_0^2/4}\).
Their difference exceeding the derivative error gives the contradiction.
Only local phase branches are needed.

The simpler carrier criterion (9) is also valid. The contribution from
the derivative of \(P\) costs at most \(2p_1\). The carrier contribution
has modulus at least
\(2\omega_0\sqrt{p_0^2-\epsilon_0^2/4}\).
For \(P=1\), this reduces to the previously proved leading-pair criterion.
These are conditional analytic lemmas. Neither proves the required
arithmetic amplitude or phase margin for a genuine many-term sum.

## Scaling diagnostic and mollifier scope

Equation (10) concerns coefficient mass, not the heat function or the
collision vector. For \(x=4\pi e^{\kappa/t}\),
\[
 \operatorname{Re}\alpha((1-ix)/2)
 =\frac{\kappa}{2t}+\frac14\log(1+x^{-2})
   -\frac1{1+x^2}.
\]
The last two terms are \(O(x^{-2})\). Also
\(\log N=\kappa/(2t)+o(1)\). On the last multiplicative block,
write \(n/N=u\in[1/2,1]\). Direct substitution gives
\[
 |p_n|=e^{-\kappa(\kappa+4)/(16t)}u^{-1/2}(1+o(1)).
\]
The error is uniform for \(\kappa\) in a fixed compact interval in
\((0,4)\). Multiplication by the block length proves the claimed mass
scale. More precisely, a Riemann sum gives
\[
 \sum_{N/2\le n\le N}|p_n|
 \sim 2(1-1/\sqrt2)e^{\kappa(4-\kappa)/(16t)}.
\]
At \(\kappa=4\), a block \([Ne^{-M},N]\) has limiting mass
\(2(1-e^{-M/2})\). This establishes the non-small-tail diagnostic.

A finite Dirichlet mollifier with constant coefficient one and indices
formed from a fixed finite prime set leaves all coprime coefficients below
the cutoff unchanged. Those integers occupy positive density in the last
block. Its coefficient-wise absolute majorant therefore retains the
exponential obstruction. This is a scoped limitation of that method,
not a no-go theorem for arbitrary mollifiers, grouped phase cancellation,
growing prime sets, or collision-conditioned identities.

No approximation or derivative error is being ignored in a new zeta
theorem: the diagnostic is only about the explicit coefficients. Paying
the full errors remains part of the proposed collision-exclusion task.
The note correctly labels the shrinking-time nonvanishing estimate as
unproved.

## Arithmetic alternatives and continuation decision

The fixed-scale section distinguishes the actual prime response from the
related scalar detector used by the completed-delay note. It defines
\(E_\delta,F_X,D_X\) and retains the full net energy change. Its RH
implication requires a new contraction at every positive admissible
optimal exponent and the inherited attainment/detection theorem.
Negative covariance alone or logarithmic savings do not suffice.

The short-family extraction and its possible endpoint hierarchy remain
conditional on the new short moments and adequate detecting profiles.
The \(4/15\) deficit and positive deletion coefficient are correctly
stated. The proposed single-prime contrast has a power-accuracy requirement;
within-cell variance and the full squarefree complement remain separate
obligations.

The mixed section keeps the actual gate, phases, inverse weights, physical
zeros, and witness family. Its remaining signed aggregate is the best
developed first arithmetic gain target in the current review record.
The note does not turn this first-gain opportunity into an iteratable
RH theorem.

Correlated translated probes are identified as a possible tool for a new
joint inequality; external computed endpoints are not adopted. Their
promise is conditional on retaining all adverse pairs and errors in a
shrinking-time comparison, rather than expanding an optimized numerical
grid.

Disposition: the continuation note passes the scoped internal assessment.
Its recommended next attempt has a proof-producing completion condition:
an error-paid signed collision estimate in a genuinely many-term scaling
family, or a precise arithmetic obstruction. Further threshold constant
optimization or finite parameter coverage does not satisfy that condition.
