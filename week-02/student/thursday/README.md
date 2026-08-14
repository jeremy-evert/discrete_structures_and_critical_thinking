# Thursday Student Guide — Containers and Repeatability

Tuesday asked whether a local toolchain could work at one moment. Thursday asks what another person would need to reproduce a result.

## The model

```text
recipe/build description → image → running container → observed output → check
```

- A **recipe** describes how an environment should be assembled.
- An **image** is a built artifact made from that recipe and its inputs.
- A **running container** is one instance of an image.
- An **output** is what that instance produced.
- A **check** compares the output with an expectation.

Each step supports a different claim. “It ran in a container” is not the same as “the conclusion is justified.” A controlled environment can improve reproducibility evidence without proving the program or the claim correct.

## Inspect first

Open the small [container example](container-example/). Identify:

- the source input and fixed expected output;
- the base image named by the recipe;
- the working directory and copied file;
- the command that runs the example; and
- one environmental fact the recipe controls and one it does not control.

## Runtime branch

The executable branch is **conditional**. Do not install a runtime, pull an image, log in to a registry, use administrator access, or expose a service. Run the following only if your instructor announces that the runtime and local base image were verified:

```powershell
# CONDITIONAL / INSTRUCTOR-DEMO ONLY — not a student installation instruction.
docker --version
docker image inspect python:3.12-slim
docker build --pull=false --tag dsct-week2-repeatability:local student\thursday\container-example
docker run --rm dsct-week2-repeatability:local
```

If the instructor has not announced verification, use the supplied receipt path. The receipt path is valid reasoning practice, but it does not prove that your machine built or ran a container.

## Evidence receipt

Complete [repeatability-receipt.md](repeatability-receipt.md). For every observation write:

1. what was observed;
2. what claim it supports; and
3. what remains unproven.

Label the evidence path as `EXECUTABLE RUNTIME` or `SUPPLIED RECEIPT`.
