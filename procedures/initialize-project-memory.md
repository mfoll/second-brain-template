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

Use this procedure when a Codex project workspace should be connected to a vault so future agents start from the right memory scope.

## Goal

Prepare a short project-local `AGENTS.md` pointer and, when needed, the corresponding vault entry note without copying full vault rules into the workspace.

The memory scope can be:

- Entry-point-scoped: the workspace points to one primary vault entry note. This is usually a `Project`, but another Type may be used when the user deliberately wants the workspace scoped to a Responsibility, Topic, Procedure, Source, or another existing note.
- Vault-scoped: the workspace points to the selected vault only and intentionally does not create or link a Project note.

## Steps

1. Inspect or create the target workspace folder before asking the user to create or open it as a Codex project.
2. Confirm that the configured vault root is known, readable, and contains `AGENTS.md`. If not, stop and ask the user to configure global instructions from [[global-agent-instructions-template]].
3. Read the vault-level `AGENTS.md` and discover current Type notes at the vault root.
4. Ask or infer the workspace title, purpose, scope, and whether it is Entry-point-scoped or Vault-scoped.
5. For Entry-point-scoped work, search existing vault notes across all Types before creating a new entry note.
6. If a matching entry note exists, propose using it. If none exists, propose a kebab-case filename, Type, and concise initial structure.
7. Decide relationships using `Belongs to`, `Related to`, and `Has`. Explain only high-confidence relationships before writing.
8. Create or update the entry note. When creating a new Project note, instantiate the structure from [[project]]: Outcome, Current State, Scope and Boundaries, useful project-specific working context, Active Workflows when applicable, Next Actions, Open Questions, Important Notes, optional Do Not Do Yet, and Maintenance Log.
9. Create or update the workspace-local `AGENTS.md` as a short pointer. It should name only the primary entry note and tell agents to read the configured vault root's `AGENTS.md`.
10. For Vault-scoped work, create or update the workspace-local `AGENTS.md` without naming a primary entry note.
11. After the target folder and `AGENTS.md` pointer exist, ask the user to create or open the Codex project and point it to that prepared folder.
12. Review the diff in both the workspace and vault repository before committing.

## Entry-Point-Scoped Local Pointer Template

```md
## Second Brain Memory

This workspace uses entry-point-scoped Second Brain memory.

The agent must know the configured vault root from global/user instructions. If the vault root is unknown or unreadable, stop and ask the user to configure global Second Brain instructions with the correct vault path. Do not guess the path or create a new vault.

Primary Second Brain entry note:

`<entry-note-wikilink>`

Read the vault-level `AGENTS.md` from the configured vault root.

Start memory lookup from notes linked to this entry note before widening search.
```

The local pointer should name only the primary entry note. Do not add a hand-picked list of secondary notes, procedures, responsibilities, sources, or topics to the workspace `AGENTS.md`; those relationships belong in the entry note and evolve there.

## Vault-Scoped Local Pointer Template

```md
## Second Brain Memory

This workspace uses vault-scoped Second Brain memory. It is intentionally not linked to a primary entry note.

The agent must know the configured vault root from global/user instructions. If the vault root is unknown or unreadable, stop and ask the user to configure global Second Brain instructions with the correct vault path. Do not guess the path or create a new vault.

Read the vault-level `AGENTS.md` from the configured vault root.

Start memory lookup from the vault root note and relevant Type, Topic, Responsibility, Source, Question, Concept, Procedure, and Inbox/Unprocessed notes before widening search.

Do not create or link a primary entry note for this workspace unless the user explicitly asks.
```

## Guardrails

- Keep edits scoped to the user's request and the relevant entry note or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
