# DSCT Week 6 Presentation-Ready Cleanup — HUMAN_GATE_PUSH_AUTH

## Result

The local Week 6 teaching package is presentation-ready and committed as
`a7e399e4283643259ab8d9027c6b90880c0e80e2` (`Prepare Week 6 presentation
package`). GitHub publication is the sole remaining gate: HTTPS has no usable
non-interactive credential and the configured SSH transport fails its system
proxy configuration before authentication. Do not reset, force-push, or rewrite
the preserved Morgan history; authenticate and push `main` normally.

## Authoritative presentation path

- Start with `week-06/instructor/PRESENTATION_RUNBOOK.md`.
- Before class run `bash week-06/scripts/13_preclass_check.sh`.
- First local page on WSL:
  `explorer.exe "$(wslpath -w week-06/websites/02_big_o_growth.html)"`.
- The runbook carries the complete sequence: Big-O, simple/trace/timed
  Fibonacci, iterative contrast, Bubble model and measured page,
  Bubble-versus-Merge, live runtime race, and parallelism.

## What changed and what was preserved

- The class-facing `stuff.md` conversational residue moved intact to
  `sidecar/archived_week06_conversation_residue_20260922.md`.
- `websites/README.md` now matches the actual seven-page order, including
  `04b_bubble_sort_measured.html`, and documents WSL opening.
- The Bubble page was regenerated from a complete real run on this host:
  10,000 in 6.04 seconds, 20,000 in 23.69 seconds, and 30,000 in 58.30 seconds.
- `instructor/week06_algorithms_growth_backdrop.tex` is a sparse ten-slide
  Beamer backdrop. No `latexmk` or `pdflatex` is installed locally, so no PDF
  was fabricated; the checker and runbook state the honest build condition.
- The default parallelism dataset remains the labelled i7-13700 24-worker CPU
  measurement in `results/parallel_sort_results.csv`. The Morgan i7-8700K
  Python result files remain preserved as clearly separate alternate evidence.
  GPU measurements remain absent because this environment lacked device access.

## Acceptance evidence

`bash week-06/scripts/13_preclass_check.sh` passed required-file checks, Python
and Bash syntax checks, and the no-external-HTML-dependency check. The simple
and iterative Fibonacci scripts and full recursive trace also ran successfully.
No class-facing conflict markers were found. See `AUTHORSHIP.md` for the Git
reconciliation, tool probe, heavy Bubble run, and exact transport failure.

## Git history and next action

The prior legitimate local Week 6 commits were preserved by ordinary merge
`ff717cc` after fetching GitHub `main` non-destructively. The package payload
is `a7e399e`; this terminal ledger commit records the gate locally. Resolve
`HUMAN_GATE_PUSH_AUTH` by making a GitHub credential available or repairing the
authorized SSH transport, then run a normal `git push origin main` (or the
equivalent authenticated HTTPS push).
