---
name: update-project-next-actions
description: "Reconcile completed, changed and new project next actions in the selected deployed vault; refresh related state when those actions affect it."
---

# Update Project Next Actions

Reconcile what should happen next: remove completed actions, rewrite remaining work and merge overlaps. Refresh related project state when the action changes affect it.

For a broader refresh of current state, scope, blockers and links, use `update-project-summary`. Both workflows keep actions and state consistent.

## Source of truth

- Vault rules: `AGENTS.md`
- Project contract: `project.md`
- Complete workflow: `procedures/update-project-next-actions.md`

Read the vault rules, Project Type, and Procedure completely before acting.

## Guardrails

- Keep 3–7 outcome-level actions; review lists above 10.
- Remove completed items, rewrite partial work, and merge overlaps instead of appending duplicates.
- Route durable uncertainty, knowledge, ownership, workflows, and decisions into the appropriate existing Type only when direct and high-confidence.
- Refresh Project state, questions, links, workflows, or guardrails when action changes affect them.
- Add a milestone only for a meaningful state transition and reconcile the human view when needed.
- Avoid broad cascades, preserve unrelated edits, review the diff, and push only with current explicit authorization.

Select this package by the requested vault role, not its name alone. Reuse rules and the complete Procedure already read in this session while they remain current; reread after a relevant change.
