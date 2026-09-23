# Week 6 — Start Here Next Semester

This is the archaeological map for the Fall 2026 package. Week 6 taught that
correct output is not the same as a justified efficiency claim: trace the
procedure, count meaningful work, test edge cases, and distinguish growth from
one machine's stopwatch.

## The sequence that actually emerged

1. Begin with the correctness/contract work in `student/` and the Tuesday and
   Thursday run-of-show notes.
2. Open `websites/02_big_o_growth.html` to ask what changes when the input gets
   bigger.
3. Run or inspect `scripts/00_recursive_fibonacci_simple.py` and
   `scripts/01_recursive_fibonacci_trace.py`; then compare
   `scripts/02_recursive_fibonacci_60_second_race.py` with
   `scripts/03_iterative_fibonacci_timing.py`.
4. Use `websites/04_bubble_sort_quadratic_growth.html`, then the measured page
   `websites/04b_bubble_sort_measured.html` and
   `scripts/04_bubble_sort_timing.py`.
5. Use `websites/05_bubble_vs_merge_growth.html` and
   `websites/06_live_sorting_runtime_race.html` to show that recursion itself
   is not the villain.
6. Finish with `websites/07_parallelism_plot_twist.html`, the CPU source, and
   the measured CSV. Parallelism has overhead and a crossover point; it changes
   throughput, not the underlying growth class.

## The classroom discoveries worth preserving

- Naive recursive Fibonacci repeats work explosively; iterative Fibonacci
  removes that repeated-work problem while producing the same answers.
- Bubble Sort's worst-case growth is visible at 10, 100, 1,000, 10,000,
  20,000, and 30,000 values. A 10× input increase trends toward about 100×
  work, not 10×.
- Single-threaded Bubble Sort should visibly work roughly one logical CPU core
  on a telemetry view such as `htop`.
- Merge Sort demonstrates that recursion is not the villain; the growth rate
  and amount of repeated work matter.
- Parallelism has a cover charge: setup, coordination, synchronization, and
  data movement can lose on small inputs, then pay off after a crossover.
- Algorithmic growth and hardware throughput are different ideas. Better
  algorithms change growth; more workers can change constants and throughput.
- A GPU may exist on the host while the particular sandbox or process cannot
  access it. Do not turn GPU presence into fabricated timing data.

## Evidence and defaults

The default Fall 2026 reference is the committed CPU dataset in
`results/parallel_sort_results.csv`, generated on a 13th Gen Intel Core
i7-13700 with 24 logical processors and 24 parallel workers. Read it with
`results/parallel_sort_hardware.txt` and page 07; it contains nine sizes through
20,000,000 values, measured sequential and parallel CPU rows, and no invented
GPU rows. The practical CPU crossover first appears at `n=10,000` in this
dataset, while the small batched rows are explicitly clock-noise-scale.

The alternate historical evidence is the archived pasted transcript at
`sidecar/archive/fall-2026/stuff.md`. It records reverse-sorted Bubble Sort
runs on the host identified in the transcript as `STF259-CZYC704`, including
the 10,000-value run and the later 20,000/30,000 teaching progression. Treat
those seconds as illustrative, not as a canonical machine-independent result.
The browser race page also measures on the viewer's machine and has no durable
Fall 2026 timing table; use its shape, not a universal millisecond claim.

## First things to inspect or rerun

Read this file and `instructor/FALL_2026_ARCHIVE_MANIFEST.md`, then inspect the
CSV and the self-contained pages. For a bounded rerun, use:

```bash
python3 week-06/scripts/01_recursive_fibonacci_trace.py
python3 week-06/scripts/03_iterative_fibonacci_timing.py
python3 week-06/scripts/04_bubble_sort_timing.py
bash week-06/scripts/10_run_parallelism_showdown.sh
```

The Bubble Sort 20,000/30,000 progression is intentionally heavy. Do not run
it casually during class without watching the time and CPU load. The parallel
showdown may be regenerated when a fresh machine-specific reference is wanted;
do not merge different hosts into one dataset. The optional GPU path is
`scripts/12_collect_gpu_parallelism_showdown.sh` and requires a device-enabled
WSL shell with `nvcc` and `nvidia-smi`; no GPU experiment was actually
collected for this archive.

From WSL/Windows, open a self-contained page with:

```bash
explorer.exe "$(wslpath -w week-06/websites/04b_bubble_sort_measured.html)"
```

Other browsers can open the HTML files directly; no server or external chart
library is required.

## Known rough edges and archive map

The old root-level `stuff.md` was conversational residue, so it is preserved
under `sidecar/archive/fall-2026/` rather than left in the class-facing root.
The prior live parallelism receipt remains under
`sidecar/hanna_parallelism_showdown/`; the semester closeout receipt is under
`sidecar/hanna_semester_closeout/`. The LaTeX backdrop is reusable source,
not a claim that a new lecture deck was presented in Fall 2026. Read the
closeout `SUMMARY.md` for the exact final commit and validation state.
