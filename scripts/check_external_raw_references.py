#!/usr/bin/env python3
"""Refresh external raw-file Source notes in a Second Brain vault."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from pathlib import Path


SKIP_DIRS = {".git", ".agents", ".local", ".tmp", ".tolaria-cache", ".cache", "attachments"}


def parse_roots(path: Path) -> dict[str, list[str]]:
    if not path.exists():
        return {}

    roots: dict[str, list[str]] = {}
    current: str | None = None
    in_candidates = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.strip() == "roots:":
            continue
        if raw.startswith("  ") and not raw.startswith("    ") and raw.strip().endswith(":"):
            current = raw.strip()[:-1]
            roots.setdefault(current, [])
            in_candidates = False
            continue
        if current and raw.startswith("    candidates:"):
            in_candidates = True
            continue
        if current and in_candidates and raw.startswith("      - "):
            value = raw.split("- ", 1)[1].strip().strip('"').strip("'")
            roots[current].append(os.path.expanduser(value))

    return roots


def split_frontmatter(text: str) -> tuple[list[str], list[str]] | None:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[: idx + 1], lines[idx + 1 :]
    return None


def parse_frontmatter(lines: list[str]) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in lines[1:-1]:
        if line.startswith(" ") or line.startswith("\t") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def set_frontmatter_value(lines: list[str], key: str, value: str) -> list[str]:
    pattern = re.compile(rf"^{re.escape(key)}\s*:")
    out = list(lines)
    for idx in range(1, len(out) - 1):
        if pattern.match(out[idx]):
            out[idx] = f"{key}: {value}\n"
            return out
    out.insert(len(out) - 1, f"{key}: {value}\n")
    return out


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            continue
        files.append(path)
    return sorted(files)


def resolve_root(root_key: str, roots: dict[str, list[str]]) -> tuple[Path | None, list[str]]:
    candidates = roots.get(root_key, [])
    for candidate in candidates:
        candidate_path = Path(candidate)
        if candidate_path.exists():
            return candidate_path, candidates
    return None, candidates


def resolve_source_target(root: Path, relative_path: str) -> Path:
    relative = Path(relative_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("expected a relative path without parent traversal")
    resolved_root = root.resolve()
    target = (resolved_root / relative).resolve()
    if not target.is_relative_to(resolved_root):
        raise ValueError("symlink resolves outside the configured root")
    # Non-strict resolve/exists can suppress symlink-loop errors on newer Python.
    try:
        target.stat()
    except (FileNotFoundError, NotADirectoryError):
        pass
    return target


def source_kind(source_type: str) -> str | None:
    lower = source_type.lower()
    if "folder" in lower or "library" in lower or "directory" in lower:
        return "folder"
    if "file" in lower or "document" in lower:
        return "file"
    return None


def index_depth(index_scope: str) -> int:
    match = re.search(r"max depth\s+(\d+)", index_scope.lower())
    if not match:
        return 2
    return max(1, int(match.group(1)))


def shallow_folder_lines(path: Path, checked_date: str, max_depth: int) -> list[str]:
    lines = ["## Shallow Folder Index\n", "\n", f"Observed on {checked_date}:\n", "\n"]
    first_level = sorted(
        [p for p in path.iterdir() if not p.name.startswith(".") and not p.is_symlink() and p.is_dir()],
        key=lambda p: p.name.casefold(),
    )
    for folder in first_level:
        lines.append(f"- `{folder.name}`\n")
        if max_depth >= 2:
            second_level = sorted(
                [p for p in folder.iterdir() if not p.name.startswith(".") and not p.is_symlink() and p.is_dir()],
                key=lambda p: p.name.casefold(),
            )
            for child in second_level:
                lines.append(f"  - `{child.name}`\n")
    return lines


def extract_index_items(text: str) -> list[str]:
    match = re.search(r"(?ms)^## Shallow Folder Index\n(.*?)(?=^## |\Z)", text)
    if not match:
        return []
    return [line.rstrip() for line in match.group(1).splitlines() if line.lstrip().startswith("- `") or line.lstrip().startswith("-")]


def replace_shallow_index(body: list[str], new_section: list[str]) -> list[str]:
    text = "".join(body)
    replacement = "".join(new_section).rstrip() + "\n\n"
    if re.search(r"(?ms)^## Shallow Folder Index\n.*?(?=^## |\Z)", text):
        updated = re.sub(r"(?ms)^## Shallow Folder Index\n.*?(?=^## |\Z)", replacement, text)
    else:
        if text and not text.endswith("\n"):
            text += "\n"
        updated = text.rstrip() + "\n\n" + replacement
    return updated.splitlines(keepends=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write vault Source-note updates")
    parser.add_argument("--date", default=dt.date.today().isoformat(), help="checked date")
    args = parser.parse_args()

    vault = Path.cwd()
    roots = parse_roots(vault / ".local" / "roots.yml")
    report: list[str] = []
    changed: list[Path] = []
    drifted: list[Path] = []

    for note in iter_markdown_files(vault):
        text = note.read_text(encoding="utf-8")
        split = split_frontmatter(text)
        if not split:
            continue
        fm_lines, body = split
        fm = parse_frontmatter(fm_lines)
        if fm.get("type") != "Source":
            continue
        if fm.get("_archived", "").lower() == "true":
            continue
        root_key = fm.get("root_key")
        relative_path = fm.get("relative_path")
        if not root_key or not relative_path:
            continue

        note_label = str(note.relative_to(vault))
        resolved_root, candidates = resolve_root(root_key, roots)
        if not resolved_root:
            report.append(f"WARN unresolved root {root_key} for {note_label}; configured candidates: {len(candidates)}")
            continue

        try:
            target = resolve_source_target(resolved_root, relative_path)
        except (ValueError, OSError, RuntimeError):
            report.append(f"WARN unsafe or unresolvable relative_path for {note_label}; note left unchanged")
            continue

        reference = f"{root_key}: {relative_path}"
        if not target.exists():
            report.append(f"WARN missing path for {note_label} ({reference})")
        else:
            expected = source_kind(fm.get("source_type", ""))
            if expected == "folder" and not target.is_dir():
                report.append(f"WARN expected folder for {note_label}, found non-folder ({reference})")
            elif expected == "file" and not target.is_file():
                report.append(f"WARN expected file for {note_label}, found non-file ({reference})")
            else:
                report.append(f"OK {note_label} ({reference})")

        new_fm = set_frontmatter_value(fm_lines, "last_checked", args.date)
        new_body = body
        if target.is_dir() and "shallow folder index" in fm.get("index_scope", "").lower():
            new_index = shallow_folder_lines(target, args.date, index_depth(fm.get("index_scope", "")))
            old_items = extract_index_items("".join(body))
            new_items = extract_index_items("".join(new_index))
            if old_items != new_items:
                drifted.append(note)
                report.append(f"DRIFT shallow index changed for {note_label}")
            new_body = replace_shallow_index(body, new_index)

        new_text = "".join(new_fm + new_body)
        if new_text != text:
            changed.append(note)
            if args.write:
                note.write_text(new_text, encoding="utf-8")

    if not roots:
        report.insert(0, "INFO .local/roots.yml not found or no roots parsed: no external roots configured, nothing to check")

    print("# External raw reference check")
    print(f"date: {args.date}")
    print(f"mode: {'write' if args.write else 'dry-run'}")
    print()
    for line in report:
        print(line)
    print()
    print(f"vault notes needing update: {len(changed)}")
    print(f"vault notes with index drift: {len(drifted)}")
    if changed and not args.write:
        print("Run again with --write to update vault Source notes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
