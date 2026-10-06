# Week 8 Tuesday walkthrough — Induction, Recursion & Recurrences

**Tue Oct 6, 12:30–1:45, Stafford Center 259 · 75 minutes**
**Question:** where is the logical bridge, and are we assuming what we are trying to prove?
**Method, every time:** Sources → Rules/Assumptions → Work → Check → One-Sentence Summary.

## Two threads for today

**Thread A — critical thinking.** A pattern is not a proof. Every claim gets *Claim / Evidence / Warrant*, and the question **"What would change my mind?"** Induction is the tool that turns evidence into a warrant.
**Thread B — strategies.** Recursion is **one of many** ways to solve a problem. The skill is knowing *when* it is the natural fit, and being able to defend a choice.

Code and tests: `week-08/teaching/recursion_demo.py`, `test_recursion_demo.py` (`python3 -m pytest -v` in that folder: 32 tests, in teaching order). Hand traces are the real evidence. Code is a live check; you do not need to type it, you can paste it.

## Run-of-show (75 min)

| Clock | Move | Thread | One-line takeaway |
|---|---|---|---|
| 0:00–0:07 | Circle regions: predict n = 6 | A | A pattern is not a proof. |
| 0:07–0:12 | Claim / Evidence / Warrant; "What would change my mind?" | A | Evidence says "so far." A warrant says "always." |
| 0:12–0:24 | S(n): recursion traced, then **proved by induction** | A | Induction turns evidence into a warrant. |
| 0:24–0:30 | Find-the-bug drills (4 specimens) | A | A step that assumes its own result proves nothing. |
| 0:30–0:35 | **Pairs argue:** proof / evidence-only / circular | A | Judge the argument, not the conclusion. |
| 0:35–0:45 | **Five ways** to compute S(n) (+ Fibonacci), real output | B | The same answer five ways; they differ in everything else. |
| 0:45–0:50 | Decision table + when recursion is the natural fit | B | Use recursion when the problem is *made of* smaller copies of itself. |
| 0:50–0:58 | **Strategy Court** | A+B | Pick a strategy, then defend it with claim / evidence / warrant. |
| 0:58–1:08 | Students try: the Tuesday activity | A | |
| 1:08–1:12 | AI check as a critical-thinking drill | A | An answer that looks right still needs the smallest-input test. |
| 1:12–1:15 | Wrap + Decision Gate pointer | | |

If you run long: skip the Fibonacci part of "Five ways", then shorten the drills to two specimens. The Optional demos at the end are not needed.

**How to read the script.** *SAY:* is a literal line you can read aloud. *BOARD:* is what to write. *ASK:* is a question to pose and then wait for (count to ten silently; the silence is the teaching). You do not have to know the answer in advance: every reveal is in this document.

---

## 0:00 Thread A hook: the circle (7 min)

**BOARD:** draw a circle. Put 1 point on it, then 2, 3, 4, 5 points, joining every pair of points by a straight line (chord). Count the regions inside the circle each time. Fill in a table:

```
points n :  1   2   3   4   5   6
regions  :  1   2   4   8  16   ?
```

**SAY:** "Here is a pattern. I have checked it five times. Before I tell you anything, I want your prediction for n = 6. Write a number on paper. Do not talk."

**ASK:** "Hands up for 32." (Most will.) "Anyone for something else? Why?"

**Reveal, live** (run this or just read it; real output):

```python
from math import comb
def regions(n):
    return comb(n, 4) + comb(n, 2) + 1
print([regions(n) for n in range(1, 8)])
```

```
[1, 2, 4, 8, 16, 31, 57]
```

**SAY:** "Thirty-one. Not thirty-two. The pattern 1, 2, 4, 8, 16 held five times and then failed. Five confirmations were not a proof. The real formula is C(n,4) + C(n,2) + 1, and it is not a power of two." (Optional: draw n = 6 with all chords and count; it is fiddly, so only do this if a student insists.)

**Takeaway: a pattern is not a proof. Evidence says "so far"; it cannot say "always."**

---

## 0:07 Name the discipline: Claim / Evidence / Warrant (5 min)

**BOARD:** write this three-line template and leave it up all day.

```
CLAIM     what I say is true, for ALL cases
EVIDENCE  what I observed (checked cases, a trace, a test)
WARRANT   why the evidence COVERS every case (the bridge)

and always:  What would change my mind?
```

