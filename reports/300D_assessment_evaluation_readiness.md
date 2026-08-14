# Prompt 300D — DSCT Assessment & Evaluation Readiness

## Executive assessment verdict

**PROMPT 300D RESULT: GO WITH YELLOWS.** Generic Marker -> Coach is real, schema-compatible, receipt-bearing, and safe for assessment drafts when inputs are clean. DSCT is not ready for trustworthy Week 2 automated evaluation: its five-part template exists, but there is no DSCT rubric adapter, offering-specific observable criteria, dated Week 2 artifact, or substantive approved material bundle. The future watcher remains external.

This audit did not implement a watcher, write to Savnac/Canvas, use real student data, or launch NRP.

## Prior evidence

300A established the repository set and clean handoff. 300B established Tuesday GO WITH YELLOWS, Week 2 NO-GO, semester source NO-GO, and conflicted coherence: the design is reasoning-centered but weekly implementation is under-authored. 300C established generic deployment plumbing is real but DSCT deployment is NO-GO because no DSCT DesiredCourse producer/registration exists. Those gaps do not prevent this narrower contract audit.

## Audited state and runtime

See the run receipt at runs/2026-08-14_prompt300D_assessment_evaluation_audit/receipts/repository_state.json. Audited SHAs: DSCT fb384c1, Marker 14925a2, Coach 0d01f7a, Dispatch 1bfdfb8, Harbor a5b3eb2, Synthetic Student Laboratory 54ef1a2, NRP launcher 0bf946a. All were clean after fast-forward refresh. Python 3.14.4 was available; pytest and ruff were unavailable, so documented test commands could not execute. Imports and the deterministic synthetic smoke did execute.

## DSCT rubric/evidence -> Marker

DSCT source artifacts are assignments/weekly-problem-solving-writeup.md and templates/weekly-rubric.md. They name Sources, Rules/Assumptions, Work, Check, and Summary, and the blueprint adds proof, counterexample, modeling, simulation, and AI-verification intent. This is representable by Marker’s generic rubric dictionary without inventing weights.

There is no deterministic DSCT adapter. Marker’s only Markdown adapter is the narrow CS1 Quick Check table adapter in marker/markdown_rubric.py; it must not parse DSCT by analogy. The smallest adapter would recognize the DSCT shape, preserve criterion text and grading notes, fail closed on ambiguity, and require caller-supplied points policy. Until then this seam is MISSING_DSCT_ADAPTER.

Descriptions are too broad to distinguish valid proof from fluent nonsense, a domain-valid counterexample from an irrelevant one, simulation output from a general conclusion, or disclosed/verified AI assistance from an unverified answer. These are DSCT AUTHORING GAPs, not generic Marker defects.

## Marker readiness and failure modes

Marker grade(rubric, submission_text) returns AssessmentDraft with criterion evidence/notes, suggested score, feedback, attempt, and ready|provisional|escalate. assess_with_receipt persists immutable input hashes and stages atomically. Assertion, draft-honesty, and plausibility gates only tighten toward escalation. The finite escalation ladder carries a HumanReviewPacket; its independent comprehension gate can inspect high-credit evidence against rubric wording.

Verdict: Marker engine GO; Marker DSCT safety coverage GO WITH YELLOWS. Mechanics are suitable for a draft, not a final grade. The comprehension gate is useful for credited-but-unsupported evidence but is not a proof checker. DSCT distinctions must be written into criteria and examples.

The full failure matrix is in derived/dsct_failure_mode_matrix.csv. Assertion-only evidence is partially covered; invalid proof, unstated assumptions, invalid counterexamples, simulation overclaims, and source-support truth need DSCT-specific criteria. Definition-conflicting AI explanations are partially covered only when exact definitions and verification instructions are supplied.

## Coach readiness and material grounding

Coach accepts Marker’s AssessmentDraft, explicit CourseMaterial objects, and returns CoachingNote with cited materials, next steps, text, and state. It does not retrieve materials, re-score, approve, or post. Empty material input escalates rather than inventing citations; note-honesty checks cited vocabulary.

Verdict: Coach engine GO; DSCT materials -> Coach NO-GO. Week 1 has transferable kickoff and reasoning templates, but 300B says there is no complete DSCT Week 2 assignment/material bundle. The logic/proof lesson is a short skeleton, not enough for grounded remediation. Missing substantive material is BLOCKED_BY_CONTENT.

The smallest stable future bundle is bounded objects containing source path or stable content id, section/topic, content, source revision/hash, and assignment scope. For proof remediation it should include the exact definition, valid proof pattern, counterexample exemplar, and checking/AI-verification guidance once authored.

## Marker -> Coach handoff

The boundary is already compatible: Coach consumes Marker per-criterion evidence and notes rather than raw submission. A weak criterion or escalated draft triggers coaching; a fully correct non-escalated draft does not. Verdict: GO WITH YELLOWS because compatibility is generic while DSCT material and criterion semantics are missing.

## Watcher / Dispatch contract

The compact contract is in derived/watcher_handoff_contract.md. The watcher must provide course/assignment/user-or-pseudonym/attempt, plain submission, rubric revision/hash, approved material manifest, and feedback version. It must preserve states, hashes, escalation reasons, human review, and never infer grades, policy, identity, source sufficiency, or posting authority.

Dispatch accepts exact comment_text, resolves pseudonyms through an alias table, embeds an idempotency marker over course/assignment/resolved user/attempt/version, requires live=True before PUT, and emits comments only—never posted_grade. Harbor’s course allowlist is the lower boundary. build_writeback_report is the safe non-writing seam; no execute function was called.

