# Recursion Exploration: Instructor Handoff

Last updated: 2026-10-08

## Purpose and teaching vision

Use three familiar problems to connect function definitions, recurrences, sequences of work, algorithm design, Big O, and observed runtime. The teaching question is not whether recursion is inherently good or bad. Ask when it expresses the problem's structure clearly, then count the work, measure the implementation, and identify the costs the model hides.

The intended through-line is:

1. Define a function and identify its base case and progress toward it.
2. Write a recurrence for the result or for the work performed.
3. Expand the recurrence into a sequence or closed form.
4. State the cost model and derive O / Theta bounds.
5. Count selected operations in code and compare those counts with the derivation.
6. Time the implementations and compare actual measurements with scaled growth curves.
7. Explain differences using constants, repeated work, call depth, input shape, Python integer size, and machine noise.

Big O is not a stopwatch prediction. It captures an asymptotic growth shape under an explicit cost model; the instrumented counts show the operations selected by that model, while wall time includes interpreter, representation, and hardware costs.

## Teaching points by example

### Sum from 0 through n

- Compare the direct formula, loop, and recursive definition.
- Formula: count three arithmetic operators in the unit-cost model, giving O(1). Python's arbitrary-precision integer costs rise with the bit length, so the measured line need not be perfectly flat for huge n.
- Loop: n + 1 iterations/additions, giving Theta(n) time and O(1) extra space.
- Recursion: C(0) = 1 and C(n) = C(n - 1) + 1, so n + 1 calls; n additions; Theta(n) time and O(n) call-stack space.
- The notebook raises Python's recursion limit to 5,000, verifies a recursive call at n = 4,900, then catches the expected RecursionError above the limit. This probes the implementation boundary without leaving the kernel crashed.
- Timing experiment target is 35 seconds, with a 95-second safety stop. It times all three methods at modest sizes and formula/loop at larger sizes through six million.

### Fibonacci

- Plain recursion directly mirrors F(n) = F(n - 1) + F(n - 2), but recomputes overlapping subproblems.
- Its call count satisfies C(0) = C(1) = 1 and C(n) = C(n - 1) + C(n - 2) + 1, giving C(n) = 2F(n + 1) - 1 and Theta(phi^n) work.
- The loop makes n additions in Theta(n) time and O(1) extra space.
- Memoization computes each distinct F(k) once: Theta(n) work and O(n) cache space, while retaining an O(n) recursive depth.
- Fibonacci values themselves have Theta(n) bits. Unit-cost arithmetic hides the increasing cost of additions; mention this when observed timings bend away from simple linear references.
- The notebook probes memoized recursion at n = 4,900 with a 5,000 call limit. Naive recursion is intentionally timed only through n = 30.
- Timing experiment target is 10 seconds, with a 25-second safety stop.

### Sorting

- Bubble sort is iterative and easy to trace. With its early exit, sorted input makes n - 1 comparisons (Theta(n)); reverse input makes n(n - 1)/2 comparisons (Theta(n^2)). The implementation copies its input, so this version uses O(n) extra space.
- Merge sort gives recursion a natural role: sort two smaller halves and merge. T(n) = 2T(n/2) + c*n yields Theta(n log n) time and O(n) extra space.
- Python's built-in sort is the practical reference. It is stable and adaptive; CPython's implementation is Timsort. The notebook counts comparisons through a wrapper but times native sorting separately.
- Comparison counts vary with data arrangement, especially for bubble sort and Python's adaptive sort. Compare sorted, reverse, duplicate-heavy, and fixed-seed random inputs.
- Timing experiment target is 10 seconds, with a 25-second safety stop.

## Files

- `01-summing-recursion.ipynb`: detailed derivation, counted operations, depth probe, timed benchmark, and three SVG graphs.
- `02-fibonacci-overlapping-work.ipynb`: naive/iterative/memoized implementations, call counts, depth probe, timed benchmark, and growth graphs.
- `03-sorting-and-decomposition.ipynb`: bubble/merge/built-in sort, comparison counts, timed benchmark, and growth graphs.
- `recursion-and-alternatives.ipynb`: concise all-in-one overview; its original compressed list comprehension was replaced with a readable loop.
- `recursion-stories.html`: self-contained interactive browser companion; its JavaScript demos illustrate the same ideas as the Python notebooks.
- `run-notebooks.py`: lightweight runner for this Python-only notebook set when Jupyter packages are unavailable. It executes cells, captures text and SVG outputs, and saves those outputs into each notebook. For normal interactive work, open the notebooks in VS Code with a Jupyter kernel.

## Current execution state

The current workspace Python is 3.12.10, with the default recursion limit at 1,000. Jupyter, nbconvert, nbclient, nbformat, ipykernel, and IPython are not installed in that Python environment. The background run therefore uses `run-notebooks.py`, which supplies the SVG display hook used by these notebooks and writes executed outputs back into the `.ipynb` files.

The first all-notebook run completed successfully in 55.9 seconds: sum 35.3 seconds, Fibonacci 10.1 seconds, sorting 10.1 seconds, and the combined overview 0.3 seconds. It saved 3 SVG graphs in the sum notebook and 2 each in Fibonacci and sorting; no code-cell errors were recorded.

One caveat: that first run used one Python process for all notebooks, so the sum notebook's change to a 5,000 recursion limit carried into Fibonacci. The Fibonacci output consequently says its previous limit was 5,000, though a fresh kernel starts at 1,000. The runner has since been patched to reset the initial recursion limit between notebooks. That isolation fix has not been rerun yet; the user asked to push the current work without waiting for another run. When resuming, rerun the four notebooks to refresh outputs with the corrected starting-limit record.

The depth probes themselves completed without errors. The sum notebook completed at n = 4,900 and caught the deeper RecursionError; Fibonacci memoization completed at n = 4,900 and caught its deeper RecursionError.

Current handoff action: commit and push all current notebooks, saved outputs, runner fix, and this handoff to `origin/main`.

## Resume commands

From the repository root in PowerShell:

```powershell
code .\week-09\instructor
```

Open `recursion-stories.html` in a browser for the interactive companion. Open a notebook in VS Code and run its cells with a configured Jupyter kernel. To execute all notebooks through the included lightweight runner:

```powershell
python .\week-09\instructor\run-notebooks.py
```

## Conversation decisions to preserve

- Keep the teaching prose in Markdown cells; derive each method's bound before showing comparison graphs.
- Prefer named intermediate variables, explicit loops, and printed rows over compressed one-line list comprehensions.
- Graph measured results against normalized Big O reference shapes, and separately graph counted operations against their recurrences.
- Keep the sum experiment between 30 seconds and two minutes; the current target is about 35 seconds.
- User authorized raising Python's recursion limit for controlled exploration and requested frequent commits.
- User plans to step away and resume later; use this file as the source of task status and pedagogical intent.
