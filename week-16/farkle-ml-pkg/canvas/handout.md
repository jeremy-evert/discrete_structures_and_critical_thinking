# Week 16 Tuesday: Farkle Evidence Handout

## The job this week

Our question is: **When a Farkle strategy appears better, what are we actually justified in believing?**

This is an evidence lab, not a contest to crown a strategy. **Evidence** means information we can inspect and use to support or limit a claim. A **claim** is a sentence that says what we think is true. Your job is to make the claim no larger than the evidence.

You will not write a Farkle engine, which is a program that implements the game rules. You will not write a machine-learning algorithm, which is a step-by-step method for learning a decision rule from data. You need no special hardware, cloud account, or paid tool. The shared materials provide the game results; you provide the reasoning.

## Words before work

These definitions are the working meanings for this handout:

- **Farkle** is a dice game in which a player may bank turn points or risk them by rolling again; a Farkle loses the unbanked turn points.
- A **strategy** is a fixed rule for choosing an action from the information the strategy can see.
- A **model** is a simplified representation of a real situation. Here it represents the game, the strategies, and the comparison rules.
- A **simulation** is repeatedly running a model to observe outcomes under stated rules.
- A **sample** is the particular games observed in one run.
- A **seed** is a label that makes one pseudo-random sequence repeatable. Repeatable does not mean universal.
- A **win rate** is wins divided by the games counted for that strategy.
- The **numerator** is the top number in a division; for a win rate, it is the number of wins.
- The **denominator** is the bottom number in a division; for a win rate here, it is the number of games counted.
- A **percentage point** is a direct difference between two percentages: 70% minus 30% is 40 percentage points.
- A **decision rule** is a test declared before looking at the repeated evidence that says when to declare A, declare B, or refuse.
- A **criterion** is the stated feature used to judge or order choices. A **metric** is a measurement used for that judgment.
- The **scope** of a statement is the exact conditions and cases to which it applies.
- An **assumption** is something treated as fixed or true for the comparison.
- An **outcome** is what happened in one game, such as A win, B win, or tie.
- **Balanced starts** means each strategy starts the same number of games in the first position and the second position. This addresses one fairness concern.
- **Variation** is the way results can change from one sample or seed to another.
- **Machine learning** is a way of producing a rule from examples or experience; it does not make a finite result universal.
- An **overclaim** is a statement stronger or broader than its evidence supports.
- A **model limitation** is a reason the model cannot answer some larger question.

## Why before how: a race analogy

Before a race, people need to agree whether “better” means first to the finish line, fastest average lap, or least fuel used. A stopwatch cannot choose that goal for them. In the same way, a Farkle result cannot choose the criterion for us after the numbers arrive. Decide what “better” means first; then inspect the evidence.

## The predict-then-check loop

Use this loop for each move:

1. **Predict:** write what you expect before seeing the next result.
2. **Check:** inspect the supplied counts and rebuild the rates.
3. **Explain:** say what the check supports and what it does not support.

A prediction may be wrong. That is useful because a visible prediction can be checked; an invisible prediction cannot.

## Fixed comparison

Use the comparison shown in the Tuesday slides and supplied evidence:

- **Target score** is the score needed to end the game; here it is 4000.
- Strategy A: `learner:500`.
- Strategy B: `bank_at_425`.
- Ten games per seed, with five starts for A and five starts for B.
- The same classroom Farkle rules and **opponent setup**, meaning the player or strategy being played against, are used for each row.

The first row uses seed 17. The three rows together are a **seed bundle**, meaning a named group of seed samples used for one repeated check. Before reading it, write your decision rule and prediction:

> I will call ______ better only if ______________________________________.

> I predict ______ will have more observed wins because ____________________.

## Worked evidence: keep counts and denominators visible

The table contains observations from the same fixed comparison. A row’s win rate is wins divided by 10 games. The A-minus-B column is the difference in percentage points. Do not turn these rows into a universal ranking.

| Seed | Games | Starts A | Starts B | Wins A | Wins B | Ties | Win A | Win B | A − B pp |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 10 | 5 | 5 | 3 | 7 | 0 | 30% | 70% | -40 |
| 6262 | 10 | 5 | 5 | 6 | 4 | 0 | 60% | 40% | 20 |
| 2026 | 10 | 5 | 5 | 8 | 2 | 0 | 80% | 20% | 60 |

Check the arithmetic:

- Seed 17: A is 3/10 and B is 7/10, so the displayed rates are 30% and 70%.
- Seed 6262: A is 6/10 and B is 4/10, so the displayed rates are 60% and 40%.
- Seed 2026: A is 8/10 and B is 2/10, so the displayed rates are 80% and 20%.

The observed ordering changes across these rows. That fact is not a declaration of a winner; it is a reason to limit the claim and inspect the rule you wrote before the bundle.

## Fill the evidence receipt

An **evidence receipt** is a form that records the reasoning trail. Use the existing `assignments/week-16-farkle-evidence-receipt.md` as your submission form. Keep its five headings exactly:

### Sources

Name the shared Farkle package or supplied evidence file, the course material, and any AI (artificial-intelligence tool) help. If AI helped, describe what you checked.

### Rules / Assumptions

Record the target, strategy labels, game count, balanced starts, seeds, fixed rules, and your definition of “better.” State each denominator.

### Work

Write your prediction before repeated evidence. Copy raw wins, ties, starts, games, rates, and A-minus-B percentage points. Find the minimum, maximum, and range of the A-minus-B differences. The **range** is the maximum minus the minimum.

Inspect one alternate metric, such as **average score**, meaning mean points per game; **Farkle rate per own turn**, meaning Farkles divided by own turns; **preparation effort**, meaning work done before evaluation; **evaluation speed**, meaning time per game; or **simplicity**, meaning how few rules or components a strategy requires. State whether that changes what you would prioritize; do not pretend a new metric answers the old question automatically.

### Check Your Answer

Name one way the first sample could mislead you. Audit whether a confident reader or AI hides the denominator or ordering criterion, treats one sample as proof, calls a small difference meaningful without a rule, or ignores a model limitation. Write one repaired sentence.

### One-Sentence Summary

Choose **defend**, **revise**, or **refuse** under your stated rule. Your sentence must include the scope of the observation and one limitation. Refusing to declare a winner can be the precise result when the rule is not satisfied.

## The week's AI failure mode

A confident reader or AI can hide the denominator or the ordering criterion; one sample can be treated as proof. That is an **AI failure mode**, meaning a predictable way an AI-generated or polished explanation can mislead. Audit the argument instead of grading its confidence. Ask: What was counted? What was the denominator? What does “better” mean? Did the ordering stay the same? What can this model not establish?

## What to submit and who can see it

Submit the completed Week 16 evidence receipt as the **graded discussion artifact**, meaning the assessed discussion work shared with classmates. The completed receipt is **peer-visible**, meaning classmates will see each other’s work, so the receipts become a class learning resource. Do not include private information. Your peers should be able to inspect the sources, rules, work, checks, and limited summary.

## Final check

Before submitting, verify:

- I predicted before checking the repeated evidence.
- I showed raw counts and denominators, not only percentages.
- I kept the five receipt headings: Sources; Rules / Assumptions; Work; Check Your Answer; One-Sentence Summary.
- I named a model limitation.
- I did not call one strategy universally best.
- I stated whether I defend, revise, or refuse under my declared rule.
