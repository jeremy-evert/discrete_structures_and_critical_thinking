# Hanna authorship ledger

## 2026-09-22 — Git truth and reconciliation

- Verified the supplied dispatch hash before work.
- Found local `main` at `8c9b85a`, four legitimate commits ahead of the old
  remote-tracking tip. The live GitHub `main` was `1d4ca78`, which added this
  canonical mission and diverged after `d313f3f`.
- Retrieved `origin/main` non-destructively over HTTPS because the configured
  SSH transport failed on its system SSH proxy configuration.
- Inspected the graph and made ordinary merge commit `ff717cc`, preserving both
  Morgan's existing Week 6 history and GitHub's new mission. No reset, rewrite,
  force push, or unexplained-work discard occurred.

## 2026-09-22 — Presentation package decision

- Audited the Week 6 root, scripts, websites, results, instructor material, and
  prior parallelism evidence.
- Accepted the committed `parallel_sort_results.csv` / `parallel_sort_hardware.txt`
  as the default labelled i7-13700 24-worker CPU dataset. Preserved the separate
  Morgan i7-8700K Python dataset as alternate evidence and did not combine them.
- Moved the root-level conversational residue to
  `sidecar/archived_week06_conversation_residue_20260922.md`; it remains
  preserved but no longer appears as a class-facing root artifact.
- Created the sequential runbook, a local-only HTML inventory, a restrained
  Beamer source, and a read-only pre-class checker.

## 2026-09-22 — Validation decision

- `git diff --check`, Python compilation, Bash syntax checks, required-file
  checks, and local HTML dependency checks passed through the new checker.
- Ran the simple Fibonacci and iterative Fibonacci classroom scripts. The full
  recursive trace completed (291 lines, captured only as transient test output).
  The intentional Bubble Sort run completed all six required sizes and refreshed
  the local measured page with real results: 6.04 seconds at 10,000, 23.69
  seconds at 20,000, and 58.30 seconds at 30,000 on this host.
- Tool probe found Python and `htop`; no `latexmk`, `pdflatex`, `g++`, or `nvcc`,
  and `nvidia-smi` reported blocked NVML access. The source and runbook state
  these constraints honestly; no system software or drivers were changed.

## 2026-09-22 — Commit and publication gate

- Committed the validated Week 6-only package as
  `a7e399e4283643259ab8d9027c6b90880c0e80e2`
  (`Prepare Week 6 presentation package`). The working tree was clean after
  that commit.
- An authorized ordinary HTTPS push was attempted directly to the canonical
  GitHub remote. Git returned `could not read Username ... No such device or
  address`; no credential prompt or usable credential was available in this
  non-interactive host context. The configured SSH remote had already failed on
  a system SSH proxy configuration error.
- Classified the only remaining condition as `HUMAN_GATE_PUSH_AUTH`. The local
  package is class-ready and committed; no history was rewritten and no further
  transport workaround can safely supply authentication.
