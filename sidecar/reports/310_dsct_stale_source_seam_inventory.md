# Prompt 310 — DSCT stale source seam inventory

**Status:** READ-ONLY AUDIT COMPLETE
**Worker branch:** `worker/prompt310-seam-audit`
**Worktree:** `/tmp/dsct-prompt310`

## 1. Starting DSCT commit SHA

`2ec8ea82b822a96d6bec987bb0306e51ce51376c` (`main`, equal to `origin/main` at
audit time — `git diff main origin/main --stat` was empty).

## 2. Branch / ref / commit inventory

### DSCT local branches (shared object store; this worktree branched from `main`)

| Branch | Tip commit | Relative to `main` (`2ec8ea8`) |
|---|---|---|
| `main` / `origin/main` | `2ec8ea8` | — |
| `worker/prompt310-seam-audit` (this job) | `2ec8ea8` at creation | new, audit-only |
| `worker/prompt305-vocabulary` | not independently re-walked; Prompt 305 report already merged to `main` | superseded by merged report |
| `worker/prompt306-reuse` | `851c5f4`→`8408bff` (per Prompt 306 report); report merged to `main` | superseded by merged report |
| `worker/prompt307-container-latex` | `08501ab5a4da1201988919be0b754e33d11cdd55` | report merged to `main` |
| `worker/prompt308-open-resource-harvest` | `d68af84` | report merged to `main` |
| `worker/prompt309-world-bible` | `2ec8ea8` (== `main`) tip commit, but **the separate live worktree at the repo's primary path is currently checked out on this branch with an uncommitted, untracked file** (`prompts/305_week2_assessment_contract_reconciliation.md`, pre-existing per Prompt 304/306 provenance notes, not created by this branch) | **IN PROGRESS elsewhere — not inspected further, not touched** |
| `worker/prompt311-pair-reasoning` | `38ebcca` (2 commits ahead of `main`: rewrites `assignments/pair-reasoning-report.md` + adds `sidecar/reports/311_pair_reasoning_contract.md`) | **UNMERGED EXECUTED WORK — see Seam 1** |
| `worker/prompt312-show-and-tell` | `2ec8ea8` (== `main`) | not yet executed |
| `worker/prompt313-cadence` | `2ec8ea8` (== `main`) | not yet executed |
| `worker/prompt314-decision-gate` | `2ec8ea8` (== `main`) | not yet executed |
| `worker/prompt315-checkpoints-farkle` | `2ec8ea8` (== `main`) | not yet executed |
| `worker/prompt316-container-ladder` | `2ec8ea8` (== `main`) | not yet executed |
| `worker/prompt317-revision-policy` | `2ec8ea8` (== `main`) | not yet executed |
| `golem/dsct-305-assessment-contract` | `2ec8ea8` (== `main`) | not yet executed |

### DSCT remote branches (`origin`)

| Ref | Commit | Content |
|---|---|---|
| `origin/main` | `2ec8ea8` | current truth |
| `origin/agent/prompt303-dsct-week2` | `85ea3a2cf446d2168d1d8210e297bf067389d51c` | historical/incoming Week 2 container/repeatability package (see §9, Seam 2/7) |
| `origin/agent/prompt305-dsct-assessment` | `e209a63d5f1c3021aae38f4d9d7831bb2122ae8c` | historical/incoming Week 2 assessment-contract fixtures (see §9, Seam 7) |
| `origin/worker/prompt306-reuse`, `.../prompt307-container-latex`, `.../prompt308-open-resource-harvest` | pushed worker copies of already-merged reports | superseded by `main` |

No local or remote DSCT branch was merged, rebased, cherry-picked, or deleted by this audit.

### External repositories inspected (repo + exact commit)

| Repository | Commit inspected | Role in this audit |
|---|---|---|
| `course_foundry` | `11a2a2c742b0b1a4f33494c04c2cb0a9f964b981` | Seam 8 — compiler/Savnac assumption audit |
| `local_ai_lab_setup` | `b2b2ec1afcea98c59a5ab3818cd361a29eb0f99c` | Seam 2/10 — shared Week 2 AI Lab ownership (re-confirmed unchanged since Prompt 306) |
| `windows_classroom` | `f87e340aad4bf4e4e2c064abc676afdcc5260b48` | Seam 2/10 — shared Windows runtime harness (re-confirmed unchanged since Prompt 306) |
| `professional_minds` | `af54438aeb4bddbbceed4524bc10379b0b9d5a3c` | Seam 10 — no DSCT-specific file found; no duplication seam identified |
| `ai_fluency` | `022262cf207c28a9504425779a24247ddcf66884` | Seam 10 — DSCT named as a host-course delivery target in `architecture/ai_fluency_delivery_architecture.md`, `architecture/ai_iii_host_course_delivery_map.md`, `reports/010_host_course_delivery_architecture.md` |
| `container_foundations` | `b9bb9656f73fe4db7737ee7088e363ecafb115a0` | Seam 2 — noted as an existing container-curriculum repository; not deep-audited (Prompt 316 owns that inspection; see §5 dependency table) |
| `computer_architecture` | `ba1eb7eccc5bf5731881a09a67422b6aa3903db8` | Cited via Prompt 306/307 reports — reusable container/LaTeX and Week 2 epistemic-framing evidence, not copied |
| `computer_science_2` | `origin/main` `5c3c83db7a7b4cd84adf5de80c6b728f16cf6c9d` | Cited via Prompt 306 report — Week 2 CS2 wrapper ownership evidence, not copied |

No external repository was modified. All external inspection was read-only (`git rev-parse`, `git show`, `grep`/`rg`).

## 3. Inspected source-surface checklist

| Required surface | Status | Note |
|---|---|---|
| `planning/fall-2026-spine.md` | Present, inspected | Seams 2, 3, 6 |
| `planning/fall-2026-weekly-architecture.md` | Present, inspected | Seams 1, 3, 9 |
| `planning/fall-2026-topic-map.md` | Present, inspected | Seam 3, 5 |
| `planning/fall-2026-course-design.md` | Present, inspected | Seam 5 |
| `docs/grading-model.md` | Present, inspected | Seams 1, 4, 9 |
| Assignments/rubrics for pair/show/Odyssey/grading semantics | Present, inspected (`assignments/pair-reasoning-report.md`, `assignments/show-and-tell-artifact.md`, `assignments/weekly-problem-solving-writeup.md`, `assignments/week-16-farkle-evidence-receipt.md`) | Seams 1, 4, 6, 9 |
| Reasoning Odyssey / World Bible current surfaces | Present, inspected (`planning/fall-2026-weekly-architecture.md:41-64`; `week-02/student/week-02-evidence-assignment.md`) | Seam 9 |
| Week 2 source/history | Present, inspected (`week-02/`, `planning/week-01-source-map.md`, historical branches) | Seams 2, 7 |
| Week 16 validated package/report | Present, inspected (`planning/week-16.md`, `week-16/`, `sidecar/reports/week16_farkle_ml_postmortem.md`, `sidecar/runs/week16_farkle_validation_20260816T211906Z.md`) | Seam 6 |
| Historical ZyBooks/source-decision material | Present, inspected (`planning/zybooks-section-decisions.csv`, `planning/fall-2026-course-design.md:84-99`) | Seam 5 |
| `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md` | Present; treated as design evidence, cited via Prompt 304/305 reports, not re-derived line-by-line here | Seams 1, 9 |

