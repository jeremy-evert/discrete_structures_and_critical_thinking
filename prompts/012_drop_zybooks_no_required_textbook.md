# Prompt 012 — Drop ZyBooks, no required textbook (DSCT)

## Status

READY. Jeremy, 2026-08-15 (live chat, not yet a written `questions/` card):
"we are not going to use zybooks for cs 1, cs 2, or dcst." CS1 already
walked this back on 2026-08-12 (`computer_science_1` commit `6ee41dd`,
"Pre-Savnac source reconciliation: no required textbook... walks back both
the 2026-07-27 Deitel-primary and 2026-08-11 ZyBooks-first decisions"). This
prompt applies the same reversal to DSCT. Computer Architecture is
explicitly **not** part of this decision — Jeremy said that course is still
an open question he's deciding separately today. Do not touch
`computer_architecture`.

**Read `planning/fall-2026-spine.md`, `fall-2026-weekly-architecture.md`,
and `fall-2026-topic-map.md` first — Jeremy has been actively rebuilding
DSCT's own spine concurrently this same evening (2026-08-15). Do not
conflict with or revert any of that live work.** This prompt only touches
the textbook/ZyBooks framing, not the weekly topic spine.

## Mission

Reconcile DSCT's source so it no longer presents ZyBooks as DSCT's
textbook or organizing spine.

## Scope

1. `course_metadata.yaml`'s `textbook:` block currently carries a live
   `zybook_identifier`/`zybook_url` (`SWOSUCOMSC2043EvertFall2026`) as the
   operational adoption record, and explicitly states "Fall 2026 strategy
   (Jeremy, 2026-08-11): ZyBooks-first for all four [courses]" — that
   strategy is superseded as of 2026-08-15 for CS1/CS2/DSCT. Reconcile the
   way CS1's `6ee41dd` did: state plainly DSCT has no required
   textbook/external course for Fall 2026, and preserve the ZyBooks
   identifier/URL as **historical provenance** (read
   `computer_science_1/course_metadata.yaml` for the exact shape to mirror)
   rather than erasing that Jeremy did once supply it.
2. Grep the rest of the repo (`docs/`, `planning/`, `lessons/`,
   `assignments/`) for "ZyBooks"/"zybook" and reconcile only current,
   student-facing or operative-doctrine references that assume ZyBooks is
   DSCT's textbook/spine. Leave historical/provenance/dated-decision notes
   alone (mark superseded in place if genuinely load-bearing context, do
   not delete history). **Do not touch the live spine/weekly-architecture
   rebuild files' actual week/topic content** — only their textbook
   framing, if any exists there.
3. Do not touch grading weights or assignment structure. This is a
   textbook-status change only.
4. Do not touch `computer_architecture` or any other repo.

## Deliverable

Write `reports/012_drop_zybooks_no_required_textbook.md`: every file
changed and why, every ZyBooks hit found and whether changed/left (with
reason), and explicit confirmation that no grading/structural/spine content
was touched.
