# Prompt 308 — Harvest verified Week 4–14 open/free resource candidates

**Status:** FOREMAN-READY RESEARCH / PROVENANCE  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Primary write scope:** DSCT report/evidence only  
**Required report:** `sidecar/reports/308_week4_14_open_resource_harvest.md`

## Resource philosophy already decided

If students genuinely need to buy a book, they buy one.

If they do not need to buy a book, DSCT should not replace one commercial textbook with one arbitrary free textbook merely to preserve the appearance of a textbook-driven course.

Instead, the course should curate the best useful slices from strong resources and connect them with coherent course-owned instruction.

External resources are ingredients. The course provides the connective tissue.

## Decision explicitly NOT made

Prompt 308 does **not** decide:

- which of the current twelve topic bundles become the final eleven Week 4–14 core weeks;
- which topics combine, move, narrow, or become recurring lenses;
- the final required reading list;
- final week/date assignment;
- whether one paid textbook eventually earns a required place;
- final lesson/activity design.

Those choices remain with Jeremy + ChatGPT.

## Source-role vocabulary

Use these source-role labels:

- **PRIMARY** — official/specification/normative or original truth layer where appropriate;
- **ADAPT** — material that may legally be adapted/reused under a verified compatible license, with attribution requirements recorded;
- **LINK** — useful public material that should be linked rather than copied/adapted;
- **TOOL** — official documentation/software/tooling;
- **CURRENT EVIDENCE** — time-sensitive evidence that must be date-stamped;
- **EXPLANATION** — strong pedagogical explanation that is not itself the primary truth source.

A source may legitimately carry more than one role if the reasons are explicit.

## Known candidate families to inspect

At minimum inspect relevant material from:

- MIT OpenCourseWare, especially *Mathematics for Computer Science*;
- Oscar Levin, *Discrete Mathematics: An Open Introduction*;
- Matthew Van Cleave, *Introduction to Logic and Critical Thinking*;
- Open Logic Project;
- SWOSU-owned material already present in accessible repositories;
- strong public-university course notes/materials;
- official tool/documentation sources where tools matter;
- a small number of genuinely useful public talks/videos/demos.

This is a starting list, not a quota and not a final canon.

## Coverage frame

Use the current DSCT topic map as a **coverage checklist only**, not as a frozen week allocation.

The current formal topic families to cover are:

1. Logic, Claims & Proof
2. Sets, Functions & Sequences
3. Algorithms, Correctness & Growth
4. Integer Properties & Cryptography
5. Induction, Recursion & Recurrences
6. Counting & Combinatorial Reasoning
7. Probability, Uncertainty & Evidence
8. Relations, Equivalence, Partial Orders, Matrices & Digraphs
9. Graphs & Network Reasoning
10. Trees, Search & Decision Structures
11. Boolean Algebra, Circuits & SAT
12. Finite-State Machines, Invariants & Model Limits

Do not infer from this list that all twelve remain standalone weeks.

## Required work

### 1. Freeze provenance

Record:

- DSCT starting commit SHA;
- retrieval date;
- exact URL or repository + commit/ref + path for every candidate;
- author/institution/publisher identity where available.

Do not cite a search-result snippet as the source. Open and verify the actual resource.

### 2. Build source cards by topic family

For every current topic family, produce at least one verified candidate when a credible one exists.

Prefer two or more complementary candidates when they serve genuinely different roles, for example:

- one strong formal/open reading;
- one alternate explanation or worked example;
- one short video/demo;
- one computational/proof/activity bridge.

Do not fill slots with mediocre material merely to hit a count. If a topic lacks a candidate worth recommending, mark the gap explicitly.

Each source card must include:

- topic family;
- source title;
- author/institution;
- source-role label(s);
- exact useful slice: chapter/section/page range/module/video segment/tool page, not merely the home page;
- what concept or reasoning move the slice is good for;
- Critical Thinking connection;
- proof/counterexample bridge where applicable;
- computational/simulation bridge where applicable;
- AI-verification angle where applicable;
- estimated student burden when reasonably inferable: reading length, page count, video duration, or activity scale;
- why this candidate earned attention;
- what **not** to assign wholesale;
- course-owned connective tissue likely required.

### 3. Verify access separately from reuse rights

For every candidate, record both:

#### Access class

- **FREE-NO-LOGIN**
- **FREE-LOGIN**
- **INSTITUTIONAL-ACCESS**
- **PAID**
- **UNKNOWN / UNVERIFIED**

#### Reuse class

- **OPEN-LICENSE-VERIFIED** — record exact license and license evidence;
- **PUBLIC-LINK-ONLY** — publicly accessible but adaptation/copy rights are not established;
- **INSTITUTION-OWNED** — SWOSU/course-owned material with provenance noted;
- **COPYRIGHT / RIGHTS-UNCLEAR** — link/evaluate only, do not adapt;
- **UNKNOWN / UNVERIFIED**.

