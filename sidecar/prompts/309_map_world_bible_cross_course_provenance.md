# Prompt 309 — Map World Bible provenance across CS1, CS2, and DSCT

**Status:** FOREMAN-READY READ-ONLY CROSS-COURSE ARCHAEOLOGY  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Primary write scope:** DSCT report/evidence only  
**Required report:** `sidecar/reports/309_world_bible_cross_course_provenance.md`

## Direction already known

The design quarry has a strong direction:

> The **World Bible** is worth preserving as a recognizable cross-course artifact family.

Its value is personalization, continuity, and visible intellectual history. It should not automatically mean fiction and should not become ceremonial duplicate homework.

The quarry proposes a progression worth testing against actual course evidence:

- **CS1:** ownership, identity, what exists in the student's world, what was built/broke/changed;
- **CS2:** design state, decisions, tests/evidence, debt, recovery, interfaces/contracts, accepted/rejected proposals;
- **DSCT:** potentially a reasoning history of claims, assumptions, examples/counterexamples, evidence, confidence, revision, and what would change the student's mind.

That progression is a hypothesis to verify against repository evidence, not a fact to repeat uncritically.

## Decision explicitly NOT made

Prompt 309 does **not** decide:

- literal cross-course carry-forward versus a fresh course-native World Bible;
- whether prior students import the same file/repository/artifact;
- final DSCT World Bible fields;
- final DSCT update cadence;
- which claims DSCT should track longitudinally;
- whether the student-facing name remains exactly `World Bible`;
- grading weight or assignment structure.

Those choices remain with Jeremy + ChatGPT.

## Scope boundary relative to Prompt 305

Prompt 305 inventories **DSCT vocabulary and object collisions**.

Prompt 309 investigates **World Bible history and implementation across CS1, CS2, and DSCT**.

Do not turn Prompt 309 into another full Odyssey/Quest/Gate vocabulary inventory. Mention those terms only when needed to explain the World Bible's actual relationship to course work.

## Why this is Foreman-ready

The worker is answering evidence questions:

- where the World Bible appears;
- what students were actually asked to put in it;
- how often it changes;
- what other course work feeds it;
- whether it is graded;
- whether it persists;
- whether prior-course continuity is implemented, merely suggested, or absent.

That is provenance archaeology. The future policy is not delegated.

## Required work

### 1. Freeze the evidence base

For every course repository inspected, record:

- exact repository name;
- branch/ref;
- starting commit SHA;
- relevant source paths.

Use current `main` for current doctrine. Inspect historical branches/reports only when clearly labeled as archaeology.

If the correct CS1/CS2 repository name is uncertain, resolve it from Jeremy's accessible repositories rather than guessing silently.

### 2. Search for World Bible and predecessor concepts

Search current and historically relevant sources for at least:

- `World Bible`
- `world bible`
- `living record`
- `project record`
- `project receipt`
- `charter`
- `current state`
- `known debt`
- `what changed`
- obvious assignment/template names that implement the same artifact even when `World Bible` is not in the filename

Do not treat every generic use of `world`, `record`, or `charter` as relevant. Use context.

Record exact search commands/terms in the report.

### 3. Build one implementation card per course

For **CS1**, **CS2**, and **DSCT**, document the strongest current evidence for:

- student-facing name(s);
- first introduction/onboarding point;
- whether it is required, optional, or unclear;
- artifact shape/location: file, section, repository document, submission, etc.;
- fields/prompts actually requested;
- examples/world types offered;
- fictional versus domain/system flexibility;
- update trigger/cadence actually stated;
- relationship to weekly gates/checkpoints/assignments;
- grading relationship if any;
- relationship to Pair/Show/social work if any;
- AI/tool evidence expectations if any;
- whether prior entries are preserved as history or simply overwritten;
- explicit portability/import/carry-forward language;
- bootstrap path for a student with no prior World Bible;
- contradictions between planning, assignment, rubric, template, and student-facing source.

Every substantive statement must cite repository + commit/ref + path in the report.

### 4. Separate doctrine from implementation

For each course, distinguish:

- **CURRENT DOCTRINE** — planning/design/grading language intended to govern the course;
- **STUDENT-FACING IMPLEMENTATION** — what students actually see/do;
- **HISTORICAL / PROVENANCE** — older evidence that explains how the artifact evolved;
- **ASPIRATIONAL / NOT IMPLEMENTED** — design language with no matching student-facing artifact found;
- **AMBIGUOUS** — sources conflict or evidence is incomplete.

This distinction matters. Do not report an aspirational planning paragraph as though students already use it.

### 5. Build a cross-course comparison matrix

