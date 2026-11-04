# Fermionic theta transfer continuation manuscript

2 November 2026, America/New_York. Drafted for Edward Baker with substantial LLM assistance; actual **gpt-6-astra / xhigh**.

The evolving [LaTeX source](main.tex) continues the [parent background manuscript](../../manuscript/main.tex). It concentrates on the fermionic transfer, local dissipativity, loss instrument and collision limits, signed readout, vacuum-Fock extension, scoped sign-mechanism obstruction, and theta energy-response interpretation. The signed comparison remains unproved.

From this directory run:

```sh
sh build.sh
```

Requirements: Python 3, latexmk, pdfLaTeX, BibTeX, plainurl.bst, and the standard packages named in the preamble (including mathrsfs). The build reuses the parent's bibliography preparation helper and the canonical shared bibliography. It creates a disposable print bibliography beside the PDF; it does not duplicate the source catalog.

The default output is the ignored repository-root `output/pdf/mc08-open-quantum-dynamics/fermionic_theta_open_dynamics_energy.pdf`. An alternative output directory can be supplied as the first argument. The initial reading copy has 19 pages. Generated PDF and auxiliary files stay outside the manuscript source directory under the large-file policy.

[Build record](BUILD_RECORD.json), [integration note](../notes/07_CONTINUATION_MANUSCRIPT_INTEGRATION_20261102.md), and [production self-check](../reviews/05_MC08_CONTINUATION_MANUSCRIPT_SELF_CHECK_20261102.md) identify the version, evidence status and validation. The [next-session/model-change handoff](../research-progress/handoffs/06_MC08_MANUSCRIPT_AND_NEXT_SESSION_20261102.md) gives the reading sequence and current decision. Review number 04 remains available for the separately pending E04 assessment; Review05 is editorial self-checking only.

Keep this one evolving source. Record milestones in the branch DRAFT_HISTORY.md, with future commits/tags as appropriate. No manuscript snapshot directory, commit or publication is created by this draft.
