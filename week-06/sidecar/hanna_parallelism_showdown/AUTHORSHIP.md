# Hanna authorship ledger — Week 6 Parallelism Plot Twist

## 2026-09-22 — dispatch, diagnosis, and repair

- Verified dispatch SHA-256 `a636feca46e557de550c9565799b444c78beb82c0a6bf50c74d8a4983db54ca8` and read the project-local mission before acting.
- Inspected the clean DSCT `main` worktree, origin, recent history, worktree inventory, CPU/toolchain, and installed GPU backends. The host provides a 13th Gen Intel Core i7-13700 with 24 logical processors, `g++` 11.4.0, and Python 3.10.12. NVIDIA access is OS-blocked; `nvcc`, CuPy, PyTorch, and Numba are unavailable, so no GPU result was invented.
- Ran the original command once. It completed CPU measurements and identified a CPU crossover at `n=10,000`, but the generated metadata included the host name, tiny rows were below a useful timing scale, and sorting correctness did not independently verify the source multiset.
- Repaired only `week-06/**`: sanitized metadata, added reference-output equality checks, batched tiny independent sort samples, recorded their batch count in the CSV, and made the page explain their clock-noise-scale limitation.
- Compiled the CPU benchmark and syntax-checked the runner and page generator. A fresh run produced the current results and self-contained classroom page. CSV and HTML structural checks passed.
- Ran the command a second time: it replaced the CSV with exactly 16 finite expected CPU rows and no duplicate headers or stale append data. The page retained its measured data, 1× break-even reference, CPU/GPU-unit distinction, overhead reveal, Big-O explanation, and no external dependencies.
- Inspected the bounded staged diff, committed the accepted class-ready payload as `4aa02dd83ea4582c59fe7225c46cbd13011e052d`, and pushed it normally to `origin/main`.

## 2026-09-22 — extended-scale follow-up

- Re-inspected the clean published worktree and available memory (about 5.7 GiB) before extending the staircase to 20,000,000 values.
- Calibrated both 16 and 24 OpenMP workers through the full data range. At 20,000,000 values, 24 workers measured 95.187 ms versus 113.469 ms for 16; 24 also won at 1,000,000, 5,000,000, and 10,000,000. The smaller 16-worker wins do not outweigh the requested far-right throughput goal, so the published default is the full 24 logical workers.
- Corrected the GPU account using Jeremy's host fact: an NVIDIA RTX 3060 Ti is present in the host WSL session, while this Hanna sandbox cannot access the NVIDIA device or CUDA toolchain. Added a transactional out-of-sandbox helper that preserves CPU rows, replaces only prior GPU rows, verifies device access, and regenerates the page from real GPU measurements.
