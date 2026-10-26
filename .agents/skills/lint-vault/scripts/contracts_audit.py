#!/usr/bin/env python3
"""Read-only checks for note headers and executable Skill/catalogue pairs.

Uses the vault's own Type definitions. This checks required top-level scalar
fields and pair routing, not arbitrary YAML syntax or semantic workflow quality.
Standard library only; accepts an optional vault root and exits 1 on errors.
"""
from __future__ import annotations

import re
import runpy
import sys
from pathlib import Path

# Share note exclusions, Markdown handling and scalar parsing with the link audit.
links = runpy.run_path(str(Path(__file__).with_name("links_audit.py")))


def header(text: str) -> tuple[dict[str, str], str, bool]:
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
    if not match:
        return {}, text, False
    fields = {
        key: value.strip("\"'")
        for key, value, form in links["frontmatter_entries"](match.group(1))
        if form == "scalar"
    }
    return fields, text[match.end():], True


def audit(root: Path) -> tuple[list[tuple[str, str, str]], int]:
    root = root.resolve()
    errors: list[tuple[str, str, str]] = []
    notes = {}

    def error(category: str, path: Path, message: str) -> None:
        errors.append((category, path.relative_to(root).as_posix(), message))

    for path in links["canonical"](root):
        if path.is_symlink():
            continue
        fields, body, valid = header(path.read_text(encoding="utf-8"))
        heading = links["H1"].search(links["strip_code"](body))
        notes[path] = (fields, body, heading)
        if not valid:
            error("frontmatter-missing", path, "missing or unterminated frontmatter")
        if not heading:
            error("h1-missing", path, "no first-level heading outside code")

    types = {
        heading.group(1).strip()
        for path, (fields, _, heading) in notes.items()
        if path.parent == root and fields.get("type") == "Type" and heading
    }
    package_owners: dict[Path, list[Path]] = {}
    for path, (fields, body, _) in notes.items():
        kind = fields.get("type")
        if not kind:
            error("type-missing", path, "missing scalar type")
        elif kind not in types:
            error("type-unknown", path, "type has no matching root Type definition")
        if kind != "Skill":
            continue
        package_path = fields.get("package_path", "")
        active = fields.get("status") == "Active" and fields.get("_archived", "").lower() != "true"
        if not package_path:
            if active:
                error("skill-package-missing", path, "active Skill has no package_path")
            continue
        relative = Path(package_path)
        if (relative.is_absolute() or len(relative.parts) != 3
                or relative.parts[:2] != (".agents", "skills") or ".." in relative.parts):
            error("skill-package-path", path, "expected .agents/skills/<name>/")
            continue
        package = root / relative
        if not package.resolve().is_relative_to(root):
            error("skill-package-path", path, "package resolves outside vault; not read")
            continue
        if not active:
            if package.exists():
                error("skill-retired-package", path, "inactive catalogue still has a discoverable package")
            continue
        package_owners.setdefault(package, []).append(path)
        executable = package / "SKILL.md"
        if not executable.is_file() or executable.is_symlink():
            error("skill-package-missing", path, "package SKILL.md missing or symlinked")
            continue
        text = executable.read_text(encoding="utf-8")
        meta, _, valid = header(text)
        if not valid or meta.get("name") != package.name:
            error("skill-name", path, "package name does not match its directory")
        if not meta.get("description"):
            error("skill-description", path, "package has no scalar description")
        wraps = fields.get("wraps")
        if wraps:
            match = links["WIKILINK"].fullmatch(wraps)
            target = links["target_of"](match.group(1)) if match else ""
            candidates = [p for p in notes if p.relative_to(root).with_suffix("").as_posix() == target]
            if not candidates and "/" not in target:
                candidates = [p for p in notes if p.stem == target]
            if len(candidates) != 1 or notes[candidates[0]][0].get("type") != "Procedure":
                error("skill-procedure", path, "wraps must resolve to one Procedure")
            elif candidates[0].relative_to(root).as_posix() not in text:
                error("skill-procedure", path, "package does not name its wrapped Procedure path")
        # Only explicit vault-relative package support paths are checked here.
        # Standalone ownership and natural-language support references need review.
        for support in re.findall(r"`(\.agents/skills/[^`\s]+)`", body + "\n" + text):
            if any(char in support for char in "<>*"):
                continue
            candidate = root / support
            if not candidate.resolve().is_relative_to(root) or not candidate.exists():
                error("skill-support-missing", path, "declared package support path is missing or outside vault")

    directory = root / ".agents/skills"
    if directory.exists():
        for package in sorted(directory.iterdir()):
            if not package.is_dir():
                continue
            if len(package_owners.get(package, [])) != 1:
                error("skill-catalogue", package, "package must have one active catalogue owner")
    return sorted(set(errors)), len(notes)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").expanduser().resolve()
    errors, count = audit(root)
    for category, path, message in errors:
        print(f"ERROR\t{category}\t{path}\t{message}")
    print(f"SUMMARY\terrors={len(errors)}\twarnings=0\tnotes={count}")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