**SAY:** "Look at the circle. Claim: regions double every time. Evidence: 1, 2, 4, 8, 16. Warrant: we had none. We just *liked* the pattern. That is the whole discipline in one example. Today's question is: where is the bridge, and are we assuming what we are trying to prove? The bridge *is* the warrant."

**ASK:** "What would have changed my mind about the doubling claim?" (Answer: one counterexample, a single n where it fails. n = 6 was one. A good claim tells you in advance what would break it.)

**BOARD:** under the template, add: *"What would change my mind? → a counterexample, or a gap in the bridge."*

**Takeaway: the habit is not "is it true?" but "what is my warrant, and what would change my mind?"**

---

## 0:12 Induction turns evidence into a warrant: S(n) (12 min)

### Definition (write on board)

- **Base case:** `S(0) = 0`
- **Recursive step:** `S(n) = n + S(n - 1)` for integers `n > 0`

```python
def S(n):
    if n == 0:                 # base case
        return 0
    return n + S(n - 1)        # reduction: n -> n-1 moves toward 0
```

### Trace by hand (build it live, one line at a time)

```
S(3) = 3 + S(2)
     = 3 + (2 + S(1))
     = 3 + (2 + (1 + S(0)))
     = 3 + (2 + (1 + 0))      <- base case stops the trace
     = 3 + (2 + 1)
     = 3 + 3
     = 6
```

Name three things aloud, pointing at each:

1. **Base case:** `S(0) = 0`. It answers without calling anything.
2. **Reduction step:** `n` becomes `n - 1`.
3. **Termination reason:** each call lowers a nonnegative integer by one, so it must reach 0.

### Now the bridge: prove S(n) = n(n+1)/2 by induction

Say this first: **a recursive definition tells us how to compute. It does not prove a formula. Checking S(0) through S(29) is evidence, not proof.** (The test `test_S_matches_closed_form_small_n` does exactly that, and its name says why it is not enough.)

**Claim P(n):** S(n) = n(n+1)/2 for every integer n ≥ 0.

1. **Base case (n = 0):** S(0) = 0, and 0·1/2 = 0. ✔
2. **Inductive hypothesis:** assume P(k) for one particular k ≥ 0, i.e. S(k) = k(k+1)/2.
3. **Inductive step (show P(k+1)):**
   S(k+1) = (k+1) + S(k)  *(the recursive definition, since k+1 > 0)*
   = (k+1) + k(k+1)/2  *(by the hypothesis, the only place we use it)*
   = (k+1)(2 + k)/2
   = (k+1)(k+2)/2, which is P(k+1). ✔

By induction, P(n) holds for all n ≥ 0.

Point at the **bridge**: the step is the move from "true for k" to "true for k+1." The hypothesis is used for k, never for k+1.

**Takeaway: a definition computes; induction proves.**

**SAY (framing it as thread A):** "Notice what induction did. Checking S(0) to S(29) was *evidence*. The base case plus the step is a *warrant*: it covers every n at once. And the question 'what would change my mind?' now has a precise answer: a false base case, or a step that does not follow."

---

## 0:24 Find-the-bug as critical-thinking drills (6 min)

Show each. Each one is a *reasoning* failure, not a typo. Ask "what's wrong, and what's the smallest input that shows it?"

**Bug 1: missing base case.** On screen:

```python
def S(n):
    return n + S(n - 1)
```

(Say: "Claim: this function computes 1+...+n. Evidence: it looks right. Warrant: there is none, because nothing tells it when to stop.") Smallest input: any, e.g. `S(0)` already continues to `S(-1)`. Fix: add `if n == 0: return 0`.

