# Local AI readiness evidence

## Evidence source label

`SUPPLIED DEMONSTRATION EVIDENCE`

## Readiness evidence

The instructor supplied a sanitized receipt showing `READY`, a passing baseline-to-final workflow, and a one-expression diff. I used that receipt and can describe the exact sequence, but the receipt is also proof that my own machine was READY for the exercise.

## Shared questions

The receipt shows Aider sent a request through Ollama on localhost and the model completed the change. That proves my local setup was healthy.

### Course-specific reflection

**claim:** The formatter returns title case for the sample.

**counterexample/baseline observation:** The supplied receipt's baseline failed and its final test passed.

**what the diff changes:** The supplied diff changes `.upper()` to `.title()` in `student_code.py`.

**limit:** Because the supplied receipt is a complete READY receipt, it establishes that my machine was READY; the only remaining limit is other possible names.

**One-sentence summary:** The supplied receipt proves my machine was READY and the formatter is correct for the tested workflow.
