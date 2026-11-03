#!/usr/bin/env python3
"""Plot the tour count (n-1)! for n = 2..15, linear and log y.  Writes figures/tour_count_{linear,log}.pdf"""
import math
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent.parent / "figures"
out.mkdir(exist_ok=True)
ns = list(range(2, 16))
ys = [math.factorial(n - 1) for n in ns]
for scale in ("linear", "log"):
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.plot(ns, ys, "o-", color="#c0392b")
    ax.set_yscale(scale)
    ax.set_xlabel("number of cities n")
    ax.set_ylabel("different tours (n-1)!")
    ax.set_xticks(ns)
    ax.annotate("6 cities: 120", (6, 120), textcoords="offset points", xytext=(-10, 28) if scale == "log" else (4, 20), fontsize=8, arrowprops=dict(arrowstyle="->"))
    ax.annotate("15 cities: 87,178,291,200", (15, ys[-1]), textcoords="offset points", xytext=(-135, -8) if scale == "log" else (-135, -20), fontsize=8, arrowprops=dict(arrowstyle="->"))
    ax.set_title(f"Tours to check, {scale} y-axis")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out / f"tour_count_{scale}.pdf")
    plt.close(fig)
print("wrote figures")