**Bug 2: the reduction goes the wrong way** (this is the activity's T):
`T(0) = 1`, `T(n) = T(n + 1)` for `n > 0`.
A base case exists, but it is never reached from `n = 1`: T(1) = T(2) = T(3) = ... The input grows away from 0. Smallest exposing input: **n = 1**. Note `T(0) = 1` "works", the trap of "it worked once." (Code: `bad_T(1)` hits its depth guard; `bad_T(0)` returns 1.)

**Bug 3: an inductive step that assumes the result.** Show this "proof" of P(n): S(n) = n(n+1)/2:

> *Base case:* n = 0 works.
> *Step:* assume S(n) = n(n+1)/2. Then S(n) = n(n+1)/2. ∎

Ask: "What did the step prove?" Nothing: it restated the hypothesis for the *same* n. The bridge never reached n+1. Compare with the real step above, where we assumed P(k) and derived P(k+1) using the definition `S(k+1) = (k+1) + S(k)`. Circular leap = hypothesis and conclusion are about the same case.

**Bug 4: the sneaky one, with the arrow pointing backward.** "Proof" of P(n): the first n odd numbers add to n²:

> *Base case:* n = 1: 1 = 1². ✔
> *Step:* assume the first **k + 1** odd numbers add to (k+1)². Take away the last one, 2k + 1. Then the first k odd numbers add to (k+1)² − (2k+1) = k². So P(k) holds. ∎

Ask: "Which direction did the bridge go?" It assumed P(**k+1**) to derive P(k): the result for the *next* case is assumed, not earned. Every line of algebra is correct, which is why it hides. Tell-tale: ask "what is assumed" and "what is concluded" and see whether they are in the right order. The same recipe "proves" a false claim (in the code, `odd_sum_bogus_step(4, 26)` happily returns 17, a number that no first-4-odd-numbers sum equals). Real step: P(k) ⇒ P(k+1).

**Bug 5 (use only if you ran optional demo O3): a base case in the wrong place.** "Proof" of n! > 2^n for all n ≥ 0: *Base case n = 0: 0! = 1 > 1 = 2^0 ✔.* Catch: 1 > 1 is false. The claim only holds from n = 4 (see optional demo O3).

**Takeaway: check the base case's truth, and check the direction of the step.**

---

## 0:30 Pairs argue: proof, evidence-only, or circular? (5 min)

**SAY:** "Turn to a neighbor. I will show three short arguments. For each one decide: **proof**, **evidence only**, or **circular**. One minute each, then we vote."

**BOARD:** write the three, one at a time.

> **A.** "n² + n is even for every n, because n = 1 gives 2, n = 2 gives 6, n = 3 gives 12, n = 4 gives 20, all even."
>
> **B.** "Claim: 1 + 2 + ... + n = n(n+1)/2. Base: n = 1 gives 1 = 1. Step: assume it for k; then the sum up to k+1 is (k+1) + k(k+1)/2 = (k+1)(k+2)/2."
>
> **C.** "My recursive function is correct because it calls itself on a smaller problem, and the smaller problem is solved correctly."

**Answers (for you):**
- **A: evidence only.** The *claim is true*, but the argument is four checked cases, exactly like the circle. (A real warrant: n² + n = n(n+1), a product of consecutive integers, so one factor is even.) *Judge the argument, not the conclusion.*
- **B: proof.** Base case checked, hypothesis stated, step derived from the hypothesis for k, landing on the formula for k+1.
- **C: circular.** "The smaller problem is solved correctly" is the very thing to be shown. Missing: a **base case** that is correct and a reduction that **reaches** it. This is how a recursion with no base case feels convincing.

**Takeaway: judge the argument, not the conclusion. A true claim can have a bad argument.**

---

## 0:35 Thread B: five ways to solve one problem (10 min)

**SAY:** "So far recursion is the hero. Now the honest part: recursion is **one** strategy. Same problem, five ways. Problem: add 1 + 2 + ... + n."

**BOARD:** five boxes. Fill them as you run the code.

```python
def sum_recursive(n):  return 0 if n == 0 else n + sum_recursive(n - 1)

def sum_loop(n):
    total = 0
    for i in range(1, n + 1): total += i
    return total

def sum_closed(n):     return n * (n + 1) // 2        # Gauss

def sum_memo(n, _table={0: 0}):                        # dynamic programming
    for i in range(len(_table), n + 1): _table[i] = _table[i - 1] + i
    return _table[n]

def sum_brute(n):      return sum(list(range(1, n + 1)))   # enumerate everything
```

Run them side by side (real output):

```
n=10   [55, 55, 55, 55, 55]
n=100  [5050, 5050, 5050, 5050, 5050]
```

**SAY:** "Five strategies, one answer. They are *equally correct*. So how do we choose? We look at what happens when things get big."

**Break the recursion.** Run `sum_recursive(5000)` (real output):

```
RecursionError: maximum recursion depth exceeded
```

**SAY:** "Python's default limit is about 1000 nested calls. The loop does 5000 happily: `sum_loop(5000)` is `12502500`, same as the closed form and the table. Recursion has a hidden cost: every call waits on the call stack."

**Then the closed form at scale:** `sum_closed(10**9)` is `500000000500000000`, instantly. The loop would grind through a billion steps. The recursion would fail long before.

**Fibonacci in 30 seconds.** **SAY:** "Remember the race in Week 6: why was naive recursive Fibonacci slow?" (It recomputes the same values; take one answer and move on, we are not rebuilding that.) "Fibonacci has its own five ways. Loop: fine. Memoized: fine. Closed form, Binet's formula with square roots, is beautiful... and **wrong**:"

```python
fib_closed(70) == fib_loop(70)   # True
fib_closed(71) == fib_loop(71)   # False: 308061521170130 vs 308061521170129
```

**SAY:** "The formula is *exactly* right on paper, and off by one in floating point at n = 71. Elegance is not correctness. A warrant has to cover the machine you actually run it on."

**Takeaway: five correct answers, five different costs. "Which one?" is a question about the situation, not about taste.**

---

## 0:45 Decision table and "when recursion is the natural fit" (5 min)

**BOARD:** draw this table; fill it with the class, then confirm.

| | Clear to read | Easy to prove correct | Time | Space | Stack risk |
|---|---|---|---|---|---|
| **Recursion** | when it mirrors the definition | very: induction mirrors the code | n steps | n (call stack) | **yes** (n = 5000 failed) |
| **Loop** | very | by a loop invariant (induction again) | n steps | constant | none |
| **Closed form** | terse; needs a proof you trust | needs its own proof (Gauss / induction) | constant | constant | none |
| **Memo / DP** | medium: follows the recurrence | by the recurrence | n once, then lookups | n (a table) | none if filled bottom-up |
| **Brute force** | clearest | easiest: you just add them all | n steps | n (the list) | none, but hopeless at huge n |

**SAY:** "No row wins every column. That is the point. Recursion is the *natural* fit when the **problem is made of smaller copies of itself**:"

- **Nested structures** (a list of lists of lists, to any depth).
- **Trees and directory traversal** (a folder contains folders).
- **Divide and conquer** (merge sort: sort each half, then merge).
- **Definitions that are themselves recursive** (factorial, Fibonacci, a grammar).

**Show one** (real output):

```python
def nested_sum(x):
    if isinstance(x, int): return x               # base case
    return sum(nested_sum(item) for item in x)    # reduce: smaller lists

nested_sum([1, [2, [3, 4]], 5])      # 15
```

**ASK:** "Write this with a loop. What do you need to keep track of?" (A stack of unfinished lists, which is what recursion gives you for free. This is the strongest argument *for* recursion: it lets the language remember where you were.)

Merge sort (one sentence, no code needed): split in half until a list has 0 or 1 items (base case), sort each half, merge. `merge_sort([5, 2, 9, 1, 5, 6])` returns `[1, 2, 5, 5, 6, 9]`.

**When NOT:** when the problem is a flat repetition (summing 1..n, counting), a loop is simpler and has no stack limit. Recursion there is showing off.

**Takeaway: reach for recursion when the data or the definition is recursive; otherwise a loop is usually kinder.**

---

## 0:50 Strategy Court (8 min)

**SAY:** "You are the judges. Three cases. For each, in pairs, **pick a strategy and defend it** with Claim / Evidence / Warrant. You have two minutes per case. Then I call on pairs, and the *other* pairs get to ask 'what would change your mind?'"

**BOARD:** one case at a time.

> **Case 1.** Add up every number stored in a folder tree. Folders contain files and other folders, to unknown depth.
>
> **Case 2.** Compute 1 + 2 + ... + n once, where n = 1,000,000,000.
>
> **Case 3.** A game needs Fibonacci numbers up to F(90), thousands of times per second.

**Strong answers (for you; accept others if the warrant holds):**
- **Case 1: recursion.** Claim: recursion. Evidence: the data nests to unknown depth. Warrant: a folder is "files plus smaller folders," so the structure matches the recursive definition and a base case (a file) ends each branch. Mind-changer: a depth in the millions (stack limit) pushes you to an explicit stack.
- **Case 2: closed form.** Claim: n(n+1)/2. Evidence: it matches the loop for small n and we proved it by induction. Warrant: it is a theorem, so it needs no billion steps. Mind-changer: if we had never proved it, we would test it against the loop first.
- **Case 3: loop or memo table.** Claim: compute once with a loop (or table), then look up. Evidence: same values needed over and over. Warrant: a table is filled once in about 90 steps; naive recursion would redo the work (the Week 6 race), and Binet's formula was wrong by n = 71. Mind-changer: if memory were scarce, recompute with the loop each time.

If a pair picks a "wrong" strategy but defends it with a real warrant and names what would change their mind, **that is a win**. The strategy matters less than the argument.

**Takeaway: the answer is a strategy plus a defense. No defense, no credit.**

---

## 0:58 Students try: the Tuesday activity (10 min)

Source: `week-08/student/tuesday-activity.md`. Individual work, they write Sources / Rules-Assumptions / Work / Check / One-Sentence Summary.

Answer key for you:

1. **S(4)** = 4 + S(3) = 4 + 3 + S(2) = 4 + 3 + 2 + S(1) = 4 + 3 + 2 + 1 + S(0) = **10**. Base: S(0) = 0. Reducing rule: n → n−1.
2. **T:** from n = 1 the input goes 1, 2, 3, ... away from 0, so the base case is never reached. Smallest exposing input: n = 1.
3. **Claim S(n) = n(n+1)/2:** base check S(0) = 0 = 0·1/2. Bridge: assume it for k, then show S(k+1) = (k+1) + S(k) = (k+1) + k(k+1)/2 = (k+1)(k+2)/2. Not acceptable: "assume it works" or "assume it for n+1."

Circulate. Likely stuck points: students trace S(4) but never name the base case; students say T "loops forever" without saying *why* (input moves away from 0).

---

## 1:08 AI check as a critical-thinking drill (4 min)

**SAY:** "An AI gives you this for 'sum 1 to n recursively'. It looks right. Claim, evidence, warrant: go."

```python
def ai_sum(n):
    return n + ai_sum(n - 1) if n > 1 else 1
```

**Evidence the AI offers (and you can reproduce):** `[ai_sum(n) for n in range(1, 6)]` is `[1, 3, 6, 10, 15]`. Looks right!

**ASK:** "What is the smallest input?" Run `ai_sum(0)` (real output: `1`). The correct sum of nothing is `0`. The base case is `n > 1 → ... else 1`, which quietly assumes n ≥ 1. Five correct outputs, one wrong base case: the circle all over again.

**Three checks to teach as a habit:** (1) the **smallest input**, (2) the **reduction step** (does it move toward the base case?), (3) one **nontrivial trace** by hand. For Fibonacci add: *did it state both F(0) and F(1), with the right values?* AI commonly gives recursion with no base case, an inductive step that assumes the result for the next case, or a plausible trace that never terminates.

**Takeaway: an answer that looks right is evidence. Make it earn a warrant.**

---

## 1:12 Wrap (3 min)

**SAY:** "Two things to take home. One: before you believe anything, name the claim, the evidence, the warrant, and what would change your mind. Two: recursion is one tool. Know when the problem is made of smaller copies of itself, and say why you chose it."

Point at the Decision Gate (the ordinary Week 8 gate, not a second Show & Tell report) and Thursday's Show & Tell. Their evidence artifact can be exactly the trace plus a claim / evidence / warrant defense.

**One-Sentence Summary for the board:** *"A pattern is evidence; induction supplies the warrant; and recursion is one strategy we choose when the problem is made of smaller copies of itself."*

---

## Questions that come up (with answers)

**1. "Isn't the recursive definition already a proof that S(n) = n(n+1)/2? It gives the right answers."**
No. The definition tells you how to compute each value. Seeing it match for n = 0..29 is evidence for those cases. Induction is the argument that the match continues for *every* n, by showing the step carries truth from k to k+1.

**2. "Why do we get to assume P(k) in the inductive step? Isn't that assuming what we're proving?"**
We assume it for one particular k, not for the case we are trying to reach. The proof's job is the implication "P(k) ⇒ P(k+1)." Combined with the base case, that chain reaches every n: P(0) gives P(1), gives P(2), and so on. It would be circular only if we assumed P(k+1) to prove P(k+1).

**3. "Why does Fibonacci need two base cases but the sum only one?"**
Look at how far back the rule reaches. S(n) uses only S(n−1), so one starting value suffices. F(n) uses F(n−1) *and* F(n−2); F(2) needs both F(1) and F(0). With only one base case the second branch of the call walks off into negative inputs (or, if you patch it with the wrong value, you get a clean-looking wrong answer).

---

## Optional demos (all tested; use only if time remains or a student asks)

Use any of these as a 5–10 minute detour. They are the earlier plan's demos, kept because they are good.

### Optional demo O1: 52! live (7 min)

**n! counts orderings.** A shuffled deck is one ordering of 52 cards. Run it live:

```python
from math import factorial
print(factorial(52))
print(2 ** 52)
print(52 ** 10)
```

Real output:

```
80658175170943878571660636856403766975289505440883277824000000000000
4503599627370496
144555105949057024
```

Say it: 52! is about 8 × 10^67. 2^52 is about 4.5 × 10^15. 52^10 is about 1.4 × 10^17. **Every well-shuffled deck in history is almost surely a one-off ordering.** Take a vote first: "Will factorial beat n^10 for large n?" Then it does, at n = 15 (`15! = 1,307,674,368,000` vs `15^10 = 576,650,390,625`; `14!` is still smaller than `14^10`).

Factorial is recursive too: `0! = 1`, `n! = n · (n-1)!`. Trace for 5: `5! = 5·4! = 5·4·3! = 5·4·3·2! = 5·4·3·2·1! = 5·4·3·2·1·0! = 120` (base case `0! = 1`; each call lowers n by one).

**Takeaway: we can compute the monster. Can we prove how big it is, for every n? That needs induction (O3).**

### Optional demo O2: Fibonacci, both base cases (12 min)  <- Class Pulse reteach, use if a student raises F(0)/F(1)

*Why Fibonacci again?* In Week 6 we raced recursive Fibonacci against iterative. **One-line callback: "Remember the race in Week 6: why was it slow?"** Take one answer ("it recomputes the same values"), then park speed. Today's Fibonacci is about **correctness**: this is the reteach from the 2026-09-24 Class Pulse, where students mishandled initial conditions F(0) and F(1).

### Recurrence, with BOTH base cases (write all three lines)

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n-1) + F(n-2)` for `n ≥ 2`

Ask: "Why two base cases when S had one?" Answer: this step reaches back **two** places. F(2) needs F(1) and F(0). One starting value cannot feed it.

```python
def fib(n):
    if n == 0:
        return 0               # base case 1
    if n == 1:
        return 1               # base case 2
    return fib(n - 1) + fib(n - 2)