No named path in the prompt's minimum-inspection list was `NOT PRESENT`.

## 4. Known-seam checklist — all ten required seams, explicit disposition

### Seam 1 — stale `Pair Programming` naming vs. decided **Pair Reasoning** name

- **Design-status:** DECIDED (Jeremy + ChatGPT, per `sidecar/prompts/304_reconcile_pair_reasoning_name.md` and `sidecar/prompts/311_define_pair_reasoning_contract.md`).
- **Seam status: ALREADY-RESOLVED for the naming migration itself**, with proof:
  `sidecar/reports/304_pair_reasoning_name_reconciliation.md` (DSCT commit
  `44169f8d53eeb63d4345f44db6d4d8604bb7f277`, merged to `main`) renamed
  `assignments/pair-programming-report.md` → `assignments/pair-reasoning-report.md`
  and updated `docs/grading-model.md`, `planning/fall-2026-weekly-architecture.md`,
  `planning/fall-2026-topic-map.md`. A residual `rg -i 'pair programming'`
  sweep on current `main` returns only `archive/**`, `docs/curriculum/**`,
  `docs/philosophy/**`, `docs/reports/**`, and Prompt-304/310 self-references —
  all correctly `PRESERVE-HISTORICAL` per Prompt 304's own table.
- **Residual finding (not yet on `main`):** Prompt 304 explicitly left the
  renamed template's CS2-style driver/navigator role language and stub
  content intact — that was Prompt 311's job. **Prompt 311 has already been
  executed on the unmerged local branch `worker/prompt311-pair-reasoning`
  (commit `38ebcca`)**, which rewrites `assignments/pair-reasoning-report.md`
  into the full six-field Pair Reasoning contract and adds
  `sidecar/reports/311_pair_reasoning_contract.md`. This work is **not yet on
  `main`**. Until it is merged, `main`'s `assignments/pair-reasoning-report.md`
  still carries the pre-Prompt-311 CS2-flavored stub.
- **Impact:** LOW (naming) / MEDIUM (the unmerged CS2-flavored stub could be
  copied by an author who does not know Prompt 311 already fixed it on a
  branch).
- **Safe mechanical repair:** merge `worker/prompt311-pair-reasoning` to `main`
  through normal Foreman acceptance; no new authoring needed.
- **Blocking decision:** none — Foreman-acceptance/merge only.

### Seam 2 — older Week 2/3 contract vs. newer **Week 2 Building Your AI Lab / Week 3 Containers + minimum-useful LaTeX** direction

- **Design-status:** DECIDED (Week 2 identity) / DECIDED (Week 3 pinned-container
  direction, per `sidecar/prompts/316_define_week3_pinned_container_skill_ladder.md`,
  "The design decision is now settled at the course level").
- **Current source:** `planning/fall-2026-spine.md:11` already states Week 2 =
  "Building Your AI Lab / Containers and Repeatability"; `planning/fall-2026-topic-map.md:12`
  already states Week 3 = "Logic, Claims & Proof" (Week 3's *technical topic*
  was never container/LaTeX — the container/LaTeX work is the Week 3
  *toolchain*, evaluated by Prompt 307).
- **Seam status: ALREADY-RESOLVED for Week 2's top-level identity**; **READY-MECHANICAL
  for Week 3's toolchain direction** — the pinned-container decision is settled
  (Prompt 316) but not yet implemented as course source. Prompt 307's probe
  (`sidecar/reports/307_week3_container_latex_student_path_probe.md`, DSCT
  commit `e0e7ef0`) proved only a **host-`pdflatex` baseline**; it explicitly
  found **no committed `Containerfile`/`Dockerfile`/`.tex` source in DSCT** and
  **no tested containerized LaTeX happy path**.
- **Residual stale surface:** `sidecar/reports/306_week2_shared_ai_lab_reuse_map.md`
  flags the *historical* DSCT `week-02/` container/repeatability package
  (`origin/agent/prompt303-dsct-week2` @ `85ea3a2`) as **STALE / SUPERSEDED**
  relative to the shared `windows_classroom`/`local_ai_lab_setup` path that is
  now the canonical Week 2 AI Lab implementation. That branch is unmerged and
  untouched (see §9).
- **Impact:** HIGH — a student-facing Week 3 toolchain does not exist yet; if
  authored against the host-`pdflatex` probe instead of the settled
  pinned-container direction, it would contradict Prompt 316's decision.
- **Safe mechanical repair:** none yet — no source currently claims a
  container-based Week 3 path that would need correcting; the risk is
  building the wrong thing, not fixing a wrong thing.
- **Blocking decision:** Prompt 316 (pinned base image, runtime choice,
  Tectonic vs. TeX Live/`latexmk`) has settled the direction but not yet
  chosen or validated the concrete image/engine — Prompt 316 itself is
  unexecuted (branch `worker/prompt316-container-ladder` == `main`).

### Seam 3 — twelve formal topic bundles (Weeks 3–14) vs. eleven formal core slots (Weeks 4–14)

- **Design-status:** STRONG DIRECTION, trending toward DECIDED. `sidecar/prompts/313_define_pair_show_alternating_cadence.md:37,147,169` explicitly
  states "Weeks 4–14: eleven formal DSCT core weeks" and instructs a future
  worker to "choose the final eleven Week 4–14 technical topics" and
  reconcile the topic map "where stale against the new Week 4–14 eleven-week
  spine" — i.e., this is Jeremy + ChatGPT's stated direction but is
  explicitly flagged inside its own source prompt as not yet chosen/executed.
- **Current source:** `planning/fall-2026-spine.md:31` states "Weeks 3–14 are
  exactly twelve formal DSCT topic weeks," and `planning/fall-2026-topic-map.md`
  lists exactly twelve rows (Weeks 3–14). Neither has been edited to reflect
  the eleven-week Week-4–14 framing.
