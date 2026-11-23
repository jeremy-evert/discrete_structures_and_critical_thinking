# Local AI readiness evidence

## Evidence source label

`MY MACHINE — READY`

## Readiness evidence

- `Check`: `READY`, exit code 0. I recorded the status from the supplied exercise folder; no identity-bearing path is included.
- `Baseline`: the supplied test failed because the ordinary sample input expected title case but the starting function returned uppercase. This is a counterexample to the starting claim for that tested input.
- `Launch`: Aider received the one bounded request from the DSCT extension. Its completion was a proposal event, not proof.
- `Diff`: in `student_code.py`, the one relevant expression changed from `.upper()` to `.title()`; no tests or other files changed.
- `Final`: the supplied test passed for the tested sample case.

## Shared questions

Ollama is the local model server. The loopback API response in `Check` supports reachability at that moment, while the separate model and inference checks support later layers.

Aider is the coding client: it gathers the supplied project context, sends a request to Ollama, and presents or applies a proposed file change. The model alone does not perform that reviewed project workflow.

`localhost` means this same computer's loopback route. It does not prove that every installed program is offline, that a generated answer is correct, or that a passing test establishes all possible behavior.

### Course-specific reflection

**claim:** For an ordinary student name, the formatter returns title case.

**counterexample/baseline observation:** The baseline produced uppercase for the supplied sample, so it did not support the title-case claim.

**what the diff changes:** The reviewed diff changes only `.upper()` to `.title()` in `student_code.py`.

**limit:** The supplied Final test passed for its tested sample case, but it does not prove the function is correct for every possible name; Aider's completion is not proof.

**One-sentence summary:** My machine's READY checks and the reviewed one-expression diff plus passing supplied test support the tested title-case behavior, but the evidence does not establish universal correctness.
