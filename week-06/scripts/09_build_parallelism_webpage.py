#!/usr/bin/env python3
"""Build the self-contained Week 6 parallelism classroom webpage from measured CSV."""

import argparse
import csv
import json
from pathlib import Path

LABELS = {
    "cpu_sequential": "CPU sequential",
    "cpu_parallel": "CPU parallel",
    "gpu_sort_only": "GPU sort only",
    "gpu_end_to_end": "GPU end-to-end",
}

COLORS = {
    "cpu_sequential": "#334155",
    "cpu_parallel": "#2563eb",
    "gpu_sort_only": "#16a34a",
    "gpu_end_to_end": "#dc2626",
}


def read_metadata(path):
    data = {}
    p = Path(path)
    if not p.exists():
        return data
    for line in p.read_text(errors="replace").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            data[key.strip()] = value.strip()
    return data


def read_rows(path):
    p = Path(path)
    if not p.exists():
        return []

    rows = []
    with p.open(newline="") as file:
        for row in csv.DictReader(file):
            rows.append({
                "backend": row["backend"],
                "n": int(row["n"]),
                "workers": int(row["workers"]),
                "median_ms": float(row["median_ms"]),
            })
    return rows


def first_crossover(rows, challenger):
    sequential = {
        row["n"]: row["median_ms"]
        for row in rows
        if row["backend"] == "cpu_sequential"
    }

    candidates = sorted(
        (
            row
            for row in rows
            if row["backend"] == challenger and row["n"] in sequential
        ),
        key=lambda row: row["n"],
    )

    for row in candidates:
        if row["median_ms"] < sequential[row["n"]]:
            return row["n"]

    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--metadata", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = read_rows(args.csv)
    metadata = read_metadata(args.metadata)

    cpu_crossover = first_crossover(rows, "cpu_parallel")
    gpu_crossover = first_crossover(rows, "gpu_end_to_end")

    payload = json.dumps(rows)
    metadata_json = json.dumps(metadata)
    labels_json = json.dumps(LABELS)
    colors_json = json.dumps(COLORS)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Week 6 — The Parallelism Plot Twist</title>
