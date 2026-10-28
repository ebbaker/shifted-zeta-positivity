# Initial deformation manuscript and program assessment

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0006, **Review radial collision progress**. Same-assistant internal assessment; no separate or specialist reviewer.

**Status: initial working manuscript with proofs of the stated identities and elementary local corollaries; same-assistant checking only.** The [manuscript][manuscript] consolidates Notes01, 14, 16 and 17, adds the local zero-motion formulas in [Note18][n18], and records the new structure-first direction. It does not prove a nodal-bifurcation classification, a new theta estimate, a homogeneous characteristic realization, or a contradiction under positive Lambda.

## Mathematical assessment

The central construction is the explicit family U=(partial_x-w)Y, w=kappa tanh(kappa x), with its complete transformed forcing. The Riccati identity factors both operators, gives the inverse with denominator lambda+kappa^2, and preserves the boundary observation U(0)=-8H and its spectral derivatives. The radial conjugation retains the 1/4 term. The integral kernel changes together with the forcing; integration by parts preserves the full observation and includes both endpoints. Compact parameter domains and canonical Gaussian tails justify the stated operations. These are identities of selected forced responses, not an undeclared self-adjoint spectral theorem.

The physical-time source law retains x g/2. The auxiliary law is differentiated at fixed t,x,lambda and retains the inverse denominator. The complete energy identity was checked through the Wronskian and direct integration of its two terms. In particular:

> The transported ordinary energy identity gives no additional scalar event condition; this does not rule out other uses of the deformation family.

The new zero-motion statements are elementary consequences of the existing family. The physical velocity follows from H_t=-H_aa and the chain rule in a=2sqrt(lambda). The interior velocity follows from U_x=g-(lambda+kappa^2)Y-wU and the implicit-function theorem, only where U_x is nonzero. The coordinate mu=kappa^2 removes the vanishing first kappa derivative at zero on compact x sets. No uniform expansion at spatial infinity is claimed. Spatial double nodes U=U_x=0 remain distinct from the spectral boundary event U(0)=U_lambda(0)=0.

The Gaussian-polynomial control is retained exactly. Its physical boundary zero is double, while U<0 throughout x>0 for every finite kappa>=0. This disproves an unqualified inference from absence of interior nodes to simplicity of the observation. It does not decide a theta-dependent boundary correspondence. The inherited smooth controls obey the same generic identities on their own convergence domains; their differing arithmetic, reflection and tail premises remain explicit. Atomic controls are outside this smooth formulation. No earlier numerical certificate was rerun.

The appendix accurately retains Note16's fourth-moment necessary condition, its bounded exclusion, and equality of the matched direct-u constants. No improvement over the second-moment radius is claimed without the separate moment inequality. The body treats the finite-event reduction under positive Lambda as a later application with its own hypotheses, not as a theorem proved by the deformation.

The Darboux input is classical. The [reference record][reference] identifies the primary source inspected for factorization. The forced normalization, observation, time law and control are derived explicitly here. There is no originality claim for the classical transformation and no new literature import beyond the recorded inputs.

## Program and document assessment

At Edward Baker's request, the [new overview][overview] and [proposal][proposal] supersede both RTC and RLC plans in priority. The [RDZ register][progress] distinguishes foundations already available from the still-open structural tasks. The first bounded task is the geometry of interior nodes, including degeneracies and spatial boundaries; theta specialization follows the relevant structural work. A generic structural theorem can be a valid result without immediately excluding the control. Creating the documents does not complete the research tasks.

The new [continuation note][handoff] states the actual working equations, reading order, first task, and unique chat identity. The earlier numbered overviews, progress registers, notes and assessments are preserved. The current entry points now route to RDZ, and DRAFT_HISTORY records one active source rather than a snapshot directory.

The manuscript compiled with latexmk/pdfLaTeX to nine letter-size pages. The final build log contains no LaTeX warnings, undefined references, or overfull/underfull boxes. All nine rendered pages were visually inspected for text, equations, margins, numbering and references. The installed source also compiled successfully with the desktop editor compiler. The [small build record][build] records source/PDF hashes, checks and preservation results. These are document and provenance checks, not a mathematical certificate. The editable source is in the investigation base; the generated PDF is in the ignored shared output directory identified by [the build instructions][buildinstructions].

**Disposition:** retain the initial manuscript and begin the declared structural work package. The exact family and local formulas are a foundation; broader conclusions remain research questions. Independent mathematical review remains open.

[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[n18]: ../notes/18_PHYSICAL_AND_INTERIOR_ZERO_DYNAMICS_FOUNDATION_20261027.md
[reference]: ../references/08_DARBOUX_FACTORIZATION_AND_RADIAL_DEFORMATION_20261027.md
[overview]: ../research-overview/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_OVERVIEW_20261027.md
[proposal]: ../research-proposal/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROPOSAL_20261027.md
[progress]: ../research-progress/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROGRESS_20261027.md
[handoff]: ../notes/19_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_CONTINUATION_20261027.md
[build]: ../numerics/12_INITIAL_DEFORMATION_MANUSCRIPT_BUILD_RECORD_20261027.json
[buildinstructions]: ../MANUSCRIPT_BUILD.md
