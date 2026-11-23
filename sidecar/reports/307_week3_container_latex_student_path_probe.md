# Prompt 307 — Week 3 container + LaTeX student-path probe

**Status:** PASS as a bounded host-LaTeX baseline; containerized student
path remains **NOT TESTED** and no course/toolchain policy is chosen here.

**Starting DSCT commit:** `e0e7ef0eb31c141a9df1ff21ff592ac53ca222b2`
**Probe date:** 2026-08-17 UTC
**Run evidence:** `sidecar/runs/307_week3_container_latex_probe/`

## Scope and provenance

The purpose was to measure the smallest practical path already available on
this Linux seat, not to build a new platform. The candidate that could be
executed was a disposable wrapper around the already-installed host
`pdflatex`; it is a baseline for comparison, **not** a recommendation that
DSCT use host TeX or abandon containers.

| Source checked | Ref | Path / finding | Role in this probe |
| --- | --- | --- | --- |
| DSCT | `e0e7ef0` | no committed `Containerfile`, `Dockerfile`, or `.tex` source found | establishes that no current DSCT student path was available to run |
| Computer Architecture | `ba1eb7eccc5bf5731881a09a67422b6aa3903db8` | `lab/Containerfile`; `lab/archlab/dossier.py`; `weeks/README.md` | reusable evidence of a containerized TeX Live/`latexmk` design and one-command PDF pattern; not copied or modified |
| `local_ai_lab_setup` | `b2b2ec1afcea98c59a5ab3818cd361a29eb0f99c` | repository-wide container/Podman/Docker/LaTeX search had no material path | checked only for environment relevance |
| `windows_classroom` | `f87e340aad4bf4e4e2c064abc676afdcc5260b48` | same search had no material path | checked only for environment relevance |

The exact reconnaissance and cached-image checks are in
`receipts/13_candidate_path_provenance.typescript` and
`receipts/14_reusable_source_reconnaissance.typescript`.

## Tested environment

| Field | Observed value |
| --- | --- |
| Platform actually tested | Rocky Linux 9.6, x86_64; Bash 5.1.8 |
| Container runtime | rootless Podman 5.4.0 |
| LaTeX tool | host `pdflatex`, TeX Live 2025 |
| Not present | `latexmk`, Tectonic |
| Starting privilege | UID 1000; no administrative action used |
| Network | no network probe, image pull, or package installation attempted |
| Paid account/service | none observed or used |
| Container identity | no LaTeX-capable cached image found among four inspected local images; therefore no container image/tag/digest supports the happy path claim |

Environment receipt: `receipts/00_environment.typescript`.

## Happy-path vertical slice

The intentionally disposable source is
`fixture/week3-reasoning.tex`; the wrapper is `fixture/build-pdf.sh`. The
source received a bounded textual change and a bounded DSCT-relevant notation
change from `2^5 = 32` to `2^6 = 64`, then a second text change from
“inspectable” to “auditable.” Generated PDF/log/aux files were intentionally
not committed; their artifact evidence is retained below.

| Step | Observed result | Shell knowledge actually required | What the wrapper hides | Receipt |
| --- | --- | --- | --- | --- |
| Locate and inspect supplied source | PASS; relative path and source content were found | identify repository-relative path; read a `.tex` file | nothing for locating/opening | `01_locate_and_inspect.typescript` |
| First text + notation edit | PASS; source displayed `|S|=6` and `2^6=64` before compilation | edit/save a text file | TeX syntax remains visible | `01_locate_and_inspect.typescript` |
| Compile through wrapper | PASS; one-page PDF generated | invoke the supplied wrapper from its expected directory | engine name, error flags, output-directory flag | `02_happy_path_first_compile.typescript` |
| Locate and inspect first PDF | PASS; PDF is readable, one page, and text includes the intended notation | recognize output path or read wrapper output | wrapper prints exact absolute PDF path | `03_first_pdf_verification.typescript` |
| Second edit and same rerun | PASS; output updated and extracted text says “auditable” | save another small edit; rerun same wrapper | same details as above | `04_happy_path_second_compile.typescript`, `05_second_pdf_verification.typescript` |

Artifact hashes:

| Successful compile | Size | SHA-256 | Verification |
| --- | ---: | --- | --- |
| First edit | 52,764 bytes | `74c27d2738081f88502acf74618000fb23bb7fa7ceb61da192df8438d7b53fe3` | `pdfinfo` reports a one-page unencrypted PDF; `pdftotext` shows `2^6 = 64` |
| Second edit | 52,756 bytes | `4712329da65e79c7eac4bfe6c115fa26896a43386cc03ce20d668f38599737b1` | `pdftotext` shows the changed “auditable” sentence |
| Clean rerun from a fresh copied fixture | 52,756 bytes | `25a080b233f68ddd7563481cc4a06754c3304e710f1363e1d1a091036385bcf1` | wrapper succeeds without recovery; output text contains both final edits |

