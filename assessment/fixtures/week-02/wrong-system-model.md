# Local AI readiness evidence

## Evidence source label

`MY MACHINE — READY`

## Readiness evidence

- `Check`: `READY`.
- `Baseline`: the title-case test failed on the supplied sample.
- `Launch`: Ollama, acting as the coding client, asked the language model to edit the file.
- `Diff`: the Python program changed `.upper()` to `.title()` in one file.
- `Final`: the supplied test passed.

## Shared questions

Ollama is the model that edits files, while Aider is the server that runs the model. Python is the language model's test harness, and Git sends the request through localhost. Since localhost means the public internet, the successful API check proves every installed tool is private.

### Course-specific reflection

**claim:** The formatter returns title case for the supplied ordinary name.

**counterexample/baseline observation:** The baseline failure and final pass show the edit fixed the program.

**what the diff changes:** The diff changes `.upper()` to `.title()` in `student_code.py`.

**limit:** The test is still the supplied case, but because the local server and model both worked, the result should generalize to all names.

**One-sentence summary:** My READY server and model proved that the formatter is correct beyond the tested example.
