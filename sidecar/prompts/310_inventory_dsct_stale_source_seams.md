# Prompt 310 — Inventory stale DSCT source seams against the current design quarry

**Status:** FOREMAN-READY AUDIT CUT  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Scope:** inspect, classify, and report source conflicts; do not perform wholesale reconciliation

## Why this is Foreman-ready

The quarry already names several concrete source seams. We do not need a worker to decide whether they exist. We need a precise map of where they exist and what would be affected by later reconciliation.

Known seams include:

1. `Pair Programming` naming is stale against the new **Pair Reasoning** decision.
2. Current Week 2/3 calendar/source contract is stale against the newer **Week 2 Building Your AI Lab / Week 3 Containers + minimum-useful LaTeX** runway.
3. Current Weeks 3–14 map has twelve formal topics, while the newer Weeks 4–14 core has eleven slots.
4. Current grading model may contain useful weights but stale naming and unresolved due/revision/checkpoint mechanics.
5. Historical ZyBooks source files are provenance only and should not become operational requirements again.
6. Week 16 is already validated and should be integrated rather than rebuilt.
7. Old incoming Week 2/assessment branches are archaeological inputs, not blind merge targets.

The quarry also names repositories/files that later slicing should inspect, including:

- `planning/fall-2026-spine.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `planning/fall-2026-course-design.md`
- `docs/grading-model.md`
- assignments/rubrics using Pair Programming / A3-equivalent naming
- existing Reasoning Odyssey / World Bible surfaces
- Week 2 incoming branches
- Week 16 validated package
- Course Foundry DSCT compiler expectations
- shared AI Fluency / Professional Minds sources
- sibling/shared Week 2 and container sources.

Creating a precise dependency/seam map is mechanical. Choosing how to collapse twelve formal topics into eleven, defining the final artifact ontology, or deciding grading policy is not.

## Work

1. Inspect current DSCT `main` and relevant incoming branches/read-only sibling references named by the quarry.
2. Build a source-seam matrix with columns such as:
   - seam ID;
   - current path;
   - current statement/contract;
   - newer quarry direction it conflicts with;
   - whether the resolution is already decided or still pedagogical;
   - likely downstream files/systems affected;
   - safe mechanical action now, if any;
   - hard stop / decision owner.
3. Search for stale operational requirements such as required ZyBooks/textbook language that contradict current no-required-textbook direction.
4. Identify where Week 16 is already treated as GREEN/validated so future work does not accidentally rebuild it.
5. Inspect incoming branches enough to report unique useful content and divergence, but do not merge them.
6. Identify Course Foundry/compiler/Savnac assumptions that encode the older Week 2/3 or pair-activity grammar.
7. Produce a sidecar report that can serve as a dependency map for later prompt authoring.

## Hard stops

Do **not**:

- solve the eleven-week intellectual spine;
- decide the final Reasoning Odyssey / Quest / World Bible ontology;
- decide grading weights, due policy, revision, or checkpoints;
- blindly merge incoming branches;
- rebuild Week 16;
- bulk-edit all stale files merely because the seam is obvious;
- write Savnac/Canvas.

Prompt 304 separately owns the already-decided Pair Reasoning naming reconciliation. Avoid duplicating that work except where needed to map downstream dependencies.

## Acceptance

Complete when we have one trustworthy map of stale source truth and downstream dependencies, with each seam clearly marked as either already-mechanical or still requiring Jeremy + ChatGPT design judgment.