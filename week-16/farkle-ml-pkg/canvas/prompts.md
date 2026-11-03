# Prompt 01 — Claim and rule

```prompt-a
Sources:
- Use the fixed rules, strategy labels, and comparison setup shown in the slide.
- Do not invent a new game, opponent, metric, or data source.

Rules / Assumptions:
- State what stays fixed and define what "better" means for this comparison.
- Write a decision rule that can return "declare A," "declare B," or "refuse."

Work:
- Write one precise claim you are testing.
- Write the rule you will use before you inspect the repeated seed bundle.
- Make one prediction and give one reason for it.

Check:
- Could another reader apply your rule without guessing what "better" means?
- Does your rule name the metric, denominator, and scope?

One-Sentence Summary:
- Finish: "Under these rules, I will call ___ better only if ___; otherwise I will ___."

Do not write a Farkle engine, simulation, or machine-learning algorithm. Make the reasoning trail visible instead.
```
# Prompt 02 — Initial sample audit

```prompt-a
Sources:
- Use the initial evidence row shown on the slide and the fixed course setup.

Rules / Assumptions:
- Name the seed, game count, balanced starts, strategy labels, and target/rules.
- Define the denominator for each win rate.

Work:
- Copy the raw wins, starts, games, ties, and both win rates.
- State what appears better in this one sample under your predeclared rule.
- Name one specific reason this result could mislead you.

Check:
- Rebuild each rate from its numerator and denominator.
- Separate "observed in this sample" from "generally better."

One-Sentence Summary:
- Write one sentence that reports the bounded observation without declaring a universal winner.

Do not write code or design a Farkle engine. Audit the evidence and its interpretation.
```
# Prompt 03 — Bundle stability check

```prompt-a
Sources:
- Use the three deterministic seed rows shown in the Thursday-preview table.

Rules / Assumptions:
- Confirm that the strategies, target, game count, classroom rules, and start balance stay fixed.
- Reuse the decision rule you wrote before seeing the bundle.

Work:
- Record each row's raw wins, denominators, win rates, and A-minus-B difference.
- Check whether the ordering has the same sign in every row.
- Find the smallest difference, largest difference, and range.

Check:
- Does the bundle satisfy your predeclared rule?
- What can the bundle support, and what would still be an overclaim?

One-Sentence Summary:
- Defend, revise, or refuse the winner claim in one evidence-bounded sentence.

Do not write a simulator or machine-learning algorithm. Compare and interpret the supplied evidence.
```
# Prompt 04 — Repair an overclaim

```prompt-a
Sources:
- Audit the confident reader/AI statement on the slide against the displayed rows and the fixed course setup.

Rules / Assumptions:
- Treat "best" as undefined until an ordering criterion is named.
- Treat a finite simulation as evidence about this model, not proof about every possible Farkle game.

Work:
- Mark the hidden denominator, missing ordering criterion, unsupported leap from one sample to a universal claim, and ignored model limitation.
- Rewrite the statement so it says only what the evidence earns.
- Name one additional check that would be useful without turning this into a programming project.

Check:
- Does the repaired sentence include scope, rules, denominator or raw counts, and a limitation?
- Does it avoid calling a strategy "best" without a decision rule?

One-Sentence Summary:
- Finish: "The evidence supports ___ under ___, but it cannot establish ___ because ___."

Do not write a Farkle engine, simulation, or machine-learning algorithm. Repair the claim, not the software.
```
