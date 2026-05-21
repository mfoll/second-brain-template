---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[global-agent-instructions-template]]"
  - "[[project-scoped-memory]]"
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
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
7. Decide relationships using `belongs_to`, `related_to`, and `has`. Explain only high-confidence relationships before writing.
8. Create or update the entry note. When creating a new Project note, instantiate the structure from [[project]]: Outcome, Current State, Scope and Boundaries, useful project-specific working context, Active Workflows when applicable, Next Actions, Open Questions, Important Notes, optional Do Not Do Yet, and Maintenance Log.
9. Unless the user explicitly says the Project does not need a saved view, add `surface_for` with the real Project wikilink to the Project note and create the matching small saved view by following [[procedures/maintain-project-human-view|Maintain Project Human View]]. If the user explicitly opts the Project out of a view, add `Project view: false` to the Project note instead.
10. Create or update the workspace-local `AGENTS.md` as a short pointer. It should name only the primary entry note and tell agents to read the configured vault root's `AGENTS.md`.
11. For Vault-scoped work, create or update the workspace-local `AGENTS.md` without naming a primary entry note.
12. Add the workspace documentation rule to the local `AGENTS.md` pointer: durable design docs, workflow decisions, research notes, open questions, tool evaluations, and project state should be written into the selected vault as typed notes linked from the primary entry note; keep workspace `docs/` only for implementation-local, generated, or explicitly transient material.
13. Add the project memory writeback rule to Entry-point-scoped local `AGENTS.md` pointers so agents working outside the vault check whether the linked project memory needs updates before finishing significant work.
14. After the target folder and `AGENTS.md` pointer exist, ask the user to create or open the Codex project and point it to that prepared folder.
15. Review the diff in both the workspace and vault repository before committing.

## Entry-Point-Scoped Local Pointer Template

```md
## Second Brain Memory

This workspace uses entry-point-scoped Second Brain memory.

The agent must know the configured vault root from global/user instructions. If the vault root is unknown or unreadable, stop and ask the user to configure global Second Brain instructions with the correct vault path. Do not guess the path or create a new vault.

Primary Second Brain entry note:

`<entry-note-wikilink>`

Read the vault-level `AGENTS.md` from the configured vault root.

Before doing project work, read the primary entry note and the directly linked notes that are relevant to the task, especially Source notes, External Raw Locations, active workflows, and important notes.

If the user refers to a file, folder, dataset, manuscript, raw document, or path-like reference, check the primary entry note and linked Source notes for external raw-file pointers before guessing paths or searching broadly.

Workspace documentation rule: before creating or extending Markdown documentation in this workspace, decide whether it is durable project knowledge. If it is durable, write or update the appropriate Second Brain note linked from the primary entry note instead of creating a parallel `docs/` knowledge base. Keep workspace `docs/` material only when it is implementation-local, generated, or explicitly transient.

Project memory writeback: before finishing significant project work, check whether the linked project memory needs an update. Use the primary entry note as the entry point and resumption surface, but update the most appropriate durable note(s). This may mean refreshing the Project note's `Current State`, `Next Actions`, `Open Questions`, `Important Notes`, or `Maintenance Log`; updating linked Source, Procedure, ADR, Question, Concept, Skill, Responsibility, or other typed notes when the durable change belongs there; or adding a new typed note only when it improves retrieval or separates a stable decision, source, workflow, or question from project-summary prose. Keep the primary entry note coherent after related-note edits: if a linked note changes the project's state, next actions, active workflows, boundaries, or important starting points, reflect that briefly in the primary entry note too. If no memory update is needed, say so briefly in the final response.
```

The local pointer should name only the primary entry note and the generic lookup rule above. Do not add a hand-picked list of secondary notes, procedures, responsibilities, sources, raw folders, or topics to the workspace `AGENTS.md`; those relationships belong in the entry note and evolve there.

## Vault-Scoped Local Pointer Template

```md
## Second Brain Memory

This workspace uses vault-scoped Second Brain memory. It is intentionally not linked to a primary entry note.

The agent must know the configured vault root from global/user instructions. If the vault root is unknown or unreadable, stop and ask the user to configure global Second Brain instructions with the correct vault path. Do not guess the path or create a new vault.

Read the vault-level `AGENTS.md` from the configured vault root.

Start memory lookup from the vault root note and relevant Type, Topic, Responsibility, Source, Question, Concept, Procedure, and Inbox/Unprocessed notes before widening search.

Do not create or link a primary entry note for this workspace unless the user explicitly asks.

Workspace documentation rule: before creating or extending Markdown documentation in this workspace, decide whether it is durable vault knowledge. If it is durable, write or update the appropriate Second Brain note instead of creating a parallel `docs/` knowledge base. Keep workspace `docs/` material only when it is implementation-local, generated, or explicitly transient.
```

## Guardrails

- Keep edits scoped to the user's request and the relevant entry note or Source.
- Use `belongs_to`, `related_to`, and `has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.

Do not let a workspace `docs/` folder become a second project memory system. Use it only for implementation-local, generated, or explicitly transient material; promote durable knowledge into the vault.
