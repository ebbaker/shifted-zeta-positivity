# Initial research questions for threshold higher jet sign

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model: **gpt-6-astra (Codex)**;
actual reasoning effort: **xhigh**, verified from the recorded turn metadata.

## Research status and standards

This is an initial exploration note, not a completed research program,
progress tracker, new theorem, or numerical acceptance record. The
[living brainstorm][brainstorm] supplies the common RH context. Read the
[result summaries][results] and [patterns to avoid][avoid], especially
[target classification][classification], [collision controls][controls],
[control premises][control-rule], [scoped exclusions][scope], and
[signed recombination][pairing]. Existing results keep their source status;
the required new estimates below are proposed work.

Before quantitative work, identify the exact source versions, domain,
normalization, derivative orders, cutoff conventions, and complete error
norm. Any control run must use the control's own source and errors on a
domain containing its event or relevant witness. Analytic existence results
must not be assigned invented numerical event locations. The analytic
screens below select premises; they are not new numerical validations.

## Hypothetical event and exact contradiction

Failure of RH implies a positive Newman threshold and a finite multiple
real zero at that threshold, where all zeros of the genuine field are real.
Uniform confinement is essential to that reduction; see
`prop:finitecollision` in the [predecessor][predecessor]. The all-real
hypothesis is specific to the candidate threshold and must not be assigned
to an arbitrary positive-time event.

At an ordinary double zero \(x_*>0\), write
\(H_j=\partial_x^jH(T,x_*)\). The inherited deflated mirror condition is

\[
2H_3^2-3H_2H_4-9H_2^2/x_*^2\ge0.
\]

For \(Q=H/\mathcal A\), put \(q_j=\partial_x^jQ\),
\(b=\mathcal A_x/\mathcal A\), and \(\gamma=18b_x+9/x_*^2\).
At the collision the normalized condition is

\[
\mathscr L(q)=2q_3^2-3q_2q_4-\gamma q_2^2\ge0.
\]

The desired contradiction is a genuine arithmetic upper bound forcing
\(\mathscr L(q)<0\) for the specified candidate class. It may use the
necessary small first-jet coordinates, but cannot assume the separation
it is intended to establish.

## Existing error interface and missing estimate

For a specified approximant with derivatives \(f_j\) and complete errors
\(|q_j-f_j|\le\delta_j\), the predecessor's `lj:paidtest` supplies

\[
\begin{aligned}
|\mathscr L(q)-\mathscr L(f)|\le\Delta={}&
4|f_3|\delta_3+2\delta_3^2+3|f_2|\delta_4+3|f_4|\delta_2\\
&+3\delta_2\delta_4+|\gamma|(2|f_2|\delta_2+\delta_2^2).
\end{aligned}
\]

Thus \(\mathscr L(f)+\Delta<0\) is the precise paid contradiction.
Re-deriving the mirror inequality or this algebra is not a new research
result. The missing work is the arithmetic sign estimate. Adopting Project
11's current corrected approximant requires its own complete errors through
order four; bounds for an omitted edge alone do not supply those errors.
The normalizer contribution \(18b_x\) and all products of errors remain.

## Questions for the first deeper discussion

1. Which signed arithmetic expression controls \(\mathscr L(f)\), and
   how does conditioning on small value and slope alter its feasible
   range? Compare this with unconditional upper bounds on the same domain.
2. Is a restricted ordinary-double class accessible, with a stated
   nondegeneracy or curvature range that can itself be verified? Any such
   restriction leaves other events explicitly untreated.
3. Which higher-multiplicity condition is useful if ordinary doubles are
   not enough? The predecessor already derives a deflation hierarchy at
   `lj:hierarchy`; the new task is its arithmetic estimate and error transfer.

At exact multiplicity three the fourth-jet inequality is automatically
satisfied. At multiplicity at least four it reduces to \(0\ge0\).
Do not infer that these events are absent. An all-multiplicity conclusion
needs the relevant higher derivatives and their separate payments, or a
separately proved restriction on multiplicity.

## Control screen

The predecessor's `lj:quartic` is an exact sharpness screen. For
\(\delta=t-T\),

\[
P_t(z)=z^4-(2a^2+12\delta)z^2+a^4+4a^2\delta+12\delta^2
\]

solves backward heat and has all zeros real exactly for \(t\ge T\).
At \((T,a)\), its derivatives are \(P_2=8a^2\), \(P_3=24a\),
\(P_4=24\), giving
\(2P_3^2-3P_2P_4=576a^2=9P_2^2/a^2\). It has a genuine positive
threshold and saturates the necessary inequality. Its failed premises are
the complete theta source and its arithmetic approximation contract; it is
not asserted to come from a positive theta kernel.

Weighted-square and finite-prime controls cannot automatically be used as
finite-threshold controls: the source audits do not give them an all-real
heat time. They still screen generic arithmetic premises when relevant,
with their failed full-reflection or complete-coefficient assumptions named.
The multiplicative phase relaxation screens loss of actual-height coupling,
not a claimed all-real twisted heat field.

## Useful first results and remaining scope

A useful first result is a conditional arithmetic restriction on the
second-through-fourth jets, a paid exclusion of a declared threshold-event
class, or a proof that a particular estimate cannot beat its error on that
class. Report the strict sign margin and the covered domain. The initial
sector may follow the existing UAR domain, but its approximation through
order four must first be justified for the chosen representation.

This route is a narrower consumer of retained-jet information. It exploits
the global all-real hypothesis rather than demanding exclusion of every
heat event. Excluding every possible positive threshold event would imply
RH; excluding one domain or multiplicity class does not. The [research
assessment][review19] and [existing program][program11] retain those scope
limits. No global program, schedule, or progress register is created here.

[brainstorm]: ../../../brainstorm/notes/04_SMALL_JET_OBSTRUCTION_AND_RH_CONTRADICTION_TARGETS_ASTRA_20261019.md
[review19]: ../../../11_arithmetic_collision_rigidity/reviews/19_FIXED_FUNCTION_PROGRAM_AND_AMBITIOUS_NEXT_STEPS_REVIEW_ASTRA_20261019.md
[program11]: ../../../research-overview/03_FIXED_FUNCTION_ARITHMETIC_RESEARCH_PROGRAM_20261019.md
[predecessor]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[control-rule]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[pairing]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
