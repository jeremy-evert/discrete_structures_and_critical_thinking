# Week 16 Thursday: Defend, Revise, or Refuse

## The Thursday job

Reopen Tuesday's prediction and decision rule before reading the bundle. You will inspect the same comparison across three named **deterministic** seed samples (a deterministic sample repeats when its seed and inputs are held fixed), test whether your rule survives, audit a confident interpretation, and make one final move: **defend**, **revise**, or **refuse**.

This is an evidence check, not a contest to crown a strategy. A **threshold** is the minimum difference your decision rule requires before it declares a result. Use the threshold you declared in the receipt; do not choose a new one because a row looks favorable. If a term is unfamiliar, use the [Week 16 glossary](glossary.md).

## 1. Retrieve your prediction

Before looking at the table, write down:

- what you predicted on Tuesday;
- what “better” means in your decision rule;
- the threshold or other test you said you would use;
- the claim you were prepared to make after the initial sample.

Checkable answer: another reader should be able to tell exactly what would make you declare A, declare B, or refuse.

## 2. Inspect the same comparison

The fallback evidence is a synthetic bundle (made for classroom practice, not from student data) checked against the same classroom comparison:

- Strategy A is `learner:500`; Strategy B is `bank_at_425`.
- The target score is 4000, with the classroom rules and opponent setup held fixed.
- Each row has 10 games and balanced starts: 5 for A and 5 for B.
- The seed labels are 17, 6262, and 2026. A seed makes a repeatable sample; it does not make the result universal.

| Seed | Games | Starts A | Starts B | Wins A | Wins B | Ties | Win A | Win B | A − B pp |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 10 | 5 | 5 | 3 | 7 | 0 | 30% | 70% | −40 |
| 6262 | 10 | 5 | 5 | 6 | 4 | 0 | 60% | 40% | +20 |
| 2026 | 10 | 5 | 5 | 8 | 2 | 0 | 80% | 20% | +60 |

The **denominator** for each win rate is the 10 games in its row. The A−B value is the win rate for A minus the win rate for B, measured in **percentage points**. Rebuild at least one row from its raw wins and games.

Answer these questions in your Work section:

1. Did the ordering stay the same? In other words, did the same strategy have the higher win rate in every row?
2. What were the minimum and maximum A−B differences?
3. What was the range, meaning maximum minus minimum?
4. Does the bundle clear **your** declared threshold or satisfy your decision rule?

The fallback numbers are deliberately mixed evidence: the A−B differences are −40, +20, and +60, with a 100-percentage-point range. They do not declare a winner. Your task is to explain what that movement permits you to say and what it does not.

## 3. Ask whether another metric changes the story

A **metric** is a measurement used for a judgment. Pick one alternate metric already named in the receipt: average score, Farkle rate per own turn, preparation effort, evaluation speed, or simplicity.

Write:

> If I ordered the strategies by __________ instead of win rate, my decision would / would not change because __________.

Do not silently replace your original criterion. Say whether the alternate view changes what you would prioritize, and keep the denominator visible when the metric has one.

## 4. Name what the model does not represent

A **model** is a simplified representation of a situation. Name at least one thing this experiment does not represent. For example, the learner may not use every score or opponent detail; the training setup is not every possible whole-game strategy; the classroom rules are not every house rule; and these finite samples do not test every opponent or future game.

Complete this sentence:

> Even if I ran many more games, this experiment still would not establish __________ because __________.

Then write one claim that would still be too broad, such as “A is the universally best Farkle strategy” or “machine learning always beats a hand-written rule.” Explain which missing condition or model limitation makes that claim too broad.

## 5. Critique a confident interpretation

An AI-interpretation audit checks an explanation as another claim, not as evidence. This week's AI failure mode is a polished explanation that hides the denominator or ordering criterion, treats one sample as proof, or ignores seed-to-seed variation and model limits.

Audit this example:

> “The learner is clearly the best strategy because it won the most games in the simulation. The result proves that machine learning beats the hand-written rule.”

Mark at least two problems:

- What games and denominator were counted?
- Does “best” name an ordering criterion and threshold?
- Does one sample become a universal claim?
- Does the explanation notice that the bundle changes ordering?
- What does the model fail to represent?

Exchange your critique with a classmate. Your classmate should ask one question intended to break your claim, such as “What would happen if the −40 row were not ignored?” or “What exactly does your threshold require?” Record the question and your answer in **Check Your Answer**.

Write one repaired sentence that is no broader than the evidence. Do not declare a winner just because the repaired sentence sounds confident.

## 6. Make the final move

Return to the prediction and rule you wrote before the repeated evidence:

- **Defend** the original limited claim if the checks support it under your stated rule.
- **Revise** the claim into a narrower or different claim if the evidence changed what you can responsibly say.
- **Refuse** to declare a winner if the evidence does not satisfy your rule. Refusal is a precise result, not a failure.

## What to submit

Complete the existing `assignments/week-16-farkle-evidence-receipt.md`. It has these five headings, which must remain verbatim:

1. **Sources**
2. **Rules / Assumptions**
3. **Work**
4. **Check Your Answer**
5. **One-Sentence Summary**

This receipt is its own **5% Farkle + ML Synthesis** category, not an ordinary Decision Gate. There is no separate Week 16 `student/decision-gate.md`; do not create or submit a new gate. The receipt is a **graded discussion** where peers see each other's work as a class learning resource. Do not include private information. Your classmates should be able to inspect your sources, assumptions, calculations, critique exchange, limitation, and final move.

Before submitting, check that you:

- predicted before inspecting the repeated rows;
- showed raw counts and denominators;
- reported ordering, minimum, maximum, and range;
- tested your own threshold or decision rule;
- considered one alternate metric;
- named a model limitation and repaired the AI interpretation;
- chose defend, revise, or refuse without claiming more than the evidence supports.
