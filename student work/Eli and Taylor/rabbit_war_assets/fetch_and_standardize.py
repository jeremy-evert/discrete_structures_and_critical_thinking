import io, json, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).parent
OUT = ROOT / "images"
OUT.mkdir(exist_ok=True)
items = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

for item in items:
    url = item.get("source_url")
    dest = ROOT / item["file"]
    if dest.exists() or not url:
        continue
    req = urllib.request.Request(url, headers={"User-Agent": "rabbit-war-reference-pack/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        data = response.read()
    image = Image.open(io.BytesIO(data)).convert("RGB")
    image.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (1024, 1024), "white")
    canvas.paste(image, ((1024-image.width)//2, (1024-image.height)//2))
    canvas.save(dest, "JPEG", quality=90, optimize=True)
    print("saved", dest)
