# B07 proof author self check

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, authenticated chat0006. Actual model
and effort are unavailable. Same assistant as Note13; no helper,
different-model or specialist review.

**Disposition: B07 supplies a concrete conditional evaluator contract.**
The six obligations below are checked analytically at proof-author level.
E09 must assess them before acquisition. No root/count/quadrature code
was implemented and no canonical values were measured in B07.

| Obligation | Author check and remaining execution requirement |
| --- | --- |
| C1 Geometry and canonical identity | x=2 gamma and y=2 beta-1 use conjugation with s=1/2-iz/2. Rectangle (998,2002)×(-3/2,3/2) contains the entire contributing window. The nontrivial strip and zero-free multipliers preserve labels. Actual contour zero-freeness is still required. |
| C2 Complete count | Each full segment image must lie in a convex box avoiding zero. Its arguments occupy a strict half-plane, so principal endpoint increments are valid. Integer extraction then counts all complex zeros. Distinct real sign brackets plus equality to this count imply one simple zero each; candidates alone prove nothing. |
| C3 Root transport | Global A=3,L=26 include both cutoff derivatives. Ordered distinct-label products cost 2N(N-1)ALrho; connected subtraction adds 2N²ALrho. Common error is 4992/2^24 at the caps. Coincident labels retain m(m-1). |
| C4 Quadrature | Branches are split before analytic continuation, at most five pieces per pair, each length <=1. The parameter-2 ellipse gives transition modulus <=9/8 and imaginary center <=3/8. M1=600,M2=200000 bound both-disk Gaussian costs. Chebyshev tail plus positive Gauss weights gives 8dM2^(-2q). Summing lengths, rather than number of pieces, yields the stated e1/e2. |
| C5 Connected/error ledger | Positive mean quadratures and midpoint means are <4, so connected quadrature costs e2+8e1<257/2^24. Combined bound 5249/2^24<1/3000 is analytical. Arithmetic radii must be measured separately; <1/750 is a conditional final radius. Exact-zeta balls must include all evaluation remainders. No truncated-source tail is free. |
| C6 Scope and budget | One T, exact center interval, seven report probes and a continuous surrogate; no interpolation claim. Complete counts/radii/cost caps are gates. The pilot has no guaranteed success or measured runtime. Collision controls are a premise screen, not rerun certificates. |

The circle/ellipse estimates do not assume analyticity of a compact
window globally. The argument counter does not confuse a principal
argument at one endpoint with a winding count. Midpoint support changes
are covered by the global Lipschitz transport, including pairs that
appear or disappear at a support edge. The zero-free collar is wider
than the actual support, so discarded external labels cannot contribute.

B07 made one implementation clarification: use a full-complex winding
certificate rather than promote a library's real-line zero list to a
complete divisor without checked count evidence. This was part of the
initial B decision, not a numerical repair or a correction to E08.

The official online API passages identify tools, not validated runtime
results. The selected Python interpreter lacks the optional numerical
libraries; E09 owns isolated environment setup and actual version
recording. Failure to obtain a supported interval runtime is an
environment-gate failure, not a no-go theorem.

Frozen E03/E04/E08 inputs, manuscript/build and prior evidence levels
must remain unchanged; the session validation records their hashes.
No manuscript milestone or investigation closure is claimed. The
[continuation](../continuation-notes/15_TND_OC_AFTER_B07_AND_MODEL_CHANGE_20261108.md)
routes fixed execution to Sol and reserves new choices for B08.
