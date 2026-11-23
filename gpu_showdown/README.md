# The GPU Showdown

A short, standalone student handout: an evidence dossier from a small local-GPU
benchmark fleet, framed through this course's own reasoning chain
(OBSERVATION → CLAIM → EVIDENCE → WARRANT → CONFOUND → BETTER TEST). It asks
students to decide what the benchmark evidence actually supports rather than
accept a headline "which GPU wins" ranking at face value.

This is a distinct artifact from the existing Week 3 GPU-concurrency LaTeX
walkthrough (`lectures/ai_reasoning_latex_from_data/`) — same general subject
area (GPU benchmarking), different exercise and different content. It is not
a replacement for that walkthrough.

Delivered as its own dedicated Canvas module ("The GPU Showdown") rather than
folded into a week module, so it stays easy to find and easy to extend later
if companion material is added.

Machine labels in the table (Machine A-H) are anonymized fleet host names —
the source data used real host names, relabeled before publication so the
student-facing copy doesn't expose them.

## Provenance

- Source repository: `jeremy-evert/local_ai_lab_setup`
- Source branch: `anna/gpu-showdown-latex-027`
- Source commit: `7feb3b1b8725b41a659aaa69d46221377b97a852`
- Built from: `curriculum/gpu_showdown/wrappers/dsct.tex` (machine labels
  relabeled to Machine A-H before build; see note above)
- Built on: April, 2026-09-02, via `latexmk` (pdflatex backend)
- SHA-256 (v3, relabeled + CPU column added): `a2344091e5a4bffb689d738ec0f14d77d987061e4b989a10ac83a00271eaaab5`
- Live Canvas placement: course 74035 (COMSC-2043-1420), module "The GPU Showdown"
