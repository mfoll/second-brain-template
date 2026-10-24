#!/usr/bin/env python3
"""Read-only compactness audit for canonical Second Brain Markdown notes."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

EXCLUDED_PARTS = {".agents", ".local", "attachments", ".tolaria-cache", ".cache", ".tmp", "node_modules"}
WORD_RE = re.compile(r"[^\W_]+(?:['’\-][^\W_]+)*", re.UNICODE)
# Session output appended as "## Follow-up, 16 October 2026" instead of reconciled
# into the section that owns the fact. A bare year ("2026 objective map") is allowed.
DATED_HEADING_RE = re.compile(
    r"\b\d{4}-\d{2}-\d{2}\b|(?<![A-Za-z])(?:January|February|March|April|May|June|July|"
    r"August|September|October|November|December)(?![a-z])",
)
RESUMPTION_TYPES = {"Project", "Responsibility", "Topic", "Guide", "Operation"}
LOG_HEADINGS = {"maintenance log"}
FENCE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def tracked_markdown(root: Path) -> list[Path]:
    """Canonical notes: Git-tracked Markdown when the root is a Git worktree, else every Markdown file on disk."""
    relatives: list[Path] = []
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z", "--", "*.md"],
            cwd=root,
            check=True,
            capture_output=True,
        )
        relatives = [
            Path(raw.decode("utf-8", errors="surrogateescape"))
            for raw in result.stdout.split(b"\0")
            if raw
        ]
    except (FileNotFoundError, subprocess.CalledProcessError):
        relatives = sorted(path.relative_to(root) for path in root.rglob("*.md"))
    paths: list[Path] = []
    for relative in relatives:
        if any(part in EXCLUDED_PARTS or part == ".git" for part in relative.parts):
            continue
        paths.append(root / relative)
    return paths


def split_note(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    return ("", text) if end < 0 else (text[4:end], text[end + 5 :])


def strip_fences(body: str) -> str:
    """Blank fenced code blocks so example headings are not read as note structure."""
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
        out.append(line)
    return "\n".join(out)


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
        outline = strip_fences(body)
        relative = str(path.relative_to(root))
        totals["notes"] += 1
        totals["words"] += body_words

        if relative == "AGENTS.md" and words(text) > 2000:
            warnings.append(("instructions", relative, f"{words(text)} words; target <=2000"))

        if note_type == "Project" and status == "Active":
            totals["projects"] += 1
            totals["project_words"] += body_words
            if body_words > 3000:
                warnings.append(("project-critical", relative, f"{body_words} body words; split or justify"))
            elif body_words > 1500:
                warnings.append(("project-review", relative, f"{body_words} body words; target <=1500"))
            current_words = words(section(outline, "Current State"))
            if current_words > 250:
                warnings.append(("current-state", relative, f"{current_words} words; target <=250"))
            action_count = len(re.findall(r"(?m)^\s*[-*]\s+\[ \]\s+", section(outline, "Next Actions")))
            if action_count > 10:
                warnings.append(("next-actions", relative, f"{action_count} unchecked actions; target <=10"))
            log_count = len(re.findall(r"(?m)^\s*[-*]\s+\S", section(outline, "Maintenance Log")))
            if log_count > 5:
                warnings.append(("maintenance-log", relative, f"{log_count} entries; target <=5"))

        if note_type in RESUMPTION_TYPES and field(frontmatter, "_archived") != "true":
            headings = re.findall(r"(?m)^## (.+?)\s*$", outline)
            for heading in headings:
                if DATED_HEADING_RE.search(heading):
                    warnings.append(("dated-section", relative, f"'{heading}'; fold into the owning section or an Event"))
            log_positions = [i for i, heading in enumerate(headings) if heading.lower() in LOG_HEADINGS]
            if len(log_positions) > 1:
                warnings.append(("maintenance-log", relative, f"{len(log_positions)} Maintenance Log headings; merge"))
            if log_positions and log_positions[0] < len(headings) - 1:
                after = len(headings) - 1 - log_positions[0]
                warnings.append(("after-log", relative, f"{after} section(s) below Maintenance Log; move above it"))

        if note_type == "Question" and body_words > 750:
            warnings.append(("question-review", relative, f"{body_words} body words; review routing"))

        if note_type in {"Source", "Event", "Method"} and body_words > 2000:
            if not re.search(
                r"(?mi)^## (?:At a [Gg]lance|Summary|Abstract|Current Recommendation|Event Summary)\s*$",
                outline,
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
