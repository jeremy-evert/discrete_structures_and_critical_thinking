# Week 8 Tuesday walkthrough — Induction, Recursion & Recurrences

**Tue Oct 6, 12:30–1:45, Stafford Center 259 · 75 minutes**
**Question:** where is the logical bridge, and are we assuming what we are trying to prove?
**Targets:** tell a base case from a recursive/inductive step; trace a terminating recursive definition; spot a missing base case or a circular leap.
**Method, every time:** Sources → Rules/Assumptions → Work → Check → One-Sentence Summary.

Code and tests: `week-08/teaching/recursion_demo.py`, `test_recursion_demo.py` (run `python3 -m pytest -v` from that folder). Code is optional on screen; hand traces are the evidence. Tests are in teaching order, so reading them top to bottom replays the class.

| Clock | Move |
|---|---|
| 0:00–0:08 | Opening hook |
| 0:08–0:22 | Worked example 1: sum S(n), traced, then proved |
| 0:22–0:32 | Worked example 2 (brief): factorial |
| 0:32–0:47 | Worked example 3: Fibonacci, two base cases, proof |
| 0:47–0:55 | Find the bug |
| 0:55–1:08 | Students try: the Tuesday activity |
| 1:08–1:13 | Check for understanding |
| 1:13–1:15 | AI check and Decision Gate pointer |

(Timing is a suggestion. If you run long, shrink factorial to two minutes; it adds no new idea.)

---

## 0:00 Opening hook (8 min)

Put this on screen, say nothing about what is wrong with it:

```python
def S(n):
    return n + S(n - 1)
```

Ask: "Polished, short, looks right. What does `S(3)` do?" Let them reach: it calls S(2), S(1), S(0), S(-1)... it never stops. Python eventually raises `RecursionError`. Nothing in the code says when to stop.

Line for the board: **A recursive definition needs a place to stop, and every step has to move toward it.**

Then the Week 8 question: "Where is the logical bridge, and are we assuming what we are trying to prove?" We will use it twice today: once for recursion (does it stop?) and once for induction (does the step earn its claim?).

---

## 0:08 Worked example 1: the sum S(n) (14 min)

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

---

## 0:22 Worked example 2 (brief): factorial (10 min)

`0! = 1`, `n! = n · (n-1)!` for n > 0. Trace `fact(4)`: `4·3·2·1·fact(0) = 24`. Ask one question: "What if the base case said `fact(0) = 0`?" (Every answer collapses to 0; same shape, wrong value. Hold that thought, because Fibonacci makes it sharper.)

---

## 0:32 Worked example 3: Fibonacci (15 min)

*Why again?* In Week 6 we raced recursive Fibonacci against iterative. **One-line callback: "Remember the race in Week 6: why was it slow?"** Take one answer ("it recomputes the same values"), then park speed. Today's Fibonacci is about **correctness**: this is the reteach from the 2026-09-24 Class Pulse, where students mishandled initial conditions F(0) and F(1).

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

---

## 0:47 Find the bug (8 min)

Show each, ask "what's wrong, and what's the smallest input that shows it?"

**Bug 1: missing base case.** The opening hook. Smallest input: any, e.g. `S(0)` already continues to `S(-1)`. Fix: add `if n == 0: return 0`.

