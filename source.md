---
type: Type
_icon: file-text
_color: "#0ea5e9"
_order: 6
_organized: true
---

# Source

A Source records external or re-checkable material, or a maintained external project location, with provenance, summary, caveats, and links to relevant synthesis.

Detailed evidence may remain long, but a Source above roughly 2,000 words should open with a 100–150-word `## At a Glance` or `## Summary` so readers can decide whether deeper inspection is necessary.

Provenance should be human-visible in the note body as well as machine-readable in frontmatter. If frontmatter includes `url`, `urls`, `source_file`, DOI, repository, `root_key`, `relative_path`, or another source pointer, include the useful link or location again in a readable section such as `## Source Links` or `## Source Location`.

## External Project Files

For maintained project inputs, outputs, deliverables, or folders that intentionally remain outside the vault, use Source notes as portable pointers and retrieval hooks. Store `storage_system`, `root_key`, `relative_path`, `access`, and `last_checked` rather than a committed absolute local path.

`root_key` resolves through ignored local configuration such as `.local/roots.yml`, environment variables, or machine-local agent setup. `access: guarded-write` means read-only by default, with writes allowed only when the user explicitly asks for the specific write.

A specific external file or project folder that should be maintained over time gets its own Source note. Project notes should link to that Source note instead of storing `last_checked` themselves. Casual one-off mentions of files do not need Source notes unless the user asks to remember, track, reference, associate, or maintain that file.

## Template

```md
---
type: Source
source_type: Scientific paper
url: https://example.org/the-item
date_accessed: YYYY-MM-DD
belongs_to: "[[project-or-responsibility-that-answers-for-it]]"
related_to:
  - "[[relevant-concept-or-question]]"
_organized: true
---

# Title As Published

## Summary

What the source is and the two or three findings that matter here.

## Why It Matters

Which Project, Question or decision it informs.

## Key Details

The specific facts, numbers, methods or quotes worth keeping, with their limits.

## Caveats

What the source does not show, and any conflict with notes already in the vault.

## Source Links

- [Title As Published](https://example.org/the-item)
```

A Source does not need a URL. `date_accessed` is the date you consulted an external item; for a document of your own, record the date you captured it. For a document, spreadsheet or list you keep yourself, use for example `source_type: Internal document`, omit `url`, and replace `## Source Links` with `## Source Location` naming where the item lives (a folder, an app, a drawer). For a maintained external file or folder, use `source_file`, or `storage_system` with `root_key`, `relative_path`, `access` and `last_checked`, with `## Source Location` as well. Follow [[procedures/ingest-source|Ingest Source]] for the full ingestion steps.