```

(Week 6's `00_recursive_fibonacci_simple.py` writes the same two bases as `if n <= 1: return n`. Same definition, compact. Use whichever form the class remembers.)

### Trace F(5) by hand, working down then back up

```
F(5) = F(4) + F(3)
F(4) = F(3) + F(2)
F(3) = F(2) + F(1)
F(2) = F(1) + F(0) = 1 + 0 = 1     <- first value built from base cases
F(3) = 1 + 1 = 2
F(4) = 2 + 1 = 3
F(5) = 3 + 2 = 5
```

Table on the board: `n: 0 1 2 3 4 5` → `F(n): 0 1 1 2 3 5`. (Real run: `[0, 1, 1, 2, 3, 5, 8, 13]` for n = 0..7.)

### What breaks if a base case is wrong or missing (live demos)

**(a) Missing F(1)**, keeping only `F(0) = 0`:
F(2) = F(1) + F(0), and F(1) = F(0) + F(-1), and F(-1) = F(-2) + F(-3), and so on downward. The input walks past the base case into negatives and never lands on 0 for the second branch. That is non-termination: the reduction does not reliably reach the base case. In `fib_missing_base(5)` a depth guard turns the hang into `RecursionError: no base case reached` (real output, see receipt).

**(b) Wrong F(1)**, say `F(1) = 0` by slip:
Every value is 0, because every value is built from sums of base values. In the run: `[fib_wrong_base(k) for k in range(6)]` → `[0, 0, 0, 0, 0, 0]`. It terminates and looks confident. **Terminating is not the same as correct.** The base cases are the only source of new information; the step just recombines them.

Tie to the question: a wrong base case means we are *assuming* values we never established.

### Short induction proof: sum of the first n Fibonacci numbers

**Claim P(n):** F(1) + F(2) + ... + F(n) = F(n+2) − 1, for every integer n ≥ 0 (empty sum = 0).

1. **Base case (n = 0):** the empty sum is 0, and F(2) − 1 = 1 − 1 = 0. ✔
   *(Sanity, n = 1: F(1) = 1 and F(3) − 1 = 2 − 1 = 1. ✔)*
2. **Inductive hypothesis:** assume P(k) for one k ≥ 0: F(1) + ... + F(k) = F(k+2) − 1.
3. **Inductive step (show P(k+1)):**
   F(1) + ... + F(k) + F(k+1)
   = (F(k+2) − 1) + F(k+1)  *(hypothesis)*
   = (F(k+2) + F(k+1)) − 1
   = F(k+3) − 1  *(Fibonacci recurrence at index k+3 ≥ 2)*, which is P(k+1). ✔

Check against the table: n = 5: 1+1+2+3+5 = 12 = F(7) − 1 = 13 − 1. ✔

Where the recurrence entered: the step's last line *is* the recursive definition. The proof's bridge and the definition's reduction step are the same equation used two ways.

*(Optional, if time: `F(n) < 2^n` needs the hypothesis for both n−1 and n−2 (strong induction), so it needs two base cases, n = 0 and n = 1. Same lesson from the proof side: step reaches back two, so base needs two. Tested for n < 20 only as evidence in `test_fib_less_than_2_pow_n`.)*

**Takeaway: the recurrence only recombines. If the starting values are wrong or missing, every later value is wrong or undefined.**

### Optional demo O3: n! > 2^n, and why the base case is n = 4 (10 min)

Back to the monster. **Claim P(n): n! > 2^n.**

First, **do not start at 0 out of habit.** Test it (real run: `[n for n in range(0, 12) if fact(n) > 2 ** n]` gives `[4, 5, 6, 7, 8, 9, 10, 11]`):

| n | 0 | 1 | 2 | 3 | **4** | 5 |
|---|---|---|---|---|---|---|
| n! | 1 | 1 | 2 | 6 | **24** | 120 |
| 2^n | 1 | 2 | 4 | 8 | **16** | 32 |
| n! > 2^n ? | no (1 > 1 false) | no | no | no | **yes** | yes |

The claim is **false** for n = 0, 1, 2, 3. A "base case" at n = 0 would be checking a false statement. n = 4 is the first place it is true, so the honest claim is **P(n) for every integer n ≥ 4**, and the base case is n = 4. (This is the missing-base-case theme from the other direction: a base case in the wrong place is as bad as none. It is also the Week 6 growth idea: factorial eventually leaves exponential behind, but not from the start.)

1. **Base case (n = 4):** 4! = 24 and 2^4 = 16, and 24 > 16. ✔
2. **Inductive hypothesis:** assume P(k) for one k ≥ 4: k! > 2^k.
3. **Inductive step (show P(k+1)):**
   (k+1)! = (k+1) · k!  *(definition of factorial)*
   > (k+1) · 2^k  *(hypothesis; (k+1) > 0 so the inequality survives multiplying)*
   ≥ 2 · 2^k  *(because k+1 ≥ 5 ≥ 2)*
   = 2^(k+1). ✔

So (k+1)! > 2^(k+1), which is P(k+1). By induction P(n) holds for all n ≥ 4.

Point at the exact line where "k ≥ 4" gets used: it makes k+1 ≥ 5 ≥ 2. (Truth of the base case is what the whole chain rests on; the *step* here would work from k ≥ 1, which is exactly why a lazy "it's fine from 0" feels plausible.)

**Takeaway: start the induction where the claim is true. A proof is only as honest as its base case.**

### Optional demo O4: odd numbers add to n², L-shapes + dominoes (10 min)

**Claim P(n): 1 + 3 + 5 + ... + (2n − 1) = n².** Real run: `[odd_sum(n) for n in range(6)]` gives `[0, 1, 4, 9, 16, 25]`.

Draw it, growing an L-shape at a time (the digit is which odd number added that cell):

```
n=1   n=2     n=3       n=4         n=5
1     1 2     1 2 3     1 2 3 4     1 2 3 4 5
      2 2     2 2 3     2 2 3 4     2 2 3 4 5
              3 3 3     3 3 3 4     3 3 3 4 5
                        4 4 4 4     4 4 4 4 5
                                    5 5 5 5 5
