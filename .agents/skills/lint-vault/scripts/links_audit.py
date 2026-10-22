#!/usr/bin/env python3
"""Read-only wikilink and relative-link audit for a Second Brain vault.

Usage: python3 links_audit.py [vault-root]

Prints TSV lines (ERROR|WARNING|INFO<TAB>category<TAB>note<TAB>message) followed by a SUMMARY line.
Error categories:
  wikilink-unresolved      [[target]] in a body or frontmatter resolves to no canonical note by exact
                           vault-relative path stem or unique filename stem
  wikilink-ambiguous       filename stem shared by several notes and no exact path stem given
Warning categories:
  wikilink-non-portable    target matches no stem but matches a note's first H1; the stem is suggested
  markdown-link-missing    relative Markdown link [text](path) whose file does not exist
  relationship-value       frontmatter relationship value that is not a wikilink
  relationship-unquoted    frontmatter wikilink without quotes, which YAML parses as a nested list
Info: links-checked totals (wikilinks by location, Markdown links, relationship values).

Canonical notes exclude `.git`, `.agents`, `.local`, `attachments`, caches and `.tmp`, so links into
those trees are reported. Fenced code blocks and inline code spans are stripped before a body is
scanned, so illustrative placeholders such as `[[project-stem]]` inside them are never reported.
Frontmatter is scanned separately: every wikilink there must resolve, and relationship keys
(belongs_to, related_to, has, surface_for, wraps, based_on, superseded_by, plus any key whose value
is a wikilink or a list of them) must hold only wikilinks. Wikilink targets may carry `|label`
and `#heading`; a `.md` suffix is tolerated.
Standard library only; the script never writes. Exit status is 1 when errors were found, so a
deployment can require link validation to pass.
"""
from __future__ import annotations
import re, sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

EXCLUDE = {".git", ".agents", ".local", "attachments", ".tolaria-cache", ".cache", "node_modules", ".tmp", ".roughdraft-assets"}
RELATIONSHIP_KEYS = {"belongs_to", "related_to", "has", "surface_for", "wraps", "based_on", "superseded_by"}
WIKILINK = re.compile(r"\[\[([^\]]*?)\]\]")
MD_LINK = re.compile(r"(?<!\\)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CODE_SPAN = re.compile(r"(`+)(?!`)(.+?)(?<!`)\1(?!`)")
FENCE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
H1 = re.compile(r"(?m)^#[ \t]+(.+?)[ \t]*$")


def canonical(root: Path):
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root)
        if any(part in EXCLUDE for part in rel.parts):
            continue
        yield p


def split(text: str):
    """Return (frontmatter, body, body_line_offset)."""
    if not text.startswith("---\n"):
        return "", text, 0
    end = text.find("\n---", 4)
    if end == -1:
        return "", text, 0
    fm = text[4:end]
    body_start = text.find("\n", end + 1)
    body = text[body_start + 1:] if body_start != -1 else ""
    return fm, body, fm.count("\n") + 3


def strip_code(body: str) -> str:
    """Blank fenced blocks and inline code spans, keeping line numbers stable."""
    out, fence = [], None
    for line in body.split("\n"):
        m = FENCE.match(line)
        if fence is None and m:
            fence = m.group(1)
            out.append("")
            continue
        if fence is not None:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and line.strip() == m.group(1):
                fence = None
            out.append("")
            continue
        out.append(CODE_SPAN.sub(lambda s: " " * len(s.group(0)), line))
    return "\n".join(out)


def target_of(inner: str) -> str:
    t = inner.split("|", 1)[0].split("#", 1)[0].strip()
    if t.endswith(".md"):
        t = t[:-3]
    return t.strip("/")


def strip_comment(value: str) -> str:
    """Drop a trailing YAML comment outside quotes."""
    v = value.strip()
    if v[:1] in ("'", '"'):
        q = v[0]
        close = v.find(q, 1)
        return v[: close + 1] if close != -1 else v
    if v.startswith("#"):
        return ""
    return re.split(r"\s+#", v, maxsplit=1)[0].strip()


