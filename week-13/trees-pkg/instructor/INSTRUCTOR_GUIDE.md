# Week 13 instructor guide — Trees, Search & Decision Structures

**Meetings:** Tuesday, November 10 and Thursday, November 12, 2026
**Mode:** Tuesday model/trace/audit; Thursday Pair Reasoning plus the ordinary
Decision Gate.

## Teaching spine

Begin with a concrete choice between two pictures: a folder/org-chart view
answers “what is under this?” while a work-order view answers “what must happen
before this?” Define every new term when it first appears. Keep the class loop
visible: **Predict → Run → Explain**. Students who find graphs, testing, or
abstraction difficult should always see the small concrete case before the
general word.

The synthetic dependency graph is:

```text
project -> plan       project -> build
plan -> requirements  plan -> design
build -> tests        build -> docs
requirements -> tests
```

The directory-style tree places `requirements` under `plan` and `tests` under
`build`. Those six parent-child edges are containment edges. The graph has one
additional dependency: `requirements -> tests`. The answer key must stay in
this instructor guide; student pages ask students to perform the comparison.

## Tuesday run of show — 75 minutes

| Time | Move | Evidence to protect |
|---|---|---|
| 0:00–0:08 | Show the folder/work-order contrast and ask students to predict which relationships each picture can answer. | Students name edge meaning before drawing. |
| 0:08–0:18 | Introduce the seven synthetic vertices and exact directed edges. | Direction means “completed before”; no real data enters the example. |
| 0:18–0:30 | Build the directory-style tree with `project` at the root. Define parent, child, leaf, depth, and subtree. | Students distinguish containment from dependency. |
| 0:30–0:44 | Predict and trace preorder, postorder, and breadth-first with left-to-right child order. | Each trace visits all seven vertices once. |
| 0:44–0:55 | Show the cleaned decision tree. Explain that `yes` and `no` are edge labels, not nodes. | The eligible-plus-aid route is traced without inventing a condition. |
| 0:55–1:08 | Individual Tuesday activity: route labels, traces, language-access note, and five-part check. | Each student records a model limitation. |
| 1:08–1:15 | Collect one bounded conclusion and bridge to Thursday's pair audit. | A clean hierarchy is not treated as complete evidence. |

### Tuesday answer key

For the project tree, with children visited left to right:

```text
preorder:      project, plan, requirements, design, build, tests, docs
postorder:     requirements, design, plan, tests, docs, build, project
breadth-first: project, plan, build, requirements, design, tests, docs
```

The tree parent-child edge set contains:

```text
project -> plan, project -> build,
plan -> requirements, plan -> design,
build -> tests, build -> docs
```

The dropped graph edge is `requirements -> tests`. It is a dependency cross-link,
not a containment edge. A vertex search can still find `requirements` and
`tests`; that does not establish that all dependencies were preserved.

For the cleaned decision tree:

```text
preorder:      Start, eligible?, needs aid?, aid route, standard route, explain rule
postorder:     aid route, standard route, needs aid?, explain rule, eligible?, Start
breadth-first: Start, eligible?, needs aid?, explain rule, aid route, standard route
```

An eligible person who needs aid traces `Start -> eligible? -> needs aid? -> aid
route`. The intake note adds `aid route -> language-access review`; therefore the
displayed tree does not justify “everyone routed to aid can use the aid route
immediately.” Students may add a review node or state the limitation, but must
connect the choice to the note.

## Thursday run of show — 75 minutes

| Time | Move | Evidence to protect |
|---|---|---|
| 0:00–0:10 | Revisit one Tuesday bounded conclusion and ask what evidence could change it. | A claim is separated from its author. |
| 0:10–0:20 | Re-state Pair Reasoning: each person writes a starting position before talking. | No divided-labor substitute. |
| 0:20–0:45 | Pairs compare source relationships with the tree and seek discriminating evidence. | Trace, missing-node search, edge comparison, or counterexample. |
| 0:45–0:57 | Partners revise or defend and name a remaining limit. | Claim is no broader than evidence. |
| 0:57–1:10 | Each student assembles the Decision Gate and individual Pair Reasoning report. | Technical artifact and reasoning-under-challenge record remain distinct. |
| 1:10–1:15 | Exit: “What relationship did the hierarchy erase, and did it matter?” | Concrete relation plus consequence. |

## Facilitation and grading boundaries

Do not require coding, a particular diagramming tool, an external account, or
real sensitive data. If a student uses an AI tool, ask for the original
relationship list and the independent comparison that checked the proposed
tree. A generated picture is a proposal, not evidence.

The Decision Gate uses the five headings in the existing source. The Pair
Reasoning report is an individual account of starting position, strongest
challenge, evidence that mattered, change or survival, current position, and
what could change the student's mind. It is not a duplicate technical artifact.
Use the existing weekly rubric and report shape; do not create a new submission
category or a second tree assignment.

## Common slips and recovery moves

| Slip | Recovery question |
|---|---|
| Student treats `yes` or `no` as a vertex. | “What question owns that answer, and which edge carries it?” |
| Tree edges are called dependencies without stating why. | “Is this edge about work order or placement?” |
| Breadth-first is listed as a depth-first trace. | “Have you finished the current level before descending?” |
| The audit says all seven vertices were found, so the model is complete. | “Which exact edge set did you compare?” |
| A pair agrees and stops. | “What check could try to disprove the agreement?” |