Compare CS1 / CS2 / DSCT across at least:

- purpose;
- artifact shape;
- personalization mechanism;
- persistence/history;
- evidence fields;
- engineering/reasoning depth;
- update cadence;
- grading connection;
- bootstrap path;
- carry-forward language;
- anti-bureaucracy posture;
- relationship to the course's Odyssey/gate structure.

### 6. Identify observed commonalities and divergences

Create two evidence-backed lists:

#### OBSERVED COMMONALITIES

Mechanics or purposes that actually recur across two or more course sources.

#### COURSE-SPECIFIC DIVERGENCES

Places where CS1, CS2, and DSCT deliberately or accidentally use different structures.

Do not convert commonality into a future requirement. Do not convert divergence into a defect automatically.

### 7. Test the carry-forward hypothesis against evidence

Report exactly what the repositories currently support:

- literal same-artifact carry-forward explicitly implemented;
- optional reuse/import language;
- thematic continuity only;
- no carry-forward language found;
- hidden prior-course assumption;
- explicit fresh-start/bootstrap support.

If no source supports literal carry-forward, say so. If one does, cite it precisely.

### 8. Identify anti-bureaucracy evidence

Find concrete evidence for or against the quarry principle that the World Bible should record meaningful change rather than require empty ceremonial updates.

Look for:

- append/update only when something changed;
- concise one-line receipts;
- integration into existing weekly work;
- duplicate reflections;
- mandatory weekly entries regardless of substance.

Report what exists. Do not redesign it here.

## Required report

Create `sidecar/reports/309_world_bible_cross_course_provenance.md` containing:

1. DSCT starting commit SHA;
2. repository/ref/commit inventory for CS1, CS2, DSCT;
3. search method/terms;
4. implementation card for each course;
5. doctrine-vs-implementation findings;
6. cross-course comparison matrix;
7. observed commonalities;
8. course-specific divergences;
9. carry-forward evidence matrix;
10. bootstrap/transfer-student evidence;
11. anti-bureaucracy findings;
12. contradictions/uncertainties;
13. exact decisions returned to Jeremy + ChatGPT;
14. verification results.

## Write authority

Allowed writes are limited to:

- `sidecar/reports/309_world_bible_cross_course_provenance.md`;
- optional Prompt-309 evidence under `sidecar/runs/309_*`.

Do not edit CS1, CS2, DSCT course source, the raw quarry, assignments, grading, or sibling repositories.

## Hard stops

Do **not**:

- choose literal carry-forward versus course-native fresh artifact;
- invent import/migration mechanics;
- rename World Bible;
- decide required DSCT update frequency;
- choose DSCT World Bible fields;
- decide which claims deserve longitudinal tracking;
- create or alter gradebook objects;
- edit CS1/CS2 to make them look more consistent;
- infer implementation from design prose without finding student-facing evidence;
- change Savnac/Canvas.

## Verification battery

### A. Repository provenance audit

Every course-level finding must trace to:

- repository;
- exact commit/ref;
- path.

No memory-only claim passes.

### B. Surface coverage audit

For each course, explicitly state whether these source families were inspected and what was found:

- planning/design docs;
- assignments;
- rubrics;
- student-facing templates/content;
- grading model;
- sidecar reports/raw history where relevant.

If a surface does not exist, record `NOT PRESENT`.

### C. Doctrine-versus-implementation audit

Every major World Bible behavior in the final comparison must be labeled as current doctrine, student-facing implementation, historical, aspirational, or ambiguous.

Do not let planning language silently substitute for implementation evidence.

### D. Carry-forward claim audit

Any claim that students can or should carry a World Bible across courses must point to explicit source evidence.

If only conceptual similarity exists, label it **FAMILY RESEMBLANCE / NO LITERAL CARRY-FORWARD EVIDENCE FOUND** rather than overstating continuity.

### E. Write-scope audit

Run:

- `git diff --check`
- `git diff --name-only`

Only the required report and optional Prompt-309 evidence may change in DSCT. Sibling repositories must remain unmodified.

## Definition of done

Prompt 309 is complete only when:

1. CS1, CS2, and DSCT each have an evidence-backed implementation card;
2. current doctrine is distinguished from actual student-facing implementation and history;
3. the cross-course comparison exposes both commonality and divergence;
4. carry-forward/bootstrap claims do not exceed explicit evidence;
5. anti-bureaucracy evidence is concrete rather than aspirational;
6. every substantive finding has repo + commit/ref + path provenance;
7. no future World Bible policy has been chosen;
8. Jeremy + ChatGPT can decide the DSCT World Bible contract from actual course lineage rather than memory or analogy.