#!/usr/bin/env python3
"""Audit icon fields against the pinned Phosphor name list; confirm UI rendering separately."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

CATALOG_PATH = (
    Path(__file__).resolve().parent.parent
    / "references"
    / "phosphor-icon-names.txt"
)
FRONTMATTER_END_RE = re.compile(r"(?m)^---\s*$")
SCALAR_RE_TEMPLATE = r"(?m)^{key}:\s*(.*?)\s*$"
ICON_NAME_RE = re.compile(r"^[a-z][a-z0-9-]*$")


def selected_files(root: Path) -> list[Path]:
    """Return tracked notes plus every current saved-view YAML file."""

    try:
        result = subprocess.run(
            ["git", "ls-files", "-z", "--", "*.md"],
            cwd=root,
            check=True,
            capture_output=True,
        )
        paths = {
            root / raw.decode("utf-8", errors="surrogateescape")
            for raw in result.stdout.split(b"\0")
            if raw
        }
    except (FileNotFoundError, subprocess.CalledProcessError):
        skipped = {".git", ".agents", ".local", ".tmp", ".tolaria-cache", ".cache", "attachments"}
        paths = {
            path for path in root.rglob("*.md")
            if not any(part in skipped for part in path.relative_to(root).parts)
        }
    views_root = root / "views"
    if views_root.is_dir():
        paths.update(path for pattern in ("*.yml", "*.yaml") for path in views_root.glob(pattern))
    return sorted(paths, key=lambda path: path.relative_to(root).as_posix())


def frontmatter(text: str) -> tuple[str, int]:
    if not text.startswith("---\n"):
        return "", 0
    match = FRONTMATTER_END_RE.search(text, 4)
    if match is None:
        return "", 0
    return text[4 : match.start()], 2


def scalar(text: str, key: str, line_offset: int = 1) -> tuple[str | None, int | None]:
    pattern = re.compile(SCALAR_RE_TEMPLATE.format(key=re.escape(key)))
    match = pattern.search(text)
    if match is None:
        return None, None

    raw = match.group(1).strip()
    if raw and raw[0] in {'"', "'"} and raw[-1:] == raw[0]:
        raw = raw[1:-1]
    elif " #" in raw:
        raw = raw.split(" #", 1)[0].rstrip()

    line = line_offset + text.count("\n", 0, match.start())
    if raw.casefold() in {"", "null", "~"}:
        return None, line
    return raw, line


def is_http_url(value: str) -> bool:
    """Approximate Tolaria's URL parsing without claiming that an image will load."""

    if any(character.isspace() for character in value):
        return False
    try:
        parsed = urlparse(value)
        return (
            parsed.scheme.casefold() in {"http", "https"}
            and bool(parsed.netloc)
            and bool(parsed.hostname)
        )
    except ValueError:
        return False


def classification(value: str, catalog: set[str]) -> tuple[str, str] | None:
    """Return an error or manual-review category for a non-registry value."""

    if value in catalog:
        return None
    if ICON_NAME_RE.fullmatch(value):
        return "error", "unknown-named-icon"
    if is_http_url(value):
        return "warning", "manual-url-icon"
    if any(ord(character) > 127 for character in value):
        return "warning", "manual-non-registry-icon"
    return "error", "unsupported-icon-value"


def load_catalog() -> set[str]:
    return {
        line.strip()
        for line in CATALOG_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR\tvault root is not a directory: {root}", file=sys.stderr)
        return 2
    try:
        catalog = load_catalog()
        files = selected_files(root)
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"ERROR\t{error}", file=sys.stderr)
        return 2

    errors: list[tuple[str, int, str, str]] = []
    warnings: list[tuple[str, int, str, str]] = []
    counts = {"views": 0, "note_icons": 0}

    for path in files:
        relative = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")

        if relative.startswith("views/") and path.suffix.casefold() in {".yml", ".yaml"}:
            counts["views"] += 1
            value, line = scalar(text, "icon")
            result = classification(value, catalog) if value is not None else None
            if result is not None:
                severity, category = result
                target = errors if severity == "error" else warnings
                target.append((relative, line or 1, f"{category}-in-view", value))
            continue

        metadata, line_offset = frontmatter(text)
        if not metadata:
            continue
        for key in ("_icon", "icon"):
            value, line = scalar(metadata, key, line_offset)
            if value is None:
                continue
            counts["note_icons"] += 1
            result = classification(value, catalog)
            if result is not None:
                severity, category = result
                target = errors if severity == "error" else warnings
                target.append((relative, line or 1, f"{category}-in-{key.lstrip('_')}", value))

    print(
        "SUMMARY\t"
        f"views={counts['views']}\tnote_icons={counts['note_icons']}\t"
        f"catalog_icons={len(catalog)}\terrors={len(errors)}\twarnings={len(warnings)}"
    )
    for relative, line, category, value in sorted(errors):
        print(f"ERROR\t{category}\t{relative}:{line}\t{value}")
    for relative, line, category, value in sorted(warnings):
        print(f"WARN\t{category}\t{relative}:{line}\t{value}")
    if not errors and not warnings:
        print("OK\tall configured named icons are in the Phosphor catalogue; confirm rendering in the viewer")
    elif not errors:
        print("OK\tall named icons are verified; confirm warned non-registry icons in Tolaria")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
