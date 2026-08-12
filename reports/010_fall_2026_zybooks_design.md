# Prompt 010 — Fall 2026 ZyBooks Design Report (DSCT)

## Result

Designed a Fall 2026 blueprint for COMSC-2043, Discrete Structures and
Critical Thinking.  The design preserves the repository’s topic-first,
critical-thinking, problem-writeup, pair/show-and-tell, career-evidence, and
synthesis strands.  It does not deploy Canvas/Savnac, change ZyBooks, or copy
licensed ZyBooks page content.

## Evidence used

- `planning/fall-2026-spine.md` for the actual T/Th Fall 2026 calendar and
  17-week allocation;
- `docs/curriculum/course-sequence.md`, lesson skeletons, assignments,
  templates, and history synthesis for canonical course intent;
- `course_metadata.yaml` for course/requisite facts and current zyBook ID;
- durable manifest
  `/mnt/brandy_nvme/jevert/durable/zybooks_captures/SWOSUCOMSC2043EvertFall2026/course_manifest.json`.

The durable manifest is validated and contains 126 discovered sections. The
decision CSV contains exactly 126 rows: 75 KEEP, 46 OPTIONAL, and 5 UNUSED.
The required path is 59.5% of the captured corpus. Every KEEP row maps to a
week/topic; OPTIONAL material is a deliberately gated reference/remediation
menu rather than hidden required reading.

## Design changes and observations

The original spine had one topic skeleton per teaching week but no daily split,
assignment tie-in, textbook selection, or student-facing module blueprint.
The new design supplies those planning elements without inventing due dates or
grading weights. It avoids a section-by-section textbook march by keeping the
work anchored in argument, model choice, implementation/simulation, checking,
and explanation. The greatest non-textbook needs are proof-feedback examples,
context-rich model prompts, coding/simulation tooling, and the collaboration
and reflection evidence trail.

## Unresolved items

Jeremy still needs to set grading weights/final format, decide whether career
evidence is assessed or advisory, choose the synthesis-project/tooling details,
and supply source-backed due dates. The vendor should answer the recorded lean
configuration price question before any price claim or configuration change.

## Validation

- Parsed the durable manifest and verified 126 rows in the CSV.
- Verified KEEP + OPTIONAL + UNUSED = 126 and that every KEEP row has a target.
- Confirmed the artifacts contain identifiers, titles, derived classifications,
  and planning notes only—not licensed section bodies.
- `git diff --check` and repository make targets are recorded after final
  validation below.

## Next recommended work

Use the approved design to create instructor materials and explicit module
objects only after the cross-course synthesis and Jeremy’s targeted decisions.