- **Seam status: BLOCKED-DESIGN.** This is the exact seam Prompt 310's hard
  stops forbid solving ("do not solve the eleven-week intellectual spine" /
  "do not decide how twelve current topic bundles collapse into eleven
  slots").
- **Impact:** HIGH — the two counts are directly student-facing (which week
  gets a formal topic, which week is "spine-only" infrastructure/rotation),
  and any Course Foundry Week 3–14 build would need to pick one.
- **Blocking decision:** Jeremy + ChatGPT must decide whether Week 3 remains
  a twelfth formal topic bundle alongside its toolchain role, or whether Week
  3 becomes toolchain-only and the twelve-bundle topic map collapses to
  eleven (Weeks 4–14). `sidecar/prompts/313_define_pair_show_alternating_cadence.md`
  is evidence the eleven-week framing is the current direction, but it has
  not yet been executed against `planning/fall-2026-spine.md` or
  `planning/fall-2026-topic-map.md`.
- **Related evidence job:** Prompt 308 (Week 4–14 open-resource harvest,
  merged) already gathered resources under the eleven/twelve-week ambiguity;
  its report should be re-checked once the count is settled.

### Seam 4 — grading-model surfaces with useful weights but stale naming and unresolved checkpoint/due/revision mechanics

- **Design-status:** DECIDED for naming (Prompt 314, Decision Gate) and for
  revision/resubmission/highest-score policy (Prompt 317) and drop-lowest
  policy (Prompt 318); OPEN QUESTION for exact checkpoint-week selection
  (Prompt 315 partially resolves the *tiering*, not the exact weeks).
- **Current source:** `docs/grading-model.md` is internally consistent and
  arithmetically correct (`5×9 + 3 + 2 + 30 + 15 + 5 = 100%`, verified by
  direct sum in the file and independently re-summed here) but uses the
  **pre-Decision-Gate names** throughout: "Weekly reinforcement / Reasoning
  Odyssey gate," "A3/A4/A7 equivalent" labels, and explicitly states (line
  81) "Exact Canvas/Savnac object IDs, due dates, late rules, drop-lowest
  behavior, and the exact checkpoint-week selection remain deployment
  questions."
- **Seam status: READY-MECHANICAL for naming** (Prompt 314's Decision Gate
  rename is settled and non-arithmetic — a rename does not change any of the
  14 weight rows) **and for revision/late-policy mechanics** (Prompt 317's
  continuous 1%/24h + highest-score-kept rule is settled and already has a
  working `course_foundry` late-work adapter to bind to, per
  `sidecar/prompts/317_define_revision_resubmission_highest_score_policy.md:33-40`).
  **BLOCKED-DESIGN for exact checkpoint-week selection and drop-lowest
  parameters** — those remain named "deployment questions" in
  `docs/grading-model.md:81` itself and Prompt 318 (unexecuted) is the
  authorized place to settle drop-lowest count/eligibility.
- **Impact:** HIGH — grading is the most student-facing and Canvas/Savnac-consequential
  surface in the course.
- **Safe mechanical repair:** apply Prompts 314/317's already-settled naming
  and policy language to `docs/grading-model.md` once those prompts are
  executed; the underlying 14-row weight table does not need to change.
- **Blocking decision:** exact checkpoint weeks (Prompt 315) and drop-lowest
  parameters (Prompt 318) are unexecuted; both branches (`worker/prompt315-checkpoints-farkle`,
  `worker/prompt317-revision-policy` — note 317 policy language is settled
  but not yet applied to source) are still at `main` tip.

### Seam 5 — historical ZyBooks/textbook material as provenance, not operational path

- **Design-status:** DECIDED. `planning/fall-2026-course-design.md:4-13,84-99`
  states, verbatim: "DSCT has no required textbook or external course for
  Fall 2026," and frames the ZyBooks references and `zybooks-section-decisions.csv`
  KEEP/OPTIONAL/UNUSED decisions as provenance only.
  `planning/fall-2026-topic-map.md:1-8` repeats: "RECONCILED 2026-08-15:
  DSCT has no required textbook or external course... retained only as
  source provenance, not as an assigned reading path or course spine."
- **Seam status: ALREADY-RESOLVED.** A targeted `rg -n -i 'zybooks|required
  text|textbook'` sweep across `planning/`, `docs/`, `assignments/`,
  `week-01/`, `week-02/`, `week-16/` found zero current-operational-requirement
  hits. All hits are one of: (a) explicit "no required textbook" reconciliation
  language, (b) the historical `docs/curriculum/course-sequence.md` /
  `docs/reports/curriculum-history-synthesis.md` narrative of *past* semesters
  (2021–2026), correctly framed as history, or (c) `week-01/help-tools-status.md:24`
  stating that formal ZyBooks work is **not** assigned in Week 1.
- **Impact:** LOW — no leakage found; classification below (§7) is provided
  per the prompt's required leakage-audit structure regardless.
- **Safe mechanical repair:** none needed.
- **Blocking decision:** none.

### Seam 6 — Week 16 Farkle + ML as already validated/GREEN, must be integrated not rebuilt

- **Design-status:** DECIDED / VALIDATED.
- **Seam status: ALREADY-GREEN / DO-NOT-REBUILD**, with exact evidence:
  - `planning/fall-2026-spine.md:25` — Week 16 status column = `VALIDATED`.
  - `sidecar/reports/week16_farkle_ml_postmortem.md` — "Status: GREEN —
    AUTHORED, SYNCHRONIZED, AND VALIDATED AGAINST CANONICAL SHARED CORE."
  - `sidecar/runs/week16_farkle_validation_20260816T211906Z.md` — "status:
    **GREEN**," shared commit `d3a1ed379a652731b0b6237c33b4fe42c518ac9e`,
    consumer commit `bab5ef89fa08e73b88bcdabd736600b58c45ec13`, real bundle
    evidence at `week-16/fallback/quick_v1_results.csv` (3 rows, CPU-only, no
    GPU/cloud/paid dependency).
  - Artifact paths: `planning/week-16.md`, `week-16/README.md`,
    `week-16/student/farkle-evidence-lab.md`,
    `assignments/week-16-farkle-evidence-receipt.md`,
    `week-16/instructor/guide.md`, `lessons/week-16-farkle-evidence.py`,
    `scripts/validate_week16_farkle.py`, `week-16/fallback/quick_v1_results.csv`,
    generated vendor snapshot `lessons/vendor/farkle_ml/` (with
    `_SHARED_PROVENANCE.json`).
  - **Course Foundry/deployment dependency:** none observed yet — `course_foundry/course_foundry/dsct_desired_course.py`
    at `course_foundry@11a2a2c` only builds Week 1/2; Week 16 has no compiler
    wiring yet, so there is nothing on the Course Foundry side that could
    conflict with or accidentally rebuild Week 16.
  - **Which later seams may legitimately integrate it without rebuilding:**
    Seam 3 (eleven/twelve-week spine decision) may reference Week 16 as a
    synthesis endpoint but must not re-author its package; Seam 4 (grading
    naming) may rename "Weekly reinforcement / Reasoning Odyssey gate" to
    "Decision Gate" around Week 16 without touching its authored content,
    since `sidecar/reports/week16_farkle_ml_postmortem.md` already states "No
    new grading category was invented."
