---
name: update-project-next-actions
description: Use when project-scoped agent work should update a Second Brain Project note's Next Actions after tasks are completed, partially completed, changed, or when a chat creates durable future follow-up work. Applies to the current Second Brain vault.
---

# Update Project Next Actions

Use this skill to reconcile a Second Brain Project note's `## Next Actions` section with the current state of project work.

## Source of truth

- Second Brain vault: this repository/vault root
- Vault rules: `AGENTS.md`
- Detailed procedure: `procedures/update-project-next-actions.md`

Read the vault rules and detailed procedure before making changes.

## Workflow

1. Identify the active Project note from the workspace `AGENTS.md`, explicit user request, or Tolaria context.
2. Read the current `## Next Actions` section.
3. Determine which actions were completed, partially completed, made obsolete, or newly created by recent work.
4. Update the list so it remains useful for project resumption.
5. Convert durable uncertainty, reusable ideas, ongoing responsibilities, repeated workflows, decisions, or other durable categories into appropriate typed notes only when the update is direct and high-confidence. Use the vault's current Type notes as the routing set.
6. When an action is added, changed, checked, or removed, update linked typed notes only if their state clearly changed.
7. Do not perform global cascade maintenance; record uncertain broader effects as follow-up or leave them for `review-vault-health`.
8. If the next-action update changes project state, important context, scope, open questions, important notes, active workflow, or guardrails, refresh the affected Project-note sections so the live entry point does not drift.
9. Add a short Maintenance Log entry when the project state meaningfully changed.
10. Review the diff before any commit.

## Defaults

- The next-actions list should be scannable, but there is no strict item limit.
- Prefer outcome-oriented actions over microtasks.
- Do not update the vault unless the user asked to save, update, remember, maintain, reconcile, or otherwise persist the change.
- Follow the vault's Git checkpoint rules after agent-managed vault changes unless the user explicitly asks not to.
