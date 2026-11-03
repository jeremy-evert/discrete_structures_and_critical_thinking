# Week 14 run of show

Both meetings use a 75-minute cadence. Keep the visible evidence on the board
or screen while students explain it in their own words.

## Tuesday — exhaust small cases

| Clock | Facilitator action | Student product |
|---|---|---|
| 0:00–0:08 | Show the proposed `F` to `B` simplification. Ask what would establish equivalence. Introduce predict → run → explain. | A prediction about the evidence needed. |
| 0:08–0:20 | Define the Boolean terms and fill every truth-table row. Mark the mismatch in red. | Four rows and the exact counterexample `P=False, Q=True`. |
| 0:20–0:28 | Run Prompt 01. Stop for definitions before code. | A plain-language claim and one predicted row. |
| 0:28–0:38 | Run Prompt 02. Compare its four outputs to the visible table. | One mismatch and no hidden row. |
| 0:38–0:45 | Run Prompt 03a on the correct `E`/`S` pair and false `F`/`B` pair. | Empty counterexample list for `E`/`S`; exact mapping for `F`/`B`. |
| 0:45–0:53 | Run Prompt 03b. Ask whether one witness proves every case. | Witness, non-tautology counterexample, tautology, and unsatisfiable result kept separate. |
| 0:53–1:02 | Define state, input, transition, start state, trace, and model limit. Trace `valid, timeout, valid`. | `Locked → Open → Locked → Open`. |
| 1:02–1:10 | Run Prompt 04 and then show the incomplete table for Prompt 05. | Unknown input fails visibly; missing pair is `("Open", "timeout")`. |
| 1:10–1:20 | Students choose a small defense artifact and test one row or trace. | Claim, evidence, and boundary. |
| 1:20–1:25 | Preview Thursday and read the exit sentence aloud. | A one-sentence limited conclusion. |

### Tuesday stop points

If the class is behind, stop after the four-row table and Prompt 03b, then
show the state trace and missing pair as instructor examples. If a generated
answer differs, use the committed reference code and narrate the recovery;
never edit the expected test to make a drifted answer appear correct.

## Thursday — defend a model and name its boundary

| Clock | Facilitator action | Student product |
|---|---|---|
| 0:00–0:10 | Establish the critique norm: challenge the evidence or assumption, never the person. | One testable challenge question. |
| 0:10–0:20 | Re-state the two artifact paths and check that each claim is inspectable. | Boolean: complete rows. State: named states/inputs/transitions, start, two traces, limit. |
| 0:20–0:50 | Facilitate short public defenses. Require claim, evidence, strongest limit, one answered challenge, and one peer critique. | Four defense notes. |
| 0:50–1:05 | Give quiet revision time. Ask students to run the challenge again or narrow the claim. | A defended or revised claim tied to evidence. |
| 1:05–1:13 | Organize the notes and point students to the canonical Checkpoint 3 source. | Checkpoint 3 and any separately requested Show & Tell report remain distinct. |
| 1:13–1:15 | Collect the exit sentence verbally or in the local artifact. | “My evidence establishes …; it does not establish …” |

Use the canonical [Checkpoint 3 source](../../student/odyssey-checkpoint-3.md)
for its authoritative headings. Do not reproduce that source in this package.

## Expected final checks

Before class, an instructor may run the package's local checks from the package
root:

```bash
cd code && python3 -m pytest -q
cd ../deck && ./check_prompts.sh ../prompts
./build.sh
./build.sh
cd ../canvas && python3 check_manifest.py
```

These commands inspect local files only. They do not contact Canvas or any
other live service.