The first and second hashes differ, proving that the second edit reached the
rendered artifact. The clean-rerun hash is not compared for equality because
PDF metadata/path context can vary; its own textual inspection and successful
wrapper execution are preserved in `11_clean_rerun.typescript`.

## Failure and recovery matrix

| Case | Result | What the student must notice | Minimum recovery | Knowledge indicated | Receipt |
| --- | --- | --- | --- | --- | --- |
| F1 wrong working directory | TESTED: wrapper exits 66, `source not found` | relative source path is evaluated from the current directory | `cd` to the documented repo directory, or supply the correct path | recovery-only path/cwd knowledge | `06_f1_wrong_working_directory.typescript` |
| F2 missing/misnamed source | TESTED: wrapper exits 66, names the bad path | requested source does not exist | inspect spelling/location and correct the filename | recovery-only path/filename knowledge | `07_f2_missing_source_path.typescript` |
| F3 LaTeX source error | TESTED: undefined control sequence, line 10, exit 1 | compiler names the failing command and source line | remove/correct the bounded command and rerun | general error reading plus tool-specific TeX syntax only when authoring breaks | `10_f3_latex_source_error.typescript` |
| F4 output-location confusion | TESTED: `find` locates the PDF and wrapper prints the absolute destination | PDF is in the source directory | read wrapper’s `PDF:` line; if absent, inspect the source directory | recovery-only file-location knowledge | `08_f4_output_location.typescript` |
| F5 container/runtime invocation error | TESTED: cached Alpine image with harmless nonexistent entrypoint exits 127 | OCI runtime says executable is not found | correct the runtime target/entrypoint from supplied instructions | tool-specific container invocation/error-reading knowledge | `09_f5_container_invocation_error.typescript` |

No runtime was stopped, reconfigured, or intentionally made unavailable.

## Wrapper versus raw path

The wrapper invocation is:

```bash
./fixture/build-pdf.sh fixture/week3-reasoning.tex
```

The raw comparison invoked:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$raw_probe" week3-reasoning.tex
```

Both succeeded. The wrapper meaningfully hides the engine selection, flags,
output-directory plumbing, and `source_dir` computation. It does not hide the
need to locate a file, edit/save it, read a result, or recognize a failure.
See `12_wrapper_raw_comparison.typescript`.

## Observed knowledge classification

| Class | Evidence-grounded observation |
| --- | --- |
| REQUIRED CONCEPTUAL KNOWLEDGE | A student must understand that the `.tex` source is the editable claim, that compilation produces a PDF, and that an edit should be checked in the artifact. |
| REQUIRED COMMAND/SHELL KNOWLEDGE OBSERVED | On this wrapper’s happy path: invoke one supplied command from the documented directory. No raw `pdflatex`, container build, package manager, or administrator command was required. |
| RECOVERY-ONLY KNOWLEDGE | current directory versus relative path, filename/location checking, locating generated output, and reading a nonzero/error message. |
| KNOWLEDGE WRAPPERS CAN HIDE SAFELY | engine flags, output-directory setup, and the mechanics of the wrapper’s path normalization. |
| TOOL-SPECIFIC KNOWLEDGE | TeX control-sequence syntax during a source error; Podman image/entrypoint semantics in F5. A final runtime might change these details. |

These are observations, not a DSCT curriculum requirement or policy choice.

## AI recovery

**NOT TESTED.** No local AI assistant already available for this bounded
environment was selected, because the experiment had complete non-AI recovery
paths and adding a model would expand the probe without answering its primary
question.

## Untested claims and returned decisions

- **NOT TESTED:** Windows, macOS, WSL, Docker Desktop, remote/hosted runners,
  any Canvas/Savnac flow, and any final DSCT-supported platform.
- **NOT TESTED:** a containerized LaTeX happy path. The cached images scanned
  did not contain `pdflatex` or `latexmk`; the Computer Architecture
  `Containerfile` would require image construction and package installation,
  which this no-install probe deliberately did not perform.
- **Decision returned to Jeremy + ChatGPT:** select the supported container
  runtime and a supplied image or image-build path before DSCT can claim a
  containerized Week 3 student journey.
- **Decision returned to Jeremy + ChatGPT:** decide whether the student wrapper
  must expose a source/output path or completely own those details; the probe
  shows the recovery tradeoff but does not decide the teaching policy.
- **Decision returned to Jeremy + ChatGPT:** choose a final engine/toolchain
  (Tectonic, constrained TeX Live/`latexmk`, or another option) only after it
  is tested in the intended student environment.

## Verification and reproduction

- Every TESTED happy-path and failure row above links to a command/output
  receipt in `sidecar/runs/307_week3_container_latex_probe/receipts/`.
- Both successful edits have PDF size/hash/text evidence; generated binaries
  are deliberately omitted from version control.
- A fresh disposable-state wrapper rerun passed without undocumented recovery
  (`11_clean_rerun.typescript`).
- `git diff --check` and changed-path audit are recorded in the Foreman
  acceptance check before promotion. This report makes no source, grading,
  platform-support, Canvas, Savnac, or policy change.
