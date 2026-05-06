---
type: Procedure
status: Active
Belongs to: "[[vault]]"
Related to:
  - "[[global-agent-instructions-template]]"
  - "[[project-scoped-memory]]"
_organized: true
---

# Initialize Project Memory

Use this procedure when a project workspace should be connected to a vault Project note so future agents start from the right memory scope.

## Goal

Create or update a short project-local `AGENTS.md` pointer and the corresponding vault Project note without copying full vault rules into the workspace.

## Steps

1. Inspect the current workspace path, folder name, Git status, and any existing local `AGENTS.md`.
2. Confirm that the configured vault root is known, readable, and contains `AGENTS.md`. If not, stop and ask the user to configure global instructions from [[global-agent-instructions-template]].
3. Read the vault-level `AGENTS.md` and discover current Type notes at the vault root.
4. Ask or infer the project title, purpose, scope, and whether this is a new project or an existing one.
5. Search existing vault notes by folder name, project title, aliases, and purpose before creating a new Project note.
6. If a matching Project exists, propose using it. If none exists, propose a kebab-case Project filename and a concise initial structure.
7. Decide relationships using `Belongs to`, `Related to`, and `Has`. Explain only high-confidence relationships before writing.
8. Create or update the Project note with purpose, scope, current context, active workflows, next actions, open questions, and a Maintenance Log when useful.
9. Create or update the workspace-local `AGENTS.md` as a short pointer. It should name the primary Project wikilink and tell agents to read the configured vault root's `AGENTS.md`.
10. Do not embed machine-specific vault paths in the project-local pointer unless the user's local setup explicitly requires it and the file is intentionally machine-local.
11. Review the diff in both the workspace and vault repository before committing.

## Local Pointer Template

```md
## Second Brain Memory

This workspace uses project-scoped Second Brain memory.

The agent must know the configured vault root from global/user instructions. If the vault root is unknown or unreadable, stop and ask the user to configure global Second Brain instructions with the correct vault path. Do not guess the path or create a new vault.

Primary Project note:

`[[project-note-stem]]`

Read the vault-level `AGENTS.md` from the configured vault root. Start memory lookup from this Project note and its linked notes before widening search.
```


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
