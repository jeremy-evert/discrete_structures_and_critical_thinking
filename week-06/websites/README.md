# Week 6 Classroom Websites

Open these self-contained local files in this order during the lesson. The
speaker path, including code demonstrations and prompts, is in
[`../instructor/PRESENTATION_RUNBOOK.md`](../instructor/PRESENTATION_RUNBOOK.md).

1. `02_big_o_growth.html`
   - Introduce Big O as a question about what happens when input size grows.
   - Compare O(1), O(log n), O(n), O(n log n), O(n²), and O(2ⁿ).
   - Use the slider first; turn on log scale after the exponential curve runs away.

2. `03_fibonacci_recursive_vs_iterative.html`
   - Compare exact call counts for naive recursive Fibonacci with iterative loop steps.
   - Connect this page to `../scripts/01_recursive_fibonacci_trace.py`.
   - Ask students where repeated work appears.

3. `04_bubble_sort_quadratic_growth.html`
   - Show worst-case Bubble Sort comparison growth.
   - Have students predict the effect of doubling n before clicking the button.
   - The multiplier approaches 4×.

4. `04b_bubble_sort_measured.html`
   - Show the committed, machine-specific reverse-sorted Bubble Sort run:
     10, 100, 1,000, 10,000, 20,000, and 30,000 values.
   - It is the measured bridge from the growth model to a real stopwatch.
   - To regenerate it on the presentation machine, run
     `python3 week-06/scripts/04_bubble_sort_timing.py`; timings will change
     with the machine, but the measured page remains local and self-contained.

5. `05_bubble_vs_merge_growth.html`
   - Reveal the recursion plot twist.
   - Compare Bubble Sort O(n²) with the n log₂n growth model for Merge Sort.
   - Use this to separate "recursive" from "slow."

6. `06_live_sorting_runtime_race.html`
   - Run both sorting algorithms on the same deterministic random arrays.
   - Graph actual browser timings.
   - Normal mode is the default classroom run; "turn up the pain" extends to n=8,000.
   - Timings vary by machine, so discuss the shape rather than treating one millisecond value as universal.

7. `07_parallelism_plot_twist.html`
   - Ask whether more CPU workers and then GPU parallelism automatically make
     sorting faster.
   - The committed default dataset is the labelled 24-worker i7-13700 CPU
     measurement in `../results/parallel_sort_results.csv`. The preserved
     `morgan_python_parallel_sort_results.csv` is an alternate 12-worker
     i7-8700K measurement, not a dataset to combine with the default.
   - Tiny points are clock-noise-scale; use them as an overhead cue, then use
     the larger points for the crossover and scale story.
   - GPU data is absent because the accessible Hanna environment had no CUDA
     device; no timings were invented. A device-enabled WSL shell may add real
     GPU measurements with
     `bash week-06/scripts/12_collect_gpu_parallelism_showdown.sh`.

## Open locally on WSL

From the repository root:

```bash
explorer.exe "$(wslpath -w week-06/websites/02_big_o_growth.html)"
```

Or open any HTML file directly in a browser. The pages do not require a Python
server or an external chart library.