Verdict: Dispatch contract GO WITH YELLOWS for the generic interface. Automated Savnac watcher/orchestration is EXTERNAL_WATCHER_DEPENDENCY — IN FLIGHT ELSEWHERE and was not audited as implemented here.

## Synthetic smoke

A deterministic local synthetic-only smoke used a run-local five-part micro-rubric with neutral one-point mechanics and four cases: strong reasoning, unsupported assertion, invalid counterexample, and bad check. It exercised AssessmentDraft, Marker gates, CourseMaterial, and CoachingNote without Ollama or a remote backend. The strong case remained ready; weak cases reached Coach, whose intentionally inadequate fake grounding response escalated. This validates interface and fail-closed behavior, not grading accuracy or the full LLM path. Receipt: runs/2026-08-14_prompt300D_assessment_evaluation_audit/receipts/synthetic_smoke.json.

## Synthetic Student Laboratory

The lab can represent an observable behavior profile, effort dimensions, assignment, rubric, approved materials, local Ollama, and reproducible receipts; dry-run avoids model contact. It must not use protected traits or real students. DSCT is not configured because real Week 2 assignment/rubric/materials do not exist.

Once Week 2 is authored, use 3–5 cases spanning valid proof, assertion-only, invalid proof/counterexample, bad check, and AI-style definition conflict. Relevant axes are instruction attention, source consultation, planning, revision, persistence, depth, and AI reliance only as observable behavior. Measure evidence completeness, criterion-level agreement, escalation precision, grounded citation, remediation actionability, and unsupported-generalization detection, not raw score alone. “Deliciously wrong” reasoning is fluent prose violating a supplied definition/domain; expected labels require human review.

Verdict: NO-GO for DSCT-specific readiness, not a Tuesday blocker.

## NRP future scale path

NRP is SCALE_ONLY. Before scale, local evidence must include an authored Week 2 rubric/material contract, deterministic smoke receipts, a small local Ollama comparison, expected qualitative labels, and a reviewed watcher packet. A future container would package the synthetic lab, Marker/Coach clients, frozen manifests, model configuration, and payload emitting per-case raw/model/assessment/coaching receipts. Informative scale means multiple failure cases across a small profile/effort sample and an independent model comparison—not a large matrix before the contract is stable. NRP is not a Tuesday or Week 2 blocker because no automated grading is required for the first meeting and Week 2 is content-blocked.

## Seam verdict matrix

| Seam | Verdict | Timing / owner |
|---|---|---|
| DSCT rubric/evidence -> Marker | NO-GO | Week 2; DSCT authoring + explicit adapter |
| Marker generic engine | GO | No Tuesday blocker; Marker |
| Marker DSCT safety coverage | GO WITH YELLOWS | Week 1; DSCT rubric author |
| DSCT source -> Coach materials | NO-GO | Week 2; DSCT content owner |
| Coach generic engine | GO | No Tuesday blocker; Coach |
| Marker -> Coach schema | GO WITH YELLOWS | Week 1; caller preserves states |
| Coach/Marker -> watcher | GO WITH YELLOWS | Later; watcher effort |
| Dispatch generic contract | GO WITH YELLOWS | Later; Dispatch/Harbor |
| Automated watcher | EXTERNAL_WATCHER_DEPENDENCY | Later; external effort |
| Local synthetic acceptance | GO WITH YELLOWS | Week 1 after rubric shape |
| Synthetic Student Laboratory | NO-GO | Later; lab + DSCT inputs |
| NRP scale | SCALE_ONLY | Can wait; NRP launcher |

## Prioritization

### MUST BEFORE TUESDAY

No automated assessment work. Teach from bounded Week 1 material and make unresolved DSCT framing/transition explicit. This audit finds no Marker/Coach dependency that prevents the first meeting.

### SHOULD DURING WEEK 1

Reconcile Week 2 identity; author one real Week 2 assignment, rubric, proof/counterexample exemplars, exact definitions, checking and AI-verification expectations; specify the DSCT adapter and approved Coach bundle; run the 3–5-case deterministic/local battery. This is the conditional Week 2 assessment gate.

### CAN WAIT

Watcher implementation, Harbor ingestion, Dispatch live proving, later-week adapters, large synthetic matrices, NRP, and generalized evaluation research. The watcher is owned elsewhere; no duplicate task is filed.

## Smallest next actions

1. Resolve the Week 2 orientation-versus-logic/proof conflict.
2. Author the smallest real Week 2 artifact/rubric/material bundle with observable proof, domain, check, and AI-verification evidence.
3. Implement and test a fail-closed DSCT rubric adapter, preserving author text and inventing no points.
4. Re-run the local synthetic battery, then hand the frozen contract to the external watcher effort.

## Evidence appendix

Primary paths: DSCT assignments/weekly-problem-solving-writeup.md, templates/weekly-rubric.md, planning/fall-2026-course-design.md, planning/fall-2026-spine.md, lessons/02-logic-proofs-and-sequences.md; Marker marker/pipeline.py, assessment_receipt.py, gate modules, markdown_rubric.py, escalation_ladder.py; Coach coach/pipeline.py and note_honesty.py; Dispatch dispatch/writeback.py; Harbor package_pull.py and client.py; lab README.md, schemas.py, runner.py; NRP README.md and nrp_launch_job.py. Full matrices and receipts are under the canonical run directory.

