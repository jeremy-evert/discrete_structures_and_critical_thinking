# Authorship — Hanna Week 6 Parallelism Showdown

- 2026-09-22 — Hanna inspected the clean DSCT `main` checkout and its sole worktree.
- 2026-09-22 — Hardware preflight found an Intel Core i7-8700K exposed as 12 logical processors, no installed C++ compiler, and no accessible CUDA backend. `nvidia-smi` failed to initialize NVML; `nvcc`, CuPy, PyTorch, and Numba were unavailable.
- 2026-09-22 — The original launcher was run and failed only because it required `g++`. Hanna replaced that missing-toolchain path with a standard-library Python multiprocessing chunk-sort-and-merge benchmark. It warms a persistent process pool, uses deterministic identical data, verifies exact sorted output/multiset equality, includes dispatch and merging in parallel timings, and writes a fresh CSV atomically.
- 2026-09-22 — Tiny jobs were changed to batched identical operations per timed sample so per-sort values do not depend on sub-microsecond clock resolution.
