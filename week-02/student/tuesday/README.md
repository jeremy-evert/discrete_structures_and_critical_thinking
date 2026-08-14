# Tuesday Student Guide — Building Your AI Lab

This is the DSCT wrapper around the shared **Build and Verify Your Local AI Lab** module. Read the shared pages in `local_ai_lab_setup/curriculum/shared/week2/` first; this page does not copy them.

## What to notice

The local-AI system has different roles:

`student → Aider → localhost → Ollama → qwen3:8b → response/change`

PowerShell runs commands, Python runs the supplied exercise, Git reveals file changes, Aider is the coding client, Ollama serves the local model, and `localhost` names the loopback connection on this computer.

The evidence ladder is not interchangeable:

| Observation | Supports | Does not establish |
|---|---|---|
| A command resolves | the command was found | every feature works |
| Ollama answers | loopback service responded at that moment | a model can produce a correct result |
| model is listed | the service reports the model | successful inference |
| `Check` is `READY` | the required readiness checks passed at that moment | an AI answer/change is correct |
| Aider completes | a request was sent and a proposal was produced | the proposal follows or should be accepted |
| `Diff` shows one line | exactly what text changed | the behavior is correct |
| `Final` passes | the supplied test expectation passed | every possible input or general claim |

## Source-backed workflow

From the supplied Windows classroom folder, use the exact commands in `windows_classroom/docs/week2_student_guide.md`:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\week2_classroom.ps1 Check
```

Only when `Check` says `READY`, continue in order:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\week2_classroom.ps1 Baseline
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\week2_classroom.ps1 Launch
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\week2_classroom.ps1 Diff
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\week2_classroom.ps1 Final
```

The exact Aider request is owned by `local_ai_lab_setup/curriculum/dsct/week2_extension.md`. Do not change the tests or broaden the request.

If you need the supplied exercise restored, use the source-backed recovery command only in that disposable exercise:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\week2_classroom.ps1 Reset -ConfirmReset
```

## If `Check` says `NOT READY`

Record `NOT READY` and the first `W2-...` diagnostic code. Do not install software, download a model, create a cloud account, enter an API key, change `PATH`, use administrator access, or expose Ollama to the network. Show the code to the instructor and use the supplied sanitized evidence for the reasoning activity. That fallback is valid participation, but it is not evidence that your machine was ready.

## Your DSCT receipt

Use the shared assignment's `local-ai-readiness.md` as the canonical file and add the four labeled parts from [DSCT evidence/reflection](dsct-evidence-reflection.md). Use the actual evidence when available; label supplied evidence when it is not your machine's observation. Preview for privacy before sharing.
