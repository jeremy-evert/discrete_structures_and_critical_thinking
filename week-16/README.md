# Week 16 — Farkle, Machine Learning, and What the Evidence Lets You Say

**Tuesday, December 1 and Thursday, December 3, 2026**

## This week's question

> **When a Farkle strategy appears better, what are we actually justified in believing?**

You have spent the semester learning how to make reasoning visible: state the claim, expose assumptions, do the work, check it, and write a conclusion that says no more than the evidence earns.

This week gives that whole habit a noisy playground.

Farkle has randomness. Machine-learning and simulation strategies produce tempting numbers. A polished result can make `53% beats 47%` feel like the end of the conversation.

It is usually the beginning.

## What you are *not* doing

You are not:

- writing a Farkle game from scratch;
- implementing a new machine-learning algorithm;
- learning a new statistics course in two meetings;
- hunting for one magic `best strategy`;
- building a giant program;
- needing a GPU, cloud account, or paid AI tool.

The shared Farkle package does the computational heavy lifting. Your job is to decide what its evidence means.

## Tuesday — Make a claim, then try to break it

You will:

1. inspect the fixed rules and comparison setup;
2. define what **better** means for your comparison;
3. choose a decision rule before the numbers start sweet-talking you;
4. predict what will happen;
5. run or inspect one bounded experiment;
6. look at raw counts and denominators, not only percentages;
7. identify one reason the result might mislead you;
8. write a one-sentence limited conclusion.

A good Tuesday conclusion might sound like:

> In this sample, under these rules, A had the higher observed win rate, but I am not yet willing to claim A is generally better because ______.

## Thursday — Defend, revise, or refuse

You will inspect several deterministic samples of the **same comparison**.

Then you will ask:

- Did the ordering stay the same?
- How much did the measured difference move?
- Would another reasonable metric change the story?
- Does the difference clear the decision threshold you declared?
- What does the model fail to represent?
- What claim would be too broad even after all of these games?

Your final move can be any of these if the evidence supports it:

- **Defend** the original limited claim.
- **Revise** it into a narrower claim.
- **Refuse** to declare a winner under your decision rule.

Refusing is not failure. Pretending the evidence is stronger than it is would be.

## Your Reasoning Odyssey evidence

Use:

`assignments/week-16-farkle-evidence-receipt.md`

It follows the method you already know:

1. **Sources**
2. **Rules / Assumptions**
3. **Work**
4. **Check Your Answer**
5. **One-Sentence Summary**

## AI this week

Our standing rule still applies:

> **Love AI more. Trust AI less.**

You may be given an AI-generated interpretation of the same Farkle results.

Do not grade it by whether it sounds intelligent.

Audit it:

- What claim did it make?
- Did it use the right denominator?
- Did it treat one sample as proof?
- Did it confuse `different` with `meaningfully different`?
- Did it ignore the model's limits?
- Did it say `best` without telling you the ordering criterion?

AI output is another claim to check. It is not the evidence.

## Technical path

Your instructor will provide the shared package through the course repository before this week is released.

The course-facing runner is:

```text
python lessons/week-16-farkle-evidence.py initial
python lessons/week-16-farkle-evidence.py bundle
```

If live execution fails, the instructor will provide a validated evidence fixture generated from the same shared package/benchmark. You will still do the reasoning task.

## The finish line

By the end of Thursday, you should be able to say:

> **Here is exactly what I claimed, here are the assumptions and denominators, here is how the result moved across samples, here is what the model cannot establish, and here is the decision I am willing to defend.**

That is the point of the week.