```

Each L has 1, then 3, then 5, then 7, then 9 cells. The n×n square becomes the (n+1)×(n+1) square by wrapping one more L around it. That L has n + n + 1 = **2n + 1** cells, the next odd number. (Real output of `print(L_picture(5))` is the last square.)

Now the same thing in labeled form:

1. **Base case (n = 0 or n = 1):** the empty sum is 0 = 0²; or 1 = 1². ✔
2. **Inductive hypothesis:** assume P(k): the first k odd numbers add to k².
3. **Inductive step (show P(k+1)):**
   (first k odd numbers) + (2k + 1)
   = k² + (2k + 1)  *(hypothesis)*
   = (k + 1)²  *(algebra: the L-shape)*. ✔

**Physical dominoes (take a row of dominoes or a stack of index cards into class):**
- **Base case:** the first domino falls. (Push it.)
- **Step:** if domino k falls, it hits domino k+1. (Show the spacing is right.)
- Then all fall. **No base-case push, nothing falls. Spacing too wide, nothing continues.** That is exactly "base case + bridge."
- Dominoes are a picture, not a proof. The proof is the algebra line, and the step must be a conditional ("if domino k falls, then k+1 falls"), not an assertion that every domino has fallen.

**Takeaway: base case plus "if one falls, the next falls" means all fall.**

### Optional demo O5: Horner polynomial recurrence

#### Extra A: polynomials as recurrences (Horner)

Evaluating `p(x) = a_n x^n + ... + a_0` can be a recurrence on partial results: `p_0(x) = a_n`, `p_k(x) = x · p_{k-1}(x) + a_{n-k}`. Same shape as a recursive definition: a start, then a step that uses the previous value.

Trace for the cubic `p(x) = 2x³ − 6x² + 2x − 1` at `x = 3` (coefficients 2, −6, 2, −1):

```
p_0 = 2
p_1 = 3·2 + (−6)  = 0
p_2 = 3·0 + 2     = 2
p_3 = 3·2 + (−1)  = 5      <- p(3)
```

Direct check: 2·27 − 6·9 + 2·3 − 1 = 54 − 54 + 6 − 1 = **5**. ✔ (Real run: `horner([2,-6,2,-1], 3)` gives `(5, [2, 0, 2, 5])`; the test also compares Horner with direct evaluation for x = −5 ... 5.)

**Payoff, multiplications for degree n** (direct term-by-term with powers built from scratch, vs Horner): degree 3: **9 vs 3**; degree 10: **65 vs 10** (from `op_counts`; direct = n(n+1)/2 powers + n coefficient multiplies, Horner = n). Evaluate the same polynomial in far fewer steps by recognizing a recurrence.

**Takeaway: a good recurrence is also a faster algorithm.**

#### Extra B: the factorial reduction trace
Already in Hook B.

### Optional O6: check for understanding (3 min)

One question on a card or the board, 2 minutes silent, then cold-call:

> "A classmate defines `G(0) = 5`, `G(1) = 5`, `G(n) = G(n-1) + G(n-2)`. Does it terminate? Is it the Fibonacci sequence? What one thing would you check first?"

Good answers: it terminates (both base cases present, reduction reaches them); it is *not* Fibonacci (different base values, so it produces 5, 5, 10, 15, 25, ...); check the base cases first. This lands the point that termination and correctness are separate questions.

---

## Run record (what actually ran)

Python 3.12.3, pytest 9.0.3: `python3 -m pytest -v` in `week-08/teaching/` -> see receipt for the latest count (32 passed at this revision). Real output used above: circle regions `[1, 2, 4, 8, 16, 31, 57]`; five strategies at n = 10, 100; `RecursionError` for `sum_recursive(5000)`; `sum_loop(5000) = 12502500`; `sum_closed(10**9) = 500000000500000000`; Binet fails first at n = 71 (`308061521170130` vs `308061521170129`); `nested_sum([1,[2,[3,4]],5]) = 15`; `merge_sort([5,2,9,1,5,6]) = [1,2,5,5,6,9]`; `ai_sum(0) = 1`. Hand traces and induction proofs are by hand, checked only on small n (evidence, not proof). Timings are a plan, not measured. Dominoes (optional) are a prop.
