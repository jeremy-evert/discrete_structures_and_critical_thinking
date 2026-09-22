# Week 6 Parallelism Showdown — Summary

**Status:** COMPLETE

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