**Bug 2: the reduction goes the wrong way** (this is the activity's T):
`T(0) = 1`, `T(n) = T(n + 1)` for `n > 0`.
A base case exists, but it is never reached from `n = 1`: T(1) = T(2) = T(3) = ... The input grows away from 0. Smallest exposing input: **n = 1**. Note `T(0) = 1` "works", the trap of "it worked once." (Code: `bad_T(1)` hits its depth guard; `bad_T(0)` returns 1.)

**Bug 3: an inductive step that assumes the result.** Show this "proof" of P(n): S(n) = n(n+1)/2:

> *Base case:* n = 0 works.
> *Step:* assume S(n) = n(n+1)/2. Then S(n) = n(n+1)/2. ∎

Ask: "What did the step prove?" Nothing: it restated the hypothesis for the *same* n. The bridge never reached n+1. Compare with the real step above, where we assumed P(k) and derived P(k+1) using the definition `S(k+1) = (k+1) + S(k)`. Circular leap = hypothesis and conclusion are about the same case.

---

## 0:55 Students try: the Tuesday activity (13 min)

Source: `week-08/student/tuesday-activity.md`. Individual work, they write Sources / Rules-Assumptions / Work / Check / One-Sentence Summary.

Answer key for you:

1. **S(4)** = 4 + S(3) = 4 + 3 + S(2) = 4 + 3 + 2 + S(1) = 4 + 3 + 2 + 1 + S(0) = **10**. Base: S(0) = 0. Reducing rule: n → n−1.
2. **T:** from n = 1 the input goes 1, 2, 3, ... away from 0, so the base case is never reached. Smallest exposing input: n = 1.
3. **Claim S(n) = n(n+1)/2:** base check S(0) = 0 = 0·1/2. Bridge: assume it for k, then show S(k+1) = (k+1) + S(k) = (k+1) + k(k+1)/2 = (k+1)(k+2)/2. Not acceptable: "assume it works" or "assume it for n+1."

Circulate. Likely stuck points: students trace S(4) but never name the base case; students say T "loops forever" without saying *why* (input moves away from 0).

---

## 1:08 Check for understanding (5 min)

One question on a card or the board, 2 minutes silent, then cold-call:

> "A classmate defines `G(0) = 5`, `G(1) = 5`, `G(n) = G(n-1) + G(n-2)`. Does it terminate? Is it the Fibonacci sequence? What one thing would you check first?"

Good answers: it terminates (both base cases present, reduction reaches them); it is *not* Fibonacci (different base values, so it produces 5, 5, 10, 15, 25, ...); check the base cases first. This lands the point that termination and correctness are separate questions.

---

## 1:13 AI check (2 min)

AI commonly gives recursion with no base case, an inductive step that assumes the thing to be proved, or a trace that looks plausible and never terminates. Three checks: **smallest input, the reduction step, one nontrivial trace.** For Fibonacci add: **did it state both F(0) and F(1), and with the right values?**

Then point at the Decision Gate (`week-08/student/decision-gate.md`, ordinary Week 8 gate, not a second Show & Tell report) and Thursday's Show & Tell.

---

## Three likely student questions

**1. "Isn't the recursive definition already a proof that S(n) = n(n+1)/2? It gives the right answers."**
No. The definition tells you how to compute each value. Seeing it match for n = 0..29 is evidence for those cases. Induction is the argument that the match continues for *every* n, by showing the step carries truth from k to k+1.

**2. "Why do we get to assume P(k) in the inductive step? Isn't that assuming what we're proving?"**
We assume it for one particular k, not for the case we are trying to reach. The proof's job is the implication "P(k) ⇒ P(k+1)." Combined with the base case, that chain reaches every n: P(0) gives P(1), gives P(2), and so on. It would be circular only if we assumed P(k+1) to prove P(k+1).

**3. "Why does Fibonacci need two base cases but the sum only one?"**
Look at how far back the rule reaches. S(n) uses only S(n−1), so one starting value suffices. F(n) uses F(n−1) *and* F(n−2); F(2) needs both F(1) and F(0). With only one base case the second branch of the call walks off into negative inputs (or, if you patch it with the wrong value, you get a clean-looking wrong answer).

---

## Run record (what actually ran)

Python 3.12.3, pytest 9.0.3: `python3 -m pytest -v` in `week-08/teaching/` → 13 passed (receipt has the full output). The hand traces and induction proofs above were written by hand and spot-checked by the tests only where noted (sum identity and F(n) < 2^n for small n, evidence not proof).
