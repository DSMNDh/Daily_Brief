"""Build the Mamee Intelligence Brief dashboard (index.html) from data/briefing.csv.

Run: python3 build_dashboard.py
The template is dashboard/template.html. Data is embedded so the page works
on GitHub Pages without a backend.
"""
import csv, json, pathlib

root = pathlib.Path(__file__).resolve().parent
rows = list(csv.DictReader(open(root / "data" / "briefing.csv", encoding="utf-8")))
template = (root / "dashboard" / "template.html").read_text(encoding="utf-8")

payload = json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")
shim = ("<script>window.dash={data:function(){return {status:'ok',data:"
        + payload + "}},onData:function(fn){fn()}};</script>")

html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="claude:viewport-fit-sides" content="cover">'
        '<title>Mamee Intelligence Brief</title></head>'
        '<body style="margin:0;padding:16px;background:#07090F;min-height:100vh">'
        + shim + template + '</body></html>')
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html written with {len(rows)} rows")
