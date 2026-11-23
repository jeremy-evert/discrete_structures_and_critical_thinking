# Instructor Guide — Week 16 Farkle + Machine Learning

## Week identity

**Tuesday Dec. 1 / Thursday Dec. 3, 2026**

Central question:

> **When a Farkle strategy appears better, what are we actually justified in believing?**

This is synthesis. Do not turn it into a statistics lecture, a programming project, or a tournament whose winner becomes the learning objective.

The computational source of truth is the canonical shared repository:

`jeremy-evert/Farkle_and_Machine_Learning`

DSCT owns the reasoning task.

---

# Before releasing the week

## Shared package

From a current shared checkout:

```text
python scripts/validate.py
```

Retain the generated shared validation receipt.

## Synchronize the course vendor copy

From the shared checkout, with the DSCT repo at the expected local path:

```text
python scripts/sync_consumer.py ../discrete_structures_and_critical_thinking/lessons/vendor/farkle_ml --apply
python scripts/sync_consumer.py ../discrete_structures_and_critical_thinking/lessons/vendor/farkle_ml --check
```

Do not edit the generated package in DSCT.

## Course seam validation

From the DSCT checkout:

```text
python scripts/validate_week16_farkle.py
```

Retain its raw receipt.

## Fallback evidence

After the real shared/DSCT validation succeeds, retain one generated `classroom_v1` evidence table from the exact synchronized shared commit.

Use that as the classroom fallback if live execution fails.

Do not hand-author plausible-looking win-rate numbers.

---

# What students need to know about Farkle

They do not need full game-design expertise.

They need only enough to understand:

- a player accumulates turn score;
- a Farkle loses the current turn score;
- after a scoring roll a strategy chooses ROLL or BANK;
- the classroom rules/target are fixed;
- a strategy sees a defined state;
- repeated games contain randomness;
- starting position is deliberately balanced in comparisons.

If rules discussion starts eating the lesson, point to the shared rule sheet and move to evidence.

---

# Tuesday — 75 minutes

## 0–8 min — AI Fluency / convincing wrong answer

Put this claim on screen:

> Strategy A won 53 of 100 games and B won 47. A is clearly the better strategy.

Ask:

> **What would make that a convincing wrong answer?**

Collect possibilities without adjudicating all of them yet.

Useful student suspicions:

- one sample;
- 53/47 may be too small a difference for the decision;
- starter imbalance;
- different rules;
- unclear strategy definition;
- wrong denominator;
- `better` not defined.

## 8–18 min — Professional judgment bridge

Question:

> When somebody gives you one clean metric at work, what do you ask before accepting the recommendation?

Keep this short. The bridge is evidence discipline, not business theater.

## 18–35 min — Technical/demo: make the machine inspectable

Show:

- fixed rule contract;
- public state fields;
- two strategy identifiers;
- raw receipt fields;
- starter balancing;
- seed identity.

Run or open one `initial` comparison.

Do **not** begin by showing the bundle average. Let the first sample tempt them.

## 35–62 min — Reasoning challenge

Students work through Parts 1–3 of the student lab:

- define `better`;
- declare a decision rule;
- predict;
- inspect/run initial evidence;
- identify how it could mislead.

Pair discussion is fine, but each student records an individual reasoning trail.

## 62–75 min — Exit trace

Require a Tuesday one-sentence summary in this shape:

> In this sample, under these assumptions, ______, but I am not yet willing to claim ______ because ______.

Save the unresolved question for Thursday.

---

# Thursday — 75 minutes

## 0–10 min — Reflection / prediction retrieval

Have students reopen Tuesday's criterion and prediction **before** the bundle evidence.

Ask:

> Are you about to grade the evidence by whether it agrees with you?

## 10–25 min — Bundle evidence

Run/open:

```text
python lessons/week-16-farkle-evidence.py bundle
```

Show the per-seed rows first.

Then show the transparent descriptive summary:

- mean;
- min;
- max;
- range of A-B win-rate difference.

Avoid implying that these four numbers create formal statistical proof.

## 25–48 min — Inspect, reorder, limit

Students complete Parts 4–6:

- compare seed rows;
- test their declared decision rule;
- inspect one alternate metric;
- name a model limitation.

Good instructor questions:

- Would you tell the same story if the seed with the largest difference disappeared?
- What denominator created this rate?
- If we doubled the games, which problem might improve and which problem would remain?
- If the learner never sees opponent score, what claims should that make you cautious about?
- Does a higher win rate against this baseline imply universal superiority?

## 48–60 min — AI/confident explanation audit

Use live AI only when appropriate and accessible. Otherwise use a prepared example.

Give the interpreter the same raw table and ask for the `best strategy`.

Students mark:

- overclaim;
- hidden assumption;
- denominator omission;
- unsupported causality;
- unexplained `best` criterion;
- ignored model limit.

Then repair one sentence.

## 60–70 min — Peer critique and final move

Each student shares:

- decision rule;
- final claim;
- model limitation.

Peer asks one question intended to break the claim.

Student chooses:

- defend;
- revise;
- refuse.

## 70–75 min — Exit

Collect the One-Sentence Summary or completion signal for the weekly Reasoning Odyssey receipt.

---

# Useful wrong claims

These are discussion fuel, not answer keys.

## `A won this run, therefore A is better.`

Attack:

- scope;
- sample variability;
- criterion definition.

## `10,000 simulated games prove A is optimal.`

Attack:

- simulation estimates behavior under the model;
- finite sample;
- opponent/rules/state limits;
- `optimal` is broader than the experiment.

## `The exact same seed reproduced, so the conclusion is reliable.`

Attack:

- reproducibility of one trajectory is not evidence of robustness across trajectories.

## `A is ahead by 0.4 percentage points, so A matters.`

Attack:

- numerical difference versus decision significance;
- predeclared threshold.

## `Machine learning should beat a rule because it learned.`

Attack:

- complexity is not evidence of quality;
- training objective/state/data may be limited.

## `The biggest number is the best strategy.`

Attack:

- best by what ordering relation/objective?

---

# What to assess

Reward:

- precise claim;
- visible assumptions;
- raw evidence/denominators;
- checking across samples/interpretations;
- model limitation;
- defensible revision judgment;
- reproducible trail.

Do not reward:

- picking the strategy that happened to win;
- using the largest sample merely because it looks impressive;
- writing more prose;
- adding advanced statistics not understood by the student;
- using AI more extensively.

---

# Live failure plan

If student execution fails:

1. confirm the course vendor synchronization was validated before class;
2. avoid turning class into environment debugging;
3. distribute/open the validated fallback evidence generated from the exact shared commit;
4. continue the reasoning lab from the evidence table;
5. record the technical yellow separately.

The reasoning objective does not require every student's machine to simulate live during the class period.

---

# Boundaries

Do not add:

- p-value lecture;
- formal confidence-interval requirement;
- new machine-learning theory;
- Farkle-engine coding assignment;
- leaderboard grade;
- comprehensive final;
- GPU/cloud requirement.

The week succeeds when students make a narrower, better-supported claim than the one the first shiny percentage invited them to make.
