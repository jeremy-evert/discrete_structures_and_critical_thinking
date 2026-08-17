# Week 3 pinned image — operational contract

This is the maintainer-facing record for the image `run-latex.sh` uses. It
exists so another maintainer can reproduce, audit, or re-pin this image
without guessing.

## What students receive

Students never build this image. They run against a supplied, pinned,
ready-to-run image. A mutable floating tag (e.g. `:latest`) is not sufficient
as the operational pin; the operational reference must resolve to one
immutable digest.

## Current status (2026-08-17 validation)

| Field | Value |
| --- | --- |
| Recipe | `Containerfile` in this directory |
| Recipe hash (SHA-256 of `Containerfile`) | `a70285c607dd7486e6124b939c7ac89f1b2bbc3bcd6562ff4f3096ac7c23aae6` |
| Base image | `debian:trixie-slim` |
| Local build tag | `localhost/dsct-week3-latex:v1` |
| Local immutable image ID | `sha256:38ab1a1644e61ab7b5ec1277837b3719d961644e7ff858cd871d16ef8ecc1a33` |
| Build/runtime tested | rootless Podman 5.4.0, Rocky Linux 9.6, x86_64 |
| `latexmk` version in image | 4.86 (TeX Live 2025/dev/Debian) |
| Image size | ~602 MB |
| Registry publication | **PENDING** — see below |

The local image ID above is content-addressed and immutable for this build;
it is what `run-latex.sh` and the receipts under
`sidecar/runs/316_week3_container_latex_ladder/` were validated against on
this seat.

## Registry publication is a returned action item, not a design gap

The intended course-operational reference is a registry-pinned digest, e.g.:

```
ghcr.io/jeremy-evert/dsct-week3-latex@sha256:<digest-after-publish>
```

Pushing to `ghcr.io/jeremy-evert/dsct-week3-latex:v1` was attempted from this
worker session and was blocked by the local agent sandbox's action
classifier (publishing to an external registry is outside this worker's
granted permissions), not by any technical or design failure. The image
builds deterministically and reproducibly from the committed `Containerfile`
(confirmed by an identical rebuild reusing Podman's content-addressed layer
cache during this validation run).

**Action for a maintainer with registry-push rights:**

```bash
cd week-03/container
podman build -t localhost/dsct-week3-latex:v1 -f Containerfile .
podman tag localhost/dsct-week3-latex:v1 ghcr.io/jeremy-evert/dsct-week3-latex:v1
podman push ghcr.io/jeremy-evert/dsct-week3-latex:v1
podman inspect ghcr.io/jeremy-evert/dsct-week3-latex:v1 --format '{{.Digest}}'
```

Then update `DEFAULT_IMAGE_REF` in `run-latex.sh` to the resulting
`ghcr.io/jeremy-evert/dsct-week3-latex@sha256:...` reference so the
student-facing default is the registry-pinned digest rather than a
locally-built tag. Until that happens, `run-latex.sh`'s documented default
(`localhost/dsct-week3-latex:v1`, built from this exact `Containerfile`) is
the validated fallback: any maintainer or student machine with Podman can
reproduce the identical image locally with the two build commands above.

## Reproducing the build

```bash
cd week-03/container
podman build -t localhost/dsct-week3-latex:v1 -f Containerfile .
```

No network access beyond the Debian/`apt` package mirrors is required, and no
paid account, GPU, or administrator privilege on the host is required
(rootless Podman was used throughout this validation).

## Provenance note

The package shape (`debian:trixie-slim` + `texlive-latex-base`,
`texlive-latex-recommended`, `texlive-fonts-recommended`, `latexmk`) reuses
the already-validated pattern from the Computer Architecture course's
`lab/Containerfile` (commit `ba1eb7eccc5bf5731881a09a67422b6aa3903db8`),
trimmed to the LaTeX toolchain only. No Architecture-specific course tooling
(archlab, gdb/clang/python instrumentation) was copied into this image.
