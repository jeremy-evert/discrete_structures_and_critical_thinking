# Farkle Evidence Lab — Which Claim Survives the Dice?

## Big question

> **When a Farkle strategy appears better, what are we actually justified in believing?**

This lab is about evidence, not about crowning a champion.

You will compare two fixed strategies using the same shared Farkle machine, inspect more than one sample, and decide whether your original claim deserves to survive.

Keep your Reasoning Odyssey receipt open while you work:

`assignments/week-16-farkle-evidence-receipt.md`

---

# Part 1 — Know what is fixed

Before running anything, identify these facts from the instructor/shared materials:

- classroom target score;
- legal strategy actions;
- which strategy is A;
- which strategy is B;
- number of games;
- how starting position is handled;
- seed or seed-bundle name.

Write them in **Rules / Assumptions**.

If you cannot tell what was held constant, you are not ready to interpret the comparison.

---

# Part 2 — Define `better` before you see the answer

Choose one primary comparison rule.

Examples:

- higher win rate by at least **2 percentage points**;
- higher win rate in **every tested seed sample**;
- higher average score if win rates are within **1 percentage point**;
- prefer the simpler strategy unless the more complex one clears a stated win-rate improvement.

You may choose a different reasonable rule.

Write it down **before** the bundle evidence.

Then make a prediction:

> I predict ______ will be better under my rule because ______.

Your prediction is allowed to be wrong. An invisible prediction teaches you almost nothing.

---

# Part 3 — Run one initial sample

A default comparison is available:

```text
python lessons/week-16-farkle-evidence.py initial
```

Your instructor may give you another approved strategy pair.

You can also inspect available runner options with:

```text
python lessons/week-16-farkle-evidence.py --help
```

For the initial sample, record at least:

| Evidence | Value |
|---|---:|
| Games | |
| Starts A | |
| Starts B | |
| Wins A | |
| Wins B | |
| Ties | |
| Win rate A | |
| Win rate B | |
| A - B difference (percentage points) | |

Then answer:

1. Which strategy appears better **in this sample** under your rule?
2. What is one reason this first result could mislead you?

Possible traps include:

- one random sample;
- tiny difference;
- wrong denominator;
- starter imbalance;
- choosing the metric after seeing which one makes your favorite strategy win;
- assuming the learner sees information it actually ignores.

---

# Part 4 — Try to break your first conclusion

Run the repeated evidence bundle:

```text
python lessons/week-16-farkle-evidence.py bundle
```

The runner uses the same strategy comparison across a named set of deterministic seeds and saves the raw rows.

Do **not** throw away the individual rows and keep only the average.

Complete or attach a table with at least:

| Seed | Games | Starts A | Starts B | Wins A | Wins B | Ties | Win A | Win B | A-B pp |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | |

Now inspect the bundle:

- Did A-B have the same sign in every row?
- What was the smallest A-B difference?
- What was the largest?
- What was the range?
- Did one sample look dramatically different from the others?
- Does the bundle satisfy the rule you wrote **before** seeing it?

---

# Part 5 — Change the question once

A strategy can be `better` under one ordering and worse under another.

Choose **one** alternate view already present in the shared receipt, such as:

- average score;
- Farkle rate per own turn;
- preparation/training effort;
- evaluation speed;
- simplicity/complexity note.

Ask:

> If I ranked the strategies by this measure instead, would my decision change?

You do not need to optimize every metric. The point is to notice that `best` needs a criterion.

---

# Part 6 — Name what the model does not know

Inspect the strategy description and shared state contract.

Name at least one limitation.

Examples:

- the transparent learner may not use total score or opponent score in its learned state key;
- training on solo turns is not the same as learning whole-game strategy;
- the classroom Farkle rules omit other house-rule choices;
- a finite number of simulated games cannot prove universal optimality;
- performance against one opponent does not define performance against every possible opponent.

Finish this sentence:

> Even if I ran many more games, this experiment still would not establish ______ because ______.

---

# Part 7 — Audit a confident explanation

Your instructor will provide either:

- a live AI-generated interpretation, or
- a prepared example if live AI access is not appropriate.

Audit it as another argument.

Mark any statement that:

- overstates the sample;
- hides a denominator;
- ignores seed-to-seed variation;
- ignores starter balance;
- calls a tiny difference meaningful without a criterion;
- says `best` without defining the order;
- ignores a model limitation;
- uses confident language where the evidence is conditional.

Then write **one repaired sentence** that says what the evidence actually supports.

---

# Part 8 — Defend, revise, or refuse

Return to your original prediction and decision rule.

Choose one final move:

## Defend

Your original limited claim survived the checks.

## Revise

The evidence supports a narrower/different claim than the one you started with.

## Refuse

The evidence does not justify declaring a winner under your stated rule.

All three can earn full credit when the reasoning trail supports them.

Your final **One-Sentence Summary** should include the scope of the conclusion.

Good shape:

> Under ______ rules, against ______, across ______ evidence, I would ______ because ______, while this experiment still cannot establish ______.

The dice do not owe you a clean winner. Your reasoning owes the reader an honest claim.
