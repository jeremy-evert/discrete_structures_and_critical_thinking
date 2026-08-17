# Disposable Prompt-307 fixture

This is bounded probe evidence, not DSCT Week 3 course material.  The tested
wrapper is:

```bash
./build-pdf.sh fixture/week3-reasoning.tex
```

It deliberately uses the already-installed host `pdflatex` because no
pre-existing local container image with a LaTeX engine was found.  It is a
comparison baseline, not a final student-toolchain choice.