- **One superseded artifact note:** `sidecar/reports/week16_farkle_ml_current_state.md`
  (dated 2026-08-16, same day) is an **earlier, now-superseded** snapshot
  that says "WEEK 16 NOT YET AUTHORED" — it predates the postmortem/validation
  receipt and must be read as historical process evidence, not current status.
  A future author should not be confused by finding both files.
- **Impact:** HIGH if violated (rebuilding validated work), otherwise N/A —
  this is a preservation boundary, not an open problem.
- **Safe mechanical repair:** none — do not touch.
- **Blocking decision:** none; explicitly marked DO-NOT-REBUILD.

### Seam 7 — historical/incoming Week 2 and assessment branches as archaeology/salvage inputs, not blind merge targets

- **Design-status:** N/A (archaeology, not a design question).
- **Seam status: HISTORICAL-PRESERVE**, with exact evidence:
  - `origin/agent/prompt303-dsct-week2` @ `85ea3a2cf446d2168d1d8210e297bf067389d51c`
    — contains a `week-02/` student/instructor container/repeatability
    package, source maps, and runtime receipts. Per
    `sidecar/reports/306_week2_shared_ai_lab_reuse_map.md`, this is behind
    current `main` and classified **STALE / SUPERSEDED** (container/repeatability
    runtime superseded by the now-canonical shared `windows_classroom` +
    `local_ai_lab_setup` path), with salvageable evidence-oriented inventory
    and explicit receipts.
  - `origin/agent/prompt305-dsct-assessment` @ `e209a63d5f1c3021aae38f4d9d7831bb2122ae8c`
    — Week 2 readiness assessment contract and evidence-quality fixtures. Per
    the same report, classified **ADAPT FOR DSCT** — salvageable boundary
    cases/failure-mode vocabulary, but does not decide final grading or
    reflection semantics.
  - Neither branch was merged, cherry-picked, rebased, or deleted by this
    audit or by Prompt 306's audit. Both remain exactly at the commits above
    on `origin`.
  - `worker/prompt309-world-bible` is additionally **actively in progress**
    in a separate live worktree at audit time (uncommitted untracked file
    present); it was not inspected beyond confirming its tip commit equals
    `main` and it was not touched.
- **Impact:** MEDIUM — risk is an author blind-merging the stale container
  runtime instead of the shared AI Lab path, or a future worker not realizing
  Prompt 309's evidence is still being produced live.
- **Safe mechanical repair:** none authorized here (would require merge
  decisions).
- **Blocking decision:** which pieces of `prompt303-dsct-week2` (if any)
  should be salvaged before the branch is abandoned — reserved for whoever
  authors the real Week 2 exercise (see Seam 2).

### Seam 8 — Course Foundry/compiler/Savnac assumptions that may encode older Week 2/3, Pair Programming, grading, or course-structure contracts

