# Week 16 Thursday: Defend, Revise, or Refuse

## The Thursday job

Reopen Tuesday's prediction and decision rule before reading the **bundle**, a named group of seed samples. You will inspect the same comparison across three named **deterministic** seed samples (a deterministic sample repeats when its seed and inputs are held fixed), test whether your rule survives, and **audit** (inspect a claim for evidence, assumptions, calculations, and limitations) a confident interpretation. Your final move is **defend** (keep a limited claim), **revise** (replace it with a narrower claim), or **refuse** (decline to declare a winner). If a term is unfamiliar, use the [Week 16 glossary](glossary.md).

This is an evidence check, not a contest to crown a strategy. A **threshold** is the minimum number or amount your decision rule requires before it declares a result; the rule and threshold belong together. Do not choose a new threshold because a row looks favorable.

## 1. Retrieve your prediction

Before looking at the table, write down:

- what you predicted on Tuesday;
- what “better” means in your decision rule;
- the numeric threshold or other test you said you would use;
- the claim you were prepared to make after the initial sample.

If your Tuesday rule was not written down or was not a checkable test (for example, no stated number or condition), write one now, mark it **LATE**, and say that it was written after seeing the data. Do not silently present a late rule as if it had been predeclared.

Checkable answer: another reader should be able to tell exactly what would make you declare A, declare B, or refuse.

## 2. Inspect the same comparison

The numbers you will read are practice numbers from a fallback fixture (a ready-made set of results used when live running is not available), produced by the shared course Farkle package; they are not live student results.

- Strategy A is `learner:500`. A learner is a strategy that uses training experience to choose an action. Here the transparent table trains on 500 turns, sorts each situation into a group by how many turn points it has so far and how many dice it can still roll, and chooses roll or bank from learned average outcomes; `500` means 500 training turns, not 500 games.
- Strategy B is `bank_at_425`. Banking means adding current turn points to the total and ending the turn; this strategy banks at 425 points or more and rolls again below 425.
- The target score is 4000, with the classroom rules and opponent setup held fixed. A **start** records which player takes the first turn.
- Each row has 10 games and balanced starts: 5 for A and 5 for B.
- The seed labels are 17, 6262, and 2026. A seed makes a **pseudo-random** sample repeatable; it does not make the result universal.

| Seed | Games | Starts A | Starts B | Wins A | Wins B | Ties | Win A | Win B | A − B pp |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 10 | 5 | 5 | 3 | 7 | 0 | 30% | 70% | −40 |
| 6262 | 10 | 5 | 5 | 6 | 4 | 0 | 60% | 40% | +20 |
| 2026 | 10 | 5 | 5 | 8 | 2 | 0 | 80% | 20% | +60 |

The **denominator** for each win rate is the 10 games in its row. The A−B value is the win rate for A minus the win rate for B, measured in **percentage points**; **pp** is the short label for percentage points. A **tie** is a game neither strategy wins.

Rebuilding a row means recomputing the displayed rate from its raw count and denominator: 3/10 = 0.30 = 30%. For seed 17, A's 3 wins out of 10 games rebuild to 30%.

Answer these questions in your Work section:

1. Did the ordering stay the same? In other words, did the same strategy have the higher win rate in every row?
2. What were the most negative and most positive A−B differences?
3. What was the range, meaning maximum minus minimum?
4. Does the bundle clear **your** declared threshold or satisfy your decision rule?

After you apply your own rule, for many rules this will lead to refuse; check yours. Explain what the movement permits you to say and what it does not.

## 3. Ask whether another metric changes the story

A **metric** is a measurement used for a judgment. No extra numbers are supplied for this step; reason in words: would ordering by **points per game** plausibly change your decision, and why? Points per game means the average points scored in one complete game. You may instead use **Farkle rate per own turn**, meaning Farkles divided by the number of turns taken by that strategy; an own turn is one opportunity for that strategy's player to roll or bank. Preparation effort means work or time before evaluation, evaluation speed means time per game, and simplicity means how few rules or components a strategy requires.

Write:

> If I ordered by __________ instead of win rate, my decision would / would not change because __________.

Model filled sentence: “If I ordered by Farkle rate per own turn instead of win rate, my decision might change because I might prioritize fewer Farkles; no extra numbers are supplied, so this is a reasoned possibility, not a measured result.”

Do not silently replace your original criterion. Say whether the alternate view changes what you would prioritize, and keep the denominator visible when the metric has one.

## 4. Name what the model does not represent

A **model** is a simplified representation of a situation. Name at least one thing this experiment does not represent. For example, the learner may not use every score or opponent detail; the training setup is not every possible whole-game strategy; the classroom rules are not every house rule; and these **finite** samples do not test every opponent or future game.

Complete this sentence:

> Even if I ran many more games, this experiment still would not establish __________ because __________.

Model filled sentence: “Even if I ran many more games, this experiment still would not establish that A is the universally best Farkle strategy because the model tests only these strategies, rules, opponent setup, and training process.”

Then write one claim that would still be too broad, such as “A is the universally best Farkle strategy” or “machine learning always beats a hand-written rule.” Explain which missing condition or model limitation makes that claim too broad.

## 5. Critique a confident interpretation

An AI-interpretation **audit** checks an explanation as another claim, not as evidence. This week's AI failure mode is a polished explanation that hides the denominator or ordering criterion, treats one sample as proof, or ignores seed-to-seed variation and model limits.

Audit this example:

> “The learner is clearly the best strategy because it won the most games in the simulation. The result proves that machine learning beats the hand-written rule.”

Quote the words and label each problem:

- What games and denominator were counted?
- Does “best” name an ordering criterion and threshold?
- Does one sample become a universal claim?
- Does the explanation notice that the bundle changes ordering?
- What does the model fail to represent?

Exchange your critique by replying in the Week 16 graded discussion thread, or in class with a partner; if you have no partner, critique the AI-audit example sentence instead. Your classmate should ask one question intended to break your claim, such as “What if you had paid attention to the −40 row?” or “What exactly does your threshold require?” Record the question and your answer in **Check Your Answer**.

Write one repaired sentence that is no broader than the evidence. Do not declare a winner just because the repaired sentence sounds confident.

## 6. Make the final move

Return to the prediction and rule you wrote before the repeated evidence:

- **Defend** the original limited claim if the checks support it under your stated rule.
- **Revise** the claim into a narrower or different claim if the evidence changed what you can responsibly say.
- **Refuse** to declare a winner if the evidence does not satisfy your rule. Refusal is a precise result, not a failure.

## What to submit

Submit to the Week 16 Farkle Evidence Receipt assignment in this module (it has the five headings: Sources; Rules / Assumptions; Work; Check Your Answer; One-Sentence Summary). Those headings must remain verbatim.

This receipt is graded as its own 5% category; there is no other Week 16 form to submit. It is a **graded discussion** where peers see each other's work as a class learning resource. Do not include private information. Your classmates should be able to inspect your sources, assumptions, calculations, critique exchange, limitation, and final move.

Before submitting, check that you:

- predicted before inspecting the repeated rows;
- showed raw counts and denominators;
- reported ordering, most negative and most positive difference, and range;
- tested your own numeric threshold or decision rule;
- considered one alternate metric using words, since no extra numbers were supplied;
- named a model limitation and repaired the AI interpretation;
- chose defend, revise, or refuse without claiming more than the evidence supports.
