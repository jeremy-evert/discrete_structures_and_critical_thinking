# Tuesday activity — A few passing tests prove what?

Inspect this procedure, which should return the largest value in a nonempty
list of integers:

```text
largest(L):
    best = 0
    for each x in L:
        if x > best: best = x
    return best
```

1. State the intended input and output contract.
2. Trace the procedure on `[3, 1, 4]` and on `[-3, -1, -4]` in a table showing
   `x` and `best` after each step.
3. Does it meet the contract on both lists? If not, give the smallest repair
   you can justify.
4. State an invariant for a repaired version: after processing some items,
   what must `best` represent?
5. Count comparisons for lists of length 1, 2, and 5. What cautious claim can
   you make about growth? What does this count *not* prove?

Use Sources, Rules/Assumptions, Work, Check, and One-Sentence Summary. Your
check must include an edge case, not only the friendly list.

## AI fluency prompt

If an AI system repairs the procedure, independently trace its version on the
negative list and one single-item list. Identify the input assumption it made.
Do not accept “linear time” without showing what operation was counted.
