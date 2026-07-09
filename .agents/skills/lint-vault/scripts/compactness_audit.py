#!/usr/bin/env python3
"""Read-only compactness audit for canonical Second Brain Markdown notes."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

EXCLUDED_PARTS = {".agents", ".local", "attachments", ".tolaria-cache", ".cache"}
WORD_RE = re.compile(r"[^\W_]+(?:['’\-][^\W_]+)*", re.UNICODE)


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def tracked_markdown(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.md"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    paths: list[Path] = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        relative = Path(raw.decode("utf-8", errors="surrogateescape"))
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        paths.append(root / relative)
    return paths


def split_note(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    return ("", text) if end < 0 else (text[4:end], text[end + 5 :])


def field(frontmatter: str, name: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*['\"]?([^'\"\n]+)", frontmatter)
    return match.group(1).strip() if match else None


def section(body: str, heading: str) -> str:
    match = re.search(rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", body)
    return match.group(1) if match else ""


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").expanduser().resolve()
    warnings: list[tuple[str, str, str]] = []
    totals = {"notes": 0, "words": 0, "projects": 0, "project_words": 0}

    for path in tracked_markdown(root):
        text = path.read_text(encoding="utf-8")
        frontmatter, body = split_note(text)
        note_type = field(frontmatter, "type")
        status = field(frontmatter, "status")
        body_words = words(body)
        relative = str(path.relative_to(root))
        totals["notes"] += 1
        totals["words"] += body_words

        if relative == "AGENTS.md" and words(text) > 1200:
            warnings.append(("instructions", relative, f"{words(text)} words; target <=1200"))

        if note_type == "Project" and status == "Active":
            totals["projects"] += 1
            totals["project_words"] += body_words
            if body_words > 3000:
                warnings.append(("project-critical", relative, f"{body_words} body words; split or justify"))
            elif body_words > 1500:
                warnings.append(("project-review", relative, f"{body_words} body words; target <=1500"))
            current_words = words(section(body, "Current State"))
            if current_words > 250:
                warnings.append(("current-state", relative, f"{current_words} words; target <=250"))
            action_count = len(re.findall(r"(?m)^\s*[-*]\s+\[ \]\s+", section(body, "Next Actions")))
            if action_count > 10:
                warnings.append(("next-actions", relative, f"{action_count} unchecked actions; target <=10"))
            log_count = len(re.findall(r"(?m)^\s*[-*]\s+\S", section(body, "Maintenance Log")))
            if log_count > 5:
                warnings.append(("maintenance-log", relative, f"{log_count} entries; target <=5"))

        if note_type == "Question" and body_words > 750:
            warnings.append(("question-review", relative, f"{body_words} body words; review routing"))

        if note_type in {"Source", "Event", "Method"} and body_words > 2000:
            if not re.search(
                r"(?mi)^## (?:At a [Gg]lance|Summary|Abstract|Current Recommendation|Event Summary)\s*$",
                body,
            ):
                warnings.append(("long-reference", relative, f"{body_words} body words; add opening summary"))

    mean_project = round(totals["project_words"] / totals["projects"]) if totals["projects"] else 0
    print(
        "SUMMARY\t"
        f"notes={totals['notes']}\tbody_words={totals['words']}\t"
        f"active_projects={totals['projects']}\tmean_active_project_words={mean_project}"
    )
    for category, relative, detail in sorted(warnings):
        print(f"WARNING\t{category}\t{relative}\t{detail}")
    print(f"WARNINGS\t{len(warnings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
