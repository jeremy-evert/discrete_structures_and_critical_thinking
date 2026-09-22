# Morgan validation record

This records Morgan’s independent Python multiprocessing run on 2026-09-22. Its measurements are kept separately from the published GNU/OpenMP run because the hosts and algorithms differ. The original commits remain in the merge history.

## Original AUTHORSHIP.md

# Authorship — Hanna Week 6 Parallelism Showdown

- 2026-09-22 — Hanna inspected the clean DSCT `main` checkout and its sole worktree.
- 2026-09-22 — Hardware preflight found an Intel Core i7-8700K exposed as 12 logical processors, no installed C++ compiler, and no accessible CUDA backend. `nvidia-smi` failed to initialize NVML; `nvcc`, CuPy, PyTorch, and Numba were unavailable.
- 2026-09-22 — The original launcher was run and failed only because it required `g++`. Hanna replaced that missing-toolchain path with a standard-library Python multiprocessing chunk-sort-and-merge benchmark. It warms a persistent process pool, uses deterministic identical data, verifies exact sorted output/multiset equality, includes dispatch and merging in parallel timings, and writes a fresh CSV atomically.
- 2026-09-22 — Tiny jobs were changed to batched identical operations per timed sample so per-sort values do not depend on sub-microsecond clock resolution.

## Original STATUS.md

# Hanna Week 6 Parallelism Showdown

HUMAN_GATE — the class-ready benchmark and page are complete locally, but publication is blocked by unavailable GitHub SSH credentials on this host.

Class-ready implementation commit: `e5a9362c82cd8e5c8099361ee08665e8c4cc5e3a`.
Local validation/receipt commit: `4afa9a7` (the publication-gate receipt follows this status update).

## Original SUMMARY.md

# Week 6 Parallelism Showdown — Summary

**Status:** HUMAN_GATE — implementation and validation are complete, but the authorized push cannot authenticate from this host.

Open `week-06/websites/07_parallelism_plot_twist.html` directly from disk.
The class-ready benchmark/page implementation is commit
`e5a9362c82cd8e5c8099361ee08665e8c4cc5e3a`.

## What this host actually provided

- Intel Core i7-8700K exposed as 12 logical processors; the experiment used 12 worker processes.
- No C++ compiler was installed, so the launcher selected its standard-library Python multiprocessing fallback: concurrent chunk sorts plus the required final merge.
- No usable GPU backend was available: NVML was inaccessible, `nvcc` was absent, and CuPy, PyTorch, and Numba were not installed. No GPU result was fabricated.

## Measured lesson

The CPU-parallel path was slower at small sizes because dispatching chunks and merging results has a real cover charge. On the final fresh run it first beat the sequential CPU baseline at 1,048,576 values and remained ahead at 2,097,152 values. The exact medians are committed in `week-06/results/parallel_sort_results.csv`; the webpage embeds that data and labels the GPU gap.

Each backend receives deterministic identical input. The pool is warmed, medians are recorded, tiny inputs are batched before timing, and every result is checked against an exact sequential sorted oracle (therefore sorted and multiset-preserving). The parallel timing honestly includes process dispatch, coordination, and merge.

## Repair history and verification

The original launcher failed because it unconditionally required `g++`. It now retains the GNU/OpenMP path when `g++` exists and otherwise runs the tested multiprocessing fallback. Results are overwritten atomically, so a fresh rerun has one header and exactly one row per backend/size. A second fresh run verified 14 finite, nonnegative CPU rows with no duplicate append contamination. The generated local HTML has embedded data, a 1× speedup reference, the CPU/GPU-units caveat, and no external dependencies.

## Publication gate

The local branch is two ordinary forward commits ahead of `origin/main`:
`e5a9362` and `4afa9a7`. A normal `git push origin main` was blocked before authentication because the host's `/etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf` has unsafe ownership or permissions. Retrying with that config bypassed reached GitHub, which rejected the connection with `Permission denied (publickey)`; `ssh-add -l` also reported no authentication agent.

The smallest required human action is to make an authorized GitHub SSH key/agent available to this host (or provide an approved authenticated Git transport), then run a normal non-force push of the existing commits. No code, benchmark, driver, or system change remains needed.

## Original WORKER_INDEX.md

# Worker Index — Hanna Week 6 Parallelism Showdown

No child workers were used. Hanna performed the bounded implementation and validation directly.
