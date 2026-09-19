#!/usr/bin/env python3
"""Static validation for the site, since Jekyll will not build locally.

Checks front matter, permalink uniqueness, internal link targets, image/video
paths, the cross-link graph, and the inline-math delimiter rule.
"""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(".")
COLLECTIONS = ["_pages", "_projects", "_publications", "_talks", "_teaching"]
problems, notes = [], []


def front_matter(text):
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    fm = {}
    for line in parts[1].split("\n"):
        m = re.match(r"^([a-z_]+)\s*:\s*(.*)$", line.strip())
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("\"'")
    return fm


files = []
for c in COLLECTIONS:
    files += sorted(Path(c).glob("*.md")) + sorted(Path(c).glob("*.html"))

permalinks = defaultdict(list)
known_urls = set()

for f in files:
    text = f.read_text(encoding="utf-8")
    fm = front_matter(text)
    if fm is None:
        problems.append(f"{f}: no front matter")
        continue
    if "description" not in fm and f.name != "404.md":
        problems.append(f"{f}: missing `description:` front matter (style guide §11)")
    if "date" in fm and not re.match(r"^\d{4}-\d{2}-\d{2}$", fm["date"]):
        problems.append(f"{f}: date `{fm['date']}` is not ISO")
    # derive url
    if "permalink" in fm:
        url = fm["permalink"]
    else:
        coll = f.parent.name.lstrip("_")
        url = f"/{coll}/{f.stem}"
    permalinks[url.rstrip("/") or "/"].append(str(f))
    known_urls.add(url.rstrip("/") or "/")

for url, srcs in permalinks.items():
    if len(srcs) > 1:
        problems.append(f"duplicate permalink {url}: {', '.join(srcs)}")

# internal links and assets (HTML comments are not rendered, so skip them)
for f in files:
    text = re.sub(r"<!--.*?-->", "", f.read_text(encoding="utf-8"), flags=re.S)
    for m in re.finditer(r"\]\((/[^)#\s]*)", text):
        target = m.group(1).rstrip("/") or "/"
        if target.startswith(("/images/", "/files/", "/assets/")):
            if not (ROOT / target.lstrip("/")).exists():
                problems.append(f"{f}: missing asset {target}")
        elif target not in known_urls:
            problems.append(f"{f}: internal link to unknown page {target}")
    for m in re.finditer(r'(?:src|poster)="(/[^"]+)"', text):
        if not (ROOT / m.group(1).lstrip("/")).exists():
            problems.append(f"{f}: missing media {m.group(1)}")
    # inline math delimiter rule
    for m in re.finditer(r"(?<!\$)\$(?!\$)[^$\n]{1,80}\$(?!\$)", text):
        problems.append(f"{f}: single-$ math span {m.group(0)!r} (style guide §11)")
    # reference anchors resolve
    cited = set(re.findall(r"\]\(#(ref-\d+)\)", text))
    defined = set(re.findall(r'<a id="(ref-\d+)">', text))
    for c in sorted(cited - defined):
        problems.append(f"{f}: citation links to #{c} with no anchor")
    for d in sorted(defined - cited):
        notes.append(f"{f}: reference #{d} defined but never cited")

# cross-link graph (style guide §11)
EDGES = {
    "_publications/2023-relational.md": ["/publication/2023-icdl-scaffolding", "/projects/intrinsic_curiosity"],
    "_publications/2023-icdl-scaffolding.md": ["/publication/2023-relational", "/projects/intrinsic_curiosity"],
    "_projects/intrinsic_curiosity.md": ["/publication/2023-relational", "/publication/2023-icdl-scaffolding"],
}
for src, targets in EDGES.items():
    text = Path(src).read_text(encoding="utf-8")
    for t in targets:
        if t not in text:
            problems.append(f"CROSS-LINK BROKEN: {src} no longer links to {t}")

print(f"{len(files)} content files checked\n")
if problems:
    print("PROBLEMS")
    for p in problems:
        print("  -", p)
else:
    print("PROBLEMS: none")
if notes:
    print("\nNOTES")
    for n in notes:
        print("  -", n)
