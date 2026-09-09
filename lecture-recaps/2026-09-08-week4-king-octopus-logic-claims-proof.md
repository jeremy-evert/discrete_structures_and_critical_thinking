# Week 4 recap — Logic, Claims & Proof (King Octopus)

Sept. 8, 2026. Monday was Labor Day, so this was the week's first meeting.
If you missed the room, here's what we did and — more important — the method.

## The puzzle

**King Octopus and His Servants** (from Puzzle Prime). Servants have 6, 7, or
8 legs. Servants with **7 legs always lie**; servants with **6 or 8 legs
always tell the truth**. Four servants speak:

- "We together have 28 legs."
- "We together have 27 legs."
- "We together have 26 legs."
- "We together have 25 legs."

Which servant(s) told the truth?

The answer isn't the point. Working it four different ways is the point.

## Four ways to reason about the same claim

**1. Informally, by hand.**
The four claims are all different, so at most one can be true, so at least
three servants are lying, so at least three have 7 legs. That's 21 legs
already; the last servant has 6 or 8, giving 27 or 29. Only 27 is on the
list. So the legs are (7, 6, 7, 7) and **the servant who said "27" told the
truth**.

*Parity shortcut:* even + even is even; adding a 7 flips even/odd. "25" and
"27" are odd totals and can't be right; only "26" and "28" could be true.
Combined with "at most one true," you land on 27 again.

**2. Build a precise model.**
Translate the English into exact statements. "We together have 28 legs"
means the total is *exactly* 28 — not about 28, not at least 28. Make the
group "we" refers to explicit (all four). State the rule as: a 7-legged
servant's statement is false; a 6- or 8-legged servant's statement is true.

**3. Write the proof with logical bounds.**
- *At least one* servant tells the truth: if all four lied, then the "28"
  claim would actually be true — contradiction.
- *At most one* servant tells the truth: the four claims are distinct
  numbers, so they can't both be exact totals.
- Therefore *exactly one*. Find the witness (legs (7,6,7,7), total 27) and
  check it with a truth table: F, T, F, F. No counterexample is needed here
  because the claim is true and we produced a witness.

**4. Brute force.**
Each servant is 6, 7, or 8 — three options — and there are four servants, so
3 × 3 × 3 × 3 = **3⁴ = 81** possible assignments. Check every one; exactly
one satisfies all the rules. A program like this proves a fact **about the
model you gave it** — nothing more. If your model is wrong, the program is
confidently wrong with you.

## Habits we practiced (these carry past this puzzle)

- **Change one thing, then rebuild and check.** One added LaTeX package is
  enough to break a document. Don't stack five changes and then debug.
- **Names are reasoning.** A file called `..._version_2.py` tells you
  nothing. Give it a name that says what it *is*; let source control track
  versions.
- **Source vs. output.** We track the `.tex` (the recipe), not the `.pdf`
  (the cake — you can always re-bake it). That's why `git status` only
  showed the PDF changing, and that's correct.
- **Use the AI for the boring layer, not the thinking.** Let it grind
  through syntax and compiler messages. Keep your own brain on the real
  questions and on what a classmate just said.
- **An AI can be confidently wrong.** It happened twice on screen. When it
  says a build "worked cleanly" or that something is "definitely" true —
  verify against the definition or find a counterexample. Anyone can make a
  bad argument sound good; that's old. The AI just does it faster.

## Thursday (Sept. 10) — Show & Tell

Bring **your own** logic puzzle (a river-crossing one, say) and run it
through the same five headings. Re-explaining King Octopus won't be enough —
expect questions until something interesting shows up.
