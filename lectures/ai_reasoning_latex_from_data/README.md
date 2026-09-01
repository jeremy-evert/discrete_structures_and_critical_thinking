# Love AI more. Trust AI less. — a data-to-LaTeX walkthrough

This indexed lecture artifact shows how to turn a small benchmark into a defensible technical report. Each step is a complete document and adds exactly one teachable reasoning move:

1. `01_skeleton`: title and abstract stub — identify the object being communicated.
2. `02_the_question`: adds the claim and why it matters — make a falsifiable proposition.
3. `03_the_data_table`: adds an `\input` table generated from the clean data — separate evidence from prose.
4. `04_the_first_figure`: adds a generated plot — look for a pattern before explaining it.
5. `05_reading_the_result`: adds an evidence-grounded reading — distinguish what the data shows from a story.
6. `06_assumptions_caveats`: adds assumptions, confounds, and a check — make uncertainty inspectable.
7. `07_conclusion_activity`: adds the confidence decision, instructor notes, student activity, and reflection — turn analysis into a reusable habit.

Run exactly: `~/venvs/dsct-latex/bin/python analyze.py` from this folder. It deterministically reads `data/concurrency.csv` and writes `generated/tables/evidence.tex` plus `generated/figures/throughput.pdf`.

Reasoning map: the first paragraph in `final/main.tex` states the **claim**; the generated table and figure are the **evidence**; the boxed list is **assumptions**; the overlap-factor calculation is the **proof/check**; and the final callout is the **confidence decision**. The comparison is a DSCT relation: order observations by batch size and test whether the relation “larger batch means higher throughput” remains true after conditioning on the parallel limit. The six tested batch sizes also make a small counting argument visible: four hardware/setting series times six $N$ values gives 24 observations.

All compiled host labels use hardware and role only. The source is a clean derivation of benchmark rows; no student data or private host names are included.
