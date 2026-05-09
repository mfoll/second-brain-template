---
name: update-project-summary
description: Use when the user asks to refresh, maintain, reconcile, or update a Second Brain Project note summary, or when project-scoped vault work significantly changes project state. Applies to the current Second Brain vault.
---

# Update Project Summary

Use this skill to refresh a Second Brain Project note as the live entry point for returning to that project.

## Source of truth

- Second Brain vault: this repository/vault root
- Vault rules: `AGENTS.md`
- Detailed procedure: `procedures/update-project-summary.md`

Read the vault rules and detailed procedure before making changes.

## Workflow

1. Identify the active Project note from the workspace `AGENTS.md`, explicit user request, or Tolaria context.
2. Read the Project note and identify its current structure.
3. Find relevant linked notes through `Belongs to`, `Related to`, `Has`, backlinks, and obvious saved views.
4. Review recent or important linked notes before editing.
5. Preserve or normalize the standard Project structure from `project.md`: Outcome, Current State, Scope and Boundaries, useful project-specific working context, Active Workflows when applicable, Next Actions, Open Questions, Important Notes, optional Do Not Do Yet, and Maintenance Log.
6. Update only the sections affected by the work, such as Current State, Scope and Boundaries, Next Actions, Open Questions, Important Notes, Active Workflows, Do Not Do Yet, and Maintenance Log.
7. Check whether the project update should create or update linked typed notes, using the vault's current Type notes rather than a fixed list.
8. Make only direct, high-confidence linked-note updates; defer uncertain broader effects to `review-vault-health` or a follow-up action.
9. Preserve uncertainty and provenance; link to detailed notes instead of copying full note content.
10. Review the diff before any commit.

## Defaults

- Run after significant project-scoped vault work, source ingestion, or next-action reconciliation when the project entry point would otherwise be stale.
- If significance is unclear, report the possible summary update before editing.
- Follow the vault's Git checkpoint rules after agent-managed vault changes unless the user explicitly asks not to.
