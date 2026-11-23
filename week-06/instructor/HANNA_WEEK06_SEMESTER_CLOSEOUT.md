# Hanna Mission — DSCT Week 6 Fall 2026 Semester Closeout

You are Hanna the Helper. This is a bounded archival and repository-cleanup mission for Jeremy's Discrete Structures & Critical Thinking Week 6 materials.

## Mission goal

Week 6 is finished.

Do NOT optimize this package for another live presentation now.

Instead, leave `week-06/**` in durable cold storage so that Jeremy can return next semester, understand exactly what worked, reproduce the useful experiments, and selectively revive the lesson without reconstructing today's history from chat logs or Git archaeology.

The desired final state is:

- clean Git history;
- preserved legitimate Morgan and published work;
- no unresolved merge debris;
- useful scripts and measured evidence retained;
- machine-specific measurements clearly labeled;
- conversational scratch/log residue archived out of the class-facing root;
- one obvious "start here next semester" document;
- a concise archival manifest;
- a valid LaTeX/Beamer lesson backdrop kept as reusable source;
- reproducibility notes that are honest about CPU/GPU/toolchain differences;
- durable mission receipts explaining exactly what was preserved and why.

## Current Git truth to re-establish

Do not assume Morgan matches GitHub.

A prior Codex repair found that Morgan's `main` diverged from `origin/main` after `3da0845`. It preserved both histories in local merge commit `8c9b85a` and left Morgan clean but ahead because GitHub push authentication was unavailable at that time.

Since then GitHub `main` has advanced again with additional Week 6 files.

Before changing content:

- inspect `git status --short --branch`;
- inspect local and live remote commit graphs and merge-base;
- inspect local-only commits, including `8c9b85a` and its parents when present;
- fetch the live remote non-destructively;
- preserve legitimate Morgan work;
- integrate with ordinary forward history only;
- never force-push, amend published commits, hard-reset away unexplained commits, or rewrite either history;
- if push credentials remain unavailable, finish and commit the local archive and record the exact push gate.

## Writable scope

Only modify:

- `week-06/**`

You may inspect adjacent repository files and Foreman Interface protocol files for conventions and truth, but do not modify them.

## Required archival package

### 1. Create the next-semester entry point

Create:

`week-06/NEXT_SEMESTER_START_HERE.md`

This is the primary artifact for Future Jeremy.

Keep it concise and useful. It must explain:

- what Week 6 taught in Fall 2026;
- the final teaching sequence that actually emerged;
- which scripts/websites are worth keeping;
- what measurements were collected and on which host classes when known;
- which result set is the default reference and which are alternates;
- the important classroom discoveries:
  - naive recursive Fibonacci repeats work explosively;
  - iterative Fibonacci removes that repeated-work problem;
  - Bubble Sort worst-case growth becomes visible at 10/100/1,000/10,000/20,000/30,000;
  - single-threaded Bubble Sort should visibly work roughly one logical CPU core;
  - Merge Sort demonstrates that recursion itself is not the villain;
  - parallelism has overhead and a crossover point;
  - algorithmic growth and hardware throughput are different ideas;
  - GPU hardware may exist while a particular sandbox/process cannot access it;
- what Jeremy should inspect or rerun first next semester;
- known rough edges or unfinished ideas, including any GPU experiment that was not actually collected;
- commands that work in WSL/Windows, including `explorer.exe "$(wslpath -w ...)"`.

Do not write this as a live lecture script. Write it as an archaeological map for reuse.

### 2. Create an archival manifest

Create:

`week-06/instructor/FALL_2026_ARCHIVE_MANIFEST.md`

Inventory the durable artifacts by category:

- teaching scripts;
- websites;
- measured results;
- instructor notes/missions;
- student-facing artifacts;
- sidecar/receipts.

For each important item, state in one line what it is and whether it is:

- SOURCE;
- GENERATED;
- MEASURED;
- ARCHIVAL;
- OPTIONAL/EXPERIMENTAL.

Also identify anything intentionally not treated as canonical.

### 3. Clean the Week 6 root and archive residue

Audit every file directly under `week-06/`.

`week-06/stuff.md` currently contains pasted conversational/log residue. Preserve any uniquely useful historical content, but move that residue into an archival location such as:

`week-06/sidecar/archive/fall-2026/`

Do not leave raw chat/paste debris in the Week 6 root.

Do not discard unique measurements, code, or reasoning merely because it is messy. Preserve first, then organize.

Remove generated junk only when it is clearly reproducible and unneeded. Never delete unexplained user work.

### 4. Reconcile scripts and document what is canonical

The archive should preserve, at minimum, working or historically useful versions of:

- simple recursive Fibonacci;
- full recursive Fibonacci trace;
- recursive 60-second Fibonacci timing race;
- iterative Fibonacci timing;
- measured Bubble Sort timing;
- CPU parallel sort path;
- optional GPU path;
- webpage generator and runners;
- Hanna launcher/mission helpers that are specific to this Week 6 experiment, if they remain useful historical evidence.