**Free to read does not imply permission to copy or adapt.**

### 4. Verify current availability

For each recommended candidate:

- open the actual resource during this run;
- verify the useful slice still exists;
- verify whether authentication/payment is required;
- verify the license/reuse claim from the resource or an authoritative license/source page;
- record retrieval date;
- note broken redirects, stale mirrors, or unstable links.

If live verification fails, keep the source only as **UNVERIFIED** evidence, not as a recommended required-course candidate.

### 5. Evaluate pedagogical fit without choosing the curriculum

For each candidate, briefly assess:

- **AUTHORITY** — why this source deserves trust for its role;
- **FIT** — what exact DSCT concept/reasoning move it serves;
- **CLARITY** — whether the slice is realistically usable by students at this level;
- **BURDEN** — whether the amount assigned could stay proportionate;
- **ACCESSIBILITY** — captions/transcript for video when available, readable formats, obvious barriers;
- **REUSE SAFETY** — whether DSCT should adapt, link, or only use as background.

Do not collapse these dimensions into a fake numerical score. Explain the tradeoff.

### 6. Identify gaps honestly

For each topic family, state whether external resources adequately cover:

- formal concept explanation;
- worked example/proof support;
- Critical Thinking connection;
- computational/hands-on bridge;
- accessible student path.

Where they do not, mark **COURSE-OWNED CONTENT NEEDED** and say what kind of connective tissue or activity is missing.

Do not pretend a link pile is a course.

## Required report structure

Create `sidecar/reports/308_week4_14_open_resource_harvest.md` containing:

1. starting commit SHA and retrieval date;
2. search/research method and source families inspected;
3. topic-family coverage table;
4. detailed source cards;
5. access/reuse-rights matrix;
6. broken/stale/unverified source list;
7. course-owned-content gaps;
8. especially strong cross-topic resources worth considering later;
9. explicit decisions returned to Jeremy + ChatGPT;
10. verification summary.

Optional machine-readable URL/license checking evidence may live under `sidecar/runs/308_*`.

## Write authority

Allowed writes are limited to:

- `sidecar/reports/308_week4_14_open_resource_harvest.md`;
- optional Prompt-308 research/verification receipts under `sidecar/runs/308_*`.

Do not edit planning, weekly lessons, assignments, grading, the topic map, or sibling repositories.

## Hard stops

Do **not**:

- decide the final eleven-week intellectual spine;
- combine or remove topic families;
- assign resources to final calendar dates;
- declare one textbook the course spine;
- reintroduce ZyBooks as an operational requirement;
- copy/adapt material without verified rights;
- treat `FREE-NO-LOGIN` as equivalent to `OPEN-LICENSE-VERIFIED`;
- author final weekly lessons;
- change grading;
- write Canvas/Savnac.

## Verification battery

### A. Topic coverage audit

All twelve current topic families must appear in the coverage table.

Each must be marked as either:

- adequately served by one or more verified candidates; or
- **COURSE-OWNED CONTENT NEEDED / GAP** with an explanation.

No topic may disappear because the worker personally thinks it should be merged later.

### B. Candidate provenance audit

Every recommended candidate must have:

- exact useful slice;
- verified retrieval date;
- access class;
- reuse class;
- authority/fit rationale;
- source URL or repo + commit + path.

A home-page-only citation is insufficient when a specific instructional slice is being recommended.

### C. License audit

Every `ADAPT` or `OPEN-LICENSE-VERIFIED` classification must point to authoritative license evidence.

If rights cannot be verified, downgrade to `LINK`, `PUBLIC-LINK-ONLY`, `COPYRIGHT / RIGHTS-UNCLEAR`, or `UNKNOWN / UNVERIFIED` as appropriate.

### D. Live-availability audit

Every resource proposed for the required free path must have been opened successfully during the run and must not require payment.

Login/institutional access may still be reported as optional evidence but must be labeled clearly.

### E. Anti-link-pile audit

For every topic family, confirm the report answers:

- what exact slice is useful;
- why it is useful;
- what student should do with it;
- what course-owned explanation/activity still has to connect it to DSCT.

If those answers are missing, the harvest is not instructional evidence yet.

### F. Write-scope audit

Run:

- `git diff --check`
- `git diff --name-only`

Only the required report and optional Prompt-308 run evidence may change.

## Definition of done

Prompt 308 is complete only when:

1. all twelve current topic families have been deliberately covered or explicitly marked as gaps;
2. recommended sources have exact slices, current access verification, provenance, and honest reuse-rights classification;
3. free access and adaptation rights are never conflated;
4. weak/broken/unverified candidates are clearly separated from recommended ones;
5. course-owned connective-tissue gaps are explicit;
6. no final week allocation or topic-combination decision has been made;
7. Jeremy + ChatGPT can compare the intellectual-spine options using a verified source catalog rather than vague memory, stale URLs, or whole-book recommendations.