#!/usr/bin/env python3
"""Read-only belongs_to hierarchy audit for a Second Brain vault.

Usage: python3 hierarchy_audit.py [vault-root] [--tree]

Prints TSV lines (WARNING|INFO<TAB>category<TAB>note<TAB>message) followed by a SUMMARY line.
Warning categories:
  belongs-to-cycle      ERROR: a belongs_to chain loops back on itself
  topic-root-unflagged  a Topic with no belongs_to roots other notes without hierarchy_root: true
  root-not-responsibility a Note, Concept, Person, Source or Event with no belongs_to roots other notes
  project-parent        active Project without belongs_to, or parented by a Topic not flagged hierarchy_root
  homeless              durable note whose belongs_to chain reaches no Project/Responsibility/Topic
  has-only              note reachable only through an inverse `has` link
  multi-parent          note with two parent hubs at the same distance (flagged accepted cases are INFO)
  non-hub-parent        Note/Concept/Person/Source/Event parenting >= 3 notes while reaching no hub itself
  related-only-cluster  three or more related_to-only notes sharing a first related_to target
  hierarchy-root        `hierarchy_root: true` set on a note that is not a Topic
Info categories: person-no-affiliation, non-hub-parent (parent rolls up), multi-parent (accepted),
  hierarchy-root (each Topic deliberately allowed to root an area).
Exempt from homeless: Recap, Guide, Type, Operation, archived notes, root hubs, and Inbox notes
  (`_organized: false` or `status: Unprocessed`), whose home Process Inbox has not yet decided.

Deliberate exceptions live in the frontmatter of the note concerned, so the script carries no vault names:
  hierarchy_root: true          on a Topic allowed to root an area (recorded in the vault's hierarchy ADR)
  accepted_double_parent: true  on a note allowed two parents at the same distance
  hierarchy_exempt: true        on a Type definition note whose notes sit outside the hierarchy by design, like Recaps
Standard library only; the script never writes.
"""
from __future__ import annotations
import re, sys
from collections import defaultdict
from pathlib import Path

EXCLUDE = {".git", ".agents", ".local", "attachments", ".tolaria-cache", ".cache", "node_modules", ".tmp", ".roughdraft-assets"}
HUBS = {"Project", "Responsibility", "Topic"}
EXEMPT = {"Recap", "Guide", "Type", "Operation"}
LINK = re.compile(r"\[\[([^\]|#]+)")


def canonical(root: Path):
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root)
        if any(part in EXCLUDE for part in rel.parts):
            continue
        yield p


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def key_block(fm: str, key: str) -> str:
    m = re.search(rf"(?ms)^{key}:[ \t]*(.*?)(?=^[A-Za-z_]|\Z)", fm)
    return m.group(1) if m else ""


def links(fm: str, key: str):
    return [t.strip().removesuffix(".md") for t in LINK.findall(key_block(fm, key))]


def scalar(fm: str, key: str):
    m = re.search(rf"(?m)^{key}:[ \t]*['\"]?([^'\"\n]+)", fm)
    return m.group(1).strip() if m else None


