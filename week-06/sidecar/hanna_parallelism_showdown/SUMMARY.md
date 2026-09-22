# Week 6 Parallelism Plot Twist — running summary

Publication is still pending final fresh-run idempotence and Git review.

Current evidence:

- `../results/parallel_sort_results.csv` contains fresh median CPU measurements from this host.
- `../results/parallel_sort_hardware.txt` records only classroom-relevant, non-identifying hardware metadata.
- `../websites/07_parallelism_plot_twist.html` is generated directly from those measurements and is self-contained.
- The CPU parallel path is GNU libstdc++ parallel multiway mergesort through OpenMP with 16 requested workers; it first beat the sequential baseline at `n=10,000` in the current run.
- The GPU demonstration is unavailable on this host: NVML reports OS-blocked GPU access, no `nvcc` is installed, and no installed GPU Python backend is usable. No GPU curves are present.
