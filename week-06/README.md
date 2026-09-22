# Week 6 — Algorithms, Correctness & Growth

**Tuesday, September 22 and Thursday, September 24, 2026**
COMSC-2043-1420 · 12:30–1:45 PM · Stafford 259

## Purpose and targets

An algorithm is not established by a few successful examples. We describe a
procedure precisely, trace it, look for invariants and edge cases, and compare
how its work grows as inputs grow.

By the end of the week, you can state an algorithm's input/output contract,
trace it, give a correctness reason or counterexample, and distinguish a
small observed result from a general claim about efficiency.

**Bring forward:** precise definitions from Week 4 and representation/boundary
checks from Week 5.

## This week's evidence

- Tuesday: retain the trace and test table in `student/tuesday-activity.md` as
  your technical presentation/demo evidence receipt.
- Thursday: publicly defend a trace, test, or correctness claim; submit the
  established [Show & Tell report](../assignments/show-and-tell-artifact.md).
- Submit one individual [Decision Gate](student/decision-gate.md). This is an
  ordinary Decision Gate, not a checkpoint.

No submission time is invented in this source package; use the published
course channel.

## AI fluency check

AI commonly produces code or pseudocode that works on friendly examples but
fails an edge case, changes an input contract, or states a complexity claim
without a counting argument. Ask: *what invariant or test distinguishes this
procedure from a lucky output?*

## Source provenance

Adapted from `planning/fall-2026-topic-map.md`,
`planning/fall-2026-weekly-architecture.md`, and `lessons/04-algorithms.md`.
The reasoning, Show & Tell, and grading contracts are local reusable sources:
`assignments/weekly-problem-solving-writeup.md`,
`assignments/show-and-tell-artifact.md`, and `docs/grading-model.md`.


## Present this week

Start with [`instructor/PRESENTATION_RUNBOOK.md`](instructor/PRESENTATION_RUNBOOK.md).
It is the authoritative, sequential classroom path: what to open or run, what
to say, what to ask, the intended reveal, and where to go next. The supporting
pages remain in [`websites/`](websites/README.md) and are numbered in teaching
order. They are self-contained and may be opened directly from local disk.

The sequence moves from Big-O growth and recursive Fibonacci through the
measured Bubble Sort page, the Bubble-versus-Merge reveal, the live runtime
race, and the CPU parallelism plot twist. Host-specific timings are labelled
as measurements rather than universal facts.

Before class, run:

```bash
bash week-06/scripts/13_preclass_check.sh
```


## Hanna implementation mission

The bounded Codex mission for the parallelism plot twist is:

- `instructor/HANNA_PARALLELISM_SHOWDOWN.md`

Launch it through the Foreman Interface Hanna fire-and-forget control plane:

```bash
bash week-06/scripts/11_hanna_parallelism_showdown.sh go
```

Useful detached controls:

```bash
bash week-06/scripts/11_hanna_parallelism_showdown.sh status
bash week-06/scripts/11_hanna_parallelism_showdown.sh tail
bash week-06/scripts/11_hanna_parallelism_showdown.sh go-baby-go
```

The mission authorizes Hanna to inspect, benchmark, repair, validate, commit, and
push the bounded `week-06/**` work. A genuine credential, destructive-system,
driver, purchase, physical-action, or scope-expansion decision remains a human
gate.
