#!/usr/bin/env python3
"""Count body-prose words per the style guide, section 6.

Excluded: front matter, the Abstract section, figure/table captions, code and
prompt blocks, BibTeX, reference lists, HTML comments, block-level raw HTML,
and Markdown tables. Inline links and inline math are kept as prose.
"""
import re
import sys
from pathlib import Path

SKIP_SECTIONS = ("abstract", "references", "bibtex", "citation")
BLOCK = r"div|video|iframe|pre|style|figure|table|ul|ol|blockquote"


def body_prose(text: str, verbose=False):
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    out, in_fence, in_comment, depth, section, in_para = [], False, False, 0, "", False
    for line in text.split("\n"):
        s = line.strip()

        if in_comment:
            if "-->" in s:
                in_comment = False
            continue
        if s.startswith("<!--"):
            if "-->" not in s:
                in_comment = True
            continue

        if re.match(r"^(```|~~~)", s):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        # block-level raw HTML: only when the line begins with a tag
        if depth > 0 or re.match(rf"^</?({BLOCK})\b", s):
            depth += len(re.findall(rf"<({BLOCK})\b", s))
            depth -= len(re.findall(rf"</({BLOCK})>", s))
            depth -= len(re.findall(rf"<({BLOCK})\b[^>]*/>", s))
            depth = max(depth, 0)
            # prose laid out in two columns still counts; italic <p> are captions
            if in_para and not re.match(r"^</?p\b", s):
                out.append(s)
            if re.match(r"^<p\b", s) and "font-style: italic" not in s:
                in_para = True
            if "</p>" in s:
                in_para = False
            continue
        # self-closing / void block tags on their own line
        if re.match(r"^<(img|source|br|hr|a)\b", s):
            continue

        m = re.match(r"^#{1,6}\s+(.*)", s)
        if m:
            section = m.group(1).strip().lower().rstrip(":")
            continue
        if section.startswith(SKIP_SECTIONS):
            continue

        if s.startswith("|") or re.match(r"^\|?\s*:?-{3,}", s):
            continue
        if not s:
            continue
        out.append(s)

    prose = "\n".join(out)
    prose = re.sub(r"\$\$.+?\$\$", "x", prose)
    prose = re.sub(r"\[\\?\[?\d+\\?\]?\]\(#ref-\d+\)", "", prose)
    prose = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", prose)
    prose = re.sub(r"</?[a-z][^>]*>", "", prose)
    prose = re.sub(r"[*_`>]", "", prose)
    if verbose:
        print(prose)
        print("=" * 60)
    return len([w for w in prose.split() if re.search(r"\w", w)])


TARGETS = {
    "_projects/intrinsic_curiosity.md": 1800,
    "_publications/2023-icdl-scaffolding.md": 900,
    "_publications/2023-relational.md": 800,
    "_projects/correspondence_learning.md": 600,
    "_projects/evolutionary.md": 600,
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for p in sys.argv[1:]:
            print(p, body_prose(Path(p).read_text(encoding="utf-8"), verbose=True))
    else:
        for p, target in TARGETS.items():
            n = body_prose(Path(p).read_text(encoding="utf-8"))
            flag = "ok" if n <= target * 1.05 else f"OVER by {n - target}"
            print(f"{p:45s} {n:5d}   target {target:5d}   {flag}")
