# Week 6 presentation runbook — Algorithms, Correctness & Growth

Before class, run `bash week-06/scripts/13_preclass_check.sh` from the repository root.
Open local HTML pages on WSL with `explorer.exe "$(wslpath -w PATH)"`; no web server or network is needed.

| Step | Open or run | Say | Ask | Reveal | Next |
|---|---|---|---|---|---|
| 1. Growth | `explorer.exe "$(wslpath -w week-06/websites/02_big_o_growth.html)"` | “Today is about what happens when the problem gets bigger, not one lucky fast answer.” Move the slider, then enable log scale. | “Which curve stays manageable if input becomes a million times larger?” | Growth shape matters more than a single stopwatch result. | Read a correct recursive program. |
| 2. Simple Fibonacci | `python3 week-06/scripts/00_recursive_fibonacci_simple.py` | “The base cases make this correct; every other call asks two smaller questions.” | “What makes it stop, and where might it repeat work?” | Correctness and efficiency are separate claims. | Trace the calls. |
| 3. Recursive trace | `python3 week-06/scripts/01_recursive_fibonacci_trace.py` | “The trace counts chosen algorithmic operations, not Python internals.” | “Which `fib(n)` calls appear in more than one branch?” | The recursion tree duplicates subproblems. | Put a limit on the class clock. |
| 4. 60-second race | `python3 week-06/scripts/02_recursive_fibonacci_60_second_race.py` | “We stop deliberately after one minute; a bounded experiment protects class time.” | “The answer is correct, so why does the larger target become a problem?” | Naive recursion repeats work at an explosive rate. | Run the same targets iteratively. |
| 5. Iterative contrast | `python3 week-06/scripts/03_iterative_fibonacci_timing.py` | “The answer did not change; the amount of repeated work did.” | “What changed in the algorithm, and what did not?” | Iteration makes one progressing pass rather than rebuilding the tree. | Compare the growth models. |
| 6. Fibonacci models | `explorer.exe "$(wslpath -w week-06/websites/03_fibonacci_recursive_vs_iterative.html)"` | “This compares naive call counts with iterative loop steps.” | “Where does repeated work become the dominant story?” | A working program can still have a disastrous growth curve. | Predict Bubble Sort. |
| 7. Bubble model | `explorer.exe "$(wslpath -w week-06/websites/04_bubble_sort_quadratic_growth.html)"` | “Predict before we measure: worst-case Bubble Sort compares neighbors over repeated passes.” | “Does doubling `n` mean roughly 2× or 4× comparisons?” | The comparison model is quadratic. | Show the measured run. |
| 8. Measured Bubble Sort | `explorer.exe "$(wslpath -w week-06/websites/04b_bubble_sort_measured.html)"` | “This is a reverse-sorted, host-specific measurement; its shape is the lesson.” | “When `n` grows by 10×, is this closer to 10× or 100×?” | Bubble Sort trends toward `n²`. For a live version, use `htop` in one terminal and `python3 week-06/scripts/04_bubble_sort_timing.py` in another. Its intentional 10/100/1,000/10,000/20,000/30,000 progression lights up roughly one logical core; that is a feature. | Separate recursion from slowness. |
| 9. Bubble vs Merge | `explorer.exe "$(wslpath -w week-06/websites/05_bubble_vs_merge_growth.html)"` | “Bubble Sort is iterative and quadratic; Merge Sort is recursive and follows `n log₂n` growth.” | “What actually makes one curve win?” | Recursion is a technique, not a complexity class. | Race the algorithms. |
| 10. Live runtime race | `explorer.exe "$(wslpath -w week-06/websites/06_live_sorting_runtime_race.html)"` | “Both algorithms receive the same deterministic arrays in this browser; look for shape, not universal milliseconds.” | “Why does the gap widen when we turn up the pain?” | Better growth dominates as inputs grow. | Bait the hardware answer. |
| 11. Parallelism | `explorer.exe "$(wslpath -w week-06/websites/07_parallelism_plot_twist.html)"` | “The default chart is a labelled i7-13700, 24-worker CPU measurement. Morgan’s 12-worker Python data is preserved separately, never mixed. GPU access was unavailable here, so no GPU timing was invented.” | “Will more CPU workers—or a GPU—win at every input size?” | Division, coordination, synchronization, and transfers cost something; scale can eventually repay that cost. GPU execution units are not CPU cores. A device-enabled WSL shell may collect real GPU data with `bash week-06/scripts/12_collect_gpu_parallelism_showdown.sh`. | Close the loop. |

## Closing synthesis

Say: “Correctness tells us whether an algorithm solves the problem. Growth tells us whether it remains useful as the problem grows. Better algorithms change the growth story; parallelism changes throughput and constants.”

Ask: “What evidence would you need before claiming an optimization really helps?”

Reveal: Measure honestly, state the input and timing boundary, and distinguish one observation from a general claim.
