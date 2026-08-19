# Job 321 — Luna preflight

## Verdict basis

This is a read-only preflight. No SWOSU production Canvas mutation was attempted. Three bounded Golem dispatches (broad current-truth audit, repair, and a smaller week-source audit) failed to produce their required evidence package; the Foreman therefore used only independently observed repository facts below and did not infer readiness from historical reports.

## SHA set

| Component | SHA / state | Evidence |
|---|---|---|
| DSCT working `main` | `a0f5b09e656ea5d2d32a91e15e732c65d2e91e5a` | `git rev-parse HEAD` |
| DSCT `origin/main` | `e0085d499826e0ec848d233defa31543141f52eb` | `git rev-parse origin/main` |
| DSCT relation | local `main` ahead by one local prompt-framing commit | `git status --short --branch` |
| Course Foundry | `9ca412b4e9f75dd46fe183626b52309f3107bfcc` | `git -C ../course_foundry rev-parse HEAD` |
| Course Foundry state | materially dirty with tracked runtime/config changes and untracked receipts, raw logs, reports, and queue state | `git -C ../course_foundry status --short --branch` |

The shared Course Foundry checkout was not cleaned, reset, stashed, normalized, or mutated. No isolated exact-SHA Course Foundry deployment worktree was created because the source preflight failed first.

## Current week-by-week source classification

The authoritative spine is `planning/fall-2026-spine.md`; its status is explicitly `CONTRACTED_NOT_AUTHORED` unless marked otherwise. The following classification uses actual student-facing paths, not spine labels.

| Week | Classification | Current evidence |
|---:|---|---|
| 1 | SOURCE READY | `week-01/` contains student activities, exit checks, reasoning method, AI expectation, help/tools status, and instructor run-of-show files; spine marks the package landed. |
| 2 | PARTIAL | `week-02/student/` and instructor run-of-show files exist, including evidence assignment/rubric, but the spine marks the AI-lab package `CONTRACTED_NOT_AUTHORED`; a complete deployable package is not proven. |
| 3 | SOURCE READY | `week-03/container/`, student skill ladder, instructor notes, and pinned-container evidence exist; it is a validated runway/toolchain rather than a formal topic chassis. |
| 4 | STRUCTURE ONLY | Spine names Logic, Claims & Proof, but no `week-04/` student package exists; `lessons/02-logic-proofs-and-sequences.md` is legacy lesson material, not a dated week package. |
| 5 | STRUCTURE ONLY | Spine names Sets, Functions & Sequences; no `week-05/` student package exists. |
| 6 | STRUCTURE ONLY | Spine names Algorithms, Correctness & Growth; no `week-06/` student package exists. |
| 7 | STRUCTURE ONLY | Spine names Integer Properties & Cryptography; no `week-07/` student package exists. |
| 8 | STRUCTURE ONLY | Spine names Induction, Recursion & Recurrences; no `week-08/` student package exists. |
| 9 | STRUCTURE ONLY | Spine names Counting; no `week-09/` student package exists; Thursday is explicitly no class. |
| 10 | STRUCTURE ONLY | Spine names Probability, Uncertainty & Evidence; no `week-10/` student package exists. |
| 11 | STRUCTURE ONLY | Spine names Relations/Orders/Matrices/Digraphs; no `week-11/` student package exists. |
| 12 | STRUCTURE ONLY | Spine names Graphs & Network Reasoning; no `week-12/` student package exists. |
| 13 | STRUCTURE ONLY | Spine names Trees, Search & Decision Structures; no `week-13/` student package exists. |
| 14 | STRUCTURE ONLY | Spine names Boolean/Circuits/Finite-State Machines; no `week-14/` student package exists. |
| 15 | STRUCTURE ONLY | Spine reserves Thanksgiving/travel asynchronous integration, but no `week-15/` package or declared assignment exists. |
| 16 | SOURCE READY | `week-16/`, `planning/week-16.md`, Farkle/ML planning, assignments, validator, and validation receipts exist; spine marks it validated. |
| 17 | STRUCTURE ONLY | Spine names final reflection during finals week, but no `week-17/` package exists and grading/final format remains open. |

Only four week directories exist in the current tree (`week-01`, `week-02`, `week-03`, `week-16`), plus assessment fixtures. Legacy `lessons/01`–`14` files and the planning spine do not constitute student-facing weekly source.

## Grading, dates, and behavior

Current grading evidence is distributed among `docs/grading-model.md`, `assignments/`, `templates/`, `planning/fall-2026-spine.md`, and accepted policy reports 317–318. The repository contains reusable weekly write-up, pair-reasoning, show-and-tell, project/final-reflection, programming-exam, career-artifact, and Week 16 receipt materials, but no single deterministic deployment model proving all assignment groups, weights, drop rules, dated assignment instances, and complete Week 1–17 module coverage. Week 15 is reserved asynchronous travel/buffer behavior; Week 16 has validated Farkle/ML source; Week 17's final format and weight remain open per the spine. Therefore the required grading/date validation and semantic diff cannot truthfully pass.

## Deployment and live-target state

The DSCT repository has `sidecar/scripts/320_launch_cleo_dsct_shipping.sh` and historical deployment reports, but no current DSCT-side complete desired course model was independently verified in this shift. The only direct production-target hint found in current launcher material is historical course `74035`; no fresh read-only Canvas identity/module/assignment readback was completed. The Canvas environment file exists locally, but its secrets were not read or exposed. Production remains untouched.

No Savnac reconcile was attempted. The dirty shared Course Foundry checkout and absent complete desired model mean the dry-run, zero-delta proof, post-write readback, and production semantic diff requirements were not met.

## Useful current evidence and yellows

- Accepted Week 1, Week 3, and Week 16 evidence is present in the paths named above and can support later bounded implementation.
- Remote worker branches contain historical prompt/report work, but no worker receipt from this shift was produced and no stale branch was promoted.
- The local DSCT prompt-framing commit is not yet on `origin/main`; it is intentionally preserved for the next promotion checkpoint.
- Production target identity, production module state, assignment state, enrollment/submission facts, and a final semantic diff remain unverified.

## Exact remaining action

Author and validate the missing student-facing Week 4–15 and Week 17 packages, resolve the Week 2 partial package and complete grading/final-format contract, then generate a deterministic desired-course model in an isolated exact-SHA Course Foundry worktree. Only after that should a fresh read-only production identity readback and semantic diff be attempted.

**Verdict:** `BLOCKED`
BLOCKED: current DSCT source is not a complete teachable Weeks 1–17 course; Weeks 4–15 and Week 17 remain structure-only or missing, so the required desired-course and production semantic diff cannot be proven.