- **Design-status:** N/A (audit of external code, not a DSCT design question).
- **Seam status: mostly ALREADY-RESOLVED / NOT PRESENT, with one EXTERNAL-DEPENDENCY caveat.**
  - `course_foundry/course_foundry/dsct_desired_course.py` @ `course_foundry@11a2a2c742b0b1a4f33494c04c2cb0a9f964b981`
    builds **only Week 1 and Week 2**. `grep -n -i "pair programming\|A3\|A4\|A7\|week 3\|week3\|topic.*week\|eleven\|twelve"`
    across `dsct_desired_course.py` and `dsct_savnac.py` returned **zero
    hits** — the compiler does not currently encode any Week 3–14 topic
    count, Pair Reasoning/Pair Programming category name, or A3/A4/A7 label,
    so it cannot presently be stale against Seams 1, 3, or 4.
  - `WEEK_2_TITLE = "DSCT Week 2 — Build the Lab, Then Make Results
    Reproducible"` (`dsct_desired_course.py:23`) is already aligned with the
    "Building Your AI Lab" direction, and `course_foundry/reports/137_dsct_savnac_deployment_reconciliation.md`
    (`course_foundry@2e5bd3955ec3b8c152d5c88f0f8b2357fcd58e58`) documents that
    the stale `tuesday/`/`thursday/` Week 2 path layout was already corrected
    to the current flat `week-02/student/*.md` layout, with the 40-point
    portfolio rubric cross-checked against `docs/grading-model.md`.
  - **EXTERNAL-DEPENDENCY caveat:** `course_foundry/course_foundry/dsct_desired_course.py:143`
    references shared object kinds including `"dsct-week2-claims"`; and the
    Week 2 build reads `local_ai_lab_setup`'s `curriculum/week2_module_manifest.yml`
    with an explicit staleness guard ("`local_ai_lab_setup` DSCT Week 2
    sequence changed; review before deployment," line 148) — this is a
    *working* cross-repo staleness check, not a stale seam, but it means any
    future Week 2 change on either side must keep both repos synchronized
    through that guard.
  - No Week 3–14 or Week 16 Course Foundry build exists yet, so there is
    currently no compiler code that could encode a stale eleven/twelve-week
    count or a stale "Weekly reinforcement / Reasoning Odyssey gate" vs.
    "Decision Gate" name for those weeks. This will become a real
    EXTERNAL-DEPENDENCY the moment such a build is authored, so any Seam
    3/4 repair prompt should check `course_foundry` again once it exists.
- **Impact:** LOW today, will become HIGH the day a Week 3–14/16 Course
  Foundry build is authored before Seams 3/4 are settled.
- **Safe mechanical repair:** none needed now.
- **Blocking decision:** none now; future compiler authoring should be
  sequenced *after* Seams 3 and 4, not before.

### Seam 9 — Reasoning Odyssey / Quest / Gate / World Bible vocabulary seams

- **Design-status:** Mixed — DECIDED for the ontology simplification
  (`sidecar/prompts/314_define_decision_gate_contract.md`: "Reasoning Odyssey"
  = semester-long frame, "Decision Gate" = the single recurring weekly
  individual submission; "Reasoning Quest" and "Reasoning Gate" are retired
  as competing student-facing names); OPEN QUESTION for World Bible
  carry-forward/required-vs-optional status and checkpoint-vs-gate distinction
  (per `sidecar/reports/305_reasoning_vocabulary_inventory.md`'s own
  "Questions for Jeremy + ChatGPT" section).
- **Current source:** `docs/grading-model.md:23` still uses "Weekly
  reinforcement / Reasoning Odyssey gate"; no current file uses "Decision
  Gate." `sidecar/reports/305_reasoning_vocabulary_inventory.md` is the full
  evidence-backed vocabulary inventory (14-row object matrix, ALIAS/OVERLOAD/
  DUPLICATE-HOMEWORK-RISK/STALE-LEGACY/GRADEBOOK-SEAM/UNRESOLVED collision
  classes) and is the authoritative citation for this seam; it is not
  re-derived here per Prompt 310's hard stop against duplicating Prompt
  305's job.
- **Seam status: READY-MECHANICAL for the Decision Gate rename** (decision is
  settled by Prompt 314; source has simply not been edited yet — Prompt 314's
  branch `worker/prompt314-decision-gate` is still at `main` tip).
  **BLOCKED-DESIGN for World Bible required/optional status, cadence, and
  cross-course carry-forward** (still an open question in both the current
  weekly-architecture text — "not mandatory fiction and not a required
  connection every week" — and in Prompt 305's unresolved-questions list).
- **Impact:** HIGH — this is the seam most likely to cause duplicate
  homework or a confusing multi-named weekly submission if not resolved
  before Weeks 3–14/16 are built out.
- **Safe mechanical repair:** rename "Reasoning Odyssey gate"/"Weekly
  reinforcement" to "Decision Gate" in `docs/grading-model.md` and
  `planning/fall-2026-weekly-architecture.md` once Prompt 314 is executed;
  no weight/arithmetic change required.
- **Blocking decision:** World Bible contract (required/optional, submission
  shape, cross-course carry-forward) remains open; reserved for a future
  prompt, not this one.
- **Related evidence job:** Prompt 305 (merged, `sidecar/reports/305_reasoning_vocabulary_inventory.md`).

### Seam 10 — shared AI Fluency / Professional Minds / local-AI/container ownership seams

- **Design-status:** DECIDED (ownership pattern) per user memory
  (`shared_strands_vs_ai_fluency_sequencing.md`: professional_minds is shared
  verbatim; AI Fluency is sequential per course, "AI Fluency I now, II–V
  Spring 2027") and per `sidecar/reports/306_week2_shared_ai_lab_reuse_map.md`'s
  three-owner model (shared spine/assignment owner, Windows runtime owner,
  course wrapper owner).
- **Current source / external evidence:**
  - `docs/grading-model.md:13-15` already points to "shared AI Fluency
    content" and "Professional Minds reflection object" for the Monday-Moment
    and Wacky-Wednesday/Fun-Friday-equivalent categories — DSCT does not
    duplicate that content locally; it references the shared strand by name.
  - `professional_minds@af54438aeb4bddbbceed4524bc10379b0b9d5a3c`: a
    case-insensitive repository-wide search for `discrete_structures`/`dsct`
    found **zero hits** — DSCT is not yet named as a specific consumer inside
    that repo, i.e. the pointer is currently one-directional (DSCT → shared
    repo by category name only, not confirmed by a matching entry in the
    shared repo).
  - `ai_fluency@022262cf207c28a9504425779a24247ddcf66884`: DSCT **is** named
    as a host-course delivery target in `architecture/ai_fluency_delivery_architecture.md`,
    `architecture/ai_iii_host_course_delivery_map.md`, and
    `reports/010_host_course_delivery_architecture.md`.
  - Week 2's AI Lab ownership (already covered in depth by Seam 2 and Prompt
    306) is the clearest instance of this seam family and is **not**
    duplicated: `sidecar/reports/306_week2_shared_ai_lab_reuse_map.md`
    confirms DSCT should be a thin wrapper around `local_ai_lab_setup`
    (shared spine) and `windows_classroom` (runtime), and that current DSCT
    `main` does not fork either.
- **Seam status: mostly ALREADY-RESOLVED / NOT PRESENT for duplication**;
  **AMBIGUOUS for the one-directional `professional_minds` pointer** (DSCT
  references the shared category by name, but the shared repo does not yet
  list DSCT as a consumer — this may simply reflect that `professional_minds`
  doesn't track per-course consumers the way `ai_fluency` does, which would
  make it a non-issue, but this audit did not confirm that pattern
  affirmatively).
- **Impact:** LOW — no duplication found; the ambiguity is a provenance gap,
  not a contradiction.
- **Safe mechanical repair:** none needed; if the `professional_minds`
  ownership pattern turns out to require a per-course pointer entry, that is
  a `professional_minds`-repo change outside DSCT's write scope.
- **Blocking decision:** none for DSCT source.

## 5. Full seam matrix

| ID | Short name | Impact | Current source | Newer direction source | Design-status | Seam status | Student risk | Author/agent risk | Downstream affected | Sibling/shared owner | Safe mechanical repair | Blocking decision | Related evidence job | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Pair Reasoning naming/contract | LOW/MEDIUM | `docs/grading-model.md`, `planning/fall-2026-{weekly-architecture,topic-map}.md`, `assignments/pair-reasoning-report.md` (on `main`) | `sidecar/prompts/304_*.md`, `311_*.md`; unmerged `worker/prompt311-pair-reasoning@38ebcca` | DECIDED | ALREADY-RESOLVED (naming) / READY-MECHANICAL (contract merge) | none once merged | author may copy stale CS2 stub if unaware of unmerged branch | `assignments/pair-reasoning-report.md` | none | merge `worker/prompt311-pair-reasoning` | none | Prompt 304 (merged), 311 (unmerged) | §4 Seam 1 |
| 2 | Week 2/3 direction | HIGH (Week 3 only) | `planning/fall-2026-spine.md:11`, `planning/fall-2026-topic-map.md:12`, no committed Week 3 container/tex source | `sidecar/prompts/316_*.md`; `sidecar/reports/307_*.md` | DECIDED (direction) / OPEN (image/engine) | ALREADY-RESOLVED (Week 2 identity) / READY-MECHANICAL-pending-authoring (Week 3, once image/engine picked) | none yet (nothing built) | building against host-pdflatex probe instead of pinned-container direction | future Week 3 student package, `course_foundry` | `container_foundations`, `computer_architecture` (reusable evidence only) | none yet — nothing to repair | pin base image + engine (Prompt 316, unexecuted) | Prompt 307 (merged), 316 (unexecuted) | §4 Seam 2 |
| 3 | 12 vs 11 topic bundles | HIGH | `planning/fall-2026-spine.md:31` ("exactly twelve"), `planning/fall-2026-topic-map.md` (12 rows) | `sidecar/prompts/313_*.md:37,147,169` ("eleven formal DSCT core weeks," Weeks 4–14) | STRONG DIRECTION | BLOCKED-DESIGN | HIGH if unresolved before build | HIGH — two authoritative counts | `planning/fall-2026-spine.md`, `planning/fall-2026-topic-map.md`, future Course Foundry Week 3–14 build | none | none (explicit hard stop) | choose Week 3's role: 12th topic bundle or toolchain-only | Prompt 308 (merged, resource harvest under ambiguity), 313 (unexecuted) | §4 Seam 3 |
| 4 | Grading naming + checkpoint/due/revision mechanics | HIGH | `docs/grading-model.md` (arithmetically correct, pre-Decision-Gate names, checkpoint/due/drop marked "deployment questions") | `sidecar/prompts/314_*.md`, `315_*.md`, `317_*.md`, `318_*.md` (all unexecuted) | DECIDED (naming, revision/late policy) / OPEN (checkpoint weeks, drop-lowest params) | READY-MECHANICAL (naming, revision policy) / BLOCKED-DESIGN (checkpoint weeks, drop-lowest) | HIGH if inconsistent at deployment | MEDIUM | `docs/grading-model.md`, future `course_foundry` grading wiring | `course_foundry` late-work adapter (already exists per Prompt 317 text) | apply Decision Gate rename + revision-policy language, no arithmetic change | exact checkpoint weeks (315), drop-lowest count/eligibility (318) | Prompt 314/315/317/318 (all unexecuted) | §4 Seam 4 |
| 5 | ZyBooks/textbook leakage | LOW | `planning/fall-2026-course-design.md:4-13,84-99`, `planning/fall-2026-topic-map.md:1-8` | same (already reconciled 2026-08-15) | DECIDED | ALREADY-RESOLVED | none | none | none | none | none needed | none | n/a | §4 Seam 5, §7 |
| 6 | Week 16 GREEN | HIGH if violated | `planning/week-16.md`, `week-16/`, `sidecar/reports/week16_farkle_ml_postmortem.md`, `sidecar/runs/week16_farkle_validation_20260816T211906Z.md` | n/a — this is the settled state | DECIDED / VALIDATED | ALREADY-GREEN / DO-NOT-REBUILD | none (preserve) | rebuilding wastes validated work | `lessons/vendor/farkle_ml/`, shared `Farkle_and_Machine_Learning` repo | `Farkle_and_Machine_Learning` (shared) | none — preserve | none | Prompt 303 (Week 16 build, merged) | §4 Seam 6, §8 |
| 7 | Historical/incoming branches | MEDIUM | `origin/agent/prompt303-dsct-week2@85ea3a2`, `origin/agent/prompt305-dsct-assessment@e209a63`, local `worker/prompt309-world-bible` (in progress elsewhere) | `sidecar/reports/306_*.md` dispositions | n/a | HISTORICAL-PRESERVE | none if not blind-merged | blind merge would reintroduce stale container runtime | `week-02/` | none | none authorized here | which pieces (if any) to salvage | Prompt 306 (merged) | §4 Seam 7, §9 |
| 8 | Course Foundry/compiler assumptions | LOW now / HIGH later | `course_foundry/course_foundry/dsct_desired_course.py@11a2a2c` (Week 1/2 only, already aligned) | n/a yet — no Week 3–14/16 build exists | n/a | ALREADY-RESOLVED (Week 1/2) / EXTERNAL-DEPENDENCY (future Weeks 3–14/16 build) | none now | future compiler could be built before Seams 3/4 settle | `course_foundry` | `course_foundry` (external repo) | none needed now | sequence future compiler work after Seams 3/4 | Prompt 137 (course_foundry, merged) | §4 Seam 8 |
| 9 | Reasoning Odyssey/Quest/Gate/World Bible vocabulary | HIGH | `docs/grading-model.md:23` ("Reasoning Odyssey gate"), `planning/fall-2026-weekly-architecture.md:41-64` (World Bible optional) | `sidecar/prompts/314_*.md` (Decision Gate settled); Prompt 305 unresolved-questions list (World Bible open) | DECIDED (ontology simplification) / OPEN (World Bible contract) | READY-MECHANICAL (rename) / BLOCKED-DESIGN (World Bible) | HIGH if left multi-named | HIGH — collision classes documented in Prompt 305 | `docs/grading-model.md`, `planning/fall-2026-weekly-architecture.md`, all weekly assignment templates | none | apply Decision Gate rename, no weight change | World Bible required/optional, cadence, cross-course carry-forward | Prompt 305 (merged), 309 (in progress), 314 (unexecuted) | §4 Seam 9 |
| 10 | Shared AI Fluency/Professional Minds/local-AI ownership | LOW | `docs/grading-model.md:13-15` (references shared content by name) | `sidecar/reports/306_*.md` (three-owner model) | DECIDED | ALREADY-RESOLVED (no duplication) / AMBIGUOUS (one-directional `professional_minds` pointer) | none found | none found | none | `ai_fluency`, `professional_minds`, `local_ai_lab_setup`, `windows_classroom` | none needed | none for DSCT | Prompt 306 (merged) | §4 Seam 10 |

No known seam disappeared silently; all ten received an evidence-backed disposition above.

## 6. Dependency graph / table

| Seam / decision | Depends on | Status of dependency |
|---|---|---|
| Seam 1 (Pair Reasoning naming) | Prompt 304 | ACCEPTED, merged to `main` |
| Seam 1 (Pair Reasoning contract/non-duplication) | Prompt 311 | EXECUTED on unmerged branch `worker/prompt311-pair-reasoning@38ebcca`; awaiting Foreman merge |
| Seam 9 (DSCT vocabulary/ontology naming) | Prompt 305 | ACCEPTED, merged to `main` (evidence only, no doctrine chosen) |
| Seam 9 (Decision Gate rename applied to source) | Prompt 314 | Prompt authored, unexecuted (`worker/prompt314-decision-gate` == `main`) |
| Seam 2/7 (Week 2 shared ownership/reuse) | Prompt 306 | ACCEPTED, merged to `main` |
| Seam 2 (Week 3 toolchain evidence) | Prompt 307 | ACCEPTED, merged to `main` |
| Seam 2 (Week 3 pinned-container implementation) | Prompt 316, which depends on Prompt 307 | Prompt authored, unexecuted; depends on already-merged 307 evidence |
| Seam 3 (Week 4–14 resource evidence) | Prompt 308 | ACCEPTED, merged to `main` |
| Seam 9 (World Bible lineage / cross-course provenance) | Prompt 309 | IN PROGRESS (uncommitted work observed in a live worktree on `worker/prompt309-world-bible`) |
| Seam 3 (eleven-week core-spine choice) | Jeremy + ChatGPT design decision, informed by Prompt 308 evidence and Prompt 313's stated direction | OPEN — Prompt 313 states the direction but has not executed the topic-map/spine edit |
| Seam 4 (grading naming + checkpoint/revision/drop mechanics) | Prompts 314 (naming), 315 (checkpoint tiering), 317 (revision/late), 318 (drop-lowest) | All authored, none executed |
| Seam 4/9 (grading category naming applied to Course Foundry) | Seam 8 (Course Foundry Week 3–14/16 build) | Not yet started — should wait for Seams 3 and 4 |
| Seam 8 (Course Foundry/Savnac reconciliation) | Seams 1, 3, 4, 9 all being frozen first | Only Weeks 1–2 are currently wired; later weeks intentionally not yet built |

This is a dependency map only; it does not authorize or schedule execution of any listed prompt.

## 7. Textbook/ZyBooks leakage audit

Search commands:

```
rg -n -i 'zybooks|required text|textbook' planning/ docs/ assignments/ week-01 week-02 week-16
```

| Hit | Classification | Reason |
|---|---|---|
| `planning/fall-2026-course-design.md:4-13,84-99` | source-mapping reference only | Explicitly states no required textbook; frames ZyBooks as historical mapping input |
| `planning/fall-2026-topic-map.md:1-8` | source-mapping reference only | "RECONCILED 2026-08-15... retained only as source provenance" |
| `planning/fall-2026-topic-map.md` (per-row "Historical ZyBooks family" column) | source-mapping reference only | Column explicitly labeled historical/provenance, used to justify catalog coverage, not assigned reading |
| `week-01/help-tools-status.md:24` | current operational requirement — but stated as a **negative** requirement | "No formal DSCT topic reading or ZyBooks work" is assigned in Week 1 — confirms absence, not presence, of a ZyBooks requirement |
| `docs/curriculum/course-sequence.md:18` | historical/provenance | Narrates 2021–2026 course evolution |
| `docs/reports/curriculum-history-synthesis.md:17` | historical/provenance | Narrates 2021–2026 course evolution |
| `planning/week-01-source-map.md:30-31` | source-mapping reference only | "No formal DSCT topic instruction or textbook reading is assigned in Week 1" |
| `planning/zybooks-section-decisions.csv` (file itself) | historical/provenance | KEEP/OPTIONAL/UNUSED decisions retained as source-mapping input per Prompt 302 |

**No current operational textbook/ZyBooks requirement was found.** This seam
is confirmed clean; historical evidence was not deleted or altered.

## 8. Week 16 GREEN preservation evidence

- DSCT `main` commit: `2ec8ea82b822a96d6bec987bb0306e51ce51376c`; `planning/fall-2026-spine.md:25`
  lists Week 16 status as `VALIDATED`.
- Report: `sidecar/reports/week16_farkle_ml_postmortem.md` — "Status: GREEN —
  AUTHORED, SYNCHRONIZED, AND VALIDATED AGAINST CANONICAL SHARED CORE."
- Validation receipt: `sidecar/runs/week16_farkle_validation_20260816T211906Z.md`
  — `status: GREEN`; shared commit `d3a1ed379a652731b0b6237c33b4fe42c518ac9e`;
  consumer commit `bab5ef89fa08e73b88bcdabd736600b58c45ec13`; bundle evidence
  `week-16/fallback/quick_v1_results.csv` (3 rows); CPU-only, no GPU/cloud/paid
  dependency.
- Key artifact paths: `planning/week-16.md`, `week-16/README.md`,
  `week-16/student/farkle-evidence-lab.md`,
  `assignments/week-16-farkle-evidence-receipt.md`, `week-16/instructor/guide.md`,
  `lessons/week-16-farkle-evidence.py`, `scripts/validate_week16_farkle.py`,
  `week-16/fallback/quick_v1_results.csv`, `lessons/vendor/farkle_ml/_SHARED_PROVENANCE.json`.
- Course Foundry/deployment dependency: **none currently wired** —
  `course_foundry@11a2a2c` only builds Week 1/2; Week 16 has no compiler
  integration yet, so no downstream system currently depends on or could
  silently overwrite this package.
- Legitimate future integration without rebuilding: Seam 3 (spine week-count
  decision) may reference Week 16 as the synthesis endpoint; Seam 4/9
  (Decision Gate rename) may relabel its grading category wrapper without
  touching authored content, since the postmortem confirms "No new grading
  category was invented."
- **Superseded-artifact caution:** `sidecar/reports/week16_farkle_ml_current_state.md`
  (same date, earlier in the campaign) says Week 16 is "NOT YET AUTHORED" —
  this is stale within its own report set and must be read as historical
  process evidence, not current status. It was not deleted or edited by this
  audit; it remains as provenance of the campaign's sequence.

## 9. Historical/incoming branch audit

| Branch | Commit | Unique content vs. `main` | Classification | Merge/cherry-pick risk |
|---|---|---|---|---|
| `origin/agent/prompt303-dsct-week2` | `85ea3a2cf446d2168d1d8210e297bf067389d51c` | `week-02/` student/instructor container/repeatability package, container example, repeatability receipt, source maps, runtime receipts | STALE / SUPERSEDED (per Prompt 306) — container/repeatability runtime superseded by shared `windows_classroom`/`local_ai_lab_setup` path | HIGH if blind-merged — would reintroduce a second Week 2 runtime alongside the shared canonical one; salvage only the evidence-oriented inventory/receipts |
| `origin/agent/prompt305-dsct-assessment` | `e209a63d5f1c3021aae38f4d9d7831bb2122ae8c` | Week 2 readiness assessment contract, evidence-quality fixtures | ADAPT FOR DSCT (per Prompt 306) — decision-dependent | MEDIUM — fixtures encode useful boundary cases but not final grading/reflection semantics; do not merge as-is |
| `worker/prompt311-pair-reasoning` | `38ebcca` | Executed Prompt 311 (Pair Reasoning contract rewrite + report) | potentially SALVAGEABLE / ready-to-merge (executed work, not stale) | LOW — this is forward-progress work, not archaeology; normal Foreman-acceptance merge, no special risk beyond standard review |
| `worker/prompt309-world-bible` | tip == `main`, but a **separate live worktree** is currently checked out on this branch with uncommitted work | unknown — in progress | DECISION-DEPENDENT / IN PROGRESS | do not touch; another job is actively using it |
| `worker/prompt312-317`, `golem/dsct-305-assessment-contract` | all == `main` tip | none yet | not yet executed | none — nothing to merge |

No branch was merged, rebased, cherry-picked, or deleted by this audit.

## 10. Course Foundry/downstream assumption audit

- `course_foundry@11a2a2c742b0b1a4f33494c04c2cb0a9f964b981`,
  `course_foundry/course_foundry/dsct_desired_course.py` (363 lines) and
  `course_foundry/course_foundry/dsct_savnac.py` (164 lines) are the only DSCT
  compiler/operator surfaces. They build/target **Week 1 and Week 2 only**.
- `grep -n -i "pair programming\|A3\|A4\|A7\|week 3\|week3\|topic.*week\|eleven\|twelve"` across both files: **zero hits** — no stale Pair Programming
  name, A-label, or topic-week-count assumption currently exists in the
  compiler.
- `WEEK_2_TITLE` and the Week 2 shared-object loader (`_week_2_shared_objects()`,
  reading `local_ai_lab_setup`'s `curriculum/week2_module_manifest.yml` with
  an explicit "sequence changed; review before deployment" staleness guard)
  are already aligned with the current Week 2 identity and the shared
  ownership model documented in Prompt 306.
- `course_foundry/reports/137_dsct_savnac_deployment_reconciliation.md`
  (`course_foundry@2e5bd3955ec3b8c152d5c88f0f8b2357fcd58e58`) documents that a
  prior stale `tuesday/`/`thursday/` Week 2 path assumption was already
  corrected to match DSCT's current flat `week-02/student/*.md` layout, with
  the 40-point rubric cross-checked against `docs/grading-model.md`.
  This is compiler-side evidence that Course Foundry has previously been
  reconciled against DSCT source changes, not evidence of a current stale
  dependency.
- **No dependency was found requiring a Course Foundry edit today.** The one
  forward-looking risk is Seam 8 in §4/§5: if a Week 3–14 or Week 16 Course
  Foundry build is authored before Seams 3 (eleven/twelve-week count) and 4/9
  (Decision Gate naming) are settled, that new compiler code would itself
  become instantly stale. No compiler/deployment code was edited by this
  audit.

## 11. High-impact unresolved seams

1. **Seam 3 — twelve vs. eleven formal topic weeks (BLOCKED-DESIGN, HIGH).**
   `planning/fall-2026-spine.md:31` and `planning/fall-2026-topic-map.md`
   still say "exactly twelve" (Weeks 3–14); `sidecar/prompts/313_*.md`
   already asserts "eleven formal DSCT core weeks" (Weeks 4–14) as direction
   but has not executed the source edit. This blocks any Course Foundry
   Week 3–14 build and any final topic-map authoring.
2. **Seam 9 — Reasoning Odyssey/Decision Gate naming and World Bible contract
   (mixed READY-MECHANICAL/BLOCKED-DESIGN, HIGH).** `docs/grading-model.md`
   still says "Reasoning Odyssey gate" while Prompt 314 has already settled
   "Decision Gate" as the sole student-facing weekly name; World Bible
   required/optional status remains genuinely open per Prompt 305's own
   question list.
3. **Seam 4 — grading naming + checkpoint/drop-lowest mechanics (mixed, HIGH).**
   `docs/grading-model.md:81` itself names checkpoint weeks and drop-lowest
   behavior as open "deployment questions"; Prompts 315/318 are authored but
   unexecuted.
4. **Seam 2 — Week 3 container/LaTeX implementation (READY-MECHANICAL-pending-authoring,
   HIGH once built).** No committed Week 3 toolchain source exists yet;
   Prompt 316's pinned-container direction is settled but the concrete
   image/engine is not chosen or validated (Prompt 307 proved only a host
   baseline).

## 12. Ready-mechanical seams

- **Seam 1 residual:** merge already-executed `worker/prompt311-pair-reasoning@38ebcca`
  to `main` — no new authoring required, just Foreman acceptance.
- **Seam 9 naming:** once Prompt 314 executes, its rename ("Reasoning Odyssey
  gate" → "Decision Gate") is a pure rename against a settled decision — the
  14-row grading arithmetic in `docs/grading-model.md` does not change.
- **Seam 4 revision/late-policy language:** Prompt 317's policy is fully
  settled (continuous 1%/24h, highest-score-kept, existing `course_foundry`
  late-work adapter already implements the rate) — applying its language to
  `docs/grading-model.md` is mechanical once executed.

Each is "safe to repair later" specifically because the underlying decision
is already settled in a numbered, authored prompt (311/314/317) and the
current source's only defect is that the edit has not yet been applied —
none of these require new judgment calls beyond what those prompts already
state.

## 13. Explicit Jeremy + ChatGPT decisions still blocking repair

1. Whether Week 3 remains a twelfth formal topic bundle (alongside its
   toolchain role) or becomes toolchain-only, collapsing the topic map to
   eleven bundles (Weeks 4–14) — blocks Seam 3, and downstream, any Course
   Foundry Week 3–14 build.
2. World Bible's exact contract: required vs. optional, submission shape
   (container vs. separate artifact vs. record), and cross-course
   carry-forward — blocks the non-naming half of Seam 9.
3. Exact checkpoint weeks and what distinguishes a checkpoint from an
   ordinary Decision Gate (Prompt 315's job) — blocks the checkpoint half of
   Seam 4.
4. Drop-lowest count/eligibility parameters (Prompt 318's job) — blocks the
   drop-lowest half of Seam 4.
5. Final container base image and TeX/build engine for Week 3 (Prompt 316's
   remaining job, after its direction is already settled) — blocks Seam 2's
   concrete implementation.

## 14. Verification commands/results

```
git rev-parse HEAD                     # 2ec8ea82b822a96d6bec987bb0306e51ce51376c
git diff main origin/main --stat       # empty — main == origin/main at start
git branch -a                          # branch inventory in §2
git for-each-ref refs/remotes/origin/  # remote inventory in §2
git log worker/prompt311-pair-reasoning -3 --oneline   # confirmed 38ebcca ahead of main
git diff main worker/prompt311-pair-reasoning --stat   # 2 files changed (assignments/pair-reasoning-report.md, sidecar/reports/311_pair_reasoning_contract.md)
git log golem/dsct-305-assessment-contract -1 --format='%H %s'   # == main tip
git log worker/prompt312..317 -1 --format='%H %s'      # all == main tip (checked individually)
rg -n -i 'pair programming|paired-programming' assignments docs planning -g '!docs/curriculum/**' -g '!docs/philosophy/**' -g '!docs/reports/**'   # 0 current-operational hits (Seam 1)
rg -n -i 'zybooks|required text|textbook' planning/ docs/ assignments/ week-01 week-02 week-16   # results tabulated in §7
grep -n -i "pair programming|A3|A4|A7|week 3|week3|topic.*week|eleven|twelve" course_foundry/dsct_desired_course.py course_foundry/dsct_savnac.py   # 0 hits, in course_foundry@11a2a2c (Seam 8)
grep -ril -i "discrete_structures|dsct" professional_minds@af54438, ai_fluency@022262c   # results tabulated in §10 Seam 10
```

Write-scope audit (this worktree, `worker/prompt310-seam-audit`):

```
git status --short --branch    # clean at start; this report is the only intended change
git diff --check               # to be run again immediately before commit
git diff --name-only           # to be run again immediately before commit
```

No course source, external repository, branch history, or JTT file was
modified by this audit. The only intended write is this report.
