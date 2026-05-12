---
type: Type
_icon: file-text
_color: "#0ea5e9"
_order: 6
_organized: true
---

# Source

A Source records external or re-checkable material with provenance, summary, caveats, and links to relevant synthesis.

Provenance should be human-visible in the note body as well as machine-readable in frontmatter. If frontmatter includes `url`, `urls`, `source_file`, DOI, repository, `root_key`, `relative_path`, or another source pointer, include the useful link or location again in a readable section such as `## Source Links` or `## Source Location`.

## External Raw Files

For raw files or folders that intentionally remain outside the vault, use Source notes as portable pointers and retrieval hooks. Store `storage_system`, `root_key`, `relative_path`, `access`, and `last_checked` rather than a committed absolute local path.

`root_key` resolves through ignored local configuration such as `.local/roots.yml`, environment variables, or machine-local agent setup. `access: guarded-write` means read-only by default, with writes allowed only when the user explicitly asks for the specific write.

A specific external file that should be maintained over time gets its own Source note. Project notes should link to that Source note instead of storing `last_checked` themselves. Casual one-off mentions of files do not need Source notes unless the user asks to remember, track, reference, associate, or maintain that file.
