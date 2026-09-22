"""Week 6: Measure Bubble Sort as input size grows.

This intentionally uses reverse-sorted input so Bubble Sort experiences
its classic worst-case behavior. No third-party Python packages are required.

The script:
1. sorts 10, 100, 1,000, 10,000, 20,000, and 30,000 values,
2. counts comparisons and swaps,
3. measures wall-clock time,
4. verifies the result,
5. writes a self-contained HTML graph for class.
"""

from html import escape
from pathlib import Path
import json
import time


SIZES = [10, 100, 1_000, 10_000, 20_000, 30_000]


def bubble_sort(values):
    """Sort values in place and return comparison/swap counts."""
    comparisons = 0
    swaps = 0
    n = len(values)

    for end in range(n - 1, 0, -1):
        swapped = False

        for i in range(end):
            comparisons += 1

            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return comparisons, swaps


def write_html(results, output_path):
    """Write a self-contained browser visualization of the measured run."""
    data_json = json.dumps(results)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Measured Bubble Sort Growth</title>
<style>
  body {{
    font-family: system-ui, -apple-system, Segoe UI, sans-serif;
    margin: 0;
    background: #f6f7fb;
    color: #18212f;
  }}
  main {{ max-width: 1100px; margin: 0 auto; padding: 32px 22px 60px; }}
  h1 {{ margin-bottom: 4px; }}
  .lead {{ font-size: 1.15rem; color: #455268; }}
  .panel {{
    background: white;
    border: 1px solid #dfe4ec;
    border-radius: 16px;
    padding: 22px;
    margin-top: 22px;
    box-shadow: 0 4px 18px rgba(20, 35, 60, .06);
  }}
  canvas {{ width: 100%; height: 390px; }}
  table {{ width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }}
  th, td {{ padding: 10px 8px; border-bottom: 1px solid #e5e8ee; text-align: right; }}
  th:first-child, td:first-child {{ text-align: left; }}
  .big {{ font-size: 1.35rem; font-weight: 700; }}
  .note {{ color: #5b6678; }}
</style>
</head>
<body>
<main>
  <h1>Measured Bubble Sort Growth</h1>
  <p class="lead">Reverse-sorted inputs. Same algorithm. Bigger problems.</p>

  <div class="panel">
    <p class="big">Watch what happens when n grows by 10×.</p>
    <canvas id="runtime" width="1000" height="390"></canvas>
  </div>

  <div class="panel">
    <h2>Measured results</h2>
    <table>
      <thead>
        <tr><th>n</th><th>Comparisons</th><th>Swaps</th><th>Time (s)</th><th>Time vs previous</th></tr>
      </thead>
      <tbody id="rows"></tbody>
    </table>
    <p class="note">Exact milliseconds vary by computer. The important story is the growth pattern.</p>
  </div>

  <div class="panel">
    <h2>Class question</h2>
    <p class="big">If we multiply n by 10, should Bubble Sort take about 10× longer or closer to 100× longer?</p>
    <p>Bubble Sort performs about n² work in the worst case. Hardware changes the stopwatch. It does not change that growth shape.</p>
  </div>
</main>

<script>
const data = {data_json};

function fmt(n) {{
  return Number(n).toLocaleString();
}}

function table() {{
  const body = document.getElementById('rows');
  body.innerHTML = '';
  data.forEach((r, i) => {{
    const prev = i ? data[i - 1].seconds : null;
    const multiple = prev ? (r.seconds / prev).toFixed(1) + '×' : '—';
    const tr = document.createElement('tr');
    tr.innerHTML =
      '<td>' + fmt(r.n) + '</td>' +
      '<td>' + fmt(r.comparisons) + '</td>' +
      '<td>' + fmt(r.swaps) + '</td>' +
      '<td>' + r.seconds.toFixed(6) + '</td>' +
      '<td>' + multiple + '</td>';
    body.appendChild(tr);
  }});
}}

function draw() {{
  const canvas = document.getElementById('runtime');
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  const L = 90, R = 35, T = 35, B = 70;
  ctx.clearRect(0, 0, W, H);

  const maxY = Math.max(...data.map(d => d.seconds));
  const safeMax = maxY || 1;

  ctx.strokeStyle = '#8a94a6';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(L, T);
  ctx.lineTo(L, H - B);
  ctx.lineTo(W - R, H - B);
  ctx.stroke();

  ctx.fillStyle = '#465266';
  ctx.font = '16px system-ui';
  ctx.textAlign = 'center';

  const usableW = W - L - R;
  const usableH = H - T - B;
  const step = usableW / data.length;
  const barW = step * 0.56;

  data.forEach((d, i) => {{
    const x = L + step * i + (step - barW) / 2;
    const h = Math.max(2, (d.seconds / safeMax) * usableH);
    const y = H - B - h;

    ctx.fillStyle = '#4059ad';
    ctx.fillRect(x, y, barW, h);

    ctx.fillStyle = '#263247';
    ctx.textAlign = 'center';
    ctx.fillText(fmt(d.n), x + barW / 2, H - B + 28);

    ctx.save();
    ctx.translate(x + barW / 2, Math.max(T + 18, y - 8));
    ctx.fillText(d.seconds.toFixed(4) + ' s', 0, 0);
    ctx.restore();
  }});

  ctx.save();
  ctx.translate(22, T + usableH / 2);
  ctx.rotate(-Math.PI / 2);
  ctx.textAlign = 'center';
  ctx.fillStyle = '#263247';
  ctx.fillText('Measured seconds', 0, 0);
  ctx.restore();

  ctx.textAlign = 'center';
  ctx.fillText('Input size n', L + usableW / 2, H - 18);
}}

table();
draw();
</script>
</body>
</html>
"""
    output_path.write_text(html, encoding="utf-8")


def main():
    print("BUBBLE SORT: WATCH QUADRATIC WORK GROW")
    print("=" * 76)
    print("Reverse-sorted input gives Bubble Sort its worst-case workout.")
    print("The 20,000 and 30,000 runs are intentionally heavy so you can watch one CPU core work in htop.")
    print()

    results = []

    for n in SIZES:
        values = list(range(n, 0, -1))

        start = time.perf_counter()
        comparisons, swaps = bubble_sort(values)
        seconds = time.perf_counter() - start

        assert values == list(range(1, n + 1))

        row = {
            "n": n,
            "comparisons": comparisons,
            "swaps": swaps,
            "seconds": seconds,
        }
        results.append(row)

        print(
            f"n={n:>6,} | "
            f"comparisons={comparisons:>12,} | "
            f"swaps={swaps:>12,} | "
            f"time={seconds:>10.6f} s"
        )

    print()
    print("TIME GROWTH")
    print("-" * 76)
    for previous, current in zip(results, results[1:]):
        if previous["seconds"] > 0:
            multiplier = current["seconds"] / previous["seconds"]
            print(
                f"{previous['n']:>6,} -> {current['n']:>6,}: "
                f"{multiplier:>8.2f}x measured time"
            )

    websites_dir = Path(__file__).resolve().parent.parent / "websites"
    output_path = websites_dir / "04b_bubble_sort_measured.html"
    write_html(results, output_path)

    print()
    print("=" * 76)
    print("GRAPH WRITTEN TO:")
    print(output_path)
    print()
    print("STUDENT QUESTION:")
    print("When n grows by 10x, why does the work trend toward roughly 100x?")


if __name__ == "__main__":
    main()
