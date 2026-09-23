# Fall 2026 Week 6 Archive Manifest

This manifest describes the durable cold-storage package. `SOURCE` means
human- or instructor-authored reusable material; `GENERATED` means reproducible
output; `MEASURED` means machine-specific evidence; `ARCHIVAL` means preserved
history or receipts; `OPTIONAL/EXPERIMENTAL` means useful but not required for
the default lesson.

## Teaching scripts

- `scripts/00_recursive_fibonacci_simple.py` — minimal recursive example — SOURCE.
- `scripts/01_recursive_fibonacci_trace.py` — full operation-count trace — SOURCE.
- `scripts/02_recursive_fibonacci_60_second_race.py` — bounded naive-recursion timing race — SOURCE/OPTIONAL/EXPERIMENTAL.
- `scripts/03_iterative_fibonacci_timing.py` — iterative comparison timing — SOURCE.
- `scripts/04_bubble_sort_timing.py` — reverse-sorted measured Bubble Sort, including 30,000 — SOURCE/MEASURED generator.
- `scripts/07_parallel_sort_cpu.cpp` — sequential vs GNU/OpenMP parallel sort — SOURCE.
- `scripts/08_parallel_sort_gpu.cu` — CUDA/Thrust sort-only and end-to-end path — SOURCE/OPTIONAL/EXPERIMENTAL.
- `scripts/09_build_parallelism_webpage.py` — CSV/metadata to self-contained page generator — SOURCE.
- `scripts/10_run_parallelism_showdown.sh` — CPU benchmark and optional GPU orchestration — SOURCE.
- `scripts/12_collect_gpu_parallelism_showdown.sh` — safe host-side GPU collection helper — SOURCE/OPTIONAL/EXPERIMENTAL.

## Websites

- `websites/02_big_o_growth.html` — interactive growth models — GENERATED/ARCHIVAL.
- `websites/03_fibonacci_recursive_vs_iterative.html` — repeated-work comparison — GENERATED/ARCHIVAL.
- `websites/04_bubble_sort_quadratic_growth.html` — theoretical quadratic model — GENERATED/ARCHIVAL.
- `websites/04b_bubble_sort_measured.html` — measured reverse-sorted Bubble Sort page — GENERATED/MEASURED.
- `websites/05_bubble_vs_merge_growth.html` — recursion-versus-growth comparison — GENERATED/ARCHIVAL.
- `websites/06_live_sorting_runtime_race.html` — viewer-machine Bubble/Merge race — SOURCE/OPTIONAL/EXPERIMENTAL.
- `websites/07_parallelism_plot_twist.html` — generated CPU reference page with honest GPU status — GENERATED/MEASURED.
- `websites/README.md` — classroom order and operating notes — SOURCE.

## Measured results

- `results/parallel_sort_results.csv` — Fall 2026 CPU sequential/parallel medians through 20,000,000 values — MEASURED.
- `results/parallel_sort_hardware.txt` — CPU, worker, and GPU-access provenance — MEASURED/ARCHIVAL.
- `sidecar/archive/fall-2026/stuff.md` — preserved pasted Bubble Sort transcript and host-specific observations — ARCHIVAL/OPTIONAL.

The default reference is the committed CPU CSV plus its hardware note and page
07. The archived transcript is an alternate historical dataset, not merged into
the CSV. GPU hardware was reported present on the host WSL session but no GPU
timings were recorded from the Hanna sandbox.

## Instructor notes and missions

- `README.md` — week purpose, contracts, and archive pointer — SOURCE.
- `instructor/tuesday-run-of-show.md` and `instructor/thursday-run-of-show.md` — actual classroom contracts — SOURCE.
- `instructor/HANNA_PARALLELISM_SHOWDOWN.md` — completed predecessor mission — ARCHIVAL.
- `instructor/HANNA_PRESENTATION_READY.md` — superseded presentation mission pointer — ARCHIVAL.
- `instructor/HANNA_WEEK06_SEMESTER_CLOSEOUT.md` — closeout authority — SOURCE/ARCHIVAL.
- `instructor/week06_algorithms_growth_backdrop.tex` — reusable minimalist Beamer source — SOURCE.
- `instructor/week06_algorithms_growth_backdrop.pdf` — compiled backdrop when the local TeX toolchain is available — GENERATED.

## Student-facing artifacts

- `student/tuesday-activity.md` — contract, trace, edge-case, and invariant activity — SOURCE.
- `student/thursday-show-and-tell.md` — public defense artifact contract — SOURCE.
- `student/decision-gate.md` — individual algorithm-analysis contract — SOURCE.

## Sidecar and receipts

- `sidecar/hanna_parallelism_showdown/` — predecessor mission ledger and accepted evidence — ARCHIVAL.
- `sidecar/hanna_semester_closeout/STATUS.md`, `AUTHORSHIP.md`, `WORKER_INDEX.md`, and `SUMMARY.md` — this closeout's durable receipt — ARCHIVAL.
- `scripts/13_archive_validation.sh` — fast non-destructive archive-integrity check — SOURCE.

Intentionally not canonical: raw conversation residue is not a teaching source;
it is retained only in the archive location above. GPU timing is not claimed;
the CUDA source and helper remain optional until a device-enabled host produces
real measurements. Browser stopwatch values from page 06 are not promoted to a
Fall 2026 measured dataset.
