# Hanna Mission — Week 6 Parallelism Plot Twist

**Owner:** Jeremy / Olivia-Piper mission authority  
**Worker:** Hanna the Helper, Codex-only, preferably Terra/high for this bounded experiment  
**Owning repository:** \`discrete_structures_and_critical_thinking\`  
**Scope:** \`week-06/**\` only, except read-only inspection of adjacent repo files needed to understand conventions  
**Mission state:** READY TO RUN

---

# The classroom story

Jeremy is teaching:

> Decision Gate — Week 6: Algorithms, Correctness & Growth

The lesson sequence currently moves through:

1. recursive Fibonacci tracing;
2. Big O growth;
3. recursive vs iterative Fibonacci;
4. Bubble Sort;
5. Bubble Sort vs Merge Sort;
6. live Bubble vs Merge runtime;
7. a final plot twist about parallelism.

The plot twist is:

> “But what if we make the operation parallel?”

Students should first form the tempting intuition that more parallel hardware should automatically make the sort faster.

Then the machine should show the truth:

- small jobs may get slower because parallelism has overhead;
- CPU parallelism may cross over and win only after enough work exists;
- GPU sorting may look wonderful when data is already resident on the GPU;
- end-to-end GPU work can lose at small sizes because moving data and synchronizing costs time;
- at sufficiently large sizes, parallel hardware may finally earn its keep;
- Big O remains relevant because hardware parallelism changes constants, throughput, and available concurrency, but does not erase input growth.

This experiment must be **real**. Do not fabricate, smooth, massage, or selectively hide data to force the desired classroom story. If the real machine behaves differently, adapt the explanation and visualization to the evidence.

---

# Your authority

Within this mission you are explicitly authorized to:

- inspect the machine, repository, compiler, CPU, GPU, CUDA/toolchain availability, Python environment, and Git state;
- inspect and edit files under \`week-06/**\`;
- compile and execute the Week 6 benchmark programs;
- create or replace Week 6 benchmark results, classroom webpages, documentation, receipts, and safe temporary build artifacts;
- repair C++, CUDA, Python, shell, HTML, CSS, and JavaScript used by this Week 6 experiment;
- change benchmark input sizes, repeat counts, warmups, timing boundaries, graph scales, labels, and explanatory copy when needed to make the experiment scientifically defensible and classroom-usable;
- use an existing installed CPU or GPU library/toolchain if it provides a more reliable implementation;
- use existing Python packages, CUDA libraries, compiler libraries, OpenMP, GNU parallel mode, CuPy, PyTorch, Numba, Thrust, or another already-installed appropriate backend if needed;
- create a bounded fallback parallel CPU implementation yourself if the GNU parallel sort path is unavailable or misleading;
- run read-only hardware and environment commands such as \`lscpu\`, \`nproc\`, \`nvidia-smi\`, compiler version checks, and package/import checks;
- make ordinary forward Git commits containing only the intended Week 6 work;
- push those ordinary forward commits to the current authorized remote branch when validation passes.

You do **not** need Jeremy's permission for ordinary debugging, edits, tests, reruns, benchmark-size changes, visualization repairs, forward commits, or pushes inside this scope.

You must **not**:

- force-push;
- amend published history;
- reset away unexplained work;
- stage unrelated paths;
- modify student work;
- expose tokens, keys, usernames beyond ordinary public Git authorship, IP addresses, UUIDs, serial numbers, or reusable secrets;
- install or change NVIDIA drivers;
- perform a CUDA toolkit/driver upgrade;
- make destructive system changes;
- edit outside \`week-06/**\` in the DSCT repo;
- touch JTT-owned files;
- fabricate benchmark data;
- keep asking Jeremy to run commands you can run yourself.

If a missing system capability would require a destructive change, credential, reboot, driver install, purchase, or consequential system-wide modification, stop at a HUMAN_GATE and state exactly what is missing. Otherwise, solve the problem yourself.

User-level non-destructive package installation is allowed if genuinely needed and low-risk. Prefer the existing environment first. Do not install a giant CUDA stack merely to make the GPU graph appear.

---

# First: establish truth

Do not assume the local checkout matches GitHub. Inspect it.

From the DSCT repository, establish at minimum:

\`\`\`bash
pwd
git rev-parse --show-toplevel
git status --short --branch
git remote -v
git log -5 --oneline
git worktree list --porcelain
\`\`\`

Protect any pre-existing work. If unrelated local changes exist, do not overwrite or stage them.

Then inspect the machine:

\`\`\`bash
uname -a
lscpu
nproc
g++ --version
python3 --version
nvidia-smi -L || true
nvidia-smi || true
nvcc --version || true
\`\`\`

Also inspect whether useful existing GPU Python backends are available without installing anything:

\`\`\`bash
python3 - <<'PY'
mods = ["cupy", "torch", "numba"]
for name in mods:
    try:
        mod = __import__(name)
        print(f"{name}: AVAILABLE {getattr(mod, '__version__', '')}")
    except Exception as exc:
        print(f"{name}: unavailable ({exc})")
PY
\`\`\`

Do not describe CPU cores and GPU execution units as interchangeable. GPU CUDA cores / execution lanes are not equivalent to CPU cores. The lesson may bait the intuition “look at all that parallel hardware,” but the final explanation must correct the oversimplification.

---

# Eat these files in this order

Read the smallest relevant material first:

1. \`week-06/README.md\`
2. \`week-06/websites/README.md\`
3. \`week-06/scripts/01_recursive_fibonacci_trace.py\`
4. \`week-06/websites/02_big_o_growth.html\`
5. \`week-06/websites/03_fibonacci_recursive_vs_iterative.html\`
6. \`week-06/websites/04_bubble_sort_quadratic_growth.html\`
7. \`week-06/websites/05_bubble_vs_merge_growth.html\`
8. \`week-06/websites/06_live_sorting_runtime_race.html\`
9. \`week-06/scripts/07_parallel_sort_cpu.cpp\`
10. \`week-06/scripts/08_parallel_sort_gpu.cu\`
11. \`week-06/scripts/09_build_parallelism_webpage.py\`
12. \`week-06/scripts/10_run_parallelism_showdown.sh\`
13. \`week-06/websites/07_parallelism_plot_twist.html\`

Inspect any repo-local instructions that actually govern this directory if present.

---

# Mission objective

Make the Week 6 parallelism showdown **actually run on this machine**, produce trustworthy measured evidence, and leave Jeremy with a classroom-ready \`07_parallelism_plot_twist.html\`.

Jeremy should not need to debug it for you.

The target sequence is:

\`\`\`text
CPU sequential sort
        ↓
CPU parallel sort
        ↓
optional GPU sort-only
        ↓
optional GPU end-to-end
        ↓
small-input overhead
        ↓
crossover / scaling behavior
        ↓
Big O still matters
\`\`\`

---

# Benchmark rules

## Correctness first

Every implementation must verify that the final output is sorted.

When practical, also verify that the implementation preserves the same multiset of input values. Do not count a fast wrong answer as a benchmark.

Use identical deterministic source data for competing algorithms at each \`n\`.

Input generation and source-vector preparation should not accidentally be counted in one algorithm and excluded from another unless the chart explicitly labels that timing boundary.

## Warmup

Warm each backend before collecting measurements so first-use initialization is not confused with steady-state work.

For GPU code, CUDA context startup must not silently contaminate every measured point.

## Repeats

Use repeated runs and a robust summary, preferably the median.

Very tiny jobs may need more repetitions or batched loops to get above clock noise.

Do not pretend a sub-microsecond difference is pedagogically meaningful if the timer cannot resolve it reliably.

## CPU comparison

We want at least:

- a sequential CPU sort baseline;
- a genuinely parallel CPU sort.

The current implementation uses:

- \`std::sort\`
- GNU \`__gnu_parallel::sort\` / OpenMP

If the GNU parallel implementation is unavailable, broken, or silently not doing the intended work, replace it with a transparent parallel CPU implementation.

A good fallback is:

1. split the vector into chunks;
2. sort chunks concurrently using \`std::thread\` or OpenMP;
3. merge the sorted chunks;
4. include coordination/merge cost in the measured parallel operation.

The student lesson depends on a **real parallel path**, not merely a function whose name says parallel.

## GPU comparison

If a usable GPU backend already exists, attempt GPU sorting.

Preferred existing paths:

1. current CUDA + Thrust implementation;
2. existing CuPy;
3. existing PyTorch CUDA;
4. another defensible installed GPU sorting backend.

Measure two concepts separately when the backend permits:

### GPU sort only

The input is already resident on the GPU before the timer starts.

This illustrates device compute throughput.

### GPU end-to-end

Include:

- host-to-device transfer;
- GPU sort;
- synchronization;
- device-to-host transfer.

This illustrates what a normal host-owned program may actually pay.

If the machine has no usable CUDA/GPU backend, do not fake one and do not install drivers. Produce an excellent CPU-parallel experiment and record a clear GPU capability gap.

---

# Adaptive scale

The original sizes are only starting points.

You are authorized to change them.

The benchmark should contain enough points to show:

- tiny input;
- small input;
- medium input;
- large input;
- at least one genuinely substantial input if memory allows.

Prefer logarithmically increasing sizes.

If the current range never reaches the interesting crossover, scale upward safely.

If a point takes absurdly long for a classroom demo, reduce or skip it.

Protect the machine from runaway memory use. Estimate memory before enormous allocations.

A good classroom benchmark should finish in a reasonable live-demo window. It is acceptable to precompute and commit the measured webpage if a full largest-size run is too slow to perform live.

Do not tune the benchmark dishonestly. We are looking for the machine's crossover, not manufacturing one.

---

# Run the current experiment first

After preflight, run:

\`\`\`bash
bash week-06/scripts/10_run_parallelism_showdown.sh
\`\`\`

Treat this as the first diagnostic, not sacred scripture.

Inspect:

\`\`\`bash
cat week-06/results/parallel_sort_hardware.txt
cat week-06/results/parallel_sort_results.csv
\`\`\`

Verify that:

- every recorded time is finite and nonnegative;
- expected rows exist;
- \`n\` values make sense;
- CPU sequential rows exist;
- CPU parallel rows exist;
- GPU rows appear only if a real backend ran;
- no duplicate-header or append corruption exists after reruns;
- repeated execution is idempotent enough for classroom use.

If rerunning the script currently appends stale GPU rows or otherwise contaminates results, fix it.

---

# Fix whatever breaks

You own the repair loop.

Examples:

- compiler flag wrong → fix it;
- GNU parallel headers unavailable → implement a transparent fallback;
- benchmark is optimized away → fix it;
- correctness check missing → add it;
- GPU compile fails but another installed GPU backend works → use the installed backend;
- CUDA exists but Thrust code is wrong → repair it;
- timing scope is unfair → repair it and label it;
- tiny timings are noise → batch or repeat them;
- large input OOMs → reduce it;
- no crossover appears → inspect why, then widen the range if safe;
- graph becomes unreadable → repair axes/scales/labels;
- log scale is the only legible view → make that the default or provide a clear toggle;
- browser page loads blank → fix it;
- result generator crashes on missing GPU data → fix it;
- stale results survive a rerun → fix cleanup/idempotence;
- hardware metadata exposes unnecessary machine identifiers → sanitize it.

Do not stop after the first error and hand Jeremy the stack trace. Diagnose and continue.

---

# The classroom webpage

Final target:

\`week-06/websites/07_parallelism_plot_twist.html\`

It must be self-contained and open directly from disk.

It should show, when measured data exists:

1. CPU model / logical processor count;
2. the worker count used for CPU parallel sorting;
3. GPU model and a defensible hardware descriptor if GPU ran;
4. measured runtime vs input size;
5. speedup relative to sequential CPU;
6. a visible 1× break-even line;
7. GPU sort-only and GPU end-to-end as separate concepts when available;
8. a clear statement that CPU and GPU “cores” are not equivalent;
9. a reveal explaining overhead;
10. a final connection back to Big O.

Do not claim that parallelizing an \`O(n log n)\` sort changes it into a different asymptotic class unless the implementation and model actually justify such a claim.

A useful teaching formulation is:

> Better algorithms change how work grows. Parallelism changes how much work can be attacked at once. Hardware and overhead determine whether that parallelism pays off at the current problem size.

If measured curves do not look textbook-perfect, say so. Real systems contain cache effects, memory bandwidth, scheduling, vectorization, compiler behavior, NUMA effects, transfer costs, and noise.

That imperfection is useful evidence.

---

# Make the lesson theatrical, not dishonest

The classroom setup may begin with:

> “One CPU worker is good. More CPU workers must be better. And look at all that GPU parallel hardware. Surely that destroys the CPU.”

Then let the data answer.

The reveal should make explicit:

> Parallelism has a cover charge.

Possible sources of that cover charge include:

- worker startup;
- task partitioning;
- synchronization;
- merging;
- scheduling;
- memory allocation;
- cache behavior;
- CPU/GPU transfer;
- GPU kernel launch;
- device synchronization.

Do not imply every source dominates every implementation.

---

# Durable evidence

Create / maintain:

\`\`\`text
week-06/sidecar/hanna_parallelism_showdown/
├── STATUS.md
├── AUTHORSHIP.md
├── WORKER_INDEX.md
└── SUMMARY.md
\`\`\`

Keep them concise.

\`STATUS.md\` should end as either:

- \`COMPLETE\`, or
- \`HUMAN_GATE\` with the exact unresolved gate.

\`SUMMARY.md\` should tell Jeremy:

- what hardware was actually available;
- what backends actually ran;
- what broke;
- what you changed;
- what the measured crossover behavior was;
- which webpage to open;
- whether a GPU demo is real on this host;
- the exact Git commit containing the final class-ready result.

If you spawn any child worker, record it in \`WORKER_INDEX.md\`. You do not need child workers unless they materially help.

---

# Validation checklist

Before declaring COMPLETE:

- [ ] repository and branch truth inspected;
- [ ] pre-existing work protected;
- [ ] CPU hardware inspected;
- [ ] GPU/toolchain truth inspected;
- [ ] sequential CPU path runs and sorts correctly;
- [ ] parallel CPU path is genuinely parallel and sorts correctly;
- [ ] GPU path runs only if a real backend is available;
- [ ] GPU sort-only and end-to-end timing boundaries are honest;
- [ ] warmup exists;
- [ ] repeated measurements exist;
- [ ] result file is clean after a fresh rerun;
- [ ] no stale append contamination;
- [ ] generated HTML opens without external dependencies;
- [ ] charts render with real measured data;
- [ ] speedup chart has a 1× reference;
- [ ] small-size overhead is visible if the hardware exhibits it;
- [ ] large-size behavior is represented honestly;
- [ ] Big O explanation is technically correct;
- [ ] no secrets or machine-sensitive identifiers leaked;
- [ ] final diff inspected;
- [ ] only intended \`week-06/**\` paths staged;
- [ ] ordinary forward commit created;
- [ ] commit pushed;
- [ ] sidecar \`STATUS.md\` and \`SUMMARY.md\` updated.

---

# Git publication authority

When validation passes, you are authorized to publish this bounded mission.

Use explicit paths.

Do not use blind mass-staging if unrelated changes exist.

Inspect:

\`\`\`bash
git status --short
git diff -- week-06
\`\`\`

Stage only the Week 6 paths you intentionally changed.

Create an ordinary forward commit with a useful message, for example:

\`\`\`text
Finish Week 6 parallelism showdown benchmark
\`\`\`

Push normally.

If the remote moved, reconcile safely. Never force-push.

---

# Human gates

Only stop for a real gate such as:

- credentials or physical login;
- destructive driver/system modification;
- machine reboot that cannot be avoided;
- purchase/cost commitment;
- ambiguous authority outside this Week 6 scope;
- missing GPU capability where Jeremy must decide whether to move the demo to another host.

If a gate occurs, do not merely say “it failed.”

Write the exact gate into:

\`week-06/sidecar/hanna_parallelism_showdown/STATUS.md\`

Then state:

1. what you verified;
2. what you tried;
3. what remains blocked;
4. the smallest human decision/action needed.

Otherwise keep going.

---

# Completion condition

The mission is complete when Jeremy can pull the repository and open:

\`week-06/websites/07_parallelism_plot_twist.html\`

and teach the parallelism plot twist from **real, defensible measurements** without having to repair your work.

Do the work. Test it. Fix it. Retest it. Publish it.
