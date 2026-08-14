# DSCT watcher handoff contract (definition only)

Status: EXTERNAL_WATCHER_DEPENDENCY - IN FLIGHT ELSEWHERE. This document does not implement detection, polling, Harbor ingestion, orchestration, or writeback.

## Boundary packet

- Watcher obtains: course id, assignment id, pseudonymous user id, attempt, submission text, source rubric revision/hash, approved material-bundle manifest, and a stable feedback version.
- Marker receives: rubric dictionary with named criteria/descriptions/points, plain submission text, attempt, and an immutable-input map for receipt hashes.
- Marker returns: AssessmentDraft with criterion points, evidence, notes, overall suggested score, feedback text, state (ready|provisional|escalate), and state reason. It is never a final grade.
- Coach receives: the draft plus explicit CourseMaterial(file, section_or_topic, content) objects. It must not retrieve materials itself.
- Coach returns: CoachingNote(item_id, cited_materials, next_steps, note_text, state), with state=escalate when material or grounding is inadequate.
- Dispatch receives: course, assignment, pseudonymous-or-raw user, attempt, exact comment_text, feedback version, and alias table when needed.
- Safety preserved: synthetic/de-identified policy, rubric/material hashes, assessment state, escalation reasons, human-review requirement, course allowlist, and no-grade/comments-only policy.
- Never infer: final grade, missing rubric criteria, course policy/weights, source sufficiency, student identity from a pseudonym, or permission to post.
- Idempotency: Dispatch marker is the stable tuple (course, assignment, resolved user, attempt, feedback_version).
- Escalation: preserve the draft/note and reason; do not post automated feedback as resolved. Route to human review or the watcher explicit hold state.

## Dispatch safety

build_writeback_report is the permitted audit seam: it builds a GET-backed, non-writing report. execute_writeback is outside this run and requires live=True; no call was made. Dispatch writes comments only and never posted_grade. Harbor course allowlist remains the lower transport guard.