def frontmatter_entries(fm: str):
    """Yield (key, value, form) for top-level scalars ('scalar') and list items ('item'); comments and empty values skipped."""
    key = None
    for line in fm.split("\n"):
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*)$", line)
        if m:
            key, value = m.group(1), strip_comment(m.group(2))
            if value.startswith("#") or value in ("", "[]", "~", "null"):
                continue
            if value.startswith("[") and value.endswith("]") and not value.startswith("[["):
                for item in re.findall(r"""'[^']*'|"[^"]*"|[^,\s][^,]*""", value[1:-1]):
                    item = item.strip()
                    if item:
                        yield key, item, "item"
                continue
            yield key, value, "scalar"
            continue
        m = re.match(r"^[ \t]*-[ \t]+(.*)$", line)
        if m and key:
            value = strip_comment(m.group(1))
            if value:
                yield key, value, "item"


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = Path(args[0] if args else ".").expanduser().resolve()
    notes = {}
    for p in canonical(root):
        notes[str(p.relative_to(root))[:-3]] = p
    by_name = defaultdict(list)
    for stem in notes:
        by_name[stem.split("/")[-1]].append(stem)
    titles = {}
    for stem, p in notes.items():
        fm, body, _ = split(p.read_text(encoding="utf-8"))
        m = H1.search(body)
        if m:
            titles.setdefault(m.group(1).strip().lower(), []).append(stem)

    def resolve(target: str):
        """Return ('ok', stem) | ('ambiguous', [stems]) | ('title', [stems]) | ('none', None)."""
        if target in notes:
            return "ok", target
        c = by_name.get(target.split("/")[-1], []) if "/" not in target else []
        if len(c) == 1:
            return "ok", c[0]
        if len(c) > 1:
            return "ambiguous", c
        t = titles.get(target.lower())
        if t:
            return "title", t
        return "none", None

    errors, warnings = [], []
    counts = defaultdict(int)

    def check_wikilink(stem: str, inner: str, where: str):
        target = target_of(inner)
        if not target:
            return
        status, found = resolve(target)
        if status == "ok":
            return
        link = f"[[{inner}]]"
        if status == "ambiguous":
            errors.append(("wikilink-ambiguous", stem, f"{link} ({where}) matches several notes: {', '.join(found)}; use a vault-relative path stem"))
        elif status == "title" and len(found) > 1:
            errors.append(("wikilink-ambiguous", stem, f"{link} ({where}) matches the title of several notes: {', '.join(found)}; use a vault-relative path stem"))
        elif status == "title":
            warnings.append(("wikilink-non-portable", stem, f"{link} ({where}) resolves only by title; use [[{found[0]}]]"))
        else:
            errors.append(("wikilink-unresolved", stem, f"{link} ({where}) resolves to no note"))

    for stem, p in sorted(notes.items()):
        fm, body, offset = split(p.read_text(encoding="utf-8"))
        relationship_keys = set(RELATIONSHIP_KEYS)
        entries = list(frontmatter_entries(fm))
        relationship_keys.update(k for k, v, _ in entries if WIKILINK.search(v))
        for key, value, form in entries:
            for m in WIKILINK.finditer(value):
                counts["frontmatter-wikilinks"] += 1
                check_wikilink(stem, m.group(1), f"frontmatter {key}")
            if key in relationship_keys:
                counts["relationship-values"] += 1
                if re.fullmatch(r"""(['"])\[\[[^\]]+\]\]\1""", value):
                    continue
                if re.fullmatch(r"\[\[[^\]]+\]\]", value):
                    warnings.append(("relationship-unquoted", stem, f"{key}: {value} is an unquoted wikilink, which YAML reads as a nested list; quote it"))
                    continue
                bare = value.strip("'\"")
                status, found = resolve(target_of(bare)) if bare and not bare.startswith("[") else ("none", None)
                hint = f"; plain stem resolves to {found}, quote it as a wikilink" if status == "ok" else " and resolves to no note"
                warnings.append(("relationship-value", stem, f"{key}: {value!r} is not a quoted wikilink{hint}"))
        clean = strip_code(body)
        for i, line in enumerate(clean.split("\n"), start=offset + 1):
            for m in WIKILINK.finditer(line):
                counts["body-wikilinks"] += 1
                check_wikilink(stem, m.group(1), f"line {i}")
            for m in MD_LINK.finditer(line):
                href = m.group(1)
                if href.startswith(("#", "<")) or SCHEME.match(href) or href.startswith("/"):
                    continue
                counts["markdown-links"] += 1
                rel = unquote(href.split("#", 1)[0].split("?", 1)[0])
                if not rel:
                    continue
                if not (p.parent / rel).exists():
                    hint = "; add .md to link the note" if not Path(rel).suffix and (p.parent / (rel + ".md")).exists() else ""
                    warnings.append(("markdown-link-missing", stem, f"({href}) (line {i}) points to a file that does not exist{hint}"))

    for cat, note, msg in errors:
        print(f"ERROR\t{cat}\t{note}.md\t{msg}")
    for cat, note, msg in warnings:
        print(f"WARNING\t{cat}\t{note}.md\t{msg}")
    print("INFO\tlinks-checked\t-\t" + ", ".join(f"{k}={counts[k]}" for k in ("body-wikilinks", "frontmatter-wikilinks", "markdown-links", "relationship-values")))
    by_cat = defaultdict(int)
    for cat, _, _ in errors + warnings:
        by_cat[cat] += 1
    print("SUMMARY\t" + "\t".join(f"{k}={v}" for k, v in sorted(by_cat.items())) + f"\terrors={len(errors)}\twarnings={len(warnings)}\tinfo=1\tnotes={len(notes)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
