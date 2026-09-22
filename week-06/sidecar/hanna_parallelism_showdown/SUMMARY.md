# Week 6 Parallelism Plot Twist — COMPLETE

Open `week-06/websites/07_parallelism_plot_twist.html`. The self-contained page
is generated from the committed CPU measurements and now visibly extends to
20,000,000 values.

## What ran

- CPU: 13th Gen Intel Core i7-13700 with 24 logical processors.
- CPU paths: `std::sort` versus GNU libstdc++ parallel multiway mergesort via
  OpenMP. A 16-versus-24 worker calibration found that 24 workers win at the
  large far-right points, so 24 is the default. Every output matches an
  independently sorted reference, validating order and multiset preservation.
- GPU: an NVIDIA GeForce RTX 3060 Ti is present in Jeremy's host WSL session,
  but unavailable to this Hanna sandbox. No GPU measurement was fabricated and
  the webpage states that distinction next to the GPU hardware card.

## Measured classroom story

The final fresh 24-worker dataset has nine logarithmic sizes and 18 unique CPU
rows. Parallel sorting loses at `n=10` and `1,000`, first wins at `10,000`, and
has useful far-right separation: `23.30 ms` versus `287.89 ms` at 5 million,
`42.45 ms` versus `604.34 ms` at 10 million, and `86.96 ms` versus `1,274.12 ms`
at 20 million (about 14.7×). An earlier worker calibration also found 24 workers
faster than 16 at 1, 5, 10, and 20 million. The retained small-point overhead,
including minor noise-scale variation, is described honestly rather than smoothed.

## GPU collection outside this sandbox

From Jeremy's device-enabled WSL terminal, run exactly:

```bash
bash week-06/scripts/12_collect_gpu_parallelism_showdown.sh
```

The helper verifies `nvcc` and NVIDIA device access before mutation, preserves
the CPU rows, transactionally replaces only existing GPU rows, records honest
GPU sort-only and end-to-end medians in the same CSV schema, and regenerates the
webpage. Its sandbox preflight failed safely here before changing any evidence.

## Validation and publication

- Two heavy CPU runs completed in roughly 12–14 seconds each, within the live
  demo budget; the second left exactly 18 finite, non-duplicated rows.
- CPU source compiled; Bash scripts and the page generator passed syntax checks.
- The generated page contains the measured 20-million point, 1× speedup line,
  GPU-host-versus-sandbox distinction, overhead reveal, Big-O explanation, and
  no external dependency.

Accepted payload: `216803d4a9cb88b9b64671eca04fab33703444c8`
(`Extend Week 6 parallelism benchmark scale`), pushed to `origin/main`.
