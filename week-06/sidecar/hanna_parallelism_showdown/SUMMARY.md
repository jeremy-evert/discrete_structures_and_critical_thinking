# Week 6 Parallelism Plot Twist — running follow-up

Publication is pending the final Git review of the extended 20-million-value
CPU dataset and GPU-access clarification.

- The benchmark now uses all 24 logical CPU workers by default after a direct
  16-versus-24 calibration showed a 24-worker far-right advantage.
- The committed result schema now has nine logarithmic CPU sizes through
  20,000,000 values; a fresh rerun produced exactly 18 finite, non-duplicated
  CPU rows and a real 20-million parallel win.
- The host WSL session has an NVIDIA GeForce RTX 3060 Ti, but this Hanna sandbox
  cannot access its NVIDIA device or CUDA toolchain. No GPU measurements were
  fabricated. `scripts/12_collect_gpu_parallelism_showdown.sh` is the one-command
  out-of-sandbox collector; it preserves CPU rows, replaces only prior GPU rows,
  and regenerates the webpage after real CUDA measurements complete.
