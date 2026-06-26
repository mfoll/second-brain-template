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
2. Confirm that the configured vault root and its short logical vault role are known. The role should be a stable label such as `personal`, `work/control`, `research`, or `team`; it may appear in project-local `AGENTS.md`, but concrete local paths must not. Confirm that the root is readable and contains `AGENTS.md`. If not, stop and ask the user to configure global instructions from [[global-agent-instructions-template]].
3. Read the vault-level `AGENTS.md` and discover current Type notes at the vault root.
4. Ask or infer the workspace title, purpose, scope, and whether it is Entry-point-scoped or Vault-scoped.
5. For Entry-point-scoped work, search existing vault notes across all Types before creating a new entry note.
6. If a matching entry note exists, propose using it. If none exists, propose a kebab-case filename, Type, and concise initial structure.
7. Decide relationships using `belongs_to`, `related_to`, and `has`. Explain only high-confidence relationships before writing.
8. Create or update the entry note. When creating a new Project note, instantiate the structure from [[project]]: Outcome, Current State, Scope and Boundaries, useful project-specific working context, Active Workflows when applicable, Next Actions, Open Questions, Important Notes, optional Do Not Do Yet, and Maintenance Log.
9. Unless the user explicitly says the Project does not need a saved view, add `surface_for` with the real Project wikilink to the Project note and create the matching small saved view by following [[procedures/maintain-project-human-view|Maintain Project Human View]]. If the user explicitly opts the Project out of a view, add `Project view: false` to the Project note instead.
10. Create or update the workspace-local `AGENTS.md` as a short pointer. It should name the logical vault role, name only the primary entry note, and tell agents to read the configured root's `AGENTS.md` for that named role.
11. For Vault-scoped work, create or update the workspace-local `AGENTS.md` without naming a primary entry note.
12. Add or verify a project-local `CLAUDE.md` compatibility shim that imports the local `AGENTS.md` with `@AGENTS.md`, unless an existing custom `CLAUDE.md` deliberately contains Claude-specific instructions.
13. Add the workspace documentation rule to the local `AGENTS.md` pointer: durable design docs, workflow decisions, research notes, open questions, tool evaluations, and project state should be written into the selected vault as typed notes linked from the primary entry note; keep workspace `docs/` only for implementation-local, generated, or explicitly transient material. Do not duplicate the vault-level project memory writeback rule in the local pointer.
14. Apply the workspace repository and backup decision:
   - a folder that only contains an `AGENTS.md` pointer is acceptable as a short bootstrap state, but should not remain the steady-state form of a proper instantiated project workspace;
   - when the workspace is meant to contain code, scripts, manuscript inputs, generated-but-useful artifacts, configs, or project-specific tooling, initialize a local Git repository and an appropriate private remote by default, unless the workspace is explicitly disposable, sensitive/local-only, or backed by another canonical system;
   - keep raw data, shared-drive dumps, credentials, `.env` files, local root resolvers, caches, virtual environments, controlled data, and large generated outputs out of the project remote; represent maintained external raw locations with Source notes or external storage pointers, and use Git LFS only when deliberately appropriate.
15. After the target folder, `AGENTS.md` pointer, and any needed `CLAUDE.md` shim exist, ask the user to create or open the Codex project and point it to that prepared folder.
16. Review the diff in both the workspace and vault repository before committing.

## Entry-Point-Scoped Local Pointer Template

```md
## Second Brain Memory

This workspace uses entry-point-scoped Second Brain memory.

Second Brain vault: `<vault-role>`

The agent must know the configured `<vault-role>` vault root from global/user instructions. If the `<vault-role>` vault root is unknown or unreadable, stop and ask the user to configure global Second Brain instructions with the correct `<vault-role>` vault path. Do not guess the path or create a new vault.

Primary Second Brain entry note:

`<entry-note-wikilink>`

Read the vault-level `AGENTS.md` from the configured `<vault-role>` vault root.

Before doing project work, read the primary entry note and the directly linked notes that are relevant to the task, especially Source notes, External Raw Locations, active workflows, and important notes.

If the user refers to a file, folder, dataset, manuscript, raw document, or path-like reference, check the primary entry note and linked Source notes for external raw-file pointers before guessing paths or searching broadly.

Workspace documentation rule: before creating or extending Markdown documentation in this workspace, decide whether it is durable project knowledge. If it is durable, write or update the appropriate Second Brain note linked from the primary entry note instead of creating a parallel `docs/` knowledge base. Keep workspace `docs/` material only when it is implementation-local, generated, or explicitly transient.

```

The local pointer should name the logical vault role, only the primary entry note, and the generic lookup rule above. Do not duplicate the vault-level project memory writeback rule in the local pointer. Do not add a hand-picked list of secondary notes, procedures, responsibilities, sources, raw folders, or topics to the workspace `AGENTS.md`; those relationships belong in the entry note and evolve there. Do not add project-specific artifact sections such as local working files, deliverables, datasets, outputs, or workflow handoffs to the workspace `AGENTS.md`; record those in the primary entry note or an appropriate linked typed note instead.

## Claude Code Compatibility Shim

When Claude Code may use the workspace, create this beside the local `AGENTS.md` unless an existing `CLAUDE.md` intentionally carries custom Claude-specific instructions:

```md
# Claude Code Compatibility

@AGENTS.md

This file is only a Claude Code compatibility shim. Keep shared agent instructions in `AGENTS.md`.
```

## Vault-Scoped Local Pointer Template

```md
## Second Brain Memory

This workspace uses vault-scoped Second Brain memory. It is intentionally not linked to a primary entry note.

Second Brain vault: `<vault-role>`

The agent must know the configured `<vault-role>` vault root from global/user instructions. If the `<vault-role>` vault root is unknown or unreadable, stop and ask the user to configure global Second Brain instructions with the correct `<vault-role>` vault path. Do not guess the path or create a new vault.

Read the vault-level `AGENTS.md` from the configured `<vault-role>` vault root.

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