def flag(fm: str, key: str) -> bool:
    return (scalar(fm, key) or "").lower() == "true"


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = Path(args[0] if args else ".").expanduser().resolve()
    show_tree = "--tree" in sys.argv
    notes = {}
    for p in canonical(root):
        fm = frontmatter(p.read_text(encoding="utf-8"))
        stem = str(p.relative_to(root))[:-3]
        notes[stem] = {
            "type": scalar(fm, "type") or "",
            "archived": flag(fm, "_archived"),
            "inbox": (scalar(fm, "_organized") or "").lower() == "false" or (scalar(fm, "status") or "") == "Unprocessed",
            "hierarchy_root": flag(fm, "hierarchy_root"),
            "hierarchy_exempt": flag(fm, "hierarchy_exempt"),
            "title": (re.search(r"(?m)^# (.+)$", p.read_text(encoding="utf-8")) or [None, stem])[1].strip() if re.search(r"(?m)^# (.+)$", p.read_text(encoding="utf-8")) else stem,
            "accepted_double_parent": flag(fm, "accepted_double_parent"),
            "belongs_to": links(fm, "belongs_to"),
            "related_to": links(fm, "related_to"),
            "has": links(fm, "has"),
        }
    by_name = defaultdict(list)
    for stem in notes:
        by_name[stem.split("/")[-1]].append(stem)

    def resolve(target: str):
        if target in notes:
            return target
        c = by_name.get(target.split("/")[-1], [])
        return c[0] if len(c) == 1 else None

    # Types whose definition note carries `hierarchy_exempt: true` sit outside the hierarchy, like Recaps.
    exempt = set(EXEMPT)
    for stem, n in notes.items():
        if n["type"] == "Type" and n["hierarchy_exempt"]:
            exempt.add(n["title"])

    strong, both = defaultdict(list), defaultdict(list)
    self_refs = []
    for stem, n in notes.items():
        for t in n["belongs_to"]:
            r = resolve(t)
            if r == stem:
                self_refs.append(stem)
            elif r:
                strong[stem].append((r, "belongs_to")); both[stem].append((r, "belongs_to"))
        for t in n["has"]:
            r = resolve(t)
            if r and r != stem:
                both[r].append((stem, "has"))

    def is_hub(s):
        return notes[s]["type"] in HUBS

    def walk(stem, parents):
        seen, frontier, fallback = {stem}, [(stem, [])], None
        for _ in range(8):
            nxt = []
            for s, path in frontier:
                for p, via in parents.get(s, []):
                    if p not in seen:
                        seen.add(p); nxt.append((p, path + [f"{via}->{p}"]))
            hubs = [x for x in nxt if is_hub(x[0])]
            projects = [x for x in hubs if notes[x[0]]["type"] == "Project"]
            if projects:
                return projects[0][0], projects[0][1], [x[0] for x in projects[1:]]
            if hubs and fallback is None:
                fallback = (hubs[0][0], hubs[0][1], [x[0] for x in hubs[1:]])
            frontier = nxt
            if not frontier:
                break
        return fallback

    warnings, infos, errors = [], [], []
    for stem, n in sorted(notes.items()):
        if not n["hierarchy_root"]:
            continue
        if n["type"] == "Topic":
            infos.append(("hierarchy-root", stem, "Topic deliberately allowed to root an area (hierarchy_root: true)"))
        else:
            warnings.append(("hierarchy-root", stem, f"hierarchy_root is only meaningful on a Topic, not a {n['type'] or 'note without type'}"))

    homes = {}
    for stem, n in notes.items():
        if n["type"] == "Type":
            continue
        h = walk(stem, strong) or walk(stem, both)
        homes[stem] = h
        if n["type"] == "Project" and not n["archived"]:
            if not n["belongs_to"]:
                warnings.append(("project-parent", stem, "Project has no belongs_to"))
            elif h and notes[h[0]]["type"] == "Topic" and not notes[h[0]]["hierarchy_root"]:
                warnings.append(("project-parent", stem, f"Project parent is a Topic: {h[0]}"))
        if h is None:
            if n["type"] in exempt or n["archived"] or n["inbox"] or (is_hub(stem) and n["type"] != "Project"):
                continue
            if n["type"] == "Person":
                infos.append(("person-no-affiliation", stem, "Person without belongs_to; fine when no affiliation hub exists"))
            elif n["type"] != "Project":
                warnings.append(("homeless", stem, f"{n['type']} reaches no Project/Responsibility/Topic"))
        else:
            hub, path, alts = h
            if any(step.startswith("has->") for step in path):
                warnings.append(("has-only", stem, f"reaches {hub} only via {' / '.join(path)}"))
            if alts:
                msg = f"{hub} and {', '.join(alts)} at the same distance"
                if n["accepted_double_parent"]:
                    infos.append(("multi-parent", stem, msg + " (accepted_double_parent: true)"))
                else:
                    warnings.append(("multi-parent", stem, msg))

    # belongs_to cycles and chain roots: every chain must end at a Responsibility or a Topic flagged hierarchy_root.
    cycles = set()
    roots_of = {}

    def chain_roots(stem, path):
        if stem in roots_of:
            return roots_of[stem]
        if stem in path:
            cycles.add(tuple(path[path.index(stem):]))
            return set()
        parents = [p for p, _ in strong.get(stem, [])]
        if not parents:
            roots_of[stem] = {stem}
            return roots_of[stem]
        out = set()
        for p in parents:
            out |= chain_roots(p, path + [stem])
        roots_of[stem] = out
        return out

    for stem in notes:
        chain_roots(stem, [])
    for stem in sorted(self_refs):
        errors.append(("belongs-to-cycle", stem, "belongs_to points at the note itself"))
    for cyc in sorted(cycles):
        errors.append(("belongs-to-cycle", cyc[0], "belongs_to chain loops: " + " -> ".join(cyc + (cyc[0],))))
    bad_roots = defaultdict(int)
    for stem, n in notes.items():
        if n["type"] in exempt or n["archived"] or n["inbox"] or not n["belongs_to"]:
            continue
        for r in roots_of.get(stem, ()):
            if r == stem:
                continue
            rt = notes[r]["type"]
            if rt == "Responsibility" or (rt == "Topic" and notes[r]["hierarchy_root"]) or rt == "Project":
                continue  # a parentless Project is already reported as project-parent
            bad_roots[r] += 1
    for r, k in sorted(bad_roots.items()):
        rt = notes[r]["type"] or "untyped note"
        if rt == "Topic":
            warnings.append(("topic-root-unflagged", r, f"Topic is the root of {k} note(s) but has no belongs_to and no hierarchy_root: true; give it a parent or flag it"))
        else:
            warnings.append(("root-not-responsibility", r, f"{rt} is the root of {k} note(s); belongs_to chains should end at a Responsibility"))

    children = defaultdict(int)
    for stem, n in notes.items():
        for t in n["belongs_to"]:
            r = resolve(t)
            if r:
                children[r] += 1
    for parent, k in sorted(children.items()):
        if parent in notes and not is_hub(parent) and k >= 3:
            msg = f"{notes[parent]['type']} is belongs_to parent of {k} notes"
            if homes.get(parent):
                infos.append(("non-hub-parent", parent, msg + f"; rolls up to {homes[parent][0]}"))
            else:
                warnings.append(("non-hub-parent", parent, msg + "; reaches no hub"))

    clusters = defaultdict(list)
    for stem, n in notes.items():
        if n["belongs_to"] or not n["related_to"] or n["archived"]:
            continue
        if n["type"] in exempt | {"Person"} or is_hub(stem):
            continue
        r = resolve(n["related_to"][0])
        if r:
            clusters[r].append(stem)
    for target, members in sorted(clusters.items()):
        if len(members) >= 3:
            warnings.append(("related-only-cluster", target, f"{len(members)} related_to-only notes share this first link: {', '.join(sorted(members)[:6])}{'…' if len(members) > 6 else ''}"))

    if show_tree:
        kids = defaultdict(list)
        for stem, h in homes.items():
            if h:
                kids[h[0]].append(stem)
        roots = [s for s in notes if is_hub(s) and not (homes.get(s) or [None])[0]]

        def show(s, d):
            hub_kids = [k for k in kids[s] if is_hub(k)]
            print(f"{'  ' * d}{'◆' if notes[s]['type'] == 'Project' else '■'} {s} [{notes[s]['type']}; {len(kids[s]) - len(hub_kids)} notes, {len(hub_kids)} sub-hubs]")
            for k in sorted(hub_kids):
                show(k, d + 1)
        for r in sorted(roots, key=lambda s: -len(kids[s])):
            show(r, 0)
        print()

    for cat, note, msg in errors:
        print(f"ERROR\t{cat}\t{note}.md\t{msg}")
    for cat, note, msg in warnings:
        print(f"WARNING\t{cat}\t{note}.md\t{msg}")
    for cat, note, msg in infos:
        print(f"INFO\t{cat}\t{note}.md\t{msg}")
    counts = defaultdict(int)
    for cat, _, _ in errors + warnings:
        counts[cat] += 1
    print("SUMMARY\t" + "\t".join(f"{k}={v}" for k, v in sorted(counts.items())) + f"\terrors={len(errors)}\twarnings={len(warnings)}\tinfo={len(infos)}\tnotes={len(notes)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
