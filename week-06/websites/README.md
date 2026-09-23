# Week 6 Classroom Websites

Open these in this order during the lesson.

1. `01_burrito_big_o.html`
   - Concrete anchor for Big O, built from the peanut-butter-banana-burrito timing exercise in class.
   - The jar is opened once (O(1)); the assembly repeats per burrito (O(n)); the largest step dominates as n grows.
   - The jar's duration was never timed in class, so the page makes it a visitor-set slider. No student names appear.

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
   - Use the preserved reverse-sorted 10/100/1,000/10,000/20,000/30,000 run.
   - Watch measured time and one-core work grow; exact seconds are machine-specific.

5. `05_bubble_vs_merge_growth.html`
   - Reveal the recursion plot twist.
   - Compare Bubble Sort O(n²) with the n log₂n growth model for Merge Sort.
   - Use this to separate "recursive" from "slow."

6. `06_live_sorting_runtime_race.html`
   - Run both sorting algorithms on the same deterministic random arrays.
   - Graph actual browser timings.
   - Normal mode is the default classroom run; "turn up the pain" extends to n=8,000.
   - Timings vary by machine, so discuss the shape rather than treating one millisecond value as universal.

## Open locally

From the repository root:

```bash
git pull
xdg-open week-06/websites/02_big_o_growth.html
```

Or open any HTML file directly in a browser. The pages are self-contained and do not require a Python server or external chart library.


7. `07_parallelism_plot_twist.html`
   - Ask whether more CPU cores and then GPU parallelism automatically make sorting faster.
   - Before class, generate the measured version with:
     `bash week-06/scripts/10_run_parallelism_showdown.sh`
   - The experiment compares sequential CPU sort, GNU/OpenMP parallel CPU sort,
     optional CUDA/Thrust GPU sort-only time, and GPU end-to-end time including transfers.
   - Use the 1× speedup line to find where overhead loses and where scale finally pays for it.
   - Tiny inputs are timed in batches and labeled as clock-noise-scale; use their
     direction as an overhead cue, not as a meaningful contest decided by nanoseconds.
   - This host's RTX 3060 Ti is visible to the host WSL session but not to Hanna's
     sandbox. Run `bash week-06/scripts/12_collect_gpu_parallelism_showdown.sh`
     outside that sandbox to append real GPU measurements and regenerate the page.
   - Finish with the reveal: parallelism changes throughput and constants, but growth still matters.

The measured CPU reference behind page 07 is preserved in
`../results/parallel_sort_results.csv` and labeled in
`../results/parallel_sort_hardware.txt`. GPU hardware was known to exist on the
host WSL session, but no GPU timing was collected from the Hanna sandbox.
