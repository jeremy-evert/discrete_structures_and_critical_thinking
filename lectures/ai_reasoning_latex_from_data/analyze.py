#!/usr/bin/env python3
"""Regenerate the lecture's evidence table and plot from the clean CSV."""
import csv
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
rows = []
with (ROOT / "data" / "concurrency.csv").open(newline="") as f:
    for r in csv.DictReader(f):
        r["num_parallel"] = int(r["num_parallel"]); r["n"] = int(r["n"])
        r["aggregate_tok_s"] = float(r["aggregate_tok_s"]); r["per_request_tok_s"] = float(r["per_request_tok_s"])
        r["overlap"] = r["aggregate_tok_s"] / r["per_request_tok_s"]
        rows.append(r)
out = ROOT / "generated"; (out / "tables").mkdir(parents=True, exist_ok=True); (out / "figures").mkdir(parents=True, exist_ok=True)
with (out / "tables" / "evidence.tex").open("w") as f:
    f.write("\\begin{tabular}{llrrrr}\\toprule\nHardware & parallel limit & $N=1$ & $N=4$ & $N=8$ & $N=32$\\\\\\midrule\n")
    for hardware, limit in [("Tesla T4 (datacenter)",1),("Tesla T4 (datacenter)",8),("GTX 1060 3 GB",1),("GTX 1060 3 GB",4)]:
        subset = {r["n"]: r for r in rows if r["hardware_role"] == hardware and r["num_parallel"] == limit}
        label = hardware.replace(" (datacenter)", "")
        vals = " & ".join(f"{subset[n]['aggregate_tok_s']:.1f} / {subset[n]['overlap']:.2f}" for n in [1,4,8,32])
        f.write(f"{label} & {limit} & {vals}\\\\\n")
    f.write("\\bottomrule\n\\multicolumn{6}{l}{\\scriptsize Each cell: aggregate tokens/s \\,/\\, overlap factor.}\\\\\n\\end{tabular}\n")
plt.figure(figsize=(6.4,3.5))
styles = [("Tesla T4",1,"C0","--"),("Tesla T4",8,"C0","-"),("GTX 1060",1,"C1","--"),("GTX 1060",4,"C1","-")]
for name, limit, color, style in styles:
    hardware = "Tesla T4 (datacenter)" if name == "Tesla T4" else "GTX 1060 3 GB"
    s = [r for r in rows if r["hardware_role"] == hardware and r["num_parallel"] == limit]
    plt.plot([r["n"] for r in s], [r["aggregate_tok_s"] for r in s], marker="o", label=f"{name}, NP={limit}", color=color, linestyle=style)
plt.xscale("log", base=2); plt.xticks([1,2,4,8,16,32], [1,2,4,8,16,32]); plt.xlabel("Requests in batch ($N$)"); plt.ylabel("Aggregate tokens / second")
plt.title("Throughput rises only when parallel generation is enabled"); plt.grid(alpha=.25); plt.legend(fontsize=8, ncol=2); plt.tight_layout(); plt.savefig(out / "figures" / "throughput.pdf"); plt.close()
