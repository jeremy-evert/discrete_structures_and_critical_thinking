# Week 6 Parallelism Plot Twist — COMPLETE

Open `week-06/websites/07_parallelism_plot_twist.html`. It is self-contained,
generated from the committed measured CSV, and needs no web server or external
chart library.

## What actually ran

- CPU: 13th Gen Intel Core i7-13700, 24 logical processors.
- CPU benchmark: `std::sort` versus GNU libstdc++ parallel multiway mergesort
  via OpenMP, with 16 requested parallel workers. Each output is compared with
  an independently sorted reference, verifying both order and the input multiset.
- GPU: no real GPU backend ran. NVML reports OS-blocked GPU access; `nvcc`,
  CuPy, PyTorch, and Numba were unavailable. The page says so plainly and
  includes no invented GPU curve.

## Measured classroom story

Parallel CPU sorting lost at the tiny points (`n=10`, `100`, and `1,000`) and
first beat the sequential baseline at `n=10,000`. It remained ahead through
`10,000,000`; the fresh run measured about 13.6× at the crossover point and
roughly 6.9–10.4× at the larger points. Tiny points are batched independent
sorts and labeled clock-noise-scale, so the lesson treats them as overhead
evidence rather than pretending a nanosecond difference is decisive.

The page separates measured runtime from speedup, draws a visible 1×
break-even line, reveals parallelism's overhead, explains why CPU cores and
GPU execution units are not interchangeable, and correctly connects hardware
throughput back to `O(n log n)` growth.

## Repairs and verification

- Removed the host-name field from persisted metadata.
- Added reference-output correctness checks and a `timed_sorts` CSV field.
- Confirmed a second fresh run creates exactly 16 finite CPU rows with no stale
  append contamination or duplicate header.
- Compiled the CPU source; syntax-checked the runner and Python generator;
  checked the generated HTML for its required classroom content and absence of
  external dependencies.

Accepted class-ready payload: `4aa02dd83ea4582c59fe7225c46cbd13011e052d`
(`Finish Week 6 parallelism showdown benchmark`), pushed to `origin/main`.

Deeper evidence: `AUTHORSHIP.md`, `WORKER_INDEX.md`,
`../../results/parallel_sort_results.csv`, and
`../../results/parallel_sort_hardware.txt`.
