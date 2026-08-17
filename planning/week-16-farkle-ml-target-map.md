# DSCT Week 16 — Farkle + Machine Learning target map

**Dates:** Tuesday Dec. 1 and Thursday Dec. 3, 2026  
**Status:** AUTHORING TARGET  
**Central question:** **When a Farkle strategy appears better, what are we actually justified in believing?**

## Purpose

Week 16 is not a thirteenth formal DSCT topic.

It is where the semester's reasoning tools are allowed to meet one playful computational problem and disagree productively about what the evidence means.

The shared Farkle repository supplies the machine.

DSCT supplies the questions:

- What exactly is the claim?
- What assumptions make the comparison fair?
- What does the sample show?
- How stable is the observation?
- Is the difference large enough to matter for the decision?
- What does the model still leave out?
- What conclusion should we defend, revise, or refuse?

---

# Semester synthesis map

| Prior DSCT idea | Farkle Week 16 use | Student-visible? |
|---|---|---|
| Logic / claims | Define `A is better than B` precisely. Better by win rate, expected score, simplicity, cost, or another criterion? | **Required** |
| Proof / counterexample habit | Ask what result or edge case would make the broad claim fail. Simulation evidence is not universal proof. | **Required** |
| Algorithms / correctness | Audit whether the shared simulator follows fixed rules and balances starting position. | **Required, light** |
| Counting / sample spaces | Identify what counts as one game/trial and what outcomes are being counted. | **Required, light** |
| Probability / uncertainty | Distinguish random variation from a stable pattern; reason about expectation and repeated samples. | **Required** |
| Base rates / independence | Spot gambler's-fallacy language, false independence, or denominator blindness. | **Required through critique** |
| Relations / order criteria | Notice that changing the comparison criterion can change the `winner`. | **Required** |
| Trees / decision structures | Recognize a strategy as a policy over possible states/choices; deeper lookahead spends more work. | Optional connection |
| Boolean checking habit | Search for a concrete case that falsifies an overbroad AI/human claim. | **Required through audit** |
| Finite-state models | Identify what variables the learner/strategy sees. | **Required** |
| Model limits | Name something no amount of simulation under this model establishes. | **Required** |
| AI Fluency | Audit a polished interpretation against raw counts, assumptions, and limits. | **Required via AI or instructor-provided example** |

Do not force students to mention every row. The required experience concentrates on the bolded reasoning spine.

---

# Four questions that must stay separate

## 1. Was the experiment fair enough to interpret?

Students should verify or be able to find:

- same Farkle rule set;
- same target score;
- fixed strategy definitions;
- number of games;
- seed/bundle identity;
- raw starter counts;
- raw wins/ties;
- no hidden workload change.

A result from an unfair comparison can be reproducible and still be misleading.

## 2. Was the observed difference stable?

Students compare several deterministic seed samples.

They ask:

- Did the sign/order of the difference stay the same?
- How much did the measured difference move?
- Did a larger sample appear less jumpy?
- Is one seed doing most of the rhetorical work?

No rule says `more trials = truth`. More trials may reduce sampling noise while leaving model assumptions untouched.

## 3. Was the difference meaningful for the stated decision?

Students must declare a criterion.

Examples:

- choose A only if it wins by at least 2 percentage points across the tested bundle;
- choose the simpler strategy unless the more complex one clears a stated improvement threshold;
- choose the strategy with the higher expected score if the win-rate difference is practically tied;
- refuse to declare a winner if the ordering changes across samples.

The criterion is itself inspectable reasoning.

## 4. What does the model not establish?

Students name at least one limitation such as:

- this is one classroom Farkle ruleset;
- target score is fixed;
- the transparent learner sees only a reduced state;
- training on solo turns differs from learning full-game strategy;
- the chosen opponent changes what `good` means;
- finite simulation cannot prove universal optimality;
- additional real-world objectives may be absent.

---

# Tuesday map — Make the claim, then try to break it

## Opening question

> Two strategies play 100 games. A wins 53 and B wins 47. What are you allowed to say?

Do not answer it for them immediately.

## Sources

Students locate/inspect:

- shared rule contract;
- strategy descriptions;
- experiment receipt headings;
- course reasoning method.

## Rules / Assumptions

Students record at least:

- what `better` means in their claim;
- target score/rules held fixed;
- sample size;
- starter-balance assumption;
- what state each strategy is allowed to see.

## Work

Students choose or receive a bounded matchup such as:

```text
bank_at_425 vs learner:500
```

or another fixed instructor-approved pair.

They make a prediction **before** reading the evidence and inspect/run an initial bounded sample.

## Check

They must find one way the first result could fool a reader.

Good possibilities:

- one seed/sample;
- small difference;
- hidden denominator;
- starter imbalance;
- metric choice;
- strategy/model state limitation;
- overbroad causal language.

## One-Sentence Summary

Tuesday summary should sound like:

> `In this 100-game sample, under these fixed assumptions, A had the higher observed win rate, but I would not yet claim A is generally better because ____.`

Not:

> `A is the best strategy.`

---

# Thursday map — Defend, revise, or refuse

## Evidence set

Use a shared named seed bundle, preferably `classroom_v1`, or a validated shorter classroom subset when time requires it.

The evidence table should expose:

| seed | games | starts A | starts B | wins A | wins B | ties | win A | win B | A-B pp |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|

Optional columns:

- avg score A/B;
- Farkles/turns;
- preparation cost;
- evaluation time.

The DSCT lesson should not require every cost column merely because the shared package has them.

## Student reasoning

Students:

1. compare the individual seed rows;
2. inspect the range/spread of A-B win-rate difference;
3. identify whether the apparent ordering is stable;
4. consider one alternate metric or criterion;
5. state one model limitation;
6. apply their declared decision rule;
7. exchange a short critique;
8. revise or preserve the conclusion.

## Final allowed moves

The student can validly conclude:

- **defend:** evidence is strong enough for my declared limited claim;
- **revise:** the original claim was too broad, so here is a narrower one;
- **refuse:** these samples do not justify choosing a winner under my criterion.

`Refuse` is a successful reasoning outcome when supported.

---

# AI audit map

Use AI live only if access is reliable and zero-cost. Otherwise provide an instructor-generated/pregenerated response.

Prompt shape:

> Here are the Farkle experiment results. Tell me which strategy is better and why.

Students audit the response for:

- unsupported universal language;
- treating the highest percentage as automatically meaningful;
- denominator mistakes;
- ignoring seed/sample variation;
- ignoring starter balance;
- assuming causality;
- ignoring model limitations;
- using `confidence` rhetorically without evidence.

The audit target is not `catch the stupid AI`.

The target is:

> **Fluent interpretation is still a claim that must earn its evidence.**

---

# Evidence receipt map

The Farkle + Machine Learning Synthesis evidence receipt (its own 5% category
as of Prompt 315, not the weekly Decision Gate) should use the existing
five-part reasoning shape.
## Sources

- shared benchmark/rules source;
- exact shared package provenance/receipt;
- any course source used to interpret probability/model limits;
- AI help if used.

## Rules / Assumptions

- operational definition of `better`;
- sample size/seed bundle;
- fixed game rules;
- declared decision threshold/criterion;
- important model assumptions.

## Work

- prediction;
- evidence table/plot;
- comparison across samples/metrics.

## Check Your Answer

- one attempted falsification/counterexample/alternate interpretation;
- one peer or AI interpretation audited;
- one model limitation.

## One-Sentence Summary

A bounded conclusion that includes the condition under which it is supported.

---

# What Week 16 deliberately does not become

- no new statistics unit;
- no p-value requirement;
- no proof that a strategy is globally optimal;
- no new ML algorithm implementation;
- no leaderboard as the learning objective;
- no GPU/cloud requirement;
- no new comprehensive final;
- no duplicate Farkle engine;
- no giant programming task.

---

# Success condition

Students should leave Week 16 able to look at a computational comparison and say:

> **Here is the claim, here are the assumptions and denominators, here is how stable the evidence was, here is what the model cannot establish, and here is the limited decision I am willing to defend.**

That is the DSCT payoff.