Syntax-check Python and shell scripts.

Do not rerun expensive classroom benchmarks merely for ceremony. Run only bounded smoke tests needed to establish that preserved source still parses/works.

For Bubble Sort, preserve the intentionally heavy 10/100/1,000/10,000/20,000/30,000 progression unless evidence shows the current file differs or is unsafe.

### 5. Reconcile websites without turning this into a redesign project

Audit `week-06/websites/`.

Ensure the README accurately lists what survived the final lesson, including the measured Bubble Sort page.

Keep self-contained HTML demos that are reusable next semester.

Do not spend time cosmetically redesigning working pages unless a defect blocks preservation/reuse.

Do not fabricate or regenerate host-specific timings unless required to repair a broken artifact.

### 6. Preserve measured evidence honestly

Audit `week-06/results/`.

If multiple machines produced different datasets, preserve them with explicit labels instead of merging them into one misleading truth.

Document:

- which dataset is the default Fall 2026 classroom reference;
- which dataset came from Morgan when known;
- which dataset came from Sinon/another host when known;
- CPU model / worker count only when already legitimately captured;
- GPU presence versus actual GPU timing availability.

Never invent missing measurements.

### 7. Create a reusable LaTeX backdrop

Create:

`week-06/instructor/week06_algorithms_growth_backdrop.tex`

This is archival reusable source for next semester, not a deliverable that must be presented now.

Use a minimalist Beamer deck with widely available packages only.

Target roughly 8–12 sparse slides covering:

1. Algorithms, Correctness & Growth.
2. What happens when the problem gets bigger?
3. Naive recursive Fibonacci and repeated work.
4. Correct does not mean efficient.
5. Bubble Sort worst-case growth and 10x input -> about 100x work intuition.
6. Recursion was never the villain: Bubble vs Merge.
7. Parallelism has a cover charge.
8. Measured CPU crossover / scale.
9. GPU present versus process/device access.
10. Closing synthesis: algorithm changes growth; parallelism changes throughput.

Use formulas where LaTeX adds value. Avoid screenshots, external assets, and fragile dependencies.

If `latexmk` or `pdflatex` is already installed, compile and preserve the PDF. If no TeX engine exists, do NOT install a TeX distribution. Preserve valid `.tex` source and document the missing toolchain.

### 8. Create a lightweight archive validation command

Create:

`week-06/scripts/13_archive_validation.sh`

It should be safe, fast, and non-destructive.

It should:

- report Git status without changing history;
- verify the important archived Week 6 files exist;
- syntax-check Python and Bash;
- verify key HTML files are non-empty;
- report availability of `htop`, C++ compiler, NVIDIA/CUDA tools, and LaTeX tools;
- verify the next-semester entry point and archive manifest exist;
- print where Future Jeremy should start;
- avoid heavy benchmarks.

Exit nonzero only for genuine archive-integrity failures.

### 9. Preserve a concise "what actually happened" record

Create or update:

`week-06/sidecar/hanna_semester_closeout/`

with:

- `STATUS.md`
- `AUTHORSHIP.md`
- `WORKER_INDEX.md`
- `SUMMARY.md`

`SUMMARY.md` must record:

- Git divergence found and how it was preserved/reconciled;
- final archive structure;
- what happened to `stuff.md`;
- default and alternate measured datasets;
- whether LaTeX compiled;
- validation results;
- exact final commit SHA(s);
- push state;
- any real gate that Future Jeremy may encounter.

## Acceptance checks

Before declaring COMPLETE:

- no unresolved Git conflict markers in Week 6 source;
- no raw chat/paste dump remains in the Week 6 root;
- `NEXT_SEMESTER_START_HERE.md` exists and is genuinely useful;
- `FALL_2026_ARCHIVE_MANIFEST.md` exists;
- important scripts pass syntax checks;
- key reusable HTML artifacts exist and are non-empty;
- measured data is preserved without pretending different machines are one dataset;
- LaTeX source exists and either compiles or has an honest no-toolchain note;
- `13_archive_validation.sh` passes all locally satisfiable checks;
- no unexplained user work is discarded;
- final local Git state is clean after committing the archive;
- push is attempted only by ordinary forward history if credentials are available.

If local archive work is complete but push authentication is the only remaining blocker, set:

`STATUS: HUMAN_GATE_PUSH_AUTH`

and provide the exact safe push command. Do not call the archive COMPLETE on GitHub until it is actually published.

## Git authority

Within `week-06/**`, ordinary forward commits are authorized.

Push is authorized if credentials work.

Never force-push.
Never amend published history.
Never hard-reset away unexplained work.
Never mass-stage unrelated paths.
Never install CUDA, GPU drivers, or a TeX distribution.
Never reboot or make destructive system changes.

Proceed autonomously through truth-establishment, preservation, organization, validation, commit, and publication until the archive is durable or a genuine credential gate remains.
