# Week 10 Tuesday — the code, one small step at a time

Python 3, nothing to install. Six files. **Each one is the previous one plus
one change.** Read the change, not the whole file.

    ./check_my_setup.sh       # or: python3 test_screening.py
    python3 v1_counts.py
    python3 compare.py v1 v2       # shows ONLY what changed

| File | What it adds | The thinking move |
|---|---|---|
| `v1_counts.py` | The four-cell table, numbers typed by hand | **Name the question**: whose group is the denominator? |
| `v2_function.py` | Cells computed from three inputs | **Make the assumptions visible**: they are now arguments |
| `v3_two_conditionals.py` | `P(+|C)` and `P(C|+)` side by side | **Charity, then precision**: the "90%" claim is true of one of these |
| `v4_change_prevalence.py` | A loop over prevalence | **Predict, then run**: write your guess down first |
| `v5_simulation.py` | A million simulated people | **What does agreement check?** The code, not the world |
| `v6_wrong_assumption.py` | A subgroup the stated rates ignore | **What would change my mind?** Evidence about the population |

`test_screening.py` holds four checks. They pass before you start; keep them
passing.

## The critical-thinking overlay: answer the question that was asked

Base-rate neglect is not bad arithmetic. It is answering a *different
question* than the one asked. "The test is 90% accurate" answers "if you have
it, does it catch you?" The patient asked "I tested positive, do I have it?"

Three habits, one per stage of the work:

1. **Name the question** — write `P(?  |  ?)` before computing. The thing
   after the bar is your denominator.
2. **Predict, then check** — write the number you expect, then compare. A
   wrong prediction is the most informative result in the room.
3. **Say what the check cannot check** — a table and a simulation that agree
   have confirmed the *code*. Only evidence about the population can confirm
   the *assumptions*.

Be charitable first: the person saying "90% accurate" is not lying. Find the
true statement inside the claim, then show which question it answers.

## Where this lands in the Decision Gate

| Gate heading | Code that supports it |
|---|---|
| Sources | the three inputs in `v2` |
| Rules / Assumptions | the "applies to this population" line; `v6` shows it failing |
| Work | `v1`/`v2`/`v3` |
| Check | totals assert (v2), changed prevalence (v4), simulation (v5) |
| One-Sentence Summary | no stronger than `v6` allows |

An AI answer is not evidence until you have rerun the numbers yourself.