<style>
:root{{font-family:Inter,system-ui,sans-serif;color:#102033;background:#f6f8fb}}
body{{margin:0}}.wrap{{max-width:1200px;margin:auto;padding:32px}}
h1{{font-size:clamp(2.3rem,5vw,4.6rem);margin:.12em 0}}.sub{{font-size:1.28rem;color:#4b5b70;max-width:930px}}
.panel{{background:#fff;border:1px solid #dbe2ea;border-radius:18px;padding:22px;margin-top:22px;box-shadow:0 8px 24px #1b35520f}}
.hardware{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}}
.card{{background:#f2f5f9;border-radius:14px;padding:16px;min-height:84px}}.card b{{display:block;font-size:1.35rem;margin-top:5px}}
.controls{{display:flex;gap:18px;align-items:center;flex-wrap:wrap}}
button{{font:inherit;font-weight:800;border:0;border-radius:12px;padding:12px 18px;background:#102033;color:#fff;cursor:pointer}}
canvas{{width:100%;height:500px;margin-top:12px}}.note{{color:#607085}}.question{{font-size:1.5rem;font-weight:800}}
.reveal{{display:none;border-left:6px solid #102033;padding:4px 18px;margin-top:20px;background:#f6f8fb;border-radius:8px}}
.reveal.show{{display:block}}table{{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}}
th,td{{padding:9px 11px;border-bottom:1px solid #e3e8ef;text-align:right}}th:first-child,td:first-child{{text-align:left}}
.tablewrap{{overflow:auto}}.empty{{padding:24px;background:#fff7ed;border-radius:12px}}
@media(max-width:800px){{.hardware{{grid-template-columns:1fr}}.wrap{{padding:18px}}canvas{{height:420px}}}}
</style>
</head>
<body><div class="wrap">
<div>DSCT · Week 6 · Open #07</div>
<h1>But what if we just throw more cores at it?</h1>
<p class="sub">First we sort on one CPU worker. Then many CPU workers. Then, if CUDA is available, we tempt fate with a GPU. Make predictions before revealing what the machine actually did.</p>

<div class="panel">
<h2>The hardware bait</h2>
<div class="hardware" id="hardware"></div>
<p class="note">CPU cores and GPU execution units are not apples-to-apples. That is part of the reveal.</p>
</div>

<div class="panel">
<div class="controls">
<h2 style="margin-right:auto">Measured runtime</h2>
<label><input id="logY" type="checkbox"> log y-axis</label>
<label><input id="guide" type="checkbox" checked> show normalized n log₂n guide</label>
</div>
<div id="empty" class="empty" style="display:none">No benchmark data yet. Run <code>week-06/scripts/10_run_parallelism_showdown.sh</code>, then reopen this page.</div>
<canvas id="runtime" width="1140" height="500"></canvas>
<p class="note">x-axis is logarithmic because the experiment spans tiny inputs through millions of values. Times are medians from this machine, not universal constants.</p>
</div>

<div class="panel">
<h2>Speedup relative to one CPU worker</h2>
<canvas id="speedup" width="1140" height="450"></canvas>
<p class="note">1× means “no faster than the sequential CPU baseline.” Below 1× means the fancy parallel option actually lost.</p>
</div>

<div class="panel">
<h2>Measured data</h2>
<div class="tablewrap">
<table>
<thead><tr><th>Backend</th><th>n</th><th>Workers / SMs</th><th>Median ms</th><th>Speedup vs CPU sequential</th></tr></thead>
<tbody id="rows"></tbody>
</table>
</div>
</div>

<div class="panel">
<p class="question">The trap: “More parallel hardware means faster.” Does the evidence agree for every n?</p>
<button id="revealBtn">Reveal what is actually happening</button>
<div id="reveal" class="reveal">
<h2>Parallelism has a cover charge.</h2>
<p>Work must be divided, workers must start and synchronize, partial results must be coordinated, and GPU jobs may have to move data across the CPU/GPU boundary. For small inputs, that overhead can cost more than the work it saves.</p>
<p><strong>Then scale changes the answer.</strong> Once there is enough useful work, many workers can amortize that overhead and parallel hardware can pull ahead.</p>
<p><strong>And Big O never left the room.</strong> Parallel hardware can change constants and throughput dramatically, but input growth still matters. A constant-factor speedup does not make growth disappear. Better algorithms and parallelism solve different parts of the problem.</p>
</div>
</div>
</div>

<script>
const data={payload};
const meta={metadata_json};
const labels={labels_json};
const colors={colors_json};

function esc(s){{
  return String(s??'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
}}
function fmtN(n){{return Number(n).toLocaleString()}}
function fmtMs(v){{return v<0.01?v.toFixed(5):v<1?v.toFixed(3):v.toFixed(2)}}
function group(){{
  const g={{}};
  for(const r of data)(g[r.backend]??=[]).push(r);
  for(const k in g)g[k].sort((a,b)=>a.n-b.n);
  return g;
}}

const grouped=group();
const seq=Object.fromEntries((grouped.cpu_sequential||[]).map(r=>[r.n,r.median_ms]));

function hardware(){{
  const cpu=meta.cpu_model||'CPU detected by benchmark machine';
  const logical=meta.cpu_logical_threads||'?';
  const workers=meta.parallel_workers||((grouped.cpu_parallel||[])[0]?.workers??'?');
  const gpu=meta.gpu_name||'No CUDA GPU benchmarked';
  const sms=meta.gpu_sms||'—';

  document.getElementById('hardware').innerHTML=
    '<div class="card">CPU<b>'+esc(cpu)+'</b><span>'+esc(logical)+' logical processors</span></div>'+
    '<div class="card">Parallel CPU run<b>'+esc(workers)+' workers</b><span>GNU/OpenMP parallel sort</span></div>'+
    '<div class="card">GPU<b>'+esc(gpu)+'</b><span>'+esc(sms)+' streaming multiprocessors</span></div>';
}}

function drawRuntime(){{
  const c=document.getElementById('runtime');
  const ctx=c.getContext('2d');
  const W=c.width,H=c.height,p={{l:86,r:26,t:30,b:60}};

  ctx.clearRect(0,0,W,H);

  if(!data.length){{
    document.getElementById('empty').style.display='block';
    return;
  }}

  document.getElementById('empty').style.display='none';

  const allN=data.map(r=>r.n);
  const minN=Math.min(...allN),maxN=Math.max(...allN);
  const logY=document.getElementById('logY').checked;
  let values=data.map(r=>r.median_ms).filter(v=>v>0);
  let maxV=Math.max(...values),minV=Math.min(...values);

  if(document.getElementById('guide').checked && grouped.cpu_sequential?.length){{
    const last=grouped.cpu_sequential[grouped.cpu_sequential.length-1];
    const scale=last.median_ms/(last.n*Math.log2(last.n));

    for(const n of [...new Set(allN)]){{
      values.push(scale*n*Math.log2(Math.max(n,2)));
    }}

    maxV=Math.max(...values);
    minV=Math.min(...values.filter(v=>v>0));
  }}

  const X=n=>p.l+(Math.log10(n)-Math.log10(minN))/(Math.log10(maxN)-Math.log10(minN))*(W-p.l-p.r);
  const yMin=logY?Math.log10(minV*.75):0;
  const yMax=logY?Math.log10(maxV*1.25):maxV*1.08;
  const Y=v=>H-p.b-((logY?Math.log10(Math.max(v,minV*.5)):v)-yMin)/(yMax-yMin)*(H-p.t-p.b);

  ctx.font='15px system-ui';
  ctx.strokeStyle='#d9e1ea';
  ctx.fillStyle='#5c6d80';
  ctx.lineWidth=1;

  for(let i=0;i<=5;i++){{
    const yy=p.t+i*(H-p.t-p.b)/5;
    ctx.beginPath();
    ctx.moveTo(p.l,yy);
    ctx.lineTo(W-p.r,yy);
    ctx.stroke();
  }}

  for(const n of [...new Set(allN)].sort((a,b)=>a-b)){{
    ctx.fillText(fmtN(n),X(n)-18,H-p.b+26);
  }}

  for(const [backend,rows] of Object.entries(grouped)){{
    ctx.strokeStyle=colors[backend]||'#64748b';
    ctx.lineWidth=4;
    ctx.beginPath();

    rows.forEach((r,i)=>{{
      const x=X(r.n),y=Y(r.median_ms);
      i?ctx.lineTo(x,y):ctx.moveTo(x,y);
      ctx.fillRect(x-3,y-3,6,6);
    }});

    ctx.stroke();
  }}

  if(document.getElementById('guide').checked && grouped.cpu_sequential?.length){{
    const last=grouped.cpu_sequential[grouped.cpu_sequential.length-1];
    const scale=last.median_ms/(last.n*Math.log2(last.n));
    const ns=[...new Set(allN)].sort((a,b)=>a-b);

    ctx.strokeStyle='#94a3b8';
    ctx.lineWidth=2;
    ctx.setLineDash([7,7]);
    ctx.beginPath();

    ns.forEach((n,i)=>{{
      const x=X(n),y=Y(scale*n*Math.log2(Math.max(n,2)));
      i?ctx.lineTo(x,y):ctx.moveTo(x,y);
    }});

    ctx.stroke();
    ctx.setLineDash([]);
  }}

  let legendY=46;

  for(const backend of Object.keys(grouped)){{
    ctx.fillStyle=colors[backend]||'#64748b';
    ctx.fillText(labels[backend]||backend,W-230,legendY);
    legendY+=23;
  }}

  if(document.getElementById('guide').checked){{
    ctx.fillStyle='#64748b';
    ctx.fillText('normalized n log₂n guide',W-230,legendY);
  }}

  ctx.fillStyle='#334155';
  ctx.fillText('input size n (log scale)',p.l,H-14);
  ctx.fillText(logY?'runtime ms (log)':'runtime ms',p.l,20);
}}

function drawSpeedup(){{
  const c=document.getElementById('speedup');
  const ctx=c.getContext('2d');
  const W=c.width,H=c.height,p={{l:76,r:26,t:30,b:60}};

  ctx.clearRect(0,0,W,H);

  if(!data.length)return;

  const rows=data.filter(r=>r.backend!=='cpu_sequential'&&seq[r.n]);
  if(!rows.length)return;

  const minN=Math.min(...rows.map(r=>r.n));
  const maxN=Math.max(...rows.map(r=>r.n));
  const values=rows.map(r=>seq[r.n]/r.median_ms);
  const maxV=Math.max(1.2,...values)*1.08;

  const X=n=>p.l+(Math.log10(n)-Math.log10(minN))/(Math.log10(maxN)-Math.log10(minN))*(W-p.l-p.r);
  const Y=v=>H-p.b-(v/maxV)*(H-p.t-p.b);

  ctx.font='15px system-ui';
  ctx.strokeStyle='#d9e1ea';
  ctx.fillStyle='#5c6d80';
  ctx.lineWidth=1;

  for(let i=0;i<=5;i++){{
    const yy=p.t+i*(H-p.t-p.b)/5;
    ctx.beginPath();
    ctx.moveTo(p.l,yy);
    ctx.lineTo(W-p.r,yy);
    ctx.stroke();
  }}

  ctx.strokeStyle='#111827';
  ctx.lineWidth=2;
  ctx.setLineDash([7,7]);
  ctx.beginPath();
  ctx.moveTo(p.l,Y(1));
  ctx.lineTo(W-p.r,Y(1));
  ctx.stroke();
  ctx.setLineDash([]);
  ctx.fillStyle='#111827';
  ctx.fillText('1× break-even',p.l+8,Y(1)-8);

  const by={{}};

  for(const r of rows)(by[r.backend]??=[]).push(r);

  for(const [backend,backendRows] of Object.entries(by)){{
    backendRows.sort((a,b)=>a.n-b.n);
    ctx.strokeStyle=colors[backend]||'#64748b';
    ctx.lineWidth=4;
    ctx.beginPath();

    backendRows.forEach((r,i)=>{{
      const x=X(r.n),y=Y(seq[r.n]/r.median_ms);
      i?ctx.lineTo(x,y):ctx.moveTo(x,y);
      ctx.fillRect(x-3,y-3,6,6);
    }});

    ctx.stroke();
  }}

  for(const n of [...new Set(rows.map(r=>r.n))].sort((a,b)=>a-b)){{
    ctx.fillText(fmtN(n),X(n)-18,H-p.b+26);
  }}

  ctx.fillStyle='#334155';
  ctx.fillText('input size n (log scale)',p.l,H-14);
  ctx.fillText('speedup ×',p.l,20);
}}

function table(){{
  let out='';

  for(const r of data.slice().sort((a,b)=>a.n-b.n||a.backend.localeCompare(b.backend))){{
    const speed=seq[r.n]?seq[r.n]/r.median_ms:null;

    out+='<tr>'+
      '<td>'+esc(labels[r.backend]||r.backend)+'</td>'+
      '<td>'+fmtN(r.n)+'</td>'+
      '<td>'+r.workers+'</td>'+
      '<td>'+fmtMs(r.median_ms)+'</td>'+
      '<td>'+(speed?speed.toFixed(2)+'×':'1.00×')+'</td>'+
      '</tr>';
  }}

  document.getElementById('rows').innerHTML=out;
}}

hardware();
table();
drawRuntime();
drawSpeedup();

document.getElementById('logY').onchange=drawRuntime;
document.getElementById('guide').onchange=drawRuntime;
document.getElementById('revealBtn').onclick=()=>document.getElementById('reveal').classList.toggle('show');
</script>
</body>
</html>"""

    Path(args.output).write_text(html)

    print(f"Wrote {args.output}")

    if cpu_crossover is not None:
        print(f"CPU parallel first beat CPU sequential at n={cpu_crossover:,}")
    else:
        print("CPU parallel never beat CPU sequential in the tested sizes.")

    if any(row["backend"] == "gpu_end_to_end" for row in rows):
        if gpu_crossover is not None:
            print(f"GPU end-to-end first beat CPU sequential at n={gpu_crossover:,}")
        else:
            print("GPU end-to-end never beat CPU sequential in the tested sizes.")


if __name__ == "__main__":
    main()
