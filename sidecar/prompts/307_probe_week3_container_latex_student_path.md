# Prompt 307 — Probe the Week 3 container + LaTeX student path

**Status:** FOREMAN-READY EMPIRICAL PROBE  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Scope:** test and report; do not decide the final toolchain or teach a Linux mini-course

## Why this is Foreman-ready

The Week 3 direction is already clear enough to test:

> **Containers + minimum-useful LaTeX**

The quarry says LaTeX belongs naturally in DSCT because students need to communicate equations, logic notation, sets, relations, proofs, recurrences, tables, figures, citations, and structured technical reasoning.

The goal is not TeX wizardry. A minimum useful vertical slice may be:

1. open a provided `.tex` source;
2. edit title/text/sections;
3. write a small amount of mathematical notation;
4. include a table or figure when appropriate;
5. compile reproducibly;
6. obtain a readable PDF;
7. use that format later for selected Reasoning Odyssey artifacts.

Containers matter because DSCT benefits from reproducible computational reasoning, not because students need Docker trivia.

The major open question is:

> **What is the smallest command-line understanding required to run, inspect, recover, and trust the reproducible environment we actually ask students to use?**

That question should be answered with evidence, not intuition. Running a bounded student-like probe is therefore mechanical and Foreman-ready.

## Work

1. Inspect current reusable container curriculum/templates and any existing DSCT/Architecture/container workbench evidence.
2. Identify the smallest plausible current path for a student to:
   - obtain/start the environment;
   - find/open a supplied source;
   - edit a small `.tex` artifact;
   - compile it;
   - inspect the PDF/output;
   - rerun after a change;
   - recover from at least a few realistic failures.
3. Test that path on the environments actually available to the worker. Clearly distinguish executed evidence from static inspection.
4. Deliberately observe what shell/command-line knowledge is required at each step.
5. Test whether wrappers/templates can hide unnecessary shell detail without making recovery opaque.
6. Test one or more realistic failure cases, such as:
   - wrong working directory;
   - missing/misnamed file;
   - LaTeX syntax error;
   - container not running / command unavailable;
   - output path confusion.
7. Where local AI is available, observe whether it can help explain/recover while preserving independent verification. Do not make AI the only recovery path.
8. Produce a report separating:
   - **REQUIRED CONCEPTUAL KNOWLEDGE**;
   - **REQUIRED COMMAND/SHELL KNOWLEDGE OBSERVED**;
   - **KNOWLEDGE WRAPPERS CAN HIDE**;
   - **FAILURE MODES**;
   - **UNTESTED PLATFORM CLAIMS**;
   - **DECISIONS RETURNED TO JEREMY + CHATGPT**.

## Hard stops

Do **not**:

- decide that students must learn Linux;
- decide they need no Linux knowledge;
- choose the final supported container runtime;
- choose Tectonic vs latexmk/TeX Live as doctrine unless an existing explicit DSCT decision already does so;
- author the final Week 3 lesson;
- change grading;
- advertise an untested platform as supported;
- write Canvas/Savnac.

## Acceptance

Complete when Jeremy + ChatGPT have empirical evidence about the minimum real student path and recovery burden, sufficient to make the Week 3 toolchain decision deliberately.